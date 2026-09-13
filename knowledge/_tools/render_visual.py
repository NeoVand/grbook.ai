#!/usr/bin/env python3
"""Render visual JSON (knowledge/visuals/<id>.json) into markdown, and write knowledge/visuals/_index.md.

Usage:
  python3 knowledge/_tools/render_visual.py <visuals/<id>.json> [...]
  python3 knowledge/_tools/render_visual.py --index
The JSON is the source of truth; never edit generated .md files by hand. Provenance is internal and is not rendered.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
VISUALS = ROOT / 'knowledge' / 'visuals'


def cell(s):
	return str(s if s is not None else '—').replace('|', '\\|').replace('\n', ' ')


def render(d):
	front = dict(
		type='visual',
		schema_version=d['schema_version'],
		id=d['id'],
		title=d['title'],
		kind=d['kind'],
		priority=d['priority'],
		rungs=d['rungs'],
		serves=[s['concept'] for s in d['serves']],
		builds_on=d['builds_on'],
		leads_to=d['leads_to'],
		review=(d.get('review') or {}).get('verdict'),
	)
	o = ['---', *(f'{k}: {json.dumps(v, ensure_ascii=False)}' for k, v in front.items()), '---', '']
	o += [f"# {d['title']}", '', f"`{d['id']}` · {d['kind']} · {d['priority']} · rungs: {', '.join(d['rungs'])}", '']
	o += [f"> {d['picture']['caption']}", '', '## What it makes visible', '', d['makes_visible'], '']
	o += ['## The picture', '', d['picture']['composition'], '', '| Element | Shows |', '| --- | --- |']
	o += [f"| {cell(e['element'])} | {cell(e['depicts'])} |" for e in d['picture']['elements']]
	o += ['', '## Variants', '', *(f"- **{v['form']}**: {v['description']}" for v in d['variants']), '']
	if d['interaction']:
		o += ['## Interaction', '', '| Control | Effect |', '| --- | --- |']
		o += [f"| {cell(i['control'])} | {cell(i['effect'])} |" for i in d['interaction']]
		o.append('')
	o += ['## Guided tour', '']
	o += [f"{i}. *{b['show']}*  \n   “{b['say']}”" for i, b in enumerate(d['tour'], 1)]
	o += ['', '## Design rules', '', *(f"- **{r['rule']}** Because: {r['because']}" for r in d['design_rules']), '']
	m = d['model']
	o += ['## Model', '', m['summary'], '']
	for e in m['equations']:
		o += ['$$', e, '$$', '']
	if m.get('method'):
		o += [f"**Method:** {m['method']}", '']
	if m['tests']:
		o += ['| Test case | Expected |', '| --- | --- |', *(f"| {cell(t['case'])} | {cell(t['expected'])} |" for t in m['tests']), '']
	o += ['## Serves', '', *(f"- [[{s['concept']}]]: {s['uses']}" for s in d['serves']), '']
	links = [('Builds on', d['builds_on']), ('Leads to', d['leads_to']), ('Variant of', [d['variant_of']] if d['variant_of'] else [])]
	o += ['## In the visual network', '', *(f"- **{k}:** " + ', '.join(f'[[{x}]]' for x in v) for k, v in links if v), '']
	o += ['## Accessibility', '', d['accessibility'], '']
	s = d['starting_material']
	if s['legacy_assets'] or s.get('notes'):
		o += ['## Starting material', '']
		if s['legacy_assets']:
			o.append('Earlier course assets: ' + ', '.join(f'`{a}`' for a in s['legacy_assets']))
			o.append('')
		if s.get('notes'):
			o += [s['notes'], '']
	r = d.get('review')
	if r:
		o += ['## Review', '', f"**Verdict:** {r['verdict']}", '', *(f'- Fixed: {x}' for x in r['fixes']), *(f'- Concern: {x}' for x in r['concerns']), '']
	return '\n'.join(o)


def write_index():
	rows = []
	for f in sorted(VISUALS.glob('*.json')):
		d = json.loads(f.read_text())
		rows.append(f"| [[{d['id']}]] {cell(d['title'])} | {d['kind']} | {d['priority']} | {', '.join(s['concept'] for s in d['serves'])} |")
	lines = ['# Visuals', '', 'Generated from knowledge/visuals/*.json. Do not edit.', '', '| Visual | Kind | Priority | Serves |', '| --- | --- | --- | --- |', *rows]
	(VISUALS / '_index.md').write_text('\n'.join(lines) + '\n')
	print(f'index written ({len(rows)} visuals)')


if __name__ == '__main__':
	if '--index' in sys.argv:
		write_index()
	else:
		for f in sys.argv[1:]:
			p = Path(f)
			p.with_suffix('.md').write_text(render(json.loads(p.read_text())))
			print('rendered', p.with_suffix('.md'))
