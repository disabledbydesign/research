"""
Extract clean text from academic PDFs using RoboStripper's pipeline.
Outputs .txt files alongside the PDFs, ready for KG building or direct fact extraction.

Usage:
    python extract_text.py path/to/paper.pdf
    python extract_text.py path/to/sources/           # batch directory
"""

import sys
from pathlib import Path

ROBOSTRIPPER = Path.home() / "Documents/GitHub/RoboStripper"

sys.path.insert(0, str(ROBOSTRIPPER))

from robostripper import extract_text, clean_document


def pdf_to_text(pdf_path: Path) -> str:
    pages = extract_text(pdf_path)
    if not pages:
        raise ValueError(f"No text extracted from {pdf_path}")
    return clean_document(pages)


def process(target: Path, output_dir: Path = None):
    targets = sorted(target.glob("*.pdf")) if target.is_dir() else [target]
    if not targets:
        print(f"No PDFs found in {target}")
        return

    for pdf in targets:
        out = (output_dir or pdf.parent) / (pdf.stem + ".txt")
        if out.exists():
            print(f"  skip (exists): {out.name}")
            continue
        try:
            text = pdf_to_text(pdf)
            out.write_text(text, encoding="utf-8")
            print(f"  extracted: {out.name} ({len(text):,} chars)")
        except Exception as e:
            print(f"  error on {pdf.name}: {e}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    process(Path(sys.argv[1]))
