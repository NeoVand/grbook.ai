#!/usr/bin/env python3
"""Validate knowledge-vault JSON against its schema, plus content checks.

Usage:
  python3 knowledge/_tools/validate.py dossier <sources/<book>/chapters/<unit>.json> [...]
  python3 knowledge/_tools/validate.py concept <concepts/<domain>/<id>.json> [...]
  python3 knowledge/_tools/validate.py visual <visuals/<id>.json> [...]
  python3 knowledge/_tools/validate.py schema <schema.json> <file.json> [...]

Exit status: 0 clean, 1 schema errors, 2 warnings only. Lines starting "note:" are information and never change it.

Dossiers: coverage against the source manifest, and copied source wording.
Concept notes and visuals (knowledge/_meta/writing-guide.md): identifiers that resolve, rung coverage, the novice
contract on entry-rung prose, unbalanced $ delimiters, mentions of the source books, and copied source wording.

Supports the JSON Schema subset used in knowledge/_schemas: type, enum, required, properties, additionalProperties,
items, minItems, minLength, pattern, minimum, maximum, anyOf, and local $ref.
"""
import json
import re
import sys
from functools import lru_cache
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
KB = ROOT / 'knowledge'
SRC = ROOT / 'book-sources'
TYPES = {'object': dict, 'array': list, 'string': str, 'boolean': bool, 'null': type(None)}
NOT_PROSE = {'latex', 'formulas', 'image_path', 'result', 'label', 'number', 'name', 'aliases', 'title', 'target'}
SHINGLE = 12


def is_type(v, t):
	if t == 'integer':
		return isinstance(v, int) and not isinstance(v, bool)
	if t == 'number':
		return isinstance(v, (int, float)) and not isinstance(v, bool)
	return isinstance(v, TYPES[t])


def check(v, s, root, path, errs):
	if '$ref' in s:
		return check(v, root['definitions'][s['$ref'].split('/')[-1]], root, path, errs)
	if 'anyOf' in s:
		if not any(not _errors(v, sub, root, path) for sub in s['anyOf']):
			errs.append(f'{path}: does not match any allowed shape')
		return
	if 'enum' in s and v not in s['enum']:
		errs.append(f'{path}: {v!r} is not one of {s["enum"]}')
		return
	if 'type' in s:
		ts = s['type'] if isinstance(s['type'], list) else [s['type']]
		if not any(is_type(v, t) for t in ts):
			errs.append(f'{path}: expected {s["type"]}, got {type(v).__name__}')
			return
	if isinstance(v, dict):
		for k in s.get('required', []):
			if k not in v:
				errs.append(f'{path}: missing required "{k}"')
		props, extra = s.get('properties', {}), s.get('additionalProperties', True)
		for k, x in v.items():
			if k in props:
				check(x, props[k], root, f'{path}.{k}', errs)
			elif extra is False:
				errs.append(f'{path}: unexpected property "{k}"')
			elif isinstance(extra, dict):
				check(x, extra, root, f'{path}.{k}', errs)
	if isinstance(v, list):
		if len(v) < s.get('minItems', 0):
			errs.append(f'{path}: needs at least {s["minItems"]} items')
		if 'items' in s:
			for i, x in enumerate(v):
				check(x, s['items'], root, f'{path}[{i}]', errs)
	if isinstance(v, str):
		if len(v) < s.get('minLength', 0):
			errs.append(f'{path}: shorter than {s["minLength"]} characters')
		if 'pattern' in s and not re.search(s['pattern'], v):
			errs.append(f'{path}: {v!r} does not match {s["pattern"]}')
	if is_type(v, 'number'):
		if 'minimum' in s and v < s['minimum']:
			errs.append(f'{path}: below minimum {s["minimum"]}')
		if 'maximum' in s and v > s['maximum']:
			errs.append(f'{path}: above maximum {s["maximum"]}')


def _errors(v, s, root, path):
	errs = []
	check(v, s, root, path, errs)
	return errs


def words(s):
	return re.findall(r"[a-z0-9]+", s.lower())


def prose(obj, key=None):
	if isinstance(obj, dict):
		for k, v in obj.items():
			if k not in NOT_PROSE:
				yield from prose(v, k)
	elif isinstance(obj, list):
		for v in obj:
			yield from prose(v, key)
	elif isinstance(obj, str):
		yield key, obj


def pdf_pages(obj, skip=('cross_references',)):
	if isinstance(obj, dict):
		for k, v in obj.items():
			if k in skip:
				continue
			if k == 'pdf_page' and isinstance(v, int):
				yield v
			else:
				yield from pdf_pages(v, skip)
	elif isinstance(obj, list):
		for v in obj:
			yield from pdf_pages(v, skip)


def dossier_warnings(d, path):
	warns = []
	manifest = json.loads((SRC / '_chapters' / d['book'] / 'manifest.json').read_text())
	unit = next((u for u in manifest['units'] if u['id'] == d['unit_id']), None)
	if not unit:
		return [f'unit "{d["unit_id"]}" is not in the {d["book"]} manifest'], []
	toc = json.loads((KB / 'sources' / d['book'] / 'toc.json').read_text())
	toc_unit = next((u for u in toc['units'] if u['id'] == d['unit_id']), {})
	lo, hi = unit['pdf_pages']
	if d.get('pdf_pages') != [lo, hi]:
		warns.append(f'pdf_pages should be [{lo}, {hi}]')

	outside = sorted({p for p in pdf_pages(d) if not lo <= p <= hi})
	if outside:
		warns.append(f'pdf_page values outside this unit ({lo}-{hi}): {outside}')

	have = {s.get('number') for s in d.get('sections', [])}
	missing = [s['number'] for s in toc_unit.get('sections', []) if s['number'] not in have]
	if missing:
		warns.append(f'TOC sections missing from sections[]: {missing}')

	inv = unit.get('inventory', {})
	described = {f.get('image_path') for f in d.get('figures', [])}
	missing = [f['image_path'] for f in inv.get('figures', []) if f['image_path'] not in described]
	if missing:
		warns.append(
			f'{len(missing)} inventory images have no figures[] entry (describe each; use redesign.form '
			f'"not-worth-redesigning" for decorative ones): {missing}'
		)
	for f in d.get('figures', []):
		if f.get('image_path') and not (SRC / f['image_path']).exists():
			warns.append(f'image_path does not exist under book-sources/: {f["image_path"]}')

	labels = ' | '.join((e.get('label') or '') for e in d.get('worked_examples', []))
	missing = [e['label'] for e in inv.get('examples', []) if e['label'] not in labels]
	if missing:
		warns.append(f'inventory examples missing from worked_examples[]: {missing}')

	source = words((SRC / unit['reading_file']).read_text(errors='replace'))
	shingles = {' '.join(source[i : i + SHINGLE]) for i in range(len(source) - SHINGLE + 1)}
	copied = []
	for key, text in prose(d):
		ws = words(text)
		for i in range(len(ws) - SHINGLE + 1):
			if ' '.join(ws[i : i + SHINGLE]) in shingles:
				copied.append(f'{key}: "{" ".join(ws[i:i + SHINGLE])} ..."')
				break
	if copied:
		warns.append(
			f'{len(copied)} prose fields repeat {SHINGLE}+ consecutive source words; paraphrase them: ' + '; '.join(copied[:12])
		)
	return warns, []


# ---- Concept notes and visuals ------------------------------------------------------------------------------

BOOKS = ('schutz', 'gifted-amateur', 'dinverno')
KEBAB = re.compile(r'^[a-z0-9]+(-[a-z0-9]+)*$')
NOTE_SKIP = {'latex', 'equations', 'provenance', 'review', 'id', 'assumes', 'symbol', 'schema_version'}
BOOKISH = [
	re.compile(r"\b(Schutz|Blundell|Lancaster|d['’]\s?Inverno|Vickers|Gifted Amateur)\b", re.I),
	re.compile(r'\b(SCH|GA|DIV)\s+(ch\d|app[A-E]|§|Ex|Fig|Box|p\.)'),
	re.compile(r'\blegacy:[a-z0-9-]+'),
	re.compile(r'§\s?\d'),
	re.compile(r'\bpp?\.\s?\d+'),
	re.compile(r'\b(Exercise|Example|Problem|Figure|Fig\.|Box|Table|Section|Chapter|Eq\.|Equation)s?\s\(?\d+[.-]\d+', re.I),
	re.compile(r'\b(one|another|each|this|that|the|our)\s+(popular\s+|standard\s+)?textbooks?\b|\bthe\s+authors?\b|\b(in|from|by)\s+the\s+book\b', re.I),
]
MATH = re.compile(r'\$\$.+?\$\$|\$[^$]+?\$', re.S)
HEDGE = re.compile(
	r'\b(clearly|obviously|trivially|evidently|it is easy to see|of course|needless to say|as is well known|recall that|it follows immediately)\b',
	re.I,
)
# Technical words the entry rung must define in its glossary if it uses them (writing guide §3 rule 4).
TECHNICAL = [
	'vector', 'tangent', 'coordinate', 'metric', 'tensor', 'geodesic', 'invariant', 'manifold', 'curvature', 'component',
	'derivative', 'spacetime', 'worldline', 'proper time', 'inertial', 'parallel transport', 'holonomy', 'scalar',
	'basis', 'covariant', 'contravariant', 'index', 'indices', 'integral', 'gradient', 'divergence', 'flux', 'topology',
	'singularity', 'redshift', 'stress-energy', 'energy-momentum', 'gauge', 'intrinsic', 'extrinsic', 'tidal',
	'Christoffel', 'Riemann', 'Ricci', 'Lorentz', 'Gaussian', 'eigenvalue', 'four-vector', 'reference frame',
]


@lru_cache(maxsize=None)
def registry_entries():
	out = {}
	for f in (KB / 'concepts').glob('*/_registry.json'):
		for c in json.loads(f.read_text())['concepts']:
			out[c['id']] = (f.parent.name, c)
	return out


@lru_cache(maxsize=None)
def legacy_ids():
	return frozenset(a['id'] for f in (KB / 'sources' / 'legacy').glob('*.json') for a in json.loads(f.read_text()).get('assets', []))


@lru_cache(maxsize=None)
def unit_shingles(book, unit):
	f = SRC / '_chapters' / book / f'{unit}.md'
	if not f.exists():
		return frozenset()
	ws = words(f.read_text(errors='replace'))
	return frozenset(' '.join(ws[i : i + SHINGLE]) for i in range(len(ws) - SHINGLE + 1))


def strings(obj, skip, path='$'):
	if isinstance(obj, dict):
		for k, v in obj.items():
			if k not in skip:
				yield from strings(v, skip, f'{path}.{k}')
	elif isinstance(obj, list):
		for i, v in enumerate(obj):
			yield from strings(v, skip, f'{path}[{i}]')
	elif isinstance(obj, str):
		yield path, obj


def plain(s):
	return MATH.sub(' X ', s)


def sentence_lengths(s):
	parts = re.split(r'(?<=[.!?])\s+|\n+', plain(s).strip())
	return [n for n in (len(re.findall(r"[A-Za-z0-9][A-Za-z0-9'’-]*", p)) for p in parts) if n]


def novice_warnings(label, text, max_math=3):
	warns = []
	lens = sentence_lengths(text)
	long = [n for n in lens if n > 32]
	if long:
		warns.append(f'{label}: {len(long)} sentence(s) over 32 words ({max(long)} max); the novice contract needs short sentences')
	if len(lens) >= 3 and sum(lens) / len(lens) > 20:
		warns.append(f'{label}: average sentence is {sum(lens) / len(lens):.0f} words; aim for 20 or fewer')
	hedges = sorted({h.lower() for h in HEDGE.findall(text)})
	if hedges:
		warns.append(f'{label}: remove {hedges}')
	n = len(MATH.findall(text))
	if n > max_math:
		warns.append(f'{label}: {n} math expressions; the entry rung allows {max_math}, each read out in words')
	return warns


def common_lints(d):
	warns = []
	for path, s in strings(d, NOTE_SKIP):
		if s.replace('\\$', '').count('$') % 2:
			warns.append(f'{path}: unbalanced $ math delimiters')
		for rx in BOOKISH:
			m = rx.search(s)
			if m:
				warns.append(f'{path}: mentions a source book or locator ("{m.group(0)}"); write in our own voice, sources go in provenance only')
				break
	return warns


def copy_warnings(d, units):
	shingles = set()
	for book, unit in units:
		shingles |= unit_shingles(book, unit)
	hits = []
	for path, s in strings(d, NOTE_SKIP):
		ws = words(s)
		for i in range(len(ws) - SHINGLE + 1):
			if ' '.join(ws[i : i + SHINGLE]) in shingles:
				hits.append(f'{path}: "{" ".join(ws[i:i + SHINGLE])} ..."')
				break
	return [f'{len(hits)} fields repeat {SHINGLE}+ consecutive words from a source; rewrite them in your own words: ' + '; '.join(hits[:12])] if hits else []


def provenance_units(prov, warns):
	units = set()
	for u in prov.get('source_units', []):
		book, _, unit = u.partition('/')
		if book not in BOOKS or not (SRC / '_chapters' / book / f'{unit}.md').exists():
			warns.append(f'provenance source unit "{u}" does not exist (format book/unit, e.g. schutz/ch06)')
		else:
			units.add((book, unit))
	return units


def concept_warnings(d, path):
	warns, notes = [], []
	reg, legacy = registry_entries(), legacy_ids()
	cid, p = d['id'], Path(path)
	if p.stem != cid:
		warns.append(f'file name should be {cid}.json')
	if cid not in reg:
		warns.append(f'id "{cid}" is not in any _registry.json')
	elif reg[cid][0] != d['domain'] or p.parent.name != d['domain']:
		warns.append(f'domain should be "{reg[cid][0]}" and the file should live in concepts/{reg[cid][0]}/')
	elif reg[cid][1]['tier'] != d['tier']:
		warns.append(f'tier should be "{reg[cid][1]["tier"]}" as in the registry')

	def known(where, i):
		if i not in reg:
			warns.append(f'{where}: "{i}" is not a registry concept id')

	pre = [x['id'] for x in d['prerequisites']]
	for i in pre:
		known('prerequisites', i)
	for x in d['leads_to']:
		known('leads_to', x['id'])
	for x in d['related']:
		known('related', x['id'])
	if cid in pre:
		warns.append('a concept cannot be its own prerequisite')
	both = set(pre) & {x['id'] for x in d['leads_to']}
	if both:
		warns.append(f'ids in both prerequisites and leads_to: {sorted(both)}')

	ways = d['ways_in']
	way_ids = [w['id'] for w in ways]
	if len(set(way_ids)) != len(way_ids):
		warns.append('ways_in ids must be unique')
	for w in ways:
		for a in w['assumes']:
			known(f'ways_in[{w["id"]}].assumes', a)
	rungs = {w['rung'] for w in ways}
	for r in ('entry', 'working', 'formal'):
		if r not in rungs:
			warns.append(f'ways_in needs at least one "{r}" way')
	if d['tier'] in ('advanced', 'frontier') and 'research' not in rungs and not d['research_horizon']:
		warns.append('advanced and frontier notes need a research way or research_horizon entries')
	check_rungs = {c['rung'] for c in d['checks']}
	for r in ('entry', 'working', 'formal'):
		if r not in check_rungs:
			warns.append(f'checks need at least one "{r}" question')
	beliefs = {m['belief'] for m in d['misconceptions']}
	for c in d['checks']:
		t = c.get('targets_misconception')
		if t and t not in beliefs:
			warns.append(f'checks: targets_misconception "{t[:70]}" does not exactly match any misconception belief')
	if d['misconceptions'] and not any(c.get('targets_misconception') for c in d['checks']):
		warns.append('at least one check should target a misconception')
	if d['tier'] in ('foundation', 'core') and not d['worked_examples']:
		warns.append('foundation and core notes need at least one worked example')

	vis = {v['id'] for v in d['visuals']}
	for v in d['visuals']:
		if not KEBAB.match(v['id']):
			warns.append(f'visual id "{v["id"]}" must be kebab-case')
		elif not (KB / 'visuals' / f'{v["id"]}.json').exists():
			if v.get('sketch'):
				notes.append(f'visual "{v["id"]}" is proposed (not in knowledge/visuals/ yet)')
			else:
				warns.append(f'visual "{v["id"]}" is not in knowledge/visuals/; give it a sketch')
	for w in ways:
		missing = [x for x in w['visuals'] if x not in vis]
		if missing:
			warns.append(f'ways_in[{w["id"]}].visuals are not listed in visuals[]: {missing}')

	for e in d['key_equations']:
		if '$' in e['say_aloud'] or '\\' in e['say_aloud']:
			warns.append(f'key_equations[{e["name"]}].say_aloud must be plain words, not LaTeX')
	for h in d['history']:
		if not re.match(r'^(c\. )?\d{3,4}s?([–-]\d{2,4})?$', h['year']):
			warns.append(f'history year "{h["year"]}" should look like 1915, 1915–1916, or 1920s')

	entry_text = [('summary', d['summary'], 1)] + [(f'ways_in[{w["id"]}]', w['explanation'], 3) for w in ways if w['rung'] == 'entry']
	entry_text += [('checks(entry)', c['question'] + '\n' + c['answer'], 3) for c in d['checks'] if c['rung'] == 'entry']
	entry_text += [(f'glossary[{g["term"]}]', g['plain_definition'], 1) for g in d['glossary']]
	for label, text, max_math in entry_text:
		warns += novice_warnings(label, text, max_math)
	for w in ways:
		if w['rung'] == 'entry':
			n = len(words(plain(w['explanation'])))
			if n < 120:
				warns.append(f'ways_in[{w["id"]}]: entry explanation has {n} words; be explicit enough that a beginner cannot get lost (120+)')
			elif n > 750:
				warns.append(f'ways_in[{w["id"]}]: entry explanation has {n} words; split it into two ways')
	terms = ' | '.join(g['term'].lower() for g in d['glossary'])
	entry_blob = ' '.join(plain(t) for label, t, _ in entry_text if not label.startswith('glossary')).lower()
	undefined = [t for t in TECHNICAL if re.search(rf'\b{re.escape(t.lower())}(s|es)?\b', entry_blob) and t.lower() not in terms]
	if undefined:
		warns.append(f'entry rung uses technical words the glossary does not define: {undefined}')

	units = provenance_units(d['provenance'], warns)
	for a in d['provenance']['legacy_assets']:
		if a not in legacy:
			warns.append(f'provenance legacy asset "{a}" does not exist')
	if cid in reg:
		units |= {(s['book'], s['unit']) for s in reg[cid][1]['sources'] if s['book'] in BOOKS}
	warns += common_lints(d)
	warns += copy_warnings(d, units)

	total = sum(len(words(plain(s))) for _, s in strings(d, NOTE_SKIP))
	if total > 5000:
		warns.append(f'note has {total} words; remove repetition (target 1,200-3,500)')
	notes.append(f'{total} words; rungs {sorted(rungs)}; {len(d["checks"])} checks; {len(vis)} visuals')
	return warns, notes


def visual_warnings(d, path):
	warns, notes = [], []
	reg, legacy = registry_entries(), legacy_ids()
	if Path(path).stem != d['id']:
		warns.append(f'file name should be {d["id"]}.json')
	for s in d['serves']:
		if s['concept'] not in reg:
			warns.append(f'serves: "{s["concept"]}" is not a registry concept id')
	links = [('builds_on', v) for v in d['builds_on']] + [('leads_to', v) for v in d['leads_to']]
	if d['variant_of']:
		links.append(('variant_of', d['variant_of']))
	for key, v in links:
		if not KEBAB.match(v):
			warns.append(f'{key}: "{v}" must be a kebab-case visual id')
		elif not (KB / 'visuals' / f'{v}.json').exists():
			notes.append(f'{key} "{v}" is not in the catalog yet')
	if d['kind'] != 'static-figure' and not d['model']['tests']:
		warns.append('interactive, animated, and plotted visuals need model tests')
	if 'entry' in d['rungs']:
		warns += novice_warnings('picture.caption', d['picture']['caption'], 0)
		for i, b in enumerate(d['tour']):
			warns += novice_warnings(f'tour[{i}].say', b['say'], 0)
	for i, b in enumerate(d['tour']):
		if '\\' in b['say']:
			warns.append(f'tour[{i}].say must be spoken words, not LaTeX')
	for a in d['starting_material']['legacy_assets']:
		if a not in legacy:
			warns.append(f'starting_material legacy asset "{a}" does not exist')
	units = provenance_units(d['provenance'], warns)
	for img in d['provenance']['figure_images']:
		if not (SRC / img).exists():
			warns.append(f'provenance figure image "{img}" does not exist under book-sources/')
	warns += common_lints(d)
	warns += copy_warnings(d, units)
	return warns, notes


MODES = {
	'dossier': ('chapter-dossier.schema.json', dossier_warnings),
	'concept': ('concept-note.schema.json', concept_warnings),
	'visual': ('visual.schema.json', visual_warnings),
}


def main(argv):
	if len(argv) < 3 or argv[1] not in (*MODES, 'schema'):
		print(__doc__)
		return 1
	if argv[1] == 'schema':
		schema_path, files, extra = Path(argv[2]), argv[3:], None
	else:
		name, extra = MODES[argv[1]]
		schema_path, files = KB / '_schemas' / name, argv[2:]
	schema = json.loads(Path(schema_path).read_text())
	status = 0
	for f in files:
		try:
			data = json.loads(Path(f).read_text())
		except (OSError, json.JSONDecodeError) as e:
			print(f'ERROR {f}: cannot parse JSON: {e}')
			status = 1
			continue
		errs = _errors(data, schema, schema, '$')
		warns, notes = extra(data, f) if extra and not errs else ([], [])
		print(f"{'ERRORS' if errs else 'WARNINGS' if warns else 'OK'} {f}")
		for e in errs[:60]:
			print('  error:', e)
		if len(errs) > 60:
			print(f'  ... {len(errs) - 60} more errors')
		for w in warns:
			print('  warning:', w)
		for n in notes:
			print('  note:', n)
		status = 1 if errs or status == 1 else max(status, 2 if warns else 0)
	return status


if __name__ == '__main__':
	sys.exit(main(sys.argv))
