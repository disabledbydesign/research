# Voice-Check Findings

Append-only log of voice-check lint runs on artifacts in the research program. Infrastructure-parallel to `logs/` but for register-discipline data rather than compression data.

## What this is

When voice-check runs catch contamination, flag structural issues, or surface qualitative observations, the data evaporates unless logged. This directory persists what voice-check finds so that:

- Register drift over time is trackable (does Claude's voice stay where the profile defends it, or drift?).
- Genre overlays get validated empirically (are the `fieldnote` qualitative checks catching what they should? false-positive rate?).
- The learning loop has traceable data (what revisions shifted the profile, session-over-session).

## What lives here

- `README.md` — this file.
- `INDEX.md` — chronological table of all lint runs.
- `logs/` — individual lint-run records, append-only, never overwritten. Filename: `voice_check_findings_YYYY-MM-DD_<artifact-slug>.md`.

## Relation to compression research

Voice-check findings are a sibling research thread to compression logs. Compression logs track what survives cross-session transmission of cognitive state. Voice-check findings track what survives normative-gravity pressure on register. Both are data on what gets preserved vs. lost in different kinds of lossy transmission. Co-locating them under `compression_research/` is deliberate: the unified research question is *what survives, and under what pressures*.

## Log entry structure

Each entry records:

- **Provenance**: date, artifact linted, profile used, genre overlay, script version.
- **Quantitative findings**: raw output of `writing_check.py` — flags by category.
- **Qualitative interpretation**: which flags are real register violations, which are false positives, what pattern the flags reveal.
- **Revisions made (if any)**: what was changed in the artifact based on findings, with rationale. If no revisions, state why (e.g., all flags were false positives, or the violations were genre-appropriate given provenance constraints).
- **Findings about the genre overlay**: does it catch what it should? Miss anything? Flag false positives that suggest a check needs refinement?
- **Learning loop result (if `--learn` was run)**: what shifted in the profile.

## Append-only discipline

Never overwrite. If a prior finding was wrong or a revision regressed, write a new entry that references and corrects the prior one. The trajectory is the data.

## Running the linter

Standard invocation when Claude is the author:

```bash
python3 ~/.claude/skills/voice-check/writing_check.py DRAFT_PATH \
  --genre GENRE_NAME \
  --profile ~/.claude/skills/voice-check/profiles/claude.json
```

When June is the author, auto-discover is correct — omit `--profile`.
