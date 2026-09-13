# grbook.ai knowledge vault

The teaching knowledge behind grbook.ai: a network of general relativity concepts, each explained on a depth
ladder from a first encounter to research, and a network of visuals that explain them. We learned how to teach
from three well-regarded textbooks and the author's earlier course; that study is internal scaffolding under
`sources/`, and the concept notes and visuals never mention it. How to write: `_meta/writing-guide.md`.
It serves three readers:

1. **Authors** writing the new course, its lessons, and its interactive demonstrations.
2. **The AI tutor**, which retrieves concepts, prerequisites, analogies, misconceptions, and demos while it teaches.
3. **The learner model**, which records progress against the concept and lesson identifiers defined here.

## Sources

| Id | Book | Short |
| --- | --- | --- |
| `schutz` | Bernard Schutz, *A First Course in General Relativity*, 3rd ed. (Cambridge, 2022) | SCH |
| `gifted-amateur` | Stephen J. Blundell and Tom Lancaster, *General Relativity for the Gifted Amateur* (Oxford) | GA |
| `dinverno` | Ray d'Inverno and James Vickers, *Introducing Einstein's Relativity*, 2nd ed. (Oxford, 2022) | DIV |

The page-level exports live in `book-sources/` (gitignored, local only, never deployed).

## Source policy: learn how to teach, never copy

The books are our teachers, not our text.

- **Ideas may be reused:** the order of topics, a good analogy, the shape of an argument, the idea of a diagram,
  and the misconceptions a book anticipates. Every note records *where* the idea came from.
- **Wording is never reused.** Notes paraphrase. A quotation is at most one short sentence and rare.
  `_tools/validate.py` rejects prose that repeats 12 or more consecutive words from the source.
- **Equations are transcribed** because mathematics is not authorial prose. We still check each one.
- **Figures are described and redesigned,** never reproduced. Each figure entry proposes an original visualization.
- The vault stores locators, not page text. The original page remains the reference.

## Locators

A locator identifies a source position: `{ "pdf_page": 143, "printed_page": 125, "section": "5.3" }`.
It renders as `SCH §5.3 p.125 (pdf 143)`. The PDF page is the export folder `book-sources/<book>/pages/page-143/`.
Printed page = PDF page − offset (SCH 18, GA 17, DIV 15). Figure images use paths relative to `book-sources/`,
for example `schutz/pages/page-143/img-48.jpeg`.

## Layout

```
knowledge/
  README.md                     this file
  _schemas/                     JSON Schemas for every structured note type
  _tools/                       build, validate, and render scripts
  _index/                       generated machine indices for the app and tutor (later phase)
  _build/                       intermediate generated data (e.g. concept candidate clusters)
  _meta/                        design notes (tutor access, unit lists)
  sources/<book>/
    toc.json                    parts, chapters, sections with printed and PDF pages
    book-profile.md             what the book is, its audience, conventions, and teaching signature
    chapters/<unit>.json        chapter dossier (source of truth)
    chapters/<unit>.md          rendered note (generated; do not edit)
  sources/legacy/               inventory of the earlier "General Relativity, From the Inside Out" project
    <group>.json, overview.md   manuscript, lessons, labs, figures, app code, reviews; reuse verdicts
  concepts/<domain>/<id>.json   one note per concept on the depth ladder (schema v2; .md rendered)
  visuals/<id>.json             the visual network: diagrams, widgets, animations, 3D demos (.md rendered)
  curriculum/                   union syllabus, prerequisite graph, learning paths (later phase)
  pedagogy/                     analogies, misconceptions, thought experiments, demos, worked examples (later phase)
  notation/                     sign conventions and symbol crosswalk across the books (later phase)
  history/                      people and timeline (later phase)
```

## Build phases

| Phase | Output | Status |
| --- | --- | --- |
| 0. Source manifests | `sources/<book>/toc.json`, reading copies and inventories in `book-sources/_chapters/` | done |
| 1. Chapter dossiers | 94 units read and independently verified (PDF renders for export losses); book profiles | done |
| 1b. Legacy inventory | 336 assets with reuse verdicts; `sources/legacy/overview.md` ranks what to carry forward | done |
| 2. Concept union | registry done (1,370 concepts in 24 domains, 0 check errors) | done |
| 3. Concept notes and visuals | standard v2 (`_meta/writing-guide.md`); notes per domain with novice and physics reviews; visual network | in progress |
| 4. Curriculum | cross-book sequencing, prerequisite DAG, modules and lessons at several entry levels | planned |
| 5. Tutor layer | generated indices, retrieval functions, learner-memory schema, completeness review | planned |

## Commands

```bash
python3 knowledge/_tools/build_source_manifests.py
python3 knowledge/_tools/validate.py dossier knowledge/sources/schutz/chapters/ch05.json
python3 knowledge/_tools/render_dossier.py knowledge/sources/schutz/chapters/ch05.json
```
