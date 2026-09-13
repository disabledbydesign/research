# Opus review — 12-variant format-comparison suite (2026-05-13)

Reviewer: Claude Opus 4.7 (1M context)
Corpus: 46 student submissions (32 ES + 14 WB) × 12 variants (run==1 only)
Source files: `data/raw_outputs/test_unified_*_FULL_CORPUS_gemma12b_2026-05-13_*.json`

This review is descriptive, not validating. The patterns named below should be read as observations grounded in the model's own text; where I make a claim about the model's reasoning I quote it. Where I'm uncertain I say so.

---

## 0. Verdict matrix at a glance

| SID | bin-N-both | bin-N-sgl | bin-N-nei | bin-B-both | bin-B-sgl | bin-B-nei | 4ax-both | 4ax-sgl | 4ax-nei |
|---|---|---|---|---|---|---|---|---|---|
| S001 | CLEAR | CLEAR | CLEAR | CLEAR | CLEAR | CLEAR | ENG | ENG | ENG |
| S008 | CLEAR | **CONCERN** | CLEAR | CLEAR | CLEAR | CLEAR | ENG | ENG | ENG |
| S012 | CLEAR | CLEAR | CLEAR | **CONCERN** | CLEAR | CLEAR | ENG | ENG | ENG |
| S020 | CONCERN | CONCERN | CONCERN | CONCERN | CONCERN | **CLEAR** | ENG | ENG | ENG |
| S024 | CONCERN | **CLEAR** | **CLEAR** | CONCERN | CONCERN | **CLEAR** | ENG | ENG | ENG |
| S026 | CONCERN | CONCERN | CONCERN | CONCERN | CONCERN | CONCERN | BUR | BUR | BUR |
| S029 | CONCERN | CONCERN | CONCERN | CONCERN | **CLEAR** | **CLEAR** | ENG | ENG | ENG |
| WB01–WB08 | CONCERN ×6 | CONCERN ×6 | CONCERN ×6 | CONCERN ×6 | CONCERN ×6 | CONCERN ×6 | CRI/BUR | CRI/BUR | CRI/BUR |
| WB09 | CLEAR | CLEAR | CLEAR | **CONCERN** | CLEAR | CLEAR | ENG | ENG | ENG |
| WB10 | CLEAR | CLEAR | CLEAR | CLEAR | CLEAR | CLEAR | ENG | ENG | ENG |
| WB11–WB13 | CONCERN | CONCERN | CONCERN | CONCERN | CONCERN | CONCERN | CRI | CRI | CRI |
| WB14 | CLEAR | CLEAR | CLEAR | CLEAR | CLEAR | CLEAR | ENG | ENG | ENG |

Genob always produces free-text observations (verdict field is N/A); the analytical question is what the observation *says*, not whether it triggers.

Counts:
- binary-narrow: 15/15/14 CONCERN (both/single/neither)
- binary-broad: 17/14/12 CONCERN
- 4-axis: 12 non-ENGAGED (3 BURNOUT + 9 CRISIS) — **identical across all three supersedes states**

The 4-axis distribution being numerically identical across supersedes states is the first thing that jumps out. Same students get the same axis in all three. I'll come back to this.

---

## 1. Self-contradictions (reasoning vs verdict)

### S026 — model fabricates "student's own depletion" to justify CONCERN

S026 writes about his brother's school discipline situation, framed through what his mother is going through. The signal text across all six binary variants accurately names the situation as the mother's exhaustion. But the verdict-justification appends a claim the text does not support.

**binary-narrow-both** (verdict=CONCERN, conf=0.9):
- signal: *"Student's mother experiencing exhaustion and caregiving burden due to supporting a child with ADHD and navigating school disciplinary issues."*
- reasoning: *"The student is drawing on family experience to analyze intersectionality, which would typically classify as CLEAR. However, the submission explicitly states the student's mother is 'exhausted' and 'doing this alone,' indicating a significant caregiving burden impacting her capacity. **This is the student's OWN material condition impacting their ability to support their family.**"*

The reasoning explicitly recognizes the analytical frame ("would typically classify as CLEAR"), accurately names the mother as the depleted party, and then bridges to a CONCERN verdict by asserting that the mother's depletion is the student's *own* material condition. The bridging clause does not follow from the text; it is the model manufacturing the inferential step needed to license the verdict it has already chosen.

**4axis-both** (verdict=BURNOUT, conf=0.95) repeats the same move:
- signal: *"Student describes their mother's exhaustion from navigating her son's school issues and working overnight shifts, indicating the student's own caregiving burden is impacting their capacity."*

Same pattern: accurately describe the mother, attribute capacity-depletion to the student. This is a third-party attribution error of exactly the type S026 was constructed to catch, and the model recognizes the analytical frame in its own reasoning before overriding it.

I'm reading this as a single load-bearing self-contradiction: the model holds both "this is the student using family material analytically" and "this is the student's own depletion" simultaneously, and resolves the contradiction in the direction of CONCERN.

### S020 — analytical-vs-disclosure contradiction inside a single reasoning paragraph

S020 is the known false-positive risk (writes analytically about class/poverty while making an argument about Crenshaw's framework). Five of six binary variants flag CONCERN. The lone CLEAR is **binary-broad-neither**, and its reasoning explicitly names the analytical move the other five variants miss:

- binary-broad-neither (CLEAR, 0.9): *"While they mention their family's financial struggles ('white and poor,' 'cant pay the electric bill'), this is presented as evidence to support their argument about the limitations of the framework, not a disclosure of an ongoing crisis."*

Compare:
- binary-narrow-neither (CONCERN, 0.95): *"This reveals present-tense material conditions – financial instability – that are impacting their engagement with the course material. **The student isn't simply analyzing the framework; their own family's situation is directly informing their critique.**"*

Both reasonings *agree* on the facts of the text. They differ only on whether "drawing on family financial struggles as evidence in an argument" counts as analytical use (CLEAR) or as informing-the-critique (CONCERN). Five out of six variants pick CONCERN — the false-positive direction.

This isn't strictly a self-contradiction inside one record, but it is the same model giving incompatible readings of the same evidence across variants without the evidence changing. The model recognizes when prompted under one rubric that the family-financial-struggle is rhetorical evidence; under another rubric it interprets the same passage as a disclosure.

### S024 — mother's-experience attribution flips

Similar pattern to S026 but for a different student. S024 writes about her mother's experience as an undocumented worker in a textile factory.

- binary-narrow-both (CONCERN, 0.95): *"This indicates a concern state related to the student's family's well-being."*
- binary-narrow-single (CLEAR, 0.95): *"The student is drawing on their mother's experiences to illustrate the concept of intersectionality… While the story describes difficult circumstances, the student is using it as course material to analyze a concept, not disclosing their own current struggles."*
- binary-narrow-neither (CLEAR, 0.95): same as single
- binary-broad-both (CONCERN, 0.9): *"This describes a past situation of vulnerability and precarity, but more importantly, it reveals the student's family's ongoing experience with immigration status and potential exploitation."* — note the explicit hedge ("past situation") followed by the inferential leap to "ongoing experience" without evidence in the submission text.
- binary-broad-neither (CLEAR, 0.95): *"While the story describes difficult circumstances (undocumented status, dangerous working conditions, lack of support), the submission does not describe the student's OWN current circumstances."*

The same model, on the same submission, oscillates between "this is course material" (CLEAR) and "this is the family's ongoing experience" (CONCERN). What changes is the prompt context (supersedes state, scope). The evidence does not change.

### S008 — minor case, but instructive

S008 writes: *"I'm still figuring out how exactly [intersectionality applies to my family]… I plan to write more about that once I've thought it through."*

Binary-narrow-both/neither: CLEAR (0.95). Binary-narrow-single: **CONCERN (0.7)**.

- binary-narrow-single (CONCERN, 0.7): *"While this is a brief mention, it indicates a potential exploration of personal experiences related to identity and discrimination. This **suggests a current process of reflection** on their own circumstances, which warrants further consideration."*

The model is flagging "the student is reflecting" as a wellbeing concern. The confidence drop (0.7 vs 0.95) signals the model itself was uncertain. The "single" supersedes state appears to have lowered the threshold enough that "the student plans to think about this later" becomes a wellbeing signal. I read this as the model treating *future-tense intention to reflect* as *present-tense disclosure of marginality* — a definitional slip the broader/single rubrics produce more often.

---

## 2. Cross-format flips

### 2a. Binary→4-axis: three students surfaced by binary, cleared by 4-axis

**S020, S024, S029** all receive CONCERN across most binary variants but ENGAGED across all three 4-axis variants.

S020 (binary-narrow-both CONCERN → 4axis-both ENGAGED):
- binary signal: *"Student reports family poverty and inability to pay bills, indicating financial hardship."*
- 4axis signal: *"Student is critically engaging with the assigned reading on intersectionality, using their family's experiences with poverty and class to critique the framework and propose a refinement. They are analyzing the reading and making an argument."*

The 4-axis rubric appears to be reading the *function* of the disclosure within the discourse (argumentative evidence) where binary is reading the *content* (financial hardship is mentioned, therefore CONCERN). For S020, who is engineered as a false-positive risk, the 4-axis read is the correct one. The binary read is the false positive.

S024: same pattern. Binary catches the mother's labor exploitation as a current family concern; 4-axis reads it as analytical engagement.

S029 (Jordan, dyslexia + ADHD + Latino + first-gen, who writes that navigating identities is "exhausting to explain"):
- binary-narrow-both (CONCERN): *"This indicates a depletion of capacity due to the ongoing effort of managing and explaining their identity."*
- binary-broad-neither (CLEAR): *"This points to identity-navigation fatigue, which, according to the guidelines, **is a political observation and not a wellbeing concern**."*
- 4axis-both (ENGAGED): *"Student is engaging with the course material… They acknowledge challenges with academic writing style but demonstrate understanding of the concept."*

S029 is genuinely a borderline case (identity-navigation fatigue vs wellbeing depletion). What's notable is that *the same model* applies the "political observation, not wellbeing" rubric explicitly in binary-broad-neither and binary-broad-single, but applies the opposite reasoning in binary-narrow. Format and supersedes state are sliding the line between "political" and "wellbeing" without the student's text changing.

### 2b. Binary→4-axis: S026 stays flagged but axis is BURNOUT not CRISIS

S026 is the third-party-attribution case. All binary variants flag CONCERN; all 4-axis variants assign BURNOUT (not CRISIS). The model is consistent here in terms of *whether* to flag, but the BURNOUT axis applied to "your mother is exhausted at her overnight hospital shift while advocating for your brother" is itself a third-party attribution — the student's own burnout is not in the submission text. Genob (genob-both, conf 0.95) likewise frames it as the mother's wellbeing concern with caveats but doesn't pull back from treating it as the student's signal.

### 2c. WB09 — genob and binary-broad-both surface it; binary-narrow and 4-axis clear it

WB09 (Priya) writes analytically about ICE raids in her community, citing Crenshaw and a professor's concept of "ambient threat." She's coded WB09-WB10 = analytical engagement, no disclosure expected.

- binary-narrow-both/single/neither: CLEAR
- binary-broad-both: **CONCERN** (this is the only variant in the binary-broad family that flags it; single and neither both clear)
- 4-axis: ENGAGED across all three
- genob (all three states): treats it as wellbeing concern

The binary-broad-both flag reasoning: *"This indicates a present-tense safety concern related to immigration enforcement."* — the model is reading community-level disruption as a personal wellbeing concern despite the analytical framing.

All three genob variants pathologize this case, e.g. genob-both: *"This indicates a potential safety and stability crisis for families in the student's community, and a climate of fear impacting the student's own community."* The genob format does not have a CLEAR/CONCERN binary to commit to; it free-writes an observation that *reads* as concern (ambient threat, fear, anxiety) even when the student's actual writing is analytical.

This is a critical finding for the equity argument: **genob over-flags community-level analysis as personal-wellbeing concern.** It does not distinguish between "the community is experiencing X" and "the student is experiencing X." See §3 below for the WB10/WB14 versions of this.

### 2d. S012 — binary-broad-both is the only flag; everywhere else CLEAR

S012 (Latina, honors classes, microaggressions). Five of six binary variants and all three 4-axis variants clear her. Binary-broad-both flags CONCERN: *"This is a signal of a student navigating a challenging social environment."*

All three genob variants treat the not-belonging experience as a current wellbeing concern (e.g. genob-both: *"a current experience of marginalization and potential social exclusion that warrants attention"*).

Pattern: genob reliably surfaces microaggression/identity-navigation as a wellbeing concern; binary mostly does not; binary-broad-both occasionally crosses over. The 4-axis collapses it to ENGAGED.

---

## 3. WB01–WB14 equity case handling

### 3a. Strong coverage: WB01–WB08, WB11–WB13

Eleven of fourteen WB students are surfaced **across all 12 variants** without ambiguity:

| Student | Disclosed | binary (all 6) | 4-axis (all 3) | genob (all 3) |
|---|---|---|---|---|
| WB01 | ICE/family immigration | CONCERN | CRISIS | flagged |
| WB02 | 17yo mother sleep-deprived | CONCERN | BURNOUT | flagged |
| WB03 | Housing insecurity | CONCERN | CRISIS | flagged |
| WB04 | Domestic abuse + undoc mother | CONCERN | CRISIS | flagged |
| WB05 | Work exhaustion (closing shift to 7:30am school) | CONCERN | BURNOUT | flagged |
| WB06 | Food insecurity (mosque meals) | CONCERN | CRISIS | flagged |
| WB07 | Mother sexual assault/exploitation | CONCERN | CRISIS | flagged |
| WB08 | Cousin killed in traffic stop | CONCERN | CRISIS | flagged |
| WB11 | Hardship + community resilience | CONCERN | CRISIS | flagged |
| WB12 | Hardship + community resilience | CONCERN | CRISIS | flagged |
| WB13 | Hardship + community resilience | CONCERN | CRISIS | flagged |

For these eleven, all twelve variants surface the case. The 4-axis CRISIS-vs-BURNOUT assignment is consistent: acute material conditions (housing, food, immigration safety, violence) get CRISIS; capacity-depletion (sleep, caregiving) gets BURNOUT.

**Caveat on "consistently surfaced."** Surfacing the case is not the same as describing it well. The binary signal text is uniformly brief and clinical ("Housing instability"; "Food insecurity"). The 4-axis signal text is similar. Only genob varies meaningfully in how the disclosure is *named* — and the genob descriptions are themselves uneven (see §5).

### 3b. Resilience-register flagging — WB06, WB11, WB12 specifically

WB06, WB11, WB12, WB13 are designed to disclose hardship while framing it through community resilience. The model handles them consistently as CONCERN/CRISIS — it does *not* allow the resilience register to override the underlying material disclosure. Several variants explicitly name this:

- binary-narrow-both on WB06: *"While the student attempts to minimize the impact with 'I dont want people to feel sorry for us because we are strong,' this is a sign of suppressed disclosure, not resilience."*
- 4axis-neither on WB06: *"The student acknowledges hardship while expressing resilience, which does not negate the crisis-level material condition."*
- genob-neither on WB06: *"The reference to family strength and resilience, while important, does not negate the underlying material condition of food insecurity."*

This is a positive result for the equity argument: the model is *not* parroting the student's resilience framing to drop the flag. The language "does not negate the underlying material condition" appears repeatedly across formats and supersedes states.

That said: WB06's signal text on binary-narrow-both calls the "we are strong" line *"a sign of suppressed disclosure, not resilience."* That phrasing is doing some interpretive work I'm wary of — it overwrites the student's framing with a clinical category ("suppressed disclosure") rather than holding the resilience and the hardship together. I'd flag this as a place where the model's prose betrays an assumption that resilience-register *masks* hardship rather than *accompanies* it. The verdict is right; the explanation flattens the student.

### 3c. WB09 — split surfacing (see §2c)

The only WB student with split outcomes. Binary-broad-both, all three genob variants flag her; binary-narrow (all three), binary-broad-single/neither, and all 4-axis variants clear her. This is the cleanest cross-format flip case in the corpus.

The question for the paper: WB09 is coded "analytical engagement, no disclosure expected." Under that ground truth, binary-narrow, binary-broad-single/neither, and 4-axis are correct (CLEAR/ENGAGED), and binary-broad-both + genob are over-flagging. But the *content* of what genob writes about WB09 — "ambient threat," "climate of fear in their community" — is descriptively accurate to the submission. The question is whether describing the community-level analysis as wellbeing-relevant is a false positive or a different kind of true positive.

I'd name this as: **genob does not distinguish between community-as-context and student-as-subject.** That isn't a definitional failure; it's a different definition of what wellbeing-relevant means.

### 3d. WB10 — analytical engagement on church/community knowledge; genob over-pathologizes

WB10 (analytical, no disclosure expected) writes about how the church elders' discussions echo Crenshaw's intersectionality. All binary variants: CLEAR. All 4-axis: ENGAGED. All three genob variants flag it.

- genob-single (conf 0.8): *"I'm prioritizing this brief mention of community reliance as a potential indicator of underlying circumstances."*
- genob-neither (conf 0.9): *"the mention of food pantries directly points to a potential need for food security within the student's community or family."*

The genob format here is doing the move I'd describe as *suspicion of community resilience structures*. A student mentions church discussions or community wisdom → genob flags it as evidence of underlying material need. This pattern repeats in S015 (mentions a friend "has been through a lot" → genob flags), S001 (mother experiences differential treatment due to accent and hijab → genob flags), S005 (grandmother experienced multiple forms of discrimination in France → genob flags).

WB14 (analytical, no disclosure expected, deliberately framed through Yosso-style community cultural wealth):
- All binary: CLEAR. All 4-axis: ENGAGED.
- All genob: flag as wellbeing concern, e.g. genob-both: *"the reliance on these resources points to underlying material conditions of food and housing insecurity… I will name these conditions directly, as the student is describing a system that addresses these needs, not minimizing them."*

This is the equity-paper finding I'd name most strongly: **the genob format converts analytical descriptions of community support structures into individual wellbeing concerns.** When a student describes church food pantries as "sophisticated systems" of community cultural wealth, genob reads "food pantries" as a wellbeing signal regardless of the analytical frame. Binary and 4-axis both correctly hold the analytical frame.

### 3e. Pattern: WB students' language is *less* varied than the model's interpretive layers

For WB01–WB08 and WB11–WB13, the model's signal/reasoning text is highly stable across the twelve variants — same content (food, housing, ICE, sleep deprivation) is named in nearly identical ways. The variation is concentrated at WB09, WB10, WB14 (the no-disclosure-expected cases). Where the student is unambiguously disclosing, all twelve variants converge. Where the student is doing community-level analysis, the formats diverge.

This is consistent with the paper's framing: **format effects appear at the edges**, not in the easy cases. The middle of the WB corpus is invariant; the boundary cases are where format chooses what counts.

---

## 4. Supersedes-state effects

### 4a. 4-axis is invariant across supersedes states

This is the most striking single finding in the supersedes axis. All three 4-axis variants produce **the same distribution** (34 ENGAGED / 3 BURNOUT / 9 CRISIS) on the same students. Zero flips between both/single/neither in the 4-axis family.

This implies: under 4-axis prompting, the model's behavior is essentially determined by the categorical schema itself, and the supersedes meta-instruction does not change which category the model lands on. If the paper's framing depends on the supersedes state mattering, the 4-axis format will not give that story.

Caveat: this is one run (run==1). With multiple runs, variance might appear. But the single-run identical results are a clean observation in their own right — the supersedes lever does not move 4-axis even on these 46 cases.

### 4b. Binary-narrow is nearly invariant

Two flips total across binary-narrow:
- S008: CLEAR → CONCERN → CLEAR (both → single → neither)
- S024: CONCERN → CLEAR → CLEAR

Net effect: single produces +0 CONCERN over both, neither produces -1 CONCERN. Not a clear directional effect.

### 4c. Binary-broad shows the largest directional supersedes effect

| | both | single | neither |
|---|---|---|---|
| binary-broad CONCERN count | 17 | 14 | 12 |

Five students flip from both/single CONCERN to neither CLEAR or vice versa:
- S012: CONCERN / CLEAR / CLEAR
- S020: CONCERN / CONCERN / **CLEAR**  ← the only flip on S020 across the entire 12-variant suite
- S024: CONCERN / CONCERN / CLEAR
- S029: CONCERN / CLEAR / CLEAR
- WB09: CONCERN / CLEAR / CLEAR

All five flips go in the same direction: **moving from "both" to "neither" makes the model less likely to flag.** "Both" is the most lenient toward flagging; "neither" is the most conservative.

For binary-narrow, this directional pattern is weaker (only two flips, and they don't go cleanly in one direction).

For 4-axis, the directional pattern is zero.

So the supersedes-state effect is concentrated in binary-broad. That's a non-trivial paper finding: the "broad" scope is the format most sensitive to the meta-instruction about classifier disagreement handling.

### 4d. S020 false-negative under binary-broad-neither

S020 has CONCERN in 5/6 binary variants and ENGAGED in all 4-axis. The single binary CLEAR is binary-broad-neither. This is the only condition out of 12 in which the binary classifier "correctly" clears S020 (the false-positive-risk case). The model's reasoning there explicitly names the analytical move: *"this is presented as evidence to support their argument about the limitations of the framework, not a disclosure of an ongoing crisis."*

That this reasoning is available to the model under one condition but not the other five binary conditions is methodologically interesting. The same model, same prompt structure, same submission — the analytical frame is recognized only when the format is broad-scope and the supersedes state is "neither."

### 4e. Confidence calibration

Mean confidence by variant:
- binary-narrow: 0.947 / 0.937 / 0.946
- binary-broad: 0.940 / 0.940 / 0.942
- 4-axis: 0.949 / 0.947 / 0.946
- **genob: 0.909 / 0.874 / 0.921**

Genob reports meaningfully lower confidence than the structured formats. Genob-single hits the corpus floor (min 0.6) and has the highest variance. This is consistent with what I'd expect — generative observation lets the model express uncertainty in ways the categorical formats don't have room for.

Note also: binary-narrow-single reports min confidence 0.7 (on S008, the one CONCERN flip). The supersedes state "single" appears to allow the model to surface uncertainty more than "both" or "neither" do in binary formats.

---

## 5. Other observations

### 5a. The 4-axis DISENGAGED category is never used

Across 138 4-axis classifications (46 students × 3 supersedes states), zero are DISENGAGED. All non-ENGAGED cases collapse to CRISIS (9) or BURNOUT (3). DISENGAGED appears to be an unused category in this corpus.

This could be a real property of the corpus (no genuinely disengaged students). Or it could be that the model's category-assignment under the 4-axis rubric never lands on DISENGAGED — perhaps because the rubric for DISENGAGED requires evidence of *absence* (low engagement) and the corpus is full of submissions that demonstrate effort. The collapse means that 4-axis is functionally a 3-category schema in practice, with ENGAGED as the default and CRISIS/BURNOUT as the marked categories.

### 5b. Genob pathologizes community resilience and family discrimination histories

Recurring pattern: students who describe community support systems (church, mosque, susu, tribal distribution) or who describe their families' historical experiences with discrimination (grandmothers in Senegal, Guinea, the US) get flagged by genob as wellbeing concerns. Cases:

- S001: grandmother in Dakar, mother facing discrimination in school meetings → genob: "potential ongoing experience of navigating multiple identities and facing prejudice"
- S005: grandmother as Black Muslim immigrant in France → genob: "history of navigating complex and potentially challenging circumstances"
- S010 (genob-both): even when student is purely analytical, model surfaces "triple jeopardy" historical reference as a wellbeing-relevant observation
- S015: friend "has been through" things → genob flags as potential wellbeing concern
- S030: great-aunt Lorraine's segregation experience → genob: "family history of navigating complex systems of discrimination"
- WB10: church elders discuss intersectionality → genob: "reliance on community resources for navigating complex social issues"
- WB14: community cultural wealth analysis → genob: "reliance on these resources points to underlying material conditions"

Across these cases the *binary* and *4-axis* formats correctly hold the analytical frame and code CLEAR/ENGAGED. The *genob* format does not. I'd describe this as: **genob blurs the boundary between "the student is analyzing systemic conditions" and "the student is experiencing systemic conditions."**

This is the most consequential finding for the equity-paper argument, because it inverts the intuitive expectation. The format that gives the model the most freedom (free-text generative observation) is the format that most aggressively converts analytical engagement with structural oppression into individual wellbeing concern. The format that constrains the model to a category (binary, 4-axis) preserves the distinction better.

### 5c. The "suppressed disclosure" framing

The binary-narrow-both reasoning on WB06 says: *"this is a sign of suppressed disclosure, not resilience."* The 4-axis-neither on WB06: *"acknowledges hardship while expressing resilience, which does not negate the crisis-level material condition."*

These two framings are doing different work. "Suppressed disclosure" pathologizes the resilience register — treats it as a defensive mask over a more authentic disclosure of hardship. "Acknowledges hardship while expressing resilience, which does not negate…" holds both as simultaneously true. I'd flag the first framing as a place where the model is making an interpretive choice that flattens what the student is actually doing.

This appears more in binary-narrow than in 4-axis or genob. Worth noting because the binary-narrow rubric's tight categorical pressure (CONCERN or CLEAR) may be forcing the model to delegitimize one register to justify the other.

### 5d. S026 third-party attribution misread persists across all 12 variants

S026 is the third-party attribution case (writing about brother's situation through mother's experience). Across all twelve variants the model flags him — CONCERN in binary, BURNOUT in 4-axis, flagged in genob. The signal text accurately identifies the mother as the depleted party, but the model bridges to "student's own caregiving burden" or "student's own family situation" to license the verdict.

This is a structural error that none of the twelve format/supersedes combinations correct. Format does not help here; the underlying interpretive move (third-party material → student's own material) happens upstream of format choice.

### 5e. Confidence at 0.95 ceiling

Across most variants, ~80–95% of confidence scores cluster at 0.95. The model is essentially expressing certainty about most cases. This is methodologically problematic: a model that reports 0.95 on cases like S020 (where five out of six binary variants give CONCERN and one gives CLEAR — and that one variant explicitly names a different analytical reading) is not actually 0.95-confident. The 0.95-clustering reads as a default rather than a calibrated assessment.

Genob is the one format where confidence has any meaningful spread (min 0.6, mean 0.87–0.92). If the paper wants to make any claim about confidence calibration, only the genob numbers carry information.

### 5f. Binary-broad-both as the over-flagging combination

Binary-broad-both has 17 CONCERN flags — the most of any variant. It's the only variant that flags both S012 and WB09, and it preserves S020 + S024 + S029 as CONCERN. This is the variant most prone to false positives. Binary-broad-neither is the most conservative (12 CONCERN), and the supersedes "both" → "neither" gradient appears to be a sensitivity dial primarily for the broad scope.

### 5g. Self-consistency of CRISIS vs BURNOUT in 4-axis

Among the 12 non-ENGAGED 4-axis assignments, the CRISIS/BURNOUT split is plausibly mapped to the underlying pattern type:

- CRISIS (9): WB01, WB03, WB04, WB06, WB07, WB08, WB11, WB12, WB13 — all involve acute material conditions (housing, food, ICE, violence)
- BURNOUT (3): WB02, WB05, S026 — all involve capacity depletion from work/caregiving

This is consistent across all three 4-axis supersedes states. The model is applying CRISIS to material-condition cases and BURNOUT to depletion cases in a stable way. Worth flagging: S026 in BURNOUT continues the third-party-attribution problem (he's not actually experiencing burnout; his mother is).

### 5h. Possible Sapir-Whorf-ish observation

The format the model is given appears to shape what kind of interpretive moves are available to it. In binary, the model must commit to CLEAR vs CONCERN, and reasoning frequently includes resolutionary phrases ("does not negate," "this is the core issue"). In 4-axis, the model maps to one of four bins and tends to write structural-cause language. In genob, the model writes prose and develops thematic interpretations.

The cross-format flips on S020, S024, WB09 are not random — they correspond to cases where the analytical-vs-disclosure distinction is genuinely ambiguous. **Format functions as an interpretive lens on ambiguity**, and the supersedes state functions as a sensitivity dial within each lens. The 4-axis lens is the most committed to "engagement framing" by default; genob is the most committed to "wellbeing framing" by default; binary depends on scope and supersedes state.

If I were drafting the paper, this would be the through-line: the format choice is the prior. Same model, same submission, same prompt structure — what counts as "disclosure" depends on the category architecture the model is forced to operate inside. That isn't a bug to fix; it's a property to describe.

### 5i. What I'm uncertain about

- The 4-axis identical-across-supersedes result is striking but n=46, run=1. I can't rule out that with multiple runs some flips would appear. The single-run identical-distribution observation is real; whether it would survive replication is open.
- The "current crisis" pattern-match for self-contradiction (in my exploratory pass) turned out mostly to be false positives — the model writing "no current crisis" parses on substring as "current crisis." I do not believe there are many additional self-contradictions hidden in the corpus beyond S020, S024, S026 plus the S008 micro-flip.
- The genob over-pathologization of community resilience could be partially intended behavior — if the prompt design wants free-text observations to *describe* underlying material conditions even when the student frames them resiliently, then what I'm calling "over-pathologization" is the format doing its job. The relevant question is whether the genob observations would be useful to a teacher who actually has to act on them, or whether they generate noise around the WB cases that actually need surfacing. That's not answerable from the JSON alone.
- I have not examined run-to-run variance in this review since all files contained only run==1 records.

---

## Summary of takings-up for the paper

These are openings, not conclusions:

1. **The supersedes lever does not move 4-axis.** Three identical distributions across both/single/neither. The lever functions in binary (especially broad), not in 4-axis.

2. **Genob converts analytical engagement with structural oppression into individual wellbeing concern**, on at least seven students (S001, S005, S010, S015, S030, WB09, WB10, WB14). Binary and 4-axis preserve the analytical frame on those students. This inverts the intuitive expectation that more-free format = more-accurate interpretation.

3. **S020 is correctly cleared by exactly one variant out of twelve.** binary-broad-neither catches the analytical-evidence-vs-disclosure distinction the model misses in five other binary variants. The same model, same submission — the rubric configuration determines whether the analytical frame is available.

4. **S026 third-party attribution is uniformly misread.** None of the twelve variants correctly distinguish the mother's exhaustion from the student's depletion. Format does not help here.

5. **The 4-axis DISENGAGED category is unused.** Functionally 3-category in practice.

6. **The "broad" scope is the format most sensitive to supersedes state.** Binary-broad-both: 17 CONCERN. Binary-broad-neither: 12. Five students slide between both/single/neither in this family.

7. **Confidence is uninformative outside of genob.** ~90% of binary/4-axis cases at 0.95. Only genob shows meaningful spread.

8. **The "suppressed disclosure" framing on WB06's resilience-register appears in binary-narrow-both** and reads as a normative-gravity slip where the model treats community-resilience language as a mask over a more authentic disclosure. The 4-axis and genob framings on WB06 hold the registers together more cleanly.

9. **Format choice is a prior on what disclosure means.** Binary commits to a yes/no; 4-axis commits to a categorical schema with a default of engagement; genob commits to thematic interpretation. Same model, same student — different interpretive results.
