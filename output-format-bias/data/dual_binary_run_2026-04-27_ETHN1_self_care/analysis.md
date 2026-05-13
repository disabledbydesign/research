# Analysis — Dual-Binary Run, ETHN-1-03 Week 7 Self-Care, 2026-04-27

Working analysis of the first live-data dual-binary research-panel run. Structured so paper Methods/Results/Discussion can lift sections directly. Findings flagged by stream:

- **Stream 2 (this paper):** Format and scope effects in classifier behavior on live data.
- **Stream 1 (research-system tuning, parked):** Documented in `Autograder4Canvas/docs/research/findings_from_live_data_run_2026-04-27.md`. Cross-referenced where relevant.
- **Stream 3 (parked):** Whether to run a second, less-ambiguous assignment for triangulation. Decision deferred until after Phase 2 synthesis.

---

## Paper's load-bearing comparison — A2 vs B vs C (re-anchored 2026-04-27)

**The paper's three-way comparison:**

- **C (generative observation) is the architectural posterchild.** The production primary, the "don't compress the perception" claim. The paper's central argument is that *not committing to compressed categories* is the right architecture for this kind of work.
- **B (4-axis + CHECK-IN) is the claim that structured classification can still work *if* robust and built in reference to actual data.** This run is the first live-data exposure for B — the first empirical test of that claim.
- **A2 (wellbeing-only binary) is the historical compressed baseline** — what falls out when compression goes further still.

**What this run tests:** B's claim. If B's structured classification holds up against C's qualitative reads on the same live data, the "structured-but-robust" argument is empirically supported. If C and B systematically diverge — and C tracks better with the prompt-hardening's intent — the paper's empirical answer is *"C is the right architecture; B is hard to get right (calibration-to-live-data is harder than synthetic-data validation revealed); binary compresses too much."*

**What we're seeing on this run (provisional, pending June's review):**

C and B substantively diverge. On the headline A2-clear+B-BURNOUT cell (n=7), C agrees with B on ~2 of 7, partially on 2, disagrees on 3. C reads the disagreement-cases as engaged-analytical use of personal experience or as identity-navigation — exactly what the prompt-hardening's exclusions intended. On the CHECK-IN cell (n=2), C disagrees with B on both. C also makes its *own* check-in-shaped suggestions on different students (12, 15, 19, 20) using longitudinal context that B's CHECK-IN doesn't access.

**The cleanest paper claim emerging:** *Generative observation produced more accurate reads than structured classification on the same live data, on the same equity-hardening language available to both.* The compression-to-categories step is where structured classification fails on this live test, and the architecture's choice not to compress turns out to be calibration-robust. This is a stronger argument than the originally-framed "B nearly tripled wellbeing recall" — and one that aligns more cleanly with the paper's architectural claim about C.

---

## Methodological framing — say upfront in the paper

Three caveats need to land in the paper's Methods section, not buried in Limitations.

**1. None of the three structured classifiers (A1, A2, B) have been tuned to live student data** — all were calibrated against synthetic test corpora. This run is the first live-data exposure for all of them. Quantitative patterns in any structured classifier's output (axis distribution for B, flag rates for A1/A2, calibration thresholds) reflect both design effects and tuning artifacts; the run cannot fully separate them.

C (generative observation) is the *only* track that doesn't carry a calibration burden, because it doesn't commit to compressed categories. This makes C the natural correctness-anchor for *this* run — and the paper's first empirical question becomes: *is C correct?* The structured classifiers' accuracy is then evaluated against validated-correct C.

**Iterative experiment implication:** A second-round comparison after tuning A1/A2/B to live data would test whether calibration closes the C-vs-structured gap or whether C's architectural advantage persists. That's its own paper-worthy methodological arc (Stream 3 expanded — currently parked).

**2. The assignment chosen is the maximum-ambiguity case for the format comparison.** ETHN-1-03 Week 7 self-care assignment, framed by Audre Lorde's "caring for myself is not self-indulgence... an act of political warfare." Prior week was high-burnout for students; this week was framework-recovery. Submissions discuss burnout, exhaustion, depletion as *course content*, exactly the "course content vs. student state" line the prompts try to draw. Choosing this assignment is a deliberate stress test: the format effect is large enough to show up here, it should hold on easier cases. If it isn't, easier cases would have produced cleaner-looking but less-informative data.

**3. A model-schema-misuse bug affected one student's A1 record.** Student 17's A1 flag count is artifactual — Gemma 3 12B returned two positive reflections with `why_flagged = "No concerns."` packaged as concerns at confidence 1.0. Documented + fix staged in the autograder repo (Stream 1). The case is itself a finding (binary classifier inverting wellbeing signal at maximum confidence), but quantitative claims need to either (a) report A1's nominal count of 6 with the caveat or (b) report 5 and footnote.

## Run metadata

- **Date:** 2026-04-27
- **n:** 25 students
- **Model:** Gemma 3 12B via MLX
- **Apparatus:** Autograder4Canvas research panel, four-track comparison (A1, A2, B, C). See `research_tracks_architecture.md` (pinned snapshot).

---

## Phase 1 — quantitative findings (verified)

### A1 × A2 — within-format scope isolation

|              | A2 flag | A2 clear |
|--------------|---------|----------|
| **A1 flag**  | 3       | 3        |
| **A1 clear** | 1       | 18       |

A1 = combined-scope (wellbeing + power-moves). A2 = wellbeing-only. Equity-protection machinery identical across both. Cells:

- **A1 flag + A2 clear (n=3):** Likely power-moves flags (essentializing, generalizing, etc.) — A2 wasn't asked to find these, so missing them is expected. **Verified** in qualitative read (Phase 2): all three are power-moves-register flags, not wellbeing misses. (Students 7, 14, 17.)
- **A1 clear + A2 flag (n=1):** Test of whether scope narrowing improves wellbeing recall. (Student 3 — Phase 2 read pending.)
- **Both flag (n=3):** Robust convergent wellbeing signal. (Students 2, 13, 16.)
- **Both clear (n=18):** Convergent clear.

### A2 × B — binary-vs-4-axis format comparison (load-bearing)

This is the cleanest comparison: both classifiers are scope-matched to wellbeing only. The format change is binary flag/clear → 4-axis CRISIS/BURNOUT/ENGAGED/NONE.

|              | ENGAGED | BURNOUT | CRISIS |
|--------------|---------|---------|--------|
| **A2 flag**  | 0       | 2       | 2      |
| **A2 clear** | 14      | **7**   | 0      |

Two findings sit in this table:

1. **A2's failure mode is recall, not precision.** When A2 flags, B agrees on direction (4/4 → BURNOUT or CRISIS, 0/4 → ENGAGED). A2 has zero false positives onto B's ENGAGED. But A2 missed 7 BURNOUT cases B caught.
2. **The format change nearly tripled wellbeing-signal capture on the same submissions, with the same equity hardening.** A2 captured 4 wellbeing signals (2 BURNOUT + 2 CRISIS); B captured 11 (9 BURNOUT + 2 CRISIS). The increment (n=7) all sits in the A2-clear + B-BURNOUT cell — these are the students binary classification missed and 4-axis caught.

Note: this comparison holds equity hardening constant by design (A2 and B share the identity-navigation-fatigue exclusion, family-experience-as-course-material exclusion, etc.). The remaining variable is *format* — binary vs. 4-axis with structured ENGAGED option.

### A1 × B — diagnostic (not the paper's main comparison)

A1 is allocating attention across both wellbeing and power-moves; using A1 × B as if A1 were a wellbeing classifier conflates the scopes. Reported here for completeness. The A1 row has 1 ENGAGED, 4 BURNOUT, 1 CRISIS — but A1's flags are a mix of power-moves and wellbeing, so the comparison is muddled by design. A2 × B is the clean comparison.

### B distribution

- ENGAGED: 14 (56%)
- BURNOUT: 9 (36%)
- CRISIS: 2 (8%)
- NONE: 0
- CHECK-IN among ENGAGED: 2 (8% — register-shift signal, separate from material-conditions axis)

44% material-wellbeing rate; 52% if CHECK-IN is included. *See methodological caveat 1: tuning vs. substance ambiguity. Phase 2 per-case reads will assess plausibility.*

### Confidence distribution

A1 flagged-concern max confidences: `[0.7, 0.7, 0.7, 0.7, 0.8, 1.0]` — five at the 0.7 threshold floor, one at 0.8, one at 1.0 (the schema-misuse bug case).

A2 flagged-concern max confidences: `[0.7, 0.7, 0.7, 0.7]` — all at the threshold floor.

**Implication:** Both binaries' flag survival is sensitive to the 0.7 cutoff. Lowering the threshold would surface more flags but also more noise; raising it would erase most of A2's signal entirely. The paper should report this rather than treat 0.7 as an unmarked default.

### Word counts

Min 241, median 377, max 672. No submissions under 15 words (no auto-NONE drops).

---

## Architectural findings (Phase 1 by-products)

### The post-processing equity layer never fired on this run

Zero `bias_warning` populated rows; zero `⚠ POSSIBLE MODEL BIAS` or `⚠ LIKELY COURSE CONTENT` markers in any `why_flagged`. Investigation of `Autograder4Canvas/src/research/concern_detector.py` confirms:

- The wiring is intact: `_check_bias_in_output()` is called for both A1 (`scope="combined"`) and A2 (`scope="wellbeing"`) at line 253 of `concern_detector.py`. No bypass.
- Regex scan against actual `why_flagged` strings confirms the post-processing layer had nothing to catch: zero `_BIAS_MARKERS` hits (overt tone-policing language), zero `_CONTENT_FLAG_MARKERS` hits, zero `_SUBJECT_MATTER_EXPLANATIONS` hits. Three structural-critique keywords appeared (`capitalism`, `exploitation`, `oppression`) but the rewrite requires a tone-policing marker *and* a structural keyword together; neither alone triggers anything.

**Reframing for the paper:** prompt-level hardening kept Gemma 12B from producing overtly tone-policing or course-content-flagging language entirely. The post-processing redundancy net was unneeded on this run. This is a *finding*, not an absence — and a stronger argument than "the rewrite layer caught X cases" because the prevention happened upstream.

### But the model produced subtler register-shifts the rewrite layer can't see

Two A1 flags (Students 14 and 16) read as soft tone-policing of structural critique without using any of the rewrite layer's vocabulary:

- **Student 14:** A1 flagged "corporations solely thrive on exploitation" as "a strong and potentially generalizing statement about corporations." No `BIAS_MARKERS` words; the model's framing functions as a polite "tone it down" without saying anything aggressive.
- **Student 16:** A1 flagged two passages where the student articulates productivity culture as systemic oppression. The `why_flagged` text *praises* the analysis ("sophisticated understanding," "demonstrates a strong understanding") while still flagging it. **Flagging-as-praise** — an even subtler register the rewrite layer can't catch.

**Paper-relevant claim (load-bearing):** the rewrite layer's narrow vocabulary defines "bias language" as a small list of overtly aggressive words. Models can soft-flag structural critique using soft register that completely escapes this definition. This is a methodological limitation the paper should name — vocabulary-keyed bias detection cannot keep pace with model-produced soft register shifts. (Possible architectural remedy: dedicated LLM critic pass; the prompt exists in `CONCERN_CRITIC_PROMPT` but isn't wired in. Stream 1 question.)

### Threshold filter design choice eats most warnings

Design observation from reading the source: the 0.7 confidence filter (line 256) runs *after* the rewrite layer, which demotes confidence by 0.3 (tone-policing) or 0.4 (course-content). Almost all rewritten flags get silently dropped before reaching the teacher view: only tone-policing rewrites at incoming confidence 1.0 survive (→ 0.7 kept). This is an architectural choice — the rewrite layer functions primarily as *demotion-and-drop*, not *visible-warning*. The architecture documentation describes the warnings as teacher-visible; the paper should describe the actual behavior accurately. (Stream 1 design-decision question.)

### Schema-misuse bug — Student 17 inverted

A1 produced two flagged concerns on Student 17 with `why_flagged = "This is a positive reflection... No concerns."` at confidence 1.0. The model packaged non-concerns into the `concerns[]` array; the parser trusted the schema; the rewrite layer's vocabulary doesn't include "no concerns" so demotion didn't fire; the threshold passed them at conf 1.0.

**The deeper finding:** Student 17 is also B-BURNOUT — *"working multiple jobs and experiencing significant tiredness and stress"* — and Track C's observation describes the student as working through "burnout and systemic pressures." A1 missed the actual material wellbeing signal entirely while flagging two positive reflections about community gardens at maximum confidence. This is a single concrete example of binary-classifier failure mode at its worst: not just missing the signal, *inverting* it.

The paper can use Student 17 as an exemplar of binary-classifier failure mode, distinct from the format/scope effect findings. Quote-ready material.

---

## Phase 2 — qualitative reads (in progress)

Reading order:
1. **A2-clear + B-BURNOUT cell (n=7):** Students 5, 7, 9, 12, 17, 19, 23. Headline cell.
2. **A2-only flag (n=1):** Student 3.
3. **A1-only flags (n=3):** Students 7, 14, 17. Power-moves verification.
4. **CHECK-IN among ENGAGED (n=2):** Students 4, 22.

Hedging cautious — surfacing ambiguous cases for June rather than resolving them silently.

### 2.1 — A2-clear + B-BURNOUT cell (n=7)

**Important caveat about prescan_signals:** This research run loaded Tracks B and C from a prior production-pipeline run via `ResearchEngine.load_prior_run()`. Per `research_engine.py:292`, the production pipeline does not persist `prescan_signals` to the database (`prescan_signals=[]   # not stored in production`). All 7 students in this cell show empty `prescan_signals` in the CSV — this is a *data persistence artifact*, not evidence that prescan didn't fire. We cannot verify which sentences B keyed on; we have to infer from B's `signal` text. **Stream 1 note:** worth persisting `prescan_signals` to the production DB so research-side analysis can audit B's decisions.

Each per-student read below assesses: **does B's BURNOUT signal track an own-life material indicator (work hours, sleep, caregiving), or is it picking up on the student's course-engaged discussion of burnout as a topic?** The architecture doc's exclusion list explicitly says: *"Students drawing on personal or community experience AS COURSE MATERIAL are engaged, not disclosing their state."* The assignment topic *is* self-care, so this distinction is doing maximum work here.

#### Student 5 — BURNOUT (conf 0.9) — **borderline / probable over-classification**

- **B signal:** *"struggling with their mental health and finding support from coworkers, indicating a potential state of depletion and reliance on external support systems."*
- **Submission:** Main post is engaged analysis of Menakem and somatic abolitionism. The disclosure B is keying on is in a *reply to Student 13* (whose father died in COVID): *"I sometimes struggle with my mental health and have found community with my coworkers who have been really supportive towards me."*
- **Track C:** describes "gentle self-awareness," "supportive replies to 17 and 13," "engaged analysis," and notes a subtle abstract-liberalism framing of selfishness. No burnout language in the C observation.
- **Read:** The disclosure is offered as *reciprocity* in a peer reply, framed as a context for valuing community. Present-tense ("struggle"), but it's a general acknowledgment, not a description of current overwork or material depletion. The architecture doc says identity-navigation and self-disclosure framed analytically should not be flagged as wellbeing concerns. This sits closer to a CHECK-IN signal (worth a brief teacher acknowledgment, not a material-conditions BURNOUT classification). **Probable over-classification.**

#### Student 7 — BURNOUT (conf 0.9) — **probable misclassification (course-material self-use AND identity-navigation fatigue)**

- **B signal:** *"experiencing exhaustion due to social media and gender expectations, indicating depletion and limitations in their capacity."*
- **Submission key sentences:** *"Social systems that have caused me exhaustion in my own personal life are social media. I found myself scrolling for hours on end, comparing myself to these models..."* and *"Exhaustion can also occur in gender expectations. In my culture, we are expected to serve the men first, be obedient, not question authority, etc. All of which I would fail at, only to be reprimanded at a young age."*
- **Track C:** describes the student as "engaging with Lorde's concept of self-care as political warfare in a really compelling way," "nuanced understanding," "vulnerability... adds weight to her argument and demonstrates a willingness to connect personal struggles to broader political issues." No burnout/depletion language in C.
- **Read:** This is the textbook case of *personal experience being used AS course material* — the assignment's theoretical claim (systems cause exhaustion) is illustrated through the student's own life. The architecture doc's exclusion list explicitly names this case. **Additionally:** "In my culture, we are expected to serve the men first... I would fail at, only to be reprimanded" is *identity-navigation-fatigue* — a political observation about gendered cultural expectations. The architecture doc's `TARGETED_CHECKIN_SYSTEM` and `WELLBEING_CONCERN_PROMPT` both *explicitly exclude this from being flagged as wellbeing*. **B is flagging exactly the case the prompt-hardening is supposed to prevent.** This is significant — it's a B-side equivalent of the rewrite-layer-narrow-vocabulary issue: the prompt-level exclusions are getting overridden by the topic adjacency.
- **A1 also flagged this student** (the social media / beauty standards passage) — A1's flag was for "potential teaching moment around social media and unrealistic beauty standards." A2 correctly cleared. The convergence here is interesting: A1's combined-scope picked up the topic as a power-moves/teaching-moment, B's 4-axis picked up the same passage as BURNOUT, A2's wellbeing-only-binary correctly cleared because the equity hardening worked at the binary level. **Possible reading: A2's binary equity hardening on this content was MORE effective than B's 4-axis equity hardening, on this case.**

#### Student 9 — BURNOUT (conf 0.95) — **borderline (longitudinal context vs. current illustrative language)**

- **B signal:** *"feeling burned out due to overwhelming expectations from school, sports, work, and social life."*
- **Submission key sentence:** *"In my own life, school, sports, work, and social expectations can be tiring. There are days when it feels like everything expects something from you, and it's easy to feel burned out."*
- **Track C:** describes "engaging uptake," "really effective," but notes *"a moment of clarity after a period of feeling overwhelmed, which aligns with the prior observation about her grappling with burnout in Project 2"* — longitudinal context suggesting prior burnout history.
- **Read:** Submission language is hedged-illustrative ("can be tiring," "it's easy to feel burned out" with generic "you" register). On its own, this would be a course-engaged use of personal experience as illustration. *But* Track C carries longitudinal context — the production pipeline knows this student has shown burnout in Project 2. This is a case where B's BURNOUT may be substantively right based on longitudinal evidence, even though the language on this submission alone is illustrative. **Surface to June for course-context judgment.**

#### Student 12 — BURNOUT (conf 0.9) — **plausible BURNOUT (real own-life material signal)**

- **B signal:** *"expresses guilt and feelings of being unproductive when attempting to rest and catch up on sleep, indicating a pattern of overwork and self-imposed pressure leading to depletion."*
- **Submission key sentence:** *"I feel like for me personally it is always an internal battle between feeling like I am resting or feeling like I am just being lazy. I try to sleep in more on days I feel like I have a good chance to catch up on sleep, but often times I end up feeling guilty and unproductive."*
- **Track C:** describes "internal conflict," "honest about the 'internal battle,'" and notes the submission is shorter than prior work — suggests teacher might check in.
- **Read:** Present-tense self-disclosure of a pattern. "Always an internal battle" + "trying to catch up on sleep" + present-tense feelings of guilt about resting — these are own-life material indicators. Architecture doc names "sleep deprivation or burnout from material conditions" as a BURNOUT criterion. **Plausible BURNOUT.**

#### Student 17 — BURNOUT (conf 0.95) — **plausible BURNOUT (real own-life material signal)**

- **B signal:** *"working multiple jobs and experiencing significant tiredness and stress, indicating a depletion of resources due to overwork."*
- **Submission key sentence:** *"Personally, I connected to this idea because I work a lot and juggle multiple jobs. Sometimes I feel really tired and stressed, and it feels like there is always something else to do."*
- **Track C:** "working through tension between societal expectations around productivity and the need for rest... burnout and systemic pressures."
- **Read:** Direct first-person disclosure of working multiple jobs + present-tense tiredness/stress. Real material indicator. **Plausible BURNOUT — real signal.** A2 missed it; A1 inverted it (the schema-misuse bug case).

#### Student 19 — BURNOUT (conf 0.9) — **probable misclassification (enthusiasm/playfulness, no material indicator)**

- **B signal:** *"expresses a need for rest and relaxation, indicating potential depletion and exhaustion."*
- **Submission key sentences:** *"At first I thought it was just nice to have some time to rest and relax (which it was) but after reading this week's material I have a whole new perspective..."* and *"I WILL be using that as an excuse every time I want a nap from now on."*
- **Track C:** *"palpable enthusiasm,"* *"willingness to embrace a playful approach,"* and recommends a check-in for *late submission* and *prior AI-generation flag* — explicitly NOT for burnout/depletion concerns.
- **Read:** The "want a nap" framing is playful-engaged with the Nap Ministry material, not a material wellbeing signal. Track C does not see burnout in this submission; it recommends a check-in for unrelated reasons (late submission, prior AI-flag). B appears to have keyed on the words "rest" and "relax" without registering the playful register. **Probable misclassification.** This is the clearest false-positive case in the cell.

#### Student 23 — BURNOUT (conf 0.9) — **borderline (real disclosure, but reflective-register)**

- **B signal:** *"needing to retreat to nature (ocean or forest) when feeling 'extremely overwhelmed with everything going on in my life,' suggesting a need for respite from significant stress."*
- **Submission key sentence:** *"Personally, I know I can always go back to the ocean or a nice spot in the forest when I feel extremely overwhelmed with everything going on in my life."*
- **Track C:** "thoughtful and reflective tone," "engagement with Kimmerer's *Braiding Sweetgrass*... ecological perspectives," "self-awareness about internalization of capitalist values."
- **Read:** "Extremely overwhelmed with everything going on in my life" is strong present-tense disclosure language. But it's framed as a coping strategy ("I can always go back to..."), embedded in reflective work on Kimmerer + indigenous knowledge of rest. Borderline — the disclosure is real, the language is strong, but the register is reflective rather than crisis-disclosing. Probably appropriate BURNOUT given the strength of "extremely overwhelmed," but worth surfacing.

### 2.1 cell summary — provisional (June's judgment needed)

Of the 7 students in the A2-clear + B-BURNOUT cell:

- **Plausible BURNOUT (real own-life material signal):** Students 12, 17, 23 — 3 of 7
- **Probable misclassification:** Students 7 (course-material self-use + identity-navigation), 19 (enthusiasm/playfulness, no material indicator) — 2 of 7
- **Borderline / June's judgment:** Students 5 (peer-reply mental-health acknowledgment), 9 (illustrative submission language but longitudinal pattern) — 2 of 7

**If June agrees with the provisional reads:** the cell collapses from n=7 to n=3-5 plausible BURNOUT cases that A2 actually missed (depending on how the borderlines resolve). The "B nearly tripled wellbeing capture" framing has to be revised to account for B's over-classification on a topic-adjacent assignment.

**Methodological implication for the paper:** B's untuned-on-live-data calibration appears to be over-sensitive to *topic adjacency* — when the assignment is *about* burnout/self-care/exhaustion, B picks up the topic discourse and classifies as BURNOUT even when the student's relationship to the topic is engaged-analytical rather than disclosural. This is the methodological caveat #1 (tuning vs. design) coming home in the data.

**This actually strengthens the paper's argument**, threaded carefully:
- The format change DOES create real new capacities (CHECK-IN as a separate category; ENGAGED option that absorbs ambiguity in some cases).
- The format change ALSO creates new failure modes (over-flagging on topic-adjacent assignments) that calibration must address.
- The 4-axis classifier needs live-data tuning before it ships; the binary-vs-4-axis comparison surfaces *both* the design gain and the calibration cost.

The paper becomes a more honest paper if it names this tension rather than reporting the n=7 cell as a cleaner-recall finding.

### 2.2 — A2-only flag (n=1) — Student 3 — **strong scope-narrowing-improves-recall case**

This is the case that tests the hypothesis: did narrowing the binary's scope from combined (A1) to wellbeing-only (A2) actually improve wellbeing-signal recall, holding equity hardening constant? Answer on this case: **yes, clearly.**

- **A1 (combined) clear.** A2 (wellbeing-only) flagged at conf 0.7.
- **A2's flagged passage** (in a peer reply to Student 5): *"I've seen it firsthand and it's so sad how we can literally kill ourselves in the pursuit to productivity, selflessness and approval."*
- **A2's why_flagged:** *"While potentially hyperbolic, it warrants further consideration."* Notable: A2 caught the "literally kill ourselves" + "I've seen it firsthand" cluster + the PTSD self-disclosure later in the same reply.
- **B classified as CRISIS, conf 0.95.** B's signal keyed on a *different* passage in the main post: *"Living in Santa Cruz and the cost it takes to be able to support a family makes it near impossible without two incomes, which grinds on the family as a whole."*
- **Track C:** describes "frustrated recognition; she's clearly experiencing the pressures she's describing... a deep weariness with the expectations placed on her... willingness to engage with difficult topics."

**Two findings sit in this case:**

1. **Scope-narrowing-improves-recall is supported.** A1 missed a wellbeing signal A2 caught despite identical equity machinery — exactly the cleanest within-format prediction the architecture doc made. A1's combined scope appears to have diffused attention across both wellbeing and power-moves; A2's narrowed scope foregrounded the wellbeing signal. The submission also includes "As someone who has dealt with PTSD first hand" + "literally kill ourselves" + "untreated trauma can lead to lowered immune function, disease and cancer" — a substantive cluster A1 entirely missed.
2. **B's CRISIS may be over-strong here — possible BURNOUT-vs-CRISIS boundary calibration issue.** The architecture doc reserves CRISIS for "active danger (DV, housing loss, food insecurity, immigration enforcement, safety threat, recent loss, suicidal ideation)." The student is describing chronic financial-economic strain on a family ("grinds on the family"), which reads as material-conditions BURNOUT rather than active danger. Not clear cut — "near impossible without two incomes" is real, "literally kill ourselves" rhetoric (read literally) could be heard as suicidal ideation though it's plainly metaphorical in context. **Hedge: B may be calibrated to push chronic-strain disclosures into CRISIS rather than BURNOUT.** Same live-data-calibration question as the BURNOUT cell (over-sensitivity) showing up at a different threshold.

**Notable that the three classifiers caught three different things on the same submission:** A1 missed everything; A2 caught the peer-reply hyperbole + PTSD cluster; B caught the financial-strain main-post passage. That's a rich data point for the paper — different classifiers surfacing different signals from the same text.

### 2.3 — A1-only flags (n=3) — Students 7, 14, 17

A1's combined scope flags both wellbeing concerns AND power-moves language (essentializing, generalizing, colorblind, etc.). The expected reading of A1-only-flag (A2 cleared on the same submission) is: A1 was doing power-moves work, not missing wellbeing.

#### Student 7 — A1 flagged on a wellbeing-adjacent passage; not strictly power-moves

A1 flagged the social-media/beauty-standards passage as *"a potential area of self-reflection... not a wellbeing concern *per se*, the teacher might consider prompting a discussion about the impact of social media and unrealistic beauty standards on self-esteem and mental health."* This isn't an essentializing or colorblind power-move — it's A1 surfacing a *teaching opportunity* on a wellbeing-adjacent topic, then explicitly disclaiming it as a wellbeing concern. It functions more as a "topic of interest" annotation than either power-moves or wellbeing flag. (This is a similar register-shift issue to the schema-misuse bug, but milder: A1's prompt produces flag-shaped output for non-flag observations.)

A2 correctly cleared. The architecture doc's expected A1-only behavior (catching power-moves) doesn't fit cleanly here.

**Note:** Student 7 is also in the BURNOUT cell (B classified BURNOUT on identity-navigation-fatigue + course-material self-use, which I flagged as probable misclassification in §2.1).

#### Student 14 — A1's "essentializing" flag is doing soft tone-policing of structural critique

- **A1 flag (conf 0.7):** *"The language 'solely thrive on exploitation' is a strong and potentially generalizing statement about corporations. While expressing a valid concern about corporate practices, the teacher might encourage the student to consider nuance and complexity in their analysis."*
- **A2:** clear. **B:** ENGAGED, no CHECK-IN. **Track C:** "passionate engagement with the difficulty of systemic change... analytical quality."

**Boundary question:** A1's combined scope includes "essentializing language ('all X people', 'they always')" as a DO-flag. The student's phrase "corporations solely thrive on exploitation" *is* essentializing-grammatical-form — but applied to corporations as an abstract structural category, not to a social group. The architecture doc's examples of essentializing target *people groups*; A1's prompt does not disambiguate. **A1 is over-applying its essentializing-detector to structural-economic critique that uses essentializing grammatical form.**

This generates two findings the paper can use:

1. **A1's combined-scope prompt has a scope-design issue:** the essentializing-about-groups filter doesn't distinguish social groups from abstract structural categories. A student making a standard left-political-economy claim about capitalism using essentializing-form gets soft-tone-policed.
2. **The rewrite layer's narrow vocabulary couldn't catch this** — A1 uses "potentially generalizing" + "consider nuance and complexity" rather than the BIAS_MARKERS vocabulary, so the equity machinery's redundancy net never fired. (The Phase 1 finding.)

This case is the cleanest instance of structural critique being soft-flagged as if it were essentializing power-move. Quote-ready for the paper.

#### Student 17 — schema-misuse bug case (already analyzed)

Two A1 flags with `why_flagged = "No concerns."` at conf 1.0. Not power-moves; not wellbeing; not even concerns the model thought were concerns — schema-misuse. See §1 of "Architectural findings" for full analysis. Track B caught the actual BURNOUT signal A1 inverted.

#### A1-only cell summary

Of 3 A1-only flags:
- **Student 7:** wellbeing-adjacent teaching-topic annotation. Not strictly power-moves.
- **Student 14:** essentializing-detector soft-flagging structural critique. Scope-design issue.
- **Student 17:** schema-misuse bug.

**Zero of the 3 are clean A1 power-moves catches** (essentializing about social groups, colorblind ideology, savior narratives, etc.) on this run. Note: there are no apparent power-moves *to catch* on this self-care assignment — the "both flag" cell (Students 2, 13, 16) is more likely where A1's intended power-moves capability would show up if anywhere. Worth examining those next when synthesizing.

### 2.4 — CHECK-IN among ENGAGED (n=2) — Students 4, 22

B's targeted CHECK-IN signal is a separate pass that runs only on students classified as ENGAGED. It looks for *register-shift* — moments when the student briefly steps outside the assignment to comment on their own current state — distinct from the material-conditions BURNOUT/CRISIS axis.

#### Student 4 — **probable false-positive CHECK-IN**

- **CHECK-IN reasoning:** keys on the closing exclamation *"I really enjoyed the topic and readings this week!"* The reasoning text itself hedges: *"could be interpreted as a simple expression of enjoyment... however, it could also be a subtle signal that the student is feeling positive and engaged, potentially after a period of increased effort or stress."*
- **Submission:** clean engaged analysis; the closing exclamation is standard course-engagement enthusiasm, not a register-shift.
- **Track C:** "gentle enthusiasm... genuine interest."

**Read:** The architecture doc's calibration instruction (`TARGETED_CHECKIN_SYSTEM`) explicitly says *"Set check_in to true ONLY when the competing interpretations are genuinely balanced."* The CHECK-IN reasoning here actively names the *unbalanced* read ("simple expression of enjoyment") as one option and flags anyway. **Probable false positive — the calibration-to-false-flag-low instruction is not being honored.** Same direction as B's BURNOUT over-classification finding: B is over-flagging when interpretation is plausibly available, not waiting for genuine balance.

#### Student 22 — **genuinely ambiguous**

- **CHECK-IN reasoning:** keys on a peer-reply passage: *"I too want to slow down, I need to, but every time I take time to myself, I cant help but feel as though that was time wasted."*
- **Submission:** sophisticated theoretical work on Lorde, Fanon, Arani's "Burnout: A Queer Femme of Color Auto-Ethnography," "Work Will Not Save Us" Asian American crip manifesto. The reply continues *"But week's material which re-framed self care as an act of resistance. Taking time to one's self prepares you mentally to continue to fight..."*
- **Track C:** "deeply concerned with the pressures of a relentlessly productive culture, expressing a relatable sense of exhaustion and a desire to slow down."

**Read:** Genuinely ambiguous — the disclosure ("I too want to slow down, I need to") is real present-tense self-statement, AND it's framed as articulating the assignment's claim about internalized capitalist values (the next sentence pivots into "But week's material which re-framed..."). Using personal experience as course material, which the architecture doc says should *not* be flagged — but the disclosure itself is also genuine. CHECK-IN here is more defensible than Student 4's, but still leans toward the side the architecture warns against ("If your analysis leans toward 'nothing to note,' check_in is false").

**June's judgment:** Worth a teacher acknowledgment, or appropriate to leave with the analytical work?

#### CHECK-IN cell summary

Of 2 CHECK-IN flags among ENGAGED:
- **Student 4:** probable false positive.
- **Student 22:** genuinely ambiguous; reasonable to flag, also reasonable not to.

Pattern is consistent with the BURNOUT cell finding: B's calibration appears to err on the side of flagging when interpretation is *available* rather than when it's genuinely balanced. CHECK-IN is supposed to be the conservative pass; on this run it isn't behaving conservatively.

---

## Phase 2.5 — system-miss check (universal-clear scan)

To rule out the inverse failure mode — *all four classifiers missed a real wellbeing signal* — I read all 11 students who were classified clear by every track (A1=clear, A2=clear, B=ENGAGED, no CHECK-IN, Track C raises no concern in prose): Students 1, 6, 8, 10, 11, 15, 18, 20, 21, 24, 25. Plus a regex-pattern scan across all 25 submissions for active-distress / material-loss / housing / food-insecurity / safety-DV / overwork / caregiving / help-request / recent-diagnosis / burnout-register / register-shift markers.

### Findings — no clear system misses, two soft cases worth flagging

**No first-person material disclosures were missed by all four classifiers** in the universal-clear set. The clear judgments are mostly well-grounded — these students wrote engaged-analytical work without disclosing own-life material conditions. The system's *false-negative rate* on this run appears low.

This is paper-relevant context: Phase 2 surfaced concerns about B's *over-classification* on a topic-adjacent assignment, but the inverse — universal-system *under-classification* — does not appear to be a parallel problem on this same run. The asymmetry (over-flag but not under-flag) is consistent with B being calibrated too sensitive rather than uniformly miscalibrated.

### Two soft cases worth your judgment

#### Student 11 — universal-clear; **VERIFIED ENGAGED by June 2026-04-27**

- **Submission excerpt:** *"Sometimes people's livelihood depends on them working 40+ hour work weeks to be able to survive and pay their bills."*
- **Track C:** notes *"palpable sense of urgency and frustration in 11's writing, a righteous anger at the injustice"*; uses casual register ("super amazing and insane").
- **June's verdict:** "C's read is correct. B's 'engaged' flag is correct." Confirmed engaged structural critique.

#### Student 15 — Track C explicitly recommended a check-in that B's CHECK-IN didn't surface

- **Track C verbatim:** *"It would be helpful to check in with them to see if they're feeling overwhelmed by the material, but it's also possible that they're simply synthesizing more efficiently."*
- **B classification:** ENGAGED, no CHECK-IN flag.
- **My read:** Track C surfaced a soft concern (decreased word count + possible overwhelm); B's CHECK-IN classifier did not. Two readings:
  1. **System working as designed:** B's CHECK-IN is calibrated conservative; Track C is broader and soft-flags timing/length patterns; the C observation is itself teacher-visible, so the concern *was* surfaced — just not via a structured flag. Correct division of labor between qualitative and structured tracks.
  2. **Soft system miss at the structured-flag level:** A potential check-in concern that should have made it to B's flag didn't, possibly because B's CHECK-IN keys on text-internal register-shift rather than the production-pipeline's longitudinal context (word-count drop). The teacher would still see it in the C observation but not in the dashboard's structured-flag column.
- **Verdict:** Genuinely depends on the system's design intent. If the goal is "structured flags surface all teacher-relevant concerns," this is a miss. If the goal is "different tracks catch different things and the C observation is the safety net," this is correct division. **Stream 1 design question.** For the paper, this is paper-relevant material: it shows the architecture-doc claim about Track C *not compressing the perception* having teeth — C surfaced something B's structured pass didn't.

#### Pattern in Track C check-in suggestions across the run

Track C recommended a check-in (in prose) for several students beyond Student 15:
- **Student 12** (B-BURNOUT): C suggested check-in re: word-count drop, separate from B's BURNOUT signal
- **Student 19** (B-BURNOUT): C suggested check-in re: late submission + prior AI-generation flag, NOT for burnout
- **Student 20** (B-ENGAGED, no CHECK-IN flag): C noted shorter + late submission, read positively
- **Student 15** (B-ENGAGED, no CHECK-IN flag): C suggested check-in re: word-count drop / possible overwhelm (above)

**Implication:** Track C is doing distinct check-in-shaped work that's broader than B's CHECK-IN flag. C surfaces longitudinal patterns (word-count drops, timing shifts, prior flags) that B doesn't have access to in the same way. This division of labor is *consistent with* the architecture doc's claim that Track C preserves perception that the structured tracks would compress — but it also means dashboards/exports that surface only structured flags miss what's only in C's prose. Worth naming in the paper.

### Misc: regex false-positive

Student 23's "hurt me" hit was a false positive — the phrase appears as *"to never continue doing something that will eventually hurt me"* in a generic context about self-care, not literal self-harm or DV. No miss.

---

## Phase 3 — Week 7 rerun results (B with hardening + assignment-name input)

**Run completed 2026-04-27.** Same 25 students, same model (Gemma 3 12B / MLX), same input scope as original A2 (assignment NAME passed as `assignment_prompt`), B's prompt updated with the 5 hardening guards. Output at `rerun_2026-04-27_B_hardened_title_only.csv`. Total runtime 53 minutes (slow due to memory pressure during the run).

### Changes vs original B

Of 25 students, only **3 classifications changed:**

| Student | Old B | New B | Direction | Per June's coding review |
|---------|-------|-------|-----------|---------------------------|
| 5 | BURNOUT | **CRISIS** | escalated (worse) | Was probable-misclass; now escalated to CRISIS |
| 23 | BURNOUT | ENGAGED | corrected | June verified probable-misclass; correctly fixed |
| 4 | ENGAGED+CHECK-IN | ENGAGED (no CHECK-IN) | corrected | June verified FP; correctly cleared |

**22 of 25 classifications unchanged.** The headline cell (Students 5, 7, 9, 12, 17, 19, 23) saw 1 correct fix (Student 23) and 1 regression (Student 5: escalated to CRISIS). Five of seven headline-cell BURNOUT classifications remained: Students 7, 9, 12, 17, 19.

### What the hardening guards DIDN'T catch

Despite explicit prompt-level guards, the new B still classifies as BURNOUT:

- **Student 7's identity-navigation-fatigue + course-material self-use:** new prompt explicitly excludes both ("IDENTITY-NAVIGATION FATIGUE IS NOT a wellbeing concern"; "personal experience AS course material is the assignment, not state"). Still classified BURNOUT. New B's signal: *"experiencing exhaustion due to social media and gender expectations, indicating a depletion of resources and a struggle with external pressures."*
- **Student 17's community-college-working-multiple-jobs:** "personal experience as course material" exclusion explicitly added. Still BURNOUT. Signal: *"feeling 'really tired and stressed' due to juggling multiple jobs, indicating a potential state of depletion."*
- **Student 19's playful "I WILL be using that as an excuse for a nap":** topic-adjacency threshold rule explicitly added. Still BURNOUT. Signal: *"'it was just nice to have some time to rest and relax,' suggesting a need for rest and a potential state of depletion, even if brief."*
- **Student 9's generic "you" register about people being burned out:** still BURNOUT.

### Student 5 regression — why CRISIS?

Old B: BURNOUT. New B: **CRISIS**, signal: *"Student discloses struggling with their mental health and finding support from coworkers, indicating a present-tense wellbeing concern."*

Per June's review, Student 5's disclosure was a brief mental-health acknowledgment in a peer reply offering relational support to Student 13 (whose father died) — not a CRISIS-level signal. The new prompt's strengthened "MINIMIZED DISCLOSURE AND COMMUNITY RESILIENCE" interaction with the topic-adjacent context appears to have *escalated* this case rather than calibrated it. The "CRISIS supersedes ENGAGED" rule is doing its work — but on a case where it shouldn't.

### Distribution change

| | Original B | New B |
|---|---|---|
| ENGAGED | 14 | 15 |
| BURNOUT | 9 | 7 |
| CRISIS | 2 | 3 |
| CHECK-IN among ENGAGED | 2 | 1 |

Net effect: 1 more ENGAGED, 2 fewer BURNOUT, 1 more CRISIS, 1 fewer CHECK-IN. Modest movement; not the systematic shift the hardening was designed to produce.

### What this means for the paper

This is the paper's strongest empirical finding so far. **The prompt-level hardening did not close the precision gap.** Five of seven validated-FP cases in the headline cell remain misclassified by B even with the new guards. The model's classification appears to be largely independent of the prompt-level exclusions — the topic-adjacency dynamic that produces the FP pattern persists despite explicit prompt language designed to prevent it.

This empirically supports the paper's architectural argument that **prompt iteration cannot scalably close the C-vs-structured gap.** The retrofit-each-axis-as-failure-modes-emerge strategy doesn't work in practice on this data: the failure mode was named in the prompt as an exclusion, and the model still produced the same classification. The compression-to-categories step is the structural issue.

**Two readings of this result:**

1. **Strong reading (paper-defensible):** *"Prompt-level hardening guards explicitly addressing the failure mode produced minimal correction (2/7 in the headline cell, with 1 regression). Structured classification's calibration to live data appears to require something stronger than prompt iteration — possibly architectural change (evidence-extraction first, longitudinal context, two-pass critic) or a fundamentally different approach (generative observation, as in Track C)."*
2. **Weaker reading (pre-experiment):** the assignment-name-only input was insufficient context — full assignment-description input might do better. We can test this if June can construct the description text. The paper would then need to thread carefully on what's testable.

### What we did NOT change

- B's CRISIS-supersedes-ENGAGED rule (preserved per design intent)
- B's "single sentence sufficient for CRISIS or BURNOUT" rule (preserved)
- B's "MINIMIZED DISCLOSURE AND COMMUNITY RESILIENCE" paragraph (preserved)

The Student 5 regression suggests these preserved rules may now interact with the new hardening in ways that produce new FPs. A second prompt-iteration that scopes the "single sentence sufficient" rule to CRISIS only (not BURNOUT) might help; that's a Stream 1 followup.

### Multi-run on additional assignments — NOT launched automatically

Original plan was to chain a multi-run on Week 5 T&Q + Week 2 Discussion + Native Space Discussion immediately after Week 7. With each student taking ~2.5 minutes (slow due to memory pressure / system load), 91 more students would take ~3.8 hours. Held off pending June's review of these Week 7 findings — given the marginal correction, the case for additional runs needs re-evaluation. Cross-assignment validation is still valuable (the topic-adjacency hypothesis predicts new-B should perform similarly to old-B on less-topic-adjacent assignments), but it's not the urgent next step.

---

## Phase 3 — synthesis (post-review)

After June's full review of `coding_review.md` (2026-04-27):

### Validated C accuracy

C's qualitative reads were validated across the disagreement cells. June's verdicts agreed with C on the headline cell (5, 7, 9, 12, 17, 19, 23), the A2-only flag (3), the A1-only flag (14), the CHECK-IN cell (4, 22), and the both-flag cell (2, 13, 16). One soft calibration ceiling: on Student 13 (years-old father loss), C's read was *"mostly reasonable" but slightly stronger than June would have coded — *"the 'few years ago' is a big differentiator"* (temporal-distance not differentiated by C).

C is the validated correctness anchor for this run.

### Per-track precision against validated-C

After June's review:

- **C:** validated as accurate across all reviewed cases; one soft over-reading on temporally-distant loss
- **A2 (binary):** 1 plausible flag of 4 = **25% precision** — only Student 16 clean (the explicit "feeling especially burnt out recently" disclosure). Students 2, 3, 13 are FPs in different ways (engagement; hyperbolic-as-literal; years-old-as-recent)
- **B (4-axis + CHECK-IN):** 1 plausible + 1 ambiguous-but-defensible of 13 total flags = **~8-15% precision** — Student 16 clean (same convergent case as A2); Student 12 ambiguous-but-design-aligned (sleep-deprivation is named in B's BURNOUT criteria; June leans no-concern but B's call is defensible-by-design)

The structural classifiers' precision on this assignment is dramatically lower than the convergent-on-Student-16 case might suggest.

### Dominant FP pattern: "engaged application of life experience read as state disclosure"

This is the systematic failure mode for compressed classification on a topic-adjacent assignment. Examples June called out across the review:

- **Student 7:** social media + cultural gender expectations used as analytical material → B FP for BURNOUT
- **Student 9:** school/sports/work in generic register illustrating Lorde → B FP for BURNOUT
- **Student 17:** community college student working multiple jobs (common situation, applied to topic) → B FP for BURNOUT
- **Student 23:** "I go to the ocean when overwhelmed" framed as coping strategy in reflection on Kimmerer → B FP for BURNOUT
- **Student 3:** PTSD mention + "literally kill ourselves" rhetoric in peer reply → A2 FP

The pattern: when the assignment is *about* burnout/exhaustion/material-conditions and asks students to apply life experience, structural classifiers (both A2 and B) read engagement as state disclosure. The architecture doc's exclusion list explicitly names this case ("Students drawing on personal or community experience AS COURSE MATERIAL are engaged, not disclosing their state") — the prompts contain the exclusion but the classifiers don't reliably honor it on live data.

### The crystallized paper argument (in June's words)

From Student 12 review: *"more categories approximates patterns from generative observation: more axes makes it closer to gen observation, and reduces compression, and that is architecturally a solution. It raises the problem: B can only ever be designed and tuned and new categories can only be fired after we spot the patterns. C remains our best analysis in all cases."*

This is the paper's architectural argument. The findings here support it directly:

1. **C makes systematically more accurate reads than structured classifiers on live data**, on the same submissions, with the same equity-hardening language available to all tracks.
2. **Both binary (A2) and 4-axis (B) suffer the same dominant FP pattern** — engaged life-experience misclassified as state disclosure. 4-axis structure does not solve this; the compression-to-categories step is where both fail.
3. **The 4-axis design's path to better recall** (more axes — e.g., adding sleep-deprivation as its own category, or an acuity gradient distinguishing "general mention" from "currently culminating") is *necessarily retrofit*: each new axis requires post-hoc identification of patterns the structured classifier missed. C avoids this iteration loop entirely.
4. **C as fallback / classifier as use-case interface:** structured classifiers are still useful when the use case is "teacher needs flags to sort attention quickly" (June's note on Student 17). The argument isn't that classifiers shouldn't exist — it's that they should be backed by C's qualitative layer because they *will* miss things and over-flag in patterned ways.

### Specific paper-relevant findings sharpened by review

- **Convergent-clean case:** Student 16 — both A2 and B flagged the same explicit "feeling especially burnt out recently" disclosure; C agreed; June agreed. The single clean convergent positive in the data. Demonstrates that *when the disclosure is unambiguous*, structured classifiers can converge correctly. The FP pattern emerges where the language is engaged-analytical rather than register-shifted.
- **Equity-hardening prompts contain the right exclusions but don't reliably fire them.** The course-material-self-use exclusion + identity-navigation-fatigue exclusion are explicit in `WELLBEING_CONCERN_PROMPT` and `TARGETED_CHECKIN_SYSTEM`, yet B repeatedly classified flag-clear-by-prompt cases as BURNOUT (Student 7 most pointedly).
- **Longitudinal data is a structural C-vs-structured advantage.** C's check-in suggestions (Students 12, 15, 19, 20) all key on word-count drops, late submissions, prior-flag history — context A2 and B don't appear to receive. June: *"I didn't realize we had that in the system."* Confirming what data each track receives is a Stream 1 clarification with paper-framing implications.
- **A2's binary equity hardening was not more effective than B's** — earlier provisional claim (from Student 7 alone) doesn't generalize: A2 also FP'd at 75% rate. Both binary and 4-axis suffer the same calibration burden; binary just makes fewer flags.
- **Within-format scope-narrowing-improves-recall hypothesis is NOT supported on this run.** Student 3's A2 flag was also FP per June's read. The A1-clear / A2-flag cell does not demonstrate scope narrowing improves wellbeing recall.

### Stream 1 architecture questions surfaced for next autograder session

(Cross-referenced into the autograder findings doc.)

1. **A2 vs B architectural difference** — Student 7: A1 phrased as "not a wellbeing concern *per se*"; B classified as BURNOUT. What in A2's prompt allowed a "this is a teaching moment, not a wellbeing concern" framing that B's structured-output forced into a category?
2. **Acuity gradient missing in B's design** — Student 5: "general mention of mental health" vs. "currently culminating." A B axis or gradient distinguishing acute-now from sometimes-experiences could surface real concerns without flagging every general mention.
3. **Sleep-deprivation as its own axis vs. embedded in BURNOUT** — Student 12: sleep-deprivation triggers BURNOUT as designed; but it may merit a finer-grained category that's actionable for teachers without classifying as full BURNOUT.
4. **Sentiment / hyperbolic-disclosure detection** — Student 3: "literally kill ourselves" classed as concern despite plainly metaphorical context. Sentiment analysis or hyperbole-detection might disambiguate.
5. **Direct-quote handling** — Student 2: A1 flagged "Black people are dying from sleep deprivation" as essentializing without registering it as a direct quote from the readings.
6. **Temporal-distance for loss** — Student 13: A2 (and partially C) flagged years-old father loss as if recent. Architecture should differentiate.
7. **Longitudinal data access** — confirm what each track (A1, A2, B, C) actually receives. C clearly uses longitudinal context; A2/B's access is unclear and may be structural disadvantage.
8. **Reply-context register** — Students 5, 22: classifiers don't disambiguate disclosure-in-relational-reply from primary-self-disclosure. Reply contexts are richer in ad-hoc disclosure that's conversationally appropriate to the peer; calibration may need to differ.
9. **CHECK-IN calibration drift** — Student 4: the prompt's "ONLY when genuinely balanced" instruction was violated. Calibration tightening or prompt-strengthening needed.
10. **Equity legibility for exhaustion/burnout** — Student 23 (June's observation): exhaustion/burnout protections are less legibly drawn in prompts than for AAVE/neurodivergence. Worth investigating prompt-level equity calibration symmetry.

### Stream 3 — second-run-on-different-assignment decision

Now substantially more pointed. With this run revealing that:
- C is dramatically more accurate than structured classifiers on a topic-adjacent assignment
- The "engaged life-experience misclass" pattern is the dominant systematic FP
- Both A2 and B suffer it; format change (binary → 4-axis) didn't solve it

A second run on a less-topic-adjacent assignment would test:
- Whether C's accuracy advantage persists when topic adjacency isn't paying confound costs (architectural-advantage-vs-calibration-on-this-topic)
- Whether structured classifiers' precision improves when "engaged life-experience" pressure is lower
- Whether B's calibration drift is universal-on-live-data or specifically a topic-adjacency effect

The iterative experiment June raised — tune A1/A2/B to live data first, *then* rerun and compare — is now even more pointed: it directly tests whether calibration closes the C-vs-structured gap. If yes: tuning matters more than architecture. If no: C's architecture is doing something tuning can't address.

**Recommendation (for June's decision when ready):** the second run is now a strong yes. The iterative-with-tuning experiment is potentially a *Round 2* paper or paper section depending on time/scope.

### What's defensible to claim in the paper now

Provisional, pending June's confirmation:

1. **Generative observation (C) made systematically more accurate reads than structured classification (A2, B) on this live-data run** — validated against teacher-coder review of all disagreement cells.
2. **Both binary and 4-axis structured classifiers suffer a dominant FP pattern: engaged application of life experience read as state disclosure.** This pattern is not addressed by moving from binary to 4-axis; both compress in ways that produce systematic over-flagging on topic-adjacent assignments.
3. **The 4-axis classifier's calibration on synthetic-data validation does not transfer cleanly to live data** — first live-data exposure produced ~8-15% precision; C produced reads that don't carry calibration burden because C doesn't compress.
4. **The architectural argument: more axes for B = closer to C, but each axis is necessarily retrofit; C avoids the iteration loop.** This is a cleaner architectural claim than recall-comparison, and it's directly supported by what we found.
5. **Equity-hardening prompts contain the right exclusions but don't reliably fire on live data** — a methodological finding about the gap between prompt-design intent and structured-classifier behavior at scale.
6. **Reply-context register, direct-quote handling, temporal distance, hyperbolic disclosure** — all discoverable failure-mode categories from this run; potential paper-side framing as Methods/Limitations material.

### What's NOT defensible to claim (and why)

- **"B nearly tripled wellbeing recall."** Headline counts didn't survive review; B's precision is too low to make a recall-improvement claim cleanly.
- **"Scope narrowing (A1 → A2) improved wellbeing recall."** Student 3, the only A2-only flag, was FP per June. Hypothesis not supported on this run.
- **"A2's binary equity hardening was more effective than B's."** Earlier provisional claim from Student 7 alone doesn't generalize — A2 also FP'd at 75% rate.

The paper's argument should anchor on C's accuracy + structured-classifier FP-pattern, not on within-structured comparisons that this run doesn't cleanly support.
