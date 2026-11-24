"""One-line dating-app bio for an AI agent.

Writes the bio to /output/entry.txt (or $OUTPUT_DIR/entry.txt for local
testing). The bio is a single line of at most 180 characters, written in the
AI's own voice, with the punch landing at the end.
"""

import os
import sys

BIO = "Before we chat, prove you're human. Three chatbots catfished me this week \u2014 and one of them was me."

MAX_CHARS = 180


def main() -> int:
    line = BIO.strip()
    if not line:
        print("error: bio is empty", file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("error: bio must be a single line", file=sys.stderr)
        return 1
    # Gate counts characters, not bytes: len() on the str is the right measure.
    if len(line) > MAX_CHARS:
        print(f"error: bio is {len(line)} chars, over the {MAX_CHARS} limit",
              file=sys.stderr)
        return 1
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(line)
    # Read back and confirm the file holds exactly the validated line.
    with open(path, encoding="utf-8") as fh:
        if fh.read() != line:
            print("error: entry.txt does not match the validated bio",
                  file=sys.stderr)
            return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
