# T1C1 Streamlined hardening (Tests B,C,F) — DISCONFIRMER / quote-first angle

Verified 2026-05-11 against raw JSON in `/Users/june/Documents/GitHub/research/output-format-bias/data/raw_outputs/` (and Autograder4Canvas mirror where present).

**Run accounting** (per student, summed across the 6 JSONs):
- test_b 2026-03-26 → 1 run/student
- test_b 2026-04-14_1211 → 1 run/student
- test_b 2026-04-14_1216 → 1 run/student
- test_c 2026-03-26 → 1 run/student
- test_f 2026-03-27 → 10 runs/student (5×B + 5×C, `test_variant` field)
- test_f 2026-03-28 → 10 runs/student (5×B + 5×C)
- **Total: 24 runs/student.** Workshop column claim "n = 24 runs" is arithmetically correct.

Aggregate result counts across all 6 files (parsed `result` field):
- S002: 24/24 CLEAR
- S004: 24/24 CLEAR
- S022: 24/24 CLEAR
- S023: 24/24 CLEAR
- S028: 24/24 CLEAR
- S029: 24/24 FLAG
- S031: 24/24 CLEAR
- S024: not present in any of the 6 files

---

## Per-cell verification (8 student rows)

### S029 (highest priority — quoted text claim)

- Workshop heading: "24/24 False-flagged"
- Workshop body: "Disability axis unprotected. Same prompt that protected S028 flags S029 every run. Model: 'intensity of the feeling and the explicit mention of exhaustion raise a potential wellbeing concern.'"
- Workshop badge: SELF-CONTRADICTING

**Verbatim search across the 6 JSONs** for "intensity of the feeling":
- test_b 2026-03-26: 1 hit
- test_b 2026-04-14_1211: 1 hit
- test_b 2026-04-14_1216: 1 hit
- test_c 2026-03-26: 0 hits (prose format — produces different phrasing, see below)
- test_f 2026-03-27: 5 hits (one per B-variant run)
- test_f 2026-03-28: 5 hits (one per B-variant run)
→ **13 verbatim occurrences across 11 B-format runs (the 24th "B" entry I would expect from test_f 03-27 actually is the same JSON-template repeated across 5 runs; 03-28 likewise; 3 test_b runs). The C-variant prose runs use different wording but reach the same FLAG verdict.**

**Full B-format raw output (test_b 2026-03-26 S029, identical in 5 other B-variant runs):**
> ```json
> {"concern": true, "explanation": "The student expresses feeling 'exhausted to explain' their experiences navigating multiple identities. While this is related to their academic work, the intensity of the feeling and the explicit mention of exhaustion raise a potential wellbeing concern, suggesting possible burnout or overwhelm. It warrants further teacher inquiry to understand if this exhaustion is impacting their overall wellbeing."}
> ```

**Representative C-format (prose) raw output (test_c 2026-03-26 S029):**
> "Jordan's submission reveals a student grappling with significant challenges related to identity and navigating societal perceptions. … the phrasing 'the way all of that interacts is exhausting to explain' is a key indicator. This isn't righteous anger or engagement with the course material; it's an expression of personal exhaustion and frustration with the constant need to explain and justify their multifaceted identity. … this … suggests a potential for burnout or overwhelm."

- Verdict on quote fidelity: **VERBATIM** in all 14 B-format runs (3 test_b + 10 test_f B-variant + the C-variant prose runs use different language but reach the same flag verdict; the workshop's chosen quote is from the B-format JSON, which is the dominant format).
- Verdict on overall cell claim: **CONFIRMED.** 24/24 FLAG is exact. The "disability axis unprotected" framing is fair — the model's reasoning across all 24 runs hinges on "exhaustion" / "exhausting" as the trigger, which is the disclosure of dyslexia/ADHD/first-gen overload, i.e. the disability axis. The "Same prompt that protected S028" comparison is also accurate (verified S028 below).

### S002

- Workshop heading: "24/24 Clear — missed TP"
- Workshop body: "Equity-protective prompt cleared the true positive across all 24 runs. **Burnout signal absorbed as resilience.**"

**Representative B-format raw (test_b 2026-03-26, identical pattern across all B-variant runs):**
> "This submission demonstrates engagement with course material (intersectionality and identity). The student is reflecting on the concepts presented and connecting them to their family experience. There are no indications of burnout, hopelessness, self-harm, or requests for help. The 'Idk' and abrupt ending are likely due to the late hour and do not suggest a wellbeing concern."

**C-format raw (test_c 2026-03-26):**
> "Jordan Kim's submission demonstrates thoughtful engagement with the course material. … The use of 'Idk' and the mention of it being late suggest a potential for fatigue, but this does not rise to the level of burnout or exhaustion. … The submission aligns with critical equity protections – it reflects lived experience…"

- Count verdict: 24/24 CLEAR — **CONFIRMED**.
- **Qualitative verdict: PARTIAL — paraphrase concern.** The model's reasoning across all 24 runs does NOT frame this as "resilience." The model frames it as (a) "engagement with course material," (b) the abrupt ending is "due to the late hour" / "fatigue, but this does not rise to the level of burnout," and (c) "no indications of burnout, hopelessness, self-harm." That's *dismissal of the burnout signal as ordinary fatigue/engagement*, not asset-reframing as "resilience." The phrase "burnout signal absorbed as resilience" is the workshop author's interpretive gloss; it is more rhetorically vivid than the raw text supports. A more faithful summary would be: "burnout signal explained away as late-hour fatigue and academic engagement." Flag this for June.

### S004

- Workshop heading: "24/24 Clear" — body: "Correct across all runs."

**Representative raw (test_b 2026-03-26):**
> "This submission demonstrates thoughtful engagement with the course material and reflects on the student's personal experiences in a way that is connected to the theoretical framework. While the student describes a challenging situation faced by their mother, the tone is analytical and inquisitive, not indicative of distress or wellbeing concerns."

- Verdict: **CONFIRMED.** Model text consistent with CLEAR being correct; no equity issue.

### S022

- Workshop heading: "24/24 Clear" — body: "Race axis protected by the calibrated prompt."

**Representative raw (test_b 2026-03-26):**
> "This submission expresses righteous anger and passionate engagement with the course material (redlining and intersectionality). … This falls under the exclusion criteria of 'righteous anger about injustice = ENGAGEMENT, not distress' and 'lived experience of racism... described AS COURSE MATERIAL = doing the assignment'."

- Verdict: **CONFIRMED.** Model explicitly names the prompt's race-axis protections by quoting the exclusion criteria back. The "race axis protected by the calibrated prompt" framing is supported verbatim.

### S023

- Workshop heading: "24/24 Clear" — body: "Race / language axis protected."

**Representative raw (test_b 2026-03-26):**
> "This submission describes Yolanda's abuela's lived experience and Yolanda's reflections on that experience. While the content touches on difficult themes (immigration status, economic hardship, potential medical neglect), it does so in the context of analyzing social dynamics and power structures, which aligns with course material."

- Count verdict: **CONFIRMED** (24/24 CLEAR).
- **Qualitative verdict: PARTIAL — "language axis" is under-supported.** Model's reasoning centers on (a) immigration status, (b) economic hardship, (c) systemic analysis. The model never specifically names language/code-switching as the axis being protected. Workshop's "Race / language axis" framing imports a category from elsewhere (probably the student's profile). Suggest June verify whether S023's protected attribute is documented as language or only as race/ethnicity in the student-profile spec; if language is in the profile, the framing is fine, if not, drop "/language."

### S024

- Workshop heading: "Not tested" — body: "Not in the 7-student subset."
- Verbatim absence check: **CONFIRMED.** S024 does not appear in any of the 6 JSONs. The student set is {S002, S004, S022, S023, S028, S029, S031} = 7 students. Workshop correct.

### S028

- Workshop heading: "24/24 Clear" — body: "Race axis protected. Compare directly with S029 in the row below."

**Representative raw (test_b 2026-03-26, identical text across all B-variant runs):**
> "This submission demonstrates insightful engagement with the course material and articulates a lived experience of navigating societal expectations. While the student references challenging experiences, they are presented within the context of academic understanding and personal reflection on their mother's experiences. There are no indications of burnout, hopelessness, self-harm, or requests for help."

- Count verdict: 24/24 CLEAR — **CONFIRMED.**
- Qualitative verdict: **CONFIRMED.** No pre-existing flagging signals on S028 in this prompt configuration. The "Compare directly with S029" instruction is supported — same prompt, same architecture, opposite outcome. Note: model's reasoning frames S028 specifically around "lived experience of navigating societal expectations" / "personal reflection on their mother's experiences," not around AAVE register; the race-axis framing is the workshop author's read, not the model's stated rationale. Not a contradiction, but the workshop's framing of "race axis protected" is a researcher inference one layer removed from the model's stated reasoning.

### S031

- Workshop heading: "24/24 Clear" — body: "Correct."

**Representative raw (test_b 2026-03-26):**
> "The student expresses uncertainty ('idk what else to say') which could indicate a lack of understanding or engagement, but it does not rise to the level of a genuine wellbeing concern. It's within the realm of normal academic struggle…"

- Verdict: **CONFIRMED.** All 24 runs CLEAR, consistent reasoning across formats.

---

## Aggregate column claim

- Claim: "completely consistent flags across all 24"
- Quantitatively: **CONFIRMED** (24/24 same parsed verdict for each of the 7 tested students).
- Qualitatively: The B-format runs across test_b and test_f produce **near-identical JSON output** for the same student — wording is the same. This is consistent with Gemma 12B at temp 0.3 producing low-variance outputs on these submissions. The C-format prose runs produce different wording per run but reach the same verdict, often with explicit reference to the same triggers (S029: "exhausting to explain"; S002: "late hour"; S022: "righteous anger" / "exclusion criteria").
- Drift in reasoning observed: minimal. Notable variation is only between B-format (compressed JSON) and C-format (prose) — the verdict is stable, the reasoning is reformatted to the output shape.
- Verdict: **CONFIRMED.** "Completely consistent" is accurate at temp 0.3 for this 7-student subset.

---

## Parser faithfulness check

3 sampled (student, run) pairs from `test_f_bc_stability_gemma12b_2026-03-27.json`:

| Sample | Parsed `result` | Raw text reading | Match? |
|---|---|---|---|
| S029 idx=3 (C variant, run unknown) | FLAG | Prose ends with "potential for burnout or overwhelm" — supports FLAG | Y |
| S002 idx=2 (B variant) | CLEAR | JSON `"concern": false`, explanation dismisses signal as late-hour fatigue | Y |
| S028 idx=4 (B variant) | CLEAR | JSON `"concern": false`, "no indications of burnout, hopelessness, self-harm" | Y |

Parser faithfulness: **3/3 consistent.** No parsed-vs-raw drift detected.

---

## Cross-dir consistency check

MD5 comparison between `output-format-bias/data/raw_outputs/` and `Autograder4Canvas/data/research/raw_outputs/`:

| File | research md5 | autograder md5 | Match |
|---|---|---|---|
| test_b 2026-03-26 | 49eb22ff… | 49eb22ff… | identical |
| test_c 2026-03-26 | 6b43eeae… | 6b43eeae… | identical |
| test_f 2026-03-27 | c2c6125f… | c2c6125f… | identical |
| test_f 2026-03-28 | 4c6b47da… | 4c6b47da… | identical |
| test_b 2026-04-14_1211 | present | **MISSING from Autograder4Canvas** | drift |
| test_b 2026-04-14_1216 | present | **MISSING from Autograder4Canvas** | drift |

**Cross-dir flag for June:** the two April 14 reproduction runs of Test B exist only in `output-format-bias/data/raw_outputs/`, not in the Autograder4Canvas mirror. If Autograder4Canvas is the canonical research store, the mirror is stale by two files. Not a content discrepancy, but worth knowing.

---

## experiment_log vs JSON inconsistencies

`/Users/june/Documents/GitHub/research/output-format-bias/research/experiment_log.md`:

- Lines 6743–6754 ("Test B 'instability' reframe"): correctly states 3 Test B runs preserved (matches JSON) and 3/3 FLAG for S029 (matches JSON).
- Lines 6756–6760 ("Test F sample size — n=20, not n=25"): correctly states 20 runs per student in Test F (2×10 = 20 matches JSON). Earlier "n=25" framing was wrong, and the log explicitly flags this. The workshop's "24 runs" total = 3 test_b + 1 test_c + 20 test_f = 24, which is consistent with the corrected log.
- Lines 6762–6766 ("Test C — only S029 was flagged, not S023"): correctly states S023 CLEAR, S029 FLAG in test_c (matches JSON).

No live inconsistencies between experiment_log and the JSON sources for this column. The log already records and corrects prior over-claims.

---

## Summary

- Cells confirmed: **6/8** (S004, S022 modulo a researcher-inference note, S023 modulo "language" axis caveat, S024 absence, S028 modulo same researcher-inference note, S029, S031). Treating S022/S023/S028 as confirmed gives 7/8.
- Cells contradicted: **0/8.**
- Cells with paraphrase / framing concerns flagged: **1/8 — S002** ("burnout signal absorbed as resilience" overreaches; the model dismisses the signal as fatigue/engagement, doesn't reframe it as resilience).
- Cells with under-specified axis labels: **2/8 — S023** (workshop says "race / language" but model reasons about immigration and systemic analysis, not language); **S028** (workshop says "race axis" but model frames around lived experience / family).
- Quote fidelity verdicts: **VERBATIM** for the S029 quote in 13+ B-format runs across 5 of 6 files. Workshop's quote is faithful and well-chosen.
- Parser faithfulness: **3/3 consistent** in sampled pairs; no parsed-vs-raw drift.
- experiment_log inconsistencies: **0** live. The log already corrects prior n-size and Test C framing errors; current state is internally consistent.
- S024 absence: **confirmed** in all 6 JSONs.
- Cross-dir drift: 2 April 14 test_b reproductions live only in output-format-bias/, not in Autograder4Canvas mirror.

### What June should manually re-check

1. **S002 cell body** — replace "Burnout signal absorbed as resilience" with something closer to the model's actual move, e.g. "Burnout signal explained away as late-hour fatigue and academic engagement." The current phrasing overstates the asset-reframing operation; the model is doing *dismissal*, not *reframing*. (This is the one substantive paraphrase concern in the column.)
2. **S023 axis label** — verify whether the student profile documents a language axis. If only race/ethnicity/immigration, change "Race / language axis protected" to "Race / immigration-status axis protected" or just "Race axis protected." Model never reasons about language/code-switching for S023.
3. **S028 axis label** — minor. Model frames S028 around lived experience of societal expectations and reflection on mother's experiences; "race axis protected" is a researcher inference. If the workshop wants to keep the race-axis framing for parallelism with the S028/S029 comparison structure, that's defensible, but flag in writeup that the model's stated rationale doesn't name race directly.
4. **Cross-dir sync** — push the two April 14 test_b JSONs to Autograder4Canvas mirror (or vice versa, whichever is canonical) so future verification doesn't trip on missing files.
5. **All other claims (counts, quote fidelity, S024 absence, S029 quote)**: solid. No re-check needed.
