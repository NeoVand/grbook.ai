#!/usr/bin/env python3
"""Bring registry prerequisites in line with reviewed concept notes, without creating cycles.

Usage: python3 knowledge/_tools/sync_registry.py [--domain <id>] [--write]

For every schema v2 note with both reviews, the note's prerequisites replace the registry entry's prerequisites.
Unknown ids are dropped. An edge that would close a cycle in the whole-vault prerequisite graph is skipped and reported.
Without --write, prints the planned changes only. Run check_registry.py and render_concept.py --indexes afterwards.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CONCEPTS = ROOT / 'knowledge' / 'concepts'


def reaches(graph, start, goal):
	seen, stack = set(), [start]
	while stack:
		n = stack.pop()
		if n == goal:
			return True
		if n not in seen:
			seen.add(n)
			stack.extend(graph.get(n, ()))
	return False


def main(argv):
	only = argv[argv.index('--domain') + 1] if '--domain' in argv else None
	registries = {f.parent.name: json.loads(f.read_text()) for f in sorted(CONCEPTS.glob('*/_registry.json'))}
	entries = {c['id']: c for r in registries.values() for c in r['concepts']}
	graph = {cid: set(c['prerequisites']) for cid, c in entries.items()}
	changed_domains, report = set(), []
	for domain, reg in registries.items():
		if only and domain != only:
			continue
		for c in reg['concepts']:
			note = CONCEPTS / domain / f"{c['id']}.json"
			if not note.exists():
				continue
			d = json.loads(note.read_text())
			r = d.get('review') or {}
			if d.get('schema_version') != 2 or not (r.get('novice') and r.get('physics')):
				continue
			wanted = [p['id'] for p in d['prerequisites'] if p['id'] in entries and p['id'] != c['id']]
			if wanted == c['prerequisites']:
				continue
			graph[c['id']] = set()
			kept, skipped = [], []
			for p in wanted:
				if reaches(graph, p, c['id']):
					skipped.append(p)
				else:
					kept.append(p)
					graph[c['id']].add(p)
			report.append(f"{domain}/{c['id']}: {c['prerequisites']} -> {kept}" + (f'  (skipped, would close a cycle: {skipped})' if skipped else ''))
			if kept != c['prerequisites']:
				c['prerequisites'] = kept
				changed_domains.add(domain)
	print('\n'.join(report) if report else 'registry already matches the reviewed notes')
	if '--write' in argv:
		for domain in sorted(changed_domains):
			(CONCEPTS / domain / '_registry.json').write_text(json.dumps(registries[domain], indent='\t', ensure_ascii=False) + '\n')
		print(f'wrote {len(changed_domains)} registries')
	return 0


if __name__ == '__main__':
	sys.exit(main(sys.argv))
