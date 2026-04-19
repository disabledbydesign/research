# Session Handoff — 2026-04-15

**For**: Next instance picking up this project  
**From**: Session that completed the research phase  
**Context**: June is Dr. L. June Bloch — read `/Users/june/Documents/GitHub/profile/JUNE_BLOCH_AGENT_BRIEFING.md` before doing any work related to her professional identity. Global behavior instructions at `~/.claude/CLAUDE.md`.

---

## What happened this session

We completed the research phase for a second brain / context mesh project. Started with June's brief, conducted parallel research using multiple subagents, and documented 16 sources in `research/sources/`. The research phase is now substantially complete.

**Full research directory**: `/Users/june/Documents/GitHub/profile/research/second-brain/`  
**Source index**: `research/INDEX.md` — read this first for a fast overview  
**Updated plan**: `PLAN.md` — reflects all research findings  
**Working synthesis notes**: `research/synthesis/overview.md` — written mid-session, treat as working notes

---

## The most important things to know

### 1. This project connects to the Capacity Building Plan
Read `/Users/june/Documents/GitHub/profile/CAPACITY_BUILDING_PLAN.md` before designing anything. It has a Workstream C (memory architecture) that is directly relevant. Key finding from that plan: **the relational network generates voice-accurate output, not factual completeness.** Stripping through-lines and cross-references produces generic output even with full factual coverage.

### 2. The lib lab stack is the most relevant existing system
Liberation Labs / TH Coalition built two architectures that together implement most of our design principles:
- `kintsugi-cma`: values-aligned memory, BDI governance, significance scoring, temporal tagging, hybrid retrieval
- `hipporag-catrag-kg`: associative retrieval via Personalized PageRank + CatRAG edge weighting (prevents hub node drift)

Combined, they address: values-at-query-time, relational retrieval, temporal tracking, hybrid vector+graph. **June knows the person building this** — worth a conversation.

Repo: https://github.com/Liberation-Labs-THCoalition/Agent-Memory-Architectures

### 3. The configurator problem is the central unsolved challenge
From LeCun's V-JEPA work: a configurator module determines *what you're currently trying to accomplish*, conditioning all retrieval and action. **No existing PKM system implements this.** Every design decision about retrieval should be framed as: "how does the system know what the user is currently doing?" This is the novel contribution our design needs to make.

### 4. Reframe has what we want to build
Reframe (June's project at `/Users/june/Documents/GitHub/reframe/`) already has: context scheduler (signal-weighted, penalizes recency, prioritizes framework dropout and revision chains), warm tier compression, PARK system, thread graph. The second brain is partly about extending these principles beyond Reframe to all of June's work. **Read the Reframe architecture before doing design work.**

### 5. The vocabulary
- **Context mesh** (not "second brain") — distributed, no single root
- **Relational architecture** — the through-lines and cross-references that generate voice
- **Context isolation** — editing mode: minimum viable context per document
- **Values-at-query-time** — BDI governance filters retrieval through theoretical commitments
- **Configurator** — what the system knows you're currently trying to do
- **Diffractive retrieval** — surfaces productive contradictions, not similarity clusters
- **Compile at write time** — synthesis happens at ingest/session end, not at query time

---

## What June wants to do next (in order)

### Immediate quick fixes (before design session)
1. `mempalace init && mempalace mine` — 2 commands, already installed as MCP
2. Set up Obsidian vault with Karpathy three-layer structure: `raw/`, `wiki/`, `vault-schema.md`, `log.md` — manual, no code

### Before full design session
3. Read Reframe architecture and formally document what it has
4. Do the local drive audit (PLAN.md §5 has the question list)
5. Talk to lib lab person about kintsugi-cma + hipporag-catrag-kg

### The design session itself
- Hook in Reframe — it's the design input for what we can't yet build
- First task: draft the vault-schema.md — the single most important artifact
- Draft values.json entries (anti-normative gravity, structural violence, recognition politics, disability justice, queer temporality)
- Define relationship types (typed edges)
- Decide Obsidian vs. Logseq (block-level granularity matters for associative work)
- Address heterarchical scope navigation (how Autograder ↔ AI welfare ↔ Reframe connections surface without flooding context)

---

## PARKed threads from this session — don't lose these

**Heterarchical design**: When working in Autograder, insights from AI welfare are relevant and vice versa. Do we need a heterarchical agent design where agents can quickly move between scopes/scales? This may be a core architectural question. Maps onto GraphRAG community hierarchy + the configurator problem.

**Mycilial/slow multi-call synthesis**: June suggested using Reframe's slow synthesis approach — multiple targeted calls that synthesize incrementally — as an alternative to loading all context at once. Potentially changes the whole architecture. Explore in design session.

**Semantic gaps in job materials**: Gap detection at the document level (what's structurally absent from this cover letter?) not just the knowledge graph level. Connects to the configurator problem — the system needs to know you're writing a job application to surface the right gaps.

**Anti-normative gravity as values.json entry**: This should be a first draft item in the design session. "Distributional gravity" and "structural violence" as named BDI entries that shape what the system treats as relevant.

**Diffractive retrieval**: From Barad — surfaces productive contradictions, not similarity clusters. How is this implemented concretely? What does it return? Open design question.

---

## What's still open in research

| Gap | Status | Priority |
|-----|--------|----------|
| Reframe architecture documentation | ❌ Not done | High — needed before design |
| Local drive audit | ❌ Not done | High — needed before design |
| Episodic memory paper (arXiv 2502.06975) | ❌ Unread | Medium |
| TiddlyWiki + Roam as rhizomatic reference cases | ❌ Deferred | Design phase |
| MemPalace documentation | ❌ Deferred | Design phase |

---

## Research files to read for fast context

1. `research/INDEX.md` — all 16 sources in one table with relevance ratings
2. `research/sources/kintsugi-cma.md` + `hipporag-catrag-kg.md` — the lib lab stack
3. `research/sources/vjepa-predictive-architectures.md` — the configurator problem, WKM
4. `research/sources/infranodus.md` — structural gap identification
5. `research/sources/karpathy-llm-wiki.md` — the write-time compilation model
6. `research/sources/decolonial-feminist-pkm-landscape.md` — epistemological design constraints
7. `research/sources/neurodivergent-pkm-landscape.md` — ND design constraints
8. `CAPACITY_BUILDING_PLAN.md` (in profile root) — Workstream C, relational architecture finding

Do NOT try to read all source notes at once. The INDEX tells you which ones are most relevant to the current task.
