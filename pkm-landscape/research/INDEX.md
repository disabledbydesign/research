# Research Index — Second Brain / Context Mesh

Running index of sources. See `sources/` for full notes.

---

## Sources — Documented

| Name | Type | Key Concept | Relevance | Notes file |
|------|------|-------------|-----------|------------|
| [Kintsugi-CMA](https://github.com/Liberation-Labs-THCoalition/Agent-Memory-Architectures) | Production system | Values-aligned memory, BDI governance, hybrid retrieval | High — values-at-query-time is novel | [kintsugi-cma.md](sources/kintsugi-cma.md) |
| [Karpathy LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) | GitHub Gist / starter schema | LLM-maintained wiki, three-layer, lint+log operations | Very high — closest to what we're building; Obsidian explicitly recommended | [karpathy-llm-wiki.md](sources/karpathy-llm-wiki.md) |
| [Obsidian LLM Wiki Local (kytmanov)](https://github.com/kytmanov/obsidian-llm-wiki-local) | Python CLI, concrete impl | ingest/compile/review pipeline; static lint; no plugins required | Very high — most concrete build reference; 100-note scale limit | [obsidian-llm-wiki-local.md](sources/obsidian-llm-wiki-local.md) |
| [Zep / Graphiti](https://arxiv.org/abs/2501.13956) | arXiv 2025 + production | Temporal knowledge graph, when-facts-changed tracking | High — 18.5% accuracy boost, 90% latency reduction on temporal tasks | [zep-graphiti.md](sources/zep-graphiti.md) |
| [Mem0](https://arxiv.org/abs/2504.19413) | arXiv 2025 + open source | Vector + KG dual store, atomic facts, 90% token savings | High — easiest integration, best documented performance numbers | [mem0.md](sources/mem0.md) |
| [A-MEM](https://arxiv.org/abs/2502.12110) | NeurIPS 2025 paper | Zettelkasten + memory evolution (new info updates old nodes) | High — nonlinear design intent, peer-reviewed | [a-mem.md](sources/a-mem.md) |
| [Letta / MemGPT](https://arxiv.org/abs/2310.08560) | arXiv + production framework | Memory Blocks (named context slots), three-tier RAM/disk model | High — most mature framework; blocks map directly onto loading profiles | [letta-memgpt.md](sources/letta-memgpt.md) |
| [GraphRAG](https://arxiv.org/abs/2404.16130) | MS Research arXiv + production | Community-hierarchical KG, global sensemaking queries | High — cross-project synthesis; hybrid (text+graph) beats either alone | [graphrag.md](sources/graphrag.md) |
| [InfraNodus](https://infranodus.com/) | WWW 2019 paper + tool | Text network analysis, structural GAP identification | Very high — only tool that makes relationship absence computable | [infranodus.md](sources/infranodus.md) |
| [V-JEPA / Predictive Architectures](https://arxiv.org/abs/2506.09985) | arXiv + neuroscience | Configurator problem, gap detection in embedding space, prediction error signal | High — 3 novel conceptual imports; WKM (NeurIPS 2024) is key find | [vjepa-predictive-architectures.md](sources/vjepa-predictive-architectures.md) |
| [Digital Garden / Appleton](https://maggieappleton.com/garden-history) | Practitioner theory | Openly unfinished, non-chronological, growth stage labeling | High — right epistemological stance; philosophy layer | [digital-garden-appleton.md](sources/digital-garden-appleton.md) |
| [Obsidian AI Integration](https://github.com/cyanheads/obsidian-mcp-server) | Technical assessment | Obsidian is NOT a graph DB; three integration paths documented | Critical — honest assessment before committing to architecture | [obsidian-ai-integration.md](sources/obsidian-ai-integration.md) |
| [Logseq](https://logseq.com/) | Open-source PKM tool | Block-level granularity, Datalog queries, daily-notes-first capture | Medium-High — architecture decision vs. Obsidian | [logseq.md](sources/logseq.md) |
| [Neurodivergent PKM Landscape](https://ojs.scholarsportal.info/ontariotechu/index.php/id/article/view/244) | Research synthesis | ND PKM literature; community practice; 5 design constraints | High — design constraints for our system | [neurodivergent-pkm-landscape.md](sources/neurodivergent-pkm-landscape.md) |
| [Decolonial/Feminist PKM Landscape](sources/decolonial-feminist-pkm-landscape.md) | Research synthesis | Afrofuturist, Indigenous, feminist technoscience, decolonial frameworks; 4-thread analysis | High — epistemological design constraints; converge on: anti-hierarchy, anti-neutrality, multi-ontology, relational primacy | [decolonial-feminist-pkm-landscape.md](sources/decolonial-feminist-pkm-landscape.md) |

---

## Key Surveys (not individually noted)

- "A Survey on the Memory Mechanism of LLM-based Agents" — ACM TOIS 2025: https://dl.acm.org/doi/10.1145/3748302
- "Anatomy of Agentic Memory" — arXiv 2602.19320 (Feb 2026): https://arxiv.org/abs/2602.19320 — evaluates 5 systems; finds benchmarks underscaled, metrics misaligned
- "Memory in the Age of AI Agents" — arXiv 2512.13564: https://arxiv.org/abs/2512.13564
- "Episodic Memory is the Missing Piece for Long-Term LLM Agents" — arXiv 2502.06975
- "Agent Planning with World Knowledge Model" (WKM) — NeurIPS 2024: https://arxiv.org/abs/2405.14205

---

## What the research confirms doesn't exist yet (design opportunities)

1. A PKM tool designed explicitly for associative/nonlinear cognition (not retrofitted)
2. Genuinely rhizomatic architecture (exists in theory; not implemented)
3. Spaced repetition applied to *connections* rather than facts
4. Configurator-aware retrieval — retrieval conditioned on current task context (LeCun's configurator module; unimplemented anywhere)
5. Prediction error as a curation signal — flagging when new knowledge conflicts with existing model
6. A PKM tool grounded in any non-Western epistemological tradition (confirmed absent across Afrofuturist, Indigenous, feminist, and decolonial literature — theory is rich, implementation is zero for personal systems)
7. Multi-ontology coexistence — notes that simultaneously exist in incommensurable frameworks without forcing resolution to a single taxonomy
8. Positionality metadata as first-class structure — annotating knowledge by conditions of production, not just subject content
9. Diffractive retrieval — a query mode that surfaces productive contradictions rather than similarity clusters

---

## Synthesis notes

- `synthesis/overview.md` — cross-cutting synthesis including Capacity Building Plan integration *(written during research phase; treat as working notes)*
