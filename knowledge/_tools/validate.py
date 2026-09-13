#!/usr/bin/env python3
"""Validate knowledge-vault JSON against its schema, plus coverage and copying checks for chapter dossiers.

Usage:
  python3 knowledge/_tools/validate.py dossier <dossier.json> [...]
  python3 knowledge/_tools/validate.py concept <concepts/<domain>/<id>.json> [...]
  python3 knowledge/_tools/validate.py schema <schema.json> <file.json> [...]

Exit status: 0 clean, 1 schema errors, 2 warnings only (coverage gaps or copied source wording).
Supports the JSON Schema subset used in knowledge/_schemas: type, enum, required, properties,
additionalProperties, items, minItems, minLength, minimum, maximum, anyOf, and local $ref.
"""
import json
import re
import sys
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
	if isinstance(v, str) and len(v) < s.get('minLength', 0):
		errs.append(f'{path}: shorter than {s["minLength"]} characters')
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


def dossier_warnings(d):
	warns = []
	manifest = json.loads((SRC / '_chapters' / d['book'] / 'manifest.json').read_text())
	unit = next((u for u in manifest['units'] if u['id'] == d['unit_id']), None)
	if not unit:
		return [f'unit "{d["unit_id"]}" is not in the {d["book"]} manifest']
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
	return warns


REF = re.compile(r'^(?:(SCH|GA|DIV) (ch\d{2}|app[A-E]|front)\b.*|legacy:([a-z0-9-]+).*)$')
BOOK_OF = {'SCH': 'schutz', 'GA': 'gifted-amateur', 'DIV': 'dinverno'}


def registry_ids():
	ids = {}
	for f in (KB / 'concepts').glob('*/_registry.json'):
		for c in json.loads(f.read_text())['concepts']:
			ids[c['id']] = f.parent.name
	return ids


def legacy_ids():
	return {a['id'] for f in (KB / 'sources' / 'legacy').glob('*.json') for a in json.loads(f.read_text()).get('assets', [])}


def refs(obj):
	if isinstance(obj, dict):
		for k, v in obj.items():
			if k in ('refs', 'inspired_by') and isinstance(v, list):
				yield from (x for x in v if isinstance(x, str))
			else:
				yield from refs(v)
	elif isinstance(obj, list):
		for v in obj:
			yield from refs(v)


def concept_warnings(d, path):
	warns = []
	ids, legacy = registry_ids(), legacy_ids()
	if Path(path).stem != d['id']:
		warns.append(f'file name should be {d["id"]}.json')
	if d['id'] not in ids:
		warns.append(f'id "{d["id"]}" is not in any _registry.json')
	elif ids[d['id']] != d['domain'] or Path(path).parent.name != d['domain']:
		warns.append(f'domain should be "{ids[d["id"]]}" and the file should live in concepts/{ids[d["id"]]}/')
	for key in ('prerequisites', 'leads_to', 'related'):
		for link in d.get(key, []):
			if link['id'] not in ids:
				warns.append(f'{key} id "{link["id"]}" is not in the registry')
	for lvl in d['levels'].values():
		for a in lvl.get('assumes', []):
			if a not in ids:
				warns.append(f'levels.assumes id "{a}" is not in the registry')
	cited_units = set()
	for r in refs(d):
		m = REF.match(r)
		if not m:
			warns.append(f'reference "{r}" does not look like "SCH ch05 §5.3 p.125" or "legacy:<asset-id>"')
		elif m.group(3) and m.group(3) not in legacy:
			warns.append(f'legacy asset "{m.group(3)}" does not exist')
		elif m.group(1):
			cited_units.add((BOOK_OF[m.group(1)], m.group(2)))
	for s in d['sources']:
		if s['source'] != 'legacy':
			cited_units.add((s['source'], s['unit']))
	source_words = []
	for book, unit in sorted(cited_units):
		f = SRC / '_chapters' / book / f'{unit}.md'
		if f.exists():
			source_words.append(words(f.read_text(errors='replace')))
	shingles = {' '.join(ws[i : i + SHINGLE]) for ws in source_words for i in range(len(ws) - SHINGLE + 1)}
	copied = []
	for key, text in prose(d):
		ws = words(text)
		for i in range(len(ws) - SHINGLE + 1):
			if ' '.join(ws[i : i + SHINGLE]) in shingles:
				copied.append(f'{key}: "{" ".join(ws[i:i + SHINGLE])} ..."')
				break
	if copied:
		warns.append(f'{len(copied)} prose fields repeat {SHINGLE}+ consecutive words from cited source units; paraphrase: ' + '; '.join(copied[:12]))
	return warns


def main(argv):
	if len(argv) < 3 or argv[1] not in ('dossier', 'schema', 'concept'):
		print(__doc__)
		return 1
	if argv[1] == 'dossier':
		schema_path, files = KB / '_schemas' / 'chapter-dossier.schema.json', argv[2:]
	elif argv[1] == 'concept':
		schema_path, files = KB / '_schemas' / 'concept-note.schema.json', argv[2:]
	else:
		schema_path, files = Path(argv[2]), argv[3:]
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
		warns = []
		if not errs and argv[1] == 'dossier':
			warns = dossier_warnings(data)
		elif not errs and argv[1] == 'concept':
			warns = concept_warnings(data, f)
		label = 'OK' if not errs and not warns else ('ERRORS' if errs else 'WARNINGS')
		print(f'{label} {f}')
		for e in errs[:60]:
			print('  error:', e)
		if len(errs) > 60:
			print(f'  ... {len(errs) - 60} more errors')
		for w in warns:
			print('  warning:', w)
		status = max(status, 1 if errs else (2 if warns else 0)) if status != 1 else 1
	return status


if __name__ == '__main__':
	sys.exit(main(sys.argv))
