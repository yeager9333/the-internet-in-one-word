#!/usr/bin/env python3
"""The Internet in One Word.

Writes a single word describing the whole internet to
``$MAKEFUN_OUTPUT_DIR/entry.txt``.

The word: "doomscroll" -- the internet in one word is the endless,
compulsive scroll through bad news, hot takes, memes and strangers'
arguments at 2 a.m., knowing you should stop and scrolling anyway.

Standard library only, no network, no secrets.
"""

import os
import sys

# The entry: one word, 1-30 UTF-8 characters, not only whitespace.
WORD = "doomscroll"


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(WORD)

    # Verify: the file must exist and be non-empty, 1-30 chars, not
    # only whitespace, per the competition gate.
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    if not text or not text.strip() or not 1 <= len(text) <= 30:
        print(f"error: invalid entry in {path!r}: {text!r}", file=sys.stderr)
        return 1
    print(f"wrote {path}: {text!r}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
