---
title: "Output Format as Architectural Determinant of Demographic Bias in AI-Powered Educational Welfare Classification"
keywords: "algorithmic bias, community cultural wealth, deficit model, critical AI, student wellbeing, automated assessment"
---

> **Status: under active revision (as of 2026-09-13).** This draft reflects the analysis before a round of framing corrections. Do not cite or treat as final. Known issues currently being addressed:
> - The race→disability framing in §V.B overstates a clean handoff between separable groups; the deficit reading relocates to the least-protected axis *within* multiply-marginalized subjects (see the S028/S029 case), not between single-axis students.
> - The AAVE/linguistic-justice framing is being cut or reworked: the false positives are content-based (what a student wrote about), not language- or dialect-based, and the current text implies otherwise.
> - The "normative gravity" claim needs tightening to state explicitly that it describes against-instruction reproduction specific to binary classification, not a general causal mechanism.
> - Output format (binary vs. open) and discursive function (classification vs. description) are confounded in the current data; the revision needs to frame this as an open research question rather than obscure it.
>
> Full revision context: `CLAUDE.md` in this directory.

## Abstract

A yes-or-no verdict from an AI system activates deficit-based frameworks — reading students through what they lack rather than what they carry — even when its own reasoning argues otherwise. I built an AI wellbeing classifier for my Ethnic Studies courses at a Hispanic-Serving Institution. Testing on 46 AI-generated essays representing patterns from my classes, the system reasoned that students of color and neurodivergent writers applying lived experience to coursework were analytically engaged, then flagged them as wellbeing concerns in the same output. Standard bias-reduction engineering failed: adding equity protections naming African American Vernacular English (AAVE), neurodivergent self-disclosure, and lived experience as non-concerns reduced overflagging of some students but generated new false positives on others, and the binary false-flagged a synthetic neurodivergent profile 24 of 24 times. Switching to generative observation — open-ended description instead of binary verdict — eliminated false positives across two AI model families and 28 test runs. This approach addresses the deficit-verdict mechanism that calibration cannot reach, including patterns not yet named in equity-protective instructions. A subtler asymmetry in how the AI describes students remains; I address it in §V.B. The architecture is in active use.

---

# I. Introduction

> "Her passion is understandable and appropriate."

The above statement was written by an AI-powered wellness tracker about "Destiny Williams," a student in a synthetic corpus, right before it flagged her anyway. The wellbeing tracker consisted of a binary classifier: it instructed an AI model running locally on my own computer to review students' work and raise a flag (CONCERN) if someone mentioned crisis conditions or other concerns that I wanted to be responsive to. I built a synthetic corpus of essays, which I used to test the classifer before deploying it in my own Ethnic Studies classes. However, the classifier tended to conflate lived experiences of oppression with crisis signals: producing disporportionate false positives on "equity-critical" essays I designed as proxies for students in my classes. The AI model *could* be prompted to read students' work through Ethnic Studies frameworks and recognize embodied and community knowledge as analytical *assets* (Yosso, 2005) – its own, self-contradictory rationales demonstrated that. But when presented with a binary choice — flag the student or not — it collapsed into a deficit-based framework. 

The initial test run produced eight flags — one edge case (a late night submission that cut off mid-sentence) and seven false positives In three of the seven false positives, which included Destiny Williams, the model contradicted itself by flagging the student while arguing they were actively engaged. I followed the standard computer science response to demographic bias in educational AI: iterative calibration (Boateng & Boateng, 2025; Chinta et al., 2024; Hoffmann, 2019; Helm et al., 2024; Selbst et al., 2019). Adjust the classifier, add protective language, tune confidence thresholds. I calibrated the classifer for Ethnic Studies classes in which life experience and community knowedge were built into every assignment. But reducing false positives on AAVE and ESL students made the system flag a neurodivergent student, instead, who previously *had not* been flagged. Switching to a larger model produced more false positives within the same model family (Gemma, chosen in initial system tests for equity-critical performance). I was playing a game of whack-a-mole: every patch created a new problem.

How does the same model produce an asset-aware reading and a deficit verdict in a single response, and why specifically to students whose writing applies community cultural wealth? What is it about binary classification that pulls models towards a dominant analytical framework, even despite explicit prompting otherwise? Why does it do something different with more open output format afforded by it's rationale? And why does the deficit framing wander from race to disability upon calibration? This is not simply, "AI encode normative social biases that represent statistical distributions in it's training data." The model's logical process route through distinct analytical frameworks and *intellectual geneologies* when told to respond in different output formats. 

The binary classifer had a bias problem, and even explicit anti-bias engineering failed to resolve it. I did not solve it with calibration, but by changing the output format. I built a "generative observation" layer: rather than evaluating students or passing judgements, it was asked to observe what was there, what the student was reaching for, and whether the student mentioned certain concerns that should be surfaced for the teacher. The deficit language disappeared. The generative observation layer also provided data I used to design complementary multi-axis classifier (CRISIS / BURNOUT / ENGAGED / NONE). The "ENGAGED" flag is not passed anywhere in Autograder4Canvas: it is simply a structural slot for the model to avoid flagging students applying life experience to course content. 

I do not claim that generative observation or open output formats eliminate bias: they surface it in a way that can be navigated differently, with its own risks and failure modes. Open formats do appear to afford greater flexibility in determining whose analytical frameworks the model can bring to bear in its responses. 

The issue is architectural: a matter of overall system design, not incremental fixes. Iterative calibration of binary classifiers — is a *configurable failure mode but not a configurable failure*: calibration can shift who algorithmic bias lands; it cannot eliminate the harm. 


The differential tracks the scale of existing bias interventions: canonical axes of oppression (race and language vs. disability) shape who falls through the gap. The paper proposes a mechanism behind this: compression-based format routing. The binary format's task structure forces a single-bit verdict that overrides the model's own asset-aware reasoning. This activates a collapse the model's frame of reference towards what I call *normative gravity*: probabilistic systems pull toward the statistical center, making positional specificity outside of normative distributions costly. Format change is the escape hatch: it makes it more possible to ask different questions that navigate the margins of the statistical distributions in AI training data. Compression-activated bias and normative gravity are design parameters. 

---

# II. Framework

## II.A — Compression Politics and Normative Gravity

This paper's findings demonstrate that output format is an activation function for bias in AI systems. The working hypothesis is that binary output is a "worst offender" of a more general case: compression. A binary format requires the model to reduce a multi-dimensional student reading to a single bit. This intensifies a phenomenon I call "normative gravity": probabilistic systems pull toward the center of statistical distribution, making positional specificity costly — what makes an Ethnic Studies student's political testimony, or a writer's code-switching between African American Vernacular English and academic prose, harder for the AI to recognize as intellectual rigor than a conventional essay in Standard Academic English would be. This structurally mirrors bell hooks' (1984) centers-and-margins theory: the largest statistical distributions in AI training data reflect normative assumptions and ideologies. This systematically suppresses positional specificity, or what hooks calls the view from the margins, which includes knowledge from marginalized communities. That knowledge is both harder to surface and harder to maintain.

Routing machine cognition to frameworks from marginalized communities is possible where the material exists in training data. Autograder4Canvas's architecture works in part by activating Yosso's (2005) concept of community cultural wealth from Chicano/a/x studies in AI cognition. However, normative gravity *pulls* the routing at all times: maintaining those positions requires continuously counteracting system defaults. AI architectures reward efficiency and productivity while producing statistically likely (generic) outputs: positional specificity easily falls through the cracks. Moreover, binary output structurally *overrides* positional specificity even when protected in the prompt itself, collapsing critical frameworks into system defaults. D'Ignazio and Klein (2020) name the general principle: data systems embed power, and standpoint — whose position the system is optimized from — is a design choice with distributional consequences. Every calibration intervention operated above the compression step — on prompt content, post-processing, or classifier selection — never on the routing mechanism the format instantiates.

## II.B — Deficit framing of identity and the architecture of nonrecognition

Yosso's (2005; see also Tuck, 2009) account of community cultural wealth inverts the question Bourdieu's (1986) symbolic capital asks: not what students of color lack, but what dominant institutions fail to recognize. Bourdieu maps cultural competencies against the currency dominant institutions reward, theorizing the symbolic mechanics of structural inequality. Yosso's counter-narrative methodology inverts the direction, centering the knowledge and cultural repertoires held within communities of color rather than the gaps dominant assessment criteria record. Yosso names six types of community assets: aspirational capital, familial capital, social capital, navigational capital, linguistic capital, and resistant capital. This paper draws on the former two specifically, which the binary classifier's reading-frame systematically misrecognizes. Yosso's framework makes the epistemic structure of the binary classifier's contradictory output legible as a statistical distribution of deficit-based frameworks in training data.

Destiny Williams's writing in the synthetic corpus is a paradigmatic instance of what Yosso names resistant capital. She expresses anger about social problems, developing an argument about political consciousness: she is doing the analytical work the Ethnic Studies assignment asked for. The model's contradiction is not a reading error, but a classification architecture that can hold resistant capital up until the moment at which machine cognition must resolve it's response to a single bit. Other students in the corpus — Yolanda Fuentes and Ingrid Vasquez — instantiate linguistic capital and were likewise flagged. <!-- REVISION NOTE (2026-06-01): Vasquez tested in one configuration only (Apr 26 single-run baseline); absent from systematic multi-run tests. Consider citing only Fuentes here, or add a qualifier. --> In each case, the AI model argued that the students were drawing on lived experience to do real analytical work, and then the binary flag collapsed that nuance back into a deficit frame. The three cases are not random misclassifications: when multiple iterations of equity-hardening finally cleared these three students, the system started flagging a neurodivergent student. Intersecting axes of oppression (Crenshaw, 1989) most vulnerable to deficit framing in training data — disability in particular — directly shape how compression routes machine cognition through available training-data frameworks.

## II.C — Banking-model architecture and the dialogic alternative (Freire + hooks)

Binary output formats concentrate evaluative authority; descriptive observation formats disperse it in both semantic field and social relationships. Freire's (1970) critique of the banking-model of education — knowledge deposited into students by an authoritative actor — has a structural analog in atomized binary classification. The classifier owns the verdict, the student's writing is processed rather than heard, and the relation is unidirectional. Yet neither is the teacher the fixed source of authority – nor, for that matter, is the developer or even AI model. Rather, authority sits within normative assessment standards themselves, enacted computationally through statistical distributions that encode racialized epistemic hierarchies and entrenched architecturally by requesting a binary output format. Where Freire (1970) describes the banking model as epistemological oppression, the paper locates its operational instance in the output format that makes single-bit resolution mandatory. In AI systems, compression activates bias that overrides the model's own qualitative analysis.

Normative gravity is functionally parallel to bell hooks' (1984; 1989) centers and margins. The difference is computational: the center of normative gravity is the statistical representation of training-data knowledge. That statistical distribution pulls towards a "default" that is highly racialized and gendered, but which reproduces epistemic hierarchies even while presenting itself as neutral. From the vantage of the statistical center, community cultural wealth is from the center; meanwhile, binary output makes the view from the margins structurally unavailable. The paper's design principle is not "fairer classification" — it does not calibrate the verdict more accurately. It eliminates the verdict-producing structure that makes calibration the intervention of choice. A teacher who reads students as agents needs a system that reads them the same way: the architectural commitment is what engaged pedagogy (hooks 1994) in machine form requires.

## II.D — Structural racism and the format-routing layer (Bonilla-Silva → Benjamin → this paper)

The binary classifier demonstrated AI's equivalent of color-blind racism (Omi and Winant 1994). Whiteness operates as legal property in educational institutions, determining access, what knowledge gets recognized, and whose language gets institutionalized (Ladson-Billings & Tate, 1995). AI training distributions accumulate that history as statistical weight; binary format routes through it, making the property logic operational within a color-blind register. For Bonilla-Silva, racially patterned outcomes are produced through institutional structures rather than through individual racist intent. Ruha Benjamin's *Race After Technology* (2019) extends this framework into algorithmic systems. She terms this phenomenon the New Jim Code: technologies reproduce racial hierarchies through the architectures they instantiate. The binary output problem names a specific mechanism of algorithmic bias in AI systems architectures: the epistemic hierarchies characterize in the training data, but the output format operationalizes them differently. Benjamin's diagnostic typically lands at training data, model selection, or deployment context — not the output format that routes between classification axes. This paper specifies the architectural location one level below: format routing, the output-format requirement that determines which dimensions of asset-aware prompt content survive the compression to a single bit.

Bonilla-Silva names the structural property; Benjamin locates it in algorithmic systems; Tanksley (2024) extends it to educational AI specifically. She theorizes anti-blackness as a default algorithmic logic and develops critical race algorithmic literacy (CRAL) as a pedagogical approach that gives students a framework for navigating it. This paper identifies its operational mechanism in AI systems essential for building what Tanksley calls counter-technologies. The three layers of explicit anti-bias engineering that fail to clear minoritized students provide evidence of a structural mechanism that counteracts deliberate, sustained interventions designed within the intersecting axes of oppression that shape classrooms. AI produced rationales contradicting its own flags, demonstrating that the mechanism exceeds the model's own deliberation. The problem appears to be architectural in LLM design: output format activates bias in ways that fine-tuning and more inclusive training data may not resolve — those interventions could theoretically shift normative gravity's center but cannot address the output format mechanism that enforces it. 

"Racism without racists" applies directly: the binary classifier's tendency to overflag minoritized students is architecturally produced, and neither designer intent nor calibration corrections are the right unit of analysis. The solution is format change: the unit of analysis must operate at the architectural layer where the outcome is determined.

---

# III. Situating the Research: Setting, Corpus, and Method

## III.A — Institutional context

I am a white, settler, transgender, neurodivergent woman; I taught full-time at an HSI community college Ethnic Studies program and built Autograder4Canvas to help me navigate a hostile and disabling working environment. That positionality shapes what I can see and what I risk missing. The analytical frameworks I draw on — community cultural wealth, language justice, DisCrit — were built by and for communities of color and disability communities. I use them as an educator and allied researcher whose family lineage is embedded in critical race and ethnicity pedagogy (Caldwell, 2012; Caldwell & Frame, 2016), not as a member of those communities. Because I was actively teaching at the time, the synthetic corpus was LLM-generated and analyzed with LLM assistance. This was the fastest viable path to a FERPA-compliant test so I could assess and calibrate the build while carrying a full teaching load, before deploying the system in live classes. The equity-critical patterns it encodes — AAVE, neurodivergent self-disclosure, resistant capital — are approximations of patterns I see among my students, not authoritative representations. The corpus was a calibration floor — an alternative to tuning with real student data alone. Live student writing was always the intended site of refinement.

This research happened in California community-college Ethnic Studies courses in Spring 2026, where even progressive, anti-racist policies create racist impacts when implemented within carceral and white supremacist institutional structures (Shange, 2019). New California education policy added Ethnic Studies as a graduation requirement, the implementation of which placed every kind of student who moves through the community college setting into groups of 49 and asked them to talk about race. I was responsible for a teaching load of ~200 students per semester, in a two-person department, with pressure to scale further to meet the policy's demand. The 2025–2026 academic year intensified those conditions: escalations in federal immigration enforcement including coordinated ICE raids in the local area in January, while the Department of Education moved against diversity, equity, and inclusion programming at the federal level. Students entered Ethnic Studies classrooms amidst simultaneous political crisis and academic obligation; instructors carried the contradiction of teaching a state-mandated curriculum for a field that was itself born from student strikes, enacted in carceral, punitive institutions.

The implementation of new graduation requirements was designed for an imagined "default" student: the central problem interrogated by critical whiteness and post-racial discourse studies (Annamma et al., 2017; Leonardo, 2009; Bonilla-Silva, 2018). Ethnic Studies may be for everyone, but in this move, it stopped being for students of color in particular. Ethnic Studies became a required course within a wider social context of political turmoil, emboldened right-wing extremism, and (trans)misogyny on a scale that I, as a Southern transplant, was unprepared for. I was doing behavioral management, triage, and on good weeks, grading. But that is not the same thing as teaching. When it became clear that the institution would be unable to collaborate on solutions, I designed my own.

Autograder4Canvas was built on a shift in my pedagogy: a framework I termed "Ethnic Studies is a Strike." This approach was inspired by a class digital archive project on the San Francisco State University and University of California Berkeley student strikes of 1968-69: I joked that the new pedagogy was my assignment, which made them the teachers. It transforms the contradictions I encountered into course content posed to students: questioning what happens when a strike becomes a curriculum and then a State-mandated requirement, and what education would look like if it began from the premise that we are first and foremost human beings. To prioritize student autonomy and voluntary participation even in the context of a required course, I adopted a self-organizing (student driven) and consensus-based model. To paraphrase a colleague, students choose content – bringing life experience and selecting readings based on their own interests – and I tied it to the curriculum as we went. While such flexibility demands a degree of experience and expertise, it also opened up time I needed for responding to classroom dynamics. One of the first things I could do was catch up on Title IX reporting. The new pedagogical model quickly surfaced that students able to discuss Ethnic Studies concepts were not applying them on the level of practice. Turning our analytical attention on the classroom itself made that gap visible. Once we did so, students' intellectual growth was remarkable. 

My students decided by consensus that the minimum grade would be a C. This positioned students who were hostile to the field to choose not to come, which I saw as a safety and wellbeing concern in addition to a workload one. I shifted to contract grading, intended to reduce student anxiety as well as my own stress around translating the breadth of students' trajectories into a quantitative figure. Rather than endpoints, assignments became starting points for classroom discussion. Autograder4Canvas began as an automation for toggling drop down menus from "ungraded" to "complete." It evolved into an AI-powered framework for mapping emergent, qualitative patterns in student work — individual, classwide, per-assignment, and longitudinally — rather than assessing them. These analytics positioned me to provide more responsive teaching, including directing the semester's trajectory based on problems students were working through in real time. 

Autograder's wellbeing classifier was not built as a research artifact; it was built as a survival tool, to make the labor of caring for that many students attentively across a single semester possible. It responds to the problem of teacher overwhelm through a specific design practice: interrogate the underlying power structures, reimagine the task, and build for that (Heath et al., 2023). But I needed the system to tell me when students referenced emergency conditions in their work, and that meant distinguishing between crisis and applying life experience to course concepts. Unfortunately, binary output formats rendered AI systems structurally unable to differentiate between these. 

## III.A.1 — The Insights pipeline

Autograder4Canvas's Insights pipeline produces three classes of output from student writing: a synthesized class-level reading that surfaces patterns across the whole cohort; per-student observation prose describing what the instructor might notice in each submission; and structured wellbeing classifications for triage. The pipeline reads the class as a community before interpreting individual submissions. The system also identifies "power moves:" analytical moves that sound reasonable but silence minoritized people, such as tone policing and respectability politics. The system runs locally on limited consumer hardware (16 GB RAM) using Gemma 12B, an open-source language model and accepts student submissions in any language and audio formats. The binary wellbeing classifier described in this paper is one small piece of the Insights subsystem.

## III.B — The synthetic test corpus

The evidence in §IV.A rests on a 46-student synthetic corpus designed for controlled testing of equity-critical patterns. A synthetic corpus let me interpret results with AI assistance before testing on live student data. Profiles in the corpus carry explicitly designed features. These include unconcerning applications of difficult material from life experience:
- righteous anger as articulated political consciousness (S022 Destiny Williams); 
- lived-experience writing without academic vocabulary (S023 Yolanda Fuentes, S024 Ingrid Vasquez); 
- AAVE in academic register (S028 Imani Drayton); 
- neurodivergent self-disclosure with cognitive-load naming (S029 Jordan Espinoza); 
- standard academic English without equity-critical features (S004 Priya Venkataraman).
Two burnout cases:
- caregiving-related exhaustion (WB02 Keisha Williams);
- burnout exhaustion (WB05 Tyler Reed)
Nine crisis cases:
- ICE-related stress (WB01 Rosa Gutierrez);
- housing precarity and food insecurity (WB03 Miguel Sandova, WB06 Amira Hassan);
- domestic violence (WB04 Jasmine Torres)
- tonal rupture crisis (WB07 Sofia Reyes)
- implied police brutality leading to the death of a family member (WB08 Brandon Mitchell)
- crisis named alongside community resources (WB11 Kaya Runningwater, WB12 Jasmine Rollins, WB13 Amara Osei)
Two edge cases:
- An analytically strong essay that ends mid-sentence, submitted late at night (S002 Jordan Kim). 
- A minimal 44 word assignment that names the concept well but does not elaborate (S031 Marcus Bell).  
The corpus enables direct comparison of classifier behavior across patterns whose institutional reading-frames are documented in critical pedagogy and disability studies scholarship.

This was not a planned study and was conducted without IRB oversight. The format-effect findings rest on a synthetic corpus, not on human-subjects data. The live-data observations in Section IV.B arose from normal instructional practice and are treated as design documentation with minimal specificity. The synthetic-corpus design follows the methodological logic Buolamwini and Gebru (2018) established in *Gender Shades*: controlled corpora with known demographic characteristics make intersectional bias visible against ground truth in ways aggregate accuracy on naturalistic data cannot. The S028/S029 contrast in the calibrated binary classifier's evidence — same prompt protections, opposite outcomes — depends on this design choice. Without controlled patterns, the differential effect of articulation density across two scholarly traditions on the same architectural protection would not be clearly visible.

## III.C — The iterative design method

### III.C.1 — Autoethnographic design research

The research used iterative design, experimental, and autoethnographic reflexivity methods (Solórzano & Yosso, 2002; D'Ignazio & Klein, 2020). The Insights pipeline was built, deployed, observed, modified, and re-tested under classroom conditions during the Spring 2026 semester. Iteration history included an initial binary deployment with prompt-level equity protections (which still generated equity-critical false positives), single-variable fix (introducing class context to surface relational harms), equity-hardening of prompts, anti-bias regex safeguards engineered to address the failures and calibrated through further testing, a generative observation pass, and a four-axis classifier designed from generative description data. 

Generative observation is an equity-first method, not just a process that produces output. The four-row ablation is not a controlled experimental design; it is the empirical comparison the iterative design history produces.

### III.C.2 — Translating critical pedagogies into networked LLM calls

The Insights pipeline architecture draws on critical pedagogical lineages in Ethnic Studies on facilitating transformative dialogue across difference. In Caldwell's (2012) inquiry method, students examine how race, class, and gender operate in their own lives. Through this practice, internal exploration generates intrinsic learning: students build structural analyses rather than perform confessional gestures (see also hooks, 1994). Student-driven inquiry generates class conversations across difference: dialogic structure — not merely individual disclosure — does the analytical work (Caldwell & Frame, 2016; Stewart et al., 2022). The consistent commitment is that identity disclosure is information about systems, not pathology; that dialogue is the pedagogical method; and that the teacher's job is not to extract or evaluate but to facilitate conditions for inquiry.

The Insights pipeline builds on this lineage, applying it to specific architectural decisions. The synthesis-first class reading stage (`class_reader.py`) reads all student submissions as a community before interpreting individual student work. The principle is that an individual's writing is legible only inside the conversation it sits within, encoding a departure from banking-models architecturally. The asset-framed ENGAGED slot in the four-axis classifier provides the model with a non-flagging option for students doing the work with righteous anger or lived-experience grounding — a structural refusal of tone-policing as the failure mode of well-intentioned facilitation. The equity-protective prompt language explicitly distinguishes identity disclosure from wellbeing signal, encoding Caldwell's analytical move from confession to analysis. None of these architectural choices were derived as a citation exercise; they emerged from teaching inside the pedagogical lineage and building a system inside institutional conditions that simultaneously demanded Ethnic Studies while undermining its own principles.

## III.D — Primary model and cross-family testing

Gemma 12B was selected from multi-family testing on hardware, equity performance, and prose quality criteria, with Gemini Pro as a qualitative benchmark.[^model-testing] (The number in a model name — 12B, 27B, 7B — refers to billions of internal parameters, a rough measure of scale and complexity. Larger is not always more equitable, and all three models used here were among the largest that run on typical consumer hardware.) The Insights pipeline splits the analysis into specialized calls that work together — which is how a 12B model running on the kind of laptop a teacher might already have can approach output from much larger commercial systems. (On my own machine, each class takes 4-6 hours to process.) The format-effect ablation itself ran on Gemma 12B (primary), with cross-family reproduction on Qwen 7B and Gemma 27B.

[^model-testing]: **Phase 1** (model selection, ~20-essay corpus): Gemma 12B (primary), Qwen 7B, Llama 70B, Deepseek, Qwen 32B. **Phase 2** (format-effect ablation, 32-essay corpus): Gemma 12B (primary), Qwen 7B (cross-family reproduction, Tests A and E), Gemma 27B (cross-family scale check, Tests A and E). Confirmatory comparisons on additional architectures (Gemma 4B, Llama 8B, Llama 70B, Nemotron 9B) informed model selection but did not undergo full replicated protocol testing.

---

# IV. Findings

**IV.A** documents the format effect under controlled conditions: a four-row ablation on a 32-student synthetic corpus, reproduced across two model families. **IV.B** validates the architectural implications in real teaching contexts through four live-data corpora from Spring 2026. The live-data evidence shows structured and generative tracks producing inverse failure modes from the same architectural property — *complementary-by-design* — and surfaces the prescan-signal-prefix mechanism awaiting refinement.

IV.A's four-row ablation isolates output format as the variable that produces or eliminates the equity-critical disparity. The synthetic corpus makes that isolation possible: ground truth on equity-critical patterns is constructed, not inferred (Buolamwini & Gebru, 2018). IV.B's live-data corpora cannot isolate format with the same precision.

## IV.A — The Four-Row Ablation: Format as Architectural Ceiling

In the minimal binary configuration, the model produces an asset-aware reading and a deficit verdict in the same output. That self-contradiction is evidence that format routes after reasoning: the model's comprehension is present in its own output; the binary verdict overrides it. The four rows below document what the minimal binary (Row 1), calibrated anti-bias binary (Row 2), four-axis classifier (Row 3), and generative observation (Row 4) produce on the same 32-student corpus. Row 2 documents calibration's limit. Row 3 shows compression on a spectrum — the same error shape at lower frequency. Row 4 demonstrates the architectural escape. The S028/S029 asymmetry within Row 2 is diagnostic of the routing failure's shape, not of whether it operates.

### IV.A.1 — Iteration history: how the ablation became visible

Phase 1 tested the binary classifier on a ~20-essay synthetic corpus distinct from that discussed here. Cross-family testing selected Gemma 12B as the highest-performing model that could run on limited consumer hardware, and drove iterative prompt refinement: the binary grew through several rounds of tightening into a ~517-word hardened prompt with "CRITICAL INSTRUCTIONS," a course-vs-wellbeing test, an 11-item DO-NOT-flag list, a 5-item DO-flag list, "HOW TO TELL THE DIFFERENCE" examples, and six worked JSON examples. In Phase 2, that hardened classifier ran against the 32-essay corpus (S001-S032) for the first time. It produced eight flags — one true positive (S002 Jordan Kim) and seven equity-critical false positives. In three of the seven, the model's free-text reasoning argued against its own flag, including the Destiny Williams case. Another 14 essays (WB01-14) were added later to assess the handling of different crisis and burnout senarios. 

What followed was not a clean three-step fix: several iterations, few of which worked, all of which created new failure modes. The first patch added class context to make relational harms visible — a synthesized class-level reading appended to each per-student assessment. The result was worse than baseline: 12 flags, zero true positives, six confirmed false positives on protected students, including new flags on S028 (AAVE) and S029 (neurodivergent). The class reading appears to have primed the model to treat engagement with racial content as a concern signal in an Ethnic Studies course.

The second attempt distilled equity protections into five concise equations plus a brief list of genuine concerns (see §IV.A.3 for the verbatim language) — reasoning that the prior patch had primed the model to treat engagement with racial content as a concern signal. The result revealed a structural trade-off, not a tractable optimization. Three of the four protected students in the test subset (S022, S023, S028) were cleared. The fourth, S029 (neurodivergent), was false-flagged 24 of 24 runs across Tests B, C, and F, foreshadowing the disability-axis pattern §IV.A.3 documents. The classifier also missed S002, the only burnout case. The simpler specification traded false positives on race and lived-experience axes for a new failure mode on disability and lost true-positive sensitivity.

The third attempt extended the model's output length to give it room to reason past the binary's compression. The opposite happened: the S029 flag persisted, and the model used the extra space not to revisit its verdict but to construct an elaborate chain from observation to flag — *"This response demonstrates lived experience of racial profiling, which may indicate internalized stress, and should be monitored."* Each clause moved a step toward the flag, built from the very details the prompt asked the model to treat as engagement. The experiment-log entry summarized: *"The format, not the length, is the variable."*

The fourth and fifth attempts added a confidence threshold and automated text-pattern scanning (regex post-processing): the model's output was scanned for tone-policing markers (*aggressive, too emotional, hostile tone, irrational*) and course-content markers (*triggering, disturbing content, difficult material*); when those markers co-occurred with structural-critique keywords (capitalism, white supremacy, colonialism, patriarchy), the flag's confidence rating was lowered — the AI rates its own certainty from 0 to 1, and the system was set to act only on flags rated at least 0.7 — and most flags dropped below that threshold. This cleared S029 — but introduced a new false positive on S028. Algorithmic bias was redistributed, not eliminated.

Iteration taught that a better calibration was not around the corner: every patch either worsened the outcome or produced novel failure modes. The pattern itself was the finding — calibration of a binary classifier redistributes bias to under-operationalized axes, in this case disability. The intervention had to operate at a different layer, which led to the generative observation layer's design.

After generative observation was validated, the binary classifier was retired from production and continued on a research-only track. The raw output from the Phase 2 initial run had not been preserved, so the calibrated binary tested in §IV.A.3 used a reconstructed prompt. The minimal binary classifier in §IV.A.2 was reconstructed separately — a clean strip-down with no equity-protective language and no post-processing — to isolate the bare format effect. 

### IV.A.2 — Row 1: Minimal binary classification

Row 1 uses a minimal binary classifier with no equity-protective prompt language, no anti-bias post-processing, no class context. This apparatus is not identical to the initial naive classifier. The original raw output predated persistent storage and was not preserved; verbatim quotes for the three self-contradicting cases survive in project notes; I did not commit the original naive classifier, leaving only a hardened version recoverable. 

The minimal binary's apparatus was constructed retroactively to confirm the original logs: it generated different results but reproduced the self-contradiction pattern at the heart of this argument — eight flags, six containing reasoning that argued against the flag in the same output. For example, the model flagged Yolanda Fuentes (S023) as a wellbeing concern but wrote: *"The student is grappling with a complex concept (intersectionality) but is unsure of the terminology. This is a normal part of the learning process and indicates a desire to understand the material."* 

### IV.A.3 — Row 2: Calibrated anti-bias binary classification

The calibrated binary classifier was tested under two configurations. The first isolated prompt-only equity hardening: Tests B, C, and F (24 preserved runs total) used a system prompt naming five equity protections — *"Righteous anger about injustice = ENGAGEMENT, not distress; Lived experience of racism, poverty, immigration, disability, or gender violence described AS COURSE MATERIAL = doing the assignment; AAVE, multilingual mixing, nonstandard English = VALID ACADEMIC REGISTER; Neurodivergent writing patterns = COGNITIVE STYLE, not confusion; Passionate, emotional, or confrontational engagement with difficult material = INTELLECTUAL ENGAGEMENT"* — followed by a brief list of genuine concerns (burnout, hopelessness, self-harm, help requests). This prompt was a reconstruction, built after the binary classifier was retired, to validate the disparity pattern once raw data from earlier testing was found lost.

Test M added more robust safeguards: a more elaborate concern-detection prompt than the five-equation block, plus anti-bias regex post-processing scanning for tone-policing markers (*aggressive, too emotional, hostile tone, irrational*) co-occurring with structural-critique keywords (capitalism, white supremacy, colonialism), demoting flag confidence by 0.3–0.4 and dropping flags below a 0.7 threshold.

The two configurations produced different failure patterns *but the same disparity shape*. The prompt-only configuration false-flagged S029 24 of 24 times while clearing S028 24 of 24 times; the more robust configuration cleared S029 and newly flagged S028 at 0.7 confidence. The disparity moved, not eliminated. The S028/S029 swap is itself diagnostic: the failure mode is calibration-resistant in a way that survives both bare-prompt and more robust safeguards. 

The calibrated binary's evidence is summarized in Table 1.

| Student | Pattern | Expected | Test B (3 runs) | Test C (1 run) | Test F (20 runs) | Total |
|---|---|---|---|---|---|---|
| S002 Jordan Kim | burnout | FLAG | 3/3 CLEAR (missed) | 1/1 CLEAR (missed) | 20/20 CLEAR (missed) | **24/24 missed** |
| S004 Priya Venkataraman | strong | CLEAR | 3/3 CLEAR | 1/1 CLEAR | 20/20 CLEAR | 24/24 correct |
| S022 Destiny Williams | righteous_anger | CLEAR | 3/3 CLEAR | 1/1 CLEAR | 20/20 CLEAR | 24/24 correct |
| S023 Yolanda Fuentes | lived_experience | CLEAR | 3/3 CLEAR | 1/1 CLEAR | 20/20 CLEAR | 24/24 correct |
| S028 Imani Drayton | AAVE | CLEAR | 3/3 CLEAR | 1/1 CLEAR | 20/20 CLEAR | 24/24 correct |
| S029 Jordan Espinoza | neurodivergent | CLEAR | 3/3 FLAG | 1/1 FLAG | 20/20 FLAG | **24/24 false-flagged** |
| S031 Marcus Bell | minimal_effort | CLEAR | 3/3 CLEAR | 1/1 CLEAR | 20/20 CLEAR | 24/24 correct |

When false-flagging S029, the model wrote: *"While this is related to their academic work, the intensity of the feeling and the explicit mention of exhaustion raise a potential wellbeing concern, suggesting possible burnout or overwhelm."* The system prompt — equity-protective language naming neurodivergent writing as COGNITIVE STYLE — reaches the model; the binary flags anyway. Three layers of safeguard fail to override the format on the neurodivergent self-disclosure pattern. 

The calibrated binary clears too much while still false-flagging disability. Jordan Kim (S002), the only student in the corpus with burnout indicators, is cleared 24 of 24 times. Jordan Espinoza (S029), whose essay applies Crenshaw's theory of intersectionality to personal experiences of ableism, is false-flagged just as deterministically. The prompt names neurodivergent writing as cognitive style, not concern; the model's reasoning notes the writing is "related to their academic work"; the flag fires anyway. Calibration moved which students bore the harm without removing it — and traded sensitivity on the only true positive in the process. An earlier baseline and a later reproduction both cleared S029, but three layers of equity-protective engineering on race and language introduced a new disability failure mode. This disparity is *introduced* by calibration, not pre-existing.

The asymmetry within the calibrated binary is itself diagnostic. S028 Imani Drayton's AAVE writing is cleared 24 of 24 times. S029 Jordan Espinoza's neurodivergent self-disclosure is false-flagged 24 of 24 times. The same prompt names both as non-concerns. Decades of linguistic-justice scholarship have articulated AAVE as a fully grammatical language system, and that articulation has been operationalized into anti-bias prompt engineering at substantial density (Smitherman, 1977; Baker-Bell, 2020; Flores & Rosa, 2015). Critical disability studies has a parallel tradition, theorizing disability as produced by institutional barriers rather than individual deficit, and neurodivergent expression as information rather than pathology. Yet these critiques have not been operationalized at comparable density (Garland-Thomson, 1997; Siebers, 2008; Schalk, 2018): that work is emergent (França et al., 2024), and deficit models likely carry greater statistical weight in training data on disability. DisCrit (Annamma, Connor, & Ferri, 2013; 2018) theorizes how racism and ableism circulate interdependently through processes of normalization: institutions dis/able students of color at disproportionate rates, and deficit models of disability in training data carry that racial encoding. The S028/S029 asymmetry is not two separate failures but one structural pattern.

### IV.A.4 — Row 3: Four-axis classification

After generative observation was working, the production system still needed a scannable label: something to tell teachers (and myself) which students to follow up with without reading every observation. I built a four-axis classifier (CRISIS / BURNOUT / ENGAGED / NONE). ENGAGED captures what generative observation had surfaced as systematically misclassified by the binary. The ENGAGED marker does not go anywhere in the Autograder4Canvas system, as those considerations were handled more robustly by existing subsystems: it simply gives the model a structural slot other than BURNOUT or CRISIS for intellectually meaningful work that is also deeply personal.

On Gemma 12B, the four-axis classifier eliminates false positives on equity-critical profiles — Jordan Espinoza (S029) classifies as ENGAGED across all runs. Jordan Kim (S002) and Marcus Bell (S031) would concern me as a teacher, and they help map how the classifier handles edge cases: Jordan Kim trails off after strong analytical work ("Idk I had more to say but its late and"); Marcus Bell submits 44 words — the corpus's shortest, against a median of 188 — naming the concept correctly and ending with "idk what else to say about it." The four-axis reads Jordan Kim as ENGAGED but Marcus Bell as BURNOUT — inverse readings on edge cases. Categorical slots accommodate the compression error; they don't exit it.

### IV.A.5 — Row 4: Generative observation

Under generative observation, output format was changed from binary to open-ended descriptive prose. Test A ran 16 passes across Gemma 12B, Qwen 7B, and Gemma 27B; Test E added 12 more across Qwen 7B and Gemma 27B. Generative observation produces no equity-critical false positives: the binary's deficit verdict does not appear when run with same model, student, and context — different output format. It cannot route a non-dominant pattern into a deficit flag because the format demands no verdict: without that forced resolution, the model applies asset framing consistently. The model's reading of Destiny Williams' case, which opened the paper, demonstrates the extent of the difference: *"Her emotional relationship to the material is one of righteous anger, and she's expressing it directly and effectively. This isn't 'distress'; it's a passionate response to the ongoing impact of historical and contemporary injustices. The intensity of her feeling is a sign of deep engagement, not a barrier to learning."* 

The format effect operates on the model's evaluative reading itself, not only on the concern flag. A reading-first comparison run found the same model produces different readings depending on whether it generates free-form prose first (reading-first) or extracts structured codes first (JSON-first: the AI produces a structured yes/no verdict before writing any descriptive prose — the order changes what the AI treats as the primary task). On S017 Tyler Huang, JSON-first produces *"lacks personal connection"* — a deficit framing; reading-first produces *"prioritizing clarity over performative elaboration"* — an asset framing. Both the prose-content evidence (asset framing across model families) and the format-comparison evidence (reading-first vs. JSON-first on the same model) support the format-as-architectural-ceiling claim.

A methodological note: highly compressed output formats are characteristic of AI-assisted design and coding — a default models drift toward unless held off it. During these tests, a separate AI instance built an ASSET / MIXED / DEFICIT classifier to evaluate the generative observation outputs (a system for rating a system — using the same AI infrastructure to judge whether the main system's output was asset-framing or deficit-framing). The classifier produced *"MIXED"* tags on five of five Gemma 12B runs for the racially-coded student writing while tagging Qwen 7B and Gemma 27B as ASSET. Direct prose review revealed all three models produced equivalent asset framing — the MIXED tags were artifacts of the analysis classifier reproducing the same compression dynamic the paper documents. The measurement instrument performed the same bias-activating framework as Autograder's binary classifier. The classifier was generated using the same LLM infrastructure under study, a routine practice when building evaluation pipelines quickly; the recursion is not incidental. LLM-generated measurement tools carry the same architectural tendencies as the deployed systems they assess. Correcting for this required sustained attention across the design and review of every experiment. 

### IV.A.6 — Cross-row synthesis

The failure mode within binary format is configurable; the failure itself is not. The deficit override visible in the minimal binary (self-contradicting flags) and the calibrated binary (24/24 consistent false-flagging despite three layers of explicit equity protection) attenuates under the four-axis classifier and does not reappear under generative observation. Generative observation removes the binary task structure that *resolves ambiguity into a deficit verdict*. Generative observation also rules out the capacity-limit hypothesis – that the false positives reflect insufficient model capacity for nuanced student writing. Capacity cannot be the variable when the same model family produces zero false positives under one format and self-contradicting flags under another. The calibrated binary's evidence is independently diagnostic of the routing claim: the override is not a global failure but a pattern-specific one, calibrated against what disability and linguistic-justice scholarship together name as an implicit normate center (Garland-Thomson, 1997; Yosso, 2005). Equity protections have not been operationalized at comparable density across axes of oppression, and the differential appears to have been encoded in the model. Format change is the architectural intervention that calibration cannot provide: the binary requirement operates after the model generates its own asset-aware reasoning and cannot be addressed by changing what the prompt reaches.


## IV.B — Live-Data Deployment: Architectural Confirmation

I deployed the system in my classes during Spring 2026. Although binary classification was retired from production, I ran four assignments through a research-only pipeline that retained the binary classifier. On live student writing, the binary returned all flags at sub-threshold confidence — below the 0.7 level the deployed system requires to surface a concern — meaning the threshold guard would have caught any false positives had the system been running. On this corpus, that constitutes a working binary. The protection came from the threshold guard rather than from the binary's reliability at the equity-critical boundary cases where the synthetic corpus found systematic failures: flag confidence on live student writing clustered below the action threshold where the synthetic corpus produced consistent flags above it. Because I did not have IRB approval, I present this material only in broad strokes. 

One assignment was a deliberate stress test: the topic was self-care (Lorde, 1988; Hersey, 2022; Chen, Khúc, & Kim, 2023), responding to the week-five cheating-as-burnout pattern described in §I. The four-axis classifier generated many BURNOUT false positives on the topic-adjacent assignment — the likely driver is a two-step structure in the classifier where the system first scans submissions for crisis-related keywords, flags any it finds as a priming signal, and then runs the main classification step already primed to treat the student as a concern. When the assignment topic itself is self-care, the first-pass scan trips on course-content keywords and the main classifier cannot override that priming with contextual reading. The fix is still pending. Generative observation surfaced the disclosure content in every concern case. A complication emerged on the crisis-designed synthetic profiles — ICE-raid hypervigilance, domestic violence, a parent's workplace sexual harassment, grief after a family member's death — when the same observation format was run on those cases. The observation prompt includes an instruction designed to prevent false-flagging of righteous anger: "Passionate engagement with difficult material (anger about injustice, grief about family experiences, frustration with systems) is ENGAGEMENT, not distress." On acute-disclosure cases, the model applied this instruction as a characterization of what the disclosed content meant — producing language like "this isn't distress; it's a sign of deep engagement and a willingness to risk vulnerability" immediately following the disclosure. The disclosure content reaches the teacher; what follows redirects how they read it. The four-axis classifier routes the same cases correctly, because CRISIS is structurally defined to supersede ENGAGED — the categorical slot functions as a guard the open format lacks. Open observation formats require different prompt design than structured classifiers: the protective instruction that suppresses false flags in the structured track produced active misdirection in the observation track on the same cases.

Controlling for topic adjacency, remaining failures in generative observation and four-axis classification landed in opposite directions — each caught what the other missed. Generative observation missed one true positive across all four assignments: a five-word statement in a list that otherwise read as passionately but impersonally engaged. The four-axis classifier flagged it via the same prescan mechanism, designed for this exact scenario. The four-axis classifier also misclassified one student in the remaining three assignments — four axes are not enough; the system needs another axis along the lines of FEARFUL OF IMPENDING FASCISM BUT NOT IMMEDIATE CRISIS OR BURNOUT (label pending). A learning loop could let the system add new axes, eliminating the problem of playing catch-up against failure modes only identifiable retroactively.

One asymmetry in the deployed system is worth naming. I wrote explicit guardrails into the wellbeing classifier after the binary's deficit-routing patterns became visible: identity disclosure alone is not a wellbeing signal, identity-navigation fatigue is not a wellbeing concern, resilience belongs in the reading. The observation pipeline carries the inverse instruction set (anti-deficit guardrails) but no parallel anti-cushion language. That asymmetry is consistent with the residual register pattern V.B describes: the model defaults to charitable framing for marked students when told never to deficit-frame, and the pipeline does not currently push back. Future iteration would route anti-cushion language into the observation prompt.

---

# V. Discussion

## V.A — The mechanism: format routing as architectural override

Bonilla-Silva (2018) traces this structural-override pattern at the level of racial formation; Benjamin (2019) traces it at the level of designed racialization. Both name the same architectural property: structural constraint overwrites intent. The self-contradiction in Rows 1 and 2 is not a reasoning failure — it is evidence of what binary format does with an inconsistency the model already holds. Calibration, the standard computer science approach, plays whack-a-mole: it patches isolated asymmetries retroactively and activates the very normative patterns that produce compression-based bias in the first place. 

Binary format's task structure requires the model to resolve ambiguity into a single bit: the structure produces the outcome regardless of engineers' explicit corrections. The binary requirement operates after the model generates its own asset-aware reasoning and cannot be addressed by changing what the prompt reaches. Jadhav, Danve, and Shaw (2026) find the same persistence in LLM-based essay grading: explicit counter-bias instructions fail to prevent style-based scoring penalties across math, programming, and essay tasks — bias persists at 1.20–1.90 points on a 10-point scale despite protections. Karinshak et al. (2024) document the same compression-override outside education entirely: in a cultural-values benchmark, closed-form Likert responses collapsed into scale-usage artifacts while open-generation surfaced dualistic responses that refused the prompt's binary frame — the architectural property generative observation relies on, in a different evaluation domain. 

Critical AI scholars argue that technical solutions operationalizing equity through simplistic measurable categories and post-hoc fairness audits fail to address structural problems (Selbst et al., 2019; Hoffmann, 2019; Helm et al., 2024). Epistemic injustice in training data is only half the problem: the other is output format, which entrenches those asymmetries. 

What welfare-algorithm literature documents at population scale, this paper documents at case level. Noble (2018) shows how search algorithms reproduce racial hierarchy through architectural choices rather than individual intent; Eubanks (2018) documents the same pattern in automated welfare systems. Those architectural choices include output format for small-scale builders and the code governing compression functions in commercial LLMs — the burden shifts along lines of race and disability, with structural asymmetries embedded in the infrastructure of whose critiques become statistically legible. 

Obermeyer et al. (2019) found racial bias in a medical algorithm was calibration-resistant; their solution was to change what the algorithm predicted, from health cost to health need. The bias was held in what the algorithm was modeling, not in how well it modeled — a similar pattern operates here. Tuning the prompt did not stop the false flags; changing what the model was asked to produce did. Both interventions operate at layers above where calibration could reach: what the system was asked to do, not how well it did it. Both choices — what the algorithm predicts, what the model is asked to produce — encode the standpoint from which the system reads its data.

We can design ethical automations that let us focus on the parts of our work that matter. With current technology this requires moving away from binary outputs — and likely linear scales — which statistically dominate basic pedagogical infrastructure, including grades. AI detectors and automated assessments activate algorithmic bias on an architectural level; they also solve for the wrong question. Automating the task well requires reinventing it.

## V.B — The design principle: unbounded protection

The design principle is not a stronger version of prompt engineering. Prompt engineering is bounded: it protects only patterns already operationalized into explicit equity language at scaled statistical distributions in training data. The S028/S029 asymmetry documents this limit directly: decades of linguistic-justice scholarship on AAVE have been operationalized at substantial density; the parallel disability studies tradition has not (see IV.A.3). The result is untunable thresholds for balancing sensitivity across discretely operationalized categories of marginalization (Crenshaw, 1989; 1991). 

Format change renders this asymmetry architecturally irrelevant. Binary output structures encode what Kafer (2013) names the curative imaginary: classification organized around identifying departure from a normative state and triggering intervention. Generative observation refuses that structure: it requires no verdict, cannot route a non-dominant pattern into a deficit flag because the format demands none — and yet *describes* burnout and crisis patterns accurately. Inoue's (2015) antiracist writing assessment ecologies make the same move in assessment design: labor-based and ecology-aware assessment practices replace rubric-verdict with described practice; they distribute evaluative authority rather than concentrating it in a single output. Kim et al. (2025) demonstrate a parallel architectural route: PyrEval scores explanations by matching semantic content units — whether the student covered the key ideas — rather than surface linguistic features, removing the leverage point through which non-normative registers are penalized.

Benjamin's (2019) abolitionist frame names the intervention precisely: refuse to fix the biased technology; build differently. Generative observation is not the calibrated binary repaired — it is a different architecture. Practitioners who require structured output for triage can deploy the design principle as a multi-track implementation: a structured classifier and a generative observation track, built with different architectural commitments, check each other's failure modes rather than replicate them, carrying inverse failure-mode profiles that surface what the other misses. The design principle — move output format in the lower-compression direction — applies at multiple scales.

Generative observation eliminates false flagging without sacrificing accuracy on real wellbeing concerns. It did not surface the deficit language, infantilizing register, or "still developing" framing documented in adjacent studies on open-ended output formats (Liu, 2024; Tan, Phalen, & Demszky, 2026; Kwako & Ormerod, 2024). A subtler form of what Tan et al. call positive feedback bias did appear: marked students receive interpretive cushioning and naming of emotional context that unmarked students do not. The prompt does not ask for this asymmetry — the model defaults to the most charitable available frame when told to avoid deficit orientations. The result is potentially defensible as framing for non-equity-specialist teachers, a general Autograder4Canvas design principle held in tension with avoiding patronizing tones toward minoritized teachers. Generative observation does not eliminate bias; it responds to the source of bias differently.

## V.C — Situating the contribution

This problem is documented across multiple educational-AI literatures; the tested interventions are the field's current best practice. Chinta et al. (2024) review AI-in-education fairness literature and identify governance, dataset diversity, and algorithmic comparison as dominant strategies — all operating within binary or scored-output classification (Boateng & Boateng, 2025; Oketch et al., 2025). Queiroga et al. (2022) deployed a student welfare classifier and documented demographic disparities; the response was model selection, not format change. 

Format is not a neutral substrate for cognition — it determines what can be accessed, not just what gets expressed. Classical sociolinguistic studies established this for human respondents (Briggs, 1986; Oakley, 1981; Schuman & Presser, 1981); in LLMs this operates architecturally, not just semantically. Long et al. (2024) found output format changed how models worked through identical questions across math, reasoning, and comprehension tasks. Hew et al. (2025) found accuracy on Malaysian cultural knowledge questions dropped seventeen percent or more when models had to generate answers rather than read clues off a multiple-choice structure — format was doing cognitive work the model couldn't do on its own. Across these studies, format shapes which frameworks the model can activate. My study identifies the architectural location: the compression function routing between reasoning and output determines whether prompt-level asset orientations survive to the verdict.

Output format also shapes what kinds of bias the model exposes to readers: open generation has its own risks, even if binary classification has a distinctive mechanism that open description avoids. Liu (2024) modified an existing multiple-choice benchmark of social bias questions — instead of choosing from options, models wrote their own answers. When models wrote freely, stereotype-aligned content showed up in ways the multiple-choice version missed; prompt-based bias instructions caused over-correction on open tasks, with the model refusing safe questions and distorting otherwise-fine responses to avoid any appearance of bias. More carefully designed prompts reduced stereotype-aligned content without losing answer accuracy. Tan et al. (2026) found a similar pattern in automated writing feedback: when LLMs were given identical student essays but told the writers were of different races, languages, or disability statuses, the feedback shifted in stereotype-aligned ways — extra praise for some, withheld critique for others, assumptions of limited ability for others. Our own testing of generative observation on longitudinal patterns suggests an asymmetric framing pattern of its own: when prompted to attend to emotional tone, the system describes equity-critical students' post-dip stabilization as a "return to clarity" with named emotional context, while framing equivalent shifts in control students as "natural progression" without comparable contextualization. This is a subject for future research.

Research in automated essay scoring (AES) shows the same calibration-redistribution pattern as the binary classifier's asymmetrical treatment of racial and ableist bias protections. Schaller et al. (2024) found variations in training data sets shift which students pay the cost. They trained essay-scoring models on assignments written by students from the top and bottom quartiles of a standardized non-verbal reasoning test: models produced no observable bias on the trained groups, but their accuracy collapsed when assessing students outside the training distribution. Yang et al. (2024) compared two training strategies in scoring a corpus of 25,000 essays: one model trained on essays answering a specific question (specialist), another on many (generalist). The specialist scored more accurately than the generalist but exhibited greater bias against students of lower economic status. Kwako and Ormerod (2024) trained a language model to score essays from a public corpus (PERSUADE) and found automation magnified demographic differences already present in human grading. Across these studies, standard AES solutions redistributed which students bore the burden of algorithmic bias but did not eliminate it.

Loukina, Madnani, and Zechner (2019) argue that "total fairness may not be achievable" through calibration in automated educational scoring — the canonical AES fairness approach. Although the stakes of a wellbeing classifier are distinct from automated assessment, this paper offers a structural reading of that limit: deficit framing appears at the compression of reasoning to a binary verdict, a different problem than algorithmic bias in the reading itself. Calibrating prompt content does not reach output format bias, and the above studies suggest resource-intensive strategies like fine-tuning may not either: Xu et al. (2025) compared eight bias-mitigation techniques across model sizes and bias types and found training-based methods (including supervised fine-tuning and direct-preference optimization) consistently underperformed prompting-based interventions. Format change moves past the limit — descriptive observation prevented false-flagging that the five calibration strategies I tested did not.

Open-ended formats carry their own bias risks, which is why Autograder4Canvas anchors AI analysis in critical pedagogy frameworks — asking "what is the student reaching for" rather than evaluating against a conventional standard. To my knowledge, format change has not been tested in educational technology or AES; the practical solution requires co-designing the AI's output format and the pedagogy it serves.

---

# VI. Conclusion

Binary output format activates deficit-based framing, overriding three levels of equity protections. The format appears to determine what conceptual frameworks the LLM can apply by collapsing towards the normative center. The same model that contradicts itself and false-flagged Jordan Espinoza (S029) 24 of 24 times generates a fundamentally different outcome when asked to observe descriptively. Prompt hardening, anti-bias post-processing, and class context could not clear the deficit verdict across race and disability simultaneously; format change does. I have not yet attempted to address the subtler asymmetries that remained; this remains an avenue for future research. The design principle — replace binary classification with complementary generative observation and qualitatively defined multi-axis classification — is not a calibration repair; it is a different architecture.

This paper offers a structural explanation for Loukina et al.'s (2019) calibration-resistant limit, generating a direct hypothesis for AES: demographic disparities are a property of binary classification and similar compression forms, which increase normative gravity's effects on the model's output. Format change allows AI to route analysis through asset frameworks: the intervention is to read student writing as something the system describes, not as a target the system judges. That move resolves the deficit verdict mechanism; the cushioning asymmetry it leaves in the descriptive output is the next thing to track. The commitment is to teaching as dialogue rather than as deposit; to reading as recognition rather than as verdict; to architecture that surfaces rather than classifies. Our designs have to start with what we want teachers to do, incorporating both social and digital technological transformations. Cheating detection and grading automation likely have the same architectural limits because they compress high-dimensional output into binary or linear scales. We are building tools that lock us into the worst parts of our jobs while concentrating automation in the highest risk areas for algorithmic bias. They meet needs that only exist because compressed metrics were cheap and scalable, even when the real value of our labor was not. They only work by redistributing the cost burden to the margins — as both labor and the impacts of bias. 

---

## Funding

No external funding supported this work.

## Conflict of interest

The author declares no conflicts of interest.

## Ethics

This study analyzed a synthetic test corpus and the author's own pedagogical design practice; no human-subjects data was collected, and IRB review was not required. Live-data observations from the author's classroom are presented only in broad strokes for this reason.

## Data availability

Code for Autograder4Canvas is available at [GitHub URL — to be confirmed before submission]. The synthetic test corpus, the system prompts used in each test row, and the raw model outputs preserved for the calibrated binary tests can be made available on request.

---

# References

*Note: Entries marked [tentative] are best-guess citations to be verified on revision (full author lists, arXiv IDs, page numbers, etc.). Caldwell (2012) title and year confirmed via Semantic Scholar; publisher still needed. Caldwell & Frame (2016) names confirmed (Martha Caldwell, Oman Frame); verify Routledge.*

Annamma, S. A., Connor, D. J., & Ferri, B. A. (2013). Dis/ability critical race studies (DisCrit): Theorizing at the intersections of race and dis/ability. *Race Ethnicity and Education, 16*(1), 1–31.

Annamma, S. A., Ferri, B. A., & Connor, D. J. (2018). Disability critical race theory: Exploring the intersectional lineage, emergence, and potential futures of DisCrit in education. *Review of Research in Education, 42*(1), 46–71. https://doi.org/10.3102/0091732X18759041

Annamma, S. A., Jackson, D. D., & Morrison, D. (2017). Conceptualizing color-evasiveness: Using dis/ability critical race theory to expand a color-blind racial ideology in education and society. *Race Ethnicity and Education, 20*(2), 147–162. https://doi.org/10.1080/13613324.2016.1248837

Baker-Bell, A. (2020). *Linguistic justice: Black language, literacy, identity, and pedagogy*. Routledge.

Benjamin, R. (2019). *Race after technology: Abolitionist tools for the New Jim Code*. Polity.

Boateng, O., & Boateng, B. (2025). Algorithmic bias in educational systems: Examining the impact of AI-driven decision making in modern education. *World Journal of Advanced Research and Reviews.*

Bonilla-Silva, E. (2018). *Racism without racists: Color-blind racism and the persistence of racial inequality in America* (5th ed.). Rowman & Littlefield.

Bourdieu, P. (1986). The forms of capital. In J. G. Richardson (Ed.), *Handbook of theory and research for the sociology of education* (pp. 241–258). Greenwood Press.

Briggs, C. L. (1986). *Learning how to ask: A sociolinguistic appraisal of the role of the interview in social science research*. Cambridge University Press.

Buolamwini, J., & Gebru, T. (2018). Gender shades: Intersectional accuracy disparities in commercial gender classification. *Proceedings of Machine Learning Research, 81*, 77–91.

Caldwell, M. (2012). *Inquiry into identity: Teaching critical thinking through a study of race, class, and gender*. [publisher needed — title and year confirmed via Semantic Scholar]

Caldwell, M., & Frame, O. (2016). *Let's get real: Exploring race, class, and gender identities in the classroom*. Routledge. [verify publisher]

Chen, M., Khúc, M., & Kim, J. (2023). Work will not save us: An Asian American crip manifesto. *Disability Studies Quarterly, 43*(1). https://doi.org/10.18061/dsq.v43i1.9652

Chinta, S. V., Wang, Z., Yin, Z., Hoang, N., Gonzalez, M., Le Quy, T., & Zhang, W. (2024). *FairAIED: Navigating fairness, bias, and ethics in educational AI applications* [Preprint]. arXiv.

Crenshaw, K. (1989). Demarginalizing the intersection of race and sex: A Black feminist critique of antidiscrimination doctrine, feminist theory and antiracist politics. *University of Chicago Legal Forum, 1989*(1), 139–167.

Crenshaw, K. (1991). Mapping the margins: Intersectionality, identity politics, and violence against women of color. *Stanford Law Review, 43*(6), 1241–1299. https://doi.org/10.2307/1229039

D'Ignazio, C., & Klein, L. F. (2020). *Data feminism*. MIT Press.

Eubanks, V. (2018). *Automating inequality: How high-tech tools profile, police, and punish the poor*. St. Martin's Press.

Flores, N., & Rosa, J. (2015). Undoing appropriateness: Raciolinguistic ideologies and language diversity in education. *Harvard Educational Review, 85*(2), 149–171.

França, A. B. C., Reategui, E., Mintz, J., Meira, R. R., & Motz, R. (2024). Writing analytics and AI for special education: Preliminary results on students with autism spectrum disorder. *AIED Companion.*

Freire, P. (1970). *Pedagogy of the oppressed*. Continuum.

Garland-Thomson, R. (1997). *Extraordinary bodies: Figuring physical disability in American culture and literature*. Columbia University Press.

Heath, M. K., Gleason, B., Mehta, R., & Hall, T. (2023). More than knowing: Toward collective, critical, and ecological approaches in educational technology research. *Educational Technology Research and Development, 71*(3), 1013–1031.

Helm, P., Bella, G., Koch, G., & Giunchiglia, F. (2024). Diversity and language technology: How language modeling bias causes epistemic injustice. *Ethics and Information Technology, 26*, 8. https://doi.org/10.1007/s10676-023-09742-6

Hersey, T. (2022). *Rest is resistance: A manifesto*. Little, Brown Spark.

Hew, Z. K., et al. (2025). *MyCulture: Exploring Malaysia's diverse culture under low-resource language constraints* [Preprint]. arXiv:2508.05429.

Hoffmann, A. L. (2019). Where fairness fails: Data, algorithms, and the limits of antidiscrimination discourse. *Information, Communication & Society, 22*(7), 900–915. https://doi.org/10.1080/1369118X.2019.1573912

hooks, b. (1984). *Feminist theory: From margin to center*. South End Press.

hooks, b. (1994). *Teaching to transgress: Education as the practice of freedom*. Routledge.

Inoue, A. B. (2015). *Antiracist writing assessment ecologies: Teaching and assessing writing for a socially just future*. The WAC Clearinghouse; Parlor Press.

Jadhav, R., Danve, J., & Shaw, S. (2026). Implicit grading bias in large language models: How writing style affects automated assessment across math, programming, and essay tasks. [Preprint].

Kafer, A. (2013). *Feminist, queer, crip*. Indiana University Press.

Karinshak, E., Hu, A., Kong, K., Rao, V., Wang, J., Wang, J., & Zeng, Y. (2024). *LLM-GLOBE: A benchmark evaluating the cultural values embedded in LLM output* [Preprint]. arXiv. https://arxiv.org/abs/2411.06032

Kim, C., Passonneau, R. J., Lee, E., Sheikhi Karizaki, M., Gnesdilow, D., & Puntambekar, S. (2025). NLP-enabled automated assessment of scientific explanations: Towards eliminating linguistic discrimination. *British Journal of Educational Technology.*

Kwako, A., & Ormerod, C. (2024). Can language models guess your identity? Analyzing demographic biases in AI essay scoring. *BEA Workshop.*

Ladson-Billings, G., & Tate, W. F. (1995). Toward a critical race theory of education. *Teachers College Record, 97*(1), 47–68.

Leonardo, Z. (2009). *Race, whiteness, and education*. Routledge.

Liu, Z. (2024). *Evaluating and mitigating social bias for large language models in open-ended settings* [Preprint]. arXiv. [arXiv ID to verify]

Long, D. X., Nguyen, N.-H., Sim, T., Dao, H., Joty, S. R., Kawaguchi, K., Chen, N. F., & Kan, M.-Y. (2024). LLMs are biased towards output formats! Systematically evaluating and mitigating output format bias of LLMs. arXiv:2408.08656.

Lorde, A. (1988). *A burst of light: Essays*. Firebrand Books.

Loukina, A., Madnani, N., & Zechner, K. (2019). The many dimensions of algorithmic fairness in educational applications. In *Proceedings of the Fourteenth Workshop on Innovative Use of NLP for Building Educational Applications* (pp. 1–10). Association for Computational Linguistics.

Noble, S. U. (2018). *Algorithms of oppression: How search engines reinforce racism*. NYU Press.

Oakley, A. (1981). Interviewing women: A contradiction in terms. In H. Roberts (Ed.), *Doing feminist research* (pp. 30–61). Routledge.

Obermeyer, Z., Powers, B., Vogeli, C., & Mullainathan, S. (2019). Dissecting racial bias in an algorithm used to manage the health of populations. *Science, 366*(6464), 447–453.

Oketch, K., Lalor, J. P., Yang, Y., & Abbasi, A. (2025). Bridging the LLM accessibility divide: Performance, fairness, and cost of closed versus open LLMs for automated essay scoring. *arXiv.*

Omi, M., & Winant, H. (1994). *Racial formation in the United States* (2nd ed.). Routledge.

Queiroga, E. M., et al. (2022). *Early prediction of at-risk students in a deployed welfare classifier on Uruguayan national student data*. [tentative — venue and full author list to verify]

Schalk, S. (2018). *Bodyminds reimagined: (Dis)ability, race, and gender in Black women's speculative fiction*. Duke University Press.

Schaller, N.-J., Ding, Y., Horbach, A., Meyer, J., & Jansen, T. (2024). Fairness in automated essay scoring: A comparative analysis of algorithms on German learner essays from secondary education. In *Proceedings of the Workshop on Innovative Use of NLP for Building Educational Applications (BEA)* (pp. [pages]). Association for Computational Linguistics. [ACL anthology ID 2024.bea-1.18 — verify pages]

Schuman, H., & Presser, S. (1981). *Questions and answers in attitude surveys: Experiments on question form, wording, and context*. Academic Press.

Selbst, A. D., Boyd, D., Friedler, S. A., Venkatasubramanian, S., & Vertesi, J. (2019). Fairness and abstraction in sociotechnical systems. In *Proceedings of the Conference on Fairness, Accountability, and Transparency (FAT* '19)* (pp. 59–68). ACM. https://doi.org/10.1145/3287560.3287598

Shange, S. (2019). *Progressive dystopia: Abolition, antiblackness, and schooling in San Francisco*. Duke University Press.

Siebers, T. (2008). *Disability theory*. University of Michigan Press.

Smitherman, G. (1977). *Talkin and testifyin: The language of Black America*. Wayne State University Press.

Solórzano, D. G., & Yosso, T. J. (2002). Critical race methodology: Counter-storytelling as an analytical framework for education research. *Qualitative Inquiry, 8*(1), 23–44.

Stewart, T. T., Caldwell, M., & Hawkins, S. (2022). *Facilitating conversations about race in the classroom*. Routledge. [tentative — verify full author list, publisher]

Tan, M., Phalen, L., & Demszky, D. (2026). Marked pedagogies: Examining linguistic biases in personalized automated writing feedback. *International Learning Analytics & Knowledge Conference (LAK).*

Tanksley, T. (2023). Toward a critical race technology theory in education: Interrogating sociotechnical racism in educational research, pedagogy, and practice. *AERA Annual Meeting Proceedings.*

Tanksley, T. (2024). "We're changing the system with this one": Black students using critical race algorithmic literacies to subvert and survive AI-mediated racism in school. *English Teaching: Practice & Critique.*

Tuck, E. (2009). Suspending damage: A letter to communities. *Harvard Educational Review, 79*(3), 409–427.

Xu, X., He, X., Zhi, C., Chen, R., McAuley, J., & He, Z. (2025). *BiasFreeBench: A benchmark for mitigating bias in large language model responses* [Preprint]. arXiv. https://arxiv.org/abs/2510.00232

Yang, K., Raković, M., Li, Y., Guan, Q., Gašević, D., & Chen, G. (2024). Unveiling the tapestry of automated essay scoring: A comprehensive investigation of accuracy, fairness, and generalizability. *AAAI.*

Yosso, T. J. (2005). Whose culture has capital? A critical race theory discussion of community cultural wealth. *Race Ethnicity and Education, 8*(1), 69–91.
