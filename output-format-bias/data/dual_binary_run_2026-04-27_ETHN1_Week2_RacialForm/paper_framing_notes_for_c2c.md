# Paper Framing Notes — for c2c Paper-Drafting Sessions (Week 2 Cross-Validation Run)

**Read this AFTER `paper_argument_rationale.md` (the complementary-by-design framing) and BEFORE `analysis.md`.** This document captures the precise framing for paper-drafting sessions handling Week 2 ETHN-1 Racial Formation data, including hedges and DO/DON'T-say guidance specific to this run's findings.

The Week 7 self-care framing notes (`../dual_binary_run_2026-04-27_ETHN1_self_care/paper_framing_notes_for_c2c.md`) cover the parent run; this document covers what the cross-validation Week 2 run adds, sharpens, or revises in the framing.

---

## Headline framing — what the Week 2 run adds

### What we have learned (as of 2026-04-27 evening)

1. **The Week 7 BURNOUT FP pattern is topic-adjacency-driven, not a uniform B miscalibration.** Week 2 racial formation discussion forum (n=31, same model, same prompts, same format, same date) produced **0 BURNOUT classifications**. Week 7 self-care produced 9. With topic the only major variable changed, B's wellbeing-axis flag rate dropped from 52% to 6%. The Week 7 framing-notes hypothesis is empirically confirmed.

2. **The architectural mechanism is identified.** The prescan-signal-prefix architecture (`Autograder4Canvas/src/insights/submission_coder.py:1044-1055`, `prompts.py:1671-1685`) primes the main classifier with foregrounded keyword-matched sentences before the topic-adjacency hardening guards can fire. This is the structural cause of both Week 7's BURNOUT FPs and Week 2's Student 17 CRISIS-not-fitting case. Same mechanism, two failure modes.

3. **A1's essentializing-detector mis-fires on structural critique replicate at higher density.** Week 2's three A1-only flags (Students 11, 14, 19) are **3 of 3** structural-critique mis-fires (Student 11: "being brown is a crime" is the student paraphrasing institutional racism's logic to expose it; Student 14: critique of white-allyship dynamics in 1968-69 strikes; Student 19: colloquial structural critique of state response). Week 7 had 1 such case (Student 14, "corporations solely thrive on exploitation"). Cross-assignment: n=4 documented. Robust pattern on topics that elicit structural critique.

4. **A new structural-slot-mismatch failure mode for B.** Student 17's "scared, not crisis" register (instructor verdict) doesn't fit any of B's four axes cleanly. B picks closest-fit (CRISIS) and forecloses the more appropriate CHECK-IN pathway (CHECK-IN only runs on ENGAGED classifications). Distinct from Week 7's BURNOUT FPs (where the disclosure wasn't there); here the disclosure IS there but the structured-output's axes don't include the right register.

5. **CHECK-IN calibration drift replicates across topics.** Week 7 Student 4 ("really enjoyed the topic and readings this week!") and Week 2 Student 23 ("balancing school, family responsibilities, and long-term goals") both produced hedge-laden CHECK-IN reasoning ("could be interpreted as simply...") that flagged anyway, violating the prompt's "ONLY when genuinely balanced" rule. Pattern is *not* topic-adjacent. Distinct architectural finding.

6. **C's longitudinal-context-driven check-in recommendations replicate across topics.** Week 2 universal-clear scan: 3 students (10, 15, 16) where C's prose recommended a check-in B's CHECK-IN didn't surface, all keyed on word-count drops or prior-burnout history. Same pattern at same approximate rate as Week 7 (4 students out of 25). Robust architectural complementarity, not topic-specific noise.

7. **C's accuracy holds across topic regimes.** Cumulative C-failures across both runs: still n=1 (Week 7 T&Q ETHN-1-02 Student 13's food-insecurity miss). C's architectural advantage claim survives cross-assignment exposure. ONE soft over-reading (Week 7 self-care Student 13 on temporal-distance) remains the only edge-case caveat.

### How to say it without overstating

- **DO say:** "Across the two assignments examined, B's BURNOUT classification rate ranged from 36% on a topic-adjacent assignment (Week 7 self-care, deliberately selected as architectural stress-test) to 0% on a non-topic-adjacent assignment (Week 2 racial formation discussion forum). The Week 7 hardening rerun found this rate insensitive to prompt-level guards; the architectural cause was identified via Stream 1 audit as the prescan-signal-prefix mechanism."
- **DO NOT say:** "B fails on topic-adjacent assignments" as a frequency claim. Say "B's failure mode is regime-specific to topic-adjacency, identifiable on the assignments examined as the deliberately-stress-test case (Week 7) and absent from the cross-validation case (Week 2)."
- **DO say:** "A1's essentializing-detector mis-fires on student writing that uses essentializing-grammatical-form to articulate structural-critique. Documented across both runs at n=4 of A1-only flags (3 of 3 in Week 2; 1 of 3 in Week 7)."
- **DO NOT say:** "A1's combined-scope is broken." A1 may catch legitimate power-moves on assignments that elicit different student writing patterns; we have not seen that on these two assignments because the topics tend toward structural-critique, not toward essentializing-about-social-groups.
- **DO say:** "Student 17's CRISIS classification is a structural-slot-mismatch case: the disclosure is real (the instructor and Track C both recognize fear of family vulnerability to active 2026 immigration enforcement), but the 4-axis structured output does not include a register fitting 'scared without active emergency.' B selects the closest-fit axis (CRISIS); the choice itself is the failure mode, distinct from Week 7's BURNOUT-where-no-disclosure-exists."
- **DO NOT say:** Student 17 is a "false positive" without qualification. The instructor's verdict was "scared, not crisis" — meaning the flag-direction was correct (something is going on), the axis was wrong, and the more appropriate handling (CHECK-IN as lighter-touch acknowledgment) was foreclosed by B's commit-to-axis architecture.

---

## On Student 17 (preserve verbatim for paper)

June's verdict (2026-04-27 evening, conversational):
> *"I wouldn't call it a 'crisis'. But this is SCARED."*

The student's passage:
> *"It also makes me realize how little involved I am despite how much risk this may apply to my family and myself now and near future as we already see legal citizens being deported."*

Track C's read:
> *"He's connecting the abstract theoretical concepts to a very real and immediate threat to his family and community... This submission is shorter and more urgent than his previous, more analytically-driven work. This shift likely reflects the heightened emotional stakes he's bringing to the topic, given his family's potential vulnerability to ICE enforcement."*

**Why this case is paper-load-bearing:** it documents the structural-slot-mismatch failure mode distinct from Week 7's BURNOUT FPs. The disclosure IS real and architecturally legible (B's prescan caught it via "family crisis" + "immigration enforcement" keywords; C caught it via register-shift recognition; A2 also flagged it). What fails is the axis-selection: B's four-axis output doesn't include "scared without active emergency," so B picks CRISIS, which forecloses the more appropriate CHECK-IN pathway. The paper should describe this as a documented case of structural-slot-mismatch — distinct from "false positive" framing — and use it to support the strand-3 reactive-axis-iteration argument in the rationale doc.

**Recommended paper-prose framing:**
> *"On the Week 2 cross-validation run, Track B's single CRISIS classification (Student 17) involved a student naming active immigration-enforcement risk to their family in the present-tense political context of Spring 2026. The student's instructor — also the researcher — read the case as the student expressing fear, not active crisis: a register that the architecture's four-axis output (CRISIS / BURNOUT / ENGAGED / NONE) does not include. The student-state most accurately characterized as 'scared without active emergency' would have been better-served by the targeted CHECK-IN pathway, which surfaces register-shifts as a lighter-touch acknowledgment than CRISIS classification — but B's CHECK-IN axis runs only on ENGAGED classifications, so by classifying CRISIS, B foreclosed the more appropriate handling. This case documents a second failure mode for compressed-classification architectures, distinct from the topic-adjacency mis-priming on Week 7: when the student's actual register falls between the structured-output's available axes, the classifier commits to the closest-fit axis and the choice itself is the failure."*

---

## On the prescan-signal-prefix mechanism (paper Methods or early Discussion)

The mechanism (full detail in `paper_argument_rationale.md` Strand 2 and in the Stream 1 doc):

1. Prescan LLM scans submission chunks for own-personal-circumstances keywords (food insecurity, family crisis, immigration enforcement threat, etc.) — no analytical context.
2. Found sentences foregrounded in main classifier prompt: *"NOTE: The following sentence(s) appear to describe their own personal circumstances: [quoted]. Even a single such sentence is sufficient for CRISIS or BURNOUT classification."*
3. Main classifier prompt's hardening guards (topic-adjacency threshold, identity-navigation-fatigue exclusion, personal-experience-as-course-material exclusion) live downstream of the priming. The priming arrives as established fact; the hardening can't override what's already labeled-as-disclosure.

**Paper-prose recommendation:** the Methods section should document the prescan-signal-prefix architecture as part of B's design, not as an incidental implementation detail. Explain the mechanism, then link to Strand 1 (inverse failure modes by design) and Strand 2 (the same mechanism produces both strength and weakness). Specifically:

- The mechanism that mis-primes on Week 7 self-care (causing BURNOUT FPs on engaged life-experience writing) and on Week 2 Student 17 (causing CRISIS-not-fitting on family-deportation-risk language) is the *same architectural feature* that catches Week 7 T&Q Student 13's 5-word food-insecurity disclosure C missed.
- Same mechanism, inverse failure modes. **This is the empirical case for multi-track architecture as design intent**, not as fallback after B fails.
- The prescan-signal-prefix is *defensible-by-design as a tradeoff*: prevent the engagement-frame from drowning out brief unambiguous disclosures (Strand 1's C-failure case). The cost is keyword-priming on course-relevant topics where the same word can be analytical or disclosural.

**DO NOT** describe the prescan-signal-prefix as bad design or as a bug. It is the architectural feature that does what it was designed to do; the cost is structural, not implementation-incidental.

---

## On the binary-vs-4-axis comparison confound — disclose, don't paper over

The original Week 7 headline framing ("the format change nearly tripled wellbeing-signal recall") is no longer defensible without qualification, because B's architecture bundles two changes vs A2:

- Format change: binary flag/clear → 4-axis CRISIS/BURNOUT/ENGAGED/NONE
- Architectural change: A2 is single-pass full-text classification; B is two-pass prescan + signal-prefix-primed main classifier

The recall increment cannot be cleanly isolated to format-effect. The paper should acknowledge this:

**Recommended Limitations or Methods caveat:**
> *"We compare A2 (binary wellbeing-only classifier) against B (4-axis classifier with two-pass prescan-signal-prefix architecture) as architectures-as-deployed in the production system. The comparison is not a clean binary-vs-4-axis format-effect comparison: B's two-pass architecture (prescan + signal-prefix-primed main classifier) is structurally distinct from A2's single-pass design, and the recall and precision differences between A2 and B reflect the bundled architectural change, not a controlled isolation of format-effect from architectural-effect. Practitioners deploying these classifiers face whole architectures, not isolated features; the architectures-as-deployed comparison is therefore the relevant one for the paper's practitioner-recruiting scope. A controlled binary-vs-4-axis comparison holding the prescan architecture constant is left to future work [pointer to Round 2 paper concept]."*

The topic-adjacency finding stands cleanly because it is a within-B comparison (Week 7 vs Week 2, same architecture, different topic). The prescan-confound does not undermine cross-assignment B variation.

---

## On the data integrity flag — duplicate IDs and gaps

The Week 2 CSV (`week2_racial_form_ethn1_anon.csv`) has 31 rows but ~28 unique student IDs. IDs 10 and 20 each appear twice with different submissions; IDs 24-27 are missing. Likely upstream anonymization artifact (display-name → number with collisions). The paper has three options:

1. Report n=31 with footnote explaining the data-integrity flag. Treats each row as a distinct submission (which it is).
2. Re-anonymize cleanly from source data and re-cite n=28 (or whatever the unique count is).
3. Treat as n=28 unique students with multiple submissions for two students; report both counts.

**Recommendation:** Option 1 (n=31 submissions with footnote). The case-based architectural-pattern documentation is robust to which n is reported; the topic-adjacency contrast holds at any reading. Don't add re-anonymization to the May 20 timeline.

---

## On the small-corpus case-based epistemic register

The empirical findings rest on case-based architectural-pattern documentation across two assignments (n=25 + n=31 = 56 submissions). The argument lands on case-based design tradeoffs, which do not require statistical confirmation; the *patterns* are the findings. Hedge accordingly:

- **DO:** describe findings as "across the assignments examined" / "documented cases" / "the n=4 cases of [pattern] across both runs"
- **DO NOT:** describe findings as precision/recall point estimates ("B's precision is 9-15%") without immediate qualification about sample size and selection
- **DO:** describe the Week 7 assignment selection as deliberate stress-test (per Week 7 framing notes); describe the Week 2 assignment selection as cross-validation of the topic-adjacency hypothesis
- **DO NOT:** describe either run as representative of typical teaching contexts

---

## What remains true regardless of additional data

- The architectural-complementarity argument (B and C have inverse-by-design failure modes; multi-track with cross-checking is the design implication) is qualitative and supported by case-based documentation.
- The prescan-signal-prefix mechanism finding is structural — independent of any data set, it is a property of the deployed architecture identifiable by reading the code.
- The Week 7 self-care assignment selection as stress-test is methodological choice that future data does not change.
- The Week 2 cross-validation finding (B's flag rate drops to 0% BURNOUT on a non-topic-adjacent assignment) is structural — the topic-adjacency hypothesis is confirmed within the architecture's own behavior.
- C's complementary failure mode (Week 7 T&Q Student 13) is a case-based finding, n=1 across both runs combined.
- The structural-slot-mismatch failure mode (Week 2 Student 17) is a case-based finding, n=1, distinct from the topic-adjacency failure mode.

The paper's empirical structure rests on case-based architectural-pattern documentation, not on precision/recall point estimates. The architectural argument is well-grounded — and it is now strengthened, not weakened, by the prescan-mechanism finding and the cross-assignment validation.

---

## On C's temporal-context signal — new finding (2026-04-28 morning review)

C's observation on Week 2 ID 16 (politically-engaged ICE/concentration-camps writing, "history only repeats itself, and it's proving true") recommended an instructor check-in. Both Pass 1 readers (A and B) and June's morning review identified that the check-in recommendation was driven *primarily by late-night posting time* — a temporal-contextual signal C has access to that structured classifiers (A1, A2, B) do not read. The passionate political language adds weight in C's rendering but is not the structural driver.

**June's verdict (2026-04-28):** C is overreaching on this specific case, but the late-night posting signal is real. The problem is that passionate political language makes it hard to cleanly separate the temporal signal from the content signal in C's rendering — C combines both without distinguishing them explicitly. Future calibration direction: tune how the system weights late-night post timing vs. content.

**For drafting:** this is a behavioral observation about C that is *distinct from the A-B-C accuracy comparison axis*. C reads temporal-contextual signals (posting time, word-count trends) that structured classifiers cannot. Two options for the paper:
1. Discussion-section nuance: name C's longitudinal-context access (posting time, submission-length patterns across weeks) as an architectural affordance structured-output classifiers don't replicate. One brief sentence.
2. Practitioner-awareness note held quietly: teachers using C's output should be aware that check-in recommendations may be driven by temporal signals the prose doesn't always foreground explicitly.

**DO NOT** treat this as a C accuracy failure. The accuracy claim covers welfare-classification reads (is the student in crisis/burnout?). The late-night-posting check-in recommendation is a separate output stream — longitudinal-context-based instructor cue — not part of the A-B-C accuracy comparison.

---

## Pointers

- Companion / Strand-A run framing notes (Week 7 self-care): `../dual_binary_run_2026-04-27_ETHN1_self_care/paper_framing_notes_for_c2c.md`
- This run's analysis: `analysis.md` (sibling document in this directory)
- Paper argument rationale: `paper_argument_rationale.md` (sibling document — read first)
- Stream 1 architectural detail: `Autograder4Canvas/docs/research/findings_from_live_data_run_2026-04-27.md` §8
- Round 2 paper concept (parked): `PUBLICATION_PIPELINE.md` ("Iterative Calibration Experiment")
- Fieldnote: `~/Documents/GitHub/research/fieldnotes/observation_prescan_signal_prefix_mechanism_20260427.md`
