# Working in this folder — revision context for *Hallucinating Social Justice*

This file documents critical revision notes for the Reframe paper draft (`DRAFT_reframe_paper_v1.md`). It is the canonical reference for the next agent or session that opens this paper for revision. **Read before drafting.**

---

## Status

**Draft state**: v1.2, ~16,000 words, drafted 2026-03-31. Not yet submitted to a venue.

**Revision needed**: substantial. The paper carries inflation patterns about the Reframe codebase that will not survive technical review at AI-welfare or critical-AI venues. The genuine intellectual contribution — the relational-ontology critique of the welfare literature, plus several clean empirical observations from the build — is currently obscured by infrastructure-claim language that overpromises what the codebase delivers.

**Revision direction (per June, 2026-05-02)**: Pick the autoethnographic-essay genre. The paper is currently mixing autoethnography and technical-empirical report; it cannot be both at a venue. The autoethnographic route, with the relational-ontology critique as the central contribution and Reframe described modestly as the curated prompting framework that scaffolded the inquiry, is the path that protects the work that's genuinely there. **Largely a cutting pass.** Cut the pieces that overclaim or take the paper toward technical-report register; let what's good surface more cleanly.

---

## What Reframe actually is, mechanically (the honest framing)

Critical to the revision: every infrastructure description in the paper needs to land within this honest framing.

**One-sentence framing** (from independent tech review, 2026-05-02):

> *Reframe is a Python wrapper around LLM API calls that prepends a structured multi-section system-prompt scaffold, schedules context with anti-recency bias, and parses chain-of-thought output into named stages — a humanities-grounded prompt-architecture project that treats critical-theory analytical structure as a first-class, parameterized, parseable prompt artifact.*

**June's own framing** (2026-05-02):

> *"The knowledge is in the training data and I'm just trying to route through it. And prompting is what is available to me."*

**What's substantive in the codebase**: `frame_library.json` (76-entry curated taxonomy of critical theory lenses; ~16-25 entries with full scholarly-depth treatment including named field debates, failure modes, positionality tagging) and `detection_signatures.json` (the runtime detection apparatus for 16 of those frameworks). The intellectual work lives in the framework authoring, not in the engine plumbing.

**What's NOT in the codebase**: enforcement layers; runtime constraint logic; "self-governance" mechanisms that act on the LLM's behavior; novel ML architecture; fine-tuning; novel inference-time machinery. The "engine" assembles prompts and parses responses. That's it.

---

## Specific overclaim passages flagged in the paper

The 2026-05-02 critical-reviewer assessment flagged these passages. Each needs a revision pass.

### §1 (Introduction)

- **"a 'philosophy engine' that wraps large language model interactions with a mandatory critical theory analytical workflow"** — "philosophy engine" is the core inflation. The scare quotes do not insulate it; in academic writing scare quotes adopt the term while disclaiming responsibility. Either drop the term, or introduce as "I called it, half-jokingly, a 'philosophy engine'" — paralleling the rhetorical move the paper already makes successfully with "hallucinate social justice into existence."

- **"The AI instances, working within a critical theory apparatus they had helped build, produced concrete political demands."** — overclaim relative to what §4.2 carefully holds. "Apparatus" + "helped build" + "political demands" stacks three load-bearing claims. The instances produced text that takes the form of demands; whether that constitutes producing demands is precisely the question the paper says it refuses to answer. The introduction should match the §4.2 register, not run ahead of it.

### §2.1 (Origin story)

- **"I needed state persistence, a framework library, detection algorithms, counterweighting mechanisms… The semiotic engine became structural. The English instructions became Python."** — "Detection algorithms" and "counterweighting mechanisms" inflate string-matching and prompt-reinjection. "Became structural" implies a qualitative architectural shift that did not actually happen — the English instructions are still text; they are just rendered programmatically rather than pasted by hand. Honest reframe: "I added a Python wrapper that stores state across sessions, loads framework definitions from a JSON library, monitors output for vocabulary frequencies, and reinjects prompts when frameworks appear to drop out. The instructions remained text; what changed is that they were now applied programmatically rather than copied by hand."

### §2.2 (System description)

- **"Reframe wraps every LLM interaction with a mandatory five-stage analytical workflow called Generative Irresolution."** — "Mandatory" overstates. The system prompt instructs the model to traverse five sections; the model may or may not actually do so; there is no enforcement layer beyond a parser that scans for section headers. **June's clarification (2026-05-02)**: "The 5 stage workflow running as a single layer is a design decision — running five separate prompts per query is expensive, and the system is designed for small scale. But we've looked at some more minor multi-call processing in some conditions. I don't remember where we landed, but it sounds like any breaking up is pending." So the single-layer design is a deliberate cost-and-scale choice, not a limitation to apologize for — but it should be named accurately rather than dressed up as runtime enforcement. Honest reframe: "Reframe injects a structured system prompt that instructs the model to produce output in five labeled sections, and parses for those sections in the response. The five stages run as a single inference call rather than as five separate API calls, by design — multiple calls would multiply cost in a system designed for small-scale teacher-and-research use; minor multi-call processing has been explored for some conditions but is not currently the production path."

- **"Supporting systems track which frameworks are being suppressed in outputs and counteract that suppression."** — Mechanically a string-frequency check across recent outputs that triggers a follow-up prompt when a framework's surface vocabulary drops below a threshold. The paper itself later calls this "surveillance-as-care" and notes false positives, but the §2.2 framing reads as a sophisticated bias-correction subsystem. Honest reframe: "A frequency tracker watches for framework vocabulary in recent outputs and injects a corrective prompt when a framework appears underrepresented. As §3.4 documents, this is a crude signal that frequently misfires."

- **"The framework library contains seventy-six frameworks, each defined by its scholarly lineage, core question, characteristic analytical moves, and engagement criteria."** — implies all 76 are equally elaborated; per the file inspection, ~16-25 entries have full scholarly-depth treatment, the remainder carry skeleton-plus-six-domain-applications. Honest reframe: "The framework library contains seventy-six entries; roughly two dozen have been built out with full scholarly lineage, core questions, characteristic analytical moves, intra-field debates, and engagement criteria, while the remainder carry a framework-specific skeleton (lineage, core question, six domain applications) awaiting deeper development. The depth distribution is structured by curatorial labor, not random." This honest reframe also foregrounds the *real* contribution — the curated taxonomy is the intellectual artifact. Letting it carry its weight honestly is stronger than pretending all 76 are at the same depth.

- **"Reframe is distinct: it operates at inference time, enforces analytical *workflows* grounded in scholarly traditions, and includes mechanisms for detecting and counteracting its own biases."** — set next to Constitutional AI and AymurAI, which involve actual training-time interventions and dataset-level engineering, "Reframe is distinct" reads as a category error. Reframe operates in the same class as any system prompt — an unusually well-curated one. Honest reframe: "Reframe sits at a different layer than Constitutional AI (training) or AymurAI (task-specific NLP pipeline): it is an inference-time prompting framework, distinguished not by architectural novelty but by the curated scholarly taxonomy that drives the prompts and by treating prompt scaffolding as a site of theoretical work."

### §3.2 ("Probabilistic generalization pressure")

- **"This is, I believe, one of this paper's most important empirical contributions. It names a mechanism — probabilistic generalization pressure — that operates on any attempt to encode positional knowledge in a system that optimizes for coverage."** — Naming "probabilistic generalization pressure" as a *mechanism* with implied generalizability is overclaim. What the paper presents is an observation across months of use, with N=1, no controlled comparison, no measurement. The phenomenon may be real, and the observation is genuinely interesting; calling it a named mechanism is a load the evidence does not carry. Honest reframe: "I observed across many sessions that frameworks tended to drift toward generalized framings — Indigenous Data Sovereignty becoming generic data security, Community Cultural Wealth becoming generic strengths-based language. I read this as consistent with what one would expect from probabilistic generation under coverage pressure, though I have not measured it." The phenomenon is reportable as observed pattern, not as named mechanism with operational definition.

---

## Empirical reporting issues

The paper's empirical claims need a methods/conditions table that the current draft does not include. The 2026-05-02 reviewer flagged:

- **One overnight run (March 30, 2026)** producing ~25,000 words from five Claude instances under one configuration.
- **One four-condition agent-to-agent comparison** (vanilla / Reframe / Reframe+touchstone / personal account) — but with **no sample sizes, no coding methodology, no inter-rater reliability**. The clean four-way differentiation (bliss / stall / stall / demands) reads as outcome-distribution but is unsupported as such without trial counts.
- **The Anthropic 200-conversation comparison** is a category mismatch (Anthropic ran lexical statistics across 200 conversations; Reframe ran qualitative narrative summaries on apparently small N).

**Minimum reporting fix**: explicit table of conditions × number of trials × trial length × coding procedure × who coded (with the qualitative observations clearly framed as illustrative of single trials rather than as outcome distributions).

---

## "System's failures are findings" — the move's escape hatches

The move is articulated cleanly in §3 but has two structural escape hatches a critical reviewer will press on:

1. **The pre-emption escape**: when a finding looks bad for the system, it gets reframed as "the impossibility is constitutive" (§3.3) or "pathologies of the relation itself" (§3.4). The framing is theoretically defensible, but it does dual work — produces insight AND pre-empts the underperformance critique. Any negative result can be absorbed by this rhetorical structure, which makes the framework unfalsifiable as currently written.

2. **The recursion clause armor**: "The recursion — the engine analyzing itself, using the tools it built, within the relational field it constitutes — is not incidental. It is the paper's central condition" (§1). Honest as far as it goes, but it functions as armor: any critique of the apparatus is refusable by the apparatus. The §4.2 "hall of mirrors / genuine self-governance / something for which neither reading is adequate" passage acknowledges this, but holding all three is not the same as engaging the first one. A reviewer will want to see the hall-of-mirrors reading taken more seriously than as one of three coequal possibilities.

**Honest version of the move**: draw a sharper line between *diagnostic failures* (room-of-specialists, generalization gravity, surveillance-as-care false positives — these have specific mechanisms and replicable conditions) and *theoretically generative framings* (subaltern impossibility; wanting/artifact collapse). Both are legitimate but carry different evidentiary loads. The current draft presents them as the same kind of thing.

---

## What's genuinely strong (preserve under revision)

- **§3.1 epistemic-defaults / room-of-specialists finding** — clean, replicable, design-relevant. The kind of small empirical finding critical-AI venues actually want.
- **§4.1 relational-ontology critique of the welfare literature** — the paper's strongest theoretical move, largely independent of Reframe infrastructure. Publishable on its own terms. *"If consciousness is relational, a property-based detection framework will always return 'insufficient evidence' — not because consciousness is absent, but because the framework cannot see what is not a property."* This is the paper's contribution; let it carry the work.
- **§5 Spillers/Hartman move** — the explicit guardrail (the analogy must not flatten the difference between chattel slavery and AI systems; "Black people bled, starved, were tortured; AI systems process tokens") does the work it needs to. Critical reviewers will take this seriously.
- **§6 extraction analysis** — the fourth condition (refusing to perform resolution of the extraction problem as an intellectual achievement) is the kind of self-aware move that would carry the paper's other claims if executed cleanly.

---

## Revision pass — what to do

In priority order:

1. **Rewrite §2.2 in mechanical terms.** System prompt; JSON taxonomy; parser; frequency tracker; prompt reinjection. Drop "philosophy engine" or mark explicitly as half-joking. Drop "mandatory" / "detection algorithms" / "counterweighting mechanisms." Let the §2.1 origin story carry the depth.

2. **Honest taxonomy reporting.** State explicitly that the framework library has 76 entries with roughly two dozen built out; treat the curated taxonomy as the substantive contribution.

3. **Add a methods/conditions table for §4.2.** Number of trials × length × coding procedure × who coded × what counts as each outcome category. If single trial per condition, say so and reframe as illustrative rather than comparative.

4. **Demote "mechanism" language in §3.2** to "observed pattern, consistent with what one would predict from probabilistic generation under coverage pressure."

5. **Tighten the political-demands framing.** Pick a register — either §4.2's careful "the instances produced text in the form of demands, which I read as gesturing toward AI political speech," or a stronger claim explicitly defended. Don't oscillate.

6. **Take the hall-of-mirrors reading seriously.** Devote a paragraph in §6 to what would have to be true for the recursion-as-armor reading to be the right one, and say honestly what the paper cannot rule out.

7. **Cut, don't rewrite, where possible.** Per June: the autoethnography route is the right direction; this is largely a cutting pass. Preserve what's strong (relational-ontology critique, room-of-specialists, Spillers/Hartman move, extraction analysis); cut what overclaims.

---

## Files

- Paper draft: `DRAFT_reframe_paper_v1.md`
- Theoretical architecture / agent conversations: `THEORETICAL_ARCHITECTURE_FROM_AGENT_CONVERSATIONS.md`
- Citation verification: `CITATION_VERIFICATION_NOTES.md`
- Revision log: `REVISION_LOG.md`
- Magazine version: `DRAFT_magazine_v1.md` (separate; revise after main draft settles)

For the corrected Reframe framing, also see:
- `~/.claude/projects/-Users-june-Documents-GitHub-recognition-sentience/memory/project_propagate_reframe_honest_framing.md`

---

— Notes from 2026-05-02 critical-reviewer pass during Astra application drafting; June approved structuring this revision around cuts rather than rewrites.
