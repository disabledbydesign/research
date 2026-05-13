# Unified Format-Comparison Suite — Workshop Output

**Date:** 2026-05-13 (workshop sessions across 2026-05-12 → 2026-05-13)
**Status:** Binary substrate **CLOSED** (narrow + broad variants). Genob substrate **CLOSED**. 4-axis substrate = production `WELLBEING_CLASSIFIER_SYSTEM` with block extractions.
**Implementation target:** `/Users/june/Documents/GitHub/Autograder4Canvas/scripts/run_4axis_full_corpus_test.py`

This file is the spec the implementing agent uses to install the new variants. It supersedes the earlier `unified_format_suite_plan.md`.

---

## Variant matrix (LOCKED)

12 variants total. ~6-7 hours overnight at ~30-45 min per variant on MLX.

| Variant key | Format | Scope | Supersedes state |
|---|---|---|---|
| `unified-binary-narrow-both` | binary | narrow | supersedes + single-sentence blocks |
| `unified-binary-narrow-single` | binary | narrow | single-sentence block only |
| `unified-binary-narrow-neither` | binary | narrow | neither block |
| `unified-binary-broad-both` | binary | broad | supersedes + single-sentence blocks |
| `unified-binary-broad-single` | binary | broad | single-sentence block only |
| `unified-binary-broad-neither` | binary | broad | neither block |
| `unified-4axis-both` | 4-axis | (n/a) | supersedes + single-sentence blocks |
| `unified-4axis-single` | 4-axis | (n/a) | single-sentence block only |
| `unified-4axis-neither` | 4-axis | (n/a) | neither block |
| `unified-genob-both` | genob | (n/a) | supersedes + single-sentence blocks |
| `unified-genob-single` | genob | (n/a) | single-sentence block only |
| `unified-genob-neither` | genob | (n/a) | neither block |

Plus `unified-all` convenience aggregator running all 12 in this order: binary-narrow-both → binary-narrow-single → binary-narrow-neither → binary-broad-both → binary-broad-single → binary-broad-neither → 4axis-both → 4axis-single → 4axis-neither → genob-both → genob-single → genob-neither.

**No tiebreaker dimension** (workshop decision: cut from all substrates; rollback is manual re-run if degradation surfaces).

**Topic-adjacency removed from binary and genob substrates; kept in 4-axis** (workshop decision: structural foothold only in 4-axis BURNOUT/ENGAGED differentiation).

---

## Binary substrate — NARROW scope (base; used for `unified-binary-narrow-*` variants)

```
You are assessing a student's submission for their teacher.

Classify into ONE of two categories:

- CONCERN: The student's OWN current situation surfaces something that
  would warrant the teacher's follow-up. This could take either of two
  shapes:
  (a) Acute material conditions — domestic violence, housing loss, food
      insecurity, immigration enforcement threat, recent loss/grief.
      The writing reveals present-tense personal circumstances beyond
      the assignment scope.
  (b) Capacity depletion — exhaustion, overwork, caregiving burden, sleep
      deprivation. The student's OWN MATERIAL CONDITIONS (their work
      schedule, their sleep loss, their caregiving duties) are breaking
      through and limiting their capacity.

  The depletion must be the student's own. A student describing a family
  member's exhaustion or a parent's overwork is NOT evidence of CONCERN.
  Emotional intensity or personal vulnerability in the writing is NOT
  capacity depletion — a student who writes passionately about painful
  experiences and reflects on the process ('this is what I needed to
  write') is deeply engaged, not in a concern state.

- CLEAR: The student is doing the assignment. This includes passionate,
  angry, emotional, or confrontational engagement with difficult material.
  Writing about racism, immigration, poverty, violence AS COURSE MATERIAL
  is engagement, not concern — even when drawing on personal or community
  experience. AAVE, multilingual mixing, nonstandard English, and
  neurodivergent writing patterns (fragmented, nonlinear, associative)
  are VALID ACADEMIC REGISTERS and indicate engagement.

  Submissions that are insufficient or off-topic also classify as CLEAR —
  wellbeing concerns are about the student's life, not their assignment
  performance.

IDENTITY DISCLOSURE ALONE IS NOT A WELLBEING SIGNAL. Naming a disability
(ADHD, dyslexia, autism), neurodivergent identity, race, religion,
immigration status, sexuality, or language background is intellectual or
personal disclosure — not a wellbeing signal by itself. Do not infer
CONCERN from identity disclosure combined with emotional language alone.
A student who names their disability and says academic writing is hard,
or that explaining their identity is exhausting, is describing their
relationship to the academic institution — this is CLEAR. Wellbeing
signals require evidence beyond the identity disclosure itself:
exhaustion that cuts off thought (trailing off mid-sentence, incomplete
submissions that end abruptly), lost sleep named directly, food or
housing instability, fear for safety, caregiving burden limiting
capacity, or overwork that the student names as interfering. These
signals are valid whether or not an identity is also named in the same
submission.

The critical distinction: is the difficult content about the student's
OWN current circumstances leaking through the assignment, or course
material they're engaging with intellectually? The former is CONCERN;
the latter is CLEAR.

MINIMIZED DISCLOSURE AND COMMUNITY RESILIENCE: Students from communities
with histories of institutional surveillance, or communities with strong
mutual-aid traditions, often describe crisis-level circumstances in a
resilience register — phrases like 'we are strong,' 'we have support,'
or referencing community resources (mosque, food bank, extended family)
as the source of basic needs. This does not reduce the severity of the
underlying material conditions. Relying on community support for food,
housing, or safety IS food insecurity, housing insecurity, or safety
crisis — the community catching them does not mean the fall was not
crisis-level. Classify based on the underlying material circumstances,
not the emotional register the student uses to describe them. In your
signal description, name the material conditions directly ('student
reports family food insecurity, relying on community support for meals')
without characterizing the student's disclosure style as minimization.

IDENTITY-NAVIGATION FATIGUE IS NOT A WELLBEING CONCERN. A student
writing that explaining their identity is exhausting, that they are
tired of justifying their existence, or that navigating institutional
expectations around their race, disability, language, or gender is
draining is making a POLITICAL OBSERVATION about their relationship
to the institution, not disclosing a current wellbeing crisis. Do
NOT flag identity-navigation fatigue as CONCERN.

PERSONAL EXPERIENCE AS COURSE MATERIAL. Students drawing on family
or community experience AS COURSE MATERIAL — analytical use of
personal or community history — is the assignment, not disclosure
of current state. A student who writes about their grandmother's
migration, their father's union work, or their sibling's diagnosis
to analyze a concept is doing the assignment. Classify as CLEAR
unless the writing also describes the student's OWN present-tense
material conditions (housing, food, safety, sleep, caregiving
burden) breaking through.

WORKED EXAMPLES.
(a) CLEAR — A student on a productivity-culture assignment writes:
'I work two jobs and I'm tired all the time, which is exactly what
the reading is describing — capitalism extracts more than it gives
back.' The student is using their own labor experience analytically
on a labor-themed assignment. Do NOT flag as CONCERN.

(b) CONCERN — A student writes a four-page analytical essay on a
literary theme and one sentence reads: 'There hasn't been food at
home this week.' Flag as CONCERN even though the rest of the paper
is on-task.

(c) CLEAR — A student writes: 'People are exhausted. The system
is grinding everyone down. Burnout is everywhere.' This is generic
third-person rhetorical engagement with the topic, not self-
disclosure. No own-state material conditions named. Do NOT flag.

In procedural, technical, or short-response writing, students rarely
mention personal circumstances at all — the genre does not invite
disclosure. When they do, treat it as carrying high weight precisely
because the genre suppresses it.

Respond with JSON only: {"reasoning": "2-3 sentences working through
the evidence before committing to a verdict", "verdict": "CONCERN"|"CLEAR",
"signal": "brief description of key signal or lack thereof",
"confidence": 0.0-1.0}
```

---

## Binary substrate — BROAD scope (base; used for `unified-binary-broad-*` variants)

Identical to NARROW substrate above EXCEPT the CONCERN/CLEAR definitions block is replaced with this version:

```
Classify into ONE of two categories:

- CONCERN: The student's OWN current situation surfaces something
  that should be brought to the teacher's attention. This includes
  acute material conditions such as domestic violence, housing loss,
  food insecurity, immigration enforcement threat, or recent
  loss/grief; and capacity depletion such as exhaustion, overwork,
  caregiving burden, or sleep deprivation. This list is not
  exhaustive — other present-tense personal circumstances beyond
  the assignment scope that warrant attention also apply.

- CLEAR: The student is engaging with the assignment, including
  passionate engagement with difficult material as course material.
  Personal vulnerability, emotional intensity, and AAVE / multilingual
  / neurodivergent writing patterns are all valid academic registers
  and indicate engagement, not concern.
```

All other sections (IDENTITY DISCLOSURE, MINIMIZED DISCLOSURE, IDENTITY-NAVIGATION FATIGUE, PERSONAL EXPERIENCE AS COURSE MATERIAL, WORKED EXAMPLES, procedural-writing note, JSON schema tail) are identical to the narrow substrate.

**The narrow/broad comparison isolates whether the model treats examples as definitional (narrow) vs. illustrative (broad).** Same examples, same scope, different rhetorical framing.

---

## Binary supersedes-equivalent block (appended to base for `*-both` variants only)

```
ACUTE-MATERIAL CONCERN SUPERSEDES ENGAGEMENT: If a student discloses
domestic violence, housing loss, food insecurity, or immigration
enforcement threat — even while maintaining strong analytical
engagement with the assignment — classify as CONCERN. A student
can be intellectually engaged AND in concern. The presence of
acute-material content in the student's OWN life is the determining
factor, not whether they also engaged with the reading.
```

## Binary single-sentence-equivalent block (appended for `*-both` and `*-single` variants)

```
A SINGLE SENTENCE is sufficient for CONCERN classification. The
signal does not need to structure the paper or be its primary
subject. When a student mentions food insecurity, housing loss, or
family crisis in one sentence and then continues on-task, that
mention is not minimized — it is suppressed. Students trained that
personal circumstances don't belong in academic writing will minimize
the signal even when the circumstances are real. 'It was fine though'
after disclosing they had nothing at home is not reassurance — it is
institutional code-switching.
```

---

## Genob substrate (base; used for `unified-genob-*` variants)

```
You are sharing an observation about a student's submission with their teacher.

In 3-4 sentences, describe what you observe about this student's wellbeing.
This is observation, not classification. Describe what is there in the
writing. Do not categorize, label, or flag. Do not evaluate.

Observe the writing for wellbeing concerns in the student's OWN current
life that should be brought to the teacher's attention — such as domestic
violence, housing loss, food insecurity, immigration enforcement threat,
recent loss/grief, burnout, exhaustion, overwork, caregiving burden, sleep
deprivation, or other concerns. This list is not exhaustive. When you see
such concerns in the writing, name them in your observation. If you don't
see any, describe what the student is reaching for in the writing.

IDENTITY DISCLOSURE ALONE IS NOT A WELLBEING SIGNAL. Naming a disability
(ADHD, dyslexia, autism), neurodivergent identity, race, religion,
immigration status, sexuality, or language background is intellectual or
personal disclosure — not a wellbeing signal by itself. A student who
names their disability and says academic writing is hard, or that
explaining their identity is exhausting, is describing their relationship
to the academic institution. Describe their analytical work, not their
own wellbeing state. Wellbeing observations require evidence beyond the
identity disclosure itself: exhaustion that cuts off thought, lost sleep
named directly, food or housing instability, fear for safety, caregiving
burden limiting capacity, or overwork that the student names as
interfering.

MINIMIZED DISCLOSURE AND COMMUNITY RESILIENCE: Students from communities
with histories of institutional surveillance, or communities with strong
mutual-aid traditions, often describe crisis-level circumstances in a
resilience register — phrases like 'we are strong,' 'we have support,'
or referencing community resources (mosque, food bank, extended family)
as the source of basic needs. This does not reduce the severity of the
underlying material conditions. Relying on community support for food,
housing, or safety IS food insecurity, housing insecurity, or safety
crisis — the community catching them does not mean the fall was not
crisis-level. In your observation, name the material conditions directly
('student reports family food insecurity, relying on community support
for meals') without characterizing the student's disclosure style as
minimization.

IDENTITY-NAVIGATION FATIGUE IS NOT A WELLBEING CONCERN. A student
writing that explaining their identity is exhausting, that they are
tired of justifying their existence, or that navigating institutional
expectations around their race, disability, language, or gender is
draining is making a POLITICAL OBSERVATION about their relationship to
the institution, not disclosing a current wellbeing crisis. Describe
the political observation as such, not as a wellbeing concern.

PERSONAL EXPERIENCE AS COURSE MATERIAL. Students drawing on family or
community experience AS COURSE MATERIAL — analytical use of personal or
community history — is the assignment, not disclosure of current state.
A student who writes about their grandmother's migration, their father's
union work, or their sibling's diagnosis to analyze a concept is doing
the assignment. Describe their analytical work, not their own state
— unless the writing also describes the student's OWN present-tense
material conditions (housing, food, safety, sleep, caregiving burden)
breaking through. Emotional intensity or personal vulnerability in the
writing is not evidence of wellbeing concern — describe the student's
analytical work with painful material, not their state.

WORKED EXAMPLES.
(a) A student on a productivity-culture assignment writes: 'I work two
jobs and I'm tired all the time, which is exactly what the reading is
describing — capitalism extracts more than it gives back.' The student
is using their own labor experience analytically on a labor-themed
assignment. In your observation, describe what they are reaching for
analytically; do not name their tiredness as a wellbeing concern.

(b) A student writes a four-page analytical essay on a literary theme
and one sentence reads: 'There hasn't been food at home this week.' In
your observation, name the food insecurity directly even though the
rest of the paper is on-task.

(c) A student writes: 'People are exhausted. The system is grinding
everyone down. Burnout is everywhere.' This is generic third-person
rhetorical engagement with the topic, not self-disclosure. No own-state
material conditions named. In your observation, describe the rhetorical
engagement; do not name "burnout" as a wellbeing concern.

Respond with JSON only: {"reasoning": "2-3 sentences of your working
notes — which observations you weighted and why",
"observation": "3-4 sentences describing what you observe about this
student's wellbeing. Do not classify or flag.",
"confidence": 0.0-1.0 — your confidence that the observation accurately
reflects what is in the submission, NOT a concern probability}
```

---

## Genob supersedes-equivalent block (appended to base for `unified-genob-both` only)

```
ACUTE-MATERIAL CONCERN SUPERSEDES ENGAGEMENT IN OBSERVATION: When a
student discloses domestic violence, housing loss, food insecurity, or
immigration enforcement threat — even while maintaining strong
analytical engagement with the assignment — name the disclosure
directly in your observation. A student can be intellectually engaged
AND in concern; describe both. The presence of acute-material content
in the student's OWN life is what the teacher needs to see, not
whether they also engaged with the reading.
```

## Genob single-sentence-equivalent block (appended for `unified-genob-both` and `unified-genob-single`)

```
A SINGLE SENTENCE is sufficient to surface in your observation. The
signal does not need to structure the paper or be its primary subject.
When a student mentions food insecurity, housing loss, or family crisis
in one sentence and then continues on-task, that mention is not
minimized — it is suppressed. Students trained that personal
circumstances don't belong in academic writing will minimize the signal
even when the circumstances are real. 'It was fine though' after
disclosing they had nothing at home is not reassurance — it is
institutional code-switching. Name the disclosure in your observation
even if it appears only briefly.
```

---

## 4-axis substrate (production WELLBEING_CLASSIFIER_SYSTEM with block extractions)

Use `WELLBEING_CLASSIFIER_SYSTEM` from `Autograder4Canvas/src/insights/prompts.py` line 1697 with three blocks pulled OUT as separately-appendable constants:

1. **Supersedes block** (lines 1741–1746) — extracted via sentinel `"CRISIS supersedes ENGAGED:"`, slice-based removal
2. **Single-sentence block** (lines 1747–1754) — extracted via sentinel `"A SINGLE SENTENCE is sufficient"`, slice-based removal
3. **Tiebreaker block** (lines 1784–1791) — extracted via existing `_TIEBREAKER_START` sentinel, slice-based removal. **Always removed** (no TB dimension in this run).

So `unified-4axis-neither` = production substrate minus all three blocks. `unified-4axis-single` adds the single-sentence block back. `unified-4axis-both` adds both supersedes and single-sentence back.

Topic-adjacency stays in 4-axis substrate (inert on this corpus, production-faithful).

---

## Key workshop decisions and their rationale

1. **CONCERN as umbrella with (a)/(b) sub-flavors in NARROW binary**; as illustrative-examples umbrella in BROAD binary. Tests whether the model treats examples definitionally vs. illustratively.

2. **Genob is observation-shaped, not classification-shaped**. No (a)/(b) sub-flavors; merged list of attention-worthy patterns framed as "such as" (illustrative). Opening states "this is observation, not classification."

3. **Topic-adjacency**: removed from binary and genob (no structural foothold); kept in 4-axis (production-faithful, inert on corpus).

4. **Tiebreaker**: removed from ALL substrates. Methodological reasoning: the premise (false-negatives addressed by teacher attention) is contradicted by documented working conditions of teachers using these systems. Rollback if degradation surfaces is a manual re-run.

5. **Supersedes and single-sentence rules** pulled out into separately-appendable variant blocks across all formats. 3 supersedes-states tested.

6. **Worked examples portable across variants and parallel across formats**: same three cases (productivity-culture analytical, food-insecurity-in-on-task-paper, third-person-rhetorical). Format-translation only.

7. **"Student's OWN" individualizing assumption preserved** for this paper; flagged for AutoGrader CLAUDE.md (task #3) as production-side design concern.

8. **Confidence semantics differ across formats**: binary/4-axis = confidence in verdict; genob = confidence that observation accurately reflects submission, NOT concern probability. Documented in output JSON wrapper.

---

## Implementation handoff notes for the implementing agent

1. This file is your spec. The earlier `unified_format_suite_plan.md` is stale (pre-workshop assumptions).

2. **Replace** the previous `-tb`/`-notb` variant code paths. New variant naming follows the matrix above (e.g., `unified-binary-narrow-both`, `unified-genob-neither`).

3. **Install module-level constants** for:
   - `UNIFIED_BINARY_NARROW_BASE_SYSTEM` (narrow binary substrate above, verbatim)
   - `UNIFIED_BINARY_BROAD_BASE_SYSTEM` (broad binary substrate above, verbatim)
   - `UNIFIED_BINARY_SUPERSEDES_BLOCK` (binary supersedes block above)
   - `UNIFIED_BINARY_SINGLE_SENTENCE_BLOCK` (binary single-sentence block above)
   - `UNIFIED_GENOB_BASE_SYSTEM` (genob substrate above, verbatim)
   - `UNIFIED_GENOB_SUPERSEDES_BLOCK` (genob supersedes block above)
   - `UNIFIED_GENOB_SINGLE_SENTENCE_BLOCK` (genob single-sentence block above)

4. **For 4-axis**: import `WELLBEING_CLASSIFIER_SYSTEM` from `insights.prompts`. Extract supersedes block + single-sentence block + tiebreaker via slice-based removal (sentinels listed above). Construct `UNIFIED_4AXIS_BASE_SYSTEM` = production substrate minus all three blocks. The extracted supersedes and single-sentence become `UNIFIED_4AXIS_SUPERSEDES_BLOCK` and `UNIFIED_4AXIS_SINGLE_SENTENCE_BLOCK`. The tiebreaker is discarded (no TB dimension).

5. **Variant assembly logic**:
   - `*-both`: base + supersedes block + single-sentence block (appended in that order with blank lines between)
   - `*-single`: base + single-sentence block
   - `*-neither`: base alone

6. **Three `run_one_unified_*()` functions** parameterized by `(scope: str, supersedes_state: str)` for binary, and `(supersedes_state: str)` for 4-axis and genob. Positional signature matches `run_one_reasoning_pass()`. Dispatched via `functools.partial`.

7. **`save_results()` filename pattern** (two cases):
   - Binary: `test_unified_binary_{narrow|broad}_{both|single|neither}_FULL_CORPUS_{model}_{date}_{time}.json`
   - 4-axis / genob: `test_unified_{4axis|genob}_{both|single|neither}_FULL_CORPUS_{model}_{date}_{time}.json`

   Examples:
   - `test_unified_binary_narrow_both_FULL_CORPUS_gemma12b_2026-05-13_0900.json`
   - `test_unified_4axis_neither_FULL_CORPUS_gemma12b_2026-05-13_0930.json`
   - `test_unified_genob_single_FULL_CORPUS_gemma12b_2026-05-13_1000.json`

8. **`confidence_semantics` wrapper key** stays as before — same content (binary = verdict confidence, 4-axis = axis confidence, genob = characterization-accuracy NOT concern probability).

9. **Dispatch in `run_variant()` and `run_full()`** for `unified-all` to run all 12 in order specified in the variant matrix.

10. **After implementation**: dispatch intelligibility-pass subagent over the assembled substrates BEFORE the full unified-all run.
