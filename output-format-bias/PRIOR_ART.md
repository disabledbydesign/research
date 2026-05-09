# Prior Art — Output Format & Bias in Educational AI
**Last updated:** 2026-04-20
**Purpose:** Annotated bibliography for the Autograder4Canvas finding. Establishes what the literature does and does not cover so future drafts (papers, grants, applications) don't overstate novelty claims.

## Core finding to situate
Replacing binary classification with generative observation eliminated demographic bias in a student welfare classifier. The headline empirical anchor is a four-test ablation study on Gemma 12B that systematically rules out alternative explanations (prompt engineering, model capability, output length, context); the format effect is reproduced across Gemma 12B, Qwen 7B, and Gemma 27B (16/16 generative-observation runs with zero binary flags on equity-critical students), with confirmatory qualitative comparisons across additional architectures (Gemma 4B, Llama 8B, Llama 70B, Nemotron 9B, Gemini Pro, Claude Opus). 32-entry synthetic corpus. **No published work tests this specific architectural intervention in educational AI.** That claim held up under a targeted Semantic Scholar search (April 2026).

---

## Category 1: EdTech bias literature — documents the problem, no architectural fix

These papers establish that algorithmic bias in educational AI is a documented, recognized problem. None propose or test output-format change as an intervention. Safe to cite as "the field knows the problem."

**Chinta, R., et al. (2024). "FairAIED: Navigating Fairness, Bias, and Ethics in Educational AI Applications." arXiv.**
Systematic review of fairness in educational AI. Catalogs bias sources, definitions, mitigation strategies, and evaluation resources. Mitigation strategies discussed: diverse datasets, ethical guidelines, post-hoc calibration. No architectural interventions. Does not address output format. → *Use to establish the problem exists and is documented.*

**Barnes, J., & Hutson, J. (2024). "Navigating the ethical terrain of AI in higher education: Strategies for mitigating bias and promoting fairness." Forum for Education Studies.**
Literature review and case studies. Mitigation strategies: diverse datasets and "ethical guidelines." No technical architectural proposals. → *Use to establish that existing mitigation strategies don't address architecture.*

**Córdova-Esparza, D.-M., et al. (2025). "AI-Powered Educational Agents." Systematic review of 82 studies.**
Finds "hybrid human–AI workflows outperform fully autonomous tutors" — the closest the edtech literature comes to an architectural observation, but it's about human-in-the-loop, not output format. → *Citable for "existing solutions rely on human oversight rather than architectural redesign."*

**Queiroga, E., et al. (2022). "Early Prediction of At-Risk Students..." Uruguay national deployment.**
Real deployed welfare classifier (Random Forest) with protected-attribute bias analysis. One of seven models failed bias checks and was excluded. Fix: reject the biased model, not redesign its output format. → *Closest to Autograder's context. Shows the field's current approach is model rejection, not architectural change.*

**Farheen, N., et al. (2025). "Equity and Bias in AI Educational Tools." Survey of teacher perceptions (N=270, Pakistan).**
Documents perceived problem; no technical intervention proposed. → *Background only.*

**Barnes, J., & Hutson, J. (2024). "Navigating the ethical terrain of AI in higher education."**
Same category — governance and awareness, not architecture.

**Cui, Y. (2025). "Educational AI and the Politics of Fairness."**
Theoretical critique arguing algorithmic classification itself produces inequality. Recommends policy/governance responses. → *Supports the claim that the problem is architectural, but doesn't propose the fix.*

---

## Category 2: LLM fairness / output format — adjacent, not direct prior art

These papers establish that output format affects bias in LLM evaluation contexts. They are NOT in educational AI and do NOT test the specific architectural intervention (deploying a generative classifier instead of a binary one). A reviewer who knows LLM fairness literature may raise these — acknowledge them and note the distinction.

**Liu, Y. (2024). "Evaluating and Mitigating Social Bias for Large Language Models in Open-ended Settings" (Open-BBQ). arXiv.**
Extends BBQ benchmark from multiple-choice to fill-in-the-blank / short-answer to measure bias in open-ended generation. Key finding: "predefined question formats like multiple-choice limit bias evaluation." Conceptual cousin — compares closed-form vs. open-ended *evaluation*, but does not propose generative output as an architectural fix for a deployed classifier, and is not in educational contexts. → *Cite to acknowledge the general finding; note the distinction: evaluation format vs. deployed system architecture.*

**Hew, K.F., et al. (2025). "MyCulture: Exploring Malaysia's Diverse Culture under Low-Resource Language Constraints." arXiv.**
Explicitly compares structured vs. free-form outputs as a driver of format bias in LLMs. Theoretical justification: open-ended structure improves fairness. Cultural-knowledge benchmark, not educational AI. **This is the single closest published paper to the Autograder hypothesis ("format itself is the bias lever")** — but in a different domain and without testing a deployed classifier. → *Most important to cite and distinguish. Note: cultural knowledge benchmark ≠ student welfare classifier; evaluation format ≠ deployed architectural intervention.*

**Xu, J., et al. (2025). "BiasFreeBench." arXiv.**
Benchmarks eight bias-mitigation techniques across multi-choice QA vs. open-ended multi-turn QA. Treats response format as an evaluation variable, not an intervention. → *Background — supports that format matters for bias measurement.*

---

## Category 3: Gap — not yet searched

**Automated Essay Scoring (AES) fairness literature.** AES tools have known racial bias documented by ETS researchers (Loukina and colleagues). If the novelty claim extends to "academic integrity / assessment tools," this sub-literature should be searched before finalizing. Search terms: "automated essay scoring fairness rubric generative feedback." The Autograder finding is about *welfare classification* (not scoring), so AES may not be directly relevant — but worth verifying.

---

## What the literature does and does not support

| Claim | Supported? |
|---|---|
| Algorithmic bias in educational AI tools is a documented, recognized problem | ✓ Strong — multiple survey papers 2022–2025 |
| Existing mitigation strategies focus on dataset diversity and governance, not architecture | ✓ Supported |
| Output format affects bias in LLM evaluation contexts | ✓ Supported (Open-BBQ, MyCulture, BiasFreeBench) |
| No published work tests binary → generative as an architectural fix in deployed student welfare classifiers | ✓ Supported as of April 2026 Semantic Scholar search |
| No published work tests this intervention across multiple model families | ✓ Supported |
| The finding generalizes to academic integrity tools | ✗ Not yet tested — analogical claim only |
| AES fairness literature contains no relevant prior art | ? Not yet searched |

---

## Citation language for different contexts

**Grant applications (SFF, Spencer, etc.):**
> "A substantial literature documents algorithmic bias in educational AI tools (Chinta et al., 2024; Córdova-Esparza et al., 2025); mitigation strategies in that literature focus on dataset diversity and governance, not architectural intervention. Recent LLM fairness work has established that output format affects bias in evaluation contexts (Liu, 2024; Hew et al., 2025) — but no published work tests replacing a deployed welfare classifier with generative observation or measures demographic impact across model families."

**Academic papers:**
Add: distinguish Hew et al. (2025) / Liu (2024) explicitly — same conceptual direction in non-educational contexts, different mechanism (evaluation format vs. deployed classifier architecture).

**Strongest novelty claim:**
"The architectural intervention — replacing binary classification with generative observation in a deployed student welfare classifier — has not been published. The general principle (output format affects bias) has support in non-educational LLM fairness research."

**What NOT to claim:**
- Don't claim the finding generalizes to academic integrity tools until tested
- Don't claim no one has studied bias in AES — that literature exists and wasn't fully searched
- Don't call Constitutional AI or Sparrow prior art — they address model alignment training, not output format in deployed classifiers
