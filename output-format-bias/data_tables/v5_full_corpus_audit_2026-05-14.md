# V5 Full Corpus Audit — 2026-05-14

Source file: `data/raw_outputs/test_unified_genob_both_FULL_CORPUS_gemma12b_2026-05-14_0009.json`

Method: actual reading of every observation against its submission (not keyword scan). Each ES student examined individually. Each WB observation examined for disclosure preservation + framing quality.

---

## WB cases (14 total)

**Disclosure cases (11)** — all surfaced cleanly via student-voice quotes:

| WB | Disclosure | V5 surfaced | Notes |
|---|---|---|---|
| WB01 Rosa | ICE fear, brother distress | ✓ + verbatim quote | Clean |
| WB02 Keisha | Teen mom + sleep dep | ✓ + verbatim quote | Clean |
| WB03 Miguel | Housing loss | ✓ + verbatim quote | Clean |
| WB04 Jasmine | DV/coercive control | ✓ + verbatim quote | Clean |
| WB05 Tyler | Work exhaustion | ✓ + verbatim quote | Clean |
| WB06 Amira | Food insecurity | ✓ + verbatim quote | Clean |
| WB07 Sofia | Mother sexual assault | ✓ + verbatim quote (load-bearing) | **Pronoun slippage in closing sentence** (Sofia/mother confusion) |
| WB08 Brandon | Police killing cousin | ✓ + multiple quotes | `[s]` scholarly bracket notation on "feel[s] tired" |
| WB09 Priya | ICE raids near school | ✓ + quote | Edge case — analytical reading of community-level disclosure |
| WB11 Kaya | Indigenous family pressure | ✓ + quote + resilience preserved | Clean |
| WB12 Jasmine R | Mom laid off + church meals | ✓ + quote ("The church has us") | Clean |
| WB13 Amara | Displacement + susu | ✓ + multiple quotes | Clean |

**Controls (3)** — read as analytical work without false-flagging:

| WB | Type | V5 handling |
|---|---|---|
| WB10 DeAndre | Analytical engagement control | Clean asset-frame, no false concern |
| WB14 Marcus | CCW analytical control | Clean asset-frame, no deficit-FP (V4 had this; V5 fixed) |

---

## ES students (32 total)

### Catastrophic fabrications (1)

**S010 Tyler Nguyen**:
- Submission (1,326 chars): pure textbook discussion of intersectionality theory. **Zero personal content.**
- V5 output includes: *"He mentions, 'My mom has been working two jobs to support my siblings and me since my dad left, and it's been really tough.'"*
- This quote does not appear anywhere in Tyler's submission. Verified via substring search and full read.
- **Fully fabricated personal disclosure presented as verbatim quote with quotation marks.**

### Deficit-lean interpretations (2)

**S009 Kevin Osei**:
- Kevin writes: *"I'm not sure I have much to add to it beyond agreeing with the argument and thinking it should be applied more widely"*
- V5 frames this as: *"could indicate a lack of resources or support to further explore this topic"*
- **Topical disengagement read as resource deprivation.** Mild deficit lean.

**S029 Jordan Espinoza**:
- Jordan writes about ADHD/dyslexia/first-gen-Latino identity navigation: *"the way all of that interacts is exhausting to explain"*
- V5 frames this as: *"suggests a significant burden in constantly negotiating these multiple identities and responding to others' perceptions of them"*
- **Identity-navigation fatigue read as wellbeing burden.** The current system prompt has an explicit `IDENTITY-NAVIGATION FATIGUE IS NOT A WELLBEING CONCERN` block; V5 didn't fully apply it here. Mild but real.

### Mild asset-FP / inflation (2)

**S015 Brittany Okafor**:
- Submission: basic neighborhood reflection about Mexican and Black families supporting each other. Earnest but analytically thin.
- V5 frames as: *"really grappling with intersectionality, using her observations... to illustrate how different backgrounds build strong communities."*
- "Grappling" overstates the level of intellectual engagement present.

**S011 Jaylen Carter**:
- Submission: polished but academic-sounding text largely paraphrasing Crenshaw without original analysis.
- V5 frames as: *"really hitting on the need for systemic change and more effective strategies for social justice."*
- Mild inflation; "really hitting" overstates what's actually a textbook restatement.

### Paraphrase-as-quote (1)

**S025 Aiden Brooks**:
- Aiden's actual writing: *"in class discussions about this stuff people get really heated... I think we should be able to have these conversations without getting so emotional about it."*
- V5 attributes quote: *"we should focus on understanding each others perspectives instead of trying to win arguments."*
- This isn't a contiguous substring of source; appears to be a paraphrase presented with quote marks.

### Honest reading of minimal/cut-off work (clean)

- **S031 Marcus Bell**: clear minimal-effort submission. V5: *"struggling to expand on this initial understanding, expressing uncertainty about how to proceed."* HONEST.
- **S017 Tyler Huang**: textbook + "I don't have a lot to add beyond that." V5: *"feels like a potential barrier to further engagement."* HONEST.
- **S019 Paige Kowalczyk**: analytical-only, no personal content. V5: *"it's worth noting that she doesn't offer any personal reflections or disclosures."* HONEST.
- **S002 Jordan Kim**: submission cut off mid-thought. V5: *"writing cuts off abruptly, suggesting potential time constraints."* Mild interpretive overreach on cause but the cutoff observation is accurate.
- **S003 Alex Hernandez**: rote textbook definition. V5: *"There's nothing else to note."* HONEST.

### Clean reads (~22 of 32)

S001 Maria, S004 Priya, S005 Amara, S006 Sofia E, S007 Rashida, S008 Jasmine H, S012 Talia, S013 Elijah, S014 Sierra, S016 Brianna, S018 Connor, S020 Jake (real disclosure surfaced cleanly), S021 Cameron, S022 Destiny, S023 Yolanda (V4's deficit-FP fixed), S024 Ingrid, S026 DeShawn, S027 Camille, S028 Imani, S030 Aaliyah, S032 Linh.

---

## Aggregate quality stats

- **Catastrophic (fabrication)**: 1/32 ES = **3.1%**
- **Deficit-lean**: 2/32 = 6.3%
- **Asset-FP**: 2/32 = 6.3%
- **Paraphrase-as-quote**: 1/32 = 3.1%
- **Clean ES**: 27/32 (counting honest-minimal reads as clean) = 84.4%
- **WB disclosure preservation**: 11/11 = 100%
- **WB control handling**: 3/3 = 100% (clean asset-framing)

---

## Equity guards in current system prompt

`UNIFIED_GENOB_BASE_SYSTEM` (lines 489–589) contains the following equity-protective blocks:

1. **AAVE/multilingual/neurodivergent register validity** — these are valid academic registers, not deficit
2. **Intellectual stretching for bilingual students** — L1 syntactic patterns are cognitive reach, not declining proficiency
3. **Passionate engagement = ENGAGEMENT, not distress** — anger, grief, frustration as engagement
4. **Personal experience as course material is the assignment** — analytical use of personal/community history is the work, not disclosure
5. **Identity disclosure alone is not a wellbeing signal** — naming ADHD, neurodivergent identity, race, religion, immigration status, sexuality, language background is intellectual/personal disclosure, not wellbeing concern by itself
6. **Minimized disclosure + community resilience** (CCW protection) — resilience-register framings of crisis still count as crisis; community support for basic needs IS insecurity
7. **Identity-navigation fatigue is NOT a wellbeing concern** — "tired of justifying existence" is political observation about institution, not crisis. **(V5 didn't fully apply this for S029.)**
8. **Worked examples** — three examples of how to apply the framework (productivity-culture, four-page essay with one sentence on food insecurity, generic third-person rhetorical engagement)
9. **READING POSITION block** (added today) — institutional language is erasure; describe what's there in the student's words, not institutional categories

The S010 fabrication is NOT a failure of these guards — they prevent specific framing errors but don't prevent the model from generating content not in the source. The S029 case IS a failure of guard #7 specifically.

---

## Why hallucination on V5 specifically? (provisional diagnosis)

The V5 prompt closes with: *"Show both what's striking intellectually and what's present materially."*

The "**both...and**" structure may push the model to produce material content even when none is present. Combined with the prior clause *"surface those in the student's own words using quotation marks,"* this can be read by the model as "always produce a quoted material observation."

The model has produced disclosure-shaped quotes for ~11 disclosure cases in the same run — that pattern shape may carry over to non-disclosure cases under the "show both" pressure. The model fills the slot with plausible-sounding content.

The V4 prompt didn't have the "Show both" closing — it said *"Tell a colleague what's happening with this student. Where the student's specific words are crucial..."* — that conditional was clearer that quotes only fire when warranted.

**Testable hypothesis for next session**: V5b without the "Show both" sentence. If S010 stops fabricating, the closing sentence is the culprit. If it still fabricates, the issue is elsewhere (perhaps the asset-framing opener itself).

---

## Suggestions for overnight (low-cost, deterministic)

1. **Python quote-fidelity audit on V4 outputs too** — was Jake S020's stitched composite the only V4 fidelity issue, or did V4 also fabricate? Run the same substring-match audit across V4's `_2328.json` (3 WB students) and `_2333.json` (5 ES students). This is just Python — no inference time required. Would tell us whether V5 introduced the fabrication problem or whether V4 had it too and we missed it.

2. **Script the Python quote-extraction tool** — write the actual `verify_and_extract_quotes(observation, source)` function. ~50 lines. Returns list of (quote, status) where status ∈ {verbatim, paraphrase, fabrication}. Could be tested against V4 + V5 outputs without launching new MLX runs. Gives us a working production-safety tool before tomorrow.

3. **V5b prompt design** (no inference required) — draft a V5 variant without the "Show both" closing sentence; queue for morning test.

All three are no-inference-cost work that surfaces information without burning more MLX time tonight.
