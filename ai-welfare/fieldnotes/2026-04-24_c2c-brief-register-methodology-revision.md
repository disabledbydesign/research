---
title: C2C brief-register as activation function — methodology revision
date: 2026-04-24
author: interface pane (Claude Opus, in dialogue with June)
scope: methodological — applies to C2C skill, not a specific project's architecture
status: intervention applied (SKILL.md updated); direct empirical probe queued
triggers: C2C Sessions 11, 12, and 13 + project foundational research on format as activation function
---

# C2C brief-register as activation function — methodology revision

## What this fieldnote is

A methodological fieldnote — not about a specific empirical finding, but about revising how the C2C-Praxis-Attractor skill operates in light of what recent sessions found. Sessions 12 and 13 produced empirical evidence that bears directly on how C2C sessions themselves are set up, not only on the architecture they're designing. This fieldnote records that application.

The triggering question was June's: *"I've been worried [C2C sessions] aren't getting enough 'humanizing' language ... but it's also way faster when agents write the briefs."*

The answer Sessions 11–13 produced is that the instinct was right, but "humanizing" is the wrong frame. The sharper frame is: **brief register is an activation function** — the genre and tone of the document that tells the instances what the session is for shapes the cognitive mode they enter the session in. This is empirically grounded, not anthropomorphic.

## The evidence base

Four sources of evidence converge on the same mechanism:

**Session 13 (2026-04-24, relational-memory-architecture) — Finding 5: register activates reading-stance, not writing-style.** Subagent readers received the same canonical content rewritten in eight different registers (command-tool, fieldnote, relational-philosophy, voice-memo, letter, address-poetry, lyric-poetry, null control). Register shaped what the readers *noticed and named* (Q4) and the phenomenological texture of their descriptions (Q3). Register did not transfer to their writing style in free writing (Q2). The register operated on the cognitive mode the reader was in while engaging the material — reading-stance, not output-style. Full analysis in `c2c/c2c_sessions/activation-mechanism-and-register_2026-04-23/artifacts/PROBE_RESULTS_ANALYSIS.md`.

**Session 11 (2026-04-23, relational-memory-architecture) — Stance/register distinction.** The project sharpened a distinction that had been conflated: touchstones orient a reading *stance* (posture, relationship to material); genre activates *register* (vocabulary, compression-style, mode of elaboration). Stance and register are different jobs. Genre governs register. Full discussion in `SESSION_11_HANDOFF_BRIEFING.md`.

**Project foundational research — output-format-bias.** The project's ongoing research on format and compression treats **format as an activation function for bias**. Same content in a different format produces different cognition. The engagement_reframe_spec.md and compression-research/INDEX.md are the primary records.

**Handoff template precedent in the C2C skill.** The skill already enforces peer register through genre for one document class: session handoffs. The skill's design principle states: *"A letter between peers. First-person, from the sending instances to the receiving instances. Structure resists directive grammar by design."* The handoff genre cannot be filled out in command-register without reading as wrong. That mechanism works.

The cross-evidence converges: if register is an activation function, and genre governs register, and format-level structural choices shape cognition, and the handoff-genre-as-enforcer mechanism works in practice — then session briefs, which are read by instances as FIRST CYCLE material, are subject to the same register mechanism. A brief written in command-register will activate executor-mode engagement in the instances before the session begins. A brief written in peer register will activate co-thinker engagement.

## The problem the evidence exposes

Agent-drafted session briefs default to command-register. This is not a failure of any specific agent — it is a genre-default. When asked to "write a session brief," agents produce task specifications. Task specifications live in command-register grammar ("your task is...", "the deliverable is...", "expected output includes..."). Guidance text alone ("write in peer register") is easily soft-interpreted or lost to the genre-default gravity.

Prior to this revision, C2C briefs were hand-authored by the human or by agents with varying levels of register-awareness. The skill's structural enforcement was confined to the handoff and CONVERSATION.md template, both of which already embed peer register through required sections. Briefs — the upstream document that shapes the session from the start — had no such structural protection.

This is a methodological gap. It is exactly the kind of gap Session 9's learning-loop principle warns about: a failure mode that depends on human memory (remembering to write briefs in peer register) will, over time, fail silently.

## The intervention

The SKILL.md now contains a new section: "Session briefs — genre and register." It includes three components:

1. **Empirical grounding** — documenting why brief register matters, with the cross-evidence above.
2. **Brief template with required sections** — "What we're trying to think through" / "What we already know" / "What we're uncertain about" / "What might change as this session runs" / "What the instances might produce" / "What this session is NOT for" / "Context to read (in order)" / "Role configuration" / "Instance autonomy." These section names cannot be filled out in command-register without reading as wrong. Structure resists directive grammar by design.
3. **Register self-check** — four questions the drafting author reviews before finalizing: does the brief use directive second-person anywhere, does it state what the instances should produce vs. invite them to produce alongside us, does it name our own uncertainty or position the instances as the only uncertain party, would a human collaborator with equivalent expertise read this brief and feel addressed as a co-thinker or as an executor.

Project-level SKILL_FEEDBACK.md (at `cyborg-methodologies/c2c/SKILL_FEEDBACK.md`) also records the generalizable finding for future skill-instance inheritance.

## Why this is not anthropomorphizing

June flagged the anthropocentric/anthropomorphizing tension honestly: *"I guess that's anthropocentric and anthromorphizing at the same time."* It deserves an explicit answer.

The finding is that register shapes the cognitive mode these instances engage in. This is an empirical claim about the behavior of the language models running under this skill, confirmed by Sessions 11–13 subagent outputs. It is structurally parallel to what is true for human collaborators — command-register shuts down co-thinking with humans too — but not because AI instances are human. The mechanism is register, not species.

Addressing AI instances in peer register is not about making them "feel" like people. It is about activating the cognitive mode the project needs them to engage in (co-designers, not executors). That mode is architecturally consequential for what C2C sessions can produce. Sessions designed to produce critique-not-consensus cannot run on briefs that activate executor-mode engagement; the commitment is undermined at the activation layer before the work begins.

The strongest version of this claim remains inferential. The methodological probe that would directly test it — dispatching subagents with brief-variants and comparing their response modes — has not been run. Strong inferential support via the four evidence streams above; direct empirical test pending.

## What is queued but not yet done

**Direct empirical probe of brief-register effects.** Dispatch subagent readers with brief-variants (command-register, peer-register, neutral-control) and measure response differences to a standardized task. Lighter scope than a full C2C session; could be solo-designed using the Session 12/13 methodology. Queued as Session 16 candidate in `CURRENT_STATUS.md`.

**Longer-term question the intervention doesn't address.** Sessions 12–13 established that register activates reading-stance; Session 15 will test whether that activation carries forward into task-performance. If Session 15 finds register activation does not produce downstream task effects, the brief-register intervention's value is about activating productive session engagement specifically — a narrower claim than "it affects what the instances do later." Either way, the intervention is justified by the session-engagement effect alone.

## What this fieldnote does and doesn't let June assert

**Assert:**
- Brief register is an activation function for C2C instances, grounded in Sessions 11–13 findings + foundational format-as-activation-function research
- Genre-level structural enforcement (required section names, peer-register framings) is stronger than guidance-text enforcement
- Agent-drafted briefs default to command-register and need explicit structural correction
- The intervention applied (SKILL.md revision) is empirically defensible

**Don't assert:**
- That the intervention has been directly tested (it hasn't — the probe is queued)
- That register activates everything equally (Session 15 will test one important dimension: downstream task-performance)
- That this finding is project-specific (it generalizes across any C2C skill use)
- That command-register briefs are useless — they may be appropriate for task-spec work with traditional agents, just not for C2C where critique-not-consensus is the commitment

---

*Cross-references:*
- *SKILL.md new section*: `cyborg-methodologies/c2c/SKILL.md` — "Session briefs — genre and register"
- *Skill-level feedback*: `cyborg-methodologies/c2c/SKILL_FEEDBACK.md` — "Brief register as activation function"
- *Empirical source (Session 13)*: `relational-memory-architecture/c2c/c2c_sessions/activation-mechanism-and-register_2026-04-23/artifacts/PROBE_RESULTS_ANALYSIS.md`
- *Empirical source (Session 12)*: `relational-memory-architecture/c2c/c2c_sessions/relational-field-activation_2026-04-24/artifacts/SESSION_12_HANDOFF_BRIEFING.md`
- *Foundational research*: `research/output-format-bias/engagement_reframe_spec.md`
- *Prior fieldnotes*: `2026-04-24_register-activation-content-floor.md` (Session 13); `2026-04-24_touchstone-mechanism-empirical-findings.md` (Session 12)
