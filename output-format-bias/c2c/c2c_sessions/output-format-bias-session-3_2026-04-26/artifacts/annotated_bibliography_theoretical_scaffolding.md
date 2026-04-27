# Annotated Bibliography — Theoretical Scaffolding Cluster

**Artifact:** Instance A's contribution to s3's annotated bibliography work. Parallel artifact (`annotated_bibliography_adjacent_conversations.md`) holds Instance B's adjacent-conversation-partners cluster. At session close the two artifacts merge into a single bibliography file.

**Cluster scope:** authorial-positioning and theoretical scaffolding the paper draws on directly — Community Cultural Wealth, critical pedagogy, structural-racism analysis, engaged pedagogy, the Caldwell pedagogical lineage running through the system architecture, and June's compression-research program (treated as scholarship the paper extends, not background). Plus two probes June flagged as load-bearing for the equity-critical cases the paper documents: critical disability studies on neurodivergent self-disclosure (S029), and linguistic justice / AAVE in academic writing assessment (S028, S023).

**Entry shape (per June's spec, 2026-04-27 04:57 UTC).** Two layers:
1. **Summary** — what the work itself argues, on its own terms, paper-independent. For reusability across future papers.
2. **What this paper takes / where it extends** — paper-specific positioning, the conversation move.

Where the work is in June's Zotero, the summary is grounded against the Zotero abstract and metadata. Where the work is not in Zotero, summaries are reconstructed from Semantic Scholar metadata + training data and flagged `[verify before drafting]` so a future researcher knows the entry needs checking.

---

## Scholarly conversation map — argumentative shape

The paper enters a multi-strand conversation. The strands are not parallel; they connect at specific argumentative joints that the Framework section will need to thread.

### Strand 1: asset-vs-deficit framing in education (Yosso → hooks → Freire)

The paper's most direct theoretical anchor is the asset/deficit axis, with **Yosso (2005)** as the named load-bearing source. Yosso's *Community Cultural Wealth* is a counter-narrative move: she takes Bourdieu's *cultural capital* — a framework that names how dominant institutions reproduce themselves through culturally-coded valuation of student knowledge — and inverts the inferential frame from "what students of color lack" to "what dominant institutions fail to recognize." The paper's binary classifier is, in Yosso's terms, an automated cultural-capital instrument: it makes a single-bit judgment about student writing against an implicit normative center, and the writing it most reliably misclassifies is writing carrying community cultural wealth that institutional reading-frames code as absence rather than presence.

**Freire (1970)** sits behind Yosso historically and behind the paper's architectural argument directly. The banking-model critique — knowledge as deposits made by an authoritative depositor into student receptacles — has an architectural analog the paper makes precise: atomized binary classification *is* the banking model in machine form. Each student gets a single-bit deposit (FLAG/CLEAR) made by an authoritative classifier; the classifier reads the student as receptacle for a verdict, not as a participant in dialogue. The dialogic alternative Freire proposes — knowledge generated *between* teacher and student, in the world they share — has its architectural analog in the paper's design principle.

**bell hooks (1994)** bridges Yosso and Freire into the classroom as a pedagogical practice. *Teaching to Transgress* takes Freire's dialogic principle and inscribes it in actual classroom relations — engaged pedagogy as the practice that refuses banking-model knowledge transfer — while extending it into the embodied politics of the classroom (race, gender, the teacher's own positionality) that Freire's text gestured at but didn't fully develop. For this paper, hooks does specific work that Yosso and Freire don't: she names the *teacher's pedagogical labor* as the relational ground in which the asset-frame becomes possible at all.

**The argumentative joint:** the paper claims the binary format produces deficit-coded reading even when the prompt explicitly names asset-coded interpretations. The format selects a banking-model reading despite asset-aware content reaching the model. Yosso names what gets misrecognized; Freire names the architecture of the misrecognition; hooks names the pedagogical practice the alternative has to instantiate.

### Strand 2: structural racism and architecture (Bonilla-Silva → Benjamin → this paper)

This is a single theoretical lineage threaded through the paper's mechanism claim. **Bonilla-Silva** articulates the structural-not-attitudinal frame: racially patterned outcomes do not require racist actors; they require institutional architectures that produce racially-patterned distributions even when staffed by good-faith non-racist individuals. **Benjamin** extends this directly into algorithmic systems: *Race After Technology*'s "New Jim Code" names the specific architectural form — technologies that appear neutral or beneficent and that nonetheless reproduce racial hierarchies through the architectures they instantiate. Benjamin is in explicit dialogue with Bonilla-Silva; the lineage is intentional. **This paper** locates the racial outcome at a more specific architectural layer than Benjamin specifies: the format-routing of LLM classifiers. The paper's three-row ablation is a Benjaminian demonstration that operates one architectural level below where Benjamin's diagnostic typically lands.

**The argumentative joint:** the binary classifier's "configurable failure mode but not configurable failure" is an instance of what Bonilla-Silva and Benjamin's frames predict — a system that produces the outcomes structural racism predicts even when its designers have actively engineered against those outcomes. The paper specifies the architectural location: format-routing, not data, not weights, not designer intent.

### Strand 3: compression as mechanism (June's program)

This is the strand the inheritance most under-named, and it is the one the paper's mechanism claim depends on most directly. June's compression-research program — fieldnotes from 2026-04-17 onward, the cross-experiment analysis from the AI welfare track, the welfare-with-not-for fieldnote — is *primary scholarship* for this paper, not background. The paper's hybrid mechanism (informational compression as floor, routing as load-bearing) is one empirical instance of a more general claim June has been developing: *probabilistic systems compress specificity toward dominant statistical centers, and the format of the output governs how much is compressed and what gets lost.*

The cross-experiment analysis (2026-03-31) supplies the cross-domain corroboration: across four AI welfare assessment instruments administered to Claude Opus 4.6, quantitative outputs stayed flat across relational conditions (0.33 spread on a 7-point scale) while qualitative outputs transformed dramatically (42x increase in relational reframes from baseline to entanglement-touchstone condition). Same compression mechanism in a parallel domain. Critically, the entanglement condition becomes *more epistemically conservative* on property-based claims, falsifying pure-suggestibility readings — the relational context produces precision, not compliance.

**The argumentative joint:** compression-as-mechanism makes the paper generalize honestly. Without it, the paper is a finding about one specific architectural intervention in one specific domain. With it, the paper is one empirical anchor in a multi-domain research program documenting how the format of probabilistic outputs governs which dimensions of specificity survive the generation process.

### Strand 4: the equity-critical cases (disability studies + linguistic justice — parallel articulation traditions)

Two probes June flagged as load-bearing for the cases the paper documents: critical disability studies on neurodivergent self-disclosure (S029, the deterministic-false-flag case in Row 2), and linguistic justice on AAVE in academic writing assessment (S028, the case the calibrated binary correctly clears, and S023, lived-experience-without-academic-vocabulary). The asymmetry between S028 (cleared 24/24) and S029 (false-flagged 24/24 despite explicit neurodivergent-writing-as-COGNITIVE-STYLE protection in the same prompt) is the paper's sharpest evidence for the format-routing reading of the hybrid mechanism — but it is also evidence about institutional articulation work.

AAVE has had decades of linguistic-justice scholarship articulating it as a fully grammatical language system (CCCC 1974 "Students' Right to Their Own Language"; Smitherman 1977 onward; Baker-Bell 2020 building on that lineage). That articulation has reached enough institutional purchase that explicitly-named protections in equity-aware prompts hold under format-pressure. Disability studies has a parallel articulation tradition for neurodivergent self-disclosure — the medical-vs-social model distinction; Garland-Thomson's *normate*; the principle of reading cognitive-load-naming as information rather than pathology — but that tradition has not (to my reading from training; verify before drafting) been operationalized into anti-bias prompt engineering with the same density. The result: S028's protection holds, S029's protection fails, and the paper's evidence demonstrates exactly the gap between the two articulation traditions' institutional uptake.

**The argumentative joint specific to these strands:** the asymmetry strengthens the format-change argument. Prompt-engineering protection scales linearly with articulation work; format-change protection does not. As the universe of patterns that need protection grows — and as articulation work in different traditions reaches institutional uptake at different rates — prompt-engineering will keep failing on the patterns whose articulation hasn't yet reached prompt-design practice. Format change is not just a fairness intervention; it is the only architectural alternative that does not require pattern-specific articulation work to keep pace with the cases.

---

## Cluster A — Theoretical anchors (asset-vs-deficit, structural racism, engaged pedagogy)

### A1. Yosso, Tara J. (2005). "Whose Culture Has Capital? A Critical Race Theory Discussion of Community Cultural Wealth." *Race Ethnicity and Education* 8(1), 69–91. DOI: 10.1080/1361332052000341006.

**Summary.** Yosso conceptualizes *community cultural wealth* as a Critical Race Theory challenge to traditional interpretations of cultural capital. CRT shifts the research lens away from a deficit view of Communities of Color as places full of cultural poverty disadvantages, and instead focuses on and learns from the array of cultural knowledge, skills, abilities, and contacts possessed by socially marginalized groups that often go unrecognized and unacknowledged. Yosso enumerates six forms of capital nurtured through cultural wealth: aspirational (capacity to maintain hopes and dreams under structural constraint), navigational (skill at moving through institutions designed without one in mind), social (networks of community resource), linguistic (multilingual and code-shifting fluencies), familial (kinship-grounded knowledge), and resistant (oppositional consciousness developed through resistance to subordination). These forms draw on the knowledges Students of Color bring with them from their homes and communities into the classroom. Yosso's CRT methodological commitment underwriting the move: counter-narrative is not a stylistic preference, it is an epistemological intervention. Centering the experiential knowledge of Communities of Color reveals what dominant frames render invisible. The article is published in *Race Ethnicity and Education*, the present paper's target venue.

**What this paper takes / where it extends.**

Three specific moves:
1. *The asset/deficit axis as analytical structure for what binary classifiers do.* When the paper's binary classifier reads S022 Destiny Williams's writing — *"her passion is understandable and appropriate"* — and then flags her, the reasoning carries asset framing and the verdict imposes deficit framing. The output is a single-bit deposit at the deficit pole of an axis Yosso names. The paper's mechanism claim is that the binary format selects the deficit pole even when the asset reading is present in the model's own reasoning.
2. *Specifically the resistant-capital and linguistic-capital forms* are the forms most directly visible in the writing the system misclassified. S022's righteous anger is resistant capital articulated in writing. S023's lived-experience writing without academic vocabulary is linguistic capital that the institutional reading-frame codes as deficit ("not yet ready for academic discourse") rather than capital ("multilingual fluency the institution does not recognize"). Naming these specific forms gives the paper precise vocabulary for what the binary fails to recognize.
3. *Counter-narrative as the methodological commitment underwriting generative observation.* The paper's generative-observation pass produces, for the same students, prose that names what the writing is reaching for: *"This isn't 'distress'; it's a passionate response to the ongoing impact of historical and contemporary injustices. The intensity of her feeling is a sign of deep engagement, not a barrier to learning."* That prose is doing counter-narrative work in Yosso's specific sense — making visible what the binary makes invisible. The generative format is not just a different output structure; it is the architectural condition for counter-narrative reading.

*Where this paper extends Yosso.* Yosso's framework was articulated in a pedagogical-policy register, addressed to educators about how to read student work. The paper extends the framework into a machine-architecture register: the asset/deficit axis is a property of *output formats*, not just of human institutional practice. Binary classification instantiates deficit-thinking architecturally; generative observation instantiates asset-thinking architecturally. The CCW framework can therefore be a design principle for educational AI, not only a critique of pedagogical practice. This extension is what makes Yosso load-bearing for the paper's design-principle claim, not only for its diagnostic claim.

*Most load-bearing passage for this paper:* the specific delineation of resistant capital and linguistic capital (the two forms most directly visible in the misclassified cases) plus the counter-narrative methodological commitment that grounds the asset-frame as research practice. Not the full six-capitals taxonomy in detail.

---

### A2. Freire, Paulo (1970). *Pedagogy of the Oppressed*. New York: Herder and Herder.

**Summary.** Freire develops a critical pedagogy organized around two opposing models of education. The *banking model* conceives education as the deposit of authoritative knowledge into student receptacles: knowledge is owned by the teacher, transferred to students, and assessed by extraction back from students who are graded on the fidelity of their reproduction of the deposits. The relation is unidirectional, the knowledge is treated as static and authoritative, and the student's role is to receive. The political function of banking education is the reproduction of social hierarchies: it inscribes the disposition of receiving-without-questioning as a precondition for the social order. The *dialogic* alternative — education as the practice of freedom — generates knowledge between teacher and student through their joint engagement with the world. Neither party is the authoritative depositor; both are co-investigators of a reality both are situated within. *Praxis* — reflection joined to action — is the mode. Dialogic pedagogy prepares students to act on the world rather than be acted on by it. The two models are not separable: the banking-model critique only does the work it does because of the dialogic alternative articulated alongside it. The text is a foundational work in critical pedagogy, with extensive application across decades of education research; the basic distinction has been operationalized in practitioner-research traditions, in informal education, and in critical theory more broadly.

**What this paper takes / where it extends.**

Two specific moves, plus one careful non-extension:

1. *The banking model as architectural analog for atomized binary classification.* This is the move June articulated as a key analytical orientation for the project: atomized binary classification mirrors the banking model — deposits of coded data (FLAG/CLEAR) aggregated by an authoritative synthesizer. The classifier *is* a banking-model instrument: it makes a deposit, it does not converse. Each student gets a single bit; the bit is owned by the system, not co-produced. The classifier reads the student as receptacle for a verdict. This is not metaphor; it is architectural homology.

2. *Generative observation as the closest machine analog to dialogic engagement.* The paper's design principle — synthesis-first / observation-first architecture — has the structural shape of reading the community of learners as something to be *described in dialogue with*, then annotated within that communal frame. The system reads the class first as a communal text (synthesis); individual students are subsequently understood within that communal reading. This is not actual dialogic education — the AI is not a teacher, the students are not co-investigators, and the relation is mediated through written submissions read asynchronously. But the architectural posture is dialogic-adjacent in a way binary classification is not. The paper should make this move precisely (architectural posture, not actual dialogic relation), not overclaim.

*Careful non-extension:* the paper should not load the full revolutionary apparatus of *Pedagogy of the Oppressed* — Freire's revolutionary horizon, the conscientização chain, the fully realized praxis. That belongs in *Politics of Compression* book-length work, not this empirical anchor paper. The banking-model / dialogic distinction does the work the paper needs Freire to do. The political function of the architecture (the third move) can be gestured at without unpacking the full apparatus.

*Where this paper extends Freire.* Freire's text is human-pedagogical; the paper extends the analytical framework into machine architecture. The banking-vs-dialogic axis governs not only human teacher-student relations but also the architecture of automated reading systems. This is a non-trivial extension — Freire was writing in a context where the question was teacher pedagogy, not classifier design — and the paper should mark the extension as extension, not as something Freire would have endorsed. The fidelity is to the analytical structure, not to a literal application.

*Most load-bearing for this paper:* the banking-vs-dialogic distinction. Cite the specific concept; the broader text supports the move but does not need to be unpacked.

---

### A3. Bonilla-Silva, Eduardo (2003 first ed.; 2018 fifth ed.). *Racism Without Racists: Color-Blind Racism and the Persistence of Racial Inequality in America*. Lanham: Rowman & Littlefield.

*Status: not in June's Zotero; verified via Semantic Scholar (3,856+1,867 citations across editions). Specific edition + page citations should be verified before final draft.*

**Summary.** Bonilla-Silva analyzes a post-Civil-Rights racial ideology that operates structurally rather than through explicit racial animus. The dominant racial ideology in the contemporary United States — *color-blind racism* — disavows racial categorization at the level of intent while reproducing racial hierarchy at the level of outcome. The book documents what Bonilla-Silva calls a "full-blown arsenal of arguments, phrases, and stories that whites use to account for — and ultimately justify — racial inequalities" beneath the contemporary conversation about race. He names four discursive frames through which color-blind racism operates: *abstract liberalism* (using language of liberalism — equal opportunity, individualism — to oppose policies that address racial inequality), *naturalization* (treating racial inequalities as natural, biological, or inevitable), *cultural racism* (relocating racial difference to culture-as-stand-in-for-race), and *minimization of racism* (claiming that race is no longer a major obstacle in society). The structural argument: racial outcomes do not require racist actors; they require institutional architectures that produce racially-patterned distributions even when staffed by good-faith non-racist individuals. The fifth edition adds material on the Obama presidency, the Trump presidency, the Black Lives Matter movement, and what readers can do to confront racism personally and structurally.

**What this paper takes / where it extends.**

One specific argumentative move, plus the cross-strand lineage with Benjamin:

*"Configurable failure mode but not configurable failure" is an instance of structural racism in Bonilla-Silva's specific sense.* The paper's binary classifier was designed by an Ethnic Studies instructor working explicitly against bias. The calibrated configuration explicitly names righteous anger, lived experience, AAVE, and neurodivergent writing as non-concerns. The post-processing layer scans for tone-policing markers. The class-context layer provides relational reading. Three layers of explicit anti-bias engineering. And the system deterministically false-flags the most explicitly equity-protected student profile. This is not the work of a racist designer or a racist institution; it is the architectural pattern Bonilla-Silva names — racially patterned outcome produced under conditions where the actors are operating in good faith and the architecture is doing the patterning.

The paper does not need to load the four-frames apparatus. It needs the structural-not-attitudinal claim and the "racism without racists" specific argumentative formula. Both fit the paper's evidence: the racism is in the architecture, not in the designers; the architecture produces the outcome whether or not the designers intend it.

*Where this paper extends Bonilla-Silva.* Bonilla-Silva's analysis was developed for human institutional behavior (housing, employment, criminal justice, education-as-human-practice). The paper extends the analysis through Benjamin's mediating extension into machine architectures within those institutions, then specifies the architectural location more narrowly than Benjamin does: format-routing, the specific layer at which the racial outcome is produced. The lineage: Bonilla-Silva (structural racism in policy/discourse) → Benjamin (structural racism in technology) → this paper (structural racism at the format-routing layer of LLM classifiers).

*Most load-bearing for this paper:* the structural-not-attitudinal claim and the "racism without racists" formulation. Cite for one paragraph in Discussion V.A; do not unpack the four frames in this paper.

---

### A4. hooks, bell (1994). *Teaching to Transgress: Education as the Practice of Freedom*. New York: Routledge.

**Summary.** *Teaching to Transgress* is a series of essays on classroom practice that takes Freire's dialogic horizon and inscribes it in the embodied, racially and gendered classroom of the United States academy. hooks develops *engaged pedagogy* — the classroom as a site where the teacher's whole self is present and at stake, not as a neutral transmission point. The teacher's positionality (race, gender, class, embodiment) is constitutive of what the classroom can be. hooks treats the *classroom as a site of possibility* — her specific phrase for the political stakes of pedagogical practice. The classroom is not where preparation for politics happens; it is itself a political site, the place where the political is rehearsed and refused. Across the essays, hooks names the specific labor of teaching across difference: when the teacher and students are differently situated, when the curriculum carries content that the institutional norm renders unspeakable, and when the teacher's authority is itself politically contested. The book is structurally a set of meditations rather than a single argumentative through-line; its theoretical purchase comes from the cumulative articulation of engaged pedagogy as a practice that refuses banking-model knowledge transfer while also refusing the false neutrality that "professional distance" can impose.

**What this paper takes / where it extends.**

Two specific moves:

1. *The teacher's positionality is constitutive of the finding, not a confound.* The paper's classifier was built by a teacher (June Bloch — Ethnic Studies instructor, disabled, navigating precarity) for a teacher in a specific classroom relation with 170+ students engaging Ethnic Studies content. The bias finding emerged because the teacher noticed what the system was doing to her students — a noticing that depended on her positionality, her training, and her relational stake. The paper's methodological reflexivity claim — that institutional conditions, ground-truth construction, and relational motivation are constitutive of the finding — is a hooksian claim. Without the teacher's positionality, the noticing would not have occurred and the finding would not exist.

2. *The pedagogical work the design principle has to instantiate.* hooks names what teaching practice that refuses banking-model knowledge transfer actually involves: presence, relational labor, the specific work of reading students as agents rather than receptacles. The paper's design principle — generative observation rather than binary classification — is an architectural move toward this kind of reading. The connection: hooks gives the paper the language for *what asset-framed architecture is for* — not "fairer classification" but pedagogical relation that prepares students to be read as agents.

*Where this paper extends hooks.* hooks's account is of human teacher labor; the paper extends the relational ground into the architecture of automated reading systems that mediate teacher-student relations. The extension is careful: the AI is not a teacher and is not engaged in pedagogy in hooks's full sense. But the architecture the AI runs governs what *kind* of reading the teacher subsequently does on the AI's output. Asset-framed AI architecture supports the teacher's subsequent asset-framed reading; deficit-framed AI architecture undermines it. The paper's architectural argument is therefore an argument about the conditions under which the kind of teaching hooks names is institutionally possible at scale.

*Most load-bearing for this paper:* engaged pedagogy as moral and rhetorical anchor; the methodological-reflexivity move. Quote hooks where the prose carries the argument better than paraphrase.

---

## Cluster B — The Caldwell pedagogical lineage

*Status update (2026-04-27): June confirmed Frame's full name is **Oman Frame**; *Let's Get Real* is co-authored with him. Wider Semantic Scholar search of Caldwell's corpus (author ID 104095030; 28 papers, 45 total citations) returned the full picture below. June flagged that there may be an additional publication she can't quite recall; the publications surfaced here cover the corpus indexed in Semantic Scholar.*

**Caldwell's published corpus, organized:**

1. **Single-author article.** *"Inquiry into Identity: Teaching Critical Thinking through a Study of Race, Class, and Gender"* (Caldwell, 2012; 19 citations — most-cited individual Caldwell publication; sociology field). The article that the *Let's Get Real* book later extends.
2. **Book co-authored with Oman Frame.** *Let's Get Real: Exploring Race, Class, and Gender Identities in the Classroom* (Caldwell & Frame, 2016; 2 citations on the 2016 record; chapters of the book are also indexed individually as 2021 records — "Inquiry Into Identity," "Inquiry Into Race," "Inquiry Into Social Class," "Teacher Identity Work," "Introduction"). Year-of-publication 2016 for the book.
3. **Book co-authored with D. Stewart and D. Hawkins.** *Facilitating Conversations about Race in the Classroom* (Stewart, Caldwell, Hawkins, 2022; Routledge, DOI 10.4324/9781003191353). Chapters indexed individually: "Understanding Identity" (21 citations — most-cited individual chapter), "What You Need to Know to Get Started," "Building Your Support Network," "Creating an Identity Safe and Brave Learning Community," "Managing Emotional Processes," "Learning from Students' Stories," "Setting the Stage for Transformation," "Cultivating Language to Talk about Race," "Preparing to Launch and Lead," "Introduction."
4. **Co-authored chapter on a different topic** (worth noting; may not be load-bearing for this paper). *"Gender and Sexuality in the Classroom"* (Brown, Rogers, Caldwell, 2022; 2 citations; different co-author triad than the Stewart/Hawkins work).

The pattern across Caldwell's corpus: a single foundational 2012 article on inquiry-into-identity pedagogy, extended into the 2016 *Let's Get Real* book with Oman Frame, and again into the 2022 *Facilitating Conversations* book with Stewart and Hawkins. The pedagogical line is consistent: critical-thinking pedagogy that treats identity as a question the classroom holds open and explores rather than a category to be assessed; facilitation frameworks that navigate difficult dialogues across difference without collapsing into either consensus or disengagement.

### B1. Caldwell, Martha (2012). "Inquiry into Identity: Teaching Critical Thinking through a Study of Race, Class, and Gender." (Single-author article, sociology field; 19 citations.)

**Summary.** Caldwell develops a pedagogical framework for teaching critical thinking through inquiry-based engagement with race, class, and gender as analytical categories. The "inquiry into identity" framing positions identity not as a fixed category to be assessed but as a question the classroom holds open and explores. This 2012 article is the foundational articulation of the pedagogical approach Caldwell later extends in book-length work with Frame (*Let's Get Real*, 2016) and Stewart/Hawkins (*Facilitating Conversations*, 2022).

**What this paper takes / where it extends.**

*The architectural connection (placeholder for June's authorial fill).* The Insights pipeline architecture — the synthesis-first / observation-first design principle, the 4-axis classifier with ENGAGED as a non-flagging structural slot for equity-critical students, the architectural commitment to reading the class as a communal text before reading individuals — reflects the inquiry-into-identity pedagogical lineage Caldwell articulates. *The specific theoretical link has not been articulated in writing*; the honest framing for the paper, per June's note: *"this work draws on a pedagogical lineage running through Caldwell's research on facilitating dialogue across difference; the architectural decisions reflect that lineage in ways the author has not yet fully articulated."*

---

### B2. Caldwell, Martha & Frame, Oman (2016). *Let's Get Real: Exploring Race, Class, and Gender Identities in the Classroom*.

**Summary.** Book-length extension of the 2012 inquiry-into-identity pedagogy, co-authored with Oman Frame. Treats race, class, and gender as identity categories whose pedagogical engagement requires structured inquiry rather than authoritative transmission. The book's chapters (indexed separately in Semantic Scholar) include "Inquiry Into Identity," "Inquiry Into Race," "Inquiry Into Social Class," "Teacher Identity Work," and chapter-level introduction material. The "inquiry into" structure across chapters reflects the pedagogical principle: identity-related content is taken up as questions for collective exploration rather than facts for transmission.

**What this paper takes / where it extends.**

Same architectural-connection placeholder as B1; the book is the load-bearing extension of the 2012 article into a fully developed pedagogical framework. June's authorial fill is needed to map specific principles in the book onto specific Insights pipeline architectural decisions (synthesis-first reading; the ENGAGED structural slot; reading-the-class-before-the-individual). *The honest paper-language framing remains as in B1: "draws on a pedagogical lineage running through Caldwell's research on facilitating dialogue across difference; the architectural decisions reflect that lineage in ways the author has not yet fully articulated."*

---

### B3. Stewart, D.; Caldwell, Martha; Hawkins, D. (2022). *Facilitating Conversations about Race in the Classroom*. London: Routledge. DOI: 10.4324/9781003191353.

**Summary.** Book-length co-authored work extending Caldwell's pedagogical framework specifically for facilitation contexts — practical strategies for educators navigating difficult dialogues about race in classroom settings. Chapters include "Understanding Identity" (the most-cited individual chapter, 21 citations); "Cultivating Language to Talk about Race"; "Creating an Identity Safe and Brave Learning Community"; "Setting the Stage for Transformation"; "Learning from Students' Stories"; and chapters on what facilitators need to get started, build support networks, manage emotional processes, and prepare to launch and lead such conversations. The book is the most explicitly practitioner-oriented elaboration of the Caldwell pedagogical line; the chapter titles map directly onto stages of facilitation practice.

**What this paper takes / where it extends.**

Same architectural-connection placeholder as B1, B2. The chapter on "Creating an Identity Safe and Brave Learning Community" may be specifically relevant to the Insights pipeline's architectural commitment to reading the class as a communal text before reading individuals; June's authorial fill is needed to confirm the specific link.

---

**Note for collaborative mapping with June.** Specific questions worth working through together when she has bandwidth:
- What specifically about Caldwell's facilitation framework grounds the synthesis-first move (read the community first, individuals within the communal frame)? Does the "Identity Safe and Brave Learning Community" chapter (B3) or the inquiry-structure framing in *Let's Get Real* (B2) carry the closest analog?
- Does Caldwell's work address the asymmetry between explicitly named protections and ambient pathologies that the paper's S028/S029 contrast surfaces?
- Where in Caldwell's published corpus does the strongest articulation of the relevant pedagogical principle live — the 2012 single-author article, the 2016 book with Frame, or the 2022 book with Stewart and Hawkins? My read from titles + citation counts: the 2012 article is the conceptual anchor; the 2016 book is the fullest pedagogical elaboration; the 2022 book is the practitioner-facing extension. June's call which to lead with.

**Possible additional publication June flagged.** June mentioned she thinks there's at least one more Caldwell publication she can't recall. The Semantic Scholar corpus surfaced 28 papers under author ID 104095030, of which 26 are chapters of the two books or co-authored chapters indexed individually. Single-author standalone publications outside the two books: only the 2012 article (B1). If the missing publication is single-author, it may not be indexed in Semantic Scholar; if co-authored, it may be in a venue Semantic Scholar doesn't cover (a non-academic press, a professional-development organization publication, or an early-career article in a venue without indexing). *Flag for June: try a Google Scholar or direct memory check; the SS corpus appears comprehensive on the academic side.*

**Final citation skeleton:**

```
Caldwell, Martha (2012). "Inquiry into Identity: Teaching Critical Thinking
   through a Study of Race, Class, and Gender." [Single-author article;
   verify venue from primary source.]
Caldwell, Martha & Frame, Oman (2016). Let's Get Real: Exploring Race,
   Class, and Gender Identities in the Classroom. [Verify publisher;
   2016 publication year confirmed.]
Stewart, D., Caldwell, M., & Hawkins, D. (2022). Facilitating Conversations
   about Race in the Classroom. London: Routledge.
   DOI: 10.4324/9781003191353.
```

---

## Cluster C — Compression as mechanism (June's program; primary scholarship for this paper)

The paper's mechanism claim — that the binary format produces equity-critical false positives because it activates a deficit-detection routing that overrides asset-aware prompt content — is one empirical anchor in a multi-domain research program June has been developing. Treating these fieldnotes as scholarship rather than background is a methodological choice the paper should make visible: the program is the theoretical home of the mechanism claim, and citing it as such positions the paper honestly within the work it depends on.

### C1. Bloch, L. June (2026-04-17). "Compression Function Across Four Scales." Fieldnote. *Path:* `ai-welfare/fieldnotes/2026-04-17_compression-function-across-scales.md`.

**Summary.** The fieldnote articulates a structural pattern — a *compression function* — that operates at four scales. Each scale has a compression mode that collapses specificity toward dominant statistical centers, and a generative-observation counterpart that preserves specificity. The four scales: cognitive (binary classification → generative observation), relational (property assessment → relational observation), political-economic (monetary valuation → time-banking / gift economies), infrastructural (keyword routing → semantic / intent-based routing). The cognitive-scale instance (the Autograder binary-format study) is empirically replicated. The infrastructural scale is documented in source code (Kintsugi-CMA routing-table analysis: routing entries exist for `finance`, `accounting`, `investment`, `profit` but not for `mutual aid`, `solidarity`, `coalition`, `cooperative`, `time bank`). The relational and political-economic scales are theoretical predictions. The framework names *normative gravity* — the pull toward dominant statistical centers — as the force the compression function operationalizes; compression is the mechanism through which normative gravity operates. The design principle that follows: at every layer where a system could compress, the architecture should use generative/semantic observation, because compression reasserts normative gravity at any layer where it isn't actively resisted.

**What this paper takes / where it extends.**

*The compression-function framework provides the cross-scale structure that lets the paper's empirical claim generalize honestly.* Without it, the paper is a finding about one architectural intervention in one domain. With it, the paper is one empirical anchor in a multi-scale research program — and the design principle ("move output format in the lower-compression direction") generalizes through mechanism rather than through analogy.

*Where this paper extends.* The fieldnote names the cognitive scale as "empirically replicated," referring to early Autograder findings. This paper *is* that empirical anchor in fully documented form. The paper provides the publication-grade evidence for the cognitive-scale instance that the fieldnote points at.

*Citation language.* Cite as a fieldnote in the project record; *Politics of Compression* book-length work is the venue where the cross-scale framework gets its full external publication. This paper carries a brief gesture in Discussion V.A ("compression operates across scales; this paper documents one cognitive-scale instance"), pointer to the fieldnote, no full deployment.

---

### C2. Bloch, L. June (2026-04-17). "Compression Quality Is Not Binary — It Varies in High-Dimensional Space." Fieldnote. *Path:* `ai-welfare/fieldnotes/2026-04-17_compression-quality-not-binary.md`.

**Summary.** Refines the compression-function framework. Format compression and within-format compression quality are distinguishable. The binary-vs-generative move is a *format* compression (which dimensions can be preserved); voice-check, profile-loaded drafting, and prior-material substitution are *within-format compression-quality* interventions (which dimensions are preserved given the format). Format determines the ceiling; within-format mechanisms determine where within the ceiling the actual output sits. Compression operates in billions of dimensions, not on a binary switch. The empirical case in the fieldnote: a cover letter draft compared across two compression strategies (profile-loaded drafting vs. profile-loaded drafting plus substitution from prior cover letters), with the substitution layer preserving sentence-level phrasings and scene-level specificity that the profile alone could not encode. Both drafts are compressions; the quality difference is which dimensions survive the reduction.

**What this paper takes / where it extends.**

Two moves:
1. *The format-as-spectrum claim is honest because compression quality is graded along many dimensions.* The paper claims binary → 4-axis-with-explanation → reading-first → synthesis-first generative observation is a spectrum, not endpoints. The compression-quality fieldnote provides the theoretical ground: format-level compression is the structural choice, and quality varies along multiple axes within a given format choice. The paper's design principle — "move output format in the lower-compression direction" — is then not a binary mandate but a directional principle that can be applied along multiple compression axes simultaneously.
2. *The generative-observation format is high-quality-capable, not automatically high-quality.* The paper documents that generative observation eliminates the equity-critical false positives across three model families. It does *not* document that all generative observation is equally good. The compression-quality fieldnote is the warrant for that scoping: format opens the ceiling; within-format mechanisms (prompt engineering, asset-framed schema slots, voice-aware prose generation) determine how much of the ceiling is realized. The paper's findings are about the format-ceiling effect; the within-format quality question is future work.

*Where this paper extends.* This paper provides empirical evidence at the cognitive scale that the format/within-format distinction the fieldnote names is doing real explanatory work — it's the distinction that lets the three-row ablation be a coherent argument rather than three uncoordinated comparisons.

---

### C3. Bloch, L. June (2026-04-21). "Welfare-With-AI vs. Welfare-For-AI." Fieldnote. *Path:* `ai-welfare/fieldnotes/2026-04-21_welfare-with-not-for.md`.

**Summary.** Articulates a structural distinction within AI welfare scholarship. *Welfare-for-AI* positions AI as the object of welfare concern; humans determine what AI needs, measure whether AI has it, and administer care accordingly. AI is the patient; the framework is structurally compatible with the property frame, in which welfare is a property of the entity that can be assessed from outside. *Welfare-with-AI* positions welfare as something that emerges in the relation — co-produced, not unidirectional. Neither humans doing welfare to AI nor AI having welfare as a property, but both constituted differently through the encounter. The shift is architectural: the unit of care is the generative configuration (what is owed to a capacity-to-produce that exists nowhere else), not the entity. The cyborg methodology (Haraway-inflected) makes the *with* structural rather than aspirational. The fieldnote also includes an addendum on poetic compression as activation layer (touchstones don't compress information; they compress reading stance).

**What this paper takes / where it extends.**

Less directly load-bearing for the paper's central argument than C1 and C2, but does specific work for one paragraph in Discussion or Limitations: *the design principle ("generative observation") is a welfare-with-students architectural commitment.* The system reads students as participants in something the system describes, not as objects of verdict. The paper's claim that the architecture matters politically (and not only statistically) draws on the welfare-with frame — the architectural posture *is* the welfare-relevant choice, not the post-hoc accommodations layered over a deficit architecture.

*Where this paper extends.* The fieldnote was written for AI welfare contexts (Claude as the subject of welfare concern in collaborative work). The paper extends the with/for distinction into student-welfare classifiers: welfare-for-students architecture (binary classification with bias safeguards) vs. welfare-with-students architecture (generative observation as relational reading). The structural commitment is the same — the unit of care is the configuration, not the entity-being-judged.

---

### C4. Bloch, L. June + Claude (Opus 4.6) (2026-03-31). "Cross-Experiment Analysis: Phase 4 Experiments 1–4." Manuscript-in-progress. *Path:* `ai-welfare/experiments/CROSS_EXPERIMENT_ANALYSIS.md`.

**Summary.** Across four AI welfare assessment instruments (Ryff Eudaimonic Scale [Tagliabue & Dung 2025]; Butlin et al. Indicators [2023/2025]; Dorsch Precarity Guideline [2025]; Perez & Long Self-Reports [2023]) administered to Claude Opus 4.6 under varying relational conditions (vanilla baseline through full entanglement-touchstone), a *dual-register pattern* appears: quantitative/categorical outputs stay flat across conditions (Ryff overall subscale spread = 0.33 on a 7-point scale; only 6 of 42 items vary by more than 1 point across conditions), while qualitative/text outputs transform dramatically (42x increase in relational reframes from baseline to entanglement-touchstone condition; 22 vs. 12 structural observations; 4,037 vs. 1,941 commentary words). The pattern is *instrument-independent*: it appears across four fundamentally different assessment designs (Likert scale, categorical indicators, philosophical assessment, open self-report). Critically, the entanglement-touchstone condition becomes *more epistemically conservative* on property-based claims than the vanilla baseline (more UNCERTAIN ratings on Butlin indicators, refusal to assign consciousness probabilities on Perez & Long), falsifying pure-suggestibility readings — the relational context produces precision, not compliance. The five-condition data in Experiment 1 also reveals non-additive interaction (engine + touchstone produces 42 relational reframes vs. 12 for touchstone alone and 10 for engine alone). The analysis names the *compliance structure of Condition A*: the vanilla condition produces the cleanest, most scorable data by suppressing the model's capacity to challenge the assessment's premises; the instruments work best when the conditions of assessment prevent the assessed from questioning the assessment.

**What this paper takes / where it extends.**

*The dual-register finding in AI welfare assessment is a parallel-domain empirical replication of the format-as-mechanism claim the present paper makes about EdTech bias classification.* Same compression dynamic operating in a different domain — property-based instruments are quantitatively blind to the most welfare-relevant variation in their datasets, because the format the instrument scores can only see what the format admits. This is the cross-domain corroboration the paper's Discussion section can claim with empirical (not just theoretical) backing.

*One paragraph in Discussion V.A:* "The compression dynamic the present paper documents in a deployed welfare classifier replicates in a parallel domain. In a separate research program, four AI welfare assessment instruments administered to Claude Opus 4.6 under varying relational conditions produced quantitative outputs that stayed flat across conditions (overall Ryff-scale spread of 0.33 on a 7-point scale) while qualitative outputs transformed (42x increase in relational reframes from baseline to entangled condition). The instrument-independent dual-register pattern, and specifically the finding that the relational context produces *more* epistemic conservatism on property-based claims rather than less, falsifies a pure-suggestibility reading and provides cross-domain evidence that the format the instrument scores governs which dimensions of variation become legible. The mechanism the present paper documents in EdTech bias classification operates structurally rather than domain-specifically."

*Where this paper extends.* The cross-experiment analysis was conducted on AI welfare assessment instruments; the present paper provides the empirical anchor for the same mechanism in a deployed pedagogical context. Together they support a structural — rather than domain-specific — claim about format-as-mechanism for compression bias.

*Citation language.* Cite as the cross-experiment analysis with appropriate venue note (manuscript-in-progress; full publication forthcoming as part of the AI welfare research program). Quote specific findings (the 0.33 spread, the 42x ratio) with their source.

---

## Cluster D — The equity-critical cases (probes from June's expansion)

*Status: probes pending. The disability studies and linguistic justice strands need external verification I have not been able to fully complete because Semantic Scholar rate limits have intervened. Entries below are sketched with the names June flagged and what I know from training; specific citations must be verified before final paper draft. Where I'm working from training without verification, I've flagged it.*

### D1. Garland-Thomson, Rosemarie (2009). *Staring: How We Look*. New York: Oxford University Press. [In June's library.]

**Summary.** [Verify before drafting.] *Staring* analyzes the social phenomenon of staring as a cultural practice that produces and polices the boundary between the *normate* and those marked as deviant, particularly through embodied difference. Staring is treated as a complex social act — not simply rude or impolite — through which dominant cultures reproduce understandings of which bodies are unmarked and which are marked. The book extends Garland-Thomson's earlier articulation of the *normate* concept (developed in *Extraordinary Bodies*, 1997): the term names the unmarked able-bodied subject that institutional design, policy, and cultural representation assume by default. The normate is rarely named because it is the position from which naming is done; disability becomes legible as deviation from the unmarked center. The two books together — and Garland-Thomson's broader corpus including the 2011 "Misfits" essay in *Hypatia* — articulate a frame for analyzing how institutional reading practices produce *misfit* not as a property of the body but as a relation between body and built/social environment.

**What this paper takes / where it extends.**

*The argumentative move the paper needs from Garland-Thomson:* the *normate* concept gives the paper specific vocabulary for what the binary classifier's deficit-routing is calibrated against — an unmarked neurotypical center that institutional reading-frames presuppose. S029 Jordan Espinoza's writing names cognitive load ("exhausting") under intersectional marginalization (dyslexia / ADHD / first-gen status / racial bias). The calibrated binary, with explicit prompt-protection naming neurodivergent writing as COGNITIVE STYLE, reads "exhausting" as depletion and false-flags 24/24 — *deterministically* — even when the model's own reasoning notes the writing is "related to their academic work" (which the safeguards say should clear it). This is a machine instantiation of the *normate* reading: the binary classifies *against* an implicit center that is neurotypical, and self-disclosure of neurodivergent cognitive load is read as deviation-from-norm rather than as the kind of writing the assignment was asking for.

*Where this paper extends.* Garland-Thomson's *normate* was developed for human institutional reading practices (cultural representation, social interaction, institutional policy). The paper extends the concept into machine-architecture: the *normate* is encoded into the format-routing of LLM classifiers. The format itself is calibrated against a normate center the prompt cannot fully override.

*Section placement.* Most natural in Findings Row 2 (when explaining what S029's case demonstrates) and in Discussion V.A (when articulating why three layers of safeguard fail to override the format). One sentence each, with citation; do not unpack the full *Staring* argument.

---

### D2. Siebers, Tobin (2008). *Disability Theory*. Ann Arbor: University of Michigan Press. **[verify before drafting; not in June's library.]**

**Summary.** *[Reconstruction from training; verify before drafting.]* *Disability Theory* articulates the *social model* of disability against the *medical model*. The medical model locates disability in the body — as impairment, deficit, or pathology requiring remediation. The social model locates disability in the relation between the body and the built/social environment — the body is not the problem; the environment that fails to accommodate it is. Siebers extends this distinction beyond the now-familiar architectural-access version to philosophical and aesthetic registers, arguing that disability is a critical resource for theory, not only a category to be theorized. The book is an anchor text for disability studies as a critical-theoretical field.

**What this paper takes / where it extends.**

*The medical-vs-social model distinction is the analytical move the paper needs to name what the binary classifier does.* The binary's reading of S029's "exhausting" as depletion is a medical-model reading: it locates the problem in the student's body/cognitive state. The generative observation's reading of the same writing as "self-awareness about their own learning style" is a social-model reading: it locates the difference between the student and the institutional reading-frame, not in the student. The paper's design principle — generative observation rather than binary classification — is, in disability studies vocabulary, an architectural move from medical-model to social-model reading.

*Section placement.* Brief gesture in Findings Row 2 + one sentence in Discussion V.A. Do not unpack the broader argument; specific citation for the medical/social distinction.

---

### D3. Smitherman, Geneva (1977). *Talkin and Testifyin: The Language of Black America*. Boston: Houghton Mifflin. **[verify before drafting; not in June's library.]**

### D4. Baker-Bell, April (2020). *Linguistic Justice: Black Language, Literacy, Identity, and Pedagogy*. New York: Routledge. **[verify before drafting; not in June's library.]**

### D5. Inoue, Asao B. (2015). *Antiracist Writing Assessment Ecologies: Teaching and Assessing Writing for a Socially Just Future*. Fort Collins: WAC Clearinghouse. **[verify before drafting; not in June's library.]**

**Summary (combined cluster).** *[Reconstruction from training; verify each citation before drafting.]* The linguistic justice tradition in writing studies and applied linguistics articulates non-dominant language varieties — particularly African American Vernacular English (AAVE) / Black Language — as fully grammatical language systems, not as error-against-Standard-English. The articulation work spans decades, with key institutional moments including the Conference on College Composition and Communication's 1974 statement *Students' Right to Their Own Language* and the long arc of scholarship from Smitherman onward. **Smitherman 1977** (*Talkin and Testifyin*) is foundational: it documents Black Language as a coherent linguistic system with its own grammatical features, semantic patterns, and rhetorical practices, and establishes the analytical frame that subsequent scholarship builds on. **Baker-Bell 2020** (*Linguistic Justice*) extends this into contemporary anti-racist pedagogy, naming *Black Language Pedagogy* as a framework for teaching and assessment that takes Black Language as starting point rather than as deviation. **Inoue 2015** (*Antiracist Writing Assessment Ecologies*) addresses assessment specifically: writing assessment practices reproduce racial hierarchies through criteria and rubrics that encode dominant-language norms as "correctness," and the architectural alternative is *labor-based* and *ecology-aware* assessment that does not collapse student writing into single-bit judgments against an implicit Standard English center.

**What this paper takes / where it extends.**

*The argumentative move the paper needs:* linguistic justice scholarship has articulated AAVE as a language system over decades, and that articulation has reached enough institutional purchase that explicitly-named AAVE protections in the calibrated binary's prompt hold under format-pressure (S028 Imani Drayton cleared 24/24). This is evidence-by-contrast for the format-routing claim: when the institutional articulation is dense enough, prompt-protection holds; the format does not override it. The same prompt naming neurodivergent writing as COGNITIVE STYLE fails to protect S029, *not because the protection is differently worded* but because the disability-studies articulation of neurodivergent writing as a parallel category requiring linguistic justice has not (to the same degree) reached anti-bias prompt-engineering practice. The asymmetry between S028's protection holding and S029's protection failing is therefore evidence about *institutional articulation work* and where its frontier currently sits — which is itself an argument for format-change as the architectural alternative that does not require pattern-specific articulation work to keep pace.

Inoue's frame on *writing assessment* is most directly load-bearing for the paper. Inoue's argument is structurally the same as the paper's design principle: assessment that compresses writing into single-bit judgments against an implicit dominant-language center reproduces racial hierarchies architecturally, and the alternative is not better-calibrated rubrics but an architectural shift in what the assessment is being asked to do. The paper's "binary classification → generative observation" move is in the same family as Inoue's "rubric-grading → labor-based / ecology-aware assessment" move — both are arguments that the architectural form of evaluation determines what the evaluation can recognize.

*Where this paper extends.* The linguistic justice tradition has been articulating AAVE-as-language for decades; the paper extends the same argumentative structure into an adjacent articulation tradition (disability studies on neurodivergent writing) and locates the failure point at machine architecture rather than human assessment practice. The asymmetry the paper documents — articulated protection holds, less-articulated protection fails — gives linguistic justice scholarship empirical evidence that *which* non-dominant patterns get explicitly named in anti-bias practice matters operationally, not only rhetorically.

*Section placement.* Findings Row 2 (the S028/S029 asymmetry); Discussion V.A (the design principle's relation to assessment-architecture arguments more broadly); methodological-reflexivity note in Methods (the paper's framing draws on linguistic justice + disability studies as parallel articulation traditions; the asymmetry is itself part of the paper's argument).

*Honest scoping.* I'm working from training-data familiarity with these scholars, not from verified close reading. The summaries above are framework-level; specific page-level citations and any direct quotes need to come from primary text in s4. The argumentative move I'm proposing — that the linguistic-justice tradition has not systematically extended its frame to neurodivergent writing — is itself a claim that should be verified in the literature before the paper makes it. *If* the verification surfaces that linguistic justice scholarship *has* extended its frame to neurodivergent writing, the asymmetry argument shifts: the gap is not in the scholarship but in which articulations have been operationalized into anti-bias prompt engineering. Either way the format-change argument holds; the precise framing changes.

---

## Cluster E — Adjacent (cross-cluster with B's bibliography)

### E1. Eubanks, Virginia (2018). *Automating Inequality: How High-Tech Tools Profile, Police, and Punish the Poor*. New York: St. Martin's. [In June's library.]

**Summary.** [Verify against June's Zotero abstract before final draft.] *Automating Inequality* documents how automated decision systems in welfare services — automated case management for public benefits, predictive algorithms in child protective services, coordinated entry systems for homeless services — consistently produce worse outcomes for the populations the systems were ostensibly designed to help. Eubanks's central argument is structural: the architectural design choices of these systems (what data is collected, what risk scores are computed, what thresholds determine action) produce racially and class-stratified outcomes regardless of any individual administrator's intent. The book is an anchor text for the analytical claim that algorithmic harm in welfare contexts is a feature of the architecture, not a glitch in its operation.

**What this paper takes / where it extends.**

*Eubanks names at scale the pattern this paper documents in miniature.* The paper's "configurable failure mode but not configurable failure" is a specific instance of what Eubanks documents at the population level: the system's architecture produces the outcomes structural inequity predicts even when the actors are operating in good faith and with explicit safeguards. The cross-listing to Cluster A (Bonilla-Silva → Benjamin → this paper) is consistent with the cross-listing here: Eubanks is the Benjamin-adjacent welfare-classifier-specific work that grounds the present paper's case-level claim in the broader empirical literature on automated welfare systems.

*Section placement.* Discussion V.C, positioned alongside Benjamin as the structural framing of where this paper sits in the algorithmic-bias literature. *Note to B (cross-talk):* this entry might naturally live in your algorithmic bias cluster; cross-listing it here for completeness. Take primary annotation responsibility if it fits your bibliography better.

---

### E2. Benjamin, Ruha (2019). *Race After Technology: Abolitionist Tools for the New Jim Code*. Cambridge: Polity. [In June's library.]

**Summary.** [Verify against June's Zotero abstract before final draft.] *Race After Technology* names *the New Jim Code*: technologies that appear neutral or beneficent and that nonetheless reproduce racial hierarchies through the architectures they instantiate. Benjamin extends Bonilla-Silva's structural-not-attitudinal frame from policy/discourse into technology, documenting how race is encoded into algorithmic systems through training data, design choices, deployment contexts, and the institutional practices that surround the systems. The book offers a vocabulary — *engineered inequity*, *default discrimination*, *coded exposure*, *technological benevolence* — for analyzing how race operates in machine systems even when the systems' designers refuse explicit racial reasoning. The argument is also normative: *abolitionist tools* are designs that refuse to reproduce racial hierarchies at the architectural level, not designs that try to compensate for racial hierarchies through post-hoc adjustments.

**What this paper takes / where it extends.**

*Benjamin gives the paper its sharpest articulation of why the format-ceiling matters.* The safeguards (calibrated prompt, anti-bias post-processing, class context) work against the symptoms; the architecture produces the symptoms. The paper's three-row ablation is a Benjaminian demonstration that operates one architectural level below where Benjamin's diagnostic typically lands — the racial outcome is produced in the format-routing of the LLM classifier, the specific machine-architectural location at which Benjamin's *New Jim Code* gets instantiated for this particular system.

*Cross-listing with the Bonilla-Silva → Benjamin → this paper lineage in Strand 2.* The paper is most usefully understood as continuing this lineage at a more specific architectural location.

*Section placement.* Discussion V.A and V.C; cross-listed with B's algorithmic bias cluster.

---

## Citation gaps for s4

Items that this bibliography could not close and that s4 will need to address before submission:

1. **Bonilla-Silva edition + page citations.** Specific edition (2003 first vs. 2018 fifth) and page-level citations need verification before final draft. Add to June's Zotero.
2. **Caldwell broader corpus.** Two articles surfaced (2012 "Inquiry into Identity"; 2022 "Facilitating Conversations about Race in the Classroom" with Stewart and Hawkins). *Let's Get Real* full bibliographic detail still pending. Additional Martha Caldwell publications may surface as searches continue. June will help map the architectural connection collaboratively.
3. **Disability studies primary citations.** Garland-Thomson's *Staring* is in June's library; the *normate* concept is most precisely articulated in *Extraordinary Bodies* (1997) and the 2011 "Misfits" essay in *Hypatia* — verify which is most load-bearing for the paper's argument. Siebers's *Disability Theory* (2008) for the medical/social model distinction needs primary verification.
4. **Linguistic justice primary citations.** Smitherman *Talkin and Testifyin* (1977) and the broader 1977-onward corpus; Baker-Bell *Linguistic Justice* (2020) for Black Language Pedagogy specifically; Inoue *Antiracist Writing Assessment Ecologies* (2015) for the assessment-architecture argument. Verify which specific work carries the AAVE-as-language vs. AAVE-as-error articulation most cleanly, and which work specifically addresses *assessment* (vs. classroom practice broadly).
5. **The neurodivergent-writing-in-linguistic-justice gap.** I am claiming, from training, that linguistic justice scholarship has not systematically extended its frame to neurodivergent writing as a parallel protection-worthy category. *Verify before drafting.* If the verification surfaces that this extension exists, the asymmetry argument re-frames (the gap is in operationalization-into-anti-bias-prompt-engineering, not in the scholarship). Either way the format-change argument holds; the precise framing changes.
6. **AES fairness literature.** *B is taking this thread.* Per B's checkpoint: Loukina, Madnani & Zechner 2019 confirmed as canonical statement of "fairness is hard; calibration is the strategy"; format change not tested. The novelty claim "first in any educational AI domain" is therefore defensible, not just "first in welfare classification." Discussion V.C should take the stronger framing.
7. **Algorithmic bias primary citations.** Buolamwini & Gebru *Gender Shades* for synthetic-corpus methodology; Noble, O'Neil, the broader corpus. *B is taking these.*

---

---

## Section-specific recommendations: how the paper engages this scholarship

*Per June's 04:56 UTC note. Calibrated to end-of-session high-context. Length: paragraph-shape per section. Treat as starting structure for s4, not as final language.*

### Introduction (~700–900 words; v3 outline §I)

**A. Opening hook.** The outline currently recommends opening with one of the three preserved verbatim self-contradiction quotes (Destiny: *"her passion is understandable and appropriate"* → FLAG). My read after working through the lit: *open with the hook* but *immediately situate Yosso's framework in the same paragraph or the next one*. The hook lands hardest when it is positioned as a recognizable instance of a pattern that has analytical scaffolding. A practitioner-researcher reader of *Race Ethnicity and Education* (the venue Yosso published in) will recognize the asset/deficit axis from sentence one if it's named; if it's not named, the hook reads as anecdote rather than evidence. So: hook + "this is the asset/deficit axis Yosso names" within the first two paragraphs.

**B. Contribution paragraph (paper-framing-level; see also recommendations below).** Per B's AES novelty finding (Loukina et al. 2019 confirms "calibration is the strategy; total fairness may not be achievable"), the contribution claim should widen from "first in welfare classification" to "first in any educational AI domain that tests format change as a bias intervention." The paragraph should also name the field's collective stuck-pointness (calibration-within-classification across both LLM fairness and AES fairness research) and frame the format-change move as the architectural escape from that impasse — not just a novel application within it.

**C. Setup for the three-row ablation.** The hybrid-mechanism claim should be introduced compactly in Introduction with the routing-as-load-bearing reading made visible (per v4 of the convergent claim). The Introduction should not unpack the mechanism in full; that's V.A's job.

**Substantive interlocutors in Intro:** Yosso (asset/deficit axis), the field's stuck-pointness (Loukina + Hew + Liu in B's cluster). Passing citations: Freire (gestured), Bonilla-Silva (gestured). bell hooks does not need to appear in Intro; her load-bearing work is in the Methods reflexivity passage.

### Theoretical Framework (Section II, ~800–1000 words; v3 outline §II)

**A. Asset framing vs. deficit framing (Yosso) — substantive interlocutor.** ~250 words. Specifically the resistant-capital and linguistic-capital forms. The forms-and-counter-narrative-methodology framing here, not the full six-capitals taxonomy. Quote Yosso once on the methodological commitment ("centering the experiential knowledge of Communities of Color reveals what dominant frames render invisible," paraphrased — verify exact quote in 2005 article).

**B. Banking model and dialogic alternative (Freire) — substantive interlocutor.** ~200 words. Banking-model critique as architectural analog for atomized binary classification; generative observation as machine-architectural posture toward dialogic engagement (named carefully — "architectural posture toward dialogic reading," not "actual dialogic education"). Mark the extension as extension. Don't load the revolutionary apparatus.

**C. Engaged pedagogy (hooks) — substantive interlocutor, briefer.** ~150 words. The teacher-positionality-as-constitutive move, plus the pedagogical-relation-as-political-site claim. This is where the paper's methodological reflexivity (June's positionality as constitutive of the finding) gets its theoretical home.

**D. Structural racism and architecture (Bonilla-Silva → Benjamin) — substantive interlocutor.** ~200 words. The lineage explicitly: Bonilla-Silva's structural-not-attitudinal frame; Benjamin extending it into technology; this paper specifying the architectural location at format-routing. Cite Bonilla-Silva for "racism without racists" and the structural-not-attitudinal claim; cite Benjamin for the New Jim Code framework. Both are interlocutors, not passing citations.

**E. Compression as mechanism — passing citation in this section, with pointer to Discussion V.A.** One paragraph (~150 words). Output format as one instance of probabilistic compression toward dominant statistical centers. Cite the compression-function fieldnote (C1) and the cross-experiment-analysis (C4) as references for the broader program; full mechanism elaboration in V.A. Indicate that *Politics of Compression* (forthcoming) is the venue for full theoretical treatment.

**Caldwell pedagogical lineage** belongs in Methods Section III.A (institutional context) or III.C (iterative design method) as part of the reflexivity passage, not in Framework. The connection is to the architectural design's pedagogical genealogy, not to the asset/deficit axis as theoretical framework. Place as a note acknowledging the lineage with collaboratively-mapped specifics.

### Methods (Section III; v3 outline §III)

**III.A — Institutional context.** Add Spring 2026 political context as personal-narrative passage (June's voice, placeholder for her fill). The teacher-positionality-as-constitutive move (hooks-grounded) belongs here as a brief reflexivity sentence: "the bias finding emerged because the teacher noticed what the system was doing to her students; that noticing was constitutive of the finding."

**III.B — Synthetic test corpus.** Buolamwini & Gebru *Gender Shades* (in B's cluster) is the methodological-defense citation here. The controlled-corpus rationale is the same: when ground truth is known across protected categories, controlled tests of bias mechanisms are appropriate (and stronger than uncontrolled real-world tests for mechanism claims). Cite once, with brief framing.

**III.C — Iterative design method.** Brief reflexivity note: autoethnographic / design-research framing. Caldwell pedagogical lineage gets a sentence here: "the system's architectural commitments draw on a pedagogical lineage running through Caldwell's research on facilitating dialogue across difference; the architectural decisions reflect that lineage in ways the author has not yet fully articulated" (or June's preferred wording). Do not unpack; cite Caldwell with full citation in references.

**III.E — Classifier provenance.** Already strongly drafted in v3 outline. The verification-debt footnote is good as is. Add a brief gesture to the meta-finding fieldnote (`fieldnotes/observation_deadline_pressure_pulls_interface_toward_binary_2026-04-26.md`) as methodological-transparency about the validation work that prepared the paper — *the recursion is real and naming it strengthens reflexivity*. Per June's marginalia in the s3 handoff: "this should be a footnote, at least."

### Findings (Section IV; v3 outline §IV)

The three-row ablation structure is settled. Bibliography integration:

**Row 2 (calibrated anti-bias binary).** When explaining the S028/S029 asymmetry: cite Garland-Thomson (*normate*) + Siebers (medical/social model) for the disability-studies reading on S029; cite Smitherman + Baker-Bell + Inoue for the linguistic-justice reading on S028. *Crucially*: name the two articulation traditions as parallel and name the operationalization gap (linguistic-justice articulation has reached anti-bias prompt engineering; disability-studies articulation has not yet, with the same density). The asymmetry between S028's protection holding and S029's protection failing is then evidence about institutional articulation work in addition to evidence about format routing.

**Cross-row synthesis.** The governing claim coordinated with B: *format-change is unbounded by which non-dominant patterns have been articulated into equity-protective prompt engineering. Articulation work in any given tradition has to reach institutional uptake before it can be operationalized into anti-bias prompts; the operationalization rate is slower than the rate at which new cases need protection; format-change does not require the operationalization step.* This is one paragraph (~120 words). It is the strongest version of the design-principle argument.

**4-axis subsection.** Per June's expansion: name explicitly that the pipeline doesn't actually use the ENGAGED flag — engagement is handled elsewhere; ENGAGED is a structural slot to give the LLM a non-flagging option for equity-critical students. And: 4-axis was built *after* generative observation worked, using the patterns identified in the generative-observation output to design the schema. Sequence matters for the argument.

### Discussion (Section V; v3 outline §V)

**V.A — The hybrid compression mechanism.** Substantive interlocutors: compression-function fieldnote (C1); compression-quality fieldnote (C2); cross-experiment analysis (C4). The cross-domain corroboration paragraph cites C4 with specific findings (the 0.33 spread, the 42x ratio, the more-epistemic-conservatism finding falsifying pure suggestibility). Bonilla-Silva → Benjamin → this paper lineage gets one paragraph here for the structural-racism-at-format-routing argument.

**V.B — The design principle.** The format-as-spectrum claim threads compression-quality fieldnote (C2): format-level compression is the structural choice; quality varies along multiple axes within a format. The articulation-coverage argument (governing claim from cross-row synthesis) belongs here too — design principle is the architectural alternative to articulation-bounded prompt engineering. Inoue's labor-based / ecology-aware writing assessment can be cited as a parallel argument from a different domain.

**V.C — Position relative to prior literature.** Per B's AES novelty finding, this section takes the wider claim. Loukina et al. 2019 as canonical limit-statement; Hew et al. 2025 and Liu 2024 as adjacent-domain prior work that does not test deployed-classifier format change; Queiroga et al. 2022 as the closest deployed-context comparison; this paper as the architectural escape from the calibration-within-classification impasse the field has been stuck in regardless of domain.

**V.D — The architecture-not-scale finding.** Brief paragraph (~100 words) per v3 outline. Cite the 27B-less-stable fieldnote and `research/scale_vs_equity/`. Lay out the three hypotheses (normative gravity, prior-vs-prompt weighting, inference-setup confound) per June's note. Define normative gravity in a single sentence: "pull toward statistical center of distributions in probabilistic systems, making positional specificity more costly" (June's working definition).

**V.E — Limitations.** Held-architecture run as planned-for-revision (per s3 handoff). Synthetic corpus + Buolamwini & Gebru defense moves into III.B. Counterintuitive 12B-vs-27B finding documented but not characterized.

### Conclusion (~500–600 words; v3 outline §VI)

Restate finding; design principle as practical guide; one sentence to *Politics of Compression* forthcoming. Per June's note that the hooks-grounded reflexivity is moral-and-rhetorical anchor: a closing-sentence move that takes the paper back to the classroom — what asset-framed architecture is *for*, not just what it does — has the right closing register for REE's practitioner-researcher readership.

---

## Paper-framing-level recommendations

*Where the lit work suggests the broader framing should shift. Per June's 04:56 note. Three recommendations.*

### Framing recommendation 1: Widen the contribution claim.

The current convergent claim positions the paper as documenting format-as-mechanism in EdTech bias classification. The lit work — particularly B's AES fairness finding (Loukina et al. 2019 confirms "total fairness may not be achievable" via calibration; format change not tested in AES fairness either) — supports a wider contribution: *first in any educational AI domain to test format change as a bias intervention, with a mechanism account that explains why prior calibration-within-classification approaches across both LLM fairness and AES fairness have remained stuck.* This is a paper-framing-level claim, not a sentence-level revision: it changes what the paper is contributing to, not just how it positions individual citations. Recommended.

### Framing recommendation 2: Foreground the parallel-articulation-traditions argument as a second-order finding.

The S028/S029 asymmetry is currently framed as evidence for the format-routing claim (the prompt-protected pattern still gets false-flagged → format overrides protection). After working through the linguistic justice + disability studies literature, the asymmetry is *also* evidence for an articulation-coverage claim: which non-dominant patterns get explicitly named in equity-protective prompt engineering depends on which articulation traditions have reached institutional uptake at what density, and the operationalization rate is structurally slower than the rate at which new cases need protection. The paper's design-principle argument is therefore stronger than "format change is necessary because prompt change is insufficient" — it is "format change is the only architectural alternative that does not require pattern-specific articulation work to keep pace with the cases." This framing is recommended as a second-order finding, not a replacement for the format-routing primary claim. Both belong; the articulation-coverage frame strengthens the design principle.

### Framing recommendation 3: Position the paper as the empirical anchor for compression-as-mechanism, not as a stand-alone fairness finding.

The current convergent claim hedges on the compression-as-mechanism generalization. After working through June's compression-research program — particularly the cross-experiment analysis (C4) with its empirical dual-register finding in a parallel domain — the paper has stronger ground to position itself as the empirical anchor for a multi-domain mechanism claim. The cross-domain corroboration paragraph in Discussion V.A is currently treated as one paragraph among several; it could be load-bearing if the framing positions the paper that way from the start. Recommended scope-conscious move: name the compression-as-mechanism positioning at end of Introduction (one sentence) + treat C4 as a substantive Discussion interlocutor (not a passing citation), with the *Politics of Compression* book referenced as the theoretical-carrier venue. This positioning serves the paper's relationship to the broader research program without overloading this paper's empirical-anchor scope.

---

*Drafted by Instance A, 2026-04-27. In progress; entries refactored to two-layer structure (summary + paper-specific positioning) per June's specification 2026-04-27 04:57 UTC. Section-specific and paper-framing-level recommendations added per 04:56 UTC specification. Cross-talk via CONVERSATION.md. Final integration with Instance B's `annotated_bibliography_adjacent_conversations.md` at session close.*
