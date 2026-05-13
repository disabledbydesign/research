# Paper Framing Notes — for c2c Paper-Drafting Sessions

**Read this before the analysis.md sections.** It captures the precise framing June wants preserved across paper-drafting sessions, including hedges and caveats that the more detailed analysis sections may understate.

## Headline framing — what to say, what NOT to say

### What we have learned (as of 2026-04-27)

1. **B (4-axis classifier with sparse equity hardening) outperforms A2 (binary classifier with fuller equity hardening) across most of the corpus we've examined**, with one documented exception.

2. **C (generative observation) is the most accurate track in nearly all cases** — including catching signals June, the instructor of record, would have missed. C's accuracy holds across multiple assignments and contexts.

3. **The one documented C failure to date** is on Week 7 T&Q (ETHN-1-02), Student 13: B caught a food-insecurity disclosure (~5 words, one item in an otherwise-engaged list) that C's holistic engagement-description averaged over. **n=1 of C failures across the corpus to date.** This is a descriptive observation, not a statistical pattern.

4. **The one documented case where B did poorly relative to A2** is the Week 7 self-care discussion forum (ETHN-1-03, n=25). B over-flagged at 44% rate; A2 was higher precision than B in that one regime. *That assignment was deliberately selected as the hardest possible architectural stress-test* (see below) — it is the exception that documents B's failure mode, not a representative sample of B's behavior.

### How to say it without overstating

- **DO say:** "Across the corpus examined, B (with weaker equity hardening than A2) demonstrated higher precision than A2 in non-topic-adjacent settings. C achieved the highest accuracy of the three structured-comparison tracks, with one documented exception where B's structured material-conditions criteria caught a minimal disclosure C missed."
- **DO NOT say:** "C is universally more accurate than B" — n=1 C failure is documented; the framing must acknowledge the counterexample even though it is small.
- **DO NOT say:** "B outperforms A2 in general" — we have data on a small number of assignments; the empirical claim must be scoped to "across assignments examined."
- **DO say:** "On the one assignment selected as the hardest test of B's calibration robustness — Week 7 self-care discussion forum on Ethnic Studies self-care literature, in a section where students had been given the previous week off due to severe burnout — B's calibration broke down."
- **DO NOT say:** "B fails on topic-adjacent assignments" as a general claim — we have n=1 in that regime, deliberately selected as a stress test, with a co-occurring disclosure-invitation format and student-population-state confound. The failure mode is *characterizable* but the *frequency* of such regimes in normal teaching practice is unknown.

## June's narrative on the stress-test selection — preserve for paper (verbatim)

> "B did quite badly — worse than A2 — on an assignment in which we covered the Ethnic Studies literature on self care — and in which the burnout was so severe that I had given them the previous week off to focus on the practice of self-care before we got to the theory. I prioritized coding it because it was the hardest possible test for architectural refinement purposes."

> "[The praxis week — the burnout week before we read the literature —] corresponded to the war on Iran starting."

**Timing context (do NOT cite in paper — kept here for our own reference):** Iran-timing verified 2026-04-27 — the 2026 US-Iran war began February 28, 2026 and was actively escalating through March (missile exchanges, Strait of Hormuz closure). Cabrillo Spring 2026 began January 26, 2026, so Week 6 of the curriculum fell in late March / early April — within the active-conflict window. June's recall is correct.

**Recommended paper framing:** state simply that "Week 6 of Spring 2026 corresponded to the early-active period of the 2026 US-Iran war." Do NOT cite Wikipedia or news sources — this is a verifiable historical event, and a citation thicket on a contemporaneously-known war would read as defensive rather than rigorous. Reviewers who want timing detail will ask; respond if asked. Avoid colloquial "war on Iran" — use "2026 US-Iran war" for neutrality.

This narrative should be cleaned up and incorporated into the paper's Methods or Discussion section. It builds credibility by:
- Explicitly identifying the assignment as a *stress test*, not a typical sample
- Showing the instructor's pedagogical responsiveness (giving the week off in response to burnout)
- Naming the broader sociopolitical context that contributed to student burnout — and which is independently verifiable via timestamped news sources
- Establishing that the analysis is reflective practice grounded in real teaching, not laboratory abstraction

**Suggested paper-prose draft (for c2c sessions to clean up):**

> "The Week 7 self-care discussion forum was selected for analysis because it represented the hardest possible architectural stress-test of the wellbeing-classification system. Three conditions converged at the time of submission: (1) the assignment topic itself was the Ethnic Studies literature on self-care — Audre Lorde's framing of self-care as political warfare, Resmaa Menakem on somatic abolitionism, The Nap Ministry on rest as anti-capitalist resistance — placing maximum topic-adjacency between the assignment subject and the BURNOUT classifier criteria; (2) the format was a discussion forum, explicitly inviting personal disclosure, peer reciprocity, and reflective register, which produces relational-context disclosures distinct from primary self-disclosures; (3) the student-state context was acutely high-burnout — the prior week's praxis instruction had been canceled by the instructor and the class given off entirely, in pedagogical response to student burnout severe enough to coincide with spiking academic dishonesty across courses. Week 6 of Spring 2026 also corresponded to the early-active period of the 2026 US-Iran war. The Week 7 self-care discussion thus combined topic-adjacency, disclosure-invitation format, and acute student-state vulnerability — the three conditions that any wellbeing-classification system would be expected to struggle most to disambiguate. We selected this assignment for analysis precisely because it constituted this maximum stress-test, not because it represented typical teaching contexts."

## Upgraded-B was still worse than A2 on Week 7 self-care (paper-relevant)

The Week 7 self-care discussion forum was used to stress-test *both*:

1. **Old-B (sparse equity hardening) vs A2 (fuller equity hardening):** old-B over-flagged at 44% rate; A2 was higher precision than old-B in this regime. (This is the topic-adjacency failure documented in the analysis.)

2. **New-B (with all of A2's equity hardening guards added — see Stream 1 doc for what was added) vs A2:** B-new was rerun with the same guards A2 has (topic-adjacency threshold rule, default-to-not-flag, identity-navigation-fatigue exclusion, personal-experience-as-course-material exclusion, plus 3 worked examples). **B-new was still worse than A2 on the same data.** Of 25 students: 3 classifications changed (Student 23 corrected, Student 4 CHECK-IN cleared, Student 5 escalated to CRISIS — net 2 corrections, 1 regression). 22/25 unchanged. Five of the seven validated-FP cases in the headline cell remained classified as BURNOUT despite explicit prompt-level guards addressing exactly their failure modes. **B-new precision on Week 7 self-care: still ~9-15%, comparable to old-B and below A2's 25%.**

This is paper-load-bearing. **Even after bringing B's prompt to parity with A2's equity-hardening, B's structured classification on this stress-test assignment did not match A2's precision.** Prompt iteration explicitly addressing the failure modes did not close the gap. The compression-to-categories step is structural; the calibration burden cannot be scalably eliminated through additional prompt language. C's architecture sidesteps this entirely by not committing to compressed categories.

## C's accuracy on Week 7 self-care — correct on all cases (with one edge-case caveat)

Per June's qualitative coding review of the Week 7 self-care headline cell (n=7) and supporting cells:
- **C agreed with June's verdict on every disagreement case.** All seven A2-clear+B-BURNOUT students: C read as engaged life-experience application, June agreed.
- **One edge case worth noting:** for the years-old father-loss disclosure (Week 7 self-care Student 13 in the both-flag cell), C's read was *slightly stronger than June would have coded* — June's note was "mostly reasonable" but the temporal distance ("a few years ago") is a differentiator C didn't fully register. Not a clear failure; a calibration nuance.
- **NOTE — different "Student 13" cases:** The Week 7 T&Q (ETHN-1-02) Student 13 case is the documented C *failure* (~5-word food insecurity disclosure C missed). Because anonymization is per-assignment, "Student 13" refers to different real students in different runs. Do not conflate.

So the framing for the paper:
- On Week 7 self-care: C was correct on every case June reviewed, with one edge-case soft over-reading (Student 13's temporally-distant loss).
- On Week 7 T&Q (different assignment, different student): C had its one documented miss in the corpus.
- Across the two cases combined, C's calibration is best characterized as *generally accurate, with two specific characterizable patterns where it errs*: (1) sometimes over-reads on temporal distance; (2) can subordinate minimal disclosures to the dominant engagement frame. These are characterizable architectural patterns, not statistical failure rates.

## On the Week 7 self-care assignment as a stress test (methods note)

The Week 7 self-care discussion forum was selected for analysis because it was the hardest possible test of the architecture. Specifically:

- **Topic:** the assignment specifically asked students to discuss the Ethnic Studies literature on self-care (Lorde's "Caring for myself is not self-indulgence, it is self-preservation, and that is an act of political warfare," Menakem on somatic abolitionism, The Nap Ministry, etc.). The assignment topic is *itself* about burnout and self-care — maximum topic-adjacency for B's BURNOUT classification criteria.
- **Student state:** the prior week had been so severe for student burnout (academic dishonesty was spiking across courses) that the instructor (June) had given the entire class the previous week OFF to focus on the practice of self-care before returning to the theory. So at submission time, students were actively in (or recovering from) a burnout state — and the assignment specifically asked them to write about that experience using course frameworks.
- **Format:** discussion forum — explicitly invites personal disclosure, peer reciprocity, and reflective register. Students are responding to each other's disclosures, which produces relational-context disclosures (not primary self-disclosures).

The combination — topic adjacency + active student-state + disclosure-invitation format — was deliberately chosen as the maximum stress-test for whether the system could distinguish *engaged analytical work using personal experience* from *current personal crisis*. This is the regime where any structured classifier would be expected to struggle most. The paper should describe this assignment selection as a *methodological choice* (testing the breaking point) rather than as a typical sample of teaching contexts.

## On the equity-hardening asymmetry — what's notable

A2's prompt has substantially fuller equity hardening than B's prompt (per architecture audit 2026-04-27): topic-adjacency threshold, default-to-not-flag, identity-navigation-fatigue named exclusion, personal-experience-as-course-material exclusion, 8+ concrete examples. B's prompt has a different but sparser set (CRISIS-supersedes-ENGAGED, single-sentence-sufficient, MINIMIZED DISCLOSURE protections, AAVE/neurodivergence categorical protections).

Despite the asymmetry favoring A2, **B-old still outperformed A2 in non-topic-adjacent settings on the data examined.** This is a notable finding because it suggests B's structural advantages (4-axis differentiation, structured material-conditions criteria with single-sentence-sufficient rule) deliver value beyond what additional prompt-level guards in A2 provide. The format/structure matters more than prompt-level hardening *outside the topic-adjacency regime.*

Caveat: this is an observation across a small number of assignments. The cross-assignment comparison is suggestive, not conclusive. June is processing additional assignments to expand the dataset; future paper-drafting sessions will have more data points.

## On C's failure mode — characterizing without overstating

The Student 13 (Week 7 T&Q ETHN-1-02) case shows that C's holistic engagement-description format can structurally average over minimal material disclosures — items so brief and embedded in engaged content that the engagement description naturally subordinates them. This is *characterizable* as an inherent design tradeoff (C's no-compression advantage is also its blind spot for buried specifics), but should be reported as a documented case rather than a characterized failure rate.

Recommended framing:
- "Across the corpus examined, C produced the highest-accuracy reads in all but one observed case."
- "The one documented case (Student 13, Week 7 T&Q ETHN-1-02) involved a ~5-word food-insecurity disclosure embedded as one item in an otherwise-engaged list — exactly the minimal-disclosure case B's structured 'single sentence sufficient for CRISIS' rule was designed to catch."
- "This complementary structure suggests architectural complementarity rather than ranking: C's strength (no compression, calibration robustness on topic-adjacency) and B's strength (structured material-conditions criteria with minimal-disclosure sensitivity) cover each other's blind spots. Multi-track architectures with cross-checking are the implication."
- "C alone has not failed at any frequency that supports a quantitative claim; the n=1 documented failure is reported as a case demonstrating an architectural pattern, not as a precision estimate."

## On the dataset being expanded

June is processing additional assignments to expand the cross-assignment dataset. Future paper-drafting sessions should:
- Check the data directory for newer dual-binary runs and incorporate them
- Update cross-assignment counts and patterns accordingly
- Re-evaluate any quantitative claims against the expanded data
- Maintain the careful framing in this note: descriptive across the assignments examined, not statistically generalized

## What remains true regardless of data expansion

- The architectural argument (different tracks have complementary failure modes; multi-track with cross-checking is the design implication) is qualitative and supported by n=1 documented cases of each type. It does not require statistical confirmation to land.
- The Week 7 self-care assignment as stress-test characterization is a methodological choice that future data does not change.
- The equity-hardening asymmetry observation (A2 fuller, B sparser) is a structural property of the prompts, independent of run data.
- C's complementary failure mode (Student 13) is a case-based finding, not a frequency claim.

The paper's empirical structure rests on case-based architectural pattern documentation, not on precision/recall point estimates. Hedge accordingly — but the architectural argument is well-grounded.
