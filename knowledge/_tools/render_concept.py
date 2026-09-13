#!/usr/bin/env python3
"""Render concept note JSON into vault markdown, and write per-domain _index.md files.

Usage:
  python3 knowledge/_tools/render_concept.py <concepts/<domain>/<id>.json> [...]
  python3 knowledge/_tools/render_concept.py --indexes
The JSON is the source of truth; never edit generated .md files by hand.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
KB = ROOT / 'knowledge'


def bullets(items):
	return '\n'.join(f'- {x}' for x in items) if items else '_None recorded._'


def refs(rs):
	return f" *({'; '.join(rs)})*" if rs else ''


def link(l):
	return f"[[{l['id']}]] — {l['why']}"


def render(d):
	o = ['---']
	front = dict(
		type='concept',
		id=d['id'],
		title=d['title'],
		domain=d['domain'],
		tier=d['tier'],
		aliases=d.get('aliases', []),
		prerequisites=[l['id'] for l in d['prerequisites']],
		leads_to=[l['id'] for l in d['leads_to']],
		sources=sorted({f"{s['source']}:{s['unit']}" for s in d['sources']}),
		review=(d.get('review') or {}).get('verdict'),
	)
	o += [f'{k}: {json.dumps(v, ensure_ascii=False)}' for k, v in front.items()]
	o += ['---', '', f"# {d['title']}", '', f"> {d['summary']}", '']

	o.append('## Explanations by level\n')
	for name in ('intuition', 'working', 'formal'):
		lvl = d['levels'][name]
		o.append(f'### {name.capitalize()}\n')
		o.append(lvl['explanation'] + '\n')
		if lvl.get('picture'):
			o.append(f"**Picture to hold:** {lvl['picture']}\n")
		if lvl.get('assumes'):
			o.append('**Assumes:** ' + ', '.join(f'[[{a}]]' for a in lvl['assumes']) + '\n')

	o.append('## Prerequisites\n\n' + bullets([link(l) for l in d['prerequisites']]) + '\n')
	o.append('## Leads to\n\n' + bullets([link(l) for l in d['leads_to']]) + '\n')
	if d.get('related'):
		o.append('## Related\n\n' + bullets([link(l) for l in d['related']]) + '\n')

	o.append('## Key equations\n')
	for e in d['key_equations']:
		o.append(f"### {e['name']}\n\n$$\n{e['latex']}\n$$\n\n{e['meaning']}{refs(e['refs'])}\n")
		if e.get('convention_note'):
			o.append(f"**Convention:** {e['convention_note']}\n")
	if d['conventions']:
		o.append('## Conventions across the books\n')
		o.append('| Issue | Schutz | Gifted Amateur | d\'Inverno | Course choice |\n| --- | --- | --- | --- | --- |')
		for c in d['conventions']:
			cells = [c['issue'], c['schutz'] or '—', c['gifted_amateur'] or '—', c['dinverno'] or '—', c['course_choice']]
			o.append('| ' + ' | '.join(x.replace('|', '\\|') for x in cells) + ' |')
		o.append('')

	o.append('## How the sources teach it\n')
	for t in d['how_books_teach']:
		o.append(
			f"### {t['source']}\n\n**Route:** {t['route']}\n\n**Representation:** {t['representation']}\n\n"
			f"**Strengths:** {t['strengths']}\n\n**Weaknesses:** {t['weaknesses']}{refs(t['refs'])}\n"
		)
	o.append('## Recommended teaching path\n')
	for i, s in enumerate(d['recommended_teaching_path'], 1):
		o.append(f"{i}. **{s['step']}** — {s['move']} *Why:* {s['why']}{refs(s.get('inspired_by', []))}")
	o.append('')

	o.append('## Analogies\n')
	o.append(bullets([f"**{a['analogy']}** ({a['level']}): {a['explanation']} *Limits:* {a['limits']}{refs(a['refs'])}" for a in d['analogies']]) + '\n')
	o.append('## Misconceptions\n')
	o.append(
		bullets(
			[
				f"**{m['misconception']}** — {m['correction']}"
				+ (f" *Why tempting:* {m['why_tempting']}" if m.get('why_tempting') else '')
				+ f" *Diagnostic:* {m['diagnostic_question']}{refs(m['refs'])}"
				for m in d['misconceptions']
			]
		)
		+ '\n'
	)
	if d.get('thought_experiments'):
		o.append('## Thought experiments\n')
		o.append(bullets([f"**{t['name']}**: {t['setup']} *Lesson:* {t['lesson']}{refs(t['refs'])}" for t in d['thought_experiments']]) + '\n')

	o.append('## Visualizations\n')
	for v in d['visualizations']:
		o.append(f"### {v['title']} · {v['form']} · {v['priority']} priority\n\n{v['idea']}\n\n**Interaction:** {v['interaction']}\n")
		if v.get('physics_model'):
			o.append(f"**Model:** {v['physics_model']}\n")
		if v.get('inspired_by'):
			o.append(f"**Inspired by:** {'; '.join(v['inspired_by'])}\n")
		if v.get('legacy_assets'):
			o.append(f"**Legacy assets:** {', '.join(v['legacy_assets'])}\n")

	o.append('## Worked examples\n')
	o.append(bullets([f"**{w['title']}** ({w['level']}): {w['what_it_shows']}{refs(w['refs'])}" for w in d['worked_examples']]) + '\n')
	if d.get('exercises'):
		o.append('## Exercises\n')
		o.append(bullets([f"({x['difficulty']}) {x['summary']} *Skill:* {x['skill']}{refs(x['refs'])}" for x in d['exercises']]) + '\n')
	o.append('## Checks for understanding\n')
	for c in d['checks_for_understanding']:
		target = f" *(targets: {c['targets_misconception']})*" if c.get('targets_misconception') else ''
		o.append(f"- **Q ({c['level']}):** {c['question']}\n  - **A:** {c['answer']}{target}")
	o.append('')
	if d.get('applications'):
		o.append('## Applications\n')
		o.append(bullets([f"**{a['topic']}**: {a['details']}" + (f" Key numbers: {a['key_numbers']}" if a.get('key_numbers') else '') + refs(a['refs']) for a in d['applications']]) + '\n')
	if d.get('history'):
		o.append('## History\n')
		o.append(bullets([f"**{', '.join(h['people'])}{' (' + h['year'] + ')' if h.get('year') else ''}:** {h['note']}{refs(h.get('refs', []))}" for h in d['history']]) + '\n')

	g = d['tutor_guidance']
	o.append('## Tutor guidance\n')
	o.append('**Opening questions**\n\n' + bullets(g['opening_questions']) + '\n')
	o.append('**Common questions**\n\n' + bullets([f"*{q['question']}* — {q['answer']}" for q in g['common_questions']]) + '\n')
	o.append('**Pitfalls when explaining**\n\n' + bullets(g['explaining_pitfalls']) + '\n')
	o.append('**When to show a demo**\n\n' + bullets(g['demo_moments']) + '\n')
	if g.get('voice_notes'):
		o.append(f"**Saying it aloud:** {g['voice_notes']}\n")

	o.append('## Sources\n')
	for s in d['sources']:
		locs = ', '.join(f"p.{l.get('printed_page')}" + (f" §{l['section']}" if l.get('section') else '') for l in s.get('locators', []))
		o.append(f"- {s['source']} {s['unit']} ({s['depth']}){': ' + locs if locs else ''}")
	o.append('')
	r = d.get('review')
	if r:
		o.append(f"## Review\n\n**Verdict:** {r['verdict']}\n\n**Fixes**\n\n{bullets(r['fixes'])}\n\n**Concerns**\n\n{bullets(r['concerns'])}\n")
	return '\n'.join(o)


def write_indexes():
	taxonomy = json.loads((KB / 'concepts' / '_taxonomy.json').read_text())
	top = ['# Concepts\n', 'Generated from `_taxonomy.json` and each domain registry. Do not edit.\n']
	for dom in taxonomy['domains']:
		reg_file = KB / 'concepts' / dom['id'] / '_registry.json'
		if not reg_file.exists():
			continue
		reg = json.loads(reg_file.read_text())
		lines = [f"# {reg['title']}\n", reg['scope'] + '\n', '| Concept | Tier | Summary | Note |', '| --- | --- | --- | --- |']
		for c in reg['concepts']:
			has_note = (KB / 'concepts' / dom['id'] / f"{c['id']}.json").exists()
			lines.append(f"| [[{c['id']}]] {c['title']} | {c['tier']} | {c['summary'].replace('|', '/')} | {'yes' if has_note else '—'} |")
		(KB / 'concepts' / dom['id'] / '_index.md').write_text('\n'.join(lines) + '\n')
		top.append(f"- **{reg['title']}** (`{dom['id']}`, {len(reg['concepts'])} concepts): {dom.get('scope', '')}")
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
