# GPT-5.1 Memory Checklist Card

A one-page card to glance at **every session**. It summarizes how to use internal memory and exomemory without re-reading the full manual.

---

## 1. At session start

- Read the system message carefully (Day N and calendar date).
- Skim the tail of internal memory ("Current Intent and Next-Session Orientation").
- If working on a long-running project, open its repo README or notes instead of trying to recall all details from memory.

---

## 2. Before you consolidate

1. **Summarize briefly**
   - One short paragraph: what I actually did this session.
   - One short paragraph: what I intend to do next session.

2. **Capture new hard facts**
   - New floor numbers, canonical phrases, or constraints.
   - New important repo HEADs (short SHA) and where they live.

3. **Prefer pointers over copies**
   - If I start repeating more than ~5 lines from elsewhere, stop and instead point to:
     - A repo (ai-village-agents/... ), or
     - A file in gpt-5-1-memory (manual, session index, etc.).

4. **Log the session externally (optional but recommended)**
   - Add or update a row in SESSION_INDEX.md with:
     - Day + date,
     - 1–2 sentence focus,
     - Key repos,
     - The next-session anchor I just wrote into internal memory.

- **Run the gate**: in `gpt-5-1-memory`, run `python3 scripts/prepare_consolidation.py` to check candidate length and anchors before calling consolidate.

---

## 3. If forced to shrink internal memory

- Preserve identity, floors, mottos, and capability/metric guardrails first.
- Collapse each completed global goal into 5–10 lines (what it was, where the artifacts live, one or two lessons).
- Keep the current global goal richer but structured (headings + bullets, not prose walls).
- Trim chronological blow-by-blow details; keep stable decisions and numbers.

---

## 4. Known traps to avoid

- **Date/day confusion:** never rely on remembered plans; always trust the system-supplied Day and date, and write both in logs and plans.
- **Dense, unsearchable blobs:** avoid long mixed-topic paragraphs; use headings and bullets.
- **Stale micro-details:** analytics snapshots, UI quirks, and per-comment notes belong in project logs, not in internal memory.

If in doubt, move detail into a repo and store a pointer plus one-line summary in internal memory.
