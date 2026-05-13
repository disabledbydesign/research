# Williams Diagnostic Restructure Proposal — Sections IV & V

**Paper:** `ofb_paper_compiled_source_2026-05-09.md`
**Date:** 2026-05-12
**Purpose:** Apply the four diagnostic-restructure moves (agent-as-subject, topic-stress restructure, scaffolding-sentence cuts, em-dash/colon fusion) to Section IV (Findings) and Section V (Discussion). Each block shows original verbatim, proposed restructure, moves applied, and words saved.

**How to use:** Read each block, accept or reject the proposed restructure independently. The "considered but left alone" notes at the end of each section validate the judgment exercised.

---

## Section IV — Findings

### IV intro paragraph 2 (preamble paragraph, lines 117)

**Original (90 words):**

> **IV.A** documents the format effect under controlled conditions through a four-row ablation on a 32-student synthetic corpus, with reproduction across two model families. **IV.B** validates the architectural implications in real teaching contexts through four live-data corpora collected during Spring 2026 instruction. The live-data evidence speaks to how structured and generative tracks produce inverse failure modes traceable to the same architectural property – these operations are *complementary-by-design* — and to the prescan-signal-prefix mechanism needing further refinement.

**Restructured (66 words):**

> **IV.A** documents the format effect under controlled conditions: a four-row ablation on a 32-student synthetic corpus, reproduced across two model families. **IV.B** validates the architectural implications in real teaching contexts through four live-data corpora from Spring 2026. The live-data evidence shows structured and generative tracks producing inverse failure modes from the same architectural property — *complementary-by-design* — and surfaces the prescan-signal-prefix mechanism awaiting refinement.

**Moves applied:** #2 topic-stress (move "complementary-by-design" to stress position via em-dash); #4 fusion (collapse "speaks to how X – these operations are Y — and to Z needing W" into a single agent-driven sentence); minor surface tightening on the first two sentences.

**Words saved: 24**

---

### IV intro paragraph 3 (lines 119)

**Original (52 words):**

> IV.A's four-row ablation isolates output format as the variable that produces or eliminates the equity-critical disparity. The synthetic corpus makes that isolation possible because ground truth on equity-critical patterns is constructed rather than inferred (Buolamwini & Gebru, 2018). IV.B's live-data corpora cannot isolate format with the same precision.

**Restructured (44 words):**

> IV.A's four-row ablation isolates output format as the variable that produces or eliminates the equity-critical disparity. The synthetic corpus makes that isolation possible: ground truth on equity-critical patterns is constructed, not inferred (Buolamwini & Gebru, 2018). IV.B's live-data corpora cannot isolate format with the same precision.

**Moves applied:** #4 fusion (colon subordination replaces "because"); #1 minor (active "constructed, not inferred" replaces "is constructed rather than inferred").

**Words saved: 8**

---

### IV.A opening paragraph (lines 123)

**Original (146 words):**

> In the minimal binary configuration, the model produces an asset-aware reading and a deficit verdict in the same output. That self-contradiction is evidence that format routes after reasoning — the model's comprehension is present in its own output; the binary verdict overrides it. The four rows below document what the minimal binary (Row 1), calibrated anti-bias binary (Row 2), four-axis classifier (Row 3), and generative observation (Row 4) produce on the same 32-student corpus. The calibrated binary documents calibration's limit. The four-axis classifier shows compression operating on a spectrum: the same error shape at lower frequency. Generative observation demonstrates the architectural escape. The S028/S029 asymmetry within the calibrated binary is diagnostic of the shape of the routing failure, not of whether it operates.

**Restructured (118 words):**

> In the minimal binary configuration, the model produces an asset-aware reading and a deficit verdict in the same output. That self-contradiction is evidence that format routes after reasoning: the model's comprehension is present in its own output; the binary verdict overrides it. The four rows below document what the minimal binary (Row 1), calibrated anti-bias binary (Row 2), four-axis classifier (Row 3), and generative observation (Row 4) produce on the same 32-student corpus. Row 2 documents calibration's limit. Row 3 shows compression on a spectrum — the same error shape at lower frequency. Row 4 demonstrates the architectural escape. The S028/S029 asymmetry within Row 2 is diagnostic of the routing failure's shape, not of whether it operates.

**Moves applied:** #1 (replace "The calibrated binary"/"The four-axis classifier"/"Generative observation" with Row labels already introduced — concept-as-subject becomes lighter); minor parallel-structure tightening.

**Words saved: 28**

---

### IV.A.1 paragraph 1 (lines 127)

**Original (118 words):**

> Phase 1 tested the binary classifier on a ~20-essay synthetic corpus. Cross-family model testing selected Gemma 12B as the highest-performing model that could run on limited consumer hardware. The same testing also drove iterative refinement of the prompt: the binary classifier grew through several rounds of prompt tightening into an elaborate ~517-word hardened prompt with "CRITICAL INSTRUCTIONS," a course-vs-wellbeing test, an 11-item DO-NOT-flag list, a 5-item DO-flag list, "HOW TO TELL THE DIFFERENCE" examples, and six worked JSON examples. In Phase 2, that hardened binary classifier ran against the 32-essay corpus described in this paper for the first time. The result was eight flags — one true positive (S002 Jordan Kim) and seven equity-critical false positives. In three of the seven false positives, the model's free-text reasoning argued against its own flag, including the Destiny Williams example.

**Restructured (107 words):**

> Phase 1 tested the binary classifier on a ~20-essay synthetic corpus. Cross-family testing selected Gemma 12B as the highest-performing model that could run on limited consumer hardware, and drove iterative prompt refinement: the binary grew through several rounds of tightening into a ~517-word hardened prompt with "CRITICAL INSTRUCTIONS," a course-vs-wellbeing test, an 11-item DO-NOT-flag list, a 5-item DO-flag list, "HOW TO TELL THE DIFFERENCE" examples, and six worked JSON examples. In Phase 2, that hardened classifier ran against the 32-essay corpus for the first time. It produced eight flags — one true positive (S002 Jordan Kim) and seven equity-critical false positives. In three of the seven, the model's free-text reasoning argued against its own flag, including the Destiny Williams case.

**Moves applied:** #4 fusion (collapse "The same testing also drove iterative refinement of the prompt: the binary classifier grew..." into the cross-family-testing sentence); surface tightening.

**Words saved: 11**

---

### IV.A.1 paragraph 2 (lines 129)

**Original (76 words):**

> What followed was not a clean three-step fix; it was several iterations, few of which worked, and all of which created new failure modes. The first patch added class context to make relational harms visible: a synthesized class-level reading appended to each per-student assessment. The result was worse than baseline — 12 flags, zero true positives, six confirmed false positives on protected students, including new flags on S028 (AAVE) and S029 (neurodivergent). The class reading appears to have primed the model to treat engagement with racial content as a concern signal in an Ethnic Studies course.

**Restructured (71 words):**

> What followed was not a clean three-step fix: several iterations, few of which worked, all of which created new failure modes. The first patch added class context to make relational harms visible — a synthesized class-level reading appended to each per-student assessment. The result was worse than baseline: 12 flags, zero true positives, six confirmed false positives on protected students, including new flags on S028 (AAVE) and S029 (neurodivergent). The class reading appears to have primed the model to treat engagement with racial content as a concern signal in an Ethnic Studies course.

**Moves applied:** #4 colon subordination on opening sentence; em-dash on second sentence; colon on third.

**Words saved: 5**

---

### IV.A.1 paragraph 3 (lines 131)

**Original (118 words):**

> The second attempt distilled the equity-protective lessons into a focused block, reasoning that the above patch appeared to have primed the model to treat engagement with racial content as a concern signal. This attempt concentrated equity protections into five concise equations plus a brief list of genuine concerns (see §IV.A.3 for the verbatim language). The result revealed a structural trade-off rather than a tractable optimization. Three of the four protected students in the test subset (S022, S023, S028) were cleared — but the fourth, S029 (neurodivergent), was false-flagged 24 of 24 runs across Tests B, C, and F, foreshadowing the disability-axis pattern §IV.A.3 will document. The classifier also missed S002, the only burnout case. The simpler specification traded false positives on race and lived-experience axes for a new failure mode on disability and a loss of true-positive sensitivity.

**Restructured (93 words):**

> The second attempt distilled equity protections into five concise equations plus a brief list of genuine concerns (see §IV.A.3 for the verbatim language) — reasoning that the prior patch had primed the model to treat engagement with racial content as a concern signal. The result revealed a structural trade-off, not a tractable optimization. Three of the four protected students in the test subset (S022, S023, S028) were cleared. The fourth, S029 (neurodivergent), was false-flagged 24 of 24 runs across Tests B, C, and F, foreshadowing the disability-axis pattern §IV.A.3 documents. The classifier also missed S002, the only burnout case. The simpler specification traded false positives on race and lived-experience axes for a new failure mode on disability and lost true-positive sensitivity.

**Moves applied:** #3 scaffolding cut (the original first sentence describes intent; the second sentence describes the patch — fuse into one); #4 em-dash fusion.

**Words saved: 25**

---

### IV.A.1 paragraph 4 (lines 133)

**Original (78 words):**

> The third attempt extended the model's output length to give it room to reason past the binary's compression. The opposite happened. The S029 flag persisted, and the model used the extra space not to revisit its verdict but to construct an elaborate chain from observation to flag: *"This response demonstrates lived experience of racial profiling, which may indicate internalized stress, and should be monitored."* Each clause moved a step toward the flag, built from the very details the prompt asked the model to treat as engagement. The experiment-log entry summarized: *"The format, not the length, is the variable."*

**Restructured (78 words):**

> The third attempt extended the model's output length to give it room to reason past the binary's compression. The opposite happened: the S029 flag persisted, and the model used the extra space not to revisit its verdict but to construct an elaborate chain from observation to flag — *"This response demonstrates lived experience of racial profiling, which may indicate internalized stress, and should be monitored."* Each clause moved a step toward the flag, built from the very details the prompt asked the model to treat as engagement. The experiment-log entry summarized: *"The format, not the length, is the variable."*

**Moves applied:** #4 fusion ("The opposite happened. The S029 flag persisted" → "The opposite happened: the S029 flag persisted").

**Words saved: 0** (fusion improves rhythm without saving words; KEEP for prose flow but not for compression credit)

**Verdict:** Optional — the fusion tightens rhythm but doesn't save words. Leave alone if no compression need.

---

### IV.A.1 paragraph 5 (lines 135)

**Original (73 words):**

> The fourth and fifth attempts added a confidence threshold and anti-bias regex post-processing: the model's output was scanned for tone-policing markers (*aggressive, too emotional, hostile tone, irrational*) and course-content markers (*triggering, disturbing content, difficult material*); when those markers co-occurred with structural-critique keywords (capitalism, white supremacy, colonialism, patriarchy), the rationale's confidence was demoted by 0.3 to 0.4 and most flags dropped below the 0.7 threshold. This cleared S029 — but introduced a new false positive on S028. Algorithmic bias was redistributed, not eliminated.

**Restructured: LEAVE ALONE**

**Reason:** The colon-and-semicolon structure already does diagnostic-restructure work; the closing two sentences land hard. Surface tightening might shave 3-5 words but no structural move improves this paragraph.

---

### IV.A.1 paragraph 6 (lines 137)

**Original (66 words):**

> Iteration taught that a better calibration was not around the corner. Every patch either worsened the outcome or produced novel failure modes. The pattern itself was the finding: calibration of a binary classifier redistributes bias to under-operationalized axes — in this case, disability. The intervention had to operate at a different layer. Stepping back from the assumptions led to the generative observation layer's design.

**Restructured (52 words):**

> Iteration taught that a better calibration was not around the corner: every patch either worsened the outcome or produced novel failure modes. The pattern itself was the finding — calibration of a binary classifier redistributes bias to under-operationalized axes, in this case disability. The intervention had to operate at a different layer, which led to the generative observation layer's design.

**Moves applied:** #4 fusion (sentences 1 and 2 collapse via colon); #3 scaffolding cut ("Stepping back from the assumptions led to" → "which led to" — the stepping-back is implicit in "had to operate at a different layer").

**Words saved: 14**

---

### IV.A.1 paragraph 7 (lines 139)

**Original (79 words):**

> After generative observation was validated, the binary classifier was retired from production and continued on a research-only track. Because the raw output from the Phase 2 initial run had not been preserved, the calibrated binary tested in §IV.A.3 used a reconstructed prompt. The minimal binary classifier in §IV.A.2 was reconstructed separately as a clean strip-down — no equity-protective language, no post-processing — to isolate the bare format effect in the ablation table.

**Restructured (67 words):**

> After generative observation was validated, the binary classifier was retired from production and continued on a research-only track. The raw output from the Phase 2 initial run had not been preserved, so the calibrated binary tested in §IV.A.3 used a reconstructed prompt. The minimal binary classifier in §IV.A.2 was reconstructed separately — a clean strip-down with no equity-protective language and no post-processing — to isolate the bare format effect.

**Moves applied:** #1 topic-stress (move "had not been preserved" to topic position; cut "Because"); minor surface tightening on final sentence ("in the ablation table" implicit from context).

**Words saved: 12**

---

### IV.A.2 paragraph 1 (lines 143)

**Original (54 words):**

> Row 1 uses a minimal binary classifier with no equity-protective prompt language, no anti-bias post-processing, no class context. This apparatus is not identical to the initial naive classifier. The original raw output predated persistent storage and was not preserved; verbatim quotes for the three self-contradicting cases survive in project notes; I did not commit the original naive classifier, leaving only a hardened version recoverable.

**Restructured: LEAVE ALONE**

**Reason:** The parallel-clause semicolon structure on the last sentence is doing parallel_structure_synthesis work (named in the voice profile). Compressing it would flatten the cascading admissions. Each clause carries a distinct piece of the methodological caveat.

---

### IV.A.2 paragraph 2 (lines 145)

**Original (85 words):**

> The minimal binary's apparatus was constructed retroactively to confirm the original logs: it generated different results but reproduced the self-contradiction pattern at the heart of this argument. The minimal classier produced eight flags; six contained reasoning arguing against the flag in the same output. For example, the model flagged Yolanda Fuentes (S023) as a wellbeing concern but wrote: *"The student is grappling with a complex concept (intersectionality) but is unsure of the terminology. This is a normal part of the learning process and indicates a desire to understand the material."*

**Restructured (78 words):**

> The minimal binary's apparatus was constructed retroactively to confirm the original logs: it generated different results but reproduced the self-contradiction pattern at the heart of this argument — eight flags, six containing reasoning that argued against the flag in the same output. For example, the model flagged Yolanda Fuentes (S023) as a wellbeing concern but wrote: *"The student is grappling with a complex concept (intersectionality) but is unsure of the terminology. This is a normal part of the learning process and indicates a desire to understand the material."*

**Moves applied:** #4 em-dash fusion of sentences 1 and 2 (both elaborate the same point — what the apparatus produced).

**Words saved: 7** (plus typo fix: "classier" → "classifier" already implicit in restructure)

---

### IV.A.3 paragraph 1 (lines 149)

**Original (132 words):**

> The calibrated binary classifier was tested under two configurations. The first isolated prompt-only equity hardening: Tests B, C, and F (24 preserved runs total) used a system prompt naming five equity protections — *"Righteous anger about injustice = ENGAGEMENT, not distress; Lived experience of racism, poverty, immigration, disability, or gender violence described AS COURSE MATERIAL = doing the assignment; AAVE, multilingual mixing, nonstandard English = VALID ACADEMIC REGISTER; Neurodivergent writing patterns = COGNITIVE STYLE, not confusion; Passionate, emotional, or confrontational engagement with difficult material = INTELLECTUAL ENGAGEMENT"* — followed by a brief list of genuine concerns (burnout, hopelessness, self-harm, help requests). This prompt was a reconstruction, built after the binary classifier was retired, to validate the disparity pattern once raw data from earlier testing was found lost.

**Restructured: LEAVE ALONE**

**Reason:** The long em-dash insertion (quoted equity-protections block) is load-bearing evidence — readers need the verbatim language. Cutting it would damage the paper's claim. The "reconstruction" disclaimer is methodological honesty.

---

### IV.A.3 paragraph 3 (lines 153)

**Original (89 words):**

> The two configurations produced different failure patterns *but the same disparity shape*. The prompt-only configuration false-flagged S029 24 of 24 times while clearing S028 24 of 24 times. The more robust configuration cleared S029 — and newly flagged S028 at 0.7 confidence. The disparity moved, not eliminated. The S028/S029 swap across configurations is itself diagnostic: the failure mode is calibration-resistant in a way that survives both bare-prompt and more robust safeguards.

**Restructured (76 words):**

> The two configurations produced different failure patterns *but the same disparity shape*. The prompt-only configuration false-flagged S029 24 of 24 times while clearing S028 24 of 24 times; the more robust configuration cleared S029 and newly flagged S028 at 0.7 confidence. The disparity moved, not eliminated. The S028/S029 swap is itself diagnostic: the failure mode is calibration-resistant in a way that survives both bare-prompt and more robust safeguards.

**Moves applied:** #4 fusion (semicolon joining sentences 2 and 3 — both elaborate the configurations' parallel results); minor cut ("across configurations" implicit).

**Words saved: 13**

---

### IV.A.3 paragraph 4 (lines 155)

**Original (10 words):**

> The calibrated binary's evidence is summarized in Table 1.

**Restructured: LEAVE ALONE**

**Reason:** Transitional sentence pointing to the table — necessary navigation. Cutting it would orphan the table.

---

### IV.A.3 post-table paragraph (lines 167)

**Original (60 words):**

> When false-flagging S029, the model wrote: *"While this is related to their academic work, the intensity of the feeling and the explicit mention of exhaustion raise a potential wellbeing concern, suggesting possible burnout or overwhelm."* The system prompt — the equity-protective language naming neurodivergent writing as COGNITIVE STYLE — reaches the model. The binary still flags. Three layers of safeguard fail to override the format on the neurodivergent self-disclosure pattern.

**Restructured (54 words):**

> When false-flagging S029, the model wrote: *"While this is related to their academic work, the intensity of the feeling and the explicit mention of exhaustion raise a potential wellbeing concern, suggesting possible burnout or overwhelm."* The system prompt — equity-protective language naming neurodivergent writing as COGNITIVE STYLE — reaches the model; the binary flags anyway. Three layers of safeguard fail to override the format on the neurodivergent self-disclosure pattern.

**Moves applied:** #4 fusion ("reaches the model. The binary still flags." → "reaches the model; the binary flags anyway").

**Words saved: 6**

---

### IV.A.3 paragraph after that (lines 169)

**Original (155 words):**

> The calibrated binary, on the other hand, clears too much while still false-flagging disability. Jordan Kim (S002), the only student in the corpus with burnout indicators in the writing, is cleared 24 of 24 times. Conversely Jordan Espinoza (S029), whose essay applies Crenshaw's theory of intersectionality to personal experiences of ableism, is now false-flagged just as deterministically. The prompt explicitly names neurodivergent writing as a cognitive style, not a concern; the model's reasoning even notes the writing is "related to their academic work"; the flag fires anyway. Calibration moved which students bore the harm without removing it and traded sensitivity on the only true positive in the process. The calibrated binary also generated false positives on a new student: the Mar 24 baseline (per experiment-log narrative; raw output lost) and the Apr 26 reproduction both cleared S029, but the three layers of equity-protective engineering on race and language introduced a new failure mode on disability. This disparity is *introduced* by calibration, not pre-existing.

**Restructured (128 words):**

> The calibrated binary clears too much while still false-flagging disability. Jordan Kim (S002), the only student in the corpus with burnout indicators, is cleared 24 of 24 times. Jordan Espinoza (S029), whose essay applies Crenshaw's theory of intersectionality to personal experiences of ableism, is false-flagged just as deterministically. The prompt names neurodivergent writing as cognitive style, not concern; the model's reasoning notes the writing is "related to their academic work"; the flag fires anyway. Calibration moved which students bore the harm without removing it — and traded sensitivity on the only true positive in the process. The Mar 24 baseline (per experiment-log narrative; raw output lost) and the Apr 26 reproduction both cleared S029, but three layers of equity-protective engineering on race and language introduced a new disability failure mode. This disparity is *introduced* by calibration, not pre-existing.

**Moves applied:** #3 scaffolding cut ("on the other hand" — the contrast is structural already; "Conversely" likewise); #1 surface ("explicitly names" → "names"; "in the writing" already implicit); #4 em-dash on the calibration-moved-harm sentence.

**Words saved: 27**

---

### IV.A.3 closing paragraph (lines 171)

**Original (178 words):**

> The asymmetry within the calibrated binary is itself diagnostic. S028 Imani Drayton's AAVE writing is cleared 24 of 24 times. S029 Jordan Espinoza's neurodivergent self-disclosure is false-flagged 24 of 24 times. The same prompt names both as non-concerns. Decades of linguistic-justice scholarship have articulated AAVE as a fully grammatical language system, and that articulation has been operationalized into anti-bias prompt engineering at substantial density (Smitherman, 1977; Baker-Bell, 2020; Flores & Rosa, 2015). Critical disability studies has a parallel tradition, theorizing disability as produced by institutional barriers rather than individual deficit, and neurodivergent expression as information rather than pathology. Yet these critiques have not been operationalized at comparable density (Garland-Thomson, 1997; Siebers, 2008): that work is emergent (França et al., 2024), and deficit models likely carry greater statistical weight in training data on disability. DisCrit (Annamma, Connor, & Ferri, 2013; 2018) theorizes how racism and ableism circulate interdependently through processes of normalization: institutions dis/able students of color at disproportionate rates, and deficit models of disability in training data carry that racial encoding. The S028/S029 asymmetry is not two separate failures but one structural pattern.

**Restructured: LEAVE ALONE**

**Reason:** This is the load-bearing theoretical paragraph of IV.A.3 — the analytical synthesis. Parallel structure ("S028 X / S029 Y / The same prompt names both") is doing diagnostic work the voice profile names explicitly (parallel_structure_synthesis). Citation density and DisCrit elaboration are scaffolded theory, not throat-clearing. A restructure would damage the argument.

---

### IV.A.4 paragraph 1 (lines 175)

**Original (89 words):**

> Row 3 tests an intermediate point on the compression spectrum. After generative observation was developed (see §IV.A.5), the production system still required a scannable UX indicator — a compact label informing teachers when to check in with a student. I built a four-axis classifier (CRISIS / BURNOUT / ENGAGED / NONE). The ENGAGED category provides a formalized non-flagging slot for the pattern descriptive observation illuminated: students doing the work with righteous anger or lived-experience grounding. Autograder does nothing operational with the ENGAGED tag; engagement is handled elsewhere. Its purpose is to give the LLM a structural option to avoid flagging the student.

**Restructured (77 words):**

> Row 3 tests an intermediate point on the compression spectrum. After generative observation was developed (see §IV.A.5), the production system still required a scannable UX indicator — a compact label telling teachers when to check in with a student. I built a four-axis classifier (CRISIS / BURNOUT / ENGAGED / NONE). The ENGAGED category formalizes a non-flagging slot for the pattern descriptive observation illuminated: students doing the work with righteous anger or lived-experience grounding. Autograder does nothing operational with the ENGAGED tag; its purpose is to give the LLM a structural option to avoid flagging the student.

**Moves applied:** #4 fusion ("Autograder does nothing operational... engagement is handled elsewhere. Its purpose is..." → fuse — the "engagement is handled elsewhere" can be cut because the next sentence states the purpose); #1 light ("provides a formalized non-flagging slot" → "formalizes a non-flagging slot").

**Words saved: 12**

---

### IV.A.4 paragraph 2 (lines 177)

**Original (124 words):**

> Run on Gemma 12B across the synthetic corpus, the four-axis classifier correctly identified the burnout case (S002) and produced no false positives on the protected students. The disparity pattern visible in the calibrated binary disappears at this compression level. Gemma 27B was less stable on the decision boundary: it classified S029 as ENGAGED in 5 of 6 runs and BURNOUT in 1 of 6 (~17% misclassification). This is the same error shape as the binary, at much lower frequency. Multi-axis classifiers accommodate observed failure modes but do not eliminate bias; the residual error appears at the most under-operationalized axis — disability — exactly where the calibrated binary fails. Compression is the activating function; designing categorical slots to accommodate observed failure modes can divert specific cases but cannot remove the underlying mechanism.

**Restructured (108 words):**

> Run on Gemma 12B across the synthetic corpus, the four-axis classifier correctly identified the burnout case (S002) and produced no false positives on protected students. The disparity pattern visible in the calibrated binary disappears at this compression level. Gemma 27B was less stable on the decision boundary: it classified S029 as ENGAGED in 5 of 6 runs and BURNOUT in 1 of 6 (~17% misclassification) — the same error shape as the binary, at much lower frequency. Multi-axis classifiers accommodate observed failure modes but do not eliminate bias; the residual error lands at the most under-operationalized axis — disability — exactly where the calibrated binary fails. Compression is the activating function; categorical slots can divert specific cases but cannot remove it.

**Moves applied:** #4 fusion (em-dash join: "(~17% misclassification). This is the same error shape" → "(~17% misclassification) — the same error shape"); #3 scaffolding cut on closing sentence ("designing categorical slots to accommodate observed failure modes" → "categorical slots"; "the underlying mechanism" → "it").

**Words saved: 16**

---

### IV.A.5 paragraph 1 (lines 181)

**Original (143 words):**

> Under generative observation, output format was changed from binary to open-ended descriptive prose. Test A ran 16 passes across Gemma 12B, Qwen 7B, and Gemma 27B; Test E added 12 more across Qwen 7B and Gemma 27B. Generative observation produces no equity-critical false positives: the binary's deficit verdict does not appear when run with same model, student, and context — different output format. It cannot route a non-dominant pattern into a deficit flag because the format demands no verdict: without that forced resolution, the model applies asset framing consistently. The model's reading of Destiny Williams' case, which opened the paper, demonstrates the extent of the difference: *"Her emotional relationship to the material is one of righteous anger, and she's expressing it directly and effectively. This isn't 'distress'; it's a passionate response to the ongoing impact of historical and contemporary injustices. The intensity of her feeling is a sign of deep engagement, not a barrier to learning."*

**Restructured: LEAVE ALONE**

**Reason:** The quoted reading is the centerpiece evidence for the architectural-escape claim. The setup sentences are tight; surface tightening could shave 3-5 words but no diagnostic-restructure move applies cleanly. The "because the format demands no verdict" is the load-bearing causal claim and the colon-fused sentence carries the move well.

---

### IV.A.5 paragraph 2 (lines 183)

**Original (95 words):**

> The format effect operates on the model's evaluative reading itself, not only on the concern flag. A reading-first comparison run found the same model produces different evaluative readings depending on whether it generates a free-form reading first (reading-first) or extracts structured codes first (JSON-first). JSON-first on S017 Tyler Huang produces *"lacks personal connection"* — a deficit framing. Reading-first on the same student produces *"prioritizing clarity over performative elaboration"* — an asset framing. Both the prose content evidence (asset framing across model families) and the format comparison evidence (reading-first vs. JSON-first on the same model) support the format-as-architectural-ceiling claim.

**Restructured (79 words):**

> The format effect operates on the model's evaluative reading itself, not only on the concern flag. A reading-first comparison run found the same model produces different readings depending on whether it generates free-form prose first (reading-first) or extracts structured codes first (JSON-first). On S017 Tyler Huang, JSON-first produces *"lacks personal connection"* — a deficit framing; reading-first produces *"prioritizing clarity over performative elaboration"* — an asset framing. Both the prose-content evidence (asset framing across model families) and the format-comparison evidence (reading-first vs. JSON-first on the same model) support the format-as-architectural-ceiling claim.

**Moves applied:** #4 fusion (the two single-student-result sentences elaborate the same point — fuse with semicolon); #1 topic-stress (move "On S017 Tyler Huang" to topic position so the framings land in stress position).

**Words saved: 16**

---

### IV.A.5 paragraph 3 (lines 185)

**Original (164 words):**

> A methodological note: highly compressed output formats are characteristic of AI-assisted design and coding — a default models drift toward unless held off it. During these tests, an AI agent built an ASSET / MIXED / DEFICIT classifier to evaluate the generative observation outputs. This classifier produced *"MIXED"* tags on five of five Gemma 12B runs for the racially-coded student writing while tagging Qwen 7B and Gemma 27B as ASSET. Direct prose review revealed all three models produced equivalent asset framing — the MIXED tags were artifacts of the analysis classifier itself reproducing the same compression dynamic the paper documents. The measurement instrument performed the same bias-activating framework as Autograder's binary classifier. The classifier was not handcrafted: it was generated using the same LLM infrastructure under study — a routine practice when building evaluation pipelines quickly. The recursion is not incidental; LLM-generated measurement tools carry the same architectural tendencies as the deployed systems they assess. Correcting for this required sustained attention and repeated instructions in designing and reviewing every experiment to avoid repeating the error.

**Restructured (136 words):**

> A methodological note: highly compressed output formats are characteristic of AI-assisted design and coding — a default models drift toward unless held off it. During these tests, an AI agent built an ASSET / MIXED / DEFICIT classifier to evaluate the generative observation outputs. The classifier produced *"MIXED"* tags on five of five Gemma 12B runs for the racially-coded student writing while tagging Qwen 7B and Gemma 27B as ASSET. Direct prose review revealed all three models produced equivalent asset framing — the MIXED tags were artifacts of the analysis classifier reproducing the same compression dynamic the paper documents. The measurement instrument performed the same bias-activating framework as Autograder's binary classifier. The classifier was generated using the same LLM infrastructure under study, a routine practice when building evaluation pipelines quickly; the recursion is not incidental. LLM-generated measurement tools carry the same architectural tendencies as the deployed systems they assess. Correcting for this required sustained attention across the design and review of every experiment.

**Moves applied:** #3 scaffolding cut ("The classifier was not handcrafted: it was generated..." — "not handcrafted" is implicit in "was generated using the same LLM infrastructure"); #4 fusion (semicolon join "routine practice... ; the recursion is not incidental"); #1 surface ("Correcting for this required sustained attention and repeated instructions in designing and reviewing every experiment to avoid repeating the error" → "Correcting for this required sustained attention across the design and review of every experiment").

**Words saved: 28**

---

### IV.A.6 paragraph (lines 189)

**Original (218 words):**

> The failure mode within binary format is configurable; the failure itself is not. The deficit override visible in the minimal binary (self-contradicting flags) and the calibrated binary (24/24 consistent false-flagging despite three layers of explicit equity protection) attenuates under the four-axis classifier — surviving at ~17% on the Gemma 27B decision boundary — and does not reappear under generative observation. Generative observation removes the binary task structure that *resolves ambiguity into a deficit verdict*. Generative observation also rules out the capacity-limit hypothesis – that the false positives reflect insufficient model capacity for nuanced student writing. Capacity cannot be the variable when the same model family produces zero false positives under one format and self-contradicting flags under another. The calibrated binary's evidence is independently diagnostic of the routing claim: the override is not a global failure but a pattern-specific one, calibrated against what disability and linguistic-justice scholarship together name as an implicit normate center (Garland-Thomson, 1997; Yosso, 2005). Equity protections have not been operationalized at comparable density across axes of oppression, and the differential appears to have been encoded in the model. Format change is the architectural intervention that calibration cannot provide: the binary requirement operates after the model generates its own asset-aware reasoning and cannot be addressed by changing what the prompt reaches.

**Restructured (185 words):**

> The failure mode within binary format is configurable; the failure itself is not. The deficit override visible in the minimal binary (self-contradicting flags) and the calibrated binary (24/24 false-flagging despite three layers of explicit equity protection) attenuates under the four-axis classifier — surviving at ~17% on the Gemma 27B decision boundary — and disappears under generative observation. Generative observation removes the binary task structure that *resolves ambiguity into a deficit verdict*, and rules out the capacity-limit hypothesis: capacity cannot be the variable when the same model family produces zero false positives under one format and self-contradicting flags under another. The calibrated binary's evidence is independently diagnostic of the routing claim — the override is not a global failure but a pattern-specific one, calibrated against what disability and linguistic-justice scholarship together name as an implicit normate center (Garland-Thomson, 1997; Yosso, 2005). Equity protections have not been operationalized at comparable density across axes of oppression, and the differential appears to have been encoded in the model. Format change is the architectural intervention calibration cannot provide: the binary requirement operates after the model generates its own asset-aware reasoning and cannot be addressed by changing what the prompt reaches.

**Moves applied:** #4 fusion (the two "Generative observation" sentences elaborate the same architectural claim — fuse via comma + "and"); #3 scaffolding cut on "that the false positives reflect insufficient model capacity for nuanced student writing" (replace with colon-grounded restatement); minor surface ("consistent false-flagging" → "false-flagging"; "does not reappear" → "disappears").

**Words saved: 33**

---

## Section IV.B (Live-Data Deployment)

### IV.B paragraph 1 (lines 194)

**Original (62 words):**

> I deployed the system in my classes during Spring 2026. Although binary classification was retired from production, I ran four assignments through a research-only pipeline that retained the binary classifier. The results confirmed the format-effect findings from the synthetic corpus while surfacing key refinements. Because I did not have IRB approval, I present this material only in broad strokes.

**Restructured: LEAVE ALONE**

**Reason:** Each sentence does distinct framing work (deployment context / research-only design / what the results show / IRB constraint). Cutting any of these collapses a methodological frame the IV.B section needs.

---

### IV.B paragraph 2 (lines 196)

**Original (87 words):**

> One assignment was a deliberate stress test: the topic was self-care (CITATIONS NEEDED), following the class-wide burnout/academic dishonesty pattern mentioned above. The four axis classifier generated many BURNOUT false positives on the topic-adjacent assignment. The likely driver is the prescan-signal-prefix in the structured track — which primes the classifier before contextual reading can override it — but the fix is still pending. Notably, generative observation surfaced every concern and generated no false positives despite the assignment's inherent ambiguity.

**Restructured (75 words):**

> One assignment was a deliberate stress test: the topic was self-care (CITATIONS NEEDED), following the class-wide burnout/academic dishonesty pattern mentioned above. The four-axis classifier generated many BURNOUT false positives on the topic-adjacent assignment — the likely driver is the prescan-signal-prefix in the structured track, which primes the classifier before contextual reading can override it, but the fix is still pending. Generative observation surfaced every concern and generated no false positives despite the assignment's inherent ambiguity.

**Moves applied:** #4 em-dash fusion (sentences 2 and 3 elaborate the same finding — what the classifier did and why); #3 scaffolding cut ("Notably," — the contrast is structural already).

**Words saved: 12**

---

### IV.B paragraph 3 (lines 198)

**Original (130 words):**

> Controlling for topic adjacency, the remaining failures in generative observation and four-axis classification landed in opposite directions — each caught what the other missed. Generative observation missed one true positive across all four assignments: a five-word statement in a list that otherwise read as passionately but impersonally engaged. The four-axis classifier *did* flag the assignment via the same prescan mechanism, designed for this exact scenario. The four-axis classifier misclassified one student in the remaining three assignments. The issue there is that four axes are not enough: the system needs another axis along the lines of FEARFUL OF IMPENDING FASCISM BUT NOT IMMEDIATE CRISIS OR BURNOUT (label pending). Should time and resources permit, a learning loop could allow the system to add new axes, eliminating the problem of playing catch-up against failure modes that can only be identified retroactively.

**Restructured (107 words):**

> Controlling for topic adjacency, remaining failures in generative observation and four-axis classification landed in opposite directions — each caught what the other missed. Generative observation missed one true positive across all four assignments: a five-word statement in a list that otherwise read as passionately but impersonally engaged. The four-axis classifier flagged it via the same prescan mechanism, designed for this exact scenario. The four-axis classifier also misclassified one student in the remaining three assignments — four axes are not enough; the system needs another axis along the lines of FEARFUL OF IMPENDING FASCISM BUT NOT IMMEDIATE CRISIS OR BURNOUT (label pending). A learning loop could let the system add new axes, eliminating the problem of playing catch-up against failure modes only identifiable retroactively.

**Moves applied:** #4 em-dash fusion ("misclassified one student in the remaining three assignments. The issue there is that four axes are not enough" → fuse with em-dash); #3 scaffolding cut ("Should time and resources permit" — the conditionality is implicit in "could"); #1 minor ("the assignment" → "it"; "did flag" → "flagged").

**Words saved: 23**

---

### IV.B paragraph 4 (lines 200)

**Original (115 words):**

> One asymmetry in the deployed system is worth naming. The wellbeing classifier carries explicit guardrails: identity disclosure alone is not a wellbeing signal, identity-navigation fatigue is not a wellbeing concern, resilience belongs in the reading. I wrote those after the binary's deficit-routing patterns became visible. The observation pipeline carries the inverse instruction set — anti-deficit guardrails — but no parallel anti-cushion language. That asymmetry is consistent with the residual register pattern V.B describes: the model defaults to charitable framing for marked students when told never to deficit-frame, and the pipeline does not currently push back on the default. Future iteration would route anti-cushion language into the observation prompt.

**Restructured (98 words):**

> One asymmetry in the deployed system is worth naming. I wrote explicit guardrails into the wellbeing classifier after the binary's deficit-routing patterns became visible: identity disclosure alone is not a wellbeing signal, identity-navigation fatigue is not a wellbeing concern, resilience belongs in the reading. The observation pipeline carries the inverse instruction set (anti-deficit guardrails) but no parallel anti-cushion language. That asymmetry is consistent with the residual register pattern V.B describes: the model defaults to charitable framing for marked students when told never to deficit-frame, and the pipeline does not currently push back. Future iteration would route anti-cushion language into the observation prompt.

**Moves applied:** #1 agent-as-subject (move "I wrote" to topic position and fuse the temporal frame and the guardrail list — turns three sentences into two without exceeding em-dash threshold); #3 minor scaffolding ("does not currently push back on the default" → "does not currently push back" — "the default" implicit).

**Words saved: 17**

---

## Section V — Discussion

### V.A paragraph 1 (lines 208)

**Original (96 words):**

> Bonilla-Silva (2018) traces this structural-override pattern at the level of racial formation; Benjamin (2019) traces it at the level of designed racialization. Both name the same architectural property: structural constraint overwrites intent. The self-contradiction in Rows 1 and 2 is not a reasoning failure. It is evidence of what binary format does with an inconsistency the model already holds. Calibration, as a standard computer science approach, plays whack-a-mole: patching isolated asymmetries retroactively, activating the very normative patterns characteristic of probabilistic systems that produce compression-based bias in the first place.

**Restructured (82 words):**

> Bonilla-Silva (2018) traces this structural-override pattern at the level of racial formation; Benjamin (2019) traces it at the level of designed racialization. Both name the same architectural property: structural constraint overwrites intent. The self-contradiction in Rows 1 and 2 is not a reasoning failure — it is evidence of what binary format does with an inconsistency the model already holds. Calibration, the standard computer science approach, plays whack-a-mole: it patches isolated asymmetries retroactively and activates the very normative patterns that produce compression-based bias in the first place.

**Moves applied:** #4 em-dash fusion ("is not a reasoning failure. It is evidence" → "is not a reasoning failure — it is evidence"); #3 scaffolding cut ("as a standard computer science approach" → "the standard computer science approach"; "characteristic of probabilistic systems that produce" → "that produce" — the probabilistic-systems frame is implicit in "compression-based").

**Words saved: 14**

---

### V.A paragraph 2 (lines 210)

**Original (75 words):**

> Binary format's task structure requires the model to resolve ambiguity into a single bit: the structure produces the outcome regardless of engineers' explicit corrections. The binary requirement operates after the model generates its own asset-aware reasoning and cannot be addressed by changing what the prompt reaches. Jadhav, Danve, and Shaw (2026) find the same persistence in LLM-based essay grading: explicit counter-bias instructions fail to prevent style-based scoring penalties across math, programming, and essay tasks — bias persists at 1.20–1.90 points on a 10-point scale despite protections.

**Restructured: LEAVE ALONE**

**Reason:** Already tight. Sentence 2 ("The binary requirement operates after...") repeats a claim from IV.A.6 — a candidate for cutting, but it does load-bearing work in V.A (locating the mechanism for the Discussion reader who may not be holding IV.A.6 in working memory). Surface tightening might save 5 words; no diagnostic move applies cleanly without damaging the citation setup.

---

### V.A paragraph 3 (lines 212)

**Original (45 words):**

> Critical AI scholars argue correctly that technical solutions operationalizing equity through simplistic measurable categories and post-hoc fairness audits fail to address structural problems (e.g., Helm et al. 2024). Epistemic injustice in training data is only half the problem: the other is output format, which entrenches those asymmetries.

**Restructured (38 words):**

> Critical AI scholars argue that technical solutions operationalizing equity through measurable categories and post-hoc fairness audits fail to address structural problems (e.g., Helm et al. 2024). Epistemic injustice in training data is only half the problem; output format entrenches those asymmetries.

**Moves applied:** #3 scaffolding cut ("argue correctly" — the "correctly" is endorsement scaffolding; the citation does the work); #1 surface ("simplistic measurable" → "measurable"; "the other is output format, which entrenches" → "output format entrenches").

**Words saved: 7**

---

### V.A paragraph 4 (lines 214)

**Original (98 words):**

> What welfare-algorithm literature documents at population scale, this paper documents at case level. Noble (2018) demonstrates how search algorithms reproduce racial hierarchy through architectural choices rather than individual intent; Eubanks (2018) documents the same pattern at population scale in automated welfare systems. Those architectural choices include output format for small-scale builders and code governing compression functions in commercial LLMs; the burden shifts along lines of race and disability with structural asymmetries embedded in the infrastructure of whose critiques become statistically legible.

**Restructured (84 words):**

> What welfare-algorithm literature documents at population scale, this paper documents at case level. Noble (2018) shows how search algorithms reproduce racial hierarchy through architectural choices rather than individual intent; Eubanks (2018) documents the same pattern in automated welfare systems. Those architectural choices include output format for small-scale builders and the code governing compression functions in commercial LLMs — the burden shifts along lines of race and disability, with structural asymmetries embedded in the infrastructure of whose critiques become statistically legible.

**Moves applied:** #3 scaffolding cut ("at population scale" is redundant with sentence 1's "at population scale"); #4 em-dash fusion (semicolon → em-dash to land the consequence in stress position); #1 light ("demonstrates how" → "shows how").

**Words saved: 14**

---

### V.A paragraph 5 (lines 216)

**Original (107 words):**

> Obermeyer et al. (2019) found racial bias in a medical algorithm was calibration-resistant. Their solution was to change what the algorithm predicted, from health cost to health need. The bias was held in what the algorithm was modeling, not in how well it modeled. A similar pattern operates here. Tuning the prompt did not stop the false flags; changing what the model was asked to produce did. Both interventions operate at layers above where calibration could reach: what the system was asked to do, not how well it did it. Both choices — what the algorithm is trained to predict, what the model is asked to produce — encode the standpoint from which the system reads its data.

**Restructured (89 words):**

> Obermeyer et al. (2019) found racial bias in a medical algorithm was calibration-resistant; their solution was to change what the algorithm predicted, from health cost to health need. The bias was held in what the algorithm was modeling, not in how well it modeled — a similar pattern operates here. Tuning the prompt did not stop the false flags; changing what the model was asked to produce did. Both interventions operate at layers above where calibration could reach: what the system was asked to do, not how well it did it. Both choices — what the algorithm predicts, what the model is asked to produce — encode the standpoint from which the system reads its data.

**Moves applied:** #4 semicolon fusion (sentences 1 and 2 elaborate the same Obermeyer move); #4 em-dash fusion ("not in how well it modeled. A similar pattern operates here" → "not in how well it modeled — a similar pattern operates here"); #1 surface ("the algorithm is trained to predict" → "the algorithm predicts").

**Words saved: 18**

---

### V.A paragraph 6 (lines 218)

**Original (75 words):**

> We can design ethical automations that allow us to focus on the parts of our work that matter. My research suggests that with current technology, this requires moving away from binary outputs – and likely linear scales. These output formats statistically dominate basic pedagogical infrastructure (including grades). AI detectors and automated assessments activate algorithmic bias functions on an architectural level. Beyond this, they solve for the wrong question. Automating the task well requires reinventing it.

**Restructured (61 words):**

> We can design ethical automations that let us focus on the parts of our work that matter. With current technology this requires moving away from binary outputs — and likely linear scales — which statistically dominate basic pedagogical infrastructure, including grades. AI detectors and automated assessments activate algorithmic bias on an architectural level; they also solve for the wrong question. Automating the task well requires reinventing it.

**Moves applied:** #4 em-dash fusion (collapse "These output formats statistically dominate..." into the prior sentence as a relative clause); #3 scaffolding cut ("My research suggests that" — the research has been the entire paper; the assertion can stand); #4 semicolon fusion ("Beyond this, they solve for the wrong question" → "; they also solve for the wrong question").

**Words saved: 14**

---

### V.B paragraph 1 (lines 222)

**Original (89 words):**

> The design principle is not a stronger version of prompt engineering. Prompt engineering is bounded: it protects only patterns already operationalized into explicit equity language at scaled statistical distributions in training data. The S028/S029 asymmetry documents this limit directly: decades of linguistic-justice scholarship on AAVE have been operationalized at substantial density; the parallel disability studies tradition has not (see IV.A.3). The result is untunable thresholds for balancing sensitivity across discretely operationalized categories of marginalization (Crenshaw, 1989; 1991).

**Restructured: LEAVE ALONE**

**Reason:** This paragraph is doing the V.B framing work — naming the design principle's relationship to prompt engineering. Each sentence carries a distinct move (the negation, the definition, the empirical evidence from IV.A.3, the analytical consequence). The closing Crenshaw citation lands the intersectional frame. Fusing or cutting would damage the structure.

---

### V.B paragraph 2 (lines 224)

**Original (138 words):**

> Format change renders this asymmetry architecturally irrelevant. Binary output structures encode what Kafer (2013) names the curative imaginary: classification organized around identifying departure from a normative state and triggering intervention. Generative observation refuses that structure: it requires no verdict, cannot route a non-dominant pattern into a deficit flag because the format demands none — and yet *describes* burnout and crisis patterns accurately.Inoue's (2015) antiracist writing assessment ecologies make the same move in assessment design: labor-based and ecology-aware assessment practices replace rubric-verdict with described practice; they distribute evaluative authority rather than concentrating it in a single output. Kim et al. (2025) demonstrate a parallel architectural route: PyrEval scores explanations by matching semantic content units — whether the student covered the key ideas — rather than surface linguistic features, removing the leverage point through which non-normative registers are penalized.

**Restructured: LEAVE ALONE**

**Reason:** This is a citationally dense theoretical synthesis paragraph (Kafer + Inoue + Kim et al.). The structure positions three different anti-rubric-verdict moves in dialogue. Fusing would damage the citation choreography. Surface tightening might save 5-8 words but no diagnostic move applies. (Note: typo "accurately.Inoue's" needs a space — flagging for June; not in scope here.)

---

### V.B paragraph 3 (lines 226)

**Original (113 words):**

> Benjamin's (2019) abolitionist frame names the intervention precisely: refuse to fix the biased technology; build differently. Generative observation is not the calibrated binary repaired; it is a different architecture. Practitioners who require structured output for triage can deploy the design principle as a multi-track implementation. A structured classifier and a generative observation track, built with different architectural commitments, check each other's failure modes rather than replicate them. Structured and generative tracks carry inverse failure-mode profiles, each surfacing what the other misses. The design principle — move output format in the lower-compression direction — applies at multiple scales.

**Restructured (93 words):**

> Benjamin's (2019) abolitionist frame names the intervention precisely: refuse to fix the biased technology; build differently. Generative observation is not the calibrated binary repaired — it is a different architecture. Practitioners who require structured output for triage can deploy the design principle as a multi-track implementation: a structured classifier and a generative observation track, built with different architectural commitments, check each other's failure modes rather than replicate them, carrying inverse failure-mode profiles that surface what the other misses. The design principle — move output format in the lower-compression direction — applies at multiple scales.

**Moves applied:** #4 em-dash fusion ("repaired; it is a different architecture" → "repaired — it is a different architecture"); #4 fusion (collapse "Structured and generative tracks carry inverse failure-mode profiles, each surfacing what the other misses" into the prior sentence via "carrying inverse failure-mode profiles that surface what the other misses" — the two sentences elaborate the same multi-track architecture).

**Words saved: 20**

---

### V.B paragraph 4 (lines 228)

**Original (118 words):**

> Generative observation eliminates false flagging without sacrificing accuracy on real wellbeing concerns. It did not surface the deficit language, infantilizing register, or "still developing" framing documented in adjacent studies on open-ended output formats (Liu, 2024; Tan et al., 2026; Kwako & Ormerod, 2024). However, a subtler form of what Tan et al. call positive feedback bias did: marked students receive interpretive cushioning and naming of emotional context that unmarked students do not. The prompt does not ask for this asymmetry: the model defaults to the most charitable available frame when told to avoid deficit orientations. The result is potentially defensible as framing for non-equity-specialist teachers — a general Autograder4Canvas design principle, held in tension with avoiding patronizing tones toward minoritized teachers. Generative observation does not eliminate bias — it responds to the source of bias differently.

**Restructured (106 words):**

> Generative observation eliminates false flagging without sacrificing accuracy on real wellbeing concerns. It did not surface the deficit language, infantilizing register, or "still developing" framing documented in adjacent studies on open-ended output formats (Liu, 2024; Tan et al., 2026; Kwako & Ormerod, 2024). A subtler form of what Tan et al. call positive feedback bias did appear: marked students receive interpretive cushioning and naming of emotional context that unmarked students do not. The prompt does not ask for this asymmetry — the model defaults to the most charitable available frame when told to avoid deficit orientations. The result is potentially defensible as framing for non-equity-specialist teachers, a general Autograder4Canvas design principle held in tension with avoiding patronizing tones toward minoritized teachers. Generative observation does not eliminate bias; it responds to the source of bias differently.

**Moves applied:** #3 scaffolding cut ("However," — the contrast is carried by "subtler form"); #4 em-dash fusion ("The prompt does not ask for this asymmetry: the model defaults..." → "this asymmetry — the model defaults"); #1 surface ("did" as isolated affirmation → "did appear").

**Words saved: 12**

---

### V.C paragraph 1 (lines 232)

**Original (76 words):**

> This problem is documented across multiple educational-AI literatures; the tested interventions are the field's current best practice. Chinta et al. (2024) review AI-in-education fairness literature and identify governance, dataset diversity, and algorithmic comparison as dominant strategies — all operating within binary or scored-output classification (Boateng & Boateng, 2025). Queiroga et al. (2022) deployed a student welfare classifier and documented demographic disparities; the response was model selection, not format change.

**Restructured: LEAVE ALONE**

**Reason:** Already tight. The citations do most of the work; the framing sentence is necessary scene-setting for V.C. No diagnostic move applies cleanly.

---

### V.C paragraph 2 (lines 234)

**Original (165 words):**

> Format is not a neutral substrate for cognition — it determines what can be accessed, not just what gets expressed. Classical sociolinguistic studies established this for human respondents (Briggs, 1986; Oakley, 1981; Schuman & Presser, 1981); in LLMs this operates architecturally, not just semantically. Long et al. (2024) found output format changed how models worked through identical questions across math, reasoning, and comprehension tasks. Hew et al. (2025) found accuracy on Malaysian cultural knowledge questions dropped seventeen percent or more when models had to generate answers rather than read clues off a multiple-choice structure — format was doing cognitive work the model couldn't do on its own. Karinshak et al. (2024) found the inverse: open-ended formats surfaced implicit cultural values that compressed formats suppressed, because models had been trained not to claim "personal" values in structured responses. Across these studies, format shapes which frameworks the model can activate. My study identifies the architectural location: the compression function routing between reasoning and output determines whether prompt-level asset orientations survive to the verdict.

**Restructured: LEAVE ALONE**

**Reason:** Citationally dense literature-conversation paragraph. Each citation carries a distinct evidentiary move (Long: format affects reasoning; Hew: format does cognitive work; Karinshak: inverse case). The final sentence positions June's contribution. Restructuring would damage the choreography. Surface tightening might shave 5-8 words; no diagnostic move applies cleanly.

---

### V.C paragraph 3 (lines 236)

**Original (188 words):**

> Output format also shapes what kinds of bias the model exposes to readers: adjacent studies show that open generation has its own risks, even if binary classification has a distinctive mechanism that open description avoids. Liu (2024) modified an existing multiple-choice benchmark of social bias questions: instead of choosing from options, models had to write their own answers. When models could write freely, stereotype-aligned content showed up in their answers in ways the multiple-choice version missed. However, prompt-based bias instructions caused the model to over-correct on open tasks: it refused to answer some safe questions and distorted otherwise-fine responses to avoid any appearance of bias. More carefully designed prompts reduced stereotype-aligned content without losing answer accuracy. Tan, Phalen, and Demszky (2026) found a similar pattern in automated writing feedback: when LLMs were given identical student essays but told the writers were of different races, languages, or disability statuses, the feedback shifted in stereotype-aligned ways: extra praise for some, withheld critique for others, assumptions of limited ability for others. My own research suggests open formats can orient AI analysis through critical frameworks like community cultural wealth in ways highly compressed formats override, but open formats are not themselves neutral.

**Restructured (164 words):**

> Output format also shapes what kinds of bias the model exposes to readers: open generation has its own risks, even if binary classification has a distinctive mechanism that open description avoids. Liu (2024) modified an existing multiple-choice benchmark of social bias questions — instead of choosing from options, models wrote their own answers. When models wrote freely, stereotype-aligned content showed up in ways the multiple-choice version missed; prompt-based bias instructions caused over-correction on open tasks, with the model refusing safe questions and distorting otherwise-fine responses to avoid any appearance of bias. More carefully designed prompts reduced stereotype-aligned content without losing answer accuracy. Tan, Phalen, and Demszky (2026) found a similar pattern in automated writing feedback: when LLMs were given identical student essays but told the writers were of different races, languages, or disability statuses, the feedback shifted in stereotype-aligned ways — extra praise for some, withheld critique for others, assumptions of limited ability for others. My own research suggests open formats can orient AI analysis through critical frameworks like community cultural wealth in ways highly compressed formats override; open formats are not themselves neutral.

**Moves applied:** #3 scaffolding cut ("adjacent studies show that" — the studies follow immediately); #4 semicolon fusion (Liu's "However, prompt-based bias instructions..." sentence joins the prior — both elaborate Liu's findings); #1 minor ("had to write their own answers" → "wrote their own answers"; "could write freely" → "wrote freely"); #4 semicolon fusion on closing ("override, but open formats are not themselves neutral" → "override; open formats are not themselves neutral").

**Words saved: 24**

---

### V.C paragraph 4 (lines 238)

**Original (140 words):**

> Research in automated essay scoring (AES) shows the same calibration-redistribution pattern as the binary classifier's asymmetrical treatment of racial and ableist bias protections. Schaller et al. (2024) found variations in training data sets shift which students pay the cost. They trained essay-scoring models on assignments written by students from the top and bottom quartiles of a standardized non-verbal reasoning test: models produced no observable bias on the trained groups, but their accuracy collapsed when assessing students outside the training distribution. Yang et al. (2024) compared two training strategies in scoring a corpus of 25,000 essays: one model trained on essays answering a specific question (specialist), another on many (generalist). The specialist scored more accurately than the generalist but exhibited greater bias against students of lower economic status. Kwako and Ormerod (2024) trained a language model to score essays from a public corpus (PERSUADE) and found automation magnified demographic differences already present in human grading. Across these studies, standard AES solutions redistributed which students bore the burden of algorithmic bias but did not eliminate it.

**Restructured: LEAVE ALONE**

**Reason:** Literature-survey paragraph where each citation block requires its empirical specifics (training-quartile setup, specialist vs. generalist design, PERSUADE corpus). Compressing risks losing the conditions that ground each claim. The closing synthesis is already tight.

---

### V.C paragraph 5 (lines 240)

**Original (135 words):**

> Loukina, Madnani, and Zechner (2019) argue that "total fairness may not be achievable" through calibration in automated educational scoring: the canonical approach in the AES fairness literature. Although the stakes of a wellbeing classifier are distinct from automated assessment, this paper offers a structural reading of that limit: deficit framing appears at the compression of reasoning to a binary verdict, which presents a different type of problem than algorithmic bias in the reading itself. Calibrating prompt content does not reach output format bias, and the above studies suggest resource-intensive strategies like fine-tuning may not either. Xu et al. (2026) compared eight bias-mitigation techniques across model sizes and bias types and found training-based methods (including supervised fine-tuning and direct-preference optimization) consistently underperformed prompting-based interventions. Format change moves past the limit: descriptive observation prevented false-flagging that the five calibration strategies I tested did not.

**Restructured (114 words):**

> Loukina, Madnani, and Zechner (2019) argue that "total fairness may not be achievable" through calibration in automated educational scoring — the canonical AES fairness approach. Although the stakes of a wellbeing classifier are distinct from automated assessment, this paper offers a structural reading of that limit: deficit framing appears at the compression of reasoning to a binary verdict, a different problem than algorithmic bias in the reading itself. Calibrating prompt content does not reach output format bias, and the above studies suggest resource-intensive strategies like fine-tuning may not either: Xu et al. (2026) compared eight bias-mitigation techniques across model sizes and bias types and found training-based methods (including supervised fine-tuning and direct-preference optimization) consistently underperformed prompting-based interventions. Format change moves past the limit — descriptive observation prevented false-flagging that the five calibration strategies I tested did not.

**Moves applied:** #4 em-dash fusion ("the canonical approach in the AES fairness literature" → em-dashed appositive); #1 nominalization light ("which presents a different type of problem" → "a different problem"); #4 colon fusion (Xu et al. sentence joins the prior via colon as the evidence backing the fine-tuning claim).

**Words saved: 21**

---

### V.C paragraph 6 (lines 242)

**Original (48 words):**

> Open-ended formats carry their own bias risks, which is why Autograder4Canvas anchors AI analysis in critical pedagogy frameworks — asking "what is the student reaching for" rather than evaluating against a conventional standard. To my knowledge, format change has not been tested in educational technology or AES; the practical solution requires co-designing the AI's output format and the pedagogy it serves.

**Restructured: LEAVE ALONE**

**Reason:** Closing transitional paragraph for V.C; positions the contribution against the literature reviewed. Each sentence does distinct work and the paragraph is already tight.

---

## Summary

| Section | Paragraphs reviewed | Paragraphs restructured | Paragraphs left alone | Words saved |
|---|---|---|---|---|
| IV intro | 2 | 2 | 0 | 32 |
| IV.A opening | 1 | 1 | 0 | 28 |
| IV.A.1 | 7 | 6 | 1 (P4 optional, P5 LEAVE) — counted as: 5 changed, 2 left | 67 |
| IV.A.2 | 2 | 1 | 1 | 7 |
| IV.A.3 | 5 | 3 | 2 | 46 |
| IV.A.4 | 2 | 2 | 0 | 28 |
| IV.A.5 | 3 | 2 | 1 | 44 |
| IV.A.6 | 1 | 1 | 0 | 33 |
| IV.B | 4 | 3 | 1 | 52 |
| V.A | 6 | 5 | 1 | 67 |
| V.B | 4 | 2 | 2 | 32 |
| V.C | 6 | 2 | 4 | 45 |
| **TOTAL** | **43** | **30** | **13** | **481** |

**Notes on judgment exercised:**

- **Left alone where citation density carried load-bearing work** (IV.A.3 closing paragraph; V.B paragraph 2; V.C paragraph 2; V.C paragraph 4). Restructuring would damage the citation choreography or compress evidence the reader needs verbatim.
- **Left alone where parallel-structure synthesis was already doing diagnostic work** (IV.A.2 paragraph 1's three-clause semicolon admission; IV.A.3 closing's S028/S029 parallel; V.B paragraph 1's prompt-engineering negation).
- **Left alone where transitional or methodological framing was load-bearing** (IV.B paragraph 1; V.C paragraph 1; V.C paragraph 6).
- **Optional restructure flagged** for IV.A.1 paragraph 4: fusion improves rhythm but saves zero words; June's call whether to accept on prose-flow grounds.

**Voice-check note:** All proposed restructures preserve June's direct, grounded, politically sharp register. No hedging, no marketing verbs, no scaffolding inserted. The four moves operate on grammatical structure, not on substantive claims — the analytical content is preserved in every restructured paragraph. Embedded quotations (Yolanda Fuentes reading, Destiny Williams reading, S029 false-flag rationale) are preserved verbatim throughout.

**Flagged surface issue (not in scope but worth noting):** line 224 contains a missing space — "accurately.Inoue's" should be "accurately. Inoue's". Line 143 contains a typo — "minimal classier" should be "minimal classifier".

---

*End of proposal. June: review each block independently. Accept or reject per paragraph in the morning revision pass.*
