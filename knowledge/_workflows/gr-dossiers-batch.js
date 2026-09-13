export const meta = {
  name: 'gr-dossiers-batch',
  description: 'Read a batch of textbook units into verified teaching dossiers (read, then adversarial verify)',
  phases: [
    { title: 'Read', detail: 'one agent per unit writes the dossier JSON' },
    { title: 'Verify', detail: 'independent reviewer checks coverage, accuracy, locators, copying; fixes in place' },
  ],
}

const ROOT = '/Users/neo/repos/grbook.ai'
const SHORT = { schutz: 'SCH', 'gifted-amateur': 'GA', dinverno: 'DIV' }

const BOOK_NOTES = {
  schutz: 'Schutz, A First Course in General Relativity (3rd ed.). Geometric, component-light style built on one-forms and pictures of tensors as machines; strong on physical interpretation and astrophysics; later chapters are long and observational (gravitational-wave detection, black holes, cosmology). Printed page = pdf page - 18. No "Example N.M" headings: find worked calculations inside the prose. The export drops some footnotes and occasionally truncates a page.',
  'gifted-amateur': 'Blundell and Lancaster, General Relativity for the Gifted Amateur. Short chapters, informal voice, many margin notes (biographies, cautions, pointers) that appear in the reading copy as superscript-numbered notes, often placed before the main text of a page. Formal "Example N.M" blocks, chapter summaries, and a spiral structure where Part V revisits geometry rigorously. Printed page = pdf page - 17. Inventory figure labels are sometimes attached to the wrong image; label each figure by what the image shows.',
  dinverno: "d'Inverno and Vickers, Introducing Einstein's Relativity (2nd ed.). Starts special relativity from the Bondi k-calculus, is careful and mathematically explicit (tensor formalism, variational methods, 3+1 formalism), with many spacetime diagrams, principles stated as numbered postulates, and exercises keyed to sections as \"N.M (§N.K)\". Printed page = pdf page - 15. Worked examples are mostly inline.",
}

const POLICY = `SOURCE POLICY (strict): we study these books to learn how to TEACH general relativity, not to copy them. Ideas, sequencing, analogies, argument shapes, and diagram concepts may be reused with a locator. Wording may not: every prose field must be in your own words (the validator rejects any 12 consecutive words matching the source). Equations may be transcribed (clean up OCR artifacts). Never transcribe exercise statements or long passages; summarize them.`

const RENDER = (book) => `PDF PAGE RENDERS: the page export sometimes loses text, footnotes, or vector figures. Render any original page with
  python3 ${ROOT}/knowledge/_tools/render_pdf_page.py ${book} <pdf_page> [<pdf_page> ...]
and open the printed PNG path with the Read tool. You MUST render and read every page listed in the inventory's suspect_short_pages and every first_mentioned_pdf_page in figures_mentioned_without_image. Also render any page where the text stops mid-argument, an equation is garbled beyond confident repair, a footnote marker has no note, or a figure is referenced but has no image. Recover the missing content into the dossier with normal locators.`

const READ_SCHEMA = {
  type: 'object',
  required: ['json_path', 'validator_status', 'counts', 'notes'],
  properties: {
    json_path: { type: 'string' },
    validator_status: { enum: ['OK', 'WARNINGS', 'ERRORS'] },
    counts: {
      type: 'object',
      required: ['sections', 'concepts', 'key_equations', 'figures', 'worked_examples', 'analogies', 'misconceptions'],
      properties: {
        sections: { type: 'integer' }, concepts: { type: 'integer' }, key_equations: { type: 'integer' },
        figures: { type: 'integer' }, worked_examples: { type: 'integer' }, analogies: { type: 'integer' },
        misconceptions: { type: 'integer' },
      },
    },
    rendered_pages: { type: 'array', items: { type: 'integer' } },
    remaining_warnings: { type: 'array', items: { type: 'string' } },
    notes: { type: 'string' },
  },
}
const VERIFY_SCHEMA = {
  type: 'object',
  required: ['verdict', 'fixes_count', 'major_issues', 'validator_status', 'rendered_md'],
  properties: {
    verdict: { enum: ['accurate', 'fixed', 'needs-attention'] },
    fixes_count: { type: 'integer' },
    major_issues: { type: 'array', items: { type: 'string' } },
    validator_status: { enum: ['OK', 'WARNINGS', 'ERRORS'] },
    rendered_md: { type: 'string' },
  },
}

function paths(book, unit) {
  return {
    reading: `${ROOT}/book-sources/_chapters/${book}/${unit}.md`,
    json: `${ROOT}/knowledge/sources/${book}/chapters/${unit}.json`,
    inspect: `python3 -c "import json; m=json.load(open('${ROOT}/book-sources/_chapters/${book}/manifest.json')); t=json.load(open('${ROOT}/knowledge/sources/${book}/toc.json')); print(json.dumps([x for x in t['units'] if x['id']=='${unit}'][0], indent=1)); print(json.dumps([x for x in m['units'] if x['id']=='${unit}'][0], indent=1))"`,
  }
}

function readPrompt(book, unit) {
  const p = paths(book, unit)
  return `You are building one entry of the grbook.ai knowledge vault: a structured teaching dossier for one unit of a general relativity textbook. The vault will drive (1) authors rewriting an AI-centred interactive GR course with beautiful 2D/3D demos, (2) a live AI voice tutor that must retrieve concepts, prerequisites, analogies, misconceptions and demos while teaching learners of any level, and (3) a learner model. Quality, specificity, and faithfulness to the source matter more than speed.

UNIT: ${SHORT[book]} ${unit} (book id "${book}").
BOOK CONTEXT: ${BOOK_NOTES[book]}

${POLICY}

INPUTS
- Reading copy of the unit, with page markers like "=== [SCH pdf page-143 | printed p.125 | running header: ...] ===": ${p.reading}
- The unit's TOC entry (sections with printed/pdf pages) and inventory (every exported figure image path with caption, "Example N.M" labels, equation tags, exercise pages, suspect_short_pages, figures_mentioned_without_image). Print both with:
  ${p.inspect}
- JSON Schema you must satisfy (read it fully first; descriptions and enums are binding): ${ROOT}/knowledge/_schemas/chapter-dossier.schema.json
- A finished example dossier of the expected depth (skim its structure, do not copy its content): ${ROOT}/knowledge/sources/gifted-amateur/chapters/ch11.json

${RENDER(book)}

PROCEDURE
1. Run the inspect command and read the schema.
2. Read the ENTIRE reading copy in consecutive chunks with the Read tool (offset/limit); do not skim or sample. Track page markers so every locator is exact (pdf_page is the page-N folder number; printed_page from the marker; section = section number in force on that page, or null).
3. Render and read the required PDF pages (see above).
4. Open EVERY figure image in the inventory with the Read tool (absolute paths are in the reading copy; the vault image_path is the inventory path relative to book-sources, e.g. "${book}/pages/page-130/img-42.jpeg"). Describe what is actually drawn (axes, curves, labels, arrows, what varies). A figure with no exported image gets image_path null and a description from the rendered page.
5. Write the dossier to ${p.json} (mkdir -p the directory). For very long units you may build the JSON in parts in a scratch directory and merge them with a short Python script; the final file must be one valid dossier. Field guidance:
   - one_line_summary, role_in_book: what this unit does and why it sits here in the book's arc.
   - learning_objectives: concrete "reader can ..." capabilities.
   - teaching_approach: the pedagogical signature of THIS unit. narrative_arc = the ordered moves the authors make (motivating question -> model -> formalism -> check -> application). signature_moves = distinctive techniques. No generic praise.
   - sections: one per TOC section plus any unnumbered opening or subsection worth separating; summary in own words; key_moves = crucial argument/derivation steps.
   - concepts: every concept the unit defines, develops, or relies on centrally, at useful granularity (e.g. "metric compatibility of the connection", not "tensor calculus"). Use the standard name as name; book-specific names go in aliases. definition must be correct and self-contained. how_introduced = the motivating problem, the route, the representation used. prerequisites = concept names. depth: mention/introduced/developed/core/revisited.
   - key_equations: every central result and the important intermediate steps, with the book's label e.g. "(5.38a)", clean LaTeX, meaning, symbols. Flag printed errors you detect in notes or gaps.
   - figures: all of them; redesign = a concrete ORIGINAL interactive idea for the app (what the learner manipulates, what updates), with form and priority.
   - worked_examples: every "Example N.M" in the inventory plus substantial worked calculations embedded in prose.
   - analogies_and_intuitions, misconceptions_addressed (explicit_in_book=false when inferred), thought_experiments.
   - applications_and_observations: experiments, astrophysical systems, detections, numerical estimates with key numbers (mark your own estimates as such).
   - notation_and_conventions: signature, units, index placement, curvature sign conventions, symbols special to the book.
   - margin_notes: significant side notes and footnotes; skip trivial ones.
   - exercises: count estimate, pdf pages, skills practiced, 3-8 notable exercises summarized in your own words.
   - difficulty: honest 1-5 ratings with notes.
   - cross_references: backward/forward links inside the book (target like "${SHORT[book]} ch6 §6.4") and external works the authors point to.
   - teaching_gems: the 3-10 most reusable explanatory moves, each with an app_idea.
   - gaps_and_pitfalls: where a novice would stumble or the text is terse, wrong, or dated, with a suggestion.
   - tutor_notes: practical guidance for an AI tutor: opening questions, order of explanation, checks for understanding, common learner questions.
   Do NOT add a "verification" object; a reviewer adds it.
6. Validate: python3 ${ROOT}/knowledge/_tools/validate.py dossier ${p.json}
   Fix every error and every warning. Repeat until OK, or until only genuinely wrong warnings remain (explain them in remaining_warnings).
7. Return the summary object (include the pdf pages you rendered).`
}

function verifyPrompt(book, unit, readResult) {
  const p = paths(book, unit)
  return `You are an independent, skeptical reviewer: a GR physicist and experienced educator. Another agent wrote a teaching dossier for ${SHORT[book]} ${unit} (book id "${book}"). Find and FIX its problems in place. Assume it contains errors and omissions until you have checked.

BOOK CONTEXT: ${BOOK_NOTES[book]}
${POLICY}

FILES
- Dossier JSON (edit in place): ${p.json}
- Source reading copy with page markers: ${p.reading}
- TOC entry and inventory: ${p.inspect}
- Schema: ${ROOT}/knowledge/_schemas/chapter-dossier.schema.json
- Writer's report: ${JSON.stringify(readResult || {})}

${RENDER(book)}

CHECKS (do all of them)
1. Run the validator: python3 ${ROOT}/knowledge/_tools/validate.py dossier ${p.json}
2. Read the ENTIRE source reading copy yourself, chunk by chunk, and compare against the dossier:
   a. Coverage: every section; every concept the unit defines or develops (defined terms, emphasized terms, named results, principles); every central equation; every figure; every worked example or substantial worked calculation; notable analogies, thought experiments, misconceptions, applications, historical notes, margin notes and footnotes. Add what is missing.
   b. Export losses: render every suspect page and every figure_mentioned_without_image page, plus 3 other pages of your choice, and compare them to the reading copy. Recover anything the export lost.
   c. Physics and math accuracy: definitions, equation transcriptions (signs, indices, factors, the book's own conventions), claims about what the book argues. Correct errors. Flag any statement that would mislead a learner.
   d. Locators: spot-check at least 15 locators (pdf_page, printed_page, section) against the page markers; if several are wrong, check them all.
   e. Figures: open at least half of the figure images (and every one whose description sounds generic or whose label may be mismatched) and make descriptions and labels match what is drawn. Make redesign ideas concrete and original.
   f. Specificity: replace generic filler with concrete content. teaching_approach, how_introduced, teaching_gems and tutor_notes must describe what this book actually does.
   g. Wording: rewrite any prose that tracks the source text closely, even below the validator threshold.
3. Add or replace the "verification" object: verdict ("accurate" if you changed nothing substantive, "fixed" if you corrected things, "needs-attention" if serious problems remain), fixes (specific list), residual_concerns, coverage counts {toc_sections, sections, inventory_figures, figures, inventory_examples, worked_examples, concepts, key_equations, locators_checked, locators_wrong, pages_rendered}.
4. Re-run the validator until it reports OK (or only justified warnings, recorded in residual_concerns).
5. Render the note: python3 ${ROOT}/knowledge/_tools/render_dossier.py ${p.json}
Return the summary object.`
}

const parse = (mode) => (s) => {
  const [book, unit] = s.split('/')
  return { book, unit, mode }
}
// args.units: read then verify. args.verify_only: the dossier already exists from an interrupted run; verify it.
const units = [...((args && args.units) || []).map(parse('full')), ...((args && args.verify_only) || []).map(parse('verify'))]
log(`Batch "${(args && args.name) || 'unnamed'}": ${units.length} units`)

// Gentle pacing: at most `concurrency` units in flight (default 2). Each unit's dossier is on disk before the next
// chunk starts, so stopping the workflow loses at most the units currently in flight.
const CONCURRENCY = Math.max(1, (args && args.concurrency) || 2)
const READ_ONLY = Boolean(args && args.read_only)

function chain(u) {
  const read = u.mode === 'verify'
    ? Promise.resolve({ notes: 'Dossier written by an earlier, interrupted run; its writer report is unavailable. Verify it fully, including coverage.' })
    : agent(readPrompt(u.book, u.unit), { label: `read:${SHORT[u.book]}-${u.unit}`, phase: 'Read', schema: READ_SCHEMA })
  return read.then((r) => (READ_ONLY && u.mode !== 'verify'
    ? { unit: `${u.book}/${u.unit}`, read: r, verify: null }
    : agent(verifyPrompt(u.book, u.unit, r), { label: `verify:${SHORT[u.book]}-${u.unit}`, phase: 'Verify', schema: VERIFY_SCHEMA, effort: 'high' })
      .then((v) => ({ unit: `${u.book}/${u.unit}`, read: r, verify: v }))))
}

const results = []
for (let i = 0; i < units.length; i += CONCURRENCY) {
  const chunk = units.slice(i, i + CONCURRENCY)
  results.push(...(await parallel(chunk.map((u) => () => chain(u)))))
  log(`${Math.min(i + CONCURRENCY, units.length)}/${units.length} units finished`)
}
const done = results.filter(Boolean)
const failed = units.filter((u, i) => !results[i]).map((u) => `${u.book}/${u.unit}`)
if (failed.length) log(`Units without a dossier: ${failed.join(', ')}`)
return {
  done: done.map((r) => (r.verify
    ? { unit: r.unit, verdict: r.verify.verdict, fixes: r.verify.fixes_count, major_issues: r.verify.major_issues, validator: r.verify.validator_status }
    : { unit: r.unit, verdict: 'read-only', validator: r.read && r.read.validator_status })),
  failed,
}
