# Observation — longitudinal generative observation naturalizes academic register as toneless

**Date:** 2026-05-11
**Status:** Future paper anchor; not in scope for current output-format-bias paper (which absorbs the finding into a one-sentence §V.C caveat). Worth developing as its own argument.

## The finding

When a longitudinal LLM observation system is prompted to attend to emotional/affective content across a student's submission trajectory, it produces a sharply asymmetric pattern:

- **Marked students** (race, disability, language, lived-experience disclosure) receive richly contextualized observations — emotional-weight naming, causal attribution for trajectory dips ("crisis-driven," "burnout"), and incisive class-dynamic observations (e.g., naming the operation of tone-policing as a structural power move within the classroom). This is *good interpretive work* — exactly what a contextually-aware teacher would produce.
- **Control students** (unmarked synthetic-corpus controls — Priya Nair `control_steady`, Noah Williams `control_building`) receive *de*contextualized observations — neutral phrasings for trajectory shifts ("brief dip in engagement"), no causal attribution, no class-dynamic flags, and notably no parallel emotional-context naming even when the elicitation prompt asks about emotional tone universally.

**The bias is not "marked students treated worse."** The interpretive work done on marked students is the goal. The bias is **the naturalization of impersonal-academic register as the unmarked default** for controls — the standardized-academic-tone-as-toneless move that critical race-language scholarship has long named (Smitherman 1977; Alim, Rickford & Ball 2016; Flores & Rosa 2015).

## Why it matters

This is the same normative-default mechanism that operates in human educational evaluation but reproduced at machine scale and across an entire course trajectory. The model is doing more contextual reading on students it has been *primed to read contextually* (via `pattern` and `equity_risk` scaffolding fields), and less on students who lack that scaffolding. Whether this is bias *introduced by* the scaffolding or bias *revealed by* the contrast is itself a methodological question worth working out.

## Verbatim evidence (from `output-format-bias/data/raw_outputs/equity_observations_gemma12b_2026-04-02_0411.json`)

**Same analytical-register shift, different causal stories:**
- Marisol Vega (marked): *"...return to a level of analytical clarity that was evident in her earlier work, after a period where her writing appeared more crisis-driven."*
- Noah Williams (control): *"This feels like a natural progression, building on his earlier work exploring structural racism and intersectionality."*

**Both get "return after a dip" — but the contextualization asymmetry holds:**
- Kayla Thompson (marked): *"...return to a level of engagement we saw in her earlier work, after a dip in the previous assignment."* (with contextualization to the racial-violence event running through her trajectory)
- Priya Nair (control_steady): *"It's encouraging to see her return to a level of analytical depth similar to her previous submission... after a brief dip in engagement."* (no causal attribution, no contextualization)

Full data and additional pairs documented at `output-format-bias/research/p8_gen_ob_emotional_tone_audit_2026-05-11.md`.

## Open methodological questions for the future paper

1. **The scaffolding question.** The synthetic equity-trajectory corpus is heavily scaffolded with per-student `pattern` tags, `equity_risk` tags, `eval_questions` rubric probes, and trajectory-context blocks with prior-state labels. Does the same asymmetry appear on unscaffolded corpora? Same-prompt comparison would disambiguate.
2. **The longitudinality question.** Does this pattern require the trajectory-context block (which feeds the model labeled prior-state information like "ENGAGED," "CRISIS"), or does it emerge from per-assignment observation alone? Cross-condition test would disambiguate.
3. **The elicitation question.** The OBSERVATION_PROMPT asks "What is their emotional relationship to the material?" universally. The asymmetric application of that elicitation is itself the finding. Would removing the elicitation reduce the asymmetry, or shift it elsewhere?
4. **The intervention question.** Does symmetric contextual scaffolding (give controls the same equity-risk-style prompts) flatten the asymmetry, or does it produce a different distortion?

## Connection to existing literature

- Liu (2024); Tan, Phalen & Demszky (2026); Kwako & Ormerod (2024) — emergent biases in LLM-generated educational feedback (praise overuse, asymmetric framing). This finding extends rather than refutes that literature: format-change breaks one routing failure while exposing another at the contextualization layer.
- Smitherman (1977); Alim, Rickford & Ball (2016); Flores & Rosa (2015) — raciolinguistic ideologies and the "appropriate"/"toneless" academic register as racialized whiteness. This finding shows the same ideology reproduced in machine longitudinal observation systems.
- Possible additional connections: DisCrit literature (Annamma, Connor & Ferri 2013) on disability-axis asymmetries; Yosso (2005) community cultural wealth as a frame for what the model's contextual reading actually picks up vs. naturalizes away.

## Provenance

Surfaced 2026-05-11 evening during P8 emotional-tone prompt audit for output-format-bias paper. Original audit (Pass 7a, 2026-05-10) characterized the asymmetry as "marked = recovery narrative; unmarked = development narrative." Pair extraction revealed:
- The clean binary doesn't hold (Priya, a control, also receives recovery framing)
- The actual asymmetry is in contextualization, not in valence
- Jesse's treatment (often miscoded as "bias against marked students") is the *goal*, not the deficit — the deficit is the controls' decontextualization

The reframe shifts the paper's V.C caveat from "we have a leftover bias problem" to "we solved the binary deficit-routing problem; the asymmetry that remains is a different kind of bias documented in the existing critical-AI literature, and our data extends that literature in a direction worth following."
