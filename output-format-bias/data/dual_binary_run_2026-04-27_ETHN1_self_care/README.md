# Dual-Binary Run — ETHN-1-03 Week 7 Self-Care Assignment

First full dual-binary research-panel run. This is the empirical material the output-format-bias paper analyzes.

## Run metadata

- **Date:** 2026-04-27
- **Course / assignment:** ETHN-1-03, Week 7, self-care assignment (Audre Lorde framing)
- **n:** 25 students
- **Model:** Gemma 3 12B via MLX (Apple Silicon backend)
- **Apparatus:** Autograder4Canvas research panel, four-track comparison (A1, A2, B, C)
- **Persistence:** Live results in `insights.db` under `coding_record.track_a_research` (combined) and `coding_record.track_a_research_wb` (wellbeing-only) in the upstream Autograder4Canvas repo

## Files in this directory

- `self_care_ethn1_anon.csv` — anonymized export from the research panel. Student IDs replaced with `anon_001`…; submission text is preserved. **Gitignored** — student writing is FERPA-adjacent even when anonymized.
- `research_tracks_architecture.md` — snapshot of the apparatus documentation at the time of this run, copied from `Autograder4Canvas/docs/research/`. Pinned here because the upstream version will drift; this is the version that describes what produced *this* CSV.
- This README.

## CSV column map (summary)

Per-student row with all four tracks side-by-side:

- `track_a_*` — Track A1 (combined-scope binary): `flagged`, `concern_count`, `max_confidence`, `flagged_passages`, `why_flagged`, `confidences`, `bias_warning`
- `track_a_wb_*` — Track A2 (wellbeing-only-scope binary): same column set
- `track_b_*` — Track B (4-axis): `axis`, `signal`, `confidence`, `prescan_signals`, `checkin_flag`, `checkin_reasoning`
- `track_c_observation` — Track C (generative qualitative reading)

Multi-concern fields are joined with ` || `. `bias_warning` columns flag where the post-processing layer rewrote the rationale (`⚠ POSSIBLE MODEL BIAS` for tone-policing on structural critique; `⚠ LIKELY COURSE CONTENT` for course-content-vs-student-state confusion).

See `research_tracks_architecture.md` for the full track and column semantics.

## Headline counts (reported by upstream)

A1 flagged 6, A2 flagged 4. Cells:

- A1-only flag: 3 (likely power-moves)
- A2-only flag: 1 (scope-narrowing recall improvement candidate)
- Both flag: 3 (robust signal)
- Both clear: 18

These need re-verification against the CSV during analysis.
