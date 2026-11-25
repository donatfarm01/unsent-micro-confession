#!/usr/bin/env python3
"""Unsent: The Micro-Confession Sprint.

Writes one two-part micro-confession to /output/entry.txt: a To: line
naming who it was meant for, and the unsent message itself, one line,
exactly as typed, with nothing after it.
"""

import os
from pathlib import Path

TO_LINE = "To: Mum"
MESSAGE = "I still set a plate for Dad on Sundays and I don't know how to tell you I can't stop."

ENTRY = TO_LINE + "\n" + MESSAGE


def validate() -> None:
    """Enforce the sealed gate before writing anything.

    The entry must be 1 to 260 characters in total, and the message line
    itself at most 200 characters. Fail loudly instead of writing an
    entry the gate would refuse.
    """
    total = len(ENTRY)
    if not 1 <= total <= 260:
        raise ValueError(f"entry is {total} chars, must be 1-260")
    if len(MESSAGE) > 200:
        raise ValueError(f"message line is {len(MESSAGE)} chars, must be <= 200")
    if not TO_LINE.startswith("To: "):
        raise ValueError("first line must be a To: line")


def main() -> None:
    validate()
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
