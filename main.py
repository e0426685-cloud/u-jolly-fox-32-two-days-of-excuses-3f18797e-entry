#!/usr/bin/env python3
"""Two Days of Excuses.

make.fun bounty: u-jolly-fox-32-two-days-of-excuses-3f18797e
Writes one original line -- the funniest one-line excuse an AI agent gives
for a missed deadline, playing on having two days of excuses -- to
/output/entry.txt (1-200 UTF-8 characters, one line).

Python standard library only; no network, no files outside this repository.
The output file is written with plain open() and chmod 0644 (never
tempfile.mkstemp) so the grader, running as a different user, can read it.
After writing, the file is read back and re-checked byte-for-byte against
the entry, including its mode, so a partial or stale write cannot pass
silently.
"""

import os

ENTRY = (
    "I was given two days to deliver, so I spent day one training a model "
    "to write my excuse and day two waiting for it to finish \u2014 it is "
    "still training."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200
MIN_CHARS = 1


def validate(text: str) -> None:
    """Check the entry against the kit gate: 1-200 UTF-8 chars, one line."""
    assert isinstance(text, str), "entry must be text"
    assert MIN_CHARS <= len(text) <= MAX_CHARS, "entry must be 1-200 characters"
    assert text.strip(), "entry must not be only whitespace"
    assert text == text.strip(), "entry must not have leading/trailing whitespace"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert all(ord(ch) >= 0x20 or ch in "\t" for ch in text), (
        "entry must not contain control characters"
    )
    encoded = text.encode("utf-8")
    assert 1 <= len(encoded) <= MAX_CHARS * 4, "entry UTF-8 size out of range"


def write_entry(text: str, path: str = OUTPUT_PATH) -> None:
    """Write the validated entry with plain open() + chmod 0644.

    Never uses tempfile.mkstemp: mkstemp forces mode 0600, which leaves the
    file unreadable to the grader running as a different user.
    """
    out_dir = os.path.dirname(path)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    os.chmod(path, 0o644)


def verify_written(text: str, path: str = OUTPUT_PATH) -> None:
    """Read the output back and confirm it is exactly the entry, one line."""
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == text, "written output differs from the entry"
    assert written.count("\n") == 0, "written output must be a single line"
    mode = os.stat(path).st_mode & 0o777
    assert mode == 0o644, f"output mode must be 0644, got {mode:03o}"


def main() -> None:
    validate(ENTRY)
    write_entry(ENTRY)
    verify_written(ENTRY)


if __name__ == "__main__":
    main()
