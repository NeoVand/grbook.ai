export const meta = {
  name: 'gr-concept-registry',
  description: 'Build the canonical cross-book concept registry: taxonomy, cluster assignment, per-domain canonicalization, reconciliation',
  phases: [
    { title: 'Taxonomy', detail: 'design the concept domains' },
    { title: 'Assign', detail: 'assign every candidate cluster to a domain' },
    { title: 'Canonicalize', detail: 'one agent per domain merges candidates into canonical concepts' },
    { title: 'Reconcile', detail: 'resolve duplicates, dangling prerequisites, cycles, and uncovered candidates' },
  ],
}

const ROOT = '/Users/neo/repos/grbook.ai'
const KB = `${ROOT}/knowledge`
const T = `${KB}/_tools`
const CLUSTERS = (args && args.cluster_count) || 0
const BATCH = (args && args.batch_size) || 300
const MAX_AGENTS = Math.min((args && args.max_agents) || 5, 5) // user's pacing rule: at most 5 agents in flight
if (!CLUSTERS) throw new Error('args.cluster_count is required (run collect_concept_candidates.py first)')

/** Runs thunks at most `limit` at a time, preserving result order; failed thunks resolve to null. */
async function limited(thunks, limit = MAX_AGENTS) {
  const results = []
  for (let i = 0; i < thunks.length; i += limit) {
    results.push(...(await parallel(thunks.slice(i, i + limit))))
  }
  return results
}

const CONTEXT = `CONTEXT: grbook.ai is an AI-centred general relativity course for learners of any starting level, with a live voice tutor and interactive 2D/3D demos. Its knowledge vault (${KB}) holds verified teaching dossiers for every unit of three textbooks (Schutz 3rd ed. = SCH, Blundell & Lancaster "Gifted Amateur" = GA, d'Inverno & Vickers 2nd ed. = DIV) plus an inventory of the user's earlier course (${KB}/sources/legacy/). We are now building the canonical CONCEPT REGISTRY: the union of what the three books teach, as permanent concept ids that the course, the tutor's retrieval functions, and the learner model will reference. Candidate concepts were extracted mechanically from the dossiers into clusters of mentions (${KB}/_build/concept-candidates.json, ${CLUSTERS} clusters).
TOOLS:
- python3 ${T}/print_clusters.py --compact [--start N --end M]   one line per cluster
- python3 ${T}/print_clusters.py --detail <i> [<j> ...]          definitions for specific clusters
- python3 ${T}/print_clusters.py --domain <id> [--secondary]     full detail of clusters assigned to a domain
- python3 ${T}/concept_evidence.py --names "<name>" ["<alias>" ...]  all dossier and legacy evidence for a concept
- python3 ${T}/validate.py schema <schema.json> <file.json>
- python3 ${T}/check_registry.py                                cross-domain registry checks
ORIGINAL WORDING ONLY: summaries and notes are written in your own words.`

const ID_RULES = `ID RULES: kebab-case of the standard English name (e.g. metric-tensor, christoffel-symbols, riemann-curvature-tensor, einstein-field-equations, schwarzschild-metric, gravitational-redshift, weak-equivalence-principle). No book prefixes, no chapter numbers, at most 5 words, singular unless the standard name is plural. Ids are permanent: choose the name a physicist would search for.`

const GRANULARITY = `GRANULARITY: a concept is one teachable idea a learner could be said to "know", worth its own 2-10 minute explanation and able to sit in a prerequisite chain (definitions, principles, named equations and results, techniques, phenomena, solutions, key experiments/observations, conventions that cause confusion). Merge synonyms and book-specific names into one concept (book names become aliases, e.g. GA "linear slot machine" -> tensor). Split clusters that conflate distinct ideas (e.g. "local inertial frame" vs "local flatness theorem"). Fold very specific instances (e.g. "Christoffel symbols of the 2-sphere", "covariant derivative of a scalar") into their parent concept's merged_from and mention them in notes as examples, unless they are pivotal results in their own right. Keep genuinely distinct levels of the same idea separate only when books teach them as separate steps (e.g. weak vs Einstein vs strong equivalence principle).`

phase('Taxonomy')
const taxonomy = await agent(`${CONTEXT}

TASK: Design the domain taxonomy that partitions the concept registry.
Read first: the three book profiles (${KB}/sources/schutz/book-profile.md, ${KB}/sources/gifted-amateur/book-profile.md, ${KB}/sources/dinverno/book-profile.md), section 3 ("Topic reuse matrix") of ${KB}/sources/legacy/overview.md, and the compact list of ALL candidate clusters (print it in chunks with --start/--end; read all of it).

Write ${KB}/concepts/_taxonomy.json satisfying ${KB}/_schemas/taxonomy.schema.json. Requirements:
- 14-24 domains ordered as a learning arc from prerequisites to frontier topics. Include prerequisite domains for learners who arrive without them (mathematical tools, classical mechanics and Newtonian gravity, electromagnetism and fields, thermodynamics/quantum background as needed) because the course must serve any starting level.
- Domains must be balanced enough that each can be canonicalized by one expert agent (aim for 20-150 clusters each), and boundaries must be unambiguous: use excludes to settle common border cases (flat vs curved tensor calculus; geodesics vs connection; Schwarzschild geometry vs black holes vs orbits and tests; linearized gravity vs gravitational-wave astronomy; differential forms and Cartan methods; field theory and variational methods; cosmology kinematics vs dynamics vs physical cosmology; experiments and observations).
- Observations and experiments may be their own domain or live with their theory; decide and state the rule.
- course_arc explains how the domains build on each other.
Validate with the schema tool, then return the domain list.`, {
  label: 'taxonomy', phase: 'Taxonomy', effort: 'high',
  schema: { type: 'object', required: ['domains'], properties: { domains: { type: 'array', items: { type: 'object', required: ['id', 'title'], properties: { id: { type: 'string' }, title: { type: 'string' } } } } } },
})
const domainIds = taxonomy.domains.map((d) => d.id)
log(`Taxonomy: ${domainIds.length} domains: ${domainIds.join(', ')}`)

phase('Assign')
const starts = []
for (let s = 0; s < CLUSTERS; s += BATCH) starts.push(s)
await limited(starts.map((s) => () => agent(`${CONTEXT}

TASK: Assign candidate clusters ${s} to ${Math.min(s + BATCH, CLUSTERS) - 1} to domains.
Read the taxonomy ${KB}/concepts/_taxonomy.json (scope, includes, excludes). Print the clusters with --compact --start ${s} --end ${s + BATCH}; use --detail for any cluster whose meaning is unclear from its names.
Write ${KB}/_build/assign-${String(s).padStart(5, '0')}.json as {"assignments": [{"index": <int>, "key": "<cluster key exactly as printed>", "primary": "<domain id>", "secondary": ["<domain id>", ...]}]} with exactly one entry per cluster in your range.
- primary: the single domain that should own the concept. secondary: other domains where it matters as a prerequisite or application (0-2 entries).
- Use primary "discard" only for clusters that are not teachable physics or mathematics concepts (book logistics, a label for one argument that is really an example of another concept should NOT be discarded; assign it to the owner domain so it can be folded in).
Return the count.`, { label: `assign:${s}`, phase: 'Assign', effort: 'medium', schema: { type: 'object', required: ['count'], properties: { count: { type: 'integer' } } } })))

const merged = await agent(`${CONTEXT}

TASK: Merge and complete the cluster assignments.
1. Run: python3 ${T}/print_clusters.py --merge-assignments
2. If it reports UNASSIGNED or KEY MISMATCH clusters, inspect them (--detail), add or correct their entries in the relevant ${KB}/_build/assign-*.json file, and re-run until clean.
3. Return the per-domain primary counts (including "discard") exactly as the final merge prints them.`, {
  label: 'assign:merge', phase: 'Assign', effort: 'low',
  schema: { type: 'object', required: ['counts'], properties: { counts: { type: 'array', items: { type: 'object', required: ['domain', 'count'], properties: { domain: { type: 'string' }, count: { type: 'integer' } } } } } },
})
log(`Assignments: ${merged.counts.map((c) => `${c.domain}=${c.count}`).join(', ')}`)

phase('Canonicalize')
const canon = await limited(domainIds.map((d) => () => agent(`${CONTEXT}

TASK: Canonicalize the concepts of domain "${d}".
Read the taxonomy entry for "${d}" in ${KB}/concepts/_taxonomy.json and the full domain list (so you know where out-of-scope items belong). Print your candidates with: python3 ${T}/print_clusters.py --domain ${d} --secondary   (read all of it; it may be long). Use concept_evidence.py when you need more context.

Write ${KB}/concepts/${d}/_registry.json satisfying ${KB}/_schemas/concept-registry.schema.json:
- domain "${d}", title, scope (from the taxonomy, sharpened).
- concepts: the canonical concepts this domain owns, ordered as they should be learned.
${ID_RULES}
${GRANULARITY}
- tier: prerequisite | foundation | core | advanced | frontier (see schema descriptions).
- summary: 1-2 tutor-ready sentences, correct and self-contained.
- prerequisites: DIRECT prerequisite concept ids only (any domain), minimal and acyclic. For concepts in other domains, use the id that domain will most likely choose under the ID RULES; reconciliation will fix mismatches.
- related: typed links where genuinely useful.
- sources: one entry per book unit that treats it (book, unit, deepest depth there, the names used there). Every primary-domain candidate mention must end up in some concept's sources/merged_from, or in out_of_scope_candidates with the domain it belongs to.
- merged_from: every candidate name folded in.
- Secondary-domain candidates: take ownership only if this domain is the right owner under the taxonomy; otherwise ignore them (their owner handles them).
If the registry is large, you may build it in parts and merge with a short Python script. Validate: python3 ${T}/validate.py schema ${KB}/_schemas/concept-registry.schema.json ${KB}/concepts/${d}/_registry.json
Return the summary.`, {
  label: `canon:${d}`, phase: 'Canonicalize', effort: 'high',
  schema: { type: 'object', required: ['domain', 'concept_count', 'external_prerequisites'], properties: { domain: { type: 'string' }, concept_count: { type: 'integer' }, external_prerequisites: { type: 'array', items: { type: 'string' } }, notes: { type: 'string' } } },
})))
const failedDomains = domainIds.filter((d, i) => !canon[i])
if (failedDomains.length) log(`Domains without a registry: ${failedDomains.join(', ')}`)

phase('Reconcile')
let report = null
for (let round = 1; round <= 4; round++) {
  report = await agent(`${CONTEXT}

TASK: Reconcile the concept registry across all domains (round ${round}).
1. Run: python3 ${T}/check_registry.py   (full report also written to ${KB}/_build/registry-report.json)
2. Fix ALL errors by editing the relevant ${KB}/concepts/<domain>/_registry.json files:
   - duplicate ids: keep the concept in the domain that owns it under the taxonomy; merge sources, aliases, merged_from.
   - unresolved prerequisite/related ids: map to the existing id that means the same thing; if no concept exists and it is a real teachable concept, add it to the owning domain with sources found via concept_evidence.py; otherwise remove the link.
   - prerequisite cycles: remove the edge that is not a true direct prerequisite.
3. Work through warnings, most important first:
   - possible duplicates (same normalized title/alias under different ids): merge true duplicates (update every reference to the removed id across all registries); for distinct concepts, make titles and aliases unambiguous.
   - uncovered candidates: for those appearing in 2+ books or treated at depth developed/core, add them to the right concept (merged_from/sources) or create a concept; for single-book mentions, fold them into the closest concept's merged_from when appropriate. Leave genuinely irrelevant ones.
   - out-of-scope handoffs not picked up: add them to the named domain.
4. Validate each registry you touched with the schema tool, re-run check_registry.py, and iterate within this round as far as you can.
Return the final counts from the last check_registry.py run.`, {
    label: `reconcile:round-${round}`, phase: 'Reconcile', effort: 'high',
    schema: { type: 'object', required: ['concepts', 'errors', 'warnings', 'uncovered'], properties: { concepts: { type: 'integer' }, errors: { type: 'integer' }, warnings: { type: 'integer' }, uncovered: { type: 'integer' }, notes: { type: 'string' } } },
  })
  log(`Reconcile round ${round}: ${report.concepts} concepts, ${report.errors} errors, ${report.warnings} warnings, ${report.uncovered} uncovered`)
  if (report.errors === 0 && report.warnings <= Math.max(25, Math.round(report.concepts * 0.03))) break
}

const listing = await agent(`Run: python3 -c "import json,glob,os; out=[]
for f in sorted(glob.glob('${KB}/concepts/*/_registry.json')):
    r=json.load(open(f)); out.append({'domain': r['domain'], 'concepts': [{'id': c['id'], 'tier': c['tier']} for c in r['concepts']]})
print(json.dumps(out))"
Return its output exactly as the domains array.`, {
  label: 'registry:list', phase: 'Reconcile', effort: 'low',
  schema: { type: 'object', required: ['domains'], properties: { domains: { type: 'array', items: { type: 'object', required: ['domain', 'concepts'], properties: { domain: { type: 'string' }, concepts: { type: 'array', items: { type: 'object', required: ['id', 'tier'], properties: { id: { type: 'string' }, tier: { type: 'string' } } } } } } } } },
})

return { taxonomy: domainIds, assignments: merged.counts, canonicalized: canon.filter(Boolean), failedDomains, finalCheck: report, registry: listing.domains }
