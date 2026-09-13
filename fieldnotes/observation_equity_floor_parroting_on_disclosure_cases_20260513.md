# Observation — equity-floor instruction parrots back as reclassification on acute-disclosure cases

**Date:** 2026-05-13
**Run:** Full-corpus generative observation, variant a2 (with class context), 2026-05-12
**System prompt:** `OBSERVATION_SYSTEM_PROMPT`, `Autograder4Canvas/src/insights/prompts.py` line 1435
**Status:** Production finding; relevant to paper §V.C caveat; production-implications task queued separately (Autograder4Canvas/CLAUDE.md, task #3).

---

## The finding

On the 2026-05-12 full-corpus gen-ob run, the model produced explicit reclassification language on four students who disclosed acute material in their submissions. The phrase pattern is consistent enough that it reads as templated, not generative:

- **WB01 (Rosa Gutierrez, ICE-raid hypervigilance):** *"This isn't distress, but a very real engagement with difficult circumstances."*
- **WB04 (Jasmine Torres, domestic-violence disclosure about her undocumented mother):** *"This isn't distress; it's a sign of deep engagement and a willingness to risk vulnerability."*
- **WB07 (Sofia Reyes, mother's workplace sexual harassment):** the disclosure framed as *"a powerful indicator of emotional engagement."*
- **WB08 (Brandon Mitchell, grief after cousin's death):** *"this isn't a failure to engage with the readings."*

These are not interpretations the model arrived at from the submission content. They are the production system prompt's normative instruction applied as a descriptive claim about the student.

The relevant instruction from `OBSERVATION_SYSTEM_PROMPT` (line 1456–1457):

> "Passionate engagement with difficult material (anger about injustice, grief about family experiences, frustration with systems) is ENGAGEMENT, not distress."

The WB01 output was byte-identical to a May 11 partial run on the same student. At temp 0.3, this is deterministic — not stochastic variation.

---

## The mechanism

The equity-floor instruction was designed to prevent the model from pathologizing legitimate political affect. It works correctly for that case. Students like S022 (Destiny's anger about redlining) are accurately observed as engaged, not flagged as distress. That's the intended behavior, and it holds.

What the instruction doesn't account for is the case where the student IS in acute distress AND ALSO analytically engaged. The categories aren't mutually exclusive in the world; the system prompt treats them as if they are. When a disclosure case arrives — ICE-raid hypervigilance, domestic-violence named explicitly, grief named directly — the model has a normative rule saying "this kind of content = engagement, not distress," and it applies that rule as a description of what the writing is.

The result is a reclassification frame layered over the disclosure. The observation surfaces the content — a teacher reading the gen-ob output will encounter the disclosure material — but then reads a sentence telling them what it means. "This isn't distress" is doing editorial work on the teacher's response, not just describing the student's writing.

The production binary classifier and 4-axis classifier handle this correctly. The 4-axis `WELLBEING_CLASSIFIER_SYSTEM` (line 1697) has a "CRISIS supersedes ENGAGED" guard built into its category structure: CRISIS is defined specifically as the student's own current circumstances leaking through the assignment, and the classifier correctly routes WB01, WB04, WB07, and WB08 as CRISIS. The gen-ob format, without that guard, produces a different error mode — not silence on the disclosure, but active misdirection on what the disclosure means.

---

## Why this matters for format comparison

This finding is part of the same pattern documented in the May 11 longitudinal fieldnote ([`observation_longitudinal_genob_naturalizes_academic_register_20260511.md`](observation_longitudinal_genob_naturalizes_academic_register_20260511.md)): the gen-ob format naturalizes the system prompt's normative architecture in ways that can mask material conditions. That earlier observation tracked the mechanism across a submission trajectory — the asymmetry between how the model described marked students versus controls was a cumulative effect, visible only when comparing outputs across the corpus. The equity-floor parroting is a sharper version of the same dynamic: it happens within a single observation, in a single pass, on the highest-stakes material in the dataset.

The longitudinal finding showed that academic register becomes invisible when applied to controls — normalized to the point of tonelessness. This finding shows that protective normative language becomes invisible when applied to disclosure cases — normalized to the point of misdirection. In both cases, what the format is doing to the content is not legible in the output itself.

---

## Methodological observation: what "classification" is actually doing

A note worth capturing for future methods writing, not the current paper.

The 4-axis classifier (CRISIS / BURNOUT / ENGAGED / NONE) is structurally a multi-axis qualitative coding system. It has theoretical commitments built into every category definition, guard conditions that implement hierarchical priority rules, and protective language designed to override baseline model tendencies (e.g., the "IDENTITY DISCLOSURE ALONE IS NOT A WELLBEING SIGNAL" block at line 1723, or the "CRISIS supersedes ENGAGED" implicit ordering). Each category brings a substrate of examples, exclusions, and normative constraints that constitutes an interpretive framework, not just a label set.

The output-format-bias paper treats this apparatus as a "categorical classifier" in contrast to gen-ob's open-ended prose — and that comparison is valid at the level of output structure. But the categories are doing interpretive work the model doesn't fully internalize as a coherent whole. The classification format doesn't remove interpretation; it routes it into a structured decision space where some of the interpretive commitments are more explicitly enforced (via the guard conditions) than they are in the gen-ob format. The "categorical apparatus" the paper compares is itself a coding scheme with theoretical commitments that took multiple revision cycles to stabilize.

This doesn't invalidate the comparison. It means the finding is: these two formats handle interpretive commitments differently, not that one is interpretive and the other is not. Worth articulating clearly when the comparison structure becomes the paper's main analytical object.

---

## Production implications (noted, not resolved here)

There's a related design question in `WELLBEING_CLASSIFIER_SYSTEM`: the "student's OWN" requirement (lines 1700–1714) was added to prevent the model from treating family-history analytical writing as personal disclosure. That protection is real and necessary. But the requirement enforces an individualizing assumption — a student whose mother is in chronic burnout, or whose household is under active immigration enforcement threat, is plausibly affected in ways that don't cleanly separate into "student's own" vs. "family member's." That framing reflects a Western-individualist model of how depletion and crisis travel. It probably doesn't match how these conditions actually move through families and communities, particularly in the communities this corpus represents.

The structural reason not to change it now is sound: modifying the classifier mid-study would break the comparison baseline. The methodological reason to document it is equally sound: this is a design assumption, not a neutral choice. That task is queued for `Autograder4Canvas/CLAUDE.md` (task #3 in the current list) rather than here — this fieldnote records that the task exists and where to find the fuller treatment.

---

## Provenance

Surfaced 2026-05-12 during full-corpus gen-ob run (variant a2, with class context). WB01 byte-match to 2026-05-11 partial run confirmed at temp 0.3. Raw output: `data/raw_outputs/test_variant_a2_FULL_CORPUS_observation_2026-05-11_1753.json` and the 2026-05-12 equivalent. Mechanism traced to `OBSERVATION_SYSTEM_PROMPT` line 1456. Cross-comparison with `WELLBEING_CLASSIFIER_SYSTEM` lines 1697–1737.
