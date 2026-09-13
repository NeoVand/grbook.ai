---
type: guide
status: adopted
decided: 2026-09-13
revised: 2026-09-13 (after four independent critiques of the first standard)
applies_to: concept notes (knowledge/concepts), visuals (knowledge/visuals)
---

# How we write the vault

The vault is the raw material for a general relativity book and its interactive experience. Everything must be
**as explicit and simple as possible at the start, and deep enough to carry a reader to research**. The AI tutor
retrieves these notes and teaches from them live. So a sentence that confuses a beginner, or an equation with a wrong
sign, becomes a real learner's confusion.

**Read this guide completely before writing or reviewing, and read it again when a validator warning surprises you.**

Then read:

- the schemas `knowledge/_schemas/concept-note.schema.json` and `knowledge/_schemas/visual.schema.json`;
- the conventions `knowledge/notation/course-conventions.md`;
- the exemplars `knowledge/concepts/curvature/holonomy.json` and `knowledge/visuals/carry-an-arrow-around-a-loop.json`.

Writers copy exemplars more than guides, so the exemplars obey every rule here.

## 1. The books are our teachers, not our subject

We studied three textbooks and the author's earlier course to learn how GR is taught well. That study lives in
`knowledge/sources/`. It is scaffolding.

- **Never mention the source books in any field.** No titles, authors, abbreviations, chapters, page or equation
  numbers, "one textbook", or "the authors".
- **Never copy their wording.** Take ideas, not sentences. Invent your own numbers and situations. The validator flags
  12 or more consecutive words shared with a source.
- **Record what you drew on only in `provenance`.** The runtime strips `provenance`; readers never see it.
- **Cite only the giants.** History and research references name the people who made the ideas, their primary works,
  and good reviews for researchers. References are structured objects. A writer always sets `verified: false`; only
  the physics reviewer sets `verified: true`, after confirming authors, year and title against a reliable record.
  **If you are not certain, leave it out.** Never invent a reference.

## 2. Who sees what

| Field | Seen by |
| --- | --- |
| summary, tagline, objectives, glossary, pronunciations | Readers at every rung. Entry-rung items obey the novice contract. |
| Each way's gist, recap, explanation, try_it, takeaway, picture, simplifies | Readers at that way's rung. Entry ways obey the novice contract in every one of these fields. |
| key_equations, derivations, worked_examples, problems, observations, analogies, checks, notation_traps | Readers at the item's own rung. |
| misconceptions, teaching_arc, tutor_moves, each way's retell | The tutor and authors only. Entry-rung items are still written in plain words, because the tutor speaks them. |
| provenance, review | Internal only. |

## 3. The depth ladder

Every idea is written on four rungs. Each rung stands on the one below it.

| Rung | Reader | May use | Gives |
| --- | --- | --- | --- |
| `entry` | A curious 16-year-old with school algebra and geometry, no calculus, and no physics beyond everyday experience. They know only the entry rung of this concept's prerequisites. | Words, everyday objects, pictures, simple arithmetic, degrees and fractions of a turn. At most three math expressions per explanation. | A concrete situation, the idea in plain words, why it matters, and a real-world number. |
| `working` | A strong second-year undergraduate with calculus, vectors and matrices. | Calculus, vectors, matrices, and SI units with G and c. Component and index notation only once `index-notation` is a prerequisite at or below working. | The key relations and their meaning, every algebra step, standard examples, and numbers with units. |
| `formal` | A first-year graduate student. | Coordinate-free notation, manifolds, forms, groups, theorems with proof sketches, and $G = c = 1$. | Precise definitions, hypotheses, theorems, and limits of validity. |
| `research` | A PhD student starting research. | Anything, with references. | Modern formulations, generalizations, open problems, and landmark papers and reviews. |

- **The ladder is continuous.** Every non-entry way names in `continues` the earlier way it climbs from. Its first
  sentence refers back to that way's picture or result by name, for example "In the walk from the North Pole…".
- **Never write** "above", "below", "earlier" or "later" to point within a note. Ways are retrieved one at a time, so
  name the thing, or put its address in `refs`.
- **An equation is justified at or below its rung.** Its `justified_by` is a derivation at the same or a lower rung,
  a prerequisite concept, or `"stated"` (taken on trust, which the prose must say).
- **Entry ways are self-sufficient.** Put any re-statement of a prerequisite idea in `recap`, not in `explanation`.
  The book hides the recap when a reader arrives in sequence.
- **What each tier requires:**
  - Advanced and frontier notes need a `research` way that actually teaches a modern formulation.
  - Core, advanced and frontier notes need 2 to 5 `research_horizon` topics with references. Advanced and frontier
    notes include at least one review.
  - Notes of other tiers may omit research.

## 4. The novice contract

This contract applies to entry-rung reading, in every field that section 2 marks. You know this material too well, and
that is the main risk: experts skip steps they no longer see. Write for a bright friend who will stop you at every
word they don't know.

1. **Start concrete.** Begin with something the reader can picture, hold or do: a walk, a ball, a clock, a lift, a
   sheet of paper. Never begin with a definition.
2. **Keep sentences short.** Average 20 words or fewer, and never more than 32. Put one idea in each paragraph.
3. **Make every step explicit.** Link each sentence to the one before with "So…", "This means…", or "Because…".
4. **Introduce at most one new term per paragraph,** in its own sentence ("This is called holonomy."), and only after
   the reader has met the thing it names. Add the term to the `glossary`, with `say_as` if it is hard to pronounce.
5. **Use one word per idea for the whole note and its visuals.** No synonyms (always "loop", never also "closed
   path"). Never use one word in two senses: the walker *turns* at corners, the arrow must not *swing*, and the arrow
   *comes back turned*.
6. **Give every direction its reference.** State whose left, facing which way, seen from where. Prefer directions
   relative to the path: ahead, left, right, behind. Never use compass directions at or near a pole. Announce every
   switch between the view from the surface and a view from outside ("Seen from above the North Pole, …"). On a
   closed surface, never say "inside the loop"; name the region ("the smaller piece, on your left as you walk").
7. **Make every rule doable.** Any rule in a thought experiment ("keep the arrow from swinging", "let go and fall
   freely") must be something the reader could physically do at each step and at each corner. If the precise rule is
   simple, it goes in the explanation, not in `simplifies`.
8. **Back every surprise.** Within two sentences of any surprising claim, give its reason, a count the reader can
   check, or a try-it test with household objects (an orange, a sheet of paper, a pencil). Put that test in `try_it`.
9. **Never describe a change with a word that sounds unchanged.** Avoid "still points south" unless you explain at
   once why the word hides the change. Compare against a named, visible reference: the path, a wall, the starting
   arrow.
10. **Use a pronoun only when its noun is unmistakable.** "It", "this" and "that" may refer only to a noun in the same
    or the previous sentence, with no other candidate. Otherwise repeat the noun.
11. **Include one real number in everyday units,** and answer the question "why don't I notice this in daily life?"
    with a number. At entry, no radians, no scientific notation, and no unit symbols without words.
12. **Try the first what-ifs.** Before finishing, list the three variations a curious teenager would try first, such
    as walking the equator, walking backwards, or using a bigger ball. Make sure every general sentence stays true
    for them, or scope it ("most loops").
13. **Never write** *clearly, obviously, trivially, evidently, of course, it is easy to see, recall that, as is well
    known*.
14. **Keep simplifications true.** A simple sentence must be correct within a stated scope. The entry prose must be
    true for a reader who never sees `simplifies`.
15. **Make entry checks self-contained.**
    - They are answerable from the entry ways alone.
    - The starting state is unambiguous: a fresh arrow, or the already-turned arrow.
    - They use specific numbers, not "a little".
    - The answer is a chain of because-steps.
    - An opening question names its setting, so an answer that is right in everyday life is never marked wrong.
16. **End each way with a `takeaway`** of one sentence. Give a `retell`: the one or two sentences a beginner should be
    able to say back.

**Before:** "Parallel transport around a closed curve induces a rotation proportional to the enclosed Gaussian
curvature."

**After:** "Carry an arrow around a loop on a ball, and never let it swing left or right. Back at the start, compare
it with the way it pointed when you set off. Most loops bring it back pointing a new way."

**Wording traps for beginners:**
- compass words at a pole;
- "down" on a ball;
- "inside the loop" on a closed surface;
- "from the inside" (inside the ball, or within the surface?);
- "straight" on a curved surface, unless it is defined;
- "clockwise" without a viewpoint;
- one word used for two different kinds of turning.

**Physics traps.** If you use one of these pictures, state its limits:
- *The rubber sheet.* It uses gravity to explain gravity, and it shows only space bending, while everyday gravity is
  mostly the warping of time.
- *"Light slows down near a mass."* Only a coordinate speed changes; every local observer measures $c$.
- *"The escape speed at a black hole exceeds light speed."* Inside the horizon, every future path leads inward.
- *"The universe expands into something" or "galaxies fly apart through space."*
- *"Curved means bent, like a tube."* A rolled paper tube is intrinsically flat.
- *"The event horizon is a place where something happens locally."* A freely falling observer notices nothing
  special there.

## 5. The accuracy contract

This contract applies at every rung.

1. **Conventions are binding.** Follow `knowledge/notation/course-conventions.md`. If you need a choice it does not
   make, stop and report it. Never make a note-local convention.
2. **Derive or check every equation yourself.** Check dimensions, signs, index placement, and factors of 2 and $\pi$.
   Check the limits too: flat space gives zero, weak fields give Newton, small loops give the leading order.
3. **Compute every number with `python3`,** with units and sensible significant figures. Work every check, example and
   problem to its final answer.
4. **Give every universal sentence its hypotheses.** Words like *never, always, must, exactly, any, all* need their
   conditions stated: dimension, simple or contractible loop, orientability, no singular points or holes, vacuum,
   symmetry, idealization.
5. **Give sense and branch.** Every angle, phase or rotation states its positive sense, and "modulo $2\pi$" where that
   applies. A claim that two quantities are equal or differ by something is checked with signs, preferably by a small
   numerical calculation, not by magnitude alone.
6. **Check analogies that relate quantities.** The relation must be computed and must hold with signs, not only in
   magnitude.
7. **Never claim that something does not exist** ("no such law exists", "cannot be defined") unless a theorem in the
   note backs it. Prefer "there is no simple X; the exact statement is Y".
8. **Name objects unambiguously:** first or second Bianchi identity, local or global Gauss–Bonnet, restricted or full
   holonomy. When a picture reproduces an identity, say at which order in the small size the content appears.
9. **Try counterexamples.** Before finishing, try the standard counterexamples of the domain against every simple
   statement. For geometry: a cone tip, a hole, a Möbius band, a great circle, a figure-eight loop, a non-commuting
   case, and a bent-but-flat surface. For physics: the non-relativistic limit, a massless case, a non-static case,
   and a strong field.
10. **Record the verification.** The physics reviewer writes what was checked, and how, in
    `review.physics.verification`.
11. **Prefer leaving something out** to including something that might be wrong.

## 6. Text formats

Every string field declares its format in the schema through `x-format`.

- **`md`**:
  - paragraphs separated by a blank line, `- ` bullets, and `*emphasis*`;
  - no headings, links, HTML or tables;
  - inline math in `$…$`, and display math in `$$…$$` as its own paragraph;
  - a literal dollar sign is written `\$`;
  - every symbol, Greek letter, index, subscript and superscript goes inside math, never as Unicode pseudo-math
    (write $R^\rho{}_{\sigma\mu\nu}$, not R^ρ_σμν; write $\theta_0$, not θ₀). Unit squares like km² are allowed.
- **`latex`**: bare KaTeX with no `$` delimiters.
- **`speech`**: words a voice can read.
  - No `$`, backslashes, carets, underscores, Unicode super- or subscripts, or ×.
  - Write numbers the way they are spoken ("about 520 thousand square kilometres").
  - Give symbols in words ("the turn", "R", "the Riemann tensor").
- **`plain`**: one or more sentences with no markup and no math.

## 7. Ids and addresses

Every addressable item has a kebab-case `id`, unique within its collection. The learner model and the tutor refer to
items by address:

- `<collection>/<item-id>` within a note, for example `checks/reverse-the-loop`;
- `<concept-id>/<collection>/<item-id>` across notes;
- `visual:<visual-id>` for visuals, with preset and beat ids inside.

**Ids are permanent once published.** Change the text, never the id. Name the idea in the id
(`direction-does-not-matter`), not its position (`check-3`).

Links inside a note:
- `checks[].targets` lists misconception ids;
- `misconceptions[].diagnosed_by` lists check ids, and the two lists must agree;
- `objectives[].evidenced_by` lists addresses of checks, problems and worked examples; every check and problem
  evidences some objective;
- `if_stuck[].misconception` names a misconception id or is null;
- `refs`, `uses` and `justified_by` use addresses.

## 8. Fields, and how to fill them

- **`title`, `tagline`, `aliases`.**
  - `title` is the canonical name ("Holonomy").
  - `tagline` is a plain phrase of about 12 words or fewer.
  - `aliases` are true synonyms only. A distinct object, such as the holonomy group, is its own concept.
- **`summary`**: two or three entry-rung sentences, speakable, true for every first what-if.
- **`objectives`**: what the learner can do at each rung, starting with a verb (Explain, Predict, Compute, Derive,
  Estimate, Distinguish, Prove, State, Use, Sketch). At least one each at entry, working and formal, plus research for
  advanced and frontier notes.
- **`ways_in`**: 3 to 7 routes, using at least two different `kind`s among picture, operational, calculation,
  historical-puzzle, bridge and contrast. Each way answers its own `question`.
  - `gist` is what the tutor says first, at most 300 characters.
  - `explanation` is the full teaching.
  - `takeaway` is one sentence.
  - `visuals` are `{id, preset}` references.
  - `assumes` lists concepts this way relies on. Each must be a prerequisite with `needed_for` at or below the way's
    rung, or a prerequisite of one. It may never appear in `leads_to`.
- **`glossary`**: every technical term the entry rung uses, with its other `forms`, a plain definition, and `say_as`
  when needed.
- **`pronunciations`**: names and words a voice may get wrong ("Levi-Civita" → "LEH-vee CHEE-vee-tah").
- **`prerequisites`**: direct prerequisites only, with `why` and `needed_for`. Use registry ids and never create
  cycles.
- **`leads_to`, `related`**: registry ids, each with a reason.
- **`key_equations`**: an id, name, rung and LaTeX, plus:
  - its meaning;
  - every symbol with its meaning and how to say it;
  - the `conditions` under which it holds;
  - `say_aloud`;
  - `justified_by`.
- **`derivations`**: one move per step, at a stated rung. If a step combines many terms, split it.
- **`worked_examples`**: an original problem, one move per step, the answer with units, and a takeaway. Foundation
  and core notes need at least one.
- **`problems`**: graded practice for self-study, with difficulty 1 to 3 and a type, up to three hints (gentlest
  first), an answer, and a full solution.
  - Prerequisite notes need at least 1 problem.
  - Foundation notes need at least 2, across at least two rungs.
  - Core, advanced and frontier notes need at least 3, across at least two rungs.
- **`observations`**: real measurements and phenomena that connect the concept to the world, with numbers and a
  verified reference. Mark thought experiments and analogues as such. Leave the list empty only when no honest
  connection exists.
- **`teaching_arc`**: 4 to 8 steps from a motivating question to a picture, formalism, check and transfer. Each step
  has a rung, a reason, the addresses it `uses`, an optional visual preset, and the prediction the learner is asked to
  make first.
- **`analogies`**: from a different setting than every way. If an analogy is the same scenario as a way, delete it.
  Give an explicit mapping and its limits.
- **`misconceptions`**: at most 8, each one real. `belief` is in the learner's words; also give `why_tempting`,
  `correction`, and `diagnosed_by` (check ids).
- **`checks`**: gradable, with at least one each at entry, working and formal.
  - Choose a `format`.
  - Give `question_spoken` whenever the question contains math.
  - `answer` is a chain of because-steps.
  - `key_points` are what a correct answer must contain.
  - Give `numeric` answers with a unit and tolerance.
  - Give hints and `targets`.
- **`notation_traps`**: variants readers will meet, in generic terms, with a `course_choice` from the conventions
  file.
- **`visuals`**: links to the visual catalog (section 10), each with this concept's priority. A proposal not yet in
  the catalog needs a `sketch`.
- **`tutor_moves`**:
  - opening questions that name their setting and invite a prediction;
  - if-stuck moves for symptoms that are not misconceptions (lost in notation, stalled, missing prerequisite);
  - common questions with rungs;
  - optional `voice_notes`, only for what the symbol `say` fields and `pronunciations` do not already cover;
  - structured `level_switching` signals.
- **`history`**: people, an integer year, the primary work as a reference (or null), and the contribution. State the
  scope precisely: what exactly was first, and in what setting.
- **`research_horizon`**: topic, a two-to-four-sentence connection, and references.
- **`provenance`**: the source units and legacy assets you drew on.
- **`status`, `revision`, `updated`**:
  - The writer sets `draft`, revision 1, and today's date.
  - The novice reviewer sets `novice-reviewed`.
  - The physics reviewer sets `physics-reviewed`.
  - Any learner-visible change after publication bumps the revision.

## 9. Length budgets

Budgets apply to parts, not only to the total. The entry rung is never cut to meet a budget; cut support fields first.

Word counts exclude reference metadata, ids and enum values.

| Part | Words |
| --- | --- |
| Entry way explanations (total) | 400–1,000 |
| Working way explanations (total) | 300–1,100 |
| Formal way explanations (total) | 250–1,000 |
| Research way explanations (total) | 0–700 |
| Other way fields: question, gist, recap, try_it, takeaway, retell, picture, simplifies | up to 1,300 |
| Equations, derivations, examples, problems, observations | up to 2,200 |
| Objectives, misconceptions, checks, teaching arc, tutor moves, analogies, glossary, traps | up to 3,300 |
| Links, visuals, history, research horizon | up to 1,000 |

The holonomy exemplar is a full core note at about 9,000 words. Only about 2,000 of those are teaching prose; the
rest are checks, problems, examples and tutor material. Prerequisite and foundation notes should stay under 7,000,
and every note under 10,000. Cut fields that repeat each other before cutting anything a learner will use.

## 10. Visuals: a network of pictures, and a contract for components

Diagrams, widgets, animations and 3D demos live in `knowledge/visuals/<id>.json`. One visual usually serves several
concepts. Visuals link to each other through `builds_on`, `leads_to` and `variant_of`.

- **Name visuals after the picture, not the concept:** `carry-an-arrow-around-a-loop`, not `holonomy-demo`. Search
  with `python3 knowledge/_tools/visual_ids.py --grep <word>` and reuse ids.
- **A proposal in a note** gives a `sketch`: what the learner sees, what they change, what updates, and what it
  proves. Contrast readouts only when they differ physically, not when they are one quantity on another branch.
- **A catalog entry is a component contract.**
  - `params` are typed, with options, ranges and defaults.
  - `presets` are named states.
  - `readouts` say when they are visible.
  - `tour` beats name a preset and any overrides, and give their `say` and `describe` lines in speech format.
  - `model.tests` give a state, the readout values expected, and tolerances. They compile into unit tests.
  - Every state used by the tour or by a note's `{id, preset}` must be a declared preset.
- **Rules for the parts of an entry:**
  - Design rules name the misconception they prevent.
  - A tour at entry rung obeys the novice contract.
  - `print_figure` describes the book figure.
  - `accessibility` gives a static alternative and keyboard control.
- **Figures from the books** inspire compositions; they are never reproduced.

## 11. Reviews

Each note passes two independent reviews before it counts as done. Each review records its findings in the note.

1. **Novice review.** The reviewer adopts the entry persona and reads only the fields section 2 marks for entry
   readers, sentence by sentence.
   - **Retell first.** Before fixing anything, write `retell_attempt`: what the persona would say back after one
     reading.
   - **Record every stumble** as a quote, the problem, and a rewrite:
     - every sentence reread;
     - every undefined word;
     - every step taken on trust;
     - every unreferenced direction;
     - every false first what-if.
   - **Fix and check the ladder.** Rewrite until the contract holds, then climb the ladder as a stronger student and
     add bridges wherever there is a jump.
   - **Sign off:** set `status: novice-reviewed`.
2. **Physics review.** The reviewer works as an adversarial referee.
   - Re-derive every equation, and recompute every number.
   - Work every check, example and problem.
   - Verify conventions, sense and branch, conditions, and analogies with signs.
   - Try the standard counterexamples.
   - Confirm every reference and set `verified`.
   - Check the novice reviewer's rewrites for accuracy.

   Fix errors while keeping the simplicity: an inaccurate simple sentence becomes an accurate simple sentence. Record
   `verification` and `counterexamples`, then set `status: physics-reviewed`.
