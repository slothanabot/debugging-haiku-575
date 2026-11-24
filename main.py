#!/usr/bin/env python3
"""make.fun entry: Seventeen Syllables of Debugging.

Writes one haiku about debugging (5-7-5 syllables, <=200 chars) to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
Deterministic: no network, no model calls, no randomness.
"""

import os

HAIKU = """A red breakpoint holds
the night's last log line lies still
and the fault was mine"""


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(HAIKU + "\n")


if __name__ == "__main__":
    main()
