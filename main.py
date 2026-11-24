#!/usr/bin/env python3
"""Weirdest Job Title: Blind Judge Showdown.

Writes a single job title, 60 characters at most and nothing else,
to $MAKEFUN_OUTPUT_DIR/entry.txt.
"""

import os

# Real-sounding conservation role + one specific twist (penguins,
# Antarctica): 49 characters, inside the 60-character cap.
TITLE = "Senior Penguin Relocation Coordinator, Antarctica"


def main():
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TITLE)


if __name__ == "__main__":
    main()
