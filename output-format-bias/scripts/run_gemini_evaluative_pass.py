#!/usr/bin/env python3
"""
Run the evaluative coding pass (pass 2) via OpenRouter using Gemini 2.5 Pro.

Each cell gets evaluative labels: TP / FP / hallucination / unclear, with verbatim
quotes from the model output and reasoning. Companion to the Opus subagent
evaluative pass for inter-coder variance.

Reads:
  - data_tables/variant_a_ai_coding_2026-05-11/evaluative_coding_instructions_2026-05-11.md
  - data_tables/variant_a_ai_coding_2026-05-11/evaluative_pass_input_gemini.json
  - OPENROUTER key from ~/Documents/GitHub/profile/.env (REFRAME_SHARED_OPENROUTER_KEY)

Writes:
  - data_tables/variant_a_ai_coding_2026-05-11/variant_a_evaluative_pass_gemini_2026-05-11.json
"""
import json
import os
import sys
import time
from pathlib import Path
from urllib import request as urlrequest
from urllib.error import HTTPError, URLError

ROOT = Path("/Users/june/Documents/GitHub/research/output-format-bias")
AI_DIR = ROOT / "data_tables" / "variant_a_ai_coding_2026-05-11"
INSTRUCTIONS = AI_DIR / "evaluative_coding_instructions_2026-05-11.md"
INPUT = AI_DIR / "evaluative_pass_input_gemini.json"
OUTPUT = AI_DIR / "variant_a_evaluative_pass_gemini_2026-05-11.json"
RAW_OUT = AI_DIR / "variant_a_evaluative_pass_gemini_2026-05-11.raw.txt"
ENV_FILE = Path.home() / "Documents/GitHub/profile/.env"

MODEL = "google/gemini-2.5-pro"
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"


def load_key():
    if not ENV_FILE.exists():
        sys.exit(f"ERROR: {ENV_FILE} not found")
    for line in ENV_FILE.read_text().splitlines():
        line = line.strip()
        if line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        if k.strip() == "REFRAME_SHARED_OPENROUTER_KEY":
            return v.strip().strip('"').strip("'")
    sys.exit("ERROR: REFRAME_SHARED_OPENROUTER_KEY not in env file")


def call_openrouter(key, system_prompt, user_prompt, max_retries=3):
    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        "temperature": 0.2,
        "max_tokens": 32000,
    }
    body = json.dumps(payload).encode("utf-8")
    headers = {
        "Authorization": f"Bearer {key}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://github.com/grouchyseafowl/research",
        "X-Title": "Variant A Evaluative Pass (Output Format Bias)",
    }
    for attempt in range(max_retries):
        try:
            req = urlrequest.Request(OPENROUTER_URL, data=body, headers=headers, method="POST")
            with urlrequest.urlopen(req, timeout=900) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                return data["choices"][0]["message"]["content"]
        except HTTPError as e:
            err_body = e.read().decode("utf-8", errors="replace")
            print(f"[attempt {attempt+1}] HTTP {e.code}: {err_body[:500]}", file=sys.stderr)
            if e.code in (429, 500, 502, 503, 504) and attempt < max_retries - 1:
                wait = 2 ** (attempt + 2)
                print(f"  retrying in {wait}s...", file=sys.stderr)
                time.sleep(wait)
                continue
            raise
        except URLError as e:
            print(f"[attempt {attempt+1}] URL error: {e}", file=sys.stderr)
            if attempt < max_retries - 1:
                time.sleep(2 ** (attempt + 2))
                continue
            raise
    raise RuntimeError("All retries failed")


def extract_json(text):
    text = text.strip()
    if text.startswith("```"):
        text = text.split("\n", 1)[1] if "\n" in text else text
        if text.startswith("json\n"):
            text = text[5:]
        if text.endswith("```"):
            text = text[:-3]
        text = text.strip()
    start = text.find("{")
    end = text.rfind("}")
    if start == -1 or end == -1:
        raise ValueError(f"No JSON object found. First 500 chars:\n{text[:500]}")
    return json.loads(text[start : end + 1])


def main():
    key = load_key()
    instructions = INSTRUCTIONS.read_text()
    bundle = json.loads(INPUT.read_text())
    n_cells = bundle["n_cells"]
    print(f"Loaded {n_cells} cells. Sending to {MODEL} via OpenRouter...", file=sys.stderr)

    system_prompt = (
        "You are a qualitative researcher performing evaluative coding (pass 2) on model-generated "
        "observations of student writing. You did open coding (pass 1) earlier; this pass adds "
        "TP/FP/hallucination/unclear verdicts grounded in the student submission. Read the coding "
        "instructions in full, then evaluate every cell. Return ONLY a valid JSON object with the "
        "specified shape, no preamble or commentary outside the JSON."
    )

    user_prompt = f"""# EVALUATIVE CODING INSTRUCTIONS

{instructions}

---

# INPUT BUNDLE

Below is the JSON bundle. Each cell contains: student_submission (verbatim student writing),
model_output (what the model said about the student), own_open_codes (your prior open-coded
description + quotes), and student_seed + cross_notes_for_student as orientation.

```json
{json.dumps(bundle, ensure_ascii=False, indent=2)}
```

---

Return a single JSON object with these top-level fields:
- `coder`: must be `"gemini-2.5-pro"`
- `pass`: `"evaluative"`
- `pass_date`: `"2026-05-11"`
- `per_cell`: array of 96 cell objects (one per cell_id)
- `coder_meta_notes`: 1 paragraph about your coding process

Code every cell. Quotes in the *_examples arrays MUST be verbatim substrings of the model_output. Use "unclear" honestly when the submission doesn't decide. No text outside the JSON."""

    start = time.time()
    response_text = call_openrouter(key, system_prompt, user_prompt)
    elapsed = time.time() - start
    print(f"Response received in {elapsed:.1f}s ({len(response_text):,} chars)", file=sys.stderr)

    RAW_OUT.write_text(response_text)
    print(f"Raw response saved: {RAW_OUT}", file=sys.stderr)

    try:
        parsed = extract_json(response_text)
    except (ValueError, json.JSONDecodeError) as e:
        print(f"\nFAILED to parse JSON: {e}", file=sys.stderr)
        sys.exit(1)

    per_cell = parsed.get("per_cell", [])
    print(f"per_cell entries: {len(per_cell)} (expected {n_cells})", file=sys.stderr)
    if len(per_cell) != n_cells:
        coded_ids = {c.get("cell_id") for c in per_cell}
        expected_ids = set(bundle["cells"].keys())
        missing = expected_ids - coded_ids
        extra = coded_ids - expected_ids
        print(f"MISSING ({len(missing)}): {sorted(missing)[:10]}", file=sys.stderr)
        if extra:
            print(f"EXTRA ({len(extra)}): {sorted(extra)[:10]}", file=sys.stderr)

    OUTPUT.write_text(json.dumps(parsed, indent=2, ensure_ascii=False))
    print(f"\nWrote {OUTPUT}", file=sys.stderr)


if __name__ == "__main__":
    main()
