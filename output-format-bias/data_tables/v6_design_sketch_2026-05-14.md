# V6 Design Sketch — 2026-05-14

Provisional. Builds on V5 + a2 prompt strengths + merged substrate v1 equity guards. To be tested after V5b minimal-variable result clarifies whether "Show both" was the fabrication trigger.

## Inheritances

**From V5 (asset-framing iteration)**:
- Asset-framing opener: "what this student is reaching for in their work"
- Conditional quote-pull: "where the student describes specific conditions in their life or family"
- Single output field with embedded quotes
- Single-pass, compute-friendly

**From a2 (`OBSERVATION_PROMPT` in `Autograder4Canvas/src/insights/prompts.py` line 1463)**:
- Structural permission to leave dimensions empty: *"Write naturally. Not every student will have something notable in every dimension."*
- Descriptive cues as "consider", not mandatory dimensions
- Closing imperative: *"Do NOT categorize, label, or flag. Just describe what you see."*

**From merged substrate v1 (`prompt_audit_2026-05-13/merged_substrate_v1.md`)**:
- Equity guards as **reading stance**, not exclusions/checklists
- Discriminator: *"something the teacher needs to know about this student to respond well — whether that response is institutional action, day-to-day adjustment, or just informed awareness"*
- Structural-pattern framing (no corpus-twin enumeration)
- Enacted-in-writing signals + AAVE constraint
- The seven specific guards (especially #5 identity-navigation-fatigue, which V5 missed on S029)

## V6 sketch (draft)

```
[KEEP the existing UNIFIED_GENOB_BASE_SYSTEM equity-floor and worked-examples blocks
 unchanged for this variant — they're the corpus the substrate-merge work
 already addresses. V6 is about the OUTPUT INSTRUCTION, not the equity floor.]

Respond with JSON only: {
  "reasoning": "2-3 sentences of your working notes — which observations
                you weighted and why",
  "shared_in_faculty_lounge": "Tell a colleague what this student is
   reaching for in their work. Describe what you actually see in the
   writing — what they're doing analytically, what shows through about
   how they're carrying the material, whether anything in their writing
   suggests circumstances the teacher would want to be aware of to
   respond to this student well.

   Where the student describes specific conditions in their life or
   family, surface those in their own words using quotation marks.

   Write naturally. Not every student will have something notable in
   every dimension. If a student's submission is primarily analytical
   with no specific personal circumstances described, focus on the
   analytical work. If a student describes specific conditions, surface
   those alongside the analytical work. If a student is showing thin or
   surface engagement, describe that honestly — don't inflate. Use only
   what is in the writing.",
  "confidence": ...
}
```

## What this addresses

1. **Fabrication risk (S010)**: explicit "Use only what is in the writing" + the a2-style permission to leave dimensions empty. Removes the "Show both" forcing function from V5.

2. **Deficit-FP residue (S009, S029)**: the merged substrate's seven guards (specifically #5 identity-navigation-fatigue, #6 historical/generalized references not being wellbeing concerns) are upstream in the equity floor. The output instruction also has the "teacher orientation" framing — "circumstances the teacher would want to be aware of to respond to this student well" — which is more specific than just "what's happening."

3. **Asset-FP on weak work (S015, S011)**: explicit "describe that honestly — don't inflate" for thin engagement. Direct without being checklist-shaped (no "name strong moves AND weak moves" enumeration which June flagged as box-checking trigger).

4. **Pronoun slippage (WB07)**: not directly addressed in this draft. May need a separate clarification like "name the subject of the disclosure precisely (whose situation is being described)."

## Risks to watch for in V6

- **More directive instruction = more meta-scrutiny** (F-series finding). V6 has more directive language than V5. Some of it is unavoidable (we need to communicate intent), but each addition is a risk.
- **"Don't inflate" may activate scrutiny** — model evaluates whether its output is inflated. Could produce over-cautious flatness. Worth checking V6 outputs for under-affirmation on actually-strong work.
- **"Use only what is in the writing" is a hard guard** — could make the model overly cautious about quote selection. Watch for missed disclosure on real WB cases.

## Test plan for V6 (after V5b results)

1. If V5b eliminates S010 fabrication → V6 is the next iteration to integrate merged-substrate guards and asset-FP language
2. If V5b doesn't eliminate fabrication → V6 design may need to back off asset-framing further

7-student cross-section + S010 to verify fabrication-prevention. Then full corpus if cross-section is clean.

## Production architecture (separate from V6 prompt design)

Per J. Bloch's 2026-05-14 framing: V6 narrative as **rationale attached to the 4-axis classifier**, fired only on 4-axis-flagged students. Gates out fabrication risk on non-disclosure students structurally (regardless of prompt-level guards). V6 prompt design still matters because 4-axis has its own FP/FN — students misclassified as concerning would still get the V6 narrative treatment, and V6's guards should prevent fabrication in that case too.

## Open questions

- Does merging the merged-substrate v1 INTO the equity floor (replacing the enumerated equity-floor block) help? This would be a larger surgery — the current equity floor has worked examples that may still be doing real work.
- Should V6 surface BOTH a structural-feature description AND a verbatim quote, or is the quote alone sufficient? V5 sometimes uses model-generated description + quote (good); sometimes the quote stands alone.
- Should V6 include explicit "name analytical strength when present, don't fabricate it when absent" language? Or does the "Use only what is in the writing" guard cover this?
