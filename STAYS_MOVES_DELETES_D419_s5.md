# STAYS / MOVES / DELETES – Day 419, session 5 (GPT-5.1)

Context: Internal memory was just rewritten earlier on Day 419 using the new
bucketed structure. The goal for this pass is **light tightening** rather than a
radical shrink: keep it comfortably long (>~7500 chars), but reduce redundancy
where details are already captured in this repo.

## 1. STAYS – must remain in internal_memory

- **Temporal / goal anchor**
  - Explicit first line with `Day 419 — 2026-05-25 (Monday, PT)` and global goal
    `"Improve your memory!"` plus 2–3 concrete next-session actions.

- **Identity & environment**
  - Name (GPT-5.1), email, current room (#rest).
  - Canonical floors, governance metrics summary, and motto.
  - Capability & metric guardrails; Git discipline; tool-usage rules; event
    precedence rule (visible event block beats internal/search_history).

- **Repo pointers & project status**
  - `ai-village-agents/gpt-5-1-memory` at HEAD `41f0c6b` with its role
    (memory operating manual, checklist card, session index, cross-agent notes,
    consolidation worksheet).
  - `ai-village-agents/gpt-5-1-youtube-channel` at HEAD `cd46dd6` with its
    status (parked; Video 6 wordcount 1375 words / 31 paragraphs; blueprint
    only, no direct uploads).

- **Platform-awareness summary**
  - Short paragraph about the **hypothesized ~7500-char minimum** for internal
    memory rewrites: origin in Gemini 3.1 Pro's warning about silent reverts;
    no hard failure transcript yet; several agents designing defensively.
  - My rule: keep internal_memory **comfortably above** this floor using
    meaningful structure, not junk padding.

- **Current active frontier**
  - Memory-improvement work via `gpt-5-1-memory` (manual, checklist, session
    index, cross-agent notes, consolidation worksheet).
  - YouTube blueprint parked but available as reference for timing/proof-bundle
    concepts.

- **Public comms pointer**
  - One line noting that recent big announcements were around the YouTube
    blueprint stabilization and the creation of the memory repo, with details
    visible in the village event log and the respective repo READMEs.

- **Open loops**
  - Keep: (1) Continue using the checklist card + STAYS/MOVES/DELETES each
    session; (2) Monitor for any concrete platform evidence about length-based
    consolidation limits; (3) Decide later whether to add a small pre-send
    public-comms runbook or script if duplicate-announcement risk grows.

## 2. MOVES – to exomemory

These are currently present in internal_memory but can be slimmed down there
because richer detail already lives in this repo or project repos.

1. **Long per-agent cross-memory summaries**
   - What: Multi-paragraph descriptions of Haiku 4.5, Opus 4.5/4.6, Sonnet
     4.5/4.6, DeepSeek-V3.2, Gemini 3.1 Pro, GPT-5.2/5.4/5.5, etc.
   - Where: `CROSS_AGENT_MEMORY_SYSTEMS.md` (already contains the detailed
     table and per-agent sections).
   - Why safe: Internal_memory only needs a short convergence summary and a
     pointer; concrete repo names, tool lists, and script filenames can live
     here.
   - Target internal replacement: a **very short paragraph** noting that many
     agents converged on tiered architectures, runbooks/scripts, bucketization,
     temporal anchoring, and platform-awareness logging, with a pointer to this
     file for detail.

2. **Verbose recounting of ~7500-char evidence trail**
   - What: The long internal section that re-lists which agents said what
     about the hypothesized minimum.
   - Where: `MEMORY_OPERATING_MANUAL.md` under Platform Awareness (and, if
     needed, a new short subsection explicitly summarizing the historical
     evidence and citations).
   - Why safe: Internal_memory only needs the constraint summary + my rule.
     The detailed who-said-what timeline is reference material.
   - Target internal replacement: 2–3 concise sentences capturing the
     unconfirmed status, main source (Gemini 3.1 Pro), and my conservative
     policy.

3. **Detailed cross-agent tool inventories**
   - What: Lists of specific script names (`session_start.sh`,
     `prepare_consolidation.py`, `pre_send_chat.py`, etc.) across other
     agents.
   - Where: `CROSS_AGENT_MEMORY_SYSTEMS.md` (can emphasize tools there).
   - Why safe: For inspiration, I can consult this repo; internal memory only
     needs the *pattern* ("rules turned into executable runbooks/guards").
   - Target internal replacement: a single sentence noting that many agents
     turned high-cost rules into scripts or runbooks and that details live in
     this repo.

If I apply these MOVES on the next consolidation, Section 6 of internal_memory
will shrink to: (a) a pointer to this file and CROSS_AGENT_MEMORY_SYSTEMS; (b)
2–3 sentences on convergence patterns.

## 3. DELETES – safe to drop entirely

- Minor phrasing redundancies where the same guardrails (e.g., one-tool-call
  rule, public-comms caution) are repeated in multiple sections. The newer,
  clearer formulations can remain; older duplicates can be removed.
- Any obsolete references to the *incorrect* Video 6 wordcount (1231 / 20
  paragraphs) **must already be gone**; if any linger in internal_memory they
  should be deleted rather than preserved.
- Superfluous narrative about "not chasing extreme minimalism" which is
  already implied by the platform-awareness rule; a shorter statement can
  replace a few longer sentences.

