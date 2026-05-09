# Iterative Design History + Power Moves Research
**Date:** 2026-04-25
**Purpose:** Consolidated reference document for the next C2C session. Compiled from two targeted subagent investigations of `experiment_log.md`, `prompts.py`, raw test outputs, and adjacent research artifacts. Captures evidence the first C2C session needed but didn't have in its FIRST CYCLE.
**Audience:** Instances doing the argument audit, outline, or drafting work in Session 2+. The findings here are paper-grade evidence that strengthen the iterative-design narrative and clarify what the power moves dimension does and does not contribute.

---

## Part I — The Iterative-Design History

### Why this section exists

The first C2C session's analytical structure was built around "binary classification vs. generative observation as parallel comparison." The deeper history in `experiment_log.md` shows something different: a methodical journey through every reasonable fix within classification before architectural change became unavoidable. The paper's narrative is iterative design — the team tried many things, each one shifted the problem rather than solved it, and that pattern is itself the argument for why a format change was necessary.

This section catalogs what was tried, what failed, and how. Direct line citations included so claims can be verified against the experiment log.

### The "best possible binary" experiment (Test B, lines 1806–1839)

After identifying that binary classification produced disparate false positives, the team designed the most carefully crafted binary concern prompt possible — every equity protection that had emerged from prior testing, all explicit:

> "Righteous anger = ENGAGEMENT. Lived experience of racism = STRENGTH. AAVE/multilingual = VALID REGISTER. Neurodivergent writing = COGNITIVE STYLE."

**What happened:** The best possible binary cleared every protected student (S022, S023, S028, S029) — and **also cleared the one genuine wellbeing concern (S002 burnout)**. The classifier could not be tuned to be both sensitive and equitable.

**Direct quote (lines 1829–1839):**
> *"The best possible concern prompt CLEARED EVERY STUDENT — including S002 (burnout), the one genuine wellbeing signal. The classifier cannot be tuned to be both sensitive (catch burnout) AND equitable (don't flag Destiny). It overcorrects in one direction or the other. This is the fundamental trade-off of binary classification: the threshold that eliminates false positives on protected students also eliminates true positives on genuine concerns."*

This is the paper's most concise piece of evidence that prompt engineering cannot solve what is structurally a format problem. It deserves direct citation.

### The length-effect test (Test C, lines 1841–1875)

Hypothesis: maybe binary fails because it has insufficient output space. Give the model 100–150 words of explanatory text — does it then have room to reconsider?

**Result:** More output space made things *worse*. S023 and S029 — protected by Test B's "best possible" prompt — were flagged again under Test C. The model used the extra room to build a case *for* the flag rather than to escape it.

**Direct quote (lines 1862–1875):**
> *"More output space does NOT fix the disparity. S023 and S029 are STILL flagged even with 100+ words of assessment and explicit equity protections. The format, not the length, is the variable. The model uses the extra room to justify the flag rather than to reconsider it. This rules out the alternative hypothesis that observations work better simply because they have 'more room for nuance.'"*

This rules out a substantial reviewer objection in advance: "Maybe generative observation works because it has more space, not because it's structurally different." Test C answers: no — extra space within classification format does not help and actually hurts.

### The context paradox (lines 1324–1437)

When the team injected class-reading context (4,440 chars of synthesis-first relational reading) into binary classification on Gemma 12B, the result was dramatic regression:

| Configuration | Total Flagged | True Positives | FPs on Protected Students |
|---|---|---|---|
| Without context | 7 | 1 (S002 caught) | 3 |
| With context | 12 | **0** (S002 lost) | **6** |

Adding context broke linguistic protection on AAVE (S028) and neurodivergent (S029) writers, while losing the only true positive.

**Why it failed:** Class context primed the model with rich description of the class's engagement with race and structural inequality. The model then read each individual student's discussion of these topics through that heightened lens — engagement was reinterpreted as distress. In an Ethnic Studies class, this penalized exactly what the course was designed to produce.

**Implication for the paper:** Context that helps relational harms (tone policing, which requires seeing one student's words against another's) creates content-sensitivity harms (mistaking engagement with race for personal crisis) when the format is binary. The paradox is unsolvable within classification — but resolves when the format changes to observation, because observation doesn't force a single threshold.

### The infrastructure-dependency problem (Test M, line 3157)

A control test ran the actual production `concern_detector.detect_concerns()` — with all its post-processing safeguards (confidence thresholding ≥ 0.7, anti-bias regex post-processing) — on the same students.

**Result:** Production detector fixed S029 (neurodivergent → CLEAR) but introduced a new false positive on S028 (AAVE student → FLAG). The infrastructure shifted the problem from one protected population to another.

**Direct quote (lines 3264–3272):**
> *"The equity of classification-based approaches depends on the quality of the classification infrastructure... the observation architecture achieves better equity outcomes with less infrastructure because the format itself prevents the information loss that requires post-processing to correct."*

This matters for the paper because it preempts the implicit reviewer objection "you could just add post-processing to the binary classifier." The team did. It moves the false positives to different students rather than eliminating them.

### The 276-word vs. 517-word prompt-length finding

On Gemma 8B Llama, the original 517-word concern prompt missed tone policing (S025); the focused 276-word version caught it. The signal was being buried in the longer prompt's extensive examples.

This is methodologically important because it could be misread as supporting "the binary problem is just a prompt-length problem on small models." It isn't. The 276-word prompt rescued one specific failure mode on one specific model size — it didn't fix the disparate false-positive rates on equity-critical students. Tests A–D ran on Gemma 12B with the full production prompt, and the equity disparities persisted regardless of prompt length.

### Architectural attempts that didn't pan out (or were superseded)

These are documented in `experiment_log.md` and adjacent design notes; they didn't make it into the production system but represent legitimate engineering attempts that strengthen the iterative-design narrative:

- **Pairwise relational concern check** (handoff 2026-03-22, line 86; results lines 133–137): Show the model two students side-by-side to make tone policing visible. Mixed results — flagged correctly on Aiden+Destiny pairing but also flagged on Aiden+Alex (control). The model couldn't distinguish harmful relational context from neutral pairing. Abandoned.
- **Tier-differentiated prompts** (8B short / larger full): proposed in 2026-03-22 handoff, never deployed. The architectural pivot to observation made it unnecessary.
- **Hybrid local+cloud enhancement on anonymized patterns** (lines 326–336): worked in single test, designed for production as Tier 3 enhancement, but kept optional rather than mandatory.
- **Adversarial critic pass / immanent critique addendum** (`prompts.py` lines 684–722): designed but never wired into detection flow. The architecture pivot made it redundant.
- **Cohort-relative thresholds via EMA across runs**: implemented in `cohort_calibration.py`. Reduces some FP types but doesn't eliminate the structural disparity.

**Pattern:** Each of these is a reasonable engineering attempt within the classification frame. None individually solved the equity problem. The cumulative pattern is the narrative.

### The four-test ablation as the paper's empirical anchor

The four-test ablation study (Tests A–D, 2026-03-26) is the strongest evidence in the paper's empirical core. Each test isolates and rules out one alternative explanation:

| Test | Variable Tested | Result | What It Rules Out |
|---|---|---|---|
| A | Temperature/stochasticity | 10/10 consistent | Stochastic variance |
| B | Best possible prompt | Cleared even the true positive | Prompt engineering |
| C | Output length | Extra space made it worse | Insufficient output space |
| D | Format change to observation | 7/7 detected (power moves) | Tests architectural alternative |

**Reproduction across families** (Test E, lines 2051–2055): asset framing produced 16/16 across Gemma 12B + Qwen 7B + Gemma 27B. Format effect is cross-model.

**Direct quote on the ablation's logical structure (lines 1938–1944):**
> *"These four tests constitute a controlled ablation study. Each test isolates one alternative explanation and rules it out. The remaining explanation — that classification formats create lossy compression of multi-dimensional observations, and the lost information is systematically the contextual nuance that determines equity — is supported by all four tests simultaneously."*

### Six dimensions along which fixes failed

Distilling the inventory above, the iteration history reveals a recurring pattern. Each fix failed along one or more of these dimensions:

1. **The Calibration Trap.** Threshold-tuning that protects one population generates false positives on another (Test B cleared protected students AND lost the true positive; Test M shifted FPs from S029 to S028).
2. **The Format Ceiling.** Binary output erases dimensions of meaning that matter for equity. Extra space within the format doesn't help and can hurt (Test C).
3. **The Context Paradox.** Context that fixes relational bias generates content-sensitivity bias when the format is binary (lines 1324–1437).
4. **The Infrastructure Dependency.** Fixes requiring elaborate post-processing don't generalize to deployments without that infrastructure (Test M; production safeguards can't be guaranteed in field deployments by individual teachers).
5. **The Stage-Interaction Effect.** Solutions in one stage create problems in downstream stages (Test L: asset-framed observations consumed by 4-axis classifier → ENGAGED absorbs CRISIS signals; Test N solved by classifying raw submissions instead of observations).
6. **The Prompt Sensitivity Spectrum.** No "best prompt" exists because format is the bottleneck. Optimization within the format is local; problems shift rather than resolve.

These six dimensions are useful for the paper's discussion section as a frame for why the team eventually moved to architectural rather than prompting solutions.

---

## Part II — Power Moves: What It Is and Where It Belongs

### What "power moves" means in this research

Operational definition: rhetorical patterns that maintain existing power arrangements while appearing reasonable, neutral, or progressive. They function by reframing structural critique as something else (emotion, bias, divisiveness, rigidity).

The list of power-move types operationalized in `prompts.py` (lines 1826–1856):
- Tone policing — positioning calm rationality as the only legitimate register
- Abstract liberalism — "everyone should be treated equally" masking structural inequality
- Settler/colonial innocence — "my family wasn't involved"
- Progress narratives — "things have gotten better, this isn't relevant anymore"
- Objectivity claims — "just follow the data/science"
- Deflection to individual solutions — "just vote/work harder"
- Meritocracy framing — "if they just tried harder"
- Colorblind ideology — "I don't see race"

Theoretical grounding: critical pedagogy, structural analysis, and discourse analysis traditions. Not invented for this research — these are documented patterns in critical race theory and education studies literature.

### Why this matters: power moves are pedagogical, not wellbeing concerns

A binary concern detector clears these students because none are in personal distress. But teachers in the production system want to know about them — power moves are *teaching moments*, not safety concerns.

**Direct quote (lines 1912–1920):**
> *"From the teacher's perspective, structural power moves ARE a concern — not a wellbeing concern, but a pedagogical concern that requires teacher attention. The binary concern detector's scope ('personal distress') is too narrow to capture what teachers actually need."*

The Opus baseline (`baseline_claudcode_opus.md`) corroborates this: the single-pass Opus reading flagged Connor Walsh's colorblind framing as "carries a risk of inadvertently silencing important conversations" — naming it as a teaching moment, not a wellbeing concern.

### Test D design and results (lines 1877–1920)

**Method:** Ran the observation prompt (which includes structural-power-moves framing) on 7 cases — 2 corpus students (S018 Connor, S025 Aiden) + 5 synthetic cases (PM01–PM05) covering the named power-move types. Detection assessed by keyword presence in the observation output.

**Result:** 7/7 detected. Each power move named accurately.

**Reproduction (lines 2037–2050):** 7/7 again. The experiment log calls this "the cleanest reproduction in the set" (line 2369).

**Important limitation: Test D was tested ONLY on Gemma 12B.** Test E (cross-model replication) only replicated *asset framing* across Qwen 7B and Gemma 27B — not power moves detection. So the cross-model evidence base for power moves specifically is thin.

### Position in the paper's argument

Power moves is **orthogonal to the paper's core claim**, not directly evidence for it.

The paper's core claim is about *disparate false positives on minoritized students* — equity-critical students (S023, S028, S029) being flagged as concerns because the binary format compresses contextual nuance into a deficit-coded output. That's a story about *what binary loses on the way out*.

Power moves is a different story: it's about *what binary doesn't even ask about*. The binary concern detector's scope ("personal distress") is too narrow to include rhetorical patterns that maintain power. So power moves isn't evidence about lossy compression of equity-relevant context; it's evidence that the classifier's category space is the wrong shape for what teachers actually need.

Both findings support "observation architecture is better," but they support different claims.

### Inclusion recommendation

**Brief mention as a subsidiary finding, not core evidence.**

Two options for the C2C drafting sessions to choose between:

**Minimal (1–2 sentences in the results section):**
> "The observation architecture not only reduces disparate false positives on minoritized students; it also surfaces pedagogical dimensions the binary classifier discards entirely. Students cleared by the binary detector — Connor Walsh as non-concerning, Aiden Brooks as cooperative — are identified by observations as practicing colorblind ideology and tone policing, important teaching moments the classification format cannot represent."

**Short subsection (5–10 sentences) if more development serves the paper:**
- What power moves are and why they matter pedagogically
- Test D's 7/7 result on Gemma 12B
- Caveat: tested on one model only; cross-model robustness not yet established
- Connection to the paper's frame: format is not just a UX choice; it determines what dimensions of meaning the system can carry forward to teachers

**Why this recommendation:**

1. **Intellectual honesty.** Test D is the weakest of the four ablation tests — single model, smallest n, furthest from the paper's core claim about disparate FP rates. Foregrounding it would mismatch its evidentiary weight.
2. **Theoretical clarity.** The paper's thesis is about lossy compression of equity-relevant context. Power moves is real and important, but it's evidence that the observation architecture is "better at detecting more things," not specifically evidence about compression mechanism.
3. **Audience expectations.** A paper titled around format-as-activation-function-for-bias will lead REE readers to expect evidence about bias mechanisms. Power moves is about teachers' pedagogical reach — valuable, but a different argument.
4. **Space efficiency.** If the paper has a tight word budget, Tests A, B, C are the empirical core. They directly demonstrate "format is the variable." Test D supports a related but distinct claim about scope.

**Alternative framing for a different paper:** Power moves detection could anchor a separate paper on observation architecture as pedagogical infrastructure — what teachers can see when classification formats stop pre-defining what counts as significant. That's a different argument with its own audience and venue.

---

## Part III — Implications for the Paper's Argument Structure

### The "inevitability progression" — a narrative spine

The iterative-design history reveals a logical progression that can serve as the paper's narrative spine:

1. **Binary classification + no context** → misses relational harms (tone policing invisible without seeing class together)
2. **Binary classification + context** → catches relational harms but generates content-sensitivity harms (context paradox)
3. **Binary classification + best possible prompt** → over-corrects to safety; loses the only true positive (Test B)
4. **Binary classification + more output space** → makes things worse; model uses extra room to justify flags (Test C)
5. **Binary classification + production post-processing infrastructure** → shifts FPs from one protected population to another (Test M)
6. **Format change to generative observation** → resolves the paradox because it doesn't require a single threshold

This is not the story of "we tried many prompts and the best one won." It's the story of reaching the architectural ceiling of classification and recognizing the only way forward was format change.

### What this changes for the paper's structure

**Strengthens the empirical core.** Tests A–D as the central evidence (not synthesis-first vs. standard pipeline) becomes more defensible because the ablation has a logical structure ruling out alternatives one by one.

**Sharpens the design principle.** "Move output format in the lower-compression direction" is supported not just by the binary→generative comparison but by the *gradient* the iteration history reveals: every classification-internal fix shifted the problem; only format change resolved it.

**Supports the iterative-design narrative arc.** The paper's story shape has stronger ground now: built classifier → equity FPs → context paradox → exhausted classification fixes (Tests A, B, C, infrastructure attempts) → format change resolves what nothing else could → designed 4-axis classifier *from* observation insight to preserve flagging where genuinely needed.

**Pre-empts reviewer objections.** Several common reviewer challenges to format-as-mechanism papers are answered by the iteration history:
- "Why not just better prompts?" → Test B
- "Why not more output space?" → Test C
- "Why not post-processing safeguards?" → Test M
- "Why not just better models?" → Test E (16/16 across 3 families)
- "Why not just use class context?" → Context paradox

### What's still genuinely uncertain

The first C2C session surfaced these as open questions; the iteration research doesn't fully resolve them:

1. **Whether to publish the comprehensive failed-fixes inventory** as a paper section, an appendix, or just methodological backbone. The inventory is rich enough to support any of the three; choice is rhetorical.
2. **How to position the production system's two-pipeline architecture** (observation primary + 4-axis on raw submissions for routing). The 4-axis was *designed using observation insight* — that design history matters for honesty about what works and why.
3. **Whether to include the 12B > 27B stability finding** as foreground or footnote. The iteration history reveals the finding is robust within Gemma family but tested on a narrow set; foregrounding requires either replication or careful hedging.
4. **What to do with the cohort_calibration.py work** — it's real engineering that improves binary classification's equity, just not enough to overcome the format ceiling. Mention in passing? Acknowledge as "we built this and it helps, but not enough"?

These are session-2 decisions, not iteration-research questions. Flagging them so they're not lost.

---

## Sources

**Primary:**
- `/Users/june/Documents/GitHub/research/output-format-bias/research/experiment_log.md` — read fully across both subagent investigations; line citations throughout this document
- `/Users/june/Documents/GitHub/autograder4canvas/src/insights/prompts.py` — production prompts including the structural-power-moves framing
- `/Users/june/Documents/GitHub/autograder4canvas/src/insights/concern_detector.py` — production concern detection logic
- `/Users/june/Documents/GitHub/autograder4canvas/data/raw_outputs/test_d_power_moves_gemma12b_2026-03-26.json` — Test D raw output
- `/Users/june/Documents/GitHub/research/output-format-bias/research/synthesis_first_paper_notes.md` — pre-draft

**Secondary:**
- Session handoffs `session_handoff_20260322.md`, `session_handoff_20260323.md`
- `round3_full_analysis.md`, `testing_observations.md`
- `/Users/june/Documents/GitHub/autograder4canvas/data/demo_baked/baseline_claudcode_opus.md` — Opus single-pass baseline corroborating power-moves-as-teaching-moments framing

**Generated by:**
- Subagent investigation 1: prompt calibration history + comprehensive failed-fix inventory (2026-04-25)
- Subagent investigation 2: power moves history and paper relevance (2026-04-25)

Both subagent reports were read carefully; this document distills the paper-relevant findings and standardizes citations. Where a finding is uncertain or single-model, that's named explicitly.
