# output-format-bias — agent notes

This repo holds the output-format bias / normative gravity paper (`paper/ofb_paper_v4.md`), the synthetic corpus, the test harness, and analysis.

## Framings sharpened during the Oxford AFP application (2026-06-11)

Drafting the Oxford Accelerator Fellowship statement forced several framings sharper than the current paper draft. Worth folding back into a revision:

**1. The redistribution is not a clean "race → disability" handoff — it's relocation to the least-protected axis *within* a multiply-marginalized subject.**
The paper's S028/S029 asymmetry (AAVE cleared 24/24, neurodivergence flagged 24/24, same prompt) is real and central. But "harm moved from race to disability" flattens what the data shows. S029 (Espinoza) is *multiply* marginalized — dyslexia, ADHD, Latino, first-generation — and the essay explicitly refuses to separate those axes ("the combination is its own specific thing"). The deficit reading **routes through the disability-coded signal** (the "exhaustion"/intensity the flag latched onto) even in a student whose own analysis is intersectional. So the sharper DisCrit claim (Annamma/Connor/Ferri): calibration relocates the deficit reading to the axis with the *least operationalized critique in training data* — and it does so *within* intersectional subjects, not by handing harm between separable single-axis students. The "race vs. disability" framing should be qualified accordingly.

**1b. The false positives are CONTENT-based, not language/register-based — do NOT port the AAVE/linguistic-justice framing into other documents (flagged 2026-06-19, SSRC drafting).**
The paper frames cleared/flagged cases partly through AAVE and linguistic-justice scholarship (Baker-Bell, Smitherman, Flores & Rosa), which implies the classifier took issue with students' *language or writing structure*. It did not. The flags fall on **what students wrote about**: family histories, lived experience, and frustration at the systems of oppression they were analyzing. S029's exhaustion was flagged for its *content* (a structural analysis), not his dialect or form. The linguistic-justice density argument ("AAVE operationalized at density, disability not") rests on this inaccurate premise — reframe or cut it; the real asymmetry, if any, is in operationalized *disability* critique, not language. (June flagged the recurring port of this error into application drafts; fixing it in the paper stops the propagation.)

**2. The medical-model move, stated concretely: the verdict relocates the problem from the institution into the student.**
S029's essay locates exhaustion in *structures* (the labor of managing others' deficit assumptions across axes) — a social-model, political observation (the model's own reasoning field even logged it as "a political observation about their relationship to the institution, not a disclosure of current wellbeing crisis"). The binary verdict relocates that exhaustion *into the student* as a wellbeing risk (burnout). That relocation — **"the student located the problem in the institution; the classifier located it in the student"** — is the medical model concretely: the problem made individual rather than structural. Avoid "symptom"/"diagnosis" as shorthand (ambiguous — symptom *of what?*). The precise move is world→individual relocation. And the loop: the classifier **reproduces the very discrimination the student critiques** — re-performing the deficit reading the essay is analyzing.

**3. Normative gravity is a descriptive claim about how probabilistic systems reproduce a normative default — not a causal-mechanism claim, and not base-rate regression.**
Cash out "normative": the statistical center is a *normative default* (white, able-bodied as implicit baseline); the pull reproduces that default *even against explicit instruction* (the equity-protected prompt). That "against instruction" piece is what distinguishes it from base-rate regression and aligns it with Benjamin (*Race After Technology* / New Jim Code) and Bonilla-Silva (*Racism without Racists*): a "neutral" mechanism reproducing hierarchy without/against intent. The against-instruction property is specifically a *binary-classification* phenomenon (the reasoning field followed the instruction; the verdict overrode it) — don't over-generalize it to all configurations.

**4. Output format gates discursive function — they are confounded in the preliminary data, and that's the research question, not a flaw.**
The redesign (descriptive observation) reduced bias by changing format *and* prompt together, because the open format *afforded* a different task (describe vs. judge). So the preliminary finding does not isolate output format (binary verdict vs. open text) from discursive function (classification vs. reasoning vs. description). Frame this as the question the generalization study takes up, not as a hedge to apologize for.

<!-- SESSION NOTE 2026-06-23 (SSRC work) — revisit later, do not treat as resolved -->
## TODO / open finding: the "concern" channel conflates pedagogical-opportunity → concern
A distinct failure category, separate from flat self-contradiction and from the exception-denying
wellbeing bias: the binary concern classifier flags *good, engaged work* because the model wants to
make a teaching note ("the teacher could use this as a springboard to discuss [concept]") and the
schema gives it no slot but `concerns[]`. **Prompt-traceable:** of the 8 worked examples in
`src/research/prompts.py` CONCERN_PROMPT, 7 (all the power-move examples) end their `why_flagged`
with "Teacher may want to engage/discuss/redirect…"; only 1 (wellbeing) says "check in." That 7:1
ratio teaches the model that "a concern = teacher should discuss this concept," so notable/structural
student work collapses into a flag. Instances: S001 Maria (springboard), S028 Imani (structural
awareness), + ~9 "teacher should engage" hits. Decide later whether this is its own paper category.
Working data: /Users/june/Documents/Filing/Job Search/SSRC_Just_Tech/ofb_verification/
