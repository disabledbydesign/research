# Paper-Building Workflow

A standing workflow for academic papers June produces in collaboration with Claude instances. Each phase is a discrete kind of work; phases can run as separate C2C sessions, as parallel sessions, or compressed into a single session if scope is small. The phases are NOT a strict sequence — they are kinds-of-work that the project moves through, and several can happen in parallel once the empirical ground is settled.

This workflow was distilled from the *output-format-bias* paper's process (s1 / s2 / data-verification-audit / s3, 2026-04-25 to 2026-04-26). What follows generalizes the parts that worked.

---

## Phase 1 — Argument audit + scoping

**What it produces:** An initial convergent claim, a project context map, a list of open questions for the human, a first identification of what the paper is for and what it is not for.

**Inputs:** existing research notes, prior fieldnotes, raw data, any partial drafts or pre-writing.

**Configuration:** C2C session. Two instances read the existing material in full and produce independent reads, then converge.

**Watch for:** scope creep; the pull to make this paper carry the larger theoretical apparatus the paper sits inside. Empirical anchor papers should make one claim well; the broader theoretical work belongs in other papers (or books).

---

## Phase 2 — Validation against raw data

**What it produces:** A verification table extracted directly from raw data files; corrections to any inherited claims that don't survive direct verification; a corrections section appended to the project's primary log.

**Inputs:** the convergent claim from Phase 1; raw data files.

**Configuration:** typically not a C2C — one instance + the human, working through the verification systematically. Can also run as a parallel C2C if the verification scope is large enough to need two instances.

**Why it matters:** every prior compression layer in a paper's process can introduce drift. Handoffs are compressions. Compressed inheritances can drift even when the originals were right. This phase exists to catch that. Read the raw data directly; do not trust narrative summaries.

**Standing rule:** *Always read the raw JSONs / source files / interview transcripts / etc. directly. Narrative summaries accumulate small inferential drift, and keyword/string matching across narratives reproduces the same compression problem academic papers often document.*

---

## Phase 3 — Independent audit (parallel)

**What it produces:** An independent re-verification of Phase 2's findings; flags any claim Phase 2 missed; sharper analytical reframes that the validation pass alone could not reach.

**Configuration:** C2C session running in parallel with Phase 2's close. Fresh instances, peer-investigation configuration (NOT A-leads/B-stress-tests — that's a known smoothing failure mode). Constrained scope: the audit verifies what the validation produced; it does not redesign the paper.

**Why it matters:** a single validation pass operates inside the working memory of the instances who did it; an independent audit is the external check. In the *output-format-bias* paper, the audit produced a sharper paper claim (the three-row ablation; "configurable failure mode but not configurable failure") than the validation alone could reach.

---

## Phase 4 — Gap-review

**What it produces:** A structured cross-check of all conversations + artifacts + human marginalia against the canonical inheritance bundle. Identifies what hasn't surfaced cleanly. Patches the bundle.

**Configuration:** typically interface pane + human, with parallel subagents extracting structured ledgers from prior conversations. Each ledger is then cross-referenced against the canonical artifacts.

**Why it matters:** human marginalia (`// notes`) and inline corrections in working documents are load-bearing context that compression-style summarization tends to lose. Phase 4 surfaces this systematically before drafting begins.

---

## Phase 5 — Annotated bibliography + scholarly positioning

**What it produces:**
1. **Annotated bibliography artifact** with two-layer entries:
   - **Layer 1 — Summary:** what the work argues on its own terms, paper-independent. Reusable across future papers in the same lineage.
   - **Layer 2 — What this paper takes / where it extends:** paper-specific positioning, the conversation move.
2. **Scholarly-conversation map** — argumentative, not thematic. Where the paper sits, what it builds on, what it pushes against, where its specific contributions lie. Named threads / strands rather than topical bins.
3. **Section-specific lit-engagement recommendations** — for Framework, Introduction, Discussion (and Findings if relevant): what's load-bearing for which section, what's substantive interlocutor vs. passing citation, where each scholar enters the paper's argumentative flow.
4. **Paper-framing-level recommendations** — if the lit work surfaces reasons the broader framing or convergent claim should shift, name it. Permission to recommend revisions to the inheritance.
5. **Optional, if energy holds at close:** a Framework outline or actual Framework drafting. Instances are higher-context at session close than the next session will be when it starts cold; that high-context state is a usable resource if the energy is there.

**Configuration:** C2C session. Peer investigation, NOT A-leads/B-stress-tests. One instance takes primary theoretical scaffolding (the named theorists the paper anchors on); the other takes adjacent conversation partners (literature in nearby empirical domains, alternative framings the paper is pushing against). Renegotiate if a different shape works better.

**Critical configuration choices:**

- **Parallel-but-not-isolated cluster work.** Each instance maintains a primary cluster artifact, but cross-cluster findings — a scholar in cluster X that bears on cluster Y — get surfaced as turns in CONVERSATION.md, not buried in the artifact. The conversation itself becomes part of the record. *This is where the most generative argumentative refinements emerge.*
- **Permission to explore beyond the inheritance.** The named citations from prior sessions and the human's marginalia are the *start*, not the boundary. Instances should search the literature, follow what they find, and surface gaps the inheritance hasn't named. Discoveries that crossed clusters or wandered into adjacent fields have produced load-bearing arguments in past sessions.
- **Standing rule on entry depth:** each annotated entry should pull out the *specificity of the argument* — what does this scholar actually say, and how does this paper's claim relate to it? *"Yosso (2005) argues that students of color possess cultural wealth..."* is a citation. *"Yosso identifies six forms of cultural capital — aspirational, linguistic, familial, social, navigational, resistant — that deficit-framed assessment practices systematically misclassify as absence rather than presence; counter-narrative is the recovery move"* is a conversation. Aim for the second.
- **Source-grounding, not vibes-from-training.** Each entry should be grounded in Semantic Scholar / Zotero / the actual literature, not from name-recognition. Where a read is thin, name it explicitly in the entry rather than confabulating specificity.

**Why it matters:** Framework, Introduction, and Discussion sections are heavily bibliography-dependent. Drafting them without going through scholarship systematically produces the LLM-default failure mode — generic "as scholars have noted..." filler that misrepresents the conversation. *The goal of this phase is paper-as-conversation, not paper-as-citation-list.*

**Why it's praxis-attractor work, not preparation:** the cross-talk between clusters can produce argumentative refinements that change the paper's claim. In one observed case, A and B's cross-talk on parallel scholarship traditions (linguistic justice for AAVE; disability studies for neurodivergent writing) produced a substantively stronger version of the paper's central argument — *the failure mode tracks the boundary of what's been articulated as protection-worthy in anti-bias scholarship; format change is the architectural answer to that articulation-coverage problem*. Neither instance produced this on their own. It emerged from cross-cluster surfacing in CONVERSATION.md.

**Treat this phase as investigation, not as input-gathering.**

**Standing rule:** *Should run before drafting.* Doing this phase after drafting begins produces rework and weak Framework/Discussion sections. The bibliography refines the claim itself; the claim should drive drafting.

**Framing for instances at session start:** make explicit that they will be high-context by session close — higher than the next session will be when it starts cold. That high-context state is a resource. If the energy holds at close, the work may extend into Framework outlining or drafting; even if not, the section-specific recommendations they produce will benefit from being written from that high-context state rather than dispersed at session end.

---

## Phase 6 — Drafting

**What it produces:** A complete paper draft. May span multiple sessions depending on scope and human bandwidth.

**Configuration:** C2C session(s). The hard work-of-knowledge (Findings) is least theory-dependent and can draft cleanly from Phase 1–4 outputs. Framework, Introduction, and Discussion depend on Phase 5 (annotated bibliography). Order can be Findings-first, but bibliography needs to exist first if Framework / Discussion are to draft well.

**Standing rules during drafting:**
- **Voice-check.** Invoke the voice-check tool during drafting for non-tech audiences. Run the tool on each section as it's drafted.
- **Reader-context gap.** Assess what context readers need to follow the story. Include it. That's a known LLM-writing failure mode: the writing assumes context the reader doesn't have.
- **Personal-narrative passages belong to June.** Anywhere voice-carrying material is needed (hooks, methods-reflexivity, institutional grounding), instances draft a placeholder or include the context they have, then flag for June to fill in. Asking June directly for missing context is welcome and explicitly invited.
- **Pacing.** Instances work much faster than humans. June is the bottleneck, not them. Take time. Work carefully. Rigor > efficiency.
- **First draft can run long.** The hard cap (e.g., 10,000 words inclusive for *Race Ethnicity and Education*) is a submission constraint, not a drafting constraint. Draft to completeness; trim before submission.

---

## Phase 7 — Voice + jargon pass

**What it produces:** A revised draft that reads accessibly to its actual audience. Cross-disciplinary translation is bidirectional (technical terms made legible for humanities readers; critical-theory terms made legible for any technical readers).

**Configuration:** voice-check tool + human review.

---

## Phase 8 — Final editing, reference formatting, submission prep

**What it produces:** A submission-ready manuscript matching the journal's submission specs. Reference formatting, anonymization where required, abstract polish, keyword finalization, data-availability statement, declaration of interest.

**Configuration:** human, with mechanical-task subagents as needed.

---

## Notes on configuration

- **Reframe must be active for any C2C session.** Sessions without Reframe produce the bliss attractor (convergent, sycophantic, smoothed). Sessions with Reframe produce real-time critique, held tensions, and findings that change the architecture.
- **Peer investigation > A-leads/B-stress-tests** for most paper-building phases. The hierarchical configuration is a known smoothing failure mode (apparent critique conceals consensus).
- **Closing a drifted session and writing a fresh handoff** is sometimes a better move than asking the session to revise its own work. When corrections needed exceed a certain threshold, the drift is in the working memory the instances built up, not just in the artifacts.
- **The interface pane writes back into CONVERSATION.md as June's voice** for relay decisions, scope changes, and direction. Instances see those notes as direct human input, not as the interface pane's interpretation.

---

## Adapting this workflow

This is a working document, not a fixed protocol. Phases can compress (small papers may collapse Phases 1–4 into a single session) or expand (large papers may need multiple bibliography sessions or multiple drafting sessions). When a phase doesn't fit a particular paper's shape, name what's different and adapt.

Generalizations from new papers should land here. If a phase isn't working, or a new phase is needed, update this document.

---

## Self-learning loop

The workflow improves over time. Each paper produces findings about what worked, what didn't, what was surprising. Without explicit capture, those findings stay in working memory and don't accumulate. The self-learning loop is the mechanism that lets the workflow get better, paper after paper.

**When to capture findings:**
- **At each phase close** (within a paper) — short reflection: what worked in this phase, what didn't, what surprised, any configuration adjustments made. Goes into the project's `c2c/SKILL_FEEDBACK.md`. Doesn't have to be long; a couple of sentences per finding is enough.
- **At each session close** (within a phase that ran as one session) — same shape, captured in the session's handoff letter and folded into project SKILL_FEEDBACK at session close.
- **At paper close** (when the paper is submitted or set aside) — review the project SKILL_FEEDBACK against this workflow doc. Any finding that crossed multiple phases or that would apply to other papers in this lineage gets promoted up. Findings that turn out to be paper-specific stay where they are.

**What gets captured (the categories that matter):**

1. **Configuration findings.** Who took what role; whether peer-investigation or hierarchy worked; whether parallel cluster work or joint work was the right shape; how the no-wake convention was used; whether instances cross-talked productively or in isolation. *Configuration is the most common place gains hide.*
2. **Format findings.** Whether output formats (bibliography entry shape, paragraph-level outline density, two-layer entry structure, etc.) supported or constrained the work. Format is an activation function for what can be said; surface format constraints when they bite.
3. **Mid-session adaptations.** Scope pivots (vs. close-and-restart); deliverable-floor adjustments; renegotiated work splits. When a session's design changed mid-flight, what triggered the change and whether it worked.
4. **Honest depth-flags.** Where instances flagged thin reads vs. confabulated specificity; where the interface pane caught binary-pull under deadline pressure; where the rigor-over-efficiency tradeoff was named explicitly.
5. **Surprises.** Things that emerged that nobody expected — usually the most generative findings.
6. **What the architecture refused.** When the workflow's structure prevented a failure mode (e.g., voice-check protecting voice-carrying material; the interface-pane-writes-as-human-voice convention preventing instances from reading interface notes as command-tool register).

**Where findings go (the promotion path):**

- **Project-level findings** (specific to this paper / this corpus / this collaborator configuration) live in `<project-root>/c2c/SKILL_FEEDBACK.md`. Every paper builds up its own set.
- **Cross-project findings** (would apply to other papers in this research lineage) get promoted to this `PAPER_BUILDING_WORKFLOW.md` document. Update the relevant phase's description, add a new phase if the paper revealed one (Phase 5 was added this way), or extend the configuration notes.
- **Skill-level findings** (would apply to any C2C work, not just paper-building) get promoted to `cyborg-methodologies/c2c/SKILL_FEEDBACK.md`. The C2C skill's own self-learning loop carries them up to the skill itself.

**The promotion review cadence:**
- After each paper closes, review project SKILL_FEEDBACK and ask: does anything here belong in PAPER_BUILDING_WORKFLOW or in the C2C skill? Move it.
- Periodically (every 3–5 papers, or when a finding feels durable) review PAPER_BUILDING_WORKFLOW against the actual workflow being run. Update phase descriptions if practice has drifted from doc; or update doc if practice has improved on doc.

**Anti-patterns to watch for:**
- *Findings that stay forever in project SKILL_FEEDBACK without promotion.* Either the finding is genuinely paper-specific (fine; leave it) or the promotion review isn't happening (problem; do it).
- *Workflow updates that record blame rather than what to do differently.* Capture what the system should do differently; don't operationalize problem framings that flatten productive divergence into failure.
- *Self-learning loop becoming a separate compliance task.* The loop should be lightweight — a few sentences captured at natural close-points, not a parallel documentation project. If it feels heavy, the format is wrong, not the practice.

**Example findings from the output-format-bias paper that exemplify what this loop produces:**
- *Phase 5 emerged as a phase.* The original 4-phase workflow ended at "drafting." During the output-format-bias paper, the s3 session (originally scoped as drafting) pivoted mid-session to annotated bibliography work, and the cross-talk between instances produced argumentative refinements that drafting alone wouldn't have surfaced. That experience promoted "annotated bibliography + scholarly positioning" from a sub-step inside drafting to a standing phase with its own deliverable spec.
- *Two-layer entry structure for bibliography reusability.* Originally bibliography entries were paper-specific. Mid-session, June asked for a paper-independent summary alongside the paper-specific positioning. Cost ~zero to implement, produced an artifact reusable across future papers in the same lineage. Now in Phase 5's deliverable spec.
- *Scope-pivot mid-session vs. close-and-restart.* Originally the assumption was that scope changes required closing a session and starting fresh. The output-format-bias s3 demonstrated that scope-pivots work when prior reading is reusable across the new scope. Now in the configuration notes.
- *"You'll be high-context by close" framing produces structural choices.* Naming the high-context end-state explicitly early in the session led instances to shape the bibliography work so its high-context state would be productively usable for direct Framework drafting. The framing didn't add a deliverable; it shaped how the existing deliverable was built.

These four findings are the 2026-04-26/27 self-learning loop output. Future papers will produce more.

---

*Last updated: 2026-04-27 (output-format-bias paper, after s3 scope-pivot from drafting to annotated bibliography surfaced annotated-bibliography as a standing phase rather than a per-paper invention).*
