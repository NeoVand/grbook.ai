---
type: guide
status: adopted
decided: 2026-09-13
revised: 2026-09-13 (after two rounds of independent critique)
applies_to: concept notes (knowledge/concepts), visuals (knowledge/visuals)
---

# How we write the vault

The vault is the raw material for a general relativity book and its interactive experience. Everything must be
**as explicit and simple as possible at the start, and deep enough to carry a reader to research**. The AI tutor
retrieves these notes and teaches from them live. A sentence that confuses a beginner, or an equation with a wrong
sign, becomes a real learner's confusion.

**Read this guide completely before writing or reviewing, and read the relevant section again whenever a validator
warning surprises you.** Then read:

- the schemas `knowledge/_schemas/concept-note.schema.json` and `knowledge/_schemas/visual.schema.json`;
- the conventions `knowledge/notation/course-conventions.md`;
- the exemplars `knowledge/concepts/curvature/holonomy.json` and `knowledge/visuals/carry-an-arrow-around-a-loop.json`.

Writers copy exemplars more than guides, so the exemplars obey every rule here, including a filled review record.

## 1. The books are our teachers, not our subject

We studied three textbooks and the author's earlier course to learn how GR is taught well. That study lives in
`knowledge/sources/`. It is scaffolding.

- **Never mention the source books, or any textbook, in any field.** That covers titles, authors, abbreviations,
  chapters, page or equation numbers, "one textbook", "the authors", and names of standard texts used as convention
  labels.
- **Never copy their wording.** Take ideas, not sentences. Invent your own numbers and situations. The validator flags
  12 or more consecutive words shared with a source.
- **Record what you drew on only in `provenance`.** It is internal and never shipped.
- **Cite only the giants.** History and research references name the people who made the ideas, their primary works,
  and good reviews for researchers. References are structured objects with real author names; set `more_authors` when
  you list only the first few.
  - A writer always sets `verified: false`.
  - Only the physics reviewer sets `verified: true`, after confirming authors, year, title and venue. The reviewer
    also adds a DOI or arXiv id when one exists.
  - **If you are not certain, leave it out.** Never invent a reference.

## 2. Who sees what

The schema marks each field with `x-audience`:

- `reader`: learners in the book and app;
- `tutor`: the AI tutor only;
- `author`: authors and demo builders;
- `system`: runtime metadata such as ids and links;
- `internal`: never shipped.

A build step ships each audience only its own fields. The runtime never reads `knowledge/` directly.

| Field | Seen by | Contract |
| --- | --- | --- |
| summary, tagline, objectives, glossary | readers at every rung | Entry items obey the novice contract. |
| A way's recap, explanation, try_it, takeaway, picture, simplifies | readers at that way's rung | Entry ways obey the novice contract in every one of these fields. |
| key_equations, derivations, worked_examples, problems, observations, analogies, checks, notation_traps | readers at the item's rung | Entry items obey the novice contract. |
| misconceptions, teaching_arc, tutor_moves, a way's gist, pronunciations | the tutor | Entry items are spoken, so they are plain words with no math. |
| visuals[].sketch, a visual's design_rules and model, tour `show` | authors | |
| provenance, review, starting_material | internal | |

## 3. The depth ladder

Every idea is written on up to four rungs. Each rung stands on the one below it.

| Rung | Reader | May use | Gives |
| --- | --- | --- | --- |
| `entry` | A curious 16-year-old with school algebra and geometry, no calculus, no physics beyond everyday experience, who knows only the entry rung of this concept's prerequisites | Words, everyday objects, pictures, simple arithmetic, degrees and fractions of a turn; at most three math expressions per explanation | A concrete situation, the idea in plain words, why it matters, and a real-world number |
| `working` | A strong second-year undergraduate with calculus, vectors and matrices | Calculus, vectors, matrices, SI with G and c; component and index notation only once `index-notation` is a prerequisite (directly or through a prerequisite) | Key relations and their meaning, every algebra step, standard examples, numbers with units |
| `formal` | A first-year graduate student | Coordinate-free notation, manifolds, forms, groups, theorems with proof sketches, G = c = 1 | Precise definitions, hypotheses, theorems, limits of validity |
| `research` | A PhD student starting research | Anything, with references | Modern formulations, generalizations, open problems, landmark papers and reviews |

### Tiers and the rungs they require

| Tier | What it is | Ways, objectives and checks required at | Notes |
| --- | --- | --- | --- |
| `prerequisite` | Background from outside GR (calculus, mechanics, electromagnetism) | entry, working | A formal way is optional; never invent formal padding |
| `foundation` | Needed before curvature (special relativity, tensors, the equivalence principle) | entry, working, formal | |
| `core` | Central GR | entry, working, formal | 2–5 research_horizon topics |
| `advanced` | Beyond a first course | entry (150–400 words), working, formal, research | 2–5 research_horizon topics, at least one review |
| `frontier` | Research-level context | entry (one short honest way, 150–300 words, saying what the reader would need first), formal, research | Working optional; 2–5 research_horizon topics, at least one review |

### Rules for the ladder

- **Keep it continuous.** Every way except the first entry way lists in `continues` the earlier ways it climbs from.
  A later way may continue more than one. Its first sentence refers back to one of them by its picture or result
  ("The paper tube in 'Bent is not the same as curved' returned every arrow unturned…").
- **Never point by position.** Do not write "above", "below", "earlier", "later" or "previously" to point within a
  note, because ways are retrieved one at a time. Name the thing, or put its address in `refs`.
- **Justify each equation at or below its rung.** `justified_by` is a derivation at the same or a lower rung, a
  prerequisite concept, or `"stated"`. If it is stated, the prose says it is taken on trust.
- **Make entry ways self-sufficient.** If an entry way uses a test, rule or name from another way or a prerequisite,
  restate it in `recap`. The book hides the recap when the reader arrives in sequence.

## 4. The novice contract

This contract covers every field section 2 marks for entry readers. You know this material too well, and that is
the main risk: experts skip steps they no longer see. Write for a bright friend who will stop you at every word they
don't know.

1. **Start concrete.** Begin with something the reader can picture, hold or do: a walk, a ball, a clock, a lift, a
   sheet of paper. Never begin with a definition.
2. **Keep sentences short.** Average 20 words or fewer, never more than 32. Put one idea in each paragraph.
3. **Make every step explicit.** When a sentence follows from the one before, say how ("so", "because", "this
   means"). Never leave the reader to supply the link. Don't start more than one sentence in three with a connective.
4. **Introduce at most one new term per paragraph,** in its own sentence ("This is called holonomy."), and only after
   the reader has met the thing it names. Add it to the `glossary`, with `say_as` if it is hard to pronounce.
5. **Use one word per idea and one idea per word, across the whole note and its visuals.**
   - No synonyms: always "loop", never also "closed path".
   - No word in two senses. The walker *turns* at corners, the arrow must not *swing*, and the arrow *comes back
     turned*. "Flat" describes surfaces, not how an arrow lies.
   - In speech, avoid words that double as directions: "left" meaning departed, "right" meaning exactly, "straight"
     meaning immediately.
6. **Give every direction its reference.** Say whose left, facing which way, seen from where.
   - Prefer directions relative to the path: ahead, left, right, behind.
   - Never use compass directions at or near a pole.
   - Announce every switch between the view from inside and a view from outside ("Seen from above the North
     Pole, …").
   - On a closed surface, never say "inside the loop". Name the region instead ("the smaller piece, on your left as
     you walk").
7. **Give every measurement its measurer.** Say who measures a time, length, speed or "same moment", with which clock
   or ruler, and where that person is ("the astronaut's own wristwatch", "clocks on the ground").
   - Say "moving relative to the platform", never just "moving".
   - Keep "sees" (light reaching an eye) apart from "measures" (after allowing for the light's travel time).
8. **Make every rule doable.** Any rule in a thought experiment ("never let the arrow swing", "let go and fall
   freely") must be something the reader could physically do at each step and at each corner. If the precise rule is
   simple, it goes in the explanation, not in `simplifies`.
9. **Back every surprise.** Within two sentences of a surprising claim, give its reason, a count the reader can check,
   or a test they can try with household objects. A `try_it` must be doable as written and must say what the reader
   should see.
10. **Never describe a change with a word that sounds unchanged.** Avoid "still points south" unless you explain at
    once why the word hides the change. Compare against a named, visible reference.
11. **Use pronouns only when the noun is unmistakable.** "It", "this" and "that" refer only to a noun in the same or
    the previous sentence with no other candidate. Otherwise repeat the noun.
12. **Include one real number in everyday units,** and answer "why don't I notice this in daily life?" with a number.
    At entry, use no radians, no scientific notation, and no unit symbols without words.
13. **Try the first what-ifs.** Before finishing, list the three variations a curious teenager would try first (walk
    the equator, walk backwards, use a bigger ball, use a faster train). Make every general sentence true for them,
    or scope it ("most loops"). Check the takeaway and the summary first: short general sentences are where false
    what-ifs hide.
14. **Never write** *clearly, obviously, trivially, evidently, of course, it is easy to see, recall that, as is well
    known*.
15. **Keep simplifications true.** A simple sentence must be correct within a stated scope. The entry prose must be
    true for a reader who never sees `simplifies`.
16. **Make entry checks self-contained.**
    - They are answerable from the entry ways alone.
    - The starting state is unambiguous: a fresh arrow, or the already-turned arrow.
    - They use specific numbers.
    - The answer is a chain of because-steps with no missing link.
    - An opening question names its setting, so an answer that is right in everyday life is never marked wrong.
17. **Give each entry way one idea.** An entry way answers its own `question` with one picture and one chain of
    reasons. If the reader must also take in a second new idea (how distant clocks are set, why the other side finds
    the same stretch), give that idea its own entry way and question, or move it to the working rung. A way that
    asks a beginner to hold two new ideas at once is a stumble, however short its sentences are.

**Before:** "Parallel transport around a closed curve induces a rotation proportional to the enclosed Gaussian
curvature."
**After:** "Carry a cardboard arrow around a loop on a ball, and never let it swing left or right. Back at the start,
compare its direction with the direction it had when you set off. Most loops bring it back turned."

**Wording traps.** The validator flags many of these, and the novice reviewer clears the rest.

- *Directions and places:*
  - compass words near a pole;
  - "up" or "down" on a ball;
  - "inside the loop" on a closed surface;
  - "from the inside";
  - "straight" on a curved surface without a definition;
  - "clockwise" without a viewpoint;
  - "still points".
- *Measurements:*
  - "time slows down" without saying compared with whose clock;
  - "at the same time" without saying by whose clocks;
  - "the observer" without a place;
  - "up" and "down" for someone in free fall;
  - "stretches" or "expands" without saying what is compared;
  - "sees" used to mean "measures".
- *Words doing double duty:* one verb for two kinds of turning; "flat" for both a surface and a position.

**Physics traps.** If you use one of these pictures, state its limits.

- *The rubber sheet.* It uses gravity to explain gravity, and it shows only space bending, while everyday gravity is
  mostly the warping of time.
- *"Light slows down near a mass."* Only a coordinate speed changes; every local observer measures $c$.
- *"The escape speed at a black hole exceeds light speed."* Inside the horizon every future path leads inward.
- *"The universe expands into something" or "galaxies fly apart through space."*
- *"Curved means bent, like a tube."* A rolled paper tube is intrinsically flat.
- *"The event horizon is a place where something happens locally."* A freely falling observer notices nothing
  special there.

## 5. The accuracy contract

This applies at every rung.

1. **Follow the conventions file.** `knowledge/notation/course-conventions.md` is binding. If you need a choice it
   does not make, stop and report it.
2. **Derive or check every equation yourself.** Check dimensions, signs, index placement, and factors of 2 and $\pi$.
   Check limits: flat space gives zero, weak fields give Newton, and small loops give the leading order.
3. **Compute every number with `python3`,** with units and sensible significant figures. Work every check, example
   and problem to its final answer.
4. **Give every universal sentence its hypotheses.** *Never, always, must, exactly, any* and *all* need conditions:
   dimension, simple or contractible loop, orientability, no singular points or holes, vacuum, symmetry,
   idealization.
5. **State sense and branch.** Every angle, phase or rotation states its positive sense intrinsically. For surfaces,
   use the conventions row: positive means toward the walker's left. Say "modulo $2\pi$" where it applies. When a
   published value uses a different sign convention, say so. Check any "equals" or "differs by" claim with signs,
   preferably by a small numerical calculation.
6. **Name the frame or basis** when a statement holds only in one. For example, connection matrices commute in two
   dimensions only in an orthonormal frame, not in a coordinate basis.
7. **Check analogies that relate quantities** with signs, not only in magnitude.
8. **Never claim something does not exist** ("no such law exists", "cannot be defined") unless a theorem in the note
   backs it. Prefer "there is no simple X; the exact statement is Y".
9. **Name objects unambiguously:** first or second Bianchi identity, local or global Gauss–Bonnet, restricted or full
   holonomy. A group contains transformations, not loops.
10. **Try counterexamples** against every simple statement.
    - For geometry: a cone tip, a hole, a Möbius band, a great circle, a figure-eight loop, a region bigger than half
      a closed surface, a non-commuting case, a bent but flat surface.
    - For physics: the non-relativistic limit, a massless case, a non-static case, a strong field, and a different
      choice of observer or slicing.
11. **Record the verification.** The physics reviewer writes what was checked and how in
    `review.physics.verification`, as the exemplar does.
12. **Prefer leaving something out** to including something that might be wrong.

## 6. Text formats

Every string field declares its format with `x-format`.

- **`md`:**
  - Paragraphs are separated by blank lines. Use `- ` bullets and `*emphasis*`, and nothing else: no headings,
    links, HTML or tables.
  - Inline math goes in `$…$`. Display math goes in `$$…$$` as its own paragraph. A literal dollar sign is `\$`.
  - Every symbol, Greek letter, index, subscript and superscript goes inside math, never as Unicode pseudo-math.
    Unit squares like km² are allowed.
- **`latex`:** bare KaTeX with no `$` delimiters.
- **`speech`:** words a voice can read.
  - No `$`, backslashes, carets, underscores, Unicode super- or subscripts, or ×.
  - Write numbers as they are spoken.
  - Give symbols in words.
- **`plain`:** sentences with no markup and no math.

## 7. Ids and addresses

Every addressable item has a kebab-case `id`, unique within its collection, that names the idea
(`direction-does-not-matter`) rather than its position.

**Address forms:**
- Concept items: `<collection>/<item-id>` within a note, and `<concept-id>/<collection>/<item-id>` across notes.
- Visuals: `visual:<visual-id>`, `visual:<visual-id>/presets/<preset-id>` and
  `visual:<visual-id>/tours/<tour-id>/beats/<beat-id>`.

**Ids are permanent once published.** Change the text, never the id. If an item must go after publication, move its
id to `retired_ids`, so stored learner evidence still resolves.

**Links inside a note:**
- `checks[].targets` lists misconception ids, and `misconceptions[].diagnosed_by` lists check ids. The two lists must
  agree.
- `problems[].targets` may also list misconceptions.
- `objectives[].evidenced_by` lists `checks/` or `problems/` addresses at the objective's own rung. Every check and
  problem evidences some objective.
- `if_stuck[].misconception` names a misconception id, or null.
- `refs`, `uses` and `justified_by` use addresses.
- A tour beat's `check` links the beat to the concept check or problem its prediction evidences.

## 8. Fields, and how to fill them

- **`title`, `tagline`, `aliases`.** The title is the canonical name ("Holonomy"). The tagline is a plain phrase of
  about 12 words. Aliases are true synonyms only; a distinct object gets its own concept.
- **`summary`**: two or three entry-rung sentences, speakable, and true for the first what-ifs.
- **`objectives`**: one skill each, starting with a verb. Every required rung has at least one objective, and each
  objective is evidenced by a check or problem at its own rung. Worked examples demonstrate; they are not evidence.
- **`ways_in`**: genuinely different routes, each answering its own `question`.
  - **Kinds:**
    - `picture`: a concrete scene the reader imagines or builds.
    - `operational`: what a named observer or instrument measures, and how.
    - `calculation`: a quantitative relation derived or applied.
    - `structure`: definitions, classifications, theorems.
    - `historical-puzzle`: the problem that forced the idea.
    - `bridge`: the same mathematics in other physics.
    - `contrast`: a near-miss case that isolates the idea.
  - **Kind rules:** use at least two kinds, and no kind for more than half of a note's ways. Foundation and core notes
    with observations include at least one operational way.
  - **Fields of a way:**
    - `takeaway` is the sentence the reader should be able to say back.
    - `gist` is null unless the tutor's spoken opener must differ from the takeaway.
    - `picture` is null when the way cites a visual.
    - `visuals` are `{id, preset, tour}` references.
    - Each id in `assumes` must be a prerequisite with `needed_for` at or below the way's rung, or a prerequisite of
      one, and never appears in `leads_to`.
- **`glossary`**: every technical term the entry rung uses, with its forms, a plain definition, `say_as` when needed,
  and the concept that owns it when there is one.
- **`pronunciations`**: names and words a voice may get wrong.
- **`prerequisites`**: direct prerequisites only, with `why` and `needed_for`. Use registry ids and create no cycles.
- **`leads_to`, `related`**: registry ids, each with a reason.
- **`key_equations`**: id, name, rung, LaTeX, meaning, every symbol (meaning and how to say it), `conditions`,
  `say_aloud` and `justified_by`.
- **`derivations`**: one move per step. If a step combines many terms, split it.
- **`worked_examples`**: an original problem, one move per step, the answer with units, and a takeaway. Foundation
  and core notes need at least one. Don't repeat a computation that a check or problem already covers.
- **`problems`**: graded practice for self-study. Give each a difficulty from 1 to 3 and a type. Include
  `statement_spoken` when the statement has math, up to three hints (gentlest first), the answer, `key_points`,
  `numeric` answers, a full solution, and `targets`.
  - Minimum count: prerequisite notes 1, foundation notes 2, core and above 3.
  - Problems span at least two rungs when there is more than one.
- **`observations`**: real measurements that connect the concept to the world, with numbers and a reference. A
  phenomenon that has been measured is `measured`, even if it is not gravitational. Leave the list empty only when no
  honest connection exists.
- **`teaching_arc`**: 3 to 8 steps from a motivating question to a picture, formalism, check and transfer. Each move
  is one or two sentences that point at content through `uses` rather than restating it.
- **`analogies`**: from a different setting than every way. If an analogy uses the same scenario as a way, delete it.
  Give an explicit mapping and the limits.
- **`misconceptions`**: at most 8, each one real.
  - `belief`: in the learner's words.
  - `why_tempting`: one sentence.
  - `correction`: at most two sentences that name why the belief fails. The full reasoning lives in the diagnosing
    check's answer.
  - `diagnosed_by`: the ids of the checks that expose it.
- **`checks`**: gradable.
  - Give a format, and `question_spoken` when the question has math.
  - The answer is a chain of because-steps.
  - Give `key_points`, hints, `targets` and an optional visual.
  - `numeric` answers carry a unit from the unit table, a sign (`signed` in the note's stated sense, or
    `magnitude`), tolerances (`abs_tol` is required when the value is 0) and a modulo for angles.
- **`notation_traps`**: variants readers will meet, in generic terms, with a `course_choice` from the conventions
  file.
- **`visuals`**: links to the catalog, each with this concept's priority. A proposal not yet in the catalog needs a
  `sketch`.
- **`tutor_moves`**:
  - opening questions that name their setting and invite a prediction;
  - if-stuck moves for symptoms that are not misconceptions;
  - common questions with rungs;
  - level switching with signals.

  If-stuck moves, common questions and level switches carry `uses` addresses so the tutor can act on them. Entry
  common-question answers are spoken, so they contain no math.
- **`history`**: people, an integer year, the primary work as a reference or null, and a precisely scoped
  contribution.
- **`research_horizon`**: topic, a connection of two to four sentences, and references.
- **`retired_ids`**: empty until something published is removed.
- **`provenance`**: the source units and legacy assets you drew on.

**Lifecycle.** The note moves through these stages:

1. The writer sets `draft`, revision 1, and today's date.
2. The novice reviewer sets `novice-reviewed`.
3. The physics reviewer sets `physics-reviewed`, but only with a verdict of `accurate` or `fixed`. A verdict of
   `needs-attention` leaves the status at `novice-reviewed`.
4. Each review records `reviewed_revision`.
5. **Any learner-visible change bumps the revision,** including a reviewer's own fixes after the other review has
   signed off. The changed text then gets the other lens, and only that text:
   - When the physics review changes text a learner meets, a novice re-read covers exactly those changes and is
     recorded in `review.novice.rereads`.
   - When that re-read changes text, a physics diff check covers exactly those changes and is recorded in
     `review.physics.diff_checks`.
   - Each sets its stage's `reviewed_revision` to the revision it signed.
   - `python3 knowledge/_tools/note_diff.py <before.json> <after.json>` (or `--git <rev> <note.json>`) lists the
     changed learner-visible sentences with their rungs.
6. An editor sets `published` only when both stages cover the current revision. The runtime serves only published
   notes.

Every schema_version bump ships a migration script in `knowledge/_tools`, and loaders accept the current and
previous versions.

## 9. Length budgets

Word counts exclude ids, enum values and reference metadata. The validator warns above each cap and below each
minimum. Only about a quarter of a full core note is explanation prose; most of the rest is gradable checks and
problems, which the learner model and the tutor depend on.

- **Caps are ceilings, not targets.** Write what each rung needs, then stop. The pilot showed that notes filled to
  every cap get dense: reviewers add the explicit steps a beginner needs, then squeeze other sentences to fit.
- **Drafts leave headroom.** A draft stays within 80% of every cap, so reviewers have room for explicit steps.
- **Never compress to fit.** When a clarity or accuracy fix needs words and a part is at its cap, drop or shorten the
  lowest-value item: a check that tests the same skill as another, a common question a way already answers, a second
  analogy. Never compress entry sentences or check answers, and say in the review's fixes what you dropped.
- **The formal rung carries graduate readers.** Tiers that require it need at least two formal checks and one formal
  problem, and a formal way with real substance: precise definitions, hypotheses, results with proof sketches, and
  limits of validity.

| Part | Prerequisite | Foundation | Core | Advanced | Frontier |
| --- | --- | --- | --- | --- | --- |
| Entry way explanations | 400–1,000 | 400–1,000 | 400–1,000 | 150–400 | 150–300 |
| Working way explanations | 300–900 | 300–900 | 300–1,000 | 300–1,000 | 0–1,000 |
| Formal way explanations | 0–300 | 300–600 | 400–900 | 400–1,100 | 400–1,100 |
| Research way explanations | 0 | 0 | 0–400 | 250–900 | 250–900 |
| Other way fields (question, gist, recap, try_it, takeaway, picture, simplifies) | 450 | 650 | 800 | 800 | 800 |
| Equations, derivations, examples, problems, observations | 900 | 1,500 | 2,300 | 2,500 | 2,500 |
| Objectives, misconceptions, checks, arc, tutor moves, analogies, glossary, traps | 1,200 | 2,200 | 3,300 | 3,500 | 3,500 |
| Links, visuals, history, research horizon | 200 | 300 | 900 | 1,000 | 1,000 |
| **Total cap** | **5,000** | **7,000** | **9,500** | **10,500** | **10,500** |

## 10. Visuals: a network of pictures, and a contract for components

Diagrams, widgets, animations and 3D demos live in `knowledge/visuals/<id>.json`. One visual usually serves several
concepts. Visuals link to each other through `builds_on`, `leads_to` and `variant_of`.

- **Name visuals after the picture, not the concept.** Search with
  `python3 knowledge/_tools/visual_ids.py --grep <word>` and reuse ids.
- **A proposal in a note** gives a `sketch`: what the learner sees, what they change, what updates, and what it
  proves. Contrast two readouts only when they differ physically, not when they show one quantity on two branches.
- **A catalog entry is a component contract:**
  - `params` are typed, with ranges, steps, defaults, and `available_when` constraints for combinations that make
    sense.
  - `presets` are named states.
  - `readouts` declare unit, sense, range (branch), decimals, visibility, and speech templates, including
    `say_negative` for signed values.
  - `tours` hold beats for a concept. A visual serving several concepts may have several tours. A beat names a
    preset, optional overrides and an animation, its `say` and `describe` lines in first-person speech, and the check
    it evidences.
  - `model.tests` give a full state (with progress at 1 when a readout appears only on completion), the expected
    readout values with tolerances, and readouts that must stay hidden. They compile into unit tests.
  - Every state used by a tour, a test, or a note's `{id, preset}` must be a declared preset whose combinations are
    available.
  - Design rules name the misconception they prevent.
  - `print_figure` describes the book figure.
  - `accessibility` gives a static alternative and keyboard control.
  - A visual whose status is `built` or `published` names its component.
- **Figures from the books** inspire compositions; they are never reproduced.

## 11. Reviews

Each note passes two independent reviews before it counts as done. Each review records its findings in the note, as
the exemplar shows.

1. **Novice review.** The reviewer adopts the entry persona and reads, sentence by sentence, only the fields section
   2 marks for entry readers.
   - **Before fixing anything,** write `retell_attempt`: what the persona would say back after one reading. Compare
     it with the entry takeaways.
   - **Record every stumble** as a quote, the problem, and a rewrite:
     - every sentence reread;
     - every undefined word;
     - every step taken on trust;
     - every direction or measurement without a reference;
     - every word used in two senses;
     - every false first what-if;
     - every way that asks the reader to hold two new ideas at once (rule 17);
     - every sentence squeezed to fit a budget;
     - every wording-trap warning from the validator.
   - **Fix and check the ladder.** Rewrite until the contract holds, then climb the ladder as a stronger student and
     add bridges where there is a jump.
   - **Sign off:** set `status: novice-reviewed` and `reviewed_revision`.
2. **Physics review.** The reviewer works as an adversarial referee.
   - Re-derive every equation, and recompute every number.
   - Work every check and problem.
   - Verify conventions, sense and branch, frames, conditions, and analogy relations with signs.
   - Try the counterexamples from section 5.
   - Confirm every reference.
   - Check the novice reviewer's rewrites for accuracy.

   Fix errors while keeping the simplicity: an inaccurate simple sentence becomes an accurate simple sentence. Record
   `verification` and `counterexamples`. Set `status: physics-reviewed` only with a verdict of `accurate` or `fixed`.
