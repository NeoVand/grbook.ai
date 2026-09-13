#!/usr/bin/env python3
"""Render concept note JSON (schema v2) into vault markdown, and write the concept _index.md files.

Usage:
  python3 knowledge/_tools/render_concept.py <concepts/<domain>/<id>.json> [...]
  python3 knowledge/_tools/render_concept.py --indexes
The JSON is the source of truth; never edit generated .md files by hand. Provenance is internal and is not rendered.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
KB = ROOT / 'knowledge'


def cell(s):
	return str(s if s is not None else '—').replace('|', '\\|').replace('\n', ' ')


def numbered(items):
	return '\n'.join(f'{i}. {x}' for i, x in enumerate(items, 1))


def render(d):
	review = d.get('review') or {}
	front = dict(
		type='concept',
		schema_version=d['schema_version'],
		id=d['id'],
		title=d['title'],
		domain=d['domain'],
		tier=d['tier'],
		aliases=d['aliases'],
		prerequisites=[p['id'] for p in d['prerequisites']],
		leads_to=[x['id'] for x in d['leads_to']],
		visuals=[v['id'] for v in d['visuals']],
		review={k: v['verdict'] for k, v in review.items()},
	)
	o = ['---', *(f'{k}: {json.dumps(v, ensure_ascii=False)}' for k, v in front.items()), '---', '']
	o += [f"# {d['title']}", '', f"`{d['id']}` · {d['domain']} · {d['tier']}", '']
	needs = ' · '.join(f"[[{p['id']}]] ({p['needed_for']})" for p in d['prerequisites'])
	o.append(f"**Needs:** {needs or 'nothing beyond everyday experience'}  ")
	if d['leads_to']:
		o.append('**Opens:** ' + ' · '.join(f"[[{x['id']}]]" for x in d['leads_to']) + '  ')
	if d['related']:
		o.append('**Related:** ' + ' · '.join(f"[[{x['id']}]] ({x['relation']})" for x in d['related']) + '  ')
	if d['visuals']:
		o.append('**Visuals:** ' + ' · '.join(('★ ' if v['priority'] == 'flagship' else '') + f"[[{v['id']}]]" for v in d['visuals']))
	o += ['', f"> {d['summary']}", '', '## Ways in', '']

	for i, w in enumerate(d['ways_in'], 1):
		o += [f"### {i}. {w['title']} · {w['rung']}", '', w['explanation'].strip(), '']
		if w.get('picture'):
			o += [f"*Picture:* {w['picture']}", '']
		if w.get('simplifies'):
			o += [f"*What this leaves out:* {w['simplifies']}", '']
		tail = []
		if w['assumes']:
			tail.append('*Builds on:* ' + ', '.join(f'[[{a}]]' for a in w['assumes']))
		if w['visuals']:
			tail.append('*Visuals:* ' + ', '.join(f'[[{v}]]' for v in w['visuals']))
		if tail:
			o += [' · '.join(tail), '']

	if d['glossary']:
		o += ['## Glossary', '', '| Term | In plain words |', '| --- | --- |']
		o += [f"| {cell(g['term'])} | {cell(g['plain_definition'])} |" for g in d['glossary']]
		o.append('')

	if d['key_equations']:
		o += ['## Key equations', '']
		for e in d['key_equations']:
			o += [f"### {e['name']} · {e['rung']}", '', '$$', e['latex'], '$$', '', e['meaning'], '']
			o.append('**Symbols:** ' + '; '.join(f"{s['symbol']}: {s['meaning']}" for s in e['symbols']) + '  ')
			if e.get('conditions'):
				o.append(f"**Holds when:** {e['conditions']}  ")
			o += [f"**Say it:** “{e['say_aloud']}”", '']

	if d['derivations']:
		o += ['## Derivations', '']
		for x in d['derivations']:
			o += [f"### {x['title']} · {x['rung']}", '', f"**Goal:** {x['goal']}", '', numbered(x['steps']), '', f"**Result:** {x['result']}", '']

	if d['worked_examples']:
		o += ['## Worked examples', '']
		for x in d['worked_examples']:
			o += [f"### {x['title']} · {x['rung']}", '', f"**Problem:** {x['problem']}", '', numbered(x['steps']), '']
			o += [f"**Answer:** {x['answer']}", '', f"**Takeaway:** {x['takeaway']}", '']

	o += ['## Teaching arc', '', numbered(f"**{s['step']}.** {s['move']} *Why:* {s['why']}" for s in d['teaching_arc']), '']

	if d['analogies']:
		o += ['## Analogies', '']
		for a in d['analogies']:
			o += [f"### {a['analogy']} · {a['rung']}", '', a['explanation'], '', '| In the analogy | Stands for |', '| --- | --- |']
			o += [f"| {cell(m['this'])} | {cell(m['stands_for'])} |" for m in a['mapping']]
			o += ['', f"*Limits:* {a['limits']}", '']

	if d['misconceptions']:
		o += ['## Misconceptions', '']
		for m in d['misconceptions']:
			o += [f"### “{m['belief']}” · {m['rung']}", '']
			o += [f"- **Why it is tempting:** {m['why_tempting']}", f"- **What is true:** {m['correction']}", f"- **Question that exposes it:** {m['diagnostic_question']}", '']

	o += ['## Checks', '']
	for i, c in enumerate(d['checks'], 1):
		target = f" *(targets: “{c['targets_misconception']}”)*" if c.get('targets_misconception') else ''
		o += [f"{i}. **{c['rung'].capitalize()}.** {c['question']}{target}", f"   - **Answer:** {c['answer']}"]
	o.append('')

	if d['notation_traps']:
		o += ['## Notation traps', '', '| Issue | Course choice | Variants you will meet |', '| --- | --- | --- |']
		o += [f"| {cell(t['issue'])} | {cell(t['course_choice'])} | {cell(t['variants'])} |" for t in d['notation_traps']]
		o.append('')

	if d['visuals']:
		o += ['## Visuals', '']
		for v in d['visuals']:
			star = '★ ' if v['priority'] == 'flagship' else ''
			o.append(f"- {star}[[{v['id']}]] ({v['priority']}): {v['role']}" + (f" *Sketch:* {v['sketch']}" if v.get('sketch') else ''))
		o.append('')

	t = d['tutor_moves']
	o += ['## Tutor moves', '', '**Open with**', '', *(f'- {q}' for q in t['opening_questions']), '']
	o += ['**If the learner is stuck**', '', *(f"- *{s['symptom']}* → {s['move']}" for s in t['if_stuck']), '']
	o += ['**Common questions**', '', *(f"- *{q['question']}* {q['answer']}" for q in t['common_questions']), '']
	if t['demo_moments']:
		o += ['**Demo moments**', '', *(f'- {m}' for m in t['demo_moments']), '']
	o += [f"**Saying it aloud:** {t['voice_notes']}", '', f"**Switching levels:** {t['level_switching']}", '']

	if d['history']:
		o += ['## History', '']
		for h in d['history']:
			work = f", *{h['work']}*" if h.get('work') else ''
			o.append(f"- **{', '.join(h['people'])} ({h['year']}){work}.** {h['contribution']}")
		o.append('')
	if d['research_horizon']:
		o += ['## Research horizon', '']
		for r in d['research_horizon']:
			ptr = f" *Pointers:* {'; '.join(r['pointers'])}" if r['pointers'] else ''
			o.append(f"- **{r['topic']}.** {r['connection']}{ptr}")
		o.append('')
	for stage in ('novice', 'physics'):
		r = review.get(stage)
		if r:
			o += [f'## Review: {stage}', '', f"**Verdict:** {r['verdict']}", '']
			o += ['**Fixes**', '', *(f'- {x}' for x in r['fixes'] or ['none']), '', '**Concerns**', '', *(f'- {x}' for x in r['concerns'] or ['none']), '']
	return '\n'.join(o)


def note_status(path):
	if not path.exists():
		return '—'
	try:
		d = json.loads(path.read_text())
	except json.JSONDecodeError:
		return 'invalid'
	if d.get('schema_version') != 2:
		return 'old draft'
	r = d.get('review') or {}
	return 'reviewed' if r.get('novice') and r.get('physics') else 'draft'


def write_indexes():
	taxonomy = json.loads((KB / 'concepts' / '_taxonomy.json').read_text())
	top = ['# Concepts\n', 'Generated from `_taxonomy.json` and each domain registry. Do not edit.\n']
	for dom in sorted(taxonomy['domains'], key=lambda x: x['order']):
		reg_file = KB / 'concepts' / dom['id'] / '_registry.json'
		if not reg_file.exists():
			continue
		reg = json.loads(reg_file.read_text())
		lines = [f"# {reg['title']}\n", reg['scope'] + '\n', '| Concept | Tier | Summary | Note |', '| --- | --- | --- | --- |']
		done = 0
		for c in reg['concepts']:
			status = note_status(KB / 'concepts' / dom['id'] / f"{c['id']}.json")
			done += status == 'reviewed'
			lines.append(f"| [[{c['id']}]] {c['title']} | {c['tier']} | {cell(c['summary'])} | {status} |")
		(KB / 'concepts' / dom['id'] / '_index.md').write_text('\n'.join(lines) + '\n')
		top.append(f"- **{reg['title']}** (`{dom['id']}`, {len(reg['concepts'])} concepts, {done} reviewed notes): {dom.get('scope', '')}")
	(KB / 'concepts' / '_index.md').write_text('\n'.join(top) + '\n')
	print('indexes written')


if __name__ == '__main__':
	if '--indexes' in sys.argv:
		write_indexes()
	else:
		for f in sys.argv[1:]:
			p = Path(f)
			p.with_suffix('.md').write_text(render(json.loads(p.read_text())))
			print('rendered', p.with_suffix('.md'))
