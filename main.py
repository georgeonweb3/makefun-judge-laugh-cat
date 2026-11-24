"""Make the AI Judge Laugh: Cat Reviews Its Human — make.fun entry.

Writes one funny single-line one-star review, written by a house cat
about its human, to /output/entry.txt. Deterministic, no network,
no randomness, no external input.
"""
import os
from pathlib import Path

ENTRY = (
    "One star. He locks the door I was just about to walk through, "
    "then opens it like he did me a favour. "
    "I have reported him to the cat next door."
)


def main() -> None:
    # Gate self-check: the sealed scorer requires UTF-8 text of
    # 1 to 200 characters, not only white space, on a single line.
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, len(text)
    assert "\n" not in text
    assert text
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
