#!/usr/bin/env python3
"""Compile knowledge/book/outline.txt into outline.json and outline.md, checking registry coverage.

Usage: python3 knowledge/_tools/book_outline.py

outline.txt lines: "= part-id | title", "# chapter-id | title | track | depth", "## section-id | title [| track | depth]",
then one line of comma-separated registry concept ids the section teaches. Track: main (every reader), advanced
(graduate track), reference (read on demand). Depth: the rung the section is written at. Every registry concept must
be taught by exactly one section; the tool prints unknown, missing and duplicated ids and exits 1 on any.
"""
import json
import sys
from pathlib import Path

KB = Path(__file__).resolve().parents[1]
SRC, OUT_JSON, OUT_MD = KB / 'book' / 'outline.txt', KB / 'book' / 'outline.json', KB / 'book' / 'outline.md'


def registry():
	reg = {}
	for f in (KB / 'concepts').glob('*/_registry.json'):
		for c in json.loads(f.read_text())['concepts']:
			reg[c['id']] = (f.parent.name, c['tier'], c['title'])
	return reg


def parse():
	parts, part, chapter, section = [], None, None, None
	for raw in SRC.read_text().splitlines():
		line = raw.strip()
		if not line:
			continue
		if line.startswith('= '):
			pid, title = [x.strip() for x in line[2:].split('|')]
			part = {'id': pid, 'title': title, 'chapters': []}
			parts.append(part)
		elif line.startswith('## '):
			f = [x.strip() for x in line[3:].split('|')]
			section = {'id': f[0], 'title': f[1], 'track': f[2] if len(f) > 2 else chapter['track'], 'depth': f[3] if len(f) > 3 else chapter['depth'], 'concepts': []}
			chapter['sections'].append(section)
		elif line.startswith('# '):
			f = [x.strip() for x in line[2:].split('|')]
			chapter = {'id': f[0], 'title': f[1], 'track': f[2], 'depth': f[3], 'sections': []}
			part['chapters'].append(chapter)
		else:
			section['concepts'] += [x.strip() for x in line.split(',') if x.strip()]
	return parts


def main():
	reg, parts = registry(), parse()
	seen, problems = {}, []
	for p in parts:
		for ch in p['chapters']:
			for s in ch['sections']:
				for c in s['concepts']:
					if c not in reg:
						problems.append(f'unknown id {c} in {ch["id"]}/{s["id"]}')
					elif c in seen:
						problems.append(f'{c} taught twice: {seen[c]} and {ch["id"]}/{s["id"]}')
					seen[c] = f'{ch["id"]}/{s["id"]}'
	missing = sorted(set(reg) - set(seen))
	problems += [f'not taught: {m} ({reg[m][0]})' for m in missing]
	nsec = sum(len(ch['sections']) for p in parts for ch in p['chapters'])
	nch = sum(len(p['chapters']) for p in parts)
	print(f'{len(parts)} parts, {nch} chapters, {nsec} sections, {len(seen)} of {len(reg)} concepts assigned')
	for x in problems:
		print(' ', x)
	if problems:
		return 1
	OUT_JSON.write_text(json.dumps({'schema_version': 1, 'parts': parts}, indent='\t', ensure_ascii=False) + '\n')
	o = ['# Book outline', '', f'{nch} chapters, {nsec} sections. Each section lists the registry concepts it teaches; the section, not the concept, is the unit of writing.', '']
	n = 0
	for p in parts:
		o += [f'## {p["title"]}', '']
		for ch in p['chapters']:
			n += 1
			o += [f'### {n}. {ch["title"]} `{ch["id"]}` ({ch["track"]}, {ch["depth"]})', '']
			for i, s in enumerate(ch['sections'], 1):
				tag = '' if (s['track'], s['depth']) == (ch['track'], ch['depth']) else f' ({s["track"]}, {s["depth"]})'
				o += [f'{n}.{i} **{s["title"]}**{tag} — {len(s["concepts"])} concepts: ' + ', '.join(f'`{c}`' for c in s['concepts']), '']
	OUT_MD.write_text('\n'.join(o))
	by_track = {}
	for p in parts:
		for ch in p['chapters']:
			for s in ch['sections']:
				by_track[s['track']] = by_track.get(s['track'], 0) + 1
	print('sections by track:', by_track)
	return 0


if __name__ == '__main__':
	sys.exit(main())
