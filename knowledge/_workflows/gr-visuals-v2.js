export const meta = {
  name: 'gr-visuals-v2',
  description: "Turn visuals proposed in a domain's concept notes into reviewed component contracts in the visual network (max 5 agents in flight)",
  phases: [
    { title: 'Plan', detail: 'merge duplicate proposals, choose canonical picture ids, update note references' },
    { title: 'Write', detail: 'write one catalog entry per agent: params, presets, readouts, tours, model and tests' },
    { title: 'Novice read', detail: 'a beginner reads the tours, readout speech, labels and caption' },
    { title: 'Physics review', detail: 'recompute the model and every test, check states, branches, claims and links' },
    { title: 'Re-read', detail: 'the beginner reads speech changed after the novice read' },
    { title: 'Diff check', detail: 'the physicist checks text changed after the physics review' },
  ],
}

const ROOT = '/Users/neo/repos/grbook.ai'
const KB = `${ROOT}/knowledge`
const T = `${KB}/_tools`
const domain = args && args.domain
const DATE = (args && args.date) || 'unknown-date'
const SNAP = args && args.snap_dir
const GROUP = (args && args.group_size) || 1
if (!domain) throw new Error('args.domain is required')
if (!SNAP) throw new Error('args.snap_dir is required: a directory outside the repository for snapshots')

const MAX_AGENTS = Math.min((args && args.max_agents) || 5, 5)
let active = 0
const waiting = []
async function slot(priority, fn) {
  if (active >= MAX_AGENTS) await new Promise((resolve) => waiting.push({ priority, resolve }))
  else active++
  try {
    return await fn()
  } finally {
    if (waiting.length) {
      let best = 0
      for (let i = 1; i < waiting.length; i++) if (waiting[i].priority > waiting[best].priority) best = i
      waiting.splice(best, 1)[0].resolve()
    } else active--
  }
}

const CONTEXT = `CONTEXT: grbook.ai is a general relativity book and interactive learning experience with a live voice AI tutor and 2D/3D demos, for learners from zero to research level. Visuals (diagrams, widgets, animations, 3D demos) form their own network in ${KB}/visuals/<id>.json, linked to concepts and to each other. Developers build components from these entries, the tests compile into unit tests, and the tutor speaks the tours and readouts aloud, so every state must be buildable, every expected value correct, and every spoken line clear to its rung. Today's date: ${DATE}.

BINDING DOCUMENTS (read once, completely, before starting): the standard card ${KB}/_meta/standard-card.md (sections 4, 5, 6 and 10 bind every spoken line and every model); the schema ${KB}/_schemas/visual.schema.json; ${KB}/notation/course-conventions.md; and the exemplar visual ${KB}/visuals/carry-an-arrow-around-a-loop.json. Open the full guide ${KB}/_meta/writing-guide.md only at the section a validator warning names. Do not read the holonomy note; use its digest.

TOOLS:
- Visual ids: python3 ${T}/visual_ids.py [--missing] [--domain <id>] [--grep <word>] [--json]
- Book sections (the unit of writing; a visual serves the concepts a section teaches): ${KB}/book/sections/<chapter>/<id>.json, indexed by ${KB}/book/outline.json. Read a section's summary, the part teaching a concept, its checks, misconceptions and the visual's sketch with ONE python one-liner; never read whole section files.
- Concept notes where they exist: python3 ${T}/note_digest.py [--ways entry,working] <concept> [...]. Never read a note file directly.
- COUNT YOUR TOOL CALLS. Every call re-reads your whole context, so cost tracks the number of calls. A writer needs about 25 calls, a reviewer about 25. Compute all test expectations in ONE python script; write the entry in ONE Write call; apply all validator fixes in ONE pass; at most three validate-then-fix rounds; validator output through head -60; render once at the end; never re-read a file.
- Figure ideas from the textbook study, only for concepts with neither a section nor a note: python3 ${T}/concept_evidence.py --id <concept>, section "Figures and redesign ideas", with image paths under ${ROOT}/book-sources/ that you may view for inspiration only; never reproduce or name them.
- Earlier course assets (demos, labs, figures; reuse encouraged): ${KB}/sources/legacy/*.json
- Numbers: python3 (no numpy or sympy; write plain python)
- Changed text: python3 ${T}/note_diff.py <before.json> <after.json> lists strings that differ, tagged by the rung of the tour or item that holds them ("none" for readouts, labels, model and design rules).
- Snapshots: ${SNAP} (run mkdir -p first).
- Validate: python3 ${T}/validate.py visual ${KB}/visuals/<id>.json ; notes: python3 ${T}/validate.py concept <note.json>. Fix every error and warning unless your task names one as expected.
- Render: python3 ${T}/render_visual.py ${KB}/visuals/<id>.json ; notes: python3 ${T}/render_concept.py <note.json>`

const PLAN_SCHEMA = {
  type: 'object',
  required: ['visuals', 'problems'],
  properties: {
    visuals: {
      type: 'array',
      items: {
        type: 'object',
        required: ['id', 'title', 'kind', 'priority', 'serves', 'merged_from'],
        properties: {
          id: { type: 'string' },
          title: { type: 'string' },
          kind: { type: 'string' },
          priority: { type: 'string' },
          serves: { type: 'array', items: { type: 'string' } },
          merged_from: { type: 'array', items: { type: 'string' } },
        },
      },
    },
    problems: { type: 'array', items: { type: 'string' } },
  },
}
const DONE_SCHEMA = {
  type: 'object',
  required: ['visuals', 'problems'],
  properties: {
    visuals: {
      type: 'array',
      items: {
        type: 'object',
        required: ['id', 'validator'],
        properties: {
          id: { type: 'string' },
          validator: { enum: ['OK', 'WARNINGS', 'ERRORS'] },
          verdict: { enum: ['accurate', 'fixed', 'needs-attention'] },
          stumbles: { type: 'integer' },
          errors_fixed: { type: 'integer' },
          learner_changes: { type: 'integer', description: 'Physics review: spoken or displayed strings note_diff.py lists as changed (tours, readout speech, labels, caption, accessibility)' },
          edited: { type: 'boolean', description: 'True if this stage changed spoken or displayed text' },
        },
      },
    },
    problems: { type: 'array', items: { type: 'string' } },
  },
}
const LEARNER_TEXT = 'tour beats (say, predict, describe), readout labels and say and say_negative templates, param and option labels, preset labels, title, picture, makes_visible, variants, and accessibility text'

phase('Plan')
const plan = await slot(1, () =>
  agent(
    `${CONTEXT}

TASK: Plan the catalog entries for visuals proposed in domain "${domain}".
1. Run visual_ids.py --missing --domain ${domain}, and visual_ids.py for the whole catalog. Read each proposal's sketch where it is listed (visual_ids.py prints it).
2. Group proposals that describe the same picture, even under different names or in other domains, and match any proposal an existing catalog entry already covers.
3. For each group, choose one canonical id that names the picture, not the concept (guide section 10), and decide kind and priority.
4. Edit every section in ${KB}/book/sections/ and every concept note in ${KB}/concepts/ that uses a non-canonical or already-covered id: change the id everywhere in that file, keep the most informative sketch, validate (validate.py section or concept), and re-render (render_section.py or render_concept.py). Visual ids are not learner-visible prose, so do not bump the note's revision and do not edit any prose.
5. Return the NEW catalog entries to write. For each, give every concept it serves across all domains, and the proposal ids it merges.`,
    { label: `plan:${domain}`, phase: 'Plan', schema: PLAN_SCHEMA, effort: 'high' },
  ),
)
const planned = (plan && plan.visuals) || []
log(`${planned.length} new visuals planned for ${domain}`)
const groups = []
for (let i = 0; i < planned.length; i += GROUP) groups.push(planned.slice(i, i + GROUP))

const writePrompt = (g) => `${CONTEXT}

TASK: Write catalog entries for these planned visuals: ${JSON.stringify(g)}.
For each visual:
1. For every concept it serves, read the section that teaches it (summary, the part teaching the concept, its checks and misconceptions, and this visual's sketch) and the note digest where a note exists. Read figure evidence only for concepts with neither. Read matching legacy assets when the evidence names one.
2. Design the component contract (guide section 10), following the exemplar field by field:
   - title, kind, priority, rungs, makes_visible, a plain caption in picture, print_figure for the book, and variants from a static card up;
   - params: typed (enum, number, integer, boolean, path, progress), with options, ranges, steps, units, defaults, effect, and available_when constraints on params and options so only combinations that make sense can be chosen;
   - presets: named states (param id to value, no preset key); every state that a tour, a test or a note reference uses must be a declared preset whose combination is available;
   - readouts: label, unit from the validator's unit table, sense for every signed quantity stated intrinsically as in course conventions, range as the reported branch (angles use (-180, 180]), decimals, visible_when, and say plus say_negative templates in speech format;
   - tours: one tour per served concept and rung where a guided walk helps, with at least 3 beats. Each beat gives rung, state (a preset id plus overrides), animate or null, await, predict (the question asked before the reveal) or null, check (the check the prediction evidences: <concept>/checks/<id> in a note or <section-id>/checks/<id> in a section; it must exist) or null, show for authors, say in first person naming what is on screen by colour and line style with directions relative to the path and no skipped step, and describe for a listener who cannot see. Entry-rung beats obey the novice contract;
   - design_rules: each rule says what it prevents, with the misconception address it guards against (<concept>/misconceptions/<id> in a note or <section-id>/misconceptions/<id> in a section), or null;
   - model: a summary, equations in course conventions with say lines and conditions, the numerical method, and tests. Each test gives a full state (progress 1 when a readout appears only on completion), expected readout values with tolerances computed with python3, and the readouts that must stay hidden. Cover every preset used by a tour, both signs and both branches of every signed readout, limits (flat case zero, small-size leading order), and at least one boundary case;
   - serves (every concept, with how it uses the visual), builds_on, leads_to and variant_of using existing or planned ids, accessibility (summary, static_alt, keyboard), starting_material and provenance.
3. Set status "proposed", revision 1, and updated "${DATE}". Write ${KB}/visuals/<id>.json. Validate until OK, then render.
4. In each section that teaches a served concept, and in each served note, make sure visuals[] lists the id (a catalog visual needs no sketch). Do not edit prose. Validate and re-render each file you touched.
Return the summary object.`

const novicePrompt = (g, w) => `${CONTEXT}

TASK: You are the NOVICE READER for these visuals: ${g.map((x) => x.id).join(', ')}. The writer reported: ${JSON.stringify(w || {})}
For each visual ${KB}/visuals/<id>.json:
1. Adopt the persona strictly: a curious 16-year-old with school algebra and geometry, no calculus and no physics beyond everyday experience, who has read only the entry ways of the served concepts. For working-rung tours, read as a strong second-year undergraduate.
2. Read the ${LEARNER_TEXT}, beat by beat, as if the tutor were speaking while you watch. Picture what each beat's show line puts on screen.
3. BEFORE changing anything, write retell_attempt: what you would say back after the entry tour.
4. Record every stumble as {quote, problem, rewrite}: the novice review's stumble list (guide section 11), plus a say line that does not name what is on screen, a direction without its reference, a prediction you could not make from what you have seen so far, a readout phrase that sounds wrong for a negative or zero value, and a colour-only distinction without a second cue.
5. Fix wording only. Never change what a line claims, a number, a sign or a state. If a beat needs a different state, order or claim, describe it in concerns.
6. If you changed spoken or displayed text, bump revision by exactly 1. Add review.novice with verdict, date "${DATE}", reviewed_revision (the visual's revision), retell_attempt, stumbles, fixes and concerns. Keep status "proposed". Validate until OK, then render.
Return the summary object with stumbles and edited per visual.`

const physicsPrompt = (g, n) => `${CONTEXT}

TASK: You are the ADVERSARIAL PHYSICS REVIEWER for these visuals: a GR physicist who also builds interactive demos. Visuals: ${g.map((x) => x.id).join(', ')}. The novice reader reported: ${JSON.stringify(n || {})}
For each visual ${KB}/visuals/<id>.json:
0. Run mkdir -p ${SNAP} and copy the visual to ${SNAP}/<id>.before-physics.json before editing.
1. Re-derive every model equation in course conventions. Write a small independent python3 implementation of the model and recompute every test expectation from its state; check tolerances, hidden readouts and progress.
2. Check the contract can be built: every param range, step and default; every available_when constraint (no preset, tour state or test uses an unavailable combination); every readout's sense, branch and decimals; every tour state is a declared preset; animations name real params and reachable values.
3. Check every claim a beat, caption, readout template or design rule makes, at its rung: conditions on general statements, sense and branch, frames and observers, and the first what-ifs. Check each beat's check address exists in the served note and really is evidenced by that beat's prediction or action. Check design rules against the served notes' misconceptions.
4. Try counterexample states (guide section 5, rule 10): the flat case, the boundary of each range, the largest region or strongest field allowed, both directions, and a degenerate path. Record them.
5. Check network links and that nothing mentions or reproduces the source books.
6. Fix errors with the simplest true wording and keep speech plain. Add review.physics with verdict, date "${DATE}", verification (claim, method, result for each equation, test and claim checked), counterexamples, fixes and concerns. With a verdict of accurate or fixed, set status "specified".
7. Run python3 ${T}/note_diff.py ${SNAP}/<id>.before-physics.json ${KB}/visuals/<id>.json. Count the changed strings among the ${LEARNER_TEXT}. If there are any, bump revision by exactly 1; the warning that review.novice covers an older revision is then expected, because a re-read follows. Set review.physics.reviewed_revision to the visual's revision. Fix every other warning, validate, render.
Return the summary object with errors_fixed and learner_changes per visual.`

const rereadPrompt = (g, ids, p) => `${CONTEXT}

TASK: You are the NOVICE READER doing a RE-READ of spoken and displayed text that the physics review changed. Visuals: ${ids.join(', ')}. The physics reviewer reported: ${JSON.stringify(p || {})}
For each visual:
1. Copy it to ${SNAP}/<id>.before-reread.json before editing.
2. Run python3 ${T}/note_diff.py ${SNAP}/<id>.before-physics.json ${KB}/visuals/<id>.json and read every changed string among the ${LEARNER_TEXT}, inside its beat or readout, with the persona of the novice read.
3. Record stumbles as {quote, problem, rewrite}. Fix wording only; never change a claim, number, sign or state. Put any other proposal in concerns.
4. Append {date "${DATE}", revision, read, stumbles, fixes} to review.novice.rereads. If you changed text, bump revision by exactly 1 first. Set review.novice.reviewed_revision to the visual's revision. If you edited, the warning that review.physics covers an older revision is expected, because a diff check follows. Validate, render.
Return the summary object with stumbles and edited per visual.`

const diffcheckPrompt = (g, ids, r) => `${CONTEXT}

TASK: You are the ADVERSARIAL PHYSICS REVIEWER doing a DIFF CHECK of wording the re-read changed. Visuals: ${ids.join(', ')}. The re-read reported: ${JSON.stringify(r || {})}
For each visual:
1. Run python3 ${T}/note_diff.py ${SNAP}/<id>.before-reread.json ${KB}/visuals/<id>.json.
2. Check that every changed line claims exactly what it did before, or something equally true at its rung, with its sense, branch, frame and conditions intact.
3. Fix errors with the simplest true wording. If you change text, bump revision by exactly 1 and list the changed lines in problems, because the novice stage will lag one revision.
4. Append {date "${DATE}", revision, verification, fixes} to review.physics.diff_checks and set review.physics.reviewed_revision to the visual's revision. Validate, render.
Return the summary object with edited per visual.`

const byId = (r) => (r && Array.isArray(r.visuals) ? r.visuals : [])
async function runGroup(g) {
  const tag = g.map((x) => x.id).join('+')
  const out = { ids: g.map((x) => x.id), stopped: null }
  out.write = await slot(2, () => agent(writePrompt(g), { label: `write:${tag}`, phase: 'Write', schema: DONE_SCHEMA }))
  if (!out.write) return ((out.stopped = 'write'), out)
  out.novice = await slot(3, () => agent(novicePrompt(g, out.write), { label: `novice:${tag}`, phase: 'Novice read', schema: DONE_SCHEMA, effort: 'high' }))
  if (!out.novice) return ((out.stopped = 'novice read'), out)
  out.physics = await slot(4, () => agent(physicsPrompt(g, out.novice), { label: `physics:${tag}`, phase: 'Physics review', schema: DONE_SCHEMA, effort: 'high' }))
  if (!out.physics) return ((out.stopped = 'physics review'), out)
  const rereadIds = byId(out.physics).filter((x) => (x.learner_changes || 0) > 0).map((x) => x.id)
  if (rereadIds.length) {
    out.reread = await slot(5, () => agent(rereadPrompt(g, rereadIds, out.physics), { label: `reread:${tag}`, phase: 'Re-read', schema: DONE_SCHEMA, effort: 'high' }))
    if (!out.reread) return ((out.stopped = 're-read'), out)
  }
  const checkIds = byId(out.reread).filter((x) => x.edited).map((x) => x.id)
  if (checkIds.length) {
    out.diffcheck = await slot(6, () => agent(diffcheckPrompt(g, checkIds, out.reread), { label: `diffcheck:${tag}`, phase: 'Diff check', schema: DONE_SCHEMA, effort: 'high' }))
    if (!out.diffcheck) return ((out.stopped = 'diff check'), out)
  }
  return out
}

const results = await pipeline(groups, (g) => runGroup(g))
const done = results.filter(Boolean)
const problems = (stage) => done.flatMap((r) => ((r[stage] && r[stage].problems) || []).map((m) => `${stage}: ${m}`))
return {
  planned: planned.map((x) => x.id),
  plan_problems: (plan && plan.problems) || [],
  finished: done.filter((r) => !r.stopped).flatMap((r) => r.ids),
  stopped: [...done.filter((r) => r.stopped).map((r) => `${r.ids.join('+')}: stopped at ${r.stopped}`), ...groups.map((g, i) => (results[i] ? null : `${g.map((x) => x.id).join('+')}: crashed`)).filter(Boolean)],
  lagging_novice: done.flatMap((r) => byId(r.diffcheck).filter((x) => x.edited).map((x) => x.id)),
  stages: done.flatMap((r) => ['write', 'novice', 'physics', 'reread', 'diffcheck'].flatMap((s) => byId(r[s]).map((x) => ({ stage: s, ...x })))),
  problems: [...problems('write'), ...problems('novice'), ...problems('physics'), ...problems('reread'), ...problems('diffcheck')],
}
