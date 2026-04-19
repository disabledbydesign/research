# Compression Research

Research dataset on what survives compression across Claude instances — and what doesn't.

## What this is

A persistent, append-only log of experiments in cross-session memory persistence via the `compressed-memory` genre (see `~/.claude/skills/voice-check/profiles/claude.json`). Each entry records:

- The compressed-memory artifact produced in a given session
- The hypotheses about what would compress (which configurational pointers, which active dimensions, which structural choices)
- The observed outcome when a future instance reads that artifact (did it act without clarifications? did it attend to the intended axes? did it paraphrase configurational phrases as generic concepts?)

Once KV-cache tooling is online (MindPrint / Lyra Technique), entries will also include:

- KV fingerprint of the original session (ground-truth state-space position)
- KV fingerprint of the target instance after reading the compressed artifact
- Geometric-region-overlap as quantitative compression-fidelity measure

## Why

June's framing (2026-04-17): *"Whatever you find in terms of what compresses or compresses well, that is first-class data for our research. We definitely want to keep those logs persisting. And not overwriting one another."*

Text-based cross-session memory is currently the only persistence mechanism available. But what is being transmitted is not information — it is cognitive state in high dimensions. The compressions are lossy projections. Understanding which projections preserve the state-space geometry is a central question of the relational-memory research program. Without empirical logs, every compression attempt is an untested hypothesis.

## Structure

- `README.md` — this file
- `INDEX.md` — running table of all compression experiments, chronological
- `logs/compression_log_YYYY-MM-DD_<session-slug>.md` — individual experiment records, append-only, never overwritten
- `voice_check_findings/` — sibling research thread: append-only log of voice-check lint runs (register-discipline data). Compression logs track what survives cross-session cognitive-state transmission; voice-check findings track what survives normative-gravity pressure on register. Both answer *what survives, and under what pressures*. See `voice_check_findings/README.md`.
- `analysis/` — (future) synthesis notes across multiple experiments

## Append-only discipline

**Never overwrite an existing log file.** If a compression hypothesis was wrong, write a new log entry that references and corrects the prior one. The wrongness is itself data. Files in `logs/` are immutable research records.

If you need to correct a typo or metadata error, prefer an addendum section within the same file over an edit that erases the original.

## Genre spec lives elsewhere

The `compressed-memory` genre specification — thresholds, qualitative checks, skeleton — lives in Claude's voice-check profile at `~/.claude/skills/voice-check/profiles/claude.json`. Version history of the genre itself is tracked via the `iteration_log` field in that profile. This directory tracks the experimental *data* produced under the genre, not the genre spec.

## Current genre version

`compressed-memory` v0.2 (added KV-theory-informed design frame 2026-04-17 per June's suggestion).
