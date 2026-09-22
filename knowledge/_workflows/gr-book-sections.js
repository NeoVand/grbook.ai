export const meta = {
  name: 'gr-book-sections',
  description: 'Write book sections from the outline: a writer, then one reviewer who applies the reader lens and the adversarial physics lens in that order (max 5 agents in flight)',
  phases: [
    { title: 'Write', detail: 'one agent per section writes it from the outline, the concept notes and the study evidence' },
    { title: 'Review', detail: 'one agent reads it as a learner, then referees it as an adversarial physicist, then re-reads its own fixes as the learner' },
  ],
}

const ROOT = '/Users/neo/repos/grbook.ai'
const KB = `${ROOT}/knowledge`
const T = `${KB}/_tools`
const DATE = (args && args.date) || 'unknown-date'
const SNAP = args && args.snap_dir
const EXEMPLAR = (args && args.exemplar) || null // section id every other section waits for and reads as the exemplar
// sections: [{chapter, id, after?: [section ids in this run to wait for], start?: 'write'|'review'}]
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

COUNT YOUR TOOL CALLS. Every call re-reads your whole context, so cost tracks the number of calls, not their size. A writer needs about 25 calls in total, a reviewer about 40 for both of its lenses. Batch every mechanical step: compute all numbers in ONE python script; apply all fixes from a validator run in ONE pass (a single python script that edits the JSON, or a few Edit calls); write or rewrite the whole section in ONE Write call; at most three validate-then-fix rounds; validator output through head -60; render once at the end and do not read the rendered file; never re-read a file.

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
    : s.depth === 'working'
      ? 'a strong second-year undergraduate with calculus, vectors and matrices, who has read every earlier section on this track and nothing else'
      : 'a first-year graduate student who has read every earlier section on this track and nothing else, and who knows no notation this book has not introduced'

const writePrompt = (s) => `${CONTEXT(s)}

TASK: Write the book section "${s.id}" of chapter "${s.chapter}" at ${file(s)}.
1. Print the outline entry, the registry entries of its concepts, and the note digests (with --ways at this section's depth, and entry too when the depth is working). Read the summaries and takeaways of the sections it builds on (the earlier sections of its chapter, plus any it needs from earlier chapters). Run concept_evidence.py only for concepts without a note.
2. Plan: the one concrete opening; the parts, one idea each, and which concepts each introduces; the equations and how each is justified; 3 to 8 checks, gradable at this depth, that expose the real misconceptions; the visuals (reuse first); the glossary terms; what earlier sections already give the reader, which you name and do not restate.
3. Derive every equation in course conventions and compute every number with one python3 script before writing. Work every check and example to its final answer. Try the first what-ifs and the standard counterexamples on every general sentence.
4. Write the JSON in ONE Write call, following the section guide and the standard card exactly: the depth's contract on every sentence; text formats per field; permanent ids; a draft stays within 80% of the caps (the validator checks). Set status "draft", revision 1, updated "${DATE}", provenance.notes_used to the note ids you drew on, and every reference "verified": false.
5. Validate; fix in at most three passes; render once.
Return {id, validator, words, problems}. In problems, list missing conventions, concepts that fit badly in this section, and visuals you proposed.`

const reviewPrompt = (s, w) => `${CONTEXT(s)}

TASK: You are the REVIEWER for section "${s.id}" at ${file(s)} (depth ${s.depth}). You carry two lenses and you use them in this order: first you read the section as its learner, then you referee it as an adversarial physicist, then you read your own physics fixes as the learner again. The writer reported: ${JSON.stringify(w || {})}
0. Run mkdir -p ${SNAP}, copy the section to ${SNAP}/${s.id}.before-review.json, and validate it.

READER PASS. You are ${persona(s)}.
1. Read the summaries and takeaways of the sections this one builds on; that is all you know besides the section.
2. Read the section in order: summary, opening, every part's text and takeaway, the equations' meanings and say_aloud lines, the examples, every check's question and answer, the misconceptions, the glossary, the tutor lines.
3. BEFORE changing anything, write retell_attempt: what this reader would say back after one reading. Compare it with the takeaways.
4. Record every stumble as {quote, problem, rewrite}: a sentence you had to reread; an undefined word; two words for one idea or one word for two; a step left implicit; an ambiguous "it"; a direction without its reference; a measurement without its measurer; a rule you could not physically follow; a surprising claim with no reason or test; a general sentence that fails the first what-if; a check the parts do not prepare you for; something restated that an earlier section already gave you; something assumed that no earlier section gave you.
5. Fix wording with targeted edits applied in ONE pass. Keep the physics exactly right; if a simpler wording might become false, keep the precise statement and add the sentence that explains it. Never compress other sentences to make room; use the 10% review allowance, then drop the lowest-value item and say which.

PHYSICS PASS. You are now a meticulous GR physicist and differential geometer acting as a referee, and your reader rewrites above are under review with everything else.
6. Re-derive every key equation in course conventions; check signs, index placement, factors of 2 and pi, and G, c, hbar in SI results. For equations marked earlier-section, confirm the earlier section states them; for stated, confirm the prose says so.
7. Recompute every number with one or two python3 scripts. Work every check and example to its final answer; check numeric fields and tolerances.
8. Check the conditions of every universal sentence at this depth; sense and branch of every angle or rotation; frames and measurers; every "equals" and "differs by" claim, numerically where possible. A false simplification becomes an equally simple true sentence, never a vaguer one.
9. Try the standard counterexamples (card section 5) on each general statement and record them.
10. Verify each reference in further with one WebSearch (no page fetches, none twice); set verified true only when confirmed; remove what you cannot confirm.
11. Check structure: teaches matches the outline and every concept is introduced by name in some part; builds_on names real earlier sections and nothing is assumed that they do not give; checks and misconceptions link both ways; visuals exist or carry sketches; nothing mentions or copies the source books.

READER RE-READ. This is the step a separate physics reviewer could not do.
12. Run python3 ${T}/note_diff.py ${SNAP}/${s.id}.before-review.json ${file(s)} and read every sentence it lists that your physics pass changed, back in the persona of step 1. Fix wording only; a change that would need a different claim goes in major_issues instead.

13. Set status "physics-reviewed" (only with verdict accurate or fixed) and set revision to the writer's revision plus 1 if you changed any learner-visible text. Add review.novice with {verdict, date "${DATE}", reviewed_revision, retell_attempt, stumbles, fixes, concerns} and review.physics with {verdict, date "${DATE}", reviewed_revision, verification (claim, method, result per item), counterexamples, fixes, concerns}; both reviewed_revision fields are the section's final revision, so no stage is left covering an older one. Validate until OK, render once.
Return {id, verdict, validator, stumbles, errors_fixed, learner_changes, edited, major_issues}.`

// Sections wait for the exemplar's review and for the review of anything listed in "after".
const done = {}
const release = {}
for (const s of sections) {
  done[`review:${s.id}`] = new Promise((resolve) => (release[`review:${s.id}`] = resolve))
}
const rel = (k) => release[k] && release[k]()

async function runSection(s) {
  const out = { id: s.id, chapter: s.chapter, stopped: null }
  try {
    const waits = [...(s.after || []).map((id) => done[`review:${id}`]), ...(EXEMPLAR && EXEMPLAR !== s.id && done[`review:${EXEMPLAR}`] ? [done[`review:${EXEMPLAR}`]] : [])].filter(Boolean)
    if (waits.length) await Promise.all(waits)
    let prior = null
    if ((s.start || 'write') === 'write') {
      out.write = await slot(1, () => agent(writePrompt(s), { label: `write:${s.id}`, phase: 'Write', schema: WRITE_SCHEMA }))
      if (!out.write) return ((out.stopped = 'write'), out)
      prior = out.write
    }
    out.review = await slot(2, () => agent(reviewPrompt(s, prior), { label: `review:${s.id}`, phase: 'Review', schema: REVIEW_SCHEMA, effort: 'high' }))
    if (!out.review) return ((out.stopped = 'review'), out)
    return out
  } finally {
    rel(`review:${s.id}`)
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
  stages: [...stage('write'), ...stage('review')],
  writer_problems: finished.flatMap((r) => ((r.write && r.write.problems) || []).map((m) => `${r.id}: ${m}`)),
  issues: finished.flatMap((r) => ['review'].flatMap((k) => ((r[k] && r[k].major_issues) || []).map((m) => `${r.id} [${k}]: ${m}`))),
}
