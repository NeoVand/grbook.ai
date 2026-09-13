#!/usr/bin/env python3
"""List learner-visible text that differs between two versions of a concept note.

Usage:
  python3 knowledge/_tools/note_diff.py <before.json> <after.json> [--rungs entry,working,none] [--json]
  python3 knowledge/_tools/note_diff.py --git <rev> <note.json> [--rungs ...] [--json]

Reviewers use this after another stage has edited a note. The novice re-read covers the changed text a reader meets,
and the physics diff check covers every changed claim. Internal and author-only fields (review, provenance,
retired_ids, visual sketches, reference metadata and bookkeeping) are ignored. List items are matched by id, so
reordering items is not a change. Each change is tagged with the rung of the item that holds it; "none" marks text
with no rung, such as prerequisite reasons and history. Long strings show only the sentences that differ.
"""
import difflib
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SKIP = {'review', 'provenance', 'retired_ids', 'updated', 'revision', 'status', 'schema_version', 'sketch', 'starting_material'}
REF_META = {'authors', 'more_authors', 'year', 'venue', 'doi', 'arxiv', 'kind', 'verified'}
# Top-level fields and tutor moves that an entry reader meets or the tutor speaks at any level.
ENTRY_FIELDS = {'title', 'tagline', 'summary', 'aliases', 'glossary', 'pronunciations', 'opening_questions', 'if_stuck', 'voice_notes'}
SENTENCE = re.compile(r'(?<=[.!?])\s+|\n\n+')


def flatten(obj, path='$', rung='none', out=None):
	out = {} if out is None else out
	if isinstance(obj, dict):
		if isinstance(obj.get('rung'), str):
			rung = obj['rung']
		for k, v in obj.items():
			if k in SKIP or k in REF_META or k in ('id', 'rung'):
				continue
			r = 'entry' if k in ENTRY_FIELDS else rung
			flatten(v, f'{path}.{k}', r, out)
	elif isinstance(obj, list):
		for i, v in enumerate(obj):
			key = v['id'] if isinstance(v, dict) and isinstance(v.get('id'), str) else i
			flatten(v, f'{path}[{key}]', rung, out)
	elif isinstance(obj, str):
		out[path] = (rung, obj)
	return out


def sentence_changes(before, after):
	a, b = [s for s in SENTENCE.split(before) if s.strip()], [s for s in SENTENCE.split(after) if s.strip()]
	removed, added = [], []
	for op, i1, i2, j1, j2 in difflib.SequenceMatcher(a=a, b=b, autojunk=False).get_opcodes():
		if op != 'equal':
			removed += a[i1:i2]
			added += b[j1:j2]
	return removed, added


def load_git(rev, note):
	rel = Path(note).resolve().relative_to(ROOT)
	try:
		return json.loads(subprocess.check_output(['git', 'show', f'{rev}:{rel}'], cwd=ROOT, stderr=subprocess.DEVNULL))
	except subprocess.CalledProcessError:
		return {}


def main(argv):
	args = [a for a in argv[1:]]
	as_json = '--json' in args
	rungs = None
	if '--rungs' in args:
		rungs = set(args[args.index('--rungs') + 1].split(','))
		del args[args.index('--rungs') : args.index('--rungs') + 2]
	args = [a for a in args if a != '--json']
	if args and args[0] == '--git':
		before, after = load_git(args[1], args[2]), json.loads(Path(args[2]).read_text())
	elif len(args) == 2:
		before, after = json.loads(Path(args[0]).read_text()), json.loads(Path(args[1]).read_text())
	else:
		print(__doc__)
		return 2
	old, new = flatten(before), flatten(after)
	changes = []
	for path in sorted(set(old) | set(new)):
		o, n = old.get(path), new.get(path)
		if o and n and o[1] == n[1]:
			continue
		rung = (n or o)[0]
		if rungs and rung not in rungs:
			continue
		kind = 'changed' if o and n else ('added' if n else 'removed')
		removed, added = sentence_changes(o[1] if o else '', n[1] if n else '')
		changes.append(dict(path=path, rung=rung, change=kind, removed_sentences=removed, added_sentences=added))
	if as_json:
		print(json.dumps(changes, indent=1, ensure_ascii=False))
		return 0
	counts = {}
	for c in changes:
		counts[c['rung']] = counts.get(c['rung'], 0) + 1
	print(f'{len(changes)} learner-visible strings differ; by rung: {counts}')
	for c in changes:
		print(f"\n[{c['rung']}] {c['change']} {c['path']}")
		for s in c['removed_sentences']:
			print(f'  - {s}')
		for s in c['added_sentences']:
			print(f'  + {s}')
	return 0


if __name__ == '__main__':
	sys.exit(main(sys.argv))
