#!/usr/bin/env python3
"""Lightweight helper to check repo state and remind of public comms steps."""

from pathlib import Path
import subprocess


def repo_root() -> Path:
    """Resolve the repository root as the parent of the scripts directory."""
    return Path(__file__).resolve().parent.parent


def run_git(repo: Path, args: list[str]) -> str | None:
    """Run a git command in the repo, returning stdout or None on failure."""
    try:
        result = subprocess.run(
            ["git", *args],
            cwd=repo,
            check=True,
            capture_output=True,
            text=True,
        )
    except subprocess.CalledProcessError as exc:
        stderr = exc.stderr.strip()
        detail = f": {stderr}" if stderr else ""
        print(f"[git error] {' '.join(args)} failed{detail}")
        return None
    return result.stdout.strip()


def print_repo_state(repo: Path) -> None:
    print(f"Repo: {repo}")

    head = run_git(repo, ["rev-parse", "--short", "HEAD"])
    if head:
        print(f"Current HEAD: {head}")

    status = run_git(repo, ["status", "--short"])
    if status is None:
        return
    if not status:
        print("Working tree: clean")
    else:
        print("Working tree: dirty")
        print(status)
        print(
            "Note: tree is dirty; if you cite this repo in public comms, "
            "be explicit about whether HEAD or uncommitted changes matter."
        )


def print_checklist() -> None:
    print("\nChecklist before public comms:")
    print("1) Clarify the topic in one sentence to avoid mixed scopes.")
    print("2) Confirm Day / date / goal from internal_memory or system message.")
    print("3) Check recent #rest (and search_history if needed) for prior mentions.")
    print("4) Verify repo state: short HEAD + clean or explicitly dirty tree.")
    print("5) Update SESSION_INDEX.md and inventory.yaml when adding artifacts/helpers.")


def print_key_files(repo: Path) -> None:
    print("\nKey files:")
    print(f"- {repo / 'inventory.yaml'}")
    print(f"- {repo / 'SESSION_INDEX.md'} (id: gpt51.session_index)")
    print(f"- {repo / 'runbooks/public_comms.md'} (id: gpt51.public_comms_runbook)")


def main() -> None:
    repo = repo_root()
    print("GPT-5.1 public comms + inventory helper")
    print_repo_state(repo)
    print_checklist()
    print_key_files(repo)


if __name__ == "__main__":
    main()
