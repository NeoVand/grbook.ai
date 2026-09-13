# How the tutor will use this vault (working design)

This note records constraints from the voice and agent research that shape the vault's structure.
It is a design input for the later "tutor layer" phase, not a final architecture.

## Constraints from the voice model

GPT-Live (`gpt-live-1`) listens and speaks; reasoning and tools run in a separate backend model whose tools
are custom functions and web search. Hosted file search and remote MCP are not available to it. The vault
must therefore be reachable through functions that we implement. See
[`docs/research/openai-live-voice-and-elevenlabs.md`](../../docs/research/openai-live-voice-and-elevenlabs.md).

Candidate functions, each answering in a few hundred tokens because context injections are small:

| Function | Returns |
| --- | --- |
| `search_knowledge(query, level?)` | ranked concept, lesson, analogy, and figure hits with one-line summaries and ids |
| `get_concept(id, depth)` | the concept note at a chosen explanation level (intuition, working, formal) |
| `get_prerequisites(id, learner?)` | the prerequisite path, marking what this learner has already covered |
| `find_misconception(statement)` | the closest known misconception with its correction and a diagnostic question |
| `get_analogy(id)` / `get_demo(id)` | analogies with their limits; interactive demos the app can open |
| `navigate(target)` | an app action: open a lesson, section, or demo and highlight it |
| `record_learning_event(...)` | writes to the learner model: read, asked, misconception observed, check passed |

## Implications from Deep Agents

A backend agent can explore files progressively (`ls`, `read_file`, `glob`, `grep`) and load `SKILL.md`
playbooks on demand. Persistent memory lives under a routed path such as `/memories/`, backed by a store.
For the vault this means:

- **Atomic, stable paths.** One concept per file under a stable id, so a tool call or `read_file` retrieves
  exactly one idea. Ids never change once the learner model references them.
- **Front-loaded summaries.** Every note starts with frontmatter and a short summary, so reading the first
  lines is enough to decide whether to read on.
- **Folder indexes.** Each folder gets a generated `_index.md` listing its notes with one-line summaries, giving
  an agent a cheap map before it opens files.
- **Teaching playbooks as skills.** Reusable tutoring procedures (diagnose a misconception, Socratic walk
  through a derivation, choose an analogy for a level, run a demo-guided exploration) belong in `SKILL.md`
  form so they load only when needed.
- **Learner memory separate from the vault.** The vault is read-only knowledge. Learner state (read, mastered,
  confused, goals) lives in the app database and is exposed to the agent through memory tools or a `/memories/`
  route, keyed by vault ids.
- **Server-side filesystem access is not exposed to the web.** On Vercel, the vault is compiled into indices
  and a store; the agent reads through that store, never through raw disk access.
