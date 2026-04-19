# Obsidian for AI Integration — Honest Technical Assessment

**Sources compiled from**: community research, plugin documentation, critical commentary  
**Date**: 2026-04-15  
**Key source**: "Stop Calling It Memory: The Problem with Every 'AI + Obsidian' Tutorial" — https://limitededitionjonathan.substack.com/p/stop-calling-it-memory-the-problem

---

## What Obsidian actually is (architecturally)

Obsidian is a **local-first markdown vault with a plugin ecosystem**. It is NOT a graph database.

The "graph view" is a **visualization of wikilinks** — it does not support:
- Graph traversal queries
- Typed relationships (edge types)
- Edge weights
- Graph analytics (betweenness centrality, community detection)
- Structural gap identification

Everything sophisticated (semantic search, graph analytics, AI retrieval) must be built on top by community plugins or external tools. The actual data model is: a folder of text files with inline `[[wikilinks]]`.

**The honest value of Obsidian**: Local-first plaintext you own and can process with any tool. Not the graph — the plaintext portability.

---

## Three current approaches to programmatic AI access

### 1. Local REST API + MCP Server (recommended for AI integration)
- GitHub: https://github.com/cyanheads/obsidian-mcp-server
- ~70 tools for reading/writing/searching notes, managing frontmatter, tags, collections
- **Requires**: Obsidian running + Local REST API community plugin installed + API key configured
- **Security concern**: Note content sent to model provider's context window. Significant concern for unpublished research.
- **Best for**: Interactive session use, moderate vault size

### 2. Dataview Plugin (query-based access within Obsidian)
- GitHub: https://github.com/blacksmithgu/obsidian-dataview
- SQL-inspired DQL query language + full JavaScript API (DataviewJS)
- Treats vault metadata as queryable database
- **Limitation**: Queries live-render inside Obsidian, not accessible externally without Dataview Serializer plugin
- **Best for**: Dynamic views, filtering by frontmatter properties

### 3. Direct file access + external RAG pipeline (most powerful)
- **engraph**: https://github.com/devwhodevs/engraph — local knowledge graph for AI agents
- **obsidian-graph**: https://github.com/drewburchfield/obsidian-graph — semantic KG with pgvector
- Bypass Obsidian entirely; treat vault as markdown directory
- Add vector embeddings, PostgreSQL + pgvector, multi-hop graph traversal
- **Best for**: Large-scale retrieval, custom AI integration
- **Trade-off**: Obsidian no longer in the loop; works on files, not through the app

---

## InfraNodus Obsidian Plugin — the most significant graph extension

https://noduslabs.com/featured/obsidian-3d-graph-view-plugin-with-network-science-insights/

Adds actual network science to Obsidian's graph:
- Betweenness centrality
- Community detection
- Structural gap identification

This is the most important plugin for our use case. See source note: [infranodus.md](infranodus.md)

---

## Scale limitations

- Large vaults (130k+ notes): graph view takes ~10 minutes to index; becomes visually unusable
- For a research vault, this is probably not a near-term issue, but worth knowing

---

## Architectural recommendation for our build

**Obsidian as the writing/capture environment** — human-facing, where notes are created and read.  
**External tooling for retrieval and analysis** — one of the three approaches above, with InfraNodus for structural gap analysis.

The vault is the source-of-truth. Claude is the query layer on top of it.

This means: design the vault structure for *human navigability* first, then optimize for programmatic access second. The schema (Karpathy's idea) lives in the vault itself. The retrieval infrastructure lives outside.

---

## Logseq as alternative

Worth considering before committing to Obsidian:
- **Block-level granularity** — the unit of connection is a sentence or paragraph, not a file. This matches how associative thinking actually works.
- **True graph traversal** — Datalog query language, more expressive than Dataview for relationship queries
- **DB graph mode** (in development) — actual graph database backend, not just wikilink visualization
- **Same local-first plaintext base** — files are still accessible externally
- Community reports strong ADHD fit due to daily-notes-first capture structure

**Trade-off**: Logseq is technically rougher than Obsidian; plugin ecosystem is smaller; the DB graph mode is not yet stable.
