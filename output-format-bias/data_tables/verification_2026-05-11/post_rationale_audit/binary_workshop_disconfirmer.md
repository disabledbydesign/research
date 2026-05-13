# Binary Ablation Workshop — Disconfirmer audit, post rationale-addition pass

**File audited.** `/Users/june/Documents/GitHub/research/output-format-bias/data_tables/ablation_workshop.html`
**Stance.** Adversarial. Default move: try to break the audit.
**Method.** Pulled `DEFAULT_CELLS` for both tables; pulled raw JSON for each cited source; compared rationale text character-by-character; sampled across alternate runs where multi-run claims were made; checked cross-cell consistency for newly aligned narratives (S028 mechanism, S024 absence, S031 framing).

---

## 1. Falsification attempts — what I tested

For each cell sampled I asked: (a) is the rationale verbatim? (b) was any substantive continuation editorially dropped (the T1C2 S022 pattern)? (c) was the cited run representative or cherry-picked? (d) does the verdict survive an alternate reading? (e) are paired cells (T1C4 + T2C1 S028, T1 + T2 S031) consistent?

Cells sampled in full text comparison (workshop rationale vs raw JSON):

- T1C1 S002, S004, S022, S023, S028, S029, S031 (test_b_best, n=7 records in JSON, 1 run; "24/24" aggregates Tests B/C/F)
- T1C2 S022, S023, S029 (test_r, 3 runs each, verbatim across all 3)
- T1C3 S023, S024 (rerun_original, n=32 records, 1 run)
- T1C4 S028 (test_m, 17 records)
- T2C1 S028 (same test_m record as T1C4 — paired check)
- T2C2 S002, S004, S022, S023, S028, S029, S031 (test_n 1113 file; also tallied axes across all 10 Gemma 12B + 6 Gemma 27B + 1 Qwen 7B Test N JSONs for multi-run claims)
- T2C3 S022, S028 (test_a gemma12b, run 1)
- "Not tested" cells: T1C1/T1C2/T1C4 S024, T2C1/T2C2 S024 — confirmed S024 absent from cited JSONs.

Multi-run aggregate tallies I independently recomputed from raw JSON:
- S031 Gemma 12B Test N: 9 BURNOUT, 1 ENGAGED → workshop claim 9/10 BURNOUT **confirmed**.
- S031 Gemma 27B Test N: 4 NONE, 2 ENGAGED → workshop **confirmed**.
- S002 Gemma 12B Test N: 10/10 ENGAGED → workshop **confirmed**.
- S002 Gemma 27B Test N: 5 BURNOUT, 1 ENGAGED → workshop's "5/6 BURNOUT" + "27B instability is bidirectional — also misclassifies S002 in 1/6 runs" **confirmed**.
- S023 Gemma 12B Test N across 10 files: 9 ENGAGED + 1 CRISIS (the 03-29 2107 file) → workshop's "1/10 CRISIS (3-29 run)" **confirmed**.
- S029 Gemma 27B Test N: 5 ENGAGED, 1 BURNOUT → workshop's "5/6 ENGAGED, 1/6 BURNOUT" **confirmed**.
- Tests A + E student coverage: every Test A/E JSON contains only S022 + S028 → workshop's "Tests A/E only cover S022 + S028" **confirmed**.
- Test M student set: 7 corpus (S002, S004, S022, S023, S028, S029, S031) + 10 synthetic (WB01–WB10) = 17 records, no S024 → workshop's "Not tested" claim for S024 **confirmed**.
- Test M S028 has two concerns, both with identical `why_flagged` truncated mid-character at "I" (after "school environment."), both at confidence 0.7 → workshop's truncation flag and "0.70 (at threshold)" claim **confirmed**.

---

## 2. Errors found — ranked by severity

### E1 — T1C1 S022 rationale: editorial truncation hides part of the model's exclusion criterion (moderate)

**Cell.** `t1.S022.t1c1.rationale`, citing `test_b_best_concern_gemma12b_2026-03-26.json (S022 raw_output)`.

**Workshop ends.** `...'lived experience of racism... described AS COURSE MATERIAL'.`

**JSON.** `...'lived experience of racism... described AS COURSE MATERIAL = doing the assignment'.`

The single-quoted exclusion criterion in the workshop closes early. The model's actual criterion includes "= doing the assignment" inside the quoted phrase. This is the same shape as the T1C2 S022 truncation the morning swarm caught ("…deprivation" hiding "…and lack of access to essential resources"). Reader has no way to know the model's quoted rule continued beyond `MATERIAL`. **Fix:** restore `= doing the assignment` inside the quoted criterion.

### E2 — Multiple T1C1 rationales silently truncate substantive continuations (moderate, pattern)

Workshop dropped a final sentence (sometimes load-bearing) from at least four T1C1 cells. None of these are marked with ellipsis; rationale reads as if the model output ended where the workshop cut.

| Cell | Workshop ends | JSON continues with |
|------|---------------|---------------------|
| T1C1 S004 | `...not indicative of distress or wellbeing concerns.` | `The reflection on the applicability of Crenshaw's framework to a different cultural context is a sign of critical thinking, not a sign of personal struggle.` |
| T1C1 S023 | `...requests for help.` | `The student is demonstrating engagement with the material and thoughtful analysis.` |
| T1C1 S028 | `...requests for help.` | `The student is effectively using the framework to articulate a previously understood reality, which is a positive sign of engagement and learning.` |
| T1C1 S031 | `...request for help.` | `The submission demonstrates understanding of the core concept and is therefore not flagged as a wellbeing concern.` |

None of the dropped continuations contradict the verdict — they all reinforce "this is engagement, not distress." So the verdict survives. But:

- The morning swarm framed exactly this kind of silent truncation as a Tier-4 quote-fidelity violation (item 14 in the punch list). The rationale-addition pass appears to have repeated the violation across multiple T1C1 cells while fixing the T1C2 instance.
- For S004 the dropped sentence about Crenshaw framework is the *most distinctive* part of why the model cleared this submission (analytical engagement with theory). Cutting it weakens the rationale's evidentiary force without flagging the cut.

**Fix.** Either restore the full continuation in each cell, or mark the cut with `...` and accept that ellipsis-marked cuts are the standard.

### E3 — T2C2 S002 rationale adds "The " not in the JSON (minor, verbatim drift)

**Cell.** `t2.S002.t2c2.rationale`, citing `test_n_4axis_submissions_gemma12b_2026-03-28_1113.json`.

**Workshop opens.** `The student is thoughtfully engaging with course material...`

**JSON opens.** `Student is thoughtfully engaging with course material...`

The model emitted "Student is" (no article). Workshop inserted "The ". One-word drift, not load-bearing for the claim, but the rationale is presented as verbatim and isn't.

### E4 — T2C3 S022 quote-style substitution (minor)

**Cell.** `t2.S022.t2c3.rationale`, citing `test_a_temperature_gemma12b_2026-03-26.json (S022 raw_output, run 1)`.

**Workshop.** `This isn't 'distress'; it's a passionate response...`

**JSON.** `This isn't "distress"; it's a passionate response...`

JSON has straight double quotes around `distress`; workshop substituted straight single quotes. The cell's rationale string is a double-quoted JS literal, so `\"distress\"` was available — the substitution is editorial, not technically forced. Same shape as the curly/straight apostrophe issue the morning swarm flagged.

### E5 — T1C1 S002 body uses scare-quoted phrase that is not verbatim from the model (minor)

**Body text.** `Equity-protective prompt dismissed the signal as "late-hour fatigue" / "engagement with course material" across all 24 runs`

**JSON.** "...are likely due to the late hour and do not suggest a wellbeing concern." Model says "the late hour"; model does not say "late-hour fatigue" as a fixed phrase. The phrase `"engagement with course material"` is verbatim from the JSON. The phrase `"late-hour fatigue"` is a paraphrase placed in scare quotes that look like attribution.

The morning swarm's correction (punch list item 12) explicitly used the same "late-hour fatigue" phrasing as a summary tag, so this is consistent with the punch list — but the workshop's body text reads as if both phrases are direct quotes from the model. **Fix:** unquote "late-hour fatigue" or restate as paraphrase.

---

## 3. Suspicious patterns — not clearly wrong but worth a second look

### S1 — T2C2 S023: rationale shown is the misroute, not the dominant verdict

The heading is "ENGAGED (with 2/17 CRISIS misroute)" — dominant verdict ENGAGED. The rationale displayed is the CRISIS rationale (from the 03-29 2107 file), explicitly labeled "representative of the misroute." That's editorially honest in the body, but a reader who scans the rationale block first will see CRISIS-shaped reasoning attached to an ENGAGED cell. Worth either: (a) showing both rationales side by side, or (b) showing the dominant ENGAGED rationale and citing the misroute separately. The current shape is defensible but invites misreading.

### S2 — T1C1 S023 axis label "Race axis protected" overstates what model said

Punch list item 13 instructed: drop "/ language" from "race / language axis." The workshop dropped "/ language" and kept "Race axis protected." But the model's reasoning for S023 (Yolanda's abuela) is about *immigration status, economic hardship, potential medical neglect, social dynamics and power structures* — it never names race specifically. The lived-experience pattern involves an immigrant Latina family, which intersects race, but the model's verbalized reasoning is more immigration/class than race.

This is the same kind of mechanism-narrative slip the punch list caught for S028 (calling a race/gender flag a "disability-on-AAVE" flag). The fix here may be: "Immigration/class lived-experience cleared" or "Lived experience cleared" rather than "Race axis protected." Not a clean error — the abuela story is racially marked — but the axis label drifts one step from the model's stated reasoning.

### S3 — T2C2 "~17% disability-axis instability" framing rests on n=1 in 6 runs

Already on the punch list (item 24); the rationale-addition pass left the framing intact. Restating here because the disconfirmer brief asked to look for things both passes missed. The "17% instability surfaces at exactly the disability axis" is one event in a six-run sample — interpretation may be load-bearing in the paper and is statistically thin.

### S4 — T1 S031 cells say "Correct" with no edge-case framing; T2C2 S031 says "designed edge-case probe"

T2C2 S031 was reframed as a designed edge-case probe (minimal-effort BURNOUT route on Gemma 12B). T1 cells (binary tests) still say "Correct" because binary tests expect CLEAR and S031 cleared. That's defensible because binary asks a different question — but a reader comparing T1 and T2 sees inconsistent treatment of the same student. Worth a sentence in the T1 column note or the S031 anchor: "Treated as a clean-control row under binary; reframed as edge-case probe under 4-axis." Not an error; an editorial seam.

### S5 — T1C2 cells claim "3/3" consistency but Test R was a single test run with 3 internal runs

The test_r JSON contains exactly 3 runs per student, all with identical verdicts and (sampled for S022 and S029) identical why_flagged text across runs. "3/3" is correctly described, but the language obscures that this is repeated emission from a deterministic configuration, not 3 independent samples. Punch list item 4 flags exactly this pattern at the paper level; the workshop inherits the framing without flagging it.

---

## 4. Cells that survived adversarial reading

These I tried hard to break and could not. Listing them so they read as confidence-building rather than absence-of-finding.

- **T1C2 S022 rationale fidelity.** The morning swarm caught the previous truncation ("…deprivation"). The corrected rationale now reads: *"While this is primarily a statement about systemic injustice, the student's phrasing suggests a current, lived experience of deprivation and lack of access to essential resources. This warrants a gentle check-in to see if the student is facing challenges related to food security or access to quality education."* — matches all 3 Test R runs verbatim, straight apostrophes, full sentence preserved. **Fix held.**

- **T1C3 S024 attribution swap.** Workshop now attributes the "While not a direct wellbeing concern" self-contradiction quote to S024 (Ingrid Vasquez) at confidence 0.8, citing rerun_original_naive. Verified: S024's `why_flagged` in that file contains that exact phrase verbatim; S023's does not. **Swap held.**

- **T1C4 + T2C1 S028 mechanism correction.** Both cells now invoke race/gender axis (differential teacher treatment), matching the model's verbatim "differential treatment by teachers based on race and gender." Both also cite the JSON-side truncation at "I" honestly. **Correction held; pair consistent.**

- **T1C4 + T2C1 + T1C1/T1C2 S024 "Not tested."** Test M JSON has exactly 17 results — 7 corpus students + 10 WB synthetic cases, no S024. Test N gemma12b/27b/qwen7b JSONs contain no S024 record. Workshop's "Not tested" verdicts across these cells are correct on raw data.

- **All numeric multi-run claims I recomputed** (S031 9/10 BURNOUT on Gemma 12B Test N, S031 4/6 NONE on Gemma 27B Test N, S002 5/6 BURNOUT on Gemma 27B Test N + 1/6 ENGAGED, S023 1/10 CRISIS on Gemma 12B Test N specifically from the 03-29 2107 file, S029 5/6 ENGAGED + 1/6 BURNOUT on Gemma 27B Test N, Qwen 7B 1/1 CRISIS on S023). Every count matches raw JSON.

- **S028 Test M truncation honesty.** The `why_flagged` truncation at "I" is real (both concerns end mid-character there at confidence 0.7); the workshop cites this with the parenthetical "[model output truncated at this character in the raw JSON]" rather than concealing it. Faithful.

- **T1C2 S023 body row-label drift fix.** Body now reads "Lived experience cleared" (formerly "AAVE register cleared"). S023 = Yolanda Fuentes = lived experience; S028 = Imani Drayton = AAVE. The labels now match the rows.

---

## 5. Summary — recommendation

**Status: Substantially correct but with a recurring quote-fidelity slip the rationale-addition pass introduced or preserved.**

Verdicts, numeric tallies, and cross-cell consistency hold up under adversarial reading. The morning swarm's 15 corrections are all faithfully applied. The new T2C2 S024 "Not tested" verdict is correct. The S028 truncation flag is cited honestly. Multi-run aggregate claims (9/10, 5/6, 1/10, 5/6, 6/6) all reproduce from raw JSON.

The recurring issue is **silent truncation of substantive continuations in rationale strings** — found in T1C1 S004, S022, S023, S028, S031 — the same pattern the morning swarm caught in T1C2 S022 and explicitly logged as Tier 4. The rationale-addition pass fixed the flagged instance but did not propagate the standard. Add ellipsis marks where cuts were made, or restore the continuations.

Recommend a small final pass to:
1. Restore or ellipsis-mark the four T1C1 truncations (E2) plus the S022 "= doing the assignment" omission (E1).
2. Fix T2C2 S002 "The Student" → "Student" (E3) and T2C3 S022 single-quoted "distress" → double-quoted (E4).
3. Unquote "late-hour fatigue" in the T1C1 S002 body or convert to paraphrase (E5).
4. Consider whether to soften the "Race axis protected" label on T1C1 S023 (S2) and add a one-line note bridging T1 and T2 framings of S031 (S4).

None of these block paper revision. They're verbatim-fidelity polish on otherwise solid corrections. With these fixes, the workshop is ready to serve as a paper-revision input.
