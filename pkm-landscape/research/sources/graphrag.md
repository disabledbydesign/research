# GraphRAG — Community-Hierarchical Knowledge Graph

**Paper**: "From Local to Global: A Graph RAG Approach to Query-Focused Summarization" — https://arxiv.org/abs/2404.16130  
**By**: Microsoft Research  
**GitHub**: https://github.com/microsoft/graphrag (Microsoft)  
**Project page**: https://www.microsoft.com/en-us/research/project/graphrag/  
**Survey**: https://dl.acm.org/doi/10.1145/3777378 (ACM TOIS graph RAG survey)  
**Curated resource list**: https://github.com/DEEP-PolyU/Awesome-GraphRAG

---

## What it does

GraphRAG builds a community-hierarchical knowledge graph from raw documents, then uses that structure for retrieval. Unlike flat RAG (chunk text → embed → retrieve), GraphRAG:

1. Extracts entities and relationships from documents
2. Groups related entities into communities (using graph clustering algorithms)
3. Generates summaries at each community level — from fine-grained to global
4. At retrieval time, queries the appropriate level of the hierarchy

---

## The local vs. global distinction

**Flat RAG** is good at "local" queries — specific factual questions about specific documents.  
**GraphRAG** is designed for "global" queries — "what are the major themes across all these documents?" "what connects these seemingly separate ideas?"

For a researcher with sprawling work across many projects and years, global sensemaking queries are often more valuable than local factual retrieval.

---

## Key empirical finding

- **Hybrid (text + graph)** substantially outperforms either alone
- Graph-only RAG is only ~5% better than text-only RAG
- **The combination** is where significant accuracy improvements appear

This directly supports the architecture in our synthesis: **don't choose between vector search and graph structure — use both.**

---

## LazyGraphRAG (2025 update)

A new variant reduces indexing cost to **0.1% of full GraphRAG** while preserving most of the benefits. Available in Microsoft Discovery / Azure. This addresses the original GraphRAG's main limitation (expensive upfront indexing of large corpora).

---

## Relevance to our build

### High relevance for cross-project synthesis
June's work spans disability justice, AI welfare, pedagogy, job search, and Autograder development. These aren't siloed — they connect through through-lines (structural violence, recognition politics, distributional gravity). GraphRAG's community detection and global summarization is exactly what you'd want for "what connects AI welfare research to the Autograder findings?"

### Practical consideration: indexing cost
For a personal knowledge vault (not a million-document corpus), full GraphRAG indexing is feasible. LazyGraphRAG makes it even more so. But it still requires infrastructure (the Microsoft stack: Python, Neo4j or Azure).

### What it doesn't address
- Doesn't handle the write/ingest loop (only builds graphs from existing documents)
- Doesn't model temporal belief changes
- Doesn't have the ND-specific design properties (frictionless write, active resurfacing)
- The community detection algorithm may not respect June's theoretical frameworks — communities emerge from co-occurrence, not from epistemological alignment

---

## The InfraNodus comparison

Both GraphRAG and InfraNodus work by representing knowledge as a graph and finding structure. Key differences:

| Dimension | GraphRAG | InfraNodus |
|-----------|----------|------------|
| Purpose | Retrieval from large corpora | Gap identification in knowledge networks |
| Scale | Enterprise, millions of documents | Personal PKM, thousands of notes |
| Finding | "What's related" | "What's missing" |
| Implementation | Full ML pipeline | Obsidian plugin |
| Open source | Yes (Microsoft) | Yes |

For our build: **InfraNodus for gap analysis, GraphRAG-inspired community detection for synthesis queries.** They're complementary, not competitive.
