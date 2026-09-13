#!/usr/bin/env python3
"""Views over concept candidate clusters, and merging of domain assignments.

Usage:
  python3 knowledge/_tools/print_clusters.py --compact [--start N] [--end M]
      One line per cluster: index | key | names | book counts | deepest treatment | kinds.
  python3 knowledge/_tools/print_clusters.py --merge-assignments
      Merge knowledge/_build/assign-*.json into knowledge/_build/assignments.json; report unassigned clusters.
  python3 knowledge/_tools/print_clusters.py --domain <domain-id> [--secondary]
      Full details of clusters whose primary (or, with --secondary, any) domain is <domain-id>.
  python3 knowledge/_tools/print_clusters.py --detail <index> [<index> ...]
      Definitions of specific clusters by index.

The pseudo-domain "discard" marks clusters that are not teachable concepts (book logistics, one-off labels).

Assignment files look like {"assignments": [{"index": 12, "key": "riemann curvature tensor", "primary": "curvature", "secondary": []}]}.
"""
import json
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BUILD = ROOT / 'knowledge' / '_build'
SHORT = {'schutz': 'SCH', 'gifted-amateur': 'GA', 'dinverno': 'DIV'}


def load_clusters():
	return json.loads((BUILD / 'concept-candidates.json').read_text())['clusters']


def arg(argv, flag, default=None):
	return argv[argv.index(flag) + 1] if flag in argv else default


def compact(argv):
	clusters = load_clusters()
	start, end = int(arg(argv, '--start', 0)), int(arg(argv, '--end', len(clusters)))
	for i in range(start, min(end, len(clusters))):
		c = clusters[i]
		books = ' '.join(f"{SHORT[b]}:{len(v)}" for b, v in c['books'].items())
		kinds = ','.join(k for k, _ in c['kinds'][:2])
		print(f"{i} | {c['key']} | {' / '.join(c['names'][:4])} | {books} | {c['max_depth']} | {kinds}")
	print(f'# clusters {start}-{min(end, len(clusters)) - 1} of {len(clusters)}')


def merge():
	clusters = load_clusters()
	merged = {}
	for f in sorted(BUILD.glob('assign-*.json')):
		for a in json.loads(f.read_text())['assignments']:
			merged[a['index']] = a
	missing = [i for i in range(len(clusters)) if i not in merged]
	mismatched = [i for i, a in merged.items() if i < len(clusters) and a.get('key') != clusters[i]['key']]
	(BUILD / 'assignments.json').write_text(json.dumps(dict(assignments=[merged[i] for i in sorted(merged)]), indent=1))
	counts = Counter(a['primary'] for a in merged.values())
	print(f'{len(merged)} assignments for {len(clusters)} clusters')
	print('primary domain counts:', dict(sorted(counts.items(), key=lambda kv: -kv[1])))
	if missing:
		print(f'UNASSIGNED ({len(missing)}): {missing[:200]}')
	if mismatched:
		print(f'KEY MISMATCH ({len(mismatched)}): {mismatched[:50]}')
	return 1 if missing or mismatched else 0


def domain(argv):
	target = arg(argv, '--domain')
	clusters = load_clusters()
	assignments = json.loads((BUILD / 'assignments.json').read_text())['assignments']
	picked = [a for a in assignments if a['primary'] == target or ('--secondary' in argv and target in a.get('secondary', []))]
	print(f'# Candidate clusters for domain "{target}": {len(picked)}\n')
	for a in picked:
		c = clusters[a['index']]
		role = 'primary' if a['primary'] == target else f"secondary (primary: {a['primary']})"
		print(f"## [{a['index']}] {c['key']} ({role}; deepest: {c['max_depth']}; {c['mention_count']} mentions)")
		print(f"Names: {' / '.join(c['names'])}")
		if c['aliases']:
			print(f"Aliases: {' / '.join(c['aliases'])}")
		for book, mentions in c['books'].items():
			for m in mentions:
				locs = ', '.join(f"p.{l.get('printed_page')}" for l in m['locators'])
				print(f"- {SHORT[book]} {m['unit']} [{m['depth']}, {m['kind']}; {locs}] {m['name']}: {m['definition']}")
				print(f"  introduced: {m['how_introduced'][:400]}")
				if m['prerequisites']:
					print(f"  prerequisites: {', '.join(m['prerequisites'])}")
		print()
	return 0


def detail(argv):
	clusters = load_clusters()
	for raw in argv[argv.index('--detail') + 1 :]:
		if not raw.isdigit():
			break
		c = clusters[int(raw)]
		print(f"## [{raw}] {c['key']} ({c['mention_count']} mentions, deepest {c['max_depth']})")
		for book, mentions in c['books'].items():
			for m in mentions:
				print(f"- {SHORT[book]} {m['unit']} [{m['depth']}, {m['kind']}] {m['name']}: {m['definition']}")
		print()
	return 0


def main(argv):
	if '--compact' in argv:
		compact(argv)
		return 0
	if '--detail' in argv:
		return detail(argv)
	if '--merge-assignments' in argv:
		return merge()
	if '--domain' in argv:
		return domain(argv)
	print(__doc__)
	return 1


if __name__ == '__main__':
	sys.exit(main(sys.argv))
