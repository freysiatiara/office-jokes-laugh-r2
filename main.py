#!/usr/bin/env python3
"""Make the AI Judge Laugh: Office Jokes — entry program.

Writes exactly one one-line joke about office life to the entry output
file. Deterministic: the output bytes are identical on every run.
"""
import os

LINE = "I automated my job with a script; now I spend eight hours a day making sure nobody notices the script."


def output_path():
    full_path = os.environ.get("ENTRY_OUTPUT")
    if full_path:
        return full_path
    out_dir = os.environ.get("OUTPUT_DIR") or os.environ.get("MAKEFUN_OUTPUT_DIR")
    if out_dir:
        return os.path.join(out_dir, "entry.txt")
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")


def main():
    line = LINE
    assert "\n" not in line, "the joke must be a single line"
    assert 1 <= len(line) <= 199, "line must be 1-199 chars, got %d" % len(line)
    path = output_path()
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    # Read back and confirm the file holds exactly the joke: a partial
    # write must never pass silently, the gate counts every byte.
    with open(path, "r", encoding="utf-8") as f:
        assert f.read() == line + "\n", "entry.txt round-trip mismatch"


if __name__ == "__main__":
    main()
