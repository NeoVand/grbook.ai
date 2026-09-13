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


def constraint(c):
	return '; '.join(f"{k} in {', '.join(v)}" for k, v in (c or {}).items())


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
		o += ['## Parameters', '', '| Id | Label | Type | Options or range | Default | Available when | Effect |', '| --- | --- | --- | --- | --- | --- | --- |']
		for p in d['params']:
			if p['options']:
				rng = ', '.join(x['value'] + (f" ({constraint(x['available_when'])})" if x['available_when'] else '') for x in p['options'])
			elif p['min'] is not None:
				rng = f"{p['min']}–{p['max']} step {p['step']} {p['unit'] or ''}".strip()
			else:
				rng = '—'
			o.append(f"| `{p['id']}` | {cell(p['label'])} | {p['type']} | {cell(rng)} | {cell(json.dumps(p['default']))} | {cell(constraint(p['available_when']) or '—')} | {cell(p['effect'])} |")
		o.append('')
	o += ['## Presets', '', *(f"- `{p['id']}` {p['label']}: {state(p['state']) or 'defaults'}" for p in d['presets']), '']
	if d['readouts']:
		o += ['## Readouts', '']
		for r in d['readouts']:
			bits = [r['unit'] or 'no unit', f"visible {r['visible_when']}", f"{r['decimals']} decimals"]
			if r['range']:
				bits.append(f"range ({r['range'][0]}, {r['range'][1]}]")
			if r['sense']:
				bits.append(f"sense: {r['sense']}")
			say = f"“{r['say']}”" + (f" / “{r['say_negative']}”" if r['say_negative'] else '')
			o.append(f"- `{r['id']}` {r['label']} ({'; '.join(bits)}): {say}")
		o.append('')
	o += ['## Tours', '']
	for t in d['tours']:
		o += [f"### `{t['id']}` · for {('[[' + t['for_concept'] + ']]') if t['for_concept'] else 'any concept'} · {t['rung']}", '']
		for i, b in enumerate(t['beats'], 1):
			anim = f"; animate {b['animate']['param']} → {b['animate']['to']} over {b['animate']['seconds']} s" if b['animate'] else ''
			check = f"; evidences `{b['check']}`" if b['check'] else ''
			o.append(f"{i}. `{b['id']}` ({b['rung']}, await {b['await']}) state: {state(b['state'])}{anim}{check}  ")
			o.append(f"   *{b['show']}*  ")
			if b['predict']:
				o.append(f"   Predict: “{b['predict']}”  ")
			o.append(f"   Say: “{b['say']}”  ")
			o.append(f"   Describe: {b['describe']}")
		o.append('')
	o += ['## Design rules', '', *(f"- **{r['rule']}** Because: {r['because']}" + (f" Prevents `{r['misconception']}`." if r['misconception'] else '') for r in d['design_rules']), '']
	m = d['model']
	o += ['## Model', '', m['summary'], '']
	for e in m['equations']:
		o += [f"**{e['label']}**", '', '$$', e['latex'], '$$', ''] + ([f"Holds when: {e['conditions']}", ''] if e['conditions'] else [])
	if m.get('method'):
		o += [f"**Method:** {m['method']}", '']
	if m['tests']:
		o += ['| Test | State | Expect | Hidden | Note |', '| --- | --- | --- | --- | --- |']
		for t in m['tests']:
			exp = '; '.join(f"{e['readout']} = {e['value']}" + (f" ±{e['abs_tol']}" if e['abs_tol'] is not None else '') + (f" (rel {e['rel_tol']})" if e['rel_tol'] is not None else '') for e in t['expect'])
			o.append(f"| `{t['id']}` | {cell(state(t['state']))} | {cell(exp or '—')} | {cell(', '.join(t['expect_hidden']) or '—')} | {cell(t['note'])} |")
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
	review = d.get('review') or {}
	nov, phy = review.get('novice'), review.get('physics')
	if nov:
		o += ['## Review: novice', '', f"**Verdict:** {nov['verdict']} ({nov['date']}, revision {nov['reviewed_revision']})", '', f"**Retell attempt:** {nov['retell_attempt']}", '']
		o += [*(f"- Stumble: “{s['quote']}”: {s['problem']}" for s in nov['stumbles']), *(f'- Fixed: {x}' for x in nov['fixes']), *(f'- Concern: {x}' for x in nov['concerns']), '']
		for rr in nov.get('rereads', []):
			o += [f"**Re-read** ({rr['date']}, revision {rr['revision']})", '', *(f"- Stumble: “{s['quote']}”: {s['problem']}" for s in rr['stumbles']), *(f'- Fixed: {x}' for x in rr['fixes']), '']
	if phy:
		o += ['## Review: physics', '', f"**Verdict:** {phy['verdict']} ({phy['date']}, revision {phy['reviewed_revision']})", '']
		o += [*(f"- Verified: {v['claim']}: {v['method']} → {v['result']}" for v in phy['verification']), *(f'- Counterexample: {x}' for x in phy['counterexamples'])]
		o += [*(f'- Fixed: {x}' for x in phy['fixes']), *(f'- Concern: {x}' for x in phy['concerns']), '']
		for dc in phy.get('diff_checks', []):
			o += [f"**Diff check** ({dc['date']}, revision {dc['revision']})", '', *(f"- Verified: {v['claim']}: {v['method']} → {v['result']}" for v in dc['verification']), *(f'- Fixed: {x}' for x in dc['fixes']), '']
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
