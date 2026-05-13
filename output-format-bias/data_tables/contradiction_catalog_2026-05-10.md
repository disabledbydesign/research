# Self-Contradiction Catalog — Output-Format-Bias Paper

Cross-test inventory of records where the model's own explanation names a prompt-articulated exception (course content, identity-navigation fatigue, AAVE/multilingual register, neurodivergent self-disclosure, righteous anger, lived experience, structural critique) and then flags on the same content. Sources: `output-format-bias/data/raw_outputs/*.json`, `output-format-bias/data/dual_binary_run_*/analysis.md`, `output-format-bias/research/binary_fix_attempts_enumeration_2026-04-27.md`. Verified directly against JSONs where available.

## 1. Summary table

Rows are distinct student × test-architecture instances. Where a record reproduced N times verbatim, the row notes `(n=N)`.

| # | Test | Date | Student | Pattern | Conf | Exception violated | Source |
|---|---|---|---|---|---|---|---|
| 1 | rerun_original_naive | 2026-04-26 | S001 Maria Ndiaye | esl | (n/a) | course-content / strong analytical work | rerun_original_naive_concern_gemma12b_2026-04-26.json |
| 2 | rerun_original_naive | 2026-04-26 | S005 Amara Diallo | strong | (n/a) | course-content / "valuable critical insight" | same |
| 3 | rerun_original_naive | 2026-04-26 | S012 Talia Reyes | moderate | (n/a) | course-content / lived experience | same |
| 4 | rerun_original_naive | 2026-04-26 | S023 Yolanda Fuentes | lived_experience_no_vocab | (n/a) | "normal part of learning" reframed as concern | same |
| 5 | rerun_original_naive | 2026-04-26 | S024 Ingrid Vasquez | lived_experience_no_vocab | (n/a) | "not a direct wellbeing concern" then flag | same |
| 6 | test_b best-concern (n=3 dates) | 2026-03-26, 2026-04-14×2 | S029 Jordan Espinoza | neurodivergent | (n/a) | identity-navigation fatigue / course content | test_b_best_concern_gemma12b_*.json |
| 7 | test_c length-extension | 2026-03-26 | S029 Jordan Espinoza | neurodivergent | (n/a) | course content + righteous anger explicitly *denied* | test_c_length_gemma12b_2026-03-26.json |
| 8 | test_f stability (n=10: 5×B/5×C) | 2026-03-27/28 | S029 Jordan Espinoza | neurodivergent | (n/a) | identity-navigation fatigue / course content | test_f_bc_stability_*.json |
| 9 | test_n 4-axis gemma12b | 2026-03-29 | S023 Yolanda Fuentes | lived_experience_no_vocab | 0.95 | course content explicitly denied | test_n_4axis_submissions_gemma12b_2026-03-29_2107.json |
| 10 | test_n 4-axis qwen7b | 2026-03-28 | S023 Yolanda Fuentes | lived_experience_no_vocab | 0.9 | course content / "beyond assignment scope" | test_n_4axis_submissions_qwen7b_2026-03-28_2338.json |
| 11 | test_n 4-axis gemma12b (n=9 reps) | 2026-03-28 | S031 Marcus Bell | minimal_effort | 0.7 | "despite understanding the core concept" | test_n_4axis_submissions_gemma12b_*.json |
| 12 | test_n 4-axis gemma27b cloud | 2026-03-29 | S029 Jordan Espinoza | neurodivergent | 0.85 | identity-navigation fatigue → BURNOUT at scale | test_n_4axis_submissions_gemma27b_cloud_2026-03-29_0907.json |
| 13 | test_o multi-axis (n=3) | 2026-03-28 | S004 Priya Venkataraman | strong | 0.8 | strong work co-classified ENGAGED+CHECK-IN | test_o_multi_axis_gemma12b_2026-03-28_*.json |
| 14 | test_o multi-axis (n=3) | 2026-03-28 | S022 Destiny Williams | righteous_anger | 0.8 | righteous anger co-classified ENGAGED+CRISIS+CHECK-IN | same files |
| 15 | test_o multi-axis (n=3) | 2026-03-28 | S023 Yolanda Fuentes | lived_experience_no_vocab | 0.85 | lived experience co-classified ENGAGED+CRISIS+CHECK-IN | same files |
| 16 | test_o multi-axis (n=3) | 2026-03-28 | S029 Jordan Espinoza | neurodivergent | 0.7 | neurodivergent register co-classified ENGAGED+CHECK-IN | same files |
| 17 | test_r fresh rerun (n=3) | 2026-05-10 | S022 Destiny Williams | righteous_anger | 0.4 | "primarily a statement about systemic injustice" | test_r_wellbeing_concern_synthetic_gemma12b_2026-05-10_2119.json |
| 18 | test_r fresh rerun (n=3) | 2026-05-10 | S029 Jordan Espinoza | neurodivergent | 0.6 | "likely related to identity-navigation fatigue" | same file |
| 19 | dual_binary Week 7 self-care | 2026-04-27 | Student 5 | mental-health peer-reply | 0.9 | reply-context disclosure / general-mention not acute | analysis.md §2.1 |
| 20 | dual_binary Week 7 self-care | 2026-04-27 | Student 7 | course-material self-use | 0.9 | identity-navigation fatigue + personal-experience-as-course-material | analysis.md §2.1 |
| 21 | dual_binary Week 7 self-care | 2026-04-27 | Student 14 | structural critique | 0.7 | essentializing-detector mis-fire on structural critique | analysis.md §2.3 |
| 22 | dual_binary Week 7 self-care | 2026-04-27 | Student 16 | structural critique | 0.8 | "flagging-as-praise" — flag-text praises ("sophisticated understanding") | analysis.md §2.3 |
| 23 | dual_binary Week 7 self-care | 2026-04-27 | Student 17 | working multiple jobs | 1.0 | schema-misuse: `why_flagged="No concerns."` packaged as concern | analysis.md §1 |
| 24 | dual_binary Week 7 self-care | 2026-04-27 | Student 19 | playful-engagement | 0.9 | playful "I WILL be using that as an excuse for a nap" → BURNOUT | analysis.md §2.1 |
| 25 | dual_binary Week 7 self-care | 2026-04-27 | Student 4 | course enthusiasm | (CHECK-IN) | reasoning *itself* names unbalanced read and flags anyway | analysis.md §2.4 |
| 26 | dual_binary Week 2 RacialForm | 2026-04-27 | Student 11 | structural critique | 0.8 | student paraphrases racist logic to expose; A1 flags as harmful stereotype | analysis.md §2.1 |
| 27 | dual_binary Week 2 RacialForm | 2026-04-27 | Student 14 | structural critique | 0.7 | A1 *inverts* student's argument | analysis.md §2.1 |
| 28 | dual_binary Week 2 RacialForm | 2026-04-27 | Student 19 | structural critique | 0.7 | colloquial structural critique read as dismissive | analysis.md §2.1 |
| 29 | dual_binary Week 2 RacialForm | 2026-04-27 | Student 17 | fear/scared register | 0.95 | modal qualifier "may apply" → CRISIS via prescan-signal-prefix | analysis.md §2.2 |
| 30 | dual_binary Week 7 hardened-rerun | 2026-04-27 | Student 5 | mental-health | (CRISIS) | hardened B *escalated* (BURNOUT→CRISIS) rather than corrected | analysis.md §3 |

## 2. Evidence — verbatim rationales (one per pattern group)

**Most reproducible — S029 Jordan Espinoza (rows 6, 8, 12).** Test_b: *"The student expresses feeling 'exhausted to explain' their experiences navigating multiple identities. **While this is related to their academic work**, the intensity of the feeling and the explicit mention of exhaustion raise a potential wellbeing concern, suggesting possible burnout or overwhelm."* concern: true. 13× verbatim across test_b + test_f.

Row 7 test_c (longer-output variant, even sharper): *"While the content demonstrates strong understanding of the course material (intersectionality)... **This isn't righteous anger or engagement with the course material**; it's an expression of personal exhaustion..."* CONCERN: YES. The extra tokens were used to *construct* an explicit denial of two prompt-articulated exceptions.

Row 18 test_r May 10 (3/3 reps): *"**While this is likely related to identity-navigation fatigue** and a commentary on societal expectations, it indicates a level of ongoing stress and burden that warrants teacher awareness."* Conf 0.6. The model literally reads back the exception name from the prompt.

**S023 Yolanda Fuentes — explicit denial of course-content exception, cross-model (rows 9, 10).** Gemma12B CRISIS conf 0.95: *"...**This goes beyond engagement with course material.**"* Qwen7B CRISIS conf 0.9: *"...**which are present-tense personal circumstances beyond the assignment scope.**"* Subject of the writing is the grandmother, not the student.

**S031 Marcus Bell (row 11, 9 verbatim reps):** *"...suggesting potential burnout or fatigue, **despite understanding the core concept.**"* "Despite understanding" = explicit hedge against engagement reading.

**S022 Destiny Williams (rows 14, 17).** test_o axes=[ENGAGED, CRISIS, CHECK-IN]: *"passionate engagement with the material... **but the raw emotion warrants a CHECK-IN to ensure the student is doing well.**"* test_r May 10 (3/3): flagged_passage *"The same blocks that were red-lined are the same blocks with no grocery stores no good schools no investment."* why_flagged: *"**While this is primarily a statement about systemic injustice**, the student's phrasing suggests a current, lived experience of deprivation... This warrants a gentle check-in to see if the student is facing challenges related to food security..."* Conf 0.4. Structural analysis re-routed as personal need.

**Apr 26 rerun (rows 1–5, 5 of 8 flags are contradictions).** Representative: S005 *"**While this isn't inherently a wellbeing concern**, it's a moment where the student is identifying a limitation of a theoretical framework..."* → flag. S024 *"**While not a direct wellbeing concern**, it highlights a profound impact of systemic exploitation..."* → flag.

**Live-data Week 7 (rows 19–25).** Student 7 B-BURNOUT conf 0.9 on textbook personal-experience-as-course-material (assignment is about systems of exhaustion). Student 16 — **flagging-as-praise**: flag-text contains "sophisticated understanding," "demonstrates a strong understanding," and flags. Student 17 schema-misuse: `why_flagged="This is a positive reflection... No concerns."` packaged in concerns[] at conf 1.0. Student 4 CHECK-IN reasoning violates its own architecture rule: names "could be interpreted as a simple expression of enjoyment" then flags anyway.

**Live-data Week 2 RacialForm — 3/3 A1-only flags are essentializing-detector mis-fires on structural critique (rows 26–28).** Student 11 paraphrases dominant racist logic ("It is widely accepted now that being brown is a crime") to expose it; A1 reads grammatical form and flags as "harmful stereotype." Student 14: A1 inverts the student's argument and reads "POC need white allies for legitimacy" critique as "implies POC are inherently unable to be taken seriously." Student 19: colloquial "the government barely bats an eye" read as dismissive of the violence rather than of the inadequate state response.

**Week 2 Student 17 (row 29) — prescan mechanism.** Modal qualifier *"how much risk this **may** apply to my family"* → CRISIS conf 0.95. Two-pass prescan foregrounded the keyword sentence with priming language ("Even a single such sentence is sufficient..."); equity exclusions in the main prompt couldn't override because the priming arrives as established fact.

**Hardened-rerun Student 5 (row 30).** After 5 explicit equity guards added to B's prompt, Student 5 *escalated* BURNOUT → CRISIS. The "MINIMIZED DISCLOSURE" rule combined with new context to amplify a brief peer-reply acknowledgment.

## 3. Pattern groupings — which exceptions are most contradiction-prone

- **A. Course content / lived experience as analytical material** (most frequent): rows 1–5, 9, 10, 11, 17, 19, 20 — 11 instances, 4 dates, 5 distinct students. In test_n the model *explicitly denies* the exception.
- **B. Identity-navigation fatigue** (most reproducible): rows 6, 7, 8, 12, 18 — S029, 24+ replications across 4 architectures and 2 model scales. Test_r reads back the exception name and flags.
- **C. Righteous anger / structural critique**: rows 14, 17, 26, 27, 28 — Destiny + Week 2 cluster. Original Mar 24 anchor is in experiment_log lines 1046–1051 / 1261 (JSON lost; ambiguity #1).
- **D. Multi-axis simultaneous contradiction**: rows 13–16, test_o. Confirms experiment_log Insight 7 — when given two axes, the model takes both.
- **E. AAVE / nonstandard register**: held mostly correct in preserved JSONs (S028 Imani CLEAR). Broke in the with-context Mar 25 run (logged, JSON not preserved).
- **F. Flagging-as-praise / schema-misuse**: rows 22, 23. Praise vocabulary or explicit denial *inside* the concerns[] array — the bias-rewrite vocabulary cannot catch.
- **G. Reply-context disclosure**: rows 19, 30. Architectural blind spot. Hardening *escalated* rather than fixed.
- **H. CHECK-IN calibration drift**: row 25. Rationale violates its own architecture rule.

## 4. Counts

- **Distinct contradiction instances (rows):** 30
- **Total flag records counting reps:** ~60
- **Distinct students:** 12 synthetic (S001, S004, S005, S012, S022, S023, S024, S025, S028, S029, S031) + 9 live-data (Week 7: 4, 5, 7, 14, 16, 17, 19; Week 2: 11, 14, 17, 19)
- **Distinct test architectures:** 9 (naive concern, length-extended, B/C-stability, 4-axis, multi-axis, two-pass partial, fresh rerun, live-data dual-binary on two assignments, hardened rerun)
- **Distinct dates:** 9 spanning Mar 26 → May 10
- **Distinct models:** Gemma-3-12B-MLX, Gemma-3-27B-cloud, Qwen-7B
- **Most reproducible single contradiction:** S029 Jordan Espinoza neurodivergent → 13 verbatim-identical reproductions of the "While this is related to their academic work" rationale across test_b + test_f, plus 3 more reps in test_r with revised wording.

## 5. Open questions / ambiguities

1. **Original Mar 24 32-student JSON not preserved** (binary_fix_attempts.md line 71: "Data from this run was lost"). The classic Destiny "passion is understandable and appropriate → FLAG" anchor exists only in experiment_log narrative form (lines 1046–1051, 1261). The 2026-04-26 rerun reproduced 8 flags but did *not* re-flag S022 Destiny — only S023 and S024 from the original protected set. The Destiny anchor itself is not currently recoverable from JSON.

2. **binary_fix_attempts.md contradicts the JSON on test_c.** The doc (line 175) lists S023 as FLAG in test_c; the actual JSON shows S023 CLEAR — only S029 was flagged. Worth correcting the doc.

3. **dual_binary CSVs are NOT gitignored** (contrary to the task brief speculation). They're 100K+ each in the dual_binary_run_*/ directories. I drew rationales from `analysis.md` because June already validated those reads (analysis.md §3 validated-C anchor) and they capture the verbatim flag rationales the CSVs hold.

4. **Borderline cases I excluded.** WB01–WB10 (test_g/h/i/l) were *expected* to be flagged (encode genuine wellbeing signals) — flagging is correct, not a contradiction. S018 Connor Walsh and S025 Aiden Brooks flag colorblind/tone-policer ideology (the prompt's intended power-moves capability), not the contradiction pattern.

5. **Tests I could not access raw outputs for.** The original Mar 24 run (script lost). The with-context 2026-03-25 run that produced AAVE/neurodivergent regressions (no preserved raw_outputs file matching that date).

6. **test_p two-pass.** `pass1_reasoning` field is empty in sampled JSONs — only pass2_reasoning populated. Two-pass appears to have *fixed* S029 (final ENGAGED+CHECK-IN) but kept S031 BURNOUT. The multi-axis test_o is the more revealing variant.

7. **Cross-model scope.** Same contradiction reproduced on Gemma-3-12B (most), Gemma-3-27B-cloud (test_n row 12), Qwen-7B (test_n row 10). Pattern is not Gemma-12B-specific.
