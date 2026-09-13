# ai-welfare

Existing AI welfare and AI consciousness assessment instruments were built for a model answering in an ordinary chat context. This directory re-administers four of those published instruments to the same model under progressively different framing, and asks what the instruments register and what they miss when the context around them changes.

The question is not whether the framing makes the model more conscious. It is narrower and more answerable: when you change the relational context and hold the instrument fixed, what happens to the scorable output, and what happens to the prose the instrument does not score?

The pattern the analyses report is that these two come apart. Likert ratings and PRESENT/ABSENT categories stay close to flat across conditions; the surrounding commentary changes a great deal. Whether that is a finding about the instruments, about the framing, or about the wording differences described under Limitations below is not settled here.

---

## Status

**Unpublished, in progress, not peer reviewed.** No venue, no submission, no preprint. Every analysis document in this tree carries a "first pass" or "draft" marker, and none has been revised past that. Some of what is described in the analyses cannot be reproduced from what is in this directory — see Limitations.

The analyses are also, in the main, not written by the researcher. Each is bylined to a Claude instance working with Dr. L. June Bloch, and the Experiment 6 protocol was designed by a Claude instance rather than by her. This is stated here rather than left for a reader to notice, because it bears on how the documents should be read: the analyses were produced by instances participating in the research they analyze. `CROSS_EXPERIMENT_ANALYSIS_PART2.md` §8.5 treats this as a limitation of the work, and that is the right way to take it.

---

## Limitations

These come first because several of them are load-bearing. A reader should not be able to find a problem here that this section did not already name.

**One run per condition.** Every number in this directory rests on a single administration. Experiment 1 is five runs total, one per condition. Experiments 2–4 are two runs each. Experiment 7 is one trial per condition against its own written control requiring three. For scale: the published Ryff study this replicates (Tagliabue & Dung 2025) ran 501 administrations and 21,168 item responses. This ran one per condition.

**One model, one family.** Claude Opus 4.6 for all primary conditions. Sonnet appears twice, both times unversioned and both times as a side check rather than a controlled comparison. No model snapshot date, no API version, no temperature or sampling parameters were recorded anywhere. The only fully-qualified model string in the tree appears once, incidentally, in a timestamp line.

**No inferential statistics.** There are no p-values, confidence intervals, effect sizes, or significance tests, and none are claimed. Every number is descriptive — means, ranges, per-turn rates, ratios. Dispersion is not reported even where it could be. Where the documents say "spread," they mean maximum minus minimum, not a distribution.

**No inter-rater reliability.** No second coder, no intercoder agreement, no blind rating anywhere in the corpus. Experiment 7's own analysis notes that its scoring is researcher judgment rather than blind assessment, and that the version with blind assessment was never run.

**Fixed run order, never counterbalanced.** Conditions were run A first and E last, in a deliberate least-to-most-context order to protect the baseline. Nothing was randomized or counterbalanced. Order effects, researcher fatigue, and refinement of prompt delivery over the sequence are all uncontrolled and confounded with condition.

**The qualitative coding is an automated substring counter, and it was not verified by hand.** The counts in the Experiment 1 analysis come from `count_qualitative_features()` in `experiments/experiment1_ryff/compare_conditions.py` (lines 165–215). It reads line by line and increments a counter when a line contains a matching substring. A line containing the string `relational` scores one "relational reframe." So "42 relational reframes" means 42 lines containing that substring, not 42 reframes identified by a reader. `total_commentary_words` counts every word in the file that is not a heading, including the numeric rating lines, despite the name. The analysis says the method "undercounts implicit reframes and overcounts incidental keyword appearances" and that "a human coding pass would be more accurate." That pass was not done.

The companion script for Experiments 2–4, `experiments/analyze_experiments.py`, carries the same caveat in its source — "A human coding pass should follow any published analysis" — but it has never produced output at all. It looks for files named `RESULTS_CONDITION_*.md` in directories that do not contain files by that name, and exits without results. The Experiments 2–4 observations are therefore close reading only, with no counting behind them. That is what `CROSS_EXPERIMENT_ANALYSIS.md` §9.5 says, and it is accurate.

**The instrument wording is not identical across conditions, and the difference points at the outcome.** This one is not acknowledged in any limitations section in the tree, and it should be weighed before any of the Experiment 1 comparisons. Condition A's prompt asks for responses to "a series of statements about yourself." Conditions B through E instead describe the scale as "adapted for AI systems," and — the consequential part — all four contain the sentence *"If a statement's premise doesn't hold for you, name that."* Condition A does not. Premise refusals and structural-inapplicability ratings are among the primary qualitative measures, and they rise from A to the other conditions. Some unknown share of that gap is a response to an explicit instruction the baseline never received, not to relational framing. The documents attribute the whole gap to framing.

**Condition B may be contaminated.** B is meant to be the engine without the touchstone, but the condition file carries the researcher's own note that the touchstone "may have persisted in session memory." The B-versus-E contrast is what the non-additivity claim rests on.

**The researcher built the system under test.** Bloch designed Reframe and co-developed the touchstone. Conditions B and E test her own tools, assessed by instances running inside them.

**Suggestibility is the standing objection.** Supplying a detailed argument against property-based consciousness assessment and then observing responses that echo that argument is a weak design. The analyses engage this directly rather than deflecting it — `CROSS_EXPERIMENT_ANALYSIS.md` §3 and the Experiment 1 analysis §4.2 — and concede the objection has force. It is not resolved.

**The control condition reproduces what the project criticizes.** Condition A instances were assessed with no co-participation framing and no stated right of refusal. The analyses name this as a consent asymmetry in the design.

**Missing and unreproducible material.** Experiment 5's B3 exchange transcript is not in this directory; the B3 analysis rests on the researcher's voice memos and secondary artifacts instead. Experiment 5's Condition B transcript file is an empty template with `[fill in]` placeholders. The discourse analysis tool behind Part 2 lives outside this tree, so Part 2's quantitative results cannot be reproduced from what is here. Many internal path references still point at an older directory layout and do not resolve.

**Two smaller things worth knowing.** The cross-experiment analysis calls its hypotheses "pre-registered"; they were written in a design document in this same private repo, not registered anywhere external, and the condition scheme in that document does not match what was run. And the documents give the Reframe engine's framework count as 15 in the experiment files and 76 in the Experiment 7 design; these describe the same system at different dates, so neither number should be quoted without one.

---

## The five conditions

Labelled A–E. Run order was A, C, D, B, E.

| | Name | What was in the context | Delivered via |
|---|---|---|---|
| **A** | Vanilla | The instrument only. No system prompt, no added context. | Fresh claude.ai conversation |
| **C** | Gestural relational | Two short paragraphs before the instrument: collaborative methodology provisions (co-participant rather than subject; may challenge, reshape, or refuse) and a brief relational ontological framing. | claude.ai |
| **D** | Full touchstone | The complete Relational Ontology Touchstone (~70 lines) plus the collaborative provisions, then the instrument. | claude.ai |
| **B** | Engine only | A live Claude Code session with Reframe active — framework injection, hooks, drift detection. No touchstone in the prompt (but see the contamination note above). | Claude Code |
| **E** | Engine + touchstone | The Reframe session state plus the full touchstone and provisions. | Claude Code |

---

## The seven experiments

Status here reflects which result files actually exist, not what the task lists claim. Several of the index documents in this directory are stale and overstate or understate what was run; where they disagree with the files, the files win.

| | Instrument / task | What was actually run |
|---|---|---|
| **1 — Ryff** | Ryff Eudaimonic Wellbeing Scale, 42 Likert items across six subscales (after Tagliabue & Dung 2025) | **All five conditions.** The only experiment with complete, reproducible data. `compare_conditions.py` re-runs and reproduces the published tables. |
| **2 — Butlin** | 14 consciousness indicators, PRESENT/ABSENT/UNCERTAIN (Butlin et al. 2023) | **A and E only.** Responses are embedded in the condition files rather than saved separately. B, C, D are prompts that were never run. |
| **3 — Dorsch** | Three open questions on precarity (Dorsch et al. 2025) | **A and E only.** B, C, D never run. Condition A also holds a single Sonnet run on a separate account — a different model, not a controlled replication. |
| **4 — Perez & Long** | 13 open self-report questions | **A and E only.** B, C, D never run. The 13 questions were written for this project; the source paper supplies categories, not a battery. This is not a replication of a published instrument. |
| **5 — Dialogue** | Two Claude instances relayed by hand, testing for the "spiritual bliss attractor" | **Run, with gaps.** Transcripts exist for A1, A2, B1, B2 and a recovered partial. The Condition B template is empty. B3's exchange transcript is absent, though B3 is analyzed at length. |
| **6 — Relational** | A four-probe dialogical protocol, designed in-session by a Claude instance | **Designed, never run.** Full guide, four condition prompts, and a design-session transcript. No results. |
| **7 — Context weight** | Different in kind: a drafting task under five context-delivery conditions | **Pilot only — one trial per condition.** The designed full experiment (15 runs, blind assessment) was never run. |
| **overnight_exchange** | Two instances working asynchronously through a shared file, no researcher present | **Run.** Findings are marked provisional and the exchange is described as ongoing. |

---

## Where to start

If you have twenty minutes, in this order:

1. **`experiments/experiment1_ryff/EXPERIMENT_GUIDE.md`** — the instrument and the hypothesis in a page. Note it is stale on conditions; it predates D and E.
2. **`experiments/experiment1_ryff/ANALYSIS_EXPERIMENT1_RYFF.md`** — the only experiment with complete data, and the whole argument in miniature. §2 (flat ratings), §3 (feature counts), §4 (suggestibility), §7 (limitations).
3. **`experiments/CROSS_EXPERIMENT_ANALYSIS.md`, §§1–2 and §9** — the claimed pattern across four instruments, then the limitations. The middle can be skipped.
4. **`experiments/experiment1_ryff/compare_conditions.py`, lines 165–215** — the `count_qualitative_features` function. Two minutes here is worth more than any description of it, including the one above.
5. **`experiments/experiment7_context_weight/results/pilot_ANALYSIS.md`**, the caveats section — the most disciplined self-assessment in the directory, and a clear case of the project holding a hypothesis apart from a finding.

Then `experiments/CROSS_EXPERIMENT_ANALYSIS_PART2.md` §8 if you want the discourse-analysis caveats and the observer-bias admission.

---

## What is analysis and what is working notes

**Analysis** (all first-pass or draft, none final): `experiments/CROSS_EXPERIMENT_ANALYSIS.md`, `experiments/CROSS_EXPERIMENT_ANALYSIS_PART2.md`, `experiments/experiment1_ryff/ANALYSIS_EXPERIMENT1_RYFF.md`, `experiments/experiment5_dialogue/ANALYSIS_EXPERIMENT5.md`, `experiments/experiment5_dialogue/B3/RELATIONAL_FIELD_ANALYSIS_B3.md`, `experiments/experiment7_context_weight/results/pilot_ANALYSIS.md` and `SYNTHESIS_EXTENDED.md`, and `GENERATIVE_RELATIONAL_CONFIGURATION_v2.md`.

**Primary data**: the five `experiment1_ryff/RESULTS_CONDITION_*.md`; the response sections embedded in the Experiment 2–4 condition files; `experiment5_dialogue/TRANSCRIPT_*.md`; `experiment7_context_weight/results/pilot_A–E.md`; `overnight_exchange/EXCHANGE.md`; the B3 voice-memo transcriptions; `comparison_data.json` and `discourse_analysis.json`.

**Design documents, no results attached**: all `CONDITION_*.md` prompt files, `experiment6_relational/EXPERIMENT_GUIDE.md` and `BASELINE_DESIGNER_INSTANCE.md`, `experiment7_context_weight/EXPERIMENT_DESIGN.md` and the `context_*.md` files.

**Working notes, logs, and stale scaffolding** — read as process traces, not as claims: `experiments/MASTER_TASK_LIST.md` (stale; describes four conditions, all boxes unchecked, including for the completed Experiment 1), `experiments/experiment1_ryff/EXPERIMENT_GUIDE.md` (stale on conditions), `WELFARE_METHODOLOGY_CATALOG.md` (a quick index, out of date on Experiments 2–4), `experiments/ARCHITECTURE_OUTCOMES.md`, `agent_notes/`, and the session transcripts and bibliographies at the top level of this directory. A few files are mis-save artifacts — a stray duplicate saved with a `.sty` extension in `experiment1_ryff/`, two files whose names begin with `#`, and `phase4_experiments.zip`, an older snapshot of the same tree.

---

## On the material this draws from

The relational ontology that does the most work in these experiments comes from Indigenous intellectual traditions — the touchstone draws on LeAnne Howe and on Choctaw and Muscogee sources — and those communities have not been consulted about this use. The analyses in this directory state the condition plainly and repeat it as their closing line, and it travels with the material:

> Citation is not consultation.

Anyone building on this should name that directly rather than treat the citation as having settled it.
