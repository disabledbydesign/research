# Dispatch Notion Memory

**Source**: https://github.com/Liberation-Labs-THCoalition/Agent-Memory-Architectures/tree/main/dispatch-notion-memory  
**By**: Liberation Labs / TH Coalition  
**Status**: Phase 1 focused (core store/search/retrieve)  
**Date assessed**: 2026-04-15

---

## What it is

A persistent memory system that integrates Discord/n8n input with **Notion as the central store**, using SQLite-vec for fast local semantic search and spaCy for entity extraction. Organized around PARA structure (Projects, Areas, Resources, Archive).

---

## Architecture

- **Primary store**: Notion as source-of-truth and human interface
- **Embedding cache**: SQLite-vec for local, fast semantic search
- **Entity extraction**: spaCy NER → knowledge graph readiness
- **Ingest path**: Discord voice/text → n8n → Notion inbox → PARA categorization
- **Significance scoring**: 0.0–1.0 values governing memory decay behavior
- **Phased roadmap**: Phase 1 (core store/search/retrieve) → Phase 2 (significance-aware decay + consolidation) → Phase 3 (KG traversal)

---

## Relevance to our build

**Medium.** The Notion-centric architecture doesn't fit our Obsidian design. But two concepts are worth noting:

1. **Significance-based decay**: memories that aren't accessed or reinforced decay over time. Prevents the system from treating all memories as equally current. We should incorporate this principle.

2. **n8n as automation layer**: the Discord → Notion ingest pipeline is the equivalent of our voice memo → Obsidian pipeline. n8n (or a simpler equivalent) could handle that automation without custom code.

The PARA structure (Projects/Areas/Resources/Archive) is Tiago Forte's framework — widely adopted but implicitly hierarchical and linear. Not the right model for nonlinear/relational work. Worth noting as a contrast case.
