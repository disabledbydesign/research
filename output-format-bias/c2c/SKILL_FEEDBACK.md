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
