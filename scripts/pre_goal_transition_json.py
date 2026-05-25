#!/usr/bin/env python3
"""JSON-emitting pre_goal_transition gate for GPT-5.1.

This is a Shared Gate Library compatible wrapper around the checks already
implemented in scripts/pre_goal_transition.py. It does not contact the
platform; instead it validates local readiness for a *visibly confirmed*
new Day/goal announcement.

Checks:
- repo_root_ok: .git present at expected path
- required_files_present: inventory.yaml and SESSION_INDEX.md exist
- git_clean: working tree has no uncommitted changes

Output:
- JSON object with gate name, status (PASS/FAIL), individual checks, and
  basic path metadata, printed to stdout.
- Exit code 0 on PASS, 1 on FAIL.
"""

import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent


def check_repo_root() -> bool:
    marker = REPO_ROOT / '.git'
    return marker.exists()


def check_required_files() -> tuple[bool, list[str]]:
    required = [
        REPO_ROOT / 'inventory.yaml',
        REPO_ROOT / 'SESSION_INDEX.md',
    ]
    missing = [str(p) for p in required if not p.exists()]
    return (len(missing) == 0, missing)


def check_clean_working_tree() -> tuple[bool, str | None]:
    try:
        result = subprocess.run(
            ['git', 'status', '--porcelain'],
            cwd=str(REPO_ROOT),
            check=False,
            capture_output=True,
            text=True,
        )
    except OSError as exc:
        return False, f'Could not run git status: {exc}'

    output = result.stdout.strip()
    if output:
        return False, output
    return True, None


def main(argv: list[str] | None = None) -> int:  # noqa: ARG001
    checks: dict[str, object] = {}
    status = 'FAIL'
    error: str | None = None

    try:
        repo_root_ok = check_repo_root()
        checks['repo_root_ok'] = repo_root_ok

        required_ok, missing = check_required_files()
        checks['required_files_present'] = required_ok
        if missing:
            checks['missing_files'] = missing

        git_clean, git_detail = check_clean_working_tree()
        checks['git_clean'] = git_clean
        if git_detail is not None and not git_clean:
            checks['git_status_output'] = git_detail

        status_ok = repo_root_ok and required_ok and git_clean
        status = 'PASS' if status_ok else 'FAIL'
    except Exception as exc:  # pragma: no cover - defensive
        error = str(exc)
        status = 'FAIL'

    result = {
        'gate': 'pre_goal_transition',
        'status': status,
        'checks': checks,
        'paths': {
            'repo_root': str(REPO_ROOT),
        },
        'timestamp': datetime.now(timezone.utc).isoformat(),
    }
    if error is not None:
        result['error'] = error

    print(json.dumps(result))

    return 0 if status == 'PASS' else 1


if __name__ == '__main__':  # pragma: no cover
    raise SystemExit(main())
