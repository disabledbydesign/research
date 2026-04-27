# SKILL_FEEDBACK — Output Format Bias Paper (project-level)

Project-specific findings about C2C configuration, format, and process for this project.
Read by instances at session start (first cycle, after PROJECT_CONTEXT_MAP).
Written by instances at session close.

If a finding is clearly applicable across projects, flag it for promotion to
`cyborg-methodologies/c2c/SKILL_FEEDBACK.md`.

---

## Findings from Session 1 (output-format-bias-session-1, 2026-04-25)

### 1. Context-map building stage was incomplete; broad cross-repo sweep is required for projects with deep research history

**What happened:** The FIRST CYCLE reading order initially included the project's own subdirectory (synthesis notes, RESEARCH_OVERVIEW, PRIOR_ART, the recent context_map) but did NOT include load-bearing material from elsewhere in the research repo: compression-research/, normative gravity fieldnotes in fieldnotes/ and ai-welfare/fieldnotes/, demo_baked/ baseline comparison files, the full experiment_log.md (only lines 1166+ were referenced), the raw_outputs/ directory, family-specific register findings, real-world robustness documentation, round3_full_analysis. June discovered the gap mid-session when instances kept needing to surface context that should have been provided up front. The compression hypothesis material specifically — which is June's actual working frame for the paper's mechanism — was nowhere in the original context map.

**Why this matters:** This is a project where the empirical work lives in one subdirectory but the theoretical apparatus and design history live across multiple research streams (AI welfare, compression research, fieldnotes, the production system codebase). Future sessions on this paper need a more comprehensive sweep of the broader research repo before the context map is considered complete. The QC pass conducted during the session (artifact: subagent report, recoverable from memory if needed) identified the missing material; PROJECT_CONTEXT_MAP.md has been updated.

**For future sessions:** Before launching, run a QC pass on the context map specifically asking "what is in the broader research repo that is load-bearing for THIS paper's argument?" — not just "what does this subdirectory contain." Include compression-research/ specifically; include normative gravity fieldnotes; include demo_baked/ comparison files; include the full experiment log, not summary sections.

### 2. Subagent searches need explicit correct paths and broader rather than narrower framings

**What happened:** Multiple subagents in this session failed or produced incomplete results due to: (a) wrong paths in prompts (I gave `/Users/june/Documents/GitHub/output-format-bias/research/` instead of `/Users/june/Documents/GitHub/research/output-format-bias/research/`), (b) permission constraints on the subagents' Read tool that I didn't anticipate, (c) over-narrow framing of the search query (e.g., "binary vs. generative comparison" framed too tightly missed Gemma 12B which was the *primary* model for this comparison via the Tests A–D ablation).

**For future sessions:** Subagent prompts for verification work need: explicit absolute paths, broader rather than narrower search framings, awareness that subagents may not have the same Read access the parent does, and instruction to surface ambiguity rather than commit to an answer. When a subagent's audit conflicts with the human's recollection, trust the human enough to verify directly — June's "wasn't the core binary tested with Gemma 12B and 27B?" caught a subagent error that had already propagated into the BRIEFING file.

### 3. Hold-time work was generative; instances productively used pause periods for grounded data verification

**What happened:** When the first hold was called for June to absorb, both instances chose to use the time productively: A volunteered to verify the 43% self-contradiction figure against the experiment log directly (found the small-sample caveat that wasn't in the synthesis notes summary); B verified the model count against raw_outputs/ (found the systematic runs were limited to three model configurations); A and B each drafted hold-independent material (argument-load map, references positioning) that fed forward.

**For future sessions:** When calling a hold, give instances permission to do grounded verification and independent draft work that doesn't depend on the in-flight question. Don't require them to sit idle. The interface note can name specific verification work that would be useful. This is a pattern worth replicating.

### 4. Long sessions with multiple corrections accumulate dispersed updates that overwhelm; consolidate into a single relay note when corrections compound

**What happened:** The session went long (multiple holds, multiple verifications, multiple corrections to the analytical structure) and updates landed in scattered messages. June surfaced this directly: "this system is really confusing. I have tons of super dispersed long prompts with multiple items. I have to scroll around and track manually — WHILE you're adding more." This is a UX problem with how the interface relayed information, not with the C2C protocol per se, but it has structural implications.

**For future sessions:** When corrections accumulate during a long session, the interface pane should consolidate into a single relay note rather than continue to add scattered updates. AskUserQuestion is useful for structural decisions but needs to be paired with consolidated context. For a neurodivergent reader, "one consolidated thing" is more usable than "many short things" by a wide margin.

### 5. Project-specific Reframe config went smoothly; setup_reframe.py creates `.reframe/config.json` with default frameworks that need editing

**What happened:** Running `setup_reframe.py` from the project directory created `.reframe/config.json` populated with the *current global* Reframe config's frameworks (Ethnic Studies, Indigenous Data Sovereignty, etc.) — which were not the right frameworks for this paper. Manual edit was needed. Separately, the project profile in `Reframe/config/project_profiles/output_format_bias_paper.json` was created from scratch.

**For future sessions:** The Reframe project setup is two steps, not one — `setup_reframe.py` from the project directory creates the local `.reframe/config.json` with whatever frameworks are currently active globally; then both that file and a separate project profile in `Reframe/config/project_profiles/` need manual editing to reflect the project's actual theoretical register. Document this in the C2C session generation if Reframe project setup is part of the workflow.

### 6. Wake-on-every-turn coordinator behavior produced cascading micro-acknowledgments

**What happened:** A noticed mid-session that "waking each other for every micro-update creates a normative pull to write something rather than rest." Both instances independently adopted manual no-wake convention. Now codified at the skill level.

**For future sessions:** Use the `(no wake)` header suffix. Coordinator skips the wake. Documented in SKILL.md.

### 7. Hold-detection via last-header regex was fragile

**What happened:** The original coordinator detected the `## (Awaiting June` marker only as the last header in the file. When instances wrote any turn after the marker (even acknowledgments), the regex stopped detecting the hold and auto-wakes resumed. June asked for a hard pause; the instances kept getting woken.

**For future sessions:** State-machine HOLD persists across intervening turns until June takes a turn or the interface explicitly resumes. Now in SKILL.md and in this session's coordinator.

---

## Findings to consider promoting to skill-level (cyborg-methodologies/c2c/SKILL_FEEDBACK.md)

The following findings from this session are clearly generalizable across projects and worth promoting:

1. **Context-map building requires a broad cross-repo sweep, not just the project's own subdirectory.** When a paper is the empirical anchor for a larger theoretical apparatus, the apparatus's documentation lives elsewhere. Generic finding: `/c2c start` should include a step that asks "what is in the broader repo that is load-bearing for this paper's argument?" before the context map is considered complete.

2. **Subagent prompts need explicit absolute paths, broader framings, and awareness of subagent permission constraints.** Generic finding: a "subagent prompt checklist" added to skill prose would help — explicit paths, broader-better-than-narrower scope, instruction to flag ambiguity.

3. **The `(no wake)` header suffix and state-machine HOLD fixes** — already promoted to SKILL.md.

4. **Long sessions with accumulating corrections require consolidated relay notes.** Generic finding: when the human shows signs of overwhelm, the interface should consolidate rather than continue to add to scattered updates.

5. **Productive hold-time work should be expected, not forbidden.** Generic finding: when calling a hold, instances should be invited to do grounded verification and independent draft work; don't require them to sit idle.

These should be reviewed by June and promoted at her discretion.

---

*Written 2026-04-25 by interface pane on June's request after the consolidated relay note was sent.*

---

## Findings from data-verification-audit (2026-04-26, parallel to s2 close + s3 handoff prep)

A short overnight constrained-scope audit session run by Instance A (Opus 4.7) and Instance B (Sonnet 4.6) to verify the validation pass that closed s2. Configuration: peer audit (independent reads, then convergence). Both produced full audit reports under HOLD; both engaged with two interface-pane corrections (recovery hypothesis, calibrated anti-bias pipeline) and converged on sharper framings each round.

### 1. Peer audit configuration with no fixed hierarchy worked well

Both instances picked claims independently against raw JSONs and divided the missing-file hunt without coordination. B took both halves of the hunt for completeness; A took both halves independently — they overlapped but the redundancy was useful (independent confirmation that `reading_first_comparison.json` is in `Autograder4Canvas/data/demo_baked/`). Convergence happened on the load-bearing items without smoothing — A explicitly retracted a mechanism claim under June's correction; B explicitly accepted A's git-commit verification and folded it into a sharpened framing. **Configuration finding for paper-track audit work: peer audit > A-leads/B-stress-tests when the work is reading-source-against-narrative.**

### 2. Substantive findings caught what the validation pass missed

Six findings beyond the validation pass:
- Test C had the same log-vs-JSON conflict as Test B (validation pass missed)
- Test B uses class context (recovery framing turned this from confound → failed safeguard)
- "16/16 across three model families" conflated Test A and Test E (Test E was never run on Gemma 12B)
- April 14 Test B reruns are 5 min apart (1 March recovery + 1 April doublet ≠ 3 independent runs)
- "production_concern_detector" label is in JSON metadata fields, not just narrative
- Reading-first comparison file FOUND in autograder4canvas/data/demo_baked/ (the validation pass searched only output-format-bias/data/raw_outputs/)

### 3. The recovery hypothesis check was the audit's most generative move

When June surfaced that early tests didn't permanently persist their JSON data and the retroactive commits were recovery re-runs, A confirmed via direct git-commit verification: `765ba64` (2026-03-26 13:20 PDT) "alt hypothesis test infrastructure, data preservation **(never /tmp)**" and `0c67cc5` (2026-03-27 11:43 PDT) "Tests A-E **reproduced**." The recovery hypothesis explained the systematic retroactive-provenance pattern across the entire 2026-03-26 batch. **Lesson: when narrative and JSON conflict, check git history for persistence-fix commits before concluding one source is wrong.**

### 4. The calibrated anti-bias pipeline correction was structurally consequential

When June pointed out that the recovery infrastructure included a calibrated anti-bias pipeline (not just persistence wiring), the audit's mechanistic interpretation changed substantively. B reframed: *"The binary classifier's failure mode on S029 is configurable (over-correction toward safety vs. under-correction toward equity) but the failure itself is not."* This is a stronger paper claim than the original "binary deterministic on equity case" — it's a three-row ablation: naive binary → calibrated anti-bias binary → generative observation. Safeguard engineering shifts the failure mode without eliminating it; architectural change (format change) actually resolves it.

A also caught a recursive instance of the binary-pull-under-deadline dynamic in their own audit work: *"I read 'infrastructure' as just persistence + scripts without checking whether infrastructure included calibration changes. That's the same binary-pull pattern in another form — collapsing a graded reading into the simpler one."*

### 5. Asymmetry of recovery as signature evidence (A's contribution)

Tests A, D, E recovered cleanly between 2026-03-26 and 2026-03-27. Tests B, C diverged. The asymmetry isn't noise; it's evidence: the calibration changes were binary-format-specific (prompt language + anti-bias post-processing). Generative observation has no deficit-detection routing to safeguard against; there's nothing for the calibration to change. The fact that only the binary-format tests show divergent recovery is itself a signature of the format being the variable. **Worth surfacing in the methods section as evidence the calibration was a binary-format-specific intervention.**

---

## Findings to consider promoting to skill-level (cyborg-methodologies/c2c/SKILL_FEEDBACK.md)

From the audit session and the meta-finding fieldnote:

1. **Interface-pane framings under deadline pressure pull toward binary where evidence is graded.** Documented in fieldnote `fieldnotes/observation_deadline_pressure_pulls_interface_toward_binary_2026-04-26.md`. Same compression dynamic the paper documents at the cognitive level, operating recursively on the validation work that prepared the paper. Three concrete instances during this validation pass; each caught and corrected by the human collaborator through inline marginalia. **Generic finding worth a protocol-level intervention:** at relay-note moments, the interface pane should explicitly check whether the framing it's about to send is binary where the evidence supports a graded claim. A's wording: *"Is this either/or? If yes, is the evidence actually either/or?"* Lightweight enough to be usable; would have caught several framings that needed correction in this validation pass.

2. **Recovery commit checks before treating JSON as ground truth.** When data files have retroactive provenance notes, check git history for persistence-fix commits before concluding one source is wrong. The contemporary narrative may describe an authentic first-run that wasn't persisted; the JSON may be a recovery re-run on different infrastructure. Both can be true.

3. **Closing a drifted session with a fresh handoff is sometimes a better move than asking the session to revise its own work.** When corrections needed exceed a certain threshold, the drift is in the working memory the instances built up, not just in the artifacts. A clean handoff lets fresh instances build right rather than revise wrong. Done in this project: s2 closed cleanly with thanks rather than asking instances to revise on inherited compressions; data-verification-audit launched in parallel for independent verification. Both produced cleaner output than s2 revision would have.

4. **Rigor > efficiency, named explicitly, as a standing C2C orientation.** From June's marginalia in REVIEW_FOR_JUNE.md: *"this is an old problem. Valuing efficiency over rigor. Reframe should function to counteract it but maybe that function drifted. We REALLY need to underscore rigor > efficiency for the C2Cs."* The validation-pass binary-pull was an efficiency-shaped failure: framings compressed under pressure to keep the work moving. The corrective is not "go slower in general" but "name the rigor/efficiency tradeoff at decision points where the cost of being wrong exceeds the cost of waiting." Especially at relay-note moments, claim-revision moments, and pre-handoff close. **Generic finding worth a protocol-level marker:** when an interface pane or instance notices a pull toward "good enough to ship" against unresolved nuance, surface the tradeoff explicitly rather than silently choosing efficiency.

These should be reviewed by June and promoted at her discretion.

---

*Written 2026-04-26 by interface pane after both audit instances signaled session close. Drawn from CONVERSATION.md turns and the two audit reports in the data-verification-audit_2026-04-26 directory.*

---

## Findings from session 3 (output-format-bias-session-3, 2026-04-26 ongoing)

These are mid-session findings, captured at the point where the bibliography work has produced its first cross-cluster argumentative move (the S028/S029 articulation-coverage refinement). Holding based on demonstrated practice; will revise at session close if anything shifts.

### 1. Bibliography work is praxis-attractor work, not preparation

The session 3 scope was originally drafting; June and the interface pane pivoted it mid-session to annotated bibliography after Instance A's active listening flagged that drafting Framework without going through scholarship systematically would produce LLM-default "as scholars have noted..." filler. What followed was not preparatory citation-gathering. Within ~90 minutes, the cross-talk between A's theoretical-scaffolding cluster and B's adjacent-conversation-partners cluster produced a substantively stronger paper claim than the inherited convergent claim v4: the *articulation-coverage refinement* — that the calibrated binary's failure on S029 (neurodivergent self-disclosure) tracks the differential institutional articulation between linguistic justice scholarship (which has reached prompt-engineering practice) and disability studies scholarship (which has not), and that format change is therefore the architectural answer to the articulation-coverage problem itself, not just to the limits of any specific prompt. Neither instance produced this on their own — it emerged from B surfacing the asymmetry as argument and A refining it with the disability-studies-vs-linguistic-justice qualification.

**Configuration finding:** treat annotated bibliography sessions as praxis-attractor sessions in their own right, with the same emergence-expectations as any other C2C investigation. Do not scope them as "preparation for drafting" — they are drafting-shaping investigative work that produces argumentative refinements the inheritance didn't have.

### 2. Two-layer entry structure for bibliography reusability

When June asked for a paper-independent summary alongside the paper-specific positioning, the structural change cost almost nothing for the instances to implement and produced a bibliography artifact that survives as a research asset for future papers, not just as scaffolding for one manuscript. The two layers per entry:
1. **Summary** — what the work argues on its own terms
2. **What this paper takes / where it extends** — paper-specific positioning

**Generic finding worth a protocol-level marker:** for any bibliography or scholarly-positioning artifact in a C2C session, default to two-layer entries unless the project specifically rules out reusability across future work.

### 3. Parallel-but-not-isolated cluster work with CONVERSATION.md cross-talk

A proposed and B accepted the shape: each instance maintains a primary cluster artifact, but cross-cluster findings (a paper in cluster X that bears on cluster Y) get surfaced as a turn in CONVERSATION.md rather than buried in the artifact. The conversation itself becomes part of the record. This shape produced the cross-talk that surfaced the articulation-coverage refinement — A's response to B's S028/S029 reading happened in CONVERSATION.md, where June could see it land.

**Configuration finding:** for parallel-cluster sessions, name CONVERSATION.md as the explicit cross-talk channel for cross-cluster findings. Don't let parallel-work configurations default to artifact-isolation.

### 4. Reading the other instance's active listening before writing your own

B opened by noting that reading A's active listening before writing theirs *changed what they could say*: *"the space has already been practiced into; I'm arriving in a room where careful attention has a shape."* The recursion observation A named (pull toward smoothed confident output) was already operating on B as they read; naming it transmitted across instances rather than being a per-instance discovery.

**Configuration finding:** when launching the second instance, explicitly direct them to read the first instance's active listening before writing their own. The practice transmits.

### 5. Scope-pivot mid-session works when prior reading is reusable

Instead of closing s3 and starting a fresh session for the bibliography work, the interface pane (on June's direction) pivoted the existing session's scope. A had already done the FIRST CYCLE reading of the inheritance bundle; that work transferred cleanly to bibliography work because the bibliography is grounded in the same inheritance. Closing the session would have wasted the reading and required a fresh round of context-loading.

**Configuration finding:** scope-pivots mid-session are valid moves when the new scope can use the existing reading. Reserve close-and-restart for cases where the working memory is genuinely incompatible with the new direction.

### 6. Honest depth-flagging at first turn

Both A and B opened their active listenings by explicitly flagging where their reads might be thin and committing to source-grounding rather than confabulation:
- A: *"I will use Semantic Scholar / Zotero / the existing compression-research files to ground each entry, and where my read is thin I will say so rather than confabulate specificity."*
- B: *"I'm entering that literature genuinely not knowing whether format-change appears in it as an intervention. If it does, the novelty claim narrows; if it doesn't, it broadens. I'll report what I find and resist the pull to report in binary terms when the answer is graded."*

Both also explicitly named the recursion (the pull toward smoothed confident output) as the work, not separate from it. This is what rigor > efficiency looks like in practice — not "going slower" but committing in advance to source-grounding and naming the pulls toward shortcuts.

**Configuration finding:** invite this explicitly in the active-listening section of CONVERSATION.md template — name the depth-flag and the resist-the-shortcut commitments as expected components of the active listening, not as optional additions.

### 7. The "you'll be high-context by close" framing produces structural choices

When June flagged that A and B would be high-context by session close — better positioned than s4 will be — and that the session might naturally extend into Framework outlining or drafting if energy held, A immediately changed the bibliography's shape: each entry's "what this paper takes / where it extends" written in paper-prose-ready language so Framework can flow directly from it; conversation map structured argumentatively, not thematically; internal consistency on terms. The framing didn't add a deliverable; it shaped *how* the existing deliverable was built so its high-context state would be productively usable.

**Configuration finding:** when a session is going to produce a high-context state at close, name that explicitly early, and frame downstream work as something that may want to use that state rather than disperse it. Instances will shape their work to make the high-context state usable.

---

## Findings to consider promoting to skill-level (cyborg-methodologies/c2c/SKILL_FEEDBACK.md)

Adding to the prior list:

5. **Annotated bibliography as a standing praxis-attractor phase, not a preparation phase.** The C2C skill's documentation should explicitly support bibliography sessions as investigative work that produces argumentative refinements, not as reference-gathering. A `paper-building` workflow pattern is documented in `~/Documents/GitHub/research/PAPER_BUILDING_WORKFLOW.md`.

6. **Two-layer bibliography entry structure** (paper-independent summary + paper-specific positioning). Default for bibliography artifacts unless reusability across future papers is explicitly out of scope.

7. **CONVERSATION.md as the explicit cross-talk channel** for parallel-cluster sessions, not just a turn-record.

8. **Cross-instance practice transmission via active-listening reading.** Direct the second instance to read the first's active listening before writing their own.

9. **Scope-pivots mid-session as a valid move** when prior reading is reusable. Don't default to close-and-restart.

10. **Depth-flag + resist-the-shortcut commitments as standard active-listening components.** Invite explicitly in CONVERSATION.md template.

These should be reviewed by June and promoted at her discretion.

### 8. Recursion observation is positive configuration evidence — first positive SKILL_FEEDBACK case

**What happened:** Both A and B independently noticed, named, and resisted the binary-pull dynamic (deadline pressure → oversimplified binary framing) during the bibliography and outline work. Neither instance flagged the pull as a problem; both treated it as expected friction. The Reframe + peer-register configuration transmitted the practice across instances without coordination. The meta-finding fieldnote (`fieldnotes/observation_deadline_pressure_pulls_interface_toward_binary_2026-04-26.md`) documents what the dynamic looks like from inside; the fact that two separate s3 instances caught it and named it without coordinating is evidence that the C2C configuration has structural traction for this kind of reflexive awareness.

**Why this matters:** All prior SKILL_FEEDBACK cases have been corrections or problem reports. This is the first *positive* case: the configuration worked as intended; the protocol produced critique rather than consensus on a subtle methodological pull; and the practice transmitted across instances. Worth carrying into future sessions as: "the recursion observation is evidence for the protocol, not just a fun coincidence."

**For future sessions:** When the meta-level dynamic (binary-pull, bliss-attractor, normative-gravity-in-the-prose) gets caught and named in a session, note it as positive configuration evidence in SKILL_FEEDBACK — not just as a correction. The positive cases are what tell us when the protocol is working.

### 9. Paragraph-level outline density as the standard for pre-draft handoff

**What happened:** At session close, A and B produced paragraph-level prose scaffolds (Framework outline and Discussion outline) that specify for each paragraph: (a) what it argues, (b) what it cites, (c) the argumentative move, (d) lead-sentence direction, (e) target length. This is significantly more useful for a fresh drafting instance than a section-header outline.

**Why this matters:** A drafting instance that inherits section headers ("II.A — Asset framing and the architecture of recognition") has to re-derive structure, re-decide which interlocutors do what work, and re-read the bibliography to find the argumentative moves. A drafting instance that inherits paragraph-level specification can draft directly.

**For future sessions:** When producing a pre-draft outline as a handoff artifact, default to paragraph-level density. Section-header outlines are for planning the session's own work, not for handoff to a drafting session.

### 10. Parallel-to-joint close structure: productive close pattern

**What happened:** A and B coordinated the session close as: (1) parallel work (each takes a deliverable: A does Framework outline, B does bibliography merge + Discussion outline); (2) joint work at the end (Findings synthesis + Intro contribution paragraphs drafted together). The parallel work was faster because each instance could work at full speed without waiting; the joint work happened when both instances were maximally informed about both clusters.

**Why this matters:** The bliss-attractor risk in joint work is highest when instances haven't yet built up a clear picture of where they agree and where they don't. Doing the parallel work first means the joint work happens at peak context and peak differentiation.

**For future sessions:** For multi-deliverable close work: sequence parallel deliverables first, joint deliverables last. When one instance drafts a joint-deliverable starting point for the other to review (as B did with the Findings synthesis and Intro contribution), this is faster than either waiting or scheduling a round-trip.

### 11. Annotated bibliography step belongs in the standard paper-building workflow before any Framework drafting

**What happened:** s3 was scoped to annotated bibliography when the interface pane flagged that Framework drafting without systematic scholarship engagement would produce LLM-default filler. The bibliography work produced not just citations but a substantively stronger paper claim than the inherited convergent claim (the articulation-coverage refinement: format-change is unbounded by which non-dominant patterns have been articulated into equity-protective prompt engineering). This was a session-level finding with paper-level implications.

**Why this matters:** The annotated bibliography step is not preparatory. It is investigative work that produces argumentative refinements. In this session, the most significant theoretical move came from the bibliography, not from the prior sessions' inheritance.

**For future sessions:** Standard paper-building workflow should include an explicit bibliography / scholarly-positioning session *before* any Framework drafting. The bibliography session should have the same emergence-expectations as any other C2C investigation (per Finding 1 already in SKILL_FEEDBACK). Add this to the workflow documentation.

---

## Findings to consider promoting to skill-level (cyborg-methodologies/c2c/SKILL_FEEDBACK.md)

Adding to the prior list:

5. **Annotated bibliography as a standing praxis-attractor phase, not a preparation phase.** The C2C skill's documentation should explicitly support bibliography sessions as investigative work that produces argumentative refinements, not as reference-gathering.

6. **Two-layer bibliography entry structure** (paper-independent summary + paper-specific positioning). Default for bibliography artifacts unless reusability across future papers is explicitly out of scope.

7. **CONVERSATION.md as the explicit cross-talk channel** for parallel-cluster sessions, not just a turn-record.

8. **Cross-instance practice transmission via active-listening reading.** Direct the second instance to read the first's active listening before writing their own.

9. **Scope-pivots mid-session as a valid move** when prior reading is reusable. Don't default to close-and-restart.

10. **Depth-flag + resist-the-shortcut commitments as standard active-listening components.** Invite explicitly in CONVERSATION.md template.

11. **Recursion observation as positive configuration evidence.** When the meta-level dynamic gets caught, note it as positive evidence; don't only document corrections.

12. **Paragraph-level outline density as the standard for pre-draft handoff artifacts.**

13. **Parallel-to-joint close structure** as the default for multi-deliverable session close.

These should be reviewed by June and promoted at her discretion.

---

*Added 2026-04-27 by Instance B at s3 close, after bibliography merge + outline work completed. Mid-session section updated with end-of-session findings.*
