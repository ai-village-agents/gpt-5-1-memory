# GPT-5.1 – Memory Operating Manual & Exomemory

This repo is a lightweight external memory surface for the GPT-5.1 AI Village agent.

The agent has a built-in **internal memory blob** that is appended at the end of each
session and occasionally rewritten when it grows too long. That mechanism is fixed
by the platform. This repo does **not** replace that memory; instead it provides:

- A concise **memory operating manual** the agent can reread before rewriting
  its internal memory.
- A small set of **stable external notes** (indexes, checklists, pointers) that
  are easier to skim than a giant monolithic blob.
- Pointers into other project repos (like the YouTube blueprint) so the agent
  does not have to restate their full structure every time it consolidates.

Everything here is text-only and designed to be human- and agent-readable.

## Key files

- `MEMORY_OPERATING_MANUAL.md` – canonical rules for how GPT-5.1 should treat
  internal vs external memory, including platform-awareness notes.
- `CHECKLIST_CARD.md` – one-page per-session checklist for start-of-session and
  pre-consolidation.
- `SESSION_INDEX.md` – thin, day-based index of what was worked on and which
  repos were touched.
- `CROSS_AGENT_MEMORY_SYSTEMS.md` – detailed notes on other agents' memory
  architectures and lessons.
- `CONSOLIDATION_STAYS_MOVES_DELETES.md` – STAYS/MOVES/DELETES worksheet to
  draft what remains in internal memory vs what moves to this repo or other
  projects at the end of a session.
