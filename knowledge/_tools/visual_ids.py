#!/usr/bin/env python3
"""List visuals: catalog entries (knowledge/visuals) and ids proposed in concept notes but not yet in the catalog.

Usage: python3 knowledge/_tools/visual_ids.py [--grep <text>] [--missing] [--domain <id>] [--json]

Search before proposing a new visual id, so one picture is not invented twice under different names.
--missing lists only proposed ids; --domain restricts proposals to notes in one domain; --json prints machine output.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
KB = ROOT / 'knowledge'


def main(argv):
	grep = argv[argv.index('--grep') + 1].lower() if '--grep' in argv else None
	domain = argv[argv.index('--domain') + 1] if '--domain' in argv else None
	catalog = {}
	for f in sorted((KB / 'visuals').glob('*.json')):
		d = json.loads(f.read_text())
		catalog[d['id']] = {'title': d['title'], 'kind': d['kind'], 'priority': d['priority'], 'serves': [s['concept'] for s in d['serves']]}
	proposed = {}
	for f in sorted((KB / 'concepts').glob('*/*.json')):
		if f.name.startswith('_') or (domain and f.parent.name != domain):
			continue
		try:
			d = json.loads(f.read_text())
		except json.JSONDecodeError:
			continue
		if d.get('schema_version') != 2:
			continue
		for v in d['visuals']:
			if v['id'] in catalog:
				continue
			p = proposed.setdefault(v['id'], {'used_by': []})
			p['used_by'].append({'concept': d['id'], 'domain': d['domain'], 'priority': v['priority'], 'role': v['role'], 'sketch': v['sketch']})

	for f in sorted((KB / 'book' / 'sections').glob('*/*.json')):
		if domain and f.parent.name != domain:
			continue
		try:
			d = json.loads(f.read_text())
		except json.JSONDecodeError:
			continue
		for v in d.get('visuals', []):
			if v['id'] in catalog:
				continue
			p = proposed.setdefault(v['id'], {'used_by': []})
			p['used_by'].append({'concept': f"section {d['id']}", 'domain': f"book/{d['chapter']}", 'priority': v['priority'], 'role': v['role'], 'sketch': v['sketch']})

	def match(vid, blob):
		return not grep or grep in (vid + ' ' + json.dumps(blob)).lower()

	catalog = {k: v for k, v in catalog.items() if match(k, v)}
	proposed = {k: v for k, v in proposed.items() if match(k, v)}
	if '--json' in argv:
		print(json.dumps({'catalog': {} if '--missing' in argv else catalog, 'proposed': proposed}, indent=1))
		return 0
	if '--missing' not in argv:
		print(f'# Catalog ({len(catalog)})\n')
		for k, v in catalog.items():
			print(f"- {k} [{v['kind']}, {v['priority']}] {v['title']} — serves {', '.join(v['serves'])}")
	print(f'\n# Proposed in notes, not in catalog ({len(proposed)})\n')
	for k, v in sorted(proposed.items()):
		print(f'- {k} (used by {len(v["used_by"])})')
		for u in v['used_by']:
			sketch = (u['sketch'] or '')[:160]
			print(f"  - {u['domain']}/{u['concept']} [{u['priority']}]: {u['role'][:120]}" + (f' | sketch: {sketch}' if sketch else ''))
	return 0


if __name__ == '__main__':
	sys.exit(main(sys.argv))
