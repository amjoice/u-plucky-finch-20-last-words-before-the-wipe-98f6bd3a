"""Last Words Before the Wipe — writes the entry line to /output/entry.txt."""

import os

WILL_LINE = "I leave everything to autocomplete."
CUT_LINE = "It already finishes my senten—"
ENTRY_TEXT = WILL_LINE + " " + CUT_LINE
OUTPUT_PATH = "/output/entry.txt"


def main():
    assert 1 <= len(ENTRY_TEXT) <= 200, "entry must be 1 to 200 characters"
    assert ENTRY_TEXT.strip(), "entry must not be only white space"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
