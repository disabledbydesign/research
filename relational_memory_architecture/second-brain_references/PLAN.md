# Second Brain / Context Mesh — Project Plan

**Status**: Research phase COMPLETE → moving to design phase  
**IDE**: Obsidian (confirmed; Logseq documented as alternative worth considering)  
**Home**: `/Users/june/Documents/GitHub/profile/research/second-brain/`  
**Last updated**: 2026-04-15

---

## 1. Problem Statement

### Core Problem A: Context Degradation
Rich context is the primary mechanism for countering normative gravity in AI collaboration. But context has weight, and as it grows, Claude's generative quality degrades — particularly for precise tasks like editing papers or grant applications.

The right question is not "how do we make context lighter" but **how do we structure context so retrieval matches the query pattern**. The research confirmed: context weight ≠ context structure. Well-structured context degrades less than flat context of the same size.

*Research finding*: The Capacity Building Plan's "relational architecture finding" (2026-04-13) established that **the relational network generates voice-accurate output, not factual completeness**. Stripping the connective tissue — through-lines, parallels, cross-references — produces generic output even with full factual coverage. This reframes the optimization target: always preserve the relational network, selectively load factual detail.

### Core Problem B: Nonlinear Knowledge Architecture
June's work is associative, relational, and mutually constitutive — not hierarchical or procedural. Standard PKM systems (Zettelkasten, PARA, "Building a Second Brain") are implicitly designed for neurotypical linear cognitive styles.

**Reframing "de-atomize"**: The right question isn't "how do we de-atomize context" but **how do we make relationships first-class, not second-class**. The atoms (notes, facts, claims) are still useful. What's missing is rich relationship metadata — typed edges, annotated connections, relationship reason.

*Research finding*: No existing PKM tool is designed explicitly for associative/nonlinear cognition. The nonwestern/decolonial/feminist traditions confirm this gap: zero personal PKM tools exist in Afrofuturist, Indigenous, feminist technoscience, or decolonial frameworks — despite rich theory. We're building something novel.

### Core Problem C: The Write Loop
Retrieval quality is downstream of write quality. Low-friction write is existential for a ND workflow. The write loop is the hardest part and should be solved first.

*Research finding*: The voice memo pipeline (`mlx_whisper` → transcription) is already the right instinct — lowest friction capture. The gap is what happens after transcription: currently ad hoc. Formalizing the ingest pipeline is the first build priority.

---

## 2. Design Parameters (Fixed)

These constraints hold regardless of what further design work finds:

- **IDE**: Obsidian as human-facing writing/capture environment
- **Voice-first write pipeline**: `mlx_whisper` → structured ingest is a first-class citizen
- **Relationships are first-class data**: connections between ideas carry metadata (type, reason, confidence). Wikilinks alone are insufficient.
- **Nonlinear retrieval**: associative + gap-finding queries, not just keyword/vector search
- **Values-at-query-time**: the system filters retrieval through theoretical commitments (CRT, disability justice, queer studies, AI welfare) — context is not epistemically neutral. Inspired by kintsugi-cma's BDI governance.
- **Generative observation at every layer** (Bloch, 2026-04-16): At every layer where compression could assert itself — routing, consolidation, retrieval, interface — the architecture must use generative/semantic observation rather than categorical compression. Compression reasserts normative gravity at any layer where it isn't actively resisted. This is an architectural commitment, not a stylistic preference. Corresponding to: routing (semantic intent reading, not keyword matching), consolidation (relational clustering, not categorical slotting), retrieval (relational specificity preserved), interface (generative description of state, not dashboard metrics). Source: liberation_labs/RESEARCH_NOTES.md.
- **AI-partnership model**: this is a shared context layer for human-AI collaboration, not "June's filing system"
- **Compile at write time**: synthesis happens at session end / ingest time, not at query time
- **Frictionless write is non-negotiable**: no decision points at capture time; structure is suggested, not required

---

## 3. Retrieval Scenarios

Confirmed workflows from session 2026-04-15. The system is designed backward from these:

### Confirmed scenarios:
1. **Job applications** — academic, tech, edtech, grant. Needs: relational core always loaded; heavy detail (publications, teaching, portfolio) on demand. *Note: editing a cover letter is different from drafting one — needs context isolation, not accumulation.*
2. **Research — AI welfare** — needs: theoretical through-lines, cross-project connections, working paper context
3. **Research — Autograder / normative gravity / Reframe** — needs: heterarchical scope navigation (Autograder insights ↔ AI welfare ↔ what is Reframe). **Key design question: how do agents quickly move between scopes/scales when projects inform each other?**
4. **Social media / disabled_by_design** — needs: voice context, relational core, story sections; NOT full technical detail
5. **Development (Reframe)** — large, complex, buggy project; needs: design rationale, current architecture state, theoretical commitments; NOT voice/social content
6. **Theory building** — "where does structural context delivery appear across projects?" — needs: concept tracking, cross-project relational query
7. **Editing mode** — minimum viable context per document; gets more skeletal as edits become more fine-grained; potentially uses subagents with more expansive context for verification
8. **Session startup** — compressed project state; what was open, what was parked, what's next

*New retrieval types are easy to add — they're defined in the schema document and require no code changes, just documentation.*

---

## 4. Research Phase — COMPLETE

All source notes at `research/sources/`. Index at `research/INDEX.md`.

### Key findings that shape the design:

**Architecture**: The kintsugi-cma + hipporag-catrag-kg stack (Liberation Labs / TH Coalition) already implements most of our design principles. June knows the person building it. This is the most relevant existing system and a potential collaboration.

**The configurator problem**: No existing PKM system conditions retrieval on *what you're currently trying to accomplish*. This is the central unsolved problem our design should address.

**Graph + vector hybrid beats either alone**: Confirmed across multiple empirical studies. Don't choose between semantic search and relational structure — use both.

**Karpathy wiki pattern**: Three-layer structure (raw sources / LLM-maintained wiki / schema document) is the closest existing model to what we're building. Key operations: ingest, query, lint. The schema document is the most important single artifact — it's a short markdown file that tells the LLM how the knowledge is organized.

**InfraNodus**: Only tool that makes structural gap identification computable. Gap = where connections are absent but could be productive. Critical for nonlinear, associative work.

**Temporal tracking** (Zep/Graphiti): Knowing *when* you believed something, when you changed your mind — essential for intellectual integrity and reconstructing reasoning paths.

**Nonwestern/feminist design constraints** (all four traditions confirm):
- Anti-hierarchy: web/spiral/network, not tree
- Anti-neutrality: classification embeds values; make them explicit
- Multi-ontology coexistence: notes simultaneously inhabit incommensurable frameworks
- Relational primacy: relationships before categories

**Most immediately implementable external resources**:
- TK Labels (localcontexts.org) — positionality metadata layer, installable today
- D'Ignazio & Klein's Data Feminism — 7 design constraints, free at data-feminism.mitpress.mit.edu
- Bauwens et al. 2026 pluriversal typology — diagnostic for every design decision

### What doesn't exist yet (we're building into this space):
1. PKM designed for associative/nonlinear cognition
2. Genuinely rhizomatic architecture
3. Configurator-aware retrieval
4. Spaced repetition applied to connections rather than facts
5. Diffractive retrieval — surfaces productive contradictions, not similarity clusters
6. Prediction error as a curation signal
7. Any personal PKM grounded in nonwestern epistemological tradition

---

## 5. Local Drive Audit — NOT YET DONE

Before design phase, assess what knowledge assets exist locally:

### Known repositories (to audit):
- `/Users/june/Documents/GitHub/profile/` — central identity, briefing, publications deep read
- `/Users/june/Documents/GitHub/reframe/` — AI welfare research, working papers, experiments, context scheduler, PARK system
- `/Users/june/Documents/GitHub/disabled_by_design/` — voice memos, story prompt responses
- `/Users/june/Documents/GitHub/` — Autograder project (location TBD)
- `/Users/june/Documents/Filing/Job Search/` — job search materials
- Zotero library (MCP available — `mcp__zotero__zotero_list_libraries`)
- MemPalace (MCP available — needs initialization)
- Graphify knowledge graphs (exist in each project's `graphify-out/`)

### Audit questions:
- What format are these in? (md, pdf, voice transcripts, jupyter notebooks)
- What's already structured vs. flat?
- What's in Zotero? What's in MemPalace?
- What do the Graphify graphs reveal about structure?
- What's the total token footprint of the knowledge base?

---

## 6. Design Phase — Parameters

*Hook in Reframe during this phase. Read Reframe's architecture before the design session.*

### Key design questions to answer:
1. **The configurator**: How does the system know what you're currently trying to accomplish? What triggers a context-mode switch?
2. **Heterarchical scope navigation**: When working on Autograder, how does the system surface AI welfare connections and vice versa? Do we need multi-scale agents?
3. **The schema document**: What does June's vault-schema.md actually say? This is the single most important design artifact. Cannot be researched — requires June's judgment.
4. **Values.json**: What are the BDI entries? Draft: anti-normative gravity, structural violence as analytical frame, recognition politics, disability justice as epistemological foundation, queer temporality. These are retrievable frameworks, not decorative metadata.
5. **Relationship types**: What are the typed edges? Draft: informs, contradicts, extends, applies-to, challenges, cross-references, is-parked-thread-of
6. **Obsidian vs. Logseq final decision**: Block-level granularity matters for associative connection. Worth a 10-minute comparison before committing.
7. **Reframe integration**: The Reframe architecture (context scheduler, warm tiers, PARK, thread graph) is the design input for what we can't yet build. How does this system connect to or share infrastructure with Reframe?
8. **Quick fix layer**: Implement kintsugi-cma + hipporag-catrag-kg as near-term backend while designing the full system?

### Theoretical frames to draw on (confirmed by research):
- Mycilial network (distributed, no center) — better frame than "second brain"
- Rhizome (Deleuze/Guattari) — aspirational architecture; Roam and TiddlyWiki as partial implementations to study critically
- HippoRAG (hippocampal indexing) — neuroscience-grounded associative memory
- BQF temporal dissonance — non-linear temporal tagging
- Barad's diffraction — diffractive retrieval as a distinct query mode

---

## 7. Build Phase — Parameters Only

*To be fleshed out after design phase.*

### Quick-fix tier (before full build):
- **Immediate**: `mempalace init && mempalace mine` (2 commands, already installed)
- **This week**: Obsidian vault with Karpathy three-layer structure — `raw/`, `wiki/`, `vault-schema.md`, `log.md`. Manual write loop. No code.
- **Before full build**: Talk to lib lab person about kintsugi-cma + hipporag-catrag-kg. Evaluate "Seed" SQLite tier for laptop deployment.

### Likely build components:
- Obsidian vault setup + vault-schema.md
- kintsugi-cma backend (values alignment, significance scoring, temporal tagging, hybrid retrieval)
- hipporag-catrag-kg extension (associative/relational retrieval via PPR)
- InfraNodus integration (structural gap analysis)
- Voice memo pipeline formalization (mlx_whisper → ingest)
- Configurator layer (novel; no existing implementation to borrow from)
- Connection to MemPalace, Zotero MCP

### Build constraints:
- Build incrementally — each component testable standalone
- Low-friction write is non-negotiable; if write takes >30 seconds, it won't happen
- Don't break existing workflows
- No GPU requirement — everything must run on available hardware

---

## 8. Open Questions / PARKed Threads

**Architectural:**
- Heterarchical design: when working in one project, how does the system surface relevant cross-project connections without flooding context?
- Mycilial/slow multi-call synthesis: can we use Reframe's slow synthesis approach — multiple targeted calls that synthesize incrementally — instead of loading all context at once?
- Training vs. architecture: we're building memory architecture, not training. V-JEPA concepts are vocabulary imports, not infrastructure.
- **Mycorrhizal compute architecture** (Bloch, 2026-04-16): Generative observation is more expensive than keyword matching. The solution is fast/slow division of labor — a lightweight aux LLM (~32B, ~32GB VRAM) handles routing, classification, and metadata in background; main model handles expensive semantic heavy lifting. This makes generative observation economically viable at scale. Infrastructure plan needs two budget lines: main-model inference + aux-model inference. Both are load-bearing for the values architecture. Reframe already implements this pattern; the Profile architecture should treat the mycorrhizal layer as a first-class design commitment, not an optimization afterthought.
- **Recursive design question**: In designing this system, in what ways will our own choices subordinate progressive values to other logics? This question should be put to Reframe at high power before finalizing architecture — not rhetorical, genuinely architectural.

**Design:**
- Anti-normative gravity as values.json entry — this should be a first draft in the design session
- Semantic gaps in writing (job materials especially) — gap detection at the document level, not just the knowledge graph level
- Diffractive retrieval as a query mode — how is it implemented? What does it return?
- TK Labels as positionality metadata layer — straightforward to add; when?
- Editing mode granularity: how skeletal does context get for fine-grained edits? At what point does a subagent with wider context handle verification?

**Process:**
- Conversation with lib lab person — potential collaboration on kintsugi-cma extension
- Reframe architecture documentation — should be read and formally documented before design session
- Local drive audit — needed before we know the full scope of what to ingest

---

## Appendix: Vocabulary

- **Context mesh** (vs. second brain): distributed, multiply-linked, no single root. Better frame.
- **Relational architecture**: the connective tissue that generates voice-accurate output; through-lines + parallels + cross-references.
- **Context isolation**: retrieving ONLY what's needed for a specific task (editing mode). Inverse of context accumulation.
- **Configurator**: LeCun's term — the module that sets the current task objective, conditioning all retrieval and action.
- **Diffractive retrieval**: query mode (from Barad) that surfaces productive contradictions rather than similarity clusters.
- **Significance scoring**: weighting memories by relevance + recency + connection density, not just recency.
- **Compile at write time**: synthesis happens at session end / ingest, not at query time.
- **Values-at-query-time**: the system filters retrieval through theoretical commitments, not just semantic similarity.
- **Hub node drift**: PageRank failure mode where highly-connected concepts dominate retrieval regardless of query intent. CatRAG addresses this.
