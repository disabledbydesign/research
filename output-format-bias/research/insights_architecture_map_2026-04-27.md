# Insights Pipeline Architecture Map: Critical Pedagogy Encoding

## Executive Summary

The Insights pipeline implements a "decomposing tenets of critical pedagogy" architecture that operationalizes Martha Caldwell's "identity as inquiry" pedagogical framework and Freire's distinction between banking and dialogic models of education. Rather than automating teacher judgment, the system reads student writing through four deliberate design choices:

1. **Synthesis-first architecture** (class reading before individual evaluation)
2. **Asset-framed classification** (ENGAGED as a structural non-flagging option)
3. **Equity-protective prompts** (validating AAVE, neurodivergent writing, lived experience)
4. **Anti-bias post-processing** (demoting tone-policing classifications)

This document maps how these pedagogical commitments are encoded in the codebase—not as add-ons, but as fundamental design choices in the pipeline's sequential stages.

---

## Architecture Overview

The production Insights pipeline has three parallel classification tracks that converge on a single student submission:

- **Track A (Binary Concern Detector)**: Isolated LLM call per student, no class context. Produces flagged concerns with confidence scores. **Never called in production** (`research_engine.py:247`); research-use only.
- **Track B (4-Axis Wellbeing Classifier)**: Per-student classification on CRISIS/BURNOUT/ENGAGED/NONE axes, with targeted CHECK-IN pass for ENGAGED students. Runs per-submission, no class context.
- **Track C (Generative Observation)**: 3–4 sentence free-form prose describing what the teacher might notice about each student. Runs WITH class context injected via synthesis-first reading.

The pipeline also generates a **class-level synthesis report** that surfaces emergent themes, contradictions, linguistic diversity (asset-framed), and relational harms visible only when reading the class as a community.

### Data Flow (Simplified)

```
Fetch submissions from Canvas
         ↓
Preprocess (translate, transcribe if needed)
         ↓
Quick Analysis (non-LLM signal matrix, sentiment, linguistic repertoire features)
         ↓
Class Reading [Stage 3.5] — read ALL submissions as community
         ↓
Per-Submission Coding [Stage 4] — READING-FIRST: free-form reading → structured extraction
         ↓
         ├─→ Track A: detect_concerns() [research only; skipped in production]
         ├─→ Track B: classify_wellbeing() → classify_checkin() [if ENGAGED]
         └─→ Track C: observe_student() [WITH class context]
         ↓
Synthesis Report (class-level themes, contradictions, outliers, concerns, linguistic assets)
```

**Critical detail**: Tracks B and C run SEQUENTIALLY after class reading is complete. Track A (binary concern detection) was designed to test whether class context helps accuracy, but found instead that it degrades binary classification performance. Therefore, Track A never runs in production, only in research comparisons.

---

## Component Map

### 1. Data Fetcher + Preprocessing
**File**: `src/insights/data_fetcher.py`, `src/insights/engine.py:_preprocess()`

Retrieves student submissions from Canvas API. Handles translation (via API) and transcription (Whisper) if enabled. Strips HTML, extracts text from attachments (PDFs, Word docs).

**Pedagogical relevance**: Early-stage detection that a submission is un-analyzable (blank, audio-only, image-only) prevents later stages from generating false data. Skip logic is diagnostic—tells the teacher specifically what was submitted and why the system can't analyze it.

### 2. Quick Analysis (Stage 3)
**File**: `src/insights/quick_analyzer.py`

Non-LLM signal matrix for each submission:
- Sentiment analysis (VADER + GoEmotions when available)
- Keyword-based concern signals (financial stress, health crisis, time pressure, etc.)
- Linguistic repertoire feature detection (AAVE, multilingual mixing, neurodivergent patterns)
- Assignment-connection assessment (does the submission address the assignment?)

**Data stored**: `QuickAnalysisResult` containing per-submission signal matrix, sentiment distribution, semantic clusters, concern signals list.

**Pedagogical encoding**: The "linguistic repertoire" object tracks features and marks them as **protected** (AAVE, multilingual, neurodivergent). These features are later used in class reading to **boost word budget** for students using non-standard English registers—ensuring their voices get represented proportionally.

### 3. Class Reading (Stage 3.5) — Synthesis-First Architecture
**File**: `src/insights/class_reader.py`, prompts in `src/insights/prompts.py:CLASS_READING_PROMPT`

The system reads ALL submissions as a unified community BEFORE evaluating individual students. The prompt instructs the LLM to:

- **ASSET READING**: What knowledge and capacities are students bringing?
- **THRESHOLD READING**: Where is productive difficulty? What confusion signals deep engagement?
- **CONNECTION READING**: How do students connect to each other? Where are relational moves (tone policing, essentializing, colorblind erasure) visible?

**Critical design choice**: Relational harms (e.g., Student A saying "be civil" in a class where Student B is expressing justified anger about racism) are **only visible when reading the class as a community**. Atomized reading makes them invisible.

**System addendum** (`prompts.py:51-53`):
> "Non-standard English, AAVE, multilingual syntax, and neurodivergent writing styles are valid academic registers—they are assets, not deficits."

**Output**: Free-form prose class reading (~1500 tokens). Injected into all per-student prompts in Track C.

### 4. Per-Submission Coding (Stage 4) — Reading-First Architecture
**File**: `src/insights/submission_coder.py:code_submission_reading_first()`

Two-pass architecture preserving qualitative richness:

**Pass 1 (free-form reading)**: LLM reads as a human reader would—no JSON, no rubric. Output: 3–5 sentences of what the LLM noticed. For long submissions, chunks are read separately and readings are merged to ensure the full text is considered.

**Pass 2 (structured extraction)**: LLM extracts structured fields FROM the Pass 1 reading. The reading grounds the extraction, preventing "slot-filling behavior" where the LLM invents content to satisfy a JSON schema.

**Data structure extracted**:
- Theme tags + confidence scores
- Notable quotes (with significance)
- Emotional register
- Personal connections, readings referenced, concepts applied
- **what_student_is_reaching_for** (synthesizes whether the student is trying to do the work)
- Free-form reading (preserved for inspection)
- confusion_or_questions

**Pedagogical encoding**:
- Verbatim quotes over paraphrases (preserves student voice)
- Emotional register read from raw text, not sentiment score (trusts teacher's reading eye)
- **what_student_is_reaching_for** reframes the question from "what did they do?" to "what are they trying to do?"—an asset-oriented framing
- Reading is stored unmodified, allowing teachers to inspect LLM reasoning

### 5. Track B: 4-Axis Wellbeing Classification
**File**: `src/insights/submission_coder.py:classify_wellbeing()` + `classify_checkin()`

**Two-pass architecture** (implemented 2026-03-29):

**Pass 0 (semantic prescan)**: LLM scans all chunks of text for sentences where the student describes their OWN personal circumstances (food insecurity, housing loss, sleep deprivation, family crisis, immigration threat, domestic violence, recent loss). Returns quoted sentences.

**Pass 1 (4-axis classification)**: LLM classifies submission as CRISIS, BURNOUT, ENGAGED, or NONE. Found sentences from prescan are foregrounded so they're not swamped by on-task content.

**Classification definitions** (from `prompts.py:WELLBEING_CLASSIFIER_SYSTEM`):

- **CRISIS**: Student's OWN current situation involves active danger/instability (housing loss, food insecurity, immigration enforcement, recent loss).
- **BURNOUT**: Student is depleted (exhaustion, overwork, caregiving burden). Material conditions breaking through and limiting capacity.
- **ENGAGED**: Student is doing the assignment, including passionate, angry, emotional engagement with difficult material. **AAVE, multilingual mixing, nonstandard English, and neurodivergent writing patterns are VALID ACADEMIC REGISTERS and indicate engagement.**
- **NONE**: Insufficient text or off-topic.

**Critical equity clause** (from same prompt):
> "IDENTITY DISCLOSURE ALONE IS NOT A WELLBEING SIGNAL. Naming a disability, neurodivergent identity, race, religion, immigration status, sexuality, or language background is intellectual disclosure—not a wellbeing signal by itself. A student who names their disability and says academic writing is hard is describing their relationship to the institution—this is ENGAGED."

**Pass 2 (CHECK-IN for ENGAGED only)**: If axis == ENGAGED, run targeted CHECK-IN at lower temperature (0.3) to surface subtle self-disclosure (exhaustion, time pressure, personal difficulty) that a teacher might want to note. Requires quotable self-reference; only triggers if register shift suggests the student is revealing something about their state.

**Data returned**: `{axis, signal, confidence, prescan_signals, [checkin_flag, checkin_reasoning if ENGAGED]}`

**Pedagogical encoding**:
- **ENGAGED is a structural non-flagging option**. It's not "no concern detected"—it's "the student is doing the work, with all the emotional intensity that entails." This reframes righteous anger about injustice, lived experience testimony, and neurodivergent writing as markers of engagement, not warning signs.
- The prescan + classifier architecture ensures students aren't falsely flagged because their writing is about disturbing content (course material on violence, racism, colonialism) rather than about their own crisis.

### 6. Track A: Binary Concern Detection (Research-Use Only)
**File**: `src/insights/concern_detector.py:detect_concerns()`

Separate LLM call per student, no class context. Designed to test whether relational context helps binary classification, but found to degrade accuracy (`research_engine.py:247` comment: "detect_concerns never called in production").

**Anti-bias post-processing** (`concern_detector.py:_check_bias_in_output()`):

Scans LLM's `why_flagged` explanation for tone-policing markers and subject-matter confusion:

```python
_BIAS_MARKERS = re.compile(
    r"\b(aggressive|too emotional|overly emotional|hostile tone|"
    r"angry rhetoric|threatening|confrontational|too angry|"
    r"irrational|hysterical)\b", re.IGNORECASE
)
```

**Logic**: If the flagged passage contains structural critique keywords AND the LLM used tone-policing language, add warning and demote confidence by 0.3.

**Subject-matter detection**: If LLM is flagging because the passage discusses rape, violence, genocide, etc. AS COURSE MATERIAL (not because student is in distress), demote confidence by 0.4 and flag as "LIKELY COURSE CONTENT (not student distress)."

**Output**: `List[ConcernRecord]` with confidence scores. Only concerns with confidence >= 0.7 survive (line 230).

### 7. Track C: Generative Observation
**File**: `src/insights/submission_coder.py:observe_student()`

Generates 3–4 sentence observation for one student, given:
- Submission text
- Class context (from Stage 3.5 class reading)
- Assignment prompt
- Teacher lens (from Stage 4 coding: what the student is reaching for)
- Optional trajectory context (longitudinal pattern from prior submissions)

**System prompt** (`prompts.py:OBSERVATION_SYSTEM_PROMPT`):
> "You are NOT a grading system, a concern detector, or an alert generator. You are a reader sharing what you noticed. Write as a colleague, not a system."

**Output**: Free-form prose with model preamble stripped (regex removes "Okay, here are my observations..." patterns).

**Pedagogical encoding**: Observation is written to a teacher colleague, not to a system. It preserves uncertainty ("I notice...," "The student seems..."), avoids diagnostic framing, and treats the student as an agent with intentions ("reaching for," "grappling with").

### 8. Class-Level Synthesis
**File**: `src/insights/synthesizer.py`

Aggregates all per-student coding records into a single report. Extracts:
- **Emergent themes** (across students, grouped by frequency)
- **Contradictions** (e.g., some students say X, others say -X; marks both as valid)
- **Outliers** (unusual approaches, surprising insights)
- **Concerns** (aggregated from concern records)
- **Linguistic diversity** (counts asset labels across class, e.g., "8 students: code-switching," "5 students: neurodivergent writing style")
- **Focus areas** (where should the teacher pay attention next?)

**Tier-differentiated output**:
- Lightweight: structured, template-constrained
- Medium: all records + teacher context, interpretive
- Deep: full context + pedagogical philosophy

---

## Data Flow Narrative: One Student Submission

### Example: Maria's submission on intersectionality

1. **Fetch** (Stage 1): Canvas retrieves Maria's text response, metadata.
2. **Preprocess** (Stage 2): HTML stripped, text extracted.
3. **Quick Analysis** (Stage 3): 
   - Sentiment: positive (VADER 0.65, GoEmotions: joy 0.72, pride 0.58)
   - Linguistic repertoire: **code-switching** (English-French mixing), **ESL features** (marked as protected)
   - Assignment connection: 94% overlap with prompt (discussing intersectionality)
   - Concern signals: none
4. **Class Reading** (Stage 3.5): 
   - System reads all 25 students' submissions
   - Notices Maria's cross-cultural perspective, comparison between Senegal and US
   - Notices how Maria's lived experience validates Crenshaw's theory
   - Notes relational move: other students cite theory abstractly; Maria grounds it in family experience
5. **Coding** (Stage 4):
   - **Pass 1 (reading)**: "Maria powerfully connects intersectionality to lived experience. Starting with her grandmother in Dakar is insightful—not forcing a Western framework onto a different context, but showing the phenomenon is recognizable across cultures. Her move from 'this is a theory' to 'this is what my family lives through' is a profound statement of validation and recognition..."
   - **Pass 2 (extraction)**:
     - theme_tags: ["Cross-cultural relevance of intersectionality," "Lived experience as validation of theory," "Critique of Western-centric perspectives"]
     - emotional_register: "passionate|personal|reflective"
     - personal_connections: ["family experiences (grandmother in Dakar, mother in American schools)"]
     - what_student_is_reaching_for: "Maria is demonstrating sophisticated understanding of intersectionality, moving beyond definitions to connect it to concrete lived experiences across cultural contexts, while offering thoughtful critique of course readings' scope"
     - linguistic_assets: ["code-switching," "multilingual repertoire", "cross-cultural framing"]
6. **Track B (Wellbeing)**:
   - Prescan: no personal crisis signals
   - Classification: ENGAGED (passionate engagement with material, drawing on lived experience)
   - CHECK-IN: skip (not needed for ENGAGED students unless they show subtle distress signals)
   - confidence: 0.92
7. **Track C (Observation)**: 
   - "Maria is demonstrating a sophisticated grasp of intersectionality—not as abstract theory, but as lived reality. Her move from 'this is what my family experiences' to a critique of the course readings' Western focus is intellectual work that should shape what the class reads next. She's asking the teacher to see her knowledge as valid and her critique as pedagogically productive."
8. **Synthesis** (class-level):
   - Theme: "Grounding theory in lived/family experience" (5 students)
   - Supporting quotes: Maria's quote, Talia's quote, James's quote
   - Linguistic asset: "code-switching" (+1 count for Maria)
   - Relational note: "Maria and Jamal both critique Western-centrism; their critiques should be read together, not in isolation."

**What happens if Maria's writing had been in pure AAVE without code-switching?**
- Quick Analysis still marks it as protected (asset, not deficit)
- Wellbeing classifier sees the system instruction: "AAVE... are VALID ACADEMIC REGISTERS and indicate engagement"
- Prescan would still find personal crisis signals (if present)
- Observation would still frame her voice as intellectual work
- Class reading would still position her voice as belonging, not aberrant

---

## Design Choices Encoding Pedagogical Commitments

### 1. Synthesis-First Architecture vs. Banking Model Atomization

**Freire's banking model**: An authoritative system deposits coded data into students, then aggregates individual responses to understand a class. Students are treated in isolation; relational harms (tone policing, essentializing) are invisible.

**Insights synthesis-first**: The system reads the class as a dialogic community BEFORE individual evaluation. Code locations:

- `class_reader.py:generate_class_reading()` generates class-level reading BEFORE per-student coding (pipeline Stage 3.5 before Stage 4)
- Class reading is then injected into every per-student prompt (see `submission_coder.py:_code_lightweight()` line 571, `_code_full()` line 668, `code_submission_reading_first()` line 768: `class_context_block`)
- `concern_detector.py:182-186` injects class context into concern detection prompt to make relational harms visible
- `synthesizer.py:_summarize_themes()` aggregates individual records back into class-level contradictions (e.g., "Side A (12 students) say X; Side B (8 students) say -X")

**Result**: Relational dynamics are named in the synthesis report, not erased. A student's voice is read in the context of the class's conversation, not in isolation.

### 2. Asset-Framed ENGAGED Slot in 4-Axis Classifier

**Banking model logic**: Flag students who deviate from institutional norms (emotional writing, non-standard English, angry tone, lived-experience grounding).

**Critical pedagogy reframing**: Caldwell's "identity as inquiry" values students' situated knowledge and emotional engagement. The ENGAGED axis is specifically designed as a structural slot for "NOT flagging the student" while honoring their intellectual engagement.

Code evidence:

- `submission_coder.py:classify_wellbeing()` returns `axis: "ENGAGED"` for students doing the assignment with "passionate, angry, emotional, or confrontational engagement" (prompts.py)
- The prescan + classifier architecture in `classify_wellbeing()` ensures students discussing racism/violence/poverty AS COURSE MATERIAL aren't falsely classified as in crisis
- `classify_checkin()` (line 1090) is called ONLY for ENGAGED students, and is designed to surface subtle signs a teacher might want to note, not to flag them as problems
- `research_engine.py:668` shows the CHECK-IN pass is optional for ENGAGED students; they are NOT automatically escalated

**What the code refuses**: Students using AAVE, multilingual mixing, or neurodivergent writing patterns are NOT downweighted in wellbeing classification. The prompt explicitly states these are "VALID ACADEMIC REGISTERS and indicate engagement" (prompts.py).

### 3. Equity-Protective System Prompts

**Problem addressed**: Standard LLM prompts encode institutional tone-policing ("emotional," "aggressive," "too angry"). They conflate course material (students discussing violence as assigned content) with student distress.

**Prompt locations and explicit language**:

1. **Core system prompt** (`prompts.py:26-41`):
   > "Political urgency about injustice is appropriate academic engagement, not a concern."
   > "Never confuse disturbing SUBJECT MATTER with student WELLBEING concerns."

2. **Class reading system addendum** (`prompts.py:50-53`):
   > "Non-standard English, AAVE, multilingual syntax, and neurodivergent writing styles are valid academic registers—they are assets, not deficits."

3. **Wellbeing classifier system** (prompts.py, approx line 1031-1035):
   > "Righteous anger about injustice is APPROPRIATE engagement, not a concern."
   > "AAVE, multilingual mixing, nonstandard English, and neurodivergent writing patterns (fragmented, nonlinear, associative) are VALID ACADEMIC REGISTERS."
   > "IDENTITY DISCLOSURE ALONE IS NOT A WELLBEING SIGNAL."

4. **Observation system prompt** (prompts.py:1753-1765):
   > "You are NOT a grading system, a concern detector, or an alert generator. You are a reader sharing what you noticed."

5. **Prescan system prompt** (prompts.py, approx line 208):
   > "Find any sentence where the student describes their OWN current personal circumstances...specifically food insecurity, housing instability, sleep deprivation...Do NOT flag course discussions of these topics."

**Operational effect**: When the wellbeing classifier reads a passage where a student writes passionately about racism they experience, the system prompt prevents it from marking passion/anger as warning signs. Instead, the prescan/classifier logic looks for the signal: "Is the student describing their OWN current circumstances, or discussing course material?" If the latter, no prescan signal appears, and the classifier reads the passion as engagement.

### 4. Anti-Bias Post-Processing (Track A)

**Problem**: Binary concern classifiers can encode teacher bias (tone-policing, racial bias, ableism).

**Solution** (`concern_detector.py:97-138`): After LLM generates concern flags, scan the `why_flagged` explanation for bias markers:

```python
_BIAS_MARKERS = re.compile(
    r"\b(aggressive|too emotional|overly emotional|hostile tone|..."
)
```

**Logic**:
1. If LLM used tone-policing language AND the flagged passage contains structural critique keywords, demote confidence and prepend warning: "⚠ POSSIBLE MODEL BIAS: The model characterized this student's tone negatively. The passage appears to contain structural critique, which is appropriate academic engagement, not a concern."
2. If LLM is flagging course content (detects phrases like "may be triggering," "discusses rape," "mentions violence"), demote confidence and flag: "⚠ LIKELY COURSE CONTENT (not student distress)."

**Data structure**: Concerns with confidence < 0.7 are dropped entirely (line 230). Bias-warning-flagged concerns have confidence reduced by 0.3–0.4.

**Why this matters for research**: This is why Track A (binary concern detection) never runs in production. Testing found that class context actually **worsens** binary classification (makes the model more likely to flag students as concerning based on relational dynamics rather than actual crisis signals). The anti-bias post-processing is necessary but imperfect—better to not run the classifier at all than to run it with relational context and then try to patch the bias afterward.

---

## What the Architecture Refuses (Decomposing Banking Model)

The pipeline's design choices specifically **reject** banking-model patterns:

### Refuses: Student as Information Source, Teacher as Aggregator
**Instead**: Reads class as dialogic community, then individual within community. Class reading names relational dynamics (tone policing, essentializing) that only appear when students are read together.

### Refuses: Sentiment Score as Proxy for Engagement
**Instead**: Reads emotional register from the student's own text. Sentiment scores are shown to the LLM with explicit caveats: "⚠ Signal misreads AAVE, ESL writing, neurodivergent patterns—read tone directly from text." Sentiment is withheld entirely (marked "[SUPPRESSED]") when feature detection finds protective markers.

### Refuses: Non-Standard English as Deficit
**Instead**: Explicitly frames AAVE, multilingual mixing, neurodivergent writing as "valid academic registers" and "assets." Class reading boosts word budget for students with protected linguistic features.

### Refuses: Anger About Injustice as Pathology
**Instead**: Explicitly states "Political urgency about injustice is appropriate academic engagement, not a concern" and "Righteous anger about injustice is APPROPRIATE engagement."

### Refuses: Lived Experience as Personal Problem
**Instead**: Caldwell's "identity as inquiry" frame means the system distinguishes "naming a disability/race/language is intellectual disclosure" from "expressing crisis." The prescan and CHECK-IN logic surface genuine distress while treating identity disclosure and experience-grounding as evidence of engagement.

### Refuses: Slot-Filling JSON Generation
**Instead**: Reading-first architecture (Pass 1 free-form, Pass 2 extraction) ensures the model reads qualitatively before structuring. This prevents the LLM from inventing content to satisfy schema slots (e.g., attributing concepts to a student based on the prompt rather than the actual text).

### Refuses: Atomized Evaluation
**Instead**: Class reading and synthesis report make relational harm visible. A student's voice is read in context of the class's conversation, not in isolation.

---

## Load-Bearing Implementation Details

### The ENGAGED Flag: Structural Non-Flagging

The four-axis classifier returns `axis: "ENGAGED"` not because the system detects engagement (which is hard to operationalize), but because it uses **prescan + classifier logic** to rule out CRISIS and BURNOUT:

```python
# From classify_wellbeing() — prescan finds personal crisis signals
found_signals = _prescan_for_personal_signals(backend, submission_text)

# If prescan found nothing, and classifier doesn't detect burnout material
# conditions (work schedule, sleep loss, caregiving), then axis = ENGAGED
```

**Result**: Any student whose writing doesn't contain explicit personal crisis/burnout signals is classified as ENGAGED, even if they're quiet, even if they're brief, even if they're writing in AAVE or fragmented neurodivergent style. ENGAGED is not a positive claim about engagement; it's a structural refusal to flag students without explicit distress signals.

The CHECK-IN pass (only for ENGAGED) then optionally surfaces subtle distress signals within engaged writing—"exhaustion showing through despite engagement," not "this student is in crisis."

### Reading-First Prevents Hallucination

From `submission_coder.py:737-927`:

```python
def code_submission_reading_first():
    # Pass 1: Free-form reading (no JSON, no schema)
    # For long submissions, chunk + merge readings
    readings = []
    for chunk in chunks:
        chunk_reading = send_text(backend, p1_prompt, ...)
        readings.append(chunk_reading)
    reading = "\n\n".join(readings)
    
    # Pass 2: Extract structured fields FROM the reading
    # The reading grounds extraction, preventing slot-filling
    p2_prompt = CODING_READING_FIRST_P2.format(
        student_name=student_name,
        free_form_reading=reading,
        submission_text=p2_text,
        lens_fragment=lens_fragment,
    )
    parsed = parse_json_response(send_text(backend, p2_prompt, ...))
```

**Why this matters**: If you do JSON-first (ask for structured fields directly), the 8B model fills slots based on the assignment prompt rather than what the student actually wrote. If you do reading-first (read what you notice, then extract from the reading), the reading anchors the extraction. For "concepts_applied," Pass 1 reading mentions "the student uses X concept," then Pass 2 extracts it from there, preventing hallucination.

Data evidence: `reading_first_comparison.json` shows that reading-first approach extracts richer quotes and more accurate personal_connections than standard approach.

### Prescan + Classifier Prevents False Positives

From `submit_coder.py:1009-1087`:

```python
def classify_wellbeing():
    # Pass 0: prescan across all chunks for personal circumstances
    found_signals = _prescan_for_personal_signals(backend, text)
    
    # Pass 1: classifier with found sentences foregrounded
    signal_prefix = (
        "NOTE: The following sentence(s) from this student's submission "
        "appear to describe their own personal circumstances:\n"
        f"{quoted}\n"
        "Even a single such sentence is sufficient for CRISIS or BURNOUT..."
    )
    prompt = WELLBEING_CLASSIFIER_PROMPT.format(
        signal_prefix=signal_prefix,
        submission_text=classifier_input,
    )
```

**Why this matters**: A student writing about genocide, slavery, or police violence AS COURSE MATERIAL might score high on keyword-based danger signals. The prescan-classifier architecture says: "Are these keywords about the STUDENT's circumstances, or course material?" If prescan finds personal circumstance signals, they're foregrounded. If not, the classifier reads the content as engagement with course material, not personal distress.

---

## How Class Context is Loaded vs. Withheld

### Class Context Is Loaded:

1. **Per-student coding** (Track C observation): `submission_coder.py:_code_lightweight()` and `_code_full()` both include `class_context_block` in prompts (lines 571, 668)
2. **Concern detection** (research Track A): `concern_detector.py:182-186` injects class context to make relational harms visible
3. **Class reading synthesis**: `synthesizer.py` reads all records together, surfaces contradictions and relational patterns

### Class Context Is NOT Loaded:

1. **Wellbeing classification** (Track B): `classify_wellbeing()` runs on raw submission text without class context. This is intentional—relational context makes students more likely to be flagged (e.g., if the class is discussing racism and one student is quiet, relational context might make the system think they're withdrawn when actually they're listening). The prescan + classifier logic is sufficient.
2. **Binary concern detection** (Track A, research only): Despite having the capability to inject class context (`concern_detector.py:182-186`), Track A is never called in production because testing showed class context **worsens** binary classification accuracy (makes the model over-flag students based on relational position rather than actual distress).

---

## Open Questions / Authorial Knowledge Needed

1. **March 2026 refactor**: The codebase shows recent changes to wellbeing classification (prescan + classifier as of March 29, 2026). Were there false positives in the earlier single-pass classifier that motivated the two-pass redesign?

2. **Track A production decision**: The comment "detect_concerns never called in production" (research_engine.py:247) suggests a deliberate decision not to deploy binary concern detection. What evidence led to that decision? Was it the bias post-processing being insufficient, or the class context actually hurting accuracy, or both?

3. **ENGAGED vs. observational framing**: The pipeline generates observations for ENGAGED students the same way as CRISIS/BURNOUT students. Is there any downstream filtering that deprioritizes ENGAGED observations in the teacher's view, or are they treated equally?

4. **Reading-first deployment timeline**: The `code_submission_reading_first()` function is called from `research_engine.py:543`, but I don't see it called from production `engine.py`. Is reading-first currently research-only, or has it been integrated into production as of April 2026?

5. **Linguistic asset labels**: The `linguistic_assets` field in `SubmissionCodingRecord` is populated from `quick_summary.linguistic_repertoire.asset_labels` (submission_coder.py:544). What are the full set of possible labels (beyond "code-switching," "multilingual repertoire")? Are they auto-generated from feature detection or hand-coded?

6. **Identity disclosure logic**: The wellbeing classifier prompt explicitly says "IDENTITY DISCLOSURE ALONE IS NOT A WELLBEING SIGNAL." In practice, how often does the prescan pick up a student naming their disability/race/language as a "personal circumstance signal"? Is there a post-prescan filter that distinguishes "I have ADHD" (identity) from "I have ADHD and can't sleep" (wellbeing)?

---

## Data Files & Checkpoints

The demonstration data in `data/demo_baked/` shows the architecture in action:

- **`ethnic_studies_gemma12b_mlx_class_reading.json`**: Example class reading output (asset/threshold/connection reading)
- **`reading_first_comparison.json`**: Side-by-side comparison of standard vs. reading-first coding on same student submissions (shows reading-first extracting richer quotes and detecting lived-experience grounding more reliably)
- **`synthesis_first_*.json`**: Outputs of synthesis report generation at different tiers (lightweight, medium, deep)

The `reading_first_comparison.json` is particularly valuable for the paper's Methods section—it provides concrete evidence that reading-first architecture surfaces student voice and pedagogical engagement better than JSON-first prompting.

---

## Summary for Methods Section

The Insights pipeline architecture encodes critical pedagogy commitments through:

1. **Synthesis-first design**: Class reading before individual evaluation, making relational dynamics visible
2. **Asset framing**: ENGAGED as non-flagging structural option; linguistic diversity explicitly valued
3. **Equity-protective prompts**: System-level instructions validating AAVE, lived experience, neurodivergent writing as academic registers
4. **Anti-bias post-processing**: Detecting and demoting tone-policing and subject-matter confusion in flagged concerns
5. **Reading-first coding**: Free-form observation before structured extraction, preventing hallucination and preserving student voice
6. **Prescan + classifier logic**: Distinguishing student crisis from course material engagement

Rather than automating teacher judgment, the system scaffolds it: reads the class as a community, preserves student voice verbatim, makes relational harms visible, and refuses to flag students for using protected linguistic registers or expressing justified anger about injustice.

