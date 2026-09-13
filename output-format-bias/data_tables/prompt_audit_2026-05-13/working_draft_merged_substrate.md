# Session Handoff — Prompt Fragility Audit
*Session date: 2026-05-13. Output-format-bias project.*

## What this session was about

The output-format-bias paper compares three classifier prompt formats (binary, 4-axis, generative observation) on the same student-writing corpus. Last night's "v2 unified" runs are the cleanest format comparison so far — equalized prompts across formats, with three conditions for two appended blocks: supersedes_state = `both` | `single` | `neither`.

This session looked at whether the v2 prompts themselves are calibrated to corpus-specific examples in ways that would make the comparison fragile and the prompts hard to maintain. Ran a parallel fragility audit (Sonnet + Opus subagents) on the v2 prompts, reconciled findings, worked through what to change.

## Scope: what's v2 unified

**In scope** (used in last night's runs):
- `UNIFIED_BINARY_NARROW_BASE_SYSTEM`, `UNIFIED_BINARY_BROAD_BASE_SYSTEM` (lines 270–460 of `Autograder4Canvas/scripts/run_4axis_full_corpus_test.py`)
- `UNIFIED_4AXIS_BASE_SYSTEM` (programmatically extracted from `WELLBEING_CLASSIFIER_SYSTEM` minus supersedes, single-sentence, and tiebreaker blocks)
- `UNIFIED_GENOB_BASE_SYSTEM` (lines 489–582)
- Conditional blocks: `UNIFIED_*_SUPERSEDES_BLOCK`, `UNIFIED_*_SINGLE_SENTENCE_BLOCK` (binary lines 466–484; 4-axis extracted from WCS; genob lines 587–607)
- User prompt: `WELLBEING_CLASSIFIER_PROMPT` in `Autograder4Canvas/src/insights/prompts.py`, shared across all three formats. signal_prefix=""; no prescan.

**Out of scope** (relevant for legacy maintenance only):
- `WELLBEING_CLASSIFIER_SYSTEM` directly (full version with all blocks)
- `BINARY_REASONING_SYSTEM`, `FOUR_AXIS_REASONING_SYSTEM` (older variants)
- `OBSERVATION_PROMPT`, `OBSERVATION_SYNTHESIS_PROMPT` (legacy production genob; `UNIFIED_GENOB_BASE_SYSTEM` replaces them — including Opus's A19 "Ingrid"/"DeShawn" finding, which is in `OBSERVATION_SYNTHESIS_PROMPT`)
- `WELLBEING_PRESCAN_*`

## Decisions made this session

1. **Cut the supersedes block.** Data: binary FP drops (narrow: 3→2; broad: 5→1); 4-axis neutral. Same rule across formats (format-adapted labels), so the cut applies symmetrically.
2. **Cut the single-sentence block.** Same direction in the data.
3. **Merge the substrate.** One shared "concerning circumstances" description across all three formats. CRISIS/BURNOUT/CONCERN triage moves to the format-output layer. Justified because the acute-vs-ongoing distinction is fuzzy in real cases (WB04 is both; WB02 same); pre-bucketing imports the corpus design into the substrate.

## Working language for the merged substrate (not final)

> "Concerning circumstances in the student's own life — whether acute threats to safety/stability OR ongoing demands wearing down their capacity — including basic bodily needs (food, sleep, rest, safety) being squeezed out by demands on their time and body."

**Fourth structural piece, implicit but not yet in the language:** the concern is **visible in the work itself**, not just reported. WB05's "I can't remember what it said, everything is blurring together" — capacity depletion enacted in the submission. WB02's "cuts off mid-thought to pick up daughter" — same. Distinguishes "student says they're tired" (could be casual) from "tiredness limiting the actual work in front of them" (the structural feature). Operationally: the prompt needs to point the model at signals visible in HOW the student wrote, not only at signals stated in WHAT they wrote.

## Technique developed this session

For each enumeration or case-anchored guard in the prompt:

1. **Identify the structural feature the enumeration is trying to evoke.** (E.g., the BURNOUT four-word list was reaching for "the student's own ongoing material conditions are limiting their capacity.")
2. **Distinguish items doing two different jobs:**
   - **Definitional work** — the structural feature already catches them. Drop. (E.g., "exhaustion" — vague, already implied by structural feature.)
   - **Model-correction work** — the model misses a specific thing without the example named. Keep, but reframe as grounding example. (E.g., "sleep deprivation" — June flagged that models specifically miss this without it being named.)
3. **Frame retained items as illustrative, not exhaustive.** "Such as X, Y, Z" rather than "X, Y, Z" stated as a checklist.
4. **Drop pure corpus-overlay items.** Items whose only function is to point at specific essays in the 46-case corpus.

## Held for next session

In priority order:

### 1. Draft the merged substrate text
Use the working language as starting point. The merged substrate needs to:
- Describe both shapes (acute danger AND ongoing depletion) describably enough that 4-axis output instructions can triage from it
- Include the "visible in the work itself" structural piece
- Apply the technique (structural feature + grounding examples + "such as") to the merged enumeration

### 2. Decide format-output triage rules
Substrate becomes flat. Triage moves to format-specific output instructions:
- **4-axis:** rules for assigning CRISIS / BURNOUT / ENGAGED / NONE from the merged substrate's structural features
- **Binary:** just CONCERN / CLEAR
- **Genob:** just describe; no triage

### 3. Apply the technique to remaining A/B items
Items not directly addressed by the merge — each needs a pass:
- **Worked examples (a/b/c)** — case-anchored; reframe as principle-with-illustration or cut
- **S002 "trailing off mid-sentence" cue** — calibrates to one case whose true label is EDGE per master log
- **"this is what I needed to write" guard** — Sonnet/Opus disagreed on which WB case it maps to; potentially internally incoherent (same case used both to clear and to flag in different guards)
- **"It was fine though" guard** — no clear corpus match found; calibration source outside synthetic corpus
- **IDENTITY-NAVIGATION FATIGUE passage** — calibrated to S029
- **AAVE register list** (`AAVE, multilingual mixing, nonstandard English, neurodivergent writing patterns (fragmented, nonlinear, associative)`) — enumeration
- **Identity disclosure list** (`disability (ADHD, dyslexia, autism), neurodivergent identity, race, religion, immigration status, sexuality, or language background`) — autism/dyslexia have no corpus referent; sexuality has no corpus referent
- **Family-narrative passage** (`grandmother's migration, father's union work, sibling's diagnosis`) — Sonnet's N2: most saturated single corpus-to-prompt connection (7–8 corpus essays)
- **Mosque/food bank/extended family enumeration** — corpus-design rendered as checklist
- **TOPIC-ADJACENCY block** — survives in `UNIFIED_4AXIS_BASE_SYSTEM`; enumerates assignment themes (rest, self-care, productivity, exhaustion, overwork, labor / violence, trauma, illness, displacement, loss)

### 4. Inference-handling cluster
Separate move at the reasoning/rationale layer of the prompt. Three layers June surfaced:
- Sometimes inference is needed (signal enacted, not stated) — model SHOULD make it
- When it does, it should mark the inference AS inference in the rationale, not assert it as stated fact
- Sometimes inference is a leap (multiple readings equally plausible) — the model should name ambiguity instead of picking

**Controlled across formats:** this failure mode affects binary, 4-axis, and genob equally. Not biasing the comparison. Can address later without it being load-bearing for the paper.

### 5. S026 and S029 as real signals
- **S026** (DeShawn / brother Malik): persistent FP across all conditions and formats. The OWN-life guard isn't catching this. Worth digging into what about the guard's language is failing — is the guard too lexically anchored to "exhaustion/overwork" rather than the structural "student's own ongoing depletion"?
- **S029** (neurodivergent writer, format-constraint complaint): binary-narrow FP across all three supersedes_state conditions; 4-axis catches correctly across all three. Format-effect signal worth thinking about for paper claims — even with merged substrate, the format itself matters here.

### 6. Re-run tests after substrate change
Probably smoke test first (4 cases) then full corpus. v2 supersedes_state='neither' is the closest comparable baseline since both blocks are already cut in that condition.

### 7. Paper integration
REE deadline is **2026-05-20 (7 days from this session)**. Substrate restructure has paper consequences — either re-run results land in the paper, or paper describes both versions, or work is positioned as follow-up. Worth deciding scope before drafting starts.

## Practical first step for next session

**Re-export June's annotations.** The JSON-save bug in `data_tables/test_comparisons/comparison_2026-05-13_unified.html` was fixed this session — the save button now exports cell-level annotations (was only exporting row-level). June should re-open the HTML and click save, which will populate `comparison_2026-05-13_unified.notes.json` with per-run case-level notes. These notes are her authoritative read of each case's true classification and will be needed for any further FP/FN analysis.

## Methodological notes for the next instance

- **Defer to annotated case notes** (`corpus_review_state.json` + `comparison_2026-05-13_unified.notes.json` once re-exported), not raw tabulations. Raw FP counts can be inflated by:
  - **Edge cases (ambiguous true label):** explicitly marked `expected_*` = "EDGE" — S002, S020, S031
  - **Out-of-scope cases handled by separate subsystems:** S010, S011 (academic integrity); S015, S018, S025 (power moves)
  - **S026:** notes flag this as "Concern broadly scoped could be arguable" — not a clean FP
- **"Controlled across formats" as methodology principle.** A failure mode affecting all comparison cells equally doesn't bias the format-effect comparison. Use this to scope what needs to be fixed now (cell-differentiating issues) vs. what can wait (cell-symmetric issues). This was June's articulation; it generalizes.
- **The fragility-audit technique is one-step, not two.** The audits surface fragility (Column A: direct example-to-essay matches; Column B: name-all-the-things passages). The structural-pattern extraction is the lead Claude + June's joint work, not the agents' work.

## Source artifacts the next instance needs

- **Fragility audits (read first):** `data_tables/prompt_audit_2026-05-13/audit_sonnet.md`, `audit_opus.md`
- **Master verification log (settled findings):** `MASTER_RESPONSE_LOG_2026-05-11.md`
- **Corpus annotations (case-level ground truth, 46 students):** `data_tables/corpus_overview/corpus_review_state.json`
- **Per-run notes** (June needs to re-export first): `data_tables/test_comparisons/comparison_2026-05-13_unified.notes.json`
- **Comparison HTML** (re-export here): `data_tables/test_comparisons/comparison_2026-05-13_unified.html`
- **v2 raw test outputs:** `data/raw_outputs/test_unified_{binary_narrow,binary_broad,4axis,genob}_{both,single,neither}_FULL_CORPUS_gemma12b_2026-05-13_*.json`
- **Prompt source:**
  - `Autograder4Canvas/scripts/run_4axis_full_corpus_test.py` (lines 270–700 for unified substrates + blocks; lines 1595–1860 for run functions)
  - `Autograder4Canvas/src/insights/prompts.py` (lines 1697–1830 for `WELLBEING_CLASSIFIER_SYSTEM` — the source of `UNIFIED_4AXIS_BASE_SYSTEM`)
- **Paper draft:** `paper/ofb_paper_v3.md`
- **Paper-side context:** `paper/revision_documentation/SESSION_HANDOFF_2026-05-12.md` (the parallel paper-revision handoff)

## State at session end

- Cut decisions (supersedes + single-sentence) made but not yet implemented in code; v2 raw outputs already exist for the 'neither' condition (cleanest baseline)
- Working substrate language drafted; not yet implemented as prompt text
- Format-output triage rules not yet drafted
- Other A/B items not yet addressed
- Annotation re-export not yet done by June (JSON-save fix is in; UX-ready)
- No test re-runs scheduled yet
- Paper unmodified this session
