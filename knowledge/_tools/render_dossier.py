#!/usr/bin/env python3
"""Render chapter dossier JSON into readable vault notes.

Usage: python3 knowledge/_tools/render_dossier.py <dossier.json> [...]
Writes <dossier>.md next to each JSON file. The JSON stays the source of truth; never edit the .md by hand.
"""
import json
import sys
from pathlib import Path

SHORT = {'schutz': 'SCH', 'gifted-amateur': 'GA', 'dinverno': 'DIV'}


def loc(book, l):
	if not l:
		return ''
	sec = f"§{l['section']} " if l.get('section') else ''
	printed = f"p.{l['printed_page']}" if l.get('printed_page') is not None else 'p.?'
	return f"{SHORT[book]} {sec}{printed} (pdf {l['pdf_page']})"


def bullets(items):
	return '\n'.join(f'- {x}' for x in items) if items else '_None recorded._'


def yaml_value(v):
	return json.dumps(v, ensure_ascii=False)


def render(d):
	b = d['book']
	out = []
	concept_names = [c['name'] for c in d['concepts']]
	front = {
		'type': 'source-unit',
		'book': b,
		'book_short': SHORT[b],
		'unit': d['unit_id'],
		'title': d['title'],
		'part': d.get('part'),
		'printed_pages': d['printed_pages'],
		'pdf_pages': d['pdf_pages'],
		'math_level': d['difficulty']['math_level'],
		'conceptual_level': d['difficulty']['conceptual_level'],
		'novice_friendliness': d['difficulty']['novice_friendliness'],
		'style_tags': d['teaching_approach']['style_tags'],
		'concepts': concept_names,
		'verification': (d.get('verification') or {}).get('verdict'),
	}
	out.append('---')
	out += [f'{k}: {yaml_value(v)}' for k, v in front.items()]
	out.append('---\n')
	out.append(f"# {SHORT[b]} {d['unit_id']} · {d['title']}\n")
	out.append(f"> {d['one_line_summary']}\n")
	pp, pdf = d['printed_pages'], d['pdf_pages']
	diff = d['difficulty']
	out.append(
		f"**Pages:** printed {pp[0]}–{pp[-1]} · pdf {pdf[0]}–{pdf[-1]} · **Difficulty:** math {diff['math_level']}/5, "
		f"conceptual {diff['conceptual_level']}/5, novice-friendliness {diff['novice_friendliness']}/5\n"
	)
	out.append(f"{diff['notes']}\n")

	out.append('## Role in the book\n')
	out.append(d['role_in_book'] + '\n')
	out.append('## Learning objectives\n')
	out.append(bullets(d['learning_objectives']) + '\n')
	out.append('## Assumed background\n')
	out.append(bullets([f"{x['topic']} — {x['source']}" + (f" ({x['where']})" if x.get('where') else '') for x in d['assumed_background']]) + '\n')

	t = d['teaching_approach']
	out.append('## Teaching approach\n')
	out.append(t['summary'] + '\n')
	out.append(f"**Style:** {', '.join(t['style_tags'])}\n")
	out.append('**Narrative arc**\n')
	out.append('\n'.join(f'{i}. {s}' for i, s in enumerate(t['narrative_arc'], 1)) + '\n')
	out.append('**Signature moves**\n')
	out.append(bullets(t['signature_moves']) + '\n')

	out.append('## Section by section\n')
	for s in d['sections']:
		num = f"§{s['number']} " if s.get('number') else ''
		out.append(f"### {num}{s['title']} — p.{s.get('printed_page')} (pdf {s['pdf_page']})\n")
		out.append(s['summary'] + '\n')
		if s['concepts']:
			out.append(f"**Concepts:** {', '.join(s['concepts'])}\n")
		if s['key_moves']:
			out.append('**Key moves**\n' + bullets(s['key_moves']) + '\n')

	out.append('## Concepts\n')
	for c in d['concepts']:
		out.append(f"### {c['name']}\n")
		meta = f"*{c['kind']} · {c['depth']}*"
		if c['aliases']:
			meta += f" · also: {', '.join(c['aliases'])}"
		out.append(meta + '\n')
		out.append(c['definition'] + '\n')
		out.append(f"**How introduced:** {c['how_introduced']}\n")
		if c['prerequisites']:
			out.append(f"**Prerequisites:** {', '.join(c['prerequisites'])}\n")
		for f in c['formulas']:
			out.append(f'$$\n{f}\n$$\n')
		if c.get('notes'):
			out.append(f"**Notes:** {c['notes']}\n")
		out.append(f"**Where:** {'; '.join(loc(b, l) for l in c['locators'])}\n")

	out.append('## Key equations\n')
	for e in d['key_equations']:
		name = ' '.join(x for x in [e.get('label'), e.get('name')] if x) or 'Equation'
		out.append(f"### {name} · {e['importance']} · {loc(b, e['locator'])}\n")
		out.append(f"$$\n{e['latex']}\n$$\n")
		out.append(e['meaning'] + '\n')
		if e.get('symbols'):
			out.append(f"**Symbols:** {e['symbols']}\n")

	out.append('## Figures\n')
	for f in d['figures']:
		r = f['redesign']
		out.append(f"### {f.get('label') or 'Unlabelled figure'} · {f['figure_type']} · {loc(b, f['locator'])}\n")
		if f.get('image_path'):
			out.append(f"`book-sources/{f['image_path']}`\n")
		out.append(f"**Caption (paraphrased):** {f['caption_paraphrase']}\n")
		out.append(f"**What it shows:** {f['visual_description']}\n")
		out.append(f"**What it teaches:** {f['what_it_teaches']}\n")
		if f['concepts']:
			out.append(f"**Concepts:** {', '.join(f['concepts'])}\n")
		out.append(f"**App redesign ({r['form']}, {r['priority']} priority):** {r['idea']} — *Interaction:* {r['interaction']}\n")

	def section(title, items, fmt):
		out.append(f'## {title}\n')
		out.append('\n'.join(fmt(x) for x in items) + '\n' if items else '_None recorded._\n')

	section(
		'Worked examples',
		d['worked_examples'],
		lambda x: f"### {x.get('label') or 'Example'} · {x['difficulty']} · {loc(b, x['locator'])}\n\n"
		f"**Problem:** {x['problem']}\n\n**Method:** {x['method']}\n\n**Key insight:** {x['key_insight']}\n"
		+ (f"\n**Result:** {x['result']}\n" if x.get('result') else '')
		+ (f"\n**Concepts:** {', '.join(x['concepts'])}\n" if x['concepts'] else ''),
	)
	section(
		'Analogies and intuitions',
		d['analogies_and_intuitions'],
		lambda x: f"### {x['analogy']} → {x['target_concept']} · {x['effectiveness']} · {loc(b, x['locator'])}\n\n"
		f"{x['how_used']}\n\n**Where it breaks down:** {x['limits']}\n"
		+ (f"\n**App idea:** {x['app_idea']}\n" if x.get('app_idea') else ''),
	)
	section(
		'Misconceptions addressed',
		d['misconceptions_addressed'],
		lambda x: f"### {x['misconception']} · {loc(b, x['locator'])}\n\n**Correction:** {x['correction']}\n\n"
		f"**Why tempting:** {x['why_tempting']}\n"
		+ ('' if x.get('explicit_in_book', True) else '\n*Inferred: the book guards against this implicitly.*\n'),
	)
	section(
		'Thought experiments',
		d['thought_experiments'],
		lambda x: f"### {x['name']} · {loc(b, x['locator'])}\n\n**Setup:** {x['setup']}\n\n**Lesson:** {x['lesson']}\n"
		+ (f"\n**App idea:** {x['app_idea']}\n" if x.get('app_idea') else ''),
	)
	section(
		'Applications and observations',
		d['applications_and_observations'],
		lambda x: f"- **{x['topic']}** ({x['kind']}, {loc(b, x['locator'])}): {x['details']}"
		+ (f" Key numbers: {x['key_numbers']}" if x.get('key_numbers') else ''),
	)
	section(
		'Historical notes',
		d['historical_notes'],
		lambda x: f"- **{', '.join(x['people']) or 'History'}{' (' + x['year'] + ')' if x.get('year') else ''}:** "
		f"{x['event']} — {x['significance']} ({loc(b, x['locator'])})",
	)
	section(
		'Notation and conventions',
		d['notation_and_conventions'],
		lambda x: f"- **{x['item']}:** {x['convention']}" + (f" — {x['notes']}" if x.get('notes') else '') + f" ({loc(b, x['locator'])})",
	)
	section('Margin notes', d['margin_notes'], lambda x: f"- *{x['type']}* — {x['summary']} ({loc(b, x['locator'])})")

	ex = d['exercises']
	out.append('## Exercises\n')
	out.append(f"About {ex['count_estimate']} exercises (pdf pages {', '.join(map(str, ex['pdf_pages'])) or 'n/a'}).\n")
	if ex.get('solutions'):
		out.append(f"**Solutions:** {ex['solutions']}\n")
	out.append('**Skills practiced**\n' + bullets(ex['skills_practiced']) + '\n')
	for n in ex['notable']:
		out.append(f"- **{n['number']}** ({n['difficulty']}): {n['summary']} — *{n['why_notable']}* Skills: {', '.join(n['skills'])}")
	out.append('')

	section(
		'Cross-references',
		d['cross_references'],
		lambda x: f"- *{x['direction']}* → **{x['target']}**: {x['reason']}",
	)
	section(
		'Teaching gems',
		d['teaching_gems'],
		lambda x: f"### {x['gem']} · {loc(b, x['locator'])}\n\n**Why it works:** {x['why_effective']}\n\n**App idea:** {x['app_idea']}\n",
	)
	section(
		'Gaps and pitfalls',
		d['gaps_and_pitfalls'],
		lambda x: f"- **{x['issue']}** — {x['impact_on_learner']} *Suggestion:* {x['suggestion']}",
	)
	out.append('## Tutor notes\n')
	out.append(bullets(d['tutor_notes']) + '\n')

	v = d.get('verification')
	if v:
		out.append('## Verification\n')
		out.append(f"**Verdict:** {v['verdict']}\n")
		out.append('**Fixes applied**\n' + bullets(v['fixes']) + '\n')
		out.append('**Residual concerns**\n' + bullets(v['residual_concerns']) + '\n')
		if v.get('coverage'):
			out.append('**Coverage:** ' + ', '.join(f'{k}: {val}' for k, val in v['coverage'].items()) + '\n')
	return '\n'.join(out)


if __name__ == '__main__':
	for f in sys.argv[1:]:
		p = Path(f)
		p.with_suffix('.md').write_text(render(json.loads(p.read_text())))
		print('rendered', p.with_suffix('.md'))
