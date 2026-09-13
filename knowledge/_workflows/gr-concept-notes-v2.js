export const meta = {
  name: 'gr-concept-notes-v2',
  description: 'Write concept notes on the depth ladder, then a novice-reader review and an adversarial physics review (max 5 agents in flight)',
  phases: [
    { title: 'Write', detail: 'one agent per batch writes schema v2 notes from the evidence' },
    { title: 'Novice review', detail: 'a beginner-reader reviewer records a retelling and stumbles, then fixes the entry rung and the ladder' },
    { title: 'Physics review', detail: 'an adversarial physicist re-derives, recomputes, tries counterexamples, verifies references, and fixes' },
  ],
}

const ROOT = '/Users/neo/repos/grbook.ai'
const KB = `${ROOT}/knowledge`
const T = `${KB}/_tools`
const batches = (args && args.batches) || []
const DATE = (args && args.date) || 'unknown-date'
log(`Run "${(args && args.name) || 'unnamed'}": ${batches.length} batches, ${batches.reduce((n, b) => n + b.ids.length, 0)} concepts, date ${DATE}`)

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

const CONTEXT = `CONTEXT: grbook.ai is a general relativity book and interactive learning experience with a live voice AI tutor, narration, and 2D/3D demos, for learners from zero to research level. Its knowledge vault (${KB}) holds one concept note per registry concept plus a network of visuals. The tutor teaches from these notes live, and authors write the book from them, so every sentence must be understandable at its rung and every statement must be correct. Today's date: ${DATE}.

BINDING DOCUMENTS (read them completely before starting; re-read the relevant section whenever a validator warning surprises you):
- Writing guide: ${KB}/_meta/writing-guide.md. It covers: books as teachers only; who sees each field; the depth ladder; the novice contract; the accuracy contract; text formats; ids and addresses; field rules; length budgets; visuals; reviews.
- Schema: ${KB}/_schemas/concept-note.schema.json
- Course conventions: ${KB}/notation/course-conventions.md. If a note needs a choice this file does not make, report it in your summary instead of inventing one.
- Exemplar note: ${KB}/concepts/curvature/holonomy.json. It sets the bar, especially its entry ways, checks, and the ids linking objectives, checks, and misconceptions.
- Exemplar visual: ${KB}/visuals/carry-an-arrow-around-a-loop.json

TOOLS:
- Registry entry: python3 -c "import json,glob; [print(json.dumps(c, indent=1)) for f in glob.glob('${KB}/concepts/*/_registry.json') for c in json.load(open(f))['concepts'] if c['id']=='<ID>']"
- Study evidence: python3 ${T}/concept_evidence.py --id <ID>. These are internal notes on how three textbooks and the author's earlier course teach the idea, with book locators. Learn from them; never mention or copy them.
- More detail when needed:
  - dossiers: ${KB}/sources/<book>/chapters/<unit>.json
  - source reading copies, for checking an equation or argument: ${ROOT}/book-sources/_chapters/<book>/<unit>.md
  - legacy assets: ${KB}/sources/legacy/*.json
- Notes already written: ${KB}/concepts/<domain>/<id>.json. Read the prerequisites' notes when they exist, so glossaries, pictures, and ladders connect.
- Visuals: python3 ${T}/visual_ids.py [--grep <word>] lists catalog ids with their presets and proposed ids. Reuse an id before inventing one. Use a preset only if the catalog entry declares it.
- Numbers: python3 (sympy is not installed; use plain python or careful hand algebra).
- Validate: python3 ${T}/validate.py concept ${KB}/concepts/<domain>/<ID>.json. Fix every error and warning; "note:" lines are information.
- Render: python3 ${T}/render_concept.py ${KB}/concepts/<domain>/<ID>.json`

const WRITE_SCHEMA = {
  type: 'object',
  required: ['written', 'problems'],
  properties: {
    written: {
      type: 'array',
      items: { type: 'object', required: ['id', 'validator'], properties: { id: { type: 'string' }, validator: { enum: ['OK', 'WARNINGS', 'ERRORS'] }, words: { type: 'integer' } } },
    },
    problems: { type: 'array', items: { type: 'string' }, description: 'Anything unresolved, including missing conventions' },
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
        properties: { id: { type: 'string' }, verdict: { enum: ['accurate', 'fixed', 'needs-attention'] }, validator: { enum: ['OK', 'WARNINGS', 'ERRORS'] }, stumbles: { type: 'integer' }, errors_fixed: { type: 'integer' } },
      },
    },
    major_issues: { type: 'array', items: { type: 'string' } },
  },
}

const writePrompt = (b) => `${CONTEXT}

TASK: Write schema v2 concept notes for domain "${b.domain}", in this order (learning order): ${b.ids.join(', ')}.
For each id:
1. Print the registry entry and run concept_evidence.py; read all of the evidence. Read the notes of the concept's prerequisites if they exist. If a file already exists at ${KB}/concepts/${b.domain}/<ID>.json without "schema_version": 2, treat it as an older book-centred draft: mine it for content, but rebuild the note completely.
2. Plan before writing. Answer each of these:
   - What concrete situation opens the entry rung?
   - Which distinct ways in exist, of at least two kinds, each answering its own question?
   - What can a learner do at each rung (the objectives)?
   - Which checks and problems prove it?
   - Which misconceptions do learners really have, and which check exposes each one?
   - Which real observations connect the concept to the world?
   - Which visuals serve it? Search visual_ids.py first.
   - What does the formal rung need for a graduate student?
   - Which research connections are real, and for which are you certain of the references?
3. Write ${KB}/concepts/${b.domain}/<ID>.json following the guide exactly:
   - the novice contract on every entry-rung field (section 2 of the guide lists them);
   - the accuracy contract everywhere;
   - text formats per field;
   - permanent ids, linked by id;
   - length budgets.
   Set status "draft", revision 1, and updated "${DATE}". Every reference gets "verified": false.
4. Derive every equation in course conventions. Compute every number with python3. Work every check, example, and problem to its final answer. Try the first what-ifs (guide section 4, rule 12) and the counterexamples (section 5, rule 9) against every general sentence.
5. Validate and fix until OK. Render.
Return the summary object.`

const novicePrompt = (b, w) => `${CONTEXT}

TASK: You are the NOVICE-READER REVIEWER (writing guide section 11, review 1) for domain "${b.domain}": ${b.ids.join(', ')}. The writer reported: ${JSON.stringify(w || {})}
For each note ${KB}/concepts/${b.domain}/<ID>.json:
1. Adopt the persona strictly. You are a curious 16-year-old with school algebra and geometry, no calculus, and no physics beyond everyday experience. You know only the entry rungs of this concept's prerequisites; read those notes' entry ways if they exist.
2. Read only what an entry reader meets, sentence by sentence: the summary and tagline, then every field of each entry way, the glossary, entry objectives, entry checks, entry misconceptions, entry analogies, entry problems, entry observations, opening questions, and entry common questions.
3. BEFORE changing anything, write retell_attempt: what this reader would say back after one reading. Compare it with each entry way's retell.
4. Record every stumble as {quote, problem, rewrite}. Stumbles include:
   - a sentence you had to reread;
   - an undefined or unfamiliar word;
   - two words used for one idea, or one word used for two;
   - a step left implicit;
   - an ambiguous "it" or "this";
   - a direction without a reference, such as whose left, seen from where, or a compass word near a pole;
   - a rule the reader could not physically follow;
   - a surprising claim with no reason or try-it test;
   - a general sentence that fails for the first what-if a teenager would try;
   - a check whose starting state is ambiguous or that the entry ways do not prepare for;
   - a missing everyday number.
5. Rewrite the JSON until the novice contract holds. Keep the physics exactly right. If a simpler wording might become false, keep the precise statement and add a sentence that explains it.
6. Read as a stronger student climbing the ladder.
   - Each non-entry way's first sentence refers back to the way it continues.
   - No idea, symbol, or notation is used before its rung allows it; index notation at working requires the index-notation prerequisite.
   - Add bridges wherever there is a jump.
   Check that the ways in are genuinely different routes.
7. Set status "novice-reviewed". Add review.novice with verdict, date "${DATE}", retell_attempt, stumbles, fixes, and concerns. Do not touch review.physics. Validate until OK, then render.
Return the summary object, with stumbles counted per note.`

const physicsPrompt = (b, n) => `${CONTEXT}

TASK: You are the ADVERSARIAL PHYSICS REVIEWER (writing guide section 11, review 2): a meticulous GR physicist and differential geometer acting as a referee. Domain "${b.domain}": ${b.ids.join(', ')}. The novice reviewer reported: ${JSON.stringify(n || {})}
For each note ${KB}/concepts/${b.domain}/<ID>.json:
1. Validate it.
2. Re-derive every key equation and every derivation step in course conventions. Check signs (signature, Riemann, Ricci, Einstein equation, gauge coupling), index placement, factors of 2 and pi, and the G, c, and hbar factors in SI results.
3. Recompute every number with python3. Work every check, worked example, and problem to its final answer, and check each numeric field and tolerance.
4. Check the conditions of every universal sentence at every rung, including the friendly entry sentences and the novice reviewer's rewrites. Check the sense and branch of every angle, phase, or rotation. Check every "equals" and "differs by" claim, and every analogy that relates quantities, with signs, numerically where possible. A false simplification becomes an equally simple true sentence, never a jargon-heavy one.
5. Try the standard counterexamples of the domain against each general statement (guide section 5, rule 9), and record them.
6. Verify every reference (authors, year, title, venue, doi or arxiv) with WebSearch or another reliable record. Set "verified": true only when confirmed. Correct details you can confirm. Remove references you cannot confirm. Check history claims for scope: what exactly was first, and in what setting.
7. Check structure:
   - Prerequisites are direct and acyclic, and assumes and justified_by are consistent.
   - The formal rung is graduate level; the research rung and horizon are accurate and current.
   - Observations are real, with correct numbers.
   - Visual ids and presets exist or are proposed with sketches.
   - Nothing mentions or copies the source books.
8. Set status "physics-reviewed". Add review.physics with verdict, date "${DATE}", verification (claim, method, result for each equation, number, analogy relation, and reference checked), counterexamples, fixes, and concerns. Validate until OK, then render.
Return the summary object, with errors fixed counted per note.`

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
  novice: done.flatMap((r) => (r.novice?.reviewed ?? []).map((x) => ({ domain: r.domain, ...x }))),
  novice_issues: done.flatMap((r) => (r.novice?.major_issues ?? []).map((m) => `${r.domain}: ${m}`)),
  physics_issues: done.flatMap((r) => r.physics.major_issues.map((m) => `${r.domain}: ${m}`)),
  writer_problems: done.flatMap((r) => (r.write?.problems ?? []).map((m) => `${r.domain}: ${m}`)),
  failed,
}
