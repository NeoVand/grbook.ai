export const meta = {
  name: 'gr-concept-notes-v2',
  description: 'Write concept notes on the depth ladder, then a novice review, an adversarial physics review, and re-checks of any text changed afterwards (max 5 agents in flight)',
  phases: [
    { title: 'Conform', detail: 'bring an existing note up to the current standard (mode conform)' },
    { title: 'Write', detail: 'one agent per batch writes schema v2 notes from the evidence' },
    { title: 'Novice review', detail: 'a beginner-reader reviewer records a retelling and stumbles, then fixes the entry rung and the ladder' },
    { title: 'Physics review', detail: 'an adversarial physicist re-derives, recomputes, tries counterexamples, verifies references, and fixes' },
    { title: 'Re-read', detail: 'the novice reader reads text changed after the novice review' },
    { title: 'Diff check', detail: 'the physicist checks text changed after the physics review' },
  ],
}

const ROOT = '/Users/neo/repos/grbook.ai'
const KB = `${ROOT}/knowledge`
const T = `${KB}/_tools`
const batches = (args && args.batches) || []
const DATE = (args && args.date) || 'unknown-date'
// mode "write" (default): write, novice, physics, then re-checks. "review_only": the note exists; skip the writer.
// "conform": bring reviewed notes up to a changed standard: conform edit (when batch.conform), full novice re-read, diff check against base_rev.
const MODE = (args && args.mode) || (args && args.review_only ? 'review_only' : 'write')
const SNAP = args && args.snap_dir
const BASE = (args && args.base_rev) || 'HEAD'
if (!['write', 'review_only', 'conform'].includes(MODE)) throw new Error(`unknown mode "${MODE}"`)
if (!SNAP) throw new Error('args.snap_dir is required: a directory outside the repository for note snapshots')
log(`Run "${(args && args.name) || 'unnamed'}" (${MODE}): ${batches.length} batches, ${batches.reduce((n, b) => n + b.ids.length, 0)} concepts, date ${DATE}`)

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
- Writing guide: ${KB}/_meta/writing-guide.md. It covers: books as teachers only; who sees each field; the depth ladder; the novice contract; the accuracy contract; text formats; ids and addresses; field rules and the lifecycle; length budgets; visuals; reviews.
- Schema: ${KB}/_schemas/concept-note.schema.json
- Course conventions: ${KB}/notation/course-conventions.md. If a note needs a choice this file does not make, report it in your summary instead of inventing one.
- Exemplar note: ${KB}/concepts/curvature/holonomy.json. It sets the bar, especially its entry ways, checks, and the ids linking objectives, checks, and misconceptions.
- Exemplar visual: ${KB}/visuals/carry-an-arrow-around-a-loop.json

BUDGETS: caps are ceilings, not targets (guide section 9). Never compress sentences to fit a cap. When a fix needs words and a part is at its cap, drop or shorten the lowest-value item and say which in your fixes.

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
- Changed text: python3 ${T}/note_diff.py <before.json> <after.json> [--rungs entry,working], or python3 ${T}/note_diff.py --git <rev> <note.json>. It prints the learner-visible sentences that differ, tagged by rung.
- Snapshots: ${SNAP} (run mkdir -p first). Copy a note there before your stage edits it when your task says so.
- Validate: python3 ${T}/validate.py concept ${KB}/concepts/<domain>/<ID>.json. Fix every error and warning unless your task names a warning as expected; "note:" lines are information.
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
        properties: {
          id: { type: 'string' },
          verdict: { enum: ['accurate', 'fixed', 'needs-attention'] },
          validator: { enum: ['OK', 'WARNINGS', 'ERRORS'] },
          stumbles: { type: 'integer' },
          errors_fixed: { type: 'integer' },
          learner_changes: { type: 'integer', description: 'Physics review: learner-visible strings that note_diff.py lists as changed at entry or working rung' },
          edited: { type: 'boolean', description: 'True if this stage changed learner-visible text' },
        },
      },
    },
    major_issues: { type: 'array', items: { type: 'string' } },
  },
}

const note = (b) => `${KB}/concepts/${b.domain}/<ID>.json`

const writePrompt = (b) => `${CONTEXT}

TASK: Write schema v2 concept notes for domain "${b.domain}", in this order (learning order): ${b.ids.join(', ')}.
For each id:
1. Print the registry entry and run concept_evidence.py; read all of the evidence. Read the notes of the concept's prerequisites if they exist. If a file already exists at ${note(b)} without "schema_version": 2, treat it as an older book-centred draft: mine it for content, but rebuild the note completely.
2. Plan before writing. Answer each of these:
   - What concrete situation opens the entry rung?
   - Which distinct ways in exist, of at least two kinds, each answering its own question? Each entry way carries one idea (novice contract rule 17).
   - What can a learner do at each rung (the objectives)?
   - Which checks and problems prove it?
   - Which misconceptions do learners really have, and which check exposes each one?
   - Which real observations connect the concept to the world?
   - Which visuals serve it? Search visual_ids.py first.
   - What does the formal rung need for a graduate student: precise definitions, hypotheses, results with proof sketches, limits of validity? Tiers that require a formal rung need at least two formal checks and one formal problem.
   - Which research connections are real, and for which are you certain of the references?
3. Write ${note(b)} following the guide exactly:
   - the novice contract on every entry-rung field (section 2 of the guide lists them);
   - the accuracy contract everywhere;
   - text formats per field;
   - permanent ids, linked by id;
   - length budgets: a draft stays within 80% of every cap, which the validator checks. Write what each rung needs and stop.
   Set status "draft", revision 1, and updated "${DATE}". Every reference gets "verified": false.
4. Derive every equation in course conventions. Compute every number with python3. Work every check, example, and problem to its final answer. Try the first what-ifs (guide section 4, rule 13) and the counterexamples (section 5, rule 10) against every general sentence.
5. Validate and fix until OK. Render.
Return the summary object.`

const novicePrompt = (b, w) => `${CONTEXT}

TASK: You are the NOVICE-READER REVIEWER (writing guide section 11, review 1) for domain "${b.domain}": ${b.ids.join(', ')}. The previous stage reported: ${JSON.stringify(w || {})}
For each note ${note(b)}:
1. Adopt the persona strictly. You are a curious 16-year-old with school algebra and geometry, no calculus, and no physics beyond everyday experience. You know only the entry rungs of this concept's prerequisites; read those notes' entry ways if they exist.
2. Read only what an entry reader meets, sentence by sentence: the summary and tagline, then every field of each entry way, the glossary, entry objectives, entry checks, entry misconceptions, entry analogies, entry problems, entry observations, opening questions, and entry common questions.
3. BEFORE changing anything, write retell_attempt: what this reader would say back after one reading. Compare it with each entry way's takeaway.
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
   - a missing everyday number;
   - a way that asks you to hold two new ideas at once (rule 17): give the second idea its own entry way, or move it to the working rung;
   - wording squeezed to fit a budget.
5. Rewrite the JSON until the novice contract holds. Keep the physics exactly right. If a simpler wording might become false, keep the precise statement and add a sentence that explains it. Never compress other sentences to make room.
6. Read as a stronger student climbing the ladder.
   - Each non-entry way's first sentence refers back to the way it continues.
   - No idea, symbol, or notation is used before its rung allows it; index notation at working requires the index-notation prerequisite.
   - Add bridges wherever there is a jump.
   Check that the ways in are genuinely different routes.
7. If you changed learner-visible text, bump revision by exactly 1. Set status "novice-reviewed". Add review.novice with verdict, date "${DATE}", reviewed_revision (the note's revision), retell_attempt, stumbles, fixes, and concerns. Do not touch review.physics. Validate until OK, then render.
Return the summary object, with stumbles counted per note.`

const physicsPrompt = (b, n) => `${CONTEXT}

TASK: You are the ADVERSARIAL PHYSICS REVIEWER (writing guide section 11, review 2): a meticulous GR physicist and differential geometer acting as a referee. Domain "${b.domain}": ${b.ids.join(', ')}. The novice reviewer reported: ${JSON.stringify(n || {})}
For each note ${note(b)}:
0. Before editing, run mkdir -p ${SNAP} and copy the note to ${SNAP}/<ID>.before-physics.json.
1. Validate it.
2. Re-derive every key equation and every derivation step in course conventions. Check signs (signature, Riemann, Ricci, Einstein equation, gauge coupling), index placement, factors of 2 and pi, and the G, c, and hbar factors in SI results.
3. Recompute every number with python3. Work every check, worked example, and problem to its final answer, and check each numeric field and tolerance.
4. Check the conditions of every universal sentence at every rung, including the friendly entry sentences and the novice reviewer's rewrites. Check the sense and branch of every angle, phase, or rotation. Check every "equals" and "differs by" claim, and every analogy that relates quantities, with signs, numerically where possible. A false simplification becomes an equally simple true sentence, never a jargon-heavy one.
5. Try the standard counterexamples of the domain against each general statement (guide section 5, rule 10), and record them.
6. Verify every reference (authors, year, title, venue, doi or arxiv) with WebSearch or another reliable record. Set "verified": true only when confirmed. Correct details you can confirm. Remove references you cannot confirm. Check history claims for scope: what exactly was first, and in what setting.
7. Check structure:
   - Prerequisites are direct and acyclic, and assumes and justified_by are consistent.
   - The formal rung is graduate level, with at least two formal checks and one formal problem where the tier requires a formal rung; the research rung and horizon are accurate and current.
   - Observations are real, with correct numbers.
   - Visual ids and presets exist or are proposed with sketches.
   - Nothing mentions or copies the source books.
8. Set status "physics-reviewed" (only with a verdict of accurate or fixed). Add review.physics with verdict, date "${DATE}", verification (claim, method, result for each equation, number, analogy relation, and reference checked), counterexamples, fixes, and concerns.
9. Run python3 ${T}/note_diff.py ${SNAP}/<ID>.before-physics.json ${note(b)} --rungs entry,working. If it lists any change, bump revision by exactly 1. Set review.physics.reviewed_revision to the note's revision. A novice re-read of exactly those changes follows, so the one warning that review.novice covers an older revision is expected; fix every other warning. Render.
Return the summary object, with errors_fixed per note and learner_changes = the number of changed strings note_diff.py listed (0 if none).`

const conformPrompt = (b) => `${CONTEXT}

TASK: You are an EDITOR with a GR physicist's standards, bringing reviewed notes up to a changed standard. Domain "${b.domain}": ${b.ids.join(', ')}.
What changed: tiers that require a formal rung now need at least two formal checks and one formal problem; formal way minimums are foundation 300 and core, advanced and frontier 400 words; drafts keep budget headroom (not your concern: these notes are reviewed); and novice contract rule 17 (one idea per entry way) is new, which a re-read handles after you.
For each note ${note(b)}:
1. Validate it and read the guide sections that its warnings name.
2. Fix every warning except warnings about review revisions. Add real graduate-level substance, never padding: a precise definition, hypotheses, a result with a proof sketch, limits of validity, or a standard computation. New checks and problems evidence an objective at their own rung (add a formal objective when needed), follow the check and problem rules, give numeric answers where they apply, and target real misconceptions. Derive every equation in course conventions and compute every number with python3. Stay within every cap; if a part is full, drop or shorten the lowest-value item.
3. Do not edit entry-rung text unless a warning requires it.
4. If you changed learner-visible text, bump revision by exactly 1. Keep the status. Do not edit review. The warnings that review.novice and review.physics cover an older revision are expected, because a re-read and a physics diff check follow. Render.
Return the summary object with verdict "fixed" when you edited and "accurate" otherwise, edited per note, and major_issues listing exactly what you added or changed.`

const rereadPrompt = (b, ids, prior) => `${CONTEXT}

TASK: You are the NOVICE-READER REVIEWER doing a RE-READ (writing guide section 8, lifecycle step 5) for domain "${b.domain}": ${ids.join(', ')}. The previous stage reported: ${JSON.stringify(prior || {})}
For each note ${note(b)}:
1. Run mkdir -p ${SNAP} and copy the note to ${SNAP}/<ID>.before-reread.json before editing.
2. Adopt the novice persona strictly: a curious 16-year-old with school algebra and geometry, no calculus, and no physics beyond everyday experience, who knows only the entry rungs of the prerequisites. For working-rung text, read as a strong second-year undergraduate climbing the ladder.
3. Scope:
${
  MODE === 'conform'
    ? `   - This note's entry text was edited by its physics review without a novice re-read. Read the whole entry rung again, sentence by sentence, exactly as the novice review does (guide section 11): summary and tagline, every field of each entry way, glossary, entry objectives, checks, misconceptions, analogies, problems and observations, opening questions and entry common questions.
   - Then run python3 ${T}/note_diff.py --git ${BASE} ${note(b)} and read every change the conform stage made at entry and working rung.`
    : `   - Run python3 ${T}/note_diff.py ${SNAP}/<ID>.before-physics.json ${note(b)} --rungs entry,working. Read each changed sentence inside its paragraph and field. Read nothing else closely.`
}
4. Record every stumble as {quote, problem, rewrite}, using the novice review's stumble list, including a way that asks the reader to hold two new ideas at once (rule 17) and wording squeezed to fit a budget.
5. Fix wording only. Never change what a sentence claims: its numbers, conditions, scope, signs, or sense. ${
  MODE === 'conform'
    ? 'You may split an overloaded entry way into two entry ways, or move its second idea into a working way, as long as every sentence keeps its claim and the ids, questions, takeaways and continues links stay valid. '
    : ''
}If clarity needs a different claim, leave the sentence and describe the proposal in major_issues. Never compress other sentences to make room; drop or shorten the lowest-value item instead and say which.
6. Append {date "${DATE}", revision, read (the note_diff paths or field paths you read), stumbles, fixes} to review.novice.rereads. If you changed learner-visible text, bump revision by exactly 1 first. Set that entry's revision and review.novice.reviewed_revision to the note's revision. Keep the status. If you edited, the warning that review.physics covers an older revision is expected, because a physics diff check follows; fix every other warning. Render.
Return the summary object with, per note, verdict ("fixed" if you edited, else "accurate"), stumbles, and edited.`

const diffcheckPrompt = (b, ids, prior) => `${CONTEXT}

TASK: You are the ADVERSARIAL PHYSICS REVIEWER doing a DIFF CHECK (writing guide section 8, lifecycle step 5) for domain "${b.domain}": ${ids.join(', ')}. The previous stage reported: ${JSON.stringify(prior || {})}
For each note ${note(b)}:
1. List the changes: ${
  MODE === 'conform'
    ? `python3 ${T}/note_diff.py --git ${BASE} ${note(b)}. This covers the conform editor's additions and the re-read's rewording.`
    : `python3 ${T}/note_diff.py ${SNAP}/<ID>.before-reread.json ${note(b)}.`
}
2. Check every changed or added sentence in context, as the physics review does: true within its stated scope at its rung; conditions on universal sentences; sense and branch; frames, observers and measurers; consistent with the rest of the note and with course conventions. Try the first what-ifs and the domain's standard counterexamples on every changed general sentence. A reworded sentence must claim exactly what the old one did, or something equally true.
3. For every new or changed equation, derivation, check, problem, worked example or observation: re-derive it in course conventions, recompute with python3, work it to its final answer, and check numeric fields and tolerances. Verify any new reference with WebSearch before setting verified true.
4. Fix errors with the simplest true wording. Never compress other sentences to make room.
5. If you changed learner-visible text, bump revision by exactly 1 and list in major_issues exactly which sentences you changed, because the novice stage will then lag one revision. Append {date "${DATE}", revision, verification (claim, method, result for each item checked), fixes} to review.physics.diff_checks. Set review.physics.reviewed_revision to the note's revision. Validate until OK (apart from the novice-revision warning if you edited), then render.
Return the summary object with, per note, verdict, errors_fixed, and edited.`

// Each concept's novice review releases the batches that list it in "after", so pictures and terms connect.
const noviceDone = {}
const release = {}
for (const b of batches) for (const id of b.ids) noviceDone[id] = new Promise((resolve) => (release[id] = resolve))
const items = (r) => (r && Array.isArray(r.reviewed) ? r.reviewed : [])

async function runBatch(b) {
  const tag = `${b.domain}:${b.ids.join('+')}`
  const out = { domain: b.domain, ids: b.ids, stopped: null }
  try {
    const deps = (b.after || []).filter((id) => noviceDone[id] && !b.ids.includes(id))
    if (deps.length) await Promise.all(deps.map((id) => noviceDone[id]))
    let prior = null
    if (MODE === 'write') {
      out.write = await slot(1, () => agent(writePrompt(b), { label: `write:${tag}`, phase: 'Write', schema: WRITE_SCHEMA }))
      if (!out.write) return ((out.stopped = 'write'), out)
      prior = out.write
    }
    if (MODE === 'conform' && b.conform) {
      out.conform = await slot(1, () => agent(conformPrompt(b), { label: `conform:${tag}`, phase: 'Conform', schema: REVIEW_SCHEMA, effort: 'high' }))
      if (!out.conform) return ((out.stopped = 'conform'), out)
      prior = out.conform
    }
    let rereadIds = b.ids
    if (MODE !== 'conform') {
      out.novice = await slot(2, () => agent(novicePrompt(b, prior), { label: `novice:${tag}`, phase: 'Novice review', schema: REVIEW_SCHEMA, effort: 'high' }))
      b.ids.forEach((id) => release[id]())
      if (!out.novice) return ((out.stopped = 'novice'), out)
      out.physics = await slot(3, () => agent(physicsPrompt(b, out.novice), { label: `physics:${tag}`, phase: 'Physics review', schema: REVIEW_SCHEMA, effort: 'high' }))
      if (!out.physics) return ((out.stopped = 'physics'), out)
      prior = out.physics
      rereadIds = items(out.physics).filter((x) => (x.learner_changes || 0) > 0).map((x) => x.id)
    }
    if (rereadIds.length) {
      out.reread = await slot(4, () => agent(rereadPrompt(b, rereadIds, prior), { label: `reread:${tag}`, phase: 'Re-read', schema: REVIEW_SCHEMA, effort: 'high' }))
      if (!out.reread) return ((out.stopped = 're-read'), out)
    }
    const checkIds = new Set(items(out.reread).filter((x) => x.edited).map((x) => x.id))
    if (MODE === 'conform' && out.conform) items(out.conform).filter((x) => x.edited).forEach((x) => checkIds.add(x.id))
    if (checkIds.size) {
      out.diffcheck = await slot(5, () =>
        agent(diffcheckPrompt(b, [...checkIds], { conform: out.conform || null, reread: out.reread || null }), { label: `diffcheck:${tag}`, phase: 'Diff check', schema: REVIEW_SCHEMA, effort: 'high' }),
      )
      if (!out.diffcheck) return ((out.stopped = 'diff check'), out)
    }
    return out
  } finally {
    b.ids.forEach((id) => release[id]())
  }
}

const results = await pipeline(batches, (b) => runBatch(b))
const done = results.filter(Boolean)
const stopped = [
  ...done.filter((r) => r.stopped).map((r) => `${r.domain}/${r.ids.join('+')}: stopped at ${r.stopped}`),
  ...batches.map((b, i) => (results[i] ? null : `${b.domain}/${b.ids.join('+')}: crashed`)).filter(Boolean),
]
if (stopped.length) log(`Unfinished: ${stopped.join(' | ')}`)
const tagged = (stage, key) => done.flatMap((r) => items(r[stage]).map((x) => ({ domain: r.domain, stage: key, ...x })))
const issues = (stage) => done.flatMap((r) => ((r[stage] && r[stage].major_issues) || []).map((m) => `${r.domain}: ${m}`))
return {
  mode: MODE,
  finished: done.filter((r) => !r.stopped).flatMap((r) => r.ids),
  stopped,
  lagging_novice: done.flatMap((r) => items(r.diffcheck).filter((x) => x.edited).map((x) => `${r.domain}/${x.id}`)),
  stages: [...tagged('conform', 'conform'), ...tagged('novice', 'novice'), ...tagged('physics', 'physics'), ...tagged('reread', 're-read'), ...tagged('diffcheck', 'diff check')],
  writer_problems: done.flatMap((r) => ((r.write && r.write.problems) || []).map((m) => `${r.domain}: ${m}`)),
  conform_issues: issues('conform'),
  novice_issues: issues('novice'),
  physics_issues: issues('physics'),
  reread_issues: issues('reread'),
  diffcheck_issues: issues('diffcheck'),
}
