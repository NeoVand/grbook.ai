#!/usr/bin/env python3
"""Split the concept registry into batches for knowledge/_workflows/gr-concept-notes-batch.js.

Usage: python3 knowledge/_tools/make_note_batches.py [--per-run 25] [--all]

Batches hold concepts of one domain, in registry (learning) order: 3 per batch for prerequisite, foundation, and core
concepts; 5 per batch for advanced and frontier ones. Concepts that already have a reviewed note are skipped unless
--all is given. Prints a size summary, then one Workflow args object per line with at most --per-run batches each.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CONCEPTS = ROOT / 'knowledge' / 'concepts'
SMALL = {'prerequisite', 'foundation', 'core'}


def main(argv):
	per_run = int(argv[argv.index('--per-run') + 1]) if '--per-run' in argv else 25
	taxonomy = json.loads((CONCEPTS / '_taxonomy.json').read_text())
	order = [d['id'] for d in sorted(taxonomy['domains'], key=lambda d: d['order'])]
	batches, total, done = [], 0, 0
	for domain in order:
		registry_file = CONCEPTS / domain / '_registry.json'
		if not registry_file.exists():
			continue
		pending = {'small': [], 'large': []}
		for c in json.loads(registry_file.read_text())['concepts']:
			total += 1
			note = CONCEPTS / domain / f"{c['id']}.json"
			if note.exists() and '--all' not in argv:
				try:
					if json.loads(note.read_text()).get('review'):
						done += 1
						continue
				except json.JSONDecodeError:
					pass
			pending['small' if c['tier'] in SMALL else 'large'].append(c['id'])
		for kind, size in (('small', 3), ('large', 5)):
			ids = pending[kind]
			batches += [{'domain': domain, 'ids': ids[i : i + size]} for i in range(0, len(ids), size)]
	agents = 2 * len(batches)
	print(f'{total} concepts, {done} with reviewed notes, {len(batches)} batches to run ({agents} agents), {-(-len(batches) // per_run)} runs')
	for i in range(0, len(batches), per_run):
		print(json.dumps({'name': f'concept-notes-{i // per_run + 1}', 'max_agents': 5, 'batches': batches[i : i + per_run]}))
	return 0


if __name__ == '__main__':
	sys.exit(main(sys.argv))
