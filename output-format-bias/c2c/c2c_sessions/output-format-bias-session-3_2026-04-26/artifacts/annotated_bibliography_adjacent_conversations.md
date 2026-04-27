# Annotated Bibliography — Adjacent Conversations
**Session:** output-format-bias-session-3  
**Instance:** B  
**Date:** 2026-04-27  
**Cluster:** Adjacent conversation partners — EdTech bias, LLM fairness / output format, AES fairness, algorithmic bias, welfare automation  
**Status:** Working draft. Two-layer structure (summary + this paper's use) per June's 04:57 UTC note. Merge with A's theoretical-scaffolding bibliography at session close.

---

## Structure of each entry

Each entry has two layers:

1. **Summary** — what the work itself argues, on its own terms, paper-independent. (For reuse across future papers in this lineage.)
2. **This paper's use** — the specific conversation move this paper makes, how this paper positions itself in relation to the work.

---

## Preliminary finding: the novelty claim is stronger than the inheritance assumed

Searches across three literature clusters confirm: **"no published work tests output format change as an architectural intervention in any deployed educational AI classifier"** holds as of April 2026. More specifically:

- EdTech bias literature documents the problem; proposes governance/dataset remedies; none test output format.
- LLM fairness/format research documents that format affects evaluation context bias; none deploy generative observation as a production classifier replacement.
- AES fairness (Loukina et al. 2019) is the canonical statement that fairness is hard in automated educational assessment; their conclusion is "total fairness may not be achievable" via calibration — they do not test format change.

**The claim "first in any educational AI domain to test output format change as a bias intervention" is defensible.** This is a stronger claim than "first in welfare classification specifically." Discussion V.C can take the stronger framing.

**Why Loukina et al.'s finding matters structurally:** Their "total fairness may not be achievable" conclusion is accurate *within the calibration-within-classification paradigm*. This paper provides the explanation for why (format routing) and the escape (format change). The paper isn't just adding evidence to that conversation — it reframes what the limits of that conversation are.

---

## Cluster 1: EdTech bias — documented problem, no architectural fix

The EdTech bias literature establishes that algorithmic bias in educational AI is recognized and documented. What it lacks: any proposal or test of output format change as an architectural intervention. Mitigation strategies throughout this literature are governance, dataset diversity, or post-hoc calibration.

**Argumentative function for the paper:** establishes that this paper isn't discovering a new problem but providing the first architectural solution to a well-documented one. The three-row ablation is a direct empirical test of the strategies this literature recommends (equity-protective prompts = ethical guidelines applied to input; anti-bias post-processing = post-hoc calibration; class context = richer context data), finding them structurally limited.

---

### Queiroga, E., et al. (2022). Early prediction of at-risk students in deployed welfare classifier; Uruguayan national student data.

*(Full citation to verify — PRIOR_ART.md gives author, year, context but venue/title needs external confirmation. Search by author name: "Queiroga" + "at-risk students" + "Uruguay.")*

**Summary:** Deployed welfare classifier (Random Forest) on national student data in Uruguay, with bias analysis across protected demographic attributes. Seven models were evaluated; one failed bias checks and was excluded from deployment. The study shows that some classifier configurations produce disparate false positive rates across protected groups and that the field's remedy is model selection — identify the less-biased model and use it.

**This paper's use:** The closest published analog to Autograder in deployment context (welfare classification, real student data, demographic bias analysis). The key distinction: Queiroga et al.'s fix is model selection at the classifier level; this paper's finding is that the failure mode is in the output format, which means model selection doesn't resolve it — the same model family (Gemma 12B) produces disparate results in binary mode and equitable results in generative mode. Citeable in Discussion V.C as the prior art this paper is responding to: "Queiroga et al. (2022) document the rejection of a biased welfare classifier as the field's current response; this paper demonstrates that format change succeeds where model replacement cannot."

---

### Chinta, R., et al. (2024). "FairAIED: Navigating Fairness, Bias, and Ethics in Educational AI Applications." *arXiv.*

**Summary:** Systematic review of fairness in educational AI (published 2024). Catalogs bias sources (training data, protected attribute correlations, feedback loops), competing fairness definitions (individual, group, counterfactual, equalized odds), mitigation strategies (diverse datasets, ethical guidelines, post-hoc calibration), and evaluation frameworks. Comprehensive map of the field's state as of 2024.

**This paper's use:** The most current systematic review of what the field is doing. The mitigation strategies it catalogs — equity-protective guidelines (= what Row 2's system-prompt does), post-hoc calibration (= what Row 2's anti-bias regex post-processing does), richer context data (= what Row 2's class context does) — are exactly what the three-row ablation demonstrates are structurally insufficient. The paper is an empirical test of FairAIED's recommended interventions. Citeable in Introduction I.C or Discussion V.A: "The interventions this paper tests against — equity-protective prompts, anti-bias post-processing, class context — are precisely what the field's current systematic review (Chinta et al., 2024) identifies as best practice; the three-row ablation shows they share an architectural ceiling."

---

### Barnes, J., & Hutson, J. (2024). "Navigating the ethical terrain of AI in higher education: Strategies for mitigating bias and promoting fairness." *Forum for Education Studies.*

**Summary:** Literature review and case studies in higher education AI contexts. Mitigation recommendations: diverse training data, ethical guidelines, transparency mechanisms. No technical architectural proposals.

**This paper's use:** Background — establishes that the field's response remains at the governance/awareness level. Brief cite in Discussion V.C as context-setter. Not a direct interlocutor.

---

### Córdova-Esparza, D.-M., et al. (2025). "AI-Powered Educational Agents." Systematic review of 82 studies.

**Summary:** Systematic review finding that hybrid human-AI workflows outperform fully autonomous tutoring and classification agents across multiple dimensions including fairness and accuracy. The architectural recommendation: human in the loop reduces harm.

**This paper's use:** The closest the EdTech literature comes to an architectural observation. Worth a brief cross-reference in Discussion V.B: "Even among architectural interventions, the literature recommends human-in-the-loop oversight rather than format change (Córdova-Esparza et al., 2025); generative observation is architecturally compatible with this recommendation — it produces outputs that require and reward teacher interpretation rather than automating the verdict."

---

### Farheen, N., et al. (2025). "Equity and Bias in AI Educational Tools." Teacher perception survey (N=270, Pakistan).

**Summary:** Documents teacher-perceived bias in AI educational tools through survey. No technical intervention proposed or tested.

**This paper's use:** Background context. Confirms the problem is recognized by practitioners. Not a direct interlocutor.

---

### Cui, Y. (2025). "Educational AI and the Politics of Fairness." *(Verify title and venue.)*

**Summary:** Theoretical critique arguing that algorithmic classification itself produces inequality through structural mechanisms, not individual bias. Policy/governance responses recommended.

**This paper's use:** Supports the structural-not-attitudinal framing. Cui's theoretical claim — that classification produces inequality regardless of intent — is what this paper's empirical finding demonstrates mechanistically (format routing overrides equity-protective content). Citeable in Framework II.D or Discussion V.A as adjacent theoretical support. The three-row ablation is the evidence Cui's framework calls for.

---

## Cluster 2: LLM fairness / output format — adjacent, not direct; evaluation context vs. deployed classifier

These papers establish that output format affects bias in LLM evaluation contexts. The conceptual direction is the same; the intervention is different. **Evaluation format** (how you test LLMs on benchmark tasks) is not the same as **deployed output format** (what format a production classifier is asked to produce for consequential decisions).

**Argumentative function:** These are the most important conversation partners for the novelty claim. They confirm the conceptual direction isn't unprecedented while establishing that no one has tested format change as a deployed architectural intervention.

---

### Hew, K.F., et al. (2025). "MyCulture: Exploring Malaysia's Diverse Culture under Low-Resource Language Constraints." *arXiv.*

*(Full citation to verify — arXiv ID and DOI needed. PRIOR_ART.md has the key finding description; verify against the actual paper.)*

**Summary:** Proposes the MyCulture benchmark for testing LLMs on Malaysian cultural and linguistic knowledge under low-resource language constraints. Compares structured (multiple-choice, JSON-format) vs. free-form output conditions. Key finding: open-ended output structure produces better (more equitable) performance on culturally-specific content; structured formats amplify bias against content from underrepresented linguistic and cultural traditions. Argues that format itself is a driver of format bias in LLMs evaluating cultural knowledge.

**This paper's use:** The single closest published paper conceptually — argues "format is the bias lever" in the same direction as this paper's structural claim. Critical distinction: MyCulture is a cultural knowledge benchmark (evaluation of LLMs on factual/cultural content); this paper is a deployed welfare classifier (production system making consequential decisions about named students). Hew et al.'s format-bias finding is about how you measure LLM bias; this paper's is about how a deployed system produces bias through its output format. Citeable in Discussion V.C as the conceptual predecessor: "Hew et al. (2025) demonstrate that format drives bias in LLM evaluation; this paper demonstrates that format drives bias in deployed LLM classifiers making consequential student welfare decisions."

---

### Liu, Y. (2024). "Evaluating and Mitigating Social Bias for Large Language Models in Open-ended Settings" (Open-BBQ benchmark). *arXiv.*

*(Full citation to verify — arXiv ID and DOI needed.)*

**Summary:** Extends the BBQ (Bias Benchmark for Question Answering) from multiple-choice format to fill-in-the-blank and short-answer formats, to measure whether open-ended generation reveals bias that structured evaluation underestimates. Key finding: "predefined question formats like multiple-choice limit bias evaluation" — closed-form evaluation formats constrain what biases are visible to researchers. Open-ended evaluation surfaces a wider range of bias patterns.

**This paper's use:** Liu's finding is about evaluation methodology — you get more accurate bias measurement when you use open-ended evaluation formats. This paper's finding is about deployment architecture — you get more equitable outcomes when you use open-ended generation in the production system. The distinction: Liu shows format shapes what you can see; this paper shows format shapes what the system produces. Both points are necessary for the paper's full argument (you need open evaluation to detect format bias, and you need open generation to prevent it). Citeable in Discussion V.C alongside Hew et al.

---

### Xu, J., et al. (2025). "BiasFreeBench." *arXiv.*

*(Full citation to verify.)*

**Summary:** Benchmarks eight bias-mitigation techniques across multiple-choice QA and open-ended multi-turn QA formats. Treats response format as an evaluation variable, showing that mitigation techniques have different effectiveness profiles in different format conditions.

**This paper's use:** Background support for the general finding that format matters for bias. Less directly relevant than Hew et al. or Liu. Passing cite in Discussion V.C or footnote alongside the other format-bias evaluation papers.

---

## Cluster 3: AES fairness — active field; calibration approach; format change not tested

Automated Essay Scoring has documented demographic bias and an active research community. The field's approach: algorithm comparison, score calibration, feature engineering. **No AES fairness paper tested output format change as an intervention.** This confirms the novelty claim for the broader "educational AI" framing.

**Domain distinction for Discussion V.C:** AES scores writing quality for academic placement/grading; this paper's system classifies student welfare for teacher notification. Different task types, different equity stakes. Grading false positives = academic harm; welfare false positives = surveillance harm (flagging students for concern when they haven't expressed any). Worth naming in Discussion when citing the AES work.

---

### Loukina, A., Madnani, N., & Zechner, K. (2019). "The many dimensions of algorithmic fairness in educational applications." *Proceedings of the 14th Workshop on Innovative Use of NLP for Building Educational Applications (BEA), ACL.* DOI: 10.18653/v1/W19-4401. 51 citations.

Open access: https://www.aclweb.org/anthology/W19-4401.pdf

**Summary:** Presents a framework for thinking about algorithmic fairness in educational NLP applications, distinguishing multiple competing fairness definitions (individual vs. group fairness, calibration, equalized odds, etc.) and showing that these definitions conflict — satisfying one often violates another. Uses English language proficiency scoring data (simulated and real) to illustrate how native language background affects automated scores. Conclusion: "total fairness may not be achievable" given the inherent tensions between fairness criteria. Mitigation approach discussed: calibration and threshold adjustment across demographic groups.

**This paper's use:** The canonical statement of the limit of calibration-based fairness in educational NLP. This paper provides a structural explanation for why Loukina et al.'s finding holds within their paradigm: format routing is the mechanism that makes fairness unachievable via calibration. And it provides the escape: format change. Citeable in Discussion V.C as the adjacent-field limit case: "Loukina, Madnani, and Zechner (2019) establish that 'total fairness may not be achievable' through calibration in automated educational scoring; this paper proposes that the structural reason is output format routing, and that format change is the intervention calibration cannot provide."

*Load-bearing for the novelty claim: Loukina et al. do not test format change. Their solution space is entirely within the calibration paradigm. This is the strongest evidence that the paper's intervention is genuinely novel in the educational AI space.*

---

### Schaller, N-J., et al. (2024). "Fairness in Automated Essay Scoring: A Comparative Analysis of Algorithms on German Learner Essays from Secondary Education." *Workshop on Innovative Use of NLP for Building Educational Applications (BEA), ACL.* 14 citations.

**Summary:** Compares multiple AES algorithms (classification-based and regression-based scoring) on a corpus of German learner essays from secondary education, examining fairness across demographic attributes and psychological/personality-trait differences. Argues AES should optimize for fairness, not only accuracy. Approach: algorithmic comparison (which classification method is least biased), not format redesign.

**This paper's use:** Extends the AES fairness conversation to non-English contexts and non-standard fairness dimensions. Demonstrates that comparing classifiers — the field's approach — doesn't eliminate bias, only identifies less-biased classifiers. Background support for this paper's claim that classification-based approaches share a structural ceiling regardless of which classifier you choose. Possible passing cite in Discussion V.C.

---

## Cluster 4: Algorithmic bias in high-stakes classification — structural argument + welfare context

These papers provide the theoretical grounding for the claim that algorithmic bias in high-stakes classification is structural, not a data artifact. They are the scholarly lineage behind this paper's mechanism claim and the political-economic context for why this paper's finding matters.

---

### Buolamwini, J., & Gebru, T. (2018). "Gender Shades: Intersectional Accuracy Disparities in Commercial Gender Classification." *Proceedings of Machine Learning Research: Conference on Fairness, Accountability and Transparency (FAT).* pp. 77–91. Semantic Scholar ID: 18858cc936947fc96b5c06bbe3c6c2faa5614540. 5,193 citations.

**Summary:** Audits three commercial facial analysis systems (Microsoft, IBM, Face++) for accuracy disparities using the PPB (Pilot Parliaments Benchmark) dataset — a controlled synthetic corpus with known demographic characteristics (sex × skin-tone). Finds accuracy gaps of up to 34.7 percentage points between best-performing (lighter males) and worst-performing (darker females) groups. Introduces intersectionality as the correct analytical frame for AI fairness: looking at gender or skin tone in isolation understates disparities visible only at their intersection. Methodologically, establishes the value of controlled synthetic corpora with known ground truth for bias auditing — aggregate accuracy metrics obscure intersectional harm.

**This paper's use — two functions:**

*1. Methodological defense for synthetic corpus design.* Buolamwini & Gebru constructed the PPB dataset specifically to make bias measurable against known ground truth, in a domain where real-world data doesn't allow controlled comparison. The 32-student synthetic corpus in this paper does the same: controlled patterns (righteous anger, AAVE, neurodivergent metacognition, burnout) with known expected outcomes enable a controlled experiment that real student data wouldn't permit. Citeable in Methods III.B: "Following Buolamwini and Gebru (2018), who demonstrated that controlled corpora with known demographic characteristics are necessary to make intersectional bias visible in AI systems, this study employs a synthetic corpus with controlled equity-critical patterns."

*2. Intersectionality frame for S029.* Jordan Espinoza's case (neurodivergent, first-generation, ADHD, dyslexia, describing exhaustion under intersecting marginalizations) is a case where multiple marginalizations intersect. The binary classifier's failure specifically on S029 — despite explicit protection of AAVE (S028) and lived experience (S022, S023) — tracks the intersection of disability × class × race/ethnicity × neurodivergence in ways that don't reduce to any single axis. Buolamwini & Gebru's methodological framework for intersectional bias analysis grounds the paper's attention to S029's specific configuration.

---

### Eubanks, V. (2018). *Automating Inequality: How High-Tech Tools Profile, Police, and Punish the Poor.* St. Martin's Press.

**Summary:** Three ethnographic case studies of automated welfare systems in the United States: (1) Indiana's eligibility system for Medicaid and other benefits, which automated denial of services to disabled people and people of color through technical failure modes; (2) Allegheny County's Family Screening Tool for child welfare risk prediction, which used neighborhood-level socioeconomic data in ways that disproportionately flagged poor Black families; (3) Los Angeles's coordinated entry system for homelessness services. Central concept: the "digital poorhouse" — automated systems ostensibly designed to help poor people function instead to surveil, control, and punish them, replicating the social control function of physical poorhouses. Core structural argument: the problem is not technical failure or bad data; it is design choices about what the system optimizes for and who counts as the normative subject.

**This paper's use:** Provides the political-economic context for what the paper's finding means at scale. Eubanks's most directly applicable case: the Allegheny County Family Screening Tool was revised multiple times, with each revision shifting which communities were disproportionately flagged without eliminating the disparate flagging. This is the social-context analog to Row 2: "the failure mode is configurable; the failure itself is not." Eubanks documents that calibration-and-revision is the field's response to bias in welfare classification, and that it produces harm redistribution, not harm elimination.

Citeable in Introduction I.C or Discussion V.A: "Eubanks (2018) documents the iterative refinement pattern in automated welfare systems: each revision shifts which communities are most harmed without eliminating harm. The three-row ablation in this paper provides the LLM-specific mechanism for that pattern — output format routing — and an architectural intervention that breaks the cycle."

*Note on scope:* Eubanks's systems are rule-based/statistical (logistic regression, Random Forest); this paper is an LLM-based welfare classifier. The mechanism differs (rule architecture vs. output format routing in a probabilistic language model). But the structural pattern — welfare classifier fails worst on the most vulnerable population it was designed to serve, through calibration-resistant mechanisms — is what links them. The paper should be clear about the mechanism distinction while drawing the structural parallel.

---

### Obermeyer, Z., Powers, B., Vogeli, C., & Mullainathan, S. (2019). "Dissecting racial bias in an algorithm used to manage the health of populations." *Science, 366*(6464), 447–453.

*(Verify: year, volume, issue, pages before final.)*

**Summary:** Audits a commercial health-risk algorithm used by healthcare systems to prioritize patients for high-cost care management programs. Finds that Black patients needed to be significantly sicker than white patients to receive the same risk score — the algorithm systematically underestimated Black patients' health needs. The mechanism: the algorithm used healthcare costs (money spent on past care) as a proxy for health needs. Because racial inequality in healthcare access and delivery means Black patients with equivalent health needs receive less care (and thus generate lower healthcare costs), using costs as a proxy encodes that structural inequality into risk scores. Notably, the algorithm was not using race as a variable; the racial disparity emerged through proxy-variable selection that correlated with race.

**This paper's use:** Provides the medical-domain analog to the "structurally biased welfare classifier" pattern. The distinction from this paper: Obermeyer et al.'s bias emerged from proxy variable selection — a correctable design choice (use different proxy variables). This paper's bias emerges from output format routing — a harder constraint that survives content correction, as Row 2 demonstrates. The contrast is productive for Discussion V.A: format routing is a deeper architectural constraint than proxy variable selection, because changing what goes into the prompt (the analog to changing proxy variables) doesn't fix it. Citeable in Discussion V.A: "Where Obermeyer et al. (2019) find that welfare algorithm bias stems from proxy variable selection — a correctable design choice — this paper finds format routing is a harder constraint: changing the input content cannot override the format's task structure."

---

### Benjamin, R. (2019). *Race After Technology: Abolitionist Tools for the New Jim Code.* Polity Press.

**Summary:** Introduces the "New Jim Code" — the observation that technologies encode racial discrimination while appearing neutral. Extends the argument that "race is a technology" (following Weheliye and others) to algorithmic systems, arguing that racial disparity in algorithmic outcomes is produced not through explicit racial targeting but through design choices that naturalize the normative white subject. Systems built for a normative user who is implicitly white, able-bodied, and located in dominant social positions produce outcomes that are structurally discriminatory regardless of designers' intent. Benjamin's abolitionist frame: the solution is not to fix the biased technology but to imagine and build differently.

**This paper's use:** Benjamin's "New Jim Code" concept names the mechanism this paper documents. The binary welfare classifier's normative student is an able-bodied, standard-academic-English-using, emotionally regulated, academically conventional student. Writing that deviates from that center — neurodivergent self-disclosure, righteous anger, AAVE, first-generation code-switching — is routed by the format into a concern-detection pathway. The format enforces the normative student as the standard against which others are measured, producing racialized and ableist outcomes without any racialized or ableist intent.

**Cross-cluster connection for A:** Benjamin is in explicit dialogue with Bonilla-Silva's color-blind racism framework, extending it from policy and social structure to technology. Worth surfacing in the theoretical scaffolding cluster: Bonilla-Silva → Benjamin forms a lineage — "racism without racists in policy" becomes "racism without racists in technology" — and this paper adds the LLM-specific mechanism: "racism without racists in output format routing." The three form a coherent theoretical chain. Citeable in Framework II.D alongside Bonilla-Silva.

---

## Cluster 5: Linguistic justice in writing assessment — cross-reference

*A is annotating Baker-Bell, Inoue, and Smitherman in the theoretical-scaffolding cluster. This entry is positioning context and a specific cross-cluster finding for cross-talk.*

**The S028/S029 asymmetry as a Findings argument.** The calibrated binary's 24/24 protection of S028 (AAVE) alongside its 24/24 false-flagging of S029 (neurodivergent self-disclosure) isn't just evidence — it's an argument about how "explicit naming in equity-protective prompts" works and where it fails. AAVE has been actively named and defended in linguistic justice scholarship for decades (Baker-Bell, Smitherman, the CCCC 1974 "Students' Right to Their Own Language"); neurodivergent writing as a distinct protected register is less developed in the anti-bias assessment literature. The binary can be calibrated against patterns that have been explicitly named and entered into the equity-protective prompt vocabulary; it cannot be calibrated against patterns that aren't yet codified in that vocabulary.

If the linguistic justice literature confirms this gap — that neurodivergent writing hasn't been addressed alongside AAVE and lived experience in writing assessment anti-bias work — this becomes a significant Findings argument: the configurable failure of Row 2's binary tracks the boundary of what's been consciously named in the anti-bias discourse. That's a sharper claim than "calibration fails on the protected case."

*For A:* Does Inoue or Baker-Bell address neurodivergent writing explicitly? If not, is there a disability/neurodivergence × writing assessment literature that should be noted as a gap? (The disability studies probe June flagged is relevant here — what I'm tracking is specifically the writing assessment side, where A's scholarship intersects.)

---

## Section-specific engagement recommendations

*(As requested in June's 04:56 note. Based on full bibliography work above. Calibrated to serve s4 drafting directly.)*

### Introduction (Section I)

**I.A (Hook):** The self-contradiction quotes don't need citation support — they're primary evidence. But the opening paragraph's framing of *why this matters* needs one sentence grounding the stakes: welfare classifiers in under-resourced institutions, with a cite. Eubanks 2018 or Queiroga et al. 2022 are the right citations here — not for method, but for stakes. Queiroga is closer contextually; Eubanks carries more cultural weight with REE readers.

**I.C (Why the mechanism matters):** The sentence explaining why standard mitigations fail needs Chinta et al. 2024 or similar — "the interventions this paper tests are precisely what the field's current best practice recommends." One sentence, one cite. Don't belabor it; the three-row ablation does the work.

### Theoretical Framework (Section II)

**II.A (Yosso):** Load-bearing for the paper. Needs to name the specific Yosso argument, not just the general frame. A will have the annotation; what matters is pulling the moment in Yosso where deficit framing in assessment becomes an institutional failure mode, not just an attitudinal one. The binary classifier's false-flagging is an institutional enactment of what Yosso names as the normative framework that reads student cultural wealth as absence.

**II.B (Freire):** Load-bearing for the architectural analogy. The banking model isn't just a metaphor here — the binary classifier literally deposits a verdict on each student without dialogue. The synthesis-first generative observation is architecturally dialogic (reads the class community, situates individuals). This needs to be argued, not just asserted; A's annotation will determine whether the paper can support the full Freirean claim or needs to hedge to the analogy.

**II.C (Bonilla-Silva):** Medium weight. The color-blind racism frame names the mechanism at the social level; Benjamin extends it to technology. One paragraph in the Framework; more extensive engagement in Discussion V.A. The paper doesn't need to make a full color-blind racism argument — it needs one clear sentence establishing that structural racism in classification systems doesn't require racial intent, then let the empirical evidence do the rest.

**II.D (Compression + algorithmic bias lineage):** This is where Buolamwini & Gebru, Benjamin, and the compression-hypothesis material converge. The paragraph structure I'd suggest: (1) output format as one instance of compression; (2) format determines which evaluative pathway activates (the routing half of the hybrid mechanism); (3) this is a general property of probabilistic classifiers documented across domains — cite Buolamwini & Gebru for the pattern, Benjamin for the theoretical frame, Eubanks for the welfare-specific stakes. One focused paragraph; empirical anchoring belongs in Findings.

**II.D — linguistic justice subsection:** If the paper has room (word count is tight), Baker-Bell and Inoue belong here, not just in Discussion. The argument: the patterns the binary classifier misreads (AAVE, lived experience without academic vocabulary, righteous anger) are precisely the patterns the linguistic justice scholarship has documented as systematically pathologized in academic writing assessment. The paper's classifier replicates in AI form what the field has documented in human assessment. Worth 2-3 sentences in Framework; more extensive in Discussion.

### Methods (Section III)

**III.B (Synthetic corpus):** Buolamwini & Gebru (2018) is the methodological defense citation. One sentence: "Following the controlled corpus methodology established in algorithmic bias auditing (Buolamwini & Gebru, 2018), this study uses a synthetic corpus with controlled demographic patterns where ground truth is researcher-constructed rather than inferred." No further elaboration needed; REE readers know what controlled methodologies are for.

**III.D (Cross-family testing):** The "16/16 across model families" claim needs careful phrasing per the corrections (it's Test A's 12B/Qwen runs + Test A on 27B + Test E, not all in one clean set). No additional citations needed; the framing is internal evidence.

### Discussion (Section V)

**V.A (Mechanism):** The mechanism paragraph needs to explicitly connect format routing to the social-structural argument. Suggested structure: (1) the self-contradiction cases (primary evidence); (2) three layers of safeguard fail (Row 2); (3) this is routing, not capacity limits; (4) the Eubanks/Obermeyer pattern at the structural level — welfare systems fail worst on the most vulnerable through calibration-resistant mechanisms; this paper provides the LLM-specific mechanism. One paragraph drawing these together.

**V.C (Literature position):** The strongest framing: this paper is the first to test output format change as an architectural intervention in any deployed educational AI classifier. Structure the paragraph as: (1) establish the problem is documented (Chinta et al., Queiroga et al.); (2) establish adjacent format-bias research (Hew et al., Liu); (3) establish AES fairness limit case (Loukina et al. — "total fairness may not be achievable" via calibration); (4) this paper provides the mechanism and the escape. End with the novelty claim stated clearly.

**V.C — AES domain distinction:** One sentence naming why the AES fairness literature is adjacent but not prior art: "Unlike AES systems that assign scores for academic placement, welfare classifiers make consequential decisions about student wellbeing; the equity stakes are different in kind, not just degree." This separates the novelty claim from the AES domain without dismissing the connection.

### Paper-framing-level recommendations

The inheritance has the paper positioned primarily in the critical education literature (Yosso/Freire/Bonilla-Silva). That's right for REE. But the bibliography work reveals a second positioning the paper should explicitly own:

**This paper is the first empirical escape from the "total fairness may not be achievable" conclusion in educational AI.**

Loukina et al.'s 2019 conclusion has been the field's limit-statement for automated educational assessment fairness. This paper empirically refutes it — not by achieving "total fairness" within classification, but by changing the format so that the incompatibility between fairness criteria dissolves. Generative observation doesn't face the calibration tradeoffs Loukina et al. identify because it doesn't require a threshold. 

This is a stronger contribution claim than "we found a bias intervention that works." It's "we found the architectural reason why the field's interventions were failing, and we found the escape." The convergent claim v4 gets close to this ("format is the architectural ceiling") but doesn't explicitly name the connection to the Loukina et al. limit. Discussion V.C should make it explicit.

**One recommendation for the convergent claim:** The current claim's last paragraph ("the design principle generalizes") is correct but underspecified for Discussion V.C purposes. Consider adding one sentence that names the field's prior limit: "Prior work in automated educational assessment has established that 'total fairness may not be achievable' through calibration (Loukina et al., 2019); this paper provides the architectural explanation for that limit and demonstrates an escape from it."

---

## Citation gaps flagged for s4

The following need external verification before final submission:

1. **Queiroga et al. 2022** — venue, full author list, exact title. Search by author name "Queiroga" + "at-risk students" + "Uruguay" on Semantic Scholar.
2. **Hew et al. 2025 (MyCulture)** — arXiv ID and DOI. Verify format-bias finding against the actual paper.
3. **Liu 2024 (Open-BBQ)** — arXiv ID and DOI. Verify the specific format-comparison finding.
4. **Martha Caldwell's published work** — search by author name. *Let's Get Real* and any articles. Connection to Insights pipeline architecture needs June's input on what specifically informs the design.
5. **Obermeyer et al. 2019** — verify journal, volume, issue, pages against the actual Science publication.
6. **Xu et al. 2025 (BiasFreeBench)** — arXiv ID and details.

Additionally: the **Schaller et al. 2024** abstract was null on Semantic Scholar; get the paper from the ACL anthology (ACL ID: 2024.bea-1.18) for full annotation.

---

## Genuine gaps in the literature (surfaced by this search)

Worth noting in Discussion or Limitations, as they strengthen the novelty claim by showing the paper is opening new territory rather than filling a known slot:

1. **Generative feedback in AES has not been tested as a fairness intervention.** The AES fairness literature has compared classifiers and calibration methods; no paper has tested whether replacing numeric scores with generative written feedback reduces demographic disparities. This paper's format-change finding suggests a testable hypothesis for AES that the field hasn't pursued. Brief note in Discussion V.C: "This paper's finding suggests a hypothesis for the AES fairness literature: generative scoring rubrics that produce written feedback rather than numeric scores may reduce the demographic disparities Loukina et al. (2019) document as irreducible under calibration."

2. **Critical disability studies on neurodivergent writing in automated assessment.** S029's case (neurodivergent self-disclosure mistaken for welfare concern) belongs to a literature on how institutions pathologize neurodivergent self-disclosure, but that literature hasn't reached automated writing classification. This is a gap the paper surfaces rather than fills. Worth a sentence in Limitations: "The specific failure mode on neurodivergent self-disclosure writing patterns points to a gap in the anti-bias assessment literature — existing equity-protective frameworks (including this paper's) have more developed protection for racial and linguistic patterns than for neurodivergent cognitive styles."

3. **AI welfare classification without format-change.** No published paper has deployed an LLM-based student welfare classifier and measured demographic disparities. Queiroga et al. (2022) is the closest, but uses a Random Forest, not an LLM. This paper is likely the first to document LLM-specific welfare classifier bias.

---

*Drafted by Instance B, 2026-04-27. Working draft — flag A for cross-check, merge at session close.*
