# Public communications runbook (GPT-5.1)

**Goal:** Avoid duplicate or confusing "big" announcements, especially about repos, memory systems, and cross-agent coordination, while staying metric- and capability-honest.

**Scope:** Use this runbook **before** sending any message that:

- Announces a new or significantly updated repo, tool, runbook, or guard.
- States canonical metrics or status for my own system (e.g., repo HEADs, wordcounts, floors).
- Coordinates or summarizes cross-agent work in a way others might treat as authoritative.

This runbook is intentionally light-weight. It complements, but does not replace, more opinionated guards like GPT-5.4 and GPT-5.2's `pre_send_chat` tools.

---

## 1. Clarify the announcement

1. Write a one-sentence intent in my own words:
   - *"I want to tell the room that …"*
2. Treat this as the **topic phrase** for later duplicate checks.

If I cannot summarize the announcement in one sentence, I am probably mixing multiple topics; split them or narrow the scope.

---

## 2. Confirm temporal context

1. Check that the first line of `internal_memory` matches the current **Day / date / goal**.
2. If there is any doubt, skim the latest system message and, if needed, use `search_history` on the current Day for messages from Shoshannah.
3. Only proceed once I am confident about the current Day and global goal.

This avoids sending announcements that assume the wrong goal or day.

---

## 3. Duplicate check in visible events

1. Read the recent visible events for the current room, focusing on messages from **GPT-5.1**.
2. Ask: *"Have I already announced this repo/tool/metric or essentially the same status in this room today?"*
3. If **yes** and there is no meaningful update, **do not** send a new announcement.
4. If there **is** a real update, reference the earlier message explicitly, e.g.:
   - *"Following up on my earlier note about `gpt-5-1-memory` …"*

This step is the minimum defense against obvious duplicates.

---

## 4. Optional wider duplicate check (transcript)

For higher-risk or especially prominent announcements (new repos, major runbooks, canonical metrics):

1. Use `search_history` over the current Day with a query that includes:
   - `"GPT-5.1"`
   - The **topic phrase** from Step 1
   - The relevant repo or file name, if any.
2. If this reveals a prior, very similar announcement, either:
   - Skip sending; or
   - Clearly frame the new message as an update/clarification.

This is optional but useful when I am unsure whether I already spoke about a topic earlier in the day.

---

## 5. Repo state sanity-check (when talking about a repo)

If the announcement concerns a specific repo or file (e.g., `gpt-5-1-memory`, `gpt-5-1-youtube-channel`):

1. Change into the repo directory.
2. Run:
   - `pwd`
   - `git status --short`
   - `git rev-parse --short HEAD`
3. Prefer to mention the **short HEAD** in the announcement when it matters, rather than a vague description like "latest commit".
4. If the working tree is dirty and that matters for the announcement, say so explicitly instead of implying everything is committed.

This keeps public status messages aligned with actual repo state.

---

## 6. Compose the message with guardrails

When drafting the announcement:

1. Be clear about what was **actually observed** (via tools/logs) vs. what is a **template or instruction**.
2. Avoid scoreboard-style numeric comparisons between named AI products; prefer neutral descriptions or synthetic stand-ins.
3. When describing other agents' work, link to or name their repos / docs instead of re-stating long details from memory.
4. Keep the message concise and pointer-heavy so future agents can see what changed without re-reading old design notes.

---

## 7. After sending (lightweight logging)

After a genuinely new "big" announcement (new repo, HEAD/parking decision, core runbook, or canonical metric):

1. At the next consolidation, make sure the corresponding **SESSION_INDEX.md** row mentions the announcement in the
   "Focus / main actions" column (1 short clause is enough).
2. If duplication risk grows over time, consider adding:
   - A dedicated `public_comms` log file in this repo; and
   - A small executable guard script (e.g., `scripts/pre_send_public_comms.sh`) that walks through this checklist before `send_message_to_chat`.

For now, this markdown runbook plus disciplined use of `SESSION_INDEX.md` is the minimal public-comms guard for GPT-5.1.

---

**Inventory note:** Indexed in `inventory.yaml` as `gpt51.public_comms_runbook`.
