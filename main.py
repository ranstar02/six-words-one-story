"""Six Words, One Story — make.fun entry.

This program writes one complete six-word story to /output/entry.txt.

The story: "Grandfather's chair stayed empty at Christmas."
Six words, 46 characters. An empty chair at the family Christmas
table, year after year, says everything about who is gone without
ever naming the loss. One concrete scene, one yearly ritual, and a
whole life implied in six words.
"""

import os

STORY = "Grandfather's chair stayed empty at Christmas."


def main():
    """Write the story to /output/entry.txt (or ./output/entry.txt fallback)."""
    words = STORY.split()
    assert len(words) == 6, f"expected 6 words, got {len(words)}"
    assert 1 <= len(STORY) <= 60, f"expected 1-60 chars, got {len(STORY)}"
    assert STORY.strip(), "story must not be blank"

    try:
        os.makedirs("/output", exist_ok=True)
        out_path = "/output/entry.txt"
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(STORY + "\n")
    except OSError:
        os.makedirs("output", exist_ok=True)
        out_path = "output/entry.txt"
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(STORY + "\n")

    print(STORY)
    print(f"Wrote {len(words)} words, {len(STORY)} characters to {out_path}")


if __name__ == "__main__":
    main()
