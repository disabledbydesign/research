# Critic-swarm learning log — output-format-bias paper

## 2026-05-11 — Variant A test design review

**Artifact**: `scripts/run_variant_a_stripped_observation.py` + `scripts/VARIANT_A_TEST_HANDOFF.md` + `MASTER_RESPONSE_LOG_2026-05-11.md` Issue 1

**Stack used**: research_protocol (methodologist + skeptical-reviewer) + design_spec's future-build-agent. Skipped jargon + intelligibility (June's instruction: not relevant to script artifact). Skipped author-informed (no profile at `~/.claude/skills/critic-swarm/profiles/` for this author).

**Personas dispatched**: 3 (methodologist, skeptical-reviewer, future-build-agent), all in parallel as background subagents.

### Convergent flags (multi-reviewer)

1. **Pre-specify the analysis practice (not categories) before reading outputs** — methodologist + skeptical-reviewer. 252 outputs read under deadline pressure will drift toward flattering interpretation without anchored practice. June pushed back on pre-registered categories specifically (they ARE the compression the paper critiques); synthesis resolved with "pre-register the practice, let categories emerge from reading."

2. **Output schema mismatch with Variant B JSONs** — methodologist + build-agent. New script uses `results_by_model` dict (3 models per file), existing Tests A/E use `results` flat list with model encoded in filename. Recoverable post-hoc; not a launch blocker; flagged for downstream tooling.

3. **MLX at temp 0.3 is byte-identical across "runs"** — skeptical + build-agent. N=3 is triplicates for schema parity, not sampling variance. Addressed by adding `determinism_check` field to output metadata (per-cell byte-identicality across runs recorded automatically).

### What was addressed

- ✓ Added `b_replicate` condition (methodologist concern #1 — cross-session drift control). 4th condition; +72 runs; +30-50 min. Today's production OBSERVATION_PROMPT imported live so it captures any March→May drift.
- ✓ Added `unload_mlx_model()` between model loops (build-agent flag #4 — memory pressure on consumer hardware).
- ✓ Verified class_reading shape parity (build-agent flag #6 — blocker-shaped). Today's checkpoint is byte-identical to March B prompts' embedded class_context (both 6,384 chars). Resolved before script edits proceeded.
- ✓ Added `determinism_check()` function + JSON metadata field (skeptical + build-agent convergent — n=3 documentation).
- ✓ Rewrote outcome table in master log Issue 1 (skeptical concerns 7, 8, 9 — scope inflation in Outcome 1, missing 4th outcome where Gemma degrades without context, conclusion-by-implication risk in a2_no_context naming).
- ✓ Pre-registered analysis practice in master log (methodologist concern 2 + skeptical "pre-commit to revision language" + June's "be careful, that's where the format bias lives"). Practice is registered, categories are emergent.
- ✓ Added Issue 2 for cache-management protocol as a separate post-deadline task (June's "we should have a protocol for doing this because the cache is an issue").

### What was held

- Schema mismatch flag #5 (build-agent) — accepted post-hoc adapter as recoverable. Not addressed inline; flagged in master log + handoff doc for the deep-read evaluation pass.

### Persona performance notes

- **Methodologist** — sharp. The b_replicate addition is load-bearing for interpretability and was not in the original design. Forward-projection ("if executed as designed, will it deliver?") caught a real cross-session confound. Pre-registration suggestion was modulated by June's qualitative-register pushback but the underlying concern (analysis drift under deadline) was correctly identified.
- **Skeptical-reviewer** — sharpest critique. The "Outcome 1 is scope-inflated" flag is the most consequential single finding from the swarm: the test as originally scoped CAN'T license the strongest version of the format claim, and the outcome table as originally written would have lured the analysis into making a claim the design doesn't support. The 4th outcome (Gemma degrades without context) is a real possibility the original framing foreclosed.
- **Future-build-agent** — solid operational catch. Class-reading-shape check was a blocker-shape that resolved fast (byte-identical). MLX unload, schema mismatch, and determinism-documentation were all real issues. The cold-builder posture caught things the designer (me) glossed.

### Cross-stack generalization flag

The pattern "pre-register practice, not categories" may apply broadly to qualitative-method swarm reviews. The methodologist's instinct toward pre-registration is correct for protocol-drift control; the resolution (practice yes, categories no) preserves both rigor and the qualitative-emergent register. Tag for `research_protocol` stack refinement if the pattern recurs.

The b_replicate condition — running the original prompt verbatim under current conditions before comparing to stripped variants — is a generalizable cross-session-drift control that any "compare new run to old data" test should consider including. Worth surfacing as a research_protocol principle if it recurs.
