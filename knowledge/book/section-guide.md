# Writing book sections

The book section is the unit of writing. The standard card (`_meta/standard-card.md`) is binding for every
sentence; this guide says what a section is and how it differs from a concept note.

## 1. The book is the depth ladder
- A section is written at one depth (`entry`, `working`, `formal`, `research`), the depth the outline gives it.
  The reader has read every section before it on its track, so it does not restate them: it names them
  ("as in *Falling in*") and moves on. Nothing needs four rungs of its own.
- `main` sections carry every reader; `advanced` sections may assume the main track up to that point plus
  earlier advanced sections; `reference` sections are read on demand and stand alone.
- Entry-depth text obeys the whole novice contract. Working depth uses calculus and vectors and keeps the contract's
  rules 3 (explicit steps), 5 (one word per idea), 6 (directions with references), 7 (measurements with measurers)
  and 13 (first what-ifs). Formal and research depth are precise and complete: definitions, hypotheses, results
  with proof sketches, limits of validity, and references for anything not derived.

## 2. What a section contains
- `teaches` is exactly the outline's concept list. Every concept appears in some part's `teaches`, and its name is
  used in the text where it is introduced, so the tutor and the index can find it. A concept gets the space it
  deserves: a big idea gets a whole part with a picture and a check; a lemma gets a paragraph.
- `opening`: one concrete scene, puzzle or measurement, never a definition.
- `parts`: 2 to 8, each with a heading, its concepts, prose, and a takeaway. One idea per part.
- `key_equations` in course conventions, each with `say_aloud`, and `justified` as derived-here, earlier-section or
  stated (and the prose says when something is taken on trust).
- `worked_examples`: at most 3, original, one move per step.
- `checks`: 3 to 8, gradable, at the section's depth, with key points and numeric answers where they apply. Every
  misconception is diagnosed by a check and every check's targets exist.
- `misconceptions`: only real ones, at most 6, correction in one or two sentences.
- `glossary`: every term the section introduces, with the registry concept that owns it.
- `visuals`: reuse a catalog id when one fits (`visual_ids.py`); otherwise propose one with a sketch. A main-track
  section has at least one visual; a flagship visual per chapter is enough.
- `tutor`: an opening question and 2 to 5 common questions, all spoken.
- `further`: for formal and research depth, the landmark papers and reviews; writers set `verified: false`.

## 3. Sizes
Prose (opening, part texts, takeaways) by depth: entry 1,200 to 2,500 words; working, formal and research 1,500 to
3,200. Whole section at most 5,000 words. Caps are ceilings: a draft stays within 80%; a review may use 10% beyond
for recorded fixes; never compress to fit, drop the lowest-value item and say which.

## 4. Sources
Concept notes exist for some concepts (`note_digest.py <id>` prints a digest; `--ways entry` prints its entry
explanations). Use their pictures, numbers and checks freely; they were written for this. For concepts without a
note, `concept_evidence.py --id <id>` shows how the source books teach it. Never mention or copy the books.

## 5. Lifecycle
draft → novice-reviewed (entry and working depth only) → physics-reviewed → published. Any learner-visible change
bumps the revision; text changed after a review gets the other lens through one post-review check.
