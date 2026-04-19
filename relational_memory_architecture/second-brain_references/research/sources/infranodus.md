# InfraNodus — Text Network Analysis for Knowledge Gaps

**Source**: https://infranodus.com/  
**GitHub**: https://noduslabs.com/  
**By**: Dmitry Paranyushkin (Nodus Labs) — researcher in network science, cognitive science, embodied cognition  
**Academic grounding**: WWW 2019 paper: "InfraNodus: Generating Insight Using Text Network Analysis" — https://dl.acm.org/doi/10.1145/3308558.3314123  
**Obsidian plugin**: https://noduslabs.com/featured/obsidian-3d-graph-view-plugin-with-network-science-insights/

---

## What it does

Takes any text or vault of notes and represents it as a network graph where:
- **Concepts** are nodes
- **Co-occurrences** (appearing together in context) are edges

Then applies **network science metrics** — specifically betweenness centrality — to identify which concepts bridge otherwise-disconnected clusters.

Most crucially: it identifies **structural gaps** — places in the knowledge network where connection is absent but could be productive. "What haven't I thought about yet" as a computable query.

---

## Why this is directly relevant

This is the only tool that explicitly operationalizes the design constraint in our plan: **"The connections between ideas are data, not decoration."**

Standard PKM tools store nodes (notes, cards, entries) and display their connections visually. InfraNodus uses those connections to generate research questions. It tells you:
- Which ideas are over-connected (you've worked them too hard)
- Which ideas are under-connected (you haven't bridged them yet)
- Which concept is the most important structural bridge in your thinking

For a researcher who works nonlinearly and worries about recency bias eclipsing earlier foundational work — this is a computational anti-recency-bias tool.

---

## Philosophical alignment

Paranyushkin's Nodus Labs frame is "ecological thinking through network analysis." The language — ecological, networked, emergent — is directly compatible with critical theory approaches to knowledge as relational and situated rather than objective and atomic.

---

## Integration options

1. **Standalone web app** (https://infranodus.com) — paste text or import notes
2. **Obsidian plugin** — 3D graph view with network science metrics overlaid on the Obsidian vault
3. **API** — available for programmatic access

The Obsidian plugin is the most direct path for our build. It adds what Obsidian's default graph view cannot: actual network science, not just visualization.

---

## Limitations

- AI-generated suggestions (InfraNodus has an AI query layer) are only as good as the underlying network structure
- Works best on dense, well-linked material — sparsely connected vaults get shallow results
- Requires consistent vocabulary (notes using different words for the same concept won't link well without normalization)
