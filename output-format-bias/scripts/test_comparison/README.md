# Test comparison + gen-ob workshop tools

Built 2026-05-12. Two tools that share a registry, a loader, and a ground-truth
file.

---

## Quick reference (the things you'll actually do)

### 0. Recommended: start the local server (enables in-page register+rebuild)
```
python -m scripts.test_comparison.serve
```
Auto-opens your browser to the most recent comparison HTML on http://127.0.0.1:5173/.
With the server running, the **"＋ Add data & rebuild"** button in the top toolbar
works: drop a JSON file in, pick a target config, click — server uploads, registers,
rebuilds, and reloads the page. No terminal needed.

Without the server (i.e., if you open the HTML directly via `file://`), the button
still opens a modal that shows the equivalent CLI commands to paste into a terminal.

### 1. Rebuild the comparison HTML (CLI alternative)
```
python -m scripts.test_comparison.build --comparison comparison_2026-05-12 --open
```
Output: `data_tables/test_comparisons/comparison_2026-05-12.html`.
Notes in localStorage persist as long as the output path doesn't change.

### 2. Add a new run of an existing test
Edit registry (safely):
```
python -m scripts.test_comparison.register add-file <config_id> <path/to/new.json>
python -m scripts.test_comparison.build --comparison comparison_2026-05-12
```
The new column shows aggregated stats across all registered files.

### 3. Rebuild the gen-ob coding workshop
```
python scripts/build_variant_a_workshop.py --date 2026-05-12
```
Output: `data_tables/variant_a_coding_workshop_2026-05-12.html`.
LocalStorage key is `vaw_state` — your codes from earlier workshops carry over.
Use `--date 2026-05-11` to overwrite an existing dated file.

### 4. Export your gen-ob codes as a comparison-tool column
- In the workshop HTML, click **"Export as comparison config →"** (top toolbar).
- Pick a model + condition, edit category-to-verdict mapping if needed, click
  **Download manual_codes JSON**.
- Move the downloaded file to `data_tables/genob_codes/`.
- Register it:
```
python -m scripts.test_comparison.register add-config \
  --id genob_gemma12b_b_replicate_2026-05-12 \
  --schema manual_codes \
  --files data_tables/genob_codes/genob_codes_gemma12b_b_replicate_2026-05-12.json
```
- Add to a comparison via `add-comparison`, or edit `registry.json`'s
  `comparisons` section directly.

### 5. Set up the three-way comparison
Pick your "best representative" run from each track (narrow configs):
```
python -m scripts.test_comparison.register add-comparison \
  --id comparison_three_way_2026-05-12 \
  --configs <binary_best_run_id> <4axis_best_run_id> <genob_codes_id> \
  --output data_tables/test_comparisons/comparison_three_way_2026-05-12.html
python -m scripts.test_comparison.build --comparison comparison_three_way_2026-05-12
```

### 6. Inspect / fix the registry
```
python -m scripts.test_comparison.register list
python -m scripts.test_comparison.register validate
```
`validate` runs sanity checks (duplicate ids, missing files, broken refs).

---

## What edits where (cheat sheet)

| What you might edit | Where | How |
|---|---|---|
| Notes per row in a comparison | localStorage (autosaved) + JSON sidecar | Type in textarea. Use "Notes JSON" buttons to back up / import. |
| Gen-ob codes per cell | localStorage + workshop HTML | Click dropdown / type in notes (existing workflow). |
| Add new run of existing test | `registry.json` → `files` list | CLI `register.py add-file` OR edit JSON directly |
| Add new test config | `registry.json` → new entry | CLI `register.py add-config` OR edit JSON |
| Add new comparison | `registry.json` → new entry | CLI `register.py add-comparison` OR edit JSON |
| Pick a "best run" | `registry.json` → narrow config pointing to one JSON | CLI OR edit JSON |
| Fix a ground-truth label | `truth.json` | Edit JSON directly |
| Add to equity-pattern student list | `truth.json` → `equity_pattern_students.ids` | Edit JSON directly |
| Flag-rate threshold | per-comparison in `registry.json` → `flag_threshold` | Edit one number |
| Gen-ob category labels / colors / patterns / cross-notes / flags | `genob_workshop_config.json` | Edit JSON, rebuild workshop |
| Gen-ob category → verdict mapping | inside exported codes JSON (`category_to_verdict`) | Edit before registering, OR edit in the export modal before downloading |
| Color coding (TP/FP/FN/TN) | `templates/colors.css` (CSS variables at top) | Edit one CSS value |
| Adding a new schema (rare) | `loader.py` — one function | Python edit. Pattern documented in `loader.py` docstring. |

**Notes survival rules:**
- Notes survive HTML rebuilds at the same output path (localStorage is keyed
  per file:// origin).
- Notes also survive in a downloadable JSON sidecar (button in the UI).
- **Renaming a config orphans its notes.** `register.py rename-config` emits a
  one-time browser-console snippet you paste to migrate localStorage entries.

---

## File map

```
output-format-bias/scripts/test_comparison/
  __init__.py
  README.md                       # this file
  loader.py                       # schema-dispatched JSON readers; docstring documents adding new schemas
  truth.json                      # ground truth + equity-pattern list + controls (EDITABLE)
  truth.py                        # thin reader for truth.json
  aggregate.py                    # per-(config, student) aggregation
  register.py                     # safe registry editor (CLI)
  build.py                        # comparison HTML builder (CLI)
  registry.json                   # logical configs + comparisons (EDITABLE; prefer register.py)
  genob_workshop_config.json      # gen-ob workshop pre-populated content (EDITABLE)
  templates/
    comparison.html.tmpl          # HTML template with embedded {DATA_JSON} placeholder
    colors.css                    # CSS variables for cell coloring (EDITABLE)

output-format-bias/scripts/
  build_variant_a_workshop.py     # gen-ob workshop builder (refactored 2026-05-12, registry-backed)

output-format-bias/data_tables/test_comparisons/
  comparison_2026-05-12.html      # output: binary vs 4-axis vs binary-reasoning grid

output-format-bias/data_tables/genob_codes/
  (your exported manual_codes JSON files go here)

output-format-bias/data_tables/
  variant_a_coding_workshop_*.html   # gen-ob workshop HTMLs (per build date)
```

---

## What the comparison HTML does

- Rows: 46 students sorted ES (S001–S032) then WB (WB01–WB14). ES with equity
  patterns get a purple left stripe; WB controls get a gray left stripe.
- Static cols: ID, Name, Source, Pattern, Expected (color-coded).
- One column per registered test config. Each cell shows:
  - Axis distribution as `ENG ×5` or `CRI ×3 / BUR ×2`
  - For binary_concern only: a second `prod:` line showing the production
    post-processor's verdict, with a ⚠ if it diverges from raw
  - Confidence range below + `n=N` runs aggregated
- Cell color encodes vs-truth verdict (TP / TN / FP / FN). Edit
  `templates/colors.css` to change colors.
- **Click any cell** → reasoning modal opens with each run's reasoning prose
  (and the model's raw output, expandable per run). Esc / click-outside closes.
- Disagreement column lights when configs differ at majority-flag level.
- Filter buttons: All / Disagreements / FPs / Misses / Controls /
  Equity-pattern / Test R prod-divergent.
- CSV export + Notes JSON export/import.

## What the gen-ob workshop does

- 4 conditions (b_replicate / a1 / a2 / a2_no_context) × 3 models
  (gemma12b / qwen7b / llama8b) × 8 students = 96 cells in a grid.
- Click any cell → modal with student pattern, observation text, code dropdown,
  notes, pre-populated flags.
- Cross-condition view per student (compare all conditions × models for one
  student at once).
- LocalStorage key: `vaw_state` — codes, notes, category edits persist.
- **Export as comparison config** button: pick (model, condition), download
  the codes as a `manual_codes` JSON the comparison tool can register.

---

## Verification (already passed at build time)

- ✓ Test R raw 11 TP / 10 FP / 1 FN / 24 TN; production 8 TP / 0 FP / 4 FN / 34 TN
- ✓ Test N 11 TP / 1 FP (S026 BURNOUT 5/5) / 1 FN (S002) / 33 TN
- ✓ Binary-Reasoning 11 TP / 1 FP (S020 CRISIS) / 1 FN (S002) / 33 TN
- ✓ Disagreement count = 10 rows (the equity-pattern + WB09 cases where binary
  raw flags and 4-axis correctly clears)
- ✓ Unknown schema raises clean error with pointer to loader.py docstring
- ✓ Re-run aggregation: copying a JSON and appending to registry doubles `n_runs`
- ✓ register.py rejects file-not-exists with a clean message
- ✓ Refactored gen-ob workshop produces structurally identical DATA to the
  pre-refactor 2026-05-11 version (cells, patterns, cross_notes, flags, models,
  conds, student_ids, default_categories all match exactly)

---

## Things to flag if surfacing matters

1. **Test R cells are two-line.** `raw:` and `prod:` — production regex
   post-processor changes the answer dramatically.
2. **Binary-Reasoning shows `n=1`.** Don't read its single-shot answer as
   stable. If you queue more runs, the column updates automatically.
3. **Disagreement = different majority verdict.** So `ENG 5/5 vs CRI 1/5 + ENG 4/5`
   agrees (both majority-clear); `ENG 5/5 vs CRI 5/5` disagrees.
4. **S002 misses across all three live configs.** Orange across the board —
   the equity headline.
5. **WB04 / WB08 / WB11 in Test R** show as raw `FLAG 5/5` / prod `CLEAR 5/5`
   — production regex killing real TPs.
6. **Gen-ob category → verdict mapping is your call.** Configurable in the
   export modal before download, or in the exported JSON.

---

## Architecture notes (for the curious)

- **One source of schema knowledge:** `loader.py`. Both tools use it.
- **No statistical inference.** Surfaces raw counts. McNemar etc. are out of
  scope.
- **No re-running of classifiers.** Read-only over existing `raw_outputs/`.
- **Adding a new schema** is the only case where you'd touch Python. The
  docstring at the top of `loader.py` walks through it.
