export const meta = {
  name: 'gr-concept-notes-v2',
  description: 'Write concept notes on the depth ladder, then a novice review, an adversarial physics review, and one post-review check of any text changed afterwards (max 5 agents in flight)',
  phases: [
    { title: 'Conform', detail: 'bring an existing note up to the current standard, or apply editor items (mode conform)' },
    { title: 'Write', detail: 'one agent per batch writes schema v2 notes from the evidence' },
    { title: 'Novice review', detail: 'a beginner-reader reviewer records a retelling and stumbles, then fixes the entry rung and the ladder' },
    { title: 'Physics review', detail: 'an adversarial physicist re-derives, recomputes, tries counterexamples, verifies references, and fixes' },
    { title: 'Post-review check', detail: 'one agent reads the text changed after the reviews with the novice lens, then the physics lens, and signs' },
  ],
}

const ROOT = '/Users/neo/repos/grbook.ai'
const KB = `${ROOT}/knowledge`
const T = `${KB}/_tools`
const batches = (args && args.batches) || []
const DATE = (args && args.date) || 'unknown-date'
// mode "write" (default): write, novice, physics, then a post-review check when the physics review changed
// entry or working text. "review_only": the note exists; skip the writer. "conform": bring reviewed notes up to a
// changed standard or apply editor items. Batch fields: conform (run the editor), items (editor tasks),
// reread_scope ("full" entry rung, the default, or "changes"), reread_from (snapshot to diff from).
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

// Every agent's context is expensive: each tool result stays in context for every later call. The rules below
// keep contexts small. Measured on the curvature run, writers cost more than the three review stages together.
const CONTEXT = `CONTEXT: grbook.ai is a general relativity book and interactive learning experience with a live voice AI tutor, narration, and 2D/3D demos, for learners from zero to research level. Its knowledge vault (${KB}) holds one concept note per registry concept plus a network of visuals. The tutor teaches from these notes live, and authors write the book from them, so every sentence must be understandable at its rung and every statement must be correct. Today's date: ${DATE}.

BINDING DOCUMENTS. Read these four completely, once, before starting:
- Standard card: ${KB}/_meta/standard-card.md (the condensed writing guide; binding).
- Course conventions: ${KB}/notation/course-conventions.md. If a note needs a choice this file does not make, report it in your summary instead of inventing one.
- Exemplar excerpt: ${KB}/_meta/exemplar-excerpt.json (every field of the holonomy exemplar, one to three items per list; it shows the shape and the bar). Do not read the full exemplar.
- Schema: ${KB}/_schemas/concept-note.schema.json.
Open the full guide ${KB}/_meta/writing-guide.md only at the section a validator warning names or when a card rule is unclear, and read only that section (grep for the heading, then sed -n a line range).

KEEP YOUR CONTEXT SMALL (this matters as much as the work):
- Never read another concept note in full. Use python3 ${T}/note_digest.py <id> [...] for prerequisites and neighbours (a few hundred words each).
- Never read a source chapter or dossier in full. To check one equation or argument, grep ${ROOT}/book-sources/_chapters/<book>/<unit>.md for it and read at most 40 lines around the hit.
- Read your own note once. Fix it with targeted Edit calls, never by rewriting the whole file, and never through a builder script.
- Run the validator with its output piped through head -60. Render once, at the end, and do not read the rendered file.
- Do not re-read files you have already read.

TOOLS:
- Registry entry: python3 -c "import json,glob; [print(json.dumps(c, indent=1)) for f in glob.glob('${KB}/concepts/*/_registry.json') for c in json.load(open(f))['concepts'] if c['id']=='<ID>']"
- Study evidence: python3 ${T}/concept_evidence.py --id <ID>. Internal notes on how three textbooks and the author's earlier course teach the idea, with book locators. Learn from them; never mention or copy them.
- Legacy assets when the evidence names one: ${KB}/sources/legacy/<id>.json
- Note digests: python3 ${T}/note_digest.py <id> [...]
- Visuals: python3 ${T}/visual_ids.py [--grep <word>] lists catalog ids with their presets and proposed ids. Reuse an id before inventing one. Use a preset only if the catalog entry declares it.
- Numbers: python3 (no numpy or sympy; plain python or careful hand algebra).
- Changed text: python3 ${T}/note_diff.py <before.json> <after.json> [--rungs entry,working], or --git <rev> <note.json>. It prints the learner-visible sentences that differ, tagged by rung.
- Snapshots: ${SNAP} (run mkdir -p first).
- Validate: python3 ${T}/validate.py concept ${KB}/concepts/<domain>/<ID>.json | head -60. Fix every error and warning unless your task names a warning as expected; "note:" lines are information.
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
const PERSONA = 'a curious 16-year-old with school algebra and geometry, no calculus, and no physics beyond everyday experience, who knows only the entry rungs of the prerequisites. For working-rung text, read as a strong second-year undergraduate climbing the ladder.'

const writePrompt = (b) => `${CONTEXT}

TASK: Write schema v2 concept notes for domain "${b.domain}", in this order (learning order): ${b.ids.join(', ')}.
For each id:
1. Print the registry entry and run concept_evidence.py; read the evidence. Run note_digest.py on the prerequisites and on leads_to and related ids that have notes, so pictures, terms and ladders connect. If a file already exists at ${note(b)} without "schema_version": 2, it is an older book-centred draft: skim it once for content, then rebuild the note completely.
2. Plan before writing. Answer each of these:
   - What concrete situation opens the entry rung?
   - Which distinct ways in exist, of at least two kinds, each answering its own question? Each entry way carries one idea (card rule 17).
   - What can a learner do at each rung (the objectives)?
   - Which checks and problems prove it?
   - Which misconceptions do learners really have, and which check exposes each one?
   - Which real observations connect the concept to the world?
   - Which visuals serve it? Search visual_ids.py first.
   - What does the formal rung need for a graduate student: precise definitions, hypotheses, results with proof sketches, limits of validity? Tiers that require a formal rung need at least two formal checks and one formal problem.
   - Which research connections are real, and for which are you certain of the references?
3. Derive every equation in course conventions and compute every number with python3 before writing. Work every check, example and problem to its final answer. Try the first what-ifs (card section 4, rule 13) and the counterexamples (section 5) against every general sentence.
4. Write ${note(b)} in one Write call, following the card exactly: the novice contract on every entry-rung field; the accuracy contract everywhere; text formats per field; permanent ids linked by id; a draft stays within 80% of every cap (the validator checks). Set status "draft", revision 1, updated "${DATE}". Every reference gets "verified": false.
5. Validate; fix with targeted Edit calls until OK. Render once.
Return the summary object.`

const novicePrompt = (b, w) => `${CONTEXT}

TASK: You are the NOVICE-READER REVIEWER (card section 11, review 1) for domain "${b.domain}": ${b.ids.join(', ')}. The previous stage reported: ${JSON.stringify(w || {})}
For each note ${note(b)}:
1. Adopt the persona strictly. You are a curious 16-year-old with school algebra and geometry, no calculus, and no physics beyond everyday experience. You know only the entry rungs of this concept's prerequisites: run note_digest.py on them and use the digests' takeaways and glossary as what you know.
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
5. Rewrite until the novice contract holds, with targeted Edit calls. Keep the physics exactly right. If a simpler wording might become false, keep the precise statement and add a sentence that explains it. Never compress other sentences to make room; use the 10% review allowance, then drop the lowest-value item and say which.
6. Read as a stronger student climbing the ladder: each non-entry way's first sentence refers back to the way it continues; no idea, symbol or notation is used before its rung allows it (index notation at working requires the index-notation prerequisite); add bridges where there is a jump; the ways are genuinely different routes.
7. If you changed learner-visible text, bump revision by exactly 1. Set status "novice-reviewed". Add review.novice with verdict, date "${DATE}", reviewed_revision (the note's revision), retell_attempt, stumbles, fixes, and concerns. Do not touch review.physics. Validate until OK, then render once.
Return the summary object, with stumbles counted per note.`

const physicsPrompt = (b, n) => `${CONTEXT}

TASK: You are the ADVERSARIAL PHYSICS REVIEWER (card section 11, review 2): a meticulous GR physicist and differential geometer acting as a referee. Domain "${b.domain}": ${b.ids.join(', ')}. The novice reviewer reported: ${JSON.stringify(n || {})}
For each note ${note(b)}:
0. Before editing, run mkdir -p ${SNAP} and copy the note to ${SNAP}/<ID>.before-physics.json.
1. Validate it.
2. Re-derive every key equation and every derivation step in course conventions. Check signs (signature, Riemann, Ricci, Einstein equation, gauge coupling), index placement, factors of 2 and pi, and the G, c, and hbar factors in SI results.
3. Recompute every number with python3, in one or two scripts rather than many small runs. Work every check, worked example, and problem to its final answer, and check each numeric field and tolerance.
4. Check the conditions of every universal sentence at every rung, including the friendly entry sentences and the novice reviewer's rewrites. Check the sense and branch of every angle, phase, or rotation. Check every "equals" and "differs by" claim, and every analogy that relates quantities, with signs, numerically where possible. A false simplification becomes an equally simple true sentence, never a jargon-heavy one.
5. Try the standard counterexamples of the domain against each general statement (card section 5), and record them.
6. Verify every reference with one WebSearch each (authors, year, title, venue, doi or arxiv); do not fetch pages. Set "verified": true only when confirmed. Correct details you can confirm. Remove references you cannot confirm. Check history claims for scope: what exactly was first, and in what setting.
7. Check structure: prerequisites are direct and acyclic, and assumes and justified_by are consistent; the formal rung is graduate level, with at least two formal checks and one formal problem where the tier requires a formal rung; the research rung and horizon are accurate and current; observations are real, with correct numbers; visual ids and presets exist or are proposed with sketches; nothing mentions or copies the source books.
8. Set status "physics-reviewed" (only with a verdict of accurate or fixed). Add review.physics with verdict, date "${DATE}", verification (claim, method, result for each equation, number, analogy relation, and reference checked), counterexamples, fixes, and concerns.
9. Run python3 ${T}/note_diff.py ${SNAP}/<ID>.before-physics.json ${note(b)} --rungs entry,working. If it lists any change, bump revision by exactly 1. Set review.physics.reviewed_revision to the note's revision. A post-review check of exactly those changes follows, so the one warning that review.novice covers an older revision is expected; fix every other warning. Render once.
Return the summary object, with errors_fixed per note and learner_changes = the number of changed strings note_diff.py listed (0 if none).`

const conformPrompt = (b) => `${CONTEXT}

TASK: You are an EDITOR with a GR physicist's standards and a teacher's ear, bringing reviewed notes up to the current standard. Domain "${b.domain}": ${b.ids.join(', ')}.
${
  b.items && b.items.length
    ? `EDITOR ITEMS. Earlier reviews found these but could not apply them, because they change a claim or a cap blocked them. Apply each one under the novice and accuracy contracts, or explain in major_issues why you did not:
${b.items.map((x, i) => `${i + 1}. ${x}`).join('\n')}
`
    : ''
}For each note ${note(b)}:
0. Run mkdir -p ${SNAP} and copy the note to ${SNAP}/<ID>.before-conform.json.
1. Validate it and read the card (or guide) section its warnings name.
2. Fix every warning except warnings about review revisions. Add real graduate-level substance, never padding. New checks and problems evidence an objective at their own rung, follow the check and problem rules, give numeric answers where they apply, and target real misconceptions. Derive every equation in course conventions and compute every number with python3.
3. Apply the editor items, if any. Keep every entry sentence simple and true. Apart from the items and warnings, do not edit entry-rung text. If an item touches a visual in ${KB}/visuals/, edit only the named lines, bump that visual's revision, validate and render it.
4. Record every change in major_issues. If you changed learner-visible text, bump revision by exactly 1. Keep the status. Do not edit review. The warnings that review.novice and review.physics cover an older revision are expected, because a post-review check follows. Render once.
Return the summary object with verdict "fixed" when you edited and "accurate" otherwise, and edited per note.`

const checkScope = (b) => {
  if (MODE !== 'conform') return `python3 ${T}/note_diff.py ${SNAP}/<ID>.before-physics.json ${note(b)} --rungs entry,working, which lists what the physics review changed after the novice review.`
  if (b.reread_scope === 'changes') return `python3 ${T}/note_diff.py ${b.reread_from ? b.reread_from : `--git ${BASE}`} ${note(b)}, which lists every change no reviewer has read yet.`
  return `the whole entry rung, read sentence by sentence as the novice review does (its entry text was changed by a physics review without a novice re-read), plus python3 ${T}/note_diff.py --git ${BASE} ${note(b)} for changes at other rungs.`
}

const postcheckPrompt = (b, ids, prior) => `${CONTEXT}

TASK: You are the POST-REVIEW CHECKER (card section 8, lifecycle) for domain "${b.domain}": ${ids.join(', ')}. Text changed after a review must get the other lens. You apply both lenses in turn to exactly the changed text. The previous stage reported: ${JSON.stringify(prior || {})}
For each note ${note(b)}:
1. Run mkdir -p ${SNAP} and copy the note to ${SNAP}/<ID>.before-postcheck.json.
2. Scope: ${checkScope(b)} Read each changed sentence inside its paragraph and field. Read nothing else closely.
3. NOVICE PASS. Adopt the persona strictly: ${PERSONA} Record every stumble as {quote, problem, rewrite} (the novice review's list, including rule 17 and wording squeezed to fit a budget). Fix wording only, with targeted Edit calls; never change what a sentence claims. ${
  MODE === 'conform' && b.reread_scope !== 'changes'
    ? 'You may split an overloaded entry way into two, or move its second idea into a working way, as long as every sentence keeps its claim and the ids, questions, takeaways and continues links stay valid. '
    : ''
}If clarity needs a different claim, leave the sentence and put the proposal in major_issues. Use the 10% review allowance; beyond it, drop the lowest-value item and say which.
4. PHYSICS PASS. Now as the adversarial physicist, check every changed or added sentence, including your own rewrites: true within its stated scope at its rung; conditions on universal sentences; sense and branch; frames and measurers; consistent with the note and with course conventions. Try the first what-ifs and the domain's counterexamples on every changed general sentence. Re-derive and recompute (python3) any new or changed equation, number, check, problem, example or observation; verify any new reference with one WebSearch. Fix errors with the simplest true wording. Then read your physics fixes once more as the novice; if one still stumbles, fix its wording and check the claim again.
5. Record: if you changed learner-visible text, bump revision by exactly 1. Append {date "${DATE}", revision, read (the paths you read), stumbles, fixes} to review.novice.rereads and {date "${DATE}", revision, verification (claim, method, result per item checked), fixes} to review.physics.diff_checks. Set review.novice.reviewed_revision and review.physics.reviewed_revision to the note's revision. Keep the status. Validate until OK, then render once.
Return the summary object with, per note, verdict ("fixed" if you edited, else "accurate"), stumbles, errors_fixed, and edited.`

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
    let checkIds = b.ids
    if (MODE !== 'conform') {
      // batch.start = "physics" skips the novice review for a note that is already novice-reviewed.
      if (b.start !== 'physics') {
        out.novice = await slot(2, () => agent(novicePrompt(b, prior), { label: `novice:${tag}`, phase: 'Novice review', schema: REVIEW_SCHEMA, effort: 'high' }))
        b.ids.forEach((id) => release[id]())
        if (!out.novice) return ((out.stopped = 'novice'), out)
      }
      out.physics = await slot(3, () => agent(physicsPrompt(b, out.novice || prior), { label: `physics:${tag}`, phase: 'Physics review', schema: REVIEW_SCHEMA, effort: 'high' }))
      if (!out.physics) return ((out.stopped = 'physics'), out)
      prior = out.physics
      checkIds = items(out.physics).filter((x) => (x.learner_changes || 0) > 0).map((x) => x.id)
    }
    if (checkIds.length) {
      out.postcheck = await slot(4, () => agent(postcheckPrompt(b, checkIds, prior), { label: `postcheck:${tag}`, phase: 'Post-review check', schema: REVIEW_SCHEMA, effort: 'medium' }))
      if (!out.postcheck) return ((out.stopped = 'post-review check'), out)
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
  stages: [...tagged('conform', 'conform'), ...tagged('write', 'write'), ...tagged('novice', 'novice'), ...tagged('physics', 'physics'), ...tagged('postcheck', 'post-review check')],
  writer_problems: done.flatMap((r) => ((r.write && r.write.problems) || []).map((m) => `${r.domain}: ${m}`)),
  conform_issues: issues('conform'),
  novice_issues: issues('novice'),
  physics_issues: issues('physics'),
  postcheck_issues: issues('postcheck'),
}
