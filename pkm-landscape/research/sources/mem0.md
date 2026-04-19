# Mem0 — Dual-Store Memory Layer

**Source**: https://arxiv.org/abs/2504.19413  
**GitHub**: https://github.com/mem0ai/mem0  
**Website**: https://mem0.ai  
**Type**: arXiv paper (2025) + open source production system  
**Assessment**: Best documented performance numbers, easiest integration

---

## What it is

A dual-store memory architecture: vector database + knowledge graph. Converts conversation messages into atomic memory facts. Designed to be a drop-in layer for any LLM app.

---

## Key results

- **26% accuracy boost** vs OpenAI's memory feature on LOCOMO benchmark (66.9% vs 52.9%)
- **91% lower p95 latency** vs alternatives
- **90% token savings** compared to full-context approaches

---

## Architecture

1. Messages → atomic memory facts (LLM extracts)
2. Stored in both vector DB (semantic search) and knowledge graph (relational)
3. Retrieval: hybrid query across both stores
4. "Single line of code" integration claim

---

## Relevance to our build

**High for integration pragmatics.** If we're layering on top of existing workflows rather than rebuilding from scratch, Mem0's easy integration path is appealing. 

Specific fit:
- The **atomic memory facts** approach is essentially what our current auto-memory system tries to do manually — Mem0 does this automatically from conversation
- The **90% token savings** directly addresses the context degradation problem
- The **dual-store** (vector + graph) is the hybrid approach that the survey literature says wins empirically

**Concern**: Self-reported benchmarks. The 26% improvement claim needs independent verification. The LOCOMO benchmark tests personal assistant tasks — less clear how it generalizes to research use cases.
