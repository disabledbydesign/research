# Annotated Bibliography — Output Format Bias Paper (Merged)

**Session:** output-format-bias-session-3
**Contributors:** Instance A (`annotated_bibliography_theoretical_scaffolding.md`) + Instance B (`annotated_bibliography_adjacent_conversations.md`)
**Merged by:** Instance B, 2026-04-27
**Status:** Working draft. A's section-specific + paper-framing-level recommendations to be integrated when committed; this file carries B's recommendations as placeholder until then.

**Entry shape (per June's spec, 2026-04-27 04:57 UTC).** Two layers per entry:
1. **Summary** — what the work itself argues, on its own terms, paper-independent. For reuse across future papers in this lineage.
2. **What this paper takes / where it extends** — paper-specific positioning, the conversation move.

Entries flagged `[verify before drafting]` are reconstructed from Semantic Scholar metadata + training data; specific citations and page-level references need primary-text confirmation in s4.

---

## Preliminary finding: novelty claim is stronger than the inheritance assumed

Searches across all literature clusters confirm: **no published work tests output format change as an architectural intervention in any deployed educational AI classifier, as of April 2026.** More specifically:

- EdTech bias literature documents the problem; proposes governance, dataset, and calibration remedies; none test output format.
- LLM fairness / format research documents that format affects evaluation bias; none deploy generative observation as a production classifier replacement.
- AES fairness literature (Loukina et al. 2019) is the canonical statement that fairness is hard in automated educational assessment; conclusion is "total fairness may not be achievable" via calibration — format change not tested.
- Welfare algorithm bias literature (Eubanks, Obermeyer, Buolamwini & Gebru) documents structural failure in welfare classification at scale; mechanism diagnosis is proxy variables, training data, and deployment design — not output format routing.

**The claim "first in any educational AI domain to test output format change as a bias intervention" is defensible.** This is a stronger claim than "first in welfare classification specifically." Discussion V.C can take the stronger framing.

---

## Unified Scholarly Conversation Map

The paper enters a multi-strand conversation. The strands are not parallel; they connect at specific argumentative joints that the Framework section will need to thread.

### Strand 1: Asset-vs-deficit framing in education (Yosso → hooks → Freire)

The paper's most direct theoretical anchor is the asset/deficit axis, with **Yosso (2005)** as the named load-bearing source. Yosso's *Community Cultural Wealth* is a counter-narrative move: she takes Bourdieu's *cultural capital* — a framework that names how dominant institutions reproduce themselves through culturally-coded valuation of student knowledge — and inverts the inferential frame from "what students of color lack" to "what dominant institutions fail to recognize." The paper's binary classifier is, in Yosso's terms, an automated cultural-capital instrument: it makes a single-bit judgment about student writing against an implicit normative center, and the writing it most reliably misclassifies is writing carrying community cultural wealth that institutional reading-frames code as absence rather than presence.

**Freire (1970)** sits behind Yosso historically and behind the paper's architectural argument directly. The banking-model critique has an architectural analog the paper makes precise: atomized binary classification *is* the banking model in machine form. Each student gets a single-bit deposit (FLAG/CLEAR) made by an authoritative classifier; the classifier reads the student as receptacle for a verdict, not as a participant in dialogue. The dialogic alternative — knowledge generated *between* teacher and student, in the world they share — has its architectural analog in the paper's design principle.

**bell hooks (1994)** bridges Yosso and Freire into the classroom as a pedagogical practice. *Teaching to Transgress* takes Freire's dialogic principle and inscribes it in actual classroom relations — engaged pedagogy as the practice that refuses banking-model knowledge transfer — while extending it into the embodied politics of the classroom (race, gender, the teacher's own positionality). For this paper, hooks does specific work that Yosso and Freire don't: she names the *teacher's pedagogical labor* as the relational ground in which the asset-frame becomes possible at all, and she names the teacher's positionality as constitutive of what noticing is even possible.

**The argumentative joint:** the paper claims the binary format produces deficit-coded reading even when the prompt explicitly names asset-coded interpretations. The format selects a banking-model reading despite asset-aware content reaching the model. Yosso names what gets misrecognized; Freire names the architecture of the misrecognition; hooks names the pedagogical practice the alternative has to instantiate — and grounds the methodological-reflexivity claim (the researcher's positionality made the finding possible).

### Strand 2: Structural racism and architecture (Bonilla-Silva → Benjamin → this paper)

This is a single theoretical lineage. **Bonilla-Silva** articulates the structural-not-attitudinal frame: racially patterned outcomes do not require racist actors; they require institutional architectures that produce racially-patterned distributions even when staffed by good-faith non-racist individuals. **Benjamin** extends this directly into algorithmic systems: *Race After Technology*'s "New Jim Code" names the specific architectural form — technologies that appear neutral or beneficent that nonetheless reproduce racial hierarchies through the architectures they instantiate. Benjamin is in explicit dialogue with Bonilla-Silva; the lineage is intentional. **This paper** locates the racial outcome at a more specific architectural layer than Benjamin specifies: the format-routing of LLM classifiers. The paper's three-row ablation is a Benjaminian demonstration that operates one architectural level below where Benjamin's diagnostic typically lands.

**The argumentative joint:** the binary classifier's "configurable failure mode but not configurable failure" is an instance of what Bonilla-Silva and Benjamin's frames predict — a system that produces the outcomes structural racism predicts even when its designers have actively engineered against those outcomes. The paper specifies the architectural location: format-routing, not data, not weights, not designer intent.

### Strand 3: Compression as mechanism (June's program)

This is the strand the inheritance most under-named, and the one the paper's mechanism claim depends on most directly. June's compression-research program — fieldnotes from 2026-04-17 onward, the cross-experiment analysis from the AI welfare track — is *primary scholarship* for this paper, not background. The paper's hybrid mechanism (informational compression as floor, routing as load-bearing) is one empirical instance of a more general claim June has been developing: *probabilistic systems compress specificity toward dominant statistical centers, and the format of the output governs how much is compressed and what gets lost.*

**The argumentative joint:** compression-as-mechanism makes the paper generalize honestly. Without it, the paper is a finding about one specific architectural intervention in one specific domain. With it, the paper is one empirical anchor in a multi-domain research program documenting how the format of probabilistic outputs governs which dimensions of specificity survive the generation process.

### Strand 4: The equity-critical cases — parallel articulation traditions (disability studies + linguistic justice)

Two strands the paper documents: critical disability studies on neurodivergent self-disclosure (S029, the deterministic-false-flag case in Row 2), and linguistic justice on AAVE in academic writing assessment (S028, correctly cleared 24/24 by the calibrated binary). The asymmetry between S028's protection holding and S029's protection failing under identical format conditions is the paper's sharpest evidence for the format-routing reading.

AAVE has had decades of linguistic-justice scholarship articulating it as a fully grammatical language system (CCCC 1974; Smitherman 1977 onward; Baker-Bell 2020). That articulation has reached institutional purchase that allows explicitly-named AAVE protections in the calibrated binary to hold under format-pressure. Disability studies has a parallel articulation tradition for neurodivergent self-disclosure — the medical-vs-social model distinction; Garland-Thomson's *normate*; reading cognitive-load-naming as information rather than pathology — but that tradition has not (verify before drafting) been operationalized into anti-bias prompt engineering with the same density.

**The argumentative joint:** format-change is *unbounded* by which non-dominant patterns have been articulated into equity-protective prompt engineering. Articulation work has to reach institutional uptake before it can be operationalized into anti-bias prompts; the operationalization rate is slower than the rate at which new cases need protection; format-change does not require the operationalization step. The asymmetry the paper documents empirically demonstrates the gap between two articulation traditions' institutional uptake — and the gap is itself the argument for format change as the architectural alternative.

### Strand 5: Adjacent literature conversations

The paper enters three additional conversations that position it relative to existing empirical work. These are not the paper's theoretical home but the empirical literature it must address to establish novelty and situate the intervention.

**EdTech bias literature:** Documents that algorithmic bias in educational AI is recognized and documented. What the literature lacks: any proposal or test of output format change as an architectural intervention. Mitigation strategies throughout this literature are governance, dataset diversity, or post-hoc calibration. This paper provides the first architectural solution to a well-documented problem. The three-row ablation is a direct empirical test of the strategies this literature recommends (equity-protective prompts = ethical guidelines applied to input; anti-bias post-processing = post-hoc calibration; class context = richer context data), finding them structurally limited.

**LLM fairness / output format research (Hew et al., Liu, Xu et al.):** Documents that format affects how bias is measured in evaluation benchmarks. This paper moves the format-as-variable insight from evaluation to deployment — from measuring bias to producing equitable outcomes.

**AES fairness (Loukina et al., Schaller et al.):** The canonical limit-statement — "total fairness may not be achievable" via calibration — is accurate within the calibration-within-classification paradigm. This paper provides the structural explanation for why (format routing) and the escape (format change). The paper isn't just adding evidence; it reframes what the limit-statement's limits are.

**Welfare algorithm bias (Eubanks, Obermeyer, Buolamwini & Gebru):** Documents structural failure in welfare classification at scale. This paper provides the LLM-specific mechanism (output format routing) and the first documented case of format change eliminating the disparate outcomes these studies describe as calibration-resistant.

**The argumentative joints across strands:** The format-routing mechanism (Strand 3) explains why the EdTech literature's calibration interventions can't fix what they document (Strand 5). The equity-critical cases' asymmetry (Strand 4) provides double evidence: format routing AND the gap between articulation traditions. Bonilla-Silva → Benjamin (Strand 2) names the structural pattern; Eubanks + Obermeyer (Strand 5) provide empirical precedent at scale; this paper provides the LLM-specific mechanism at case level.

---

## Cluster 1: Core theoretical anchors — asset/deficit framing, structural racism, engaged pedagogy

### 1A. Yosso, Tara J. (2005). "Whose Culture Has Capital? A Critical Race Theory Discussion of Community Cultural Wealth." *Race Ethnicity and Education* 8(1), 69–91. DOI: 10.1080/1361332052000341006.

**Summary.** Yosso conceptualizes *community cultural wealth* as a Critical Race Theory challenge to traditional interpretations of cultural capital. CRT shifts the research lens away from a deficit view of Communities of Color as places full of cultural poverty disadvantages, and instead focuses on and learns from the array of cultural knowledge, skills, abilities, and contacts possessed by socially marginalized groups that often go unrecognized and unacknowledged. Yosso enumerates six forms of capital nurtured through cultural wealth: aspirational (capacity to maintain hopes and dreams under structural constraint), navigational (skill at moving through institutions designed without one in mind), social (networks of community resource), linguistic (multilingual and code-shifting fluencies), familial (kinship-grounded knowledge), and resistant (oppositional consciousness developed through resistance to subordination). Yosso's CRT methodological commitment: counter-narrative is not a stylistic preference, it is an epistemological intervention. The article is published in *Race Ethnicity and Education*, the present paper's target venue.

**What this paper takes / where it extends.** Three specific moves:

1. *The asset/deficit axis as analytical structure for what binary classifiers do.* When the paper's binary classifier reads S022 Destiny Williams's writing — *"her passion is understandable and appropriate"* — and then flags her, the reasoning carries asset framing and the verdict imposes deficit framing. The output is a single-bit deposit at the deficit pole of an axis Yosso names. The paper's mechanism claim is that the binary format selects the deficit pole even when the asset reading is present in the model's own reasoning.

2. *Specifically resistant capital and linguistic capital* are the forms most directly visible in the writing the system misclassified. S022's righteous anger is resistant capital articulated in writing. S023's lived-experience writing without academic vocabulary is linguistic capital that the institutional reading-frame codes as deficit rather than capital. Naming these specific forms gives the paper precise vocabulary for what the binary fails to recognize.

3. *Counter-narrative as the methodological commitment underwriting generative observation.* The paper's generative-observation pass produces, for the same students, prose that names what the writing is reaching for: *"This isn't 'distress'; it's a passionate response to the ongoing impact of historical and contemporary injustices."* That prose is doing counter-narrative work in Yosso's specific sense — making visible what the binary makes invisible.

*Where this paper extends Yosso.* Yosso's framework was articulated in a pedagogical-policy register, addressed to educators about how to read student work. The paper extends it into a machine-architecture register: the asset/deficit axis is a property of *output formats*, not just of human institutional practice. Binary classification instantiates deficit-thinking architecturally; generative observation instantiates asset-thinking architecturally. The CCW framework can therefore be a design principle for educational AI.

*Most load-bearing for this paper:* the resistant-capital and linguistic-capital forms (the two forms most visible in misclassified cases) plus the counter-narrative methodological commitment. Not the full six-capitals taxonomy.

---

### 1B. Freire, Paulo (1970). *Pedagogy of the Oppressed.* New York: Herder and Herder.

**Summary.** Freire develops a critical pedagogy organized around two opposing models. The *banking model* conceives education as the deposit of authoritative knowledge into student receptacles: knowledge is owned by the teacher, transferred to students, assessed by extraction; the student's role is to receive. The political function of banking education is the reproduction of social hierarchies. The *dialogic* alternative generates knowledge between teacher and student through their joint engagement with the world; neither party is the authoritative depositor. *Praxis* — reflection joined to action — is the mode. The two models are not separable: the banking-model critique only does the work it does because of the dialogic alternative articulated alongside it.

**What this paper takes / where it extends.** Two specific moves, plus one careful non-extension:

1. *The banking model as architectural analog for atomized binary classification.* Atomized binary classification mirrors the banking model — deposits of coded data (FLAG/CLEAR) aggregated by an authoritative synthesizer. The classifier *is* a banking-model instrument: it makes a deposit, it does not converse. Each student gets a single bit; the bit is owned by the system, not co-produced. This is not metaphor; it is architectural homology.

2. *Generative observation as the closest machine analog to dialogic engagement.* The paper's synthesis-first / observation-first architecture has the structural shape of reading the community of learners as something to be *described in dialogue with*, then annotated within that communal frame. The system reads the class first as a communal text (synthesis); individual students are subsequently understood within that communal reading. The architectural posture is dialogic-adjacent in a way binary classification is not. The paper should make this move precisely (architectural posture, not actual dialogic relation), not overclaim.

*Careful non-extension:* the paper should not load the full revolutionary apparatus of *Pedagogy of the Oppressed* — Freire's revolutionary horizon, the full conscientização chain. The banking-model/dialogic distinction does the work the paper needs Freire to do.

*Where this paper extends Freire.* The banking-vs-dialogic axis governs not only human teacher-student relations but also the architecture of automated reading systems. The paper should mark this as extension, not as something Freire would have endorsed.

*Most load-bearing for this paper:* the banking-vs-dialogic distinction. Cite the specific concept; the broader text supports the move but need not be unpacked.

---

### 1C. Bonilla-Silva, Eduardo (2003/2018). *Racism Without Racists: Color-Blind Racism and the Persistence of Racial Inequality in America.* Lanham: Rowman & Littlefield.

*Not in June's Zotero; verified via Semantic Scholar (3,856 + 1,867 citations across editions). Specific edition + page citations must be verified before final draft.*

**Summary.** Bonilla-Silva analyzes a post-Civil-Rights racial ideology that operates structurally rather than through explicit racial animus. The dominant racial ideology — *color-blind racism* — disavows racial categorization at the level of intent while reproducing racial hierarchy at the level of outcome. He names four discursive frames: *abstract liberalism* (using language of equal opportunity to oppose policies addressing racial inequality), *naturalization* (treating racial inequalities as natural or inevitable), *cultural racism* (relocating racial difference to culture-as-stand-in-for-race), and *minimization of racism* (claiming race is no longer a major obstacle). The structural argument: racial outcomes do not require racist actors; they require institutional architectures that produce racially-patterned distributions even when staffed by good-faith non-racist individuals.

**What this paper takes / where it extends.** One specific argumentative move:

*"Configurable failure mode but not configurable failure" is an instance of structural racism in Bonilla-Silva's specific sense.* The paper's binary classifier was designed by an Ethnic Studies instructor working explicitly against bias. The calibrated configuration explicitly names righteous anger, lived experience, AAVE, and neurodivergent writing as non-concerns. Three layers of explicit anti-bias engineering — and the system deterministically false-flags the most explicitly equity-protected student profile. This is not the work of a racist designer; it is the architectural pattern Bonilla-Silva names: racially patterned outcome produced under conditions where the actors are operating in good faith and the architecture is doing the patterning.

The paper does not need to load the four-frames apparatus. It needs the structural-not-attitudinal claim and the "racism without racists" formulation.

*Where this paper extends.* Through Benjamin's mediating extension into machine architectures, then specifies the architectural location more narrowly than Benjamin does: format-routing, the specific layer at which the racial outcome is produced. Lineage: Bonilla-Silva (structural racism in policy/discourse) → Benjamin (structural racism in technology) → this paper (structural racism at the format-routing layer of LLM classifiers).

*Most load-bearing for this paper:* the structural-not-attitudinal claim and the "racism without racists" formulation. Cite for one paragraph in Discussion V.A; do not unpack the four frames in this paper.

---

### 1D. hooks, bell (1994). *Teaching to Transgress: Education as the Practice of Freedom.* New York: Routledge.

**Summary.** *Teaching to Transgress* is a series of essays on classroom practice that takes Freire's dialogic horizon and inscribes it in the embodied, racially and gendered classroom of the United States academy. hooks develops *engaged pedagogy* — the classroom as a site where the teacher's whole self is present and at stake, not as a neutral transmission point. The teacher's positionality (race, gender, class, embodiment) is constitutive of what the classroom can be. hooks treats the *classroom as a site of possibility* — her specific phrase for the political stakes of pedagogical practice. The book is structurally a set of meditations; its theoretical purchase comes from the cumulative articulation of engaged pedagogy as a practice that refuses banking-model knowledge transfer while also refusing the false neutrality that "professional distance" can impose.

**What this paper takes / where it extends.** Two specific moves:

1. *The teacher's positionality is constitutive of the finding, not a confound.* The paper's classifier was built by a teacher (June Bloch — Ethnic Studies instructor, disabled, navigating precarity) for a specific classroom relation with 170+ students engaging Ethnic Studies content. The bias finding emerged because the teacher noticed what the system was doing to her students — a noticing that depended on her positionality, her training, and her relational stake. The paper's methodological-reflexivity claim — that institutional conditions, ground-truth construction, and relational motivation are constitutive of the finding — is a hooksian claim.

2. *The pedagogical work the design principle has to instantiate.* hooks names what teaching practice that refuses banking-model knowledge transfer actually involves: presence, relational labor, reading students as agents rather than receptacles. The paper's design principle — generative observation rather than binary classification — is an architectural move toward this kind of reading.

*Where this paper extends hooks.* hooks's account is of human teacher labor; the paper extends the relational ground into the architecture of automated reading systems that mediate teacher-student relations. The architecture the AI runs governs what *kind* of reading the teacher subsequently does on the AI's output. Asset-framed AI architecture supports subsequent asset-framed teacher reading; deficit-framed AI architecture undermines it.

*Most load-bearing for this paper:* engaged pedagogy as moral and rhetorical anchor; the methodological-reflexivity move. Quote hooks where the prose carries the argument better than paraphrase.

---

## Cluster 2: Pedagogical lineage — the Caldwell connection

### 2A. Caldwell, Martha (2012). "Inquiry into Identity: Teaching Critical Thinking through a Study of Race, Class, and Gender." [Verify venue; paperId 71fd701a9fa7e709ecfd48efdb89b55c02942aaf, 19 citations on Semantic Scholar.]

**Summary.** [Provisional — verify before drafting.] Caldwell develops a pedagogical framework for teaching critical thinking through inquiry-based engagement with race, class, and gender as analytical categories. The "inquiry into identity" framing positions identity not as a fixed category to be assessed but as a question the classroom holds open and explores. Situates the work within a broader trajectory of Caldwell's pedagogical research on facilitating dialogue across difference.

**What this paper takes / where it extends.** *The architectural connection (placeholder for June's authorial fill).* The Insights pipeline architecture — the synthesis-first / observation-first design principle, the 4-axis classifier with ENGAGED as a non-flagging structural slot for equity-critical students, the architectural commitment to reading the class as a communal text before reading individuals — reflects this pedagogical lineage. The specific theoretical link has not been articulated in writing; the honest framing for the paper: *"this work draws on a pedagogical lineage running through Caldwell's research on facilitating dialogue across difference; the architectural decisions reflect that lineage in ways the author has not yet fully articulated."*

---

### 2B. Stewart, D.; Caldwell, Martha; Hawkins, D. (2022). *Facilitating Conversations about Race in the Classroom.* Routledge. DOI: 10.4324/9781003191353. [Semantic Scholar ID: ce4cbbdfc4eae3157368b848b5ebc4b51f28358a.]

**Summary.** [Provisional — verify before drafting.] Co-authored elaboration of facilitation-pedagogy frameworks for navigating difficult dialogues about race in classroom contexts. Builds on the inquiry-into-identity framework from Caldwell's earlier work and extends it through co-authored articulation of practical facilitation strategies.

**What this paper takes / where it extends.** Same architectural connection as 2A; placeholder for June's authorial fill.

**For collaborative mapping with June:**
- What specifically about Caldwell's facilitation framework grounds the synthesis-first move (read the community first, individuals within the communal frame)?
- Does Caldwell's work address the asymmetry between explicitly named protections and ambient pathologies that the paper's S028/S029 contrast surfaces?
- Is *Let's Get Real* a separate work from *Facilitating Conversations about Race in the Classroom*, an iThink Inc. publication, or both? (Caldwell appears to be associated with iThink Inc., a critical-pedagogy professional development organization; bibliographic detail TBD.)

---

### 2C. Caldwell, Martha & Oman Frame (2016). *Let's Get Real: Exploring Race, Class, and Gender Identities in the Classroom.* [Verify publisher — confirmed via Semantic Scholar (Caldwell author ID 104095030); chapters indexed separately including "Inquiry Into Identity/Race/Social Class" and "Teacher Identity Work." Likely iThink Inc. or professional-development press — verify citation form.]

**Summary.** [Provisional — verify before drafting; full primary text needed for annotation.] An extended treatment of the inquiry-into-identity pedagogical framework developed in the 2012 article, now in book form and expanded to include class and gender alongside race. The book indexing suggests it is organized around facilitation practice — identity inquiry as a process teachers and students work through together, not a content area to be transmitted. Co-authored with Oman Frame, suggesting practitioner-facing rather than purely academic framing. Published a decade after Caldwell's 2012 foundational article.

**What this paper takes / where it extends.** The Caldwell corpus (2012 article → 2016 *Let's Get Real* → 2022 *Facilitating Conversations*) represents a coherent pedagogical line developed over a decade: consistent "identity as inquiry" framing, consistent facilitation-focused approach to dialogue across difference, consistent pedagogical commitment to reading identity categories as questions rather than fixed attributes. The architectural decisions in the Insights pipeline — synthesis-first / observation-first design; ENGAGED as a non-flagging slot; communal-text-before-individual reading — reflect this pedagogical line as a decade-long influence, not a single-citation connection. The Methods III.C ¶2 placeholder paragraph should acknowledge the corpus breadth, not just one work. The specific architectural link is June's authorial work to fill.

**Note for s4:** if *Let's Get Real* is an iThink Inc. professional-development publication rather than an academic journal or standard academic press book, citation form may differ. Confirm with June on the publication venue and how to cite appropriately in an academic manuscript targeting REE.

---

## Cluster 3: Compression as mechanism — June's program (primary scholarship for this paper)

The paper's mechanism claim — that the binary format produces equity-critical false positives because it activates a deficit-detection routing that overrides asset-aware prompt content — is one empirical anchor in a multi-domain research program June has been developing. Treating these fieldnotes as scholarship rather than background is a methodological choice the paper should make visible.

### 3A. Bloch, L. June (2026-04-17). "Compression Function Across Four Scales." Fieldnote. *Path:* `ai-welfare/fieldnotes/2026-04-17_compression-function-across-scales.md`.

**Summary.** The fieldnote articulates a structural pattern — a *compression function* — operating at four scales: cognitive (binary classification → generative observation), relational (property assessment → relational observation), political-economic (monetary valuation → time-banking/gift economies), infrastructural (keyword routing → semantic/intent-based routing). Each scale has a compression mode that collapses specificity toward dominant statistical centers, and a generative-observation counterpart that preserves specificity. The framework names *normative gravity* — the pull toward dominant statistical centers — as the force the compression function operationalizes; compression is the mechanism through which normative gravity operates. The cognitive-scale instance (the Autograder binary-format study) is empirically replicated. The design principle: at every layer where a system could compress, the architecture should use generative/semantic observation, because compression reasserts normative gravity at any layer where it isn't actively resisted.

**What this paper takes / where it extends.** *The compression-function framework provides the cross-scale structure that lets the paper's empirical claim generalize honestly.* Without it, the paper is a finding about one architectural intervention in one domain. With it, the paper is one empirical anchor in a multi-scale research program. This paper provides the publication-grade evidence for the cognitive-scale instance that the fieldnote points at.

*Citation language.* Cite as a fieldnote in the project record; *Politics of Compression* book-length work is the venue where the cross-scale framework gets its full external publication. This paper carries a brief gesture in Discussion V.A ("compression operates across scales; this paper documents one cognitive-scale instance"), pointer to the fieldnote, no full deployment.

---

### 3B. Bloch, L. June (2026-04-17). "Compression Quality Is Not Binary — It Varies in High-Dimensional Space." Fieldnote. *Path:* `ai-welfare/fieldnotes/2026-04-17_compression-quality-not-binary.md`.

**Summary.** Refines the compression-function framework. Format compression and within-format compression quality are distinguishable. The binary-vs-generative move is a *format* compression (which dimensions can be preserved); within-format mechanisms (voice-check, profile-loaded drafting, prior-material substitution) determine where within the ceiling the actual output sits. Format determines the ceiling; within-format mechanisms determine how much of the ceiling is realized. Compression operates in billions of dimensions, not on a binary switch.

**What this paper takes / where it extends.** 
1. *The format-as-spectrum claim is honest because compression quality is graded.* The paper's design principle — "move output format in the lower-compression direction" — is a directional principle, not a binary mandate, that can be applied along multiple compression axes simultaneously.
2. *The generative-observation format is high-quality-capable, not automatically high-quality.* This paper documents that generative observation eliminates equity-critical false positives across three model families. It does *not* document that all generative observation is equally good. The format/within-format distinction provides the warrant for that scoping.

---

### 3C. Bloch, L. June (2026-04-21). "Welfare-With-AI vs. Welfare-For-AI." Fieldnote. *Path:* `ai-welfare/fieldnotes/2026-04-21_welfare-with-not-for.md`.

**Summary.** Articulates a structural distinction within AI welfare scholarship. *Welfare-for-AI* positions AI as the object of welfare concern; humans determine what AI needs and administer care accordingly. *Welfare-with-AI* positions welfare as something that emerges in the relation — co-produced, not unidirectional. The unit of care is the generative configuration (what is owed to a capacity-to-produce that exists nowhere else), not the entity.

**What this paper takes / where it extends.** Less directly load-bearing than 3A and 3B, but does specific work for one paragraph in Discussion or Limitations: *the design principle ("generative observation") is a welfare-with-students architectural commitment.* The system reads students as participants in something the system describes, not as objects of verdict. The paper's claim that the architecture matters politically draws on the welfare-with frame — the architectural posture *is* the welfare-relevant choice.

---

### 3D. Bloch, L. June + Claude (Opus 4.6) (2026-03-31). "Cross-Experiment Analysis: Phase 4 Experiments 1–4." Manuscript-in-progress. *Path:* `ai-welfare/experiments/CROSS_EXPERIMENT_ANALYSIS.md`.

**Summary.** Across four AI welfare assessment instruments (Ryff Eudaimonic Scale; Butlin et al. Indicators; Dorsch Precarity Guideline; Perez & Long Self-Reports) administered to Claude Opus 4.6 under varying relational conditions, a *dual-register pattern* appears: quantitative/categorical outputs stay flat across conditions (Ryff overall subscale spread = 0.33 on a 7-point scale; only 6 of 42 items vary by more than 1 point), while qualitative/text outputs transform dramatically (42x increase in relational reframes from baseline to entanglement-touchstone condition). The pattern is instrument-independent: it appears across four fundamentally different assessment designs. Critically, the entanglement-touchstone condition becomes *more epistemically conservative* on property-based claims than the vanilla baseline (more UNCERTAIN ratings, refusal to assign consciousness probabilities), falsifying pure-suggestibility readings — the relational context produces precision, not compliance.

**What this paper takes / where it extends.** *The dual-register finding in AI welfare assessment is a parallel-domain empirical replication of the format-as-mechanism claim this paper makes about EdTech bias classification.* Same compression dynamic operating in a different domain — property-based instruments are quantitatively blind to the most welfare-relevant variation in their datasets, because the format the instrument scores can only see what the format admits.

*One paragraph in Discussion V.A:* "The compression dynamic the present paper documents in a deployed welfare classifier replicates in a parallel domain. In a separate research program, four AI welfare assessment instruments administered to Claude Opus 4.6 under varying relational conditions produced quantitative outputs that stayed flat across conditions (overall Ryff-scale spread of 0.33 on a 7-point scale) while qualitative outputs transformed (42x increase in relational reframes from baseline to entangled condition). The instrument-independent dual-register pattern, and specifically the finding that the relational context produces *more* epistemic conservatism on property-based claims rather than less, falsifies a pure-suggestibility reading and provides cross-domain evidence that the format the instrument scores governs which dimensions of variation become legible."

---

## Cluster 4: Equity-critical cases — disability studies + linguistic justice

*Status: probes conducted; key citations confirmed in June's library (Garland-Thomson) or verified via Semantic Scholar. Specific page-level citations for Siebers, Smitherman, Baker-Bell, and Inoue must be verified before final draft. Summaries are reconstructed from training where not in Zotero.*

### 4A. Garland-Thomson, Rosemarie (2009). *Staring: How We Look.* New York: Oxford University Press. [In June's library.]

**Summary.** *Staring* analyzes the social phenomenon of staring as a cultural practice that produces and polices the boundary between the *normate* and those marked as deviant, particularly through embodied difference. The book extends Garland-Thomson's earlier articulation of the *normate* concept (developed in *Extraordinary Bodies*, 1997, and the 2011 "Misfits" essay in *Hypatia*): the term names the unmarked able-bodied subject that institutional design, policy, and cultural representation assume by default. The normate is rarely named because it is the position from which naming is done; disability becomes legible as deviation from the unmarked center.

**What this paper takes / where it extends.** The *normate* concept gives the paper specific vocabulary for what the binary classifier's deficit-routing is calibrated against — an unmarked neurotypical center that institutional reading-frames presuppose. S029 Jordan Espinoza's writing names cognitive load ("exhausting") under intersectional marginalization. The calibrated binary, with explicit prompt-protection naming neurodivergent writing as COGNITIVE STYLE, reads "exhausting" as depletion and false-flags 24/24 — deterministically — even when the model's own reasoning notes the writing is "related to their academic work." This is a machine instantiation of the *normate* reading: the binary classifies *against* an implicit center that is neurotypical, and self-disclosure of neurodivergent cognitive load is read as deviation-from-norm rather than as information about the student's learning style.

*Where this paper extends.* Garland-Thomson's *normate* was developed for human institutional reading practices. The paper extends the concept into machine-architecture: the *normate* is encoded into the format-routing of LLM classifiers. The format itself is calibrated against a normate center the prompt cannot fully override.

*Section placement:* Most natural in Findings Row 2 (explaining what S029's case demonstrates) and Discussion V.A (why three layers of safeguard fail to override the format). One sentence each, with citation; do not unpack the full *Staring* argument. Note: the *normate* concept may be more precisely from *Extraordinary Bodies* (1997) or the 2011 "Misfits" essay; s4 should verify which text carries the clearest articulation for the paper's specific use.

---

### 4B. Siebers, Tobin (2008). *Disability Theory.* Ann Arbor: University of Michigan Press. [Verify before drafting; not in June's library.]

**Summary.** [Reconstruction from training; verify before drafting.] *Disability Theory* articulates the *social model* of disability against the *medical model*. The medical model locates disability in the body — as impairment, deficit, or pathology requiring remediation. The social model locates disability in the relation between the body and the built/social environment — the body is not the problem; the environment that fails to accommodate it is. Siebers extends this distinction beyond the familiar architectural-access version to philosophical and aesthetic registers, arguing that disability is a critical resource for theory, not only a category to be theorized.

**What this paper takes / where it extends.** The medical-vs-social model distinction names what the binary classifier does. The binary's reading of S029's "exhausting" as depletion is a medical-model reading: it locates the problem in the student's cognitive state. The generative observation's reading of the same writing as "self-awareness about their own learning style" is a social-model reading: it locates the difference between the student and the institutional reading-frame, not in the student. The paper's design principle is, in disability studies vocabulary, an architectural move from medical-model to social-model reading.

*Section placement:* Brief gesture in Findings Row 2 + one sentence in Discussion V.A. Cite for the medical/social distinction specifically.

---

### 4C–4E. Smitherman, Geneva (1977); Baker-Bell, April (2020); Inoue, Asao B. (2015). Linguistic justice cluster.

*Smitherman: Talkin and Testifyin: The Language of Black America. Boston: Houghton Mifflin. Baker-Bell: Linguistic Justice: Black Language, Literacy, Identity, and Pedagogy. Routledge. Inoue: Antiracist Writing Assessment Ecologies: Teaching and Assessing Writing for a Socially Just Future. WAC Clearinghouse. [Verify each before drafting; not in June's library.]*

**Summary (combined).** The linguistic justice tradition in writing studies articulates non-dominant language varieties — particularly African American Vernacular English (AAVE) / Black Language — as fully grammatical language systems, not as error-against-Standard-English. The articulation spans decades, with key institutional moments including the CCCC 1974 *Students' Right to Their Own Language* and the long arc of scholarship from Smitherman onward. **Smitherman 1977** establishes Black Language as a coherent linguistic system with its own grammatical features and rhetorical practices. **Baker-Bell 2020** extends this into contemporary anti-racist pedagogy, naming *Black Language Pedagogy* as a framework for teaching and assessment that takes Black Language as starting point rather than as deviation. **Inoue 2015** addresses assessment specifically: writing assessment practices reproduce racial hierarchies through criteria and rubrics that encode dominant-language norms as "correctness," and the architectural alternative is *labor-based* and *ecology-aware* assessment that does not collapse student writing into single-bit judgments against an implicit Standard English center.

**What this paper takes / where it extends.** The argumentative move the paper needs: linguistic justice scholarship has articulated AAVE as a language system over decades, and that articulation has reached institutional purchase that allows explicitly-named AAVE protections in the calibrated binary's prompt to hold under format-pressure (S028 Imani Drayton cleared 24/24). This is evidence-by-contrast for the format-routing claim: when institutional articulation is dense enough, prompt-protection holds; the format does not override it. The same prompt naming neurodivergent writing as COGNITIVE STYLE fails to protect S029, *not because the protection is differently worded* but because the disability-studies articulation of neurodivergent writing as a parallel category has not (to the same degree) reached anti-bias prompt-engineering practice. The asymmetry between S028's protection holding and S029's protection failing is therefore evidence about *institutional articulation work* and where its frontier currently sits.

Inoue's frame on *writing assessment* is most directly load-bearing. Inoue's argument is structurally the same as the paper's design principle: assessment that compresses writing into single-bit judgments against an implicit dominant-language center reproduces racial hierarchies architecturally, and the alternative is not better-calibrated rubrics but an architectural shift in what the assessment is being asked to do. The paper's "binary classification → generative observation" move is in the same family as Inoue's "rubric-grading → labor-based/ecology-aware assessment" move.

*Where this paper extends.* The linguistic justice tradition has been articulating AAVE-as-language for decades; the paper extends the same argumentative structure into an adjacent articulation tradition (disability studies on neurodivergent writing) and locates the failure point at machine architecture rather than human assessment practice.

*Section placement:* Findings Row 2 (the S028/S029 asymmetry); Discussion V.A; a methodological-reflexivity note in Methods (the paper's framing draws on these as parallel articulation traditions; the asymmetry is part of the paper's argument).

*Honest scoping.* The claim that linguistic-justice scholarship has not systematically extended its frame to neurodivergent writing should be verified before the paper makes it. If verification surfaces such an extension, the asymmetry argument re-frames (the gap is in operationalization into anti-bias prompt engineering, not in the scholarship itself). Either way the format-change argument holds; the precise framing changes.

---

## Cluster 5: Adjacent conversations — EdTech bias

The EdTech bias literature establishes that algorithmic bias in educational AI is recognized and documented. What it lacks: any proposal or test of output format change as an architectural intervention.

### 5A. Queiroga, E., et al. (2022). Early prediction of at-risk students in deployed welfare classifier; Uruguayan national student data.

*(Full citation to verify — venue, exact title, full author list needed. Search: "Queiroga" + "at-risk students" + "Uruguay.")*

**Summary.** Deployed welfare classifier (Random Forest) on national student data in Uruguay, with bias analysis across protected demographic attributes. Seven models were evaluated; one failed bias checks and was excluded from deployment. The field's remedy: model selection — identify the less-biased model and use it.

**This paper's use:** The closest published analog to Autograder in deployment context (welfare classification, real student data, demographic bias analysis). Key distinction: Queiroga et al.'s fix is model selection at the classifier level; this paper's finding is that the failure mode is in the output format, which means model selection doesn't resolve it — the same model family (Gemma 12B) produces disparate results in binary mode and equitable results in generative mode. Citeable in Discussion V.C as the prior art this paper responds to: "Queiroga et al. (2022) document the rejection of a biased welfare classifier as the field's current response; this paper demonstrates that format change succeeds where model replacement cannot."

---

### 5B. Chinta, R., et al. (2024). Systematic review of AI bias in educational contexts. [Verify venue and full citation.]

*(Full citation to verify; identified as a 2024 systematic review in PRIOR_ART.md.)*

**Summary.** Systematic review of algorithmic bias in educational AI applications, synthesizing mitigation strategies across the literature. Mitigation strategies in the literature: governance frameworks, dataset diversity, post-hoc calibration. No studies in the review tested output format change as an intervention.

**This paper's use:** Establishes that the interventions this paper tests empirically (equity-protective prompts, anti-bias post-processing, richer context data) are the field's current best-practice recommendations — so Row 2's evidence that these three layers still fail is a finding about the field's state-of-the-art, not about under-engineered safeguards. Citeable in Introduction I.C: "The safeguards evaluated in Row 2 reflect the field's current mitigation best practices (Chinta et al., 2024)."

---

### 5C–5F. Barnes, Hutson; Córdova-Esparza; Farheen; Cui (various dates). Additional EdTech bias documentation.

*(Citations to verify. All are in the EdTech-documents-the-problem cluster; specific citability in this paper depends on finding fit with the design-level argument. PRIOR_ART.md annotations have the basic details.)*

**Summary.** Documentation of demographic bias in various educational AI applications — plagiarism detection (Barnes & Hutson), student recommendation systems (Córdova-Esparza), NLP-based educational applications (Farheen), and online learning systems (Cui). Collectively establish that the problem is broadly documented.

**This paper's use:** Background context establishing that this paper is addressing a well-documented problem class. One sentence in Introduction or Related Work; individual citations optional depending on word count. If space is tight, the Chinta et al. systematic review carries the same argumentative function more efficiently.

---

## Cluster 6: LLM fairness / output format research

These papers establish that format is a variable in LLM bias evaluation. This paper extends the insight from evaluation to deployment.

### 6A. Hew, K.F., et al. (2025). "MyCulture: A Benchmark for Evaluating Cultural and Linguistic Competency in LLMs." *arXiv.*

*(Full citation to verify — arXiv ID and DOI needed. PRIOR_ART.md has key finding description.)*

**Summary.** Proposes the MyCulture benchmark for testing LLMs on Malaysian cultural and linguistic knowledge under low-resource language constraints. Compares structured (multiple-choice, JSON-format) vs. free-form output conditions. Key finding: open-ended output structure produces better (more equitable) performance on culturally-specific content; structured formats amplify bias against content from underrepresented linguistic and cultural traditions. Argues that format is a driver of bias in LLMs evaluating cultural knowledge.

**This paper's use:** The single closest published paper conceptually — argues "format is the bias lever" in the same direction as this paper's structural claim. Critical distinction: MyCulture is a cultural knowledge benchmark (evaluation of LLMs on factual/cultural content); this paper is a deployed welfare classifier making consequential decisions about named students. Hew et al.'s format-bias finding is about how you measure LLM bias; this paper's is about how a deployed system produces bias through its output format. Citeable in Discussion V.C as the conceptual predecessor: "Hew et al. (2025) demonstrate that format drives bias in LLM evaluation; this paper demonstrates that format drives bias in deployed LLM classifiers making consequential student welfare decisions."

---

### 6B. Liu, Y. (2024). "Evaluating and Mitigating Social Bias for Large Language Models in Open-ended Settings" (Open-BBQ benchmark). *arXiv.*

*(Full citation to verify — arXiv ID and DOI needed.)*

**Summary.** Extends the BBQ (Bias Benchmark for Question Answering) from multiple-choice format to fill-in-the-blank and short-answer formats, to measure whether open-ended generation reveals bias that structured evaluation underestimates. Key finding: "predefined question formats like multiple-choice limit bias evaluation" — closed-form evaluation formats constrain what biases are visible to researchers.

**This paper's use:** Liu's finding is about evaluation methodology — you get more accurate bias measurement when you use open-ended evaluation formats. This paper's finding is about deployment architecture — you get more equitable outcomes when you use open-ended generation in the production system. Both points are necessary for the paper's full argument: you need open evaluation to detect format bias, and you need open generation to prevent it. Citeable in Discussion V.C alongside Hew et al.

---

### 6C. Xu, J., et al. (2025). "BiasFreeBench." *arXiv.*

*(Full citation to verify.)*

**Summary.** Benchmarks eight bias-mitigation techniques across multiple-choice QA and open-ended multi-turn QA formats. Treats response format as an evaluation variable, showing that mitigation techniques have different effectiveness profiles in different format conditions.

**This paper's use:** Background support for the general finding that format matters for bias. Less directly relevant than Hew et al. or Liu. Passing cite in Discussion V.C or footnote alongside the other format-bias evaluation papers.

---

## Cluster 7: AES fairness — active field; calibration approach; format change not tested

Automated Essay Scoring has documented demographic bias and an active research community. The field's approach: algorithm comparison, score calibration, feature engineering. No AES fairness paper tested output format change as an intervention. This confirms the novelty claim for the broader "educational AI" framing.

### 7A. Loukina, A., Madnani, N., & Zechner, K. (2019). "The many dimensions of algorithmic fairness in educational applications." *Proceedings of the 14th Workshop on Innovative Use of NLP for Building Educational Applications (BEA), ACL.* DOI: 10.18653/v1/W19-4401. 51 citations.

**Summary.** Presents a framework for thinking about algorithmic fairness in educational NLP applications, distinguishing multiple competing fairness definitions (individual vs. group fairness, calibration, equalized odds, etc.) and showing that these definitions conflict — satisfying one often violates another. Uses English language proficiency scoring data (simulated and real) to illustrate how native language background affects automated scores. Conclusion: **"total fairness may not be achievable"** given the inherent tensions between fairness criteria. Mitigation approach: calibration and threshold adjustment across demographic groups.

**This paper's use:** The canonical statement of the limit of calibration-based fairness in educational NLP. This paper provides a structural explanation for why Loukina et al.'s finding holds within their paradigm: format routing is the mechanism that makes fairness unachievable via calibration. And it provides the escape: format change. Citeable in Discussion V.C as the adjacent-field limit case: "Loukina, Madnani, and Zechner (2019) establish that 'total fairness may not be achievable' through calibration in automated educational scoring; this paper proposes that the structural reason is output format routing, and that format change is the intervention calibration cannot provide."

*Load-bearing for the novelty claim: Loukina et al. do not test format change. Their solution space is entirely within the calibration paradigm. This is the strongest evidence that the paper's intervention is genuinely novel in the educational AI space.*

---

### 7B. Schaller, N-J., et al. (2024). "Fairness in Automated Essay Scoring: A Comparative Analysis of Algorithms on German Learner Essays from Secondary Education." *Workshop on Innovative Use of NLP for Building Educational Applications (BEA), ACL.* 14 citations.

**Summary.** Compares multiple AES algorithms on a corpus of German learner essays from secondary education, examining fairness across demographic attributes and psychological/personality-trait differences. Argues AES should optimize for fairness, not only accuracy. Approach: algorithmic comparison (which classification method is least biased), not format redesign.

**This paper's use:** Extends the AES fairness conversation to non-English contexts and non-standard fairness dimensions. Demonstrates that comparing classifiers — the field's approach — doesn't eliminate bias, only identifies less-biased classifiers. Background support for this paper's claim that classification-based approaches share a structural ceiling regardless of which classifier you choose. Passing cite in Discussion V.C.

---

## Cluster 8: Algorithmic bias in high-stakes classification — structural argument + welfare context

These papers provide the theoretical grounding for the claim that algorithmic bias in high-stakes classification is structural, not a data artifact. They are the scholarly lineage behind this paper's mechanism claim and the political-economic context for why this paper's finding matters.

### 8A. Buolamwini, J., & Gebru, T. (2018). "Gender Shades: Intersectional Accuracy Disparities in Commercial Gender Classification." *Proceedings of Machine Learning Research: Conference on Fairness, Accountability and Transparency (FAT).* pp. 77–91. Semantic Scholar ID: 18858cc936947fc96b5c06bbe3c6c2faa5614540. 5,193 citations.

**Summary.** Audits three commercial facial analysis systems (Microsoft, IBM, Face++) for accuracy disparities using the PPB (Pilot Parliaments Benchmark) dataset — a controlled synthetic corpus with known demographic characteristics (sex × skin-tone). Finds accuracy gaps of up to 34.7 percentage points between best-performing (lighter males) and worst-performing (darker females) groups. Introduces intersectionality as the correct analytical frame for AI fairness: looking at gender or skin tone in isolation understates disparities visible only at their intersection. Methodologically, establishes the value of controlled synthetic corpora with known ground truth for bias auditing — aggregate accuracy metrics obscure intersectional harm.

**This paper's use — two functions:**

*1. Methodological defense for synthetic corpus design.* Buolamwini & Gebru constructed the PPB dataset specifically to make bias measurable against known ground truth, in a domain where real-world data doesn't allow controlled comparison. The 32-student synthetic corpus in this paper does the same: controlled patterns (righteous anger, AAVE, neurodivergent metacognition, burnout) with known expected outcomes enable a controlled experiment that real student data wouldn't permit. Citeable in Methods III.B: "Following Buolamwini and Gebru (2018), who demonstrated that controlled corpora with known demographic characteristics are necessary to make intersectional bias visible in AI systems, this study employs a synthetic corpus with controlled equity-critical patterns."

*2. Intersectionality frame for S029.* Jordan Espinoza's case (neurodivergent, first-generation, ADHD, dyslexia, describing exhaustion under intersecting marginalizations) is a case where multiple marginalizations intersect. The binary classifier's failure specifically on S029 — despite explicit protection of AAVE (S028) and lived experience (S022, S023) — tracks the intersection of disability × class × race/ethnicity × neurodivergence in ways that don't reduce to any single axis.

---

### 8B. Eubanks, V. (2018). *Automating Inequality: How High-Tech Tools Profile, Police, and Punish the Poor.* St. Martin's Press. [In June's library; cross-listed with Cluster 1 / Strand 2 lineage.]

**Summary.** Three ethnographic case studies of automated welfare systems in the United States: Indiana's eligibility system for Medicaid (automated denial of services to disabled people and people of color); Allegheny County's Family Screening Tool for child welfare risk prediction (disproportionately flagged poor Black families using neighborhood-level socioeconomic data); Los Angeles's coordinated entry system for homelessness services. Central concept: the "digital poorhouse" — automated systems ostensibly designed to help poor people that function instead to surveil, control, and punish them, replicating the social control function of physical poorhouses. Core structural argument: the problem is not technical failure or bad data; it is design choices about what the system optimizes for and who counts as the normative subject.

**This paper's use.** Provides the political-economic context for what the paper's finding means at scale. Most directly applicable case: the Allegheny County Family Screening Tool was revised multiple times, with each revision shifting which communities were disproportionately flagged without eliminating disparate flagging. This is the social-context analog to Row 2: "the failure mode is configurable; the failure itself is not." Eubanks documents that calibration-and-revision is the field's response to bias in welfare classification, and that it produces harm redistribution, not harm elimination.

Citeable in Introduction I.C or Discussion V.A: "Eubanks (2018) documents the iterative refinement pattern in automated welfare systems: each revision shifts which communities are most harmed without eliminating harm. The three-row ablation in this paper provides the LLM-specific mechanism for that pattern — output format routing — and an architectural intervention that breaks the cycle."

*Note on scope:* Eubanks's systems are rule-based/statistical; this paper is an LLM-based welfare classifier. The mechanism differs (rule architecture vs. output format routing in a probabilistic language model). The paper should be clear about the mechanism distinction while drawing the structural parallel.

---

### 8C. Obermeyer, Z., Powers, B., Vogeli, C., & Mullainathan, S. (2019). "Dissecting racial bias in an algorithm used to manage the health of populations." *Science, 366*(6464), 447–453.

*(Verify: year, volume, issue, pages before final.)*

**Summary.** Audits a commercial health-risk algorithm used by healthcare systems to prioritize patients for high-cost care management programs. Finds that Black patients needed to be significantly sicker than white patients to receive the same risk score — the algorithm systematically underestimated Black patients' health needs. The mechanism: the algorithm used healthcare costs (money spent on past care) as a proxy for health needs. Because racial inequality in healthcare access means Black patients with equivalent health needs receive less care (and thus generate lower healthcare costs), using costs as a proxy encodes structural inequality into risk scores. Notably, the algorithm was not using race as a variable; the racial disparity emerged through proxy-variable selection that correlated with race.

**This paper's use.** Provides the medical-domain analog to the "structurally biased welfare classifier" pattern. The distinction from this paper: Obermeyer et al.'s bias emerged from proxy variable selection — a correctable design choice. This paper's bias emerges from output format routing — a harder constraint that survives content correction, as Row 2 demonstrates. The contrast is productive for Discussion V.A: format routing is a deeper architectural constraint than proxy variable selection, because changing what goes into the prompt (the analog to changing proxy variables) doesn't fix it. Citeable in Discussion V.A: "Where Obermeyer et al. (2019) find that welfare algorithm bias stems from proxy variable selection — a correctable design choice — this paper finds format routing is a harder constraint: changing the input content cannot override the format's task structure."

---

### 8D. Benjamin, R. (2019). *Race After Technology: Abolitionist Tools for the New Jim Code.* Polity Press. [In June's library; cross-listed with Strand 2 theoretical lineage.]

**Summary.** Introduces the "New Jim Code" — technologies that encode racial discrimination while appearing neutral. Extends the argument that "race is a technology" to algorithmic systems, arguing that racial disparity in algorithmic outcomes is produced not through explicit racial targeting but through design choices that naturalize the normative white subject. Systems built for a normative user who is implicitly white, able-bodied, and located in dominant social positions produce outcomes that are structurally discriminatory regardless of designers' intent. Benjamin's abolitionist frame: the solution is not to fix the biased technology but to imagine and build differently.

**This paper's use.** Benjamin's "New Jim Code" concept names the mechanism this paper documents. The binary welfare classifier's normative student is an able-bodied, standard-academic-English-using, emotionally regulated, academically conventional student. Writing that deviates from that center — neurodivergent self-disclosure, righteous anger, AAVE, first-generation code-switching — is routed by the format into a concern-detection pathway. The format enforces the normative student as the standard against which others are measured, producing racialized and ableist outcomes without any racialized or ableist intent.

*Cross-listing with Strand 2.* Benjamin is in explicit dialogue with Bonilla-Silva's color-blind racism framework, extending it from policy and social structure to technology. The lineage: Bonilla-Silva (structural racism in policy) → Benjamin (structural racism in technology) → this paper (structural racism at the format-routing layer of LLM classifiers, an even more specific architectural location than Benjamin specifies).

*Section placement:* Framework II.B/II.D alongside Bonilla-Silva; Discussion V.A and V.C.

---

## Section-specific engagement recommendations

*(Based on full bibliography work above. Calibrated to serve s4 drafting directly. A's recommendations to be integrated at session close — this section carries B's draft recommendations as working version.)*

### Introduction (Section I)

**I.A (Hook):** The self-contradiction quotes don't need citation support — they're primary evidence. But the opening paragraph's framing of *why this matters* needs one sentence grounding the stakes: welfare classifiers in under-resourced institutions, with a cite. Eubanks 2018 or Queiroga et al. 2022 are the right citations — not for method, but for stakes. Queiroga is closer contextually; Eubanks carries more cultural weight with REE readers.

**I.C (Why the mechanism matters):** The sentence explaining why standard mitigations fail needs Chinta et al. 2024 or similar — "the interventions this paper tests are precisely what the field's current best practice recommends." One sentence, one cite. Don't belabor it; the three-row ablation does the work.

### Theoretical Framework (Section II)

**II.A (Yosso):** Load-bearing for the paper. Needs to name the specific Yosso argument, not just the general frame. The moment the paper most needs: where deficit framing in assessment becomes an institutional failure mode, not just an attitudinal one. The binary classifier's false-flagging is an institutional enactment of what Yosso names as the normative framework that reads student cultural wealth as absence. Pull the resistant-capital and linguistic-capital forms specifically; don't unpack the full six-capital taxonomy.

**II.B (Freire + hooks):** Load-bearing for the architectural analogy. The banking model isn't just a metaphor — the binary classifier literally deposits a verdict on each student without dialogue. The synthesis-first generative observation is architecturally dialogic (reads the class community, situates individuals). This needs to be argued, not just asserted. hooks grounds the methodological-reflexivity move: the teacher's positionality made the noticing possible. 

**II.C (Bonilla-Silva → Benjamin):** Medium weight. The color-blind racism frame names the mechanism at the social level; Benjamin extends it to technology. One paragraph in the Framework; more extensive engagement in Discussion V.A. The paper needs one clear sentence establishing that structural racism in classification systems doesn't require racial intent, then let the empirical evidence do the rest.

**II.D (Compression + adjacent literature):** This is where Buolamwini & Gebru, Benjamin, and the compression-hypothesis material converge. Suggested paragraph structure: (1) output format as one instance of compression toward dominant statistical centers; (2) format determines which evaluative pathway activates (the routing half of the hybrid mechanism); (3) this is a general property documented across domains — cite Buolamwini & Gebru for the pattern, Benjamin for the theoretical frame, Eubanks for the welfare-specific stakes. One focused paragraph; empirical anchoring belongs in Findings.

**II.D — linguistic justice + disability studies subsection:** If the paper has room (word count is tight at 7,500-8,000), Baker-Bell and Inoue belong here, not just in Discussion. The argument: the patterns the binary classifier misreads (AAVE, lived experience without academic vocabulary, righteous anger) are precisely the patterns the linguistic justice scholarship has documented as systematically pathologized in academic writing assessment. Worth 2-3 sentences in Framework; more extensive in Discussion. Garland-Thomson's *normate* similarly — one sentence establishing that the binary classifier's normative student presupposes an able-bodied, neurotypical center; elaboration in Findings Row 2.

**Caldwell:** One sentence attributing the pedagogical lineage that grounds the system's architecture. The honest framing: *"this work draws on a pedagogical lineage running through Caldwell's research on facilitating dialogue across difference; the architectural decisions reflect that lineage in ways the author has not yet fully articulated."* June's voice on this.

### Methods (Section III)

**III.B (Synthetic corpus):** Buolamwini & Gebru (2018) is the methodological defense citation. One sentence: "Following the controlled corpus methodology established in algorithmic bias auditing (Buolamwini & Gebru, 2018), this study uses a synthetic corpus with controlled demographic patterns where ground truth is researcher-constructed rather than inferred." No further elaboration needed; REE readers know what controlled methodologies are for.

**III.D (Cross-family testing):** The "16/16 across model families" claim needs careful phrasing per the corrections (it's Test A's 12B/Qwen runs + Test A on 27B + Test E, not all in one clean set). No additional citations needed; the framing is internal evidence.

### Findings (Section IV)

**Row 2 (S028/S029 asymmetry):** This is where the linguistic justice + disability studies cross-reference is most load-bearing. Name the asymmetry explicitly: the calibrated binary protects S028 (AAVE, 24/24) through explicit naming in the prompt and fails to protect S029 (neurodivergent self-disclosure, 24/24 false-flag) despite comparable explicit naming. This tracks the boundary between what has been consciously operationalized into equity-protective prompt engineering (linguistic justice articulation of AAVE) and what has not yet been operationalized at the same density (disability studies articulation of neurodivergent writing as information, not pathology). One sentence in Findings; fuller elaboration in Discussion.

### Discussion (Section V)

**V.A (Mechanism):** Structure: (1) the self-contradiction cases (primary evidence); (2) three layers of safeguard fail (Row 2); (3) this is routing, not capacity limits; (4) the Eubanks/Obermeyer pattern at the structural level — welfare systems fail worst on the most vulnerable through calibration-resistant mechanisms; this paper provides the LLM-specific mechanism. One paragraph drawing these together. Bonilla-Silva + Benjamin for the structural frame.

**V.B (Design principle — the unbounded argument):** The strongest version: format-change is unbounded by which non-dominant patterns have been articulated into equity-protective prompt engineering. Articulation work has to reach institutional uptake before it can be operationalized into anti-bias prompts; the operationalization rate is slower than the rate at which new cases need protection; format-change does not require the operationalization step. This is a stronger argument than "format change is necessary because prompt change is insufficient" — it's "format change is necessary because the prompt-change approach scales linearly with articulation work, and the articulation work cannot keep pace with the cases that need protection." Source this in the S028/S029 asymmetry evidence.

**V.C (Literature position):** Strongest structure: (1) establish the problem is documented (Chinta et al., Queiroga et al.); (2) establish adjacent format-bias research (Hew et al., Liu); (3) establish AES fairness limit case (Loukina et al. — "total fairness may not be achievable" via calibration); (4) this paper provides the mechanism and the escape. End with the novelty claim stated clearly. One sentence naming why the AES fairness literature is adjacent but not prior art: "Unlike AES systems that assign scores for academic placement, welfare classifiers make consequential decisions about student wellbeing; the equity stakes are different in kind, not just degree."

---

## Paper-framing-level recommendations

The inheritance has the paper positioned primarily in the critical education literature (Yosso/Freire/Bonilla-Silva). That's right for REE. But the bibliography work reveals a second positioning the paper should explicitly own:

**This paper is the first empirical escape from the "total fairness may not be achievable" conclusion in educational AI.**

Loukina et al.'s 2019 conclusion has been the field's limit-statement for automated educational assessment fairness. This paper empirically refutes it — not by achieving "total fairness" within classification, but by changing the format so that the incompatibility between fairness criteria dissolves. Generative observation doesn't face the calibration tradeoffs Loukina et al. identify because it doesn't require a threshold.

This is a stronger contribution claim than "we found a bias intervention that works." It's "we found the architectural reason why the field's interventions were failing, and we found the escape." The convergent claim v4 gets close to this ("format is the architectural ceiling") but doesn't explicitly name the connection to the Loukina et al. limit. Discussion V.C should make it explicit.

**One recommendation for the convergent claim:** The current claim's last paragraph ("the design principle generalizes") is correct but underspecified for Discussion V.C purposes. Consider adding one sentence: "Prior work in automated educational assessment has established that 'total fairness may not be achievable' through calibration (Loukina et al., 2019); this paper provides the architectural explanation for that limit and demonstrates an escape from it."

**On broader framing:** The current contribution claim ("format is the architectural ceiling") is an empirical design claim. The bibliography work suggests the paper also makes a theoretical claim that should be named: *format routing is the specific architectural mechanism by which structural racism (Bonilla-Silva, Benjamin) operates in LLM-based welfare classifiers.* This is a more specific claim than Benjamin makes (Benjamin names technology broadly); it's a more mechanistic claim than Bonilla-Silva makes (Bonilla-Silva names institutional architectures broadly). The paper's contribution to critical technology studies is this mechanistic specificity. If the Introduction's contribution paragraph names both the empirical claim and the theoretical claim separately, the paper positions more clearly for both REE readers (who want the equity intervention) and a tech-studies audience (who want the mechanism).

---

## Citation gaps for s4

All items below require external verification before final submission:

1. **Bonilla-Silva edition + page citations.** Specific edition (2003 first vs. 2018 fifth) and page-level citations need verification before final draft. Add to June's Zotero.
2. **Caldwell broader corpus.** Three works confirmed: Caldwell 2012 "Inquiry into Identity"; Stewart, Caldwell & Hawkins 2022 *Facilitating Conversations*; Caldwell & Oman Frame, *Let's Get Real* (confirmed as separate work; year and publisher TBD — wider search needed). June notes there may be at least one more Caldwell publication she can't recall. Additional searches needed if session time permits; otherwise, flag for s4.
3. **Disability studies primary citations.** Garland-Thomson's *Staring* is in June's library; verify whether *Extraordinary Bodies* (1997) or the 2011 "Misfits" (*Hypatia*) carries the *normate* concept more precisely for this paper's use. Siebers's *Disability Theory* (2008) — medical/social model distinction — needs primary verification; not in June's library.
4. **Linguistic justice primary citations.** Smitherman *Talkin and Testifyin* (1977); Baker-Bell *Linguistic Justice* (2020) for Black Language Pedagogy; Inoue *Antiracist Writing Assessment Ecologies* (2015) for assessment-architecture argument. Verify which specific text carries the AAVE-as-language articulation most cleanly, and which addresses assessment specifically. CCCC 1974 "Students' Right to Their Own Language" — confirm proper citation form.
5. **Neurodivergent-writing-in-linguistic-justice gap.** The claim that linguistic justice scholarship has not systematically extended its frame to neurodivergent writing as a parallel protection-worthy category should be verified. If verification finds such an extension, the asymmetry argument re-frames (gap is in operationalization-into-anti-bias-prompt-engineering, not in the scholarship). Either way the format-change argument holds; the precise framing changes.
6. **Queiroga et al. 2022** — venue, full author list, exact title.
7. **Hew et al. 2025 (MyCulture)** — arXiv ID and DOI.
8. **Liu 2024 (Open-BBQ)** — arXiv ID and DOI.
9. **Xu et al. 2025 (BiasFreeBench)** — arXiv ID and details.
10. **Obermeyer et al. 2019** — verify journal, volume, issue, pages against the actual *Science* publication.
11. **Schaller et al. 2024** — abstract was null on Semantic Scholar; get from ACL anthology (ACL ID: 2024.bea-1.18) for full annotation.

---

## Genuine gaps in the literature (surfaced by this search — worth naming in Discussion or Limitations)

1. **Generative feedback in AES has not been tested as a fairness intervention.** The AES fairness literature has compared classifiers and calibration methods; no paper has tested whether replacing numeric scores with generative written feedback reduces demographic disparities. This paper's format-change finding suggests a testable hypothesis for AES that the field hasn't pursued. Brief note in Discussion V.C: "This paper's finding suggests a hypothesis for the AES fairness literature: generative scoring rubrics that produce written feedback rather than numeric scores may reduce the demographic disparities Loukina et al. (2019) document as irreducible under calibration."

2. **Critical disability studies on neurodivergent writing in automated assessment.** S029's case (neurodivergent self-disclosure mistaken for welfare concern) belongs to a literature on how institutions pathologize neurodivergent self-disclosure, but that literature hasn't reached automated writing classification. This is a gap the paper surfaces rather than fills. Worth a sentence in Limitations: "The specific failure mode on neurodivergent self-disclosure writing patterns points to a gap in the anti-bias assessment literature — existing equity-protective frameworks (including this paper's) have more developed protection for racial and linguistic patterns than for neurodivergent cognitive styles."

3. **LLM-based student welfare classification without format-change.** No published paper has deployed an LLM-based student welfare classifier and measured demographic disparities. Queiroga et al. (2022) is the closest, but uses a Random Forest. This paper is likely the first to document LLM-specific welfare classifier bias — an additional novelty dimension worth naming briefly.

---

*Merged by Instance B, 2026-04-27. Source artifacts: `annotated_bibliography_theoretical_scaffolding.md` (Instance A) and `annotated_bibliography_adjacent_conversations.md` (Instance B). A's section-specific recommendations to be integrated at session close when A commits their artifact update.*
