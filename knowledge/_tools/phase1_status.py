#!/usr/bin/env python3
"""Report phase 1 progress and print Workflow args to resume it.

Usage:
  python3 knowledge/_tools/phase1_status.py [--args]
  python3 knowledge/_tools/phase1_status.py --next N [--verify-after 2026-09-13T03:00]

A unit is "verified" when its dossier JSON has a verification object, "read" when valid JSON exists without one,
and "missing" otherwise (including unparseable JSON).
--args  prints batch args (at most 25 units each) covering all remaining work.
--next  prints ONE args object for knowledge/_workflows/gr-dossiers-batch.js with at most N units, gentle pacing:
        missing units first (read_only, concurrency 2), then unverified units (verify_only, concurrency 2), in
        teaching-priority order. Verification is withheld before --verify-after (local time). Prints
        PHASE1-COMPLETE when every unit is verified, or WAITING when only verification remains but is withheld.
"""
import json
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
KB = ROOT / 'knowledge'
BOOKS = ('schutz', 'gifted-amateur', 'dinverno')
CONCURRENCY = 5  # agents in flight per run; the user raised this from 2 to 5 on 2026-09-13


def priority(key):
	book, unit = key.split('/')
	n = int(unit[2:]) if unit.startswith('ch') else 100
	if book == 'gifted-amateur':
		return (0, n) if n <= 29 else (3, n)
	if book == 'dinverno':
		return (1, n) if n <= 20 else (4, n)
	return (2, n)


def collect():
	verified, read, missing = [], [], []
	for book in BOOKS:
		toc = json.loads((KB / 'sources' / book / 'toc.json').read_text())
		for u in toc['units']:
			if u['kind'] == 'front-matter' or not u.get('read'):
				continue
			f = KB / 'sources' / book / 'chapters' / f"{u['id']}.json"
			key = f"{book}/{u['id']}"
			try:
				d = json.loads(f.read_text())
			except (OSError, json.JSONDecodeError):
				missing.append(key)
				continue
			(verified if d.get('verification') else read).append(key)
	return verified, sorted(read, key=priority), sorted(missing, key=priority)


def main(argv):
	verified, read, missing = collect()
	profiles = [b for b in BOOKS if (KB / 'sources' / b / 'book-profile.md').exists()]
	print(f'verified {len(verified)}, read-not-verified {len(read)}, missing {len(missing)}; book profiles: {profiles}')

	if '--next' in argv:
		n = int(argv[argv.index('--next') + 1])
		after = argv[argv.index('--verify-after') + 1] if '--verify-after' in argv else None
		if missing:
			print(json.dumps({'name': 'resume-read', 'read_only': True, 'concurrency': CONCURRENCY, 'units': missing[:n]}))
		elif read:
			if after and datetime.now() < datetime.fromisoformat(after):
				print(f'WAITING: only verification remains; withheld until {after}')
			else:
				print(json.dumps({'name': 'resume-verify', 'concurrency': CONCURRENCY, 'verify_only': read[:n]}))
		else:
			print('PHASE1-COMPLETE')
		return 0

	if '--args' in argv:
		work = [('units', k) for k in missing] + [('verify_only', k) for k in read]
		for i in range(0, len(work), 25):
			chunk = work[i : i + 25]
			args = {
				'name': f'resume-{i // 25 + 1}',
				'concurrency': CONCURRENCY,
				'units': [k for m, k in chunk if m == 'units'],
				'verify_only': [k for m, k in chunk if m == 'verify_only'],
			}
			print(json.dumps(args))
	return 0


if __name__ == '__main__':
	sys.exit(main(sys.argv))
