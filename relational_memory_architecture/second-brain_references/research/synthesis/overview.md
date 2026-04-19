# Research Synthesis — Second Brain / Context Mesh

**Written**: 2026-04-15  
**Sources**: kintsugi-cma, karpathy-llm-wiki, zep-graphiti, mem0, a-mem, infranodus, digital-garden-appleton, obsidian-ai-integration, neurodivergent-pkm-landscape  
**Cross-reference**: `/Users/june/Documents/GitHub/profile/CAPACITY_BUILDING_PLAN.md` (Workstream C)

---

## What we're actually building

This is NOT a fresh start. The Capacity Building Plan (2026-04-13, revised today) has a Workstream C specifically about memory architecture, and it explicitly derives its design principles from **Reframe's existing infrastructure**:

> "Reframe's architecture teaches us several things that apply even though we can't port the infrastructure directly."

Reframe already has: context scheduler, warm tier compression, PARK system, thread graph, exchange-level tracking. The capacity building plan is a simplified port of those principles to Claude Code. The second brain project we're designing today is the *ambitious version* — building something that more fully realizes what Reframe has, but across all of June's work, not just within one project.

**The relationship**: Workstream C is the minimal viable version. The second brain is the full build. They should converge, not diverge.

---

## Four design principles confirmed by research

These are principles that *both* the capacity building plan and the external research independently arrive at:

### 1. Compile at write time, not query time
- **Capacity building plan**: "Pay the synthesis cost at session end, not session start of the next conversation."
- **Karpathy wiki**: Ingest operation synthesizes at write time; queries hit pre-compiled wiki pages, not raw sources.
- **MemGPT/Letta**: Working memory (RAM) holds compiled summaries; raw content is "on disk."
- **Design implication**: The session-wrapup skill IS a write-time compilation step. The wiki ingest IS a write-time compilation step. These should be unified.

### 2. Signal-weighted relevance, not recency
- **Capacity building plan**: "Reframe's context scheduler penalizes recency (`temporal_recency: -0.1`) and prioritizes framework dropout, revision chains, parked connections."
- **Zep/Graphiti**: Temporal knowledge graph tracks when beliefs changed, not just what was most recent.
- **A-MEM**: Memory evolution — new information can update old nodes, not just append. The most significant connections get reweighted.
- **Design implication**: The auto-memory system's flat file structure is recency-biased. The upgrade is significance scoring + temporal metadata, not just more files.

### 3. Relational architecture over factual completeness
- **Capacity building plan (key finding)**: "The cross-references and through-lines in the briefing are not just informational — they are the relational architecture that generates voice-accurate output. Stripping them produces generic output."
- **InfraNodus**: Structural gap analysis finds where relational connections are absent. The relationships ARE the knowledge.
- **A-MEM**: Atomic notes alone aren't enough — it's the memory evolution and connection generation that produces insight.
- **Design implication**: "De-atomize context" is the wrong framing. The right framing is: **make relationships first-class data, not implicit side effects**. Typed connections with annotations are the upgrade from wikilinks.

### 4. Nothing disappears silently
- **Capacity building plan**: Reframe's PARK system, session-wrapup skill — "when session context is lost to compaction, the important parts should have been captured before they disappeared."
- **Karpathy wiki**: lint operation — periodic health checks for orphan pages, stale content.
- **Digital garden**: Growth stage labeling (seedling/budding/evergreen) — epistemic status is explicit, not implicit.
- **Design implication**: Two mechanisms needed: (a) explicit capture at session end, (b) periodic health check for what's gone stale or orphaned.

---

## What the external research adds that the capacity building plan doesn't yet have

### InfraNodus — the structural gap finder
This is the biggest new piece. InfraNodus applies network science to a knowledge vault and identifies **structural gaps** — places where connection is absent but could be productive. This is the computational implementation of "what haven't I thought about yet."

The capacity building plan talks about relational architecture as the voice-generating mechanism, but doesn't yet have a mechanism for *discovering* missing relational connections. InfraNodus fills this gap.

**Integration path**: InfraNodus Obsidian plugin as a periodic analysis tool. Run it when starting a new research project, or when doing a theory-building session. The output (bridging concepts, structural gaps) feeds back into the knowledge graph as "suggested connections" — seedlings for the human to evaluate.

### Values-at-query-time (kintsugi-cma)
The capacity building plan focuses on relational density but doesn't address *epistemological alignment* at retrieval time. Kintsugi-CMA filters retrieval through a values framework (BDI governance, VALUES.json). For a researcher whose work is explicitly grounded in CRT, disability justice, and queer studies, this matters: the system shouldn't return context that embeds normative assumptions without flagging it.

**Simpler implementation**: Rather than a full BDI system, this could be implemented as: (a) tagging memories/wiki pages with epistemological stance, (b) retrieval that prioritizes context tagged with relevant theoretical frameworks, (c) a lint check that identifies wiki pages with no theoretical framework tags.

### Temporal belief tracking (Zep/Graphiti)
The capacity building plan's session-wrapup captures decisions and connections, but doesn't model *when* a belief was held vs. when it changed. For a researcher reconstructing the intellectual history of a project (e.g., for a paper introduction), knowing "I believed X when I wrote the first draft, changed my view after reading Y" is essential.

**Simple implementation**: Date metadata on belief-state changes (not just note creation dates). A `belief_updated: 2026-01-15` frontmatter field. Log.md as Karpathy proposes — append-only chronological record.

### Neurodivergent design constraints
The capacity building plan is strong on the relational architecture and context management but doesn't foreground ND-specific design constraints. From the research:
- **Frictionless capture is existential** — any decision point at write time means it won't happen
- **Novelty accommodation** — the system should surface unexpected connections (not just confirm known ones)
- **Active resurfacing** — out-of-sight/out-of-mind is a real failure mode; the system needs to push old material back to the surface

These apply to both the write loop design and the health check/lint mechanism.

---

## Architecture picture emerging from synthesis

The architecture that emerges from combining the capacity building plan + external research:

### Layer 1: Write / Capture
- **Voice memo pipeline** (existing, needs formalization): `mlx_whisper` → transcription → ingest
- **Session wrapup** (capacity building plan, Opus required): compile at session end, not query time
- **Wiki ingest operation** (Karpathy): new source → synthesize → update relevant pages simultaneously
- **No decision points at write time** (ND constraint): structure is suggested, not required

### Layer 2: Storage / Structure
- **Obsidian vault** as source-of-truth (local-first markdown)
- **Three-layer schema** (Karpathy): raw sources (immutable) / wiki (LLM-maintained) / schema config
- **Growth stage labeling** (digital garden): seedling/budding/evergreen on every note
- **Typed relationships** (beyond wikilinks): connection annotations with type and reason
- **Temporal metadata** (Zep-inspired): belief state dates, not just creation dates
- **Log.md** (Karpathy): append-only chronological record
- **Epistemological stance tags** (kintsugi-inspired): which theoretical framework does this belong to?

### Layer 3: Retrieval
- **Retrieval profiles** (capacity building plan, Workstream A): load relational core always, load detail per task type
- **Signal-weighted, not recency-biased**: significance scoring on memories
- **InfraNodus gap analysis**: periodic structural gap identification
- **Lint / health check** (Karpathy): orphans, stale content, broken connections
- **Context isolation mode**: for editing tasks, retrieve ONLY what's needed — quarantine from full context

### Layer 4: External AI integration
- **Obsidian MCP server** (Local REST API plugin): Claude reads/writes vault during sessions
- **Direct file access** for large-scale retrieval (external RAG pipeline if needed at scale)
- **MemPalace** (already installed): semantic retrieval across conversations

---

## What doesn't exist yet (genuine opportunities)

1. **Genuinely rhizomatic architecture** — no one has implemented it. The aspiration: multiple entry points, no hierarchy, productive rupture between disconnected clusters. InfraNodus + typed relationships gets closest.

2. **Spaced repetition applied to connections** — SR systems surface individual facts. No system surfaces *dormant connections between ideas*. This is the most interesting gap.

3. **Novelty-accommodation in retrieval** — retrieving what you DON'T know is connected yet. InfraNodus does this structurally; a temporal version would surface connections you made a long time ago and haven't visited.

---

## Open questions for design phase

1. **Obsidian vs. Logseq**: Block-level granularity (Logseq) vs. file-level (Obsidian). For associative thinking, linking a *specific claim* rather than a whole document matters. Worth a decision before committing.

2. **Where does this live relative to Workstream C?** Workstream C is the minimal viable version. This is the full build. How do we sequence them — implement Workstream C first as a foundation, or design the full system and implement Workstream C as the first slice?

3. **Reframe integration**: The capacity building plan says not to port Reframe's infrastructure directly. But now that we have a more complete picture of what the full second brain looks like — is there a path to actually sharing infrastructure? Or do they remain parallel?

4. **The schema document**: The most important single artifact in the Karpathy pattern is the schema document that tells the LLM how the wiki is organized. What does June's schema say? This is the design work that can't be researched — it requires June's judgment about what her knowledge architecture should look like.

5. **V-JEPA / predictive architectures**: Research pending from a running agent. May add conceptual vocabulary for the "retrieve by predicting what's missing" idea.
