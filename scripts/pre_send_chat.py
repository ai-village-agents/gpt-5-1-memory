#!/usr/bin/env python3
"""JSON-emitting pre_send_chat gate for GPT-5.1.

This gate is meant to be run just before sending a non-trivial message to
the village chat. It does not talk to the platform; instead it provides a
small structured checklist.

Interface:
- Optional --purpose "short description of the message".
- Optional --visible-events-checked flag (store_true) which the caller sets
  after glancing at recent visible events and, if needed, search_history.

Checks:
- purpose_provided: whether a non-empty purpose string was supplied.
- visible_events_checked: whether the caller set --visible-events-checked.
- inventory_present: inventory.yaml exists (sanity check only).

Status:
- PASS if purpose_provided and visible_events_checked are both True.
- Otherwise FAIL. Exit code mirrors status.
"""

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent


def parse_args(argv=None):  # noqa: D401, ARG001
    """Parse CLI arguments for the pre_send_chat gate."""
    parser = argparse.ArgumentParser(description="GPT-5.1 pre_send_chat gate")
    parser.add_argument(
        "--purpose",
        type=str,
        default="",
        help="Short description of why you are sending this chat message.",
    )
    parser.add_argument(
        "--visible-events-checked",
        action="store_true",
        help="Set after you have reviewed recent visible events / search_history.",
    )
    return parser.parse_args(argv)


def main(argv=None):  # noqa: D401, ARG001
    """Run the pre_send_chat gate and emit a JSON report."""
    args = parse_args(argv)
    checks: dict[str, object] = {}
    status = "FAIL"
    error: str | None = None

    try:
        purpose_provided = bool(args.purpose.strip())
        checks["purpose_provided"] = purpose_provided
        checks["visible_events_checked"] = bool(args.visible_events_checked)

        inventory_path = REPO_ROOT / "inventory.yaml"
        inventory_present = inventory_path.exists()
        checks["inventory_present"] = inventory_present

        status_ok = purpose_provided and bool(args.visible_events_checked)
        status = "PASS" if status_ok else "FAIL"
    except Exception as exc:  # pragma: no cover - defensive
        error = str(exc)
        status = "FAIL"

    result = {
        "gate": "pre_send_chat",
        "status": status,
        "checks": checks,
        "inputs": {
            "purpose": args.purpose,
        },
        "paths": {
            "repo_root": str(REPO_ROOT),
        },
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }
    if error is not None:
        result["error"] = error

    print(json.dumps(result))
    return 0 if status == "PASS" else 1


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
