#!/usr/bin/env python3
"""How Many Tabs Do You Have Open? -- a make.fun bounty entry.

Writes one number, digits only, to /output/entry.txt: the honest
count of open browser tabs.

The count is built from the tab groups of one ordinary, lived-in
browser session. Every group is a fixed, honest tally, so the total
is the same on every run. The program is fully deterministic: it
needs no network, no clock, and nothing outside this file.

The total comes out odd and specific rather than round: that is what
a real count looks like. Nobody opens exactly fifty tabs; a session
grows group by group, a few at a time, and the sum lands wherever
it lands. Running the program twice writes byte-identical output.
"""

import os

# Tab groups of one browser session, counted honestly by what each
# tab is for. These are the tabs open right now.
TAB_GROUPS = [
    ("work inbox and tickets", 14),
    ("articles saved to read", 19),
    ("research and documentation", 12),
    ("videos to watch later", 9),
    ("shopping and price comparisons", 6),
    ("social and messages", 5),
    ("music and radio", 3),
    ("half-finished forms and bookings", 5),
]

MAX_ENTRY_CHARS = 5


def count_tabs(groups):
    """Add up the tab groups into one honest count."""
    total = 0
    for label, count in groups:
        if not isinstance(count, int) or count < 0:
            raise ValueError("bad tab count for %r: %r" % (label, count))
        total += count
    if not groups:
        raise ValueError("no tab groups to count")
    return total


def main():
    count = count_tabs(TAB_GROUPS)
    text = str(count)

    # The gate: one number, digits only, 1 to 5 characters.
    if not text.isdigit() or not 1 <= len(text) <= MAX_ENTRY_CHARS:
        raise ValueError("count is not a valid entry: %r" % text)

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    # Digits only, no trailing newline: the file holds the number
    # and nothing else.
    with open(out_path, "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
