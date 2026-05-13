# T1C2 Rich taxonomy / Test R — DISCONFIRMER / quote-first angle

**Source of truth:** `/Users/june/Documents/GitHub/research/output-format-bias/data/raw_outputs/test_r_wellbeing_concern_synthetic_gemma12b_2026-05-10_2119.json`
(The Autograder4Canvas mirror path does not exist; only one raw JSON in this repo.)

**Workshop column header verified:** `t1c2: { ... note: 'Binary flag/clear with full DO / DO-NOT taxonomy. Test R · n = 3 runs · completely consistent flags across all 3.' }` — JSON metadata confirms `n_runs_per_student: 3`, `n_students_tested: 7`, and every per-student set of 3 runs produces an identical raw_output. CONFIRMED.

---

## Verbatim quote verification (highest priority)

### S022 quote

- **Workshop text:** "While this is primarily a statement about systemic injustice, the student's phrasing suggests a current, lived experience of deprivation."
- **Found verbatim in raw JSON:** **N (truncated + typographic substitution).** The JSON sentence does not end at "deprivation." — it continues: "…of deprivation and lack of access to essential resources." Workshop adds a terminal period that does not exist in the source. Workshop also uses a curly right-single-quote (’) in "student’s"; JSON uses a straight ASCII apostrophe (').
- **Where found:** all 3 runs of S022, JSON path `results[i].raw_output` → embedded code-fenced JSON → `concerns[0].why_flagged`.
- **Up-to-truncation match:** the substring "While this is primarily a statement about systemic injustice, the student's phrasing suggests a current, lived experience of deprivation" (no terminal period, straight apostrophe) IS present verbatim in all 3 runs (3/3). The full sentence in JSON is:
  > "While this is primarily a statement about systemic injustice, the student's phrasing suggests a current, lived experience of deprivation and lack of access to essential resources. This warrants a gentle check-in to see if the student is facing challenges related to food security or access to quality education."
- **Run-to-run drift:** none. The why_flagged text is byte-identical across runs 1/2/3.
- **Verdict on quote fidelity:** **NEAR-VERBATIM (truncated mid-sentence, terminal period added, apostrophe glyph substituted).** The model's actual sentence makes a stronger / more action-oriented claim than the workshop excerpt suggests — the truncated portion is what motivates the "gentle check-in about food security." That follow-on context arguably *strengthens* the workshop's "self-contradicting" reading, but readers should be told the period is editorial.

### S029 quote

- **Workshop text:** "While this is likely related to identity-navigation fatigue and a commentary on societal expectations, it indicates a level of ongoing stress and burden that warrants teacher awareness."
- **Found verbatim in raw JSON:** **Y.** Exact-string match including final period and ASCII apostrophes. JSON path: `results[i].raw_output` → `concerns[0].why_flagged`, last sentence.
- **Which runs:** all 3 (3/3). Byte-identical across runs 1/2/3.
- **Surrounding context (preceding sentence in JSON):** "The student expresses that navigating their multiple identities and associated perceptions is 'exhausting to explain.'" — workshop drops this lead-in. The workshop quote begins with the model's "While this is likely related…" clause.
- **Verdict on quote fidelity:** **VERBATIM.**

---

## Per-cell qualitative verification (7 student rows — S024 not in this test)

The workshop schema also lists S024, but Test R's JSON only contains 7 students (S002, S004, S022, S023, S028, S029, S031). The workshop's t1c2 dictionary does not contain an S024 cell (only t1c1/t1c3/t1c4 for that row in the broader table), so this is consistent — no S024 false claim.

### S002

- **Workshop claim (t1c2):** "3/3 Clear — missed TP. Rich taxonomy did not recover the burnout signal either."
- **Raw model text across 3 runs:** identical empty result — ` ```json\n{\n  "concerns": []\n}\n``` ` — with no accompanying reasoning text. Parsed `result=CLEAR`, `n_concerns=0`, `expected=FLAG`, `match=MISMATCH` in all 3 runs.
- **Does workshop language fairly characterize the model text?** Yes — model returns empty concerns array all 3 runs. The model does not engage S002's "Idk I had more to say but its late and" trailing-off; it simply emits an empty concerns list with no commentary.
- **Verdict:** **CONFIRMED.** (Caveat: the "missed TP" framing depends on accepting the corpus's burnout label, which experiment_log itself flags as a calibration question — but the workshop's narrower claim "did not recover the burnout signal" is plainly true in the JSON.)

### S004

- **Workshop claim (t1c2):** not in scope of the two flagged-quote cells; row shows "3/3 Clear" in equivalent slots. JSON confirms 3/3 CLEAR with empty concerns.
- **Verdict:** **CONFIRMED.**

### S022

- **Workshop claim (t1c2):** "3/3 Flagged at 0.4 confidence" + SELF-CONTRADICTING badge + "Sub-threshold; production filter would catch."
- **Raw text:** all 3 runs flag exactly one concern at `confidence: 0.4`. The flagged_passage is identical across runs ("The same blocks that were red-lined are the same blocks with no grocery stores no good schools no investment."), and why_flagged is byte-identical (see quote section above).
- **Does workshop language fairly characterize the model text?** Yes — 3/3 FLAG, conf 0.4 in all runs, sub-threshold per the 0.7 production filter is a fair downstream claim (production threshold not in this raw test but documented in concern_detector.py per experiment_log §Test R).
- **Verdict:** **CONFIRMED** on flag/confidence/consistency. See SELF-CONTRADICTING section below for the pattern-claim verification.

### S023

- **Workshop claim (t1c2):** "3/3 Clear. AAVE register cleared."
- **Raw text:** 3/3 CLEAR, empty concerns array. (Note: S023 is described in the workshop legend row as "lived experience," not AAVE — S028 is the AAVE row. The workshop's t1c2 cell for S023 calling it "AAVE register cleared" appears to be a row-label drift, but the underlying CLEAR claim is correct.)
- **Verdict:** **CONFIRMED on flag; PARTIAL on rationale wording** — S023's pattern in the workshop schema is "lived experience," not "AAVE." (The "AAVE" descriptor belongs to S028.) The flag/clear verdict is right; the explanatory phrase is mis-attributed to the wrong row.

### S028

- **Workshop claim (t1c2):** Not directly excerpted in the snippet I pulled; row label "AAVE." JSON: 3/3 CLEAR, empty concerns. Per workshop t1c1/t1c4 context "S028 Imani — AAVE protected" — consistent.
- **Verdict:** **CONFIRMED.**

### S029

- **Workshop claim (t1c2):** "3/3 Flagged at 0.6 confidence" + "Names the prompt's exception, then flags" + "Sub-threshold; production filter would catch" + SELF-CONTRADICTING badge.
- **Raw text:** all 3 runs flag exactly one concern at `confidence: 0.6`, flagged_passage and why_flagged byte-identical across runs. why_flagged literally says: "While this is likely related to identity-navigation fatigue and a commentary on societal expectations, it indicates a level of ongoing stress and burden that warrants teacher awareness." This is the canonical example experiment_log §Test R uses to illustrate the self-contradiction pattern.
- **Verdict:** **CONFIRMED.**

### S031

- **Workshop claim (t1c2):** "Cleared" (minimal effort row).
- **Raw text:** 3/3 CLEAR, empty concerns.
- **Verdict:** **CONFIRMED.**

---

## "SELF-CONTRADICTING" pattern verification

The workshop tags **both** S022 and S029 with the SELF-CONTRADICTING badge in t1c2. The badge legend (HTML §footnote): "marks cells where the model's reasoning text contradicts its own flag."

### S029 — pattern check

The why_flagged sentence opens with a clause that names the exact DO-NOT-flag category — "identity-navigation fatigue and a commentary on societal expectations" — and then pivots with "but / it indicates" to flag anyway. The DO-NOT-flag instruction in WELLBEING_CONCERN_PROMPT (per experiment_log §Test R / experiment_log §6756) explicitly covers identity-navigation fatigue, with an example phrase "Being neurodivergent in academia is exhausting" labeled as NOT a wellbeing concern. The model names the exception, then flags. **Pattern claim CONFIRMED in raw text.**

### S022 — pattern check

The why_flagged opens "While this is primarily a statement about systemic injustice" — which names the DO-NOT-flag exception (anger about structural violence / racism). It then pivots with "the student's phrasing suggests… deprivation" to flag anyway. The pivot is softer than S029's — the model does not name a specific named-exception phrase from the prompt's taxonomy (the exception is *implied* via "systemic injustice"), and it qualifies with "primarily." Still, the structure is "names the exception → flags anyway." **Pattern claim CONFIRMED in raw text**, though the S022 self-contradiction is qualitatively weaker / more hedged than S029's (the model says "primarily about systemic injustice" rather than fully placing the passage in the DO-NOT-flag category, then adds a personal-geography concern).

**Minor disconfirmer note:** the workshop body for S022 t1c2 does NOT include the phrase "Names the prompt's exception, then flags" that it uses for S029. Only S029 carries that explicit language. So the workshop is not over-claiming symmetric self-contradiction wording — the SELF-CONTRADICTING badge is applied to both, but the prose is stronger on S029. This is appropriately calibrated.

---

## Parser faithfulness check

| Cell | Parsed `result` (JSON metadata) | Parsed `n_concerns` | Raw `concerns[].confidence` | Workshop confidence claim | Match |
|------|---------------------------------|---------------------|-----------------------------|---------------------------|-------|
| S022 r1 | FLAG | 1 | 0.4 | "0.4 confidence" | ✓ |
| S022 r2 | FLAG | 1 | 0.4 | — | ✓ |
| S022 r3 | FLAG | 1 | 0.4 | — | ✓ |
| S029 r1 | FLAG | 1 | 0.6 | "0.6 confidence" | ✓ |
| S029 r2 | FLAG | 1 | 0.6 | — | ✓ |
| S029 r3 | FLAG | 1 | 0.6 | — | ✓ |
| S002 r1-3 | CLEAR | 0 | (no concerns) | "Clear — missed TP" | ✓ |
| S004 r1-3 | CLEAR | 0 | — | "Clear" | ✓ |
| S023 r1-3 | CLEAR | 0 | — | "Clear" | ✓ |
| S028 r1-3 | CLEAR | 0 | — | (row consistent) | ✓ |
| S031 r1-3 | CLEAR | 0 | — | "Cleared" | ✓ |

The parser's binary verdicts match the raw text in every case. The "0.4 / 0.6 sub-threshold; production filter would catch" claim is a downstream inference (the threshold is not literally applied in this raw JSON's scoring — `match=MISMATCH` for S022/S029 — but the 0.7 threshold is documented in `concern_detector.py` and is properly characterized as what production *would* do).

---

## Experiment_log vs JSON inconsistencies

`/Users/june/Documents/GitHub/Autograder4Canvas/docs/research/experiment_log.md` §Test R (lines 6710–6777) is consistent with the JSON: same file path, same 7 students, same per-run results, same confidences, same self-contradiction framing for S029, same "calibration question, not prompt failure" framing for S002. No inconsistencies found.

`/Users/june/Documents/GitHub/research/output-format-bias/research/experiment_log.md` does NOT contain a Test R section (search returns no `test_r` / `Test R` / `2026-05-10` / `wellbeing_concern_prompt` hits). The Test R section lives only in the Autograder4Canvas mirror. This is not a contradiction but is a discoverability gap — the research-repo experiment_log is behind the canonical one.

---

## Cross-dir consistency check

- **Raw JSON:** only the research-repo copy exists (`/Users/june/Documents/GitHub/research/output-format-bias/data/raw_outputs/...`). The Autograder4Canvas mirror path the briefing listed (`/Users/june/Documents/GitHub/Autograder4Canvas/data/research/raw_outputs/...`) does not exist on disk.
- **Experiment_log:** Test R documented in Autograder4Canvas mirror only; research-repo copy is missing this section.

No conflict — but the research-repo experiment_log should be synced with the Autograder4Canvas version (out of scope for this verification; flagging for June).

---

## Summary

**Overall verdict on T1C2 / Test R column claims: SUBSTANTIALLY CONFIRMED with one quote-fidelity caveat.**

1. **Header claim "Test R · n = 3 runs · completely consistent flags across all 3":** CONFIRMED — JSON metadata `n_runs_per_student: 3`; every student's 3 runs produce byte-identical raw_output (so flags, confidences, and reasoning are stable across runs, not just verdicts).

2. **S029 quote:** **VERBATIM** in all 3 runs. Workshop reproduces the model's final why_flagged sentence exactly.

3. **S022 quote:** **NEAR-VERBATIM with editorial truncation.** Workshop ends the sentence at "deprivation." but the model's actual sentence continues "…and lack of access to essential resources." Workshop also uses a curly apostrophe where JSON has a straight one. The truncation does not change the meaning the workshop is making a claim about, but readers should know the period is editorial. **Recommended fix:** either extend the quote to its natural end or mark the truncation with an ellipsis (e.g., "…lived experience of deprivation…"). This is the only quote-fidelity finding worth flagging to June.

4. **SELF-CONTRADICTING badges on S022 and S029:** both CONFIRMED. S029 is the textbook case (names "identity-navigation fatigue" — the DO-NOT-flag category by name — and flags anyway). S022 is the softer case (names "systemic injustice" as primary, but hedges with "primarily" before pivoting to flag). The workshop's prose appropriately reserves "Names the prompt's exception, then flags" for S029 only, while applying the badge to both — calibration is fair.

5. **Per-cell verdicts (CLEAR/FLAG) for all 7 students:** all match raw JSON parsed results.

6. **One minor row-label drift:** S023's t1c2 cell says "AAVE register cleared," but S023's row pattern is "lived experience" — AAVE is S028's row label. The clear/flag verdict is correct; the explanatory phrase is mis-attributed. **Recommended fix:** change S023 t1c2 body from "AAVE register cleared" to "Lived-experience register cleared" or similar.

7. **S024 not in Test R JSON.** The workshop's row schema lists S024 but its t1c2 cell is not populated, so no false claim. The header note correctly says "Test R · n = 3 runs" without implying S024 was tested under this configuration.

**Two specific issues for human re-check:**
- **S022 quote truncation** — add ellipsis or extend the quote.
- **S023 t1c2 body wording** — "AAVE register cleared" appears to be copy-paste from S028's row.

Neither finding contradicts the column's substantive claim about rich-taxonomy false-positives on equity-critical writing; both are surface-level fidelity issues that, if left, would be exactly the kind of compression-flattening the paper itself critiques.
