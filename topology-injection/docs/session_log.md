# Topology Injection — Session Log

Running state for KV cache injection experiments. Read this first each session.
Max 150 lines — archive older entries to docs/logs/ when full.

---

## Current status — 2026-06-01

### What's working
- MLX injection adapter (`mlx_kvpack.py`) — verified working; Gemma tokenization bug fixed
- `run_experiment.py` — synthetic test graph, A/B/C conditions
- `run_haraway_experiment.py` — Haraway graph, 8 queries, A/B/C conditions
- `diagnostic_gemma.py` — minimal 2-query debug script with DEBUG logging
- `chat_with_graph.py` — interactive Qwen + Haraway graph chat (A/B/C toggle, /compare mode)
- `results_viewer.html` — standalone HTML results viewer (drag-drop JSON files, charts, response explorer)
- `build_haraway_graph.py` — now 3-pass: paragraph (P1), section crosscutting (P2), essay threads (P3)

### Gemma tokenization fix (critical)
Gemma's chat template with `role: system` + `add_generation_prompt=False` returns 1 token (BOS only).
Fix in `mlx_kvpack.py` `_format_fact()`: detect ≤2 token output → fall back to plain encode.
Confirmed working: 1 token → 96 tokens, A≠C on both test queries.

### Runs completed — Haraway graph (run_haraway_experiment.py)

| File | Model | A avg | B avg | C avg | Notes |
|------|-------|-------|-------|-------|-------|
| haraway_1780280858.json | Qwen2.5-7B | 0.431 | 0.754 | **0.821** | C > B — reversal from synthetic |
| haraway_1780284975.json | Llama-3.1-8B | 0.394 | 0.758 | **0.790** | C > B |
| (pending rerun) | Gemma 12B | — | — | — | Was broken (tokenization), now fixed |

### Runs completed — Synthetic graph (run_experiment.py)

| File | Model | A avg | B avg | C avg | Notes |
|------|-------|-------|-------|-------|-------|
| phase1_1780173554.json | Qwen2.5-7B | 0.000 | 0.964 | 0.929 | B > C on synthetic |
| phase1_1780173756.json | Llama-3.1-8B | 0.036 | 0.821 | 0.738 | B > C on synthetic |

**Key finding**: C > B on Haraway (complex, real-world graph); B > C on synthetic (simple, 21 nodes).
Likely explanation: large graphs benefit from KV topology access; small graphs are fully readable as text.
Cluster queries drive the gap — KV injection surfaces women/homework_economy cluster that text injection misses (generation loop artifact on long walk encoding).

### Runs in progress
- `haraway_graph_v3/` rebuild — background task b92r405cf
  Output: Pass 1 (paragraph) + Pass 2 (section crosscutting, FIXED) + Pass 3 (essay threads, NEW)
  Expected: bridges cyborg↔women gap that v2 lacked; enables cross-component multi-hop queries

---

## Research direction — READ THIS FIRST

**The recall tests are infrastructure validation, not the real experiment.**

All current tests answer H-Coalition's question: "can KV injection pre-compute a knowledge store?"
Answer: yes, confirmed. Our contribution: architecture compatibility (Gemma fix), C>B on complex graphs.

**The real experiment (next phase)**: does injecting a theoretical framework change *how* the model reasons, not just what it can recall? Requires:
1. Ambiguous scenario probes (not graph traversal questions)
2. Qualitative coding by June for reasoning pattern differences
3. Three conditions: baseline / Haraway graph injection / touchstone encoding injection

**Next session priority**: Design the disposition probe set with June, then run all 3 models.
See memory: `project_topology_injection_disposition_experiment.md`

---

## Next session queue

1. **Check graph rebuild** — read `haraway_graph_v3/stats.json`, check component count (did P2+P3 bridge the cyborg↔women gap?), examine a sample of P2/P3 triples for quality
2. **Design multi-hop queries** — once graph structure is known, design 3-4 hop queries where answers can't come from training data; include cross-component paths if P2/P3 bridged them
3. **Update run_haraway_experiment.py** — switch to triples encoding (not walk), add multi-hop queries, point to haraway_graph_v3
4. **Run all 3 models** — Qwen 7B, Llama 8B, Gemma 12B (tokenization fix in place)
5. **Design disposition probe set** — this is the real work; session with June, qualitative probe design
6. **Pull Qwen3 via Ollama** — thinking model for disposition experiment (`ollama pull qwen3`)
7. **chat_with_graph.py** — pilot the chat interface as pre-experiment exploration

---

## TODOs (ongoing)

1. **numpy divide-by-zero** in `mlx_kvpack.py` lines 104/111 — non-fatal, fix before next serious run
2. **Gemma 4** — `model_type: gemma4`, not in mlx_lm 0.31.1, no open PR adding architecture; Ollama path if needed
3. **LLM judge scoring** — keyword matching gives 3x undercount (H-Coalition finding); add judge scorer for disposition experiment (free model via OpenRouter)
4. **H-labs Pharos paper** (2026-06-01 commit) — "triples > walk for injection"; update experiment encoding once query redesign is done

---

## Infrastructure notes

**Models available (MLX cache):**
- mlx-community/Qwen2.5-7B-Instruct-4bit ✓
- mlx-community/Meta-Llama-3.1-8B-Instruct-4bit ✓
- mlx-community/gemma-3-12b-it-4bit ✓ (tokenization fix required — in place)
- mlx-community/gemma-4-e4b-it-4bit ✗ (unsupported architecture in mlx_lm)

**mlx_lm version:** 0.31.1

**Key scripts:**
```bash
cd /Users/june/Documents/GitHub/research/topology-injection
python3 run_haraway_experiment.py --model MODEL_ID          # Haraway graph test
python3 run_experiment.py --model MODEL_ID                   # Synthetic graph test
python3 diagnostic_gemma.py                                  # Debug injection for any model
python3 chat_with_graph.py                                   # Interactive chat
python3 build_haraway_graph.py                               # Rebuild graph (outputs haraway_graph_v3/)
open results_viewer.html                                     # Results viewer (drag-drop JSON)
```

**Architecture decisions:**
- All conditions run through same MLX model (controlled comparison)
- Condition D excluded by default (lib labs found no effect)
- Triples encoding preferred over walk (Pharos finding) — not yet implemented in run_haraway_experiment.py
