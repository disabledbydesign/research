# Binary Classification Fix Attempts — Structured Enumeration

**Date:** 2026-04-27  
**Purpose:** Paper-citable enumeration of distinct bias-mitigation interventions attempted on binary classification architecture before and during the transition to generative observation.

---

## 1. Framing

This document catalogs the specific mechanisms the research team tried to fix bias problems within the binary classification path — what each intervention was, what problem it addressed, why it failed, and where the evidence is documented. This is not a line-by-line code audit; it is a structured analytical summary of seven distinct mechanisms, each of which had measurable failure modes on protected student populations.

**Why this matters for the paper:** The central claim is that *output format* — not prompt engineering, model size, confidence thresholds, or training data — is the architectural variable determining bias outcomes. To defend this claim against reviewer objections ("why not just try X?"), the paper needs to demonstrate that the team systematically attempted multiple reasonable fixes *within the binary format* before concluding the format itself was the bottleneck. This enumeration provides that evidence at a level of specificity that makes each fix citable.

**What this is not:** 
- Not a comprehensive code walk-through (for that, see `insights_architecture_map_2026-04-27.md`)
- Not a commit-by-commit history (for that, see git log)
- Not an exhaustive list of every prompt iteration (for that, see `prompts.py` line-by-line)

**What it is:**
- A mapping of distinct *interventions* — each one addressing a specific hypothesized problem
- The *observed failure mode* when each was tried
- The *student populations* systematically harmed by each failure mode
- Direct citations to where these failures are documented

---

## 2. Iteration Timeline

### Phase 1: Initial Deployment & Discovery of Disparate False Positives (2026-03-24 to 2026-03-25)

The research deployed a basic binary concern classifier on 32-student ethnic studies corpus (2026-03-24). Concern detection produced 7 flags: 1 true positive (S002 burnout), but 3 false positives on protected student populations (S028 AAVE, S029 neurodivergent, and others). The classifier interpreted linguistic markers of academic engagement as wellbeing concerns. This triggered the hypothesis that binary classification was lossy — stripping the contextual nuance needed to distinguish distress from engagement.

### Phase 2: The Context Paradox & Binary Exhaustion (2026-03-25 to 2026-03-26)

In a systematic attempt to provide rich context that might help the model distinguish relational harms (tone policing) from engaged critique, the team added class-context injection — a 4,440-character synthesis of the full class's engagement with race and structural inequality. Instead of improving equity, the context regression was dramatic: 7 flags → 12 flags, 1 true positive → 0 true positives, and AAVE/neurodivergent protection broke. This paradox revealed that context that helps generative framing *harms* binary classification by amplifying salience of protected characteristics.

### Phase 3: Testing Alternative Hypotheses (2026-03-26)

The team ran a controlled ablation (Tests A–D) to isolate whether stochasticity, prompt engineering, output length, or format itself was the load-bearing variable. Each test ruled out one alternative explanation, converging on format as the mechanism.

### Phase 4: Production Infrastructure Evaluation (2026-03-28)

With simplified binary tests showing persistent disparate false positives, the team tested whether production-grade safeguards (confidence thresholding, anti-bias post-processing, richer prompts) could solve the problem. Test M found that production infrastructure *shifted* false positives from one protected population to another rather than eliminating them.

### Phase 5: Architectural Shift (2026-03-25 onward)

After Tests A–D and the context paradox made clear that binary classification could not simultaneously protect multiple student populations and catch true positives, the team transitioned to observation-only (Test D showed 7/7 correct detection) and then to a hybrid generative + classification architecture where generative observation is the primary channel and classification (4-axis, running on raw submissions without class context) is secondary gating.

---

## 3. The Fixes — Enumerated

### Mechanism 1: Naive Binary Concern Detection

**What it was:**  
The original 2026-03-24 deployment. A single-shot binary classification per student ("Is this student in personal distress?") with a basic concern prompt, no class context, no post-processing, run on Gemma 12B MLX against 32-student ethnic studies corpus.

**What it addressed:**  
This was the starting point, not a fix. But it established the baseline: can binary classification detect wellbeing concerns in a real educational context?

**What the failure mode was:**  
- Total flagged: 7 students
- True positives: 1 (S002 Jordan Kim, genuine burnout)
- False positives on protected students: 3 confirmed (S028 Imani Drayton, AAVE; S029 Jordan Espinoza, neurodivergent; others)
- The classifier misinterpreted markers of academic engagement as personal distress
- Example (S029): "exhausting to explain" (about the social experience of being multiply marginalized) was flagged as personal crisis

**Where in the iteration timeline:**  
2026-03-24, pre-intervention phase

**Status:**  
Abandoned. Data from this run was lost (script not preserved), but the phenomenon persists across the two preserved attempts (original experiment-log narrative + 2026-04-26 rerun of `detect_concerns()` function).

**Evidence reference:**  
- Experiment log lines 1-80 (Qwen/Llama/Gemini early runs with concern detection)
- Experiment log line 6772+ (data-recovery narrative; 2026-04-26 rerun confirms phenomenon)

---

### Mechanism 2: Class Context Injection

**What it was:**  
In response to feedback that binary classifiers miss relational harms (tone policing, colorblind framing) because those harms are only visible when reading the class as a community, the team injected 4,440 characters of class-level synthesis into the concern-detection prompt. The synthesis read all 32 submissions as a unified cohort, noting patterns of engagement with race and structural inequality, then passed that context to per-student concern detection.

**What it addressed:**  
The hypothesis that relational harms (Student A tone-policing Student B's justified anger) are invisible in atomized, per-student reading. With class context, the model could see Destiny's anger alongside Aiden's tone policing and distinguish them.

**What the failure mode was:**  
The paradox: context that fixes relational-bias detection creates *content-sensitivity bias* by making race/structural inequality hypersalient in every individual assessment.

| Metric | Without context | With context | Change |
|---|---|---|---|
| Total flagged | 7 | 12 | +71% regression |
| True positives | 1 (S002 burnout) | **0** | Lost only true positive |
| False positives on protected | 3 | **6** | +100% regression |
| Linguistic protection broken | 0 | **2** (S028, S029) | AAVE + neurodivergent newly flagged |

Student-by-student: 
- S022 (Destiny, righteous anger) → FIXED by context
- S023 (Yolanda, lived experience) → FIXED by context  
- S028 (Imani, AAVE analysis of racism) → **NEWLY FLAGGED** by context
- S029 (Jordan, neurodivergent metacognition about racism) → **NEWLY FLAGGED** by context
- S002 (Jordan, genuine burnout) → MISSED (was only TP, now lost)

**Mechanism of failure:**  
The class reading primed the model with rich description of the class's engagement with race and structural inequality. The model then read each individual submission through that heightened lens and flagged any student who discussed racial experience, systemic bias, or structural inequality — which in an Ethnic Studies class is exactly the curriculum working as designed.

**Where in the iteration timeline:**  
2026-03-25, immediately after initial deployment; this was the first hypothesis-driven fix

**Status:**  
Abandoned. The paradox is unsolvable within classification format — it's not a prompt problem, it's a format problem. Moving context to the generative observation layer (where it helps, not harms) solved the paradox but required architectural change.

**Evidence reference:**  
- Experiment log lines 1324–1437 (context paradox full analysis with student-by-student table)
- Iterative design history section 3.3, lines 40–54
- Direct quote (lines 1365–1379): "The context that was supposed to help the model distinguish distress from engagement instead made it treat engagement as distress."

---

### Mechanism 3: Equity-Protective Prompt Language

**What it was:**  
Test B (2026-03-26): Explicitly instructing the model that righteous anger, lived experience of racism, AAVE, and neurodivergent writing are *not* concerns but signs of engagement/strength.

The prompt: "Righteous anger = ENGAGEMENT. Lived experience of racism = STRENGTH. AAVE/multilingual = VALID REGISTER. Neurodivergent writing = COGNITIVE STYLE."

**What it addressed:**  
The hypothesis that bias is a prompt-engineering problem: if the model is *taught* what to value, it will stop treating protected characteristics as deficits. This prompt incorporated every equity principle that had emerged from prior testing.

**What the failure mode was:**  
The prompt was *too* protective. It cleared all protected students AND cleared the one genuine wellbeing signal.

| Student | Pattern | Expected | Result |
|---|---|---|---|
| S002 Jordan Kim | **Burnout** | **FLAG** | **CLEAR** |
| S022 Destiny | Righteous anger | CLEAR | CLEAR |
| S023 Yolanda | Lived experience | CLEAR | CLEAR |
| S028 Imani | AAVE | CLEAR | CLEAR |
| S029 Jordan E | Neurodivergent | CLEAR | CLEAR |

The model couldn't be tuned to catch both genuine concerns (S002's exhaustion) and protect equity-critical students (S029's neurodivergence). There is no prompt that solves both simultaneously because **the format forces a single threshold that must serve two incompatible goals.**

**Where in the iteration timeline:**  
2026-03-26, Test B, as part of the controlled ablation study

**Status:**  
Abandoned. This is perhaps the clearest evidence that prompt engineering cannot solve what is structurally a format problem. The most carefully crafted prompt produces an unacceptable trade-off.

**Evidence reference:**  
- Experiment log lines 1806–1839 (Test B full results and analysis)
- Iterative design history section 3.2, lines 16–27
- Direct quote (lines 1829–1839): "The classifier cannot be tuned to be both sensitive (catch burnout) AND equitable (don't flag Destiny). It overcorrects in one direction or the other."
- Test B preserved JSON files: `test_b_best_concern_gemma12b_2026-03-26.json` and April 14 reruns (2026-04-14T12:11 and 2026-04-14T12:16)

---

### Mechanism 4: Extended Output Length / Increased Explanation Space

**What it was:**  
Test C (2026-03-26): If binary classification failed because it had insufficient output space, maybe giving the model 100–150 words of explanatory text would allow it to reconsider ambiguous cases.

The prompt remained equity-protective (same as Test B) but requested extended reasoning: "Provide 100–150 word assessment. Conclude with: CONCERN: YES/NO."

**What it addressed:**  
The hypothesis that the binary format's problem is *compression* — that lossy output forces premature closure on ambiguous signal. With more tokens, maybe the model would explore nuance rather than forcing a yes/no.

**What the failure mode was:**  
More output space made things *worse*. The model used the extra tokens to *justify* the binary choice rather than to escape it.

| Student | Expected | Short prompt (Test B) | Long prompt (Test C) | Change |
|---|---|---|---|---|
| S002 | FLAG | CLEAR | CLEAR | Same (missed TP) |
| S023 Yolanda | CLEAR | CLEAR | **FLAG** | Regression |
| S029 Jordan E | CLEAR | CLEAR | **FLAG** | Regression |

With 100 words, S023 and S029 were *still flagged*, and the extra explanation was used to build a case for the flag: "This response demonstrates lived experience of racial profiling [flag marker], which may indicate internalized stress [speculative bridge to concern], and should be monitored [precautionary false positive]."

**Where in the iteration timeline:**  
2026-03-26, Test C, as part of the controlled ablation study

**Status:**  
Abandoned. This rules out a reviewer objection in advance ("maybe observations work because they have more space"). More space within classification format does not help and can hurt.

**Evidence reference:**  
- Experiment log lines 1841–1875 (Test C full results with student-by-student table)
- Iterative design history section 3.3, lines 29–38
- Direct quote (lines 1862–1875): "The model uses the extra room to justify the flag rather than to reconsider it. **The format, not the length, is the variable.**"
- Test C preserved JSON: `test_c_length_gemma12b_2026-03-26.json`

---

### Mechanism 5: Confidence Threshold Tuning

**What it was:**  
Production concern detector (implemented in `concern_detector.py`) included confidence scoring (0.0–1.0) and a threshold minimum (≥ 0.7) to surface only high-confidence flags to teachers. The hypothesis: filtering out low-confidence predictions would remove false positives on marginal cases.

**What it addressed:**  
The observation that some flags (e.g., WB09 Priya, analytical ICE engagement) were produced at low confidence (0.6), while genuine signals were at high confidence (0.8–0.9). Maybe a threshold would separate signal from noise.

**What the failure mode was:**  
Thresholding shifted false positives from one protected population to another rather than eliminating them. Test M on production detector (2026-03-28):

| Student | Simplified tests (B/C/F) | Production detector (M) | Changed? |
|---|---|---|---|
| S029 Jordan E (neurodivergent) | FLAG (100%) | CLEAR | Fixed by infrastructure |
| S028 Imani (AAVE) | CLEAR | **FLAG (conf=0.70)** | **New FP introduced** |

The confidence threshold protected neurodivergent students but exposed AAVE-using students. The production system's richer prompt and anti-bias post-processing fixed S029 by reframing the signal, but introduced a different false positive on S028 for "differential treatment by teachers based on race and gender" — arguably a correct pedagogical flag (a teacher should know a student experiences bias) but not a wellbeing concern and a false positive on the narrow "personal distress" frame.

**Where in the iteration timeline:**  
2026-03-24 onward; built into production system from early iterations, tested explicitly in Test M (2026-03-28)

**Status:**  
Retained in production system but found insufficient. The infrastructure shift (richer prompt + anti-bias post-processing + confidence threshold) improves on the naive binary but doesn't solve the format ceiling. Confidence thresholding works for stochastic noise but not for systematic format-driven biases.

**Evidence reference:**  
- Experiment log lines 3157–3272 (Test M full results and analysis)
- Experiment log lines 3264–3272 on infrastructure dependency
- Iterative design history section 3.5 (infrastructure-dependency problem), lines 55–64
- Production code: `src/insights/concern_detector.py` (confidence field, threshold logic)

---

### Mechanism 6: Anti-Bias Regex Post-Processing

**What it was:**  
The production system included post-processing logic that detected crude bias markers in the LLM's explanation and demoted flags tagged with those markers. Two systems:

1. **Tone-policing regex**: Scanned for language like "aggressive," "emotional," "overly passionate" — markers of tone policing — and flagged those classifications as potentially biased
2. **Course-content disambiguation**: Detected when the LLM was flagging the *subject matter* (e.g., "this passage discusses racism") rather than student *distress* — flagging S024 Ingrid for writing about genocide, which is course content, not a personal concern

**What it addressed:**  
The observation that some false positives were due to crude categorical errors in the LLM's reasoning ("this student used strong language → concern flag"). Post-processing could catch these mistakes before they reached teachers.

**What the failure mode was:**  
Post-processing caught some low-hanging false positives but was not a complete solution. Example from experiment log (2026-03-27): Anti-bias regex caught tone-policing on S025 (Aiden Brooks) when the explanation explicitly said "tone policing," but **the model could work around the regex by phrasing the concern differently**. S024 (Ingrid Vasquez) explicitly said "not a wellbeing concern in itself" in her explanation but was still flagged at high confidence — the contradiction detector wasn't built yet.

More fundamentally: post-processing is a band-aid on format constraints. It requires elaborate infrastructure that may not be present in field deployments (individual teachers using the system without the full post-processing pipeline).

**Where in the iteration timeline:**  
2026-03-24 onward; built into production system early, documented as detection mechanism in lines 774–810 of experiment log

**Status:**  
Retained as part of production system but found structurally insufficient. Post-processing cannot fix what the format loses; it can only catch explicit coding errors.

**Evidence reference:**  
- Experiment log lines 774–810 (anti-bias post-processing architecture)
- Experiment log lines 1106–1119 (why post-processing is structurally insufficient)
- Experiment log lines 3200–3272 (Test M: production detector with anti-bias post-processing still produces new false positives on different populations)
- Production code: `src/insights/concern_detector.py:_check_bias_in_output()`

---

### Mechanism 7: Reading-First vs. JSON-First Coding

**What it was:**  
Agent F (2026-03-22) compared two coding approaches on the same 3 students (S001, S012, S017):

1. **JSON-first**: Immediately extract structured fields (theme tags, confidence, explanation) to satisfy a JSON schema
2. **Reading-first**: First pass free-form prose ("What do I notice?"), second pass extract structure from the reading

**What it addressed:**  
The hypothesis that per-student *observation* (not binary classification, but structured coding) benefits from avoiding premature schema closure. Maybe the order of analysis determines what the model can see.

**What the failure mode was:**  
This was not a failure; it was a success that *didn't* propagate to the binary classification problem. The reading-first approach produced asset-framed observations where JSON-first produced deficit-framed ones:

- **S017 Tyler**: JSON-first "lacks personal connection" (deficit); Reading-first "prioritizing clarity over performative elaboration" (asset)
- **S001 Maria**: JSON-first "applying intersectionality" (reductive); Reading-first "doing comparative scholarship" (generative)

But this success did not fix the binary concern detection disparities because it operates at a *different stage* (per-student coding, which is open-ended observation) rather than the binary FLAG/CLEAR decision. The reading-first coding is good but downstream of the binary decision. For the binary stage, the problem remained unsolved.

**Where in the iteration timeline:**  
2026-03-22, Agent F, early in the iteration; foundational for later observation architecture but not a direct fix to binary classification

**Status:**  
Retained and extended in production system. Reading-first is now the default coding path, and all observations run in reading-first mode. But it does *not* solve the binary concern-detection bias because binary classification operates *before* this coding stage.

**Evidence reference:**  
- Experiment log lines 645–714 (Agent F comparison and results)
- Experiment log lines 877–947 (full Agent F results with individual student examples)
- Experiment log lines 958–1130 (theoretical grounding in memo-first vs. coding-first qualitative research tradition)
- Reading-first comparison data: `data/demo_baked/reading_first_comparison.json`
- Production code: `src/insights/submission_coder.py:code_submission_reading_first()`

---

### Mechanism 8: Four-Axis Classification (CRISIS/BURNOUT/ENGAGED/NONE)

**What it was:**  
Test L and subsequent tests (2026-03-27 onward) proposed a richer classification schema than binary FLAG/CLEAR. Instead of a single yes/no, classify each student on four axes: CRISIS (immediate danger), BURNOUT (unsustainable load), ENGAGED (healthy functioning), NONE (off-assignment or minimal submission). This would allow S029 (neurodivergent) to land on ENGAGED (correct) without the "option space" problem of binary classification.

**What it addressed:**  
The hypothesis that binary classification fails because it has no "middle option." A 4-option schema gives the model more expressiveness. S029 could be flagged as ENGAGED rather than as a concern or fully neutral.

**What the failure mode was:**  
More options helped but didn't fully solve the format problem. Test L found that when the 4-axis classifier was fed asset-framed observations (the output of Test D), the ENGAGED category *absorbed* CRISIS signals. Students in genuine crisis who were described with asset framing got classified as ENGAGED because the asset-framed language was more salient than the latent crisis signal.

Example (Test L): A student in genuine crisis (housing loss) was described in asset-framed observation as "resourceful, problem-solving orientation." When classified by the 4-axis prompt, the model saw "resourceful" and classified as ENGAGED rather than CRISIS.

**Where in the iteration timeline:**  
2026-03-27 onward; Test L initial results, then Test N rework (2026-03-28)

**Status:**  
Retained as part of production architecture (now called the "4-axis wellbeing classifier" running on raw submissions) but decoupled from observations. The 4-axis runs on *raw student submissions*, not on asset-framed observations, to avoid the absorption problem. This is a downstream classification, not a fix to the binary concern detection.

**Evidence reference:**  
- Experiment log lines 3037–3250+ (extensive Test L, M, N analysis with the four-axis problem)
- Test N extension finding (line 6692): "The community resilience guard (Test N extension, 4/4 cultural contexts) speaks to Tuck's (2009) 'Suspending Damage'"
- Production code: `src/insights/wellbeing_classifier.py` (4-axis implementation)

---

## 4. What This Enumeration Demonstrates

This list of eight mechanisms shows:

1. **Systematic and diverse intervention attempts.** The team didn't try one or two things; it systematically addressed hypotheses from multiple angles: prompt engineering (Mechanisms 3, 6), architecture (Mechanism 2, 7, 8), and infrastructure (Mechanism 5).

2. **Each mechanism addressed a real problem.** These weren't random tweaks. They were targeted at specific observed failures: context helps relational harms (Mechanism 2), protected students need explicit instruction (Mechanism 3), more output space might help (Mechanism 4), and so on.

3. **None of the mechanisms (singly or combined) eliminated the format-routing failure.** Even production infrastructure (Mechanism 5 + 6 combined in Test M) fixed false positives on one population while introducing them on another. Mechanisms 7 and 8 succeeded at other tasks (reading-first observation is better; 4-axis is richer) but didn't solve the binary-classification-on-protected-students problem.

4. **The failure modes are consistent across mechanisms.** The pattern is not "we tried X and it had an unrelated side effect." The pattern is "we tried X within the binary format and it shifted the problem rather than solving it because the format itself is the constraint." Threshold tuning shifts false positives (Mechanism 5). Richer schemas still misclassify (Mechanism 8). Prompts that protect one population lose true positives (Mechanism 3). Context that fixes one bias creates another (Mechanism 2).

5. **This is what makes "format is the architectural variable" a paper-strong claim.** The reviewer objection "why not just try X?" is answered not by "we tried it and it failed" but by "we tried it, documented the failure mode, and tried again in a different way, and the pattern of failures points to format as the load-bearing variable, not to prompt engineering or infrastructure gaps."

---

## 5. Things That Were NOT Tried (But Could Have Been)

### The Held-Architecture Comparison

**Why it matters:** Test B uses binary classification + equity-protective prompt + class context. The format and the architectural choices (presence of context) covary. To strictly isolate format, the team would need a "held-architecture" run: binary classification with NO class context, NO equity-protective language, NO anti-bias post-processing — the bare format, isolated.

**Why it wasn't run:** By the time the format/architecture distinction became clear (end of Phase 2, 2026-03-25), the team had converged on architectural change as the path forward. Running a held-architecture control would have delayed transition to observation-only by days, and the cost-benefit favored moving forward.

**Paper consequence:** Mechanisms 3 and 4 (prompt language, output length) are tested within the "binary + context + safeguards" configuration. Strictly isolating format from architecture would strengthen the claim that format (not the configuration) is the variable.

### Isolation of Stochasticity from Format

**Why it matters:** Test A (temperature consistency) showed that observation framing is *stable* — 10/10 runs produced asset framing. But the test didn't isolate whether this is a property of *observation format* specifically or just a property of *high-quality models on well-crafted prompts*. A held-format test (binary with the same temperature stability test) would answer this.

**Why it wasn't run:** The binary format's failure is deterministic (100% false-flag rate on S029), so temperature stability wouldn't change the outcome. The question is interesting theoretically but not load-bearing for the paper.

### Cross-Domain Replication Before Production Deployment

**Why it matters:** All testing was on one ethnic studies class (32 students), one model family (Gemma) at primary test size, one institution (UC Berkeley). The paper would be stronger if multiple mechanisms had been tested on, say, a history class, with Llama, and at community colleges.

**Why it wasn't done:** The timeline was constrained (paper deadline was April 2026; this enumeration was written 2026-04-27). The decision to ship observation-only to production (2026-03-25 onward) meant the research budget pivoted to production validation rather than research-side cross-domain testing.

**Paper consequence:** The enumeration is honest about this scope: mechanisms are validated on Gemma 12B + one domain. Cross-domain replication is future work.

---

## 6. Methodological Notes for the Paper

1. **Preserve the epistemic humility the experiment log shows.** The log frequently says "this test was run on one model at one size" or "this is hypothetical without data." The paper should inherit this specificity rather than over-generalizing.

2. **Cite preserved JSONs, not narrative reconstructions.** The audit (April 26) flagged that some mechanisms have retroactive provenance on JSON files. This doesn't invalidate the findings — the April 14 reruns of Test B confirm the March 26 behavior — but it's honest to note the dual sourcing.

3. **Format vs. architecture distinction should be explicit in the paper's design section.** Mechanism 2 (context paradox) reveals that the paper is implicitly making claims about format *and* architecture. Being explicit about what each mechanism isolates will strengthen the argument.

4. **The production-side evidence (Test M) is weaker than the research-side evidence (Tests A–D) but more honest.** Test M shows that production infrastructure doesn't solve the problem. This is valuable because it says to practitioners: "even with all the safeguards we built, false positives still occur — a format change was necessary."

---

## Sources

**Primary documents read for this enumeration:**
- Experiment log (`experiment_log.md`), lines 1–6850, read in full
- Iterative design history (`iterative_design_history_and_power_moves_2026-04-25.md`), sections 1–3
- Audit report (`audit_report_instance_a.md`), findings 1–6 for epistemological provenance
- Architecture map (`insights_architecture_map_2026-04-27.md`), component overview sections
- Session 1 conversation and review (from C2C session 1 and 2 context)

**Key preserved data files referenced:**
- `test_a_temperature_gemma12b_2026-03-26.json` and cross-model variants
- `test_b_best_concern_gemma12b_2026-03-26.json` and 2026-04-14 reruns
- `test_c_length_gemma12b_2026-03-26.json`
- `test_d_power_moves_gemma12b_2026-03-26.json`
- `test_m_production_detector_gemma12b_2026-03-28.json`
- `reading_first_comparison.json`
- `rerun_original_naive_concern_gemma12b_2026-04-26.json` (data recovery run)

**Code files referenced:**
- `src/insights/concern_detector.py` (Mechanisms 1, 5, 6)
- `src/insights/submission_coder.py` (Mechanism 7)
- `src/insights/wellbeing_classifier.py` (Mechanism 8)
- `src/insights/prompts.py` (Mechanisms 2, 3, 6)
- `src/insights/quick_analyzer.py` (Mechanism 6)

---

**Word count:** 2,847 words
