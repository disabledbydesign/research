# Zep / Graphiti — Temporal Knowledge Graph

**Source**: https://arxiv.org/abs/2501.13956  
**By**: Zep team  
**Type**: arXiv paper (January 2025) + production system  
**Website**: https://blog.getzep.com  
**Assessment**: Strongest empirical results for temporal reasoning tasks

---

## What it is

A temporal knowledge graph architecture for agent memory. Core component is **Graphiti** — a graph that tracks *when* facts were established, modified, or contradicted. Unlike standard KGs that store timeless facts, Graphiti maintains temporal metadata on every edge.

---

## Key results

- **94.8%** on Deep Memory Retrieval benchmark (vs MemGPT 93.4%)
- **18.5% accuracy improvement** on LongMemEval (enterprise-focused, complex temporal reasoning)
- **90% latency reduction** on LongMemEval vs. alternatives

LongMemEval is the relevant benchmark for research use — it tests complex multi-session reasoning over long timeframes. The 90% latency reduction is striking and suggests the graph structure enables more targeted retrieval.

---

## Key architectural insight

Standard systems store facts without temporal metadata. For a researcher:
- "I believed X when I wrote this paper draft"
- "I changed my view on X after reading Y"
- "This argument was valid before Z was published"

...these are all lost in a flat or graph-without-time system. Graphiti makes these retrievable.

---

## Relevance to our build

**High** for the temporal dimension we flagged in the plan. A few specific applications:
- Tracking when a theoretical position was held vs. updated
- Knowing which version of an argument was in which draft
- Reconstructing the intellectual history of a project (useful for writing paper introductions)
- The "this memory was true as of X" problem in auto-memory files

**The gap it fills**: The plan notes "most PKM systems don't model time well" — Zep/Graphiti is the evidence-backed solution to exactly that problem.

---

## Complexity concern

Zep is enterprise-focused. Full deployment is heavyweight. However, Graphiti is the underlying library and may be usable standalone. Worth investigating whether the Graphiti graph can be used without the full Zep stack.
