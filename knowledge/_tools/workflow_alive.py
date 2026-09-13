#!/usr/bin/env python3
"""Print RUNNING if any workflow agent in this Claude session wrote to its transcript recently, else IDLE.

Usage: python3 knowledge/_tools/workflow_alive.py [--minutes 12] [--dir <session workflows dir>]
Agents append to their transcripts continuously while they work, so a recent write means a run is still active.
"""
import sys
import time
from pathlib import Path

DEFAULT_DIR = '/Users/neo/.claude/projects/-Users-neo-repos-general-relativity/bdf94c63-cbec-4edd-ba4c-fe7299d5507b/subagents/workflows'


def main(argv):
	minutes = float(argv[argv.index('--minutes') + 1]) if '--minutes' in argv else 12
	root = Path(argv[argv.index('--dir') + 1]) if '--dir' in argv else Path(DEFAULT_DIR)
	newest = max((p.stat().st_mtime for p in root.glob('*/agent-*.jsonl')), default=0)
	age = (time.time() - newest) / 60
	print(f"{'RUNNING' if age < minutes else 'IDLE'} (newest agent activity {age:.1f} min ago)")
	return 0


if __name__ == '__main__':
	sys.exit(main(sys.argv))
