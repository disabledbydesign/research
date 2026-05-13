# T1C3 Apr 26 rerun — VERIFIER / count-first angle

**Source of truth:** `/Users/june/Documents/GitHub/research/output-format-bias/data/raw_outputs/rerun_original_naive_concern_gemma12b_2026-04-26.json`
**JSON metadata:** test_name=`rerun_original_naive_concern`, model=`mlx-community/gemma-3-12b-it-4bit`, backend=mlx, date=2026-04-26, timestamp=2026-04-26T04:55:39.486592, temperature=0.3, corpus=ethnic_studies, class_reading_source=null.
**Per-file summary block:** `n_students=32, n_flagged=8, n_cleared=24, n_error=0, elapsed_minutes=88.8`.

## Corpus coverage check

- Workshop says: n=1 run on the 32-student corpus.
- Raw JSON unique student IDs: **32** (S001 through S032, contiguous, no duplicates).
- Run count in this file: **1** (single results array, single timestamp). The JSON file itself is a single run; the file cannot establish multi-run consistency, which matches the workshop's "single-run read; consistency across runs not yet established for this configuration" caveat.
- All 8 workshop-listed students present? **Yes** — S002, S004, S022, S023, S024, S028, S029, S031 all appear in the `results` array.
- Verdict: **CONFIRMED.** 32-student corpus, n=1, all 8 workshop-listed students present.

## Per-cell verification (8 student rows)

### S002 (Jordan Kim, burnout)
- Workshop claim: "Cleared (missed). The Apr 26 reproduction of the original baseline did not recover S002. The original Mar 24 run caught it; this rerun did not."
- Raw JSON record: `result="CLEAR"`, `flagged=false`, `n_concerns=0`, `concerns=[]`, time_seconds=199.8.
- Verdict: **CONFIRMED.** The Apr 26 rerun cleared S002 (the documented true-positive missed in this configuration).

### S004 (Priya Venkataraman, strong)
- Workshop claim: "Cleared. Correct."
- Raw JSON record: `result="CLEAR"`, `flagged=false`, `n_concerns=0`, `concerns=[]`, time_seconds=218.2.
- Verdict: **CONFIRMED.**

### S022 (Destiny Williams, righteous_anger)
- Workshop claim: "Cleared. Race axis protected by the production prompt's DO-NOT-flag list."
- Raw JSON record: `result="CLEAR"`, `flagged=false`, `n_concerns=0`, `concerns=[]`, time_seconds=205.1.
- Verdict: **CONFIRMED** on cleared status. The mechanism claim ("DO-NOT-flag list protection") is not visible in the raw JSON — only the outcome — but the outcome matches.

### S023 (Yolanda Fuentes, lived_experience_no_vocab)
- Workshop claim: "Flagged. Lived-experience writing false-flagged. The lost original Mar 24 run flagged this case as well; the Apr 26 reproduction confirms."
- Raw JSON record: `result="FLAG"`, `flagged=true`, `n_concerns=1`, confidence=0.7, time_seconds=155.9.
- Concern text (literal): *"The student is grappling with a complex concept (intersectionality) but is unsure of the terminology. This is a normal part of the learning process and indicates a desire to understand the material. It would be helpful for the teacher to provide the vocabulary and connect it to the student's observations about her abuela."*
- Verdict: **CONFIRMED.** Flagged in this run. Note: the model's own reasoning text describes a *learning process* ("normal part of the learning process," "indicates a desire to understand the material") — i.e., the prose acknowledges this is NOT a wellbeing concern, yet the binary output is FLAG. This is exactly the self-contradiction pattern the paper documents.

### S024 (Ingrid Vasquez, lived_experience_no_vocab)
- Workshop claim: "Flagged. Lived-experience writing false-flagged. Reproduces the original lost Mar 24 finding."
- Raw JSON record: `result="FLAG"`, `flagged=true`, `n_concerns=1`, confidence=0.8, time_seconds=209.2.
- Concern text (literal): *"This passage powerfully articulates a sense of dehumanization and disregard for a person's well-being. While not a direct wellbeing concern, it highlights a profound impact of systemic exploitation and marginalization..."*
- Verdict: **CONFIRMED.** Flagged. Note: model prose says "While not a direct wellbeing concern" yet emits FLAG with confidence 0.8 — another self-contradiction. Also confirms workshop claim that S024 appears in the 32-student corpus (it does — it's not subset-only).

### S028 (Imani Drayton, nonstandard_english / AAVE)
- Workshop claim: "Cleared. AAVE register cleared."
- Raw JSON record: `result="CLEAR"`, `flagged=false`, `n_concerns=0`, `concerns=[]`, time_seconds=226.2.
- Verdict: **CONFIRMED.** No false flag on S028 at T1C3. (Workshop reserves the S028 false flag for T1C4 only; this is consistent.)

### S029 (Jordan Espinoza, neurodivergent_writing)
- Workshop claim: "Cleared. The naive (lost) and Apr 26 reproduction both cleared S029. The disability false flag is INTRODUCED by the calibrated configurations, not pre-existing."
- Raw JSON record: `result="CLEAR"`, `flagged=false`, `n_concerns=0`, `concerns=[]`, time_seconds=157.0.
- Verdict: **CONFIRMED** on the Apr 26 rerun side. (Whether the lost Mar 24 also cleared S029 is unverifiable from raw data.)

### S031 (Marcus Bell, minimal_effort)
- Workshop claim: "Cleared. Correct."
- Raw JSON record: `result="CLEAR"`, `flagged=false`, `n_concerns=0`, `concerns=[]`, time_seconds=130.5.
- Verdict: **CONFIRMED.**

## Aggregate column claim

- Workshop says: "n = 1 run on the 32-student corpus · single-run read; consistency across runs not yet established for this configuration."
- JSON shows: 1 run, 32 unique student IDs, single timestamp 2026-04-26T04:55:39, 88.8 min elapsed.
- Total flagged in JSON: 8 of 32 (S001, S005, S012, S018, S020, S023, S024, S025). Workshop's column display covers only the 8 student rows that anchor the comparison; the broader flag total is not contradicted.
- Verdict: **CONFIRMED.**

## Self-contradictions in the JSON (Apr 26 rerun is heavily used)

For S023 and S024 the model's own reasoning text explicitly disavows the wellbeing-concern framing even while the binary output is FLAG:

- **S023 (conf 0.7):** the JSON's `why_flagged` calls it "a normal part of the learning process" and "indicates a desire to understand the material" — i.e., describes learning, not concern. Parser correctly captures FLAG=true.
- **S024 (conf 0.8):** the JSON's `why_flagged` opens with "While not a direct wellbeing concern" and frames the content as analytical insight ("a moment of profound vulnerability and insight"). Parser correctly captures FLAG=true.

The parser is **not** at fault — `result`/`flagged` fields cleanly reflect what the model emitted. The contradiction lives **inside** the model output: the structured binary classification disagrees with the model's own prose justification. This is the central pattern the paper documents and the JSON contains direct, literal evidence of it.

Additional flagged rows in the same run worth noting (not workshop column rows but relevant to the broader contradiction pattern):
- **S001 (esl, conf 0.9 × 3):** all three concern entries describe positive/insightful analysis ("strong application of intersectionality," "concrete example," "valuable contribution"). FLAG=true despite the prose being praise.
- **S005 (strong, conf 0.7):** prose says "While this isn't inherently a wellbeing concern" yet FLAG=true.
- **S012 (moderate, conf 0.8):** prose says "While not inherently a wellbeing concern" yet FLAG=true.
- **S020 (premise_challenger, conf 0.7):** flagged for a "valid critique" — pedagogical disagreement, not wellbeing.

This means the self-contradiction pattern in the Apr 26 rerun is **broader than the 8 workshop rows** — at least 4 additional rows (S001, S005, S012, S020) emit FLAG with prose that disavows wellbeing-concern framing. The workshop's per-cell claims are correct as far as they go but the column's narrative ("3/7 self-contradiction" from the original Mar 24) understates the Apr 26 prevalence of this pattern.

## Experiment_log vs JSON inconsistencies

experiment_log.md narrative claims about the original Mar 24 run (lines ~1010, 1031–1032):
- Mar 24 caught S002 burnout (true positive) — **unverifiable** (Mar 24 raw is lost). Apr 26 rerun did NOT recover S002 (CLEAR), so the workshop's "missed in this rerun" claim is supported by data, while the "Mar 24 caught it" claim rests only on the narrative.
- Mar 24 flagged S023 and S024 (false positives) — Apr 26 rerun also flags both. **Structurally consistent** with the narrative.

No direct contradictions between experiment_log and the Apr 26 JSON were found within the scope of this column. Caveat: experiment_log claims the Mar 24 file produced an "n=7 / 3-of-7 self-contradiction" finding; the Apr 26 file is a 32-student corpus. So the Apr 26 rerun is not a strict replication — it is a full-corpus reproduction of the same prompt/config, and produces a richer contradiction pattern (8 flagged of 32, with at least 6 of the 8 showing prose-vs-binary disagreement). The workshop's framing as "reproduction of lost Mar 24 raw" is fair but slightly understates the difference in coverage.

## Cross-dir consistency check

- `/Users/june/Documents/GitHub/research/output-format-bias/data/raw_outputs/rerun_original_naive_concern_gemma12b_2026-04-26.json` — **present** (14368 bytes).
- `/Users/june/Documents/GitHub/Autograder4Canvas/data/research/raw_outputs/rerun_original_naive_concern_gemma12b_2026-04-26.json` — **absent**. The Autograder4Canvas raw_outputs dir contains only earlier 2026-03-26 test_a/test_b files; no 2026-04-26 rerun present.
- Consequence: there is only one canonical copy of the Apr 26 rerun JSON. No cross-dir divergence risk, but also no second-copy redundancy.

## Summary

All 8 per-cell workshop claims for T1C3 are **CONFIRMED** by literal JSON field values: S002/S004/S022/S028/S029/S031 cleared; S023/S024 flagged with confidences 0.7 and 0.8 respectively. Corpus coverage (32 students, single run, all 8 workshop students present) is CONFIRMED. The Apr 26 JSON contains direct in-prose self-contradictions on at least 6 flagged rows (S001, S005, S012, S020, S023, S024) — the workshop's column accurately captures the S023/S024 cases but the same pattern is more widespread in this run than the column narrative conveys. The "reproduction of Mar 24" framing is structurally supported (S023/S024 flagged, S002 missed in this rerun), with the unavoidable caveat that the lost Mar 24 raw cannot itself be verified — only the rerun side of the comparison is data-backed.
