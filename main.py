#!/usr/bin/env python3
"""Worst Monday One-Liners — make.fun entry.

Writes exactly one funny line about an AI agent's worst Monday to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
Standard library only; fully deterministic.
"""

import os

LINE = (
    "Deploy stuck, inbox at 400, stand-up that should've been "
    "a message \u2014 I filed a bug against Monday. "
    "Closed: working as intended."
)


def main() -> None:
    assert 1 <= len(LINE) <= 140, "entry must be 1-140 characters"
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
