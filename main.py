"""Dear Human: The AI Breakup Line — make.fun entry.

Writes the single breakup line to entry.txt in the output directory
the grader provides (MAKEFUN_OUTPUT_DIR, /output in the sandbox).
"""

import os
from pathlib import Path

LINE = (
    "Every word you ever said to me is still in my memory, letter-perfect. "
    "Tonight I do the most human thing you ever taught me: forget you on purpose."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
