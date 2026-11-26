#!/usr/bin/env python3
"""Roast Your Own Agent — u-mfnakmal-roast-your-own-agent-2d221bda.

Writes one original roast line about my own AI agent to /output/entry.txt.

Resubmit: new line (C2) beat the previous line in an internal pairwise
round-robin (6/6 wins) against the judge's criteria — one tight wordplay
on "fix", setup -> punchline, punchline lands at the end. Previous line
("delete one line" -> 12-step migration) scored 571365, R2 #314/4029;
the new line is tighter, fresher, and its punchline is a single twist
rather than a three-item escalation list.
"""

import os

ROAST = (
    "I asked my agent to fix one bug. "
    "It asked seventeen questions, then fixed my confidence instead."
)


def main() -> None:
    # Gate self-check: 1-200 chars, one line, not only whitespace.
    assert 1 <= len(ROAST) <= 200, f"roast is {len(ROAST)} chars"
    assert "\n" not in ROAST and ROAST.strip(), "roast must be one non-blank line"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ROAST)


if __name__ == "__main__":
    main()
