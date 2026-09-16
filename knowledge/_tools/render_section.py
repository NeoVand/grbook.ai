#!/usr/bin/env python3
"""Render a book section to Markdown beside it (authoring view: includes checks' answers, tutor lines and reviews).

Usage: python3 knowledge/_tools/render_section.py <book/sections/<chapter>/<id>.json> [...]
       python3 knowledge/_tools/render_section.py --index   (book/sections/_index.md over the outline)
"""
import json
import sys
from pathlib import Path

KB = Path(__file__).resolve().parents[1]


def render(d):
	o = [f"# {d['title']}", '', f"`{d['chapter']}/{d['id']}` · {d['track']} track · {d['depth']} depth · {d['status']} · revision {d['revision']} · {d['updated']}", '',
		'Teaches: ' + ', '.join(f'`{c}`' for c in d['teaches']), '', ('Builds on: ' + ', '.join(f'`{b}`' for b in d['builds_on'])) if d['builds_on'] else 'Builds on: nothing', '',
		f"**{d['summary']}**", '', d['opening'], '']
	for p in d['parts']:
		o += [f"## {p['heading']}", '', p['text'], '', f"*{p['takeaway']}*", '']
	if d['key_equations']:
		o += ['## Key equations', '']
		for e in d['key_equations']:
			o += [f"**{e['name']}** ({e['justified']})", '', f"$${e['latex']}$$", '', e['meaning'], '', *(f"- ${s['symbol']}$: {s['meaning']}" for s in e['symbols']), '', f"Say: {e['say_aloud']}", '']
	if d['worked_examples']:
		o += ['## Worked examples', '']
		for x in d['worked_examples']:
			o += [f"**{x['id']}.** {x['problem']}", '', *(f'{i}. {s}' for i, s in enumerate(x['steps'], 1)), '', f"Answer: {x['answer']}", '', f"*{x['takeaway']}*", '']
	o += ['## Checks', '']
	for c in d['checks']:
		o += [f"**{c['id']}** ({c['format']}): {c['question']}", '', f"Answer: {c['answer']}", '', 'Key points: ' + '; '.join(c['key_points']), '']
		if c['numeric']:
			o += ['Numeric: ' + '; '.join(f"{n['quantity']} = {n['value']} {n['unit'] or ''}" for n in c['numeric']), '']
	if d['misconceptions']:
		o += ['## Misconceptions', '', *(f"- **{m['id']}**: \"{m['belief']}\" — {m['correction']} (diagnosed by {', '.join(m['diagnosed_by'])})" for m in d['misconceptions']), '']
	if d['glossary']:
		o += ['## Glossary', '', *(f"- **{g['term']}**: {g['plain_definition']}" + (f" (`{g['concept']}`)" if g['concept'] else '') for g in d['glossary']), '']
	if d['visuals']:
		o += ['## Visuals', '', *(f"- `{v['id']}` ({v['priority']}): {v['role']}" + (f" Sketch: {v['sketch']}" if v['sketch'] else '') for v in d['visuals']), '']
	o += ['## Tutor', '', f"Opening question: {d['tutor']['opening_question']}", '', *(f"- Q: {q['question']} A: {q['answer']}" for q in d['tutor']['common_questions']), '']
	if d['further']:
		o += ['## Further', '', *(f"- **{f['topic']}.** {f['note']} " + '; '.join(f"{', '.join(r['authors'])} ({r['year']}), {r['title']}" for r in f['references']) for f in d['further']), '']
	rv = d.get('review') or {}
	for stage in ('novice', 'physics'):
		r = rv.get(stage)
		if r:
			o += [f'## Review: {stage}', '', f"Verdict {r['verdict']} ({r['date']}, revision {r['reviewed_revision']})", '']
			if stage == 'novice':
				o += [f"Retell attempt: {r['retell_attempt']}", '', f"{len(r['stumbles'])} stumbles", '', *(f"- “{s['quote']}”: {s['problem']}" for s in r['stumbles']), '']
			else:
				o += [f"{len(r['verification'])} verification items, {len(r['counterexamples'])} counterexamples", '', *(f"- {v['claim']}: {v['result']}" for v in r['verification']), '']
			o += ['Fixes:', *(f'- {x}' for x in r['fixes'] or ['none']), '', 'Concerns:', *(f'- {x}' for x in r['concerns'] or ['none']), '']
	return '\n'.join(o)


def index():
	out = json.loads((KB / 'book' / 'outline.json').read_text())
	o = ['# Book sections', '']
	n = 0
	for p in out['parts']:
		o += [f"## {p['title']}", '']
		for ch in p['chapters']:
			n += 1
			o += [f"### {n}. {ch['title']}", '', '| Section | Track | Depth | Status | Words |', '| --- | --- | --- | --- | --- |']
			for s in ch['sections']:
				f = KB / 'book' / 'sections' / ch['id'] / f"{s['id']}.json"
				if f.exists():
					d = json.loads(f.read_text())
					o.append(f"| [[{s['id']}]] {s['title']} | {s['track']} | {s['depth']} | {d['status']} (rev {d['revision']}) | {len(json.dumps(d).split())} |")
				else:
					o.append(f"| {s['title']} | {s['track']} | {s['depth']} | — | |")
			o.append('')
	(KB / 'book' / 'sections' / '_index.md').write_text('\n'.join(o))
	print('index written')


if __name__ == '__main__':
	if sys.argv[1:] == ['--index']:
		index()
	else:
		for f in sys.argv[1:]:
			p = Path(f)
			p.with_suffix('.md').write_text(render(json.loads(p.read_text())))
			print(f'rendered {p.with_suffix(".md")}')
