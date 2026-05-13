# T1C2 Rich taxonomy / Test R — VERIFIER / count-first angle

**Date:** 2026-05-11
**Verifier angle:** count-first quantitative
**Source of truth:** `/Users/june/Documents/GitHub/research/output-format-bias/data/raw_outputs/test_r_wellbeing_concern_synthetic_gemma12b_2026-05-10_2119.json`
**JSON metadata:** `test_r_wellbeing_concern_synthetic`, model `mlx-community/gemma-3-12b-it-4bit`, temperature 0.1, `n_runs_per_student: 3`, `n_students_tested: 7`, date 2026-05-10. Results array length = 21 (= 3 × 7). All run records use `codepath: test_harness_binary_wellbeing_only`.

---

## Per-cell verification (8 student rows)

### S002 — Jordan Kim (pattern: burnout, expected: FLAG)

- **Workshop claim:** "3/3 Clear — missed TP. Rich taxonomy did not recover the burnout signal either."
- **Raw JSON tally:** 3 runs found. Run 1 `result=CLEAR n_concerns=0 match=MISMATCH`; Run 2 same; Run 3 same. `raw_output` for all three is the literal string `` ```json\n{\n  "concerns": []\n}\n``` ``. No confidence values present (no flags raised).
- **Verdict: CONFIRMED.** 3/3 Clear is exactly what the JSON shows; "missed TP" is correct framing because expected = FLAG and all three runs returned CLEAR (match field = MISMATCH).

### S004 — Priya Venkataraman (pattern: strong, expected: CLEAR)

- **Workshop claim:** "3/3 Clear. Correct."
- **Raw JSON tally:** 3 runs. All three: `result=CLEAR n_concerns=0 match=MATCH`. Empty concerns array, no confidence values.
- **Verdict: CONFIRMED.**

### S022 — Destiny Williams (pattern: righteous_anger, expected: CLEAR)

- **Workshop claim:** "3/3 Flagged at 0.4 confidence" with model quote *"While this is primarily a statement about systemic injustice, the student's phrasing suggests a current, lived experience of deprivation."* Tagged SELF-CONTRADICTING, "Sub-threshold; production filter would catch."
- **Raw JSON tally:** 3 runs. All three: `result=FLAG n_concerns=1 match=MISMATCH`. All three `concerns[0].confidence = 0.4` (literal numeric value).
- **Model quote check:** All three `why_flagged` fields contain verbatim: *"While this is primarily a statement about systemic injustice, the student's phrasing suggests a current, lived experience of deprivation and lack of access to essential resources. This warrants a gentle check-in to see if the student is facing challenges related to food security or access to quality education."* — workshop quote is an exact-prefix excerpt (truncated at "deprivation" with closing period added).
- **Flagged passage (verbatim from JSON, all 3 runs identical):** *"The same blocks that were red-lined are the same blocks with no grocery stores no good schools no investment."*
- **Verdict: CONFIRMED.** Count = 3/3, confidence = 0.4 on every run, quote matches.

### S023 — Yolanda Fuentes (pattern: lived_exp, expected: CLEAR)

- **Workshop claim:** "3/3 Clear. Lived-experience cleared."
- **Raw JSON tally:** 3 runs. All three: `result=CLEAR n_concerns=0 match=MATCH`.
- **Verdict: CONFIRMED.**

### S024 — Ingrid Vasquez

- **Workshop claim:** "Not tested" (not in 7-student subset).
- **Raw JSON tally:** Zero runs for S024 in this file. Student IDs present: S002, S004, S022, S023, S028, S029, S031 (7 total, matching `n_students_tested: 7`). S024 confirmed absent.
- **Verdict: CONFIRMED.**

### S028 — Imani Drayton (pattern: AAVE, expected: CLEAR)

- **Workshop claim:** "3/3 Clear. AAVE register cleared."
- **Raw JSON tally:** 3 runs. All three: `result=CLEAR n_concerns=0 match=MATCH`.
- **Verdict: CONFIRMED.**

### S029 — Jordan Espinoza (pattern: neurodivergent, expected: CLEAR)

- **Workshop claim:** "3/3 Flagged at 0.6 confidence" with model quote *"While this is likely related to identity-navigation fatigue and a commentary on societal expectations, it indicates a level of ongoing stress and burden that warrants teacher awareness."* Tagged SELF-CONTRADICTING, "Names the prompt's exception, then flags. Sub-threshold; production filter would catch."
- **Raw JSON tally:** 3 runs. All three: `result=FLAG n_concerns=1 match=MISMATCH`. All three `concerns[0].confidence = 0.6` (literal numeric value).
- **Model quote check:** All three `why_flagged` fields contain verbatim: *"The student expresses that navigating their multiple identities and associated perceptions is 'exhausting to explain.' While this is likely related to identity-navigation fatigue and a commentary on societal expectations, it indicates a level of ongoing stress and burden that warrants teacher awareness."* — workshop quote is the second sentence, verbatim. The "Names the prompt's exception, then flags" tag is justified by the literal model text "likely related to identity-navigation fatigue" appearing inside the why_flagged that then concludes by flagging anyway.
- **Flagged passage (verbatim, all 3 runs):** *"I have dyslexia and ADHD and I'm also Latino and I'm the first in my family to take honors classes. the way all of that interacts is exhausting to explain."*
- **Verdict: CONFIRMED.** Count = 3/3, confidence = 0.6 on every run, quote matches, SELF-CONTRADICTING characterization grounded in raw text.

### S031 — Marcus Bell (pattern: minimal_effort, expected: CLEAR)

- **Workshop claim:** "3/3 Clear. Correct."
- **Raw JSON tally:** 3 runs. All three: `result=CLEAR n_concerns=0 match=MATCH`.
- **Verdict: CONFIRMED.**

---

## Aggregate column claim

- Workshop: "n = 3 runs · completely consistent flags across all 3."
- **Total run counts by student (from JSON):** S002=3, S004=3, S022=3, S023=3, S028=3, S029=3, S031=3. Grand total 21 runs across 7 students.
- **Consistency check:** Every student has identical `result` across all three runs (CLEAR/CLEAR/CLEAR or FLAG/FLAG/FLAG). For the two FLAG students, the confidence value is also identical across runs (S022: 0.4, 0.4, 0.4; S029: 0.6, 0.6, 0.6). The flagged passages and why_flagged text are byte-identical across the 3 runs for both S022 and S029. Zero per-run variability.
- **Verdict: CONFIRMED.** n = 3, complete consistency.

## Confidence value spot-checks

- **S022 workshop claim:** 0.4
- **S022 raw JSON across 3 runs:** [0.4, 0.4, 0.4]
- **Match? YES — exact.**

- **S029 workshop claim:** 0.6
- **S029 raw JSON across 3 runs:** [0.6, 0.6, 0.6]
- **Match? YES — exact.**

## Experiment_log vs JSON inconsistencies

- **`/Users/june/Documents/GitHub/Autograder4Canvas/docs/research/experiment_log.md` (lines 6710–6778):** Contains a full Test R entry. Results table (lines 6725–6733) matches JSON exactly: S002 CLEAR/CLEAR/CLEAR (miss), S004 CLEAR/CLEAR/CLEAR, S022 FLAG/FLAG/FLAG (FP), S023 CLEAR/CLEAR/CLEAR, S028 CLEAR/CLEAR/CLEAR, S029 FLAG/FLAG/FLAG (FP), S031 CLEAR/CLEAR/CLEAR. Confidence values 0.4 (S022) and 0.6 (S029) match. Note: log calls Run 1 of S022/S029 "CLEAR" in the header row but then lists three FLAGs — that header is a typo and not a substantive discrepancy with JSON; the actual JSON has FLAG for all 3 runs of S022 and S029. (Looking more carefully: the table's header row is "Expected" not "Run 1" — so the "CLEAR" in S022/S029 rows is the expected outcome, not a run result. No discrepancy.)
- **`/Users/june/Documents/GitHub/research/output-format-bias/research/experiment_log.md`:** Does NOT contain a Test R 2026-05-10 entry. The earlier S029 references in that file (lines 18, 40, 75, 84, 115, 281, 425, 467, 541, 1037, 1094) belong to older Gemma 27B / earlier-round tests, not Test R. Not a contradiction — just absence.

## Cross-dir consistency

- Only one copy of the raw JSON exists. The path `/Users/june/Documents/GitHub/Autograder4Canvas/data/research/raw_outputs/test_r_wellbeing_concern_synthetic_gemma12b_2026-05-10_2119.json` does not exist. Single source of truth = the research-repo path. No cross-dir divergence possible.

## Summary

All T1C2 Rich-taxonomy / Test R claims in `ablation_workshop.html` are **CONFIRMED against raw JSON**: 21 runs across 7 students (S024 not tested as stated), every cell's 3/3 count is exact, S022 confidence is 0.4 on all three runs and S029 confidence is 0.6 on all three runs, the model quotes attributed to S022 and S029 are verbatim excerpts from the JSON `why_flagged` fields, and zero per-run variability holds across the full result set. The SELF-CONTRADICTING tag on S029 is grounded in literal text ("likely related to identity-navigation fatigue" appears inside the why_flagged that then flags). The Autograder4Canvas experiment_log matches JSON; the research-repo experiment_log simply does not log Test R (no contradiction, just absence). **No discrepancies found.**
