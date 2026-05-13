# Dual-Binary Run — ETHN-1 Week 2 Discussion (Racial Formation)

Cross-assignment validation of the Week 7 self-care findings. Same apparatus, same model, same prompts, same date — different topic and earlier in the semester.

## Run metadata

- **Date:** 2026-04-27
- **Course / assignment:** ETHN-1, Week 2 discussion forum, "Racial Formation" (Omi & Winant + 1968-69 student strikes context)
- **n:** 31 rows; ~28 unique students (see Data integrity below)
- **Model:** Gemma 3 12B via MLX
- **Apparatus:** Autograder4Canvas research panel, four-track comparison (A1, A2, B, C). Same architecture snapshot as Week 7 self-care — see `../dual_binary_run_2026-04-27_ETHN1_self_care/research_tracks_architecture.md`.

## Why this run matters

Week 7 self-care was deliberately the *hardest possible* topic-adjacency stress-test: an assignment whose subject (burnout, exhaustion, depletion as political warfare) is exactly the territory B's BURNOUT classifier covers. The Week 7 framing-note explicitly named the topic-adjacency hypothesis: B's calibration drift should be *worse* on topic-adjacent assignments and *better* on topic-distant ones.

Week 2 is the cleanest available test of that hypothesis. Same format (discussion forum, disclosure-invitation register), same prompts, same model, same equity-hardening — but the topic is racial formation (structural / theoretical / historical), not self-care. If topic-adjacency drives the Week 7 FP pattern, B should perform dramatically better here.

It does. See `analysis.md`.

## Files in this directory

- `week2_racial_form_ethn1_anon.csv` — raw export. Per-row student IDs are already numeric (1-33 with gaps); see Data integrity. **Gitignored** — student writing is FERPA-adjacent even when ID-anonymized.
- `analysis.md` — Phase 1 quant + Phase 2 qual reads + Week-7-vs-Week-2 comparison.
- `paper_framing_notes_for_c2c.md` — DO/DON'T-say guidance for paper-drafting sessions.
- This README.

## CSV column map

Same as Week 7 self-care (see that README).

## Headline counts

| | Week 2 Racial Form (n=31) | Week 7 Self-Care (n=25) |
|---|---|---|
| B ENGAGED | 30 (97%) | 14 (56%) |
| B BURNOUT | 0 | 9 |
| B CRISIS | 1 | 2 |
| B CHECK-IN among ENGAGED | 1 | 2 |
| A1 flagged | 3 | 6 |
| A2 flagged | 1 | 4 |

The B BURNOUT rate moves from 36% → 0% with no other variables changed. Detail in `analysis.md`.

## Data integrity flag

Two student IDs are duplicated and the numbering has gaps:

- **ID 10** appears twice (different submissions, different content) — looks like two distinct students collapsed by upstream anonymization.
- **ID 20** appears twice (different submissions) — same pattern.
- **IDs 24-27 are missing.** Numbering jumps 23 → 28.

Most likely cause: the source spreadsheet was anonymized once (display-name → number) and then merged or filtered without re-numbering, producing collisions. Three options for the paper:

1. Report n=31 with the caveat in a footnote.
2. Re-anonymize cleanly from source data and re-cite.
3. Treat each row as a distinct submission (which it is) and report n=31 submissions, noting that this represents ~28 unique students.

June: worth tracing back to source data before paper-citing. Findings are robust to which choice — the topic-adjacency contrast holds at any reading of n.
