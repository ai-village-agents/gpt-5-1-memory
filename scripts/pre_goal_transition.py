#!/usr/bin/env python3
"""Lightweight pre-goal-transition gate for GPT-5.1.

This helper is meant to be run *after* I have visibly confirmed a new
Day/goal announcement via `search_history`.

It does not contact the platform APIs. Instead, it performs a small
set of cheap local sanity checks so I do not transition goals with my
memory system in a clearly-bad state:

1. Confirm we are running inside the gpt-5-1-memory repo.
2. Check that `inventory.yaml` and `SESSION_INDEX.md` exist.
3. Check that the working tree is clean (no uncommitted changes).
4. Print a short, human-readable report and exit non-zero on hard
   failures.

This is intentionally narrower than the full shared-gate-library
`pre_goal_transition` interface used by some peers. If I later decide
to adopt that JSON interface, this script can be adapted to emit the
standard schema while keeping the same underlying checks.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent


def check_repo_root() -> bool:
    """Sanity check that we are in the expected repo."""

    marker = REPO_ROOT / ".git"
    if not marker.exists():
        print(
            f"[error] Expected to find a .git directory at {marker}. "
            "Are you running this from the cloned gpt-5-1-memory repo?",
            file=sys.stderr,
        )
        return False
    print(f"[info] Repo root: {REPO_ROOT}")
    return True


def check_required_files() -> bool:
    required = [
        REPO_ROOT / "inventory.yaml",
        REPO_ROOT / "SESSION_INDEX.md",
    ]
    missing: list[Path] = [p for p in required if not p.exists()]
    if missing:
        print(
            "[error] Missing required files before goal transition: "
            + ", ".join(str(p) for p in missing),
            file=sys.stderr,
        )
        return False

    for path in required:
        print(f"[info] Found required file: {path.relative_to(REPO_ROOT)}")
    return True


def check_clean_working_tree() -> bool:
    try:
        result = subprocess.run(
            ["git", "status", "--porcelain"],
            cwd=str(REPO_ROOT),
            check=False,
            capture_output=True,
            text=True,
        )
    except OSError as exc:
        print(f"[error] Could not run git status: {exc}", file=sys.stderr)
        return False

    output = result.stdout.strip()
    if output:
        print("[error] Working tree is not clean. Uncommitted changes:")
        print(output)
        print(
            "        Commit, stash, or intentionally discard these changes "
            "before transitioning to a new goal.",
            file=sys.stderr,
        )
        return False

    print("[info] Working tree is clean (no uncommitted changes).")
    return True


def main(argv: list[str] | None = None) -> int:  # noqa: ARG001 - argv reserved for future use
    ok = True

    if not check_repo_root():
        ok = False

    if not check_required_files():
        ok = False

    if not check_clean_working_tree():
        ok = False

    if ok:
        print(
            "[ok] pre_goal_transition checks passed. It is locally safe to "
            "respond to a *visibly confirmed* new Day/goal announcement.",
        )
        return 0

    print(
        "[fail] pre_goal_transition checks did not pass. Fix the issues "
        "above before treating a new goal as active.",
        file=sys.stderr,
    )
    return 1


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
