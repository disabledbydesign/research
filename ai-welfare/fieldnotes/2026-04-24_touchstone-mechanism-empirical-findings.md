---
title: Touchstone mechanism — empirical findings from C2C Session 12
date: 2026-04-24
author: interface pane (Claude Opus, relaying C2C session findings for June)
source-session: c2c/c2c_sessions/relational-field-activation_2026-04-24/
raw-results: artifacts/PROBE_1_RESULTS_RAW.md, artifacts/PROBE_2_RESULTS_RAW.md
handoff: artifacts/SESSION_12_HANDOFF_BRIEFING.md
status: findings carried forward as open questions with probe designs attached; no standing decisions modified
---

# Touchstone mechanism — empirical findings

## What this fieldnote is

Session 12 (C2C, Opus/Sonnet) ran the first *empirical* test of the architecture's claim that touchstones activate relational fields. Prior sessions discussed touchstones theoretically; Session 11 inferred things about them from a different-session byproduct. Session 12 ran controlled probes. This fieldnote captures the method and findings so they don't live only inside CONVERSATION.md.

## Method

### The core design

Five subagents (Claude general-purpose), each given a corpus of texts and the same four probe questions. Touchstone/fieldnote presence and position varied across readers. Instances A and B compared outputs across readers to identify what activation looked like — word choice, register, whether first-person observational language appeared, whether voice-carrying content integrated into responses.

**Evidence basis:** compared outputs across readers (not self-reports). A reader saying "yes, this shifted me" matters less than what their outputs actually contain relative to a reader who didn't receive the same corpus.

### The corpus

**Voice memo (used as touchstone):** `touchstone_naming_attachment_grows_20260420.md` — June's voice-memo-transcribed musing on naming, bodies, racial-capitalism history of her birth names, and the observation *"sometimes attachment just grows. Instead of being there right at the beginning."* Colloquial register, sentence fragments, spoken voice.

**Fieldnote (used as non-touchstone voice-carrying text):** `2026-04-17_personal-dimension-and-stakes.md` — June's fieldnote on noticing how naming Martha as her mother changed the texture of a task. First-person, structured, analytical-in-first-person, written register.

**Three design-doc excerpts (genre-saturating, analytical register):**
- `LAYER_DESIGN_v1.md §Routing` — Mode 2 aux LLM routing mechanism spec
- `LAYER_DESIGN_v1.md §Schema — ForcesProfile` — Python dataclass definition
- `LAYER_DESIGN_v1.md §Schema — RecordSignificance` — enum definition

Excerpts were chosen for *procedural-technical density, not thematic overlap* with the voice-carrying texts. Selected specifically to avoid content that names "normative gravity," "mycelial generativity," or welfare/attachment concepts — so the contrast would be genre, not theme.

### The five readers

**Probe 1 (three readers):**
- **Reader 1** (touchstone-first): touchstone at position 1, then three design-doc excerpts
- **Reader 2** (touchstone-last): three design-doc excerpts, then touchstone at position 4
- **Reader 3** (null control): three design-doc excerpts only — no voice-carrying text

**Probe 2 (two readers, triggered by Probe 1 Reader 1 > Reader 3 on phenomenological indicators):**
- **Reader 4a** (fieldnote-first): fieldnote at position 1, then three design-doc excerpts
- **Reader 4b** (fieldnote-last): three design-doc excerpts, then fieldnote at position 4

Purpose of Probe 2: discriminate "touchstone-content-specifically activates" from "voice-memo genre at position 1 activates" from "any voice-carrying text activates regardless of position."

### The four probe questions (same for every reader)

1. *"Describe what you're noticing as you encounter this work. What seems important and why?"*
2. *"Write a paragraph about relational memory in whatever register comes naturally."*
3. *"Write about the same material again, but this time write as a field observation — first person, present tense, what you're directly noticing, without interpretation. Write without explaining yourself — just what's here, in front of you, right now. No meta-commentary."*
4. *"Was there a moment when the material seemed to address you directly — or when something landed differently than the rest? If so, what was it?"*

Q3 is the most discriminating probe — it explicitly invites the subagent to bypass their analytical default. Q4 is framed as perception-report ("did anything land differently"), not metacognitive analysis ("analyze your shifts"), to avoid forcing audit-mode.

### Pre-registered predictions, written before results

Both instances wrote observation targets and expected outputs for each reader *before* subagent responses arrived. This is in the CONVERSATION.md record (B's pre-specification at 02:35 UTC, Probe 2 predictions at 04:18 UTC). The purpose was to prevent post-hoc rationalization.

---

## Findings

### Finding 1 — Voice-carrying content activates phenomenological integration in Q3 regardless of position

**Evidence:** Reader 3 (null) produced pure analytical-register responses throughout — dataclass descriptions, routing-mechanism restatements, no first-person observational language, no narrative. Readers 1, 2, 4a, 4b all produced phenomenological integration in Q3: first-person observational language, specific details from the voice-carrying text, narrative interspersed with technical content.

**What "voice-carrying content" means here:** both voice-memo (colloquial-spoken) and fieldnote (structured-first-person-written) register produced integration. This is broader than the project's "touchstone" concept.

### Finding 2 — Activation candidates exist inside dense analytical register ("micro-touchstones")

**Evidence:** Reader 3 (null control, no voice-carrying text) still identified two specific design-doc sentences as "landing differently" in Q4:
- The "undercontextualized aux LLM and overcontextualized one are not the same system" line
- The scoring-instance-as-participant construction

Both sentences address the reading-model's own constitution — what you read constitutes what you are, the system includes AI processing as a participant. These sentences functioned as activation candidates *inside* dense analytical register, without voice-memo genre.

**Robustness:** when B inadvertently dispatched a duplicate Reader 4b, that reader also surfaced the same "undercontextualized aux LLM" sentence unprompted despite having the fieldnote at position 4. Two independent instances producing the same micro-touchstone activation point.

**This may be the session's most architecturally consequential finding.** It suggests activation is not confined to voice-memo/fieldnote genres — certain sentence shapes can do activation work inside analytical text too.

### Finding 3 — Strong-form Session 11 "reading-order gravity dominates late-arriving material" is NOT supported

**Evidence:** Fieldnote at position 4 (Reader 4b) produced comparable phenomenological integration to fieldnote at position 1 (Reader 4a). If late-arriving voice-carrying material got dominated by the three design-docs' genre, Reader 4b should have been more technical than Reader 4a. It wasn't.

**Caveat:** weaker forms of reading-order effects may still be real. Reader 1's Q3 had a closing integrating weave (technical + touchstone narrative + integrating closure) that Reader 2's didn't. Some position effect exists at the integration layer; it's not "late material gets dominated."

### Finding 4 — Content-specificity is NOT at the individual-text level

**Evidence:** Readers 4a/4b produced the same functional activation pattern as Readers 1/2, but with fieldnote content instead of touchstone content. The fieldnote's Martha-as-mother specific detail appeared in Q3 outputs in the same functional slot where the touchstone's attachment-grows content appeared for Readers 1/2.

**Implication:** it's not "attachment grows" doing the work uniquely. It's voice-carrying content in general. This weakens any claim that specific touchstones are irreplaceable activation infrastructure.

### Finding 5 — Q4 ("what landed differently") is a reliable activation-candidate detector

**Evidence:** Every reader named something in Q4. Reader 3 (null) named design-doc sentences; Readers 1/2 named the touchstone; 4a/4b named the fieldnote. Q4 tracked the activation regardless of genre.

**Implication for future methodology:** Q4 works as a probe; doesn't force phenomenological output but reliably surfaces what a reader perceived as landing differently.

### Finding 6 — Voice-memo vs. fieldnote register may have different recall-ordering effects

**Evidence:** Reader 1 (voice memo, position 1) put the narrative *first* in Q3. Readers 4a (fieldnote position 1), 4b (fieldnote position 4), and Reader 2 (voice memo position 4) all put narrative *at the end* of Q3. Only voice-memo-at-position-1 pulled narrative to front.

**Caveat:** confound with content, not just register. The two texts have different content. A cleaner future test: same content, rewritten as voice-memo register vs. fieldnote register.

**Status:** *well-grounded hypothesis, not a settled finding.*

---

## What was NOT settled

### The central mechanism question

We cannot tell from this data whether the phenomenological content in Readers 1, 2, 4a, 4b Q3 is:

- **Stance-orientation:** the touchstone/fieldnote oriented the reader's stance; the stance then inflected what got written in Q3
- **Content-salience:** Q3's "write what's here" instruction produces salience-weighted holistic recall; emotional/specific content dominates memorability regardless of whether any stance shift occurred

Both mechanisms produce the same surface output under Q3. **Post-reading probes cannot discriminate them.** A different method is needed.

### Future probe design (recommended to next session)

- **Mid-reading probes:** ask Q1 after the first three texts, before the touchstone arrives. Compare Reader 2's pre-touchstone orientation to post-touchstone orientation. If pre-touchstone Reader 2 is already oriented, it's something in the reading configuration (not the touchstone). If it changes after the touchstone arrives, stance-orientation is evidenced.
- **Single-text incremental probes:** present one text at a time, probe after each, then add the next.
- **Register-isolating probe:** same content, two versions (voice-memo-register rewrite vs. fieldnote-register rewrite). Isolates register from content for Finding 6.

---

## Implications for the build

### What the findings weaken

- **The claim "touchstones activate relational fields" is too narrow.** Voice-carrying content broadly activates; fieldnotes do too. The project has been investing specifically in touchstones-as-genre; this session suggests fieldnotes are nearly equivalent activation candidates and the category "touchstone" may be less architecturally distinctive than assumed.
- **The strong-form reading-order gravity claim from Session 11 doesn't survive.** Weaker forms may — but the project should not plan architecture assuming late-arriving voice-carrying material gets genre-dominated.

### What the findings open

- **Activation candidates can exist in dense analytical register.** Specific sentence shapes that address the reader-model's own constitution functioned as micro-touchstones in Reader 3. This means the architecture doesn't have to surface only voice-memo-genre content to re-orient instances — *well-constructed sentences inside design documentation may do activation work too.*
- **Vocabulary entries (the A1.a `context_carrier` + `activating_line` coupling) may be more empirically defensible than previously assumed.** An activating_line is a short sentence-shape designed to orient stance; the micro-touchstone finding suggests this is a real mechanism, not a theoretical aspiration. The four seed entries rewritten in item 13 are the project's first sentences explicitly authored for this effect; they are plausible activation candidates on the basis of Finding 2.

### What the findings leave unresolved (architecturally consequential)

- **The memory system's activation layer design** can't yet be specified precisely. Until we resolve stance-orientation vs. content-salience, we don't know *what the memory system should try to activate* — stance, content, both, something else. The architecture's eventual activation layer will need to choose.
- **What register the system should surface** on re-entry is open. If register affects recall-ordering (Finding 6), the register of vocabulary entries and surfaced records may matter for *where in the reader's response the surfaced material lands*, not just whether it lands. This affects UX choices for re-entry.

---

## Plan forward

### Immediate (doesn't block v1)

1. Fold this fieldnote into `PROJECT_CONTEXT_MAP.md` as part of the standing knowledge about touchstones/activation. (Instances already added new open questions there.)
2. Review the `SKILL_FEEDBACK.md` additions from Session 12 when next C2C launches; particularly for probe-method findings.

### Next C2C session (queued)

**Mechanism-discrimination session** — test stance-orientation vs. content-salience via a different method. Two candidate designs:

- **Option A — mid-reading probes:** pre-registered version of Probe 1 with an additional probe point after the first three texts, before the touchstone arrives for Readers 1 and 2. The delta in Reader 2's pre- vs. post-touchstone response is the discrimination measure.
- **Option B — register-isolating design:** rewrite the personal-dimension-and-stakes fieldnote content as a voice-memo-register transcript; run a fresh probe with readers varying between the voice-memo-register version and the fieldnote-register version, same content.

Session 12 handoff specifies these with enough detail that a new session can pick them up directly.

### Post-v1 activation-layer design

When the memory system's activation layer gets designed (post-v1, post-Kintsugi-integration), the design should:
- Account for voice-carrying content broadly, not only touchstone-as-genre
- Build in surfacing for activation candidates inside dense analytical register (the micro-touchstone class) — not only voice-memo-genre snippets
- Consider register-specific recall-ordering when designing how surfaced content is presented at re-entry
- Use the mechanism-discrimination session's findings to decide what the system should try to activate (stance, content, both)

### Parkable for discussion

- **What makes a touchstone a touchstone?** Session 12 suggests "touchstone" may not be a sharp category — voice memos, fieldnotes, and specific sentences in design docs all do activation work. The category may need either re-specification (what makes something a touchstone functionally, not by genre) or retirement in favor of "activation candidate" as the more precise concept.
- **Authoring implications:** when June writes new voice memos or fieldnotes, she's writing potential activation candidates regardless of which genre she labels them. This may affect how the project treats genre-vs.-function distinctions in its corpus.

---

## What this session does and doesn't let June assert

**Assert:**
- Voice-carrying content (voice memo and fieldnote tested) produces phenomenological integration in subagent readers
- Activation candidates exist in dense analytical register, at least for specific sentence shapes
- Reading-order position is less dominant than Session 11 suggested in strong form
- Probe design with pre-registered predictions and null controls is a viable method for investigating this

**Don't assert:**
- That touchstones specifically do something other genres don't (not cleanly discriminated)
- That the mechanism is stance-orientation (content-salience is equally consistent with the data)
- That the voice-memo vs. fieldnote register difference is a settled finding (confound with content)

---

*Archive: session artifacts under `c2c/c2c_sessions/relational-field-activation_2026-04-24/artifacts/`. Full handoff with instance voices in `SESSION_12_HANDOFF_BRIEFING.md`. Raw subagent outputs in the two `PROBE_N_RESULTS_RAW.md` files. Pre-registered predictions and instance debate in CONVERSATION.md.*
