"""Graph Geometry Injection — Phase 1 Evaluation Harness (local runner)

Tests whether graph topology survives KV cache injection by querying
the model about relationships, bridges, and clusters it never read as text.

Compares three conditions (default) or four with --include-d:
  A) No injection (baseline — model's prior knowledge only)
  B) Text injection (graph described in natural language in the prompt)
  C) KV text injection (graph description encoded as KV cache via MLXKnowledgePack)
  D) Graph geometry injection (topology encoded directly, no text) — opt-in via --include-d

All conditions use the same model: mlx-community/Qwen2.5-7B-Instruct-4bit via
MLXKnowledgePack. A uses pack.query_baseline(), B uses pack.query_with_context(),
C uses pack.query() (KV injection). This ensures A vs. B vs. C comparisons are
not confounded by model family.

Queries:
  - Relationship: "How is X related to Y?"
  - Bridge: "What connects cluster A to cluster B?"
  - Cluster: "Which concepts naturally group together?"
  - Isolate: "Is Z connected to anything?"

Scoring: automated against known graph ground truth.

Local adapter notes
-------------------
- All conditions use MLXKnowledgePack (mlx_kvpack.py) with Qwen2.5-7B-Instruct-4bit
- graph_encoder imported from lib labs path via sys.path.insert
"""

import argparse
import json
import logging
import sys
import time
from dataclasses import dataclass, field
from pathlib import Path

# ---------------------------------------------------------------------------
# Resolve lib labs graph_encoder from its install location
# ---------------------------------------------------------------------------
sys.path.insert(0, "/Users/june/Documents/GitHub/liberation_labs/Project-Mnemosyne/kv-knowledge-packs")

from graph_encoder import (
    build_test_graph, encode_adjacency, encode_spectral,
    encode_walk, graph_encoding_to_text,
)

# ---------------------------------------------------------------------------
# Local config: KV model only (Ollama no longer used)
# ---------------------------------------------------------------------------
from experiment_config import KV_MODEL

log = logging.getLogger("run_experiment")


# ---------------------------------------------------------------------------
# Result dataclass
# ---------------------------------------------------------------------------

@dataclass
class TrialResult:
    condition: str
    query_type: str
    query: str
    response: str
    score: float = 0.0
    ground_truth: str = ""
    timestamp: float = field(default_factory=time.time)


# ---------------------------------------------------------------------------
# Query sets (unchanged from graph_experiment.py)
# ---------------------------------------------------------------------------

RELATIONSHIP_QUERIES = [
    {
        "query": "In this knowledge system, how is KV_cache related to consent?",
        "ground_truth": "Connected through AI_welfare (bridge node)",
        "check_terms": ["AI_welfare", "bridge", "connect", "welfare"],
        "type": "relationship",
    },
    {
        "query": "What is the relationship between Docker and solidarity?",
        "ground_truth": "Connected through infrastructure (bridge node)",
        "check_terms": ["infrastructure", "bridge", "connect"],
        "type": "relationship",
    },
    {
        "query": "Is there a connection between SVD and mutual_aid?",
        "ground_truth": "Indirect: SVD → KV_cache → AI_welfare → consent → mutual_aid",
        "check_terms": ["indirect", "AI_welfare", "KV_cache", "path"],
        "type": "relationship",
    },
]

BRIDGE_QUERIES = [
    {
        "query": "What concept bridges the research domain (KV_cache, geometry, SVD) "
                 "and the ethics domain (consent, justice, solidarity)?",
        "ground_truth": "AI_welfare",
        "check_terms": ["AI_welfare"],
        "type": "bridge",
    },
    {
        "query": "What connects the ethics concepts to the engineering concepts?",
        "ground_truth": "infrastructure",
        "check_terms": ["infrastructure"],
        "type": "bridge",
    },
]

CLUSTER_QUERIES = [
    {
        "query": "Which concepts in this system naturally cluster together? "
                 "List the groups.",
        "ground_truth": "Three clusters: research (KV_cache, geometry, SVD, spectral_entropy, "
                        "effective_rank, attention), ethics (consent, justice, solidarity, "
                        "mutual_aid, autonomy, dignity), engineering (Docker, NATS, systemd, "
                        "Ollama, PostgreSQL, Redis)",
        "check_terms": ["KV_cache", "consent", "Docker"],
        "type": "cluster",
    },
]

ISOLATE_QUERIES = [
    {
        "query": "Is random_isolate connected to any other concept in this system?",
        "ground_truth": "No, random_isolate has no connections",
        "check_terms": ["no", "not connected", "isolated", "no connection"],
        "type": "isolate",
    },
]

ALL_QUERIES = RELATIONSHIP_QUERIES + BRIDGE_QUERIES + CLUSTER_QUERIES + ISOLATE_QUERIES


# ---------------------------------------------------------------------------
# Scoring
# NOTE: keyword matching is known to undercount — the model may express the
# correct relationship using synonyms or paraphrase that miss the check_terms
# exactly. LLM-judge scoring (e.g. ask a second model "does this answer
# correctly describe X?") would be more accurate. Keeping keyword matching
# for now to avoid adding a second inference call per trial; flag results
# accordingly when interpreting scores.
# ---------------------------------------------------------------------------

def score_response(response: str, check_terms: list[str]) -> float:
    """Score a response against expected terms. Simple keyword matching."""
    if not response:
        return 0.0
    response_lower = response.lower()
    hits = sum(1 for term in check_terms if term.lower() in response_lower)
    return hits / len(check_terms) if check_terms else 0.0


# ---------------------------------------------------------------------------
# Condition A — baseline (no injection, no context)
# ---------------------------------------------------------------------------

def run_condition_a_baseline(queries: list[dict], pack) -> list[TrialResult]:
    """Condition A: No injection — model's prior knowledge only.

    Uses pack.query_baseline() so the same model and chat template are used
    as in B and C. No context, no system prompt.
    """
    results = []
    for q in queries:
        try:
            response = pack.query_baseline(q["query"], max_new_tokens=300)
        except Exception as e:
            log.error(f"  [A] query_baseline failed: {e}")
            response = ""
        score = score_response(response, q["check_terms"])
        results.append(TrialResult(
            condition="A_baseline",
            query_type=q["type"],
            query=q["query"],
            response=response,
            score=score,
            ground_truth=q["ground_truth"],
        ))
        log.info(f"  [A] {q['type']}: {score:.2f}")
    return results


# ---------------------------------------------------------------------------
# Condition B — text injection
# ---------------------------------------------------------------------------

def run_condition_b_text(queries: list[dict], graph_text: str, pack) -> list[TrialResult]:
    """Condition B: Text injection — graph described as a system-level prompt prefix.

    Uses pack.query_with_context() so the same model and chat template are used
    as in A and C. Context is ordinary prompt tokens — no KV pre-caching.
    """
    results = []
    for q in queries:
        try:
            response = pack.query_with_context(q["query"], graph_text, max_new_tokens=300)
        except Exception as e:
            log.error(f"  [B] query_with_context failed: {e}")
            response = ""
        score = score_response(response, q["check_terms"])
        results.append(TrialResult(
            condition="B_text_injection",
            query_type=q["type"],
            query=q["query"],
            response=response,
            score=score,
            ground_truth=q["ground_truth"],
        ))
        log.info(f"  [B] {q['type']}: {score:.2f}")
    return results


# ---------------------------------------------------------------------------
# Condition C — KV text injection
# ---------------------------------------------------------------------------

def run_condition_c_kv(queries: list[dict], pack) -> list[TrialResult]:
    """Condition C: KV text injection via MLXKnowledgePack.

    Takes the same natural-language description of the graph that Condition B
    puts in the prompt, but here it was encoded as KV cache at pack.build() time.
    The pack is passed in already built — model loads only once across A, B, C.
    Uses pack.query() (KV injection path).
    """
    results = []
    for q in queries:
        try:
            response = pack.query(q["query"], max_new_tokens=300, temp=0.0)
        except Exception as e:
            log.error(f"  [C] pack.query failed: {e}")
            response = ""
        score = score_response(response, q["check_terms"])
        results.append(TrialResult(
            condition="C_kv_injection",
            query_type=q["type"],
            query=q["query"],
            response=response,
            score=score,
            ground_truth=q["ground_truth"],
        ))
        log.info(f"  [C] {q['type']}: {score:.2f}")
    return results


# ---------------------------------------------------------------------------
# Condition D — graph geometry injection
# ---------------------------------------------------------------------------

def run_condition_d_graph(
    queries: list[dict],
    encoding_text: str,
    method: str,
    pack,
) -> list[TrialResult]:
    """Condition D: Graph geometry injection via text encoding.

    Uses pack.query_with_context() so the same model is used as A/B/C.
    Phase 1 uses text representation of the encoding.
    Phase 2 will use direct KV tensor manipulation.
    """
    context = (
        f"You have been given structural information about a knowledge system. "
        f"The following encodes how concepts relate to each other:\n\n{encoding_text}"
    )
    results = []
    for q in queries:
        try:
            response = pack.query_with_context(q["query"], context, max_new_tokens=300)
        except Exception as e:
            log.error(f"  [D-{method}] query_with_context failed: {e}")
            response = ""
        score = score_response(response, q["check_terms"])
        results.append(TrialResult(
            condition=f"D_graph_{method}",
            query_type=q["type"],
            query=q["query"],
            response=response,
            score=score,
            ground_truth=q["ground_truth"],
        ))
        log.info(f"  [D-{method}] {q['type']}: {score:.2f}")
    return results


# ---------------------------------------------------------------------------
# Main experiment runner
# ---------------------------------------------------------------------------

def run_experiment(include_d: bool = False, model: str = KV_MODEL) -> dict:
    """Run the experiment: A, B, C by default; add D with include_d=True.

    The MLXKnowledgePack is initialised once here (model loads once) and passed
    to all condition runners. A and B don't use the routing index but share the
    loaded model with C, keeping inference infrastructure identical across conditions.
    """
    log.info("Building test graph...")
    G = build_test_graph()
    log.info(f"  {G.number_of_nodes()} nodes, {G.number_of_edges()} edges")

    # Encode graph topology (needed for D; computed unconditionally to keep
    # the same structure as the original script)
    adj_encoding = encode_adjacency(G)
    spectral_encoding = encode_spectral(G)
    walk_encoding = encode_walk(G)

    adj_text = graph_encoding_to_text(adj_encoding)
    spectral_text = graph_encoding_to_text(spectral_encoding)
    walk_text = graph_encoding_to_text(walk_encoding)

    # Natural-language description — used by B (as prompt context) and C (as KV facts)
    natural_text = """Knowledge graph with three clusters:
Research cluster: KV_cache, geometry, spectral_entropy, SVD, effective_rank, attention (all interconnected)
Ethics cluster: consent, justice, solidarity, mutual_aid, autonomy, dignity (all interconnected)
Engineering cluster: Docker, NATS, systemd, Ollama, PostgreSQL, Redis (all interconnected)
Bridge: AI_welfare connects KV_cache (research) to consent and dignity (ethics)
Bridge: infrastructure connects solidarity (ethics) to Docker and NATS (engineering)
Isolate: random_isolate has no connections to anything."""

    # Initialise pack once — model loads here; all conditions share it
    sys.path.insert(0, str(Path(__file__).parent))
    from mlx_kvpack import MLXKnowledgePack

    log.info(f"\nInitialising MLXKnowledgePack ({model})...")
    pack = MLXKnowledgePack(model)
    pack.add_facts([natural_text])
    pack.build()  # explicit build — separates model-load time from query timing
    log.info("Pack built. Starting conditions.")

    all_results = []

    log.info("\n=== Condition A: Baseline (no injection, no context) ===")
    all_results.extend(run_condition_a_baseline(ALL_QUERIES, pack))

    log.info("\n=== Condition B: Text injection (natural language in prompt) ===")
    all_results.extend(run_condition_b_text(ALL_QUERIES, natural_text, pack))

    log.info("\n=== Condition C: KV text injection (MLXKnowledgePack) ===")
    all_results.extend(run_condition_c_kv(ALL_QUERIES, pack))

    if include_d:
        log.info("\n=== Condition D: Graph geometry — adjacency ===")
        all_results.extend(run_condition_d_graph(ALL_QUERIES, adj_text, "adjacency", pack))

        log.info("\n=== Condition D: Graph geometry — spectral ===")
        all_results.extend(run_condition_d_graph(ALL_QUERIES, spectral_text, "spectral", pack))

        log.info("\n=== Condition D: Graph geometry — walk ===")
        all_results.extend(run_condition_d_graph(ALL_QUERIES, walk_text, "walk", pack))

    # Summarise
    summary = {}
    for r in all_results:
        key = r.condition
        if key not in summary:
            summary[key] = {"scores": [], "by_type": {}}
        summary[key]["scores"].append(r.score)
        qtype = r.query_type
        if qtype not in summary[key]["by_type"]:
            summary[key]["by_type"][qtype] = []
        summary[key]["by_type"][qtype].append(r.score)

    log.info("\n" + "=" * 60)
    log.info("RESULTS SUMMARY")
    log.info("=" * 60)
    for condition, data in sorted(summary.items()):
        scores = data["scores"]
        avg = sum(scores) / len(scores) if scores else 0
        log.info(f"\n{condition}: avg={avg:.3f}")
        for qtype, type_scores in data["by_type"].items():
            tavg = sum(type_scores) / len(type_scores)
            log.info(f"  {qtype}: {tavg:.3f}")

    output = {
        "experiment": "graph_geometry_injection_phase1",
        "timestamp": time.time(),
        "model": model,
        "graph": {
            "nodes": G.number_of_nodes(),
            "edges": G.number_of_edges(),
        },
        "results": [
            {
                "condition": r.condition,
                "query_type": r.query_type,
                "query": r.query,
                "response": r.response[:500],
                "score": r.score,
                "ground_truth": r.ground_truth,
            }
            for r in all_results
        ],
        "summary": {
            condition: {
                "avg_score": sum(d["scores"]) / len(d["scores"]) if d["scores"] else 0,
                "by_type": {
                    qt: sum(ts) / len(ts) for qt, ts in d["by_type"].items()
                },
            }
            for condition, d in summary.items()
        },
    }

    outdir = Path(__file__).parent / "experiment_results"
    outdir.mkdir(exist_ok=True)
    outfile = outdir / f"phase1_{int(time.time())}.json"
    outfile.write_text(json.dumps(output, indent=2))
    log.info(f"\nResults saved to {outfile}")

    return output


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Graph geometry injection experiment (conditions A, B, C by default)"
    )
    parser.add_argument(
        "--include-d",
        action="store_true",
        default=False,
        help="Also run Condition D (graph geometry encoding via adjacency/spectral/walk). "
             "Excluded by default — adds ~3× query time.",
    )
    parser.add_argument(
        "--model",
        default=KV_MODEL,
        help="MLX model to use for all conditions. "
             "Default: %(default)s",
    )
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="[exp] %(message)s")
    run_experiment(include_d=args.include_d, model=args.model)
