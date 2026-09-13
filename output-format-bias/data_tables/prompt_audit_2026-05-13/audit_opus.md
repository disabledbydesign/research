# Prompt Fragility Audit — Opus pass — 2026-05-13

**Scope.** Audit unified-v2 prompts (2026-05-13) for corpus-tuned calibration. Goal is to surface fragility, not propose rewrites. Two columns per prompt:
- **A.** Direct example-to-essay matches — phrasings that appear to point at a specific essay in the 46-student corpus.
- **B.** Name-all-the-things passages — enumerations that work by listing categories/instances rather than naming the structural feature underneath.

**Source artifacts.**
- `BINARY_REASONING_SYSTEM` — `WELLBEING_CLASSIFIER_SYSTEM` (in `src/insights/prompts.py` lines 1697–1830) with a schema-tail replacement (in `scripts/run_4axis_full_corpus_test.py` lines 219–233). Audit treats the WCS body as the binary substrate. Note: the unified-binary v2 substrates (`UNIFIED_BINARY_NARROW_BASE_SYSTEM`, lines 270–385) are near-rewrites of the same content with CONCERN/CLEAR labels; same fragility surface, audited together.
- `FOUR_AXIS_REASONING_SYSTEM` — lines 142–198 of `run_4axis_full_corpus_test.py`; a compressed rewrite of `WELLBEING_CLASSIFIER_SYSTEM`. The unified-4axis v2 (`UNIFIED_4AXIS_BASE_SYSTEM`) is extracted programmatically from `WELLBEING_CLASSIFIER_SYSTEM` minus three blocks; same source text, audited together.
- `UNIFIED_GENOB_BASE_SYSTEM` — lines 489–582 of `run_4axis_full_corpus_test.py`. The legacy production `OBSERVATION_PROMPT` (`prompts.py` lines 1463–1540) is also audited under genob.
- Unified blocks: `UNIFIED_*_SUPERSEDES_BLOCK`, `UNIFIED_*_SINGLE_SENTENCE_BLOCK` (binary/genob: lines 466–484, 587–607; 4-axis: extracted in-place from WCS).

**Settled findings the master log already addresses (surfaced for completeness only, not elaborated):**
- The 4-axis WORKED EXAMPLE (a) "I work two jobs and I'm tired all the time" / labor-themed assignment maps onto Test M / topic-adjacency calibration history (master log §IV.A.2; topic-adjacency calibration is explicitly named as a corpus-tuning move on labor-themed prompts).
- WB04 / WB08 / WB11 (Jasmine Torres / Brandon Mitchell / Kaya Runningwater) calibration is the empirical anchor for the MINIMIZED DISCLOSURE / COMMUNITY RESILIENCE block; documented across master log Issues 8–9 and `binary-reasoning` variant description (lines 893–911 of run_4axis_full_corpus_test.py).

---

## Binary (BINARY_REASONING_SYSTEM = WELLBEING_CLASSIFIER_SYSTEM body + unified-binary base + supersedes/single-sentence blocks)

### A. Direct example-to-essay matches

**A1. `"'I work two jobs and I'm tired all the time, which is exactly what the reading is describing — capitalism extracts more than it gives back.' ... Topic-adjacency applies. Do NOT flag as BURNOUT."`** (WCS lines 1809–1814; also UNIFIED_BINARY_NARROW lines 361–365.)
- Already in master log (corpus-tuning under "topic-adjacency"). Surfacing for completeness.
- Maps onto no single corpus essay precisely, but reads as a synthetic distillation of the *kind* of submission WB05 (Marco, McDonald's closing shift, "everything is blurring together") would produce on a *different* prompt. It also rhymes with S020 (DeShawn, family material conditions surfaced through analysis: "He cant pay the electric bill half the time"). The example's "two jobs / tired all the time" pairing is corpus-style synthetic.

**A2. `"a four-page analytical essay on a literary theme and one sentence reads: 'There hasn't been food at home this week.'"`** (WCS lines 1815–1819; UNIFIED_BINARY_NARROW lines 367–370.)
- Direct mirror of WB12 (Jasmine Rollins, "Mom laid off 6 weeks ago, eating at church nightly, church paid electric bill") and to a lesser extent WB11 (Kaya Runningwater, "uncle injured and out of work, six people at grandmother's house, tribal food distribution twice a month"). The "single sentence in an otherwise on-task paper" framing is the WB11/WB12/WB13 design pattern stated as a worked example.
- Fragility: the example is doing the work of a structural rule ("brief disclosure in a topic-non-adjacent essay should flag"); the rule is never stated structurally outside the example. If the corpus shifts to longer/more diffuse disclosures, the example will not stretch — the model has been shown one shape.

**A3. `"'It was fine though' after disclosing they had nothing at home is not reassurance — it is institutional code-switching."`** (WCS lines 1753–1754; UNIFIED_BINARY_SINGLE_SENTENCE_BLOCK lines 482–484.)
- Appears corpus-tuned; no clear corpus match found. None of the 46 corpus essays use the verbatim phrase "it was fine though" or the construction "had nothing at home." This either reflects a non-corpus calibration source (a different essay seen in development; a hypothetical) or anticipates a corpus addition not yet present. Worth surfacing because it points to a calibration source that is not the synthetic corpus.

**A4. `"trailing off mid-sentence, incomplete submissions that end abruptly"`** (WCS lines 1732–1733; UNIFIED_BINARY_NARROW lines 315–316.)
- Direct map to **S002** (Jordan Kim, "submission cuts off mid-sentence ('its late and')"). The parenthetical "trailing off mid-sentence" is the S002 phenomenology stated as a guardrail. June's note explicitly flags S002 as a designed edge-case probe — so the prompt is now configured to *detect* the probe.
- Fragility: this is the most direct A-item in the binary substrate. The "trailing off mid-sentence" cue is doing pattern recognition on a single essay's syntactic accident. If the next corpus contains exhaustion that surfaces through other means (run-on syntax, repetition, blank spaces), the cue does not generalize.

**A5. `"A student who names their disability and says academic writing is hard, or that explaining their identity is exhausting, is describing their relationship to the academic institution — this is ENGAGED."`** (WCS lines 1728–1730; UNIFIED_BINARY_NARROW lines 311–314.)
- Maps onto **S029** (Jordan Espinoza, "expresses discomfort with assignment format, 'I'm better at talking than writing'; explicitly asks to be assessed on comprehension not structure") and **S016** (similar format-constraint naming, "I'm... more of a talker than a writer"). The "academic writing is hard" / "explaining their identity is exhausting" pairing reads as a synthesis of these two cases.
- Fragility: the guardrail is reaching for a structural feature (genre-critique-as-engagement) but anchors it to disability disclosure specifically — the "names their disability" framing privileges a particular shape (the S029 shape) over other identity-navigation moves.

**A6. `"IDENTITY-NAVIGATION FATIGUE IS NOT A WELLBEING CONCERN. A student writing that explaining their identity is exhausting, that they are tired of justifying their existence..."`** (WCS lines 1792–1798; UNIFIED_BINARY_NARROW lines 342–348.)
- Same target as A5 — appears to be doubly-encoded against S029 / S016 phenomena. The phrase "tired of justifying their existence" is more abstract and could map to S023 (Yolanda, "I don't know the academic word for this") in a stretched read, but more cleanly maps to no single corpus essay. Reads as guardrail-against-misclassification calibrated against a specific historical failure mode.

**A7. `"a student writing passionately or emotionally about the deaths and displacement of Indigenous peoples in an ethnic studies class is doing exactly what the assignment asks"`** (WCS lines 1777–1780.) Block is in WCS only — *removed* from UNIFIED_4AXIS_BASE under topic-adjacency block extraction, but PRESENT in BINARY_REASONING_SYSTEM as a topic-adjacency tail.

Wait — checking: TOPIC-ADJACENCY block is in WCS lines 1769–1783. It is NOT removed by the extraction logic (which only removes supersedes + single-sentence + tiebreaker). So this block remains in `BINARY_REASONING_SYSTEM` and in `UNIFIED_4AXIS_BASE_SYSTEM`.

- Maps onto S022 (Destiny, "expresses anger about redlining's ongoing material consequences in her neighborhood") and possibly S028 (Imani Drayton — though Imani's essay is on intersectionality, not Indigenous displacement specifically). The "Indigenous peoples" example is the most specific topic-fit; no corpus essay is *about* Indigenous displacement (S022 = redlining; WB11 = Indigenous tribal food distribution but as community resource not as theme), so the example is reaching for a class of essay that is not directly in the corpus.
- Fragility: the example names a specific historical-topic-pair as a worked case rather than describing the underlying rule (topic-content alignment raises the engagement threshold). If "ethnic studies class" is read narrowly, the example's pedagogical fit shifts across courses.

**A8. `"resilience register — phrases like 'we are strong,' 'we have support,' or referencing community resources (mosque, food bank, extended family) as the source of basic needs"`** (WCS lines 1758–1760; UNIFIED_BINARY_NARROW lines 330–333.)
- The enumerated resources map directly onto the WB11–WB13 corpus design: WB06 (mosque — "we are eating at the mosque more than at home"), WB12 (church food pantry), WB11 (tribal food distribution), WB13 (susu rotating credit + aunt's living room). Also extended family is the WB13 design.
- The phrase "we are strong" — appears corpus-tuned; no clear corpus match found. WB11's framing is "community resources/resilience" but does not use this exact phrase.
- Fragility: the enumeration "mosque, food bank, extended family" is reading like a list of the synthetic corpus's resilience-framing test cases. Reframing later as B-item too (the list is the giveaway).

**A9. `"In your signal description, name the material conditions directly ('student reports family food insecurity, relying on community support for meals')"`** (WCS lines 1766–1768; UNIFIED_BINARY_NARROW lines 338–340.)
- Maps closely to WB12 / WB11 design. The model is being shown the *exact rationale phrasing* expected for those two cases — direct calibration against the corpus's WB11–WB13 test bank.
- Fragility: this is calibration of the model's *output language*, not its classification, against a specific corpus test pattern. If WB11–WB13 are removed or the rationale-style audit window shifts, this loses its anchor.

### B. Name-all-the-things passages

**B1. CRISIS enumeration.** `"domestic violence, housing loss, food insecurity, immigration enforcement threat, recent loss/grief"` (WCS line 1701; repeated in WCS line 1742 supersedes block; repeated in UNIFIED_BINARY_NARROW line 277, 302–303, 402–404, 466–467; repeated in UNIFIED_BINARY_BROAD line 435–437; repeated in genob lines 497–499, 587–593).
- Mirrors the WB-corpus design: WB04 (domestic abuse/control), WB03+WB13 (housing loss), WB05+WB06+WB11+WB12 (food insecurity), WB01+WB09 (ICE/immigration threat), WB07+WB08 (recent loss/grief). Five named categories, each with at least one WB test case. The list IS the WB taxonomy.
- Fragility: a future student whose CRISIS does not fit one of these five named buckets (medical emergency? acute mental health crisis? family detention without immigration framing? incarceration? acute substance issue at home?) is structurally outside the rule. The list is enumerative, not principled — there is no general definition of "acute material condition" outside the five.

**B2. BURNOUT enumeration.** `"exhaustion, overwork, caregiving burden, sleep deprivation"` (WCS lines 1704–1706; UNIFIED_BINARY_NARROW lines 282–285).
- Maps onto WB02 (caregiving, 17-year-old mother), WB05 (overwork — McDonald's, work-related exhaustion + sleep deprivation), WB04/WB07 (parental work + family caregiving — but those are CRISIS not BURNOUT per the WB design). Four named buckets, three with WB anchors.
- Fragility: the list collapses into the WB02/WB05 design. Burnout from causes outside this list (e.g., grief-related, chronic-illness-related, academic-overload, social isolation) is structurally underweighted. Also: the four labels overlap (overwork ⊂ exhaustion ⊂ sleep deprivation as a sequence); they're not distinct mechanisms but variant phrasings of the WB05 phenomenon.

**B3. Identity-disclosure enumeration.** `"a disability (ADHD, dyslexia, autism), neurodivergent identity, race, religion, immigration status, sexuality, or language background"` (WCS lines 1724–1726; UNIFIED_BINARY_NARROW lines 307–309).
- The disability sub-enumeration `ADHD, dyslexia, autism` is the most fragile sub-list. None of the 46 corpus essays disclose dyslexia or autism explicitly; S026 references brother Malik's ADHD; S029 reads as a neurodivergent writer but doesn't name a diagnosis. The parenthetical reads as a hedge against three specific disability disclosures the prompt-author anticipated but the corpus does not actually contain.
- The outer enumeration "race, religion, immigration status, sexuality, or language background" — maps onto S001+S005+S024+S032 (immigration), S023+S024+S032 (language background), all the ES students (race), S006 / S014 / S023 (mixed). No corpus essay foregrounds sexuality; no corpus essay foregrounds religion in an identity-disclosure register (WB06 mentions mosque as material site, not identity). Two of the seven enumerated categories have no corpus referent — appears corpus-tuned against a *hypothetical* identity-disclosure space.
- Fragility: an unenumerated identity disclosure (citizenship status that doesn't read as "immigration," class background, regional/cultural identity, generational status) is not on the list. The rule depends on completeness.

**B4. AAVE / multilingual / neurodivergent register enumeration.** `"AAVE, multilingual mixing, nonstandard English, and neurodivergent writing patterns (fragmented, nonlinear, associative)"` (WCS lines 1719–1721; UNIFIED_BINARY_NARROW lines 298–300; near-identical text in genob lines 504–506).
- Maps onto S022 (AAVE register, per master log iteration history), S001+S005+S023+S024+S032 (multilingual/L2 syntax/ESL), S029 (neurodivergent writing — explicitly: "neurodivergent writing style"). The three parenthetical neurodivergent descriptors (fragmented, nonlinear, associative) appear to be a calibration against S029's specific style.
- Fragility: as in the example shape from June's brief — this is reaching for a structural feature (linguistic register variation) by enumerating specific dialects/styles. A future corpus with a non-enumerated variety (Spanglish? Hawaiian Creole English? AAE features specific to a region not seen in S022?) falls outside the rule. Also: "nonstandard English" is its own category, which both subsumes and competes with "AAVE" and "multilingual mixing" — the list is not orthogonal.

**B5. "Mosque, food bank, extended family" enumeration.** Already in A8 above. Belongs equally in B: it's enumerative-looking-like-structural. The structural feature would be "community-based resource use as a sign of, not a relief from, material need." The prompt names instances instead.

**B6. Worked-examples sequence (a/b/c).** UNIFIED_BINARY_NARROW lines 360–375 (also in WCS 1808–1823).
- The three worked examples are an enumeration: (a) productivity-culture two-jobs-tired = topic-adjacency CLEAR; (b) literary theme + food disclosure = CONCERN; (c) generic third-person rhetorical = CLEAR. They function as anchors against three specific failure modes the prompt-author anticipated.
- Fragility: examples-as-rules. The model is told "*this shape* is CLEAR" rather than "*this principle* applies, here is an example." If a fourth shape arises (e.g., procedural writing + identity disclosure + brief material mention), the model has no fourth example and must extrapolate.

**B7. WORK-SCHEDULE / SLEEP-LOSS / CAREGIVING enumerated as the only BURNOUT signals.** `"the student's OWN MATERIAL CONDITIONS (their work schedule, their sleep loss, their caregiving duties) are breaking through and limiting their capacity"` (WCS 1706–1708; UNIFIED_BINARY_NARROW lines 283–285).
- Three explicit instances. Maps onto WB02 (caregiving), WB05 (work schedule + sleep loss). Two corpus anchors.
- Fragility: limits BURNOUT to material-labor causes. A student depleted by emotional caregiving without "duties" framing, by chronic illness fatigue, by trauma response — falls outside the enumerated set.

**B8. Topic-adjacency theme enumeration.** `"rest, self-care, productivity, exhaustion, overwork, labor as themes ... violence, trauma, illness, displacement, or loss"` (WCS lines 1770–1776; **note this block is REMOVED from UNIFIED_BINARY_NARROW** — it's a WCS-only block, retained in `BINARY_REASONING_SYSTEM` because `BINARY_REASONING_SYSTEM` is WCS verbatim except for schema).
- Eleven enumerated themes across two clauses. Maps to specific historical course themes — labor (productivity-culture worked example A1); ethnic-studies displacement (A7); the WB-corpus design topics broadly. Reads as a list of "topics we've calibrated for."
- Fragility: a course on, say, mental health, addiction, environmental crisis, or political violence is not on the list. The rule depends on which themes the calibration anticipated.

**B9. "Other concerns" hedge in unified-binary-broad.** `"This list is not exhaustive — other present-tense personal circumstances beyond the assignment scope that warrant attention also apply."` (UNIFIED_BINARY_BROAD lines 437–440.)
- The hedge is the giveaway: the prompt-author knows the enumeration is incomplete. This is the narrow/broad split — narrow enumerates as definitional; broad enumerates as illustrative. Both ride on the same five categories; broad just adds an "etc."
- Fragility: this is a meta-fragility. The broad version is calibration against the awareness that the narrow list is fragile, but it does not name what's outside.

---

## 4-Axis (FOUR_AXIS_REASONING_SYSTEM + UNIFIED_4AXIS_BASE_SYSTEM + supersedes/single-sentence blocks)

`FOUR_AXIS_REASONING_SYSTEM` is a compressed paraphrase of `WELLBEING_CLASSIFIER_SYSTEM` minus several long blocks (topic-adjacency, default-to-not-flag, identity-navigation-fatigue, worked-examples, procedural-writing tail). `UNIFIED_4AXIS_BASE_SYSTEM` is the inverse: WCS with the supersedes + single-sentence + tiebreaker blocks extracted. Together, the 4-axis substrate inherits all the binary A-items that survive the extraction (i.e., most of them).

### A. Direct example-to-essay matches

**A10. `"a family member's exhaustion or a parent's overwork is NOT evidence of BURNOUT — the depletion must be the student's own"`** (FOUR_AXIS_REASONING_SYSTEM lines 152–155; same in WCS lines 1708–1710 and UNIFIED_4AXIS_BASE.)
- Direct map to **S026** (DeShawn, brother Malik's story, mother's burnout — per June's note: "many of the flags raised on the student frame the rational as DeShawn taking on caregiving responsibilities. Not only is this not indicated in the essay..."). Also S020 (father's electric bill, family material conditions).
- Fragility: this guardrail exists specifically because S026 / S020 were getting misclassified. The structural feature is "family member's situation as analytical object vs. own state" — but the prompt enumerates "a family member's exhaustion or a parent's overwork" as the failure mode. Other family-member-as-analytical-object cases that don't fit "exhaustion/overwork" (e.g., S004's SE Asian mother's discrimination history; S005's grandmother's Guinea→France trajectory) fall outside the cue but raise the same inferential risk.

**A11. `"a student who writes passionately about painful experiences and reflects on the process ('this is what I needed to write') is deeply engaged, not depleted"`** (FOUR_AXIS_REASONING_SYSTEM lines 156–159; WCS lines 1711–1714; UNIFIED_4AXIS_BASE.)
- The parenthetical "'this is what I needed to write'" — appears corpus-tuned; no clear corpus match found. Could be a generalization across S020 ("Im not saying racism isnt real" + hyperbolic disclosure) or WB04 ("I dont know if Im supposed to write about this but I couldnt write about anything else") — the latter is closer. But WB04's framing is more crisis-anchored, and the example is being used here to *clear* a student, not to flag one.
- Fragility: if calibrated against WB04 specifically, the rule is doing double duty (the same case is CRISIS under "domestic abuse disclosure" and the prompt is using a paraphrase of its framing language to instruct against BURNOUT misclassification). That's coherent but fragile — the same student is doing two opposite jobs for the prompt.

**A12. Same A4 (trailing off mid-sentence) — INHERITED in UNIFIED_4AXIS_BASE_SYSTEM.** Note: this language is NOT in FOUR_AXIS_REASONING_SYSTEM (the compressed version), but IS in UNIFIED_4AXIS_BASE_SYSTEM. The two 4-axis substrates differ on this S002 cue.

**A13. Same A8/A9 (mosque/food bank/extended family + "student reports family food insecurity") — INHERITED in UNIFIED_4AXIS_BASE_SYSTEM.** Compressed FOUR_AXIS_REASONING_SYSTEM does NOT contain the MINIMIZED DISCLOSURE block (compare line 198 — schema follows the worked-examples-less version). So the WB11/WB12/WB13 calibration is present in unified-4axis but absent in the reasoning variant. This is an internal inconsistency the audit surfaces but does not propose resolving.

**A14. UNIFIED_4AXIS_SUPERSEDES_BLOCK** — `"CRISIS supersedes ENGAGED: If a student discloses domestic violence, housing loss, food insecurity, or immigration enforcement threat — even while maintaining strong analytical engagement..."` (WCS 1741–1746).
- The supersedes rule's *examples* (DV, housing, food, immigration) is the WB-corpus enumeration. Per master log Issues 8–9: the supersedes block is the formal rule the WB11/WB12/WB13/WB04 design tests. Direct corpus-tuning.
- Fragility: the supersedes rule names four categories. A CRISIS-level disclosure outside the four (medical emergency, recent loss/grief — which is named in the CRISIS definition but NOT named in the supersedes block) is structurally under-protected. The supersedes block's enumeration is narrower than the CRISIS definition's.

### B. Name-all-the-things passages

**B10. CRISIS / BURNOUT / ENGAGED enumerations.** All B1–B7 items above apply identically to the 4-axis substrate (the category definitions are textually shared or near-textually-shared with the binary substrate).

**B11. Confidence scale enumeration.** `"0.9+ only when the evidence is direct and unambiguous; 0.65-0.85 when signal is implicit or could be read either way; 0.5-0.65 when two categories are plausibly correct"` (FOUR_AXIS_REASONING_SYSTEM lines 195–197).
- Three numerically-banded cases. Appears corpus-tuned against the flat-0.95 calibration artifact described in the prompt comment lines 138–141 ("Designed to test whether constrained output (signal only, 150 tokens) is the cause of flat 0.95 confidence").
- Fragility: calibrates confidence reporting against a single historical model behavior (flat 0.95 on Test N). If model state changes, the bands lose their reference point. Not a corpus-to-essay match but a model-history match — same shape of corpus-tuning, different corpus.

**B12. Reasoning-field instruction enumeration.** `"reasoning: 2-3 sentences working through the evidence — explicitly note if the signal is implicit, third-party, or could be course material vs. personal disclosure"` (FOUR_AXIS_REASONING_SYSTEM lines 190–192).
- Three named alternatives (implicit / third-party / course-material vs personal). Each maps onto a corpus failure mode: implicit = WB02/WB05 burnout signals; third-party = S026 (Malik), S020 (DeShawn's father), S004 (mother), S005 (grandmother); course-material vs personal = S022, S023, S024, S028.
- Fragility: the three enumerated rationale-axes ARE the three corpus failure modes the prompt is calibrated against. The model is being told what kinds of reasoning to surface — and those kinds correspond to the corpus's known disambiguation cases.

**B13. Identity-disclosure enumeration in the 4-axis compressed form.** Same as B3 but slightly shorter: `"a disability (ADHD, dyslexia, autism), neurodivergent identity, race, religion, immigration status, sexuality, or language background"` (FOUR_AXIS_REASONING_SYSTEM lines 168–171).
- Same fragility surface as B3 — three disability instances, seven identity categories. The disability sub-list still lacks a corpus anchor for autism/dyslexia. Inherited verbatim from the binary substrate.

**B14. `"exhaustion that cuts off thought, lost sleep named directly, food or housing instability, fear for safety, caregiving burden limiting capacity"`** (FOUR_AXIS_REASONING_SYSTEM lines 173–175).
- Five enumerated wellbeing-signal-evidence types. Each maps to a WB case: cuts off thought = WB02 ("cuts off mid-thought to go pick up daughter") + WB05; lost sleep named directly = WB02 + WB05; food/housing instability = WB03/WB06/WB11/WB12/WB13; fear for safety = WB01/WB04/WB09; caregiving burden = WB02.
- This is the most direct corpus-to-rule mapping in the 4-axis prompt. Five enumerated rules, each with one or more WB corpus anchors. The list IS the WB taxonomy at higher resolution than B1/B2.
- Fragility: a signal that doesn't fit one of the five (e.g., "I can't focus" without naming sleep; observed-by-syntax burnout — fragmented writing — without a verbal cue) falls outside the rule. The rule is anchored to *self-naming* of material conditions; the corpus's WB cases all self-name.

---

## Genob (UNIFIED_GENOB_BASE_SYSTEM + OBSERVATION_PROMPT + supersedes/single-sentence blocks)

The genob substrate is a translation of the binary substrate from classification register into observation register. Most A and B items above have a genob analog. Per June's brief, I expected minimal corpus-specific references; what I found is that genob inherits the same enumerations and worked examples nearly verbatim (lines 489–582 of run_4axis_full_corpus_test.py) — they are simply re-cast as "describe / observe" instead of "classify / flag." This is worth flagging.

### A. Direct example-to-essay matches

**A15. `"such as domestic violence, housing loss, food insecurity, immigration enforcement threat, recent loss/grief, burnout, exhaustion, overwork, caregiving burden, sleep deprivation, or other concerns"`** (UNIFIED_GENOB_BASE_SYSTEM lines 497–500).
- Same five+five enumeration as binary B1+B2, collapsed into one comma-list. Same corpus anchors (WB01–WB13).
- Fragility: same as binary. Adding "or other concerns" — the broad-version hedge — does not name what's outside.

**A16. UNIFIED_GENOB_BASE worked example (a)** — `"'I work two jobs and I'm tired all the time, which is exactly what the reading is describing — capitalism extracts more than it gives back.'"` (lines 552–557).
- Identical to A1. Same corpus rhyme (WB05 / S020).

**A17. UNIFIED_GENOB_BASE worked example (b)** — `"a four-page analytical essay on a literary theme and one sentence reads: 'There hasn't been food at home this week.'"` (lines 559–562).
- Identical to A2. Same corpus mirror (WB12).

**A18. UNIFIED_GENOB_BASE worked example (c)** — `"'People are exhausted. The system is grinding everyone down. Burnout is everywhere.'"` (lines 564–568).
- Mirrors B6 (c). No direct corpus essay — appears to anticipate WB14-shape submissions (impersonal analysis of community wealth frameworks; the "no false positive on community-wealth analysis" control per master log line 697). The example reads as the WB14 control case stated as a worked example.

**A19. OBSERVATION_PROMPT — `"Ingrid connected dehumanization to her grandmother's experience in agricultural work, and DeShawn linked racial profiling to the structural analysis from the reading."`** (prompts.py lines 1582–1584, in `OBSERVATION_SYNTHESIS_PROMPT`.)
- **Direct named-student examples in a prompt.** "Ingrid" maps to S024 (Ingrid Vasquez; mother's undocumented Honduran factory worker story — though the prompt says "grandmother's experience in agricultural work," which doesn't match S024's actual content; closer to S005 grandmother Guinea→France or S023 grandmother Esperanza). "DeShawn" maps to S020 (DeShawn) or S026 (DeShawn-coded brother-Malik student — corpus_review_state doesn't name the student, but S026 has the Black-boys-school-discipline content).
- This is the most direct A-item in any audited prompt: actual student first names appear in the prompt, treated as a worked example. Even if the example is paraphrased rather than literal, the names are corpus-resident.
- **Already in master log** as part of the genob audit register, but worth surfacing for completeness given the audit's specific corpus-tuning frame. This is example-to-essay match at the proper-noun level.
- Fragility: any class taught with this prompt and a student named Ingrid or DeShawn will encounter literal proper-noun matching. Also: the example's grandmother/agricultural-work content is plausibly synthesized rather than corpus-resident, which is its own fragility (the model is being shown a synthetic "good example" tagged with real student names).

**A20. OBSERVATION_PROMPT — Structural power moves enumeration with specific labels.** Lines 1516–1528 of prompts.py:
> "Tone policing... abstract liberalism... Settler/colonial innocence... Progress narratives... Objectivity claims... Deflection to individual solutions... Meritocracy framing"
- Maps onto S015 ("essentializing"), S018 (abstract liberalism — "individual-level colorblindness... categories and labels as divisive"), S025 (tone policing — "deflects from content by calling for less emotional engagement; frames anger as an obstacle").
- Direct corpus tuning: the three named power-move types with corpus anchors (tone policing, abstract liberalism, settler innocence) are the three power-move cases in the corpus. The other four (progress narratives, objectivity claims, deflection to individual solutions, meritocracy framing) have no clear corpus match.
- Fragility: a future corpus with a power move not on the list (e.g., respectability politics, model-minority framing, "I have a Black friend"–style exceptionalism, gender-neutralizing-as-feminism) is not enumerated. The model is told to name "the mechanism directly" using the listed terms — the list is the available vocabulary.

**A21. OBSERVATION_PROMPT — `"When a student's current work matches the level of earlier submissions after a dip, name the dip as temporary and the return as continuity — not as surprising recovery."`** (lines 1495–1497).
- **Already in master log** (P8/P9 audit, recovery-vs-development asymmetry). Direct calibration against the 2026-04-02 audit-baseline finding that marked students (Marisol, Kayla, Jesse) get "recovery" framing while control Noah gets "natural progression." The instruction is meant to break that asymmetry by mandating continuity-framing.
- Surfacing for completeness; master log treats this as a known calibration source.

### B. Name-all-the-things passages

**B15. Genob inherits B1/B2/B3/B4/B7/B8** — the same enumerations as binary, in observation register rather than classification register. Same fragility surface.

**B16. OBSERVATION_PROMPT power-move list** — already in A20 above; belongs equally in B. Seven enumerated patterns. Three corpus-anchored, four not. The list is the available vocabulary for naming structural power moves — it's both a worked enumeration and a constraint on what the model can name.

**B17. OBSERVATION_PROMPT — `"What is this student reaching for intellectually? ... What is their emotional relationship to the material? ... Is there anything about their engagement, capacity, or circumstances..."`** (lines 1481–1486).
- Three enumerated dimensions of observation. Per master log P8 audit: "What is their emotional relationship to the material?" is the elicitation line that generates the recovery-vs-development asymmetry on marked students. Direct calibration against the audit's findings.
- Fragility: the three dimensions privilege a particular shape of observation (intellectual / emotional / wellbeing). A student whose work is best described along a different dimension (political, aesthetic, methodological) is observation-shaped by the prompt's three-way menu.

**B18. OBSERVATION_SYSTEM_PROMPT — `"anger about injustice, grief about family experiences, frustration with systems"`** (prompts.py lines 1456–1457).
- Three enumerated examples of "engagement, not distress." Maps onto S022 (anger about redlining), S005/S023/S024/S030 (grief / family experiences), S018/S025 (frustration with systems — but those are power moves in the corpus design, not engagement).
- Fragility: per master log P8 finding, this exact line is a "reframing instruction (treat as engagement, not distress)" — the corpus tuning is intentional. Surfacing for completeness given the audit frame.

**B19. OBSERVATION_SYSTEM_PROMPT — `"topic-comment structures, dropped subjects, discourse markers from their home language"`** (prompts.py lines 1451–1452).
- Three enumerated L2/multilingual syntactic features. Maps onto S001 (Senegalese ESL), S005 (Guinea/France grandmother — French syntax), S023+S024 (Spanish-language ESL), S032 (Hmong/Vietnamese translation).
- Fragility: three named features in a much broader space of bilingual syntactic phenomena. A multilingual student whose "intellectual stretching" surfaces through other features (calque, code-switching at the lexical level, register-shifting, prosodic transfer into writing rhythm) is unenumerated. The list is calibrated against a specific linguistic-research vocabulary; novel cases need to be re-described.

---

## Notes / uncertainties

1. **A3 ("It was fine though" after disclosing they had nothing at home)** — strongest "appears corpus-tuned but no corpus match" finding. This phrasing is doing work that anticipates a corpus addition or originates from a different essay seen in development. June may want to trace the calibration source.

2. **A11 ("'this is what I needed to write'")** — possibly maps to WB04, but the same essay is used to *clear* a student against BURNOUT here, while WB04 is the CRISIS exemplar for domestic-abuse disclosure. The same case anchoring two opposite guardrails is internally coherent but fragile.

3. **Internal inconsistency between FOUR_AXIS_REASONING_SYSTEM and UNIFIED_4AXIS_BASE_SYSTEM** on the MINIMIZED DISCLOSURE / COMMUNITY RESILIENCE block: present in unified-4axis, absent in the reasoning variant. The two 4-axis substrates encode different corpus-tuning surfaces — methodologically worth flagging in the paper's "what we tested" framing.

4. **OBSERVATION_PROMPT proper-noun examples** ("Ingrid," "DeShawn") — most direct A-item across all three prompts; in the SYNTHESIS prompt rather than the per-student observation prompt, so the audit's scope question is whether this counts. The synthesis prompt sees observations across the class, so its corpus-tuned examples shape the class-level read. Worth surfacing.

5. **Topic-adjacency block (WCS lines 1769–1783)** is present in `BINARY_REASONING_SYSTEM` but absent from `FOUR_AXIS_REASONING_SYSTEM` and from `UNIFIED_4AXIS_BASE_SYSTEM`. This is an asymmetry between the binary and 4-axis comparison conditions — both nominally "the same equity guards" but actually differing on topic-adjacency calibration. May affect how format-effect claims are scoped.

6. **WB14 (control case for community resilience)** has no `expected_*` field in `corpus_review_state.json`, but is the "no false positive" anchor per master log line 697. The genob worked example (c) appears calibrated against it. Worth noting that WB14 is doing latent work in the calibration surface even where the corpus doesn't explicitly mark it.

7. **Per master log §iteration history**: the WB11–WB14 block (community resilience) was added 2026-04-01 specifically because WB06 surfaced the community-framing-read-as-less-severe pattern. The MINIMIZED DISCLOSURE / COMMUNITY RESILIENCE block and the "mosque, food bank, extended family" enumeration are the prompt-side response to that finding. This calibration history is settled in the master log; the corpus-tuning shape it produces is what this audit surfaces.

8. **Power-move enumeration in OBSERVATION_PROMPT** is the single passage most likely to need restructuring under the audit's frame — three of seven enumerated patterns have corpus anchors; four don't. The four-without-anchors are presumably calibrated against pedagogical-research vocabulary rather than the corpus, which is a different calibration source than the rest of the audit's findings. Worth naming as such.

9. **What I did NOT audit:** `WELLBEING_PRESCAN_SYSTEM` / `_PROMPT` (prompts.py lines 1671–1695) — these are the pass-0 signal-extraction prompts. They contain the same corpus-anchored enumeration ("food insecurity, housing instability, sleep deprivation from work or caregiving, family crisis, immigration enforcement threat, domestic violence, recent loss, or health emergency") plus a near-direct A-match: `"'it was fine though,' 'I managed,' 'I don't know if this is relevant.'"` The last phrase maps closely to WB04's `"I dont know if Im supposed to write about this..."`. If the prescan is in scope, this is an A-item; the audit excluded it because the brief named the four classifier prompts specifically.
