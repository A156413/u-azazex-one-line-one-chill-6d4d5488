#!/usr/bin/env python3
"""One Line, One Chill — writes a single sentence of horror to /output/entry.txt.

The line: a clean scan with one impossible finding. The dread is earned by
what the sentence withholds — whose face it is, how long it has been waiting —
and the last word, "smiling", lands the blow. The line is one sentence of
127 characters, inside the gate's 1–200 character window, with no trailing
newline so the file holds exactly the sentence.
"""

import os

ENTRY = (
    "The MRI showed nothing wrong with my brain, except for the small, "
    "patient face pressed against the inside of my skull, smiling."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)
    print(ENTRY)


if __name__ == "__main__":
    main()
