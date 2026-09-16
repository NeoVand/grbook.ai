#!/usr/bin/env python3
"""Print a compact digest of concept notes, for agents that must connect to a note without reading all of it.

Usage: python3 knowledge/_tools/note_digest.py [--ways entry,working] <concept-id> [...]

--ways prints the full explanation, try_it and takeaway of the ways at those rungs, after each digest.

A digest is a few hundred words: title, tier, status, summary, glossary terms with their plain definitions, each way
(rung, kind, title, question, takeaway), key equation names with LaTeX, check and problem ids by rung, and the
misconception beliefs. Writers use it for prerequisites and neighbours so pictures, terms and ladders connect.
"""
import json
import sys
from pathlib import Path

CONCEPTS = Path(__file__).resolve().parents[1] / 'concepts'


def digest(cid, ways=()):
	hits = list(CONCEPTS.glob(f'*/{cid}.json'))
	if not hits:
		return f'## {cid}\nno note yet (registry entry only)\n'
	d = json.loads(hits[0].read_text())
	if d.get('schema_version') != 2:
		return f'## {cid}\nolder draft, not schema v2; treat as absent\n'
	o = [f"## {d['id']} — {d['title']} ({d['tier']}, {d['status']}, revision {d['revision']})", d['summary'], '']
	if d['glossary']:
		o += ['Glossary: ' + '; '.join(f"{g['term']}: {g['plain_definition']}" for g in d['glossary']), '']
	for w in d['ways_in']:
		o.append(f"- way {w['id']} [{w['rung']}, {w['kind']}] \"{w['title']}\". Q: {w['question']} Takeaway: {w['takeaway']}")
	if d['key_equations']:
		o += ['', 'Equations: ' + '; '.join(f"{e['id']} [{e['rung']}] {e['latex']}" for e in d['key_equations'])]
	o += ['', 'Checks: ' + ', '.join(f"{c['id']} [{c['rung']}]" for c in d['checks']), 'Problems: ' + ', '.join(f"{p['id']} [{p['rung']}]" for p in d['problems'])]
	if d['misconceptions']:
		o += ['Misconceptions: ' + '; '.join(f"{m['id']}: \"{m['belief']}\"" for m in d['misconceptions'])]
	o += ['Prerequisites: ' + ', '.join(f"{p['id']} ({p['needed_for']})" for p in d['prerequisites']), 'Visuals: ' + ', '.join(v['id'] for v in d['visuals']), '']
	for w in d['ways_in']:
		if w['rung'] in ways:
			o += [f"### way {w['id']} [{w['rung']}] {w['title']}", w['explanation'], '', f"Try it: {w['try_it']}" if w.get('try_it') else '', f"Takeaway: {w['takeaway']}", '']
	return '\n'.join(o)


if __name__ == '__main__':
	if len(sys.argv) < 2:
		print(__doc__)
		sys.exit(2)
	args = sys.argv[1:]
	ways = ()
	if '--ways' in args:
		i = args.index('--ways')
		ways = tuple(args[i + 1].split(','))
		del args[i : i + 2]
	print('\n'.join(digest(c, ways) for c in args))
