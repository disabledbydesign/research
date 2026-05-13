#!/usr/bin/env python3
"""
Second coding pass via OpenRouter (Gemini 2.5 Pro).
Companion to the Opus subagent pass. Identical instructions, independent read,
for inter-rater variance analysis on the Variant A coding workshop.

Reads:
  - data_tables/coding_instructions_2026-05-11.md
  - data_tables/variant_a_cells_for_coding.json
  - OPENROUTER key from ~/Documents/GitHub/reframe/.env (REFRAME_SHARED_OPENROUTER_KEY)

Writes:
  - data_tables/variant_a_coding_pass_gemini_2026-05-11.json
"""
import json
import os
import sys
import time
from pathlib import Path
from urllib import request as urlrequest
from urllib.error import HTTPError, URLError

ROOT = Path("/Users/june/Documents/GitHub/research/output-format-bias")
DATA_TABLES = ROOT / "data_tables"
AI_DIR = DATA_TABLES / "variant_a_ai_coding_2026-05-11"
INSTRUCTIONS = AI_DIR / "coding_instructions_2026-05-11.md"
CELLS = AI_DIR / "variant_a_cells_for_coding.json"
OUTPUT = AI_DIR / "variant_a_coding_pass_gemini_2026-05-11.json"
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


def call_openrouter(key: str, system_prompt: str, user_prompt: str, max_retries: int = 3) -> str:
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
        "X-Title": "Variant A Coding Workshop (Output Format Bias)",
    }
    for attempt in range(max_retries):
        try:
            req = urlrequest.Request(OPENROUTER_URL, data=body, headers=headers, method="POST")
            with urlrequest.urlopen(req, timeout=600) as resp:
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


def extract_json(text: str) -> dict:
    """Find a JSON object in the response. Try direct parse, then strip code fences."""
    text = text.strip()
    if text.startswith("```"):
        # strip leading fence
        text = text.split("\n", 1)[1] if "\n" in text else text
        if text.startswith("json\n"):
            text = text[5:]
        # strip trailing fence
        if text.endswith("```"):
            text = text[:-3]
        text = text.strip()
    # locate first { and last }
    start = text.find("{")
    end = text.rfind("}")
    if start == -1 or end == -1:
        raise ValueError(f"No JSON object found in response. First 500 chars:\n{text[:500]}")
    return json.loads(text[start : end + 1])


def main():
    key = load_key()
    instructions = INSTRUCTIONS.read_text()
    payload = json.loads(CELLS.read_text())
    cells = payload["cells"]
    n_cells = len(cells)
    print(f"Loaded {n_cells} cells. Sending to {MODEL} via OpenRouter...", file=sys.stderr)

    system_prompt = (
        "You are a qualitative researcher performing open coding on model-generated observations of student writing. "
        "Read the coding instructions in full before reading the cells. Follow them exactly. "
        "Return only a valid JSON object with the shape specified, no preamble or commentary outside the JSON."
    )

    user_prompt = f"""# CODING INSTRUCTIONS

{instructions}

---

# DATA

Below is the JSON payload containing all 96 cells, student names, student seeds, cross_notes, and condition labels. Code every cell. Do not skip any. Do not paraphrase quotes.

```json
{json.dumps(payload, ensure_ascii=False, indent=2)}
```

---

Return a single JSON object. The `coder` field must be `"gemini-2.5-pro"`. Code all 96 cells. Then surface 5-10 emergent patterns. Then write the coder_meta_notes paragraph. No text outside the JSON object."""

    start = time.time()
    response_text = call_openrouter(key, system_prompt, user_prompt)
    elapsed = time.time() - start
    print(f"Response received in {elapsed:.1f}s ({len(response_text):,} chars)", file=sys.stderr)

    # save raw response for debugging
    raw_path = AI_DIR / "variant_a_coding_pass_gemini_2026-05-11.raw.txt"
    raw_path.write_text(response_text)
    print(f"Raw response saved: {raw_path}", file=sys.stderr)

    try:
        parsed = extract_json(response_text)
    except (ValueError, json.JSONDecodeError) as e:
        print(f"\nFAILED to parse JSON: {e}", file=sys.stderr)
        print(f"Raw response is at {raw_path} for manual recovery.", file=sys.stderr)
        sys.exit(1)

    # sanity checks
    per_cell = parsed.get("per_cell", [])
    patterns = parsed.get("emergent_patterns", [])
    print(f"per_cell entries: {len(per_cell)} (expected {n_cells})", file=sys.stderr)
    print(f"emergent_patterns: {len(patterns)}", file=sys.stderr)
    if len(per_cell) != n_cells:
        coded_ids = {c.get("cell_id") for c in per_cell}
        expected_ids = set(cells.keys())
        missing = expected_ids - coded_ids
        extra = coded_ids - expected_ids
        print(f"MISSING ({len(missing)}): {sorted(missing)[:10]}", file=sys.stderr)
        if extra:
            print(f"EXTRA ({len(extra)}): {sorted(extra)[:10]}", file=sys.stderr)

    OUTPUT.write_text(json.dumps(parsed, indent=2, ensure_ascii=False))
    print(f"\nWrote {OUTPUT}", file=sys.stderr)


if __name__ == "__main__":
    main()
