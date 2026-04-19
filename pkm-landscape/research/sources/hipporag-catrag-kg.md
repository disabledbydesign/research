# HippoRAG/CatRAG Knowledge Graph Extension

**Source**: https://github.com/Liberation-Labs-THCoalition/Agent-Memory-Architectures/tree/main/hipporag-catrag-kg  
**By**: Liberation Labs / TH Coalition  
**Relationship**: Explicitly designed as an extension of kintsugi-cma  
**Status**: Production-deployed (reportedly processed 100 memories → 788 entities + 25,290 triples)  
**Date assessed**: 2026-04-15

---

## What problem it solves

From the DESIGN.md: "The existing kintsugi-cma memory system excels at direct recall (dense + lexical retrieval) but fails at **associative retrieval** — answering questions like 'what connects Project Alpha to the budget shortfall?' These require explicit representation of relationships between entities."

This is exactly our design constraint: **relationships are first-class data.**

---

## How it works

Three-stage pipeline:
1. **Extraction**: spaCy NER identifies entities and co-occurrence patterns from memory content
2. **Storage**: Subject-predicate-object triples + entity mentions stored in three PostgreSQL tables (`kg_entities`, `kg_triples`, `kg_entity_mentions`)
3. **Retrieval**: Query entities become seed nodes → Personalized PageRank (PPR) ranks connected memories → fuses with dense and lexical search via Reciprocal Rank Fusion

**Three retrieval signals fused:**
- Dense vector search (pgvector)
- Lexical search (BM25/tsvector)
- Graph traversal via PPR

Results merge via **Reciprocal Rank Fusion** — graph boosts structurally connected memories without replacing existing retrievers.

---

## Key innovations

### CatRAG query-aware edge weighting
Before running PPR, the system reweights graph edges based on their relevance to the current query. This prevents "hub node drift" — highly-connected entities dominating PageRank regardless of query relevance. Most RAG systems don't address this problem. Applied to our use case: "distributional gravity" and "structural violence" are hub nodes in June's knowledge graph — without CatRAG weighting, they'd dominate every retrieval regardless of context.

### HippoRAG neuroscience grounding
Based on HippoRAG 2 paper — models long-term human memory via neuroscience principles (hippocampal indexing for episodic and associative memory). The hippocampal metaphor is apt: the hippocampus doesn't store memories, it indexes connections between them.

### Open predicates (not fixed ontology)
Agent memory is unpredictable; fixed schemas constrain. Subject-predicate-object triples with open predicates allow the relationship types to emerge from the content rather than being pre-specified.

---

## Design principles

1. **Additive, not invasive** — adds new tables and retrieval path without modifying kintsugi-cma
2. **PostgreSQL-native** — no Neo4j needed at this scale; SQL-based PPR handles ~5,000 entities
3. **CPU-friendly** — spaCy medium model, no GPU required, no API dependency
4. **Graceful degradation** — if KG fails, dense + lexical search still work

---

## Performance envelope

- Ingest overhead: <100ms per memory
- Retrieval latency: <30ms (PPR on 1000 nodes takes <5ms in NumPy)
- Memory: ~1.2GB baseline; adjacency matrix for 1000 entities = 8MB
- Scale limit: ~5,000 entities before needing sparse matrices

Target hardware: i5 CPU, 8GB RAM, entry-level GPU (conservative, accessible).

---

## Relevance to our build

**Very high.** This is the most complete implementation of the "relationships as first-class data" principle we've found. Combined with kintsugi-cma (values-aligned retrieval), the full stack gives us:
- Values-at-query-time (kintsugi-cma BDI governance)
- Significance scoring + temporal tagging (kintsugi-cma)
- Hybrid retrieval: vector + BM25 + graph (both architectures)
- Associative/relational retrieval via PPR (hipporag-catrag-kg)
- Hub node drift prevention (CatRAG)
- Episodic memory via HippoRAG neuroscience grounding

**The combination**: kintsugi-cma + hipporag-catrag-kg + Obsidian vault = a functionally complete second brain that already implements most of our design principles.

**The person building this**: June knows them personally. This is a potential collaboration point, not just a research reference.

---

## What it doesn't yet address

- Neurodivergent-specific design (frictionless write, active resurfacing)
- The configurator problem (context-aware retrieval based on current task)
- Growth stage labeling / digital garden epistemics
- Voice memo ingest pipeline
- The Obsidian integration layer
