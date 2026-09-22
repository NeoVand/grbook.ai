# Vault build status and how to resume

Last updated 2026-09-22. Workflow scripts live in `knowledge/_workflows/` and run with the Workflow tool
(`scriptPath` plus `args`).

**Pacing rule:** one agent at a time near the usage limits, one workflow at a time; estimate the tokens
and get the owner's go before every run.

## Done

- **Phase 0 (source manifests):** reading copies and inventories.
- **Phase 1 (chapter dossiers):** 94 dossiers, all verified, plus book profiles and QA.
- **Legacy inventory:** 336 assets (`sources/legacy/`).
- **Concept registry:** 1,370 concepts in 24 domains (`concepts/<domain>/_registry.json`), with 0 check errors.
- **Course conventions:** `notation/course-conventions.md`.
- **Standard v2** (2026-09-13), which replaces the book-centred pilot notes:
  - writing guide `_meta/writing-guide.md`;
  - schemas `_schemas/concept-note.schema.json` and `_schemas/visual.schema.json`;
  - exemplars `concepts/curvature/holonomy.json` and `visuals/carry-an-arrow-around-a-loop.json`.

## Now

1. **Standard v2.** Two rounds of independent critique by four critics (a novice reader, a GR physicist, a book author
   and a tutor engineer) are done, and every fix is applied and committed. In the recheck, the author and the engineer
   judged the standard ready for a pilot. The novice reader's and physicist's remaining findings are fixed and
   numerically re-verified. The novice and physics reviewers are now running once over the holonomy exemplar
   (`review_only` mode), so the exemplar carries a real, filled review record.
2. **Mixed pilot: done, awaiting the owner's go before scaling.** Eight concepts across tiers and domains
   (`_meta/pilot-mixed-args.json`) ran through `gr-concept-notes-v2.js` in 87 minutes with 24 agents and no failures.
   - All 8 notes are physics-reviewed and validate OK. Registry prerequisites for their domains are synced.
   - Novice reviews logged 24–30 stumbles per note; physics reviews fixed 2–9 errors per note and verified every
     reference (4–19 per note).
   - `pilot_rubric.py` over the 8 notes plus holonomy: total length 86–95% of the tier cap (spread 4%); entry 99% and
     tutoring 100% of cap in every note; working 78% and formal 59% on average. Every objective is evidenced at its
     own rung.
   - Cost: 5.9 million subagent tokens, about 740 thousand per concept.
   - Convention gaps the writers reported are now rows in `notation/course-conventions.md`.
   - Open process issues: writers treat caps as targets; physics fixes change entry text after the novice review
     without a revision bump or re-read.
3. **Curvature: all 46 notes written and reviewed (2026-09-16).** Two runs: `notes-curvature`
   (`wf_72b3e7cb-34e`, stopped twice by usage limits, 351 agents) and `notes-curvature-finish`
   (`wf_aee171b5-d10`, 35 agents) which restarted each unfinished note at its own stage (`batch.start`).
   Every note validates; registry prerequisites synced; indexes rebuilt.
   - **Cost, measured both ways (output + new context + a tenth of cached reads):** old pipeline median 11.4M per
     concept, new pipeline mean 11.7M. The cuts did not pay off.
   - **Why:** cost tracks the NUMBER of tool calls, not bytes read, because every call re-reads the agent's whole
     context. The reading cuts (standard card, exemplar excerpt, note digests) worked on the review side (the merged
     post-review check costs about a third of the three stages it replaced), but the writer rule "fix with targeted
     edits, never rewrite the file" tripled writer calls from 66 to 184, and writers are over half the cost.
   - **Fixed for the next domain, not yet measured:** writers and reviewers now get an explicit call budget (about
     25 and 30), must batch numbers into one script and validator fixes into one pass, and write the note in one
     Write call. Expect this to matter more than anything else; measure it on the first domain that runs.
4. **Pivot to book sections (2026-09-16).** The owner rejected the per-concept vault as the unit of work: 1,370 notes
   would be 10.4M words, 13 times the three source books. The section is now the unit of writing
   (`book/outline.json`: 25 chapters, 164 sections, every concept placed once; `book/section-guide.md`;
   `_schemas/book-section.schema.json`; `validate.py section`; `render_section.py`; `_workflows/gr-book-sections.js`).
   The 53 concept notes stay as reviewed source material (`note_digest.py --ways`).
5. **Section pilot: done.** The 5 main-track sections of the curvature chapter (`sections-curvature-pilot`,
   `wf_8c66aab1-001`, 20 agents, 2.7 h, sequential so each builds on the last). All validate OK with both reviews.
   - Cost (output + new context + cached reads/10): **3.5M per section, 0.45M per concept**, against 11.4M per
     concept for notes. Writers made 44 calls (184 before). Whole book at this rate: about 0.6B, not 15B.
   - Reviews still catch real errors: a Möbius-band counterexample to "holonomy is a rotation", a false claim that
     no protractor reads a 22-arcsecond excess, a wrong term pairing in the Riemann symmetry argument.
   - Open before the next chapter: six entry concepts do not fit the entry prose cap (split the section or raise
     the cap); conventions rows for the sign of the second fundamental form, the torsion sign and the K symbol
     overload; "straight walk" as the entry word for geodesic; registry prerequisites that contradict the outline
     order (intrinsic-geometry, second-fundamental-form); angular-excess never proved at working depth.
6. **Curvature chapter: 7 of 7 sections done** (`sections-curvature-rest`, `wf_a3ebae42-ea6`). All validate OK.
   The open items the pilot flagged are fixed: conventions rows (extrinsic curvature, Frenet-Serret, the letter K,
   the tidal tensor, the entry word "straight walk"), entry sections raised to 3,000 prose words, three forward
   prerequisite edges removed, and the visuals workflow retargeted at sections.
7. **Curvature visuals: stopped by the monthly spend limit (2026-09-16),** run `wf_7fa26aba-f7b`. The planner merged
   58 proposals into 8 to write and folded 3 into the existing flagship; its full merge list and the remaining
   canonical ids are in the run output. State of the catalog (6 entries):
   - `two-walkers-set-off-side-by-side`, `card-touching-a-curved-patch`, `paper-rolled-into-a-tube-and-a-cone`:
     specified, both reviews at the current revision (the last two were signed off by the editor, not an agent).
   - `paced-ring-on-a-ball-and-a-plain`: novice-read, needs the physics review.
   - `four-legs-around-a-tiny-loop`: writer's draft, unreviewed, wording and symbol warnings cleaned by hand.
   - `falling-ring-of-crumbs`, `six-entry-curvature-table`, `twenty-of-256-slots`: not written.
   Resume with `gr-visuals-v2.js` (it re-plans from the proposals) once budget allows.
8. **The app serves the book (2026-09-22).** `scripts/build-book-index.ts` compiles the outline, the written
   sections and the visual catalog into `src/lib/server/vault/generated/book.json`, dropping provenance, reviews and
   sketches (`src/lib/server/book.spec.ts` fails if any of that, or a book name, reaches the runtime). Routes:
   `/read` (all 25 chapters) and `/read/<chapter>/<section>` (the reading view, KaTeX rendered server-side). The
   theme moved to paper-and-ink with Literata, Newsreader and IBM Plex Mono.
9. **First demo built.** `two-walkers-set-off-side-by-side` is now a three.js component
   (`src/lib/visuals/two-walkers/`), status `built` in the catalog. Its model is a separate module, and
   `model.spec.ts` runs all 20 numerical tests from the catalog entry against it, so the book's promises test the
   code. Building it found one real bug the spec had anticipated: at a ball's pole the gap is 6e-17 rather than 0,
   so the extra-per-stretch readout divided by it; spheres now use the closed form.
   Lesson: a spec of this shape is buildable without its author present, and the tests are worth the trouble.
10. **Two agents a section (2026-09-22).** The owner chose the cheaper pipeline. `gr-book-sections.js` is now a
   writer plus one reviewer that applies the reader lens, then the adversarial physics lens, then re-reads its own
   physics fixes as the reader. That last step is what the separate post-review check used to do; inside one agent
   the gap it closed never opens. The reader pass now also covers formal and research depth (a graduate reader who
   knows no notation the book has not introduced), which the four-stage pipeline skipped. `start` is now
   `write` | `review`.
11. **Chapter 1 written: Measurement, mechanics and Newtonian gravity** (`sections-mechanics-and-gravity`,
   `wf_a43f104d-a91`, 12 agents, 2.8 h, sequential, no failures). All 6 sections validate OK at
   `physics-reviewed`; 13 of 164 sections are written (34,205 words).
   - **Cost: 2.15M per section** (output + new context + cached reads/10), against 3.5M with four agents: a 39%
     cut, and better than the 2.5M estimate. Writers 15-22 calls (~0.7M), reviewers 29-50 calls (~1.4M).
   - The review still earns its place. In `rotating-frames` alone it caught a ball rolled across a turntable
     described as going straight in the ground frame (contact friction curves it), a centrifugal force defined by
     the body's own ground speed rather than the frame's rotation, a rider told to add Coriolis but not
     centrifugal, and a jet's clock claimed to fall behind when the altitude term is three times larger and of the
     opposite sign. `newtonian-gravity-as-a-field` had the potential defined as a positive climb-out energy and
     then called negative in four places.
   - **Blocking before the next mechanics or orbits section: `notation/course-conventions.md` fixes nothing for
     elementary mechanics, analytical mechanics or Newtonian orbits.** Six sections each had to invent their own:
     p = m v, F = m a, U against the field potential Phi, whether vectors are bold, joules and newtons at entry
     depth, q^a colliding with the file's Latin i,j for space, overdot, L = T - V, p_a, the signed forms of
     Gauss's law and Poisson's equation, a value for G, the gravitational field symbol g colliding with the metric
     and with surface gravity, and the orbit symbol set (mu, M, a against the scale factor, e, l, v_esc).
   - Outline fixes the writers and reviewers both asked for: `heaviside-lorentz-units` and `natural-units` cannot
     be graded in `units-and-dimensions` (move to `maxwells-equations` and `the-planck-scale-and-quantum-fields`);
     `geometrized-units` needs G three sections before `newtonian-gravity-as-a-field` teaches it;
     `absolute-space` argues where the rest of `newtons-laws-and-inertial-frames` measures, and belongs in
     `rotating-frames` with Mach; `conservative-force` and `conservation-of-mechanical-energy` belong with the
     Lagrangian section; `hamilton-jacobi-equation` is taught as a preview; `negative-specific-heat` fits a
     stellar-structure section better than `kepler-orbits`.
   - `validate.py` UNITS lacks `kg m^2/s`, `J s` and `m^2/s`, so a conserved-angular-momentum check could not
     carry its real numeric answer.
   - 13 visuals were proposed with sketches and none is in the catalog yet.
12. **Next.** Chapters in reading order (Part 0 toolkit or Part II `space-and-time` next), main track first;
   visuals per chapter after its sections. The remaining curvature visuals (6 partly reviewed, 3 unwritten) are
   listed above. Do the conventions rows in item 11 before writing another mechanics or orbits section.

## App follow-ups from the engineer critique

These are not started; do them after the standard settles.

- **Tutor tools** move from book units to vault addresses: `get_concept(id, rung, parts)`, `get_item(address)`,
  `get_next_steps`, `find_misconception`, `open_visual`, `set_visual_state` and `play_tour_beat`.
- **Learner evidence** keys on addresses and records rung, outcome and content revision. `conceptState` is keyed by
  (user, concept, rung).
- **The vault compiler** strips `provenance`, `starting_material` and review concerns. A build test fails if any
  book id reaches runtime JSON.
- **Reader pages** move from book units to concepts and lessons.

## Resume

1. **Write the notes for a domain.**
   - Run `python3 knowledge/_tools/make_note_batches.py --domain <id>`. It prints a summary line, then one args object
     with one concept per batch; `after` lists the in-domain prerequisites whose novice review a batch waits for.
   - Run `knowledge/_workflows/gr-concept-notes-v2.js` with that args object plus `date` and `snap_dir` (a scratch
     directory outside the repository). Each concept goes through a writer, a novice-reader review and a physics
     review. When the physics review changes entry or working text, one post-review check reads those changes with
     the novice lens, then the physics lens, and signs both stages.
   - Agents read `_meta/standard-card.md` and `_meta/exemplar-excerpt.json` (regenerate with
     `make_exemplar_excerpt.py` when holonomy changes), use `note_digest.py` for other notes, and never read source
     chapters or notes in full. Measured on curvature: writers cost more than the three review stages together, so
     these reading rules are the main saving; `gr-visuals-v2.js` still uses the older three-stage re-check.
   - `mode: "conform"` with `base_rev` brings already reviewed notes up to a changed standard (a conform edit where
     `conform` is true, a full entry re-read, and a diff check of everything changed since `base_rev`).
   - Re-run both commands until the summary says 0 pending. `lagging_novice` in the result lists notes whose final
     physics fix changed text after the last re-read; an editor reads those sentences.
2. **Build the domain's visuals.** Run `knowledge/_workflows/gr-visuals-v2.js` with
   `{"domain": "<id>", "date": "<today>", "snap_dir": "<scratch dir>"}`. It plans canonical ids, then takes each
   visual through a writer, a novice reading of its tours and speech, and a physics review that recomputes every test.
   Changed speech gets a re-read, and a changed re-read gets a diff check, as for notes. Reviewed entries become
   `specified`.
3. **Sync and check.** Run these commands in order:
   - `python3 knowledge/_tools/sync_registry.py --domain <id> --write`
   - `python3 knowledge/_tools/check_registry.py`
   - `python3 knowledge/_tools/render_concept.py --indexes`
   - `python3 knowledge/_tools/render_visual.py --index`
4. **Commit and push** to main.

## Later phases

These are not scripted yet:

- curriculum: learning paths and modules over the prerequisite DAG, at several entry levels;
- tutor indices and retrieval functions over concepts and visuals;
- a completeness review;
- an app pivot from book-unit pages to concept and lesson pages.
