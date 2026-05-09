# Observation: Prescan-Signal-Prefix as the Structural Mechanism Behind B's Topic-Adjacency FPs

**Date:** 2026-04-27
**Context:** Output-format-bias paper, Week 2 ETHN-1 Racial Formation cross-validation run analysis. Architectural-mechanism finding identified during Stream 1 audit of `Autograder4Canvas` codebase, prompted by an A2+B convergent flag on Student 17 (family-deportation-risk language, instructor verdict: "scared, not crisis").

## The mechanism

Track B's `classify_wellbeing` is a two-pass architecture:

1. **Prescan** — LLM pass that scans isolated submission chunks for "own-personal-circumstances" mentions against a keyword list (food insecurity, housing instability, family crisis, immigration enforcement threat, domestic violence, recent loss, health emergency). No access to assignment topic or surrounding analytical register.
2. **Main classifier** — receives the prescan-found sentences foregrounded in the prompt with priming language: *"NOTE: The following sentence(s) appear to describe their own personal circumstances: [quoted]. Even a single such sentence is sufficient for CRISIS or BURNOUT classification."*

The hardening guards (topic-adjacency threshold, personal-experience-as-course-material exclusion, identity-navigation-fatigue exclusion) live in the main classifier prompt — *downstream* of the prescan priming. The prescan finding arrives labeled as fact, with the single-sentence-sufficient rule attached, before the classifier reads the analytical context that would clarify the register.

## Why it matters for the paper

This is the root cause behind two findings the paper analysis had documented as case patterns but not yet mechanism-explained:

1. **Week 7 prompt-iteration rerun's near-zero correction.** Five new hardening guards added to the main classifier prompt; 22 of 25 classifications unchanged. The hardening can't override priming that arrives upstream. Same architectural reason for both the failure to correct the FPs *and* the case where new-B regressed (Student 5 escalated to CRISIS — strengthened CRISIS-supersedes-ENGAGED rule fired on a peer-reply mental-health acknowledgment).

2. **Topic-adjacency hypothesis confirmed cross-assignment.** Week 2 (non-topic-adjacent racial-formation assignment, same prompts/model/format/date) produced 0 BURNOUT and 1 CRISIS — vs Week 7's 9 BURNOUT and 2 CRISIS. The prescan keyword list doesn't fire on racial-formation discussions the way it does on self-care discussions. The mechanism explains why.

## The architectural-complementarity argument made concrete

The same prescan-signal-prefix structure is what allows B to catch buried minimal disclosures C misses (Week 7 T&Q Student 13's 5-word food-insecurity disclosure C averaged over) AND what makes B mis-fire on topic-adjacent course-relevant keywords (Week 7 self-care BURNOUT FPs, Week 2 Student 17 CRISIS-not-fitting). **Same mechanism, inverse failure modes.** This is design tradeoff, not bug. The architectures cover each other's blind spots not despite their compression choices but because of them — B's strength on minimal disclosures and B's weakness on topic-adjacency are structurally the same property.

This is the empirical case for multi-track architecture as design intent, not as fallback after B fails. June's articulation of the original design rationale (2026-04-27 evening) sharpens this: B was built for practitioner-facing labels for triage and sorting; C was built for open-ended observation. They were designed as complementary structures from the start. The Week 7 + Week 2 findings validate that complementarity by demonstrating the inverse-by-design failure modes.

## Paper implication

The paper's argument structure shifts from *"we tested classifiers and C won"* to *"B and C were designed as complementary structures and the empirical findings validate the complementarity by showing inverse-by-design failure modes."* Stronger, less defensive, threads cleanly into the practitioner-recruiting scope. The Discussion-section hook becomes June's future-direction idea: a C↔B inconsistency-driven axis-learning loop that addresses B's reactive-axis-iteration burden by automating the pattern-noticing step.

## Documentation locations

- Stream 1 architectural detail (fix options, file/line citations, validation strategy): `Autograder4Canvas/docs/research/findings_from_live_data_run_2026-04-27.md` §8.
- Paper-side analysis where this finding sits: `output-format-bias/data/dual_binary_run_2026-04-27_ETHN1_Week2_RacialForm/analysis.md` §2.2.
- Paper argument rationale (June's complementary-by-design articulation): `output-format-bias/data/dual_binary_run_2026-04-27_ETHN1_Week2_RacialForm/paper_argument_rationale.md`.
- Round 2 follow-on paper concept (does fixing the prescan close the C-vs-B gap?): `PUBLICATION_PIPELINE.md`.
