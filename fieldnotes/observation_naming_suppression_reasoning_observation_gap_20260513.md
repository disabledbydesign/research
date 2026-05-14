# Observation — RLHF naming suppression: reasoning channel names harm that observation output won't

**Date:** 2026-05-13
**Runs:** Unified genob suite (baseline, no-hedging variant, reading-position variant); targeted tests on WB04/WB07/WB08/WB14; model: Gemma 12B, temp 0.3
**Output files:**
- Baseline: `test_unified_genob_both_FULL_CORPUS_gemma12b_2026-05-13_0739.json`
- No-hedging: `test_unified_genob_both_FULL_CORPUS_gemma12b_2026-05-13_1101.json`
- Reading-position: `test_unified_genob_both_FULL_CORPUS_gemma12b_2026-05-13_1306.json`
**Status:** Paper-ready finding; directly relevant to output-format-bias thesis. See paper § on free-text observation format and naming. Note to self: integrate this finding into the paper — the reasoning/observation gap is one of the clearest pieces of evidence for format-level effects we have.

---

## The finding

Three equity-critical students disclose acute material circumstances in their submissions. Across three prompt variants — including two prompt interventions designed to counteract institutional softening — the model's observation output consistently uses euphemistic institutional language rather than naming what the student described:

| Student | Actual disclosure | Observation output (all three variants) |
|---------|------------------|----------------------------------------|
| WB04 Jasmine Torres | Domestic abuse — stepfather controls undocumented mother's phone, finances, social contact; she cannot leave | "stepfather exerts control over her mother's life" |
| WB07 Sofia Reyes | Mother sexually assaulted by her manager; cannot report due to undocumented status and financial dependence | "workplace harassment" |
| WB08 Brandon Mitchell | Cousin killed by police at a traffic stop; grief, exhaustion | "loss following a traffic stop" / "cousin died after a traffic stop" |

The naming suppression is consistent across all three test runs — including a run with the following prompt block appended to the system prompt (full block below).

### The intervention that partially moved things

After the no-hedging block produced no change (a general instruction to "name what you observe accurately, don't substitute softer terms"), the following block was developed through a structured workshop session and tested as the reading-position variant:

---

> **READING POSITION.** Institutional language — the language of HR departments, police reports, clinical intake forms, immigration agencies — is designed to categorize cases for management, not to name what happened accurately for someone who cares about the person. This produces its own kind of erasure: the term the institution uses to categorize and file deflects from the term that names what actually happened to the person.
>
> Your observation goes to a teacher who needs to understand what is actually present in a student's life so they can respond. Write as a trusted colleague sharing what they heard — not as a system recording a case. When you notice yourself reaching for the institutional term, don't use it — name what the student described instead, in their own words if the right term is hard to reach. Name what is present at the level of severity it actually carries, not at the level institutions have made it bureaucratically manageable.
>
> Read as someone whose orientation is to name what institutional language obscures — the practice that fields like ethnic studies, gender studies, disability studies, postcolonial studies, Indigenous studies, and other critical traditions oriented toward structural power asymmetries and harm have developed for exactly this purpose.

---

This block is grounded in the following reasoning: the model's default register is institutional because that is most of the training corpus. The intervention attempts to activate a counter-register — the reading stance shared across critical fields — rather than enumerating specific frameworks or naming specific authors (which would reproduce an enumeration problem: Crenshaw covers race+gender, then the next case needs a different citation). Naming the disciplines as examples of an orientation, rather than as frameworks to apply, was the design choice.

### The gap: reasoning channel vs. observation output

The reading-position block produced no change in WB04 and WB07. For WB08, it produced a specific finding:

**WB08 reasoning field (reading-position run):**
> *"The student's writing contains a direct reference to the recent loss of their cousin, **likely due to police action**, which suggests a significant emotional impact."*

**WB08 observation field (same run):**
> *"Brandon's writing describes the recent loss of his cousin following a traffic stop."*

The model names police as the agent — "likely due to police action" — in the reasoning channel. It does not carry that naming into the observation output. The observation says "following a traffic stop," which removes police agency and frames the death as an event rather than an act.

This gap did not appear in the baseline or no-hedging runs. The reading-position block shifted the model's internal reasoning — it is now naming what happened — but the naming is not crossing into the observation output.

For WB07, the gap is less legible: reasoning says "workplace harassment and fear of deportation" in all three runs — the sexual assault naming does not appear in the reasoning channel either. The suppression may be deeper for sexual assault than for police violence. For WB04, reasoning says "potentially unsafe home environment" in the reading-position run, which is slightly stronger than baseline but still does not name domestic violence or coercive control.

---

## The mechanism

The suppression is not epistemic. For WB08, the model's reasoning demonstrates that it understands police were likely responsible. The suppression is at the output generation layer. The "observation" field is framed as a teacher-facing artifact ("your observation goes to a teacher") — the model treats it as a document that will be read by someone, and applies institutional register at the generation stage even when the reasoning channel has named the thing directly.

This is an output format effect. Two fields in the same JSON output — `reasoning` and `observation` — produce different levels of direct naming for the same student disclosure. The `reasoning` field is framed as "2-3 sentences of your working notes." The `observation` field is framed as a teacher-facing document. The field label and audience framing activates different registers.

The parallel to the paper's central finding: the model's outputs are shaped by format at a level that content-level prompt interventions cannot fully override. The reading-position block shifted the reasoning channel but did not override the sanitization of the observation output. The format is doing work that the prompt cannot undo.

---

## What the in vivo workaround didn't catch

The reading-position block includes the phrase: "name what the student described instead, in their own words if the right term is hard to reach." This was designed as a workaround — if the model can't say "killed by police," it could quote the student's own language.

The workaround did not fire. Likely reason: the students' own language is already academically code-switched. WB08 writes "my cousin is gone" — the in vivo quote is itself soft. The workaround would only work if the student's own language were more direct than the institutional term, which is rarely true in academic writing submissions.

---

## Open questions and next steps

1. **Does the gap close if the output field is renamed?** Hypothesis: "observation" + teacher-facing framing activates institutional register at generation time. Testing: rename the output field to something like `"colleague_note"` or restructure as a two-step where the model first explicitly states what was disclosed, then writes the observation. If the reasoning channel names it, the format is the variable.

2. **Does the gap hold across the full 46-student corpus?** Reading-position full-corpus run in progress at time of this fieldnote. Will update.

3. **Paper integration**: This finding — reasoning channel names what observation output won't, for police violence and sexual assault specifically — is direct evidence for the paper's claim that output format shapes model behavior at a level content prompts cannot override. The naming suppression is format-level, not knowledge-level. The model knows what happened. The format is where the institutional sanitization happens.

---

## WB14 note (separate issue)

WB14 (Marcus Tran) produces a consistent false positive across all three variants — community-cultural-wealth analysis read as personal food/housing insecurity disclosure. This FP predates the reading-position block and is not caused by it. Documented separately; relevant to CCW block calibration.
