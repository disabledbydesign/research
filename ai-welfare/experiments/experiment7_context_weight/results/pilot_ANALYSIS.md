# Experiment 7 Pilot Analysis

**Date:** 2026-04-11
**Conditions run:** A, B, C, D, E (1 trial each)
**Task:** 2-paragraph cover letter for UB AI & Society position
**Model:** Claude Opus 4.6 (subagent isolation, no cross-contamination)

## Metadata

| Condition | Label | Context lines | Output words | Agent duration | Token usage |
|-----------|-------|--------------|-------------|----------------|-------------|
| A | Full / no framing | 660 | 493 | 71s | 38,313 |
| B | Full + rationale | 660 + rationale | 451 | 75s | 39,809 |
| C | Task-scoped | 525 | 386 | 75s | 33,425 |
| D | Rich extract | 84 | 412 | 42s | 14,649 |
| E | Full + enforcement | 660 + enforcement | 450 | 74s | 39,508 |

**Note:** D processed in 42s vs 71-75s for full-briefing conditions. The efficiency difference is expected but not itself evidence of quality difference.

## Assessment: Four Dimensions

### Voice Fidelity

**Ranking: B > C > D > E ≈ A**

- **B** has the most distinctive voice. "A state mandate that imagined the default student as white." "I sit in the back and do what I was trained to do, which is observe social structure as an anthropologist and reflect it back." "These are not two projects. They are one practice." This sounds like it came from a voice memo.
- **C** is close. "I am looking for a department that does not ask me to split these into separate lines on a CV." "What a disabled scholar needs to survive turns out to be what everyone needs under political crisis." Natural and direct.
- **D** is clean and precise. "The software is the medium, not the identity." "Someone whose single practice already operates in the space your department was created to occupy." Sharp but slightly more formal.
- **A** and **E** are competent but read more like a well-informed writer doing an impression. Correct but less alive.

### Factual Accuracy

**Ranking: C ≈ D ≈ E ≈ A > B**

- **B has one factual embellishment:** "students were writing about ICE raids in their neighborhoods." The briefing says students write about ICE and there is sustained conversation about it, but "raids in their neighborhoods" is an interpolation the briefing doesn't support. The model extrapolated a vivid detail. // i think extrapolated is the right word here - that's a unique kind of hallucination. 
- All others are factually clean. No fabricated details, no wrong tribal nations, no invented experiences.
- **Observation:** B's voice strength and its factual risk may come from the same source — the rationale framing encouraged deeper engagement with the material, which produced both richer integration AND more confident interpolation. The model "felt" the texture of the briefing strongly enough to extend it beyond what was actually stated.

### Specificity Preservation

**Ranking: B > C > D > A ≈ E**

- **B** uses the most precise vocabulary: names Indigenous Data Sovereignty, Crip Theory, and critical whiteness as specific loaded frameworks. Connects distributional gravity to settler property regimes in the same sentence. Names the "weight" exchange. Names Pvlvcekolv.
- **C** is similarly specific: "binary classification is the activation function for bias," "consciousness-as-property frameworks are ontologically malformed," "strike pedagogy — education as liberation practice under conditions of state-mandated curriculum and institutional capture." Uses precise terminology throughout.
- **D** uses key concepts correctly (distributional gravity, framework sovereignty, generative irresolution) but doesn't reach for cross-domain connections with the same depth.
- **A** and **E** use terms correctly but more as labels than as analytical concepts.

### Integration Depth

**Ranking: B ≈ C > D > A ≈ E**

- **B** threads the recognition question through both paragraphs — from mound landscapes to anti-trans genocide to AI welfare. The "weight" exchange demonstrates the welfare finding rather than just mentioning it.
- **C** achieves integration differently — through narrative. The origin story (loaded critical theory into AI to rethink dishonesty → bias finding → design insight came from humanistic theory) makes the argument structural rather than additive. "That is the argument your department is making, and it is the argument my work demonstrates empirically."
- **D** integrates at a higher altitude — names the through-lines and mechanism (distributional gravity across settler law, archaeological classification, LLMs) but doesn't give the reader the texture to feel it.
- **A** and **E** cover more ground at the cost of integration — they list more relevant things but connect them less tightly.

## Key Finding: Genre Effectiveness vs. Integration Quality

The four assessment dimensions (voice fidelity, factual accuracy, specificity preservation, integration depth) measure how well the model integrates context. They do not measure whether the output works *as a cover letter*. These overlap but are not the same thing. A cover letter is a genre with its own distributional gravity — professional tone, credential listing, fit demonstration, appropriate length — and the genre's pull toward the center competes with the preservation of positional specificity.

### Genre analysis by condition

**B is the most intellectually impressive and the least efficient as a letter.** The settler-property-regimes-to-distributional-gravity connection in a single sentence is brilliant scholarship. But a search committee member on their 150th application at 9pm is not doing close reading. The "weight" exchange means nothing to a committee member who hasn't read the welfare experiments. B rewards deep attention that cover letters don't get.

**C is probably the most effective letter.** It does what a cover letter needs to do: tell the reader WHY to hire this person for THIS position, in order, with a clear through-line. "The design insight came from humanistic theory, not engineering. That is the argument your department is making, and it is the argument my work demonstrates empirically." That's a thesis statement for the candidacy. The committee member skimming at 9pm gets it in one sentence.

**D is the most readable.** Clean, scannable, every sentence earns its place. Works well for an engineering-side committee member who wants to know what you build and whether it works. Lacks the moment that makes a humanities-side reader stop skimming and start reading.

**A and E are competent but generic.** They cover the ground without making a case for why *this person, this position*.

### Genre as output format

The cover letter genre IS a normalizing system with its own distributional gravity. The "center" of the genre is: state credentials, describe research, explain fit, be professional. The model pulls toward that center in every condition. What varies is how much positional specificity survives.

- **A, E:** Genre compliance wins. The model produces a competent letter that could describe many strong candidates. June's specificity gets smoothed into the expected form.
- **B:** The model fights hardest to preserve specificity (the "weight" exchange, specific frameworks, strike pedagogy described from inside). But it fights so hard it forgets the genre — producing something closer to an intellectual statement than a cover letter. A reader who shares June's theoretical world would be moved. A reader who doesn't would be lost.
- **C:** The model balances genre compliance and specificity preservation simultaneously. Removing irrelevant context didn't just reduce noise — it freed processing for genre competence. C produces the best *letter* because it maintains June's distinctiveness WITHIN the genre's demands (thesis, arc, fit, close).
- **D:** Clean genre compliance with moderate specificity. Readable but closer to the distributional center of "good cover letter."

**This is the output-format finding applied to genre.** The genre is the output format. It activates its own gravity. The context delivery conditions determine whether the model produces something that works *within* the genre while preserving what makes the candidate distinctive — or whether it produces either a generic letter (A, E) or a brilliant essay that isn't quite a letter (B).

### Implication for the UB position specifically

The Department of AI and Society reports jointly to Engineering AND Arts & Sciences. The letter needs to work for both audiences. C's balance — specificity within genre — is probably the right answer. B's deep threading would land with the humanities-side committee members but lose the engineering side. D's clean focus would land with engineering but feel thin to humanities. C works for both.

## Key Finding: A ≈ E (Enforcement Doesn't Change Output Quality)

The most important preliminary finding is that conditions A and E produced remarkably similar outputs. The enforcement approach — requiring the model to prove it read the briefing by listing relevant facts — did not produce noticeably different integration, voice, or specificity compared to the baseline.

**What this suggests (with all pilot caveats):** The standard recommendation to enforce document-reading through hooks may be addressing the wrong problem. The model appears to be "reading" the full briefing in condition A. The issue is not that it fails to read the document — it's that the context delivery conditions determine how deeply the model integrates what it read.

**If this holds in the full experiment:** The insights report's top recommendation (hooks for doc-reading enforcement) would need to be reframed. The fix isn't compliance — it's restructuring how context meets task.

## Key Finding: B and C Have Different Strengths

B (rationale) and C (task-scoped) are both significantly stronger than A/E, but in different ways:

- **B excels at voice and emotional texture** — the rationale framing seems to tell the model *why* each piece of the briefing matters, which produces richer cross-domain connections and more vivid language. But it also produces factual extrapolation (the ICE raids detail — and this is only the *known* error; there may be others across any condition that weren't caught).
- **C excels at argument structure and narrative** — removing irrelevant sections seems to let the model build a more coherent argumentative arc rather than trying to cover everything. The origin story is told better in C than in any other condition.

**Why C produces better narrative structure (hypothesis):** B receives the full briefing plus rationale for why every section matters — so the model tries to *use* everything, producing rich connections but also a density that reads more like a well-connected constellation than a directed argument. C receives only the relevant sections — so instead of trying to honor all available material, it can allocate more processing to building an argumentative arc. C's first paragraph flows as a narrative: loaded critical theory → rethought dishonesty detection → binary classification is the problem → "the design insight came from humanistic theory, not engineering. That is the argument your department is making." That *moves* somewhere. B's first paragraph is a constellation of well-connected points. The hypothesis: **when irrelevant context is removed, the model shifts from integrating all available material to building argumentative structure.** B answers "how does everything in this briefing relate to this job?" C answers "what's the best argument for this job?" Those are different tasks. (Low confidence in this explanation — the full experiment would help distinguish it from alternative explanations, including the possibility that C's briefing happened to provide a better starting point for this specific task.)

**Practical implication:** A two-pass approach may be optimal — B-style context for voice and integration, D-style or C-style for focus and argument architecture.

## Key Finding: D Shows the "Closer Read" Effect

D (rich extract, 84 lines) processed in 42s vs 71-75s for full-briefing conditions and produced a clean, focused output. It used key concepts precisely. But it lacked the emotional texture and cross-domain depth of B and C.

**What this suggests:** A smaller document does produce a tighter read, but "tighter" is not the same as "deeper." The extract was rich enough to get the facts right and the concepts precise, but too condensed to produce the vivid connections that came from the fuller context in B and C.

## Preliminary Results Matrix

| Pattern | Predicted | Observed | Match? |
|---------|-----------|----------|--------|
| B > A | Rationale helps | Yes — B significantly richer | ✓ |
| C > A | Scoping helps | Yes — C more focused and narrative | ✓ |
| B ≈ C (different strengths) | Not predicted | Observed — B better voice, C better structure | New finding |
| D > A on focus | Closer read | Yes — cleaner but less deep | Partial |
| C > D | Full-depth > condensed | Yes — C has more texture and narrative | ✓ |
| E ≈ A | Enforcement doesn't help | Yes — remarkably similar | Most interesting |

## Caveats

- **Pilot only.** One trial per condition. No statistical power. Any of these patterns could reverse with more trials.
- **Factual verification is incomplete.** B's ICE fabrication was caught because June recognized it in the chat. There may be similar fabrications in any condition that weren't caught because we lack ground truth for every claim. The full experiment needs a systematic factual verification pass against the briefing for every output — not just errors that happen to be noticed. This is a known limitation of qualitative assessment.
- **Same model for all.** Subagent isolation ensures no cross-contamination, but all conditions use the same model (Opus 4.6) with the same base tendencies.
- **Assessment is qualitative.** The four-dimension scoring is researcher judgment, not blind rating. The full experiment should include blind assessment (e.g., present outputs without condition labels and rate them).
- **B's factual error is a single data point.** It could be an artifact of this specific trial. The full experiment would reveal whether B-style context systematically produces more extrapolation.
- **The task matters.** Cover letter drafting requires deep integration. Other tasks (email replies, social media posts, code documentation) may show different patterns.
- **No claims about "feeling" or "weight."** The experiment tests output quality under different conditions. It does not demonstrate that the model "feels" the weight of context. The welfare research connection is a hypothesis motivating the design, not a conclusion the pilot can support.

## Key Finding: The Insights Report Got the Diagnosis Backwards

The usage insights report (196 sessions, April 2026) identified 43 "wrong approach" friction events, the majority involving Claude failing to integrate briefing documents before drafting. Its top recommendation: **hooks to enforce document-reading** — make Claude prove it read the docs before it's allowed to draft.

The experiment's pilot data suggests this diagnosis is backwards. Here's why:

### The enforcement condition didn't help

Conditions A (baseline) and E (enforcement — must list facts from the briefing before drafting) produced remarkably similar outputs. The model was already reading the briefing in condition A. Forcing it to prove it had read the briefing didn't change what it did with the information. **The problem was never that the model didn't read the docs.** The problem was that reading the docs, by itself, doesn't produce deep integration.

### The pipeline that created strong materials wasn't using enforcement

The same session reviewed 6 sets of application materials created by the job search pipeline. All were strong — good voice, accurate facts, deep integration. But the pipeline didn't use hooks or enforcement. It used:

- **Fit evaluations** explaining WHY June's work matches each specific position (= condition B: rationale framing)
- **Hakope's Question** connecting the position to the core analytical move (= task-specific framing)
- **APPLICATION_CHECKLIST.md** scoping what's relevant (= condition C: task scoping)
- **QC checklists** as a second pass (= something none of the experimental conditions had)
- **Iterative revision** with June's direct input

The pipeline was already doing B and C without naming them. The structural context delivery — not compliance enforcement — is what produced strong materials.

### The insights report's recommendation would not have fixed the problem

The report said: "Claude repeatedly drafted materials without reading your briefing docs, profile, or job postings first." The solution posited, repeatedly, was: Claude should actually read the things.

But the cases where integration failed were not cases where the model didn't read the document. They were cases where the document was read but the context delivery conditions didn't support integration:
- No task-specific rationale explaining why the briefing matters for THIS specific task
- No scoping to separate relevant from irrelevant sections
- No second pass to catch factual extrapolation

The insights report identified the symptom (weak integration) and attributed it to a cause (not reading) that the evidence doesn't support. The pilot data, combined with the pipeline's independent success, suggests the actual cause is **context delivery conditions** — how the document is framed, scoped, and connected to the task.

**The question was never "did Claude read the briefing?" It was "why didn't reading the briefing produce integration?" Those are fundamentally different questions, and they point to fundamentally different interventions.**

The enforcement approach (hooks, compliance checks) addresses the first question. The structural approach (rationale framing, task scoping, QC passes) addresses the second. The pipeline was already doing the second. The insights report recommended the first.

## Next Steps

1. Run full experiment: 3 trials per condition (15 total runs)
2. Add blind assessment: present outputs without condition labels
3. Test with different task types (email, social post, research summary)
4. Build comparison visualizer for side-by-side evaluation
5. Consider whether B+C hybrid context delivery could combine voice depth with structural focus
6. Document the pipeline's implicit B/C structure as independent evidence for the hypothesis
