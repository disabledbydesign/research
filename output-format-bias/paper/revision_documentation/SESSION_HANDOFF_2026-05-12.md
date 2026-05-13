# Session handoff — 2026-05-12

**For:** Next Claude instance picking up this work
**REE deadline:** 2026-05-20 (medical, not aspirational)

---

## What landed tonight

Seven phases of revision applied to the paper, now at `paper/ofb_paper_v3.md` (migrated from c2c session-4 artifacts dir).

| Phase | What | Status |
|---|---|---|
| 1 | 5 quick edits: tests A–F parenthetical cut, *correctly* drop at V.A¶3, two typos, Crenshaw 1991 added to refs | ✅ |
| 2 | Citations at lines 23 (Selbst + Hoffmann + Helm triad) and 75 (Annamma/Jackson/Morrison + Leonardo + Bonilla-Silva — Annamma is in REE itself) | ✅ |
| 3 | Line 196 stacked fix: antecedent rewrite (now points to §I week-five pattern) + self-care citations (Lorde + Hersey + Chen/Khúc/Kim) + Williams compression | ✅ |
| 4 | Author corrections: Liu Y→Z, Chinta "Quy, T.L."→"Le Quy, T.", Xu year + title fix, Annamma "Jett"→"Jackson" | ✅ |
| 5 | 26 of 30 Williams restructures applied; skipped IV.A.6 *reappear*→*disappears* per June's "not sure"; partially applied V.A¶3 per her *simplistic* keep | ✅ |
| 6 | Anonymization: Watsonville/Santa Cruz/Pajaro → "the local area"; YAML stripped; "WORKING DRAFT" subtitle removed; author info moved to separate `title_page.md`; Bloch fieldnotes self-cite removed | ✅ |
| 7 | References alphabetized (63 entries); Caldwell year fixed (2016, not 2017); Tan citation form fixed (parens=full, narrative=et al.); Briggs (1986) *Learning How to Ask* added; funding/COI/ethics/data availability statements added before References | ✅ |

Plus tonight's late additions:
- Helm et al. (2024) and Hoffmann (2019) added to References after June confirmed the triad works at both line 23 and line 209
- Mar 24 / Apr 26 baseline dates generalized to "an earlier baseline and a later reproduction"

**Current word count: 11,248 (vs. REE 10,000 cap → 1,248 over).**

---

## Open items for next session

### 🔴 Must fix before submission

1. **Karinshak et al. (2024)** still cited at line 231 (V.C¶2) but missing from References. Either add the entry or remove the citation. Context: cited as evidence that "open-ended formats surfaced implicit cultural values that compressed formats suppressed." Likely paper: Karinshak, Walker, Lewis et al. on LLM expressed values across cultures — verify with semantic-scholar or Zotero.

2. **3 orphan references** in list but not cited inline — either add inline citations or remove:
   - Namburi & Hopkins (2024) "Beyond content: A trauma-informed framework..."
   - Oketch et al. (2025) "Bridging the LLM accessibility divide..."
   - Schalk (2018) *Bodyminds reimagined*

3. **Word-count compression** — 1,248 to cut. Candidates flagged in `revision_documentation/overnight_reports_2026-05-12/ree_submission_checklist.md`:
   - V.C tightening (longest single subsection per REE agent)
   - IV.A.6 / V.A consolidation (some redundancy between cross-row synthesis and mechanism discussion)
   - Move `[^model-testing]` footnote to methods appendix or trim
   - Generalize remaining experiment-log-specific detail

### 🟡 Decisions June deferred

- **IV.A.6 "does not reappear under generative observation" → "disappears"** — Williams proposed compression; "reappear" is methodologically more precise (tracks trajectory across formats); "disappears" loses sequence. Left as original.
- **Title shortening** — currently 16 words ("Output Format as Architectural Determinant of Demographic Bias in AI-Powered Educational Welfare Classification"); T&F prefers <12.
- **Roman numeral section labels** — keep or strip during Word conversion. Typesetter usually strips; keeping costs nothing reviewer-side.
- **Figures** — `ablation_diagram.html`, `test_timeline.html`, `test_to_ablation_crossref.html` exist in c2c artifacts. Decide whether to incorporate as figures.
- **Abstract trim** — currently 213 words; June reserved this for hand-editing.

### 🔵 [VERIFY] on live REE Instructions for Authors page (~5 min)

WebFetch to tandfonline.com was blocked during overnight pass. Need spot-check of:
- Exact abstract word cap (likely 200; some T&F education journals are 250)
- Exact manuscript word cap (memory says 10,000 inclusive)
- Double vs. single anonymized
- Structured abstract requirement (likely no, but confirm)
- Keyword count (typically 4–7)

URL: `https://www.tandfonline.com/journals/cree20` → "Instructions for Authors"

### 🟢 Held per June's instructions (separate workflows)

- Markdown → .docx conversion
- Cover letter
- Abstract trim (June by hand)

### 📝 Title page placeholders

`paper/title_page.md` has `[Affiliation to be confirmed]` and `[ORCID iD to be added]` and `[GitHub URL — to be confirmed]` (data availability) — fill in before submission.

---

## File structure (post-migration)

```
output-format-bias/
├── paper/
│   ├── ofb_paper_v3.md                  ← canonical paper
│   ├── title_page.md                    ← separate per REE anonymization
│   └── revision_documentation/
│       ├── SESSION_HANDOFF_2026-05-12.md  ← this file
│       └── overnight_reports_2026-05-12/
│           ├── MORNING_BRIEF.md           ← integrated brief w/ comments
│           ├── citation_resolution_report.md
│           ├── crossref_verification.md
│           ├── ree_submission_checklist.md
│           └── williams_restructure_proposal.md
├── c2c/c2c_sessions/output-format-bias-session-4_2026-04-28/artifacts/
│   └── (drafts, workshops, handoffs, parking lot, validation audits — c2c artifacts only)
└── data/, research/, scripts/, etc.
```

---

## Notes for next instance

- **Voice profile** at `~/.claude/skills/voice-check/profiles/june_bloch.json` — load before drafting any prose for the paper. The Williams compression tonight respected the autoethnographic register; that protection should continue.
- **MORNING_BRIEF.md** in overnight_reports has June's inline comments from the AM review — useful for understanding why certain edits were applied or skipped.
- **Hoffmann (2019)** "Where Fairness Fails" — added late after June confirmed the citation triad works. Argument summary in the conversation if needed: fairness frameworks fail because they presuppose a just baseline that doesn't exist.
- **Memory** at `~/.claude/projects/-Users-june-Documents-GitHub-research/memory/project_output_format_bias_paper.md` updated to reflect current state.
- The c2c session-4 artifacts dir is no longer where the paper lives — don't write there for journal-submission work.
