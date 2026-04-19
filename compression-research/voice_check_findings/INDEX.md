# Voice-Check Findings — Index

Chronological log of voice-check lint runs. Append new rows; do not delete.

| Date | Log file | Artifact linted | Profile | Genre | Flags (total / voice / structural) | Revisions made? |
|---|---|---|---|---|---|---|
| 2026-04-18 | `logs/voice_check_findings_2026-04-18_poetry-fieldnote.md` | `fieldnotes/poetry_as_compression_technology_2026-04-18.md` | `claude.json` v0.1 | `fieldnote` | 21 / 13 / 8 | yes — hedge register revisions; verbatim quote preserved untouched |
| 2026-04-18 | `logs/voice_check_findings_2026-04-18_cross-project-mapping.md` | `MEMORY_ARCHITECTURE_MAPPING_CROSS-PROJECT_2026-04-18.md` | `claude.json` v0.1 | `research-report` | ~36 / 27 / 9 | yes — "This is" opener tic (8 revisions); leverage→concrete; one hedge removed |

## Fields

- **Date** — when the lint was run
- **Log file** — individual record in `logs/`
- **Artifact linted** — the document the linter was run on
- **Profile** — which voice-check profile was used
- **Genre** — which genre overlay applied
- **Flags** — total count and split between voice (contamination) and structural
- **Revisions made?** — yes/no with brief note

## Research questions this log exists to answer

1. Do Claude's genre overlays (especially the new `fieldnote` and `compressed-memory` overlays) catch register violations the base profile would miss?
2. What is the false-positive rate per genre? Which checks over-trigger?
3. Does register drift over time, session-over-session? If so, in which direction — toward or away from the defended register?
4. Does running the linter + self-correction reduce flag count on the next similar artifact, or does contamination re-emerge fresh each time?
5. Are there contamination patterns the linter misses that Claude (or June) catches by other means?
