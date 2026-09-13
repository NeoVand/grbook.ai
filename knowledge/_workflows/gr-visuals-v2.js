export const meta = {
  name: 'gr-visuals-v2',
  description: 'Turn visuals proposed in a domain\'s concept notes into reviewed catalog entries in the visual network (max 5 agents in flight)',
  phases: [
    { title: 'Plan', detail: 'merge duplicate proposals, choose canonical picture ids, update note references' },
    { title: 'Write', detail: 'write catalog entries in groups' },
    { title: 'Review', detail: 'check models, tests, design rules, and spoken tour lines' },
  ],
}

const ROOT = '/Users/neo/repos/grbook.ai'
const KB = `${ROOT}/knowledge`
const T = `${KB}/_tools`
const domain = args && args.domain
const GROUP = (args && args.group_size) || 4
if (!domain) throw new Error('args.domain is required')

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

const CONTEXT = `CONTEXT: grbook.ai is a general relativity book and interactive learning experience with a live voice AI tutor and 2D/3D demos, for learners from zero to research level. Visuals (diagrams, widgets, animations, 3D demos) form their own network in ${KB}/visuals/<id>.json, linked to concepts and to each other. Developers will build them from these entries, and the tutor narrates their tours.

BINDING DOCUMENTS - read completely first: ${KB}/_meta/writing-guide.md (especially sections 1, 3, 4, 6), ${KB}/_schemas/visual.schema.json, ${KB}/notation/course-conventions.md, and the exemplar ${KB}/visuals/carry-an-arrow-around-a-loop.json.

TOOLS:
- Visual ids: python3 ${T}/visual_ids.py [--missing] [--domain <id>] [--grep <word>] [--json]
- Concept notes: ${KB}/concepts/<domain>/<id>.json; figure ideas from the textbook study: python3 ${T}/concept_evidence.py --id <concept> (section "Figures and redesign ideas", with image paths under ${ROOT}/book-sources/ that you may view for inspiration; never reproduce them)
- Earlier course assets (demos, labs, figures; reuse encouraged): ${KB}/sources/legacy/*.json
- Numbers: python3
- Validate: python3 ${T}/validate.py visual ${KB}/visuals/<id>.json ; notes: python3 ${T}/validate.py concept <note.json>
- Render: python3 ${T}/render_visual.py ${KB}/visuals/<id>.json ; index: python3 ${T}/render_visual.py --index ; notes: python3 ${T}/render_concept.py <note.json>`

const PLAN_SCHEMA = {
  type: 'object',
  required: ['visuals'],
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
  },
}
const DONE_SCHEMA = {
  type: 'object',
  required: ['visuals', 'problems'],
  properties: {
    visuals: { type: 'array', items: { type: 'object', required: ['id', 'validator'], properties: { id: { type: 'string' }, validator: { enum: ['OK', 'WARNINGS', 'ERRORS'] }, verdict: { type: 'string' } } } },
    problems: { type: 'array', items: { type: 'string' } },
  },
}

phase('Plan')
const plan = await slot(1, () =>
  agent(
    `${CONTEXT}

TASK: Plan the catalog entries for visuals proposed in domain "${domain}".
1. Run visual_ids.py --missing --domain ${domain}, and visual_ids.py for the whole catalog.
2. Group proposals that describe the same picture, even under different names, and match any proposal that an existing catalog entry already covers.
3. For each group, choose one canonical id that names the picture, not the concept, and decide kind and priority.
4. Edit every concept note in ${KB}/concepts/ that uses a non-canonical or already-covered id: change it to the canonical id, keep the most informative sketch, validate, and re-render.
5. Return the list of NEW catalog entries to write. For each, give the concepts it serves (across all domains) and the proposal ids it merges.`,
    { label: `plan:${domain}`, phase: 'Plan', schema: PLAN_SCHEMA, effort: 'high' },
  ),
)
const items = (plan && plan.visuals) || []
log(`${items.length} new visuals planned for ${domain}`)
const groups = []
for (let i = 0; i < items.length; i += GROUP) groups.push(items.slice(i, i + GROUP))

const results = await pipeline(
  groups,
  (g, _, i) =>
    slot(2, () =>
      agent(
        `${CONTEXT}

TASK: Write catalog entries for these planned visuals: ${JSON.stringify(g)}.
For each visual:
1. Read the notes of every concept it serves, including their sketches, misconceptions and entry ways. Read their figure evidence and any matching legacy assets.
2. Design the visual:
   - composition and a plain caption;
   - variants from a static card up;
   - interactions and presets;
   - a guided tour whose "say" lines obey the novice contract when the visual serves the entry rung;
   - design rules derived from the served concepts' misconceptions;
   - the physics or mathematical model, with equations in course conventions;
   - numerical test cases with expected values computed in python3.
3. Link it into the network (builds_on, leads_to, variant_of) using existing or planned ids. Add accessibility and starting material.
4. Write ${KB}/visuals/<id>.json. Validate until OK, then render.
Return the summary object.`,
        { label: `write:${domain}:${i}`, phase: 'Write', schema: DONE_SCHEMA },
      ),
    ),
  (w, g, i) =>
    slot(3, () =>
      agent(
        `${CONTEXT}

TASK: You are an independent reviewer: a GR physicist who also builds interactive demos. Review and fix these catalog entries: ${g.map((x) => x.id).join(', ')}. The writer reported: ${JSON.stringify(w || {})}
For each entry:
1. Re-derive every model equation and recompute every test expectation with python3.
2. Check that the design can actually be built, and that interactions and presets are specific.
3. Check that the design rules really prevent the served concepts' misconceptions.
4. Read the tour's "say" lines as a beginner: short sentences, no undefined words, no raw math.
5. Check that the caption and composition are accurate.
6. Check that the network links make sense.
7. Check that nothing mentions or reproduces the source books.
Fix what is wrong, set "review": {verdict, fixes, concerns}, validate until OK, and render. Finally run render_visual.py --index.
Return the summary object.`,
        { label: `review:${domain}:${i}`, phase: 'Review', schema: DONE_SCHEMA, effort: 'high' },
      ),
    ),
)
return { planned: items.map((x) => x.id), reviewed: results.filter(Boolean).flatMap((r) => r.visuals), problems: results.filter(Boolean).flatMap((r) => r.problems) }
