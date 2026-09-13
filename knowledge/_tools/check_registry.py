#!/usr/bin/env python3
"""Check the merged concept registry across all domains.

Usage: python3 knowledge/_tools/check_registry.py [--quiet]

Reads knowledge/concepts/_taxonomy.json and knowledge/concepts/<domain>/_registry.json. Reports:
  errors:   schema errors, duplicate ids, unknown domains, unresolved prerequisite/related ids, prerequisite cycles
  warnings: likely duplicates (same normalized title or alias under different ids), candidate clusters that no
            registry covers, out_of_scope names that the named domain did not pick up
Writes knowledge/_build/registry-report.json. Exit 0 clean, 1 errors, 2 warnings only.
"""
import json
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from collect_concept_candidates import normalize  # noqa: E402
from validate import _errors  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
KB = ROOT / 'knowledge'
DEPTH_ORDER = ['mention', 'introduced', 'revisited', 'developed', 'core']


def find_cycles(graph):
	cycles, state, stack = [], {}, []

	def visit(n):
		state[n] = 1
		stack.append(n)
		for m in graph.get(n, []):
			if state.get(m) == 1:
				cycles.append(stack[stack.index(m) :] + [m])
			elif m not in state:
				visit(m)
		stack.pop()
		state[n] = 2

	sys.setrecursionlimit(10000)
	for n in list(graph):
		if n not in state:
			visit(n)
	return cycles


def main(argv):
	schema = json.loads((KB / '_schemas' / 'concept-registry.schema.json').read_text())
	taxonomy_file = KB / 'concepts' / '_taxonomy.json'
	domains = {d['id'] for d in json.loads(taxonomy_file.read_text())['domains']} if taxonomy_file.exists() else set()
	errors, warnings = [], []
	concepts, owner = {}, {}
	registries = sorted((KB / 'concepts').glob('*/_registry.json'))
	out_of_scope = []
	for f in registries:
		data = json.loads(f.read_text())
		errs = _errors(data, schema, schema, f.parent.name)
		errors += [f'schema {e}' for e in errs[:30]]
		if data.get('domain') != f.parent.name:
			errors.append(f'{f}: domain field "{data.get("domain")}" does not match folder "{f.parent.name}"')
		if domains and data.get('domain') not in domains:
			errors.append(f'{f}: domain "{data.get("domain")}" is not in _taxonomy.json')
		for c in data.get('concepts', []):
			if c['id'] in concepts:
				errors.append(f'duplicate id "{c["id"]}" in {owner[c["id"]]} and {data["domain"]}')
			concepts[c['id']] = c
			owner[c['id']] = data['domain']
		out_of_scope += [(data['domain'], o) for o in data.get('out_of_scope_candidates', [])]

	graph = defaultdict(list)
	for cid, c in concepts.items():
		for p in c.get('prerequisites', []):
			if p not in concepts:
				errors.append(f'{owner[cid]}/{cid}: unresolved prerequisite "{p}"')
			else:
				graph[cid].append(p)
		for r in c.get('related', []):
			if r['id'] not in concepts:
				errors.append(f'{owner[cid]}/{cid}: unresolved related id "{r["id"]}"')
	for cyc in find_cycles(graph)[:50]:
		errors.append('prerequisite cycle: ' + ' -> '.join(cyc))

	names = defaultdict(set)
	for cid, c in concepts.items():
		for n in [c['title'], *c['aliases']]:
			names[normalize(n)].add(cid)
	for n, ids in names.items():
		if len(ids) > 1 and n:
			warnings.append(f'possible duplicate: "{n}" names {sorted(f"{owner[i]}/{i}" for i in ids)}')

	covered = set(names)
	for c in concepts.values():
		covered.update(normalize(x) for x in c['merged_from'])
		for s in c['sources']:
			covered.update(normalize(x) for x in s['names'])
	for d, o in out_of_scope:
		covered.add(normalize(o['name']))
	uncovered = []
	candidates_file = KB / '_build' / 'concept-candidates.json'
	assignments_file = KB / '_build' / 'assignments.json'
	discarded = set()
	if assignments_file.exists():
		discarded = {a['index'] for a in json.loads(assignments_file.read_text())['assignments'] if a['primary'] == 'discard'}
	if candidates_file.exists():
		for i, cl in enumerate(json.loads(candidates_file.read_text())['clusters']):
			if i in discarded:
				continue
			if not any(normalize(n) in covered for n in cl['names']):
				uncovered.append(dict(index=i, key=cl['key'], books=cl['book_count'], max_depth=cl['max_depth'], names=cl['names'][:4]))
	uncovered.sort(key=lambda u: (-u['books'], -DEPTH_ORDER.index(u['max_depth'])))
	for u in uncovered:
		warnings.append(f"uncovered candidate [{u['index']}] {u['key']} ({u['books']} books, deepest {u['max_depth']}): {u['names']}")

	picked = {normalize(x) for c in concepts.values() for x in [c['title'], *c['aliases'], *c['merged_from']]}
	for d, o in out_of_scope:
		if normalize(o['name']) not in picked:
			warnings.append(f'out-of-scope handoff not picked up: "{o["name"]}" from {d} to {o["belongs_to"]}')

	report = dict(
		registries=len(registries),
		concepts=len(concepts),
		per_domain={d: sum(1 for i in owner if owner[i] == d) for d in sorted(set(owner.values()))},
		errors=errors,
		warnings=warnings,
		uncovered=uncovered,
	)
	(KB / '_build').mkdir(exist_ok=True)
	(KB / '_build' / 'registry-report.json').write_text(json.dumps(report, indent=1, ensure_ascii=False))
	print(f"{len(registries)} registries, {len(concepts)} concepts; {len(errors)} errors, {len(warnings)} warnings ({len(uncovered)} uncovered candidates)")
	print('per domain:', report['per_domain'])
	if '--quiet' not in argv:
		for e in errors[:200]:
			print('error:', e)
		for w in warnings[:300]:
			print('warning:', w)
	return 1 if errors else (2 if warnings else 0)


if __name__ == '__main__':
	sys.exit(main(sys.argv))
