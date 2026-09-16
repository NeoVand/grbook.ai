#!/usr/bin/env python3
"""Write knowledge/_meta/exemplar-excerpt.json: the holonomy exemplar with every field but only 1-3 items per list.

Usage: python3 knowledge/_tools/make_exemplar_excerpt.py

Agents read the excerpt (about a fifth of the full note) to see the shape and standard of every field. The excerpt is
not schema-valid (it carries a leading "_excerpt" key, and trimmed lists leave dangling ids). Regenerate it whenever
concepts/curvature/holonomy.json changes.
"""
import json
from pathlib import Path

KB = Path(__file__).resolve().parents[1]
SRC = KB / 'concepts' / 'curvature' / 'holonomy.json'
OUT = KB / '_meta' / 'exemplar-excerpt.json'
KEEP = dict(aliases=2, objectives=2, glossary=2, pronunciations=1, prerequisites=2, leads_to=1, related=1, key_equations=1, derivations=1,
	worked_examples=1, problems=1, observations=1, teaching_arc=2, analogies=1, misconceptions=2, checks=2, notation_traps=1, visuals=1, history=1, research_horizon=1)


def first_per_rung(items, rungs):
	out = []
	for r in rungs:
		for x in items:
			if x['rung'] == r:
				out.append(x)
				break
	return out


def main():
	d = json.loads(SRC.read_text())
	e = {'_excerpt': 'Excerpt of concepts/curvature/holonomy.json: every field, 1 to 3 items per list, ids left dangling. Not schema-valid. Regenerate with _tools/make_exemplar_excerpt.py.'}
	for k, v in d.items():
		if k == 'ways_in':
			e[k] = first_per_rung(v, ('entry', 'working', 'formal'))
		elif k == 'checks':
			e[k] = first_per_rung(v, ('entry', 'formal'))
		elif k == 'tutor_moves':
			e[k] = {kk: (vv[:1] if isinstance(vv, list) else vv) for kk, vv in v.items()}
		elif k == 'review':
			e[k] = {}
			for stage, r in v.items():
				rr = dict(r)
				for lk in ('stumbles', 'verification', 'counterexamples', 'fixes', 'concerns'):
					if lk in rr:
						rr[lk] = rr[lk][:2]
				for lk in ('rereads', 'diff_checks'):
					if lk in rr:
						rr[lk] = [dict(x, **{s: x[s][:1] for s in ('stumbles', 'verification', 'fixes', 'read') if s in x}) for x in rr[lk][:1]]
				e[k][stage] = rr
		elif k in KEEP and isinstance(v, list):
			e[k] = v[: KEEP[k]]
		else:
			e[k] = v
	OUT.write_text(json.dumps(e, indent='\t', ensure_ascii=False) + '\n')
	print(f'wrote {OUT.relative_to(KB.parent)}: {len(OUT.read_text().split())} words (full note {len(SRC.read_text().split())})')


if __name__ == '__main__':
	main()
