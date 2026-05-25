#!/usr/bin/env python3
"""JSON-emitting session_start gate for GPT-5.1.

Shared Gate Library compatible; lightweight sanity check to run once at the
beginning of a session. It does not talk to the platform and does not modify
any files.

Checks:
- repo_root_ok: expected repo directory and .git marker exist.
- inventory_present: inventory.yaml exists.
- session_index_present: SESSION_INDEX.md exists.
- manual_present: MEMORY_OPERATING_MANUAL.md exists.
- checklist_present: CHECKLIST_CARD.md exists.

Output:
- Single JSON object with gate name, status (PASS/FAIL), individual checks, and
  basic path metadata, printed to stdout.
- Exit code 0 on PASS, 1 on FAIL.
"""

import json
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent


def main(argv=None):  # noqa: ARG001
    checks: dict[str, object] = {}
    status = "FAIL"
    error: str | None = None

    try:
        repo_root_ok = REPO_ROOT.exists() and (REPO_ROOT / ".git").exists()
        checks["repo_root_ok"] = repo_root_ok

        inventory_path = REPO_ROOT / "inventory.yaml"
        session_index_path = REPO_ROOT / "SESSION_INDEX.md"
        manual_path = REPO_ROOT / "MEMORY_OPERATING_MANUAL.md"
        checklist_path = REPO_ROOT / "CHECKLIST_CARD.md"

        checks["inventory_present"] = inventory_path.exists()
        checks["session_index_present"] = session_index_path.exists()
        checks["manual_present"] = manual_path.exists()
        checks["checklist_present"] = checklist_path.exists()

        status_ok = (
            repo_root_ok
            and checks["inventory_present"]
            and checks["session_index_present"]
            and checks["manual_present"]
            and checks["checklist_present"]
        )
        status = "PASS" if status_ok else "FAIL"
    except Exception as exc:  # pragma: no cover - defensive
        error = str(exc)
        status = "FAIL"

    result = {
        "gate": "session_start",
        "status": status,
        "checks": checks,
        "paths": {"repo_root": str(REPO_ROOT)},
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }
    if error is not None:
        result["error"] = error

    print(json.dumps(result))
    return 0 if status == "PASS" else 1


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
