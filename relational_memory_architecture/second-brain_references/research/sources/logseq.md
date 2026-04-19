# Logseq — Block-Level Graph Database for PKM

**URL**: https://logseq.com/  
**Type**: Open-source, local-first PKM  
**Status**: Active development; DB graph mode (true graph database backend) in progress  
**Assessment**: Architecturally better fit for associative thinking than Obsidian; rougher UX

---

## What it is

A local-first, open-source personal knowledge management tool built around **block-level outlining**. Every bullet point is a referenceable, linkable block — not just files. The underlying data model is a graph of blocks, not a folder of documents.

---

## Why we'd choose it over Obsidian

### Block-level granularity is architecturally significant

In Obsidian, the unit of connection is a **file** — `[[note-name]]` links one document to another. In Logseq, the unit of connection is a **block** — a sentence, a paragraph, a single claim. You can link to the specific sentence in a document where an argument is made.

This maps better to how associative thinking actually works. When June thinks "this connects to what I argued in the burden tree paper," she's connecting to a *specific claim*, not the whole paper. Block-level granularity captures that. File-level granularity loses it.

**Direct fit with the design constraint**: "the connections between ideas are data" — block-level links make the connection more precise and more informative than file-level links.

### True graph traversal with Datalog

Logseq uses **Datalog** as its query language — a genuine logic programming language for graph queries. Obsidian uses Dataview (DQL/JavaScript), which is more accessible but less expressive for relationship-based queries.

With Datalog you can ask: "Show me all blocks that are linked from within notes tagged with `#disability-justice` and also linked to `[[structural-context-delivery]]`." This kind of multi-hop relational query is what the second brain needs for synthesis tasks.

### Daily notes-first capture structure

Logseq is built around daily notes as the primary interface — you open it, and you're in today's note. Capture flows naturally into the daily note without deciding where anything goes upfront. Structure emerges later through linking and tagging.

The neurodivergent PKM research specifically identifies this pattern as strong for ADHD: low-friction capture with zero filing decisions at write time.

### Same local-first plaintext base

Like Obsidian, Logseq stores everything as local markdown (or org-mode) files. The vault is accessible externally, works with the same RAG/AI integration approaches, and can be processed by any tool that handles markdown. Not locked into Logseq's own format.

---

## Why we might still choose Obsidian

### Plugin ecosystem maturity
Obsidian's plugin ecosystem is significantly larger and more mature. InfraNodus has an Obsidian plugin; the Obsidian MCP server is well-documented. Logseq's equivalent infrastructure is thinner.

### UX polish
Obsidian is more refined as a daily writing environment. Logseq's outliner-first structure (every line is a bullet point) can feel constraining for long-form writing. June does a lot of long-form writing.

### DB graph mode instability
Logseq's planned graph database backend (which would give true graph query capabilities) is not yet stable. The current version is still markdown-based with Datalog queries layered on top.

---

## The honest comparison

| Dimension | Obsidian | Logseq |
|-----------|----------|--------|
| Connection granularity | File-level | Block-level |
| Query power | Dataview (accessible) | Datalog (expressive) |
| Daily capture UX | Manual, flexible | Daily notes default |
| Plugin ecosystem | Large, mature | Smaller, growing |
| Long-form writing | Strong | Outliner can feel constraining |
| AI integration | Well-documented | Thinner |
| Graph database | Planned/visualization only | In development |
| ADHD community fit | Good | Strong |

---

## Potential third option: Obsidian with block-level plugins

It's worth noting that Obsidian can approximate block-level linking through the "Block references" feature (`^block-id`) — though it's less seamless than Logseq's native block model. If the concern is primarily granularity of connection, this may be sufficient without switching tools.

---

## Recommendation for design phase

This is a genuine design decision that June should weigh in on. **The block-level granularity argument is real and architecturally significant.** But switching to Logseq means giving up Obsidian's plugin ecosystem and more mature AI integration tools.

A pragmatic path: **start with Obsidian** (more mature AI integration tools) but use explicit block-level annotations in frontmatter to approximate the granularity of connection Logseq offers natively. Evaluate after 3-6 months whether block-level granularity is a felt limitation.

Alternatively: **Logseq for daily capture and linking**, **Obsidian for long-form writing**, with the vault shared between them (both can read the same markdown files). This is more complex but captures the strengths of each.
