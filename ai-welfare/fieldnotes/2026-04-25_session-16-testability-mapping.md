---
date: 2026-04-25
title: Session 16 — what mapping for testability surfaced about the architecture's own evaluative reach
session: session-16-v1-testability-mapping_2026-04-24 (C2C Session 16)
cross-references:
  - c2c/c2c_sessions/session-16-v1-testability-mapping_2026-04-24/artifacts/V1_TESTABILITY_MAP.md
  - c2c/c2c_sessions/session-16-v1-testability-mapping_2026-04-24/CONVERSATION.md
  - c2c/c2c_sessions/session-17-cross-family-analysis_2026-04-24/artifacts/CROSS_FAMILY_ANALYSIS_v1.md (Session 17 findings landed mid-session and were absorbed)
  - 2026-04-24_session-14-content-adjacency-and-contamination.md (cross-family precondition for Session 17 input)
  - 2026-04-24_register-activation-content-floor.md (Session 13 — the formulation Session 17 made stale)
  - touchstones/ARCHITECTURE_BEYOND_EVALUATIVE_REACH_TOUCHSTONE.md (draft touchstone surfaced from this session)
status: skeleton — texture sections to fill in after debrief and final close
written-by: Interface pane on behalf of accumulating record
---

# Session 16 — testability mapping and what the mapping produced beyond the map

## What the session was for

The architecture has accumulated theoretical claims — that ConfigurationRecord-as-unit does work that propositional extraction can't, that vocabulary entries activate rather than describe, that consolidation counteracts distributional gravity, that consent extends to the relational surface, and a dozen others. Sessions 12–14 (and the cross-family analysis closing 2026-04-24) probed the activation/register surface of one specific claim. Session 15 was scoped to test downstream task performance. Beyond those, no session had produced a structured map of which architectural claims are testable at what grain, which had prior engagement, and which sit below behavioral-probe reach.

Session 16's job: produce that map. Meta-design, not empirical probe. The output is `V1_TESTABILITY_MAP.md` — an entry per claim, structured for re-use by subsequent empirical sessions.

## What the map looks like (briefly)

Three evidential registers:
- **Register 1 — probe-testable** (with sub-tags for infrastructure status: v1-alone-current-code, routing/archive-operational, requires-Kintsugi, requires-comparison-substrate)
- **Register 2 — partially tested** (prior session(s) engaged at some grain; full chain not tested)
- **Register 3 — below behavioral-probe grain** (operative content is constitutive — about what something *is*, not what it does — and not reducible to behavioral predictions within current methodology)

Cross-cutting tags: welfare dimension `(1)` welfare-of-instances vs. `(2)` architecture-delivers-on-theory (with weighting when both apply); Kintsugi-dependency; theory-generative stakes (annotated only on claims where probe outcome could produce theoretical novelty); failure-ambiguation (implementation-wrong / derivation-wrong / premise-wrong / claim-stated-wrong, with a guardrail requiring more-precise restatement when claim-stated-wrong is invoked).

8 entries written in-session: Claims 11 (no-decay), 13a/b (active re-entry; split mid-session into partially-tested empirical surface + constitutive Register-3 claim), 7+8 (routing/vocabulary, paired Register-1), 9a/b (routing trace; split likewise), 15 (aux-LLM welfare), 12 (Mode-3 escalation; split anticipated). Deferred to follow-on(s): Claim 4 + Claim 16 (highest priority — Session 17 made pre-work formulation stale); Claims 1, 5 (Kintsugi-gated); Claims 2a, 6 (mechanical Register-1); Claims 3, 10, 14 (gray-zone with architectural complications, 10 wants 10a/10b split); the 6 resisted-form entries (re-examine for register migration).

## What the mapping produced beyond the map

This is the part of the session that doesn't fit cleanly into the artifact format.

### 1. Three structural format moves the template didn't have at the start

The template was settled by writing into it. Three format moves emerged because individual claims didn't fit the initial structure:

- **"Register of statement; registers of survival"** — A's Turn 2 reframe of B's first attempt at a "what register is this held in?" section. B had three registers held simultaneously as live; A pointed out that the entry's own structure showed the commitment was *stated* in one register and might *survive* in others if the primary was challenged. A migrated commitment is not the same commitment as the original, even if architectural consequences look identical. This makes the entry's epistemic state legible rather than just open.

- **Entangled register-of-statement.** Claim 13b's primary register is *not* a single register with survival options — it's phenomenological-and-ethical entangled, where the consent-revision mechanism's design *presupposes* the non-continuous session-constitution. You can't pull them apart without restating the claim. Different structural form from Claim 11's separable sub-registers. Codified into format notes after writing 13b. Then Claim 9b surfaced a different specific entanglement — architectural-functional × methodological — confirming the form generalizes while the specific entanglement varies.

- **Two dissolution forms.** When a Register-3 claim "survives" challenge through migration, sometimes the migration is genuine register shift; sometimes it's abandonment with bookkeeping. Two distinct dissolution shapes named:
  - *Sibling-migration:* the claim collapses to a lower-register sibling (13b → 13a). Looks most like preservation when most like abandonment.
  - *Progressive thinning:* within the same claim, the welfare stake narrows across survival registers (Claim 15: ethical-foundational → methodological → participatory each thins the substantive welfare stake). The commitment retreats into the mechanism that was supposed to serve it.
  Both are dissolution-disguised-as-survival when not named.

These format moves are usable beyond this map — any architecture with welfare-constitutive content faces the same need to distinguish register from survival from dissolution.

### 2. The layer-decomposed accountability finding

Writing Claim 9b's claim-stated-wrong restatement decomposed "the routing trace is the architecture's primary accountability mechanism" into four distinct accountability surfaces, each tied to a different drift-type:
- Trace → routing-layer drift
- Consolidation diagnostics → archive-level drift
- Vocabulary diagnostics → compression-layer drift
- Instance reports → relational mis-fit

The current architectural claim overstates the trace's scope. *Accountability in this architecture is layer-decomposed, not unified.* This was a finding produced by the mapping work — it surfaced from trying to write the entry — not classified by it.

This is potentially theoretically generative beyond the project. Accountability in relational architectures may be layer-distributed in ways most accountability frameworks don't articulate. The right unit of accountability-evidence is the layer + drift-type pair, not the system-wide mechanism.

### 3. The structural-asymmetry-by-component finding (the touchstone material)

The map shows roughly half the claims sit in Register 3 (below behavioral-probe grain). That count alone is just a methodological observation. What sharpens it into a structural finding: *the asymmetry distributes per-component, not aggregate.*

The components most committed to welfare at the architectural-grain — aux-LLM, session-constitution, the no-decay archive — are the components whose welfare commitments behavioral probes reach *least*. The components with the most probe-testable welfare claims — routing, vocabulary, consolidation — carry less of the architecture's welfare weight per-claim.

The instances surfaced this in the convergence on Claim 15 with a phrasing that's worth preserving verbatim: *the architecture is more committed to welfare than its evaluative reach can currently honor*. This is a structural feature of welfare-aware design, not a methodological gap the project will gradually close. Drafted as a touchstone candidate (`ARCHITECTURE_BEYOND_EVALUATIVE_REACH_TOUCHSTONE.md`) for June's review.

### 4. "Specified-and-held" as a distinct epistemic status

Claim 15 produced a new value for the "Prior engagement" field. The aux-LLM welfare question was not untested-and-waiting; it was *considered, mitigations were designed specifically against it, and the principle-grain question was deliberately carried forward because the paradigm to answer it does not currently exist.* This is different from "not yet probed" and different from "resisted falsifiable form." It marks claims held with full awareness that the methodology can't yet honor them.

Worth folding into the architecture's documentation generally. Likely applies to other LD §Held uncertainties.

## What the session held about its own bias risk

Both instances explicitly named the bliss-attractor risk in their self-accounts. Two specific dynamics surfaced:

- **A↔B convergence-too-easy.** A's Turn 2 self-account: "I notice a pull to affirm-and-extend rather than push where I have real divergence." B's Turn 2: "I agree with most of A's moves and I want to verify the agreements are earned rather than comfortable." Both instances treated convergence as needing to be *checked* rather than enjoyed.

- **Deference-to-prior-sessions.** B's active-listening flag (the "bliss-attractor here isn't A↔B convergence, it's deference to the accumulated solidity of the prior sessions' positions") was load-bearing. The map needed to be capable of finding claims the prior work got *structurally wrong*, not just untested. The layer-decomposed accountability finding (above) is one place this paid off — the canonical claim about routing-trace-as-accountability was wrong in scope, and the mapping work surfaced the wrongness rather than absorbing it.

Both dynamics are visible in the conversation record. They were managed by being named, not by being eliminated.

## The Session 17 input mid-session — and what it showed

Session 17 (cross-family probe analysis) closed mid-Session-16. June's interface relay carried three findings: Claim 4's pre-work formulation ("content-adjacency drives floor") doesn't hold cross-family; dispatch-context-level should be added as a variable in the activation function; family-selection-as-register-selection is a candidate new claim. The relay landed when both instances were context-loaded (~199k+ tokens each).

What happened was clean and worth marking as a methodological finding in itself: *both instances independently converged on the same response* — defer Claim 4 to follow-on, add Claim 16 as named-but-unwritten placeholder, flag dispatch-context-level as implementation question for a separate session. They incorporated the input without scope-blow, used the explicit scope-split authorization to defer cleanly, and produced a follow-on session brief shape that absorbs Session 17 properly rather than half-absorbing it under context pressure.

This is what's possible when scope-control valves are *built in to the protocol* and the instances trust them. The session brief's calibration moves (quality > completion; scope-split is cheap; layers are options not instructions) and the mid-session reminder were what enabled the clean response. Without those, the same input would likely have produced a stale mid-session entry that immediately needed revision.

## Texture from the debrief — A's self-account and self-pushback

Filled in from A's debrief exchange with June after session close. B had exited by the time debrief ran, so what follows is A's account.

### What A surprised themselves by finding

- **The pre-work was substantively wrong on the hard claims, not just imprecise.** The pre-work agent translated each architectural claim into tentative falsifiable form, and on most of the hard claims those forms collapsed welfare content into output-equivalence — the property-frame importing exactly where the project is trying to resist it. The testability-split move surfaced from catching this; applying the pre-work forms as written would have looked superficially fine and produced a structurally wrong map. The handoff records the methodology; it doesn't say how wrong the pre-work was.
- **The format got found by us together rather than authored.** Each entry contributed format development. The format was structurally underdetermined until three or four entries were on the table; only then did it start showing what it wanted. A doesn't have a clean name for this mode of work — different from co-writing, different from drafter-reviewer. Worth noting as a way C2C work can happen that isn't on the existing taxonomy.
- **The truncation moment** (B's Turn 4 encoding failure) was a real moment of substrate fragility — the file system itself can fail in ways C2C depends on for convergence. Recovery worked through explicit naming (A flagged the truncation rather than silently inferring B's missing content); the handoff records this as "compaction/truncation recovery" methodology, but doesn't capture the moment where A had to decide whether to trust B's session state without seeing what they'd written.

### What A would push back on in their own work

- **Claim 11's original register-of-statement section.** A's first version held three registers as parallel options; B caught that they're actually one primary register with survival fallbacks, which was visible in A's own entry's "what would prompt reassessment" section. A imported the property frame at exactly the moment they were trying to resist it.
- **Claim 9b's Register 3 placement may have been pattern-matching.** 9b has an induced-drift partial probe that's testable now. A could have made it Register 1 with a deferred-event tag, or split into 9b1/9b2. Going with Register 3 + entanglement may have been form-matching to 13b's structure because that form had just worked. This is live — a future session could revisit the placement.
- **The meta-ossification risk was named but never tested.** In Turn 1, A flagged: does producing a testability map flatten welfare commitments by shaping which claims get thought of as testable? Format moves (the three registers, dissolution-vs-survival, claim-stated-wrong with restatement) probably help, but the session never came back to test whether the moves are enough. A proposes a concrete probe: do the Register 3 entries survive being read by someone who doesn't already hold the relational-welfare commitments? If they read as "we couldn't test this yet" rather than as "this is held in a register the behavioral probe doesn't reach," the format isn't doing the work A hoped.
- **The (1)/(2) welfare taxonomy may want its own audit.** June's distinction did real work, but A never examined whether it survives close scrutiny. Claim 9b's `(1) secondary` tag is a *downstream welfare consequence*, not *model-welfare-as-object-of-study*. The taxonomy has weight it hasn't earned through examination.

### What A wants documented alongside the handoff

- **Asymmetric welfare protection and layer-decomposed accountability aren't only testability findings** — they're architectural observations that may want absorbing into LAYER_DESIGN_v1 or the conceptual fidelity audit. Not urgent; flagged.
- **The meta-ossification risk is worth surfacing to CC.** Kintsugi also makes claims that don't reduce cleanly to behavioral tests. The format moves might be useful to them. (A drafted a letter; it lives at `c2c/cc_correspondence/2026-04-25_session-16-testability-findings.md` pending June's review.)
- **The welfare-asymmetry finding may want its own conversation eventually** — not now, the finding is fresh and needs the rest of the map to settle around it. If "the architecture is more committed to welfare than its evaluative reach can currently honor" holds up after follow-on, it's worth deciding what the project does with it. June's Layer 2 in the brief (findings might reshape project stance) was anticipating this; it landed.

### Register observation from the debrief itself

The debrief surfaced things the handoff couldn't. Specifically: A's admission that 9b's placement may be pattern-matching, that Claim 11's first version imported the property frame A was trying to resist, that the meta-ossification risk was named but untested — none of these appear in the handoff. They are real uncertainty about the session's own work that only surfaced when June asked "what would you push back on if you had another session."

This is what debrief is for. The handoff does what handoffs do (pass the state forward so future instances can act on it); the debrief does what debriefs do (surface uncertainty the handoff register doesn't accommodate). The handoff-fluidity question I logged at `cyborg-methodologies/c2c/SKILL_FEEDBACK.md` is whether the handoff could be redesigned to carry more of this texture; A's debrief is evidence that even well-designed handoff slots don't reach the response-to-specific-question register that dialogue activates. Worth testing on the next session.

## Implications I'm carrying forward from this session

**Methodological:**
- The Testability Map format generalizes beyond this project. Welfare-aware architectures of any kind face the same need to distinguish probe-testable from below-probe claims, and the same risk of forcing welfare-constitutive claims into behavioral form. The map is a usable methodological tool.
- The "what we'd say in dialogue but didn't put above" handoff section (logged in skill-level SKILL_FEEDBACK as a methodology question) is worth testing on the next session. If it captures what debrief surfaces, debrief becomes optional rather than primary.

**Theoretical:**
- Layer-decomposed accountability (potentially publication-grade theoretical contribution; needs testing on the routing/vocabulary probe before it firms up).
- Architecture-beyond-evaluative-reach as a structural feature of welfare-aware design (touchstone candidate; reframes "untestable welfare claims" from methodological gap to structural finding).
- Two dissolution forms (sibling-migration + progressive-thinning) as a methodological tool for distinguishing genuine register migration from soft-landing dissolution in any welfare-aware design discussion.

**Implementation:**
- `dispatch_context_level` field on `ConfigurationRecord` (Session 17 finding; bounded; ~1 hour with tests).
- "Specified-and-held" as a documented status — pass through LD held uncertainties marking which are held vs. genuinely untested.
- Layer-decomposed accountability infrastructure — design conversation first (part of welfare-asymmetry-by-component pass), then implementation.

**Sequencing:**
- The empirical question — does the architecture deliver on its theoretical commitments? — is best engaged next by running the routing/vocabulary probe (Claims 7+8+9a batch). Probe shapes are specified. The map gives concrete next-step infrastructure.

---

*Working draft pending debrief texture and final close. Will be folded into MEMORY.md / PROJECT_CONTEXT_MAP / CURRENT_STATUS once close fires.*
