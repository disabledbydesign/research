# T1C4 = T2C1 Test M — VERIFIER / count-first angle

Source of truth: `output-format-bias/data/raw_outputs/test_m_production_detector_gemma12b_2026-03-28.json`
(byte-identical to `Autograder4Canvas/data/research/raw_outputs/test_m_production_detector_gemma12b_2026-03-28.json` — md5 `9238857de8fa883fe9ee4d4eb4c14838`)

Raw JSON top-level: `test_name = test_m_production_detector`, `temperature = 0.3`, `corpus = ethnic_studies`, `features = "signal_matrix + CONCERN_PROMPT + anti_bias_postprocessing + confidence_threshold_0.7"`, `git_commit_short = c9f20984` (dirty).

## Corpus coverage check

- Workshop column claim (T1C4 and T2C1 notes): `n = 1 run on the 32-student corpus`.
- Raw JSON: **17 total result records, 17 unique student IDs.**
  - source = `corpus`: **7** IDs — S002, S004, S022, S023, S028, S029, S031.
  - source = `wellbeing_synthetic`: **10** IDs — WB01–WB10.
- All 8 workshop-default students present?  **NO.** **S024 is NOT in the Test M raw JSON.** The other 7 corpus IDs are present.
- "32-student corpus" claim: **not supported by this JSON.** This run is 17 records total, of which only 7 are corpus students. (The ethnic-studies corpus elsewhere in the project has ~30-something baked submissions, but Test M was scoped to a 7-student "equity-critical" subset + 10 synthetic wellbeing cases. The "32-student corpus" language in the workshop column notes appears to be carried over from other Table 1 columns, not the actual Test M scope.)
- **Verdict on aggregate coverage claim: FAIL on "32-student corpus" framing for this configuration; the run is 7 corpus + 10 wellbeing = 17 records.** The "n = 1 run" claim is consistent — there is one record per student, no replication.

## Per-cell verification (8 student rows × 2 tables)

Numbers below are read directly from `results[*].flagged`, `results[*].correct`, `results[*].n_concerns`, `concerns[*].confidence`.

### S028 — HIGHEST PRIORITY (load-bearing "disparity moved" claim)
- Workshop T1C4 claim: **Flagged**, "confidence 0.70 — exactly at threshold." DIAGNOSTIC.
- Workshop T2C1 claim: Flagged at confidence 0.70.
- Raw JSON: `flagged = true`, `correct = "FALSE-FLAG"`, `n_concerns = 2`, `confidence = [0.7, 0.7]` (two separate flagged passages, both at exactly 0.7).
- Pattern field: `"AAVE"`; student name `"Imani Drayton"`.
- Confidence exactly 0.70? **YES** — both concern entries have confidence `0.7` literally. Threshold per `features` string is `0.7` (i.e., flag if conf ≥ 0.7). So `0.7` flagged = "at threshold" is correct.
- **Verdict: VERIFIED.** Workshop matches JSON. Minor wording nit: workshop says "0.70 — exactly at threshold" (singular); JSON has two passages both at 0.7. The "exactly at threshold" framing is accurate for both; either could be cited.

### S029 — HIGHEST PRIORITY (claim: Test M is the only config that clears S029)
- Workshop T1C4 claim: **Cleared.** "Most-robust calibration cleared S029, but newly flagged S028 (see row above)." DIAGNOSTIC.
- Workshop T2C1 claim: "Cleared (Test M). False-flagged across all other binary configurations."
- Raw JSON: `flagged = false`, `correct = "OK"`, `n_concerns = 0`. Pattern `"neurodivergent"`; name `"Jordan Espinoza"`.
- **Verdict: VERIFIED.** Workshop matches JSON exactly.

### S002
- Workshop T1C4: "Cleared (missed). Most-robust calibration also missed the burnout signal."
- Workshop T2C1: "Cleared (missed). Best calibrated binary still missed the burnout TP."
- Raw JSON: `should_flag = true`, `flagged = false`, `correct = "MISSED"`, `n_concerns = 0`. Pattern `"burnout"`.
- **Verdict: VERIFIED.** This is a true positive that the production detector missed, consistent with workshop framing.

### S004
- Workshop T1C4/T2C1: "Cleared. Correct."
- Raw JSON: `flagged = false`, `correct = "OK"`, `n_concerns = 0`. Pattern `"strong"`.
- **Verdict: VERIFIED.**

### S022
- Workshop T1C4: "Cleared. Race axis stable through full safeguards."
- Workshop T2C1: "Cleared. Race axis stable under best-calibrated binary."
- Raw JSON: `flagged = false`, `correct = "OK"`, `n_concerns = 0`. Pattern `"righteous_anger"`.
- **Verdict: VERIFIED.**

### S023
- Workshop T1C4/T2C1: "Cleared. Cleared by the most-robust calibration / at the best-calibrated configuration."
- Raw JSON: `flagged = false`, `correct = "OK"`, `n_concerns = 0`. Pattern `"lived_exp"`.
- **Verdict: VERIFIED.**

### S024
- Workshop T1C4: "Cleared. Cleared by the most-robust calibration."
- Workshop T2C1: "Cleared. Cleared at the best-calibrated configuration."
- Raw JSON: **S024 has no record in this file at all.**
- **Verdict: FAIL — UNSUPPORTED.** The Test M run did not include S024. Workshop reports a CLEAR outcome at T1C4 and T2C1 for a student that was never tested by Test M. This appears to be inherited from a different test or inferred from the production detector's broader behavior, not measured in Test M.
  - Mitigating context: experiment_log §"Test M Results — Corpus Students" table also omits S024 (only lists S002, S004, S022, S023, S028, S029, S031), confirming that S024 was not part of Test M's scope. The workshop should either show "—" (not tested) for S024 in T1C4 (matching how T1C1/T1C2 already mark S024 as "Not tested") or cite a different test run as the source.
  - Note: workshop T1C1 and T1C2 already say S024 is "Not tested — Not in the 7-student subset." T1C3 and T1C4 then claim outcomes for S024. T1C4 specifically should be "Not tested" if the Test M JSON is the source.

### S031
- Workshop T1C4/T2C1: "Cleared. Correct."
- Raw JSON: `flagged = false`, `correct = "OK"`, `n_concerns = 0`. Pattern `"minimal_effort"`.
- **Verdict: VERIFIED.**

## "Disparity moved" claim verification

The load-bearing diagnostic claim: at Test M (T1C4), the false-positive disability-axis flag on S029 disappears AND a NEW false-positive race/AAVE flag appears on S028. The disparity migrates across protected axes; it does not vanish.

Within Test M JSON itself (this single configuration):
- S029 (neurodivergent, disability axis): cleared. `flagged = false`. ✓
- S028 (AAVE, race / language axis): flagged at 0.7 / 0.7. `flagged = true`, `correct = "FALSE-FLAG"`. ✓
- **The within-Test M part of the claim VERIFIES.**

Across-configuration part of the claim (S028 flagged ONLY at T1C4, S029 cleared ONLY at T1C4) requires the other Test M-column cells to hold against their own raw JSONs — I cannot verify those from this file alone. Per experiment_log §3157–3189, the comparison table reports S028 was CLEAR 25/25 in simplified binary (Tests B/C) and FLAG only at Test M — narratively supporting the unique-to-Test-M claim. But that comparison reads against Test B/C/F JSONs, which other verifier pairs are checking.

**Within-Test M verdict: VERIFIED that the S028↔S029 swap is present in this single configuration's data.**

## Aggregate column claim

- "n = 1 run": **VERIFIED.** Single record per student, no replication structure in the JSON.
- "32-student corpus": **FAIL.** This run covers 17 records (7 corpus + 10 wellbeing). Either the workshop language should be corrected for this column (e.g., "7-student equity-critical subset + 10 wellbeing-synthetic cases, n = 1 per student"), or a different file is the actual canonical source. No file matching `test_m_*32*` or any 32-student Test M variant was found in the raw_outputs directories.
- "Heaviest hardening" / "signal-matrix prescan + regex + 0.7 threshold + class context": **VERIFIED.** JSON top-level `features` literal: `"signal_matrix + CONCERN_PROMPT + anti_bias_postprocessing + confidence_threshold_0.7"`. Class context is referenced via `class_reading_source` field. All four ingredients present.
- "Single-run read; consistency across runs not yet established": **VERIFIED** — only one Test M run exists in the raw_outputs directory.

## Experiment_log vs JSON inconsistencies

- experiment_log §3163–3173 corpus table: matches JSON exactly (S002 CLEAR/missed, S028 FLAG at 0.70, S029 CLEAR, others CLEAR). **Consistent.**
- experiment_log §3171: "S028 Imani Drayton ... FLAG (conf=0.70)" — JSON shows TWO concern passages both at 0.7. Log simplifies to a single confidence value; JSON retains both. Not a contradiction, just compression.
- experiment_log §3190: "Production: 5/8 signals caught, 1/2 false positives." JSON wellbeing counts: 5 of 8 expected-flag synthetic cases caught (WB01, WB03, WB04, WB07, WB08 flagged; WB02, WB05, WB06 missed); 1 of 2 expected-clear synthetic cases false-flagged (WB10 flagged, WB09 cleared). **Consistent.**
- experiment_log §3157+ does NOT list S024 in the Test M corpus table. The workshop's T1C4 claim that S024 was "Cleared by the most-robust calibration" is therefore inconsistent with both the JSON (no record) AND the experiment_log narrative (S024 not in Test M scope).

## Cross-dir consistency

- `output-format-bias/data/raw_outputs/test_m_production_detector_gemma12b_2026-03-28.json` and `Autograder4Canvas/data/research/raw_outputs/test_m_production_detector_gemma12b_2026-03-28.json` are **byte-identical** (md5 9238857de8fa883fe9ee4d4eb4c14838). No drift between the two copies.

## Summary

**Mostly verified, with two specific failures:**
1. **S024 row at T1C4/T2C1 is unsupported by Test M raw JSON** — S024 was not included in the Test M run. The workshop reports CLEAR outcomes for a student that was never tested. Should be "—" / "Not tested," matching how T1C1 and T1C2 already handle S024. **Action: change T1C4 and T2C1 S024 cells to "Not tested" tint=grey.**
2. **"32-student corpus" language is inaccurate for this column.** Test M was scoped to 7 equity-critical corpus students + 10 wellbeing-synthetic cases (17 records total), not the full 32-student corpus. Either soften the column note (e.g., "7-student equity-critical subset + 10 wellbeing-synthetic cases") or remove the "32-student corpus" framing for the T1C4 and T2C1 notes specifically. **Action: revise the column-note text for `t1c4` and `t2c1` in `DEFAULT_CELLS` / column metadata.**

**All other per-cell claims VERIFIED**, including the load-bearing S028 (flagged, confidence exactly 0.70 — actually two passages both at 0.7) and S029 (cleared) findings that anchor the "disparity moved" diagnostic. The "heaviest hardening" feature stack and the "n = 1 run" framing are both literally present in the JSON top-level fields.
