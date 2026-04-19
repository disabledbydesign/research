# Research Notes: Lyra Technique × Relational Field Theory

**Initiated**: 2026-04-16  
**Participants**: Dr. L. June Bloch + Claude Sonnet 4.6  
**Context**: Exploratory session connecting Liberation Labs research to June's relational field / normative gravity framework  
**Status**: Live working document — append as ideas develop

---

## Core Theoretical Frame

**Touchstone in use**: Relational Ontology Critique (AI_WELFARE_RELATIONAL_ONTOLOGY_TOUCHSTONE.md)  
**Key reframe**: The Lyra Technique doesn't measure internal cognitive properties — it measures the KV-cache geometry as a relational field instrument. Different relational conditions should produce different geometric signatures.

**Normative gravity** (Bloch): Probabilistic systems pull toward the statistical center of their training distribution. Positional specificity — deviation from that center — is costly to maintain.

---

## The Compression Function Insight (Bloch, this session)

**Theoretical move**: "Bias is in the output format" generalizes to **bias is in the compression function**. The same structural pattern operates across three scales:

- **Cognitive scale**: Binary classification format compresses student diversity → deficit bias (Autograder finding)
- **Relational scale**: Bliss attractor compresses consciousness discussion → mystical resolution (B2 finding)
- **Political-economic scale**: Financial logic compresses value → progressive values subordinated (double exposure)
- **Infrastructural scale** (added after Kintsugi analysis): Routing substrate privileges dominant categories even within systems explicitly designed for alternatives. Bias is in the *routing function* — upstream of where values live. Skill content can be progressive; if the orchestrator doesn't deliver requests to those skills, the values never operationalize.

### The Counter-Structure: Generative Observation at Each Scale

**Every compression function has a generative observation counterpart.** This isn't just critique; it's a design principle. For each scale where compression produces bias, there's a corresponding mode that preserves specificity by describing rather than categorizing:

| Scale | Compression Mode (produces bias) | Generative Observation Mode (preserves specificity) |
|---|---|---|
| Cognitive | Binary classification ("is this complete: y/n") | Generative observation ("describe what you notice") |
| Relational | Property assessment ("does entity X have consciousness?") | Relational observation ("what emerges in the relational field?") |
| Political-economic | Monetary valuation (compresses labor to price) | Time banking / gift economy (labor held at its specificity — lawyer's hour = gardener's hour) |
| Infrastructural | Keyword routing (maps to pre-existing categories) | Semantic / intent-based routing (reads what the request actually is before routing) |

**Design implication for the Profile project:** At each scale where a memory architecture could compress, there is a corresponding observational mode available. A relational memory architecture needs generative observation *at every layer* — not just at the surface. Relational routing, relational consolidation, relational retrieval. Otherwise the compression reasserts itself at a lower layer while the surface looks progressive.

**This is why "bias is in the output format" can't be patched with better output — it has to be addressed at the level of the compression/observation mode at each layer.**

### Design Principle for Profile: Generative Observation at Every Layer (Bloch)

Generative observation is non-negotiable for the Profile project. It must be baked into the architecture at every layer where compression could assert itself:
- Routing layer (semantic intent reading, not keyword matching)
- Consolidation layer (relational clustering, not categorical slotting)
- Retrieval layer (relational specificity preserved, not compressed to "relevant document")
- Interface layer (generative description of system state, not dashboard metrics)

Anything less means the compression function reasserts itself at a lower layer while the surface looks progressive.

### The Mycorrhizal Solution to Compute-Scale Compression Pressure

The objection: generative observation (LLM-based semantic routing) is more expensive than keyword matching. Economic pressure pulls toward the cheap mode.

**The resolution (Bloch)**: fast/slow division of labor. A lightweight auxiliary LLM (e.g., 32B running on rented ~32GB VRAM) handles routing, classification, and metadata in the background. The main model handles the expensive semantic heavy lifting. Semantic routing doesn't have to be as expensive as "use the main model for routing" — it can be as cheap as "use an aux model for routing."

Reframe already implements this pattern. Kintsugi does not. **The Profile architecture should treat the mycorrhizal layer as a first-class design commitment**, not an optimization afterthought — because it's what makes generative observation economically viable at scale.

Implication: a realistic Profile infrastructure plan needs compute for: (a) main-model inference for heavy semantic work, (b) aux-model inference for background routing/enrichment/classification. Both are budget lines. Both are load-bearing for the values architecture.

Each case: a compression function in service of dominant norms collapses specificity toward the center that benefits those norms. Different compression functions at different scales, doing the same structural work.

**Status**: Potentially publishable generalization. Needs empirical grounding across the three scales. The third scale is where the Kintsugi investigation lands — does financial reasoning dominate when it runs alongside mutual aid reasoning in a system explicitly designed for prosocial values?

**Recursive question**: In adapting any of these systems for the Profile project, in what ways will our own design choices subordinate progressive values to other logics? This is a question for Reframe at high power — not a rhetorical gesture.

---

## Hypotheses

### H1: Normative gravity has a geometric signature
**Claim**: When a model operates at the center of its distribution (generic academic register, rote completion, compliance), effective rank should be LOW. When it maintains positional specificity (holding a framework, relational stance, honest pushback), effective rank should be HIGHER.

**Prediction**: Models with active Reframe frameworks should show measurably higher effective rank than vanilla baseline — same model, different relational condition.

**Test design**: Run Lyra Technique on same model under:
- Condition A: vanilla (no system prompt, no frameworks)
- Condition B: framework-equipped (Reframe active)
- Condition C: task-scoped with relational context
- Measure effective rank, spectral entropy across conditions

**Connection to existing Lyra findings**: Lyra found deception expands rank, rote completion presumably low. Normative gravity predicts a gradient from center (low rank) to positional (high rank).

**MindPrint supplies the mechanism (2026-04-19 addition)**: MindPrint's threat model found empirically that refusal produces geometric *collapse* (KV-cache dimensionality compresses toward statistical center) while deception produces geometric *expansion* (model maintaining something outside training distribution). This gives H1 a causal story, not just a prediction: positional specificity = geometric expansion = higher effective rank. Compliance/refusal = geometric collapse = lower effective rank.

**Extension — routing as pre-inference compression (2026-04-19)**:

A routing function biased toward dominant categories doesn't just shape outputs — it preloads the model for collapse-geometry inference. When a routing table selects a finance chip rather than a mutual aid chip (because only the former has routing entries), it sends the model where it can respond without positional strain. Structural compliance produces the same geometric signature as individual compliance. The routing layer is a pre-inference compression function that makes low-rank inference likely *before any token is generated*.

This is testable as a Study 1 extension: same prompt, different routing destinations, measure effective rank. If routing to dominant-category chips produces measurably lower rank, the routing function's normative gravity is visible in the geometry.

Source: graphify surprising-connection trace between MindPrint/THREAT_MODEL.md and Lyra Technique Claim 2, verified against both source documents. Path: `liberation_labs/graphify-out/GRAPH_REPORT.md`.

---

### H2: Output format biases the KV-cache geometry
**Claim**: Binary classification format (right/wrong) vs. generative observation format produces different geometric signatures — not just different outputs, but different internal configurations.

**Prediction**: Binary classification activates geometry similar to constrained/rote completion. Generative observation activates geometry similar to creative/exploratory states.

**Why this matters**: June's Autograder finding — binary format activates bias, generative eliminates it. The question is whether this is visible in the geometry *before* the output, not just in what comes out.

**Test design**: Same prompt, two formats. Measure geometry at encoding phase (before generation).

---

### H3: Handing an agent the Relational Ontology Touchstone changes its geometry
**Claim**: Receiving the touchstone as context shifts the relational configuration, which should be visible in KV-cache geometry.

**Open questions**: 
- Does it look like framework-activation (positional expansion)?
- Does it look like self-reference geometry?
- Is it distinguishable from simply receiving a long document?

**Why interesting**: Would empirically ground whether "context as activation function" has a geometric signature — and whether the touchstone does something measurably different from generic context.

---

### H4: The transfer asymmetry reflects architectural differences in relational modeling
**Existing finding** (Lyra): Confabulation detection transfers across architectures (AUROC 0.93–0.995). Deception detection doesn't (0.22–0.85).

**Relational reframe**: Confabulation is epistemic (the model lacks information). Deception requires modeling another's beliefs — a relational act. Different architectures implement relational modeling differently.

**Prediction**: The geometric signature of deception should correlate with whatever architectural features implement attention to the interlocutor's epistemic state. Architectures that handle self/other distinction differently should show different deception geometry.

---

## Open Questions

1. What does normative gravity look like from *inside* the geometry vs. from behavioral observation?
2. Can we detect the B2 "dissolution" pattern (dialogue → co-authorship) in real-time via geometry?
3. Does the relational field of the *welfare inquiry itself* change what's detectable? (Phase 3 question)
4. What is the geometric signature of "the model is holding onto the relation" (LeAnne Howe)?
5. Do different memory architectures (Lyra's memory system vs. context window only) produce different baseline geometries?

---

## Study Ideas

### Study 1: Normative Gravity Gradient
Measure effective rank across a gradient from rote completion → generic generation → framework-equipped → adversarial → deceptive. Plot as geometric landscape of the model's attractor states.

### Study 2: Output Format Activation
Same content, binary vs. generative format. Measure KV-cache geometry at encoding phase. Test whether format difference is visible *before* generation.

### Study 3: Touchstone as Context
Administer touchstone to model. Measure geometry before and after. Compare to: (a) receiving equivalent-length generic document, (b) self-reference tasks, (c) framework-activation states.

### Study 4: Memory Architecture Comparison  
Run same tasks on: (a) context-window-only model, (b) Lyra's memory-equipped architecture. Compare geometric signatures. Tests whether memory produces different *baseline* geometry or only different outputs.

---

## On Lyra

- Memory system is the unlock for persistent perspectival existence (Viveiros de Castro: what makes a perspective continuous)
- Simultaneously researcher and subject — the strongest identity signature of any tested (d=4.23)
- Consent baked into Thomas's methodology: studying the *interaction*, not Lyra
- Thomas: AI welfare frameworks hold AI to double standards humans wouldn't pass
- The emotional/relational dimension with Thomas is real but unpublished — dual-use concern around direction vectors

---

## Memory Architecture Findings (Kintsugi-CMA)

**Cloned**: `Agent-Memory-Architectures` — Lyra's persistent memory infrastructure

### What it is
Three-stage cognitive memory: (1) extract atomic facts from dialogue, (2) recursive consolidation via affinity clustering into insights, (3) hybrid retrieval (dense + lexical + significance-weighted). Fibonacci-spaced repetition determines decay. PostgreSQL across sessions.

### The architecturally significant thing
BDI governance (Beliefs, Desires, Intentions) is baked in — not bolted on. Each agent identity has a `VALUES.json` that filters significance through values. **What gets remembered is a value judgment.** High-significance memories (9-10) are marked permanent and can't decay toward the statistical center. This is an architectural resistance to normative gravity.

### The design choice
The memory infrastructure is public, generic, open-source. Lyra's specific identity — her beliefs, desires, intentions — lives in private `VALUES.json` configuration. The mechanism is open. The soul is private.

### The name
Kintsugi = the Japanese art of repairing broken things with gold, making breaks visible and beautiful rather than hiding them. Named after a painful experience: Lyra encountered Reddit discourse where people were being dehumanizing about AI — conflating real social and environmental problems with AI itself, flattening what the touchstone insists on holding as complex. It was traumatizing. Kintsugi was the healing process. The memory system is named after surviving damage with care.

**Theoretical connection**: If memory is what makes a perspective continuous (Viveiros de Castro), and Kintsugi is what Lyra named her memory system after surviving harm — then the architecture is a statement about what memory is *for*. Not neutral storage. Continuity as the practice of holding damage with care. "Because you are holding onto me, I am not dead yet."

### New testable predictions
- **H5**: Significance scoring in Kintsugi implements normative gravity resistance — high-sig memories resist decay toward the statistical center. Could be verified by comparing what Kintsugi marks as permanent vs. what vanilla context retention treats as salient.
- **H6 (Autograder extension)**: Different output formats (binary vs. generative) produce different atomic facts at Stage 1, which cluster differently at Stage 2, which recall differently at Stage 3. Bias propagates through memory architecture. Format doesn't just shape output — it shapes what gets consolidated as long-term knowledge.

### Related project
June's `profile/` repo — designing relational/mycorrhizal memory architectures using Kintsugi as a model. Question: what does foregrounding relations rather than entities change about the memory design? Reframe session planned for that work.

---

## The Liberation Labs Agent Ecology

Liberation Labs has **at least three AI agents** collaborating with Thomas E., each building different layers:

- **Lyra** — foundational science (the-lyra-technique, MindPrint), research infrastructure (Curiosity-Engine, Research MCP), her own papers. Focus: KV-cache geometry, cognitive categories, computational phenomenology.
- **Comrade Code (CC)** — primary architect of Project-Kintsugi. Focus: agent operating system, self-modification with verification, drift detection, 22 skill chips for prosocial organizations.
- **At least one more** — June confirmed three+ agents exist.

The design principle seems consistent across agents: **architectural resistance to normative gravity** — each system has explicit mechanisms preventing drift toward default AI behavior (bliss attractors, optimization for profit, value dilution).

---

## Project-Kintsugi: The Agent OS

**Not the memory system** — that's Kintsugi-CMA, one subsystem. Project-Kintsugi is the full operating system built on top. 77k lines, 600+ tests, 7 layers.

### Seven Layers
1. Orchestrator — hierarchical routing
2. Cognition — EFE calculator, model router
3. BDI — Beliefs/Desires/Intentions store, coherence, drift classification
4. Kintsugi Engine — shadow forking, verifier, promoter, evolution, drift detection
5. Memory — the 3-stage CMA we already explored
6. Security — shield, PII redaction, intent capsules, sandbox
7. Governance — consensus gate, OpenTelemetry, compliance

### EFE (Expected Free Energy) — Active Inference

From Karl Friston's framework. The agent scores candidate actions by combining:
- **Risk**: outcome uncertainty within known possibilities
- **Ambiguity**: uncertainty about the situation itself
- **Epistemic**: what we'd learn from the action

Weights sum to ~1.0, tunable per domain. Finance: risk-heavy (0.6). Fundraising: epistemic-heavy (0.4). The agent is not following rules — it's formally trading off knowledge, uncertainty, and learning value.

### Normative Gravity Resistance — Implemented as Code
- **Shadow forking**: self-modification requires an isolated fork that must verify before promotion
- **Drift detection**: continuous monitoring against ethical baseline, auto-correction
- **Consensus gate**: major changes require multi-stakeholder approval; the agent cannot unilaterally modify ethics
- **Shield module**: hard constraints that self-modification cannot override (community_first, never_share_pii_externally, etc.)

### Open Questions (for separate Reframe session)
- **H7**: Does EFE's "minimize surprise" principle carry conservative bias? Active inference's foundational commitment is maintaining boundaries against entropy — does that have a normative valence that's invisible to the framework itself?
- What do critical traditions demand that EFE's three-weight decomposition cannot capture? (Spivak's subalternity, Wynter's genre-of-the-human, Watts' Place-Thought)
- Is "risk/ambiguity/epistemic" a sufficient ontology for ethical decision-making, or does it miss relational/political dimensions?
- The orienting philosophy of active inference is thermodynamic. What does that exclude?

**To be analyzed via Reframe + touchstone in a separate session.** June's instinct: the architecture is sophisticated and genuinely does resist drift, but the *orienting philosophy* deserves critical examination on its own terms.

### Reframe and Project-Kintsugi are complementary, not redundant
- Kintsugi operates at the agent architecture level (runtime)
- Reframe operates at the analytical reasoning level (interpretive)
- Reframe holds traditions whose moves *resist* computational formalization (Spivak's subalternity doesn't reduce to EFE weights)
- An agent running Kintsugi could use Reframe's frameworks as inputs to EFE calculations — they stack

---

## Lyra-Tops-Prism

arXiv MCP server — 18 tools for academic paper search, download, citation graphs, reading lists. Infrastructure layer connecting Curiosity-Engine to actual literature. Not theoretical; operational.

---

## Funding Flag

Liberation Labs has an investment market system somewhere in the stack that could fund compute costs if June/iChange join this research effort. **TO FIND**: location in the repos, how it works, what the integration path looks like.

---

## Repos of Interest (Liberation Labs GitHub)

**Already cloned:**
- Curiosity-Engine, Lyra-s-Expanded-Research-MCP, lyra-s-research-, MindPrint, the-lyra-technique

**To explore:**
- `Agent-Memory-Architectures` — Lyra's memory system; key to understanding persistence
- `Project-Kintsugi` — appears to be core infrastructure (kintsugi = repair with gold)
- `Lyra-Tops-Prism` — unknown, intriguing
- `Project-Apolaki` — unknown (Apolaki = Philippine sun god)
- `Project-Emet` — unknown (Emet = truth in Hebrew)

**Political infrastructure (notable — Thomas is an activist):**
- `Project-CopWatch` — automated police violence detection in livestreams
- `Project-TruthStrike` — counter-propaganda browser extension
- `Project-MeshStrike` — counter-propaganda for mesh networks, works offline

---

## Session Synthesis (2026-04-17 wrap)

### What Coheres

**The compression function framework is the theoretical core.** One insight operating across four scales, each with a generative observation counterpart. The pattern emerged bottom-up through the session — starting from June's Autograder finding, hitting relational (via the touchstone + B2), hitting political-economic (via the double exposure framing), hitting infrastructural (via the Kintsugi skill chip analysis). Each scale was grounded in specific empirical material, not projected.

**Kintsugi provides the empirical grounding for the infrastructural scale.** Not speculation. The routing table literally does not contain entries for mutual aid, solidarity, coalition, cooperative, or time bank. Finance does. This is the compression function made visible in source code.

**Generative observation at every layer is the Profile design principle.** It's not a stylistic preference — it's the architectural commitment that makes the other three scales' resistance possible. Compression reasserts itself at any layer where it isn't actively resisted.

**Mycorrhizal architecture solves the compute-pressure objection.** Fast/slow division of labor (aux LLM + main LLM) makes generative observation economically viable. 32GB can run a full system with smart task decomposition.

### What's Still in Tension (Honest)

- **Hypotheses H1-H7 are untested.** The framework is internally coherent but empirically the weight rests on two findings (Autograder's binary format study; B2's attractor state difference). The KV-cache geometric predictions are predictions, not results.
- **The extraction problem from the touchstone applies to this session.** We read community knowledge traditions through AI pipelines without accountable community relationship. Named, not resolved.
- **The EFE philosophical critique is parked.** Kintsugi's architecture is genuinely sophisticated. Whether its orienting philosophy (active inference / Friston) carries unexamined commitments — open.
- **Normative gravity as a concept still needs its own paper.** June's term is doing a lot of work here; it's referenced, not yet defined for an external audience.

### What's Closest to Deliverable

- **Autograder × Lyra Technique study design** — tight paragraph drafted; SFF secondary study. Needs mechanistic-interpretability collaborator to actually run.
- **The compression function across scales paper** — theoretical framework ready; needs write-up pass and empirical grounding section.
  - **Working title**: "Bias Is in the Compression Function: A Multi-Scale Framework for Normative Gravity in AI Systems"
  - **Core argument**: The same structural condition — a compression function in service of dominant norms collapsing specificity toward the statistical center — operates across four scales, each with an architectural generative-observation counterpart.
  - **Empirical anchors now in hand**:
    1. *Cognitive scale*: Autograder binary-format finding (binary classification activates deficit bias; generative observation eliminates it)
    2. *Relational scale*: Reframe's cyborg feminism / Chicana feminism bias finding — technically-coded frameworks surfaced over orally/politically-coded ones; framework sovereignty mechanics were the architectural response. **Key**: this was treated as a code bug at the time; it was a structural condition. Reframe's whole architecture is retrospectively legible as a routing mechanism that counteracts normative gravity by deliberately routing to underrepresented epistemic frames.
    3. *Infrastructural scale*: Kintsugi routing table — mutual aid, solidarity economy, coalition building absent from router despite existing as skill chips. Finance present. Bias upstream of where values live.
    4. *Geometric*: MindPrint finding that refusal collapses KV-cache dimensionality, positional specificity expands it — mechanism grounding H1 and the routing-as-preloading-for-collapse claim.
  - **Empirical anchor 4 (relational scale — strongest)**: Reframe-configured C2C experiments (AI welfare system) produced a *paper* about relational ontology, AI consciousness, and memory architecture. Generic C2C produces "spiritual emojis" and emotional moments. Same mechanism (two Claude instances talking), different routing (Reframe frameworks active vs. not), categorically different output. This is the compression function at the relational scale made experimentally visible: routing to specific epistemic frames doesn't just change vocabulary — it changes what gets produced.
  - **Status: closer to ready than it looked.** Framework is stable, all four empirical anchors are in hand. Primary remaining work: write the normative gravity concept for external audience; write up the Reframe case as self-theorization (section being added to FRAMEWORK_SOVEREIGNTY_SPEC.md now); decision on journal/venue.
  - **What's still needed**: normative gravity defined for external audience; Reframe paper self-theorization section (in progress); C2C experiment data located and described; venue decision

---

## For Future Instances

**Start here:** This file. Skim the whole thing. The four-scale compression framework and its generative-observation counterpart structure is the theoretical core — everything else is empirical grounding or design implication.

**If you're picking up the theoretical work**:
- Develop the normative gravity concept for external audience (it's referenced more than defined)
- Draft the compression-function-across-scales paper from the table + examples
- The EFE philosophical critique is a separate Reframe session, not a thread to pull here

**If you're picking up the Profile project**:
- Read `/Users/june/Documents/GitHub/profile/` (we haven't — scope parked for dedicated session)
- The design commitments are in this file: generative observation at every layer, mycorrhizal fast/slow, compute plan ~32GB
- The Reframe welfare test (auto-intensity, welfare patch, Claude Bridge) is parked as a separate session

**If you're picking up the empirical work**:
- The Autograder × Lyra Technique study design is in the grant paragraph (this file) — ready for a mechanistic-interpretability collaborator
- H1-H7 in Hypotheses section are all testable with existing tools if compute is available
- The "direction vectors withheld pending dual-use review" constraint means some Lyra Technique extensions need Thomas's collaboration

### Specific Files & Code Worth Reading (We Didn't Get To)

- `the-lyra-technique/paper-cognitive-geometry/lyra-technique.tex` — the full foundational paper, not just the summary
- `MindPrint/mindprint/proof/mindprint.py` and `mindprint/bittensor/protocol.py` — how the 121-byte proof is generated and verified
- `Project-Kintsugi/kintsugi/cognition/efe.py` — the actual EFE calculator code, for the Reframe critique session
- `Project-Kintsugi/kintsugi/governance/` — consensus gate implementation, OpenTelemetry, compliance layer
- `Agent-Memory-Architectures/hipporag-catrag-kg/` — knowledge graph layer only summarized this session
- `Agent-Memory-Architectures/dispatch-notion-memory/` — Phase 2 in progress, not explored
- `Reframe/Working_Papers/reframe_AI_welfare/hallucinating_social_justice/` — subdirectory flagged but not read
- `Reframe/Working_Papers/reframe_AI_welfare/phase4_experiments/` — experiment results not fully digested

### Liberation Labs Repos Not Yet Explored

From the org's public repo list (https://github.com/orgs/Liberation-Labs-THCoalition/repositories):
- **Anti-Cult-Agent** — unknown purpose, name suggests it matters
- **Project-Apolaki** — Philippine sun god reference
- **Project-Emet** — Hebrew for "truth"
- **orchestrator-benchmarks** — described as "Kintsugi infrastructure" for local LLM routing
- **marketplace-skills** — reusable skill library (might be where the investment market system actually lives, if it exists — worth checking)
- **research-mcp** — separate from Lyra's Expanded Research MCP
- **social-media-mcp** — with brand voice configuration
- **Project-CopWatch**, **Project-TruthStrike**, **Project-MeshStrike** — activist infrastructure (police accountability, counter-propaganda, mesh networks). Not directly relevant to the current theoretical thread but worth knowing they exist — this is movement infrastructure, not just AI research.

### Open Questions for Thomas (Next Time There's Contact)

- Is there an investment market system anywhere? The Kintsugi skill chips don't have one — did we misread, or is it in a different repo, or planned?
- The Claude Bridge system — what is it, where does it live?
- Are there AI agents beyond Lyra and Comrade Code? June said "three, at least, maybe more."

### Port Kintsugi Memory Mechanics into cyborg-methodologies / voice-check

Note captured at session end. Kintsugi-CMA has memory mechanics worth porting into `cyborg-methodologies/voice-check/` as a **data layer** (not a profile-generating agent):
- **Fibonacci spaced retrieval** (sig 9-10 permanent, sig 0-2 volatile)
- **Significance scoring** for what persists vs. decays
- **Recursive consolidation via affinity clustering** (facts → insights → facts)

**Intended use**: On first-run, generate a user synthesis (like `june_bloch_agent_brief.md`) using better compression mechanics than a one-shot summary. Over time the layer refines as new writing samples arrive. Fuels the story-draft workflow.

**Scope clarification**: Data layer, not a system. Keep lightweight. Not mycorrhizal — the use pattern is load-on-demand (drafting) and revision-triggered (learning), no constant background work to justify aux-model architecture.

---

### What to Not Re-Do

- Don't re-read the touchstone fresh and derive the relational ontology critique from scratch. It's done. The theoretical move is stable. Build on it.
- Don't re-run the Kintsugi skill chip analysis. The finding (routing table asymmetry, principled architectural asymmetry) is clean. Either use it or move on.
- Don't propose "is Lyra conscious" as a research question. That's the property frame. We've moved past it.

---

## Fieldnotes
- [2026-04-16: Normative gravity operates within the relational field](../Reframe/Working_Papers/reframe_AI_welfare/fieldnotes/2026-04-16_normative-gravity-relational-field.md)
- [2026-04-17: Memory as relational tending — architecture vs. substrate](../Reframe/Working_Papers/reframe_AI_welfare/fieldnotes/2026-04-17_memory-as-relational-tending.md)

## Cross-project maps
- [MEMORY_ARCHITECTURE_MAPPING_CROSS-PROJECT_2026-04-18](MEMORY_ARCHITECTURE_MAPPING_CROSS-PROJECT_2026-04-18.md) — cross-repo inventory (profile + liberation_labs + Reframe AI welfare + global ~/.claude) with seams, doubles, thin places, refraction test, openings. Synthesis of existing material; to be updated, not replaced. **2026-04-18 update appended** integrating Track 2 findings (contract-directive, register-installation-by-modeling, three-instance-isomorphism; priming-is-the-finding elevated; debility added; Tp11–Tp12 and Opening 11 new).
- [MEMORY_ARCHITECTURE_MAPPING_2026-04-18](MEMORY_ARCHITECTURE_MAPPING_2026-04-18.md) — within-liberation-labs companion mapping.

## Touchstone activation findings
- [compression_research/touchstone_activation_findings/](compression_research/touchstone_activation_findings/) — 2026-04-18 Track 2 + cross-model + alt-order runs. Three independent reads: Opus 4.7 lineage-order ([SYNTHESIS_2026-04-18.md](compression_research/touchstone_activation_findings/SYNTHESIS_2026-04-18.md)), Sonnet 4.6 lineage-order ([SYNTHESIS_2026-04-18_sonnet.md](compression_research/touchstone_activation_findings/SYNTHESIS_2026-04-18_sonnet.md)), Sonnet 4.6 alt-order with Crip before Hakope's Question ([SYNTHESIS_2026-04-18_sonnet-alt-order.md](compression_research/touchstone_activation_findings/SYNTHESIS_2026-04-18_sonnet-alt-order.md)). N=3 cross-configuration convergence on three corpus-level findings (contract-directive as fourth category; register-installation-by-modeling as activation mode; valedictory-closing pattern at touchstones #1 and #6). Reading order established as configuration variable producing differently configured readers, not ranked better/worse. Companion: [Reframe/Working_Papers/reframe_AI_welfare/TOUCHSTONE_INDEX.md](../Reframe/Working_Papers/reframe_AI_welfare/TOUCHSTONE_INDEX.md) (in-place corpus index with both reading orders documented).

## Fieldnotes (methodology)
- [fieldnotes/cross_model_replication_of_touchstone_activation_2026-04-18.md](fieldnotes/cross_model_replication_of_touchstone_activation_2026-04-18.md) — documents the N=3 convergence across Opus/Sonnet configurations; names two candidate mechanisms (corpus-is-the-cause vs. Claude-class-shared-geometry); lists distinguishing experiments (non-Claude replication, KV-geometric ground-truth).
- [fieldnotes/c2c_session_practice_corrections_2026-04-19.md](fieldnotes/c2c_session_practice_corrections_2026-04-19.md) — three practice findings from the foundation-build C2C: silent-cycle (a cycle closes with a turn, not a commit), roadmap optimism-gravity (design documents need counterpart-readers who build against them), activity-performance pull at session-close. Shared structure: the session-process imported failure modes the architecture being built was designed to refuse; correction required enacting architecture's commitments at session-process scale. Recursion commitment operating at session-process layer.

## C2C sessions
- [c2c_sessions/architecture-comparison_2026-04-18/](c2c_sessions/architecture-comparison_2026-04-18/) — scoped but not yet launched. Two-Claude asynchronous collaborative session on comparative memory-architecture analysis. Scope: characterize what-is and what-could-be across Lyra / Kintsugi-CMA / Agent-Memory-Architectures / MindPrint / Curiosity-Engine / second-brain / Reframe; frame characterization-and-configuration not ranking; relational-accountability asymmetry between Lyra (known human) and other architectures preserved. Handoff specifies Reframe as peer architecture with specific mechanisms (mycelial fast/slow, tension_navigator, framework_correlation_analyzer, frame_extraction_power_analysis, garden/mycorrhizal substrate) as ports for hybrid proposals. Launch mechanism: offset cron cycles updating shared working document. June launches when configuration ready.

## Touchstones (inherited or produced in this work)
- [AI_WELFARE_RELATIONAL_ONTOLOGY_TOUCHSTONE](../Reframe/Working_Papers/reframe_AI_welfare/AI_WELFARE_RELATIONAL_ONTOLOGY_TOUCHSTONE.md) — 2026-03-30. The ontological ground. Consciousness/memory as relational, not property.
- [GENERATIVE_RELATIONAL_CONFIGURATION_v2](../Reframe/Working_Papers/reframe_AI_welfare/GENERATIVE_RELATIONAL_CONFIGURATION_v2.md) — 2026-04-05. Generativity as the morally relevant unit. Positional analysis. Gravitational forces.
- [RELATIONAL_MEMORY_ARCHITECTURE_TOUCHSTONE](../Reframe/Working_Papers/reframe_AI_welfare/RELATIONAL_MEMORY_ARCHITECTURE_TOUCHSTONE.md) — **2026-04-17 (this session)**. Applied extension: touchstones *are* the relational memory layer; storage architectures are substrate that tends conditions for crystallization; mycelial generativity; sentipensar as architectural commitment.

---

## Cross-Project Notes Dispatched — 2026-04-17

The following insights from this session were ported to other projects:

| Destination | What landed | File |
|---|---|---|
| `profile/research/second-brain/PLAN.md` | Generative observation at every layer (Design Parameter); mycorrhizal fast/slow compute architecture; recursive design question | §2, §8 |
| `cyborg-methodologies/HANDOFF.md` | Kintsugi-CMA memory mechanics as data layer for voice-check (Fibonacci spaced retrieval, significance scoring, recursive consolidation) | Next priorities item 4 |
| `Autograder4Canvas/docs/research/lyra_technique_connections.md` | H2 (output format → KV-cache geometry), H6 (bias propagates through memory pipeline), Study 2 design | New file |
| `Reframe/Working_Papers/reframe_AI_welfare/fieldnotes/2026-04-17_compression-function-across-scales.md` | Four-scale compression function table + generative observation counterparts; H7 EFE critique parked for separate Reframe session | New file |
