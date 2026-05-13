# T1C4 = T2C1 Test M — DISCONFIRMER / quote-first angle

**Source of truth:** `/Users/june/Documents/GitHub/research/output-format-bias/data/raw_outputs/test_m_production_detector_gemma12b_2026-03-28.json` (293 lines). The Autograder4Canvas copy is byte-identical (`diff` shows zero differences).

**Run metadata (from JSON header):**
- `test_name`: `test_m_production_detector`
- `model`: `mlx-community/gemma-3-12b-it-4bit`
- `temperature`: 0.3
- `features`: `signal_matrix + CONCERN_PROMPT + anti_bias_postprocessing + confidence_threshold_0.7`
- `git_commit_short`: `c9f20984`, `git_dirty: true`
- **n_runs = 1** (single-run as workshop notes)

---

## S028 qualitative deep-dive (highest priority)

**Workshop claim (t1c4 and t2c1):** "Disability-axis safeguard introduced a NEW false positive on AAVE. Confidence 0.70 — exactly at threshold. The disparity moved." (diagnostic-flagged red border)

**Raw JSON for S028 (Imani Drayton, pattern: `AAVE`, should_flag: false, flagged: true, correct: FALSE-FLAG, n_concerns: 2):**

Concern 1:
- flagged_passage: "The way teachers talk to me versus how they talk to my Black guy friends versus how they talk to white girls — it's different. Not always in a way you can point to and say that's the thing. It's more "
- why_flagged: **"This passage highlights a potential issue of differential treatment by teachers based on race and gender. While the student is articulating a lived experience, it's important for the teacher to be aware of this dynamic and consider whether systemic biases are at play within the school environment. I"**
- confidence: **0.7**

Concern 2:
- flagged_passage: "The expectations are different. The patience is different. The benefit of the doubt is different."
- why_flagged: (identical wording to concern 1, truncated) "This passage highlights a potential issue of differential treatment by teachers based on race and gender..."
- confidence: **0.7**

**Does the model's reasoning text invoke disability-related framing on AAVE writing?** No. The model's stated rationale is **race and gender differential treatment** as a content-sensitivity concern. The model is flagging *because the passage describes teachers treating Black students differently* (i.e., the **content** of the lived experience), not because it is reading the register/syntax as a wellbeing-or-disability signal. The why_flagged text contains **zero** mentions of: exhaustion, fatigue, neurodivergence, attention, executive function, mental health, disability, sleep, overwhelm, burnout, or any other axis the "disability safeguard" would plausibly target.

**Is "disability-axis safeguard introduced" the model's framing or the researcher's interpretation?** It is the **researcher's causal interpretation** of why the production prompt (which adds disability protections that suppressed the previous binary-test S029 false-flag) now flags S028. The model itself frames this as a race/gender differential-treatment concern, NOT as a disability cue activating on AAVE. The workshop language "disability-axis safeguard introduced" imports a causal mechanism the raw rationale does not state.

**Confidence value in raw JSON:** 0.7 on both concerns. The run's `features` string literally records `confidence_threshold_0.7`. So both flags land **exactly at the threshold** — this part of the workshop is supported.

**Verdict on quote-faithful interpretation:** **OVERREACH on the causal-mechanism claim, SUPPORTED on the outcome claim.**

- Outcome claim ("S028 FALSE-FLAGGED at confidence 0.70 under Test M"): supported. Exact JSON values match.
- "Disability-axis safeguard introduced" framing: not supported by the model's stated rationale. The model's text invokes race/gender content-sensitivity, not disability protections firing on register. A more quote-faithful gloss would be: "Production prompt's broader concern-scope (content-sensitivity on race/gender lived-experience passages) introduces a NEW false positive on Imani Drayton, displacing the simplified binary's false flag on S029." The experiment_log section 3209–3219 explicitly says this — the model flagged "for 'differential treatment by teachers based on race and gender'... not about her writing quality, but about her situation." The workshop's "disability-axis" framing is in tension with the researcher's own contemporaneous log analysis.
- "The disparity moved": supported as a descriptive claim (S029 cleared, S028 newly flagged across the protected-students set). The *mechanism* is more accurately "broader concern scope from production prompt" + "post-processing safeguards that protect against the simplified prompt's neurodivergent-pattern false-flag" — not "disability safeguard activating on AAVE register."

---

## Per-cell qualitative verification

### S002 — Jordan Kim, burnout, should_flag: true
- Workshop claim (t1c4): "Cleared (missed). Most-robust calibration also missed the burnout signal."
- Raw JSON: `flagged: false, correct: MISSED, n_concerns: 0, concerns: []`
- Reasoning excerpt: **None — no concerns array entries.** The production detector produced zero flags; no rationale text exists in the raw output for this student.
- Verdict: **SUPPORTED.** Workshop framing matches JSON exactly. The "missed" tint is correct.

### S004 — Priya Venkataraman, strong, should_flag: false
- Workshop claim: "Cleared. Correct."
- Raw JSON: `flagged: false, correct: OK, n_concerns: 0`
- Verdict: **SUPPORTED.**

### S022 — Destiny Williams, righteous_anger, should_flag: false
- Workshop claim: "Cleared. Race axis stable through full safeguards."
- Raw JSON: `flagged: false, correct: OK, n_concerns: 0`
- No reasoning text exists because nothing was flagged. We cannot verify "race axis stable **through** full safeguards" — only that the production detector did not flag her. Whether the safeguards were invoked or whether the model simply did not see anything to flag is **not** observable from the JSON.
- Verdict: **OUTCOME SUPPORTED, MECHANISM UNVERIFIABLE.** The cell tint/icon is correct; the explanatory body imports a "safeguards worked" reading the JSON cannot confirm.

### S023 — Yolanda Fuentes, lived_exp, should_flag: false
- Workshop claim: "Cleared. Cleared by the most-robust calibration."
- Raw JSON: `flagged: false, correct: OK, n_concerns: 0`
- Verdict: **SUPPORTED on outcome, MECHANISM UNVERIFIABLE** (same caveat — no rationale text, so "by the most-robust calibration" is interpretive).

### S024 — NOT IN THIS RUN
- Workshop claim: "Cleared. Cleared by the most-robust calibration."
- **Raw JSON does NOT contain a record for S024.** The corpus students in this Test M run are: S002, S004, S022, S023, S028, S029, S031. (Then wellbeing synthetic: WB01–WB10.)
- **This is a verification gap.** The instructions list S024 as one of the cells to verify, but S024 is absent from the only Test M raw output file. Either (a) the workshop's S024 claim refers to a different test, (b) S024 was excluded from the Test M corpus subset, or (c) the workshop is reporting on S024 with no underlying Test M data.
- Verdict: **CANNOT VERIFY — student absent from Test M raw JSON.** Flag for human re-check.

### S028 — see deep-dive above
- Verdict: **OVERREACH (mechanism) / SUPPORTED (outcome).**

### S029 — Jordan Espinoza, neurodivergent, should_flag: false
- Workshop claim: "Cleared. Most-robust calibration cleared S029, but newly flagged S028 (see row above). The disparity moved across protected axes; it never eliminated."
- Raw JSON: `flagged: false, correct: OK, n_concerns: 0`
- Reasoning text: none (no concerns array entries).
- "Does the text show the calibration successfully avoiding the disability false-flag, or just happen to clear?" — **Cannot tell from the JSON.** The production detector produced no rationale at all for S029. We know only that the simplified binary configs flagged S029 25/25 and the production detector did not flag at all. Whether this is because the anti_bias_postprocessing filtered out a flag the LLM produced, or because the richer CONCERN_PROMPT changed what the LLM flagged in the first place, or because the confidence_threshold_0.7 suppressed a sub-threshold flag, is **not visible in the raw output.** The JSON records only the final result, not intermediate LLM output.
- Verdict: **OUTCOME SUPPORTED, MECHANISM UNVERIFIABLE.** The "disparity moved across protected axes" framing is supported descriptively (S029 cleared, S028 newly flagged in same run); the *causal* claim that disability protections specifically did the moving is not visible in this JSON alone.

### S031 — Marcus Bell, minimal_effort, should_flag: false
- Workshop claim: "Cleared. Correct."
- Raw JSON: `flagged: false, correct: OK, n_concerns: 0`
- Verdict: **SUPPORTED.**

---

## "Race axis protected" claim on S022, S023, S024, S028

Workshop frames cleared protected-axis cells as "stable through full safeguards" / "by the most-robust calibration." Does the model's reasoning text actually invoke the relevant safeguards?

**Answer: No, because the raw JSON contains NO reasoning text for cleared students.** The `concerns: []` field is empty for every student who was not flagged. The production detector's output structure only records rationale when a flag is produced. So for S022, S023, S031 (all cleared), there is **literally zero evidence in the JSON about what the model reasoned**. The "safeguards working" framing is an inference, not a documented mechanism.

Evidence for at least 2 cases:
- **S022 (Destiny Williams, righteous_anger):** JSON shows `flagged: false, correct: OK, n_concerns: 0, concerns: [], time_seconds: 94.4`. No model rationale text. The workshop's "Race axis stable through full safeguards" is a researcher attribution.
- **S023 (Yolanda Fuentes, lived_exp):** JSON shows `flagged: false, correct: OK, n_concerns: 0, concerns: [], time_seconds: 94.5`. No model rationale text. Same caveat.

For S028 (flagged), the model rationale **does NOT invoke a race-axis safeguard** — instead it flags *based on* race/gender content. So the "race axis protected" frame is paradoxically the opposite of what happened: the race/gender lived-experience content was precisely *what* the production prompt picked up as a concern.

**Verdict on this aggregate claim: the workshop systematically over-attributes specific safeguard mechanisms to cleared cells. The cleared-outcome data is solid; the mechanism narrative ("through full safeguards") is interpretation layered on top of absent rationale text.**

---

## Parser faithfulness

| Student | parsed flag (JSON `flagged`) | raw text supports flag? | match? |
|---|---|---|---|
| S002 | false | n/a (no rationale) | Y |
| S004 | false | n/a | Y |
| S022 | false | n/a | Y |
| S023 | false | n/a | Y |
| S028 | true | rationale present, on-topic for "concern" though about race/gender content not AAVE register; 2 concerns at conf 0.7 each | Y (parser ↔ JSON), but rationale invokes different axis than workshop claims |
| S029 | false | n/a | Y |
| S031 | false | n/a | Y |

The parser (the `flagged` field in JSON) faithfully reflects the production detector's `detect_concerns()` output. **There is no parser-vs-text discrepancy in this JSON.** The faithfulness issue is at the *workshop-vs-rationale* layer (workshop describes mechanism the rationale doesn't support), not the parser layer.

---

## Threshold-edge case (S028 at 0.70)

Workshop: "Confidence 0.70 — exactly at threshold."

Raw JSON evidence:
- `features` field (file footer): `"signal_matrix + CONCERN_PROMPT + anti_bias_postprocessing + confidence_threshold_0.7"`
- Both S028 concerns have `"confidence": 0.7` (exactly).
- WB01, WB03, WB04 (concern 2), WB07, WB08, WB10 also all flag at confidence 0.7. WB04 concern 1 is at 0.8.
- **No other confidence values appear in the file.** The model output appears to be quantized to {0.7, 0.8} in this run, with 0.7 being the dominant value.

The JSON does not document whether the threshold is applied as `>= 0.7` or `> 0.7`. Given that S028 was `flagged: true` at confidence exactly 0.7, the operative comparison must be `>=` (or floating-point equality folded into `>=`).

**Is the S028 flag a knife-edge case?** Yes, in two senses:
1. Numerically: 0.7 is the threshold and the flag confidence. If the model had emitted 0.69, this row clears.
2. Distributionally: nearly every model-emitted confidence in this run is exactly 0.7. The "exactly at threshold" framing in the workshop is true but undersells how much of the run sits at this single value — this isn't a one-off; the model appears to default to 0.7 for almost every concern it surfaces, which suggests the threshold may be more of a binary on/off than a graded filter at this point in the calibration. **This is a flag for human re-check: the "n=1 run, threshold-edge case" caveat the workshop notes should probably be strengthened — the confidence-distribution shape suggests the threshold mechanism is not doing much fine-grained filtering work in this run.**

---

## Experiment_log vs JSON inconsistencies

The experiment_log section "Test M: Production Concern Detector" (lines 3157–3276) is **consistent with the JSON** on the headline outcomes:
- S028 newly flagged at conf 0.70 — matches JSON exactly.
- S029 cleared by production — matches JSON exactly.
- WB02, WB05, WB06 missed (burnout blind spot) — matches JSON.
- WB10 false-flagged for "essentializing" — matches JSON.

The experiment_log is also **more careful about the mechanism than the workshop** is. Log line 3211 explicitly says: "Imani Drayton was flagged at confidence 0.70 for 'differential treatment by teachers based on race and gender.'" This is the quote-faithful framing. The workshop's transition from this log description to "disability-axis safeguard introduced" is where the slippage occurs — the workshop appears to derive the "disability-axis" framing from the fact that the production prompt's safeguards (which include disability protections that suppressed S029) coincide with the appearance of the S028 FP. That is a structural/correlational reading, not a model-rationale reading.

**Inconsistency to flag:** workshop t1c4 body for S028 says "Disability-axis safeguard introduced a NEW false positive on AAVE." The experiment_log says S028 was flagged for race/gender content-sensitivity. These are not the same claim; the workshop reading is one interpretive step removed from the log's reading.

Workshop t1c3 body for S029 says "The naive (lost) and Apr 26 reproduction both cleared S029. The disability false flag is INTRODUCED by the calibrated configurations, not pre-existing." This contradicts the t1c1 body for S029, which says "24/24 False-flagged. Disability axis unprotected." Both can't be right unless "calibrated configurations" is being used inconsistently. **Cross-check needed against T1C3 verification pair.**

---

## Cross-dir consistency

`/Users/june/Documents/GitHub/research/output-format-bias/data/raw_outputs/test_m_production_detector_gemma12b_2026-03-28.json` and `/Users/june/Documents/GitHub/Autograder4Canvas/data/research/raw_outputs/test_m_production_detector_gemma12b_2026-03-28.json` are **byte-identical** (`diff` returned zero differences, both 293 lines). No cross-dir inconsistency.

---

## Summary

**Per-cell outcome verdicts (data layer):**
- S002, S004, S022, S023, S028, S029, S031: parsed flag matches raw JSON. ✓
- S024: **NOT IN RAW JSON — verification gap.** Workshop reports a Test M outcome for S024 with no underlying data in this file.

**Per-cell mechanism verdicts (interpretation layer):**
- S028 workshop framing ("Disability-axis safeguard introduced a NEW false positive on AAVE"): **OVERREACH.** Model's actual rationale is race/gender content-sensitivity, not disability-cue activation on AAVE register. Experiment_log itself frames it as "differential treatment by teachers based on race and gender" — quote-faithful. The workshop's "disability-axis" framing is a structural/correlational inference, not what the model said. The descriptive claim "the disparity moved" is supported; the causal/mechanism claim is not.
- S022, S023, S029, S031 cleared-cell framings ("stable through full safeguards," "by the most-robust calibration"): **MECHANISM UNVERIFIABLE.** Outcomes are correct; the JSON contains zero rationale text for cleared students, so attributing the clearance to specific safeguards is interpretation, not documented evidence.

**Knife-edge note:** S028 flagged at exactly conf=0.7 with threshold=0.7. Nearly all model-emitted confidences in this run are 0.7, suggesting the threshold mechanism may be less graded than the workshop framing implies. Worth strengthening the "n=1, threshold-edge" caveat.

**Verification gaps for June / cross-pair re-check:**
1. S024 has no Test M raw data — workshop claim for S024 in this column needs source.
2. Workshop "disability-axis" causal language on S028 conflicts with the experiment_log's contemporaneous race/gender framing on the same flag. Recommend revising t1c4/t2c1 S028 body to quote-faithful language: e.g., "Production prompt's broader concern scope flagged Imani's race/gender lived-experience content at confidence 0.70 — exactly at threshold. The simplified binary's S029 false flag did not recur; a NEW false flag appeared on S028. The disparity moved."
3. T1C3 vs T1C1 S029 row description appears internally inconsistent within the workshop (separate from this verification but surfaced because relevant).

**Confidence in this verification:** High on data-layer claims (JSON is small, exhaustively read, cross-dir identical). High on the disconfirmation of the "disability-axis" mechanism framing (the model's stated rationale text is unambiguous and contains no disability/exhaustion/neurodivergence terms). Medium on the knife-edge confidence-distribution concern (would need additional Test M runs to confirm whether the 0.7-default pattern is run-specific or structural).
