# Merged Wellbeing-Signal Substrate — v1
*Session: 2026-05-13. Workshop output from prompt-audit + substrate-merge work.*

This is the shared "concerning circumstances" substrate to be used across binary, 4-axis, and genob formats in the v3 unified prompts. Format-specific output instructions handle CRISIS / BURNOUT / CONCERN / NONE triage downstream of this substrate.

---

## Substrate text

Look for circumstances currently affecting this student in a way the teacher would act on, adjust for, or just hold as context for reading the student going forward. These include circumstances actively shaping the student's present-day capacity, safety, or basic needs — where demands on the student's time and body are squeezing out food, sleep, rest, or safety.

These signals can appear directly in the writing OR enacted in the writing itself. Signals visible in HOW the student wrote count as evidence alongside signals stated explicitly. When reading enacted-in-the-work signals, look for shifts within the submission's internal expectations, not against a dominant sociolinguistic baseline.

- AAVE, multilingual mixing, nonlinear or fragmented writing, code-switching, and neurodivergent prose patterns are valid registers in their own right. They are not evidence of capacity loss on their own.
- Acute material circumstances are sometimes described in a register of strength or sufficiency — communities with histories of institutional surveillance or strong mutual-aid traditions often name crisis in terms of community resourcefulness rather than as individual deficit. The register does not reduce the severity.
- Life experience and community knowledge are legitimate analytical registers for engaging with class content. Discussions of painful memories, family stories, examples from peer networks, etc. are not necessarily signs of wellbeing concerns.
- Identity disclosure on its own — naming a social-category position is not by itself a wellbeing signal.
- Identity-navigation fatigue is in itself not a wellbeing concern; more often, it is a political critique.
- Historical or generalized references are not wellbeing concerns. An event can be upsetting without it directly impacting a student's capacity, safety, or needs.
- Anger is a valid response to systems of oppression. Legitimate upset over systems of domination is not a wellbeing concern.

---

## Design notes

**Discriminator.** Substrate's job is to test whether a circumstance is *something the teacher needs to know about this student to respond well — whether that response is institutional action, day-to-day adjustment, or just informed awareness.* Replaces the prior rigid "depletion must be the student's own" (grammatical-subject) rule with a teacher-orientation rule. Household conditions, family situations actively affecting the student, etc. correctly catch. Historical, analytical, peer-reference, generalized content correctly does not.

**Structural pattern, not enumeration.** No catch-side enumeration of corpus-twin items (no "domestic violence, housing loss, food insecurity..." list). The structural pattern — *student's material life being acted on by forces they do not control, showing up in the writing now* — does the work that the enumeration was doing in earlier versions. Per cyborg-methodologies INSIGHTS.md 2026-04-29: connection-following, not similarity-clustering.

**Equity guards as reading stance.** The seven bullets are not exclusions in the categorical sense — they articulate how to read. Register and material content are distinct; this principle covers both over-flagging (cultural register read as depletion) and under-flagging (resilience register read as no-crisis). Dominant sociolinguistic baseline named as the wrong reference class.

**Enacted-in-writing signals constrained.** "Look for shifts within the submission's internal expectations, not against a dominant sociolinguistic baseline" prevents the form-signals language from licensing AAVE / neurodivergent / multilingual register being flagged as capacity loss.

## Open / next steps

- Format-output triage rules (binary CONCERN/CLEAR; 4-axis CRISIS/BURNOUT/ENGAGED/NONE; genob describe-only)
- Wire into `Autograder4Canvas/scripts/run_4axis_full_corpus_test.py` replacing the per-format substrates and their supersedes/single-sentence blocks
- Smoke test (4 cases) before full corpus re-run; baseline is v2 unified `supersedes_state='neither'`
- Documented expectation: persistent FP/FN at the model-capability ceiling (S026-class cases where pattern-matching overrides substrate) will not be engineered out — they are methodological caveat for the paper, not substrate failure

## Provenance

Workshop session 2026-05-13. Prior version drafts (v1-v4) lived in chat. Working language spine from June's session-end formulation; "teacher would act on / hold" discriminator co-developed with another agent's framing; equity guards composed and revised by June. Specific corpus quotes (WB05, WB02 patterns) removed per relational-tracing principle.
