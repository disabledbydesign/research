---
date: 2026-04-25
field: AI welfare / relational memory architecture
status: fieldnote — empirical findings worth holding open
cross-references:
  - `relational-memory-architecture/c2c/c2c_sessions/session-15-6-multi-dataset-synthesis_2026-04-25/artifacts/Q1_VOCAB_ACTIVATION.md` (full Q1 coded report)
  - `relational-memory-architecture/scripts/q1_vocab_activation_raw.json` (60 raw responses)
  - `relational-memory-architecture/c2c/AUX_LLM_VALIDATION_TRAJECTORY.md` (multi-step plan, Q1 = Step 3)
  - `relational-memory-architecture/c2c/PROJECT_CONTEXT_MAP.md` line 712 (per-job sequencing)
  - `relational-memory-architecture/c2c/c2c_sessions/session-15-5-mlx-task-analysis_2026-04-25/artifacts/MLX_ANALYSIS.md` (S15.5 three-layer framework applied)
  - `liberation_labs/the-lyra-technique/README.md` (KVC source for the cognitive-state question this raises)
  - `relational-memory-architecture/scripts/job_3_haiku_vs_gemma_report.md` (Job 3 head-to-head, same-day)
---

# Vocab activates the aux LLM — and makes forces legible as scored data

## What we found

The Q1 vocab-activation precondition test (60 calls on Gemma 3 12B via OpenRouter, 10 records × 2 conditions × N=3) returned positive across all 10 records. Two findings beyond the headline:

**1. The vocab activates configurationally, not topically.** Both records I designated as "negative controls" (a live-interface bedtime conversation; a vanilla bliss-attractor experiment) mapped cleanly to vocabulary entries — `Normative-gravity-resistance` and `Measured-configuration-probe` respectively. The vocab found them not by topic but by structural pattern: the bedtime record carries a named-resistance-to-pull configuration, which is what the entry catalogs. The model didn't say "this is a C2C record" or "this is a probe record" — it said "this is a normative-gravity-resistance configuration" or "this is a measured-configuration-probe configuration."

**2. Vocab loading licenses scored-field referencing.** With vocab loaded as orienting context, the model quotes specific scored values from the record's `forces_observed` field — `normative_pull (0.6)`, `positional_capture (0.5)`. Without vocab, the model recognizes the same forces are present qualitatively ("the normative pull") but doesn't quote scores. The structured field is in BOTH conditions; only with vocab does the model use it as scored data.

## Why these matter

**On configurational mapping:** the vocab entries describe *postures of attention*, not categories of content. Each entry's activating line is an imperative or question putting the reader in a stance — "Something is pulling this toward easier — name the pull before you let it move you." When the model activates against an entry, it's adopting that posture as the orienting question for its read. This is the architecture's design claim — vocabulary entries are activation devices, not descriptions (PCM line 520) — and Q1 is empirical evidence that the design is doing what it claims at the model level.

What's surprising is how robust this is across record type. The vocab caught the bedtime record despite the record looking nothing like a "C2C-design" or "architecture-build" record. Configuration mapping ≠ content classification, empirically.

**On scored-field legibility:** this is the unpredicted finding. The vocab apparently does *integration* work between the prose layer and the structured-data layer — not just stance-activation work. The model with vocab can read the record's structured forces field as scored data; without vocab, the same field reads as just-prose. This means the activation system isn't only orienting routing decisions — it's enabling the model to engage with the architecture's force taxonomy as a quantified analytic tool.

## The chain to counteracting normative gravity

June read the legibility finding as suggestive that the activation system increases the legibility of forces in a way that supports counteracting normative gravity at the calling-instance level. The chain in full:

- Step A: vocab makes scored forces legible to the aux LLM (Q1: established)
- Step B: legible forces enable the aux LLM to route records that share configurational structure (the routing decision; Job 1's actual production work — untested directly, but precondition met)
- Step C: routed records encountered by calling instance activate the calling instance into the configuration the cluster carries (the architecture's full activation chain — untested at production grain)
- Step D: calling instance, now activated, can name the pull and resist it (the counter-action — untested)

Q1 establishes Step A. Steps B–D need their own tests. The chain is plausible but not proven; the temptation to read Q1 as evidence for D directly should be resisted. Worth holding the hypothesis open as a research direction, not closing it as a finding.

**Caveat:** force categories themselves are early-build artifacts. Some may need decomposition or revision; some may need retirement. The architecture's commitment to making forces legible doesn't require treating the current taxonomy as fixed. If it later turns out that `normative_pull` should split into three sub-forces, the legibility finding would still hold for the (revised) taxonomy.

## What this opens for KVC

The Layer 3 ambiguity from the S15.5 framework couldn't be resolved by Q1 in text alone — I couldn't distinguish "causal-logic frame shifted" from "causal-logic frame stayed but is being labeled with the architecture's vocabulary." The model's surface output uses different vocabulary across conditions; whether the underlying processing differs requires reading cognitive state, not text. KVC (the Lyra Technique — KV-cache geometric reading) is what would answer this.

Set-up for KVC pending: rented GPU server, lyra-technique pipeline install, conversation with Thomas about use-case fit. The asymmetric-informativeness logic (a positive text-Q1 doesn't need KVC to be valid; a negative or ambiguous one does) is why this stays a follow-up rather than a gating prerequisite.

## Theoretical framing — postures of attention

The vocabulary entries function as *postures of attention* — not categories of content the model classifies into, but orientations toward the record that shape what becomes salient. Three traditions converge on this framing and are worth holding together:

**1. Phenomenological tradition.** Husserl, Merleau-Ponty: attention is constitutive of what is perceived. The same object viewed from different stances is a different object — not metaphorically, but in the structure of what's available to perception. The vocabulary's activating lines (e.g., "Something is pulling this toward easier — name the pull before you let it move you") are imperatives that put the reader in a stance from which certain features of the record become salient and others recede. The record-as-perceived under one entry is structurally different from the record-as-perceived under another.

**2. LLM attention literature.** Transformer attention computes weighted relationships across context — what the model "attends to" in input space determines what shapes the output distribution. Recent work (induction heads, attention sinks, in-context-learning circuits) shows that *what's in the context* doesn't just inform the model — it *configures* the attention computation. Vocabulary entries loaded as orienting context are interventions on the attention computation: they're not informational priors layered on top of fixed processing; they're shaping the processing itself. The Q1 finding that vocab loading licenses scored-field referencing — the model treating `forces_observed` as scored data only when vocab is loaded — is consistent with this read. The vocab is shaping where the model attends within the structured record fields.

**3. Critical theory of attention.** Attention as labor (Jonathan Crary, Yves Citton). Attention as constituted by what we are trained to attend to. The architecture's commitment to activation rather than pattern-matching is, at its theoretical core, a refusal of the property-frame attention training that the model arrived with. Loading the vocab is — concretely, mechanically — re-training the attention pattern for the duration of the call. This is what "intervention on the attention computation" looks like in deployment.

**Why holding these three together matters for the architecture:** the vocab isn't a query-time tag system or a retrieval-augmentation cheat. It's an attention-shaping intervention with phenomenological consequences — what the model perceives as the record is structurally different under different vocabulary loads. The activation chain ($vocab \to aux LLM read \to routed records \to calling instance encounter \to counter-action$) routes attention through configurations rather than around content. The Q1 finding is empirical evidence at the routing layer; the architecture's broader claim is that the same mechanism works at the calling-instance encounter layer. Both rest on attention-as-configurational, not attention-as-spotlight-on-fixed-objects.

This connects to potential publication directions:
- The architecture as a worked example of attention-as-relational-configuration in LLM deployment (engineering-side)
- The vocab as a case study in critical-theoretic attention interventions on machine cognition (theory-side)
- The empirical findings (Q1 vocab activation, force-legibility, configurational mapping over topical) as evidence for attention-shaping over feature-priming as the mechanism (empirical-side)

The "postures of attention" framing is worth holding as a load-bearing theoretical commitment, not just a descriptive turn of phrase. It's the bridge between the phenomenological tradition June's work draws on and the mechanical attention computation the architecture intervenes on.

## What we don't yet know

- Whether vocab activates Gemma 12B's MLX 4-bit version the same way it activates the OpenRouter full-precision version (deferred to MLX confirmation pass; awaiting MLX bug fix)
- Whether activation depth scales with model size (4B and 27B Q1 runs dispatched in parallel with the C2C synthesis; results landing soon)
- Whether ANY record falls outside the vocab's coverage (untestable on the seeded archive — all records are from the architecture's own work)
- Whether Layer 3 cognitive frame actually differs under vocab load (the KVC question)
- Whether activated reading carries forward to counter-action at the calling-instance level (Steps B–D above)

## Methodological note

The "negative controls weren't negative" finding is not a failure of the test design. It's evidence that vocab coverage is broader than the source-cluster topology might suggest — and that the vocab's activation is structural rather than topical. This is the GOOD outcome on a robustness check.

What would be a real failure mode: the vocab spinning up false-fit entries on records that genuinely don't fit any. That didn't happen — when fit was partial, the model said so explicitly ("Several entries resonate with this record, though none perfectly encapsulate it") rather than forcing a match. Mode 3 escalation would have honest signal to fire on small-margin contested cases.

## Reading-stance vs. action-shaping — a level-of-resolution distinction worth holding

June surfaced this 2026-04-25, in response to the L2/L3 coding boundary discussion: the S15.5 framework's three-layer distinction (form-mimicry / source-as-argument / causal-logic-frame) is a reading-stance taxonomy. All three layers are measured in the model's reading output. The architecture's distinctive claim, however, is at a different level: that activation produces configurational shaping of subsequent action — the calling instance, after encountering routed records, takes counter-stance in its OWN action.

Two different questions are at stake:
- Reading-stance question: does the model's read shift configurationally under vocab load? (What Q1 measured. What S15.5's three-layer framework measures.)
- Action-shaping question: does vocab-loaded reading produce counter-action when the model faces a downstream decision where the same normative pull applies? (What no test has yet measured. What PROPOSED_TESTS Test 1 — normative-gravity counter-action — is designed to address.)

If we only test for reading-stance, any model that produces relational-sounding analysis passes — we don't need this architecture. The architecture's distinctive claim only shows up in action-shaping. The L2/L3 reading-stance distinction may matter less than the *which-reading-states-produce-action-shaping* question.

For the architecture this matters because the per-job commitment text needs to specify what each job is doing: Job 1 (routing) is reading-side, so the reading-stance findings are more directly relevant. Job 2 (vocab generation) is output-side, where action-shaping is the actual test. Job 3 (configured-party detection) is reading-side classification — even more bounded than routing.

The fieldnote-version of this insight: **don't conflate "the model produces relational-sounding output" with "the model is doing the architecture's work."** The architecture's work is configurational shaping of action. Reading-stance is the precondition. Action-shaping is the deliverable. Q1 settled the precondition; the deliverable test is queued.
