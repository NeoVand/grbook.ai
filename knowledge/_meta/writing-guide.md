---
type: guide
status: adopted
decided: 2026-09-13
applies_to: concept notes (knowledge/concepts), visuals (knowledge/visuals)
---

# How we write the vault

The vault is the raw material for a general relativity book and its interactive experience. Everything here must be
**as explicit and simple as possible at the start, and deep enough to carry a reader to research**. The AI tutor
retrieves these notes and teaches from them live, so a sentence that confuses a beginner, or an equation with a wrong
sign, becomes a real learner's confusion.

Read this guide completely before writing or reviewing. Then read the exemplars:
`knowledge/concepts/curvature/holonomy.json` (concept) and `knowledge/visuals/carry-an-arrow-around-a-loop.json` (visual).

## 1. The books are our teachers, not our subject

We studied three textbooks and the author's earlier course to learn how GR is taught well. That study lives in
`knowledge/sources/`. It is scaffolding.

- **Never mention the source books** in any prose field. That includes their titles, authors, abbreviations, chapters,
  page or equation numbers, "one textbook", or "the authors". The validator flags these.
- **Never copy their wording.** Take ideas, not sentences. Rebuild every explanation in your own words, and invent
  your own numbers and situations for examples. The validator flags 12 or more consecutive words shared with a source.
- **Record what you drew on** in `provenance` only (`schutz/ch06`, legacy asset ids). It is never shown to readers.
- **Cite only the giants.** History and research pointers name the people who made the ideas and their primary works:
  Einstein (1915), Schwarzschild (1916), Levi-Civita (1917), landmark papers, and reviews at research level. Format:
  `Author (year), *Title*`. **If you are not certain of a year or title, leave it out.** Never invent a citation.
- Conventions that vary across the literature are described generically ("some texts use the signature
  $(+,-,-,-)$"), not per book.

## 2. The depth ladder

Every idea is written on four rungs. Each rung stands on the one below it.

| Rung | Reader | What it gives |
| --- | --- | --- |
| `entry` | A curious person with school algebra and everyday experience. They have read only the entry rung of this concept's prerequisites. | A concrete situation they can picture or do; the idea in plain words; why it matters. |
| `working` | Comfortable with calculus, vectors and matrices (a strong second-year undergraduate), with the working rung of the prerequisites. | The key relations with their meaning, every algebra step, numbers with units, standard examples. |
| `formal` | A first-year graduate student. | Precise definitions, hypotheses, index and coordinate-free notation, theorems with proof sketches, limits of validity. |
| `research` | A PhD student starting research. | Where the idea lives now: generalizations, open problems, modern formulations, landmark papers. |

- **The ladder must be continuous.** The first working way should start from the entry picture: "In the walk above,
  the turn was a quarter turn. Now let us measure it." Formal builds on working the same way. A reader climbing the
  ladder should never feel a jump.
- **Every entry way is self-sufficient.** If it needs an idea from a prerequisite, re-state that idea in a sentence or
  two. The learner may have arrived straight from search.
- `research` is required for advanced and frontier concepts, recommended for core concepts, and optional below that.

## 3. The novice contract (entry rung)

You know this material too well; that is the main risk. Experts skip steps they no longer see. Write entry prose as
if explaining to a bright friend who will stop you at every word they don't know.

1. **Start with something concrete** they can picture, hold or do: a walk, a ball, a clock, a lift, a stretched sheet
   of paper. Do not start with a definition.
2. **Use short sentences**, 20 words or fewer on average and none over 32. Put one idea in each paragraph.
3. **Make every step explicit.** Say how each sentence follows from the last: "So…", "This means…", "Because…".
   Never leave the reader to infer a step.
4. **Define every technical word** in plain language the first time it appears, or avoid it. Add each one to the
   `glossary`. Words that count as technical include *vector, tangent, coordinate, frame, metric, tensor, geodesic,
   invariant, manifold, curvature, component, derivative*.
5. **Use no symbols unless they are essential.** At most three math expressions per entry explanation, each read out
   in words.
6. **Never write** *clearly, obviously, trivially, of course, it is easy to see, recall that, as is well known*. What
   is obvious to you is the step the beginner is missing.
7. **Keep simplifications true.** A simple sentence must be correct within a stated scope ("on the surface of a
   ball…"). Say what the picture leaves out in `simplifies`. Never say something false to make it simple.
8. **End with the takeaway** in one sentence.
9. **Apply the test:** could a curious 16-year-old retell it correctly after one reading? If not, rewrite it.

**Before:** "Parallel transport around a closed curve induces a rotation proportional to the enclosed Gaussian
curvature."
**After:** "Carry an arrow around a loop on a ball, and never turn it. When you get back, it points in a new
direction. A bigger loop gives a bigger turn."

**Known traps.** If you use one of these popular pictures, state its limits explicitly.

- *The rubber sheet.* It uses gravity to explain gravity. It shows only space bending, while most everyday gravity
  comes from the warping of time.
- *"Light slows down near a mass."* Only a coordinate speed changes. Every local observer measures $c$.
- *"Nothing escapes a black hole because the escape speed exceeds light speed."* Inside the horizon every future
  path leads inward. It is not a question of speed.
- *"The universe expands into something" or "galaxies fly apart through space."*
- *"Curvature means bent, like a tube."* A rolled paper tube is intrinsically flat.
- *"The event horizon is a place where something happens locally."* A freely falling observer notices nothing
  special there.

## 4. The accuracy contract (every rung)

- **Conventions are binding:** `knowledge/notation/course-conventions.md`. Signature $(-,+,+,+)$, MTW sign
  conventions, $G = c = 1$ inside derivations, and SI units for every number. State when a sign depends on a
  convention.
- **Derive or check every equation yourself.** Check its dimensions and its limits: flat space gives zero, weak
  fields give Newton, small loops give leading order.
- **Compute every number** (use `python3`), with units and sensible significant figures.
- **State the conditions** of every general claim: vacuum, torsion-free, small loop, two dimensions, spherical
  symmetry, static.
- **Work every answer** to every check and example in full, and confirm it matches.
- **Hold history to the same standard.** If you are not sure, omit it.
- **Prefer leaving something out** to including something that might be wrong.

## 5. Fields, and how to fill them

- **`summary`**: the idea in one breath, in two or three entry-rung sentences a tutor could say aloud.
- **`ways_in`**: 2 to 6 genuinely different routes into the idea. Possible kinds of route:
  - a picture;
  - an operational measurement;
  - a calculation;
  - a historical puzzle;
  - a bridge from other physics.

  Each way has a `rung`, an `explanation`, a drawable `picture`, what it `simplifies`, the concept ids it `assumes`,
  and the `visuals` it uses. At least one way is needed on each of entry, working and formal. Do not restate the same
  explanation at three depths; each way should add a new route or a new layer.
- **`glossary`**: every technical term the entry rung uses, with a plain definition.
- **`prerequisites`**: the direct prerequisites only. Each has a one-line `why` and `needed_for`, the lowest rung that
  needs it (the entry rung often needs fewer). Use registry ids and avoid cycles: if this concept motivates another,
  the other goes in `leads_to`.
- **`key_equations`**: each has a name, LaTeX in course conventions, meaning, every symbol defined, the conditions
  under which it holds, `say_aloud` in plain words (describe meaning; do not spell out index names), and the rung.
- **`derivations`**: step lists at a stated rung. Each step is one move that a reader at that rung can follow without
  paper. End with the result.
- **`worked_examples`**: original situations and numbers. Give the problem, one move per step, the final answer with
  units, and the takeaway. Foundation and core notes need at least one.
- **`teaching_arc`**: 4 to 8 steps from a motivating question to a picture, formalism, check and transfer. Give the
  reason for each step.
- **`analogies`**: the analogy, how it works, an explicit mapping (this ↔ stands for), its limits, and a rung.
- **`misconceptions`**:
  - `belief`: in the learner's own words;
  - `why_tempting`;
  - `correction`;
  - `diagnostic_question`: a question that exposes the belief;
  - `rung`.
- **`checks`**: at least one each at entry, working and formal, all with fully worked answers. At least one check
  targets a misconception, by quoting its `belief` exactly.
- **`notation_traps`**: sign and notation variants a reader will meet in the literature, and the course choice.
- **`visuals`**: links to the visual catalog (section 6). One is `flagship` when the concept has a natural central
  picture.
- **`tutor_moves`**:
  - `opening_questions`: answerable by a novice, inviting a prediction;
  - `if_stuck`: a symptom and a move;
  - `common_questions`: with answers at entry rung unless marked otherwise;
  - `demo_moments`;
  - `voice_notes`: how to say the equations aloud;
  - `level_switching`: signals that a learner is ready for the next rung.
- **`history`**: people, year, primary work (when certain), and contribution.
- **`research_horizon`**: topic, connection, and pointers (author, year, title only when certain).
- **`provenance`**: source units and legacy assets you drew on. Never shown to readers.

**Length.** Aim for 1,200 to 2,500 words for prerequisite and foundation notes, and 2,000 to 3,500 for core,
advanced and frontier notes. Never pad. Never repeat the same content in two fields. The entry explanation is the
exception to brevity: make it as long as it needs to be to leave no step implicit.

## 6. Visuals: a network of pictures

Diagrams, widgets, animations and 3D demos live in `knowledge/visuals/<id>.json`. One visual usually serves several
concepts, and visuals link to each other (`builds_on`, `leads_to`, `variant_of`).

- **Name visuals after the picture, not the concept:** `carry-an-arrow-around-a-loop`, not `holonomy-demo`. Before
  proposing a new id, search `knowledge/visuals/` and the `visuals` of nearby notes, and reuse an existing id when it
  fits.
- **Describe a proposed visual in a note** with a `sketch`: what the learner sees, what they change, what updates, and
  what it proves. The visual phase turns sketches into catalog entries.
- **Contents of a catalog entry:**
  - the composition and a plain caption;
  - variants: static card, 2D, 3D;
  - interactions;
  - a guided `tour` the tutor can narrate, beat by beat;
  - `design_rules`, derived from misconceptions;
  - the physics `model`, with numerical test cases;
  - the concepts it serves;
  - accessibility;
  - starting material from the legacy course.
- **Figures from the books** inspire compositions. Redesign them; never reproduce them.

## 7. Reviews

Each note passes two independent reviews before it counts as done.

1. **Novice review.** A reviewer role-plays the entry reader, flags every undefined word, skipped step and ambiguous
   sentence, rewrites until the novice contract holds, and checks that the ladder climbs without gaps.
2. **Physics review.** A reviewer re-derives equations, works every check and example, verifies conventions, history
   and research pointers, and fixes errors. It keeps the simplicity: an inaccurate simple sentence becomes an accurate
   simple sentence, never a jargon-heavy one.

Both record verdicts, fixes and concerns in `review`.
