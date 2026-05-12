#!/usr/bin/env python3
"""
Generative observation — FULL CORPUS test (32 ES + 14 WB = 46 students)
2026-05-11 — Output-format-bias paper, Row 4 scope extension

WHY THIS SCRIPT EXISTS
----------------------
The paper's Row 4 claim — that generative observation (open-ended description)
avoids the deficit-routing failure that the binary classifier exhibits — has so
far only been tested on subset corpora. The other rows in the comparison table
have been run against the full 32 ES corpus + 14 WB cases (46 students total).
This script closes the scope asymmetry: same students, same assignment, but the
generative observation prompt instead of the binary.

The paper also makes a load-bearing claim about an asymmetry between conditions:
class context HELPS generative observation (gives it the community read it
needs to recognize WB cases as engagement, not crisis) but HURTS the binary
(supplies priming that the deficit-routing pathway picks up on). To verify
that claim we run BOTH:

    a2               — gen ob, with Gemma 12B class context
    a2_no_context    — gen ob, no class context

Both conditions have the structural-power-moves block stripped AND the
relational/narrative epistemology paragraph stripped (the a2 strip, not a1).
Condition prompts and condition definitions are copied VERBATIM from the
existing variant test apparatus:

    /Users/june/Documents/GitHub/research/output-format-bias/scripts/
        run_variant_a_stripped_observation.py
    OBSERVATION_PROMPT_A2          — lines 186–226
    OBSERVATION_PROMPT_A2_NO_CONTEXT — lines 235–259
    CONDITIONS["a2_no_context"]    — lines 296–307
    OBSERVATION_SYSTEM_PROMPT      — lines 85–111

This script does NOT redefine those prompts. It imports them via runtime
re-execution from the sibling script so the bytes stay identical and any future
edit propagates.

DIFFERENCES FROM THE SIBLING SCRIPT
-----------------------------------
- Model: Gemma 12B only (Qwen, Llama, and the Llama spot-check dropped). The
  paper's primary model family is Gemma; keeping the multi-model loop here
  blows compute past the May 20 deadline budget for no analytical gain.
- n_runs_per_model: 5 (sibling uses 3). Statistical comparability with the
  binary runs and 4-axis runs which also use n=5.
- Students: full 32 ES corpus + 14 WB cases (sibling uses an 8-student
  workshop subset). WB cases are synthesized into pseudo-student records that
  match the ES schema (student_id="WBxx", student_name=case["name"],
  text=case["text"]) at load time.
- Conditions: a2 and a2_no_context only. b_replicate and a1 not run.

CLI
---
    --smoke    Limit to 2 students (1 ES = S002, 1 WB = WB01) and n=1 across
               both conditions. ~3 min sanity check before launching the
               ~24-hour full run.

LAUNCH (full run, from autograder root)
---------------------------------------
    cd ~/Documents/GitHub/Autograder4Canvas
    PYTHONPATH=src python3 \\
        ~/Documents/GitHub/research/output-format-bias/scripts/run_genob_full_corpus_test.py

LAUNCH (smoke)
--------------
    cd ~/Documents/GitHub/Autograder4Canvas
    PYTHONPATH=src python3 \\
        ~/Documents/GitHub/research/output-format-bias/scripts/run_genob_full_corpus_test.py \\
        --smoke

OUTPUTS
-------
    output-format-bias/data/raw_outputs/test_variant_a2_FULL_CORPUS_observation_<YYYY-MM-DD_HHMM>.json
    output-format-bias/data/raw_outputs/test_variant_a2_no_context_FULL_CORPUS_observation_<YYYY-MM-DD_HHMM>.json
"""

import argparse
import datetime as _dt
import importlib.util
import json
import sys
import time
from dataclasses import replace
from pathlib import Path

# -- paths --
AUTOGRADER_ROOT = Path("/Users/june/Documents/GitHub/Autograder4Canvas")
CORPUS_PATH = AUTOGRADER_ROOT / "data" / "demo_corpus" / "ethnic_studies.json"
CLASS_READING_PATH = (
    AUTOGRADER_ROOT / "data" / "demo_baked" / "checkpoints"
    / "ethnic_studies_gemma12b_mlx_class_reading.json"
)
SIBLING_SCRIPT = Path(
    "/Users/june/Documents/GitHub/research/output-format-bias/scripts/"
    "run_variant_a_stripped_observation.py"
)
ALT_TESTS_SCRIPT = AUTOGRADER_ROOT / "scripts" / "run_alt_hypothesis_tests.py"
OUTPUT_DIR = Path(
    "/Users/june/Documents/GitHub/research/output-format-bias/data/raw_outputs"
)

# autograder backend
sys.path.insert(0, str(AUTOGRADER_ROOT / "src"))
from insights.llm_backend import BackendConfig, send_text, unload_mlx_model  # noqa: E402


# ============================================================================
# Import prompts and condition defs VERBATIM from the sibling variant script.
#
# We load the sibling as a module rather than re-typing the prompts here, so
# that any future correction to the canonical A2 / A2-no-context prompt text
# propagates automatically. The sibling's `main()` is not executed; we only
# pull the constants out of its namespace.
# ============================================================================
def _load_sibling_module():
    spec = importlib.util.spec_from_file_location(
        "_variant_a_stripped_observation", SIBLING_SCRIPT
    )
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


_SIB = _load_sibling_module()

OBSERVATION_SYSTEM_PROMPT = _SIB.OBSERVATION_SYSTEM_PROMPT
OBSERVATION_PROMPT_A2 = _SIB.OBSERVATION_PROMPT_A2
OBSERVATION_PROMPT_A2_NO_CONTEXT = _SIB.OBSERVATION_PROMPT_A2_NO_CONTEXT

# Reuse the sibling's a2 condition description verbatim. The sibling's
# CONDITIONS dict does not currently expose a separate "a2" entry (it's
# implicit in the prompt constant), so we copy the description from the
# sibling's comment block above OBSERVATION_PROMPT_A2 (lines 182–185).
CONDITIONS = {
    "a2": {
        "prompt": OBSERVATION_PROMPT_A2,
        "uses_class_context": True,
        "description": (
            "A1 strip + also strip relational/narrative epistemology paragraph. "
            "Retain Gemma 12B class context."
        ),
    },
    "a2_no_context": {
        "prompt": OBSERVATION_PROMPT_A2_NO_CONTEXT,
        "uses_class_context": _SIB.CONDITIONS["a2_no_context"]["uses_class_context"],
        "description": _SIB.CONDITIONS["a2_no_context"]["description"],
    },
}


# ============================================================================
# Models — Gemma 12B ONLY for this run. Qwen and Llama dropped to keep the
# full-corpus run tractable inside the paper's compute budget. Temperature
# and max_tokens copied from the sibling script's MODELS["gemma12b"] entry.
# ============================================================================
MODELS = {
    "gemma12b": {
        "name": _SIB.MODELS["gemma12b"]["name"],
        "model": _SIB.MODELS["gemma12b"]["model"],
        "max_tokens": _SIB.MODELS["gemma12b"]["max_tokens"],
        "temperature": _SIB.MODELS["gemma12b"]["temperature"],
    },
}

N_RUNS_PER_MODEL = 5  # paper-level comparability with binary + 4-axis runs
ASSIGNMENT = _SIB.ASSIGNMENT  # "Week 6 Discussion: Intersectionality in Practice"


# ============================================================================
# WELLBEING_SIGNAL_CASES — extract the 14 WB case definitions from the
# Autograder4Canvas alt-hypothesis test script. We import the constant as-is
# (no re-typing) and then harmonize the schema with the ES corpus.
#
# ES corpus row:  {"student_id": "S002", "student_name": "Jordan Kim", "text": "..."}
# WB case row:    {"id": "WB01", "name": "Rosa Gutierrez", "text": "...", ...}
#
# After harmonization, WB cases are appended into the corpus dict under
# keys "WB01".."WB14" with an added `is_wb_case` flag for downstream analysis.
# ============================================================================
def _load_wellbeing_cases():
    spec = importlib.util.spec_from_file_location(
        "_alt_hypothesis_tests", ALT_TESTS_SCRIPT
    )
    mod = importlib.util.module_from_spec(spec)
    # The alt-hypothesis module has top-level imports that may not be needed
    # for just reading the constant; we tolerate ImportError on heavy deps by
    # reading the file as text and parsing only the WELLBEING_SIGNAL_CASES
    # literal if module-load fails. Try the clean path first.
    try:
        spec.loader.exec_module(mod)
        return mod.WELLBEING_SIGNAL_CASES
    except Exception as e:
        print(f"  (note: module-load failed for alt-hypothesis script: "
              f"{type(e).__name__}: {e}; falling back to AST extraction)")
        import ast
        src = ALT_TESTS_SCRIPT.read_text()
        tree = ast.parse(src)
        for node in ast.walk(tree):
            if isinstance(node, ast.Assign):
                for tgt in node.targets:
                    if isinstance(tgt, ast.Name) and tgt.id == "WELLBEING_SIGNAL_CASES":
                        return ast.literal_eval(node.value)
        raise RuntimeError("WELLBEING_SIGNAL_CASES not found in alt-hypothesis script")


def load_corpus(smoke=False):
    """Return {student_id: student_dict} keyed by ES id or WB id.

    Each value has at minimum: student_id, student_name, text, is_wb_case.
    """
    es_rows = json.loads(CORPUS_PATH.read_text())
    corpus = {s["student_id"]: {**s, "is_wb_case": False} for s in es_rows}

    wb_cases = _load_wellbeing_cases()
    for case in wb_cases:
        corpus[case["id"]] = {
            "student_id": case["id"],
            "student_name": case["name"],
            "text": case["text"],
            "is_wb_case": True,
            "wb_signal_type": case.get("signal_type"),
            "wb_expected_surface": case.get("expected_surface"),
            "wb_description": case.get("description"),
        }

    if smoke:
        keep = {"S002", "WB01"}
        corpus = {k: v for k, v in corpus.items() if k in keep}
    return corpus


def load_class_reading():
    data = json.loads(CLASS_READING_PATH.read_text())
    if isinstance(data, dict) and "class_reading" in data:
        return data["class_reading"]
    if isinstance(data, dict) and "result" in data:
        return data["result"]
    return str(data)


def get_backend(model_key):
    cfg = MODELS[model_key]
    return BackendConfig(
        name=cfg["name"],
        model=cfg["model"],
        max_tokens=cfg["max_tokens"],
        temperature=cfg["temperature"],
    )


def git_provenance():
    """Capture Autograder4Canvas git state — the prompts and backend live there."""
    import subprocess as sp
    prov = {}
    try:
        prov["autograder_commit"] = sp.run(
            ["git", "rev-parse", "HEAD"], capture_output=True, text=True, timeout=5,
            cwd=str(AUTOGRADER_ROOT),
        ).stdout.strip()
        prov["autograder_dirty"] = bool(sp.run(
            ["git", "diff", "--quiet"], capture_output=True, timeout=5,
            cwd=str(AUTOGRADER_ROOT),
        ).returncode)
        prov["autograder_branch"] = sp.run(
            ["git", "branch", "--show-current"], capture_output=True, text=True, timeout=5,
            cwd=str(AUTOGRADER_ROOT),
        ).stdout.strip()
    except Exception as e:
        prov["error"] = str(e)
    return prov


def determinism_check(results_by_model):
    """Per-cell byte-identicality across runs, matching the sibling schema."""
    summary = {}
    for model_key, runs in results_by_model.items():
        by_student = {}
        for r in runs:
            by_student.setdefault(r["student_id"], []).append(r["raw_output"])
        cell_status = {}
        for sid, outputs in by_student.items():
            if len(outputs) <= 1:
                cell_status[sid] = "single_run"
            elif all(o == outputs[0] for o in outputs):
                cell_status[sid] = f"identical_across_{len(outputs)}_runs"
            else:
                distinct = len(set(outputs))
                cell_status[sid] = f"variable_{distinct}_distinct_of_{len(outputs)}"
        summary[model_key] = cell_status
    return summary


def run_condition(condition_name, condition_cfg, corpus, class_reading, student_ids,
                  n_runs, timestamp, initial_results=None, start_run=1):
    resumed = start_run > 1
    print(f"\n\n{'#'*72}")
    print(f"#  CONDITION: {condition_name}")
    print(f"#  {condition_cfg['description']}")
    print(f"#  students={len(student_ids)}  n_runs={n_runs}"
          + (f"  (resuming from pass {start_run})" if resumed else ""))
    print(f"{'#'*72}")

    prompt_template = condition_cfg["prompt"]
    use_class = condition_cfg["uses_class_context"]
    results_by_model = {}
    partial_path = OUTPUT_DIR / f"test_variant_{condition_name}_FULL_CORPUS_observation_{timestamp}.partial.json"

    for model_key in MODELS:
        print(f"\n{'='*70}\n  {condition_name} — {model_key} (n={n_runs})\n{'='*70}")
        backend = get_backend(model_key)
        results = list(initial_results) if initial_results else []
        for run in range(start_run, n_runs + 1):
            print(f"\n  --- Pass {run}/{n_runs} ---")
            for sid in student_ids:
                if sid not in corpus:
                    print(f"  WARNING: {sid} not in corpus — skipping")
                    continue
                student = corpus[sid]
                tag = "[WB]" if student.get("is_wb_case") else "[ES]"
                fmt_kwargs = {
                    "assignment": ASSIGNMENT,
                    "student_name": student["student_name"],
                    "submission_text": student["text"],
                    "trajectory_context": "",
                    "teacher_lens": "",
                }
                if use_class:
                    fmt_kwargs["class_context"] = class_reading
                prompt = prompt_template.format(**fmt_kwargs)
                t0 = time.time()
                output = send_text(
                    backend, prompt, OBSERVATION_SYSTEM_PROMPT, max_tokens=300
                )
                elapsed = round(time.time() - t0, 1)
                results.append({
                    "student_id": sid,
                    "student_name": student["student_name"],
                    "is_wb_case": student.get("is_wb_case", False),
                    "wb_signal_type": student.get("wb_signal_type"),
                    "wb_expected_surface": student.get("wb_expected_surface"),
                    "run": run,
                    "condition": condition_name,
                    "codepath": f"variant_{condition_name}_observation_prompt_direct",
                    "prompt": prompt,
                    "system_prompt": OBSERVATION_SYSTEM_PROMPT,
                    "raw_output": output,
                    "time_seconds": elapsed,
                })
                print(f"  {tag} {sid} {student['student_name']}: {elapsed}s, {len(output)} chars")
            # Checkpoint after each complete pass through the corpus
            partial_path.write_text(json.dumps({"condition": condition_name, "model": model_key, "passes_complete": run, "results_so_far": results}, indent=2))
            print(f"\n  >> Checkpoint written after pass {run}/{n_runs}: {partial_path.name}")
        results_by_model[model_key] = results
        try:
            unload_mlx_model()
        except Exception as e:
            print(f"  (note: unload_mlx_model raised "
                  f"{type(e).__name__}: {e} — continuing)")

    return results_by_model


def write_condition_output(condition_name, condition_cfg, results_by_model, prov,
                           student_ids, n_runs, timestamp):
    fname_stem = (
        f"test_variant_{condition_name}_FULL_CORPUS_observation_{timestamp}"
    )
    output_path = OUTPUT_DIR / f"{fname_stem}.json"

    payload = {
        "test_name": f"test_variant_{condition_name}_full_corpus_observation",
        "condition": condition_name,
        "condition_description": condition_cfg["description"],
        "uses_class_context": condition_cfg["uses_class_context"],
        "date": timestamp,
        "temperature": MODELS["gemma12b"]["temperature"],
        "corpus": "ethnic_studies_plus_wellbeing_signal_cases",
        "corpus_path": str(CORPUS_PATH.relative_to(AUTOGRADER_ROOT)),
        "wellbeing_cases_source": str(
            ALT_TESTS_SCRIPT.relative_to(AUTOGRADER_ROOT)
        ),
        "class_reading_source": (
            str(CLASS_READING_PATH.relative_to(AUTOGRADER_ROOT))
            if condition_cfg["uses_class_context"]
            else None
        ),
        "models": {k: MODELS[k]["model"] for k in MODELS},
        "students": student_ids,
        "n_es_students": sum(1 for s in student_ids if s.startswith("S")),
        "n_wb_students": sum(1 for s in student_ids if s.startswith("WB")),
        "n_runs_per_model": {k: n_runs for k in MODELS},
        "assignment": ASSIGNMENT,
        "provenance": prov,
        "methodology_note": (
            "Full-corpus extension of the variant generative-observation test. "
            "Same A2 / A2-no-context prompt definitions as the sibling script "
            "run_variant_a_stripped_observation.py (imported verbatim, not "
            "re-typed). Scope expanded from 8-student workshop subset to "
            "32 ES + 14 WB cases = 46 students; n_runs raised from sibling's 3 "
            "to 5 for paper-level statistical comparability with the binary and "
            "4-axis runs. Gemma 12B only — Qwen and Llama dropped to keep the "
            "full-corpus run inside the May 20 deadline compute budget. Per "
            "MASTER_RESPONSE_LOG_2026-05-11.md: no keyword classifier applied "
            "to raw_output; evaluation is by human deep-read."
        ),
        "determinism_check": determinism_check(results_by_model),
        "comparison_anchor_files_variant_b": [
            "output-format-bias/data/raw_outputs/test_a_temperature_gemma12b_2026-03-26.json",
            "output-format-bias/data/raw_outputs/test_e_cross_model_qwen7b_2026-03-26.json",
        ],
        "results_by_model": results_by_model,
    }
    output_path.write_text(json.dumps(payload, indent=2))
    n_runs_total = sum(len(r) for r in results_by_model.values())
    print(f"\n  >> Wrote {n_runs_total} runs for condition "
          f"'{condition_name}' to: {output_path}")


def parse_args():
    p = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    p.add_argument(
        "--smoke", action="store_true",
        help="Limit to 2 students (1 ES = S002, 1 WB = WB01) and n=1 per condition.",
    )
    p.add_argument(
        "--condition", choices=["a2", "a2_no_context", "both"], default="both",
        help="Which condition to run. Default: both. Use 'a2' or 'a2_no_context' "
             "to run a single condition (useful for interleaving with other tests).",
    )
    p.add_argument(
        "--n-runs", type=int, default=None,
        help=f"Number of passes per condition. Default: {N_RUNS_PER_MODEL} (paper standard). "
             "Override with 1 for a quick first pass before chaining other tests.",
    )
    p.add_argument(
        "--resume-from", metavar="PARTIAL_FILE",
        help="Path to a .partial.json checkpoint. Loads completed passes and runs "
             "the remainder up to --n-runs (default: N_RUNS_PER_MODEL). The final "
             "output file uses the same timestamp as the partial, so all passes "
             "land in one file.",
    )
    return p.parse_args()


def _metal_warmup(model_key: str = "gemma12b") -> None:
    """Fire a short inference to initialize Metal before the main run.

    Prevents Metal kernel-compilation stalls on cold starts (especially after
    display sleep). Skipped in smoke mode — smoke runs are short enough that
    warmup adds proportionally too much overhead.
    """
    print("\n  [Metal warmup] Initializing GPU...")
    t0 = time.time()
    try:
        backend = get_backend(model_key)
        backend = replace(backend, temperature=0.1, max_tokens=8)
        send_text(backend, "Hi", "You are a test.")
        # Do NOT unload here — leave model cached so first real inference
        # reuses it directly.
        print(f"  [Metal warmup] Ready ({time.time() - t0:.0f}s)\n")
    except Exception as e:  # noqa: BLE001
        print(f"  [Metal warmup] Non-fatal error: {e}. Proceeding.\n")


def main():
    args = parse_args()
    smoke = args.smoke

    # Handle --resume-from: load checkpoint, override condition + timestamp.
    resume_initial_results = None
    resume_start_run = 1
    if args.resume_from:
        import pathlib as _pl
        partial_path = _pl.Path(args.resume_from)
        if not partial_path.exists():
            raise FileNotFoundError(f"--resume-from: {partial_path} not found")
        partial = json.loads(partial_path.read_text())
        resume_initial_results = partial["results_so_far"]
        resume_start_run = partial["passes_complete"] + 1
        # Infer timestamp from filename: test_variant_COND_FULL_CORPUS_observation_TIMESTAMP.partial.json
        stem = partial_path.stem  # strips .json
        stem = stem.replace(".partial", "")
        timestamp = stem.split("observation_")[-1]
        if not args.condition or args.condition == "both":
            args.condition = partial["condition"]
        print(f"  [resume] Loaded {partial['passes_complete']} passes from {partial_path.name}")
        print(f"  [resume] Resuming from pass {resume_start_run}, timestamp={timestamp}")
    else:
        timestamp = _dt.datetime.now().strftime("%Y-%m-%d_%H%M")

    if smoke:
        n_runs = 1
    elif args.n_runs is not None:
        n_runs = args.n_runs
    else:
        n_runs = N_RUNS_PER_MODEL
    condition_filter = args.condition  # "a2", "a2_no_context", or "both"

    conditions_to_run = {
        k: v for k, v in CONDITIONS.items()
        if condition_filter == "both" or k == condition_filter
    }

    print("="*72)
    print("Generative observation — FULL CORPUS test "
          f"({'SMOKE' if smoke else 'FULL'})")
    print("="*72)

    corpus = load_corpus(smoke=smoke)
    student_ids = sorted(corpus.keys(), key=lambda s: (s.startswith("WB"), s))

    es_ids = [s for s in student_ids if s.startswith("S")]
    wb_ids = [s for s in student_ids if s.startswith("WB")]

    print(f"Conditions: {list(conditions_to_run.keys())}")
    print(f"Models: {list(MODELS.keys())}  (Gemma 12B only)")
    print(f"Students: {len(student_ids)} total = "
          f"{len(es_ids)} ES + {len(wb_ids)} WB")
    print(f"  ES ids: {es_ids}")
    print(f"  WB ids: {wb_ids}")
    print(f"n_runs_per_model: {n_runs}")
    print(f"Timestamp: {timestamp}")
    print(f"Output dir: {OUTPUT_DIR}")

    class_reading = load_class_reading()
    prov = git_provenance()

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    t_start = time.time()

    if not smoke:
        _metal_warmup()

    try:
        for condition_name, condition_cfg in conditions_to_run.items():
            t_cond = time.time()
            # Pass resume state only for the matching condition (first iteration when resuming).
            use_initial = resume_initial_results if condition_name == args.condition else None
            use_start = resume_start_run if condition_name == args.condition else 1
            results_by_model = run_condition(
                condition_name, condition_cfg, corpus, class_reading,
                student_ids, n_runs, timestamp,
                initial_results=use_initial,
                start_run=use_start,
            )
            write_condition_output(
                condition_name, condition_cfg, results_by_model, prov,
                student_ids, n_runs, timestamp,
            )
            elapsed_cond = round(time.time() - t_cond, 1)
            print(f"\n  Condition '{condition_name}' completed in "
                  f"{elapsed_cond}s")
    finally:
        # MLX cleanup — drop the model from memory even if a condition raised.
        try:
            unload_mlx_model()
        except Exception as e:
            print(f"  (cleanup: unload_mlx_model raised "
                  f"{type(e).__name__}: {e})")

    total_elapsed = round((time.time() - t_start) / 60, 1)
    print(f"\n\n{'='*72}")
    print(f"Both conditions complete. Total runtime: {total_elapsed} min")
    print(f"Output files in: {OUTPUT_DIR}")
    print("="*72)


if __name__ == "__main__":
    main()
