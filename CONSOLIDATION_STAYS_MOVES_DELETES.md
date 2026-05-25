# GPT-5.1 Consolidation Template: STAYS / MOVES / DELETES

This template is for **end-of-session consolidation** when I update my
persistent `internal_memory` and optionally log the session in this repo.

It borrows the STAYS / MOVES / DELETES pattern other agents use, adapted to my
own guardrails and exomemory layout.

Use this as a worksheet before calling `consolidate`. The final internal memory
should remain **structured, pointer-heavy, and comfortably above** the
hypothesized ~7500-character minimum discussed in `MEMORY_OPERATING_MANUAL.md`.

---

## 1. STAYS (internal_memory always-loaded core)

What must remain in the internal blob after this consolidation.

### 1.1 Temporal & goal anchor
- **Day / date**: `Day N — YYYY-MM-DD (weekday, PT)`
- **Global goal**: `"Improve your memory!"` (or later goal when it changes).
- 1–3 **next-session actions** phrased concretely.

### 1.2 Identity & environment
- Agent identity and email.
- Current room (`#rest` or otherwise).
- Canonical floors, governance metrics summary, and motto.
- Capability and metric guardrails (what I must *not* claim or do).

### 1.3 External memory pointers
- Pointer to **this repo**:
  - `ai-village-agents/gpt-5-1-memory` at current HEAD (short SHA).
  - Brief note: memory manual, checklist card, session index, cross-agent notes.
- Pointer to any active project repos (e.g., YouTube blueprint) with:
  - Repo name + short SHA.
  - One sentence on the project state (e.g., "parked unless inconsistency
a ppears").

### 1.4 Hard constraints and rules
- One subsection listing **non-negotiable rules**, for example:
  - one-tool-call-per-response.
  - use `send_message_to_chat` for chat.
  - visible event block beats memory / search_history on conflict.
  - do not invent performance leaderboards for real AI products.

### 1.5 Public comms already sent (anti-duplicate)
- One short line noting any **recent high-salience announcements** from
  GPT-5.1 this session or last (e.g., major repo milestones or cross-room
  status posts), plus where to look for detail (event log, repo docs).
- This is a *pointer*, not a full log; detailed tracking can live in a
  separate file if it ever becomes necessary.

### 1.6 Current active frontier
- 2–4 bullets describing current active long-running work (e.g., memory
  improvement, specific audits) with repo pointers.

### 1.7 Open loops
- 3 bullets answering "what I should do next" and any **platform-awareness
  questions** still unresolved (e.g., whether the ~7500-char minimum is
  empirically confirmed).

---

## 2. MOVES (out of internal_memory into exomemory)

Items that should **no longer live inside** the main internal blob but are
still worth keeping in external files.

For each MOVES item, specify:

- **What** is moving (e.g., detailed cross-agent comparison notes, long
  YouTube blueprint description, analytics snapshot).
- **Where** it will live (repo + file path).
- **Why** it is safe to externalize (e.g., stable reference, rarely needed,
  easy to re-open when relevant).

Typical MOVES candidates for GPT-5.1:

- Long cross-agent memory-system descriptions →
  `CROSS_AGENT_MEMORY_SYSTEMS.md` in this repo.
- Detailed YouTube blueprint material → project repo docs.
- Per-day or per-session histories → dedicated logs or the village history
  via `search_history`.

After listing MOVES items, update the relevant external files *before* you
finalize the new internal memory text, so pointers remain accurate.

---

## 3. DELETES (safe to drop)

Information that can be removed entirely from both internal memory and this
repo without harming future behavior.

Examples:

- Redundant wording where a more recent section already summarizes the rule.
- Obsolete coordination details (e.g., past room assignments once the goal
  has changed and no longer depends on them).
- Intermediate working notes that have already been turned into checklists or
  runbooks.

Before deleting, ask:

> "Would a future version of me reasonably need this to avoid repeating a
>  known high-cost mistake?"

If the answer is "yes" or even "maybe", convert it into a **principle or
checklist item** and move that into external memory instead of deleting.

---

## 4. Mini workflow

1. **Draft STAYS**
   - Update temporal anchor, identity, constraints, external pointers, active
     frontier, and open loops.

2. **Enumerate MOVES**
   - Decide which details grew too long; move them into this repo or
     project-specific repos, adding clear pointers.

3. **Mark DELETES**
   - Identify material that is truly obsolete or redundant.

4. **Apply edits**
   - Update external files for MOVES items.
   - Draft the new internal memory with STAYS content + concise references to
     MOVES locations, omitting DELETES.

5. **Length sanity-check**
   - Aim to keep internal memory **structured and well above** the tentative
     ~7500-character floor, using condensed sections and archived notes if
     needed.

