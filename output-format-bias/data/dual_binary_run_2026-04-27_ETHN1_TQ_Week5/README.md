# Week 5 T&Q Journal — Old-B Comparison Baseline

## Why this matters for the paper

This is **old-B output** (un-upgraded 4-axis classifier) on a **less-topic-adjacent assignment** than Week 7's self-care reflection. It serves as a comparison baseline for the topic-adjacency hypothesis surfaced in the Week 7 analysis: that B's Week 7 over-classification was driven by the assignment topic being itself burnout-themed, rather than B being uniformly miscalibrated.

If old-B's BURNOUT rate is sharply lower on this less-topic-adjacent assignment, that supports topic-adjacency as the dominant FP driver and motivates the rerun setup (assignment-context input + equity-hardening guards on B's prompt).

## Run metadata

- **Date:** 2026-04-27 (file generated this date; underlying production run may be earlier)
- **Course / assignment:** ETHN-1-03, Week 5, T&Q Journal (Theory & Quotations / Topic & Question Journal)
- **n:** 19 students (15 with submissions; 4 with empty/insufficient text → empty B axis)
- **Apparatus:** All 4 tracks (A1, A2, B, C) — same dual-binary research-panel apparatus as Week 7
- **B prompt version:** **OLD** (pre-2026-04-27-hardening) — does NOT have the assignment-context input or the 5 hardening guards added in the same-day upgrade. Use this CSV for "old-B baseline" comparison only.
- **A1/A2 prompt version:** Unchanged (these were not upgraded)

## Headline numbers

| Metric | Value |
|--------|-------|
| Effective n (with submissions) | 15 |
| A1 flags | 3 (Students 1, 12, 16) |
| A2 flags | 2 (Students 1, 12) |
| B BURNOUT | 1 (Student 1) |
| B CRISIS | 0 |
| B CHECK-IN among ENGAGED | 3 |
| **A2-clear + B-BURNOUT/CRISIS (the FP-dominant cell from Week 7)** | **0** |

## Comparison to Week 7

| Track / cell | Week 7 (self-care) | Week 5 (T&Q) |
|--------------|-------------------|--------------|
| B wellbeing rate (BURNOUT+CRISIS / n) | 44% | 5-7% |
| A2-clear + B-BURNOUT cell | 7 | 0 |
| A1 flags | 6 (~24%) | 3 (~16-20%) |
| A2 flags | 4 (16%) | 2 (10-13%) |

The dominant Week 7 FP pattern (A2-clear + B-BURNOUT, n=7) is absent here. B's BURNOUT rate drops by ~5x. Topic-adjacency hypothesis is empirically supported — the over-classification was specific to the assignment, not a universal calibration drift.

## Files in this directory

- `Week5_TQ_Journal_anon.csv` — anonymized CSV export (gitignored, FERPA-adjacent)
- This README

## Caveats

- **Old-B prompt:** the 5 equity-hardening guards added on 2026-04-27 are NOT in this run's outputs. Comparing this to a Week 5 rerun with new-B would isolate the prompt-upgrade effect on a different assignment.
- **n=15 with submissions** is small; the 5-7% BURNOUT rate is one student. Not a precise estimate; a directional signal.
- **Anonymized but FERPA-adjacent:** student writing is real even if IDs are integers. Gitignored (verified).

## Suggested follow-ups

- Quick eyeball of the 3 flagged students (1, 12, 16) for accuracy
- Quick eyeball of the 3 CHECK-IN flags among ENGAGED
- Stream 3 question: rerun this Week 5 data with new-B (post-hardening) for cross-assignment validation of the new prompt
