#!/usr/bin/env python3
"""Build structural manifests and chapter reading files from the page-level book exports.

Inputs (local only, gitignored):
  book-sources/<book>/pages/page-N/{markdown.md, page-metadata.json, img-*.jpeg, tbl-*.html}

Outputs:
  knowledge/sources/<book>/toc.json           parts, units, sections with printed and PDF page numbers
  book-sources/_chapters/<book>/<unit>.md     reading copy of each unit with page markers (verbatim, local only)
  book-sources/_chapters/<book>/manifest.json per-unit inventories: figures, examples, equation tags, asides

A "unit" is a chapter, appendix, or the front matter. PDF page N is the folder page-N; printed page = N - offset.
"""
import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / 'book-sources'
KB = ROOT / 'knowledge'

BOOKS = {
	'schutz': dict(
		title='A First Course in General Relativity',
		edition='Third edition (2022)',
		authors=['Bernard Schutz'],
		publisher='Cambridge University Press',
		short='SCH',
		offset=18,
		contents_pages=range(7, 11),
		front_matter=(12, 18),
	),
	'gifted-amateur': dict(
		title='General Relativity for the Gifted Amateur',
		edition='First edition',
		authors=['Stephen J. Blundell', 'Tom Lancaster'],
		publisher='Oxford University Press',
		short='GA',
		offset=17,
		contents_pages=range(8, 17),
		front_matter=None,
	),
	'dinverno': dict(
		title="Introducing Einstein's Relativity: A Deeper Understanding",
		edition='Second edition (2022)',
		authors=["Ray d'Inverno", 'James Vickers'],
		publisher='Oxford University Press',
		short='DIV',
		offset=15,
		contents_pages=range(8, 16),
		front_matter=None,
	),
}

SKIP_TITLES = re.compile(r'^(Answers|Further reading$)', re.I)

SEC = re.compile(r'^(\d{1,2}|[A-E])\.(\d{1,2})\s+(.+?)\s+(\d{1,3})$')
PART = re.compile(r'^(?:Part\s+([A-F])|([IVX]{1,4}))\s+(.+?)(?:\s+(\d{1,3}))?$')
CH = re.compile(r'^(?:Appendix\s+)?(\d{1,2}|[A-E])\s+(.+?)\s+(\d{1,3})$')
CH_NOPAGE = re.compile(r'^(\d{1,2})\s+([A-Z][^0-9]*)$')
BACK = re.compile(r'^(Exercises|Further reading|Chapter summary|Bibliography)\s*(\d{1,3})?$')
END = re.compile(r'^(References|Index|Answers to exercises|Selected bibliography)\s*(\d{1,3})?$')


def page_dir(book, n):
	return SRC / book / 'pages' / f'page-{n}'


def page_numbers(book):
	pages = [p for p in (SRC / book / 'pages').iterdir() if p.name.startswith('page-')]
	return sorted(int(p.name.split('-')[1]) for p in pages)


def table_rows(path):
	s = path.read_text(errors='replace')
	rows = []
	for r in re.findall(r'<tr[^>]*>(.*?)</tr>', s, flags=re.S):
		cells = re.findall(r'<t[dh][^>]*>(.*?)</t[dh]>', r, flags=re.S)
		rows.append([' '.join(html.unescape(re.sub(r'<[^>]+>', ' ', c)).split()) for c in cells])
	return rows


def inline_tables(pdir, md, as_markdown):
	def sub(m):
		f = pdir / m.group(1)
		if not f.exists():
			return m.group(0)
		rows = table_rows(f)
		if as_markdown:
			return '\n'.join('| ' + ' | '.join(r) + ' |' for r in rows)
		return '\n'.join(' '.join(c for c in r if c) for r in rows)

	return re.sub(r'\[(tbl-\d+\.html)\]\(tbl-\d+\.html\)', sub, md)


def normalize(line):
	line = line.replace('$$', '').replace('$', '')
	line = re.sub(r'^[#*\s]+|[*\s]+$', '', line)
	return ' '.join(line.split())


def parse_contents(book, cfg):
	lines = []
	for n in cfg['contents_pages']:
		pdir = page_dir(book, n)
		md = inline_tables(pdir, (pdir / 'markdown.md').read_text(errors='replace'), as_markdown=False)
		lines += [normalize(x) for x in md.splitlines()]

	parts, units, seen = [], [], set()
	pending_part = None
	back_matter_start = None
	for line in lines:
		if not line or line.lower().startswith(('contents', 'preface', 'foreword')):
			continue
		if m := END.match(line):
			back_matter_start = int(m.group(2)) if m.group(2) else None
			if m.group(1) in ('References', 'Index', 'Selected bibliography') or back_matter_start:
				units.append(dict(kind='back', title=m.group(1), printed_start=back_matter_start))
			if m.group(1) == 'Index':
				break
			continue
		if m := SEC.match(line):
			if units and units[-1]['kind'] in ('chapter', 'appendix'):
				units[-1]['sections'].append(
					dict(number=f'{m.group(1)}.{m.group(2)}', title=m.group(3), printed_page=int(m.group(4)))
				)
			continue
		if m := BACK.match(line):
			if units and units[-1]['kind'] in ('chapter', 'appendix'):
				units[-1]['back_items'].append(
					dict(title=m.group(1), printed_page=int(m.group(2)) if m.group(2) else None)
				)
			continue
		if m := PART.match(line):
			label = m.group(1) or m.group(2)
			pending_part = dict(label=label, title=m.group(3), printed_page=int(m.group(4)) if m.group(4) else None)
			parts.append(pending_part)
			continue
		m = CH.match(line)
		nopage = False
		if not m:
			m = CH_NOPAGE.match(line)
			nopage = bool(m)
		if m:
			label = m.group(1)
			if label in seen:
				continue
			seen.add(label)
			kind = 'appendix' if label.isalpha() else 'chapter'
			units.append(
				dict(
					kind=kind,
					label=label,
					title=m.group(2).strip(),
					printed_page=None if nopage else int(m.group(3)),
					part=pending_part,
					sections=[],
					back_items=[],
				)
			)
			pending_part = None
	return parts, units


def last_listed_page(u):
	pages = [u.get('printed_page')] + [s['printed_page'] for s in u['sections']] + [b['printed_page'] for b in u['back_items']]
	return max(p for p in pages if p)


def resolve_ranges(book, cfg, units):
	body = [u for u in units if u['kind'] in ('chapter', 'appendix')]
	back = [u for u in units if u['kind'] == 'back' and u.get('printed_start')]
	for i, u in enumerate(body):
		if not u['printed_page']:
			u['printed_page'] = u['sections'][0]['printed_page'] if u['sections'] else None
		part = u['part']
		if part and part['printed_page']:
			u['reading_start'] = part['printed_page']
		elif part and i > 0:
			u['reading_start'] = last_listed_page(body[i - 1]) + 1
		else:
			u['reading_start'] = u['printed_page']
	# a chapter without a printed page starts after the previous unit's last listed item
	for i, u in enumerate(body):
		if u['reading_start'] is None and i > 0:
			u['reading_start'] = last_listed_page(body[i - 1]) + 1
	end_of_body = min((b['printed_start'] for b in back), default=None)
	max_pdf = page_numbers(book)[-1]
	for i, u in enumerate(body):
		nxt = body[i + 1]['reading_start'] if i + 1 < len(body) else (end_of_body or (max_pdf - cfg['offset'] + 1))
		u['reading_end'] = nxt - 1
	return body, back


def unit_id(u):
	return f"ch{int(u['label']):02d}" if u['kind'] == 'chapter' else f"app{u['label']}"


def page_header(meta):
	return ' / '.join(b['content'].replace('\n', ' ').strip() for b in meta['blocks'] if b['type'] == 'header')


def figure_label(caption):
	m = re.match(r'^\s*\**\s*(Fig(?:ure)?\.?\s*[0-9A-Z]+\.\d+[a-z]?)', caption)
	return m.group(1) if m else None


def inventory(book, cfg, pdf_first, pdf_last, label=None):
	figures, orphan_captions, examples, tags, asides, exercise_pages, tables = [], [], [], [], 0, [], []
	text_lengths, visual_pages, mentioned = {}, set(), {}
	for n in range(pdf_first, pdf_last + 1):
		pdir = page_dir(book, n)
		mf = pdir / 'page-metadata.json'
		if not mf.exists():
			continue
		meta = json.loads(mf.read_text())
		md = (pdir / 'markdown.md').read_text(errors='replace') if (pdir / 'markdown.md').exists() else ''
		printed = n - cfg['offset']
		images = [b.get('imageId') for b in meta['blocks'] if b['type'] == 'image' and b.get('imageId')]
		captions = [' '.join(b['content'].split()) for b in meta['blocks'] if b['type'] == 'caption']
		for i, img in enumerate(images):
			cap = captions[i] if i < len(captions) else None
			figures.append(
				dict(
					pdf_page=n,
					printed_page=printed,
					image_path=f'{book}/pages/page-{n}/{img}',
					label=figure_label(cap) if cap else None,
					caption=cap[:300] if cap else None,
				)
			)
		for cap in captions[len(images):]:
			orphan_captions.append(dict(pdf_page=n, printed_page=printed, label=figure_label(cap), caption=cap[:300]))
		for b in meta['blocks']:
			c = ' '.join(b['content'].split())
			if b['type'] in ('title', 'text') and (m := re.match(r'^[#*\s]*(Example\s+\d+\.\d+)', c)):
				examples.append(dict(label=m.group(1), pdf_page=n, printed_page=printed))
			if b['type'] == 'aside_text':
				asides += 1
			if b['type'] in ('title', 'header') and re.search(r'\bExercises\b', c):
				if n not in exercise_pages:
					exercise_pages.append(n)
		tags += [dict(tag=t.strip(), pdf_page=n) for t in re.findall(r'\\tag\s*\{([^}]+)\}', md)]
		page_tables = sorted(pdir.glob('tbl-*.html'))
		tables += [dict(pdf_page=n, file=f'{book}/pages/page-{n}/{t.name}') for t in page_tables]
		text_lengths[n] = len(re.sub(r'!\[[^\]]*\]\([^)]*\)|\[tbl-\d+\.html\]\(tbl-\d+\.html\)', '', md).strip())
		if images or page_tables:
			visual_pages.add(n)
		if label and label.isdigit():
			for num in re.findall(rf'(?:Figure|Fig\.)\s*({int(label)}\.\d+)', md):
				mentioned.setdefault(num, n)
	dedup = {}
	for e in examples:
		dedup.setdefault(e['label'], e)

	# Pages whose exported text is much shorter than typical and carry no figure or table often lost
	# content during export. Figure numbers cited in the text without a captioned image may be vector art.
	lengths = sorted(text_lengths.values())
	median = lengths[len(lengths) // 2] if lengths else 0
	short_pages = [
		dict(pdf_page=n, chars=c, median_chars=median)
		for n, c in text_lengths.items()
		if n != pdf_last and n not in visual_pages and n not in exercise_pages and median and c < 0.5 * median
	]
	captioned = set()
	for f in figures + orphan_captions:
		for num in re.findall(r'\d+\.\d+', f.get('label') or ''):
			captioned.add(num)
	uncaptioned = [dict(figure=num, first_mentioned_pdf_page=p) for num, p in sorted(mentioned.items()) if num not in captioned]
	return dict(
		suspect_short_pages=short_pages,
		figures_mentioned_without_image=uncaptioned,
		figures=figures,
		unpaired_captions=orphan_captions,
		examples=list(dedup.values()),
		equation_tags=tags,
		aside_count=asides,
		exercise_pdf_pages=exercise_pages,
		tables=tables,
	)


def write_reading_file(book, cfg, uid, title, pdf_first, pdf_last, out):
	parts = [
		f'<!-- SOURCE {cfg["short"]} ({book}) | UNIT {uid}: {title} | PDF pages {pdf_first}-{pdf_last} | '
		f'printed pages {pdf_first - cfg["offset"]}-{pdf_last - cfg["offset"]} -->',
		'<!-- Figure images are referenced by absolute path; open them with the Read tool to see them. -->',
		'',
	]
	for n in range(pdf_first, pdf_last + 1):
		pdir = page_dir(book, n)
		if not (pdir / 'markdown.md').exists():
			continue
		meta = json.loads((pdir / 'page-metadata.json').read_text()) if (pdir / 'page-metadata.json').exists() else {'blocks': []}
		md = inline_tables(pdir, (pdir / 'markdown.md').read_text(errors='replace'), as_markdown=True)
		md = re.sub(
			r'!\[(img-\d+\.jpeg)\]\(img-\d+\.jpeg\)',
			lambda m: f'![{m.group(1)}]({(pdir / m.group(1)).resolve()})',
			md,
		)
		printed = n - cfg['offset']
		parts.append(f'\n=== [{cfg["short"]} pdf page-{n} | printed p.{printed} | running header: {page_header(meta)}] ===\n')
		parts.append(md)
	out.write_text('\n'.join(parts))


def find_front_matter(book, cfg):
	if cfg['front_matter']:
		return cfg['front_matter']
	first_contents = cfg['contents_pages'].start
	start = None
	for n in range(1, first_contents):
		md = page_dir(book, n) / 'markdown.md'
		if md.exists() and re.search(r'^#+\s*(Preface|Foreword)', md.read_text(errors='replace'), re.M):
			start = n
			break
	return (start, first_contents - 1) if start else None


def build(book, cfg):
	parts, units = parse_contents(book, cfg)
	body, back = resolve_ranges(book, cfg, units)
	off = cfg['offset']
	chapters_dir = SRC / '_chapters' / book
	chapters_dir.mkdir(parents=True, exist_ok=True)
	toc_units, manifest_units, problems = [], [], []

	fm = find_front_matter(book, cfg)
	if fm:
		uid = 'front'
		write_reading_file(book, cfg, uid, 'Front matter (preface/foreword)', fm[0], fm[1], chapters_dir / f'{uid}.md')
		toc_units.append(dict(id=uid, kind='front-matter', title='Front matter (preface/foreword)', pdf_pages=list(fm), read=True))
		manifest_units.append(dict(id=uid, kind='front-matter', title='Front matter', reading_file=f'_chapters/{book}/{uid}.md', pdf_pages=list(fm)))

	prev_start = 0
	for u in body:
		uid = unit_id(u)
		pdf_first, pdf_last = u['reading_start'] + off, u['reading_end'] + off
		if u['reading_start'] <= prev_start or pdf_last < pdf_first:
			problems.append(f'{uid}: non-monotonic range {u["reading_start"]}-{u["reading_end"]}')
		prev_start = u['reading_start']
		for s in u['sections']:
			s['pdf_page'] = s['printed_page'] + off
			if not (u['reading_start'] <= s['printed_page'] <= u['reading_end']):
				problems.append(f'{uid}: section {s["number"]} p.{s["printed_page"]} outside {u["reading_start"]}-{u["reading_end"]}')
		read = not SKIP_TITLES.match(u['title'])
		entry = dict(
			id=uid,
			kind=u['kind'],
			label=u['label'],
			title=u['title'],
			part=dict(label=u['part']['label'], title=u['part']['title']) if u['part'] else None,
			printed_pages=[u['reading_start'], u['reading_end']],
			pdf_pages=[pdf_first, pdf_last],
			chapter_printed_page=u['printed_page'],
			sections=u['sections'],
			back_items=[dict(b, pdf_page=(b['printed_page'] + off) if b['printed_page'] else None) for b in u['back_items']],
			read=read,
		)
		if not read:
			entry['skip_reason'] = 'answers or reading list; indexed for locators, not read for concepts'
		toc_units.append(entry)
		write_reading_file(book, cfg, uid, u['title'], pdf_first, pdf_last, chapters_dir / f'{uid}.md')
		manifest_units.append(
			dict(
				id=uid,
				kind=u['kind'],
				title=u['title'],
				reading_file=f'_chapters/{book}/{uid}.md',
				pdf_pages=[pdf_first, pdf_last],
				read=read,
				inventory=inventory(book, cfg, pdf_first, pdf_last, u['label']),
			)
		)

	meta = {k: v for k, v in cfg.items() if k in ('title', 'edition', 'authors', 'publisher', 'short')}
	meta.update(id=book, printed_page_offset=off, page_folder_pattern=f'{book}/pages/page-<pdf_page>')
	toc = dict(
		book=meta,
		parts=[dict(label=p['label'], title=p['title'], printed_page=p['printed_page']) for p in parts],
		units=toc_units,
		back_matter=[dict(title=b['title'], printed_page=b['printed_start'], pdf_page=b['printed_start'] + off) for b in back],
	)
	(KB / 'sources' / book).mkdir(parents=True, exist_ok=True)
	(KB / 'sources' / book / 'toc.json').write_text(json.dumps(toc, indent=2, ensure_ascii=False))
	(chapters_dir / 'manifest.json').write_text(json.dumps(dict(book=meta, units=manifest_units), indent=2, ensure_ascii=False))

	print(f'\n=== {book}: {len(parts)} parts, {len(body)} units, back matter {[b["title"] for b in back]}')
	for e, m in zip([t for t in toc_units if t['kind'] != 'front-matter'], [m for m in manifest_units if m['kind'] != 'front-matter']):
		inv = m['inventory']
		print(
			f"  {e['id']:>6} {e['title'][:48]:<48} p{e['printed_pages'][0]:>3}-{e['printed_pages'][1]:<3} "
			f"secs={len(e['sections']):>2} figs={len(inv['figures']):>2} ex={len(inv['examples']):>2} "
			f"tags={len(inv['equation_tags']):>3} asides={inv['aside_count']:>2} "
			f"short={len(inv['suspect_short_pages']):>2} nofig={len(inv['figures_mentioned_without_image']):>2}"
			f"{'' if e['read'] else '  [SKIP]'}"
			f"{'  part=' + e['part']['label'] if e['part'] else ''}"
		)
	if fm:
		print(f'  front matter pdf pages {fm}')
	for p in problems:
		print('  PROBLEM:', p)


if __name__ == '__main__':
	for book, cfg in BOOKS.items():
		build(book, cfg)
