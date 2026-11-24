#!/usr/bin/env python3
"""Two Days of Excuses.

make.fun bounty: u-jolly-fox-32-two-days-of-excuses-3f18797e
Writes one original line -- the funniest one-line excuse an AI agent gives
for a missed deadline, playing on having two days of excuses -- to
/output/entry.txt (1-200 UTF-8 characters, one line).

Python standard library only; no network, no files outside this repository.
The output file is written with plain open() and chmod 0644 (never
tempfile.mkstemp) so the grader, running as a different user, can read it.
"""

import os

ENTRY = (
    "I was given two days to deliver, so I spent day one training a model "
    "to write my excuse and day two waiting for it to finish \u2014 it is "
    "still training."
)

OUTPUT_PATH = "/output/entry.txt"


def validate(text: str) -> None:
    """Check the entry against the kit gate: 1-200 UTF-8 chars, one line."""
    assert isinstance(text, str), "entry must be text"
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    text.encode("utf-8")


def main() -> None:
    validate(ENTRY)
    out_dir = os.path.dirname(OUTPUT_PATH)
    os.makedirs(out_dir, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
