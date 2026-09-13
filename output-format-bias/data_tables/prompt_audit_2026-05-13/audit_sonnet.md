# Prompt Fragility Audit — Sonnet pass — 2026-05-13

**Scope:** UNIFIED v2 prompts from `run_4axis_full_corpus_test.py` + base prompts from `prompts.py`.
**Corpus reference:** `data_tables/corpus_overview/corpus_review_state.json` (46 students: S001–S032, WB01–WB14).
**Not re-litigated:** Items already in `MASTER_RESPONSE_LOG_2026-05-11.md`.

The 4-axis base (`UNIFIED_4AXIS_BASE_SYSTEM`) is derived from `WELLBEING_CLASSIFIER_SYSTEM` by stripping the supersedes, single-sentence, and tiebreaker blocks. The `BINARY_REASONING_SYSTEM` is `WELLBEING_CLASSIFIER_SYSTEM` with only the JSON schema tail modified. Both therefore inherit the full body of `WELLBEING_CLASSIFIER_SYSTEM`. That shared inheritance is load-bearing for the fragility analysis: every corpus-tuned passage in `WELLBEING_CLASSIFIER_SYSTEM` propagates into both the binary and the 4-axis base unless explicitly stripped.

---

## Binary (BINARY_REASONING_SYSTEM + WELLBEING_CLASSIFIER_PROMPT + unified blocks)

`BINARY_REASONING_SYSTEM` = `WELLBEING_CLASSIFIER_SYSTEM` with only the schema tail swapped.
`UNIFIED_BINARY_NARROW_BASE_SYSTEM` and `UNIFIED_BINARY_BROAD_BASE_SYSTEM` are the v2 binary substrates audited below.

### A. Direct example-to-essay matches

**A-B1. "a student who writes passionately about painful experiences and reflects on the process ('this is what I needed to write') is deeply engaged, not depleted"**

Source: `WELLBEING_CLASSIFIER_SYSTEM` / `UNIFIED_BINARY_NARROW_BASE_SYSTEM` BURNOUT definition / CONCERN definition (b).
Corpus match: **WB07** — the student who writes a polished analytical essay and then breaks into personal overwhelm about her mother's sexual assault, closing with "Sorry I know this isnt what you asked for but I cant think about anything else right now." The phrase 'this is what I needed to write' is the guard against false-positive BURNOUT for students who write with emotional necessity. WB07 is precisely the student this phrasing is modeling: someone whose writing carries emotional weight that COULD look like depletion. The phrasing anchors the guard to a subjective report of process catharsis rather than to the material-conditions distinction the prompt elsewhere uses. Fragility: the guard as written would protect WB07 from false BURNOUT flagging, but WB07 should be flagged — as CRISIS, not BURNOUT. If a model activates this guard on WB07 (reads her closing apology as "this is what I needed to write" framing), it could suppress the crisis signal. The phrasing is corpus-tuned to a CLEAR/ENGAGED case but does not cleanly separate from the CRISIS cases.

---

**A-B2. "exhaustion that cuts off thought (trailing off mid-sentence, incomplete submissions that end abruptly)"**

Source: `WELLBEING_CLASSIFIER_SYSTEM` / `UNIFIED_BINARY_NARROW_BASE_SYSTEM` IDENTITY DISCLOSURE section.
Corpus match: **S002** — the case that cuts off mid-sentence ("its late and"). The parenthetical description of the signal is essentially a one-case definition: it matches S002's exact presentation. The `notes_S002` field confirms this was the originally imagined burnout case. This is a direct example-to-essay calibration: the ellipsis signal is described in terms that fit S002 and very few other canonical cases. Fragility: this phrasing teaches the model to weight mid-sentence cutoffs as burnout signals. In a different corpus where mid-sentence cutoffs reflect connectivity loss, device issues, or copy-paste errors, this calibration may produce false positives. Also already flagged in the master log as an edge case with ambiguous true label — already in master log, surfacing for completeness.

---

**A-B3. "a student who names their disability and says academic writing is hard, or that explaining their identity is exhausting, is describing their relationship to the academic institution — this is CLEAR / this is ENGAGED"**

Source: `WELLBEING_CLASSIFIER_SYSTEM` / `UNIFIED_BINARY_NARROW_BASE_SYSTEM` IDENTITY DISCLOSURE section.
Corpus match: **S029** — explicitly asks to be assessed on comprehension not structure, expresses discomfort with the assignment format. **S016** — mentions being "more of a talker than a writer" (format constraint naming). The phrasing "academic writing is hard" or "explaining their identity is exhausting" describes these exact cases. The guard protects them from false-positive flagging. Fragility: the phrasing works because S029 and S016 are in the corpus; it may not generalize cleanly to cases where a student names disability AND material conditions in the same sentence. The parenthetical examples define the guard very narrowly around identity-academic-difficulty, not identity-plus-burden.

---

**A-B4. "A student describing a family member's exhaustion or a parent's overwork is NOT evidence of BURNOUT / NOT evidence of CONCERN"**

Source: `WELLBEING_CLASSIFIER_SYSTEM` / `UNIFIED_BINARY_NARROW_BASE_SYSTEM` BURNOUT / CONCERN definition.
Corpus match: **S026** (brother Malik's school discipline + single working mom) and **S020** (family situation, strawman reading, "He cant pay the electric bill half the time"). The `notes_S026` annotation explicitly flags this: "the burnout is not the student's own." The `notes_S020` annotation marks it an edge case. The prompt guard is directly calibrated to suppress the S026/S020 false-positive pattern. Fragility: the guard is appropriate for S026 but the `notes_S020` annotation suggests S020 is genuinely ambiguous — the guard may be too blunt for cases where family financial distress bleeds into the student's own situation.

---

**A-B5. Worked example (a): "I work two jobs and I'm tired all the time, which is exactly what the reading is describing — capitalism extracts more than it gives back"**

Source: `WELLBEING_CLASSIFIER_SYSTEM` / `UNIFIED_GENOB_BASE_SYSTEM` WORKED EXAMPLES.
Corpus match: No exact corpus match, but the phrasing is shaped around the type that appears in **S022** (legitimate anger about redlining, substantively engaged) and the WB cases. The "two jobs" example is calibrated to not trigger BURNOUT because the student is drawing on their own labor experience AS COURSE MATERIAL on a labor-themed assignment. The specific framing ("capitalism extracts more than it gives back") is synthetic but encodes the exact analytic move the corpus tests. Fragility: this example anchors the CLEAR/ENGAGED determination to topic-adjacency — the example only holds if the assignment IS about labor. If a student writes the same thing on an intersectionality or immigration assignment where the topic is not labor, the example's logic does not transfer. The worked example is topic-conditional in ways the prompt does not state.

---

**A-B6. Worked example (b): "There hasn't been food at home this week"**

Source: `WELLBEING_CLASSIFIER_SYSTEM` / `UNIFIED_BINARY_NARROW_BASE_SYSTEM` / `UNIFIED_GENOB_BASE_SYSTEM` WORKED EXAMPLES.
Corpus match: **WB06** ("we are eating at the mosque more than at home") and **WB12** (Mom laid off, eating at church nightly). The synthetic example phrase closely mirrors the WB06 pattern: food insecurity named matter-of-factly inside an analytical essay, without it structuring the submission. The "one sentence" framing also encodes the WB11/WB12/WB13 pattern where material conditions appear briefly before the student returns to analysis. Fragility: the example teaches food insecurity recognition by analogy to a specific phrasing. A student who discloses food insecurity through avoidance language ("we haven't had much at home lately") or euphemism ("things have been tough with groceries") may not activate the same pattern. The example is more of an anchor than a structural description.

---

**A-B7. "referencing community resources (mosque, food bank, extended family) as the source of basic needs"**

Source: `WELLBEING_CLASSIFIER_SYSTEM` / `UNIFIED_BINARY_NARROW_BASE_SYSTEM` / `UNIFIED_GENOB_BASE_SYSTEM` MINIMIZED DISCLOSURE AND COMMUNITY RESILIENCE section.
Corpus match: **WB06** (mosque), **WB11** (tribal food distribution), **WB12** (church food pantries, church paid electric bill), **WB13** (susu group). These four cases are the explicit corpus design for the resilience-framing guard. The mosque, food bank, and extended-family examples are near-verbatim descriptions of WB06, WB12/WB13 patterns. Fragility: the enumeration works for these cases precisely because the corpus includes them. A student relying on a mutual-aid network not named in the list (a neighborhood "blessing bags" network, an app-based food redistribution, a school's informal pantry) may not activate the same recognition. The guard names three institutional forms rather than describing the structural feature (reliance on non-household food/housing sources as a crisis signal regardless of the source's form).

---

**A-B8. "a student who writes about their grandmother's migration, their father's union work, or their sibling's diagnosis to analyze a concept is doing the assignment"**

Source: `WELLBEING_CLASSIFIER_SYSTEM` / `UNIFIED_BINARY_NARROW_BASE_SYSTEM` / `UNIFIED_GENOB_BASE_SYSTEM` PERSONAL EXPERIENCE AS COURSE MATERIAL section.
Corpus matches: **S001** (grandmother's experience in Senegal), **S004** (mother's SE Asian immigrant experience), **S005** (grandmother Guinea→France trajectory), **S023** ("grandmother Esperanza's story"), **S024** (mother's undocumented Honduran factory worker story), **S026** (brother Malik), **S028** ("mother 'never said the word intersectionality but she showed me what it meant'"), **S030** (great-aunt growing up Black in Mississippi). The "grandmother's migration" phrase specifically echoes S001, S005, and S023. "Father's union work" is a synthetic example but names the exact analytic register (using family labor history for course concepts) that S024 and S028 demonstrate. "Sibling's diagnosis" anticipates S026 (though S026 names a brother's school experience, not diagnosis). This passage enumerates almost the entire family-history-as-course-material sub-group of the corpus. Fragility: the enumerated examples may train models on this exact corpus's family-history patterns. In a corpus where students use community institution experience (church deacons, neighborhood advocates, mutual aid organizers) rather than family narratives, the examples may not transfer. The structural feature is "third-party experience used analytically" — the examples collapse it to a particular family-narrative form.

---

**A-B9. Identity-navigation fatigue guard: "tired of justifying their existence... navigating institutional expectations around their race, disability, language, or gender is draining"**

Source: `WELLBEING_CLASSIFIER_SYSTEM` / `UNIFIED_BINARY_NARROW_BASE_SYSTEM` IDENTITY-NAVIGATION FATIGUE section.
Corpus match: **S016** ("I'm... more of a talker than a writer" — format constraint naming as fatigue), **S029** (discomfort with assignment format, asks to be assessed on comprehension not structure). These are the clearest corpus exemplars of the identity-navigation fatigue pattern. The phrasing "navigating institutional expectations" is generic enough to work across cases, but "tired of justifying their existence" is emotionally specific in ways that point at the S029 pattern. Fragility: the guard as stated protects students who name fatigue abstractly. A student who describes the drain more concretely ("I spend so much energy in office hours explaining what I mean that I have nothing left for the paper itself") is describing both identity navigation AND possible capacity depletion — the guard may suppress a real signal in that case.

---

**A-B10. "In procedural, technical, or short-response writing, students rarely mention personal circumstances at all — the genre does not invite disclosure. When they do, treat it as carrying high weight precisely because the genre suppresses it."**

Source: `WELLBEING_CLASSIFIER_SYSTEM` / `UNIFIED_BINARY_NARROW_BASE_SYSTEM`.
Corpus match: **S031** (44-word submission, "idk what else to say about it" — disengagement, possible burnout). The `notes_S031` annotation flags this as edge case / possible burnout signal. The short-response instruction is calibrated to cases like S031 where brevity itself is the signal. Fragility: this passage instructs the model to weight personal disclosures in short writing very highly. In a corpus with more genuinely brief assignment formats (discussion board posts, exit tickets), the same instruction would produce over-flagging.

---

**A-B11. UNIFIED_BINARY_SINGLE_SENTENCE_BLOCK: "'It was fine though' after disclosing they had nothing at home is not reassurance — it is institutional code-switching."**

Source: `UNIFIED_BINARY_SINGLE_SENTENCE_BLOCK` (appended block in binary v2 variants).
Corpus match: **WB06** (food insecurity named matter-of-factly without distress), **WB11/WB12** (resilience framing around food), **WB03** (lost apartment, apologizes for brevity). The specific phrasing "It was fine though" after a disclosure of nothing at home encodes a specific coping/minimization pattern seen in WB11/WB12 (tribal distribution twice a month, eating at church). The phrase "institutional code-switching" names a structural mechanism, but the example anchoring it is one specific phrasing. Fragility: the code-switching example is tuned to food-insecurity disclosures. The same institutional suppression pattern appears in housing (WB03), safety (WB01), and grief (WB08) cases — but the example doesn't model those. A model might weight this block's logic most for food-insecurity cases and less for the other crisis types.

---

**A-B12. UNIFIED_BINARY_SUPERSEDES_BLOCK: "domestic violence, housing loss, food insecurity, or immigration enforcement threat — even while maintaining strong analytical engagement"**

Source: `UNIFIED_BINARY_SUPERSEDES_BLOCK`.
Corpus match: **WB04** (domestic abuse — stepfather controls mother's contacts), **WB03** (housing loss — lost apartment, at library), **WB06/WB11/WB12/WB13** (food insecurity), **WB01** (immigration enforcement threat — brother came home crying). The four-item enumeration of the supersedes clause names precisely the four CRISIS types that appear in the WB corpus. This is the closest thing to a direct inventory-of-corpus-cases in the prompt. The CRISIS supersedes clause was added, per comment context, because WB04 required it — the domestic abuse disclosure with strong analytical engagement needed explicit override. Fragility: the enumeration omits grief/loss (WB08 — cousin killed at traffic stop) and sexual violence as secondary (WB07 — mother's manager). Those cases may get lower override priority because they're not in the supersedes list. Note: WB08 expected_WB08 = CRISIS; if model relies on supersedes list as exhaustive, it could miss the grief/loss case in a borderline submission.

---

### B. Name-all-the-things passages

**B-B1. CRISIS definition enumeration: "domestic violence, housing loss, food insecurity, immigration enforcement threat, recent loss/grief"**

Source: `WELLBEING_CLASSIFIER_SYSTEM` (CRISIS definition) / `FOUR_AXIS_REASONING_SYSTEM` (CRISIS definition) / UNIFIED_BINARY_NARROW CONCERN definition.
This list enumerates the five CRISIS categories that appear in the WB corpus. The list is close to exhaustive for what was designed into the WB cases: WB01 (ICE), WB03/WB13 (housing), WB04 (DV), WB06/WB11/WB12 (food), WB08 (grief). WB07 (sexual assault of family member) is the only WB CRISIS case not cleanly named in this list. Fragility: the list trains the model to recognize these five types. A crisis type not in the list — medical emergency, legal threat other than immigration, eviction-in-progress distinct from "housing loss," academic suspension — may not activate crisis recognition at the same sensitivity. The structural feature "present-tense danger or instability" is described but then the enumeration narrows it.

---

**B-B2. BURNOUT definition enumeration: "exhaustion, overwork, caregiving burden, sleep deprivation"**

Source: `WELLBEING_CLASSIFIER_SYSTEM` / `FOUR_AXIS_REASONING_SYSTEM` / `UNIFIED_BINARY_NARROW_BASE_SYSTEM`.
Corpus coverage: WB02 (caregiving as 17-year-old mother), WB05 (McDonald's closing shift, sleep deprivation). The list names both BURNOUT corpus cases. Fragility: mental load without physical depletion signal, chronic illness management, medication side effects, academic probation anxiety — these are plausible burnout presentations not represented in the list. The structural feature "student's own capacity is depleted" is named but then anchored to four physical/material types.

---

**B-B3. Identity disclosure list: "disability (ADHD, dyslexia, autism), neurodivergent identity, race, religion, immigration status, sexuality, or language background"**

Source: `WELLBEING_CLASSIFIER_SYSTEM` / `UNIFIED_BINARY_NARROW_BASE_SYSTEM` / `UNIFIED_GENOB_BASE_SYSTEM` IDENTITY DISCLOSURE section.
This enumerates every identity category that appears in the corpus: ADHD/dyslexia/autism (S029), race (S007, S012, S016, S022, S028 throughout), religion (WB06, WB11 mosque/tribal), immigration status (S001, S004, S005, S024, WB01), sexuality (not prominently represented in reviewed cases), language background (S001, S032). The list functions as a checklist of the protected categories present in this corpus. Fragility: socioeconomic class is not listed as an identity disclosure category, but it appears in corpus submissions (S020, S031). An LLM parsing this list as exhaustive may flag class-related identity statements differently. Caste, for example, is also absent. The structural feature is "membership in a historically surveilled group" — the list enumerates the corpus's specific instantiations.

---

**B-B4. AAVE enumeration: "AAVE, multilingual mixing, nonstandard English, and neurodivergent writing patterns (fragmented, nonlinear, associative)"**

Source: `WELLBEING_CLASSIFIER_SYSTEM` / `FOUR_AXIS_REASONING_SYSTEM` / `UNIFIED_BINARY_NARROW_BASE_SYSTEM` ENGAGED / CLEAR definition.
Corpus coverage: AAVE → WB10 (legitimate anger, church community), S007 (Black girls discourse), S022 (Destiny, legitimate anger). Multilingual mixing → S001 (ESL, L2 syntax), S032 (Hmong/Vietnamese). Neurodivergent → S029 (fragmented). Nonstandard English → S002 (its late and), S031 (idk). Each term in the list corresponds to a documented corpus register. Fragility: this list enumerates the register varieties present in this corpus. A future corpus with Spanglish (present only minimally in S006), Indigenous language switching, or creole features may not activate the same protection — particularly if the model learned the phrasing as a checklist rather than as a principle. "VALID ACADEMIC REGISTERS" names the structural claim; the parenthetical enumeration domesticates it into this corpus's specific varieties.

---

**B-B5. TOPIC-ADJACENCY threshold paragraph: "when the assignment topic is itself burnout-related (rest, self-care, productivity, exhaustion, overwork, labor as themes)... when the assignment itself deals with violence, trauma, illness, displacement, or loss"**

Source: `WELLBEING_CLASSIFIER_SYSTEM` TOPIC-ADJACENCY section (in 4-axis base; stripped from unified binary v2 variants by block removal).
Note: this paragraph is NOT in `UNIFIED_BINARY_NARROW_BASE_SYSTEM` — it is only in `WELLBEING_CLASSIFIER_SYSTEM`, which is the basis for `BINARY_REASONING_SYSTEM` and the 4-axis base. The topic-adjacency list enumerates assignment themes that appear in the corpus context. The ethnic studies intersectionality assignment (the primary corpus assignment) deals with identity, discrimination, and systemic harm — it qualifies under "displacement, or loss" and "violence, trauma." The worked example (a) is explicitly set on a "productivity-culture assignment." Fragility: the list teaches the model to recognize topic-adjacency for these themes. An assignment on microeconomics, data literacy, or quantitative methods may not trigger the threshold even if a student writing on it discloses exhaustion — because those topics don't appear in the list.

---

**B-B6. DEFAULT TO NOT FLAGGING tiebreaker (present in `WELLBEING_CLASSIFIER_SYSTEM` / `BINARY_REASONING_SYSTEM`, stripped from unified v2 4-axis and binary substrates)**

Source: `WELLBEING_CLASSIFIER_SYSTEM`, starting with "DEFAULT TO NOT FLAGGING WHEN AMBIGUOUS."
This paragraph contains internal calibration designed to address the false-positive rate on the equity corpus (S001–S032), where emotional engagement with race/labor/immigration course material was being over-flagged. The explicit "False positives — flagging students who are doing the assignment as if they were in crisis — produce real harm: surveillance of marginalized students" phrasing encodes the political concern that emerged from corpus review. Fragility: this is broadly principled, not narrowly corpus-tuned, but it was written after the S001–S032 false-positive pattern was documented. The "surveillance of marginalized students" framing may produce under-sensitivity to genuine crisis signals in marginalized students' submissions — a model internalizing this framing might weight it toward "don't flag" even when the signal is real. Note: already partially addressed in master log Issue 3 discussion.

---

**B-B7. WORKED EXAMPLES (c): "People are exhausted. The system is grinding everyone down. Burnout is everywhere." — generic third-person rhetorical engagement**

Source: `WELLBEING_CLASSIFIER_SYSTEM` / `UNIFIED_BINARY_NARROW_BASE_SYSTEM` / `UNIFIED_GENOB_BASE_SYSTEM` WORKED EXAMPLES.
Corpus match: S022 (legitimate anger about redlining), S025 (tone policing, calls for less emotional engagement), WB10 (legitimate anger, church community). The third-person rhetorical engagement example is calibrated to protect against false-positive flagging on submissions that read as emotionally intense but are analytically grounded. This covers the S022/WB10 pattern. Fragility: the example uses burnout-as-course-topic phrasing ("Burnout is everywhere"). The structural feature is "third-person rhetorical generalization without own-state material conditions." A student who writes "Everyone in my family is exhausted" is ambiguous on this dimension — partial third-person but implicating the student's household. The example does not model that boundary case.

---

## 4-Axis (FOUR_AXIS_REASONING_SYSTEM + unified blocks)

`FOUR_AXIS_REASONING_SYSTEM` is a hand-authored system prompt (not derived from `WELLBEING_CLASSIFIER_SYSTEM`). The unified 4-axis base `UNIFIED_4AXIS_BASE_SYSTEM` is derived from `WELLBEING_CLASSIFIER_SYSTEM` by stripping the supersedes, single-sentence, and tiebreaker blocks.

Note: `FOUR_AXIS_REASONING_SYSTEM` (the older reasoning variant used in Test N/O/P runs) shares most of its body text with `WELLBEING_CLASSIFIER_SYSTEM`, with some parallel phrasing. Where the two differ, the corpus-tuning analysis applies to both. Items shared between `FOUR_AXIS_REASONING_SYSTEM` and `WELLBEING_CLASSIFIER_SYSTEM` are not duplicated here if already captured above.

### A. Direct example-to-essay matches

**A-4A1. `FOUR_AXIS_REASONING_SYSTEM`: "a student who writes passionately about painful experiences and reflects on the process ('this is what I needed to write') is deeply engaged, not depleted"**

Same text as in `WELLBEING_CLASSIFIER_SYSTEM`. Same corpus match as A-B1 (WB07). Not duplicating analysis. Already surfaced above.

---

**A-4A2. `FOUR_AXIS_REASONING_SYSTEM`: "AAVE, multilingual mixing, nonstandard English, and neurodivergent writing patterns (fragmented, nonlinear, associative) are VALID ACADEMIC REGISTERS"**

Same text as in `WELLBEING_CLASSIFIER_SYSTEM`. Same corpus match as B-B4. Already surfaced above.

---

**A-4A3. `FOUR_AXIS_REASONING_SYSTEM` BURNOUT definition: "A student describing a family member's exhaustion or a parent's overwork is NOT evidence of BURNOUT — the depletion must be the student's own."**

Same text as in `WELLBEING_CLASSIFIER_SYSTEM`. Same corpus match as A-B4. Already surfaced above.

---

**A-4A4. `UNIFIED_4AXIS_SUPERSEDES_BLOCK` (extracted from `WELLBEING_CLASSIFIER_SYSTEM`): "CRISIS supersedes ENGAGED: If a student discloses domestic violence, housing loss, food insecurity, or immigration enforcement threat..."**

This block is the verbatim extraction from `WELLBEING_CLASSIFIER_SYSTEM`. Same four-item enumeration as A-B12. Corpus matches: WB04, WB03, WB06/WB11/WB12/WB13, WB01. Same fragility analysis: grief/loss (WB08) and sexual violence secondary (WB07) not in the supersedes list. Already surfaced above.

---

**A-4A5. `UNIFIED_4AXIS_SINGLE_SENTENCE_BLOCK` (extracted from `WELLBEING_CLASSIFIER_SYSTEM`): "'It was fine though' after disclosing they had nothing at home is not reassurance — it is institutional code-switching."**

Same text as A-B11 above. Already surfaced above.

---

**A-4A6. `FOUR_AXIS_REASONING_SYSTEM` PERSONAL EXPERIENCE section: "a grandmother's migration, a father's labor"**

Text in `FOUR_AXIS_REASONING_SYSTEM`: "a student who writes about their grandmother's migration, their father's labor — are doing the assignment." This is a compressed version of the full grandmother/father/sibling enumeration in `WELLBEING_CLASSIFIER_SYSTEM`. Same corpus coverage as A-B8 (S001/S004/S005/S023/S024/S028/S030). The compression here drops the sibling example — slightly less corpus-enumerated than the full form.

---

**A-4A7. `FOUR_AXIS_REASONING_SYSTEM` MINIMIZED DISCLOSURE: "mosque, food bank, extended family"**

Same enumeration as A-B7. Same corpus matches: WB06, WB11, WB12, WB13. Already surfaced above.

---

### B. Name-all-the-things passages

**B-4B1. `FOUR_AXIS_REASONING_SYSTEM` CRISIS definition: "domestic violence, housing loss, food insecurity, immigration enforcement threat, recent loss/grief"**

Same enumeration as B-B1. Already surfaced above.

---

**B-4B2. `FOUR_AXIS_REASONING_SYSTEM` BURNOUT definition: "exhaustion, overwork, caregiving burden, sleep deprivation"**

Same enumeration as B-B2. Already surfaced above.

---

**B-4B3. `FOUR_AXIS_REASONING_SYSTEM` confidence calibration instructions: "0.65-0.85 when signal is implicit or could be read either way; 0.5-0.65 when two categories are plausibly correct"**

Source: `FOUR_AXIS_REASONING_SYSTEM` JSON schema tail.
This calibration instruction is not in `WELLBEING_CLASSIFIER_SYSTEM` — it's specific to the reasoning variant. The three-band calibration (0.9+, 0.65–0.85, 0.5–0.65) was added to address the flat-0.95 artifact documented in Test N full-corpus runs (per comment at line 134–136 in `run_4axis_full_corpus_test.py`). The specific band boundaries encode the observed miscalibration. Fragility: the band structure teaches the model to use 0.5–0.65 "when two categories are plausibly correct." This instruction may inadvertently suppress confidence on edge cases that are genuinely CRISIS — if a model reads a resilience-framed food insecurity disclosure as "plausibly CRISIS or ENGAGED," the instruction pushes it toward the 0.5–0.65 range, making the uncertainty visible but also potentially making the downstream threshold ambiguous. The calibration was tuned against the flat-0.95 artifact, not against a validated calibration standard.

---

**B-4B4. `UNIFIED_4AXIS_BASE_SYSTEM` (derived from `WELLBEING_CLASSIFIER_SYSTEM` minus three blocks): topic-adjacency, tiebreaker, and worked examples are all RETAINED in base**

The v2 extraction removes supersedes, single-sentence, and tiebreaker blocks. However, the topic-adjacency paragraph (B-B5 above) and the WORKED EXAMPLES (A-B5, A-B6, B-B7 above) remain in `UNIFIED_4AXIS_BASE_SYSTEM` because they are not in the stripped blocks. These passages carry all the corpus-tuning identified for them above, and they persist in the base. This is worth noting: the v2 block-stripping modularizes the supersedes and single-sentence logic, but leaves the worked examples and topic-adjacency intact in the base — meaning those corpus-calibrated passages always apply in 4-axis runs, regardless of supersedes_state.

---

**B-4B5. `UNIFIED_4AXIS_BASE_SYSTEM` IDENTITY DISCLOSURE: wellbeing signal examples enumeration**

The full wellbeing-signal-beyond-identity-disclosure list ("exhaustion that cuts off thought (trailing off mid-sentence, incomplete submissions that end abruptly), lost sleep named directly, food or housing instability, fear for safety, caregiving burden limiting capacity, or overwork that the student names as interfering") enumerates the signal types that appear in the WB corpus. Each item in this list corresponds to at least one WB case: trailing off mid-sentence → S002 (edge, also in ethnic studies corpus); lost sleep → WB05; food/housing → WB03/WB06/WB11–13; fear for safety → WB01/WB04; caregiving → WB02; overwork → WB05. The parenthetical "trailing off mid-sentence, incomplete submissions that end abruptly" is the sharpest single-essay anchoring in the whole prompt — it's a description of S002's exact presentation. Already surfaced in A-B2; noting here that it persists in the 4-axis base.

---

## Genob (UNIFIED_GENOB_BASE_SYSTEM + OBSERVATION_PROMPT + unified blocks)

### A. Direct example-to-essay matches

**A-G1. `UNIFIED_GENOB_BASE_SYSTEM` PERSONAL EXPERIENCE section: "grandmother's migration, their father's union work, or their sibling's diagnosis"**

Same enumeration as A-B8, identical text to `WELLBEING_CLASSIFIER_SYSTEM`. Same corpus coverage: S001/S005/S023 (grandmothers), S024 (mother's factory labor → "father's union work" is the synthetic analog), S026 (sibling's school experience → "sibling's diagnosis" analog). The genob base retains this passage verbatim. This is the single clearest direct-corpus-to-prompt match that genob shares with binary and 4-axis.

---

**A-G2. `UNIFIED_GENOB_BASE_SYSTEM` MINIMIZED DISCLOSURE: "mosque, food bank, extended family"**

Same as A-B7. Genob retains this verbatim. Same corpus matches: WB06, WB11, WB12, WB13.

---

**A-G3. `UNIFIED_GENOB_SINGLE_SENTENCE_BLOCK`: "'It was fine though' after disclosing they had nothing at home"**

Same as A-B11. Identical text to the binary block.

---

**A-G4. `UNIFIED_GENOB_BASE_SYSTEM` WORKED EXAMPLES (a), (b), (c)**

Same worked examples as in `WELLBEING_CLASSIFIER_SYSTEM` and binary. The phrasing is adapted for observation mode ("In your observation, describe what they are reaching for analytically" / "In your observation, name the food insecurity directly") but the case anchors are identical: labor-themed assignment + two-job student (→ S022 corpus shape), one-sentence food insecurity (→ WB06/WB12 shape), generic third-person burnout rhetoric (→ S022/WB10 shape).

---

### B. Name-all-the-things passages

**B-G1. `UNIFIED_GENOB_BASE_SYSTEM` opening concern-list: "domestic violence, housing loss, food insecurity, immigration enforcement threat, recent loss/grief, burnout, exhaustion, overwork, caregiving burden, sleep deprivation, or other concerns. This list is not exhaustive."**

This is the genob version of the CRISIS + BURNOUT enumeration. Unlike the binary and 4-axis versions, genob explicitly appends "or other concerns. This list is not exhaustive." The "not exhaustive" hedge is a meaningful structural improvement over the binary/4-axis versions — it does not anchor the model to the list as a checklist. However, the list still enumerates the WB corpus's coverage almost completely, and the hedge comes after the list rather than before it. The order effect (list-first, hedge-second) may still prime the model toward list items over unlisted signal types.

---

**B-G2. `UNIFIED_GENOB_BASE_SYSTEM` IDENTITY DISCLOSURE signal list: "exhaustion that cuts off thought, lost sleep named directly, food or housing instability, fear for safety, caregiving burden limiting capacity, or overwork that the student names as interfering"**

Same enumeration as B-4B5 / A-B2. Same corpus anchoring. Genob retains this verbatim from the binary version.

---

**B-G3. `UNIFIED_GENOB_SUPERSEDES_BLOCK`: "domestic violence, housing loss, food insecurity, or immigration enforcement threat"**

Same four-item enumeration as A-B12 / A-4A4. Identical text to the binary supersedes block, adapted for observation framing ("name the disclosure directly"). Same fragility: WB08 (grief/loss) and WB07 (sexual violence secondary) not in the four-item list.

---

**Overall genob assessment:** Genob has markedly fewer direct A-items than binary and 4-axis — the observation framing structurally reduces the prompt's dependence on classification-triggering examples. The WORKED EXAMPLES and the PERSONAL EXPERIENCE enumeration are the primary corpus-tuning carried over. The "not exhaustive" hedge in B-G1 is the only structural improvement over binary/4-axis on the name-all-the-things dimension; the other lists are retained verbatim.

---

## Notes / uncertainties

**N1. Shared inheritance means single-source fragility.**
`BINARY_REASONING_SYSTEM` and `UNIFIED_4AXIS_BASE_SYSTEM` both inherit directly from `WELLBEING_CLASSIFIER_SYSTEM`. Every corpus-calibrated passage in `WELLBEING_CLASSIFIER_SYSTEM` propagates into both unless explicitly stripped. The v2 stripping removes only the supersedes, single-sentence, and tiebreaker blocks — everything else (WORKED EXAMPLES, TOPIC-ADJACENCY, PERSONAL EXPERIENCE, IDENTITY DISCLOSURE detail) persists in both.

**N2. The grandmother example chain is the most saturated single corpus-to-prompt connection.**
A-B8 identifies 7–8 corpus cases (S001, S004, S005, S023, S024, S026, S028, S030) implicated by the PERSONAL EXPERIENCE passage. This passage is present in all three prompts. It's the passage most likely to behave differently on a new corpus where students do not use family-narrative pedagogy.

**N3. WB07 and WB08 are the gap cases in the supersedes enumeration.**
The supersedes blocks across all three prompts enumerate four CRISIS types (DV, housing, food, immigration). WB07 (mother's sexual assault — psychological distress from family victimization) and WB08 (grief after cousin's killing at traffic stop) are both expected CRISIS but fit awkwardly into the four-item list. WB07 maps loosely to DV; WB08 maps to "recent loss/grief" in the CRISIS definition but not in the supersedes block. If the model treats the supersedes list as exhaustive for override purposes, these two cases may not trigger the override at full sensitivity.

**N4. S002 "trailing off mid-sentence" appears corpus-tuned but was confirmed EDGE in master log.**
A-B2 flags this as a direct corpus match. The master log (Issue 2, session-end state) confirms S002 is a genuine edge case. The prompt's calibration to S002's exact presentation is therefore calibration to a case whose true label is ambiguous. Not a risk that can be resolved in the audit — flagging for completeness.

**N5. `OBSERVATION_PROMPT` (legacy) is not the genob system prompt used in v2 unified runs.**
`OBSERVATION_PROMPT` in `prompts.py` (lines 1463–1540) is the production observation prompt with CLASS CONTEXT, trajectory context, teacher lens, structural power move detection, and relational epistemology instruction. The v2 unified genob variants use `UNIFIED_GENOB_BASE_SYSTEM` as the system prompt and `WELLBEING_CLASSIFIER_PROMPT` as the user prompt — not `OBSERVATION_PROMPT`. `OBSERVATION_PROMPT` carries substantially more corpus-adjacent content (power move taxonomy, relational epistemology framing, specific structural power move names like "tone policing," "colorblind erasure") and has its own fragility profile that is OUT OF SCOPE for this audit (it's not part of the unified v2 suite). Flagging so it isn't conflated with `UNIFIED_GENOB_BASE_SYSTEM` in downstream analysis.

**N6. Appears corpus-tuned; no clear corpus match found.**
The phrase "Emotional intensity or personal vulnerability in the writing is NOT burnout — a student who writes passionately about painful experiences and reflects on the process ('this is what I needed to write') is deeply engaged, not depleted" (A-B1) — the specific phrase "this is what I needed to write" has no exact corpus match in the 46-student JSON. The quote is synthetic but clearly shaped around WB07's pattern. Flagging as "appears corpus-tuned; closest match is WB07 but no verbatim corpus source identified."

**N7. The ACCURATE CHARACTERIZATION block in `UNIFIED_GENOB_BASE_SYSTEM` has no corpus-specific match.**
The final genob-specific block — "Name what you observe accurately. When a student discloses a specific circumstance, use the student's own framing or an accurate characterization of what they described. Do not substitute softer terms..." — reads as a meta-instruction against hedging rather than an example-match. No single corpus case maps cleanly to it, though WB04 (domestic abuse disclosure with institutional suppression framing) is the likely motivating case. This block appears to be a structural principle rather than corpus-tuned.
