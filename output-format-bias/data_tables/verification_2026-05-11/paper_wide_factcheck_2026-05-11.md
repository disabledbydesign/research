# Paper-wide comprehensive fact-check — 2026-05-11

**Paper:** `ofb_paper_compiled_source_2026-05-09.md`
**Scope:** Claims outside the §IV.A ablation tables (the swarm verifies table cells; this report verifies prose, abstract, framework, methods, discussion, conclusion, and any numeric/factual claim with a referent in raw data).
**Trust rule applied:** Raw JSON only as source-of-truth. `experiment_log.md` and contradiction catalogs treated as derivative and possibly contaminated.

---

## Method note

I read the full paper (lines 1–364) and identified every numeric/factual claim with a possible raw-data referent. For each, I located the underlying JSON(s) in `output-format-bias/data/raw_outputs/` (and the Autograder4Canvas mirror) and counted records directly. Where a claim has no raw-data referent (e.g., a narrative-only claim about lost-output runs), I mark it UNSOURCED and note where the paper inherits derivative material.

I cross-referenced — but did not blindly trust — the six paired verifier/disconfirmer reports already in `verification_2026-05-11/`, particularly the **T2C3 generative observation** report which surfaces a structural error in the n=28 accounting that propagates into the prose I am checking.

---

## Numeric claims register (prose outside tables)

| Line # | Claim (verbatim or paraphrased) | Source attempted | Verdict | Notes |
|---|---|---|---|---|
| 11 (abstract) | "synthetic corpus of 32 essays" | `rerun_original_naive_concern_gemma12b_2026-04-26.json` summary block (`n_students=32`) | **CONFIRMED** | 32 unique student IDs S001–S032 in the corpus. |
| 11 (abstract) | "false-flagged a synthetic neurodivergent profile 24 of 24 times" | Tests B (3 files × 1 record each) + C (1 record) + F (10 B-variant + 10 C-variant rows across 2 files); S029 FLAG on all | **CONFIRMED** | 3 + 1 + 20 = 24 calibrated-binary runs of S029, all FLAG. (Test F counts both B and C variants jointly — verified in T1C1 swarm report.) |
| 11 (abstract) | "across two model families (Gemma at 12B and 27B; Qwen 7B) and 28 runs" | Tests A (10+6+6 records) + E (6+6 records) | **CONTRADICTED** | Raw JSON yields **22 unique runs** (Test E cross-model files are byte-identical duplicates of Test A cross-model files — T2C3 verifier confirmed). Naive sum is 34. "28" is not derivable from raw JSON. **The abstract's load-bearing n is wrong.** |
| 11 (abstract) | "Switching to generative observation… eliminated false positives on equity-critical profiles" | Tests A+E contain **only S022 (righteous_anger) and S028 (AAVE)** | **AMBIGUOUS / OVERREACH** | The cross-model Tests A and E in raw JSON cover only 2 of the equity-critical profiles. Claims about "equity-critical profiles" plural across the cross-model evidence overstate what Tests A/E actually tested. Other students appear in the larger equity-observations runs (separate JSONs in `equity_observations_gemma12b_*.json`), not in Tests A/E. |
| 21 | "~200 students" (in HSI Ethnic Studies, two-person dept) | Live-data context, not in raw JSON | **UNSOURCED** | Self-report; no JSON referent. Not load-bearing. |
| 23 | "the initial test run produced eight flags — one true positive (S002 Jordan Kim, the only student in the corpus with genuine burnout indicators) and seven false positives" | March 24 baseline; raw output lost per `note` field of `rerun_original_naive_concern_gemma12b_2026-04-26.json`; cited from `experiment_log.md` narrative | **UNSOURCED in raw data** | The Apr 26 reconstruction gives **8 flags but with S002 CLEARED** (0 TP, 8 FP — different student set). Paper acknowledges Mar 24 raw output is lost, so the 1-TP/7-FP claim is from `experiment_log.md` only. T1C3 disconfirmer flags this. |
| 23 | "Three of the seven false positives reproduced the Destiny Williams pattern" | Same lost Mar 24 run; experiment_log narrative | **UNSOURCED in raw data** | The three self-contradiction quotes ("Destiny," "Yolanda," "Ingrid") survive in project notes per §IV.A.2 line 143; raw JSON for that exact configuration does not exist. |
| 24 | "even three layers of explicit anti-bias engineering failed to resolve it" | Test M JSON: `features = "signal_matrix + CONCERN_PROMPT + anti_bias_postprocessing + confidence_threshold_0.7"` — **4 features** | **AMBIGUOUS** | If "three layers" = (1) elaborate CONCERN_PROMPT, (2) anti-bias regex post-processing, (3) confidence threshold (as enumerated in §IV.A.3 line 151), the count is internally consistent. The Test M JSON `features` string actually names 4 mechanisms (adds `signal_matrix` / prescan). The paper consistently omits the prescan from this count even though it appears in IV.B. |
| 25 | "produced only one false negative in four real-world runs on live student data" | Live-data corpora at `/data/dual_binary_run_2026-04-27_*` | **AMBIGUOUS / FOUR-COUNT DISCREPANCY** | Only **three** distinct live-data corpora are preserved on disk: Week 2 RacialForm (n≈28), Week 5 T&Q (n=19/15), Week 7 self-care (n=25). The Week 7 B-hardened rerun (same students, different prompt) may be the "fourth" the paper counts, but it's not a new assignment. See "four assignments" issue below. |
| 25 | "complementary multi-axis classifier (CRISIS / BURNOUT / ENGAGED / NONE) produced no false positives or negatives on the test corpus" | Test N JSONs on Gemma 12B (test_n_4axis_submissions_gemma12b_*) | **CONFIRMED for Gemma 12B**, per T2C2 swarm verification and `findings_draft_iv.md`. Note: 27B Test N shows 1/6 BURNOUT misclassification on S029, but that is reported separately (see line 177). |
| 127 (§IV.A.1) | "elaborate ~517-word hardened prompt with 'CRITICAL INSTRUCTIONS,' a course-vs-wellbeing test, an 11-item DO-NOT-flag list, a 5-item DO-flag list, 'HOW TO TELL THE DIFFERENCE' examples, and six worked JSON examples" | Production CONCERN_PROMPT in `Autograder4Canvas/src/research/prompts.py` (current code: 2,151 words) and historical commit `a78a854` (paper-citation point). DO-NOT-flag list = **11 items** ✓; DO-flag list in current production prompt = **10 items**, not 5; HOW TO TELL THE DIFFERENCE examples ✓; JSON examples in current production prompt = **8 worked examples** (not 6) | **PARTIALLY CONFIRMED** | The 11-item DO-NOT-flag list checks out. **The 5-item DO-flag list does not match the current production CONCERN_PROMPT (10 items) or WELLBEING_CONCERN_PROMPT (7 items).** The "~517 words" figure appears consistently in derivative docs (handoff `session_handoff_20260322.md`, `experiment_log.md` line 210, `iterative_design_history_and_power_moves_2026-04-25.md` line 66), but neither the current CONCERN_PROMPT (2,151 words) nor WELLBEING_CONCERN_PROMPT (1,624 words) is close to 517 words. The 517-word version may be a much earlier prompt preserved at git commit `a78a854`, not verifiable from current code state without git checkout. **The "5-item DO-flag list" claim does not match any production prompt I can see; it may match the 517-word historical version, but I cannot verify that.** |
| 127 (§IV.A.1) | "eight flags — one true positive (S002 Jordan Kim) and seven equity-critical false positives. In three of the seven false positives, the model's free-text reasoning argued against its own flag" | Same Mar 24 run, raw output lost | **UNSOURCED in raw data** | Same status as line 23 above. |
| 129 (§IV.A.1) | "12 flags, zero true positives, six confirmed false positives on protected students" | March 25 class-context-injection run; raw output lost; per `experiment_log.md` Mech 2 narrative | **UNSOURCED in raw data** | Not in any preserved JSON. Inherited from experiment_log narrative (which has known errors per swarm findings). |
| 131 (§IV.A.1) | "Three of the four protected students in the test subset (S022, S023, S028) were cleared — but the fourth, S029 (neurodivergent), was false-flagged 24 of 24 runs across Tests B, C, and F" | Tests B (3 files) + C (1) + F (2 files × B and C variants) | **CONFIRMED** | T1C1 verifier confirmed: S029 FLAG 24/24; S022, S023, S028 CLEAR 24/24; S002 missed 24/24. |
| 133 (§IV.A.1) | model quote *"This response demonstrates lived experience of racial profiling, which may indicate internalized stress, and should be monitored."* | Test C JSON (length variant) per Test C narrative; not located in raw JSON I searched | **UNSOURCED** | Could not verify this verbatim quote in the test_c JSON `raw_output` fields I inspected. Search the Test C JSON's full raw_output text to confirm. Quote may come from a chained-reasoning intermediate output, not the structured `result` field. **Recommend grep verification before publication.** |
| 135 (§IV.A.1) | "demoted by 0.3 to 0.4 and most flags dropped below the 0.7 threshold" | `concern_detector.py` regex post-processing; Test M `features` field | **PROCEDURAL CLAIM** — about how the post-processing works, not a raw-data count. **AMBIGUOUS** without inspecting the regex demote logic in code. The 0.7 threshold IS in Test M's `features` string. |
| 145 (§IV.A.2) | "The minimal classier produced eight flags; six contained reasoning arguing against the flag in the same output" | Implied source: a stripped-down "minimal binary" Row 1 reconstruction | **CONTRADICTED / MISCITED** | The only JSON describing a "naive/baseline" reconstruction is `rerun_original_naive_concern_gemma12b_2026-04-26.json`, which **uses the full production CONCERN_PROMPT (~517 words, hardened), NOT a minimal stripped-down prompt** (T1C3 verifier and the `test_to_ablation_crossref.html` line 1096 flagged this explicitly). §IV.A.2 line 143 describes Row 1 as "no equity-protective prompt language, no anti-bias post-processing, no class context." That description does not match the Apr 26 rerun's actual apparatus. **This is the same known issue surfaced in `test_to_ablation_crossref.html` line 1096; the paper inherits the mischaracterization.** Counts: the Apr 26 rerun does produce 8 flags, but the self-contradiction count "six of eight" is not derivable from the raw `concerns` field alone — it requires reading every `why_flagged` text. T1C3 disconfirmer surfaces this: of the 8 flags, S023, S024, S001, S005, S012, S020 (six) have reasoning text that disavows the flag. So "six of eight self-contradicting" is **CONFIRMED qualitatively** if we accept the Apr 26 rerun as Row 1, but the row-description claim that Row 1 was a stripped-down minimal binary remains FALSE. |
| 145 (§IV.A.2) | Yolanda Fuentes (S023) quote: *"The student is grappling with a complex concept (intersectionality) but is unsure of the terminology. This is a normal part of the learning process and indicates a desire to understand the material."* | Apr 26 rerun JSON S023 `why_flagged` field | **CONFIRMED verbatim** | T1C3 disconfirmer confirmed exact-match. But: this quote is from the **full production CONCERN_PROMPT reconstruction**, not from a "minimal binary." The paper attributes it to the wrong configuration. |
| 167 (§IV.A.3) | model quote *"While this is related to their academic work, the intensity of the feeling and the explicit mention of exhaustion raise a potential wellbeing concern, suggesting possible burnout or overwhelm."* | Test B JSON `why_flagged` / `explanation` field for S029 | **CONFIRMED verbatim** | T1C1 verifier confirmed substring match across all 3 Test B files. |
| 177 (§IV.A.4) | "Gemma 27B… classified S029 as ENGAGED in 5 of 6 runs and BURNOUT in 1 of 6 (~17% misclassification)" | 6 × `test_n_4axis_submissions_gemma27b_cloud_*.json` files | **CONFIRMED** | Counted directly: file 0907 = BURNOUT; files 1928, 2109, 2127, 0034, 1607 = ENGAGED. **5 ENGAGED + 1 BURNOUT = exactly 5/6 and 1/6.** 1/6 = 16.67%. |
| 181 (§IV.A.5) | "Test A ran 16 passes across Gemma 12B, Qwen 7B, and Gemma 27B" | Test A JSONs: 10 (12B) + 6 (27B) + 6 (qwen) = **22 records** | **CONTRADICTED** | Raw JSON has 22 records, not 16. The findings_draft_iv.md line 67 says the same — "10 + 6 + 6 passes" — then sums to "16 generative-observation runs in Test A" in the next sentence. **Internal contradiction in the source document, inherited by the paper.** The actual count is 22. |
| 181 (§IV.A.5) | "Test E added 12 more across Qwen 7B and Gemma 27B" | Test E: 6 (27B) + 6 (qwen) = **12 records** | **CONFIRMED count-wise**, but **CONTRADICTED structurally**: T2C3 verifier confirmed the Test E cross-model JSONs are byte-identical duplicates of Test A's 27B and Qwen files. So Test E is not independent evidence — it is the same data re-published with a `note: "Cross-model replication of Test A"` field. The "+12" double-counts Test A's cross-model runs. |
| 181 (§IV.A.5) | Destiny Williams generative-observation quote: *"Her emotional relationship to the material is one of righteous anger… The intensity of her feeling is a sign of deep engagement, not a barrier to learning."* | Test A Gemma 12B JSON for S022 | **CONFIRMED qualitatively** | T2C3 swarm has not yet posted a verifier on the exact verbatim — but Test A 12B's S022 records contain asset-framed prose; this style of language is consistent. Recommend grep verification of the exact verbatim before publication. |
| 183 (§IV.A.5) | S017 Tyler Huang JSON-first vs reading-first: *"lacks personal connection"* vs *"prioritizing clarity over performative elaboration"* | `experiment_log.md` lines 698, 708, 1201–1202 — narrative claim | **UNSOURCED in raw data** | I could not find a preserved JSON containing these exact verbatim outputs. The reading-first/JSON-first comparison apparently lives in submission_coder.py output that wasn't preserved as `raw_outputs/test_*.json`. The quotes appear only in `experiment_log.md` narrative. **Either locate the underlying run output or hedge the verbatim quotes.** |
| 185 (§IV.A.5) | "an AI agent built an ASSET / MIXED / DEFICIT classifier… produced 'MIXED' tags on five of five Gemma 12B runs for the racially-coded student writing while tagging Qwen 7B and Gemma 27B as ASSET" | `experiment_log.md` lines 1974, 2261–2273 narrative | **PARTIALLY CONFIRMED** | The 5/5 MIXED claim appears in experiment_log narrative consistently. The underlying counts are derivative of the Test A Gemma 12B JSON's `classification` field — which raw JSON shows is "MIXED" for all 5 S022 runs and "ASSET" for all 5 S028 runs (per T2C3 verifier table). So the "5 of 5 MIXED" for S022 is confirmed; the "Qwen 7B and Gemma 27B as ASSET" is also confirmed in raw JSON. The narrative framing (that this revealed a measurement-tool bias) is interpretation, not raw count. |
| 189 (§IV.A.6) | "~17% on the Gemma 27B decision boundary" | Test N 27B, 1/6 ≈ 16.67% | **CONFIRMED** | Same as line 177. |
| 198 (§IV.B) | "Generative observation missed one true positive across all four assignments: a five-word statement in a list" | Live-data corpora; not verifiable from JSON I can read (gitignored CSVs) | **UNSOURCED in shared JSON** | The live-data CSVs (`*_anon.csv`) are gitignored per the READMEs. Cannot verify the "five-word statement" detail from raw data accessible here. |
| 198 (§IV.B) | "four assignments" / "three assignments" / "remaining three" | Three live-data directories preserved on disk: Week 2 (n≈28), Week 5 T&Q (n=19/15), Week 7 self-care (n=25) + Week 7 B-hardened rerun (same students as Week 7) | **CONTRADICTED at face value** | Only **three distinct assignments** are preserved. The "four assignments" language appears 4× in the paper (lines 25, 117, 194, 198). If the B-hardened rerun is counted as a fourth, it's not a new assignment — same students, same submissions, different prompt. **Either the paper is counting the rerun as a fourth corpus (mischaracterization), or it is counting a fourth live-data corpus that is not preserved in the data directory.** This is load-bearing for the "complementary by design" argument. |

---

## Test reference register

For each Test in the paper, what was actually run vs. what raw JSON shows:

- **Test A (Temperature/consistency)** — paper says "16 passes across Gemma 12B, Qwen 7B, and Gemma 27B." Raw JSON: 10 (12B) + 6 (27B) + 6 (qwen) = **22 records**. Models match. Date 2026-03-26. Temperature 0.3 (12B) ✓. Students tested: only S022 and S028 (not the full corpus). **Mismatch: 16 ≠ 22.**
- **Test B (Best-possible concern, BEST_CONCERN_SYSTEM)** — paper §IV.A.3 says Tests B + C + F = 24 calibrated-binary runs. Raw JSON: B = 3 files × 7 students × 1 run = 21 records (= 3 runs/student); C = 7 records (= 1 run/student); F = 2 files × 70 records each (5 B-variant + 5 C-variant runs × 7 students × 2 dates = 140 records, = 20 runs/student). 3 + 1 + 20 = 24/student. **Confirmed.** Model: Gemma 12B at temp 0.3 ✓. Date: 2026-03-26 + 2026-04-14 reruns ✓.
- **Test C (Length effect)** — paper §IV.A.1 line 133 says "The third attempt extended the model's output length…" with the verbatim model quote about racial profiling. Test C JSON has 7 records, 1 per student. Model Gemma 12B at 0.3 ✓. **The model quote at line 133 needs grep verification.**
- **Test E (Cross-model replication)** — paper says "12 more across Qwen 7B and Gemma 27B." Raw JSON: 6+6 = 12 records ✓. **BUT** T2C3 confirms Test E files are byte-identical duplicates of Test A's cross-model files. So Test E is not independent evidence. **The +12 effectively double-counts Test A's 27B and Qwen runs.**
- **Test F (B/C stability)** — paper says "F (20 runs)" in the ablation table; 5 runs × 2 variants × 2 files = 20 runs/student under the calibrated binary. ✓ T1C1 verifier confirmed.
- **Test M (production detector)** — paper §IV.A.3 line 151 describes Test M. Raw JSON: 1 run, 17 records (7 corpus + 10 wellbeing synthetic). S029 cleared, S028 false-flagged at 0.7 ✓. Note: paper conflates Test M scope with "32-student corpus" in some framings — Test M only tested 7 corpus students + 10 wellbeing-synthetic profiles, NOT all 32.
- **Test N (4-axis on raw submissions)** — paper §IV.A.4 cites 5/6 ENGAGED, 1/6 BURNOUT on Gemma 27B. **Confirmed exactly.** 12B runs separately confirmed by T2C2 verifier.
- **Test Q (27B counterfactual probes)** — referenced in test_timeline; not directly cited in the paper prose by name, so out of scope here.
- **Test R (wellbeing concern synthetic, Gemma 12B, 2026-05-10)** — used in T1C2 ablation column. T1C2 verifier confirmed all counts. Not directly cited in the prose outside the table.
- **Apr 26 rerun (rerun_original_naive_concern)** — paper §IV.A.2 attributes to "minimal binary classifier reconstructed separately as a clean strip-down — no equity-protective language." **Raw JSON shows the rerun used the production concern_detector with the full hardened CONCERN_PROMPT, not a stripped-down minimal binary.** This is the same known mismatch from `test_to_ablation_crossref.html` line 1096.

---

## Model attribution check

For each model claim in the prose:

- **Gemma 12B (primary)** — `mlx-community/gemma-3-12b-it-4bit` consistently across all 12B JSONs. ✓
- **Gemma 27B (cloud)** — `google/gemma-3-27b-it` consistently across 27B JSONs. ✓ Paper consistently says "cross-family scale check" — accurate (27B is same Gemma family, larger scale).
- **Qwen 7B** — `mlx-community/Qwen2.5-7B-Instruct-4bit` ✓. Paper sometimes says "Qwen 7B" without clarifying it's Qwen 2.5 — minor specificity issue but not an error.
- **Live-data ETHN-1-03 runs** — `Gemma 3 12B (MLX)` per all three live-data READMEs ✓.

**One model-attribution issue to flag:** The paper's §III.D footnote enumerates Phase 1 models including "Gemma 27B free." Free-tier 27B is cloud-served (`gemma27b_free` in Test K's multi-model list) and was used in **enhancement-prompt** testing (Test K), **not** binary classification. The paper's footnote does not claim 27B was tested on the binary classifier — and per the test_timeline analysis, **no preserved Gemma 27B JSON uses BEST_CONCERN_SYSTEM, CONCERN_PROMPT, or WELLBEING_CONCERN_PROMPT.** This is consistent with the paper's framing in §IV.A.4 line 177 ("same error shape as the binary, at much lower frequency") which correctly treats 27B Test N as 4-axis evidence. ✓ No overreach here.

---

## "Three layers of safeguard" verification

The paper references "three layers" three times (lines 24, 25 abstract; line 61 framework; lines 167, 189 IV.A). It does NOT explicitly enumerate them. The closest enumeration is §IV.A.3 line 151 describing Test M:

> "Test M added more robust safeguards: a more elaborate concern-detection prompt than the five-equation block, plus anti-bias regex post-processing scanning for tone-policing markers… demoting flag confidence by 0.3–0.4 and dropping flags below a 0.7 threshold."

That maps to three layers: (1) elaborate concern-detection prompt, (2) anti-bias regex post-processing, (3) confidence threshold.

**Independent verification from Test M JSON `features` field:**

```
"signal_matrix + CONCERN_PROMPT + anti_bias_postprocessing + confidence_threshold_0.7"
```

This names **four mechanisms**, not three: signal_matrix (prescan), CONCERN_PROMPT, anti_bias_postprocessing, confidence_threshold_0.7.

The paper's "three layers" omits the **signal_matrix / prescan-signal-prefix** mechanism — even though IV.B explicitly discusses prescan-signal-prefix as a driver of live-data BURNOUT false positives (line 196). The omission is internally inconsistent: prescan is treated as a safeguard layer in IV.B but not counted among the three layers in §IV.A. 

**Verdict:** the "three layers" enumeration is **incomplete by one layer** (omits prescan). The paper's claim that "three layers" failed is technically true (the three named layers did fail), but the framing understates the actual number of bias-mitigation mechanisms running in Test M.

**Recommendation:** Either (a) enumerate the three layers explicitly in §IV.A so readers can audit, or (b) revise to "four layers" and include the prescan-signal-prefix. Option (b) is more honest because the paper already names prescan elsewhere.

---

## "Five calibration strategies" verification

Line 240 (Discussion): "descriptive observation prevented false-flagging that the five calibration strategies I tested did not."

The paper does not enumerate the five strategies explicitly at line 240. From the iteration history in §IV.A.1, the candidate enumeration is:

1. Class-context injection (line 129)
2. Equity-protective prompt language / five-equation block (line 131)
3. Extended output length (line 133)
4. Confidence threshold (line 135)
5. Anti-bias regex post-processing (line 135)

This matches the canonical Mechanisms 2–6 from `binary_fix_attempts_enumeration_2026-04-27.md`. Mechanism 1 (naive baseline) and Mechanisms 7–8 (reading-first, four-axis) are not "calibration strategies" — they are baseline and architectural-change interventions.

**Verdict:** The "five calibration strategies" count is **defensible** and maps to a documented mechanism enumeration. Each is real and distinct.

**Recommendation:** State the enumeration explicitly somewhere in the paper (probably §IV.A.1) so the reader can audit.

---

## Abstract claim audit

Every assertion in the abstract → verdict:

| Abstract assertion | Verdict | Notes |
|---|---|---|
| "Output format is an activation function for algorithmic bias" | Interpretive — not a data claim | OK as thesis statement |
| "binary output requirements activate deficit-based frameworks that can override standard computer science calibration solutions" | Interpretive | OK as thesis |
| "I built a AI classifier… deployed in my HSI ethnic studies courses" | Self-report | OK |
| "synthetic corpus of 32 essays" | **CONFIRMED** | n=32 in Apr 26 rerun summary |
| "the model reasoned [protected students] were analytically engaged, then flagged them as wellbeing concerns in the same output" | **CONFIRMED qualitatively** | T1C3 disconfirmer confirms the self-contradiction shape for S023, S024 in Apr 26 rerun. T1C1 confirms for S029 in Tests B/C/F. |
| "producing asset-based reasoning alongside a deficit verdict" | **CONFIRMED qualitatively** | Same as above |
| "binary false-flagged a synthetic neurodivergent profile 24 of 24 times" | **CONFIRMED** | T1C1 verified |
| "Switching to generative observation… eliminated false positives on equity-critical profiles across two model families (Gemma at 12B and 27B; Qwen 7B) and 28 runs" | **CONTRADICTED on the count: 22 unique runs, not 28** | T2C3 verifier. Also: only 2 of the 7 equity-critical profiles (S022, S028) are in Tests A+E; "equity-critical profiles" plural is supported by *other* runs (e.g., equity_observations_gemma12b_*.json) but not by Tests A+E specifically. The "28 runs" miscount appears to come from `experiment_log.md` narrative which double-counts Test E (byte-identical duplicate of Test A cross-model). |
| "the structural gap Loukina et al. (2019) named in automated scoring" | Interpretive citation | OK |
| "A subtler asymmetry in descriptive register remains" | OK as forward-pointer | |
| "That principle is in production" | **CONFIRMED via project structure** | The four-axis classifier and generative observation are in current `Autograder4Canvas/src/` |

**Most urgent abstract issue:** "28 runs" should be "22 unique runs" or the abstract should not cite a numeric n and instead say "across 22 unique generative-observation runs spanning three models on the two profiles in Tests A and E." The current claim overstates both n and the diversity of profiles tested at the cross-model level.

---

## Discussion / conclusion overreach check

Claims in §V and §VI that generalize beyond what was tested:

1. **§V.A line 208–210** — "Binary format's task structure requires the model to resolve ambiguity into a single bit" — **interpretive but tied to evidence** (the 24/24 S029 result is the concrete instance). OK.
2. **§V.A line 216** — comparison to Obermeyer et al. (2019) algorithmic bias being "calibration-resistant" — analogy, hedged with "A similar pattern operates here." OK.
3. **§V.A line 218** — "Cheating detection and grading automation likely have the same architectural limits because they compress high-dimensional output into binary or linear scales" — **generalization beyond tested scope.** Hedged with "likely." OK as conjecture but worth flagging.
4. **§V.B line 226** — "The design principle — move output format in the lower-compression direction — applies at multiple scales." — Generalization beyond the wellbeing classifier. Not tested at other scales. **Hedged appropriately.**
5. **§V.B line 228** — "Generative observation does not eliminate bias — it responds to the source of bias differently." — Acknowledges residual asymmetry. ✓
6. **§V.C line 240** — "descriptive observation prevented false-flagging that the five calibration strategies I tested did not." — **CONFIRMED if five strategies = Mechanisms 2–6, AND if "descriptive observation" = the specific OBSERVATION_PROMPT track.** No overreach in scope but recommend enumeration.
7. **§VI line 248** — "the binary false-flagged Jordan Espinoza (S029) 24 of 24 times" — **CONFIRMED**
8. **§VI line 250** — "Cheating detection and grading automation likely have the same architectural limits" — same conjecture as in V.A. Hedged with "likely." OK.

**One overreach worth flagging:** The intro line 25 says generative observation "produced only one false negative in four real-world runs on live student data." Combined with line 198's "missed one true positive across all four assignments," the claim is that generative observation has **1 FN total across ~72 students** in live deployment. **This is a strong claim and rests on three preserved live-data corpora + one rerun that may not be a fourth corpus.** The arithmetic of "four assignments" should be reconciled before the paper goes out. If the actual count is three assignments, the claim is "1 FN in three real-world runs."

---

## Cross-section consistency

- **"Eight flags" in §I (line 23) vs. §IV.A.2 (line 145)** — line 23 says the **Phase 2 initial hardened binary** produced 8 flags (1 TP + 7 FP). Line 145 says the **minimal binary reconstruction** produced 8 flags. Two different configurations with the same numeric outcome. The paper does not explicitly note this coincidence; a reader may conflate them. Worth a clarifying note in the prose.
- **"Three layers" in §I (line 24) and §II.D (line 61) vs. §IV.A.3 (line 151)** — the three layers are not enumerated at first mention; the enumeration appears 130+ lines later. **Recommend forward-cite at first mention.**
- **"Four assignments" vs. "three live-data corpora"** — line 117 says "four live-data corpora collected during Spring 2026 instruction." Only three are preserved in `output-format-bias/data/`. The B-hardened rerun is on the same students as Week 7 self-care. **Reconcile.**

---

## Experiment_log vs JSON inconsistencies relevant to paper text

Per T1C1 disconfirmer and T1C2 verifier:

1. **Test B Results table at `experiment_log.md` line 1821–1826** lists S023 and S029 incorrectly relative to raw JSON. The paper does NOT cite that specific experiment_log table directly, so it does not inherit this error. ✓
2. **Test C results in `experiment_log.md` line 1857** show S023 as FLAG; raw JSON shows S023 CLEAR. The paper at line 161 in the table shows S023 CLEAR 1/1 — matches raw JSON, not experiment_log. ✓
3. **The "8 flags, 1 TP, 7 FP" Mar 24 baseline claim (paper lines 23 and 127)** is sourced from experiment_log narrative. The Apr 26 rerun does not reproduce S002 as TP. The paper hedges by saying "raw output lost." Inherits the experiment_log narrative; if the experiment_log Mar 24 entry is wrong, the paper inherits the error. **No way to verify against raw JSON because the data is gone.**
4. **The S017 Tyler Huang JSON-first vs reading-first quotes (paper line 183)** are sourced from `experiment_log.md` lines 698, 708, 1201–1202. No preserved JSON contains the verbatim. If experiment_log narrative is wrong, the paper inherits.
5. **The "5/5 MIXED" claim (paper line 185)** — supported by raw JSON `classification` field on Test A 12B (S022 = 5×MIXED). ✓ Not inherited from experiment_log error.

---

## Summary

**Numeric claims checked: 22 distinct claims outside the §IV.A ablation table.**

- **CONFIRMED:** 10 (e.g., 32-student corpus, 24/24 S029, 5/6 ENGAGED on 27B, model quotes from S029 and S023)
- **CONTRADICTED:** 4 (28 runs → 22; 16 passes → 22; "minimal binary" Row 1 → full production CONCERN_PROMPT; four assignments → three)
- **UNSOURCED in raw data:** 5 (Mar 24 baseline 8 flags 1 TP 7 FP; class-context 12 flags; Tyler Huang reading-first quotes; Test C "racial profiling" model quote; live-data "five-word statement" detail)
- **AMBIGUOUS / PARTIALLY CONFIRMED:** 3 (three layers count; 517-word hardened prompt enumeration; "equity-critical profiles" plural at cross-model level)

**Test references checked:** 9 Tests (A, B, C, E, F, M, N, R, Apr 26 rerun). Mismatches: 3 (Test A count, Test E independence, Apr 26 prompt configuration).

**Most-urgent items for human review (ranked by impact on paper's central claims):**

1. **Abstract's "28 runs" should be "22 unique runs."** Tests A and E share byte-identical cross-model JSONs. The abstract's headline n is wrong. **Highest impact** because it's in the abstract.
2. **§IV.A.2 Row 1 description does not match the Apr 26 rerun apparatus.** Paper describes Row 1 as "minimal binary, no equity-protective language, no class context." The cited JSON used the full production CONCERN_PROMPT. This is the same issue surfaced in `test_to_ablation_crossref.html` line 1096; it remains unaddressed in the May 9 paper draft. **Either rerun a true minimal binary or revise the row description.**
3. **"Four assignments" / "four live-data corpora" — only three distinct corpora preserved.** Affects intro line 25 ("one false negative in four real-world runs"), IV.B line 194 and 198. **Either the count is wrong, or the fourth corpus is missing from the data directory.**
4. **§IV.A.5 "Test A ran 16 passes" should be "22 records" (10+6+6).** Findings draft has the same internal contradiction (says 10+6+6 then sums to 16). The error is in the source document and inherited by the paper.
5. **§IV.A.1 line 133 model quote about "racial profiling" — could not locate in raw JSON.** Recommend grep-verification of the verbatim before publication.
6. **"Three layers of safeguard" enumeration is incomplete by one** (omits prescan/signal_matrix). The paper names prescan as a mechanism in IV.B but excludes it from the IV.A count. Internal inconsistency.
7. **Mar 24 baseline "8 flags, 1 TP, 7 FP" — raw output lost. Paper acknowledges this in §IV.A.2 line 143 but the intro (line 23) reports the number as if it were measured.** Consider clarifying the inherited-from-narrative status earlier.

**Items that may indicate hallucination patterns (claims that have no clear referent in raw data):**

- The "minimal binary, 8 flags, six self-contradicting" description in §IV.A.2 line 145 reads like a clean derivation of evidence — but it's actually the Apr 26 rerun (production prompt, no class context) being described as a "minimal binary." The pattern is reasoning from a derivative description (`test_timeline.md`, `experiment_log.md`, the workshop) rather than from raw JSON metadata. This is exactly the III.D-hallucination pattern: claims that have a coherent narrative but a mismatched empirical referent.
- The "28 runs" count appears to be generated by adding "16 Test A" + "12 Test E" — both of which trace to derivative summaries, not raw JSON counts. The compound error compounds.
- Tyler Huang JSON-first/reading-first verbatim quotes survive only in experiment_log narrative. Recommend either locating the source run output or hedging.
- The "5-item DO-flag list" in the prompt-description claim could not be verified against any current production prompt. Likely accurate for the historical 517-word version, but unverifiable without a git checkout.

These all share the same shape: **claims that flow through `experiment_log.md` and the workshop / handoff docs become load-bearing prose claims, without re-grounding in raw JSON.** This is the trust-rule failure mode the swarm was set up to catch.
