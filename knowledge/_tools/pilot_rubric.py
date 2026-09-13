#!/usr/bin/env python3
"""Measure consistency across schema v2 concept notes (for pilots before scaling).

Usage: python3 knowledge/_tools/pilot_rubric.py <note.json> [...]   (or --all for every v2 note)

Per note:
- word counts per part against the tier budget;
- the distribution of way kinds;
- the largest word overlap between two prose fields;
- the share of objectives evidenced at their own rung;
- entry sentence lengths;
- checks and problems per rung;
- the share of references with a DOI or arXiv id;
- review statistics.

Across notes: the spread of each part as a share of its budget. Scale up only when the spread is under 30% and no
note has an unassessed rung.
"""
import json
import re
import statistics
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import validate as v  # noqa: E402

KB = v.KB
PARTS = ('entry', 'working', 'formal', 'research', 'extras', 'support', 'tutoring', 'links', 'total')


def longest_overlap(d):
	fields = [(p, v.words(v.plain(s))) for p, s in v.strings(d, v.COUNT_SKIP) if len(s) > 60]
	best = (0, '', '')
	grams = {}
	for path, ws in fields:
		for n in (16, 12, 10, 8):
			if len(ws) < n or n <= best[0]:
				continue
			for i in range(len(ws) - n + 1):
				g = ' '.join(ws[i : i + n])
				other = grams.get((n, g))
				if other and other != path:
					best = (n, path, other)
					break
				grams.setdefault((n, g), path)
	return best


def rubric(path):
	d = json.loads(Path(path).read_text())
	tier = d['tier']
	counts = v.part_counts(d)
	budget = v.TIER_BUDGETS[tier]
	shares = {}
	for part in PARTS:
		cap = budget[part][1] if isinstance(budget[part], tuple) else budget[part]
		shares[part] = counts[part] / cap if cap else None
	cols = v.item_maps(d)
	own = sum(1 for o in d['objectives'] if any(cols[a.split('/')[0]].get(a.split('/')[1], {}).get('rung') == o['rung'] for a in o['evidenced_by']))
	entry_lens = [n for w in d['ways_in'] if w['rung'] == 'entry' for n in v.sentence_lengths(w['explanation'])]
	refs = [ref for _, ref in v.references(d)]
	review = d.get('review') or {}
	return dict(
		id=d['id'],
		tier=tier,
		status=d['status'],
		counts=counts,
		shares=shares,
		kinds=dict(Counter(w['kind'] for w in d['ways_in'])),
		overlap=longest_overlap(d),
		objectives_own_rung=f'{own}/{len(d["objectives"])}',
		entry_sentences=(round(statistics.mean(entry_lens), 1) if entry_lens else None, max(entry_lens) if entry_lens else None),
		checks_by_rung=dict(Counter(c['rung'] for c in d['checks'])),
		problems_by_rung=dict(Counter(p['rung'] for p in d['problems'])),
		refs_with_id=f'{sum(1 for r in refs if r["doi"] or r["arxiv"])}/{len(refs)}',
		refs_verified=f'{sum(1 for r in refs if r["verified"])}/{len(refs)}',
		stumbles=len(review.get('novice', {}).get('stumbles', [])) if review.get('novice') else None,
		verification_rows=len(review.get('physics', {}).get('verification', [])) if review.get('physics') else None,
	)


def main(argv):
	files = argv[1:]
	if '--all' in argv:
		files = [str(f) for f in sorted((KB / 'concepts').glob('*/*.json')) if not f.name.startswith('_') and (v.load_json(str(f)) or {}).get('schema_version') == 2]
	rows = [rubric(f) for f in files]
	for r in rows:
		print(f"\n## {r['id']} ({r['tier']}, {r['status']})")
		print('  words: ' + ', '.join(f"{p} {r['counts'][p]}" + (f" ({r['shares'][p]:.0%})" if r['shares'][p] is not None else '') for p in PARTS))
		print(f"  way kinds: {r['kinds']}")
		n, a, b = r['overlap']
		print(f"  largest overlap: {n} words" + (f' between {a} and {b}' if n else ''))
		print(f"  objectives evidenced at own rung: {r['objectives_own_rung']}; checks {r['checks_by_rung']}; problems {r['problems_by_rung']}")
		print(f"  entry sentences mean/max: {r['entry_sentences']}; references with doi/arxiv {r['refs_with_id']}, verified {r['refs_verified']}")
		print(f"  novice stumbles: {r['stumbles']}; physics verification rows: {r['verification_rows']}")
	if len(rows) > 1:
		print('\n## Spread across notes (share of tier budget: mean, coefficient of variation)')
		for part in PARTS:
			vals = [r['shares'][part] for r in rows if r['shares'][part]]
			if len(vals) > 1:
				cv = statistics.pstdev(vals) / statistics.mean(vals) if statistics.mean(vals) else 0
				print(f'  {part}: mean {statistics.mean(vals):.0%}, spread {cv:.0%}' + ('  <- over 30%' if cv > 0.3 else ''))
	return 0


if __name__ == '__main__':
	sys.exit(main(sys.argv))
