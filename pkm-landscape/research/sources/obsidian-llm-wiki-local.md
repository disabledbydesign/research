# obsidian-llm-wiki-local — Concrete Implementation

**Repo**: https://github.com/kytmanov/obsidian-llm-wiki-local  
**pip**: `obsidian-llm-wiki` | CLI: `olw`  
**Type**: Python CLI, local-only (Ollama), Obsidian as display layer  
**Date assessed**: 2026-04-15

---

## What it is

The most concrete local implementation of Karpathy's LLM wiki pattern, specifically built for Obsidian. Writes plain markdown with YAML frontmatter — no custom Obsidian plugins required.

---

## Three-stage pipeline

### Stage 1 — `olw ingest` (fast model, 3–8B)
Reads each raw note, extracts a structured `AnalysisResult`:
- `summary` (2-3 sentences)
- `key_concepts` (max 8 concept names)
- `suggested_topics` (max 5 wiki article titles)
- `quality` (high/medium/low)

Writes results to SQLite (`state.db`). Incremental via content hash — only re-processes notes that changed. Creates `wiki/sources/NoteName.md` summary pages.

### Stage 2 — `olw compile` (heavy model, 7–14B)
Concept-driven: one wiki article per concept, recompiles only concepts whose source notes changed.

Injects into compile prompt:
- System prompt
- First 1500 chars of `vault-schema.md`
- Rejection feedback from previous human reviews
- List of existing article titles

Returns structured `SingleArticle`: title, content (markdown with `[[wikilinks]]`), tags. Writes to `wiki/.drafts/` with YAML frontmatter.

### Stage 3 — `olw review` / `olw approve` (human)
Human reviews drafts. Approve strips annotations and moves to `wiki/`. Reject stores feedback for next compile. After 5 rejections without approval, concept is auto-blocked.

Every action is a `[olw]`-prefixed git commit. `olw undo` uses `git revert`.

---

## The vault-schema.md document

This is NOT a complex schema. It's a short markdown file (injected into compile prompts as the first 1500 chars). The default written by `olw init`:

```markdown
# Vault Schema

## Folder Structure
- `raw/` — input notes (immutable, never edited by olw)
- `wiki/` — AI-synthesised articles (managed by olw)
- `wiki/.drafts/` — pending human review

## Note Format
Every wiki note has YAML frontmatter with: title, tags, sources,
confidence, status, created, updated.

## Links
Use `[[Article Title]]` wikilinks between notes.
```

You edit this file to add domain-specific naming conventions, article structure expectations, etc. Deliberately short.

---

## Article frontmatter schema

```yaml
title: "Concept Name"
tags: [tag-a, tag-b]
sources: ["raw/note1.md", "raw/note2.md"]
confidence: 0.72
status: draft  # → published on approve
created: 2026-04-15
updated: 2026-04-15
```

---

## Lint operation — entirely static, no LLM

`olw lint` checks:
- `orphan` — concept page with no inbound wikilinks
- `broken_link` — `[[Target]]` that resolves to no file
- `missing_frontmatter` — required fields absent
- `stale` — file was edited by hand since last compile
- `low_confidence` — confidence < 0.3
- `invalid_tag` — invalid Obsidian tag name

`olw lint --fix` auto-repairs `missing_frontmatter` and `invalid_tag`. Reports a 0–100 `health_score`.

`olw maintain` adds: stub articles for broken wikilinks, orphan merge suggestions, source distribution warnings.

---

## Obsidian plugins required

**None required.** The tool writes plain markdown with standard YAML frontmatter and `[[wikilinks]]`. Optional plugins that add value:
- **Dataview** — query by `status: published`, `confidence: > 0.7`, `tags`
- **Graph view** — built into Obsidian
- **Backlinks** — built into Obsidian
- **Web Clipper** — to pipe web articles into `raw/`

---

## Limitations

1. **Scales to ~100 source notes** before index-based query routing degrades
2. **Local models only** (Ollama) — no API key path; cloud LLMs require forking
3. **Heavy model bottleneck**: 14B models slow for large concept counts
4. **No semantic search** — `olw query` routes by title, not vector similarity
5. **Manual-edit protection is one-way**: if you edit an article by hand, compile skips it permanently
6. **Context budget fixed**: source material truncated if > `heavy_ctx / 2` chars for a given concept

---

## Config

`wiki.toml` (per vault) + `~/.config/olw/config.toml` (global). Key settings: model names, Ollama URL, `fast_ctx`/`heavy_ctx`, `auto_approve`, `auto_commit`, `max_concepts_per_source` (default: 8).

---

## Comparison with other implementations

**lucasastorian/llmwiki**: Full web app (Next.js + FastAPI + Supabase). Claude connects directly via MCP and has five tools: guide, search, read, write, delete. Claude IS the orchestrator — you talk to it, it maintains the wiki. PGroonga full-text search. Cloud or self-hosted.

**Astro-Han/karpathy-llm-wiki**: Agent Skills package (`npx add-skill`). No infrastructure — just a skill file that your coding agent (Claude Code, Cursor) loads and executes. The agent is the executor. Simplest path for Claude Code integration.

---

## Relevance to our build

The `olw` CLI is the most concrete reference implementation for the write-time compilation principle. Key things to port:
1. The ingest → compile → review pipeline structure
2. The vault-schema.md concept (short, human-editable, injected into prompts)
3. The static lint/health check approach (no LLM required for maintenance)
4. The article frontmatter schema (especially `confidence` and `status: draft/published`)
5. Git commit per action + `undo` via revert — low-overhead version control

Key limitations to work around:
- The 100-note scale limit (we need something that handles June's full knowledge base)
- Local models only (we want to use Claude API)
- No semantic search (we want vector + graph hybrid)
