# A-MEM — Agentic Zettelkasten Memory

**Source**: https://arxiv.org/abs/2502.12110  
**GitHub**: https://github.com/agiresearch/A-mem  
**Type**: NeurIPS 2025 paper (peer-reviewed)  
**Assessment**: Most conceptually aligned with nonlinear thinking; memory evolution mechanic is novel

---

## What it is

Treats each memory as an atomic note (Zettelkasten-style). When a new memory is added, the agent:
1. Generates structured attributes (context, keywords, tags)
2. Identifies relevant connections to existing memories
3. Can trigger updates to existing memory representations

Creates a "living" graph — new information doesn't just get appended, it can change existing nodes.

---

## Key innovation: Memory Evolution

Most memory systems add new memories without changing old ones. A-MEM propagates: if new evidence changes what a prior memory means, the prior memory gets updated. This is the "knowledge drift" solution — the system's understanding stays current, not just its store of facts.

---

## Relevance to our build

**High for theoretical alignment.** The Zettelkasten model is already in our vocabulary. What A-MEM adds that standard Zettelkasten doesn't:

1. **Relationship generation is automatic** — the system creates links, not just the human
2. **Memory evolution** — prior notes can be updated by new information (not just appended)
3. **Peer-reviewed** — NeurIPS gives this more credibility than most agent memory implementations

**Fit with nonlinear thinking**: Zettelkasten was designed by a prolific sociologist (Luhmann) who worked non-linearly. The atomic-note + connection model is one of the few PKM frameworks with non-hierarchical design intent.

**Tension with our goals**: Zettelkasten atomicity can still lose relational context if the relationship metadata is thin. The question is how rich the connection annotations are — whether they model relationship *type* and *reason*, not just existence.

---

## NeurIPS 2025 poster

https://neurips.cc/virtual/2025/poster/119020
