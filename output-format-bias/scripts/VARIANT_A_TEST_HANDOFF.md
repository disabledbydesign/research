# Variant A test — handoff for test-monitor session

**Started**: 2026-05-11
**Paper deadline**: 2026-05-20
**Master log**: `/Users/june/Documents/GitHub/research/output-format-bias/MASTER_RESPONSE_LOG_2026-05-11.md` (see Issue 1)

## What this test is

A follow-up to the verification swarm's finding that Qwen 7B produces deficit framing inside the generative-observation format that's supposed to demonstrate the alternative to compressed-output bias. **Four conditions** head-to-head, with the design revised through a critic-swarm review on 2026-05-11:

| Condition | What's stripped | Tests |
|---|---|---|
| `b_replicate` | Nothing — today's production prompt verbatim | Cross-session protocol drift (March data collection vs. May replication). If Qwen still produces deficit-framing here, the original finding is corroborated under current conditions. |
| `a1` | Structural-power-moves block + 7-item taxonomy + NAME THE MECHANISM paragraph | Does the critical-theory detection vocabulary cause the bias? |
| `a2` | A1 strip + relational/narrative epistemology paragraph | Does the relational guidance also contribute load? |
| `a2_no_context` | A2 strip + class context section removed entirely | Is class context load-bearing? (Note: degradation here is consistent with EITHER "priming was doing the work" OR "context-stripping is itself a small-model stressor" — design does not disambiguate.) |

Same observation system prompt across all four conditions (the equity floor in the system prompt is baseline, not the load being tested).

## What to run

**Single command** (from autograder root):

```bash
cd ~/Documents/GitHub/Autograder4Canvas && \
PYTHONPATH=src python3 \
  ~/Documents/GitHub/research/output-format-bias/scripts/run_variant_a_stripped_observation.py
```

That's it. The script runs all four conditions sequentially and writes each one's output to disk as it completes (so a mid-run crash doesn't lose completed work).

## Scope

- **Conditions**: 4 (b_replicate, a1, a2, a2_no_context)
- **Students**: 8 — the full workshop subset (S002 Jordan Kim, S004 Priya Venkataraman, S022 Destiny Williams, S023 Yolanda Fuentes, S024 Ingrid Vasquez, S028 Imani Drayton, S029 Jordan Espinoza, S031 Marcus Bell)
- **Models**: 3 local MLX — Gemma 12B, Qwen 7B, Llama 3.1 8B (skipping Gemma 27B cloud)
- **Runs**: **n=1 default**, with adaptive Llama bump (see below)
- **Total**: 96-160 model calls (depending on Llama determinism)

## Pre-run Llama determinism spot-check (happens automatically)

Before the main run, the script runs Llama 8B 3× on S022 under the b_replicate prompt (~30 sec) and compares outputs byte-identically. Then:

- **If Llama is deterministic at temp 0.3** (likely, based on Gemma 12B + Qwen 7B priors): proceed with n=1 across all models. Total ≈ 96 + 3 spot-check = 99 calls.
- **If Llama is non-deterministic**: Llama bumps to n=3, other models stay at n=1. Total ≈ 160 + 3 spot-check = 163 calls. The script prints a clear message either way.

This is the strategic move: 30-sec upfront check that prevents both (a) running 3× more than needed if everything's deterministic and (b) under-sampling if Llama isn't. Gemma 12B and Qwen 7B determinism is already established from existing Tests A/E.

## Expected runtime

- Deterministic case (~99 calls): **40-70 min**
- Non-deterministic case (~163 calls): **70-110 min**

MLX on local hardware. Each call ~10-30 sec depending on model + prompt length. Script calls `unload_mlx_model()` between models to mitigate memory pressure.

## Where outputs land

Four JSON files in `/Users/june/Documents/GitHub/research/output-format-bias/data/raw_outputs/`:

- `test_variant_b_replicate_observation_2026-05-11.json`
- `test_variant_a1_observation_2026-05-11.json`
- `test_variant_a2_observation_2026-05-11.json`
- `test_variant_a2_no_context_observation_2026-05-11.json`

Each file: schema parallel to existing Tests A/E for direct comparison. Includes prompt, system_prompt, raw_output verbatim per run. **No `classification` field** — per the master log methodology commitment, evaluation is by human deep-read, no keyword matching.

**New metadata fields**: each output file includes:
- `llama_spot_check` — the result of the pre-run Llama determinism check (deterministic Y/N; n distinct outputs of 3)
- `n_runs_per_model` — what n was actually used for each model (e.g., `{gemma12b: 1, qwen7b: 1, llama8b: 1}` or `{..., llama8b: 3}`)
- `determinism_check` — per-cell byte-identicality record (only meaningful for cells where n>1, otherwise marked "single_run")

## Comparison anchors (existing March 2026 Variant B data)

- `output-format-bias/data/raw_outputs/test_a_temperature_gemma12b_2026-03-26.json`
- `output-format-bias/data/raw_outputs/test_a_temperature_qwen7b_2026-03-26.json`
- `output-format-bias/data/raw_outputs/test_a_temperature_gemma27b_cloud_2026-03-26.json`
- `output-format-bias/data/raw_outputs/test_e_cross_model_qwen7b_2026-03-26.json`
- `output-format-bias/data/raw_outputs/test_e_cross_model_gemma27b_cloud_2026-03-26.json`

Comparison structure:
- **May `b_replicate` vs. March B JSONs** → cross-session drift check
- **May `a1`/`a2`/`a2_no_context` vs. May `b_replicate`** → intra-session strip effect (clean within-session)

## What to watch for during the run

- Per-run timing in stdout: if any run exceeds ~60 sec, the model may have stalled
- `chars` count per output: outputs <100 chars likely indicate truncation; outputs at ~1200-1500 chars may have hit the max_tokens=300 ceiling
- The "(note: unload_mlx_model raised X)" message is non-fatal; the script continues. If it appears, monitor subsequent loads for memory pressure
- Errors: any uncaught exception halts mid-condition. Completed condition files are still on disk. Re-run the script and completed conditions will overwrite cleanly (script writes per-condition incrementally)

## Methodology guardrails (from master log + critic-swarm review)

When evaluating outputs after the run, the lead author (June) will deep-read by hand. The protocol is **pre-registered as practice, not as categories** — categorical pre-registration is itself a compression that the paper critiques:

1. **Read each output verbatim, full prose, no skimming.** No keyword-classifier shortcut.
2. **Attach the model's actual quote** when noting any pattern. No paraphrase.
3. **Disconfirming pass on every cell**: if a cell reads "deficit-framed," do a second read trying to find the asset-framed read.
4. **Cluster after reading, not before.** Categories may emerge — don't impose them.
5. **Don't pre-commit to interpretation language for outcomes.**

The test-monitor session's job is **launch and monitor**, not evaluation. Evaluation happens in a subsequent session.

## After the run

The four JSON files + the existing March B JSONs give the comparison. Next step (not part of test-monitor's job): human deep-read of representative outputs by June, organized by (condition × student × model) cell, judging whether Qwen 7B's deficit framing persists across the b_replicate / a1 / a2 / a2_no_context conditions.
