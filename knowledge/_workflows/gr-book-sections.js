export const meta = {
  name: 'gr-book-sections',
  description: 'Write book sections from the outline: writer, novice read (entry and working depth), adversarial physics review, one post-review check (max 5 agents in flight)',
  phases: [
    { title: 'Write', detail: 'one agent per section writes it from the outline, the concept notes and the study evidence' },
    { title: 'Novice review', detail: 'a beginner (or a second-year student at working depth) records a retelling and stumbles, then fixes wording' },
    { title: 'Physics review', detail: 'an adversarial physicist re-derives, recomputes, tries counterexamples, verifies references, and fixes' },
    { title: 'Post-review check', detail: 'one agent reads the text changed after the reviews with the novice lens, then the physics lens, and signs' },
  ],
}

const ROOT = '/Users/neo/repos/grbook.ai'
const KB = `${ROOT}/knowledge`
const T = `${KB}/_tools`
const DATE = (args && args.date) || 'unknown-date'
const SNAP = args && args.snap_dir
const EXEMPLAR = (args && args.exemplar) || null // section id every other section waits for and reads as the exemplar
// sections: [{chapter, id, after?: [section ids in this run to wait for], start?: 'write'|'novice'|'physics'|'postcheck'}]
const sections = (args && args.sections) || []
if (!SNAP) throw new Error('args.snap_dir is required: a directory outside the repository for snapshots')
if (!sections.length) throw new Error('args.sections is required')
log(`Run "${(args && args.name) || 'unnamed'}": ${sections.length} sections, exemplar ${EXEMPLAR || 'none'}, date ${DATE}`)

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

const file = (s) => `${KB}/book/sections/${s.chapter}/${s.id}.json`
const exemplarLine = (s) =>
  EXEMPLAR && EXEMPLAR !== s.id
    ? `- Exemplar section: ${KB}/book/sections/*/${EXEMPLAR}.json (find it with ls). It sets the bar for every field. Read it once.`
    : '- No exemplar section exists yet: this section becomes the exemplar, so make every field the best example of the guide.'

const CONTEXT = (s) => `CONTEXT: grbook.ai is a general relativity book and interactive learning experience with a live voice AI tutor, narration, and 2D/3D demos, for learners from zero to research level. The book is written section by section from an approved outline (${KB}/book/outline.json). Each section teaches a cluster of registry concepts at one depth; the book itself is the depth ladder, so a section assumes every earlier section on its track and restates nothing. The tutor teaches from sections live, so every sentence must be understandable at the section's depth and every statement must be correct. Today's date: ${DATE}.

BINDING DOCUMENTS. Read these once, completely, before starting:
- Standard card: ${KB}/_meta/standard-card.md (the writing standard; binding for every sentence).
- Section guide: ${KB}/book/section-guide.md (what a section is, sizes, sources, lifecycle).
- Course conventions: ${KB}/notation/course-conventions.md. If a section needs a choice this file does not make, report it in your summary instead of inventing one.
- Schema: ${KB}/_schemas/book-section.schema.json.
${exemplarLine(s)}
Open the full guide ${KB}/_meta/writing-guide.md only at the section a validator warning names, and read only that section.

COUNT YOUR TOOL CALLS. Every call re-reads your whole context, so cost tracks the number of calls, not their size. A writer needs about 25 calls in total, a reviewer about 30. Batch every mechanical step: compute all numbers in ONE python script; apply all fixes from a validator run in ONE pass (a single python script that edits the JSON, or a few Edit calls); write or rewrite the whole section in ONE Write call; at most three validate-then-fix rounds; validator output through head -60; render once at the end and do not read the rendered file; never re-read a file.

TOOLS:
- This section's outline entry (chapter, track, depth, concepts): python3 -c "import json; o=json.load(open('${KB}/book/outline.json')); [print(json.dumps(dict(s, chapter=c['id'], chapter_title=c['title'], earlier=[x['id'] for x in c['sections'][:i]]), indent=1)) for p in o['parts'] for c in p['chapters'] for i,s in enumerate(c['sections']) if s['id']=='${s.id}']"
- Registry entries: python3 -c "import json,glob; ids=set('${'IDS'}'.split(',')); [print(json.dumps({k:c[k] for k in ('id','title','tier','summary','prerequisites','aliases')})) for f in glob.glob('${KB}/concepts/*/_registry.json') for c in json.load(open(f))['concepts'] if c['id'] in ids]" (put the comma-separated ids in place of IDS).
- Concept notes (reviewed source material): python3 ${T}/note_digest.py [--ways entry,working] <id> [...]. One call for all of this section's concepts; add --ways for the rungs at this section's depth. Never read a note file directly.
- Study evidence, only for concepts that have no note: python3 ${T}/concept_evidence.py --id <id>. Learn from it; never mention or copy the books.
- Earlier sections this one builds on: read only their summary, part headings and takeaways: python3 -c "import json,glob; [print(json.dumps({k:d[k] for k in ('id','summary')}), [ (p['heading'],p['takeaway']) for p in d['parts']]) for f in glob.glob('${KB}/book/sections/*/*.json') for d in [json.load(open(f))] if d['id'] in ('a','b')]".
- Visuals: python3 ${T}/visual_ids.py [--grep <word>] lists catalog ids with presets and proposed ids. Reuse an id before inventing one.
- Numbers: python3 (no numpy or sympy).
- Changed text: python3 ${T}/note_diff.py <before.json> <after.json> [--rungs entry,working] lists the learner-visible sentences that differ.
- Snapshots: ${SNAP} (run mkdir -p first).
- Validate: python3 ${T}/validate.py section ${file(s)} | head -60. Fix every error and warning unless your task names a warning as expected; "note:" lines are information.
- Render: python3 ${T}/render_section.py ${file(s)}`

const WRITE_SCHEMA = {
  type: 'object',
  required: ['id', 'validator', 'problems'],
  properties: { id: { type: 'string' }, validator: { enum: ['OK', 'WARNINGS', 'ERRORS'] }, words: { type: 'integer' }, problems: { type: 'array', items: { type: 'string' } } },
}
const REVIEW_SCHEMA = {
  type: 'object',
  required: ['id', 'verdict', 'validator', 'major_issues'],
  properties: {
    id: { type: 'string' },
    verdict: { enum: ['accurate', 'fixed', 'needs-attention'] },
    validator: { enum: ['OK', 'WARNINGS', 'ERRORS'] },
    stumbles: { type: 'integer' },
    errors_fixed: { type: 'integer' },
    learner_changes: { type: 'integer', description: 'Physics review: learner-visible strings note_diff.py lists as changed' },
    edited: { type: 'boolean' },
    major_issues: { type: 'array', items: { type: 'string' } },
  },
}

const persona = (s) =>
  s.depth === 'entry'
    ? 'a curious 16-year-old with school algebra and geometry, no calculus, and no physics beyond everyday experience, who has read the main-track sections before this one'
    : 'a strong second-year undergraduate with calculus, vectors and matrices, who has read every earlier section on this track and nothing else'

const writePrompt = (s) => `${CONTEXT(s)}

TASK: Write the book section "${s.id}" of chapter "${s.chapter}" at ${file(s)}.
1. Print the outline entry, the registry entries of its concepts, and the note digests (with --ways at this section's depth, and entry too when the depth is working). Read the summaries and takeaways of the sections it builds on (the earlier sections of its chapter, plus any it needs from earlier chapters). Run concept_evidence.py only for concepts without a note.
2. Plan: the one concrete opening; the parts, one idea each, and which concepts each introduces; the equations and how each is justified; 3 to 8 checks, gradable at this depth, that expose the real misconceptions; the visuals (reuse first); the glossary terms; what earlier sections already give the reader, which you name and do not restate.
3. Derive every equation in course conventions and compute every number with one python3 script before writing. Work every check and example to its final answer. Try the first what-ifs and the standard counterexamples on every general sentence.
4. Write the JSON in ONE Write call, following the section guide and the standard card exactly: the depth's contract on every sentence; text formats per field; permanent ids; a draft stays within 80% of the caps (the validator checks). Set status "draft", revision 1, updated "${DATE}", provenance.notes_used to the note ids you drew on, and every reference "verified": false.
5. Validate; fix in at most three passes; render once.
Return {id, validator, words, problems}. In problems, list missing conventions, concepts that fit badly in this section, and visuals you proposed.`

const novicePrompt = (s, w) => `${CONTEXT(s)}

TASK: You are the READER REVIEWER for section "${s.id}" at ${file(s)} (depth ${s.depth}). The writer reported: ${JSON.stringify(w || {})}
1. Adopt the persona strictly: ${persona(s)}. Read the summaries and takeaways of the sections this one builds on; that is all you know.
2. Read the section as a reader would, in order: summary, opening, every part's text and takeaway, the equations' meanings and say_aloud lines, the examples, every check's question and answer, the misconceptions, the glossary, and the tutor lines.
3. BEFORE changing anything, write retell_attempt: what this reader would say back after one reading. Compare it with the takeaways.
4. Record every stumble as {quote, problem, rewrite}: a sentence you had to reread; an undefined word; two words for one idea or one word for two; a step left implicit; an ambiguous "it"; a direction without its reference; a measurement without its measurer; a rule you could not physically follow; a surprising claim with no reason or test; a general sentence that fails the first what-if; a check the parts do not prepare you for; something restated that an earlier section already gave you; something assumed that no earlier section gave you.
5. Fix wording with targeted edits applied in ONE pass. Keep the physics exactly right; if a simpler wording might become false, keep the precise statement and add the sentence that explains it. Never compress other sentences to make room; use the 10% review allowance, then drop the lowest-value item and say which.
6. If you changed learner-visible text, bump revision by exactly 1. Set status "novice-reviewed". Add review.novice with verdict, date "${DATE}", reviewed_revision, retell_attempt, stumbles, fixes, concerns. Validate until OK, render once.
Return {id, verdict, validator, stumbles, edited, major_issues}.`

const physicsPrompt = (s, n) => `${CONTEXT(s)}

TASK: You are the ADVERSARIAL PHYSICS REVIEWER for section "${s.id}" at ${file(s)}: a meticulous GR physicist and differential geometer acting as a referee. The previous stage reported: ${JSON.stringify(n || {})}
0. Run mkdir -p ${SNAP} and copy the section to ${SNAP}/${s.id}.before-physics.json before editing.
1. Validate it.
2. Re-derive every key equation in course conventions; check signs, index placement, factors of 2 and pi, and G, c, hbar in SI results. For equations marked earlier-section, confirm the earlier section states them; for stated, confirm the prose says so.
3. Recompute every number with one or two python3 scripts. Work every check and example to its final answer; check numeric fields and tolerances.
4. Check the conditions of every universal sentence at this depth, including the reader reviewer's rewrites; sense and branch of every angle or rotation; frames and measurers; every "equals" and "differs by" claim, numerically where possible. A false simplification becomes an equally simple true sentence.
5. Try the standard counterexamples (card section 5) on each general statement and record them.
6. Verify each reference in further with one WebSearch (no page fetches, none twice); set verified true only when confirmed; remove what you cannot confirm.
7. Check structure: teaches matches the outline and every concept is introduced by name in some part; builds_on names real earlier sections and nothing is assumed that they do not give; checks and misconceptions link both ways; visuals exist or carry sketches; nothing mentions or copies the source books.
8. Set status "physics-reviewed" (only with verdict accurate or fixed). Add review.physics with verdict, date "${DATE}", verification (claim, method, result per item), counterexamples, fixes, concerns.
9. Run python3 ${T}/note_diff.py ${SNAP}/${s.id}.before-physics.json ${file(s)}. If it lists any change, bump revision by exactly 1; the warning that review.novice covers an older revision is then expected because a post-review check follows. Set review.physics.reviewed_revision to the section's revision. Fix every other warning. Render once.
Return {id, verdict, validator, errors_fixed, learner_changes, edited, major_issues}.`

const postcheckPrompt = (s, p) => `${CONTEXT(s)}

TASK: You are the POST-REVIEW CHECKER for section "${s.id}" at ${file(s)}. Text changed after a review must get the other lens; you apply both lenses to exactly the changed text. The physics review reported: ${JSON.stringify(p || {})}
1. Run mkdir -p ${SNAP} and copy the section to ${SNAP}/${s.id}.before-postcheck.json.
2. Scope: python3 ${T}/note_diff.py ${SNAP}/${s.id}.before-physics.json ${file(s)}. Read each changed sentence inside its part or field. Read nothing else closely.
3. READER PASS as ${persona(s)}: record stumbles as {quote, problem, rewrite}; fix wording only, in one pass; never change what a sentence claims. Proposals that need a different claim go in major_issues.
4. PHYSICS PASS as the adversarial physicist: every changed or added sentence, including your own rewrites, is true within its scope at this depth, with conditions, sense, frames and measurers intact and consistent with the section and course conventions; recompute any changed number. Fix errors with the simplest true wording, then read your fixes once more as the reader.
5. If you changed learner-visible text, bump revision by exactly 1. Append {date "${DATE}", revision, read, stumbles, fixes} to review.novice.rereads (create review.novice first if the depth had no reader review, with an empty retell_attempt and stumbles) and {date "${DATE}", revision, verification, fixes} to review.physics.diff_checks. Set both reviewed_revision fields to the section's revision. Keep the status. Validate until OK, render once.
Return {id, verdict, validator, stumbles, errors_fixed, edited, major_issues}.`

// Sections wait for the exemplar's physics review and for the novice review of anything listed in "after".
const done = {}
const release = {}
for (const s of sections) {
  done[`novice:${s.id}`] = new Promise((resolve) => (release[`novice:${s.id}`] = resolve))
  done[`physics:${s.id}`] = new Promise((resolve) => (release[`physics:${s.id}`] = resolve))
}
const rel = (k) => release[k] && release[k]()

async function runSection(s) {
  const out = { id: s.id, chapter: s.chapter, stopped: null }
  try {
    const waits = [...(s.after || []).map((id) => done[`novice:${id}`]), ...(EXEMPLAR && EXEMPLAR !== s.id && done[`physics:${EXEMPLAR}`] ? [done[`physics:${EXEMPLAR}`]] : [])].filter(Boolean)
    if (waits.length) await Promise.all(waits)
    const start = s.start || 'write'
    let prior = null
    if (start === 'write') {
      out.write = await slot(1, () => agent(writePrompt(s), { label: `write:${s.id}`, phase: 'Write', schema: WRITE_SCHEMA }))
      if (!out.write) return ((out.stopped = 'write'), out)
      prior = out.write
    }
    const needsNovice = s.depth === 'entry' || s.depth === 'working'
    if (['write', 'novice'].includes(start) && needsNovice) {
      out.novice = await slot(2, () => agent(novicePrompt(s, prior), { label: `novice:${s.id}`, phase: 'Novice review', schema: REVIEW_SCHEMA, effort: 'high' }))
      rel(`novice:${s.id}`)
      if (!out.novice) return ((out.stopped = 'novice'), out)
      prior = out.novice
    } else rel(`novice:${s.id}`)
    if (['write', 'novice', 'physics'].includes(start)) {
      out.physics = await slot(3, () => agent(physicsPrompt(s, prior), { label: `physics:${s.id}`, phase: 'Physics review', schema: REVIEW_SCHEMA, effort: 'high' }))
      rel(`physics:${s.id}`)
      if (!out.physics) return ((out.stopped = 'physics'), out)
      prior = out.physics
    } else rel(`physics:${s.id}`)
    const changed = start === 'postcheck' || (out.physics && (out.physics.learner_changes || 0) > 0)
    if (changed) {
      out.postcheck = await slot(4, () => agent(postcheckPrompt(s, prior), { label: `postcheck:${s.id}`, phase: 'Post-review check', schema: REVIEW_SCHEMA, effort: 'medium' }))
      if (!out.postcheck) return ((out.stopped = 'post-review check'), out)
    }
    return out
  } finally {
    rel(`novice:${s.id}`)
    rel(`physics:${s.id}`)
  }
}

const results = await pipeline(sections, (s) => runSection(s))
const finished = results.filter(Boolean)
const stopped = [...finished.filter((r) => r.stopped).map((r) => `${r.id}: stopped at ${r.stopped}`), ...sections.map((s, i) => (results[i] ? null : `${s.id}: crashed`)).filter(Boolean)]
if (stopped.length) log(`Unfinished: ${stopped.join(' | ')}`)
const stage = (k) => finished.filter((r) => r[k]).map((r) => ({ stage: k, ...r[k] }))
return {
  finished: finished.filter((r) => !r.stopped).map((r) => r.id),
  stopped,
  stages: [...stage('write'), ...stage('novice'), ...stage('physics'), ...stage('postcheck')],
  writer_problems: finished.flatMap((r) => ((r.write && r.write.problems) || []).map((m) => `${r.id}: ${m}`)),
  issues: finished.flatMap((r) => ['novice', 'physics', 'postcheck'].flatMap((k) => ((r[k] && r[k].major_issues) || []).map((m) => `${r.id} [${k}]: ${m}`))),
}
