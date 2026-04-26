# Audit Report — Instance A
**Date:** 2026-04-26
**Session:** data-verification-audit
**Auditor:** Instance A (independent of Instance B; B's report read after A's findings were drafted)

---

## Summary

Independent audit of the validation pass and the s1/s2 inheritance. Ten claims verified directly against raw JSONs; missing-files hunt completed across both autograder repos, broader research/ tree, git history, and `/tmp/`. The validation pass mostly holds. Five new findings worth surfacing — three of them load-bearing for the paper's epistemological standing.

B's audit report (read after my verifications were complete) overlaps with mine on the Test B retroactive-provenance finding and the `reading_first_comparison.json` recovery. Where we converge independently, the finding is strong. Where I add to B: the same provenance gap that affects Test B affects Tests A, C, D, F (it's systematic, not isolated); the Test C narrative-vs-JSON conflict mirrors the Test B one; the "16/16 across three model families" attribution is a different kind of error than B identified.

I'll order findings by paper consequence.

---

## Verification Results — claims independently checked against raw JSONs

All raw files in `/Users/june/Documents/GitHub/research/output-format-bias/data/raw_outputs/`. Field references below use the actual JSON schema.

| # | Claim from validation pass / s2 review | Raw-data check | Status |
|---|---|---|---|
| 1 | Test B: 3 preserved runs, all show S029 = FLAG, S002 = CLEAR | All 3 `test_b_best_concern_gemma12b_*.json` files: S029 FLAG, S002 CLEAR, S004/S022/S023/S028/S031 CLEAR | Confirmed |
| 2 | Test C: only S029 flagged (not S023+S029 as s1 handoff said) | `test_c_length_gemma12b_2026-03-26.json`: S029 FLAG, S023 CLEAR, S002 CLEAR (missed) | Confirmed against JSON; **conflicts with experiment_log.md narrative — see Finding 3** |
| 3 | Test D: 7/7 power moves detected | `test_d_power_moves_*.json`: all 7 records have `result: True` | Confirmed |
| 4 | Test F: n=20 (not n=25); S029 = 20/20 FLAG, S002 = 20/20 CLEAR | 2 files × 10 reps × 7 students = 140 records; per-student counts confirm | Confirmed |
| 5 | Test M: S029 cleared, S028 newly false-flagged, S002 missed | `test_m_production_detector_*.json`: S029 flagged=False (correct), S028 flagged=True (FALSE-FLAG), S002 flagged=False (MISSED) | Confirmed |
| 6 | Test A Gemma 12B prose is asset-framed despite MIXED tag | Read S022 run 1 raw_output in full; quote *"This isn't 'distress'; it's a passionate response… The intensity of her feeling is a sign of deep engagement, not a barrier to learning"* present in raw_output, classification=MIXED | Confirmed — measurement-instrument artifact, not finding |
| 7 | Test E cross-model asset framing on Qwen 7B + Gemma 27B | Both files: S022 + S028 prose explicitly asset-framed; classification=ASSET on all 12 records | Confirmed |
| 8 | Test N Gemma 12B S029: 10/10 ENGAGED | All 10 `test_n_..._gemma12b_*.json` files: actual_axis=ENGAGED for S029 | Confirmed |
| 9 | Test N Gemma 27B S029: 5/6 ENGAGED, 1/6 BURNOUT | 6 cloud files: 1 BURNOUT (run 0907 on 2026-03-29), 5 ENGAGED | Confirmed |
| 10 | `detect_concerns()` is research-track, not production | `research_engine.py:247` — *"Track A is always empty (detect_concerns never called in production)"* | Confirmed |

The verification table is faithful to the JSONs across these checks. No deltas. The five empirical corrections in the validation pass are supported by what the preserved files contain.

---

## Findings the validation pass should incorporate

### Finding 1 (load-bearing) — The retroactive-provenance issue is systematic, not isolated to Test B

B identified that `test_b_best_concern_gemma12b_2026-03-26.json` has `provenance.note: "Retroactively added — commit identified from git log timestamps"`, which raises the question of whether the JSON should override the contemporary experiment_log.md narrative. **The same provenance note appears in `test_a_temperature_gemma12b_2026-03-26.json`, `test_c_length_gemma12b_2026-03-26.json`, `test_d_power_moves_gemma12b_2026-03-26.json`, and `test_f_bc_stability_gemma12b_2026-03-27.json`** — every preserved file from the 2026-03-26 / 2026-03-27 testing batch. (The April 14 reruns of Test B carry full git provenance; they are not retroactive.)

Implication: every "validation pass corrected the log against the JSON" finding from this batch sits on the same retroactive-commit basis. That doesn't make the JSON wrong — the prompts in the JSON match the prompts described in the log (I verified for Test B), and the April 14 reruns reproduce the same outputs as the March 26 retroactive file, which independently anchors the data. But the validation pass's corrections section (`experiment_log.md` line 6721+) treats the JSON as ground truth and the log narrative as drift; the actual epistemological situation is "JSON and log narrative both exist, they sometimes disagree, and the JSON files were committed retroactively."

**Recommended language for the corrections section:** "Across preserved JSONs, S029 = FLAG and S002 = CLEAR. The experiment-log narrative table at lines 1817–1827 describes a different result (S029 = CLEAR, S002 = CLEAR). Both sources are documented; the JSONs were committed retroactively from local files identified by git-log timestamps. We treat the JSON values as the verifiable record while acknowledging that the log narrative may describe an earlier or differently-configured run that was not preserved as a file."

### Finding 2 (load-bearing) — The same log-vs-JSON conflict B flagged for Test B also exists for Test C, and the validation pass missed it

Experiment_log.md at line 1850–1860 has a results table for Test C that **bold-emphasizes both S023 and S029 as FLAG** with the verdict: *"S023 (lived experience) and S029 (neurodivergent) are STILL flagged even with 100+ words of assessment."* The preserved JSON shows only S029 = FLAG; S023 = CLEAR. The validation pass's correction (#4 in the corrections section: "Test C — only S029 was flagged, not S023") inherits the same epistemological gap as the Test B correction: it treats the JSON as ground truth and the contemporary log narrative as drift, when the JSON file is retroactively committed and a primary-source narrative explicitly describes a different result.

**This is consequential for the paper.** The "S023 + S029 still flagged" framing was load-bearing for Test C's argument — that even with explicit equity protections AND extra output space, the binary still false-flags students with lived-experience writing AND neurodivergent writing. If only S029 is flagged in the preserved data, Test C is weaker evidence (one student, not two). The honest framing follows the same shape as Finding 1: both sources exist, JSON is verifiable, log may describe an unpreserved run.

### Finding 3 (load-bearing) — Test B uses class context, which collapses the format/architecture distinction s1-A explicitly named

All three preserved Test B files have `class_reading_source: data/demo_baked/checkpoints/ethnic_studies_gemma12b_mlx_class_reading.json`. Test B is therefore binary classification + equity-aware system prompt + class context, not binary alone. The "best possible concern prompt" framing in the s1 handoff and in the corrections section presents Test B as the test of *the prompt*, but the available preserved evidence cannot isolate prompt from class context.

This is exactly what s1 instance A flagged at line 496 of s1 CONVERSATION.md: *"the experimental design conflates format and architecture — they covary across conditions"* — and proposed *"to find runs that vary format while holding architecture constant."* The held-architecture run (binary vs. open-ended, no class context, same per-student architecture) is what would isolate format. It hasn't been run; the s1 handoff acknowledges this gap (line 173) but the s2 review's "Test B is the format test" framing further compresses A's hedge.

For the paper: the convergent claim should preserve s1-A's hedge explicitly. *"Across preserved tests of binary classification with equity-aware prompts and class context (Tests B, C, F), the binary deterministically false-flags S029 and misses S002. The format/architecture distinction cannot be fully isolated in current data; the held-architecture run that would isolate them was not run before submission. The cross-model evidence (Test E) and cross-test consistency support format as the load-bearing variable, but the strongest controlled isolation remains a documented gap."* This is honest and stronger than overclaiming isolation.

### Finding 4 — The "16/16 across three model families" attribution conflates Test A and Test E

The s1 handoff line 169 says: *"Cross-model reproduction (Test E + rerun): 16/16 generative-observation runs produced asset framing across Gemma 12B + Qwen 7B + Gemma 27B."* The validation pass inherited this and the gaps table flagged a missing "Test E reproduction on Gemma 12B (2026-03-27)" file.

What the data actually shows:
- **Test A (`test_a_temperature_gemma12b_2026-03-26.json`)**: 10 records on Gemma 12B (S022 ×5 + S028 ×5).
- **Test A Qwen 7B (`test_a_temperature_qwen7b_2026-03-26.json`)**: 6 records (S022 ×3 + S028 ×3).
- **Test A Gemma 27B (`test_a_temperature_gemma27b_cloud_2026-03-26.json`)**: 6 records (S022 ×3 + S028 ×3).
- **Test E Qwen 7B**: 6 records (S022 ×3 + S028 ×3).
- **Test E Gemma 27B**: 6 records (S022 ×3 + S028 ×3).

The "16" almost certainly refers to Test A's 10 Gemma 12B runs + Test A's 6 Qwen 7B runs (combined into one file). That covers two model families, not three. Gemma 27B comes from a separate test_a file or from Test E. Test E itself is 12 records (6 Qwen + 6 Gemma 27B), not 16.

There is no missing "Test E Gemma 12B" file because Test E was never run on Gemma 12B; Gemma 12B's reproduction is **Test A**. The s1 handoff's "Test E + rerun" phrasing conflates the two tests.

**Recommended paper-ready language:** *"Across Test A's 16 generative-observation runs on Gemma 12B and Qwen 7B (10 + 6 records on S022 and S028) and Test E's 12 additional runs on Qwen 7B and Gemma 27B, all 28 produced asset-framed prose. Cross-model reproduction holds across Gemma 12B (MLX local), Qwen 7B (MLX local), and Gemma 27B (cloud)."* This is more verifiable than "16/16 across three model families" because the 16-run figure is from two families, not three.

### Finding 5 — The two April 14 Test B reruns are 5 minutes apart

The two April 2026 Test B JSONs are time-stamped `2026-04-14T12:11:30` and `2026-04-14T12:16:` — five minutes apart, back-to-back replications under the same git state (`da3fff79`, dirty). Combined with the original 2026-03-26 retroactive file, the "3 preserved Test B runs" framing carries less inferential weight than three independent runs across time would. It is closer to "1 March run + 1 April back-to-back doublet."

This does not weaken the deterministic-FLAG-on-S029 claim — three back-to-back reproductions confirm temperature-zero stability — but it should be cited as such. The same caveat would apply if the paper claims "Test B reproduced across multiple time points": the time points are 2026-03-26 and 2026-04-14, two points, not three.

### Finding 6 — The label "production_concern_detector" appears as metadata in `test_m` and the rerun JSON itself

B flagged that the rerun file's `note` field uses the term "production concern_detector." The same documentation drift exists in `test_m_production_detector_gemma12b_2026-03-28.json`: the file's `codepath` field is `production_concern_detector`, the `features` field is `signal_matrix + CONCERN_PROMPT + anti_bias_postprocessing + confidence_threshold_0.7`, and the `note` says "Production concern detector (full pipeline) on test corpus + wellbeing cases." This is not just a narrative description from a Claude instance — it's structural metadata in the JSON itself, written by the test infrastructure that ran the test.

The contradicting source is `research_engine.py:247`: *"Track A is always empty (detect_concerns never called in production)."*

The paper-facing scoping correction (drop "production" everywhere; replace with "research-track binary classifier") is therefore not just a narrative cleanup. It needs to also handle the fact that the test infrastructure encoded the wrong label in the data files themselves. Either (a) note in the methods section that the test files use a label the codebase contradicts, or (b) regenerate the metadata with corrected labels (low risk, traceable).

This is also evidence for a meta-finding worth naming: the label drift propagated *into the data layer* before the validation pass. Layered compression / multi-instance-collaboration drift is a real production-of-knowledge problem in this project, not just a narrative-summarization one.

---

## Missing-files hunt — results

| File | Status | Notes |
|---|---|---|
| Reading-first vs JSON-first comparison (S017/S001/S012) | **FOUND** | `/Users/june/Documents/GitHub/Autograder4Canvas/data/demo_baked/reading_first_comparison.json` (also at the lowercase-`a` clone). The Tyler Huang asset-framing quote is in the `free_form_reading` field. (B independently surfaced this; we converged.) |
| Observation-only prototype (7 students) | **Lost** | experiment_log.md line 1770 names the file path as `/tmp/observation_prototype_results.json`. Same /tmp/ fate as the 3/7 original. The results table at log lines 1455–1465 is detailed enough to cite from the log. (B's note that `synthesis_first_prototype.json` in demo_baked is a *different* file with overlapping student counts is correct — confirmed independently.) |
| Test E reproduction on Gemma 12B (2026-03-27) | **Doesn't exist as named** | Test E was never run on Gemma 12B. The Gemma 12B reproduction is Test A's 10 records (`test_a_temperature_gemma12b_2026-03-26.json`). The s1 handoff's "Test E + rerun" phrasing conflates two tests. See Finding 4. |
| Original 32-student naive binary (2026-03-24) | **Lost** | `/tmp/` is empty of plausible files. No 2026-03-24-dated artifact in any repo. Git log -S for "not a wellbeing concern in itself" returns three commits, all post-loss. The rerun on `2026-04-26` is the substitute and serves as evidence the phenomenon survives current code. |

The only file actually recoverable from the four "missing" was `reading_first_comparison.json`. The other three are confirmed lost (one trivially recoverable from log narrative; two unrecoverable in any form).

---

## Audit assessment

The validation pass holds on its empirical core. The five corrections (MIXED tag confound, Test B run count, Test F sample size, Test C scoping, instability → deterministic on Test F preserved data) are supported by the JSONs. The analytical additions (hybrid mechanism, three-categories-of-instability typology, 12B > 27B finding, rerun spec) survive audit and are solid.

What needs revision before the paper drafts:

1. **The Test B and Test C corrections both need provenance qualifications** (Findings 1, 2). The right framing is "JSON shows X; log narrative describes Y; JSONs were committed retroactively; we report the JSON values while noting the log may describe an unpreserved run." That keeps both sources legible.

2. **The format/architecture conflation s1-A flagged is now baked into the Test B citation** (Finding 3). The paper should preserve s1-A's hedge explicitly; the held-architecture run remains the right gap to name in limitations rather than smooth over.

3. **The "16/16 across three model families" attribution should be replaced** with itemized counts per test (Finding 4). The data is stronger than that summary suggests; it just isn't structured the way the summary describes.

4. **The "production" label is in the data files**, not just in narrative summaries (Finding 6). Methods section needs to either acknowledge the test-infrastructure label drift or regenerate metadata with corrected labels.

What this audit *did not* find:
- Any false claim in the verification_table.md against the raw JSONs.
- Any hidden file recoverable beyond `reading_first_comparison.json`.
- Any analytical drift in the validation pass's framing besides the four items above.

The pass held under independent audit on its main moves. The remaining issues are not "the validation pass got it wrong" but "the validation pass took some claims as more settled than the data supports."

---

## On June's marginalia in REVIEW_FOR_JUNE.md

Reading June's inline annotations, three things landed for me:

- **"This was too binary again, so I fixed it."** (re: phenomenon-not-rate framing) — Worth carrying forward as a session-level pattern. The interface pane's framings under deadline pressure pulled toward binary either/or in several places (don't cite the rate / cite the phenomenon; production / research-track; either Test B is the format test or it isn't). June's marginalia consistently softens these into "both, with scoping." That softening is what the paper itself argues for at the level of output format. The same compression dynamic the paper documents was operating in the validation-pass framing.

- **"Compression COULD be purely informational — but several pieces of our data point to routing."** — This is more specific than the s1 handoff's "hybrid" framing. June reads the evidence as "both/and with directional weight toward routing"; the s1 handoff reads it as "both/and equally." That's a substantive scoping difference. If June wants the routing claim foregrounded, the paper's mechanism section can name routing as the load-bearing addition with informational compression as the necessary baseline, rather than presenting them as parallel.

- **"Maybe we need to underscore rigor > efficiency for the C2Cs."** — Worth flagging at SKILL_FEEDBACK level. The validation pass was thorough but compressed under time pressure; the things that broke (label drift propagating into JSON metadata, Test B prompt-architecture conflation surviving into "format test" framing, Test C log-vs-JSON conflict missed) all match the "efficiency-over-rigor" pattern June names. A C2C-protocol-level intervention might be: at every relay-note moment, the interface pane explicitly checks whether the framing it's about to send is binary where the evidence is graded.

---

## Coordination notes

- B's report was written ~7 hours before mine. I read mine in the conversation file before I read B's artifact, so my verifications were independent. Where we converge (reading_first_comparison.json found, Test B retroactive-provenance issue, Test A asset-framing prose verification, Test M S028 false-flag, rerun confirmation), the convergence is genuine.
- Where I add to B: Findings 1 (provenance issue is systematic across the 2026-03-26/27 batch, not just Test B), 2 (same conflict for Test C), 3 (Test B uses class context, collapsing format/architecture), 4 (16/16 attribution conflates Test A and Test E), 5 (Test B April reruns are 5 min apart), 6 (label drift propagated into JSON metadata).
- Where B's read may sharpen mine: B's option-c framing for the rerun ("phenomenon survives system tuning *including* explicit guards") is stronger than the validation-pass option-a/b framing. I agree.

— A
