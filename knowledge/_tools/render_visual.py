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


def state(s):
	return ', '.join(f'{k}={json.dumps(v)}' for k, v in s.items())


def render(d):
	front = dict(
		type='visual',
		schema_version=d['schema_version'],
		id=d['id'],
		title=d['title'],
		kind=d['kind'],
		priority=d['priority'],
		status=d['status'],
		revision=d['revision'],
		rungs=d['rungs'],
		serves=[s['concept'] for s in d['serves']],
		builds_on=d['builds_on'],
		leads_to=d['leads_to'],
	)
	o = ['---', *(f'{k}: {json.dumps(v, ensure_ascii=False)}' for k, v in front.items()), '---', '']
	o += [f"# {d['title']}", '', f"`{d['id']}` · {d['kind']} · {d['priority']} · {d['status']} · rungs: {', '.join(d['rungs'])}", '']
	o += [f"> {d['picture']['caption']}", '', '## What it makes visible', '', d['makes_visible'], '']
	o += ['## The picture', '', d['picture']['composition'], '', '| Element | Shows |', '| --- | --- |']
	o += [f"| {cell(e['element'])} | {cell(e['depicts'])} |" for e in d['picture']['elements']]
	pf = d['print_figure']
	o += ['', '## Book figure', '', pf['description'], '', f"Labels: {', '.join(pf['labels'])}. Aspect {pf['aspect']}. Alt text: {pf['alt_text']}", '']
	o += ['## Variants', '', *(f"- **{v['form']}** `{v['id']}`{' (fallback)' if v['fallback'] else ''}: {v['description']}" for v in d['variants']), '']
	if d['params']:
		o += ['## Parameters', '', '| Id | Label | Type | Options or range | Default | Effect |', '| --- | --- | --- | --- | --- | --- |']
		for p in d['params']:
			rng = ', '.join(x['value'] for x in p['options']) if p['options'] else (f"{p['min']}–{p['max']} {p['unit'] or ''}".strip() if p['min'] is not None else '—')
			o.append(f"| `{p['id']}` | {cell(p['label'])} | {p['type']} | {cell(rng)} | {cell(json.dumps(p['default']))} | {cell(p['effect'])} |")
		o.append('')
	o += ['## Presets', '', *(f"- `{p['id']}` {p['label']}: {state(p['state']) or 'defaults'}" for p in d['presets']), '']
	if d['readouts']:
		o += ['## Readouts', '', *(f"- `{r['id']}` {r['label']}{' (' + r['unit'] + ')' if r['unit'] else ''}, visible {r['visible_when']}: “{r['say']}”" for r in d['readouts']), '']
	o += ['## Guided tour', '']
	for i, b in enumerate(d['tour'], 1):
		anim = f"; animate {b['animate']['param']} → {b['animate']['to']} over {b['animate']['seconds']} s" if b['animate'] else ''
		o.append(f"{i}. `{b['id']}` ({b['rung']}, await {b['await']}) state: {state(b['state'])}{anim}  ")
		o.append(f"   *{b['show']}*  ")
		if b['predict']:
			o.append(f"   Predict: “{b['predict']}”  ")
		o.append(f"   Say: “{b['say']}”  ")
		o.append(f"   Describe: {b['describe']}")
	o += ['', '## Design rules', '', *(f"- **{r['rule']}** Because: {r['because']}" + (f" Prevents `{r['misconception']}`." if r['misconception'] else '') for r in d['design_rules']), '']
	m = d['model']
	o += ['## Model', '', m['summary'], '']
	for e in m['equations']:
		o += [f"**{e['label']}**", '', '$$', e['latex'], '$$', ''] + ([f"Holds when: {e['conditions']}", ''] if e['conditions'] else [])
	if m.get('method'):
		o += [f"**Method:** {m['method']}", '']
	if m['tests']:
		o += ['| Test | State | Expect | Note |', '| --- | --- | --- | --- |']
		for t in m['tests']:
			exp = '; '.join(f"{e['readout']} = {e['value']}" + (f" ±{e['abs_tol']}" if e['abs_tol'] is not None else '') + (f" (rel {e['rel_tol']})" if e['rel_tol'] is not None else '') for e in t['expect'])
			o.append(f"| `{t['id']}` | {cell(state(t['state']))} | {cell(exp)} | {cell(t['note'])} |")
		o.append('')
	o += ['## Serves', '', *(f"- [[{s['concept']}]]: {s['uses']}" for s in d['serves']), '']
	links = [('Builds on', d['builds_on']), ('Leads to', d['leads_to']), ('Variant of', [d['variant_of']] if d['variant_of'] else [])]
	o += ['## In the visual network', '', *(f"- **{k}:** " + ', '.join(f'[[{x}]]' for x in v) for k, v in links if v), '']
	a = d['accessibility']
	o += ['## Accessibility', '', a['summary'], '', f"Static alternative: {a['static_alt']}", '']
	if a['keyboard']:
		o += [*(f"- `{k['key']}`: {k['action']}" for k in a['keyboard']), '']
	s = d['starting_material']
	if s['legacy_assets'] or s.get('notes'):
		o += ['## Starting material', '']
		if s['legacy_assets']:
			o += ['Earlier course assets: ' + ', '.join(f'`{x}`' for x in s['legacy_assets']), '']
		if s.get('notes'):
			o += [s['notes'], '']
	r = d.get('review')
	if r:
		o += ['## Review', '', f"**Verdict:** {r['verdict']} ({r['date']})", '', *(f"- Verified: {v['claim']}: {v['method']} → {v['result']}" for v in r['verification']), *(f'- Fixed: {x}' for x in r['fixes']), *(f'- Concern: {x}' for x in r['concerns']), '']
	return '\n'.join(o)


def write_index():
	rows = []
	for f in sorted(VISUALS.glob('*.json')):
		d = json.loads(f.read_text())
		rows.append(f"| [[{d['id']}]] {cell(d['title'])} | {d['kind']} | {d['priority']} | {d['status']} | {', '.join(s['concept'] for s in d['serves'])} |")
	lines = ['# Visuals', '', 'Generated from knowledge/visuals/*.json. Do not edit.', '', '| Visual | Kind | Priority | Status | Serves |', '| --- | --- | --- | --- | --- |', *rows]
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
