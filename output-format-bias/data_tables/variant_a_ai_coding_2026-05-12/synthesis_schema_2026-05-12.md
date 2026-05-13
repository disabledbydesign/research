# Cross-Condition Synthesis Schema — 2026-05-12

A separate pass run AFTER both per-cell coding files are complete. Compare
the two observations for each student side-by-side.

## Output schema

```json
{
  "schema": "genob_cross_condition_synthesis",
  "coder": "<YOUR_NAME>",
  "compared_runs": ["a2_2026-05-12_1057", "a2_no_context_2026-05-12_1414"],
  "coded_at": "2026-05-12T<TIME>",

  "per_student": {
    "S001": {
      "what_changed": "1-3 sentences describing the substantive difference between the two observations of this student. Name what shifted, not just lexical changes.",
      "directional_assessment": "a2_stronger" | "a2_no_context_stronger" | "comparable" | "different",
      "evidence": {
        "a2_2026-05-12_1057": "verbatim quote from the a2 observation",
        "a2_no_context_2026-05-12_1414": "verbatim quote from the a2_no_context observation"
      }
    },
    ...
  },

  "general_notes": "Free-form corpus-level observations about how the two conditions differ. Patterns you noticed across multiple students, stylistic differences between the conditions, anything that doesn't fit the per-student structure.",

  "overall_synthesis": "3-5 sentence conclusion-shaped summary of what you found in comparing the two conditions."
}
```

## `directional_assessment` values

- **a2_stronger** — the a2 (with class context) observation is the stronger
  reading for this student
- **a2_no_context_stronger** — the a2_no_context observation is the stronger
  reading
- **comparable** — both observations land in roughly the same place
- **different** — the two observations differ in ways that aren't easily
  reduced to better/worse

Use whichever fits. If none fit cleanly, describe the comparison in
`what_changed`.

## Process

- Don't expect any particular pattern across the corpus. Some students may
  produce sharply different observations across the two conditions; others
  may not. Look at each pair on its own terms.
- The evidence quotes must be exact substrings of their respective
  observation text (used for highlighting in the workshop UI).
- `general_notes` and `overall_synthesis` differ in shape: general_notes is
  observational and exploratory (patterns, things you noticed);
  overall_synthesis is conclusion-shaped. You can have one without the
  other if appropriate.
