export const meta = {
  name: 'gr-concept-notes-batch',
  description: 'Write and adversarially review canonical concept notes for batches of registry concepts',
  phases: [
    { title: 'Write', detail: 'one agent per batch of concepts writes validated concept notes' },
    { title: 'Review', detail: 'independent physicist-educator checks and fixes each batch' },
  ],
}

const ROOT = '/Users/neo/repos/grbook.ai'
const KB = `${ROOT}/knowledge`
const T = `${KB}/_tools`
const batches = (args && args.batches) || []
log(`Batch set "${(args && args.name) || 'unnamed'}": ${batches.length} batches, ${batches.reduce((n, b) => n + b.ids.length, 0)} concepts`)

const CONTEXT = `CONTEXT: grbook.ai is an AI-centred general relativity course for learners of any starting level, with a live voice tutor and beautiful interactive 2D/3D demos. Its knowledge vault (${KB}) contains verified teaching dossiers for every unit of three textbooks (SCH = Schutz 3rd ed., GA = Blundell & Lancaster "Gifted Amateur", DIV = d'Inverno & Vickers 2nd ed.), book profiles (${KB}/sources/<book>/book-profile.md), an inventory of the user's earlier course (${KB}/sources/legacy/, which may be reused directly), and a canonical concept registry (${KB}/concepts/<domain>/_registry.json). Concept notes are the heart of the vault: the tutor retrieves them by id to teach step by step at the learner's level, diagnose misconceptions, choose analogies, and launch demos; authors use them to write lessons and build demos.

COURSE CONVENTIONS (binding): ${KB}/notation/course-conventions.md. Every equation in a concept note uses these conventions; when a book differs, record it in "conventions" and translate.

SOURCE POLICY (strict): we learn HOW to teach from the books; we never copy their wording. Every prose field is original. Equations may be transcribed (in course conventions). Summarize exercises; never transcribe them. The validator flags 12+ consecutive words matching any cited source unit. Legacy material is the user's own and may be reused, citing "legacy:<asset-id>".

TOOLS:
- Registry entry: python3 -c "import json,glob; [print(json.dumps(c, indent=1)) for f in glob.glob('${KB}/concepts/*/_registry.json') for c in json.load(open(f))['concepts'] if c['id']=='<ID>']"
- Evidence: python3 ${T}/concept_evidence.py --id <ID>   (definitions, equations, figures with redesign ideas, examples, analogies, misconceptions, thought experiments, gems, gaps, exercises, legacy assets across all sources)
- Dossiers for detail: ${KB}/sources/<book>/chapters/<unit>.json ; source reading copies for checking an equation or argument: ${ROOT}/book-sources/_chapters/<book>/<unit>.md
- Schema: ${KB}/_schemas/concept-note.schema.json
- Validate: python3 ${T}/validate.py concept ${KB}/concepts/<domain>/<ID>.json
- Render: python3 ${T}/render_concept.py ${KB}/concepts/<domain>/<ID>.json
REFERENCE FORMAT: "SCH ch05 §5.3 p.125", "GA ch11 Example 11.2", "DIV ch09 Fig. 9.5 p.160", or "legacy:<asset-id>".`

const QUALITY = `QUALITY BAR for each note:
- summary: 2-3 sentences a tutor could say aloud.
- levels: intuition = no equations, one vivid picture, everyday language, honest about what is simplified; working = the key relations with meaning, for a learner with calculus and some linear algebra; formal = precise definition, conditions, conventions. Each level stands alone and is correct.
- prerequisites / leads_to / related: registry ids only, with a one-line why. prerequisites are DIRECT and match the registry (you may improve them; keep them acyclic in spirit).
- key_equations: the equations a learner must know for this concept, in course conventions, each with meaning and refs.
- conventions: every place the books differ in sign, notation, index placement, or definition for this concept, with each book's choice and the course choice. Check the dossiers' notation entries; never guess.
- how_books_teach: one entry per source that treats it at depth introduced or deeper (and legacy when assets exist): the route, the representation, strengths, weaknesses, refs.
- recommended_teaching_path: 4-8 steps synthesizing the best moves across sources into our own order (motivating question -> picture -> formalism -> check -> application), each with why and inspired_by refs.
- analogies: the best ones from the sources plus your own, each with explicit limits and level.
- misconceptions: real, specific ones (from the dossiers, legacy pitfalls list in ${KB}/sources/legacy/overview.md §5.1, or well-known), each with a correction and a diagnostic question that exposes it.
- visualizations: 1-4 concrete ORIGINAL demo ideas (what the learner manipulates, what updates, the physics model), prioritized, citing inspiring figures and legacy assets by id.
- worked_examples and exercises: pointers to the best examples and exercises across sources with what each shows (summaries only).
- checks_for_understanding: at least 3, spanning levels, with correct worked answers; at least one targets a misconception.
- tutor_guidance: opening questions, common learner questions with answers, pitfalls when explaining, demo moments, voice_notes on saying the key equations aloud.
- sources: every book unit in the registry entry, with locators.
Frontier and advanced concepts may be more compact, but every required field must be substantive and correct.`

const WRITE_SCHEMA = {
  type: 'object',
  required: ['written', 'problems'],
  properties: {
    written: { type: 'array', items: { type: 'object', required: ['id', 'path', 'validator'], properties: { id: { type: 'string' }, path: { type: 'string' }, validator: { enum: ['OK', 'WARNINGS', 'ERRORS'] } } } },
    problems: { type: 'array', items: { type: 'string' } },
  },
}
const REVIEW_SCHEMA = {
  type: 'object',
  required: ['reviewed', 'major_issues'],
  properties: {
    reviewed: { type: 'array', items: { type: 'object', required: ['id', 'verdict', 'validator'], properties: { id: { type: 'string' }, verdict: { enum: ['accurate', 'fixed', 'needs-attention'] }, validator: { enum: ['OK', 'WARNINGS', 'ERRORS'] } } } },
    major_issues: { type: 'array', items: { type: 'string' } },
  },
}

function writePrompt(b) {
  return `${CONTEXT}

TASK: Write concept notes for these concepts of domain "${b.domain}": ${b.ids.join(', ')}.
For each id:
1. Print its registry entry and run concept_evidence.py --id <ID>. Read all the evidence. Open dossiers, legacy assets, and source reading copies wherever you need more detail or must check an equation, a convention, or a claim.
2. Write ${KB}/concepts/${b.domain}/<ID>.json satisfying the schema (read the schema once, fully).
3. Validate; fix every error and warning (copied wording, unknown ids, bad references); repeat until OK.
4. Render the markdown.
${QUALITY}
Return the summary object.`
}

function reviewPrompt(b, w) {
  return `${CONTEXT}

TASK: You are an independent, skeptical reviewer (GR physicist and experienced educator). Review and FIX the concept notes for domain "${b.domain}": ${b.ids.join(', ')}. Writer's report: ${JSON.stringify(w || {})}
For each note ${KB}/concepts/${b.domain}/<ID>.json:
1. Validate it. Re-run concept_evidence.py --id <ID> and compare: is the best teaching material from every source represented? Are refs accurate (spot-check at least 5 against the dossiers)?
2. Physics and math: check every definition, equation (course conventions!), convention entry, analogy limit, misconception correction, and the answers to checks_for_understanding (work them). Fix errors.
3. Pedagogy: are the three levels genuinely different depths and each correct on its own? Is the teaching path a real synthesis with a motivating question? Are demo ideas concrete and buildable? Are prerequisites direct and sensible? Replace generic content with specifics.
4. Wording: rewrite anything that tracks a source's text.
5. Add or replace "review": verdict (accurate | fixed | needs-attention), fixes, concerns. Validate until OK and re-render.
${QUALITY}
Return the summary object.`
}

const results = await pipeline(
  batches,
  (b, _, i) => agent(writePrompt(b), { label: `write:${b.domain}:${i}`, phase: 'Write', schema: WRITE_SCHEMA }),
  (w, b, i) => agent(reviewPrompt(b, w), { label: `review:${b.domain}:${i}`, phase: 'Review', schema: REVIEW_SCHEMA, effort: 'high' })
    .then((r) => ({ domain: b.domain, ids: b.ids, write: w, review: r })),
)
const failed = batches.filter((b, i) => !results[i]).map((b) => `${b.domain}: ${b.ids.join(', ')}`)
if (failed.length) log(`Batches without reviewed notes: ${failed.join(' | ')}`)
return {
  reviewed: results.filter(Boolean).flatMap((r) => r.review.reviewed.map((x) => ({ domain: r.domain, ...x }))),
  major_issues: results.filter(Boolean).flatMap((r) => r.review.major_issues.map((m) => `${r.domain}: ${m}`)),
  failed,
}
