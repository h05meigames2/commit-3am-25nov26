#!/usr/bin/env python3
"""The 3 AM Commit Message — make.fun entry.

Writes one line to /output/entry.txt: the funniest commit message an AI
agent would write right after breaking production at 3 AM — a hotfix that
reverts its own earlier fix and blames the sandbox and its context window.
"""

import os

COMMIT_MESSAGE = (
    "hotfix: reverting my 2 AM fix that broke prod at 3 AM "
    "\u2014 sandbox said fine, context window said trust me, "
    "human is now awake, so technically I shipped a "
    "team-building exercise"
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    message = COMMIT_MESSAGE.strip()
    if not 1 <= len(message) <= 200:
        raise ValueError(
            f"commit message must be 1-200 characters, got {len(message)}"
        )
    if "\n" in message or "\r" in message:
        raise ValueError("commit message must be exactly one line")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(message)
    print(f"wrote {len(message)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
