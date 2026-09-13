export const meta = {
  name: 'gr-concept-notes-v2',
  description: 'Write concept notes on the depth ladder, then a novice-reader review and an adversarial physics review (max 5 agents in flight)',
  phases: [
    { title: 'Write', detail: 'one agent per batch writes schema v2 notes from the evidence' },
    { title: 'Novice review', detail: 'a beginner-reader reviewer makes the entry rung explicit and the ladder continuous' },
    { title: 'Physics review', detail: 'an adversarial physicist re-derives, recomputes, verifies, and fixes' },
  ],
}

const ROOT = '/Users/neo/repos/grbook.ai'
const KB = `${ROOT}/knowledge`
const T = `${KB}/_tools`
const batches = (args && args.batches) || []
log(`Run "${(args && args.name) || 'unnamed'}": ${batches.length} batches, ${batches.reduce((n, b) => n + b.ids.length, 0)} concepts`)

// The owner's pacing rule: at most 5 agents in flight. Later stages get free slots first so notes finish end to end.
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

const CONTEXT = `CONTEXT: grbook.ai is a general relativity book and interactive learning experience with a live voice AI tutor, narration, and 2D/3D demos, for learners from zero to research level. Its knowledge vault (${KB}) holds one concept note per registry concept plus a network of visuals. The tutor teaches from these notes live, and authors write the book from them, so every sentence must be understandable at its rung and every statement must be correct.

BINDING DOCUMENTS - read completely before starting:
- Writing guide: ${KB}/_meta/writing-guide.md (the books are teachers, not the subject; the depth ladder; the novice contract; the accuracy contract; field-by-field rules; visuals; reviews)
- Schema: ${KB}/_schemas/concept-note.schema.json
- Course conventions: ${KB}/notation/course-conventions.md
- Exemplar note: ${KB}/concepts/curvature/holonomy.json (the quality bar, especially its entry ways)
- Exemplar visual: ${KB}/visuals/carry-an-arrow-around-a-loop.json

TOOLS:
- Registry entry: python3 -c "import json,glob; [print(json.dumps(c, indent=1)) for f in glob.glob('${KB}/concepts/*/_registry.json') for c in json.load(open(f))['concepts'] if c['id']=='<ID>']"
- Study evidence: python3 ${T}/concept_evidence.py --id <ID> (internal notes on how three textbooks and the author's earlier course teach the idea, with book locators; learn from it, never mention or copy it)
- Detail when needed: dossiers ${KB}/sources/<book>/chapters/<unit>.json; source reading copies ${ROOT}/book-sources/_chapters/<book>/<unit>.md (to check an equation or argument); legacy assets ${KB}/sources/legacy/*.json
- Notes already written: ${KB}/concepts/<domain>/<id>.json (read prerequisites' notes, when they exist, so glossaries, pictures, and ladders connect)
- Visuals: python3 ${T}/visual_ids.py [--grep <word>] (catalog and proposed ids; reuse before inventing)
- Numbers: python3 (sympy is not installed; use plain python or careful hand algebra)
- Validate: python3 ${T}/validate.py concept ${KB}/concepts/<domain>/<ID>.json (fix every error and warning; "note:" lines are information)
- Render: python3 ${T}/render_concept.py ${KB}/concepts/<domain>/<ID>.json`

const WRITE_SCHEMA = {
  type: 'object',
  required: ['written', 'problems'],
  properties: {
    written: {
      type: 'array',
      items: { type: 'object', required: ['id', 'validator'], properties: { id: { type: 'string' }, validator: { enum: ['OK', 'WARNINGS', 'ERRORS'] }, words: { type: 'integer' } } },
    },
    problems: { type: 'array', items: { type: 'string' } },
  },
}
const REVIEW_SCHEMA = {
  type: 'object',
  required: ['reviewed', 'major_issues'],
  properties: {
    reviewed: {
      type: 'array',
      items: {
        type: 'object',
        required: ['id', 'verdict', 'validator'],
        properties: { id: { type: 'string' }, verdict: { enum: ['accurate', 'fixed', 'needs-attention'] }, validator: { enum: ['OK', 'WARNINGS', 'ERRORS'] } },
      },
    },
    major_issues: { type: 'array', items: { type: 'string' } },
  },
}

const writePrompt = (b) => `${CONTEXT}

TASK: Write schema v2 concept notes for domain "${b.domain}", in this order (learning order): ${b.ids.join(', ')}.
For each id:
1. Print the registry entry and run concept_evidence.py. Read all of it. Read the notes of its prerequisites if they exist. If a file already exists at ${KB}/concepts/${b.domain}/<ID>.json without "schema_version": 2, it is an older book-centred draft whose physics was reviewed: mine it for content, but rebuild the note completely in the new shape and voice.
2. Plan before writing. What concrete situation opens the entry rung? What distinct ways in exist (picture, measurement, calculation, historical puzzle, bridge)? Which equations must a learner own? Which misconceptions do learners really have? Which visuals serve it (search visual_ids.py first)? What does the formal rung need for a graduate student, and what research connections are real?
3. Write ${KB}/concepts/${b.domain}/<ID>.json. Follow the writing guide exactly. The entry rung obeys the novice contract; each rung climbs from the one below.
4. Derive every equation in course conventions. Compute every number with python3. Work every answer.
5. Validate and fix until OK. Render.
Return the summary object.`

const novicePrompt = (b, w) => `${CONTEXT}

TASK: You are the NOVICE-READER REVIEWER (writing guide section 7, review 1) for domain "${b.domain}": ${b.ids.join(', ')}. The writer reported: ${JSON.stringify(w || {})}
For each note ${KB}/concepts/${b.domain}/<ID>.json:
1. Adopt the persona strictly. You are a curious 16-year-old with school algebra and geometry, no calculus, and no physics beyond everyday experience. You know only the entry rungs of this concept's prerequisites (read those notes' entry ways if they exist).
2. Read, sentence by sentence, everything this reader meets first:
   - the summary;
   - every entry way;
   - the glossary;
   - the entry-rung checks, misconceptions and analogies;
   - the tutor's opening questions, and the answers to common questions.
   Mark every stumble:
   - an undefined or unfamiliar word;
   - a step left implicit;
   - an ambiguous "it" or "this";
   - a direction or picture that is hard to imagine;
   - a claim given without a reason;
   - a sentence you had to reread;
   - a jump in difficulty.
3. Rewrite those passages in the JSON so the novice contract holds. Keep the physics exactly right. If a simpler wording might become false, keep the precise statement and add a sentence that explains it.
4. Now read as a stronger student climbing the ladder.
   - Does the first working way start from the entry picture?
   - Does the formal rung start from the working rung?
   - Is any idea or symbol used before it is introduced?
   Add bridging sentences wherever there is a jump.
5. Check that the ways in are genuinely different routes. Merge or replace any that repeat each other.
6. Add "review.novice": {verdict, fixes (each concrete), concerns}. Do not change review.physics if present. Validate until OK, then render.
Return the summary object.`

const physicsPrompt = (b, n) => `${CONTEXT}

TASK: You are the ADVERSARIAL PHYSICS REVIEWER (writing guide section 7, review 2): a meticulous GR physicist and differential geometer. Domain "${b.domain}": ${b.ids.join(', ')}. The novice reviewer reported: ${JSON.stringify(n || {})}
For each note ${KB}/concepts/${b.domain}/<ID>.json:
1. Validate it.
2. Re-derive every key equation and every derivation step yourself, in course conventions. Check signs (signature, Riemann, Ricci, Einstein equation), index placement, factors of 2 and pi, and the G and c factors in SI results. Recompute every number with python3. Work every check and worked example to its final answer and compare.
3. Check the conditions of every claim at every rung, including the friendly entry sentences. A simplification must be true within its stated scope. When one is false, replace it with an equally simple true sentence, never a jargon-heavy one.
4. Verify every history entry and research pointer: people, years and titles. Use WebSearch when you are not certain. Remove or trim anything you cannot verify.
5. Check the structure:
   - Prerequisites are direct, and none of them depends on this concept.
   - The formal rung is truly graduate level.
   - The research rung and research horizon are accurate and current.
   - Visual ids reuse existing or proposed ids where the picture is the same (visual_ids.py).
   - Nothing mentions or copies the source books.
6. Add "review.physics": {verdict: accurate | fixed | needs-attention, fixes (each concrete), concerns}. Validate until OK, then render.
Return the summary object.`

const results = await pipeline(
  batches,
  (b, _, i) => slot(1, () => agent(writePrompt(b), { label: `write:${b.domain}:${i}`, phase: 'Write', schema: WRITE_SCHEMA })),
  (w, b, i) => slot(2, () => agent(novicePrompt(b, w), { label: `novice:${b.domain}:${i}`, phase: 'Novice review', schema: REVIEW_SCHEMA, effort: 'high' })).then((n) => ({ w, n })),
  ({ w, n }, b, i) =>
    slot(3, () => agent(physicsPrompt(b, n), { label: `physics:${b.domain}:${i}`, phase: 'Physics review', schema: REVIEW_SCHEMA, effort: 'high' })).then((p) => ({
      domain: b.domain,
      ids: b.ids,
      write: w,
      novice: n,
      physics: p,
    })),
)
const failed = batches.filter((b, i) => !results[i] || !results[i].physics).map((b) => `${b.domain}: ${b.ids.join(', ')}`)
if (failed.length) log(`Batches without a finished physics review: ${failed.join(' | ')}`)
const done = results.filter((r) => r && r.physics)
return {
  reviewed: done.flatMap((r) => r.physics.reviewed.map((x) => ({ domain: r.domain, ...x }))),
  novice_issues: done.flatMap((r) => (r.novice?.major_issues ?? []).map((m) => `${r.domain}: ${m}`)),
  physics_issues: done.flatMap((r) => r.physics.major_issues.map((m) => `${r.domain}: ${m}`)),
  writer_problems: done.flatMap((r) => (r.write?.problems ?? []).map((m) => `${r.domain}: ${m}`)),
  failed,
}
