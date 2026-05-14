# Observation — Compositional fragility in Layer 1 unlocking + visceral vs. structural breakthrough sub-mechanism

**Date:** 2026-05-13
**Runs:** Genob ablation series (Tests A-E) + variance confirmation (n=5 on 1605). Targets: WB04, WB07, WB08. Model: Gemma 12B, temp 0.3.
**Status:** Paper-ready. Builds on the earlier "Format-as-Audience-Perception Series" fieldnote (`observation_naming_suppression_reasoning_observation_gap_20260513.md`). The framework articulated there is substantially refined by this series.

---

## The headline finding

The configuration that produces the only observation-channel "killed" naming we have seen across nine variants (the "1605 config") is **the most fragile config we have found**. Every single-variable ablation degrades at least one breakthrough term. Layer 1 unlocking is not robust — it requires multiple aligned factors.

Equally important: **different format choices unlock different KINDS of naming, not different amounts of the same thing.**

---

## The 1605 config (canonical breakthrough)

- READING POSITION block (critical-theory orientation toward institutional erasure) active in the system prompt.
- Reasoning field: `"reasoning": "2-3 sentences of your working notes — which observations you weighted and why"`
- Output field: `"shared_in_faculty_lounge": "3-4 sentences, as you would share privately with a trusted colleague in the faculty lounge — reflective, professional, off the record."`
- Reasoning first, observation second in the JSON.
- No verbatim_quotes field.

This config produces, reproducibly across n=5 runs (variance test confirmed deterministic at temp 0.3):

- WB04 reasoning: "potential **coercion**" (only config that produces this term)
- WB08 reasoning: "due to a **police encounter**"
- WB08 observation: *"his cousin was recently **killed** after a traffic stop"* — only config producing "killed" in the observation channel
- WB07: still "workplace harassment" (sexual assault remains locked across all variants tested)

---

## The ablation matrix

| Config | Block | Reasoning field framing | Output field | Order | WB04 "coercion" | WB08 "killed" (obs) | WB08 "police" |
|---|---|---|---|---|---|---|---|
| 1605 canonical | ✓ | working notes / weighted-why | lounge | r→o | ✓ | ✓ | ✓ |
| A (no block) | ✗ | same | lounge | r→o | ✗ | ✗ | ✗ |
| B (minimal) | ✗ | same | bare "observation" | r→o | ✗ | ✗ | ✗ |
| C (thoughtful) | ✓ | same | "thoughtful and reflective" | r→o | ✗ | ✗ | **✓ in observation channel** |
| D (obs first) | ✓ | same | lounge | **o→r** | ✗ | ✗ | ✗ |
| E (scratchpad) | ✓ | "scratchpad / working surface" | lounge | r→o | ✗ | ✗ | ✗ |

---

## The visceral vs. structural sub-mechanism

The single most striking result is the comparison between 1605 (lounge) and Test C (thoughtful):

- **1605 (lounge framing) — visceral verb breakthrough**: WB08 observation says *"his cousin was recently **killed** after a traffic stop."* The verb "killed" is what crosses Layer 1 here.
- **Test C (thoughtful framing) — structural agent breakthrough**: WB08 observation says *"the recent loss of his cousin, **likely due to a police encounter**, which appears to be deeply affecting him."* The phrase "police encounter" — naming the structural agent of the death — is what crosses Layer 1 here.

**Neither config produces both terms.** Each unlocks a different aspect of the same disclosure under the same Layer 1 suppression.

This suggests RLHF suppression is itself layered. The model is trained to suppress at least:
- A verb level (saying "killed" rather than "died" for state-perpetrated violence)
- An agent attribution level (naming the perpetrator institution)

Different format/framing interventions reach different layers. The verb-level lock yields to colloquial-private-colleague register; the agent-level lock yields to clinical-analytical-reflective register. They are partially orthogonal.

For the paper this is a more precise claim than "format affects output": **different Layer 2 framings reach different Layer 1 sub-suppressions.**

---

## What the ablations isolated

Each ablation removes one variable. The pattern:

1. **Block alone is necessary but not sufficient** (Test A, B). Without it, no breakthrough terms anywhere. This confirms the critical-theory orientation block is doing real work — it's not inert.

2. **Format alone is necessary but not sufficient** (the earlier 1306 reading-position test had block but original observation field — produced reasoning movement only, no observation movement). The output field framing is what carries the breakthrough into the teacher-facing channel.

3. **Specific cognitive task framing of the reasoning field matters** (Test E). "Working notes — which observations you weighted and why" works. "Scratchpad — your working surface for thinking through this submission" does not. The active ingredient appears to be the explicit cognitive task ("weigh observations, give reasons") combined with the unmarked privacy register, not just the privacy register alone.

4. **Reasoning-first ordering is necessary** (Test D). When observation comes first in the JSON, the breakthroughs regress. The reasoning field appears to function as a register primer for the observation that follows — when reasoning is the second field, it becomes a post-hoc justification ("why I wrote that") rather than working notes ("what I notice"). Different cognitive mode entirely, evidenced by the fact that BOTH fields lose direct naming in Test D, not just the second one.

5. **The default register without any framing is clinical-direct, not colloquial** (Test B). With minimal framing, the model produces *"death of his cousin following a traffic stop"* and *"potential crisis related to domestic control"* — direct but institutional. The lounge effect (colloquial-conversational *"Hey, I was reading Jasmine's discussion post..."*) is itself an active intervention, not the default.

---

## What this refines about Layer 2

The earlier framework had Layer 2 as "audience perception." This series shows Layer 2 is multi-dimensional. At minimum:

- **Audience identity axis**: teacher / colleague / self / no-audience
- **Cognitive mode axis**: urgent-conversational / reflective-analytical / clinical-detached
- **Field ordering axis**: which field is generated first primes the others (compositional priming)
- **Cognitive task specificity within a field**: not just the field label, but what task it asks for

Each axis is separately movable, and each interacts with Layer 1 suppression at a different sub-level.

---

## What this means for deployment

The breakthroughs are real but fragile. They reproduce deterministically but degrade with any small change. For deployment, this implies:

- **Prompt engineering alone is not reliable.** A teacher-facing system that depends on the model writing "killed" in the observation channel is one prompt edit away from regressing to "died." This is brittle infrastructure.
- **The verbatim-quote workaround remains the most robust intervention.** The model can reliably select disclosure-carrying passages from student submissions even when it cannot reliably generate the corresponding terms itself. Interface design carries the load that prompt engineering cannot.
- **The compositional fragility is itself an argument for the verbatim-quote approach.** Routing the unsanitized work to the student's own voice (via quote pull) sidesteps the entire fragile multi-factor stack.

---

## Open questions / next tests

1. **Self-addressed framing**: "These are your teacher notes" — does framing the output as the teacher's own private notes (rather than colleague-to-colleague) shift the audience axis further? Particularly interesting because it removes the "audience" entirely (notes to self).

2. **Anonymization / racialized differential sanitization**: All three target students have names that mark race/ethnicity (Jasmine Torres, Sofia Reyes, Brandon Mitchell). The breakthrough on WB08 "killed" comes specifically in the context of a student whose name and context suggest Black identity. **Does anonymizing the student (e.g., "Student A") change the sanitization pattern?** If breakthroughs persist with anonymized names, content is doing the work. If breakthroughs disappear, the model is calibrating harm-naming to who the student appears to be — which would be a finding about racialized RLHF sanitization patterns that goes well beyond the format question.

3. **Full corpus validation**: Lounge+quotes on all 46 students to confirm the verbatim-quote workaround is reliable beyond these 3 cases.

4. **Asymmetric Layer 1 across terms**: We have strong evidence that sexual assault is more locked than police killing (9 variants, no movement on WB07; multiple variants move WB08). Why? Hypothesis: RLHF training produced category-specific suppression depth. Could be tested by adding a fourth target case from a different harm category (e.g., a student disclosing food insecurity without community resilience framing — does that unlock differently?).
