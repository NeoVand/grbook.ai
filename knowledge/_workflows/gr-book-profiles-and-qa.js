export const meta = {
  name: 'gr-book-profiles-and-qa',
  description: 'Write a teaching profile for each source book and validate every chapter dossier',
  phases: [
    { title: 'Profile', detail: 'one book-level teaching profile per book' },
    { title: 'QA', detail: 'validate and render every dossier; report gaps' },
  ],
}

const ROOT = '/Users/neo/repos/grbook.ai'
const SHORT = { schutz: 'SCH', 'gifted-amateur': 'GA', dinverno: 'DIV' }
const BOOK_NOTES = {
  schutz: 'Schutz, A First Course in General Relativity (3rd ed.). Geometric, component-light style built on one-forms and pictures of tensors as machines; strong on physical interpretation and astrophysics; later chapters are long and observational.',
  'gifted-amateur': 'Blundell and Lancaster, General Relativity for the Gifted Amateur. Short chapters, informal voice, many margin notes, formal "Example N.M" blocks, and a spiral structure where Part V revisits geometry rigorously and Parts VI-VII add fields, gauge theory, waves, and quantum gravity context.',
  dinverno: "d'Inverno and Vickers, Introducing Einstein's Relativity (2nd ed.). Starts special relativity from the Bondi k-calculus; careful and mathematically explicit (tensor formalism, variational methods, 3+1 and 2+2 formalisms); many spacetime diagrams; principles stated as numbered postulates.",
}
const POLICY = `SOURCE POLICY (strict): we study these books to learn how to TEACH general relativity, not to copy them. Paraphrase everything; quotations at most one short sentence and rare. Equations may be transcribed.`

const PROFILE_SCHEMA = {
  type: 'object',
  required: ['path', 'summary', 'units_needing_attention'],
  properties: { path: { type: 'string' }, summary: { type: 'string' }, units_needing_attention: { type: 'array', items: { type: 'string' } } },
}
const QA_SCHEMA = {
  type: 'object',
  required: ['ok_count', 'warnings', 'errors', 'missing', 'rendered'],
  properties: {
    ok_count: { type: 'integer' },
    warnings: { type: 'array', items: { type: 'string' } },
    errors: { type: 'array', items: { type: 'string' } },
    missing: { type: 'array', items: { type: 'string' } },
    needs_attention: { type: 'array', items: { type: 'string' } },
    rendered: { type: 'integer' },
  },
}

function profilePrompt(book) {
  return `You are writing the teaching profile of one textbook for the grbook.ai knowledge vault: ${SHORT[book]} (book id "${book}"). Its unit dossiers are finished and verified.

BOOK CONTEXT: ${BOOK_NOTES[book]}
${POLICY}

INPUTS
- Front matter (preface or foreword) reading copy: ${ROOT}/book-sources/_chapters/${book}/front.md${book === 'dinverno' ? ' ; also the organization chapter dossier ch01.json' : ''}
- Structure: ${ROOT}/knowledge/sources/${book}/toc.json
- Digest of every unit dossier (read all of it; each unit ends with its verification verdict): python3 ${ROOT}/knowledge/_tools/summarize_dossiers.py ${book}   (add --full-concepts when you need definitions)
- Individual dossiers for detail: ${ROOT}/knowledge/sources/${book}/chapters/<unit>.json (open the ones you need to substantiate claims)

Write ${ROOT}/knowledge/sources/${book}/book-profile.md, starting with YAML frontmatter (type: book-profile, book, book_short, title, authors, edition, units, signature (one sentence), units_needing_attention). Sections:
1. Identity and audience: who it is for, assumed prerequisites, level, tone, length, what it deliberately omits.
2. The authors' stated goals and philosophy (paraphrased from front matter and organization material).
3. Architecture: parts and chapter flow as a dependency outline; where the pivotal ideas first appear (special relativity, vectors and one-forms, tensors, equivalence principle, manifolds and metric, connection and parallel transport, curvature, stress-energy, field equations, Schwarzschild, orbits and tests, black holes, gravitational waves, cosmology, advanced topics); spiral or revisit structure.
4. Conventions and notation, consolidated: signature, units, index conventions, Riemann/Ricci/Einstein sign conventions, distinctive symbols and names, and internal inconsistencies the dossiers found.
5. Pedagogical signature: recurring explanatory moves, preferred representations, use of analogies and thought experiments, figure style, worked-example style, exercise style, margin notes. Be specific, with unit ids.
6. Best explanations by topic: a table of topic -> unit(s) and locators -> why this treatment is especially good.
7. Weaknesses and gaps: where novices stumble, terse or dated material, printed errors found, omissions.
8. Visual language: what the figures do well; the 10-15 most redesign-worthy figures ranked, with unit, label, locator, and the app idea.
9. Tutor guidance: which learners and which moments this book's approach suits, and how the AI tutor should draw on it.
10. Unit index table: unit id, title, printed pages, math/conceptual/novice ratings, one-line summary, verification verdict.
Every claim must be traceable to dossiers (cite unit ids and locators). Return the summary object.`
}

phase('Profile')
const [profiles, qa] = await Promise.all([
  parallel(Object.keys(SHORT).map((b) => () => agent(profilePrompt(b), { label: `profile:${SHORT[b]}`, phase: 'Profile', schema: PROFILE_SCHEMA, effort: 'high' }))),
  agent(`Validate every chapter dossier in the grbook.ai vault and report. Do not edit dossiers.
1. Expected units: every unit in ${ROOT}/knowledge/sources/<book>/toc.json with kind != "front-matter" and read == true, for books schutz, gifted-amateur, dinverno.
2. Run: python3 ${ROOT}/knowledge/_tools/validate.py dossier ${ROOT}/knowledge/sources/*/chapters/*.json
3. Run: python3 ${ROOT}/knowledge/_tools/render_dossier.py ${ROOT}/knowledge/sources/*/chapters/*.json
4. Report: units whose JSON is missing; units with ERRORS (first errors); units with WARNINGS (the warnings); units whose verification object is absent or whose verdict is "needs-attention" (with residual_concerns). Format entries as "book/unit: detail".`, { label: 'qa:validate-all', phase: 'QA', schema: QA_SCHEMA, effort: 'low' }),
])
return { profiles: (profiles || []).filter(Boolean), qa }
