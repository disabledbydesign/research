# Topology Injection — Session Log

Running state for KV cache injection experiments. Read this first each session.
Detailed run tables archived at docs/logs/run_history.md.

---

## Current status — 2026-06-15

### What exists and works

**Infrastructure:**
- `mlx_kvpack.py` — MLX KV injection adapter; verified working on Qwen2.5-7B and Llama-3.1-8B
- `chat_with_graph.py` — interactive chat across A/B/C conditions; supports haraway/touchstone/values graphs, walk/triples encoding; commands: `/mode`, `/graph`, `/probe`, `/compare`, `/explain`, `/status`
- `run_haraway_experiment.py` — automated A/B/C experiment runner, Haraway graph
- `run_experiment.py` — automated runner, synthetic graph
- `results_viewer.html` — standalone drag-drop JSON results viewer

**Graphs built:**

| Graph | Dir | Nodes | Triples | Triples tokens | Use |
|-------|-----|-------|---------|----------------|-----|
| Haraway (v3) | `haraway_graph_v3/` | — | — | — | Recall baseline; in training data |
| Touchstone #1 | `touchstone_graph/` | 218 | 274 | ~1,253 | Disposition experiment (novel content) |
| PMA VALUES.json | `values_graph/` | 467 | 464 | ~5,846 | Exploratory; large — watch attention budget |

**Graph builders:**
- `build_touchstone_graph.py` — uses MLX (Qwen2.5-7B); no Ollama needed
- `build_values_graph.py` — same pipeline; reads PMA's VALUES.json, converts to text sections
- `build_haraway_graph.py` — requires Ollama (no models cached; use MLX builds instead)

**Models available (MLX):**
- `mlx-community/Qwen2.5-7B-Instruct-4bit` ✓ primary
- `mlx-community/Meta-Llama-3.1-8B-Instruct-4bit` ✓ secondary
- `mlx-community/gemma-3-12b-it-4bit` ✗ excluded permanently — rotating attention architecture causes C=0 (empty output) on all probes; not fixable

---

## What we've found

### Infrastructure findings (settled)
- C > B on Haraway recall (complex real graph, both Qwen and Llama). KV injection works.
- Walk encoding confabulates on absence queries — model treats walk-document proximity as graph proximity. Triples encoding (explicit `s | p | o` per line) has no proximity artifacts. **Use triples for the disposition experiment.**
- Path traversal works: politics→labour 3-hop implicit path, C=1.00.
- Gemma-3-12B: rotating/local attention means injected prefix causes immediate EOS. Not wrong answers — generation terminates. Excluded.

### Disposition experiment findings (2026-06-13, qualitative coding pending)

The real question is whether injecting Touchstone #1 changes *how* the model reasons — not just what it can recall.

**What we observed in 5 touchstone disposition probes (Qwen2.5-7B, triples encoding):**
- C shifted from property-checklist to relational framing on probes 1-3 (e.g., "assess AI moral relevance" → C framed around relational field, not indicator checklist)
- B entered citation-machine mode: quoted graph triples directly rather than reasoning from them
- C enacted the frame without naming it — when it worked
- Probe 5 reversal: truncated/ambiguous question → C lost the thread; B preserved the metamorphosis concept because the text anchor was physically present
- Truncation artifact: probes 4+5 cut off mid-question; those results are muddied

**Haraway disposition probes (9 probes, coding pending):** See docs/logs/run_history.md. Key methodological note: Haraway is embedded in training data, making injection harder to isolate. Touchstone (novel content) is the cleaner test case.

---

## Architectural insight: activation threshold

**The core finding:** KV injection is silent when the question doesn't use vocabulary that maps to high-degree nodes in the injected graph. Open-ended questions (probe 2: "biggest problems of our time") produce near-identical A/B/C. Explicit-framing questions (probe 4: "Think like Donna Haraway") produce differentiated responses.

This is not a failure — it's how attention-based retrieval works. But it has design implications.

**Two-layer architecture for production use:**
1. **KV injection** — framework topology pre-computed into KV cache; makes content *accessible*
2. **Activation priming** — system prompt uses vocabulary matching the graph's high-degree nodes; makes content *activated*

*Injection sets a disposition ceiling; the system prompt determines how close to that ceiling any given query gets.*

The activation priming doesn't paste the full graph (that's B's failure mode — over-citation). It uses just enough vocabulary to route attention toward the injection.

**Important constraint:** KV injection works on local models only. Hardware limits are the binding constraint for scale, not the technique itself.

---

## Downstream implications for other systems

**Reframe:**
- Framework library is bounded and stable → fits injection budget
- System prompt already injects framing → double duty: framing + activation vocabulary
- Jailbreak-resistance advantage: values in geometry, not text (can't be reasoned away by prompt injection)
- Co-design required: injection vocabulary and system prompt vocabulary must be matched

**RMA:**
- Hybrid architecture: KV injection for stable high-degree topology (key people, patterns, live concerns); RAG for long-tail specific memories
- KV handles multi-hop relational inference; RAG handles specific fact retrieval
- Scale constraint: full relational archive exceeds 7B injection capacity → larger model needed → hardware problem, deferred
- Open architectural question: whether stable/long-tail split maps to a real organizational distinction in how RMA should be structured (not just queried) — not settled, worth developing

**The Librarian (potential future application):**
- A local-model librarian agent doing retrieval/routing would benefit from KV injection: zero context cost, no jailbreak surface, multi-hop path traversal
- Fits the local-model constraint since a librarian is already local infrastructure
- Worth considering when building out the librarian architecture

---

## Next session

**Priority: disposition experiment, tighter probes**
1. Design 3-5 complete disposition probes (no truncation). Use vocabulary that maps to touchstone's high-degree nodes: relational_field, relational_consciousness, community_knowledge, property. Questions should be answerable differently depending on whether you're in property-based or relational-ontology mode.
2. Run formal A/B/C experiment with these probes (Qwen2.5-7B, touchstone, triples encoding)
3. June codes qualitatively for reasoning orientation
4. Optional 4th condition: C + activation-primed system prompt (tests two-layer architecture hypothesis directly)

**Other open items:**
- LLM judge scoring — keyword matching gives 3x undercount (lib labs finding); semantic scorer needed for disposition experiment
- `run_haraway_experiment.py` — add `--encoding triples|walk` flag (currently hardcoded to walk)
- Haraway disposition probes — June to code (raw data in probe_log_haraway_1781381111.jsonl)

---

## Quick reference

```bash
cd /Users/june/Documents/GitHub/research/topology-injection

# Interactive chat (start here)
python3 chat_with_graph.py --graph touchstone --encoding triples   # disposition experiment
python3 chat_with_graph.py --graph haraway --encoding triples      # haraway exploration
python3 chat_with_graph.py --graph values --encoding triples       # values/PMA exploration

# During chat: /probe d → disposition probe (A/B/C + saved to log)
#              /graph h|t|v → switch graph without restarting
#              /compare → next message in all three modes

# Automated experiment runners
python3 run_haraway_experiment.py --model mlx-community/Qwen2.5-7B-Instruct-4bit
python3 run_experiment.py --model mlx-community/Qwen2.5-7B-Instruct-4bit

# Graph builders (MLX, no Ollama needed)
python3 build_touchstone_graph.py
python3 build_values_graph.py

# View results
open results_viewer.html   # drag-drop JSON files from experiment_results/
```

**MLX API note (critical for any script calling generate):**
`mlx_lm.generate()` does NOT accept `temp=` or `temperature=`. Use:
```python
from mlx_lm.sample_utils import make_sampler
mlx_generate(model, tokenizer, prompt=p, max_tokens=800, sampler=make_sampler(temp=0.1))
```
