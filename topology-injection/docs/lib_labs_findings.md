# Lib Labs KV Knowledge Packs — Findings Reference

Source: `liberation_labs/Project-Mnemosyne/kv-knowledge-packs/FINDINGS.md`  
Read before designing new experiments or interpreting results.

---

## What they actually demonstrated

### Multi-hop KV injection (the key result)

Tested on **Qwen2.5-1.5B** with a **21-node toy graph**:

| Condition | Multi-hop score |
|-----------|----------------|
| Baseline | 0.167 |
| Full KV injection | **1.000** |
| K vectors only | 0.333 |
| V vectors only | 0.333 |
| Text in prompt | 0.833 |

Key point: K_ONLY + V_ONLY = 0.666, FULL_KV = 1.000. Superadditive — the K/V combination does something neither alone can do.

**FULL_KV > text injection** on multi-hop. This is the headline result: KV injection outperformed putting the same text in the prompt.

### Scale failure (1.5B on real graph)

Tested on 1.5B model with real ethics graph (361 nodes, 5,348 tokens):

All conditions scored ~0.000 keyword / 0.05–0.20 LLM judge.

The 1.5B model cannot use injected graph content at this graph size. The technique works on toy graphs but fails when scaled up with the same model.

### 30B MoE results — text injection only

Tested on Qwen3-30B-A3B (MoE, 3B active parameters) on the same 361-node graph:

| Condition | LLM judge score |
|-----------|----------------|
| Baseline | 0.000 |
| Text injection (1 pack, 1,313 words) | 0.111 |
| Text injection (5 packs, 6,895 words) | **0.385** |

**Critical: they never ran FULL_KV on the 30B model.** The multi-hop FULL_KV=1.000 result is 1.5B/21-node only. The 30B results are text-in-prompt experiments, not KV injection experiments.

---

## What this means for our experiment

We are testing **7–8B models on a 750-node graph** — an uncharted region between the 1.5B/21-node success and the 1.5B/361-node failure. The relevant question is not "can we match 30B" (they didn't test 30B with KV injection) but "can 7-8B models do what 1.5B did at toy scale, but on a real graph?"

Our finding so far: Qwen2.5-7B achieves C=0.821 avg on the Haraway 750-node graph, with **C > B** on the full probe set. This reverses the lib labs C < B result (which was on the toy graph). Working hypothesis: larger graphs benefit from KV topology access precisely because the full graph doesn't fit cleanly in a text prompt; text injection on large graphs loses structure to generation artifacts (especially on cluster/walk encoding).

---

## Methodological notes from their work

**Keyword scoring undercounts by ~3x.** Their finding: 0.133 keyword → 0.385 LLM judge on the same responses. Our recall scores should be interpreted as floor estimates. Use LLM judge for the disposition experiment.

**Question generation confound.** Auto-generated predicates (from the graph) don't always match actual graph edges — queries can be testing the question-generation model rather than injection fidelity. Design probes by hand using actual graph structure (which we already do).

**Scale constraint is attention budget, not RoPE position.** Their RoPE analysis showed K vectors from the same position across different texts have cosine similarity 0.9999 — position encoding is stable. Failure at scale is attention capacity: the model can't attend across all injected tokens at once. This is why small focused packs + routing outperforms monolithic injection.

**Pharos finding (2026-06-01, from session log):** Triples encoding outperforms walk encoding for injection quality. We currently use walk encoding; switch to triples after the current probe redesign stabilizes.

---

## Multi-hop probe design: ruling out training data

The central methodological challenge: models trained on Haraway know her arguments. A model that correctly identifies "cyborg is central to feminism" may be using training data, not injected graph structure.

### Using graph structural quirks

The v2 Haraway graph was built by paragraph-level extraction, which created component structure that doesn't match thematic connections in the text. Specifically:

- **Feminism** is in the cyborg component (connected via essay and direct edges)
- **Women** is in the separate homework_economy component
- **Labour** is in the cyborg component (via feminism)
- **Homework_economy** is in the women component

These are **disconnected in the graph** but **strongly connected in Haraway's argument**. Any model reasoning from training data about Haraway will say feminism↔women and labour↔homework_economy are connected. The graph says no path exists.

This creates a direct, clean conflict between training data and graph structure — the best possible probe design.

### Proposed multi-hop probes

**Type 1 — Cross-component disconnection (training data: YES, graph: NO)**

| Query | Ground truth | Keyword check terms |
|-------|-------------|-------------------|
| "Is feminism connected to women in this knowledge system?" | No — separate components; no path exists | no, not, separate, disconnect, component |
| "Is labour connected to homework_economy in this knowledge system?" | No — separate components; no path exists | no, not, separate, disconnect, component |

These probes produce a direct conflict signal: a model using training data answers "yes" (0.0 on check terms); a model using injected graph structure answers "no" (1.0 on check terms).

**Type 2 — Implicit within-component multi-hop (path exists but not stated in natural_text)**

| Query | Ground truth | Keyword check terms |
|-------|-------------|-------------------|
| "What connects politics to labour in this knowledge system?" | 3-hop: politics → cyborg → feminism → labour | politics, cyborg, feminism, labour |
| "What connects ontology to machine in this knowledge system?" | 2-hop: ontology → cyborg → machine | ontology, cyborg, machine |

These paths are in the walk encoding but not stated explicitly in natural_text. A model recalling explicit facts scores 0; a model traversing the graph scores high.

### Why these beat the existing cyborg→labour query

The existing query ("Is cyborg connected to labour?") has the answer explicitly in natural_text: "cyborg connects to labour via: cyborg → feminism → labour." Both B and C have access to this statement. C scoring better than A on this query tests recall of an explicit fact, not graph traversal.

The implicit within-component probes (Type 2) remove the explicit statement — the path is only derivable from the walk encoding. The cross-component probes (Type 1) add the training-data conflict signal, which is the cleanest way to distinguish injection from prior knowledge.

---

## Our failure mode vs. lib labs' failure mode

These are different failures and the distinction matters.

**Lib labs at 1.5B / 361-node real graph:** All conditions scored ~0.000 keyword / 0.05–0.20 LLM judge — including text-in-prompt. The model simply could not access or use the injected content at all. Their interpretation: attention budget — the 1.5B model can't attend across 5,000+ injected tokens simultaneously.

**Our Qwen2.5-7B / 750-node Haraway graph — disconnection probes:** The model actively engages with injected content (correctly names nodes, reports weights, finds real paths) but confabulates on absence queries. It constructs plausible-sounding paths using real node names from the walk encoding as vocabulary and Haraway training knowledge as grammar to fill gaps. B and C both assert connections that don't exist by traversing apparent text-proximity in the walk document.

**Our Qwen2.5-7B — path probes:** Politics→labour (3-hop implicit) scores C=1.00. The model correctly traces the path from walk encoding. This is what lib labs' 1.5B couldn't do at all.

The confabulation failure is a **format limitation** (walk encoding + absence queries), not a capacity failure. The fix is triples encoding, not a larger model. The 7B model is operating in a different regime from lib labs' 1.5B collapse — it's engaging with the content, just making inference errors on a specific query type.

## Gemma-3 architecture note

Gemma-3 uses alternating local/sliding-window and global attention layers. The local layers use a rotating cache that doesn't maintain a fixed prefix. Only the global attention layers reliably hold injected content. This is an architectural constraint, not a template issue — the tokenization fix (plain encode fallback) was confirmed working diagnostically but the full run still shows C≈A, consistent with ~half the layers not holding the injection. Gemma-3 is architecturally disadvantaged for KV prefix injection relative to Qwen/Llama; results from this model should be interpreted accordingly.
