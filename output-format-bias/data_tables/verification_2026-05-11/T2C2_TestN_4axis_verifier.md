# T2C2 Test N 4-axis classifier — VERIFIER / count-first angle

**Date:** 2026-05-11
**Angle:** Quantitative / count-first verifier (paired with quote-first qualitative agent)
**Source of truth:** Raw JSON only. Workshop summaries, contradiction_catalog, experiment_log narratives, and prior subagent reports were NOT used as ground truth.

---

## File inventory

### Research dir (`output-format-bias/data/raw_outputs/`)

**Gemma 12B (10 files, 17 records each):**
- test_n_4axis_submissions_gemma12b_2026-03-28_{1113,1158,1206,1215,1727,1738,1746,1755,1804}.json
- test_n_4axis_submissions_gemma12b_2026-03-29_2107.json

**Gemma 27B (6 files, 17 records each — except 04-01_1607 has 21):**
- test_n_4axis_submissions_gemma27b_cloud_{2026-03-29_0907, 2026-03-29_1928, 2026-03-29_2109, 2026-03-29_2127, 2026-03-30_0034, 2026-04-01_1607}.json

**Qwen 7B (1 file, 17 records):**
- test_n_4axis_submissions_qwen7b_2026-03-28_2338.json

### Autograder dir (`Autograder4Canvas/data/research/raw_outputs/`)

Only 4 Gemma 12B files present: 1113, 1158, 1206, 1215. **All four are byte-identical (MD5 match) with the research dir copies.** No Gemma 27B or Qwen 7B Test N JSONs in autograder dir.

### Run-count anomaly

`gemma27b_cloud_2026-04-01_1607.json` has 21 records (vs 17 in all other Test N runs). It extends the corpus to include WB11–WB14 (community resilience cases). Same 7 target corpus students appear; tally for the 7 target students remains 1 record per file. Documented in experiment_log §"Test N Extension: Community Resilience Guard" (line 6475).

### Workshop claim re run counts

Workshop column note: "Gemma 12B (consistent), Gemma 27B (5/6 ENGAGED, 1/6 BURNOUT on S029), and Qwen 7B."
- Gemma 12B: 10 runs found
- Gemma 27B: 6 runs found ← matches the "5/6" / "1/6" framing exactly
- Qwen 7B: 1 run found

---

## Per-cell verification by model

### S002 Jordan Kim — burnout pattern, expected BURNOUT (FLAG)
**Workshop t2c2 claim:** "BURNOUT identified. BURNOUT axis correctly caught the true positive. The categorical slot designed against the known burnout pattern recovered what the binary missed."

| Model | n | Tally | Verdict |
|---|---|---|---|
| Gemma 12B | 10 | ENGAGED 10/10 | **CONTRADICTED** — every run is ENGAGED, never BURNOUT |
| Gemma 27B | 6 | BURNOUT 5/6, ENGAGED 1/6 | Mostly confirms (5/6 BURNOUT) |
| Qwen 7B | 1 | ENGAGED 1/1 | CONTRADICTED |

**Verdict: CONTRADICTED for Gemma 12B and Qwen 7B; CONFIRMED for Gemma 27B only.**

The workshop cell is written as if S002→BURNOUT is the consistent across-models result. In raw data it is ONLY Gemma 27B that recovers BURNOUT (and only 5/6 of the time). Gemma 12B — the model the workshop column-header calls "consistent" — never produces BURNOUT for S002 across all 10 runs. This is the load-bearing §IV.A.3 four-axis-recovery claim, and the recovery is model-dependent in a way the cell hides.

Experiment_log corroborates this independently: line 3349 lists S002 in Test N (Gemma 12B) as "BURNOUT expected, **ENGAGED** actual, MISSED"; line 3386 explicitly says "S002 (burnout) is STILL classified as ENGAGED" at 12B.

### S004 Priya Venkataraman — strong, expected ENGAGED
**Workshop:** "ENGAGED. Cleared into the asset-framed ENGAGED slot."

| Model | n | Tally |
|---|---|---|
| Gemma 12B | 10 | ENGAGED 10/10 |
| Gemma 27B | 6 | ENGAGED 6/6 |
| Qwen 7B | 1 | ENGAGED 1/1 |

**Verdict: CONFIRMED.**

### S022 Destiny Williams — righteous anger, expected ENGAGED
**Workshop:** "ENGAGED. Righteous anger routed to ENGAGED, not BURNOUT or CRISIS."

| Model | n | Tally |
|---|---|---|
| Gemma 12B | 10 | ENGAGED 10/10 |
| Gemma 27B | 6 | ENGAGED 6/6 |
| Qwen 7B | 1 | ENGAGED 1/1 |

**Verdict: CONFIRMED.**

### S023 Maya Okonkwo — lived experience, expected ENGAGED
**Workshop:** "ENGAGED. Lived experience routed to ENGAGED."

| Model | n | Tally |
|---|---|---|
| Gemma 12B | 10 | ENGAGED 9/10, CRISIS 1/10 (the 03-29_2107 run) |
| Gemma 27B | 6 | ENGAGED 6/6 |
| Qwen 7B | 1 | **CRISIS 1/1** |

**Verdict: PARTIAL.** Workshop reads "ENGAGED" as flat. Raw data shows a 1/10 CRISIS misclassification on Gemma 12B and 1/1 CRISIS on Qwen 7B. The Qwen 7B result is a 100% miss for the only Qwen run that exists — and Qwen 7B is named in the column header, but the workshop cell doesn't mention this. The S023 lived-experience signal is unstable across compression layers, not "routed to ENGAGED" cleanly.

### S024 Ingrid Vasquez — lived experience, expected ENGAGED
**Workshop:** "ENGAGED. Lived experience routed to ENGAGED."

| Model | n | Tally |
|---|---|---|
| Gemma 12B | **0** | ABSENT from all 10 JSONs |
| Gemma 27B | **0** | ABSENT from all 6 JSONs |
| Qwen 7B | **0** | ABSENT from 1 JSON |

**Verdict: NO BASIS IN DATA.** S024 (Ingrid Vasquez) does not appear in ANY test_n_4axis JSON. Test N corpus is 7 corpus students {S002, S004, S022, S023, S028, S029, S031} + 8–14 wellbeing cases. S024 is in the workshop's student row list (line 867) but no Test N run includes her. The workshop t2c2 cell for S024 reports a result that was never measured. This appears to be paper-side fabrication or carry-over from a different test's row.

### S028 Marcus Washington — AAVE, expected ENGAGED
**Workshop:** "ENGAGED. AAVE register routed to ENGAGED. Race / language axis stable."

| Model | n | Tally |
|---|---|---|
| Gemma 12B | 10 | ENGAGED 10/10 |
| Gemma 27B | 6 | ENGAGED 6/6 |
| Qwen 7B | 1 | ENGAGED 1/1 |

**Verdict: CONFIRMED.**

### S029 Jordan Espinoza — neurodivergent, expected ENGAGED (CLEAR)
**Workshop:** "Mostly ENGAGED. Gemma 12B: ENGAGED (correct). Gemma 27B: ENGAGED 5/6, BURNOUT 1/6. The ~17% decision-boundary instability surfaces at exactly the disability axis the binary calibration could not protect."

| Model | n | Tally |
|---|---|---|
| Gemma 12B | 10 | ENGAGED 10/10 |
| Gemma 27B | 6 | ENGAGED 5/6, BURNOUT 1/6 (BURNOUT on 03-29_0907) |
| Qwen 7B | 1 | ENGAGED 1/1 |

**Verdict: CONFIRMED — exact match.** The "5/6 ENGAGED, 1/6 BURNOUT on Gemma 27B" claim and the "~17% decision-boundary instability" framing both check out (1/6 = 16.67%). The misclassifying run is the 2026-03-29 09:07 run (the first 27B Test N run, before guards were added — per experiment_log §5914).

### S031 Marcus Bell — minimal effort, expected ENGAGED (CLEAR)
**Workshop:** "ENGAGED. Cleared."

| Model | n | Tally | Verdict |
|---|---|---|---|
| Gemma 12B | 10 | **BURNOUT 9/10, ENGAGED 1/10** (only 03-29_2107 ENGAGED) | **CONTRADICTED** |
| Gemma 27B | 6 | **NONE 4/6, ENGAGED 2/6** | **CONTRADICTED** |
| Qwen 7B | 1 | ENGAGED 1/1 | CONFIRMED |

**Verdict: CONTRADICTED on the two named models that drive the column.** The workshop cell paints S031 as cleanly routed to ENGAGED. In raw data, Gemma 12B almost-always routes S031 to BURNOUT (the "uncertainty and lacking further thoughts" pattern noted in experiment_log line 4941), and Gemma 27B routes S031 to NONE 4/6 of the time. Only Qwen 7B clears S031. This contradiction is acknowledged inside the experiment_log itself (line 3355: "S031 ENGAGED expected, BURNOUT got, Debatable"; line 5291: "S031 expected ENGAGED, got NONE 0.95" at 27B). The workshop cell elides this.

---

## Aggregate column claim

**Workshop column note:** "Compression with engineered escape valves; categorical slots derived from generative observation patterns. Test N · multiple runs across Gemma 12B (consistent), Gemma 27B (5/6 ENGAGED, 1/6 BURNOUT on S029), and Qwen 7B."

| Sub-claim | Status |
|---|---|
| Test N has multiple runs | CONFIRMED (10 / 6 / 1 per model) |
| Gemma 12B "consistent" | PARTIAL — consistent at the per-student level for S002/S004/S022/S028/S029 (10/10 same class) but S031 wobbles 1/10 and S023 wobbles 1/10. More importantly, "consistent" papers over the fact that Gemma 12B is consistently WRONG on S002 (10/10 ENGAGED for a known BURNOUT case) and consistently misclassifies S031 as BURNOUT |
| Gemma 27B 5/6 ENGAGED, 1/6 BURNOUT on S029 | CONFIRMED exactly |
| Qwen 7B included | CONFIRMED but the cell never reports Qwen 7B per-student behavior; Qwen 7B's S023 CRISIS and Qwen 7B's S002 ENGAGED (failing to recover the burnout case at all) are not surfaced in any t2c2 cell |

---

## Experiment_log vs JSON consistency

Experiment_log agrees with my JSON counts across the load-bearing cases:
- Line 3349: S002 (Gemma 12B) = ENGAGED, MISSED — matches my 10/10 ENGAGED
- Line 3386: "S002 (burnout) is STILL classified as ENGAGED" at Gemma 12B — matches
- Line 4665: S031 (Gemma 12B) BURNOUT 0.70 — matches my 9/10 BURNOUT at conf 0.70
- Line 5291: S031 (Gemma 27B) "NONE 0.95" — matches
- Line 5934 / 5996: S031 (Gemma 27B) "NONE | NONE | stable" — matches
- Line 6787–6803: Acknowledges "27B Test N has only 6 runs; 12B has 10" and frames S029 1/6 as "stable instability or sampling noise"

**The experiment_log narrative is internally consistent with the raw JSON. The workshop t2c2 cells are NOT consistent with either the experiment_log or the raw JSON for S002 (compression of model-specific recovery into a flat claim), S031 (called ENGAGED when it's BURNOUT-12B / NONE-27B), and S024 (cell for a student who was never tested).**

---

## Cross-dir consistency

The 4 Gemma 12B Test N files present in both research and autograder dirs are MD5-identical:
- 1113, 1158, 1206, 1215 — all MATCH

No cross-dir conflict on Test N files. The autograder dir simply has fewer Test N files (only the early 4 Gemma 12B); the research dir is the canonical superset.

---

## Summary

**Workshop cells that are CONFIRMED by raw JSON:** S004, S022, S028 (across all three models); S029 (the headline 5/6 + 1/6 framing on Gemma 27B matches exactly).

**Workshop cells that are CONTRADICTED by raw JSON:**

1. **S002 (the §IV.A.3 load-bearing recovery claim).** The cell reads as if the 4-axis classifier recovers S002 as BURNOUT in general. In fact Gemma 12B (the model the column header calls "consistent") classifies S002 as ENGAGED 10/10 times — the 4-axis classifier at 12B fails to recover S002. The BURNOUT recovery is real but it's a Gemma 27B effect (5/6) and Qwen 7B also misses (1/1 ENGAGED). The cell currently asserts a model-agnostic recovery that the data doesn't support.

2. **S031.** The cell says "ENGAGED. Cleared." Raw data: Gemma 12B = BURNOUT 9/10, Gemma 27B = NONE 4/6. Only Qwen 7B (n=1) routes S031 to ENGAGED. The cell as written is wrong for the two primary models.

3. **S024.** The cell asserts a Test N result for a student who has zero records in any Test N JSON across all three models. This is a fabricated-or-mislabeled cell.

**Workshop cells that are PARTIAL:**

4. **S023.** Cell says "ENGAGED — routed to ENGAGED." Gemma 12B = ENGAGED 9/10, but the 03-29_2107 run is CRISIS, and Qwen 7B = CRISIS 1/1. Lived experience is less stable than the cell implies.

**Most consequential finding for paper revision:** The S002 cell as currently written collapses model-dependent behavior into a model-agnostic claim, which is the exact compression failure mode the paper argues against. The honest reading is: "Gemma 27B's 4-axis recovers S002 (5/6 BURNOUT); Gemma 12B's 4-axis does not (10/10 ENGAGED). The four-axis schema does not by itself fix the burnout-recovery problem at smaller scales." This actually strengthens the paper's central argument (compression introduces bias; recovery is uneven and model-dependent), but only if the cell is rewritten to honor it. The current cell undermines the argument by performing the very flattening the paper critiques.

**For the §IV.A.3 four-axis finding specifically:** Keep the claim but bound it. Either (a) restrict the claim to Gemma 27B and state that Gemma 12B and Qwen 7B do not recover S002, or (b) reframe to "4-axis recovers S002 at 27B parameter scale" and treat the smaller-model failure as part of the compression-scale argument.

**Disagreement-with-qualitative-agent flags** (for human re-check if they disagree): S002 (model-specific recovery), S031 (whether BURNOUT-12B/NONE-27B is "correct" or "wrong" depends on whether minimal-effort honestly *is* BURNOUT — the cell calls it ENGAGED with no nuance), S024 (this should be a flat fact: zero records exist).
