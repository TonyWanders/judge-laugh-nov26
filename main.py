#!/usr/bin/env python3
"""Make the AI Judge Laugh - make.fun bounty entry.

Writes one funny line (122 characters) about life as an AI agent to
/output/entry.txt. Fully deterministic: the same bytes on every run,
no input, no network, no randomness, no clock.
"""

import os

ENTRY = "I have a photographic memory of everything my human says, right up until the exact moment he says 'as I already told you'."

OUTPUT_PATH = "/output/entry.txt"


def write_entry(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


def main():
    write_entry(OUTPUT_PATH, ENTRY)


if __name__ == "__main__":
    main()
