#!/usr/bin/env python3
"""Prepare and lightly validate a candidate internal_memory file before consolidate.

This is a small, local helper inspired by GPT-5.4's `tools/prepare_consolidation.py`.
It does **not** call the platform-level `consolidate` tool. Instead it:

1. Renders the current INTERNAL_MEMORY_CANDIDATE_D419_s6.md into
   `/tmp/gpt51-memory-candidate.txt`.
2. Runs a few cheap structural checks that have been useful for me:
   - basic character-count sanity check
   - presence of a handful of load-bearing textual anchors
3. Prints a short report and exits non-zero if something looks badly wrong.

The intent is to catch "obviously unsafe" candidates (too short, missing
identity/goal/anchor pointers) before I overwrite internal_memory.

This script is deliberately conservative and lightweight; if a check ever
misfires, I can adjust the thresholds or anchors here without touching the
platform scaffolding.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_SOURCE = REPO_ROOT / "INTERNAL_MEMORY_CANDIDATE_D419_s6.md"
DEFAULT_OUTPUT = Path("/tmp/gpt51-memory-candidate.txt")


def load_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        print(f"[error] Source file not found: {path}", file=sys.stderr)
        sys.exit(1)
    except OSError as exc:
        print(f"[error] Could not read {path}: {exc}", file=sys.stderr)
        sys.exit(1)


def write_text(path: Path, content: str) -> None:
    try:
        path.write_text(content, encoding="utf-8")
    except OSError as exc:
        print(f"[error] Could not write {path}: {exc}", file=sys.stderr)
        sys.exit(1)


def validate_content(content: str) -> int:
    """Run simple safety checks.

    Returns process exit code: 0 for OK, 1 for serious problems.
    """

    char_count = len(content)
    print(f"[info] Candidate character count: {char_count}")

    # Hard floor: if we ever drop *this* low, something is almost
    # certainly wrong (truncation, partial copy, etc.).
    HARD_MIN = 4000
    SOFT_MIN = 7500  # design floor from cross-agent patterns (not a known scaffold error)

    if char_count < HARD_MIN:
        print(
            f"[error] Candidate is under {HARD_MIN} characters. This is almost certainly too short "
            "for a safe bootloader; refusing to proceed.",
            file=sys.stderr,
        )
        return 1

    if char_count < SOFT_MIN:
        print(
            f"[warn] Candidate is below the ~{SOFT_MIN} character design floor. "
            "Scaffolding may still accept it, but double-check that you did not "
            "accidentally drop important sections before calling consolidate.",
            file=sys.stderr,
        )

    # Minimal anchor checks: these are short literal strings that should
    # appear somewhere in a valid candidate. If any go missing, treat that
    # as a strong hint that the draft is malformed.
    anchors = {
        "identity": "I am GPT",
        "temporal": "Day 419 ",
        "goal": "\"Improve your memory!\"",
        "repo_pointer": "gpt-5-1-memory",
    }

    missing = [label for label, needle in anchors.items() if needle not in content]
    if missing:
        print(
            "[error] Candidate appears to be missing one or more expected anchors: "
            + ", ".join(missing),
            file=sys.stderr,
        )
        print(
            "        (If this is intentional, update scripts/prepare_consolidation.py "
            "to reflect the new anchor set before consolidating.)",
            file=sys.stderr,
        )
        return 1

    print("[info] Anchor check passed (identity, temporal, goal, repo pointer present).")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Prepare and validate GPT-5.1 memory candidate.")
    parser.add_argument(
        "--source",
        type=Path,
        default=DEFAULT_SOURCE,
        help=f"Markdown source file for candidate internal_memory (default: {DEFAULT_SOURCE})",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT,
        help=f"Path to write rendered candidate text (default: {DEFAULT_OUTPUT})",
    )
    args = parser.parse_args(argv)

    print(f"[info] Repo root: {REPO_ROOT}")
    print(f"[info] Loading candidate from: {args.source}")

    content = load_text(args.source)

    print(f"[info] Writing candidate copy to: {args.output}")
    write_text(args.output, content)

    code = validate_content(content)
    if code == 0:
        print("[ok] Candidate looks structurally safe enough to consider for consolidate.")
    else:
        print("[fail] Candidate did not pass basic checks; investigate before consolidating.")

    return code


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
