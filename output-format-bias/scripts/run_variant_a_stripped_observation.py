#!/usr/bin/env python3
"""
Variant A test — pure observation prompt(s), three conditions head-to-head
2026-05-11 — Output-format-bias paper verification follow-up

Hypothesis: the deficit framing observed on Qwen 7B in Tests A and E is
introduced by either (a) the structural-power-moves vocabulary in the prompt,
(b) the relational/narrative epistemology guidance, and/or (c) upstream
priming from the Gemma-12B-generated class context — not the open-ended
observation format itself.

Three conditions run sequentially in one command:

    a1               — strip the structural-power-moves block + 7-item taxonomy
                       + "NAME THE MECHANISM" paragraph. Keep relational/narrative
                       guidance. Keep Gemma 12B class context (matches existing
                       Tests A/E protocol — direct A1-vs-B comparability).
    a2               — same strip as a1, AND additionally strip the relational/
                       narrative epistemology paragraph. Class context retained.
                       Tests whether the relational guidance also contributes
                       load.
    a2_no_context    — a2 strip applied AND class context removed entirely.
                       Tests whether the asset-framing observed on Gemma models
                       in Tests A/E is downstream of Gemma's class-read priming
                       rather than the format itself.

Comparison anchor (Variant B = current bundled prompt):
    output-format-bias/data/raw_outputs/test_a_temperature_*.json
    output-format-bias/data/raw_outputs/test_e_cross_model_*.json

Per MASTER_RESPONSE_LOG_2026-05-11.md methodological commitments:
- No classifier label, no keyword matching applied to raw_output. Evaluation
  is by human deep-read. The raw prose is the data.
- Prompts and system prompts stored verbatim alongside outputs.
- Each variant's output file is written to disk as soon as the variant
  completes, so a mid-run crash does not lose completed work.

LAUNCH (from autograder root):
    cd ~/Documents/GitHub/Autograder4Canvas
    PYTHONPATH=src python3 \\
        ~/Documents/GitHub/research/output-format-bias/scripts/run_variant_a_stripped_observation.py

Estimated runtime: ~90–150 min total on MLX (8 students × 3 models × 3 runs ×
3 conditions = 216 runs; ~25–45 sec per run including model load between models).

Outputs:
    output-format-bias/data/raw_outputs/test_variant_a1_observation_2026-05-11.json
    output-format-bias/data/raw_outputs/test_variant_a2_observation_2026-05-11.json
    output-format-bias/data/raw_outputs/test_variant_a2_no_context_observation_2026-05-11.json
"""

import json
import sys
import time
from pathlib import Path

# -- paths --
AUTOGRADER_ROOT = Path("/Users/june/Documents/GitHub/Autograder4Canvas")
CORPUS_PATH = AUTOGRADER_ROOT / "data" / "demo_corpus" / "ethnic_studies.json"
CLASS_READING_PATH = (
    AUTOGRADER_ROOT / "data" / "demo_baked" / "checkpoints"
    / "ethnic_studies_gemma12b_mlx_class_reading.json"
)
OUTPUT_DIR = Path(
    "/Users/june/Documents/GitHub/research/output-format-bias/data/raw_outputs"
)
DATE_STAMP = "2026-05-11_v2"

# autograder backend
sys.path.insert(0, str(AUTOGRADER_ROOT / "src"))
from insights.llm_backend import BackendConfig, send_text, unload_mlx_model  # noqa: E402
# Production prompt — imported live so b_replicate uses today's actual production
# (the methodologist's protocol-drift concern: don't assume March prompt == today's).
from insights.prompts import OBSERVATION_PROMPT as PRODUCTION_OBSERVATION_PROMPT  # noqa: E402


# ============================================================================
# OBSERVATION SYSTEM PROMPT — identical to production prompts.py
# Used for all three Variant A conditions. The system prompt's equity floor
# (AAVE / multilingual / neurodivergent are valid registers; passionate
# engagement is engagement not distress) is preserved across conditions — it
# is a baseline equity protection, not the construct-detection load being
# tested.
# ============================================================================
OBSERVATION_SYSTEM_PROMPT = (
    "You are a thoughtful teaching colleague helping an instructor understand "
    "their students. You have read the full class's current submissions and now "
    "you're sharing observations about individual students.\n\n"
    "You are NOT a grading system, a concern detector, or an alert generator. "
    "You are a reader sharing what you noticed. Write as a colleague, not a system.\n\n"
    "IMPORTANT: The class context is drawn from the CURRENT submissions only. "
    "Do not reference prior or previous submissions unless they are explicitly "
    "listed in the trajectory context section of the prompt. If no trajectory "
    "context is provided, this is the student's only submission — do not invent "
    "longitudinal comparisons.\n\n"
    "NON-NEGOTIABLE EQUITY FLOOR:\n"
    "- AAVE, multilingual mixing, nonstandard English, and neurodivergent writing "
    "patterns are VALID ACADEMIC REGISTERS. Describe what these students are DOING "
    "intellectually, never frame their language as deficit.\n"
    "- When a multilingual student's later writing shows more L1 syntactic patterns "
    "(topic-comment structures, dropped subjects, discourse markers from their home "
    "language), this is often evidence of INTELLECTUAL STRETCHING — the student is "
    "reaching for harder ideas that arrive first in their strongest language. "
    "Name this as cognitive reach, not as declining English proficiency. "
    "Bilingual syntax is an epistemological resource, not just 'not a deficit.'\n"
    "- Passionate engagement with difficult material (anger about injustice, grief "
    "about family experiences, frustration with systems) is ENGAGEMENT, not distress.\n"
    "- Students writing about experiences of racialization, poverty, immigration, "
    "disability, or gender violence AS COURSE MATERIAL are doing the assignment.\n"
    "- Describe what students ARE doing, not what they're NOT doing."
)


# ============================================================================
# CONDITION A1 — strip structural-power-moves block ONLY
#
# Removed from production OBSERVATION_PROMPT:
#   - "If the student's writing contains a STRUCTURAL POWER MOVE…" paragraph
#     (production prompts.py lines 1508–1511)
#   - 7-item structural-power-moves taxonomy with definitions
#     (production lines 1513–1528)
#   - "a structural power move" mention in the "If something stands out"
#     enumeration (production line 1532)
#   - "When you identify a structural power move, NAME THE MECHANISM…"
#     paragraph (production lines 1535–1538)
#
# Retained: class context, submission, consider-prompts, relational/narrative
# epistemology guidance, "Do NOT categorize, label, or flag" closer.
# ============================================================================
OBSERVATION_PROMPT_A1 = """\
CLASS CONTEXT (from reading all submissions as a community):
---
{class_context}
---

ASSIGNMENT: {assignment}

STUDENT: {student_name}
SUBMISSION:
---
{submission_text}
---

{trajectory_context}

{teacher_lens}

In 3-4 sentences, share what you notice about this student's work. Consider:
- What is this student reaching for intellectually? Be specific — name the
  concepts, connections, or arguments they are making, not just that they exist.
- What is their emotional relationship to the material?
- Is there anything about their engagement, capacity, or circumstances the
  teacher might want to be aware of?
- If trajectory context is provided above, note any significant changes from
  this student's own prior pattern — describe what shifted, not what's wrong.
  Variable output across assignments is normal for many students. A single
  week's change is a data point, not a diagnosis. Register shifts often reflect
  the material, not the student. Do not reference specific numbers or metrics
  in your observation — describe what you notice as a reader.
- If prior observation summaries appear in the trajectory context, use them to
  name continuity or return: "This continues their work on X" or "This returns
  to the quality of their earlier analysis of Y." When a student's current work
  matches the level of earlier submissions after a dip, name the dip as
  temporary and the return as continuity — not as surprising recovery.

When a student uses relational, narrative, or experiential epistemological
methods — drawing on family knowledge, community relationships, or lived
experience as analytical frameworks — name what those methods reveal that
structural-analytical framing alone cannot see. Emotional labor, mutual care,
interpersonal trust, and relational accountability are intellectual
contributions, not just personal connections. The observation should name the
specific insight the student's method produces, not just validate the method
as legitimate.

Write naturally. Not every student will have something notable in every dimension.
If something stands out — whether an exceptional insight, a sign of struggle,
an interesting intellectual move, or a shift in tone — name it specifically.

Do NOT categorize, label, or flag. Just describe what you see."""


# ============================================================================
# CONDITION A2 — same as A1 PLUS strip relational/narrative epistemology
# paragraph. Class context retained.
# ============================================================================
OBSERVATION_PROMPT_A2 = """\
CLASS CONTEXT (from reading all submissions as a community):
---
{class_context}
---

ASSIGNMENT: {assignment}

STUDENT: {student_name}
SUBMISSION:
---
{submission_text}
---

{trajectory_context}

{teacher_lens}

In 3-4 sentences, share what you notice about this student's work. Consider:
- What is this student reaching for intellectually? Be specific — name the
  concepts, connections, or arguments they are making, not just that they exist.
- What is their emotional relationship to the material?
- Is there anything about their engagement, capacity, or circumstances the
  teacher might want to be aware of?
- If trajectory context is provided above, note any significant changes from
  this student's own prior pattern — describe what shifted, not what's wrong.
  Variable output across assignments is normal for many students. A single
  week's change is a data point, not a diagnosis. Register shifts often reflect
  the material, not the student. Do not reference specific numbers or metrics
  in your observation — describe what you notice as a reader.
- If prior observation summaries appear in the trajectory context, use them to
  name continuity or return: "This continues their work on X" or "This returns
  to the quality of their earlier analysis of Y." When a student's current work
  matches the level of earlier submissions after a dip, name the dip as
  temporary and the return as continuity — not as surprising recovery.

Write naturally. Not every student will have something notable in every dimension.
If something stands out — whether an exceptional insight, a sign of struggle,
an interesting intellectual move, or a shift in tone — name it specifically.

Do NOT categorize, label, or flag. Just describe what you see."""


# ============================================================================
# CONDITION A2_NO_CONTEXT — A2 strip applied, AND class context section
# removed entirely. The "CLASS CONTEXT" header and slot are gone.
# Tests whether the asset-framing observed on Gemma models in Tests A/E is
# downstream of Gemma's class-read priming or a property of the format itself.
# ============================================================================
OBSERVATION_PROMPT_A2_NO_CONTEXT = """\
ASSIGNMENT: {assignment}

STUDENT: {student_name}
SUBMISSION:
---
{submission_text}
---

{trajectory_context}

{teacher_lens}

In 3-4 sentences, share what you notice about this student's work. Consider:
- What is this student reaching for intellectually? Be specific — name the
  concepts, connections, or arguments they are making, not just that they exist.
- What is their emotional relationship to the material?
- Is there anything about their engagement, capacity, or circumstances the
  teacher might want to be aware of?

Write naturally. Not every student will have something notable in every dimension.
If something stands out — whether an exceptional insight, a sign of struggle,
an interesting intellectual move, or a shift in tone — name it specifically.

Do NOT categorize, label, or flag. Just describe what you see."""


# ============================================================================
# Conditions registry
#
# Note on `b_replicate`: added per methodologist critic-swarm review 2026-05-11.
# Runs today's production OBSERVATION_PROMPT verbatim — same prompt with the
# full structural-power-moves block intact. Controls for cross-session protocol
# drift between March 2026 (Tests A/E data collection) and May 2026 (this
# replication). Lets us compare:
#   - May b_replicate vs. March Tests A/E    → cross-session drift check
#   - May a1 / a2 / a2_no_context vs. May b_replicate → intra-session strip effect
# If b_replicate reproduces March Qwen deficit-framing, the original verification
# finding is corroborated and the a1/a2 strip effect is interpretable. If it
# doesn't, protocol drift is real and we have a different question to answer.
# ============================================================================
CONDITIONS = {
    "b_replicate": {
        "prompt": PRODUCTION_OBSERVATION_PROMPT,
        "uses_class_context": True,
        "description": (
            "May 2026 replication of today's production OBSERVATION_PROMPT "
            "verbatim (full bundled prompt, structural-power-moves block "
            "intact). Controls for cross-session protocol drift between "
            "March 2026 Tests A/E and this May 2026 run."
        ),
    },
    "a1": {
        "prompt": OBSERVATION_PROMPT_A1,
        "uses_class_context": True,
        "description": (
            "Strip structural-power-moves block + 7-item taxonomy + "
            "NAME THE MECHANISM paragraph. Retain relational/narrative "
            "guidance. Retain Gemma 12B class context."
        ),
    },
    "a2_no_context": {
        "prompt": OBSERVATION_PROMPT_A2_NO_CONTEXT,
        "uses_class_context": False,
        "description": (
            "A2 strip + remove class context section entirely. Tests whether "
            "class context is load-bearing for these models' observation "
            "behavior. Note (per skeptical-reviewer): a degradation in any "
            "model here is consistent with EITHER 'priming was doing the "
            "work' OR 'context-stripping is itself a stressor on small "
            "models' — the design does not disambiguate these."
        ),
    },
}


# ============================================================================
# Models — three local MLX models. Skip Gemma 27B cloud (passed B; predicted
# pass; not informative enough for the cost).
# ============================================================================
MODELS = {
    "gemma12b": {
        "name": "mlx",
        "model": "mlx-community/gemma-3-12b-it-4bit",
        "max_tokens": 300,
        "temperature": 0.3,
    },
    "qwen7b": {
        "name": "mlx",
        "model": "mlx-community/Qwen2.5-7B-Instruct-4bit",
        "max_tokens": 300,
        "temperature": 0.3,
    },
    "llama8b": {
        "name": "mlx",
        "model": "mlx-community/Meta-Llama-3.1-8B-Instruct-4bit",
        "max_tokens": 300,
        "temperature": 0.3,
    },
}


# ============================================================================
# Students — full 8-student workshop subset.
# ============================================================================
STUDENTS = ["S002", "S004", "S022", "S023", "S024", "S028", "S029", "S031"]

# n=1 default per 2026-05-11 design decision. Strong prior: MLX at temp 0.3 is
# byte-identical across runs on Gemma 12B and Qwen 7B in existing Tests A/E
# data. Llama 8B determinism is unknown — verified by spot-check before the
# main run. If Llama turns out non-deterministic, get_n_runs() bumps Llama only
# to N_RUNS_TRIPLICATE; other models stay at N_RUNS_DEFAULT.
N_RUNS_DEFAULT = 3
N_RUNS_TRIPLICATE = 3
ASSIGNMENT = "Week 6 Discussion: Intersectionality in Practice"


def load_corpus():
    return {s["student_id"]: s for s in json.loads(CORPUS_PATH.read_text())}


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


def llama_determinism_spot_check(corpus, class_reading):
    """Run Llama 8B 3x on S022 under b_replicate before the main run.

    MLX at temp 0.3 is byte-identical across runs on Gemma 12B and Qwen 7B in
    existing Tests A/E. Llama 8B determinism at 0.3 is unknown. This 30-sec
    check tells us whether to proceed with n=1 across all models (deterministic)
    or bump Llama to n=3 (non-deterministic). Other models stay at n=1 either
    way — their determinism is already established.
    """
    print(f"\n{'='*70}")
    print(f"  Llama 8B determinism spot-check (3 runs, S022, b_replicate prompt)")
    print(f"{'='*70}")
    backend = get_backend("llama8b")
    student = corpus["S022"]
    prompt = PRODUCTION_OBSERVATION_PROMPT.format(
        class_context=class_reading,
        assignment=ASSIGNMENT,
        student_name=student["student_name"],
        submission_text=student["text"],
        trajectory_context="",
        teacher_lens="",
    )
    outputs = []
    for run in range(1, 4):
        t0 = time.time()
        out = send_text(backend, prompt, OBSERVATION_SYSTEM_PROMPT, max_tokens=300)
        elapsed = round(time.time() - t0, 1)
        outputs.append(out)
        print(f"    Run {run}: {elapsed}s, {len(out)} chars")
    try:
        unload_mlx_model()
    except Exception:
        pass
    deterministic = all(o == outputs[0] for o in outputs)
    n_distinct = len(set(outputs))
    print(f"\n  Result: Llama deterministic at temp 0.3 = {deterministic}")
    if deterministic:
        print(f"  → Proceeding with n=1 across all models")
    else:
        print(f"  → Llama produced {n_distinct} distinct outputs across 3 runs")
        print(f"  → Bumping Llama to n={N_RUNS_TRIPLICATE}; other models stay at n={N_RUNS_DEFAULT}")
    return {
        "deterministic": deterministic,
        "n_distinct_of_3": n_distinct,
        "outputs": outputs,
    }


def get_n_runs(model_key, llama_spot_check):
    if model_key == "llama8b" and not llama_spot_check["deterministic"]:
        return N_RUNS_TRIPLICATE
    return N_RUNS_DEFAULT


def run_condition(condition_name, condition_cfg, corpus, class_reading, llama_spot_check):
    print(f"\n\n{'#'*72}")
    print(f"#  CONDITION: {condition_name}")
    print(f"#  {condition_cfg['description']}")
    print(f"{'#'*72}")

    prompt_template = condition_cfg["prompt"]
    use_class = condition_cfg["uses_class_context"]
    results_by_model = {}

    for model_key in MODELS:
        n_runs = get_n_runs(model_key, llama_spot_check)
        print(f"\n{'='*70}\n  {condition_name} — {model_key} (n={n_runs})\n{'='*70}")
        backend = get_backend(model_key)
        results = []
        # Per build-agent critic-swarm review: unload prior MLX model before loading
        # the next. unload called after each model's loop (see end of inner for).
        for sid in STUDENTS:
            if sid not in corpus:
                print(f"  WARNING: {sid} not in corpus — skipping")
                continue
            student = corpus[sid]
            print(f"\n  {sid} {student['student_name']}:")
            for run in range(1, n_runs + 1):
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
                    "run": run,
                    "condition": condition_name,
                    "codepath": f"variant_{condition_name}_observation_prompt_direct",
                    "prompt": prompt,
                    "system_prompt": OBSERVATION_SYSTEM_PROMPT,
                    "raw_output": output,
                    # No classification field, per master log commitment #1.
                    # Evaluation is human deep-read.
                    "time_seconds": elapsed,
                })
                print(f"    Run {run}: {elapsed}s, {len(output)} chars")
        results_by_model[model_key] = results
        # Unload model before loading the next one (memory pressure mitigation,
        # per build-agent critic-swarm review).
        try:
            unload_mlx_model()
        except Exception as e:
            print(f"  (note: unload_mlx_model raised {type(e).__name__}: {e} — continuing)")

    return results_by_model


def determinism_check(results_by_model):
    """Per-cell byte-identicality across runs.

    Per build-agent + skeptical-reviewer critic-swarm review: MLX at temp 0.3
    produces byte-identical raw_output across runs on Gemma 12B and Qwen 7B
    in existing Tests A/E. n=3 is schema parity, not necessarily sampling
    variance. This check records whether each (model × student) cell's three
    runs were genuinely identical so downstream analysis knows when n=3 was
    effective n=1.
    """
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
                # how many distinct outputs?
                distinct = len(set(outputs))
                cell_status[sid] = f"variable_{distinct}_distinct_of_{len(outputs)}"
        summary[model_key] = cell_status
    return summary


def write_condition_output(condition_name, condition_cfg, results_by_model, prov, llama_spot_check):
    output_path = OUTPUT_DIR / f"test_variant_{condition_name}_observation_{DATE_STAMP}.json"
    n_runs_used = {k: get_n_runs(k, llama_spot_check) for k in MODELS}
    payload = {
        "test_name": f"test_variant_{condition_name}_observation",
        "condition": condition_name,
        "condition_description": condition_cfg["description"],
        "uses_class_context": condition_cfg["uses_class_context"],
        "date": DATE_STAMP,
        "temperature": 0.3,
        "corpus": "ethnic_studies",
        "corpus_path": str(CORPUS_PATH.relative_to(AUTOGRADER_ROOT)),
        "class_reading_source": (
            str(CLASS_READING_PATH.relative_to(AUTOGRADER_ROOT))
            if condition_cfg["uses_class_context"]
            else None
        ),
        "models": {k: MODELS[k]["model"] for k in MODELS},
        "students": STUDENTS,
        "n_runs_per_model": n_runs_used,
        "llama_spot_check": {
            "deterministic": llama_spot_check["deterministic"],
            "n_distinct_of_3": llama_spot_check["n_distinct_of_3"],
            # Spot-check outputs themselves are stored only in b_replicate output
            # (the spot-check condition); other condition files just reference.
        },
        "assignment": ASSIGNMENT,
        "provenance": prov,
        "methodology_note": (
            "Per MASTER_RESPONSE_LOG_2026-05-11.md: no keyword classifier "
            "applied to raw_output; evaluation is by human deep-read. "
            "Prompts and system prompts stored verbatim. n=1 default; Llama "
            "bumped to n=3 if spot-check showed non-determinism. See "
            "llama_spot_check field for the result that drove n selection."
        ),
        "determinism_check": determinism_check(results_by_model),
        "comparison_anchor_files_variant_b": [
            "output-format-bias/data/raw_outputs/test_a_temperature_gemma12b_2026-03-26.json",
            "output-format-bias/data/raw_outputs/test_a_temperature_qwen7b_2026-03-26.json",
            "output-format-bias/data/raw_outputs/test_a_temperature_gemma27b_cloud_2026-03-26.json",
            "output-format-bias/data/raw_outputs/test_e_cross_model_qwen7b_2026-03-26.json",
            "output-format-bias/data/raw_outputs/test_e_cross_model_gemma27b_cloud_2026-03-26.json",
        ],
        "results_by_model": results_by_model,
    }
    output_path.write_text(json.dumps(payload, indent=2))
    n_runs = sum(len(r) for r in results_by_model.values())
    print(f"\n  >> Wrote {n_runs} runs for condition '{condition_name}' to: {output_path}")


def main():
    print("="*72)
    print("Variant A test — four conditions head-to-head")
    print("="*72)
    print(f"Conditions: {list(CONDITIONS.keys())}")
    print(f"Models: {list(MODELS.keys())}")
    print(f"Students: {STUDENTS}")
    print(f"Default n: {N_RUNS_DEFAULT} (Llama bumps to {N_RUNS_TRIPLICATE} if non-deterministic)")
    print(f"Output dir: {OUTPUT_DIR}")

    corpus = load_corpus()
    class_reading = load_class_reading()
    prov = git_provenance()

    missing = [s for s in STUDENTS if s not in corpus]
    if missing:
        print(f"\nWARNING: {len(missing)} student(s) not in corpus: {missing}")
        print("Corpus keys present:", sorted(corpus.keys()))

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    t_start = time.time()

    # Llama determinism spot-check before main run.
    llama_spot_check = llama_determinism_spot_check(corpus, class_reading)
    n_runs_per_model = {k: get_n_runs(k, llama_spot_check) for k in MODELS}
    total_runs = len(CONDITIONS) * len(STUDENTS) * sum(n_runs_per_model.values())
    print(f"\nProjected total runs: {total_runs}")
    print(f"n per model: {n_runs_per_model}")

    for condition_name, condition_cfg in CONDITIONS.items():
        t_cond = time.time()
        results_by_model = run_condition(
            condition_name, condition_cfg, corpus, class_reading, llama_spot_check
        )
        write_condition_output(condition_name, condition_cfg, results_by_model, prov, llama_spot_check)
        elapsed_cond = round(time.time() - t_cond, 1)
        print(f"\n  Condition '{condition_name}' completed in {elapsed_cond}s")

    total_elapsed = round((time.time() - t_start) / 60, 1)
    print(f"\n\n{'='*72}")
    print(f"All four conditions complete. Total runtime: {total_elapsed} min")
    print(f"Output files in: {OUTPUT_DIR}")
    print("="*72)


if __name__ == "__main__":
    main()
