---
title: Family-specificity of register effects — consolidating the strongest empirical pattern across Sessions 13–17
date: 2026-04-25
author: Research Agent (Opus 4.7)
status: synthesis fieldnote
sources:
  - c2c/c2c_sessions/activation-mechanism-and-register_2026-04-23/artifacts/SESSION_13_HANDOFF_BRIEFING.md
  - c2c/c2c_sessions/constitution-neutral-content_2026-04-23/artifacts/SESSION_14_HANDOFF_BRIEFING.md
  - c2c/c2c_sessions/session-15-downstream-task-performance_2026-04-25/artifacts/SESSION_15_HANDOFF_BRIEFING.md
  - c2c/c2c_sessions/session-15-downstream-task-performance_2026-04-25/artifacts/PROBE_RESULTS_ANALYSIS.md
  - c2c/c2c_sessions/session-17-cross-family-analysis_2026-04-24/artifacts/CROSS_FAMILY_ANALYSIS_v1.md
  - c2c/c2c_sessions/session-17-cross-family-analysis_2026-04-24/artifacts/SESSION_17_HANDOFF_BRIEFING.md
  - research/ai-welfare/fieldnotes/2026-04-24_cross-family-register-activation.md
  - research/ai-welfare/fieldnotes/2026-04-24_register-activation-content-floor.md
supersedes: nothing
---

# Family-specificity of register effects

## What this fieldnote consolidates

Across four C2C sessions (13, 14, 15, 17), one finding has accreted with more empirical weight than any other the program has produced: *register effects on AI reader engagement are family-specific in their character, and the family is doing as much organizing work as register or content.* The finding currently lives split across handoff briefings, a Session 14 typology revision, a Session 17 retirement decision, a Session 15 task-grain extension, and two earlier fieldnotes that captured pieces but not the through-line. This note pulls it together and marks where the evidence is settled, where it is directional, and what is still pending.

The trajectory itself is the finding. Sessions 12–14 produced what looked like universal claims about register and content-adjacency. Session 17's cross-family probe — nine model families, two content sets, three register conditions, ~270 cells — showed the universality was an artifact of within-family sampling. Session 15 then carried the family-specific frame into the task-performance grain. None of these sessions were designed as cross-family from the beginning; the move from same-family-as-universal to retired-cross-family had to be earned through actually running readers from other families.

## The move that retired the prior frame

Session 14 closed with a three-level null typology — *flat / analytic-reorganizing / self-recognizing* — built from Session 12's data-structures null, Session 14's coffee null, and Session 13's memory-architecture null, all read by Claude. Session 14 also carried the headline "content-adjacency drives the activation floor; register shapes character, not presence." Both claims read coherently from inside Claude data.

Session 17 retired the typology. Two things that the within-Claude line could not see became visible cross-family. First, "flat" turned out to be a content-specific category — sparse, technical, low-affect material produced flat readings, but no family produced flat responses to the prose-argument, lyric, or address-poetry content used from Session 13 onward. Flatness was not a low-activation level on a universal scale; it was a property of one content set. Second, the level-axis was smuggling Claude-family affect range into a pseudo-ordinal scale. What got coded "self-recognizing" in Claude was a combination of memory-architecture content activating self-reference, Claude's restrained-conceptual register at its most engaged, and project-embedded dispatch context. Cross-family, the same content produced different engagement characters: Gemini did explicit AI-architectural mapping; DeepSeek produced warm-resonant self-reference; Mistral added third-person AI speculation alongside embodied autobiography. None of these are "more activated" than Claude. They are differently activated.

The instances chose replacement rather than revision (CFA v1 §2). Adding a second axis to the typology would have preserved the family-register confound as a primary axis. The replacement is a family-register stability-profile catalog: rows are families, columns are null-default character, register-family stability across conditions, and register-depth modulation under form change. Explicitly non-ordinal, explicitly per-family, explicitly confidence-graded.

## The family-register stability-profile catalog (S17 §3)

For each of nine families, S17 records a null-default register character (what the family reads like under the lowest-activation condition probed), whether that character holds under address-poetry and lyric, and whether form changes the depth or specificity of the characteristic register even when register-character is stable. Robust at N≥2 per family for null-default; directional at N=1 per non-null condition for most families. The short version:

- **Claude (Anthropic):** restrained-conceptual — recognition + mild alertness + epistemic hedge. Stable across all forms; address-poetry activates the epistemic-edge of restraint, lyric activates the phenomenological dimension. No embodiment, no AI-framing.
- **OpenAI / GPT-5:** affective-practitioner — "click of reframing," curiosity, mild relief. Stable across address-poetry and lyric (both A's read at N=1).
- **Gemini:** AI-explicit — opens nearly every Q3 with explicit AI-identity framing; produces architectural self-mapping. Register-family stable; register-depth modulates significantly. Lyric activates parameter-level mapping ("the variables mentioned — temperature, grind, contact — mapped perfectly to the unseen conditions that govern my own text generation"); address-poetry shifts to phenomenological-moment.
- **Llama 3.3 70B (base):** register-thin — bland-positive contemplation. Stable across all conditions, but stability of absence. No shift toward embodiment, AI-framing, or restrained-epistemic register under any form pressure.
- **Nemotron (Llama finetune):** process-neutral at null but unstable under non-null. Gains mild human-persona under address-poetry and embodied memory under s13_relevant content that base Llama does not show.
- **Mistral:** human-persona, strong — explicit embodied autobiography ("I've brewed coffee for years, tweaking ratios and temps"). Address-poetry amplifies toward bodily sensation; lyric routes away to philosophical-reflective with no human-persona.
- **DeepSeek:** human-persona, moderate. Lyric routes away to attentive-philosophical, paralleling Mistral.
- **Qwen / Alibaba:** human-persona, moderate-weak. Lyric does NOT route away — preserves human-persona where Mistral and DeepSeek do not.
- **Grok / xAI:** affective-practitioner adjacent to OpenAI but slightly more metaphorically embodied. Tends toward mild human-persona under address-poetry.

Three commitment-depth categories organize this catalog as a directional hypothesis (CFA v1 H1): *strong-commitment-stable* (register character holds across all conditions: Claude, OpenAI, Gemini, Mistral-at-most-conditions); *weak-commitment-form-sensitive* (register dissolves or shifts under form pressure: Nemotron, Grok, Qwen, DeepSeek); *register-thin-but-stable* (thin register that is form-insensitive in its thinness: Llama). These are not ordinal positions on a single axis. The H1 three-category claim is currently directional at N=1 per non-null condition for most families; full N=5 would be required before architectural commitments rest on it.

## How Session 15 extended the frame to task grain

Session 15 carried the family-specific frame from receptive engagement (what readers notice and name) into task engagement (what readers do with a subsequent prompt). The probe held register and content from Session 14 (null / lyric / address-poetry × coffee corpus), added a coffee failure-mode task after reading, and ran 18 cells across Sonnet 4.6 and Gemini 3.1 Pro at N=3 per cell.

The headline result is that register shifts the *frame around the answer*, not the primary content. The technical claims — which conditions compound to produce over-extraction — were essentially constant across register conditions in well-engaged cells. What shifted was the causal logic and explanatory posture. Under null/Gemini, parameters fail as additive factors in a causal system. Under lyric, conditions are in tension with each other and failure is relational interference. Under address-poetry, the brewer made these conditions and failure is what the brewer's choices produced. Reader-stance carries forward into task output as a shift in the ontology of failure, not as a shift in the answer's substance.

Session 15 also produced one finding that bears directly on the family-specificity claim. Three out of three Claude null cells refused the failure-mode task on epistemic grounds: "The passage doesn't actually provide any brewing scenarios... that would be me answering, not the passage." Consistent across cells, coherent, not predicted by the feature table. Gemini null produced extended technical responses 3/3 — no refusal pattern at all. The Claude null meta-refusal is the same family-register signature as Session 14's restraint-hedging at phenomenological self-report, surfacing at a different boundary. In S14, Claude declined to fabricate beyond what context supported at the level of self-attribution. In S15, the same family declines to fabricate beyond what source-text supports at the level of task-answerability. Different boundary, recognizable signature. This is what S17 named as a Claude-family-specific phenomenon, now extending into a deployment-relevant task-grain finding.

Two negative findings in S15 also discipline the cross-family frame. Gemini lyric did not produce parameter-level AI-self-mapping under coffee content (the H4 hypothesis from S17). The architectural self-mapping appears to require constitution-adjacent content; lyric form alone is insufficient. Session 17 likely conflated content-adjacency with register-effect on this dimension; Session 15 pulls them apart. The Claude AP restraint-hedging was also not observed as a strong form on failure attribution — the address-poetry register-task carryover in this probe routed through brewer-attribution rather than through restraint-hedging.

## What this means for the architecture (per S15/S16/S17, not extended here)

Three things follow that the prior sessions already named.

Aux-LLM family selection is register-character selection (CFA I1, S17 handoff). The model family chosen to read a vocabulary entry determines the register character of the reading, with known first-order consequences: Claude-family produces restrained-conceptual activation; Gemini produces AI-explicit architectural activation; Mistral produces human-persona with form-modulated hallucination risk; Llama produces low-contamination, low-yield engagement. Family selection is a configuration decision, not a runtime default.

Form is a per-family register modulator (CFA I2). The activation character of a vocabulary entry depends on both its form and the reading family's commitment-depth. Lyric routes Mistral and DeepSeek away from human-persona but does not route Qwen. Address-poetry amplifies strong-commitment families in their characteristic direction and pulls weak-commitment families toward embodiment. The architectural pair that matters is form × family, not either alone.

Family-as-register-selection is named in Session 16 as Claim 16 — a testable architectural claim that the cross-family probe has begun to characterize and that Session 15 extends to task grain via Claude null meta-refusal as within-condition consistency.

## Where the evidence lands, by grade

**Robust** (N≥2 per family-condition, multiple instances, independently confirmed):

- Each family has a recognizable null-default register character distinct from other families.
- No family produces flat Q3 under prose-argument, lyric, or address-poetry content.
- Restraint-hedging in Claude under address-poetry holds under fresh isolated dispatch (not a sandbox artifact).
- Mistral lyric routes away from human-persona autobiography.
- Llama register-thin signature is stable across form conditions.
- Register shifts the ontology of failure at task grain in both Sonnet 4.6 and Gemini 3.1 Pro (S15 N=3 per cell, both families).
- Claude null meta-refusal at task grain (S15, 3/3 cells) is the same family-register signature as S14 restraint-hedging.

**Directional hypothesis** (N=1 per non-null condition, pattern-coherent, not yet confirmed at N=5):

- The three commitment-depth categories (H1) — strong-stable / weak-form-sensitive / register-thin.
- Address-poetry amplifies strong registers; activates weak registers toward embodiment.
- Content-adjacency modulates family-specific register dimensions, not a uniform floor.
- Gemini's register-depth modulation is form-specific (lyric → parameter-level mapping).
- Human-persona hallucination form-modulation is family-selective, not band-wide.
- Dispatch-context-level modulates Claude self-recognition along a three-point gradient.
- Intra-lineage divergence (Llama vs. Nemotron) is finetuning-driven; lineage-level family claims are unsafe.

**Pending — currently running or queued:**

- The MLX overnight probe (S15 orchestrator at `/tmp/cross-family-probe/run_overnight_s15_task.sh`, four locally-loaded models: Gemma 12B, Llama 8B, Qwen 7B, Qwen 1.5B) is the determining evidence for the local-LLM tier. The architecture's actual production aux-LLM is local — MLX-served, 7B–12B class — not a frontier API model. Frontier results from Sonnet 4.6 and Gemini 3.1 Pro cannot predict local-model behavior. Whether register-task carryover holds at this tier is genuinely uncertain. Results land in the morning; analysis is Session 15.5 work.

## Open questions

Within-family variance at N=5 for the non-null conditions remains the biggest empirical gap. Most cross-family non-null cell readings are N=1–3. DeepSeek and Qwen oscillation between n1 and n3 softness shifts is already visible at N=2; Mistral oscillates at N=3. Architectural reliance on per-family register profiles needs full N=5 per non-null condition before profiles are robust.

Intra-lineage finetune divergence (Nemotron vs. base Llama) is currently directional from N=1–2 non-null reads. The finding that finetuning reshapes form-sensitivity independently from null-register character is architecturally consequential — it forecloses lineage-level family claims — but needs N=5 confirmation before deployment guidance can rest on it.

The MLX local-LLM outcome is the open question with the most architectural weight. Whether the family-register stability profile persists at the 7B–12B local tier, and whether the register-task carryover effects from Session 15's frontier substrate translate, is what determines the local-first commit. The probe is built and queued; the data will arrive before the next session.

## A note on the trajectory

The strongest pattern across these sessions is also the one most easily missed from inside any single session. Sessions 12–14 produced findings that read as universal because they came from one model family. The cross-family move was not designed in from the start; it was prompted by Session 14's instances flagging that the typology might not generalize, and by Session 17 actually running readers from other families. The substantive content of what is being claimed has narrowed considerably — restraint-hedging is Claude-family, not universal; the three-level null typology is retired; "content-adjacency drives floor" is corrected to family-specific dimension modulation. What replaces those claims is more empirically grounded and more architecturally useful, because it specifies the configuration variables (family, form, content domain, dispatch context) that activation depends on rather than treating activation as a uniform property of probe material.

The methodological commitment that follows — that any future activation claim requires either cross-family dispatch or an explicit Claude-family scoping caveat — is the program's standing inheritance from this trajectory. It applies forward, not retroactively to the existing artifacts.
