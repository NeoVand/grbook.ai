# OpenAI GPT-Live (live voice) and ElevenLabs TTS timestamps: research reference

Researched 2026-09-12. Revised the same day after a line-by-line read of the raw Markdown of the official
guides and API references on developers.openai.com. The pages were downloaded by appending `.md` to each
URL. Other sources: platform.openai.com, github.com/openai, elevenlabs.io.

The `openai.com/index/...` launch posts returned HTTP 403, so launch-blog numbers come from OpenAI's
official Developer Community announcement and are marked as such.

**Legend**

| Mark | Meaning |
|---|---|
| **[Unverified]** | Not established by an official page, or official pages disagree |
| **[Inference]** | Our engineering judgement, not an OpenAI or ElevenLabs statement |

**Primary pages read in full**

- [Getting started with GPT-Live](https://developers.openai.com/api/docs/guides/live)
- [Managing GPT-Live sessions](https://developers.openai.com/api/docs/guides/live-conversations)
- [Migrate to GPT-Live](https://developers.openai.com/api/docs/guides/live-migration)
- [Delegation and tools](https://developers.openai.com/api/docs/guides/live-delegation)
- [Prompting GPT-Live](https://developers.openai.com/api/docs/guides/live-prompting)
- [WebRTC (Live)](https://developers.openai.com/api/docs/guides/voice-webrtc?api=live)
- [Server-side controls (Live)](https://developers.openai.com/api/docs/guides/voice-server-controls?api=live)
- [WebSockets (Live)](https://developers.openai.com/api/docs/guides/voice-websockets?api=live)
- [Cost optimization (Live)](https://developers.openai.com/api/docs/guides/voice-latency-cost?api=live)
- [Custom voices](https://developers.openai.com/api/docs/guides/custom-voices)
- [GPT-Live 1 model page](https://developers.openai.com/api/docs/models/gpt-live-1)
- API references: [primary WebSocket](https://developers.openai.com/api/reference/resources/live/primary-websocket),
  [sideband WebSocket](https://developers.openai.com/api/reference/resources/live/sideband-websocket),
  [fork WebSocket](https://developers.openai.com/api/reference/resources/live/fork-websocket)

---

## 0. TL;DR

- **"GPT Live" exists.** The official name is **GPT-Live**; the API model ID is **`gpt-live-1`** (default
  snapshot `gpt-live-1`). It became **generally available on 2026-09-10**.
  [changelog](https://developers.openai.com/api/docs/changelog),
  [model page](https://developers.openai.com/api/docs/models/gpt-live-1)
- **It is a different architecture from `gpt-realtime-2.1`, not a drop-in upgrade.** GPT-Live is a
  full-duplex voice front end. It listens, speaks, and decides when to **delegate**. Reasoning and tools run
  on a backend:
  - **Responses delegation:** a hosted Responses model you configure.
  - **Client delegation:** your own code.

  It uses a new endpoint family (`/v1/live/sessions`) and new events.
  [live](https://developers.openai.com/api/docs/guides/live)
- **Price:** $0.05/min, billed per second, not rounded up. Backend Responses calls are billed at normal
  model and tool rates. [model page](https://developers.openai.com/api/docs/models/gpt-live-1)
- **Modalities:** audio and text only; image and video are not supported. Images go to a vision-capable
  backend. [model page](https://developers.openai.com/api/docs/models/gpt-live-1),
  [delegation: images](https://developers.openai.com/api/docs/guides/live-delegation#add-images-and-visual-context)
- **Backend tools:** only `function` and `web_search`. There is no hosted file search and no MCP tool for
  delegation. [primary WS ref](https://developers.openai.com/api/reference/resources/live/primary-websocket)
- **Browser auth:** there is **no ephemeral client secret** for GPT-Live. Your server sends the browser's
  SDP offer as JSON to `POST /v1/live/sessions` using the API key, and returns the SDP answer.
  [WebRTC live](https://developers.openai.com/api/docs/guides/voice-webrtc?api=live)
- **The browser may run the tool loop.** Function-call events arrive on the WebRTC data channel, and the
  docs explicitly allow the browser to forward them to an authenticated backend. No sideband WebSocket is
  required.
  [server controls](https://developers.openai.com/api/docs/guides/voice-server-controls?api=live#decide-whether-you-need-a-sideband)
- **Realtime remains available** with `gpt-realtime-2.1`, `ek_` ephemeral secrets, in-model tools, MCP, VAD
  and image input. [realtime](https://developers.openai.com/api/docs/guides/realtime)
- **SDKs:**
  - openai-node exposes `client.live.*`.
    [api.md](https://github.com/openai/openai-node/blob/master/src/resources/live/api.md)
  - The JS Agents SDK has **no GPT-Live support** through v0.18.0 (Sept 10).
    [releases](https://github.com/openai/openai-agents-js/releases)
- **ElevenLabs:**
  - `POST /v1/text-to-speech/{voice_id}/stream/with-timestamps` gives **character-level** alignment.
  - Newest models: `eleven_v3` and `eleven_v3_conversational`.
  - `eleven_v3` is **not** supported on the TTS WebSocket.
  - A browser-safe single-use token is available for the WebSocket. (§7)
- **grbook.ai:** use **Responses delegation with our knowledge-base functions**, run the tool loop **in the
  browser**, and serve retrieval from stateless SvelteKit endpoints. (§8)

---

## 1. Model: IDs, dates, and differences from gpt-realtime

### 1.1 Timeline

| Date | Release | Source |
|---|---|---|
| 2026-05-07 | `gpt-realtime-2`, GPT-Realtime-Translate, GPT-Realtime-Whisper | [changelog](https://developers.openai.com/api/docs/changelog) |
| 2026-07-06 | `gpt-realtime-2.1` and GPT-Realtime-2.1 mini | [changelog](https://developers.openai.com/api/docs/changelog) |
| 2026-07-28 | GPT Transcribe and GPT Live Transcribe | [changelog](https://developers.openai.com/api/docs/changelog) |
| 2026-09-08 | `whisper-1` and `gpt-4o-*-transcribe` deprecated; shutdown 2027-02-26 | [changelog](https://developers.openai.com/api/docs/changelog) |
| 2026-09-10 | GPT-Live 1 generally available | [changelog](https://developers.openai.com/api/docs/changelog), [community announcement](https://community.openai.com/t/introducing-gpt-live-1-in-the-api/1396471) |

The model page lists "Jul 31, 2025 knowledge cutoff". That is a cutoff, not a release date.

### 1.2 `gpt-live-1` spec sheet

| Property | Value | Source |
|---|---|---|
| Model ID | `gpt-live-1` | [model](https://developers.openai.com/api/docs/models/gpt-live-1) |
| Endpoint | `v1/live/sessions` only. Chat Completions, Responses and Realtime are not supported. | [model](https://developers.openai.com/api/docs/models/gpt-live-1) |
| Features | Streaming, function_calling. No structured_outputs, fine_tuning or predicted_outputs. | [model](https://developers.openai.com/api/docs/models/gpt-live-1) |
| Pricing | $0.05/min, per second | [model](https://developers.openai.com/api/docs/models/gpt-live-1) |
| Rate limits | Concurrent sessions: T1 25, T2 50, T3 200, T4 300, T5 500. Free tier unsupported. | [model](https://developers.openai.com/api/docs/models/gpt-live-1) |
| Context | 128,000 tokens (instructions + text + audio tokens). Auto-compaction above 90%. | [sessions](https://developers.openai.com/api/docs/guides/live-conversations#manage-longer-conversations) |
| `instructions` | Up to 16,384 tokens, but "the live model has a small context window": keep it short | [sessions](https://developers.openai.com/api/docs/guides/live-conversations), [prompting](https://developers.openai.com/api/docs/guides/live-prompting) |
| Session expiry | `session.started.session.expires_at` (Unix seconds). Close reason `expired` means "duration limit". **[Unverified]** The numeric limit is not documented; read `expires_at` at runtime. | [primary WS ref](https://developers.openai.com/api/reference/resources/live/primary-websocket) |

### 1.3 Voices (resolved)

- **Built-in names.** `audio.output.voice` accepts 22 names. The sessions guide lists 12 of them as
  "additional voice options":

  | Voice | Language | Influence | Presentation | Source |
  |---|---|---|---|---|
  | `quartz` | English | Australian | Feminine | Generated |
  | `ripple` | English | Australian | Masculine | Natural |
  | `vesper` | English | British | Masculine | Natural |
  | `willow` | English | Irish | Feminine | Natural |
  | `stone` | English | Irish | Masculine | Natural |
  | `gleam` | English | North American | Feminine | Natural |
  | `meridian` | English | North American | Masculine | Natural |
  | `bossa` | Portuguese | Brazilian | Feminine | Natural |
  | `tempo` | Portuguese | Brazilian | Masculine | Natural |
  | `beacon` | English | Filipino | Masculine | Generated |
  | `delta` | English | Southern U.S. | Feminine | Generated |
  | `cinder` | English | Southern U.S. | Masculine | Generated |

  The other 10 are the familiar Realtime voices: `alloy`, `ash`, `ballad`, `cedar`, `coral`, `echo`, `marin`,
  `sage`, `shimmer`, `verse`.
- **Default and mutability.** The default is **`marin`**, and the voice is immutable after startup.
- **Accents are not guaranteed.** "Regional influence describes a voice's speaking style, not a guarantee of
  accent fidelity."
- **Custom voices.** Pass an object `{ "id": "voice_123" }`; named voices are strings. `gpt-live-1`
  supports custom voices with English accents; state the accent in `instructions`. This needs custom-voice
  API access and `api.voices.read` / `api.voices.write`.

Sources: [sessions: voice options](https://developers.openai.com/api/docs/guides/live-conversations#voice-options),
[primary WS ref](https://developers.openai.com/api/reference/resources/live/primary-websocket),
[custom voices](https://developers.openai.com/api/docs/guides/custom-voices).

### 1.4 GPT-Live vs gpt-realtime-2.1

| | **GPT-Live (`gpt-live-1`)** | **Realtime (`gpt-realtime-2.1`)** |
|---|---|---|
| Architecture | Voice front end; backend chosen independently ([live](https://developers.openai.com/api/docs/guides/live)) | One model for speech, reasoning and tool selection |
| Endpoint | `/v1/live/sessions` | `/v1/realtime` ([model](https://developers.openai.com/api/docs/models/gpt-realtime-2.1)) |
| Pricing | $0.05/min plus backend tokens | Per 1M tokens: text $4 in / $0.40 cached / $24 out; audio $32 / $0.40 / $64; image $5 / $0.50 ([model](https://developers.openai.com/api/docs/models/gpt-realtime-2.1)) |
| Image input | Backend only | `input_image` ([realtime conversations](https://developers.openai.com/api/docs/guides/realtime-conversations)) |
| Reasoning | `delegation.responses.reasoning.effort` (`none` … `xhigh`, depending on the model) | `reasoning.effort` ([client events](https://developers.openai.com/api/reference/resources/realtime/client-events)) |
| Tools | Backend: `function`, `web_search` | `function`, `mcp` ([realtime-mcp](https://developers.openai.com/api/docs/guides/realtime-mcp)) |
| Turn-taking | Model decides; no manual turns or VAD settings ([migration](https://developers.openai.com/api/docs/guides/live-migration)) | `server_vad` / `semantic_vad` / manual |
| Browser auth | Server brokers the SDP (JSON) | `ek_` secret, or server brokers the SDP (multipart) ([WebRTC](https://developers.openai.com/api/docs/guides/voice-webrtc?api=realtime)) |
| Transcripts | Native deltas with `start_ms` / `end_ms` | Configured transcription model |

**Benchmarks** (from the
[community announcement](https://community.openai.com/t/introducing-gpt-live-1-in-the-api/1396471); not
re-verified against the 403'd blog):

| Benchmark | GPT-Live-1 | GPT-Realtime-2.1 |
|---|---|---|
| Tau3, first attempt | 83.6% | 45.7% |
| Turn-taking latency | 0.798 s | 1.41 s |
| Conversational Dynamics | 97.3% | n/a |

- **Keyword biasing:** the announcement advertises it, but **no keyword or biasing field exists in the Live
  session schema**. Treat it as model behavior, not a configurable parameter.
  ([primary WS ref](https://developers.openai.com/api/reference/resources/live/primary-websocket))
- **Backend model:** every official guide and example uses **`gpt-5.6-terra`**. Use `gpt-5.6-luna` for
  cost-sensitive work and for lightweight transcript checks. The community post mentions GPT-6 Astra; the
  guides do not.
  ([delegation](https://developers.openai.com/api/docs/guides/live-delegation#configure-responses-delegation),
  [sessions](https://developers.openai.com/api/docs/guides/live-conversations#transcript-deltas))

---

## 2. Connections and authentication

### 2.1 Transports

| Transport | Details | Source |
|---|---|---|
| **WebRTC (browser)** | See "WebRTC details" below. | [WebRTC live](https://developers.openai.com/api/docs/guides/voice-webrtc?api=live) |
| **Primary WebSocket (server)** | `wss://api.openai.com/v1/live/sessions`, with no query parameters and `Authorization: Bearer`. First message is `session.start`; wait for `session.started`. Audio in with `session.input_audio.append` (base64), out with `session.output_audio.delta`. Formats: `audio/pcm` at 24000 (default) or 16000, `audio/pcmu` / `audio/pcma` at 8000. | [WebSockets live](https://developers.openai.com/api/docs/guides/voice-websockets?api=live), [primary WS ref](https://developers.openai.com/api/reference/resources/live/primary-websocket) |
| **Sideband WebSocket (server)** | `wss://api.openai.com/v1/live/sessions/{session_id}/attach`, Bearer key. See "Sideband details" below. | [server controls](https://developers.openai.com/api/docs/guides/voice-server-controls?api=live) |
| **SIP** | Trunk to `sip:$PROJECT_ID@sip.api.openai.com;transport=tls`. Webhook `live.transport.incoming`. Accept with `POST /v1/live/sessions/{id}/accept`; also `/refer` and `/hangup`. Events: `transport.dtmf.received`, `transport.dtmf.send`, `transport.ringing`, `transport.answered`, `transport.failed`. | [SIP](https://developers.openai.com/api/docs/guides/voice-sip), [primary WS ref](https://developers.openai.com/api/reference/resources/live/primary-websocket) |

**WebRTC details**

- The browser creates the offer. The server posts JSON `{ session, transport: { type: "webrtc", sdp } }` to
  `POST /v1/live/sessions`.
- The response is **HTTP 201** `{ session: { id }, transport: { type: "webrtc", sdp } }`.
- Media tracks carry audio; the data channel `oai-events` carries JSON.
- **Do not send `session.start` on the data channel.** The HTTP request starts the session.
- Do not send `session.input_audio.append`, or expect `session.output_audio.delta`, on the data channel.
- Creating the session bills 15 s during initialization; that is credited once the session runs.

**Sideband details**

- Receives transcripts, delegation events, nested Responses events, and reflected audio (24 kHz PCM16).
- Sends `session.update`, the `*.append` events, `response.item.create`, `response.create`, mute/unmute and
  `session.close`.
- **Optional:** "Responses delegation also works without a sideband."

### 2.2 Key handling for the browser, including BYOK (resolved as far as the docs go)

**What the docs say**

- **Server-held key.** "Your application server exchanges it for an answer with `POST /v1/live/sessions`,
  using the project API key. Keep the key and session configuration on your trusted server."
  ([WebRTC live](https://developers.openai.com/api/docs/guides/voice-webrtc?api=live))
- **JSON only, and never expose the key.** "The Live endpoint requires JSON, not multipart or raw SDP."
  Also: authenticate hosted broker requests with application credentials, and "never expose the OpenAI API
  key to the browser". ([custom voices](https://developers.openai.com/api/docs/guides/custom-voices))
- **No token endpoint.** There is no GPT-Live client-secret or ephemeral-token endpoint.
  `/v1/realtime/client_secrets` accepts only `realtime` / `transcription` sessions, and openai-node's
  `live` resource has no secrets method.
  ([client secrets ref](https://developers.openai.com/api/reference/resources/realtime/subresources/client_secrets/methods/create),
  [api.md](https://github.com/openai/openai-node/blob/master/src/resources/live/api.md))
- **Reference server.** The official example uses `new OpenAI({ maxRetries: 0 })` and a 64 kB JSON body
  limit. It checks the request origin, validates the SDP string, calls `client.live.create(...)`, and
  returns the 201 result. On errors it logs only the status. "Before making the server accessible to other
  users, protect `/api/session` with your application's authentication, authorization, request limits, and
  HTTPS."
- **Wait for ICE gathering.** The browser example waits until ICE gathering is `complete`, with a 10 s
  timeout, before posting the offer. It needs Node.js 22.6+ on the server.
  ([WebRTC live](https://developers.openai.com/api/docs/guides/voice-webrtc?api=live))

**Frontend event permissions (resolved)**

- **Field:** `session.client.data_channel` is startup-only. It is "capabilities for an untrusted frontend
  attached to a unified WebRTC session. Trusted sideband connections are unaffected."
  ([primary WS ref](https://developers.openai.com/api/reference/resources/live/primary-websocket))
- **Client events:** `allowed_client_events` is `"all"` or an array of event types. An empty array allows
  none, and **omission preserves allow-all**.
- **Server events:** `allowed_server_events` is `"all"` or an array of `{ type, response_event? }`, e.g.
  `{ "type": "response.event", "response_event": "response.output_item.done" }`. Omission is allow-all.
- **Notice:** a restricted channel emits
  `{ "type": "info", "code": "data_channel_permissions", ... }`.
- **Forks:** a WebRTC fork preserves these permissions unless overridden; a WebSocket fork discards them.
  ([sessions: fork](https://developers.openai.com/api/docs/guides/live-conversations#store-and-fork-a-session))
- **Not a privacy tool.** "A sideband does not itself make session events private from the browser."
  ([server controls](https://developers.openai.com/api/docs/guides/voice-server-controls?api=live#assign-one-owner-for-each-action))

**Safety identifier.** `OpenAI-Safety-Identifier` is documented for Realtime (`/v1/realtime/calls`,
`client_secrets`). **[Unverified]** Whether `POST /v1/live/sessions` honors it; the Live pages do not mention
it.

**BYOK pattern for SvelteKit on Vercel** **[Inference]**, applying the documented rules to a user-supplied
key:

1. **The browser holds the user's key** (in memory, or opt-in `localStorage`). It sends the key only to our
   own origin over HTTPS, in a header (e.g. `Authorization`), never in a URL.
2. **Session route.** `POST /api/live/session` (`+server.ts`, Node runtime) does the following:
   - Validates the origin and the SDP string, and rate-limits.
   - Builds `session` from **server-owned** templates: instructions, delegation, tools and permissions. It
     never passes client JSON through.
   - Calls `new OpenAI({ apiKey, maxRetries: 0 }).live.create(...)` and returns `{ session.id, transport.sdp }`
     with `Cache-Control: no-store`.
   - Never logs headers or bodies, and returns sanitized errors.
3. **Restrict the data channel** to exactly the events the browser loop needs (§8.3). This is defence in
   depth against injected scripts, not against the key owner.
4. **Only session creation needs the user's key.** Knowledge-base tool endpoints are read-only and never
   see the OpenAI key; protect them with app auth and rate limits.
5. **No sideband on Vercel.** It is a WebSocket held for the whole conversation, which does not fit
   short-lived serverless functions. The documented browser-forwarding pattern avoids it.

---

## 3. Session configuration

Sources: [sessions](https://developers.openai.com/api/docs/guides/live-conversations),
[primary WS ref](https://developers.openai.com/api/reference/resources/live/primary-websocket),
[delegation](https://developers.openai.com/api/docs/guides/live-delegation),
[prompting](https://developers.openai.com/api/docs/guides/live-prompting).

### 3.1 Fields

| Field | Notes | Updatable? |
|---|---|---|
| `model` | `"gpt-live-1"`, required for every transport | No |
| `instructions` | ≤16,384 tokens. See the prompt structure below. | No; add with `session.instructions.append` |
| `input` | Startup text history: ≤128 messages, ≤8,192 tokens. Roles `developer` / `user` / `assistant`, **one text part each**; no `system`. User and developer use `input_text`; assistant uses `text` or `output_text`. | No |
| `audio.format` | WebSocket only; WebRTC and SIP negotiate. Default PCM16 24 kHz. | No |
| `audio.output.voice` | Name or `{ id }`; default `marin` | No |
| `client.data_channel.{allowed_client_events, allowed_server_events}` | Frontend permissions; omission means allow-all | No (WebRTC forks may override) |
| `delegation` | `{ type: "client" }` or `{ type: "responses", responses: {...} }`. Omitted or `null` means client. | Mode: no. `responses.*`: yes. |
| `delegation.responses.model` | Required, e.g. `gpt-5.6-terra` | Yes |
| `delegation.responses.instructions` | Backend prompt | Yes |
| `delegation.responses.tools` | `FunctionTool { name, type:"function", description?, parameters? (JSON Schema), strict? }` or `WebSearch { type:"web_search" }`, **nothing else** | Yes |
| `delegation.responses.tool_choice` | `"auto"` / `"none"` / `"required"` / `{ type:"function", name }`. The schema also lists `{ type:"mcp", name, server_label }`, but MCP tools cannot be registered. | Yes |
| `delegation.responses.parallel_tool_calls` | Boolean. The migration guide suggests `false` at first. | Yes |
| `delegation.responses.max_output_tokens` | ≥16 when set | Yes |
| `delegation.responses.reasoning` | `{ effort: none, minimal, low, medium, high, xhigh; summary: concise, detailed, auto }`, subject to the model | Yes |
| `delegation.responses.text.verbosity` | `low` / `medium` / `high` (backend text only) | Yes |
| `delegation.responses.service_tier` | Guide: `auto`, `default`, `flex`, `priority`. `"priority"` selects Fast mode. The reference enum also lists `fast_tier_temp_pilot` and `ultrafast`. | Yes |
| `store` | Default `false`; see §3.6 | No |

- **Updating:** `session.update` accepts only `session.delegation.responses` changes; omitted keys keep
  their values. It emits `session.updated` with the full resolved config.
- **Rejections:** unknown fields are rejected, and changing `model`, `instructions`, `input`, `audio`,
  `store` or the delegation mode fails with `immutable_field_update`.
- **Subset of Responses:** "Live supports a subset of the standalone Responses API". The Live
  `response.create` "does not accept a standalone Responses request body".

**Recommended `instructions` structure** (from the prompting guide):

- A short personality paragraph.
- `Backchannel policy:`
- `Interruption policy:`
- `Delegation policy:`, containing `Backend tools:`, `Delegate to the backend when:` and
  `Do not delegate to the backend when:`.
- End with "Delegate before giving an answer that depends on backend work. Do not guess the result while
  waiting."
- List only capabilities the backend really has, and put tool schemas and procedures in the backend prompt.

### 3.2 Context injection

The three client events take plain-string `content` of ≤500 tokens and a required `delegation_id`: either
`null`, or a known **client** delegation ID. A Responses response ID or tool call ID is not accepted.

| Event | Use | Acknowledgment |
|---|---|---|
| `session.instructions.append` | App-authored behavior: greetings, disclosures, "stop talking". **Can interrupt current speech.** Don't put untrusted tool output here. | `session.instructions.appended` |
| `session.thinking.append` | Quiet facts or progress, e.g. UI context | `session.thinking.appended` |
| `session.commentary.append` | Content to say aloud; the model paraphrases | `session.commentary.appended` |

**Timing and privacy**

- An acknowledgment carries `client_event_id`, `start_ms` and `end_ms`. It arrives once frame progress
  reaches the *estimated* end of injection.
- It does not prove the model consumed the content, and it does not confirm speech or playback.
- It can stay pending if frames stop. Closing the session reports errors for pending appends.
- "Quiet context can influence later speech; it is not a privacy boundary." Never send secrets.

([sessions: context](https://developers.openai.com/api/docs/guides/live-conversations#add-context-during-the-conversation))

**Greeting recipe**

1. After `session.started`, send `session.instructions.append` (`delegation_id: null`) with the greeting,
   its language, and "greet immediately, then listen".
2. Wait for the acknowledgment.
3. Keep input audio flowing, including silence.
4. Optionally follow with a short `session.commentary.append`, e.g. "Begin the conversation now…".

There is no "opening completed" event.
([sessions: greet](https://developers.openai.com/api/docs/guides/live-conversations#greet-before-the-caller-speaks))

### 3.3 Function calling: exact event flow (resolved)

**Delegation notice.** `session.delegation.created` looks like
`{ event_id, offset_ms, delegation: { id, type:"delegation", target:"client"|"responses", response_id? } }`.

- `response_id` is present only for `target: "responses"`.
- The object is metadata only, never the task text.
- Treat IDs as opaque and return them unchanged.

([primary WS ref](https://developers.openai.com/api/reference/resources/live/primary-websocket),
[delegation](https://developers.openai.com/api/docs/guides/live-delegation#handle-responses-delegation))

**Backend stream.** Backend events arrive wrapped as
`{ type:"response.event", event_id, delegation_id (may be null), event: {...Responses streaming event...} }`.
Dispatch on `envelope.event.type`, and tolerate unfamiliar nested lifecycle events.

**Responses delegation loop**

1. Track the response ID from the nested `response.created`, alongside the outer `delegation_id`.
2. **Collect calls only from nested `response.output_item.done`.** The finished function item has
   `call_id`, `name` and `arguments`; "an arguments-done event alone is not sufficient".
3. Forwarded lifecycle snapshots, including `response.completed`, **deliberately have `output: []`**, empty
   `tools`, `instructions: null`, and no `input`. An empty terminal output does not mean there are no
   pending calls.
4. Execute the authorized operation, then send:

   ```json
   {
     "type": "response.item.create",
     "event_id": "tool_result_1",
     "item": { "type": "function_call_output", "call_id": "call_123", "output": "{...}" }
   }
   ```

   This has **no success acknowledgment**; watch for `error` and the next nested lifecycle events.
5. After **all** pending results are in, send `{ "type": "response.create", "event_id": "continue_1" }`.
   - No body, model override or `delegation_id` is allowed on it.
   - Appending results does not auto-continue.
   - Both commands require Responses delegation.
6. If your app declines a pending call (blocked or superseded), still return an accurate "superseded" or
   "cancelled" output, then complete the batch.
7. For guardrails, stop executing the affected function and **don't send `response.create`**. This does not
   cancel an already-running hosted response or stop speech.

([delegation](https://developers.openai.com/api/docs/guides/live-delegation#complete-a-client-actionable-function-call),
[migration](https://developers.openai.com/api/docs/guides/live-migration),
[server controls](https://developers.openai.com/api/docs/guides/voice-server-controls?api=live#run-checks-alongside-the-conversation))

**Where the loop runs.** Nested `response.event` messages are delivered on the WebRTC data channel ("Use
the data channel for transcript deltas, session commands, and nested `response.event` messages"). "The
browser can forward function-call events from its data channel to an authenticated backend for execution."

- If both the browser and a sideband receive a function call, **execute it once**: assign one owner per
  action.

([WebRTC live](https://developers.openai.com/api/docs/guides/voice-webrtc?api=live#handle-media-and-events),
[server controls](https://developers.openai.com/api/docs/guides/voice-server-controls?api=live))

**Typed input (Responses mode).** Queue a user message with `response.item.create`, then send
`response.create`. Input items can carry `prompt_cache_breakpoint: { mode: "explicit" }` on `input_text`
parts. ([delegation: typed input](https://developers.openai.com/api/docs/guides/live-delegation#accept-typed-input),
[primary WS ref](https://developers.openai.com/api/reference/resources/live/primary-websocket))

**Client delegation**

1. On `session.delegation.created` with `target: "client"`, claim the ID so a duplicate delivery cannot
   start the work twice.
2. Build the request from role-labeled transcript fragments plus app state. A delegation can arrive before
   the sentence is complete; ask for clarification if needed.
3. Return progress with `session.thinking.append` and results with `session.commentary.append`, both with
   that ID. Repeated appends can continue the same delegation.
4. Check the task revision before announcing, so stale results are never spoken.

([migration: client adapter](https://developers.openai.com/api/docs/guides/live-migration),
[delegation](https://developers.openai.com/api/docs/guides/live-delegation#receive-a-client-delegation))

### 3.4 Turn-taking, interruptions, transcripts, mic

- **Turn-taking.** There are no VAD or turn-detection parameters. "Stream audio continuously. GPT-Live
  decides when to speak." Remove manual commits.
  ([migration](https://developers.openai.com/api/docs/guides/live-migration#adapt-the-connection-and-audio-lifecycle))
- **Backchannels and interruptions** are steered through the prompt policies. Don't add "never speak while
  the user is speaking", which suppresses backchannels.
  ([prompting](https://developers.openai.com/api/docs/guides/live-prompting))
- **Interruptions don't cancel backend work.** "Stopping speech does not automatically stop backend work."
  Track task revisions.
- **No end-of-speech events.** There is no `response.done`, no output-audio-done, and no truncate or cancel
  event in Live. Drive the "speaking" indicator from playback.
- **Transcripts.** `session.input_transcript.delta` and `session.output_transcript.delta` carry
  `{ delta, start_ms, end_ms }` on the session timeline (start inclusive, end exclusive).
  - They are not wall-clock time and **not exact word alignments**.
  - They have no item ID and no turn-completed event.
  - A missing event is not silence.
  - Concatenate fragments exactly as received.

  ([sessions: transcripts](https://developers.openai.com/api/docs/guides/live-conversations#transcript-deltas))
- **Mic.** `session.input_audio.mute` / `unmute` are acknowledged by `session.input_audio.muted` /
  `unmuted`. Muting does not stop inference, speech, delegated work, or billing.
- **Moderation.** It either ends the session, or cuts current assistant audio and emits `error` without
  closing. Read `error` events during playback.

### 3.5 Long conversations, memory, close

- **Compaction.** Older history is summarized in the background. Above 90% usage, a replacement voice
  engine starts in-session with the original instructions plus ≤8,192 tokens of recent history and summary.
  `session.usage.updated` includes `context_window.usage_ratio`. Keep durable facts in your app.
  ([sessions](https://developers.openai.com/api/docs/guides/live-conversations#manage-longer-conversations))
- **Usage.** `session.usage.updated.usage.seconds` is a cumulative snapshot; do not add snapshots together.
  Backend usage arrives in nested Responses completion events.
- **Graceful close:**
  1. Finish pending function results.
  2. Register a `session.closed` listener.
  3. Send `session.close` and keep transports open until `session.closed` arrives with `reason`,
     `usage.seconds` and a snapshot.

  `session.close` **cancels queued Responses work**, and a response waiting on a function result cannot
  continue. Reasons: `close_requested`, `expired`, `content`, `remote_hangup`, `connection_lost`.
  ([sessions: close](https://developers.openai.com/api/docs/guides/live-conversations#usage-and-graceful-close))
- **Idle cost.** "Closing saves $0.05 per minute of idle voice time." Resume later with a new session whose
  `input` carries a `developer` message summarizing the saved task state.
  ([cost](https://developers.openai.com/api/docs/guides/voice-latency-cost?api=live#close-the-session-during-long-tasks))

### 3.6 Store, fork, recording (resolved)

- **Enabling storage.** `store: true` must be enabled for the project. Recordings expire after 30 days. With
  ZDR, `store` is treated as `false`, so there are no forks or downloads.
  ([your data](https://developers.openai.com/api/docs/guides/your-data#v1livesessions))
- **WebRTC fork.** Send a new SDP offer to `POST /v1/live/sessions/{source_id}/fork`
  (`client.live.sessions.fork(id, { transport: { type:"webrtc", sdp } })`).
  - Overridable: `store`, Responses settings, and frontend permissions.
  - `audio.format` is rejected.
- **WebSocket fork.** Connect to `wss://api.openai.com/v1/live/sessions/{source_id}/fork` and send
  `session.start` with a required `session` object (`{}` means no overrides).
  - Overridable: `store`, Responses settings, and `audio.format`, which is *not* inherited (default PCM16
    24 kHz).
  - Inherited frontend permissions are discarded.
  - Do not resend model, instructions or input.
- **Fork semantics.** A fork is a **new session with a new ID** and does not reopen the old connection.
  Omitting `store` inherits it.
- **Recording.** `GET /v1/live/sessions/{id}/content` (`client.live.sessions.downloadRecording(id)`) returns
  stereo WAV: left channel input, right channel output. It requires a finalized stored recording, and stored
  sessions take longer to finalize.
- **Recovery.** If a stored session exists, fork it. Otherwise start a new session seeded through `input`.
  Reconcile pending actions before retrying.

([sessions: store and fork](https://developers.openai.com/api/docs/guides/live-conversations#store-and-fork-a-session),
[fork WS ref](https://developers.openai.com/api/reference/resources/live/fork-websocket))

---

## 4. Features relevant to an AI tutor

| Need | GPT-Live approach | Source |
|---|---|---|
| Retrieval mid-conversation | Responses delegation plus our `function` tools. Speech continues while tools run. | [delegation](https://developers.openai.com/api/docs/guides/live-delegation) |
| Hosted file search or MCP | **Not available** in delegation: tools are `function` and `web_search` only. For a vector store, call it from our own function, or use client delegation with our own Responses call. | [primary WS ref](https://developers.openai.com/api/reference/resources/live/primary-websocket) |
| Deep answers | Choose the backend model and `reasoning.effort`. `session.update` can raise effort mid-session. | [delegation](https://developers.openai.com/api/docs/guides/live-delegation#reduce-backend-latency) |
| Page, equation or screen images | Vision-capable backend: `response.item.create` with an image input item, then `response.create` | [delegation: images](https://developers.openai.com/api/docs/guides/live-delegation#add-images-and-visual-context) |
| "What am I looking at" context | `session.thinking.append`, `delegation_id: null`, with a concise summary built from app state. Skip unchanged updates and state corrections explicitly. | [delegation: UI context](https://developers.openai.com/api/docs/guides/live-delegation#share-ui-context) |
| Speculative retrieval | Watch the input transcript and start lookups early; discard stale results | [delegation: fragments](https://developers.openai.com/api/docs/guides/live-delegation#react-to-transcript-fragments) |
| Resume a lesson | `input` seed (≤8,192 tokens), or fork a stored session | [sessions](https://developers.openai.com/api/docs/guides/live-conversations) |
| Must-say wording (e.g. "AI tutor, may be wrong") | `session.instructions.append` disclosure recipe; delivery is not guaranteed verbatim | [sessions: disclosure](https://developers.openai.com/api/docs/guides/live-conversations#deliver-a-disclosure) |

If in-model MCP, image input or VAD tuning is required, `gpt-realtime-2.1` still has them.
([realtime-mcp](https://developers.openai.com/api/docs/guides/realtime-mcp))

---

## 5. SDKs and code

### 5.1 openai-node (`openai`)

From [api.md](https://github.com/openai/openai-node/blob/master/src/resources/live/api.md) and the guides:

- `client.live.create({ session, transport })` wraps `POST /v1/live/sessions`.
- `client.live.sessions.accept(id, …)`, `.fork(id, …)`, `.hangup(id)`, `.refer(id, …)`, `.reject(id, …)` and
  `.downloadRecording(id)`.
- WebSocket classes such as `ForksWS` from `openai/resources/live/forks/ws`.
- Python has matching `client.live.forks.connect(...)`, `AsyncLiveConnection` and
  `AsyncSidebandConnection`.
- Use an SDK version with Live support.

### 5.2 Agents SDK for TypeScript (`@openai/agents`)

- `RealtimeAgent` / `RealtimeSession` (`@openai/agents/realtime`) target **Realtime only**
  (`gpt-realtime-2.1`, `ek_` keys). ([realtime](https://developers.openai.com/api/docs/guides/realtime))
- There is no GPT-Live support through v0.18.0.
  ([releases](https://github.com/openai/openai-agents-js/releases))

### 5.3 GPT-Live browser WebRTC

The official browser client is in [WebRTC live](https://developers.openai.com/api/docs/guides/voice-webrtc?api=live).
Essentials, condensed from it:

```js
const pc = new RTCPeerConnection();
pc.addEventListener("track", (e) => { audio.srcObject = new MediaStream([e.track]); });
const mic = await navigator.mediaDevices.getUserMedia({ audio: true });
for (const t of mic.getAudioTracks()) pc.addTrack(t, mic);

const events = pc.createDataChannel("oai-events"); // before createOffer
events.addEventListener("message", ({ data }) => onLiveEvent(JSON.parse(data)));

await pc.setLocalDescription(await pc.createOffer());
// wait for pc.iceGatheringState === "complete" (docs use a 10 s timeout)
const res = await fetch("/api/live/session", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({ sdp: pc.localDescription.sdp }),
});
const result = await res.json(); // { session: { id }, transport: { sdp } }
await pc.setRemoteDescription({ type: "answer", sdp: result.transport.sdp });
// wait for session.started; never send session.start on this channel
```

**Server route sketch** **[Inference]**. It follows the documented `client.live.create` shape and the BYOK
rules in §2.2; verify the types against openai-node.

```ts
// src/routes/api/live/session/+server.ts
import OpenAI from "openai";
import { json, error } from "@sveltejs/kit";
import { TUTOR_SESSION } from "$lib/server/voice/session-config"; // server-owned

export async function POST({ request }) {
  const apiKey = request.headers.get("authorization")?.replace(/^Bearer\s+/i, "");
  const { sdp } = await request.json().catch(() => ({}));
  if (!apiKey) throw error(401, "Missing OpenAI key");
  if (typeof sdp !== "string" || !sdp.trim()) throw error(400, "SDP offer required");

  try {
    const result = await new OpenAI({ apiKey, maxRetries: 0 }).live.create({
      session: TUTOR_SESSION, // model, instructions, delegation.responses.{model,tools,...}, client.data_channel
      transport: { type: "webrtc", sdp },
    });
    return json(
      { session: { id: result.session.id }, transport: { sdp: result.transport.sdp } },
      { status: 201, headers: { "cache-control": "no-store" } }
    );
  } catch (e) {
    if (e instanceof OpenAI.APIError) throw error(e.status ?? 502, "Live session creation failed");
    throw e;
  }
}
```

**Browser tool loop** (Responses delegation). The event shapes come from two places:
[delegation](https://developers.openai.com/api/docs/guides/live-delegation#complete-a-client-actionable-function-call),
and the [Responses streaming events reference](https://developers.openai.com/api/reference/resources/responses/streaming-events)
for the nested events. The batching logic is ours.

What that reference confirms about the nested events:

- **Function-call item.** `response.output_item.done` has top-level fields `item`, `output_index`,
  `sequence_number` and `type`, and **no `response_id`**. A function call is
  `item: { type: "function_call", call_id, name, arguments }`.
- **Correlation.** Because the item event carries no response ID, match calls to responses by the Live
  envelope's outer `delegation_id`, plus the `response.id` from the nested `response.created`.
- **Terminal event.** `response.completed` carries `response.id`, and its forwarded snapshot has
  `output: []`. There is no `response.done` in Responses streaming.

```js
const byDelegation = new Map(); // delegation_id -> { responseId, calls: Map<call_id, item> }

async function onLiveEvent(msg) {
  if (msg.type !== "response.event") return handleSessionEvent(msg); // transcripts, delegation, usage, error, info
  const ev = msg.event;
  const key = msg.delegation_id ?? "uncorrelated";
  if (ev.type === "response.created") {
    byDelegation.set(key, { responseId: ev.response.id, calls: new Map() });
  } else if (ev.type === "response.output_item.done" && ev.item?.type === "function_call") {
    byDelegation.get(key)?.calls.set(ev.item.call_id, ev.item);
  } else if (ev.type === "response.completed") {
    const entry = byDelegation.get(key);
    if (!entry || entry.responseId !== ev.response.id || entry.calls.size === 0) return;
    const results = await Promise.all(
      [...entry.calls.values()].map(async (c) => ({
        call_id: c.call_id,
        output: JSON.stringify(await runTool(c.name, JSON.parse(c.arguments))), // runTool returns {ok:false,...} on failure
      }))
    );
    entry.calls.clear();
    for (const r of results) {
      send({ type: "response.item.create", event_id: crypto.randomUUID(), item: { type: "function_call_output", ...r } });
    }
    send({ type: "response.create", event_id: crypto.randomUUID() }); // once, after every result
  }
}
const send = (e) => events.send(JSON.stringify(e));
```

**[Unverified]**

- **Which event to act on.** It is not established whether the Live service forwards
  `response.completed` before it expects the results, or whether the app may send results as soon as each
  `response.output_item.done` arrives. The docs only say to submit every required result before
  `response.create`.
- **Failure terminals.** Handling for `response.failed` / `response.incomplete` is not covered on the Live
  pages.

Log real traffic before hardening this code.

---

## 6. Migration notes: gpt-realtime-2.x to GPT-Live

Source: [Migrate to GPT-Live](https://developers.openai.com/api/docs/guides/live-migration).

**Choosing a delegation mode.** Responses delegation suits a Realtime app where the model picked functions.
Client delegation suits an existing text agent or orchestrator. Either migration path can use either mode.

### 6.1 Event mapping

| Realtime | GPT-Live |
|---|---|
| `/v1/realtime`, `/v1/realtime/calls` (multipart), `/v1/realtime/client_secrets` | `POST /v1/live/sessions` (JSON), `…/{id}/attach`, `/fork`, `/accept`, `/refer`, `/hangup`, `GET …/{id}/content`; no client secrets |
| Sideband `wss://…/v1/realtime?call_id=` (from the `Location` header) | `wss://…/v1/live/sessions/{session_id}/attach` (from the JSON `session.id`) |
| `session.update` (full config) | Create body or `session.start`. `session.update` covers `delegation.responses` only. |
| `input_audio_buffer.append` | `session.input_audio.append` (base64 `audio`; WebSocket only) |
| Commit or `response.create` for manual turns | Removed; stream continuously |
| `response.output_audio.delta` | `session.output_audio.delta` (WebSocket only) |
| `response.output_audio.done`, `response.done` | No equivalent; track playback on the client |
| `conversation.item.input_audio_transcription.delta` / `.completed` | `session.input_transcript.delta` (no completed event) |
| `response.output_audio_transcript.delta` | `session.output_transcript.delta` |
| `session.tools` / `response.tools`, `tool_choice`, `parallel_tool_calls` | `delegation.responses.tools` / `.tool_choice` / `.parallel_tool_calls` (Responses function schema) |
| Read `response.output_item.done` | Unwrap `response.event`, then read the inner `response.output_item.done` |
| `conversation.item.create` (`function_call_output`) | `response.item.create`, then `response.create` after all results |
| `response.create` meaning "speak now" | `response.create` means continue backend work; "does not grant permission for the voice model to speak" |
| `conversation.item.truncate` / `.delete` / `.retrieve`, `response.cancel`, `output_audio_buffer.clear` | Not in the Live client-event list ([primary WS ref](https://developers.openai.com/api/reference/resources/live/primary-websocket)) |
| `input_image` on the voice model | Vision backend only |
| `mcp` tools, `prompt` (id/variables), `truncation`, `output_modalities`, `turn_detection`, `noise_reduction` | Absent from the Live session schema |
| One prompt | Split. Voice: style and delegation policy. Backend: rules, tools, confirmations. |

### 6.2 Other points

- **Audio decisions.** The backend never receives audio. For acoustic decisions, route audio to a separate
  detector, e.g. a parallel Realtime session.
- **Guardrails.** Block actions in code, send `session.instructions.append`, and remember that already-heard
  audio cannot be retracted.
- **Transcription models.** `whisper-1` and `gpt-4o-*-transcribe` shut down 2027-02-26.
  ([changelog](https://developers.openai.com/api/docs/changelog))

---

## 7. ElevenLabs TTS: timestamps and models

### 7.1 HTTP with timestamps

Sources: [stream-with-timestamps](https://elevenlabs.io/docs/api-reference/text-to-speech/stream-with-timestamps),
[convert-with-timestamps](https://elevenlabs.io/docs/api-reference/text-to-speech/convert-with-timestamps).

- **Endpoints:** `POST /v1/text-to-speech/{voice_id}/stream/with-timestamps` (streaming) and
  `POST /v1/text-to-speech/{voice_id}/with-timestamps` (single response). Header `xi-api-key`.
- **Query parameters:** `output_format` (default `mp3_44100_128`), `enable_logging`, and
  `optimize_streaming_latency` (deprecated).
- **Body:**
  - `text`
  - `model_id` (default `eleven_multilingual_v2`)
  - `language_code`
  - `voice_settings` (`stability`, `similarity_boost`, `style`, `speed`, `use_speaker_boost`)
  - `seed`
  - `previous_text` / `next_text`
  - `previous_request_ids` / `next_request_ids` (≤3 each)
  - `apply_text_normalization` (`auto` / `on` / `off`)
  - pronunciation dictionary locators (≤3)
- **Chunk shape:**

  ```json
  {
    "audio_base64": "...",
    "alignment": {
      "characters": [],
      "character_start_times_seconds": [],
      "character_end_times_seconds": []
    },
    "normalized_alignment": { "...": "same shape" }
  }
  ```

- **Granularity is character-level.** Group characters into words on whitespace; the docs note alignment
  "can be used to obtain word-level timestamps".
  ([realtime TTS guide](https://elevenlabs.io/docs/eleven-api/guides/how-to/websockets/realtime-tts))
- **[Unverified]** `eleven_v3` on the HTTP with-timestamps endpoints. The only stated requirement is that
  the model has `can_do_text_to_speech`; test it.

### 7.2 WebSockets and browser tokens

- **Single-stream:** `wss://api.elevenlabs.io/v1/text-to-speech/{voice_id}/stream-input`.
  ([ref](https://elevenlabs.io/docs/api-reference/text-to-speech/v-1-text-to-speech-voice-id-stream-input))
  - Query parameters: `model_id`, `output_format`, `sync_alignment`, `inactivity_timeout`, `auto_mode`,
    `apply_text_normalization`, `authorization` / `single_use_token`.
  - Messages returned: `{ audio, alignment: { chars, charStartTimesMs, charDurationsMs }, normalizedAlignment }`,
    then `{ isFinal: true }`.
- **`eleven_v3` is not supported.** "That endpoint does **not** support the `eleven_v3` model."
  ([realtime TTS guide](https://elevenlabs.io/docs/eleven-api/guides/how-to/websockets/realtime-tts))
- **Multi-context:** `.../multi-stream-input`, where messages carry a `contextId`.
  ([ref](https://elevenlabs.io/docs/api-reference/multi-context-text-to-speech/v-1-text-to-speech-voice-id-multi-stream-input))
- **Browser-safe token:** `POST /v1/single-use-token/tts_websocket` (with `xi-api-key`) mints a token that
  expires in 15 minutes and is consumed on use. Pass it as `single_use_token`.
  ([tokens](https://elevenlabs.io/docs/api-reference/tokens/create))

### 7.3 Models

Source: [elevenlabs.io/docs/overview/models](https://elevenlabs.io/docs/overview/models).

| Model ID | Latency | Languages | Char limit | Use |
|---|---|---|---|---|
| `eleven_v3` | standard | 70+ | 5,000 | Most expressive; audio tags; GA ([blog](https://elevenlabs.io/blog/eleven-v3-is-now-generally-available)) |
| `eleven_v3_conversational` | ~280 ms | 70+ | n/a | Expressive realtime synthesis |
| `eleven_multilingual_v2` | standard | 29 | 10,000 | Stable narration; API default |
| `eleven_flash_v2_5` | ~75 ms | 32 | 40,000 | Recommended for low latency |
| `eleven_flash_v2` | ~75 ms | English | 30,000 | Low-latency English |
| `eleven_turbo_v2_5`, `eleven_turbo_v2` | n/a | n/a | n/a | Deprecated; use Flash |

---

## 8. Implications for grbook.ai

Everything in this section is **[Inference]**. It applies the documented GPT-Live contract (§2–§3) to the
repository as it stands on 2026-09-12:

- a SvelteKit scaffold with `@sveltejs/adapter-vercel`, drizzle/libsql and better-auth;
- the knowledge vault in `knowledge/`, specified in `knowledge/README.md` and
  `knowledge/_schemas/chapter-dossier.schema.json`.

### 8.1 Architecture decision

| Decision | Choice | Why |
|---|---|---|
| Voice model | `gpt-live-1` | Full duplex and interruption handling suit tutoring. $0.05/min is predictable. |
| Delegation mode | **Responses delegation** (`gpt-5.6-terra`; `gpt-5.6-luna` for cheap sessions) | GPT-Live manages the backend connection, context and tool selection; we only implement functions. The mode cannot change mid-session, so pick it per session. |
| `web_search` | Off by default | Keeps the tutor grounded in the vault. Enable only for an explicit "current research" feature. |
| Tool loop owner | **Browser**, over the `oai-events` data channel | Officially supported ("browser can forward function-call events… to an authenticated backend"). No long-lived server socket, which Vercel functions cannot hold for a whole lesson. |
| Retrieval execution | Stateless SvelteKit `+server.ts` endpoints over a build-time vault index, plus pure client tools for UI actions | Fast, cacheable, and never needs the user's OpenAI key |
| Sideband | Not in v1 | Needed only for server-side guardrails or speculative lookups. If added later, run it on a long-lived worker (not a Vercel function), with a single owner per action. |
| Client delegation | Later, for "deep answer" pipelines | Choose it when we must compose multiple models or validate or redact results before GPT-Live hears them. It costs us transcript assembly and context management. |

### 8.2 What the knowledge base must expose as callable functions

Constraints from `knowledge/README.md`:

- The vault stores **paraphrased notes and locators, never book page text**. `book-sources/` is gitignored
  and never deployed.
- Tool outputs must therefore return notes, transcribed equations and locators (`SCH §5.3 p.125 (pdf 143)`),
  never page text.
- Prose quoted from a book stays within the vault's no-12-word-overlap rule.

Keep outputs compact. The backend reads them, and GPT-Live only hears what the backend returns; commentary
appends are ≤500 tokens. Put display-only payloads (full LaTeX, figure redesigns) in the app, not in the tool
result.

Each function is registered in `delegation.responses.tools` as
`{ type: "function", name, description, parameters, strict: true }`.

**v1: book-reader tutor, phase 1 dossiers and TOC**

| Function | Arguments | Returns | Executes | Backed by |
|---|---|---|---|---|
| `get_reading_context` | `{}` | Current book, unit, section, locator, selection, visible equation IDs | **Browser** (reader state) | App state |
| `search_knowledge` | `{ query, book?: "schutz"\|"gifted-amateur"\|"dinverno", unit_id?, kinds?: ("concept"\|"equation"\|"example"\|"misconception"\|"analogy"\|"figure")[], limit? ≤5 }` | `[{ id, kind, title, summary (≤60 words, paraphrase), locator }]` | Server `GET /api/kb/search` | Generated `knowledge/_index` (lexical first; embeddings later) |
| `get_unit_dossier` | `{ book, unit_id, fields?: ("one_line_summary"\|"learning_objectives"\|"assumed_background"\|"concepts"\|"key_equations"\|"teaching_approach"\|"tutor_notes"\|"gaps_and_pitfalls")[] }` | The selected dossier fields only | Server `GET /api/kb/unit` | `sources/<book>/chapters/<unit>.json` |
| `get_equation` | `{ book, equation_id }` | `{ latex, spoken (how to say it aloud), symbols: [{ symbol, meaning }], conventions, locator }` | Server | Dossier `key_equations`, later `notation/` |
| `get_worked_example` | `{ book, unit_id, example_id? , concept? }` | Paraphrased setup, solution steps and result, locator | Server | Dossier `worked_examples` |
| `find_misconceptions` | `{ concept \| query }` | `[{ misconception, why_wrong, correction, source_locator }]` | Server | Dossier `misconceptions_addressed`, later `pedagogy/` |
| `show_in_reader` | `{ locator? , equation_id?, highlight?: string }` | `{ shown: true }` | **Browser** (navigate or highlight) | Reader UI |

**v2: after phases 2–5 (concept union, pedagogy, curriculum, tutor layer)**

| Function | Purpose | Backed by |
|---|---|---|
| `get_concept` `{ concept_id }` | Canonical definition, per-book treatment, key equations, analogies, misconceptions | `concepts/<domain>/<id>.md` |
| `get_prerequisites` `{ concept_id, depth? }` | Prerequisite DAG slice for "you need X first" | `curriculum/` |
| `get_analogies` / `get_thought_experiment` `{ concept_id }` | Pedagogy catalogs | `pedagogy/` |
| `compare_notation` `{ symbol \| convention }` | Sign conventions and symbol crosswalk across SCH, GA and DIV | `notation/` |
| `get_learner_state` `{ concept_ids }` | Mastery and recent errors, to adapt explanations | DB (auth required) |
| `record_learner_evidence` `{ concept_id, evidence, outcome }` | Learner-model write | **Server** with better-auth session; idempotency key = `call_id` |

**Contract rules for every function**

- **Deterministic and read-only**, except `record_learner_evidence` and `show_in_reader`.
- **Fast:** target under 300 ms for server tools.
- Return `{ ok: false, reason }` rather than throwing.
- Include a `locator` so the backend can cite and the app can call `show_in_reader`.
- **Never** return raw book page text or figure images from `book-sources/`.

### 8.3 Where the tool loop runs, step by step

1. **Session creation.** The browser posts the SDP offer and the user's key in a header to
   `POST /api/live/session`. The server builds `TUTOR_SESSION`:
   - voice `instructions`: tutor persona, backchannel and interruption policy, and a delegation policy
     listing the KB capabilities;
   - `delegation.responses`: backend prompt, the tools above, `parallel_tool_calls: false` at first, and
     `reasoning.effort: "low"` (raise it with `session.update` for derivations);
   - `input`: seed from learner state, ≤8,192 tokens;
   - `client.data_channel.allowed_client_events`: `["response.item.create", "response.create",
     "session.thinking.append", "session.instructions.append", "session.input_audio.mute",
     "session.input_audio.unmute", "session.close"]`;
   - `allowed_server_events`: transcripts, `session.*` lifecycle, `error`, `info`, and the needed
     `response.event` selectors.

   The route returns the SDP answer.
2. **On `session.started`,** send `session.thinking.append` (`delegation_id: null`) with the reading
   context, e.g. "Reader is on SCH §5.3 p.125; equation 5.12 is highlighted." Resend it when navigation
   changes, debounced and only when changed. Optionally send a greeting through
   `session.instructions.append`.
3. **Browser receives `response.event`,** collects function calls from the nested
   `response.output_item.done`, and dispatches each:
   - **client tools** (`get_reading_context`, `show_in_reader`) run locally;
   - **KB tools** call `/api/kb/*` with app auth; no OpenAI key is involved.
4. **Browser sends** each `function_call_output` with `response.item.create`, then **one** `response.create`
   after all calls in that response are answered. Superseded calls get
   `{ "ok": false, "reason": "superseded" }`.
5. **UI.** Show captions from the transcript deltas. Show tool activity in a status area, not in the
   captions. When a tool returns a locator, call `show_in_reader` so the page follows the conversation.
6. **Narration.** When a voice session starts, pause ElevenLabs narration playback. Do not run TTS narration
   and GPT-Live output at the same time.
7. **End.** Idle for N minutes, or "End tutor": send `session.close`, wait for `session.closed`, then persist
   a task and learner summary. "Resume" starts a new session with that summary in `input`. Keep
   `store: false` unless the user opts in, because stored sessions keep recordings for 30 days.

### 8.4 Open items to verify with a live key before building

- **Tool-result timing.** Test whether results should be sent right after each nested
  `response.output_item.done`, or after `response.completed`. The item and terminal event shapes are
  confirmed (§5.3).
- Whether `OpenAI-Safety-Identifier` applies to `POST /v1/live/sessions`.
- The session duration limit: read `session.started.session.expires_at`.
- Whether the browser can call `api.openai.com/v1/live/sessions` directly with a user key (CORS). Even if
  it can, the docs say not to expose the key to the browser. Keep the broker.
- ElevenLabs `eleven_v3` on the HTTP with-timestamps endpoints.
