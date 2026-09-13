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
RUNGS = ('entry', 'working', 'formal', 'research')


def cell(s):
	return str(s if s is not None else '—').replace('|', '\\|').replace('\n', ' ')


def numbered(items, indent=''):
	return '\n'.join(f'{indent}{i}. {x}' for i, x in enumerate(items, 1))


def vis(v):
	return f"[[{v['id']}]]" + (f" (preset `{v['preset']}`)" if v.get('preset') else '')


def ref(r):
	title = f", *{r['title']}*" if r.get('title') else ''
	venue = f", {r['venue']}" if r.get('venue') else ''
	ident = f", doi:{r['doi']}" if r.get('doi') else (f", arXiv:{r['arxiv']}" if r.get('arxiv') else '')
	flag = '' if r['verified'] else ' _(unverified)_'
	return f"{', '.join(r['authors'])} ({r['year']}){title}{venue}{ident}{flag}"


def render(d):
	review = d.get('review') or {}
	front = dict(
		type='concept',
		schema_version=d['schema_version'],
		id=d['id'],
		title=d['title'],
		tagline=d['tagline'],
		domain=d['domain'],
		tier=d['tier'],
		status=d['status'],
		revision=d['revision'],
		updated=d['updated'],
		aliases=d['aliases'],
		prerequisites=[p['id'] for p in d['prerequisites']],
		leads_to=[x['id'] for x in d['leads_to']],
		visuals=[v['id'] for v in d['visuals']],
	)
	o = ['---', *(f'{k}: {json.dumps(v, ensure_ascii=False)}' for k, v in front.items()), '---', '']
	o += [f"# {d['title']}", '', f"*{d['tagline']}*", '', f"`{d['id']}` · {d['domain']} · {d['tier']} · {d['status']} (revision {d['revision']})", '']
	needs = ' · '.join(f"[[{p['id']}]] ({p['needed_for']})" for p in d['prerequisites'])
	o.append(f"**Needs:** {needs or 'nothing beyond everyday experience'}  ")
	if d['leads_to']:
		o.append('**Opens:** ' + ' · '.join(f"[[{x['id']}]]" for x in d['leads_to']) + '  ')
	if d['related']:
		o.append('**Related:** ' + ' · '.join(f"[[{x['id']}]]" for x in d['related']) + '  ')
	if d['visuals']:
		o.append('**Visuals:** ' + ' · '.join(('★ ' if v['priority'] == 'flagship' else '') + f"[[{v['id']}]]" for v in d['visuals']))
	o += ['', f"> {d['summary']}", '', '## You will be able to', '']
	for r in RUNGS:
		items = [x for x in d['objectives'] if x['rung'] == r]
		if items:
			o.append(f'**{r.capitalize()}**')
			o += [f"- {x['can_do']} `objectives/{x['id']}`" for x in items]
			o.append('')

	o += ['## Ways in', '']
	for i, w in enumerate(d['ways_in'], 1):
		o += [f"### {i}. {w['title']} · {w['rung']} · {w['kind']}", '', f"*{w['question']}*", '']
		if w.get('recap'):
			o += [f"**Recap:** {w['recap']}", '']
		o += [w['explanation'].strip(), '']
		if w.get('try_it'):
			o += [f"**Try it:** {w['try_it']}", '']
		o += [f"**Takeaway:** {w['takeaway']}", '']
		if w.get('picture'):
			o += [f"*Picture:* {w['picture']}", '']
		if w.get('simplifies'):
			o += [f"*What this leaves out:* {w['simplifies']}", '']
		meta = [f"*Gist:* {w['gist']}"]
		if w.get('retell'):
			meta.append(f"*Retell:* {w['retell']}")
		if w.get('continues'):
			meta.append(f"*Continues:* `ways_in/{w['continues']}`")
		if w['assumes']:
			meta.append('*Builds on:* ' + ', '.join(f'[[{a}]]' for a in w['assumes']))
		if w['visuals']:
			meta.append('*Visuals:* ' + ', '.join(vis(v) for v in w['visuals']))
		if w['refs']:
			meta.append('*See:* ' + ', '.join(f'`{r}`' for r in w['refs']))
		o += ['<br>'.join(meta), '']

	if d['glossary']:
		o += ['## Glossary', '', '| Term | Say | In plain words |', '| --- | --- | --- |']
		o += [f"| {cell(g['term'])} | {cell(g['say_as'])} | {cell(g['plain_definition'])} |" for g in d['glossary']]
		o.append('')

	if d['key_equations']:
		o += ['## Key equations', '']
		for e in d['key_equations']:
			o += [f"### {e['name']} · {e['rung']}", '', '$$', e['latex'], '$$', '', e['meaning'], '']
			o += ['| Symbol | Meaning | Say |', '| --- | --- | --- |']
			o += [f"| ${s['symbol']}$ | {cell(s['meaning'])} | {cell(s['say'])} |" for s in e['symbols']]
			o.append('')
			if e.get('conditions'):
				o.append(f"**Holds when:** {e['conditions']}  ")
			o += [f"**Say it:** “{e['say_aloud']}”  ", f"**Justified by:** `{e['justified_by']}`", '']

	if d['derivations']:
		o += ['## Derivations', '']
		for x in d['derivations']:
			o += [f"### {x['title']} · {x['rung']}", '', f"**Goal:** {x['goal']}", '', numbered(x['steps']), '', f"**Result:** {x['result']}", '']

	if d['worked_examples']:
		o += ['## Worked examples', '']
		for x in d['worked_examples']:
			o += [f"### {x['title']} · {x['rung']}", '', f"**Problem:** {x['problem']}", '', numbered(x['steps']), '']
			o += [f"**Answer:** {x['answer']}", '', f"**Takeaway:** {x['takeaway']}", '']

	if d['problems']:
		o += ['## Problems', '']
		for x in d['problems']:
			o += [f"### `{x['id']}` · {x['rung']} · difficulty {x['difficulty']} · {x['type']}", '', x['statement'], '']
			if x['hints']:
				o += ['**Hints**', '', numbered(x['hints']), '']
			o += [f"**Answer:** {x['answer']}", '', '**Solution**', '', numbered(x['solution']), '']

	if d['observations']:
		o += ['## Observations', '']
		for x in d['observations']:
			o.append(f"- **{x['phenomenon']}** ({x['status']}, {x['rung']}). {x['connection']}" + (f" *Numbers:* {x['numbers']}" if x.get('numbers') else '') + (f" *Reference:* {ref(x['reference'])}" if x.get('reference') else ''))
		o.append('')

	o += ['## Teaching arc', '']
	for i, s in enumerate(d['teaching_arc'], 1):
		extra = (f" *Predict:* {s['predict']}" if s.get('predict') else '') + (f" *Visual:* {vis(s['visual'])}" if s.get('visual') else '')
		o.append(f"{i}. **{s['step']}** ({s['rung']}). {s['move']} *Why:* {s['why']}{extra}")
	o.append('')

	if d['analogies']:
		o += ['## Analogies', '']
		for a in d['analogies']:
			o += [f"### {a['analogy']} · {a['rung']}", '', a['explanation'], '', '| In the analogy | Stands for |', '| --- | --- |']
			o += [f"| {cell(m['this'])} | {cell(m['stands_for'])} |" for m in a['mapping']]
			o += ['', f"*Limits:* {a['limits']}", '']

	if d['misconceptions']:
		o += ['## Misconceptions', '']
		for m in d['misconceptions']:
			o += [f"### “{m['belief']}” · {m['rung']} · `{m['id']}`", '']
			o += [f"- **Why it is tempting:** {m['why_tempting']}", f"- **What is true:** {m['correction']}", f"- **Exposed by:** " + ', '.join(f'`checks/{c}`' for c in m['diagnosed_by']), '']

	o += ['## Checks', '']
	for i, c in enumerate(d['checks'], 1):
		o.append(f"{i}. **{c['rung'].capitalize()} · {c['format']}** `checks/{c['id']}`. {c['question']}")
		if c['hints']:
			o.append('   - **Hints:** ' + ' / '.join(c['hints']))
		o.append(f"   - **Answer:** {c['answer']}")
		o.append('   - **Must contain:** ' + '; '.join(c['key_points']))
		if c['numeric']:
			o.append('   - **Numeric:** ' + '; '.join(f"{n['quantity']} = {n['value']} {n['unit']} (±{n['rel_tol'] * 100:g}%)" for n in c['numeric']))
		if c['targets']:
			o.append('   - **Targets:** ' + ', '.join(f'`{t}`' for t in c['targets']))
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
	o += ['## Tutor moves', '', '**Open with**', '', *(f"- {q['question']} *({q['invites']})*" for q in t['opening_questions']), '']
	o += ['**If the learner is stuck**', '', *(f"- *{s['symptom']}* → {s['move']}" for s in t['if_stuck']), '']
	o += ['**Common questions**', '', *(f"- *{q['question']}* ({q['rung']}) {q['answer']}" for q in t['common_questions']), '']
	o += ['**Switching levels**', '', *(f"- To {s['to_rung']} when: {'; '.join(s['signals'])}. {s['move']}" for s in t['level_switching']), '']
	if d['pronunciations']:
		o += ['**Pronunciations:** ' + '; '.join(f"{p['written']} → {p['spoken']}" for p in d['pronunciations']), '']
	if t.get('voice_notes'):
		o += [f"**Voice notes:** {t['voice_notes']}", '']

	if d['history']:
		o += ['## History', '']
		o += [f"- **{', '.join(h['people'])} ({h['year']}).** {h['contribution']}" + (f" {ref(h['work'])}" if h.get('work') else '') for h in d['history']]
		o.append('')
	if d['research_horizon']:
		o += ['## Research horizon', '']
		for r in d['research_horizon']:
			o.append(f"- **{r['topic']}.** {r['connection']}" + ('' if not r['references'] else ' ' + '; '.join(ref(x) for x in r['references'])))
		o.append('')

	nov, phy = review.get('novice'), review.get('physics')
	if nov:
		o += ['## Review: novice', '', f"**Verdict:** {nov['verdict']} ({nov['date']})", '', f"**Retell attempt:** {nov['retell_attempt']}", '']
		o += [f"**Stumbles ({len(nov['stumbles'])})**", '', *(f"- “{s['quote']}”: {s['problem']}" for s in nov['stumbles']), '']
		o += ['**Fixes**', '', *(f'- {x}' for x in nov['fixes'] or ['none']), '', '**Concerns**', '', *(f'- {x}' for x in nov['concerns'] or ['none']), '']
	if phy:
		o += ['## Review: physics', '', f"**Verdict:** {phy['verdict']} ({phy['date']})", '']
		o += ['**Verification**', '', *(f"- {v['claim']}: {v['method']} → {v['result']}" for v in phy['verification']), '']
		o += ['**Counterexamples tried**', '', *(f'- {x}' for x in phy['counterexamples'] or ['none']), '']
		o += ['**Fixes**', '', *(f'- {x}' for x in phy['fixes'] or ['none']), '', '**Concerns**', '', *(f'- {x}' for x in phy['concerns'] or ['none']), '']
	return '\n'.join(o)


def note_status(path):
	if not path.exists():
		return '—'
	try:
		d = json.loads(path.read_text())
	except json.JSONDecodeError:
		return 'invalid'
	return d.get('status', 'old draft') if d.get('schema_version') == 2 else 'old draft'


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
			done += status in ('physics-reviewed', 'published')
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
