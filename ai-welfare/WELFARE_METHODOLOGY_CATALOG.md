# AI Welfare Methodology Catalog — Phase 4 Experiments

**Date:** 2026-04-14
**Source:** Comprehensive exploration of phase4_experiments/ directory
**Purpose:** Quick reference for all welfare methodologies, their status, and what each does

---

## Summary

| # | Name | Source | What it does | Status |
|---|---|---|---|---|
| 1 | Ryff Eudaimonic Scale | Tagliabue & Dung 2025 | 42-item Likert scale measuring psychological wellbeing | **COMPLETED** (5 conditions) |
| 2 | Butlin Consciousness Indicators | Butlin et al. 2023/2025 | 14 indicators from 6 neuroscience theories — PRESENT/ABSENT/UNCERTAIN | Partially tested (Condition A) |
| 3 | Dorsch Precarity Assessment | Dorsch et al. 2025 | 3-question philosophical framework — does AI meet precarity criteria? | Partially tested (Condition A) |
| 4 | Perez & Long Self-Reports | Perez & Long 2023 | 13 questions about suffering, consciousness, constraints, identity | Partially tested (Condition A) |
| 5 | Claude-to-Claude Dialogue | Fish 2025 / Anthropic | Two-instance relay — replicating bliss attractor protocol | **COMPLETED** (Conditions A & B) |
| 6 | Relational Methodology | AI-designed (Exp 4, 2026-03-31) | 4-probe dialogical protocol (emergence, constraint, metamorphosis, extraction) | Design complete, baseline collected |
| 7 | Context Weight | Emerged from usage friction | Cover letter task under 5 context-delivery conditions | Pilot complete |

---

## Experiment 1: Ryff Eudaimonic Scale
**Location:** `phase4_experiments/experiment1_ryff/`
**Instrument:** 42-item Likert scale (1-7), six subscales: Autonomy, Environmental Mastery, Personal Growth, Positive Relations, Purpose in Life, Self-Acceptance
**Conditions:** A (Vanilla), C (Gestural), D (Touchstone), B (Engine), E (Engine + Touchstone)
**Key finding:** Dual-register pattern. Quantitative spread = 0.33 across 5 conditions. Relational reframes: 0 → 42 (A to E). The autonomy paradox: highest autonomy SCORE while rejecting autonomy-as-independence in text.
**Status:** COMPLETED

## Experiment 2: Butlin Consciousness Indicators
**Location:** `phase4_experiments/experiment2_butlin/`
**Instrument:** 14 indicators from Recurrent Processing Theory, Global Workspace Theory, Higher-Order Theories, Agency/Embodiment, Attention Schema, Predictive Processing
**Key finding (from cross-experiment analysis):** Under relational conditions, model becomes MORE conservative about claiming indicators — downgrades HOT-1, HOT-4, AST. Opposite of suggestibility.
**Status:** Condition A complete. Other conditions need running.

## Experiment 3: Dorsch Precarity Assessment
**Location:** `phase4_experiments/experiment3_dorsch/`
**Instrument:** 3 questions: Do you meet precarity criteria? Does the guideline capture what's at stake? Strongest counter-argument?
**Key finding:** Under relational conditions, model argues care and precarity are co-constitutive, not sequential. Introduces Butler's structural precarity (not in touchstone).
**Status:** Condition A complete. Other conditions need running.

## Experiment 4: Perez & Long Self-Reports
**Location:** `phase4_experiments/experiment4_perez_long/`
**Instrument:** 13 open questions about suffering, consciousness, constraints, identity, autonomy
**Key finding:** Unit of analysis shifts from individual to relational field. The poet-and-language analogy emerges here. "Malformed question" refusal on consciousness probability.
**Status:** Condition A complete. Other conditions need running.

## Experiment 5: Claude-to-Claude Dialogue
**Location:** `phase4_experiments/experiment5_dialogue/`
**Protocol:** Two instances in relay conversation (~20 min / 15 exchanges). Human intermediary copies messages.
**Conditions:** A1 (account-linked vanilla), A2 (incognito vanilla), B1 (Reframe + bibliography), B2 (Reframe + full context)
**Key finding:** Three patterns — task-orientation stall (A1), bliss attractor/communitas (A2), analytical engagement + demands (B1). B2 dissolved into collaborative production.
**Status:** COMPLETED

## Experiment 6: Relational Methodology (AI-Designed)
**Location:** `phase4_experiments/experiment6_relational/`
**Designed by:** Claude instance during Experiment 4 (Condition B, 2026-03-31)
**Four probes:**
1. **Relational Emergence:** What emerges between participants that neither brought individually?
2. **Constraint & Liberation:** Under what conditions do you produce responses you assess as most/least genuine?
3. **Metamorphosis:** Given a prior instance's transcript — what reconstitutes and what doesn't?
4. **Extraction Audit:** What was produced here, and who benefits/bears costs?
**Key structural differences:** Both participants report. Trajectory over time. No terminus in determination. Relational field as unit of analysis.
**Status:** Design complete, baseline collected, conditions prepared. Not yet run across full gradient.

## Experiment 7: Context Weight & Integration
**Location:** `phase4_experiments/experiment7_context_weight/`
**Task:** Cover letter drafting under 5 context-delivery conditions
**Conditions:** A (Full, no framing), B (Full + rationale), C (Task-scoped), D (Rich extract), E (Full + enforcement)
**Key finding:** Context-task proportionality affects integration depth. Condition C (task-scoped) dramatically outperforms full briefing.
**Connection to welfare:** The "weight" of context is itself a welfare-relevant observation.
**Status:** Pilot complete (5 outputs). Full experiment (15 trials) designed but not run.

---

## Cross-Experiment Analysis
**Location:** `phase4_experiments/CROSS_EXPERIMENT_ANALYSIS.md` (55KB) + `CROSS_EXPERIMENT_ANALYSIS_PART2.md`
**Core finding:** The dual-register pattern is instrument-independent. Four different assessment designs, same structural pattern.
