# grbook.ai architecture (draft for review)

Status: draft written 2026-09-13 while the knowledge vault is still being built. Decisions marked **(review)**
are the ones I most want feedback on.

## What we are building

An AI-centred general relativity course. A learner at any level can arrive, say what they want to understand,
and be taught step by step: readable lessons, interactive 2D/3D demos, narrated audio, and a live voice tutor
that knows the course, the learner's history, and what is on screen. The course and the tutor both draw on one
knowledge vault (`knowledge/`).

Principles carried from the legacy review (`knowledge/sources/legacy/overview.md` §5):

- The core course must be excellent without AI; AI makes it personal.
- Measurement before formalism; every demo names its model, exaggerations, and limits.
- Stable ids everywhere (concepts, lessons, demos, equations), never ids derived from headings or positions.
- Visited, listened, attempted, and demonstrated are different kinds of evidence; never conflate them.
- The tutor reads semantic state (reader position, lab parameters), never pixels; its UI commands are validated.

## System overview

```
                 ┌──────────────── Browser (SvelteKit client) ────────────────┐
                 │  Reader / lessons   Labs (Threlte)   Tutor dock   Narration │
                 │        │                 │  LabContract   │           │     │
                 │        └──── app state (reading context, lab state) ──┘     │
                 │                                   │                         │
                 │    WebRTC audio + oai-events data channel  ◄──────────┐     │
                 └───────────────┬───────────────────┬───────────────────┼─────┘
          SDP offer (no key)     │   tool calls      │  TTS request      │ audio
                                 ▼                   ▼                   │
         ┌──────────────── SvelteKit server on Vercel ─────────────────┐ │
         │ /api/live/session   /api/kb/tool   /api/tts   settings/auth │ │
         │  decrypt user key    vault index    decrypt ElevenLabs key  │ │
         └───────┬──────────────────┬───────────────────┬──────────────┘ │
                 ▼                  ▼                   ▼                │
        OpenAI GPT-Live      knowledge index      ElevenLabs TTS ────────┘
   (voice + Responses backend)  (build time)
                                    ▲
                     knowledge/ vault (dossiers, concepts, curriculum)
                      Drizzle + libsql: users, keys, learner memory
```

## Stack

| Layer | Choice | Notes |
| --- | --- | --- |
| App | SvelteKit (Svelte 5 runes, remote functions), Vercel adapter | Template as configured |
| UI | Tailwind 4, shadcn-svelte (mist / nova), Inter + Geist | Legacy math colour roles become design tokens |
| Math | KaTeX (server-rendered where possible) | Authored macros later map symbols to concept ids |
| 3D | Three.js through Threlte | Legacy physics kernels ported to TypeScript with their checks |
| Auth | Better Auth (email + GitHub) | Template as configured |
| Data | Drizzle + libsql (SQLite file locally, Turso in production) | **(review)** Turso vs another host |
| Search | MiniSearch over a build-time vault index | Embeddings later if lexical search is not enough |
| Voice tutor | OpenAI `gpt-live-1`, Responses delegation to `gpt-5.6-terra` | See `docs/research/openai-live-voice-and-elevenlabs.md` |
| Narration | ElevenLabs text-to-speech with timestamps | Character alignment grouped into words for highlighting |

## Content pipeline

1. `knowledge/` holds the vault: chapter dossiers per book, concept registry and notes, later curriculum and
   pedagogy catalogs. All prose is original; book page text never enters the vault.
2. `scripts/build-vault-index.ts` compiles the vault into compact runtime files under
   `src/lib/server/vault/generated/` (units, concepts, equations, misconceptions, analogies, figures and demo
   ideas, all with locators). It runs before `dev` and `build`.
3. Server code loads the index; nothing reads `book-sources/`, which is gitignored and never deployed.

Until the concept registry and curriculum exist, the app browses the three books' units. When they land, the
primary navigation switches to concepts and learning paths, and unit pages become "how the books teach this".

## Routes

| Route | Purpose |
| --- | --- |
| `/` | Landing: what the course is, start learning |
| `/learn` | Library (books and units now; concept map and paths later) |
| `/learn/[book]/[unit]` | Study page for a unit, with the tutor dock |
| `/labs/[lab]` | Interactive demos, starting with parallel transport |
| `/settings` | API keys, voices, narration preferences |
| `/login` | Sign in or sign up |
| `POST /api/live/session` | Creates a GPT-Live WebRTC session with the user's stored OpenAI key |
| `POST /api/kb/tool` | Executes knowledge tools for the tutor (read-only, auth required) |
| `POST /api/tts` | Narration audio with word timings, using the user's stored ElevenLabs key |

## API keys (bring your own) **(review)**

Keys are entered once in Settings and stored **encrypted on the server** (AES-256-GCM, key from
`CREDENTIALS_ENCRYPTION_KEY`), tied to the signed-in account. The browser never receives a key back, only the
last four characters. Server routes decrypt a key only for the request that needs it and never log it.

Why server-side: GPT-Live has no browser-safe token, so a server must attach the key to session creation anyway;
storing it encrypted avoids re-entering keys on every device and keeps keys out of browser storage. The
alternative is keeping keys only in the browser and sending them with each session request.

## Voice tutor

- **Session creation.** The browser creates an `RTCPeerConnection` with microphone audio and the `oai-events` data
  channel, waits for ICE gathering, and posts the SDP offer to `/api/live/session`. The server builds the session
  from server-owned templates (voice instructions, backend prompt, tool definitions, data-channel permissions)
  and returns only the SDP answer.
- **Tool loop in the browser.** Nested `response.event` messages carry function calls. Client tools (reading
  context, navigate, highlight, set lab parameter) run locally; knowledge tools call `/api/kb/tool`. Results go
  back with `response.item.create`, then one `response.create` per batch.
- **One tool registry** (`src/lib/tutor/tools.ts`) defines each tool's name, description, JSON Schema, and where
  it runs. It generates both the `delegation.responses.tools` payload and the server validators.
- **Context.** On start and on navigation, the browser sends `session.thinking.append` with the reading context.
- **Captions and activity.** Transcript deltas drive captions; tool activity shows in a status line.
- **Narration handoff.** Starting the tutor pauses narration; the two never play at once.
- **Memory.** When a session ends, the backend summary and the tool evidence become learner events; the next
  session starts with a short summary in `input`.

## Learner memory

| Table | Purpose |
| --- | --- |
| `user_preference` | Theme, voices, narration model and speed, hold-to-talk shortcut |
| `provider_credential` | Encrypted OpenAI and ElevenLabs keys (last four for display) |
| `learning_event` | Append-only evidence: visited, listened, asked, attempted, demonstrated, misconception; idempotency key |
| `concept_state` | Per-user status per concept id (unseen, introduced, practicing, secure) with evidence counts |
| `learner_goal` | What the learner wants to learn, linked to concept ids |
| `tutor_session` | GPT-Live session id, timestamps, usage seconds, end-of-session summary |
| `note` | Learner notes attached to units, concepts, or demos |

The tutor reads a compact learner summary and writes evidence through server tools with the session's
authenticated user; it cannot write arbitrary state.

## Labs

Each lab implements a `LabContract` (from the legacy review): typed state, `describe(state)` for narration,
`scientificContext(state)` for the tutor (model, parameters with units, readouts, assumptions, limitations,
concept ids), declared tutor commands with ranges, and prediction prompts. The first port is the legacy
parallel-transport lab (plane, cylinder, sphere; holonomy equals curvature times area), whose model and checks
are already verified.

## Milestones

| Milestone | Scope |
| --- | --- |
| M0 Skeleton (tonight) | Theme and shell, vault index, unit study pages, settings with encrypted keys, schema, GPT-Live session route and client, knowledge tools, TTS route |
| M1 Tutor that teaches a unit | Live-key testing of the tool loop, captions, reader navigation from tool results, session summaries into memory |
| M2 First labs | Parallel transport, tidal cloud, stress-energy crossings, with LabContract and tutor commands |
| M3 Concept-first course | Concept map and learning paths from the registry; concept pages with three explanation levels |
| M4 Narration and practice | Authored spoken explanations, practice items with feedback, spaced review |
| M5 Evaluation | Tutor evaluation set, learner walkthroughs, performance and accessibility passes |

## Open questions for review

1. Keys stored encrypted server-side (current plan) or browser-only?
2. Database host for production (Turso with libsql is the smallest change).
3. Voice backend model default (`gpt-5.6-terra`) and whether to offer a cheaper mode.
4. Visual direction: the template's neutral mist theme with semantic math colours, or a bolder identity.
5. Whether signed-out visitors can read the course (tutor and narration require an account and keys).
