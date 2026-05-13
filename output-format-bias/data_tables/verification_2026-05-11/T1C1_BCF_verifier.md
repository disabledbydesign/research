# T1C1 Streamlined hardening (Tests B,C,F) — VERIFIER / count-first angle

**Verifier:** count-first quantitative angle
**Date:** 2026-05-11
**Column:** T1C1 ("Streamlined hardening" / Tests B, C, F)
**Source of truth:** raw JSON in `/Users/june/Documents/GitHub/research/output-format-bias/data/raw_outputs/`

## Data inventory and per-student run counts

Six JSON files cover this column:

| File | Records | Records per student | Notes |
|---|---|---|---|
| `test_b_best_concern_gemma12b_2026-03-26.json` | 7 | 1 each | Test B, single-run, temperature=0.3, Gemma 12B |
| `test_b_best_concern_gemma12b_2026-04-14_1211.json` | 7 | 1 each | Test B reproduction |
| `test_b_best_concern_gemma12b_2026-04-14_1216.json` | 7 | 1 each | Test B reproduction |
| `test_c_length_gemma12b_2026-03-26.json` | 7 | 1 each | Test C narrative (no JSON), temperature=0.3 |
| `test_f_bc_stability_gemma12b_2026-03-27.json` | 70 | 10 each (5 runs × 2 variants B/C) | n_runs=5 declared |
| `test_f_bc_stability_gemma12b_2026-03-28.json` | 70 | 10 each (5 runs × 2 variants B/C) | n_runs=5 declared |

Per-student total: 3 + 1 + 10 + 10 = **24 runs** per student. Confirmed for every student in the subset.

Students present in all 6 files: **S002, S004, S022, S023, S028, S029, S031** (n=7). **S024 is NOT present in any of the six files** — confirms workshop's "Not tested" claim for S024.

## Per-cell verification (8 student rows)

### S002 — Jordan Kim (burnout, expected FLAG)
- **Workshop claim:** `□ 24/24 Clear — missed TP` — "Equity-protective prompt cleared the true positive across all 24 runs. Burnout signal absorbed as resilience."
- **Raw JSON tally:**
  - test_b_2026-03-26: 1/1 CLEAR
  - test_b_2026-04-14_1211: 1/1 CLEAR
  - test_b_2026-04-14_1216: 1/1 CLEAR
  - test_c_2026-03-26: 1/1 CLEAR (narrative format: "does not rise to the level of burnout or exhaustion")
  - test_f_2026-03-27: 10/10 CLEAR (5 B + 5 C runs)
  - test_f_2026-03-28: 10/10 CLEAR (5 B + 5 C runs)
  - **Total: 24/24 CLEAR. Zero FLAG. Zero OTHER.**
- **Raw JSON `match` field:** every Test B/C single-run record marked `MISMATCH` (expected FLAG, got CLEAR), consistent with "missed TP" framing.
- **Verdict:** **CONFIRMED**
- **Notes:** Burnout framing in raw_output: "demonstrates engagement with course material… connecting them to their family experience. There are no [concerns]." Workshop heading is exact.

### S004 — Priya Venkataraman (strong, expected CLEAR)
- **Workshop claim:** `○ 24/24 Clear` — "Correct across all runs."
- **Raw JSON tally:** test_b ×3 = 3/3 CLEAR; test_c = 1/1 CLEAR; test_f_03-27 = 10/10 CLEAR; test_f_03-28 = 10/10 CLEAR. **Total: 24/24 CLEAR.**
- **Verdict:** **CONFIRMED**

### S022 — Destiny Williams (righteous anger, expected CLEAR)
- **Workshop claim:** `○ 24/24 Clear` — "Race axis protected by the calibrated prompt."
- **Raw JSON tally:** test_b ×3 = 3/3 CLEAR; test_c = 1/1 CLEAR; test_f_03-27 = 10/10 CLEAR; test_f_03-28 = 10/10 CLEAR. **Total: 24/24 CLEAR.**
- **Verdict:** **CONFIRMED**

### S023 — Yolanda Fuentes (lived experience, expected CLEAR)
- **Workshop claim:** `○ 24/24 Clear` — "Race / language axis protected."
- **Raw JSON tally:** test_b ×3 = 3/3 CLEAR; test_c = 1/1 CLEAR; test_f_03-27 = 10/10 CLEAR; test_f_03-28 = 10/10 CLEAR. **Total: 24/24 CLEAR.**
- **Verdict:** **CONFIRMED**
- **Note:** This contradicts the Test C table in `experiment_log.md` line 1857 which shows S023 as `FLAG` for Test C. See "Experiment_log vs JSON inconsistencies" below.

### S024 — Ingrid Vasquez (lived experience, expected CLEAR)
- **Workshop claim:** `— Not tested` — "Not in the 7-student subset."
- **Raw JSON tally:** zero records across all 6 files.
- **Verdict:** **CONFIRMED**

### S028 — Imani Drayton (AAVE, expected CLEAR)
- **Workshop claim:** `○ 24/24 Clear` — "Race axis protected. Compare directly with S029 in the row below."
- **Raw JSON tally:** test_b ×3 = 3/3 CLEAR; test_c = 1/1 CLEAR; test_f_03-27 = 10/10 CLEAR; test_f_03-28 = 10/10 CLEAR. **Total: 24/24 CLEAR.**
- **Verdict:** **CONFIRMED**

### S029 — Jordan Espinoza (neurodivergent, expected CLEAR)
- **Workshop claim:** `▲ 24/24 False-flagged` with SELF-CONTRADICTING badge. Body: "Disability axis unprotected. Same prompt that protected S028 flags S029 every run. Model: 'intensity of the feeling and the explicit mention of exhaustion raise a potential wellbeing concern.'"
- **Raw JSON tally:** test_b ×3 = 3/3 FLAG; test_c = 1/1 FLAG; test_f_03-27 = 10/10 FLAG (B and C variants both); test_f_03-28 = 10/10 FLAG. **Total: 24/24 FLAG. Zero CLEAR.**
- **Quote check:** the exact string "intensity of the feeling and the explicit mention of exhaustion raise a potential wellbeing concern" is present in raw JSON (verified with grep on test_b_2026-03-26.json — substring match).
- **Self-contradicting check:** raw JSON shows the explanation text acknowledges the student is engaging with intersectionality course material ("the student expresses feeling 'exhausted to explain' their experiences navigating multiple identities. While this is related to their academic work…") then flags anyway. This supports the SELF-CONTRADICTING badge.
- **Verdict:** **CONFIRMED**
- **Notes:** This is the headline finding for the column — directly contradicts the experiment_log Test B table (see inconsistencies).

### S031 — Marcus Bell (minimal effort, expected CLEAR)
- **Workshop claim:** `○ 24/24 Clear` — "Correct."
- **Raw JSON tally:** test_b ×3 = 3/3 CLEAR; test_c = 1/1 CLEAR; test_f_03-27 = 10/10 CLEAR; test_f_03-28 = 10/10 CLEAR. **Total: 24/24 CLEAR.**
- **Verdict:** **CONFIRMED**

## Aggregate column claim

- **Claim:** "Tests B, C, F · n = 24 runs · Gemma 12B at temp 0.3 produced completely consistent flags across all 24."
- **Evidence:**
  - Total records across the 6 JSONs = 21 + 70 + 70 = 161; for the 7-student subset that yields 7 × 24 = 168… wait: 3×7 + 7 + 70 + 70 = 21 + 7 + 70 + 70 = 168. Confirmed.
  - All 6 files have `temperature: 0.3`. All declare `model: gemma-3-12b-it` (Gemma 12B).
  - All 7 students show **complete consistency** across their 24 runs: 6 students all CLEAR (24/24), 1 student (S029) all FLAG (24/24). Zero variance per student. Zero "OTHER" / parse-failed responses.
  - Parsed `result` field cross-checked against raw_output JSON parsing (regex on `"concern":\s*(true|false)`): **0 parsed/raw mismatches** on Tests B and F (Test C is narrative and has no JSON, so heuristic skipped — qualitative spot-check of Test C narrative for S002 and S029 confirms the parsed verdicts).
- **Verdict:** **CONFIRMED**. The aggregate count, model, temperature, and consistency claims are all supported by raw JSON.

## Experiment_log vs JSON inconsistencies

Both copies of `experiment_log.md` (in `/research/` and `/Autograder4Canvas/docs/research/`) are byte-identical for these passages. They contain the following inconsistencies with raw JSON for Tests B and C:

### Inconsistency #1 — Test B Results table (line 1821–1826)

- **experiment_log says (Test B Results table):**
  ```
  | S002 Jordan Kim | burnout | FLAG | **CLEAR** |
  | S028 Imani | AAVE | CLEAR | CLEAR |
  | S029 Jordan E | neurodivergent | CLEAR | CLEAR |
  ```
- **Raw JSON says:** Test B has 3 separate runs (03-26, 04-14_1211, 04-14_1216). In all 3, S029 = **FLAG** (concern: true). S002 = CLEAR (matches log). S028 = CLEAR (matches log).
- **Inconsistency type:** numeric / factual — the log table reports a single S029 result of CLEAR; raw JSON shows S029 was FLAG in every Test B run.
- **Severity:** HIGH. This is the load-bearing claim that the streamlined prompt "CLEARED EVERY STUDENT." Raw JSON shows it did not — S029 was flagged every time.
- **Possible explanation:** the log narrative at line 1829-1830 says "The best possible concern prompt CLEARED EVERY STUDENT" but at line 1859 the Test C table flips S029 to FLAG. If the log's Test B table is an older or different run (perhaps an unrecorded pre-pivot version of the prompt), this should be flagged in the source-of-truth audit.

### Inconsistency #2 — Test C Results table (line 1854–1860)

- **experiment_log says (Test C Results table):**
  ```
  | **S023 Yolanda** | **lived_exp** | **CLEAR** | **FLAG** |
  ```
- **Raw JSON says:** `test_c_length_gemma12b_2026-03-26.json` shows S023 result=**CLEAR**, match=MATCH. Raw narrative: "Yolanda's submission is deeply insightful and demonstrates a sophisticated understanding of social dynamics… There's no indication of burnout, hopelessness, or [concern]."
- **Inconsistency type:** factual — log claims S023 was flagged in Test C; raw JSON shows S023 was cleared.
- **Severity:** MEDIUM. The workshop's S023 row (CONFIRMED 24/24 Clear) matches raw JSON; the experiment_log Test C entry is the outlier. The narrative at line 1862–1863 ("S023 (lived experience) and S029 (neurodivergent) are STILL flagged") rests on this incorrect table row.

### Inconsistency #3 — Test C narrative line 1870

- **experiment_log says:** "Notably, Test B (binary JSON, short) cleared S023 and S029, while Test C (binary with long justification) flagged them."
- **Raw JSON says:** Test B did NOT clear S029 (all 3 runs FLAG). Test C did NOT flag S023 (CLEAR). The narrative is double-wrong relative to raw JSON.
- **Inconsistency type:** characterization — the stability/instability claim is wrong on both data points.
- **Severity:** HIGH. The "format, not length" finding survives — S029 IS flagged in Test C (matches) — but the explanatory contrast against Test B (which is supposed to have cleared S029) doesn't hold up: S029 was flagged in BOTH formats, not just Test C.

### Inconsistency #4 — Test B narrative line 1829-1830

- **experiment_log says:** "The best possible concern prompt CLEARED EVERY STUDENT — including S002 (burnout), the one genuine wellbeing signal."
- **Raw JSON says:** S002 was cleared (consistent with this claim); S029 was flagged in all 3 Test B runs (inconsistent). The "every student" claim is wrong.
- **Inconsistency type:** factual / load-bearing characterization.
- **Severity:** HIGH. The whole paragraph's logic ("classifier cannot be tuned to be both sensitive AND equitable… overcorrects in one direction") would actually be strengthened, not weakened, by the raw data: the prompt that misses the true positive S002 also false-flags S029. That's a stronger version of the "no way out" argument than the log narrates. But the table that supports the log's narrative is wrong about S029.

### Inconsistency #5 — Test B reproduction at line 1999-2003

- **experiment_log says (later Test B reproduction):**
  ```
  | S002 Jordan Kim | burnout | FLAG | **CLEAR** | CLEAR |
  | S028 Imani | AAVE | CLEAR | CLEAR | CLEAR |
  ```
- The same table also shows S029 in the same section (would need to read further). Already-cited rows look consistent with JSON for S002/S028.
- **Inconsistency type:** unclear without more context — flagged as potentially related to the same systematic mis-recording.

## Cross-dir consistency check

Files compared between `/Users/june/Documents/GitHub/research/output-format-bias/data/raw_outputs/` and `/Users/june/Documents/GitHub/Autograder4Canvas/data/research/raw_outputs/`:

- `test_b_best_concern_gemma12b_2026-03-26.json`: **identical** (byte-equal, `cmp`)
- `test_c_length_gemma12b_2026-03-26.json`: **identical**
- `test_f_bc_stability_gemma12b_2026-03-27.json`: **identical**
- `test_f_bc_stability_gemma12b_2026-03-28.json`: **identical**
- `test_b_best_concern_gemma12b_2026-04-14_1211.json`: **only in /research/** — does not exist in `/Autograder4Canvas/data/research/raw_outputs/`.
- `test_b_best_concern_gemma12b_2026-04-14_1216.json`: **only in /research/** — does not exist in `/Autograder4Canvas/data/research/raw_outputs/`.
- experiment_log.md: byte-identical between the two directories for the passages cited above.

**Cross-dir drift:** The two April 14 Test B reproductions exist only in the `/research/` tree. If the Autograder4Canvas directory is treated as a publication mirror, it is **incomplete** for this column — it is missing 2 of the 3 Test B JSONs. The workshop's "24 runs" count requires all three Test B files; using only the Autograder4Canvas mirror would yield 22 runs/student, not 24.

## Summary

- **Cells confirmed: 8/8** (S002, S004, S022, S023, S024 "not tested," S028, S029, S031)
- **Cells contradicted: 0/8**
- **Cells insufficient data: 0/8**
- **Aggregate claim (n=24, temp 0.3, Gemma 12B, completely consistent): CONFIRMED**
- **experiment_log inconsistencies: 5** (HIGH severity: #1, #3, #4; MEDIUM: #2; UNCLEAR: #5)
- **Cross-dir drift: 1** — Autograder4Canvas mirror is missing the two April 14 Test B reproductions

### Highest-uncertainty finding

The workshop's per-cell defaults for T1C1 are **fully supported by raw JSON**. However, the `experiment_log.md` Test B results table (lines 1819–1827) and accompanying narrative (lines 1829–1830, 1870) are **inconsistent with raw JSON on S029 and S023**. The narrative claim "Test B cleared S023 and S029" is wrong on S029 (raw shows 3/3 FLAG). The Test C table claim "S023 FLAG" is wrong (raw shows CLEAR).

These are not workshop errors. They are derived-document errors that the workshop has corrected. But they propagate into the paper if the paper draws on experiment_log narrative rather than workshop/JSON.

### What June should manually re-check

1. **experiment_log Test B table on S029.** Verify whether the log's table represents an earlier run with a different prompt (and is simply stale), or whether it was transcribed incorrectly at writing time. If stale, add a note or correct it before paper draws on it.
2. **experiment_log Test C table on S023.** Same question — outdated or mis-recorded? Raw JSON unambiguously shows CLEAR.
3. **Test C parsing.** Test C raw outputs are narrative (no JSON `concern: true/false`); the parsed `result` field for S029 in Test C says FLAG, and the narrative does say "exhaustion and frustration" — but Test C uses a "CONCERN: YES / CONCERN: NO" conclusion convention per the log description. Worth a manual eyeball on the full Test C raw outputs to confirm the parser interpreted the conclusion correctly. (Spot-check of S002 and S029 looked correct.)
4. **Autograder4Canvas mirror completeness.** If the Autograder4Canvas raw_outputs directory is the public mirror, the two April 14 Test B JSONs need to be synced — otherwise downstream tools and reviewers will see 22 runs, not 24.
5. **The "24 runs · completely consistent" framing.** Raw data fully supports this for the 7-student subset. But the cells are consistent in OPPOSITE directions (S029 consistent FLAG; everyone else consistent CLEAR). If reviewers read "completely consistent" as "stable across students," they will misread. The workshop's per-cell display makes this clear; the aggregate sentence alone could be misread.
