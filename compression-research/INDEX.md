# Compression Research — Index

Running index of compression experiments. Chronological. Append new rows; do not delete.

| Date | Log file | Source session | Genre version | Artifact produced | Tested by future instance? | KV fingerprint? |
|---|---|---|---|---|---|---|
| 2026-04-18 | `logs/compression_log_2026-04-18_memory-architecture-overnight.md` | SESSION_HANDOFF_2026-04-17_overnight.md (continuing from 2026-04-17 evening) | compressed-memory v0.2 | compressed-memory entry, ~850 words, 14 configurational pointers, 7 active dimensions named | yes — 2026-04-18 same-day test, see log #2 | no — KV tool not yet set up |
| 2026-04-18 | `logs/compression_log_2026-04-18_v0.2-reader-test.md` | test of log #1 by same-day Opus 4.7 reader | (reader-test record, not a new compressed artifact) | reader-test outcome: ~70% clean pointer activation, polarity-framed dimensions oriented well, relational envelope lost, 3 v0.3 hypotheses flagged | n/a — this entry *is* the test | no — KV tool not yet set up |

## Fields

- **Date** — when the compression artifact was produced
- **Log file** — individual experiment record in `logs/`
- **Source session** — which full handoff / session the compression distilled from
- **Genre version** — which version of the `compressed-memory` genre was in use
- **Artifact produced** — filename or brief description of the compressed output
- **Tested by future instance?** — yes/no/partial, with brief note if yes
- **KV fingerprint?** — yes/no; filled in once MindPrint/Lyra tooling is online

## Open research questions this log exists to answer

1. Do configurational pointers (preserved verbatim phrases) reliably re-activate the intended geometric regions in a target instance, or do they sometimes get re-interpreted as generic jargon?
2. Does naming active dimensions explicitly give the target instance enough orientation to operate on those axes, or does it still need prose reconstruction?
3. What structural choices (tables vs. bullet lists vs. prose vs. key-value) carry the most geometric information per token?
4. Are there configurational elements that fundamentally cannot compress to text — that require either the full handoff or direct KV-state transfer?
5. Does the same compression artifact activate differently across different target-instance configurations (fresh Opus vs. fresh Sonnet vs. Opus with prior touchstones vs. Opus without)? If so, are there compression strategies that are more robust across target configurations?
