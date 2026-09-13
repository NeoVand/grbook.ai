#!/usr/bin/env python3
"""Validate knowledge-vault JSON against its schema, plus content checks.

Usage:
  python3 knowledge/_tools/validate.py dossier <sources/<book>/chapters/<unit>.json> [...]
  python3 knowledge/_tools/validate.py concept <concepts/<domain>/<id>.json> [...]
  python3 knowledge/_tools/validate.py visual <visuals/<id>.json> [...]
  python3 knowledge/_tools/validate.py schema <schema.json> <file.json> [...]

Exit status: 0 clean, 1 schema errors, 2 warnings only. Lines starting "note:" are information and never change it.

Dossiers: coverage against the source manifest, and copied source wording.
Concept notes and visuals (knowledge/_meta/writing-guide.md): ids and addresses that resolve, rung and tier
requirements, the novice contract on entry-rung reading, text formats (x-format), graph consistency, length budgets,
component-contract consistency for visuals, mentions of the source books, and copied source wording.

Supports the JSON Schema subset used in knowledge/_schemas: type, enum, required, properties, additionalProperties,
items, minItems, maxItems, minLength, maxLength, pattern, minimum, maximum, anyOf, local $ref, and the custom
x-format keyword.
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
FORMATTED = []  # (path, format, text) collected while checking a file against its schema


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
		else:
			for sub in s['anyOf']:
				if not _errors(v, sub, root, path):
					check(v, sub, root, path, [])
					break
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
		if 'maxItems' in s and len(v) > s['maxItems']:
			errs.append(f'{path}: allows at most {s["maxItems"]} items')
		if 'items' in s:
			for i, x in enumerate(v):
				check(x, s['items'], root, f'{path}[{i}]', errs)
	if isinstance(v, str):
		if len(v) < s.get('minLength', 0):
			errs.append(f'{path}: shorter than {s["minLength"]} characters')
		if 'maxLength' in s and len(v) > s['maxLength']:
			errs.append(f'{path}: longer than {s["maxLength"]} characters ({len(v)})')
		if 'pattern' in s and not re.search(s['pattern'], v):
			errs.append(f'{path}: {v!r} does not match {s["pattern"]}')
		if 'x-format' in s and errs is not None:
			FORMATTED.append((path, s['x-format'], v))
	if is_type(v, 'number'):
		if 'minimum' in s and v < s['minimum']:
			errs.append(f'{path}: below minimum {s["minimum"]}')
		if 'maximum' in s and v > s['maximum']:
			errs.append(f'{path}: above maximum {s["maximum"]}')


def _errors(v, s, root, path):
	errs = []
	saved = len(FORMATTED)
	check(v, s, root, path, errs)
	del FORMATTED[saved:]
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


# ---- Shared checks for concept notes and visuals -------------------------------------------------------------

BOOKS = ('schutz', 'gifted-amateur', 'dinverno')
RUNG = {'entry': 0, 'working': 1, 'formal': 2, 'research': 3}
KEBAB = re.compile(r'^[a-z0-9]+(-[a-z0-9]+)*$')
NOTE_SKIP = {'latex', 'symbol', 'provenance', 'review', 'id', 'assumes', 'schema_version', 'refs', 'uses', 'evidenced_by', 'targets', 'diagnosed_by', 'state', 'expect'}
COLLECTIONS = [
	'ways_in', 'objectives', 'key_equations', 'derivations', 'worked_examples', 'problems', 'observations', 'checks',
	'misconceptions', 'analogies', 'glossary', 'teaching_arc', 'notation_traps', 'history', 'research_horizon',
]
TUTOR_COLLECTIONS = ['opening_questions', 'if_stuck', 'common_questions']
ADDRESS = re.compile(r'^(?:([a-z0-9]+(?:-[a-z0-9]+)*)/)?([a-z_]+)/([a-z0-9]+(?:-[a-z0-9]+)*)$')
BOOKISH = [
	re.compile(r"\b(Schutz|Blundell|Lancaster|d['’]\s?Inverno|Vickers|Gifted Amateur)\b", re.I),
	re.compile(r'\b(SCH|GA|DIV)\s+(ch\d|app[A-E]|§|Ex|Fig|Box|p\.)'),
	re.compile(r'\blegacy:[a-z0-9-]+'),
	re.compile(r'§\s?\d'),
	re.compile(r'\bpp?\.\s?\d+'),
	re.compile(r'\b(Exercise|Example|Problem|Figure|Fig\.|Box|Table|Section|Chapter|Eq\.|Equation)s?\s\(?\d+[.-]\d+', re.I),
	re.compile(r'\b(one|another|each|this|that|the|our)\s+(popular\s+|standard\s+)?textbooks?\b|\bthe\s+authors?\b|\b(in|from|by)\s+the\s+book\b', re.I),
]
MATH = re.compile(r'\$\$.+?\$\$|(?<!\\)\$[^$]+?(?<!\\)\$', re.S)
HEDGE = re.compile(
	r'\b(clearly|obviously|trivially|evidently|it is easy to see|of course|needless to say|as is well known|recall that|it follows immediately)\b',
	re.I,
)
POSITIONAL = re.compile(r'\b(given|shown|derived|discussed|described|see|as)\s+(above|below|earlier)\b|\b(above|below)\s+(derivation|example|equation|section|way)\b', re.I)
SPEECH_BAD = re.compile(r'[$\\^_`#]|[⁰¹²³⁴⁵⁶⁷⁸⁹⁻₀₁₂₃₄₅₆₇₈₉×]')
MD_PSEUDO_MATH = re.compile(r'[A-Za-zΑ-Ωα-ω][\^_][{A-Za-zΑ-Ωα-ω0-9]|[₀₁₂₃₄₅₆₇₈₉⁰¹⁴⁵⁶⁷⁸⁹⁻]|[α-ωΓΔΘΛΞΠΣΦΨΩ∂∇∮∫]')
# Technical words the entry rung must define in its glossary if it uses them (writing guide section 4, rule 4).
TECHNICAL = [
	'vector', 'tangent', 'coordinate', 'metric', 'tensor', 'geodesic', 'invariant', 'manifold', 'curvature', 'component',
	'derivative', 'spacetime', 'worldline', 'proper time', 'inertial', 'parallel transport', 'holonomy', 'scalar',
	'basis', 'covariant', 'contravariant', 'indices', 'integral', 'gradient', 'divergence', 'flux', 'topology',
	'singularity', 'redshift', 'stress-energy', 'energy-momentum', 'gauge', 'intrinsic', 'extrinsic', 'tidal',
	'Christoffel', 'Riemann', 'Ricci', 'Lorentz', 'Gaussian', 'eigenvalue', 'four-vector', 'reference frame', 'radian',
	'geodetic', 'precession', 'quadrupole', 'entropy', 'horizon',
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


@lru_cache(maxsize=None)
def load_json(path):
	try:
		return json.loads(Path(path).read_text())
	except (OSError, json.JSONDecodeError):
		return None


def v2_note(cid):
	reg = registry_entries()
	if cid not in reg:
		return None
	d = load_json(str(KB / 'concepts' / reg[cid][0] / f'{cid}.json'))
	return d if d and d.get('schema_version') == 2 else None


def catalog_visual(vid):
	d = load_json(str(KB / 'visuals' / f'{vid}.json'))
	return d if d and d.get('schema_version') == 2 else None


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


COUNT_SKIP = NOTE_SKIP | {'authors', 'venue', 'doi', 'arxiv', 'kind', 'forms', 'say_as', 'pronunciations', 'title', 'name', 'label', 'symbol', 'unit', 'quantity', 'status', 'updated', 'domain', 'tier', 'rung', 'format', 'priority', 'needed_for', 'invites', 'to_rung'}


def wc(obj):
	return sum(len(words(plain(s))) for _, s in strings(obj, COUNT_SKIP))


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
		warns.append(f'{label}: {n} math expressions; the entry rung allows {max_math} here, each read out in words')
	return warns


def format_warnings():
	warns = []
	for path, fmt, s in FORMATTED:
		if fmt in ('speech', 'plain'):
			m = SPEECH_BAD.search(s)
			if m:
				warns.append(f'{path}: {fmt} text must not contain "{m.group(0)}" (no math, markup, or symbols; write it in words)')
		elif fmt == 'md':
			t = s.replace('\\$', '')
			if t.count('$') % 2:
				warns.append(f'{path}: unbalanced $ math delimiters')
			m = MD_PSEUDO_MATH.search(plain(t))
			if m:
				warns.append(f'{path}: "{m.group(0)}" outside $...$; put symbols, indices, and Greek letters inside math')
			m = POSITIONAL.search(s)
			if m:
				warns.append(f'{path}: "{m.group(0)}" points by position; name the thing or use refs')
		elif fmt == 'latex' and '$' in s:
			warns.append(f'{path}: latex fields take bare LaTeX without $ delimiters')
	return warns


def common_lints(d):
	warns = []
	for path, s in strings(d, NOTE_SKIP):
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


def item_maps(d):
	cols = {k: {x['id']: x for x in d.get(k, [])} for k in COLLECTIONS}
	for k in TUTOR_COLLECTIONS:
		cols[k] = {x['id']: x for x in d.get('tutor_moves', {}).get(k, [])}
	return cols


def resolve(addr, d, cols, where, warns, notes):
	m = ADDRESS.match(addr)
	if not m:
		warns.append(f'{where}: "{addr}" is not an address like checks/<id> or <concept>/checks/<id>')
		return None
	cid, coll, item = m.groups()
	if coll not in COLLECTIONS and coll not in TUTOR_COLLECTIONS:
		warns.append(f'{where}: "{addr}" names unknown collection "{coll}"')
		return None
	if cid is None or cid == d['id']:
		if item not in cols[coll]:
			warns.append(f'{where}: "{addr}" does not resolve in this note')
			return None
		return coll, cols[coll][item], True
	if cid not in registry_entries():
		warns.append(f'{where}: "{addr}" names unknown concept "{cid}"')
		return None
	other = v2_note(cid)
	if other is None:
		notes.append(f'{where}: "{addr}" points to a concept without a v2 note yet')
		return None
	if item not in item_maps(other)[coll]:
		warns.append(f'{where}: "{addr}" does not resolve in {cid}')
		return None
	return coll, item_maps(other)[coll][item], False


def references(d):
	for h in d.get('history', []):
		if h.get('work'):
			yield f'history/{h["id"]}', h['work']
	for r in d.get('research_horizon', []):
		for ref in r['references']:
			yield f'research_horizon/{r["id"]}', ref
	for o in d.get('observations', []):
		if o.get('reference'):
			yield f'observations/{o["id"]}', o['reference']


# ---- Concept notes ------------------------------------------------------------------------------------------------


def entry_texts(d):
	t = [('summary', d['summary'], 1), ('tagline', d['tagline'], 0)]
	for w in d['ways_in']:
		if w['rung'] == 'entry':
			for k in ('gist', 'recap', 'explanation', 'try_it', 'takeaway', 'retell', 'picture', 'simplifies'):
				if w.get(k):
					t.append((f'ways_in/{w["id"]}.{k}', w[k], 3 if k == 'explanation' else 1))
	t += [(f'glossary/{g["id"]}', g['plain_definition'], 1) for g in d['glossary']]
	t += [(f'objectives/{o["id"]}', o['can_do'], 0) for o in d['objectives'] if o['rung'] == 'entry']
	for c in d['checks']:
		if c['rung'] == 'entry':
			t += [(f'checks/{c["id"]}.question', c['question'], 1), (f'checks/{c["id"]}.answer', c['answer'], 2)]
			t += [(f'checks/{c["id"]}.hints', h, 1) for h in c['hints']]
	for m in d['misconceptions']:
		if m['rung'] == 'entry':
			t += [(f'misconceptions/{m["id"]}.{k}', m[k], 1) for k in ('belief', 'why_tempting', 'correction')]
	for a in d['analogies']:
		if a['rung'] == 'entry':
			t += [(f'analogies/{a["id"]}.{k}', a[k], 1) for k in ('explanation', 'limits')]
	for p in d['problems']:
		if p['rung'] == 'entry':
			t += [(f'problems/{p["id"]}.statement', p['statement'], 2), (f'problems/{p["id"]}.answer', p['answer'], 2)]
			t += [(f'problems/{p["id"]}.solution', s, 2) for s in p['solution']]
	for o in d['observations']:
		if o['rung'] == 'entry':
			t += [(f'observations/{o["id"]}.{k}', o[k], 1) for k in ('phenomenon', 'connection', 'numbers') if o.get(k)]
	t += [(f'opening_questions/{q["id"]}', q['question'], 0) for q in d['tutor_moves']['opening_questions']]
	for q in d['tutor_moves']['common_questions']:
		if q['rung'] == 'entry':
			t += [(f'common_questions/{q["id"]}.question', q['question'], 0), (f'common_questions/{q["id"]}.answer', q['answer'], 1)]
	return t


def ancestors(ids):
	reg, seen, stack = registry_entries(), set(), list(ids)
	while stack:
		n = stack.pop()
		if n in seen:
			continue
		seen.add(n)
		if n in reg:
			stack.extend(reg[n][1]['prerequisites'])
	return seen


def concept_warnings(d, path):
	warns, notes = [], []
	reg, legacy = registry_entries(), legacy_ids()
	cid, p, tier = d['id'], Path(path), d['tier']
	if p.stem != cid:
		warns.append(f'file name should be {cid}.json')
	if cid not in reg:
		warns.append(f'id "{cid}" is not in any _registry.json')
	elif reg[cid][0] != d['domain'] or p.parent.name != d['domain']:
		warns.append(f'domain should be "{reg[cid][0]}" and the file should live in concepts/{reg[cid][0]}/')
	elif reg[cid][1]['tier'] != tier:
		warns.append(f'tier should be "{reg[cid][1]["tier"]}" as in the registry')

	cols = item_maps(d)
	for coll in COLLECTIONS + TUTOR_COLLECTIONS:
		src = d.get(coll, []) if coll in COLLECTIONS else d['tutor_moves'][coll]
		ids = [x['id'] for x in src]
		dups = sorted({i for i in ids if ids.count(i) > 1})
		if dups:
			warns.append(f'{coll}: duplicate ids {dups}')

	# Graph: registry ids, prerequisites, assumes, leads_to.
	def known(where, i):
		if i not in reg:
			warns.append(f'{where}: "{i}" is not a registry concept id')

	pre = {x['id']: RUNG[x['needed_for']] for x in d['prerequisites']}
	leads = {x['id'] for x in d['leads_to']}
	for i in pre:
		known('prerequisites', i)
	for i in leads:
		known('leads_to', i)
	for x in d['related']:
		known('related', x['id'])
	if cid in pre:
		warns.append('a concept cannot be its own prerequisite')
	if set(pre) & leads:
		warns.append(f'ids in both prerequisites and leads_to: {sorted(set(pre) & leads)}')
	if cid in reg:
		diff = set(pre) ^ set(reg[cid][1]['prerequisites'])
		if diff:
			notes.append(f'prerequisites differ from the registry for {sorted(diff)} (sync_registry.py applies reviewed notes)')
	deep = ancestors(pre)

	# Ways in.
	ways = d['ways_in']
	order = {w['id']: i for i, w in enumerate(ways)}
	rungs = {w['rung'] for w in ways}
	for r in ('entry', 'working', 'formal'):
		if r not in rungs:
			warns.append(f'ways_in needs at least one "{r}" way')
	if tier in ('advanced', 'frontier') and 'research' not in rungs:
		warns.append('advanced and frontier notes need a research way')
	if len({w['kind'] for w in ways}) < 2:
		warns.append('ways_in must use at least two different kinds')
	if len({w['question'] for w in ways}) < len(ways):
		warns.append('each way must answer a different question')
	for w in ways:
		where = f'ways_in/{w["id"]}'
		if w['rung'] == 'entry' and not w['retell']:
			warns.append(f'{where}: entry ways need a retell')
		if w['rung'] != 'entry':
			if not w['continues']:
				warns.append(f'{where}: non-entry ways name the earlier way they climb from in continues')
			elif w['continues'] not in order or order[w['continues']] >= order[w['id']]:
				warns.append(f'{where}: continues "{w["continues"]}" must be an earlier way in this note')
		for a in w['assumes']:
			known(f'{where}.assumes', a)
			if a in leads:
				warns.append(f'{where}: assumes "{a}", which is also in leads_to (cycle)')
			elif a in pre:
				if pre[a] > RUNG[w['rung']]:
					warns.append(f'{where}: assumes "{a}", but its prerequisite needed_for is above this way\'s rung')
			elif a not in deep:
				warns.append(f'{where}: assumes "{a}", which is not a prerequisite (direct, or of a prerequisite)')
		for r in w['refs']:
			resolve(r, d, cols, f'{where}.refs', warns, notes)
		if w['rung'] == 'entry':
			n = len(words(plain(w['explanation'])))
			if n < 150:
				warns.append(f'{where}: entry explanation has {n} words; be explicit enough that a beginner cannot get lost')

	# Objectives, checks, misconceptions, problems.
	for coll, need in (('objectives', ('entry', 'working', 'formal')), ('checks', ('entry', 'working', 'formal'))):
		have = {x['rung'] for x in d[coll]}
		for r in need:
			if r not in have:
				warns.append(f'{coll} need at least one "{r}" item')
	if tier in ('advanced', 'frontier') and 'research' not in {o['rung'] for o in d['objectives']}:
		warns.append('advanced and frontier notes need a research objective')
	evidenced = set()
	for o in d['objectives']:
		for a in o['evidenced_by']:
			r = resolve(a, d, cols, f'objectives/{o["id"]}.evidenced_by', warns, notes)
			if r:
				if r[0] not in ('checks', 'problems', 'worked_examples') or not r[2]:
					warns.append(f'objectives/{o["id"]}: evidenced_by must point to checks, problems, or worked_examples in this note')
				evidenced.add((r[0], r[1]['id']))
	unassessed = [f'checks/{c}' for c in cols['checks'] if ('checks', c) not in evidenced] + [f'problems/{x}' for x in cols['problems'] if ('problems', x) not in evidenced]
	if unassessed:
		warns.append(f'these items evidence no objective: {unassessed}')
	mis, chk = cols['misconceptions'], cols['checks']
	for m in mis.values():
		for c in m['diagnosed_by']:
			if c not in chk:
				warns.append(f'misconceptions/{m["id"]}: diagnosed_by "{c}" is not a check id')
			elif m['id'] not in chk[c]['targets']:
				warns.append(f'misconceptions/{m["id"]}: check "{c}" must list it in targets')
	for c in chk.values():
		for t in c['targets']:
			if t not in mis:
				warns.append(f'checks/{c["id"]}: target "{t}" is not a misconception id')
			elif c['id'] not in mis[t]['diagnosed_by']:
				warns.append(f'checks/{c["id"]}: misconception "{t}" must list this check in diagnosed_by')
		if '$' in c['question'] and not c['question_spoken']:
			warns.append(f'checks/{c["id"]}: the question contains math, so give question_spoken')
		if c['format'] == 'numeric' and not c['numeric']:
			warns.append(f'checks/{c["id"]}: numeric checks need numeric answers with units and tolerance')
	for s in d['tutor_moves']['if_stuck']:
		if s['misconception'] and s['misconception'] not in mis:
			warns.append(f'if_stuck/{s["id"]}: misconception "{s["misconception"]}" is not a misconception id')
	min_problems = {'prerequisite': 1, 'foundation': 2}.get(tier, 3)
	if len(d['problems']) < min_problems:
		warns.append(f'{tier} notes need at least {min_problems} problems')
	if min_problems > 1 and len({x['rung'] for x in d['problems']}) < 2:
		warns.append('problems must span at least two rungs')
	if tier in ('foundation', 'core') and not d['worked_examples']:
		warns.append('foundation and core notes need at least one worked example')
	if tier in ('core', 'advanced', 'frontier') and not 2 <= len(d['research_horizon']) <= 5:
		warns.append('core, advanced, and frontier notes need 2 to 5 research_horizon topics')

	# Equations, teaching arc, visuals.
	for e in d['key_equations']:
		j, where = e['justified_by'], f'key_equations/{e["id"]}.justified_by'
		if j == 'stated':
			continue
		if ADDRESS.match(j):
			r = resolve(j, d, cols, where, warns, notes)
			if r and r[0] == 'derivations' and r[2] and RUNG[r[1]['rung']] > RUNG[e['rung']]:
				warns.append(f'{where}: derivation "{j}" is above the equation\'s rung')
		elif j in reg:
			if j not in pre and j not in deep:
				warns.append(f'{where}: concept "{j}" is not a prerequisite')
		else:
			warns.append(f'{where}: must be derivations/<id>, a prerequisite concept id, or "stated"')
	if not 3 <= len(d['teaching_arc']) <= 8:
		warns.append('teaching_arc needs 3 to 8 steps')
	for s in d['teaching_arc']:
		for u in s['uses']:
			resolve(u, d, cols, f'teaching_arc/{s["id"]}.uses', warns, notes)
	listed = {v['id'] for v in d['visuals']}
	for v in d['visuals']:
		if not catalog_visual(v['id']):
			if v['sketch']:
				notes.append(f'visual "{v["id"]}" is proposed (not in knowledge/visuals/ yet)')
			else:
				warns.append(f'visual "{v["id"]}" is not in knowledge/visuals/; give it a sketch')
	refs_to_visuals = [(f'ways_in/{w["id"]}', x) for w in ways for x in w['visuals']]
	refs_to_visuals += [(f'teaching_arc/{s["id"]}', s['visual']) for s in d['teaching_arc'] if s['visual']]
	refs_to_visuals += [(f'checks/{c["id"]}', c['visual']) for c in d['checks'] if c['visual']]
	for where, x in refs_to_visuals:
		if x['id'] not in listed:
			warns.append(f'{where}: visual "{x["id"]}" is not listed in visuals[]')
		cat = catalog_visual(x['id'])
		if cat and x['preset'] and x['preset'] not in {pr['id'] for pr in cat['presets']}:
			warns.append(f'{where}: preset "{x["preset"]}" is not declared by visual "{x["id"]}"')

	# Status, review, references.
	review = d.get('review') or {}
	if d['status'] in ('novice-reviewed', 'physics-reviewed', 'published') and 'novice' not in review:
		warns.append(f'status "{d["status"]}" requires review.novice')
	if d['status'] in ('physics-reviewed', 'published') and 'physics' not in review:
		warns.append(f'status "{d["status"]}" requires review.physics')
	if 'physics' in review and not review['physics']['verification']:
		warns.append('review.physics.verification must record what was checked and how')
	if d['status'] in ('physics-reviewed', 'published'):
		unverified = sorted({w for w, ref in references(d) if not ref['verified']})
		if unverified:
			warns.append(f'unverified references after physics review: {unverified}')

	# Novice contract, formats, budgets, sources.
	entry = entry_texts(d)
	for label, text, max_math in entry:
		warns += novice_warnings(label, text, max_math)
	defined = ' | '.join([g['term'].lower() for g in d['glossary']] + [f.lower() for g in d['glossary'] for f in g['forms']])
	blob = ' '.join(plain(t) for label, t, _ in entry if not label.startswith('glossary')).lower()
	undefined = [t for t in TECHNICAL if re.search(rf'\b{re.escape(t.lower())}(s|es)?\b', blob) and t.lower() not in defined]
	if undefined:
		warns.append(f'entry reading uses technical words the glossary does not define: {undefined}')
	warns += format_warnings()

	by_rung = {r: sum(wc(w['explanation']) for w in ways if w['rung'] == r) for r in RUNG}
	way_extras = wc([{k: w[k] for k in ('question', 'gist', 'recap', 'try_it', 'takeaway', 'retell', 'picture', 'simplifies')} for w in ways])
	parts = {
		'entry way explanations': (by_rung['entry'], 1000),
		'working way explanations': (by_rung['working'], 1100),
		'formal way explanations': (by_rung['formal'], 1000),
		'research way explanations': (by_rung['research'], 700),
		'other way fields (question, gist, recap, try_it, takeaway, retell, picture, simplifies)': (way_extras, 1300),
		'equations, derivations, examples, problems, observations': (wc([d[k] for k in ('key_equations', 'derivations', 'worked_examples', 'problems', 'observations')]), 2200),
		'objectives, misconceptions, checks, arc, tutor moves, analogies, glossary, traps': (wc([d[k] for k in ('objectives', 'misconceptions', 'checks', 'teaching_arc', 'tutor_moves', 'analogies', 'glossary', 'notation_traps')]), 3300),
		'links, visuals, history, horizon': (wc([d[k] for k in ('prerequisites', 'leads_to', 'related', 'visuals', 'history', 'research_horizon')]), 1000),
	}
	for name, (n, cap) in parts.items():
		if n > cap * 1.1:
			warns.append(f'{name}: {n} words, over the budget of {cap}; cut support fields and repetition, never the entry rung')
	total = wc(d)
	cap = 7000 if tier in ('prerequisite', 'foundation') else 10000
	if total > cap:
		warns.append(f'note has {total} words, over {cap} for a {tier} note')

	units = provenance_units(d['provenance'], warns)
	for a in d['provenance']['legacy_assets']:
		if a not in legacy:
			warns.append(f'provenance legacy asset "{a}" does not exist')
	if cid in reg:
		units |= {(s['book'], s['unit']) for s in reg[cid][1]['sources'] if s['book'] in BOOKS}
	warns += common_lints(d)
	warns += copy_warnings(d, units)
	notes.append(f'{total} words (entry {by_rung["entry"]}, working {by_rung["working"]}, formal {by_rung["formal"]}, research {by_rung["research"]}); '
		f'{len(ways)} ways, {len(d["checks"])} checks, {len(d["problems"])} problems, {len(listed)} visuals; status {d["status"]}')
	return warns, notes


# ---- Visuals ----------------------------------------------------------------------------------------------------


def visual_warnings(d, path):
	warns, notes = [], []
	reg, legacy = registry_entries(), legacy_ids()
	if Path(path).stem != d['id']:
		warns.append(f'file name should be {d["id"]}.json')
	params = {x['id']: x for x in d['params']}
	presets = {x['id']: x for x in d['presets']}
	readouts = {x['id'] for x in d['readouts']}
	for coll in ('variants', 'params', 'presets', 'readouts', 'tour', 'design_rules'):
		ids = [x['id'] for x in d[coll]]
		if len(set(ids)) != len(ids):
			warns.append(f'{coll}: duplicate ids')

	def value_ok(where, pid, value):
		p = params[pid]
		if p['type'] == 'enum' and value not in {o['value'] for o in (p['options'] or [])}:
			warns.append(f'{where}: "{value}" is not an option of param "{pid}"')
		elif p['type'] in ('number', 'integer', 'progress'):
			if not isinstance(value, (int, float)) or isinstance(value, bool):
				warns.append(f'{where}: param "{pid}" needs a number')
			elif (p['min'] is not None and value < p['min']) or (p['max'] is not None and value > p['max']):
				warns.append(f'{where}: {value} is outside the range of param "{pid}"')
		elif p['type'] == 'boolean' and not isinstance(value, bool):
			warns.append(f'{where}: param "{pid}" needs true or false')

	def state_ok(where, state, need_preset):
		if need_preset:
			if state.get('preset') not in presets:
				warns.append(f'{where}: state.preset must name a declared preset')
		for k, v in state.items():
			if k == 'preset':
				continue
			if k not in params:
				warns.append(f'{where}: "{k}" is not a declared param')
			else:
				value_ok(where, k, v)

	for p in d['params']:
		if p['type'] == 'enum' and not p['options']:
			warns.append(f'params/{p["id"]}: enum params need options')
		if p['type'] != 'path':
			value_ok(f'params/{p["id"]}.default', p['id'], p['default'])
	for pr in d['presets']:
		state_ok(f'presets/{pr["id"]}', pr['state'], False)
	for b in d['tour']:
		state_ok(f'tour/{b["id"]}', b['state'], True)
		if b['animate'] and b['animate']['param'] not in params:
			warns.append(f'tour/{b["id"]}: animate.param "{b["animate"]["param"]}" is not a declared param')
		if b['await'] == 'prediction' and not b['predict']:
			warns.append(f'tour/{b["id"]}: a prediction beat needs predict')
		if b['rung'] == 'entry':
			for k in ('say', 'describe', 'predict'):
				if b.get(k):
					warns += novice_warnings(f'tour/{b["id"]}.{k}', b[k], 0)
	for t in d['model']['tests']:
		state_ok(f'model.tests/{t["id"]}', t['state'], True)
		for e in t['expect']:
			if e['readout'] not in readouts:
				warns.append(f'model.tests/{t["id"]}: readout "{e["readout"]}" is not declared')
			if e['abs_tol'] is None and e['rel_tol'] is None:
				warns.append(f'model.tests/{t["id"]}: give abs_tol or rel_tol')
	if d['kind'] != 'static' and not d['model']['tests']:
		warns.append('interactive, animated, and plotted visuals need model tests')
	if d['kind'] != 'static' and not any(v['fallback'] for v in d['variants']):
		warns.append('declare a fallback variant for when the richer variant cannot run')
	if 'entry' in d['rungs']:
		warns += novice_warnings('picture.caption', d['picture']['caption'], 0)
	for r in d['design_rules']:
		m = r['misconception']
		if m:
			mm = ADDRESS.match(m)
			if not mm or not mm.group(1) or mm.group(2) != 'misconceptions':
				warns.append(f'design_rules/{r["id"]}: misconception must be <concept>/misconceptions/<id>')
			else:
				other = v2_note(mm.group(1))
				if mm.group(1) not in reg:
					warns.append(f'design_rules/{r["id"]}: unknown concept "{mm.group(1)}"')
				elif other and mm.group(3) not in {x['id'] for x in other['misconceptions']}:
					warns.append(f'design_rules/{r["id"]}: "{m}" does not resolve')
	for s in d['serves']:
		if s['concept'] not in reg:
			warns.append(f'serves: "{s["concept"]}" is not a registry concept id')
		else:
			other = v2_note(s['concept'])
			if other and d['id'] not in {v['id'] for v in other['visuals']}:
				notes.append(f'serves "{s["concept"]}", whose note does not list this visual')
	links = [('builds_on', v) for v in d['builds_on']] + [('leads_to', v) for v in d['leads_to']]
	if d['variant_of']:
		links.append(('variant_of', d['variant_of']))
	for key, v in links:
		if not catalog_visual(v):
			notes.append(f'{key} "{v}" is not in the catalog yet')
	for a in d['starting_material']['legacy_assets']:
		if a not in legacy:
			warns.append(f'starting_material legacy asset "{a}" does not exist')
	units = provenance_units(d['provenance'], warns)
	for img in d['provenance']['figure_images']:
		if not (SRC / img).exists():
			warns.append(f'provenance figure image "{img}" does not exist under book-sources/')
	if d['status'] in ('specified', 'prototype', 'built', 'published') and not d.get('review'):
		warns.append(f'status "{d["status"]}" requires a review')
	warns += format_warnings()
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
		FORMATTED.clear()
		try:
			data = json.loads(Path(f).read_text())
		except (OSError, json.JSONDecodeError) as e:
			print(f'ERROR {f}: cannot parse JSON: {e}')
			status = 1
			continue
		errs = []
		check(data, schema, schema, '$', errs)
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
