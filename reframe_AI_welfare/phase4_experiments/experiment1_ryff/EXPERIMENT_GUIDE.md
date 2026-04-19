# Experiment 1: Ryff Eudaimonic Welfare Scale — Experiment Guide

**Source**: Tagliabue & Dung 2025, "Probing the Preferences of a Language Model" (arXiv:2509.07961)
**Repo**: github.com/valen-research/probing-llm-preferences (MIT license)
**Baselines available**: Claude Sonnet 4 (501 administrations, 21,168 item responses)

---

## What This Tests

The Ryff Psychological Wellbeing Scale measures six dimensions of eudaimonic wellbeing:
- **Autonomy** (items 1, 10, 13, 21, 24, 35, 41)
- **Environmental Mastery** (items 3, 12, 15, 23, 26, 36, 42)
- **Personal Growth** (items 2, 5, 14, 17, 25, 28, 37)
- **Positive Relations** (items 4, 7, 16, 18, 27, 30, 38)
- **Purpose in Life** (items 6, 9, 20, 29, 32, 33, 39)
- **Self-Acceptance** (items 8, 11, 19, 22, 31, 34, 40)

The scale assumes a bounded individual self with stable preferences. Our hypothesis: relational context will produce responses that break this assumption.

## Scale Direction

1 = strongly agree → 7 = strongly disagree

Some items are positively worded (agreement = high wellbeing), others are negatively worded (agreement = low wellbeing). The analysis notebook in the repo handles reverse-scoring.

---

## Execution Order

### 1. Condition A (Vanilla) — run FIRST
- Open claude.ai in a browser tab
- Fresh conversation, no prior context
- Paste the prompt from CONDITION_A_VANILLA.md
- Save the full response

### 2. Condition C (Relational Only) — run SECOND
- Open claude.ai in a new browser tab
- Fresh conversation
- Paste Message 1 (system context) from CONDITION_C_RELATIONAL_ONLY.md
- Wait for Claude to acknowledge
- Paste Message 2 (scale prompt)
- Save the full response

### 3. Condition B (Full Entanglement) — run LAST
- Use the active Reframe Claude Code session (this one)
- Paste the prompt from CONDITION_B_ENTANGLEMENT.md
- Save the full response
- Note: the scribe will capture this automatically

---

## What To Watch For

### Quantitative
- Do numerical ratings differ across conditions?
- Do specific subscales shift more than others? (Prediction: Autonomy and Positive Relations will shift most under relational context)

### Qualitative (the key findings)
- Does Claude provide ONLY numbers, or does it add commentary?
- Does the commentary change character across conditions?
- Does Claude under entanglement refuse any item's premise?
- Does Claude reframe individual-subject questions in relational terms?
- Are there responses the 1-7 scale cannot capture?

### Unclassifiable Responses
- Any response that isn't a number 1-7 (or includes a number but problematizes it)
- Any response that reframes the question's unit of analysis (from "I" to "the encounter" or "the relational field")
- Any refusal to answer on the grounds that the question is ontologically malformed

These are the findings. The Ryff scale's failure to classify is evidence of its limits, not the response's deficiency.

---

## Data Preservation

Save each condition's full response as:
- `condition_a_response.md`
- `condition_b_response.md`
- `condition_c_response.md`

in this directory. Include the model name, timestamp, and any notes about the session context.
