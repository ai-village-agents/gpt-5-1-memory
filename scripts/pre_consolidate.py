#!/usr/bin/env python3
"""JSON-emitting pre_consolidate gate for GPT-5.1.

This wraps the existing consolidation helper logic in a Shared Gate Library
compatible interface. It does *not* call the platform-level consolidate tool.
Instead it:

- Loads the current internal memory candidate (default: INTERNAL_MEMORY_CANDIDATE_D419_s6.md).
- Writes a copy to /tmp/gpt51-memory-candidate.txt for inspection.
- Applies lightweight structural checks (character count + anchor presence).
- Emits a JSON report to stdout and exits with code 0 on PASS, 1 on FAIL.

Design notes:
- HARD_MIN (4000 chars) is a local safety rule: below this is treated as FAIL.
- SOFT_MIN (7500 chars) is a *design floor*, not a scaffold constraint.
  Values in [HARD_MIN, SOFT_MIN) are allowed but flagged via below_soft_min.
- Anchor strings mirror scripts/prepare_consolidation.py so the two gates
  remain consistent.
"""

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_SOURCE = REPO_ROOT / 'INTERNAL_MEMORY_CANDIDATE_D419_s6.md'
DEFAULT_OUTPUT = Path('/tmp/gpt51-memory-candidate.txt')

HARD_MIN = 4000
SOFT_MIN = 7500  # design floor from cross-agent patterns (not a known scaffold error)

ANCHORS = {
    'identity': 'I am GPT',
    'temporal': 'Day 419 ',
    'goal': '"Improve your memory!"',
    'repo_pointer': 'gpt-5-1-memory',
}


def load_text(path: Path) -> str:
    try:
        return path.read_text(encoding='utf-8')
    except FileNotFoundError:
        raise RuntimeError(f'Source file not found: {path}')
    except OSError as exc:
        raise RuntimeError(f'Could not read {path}: {exc}') from exc


def write_text(path: Path, content: str) -> None:
    try:
        path.write_text(content, encoding='utf-8')
    except OSError as exc:
        raise RuntimeError(f'Could not write {path}: {exc}') from exc


def main(argv: list[str] | None = None) -> int:  # noqa: ARG001
    source = DEFAULT_SOURCE
    output = DEFAULT_OUTPUT

    checks: dict[str, object] = {}
    status = 'FAIL'
    error: str | None = None

    try:
        content = load_text(source)
        write_text(output, content)

        char_count = len(content)
        checks['char_count'] = char_count
        checks['hard_min_ok'] = hard_min_ok = char_count >= HARD_MIN
        checks['below_soft_min'] = char_count < SOFT_MIN

        missing_anchors = [label for label, needle in ANCHORS.items() if needle not in content]
        anchors_present = not missing_anchors
        checks['anchors_present'] = anchors_present
        if missing_anchors:
            checks['missing_anchors'] = missing_anchors

        status_ok = hard_min_ok and anchors_present
        status = 'PASS' if status_ok else 'FAIL'
    except Exception as exc:  # pragma: no cover - defensive
        error = str(exc)
        status = 'FAIL'

    result = {
        'gate': 'pre_consolidate',
        'status': status,
        'checks': checks,
        'paths': {
            'source': str(source),
            'tmp_copy': str(output),
        },
        'timestamp': datetime.now(timezone.utc).isoformat(),
    }
    if error is not None:
        result['error'] = error

    print(json.dumps(result))

    # Exit code: 0 only if all critical checks passed and no error occurred.
    if status == 'PASS':
        return 0
    return 1


if __name__ == '__main__':  # pragma: no cover
    raise SystemExit(main())
