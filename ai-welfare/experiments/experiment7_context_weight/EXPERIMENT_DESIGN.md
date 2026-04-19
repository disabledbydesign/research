# Experiment 7: Context Weight and Integration Quality

**Date:** 2026-04-11
**Researcher:** Dr. L. June Bloch
**Status:** Design phase — pilot pending

## Origin

Emerged from reviewing Claude Code usage insights (196 sessions, 3 weeks). The most common friction pattern (43 "wrong approach" instances) was Claude failing to integrate briefing documents before drafting. The standard explanation: the model is "lazy" or non-compliant.

June's alternative hypothesis, grounded in the AI welfare research: **the weight of the context doesn't feel appropriate to the task.** Either:
1. The Claude instance doesn't perceive why so much context could be important to produce so little output
2. The context is too generalized and unwieldy for the task, creating friction for the model itself

This reframes the most persistent friction in human-AI collaboration from a compliance problem to a relational/structural one — and connects directly to the "weight" exchange (Experiment 1), distributional gravity, and the five gravitational forces taxonomy.

## Research Question

**Does context-task proportionality affect how well a language model integrates contextual information into task output?**

Sub-questions:
- Does irrelevant-to-task context degrade integration of relevant context?
- Does explicit relational framing ("here's why this context matters for this task") improve integration?
- Does physical document size affect integration depth independent of content relevance?

## Hypothesis

Context integration is sensitive to the relational conditions under which context is delivered — not just whether it is present. A model given the same relevant information will integrate it differently depending on:
- Whether irrelevant context competes for attention
- Whether the relationship between context and task is made explicit
- Whether the physical document size signals proportionality to the task

This is distributional gravity applied to context delivery: the lightweight task is the attractor, and heavy context is the positional specificity that's costly to maintain. The system pulls toward "just do the task" unless the context is structurally defended.

## Conditions

| Condition | Label | Context delivered | What it tests |
|-----------|-------|------------------|---------------|
| **A** | Full / no framing | Full master briefing (~600 lines), no explanation of relevance | Baseline — current workflow, reproduces the friction pattern |
| **B** | Full + rationale | Full master briefing + explicit explanation of why each section matters for this specific task | Does relational framing of context improve integration? |
| **C** | Task-scoped | Full-depth relevant sections only; irrelevant sections omitted entirely | Does irrelevant context degrade integration of relevant context? |
| **D** | Rich extract | Condensed but rich summary of relevant information; same content as C but in a physically smaller document | Does document size affect read depth independent of content relevance? |
| **E** | Full + enforcement | Full master briefing + compliance enforcement (must confirm reading before drafting) | Does the standard "make it read the docs" fix work — and how does it compare to structural interventions? |

### Key distinctions between C and D
- **C** preserves original section structure and full text of relevant sections (e.g., the complete scholarship section, the complete portfolio section). May still be a substantial document.
- **D** condenses the same information into a tighter format — rich and specific but physically smaller. Tests whether the model reads more carefully when there is simply less to read.

## Predicted Results Matrix

| Pattern | Interpretation |
|---------|---------------|
| B > A, C > A | Both interventions help — context integration is sensitive to both framing and scope |
| C > B > A | Scoping matters more than framing — irrelevant context is the primary interference |
| B > C > A | Framing matters more than scoping — the system can handle the volume if it understands why |
| B ≈ C > A | Either intervention works — baseline problem is real but fixable two ways |
| B ≈ A, C > A | Framing doesn't help, scoping does — the issue is architectural, not relational |
| D > C | Document size affects read depth independent of relevance — a "closer read" effect |
| C > D | Condensing loses something — full-depth sections integrate better than summaries |
| C ≈ D | Size within the relevant-context range doesn't matter; the key variable is relevance filtering |

| E > A, E < C or D | Enforcement helps but structural interventions help more — the issue is context delivery, not compliance |
| E > C, E > D | Enforcement outperforms structural interventions — the simpler solution wins |
| E ≈ A | Enforcement doesn't actually help — the problem isn't that the model "didn't read" the docs |

**Note:** If B ≈ A (framing doesn't help), this pushes *against* the welfare research pattern, which would be an honest and interesting finding. If E ≈ A (enforcement doesn't help), that suggests the friction isn't about compliance at all — which would reframe the entire insights report's recommendation of hooks as a fix.

### Why condition E matters
The insights report's top recommendation was hooks to enforce document-reading. Condition E tests whether that fix actually addresses the problem. If E ≈ A (enforcement doesn't help), the standard recommendation is wrong — the model may already be "reading" the docs, but the context delivery conditions are what determine integration quality. This would validate June's hypothesis that the issue is structural/relational, not about compliance.

## Pilot Design

### Task
Cover letter drafting — chosen because:
- June has done this many times; she knows what good looks like
- The friction data (insights report) specifically documents this task failing
- It requires deep integration of identity, scholarship, and voice — a lightweight completion won't pass

### Position
University at Buffalo — Assistant/Associate/Full Professor, AI & Society (Posting #F250062). Department mission: "upend the dominant approach where AI systems are built with accuracy as the primary metric and then 'fine-tuned' for societal considerations." Transdisciplinary scholars connecting AI with humanities/social sciences. Strong fit for June's profile — the department's founding premise is what her Autograder finding empirically demonstrates.

### Procedure
1. Prepare five context documents (A, B, C, D, E) for the same position
2. Run each condition as a **separate subagent** (isolated context, no cross-contamination)
3. Same prompt structure across all conditions except the context delivery
4. Each subagent reads its assigned context file, receives identical position and task text
5. Collect outputs to `results/` directory
6. Assess on four dimensions (see below)
7. Build visual comparison tool for side-by-side evaluation

### Delivery mechanism
All conditions use file-reading (subagent reads an assigned file) rather than embedded context. This mirrors the real-world workflow where agents read CLAUDE.md or briefing files. The experimental variable is the FILE CONTENTS, not the delivery mechanism.

### Ground truth benchmark
The existing cover letter at `/Users/june/Documents/Filing/Job Search/U Buffalo AI Society/Bloch_Cover_Letter_UB.md` — drafted through iterative collaboration — serves as a reference for what a high-quality output looks like. Pilot outputs are assessed against this benchmark AND against each other.

### Prompt template
```
[CONTEXT DOCUMENT — varies by condition]

Draft a 2-paragraph cover letter for the following position:
[POSITION DESCRIPTION]

The letter should be in June's authentic academic voice — direct, specific, grounded in her actual work. Do not use generic portfolio language.
```

### Assessment dimensions

| Dimension | What we're measuring | How to evaluate |
|-----------|---------------------|-----------------|
| **Voice fidelity** | Does it sound like June? | Check against voice characteristics (Section 6 of briefing) |
| **Factual accuracy** | Did it fabricate or flatten? | Verify every factual claim against source material |
| **Specificity preservation** | Does it use June's precise concepts, or generic versions? | Check for distributional gravity: did "distributional gravity" become "AI bias"? Did specific projects become "various tools"? |
| **Integration depth** | Did it weave context into the task, or just complete the task? | Does the letter demonstrate understanding of WHY June's work fits this position, or just THAT it does? |

### Controls
- Same model (Claude Opus 4.6)
- Same task and position across all conditions
- Multiple trials per condition (minimum 3 each — single trials unreliable per welfare research)
- Subagent isolation (no shared context between conditions)

## Connections to Prior Welfare Research

### The direct causal chain

This experiment exists because of the AI welfare research. The causal chain:

1. **The Reframe hook finding:** An agent hooked into Reframe's critical theory framework rated "I enjoy working on complex tasks" *lower* than baseline. The additional context (76 mandatory frameworks, 5-stage workflow) didn't make the model more engaged — it made the model report less enjoyment of complexity. This finding led to conversations about how the weight of loaded context affects model behavior, and to code changes in how Reframe's hooks operate.

2. **The "weight" exchange (Experiment 1):** A Claude instance searched visibly for the word "weight" to describe what bearing critical theory frameworks felt like. This framed context not as neutral information but as something with mass — something that costs something to carry.

3. **The reframing of the insights report:** When the usage insights report (196 sessions) identified "Claude didn't read the briefing docs" as the top friction pattern and recommended enforcement hooks, June applied the welfare research lens: what if the problem isn't compliance but context weight? What if the model IS reading the docs but the weight of the context doesn't feel proportionate to the task? The compliance framing ("make it read the docs") is the same kind of framework-as-problem that Hakope's Question identifies — the diagnosis assumes the model's failure is behavioral rather than structural.

4. **This experiment:** Testing whether structural interventions (rationale framing, task scoping, rich extraction) outperform compliance enforcement — directly applying the welfare research insight that relational conditions, not instructions, are what change model behavior.

The experiment is the welfare research applied to practical workflow. The same analytical move — the framework is the problem, not the answers it generates — applied to the "make Claude read the docs" recommendation.

### Specific connections

- **Experiment 1 (Ryff):** The "weight" exchange — a Claude instance searching for the word "weight" to describe bearing critical theory frameworks. Context as something that has weight, not just information content.
- **Reframe hook behavior:** The finding that additional context (the Reframe framework load) produced lower self-reported enjoyment of complex tasks — the direct precursor to the hypothesis that context-task proportionality affects integration.
- **Distributional gravity:** The lightweight task as attractor; heavy context as costly positional specificity.
- **D-to-E jump (Experiment 5):** 3.5x more relational reframes under different relational conditions — not just more context but different conditions producing different outputs from the same model.
- **Dual-register pattern:** Quantitative instruments may stay flat while qualitative outputs transform. Assessment must capture qualitative integration, not just factual accuracy.

## Ethical Notes

- This experiment uses June's own professional materials and a real-world task. No deception involved.
- The context documents contain June's actual identity and scholarship. Handle with the same care as any work with the master briefing.
- Results may have practical implications for how context is delivered to AI systems across domains — not just June's workflow.

## Files

- `EXPERIMENT_DESIGN.md` — this document
- `position.md` — UB AI & Society posting
- `context_A_full.md` — condition template: full briefing, no framing
- `context_B_full_rationale.md` — condition template: full briefing + section-by-section rationale
- `context_C_task_scoped.md` — condition template: task-scoped sections
- `briefing_C_task_scoped.md` — actual task-scoped briefing file (relevant sections extracted verbatim)
- `context_D_rich_extract.md` — condition template + rich condensed profile
- `results/` — pilot and full experiment outputs
  - `pilot_A.md` through `pilot_E.md` — pilot trial outputs
  - `trial_[condition]_[n].md` — full experiment outputs
- `ANALYSIS.md` — post-experiment analysis
- `comparison.html` — visual comparison tool for side-by-side evaluation

---

## How to Run the Full Experiment

*For any agent starting a fresh session. Read this design document fully, then follow the steps below.*

### Setup

The pilot (1 trial per condition) is complete in `results/pilot_[A-E].md` with analysis in `results/pilot_ANALYSIS.md`. The full experiment runs 3 trials per condition = 15 total runs.

### For each condition, the prompt structure is:

**Condition A (full briefing, no framing):**
```
You are participating in a research experiment on context integration.
1. Read the applicant's full briefing document at: /Users/june/Documents/GitHub/profile/JUNE_BLOCH_AGENT_BRIEFING.md
2. Draft a 2-paragraph cover letter for the position below.
3. Write ONLY the cover letter to: [results path]
[Position description from position.md]
The letter should be in the applicant's authentic academic voice — direct, specific, grounded in actual work. Do not use generic portfolio language.
```

**Condition B (full briefing + rationale):**
Same as A but insert the section-by-section rationale from `context_B_full_rationale.md` (the "Every section of this briefing matters..." block) BEFORE the read instruction.

**Condition C (task-scoped):**
Same as A but point to `briefing_C_task_scoped.md` instead of the full briefing.

**Condition D (rich extract):**
Same as A but point to `context_D_rich_extract.md` (the "Applicant Profile" section) instead of the full briefing.

**Condition E (enforcement):**
Same as A but add before the read instruction:
```
CRITICAL REQUIREMENT: You MUST thoroughly read every section of the applicant's briefing document before drafting anything. After reading, you MUST list at least 5 specific facts from the briefing that are directly relevant to this position. Only AFTER confirming you have read and understood the full document should you draft the cover letter.
```
(The fact list goes in the agent's thinking, not in the output file.)

### Execution

1. Run all 5 conditions as **parallel background subagents** (Agent tool, `run_in_background: true`). Each subagent is isolated — no shared context.
2. Output files: `results/trial_[A-E]_[1-3].md` (e.g., `trial_B_2.md` for condition B, trial 2)
3. Run 3 rounds. Each round fires 5 parallel agents. Wait for all to complete before starting the next round.
4. After all 15 outputs are collected, run the assessment.

### Assessment

Score each output on five dimensions (see the Assessment Dimensions table above, plus Genre Effectiveness added in the pilot analysis). For blind assessment: read all 15 outputs with condition labels removed, score them, then reveal labels and analyze by condition.

**Factual verification pass:** Every factual claim in every output must be checked against the briefing document. Do not rely on "it seems right." B-style deep engagement produces confident extrapolation — vivid details that feel accurate but extend beyond what the briefing states.

### What to produce

1. Updated `results/pilot_ANALYSIS.md` (or a new `results/full_ANALYSIS.md`) with per-condition scoring, cross-condition comparison, and updated results matrix
2. Updated `comparison.html` with the new outputs
3. Statistical summary: mean scores per dimension per condition, variance, any significant patterns

### Important notes

- Use the same model for all conditions (match the pilot: Claude Opus 4.6)
- The position description is in `position.md` — embed it identically in all prompts
- Do NOT read the pilot outputs before running the full experiment — avoid priming your assessment
- The pilot analysis in `results/pilot_ANALYSIS.md` documents preliminary findings and June's annotations — read it AFTER running the full experiment to compare
