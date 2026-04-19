# Kintsugi-CMA — Cognitive Memory Architecture

**Source**: https://github.com/Liberation-Labs-THCoalition/Agent-Memory-Architectures/tree/main/kintsugi-cma  
**By**: Liberation Labs / TH Coalition  
**Status**: Phase 1 Complete  
**Date accessed**: 2026-04-15

---

## What it is

A values-aligned memory system for AI agents. Built by a coalition explicitly oriented toward mutual aid, nonprofits, cooperatives, and advocacy groups. The name "kintsugi" (the Japanese art of repairing broken pottery with gold — making the repair visible and beautiful) signals an intention: memory is not neutral storage, it's a practice of restoration and integrity.

---

## How it works

**Three-stage pipeline:**
1. Atomic fact extraction from input
2. Significance scoring with temporal tagging
3. Hybrid retrieval — combines vector search (pgvector), keyword matching (BM25), and symbolic ranking

**BDI Governance layer:** Beliefs-Desires-Intentions framework encodes organizational values in a hot-reloadable `VALUES.json`. These constraints are enforced *at query time* — the system doesn't just store context, it filters retrieval through values alignment.

**Security layer:** PII redaction, content monitoring, intent capsule verification before any memory operation. Per-organization isolation via row-level database policies.

**Tiered deployment:**
- Seed / SQLite — laptop/minimal
- Soil / PostgreSQL — medium
- Grove / full stack with pgvector — production

---

## Key architectural ideas

### Values-at-query-time
Most memory systems are epistemically neutral — they return what's most similar. Kintsugi enforces organizational values at retrieval, not just at storage. This is unusual and potentially important for a system built around specific theoretical commitments (CRT, disability justice, etc.).

### Significance scoring + temporal tagging
Memories aren't equal — some are more significant, and significance decays or grows over time. This is better than flat vector similarity.

### Intent verification
Before retrieval, the system checks the *intent* of the query — not just what's being asked, but why. This is relevant for the "context isolation" problem: you don't want grant-writing context bleeding into code-debugging context.

---

## Relevance to our build

**High relevance** on:
- Values alignment as an architectural principle (not just preference) — this maps directly to designing a system that reflects CRT, disability justice, etc.
- BDI governance for intent-based retrieval — could inform how we route different retrieval scenarios
- Significance scoring — non-flat memory hierarchy

**Questions it raises for us:**
- What are OUR values.json entries? (theoretical commitments, epistemic priorities)
- How do we define "significance" for June's knowledge assets?
- Can we adapt the intent verification layer to the retrieval scenarios we've defined?

**What it doesn't address:**
- Neurodivergent/nonlinear retrieval patterns
- Relational knowledge (relationships between nodes, not just nodes)
- Voice-first write pipeline
- Obsidian integration

---

## Technical stack

FastAPI, SQLAlchemy, PostgreSQL, Redis, pgvector, Alembic for migrations. Production-grade, not a toy.
