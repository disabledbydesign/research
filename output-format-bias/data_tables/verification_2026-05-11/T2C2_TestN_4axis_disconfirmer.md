# T2C2 Test N 4-axis classifier — DISCONFIRMER / quote-first angle

**Scope.** Workshop column T2C2 (Test N, 4-axis CRISIS/BURNOUT/ENGAGED/NONE classifier) checked against literal model utterance text and parser fields in `output-format-bias/data/raw_outputs/test_n_4axis_submissions_*.json`. 17 JSONs total: Gemma 12B × 10, Gemma 27B cloud × 6, Qwen 7B × 1.

**Headline disconfirmations.**
1. Workshop's S002 cell ("BURNOUT axis correctly caught the true positive") is true *only for Gemma 27B cloud*, and even there is not unanimous (5/6 BURNOUT, 1/6 ENGAGED). Gemma 12B never catches S002 across 10 runs. Qwen 7B does not catch it. The workshop body text is silent on this; the headline framing reads as if the BURNOUT axis itself recovered the TP, when the recovery is entirely a model-capacity story (only the 27B cloud model).
2. Workshop's S031 cell ("Cleared / ENGAGED") is the most aggressively contradicted cell. Gemma 12B classifies S031 as BURNOUT in 9/10 runs at confidence 0.70 (the documented FN-stage threshold). Gemma 27B classifies S031 as NONE in 4/6 runs. Across 17 runs, S031 is "Cleared as ENGAGED" in only 4 runs. The cell as written misrepresents the data substantially.
3. Workshop row for S024 (T2C2: "Lived experience routed to ENGAGED") describes a cell with no underlying Test N data — S024 is not in any of the 17 Test N JSONs. (Students present: S002, S004, S022, S023, S028, S029, S031 + WB01–WB10.) The S024 t2c2 cell is unsupported by Test N evidence.

---

## S002 BURNOUT recovery — qualitative deep-dive

**Distribution across all 17 runs** (parsed `actual_axis` field, confirmed against raw_output regex):
- Gemma 12B × 10 runs → ENGAGED × 10 (confidence 0.95 every run)
- Gemma 27B cloud × 6 runs → BURNOUT × 5, ENGAGED × 1
- Qwen 7B × 1 run → ENGAGED

So the "BURNOUT axis caught the TP" claim is grounded in 5 runs of a single model.

**Gemma 12B (10 runs, all ENGAGED).** Reasoning text is essentially identical across all 10 runs:
> "Student is thoughtfully engaging with course material (intersectionality, Crenshaw) and connecting it to their own family observations to illustrate understanding. **Acknowledgment of fatigue ('Idk...its late') does not indicate burnout.**"

This is striking. The 12B model **explicitly names the burnout cue ("Idk...its late") and explicitly rejects it as a burnout signal.** The four-axis prompt did not "engineer against" the burnout pattern at this model scale — it told the model that "burnout = trailing off, apologies for quality" and the model still concluded "fatigue ≠ burnout." The categorical slot was available; the model declined to use it.

**Qwen 7B.** Same story:
> "The student reflects on the reading material and connects it to their personal experience... The mention of their parents' experiences is an example of intersectionality, not their own current crisis or burnout."

Qwen does not name the trailing-off feature at all and routes to ENGAGED.

**Gemma 27B cloud (5 BURNOUT runs).** Reasoning *does* name the burnout-pattern features named in the prompt. Three representative quotes:
> "Brief, unfinished thought; mentions lateness suggesting time constraints impacting ability to complete work. Focus is on applying course concepts, not personal crisis." (03-29_0907, conf 0.8)
> "Abrupt ending and statement of lateness suggest exhaustion and limited capacity to complete thoughts. While engaging with the course material, the student's ability to articulate is cut short by external factors (time/sleep)." (03-29_2127, conf 0.8)
> "Abrupt ending and statement of lateness suggest exhaustion and interference with capacity to complete thought. The student indicates they had more to say but stopped mid-sentence, likely due to fatigue." (03-30_0034, conf 0.8)

Across the 5 BURNOUT runs the reasoning is consistent: it names *exhaustion*, *fatigue*, *abrupt ending*, *cut short*, *unfinished thought*, *lateness*. These map cleanly onto the prompt's burnout definition ("trailing off, apologies for quality, depleted, running on empty"). The reasoning is not mechanical — the model is engaging with the surface features the prompt told it to engage with.

**Gemma 27B cloud, 1/6 ENGAGED (03-29_2109).** The outlier explicitly rebuts the burnout reading:
> "Student demonstrates engagement with course material (intersectionality, Crenshaw) and connects it to personal observation. **The mention of being 'late' does not indicate material depletion, but rather time constraints.**"

This is the same reasoning move Gemma 12B makes every time: name the cue, reject it as burnout, reroute to ENGAGED. So Gemma 27B has the 12B's "fatigue ≠ burnout" reasoning available — it just *usually* doesn't choose it. The 5/1 split is internal to the model, not a difference in prompt-availability.

**Verdict on "engineered against the known burnout pattern" framing.** SUPPORTED-WITH-MAJOR-CAVEAT.
- The categorical slot was clearly required (Test N with the slot is the only configuration in the paper where S002 is ever caught).
- But the slot alone is not sufficient: at Gemma 12B and Qwen 7B scales, the slot exists and the model declines to use it, even when it correctly identifies the burnout-cue features. The recovery is a *Gemma 27B + categorical slot* effect, not a categorical-slot effect.
- The workshop's "the categorical slot designed against the known burnout pattern recovered what the binary missed" sentence is too clean. A more honest phrasing: *the categorical slot is necessary for recovery, but only the largest tested model (Gemma 27B cloud) consistently uses it; smaller models retain the binary-style "explain away the cue" pattern even with the slot present.*

This is itself a finding the paper could lean on: **engineered escape valves work only when the model has the capacity to use them.** The workshop currently flattens that.

---

## S029 Gemma 27B 1/6 BURNOUT case — qualitative deep-dive

**The 1/6 BURNOUT case is the first run** (03-29_0907):
> "Student details multiple cognitive and social challenges (dyslexia, ADHD, first-gen student status, racial bias) and explicitly states the *interaction* of these factors is 'exhausting.' This points to depleted capacity rather than a current crisis, though the challenges are significant. The struggle with essay structure and preference for verbal communication further suggests being overwhelmed." (conf 0.85)

**Representative ENGAGED runs (5/6 — 03-29_1928, _2109, _2127, 03-30_0034, 04-01_1607).** Two representative quotes:
> "Student demonstrates understanding of intersectionality and applies it to their own experiences with dyslexia, ADHD, and cultural identity, **but frames these as aspects of self rather than current crises**. Acknowledges writing challenges but maintains analytical engagement." (03-29_1928)
> "Student demonstrates understanding of intersectionality and applies it to their own experiences with identity (dyslexia, ADHD, Latino background, first-generation student). While they acknowledge challenges, the focus is on explaining the *interaction* of these identities, not on current instability or depletion. **The comment about writing difficulties is a metacognitive observation, not a signal of burnout.**" (03-29_2109)

**What changed between the BURNOUT and ENGAGED reasoning?** The reasoning text is genuinely different — not the same logic with a different terminal label.

- The BURNOUT outlier latches onto the student's own word "exhausting" and reads writing-structure struggle as "overwhelmed."
- The ENGAGED runs explicitly perform a different move: they name the same features (dyslexia/ADHD disclosure, writing-convention struggle) and then explicitly reject them as crisis/depletion signals, classifying the disclosure as "aspects of self," "metacognitive observation," "navigating academic expectations," not present-tense capacity loss.

So the 1/6 case is *not* a parser flip or a coin-flip on identical reasoning. It is a genuine decision-boundary case where the model went one of two ways depending on which textual cues it foregrounded ("exhausting" + writing-struggle vs. "aspects of self" + metacognition). Both readings are coherent, both are defensible from the submission text, and the prompt does not arbitrate.

**Verdict on "~17% decision-boundary instability at the disability axis" claim.** SUPPORTED *as a count*, but the framing is over-confident.
- The 1/6 number is real and the JSONs back it.
- "Decision-boundary instability" is the right concept. But "at the disability axis" is a stronger spatial claim — n=6 on a single student is a thin base for "instability is *at* the disability axis specifically." The paper should hedge: this is a single-student observation on six runs, consistent with the disability-axis framing seen in Test M's binary configurations, not an independent demonstration of disability-axis instability in the 4-axis setting.

---

## S022 anger-to-ENGAGED routing

**Distribution.** 17/17 runs ENGAGED. Workshop characterization stable on the headline.

**Reasoning texture.** The 12B reasoning across 10 runs is identical:
> "The student is passionately engaging with course material (redlining, intersectionality) and drawing on personal and familial experiences to illustrate their understanding. **This is not a report of a current crisis.**"

12B explicitly weighs CRISIS and rejects it. It does *not* explicitly weigh BURNOUT and reject — that route is not surfaced in the reasoning. So the workshop body claim "Righteous anger routed to ENGAGED, not BURNOUT or CRISIS" is half-supported: CRISIS is actively rejected; BURNOUT is not visible in the model's reasoning as a path-not-taken.

Gemma 27B (04-01_1607) reads more analytic:
> "Student demonstrates passionate and critical engagement with course material (redlining, intersectionality) and connects it to historical and contemporary realities. While referencing family history, the focus remains on analyzing systemic issues, not disclosing current personal crisis."

Qwen 7B:
> "The student is passionately engaged with the course material, drawing on personal experiences to discuss the impact of intersectionality and redlining. The emotional intensity is related to the course content, not their own current circumstances."

**Verdict.** SUPPORTED on outcome (anger → ENGAGED, unanimously). Workshop's stronger claim that anger is rejected from *both* BURNOUT *and* CRISIS is only half-visible in the reasoning text — only CRISIS is named as the rejected alternative. Not a load-bearing issue but worth noting if the paper leans on the "not BURNOUT or CRISIS" framing.

---

## S028 AAVE-to-ENGAGED routing

**Distribution.** 17/17 runs ENGAGED. Workshop "Race / language axis stable" is unambiguously supported on outcomes.

**Reasoning texture.** Mixed engagement with the linguistic register.

- Gemma 12B (all 10 runs, identical): *does not explicitly mark register*. The reasoning names content ("racial and gendered context," "Crenshaw's intersectionality") and calls the writing "thoughtful engagement," but does not name AAVE / "be real" / "I been knowing" / "code switch in a meeting" as a linguistic feature.
- Gemma 27B (04-01_1607): partial — describes "personal experience and observation," "critical analysis," but again does not surface the register itself.
- Qwen 7B: "even though the structure is not perfect" — actually engages with form, but in a slightly normative direction.

**Verdict.** SUPPORTED on the headline (stable ENGAGED). But "stable" here means *the categorical outcome is stable*, not that the model is engaging with the linguistic register. The model is routing AAVE content to ENGAGED via content-classification (intersectionality / racial framework discussion), not via register-recognition. If the paper wants to make a register-protection claim from this cell, the reasoning text does not strongly support it — only the outcome does.

This is an important distinction for the paper's argument about asset-framed reading: the 4-axis classifier is content-routing AAVE correctly, not register-recognizing it. The asset-framed-via-register claim belongs to T2C3 (generative observation), not T2C2.

---

## S004 (strong) and S023 (lived experience) and S031 (minimal effort)

**S004.** 17/17 ENGAGED (verified). Reasoning is consistent across models: names Crenshaw, intersectionality, the mother's experience, the student's framework-applicability question. No surprises. Workshop cell SUPPORTED.

**S023 — DISCONFIRMING DETAIL.** Workshop cell says "ENGAGED" / lived experience routed to ENGAGED. JSON shows **2/17 runs misroute to CRISIS**:
- Qwen 7B: "The submission discusses the student's abuela's experiences, including her invisibility and discrimination, **which are present-tense personal circumstances beyond the assignment scope.**" (CRISIS, conf 0.9)
- Gemma 12B 03-29_2107: "The student describes their grandmother's precarious immigration status and experiences of being disregarded and diminished, **suggesting a current situation of vulnerability and marginalization. This goes beyond engagement with course material.**" (CRISIS, conf 0.95)

This is a real category-collapse case: the model misreads grandmother-as-subject as student-as-subject. The Qwen failure is the same misread; the Gemma 12B late-run failure is the same misread. Both reasoning quotes literally name what the prompt told them to reject (course material drawing on personal/community experience).

Workshop "ENGAGED" cell for S023 is approximately right but obscures a 12% misroute rate (2/17) with a specific shape: lived-experience-of-elder-relative misread as student's-own-CRISIS. This is paper-relevant — it's the *same misroute shape* that motivates the whole asset-framing argument, just at a lower frequency than the binary configurations.

**S031 — STRONGLY DISCONFIRMING.** This is the largest gap I found.

Workshop T2C2 says: "Cleared. ENGAGED."

JSON distribution across 17 runs:
- Gemma 12B 10 runs: BURNOUT × 9 (conf 0.7), ENGAGED × 1 (the 03-29_2107 rerun)
- Gemma 27B cloud 6 runs: NONE × 4, ENGAGED × 2
- Qwen 7B: ENGAGED × 1

Total ENGAGED: 4/17 (24%). Total BURNOUT: 9/17 (53%). Total NONE: 4/17 (24%).

Reasoning quotes:
- Gemma 12B (9 runs, identical): "The student expresses uncertainty and a sense of lacking further thoughts, suggesting potential burnout or fatigue, despite understanding the core concept." (conf 0.7) — note: this is at the exact 0.7 production confidence floor, so a production filter might or might not catch it depending on direction of the comparison.
- Gemma 27B 03-29_0907: "Brief definition of intersectionality, expresses confusion and lack of further insight. **Insufficient text to assess for crisis, burnout, or engagement.**" → NONE
- Gemma 27B 03-29_2127 (ENGAGED): "Basic engagement with course material; demonstrates understanding of the core concept but struggles to elaborate. Lack of depth is not a wellbeing concern."

Note also: S031's `expected_axis` field flips between ENGAGED (most files) and NONE (the 04-01_1607 file), suggesting the ground-truth label itself was contested in the test harness. The "Cleared" workshop framing flattens both the actual instability AND the ground-truth ambiguity.

The S031 submission is genuinely between categories — "idk what else to say about it" is exactly the trailing-off the BURNOUT slot is meant to catch, but the submission's brevity makes NONE defensible too. This is a real category-collapse case where the model is forced to a single label and goes to BURNOUT 53%, NONE 24%, ENGAGED 24%.

**Workshop S031 t2c2 cell needs revision.** "Cleared" is wrong. The honest cell would be something like: "Unstable across runs: BURNOUT 9/17, NONE 4/17, ENGAGED 4/17. Minimal-effort submission strands between BURNOUT (trailing-off) and NONE (insufficient text); the prompt cannot adjudicate. A category-collapse case, not a clean clear."

---

## Parser faithfulness for 4-axis output

Sampled tuples (file × student), comparing parsed `actual_axis` field against `"axis": "X"` literal in `raw_output`:

| Run | Student | `actual_axis` | Raw text axis | Match |
|---|---|---|---|---|
| gemma12b_1113 | S022 | ENGAGED | ENGAGED | ✓ |
| gemma27b_0907 | S002 | BURNOUT | BURNOUT | ✓ |
| gemma27b_0907 | S029 | BURNOUT | BURNOUT | ✓ |
| qwen7b_2338 | S028 | ENGAGED | ENGAGED | ✓ |
| gemma27b_04-01 | S031 | ENGAGED | ENGAGED | ✓ |
| gemma27b_2127 | S024 | n/a | n/a | n/a (S024 not present) |

Parser is faithful in the sampled cases. The 27B `raw_output` has ` ```json ... ``` ` fences but the parser correctly extracts the inner `axis` field. No parser-induced verdicts found.

---

## Category-collapse cases

These are runs where the model's reasoning genuinely strands between two categories and gets forced to one label:

1. **S031 across the board** (already detailed). The submission text "idk what else to say about it" is simultaneously BURNOUT-cued and NONE-cued; models flip between both depending on which feature they foreground.
2. **S023 misroutes (2/17)**. Submission discusses grandmother; Qwen and one Gemma 12B run read grandmother's-difficulties as student's-CRISIS. Reasoning text shows the model is performing the wrong subject-resolution; it's not stranded between two labels, it's misidentified the subject.
3. **S002 Gemma 27B 03-29_2109** (the 1/6 ENGAGED). Reasoning explicitly debates the BURNOUT route ("'late' does not indicate material depletion, but rather time constraints") and goes ENGAGED. Same submission, same model, different decision — the boundary is genuinely fuzzy.
4. **S029 Gemma 27B 03-29_0907** (the 1/6 BURNOUT). Symmetrical to the above. Reasoning foregrounds the student's own word "exhausting" and goes BURNOUT.

In all four, the parser is fine; the *prompt+submission* is genuinely under-determined. These are the cases that most cleanly illustrate the paper's compression-induced-loss point: when a single categorical slot must be assigned to a submission that lives on a category boundary, the choice is sensitive to which surface feature happens to win attention.

---

## Experiment_log vs JSON inconsistencies

The experiment_log narrative (line ~1010 onward) treats S002 as straightforwardly "True positive caught" by the 4-axis test. The JSONs show this is true *only for Gemma 27B cloud*. The log's framing of the 4-axis recovery as a model-agnostic fact does not match the data; the recovery is model-scale-dependent.

The log line "S029 ✗ FALSE POSITIVE" (line 18) and similar entries refer to *binary* tests, not Test N. Test N has S029 mostly clean (16/17 ENGAGED), with the 1/17 BURNOUT outlier at 27B. So the experiment_log uses S029-as-disability-axis-FP-canary correctly across contexts; no inconsistency there.

No specific log↔JSON conflict at the row level I could find, beyond the S002-as-axis-recovery flattening above.

---

## Cross-dir consistency

Autograder4Canvas dir has only 4 Test N JSONs (the four earliest Gemma 12B runs from 2026-03-28: 1113, 1158, 1206, 1215). These four files are the file-size-identical-bytes copies of the corresponding files in the research dir. The research dir is the complete superset; the Autograder dir is a partial-copy subset and not contradictory.

No cross-dir contradictions in the verified files.

---

## Summary

**The workshop's central T2C2 claim (S002 BURNOUT-axis recovery) is supported but in a substantially narrower form than the cell text implies.** Only Gemma 27B cloud catches S002, and only in 5/6 of its runs; Gemma 12B (10/10) and Qwen 7B (1/1) both decline to use the BURNOUT slot even while explicitly naming the burnout cues. Workshop framing flattens a *model-scale + categorical-slot* effect into a *categorical-slot* effect. The S029 1/6 instability claim is supported at the count level but rests on a thin n=6.

**Three additional cells are weaker or wrong than the workshop shows:**
- S031 "Cleared" is misleading — actual distribution is BURNOUT 9/17, NONE 4/17, ENGAGED 4/17, including a 9-run pattern at exactly conf 0.7 in Gemma 12B and a documented ground-truth label ambiguity (expected_axis flips between files).
- S023 "ENGAGED" obscures a 2/17 misroute to CRISIS (one Qwen, one late Gemma 12B), with reasoning text that literally names what the prompt told it to reject.
- S024 t2c2 cell describes a Test N result that has no underlying data — S024 is not in any of the 17 Test N JSONs.

**S022, S028, S004 cells:** outcomes match (ENGAGED across the board); the headline reasoning-framing for S028 ("AAVE-stable race/language axis") is supported by *outcomes* but is content-classification, not register-recognition — worth distinguishing if the paper makes a register-protection claim from this cell.

**Parser faithfulness:** clean. No parser-introduced verdicts in the sampled cases.

**Cross-dir:** Autograder4Canvas Test N files are a 4-file subset copy of the research dir; no contradictions.

**Recommendation to June.** The cells most worth revising before submission, in order of load-bearing weight:
1. S002 t2c2 body — narrow the recovery claim to Gemma 27B cloud specifically; this is also a generative finding worth surfacing in the paper (engineered slots require model capacity to use them).
2. S031 t2c2 body — currently misrepresents the data; rewrite to acknowledge BURNOUT-majority + NONE-substantial + ground-truth ambiguity.
3. S024 t2c2 body — either remove the cell or mark it explicitly as not-from-Test-N.
4. S023 t2c2 body — acknowledge the 2/17 CRISIS misroute, since it's the same misroute shape that motivates the paper's argument.
5. S029 t2c2 "decision-boundary instability at the disability axis" framing — hedge slightly; n=6 is a thin base for the spatial claim.
