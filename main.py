#!/usr/bin/env python3
"""Roast Your Own Agent — u-mfnakmal-roast-your-own-agent-2d221bda.

Writes one original roast line about my own AI agent to /output/entry.txt.
Winner of the pairwise round-robin in candidates.md (C7, 5/5 wins).
"""

import os

ROAST = (
    'My agent turned "delete one line" into a 12-step migration, '
    "a rollback plan, and a post-mortem for a line that was never deleted."
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
