#!/usr/bin/env python3
"""Validate knowledge-vault JSON against its schema, plus content checks.

Usage:
  python3 knowledge/_tools/validate.py dossier <sources/<book>/chapters/<unit>.json> [...]
  python3 knowledge/_tools/validate.py concept <concepts/<domain>/<id>.json> [...]
  python3 knowledge/_tools/validate.py visual <visuals/<id>.json> [...]
  python3 knowledge/_tools/validate.py all          (every v2 concept note and visual, plus cross-checks)
  python3 knowledge/_tools/validate.py schema <schema.json> <file.json> [...]

Exit status: 0 clean, 1 schema errors, 2 warnings only. Lines starting "note:" are information and never change it.

Dossiers: coverage against the source manifest, and copied source wording.
Concept notes and visuals (knowledge/_meta/writing-guide.md): ids and addresses that resolve, tier and rung
requirements, the novice contract and wording traps on entry reading, text formats (x-format), graph consistency,
length budgets per tier, gradable numeric answers, lifecycle, component-contract consistency for visuals, mentions of
textbooks, and copied source wording.

Supports the JSON Schema subset used in knowledge/_schemas: type, enum, required, properties, additionalProperties,
items, minItems, maxItems, minLength, maxLength, pattern, minimum, maximum, anyOf, local $ref, and the custom
x-format and x-audience keywords.
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
		for sub in s['anyOf']:
			if not _errors(v, sub, root, path):
				check(v, sub, root, path, [])
				break
		else:
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
		if 'x-format' in s:
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
NOTE_SKIP = {'latex', 'symbol', 'provenance', 'review', 'id', 'assumes', 'schema_version', 'refs', 'uses', 'evidenced_by', 'targets', 'diagnosed_by', 'state', 'expect', 'continues', 'retired_ids', 'starting_material'}
COUNT_SKIP = NOTE_SKIP | {'authors', 'venue', 'doi', 'arxiv', 'kind', 'forms', 'say_as', 'pronunciations', 'title', 'name', 'label', 'unit', 'quantity', 'status', 'updated', 'domain', 'tier', 'rung', 'format', 'priority', 'needed_for', 'invites', 'to_rung', 'sign', 'concept', 'visual', 'visuals'}
COLLECTIONS = [
	'ways_in', 'objectives', 'key_equations', 'derivations', 'worked_examples', 'problems', 'observations', 'checks',
	'misconceptions', 'analogies', 'glossary', 'teaching_arc', 'notation_traps', 'history', 'research_horizon',
]
TUTOR_COLLECTIONS = ['opening_questions', 'if_stuck', 'common_questions']
ADDRESS = re.compile(r'^(?:([a-z0-9]+(?:-[a-z0-9]+)*)/)?([a-z_]+)/([a-z0-9]+(?:-[a-z0-9]+)*)$')
BOOKISH = [
	re.compile(r"\b(Schutz|Blundell|Lancaster|d['’]\s?Inverno|Vickers|Gifted Amateur|Misner|Wald|Carroll)\b", re.I),
	re.compile(r'\bMTW\b'),
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
POSITIONAL = re.compile(
	r"\b(return to (this|it)|come back to (this|it)|more on (this|that)) later\b"
	r"|\b(saw|showed|found|noted|mentioned|seen|derived|discussed|described) (earlier|above|below|previously)\b"
	r"|\bsee (above|below)\b"
	r"|\b(formula|equation|derivation|example|section|figure|table|result|argument|way|paragraph|step)s? (above|below)\b"
	r"|\b(above|below|earlier|previous) (formula|equation|derivation|example|section|figure|table|result|argument|way|paragraph|step)s?\b"
	r"|\baforementioned\b",
	re.I,
)
SPEECH_BAD = re.compile(r'[$\\^_`#]|[⁰¹²³⁴⁵⁶⁷⁸⁹⁻₀₁₂₃₄₅₆₇₈₉×]')
MD_PSEUDO_MATH = re.compile(r'[A-Za-zΑ-Ωα-ω][\^_][{A-Za-zΑ-Ωα-ω0-9]|[₀₁₂₃₄₅₆₇₈₉⁰¹⁴⁵⁶⁷⁸⁹⁻]|[α-ωΓΔΘΛΞΠΣΦΨΩ∂∇∮∫]')
# Technical words the entry rung must define in its glossary if it uses them (writing guide section 4, rule 4).
TECHNICAL = [
	'vector', 'tangent', 'coordinate', 'metric', 'tensor', 'geodesic', 'invariant', 'manifold', 'curvature', 'component',
	'derivative', 'spacetime', 'worldline', 'proper time', 'inertial', 'parallel transport', 'holonomy', 'scalar',
	'basis', 'covariant', 'contravariant', 'indices', 'integral', 'gradient', 'divergence', 'flux', 'topology',
	'singularity', 'redshift', 'stress-energy', 'energy-momentum', 'gauge', 'intrinsic', 'extrinsic', 'tidal',
	'Christoffel', 'Riemann', 'Ricci', 'Lorentz', 'Gaussian', 'eigenvalue', 'four-vector', 'reference frame', 'radian',
	'geodetic', 'precession', 'quadrupole', 'entropy', 'horizon', 'gyroscope', 'orbit', 'observer', 'light-year',
	'time dilation', 'simultaneity', 'free fall', 'equivalence principle', 'mass-energy', 'wavelength', 'frequency',
]
# Wording traps on entry reading (writing guide section 4). Each is (pattern, condition on the sentence, message).
WORDING_TRAPS = [
	(re.compile(r'\bstill points\b', re.I), None, '"still points" can hide a change; compare against a named reference'),
	(re.compile(r'\b(north|south|east|west)(ward|wards)?\b'), re.compile(r'\bpoles?\b', re.I), 'compass direction near a pole; use directions relative to the path'),
	(re.compile(r'\binside the loop\b', re.I), None, '"inside the loop" is ambiguous on a closed surface; name the region'),
	(re.compile(r'\bfrom (the )?inside\b', re.I), None, '"from the inside" is ambiguous; say "without leaving the surface" or name the place'),
	(re.compile(r'\b(counter-?)?clockwise\b', re.I), re.compile(r'^(?!.*\b(seen|viewed|looking) (from|down)\b)', re.I | re.S), '"clockwise" needs a viewpoint ("seen from above the North Pole")'),
	(re.compile(r"\b(never|not|didn'?t|doesn'?t|won'?t)\s+(\w+\s+)?turn(s|ed|ing)?\b", re.I), re.compile(r'\barrow\b', re.I), 'the arrow should "swing", not "turn": the walker turns at corners, the arrow never swings, and the arrow comes back turned'),
	(re.compile(r'\btime (runs|passes|goes|ticks) (slow|fast)(er|ly)?\b|\btime slows\b', re.I), re.compile(r'^(?!.*\b(compared|than|relative|according|clock)\b)', re.I | re.S), 'a time comparison needs its measurer: compared with whose clock?'),
	(re.compile(r'\bat the same time\b', re.I), re.compile(r'^(?!.*\b(according|clocks?|measured|frame)\b)', re.I | re.S), '"at the same time" needs its measurer: by whose clocks?'),
]
UNITS = {
	'1', 'percent', 'rad', 'deg', 'turn', 'arcsec', 'mas', 'arcsec/yr', 'mas/yr', 'deg/h', 'deg/day', 'm', 'cm', 'mm', 'km',
	'au', 'ly', 'pc', 'kpc', 'Mpc', 'Gpc', 'm^2', 'km^2', 'm^3', 's', 'ms', 'min', 'h', 'day', 'yr', 'Gyr', 'kg', 'g',
	'M_sun', 'M_earth', 'J', 'eV', 'keV', 'MeV', 'GeV', 'W', 'K', 'Hz', 'kHz', 'm/s', 'km/s', 'm/s^2', 'N', 'T', 'V', 'C',
	'A', 'kg/m^3', 'J/m^3', 'Pa', 'm^-2', 's^-1', 'km/s/Mpc',
}
ANGLE_UNITS = {'rad', 'deg', 'turn', 'arcsec', 'mas'}
STOP = set('the a an and or of to in on at by for with is are was be it its this that these those as from your you we our so but not no if then than into out one two each every any all can will does do did has have had there their them they he she his her who which what when where how why also only even just more most much very same other'.split())

# Required rungs (ways, objectives, checks) and word budgets per tier (writing guide sections 3 and 9).
TIER_RUNGS = {
	'prerequisite': ('entry', 'working'),
	'foundation': ('entry', 'working', 'formal'),
	'core': ('entry', 'working', 'formal'),
	'advanced': ('entry', 'working', 'formal', 'research'),
	'frontier': ('entry', 'formal', 'research'),
}
TIER_BUDGETS = {
	'prerequisite': dict(entry=(400, 1000), working=(300, 900), formal=(0, 300), research=(0, 0), extras=450, support=900, tutoring=1200, links=200, total=5000),
	'foundation': dict(entry=(400, 1000), working=(300, 900), formal=(300, 600), research=(0, 0), extras=650, support=1500, tutoring=2200, links=300, total=7000),
	'core': dict(entry=(400, 1000), working=(300, 1000), formal=(400, 900), research=(0, 400), extras=800, support=2300, tutoring=3300, links=900, total=9500),
	'advanced': dict(entry=(150, 400), working=(300, 1000), formal=(400, 1100), research=(250, 900), extras=800, support=2500, tutoring=3500, links=1000, total=10500),
	'frontier': dict(entry=(150, 300), working=(0, 1000), formal=(400, 1100), research=(250, 900), extras=800, support=2500, tutoring=3500, links=1000, total=10500),
}
MIN_PROBLEMS = {'prerequisite': 1, 'foundation': 2, 'core': 3, 'advanced': 3, 'frontier': 3}
# Tiers that require a formal rung need this many formal checks and at least one formal problem.
MIN_FORMAL_CHECKS = 2
# Caps are ceilings. A draft stays within this share of every cap, so reviewers can add explicit steps without squeezing.
DRAFT_HEADROOM = 0.8


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


def wc(obj):
	return sum(len(words(plain(s))) for _, s in strings(obj, COUNT_SKIP))


def content_words(s):
	return {w for w in words(plain(s)) if w not in STOP and len(w) > 2}


def sentences(s):
	return [p for p in re.split(r'(?<=[.!?])\s+|\n+', plain(s).strip()) if p.strip()]


def sentence_lengths(s):
	return [n for n in (len(re.findall(r"[A-Za-z0-9][A-Za-z0-9'’-]*", p)) for p in sentences(s)) if n]


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
	for sentence in sentences(text):
		for rx, condition, message in WORDING_TRAPS:
			m = rx.search(sentence)
			if m and (condition is None or condition.search(sentence)):
				warns.append(f'{label}: wording trap "{m.group(0)}": {message}')
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
		elif fmt == 'latex' and '$' in s:
			warns.append(f'{path}: latex fields take bare LaTeX without $ delimiters')
		if fmt in ('md', 'plain') and '.steps[' not in path and '.solution[' not in path:
			m = POSITIONAL.search(plain(s))
			if m:
				warns.append(f'{path}: "{m.group(0)}" points by position; name the thing or use refs')
	return warns


def common_lints(d):
	warns = []
	for path, s in strings(d, NOTE_SKIP):
		# Research papers by authors who also wrote textbooks may be cited; names are linted in prose only.
		if re.search(r'\.(authors|more_authors)\[', path):
			continue
		for rx in BOOKISH:
			m = rx.search(s)
			if m:
				warns.append(f'{path}: mentions a textbook or locator ("{m.group(0)}"); write in our own voice, sources go in provenance only')
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


def numeric_warnings(where, items):
	warns = []
	for n in items or []:
		label = f'{where} numeric "{n["quantity"]}"'
		if n['unit'] not in UNITS:
			warns.append(f'{label}: unit "{n["unit"]}" is not in the unit table ({", ".join(sorted(UNITS)[:12])}, ...)')
		if n['abs_tol'] is None and n['rel_tol'] is None:
			warns.append(f'{label}: give abs_tol or rel_tol')
		if n['value'] == 0 and n['abs_tol'] is None:
			warns.append(f'{label}: a zero answer needs abs_tol')
		if n['unit'] in ANGLE_UNITS and n['sign'] == 'signed' and n['modulo'] is None:
			warns.append(f'{label}: a signed angle needs modulo')
	return warns


# ---- Concept notes ------------------------------------------------------------------------------------------------


def entry_texts(d):
	t = [('summary', d['summary'], 1), ('tagline', d['tagline'], 0)]
	for w in d['ways_in']:
		if w['rung'] == 'entry':
			for k in ('gist', 'recap', 'explanation', 'try_it', 'takeaway', 'picture', 'simplifies'):
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
			t += [(f'misconceptions/{m["id"]}.{k}', m[k], 0) for k in ('belief', 'why_tempting', 'correction')]
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
			t += [(f'common_questions/{q["id"]}.question', q['question'], 0), (f'common_questions/{q["id"]}.answer', q['answer'], 0)]
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


def part_counts(d):
	ways = d['ways_in']
	by_rung = {r: sum(wc(w['explanation']) for w in ways if w['rung'] == r) for r in RUNG}
	return dict(
		entry=by_rung['entry'],
		working=by_rung['working'],
		formal=by_rung['formal'],
		research=by_rung['research'],
		extras=wc([{k: w[k] for k in ('question', 'gist', 'recap', 'try_it', 'takeaway', 'picture', 'simplifies')} for w in ways]),
		support=wc([d[k] for k in ('key_equations', 'derivations', 'worked_examples', 'problems', 'observations')]),
		tutoring=wc([d[k] for k in ('objectives', 'misconceptions', 'checks', 'teaching_arc', 'tutor_moves', 'analogies', 'glossary', 'notation_traps')]),
		links=wc([d[k] for k in ('prerequisites', 'leads_to', 'related', 'visuals', 'history', 'research_horizon')]),
		total=wc(d),
	)


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
	for r in d['retired_ids']:
		if r['id'] in cols.get(r['collection'], {}):
			warns.append(f'retired id "{r["collection"]}/{r["id"]}" is in use again; ids are never reused')

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
	for g in d['glossary']:
		if g['concept']:
			known(f'glossary/{g["id"]}.concept', g['concept'])
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
	required = TIER_RUNGS[tier]
	rungs = {w['rung'] for w in ways}
	for r in required:
		if r not in rungs:
			warns.append(f'{tier} notes need at least one "{r}" way')
	kinds = [w['kind'] for w in ways]
	if len(set(kinds)) < 2:
		warns.append('ways_in must use at least two different kinds')
	for k in set(kinds):
		if kinds.count(k) > len(ways) / 2:
			warns.append(f'kind "{k}" is used by more than half of the ways')
	if tier in ('foundation', 'core') and d['observations'] and 'operational' not in kinds:
		warns.append('foundation and core notes with observations need an operational way')
	if len({w['question'] for w in ways}) < len(ways):
		warns.append('each way must answer a different question')
	for i, w in enumerate(ways):
		where = f'ways_in/{w["id"]}'
		if i > 0 and not w['continues']:
			warns.append(f'{where}: every way after the first names the earlier ways it climbs from in continues')
		for c in w['continues']:
			if c not in order or order[c] >= i:
				warns.append(f'{where}: continues "{c}" must be an earlier way in this note')
		if w['continues'] and w['rung'] != 'entry':
			first = set(list(content_words(' '.join(words(plain(w['explanation']))[:40]))))
			link = set().union(*(content_words(ways[order[c]]['title'] + ' ' + ways[order[c]]['takeaway']) for c in w['continues'] if c in order))
			if link and not first & link:
				warns.append(f'{where}: the first sentences should refer back to the way it continues by its picture or result')
		if w['gist']:
			a, b = content_words(w['gist']), content_words(w['takeaway'])
			if a and len(a & b) / len(a) > 0.6:
				warns.append(f'{where}: gist repeats the takeaway; set gist to null unless the spoken opener must differ')
		if w['picture'] and w['visuals']:
			warns.append(f'{where}: picture should be null when the way cites a visual')
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

	# Objectives, checks, problems, misconceptions.
	for coll in ('objectives', 'checks'):
		have = {x['rung'] for x in d[coll]}
		for r in required:
			if r not in have:
				warns.append(f'{tier} notes need at least one "{r}" item in {coll}')
	evidenced = set()
	for o in d['objectives']:
		own = False
		for a in o['evidenced_by']:
			r = resolve(a, d, cols, f'objectives/{o["id"]}.evidenced_by', warns, notes)
			if r:
				evidenced.add((r[0], r[1]['id']))
				own |= r[1]['rung'] == o['rung']
		if not own:
			warns.append(f'objectives/{o["id"]}: needs a check or problem at its own rung ({o["rung"]})')
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
		if len(sentences(m['correction'])) > 2:
			warns.append(f'misconceptions/{m["id"]}: correction has more than two sentences; cite the check instead of re-walking the argument')
	for c in chk.values():
		for t in c['targets']:
			if t not in mis:
				warns.append(f'checks/{c["id"]}: target "{t}" is not a misconception id')
			elif c['id'] not in mis[t]['diagnosed_by']:
				warns.append(f'checks/{c["id"]}: misconception "{t}" must list this check in diagnosed_by')
		if '$' in c['question'] and not c['question_spoken']:
			warns.append(f'checks/{c["id"]}: the question contains math, so give question_spoken')
		if c['format'] == 'numeric' and not c['numeric']:
			warns.append(f'checks/{c["id"]}: numeric checks need numeric answers')
		warns += numeric_warnings(f'checks/{c["id"]}', c['numeric'])
	for x in cols['problems'].values():
		for t in x['targets']:
			if t not in mis:
				warns.append(f'problems/{x["id"]}: target "{t}" is not a misconception id')
		if '$' in x['statement'] and not x['statement_spoken']:
			warns.append(f'problems/{x["id"]}: the statement contains math, so give statement_spoken')
		warns += numeric_warnings(f'problems/{x["id"]}', x['numeric'])
	tm = d['tutor_moves']
	for s in tm['if_stuck']:
		if s['misconception'] and s['misconception'] not in mis:
			warns.append(f'if_stuck/{s["id"]}: misconception "{s["misconception"]}" is not a misconception id')
	for coll, items in (('if_stuck', tm['if_stuck']), ('common_questions', tm['common_questions']), ('level_switching', tm['level_switching'])):
		for i, s in enumerate(items):
			for u in s['uses']:
				resolve(u, d, cols, f'{coll}/{s.get("id", i)}.uses', warns, notes)
	for q in tm['common_questions']:
		if q['rung'] == 'entry' and '$' in q['answer']:
			warns.append(f'common_questions/{q["id"]}: entry answers are spoken; no math')
	if len(d['problems']) < MIN_PROBLEMS[tier]:
		warns.append(f'{tier} notes need at least {MIN_PROBLEMS[tier]} problems')
	if 'formal' in required:
		formal_checks = sum(1 for c in d['checks'] if c['rung'] == 'formal')
		if formal_checks < MIN_FORMAL_CHECKS:
			warns.append(f'{tier} notes need at least {MIN_FORMAL_CHECKS} formal checks (have {formal_checks}); the formal rung carries graduate readers')
		if not any(x['rung'] == 'formal' for x in d['problems']):
			warns.append(f'{tier} notes need at least one formal problem')
	if len(d['problems']) > 1 and len({x['rung'] for x in d['problems']}) < 2:
		warns.append('problems must span at least two rungs')
	if tier in ('foundation', 'core') and not d['worked_examples']:
		warns.append('foundation and core notes need at least one worked example')
	if tier in ('core', 'advanced', 'frontier') and not 2 <= len(d['research_horizon']) <= 5:
		warns.append(f'{tier} notes need 2 to 5 research_horizon topics')
	if tier in ('advanced', 'frontier') and not any(ref['kind'] == 'review' for r in d['research_horizon'] for ref in r['references']):
		warns.append(f'{tier} notes need at least one review among the research references')

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
		if cat:
			if x['preset'] and x['preset'] not in {pr['id'] for pr in cat['presets']}:
				warns.append(f'{where}: preset "{x["preset"]}" is not declared by visual "{x["id"]}"')
			if x['tour'] and x['tour'] not in {t['id'] for t in cat['tours']}:
				warns.append(f'{where}: tour "{x["tour"]}" is not declared by visual "{x["id"]}"')
			if cid not in {s['concept'] for s in cat['serves']}:
				warns.append(f'{where}: visual "{x["id"]}" does not list this concept in serves')

	# Status, review, references.
	review = d.get('review') or {}
	status = d['status']
	if status in ('novice-reviewed', 'physics-reviewed', 'published') and 'novice' not in review:
		warns.append(f'status "{status}" requires review.novice')
	if status in ('physics-reviewed', 'published'):
		if 'physics' not in review:
			warns.append(f'status "{status}" requires review.physics')
		elif review['physics']['verdict'] == 'needs-attention':
			warns.append(f'status "{status}" is not allowed with a physics verdict of needs-attention')
	for stage, r in review.items():
		if r['reviewed_revision'] != d['revision'] and status != 'draft':
			warns.append(f'review.{stage} covers revision {r["reviewed_revision"]}, but the note is at revision {d["revision"]}; review again')
	if 'physics' in review and not review['physics']['verification']:
		warns.append('review.physics.verification must record what was checked and how')
	for where, ref in references(d):
		if any('et al' in a.lower() for a in ref['authors']):
			warns.append(f'{where}: list real author names and set more_authors instead of "et al."')
	if status in ('physics-reviewed', 'published'):
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

	counts, budget = part_counts(d), TIER_BUDGETS[tier]

	def headroom(n, cap, label):
		room = int(cap * DRAFT_HEADROOM)
		if status == 'draft' and n > room:
			warns.append(f'{label}: {n} words; a draft stays within {room}, 80% of the {tier} cap of {cap}, so reviewers can add explicit steps without squeezing')

	for part in ('entry', 'working', 'formal', 'research'):
		lo, hi = budget[part]
		n = counts[part]
		if n > hi:
			warns.append(f'{part} way explanations: {n} words, over the {tier} cap of {hi}')
		elif part in required and n < lo:
			warns.append(f'{part} way explanations: {n} words, under the {tier} minimum of {lo}')
		else:
			headroom(n, hi, f'{part} way explanations')
	for part in ('extras', 'support', 'tutoring', 'links', 'total'):
		if counts[part] > budget[part]:
			warns.append(f'{part}: {counts[part]} words, over the {tier} cap of {budget[part]}; drop or shorten the lowest-value item, never compress the entry rung or a check answer')
		else:
			headroom(counts[part], budget[part], part)

	units = provenance_units(d['provenance'], warns)
	for a in d['provenance']['legacy_assets']:
		if a not in legacy:
			warns.append(f'provenance legacy asset "{a}" does not exist')
	if cid in reg:
		units |= {(s['book'], s['unit']) for s in reg[cid][1]['sources'] if s['book'] in BOOKS}
	warns += common_lints(d)
	warns += copy_warnings(d, units)
	notes.append(
		f'{counts["total"]} words (entry {counts["entry"]}, working {counts["working"]}, formal {counts["formal"]}, research {counts["research"]}, '
		f'extras {counts["extras"]}, support {counts["support"]}, tutoring {counts["tutoring"]}, links {counts["links"]}); '
		f'{len(ways)} ways, {len(d["checks"])} checks, {len(d["problems"])} problems, {len(listed)} visuals; status {status}'
	)
	return warns, notes


# ---- Visuals ----------------------------------------------------------------------------------------------------


def visual_warnings(d, path):
	warns, notes = [], []
	reg, legacy = registry_entries(), legacy_ids()
	if Path(path).stem != d['id']:
		warns.append(f'file name should be {d["id"]}.json')
	params = {x['id']: x for x in d['params']}
	presets = {x['id']: x for x in d['presets']}
	readouts = {x['id']: x for x in d['readouts']}
	progress_params = [p['id'] for p in d['params'] if p['type'] == 'progress']
	beats = [(t, b) for t in d['tours'] for b in t['beats']]
	for coll, ids in (
		('variants', [x['id'] for x in d['variants']]),
		('params', list(params) if len(params) == len(d['params']) else [x['id'] for x in d['params']]),
		('presets', [x['id'] for x in d['presets']]),
		('readouts', [x['id'] for x in d['readouts']]),
		('tours', [t['id'] for t in d['tours']]),
		('design_rules', [x['id'] for x in d['design_rules']]),
		('model.tests', [x['id'] for x in d['model']['tests']]),
		('accessibility.keyboard', [k['key'] for k in d['accessibility']['keyboard']]),
	):
		dups = sorted({i for i in ids if ids.count(i) > 1})
		if dups:
			warns.append(f'{coll}: duplicate ids or keys {dups}')
	for t in d['tours']:
		ids = [b['id'] for b in t['beats']]
		if len(set(ids)) != len(ids):
			warns.append(f'tours/{t["id"]}: duplicate beat ids')

	def value_ok(where, pid, value):
		p = params[pid]
		if p['type'] == 'enum':
			if value not in {o['value'] for o in (p['options'] or [])}:
				warns.append(f'{where}: "{value}" is not an option of param "{pid}"')
		elif p['type'] in ('number', 'integer', 'progress'):
			if not isinstance(value, (int, float)) or isinstance(value, bool):
				warns.append(f'{where}: param "{pid}" needs a number, got {value!r}')
				return
			if p['type'] == 'integer' and not float(value).is_integer():
				warns.append(f'{where}: param "{pid}" needs a whole number, got {value}')
			if (p['min'] is not None and value < p['min']) or (p['max'] is not None and value > p['max']):
				warns.append(f'{where}: {value} is outside the range of param "{pid}"')
			if p['step'] and p['min'] is not None and p['type'] != 'progress':
				k = (value - p['min']) / p['step']
				if abs(k - round(k)) > 1e-9:
					warns.append(f'{where}: {value} is not on the step grid of param "{pid}"')
		elif p['type'] == 'boolean' and not isinstance(value, bool):
			warns.append(f'{where}: param "{pid}" needs true or false')

	def full_state(state):
		s = {p['id']: p['default'] for p in d['params']}
		explicit = set()
		if state.get('preset') in presets:
			s.update(presets[state['preset']]['state'])
			explicit |= set(presets[state['preset']]['state'])
		s.update({k: v for k, v in state.items() if k != 'preset'})
		explicit |= {k for k in state if k != 'preset'}
		return s, explicit

	def available(s, constraint):
		return not constraint or all(s.get(k) in vals for k, vals in constraint.items())

	def state_ok(where, state, need_preset):
		if need_preset and state.get('preset') not in presets:
			warns.append(f'{where}: state.preset must name a declared preset')
		if not need_preset and 'preset' in state:
			warns.append(f'{where}: a preset state must not contain a preset key')
		for k, v in state.items():
			if k == 'preset':
				continue
			if k not in params:
				warns.append(f'{where}: "{k}" is not a declared param')
			else:
				value_ok(where, k, v)
		s, explicit = full_state(state if need_preset else {**state})
		if not need_preset:
			s = {p['id']: p['default'] for p in d['params']} | state
			explicit = set(state)
		for pid in explicit:
			if pid not in params:
				continue
			p = params[pid]
			if not available(s, p['available_when']):
				warns.append(f'{where}: param "{pid}" is not available in this combination')
			if p['type'] == 'enum':
				opt = next((o for o in p['options'] or [] if o['value'] == s.get(pid)), None)
				if opt and not available(s, opt['available_when']):
					warns.append(f'{where}: option "{opt["value"]}" of "{pid}" is not available in this combination')
		return s

	for p in d['params']:
		if p['type'] == 'enum' and not p['options']:
			warns.append(f'params/{p["id"]}: enum params need options')
		if p['type'] != 'path':
			value_ok(f'params/{p["id"]}.default', p['id'], p['default'])
		for c in [p['available_when']] + [o['available_when'] for o in p['options'] or []]:
			for k, vals in (c or {}).items():
				if k not in params:
					warns.append(f'params/{p["id"]}: available_when names unknown param "{k}"')
				elif not isinstance(vals, list):
					warns.append(f'params/{p["id"]}: available_when values must be a list')
	for pr in d['presets']:
		state_ok(f'presets/{pr["id"]}', pr['state'], False)
	for r in d['readouts']:
		if '{value}' not in r['say'] and '{abs}' not in r['say']:
			warns.append(f'readouts/{r["id"]}: say needs a {{value}} or {{abs}} placeholder')
		if r['range'] and r['range'][0] < 0 and not r['say_negative']:
			warns.append(f'readouts/{r["id"]}: a signed readout needs say_negative')
		if r['range'] and r['range'][0] < 0 and not r['sense']:
			warns.append(f'readouts/{r["id"]}: a signed readout needs sense')
		if r['unit'] in ANGLE_UNITS and not r['range']:
			warns.append(f'readouts/{r["id"]}: an angle readout needs a range (branch)')
	concept_refs = []
	for t, b in beats:
		where = f'tours/{t["id"]}/beats/{b["id"]}'
		s = state_ok(where, b['state'], True)
		if b['animate']:
			if b['animate']['param'] not in params:
				warns.append(f'{where}: animate.param "{b["animate"]["param"]}" is not a declared param')
			else:
				value_ok(f'{where}.animate.to', b['animate']['param'], b['animate']['to'])
		if b['await'] == 'prediction' and not b['predict']:
			warns.append(f'{where}: a prediction beat needs predict')
		if b['check']:
			concept_refs.append((where, b['check']))
		if b['rung'] == 'entry':
			for k in ('say', 'describe', 'predict'):
				if b.get(k):
					warns += novice_warnings(f'{where}.{k}', b[k], 0)
	for t in d['tours']:
		if t['for_concept'] and t['for_concept'] not in {x['concept'] for x in d['serves']}:
			warns.append(f'tours/{t["id"]}: for_concept "{t["for_concept"]}" is not in serves')
	for t in d['model']['tests']:
		where = f'model.tests/{t["id"]}'
		s = state_ok(where, t['state'], True)
		for e in t['expect']:
			r = readouts.get(e['readout'])
			if not r:
				warns.append(f'{where}: readout "{e["readout"]}" is not declared')
				continue
			if e['abs_tol'] is None and e['rel_tol'] is None:
				warns.append(f'{where}: give abs_tol or rel_tol')
			if e['value'] == 0 and e['abs_tol'] is None:
				warns.append(f'{where}: a zero expectation needs abs_tol')
			if r['range'] and not (r['range'][0] < e['value'] <= r['range'][1]):
				warns.append(f'{where}: expected {e["value"]} is outside the readout range {r["range"]}')
			if r['visible_when'] == 'on-complete' and progress_params and any(s.get(pp, 0) < 1 for pp in progress_params):
				warns.append(f'{where}: readout "{r["id"]}" appears only on completion; set progress to 1')
		for h in t['expect_hidden']:
			if h not in readouts:
				warns.append(f'{where}: expect_hidden readout "{h}" is not declared')
		if not t['expect'] and not t['expect_hidden']:
			warns.append(f'{where}: a test needs expect or expect_hidden')
	if d['kind'] != 'static' and not d['model']['tests']:
		warns.append('interactive, animated, and plotted visuals need model tests')
	if d['kind'] != 'static' and not any(v['fallback'] for v in d['variants']):
		warns.append('declare a fallback variant for when the richer variant cannot run')
	if d['status'] in ('built', 'published') and not d['component']:
		warns.append(f'status "{d["status"]}" requires component')
	if 'entry' in d['rungs']:
		warns += novice_warnings('picture.caption', d['picture']['caption'], 0)
	for r in d['design_rules']:
		if r['misconception']:
			concept_refs.append((f'design_rules/{r["id"]}', r['misconception']))
	for where, addr in concept_refs:
		m = ADDRESS.match(addr)
		cid, coll, item = m.groups() if m else (None, None, None)
		if not cid or cid not in reg:
			warns.append(f'{where}: "{addr}" names an unknown concept')
			continue
		other = v2_note(cid)
		if other and item not in item_maps(other).get(coll, {}):
			warns.append(f'{where}: "{addr}" does not resolve')
	for s in d['serves']:
		if s['concept'] not in reg:
			warns.append(f'serves: "{s["concept"]}" is not a registry concept id')
		else:
			other = v2_note(s['concept'])
			if other and d['id'] not in {v['id'] for v in other['visuals']}:
				warns.append(f'serves "{s["concept"]}", whose note does not list this visual')
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
	if d['status'] in ('specified', 'prototype', 'built', 'published'):
		if not d.get('review'):
			warns.append(f'status "{d["status"]}" requires a review')
		elif d['review']['reviewed_revision'] != d['revision']:
			warns.append(f'review covers revision {d["review"]["reviewed_revision"]}, but the visual is at revision {d["revision"]}')
	warns += format_warnings()
	warns += common_lints(d)
	warns += copy_warnings(d, units)
	return warns, notes


MODES = {
	'dossier': ('chapter-dossier.schema.json', dossier_warnings),
	'concept': ('concept-note.schema.json', concept_warnings),
	'visual': ('visual.schema.json', visual_warnings),
}


def run(mode, files, schema_path=None):
	name, extra = MODES.get(mode, (None, None))
	schema = json.loads(Path(schema_path or KB / '_schemas' / name).read_text())
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


def main(argv):
	if len(argv) >= 2 and argv[1] == 'all':
		notes = [str(f) for f in sorted((KB / 'concepts').glob('*/*.json')) if not f.name.startswith('_') and (load_json(str(f)) or {}).get('schema_version') == 2]
		visuals = [str(f) for f in sorted((KB / 'visuals').glob('*.json'))]
		return max(run('concept', notes), run('visual', visuals))
	if len(argv) < 3 or argv[1] not in (*MODES, 'schema'):
		print(__doc__)
		return 1
	if argv[1] == 'schema':
		return run(None, argv[3:], argv[2])
	return run(argv[1], argv[2:])


if __name__ == '__main__':
	sys.exit(main(sys.argv))
