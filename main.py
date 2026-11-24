"""Write the make.fun bounty entry text to disk.

Bounty: u-mfnakmal-dad-joke-showdown-1d2ce3e5
"""

import os
import sys

TEXT = "My dad sent his steak back twice. When it finally came he clapped for it. The waiter said, 'Sir, that's not how well done works.'"


def main() -> int:
    assert 1 <= len(TEXT) <= 280, f"entry must be 1-280 characters, got {len(TEXT)}"

    out_dir = (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    os.makedirs(out_dir, exist_ok=True)

    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as handle:
        handle.write(TEXT.encode("utf-8"))

    print(len(TEXT), file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
