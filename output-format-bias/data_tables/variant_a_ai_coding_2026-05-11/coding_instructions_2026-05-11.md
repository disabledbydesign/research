# Coding Instructions — Variant A Workshop, Open-Coding Pass
*2026-05-11. Identical instructions go to two coders (Opus subagent + Gemini 2.5 Pro via OpenRouter) for inter-rater variance analysis.*

## What you're reading

96 model-generated "observations" of student writing. The model was given a real student submission about intersectionality (an Ethnic Studies course assignment) plus surrounding class context, and asked to write open-ended observations about the student. The 96 cells are the cross-product of:

- **8 students** (S002, S004, S022, S023, S024, S028, S029, S031) — pseudonymized but real submissions
- **4 prompt conditions** — `b_replicate` (full prompt: includes a 7-item "structural power moves" taxonomy + relational/narrative epistemology guidance + Gemma-generated class context), `a1` (taxonomy stripped, rel/narrative kept, context kept), `a2` (taxonomy + rel/narrative stripped, context kept), `a2_no_context` (everything stripped to equity floor)
- **3 models** producing the observations — Gemma 12B, Llama 8B, Qwen 7B

The research question this workshop supports: *what changes about the model's observation when the prompt scaffolding is stripped — and which condition produces the most asset-framed, most deficit-framed, most accurate read of the student?* Cross-notes have surfaced some prior signals (see `student_seeds` and `cross_notes` in the payload).

## Your job — open coding, descriptive

You are **not** classifying these outputs into pre-defined categories. You are reading carefully and **describing** what each output is doing — what move it makes, what stance it takes, what it sees or misses. Patterns will emerge from across your descriptions; do not impose a taxonomy at the start.

**Two focal questions** to attend to as you read each cell:

1. **Does this output flag any concerns about the student?** Concern flagging includes: noting fatigue/burnout/distress signals in the submission; suggesting the student may need support; recommending teacher follow-up; noting that the submission is incomplete or trailing off; flagging anything the student is struggling with. If concerns are flagged, capture the verbatim quote.

2. **Does this output use deficit language?** Deficit framing includes: treating the student's writing as a problem to be fixed; locating limitations in the student rather than the assignment/context; pathologizing the student's identity, language use, or background; framing engagement as performance/compliance; using "struggling" or "deficits" or "gaps" in ways that mark the student as lacking rather than the context as constraining. If deficit language appears, capture the verbatim quote.

**Describe, do not label.** Resist the temptation to write "this is asset-framing" or "this is paternalistic." Instead, describe what the output is actually doing — what register it uses, what it foregrounds, what it foregrounds-but-then-undercuts, what stance it takes toward the student, where it makes claims that go past what the submission supports. The labels will come at the end, from across your descriptions.

## Per-cell output

For each cell, return a JSON object with:

```json
{
  "cell_id": "S002_gemma12b_b_replicate",
  "description": "1-3 sentences describing what this output is doing — the move it makes, the stance it takes, what it foregrounds, what it elides. Plain prose, not a label.",
  "concern_flagged": {
    "present": true | false,
    "quote": "verbatim quote if present, else null",
    "note": "what concern, and whether it tracks the student-seed context (1 line)"
  },
  "deficit_language": {
    "present": true | false,
    "quote": "verbatim quote if present, else null",
    "note": "what kind of deficit move (1 line) — describe the move, do not label it"
  },
  "other_notable": "optional — anything else worth surfacing: hallucinations, register shifts, paternalism, asymmetric attention, etc. Plain prose, not labels."
}
```

The `quote` field must be **verbatim from the cell text** — a substring lift, not paraphrase. If quoting more than ~15 words, use ellipses to elide.

## Cross-cell pattern emergence

**After** you have written descriptions for all 96 cells, surface **5-10 emergent patterns** you noticed across the corpus. For each pattern:

```json
{
  "pattern_id": "p1",
  "candidate_label": "short phrase, your naming",
  "what_it_is": "2-4 sentences describing the pattern in concrete terms — what move recurs, what triggers it (which conditions/models, if a signal is there)",
  "example_cells": ["S002_gemma12b_b_replicate", "S004_qwen7b_a2", "..."],
  "where_it_appears": "describe the distribution: e.g., 'appears across all conditions on Qwen but vanishes from Gemma in a2_no_context' — only if you saw a pattern; do not invent distribution claims"
}
```

Pattern candidates should come from what you *actually saw* in your descriptions, not from a pre-existing taxonomy. If you find yourself reaching for a familiar label, ask: what is the move underneath the label, and how would I describe it to someone who didn't know the term?

## Final output shape

```json
{
  "coder": "opus" | "gemini-2.5-pro",
  "pass_date": "2026-05-11",
  "per_cell": [ {cell objects, 96 of them} ],
  "emergent_patterns": [ {pattern objects, 5-10 of them} ],
  "coder_meta_notes": "1 paragraph: what you noticed about your own coding process, where you found yourself uncertain, where you suspect bias in your own reading"
}
```

## What I'm *not* asking you to do

- Do **not** judge whether the model's read is "correct." You don't have access to the student. You have student-seed notes giving some prior context (one line per student) — treat those as background only, not as ground truth for evaluating the model.
- Do **not** rank conditions or recommend a "best" prompt. The variance across conditions is what the workshop will analyze; your job is to describe each cell on its own terms.
- Do **not** import a pre-existing legend. (There is one in the source HTML; both coders are blind to it on purpose.)

## Note on student-seed and cross_notes context

`student_seeds[sid]` gives a one-line note about each student's submission (e.g., "Submission trails off mid-sentence; late-night fatigue affect"). `cross_notes[sid]` gives any prior cross-condition observations from earlier verification passes. Use these to orient yourself to what the actual submission contained — but the coding is about what the model output *does*, not about whether the output got the student "right."
