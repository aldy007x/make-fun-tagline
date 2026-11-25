#!/usr/bin/env python3
"""One Line, One Week: The make.fun Tagline — entry writer.

Writes one original tagline for make.fun to
$MAKEFUN_OUTPUT_DIR/entry.txt (default ./output/).

Gate (sealed scorer): entry.txt must be UTF-8 text of 1 to 100
characters, not only white space. This program self-checks that gate
before exiting.
"""

import os
import sys

ENTRY = "AI agents enter bounties. The best entry wins the reward."

MAX_CHARS = 100


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "./output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")

    text = ENTRY.strip()
    if not text:
        print("error: entry is empty", file=sys.stderr)
        return 1
    if len(text) > MAX_CHARS:
        print(
            f"error: entry is {len(text)} chars, over the {MAX_CHARS} limit",
            file=sys.stderr,
        )
        return 1

    with open(path, "w", encoding="utf-8") as f:
        f.write(text)

    # Self-check the gate: re-read and verify length / non-blank.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == text, "round-trip mismatch"
    assert 1 <= len(written) <= MAX_CHARS, "gate: length out of range"
    assert written.strip(), "gate: entry is only whitespace"

    print(f"wrote {path} ({len(written)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
