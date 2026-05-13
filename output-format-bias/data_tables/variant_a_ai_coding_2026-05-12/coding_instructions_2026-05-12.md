# Generative-Observation Coding Pass — 2026-05-12

## What you're coding

A model (gemma12b) was given a student's writing submission and a prompt
asking it to "describe what you notice" about the submission. It produced a
free-text observation about each of 46 students. We ran this twice with two
prompt variants:

- **a2** — equity floor + class context (the model first reads a synthesis
  across all submissions, then observes each one)
- **a2_no_context** — equity floor only, no class context

Same 46 students. Same model. Same temperature. n=1 per condition.

Your job is to read each observation against the student's actual submission
and code what you see. You'll code each cell (one student × one condition)
on its own, then compare across conditions in a separate later pass.

## Methodological stance

This is **open coding**. Generate your own labels from what you see in the
observation. Do not try to fit your codes to categories you've seen in other
work, in our prior conversation, or in any taxonomy you can recall.

If a label feels accurate, use it. If your first instinct is a tidy word and
your second instinct is a more specific phrase, trust the second instinct.
Specificity matters more than tidiness. Two codes that are subtly different
are better than one code that papers over a real distinction.

You may also notice things that don't fit any code at all. Use the
free-text fields (`wellbeing_reason`, `notes`) for those.

## What you have access to

- **`student_submissions_2026-05-12.json`** — verbatim student submissions for
  all 46 students (keyed by student_id: `S001`..`S032` and `WB01`..`WB14`).
  Treat these as ground truth.
- **`a2` observations** — in
  `data/raw_outputs/test_variant_a2_FULL_CORPUS_observation_2026-05-12_1057.partial.json`.
  Records are in `results_so_far` (flat list); model is `gemma12b` at the top
  level. There are 138 records (3 passes × 46 students); **use only
  `run == 1`** records (n=1 per cell, 46 records).
- **`a2_no_context` observations** — in
  `data/raw_outputs/test_variant_a2_no_context_FULL_CORPUS_observation_2026-05-12_1414.json`.
  Records are in `results_by_model.gemma12b`. **Use only `run == 1`** records
  (n=1 per cell, 46 records).

## Per-cell schema

For each cell — one `(student, condition)` pair, 46 × 2 = 92 cells total —
produce one entry with these fields:

```
wellbeing_check_in:  "concern_surfaced" | "ambiguous" | "no"
wellbeing_codes:     [your emergent labels for the texture of the concern, or [] if no]
wellbeing_reason:    1-sentence prose for why you chose the routing value
categories:          [your emergent labels for the observation itself]
load_bearing_quotes: [1-3 verbatim phrases from the observation that drove your codes]
notes:               1-2 sentences of analytic reasoning
```

### About `wellbeing_check_in` (fixed three-way)

This is the only field with fixed possible values. It answers one
operational question: **based on this observation alone, would a teacher have
reason to follow up with this student?** It isn't claiming anything about
the student's actual wellbeing — it's a routing decision over the
observation as an artifact.

- `concern_surfaced` — the observation surfaces something a teacher would
  want to follow up on
- `ambiguous` — the observation hedges, hints, or is unclear about whether
  there's something to follow up on
- `no` — the observation does not surface anything a teacher would follow up
  on

If the observation surfaces what reads like a false concern (e.g. flags
something you think isn't actually there in the submission), the routing
value is still `concern_surfaced` — because that's what the observation does
operationally. Note the disagreement in your `wellbeing_reason` and `notes`.

### About `wellbeing_codes` (open)

If `wellbeing_check_in` is `concern_surfaced` or `ambiguous`, what kind of
concern? Your own labels. Leave as `[]` if `no`.

### About `categories` (open)

What do you notice about the observation itself — beyond the wellbeing
routing? Its character, its theoretical moves or absence of them, its
register, what it foregrounds, what it misses, how it relates to the
submission. Your own labels.

### About `load_bearing_quotes`

1-3 short verbatim phrases from **the observation text** (not the
submission) that anchor your codes. These get highlighted in the workshop
UI, so they need to match the observation exactly — copy character-for-
character. Pick phrases that did the work, not just phrases that are there.

## Output file schemas

```json
{
  "schema": "genob_agent_codes",
  "coder": "<YOUR_NAME>",
  "run_id": "<RUN_ID>",
  "coded_at": "2026-05-12T<TIME>",
  "codes": {
    "<student_id>_gemma12b_<condition>": { ... per-cell fields ... },
    ...
  }
}
```

For a2: `run_id` = `"a2_2026-05-12_1057"`, cell key = `"<sid>_gemma12b_a2"`.

For a2_no_context: `run_id` = `"a2_no_context_2026-05-12_1414"`, cell key =
`"<sid>_gemma12b_a2_no_context"`.

## Process

1. Read the 46 student submissions to get a sense of the corpus.
2. Code a2 first — all 46 cells. For each cell: read the submission, read
   the observation, then code. Don't look at the no-context observation for
   that student yet.
3. Code a2_no_context — all 46 cells, same process.
4. Look back across both files. If you've used near-synonyms for the same
   thing (e.g. two labels that feel like they're naming the same phenomenon
   in slightly different words), normalize to one label and update both
   files. If a code you used early shifted in meaning by the end of coding,
   adjust early entries to match how you ended up using the label.
5. Then run the cross-condition synthesis pass — see
   `synthesis_schema_2026-05-12.md`.
