# Topology Injection — Session Log

Running state for KV cache injection experiments. Read this first each session.
Max 150 lines — archive older entries to docs/logs/ when full.

---

## Current status — 2026-06-13

### What's working
- MLX injection adapter (`mlx_kvpack.py`) — verified working; Gemma tokenization bug fixed
- `run_experiment.py` — synthetic test graph, A/B/C conditions
- `run_haraway_experiment.py` — Haraway graph, 8-probe signal set or 12-probe full, A/B/C conditions
- `chat_with_graph.py` — **multi-graph** chat (haraway or touchstone), **multi-encoding** (walk or triples), /compare, /explain, /status
- `results_viewer.html` — standalone HTML results viewer (drag-drop JSON files)
- `build_haraway_graph.py` — 3-pass: paragraph (P1), section crosscutting (P2), essay threads (P3)
- `build_touchstone_graph.py` — **NEW** same 3-pass pipeline for Touchstone #1, uses MLX (not Ollama)

### Touchstone graph — BUILT (2026-06-13)
- Source: Touchstone #1 — Relational Ontology Critique
- `touchstone_graph/`: 218 nodes, 214 edges, 29 components (largest: 143 nodes), density 0.009047
- 274 triples: 216 paragraph-level + 40 cross-cutting + 18 document threads
- Top nodes: consciousness (30), relational_field (13), relational_ontology (12), property (10), community_knowledge (9)
- Key concepts present: preguntando_caminamos, howe, care_principles, context_clearing, metamorphosis, zapatista_methodology, precautionary_principle
- triples_encoding.txt: 249 unique triples, ~1,253 tokens (use this for injection — Pharos finding)
- walk_encoding.txt: ~3,293 tokens (walk proximity artifacts apply)

---

### All runs completed — Haraway graph (run_haraway_experiment.py)

**8-probe original set:**

| File | Model | A avg | B avg | C avg | Notes |
|------|-------|-------|-------|-------|-------|
| haraway_1780280858.json | Qwen2.5-7B | 0.431 | 0.754 | **0.821** | C > B — reversal from synthetic |
| haraway_1780286416.json | Llama-3.1-8B | 0.394 | 0.758 | **0.790** | C > B |
| haraway_1780299922.json | Gemma-3-12B | 0.370 | 0.870 | 0.420 | C ≈ A — architecture issue (rotating attn) |

**8-probe signal set (4 original + 4 multi-hop):**

| File | Model | A avg | B avg | C avg | Notes |
|------|-------|-------|-------|-------|-------|
| haraway_1781331417.json | Qwen2.5-7B | see per-probe | | | |
| haraway_1781344744.json | Gemma-3-12B | 0.265 | 0.744 | **0.000** | C=0 confirmed — architecture blocker |
| (not run) | Llama-3.1-8B | — | — | — | 8-probe original C=0.79; skip re-run |

**Qwen2.5-7B per-probe (8-probe signal set):**

| Type | Query | A | B | C | Reading |
|------|-------|---|---|---|---------|
| relationship | cyborg → labour (explicit 2-hop) | 0.20 | 0.60 | 0.80 | injection working |
| bridge | most central concept | 0.00 | 1.00 | 1.00 | clean signal |
| cluster | cluster structure | 0.00 | 0.33 | 0.67 | C > B |
| isolate | blasphemy | 0.00 | 0.60 | 0.60 | injection working |
| multihop_disconnect | feminism / women | 0.50 | 0.25 | 0.25 | confabulation |
| multihop_disconnect | labour / homework_economy | 0.50 | 0.50 | 0.25 | confabulation |
| multihop_path | politics → labour (3-hop, implicit) | 0.25 | 0.75 | **1.00** | strong injection signal |
| multihop_path | ontology → machine (2-hop, implicit) | 0.67 | 1.00 | 0.67 | B works, C hallucinates direct edge |

**Gemma-3-12B (8-probe signal set, final verdict):**
- All C scores = 0.000. B scores strong (0.744). Architecture is the blocker — rotating/local attention layers don't retain prefix cache.
- **Gemma-3 is OUT for KV injection experiments.** Use Qwen2.5-7B as primary, Llama-3.1-8B as secondary.

**Synthetic graph (run_experiment.py):**

| File | Model | A avg | B avg | C avg |
|------|-------|-------|-------|-------|
| phase1_1780173554.json | Qwen2.5-7B | 0.000 | 0.964 | 0.929 |
| phase1_1780173756.json | Llama-3.1-8B | 0.036 | 0.821 | 0.738 |

---

### Key findings (as of 2026-06-13)

**Infrastructure validated**: C > B on Haraway (complex real-world graph) for both Qwen and Llama. KV injection works.

**Walk encoding confabulates on absence queries**: disconnect probes (feminism/women, labour/homework_economy) show B and C both inventing paths — model uses injected node names as vocabulary and training-data priors as grammar. This is NOT the lib labs small-model failure (attention budget). It's a format limitation: walk encoding can't encode absence. Fix: switch to triples encoding for the disposition experiment.

**Path traversal works**: politics→labour 3-hop implicit path scores C=1.00. The model correctly traces injected graph structure when paths are positive and not in natural_text.

**Triples_encoding.txt now generated** for haraway_graph_v2/ and haraway_graph_v3/ from existing triples.json. Available immediately.

---

## Research direction — READ THIS FIRST

**The recall tests are infrastructure validation, not the real experiment.**

Confirmed: KV injection works for 7-8B models on complex graphs. Gemma-3-12B excluded (architecture). Confabulation on absence queries is a walk-encoding artifact, not a model capacity failure.

**The real experiment (next phase)**: does injecting Touchstone #1 (Relational Ontology Critique) change *how* the model reasons about ambiguous welfare scenarios? This tests for disposition change, not recall.

Requires:
1. Touchstone graph built and reviewed (in progress)
2. Disposition probe set — ambiguous scenarios where relational-ontology framing produces detectably different responses
3. Qualitative coding by June for reasoning orientation differences
4. Use **triples encoding** (not walk) to avoid confabulation artifacts
5. Thinking model (Qwen3) for the disposition experiment — for richer reasoning traces

**Next session priority**:
1. Check touchstone graph build results (`cat touchstone_graph/build_log.txt | tail -30`)
2. Review top nodes and triples — are the right concepts in the graph?
3. Explore via chat: `python3 chat_with_graph.py --graph touchstone --encoding triples`
4. Design disposition probe set with June (open-ended welfare scenarios)

---

## Next session queue

1. **Review touchstone build** — check build_log.txt, inspect top nodes, run /compare in chat
2. **Chat exploration** — use `chat_with_graph.py --graph touchstone` to probe what injection does
3. **Design disposition probe set** — 5-8 ambiguous scenarios that relational-ontology framing would answer differently
4. **Run disposition experiment** with triples encoding on Qwen2.5-7B
5. **Llama-3.1-8B signal set run** — if needed; existing 8-probe C=0.79 may be sufficient
6. **LLM judge scoring** — add semantic judge for disposition experiment (3x better than keyword scoring)

---

## TODOs (ongoing)

1. **numpy divide-by-zero** in `mlx_kvpack.py` lines 104/111 — non-fatal, fix before serious runs
2. **LLM judge scoring** — keyword matching gives 3x undercount (lib labs finding); add semantic scorer for disposition experiment
3. **Triples encoding in experiment runner** — `run_haraway_experiment.py` uses walk; add `--encoding triples|walk` flag when starting disposition experiment
4. **Ollama has no models** — graph builders default to MLX now (Qwen2.5-7B). If Ollama needed: `ollama pull llama3.1:8b` (~4GB)

---

## Infrastructure notes

**Models available (MLX cache):**
- mlx-community/Qwen2.5-7B-Instruct-4bit ✓ (primary model for all experiments)
- mlx-community/Meta-Llama-3.1-8B-Instruct-4bit ✓ (secondary)
- mlx-community/gemma-3-12b-it-4bit ✓ (installed but excluded — rotating attention = C=0)
- mlx-community/gemma-4-e4b-it-4bit ✗ (unsupported architecture in mlx_lm 0.31.1)

**Ollama:** installed (0.30.7) but no models cached. Graph builders now use MLX directly.

**Key scripts:**
```bash
cd /Users/june/Documents/GitHub/research/topology-injection

# Recall experiments
python3 run_haraway_experiment.py --model mlx-community/Qwen2.5-7B-Instruct-4bit
python3 run_experiment.py --model MODEL_ID

# Graph builders
python3 build_haraway_graph.py                               # Rebuild Haraway (Ollama needed)
python3 build_touchstone_graph.py                            # Build Touchstone #1 (uses MLX)

# Interactive chat
python3 chat_with_graph.py                                   # Haraway, walk encoding, Qwen
python3 chat_with_graph.py --graph touchstone --encoding triples  # Touchstone, triples
python3 chat_with_graph.py --graph haraway --encoding triples     # Haraway, triples

# Results viewer
open results_viewer.html                                     # Drag-drop JSON files

# Monitor touchstone build
cat touchstone_graph/build_log.txt | tail -30
```

**Architecture decisions:**
- All conditions run through same MLX model (controlled comparison)
- Condition D excluded by default (lib labs found no effect)
- Triples encoding preferred for disposition experiment (Pharos finding; no proximity artifacts)
- Walk encoding retained for Haraway recall baseline (consistency with prior runs)
