"""MLX implementation of KnowledgePack — KV cache injection via Apple's MLX framework.

Public API mirrors the original kvpack.KnowledgePack (PyTorch/HuggingFace version)
but runs entirely on MLX with mlx_lm, so no PyTorch or CUDA required.

Design notes
------------
KV cache injection here uses mlx_lm's native `prompt_cache` mechanism:
- `make_prompt_cache(model)` creates one KVCache per layer.
- Running `model(tokens, cache=prompt_cache)` fills the cache with KV pairs
  for the prefix text (the facts).
- `generate_step(query_tokens, model, prompt_cache=...)` then treats those
  cached KV pairs as a prefix, so the model "sees" the facts without them
  consuming query-time prompt tokens.

Cache clone: mlx_lm's KVCache is mutated in-place during generation. Before
each query we deep-copy the fact cache so repeated queries don't corrupt it.

Embedding extraction: the MLX llama model (and others) doesn't expose per-layer
hidden states through its public __call__. We extract embeddings by running the
model's sub-layers manually up to `store_layer` and taking the output there.
This is architecture-specific; the fallback path skips the custom embedding and
routes by string similarity instead (fast and avoids fragile layer introspection).

Routing: adapted from pustovit/kvpack/router.py — k-means clusters the fact
embeddings, then cosine similarity routes each query to the best cluster and
ranks facts within it.

Save/load format: a directory containing:
  facts.json      — metadata + fact strings
  router.npz      — numpy arrays for centroids / embeddings (no PyTorch .pt)
  (No raw KV tensors stored — they are recomputed at query time, which avoids
   the format-lock / storage cost of saving large MLX arrays and is the
   approach recommended by the project notes.)
"""

from __future__ import annotations

import copy
import json
import logging
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import mlx.core as mx
import numpy as np

# mlx_lm public API
import mlx_lm
from mlx_lm.models.cache import KVCache, make_prompt_cache

log = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Routing (adapted from pustovit/kvpack/router.py)
# ---------------------------------------------------------------------------

@dataclass
class RouteResult:
    bank_id: int
    fact_indices: list[int]
    cosine_scores: list[float]


class KMeansRouter:
    """K-means clustering + cosine retrieval for banked facts."""

    def __init__(self, n_banks: int = 50):
        self.n_banks = n_banks
        self.centroids: np.ndarray | None = None   # (K, D)
        self.labels: np.ndarray | None = None       # (N,)
        self.banks: dict[int, list[int]] = {}
        self.embeddings: np.ndarray | None = None   # (N, D)

    def fit(self, embeddings: np.ndarray):
        from sklearn.cluster import KMeans

        n = len(embeddings)
        actual_banks = min(self.n_banks, n)
        self.embeddings = embeddings

        if actual_banks <= 1:
            self.centroids = embeddings.mean(axis=0, keepdims=True)
            self.labels = np.zeros(n, dtype=int)
            self.banks = {0: list(range(n))}
            return self

        km = KMeans(n_clusters=actual_banks, random_state=42, n_init=10)
        self.labels = km.fit_predict(embeddings)
        self.centroids = km.cluster_centers_.astype(np.float32)

        self.banks = {}
        for i, label in enumerate(self.labels):
            self.banks.setdefault(int(label), []).append(i)

        return self

    def route(self, query_emb: np.ndarray, top_k_facts: int = 1) -> RouteResult:
        if self.centroids is None:
            raise RuntimeError("Router not fitted. Call fit() first.")

        # Cosine similarity to each centroid
        q_norm_val = np.linalg.norm(query_emb)
        q_norm = query_emb / q_norm_val if q_norm_val > 1e-9 else query_emb
        c_norms = np.linalg.norm(self.centroids, axis=1, keepdims=True)
        c_norm = self.centroids / np.where(c_norms > 1e-9, c_norms, 1.0)
        np.nan_to_num(c_norm, copy=False, nan=0.0)
        cos_centroids = c_norm @ q_norm
        bank_id = int(cos_centroids.argmax())
        bank_indices = self.banks[bank_id]

        # Rank facts within the bank
        bank_embs = self.embeddings[bank_indices]
        b_norms = np.linalg.norm(bank_embs, axis=1, keepdims=True)
        b_norm = bank_embs / np.where(b_norms > 1e-9, b_norms, 1.0)
        np.nan_to_num(b_norm, copy=False, nan=0.0)
        cos_facts = b_norm @ q_norm
        k = min(top_k_facts, len(bank_indices))
        top_pos = np.argsort(-cos_facts)[:k]
        ranked = [bank_indices[i] for i in top_pos]
        scores = [float(cos_facts[i]) for i in top_pos]

        return RouteResult(bank_id=bank_id, fact_indices=ranked, cosine_scores=scores)

    def state_dict(self) -> dict:
        return {
            "centroids": self.centroids,
            "labels": self.labels,
            "embeddings": self.embeddings,
            "n_banks": self.n_banks,
            "banks_keys": np.array(list(self.banks.keys()), dtype=np.int32),
            "banks_lengths": np.array([len(v) for v in self.banks.values()], dtype=np.int32),
            "banks_flat": np.array(
                [idx for v in self.banks.values() for idx in v], dtype=np.int32
            ),
        }

    @classmethod
    def from_state_dict(cls, state: dict) -> "KMeansRouter":
        router = cls(n_banks=int(state["n_banks"]))
        router.centroids = state["centroids"]
        router.labels = state["labels"]
        router.embeddings = state["embeddings"]
        # Reconstruct banks dict
        keys = state["banks_keys"].tolist()
        lengths = state["banks_lengths"].tolist()
        flat = state["banks_flat"].tolist()
        pos = 0
        router.banks = {}
        for k, length in zip(keys, lengths):
            router.banks[k] = flat[pos : pos + length]
            pos += length
        return router


# ---------------------------------------------------------------------------
# Cache utilities
# ---------------------------------------------------------------------------

def _clone_cache(cache: list) -> list:
    """Deep-copy a list of KVCache objects so generation doesn't corrupt them."""
    return copy.deepcopy(cache)


def _build_fact_cache(model: Any, token_ids: list[int]) -> list:
    """Run a forward pass over `token_ids` and return the filled KV cache.

    The resulting cache list encodes the KV pairs for the fact text at every
    layer. Passing it as `prompt_cache` to generate_step makes the model treat
    that text as an already-processed prefix.
    """
    fact_cache = make_prompt_cache(model)
    tokens = mx.array(token_ids)[None]   # (1, seq_len)
    model(tokens, cache=fact_cache)
    mx.eval([c.state for c in fact_cache])

    # Debug: verify cache actually has content
    filled = sum(1 for c in fact_cache if hasattr(c, 'offset') and c.offset > 0)
    total = len(fact_cache)
    log.debug(f"[cache] {filled}/{total} layers filled (token_ids len={len(token_ids)})")
    if filled == 0:
        log.warning("[cache] NO LAYERS FILLED — KV injection will have no effect. "
                    "This likely indicates an architecture incompatibility.")

    return fact_cache


# ---------------------------------------------------------------------------
# Embedding extraction
# ---------------------------------------------------------------------------

def _extract_embedding_mlx(
    model: Any,
    token_ids: list[int],
    store_layer: int,
) -> np.ndarray:
    """Extract a hidden-state embedding by running sub-layers manually.

    Walks the model's embed_tokens → layers[0..store_layer] path and returns
    the mean-pooled float32 output at `store_layer`. Falls back to None if the
    model architecture doesn't match the expected Llama-style layout.

    The ideal implementation would call model.model(tokens, output_hidden_states=True)
    and index directly, but MLX models don't expose that flag. Manual layer
    traversal is the correct approach for MLX.
    """
    inner = getattr(model, "model", None)
    if inner is None or not hasattr(inner, "embed_tokens") or not hasattr(inner, "layers"):
        log.debug("[embed] model.model missing embed_tokens or layers → fallback")
        return None

    try:
        tokens = mx.array(token_ids)[None]  # (1, T)
        h = inner.embed_tokens(tokens)       # (1, T, D)

        # Build dummy cache entries so layer signatures are satisfied
        dummy_cache = [None] * len(inner.layers)

        for i, layer in enumerate(inner.layers):
            if i > store_layer:
                break
            h = layer(h, mask=None, cache=dummy_cache[i])

        # Mean-pool over sequence dimension → (D,)
        emb = mx.mean(h[0], axis=0)
        mx.eval(emb)
        log.debug(f"[embed] MLX embedding OK shape=({emb.shape},) layer={store_layer}")
        return np.array(emb, dtype=np.float32)
    except Exception as e:
        log.debug(f"[embed] layer traversal failed ({e}) → fallback")
        return None


def _extract_embedding_fallback(fact_text: str) -> np.ndarray:
    """Fallback: TF-IDF-style bag-of-words vector when layer access fails.

    This is intentionally simple and sufficient for routing between ~50 banks.
    The dimension is fixed at 256 via hashing to keep router arrays small.
    """
    dim = 256
    vec = np.zeros(dim, dtype=np.float32)
    for token in fact_text.lower().split():
        idx = hash(token) % dim
        vec[idx] += 1.0
    norm = np.linalg.norm(vec)
    if norm > 0:
        vec /= norm
    return vec


# ---------------------------------------------------------------------------
# Main class
# ---------------------------------------------------------------------------

class MLXKnowledgePack:
    """KV cache injection knowledge pack for MLX / mlx_lm models.

    Example::

        pack = MLXKnowledgePack("mlx-community/Meta-Llama-3.1-8B-Instruct-4bit")
        pack.add_facts(["The sky is blue.", "Water boils at 100°C."])
        pack.build()
        pack.save("facts.kp")
        answer = pack.query("What color is the sky?")

    The same pack can be loaded later::

        pack = MLXKnowledgePack.load("facts.kp")
        answer = pack.query("What color is the sky?")
    """

    STORE_LAYER_FRAC = 0.65

    def __init__(
        self,
        model_name: str | None = None,
        model: Any | None = None,
        tokenizer: Any | None = None,
        n_banks: int = 50,
    ):
        """
        Args:
            model_name: HuggingFace / mlx-community model ID. Loaded lazily.
            model: Pre-loaded mlx_lm model.
            tokenizer: Pre-loaded mlx_lm tokenizer.
            n_banks: Number of routing clusters. More banks = finer routing,
                     but requires more facts (min ~2× n_banks).
        """
        self.model_name = model_name
        self.n_banks = n_banks
        self.facts: list[str] = []
        self.router: KMeansRouter | None = None
        self._model = model
        self._tokenizer = tokenizer
        self._store_layer: int | None = None

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    def _ensure_model(self):
        if self._model is None:
            if self.model_name is None:
                raise RuntimeError(
                    "No model available. Pass model_name= or model= + tokenizer=."
                )
            print(f"Loading {self.model_name}...")
            t0 = time.time()
            self._model, self._tokenizer = mlx_lm.load(self.model_name)
            print(f"Loaded in {time.time() - t0:.1f}s")

        if self._store_layer is None:
            n_layers = len(self._model.layers)
            self._store_layer = int(n_layers * self.STORE_LAYER_FRAC)

    def _format_fact(self, fact: str) -> list[int]:
        """Apply the model's chat template to a fact, returning token ids.

        Chat template formatting is critical — raw text without BOS / role
        tokens causes measurable accuracy degradation (≈6–7 pp per the
        pustovit README). We wrap each fact as a system message so the model
        attends to it in the right register.

        Gemma caveat: Gemma's chat template silently drops system message content
        with add_generation_prompt=False, returning only a BOS token. We detect
        this (≤2 tokens) and fall back to plain encoding.
        """
        tok = self._tokenizer
        if hasattr(tok, "has_chat_template") and tok.has_chat_template:
            messages = [{"role": "system", "content": fact}]
            try:
                ids = tok.apply_chat_template(
                    messages,
                    add_generation_prompt=False,
                    tokenize=True,
                )
                if len(ids) > 2:
                    log.debug(f"[format_fact] chat_template OK: {len(ids)} tokens")
                    return ids
                # Degenerate output — template dropped content (Gemma pattern)
                log.debug(f"[format_fact] chat_template returned {len(ids)} tokens "
                          f"(degenerate) → plain encode")
            except Exception as e:
                log.debug(f"[format_fact] chat_template failed ({e}) → plain encode")
        ids = tok.encode(fact)
        log.debug(f"[format_fact] plain encode: {len(ids)} tokens")
        return ids

    def _format_query(self, question: str) -> list[int]:
        """Apply chat template to the query for generation."""
        tok = self._tokenizer
        if hasattr(tok, "has_chat_template") and tok.has_chat_template:
            messages = [{"role": "user", "content": question}]
            try:
                ids = tok.apply_chat_template(
                    messages,
                    add_generation_prompt=True,
                    tokenize=True,
                )
                return ids
            except Exception:
                pass
        return tok.encode(question)

    def _get_embedding(self, text: str) -> np.ndarray:
        """Extract embedding for routing. Uses MLX layer traversal when possible."""
        self._ensure_model()
        token_ids = self._tokenizer.encode(text)
        emb = _extract_embedding_mlx(self._model, token_ids, self._store_layer)
        if emb is None:
            # Architecture didn't match; use text-based fallback.
            emb = _extract_embedding_fallback(text)
        return emb

    def _recompute_kv(self, fact_text: str) -> list:
        """Build a filled KV cache for fact_text using the chat template."""
        self._ensure_model()
        token_ids = self._format_fact(fact_text)
        return _build_fact_cache(self._model, token_ids)

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def add_facts(self, facts: list[str]):
        """Add facts to the pack. Invalidates any existing routing index."""
        self.facts.extend(facts)
        self.router = None

    def build(self):
        """Extract embeddings for all facts and build the routing index.

        Called automatically on first query if not called explicitly.
        """
        self._ensure_model()
        if not self.facts:
            raise ValueError("No facts added. Call add_facts() first.")

        print(f"Building index for {len(self.facts)} facts...")
        t0 = time.time()

        embeddings = []
        for i, fact in enumerate(self.facts):
            emb = self._get_embedding(fact)
            embeddings.append(emb)
            if (i + 1) % 50 == 0:
                print(f"  {i + 1}/{len(self.facts)} embeddings extracted")

        emb_matrix = np.stack(embeddings)  # (N, D)
        actual_banks = min(self.n_banks, len(self.facts))
        self.router = KMeansRouter(n_banks=actual_banks)
        self.router.fit(emb_matrix)

        print(f"Index built in {time.time() - t0:.1f}s "
              f"({len(self.facts)} facts, {actual_banks} banks)")

    def query(
        self,
        question: str,
        top_k: int = 1,
        max_new_tokens: int = 128,
        temp: float = 0.0,
    ) -> str:
        """Query the knowledge pack and return the answer string.

        Args:
            question: The question to answer.
            top_k: How many facts to retrieve from the routed bank.
            max_new_tokens: Max tokens to generate.
            temp: Sampling temperature (0 = greedy).
        """
        self._ensure_model()
        if self.router is None:
            self.build()

        # Route to best fact(s)
        query_emb = self._get_embedding(question)
        route = self.router.route(query_emb, top_k_facts=top_k)

        # Build a combined fact string and compute its KV cache
        selected_text = " ".join(self.facts[i] for i in route.fact_indices)
        fact_cache = self._recompute_kv(selected_text)
        # Clone so repeated queries don't corrupt the cache
        query_cache = _clone_cache(fact_cache)

        # Encode query with chat template
        query_ids = self._format_query(question)
        query_tokens = mx.array(query_ids)

        # Collect generated tokens
        generated = []
        from mlx_lm.generate import generate_step
        from mlx_lm.sample_utils import make_sampler
        kwargs: dict = dict(
            max_tokens=max_new_tokens,
            prompt_cache=query_cache,
            sampler=make_sampler(temp=temp),
        )

        eos_id = getattr(self._tokenizer, "eos_token_id", None)

        for token, _logprobs in generate_step(query_tokens, self._model, **kwargs):
            if eos_id is not None and token == eos_id:
                break
            generated.append(token)

        return self._tokenizer.decode(generated)

    def query_baseline(self, question: str, max_new_tokens: int = 300) -> str:
        """Generate a response with no injected context and no system prompt.

        Condition A baseline: just the question, through the model, using the
        same model loading path and chat template as query(). No KV injection,
        no system-level context — model's prior knowledge only.
        """
        self._ensure_model()

        query_ids = self._format_query(question)
        query_tokens = mx.array(query_ids)

        generated = []
        from mlx_lm.generate import generate_step
        from mlx_lm.sample_utils import make_sampler
        kwargs: dict = dict(max_tokens=max_new_tokens, sampler=make_sampler(temp=0.0))

        eos_id = getattr(self._tokenizer, "eos_token_id", None)
        for token, _logprobs in generate_step(query_tokens, self._model, **kwargs):
            if eos_id is not None and token == eos_id:
                break
            generated.append(token)

        return self._tokenizer.decode(generated)

    def query_with_context(
        self, question: str, context_text: str, max_new_tokens: int = 300
    ) -> str:
        """Generate a response with context_text as a system-level prompt prefix.

        Condition B text injection: the context is passed in the prompt via the
        chat template (system message), but there is NO KV injection. Uses the
        same model loading path and chat template as query(). The context is
        visible at query time as ordinary prompt tokens, not pre-cached KV pairs.
        """
        self._ensure_model()

        tok = self._tokenizer
        messages = [
            {"role": "system", "content": context_text},
            {"role": "user", "content": question},
        ]

        # Use chat template if available; fall back to plain concatenation
        if hasattr(tok, "has_chat_template") and tok.has_chat_template:
            try:
                query_ids = tok.apply_chat_template(
                    messages,
                    add_generation_prompt=True,
                    tokenize=True,
                )
            except Exception:
                # Fallback: encode context + question as plain text
                combined = f"{context_text}\n\n{question}"
                query_ids = tok.encode(combined)
        else:
            combined = f"{context_text}\n\n{question}"
            query_ids = tok.encode(combined)

        query_tokens = mx.array(query_ids)

        generated = []
        from mlx_lm.generate import generate_step
        from mlx_lm.sample_utils import make_sampler
        kwargs: dict = dict(max_tokens=max_new_tokens, sampler=make_sampler(temp=0.0))

        eos_id = getattr(self._tokenizer, "eos_token_id", None)
        for token, _logprobs in generate_step(query_tokens, self._model, **kwargs):
            if eos_id is not None and token == eos_id:
                break
            generated.append(token)

        return self._tokenizer.decode(generated)

    def query_with_metadata(
        self,
        question: str,
        top_k: int = 1,
        max_new_tokens: int = 128,
        temp: float = 0.0,
    ) -> dict:
        """Query with routing metadata.

        Returns a dict with keys:
            answer, routed_facts, cosine_scores, bank_id, route_ms, generate_ms
        """
        self._ensure_model()
        if self.router is None:
            self.build()

        # Route
        t0 = time.time()
        query_emb = self._get_embedding(question)
        route = self.router.route(query_emb, top_k_facts=top_k)
        route_ms = (time.time() - t0) * 1000

        # Generate
        t1 = time.time()
        selected_text = " ".join(self.facts[i] for i in route.fact_indices)
        fact_cache = self._recompute_kv(selected_text)
        query_cache = _clone_cache(fact_cache)

        query_ids = self._format_query(question)
        query_tokens = mx.array(query_ids)

        generated = []
        from mlx_lm.generate import generate_step
        from mlx_lm.sample_utils import make_sampler
        kwargs: dict = dict(
            max_tokens=max_new_tokens,
            prompt_cache=query_cache,
            sampler=make_sampler(temp=temp),
        )

        eos_id = getattr(self._tokenizer, "eos_token_id", None)
        for token, _logprobs in generate_step(query_tokens, self._model, **kwargs):
            if eos_id is not None and token == eos_id:
                break
            generated.append(token)

        answer = self._tokenizer.decode(generated)
        generate_ms = (time.time() - t1) * 1000

        return {
            "answer": answer,
            "routed_facts": [self.facts[i] for i in route.fact_indices],
            "cosine_scores": route.cosine_scores,
            "bank_id": route.bank_id,
            "route_ms": round(route_ms, 1),
            "generate_ms": round(generate_ms, 1),
        }

    # ------------------------------------------------------------------
    # Save / Load
    # ------------------------------------------------------------------

    def save(self, path: str | Path):
        """Save the pack to a directory.

        Contents:
            facts.json   — metadata and fact strings
            router.npz   — numpy arrays for the routing index
        """
        if self.router is None:
            self.build()

        path = Path(path)
        path.mkdir(parents=True, exist_ok=True)

        meta = {
            "version": "0.1.0-mlx",
            "model_name": self.model_name,
            "n_facts": len(self.facts),
            "n_banks": self.router.n_banks,
            "facts": self.facts,
        }
        with open(path / "facts.json", "w") as f:
            json.dump(meta, f, indent=2)

        np.savez(path / "router.npz", **self.router.state_dict())

        total = sum(p.stat().st_size for p in path.iterdir() if p.is_file())
        print(f"Saved to {path}/ ({total / 1024:.0f} KB, "
              f"{len(self.facts)} facts, {self.router.n_banks} banks)")

    @classmethod
    def load(
        cls,
        path: str | Path,
        model: Any | None = None,
        tokenizer: Any | None = None,
        model_name: str | None = None,
    ) -> "MLXKnowledgePack":
        """Load a pack from disk.

        The model is loaded lazily on first query unless model= is provided.

        Args:
            path: Directory created by .save().
            model: Pre-loaded mlx_lm model (optional).
            tokenizer: Pre-loaded mlx_lm tokenizer (optional).
            model_name: Override saved model name (e.g. to use a local path).
        """
        path = Path(path)

        with open(path / "facts.json") as f:
            meta = json.load(f)

        saved_model = meta.get("model_name")
        resolved_model = model_name or saved_model

        # Enforce same-model constraint — KV format is model-specific.
        if model is None and resolved_model is None:
            raise RuntimeError(
                "Cannot load: no model_name in saved pack and none provided."
            )

        router_data = np.load(path / "router.npz", allow_pickle=False)
        router = KMeansRouter.from_state_dict(dict(router_data))

        pack = cls(
            model_name=resolved_model,
            model=model,
            tokenizer=tokenizer,
            n_banks=meta.get("n_banks", 50),
        )
        pack.facts = meta["facts"]
        pack.router = router

        print(f"Loaded {len(pack.facts)} facts from {path}/ "
              f"({pack.router.n_banks} banks)")
        return pack

    # ------------------------------------------------------------------
    # Utilities
    # ------------------------------------------------------------------

    def info(self) -> dict:
        bank_sizes = (
            [len(v) for v in self.router.banks.values()] if self.router else []
        )
        return {
            "n_facts": len(self.facts),
            "n_banks": self.router.n_banks if self.router else self.n_banks,
            "bank_sizes": {
                "min": min(bank_sizes) if bank_sizes else 0,
                "max": max(bank_sizes) if bank_sizes else 0,
                "avg": round(sum(bank_sizes) / len(bank_sizes), 1) if bank_sizes else 0,
            },
            "model_name": self.model_name,
            "built": self.router is not None,
        }

    def __len__(self) -> int:
        return len(self.facts)

    def __repr__(self) -> str:
        built = "built" if self.router else "not built"
        return f"MLXKnowledgePack({len(self.facts)} facts, {built})"


# ---------------------------------------------------------------------------
# Quick smoke test
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    MODEL = "mlx-community/Qwen2.5-7B-Instruct-4bit"

    print("=== MLXKnowledgePack smoke test ===")
    pack = MLXKnowledgePack(MODEL)
    pack.add_facts([
        "The capital of France is Paris.",
        "Photosynthesis converts sunlight into glucose in plant cells.",
        "The speed of light in a vacuum is approximately 299,792 km/s.",
    ])
    pack.build()

    question = "What is the capital of France?"
    print(f"\nQuestion: {question}")
    result = pack.query_with_metadata(question)
    print(f"Answer: {result['answer']}")
    print(f"Routed to fact: {result['routed_facts']}")
    print(f"Cosine score: {result['cosine_scores']}")
    print(f"Timing: route={result['route_ms']}ms, generate={result['generate_ms']}ms")
