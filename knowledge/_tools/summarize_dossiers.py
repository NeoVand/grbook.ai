#!/usr/bin/env python3
"""Print a compact digest of every chapter dossier for one book, for book-level synthesis.

Usage: python3 knowledge/_tools/summarize_dossiers.py <book> [--full-concepts]
Prints, per unit: summary, role, teaching approach, difficulty, concept names, notation, analogies,
misconceptions, thought experiments, teaching gems, gaps, and verification verdict. Units without a dossier are listed.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
KB = ROOT / 'knowledge'


def main(argv):
	if len(argv) < 2:
		print(__doc__)
		return 1
	book = argv[1]
	toc = json.loads((KB / 'sources' / book / 'toc.json').read_text())
	missing = []
	for u in toc['units']:
		if u['kind'] == 'front-matter' or not u.get('read'):
			continue
		f = KB / 'sources' / book / 'chapters' / f"{u['id']}.json"
		if not f.exists():
			missing.append(u['id'])
			continue
		d = json.loads(f.read_text())
		t, diff = d['teaching_approach'], d['difficulty']
		print(f"\n## {u['id']} {d['title']} (printed {d['printed_pages'][0]}-{d['printed_pages'][-1]}; part {d.get('part')})")
		print(f"Summary: {d['one_line_summary']}")
		print(f"Role: {d['role_in_book']}")
		print(f"Approach: {t['summary']}")
		print(f"Style: {', '.join(t['style_tags'])}")
		print('Signature moves: ' + ' | '.join(t['signature_moves']))
		print(f"Difficulty: math {diff['math_level']}, conceptual {diff['conceptual_level']}, novice {diff['novice_friendliness']}. {diff['notes']}")
		print('Background: ' + '; '.join(f"{b['topic']} ({b['source']})" for b in d['assumed_background']))
		print('Concepts: ' + '; '.join(f"{c['name']} [{c['depth']}]" for c in d['concepts']))
		if '--full-concepts' in argv:
			for c in d['concepts']:
				print(f"  - {c['name']}: {c['definition']} | introduced: {c['how_introduced']}")
		print('Notation: ' + '; '.join(f"{n['item']}: {n['convention']}" for n in d['notation_and_conventions']))
		print('Analogies: ' + '; '.join(f"{a['analogy']} -> {a['target_concept']} ({a['effectiveness']})" for a in d['analogies_and_intuitions']))
		print('Thought experiments: ' + '; '.join(x['name'] for x in d['thought_experiments']))
		print('Misconceptions: ' + '; '.join(m['misconception'] for m in d['misconceptions_addressed']))
		print('Figures: ' + '; '.join(f"{x.get('label')}: {x['figure_type']} ({x['redesign']['priority']})" for x in d['figures']))
		print(f"Worked examples: {len(d['worked_examples'])}; exercises ~{d['exercises']['count_estimate']}: " + ', '.join(d['exercises']['skills_practiced']))
		print('Gems: ' + ' | '.join(g['gem'] for g in d['teaching_gems']))
		print('Gaps: ' + ' | '.join(g['issue'] for g in d['gaps_and_pitfalls']))
		print('Cross-references: ' + '; '.join(f"{c['direction']} {c['target']}" for c in d['cross_references']))
		print(f"Verification: {(d.get('verification') or {}).get('verdict')}")
	if missing:
		print(f"\nUnits without a dossier: {', '.join(missing)}")
	return 0


if __name__ == '__main__':
	sys.exit(main(sys.argv))
