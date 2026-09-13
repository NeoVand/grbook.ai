#!/usr/bin/env python3
"""Gather every piece of dossier and legacy evidence about one concept, for writing its concept note.

Usage:
  python3 knowledge/_tools/concept_evidence.py --id <concept-id>
  python3 knowledge/_tools/concept_evidence.py --names "Riemann curvature tensor" "Riemann tensor"

With --id, names come from the concept's registry entry (title, aliases, merged_from, source names) in
knowledge/concepts/*/_registry.json. Matching is by normalized name; free-text fields match multi-word names.
Prints markdown grouped by evidence type with compact references (e.g. "SCH ch05 §5.3 p.125").
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from collect_concept_candidates import normalize  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
KB = ROOT / 'knowledge'
SHORT = {'schutz': 'SCH', 'gifted-amateur': 'GA', 'dinverno': 'DIV'}


def ref(book, unit, loc=None, label=None):
	parts = [SHORT[book], unit]
	if label:
		parts.append(label)
	if loc:
		if loc.get('section'):
			parts.append(f"§{loc['section']}")
		if loc.get('printed_page') is not None:
			parts.append(f"p.{loc['printed_page']}")
	return ' '.join(parts)


def registry_names(concept_id):
	for f in sorted((KB / 'concepts').glob('*/_registry.json')):
		for c in json.loads(f.read_text())['concepts']:
			if c['id'] == concept_id:
				names = {c['title'], *c['aliases'], *c['merged_from']}
				for s in c['sources']:
					names.update(s['names'])
				return c, names
	return None, set()


def main(argv):
	if '--id' in argv:
		entry, names = registry_names(argv[argv.index('--id') + 1])
		if not entry:
			print('Concept id not found in any _registry.json')
			return 1
		print(f"# Evidence for {entry['id']}: {entry['title']}\n\nRegistry summary: {entry['summary']}\n")
	elif '--names' in argv:
		names = set(argv[argv.index('--names') + 1 :])
		entry = None
		print(f"# Evidence for {sorted(names)}\n")
	else:
		print(__doc__)
		return 1

	keys = {normalize(n) for n in names if n.strip()}
	phrases = {k for k in keys if len(k.split()) >= 2}

	def hit(name):
		return bool(name) and normalize(name) in keys

	def mentions(text):
		t = normalize(text or '')
		return any(f' {p} ' in f' {t} ' for p in phrases)

	out = {k: [] for k in ('definitions', 'equations', 'figures', 'examples', 'analogies', 'misconceptions', 'thought', 'gems', 'gaps', 'exercises', 'legacy')}
	for book in SHORT:
		for f in sorted((KB / 'sources' / book / 'chapters').glob('*.json')):
			d = json.loads(f.read_text())
			u = d['unit_id']
			for c in d['concepts']:
				if hit(c['name']) or any(hit(a) for a in c['aliases']):
					locs = '; '.join(ref(book, u, l) for l in c['locators'])
					out['definitions'].append(
						f"- **{c['name']}** ({SHORT[book]} {u}, {c['kind']}, {c['depth']}; {locs})\n"
						f"  - Definition: {c['definition']}\n  - Introduced: {c['how_introduced']}\n"
						f"  - Prerequisites: {', '.join(c['prerequisites']) or 'none listed'}"
						+ (f"\n  - Formulas: {' ; '.join(c['formulas'])}" if c['formulas'] else '')
						+ (f"\n  - Notes: {c['notes']}" if c.get('notes') else '')
					)
			for e in d['key_equations']:
				if hit(e.get('name')) or mentions(e.get('name')) or mentions(e['meaning']):
					out['equations'].append(f"- {ref(book, u, e['locator'], e.get('label'))} {e.get('name') or ''}: `{e['latex']}` — {e['meaning']}")
			for x in d['figures']:
				if any(hit(c) for c in x['concepts']) or mentions(x['what_it_teaches']):
					r = x['redesign']
					out['figures'].append(
						f"- {ref(book, u, x['locator'], x.get('label'))} [{x['figure_type']}] image `{x.get('image_path')}`: {x['visual_description']} "
						f"Teaches: {x['what_it_teaches']} Redesign ({r['form']}, {r['priority']}): {r['idea']} Interaction: {r['interaction']}"
					)
			for x in d['worked_examples']:
				if any(hit(c) for c in x['concepts']) or mentions(x['problem']):
					out['examples'].append(f"- {ref(book, u, x['locator'], x.get('label'))} ({x['difficulty']}): {x['problem']} Method: {x['method']} Insight: {x['key_insight']}")
			for x in d['analogies_and_intuitions']:
				if hit(x['target_concept']) or mentions(x['target_concept']):
					out['analogies'].append(f"- {ref(book, u, x['locator'])} ({x['effectiveness']}) **{x['analogy']}**: {x['how_used']} Limits: {x['limits']}")
			for x in d['misconceptions_addressed']:
				if any(hit(c) for c in x['concepts']) or mentions(x['misconception']):
					out['misconceptions'].append(f"- {ref(book, u, x['locator'])}: **{x['misconception']}** Correction: {x['correction']} Why tempting: {x['why_tempting']}")
			for x in d['thought_experiments']:
				if any(hit(c) for c in x['concepts']):
					out['thought'].append(f"- {ref(book, u, x['locator'])} **{x['name']}**: {x['setup']} Lesson: {x['lesson']}")
			for x in d['teaching_gems']:
				if mentions(x['gem']) or mentions(x['app_idea']):
					out['gems'].append(f"- {ref(book, u, x['locator'])}: {x['gem']} Why: {x['why_effective']} App idea: {x['app_idea']}")
			for x in d['gaps_and_pitfalls']:
				if mentions(x['issue']) or mentions(x['impact_on_learner']):
					out['gaps'].append(f"- {SHORT[book]} {u}: {x['issue']} Impact: {x['impact_on_learner']} Suggestion: {x['suggestion']}")
			for x in d['exercises']['notable']:
				if mentions(x['summary']) or any(mentions(s) or hit(s) for s in x['skills']):
					out['exercises'].append(f"- {SHORT[book]} {u} Ex {x['number']} ({x['difficulty']}): {x['summary']}")

	for f in sorted((KB / 'sources' / 'legacy').glob('*.json')):
		for a in json.loads(f.read_text()).get('assets', []):
			if any(hit(t) or mentions(t) for t in a['topics']) or mentions(a['title']):
				out['legacy'].append(
					f"- legacy:{a['id']} ({a['kind']}, {a['quality']['status']}, verdict {a['reuse']['verdict']}): {a['title']} — {a['teaches']} Reuse: {a['reuse']['notes']}"
				)

	titles = {
		'definitions': 'Definitions and introductions',
		'equations': 'Equations',
		'figures': 'Figures and redesign ideas',
		'examples': 'Worked examples',
		'analogies': 'Analogies and intuitions',
		'misconceptions': 'Misconceptions',
		'thought': 'Thought experiments',
		'gems': 'Teaching gems mentioning it',
		'gaps': 'Gaps and pitfalls mentioning it',
		'exercises': 'Notable exercises',
		'legacy': 'Legacy project assets',
	}
	for k, title in titles.items():
		print(f'\n## {title} ({len(out[k])})\n')
		print('\n'.join(out[k]) if out[k] else '_None found._')
	return 0


if __name__ == '__main__':
	sys.exit(main(sys.argv))
