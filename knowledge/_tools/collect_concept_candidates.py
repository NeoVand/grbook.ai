#!/usr/bin/env python3
"""Collect concept mentions from all chapter dossiers into candidate clusters for the concept registry.

Usage: python3 knowledge/_tools/collect_concept_candidates.py [--print N]
Writes knowledge/_build/concept-candidates.json: clusters of mentions whose normalized names coincide, or which share
a multi-word alias. Clusters are starting points for canonicalization agents, not final concepts.
"""
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
KB = ROOT / 'knowledge'
OUT = KB / '_build' / 'concept-candidates.json'
BOOKS = ('schutz', 'gifted-amateur', 'dinverno')


def normalize(name):
	s = name.replace('’', "'").replace('–', ' ').replace('—', ' ').replace('-', ' ')
	s = re.sub(r"'s\b", '', s)
	s = re.sub(r'\([^)]*\)', ' ', s)
	s = re.sub(r'^(the|a|an)\s+', '', s.strip(), flags=re.I)
	words = []
	for w in re.findall(r'[A-Za-z0-9+]+', s):
		# Singularize ordinary lowercase plurals; leave proper names such as "Brans" or "Rindler" alone.
		if w.islower() and len(w) > 4 and w.endswith('s') and not w.endswith(('ss', 'is', 'us', 'ics')):
			w = w[:-1]
		words.append(w.lower())
	return ' '.join(words)


class UnionFind:
	def __init__(self):
		self.parent = {}

	def find(self, x):
		self.parent.setdefault(x, x)
		while self.parent[x] != x:
			self.parent[x] = self.parent[self.parent[x]]
			x = self.parent[x]
		return x

	def union(self, a, b):
		self.parent[self.find(a)] = self.find(b)


def main(argv):
	mentions = []
	for book in BOOKS:
		for f in sorted((KB / 'sources' / book / 'chapters').glob('*.json')):
			d = json.loads(f.read_text())
			for c in d['concepts']:
				mentions.append(
					dict(
						book=book,
						unit=d['unit_id'],
						name=c['name'],
						aliases=c['aliases'],
						kind=c['kind'],
						depth=c['depth'],
						definition=c['definition'],
						how_introduced=c['how_introduced'],
						prerequisites=c['prerequisites'],
						locators=c['locators'][:3],
					)
				)

	uf = UnionFind()
	for i, m in enumerate(mentions):
		key = normalize(m['name'])
		uf.union(f'm{i}', f'n:{key}')
		for a in m['aliases']:
			ak = normalize(a)
			if len(ak.split()) >= 2:
				uf.union(f'm{i}', f'n:{ak}')

	clusters = defaultdict(list)
	for i, m in enumerate(mentions):
		clusters[uf.find(f'm{i}')].append(m)

	out = []
	for members in clusters.values():
		names = Counter(m['name'] for m in members)
		books = defaultdict(list)
		for m in members:
			books[m['book']].append({k: m[k] for k in ('unit', 'name', 'depth', 'kind', 'definition', 'how_introduced', 'prerequisites', 'locators')})
		out.append(
			dict(
				key=normalize(names.most_common(1)[0][0]),
				names=[n for n, _ in names.most_common()],
				aliases=sorted({a for m in members for a in m['aliases']}),
				kinds=Counter(m['kind'] for m in members).most_common(),
				max_depth=max((m['depth'] for m in members), key=['mention', 'introduced', 'revisited', 'developed', 'core'].index),
				mention_count=len(members),
				book_count=len(books),
				books=books,
			)
		)
	out.sort(key=lambda c: (-c['book_count'], -c['mention_count'], c['key']))
	OUT.parent.mkdir(parents=True, exist_ok=True)
	OUT.write_text(json.dumps(dict(mention_count=len(mentions), cluster_count=len(out), clusters=out), indent=1, ensure_ascii=False))

	sizes = Counter(min(c['mention_count'], 10) for c in out)
	print(f'{len(mentions)} mentions -> {len(out)} clusters; wrote {OUT}')
	print('clusters by book coverage:', Counter(c['book_count'] for c in out))
	print('cluster sizes (10 = 10+):', sorted(sizes.items()))
	n = int(argv[argv.index('--print') + 1]) if '--print' in argv else 15
	for c in out[:n]:
		print(f"  [{c['book_count']} books, {c['mention_count']} mentions] {c['key']} <- {c['names'][:5]}")
	big = [c for c in out if c['mention_count'] > 12]
	if big:
		print('large clusters to inspect for over-merging:', [(c['key'], c['mention_count']) for c in big[:20]])
	return 0


if __name__ == '__main__':
	sys.exit(main(sys.argv))
