# Karpathy LLM Wiki Pattern

**Source**: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f  
**By**: Andrej Karpathy  
**Type**: GitHub Gist / idea file / starter schema  
**Date**: April 4, 2026  
**Implementations**: 500+ comments, multiple open-source forks

---

## What it is

Not a paper — a starter schema Karpathy wrote to be copied into a Claude Code / Codex session, where the LLM then helps build the system collaboratively. The agent builds a **persistent, structured wiki** of synthesized markdown sitting between raw sources and the user.

**The Memex reference**: Karpathy explicitly invokes Vannevar Bush's 1945 Memex concept — a personal, curated knowledge store with associative trails. His claim: Bush couldn't solve the maintenance bottleneck; LLMs can.

**Core critique of standard RAG**: It's stateless. Every query re-derives knowledge from scratch. Nothing accumulates. Knowledge compiles once and stays current in the wiki model.

---

## Three-Layer Architecture

1. **Raw Sources** — Immutable input documents. LLM reads, never modifies.
2. **The Wiki** — LLM-owned markdown files: summaries, entity pages, concept pages, comparisons. LLM creates and updates these, maintaining cross-references.
3. **The Schema** — A CLAUDE.md-style config telling the LLM how the wiki is structured, conventions, and workflows for ingest/query/maintenance.

---

## Key Operations

- **Ingest**: User adds new source → LLM reads, discusses, writes summaries, updates index, modifies relevant wiki pages simultaneously
- **Query**: LLM answers from wiki pages with citations; can file valuable answers back as new wiki pages
- **Lint**: Periodic health checks for contradictions, stale claims, orphan pages, missing cross-references

---

## Infrastructure Recommendations

- `index.md` — catalog with links, one-line summaries, metadata, organized by category
- `log.md` — append-only chronological record
- Optional: **qmd** as local BM25/vector hybrid search with LLM re-ranking, usable as MCP server
- **Obsidian** graph view for visual connectivity; Obsidian Web Clipper for ingestion; git for version history

Karpathy explicitly recommends Obsidian. There's an Obsidian-specific implementation: https://github.com/kytmanov/obsidian-llm-wiki-local

---

## Community Response

- lucasastorian/llmwiki: https://github.com/lucasastorian/llmwiki
- Astro-Han/karpathy-llm-wiki (Agent Skills compatible): https://github.com/Astro-Han/karpathy-llm-wiki
- kytmanov/obsidian-llm-wiki-local: https://github.com/kytmanov/obsidian-llm-wiki-local
- LLM Wiki v2 (extending for agent memory): https://gist.github.com/rohitg00/2067ab416f7bbe447c1977edaaa681e2

---

## Relevance to our build

**Very high.** This is essentially what we're building — human-curated, LLM-maintained, Obsidian-hosted, with accumulation rather than stateless retrieval. What Karpathy formalizes that we don't yet have:

1. **Explicit schema document** — tells the LLM how the wiki is organized and what the maintenance conventions are
2. **Lint operation** — periodic health check for orphan pages, contradictions, stale content. This directly addresses recency bias and the WEAVE problem.
3. **log.md** — append-only temporal record (temporal tracking without a full graph DB)
4. **Defined ingest workflow** — right now our write loop is ad hoc; this formalizes it

**The WEAVE/PARK functions** June already uses in session behavior are manual implementations of the episodic + working memory management that the wiki formalizes. Making them persistent across sessions (not just in-context) is exactly the upgrade this pattern enables.

---

## Critical concerns from community

- Data corruption risk if LLM modifies wiki incorrectly
- Knowledge drift between human mental model and LLM-generated content
- Need for human validation metadata to distinguish AI-generated vs human-authored content
