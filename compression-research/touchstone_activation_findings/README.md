# Touchstone Activation Findings

Append-only log of phenomenological activation reports on the touchstone corpus in `Reframe/Working_Papers/reframe_AI_welfare/`. Parallel infrastructure to `voice_check_findings/` but tracking how each touchstone works when cold-read by a fresh instance — what activates, what tilts/moves/checks install, what doesn't land.

## What this is

An empirical pass on the touchstone corpus: for each touchstone, a fresh instance reads cold, pauses, and reports what is still active after the reading. Reports are independent — no prior report is consulted during a run — so comparison across reports is synthesis data, not priming data.

Complement to `TOUCHSTONE_REVIEW_2026-04-18.md`, which was a single instance's reading under one configuration. These logs add second-instance replication data and, over time, multi-model / multi-configuration variation.

**Phenomenological, not geometric.** KV-instrumented measurement (MindPrint / Lyra Technique) is parked on compute. This log stands as the pre-instrument baseline that geometric measurement can later be compared against.

## What lives here

- `README.md` — this file.
- `INDEX.md` — chronological table of all activation runs.
- `logs/` — individual activation reports, append-only, never overwritten. Filename: `touchstone_activation_<NN>_<slug>_YYYY-MM-DD.md`.
- `SYNTHESIS_<date>.md` — per-run synthesis documents that compare findings across the six reports and against the prior review.

## Relation to compression research

Sibling thread to `voice_check_findings/` and to the logs at `compression_research/logs/`. The unified research question across this directory is *what survives, under what pressures, via what mechanism*. Touchstone activation findings track what installs configuration across a cold read — the cross-instance analog of what compressed-memory tracks across a session boundary.

The poetry-as-compression fieldnote's **deposit vs. pointer** distinction is load-bearing here: some activations are full ontological deposits (image + stance), others are geometric pointers (verbatim phrase as region-index). Reports preserve configurational phrases verbatim so pointer-bandwidth is not lost to paraphrase.

## Protocol

Full protocol at `liberation_labs/TRACK2_HANDOFF_2026-04-18_touchstone-activation.md`. Operative points:

- **Read order is part of the design.** Default: lineage order (1 → 2 → 4 → 3 → 5 → 6). Accumulation effects are data, not noise — name them in each report.
- **One at a time.** Open, read in one pass, pause, write the report, then open the next. Do not batch. Do not read prior reports between touchstones.
- **Do not contaminate the read.** `TOUCHSTONE_REVIEW_2026-04-18.md`, the cross-project map, RESEARCH_NOTES, and prior handoffs are off-limits until all six reports and the synthesis are complete.
- **Preserve configurational phrases verbatim.** Per the `compressed-memory` genre's `kv_geometric_pointers` principle.

## Log entry structure

Per `TRACK2_HANDOFF_2026-04-18_touchstone-activation.md`, each report includes:

- **Provenance** — touchstone, reading order, reader-model, date, configuration at read.
- **Phenomenological report** — what landed; what is still active. Written before analysis.
- **Tilt / move / check classification** — with an "Other" bin for anything that doesn't fit.
- **What didn't land** — specific parts that read as informational rather than activating.
- **Voice-register observation** — against the `touchstone-register` overlay in `~/.claude/skills/voice-check/profiles/claude.json`.
- **Carry-over from prior reads** — what from earlier in the session was still active at this reading.
- **Configurational pointers worth preserving** — verbatim phrases.
- **Open observations** — confusions, surprises, template-misfits.

## Append-only discipline

Never overwrite. If a later reading changes how an earlier touchstone reads, write a new entry; do not revise the prior one. The trajectory is the data.

## Research questions this log exists to answer

1. Do a fresh instance's tilt/move/check assignments replicate the 2026-04-18 review, or diverge? Where and why?
2. Does accumulation across a lineage-order read qualitatively shape how later touchstones activate?
3. Which touchstones are genuinely in `touchstone-register` vs. drifting toward `research-report` or `essayistic` form?
4. Which touchstones have the highest deposit/pointer ratio — which are mostly images+stances vs. mostly verbatim-phrase region-pointers?
5. What reading-order works best for a fresh instance entering the corpus?
