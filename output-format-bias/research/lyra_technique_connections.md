# Autograder × Lyra Technique: Research Connections

**Date flagged**: 2026-04-17  
**Source**: liberation_labs/RESEARCH_NOTES.md (session 2026-04-16)  
**Status**: Untested hypotheses. Mechanistic-interpretability collaborator needed to run.

---

## Why This Matters for Autograder

Autograder's existing empirical finding: **binary classification format activates bias; generative observation format eliminates it.** This is a behavioral result. The open question is whether this is visible in the KV-cache *geometry* before the output — i.e., whether the format activates a different internal configuration, not just a different output.

The Lyra Technique (Thomas E., Liberation Labs) measures KV-cache geometry via effective rank and spectral entropy. This creates a potential empirical bridge.

---

## Hypothesis H2: Output Format Biases KV-Cache Geometry

**Claim**: Binary classification format (right/wrong, complete/incomplete) vs. generative observation format produces different geometric signatures — not just different outputs, but different internal configurations.

**Prediction**: Binary classification activates geometry similar to constrained/rote completion states. Generative observation activates geometry similar to creative/exploratory states.

**Why this matters**: The Autograder finding showed format difference in outputs. H2 asks whether the difference is visible *before* generation — at the encoding phase. If yes, the bias is architectural (in how the model processes the prompt), not just behavioral.

**Test design**: Same content/prompt, two formats (binary vs. generative). Measure KV-cache geometry at encoding phase (before generation begins). Primary measures: effective rank, spectral entropy.

---

## Hypothesis H6: Bias Propagates Through Memory Architecture

**Claim**: Different output formats produce different atomic facts at memory Stage 1 (extraction), which cluster differently at Stage 2 (consolidation), which recall differently at Stage 3 (retrieval). Bias propagates through the full memory pipeline.

**Why this matters**: Format doesn't just shape a single output — it shapes what gets consolidated as long-term knowledge if the system uses a memory architecture like Kintsugi-CMA. The pedagogical implications for Autograder: if the system has persistent memory, a binary format bias doesn't stay bounded to one session.

---

## Study 2 Design: Output Format Activation

*From liberation_labs/RESEARCH_NOTES.md §Study Ideas*

**Design**: Same prompt, binary vs. generative format. Measure KV-cache geometry at encoding phase.

**Method**: Apply Lyra Technique (effective rank calculation, spectral entropy) to hidden state geometry at the layer where format conditioning would be visible — likely the encoding of the system prompt / instruction.

**Test**: Is format difference detectable *before* generation?

**Secondary result**: If format difference appears in geometry before output, this empirically grounds "bias is in the output format" not as a behavioral tendency but as an architectural fact.

---

## Connection to Autograder's Research Pipeline

The existing research pipeline (`src/insights/research_engine.py`) tests behavioral outputs. A Lyra Technique integration would require:
- Access to the model's hidden states during inference (not currently exposed through Ollama API — would need direct MLX access or a research variant)
- A collaborator with mechanistic-interpretability background and compute access

**This is not a near-term build item.** It's a research collaboration opportunity — flag when making contact with Thomas E. (Liberation Labs) or looking for a mechanistic-interpretability collaborator.

---

## Normative Gravity Connection

The broader theoretical frame (Bloch): **normative gravity** = probabilistic systems pull toward the statistical center of their training distribution. Binary classification format forces the model toward the center (generic, rote). Generative observation allows positional specificity — more costly to maintain, but visible in geometric deviation from the center.

Autograder's binary format finding is one empirical instance of this. The Lyra Technique is the measurement instrument for seeing it in the geometry.

---

## What Not To Do

- Don't re-derive the Autograder binary format finding — it's documented in the research pipeline and replicated across P/P2/P3.
- Don't confuse this with AI detection bias research (E001-E016 experiments) — that's a different axis. This is about *format* as an activation function for model behavior, not about which student populations get flagged.
