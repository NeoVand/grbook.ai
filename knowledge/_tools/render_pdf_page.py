#!/usr/bin/env python3
"""Render a full source page from the original PDF, to check figures the page export missed.

Usage: python3 knowledge/_tools/render_pdf_page.py <book> <pdf_page> [<pdf_page> ...]
Books: schutz, gifted-amateur, dinverno. The PDF is found anywhere under the GRbooks folder by author keyword.
PDF page numbers match the export's page-N folders. Writes book-sources/_renders/<book>/page-N.png and prints paths.
"""
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SEARCH_ROOT = (ROOT / 'book-sources' / 'schutz').resolve().parent
KEYWORDS = {'schutz': 'schutz', 'gifted-amateur': 'gifted', 'dinverno': 'inverno'}


def find_pdf(book):
	key = KEYWORDS[book]
	for p in sorted(SEARCH_ROOT.rglob('*.pdf')):
		if p.is_file() and key in p.name.lower():
			return p
	return None


def main(argv):
	if len(argv) < 3 or argv[1] not in KEYWORDS:
		print(__doc__)
		return 1
	book, pages = argv[1], [int(x) for x in argv[2:]]
	pdf = find_pdf(book)
	if not pdf:
		print(f'No PDF for {book} found under {SEARCH_ROOT} (expected a file whose name contains "{KEYWORDS[book]}").')
		return 1
	out_dir = ROOT / 'book-sources' / '_renders' / book
	out_dir.mkdir(parents=True, exist_ok=True)
	for n in pages:
		target = out_dir / f'page-{n}.png'
		if not target.exists():
			subprocess.run(
				['pdftoppm', '-f', str(n), '-l', str(n), '-r', '110', '-png', '-singlefile', str(pdf), str(target.with_suffix(''))],
				check=True,
			)
		print(target)
	return 0


if __name__ == '__main__':
	sys.exit(main(sys.argv))
