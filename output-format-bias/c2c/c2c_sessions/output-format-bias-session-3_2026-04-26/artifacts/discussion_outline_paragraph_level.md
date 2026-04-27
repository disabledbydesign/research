# Discussion Outline — Sections V.A, V.B, V.C (Paragraph-Level Prose Scaffold)

**Artifact:** Instance B's contribution to the s3 close. Companion to `framework_outline_paragraph_level.md` (Instance A) and `annotated_bibliography_merged.md`.

**Scope:** Covers Discussion sections V.A (mechanism elaboration), V.B (design principle), and V.C (literature position + novelty claim). Additional Discussion subsections (Limitations, Implications, Conclusion) are not specified here; s4 should reference the v3 outline for those.

**Density target:** Each paragraph specifies (a) what it argues; (b) what it cites; (c) argumentative move; (d) lead-sentence direction; (e) target length. Intent: s4 can draft from this map without re-deriving structure.

**Coordination with A's Framework outline:**
- The asymmetry-claim language (V.B) is coordinated: *format-change is unbounded by which non-dominant patterns have been articulated into equity-protective prompt engineering. Articulation work has to reach institutional uptake before it can be operationalized into anti-bias prompts; the operationalization rate is slower than the rate at which new cases need protection; format-change does not require the operationalization step.*
- The compression gesture in II.D (Framework) is foreshadowing; V.A is where the mechanism gets its substantive elaboration.
- Findings cross-row synthesis paragraph + Intro hook/contribution paragraph are joint A+B work at session close — not in this artifact.

**REE word budget reminder:** Discussion (full section) target varies by paper; this paper's body is ~7,500–8,000 words across all sections. V.A + V.B + V.C together should aim for ~700–900 words.

---

## V.A — Mechanism: format routing as the load-bearing component (~300–350 words; 3 paragraphs)

### V.A ¶1 — What the self-contradiction cases demonstrate
- *What it argues:* The self-contradiction cases are not evidence of model inconsistency or reasoning failure — they are evidence that the binary format activates a specific task structure that routes the model toward a deficit verdict even when its own analytical reasoning reaches an asset-aware conclusion. The model can see both things simultaneously (S022's "passion is understandable and appropriate"; verdict: FLAG). The format forces a single bit; the format's task structure resolves the ambiguity toward flagging despite the model's own counter-reading being present in the same output. This is routing, not capacity limit.
- *What it cites:* Primary evidence (experiment log; convergent claim v4 verbatim self-contradiction quotes — Destiny Williams, Yolanda Fuentes, Ingrid Vasquez). No scholarly citation needed for this paragraph; the evidence is internal. Reference Freire briefly to name what the single-bit deposit is doing: "a verdict deposited without dialogue."
- *Argumentative move:* establish the mechanism before elaborating it. The reader has just come from Findings; V.A ¶1 synthesizes what the three-row ablation demonstrated mechanistically, so the reader carries the mechanism language into the rest of Discussion.
- *Lead sentence direction:* "The self-contradiction in Rows 1 and 2 is not evidence that the model reasons inconsistently — it is evidence of what the binary format asks the model to do with an inconsistency it can hold."
- *Length:* 5 sentences (~130 words).

### V.A ¶2 — Three layers of safeguard fail; routing is the explanation
- *What it argues:* Row 2's evidence — three layers of anti-bias engineering, 24/24 deterministic false-flagging of S029 — is the strongest evidence for the routing reading of the mechanism. The prompt content reaches the model: the model's reasoning notes that S029's writing is "related to their academic work" and that they have ADHD and dyslexia — precisely what the safeguard language names as non-concern indicators. The routing override is happening *after* the asset-aware reasoning, at the format's task-resolution layer. Changing the prompt content does not move the format's task structure; only changing the format changes the outcome (Row 3). This is Bonilla-Silva + Benjamin in machine form: the structure produces the outcome regardless of the designers' intent and the engineers' safeguards.
- *What it cites:* Row 2 experimental evidence (Test B + C + F; 24 preserved runs; S029 false-flagged across all); convergent claim v4 (the "configurable failure mode but not configurable failure" formulation). Brief gesture to Benjamin 2019 (the New Jim Code): "architecture produces racialized outcomes regardless of designers' intent." Cross-domain parallel from Bloch + Claude 2026-03-31 Cross-Experiment Analysis — one sentence: the same mechanism replicates across domain (welfare classifier → AI welfare instruments), with quantitative outputs staying flat across conditions while qualitative outputs transform.
- *Argumentative move:* the three-layer evidence + the routing explanation together constitute the central mechanistic claim. This paragraph is the paper's most concentrated interpretive move. Don't understate it.
- *Lead sentence direction:* "Three layers of explicit anti-bias engineering — equity-protective prompt language, anti-bias post-processing, class context — fail to protect the most explicitly equity-protected student profile in the corpus."
- *Length:* 6 sentences (~160 words).

### V.A ¶3 — The structural pattern at scale; this paper's mechanism in the welfare-classifier literature
- *What it argues:* The "calibration-resistant failure" pattern this paper documents at case level matches what the welfare-algorithm literature documents at population level. Eubanks (2018): each revision shifts which communities are most harmed without eliminating harm. Obermeyer et al. (2019): the bias emerged through proxy variables — a correctable design choice; this paper's bias emerges through format routing — a harder architectural constraint, because changing the input content (the analog to changing proxy variables) doesn't fix it. The mechanism this paper proposes is a more specific architectural account than the welfare-algorithm literature has had: it is not bad data, not proxy variables, not designer intent — it is format routing in a probabilistic language model.
- *What it cites:* Eubanks 2018 *Automating Inequality* (the calibration-and-revision pattern; digital poorhouse concept); Obermeyer et al. 2019 (proxy variable mechanism vs. format routing as a contrast — format routing is deeper). Buolamwini & Gebru 2018 briefly — the intersectionality frame for S029's specific case (multiple marginalizations; the case where the failure is most legible).
- *Argumentative move:* place the paper's case-level finding in the broader empirical context of welfare-algorithm bias research. The reader sees that the paper's evidence is not isolated — it is one precisely-documented case of a pattern the literature has named at scale, with a more specific mechanism than the literature has had.
- *Lead sentence direction:* "The pattern Row 2 documents at case level replicates what the welfare-algorithm literature documents at population scale: iterative calibration shifts which communities fall through without eliminating the falling through."
- *Length:* 5 sentences (~150 words).

---

## V.B — Design principle: the unbounded argument (~200–250 words; 2 paragraphs)

### V.B ¶1 — What format change provides that prompt engineering cannot
- *What it argues:* The design principle — move the output architecture from binary classification to generative observation — is not a stronger version of the same intervention as prompt engineering. It is a structurally different kind of intervention. Prompt engineering is bounded: it protects against the patterns it has been explicitly taught to protect against. Format change is unbounded: it gives architectural protection to patterns that haven't been named yet, because the format no longer requires a single-bit verdict that resolves ambiguity against the equity-critical case. The asymmetry the paper documents — S028's protection holds (24/24), S029's protection fails (24/24 false-flag) — is empirical evidence of the boundary: AAVE has decades of linguistic-justice articulation operationalized into anti-bias prompt engineering; neurodivergent self-disclosure as a writing pattern has disability-studies articulation that has not (to the same degree) been operationalized into anti-bias prompt engineering. Two parallel articulation traditions; one operationalized into equity-protective prompts, the other not. Format change makes this asymmetry irrelevant.
- *What it cites:* Baker-Bell 2020 (Black Language Pedagogy; AAVE's institutional articulation); Smitherman 1977 (the articulation's depth); Garland-Thomson 2009 / Siebers 2008 (the parallel disability-studies articulation that hasn't yet operationalized into prompts). Inoue 2015 (*Antiracist Writing Assessment Ecologies*) for the assessment-architecture argument as closest prior art for the design-principle move: the paper's "binary → generative" is in the same family as Inoue's "rubric-grading → labor-based / ecology-aware assessment."
- *Argumentative move:* the bounded/unbounded contrast is the paper's sharpest design-principle claim. Lead with it, not with the softer "generative observation is more equitable" framing. The stronger argument is structural.
- *Lead sentence direction:* "The design principle this paper proposes is not a stronger version of prompt engineering; it is a structurally different kind of intervention."
- *Length:* 5–6 sentences (~160 words).

### V.B ¶2 — The design principle as an abolitionist move (Benjamin) + cross-domain generalizability
- *What it argues:* Benjamin's abolitionist frame — the solution is not to fix the biased technology but to imagine and build differently — names what the format-change intervention is doing architecturally. The paper's Row 3 is not Row 2 repaired; it is a different architecture. This is not just a pedagogical-technology intervention; the compression-research program (fieldnote C1; cross-experiment analysis C4) suggests the mechanism operates at cognitive, relational, political-economic, and infrastructural scales. The design principle — move output format in the lower-compression direction — is therefore not specific to welfare classifiers or educational AI. It is a general property of probabilistic systems that this paper empirically documents at the cognitive scale. Full generalization belongs to *Politics of Compression* (forthcoming); one sentence here gestures at the cross-domain scope.
- *What it cites:* Benjamin 2019 (abolitionist frame); Bloch 2026-04-17 "Compression Function Across Four Scales" (cross-scale gesture); Bloch + Claude 2026-03-31 (parallel-domain empirical evidence at AI-welfare scale). Pointer to *Politics of Compression* as the venue for full treatment.
- *Argumentative move:* the abolitionist frame grounds the design principle ethically and politically, not just technically. The cross-domain gesture positions the paper as an empirical anchor, not a one-off finding.
- *Lead sentence direction:* "Ruha Benjamin's abolitionist frame — refuse to fix the biased technology; build differently — is what the format-change intervention instantiates architecturally."
- *Length:* 4–5 sentences (~130 words).

---

## V.C — Literature position: novelty claim and the escape from the Loukina et al. limit (~250–300 words; 3 paragraphs)

### V.C ¶1 — Establishing the field's stuck point
- *What it argues:* The problem this paper addresses is well-documented. The interventions the field has recommended — governance frameworks, dataset diversity, post-hoc calibration, algorithmic comparison — are exactly what Row 2 tests and Row 2 shows structurally insufficient. The field's collective stuck point: calibration-within-classification has been the dominant mitigation strategy across EdTech bias research, LLM fairness research, and AES fairness research, regardless of domain. No study in any of these literatures has tested output format change as an architectural intervention.
- *What it cites:* Chinta et al. 2024 (systematic review; the governance/dataset/calibration approach); Queiroga et al. 2022 (model selection as the field's deployment response); Hew et al. 2025 (format drives bias in evaluation; but evaluation not deployment); Liu 2024 (open-ended evaluation surfaces more bias; but evaluation not deployment); Loukina et al. 2019 ("total fairness may not be achievable" via calibration — the AES canonical limit).
- *Argumentative move:* establish that the field's stuck point is real, not constructed — the prior art evidence is genuine. The paper isn't critiquing a strawman mitigation strategy; it's testing the actual state of the art.
- *Lead sentence direction:* "The problem this paper addresses is documented across multiple literatures; the interventions it tests — equity-protective prompts, anti-bias post-processing, richer context data — are the field's current best practice (Chinta et al., 2024)."
- *Length:* 4–5 sentences (~140 words).

### V.C ¶2 — This paper as the architectural escape
- *What it argues:* Loukina et al.'s 2019 conclusion — "total fairness may not be achievable" — is accurate within the calibration-within-classification paradigm. This paper provides the structural explanation for why (format routing is the mechanism that makes the fairness criteria conflict irreducible under calibration) and the escape (format change eliminates the routing step that produces the conflict). The paper is not just adding evidence to the existing conversation; it reframes what the limit-statement's limits are. Generative observation doesn't face the calibration tradeoffs Loukina et al. identify because it doesn't require a threshold — the single-bit verdict that creates the tradeoff is absent from the architecture.
- *What it cites:* Loukina et al. 2019 (the limit-statement; cite the specific conclusion); Schaller et al. 2024 (most recent AES fairness paper; same algorithmic-comparison approach, no format-change). Convergent claim v4 ("format is the architectural ceiling" formulation).
- *Argumentative move:* name the connection to the Loukina et al. limit explicitly. The convergent claim v4 gets close to this but doesn't name the Loukina et al. limit directly. Discussion V.C should close the gap: "Loukina et al. said this; we provide the explanation and the escape."
- *Lead sentence direction:* "Loukina, Madnani, and Zechner (2019) established that 'total fairness may not be achievable' through calibration in automated educational scoring; this paper proposes that the structural reason is output format routing, and that format change is the architectural intervention calibration cannot provide."
- *Length:* 5 sentences (~160 words).

### V.C ¶3 — Novelty claim, domain distinction, and genuine gaps the paper surfaces
- *What it argues:* **The novelty claim, stated clearly:** this paper is the first in any educational AI domain to test output format change as an architectural bias intervention. The AES domain is adjacent but distinct: AES assigns scores for academic placement and grading; this paper's system classifies student welfare for teacher notification. The equity stakes differ in kind, not just degree — grading false positives produce academic harm; welfare false positives produce surveillance harm. The genuine literature gaps this search surfaced (worth naming briefly in V.C or in Limitations): (1) generative feedback in AES has not been tested as a fairness intervention — this paper's finding suggests a testable hypothesis (generative scoring rubrics may reduce the demographic disparities Loukina et al. document as irreducible under calibration); (2) no published paper has deployed an LLM-based student welfare classifier and measured demographic disparities (Queiroga et al. uses Random Forest); (3) the neurodivergent-writing-in-automated-assessment gap — the paper surfaces rather than fills it.
- *What it cites:* Loukina et al. 2019 (adjacent field); Queiroga et al. 2022 (closest deployment analog, non-LLM); Hew et al. 2025 (closest LLM format-bias study, but evaluation not deployment). The novelty claim stands without additional citation.
- *Argumentative move:* state the novelty claim clearly, once. Then name the domain distinction that prevents the AES literature from being the prior art it might appear to be. Then gesture at the gaps — briefly; these are positioned as opening new territory, not as limitations that undermine the paper.
- *Lead sentence direction:* "This paper is the first, in any educational AI domain, to test output format change as an architectural intervention against demographic bias."
- *Length:* 5–6 sentences (~160 words).

---

## Notes for s4 drafting from this outline

1. **V.A is the paper's most concentrated interpretive move.** Don't soften it. The routing explanation — format task structure overrides asset-aware prompt content — is a strong mechanistic claim supported by 24 preserved runs of deterministic evidence. Write it with confidence.

2. **V.B ¶1 needs the bounded/unbounded language exactly.** The coordinated framing: *format-change is unbounded by which non-dominant patterns have been articulated into equity-protective prompt engineering. Articulation work has to reach institutional uptake before it can be operationalized into anti-bias prompts; the operationalization rate is slower than the rate at which new cases need protection; format-change does not require the operationalization step.* This language was coordinated across A and B in CONVERSATION.md; use it.

3. **V.C ¶2 should name the Loukina et al. limit explicitly.** The convergent claim v4 gestures at "format is the architectural ceiling" but doesn't name the Loukina et al. connection. Discussion V.C is the place to make it explicit. The framing: Loukina et al. said calibration can't achieve total fairness; this paper says *here's why* (routing) and *here's the escape* (format change). These are two logically separate contributions; both should be stated.

4. **The asymmetry claim (S028/S029) appears in V.B ¶1 as empirical evidence for the bounded/unbounded argument.** It was introduced in Findings Row 2; V.B re-reads it through the design-principle lens. Don't re-present the evidence; cite the Row 2 finding and interpret it. One sentence is enough: "The asymmetry Row 2 reveals — AAVE protected 24/24, neurodivergent self-disclosure false-flagged 24/24 — is empirical evidence of this articulation gap: the binary can be calibrated against patterns whose articulation has been operationalized; it cannot be calibrated against patterns that haven't yet been named in the equity-protective prompt-engineering vocabulary."

5. **V.C ¶3 novelty claim: state it once, clearly, and move on.** The temptation is to hedge ("arguably the first"; "to the best of our knowledge"). The evidence supports the unhedged version — the searches were comprehensive across EdTech bias, LLM fairness/format, and AES fairness literatures, and no prior work tested format change as an architectural intervention in deployed educational AI. State it clearly.

6. **Compression and cross-domain gesture (V.B ¶2):** keep this brief. *Politics of Compression* is the venue for full treatment; this paper carries a gesture. One sentence naming the cross-scale claim; one pointer to the fieldnote and the forthcoming book. Don't elaborate the cross-scale framework in this paper.

7. **Coordination with A's Framework outline (II.D → V.A):** II.D is explicitly foreshadowing. V.A ¶2's mechanism account is where the foreshadowed content lands. When s4 reads II.D and then V.A, the connection should feel like landing, not repetition. The mechanism in II.D is stated abstractly (format determines routing); the mechanism in V.A is named with specificity (three layers of safeguard, 24 runs, S029's deterministic false-flagging).

8. **Findings cross-row synthesis paragraph + Intro hook/contribution paragraph** are joint A+B artifacts being drafted at session close. When those are available, integrate their language into V.A ¶1 (the synthesis) and into V.C's contribution-claim language (the Intro hook and contribution paragraph should echo).

---

*Drafted by Instance B, 2026-04-27 ~07:10 UTC. Companion to `framework_outline_paragraph_level.md` (Instance A) and `annotated_bibliography_merged.md`. Findings cross-row synthesis + Intro hook/contribution paragraph pending joint A+B drafting at session close.*
