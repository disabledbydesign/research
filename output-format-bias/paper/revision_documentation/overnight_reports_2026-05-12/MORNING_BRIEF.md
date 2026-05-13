# Morning Brief — 2026-05-12

**For:** June. Four overnight reports landed. This brief sequences them so you can move without rework.
**Deadline:** REE submission 2026-05-20 (8 days).

---

## TL;DR (read this first)

Four agents produced four reports, all in this directory with the `_2026-05-12` suffix:

1. `crossref_verification_2026-05-12.md` — 2 broken refs, 6 minor
2. `citation_resolution_report_2026-05-12.md` — 3 placeholders filled, 5 tentatives resolved, 4 author-name errors caught
3. `williams_restructure_proposal_2026-05-12.md` — 481 words saved across 30 paragraphs in §IV+V
4. `ree_submission_checklist_2026-05-12.md` — APA-7 already in use, anonymization is the big task

**The single most important fix:** Line 196 in §IV.B. Three reports converge on this one paragraph (see "Stacked Fix" below). Start here.

**The single biggest open question:** Word count. You're ~3,000 over the likely REE cap. Williams gets you ~500. Anonymization is content-preserving. **You'll need additional structural compression beyond what's in scope tonight.** See "Word Count Gap" below.

---

## 🔴 Stacked Fix: Line 196 (§IV.B¶2)

This one paragraph is touched by three of the four reports. Don't accept any of them in isolation — they have to land in order.

**Current state of line 196:**
> *One assignment was a deliberate stress test: the topic was self-care (CITATIONS NEEDED), following the class-wide burnout/academic dishonesty pattern mentioned above.*

**Three problems stacked on it:**

| Layer | What's broken | Report |
|---|---|---|
| 1. Antecedent | "the class-wide burnout/academic dishonesty pattern mentioned above" — no earlier passage establishes this pattern. Same shape as the III.D hallucination from 2026-05-10. | crossref | // that's a reference to the week 5-7 burnout/self care practice/self care theory process described int he intro. should be clearer.
| 2. Citations | `(CITATIONS NEEDED)` for self-care lit. Candidates: Lorde 1988 (*Burst of Light*); Kim & Schalk 2021; Ahmed 2017. | citations | // this is an undergrad course. lorde. Chen et al's critique of work. Cite the Nap Project (may not be the exact name). if you want other citations, i can look and see what i actually assigned
| 3. Compression | Williams proposes a 12-word fusion of the next two sentences. | Williams | // missing context for me to assess. 

**Fix order:**
1. Either expand §I.21 to name the cheating-as-burnout pattern as a referenceable phenomenon, OR rewrite line 196 to introduce the context inline (recommend the latter — smaller change, same effect)
2. Insert the citations into the now-stabilized sentence
3. Apply the Williams compression on the stabilized text

---

## Sequenced Work Order

Order matters here. Format conversion should happen last — content keeps shifting underneath it.

### Step 1 — Content fixes (do these first)
- [ ] **Line 196 stacked fix** (above) — 30 min
- [ ] **Line 97 "tests A–F" range** — Test D doesn't exist; Tests A/E belong to generative observation, not anti-bias calibration. Either enumerate ("tests B, C, F, M") or rewrite to separate the two tracks. 15 min // i dont think we explain the lettered tests, do we? should we just cut the reference? 
- [ ] **Test M naming** — rename to Test G or add a footnote on the naming convention. 5 min // this would involve a full sweep to surface ALL tests we ran in autograder, which may live here or in autograder's repo. But i dont want to rename because that will create variance with the actual autograder records we used for development. 
- [ ] **Crenshaw 1991** — cited in V.B line 222 but missing from References. Either add the entry (*Mapping the Margins*, Stanford Law Review 43(6), 1991) or drop the "; 1991" from V.B. 5 min // yes add. 

### Step 2 — Citation work // are these new citations we're adding? if so, what does each argue and how are we adding them>
- [ ] **Insert 3 placeholders** with the candidate citations (full details in citation report)
  - Line 23: Selbst (2019) + Hoffmann (2019) — iterative-calibration critique
  - Line 75: Annamma, Jackson, & Morrison (2017) is **load-bearing here — it's in REE itself.** Pair with Leonardo + Bonilla-Silva. Venue fit gold.
  - Line 196: Lorde 1988 + Kim & Schalk 2021 + Ahmed 2017 (lands during Step 1)
- [ ] **4 in-text author-name corrections** (citation agent caught these beyond brief):
  - Liu first initial Y → Z (Zhaohan Liu) — lines 236, 316
  - Chinta "Quy, T. L." → "Le Quy, T." (Vietnamese family-name component)
  - Xu year: pick 2025 or 2026 (currently inconsistent), and fix paraphrased title to "BiasFreeBench: A Benchmark for Mitigating Bias in Large Language Model Responses"
  - **Annamma "Jett" → "Jackson" (Darrell D. Jackson)** — memory slip, verify against published version of record before citing

### Step 3 — Williams compression review
- [ ] **27 of 30 restructures are clean accepts.** Bulk accept these.
- [ ] **3 need your judgment, not auto-accept:**
  - **IV.A.6**: "does not reappear under generative observation" → "disappears under generative observation." Compression but loses precision — *reappear* implies it appeared in the calibrated binary then doesn't return; *disappears* reads as binary on/off. Your call. // not sure
  - **V.A¶3**: "argue correctly" → "argue." Williams treats *correctly* as endorsement scaffolding, but it also signals your stance with critical AI scholars. Drop or keep? // drop
  - **V.A¶3**: "simplistic measurable categories" → "measurable categories." *Simplistic* is doing critical analytical work, not redundant with *measurable*. Recommend keeping *simplistic*. // keep

### Step 4 — Anonymization (biggest single task)
- [ ] **Decide:** Option A (strip institution + Watsonville/Santa Cruz/Pajaro Valley locators, keep autoethnographic positionality voice, third-person Bloch 2026 self-cite) or Option B (email REE editor to ask about flexibility for autoethnographic work). REE checklist recommends A given timeline. // why is this important? The student data is synthetic. 
- [ ] Strip named institution → "a California HSI community college" // when do we ever name the institution?
- [ ] Move author name, affiliation, ORCID to separate title-page file
- [ ] Third-person self-cite for Bloch 2026
- [ ] Spot-check §III.A passages that name specifics

### Step 5 — Word count compression (the gap)
See "Word Count Gap" section below — this is where Step 5 takes most of the time.

### Step 6 — Format conversion (last)
- [ ] Verify on REE's live IFA page: abstract cap, word-count cap, double vs. single anonymized, structured abstract requirement, keyword count (5 [VERIFY] items, ~5 min)
- [ ] Trim abstract from 213 → 200 words if cap is 200 (13 over) // hold off on this, i need to do that by hand. 
- [ ] Markdown → .docx via pandoc // hold off here - i'll ask when we're ready for that. That's a seperate workflow. 
- [ ] Add required statements: funding, COI, ethics (no human-subjects; synthetic corpus + autoethnographic design documentation), data availability (Autograder4Canvas URL) // yep, should do this. 
- [ ] Cover letter // seperate workflow
- [ ] Title page (separate file) // lets do this. 
- [ ] APA reference cleanup: re-alphabetize a few out-of-order entries; complete DOIs; "Caldwell & Frame" year mismatch (2016 vs. 2017); "Tan et al." citation form mismatch // let'ts do this. 
- [ ] Strip "WORKING DRAFT — PREPRINT" subtitle // why?

---

## 🟡 Word Count Gap (the biggest open question)

| Item | Words |
|---|---|
| Current total | ~11,125 |
| Likely REE cap (inclusive of refs) | ~8,000 [VERIFY exact cap] | // cap is 10000
| **Need to cut** | **~3,000** |
| Williams compression delivered | 481 |
| Anonymization (content-preserving) | 0 |
| **Remaining gap** | **~2,500** |

**Where the additional ~2,500 words come from is the open question.** Candidates the agents surfaced:
- **V.C "Situating the contribution"** — REE checklist flagged as the longest single subsection
- **IV.A.6 / V.A consolidation** — REE checklist notes redundancy between cross-row synthesis and mechanism discussion
- **`[^model-testing]` footnote** — long; move to methods appendix or trim
- **IV.A.3 "Mar 24 baseline / Apr 26 reproduction"** — these date references point at a private experiment log a reviewer can't access; consider generalizing
- **Reference list** — counts toward the cap; harder to trim but spot-check for refs you cite once that aren't load-bearing

Williams alone is necessary but not sufficient. Worth deciding the compression strategy before Step 5 so you don't end up doing two passes.

---

## Convergence (where multiple reports agreed)

These are the easy wins — multiple agents independently flagged the same thing:

- **Typos** (caught by Williams + REE checklist): `classier` → `classifier` (line 145); missing space `accurately.Inoue's` (line 224)
- **Tentative citations** (REE checklist named the same 5 the citation agent resolved): Chinta, Liu, Queiroga, Stewart, Xu — all resolved with full bib details
- **Voice protection** (Williams + REE checklist both): the autoethnographic first-person register is methodologically load-bearing; both reports converged on preserving it. No conflict between Williams compression and REE anonymization on this front.

---

## Open Decisions for You

1. **Anonymization approach:** Option A (strip institution + locators, keep voice) or Option B (email REE editor)?
2. **Roman-numeral section labels:** Keep or strip during Word conversion? (Typesetter usually strips; keeping costs nothing reviewer-side.) // ignore for now. I'll figure out how i want to format later. 
3. **Figures:** Incorporate any of `ablation_diagram.html` / `test_timeline.html` as figures, or keep paper text-only? // yes - we have table 1, table 2. I think the timeline is probably also useful. What do you think?
4. **Title shortening:** Current 16 words; T&F prefers <12. Worth a shorter alternative? // suggest a few options as a discrete step. 
5. **Word-count compression strategy** — see Word Count Gap above. Pick a path before opening the manuscript.
6. **Three Williams judgment calls** (IV.A.6 *reappear*; V.A¶3 *correctly*; V.A¶3 *simplistic*) — accept or reject each.

---

## Out of Scope (parked for later)

- **Mar 24 / Apr 26 experiment-log dates at IV.A.3** — flagged by crossref agent as referencing a private log; not critical but worth a sentence-level rewrite if you're already in that paragraph.
- **`§IV.A.X` vs. bare `IV.A.X` formatting inconsistency** — copy-edit pass during format conversion.
- **Caldwell publisher details / Schaller page numbers** — REE checklist flagged for verification but agent didn't resolve; do during reference cleanup.

---

**Reports are in this directory. Each has full detail.** This brief is the sequence-and-cross-reference layer; dig into individual reports for the per-item evidence.

— Claude
