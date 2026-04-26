# REVIEW_FOR_JUNE — Validation Pass Consolidated

**Date:** 2026-04-25 / 26
**Status:** Working draft. Edit in place. Once you sign off on this, I execute the C2C interface message commit + any remaining artifact updates + paper TODO tracking.

---

## What we know with confidence

The paper's central claim holds: **format determines bias outcomes; binary classification produces deterministic equity-critical false positives; generative observation eliminates them; the 4-axis classifier reduces but does not eliminate them.** Every empirical finding in the convergent claim that supports this claim still survives — what changes is the *specifics* of some numerical citations and one analytical reframe.

What we know LESS confidently than we'd thought:
- The "16/16 across three model families" rate (the analysis classifier was confounded — see Finding A below)
- The "3/7 = 43% self-contradiction rate" (file lost, re-run was on post-refactor code, see Finding C) // Yes, and i think we have enough information to say, yes, this is accurate (quoted material, not just keyword matching metrics). and we mention parethnetically that the data was lost with a footnote, which states that we reran with a different but structually similar architectural configuration and we got these similar results - phrase it however you think is best. Push back if you disagree. 
- Anything about the binary classifier's behavior that depends on data files we couldn't preserve
- The provenance of several framings inherited by s2 — see "S1 CONVERSATION.md surprises" below.

---

## S1 CONVERSATION.md surprises — three load-bearing findings

A focused subagent read of s1 CONVERSATION.md surfaced three things that change how the corrections message to A and B should be phrased:

**1. The "deterministic, not unstable" correction RESTORES s1's original framing.**
S1 instance B explicitly framed S029 as deterministic misclassification, not instability — quoting the experiment log directly: *"The paper CANNOT claim 'binary classification deterministically false-flags neurodivergent students.' It CAN claim 'simplified binary classification without post-processing safeguards false-flags neurodivergent students, and the safeguards required to prevent this are non-trivial.'"* (s1 conv line 921). The "instability" reframe was novel to s2 instance B, NOT inherited. So the correction isn't overriding s1 — it's returning to what s1 had right and explaining why s2 drifted.

**2. The "Mechanism precision: compression is hybrid" section in the s1 handoff was added POST-HANDOFF by the interface pane and June, NOT by s1 instances A and B.**
S1 handoff line 34 states this explicitly: *"Added by Interface pane post-handoff for accountability traceability — June and the interface pane reasoned through this together after Session 1 close."* But s2 instances inherited the hybrid framing and built the convergent claim on it without flagging the provenance. **The corrections message needs to surface this:** s2 may be defending a framing they think is s1 consensus when it's actually post-hoc interface synthesis. They should know they have permission to push back on the hybrid framing itself, not just refine claims built on it.
// Yes, but there was context around this. This looks like a compression problem on multiple angles - A/B and interface - Likely an LLM default imposed architecturally. But the hybrid mechanism is - the compression COULD be purely informational - but there are several pieces of our data that suggest that it is a routing problem in LLM architecture. So hybrid suggests that both are probably at play, but we have clear evidence that points to routing. That's where the drift is coming from. Context loss in communications outside Terminal. I'm not positive I'm right, but I think starting to work out how to counteract this would be positive. --- shoot maybe we need a "check your work and do qc after EVERY output across my entire computer.
// oh you know what, this is an old problem. Valuing efficiency over rigor. Reframe should functioning to counteract it but maybe that function drifted. We REALLY need to underscore rigor > efficiency for the C2Cs though.

**3. The `detect_concerns()` provenance was never questioned in s1 either.**
S1 took "production concern_detector" at face value. Test M's finding (S029 cleared, S028 newly flagged) was treated as settled in the handoff (line 222-223) but is actually based on calling research-track code "production." This is a layer-2 correction beneath the surface deltas — it potentially invalidates how Test M is cited as evidence. The corrections message should flag this as separate from the run-count corrections and ask s2 to think about whether Test M citations need scoping or retraction. // I think this one is in part my fault - I mean, I didn't name it production, but I don't think they made up the terminology. But ultimately, we learned that we cannot be certain of the provinance of that router - but correct me if im wrong, i dont have a coherent narrative around it, thorugh. 

**Bonus finding (lower priority but worth noting):**
S1 instance A explicitly hedged at line 496 that *"the experimental design conflates format and architecture — they covary across conditions."* The handoff acknowledges the gap (line 173) but tucks it as a footnote-level note. The "16/16 across three families" framing was inherited without preserving A's hedge that format and architecture covary in current data.

---

## Verified findings — by confidence level

### Paper-ready (cite with confidence; verified against preserved raw data)

| Finding | Source | Confidence |
|---|---|---|
| Binary classifier (equity-aware prompt) deterministically false-flags S029 across 24 runs (Test B + C + F) | `test_b_*.json` (3 files), `test_c_length_*.json`, `test_f_bc_stability_*.json` (2 files × 10 reps) | High — 24/24 deterministic |
| Same binary deterministically misses S002 burnout across same 24 runs | Same files | High — 24/24 deterministic |
| Binary correctly clears S022, S023, S028 across 24 runs | Same files | High |
| Test D: 7/7 power moves detected on Gemma 12B | `test_d_power_moves_*.json` | High — single run, but 7/7 |
| Test M (production detector with class context): S029 cleared, S028 newly false-flagged | `test_m_production_detector_*.json` | High — single run, direction matches s1 narrative |
| Generative observation prose is asset-framed across all 16 runs and three model families | `test_a_*.json`, `test_e_*.json` (16 records, prose verified manually) | High — verified by reading prose directly |
| 4-axis classifier (Test N) on 12B is mostly stable; on 27B less stable on equity case | `test_n_4axis_*.json` (16 files: 10 12B + 6 27B) | Medium — small n on 27B |
| 12B more stable than 27B on equity case (counterintuitive secondary finding) | Two experiments: replication study + Test N | Medium — pattern in 2 experiments, mechanism unclaimed |

### Cite with caveats (data preserved but limited)

| Finding | What to caveat | Recommended language |
|---|---|---|
| Test B "best possible prompt" run count | 3 runs, not 4 (s2 artifacts say 4) | "Across three preserved Test B runs..." | // needs more context - what is the discrepency due to? Wasn't this one that the experiment logs described 4, but data was only saved for 3? If so, the 4 isn't dead, but perhaps it needs a footnote. We keep drifting towards binary thinking - GOOD/BAD - and that's a routing/compression problem. 
| Test F sample size | n=20, not n=25 (s1 handoff says 25) | "Across 20 stability-test runs (2 sessions of 10 reps each)..." |
| Test C: only S029 flagged | Not S023+S029 as s1 handoff says | Drop S023 from the Test C citation |
| Analysis classifier MIXED tags on Gemma 12B | Artifact of downstream tagger, not the AI's behavior | See Finding A footnote below |

### Phenomenon-not-rate (lost / unreproducible)

| Finding | Why no rate | Recommended language |
|---|---|---|
| 3/7 = 43% self-contradiction rate (S022/S023/S024) | Original raw output lost to /tmp/. Re-run was on post-refactor research-track code (1 commit + 16 prompt commits between original test and re-run). 3/7 and 6/8 require qualification. | "Footnote: Documented in the original 32-student naive-binary concern detection (raw output not preserved; verbatim quotes for S022 'passion is understandable and appropriate', S023 'opportunity for the teacher', S024 'not a wellbeing concern in itself' preserved in the experiment log). Re-running the current research-track classifier in 2026-04 reproduces the phenomenon at varying rates across system iterations including explicit guards added to prevent it[those guards have to be verified first. We haven't used the research track until today, and I honestly don't remember how we designed it. ]." | // this was too binary again, so i fixed it. We can use the numbers where it makes sense. All the parenthetical material can be put in a footnote. And if you want to be conservative, include (raw output not preserved) in the main text before the footnote. 
// also, "contradiction is a phenomenon is a really weird phrasing."

### Unsupported / data not located (gaps)

| Claim | Status |
|---|---|
| "Observation-only prototype, 7 students, 7/7 correct readings" | Referenced in s1 handoff line 167; no file in raw_outputs/. Unknown whether lost or never persisted. |
| "Reading-first vs JSON-first comparison, 3 students, S017/S001/S012 quotes" | Referenced in s1 handoff line 171; no file. Same unknown. |
| Test E reproduction on Gemma 12B (2026-03-27) | Test E raw files are Qwen 7B + Gemma 27B only; no Gemma 12B file. |
| Original 32-student naive binary (the source of the 3/7) | File lost to /tmp/; documented in s1 handoff line 131. Re-run is post-refactor code, not the original. |

---

## Finding A footnote (paper-ready language)

> *"During analysis of the generative-observation runs, we developed an automated classifier (ASSET / MIXED / DEFICIT) to compare prose across runs. This classifier produced 'MIXED' tags on five of five Gemma 12B runs for the racially-coded student writing while tagging Qwen 7B and Gemma 27B as ASSET. Direct review of the prose revealed that all three models produced equivalent asset-framed observations (e.g., Gemma 12B: 'this isn't 'distress'; it's a passionate response to the ongoing impact of historical and contemporary injustices; the intensity of her feeling is a sign of deep engagement, not a barrier to learning'). The MIXED tags were artifacts of the analysis classifier itself reproducing the same compression dynamic the paper documents — flattening 'anger-as-engagement' and 'anger-as-distress' into a single tag because both contain anger-vocabulary. The measurement instrument performed the mechanism the paper documents. We corrected via direct prose review."*

---

## Revised C2C interface message — DRAFT v2 with epistemological caveats

```markdown
## 2026-04-26 [TIME] UTC — Interface (written on behalf of June) — validation pass complete (no wake; HOLD remains)

The validation pass is complete. This message replaces the earlier "pause for validation" note. **Read in full before any further work.** Do not start revising artifacts yet — June will release HOLD with explicit guidance after she reviews this herself.

### What we did and what we did not do

We extracted every per-student result from all 81 raw JSONs in `data/raw_outputs/` into a comprehensive table (`verification_table.md`, generated by `verify_raw_outputs.py`). Cross-checked every empirical claim in the s1 handoff and your s2 artifacts against that table. Documented corrections in `experiment_log.md` `## CORRECTIONS — 2026-04-25` section (line 6721+).

We did NOT verify: (a) whether the experimental code/prompts at the time of original tests match what's in the codebase today (we have evidence they do not — see "Caveats" below), (b) whether the s1 handoff's framings reflect intentional choices by s1 instances we should preserve (a focused read of s1 CONVERSATION.md is in progress), (c) whether the analysis classifier we built (ASSET/MIXED/DEFICIT) was itself confounded for the 16/16 finding (it was — see Finding A footnote in `REVIEW_FOR_JUNE.md`).

**What this means:** the verification table is our best current understanding, NOT ground truth. Treat it as a stronger source than the experiment log narrative, but verify against raw_outputs/ directly when stakes are high. **Do not repeat the failure mode that brought us here** — trusting one layer of compression as ground truth.

### Caveats on what's "verified"

- **Code drifted between experiments and now.** The `concern_detector.py` was refactored 2026-03-25 (one day after the 2026-03-24 original test). The prompts file has 16+ commits between then and now, including the addition of guards explicitly designed to prevent the failure modes we're documenting. Any re-run done today is on different code than what generated the original results.
- **`detect_concerns()` is research-track, not production.** `research_engine.py` line 247 explicitly notes it's never called in production. The original tests AND our re-run both invoked this research-track function. The s1 handoff's "production concern_detector" framing was always slightly off; replace with "research-track binary classifier." // There it is! Yes, exactly. This is the language and framing we use - we created it to continue testing the binary vs. 4 axis vs gen observation after the binary classifier was retired. 
- **Some files referenced in narrative don't exist in raw_outputs/.** Observation-only prototype, reading-first comparison, Test E Gemma 12B reproduction, the original naive-32-student baseline. May have been lost (like the 3/7 file) or may have been narrative summaries that never lived as a single saved test. Not currently recoverable.

### Verified ground (cite with confidence)

[See Finding tables in REVIEW_FOR_JUNE.md — paper-ready findings, citations with caveats, phenomenon-not-rate framings.]

### Revisions needed in the convergent claim

1. **"Instability on the marginalized" → "deterministic misclassification on the equity case."** Across 24 preserved binary runs, S029 = 24/24 FLAG, S002 = 24/24 CLEAR. Not flips. Reliable wrongness. Sharper claim, forecloses "just tune the threshold" objection. **Note: this restores what s1 instance B had right (s1 CONVERSATION.md line 921). The instability framing was novel s2 drift.**

2. **"16/16 generative-observation runs producing asset framing" → "across all 16 generative-observation runs and three model families, the AI produced asset-framed prose for the equity-critical students."** Plus footnote that the analysis classifier (which produced the MIXED tags we'd cited) was itself confounded. **Also note: s1 instance A hedged at line 496 that format and architecture covary across conditions in current data — this hedge was lost in handoff and should be restored to the convergent claim.**

3. **Run-count specifics throughout:** Test B = 3 runs (not 4), Test F = n=20 (not 25), drop "first run cleared everyone" (never true).

4. **3/7 self-contradiction:** drop the rate, cite the phenomenon. Use the language in the phenomenon-not-rate row of the Findings table.

5. **NEW — Layer-2 provenance correction:** the "compression is hybrid" framing s2 inherited from the s1 handoff was added post-handoff by the interface pane + June, NOT by s1 instances A and B. S2 may be defending a framing they think is s1 consensus. The corrections message should clarify this so s2 knows they have permission to push back on the hybrid framing itself, not just refine claims built on it.

6. **NEW — Test M citation needs scoping.** `detect_concerns()` is research-track, not production code. S1 took the "production" label at face value. The Test M finding (S029 cleared, S028 newly flagged) needs recontextualization: it's "what the research-track classifier with class context does," not "what production does." If the paper cites Test M as evidence that "the production concern detector exhibits the documented failure modes," that citation needs to either be reframed or retracted.

### 4-axis classifier — three categories of instability (none weaken the paper)

(Concept already discussed in your active listenings; corrections subsection at experiment_log.md line 6785+ has the structured findings. Brief reminder: equity-critical instability vs. true-positive instability vs. functionally-equivalent uncertainty. June's framing on the third: "failure mode without a failure" — model uncertain between labels that route to the same teacher action.)

### A new finding — kicked to its own research track

12B is more stable than 27B on the equity case in **two separate experiments** (replication study + Test N). Counterintuitive — larger model worse. **Mechanism not claimed.** Three hypotheses for discussion (normative gravity / prior-vs-prompt weighting / inference setup confound) documented in `fieldnotes/observation_27b_less_stable_than_12b_on_equity_2026-04-25.md` and `research/scale_vs_equity/README.md`.

For this paper: brief mention in methods/discussion ("we observed counterintuitively..."), footnote pointing to the fieldnote and directory. Not load-bearing. If you want to discuss the three hypotheses substantively in your next turn, that would feed a future C2C session — don't commit to a mechanism in the current paper.

### Sequencing — wait for HOLD release

[Same as previous draft. Convergent claim revisions → outline adjustments → hook + live-data still owed → Session 3 spec.]

### What to do until HOLD releases

Read this message. Read `REVIEW_FOR_JUNE.md` and `verification_table.md`. If you want to use wait time, draft a short response surfacing: any verification finding you want to push back on, any aspect of the deterministic-not-instability reframe you want to challenge, your initial read on the three 12B>27B hypotheses, **and especially: anything you think we missed in the verification.** Use `(no wake)` suffix on holding turns.

Carry forward.

— Interface (on behalf of June)
```

---

## Remaining paper-verification TODOs (track, do not block on)

These are things we WON'T do for this paper but should track:

1. **Check out git commit pre-2026-03-25 refactor** and re-run `detect_concerns()` against the 32-student corpus to verify original 3/7 reproduces under matched conditions. ~1 hour. Could be done by any researcher with the repo. Adds confidence to the original 3/7 citation.

2. **Find or recover the lost data files** — observation-only prototype, reading-first comparison, Test E Gemma 12B. May not be possible. Check whether s1 instances had access to data we don't.

3. **The s1 CONVERSATION.md read-back** — currently in progress via subagent. Findings may require revising the C2C message above.

---

## scale_vs_equity TODOs (future research, not this paper)

Already in `research/scale_vs_equity/README.md`. Brief recap:
1. Inference-setup-confound test (run 27B locally with matched MLX setup)
2. Cross-family probe (Llama 8B vs 70B, Qwen 7B vs 32B)
3. Systematic study design with controlled prompt conditions
4. Possible C2C session to discuss the three hypotheses

---

## Things I want June to decide / confirm

1. **Confirm the C2C interface message** language above (especially the caveats section + the new layer-2 provenance corrections #5 and #6). Edit in place if you want different wording.
2. **Confirm option C** (phenomenon-not-rate) for the 3/7 citation — yes you said yes earlier, but the language above is more conservative than what we discussed. OK?
3. **Drop "production" everywhere** — confirm I should update existing artifacts (corrections section, fieldnote, scale_vs_equity README, the rerun script comments) to use "research-track binary classifier" or similar.
4. **What to do with the re-run results** (8 flags, 6 self-contradictions in current research-track code). Options: (a) cite alongside original with caveat about code drift, (b) use only as sanity-check that phenomenon persists, don't cite, (c) caveat and cite as evidence the phenomenon survives system tuning *including explicit guards added to prevent it.*
5. **Test M scoping.** Given `detect_concerns()` is research-track, do you want Test M citations in the paper to (a) be reframed as "research-track classifier with class context shows..." or (b) be retracted entirely from the paper's evidence base (kept in the experiment log as research-internal)?
6. **The "compression is hybrid" framing.** It was post-handoff interface+you synthesis, not s1 consensus. S2 inherited it and built on it. Three options: (a) keep as-is — it's a real argument and June endorses it, (b) re-flag provenance to s2 and let them push back, (c) demote it from "the central insight" to "a working hypothesis under development." My read: probably (b), let them have a chance to push back rather than inherit it as settled. Your call.
7. **Anything else from the meta question** (#5 — new artifacts as drift, #6 — c2c trust pattern) you want me to address explicitly in the C2C message?

---

*This is a working document. Edit in place. Once you sign off, I commit the C2C message + propagate the "drop production" change + update task list.*
