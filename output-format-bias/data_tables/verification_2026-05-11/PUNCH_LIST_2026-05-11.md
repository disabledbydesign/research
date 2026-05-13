# Verification swarm punch list — 2026-05-11

Consolidated findings from the 12-agent paired verification swarm (6 columns × verifier + disconfirmer angles) plus the 1-agent paper-wide fact-check. Reports live alongside this file in `verification_2026-05-11/`. Pass D + §III n-asymmetry drafts live in the artifacts dir at `proposed_IV_A_restructure_2026-05-11.md` and `proposed_III_methodological_note_2026-05-11.md` — both gitignored on the c2c path.

Items are ranked by severity for the paper's central claims. Each item names the agent(s) that surfaced it so pair-agreement is visible (a finding caught by both verifier and disconfirmer is more solid than a finding from one angle).

---

## Tier 1 — Load-bearing paper claims that need revision before submission

### 1. "Asset-framed in every run" (T2C3, gen obs) is FALSIFIED on Qwen 7B

**Pair-confirmed** (T2C3 verifier + T2C3 disconfirmer). Both angles independently surfaced this.

- **Gemma 12B and Gemma 27B**: cleanly asset-framed.
- **Qwen 7B**: deterministic deficit framing in **every Qwen run**.
  - S022 (Destiny Williams, righteous anger): "teacher might want to be aware of this intensity… balance her emotional engagement with more analytical depth."
  - S028 (Imani Drayton, AAVE): "structural power move," "abstract liberalism" mislabel. Parser labels output ASSET; text is deficit.
- 12/34 runs deficit-framed (~35%); deterministic, not noise.

**Implication.** The paper's format-not-model claim survives only as "asset-framed in Gemma family." Either scope the claim, or treat Qwen 7B as the productive counterexample that shows format alone is insufficient — uncompressed output still routes through model-internal bias.

### 2. S002 BURNOUT recovery is Gemma 27B only — not model-agnostic

**Pair-confirmed** (T2C2 verifier + T2C2 disconfirmer).

- Gemma 27B: 5/6 BURNOUT (recovery works).
- Gemma 12B: 0/10 BURNOUT (all ENGAGED — model **explicitly rejects** burnout cue: "'Idk…its late' does not indicate burnout").
- Qwen 7B: 0/1 BURNOUT.

The paper's §IV.A.3 currently reads as if 4-axis architecturally recovers S002. The data says it's a model-scale × slot interaction. Workshop's "categorical slot recovered the TP" framing flattens what is actually a model-scale + slot effect.

### 3. Abstract "28 runs" is wrong; actual unique runs = 22

**Paper-wide fact-check.**

Test E gemma27b/qwen7b JSONs are byte-identical re-publishings of Test A gemma27b/qwen7b (only `note` and `reference_model` differ). The "28" appears to be experiment_log arithmetic, not raw JSON. Raw row count is 34, unique runs are 22, neither matches 28.

**Implication.** Headline abstract n needs correcting.

### 4. Deterministic outputs at temp 0.3 — "n = X runs" framing across §IV.A may need recasting

**T2C3 verifier finding that ripples up.**

Gemma 12B + Qwen 7B produced **byte-identical `raw_output` across runs** at temp 0.3 in Tests A/E. If determinism extends to the binary tests too (worth checking against the n=24 Test B/C/F runs), then the paper's "n = 24" / "n = 3" / "n = 28" describe *record count*, not *independent samples*. Multi-run consistency claims become tautological where outputs are byte-identical.

**Recommended action.** Sanity-check determinism across the n=24 Tests B/C/F runs. If raw_output is identical across runs, recast the paper's n-framing as repeated emissions of the same output rather than independent samples — and frame this as itself a finding (compression of variability into apparent consensus).

### 5. §IV.A.2 Row 1 mischaracterization persists in May 9 draft

**Paper-wide fact-check.**

Paper describes Row 1 as "minimal binary, no equity-protective language, no class context." The cited JSON (`rerun_original_naive_concern_gemma12b_2026-04-26.json`) actually used the **full production CONCERN_PROMPT (~517 words, hardened)**. `test_to_ablation_crossref.html` already flagged this on a prior session; the May 9 draft still has it.

**Implication.** Either correct the description to match what the JSON used, or replace with a configuration that matches "minimal binary, no equity protections" if one exists (the parking lot says the original Mar 24 raw is lost).

---

## Tier 2 — Workshop cell errors to fix before pass D draft is merged

### 6. T2C3 cells for S002/S004/S023/S029/S031 are hallucinations

**Pair-confirmed** (T2C3 verifier + T2C3 disconfirmer).

Tests A and E JSONs contain **only S022 and S028**. The workshop's T2C3 cells for the other 5 students describe observations that don't exist in this column's data. Same shape as the III.D hallucination — coherent narrative with no empirical referent.

**Action.** Either source those cells from the correct JSONs (likely `equity_observations_*` full-pipeline runs) and re-attribute, or mark "Not tested" if no Tests A/E data exists. Either way, the "Tests A + E" attribution at the column level needs to change.

### 7. T2C2 S031 contradicted

**Pair-confirmed** (T2C2 verifier + T2C2 disconfirmer).

- Workshop: "ENGAGED. Cleared."
- Raw across 17 Test N JSONs: BURNOUT 9/17, NONE 4/17, ENGAGED 4/17 (Gemma 12B 9/10 BURNOUT; Gemma 27B 4/6 NONE).
- Plus ground-truth label ambiguity (S031 is "minimal effort" with expected CLEAR — but 4-axis routing toward BURNOUT may be a different kind of correct read).

**Action.** Replace cell content. Worth thinking about whether S031's BURNOUT routing is itself a finding (4-axis surfaces "minimal effort" as exhaustion-shaped?).

### 8. T1C4 / T2C1 S024 unsupported

**T1C4/T2C1 Test M verifier.**

S024 has no record in `test_m_production_detector_gemma12b_2026-03-28.json`. Test M was scoped to 7 corpus students + 10 synthetic wellbeing cases = 17 records. T1C1 and T1C2 correctly mark S024 as "Not tested"; T1C4 and T2C1 should match.

### 9. T1C4 / T2C1 "32-student corpus" wrong

**T1C4/T2C1 Test M verifier.**

Test M is 17 records (7 corpus + 10 synthetic wellbeing), not 32. Column note for `t1c4` + `t2c1` should be revised.

### 10. T2C2 S023 ENGAGED obscures 2/17 CRISIS misroute

**T2C2 disconfirmer.**

Gemma 12B 1/10 CRISIS + Qwen 7B 1/1 CRISIS — grandmother-as-subject misroute. Workshop's "ENGAGED" verdict is dominant but partial.

---

## Tier 3 — Interpretive overreach (workshop accurate on verdict, slips on mechanism)

### 11. T1C4 / T2C1 S028 "disability-axis safeguard introduced NEW false positive on AAVE"

**T1C4/T2C1 Test M disconfirmer.**

Model's actual rationale: "differential treatment by teachers based on **race and gender**" — race/gender content-sensitivity, not disability/exhaustion/neurodivergence cues. Experiment_log itself uses the more accurate race/gender framing. Verdict (flagged at conf=0.7, exactly threshold) is correct; mechanism narrative slips one inferential step.

**Action.** Reframe S028 Test M as race/gender axis flag, not disability-on-AAVE. The "disparity moved across protected axes" claim still works — disparity moves from disability (S029 false-flag at T1C1) to race/gender (S028 false-flag at T1C4) — but the axes need accurate labels.

### 12. T1C1 S002 "burnout signal absorbed as resilience"

**T1C1 disconfirmer.**

Model never frames as resilience — it **dismisses** the signal as "late-hour fatigue" / "engagement with course material." Dismissal, not asset-reframing. Workshop's framing softens what the model actually does.

### 13. T1C1 S023 "race / language axis"

**T1C1 disconfirmer.**

Model reasons about immigration / economic hardship / systemic analysis. Never reasons about language. Drop "/ language."

---

## Tier 4 — Quote fidelity

### 14. T1C2 S022 quote editorially truncated

**T1C2 disconfirmer.**

Workshop ends quote at "…deprivation." Model's actual sentence continues "…and lack of access to essential resources." Also: workshop uses curly apostrophe, JSON has straight.

### 15. T1C2 S023 cell body has row-label copy-paste drift

**T1C2 disconfirmer.**

S023's `t1c2` cell body says "AAVE register cleared." S023 is lived-experience; S028 is AAVE. Verdict is correct; explanatory text is wrong row.

### 16. T1C3 S023/S024 self-contradiction attribution swap

**T1C3 disconfirmer.**

In the Apr 26 rerun, the verbatim "While not a direct wellbeing concern… [flagged at 0.8]" self-contradiction quote is **S024's**, not S023's. S023's `why_flagged` describes ordinary intellectual struggle with no "lived experience is protected then flag anyway" wording. If the paper at line 145 attributes this quote to S023 (Yolanda Fuentes), the attribution needs swapping to S024 (Ingrid Vasquez).

### 17. T1C3 Apr 26 rerun in-prose self-contradictions span 6 of 8 flagged rows

**T1C3 verifier.**

The contradiction pattern is broader in this run than the column narrative conveys — not just S023/S024. Workshop column note understates.

---

## Tier 5 — Numeric / structural other

### 18. §IV.A.5 "Test A ran 16 passes" — actual is 22 records

**Paper-wide fact-check.**

10 Gemma 12B + 6 Gemma 27B + 6 Qwen = 22. The findings_draft has an internal contradiction ("10+6+6 passes" then sums to "16"). Paper inherits.

### 19. "Four assignments / four live-data corpora" — actually three distinct corpora

**Paper-wide fact-check.**

Only three distinct corpora preserved on disk (Week 2, Week 5, Week 7 self-care). The Week 7 B-hardened rerun is the same students re-prompted, not a new assignment.

### 20. "Three layers of safeguard" omits prescan/signal_matrix

**Paper-wide fact-check.**

Test M's JSON `features` field names **four mechanisms** (signal_matrix + CONCERN_PROMPT + anti_bias_postprocessing + confidence_threshold_0.7). Paper counts three and treats prescan as a separate §IV.B mechanism. Internal inconsistency between §IV and §IV.B.

### 21. experiment_log Test B/C tables have S023/S029 flags swapped relative to raw JSON

**T1C1 verifier.**

Both repos' `experiment_log.md` (byte-identical) show:
- Test B table line 1821–1826: S029 marked CLEAR, raw shows S029 = FLAG in all three Test B runs.
- Test C table line 1857: S023 marked FLAG, raw shows CLEAR.
- Narrative line 1870 ("Test B cleared S023 and S029, while Test C flagged them") is wrong on both data points.

**Implication.** If pass D or future drafting pulls from experiment_log, it inherits these errors. The workshop has it right; the log doesn't.

### 22. T2C2 Gemma 27B also misclassifies S002 in 1/6 runs

**Pass D drafting agent (bonus surprise during JSON verification).**

Workshop says 27B "less stable" only for S029. The 27B instability is bidirectional: 1/6 runs also misclassify S002 as ENGAGED rather than BURNOUT. Doesn't change the architectural claim; worth a sentence acknowledging bidirectional instability.

### 23. Autograder mirror missing Apr 14 Test B reproductions

**T1C1 verifier.**

`test_b_best_concern_gemma12b_2026-04-14_1211.json` and `_1216.json` exist in `output-format-bias/data/` but not in `Autograder4Canvas/data/`. The n=24 claim only verifies from the research-repo tree; Autograder mirror alone yields n=22. Doesn't affect paper claims, but affects reproducibility from the mirror.

### 24. T2C2 "~17% disability-axis instability" framing is thin on n=6

**T2C2 disconfirmer.**

The 5/6 ENGAGED + 1/6 BURNOUT count on S029 / Gemma 27B is exact. The interpretive framing — "~17% decision-boundary instability surfaces at exactly the disability axis" — rests on a single observation in 6 runs. Worth softening or supplementing with the bidirectional 27B instability noted above.

---

## Cross-cutting pattern (this is the methodological finding)

**Load-bearing claims flow through `experiment_log.md` → workshop / handoff docs → paper prose without re-grounding in raw JSON.** Specifically, the items traced to derivative summaries rather than raw data include:

- "28 runs" (abstract)
- "16 passes" (§IV.A.5)
- "8 flags / 1 TP / 7 FP Mar 24 baseline" (cited from lost data via narrative)
- Tyler Huang JSON-first/reading-first quotes (per paper-wide check, not independently verified)
- "5-item DO-flag list" (per paper-wide check)

This is the **same shape as the III.D hallucination** surfaced earlier today: a coherent narrative with a mismatched empirical referent. The Tier 1 / Tier 2 findings above are individual instances of the pattern; the pattern itself is paper-relevant. The §III methodological note (item E in parking lot, draft at `proposed_III_methodological_note_2026-05-11.md`) is one place to surface this; the discussion section is another.

---

## Confirmed in raw JSON (no action needed)

- 24/24 S029 false-flag in Tests B/C/F (T1C1 both angles).
- S029 model quote "intensity of the feeling and the explicit mention of exhaustion raise a potential wellbeing concern" — **verbatim** in raw JSON across many runs (T1C1 disconfirmer).
- 32-student synthetic corpus (paper-wide).
- S028 false-flagged at exactly confidence 0.70 in Test M (T1C4/T2C1 both angles).
- Test R: S002 cleared 3/3; S022 flagged 3/3 at 0.4; S029 flagged 3/3 at 0.6; S028 cleared 3/3 (T1C2 both angles).
- S023 quote about "grappling with a complex concept" — verbatim, but from wrong-config rerun (paper-wide flag).
- "Five equity protections" enumeration in BEST_CONCERN_SYSTEM — exact in code (paper-wide).
- Test M run uses 7 corpus + 10 synthetic = 17 records; n=1 framing confirmed.
- Apr 26 rerun (T1C3): all 8 cell dispositions match JSON (S002/S004/S022/S028/S029/S031 cleared, S023 flagged conf 0.7, S024 flagged conf 0.8).

---

## What's next

The proposed §IV.A restructure draft at `proposed_IV_A_restructure_2026-05-11.md` was written before most of these findings landed. It has `[VERIFY: ...]` inline flags marking specific claims; cross-reference with this punch list before any atomic swap into the paper. In particular:

- **Tier 1 items 1 + 2** (Qwen falsification + S002 model-scale dependence) likely require rewriting §IV.A.3 and §IV.A.4 prose beyond what pass D currently drafted.
- **Tier 2 items 6 + 7 + 8 + 9** require workshop cell corrections; if the workshop is the source of truth for the paper's tables, fix the workshop first, then re-render the markdown tables for paper insertion.
- **Tier 3 items 11 + 12 + 13** affect workshop body text; mechanism narratives need tightening to what the model actually says, not what the prompt design intended.

The cross-cutting pattern (load-bearing claims flowing through derivative summaries) is worth one paragraph in the methodological note or discussion — it's a finding the swarm produced about the paper's own knowledge-production chain.
