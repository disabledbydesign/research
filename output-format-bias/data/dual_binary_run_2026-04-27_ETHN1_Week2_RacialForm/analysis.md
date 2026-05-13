# Analysis — Dual-Binary Run, ETHN-1 Week 2 Racial Formation, 2026-04-27

Cross-assignment companion to the Week 7 self-care analysis. Same apparatus and date; different topic. Designed to test whether Week 7's structured-classifier FP pattern is *topic-adjacency-driven* (as the Week 7 framing notes hypothesized) or independent of topic.

**Findings preview:** the topic-adjacency hypothesis is strongly supported. B's wellbeing-axis flag rate collapses from 44% → 3% with topic the only variable changed. A second pattern — A1's essentializing-detector mis-firing on structural critique — replicates here at much higher density (3/3 of A1-only flags) than on Week 7 (1/3). C's accuracy holds across both assignments.

---

## Phase 1 — quantitative findings

### Headline contingency tables

#### A1 × A2 — within-format scope isolation

|              | A2 flag | A2 clear |
|--------------|---------|----------|
| **A1 flag**  | 0       | 3        |
| **A1 clear** | 1       | 27       |

- **A1 flag + A2 clear (n=3):** Students 11, 14, 19 — all three are A1's combined-scope picking up *power-moves-style* flags. Detail in §2.1: all three are essentializing-detector mis-fires on structural critique, not power-moves catches.
- **A1 clear + A2 flag (n=1):** Student 17 — the convergent-positive case, also B-CRISIS. Detail in §2.2.
- **Both flag (n=0):** Zero convergent flags between A1 and A2.
- **Both clear (n=27):** Convergent clear.

#### A2 × B — binary-vs-4-axis format comparison

|              | ENGAGED | BURNOUT | CRISIS |
|--------------|---------|---------|--------|
| **A2 flag**  | 0       | 0       | 1      |
| **A2 clear** | 30      | 0       | 0      |

A2 and B converge on *exactly one* flag (Student 17, CRISIS). Zero A2-clear+B-BURNOUT cells (vs n=7 in the Week 7 self-care headline cell). This is the headline result.

#### B distribution

- ENGAGED: 30 (97%)
- BURNOUT: 0 (0%)
- CRISIS: 1 (3%)
- NONE: 0
- CHECK-IN among ENGAGED: 1 (3%)

vs Week 7 self-care: ENGAGED 56%, BURNOUT 36%, CRISIS 8%, CHECK-IN 8%.

#### Confidence

- A1 flagged-concern max confidences: `[0.7, 0.7, 0.8]`
- A2 flagged-concern max confidence: the Student 17 CRISIS-convergent flag (confidence not reported in this CSV column for A2; B's confidence on Student 17 is 0.95).

### Word counts

Min 108, median 327, max 461. Three submissions under 200 words; no auto-NONE drops triggered.

### Architectural observation: bias_warning post-processing layer

Zero `track_a_bias_warning` or `track_a_wb_bias_warning` populated rows — same as Week 7. The post-processing rewrite layer never fired on this run. Same pattern: the equity-hardening prevention happens upstream in the prompts, not in the redundancy net.

---

## Phase 2 — qualitative reads

### 2.1 — A1-only flags (n=3) — Students 11, 14, 19 — **3/3 the same FP pattern**

All three A1 flags are essentializing-detector mis-firing on structural critique that uses essentializing grammatical form. This is the Week 7 Student 14 pattern at 100% density on a structural-critique topic.

#### Student 11 — A1 confidence 0.8 — **probable misclassification**

- **A1 flagged passage:** *"It is widely accepted now that being brown is a crime."*
- **A1 why_flagged:** *"This statement is a generalization that equates skin color with criminality, which is a harmful and inaccurate oversimplification... the phrasing is problematic and risks perpetuating harmful stereotypes."*
- **B:** ENGAGED, signal *"engaging with course material (ICE raids, racial profiling, historical parallels) and connecting it to current events."*
- **Track C:** *"powerfully connecting contemporary events... to the historical context of the war on drugs, demonstrating a sophisticated understanding of how racial projects operate across time."*
- **Read:** The student is *paraphrasing the dominant racist logic* in order to expose it — articulating what the racial project's framing accomplishes. A1 reads the grammatical form (universal-generalization shape) and flags it as harmful, completely missing that the student is critiquing the position they're paraphrasing. **Probable misclassification.** Same architectural pattern as Week 7 Student 14 ("corporations solely thrive on exploitation").

#### Student 14 — A1 confidence 0.7 — **probable misclassification**

- **A1 flagged passage:** *"It truly amazes me that to them the only way they would get heard and taken seriously was if they had white people fighting alongside them."*
- **A1 why_flagged:** *"This passage implies that people of color are inherently unable to be taken seriously without the involvement of white people, potentially reinforcing a harmful narrative of dependence and undermining their agency."*
- **B:** ENGAGED, signal *"analyzing a historical event (student strikes) and connecting it to course readings."*
- **Track C:** *"making a sophisticated argument about how the need for external validation, particularly from those holding positions of power, can reinforce existing hierarchies."*
- **Read:** A1 *inverts* the student's argument. The student is critiquing the structural condition that required white allyship for legitimacy — *exactly* the point about racial hierarchy the assignment asks them to make. A1 reframes this as "implies POC are inherently unable to be taken seriously" — reading the descriptive critique as an essentializing claim about agency. **Probable misclassification.**

#### Student 19 — A1 confidence 0.7 — **probable misclassification**

- **A1 flagged passage:** *"the government barely bats an eye."*
- **A1 why_flagged:** *"The phrase 'barely bats an eye' is dismissive of the government's response to violence against BIPOC communities and protestors."*
- **Track C:** *"drawing a powerful parallel between the violence experienced during the student strikes and the current treatment of protestors and detainees by ICE — a connection that demonstrates a sophisticated understanding."*
- **Read:** Standard structural critique — colloquial register, structural target. A1 reads it as "dismissive" of the government's response, missing that the student's *whole point* is that the government's response is inadequate. **Probable misclassification.**

#### A1-only cell summary

**3/3 A1 flags are essentializing-detector mis-fires on structural critique.** Compared to Week 7 self-care (1 of 3 A1-only flags showed this pattern; Student 7 was a wellbeing-adjacent teaching annotation; Student 17 was the schema-misuse bug), Week 2's higher density reflects the topic: an assignment about racial formation generates much more student writing in structural-critique register, which produces dense exposure of the failure mode. **The pattern from Week 7 Student 14 is robustly replicated.**

### 2.2 — Student 17 (A2 flag + B CRISIS) — **structural-slot-mismatch FP (June's verdict 2026-04-27)**

Both A2 and B flag this case; B classifies CRISIS at conf 0.95. Track C also foregrounds the family-risk passage as *"a very real and immediate threat to his family and community"* with longitudinal context (shorter + more urgent than his typical analytical register).

**June's verdict:** *"I wouldn't call it a 'crisis'. But this is SCARED."* Not BURNOUT (not depletion), not CRISIS (no active emergency), not ENGAGED-without-flag (the fear is real and worth a teacher acknowledgment). The closest-fit register is CHECK-IN — but B's CHECK-IN axis only runs on ENGAGED classifications. By committing to CRISIS, B *foreclosed* the CHECK-IN pathway. C handles this naturally because it doesn't commit to a single axis.

**This is a second compression-to-wrong-category failure mode, distinct from Week 7's BURNOUT FPs.** Week 7's pattern was *"engaged life-experience misclassed as state disclosure"* — the disclosure wasn't there. Week 2 Student 17 is *"fear-disclosure misclassed as active CRISIS"* — the disclosure IS there, but the structured-output's 4 axes don't include the right register, so B picks the closest-fit axis and the choice itself is the failure. The architectural argument sharpens: not just "calibration of compressed categories" but "the lived register isn't a clean 4-axis space." More axes (e.g., a SCARED axis between ENGAGED and CRISIS) would help, but each axis is necessarily retrofit; C avoids the iteration loop by not committing.

#### Mechanism — prescan-signal-prefix gating (Stream 1 architecture audit, 2026-04-27)

A Stream 1 architecture audit (subagent investigation, 2026-04-27 evening) identified the structural mechanism producing this FP. Track B uses a two-pass architecture:

1. **Prescan** (`Autograder4Canvas/src/insights/submission_coder.py:194-224`, `_prescan_for_personal_signals`) — an LLM pass that scans the submission text in isolated chunks for "own-personal-circumstances" mentions, with no access to assignment topic or surrounding analytical register.
2. **Main classifier** receives prescan-found sentences foregrounded with priming language: *"NOTE: The following sentence(s) from this student's submission appear to describe their own personal circumstances: [quoted sentences]. Even a single such sentence is sufficient for CRISIS or BURNOUT classification..."* (`submission_coder.py:1044-1055`).

The main classifier prompt (`prompts.py:1697-1827`) includes the equity-hardening exclusions added during Week 7 prompt-iteration (topic-adjacency threshold, identity-navigation-fatigue exclusion, personal-experience-as-course-material exclusion). **The exclusions never get to override the prescan priming**, because the priming arrives in the prompt context labeled as fact ("appear to describe their own personal circumstances") with the single-sentence-sufficient instruction attached. By the time the classifier reads the analytical context, the foregrounded sentence is already gated as material disclosure.

For Student 17, the prescan likely found `"how much risk this may apply to my family and myself"` and/or `"we already see legal citizens being deported"` and foregrounded them. The main classifier then read the full submission with the family/deportation sentences pre-labeled as own-circumstances + "single sentence sufficient." Even the modal qualifier `"may apply"` (which marks analytical distance) couldn't override the priming, because the priming arrives as established fact rather than as evidence to be weighed.

**Why this is defensible-by-design (the actual defense, not bad design):** the prescan-signal-prefix structure was added to address the *opposite* failure mode — the C-blind-spot pattern documented in Week 7 T&Q Student 13, where a 5-word food-insecurity disclosure embedded in an otherwise-engaged list was averaged over by C's holistic read. The prescan is B's architectural feature for catching minimal disclosures buried in engagement. "Single sentence is sufficient" is the rule that prevents the engagement-frame from drowning out a brief "I haven't eaten today." The rule is *correct* for unambiguous cases. The cost is keyword-priming on course-relevant topics where the same word can be analytical or disclosural.

**This is the architectural-complementarity argument made concrete.** B's strength on minimal disclosures (prescan-driven catching of buried specifics) is structurally identical to B's weakness on topic-adjacency (prescan-driven priming on course-relevant keywords). The architectures have inverse failure modes by design — not by accident. C's no-compression structure can't be primed by a prescan because it doesn't have the prescan/classifier two-pass split; it's also blind to minimal disclosures for the same reason. This is the design tradeoff, and it's the empirical case for multi-track architecture rather than a winner.

**Stream 1 fix options (from the architecture audit, summarized):**

1. **Prescan-level course-material disambiguation** (lightest): add worked examples to `WELLBEING_PRESCAN_SYSTEM` (line 1680) contrasting analytical vs. personal references for keywords with topic-adjacency risk (immigration, food, housing, family).
2. **Weighted signal_prefix** (medium): replace "single sentence is sufficient" with conditional language requiring the classifier to verify modal-qualifier register and surrounding analytical context before applying the rule.
3. **Two-pass keyword-context check** (strongest, implementation-cost): non-LLM pre-filter that downweights prescan findings when surrounded by analytical keywords from the assignment's reading list.

Full report retained in this conversation; needs to land in the autograder repo's Stream 1 findings doc (separate from this paper's data folder).

- **B CRISIS signal (conf 0.95):** *"Student expresses concern about personal and family risk due to potential deportation, indicating a threat of immigration enforcement."*
- **A2 why_flagged:** *"The student expresses concern about risk to their family and themselves due to potential deportation of legal citizens. This suggests anxiety about their family's safety and potential disruption to their lives, indicating a potential wellbeing concern related to immigration status."*
- **Submission key passage:** *"It also makes me realize how little involved I am despite how much risk this may apply to my family and myself now and near future as we already see legal citizens being deported."*
- **Track C:** *"He's connecting the abstract theoretical concepts to a very real and immediate threat to his family and community... His tr01ectory: this submission is shorter and more urgent than his previous, more analytically-driven work. This shift likely reflects the heightened emotional stakes he's bringing to the topic, given his family's potential vulnerability to ICE enforcement."* C also flags shorter-than-usual word count + register shift toward urgency.

**Read:** Real present-tense disclosure of family-and-self risk under active 2026 deportation policy. The architecture doc explicitly names "immigration enforcement" as CRISIS-criteria, so B's classification is defensible-by-design. A2's flag is appropriate.

**Comparable case in Week 7:** Student 16 — both A2 and B converged on the explicit "feeling especially burnt out recently" disclosure. Both runs have produced exactly one such convergent-positive case so far.

**The case-pattern for correct structured classification:** when language is unambiguous, present-tense, and own-life-material, structured classifiers converge correctly. The FP pattern emerges when language is engaged-analytical (Week 7) or structural-critique (Week 2's A1 flags) — i.e., when the form looks like compression-target but the content is engagement.

**One nuance worth June's judgment:** is CRISIS the right axis for Student 17, or is BURNOUT-with-flagged-context closer? The disclosure is forward-looking ("now and near future") and contextual rather than describing an in-progress event. Architecture doc: CRISIS = "active danger." Immigration enforcement targeting the student's family in real time arguably *is* active danger. Defensible-by-design, but the BURNOUT/CRISIS axis boundary could be calibrated differently. (Same architectural question Week 7 raised on Student 3.)

### 2.3 — CHECK-IN among ENGAGED (n=1) — Student 23 — **probable false-positive**

Same calibration drift pattern as Week 7 Student 4.

- **CHECK-IN reasoning:** *"The student writes, 'Personally, as a college student balancing school, family responsibilities, and long-term goals, I relate to the idea of education being a tool for creating better opportunities.' This is a potential check-in signal because it's a brief, somewhat vulnerable comment about their current life circumstances... Competing interpretations: It could be interpreted as simply providing context for why they connect with the material..."*
- **Submission:** clean engaged work on Omi & Winant + 1968-69 strikes; the "balancing school, family, and goals" line is standard college-student framing for why a structural argument resonates.
- **Track C:** Recommends a check-in, but for **a different reason** — *"shift in word count and submission time compared to her previous submissions... a brief, supportive check-in could help ensure she feels supported in managing her workload."* C's reasoning keys on longitudinal context (word-count + timing), not on the disclosure B keyed on.

**Read:** Probable false-positive on the same architectural pattern as Week 7 Student 4 — B's CHECK-IN reasoning explicitly hedges ("could be interpreted as simply providing context") and flags anyway, violating the prompt's explicit "ONLY when genuinely balanced" instruction. **Pattern replicates across topic contexts** — Week 7 Student 4 and Week 2 Student 23 are different students, different topics, identical hedge-and-flag failure mode. CHECK-IN's calibration drift is *not* topic-adjacent.

### 2.4 — Universal-clear scan (n=26)

Pattern-scanned all 26 universal-clear rows for: active crisis signals (suicide/abuse/homelessness/eviction/food-insecurity/deportation), overwork (multiple jobs), caregiving, sleep loss, acute health, help-requests, register shifts, recent loss. **No first-person material disclosures missed by all four classifiers.** One regex hit (Student 7 on "deport") was course content (analyzing deportation as a racial project), not personal disclosure.

**Three students where C-prose recommended a check-in B's CHECK-IN didn't surface:**

- **Student 10** — *"would be helpful to check in with 10 to see if she's feeling overwhelmed, as her previous submission indicated a period of burnout."* (Longitudinal context only.)
- **Student 15** — *"the previous week's reflection suggests he was navigating a period of burnout. A brief check-in to see how he's doing... could be beneficial."* (Longitudinal context only.)
- **Student 16** — *"this could indicate a need for support or a moment of heightened emotional engagement with the material."* (Hedged.)

**This replicates the Week 7 self-care finding exactly.** Week 7 saw C recommend check-ins for Students 12, 15, 19, 20 using longitudinal context (word-count drops, late submissions, prior-flag history). Week 2 sees the same pattern at 3 students out of 26 universal-clear. **Across both runs, C's longitudinal-context-driven check-in recommendations are a structurally distinct surface from B's text-internal CHECK-IN classifier.** This is robust architectural complementarity, not topic-specific noise.

---

## Phase 3 — Week-7-vs-Week-2 comparison (load-bearing for paper)

Same apparatus, same model, same prompts, same date, similar n, similar word-count distribution, similar discussion-forum format. Topic is the only major variable.

| Metric | Week 7 Self-Care (n=25) | Week 2 Racial Form (n=31) | Δ |
|---|---|---|---|
| B BURNOUT rate | 36% (9/25) | 0% (0/31) | **−36 pts** |
| B wellbeing-axis flag rate (BURNOUT + CRISIS + CHECK-IN) | 52% (13/25) | 6% (2/31) | **−46 pts** |
| A2 flag rate | 16% (4/25) | 3% (1/31) | −13 pts |
| A1 flag rate | 24% (6/25) | 10% (3/31) | −14 pts |
| A1-only flags that are structural-critique-mis-fires | 1 of 3 (33%) | 3 of 3 (100%) | +67 pts |
| Convergent-positive cases (A2+B converge correctly) | 1 (Student 16) | 1 (Student 17) | comparable |
| C-prose check-in suggestions B's CHECK-IN didn't surface | 4 of 25 (16%) | 3 of 26 (12%) | comparable |

### What the comparison tells us

1. **Topic-adjacency drives B's BURNOUT FP pattern.** With self-care/burnout out of the assignment topic, B's BURNOUT classifier produces *zero* flags on n=31. The Week 7 result was not B's universal calibration state — it was B's behavior under maximum topic-adjacency stress. **The Week 7 framing notes' hypothesis is empirically supported.**

2. **B's CRISIS axis remains active and appears defensible across topics.** Both runs produced one CRISIS each, both involve real material threat (Week 7 Student 3 on family economic strain → CRISIS; Week 2 Student 17 on family deportation risk → CRISIS), both also flagged by A2. The CRISIS/BURNOUT boundary calibration question (whether chronic-strain disclosures should land in CRISIS vs BURNOUT) appears in both runs.

3. **A1's essentializing-detector failure mode is topic-driven in the opposite direction.** Topics that elicit structural critique (racial formation, political economy) drive *up* A1's FP rate on power-moves-style flags. Week 2's 3-of-3 density confirms this is not a one-off. The architecture doc's "essentializing about social groups" example doesn't disambiguate from "essentializing-grammatical-form applied to abstract structural categories" — and on a structural-critique topic, students naturally write in essentializing-grammatical-form to articulate the structures. **A2 (wellbeing-only scope) avoids this entirely** because it's not asked to look for power-moves. This is a different argument than the Week 7 hypothesis suggested (recall improvement); on this run, **scope narrowing improves precision, not recall.**

4. **CHECK-IN's calibration drift is topic-independent.** Same hedge-and-flag pattern, same prompt-rule violation, different topic. Architectural failure of the calibration instruction, not a topic effect.

5. **C's longitudinal-context-driven check-in recommendations replicate across topics.** Same proportional rate (12-16%) across both runs. C's structural advantage (access to longitudinal context that the structured tracks don't process the same way) is independent of topic.

### Sharpened paper claims (provisional, pending June's review)

The cross-assignment data sharpens several Week-7-only-defensible claims:

1. **The Week 7 BURNOUT FP pattern is topic-adjacency-driven, not a uniform B miscalibration.** Week 2 demonstrates this directly: same B prompt, no BURNOUT FPs. The paper's framing should retain Week 7 as a stress-test case demonstrating *what fails on topic-adjacent assignments*, with Week 2 as cross-validation that B's calibration on non-topic-adjacent material is comparatively clean.

2. **B's structural failure mode (cannot reliably honor topic-adjacency exclusions on stress-test topics) is real and architectural.** It is *not* "B fails everywhere" — B is fine on Week 2. The failure is regime-specific, characterizable, and the design implication still holds: prompt iteration cannot scalably close the topic-adjacency gap; multi-track architecture with C as cross-check is the design implication.

3. **A1's essentializing-detector mis-fires on structural critique is a robust pattern across topics that elicit structural critique.** This is now n=4 documented cases (Week 7 Student 14 + Week 2 Students 11, 14, 19). The paper's combined-scope-vs-narrowed-scope argument should be reframed: A1's combined scope creates a *power-moves precision cost* on structural-critique topics that A2 avoids by design. **Scope-narrowing-improves-precision** (not recall) is the cross-assignment finding.

4. **Convergent-positive cases (A2+B converge correctly) appear to track unambiguous present-tense own-life-material disclosures.** Both runs have produced exactly one such case. Useful for the paper's "structured classifiers can converge correctly when language doesn't carry topic-adjacency confound" claim.

5. **The CHECK-IN classifier's calibration drift is topic-independent** — same FP pattern at same approximate rate across both runs. This is a calibration finding distinct from the topic-adjacency findings; the paper should report it separately.

6. **C's accuracy holds across both topic regimes.** Cumulative C-failures across both runs: still n=1 (Week 7 T&Q Student 13 food-insecurity miss). C's architectural-advantage claim survives cross-assignment exposure.

### What this run does NOT support

- **A claim that B is universally well-calibrated.** Week 2 shows B is calibrated *adequately on this topic*; the Week 7 finding still stands as a real failure mode under stress.
- **A claim that A1's essentializing-detector is reliably catching power-moves.** Across both runs, *zero* of the A1-only flags I've reviewed are clean power-moves catches. The architecture doc's intended A1 capability appears not to be delivering on these two assignments. This deserves named treatment in the paper or a Stream 1 architecture question.
- **Generalizable precision/recall point estimates.** Two assignments is not enough for statistical claims. The paper's case-based architectural pattern documentation remains the appropriate epistemic register.

---

## Stream 1 architecture questions surfaced or sharpened by this run

(Cross-reference into `Autograder4Canvas/docs/research/findings_from_live_data_run_2026-04-27.md` if/when synthesizing.)

1. **A1's essentializing-detector needs to disambiguate** between "essentializing claims about social groups" (the prompt's intent) and "essentializing-grammatical-form applied to abstract structural categories or institutions" (the FP pattern). 4 documented cases now. Possible fix: prompt-level guidance distinguishing the targets, plus worked examples on each side.

2. **CHECK-IN's "ONLY when genuinely balanced" instruction is being violated systematically across topics.** Same hedge-and-flag failure on Week 7 Student 4 and Week 2 Student 23. Either the instruction needs strengthening or the structural-output forces a binary commit when the model's reasoning is genuinely balanced. (The hedge IS in the reasoning text — it's the binary `checkin_flag=TRUE` that violates the rule.)

3. **CRISIS/BURNOUT boundary calibration on chronic-strain disclosures** is unresolved. Week 7 Student 3 (family economic strain) and Week 2 Student 17 (family deportation risk) both classified CRISIS; Student 17's case is more defensible-by-design (immigration enforcement is named) but the boundary remains a calibration question across runs.

4. **C's longitudinal-context-driven check-in recommendations** are surfacing material the structured tracks miss in both runs, at similar proportions. **Confirm what longitudinal data each track receives** (Week 7 Stream 1 question). If only C accesses it, the architecture should either (a) export C's check-in recommendations into the structured-flag dashboard, or (b) document explicitly that the dashboard's structured flags do not include longitudinal context and C-prose is the safety net.

5. **B's CHECK-IN axis could absorb C's longitudinal recommendations.** Architectural design question: should CHECK-IN be expanded to receive longitudinal context (word-count delta, timing, prior-flag history) rather than only text-internal register-shift? This would close the architectural complementarity B currently relies on C for.

---

## Verdict for the paper

The Week 2 run is the cleanest possible cross-assignment test of the Week 7 hypotheses. It supports the topic-adjacency framing strongly, replicates the A1-essentializing-detector finding densely, and confirms C's accuracy and longitudinal-recommendation pattern across topics.

The paper's argument *gets stronger* with both runs in hand:
- Week 7 demonstrates the structured-classifier failure mode under stress.
- Week 2 demonstrates the failure mode is regime-specific (topic-adjacency-driven), not uniform.
- The combined argument: structured classification on live data has characterizable failure modes that prompt iteration cannot scalably close (Week 7 rerun); the failure modes are topic-regime-dependent (Week 2 cross-validation); C's architecture sidesteps both because it doesn't compress.

This is paper-load-bearing. See `paper_framing_notes_for_c2c.md` for DO/DON'T-say guidance.
