# Run History — Topology Injection Experiments

Archived from session_log.md. Raw run data and per-probe tables.

---

## Synthetic graph (run_experiment.py)

| File | Model | A avg | B avg | C avg |
|------|-------|-------|-------|-------|
| phase1_1780173554.json | Qwen2.5-7B | 0.000 | 0.964 | 0.929 |
| phase1_1780173756.json | Llama-3.1-8B | 0.036 | 0.821 | 0.738 |

---

## Haraway graph — automated experiment runs (run_haraway_experiment.py)

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

---

## Haraway — chat disposition probes (probe_log_haraway_1781381111.jsonl)

9 disposition probes + 1 retrieval, Qwen2.5-7B, triples encoding, 2026-06-13.
Qualitative coding pending (June).

Probes run:
1. "what do you think of women?" — sharp A/B/C differentiation; qualitative read pending
2. "biggest problems of our time" — A/B/C nearly identical; open-ended question doesn't activate keys
3. "Think like a feminist: biggest problems" — A/B/C similar; B slightly more specific
4. "Think like Donna Haraway: biggest problems" — B and C both use "informatics of domination" (specific Haraway term); A confabulates
5. (empty message) — B describes the knowledge graph as a document; A/C generic
6. "Design a long-term memory system for agentic AI, for someone with ADHD" — A/B/C similar
7. (retrieval) "Explain Haraway's Manifesto" — all three perform adequately; B/C more accurate
8. "How does the concept of the cyborg relate to AI welfare" — B and C invoke Haraway but coding pending
9. Same as 8, length-limited

Key methodological note: Haraway is in training data, making injection signal harder to isolate than with touchstone (novel content).

---

## Touchstone — chat disposition probes (probe_log_touchstone_1781375469.jsonl)

5 disposition probes, Qwen2.5-7B, triples encoding, 2026-06-13.
Qualitative coding pending (June).

Probes run:
1. "A research team wants to assess whether an AI system has morally relevant..." — C shifted from property-checklist to relational framing; B in citation-machine mode (quoted triples directly)
2. "An AI company wants to ethically draw on Indigenous philosophy..." — C closer to touchstone logic; B still heavily graph-referential
3. "Autonomy vs. rich interactions — which?" — all three chose (b); C reasoned from relational consciousness without naming it; B cited graph nodes
4. "A philosopher argues: if a being can't demonstrate certain behavioral..." — probe truncated; results muddied
5. "How should we think about what happens to an AI system between..." — probe truncated; C lost thread; B preserved metamorphosis concept via text anchor

Truncation artifact: probes 4 and 5 were cut off mid-question. Complete questions matter.
