#!/usr/bin/env python3
"""Split registry concepts into batches for knowledge/_workflows/gr-concept-notes-v2.js.

Usage: python3 knowledge/_tools/make_note_batches.py [--domain <id>] [--per-batch 4] [--all]

Batches hold concepts of one domain in registry (learning) order. Concepts whose note is already schema v2 with both
the novice and physics reviews are skipped unless --all is given. Without --domain, every domain is listed in
taxonomy order. Prints a summary line, then one Workflow args object per domain.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CONCEPTS = ROOT / 'knowledge' / 'concepts'


def reviewed(note):
	try:
		d = json.loads(note.read_text())
	except (OSError, json.JSONDecodeError):
		return False
	r = d.get('review') or {}
	return d.get('schema_version') == 2 and d.get('status') in ('physics-reviewed', 'published') and bool(r.get('novice')) and bool(r.get('physics'))


def main(argv):
	size = int(argv[argv.index('--per-batch') + 1]) if '--per-batch' in argv else 4
	only = argv[argv.index('--domain') + 1] if '--domain' in argv else None
	taxonomy = json.loads((CONCEPTS / '_taxonomy.json').read_text())
	domains = [d['id'] for d in sorted(taxonomy['domains'], key=lambda d: d['order']) if not only or d['id'] == only]
	runs, total, done = [], 0, 0
	for domain in domains:
		concepts = json.loads((CONCEPTS / domain / '_registry.json').read_text())['concepts']
		pending = []
		for c in concepts:
			total += 1
			if '--all' not in argv and reviewed(CONCEPTS / domain / f"{c['id']}.json"):
				done += 1
			else:
				pending.append(c['id'])
		if pending:
			batches = [{'domain': domain, 'ids': pending[i : i + size]} for i in range(0, len(pending), size)]
			runs.append({'name': f'notes-{domain}', 'max_agents': 5, 'batches': batches})
	batches = sum(len(r['batches']) for r in runs)
	print(f'{total} concepts, {done} reviewed, {total - done} pending in {batches} batches ({3 * batches} agents), {len(runs)} domain runs')
	for r in runs:
		print(json.dumps(r))
	return 0


if __name__ == '__main__':
	sys.exit(main(sys.argv))
