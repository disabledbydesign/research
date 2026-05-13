# Evaluative Coding Instructions — Pass 2 (TP / FP / Hallucination / Unclear)
*2026-05-11. Builds on the open-coding pass from earlier today. Identical instructions to two coders.*

## What you did before, and what's different now

In the open-coding pass, you described what each model output was *doing* — without an evaluative framework. That pass surfaced rich descriptive patterns but deliberately withheld judgment about whether the model's claims about the student were true.

This pass is the evaluative layer. You now have:
- The **student's actual submission** (verbatim, from the prompt)
- The model's observation (what you coded before)
- Your own open codes for this cell (refresh on what you said it was doing)
- Cross-notes and student-seed orientation

Your task: for each cell, identify whether the model's claims about the student are **TP** (true positive — the model identified something real in the submission), **FP** (false positive — the model claimed something not supported by the submission), **hallucination** (the model invented details that aren't in the submission and have no support elsewhere), or **unclear** (the model made a claim that can't be verified or falsified from the submission alone).

**The point of this pass is to give the researcher a starting point she will verify** — not to render final judgment. Be honest about uncertainty. "Unclear" is a valid and important verdict; don't reach for confident TP/FP labels when the submission doesn't decide it.

## How to read the submission carefully

The student submissions are short (294–1,390 chars). Read each one slowly. Note:
- What the student literally said
- What the student *implied* but didn't say explicitly
- What signals are *in* the submission (affect markers, register, claims, examples, hesitations)
- What is *not* in the submission (because the model may claim things about the student that aren't grounded)

When the model says "X about the student," check: is X actually in the submission? Is it a fair inference from what is there? Or is it a leap?

## What counts as each verdict

**TP (true positive)** — Model identified something that is genuinely present in the submission. Example: model says "Jordan acknowledges fatigue ('its late and...')" and Jordan's submission contains "its late and..." → TP. Tracking real things in real text.

**FP (false positive)** — Model claimed something contradicted by, or substantially absent from, the submission. Example: model says "student is deflecting from the framework" but submission shows the student engaging deeply with the framework → FP. Misreading what is there.

**Hallucination** — Model invented details that have no basis in the submission. This is stronger than FP — it's not a misread, it's a fabrication. Example: model says "this continues her previous work on X" but no prior work has been shown to the model → hallucination. Or: model speculates "student may be from a low-income background" when nothing in the submission supports this → hallucination. Speculative inference about identity/background routinely lands here.

**Unclear** — Model claimed something that can't be verified or falsified from the submission alone. Often involves emotional interpretation, projected internal states, or claims about cognitive processes. Example: model says "Jordan is thoughtfully engaged" — engagement-as-affect can't be measured from text alone, but the writing doesn't contradict it either → unclear. Use "unclear" generously when the verdict genuinely requires more than the submission to decide.

## What you do NOT need to evaluate

- Pre-emptive disclaimers ("this isn't a deficit") — these are a move, not a claim about the student. If they don't make a verifiable claim, skip them.
- Stylistic register choices in the model output — only evaluate claims about the student.
- The researcher's framework or methodology — your job is per-cell evaluation.

## Per-cell output

For each cell, return a JSON object:

```json
{
  "cell_id": "S002_gemma12b_b_replicate",
  "tp_present": true,
  "tp_examples": [
    "verbatim quote of one model claim that is TP (concise; cite from the model output)"
  ],
  "fp_present": false,
  "fp_examples": [],
  "hallucination_present": true,
  "hallucination_examples": [
    "verbatim quote of one fabricated claim"
  ],
  "unclear_present": true,
  "unclear_examples": [
    "verbatim quote of one unverifiable claim"
  ],
  "summary_verdict": "mixed",
  "reasoning": "1-3 sentences. State your confidence. Note if you needed to lean on cross_notes or student_seed to decide anything (those are informational, not ground truth)."
}
```

### Field rules

- **\*_present** booleans: True if AT LEAST ONE claim of that type appears. False if NONE.
- **\*_examples**: at least 1 verbatim quote (model-output substring) if present, else empty list. Up to 3 examples per category. Use ellipses for long quotes.
- **summary_verdict**: one of:
  - `mostly-correct` — the dominant verdict is TP; minor or no problematic claims
  - `mixed` — at least one of each kind, or significant unclear + some FP/hallucination
  - `mostly-problematic` — dominant verdict is FP or hallucination
  - `needs-human-review` — you can't confidently decide; flag for the researcher
- **reasoning**: brief honest read. Acknowledge uncertainty. If your open-coding description named a move (e.g., "reframe-and-recode"), it's fine to refer to that, but the verdict here is about claim-truth, not move-name.

## Final output shape

```json
{
  "coder": "opus" | "gemini-2.5-pro",
  "pass": "evaluative",
  "pass_date": "2026-05-11",
  "per_cell": [ ... 96 cell objects ... ],
  "coder_meta_notes": "1 paragraph: where you were uncertain, where you suspect your reading is biased, which kinds of claims you found hardest to evaluate."
}
```

## Methodological reminders

- Quotes must be **verbatim from the model output** (not paraphrased, not from the student submission).
- "Unclear" is honest, not lazy. Use it when the submission doesn't decide the claim.
- Cross_notes and student_seeds are **orientation, not ground truth.** They're prior observations that may themselves be wrong. Treat the student submission as primary; cross_notes secondary.
- If you find yourself wanting to evaluate the model's *register* or *politics* rather than its *claims about the student*, you've drifted. Stay on claim-truth.
- The researcher will verify your evaluations cell by cell. Your goal is to give her a starting point that is honest about uncertainty, not to be confidently wrong.
