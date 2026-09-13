# Legacy project overview: *General Relativity, From the Inside Out*

> **Vault editor note (2026-09-12).** Two porting recommendations below predate the grbook.ai stack decisions.
> (1) GPT-Live (`gpt-live-1`) has no ephemeral client secret: a SvelteKit route forwards the browser's WebRTC offer
> using the user's key once, and function calls arrive on the data channel and run through our endpoints (see
> `docs/research/openai-live-voice-and-elevenlabs.md` §8). Read "mint an ephemeral secret" in §4.5 accordingly; the
> tool-scheduler lesson still applies but its event names change. (2) The grbook.ai template uses Drizzle with
> libsql/SQLite, not Postgres; "Postgres full-text plus pgvector" in §4.5 is a placeholder until the storage and
> retrieval design is settled.

Start here if you are planning grbook.ai and want to know what the old project
(`/Users/neo/repos/general-relativity`) can give us. This page summarises the nine inventory groups in this folder.
Every asset has an id in one of these files, and the id is the cross-reference key:

| Group file | Assets | Covers |
| --- | --- | --- |
| `manuscript-part1.json` | 36 | book.md Ch 0-8 (measurement, SR, tensors, manifolds, connection, curvature) |
| `manuscript-part2.json` | 45 | Ch 9-16 (Ricci/Weyl, tides, stress-energy, field equation, actions, symmetry, tests) |
| `manuscript-part3.json` | 41 | Ch 17-24 plus Appendices A-E (black holes, waves, cosmology, ADM, forms, thermodynamics, EFT, synthesis) |
| `lessons-and-curriculum.json` | 52 | 37 guided lessons, practice sets, skill map, routes, lesson template |
| `labs-geometry.json` | 20 | Geometry Labs 01-05, manifold/precession/Riemann-count/tidal-cloud labs, older "visual arguments", lab contract |
| `labs-physics.json` | 31 | Mechanics, matter, relativity calculators, nine three.js scenes, lab records, curvature checker |
| `figures-and-media.json` | 56 | 40 SVG figures, history images, Earth texture, figure pipeline and reviews |
| `reader-ai-audio.json` | 27 | Study companion, Realtime voice, ElevenLabs narration, highlighting, grounding, search |
| `reviews-and-plans.json` | 28 | Audits, visual curriculum plan, design system, backlog specs, tutor evaluation design |

Paths inside the JSON files are relative to the legacy repo. **The legacy project is the user's own work.** The
vault's "learn how to teach, never copy" rule covers third-party textbooks and does not apply here. Legacy prose,
code and figures may be reused verbatim. We still cite the asset id so provenance stays traceable.

**Duplicate ids to resolve on import.**
- `lesson-contract-curvature-by-hand`, `lesson-what-a-tidal-instrument-measures`, `lesson-fields-carry-energy`,
  `lesson-poisson-from-a-flux`, `lesson-variations-and-boundary-data`, `lesson-boundary-action-is-part-of-the-question`,
  `lesson-symmetry-earns-a-charge`, `lesson-orbit-conservation` and `lesson-phase-drift` appear in both
  `lessons-and-curriculum` and `manuscript-part2`. The two groups sometimes give different verdicts. Treat
  `lessons-and-curriculum` as canonical. Read a disagreement as "keep the text as it is, then add the demo or move
  the placement".
- `lab-legacy-gps-orbiting-clock-slider` (manuscript-part2) is the same code as `lab-gps-clock-rates` (labs-physics,
  canonical).
- `design-doc-experience-ideas` appears in labs-physics and reviews-and-plans. The reviews-and-plans entry is
  canonical.
- `scene-3d-tidal-cloud` (labs-physics) and `lab-tidal-cloud-geodesic-deviation` (labs-geometry) are two different
  implementations of one idea. Merge them into one demo.

---

## 1. What the project was, and where it stands

**What it was.** A self-contained graduate-ambition GR course for a reader who knows only calculus and linear
algebra. It was built between 8 and 12 September 2026. It has:

- **A manuscript** (`book.md`): 25 chapters plus five appendices, about 78,000 words and roughly 760 display
  equations. It runs from a cart on a track (Ch 0) to EFT (Ch 23) and a synthesis (Ch 24).
- **A guided-lesson layer**: 37 lessons with 128 derivation steps, each with a stated reason. They carry 37
  predict-then-feedback checks with 111 per-option rationales and 74 numeric transfer and variant problems.
- **A 25-chapter prerequisite graph, three routes and a 30-skill readiness map.**
- **About 35 interactive experiences** (2D SVG labs and three.js scenes), each built on a pure, independently
  tested physics model.
- **40 computed SVG figures.**
- **A bring-your-own-key AI study companion**: OpenAI Realtime voice that consults a text tutor, and ElevenLabs
  narration with word highlighting and generated spoken explanations of equations.

**Teaching philosophy** (consistent and worth inheriting):
1. **Measurement before formalism.** Every coordinate is tied to a clock, ruler, accelerometer or light procedure.
   Each tensor block is presented as something a detector measures.
2. **Object, components and measurement are kept separate.** Coordinate artefacts are never read as physics.
3. **A recurring flat-space counterexample thread**: the polar plane (4.2, 4.5, 6.1, 7.5, 8.4), Rindler (5.3, 24.2)
   and the cut cone (8.3). Each shows nonzero Christoffels, clock-rate differences or coordinate acceleration with
   zero curvature.
4. **Derive, don't announce, and check every derivation with a number.** About 30 worked numbers in Ch 0-8 and
   every number in Ch 9-16 were re-derived during the inventory. None was wrong.
5. **Honest status labels**: "a preview, not a derivation", "counting components is not counting modes", "imported
   quantum input", "listening is not mastery".
6. **Model-plus-limits for every visual.** Each demo and figure states its model, what is exaggerated and what it
   does not show.

**Honest assessment of the current state.**
- **Science: excellent and nearly fault-free.** Sign conventions are fixed and checked operationally (R = 2/a² on the
  sphere). `scripts/check-physics-calculations.mjs` independently verifies the high-risk results (Kerr, pp-wave,
  weak-field Φ/Ψ, FLRW, ADM). The reviews found and fixed real errors (F02 symbol collision, trace-zero
  "compression", null plane-wave coordinate).
- **Novice pedagogy: uneven.** The prose is dense and derivation-first, with a high caveat rate (up to 12 negations
  per 1,000 words in Ch 10). Visuals arrive late (Ch 21's first visual comes after 38 equations). Practice is thin
  and sits apart from the teaching (Appendix A, one guide check per chapter). A real reader complaint exposed a
  Chapter 0 that assumed metrics. It was repaired, but only Ch 0-1 got a full first-use audit. **No learner was ever
  observed.**
- **Labs: the physics kernels and tests are first rate; the interfaces are inconsistent.** There are four UI shells,
  two maths-labelling systems and duplicated older lessons. Several 3D scenes are "orderly but not explanatory"
  (embedding, lapse/shift, expansion). Some lab defaults hide the key result (star maximum mass, D_A turnover).
- **AI and audio: strong protocols, never evaluated live.** Every provider test mocks fetch and WebRTC. Tutor
  accuracy, spoken-maths fidelity, latency and cost were never measured.
- **Architecture: a dead end.** Static HTML is generated by string-templating scripts. Labs are imperative DOM
  modules. The SvelteKit rebuild (`app/`, commit 6f6384c) is unhosted and wraps a 33.7 MB `pages.json` plus the
  legacy runtime. It silently dropped the GPS and twin widgets and several tested voice behaviours. **Port content,
  models, tests and protocols. Do not port shells or pipelines.**

---

## 2. Top assets to carry forward (ranked)

The ranking weighs teaching value, quality, how cheap the port is, and fit with grbook.ai's AI-centred, demo-led
design. "Companions" are assets that should travel with the primary id.

| # | Asset id (group) | Verdict | Why it matters | Adaptation needed |
| --- | --- | --- | --- | --- |
| 1 | `scene-3d-parallel-transport-loop` + `scene-3d-parallel-transport-two-routes` (labs-geometry) | adapt | The gold-standard demo. It uses exact Levi-Civita transport on plane, cylinder and sphere, checked against RK4 to 4e-10, and shows holonomy equal to K times area and path dependence. The rendering is beautiful and robust (shader grid, orthographic fixed frustum, face-on view). | Port `parallel-transport-model.js` and its check verbatim to TS. Make one Svelte/Threlte lab with "loop" and "two routes" modes. Add a shaded signed area with an orientation arrow, an unrolled-cylinder inset, a second vector (inner product preserved), a noncontractible cylinder loop and an angle/area → 1/R² plot. Show the signed angle consistently (fix the `Math.abs` label). Companions: `lesson-carry-a-direction-without-turning-it`, `manuscript-section-8-3-sphere-holonomy-area-and-cone`, `figure-cartan-comparison` (tangent-plane inset technique). |
| 2 | `engine-lab-state-narration-qa-contract` (labs-geometry) + `engine-experiment-tutor-context-contract` (labs-physics) | adapt | Labs publish `scientificContext` (model, parameters, readouts, units, assumptions, equations) and a live narration sentence. This is exactly the grounding a GPT-Live tutor and the narrator need, without vision or DOM scraping. | Define a typed `LabContract<State>`: Zod state schema, `describe(state)`, `scientificContext(state)`, concept ids, and **validated, undoable tutor commands** (`setParameter`, `highlight`, `playCue`). Emit only committed state, never hover. Make persistence and lifecycle platform features rather than something each lab opts into. |
| 3 | `engine-or-tool-voice-tool-scheduler` (reader-ai-audio) | reuse-as-is | Encodes the key Realtime fact that `response.done` does not mean playback has finished. It queues tool calls until `output_audio_buffer.stopped`, drops stale turns and treats `cleared` as cancel. About 60 lines, with a thorough passing test. | Port to TS unchanged. Port `scripts/check-voice-tools.mjs` to Vitest. Re-check event names against current GPT-Live docs. Keep `create_response:false`, or stamp every response. |
| 4 | `engine-lab-records-and-relativity-lab-shell` (labs-physics): `relativity-models.js` + `lab-records.js` | adapt | A declarative lab record (question, prediction, units, assumptions, equations, limitation, source, parameter ranges) drives controls, disclosure, tutor context and CSV provenance. The four kernels (TOV, photon exchange, FLRW distances, dust evolution) have CI analytic checks. | Adopt the record as a TS type and add `conceptIds`, `tutorCommands` and `predictions[]` with expected answers. Port the models and `check-relativity-models.mjs` verbatim. Replace the generic chart, whose hard-coded axes hide features, with per-lab views. Render the prediction as a real interaction. |
| 5 | `engine-independent-curvature-checker` (labs-physics) | adapt | A finite-difference Christoffel/Riemann/Ricci/Kretschmann/G checker for any 4D metric. It catches sign and convention errors that hand derivations miss. | Extract `curvature(metric, point)` into a TS verification package. Run it in CI against every metric, symbol and invariant quoted in the vault and lessons. Expose it as a "compute curvature of this metric" tutor tool with a disclosed tolerance. |
| 6 | Manuscript derivation layers: `manuscript-chapter-12-einstein-field-equation`, `manuscript-section-7-5-five-polar-plane-experiments`, `manuscript-section-5-3-rindler-accelerating-laboratory`, `manuscript-section-5-4-5-5-geodesic-equation-from-action`, `manuscript-section-17-1-schwarzschild-derivation`, `manuscript-section-18-5-quadrupole-chirp`, `manuscript-section-19-1-friedmann-derivation` | reuse-as-is | The most reusable text in the book: complete, verified derivations with stated assumptions, rarely matched in introductory texts (the 1/5 angular average, the Φ and Ψ calibration, GHY cancellation). | Import as the "derive" depth layer and as tutor grounding, not as the first screen. Put a predict or compute prompt in front of each worked step (7.5 especially). Strip build links and `data-*-insert` placeholders. Encode every number as a unit test. |
| 7 | `lab-particle-stress-energy-crossings` (labs-physics) | adapt | The best pedagogy in the labs. T^{μν} is built by counting detector crossings, and "pressure with zero mean flow" is the headline surprise. Verified exhaustively. | Keep the model, check, row/column framing, insight rules and disclosures. Rebuild in Threlte with instanced particles and a movable probe box. Add a guided density → pressure → shear sequence, **a boosted-observer step that Lorentz-transforms the tensor**, and a photon-gas preset reaching p = ε/3. Companions: `manuscript-section-11-stress-energy-measurement-and-observers`, `design-doc-fluid-stress-energy-lab-spec`, `lab-fluid-viscous-shear` (optional enrichment). |
| 8 | `lab-vector-field-two-arrows` (labs-geometry) | adapt | The sharpest covariant-derivative intuition: constant components with a changing arrow, and the reverse. The exact finite product rule is drawn head to tail. | Make the component + frame decomposition always visible. Enlarge the field view. Use KaTeX hatted labels. Add a unit/coordinate basis toggle (∂θ = r ê_θ), a Δθ → 0 readout, tracer markers and a divergence flux box. Absorb the `(0,−1)+(0,1)=0` identity from `lab-visual-lesson-rotating-polar-basis` (dropped). Companions: `manuscript-section-6-1-fixed-arrow-changing-components`, `lesson-differentiate-the-arrow-not-its-address`. |
| 9 | `lab-polar-coordinates-two-addresses` + `lab-visual-lesson-polar-metric-cell` (labs-geometry) | adapt | Opens the polar-plane thread that runs through Ch 4-8. Arc versus chord, the angle undefined at the origin, and the tangent prediction versus the exact endpoint distance. | Merge into one polar lab with three views (addresses, angular step, metric cell). Use continuous sliders plus a log "shrink" control. Add a basis toggle, a ds² overlay and a coordinate-rectangle → area (determinant) mode. Companions: `manuscript-section-4-4-4-7-metric-inverse-volume`, `lesson-a-metric-converts-labels-into-lengths`. |
| 10 | `manuscript-section-10-geodesic-deviation-newtonian-tides` + `lab-tidal-cloud-geodesic-deviation` + `scene-3d-tidal-cloud` | reuse text / adapt labs | Curvature becomes something you measure. The exact Jacobi solutions show that zero initial volume acceleration does not mean constant volume (Ricci versus Weyl). Earth tide numbers are verified. | One Threlte cloud demo with a few thousand instanced particles and a translucent ellipsoid. Offer a "point mass at r" preset in SI units, a Ricci (matter) slider added to the Weyl part, a Raychaudhuri readout and Earth / neutron-star / stellar-BH presets. Teach tides **before** Ricci/Weyl. Companions: `lesson-what-a-tidal-instrument-measures`, `lesson-contract-curvature-by-hand`, `manuscript-section-09-ricci-volume-weyl-shape`. |
| 11 | `practice-set-misconception-checks` (lessons) + `design-doc-misconception-diagnostics` (reviews) | adapt / reuse-as-is | 111 mistake-specific rationales plus 12 misconceptions each turned into an operational diagnostic task, including the lapse-metric N(z) transfer task. This is a ready-made misconception catalogue and tutor-eval seed. | Key each item to concept ids. Give choices authored stable ids and shuffle per learner. Have the tutor ask *why* a chosen distractor fails. Author full solutions and distractors for the 12 diagnostic tasks. |
| 12 | `review-doc-reference-comparison` + the SCIENCE bullets of `reviews-and-plans` | adapt | Ten precise GR errors deliberately not imported from a reference text, plus errors found in the sentence-level pass. These become tutor guardrails and a "common errors" note. | Copy almost verbatim into a vault pitfalls note attached to concepts (§5.1 below). Use as adversarial tutor-eval prompts. |
| 13 | `design-doc-visual-development-plan` (+ `design-doc-geometry-sequence-spec`, `design-doc-action-study`) | adapt | The visual design contract. It gives the six-step pattern (observe, predict, try, compare, name and calculate, transfer), the 2D-versus-3D rule, a required-anchor table, release gates, the AI state architecture and buildable specs for A-C (shipped), the fluid lab (partial), action, the lens (F) and the black-hole sky (G). | Make it the seed of grbook.ai's demo spec template and acceptance checklist. Remap the chapter coverage map to concept ids. Use the F, G and action specs as build briefs (§6). |
| 14 | `engine-or-tool-math-narration-script-generation` + `engine-or-tool-spoken-word-highlighting` + `engine-or-tool-narration-audio-player` (reader-ai-audio) | adapt / reuse-as-is / adapt | Never speaks raw TeX. It generates spoken explanations under word budgets (equations 20-55, figures 25-50), rejects TeX in output, highlights words via the CSS Custom Highlight API (no span injection), and gives gapless batched ElevenLabs playback with a bounded prebuffer. | Generate and review scripts **at authoring time**, stored with provenance (generated, reviewed or authored). Cache audio server-side, shared across users for authored content. Store `content_hash` and `context_hash` separately. Copy `highlight.ts` and `wordAt`/`captionTokens` unchanged. Preserve pitch when speed changes. |
| 15 | `scene-3d-mercury-perihelion-precession` (labs-geometry) + `lesson-phase-drift` + `lesson-orbit-conservation` | adapt | The best applied demo. Kepler timing plus the leading advance, with an explicit "reveal ×300,000" magnification that separates exaggeration from physics (43″/century verified). | Port the constants, `perihelionAdvance` and the actual-versus-reveal framing to the shared shell with scientific context. Add continuous log magnification, a truncated-φ sin φ versus phase-shift overlay, and a Schwarzschild orbit-equation integrator mode so the same lab serves the black-hole orbits unit. |
| 16 | `lesson-horizon-directions` + `manuscript-section-17-3-horizon-coordinates-and-observers` + `lab-visual-lesson-horizon-light-cones` + `review-doc-causality-and-horizon-visual-contract` | reuse-as-is / adapt | Conceptually exact horizon teaching in regular EF coordinates with no escape-speed story. It includes a precise visual contract (τ_plot is not proper time, equal scales, slopes −1 and (ρ−1)/(ρ+1)). | Rebuild as an interactive EF cone field. Make ρ draggable, integrate null curves, add an infalling worldline with proper time, and toggle to Schwarzschild t to show the chart failure. Adopt the visual contract as acceptance criteria. |
| 17 | `lab-stellar-structure-tov` + `manuscript-section-17-8-tov-star` | adapt | A real relativistic calculation (TOV in log-enthalpy, RK4) checked against Lane-Emden in CI, with exceptionally honest EOS and stability text. | Redesign around the family. Show a live M-R and M(ρ_c) curve with the turning point (M_max = 0.1637 at ρ_c ≈ 0.32) and the stability caveat. Add a physical-units toggle and a Newtonian ghost star. Move step size under "audit numerics". Show the lapse through the surface into Schwarzschild. |
| 18 | `lab-cosmological-distances` + `lesson-distances-are-measurement-protocols` + `lab-numerical-flrw-evolution-audit` + `lesson-evolve-and-check-the-constraint` | adapt / reuse-as-is | Correct analytic-benchmarked FLRW distances with curvature. The rare "audit your simulation" lab asserts RK4 convergence order and monitors the constraint. | Distances: give D_A its own panel or log axis so the turnover shows. Define critical density, Ω and E(z) in the prose first. Add presets, an Ω_m-Ω_Λ allowed-region map and a supernova overlay. Evolution: auto-scale the axes, add a log-log error-versus-h plot, and add Λ/curvature (recollapse). |
| 19 | `curriculum-lesson-template` + `lesson-*` geometry set (`lesson-coordinates-change-measurements-do-not`, `lesson-measure-curvature-with-a-string`, `lesson-contract-curvature-by-hand`, `lesson-a-curved-universe-capstone`) | adapt / reuse-as-is | A consistent lesson record: question, intuition, steps each with a stated reason, formal limits, predict-check with per-option feedback, transfer, variant, takeaway. All answers are hand-verified. | Turn it into a Zod lesson schema, one file per lesson. Replace `requires` hrefs with concept ids. Add authored choice ids, claim-level citations and a **required intermediate answer** so the method is assessed. Split practice pools by role: diagnostic, in-lesson transfer and review. |
| 20 | `scene-3d-earth-free-fall-flow` (labs-physics) + `figure-earth-blue-marble-texture` | adapt / reuse-as-is | The legacy project's most striking visual: a GPU-advected falling grid on a real Earth (the rain congruence). A natural hero or opening scene. | Keep the GLSL kinematics, texture and credits (NASA, ScienceClic, Hamilton-Lisle). Thin the grid. Mark one radial pair and one transverse pair with live separation readouts so "compare two falling objects" is true. Add a release-from-rest-at-finite-radius toggle. Reuse the same flow for the black-hole river model later. |
| 21 | `lab-flow-order-lie-bracket` + `manuscript-section-6-6-lie-bracket-flow-order` | adapt / reuse-as-is | Teaches [X,Y] operationally (h² gap) before torsion, fixing a real prerequisite leak. It guards against "noncommuting implies curvature". | Compute the gap/h² ratio instead of the hard-coded "1.0000". Add a second field pair where higher-order terms show, a four-leg XYX⁻¹Y⁻¹ loop mode and a polar frame-bracket comparison. |
| 22 | `lab-riemann-independent-components` (labs-geometry) | adapt | Turns 256 → 36 → 21 → 20 into a tactile three-phase argument, verified exhaustively. | Commit on click, not hover. Renumber symbols contiguously and fix the a/b colour mapping. Add a dimension selector (2, 3, 4 → 1, 6, 20). Drop `figure-curvature-count`. |
| 23 | `engine-math-colour-palette` + `design-doc-design-system` | reuse-as-is / adapt | Five semantic colour roles (geometry teal, transport blue, curvature violet, matter amber, observer rose), with light and dark hex pairs and a restrained "colour the object, never the index" philosophy. | Copy as design tokens. Add separate 3D surface and material tokens (the dark-theme wash-out bug) and a CI contrast check. Replace the regex role guessing with authored KaTeX macros keyed to concept ids (§4). |
| 24 | `manuscript-chapter-16-clocks-light-mercury` (sections 16.1-16.5, 16.7-16.8) + `figure-gps-clocks` + `figure-tossed-clock` | reuse-as-is / adapt | The template for applied units: observer + worldline + approximation leads to a number with units and a cited experiment. All numbers are verified (1.75″, 119 μs, GPS +45.7/−7.2/+38.5 μs/day, 44.6 as). | Replace `lab-gps-clock-rates` and the GPS figure with one clock-budget demo (separate curves, Earth rotation toggle, ranging scale). Make the tossed clock and light bending interactive. Derive the Schwarzschild orbit equation before 16.6. |
| 25 | `historical-image-*` (4) + provenance manifests; `manuscript-section-1-9-history-note` | reuse-as-is | Public-domain portraits and title pages with exemplary manifests (source, licence rationale, modifications, sha256, verified date), plus a careful, myth-free history narrative. | Copy files and manifest entries. Generate WebP/AVIF derivatives. Adopt the manifest schema for every grbook.ai image, texture and video. Re-verify the Commons status of the 1921 Einstein photo at import. |

Next tier, all worth keeping: `manuscript-section-1-1-falling-scale-and-two-ball-tides` (first voice dialogue
script), `manuscript-section-2-1-2-4-basis-change-and-covector-pairing`,
`manuscript-section-3-3-3-5-interval-proper-time-twin`, `manuscript-section-11-radiation-pressure-mass-of-a-box`,
`manuscript-section-10-curvature-invariants-and-summary-table` (the 10.8 "what each object answers" card),
`lab-photon-redshift-observers`, `scene-3d-gravitational-wave-rings`, `lesson-boundary-action-is-part-of-the-question`,
`manuscript-section-24-3-calculation-checklist` (tutor "interpret a metric" protocol),
`practice-set-appendix-a-thirty-exercises`, `design-doc-ai-tutor-evaluation-and-state`,
`engine-learning-state-notebook`, `engine-or-tool-reading-context-extraction`.

---

## 3. Topic reuse matrix

The verdict follows each id: **R** reuse-as-is, **A** adapt, **I** reimagine, **ref** reference-only,
**D** drop. The "Missing" column lists what no legacy asset covers usably.

| GR topic | Best legacy assets | Missing (no usable asset) |
| --- | --- | --- |
| **Prerequisites and measurement** | `manuscript-section-0-1-derivative-as-local-prediction` R; `manuscript-chapter-00-measurements-and-motion` A; `lab-spring-energy-exchange` A; `lab-hamiltonian-phase-space` A; `lesson-initial-data-and-oscillations` A; `lesson-mechanics-energy-and-pressure` A; `lesson-measurements-and-units` A; `lesson-poisson-from-a-flux` A; `figure-local-prediction` A; `figure-metric-volume` A; `manuscript-section-0-9-entry-checks` I; `practice-set-readiness-diagnostics` I; `design-doc-curriculum-gaps-and-prerequisite-bridges` A | A real adaptive diagnostic; vector calculus on fields; waves and complex notation as a primer (partly in `lesson-waves-and-retarded-time`); an EM primer (only compressed in `lesson-fields-carry-energy`); probability and quantum primers (`lesson-probability-temperature-and-entropy` and `lesson-quantum-states-and-reduced-information` are ref only) |
| **Special relativity** | `manuscript-chapter-03-special-relativity` A; `manuscript-section-3-2-lorentz-transformation-derivation` R; `manuscript-section-3-3-3-5-interval-proper-time-twin` R; `manuscript-section-3-7-observer-measured-energy` A; `lesson-hyperbolas-and-rapidity` A; `lesson-doppler-is-an-observer-measurement` A; `scene-3d-light-cone` A; `figure-light-cone` A; `figure-twin-worldlines` A; `lab-twin-paradox-clocks` I | **Clock-and-radar lab** (synchronisation, simultaneity, Doppler); draggable Minkowski diagram with boosts; relativistic collision practice; worked hyperbolic motion in 3.8 |
| **Vectors, covectors, tensors** | `manuscript-section-2-1-2-4-basis-change-and-covector-pairing` R; `manuscript-section-2-5-2-6-tensors-index-grammar-approximations` A; `lesson-coordinates-change-measurements-do-not` R; `scene-3d-covector-level-planes` A; `figure-vector-covector` A; `practice-set-appendix-e-index-practice` A (E.1 checklist) | Generated index-grammar drills or a "lint my expression" checker; nonorthogonal-basis and negative-pairing demo; wedge-product/oriented-area explorer |
| **Manifolds and metrics** | `manuscript-section-4-4-4-7-metric-inverse-volume` R; `manuscript-chapter-04-manifolds-metrics` A; `manuscript-section-4-1-two-chart-sphere-atlas` A; `lab-polar-coordinates-two-addresses` A; `lab-visual-lesson-polar-metric-cell` A (merge); `lesson-a-metric-converts-labels-into-lengths` A; `lesson-two-maps-one-sphere` A; `lesson-dimensions-before-symbols` A; `scene-3d-manifold-surface-charts` I; `scene-3d-visual-lesson-stereographic-charts` I; `figure-polar-metric` I | One atlas lab with genuinely nonlinear charts and a live transition Jacobian; volume-element or determinant demo; locally inertial coordinates construction (4.8 only asserts it); geometrised-units card (c = G = 1) |
| **Connection and parallel transport** | `manuscript-section-6-1-fixed-arrow-changing-components` R; `manuscript-section-6-6-lie-bracket-flow-order` R; `manuscript-section-7-3-christoffel-derivation` R; `manuscript-section-7-5-five-polar-plane-experiments` R; `manuscript-chapter-06-covariant-differentiation` A; `manuscript-chapter-07-connection-parallel-transport` A; `manuscript-section-7-4-connection-transformation-law` A; `lab-vector-field-two-arrows` A; `lab-flow-order-lie-bracket` A; `scene-3d-parallel-transport-loop` A; `lesson-differentiate-the-arrow-not-its-address` A; `lesson-flows-that-do-not-commute` A; `manuscript-section-15-maps-pullbacks-lie-derivative` A; `figure-connection-cancellation` A (as KaTeX); `lab-visual-lesson-rotating-polar-basis` D; `scene-3d-visual-lesson-octant-transport-steps` D; `scene-3d-sphere-holonomy` ref | Lie-derivative flow-dragging demo; limit P(γ(h)→p)V − V → ∇_X V visual; Fermi-Walker transport; learner-completed mixed-tensor derivative practice |
| **Curvature** | `manuscript-section-8-3-sphere-holonomy-area-and-cone` R (make core); `manuscript-section-8-4-8-6-flatness-count-sphere-curvature` R; `manuscript-chapter-08-curvature-holonomy` A; `manuscript-section-8-1-8-3-riemann-commutator-and-loop` A; `scene-3d-parallel-transport-two-routes` A; `lab-riemann-independent-components` A; `lesson-carry-a-direction-without-turning-it` R; `lesson-measure-curvature-with-a-string` R; `lesson-contract-curvature-by-hand` R; `manuscript-section-09-ricci-volume-weyl-shape` R; `manuscript-section-09-bianchi-einstein-tensor` A; `manuscript-section-10-curvature-invariants-and-summary-table` R; `figure-cartan-comparison` A; `practice-set-21-8-surface-of-revolution` R; `figure-ricci-weyl` D; `figure-curvature-count` I | Shrinking-loop angle/area → K convergence; string-circle demo on sphere, cylinder and saddle; R(X,Y)V from two orders of displacement; cut-cone demo; a new learner-computed 2D metric (hyperbolic plane) with a checker; sliders for the six-entry curvature table |
| **Equivalence principle and geodesics** | `manuscript-section-1-1-falling-scale-and-two-ball-tides` R; `manuscript-chapter-01-gravity-free-fall-clocks` A; `manuscript-section-5-3-rindler-accelerating-laboratory` R; `manuscript-section-5-4-5-5-geodesic-equation-from-action` R; `manuscript-section-5-6-5-7-affine-parameters-null-geodesics` R; `manuscript-section-5-8-5-9-newtonian-limit-and-tides` R; `manuscript-section-10-geodesic-deviation-newtonian-tides` R; `lesson-weightlessness-and-tides` A; `lesson-affine-is-a-parameter-choice` A; `lab-tidal-cloud-geodesic-deviation` A; `scene-3d-tidal-cloud` A; `scene-3d-earth-free-fall-flow` A; `figure-affine-parameter` A; `manuscript-section-24-2-rindler-full-check` R; `figure-rindler-worldlines` I; `figure-free-fall-comparison` I; `manuscript-section-1-10-watching-neighboring-objects-fall` I | **Two-pebble drop demo** (radial versus side-by-side, accelerometer 0 g); Einstein's elevator; interactive Rindler observers with clock rates; proper time along several worldlines between fixed events (stationary is not a global maximum); tide magnitude with real numbers |
| **Stress-energy** | `manuscript-section-11-stress-energy-measurement-and-observers` R; `manuscript-section-11-dust-and-perfect-fluids` R; `manuscript-section-11-radiation-pressure-mass-of-a-box` R; `manuscript-chapter-11-stress-energy` A; `lab-particle-stress-energy-crossings` A; `lab-fluid-viscous-shear` A; `design-doc-fluid-stress-energy-lab-spec` A; `lesson-fields-carry-energy` A; `manuscript-section-11-field-stress-tensors` I; `figure-stress-energy` I | Boosted observer (tensor transform); movable probe subvolume; photon gas reaching p = ε/3; field-energy / Poynting-flux lab; anisotropic stress example |
| **Field equations** | `manuscript-chapter-12-einstein-field-equation` R; `manuscript-section-12-trace-subtraction-and-reversal` R; `manuscript-section-12-newtonian-limit-and-coupling` R; `lesson-poisson-from-a-flux` A; `manuscript-section-09-bianchi-einstein-tensor` A; `figure-einstein-anatomy` A (Svelte + KaTeX); `figure-newtonian-calibration` A (KaTeX steps) | Trace-reversal calculator (dust, radiation, Λ, EM); ψ = 0 versus ψ = φ slider linking to light bending; one matter-sourced solution worked end to end; Gauss-surface flux demo |
| **Variational methods** | `manuscript-section-13-euler-lagrange-and-stationarity` R; `manuscript-section-13-metric-variations-and-hilbert-stress-tensor` R; `manuscript-section-14-einstein-hilbert-variation-core` R; `manuscript-chapter-13-variational-calculus` A; `manuscript-section-13-hamiltonian-mechanics` A; `manuscript-section-14-boundary-terms-ghy-palatini` A; `lesson-variations-and-boundary-data` A; `lesson-boundary-action-is-part-of-the-question` A (place before GHY); `lesson-symmetry-earns-a-charge` A; `manuscript-section-15-noether-killing-charges-redshift` A; `design-doc-action-study` A; `figure-action-variation` A; `figure-boundary-variation` A; `figure-action-product-rule` I; `figure-killing-energy` I | **Stationary-action trial-histories interactive** (free-particle minimum, oscillator saddle; spec in `design-doc-backlog-stationary-action-histories`); Killing energy carried along a symmetry flow (E_ξ versus E_local) |
| **Tests of GR** | `manuscript-section-16-weak-field-clocks-and-redshift` R; `manuscript-section-16-light-bending-shapiro-delay` R; `manuscript-section-16-gps-and-tossed-clock` R; `manuscript-chapter-16-clocks-light-mercury` A; `manuscript-section-16-mercury-perihelion` A; `manuscript-section-16-gyroscopes-experimental-map` A; `scene-3d-mercury-perihelion-precession` A; `lesson-phase-drift` A; `lesson-orbit-conservation` A; `figure-gps-clocks` A; `figure-tossed-clock` A; `figure-light-bending` A; `lab-gps-clock-rates` I; `manuscript-section-23-7-semiclassical-tests-open-questions` A; `design-doc-research-window-case-studies` A | **Gravitational lens builder** (Experience F); tower-clock (Pound-Rebka) demo; Shapiro radar-echo demo; GP-B spin-axis drift; binary pulsar; data and uncertainty exercises |
| **Schwarzschild and orbits** | `manuscript-section-17-1-schwarzschild-derivation` R; `manuscript-section-17-5-orbits-isco-photon-sphere` A; `manuscript-section-17-9-photon-observers` A; `lab-photon-redshift-observers` A; `manuscript-section-17-8-tov-star` A; `lab-stellar-structure-tov` A; `figure-black-hole-radii` A; `manuscript-section-24-3-calculation-checklist` R; `scene-3d-schwarzschild-embedding-ruler` I | **Effective-potential plot linked to a live timelike and null orbit integrator** (2m/3m/6m, b_crit = 3√3 m); zoom-whirl; Birkhoff shown visually; constant-density interior Schwarzschild; measurement-first proper-distance demo |
| **Black holes** | `lesson-horizon-directions` R; `manuscript-section-17-3-horizon-coordinates-and-observers` A; `lab-visual-lesson-horizon-light-cones` A; `review-doc-causality-and-horizon-visual-contract` ref; `lesson-kruskal-and-causal-maps` A; `lesson-causal-domains` A; `manuscript-section-19-12-dust-collapse` A; `manuscript-section-22-1-raychaudhuri-energy-conditions` R; `manuscript-section-22-5-trapped-surfaces-causal-structure` A; `manuscript-section-22-7-black-hole-thermodynamics` A; `lesson-temperature-and-quantum-input` A; `figure-focusing-caustic` A; `figure-horizon-area` A; `figure-page-curve` A; `manuscript-section-17-7-kerr` I; `figure-horizon-cones` I; `manuscript-section-22-10-information-paradox` ref | **Penrose and Kruskal diagrams** (none exist in book.md); **Reissner-Nordström** (zero mentions); **Kerr beyond orientation** (geodesics, Carter constant, spin ISCO, 3D ergoregion, Penrose process); **black-hole observer sky / shadow** (Experience G); horizon crossing with synchronised clocks and signals; animated collapse diagram; null expansions of spheres; Hawking mode or Bogoliubov calculation |
| **Gravitational waves** | `manuscript-section-18-5-quadrupole-chirp` R; `manuscript-chapter-18-gravitational-waves` A; `manuscript-section-18-1-linearized-gravity-detector` A; `scene-3d-gravitational-wave-rings` A; `figure-wave-polarizations` A; `lesson-waves-and-retarded-time` A; `lesson-waves-modes-and-green-functions` A; `manuscript-section-10-curvature-invariants-and-summary-table` R (plane-wave example) | **Interferometer response / arm-length demo**; antenna patterns; **chirp lab** (masses → f(t), audio, GW150914 overlay); noise and matched filtering; ringdown and QNMs; memory |
| **Cosmology** | `manuscript-section-19-1-friedmann-derivation` R; `manuscript-section-15-cosmological-constant-vacuum-energy` R; `lesson-distances-are-measurement-protocols` R; `manuscript-chapter-19-cosmology` A; `manuscript-section-19-6-redshift-horizons` A; `manuscript-section-19-11-distance-measures` A; `lab-cosmological-distances` A; `lab-numerical-flrw-evolution-audit` A; `lesson-a-curved-universe-capstone` A; `figure-cosmic-expansion` A; `practice-set-appendix-e-index-practice` A (E.2 scalar field); `figure-cosmic-horizons` I; `scene-3d-cosmic-expansion-lattice` I | **Mixed-component Friedmann solver** (Ω_r, Ω_m, Ω_Λ, Ω_k → a(t), q(t)); **interactive conformal diagram** with horizons; observer-centred expansion with v = Hd and a stretching photon; critical density and Ω in prose; supernova/BAO fit; CMB, structure growth, inflation |
| **Advanced topics** | ADM: `manuscript-section-20-2-constraints-and-dof` R, `manuscript-section-20-8-hole-argument` R, `manuscript-chapter-20-initial-data-numerical-relativity` A, `manuscript-section-20-7-numerical-evolution-lab` A, `lesson-evolve-and-check-the-constraint` A, `figure-adm-slicing` A, `scene-3d-adm-lapse-shift` I, `figure-constraint-count` I. Forms and tetrads: `manuscript-section-21-1-cartan-structure-equations` A, `manuscript-chapter-21-tetrads-forms` A, `lesson-oriented-stokes` A, `practice-set-21-8-surface-of-revolution` R, `manuscript-section-21-6-gauge-spinors-palatini` ref. EFT: `manuscript-section-23-2-eft-power-counting` A, `manuscript-chapter-23-effective-field-theory` A, `manuscript-section-23-4-uniqueness-vacuum-energy` ref, `lesson-an-error-budget-for-effective-theory` ref, `figure-effective-theory` I | Forms and Stokes visuals (interior-edge cancellation grid); Hodge star and Maxwell in forms; Schwarzschild via Cartan; initial-data solve (Brill-Lindquist / puncture); 1+1 gauge-wave or CFL grid demo; foliation explorer; perturbation theory and QNMs; ADM/Bondi mass computation; QFT in curved spacetime and Unruh; worked EFT power-counting observable |
| **Synthesis, reference, practice** (cross-cutting) | `manuscript-section-24-2-rindler-full-check` R; `manuscript-section-24-3-calculation-checklist` R; `lesson-a-curved-universe-capstone` A; `practice-set-appendix-a-thirty-exercises` A; `manuscript-chapter-appendix-b-reference-sheet` A; `manuscript-chapter-appendix-c-glossary` A; `manuscript-chapter-appendix-d-further-reading` A; `practice-set-transfer-problems-and-variants` A; `practice-set-chapter-guide-checks` A; `curriculum-chapter-guides` A; `figure-calculation-map` I | Curved-spacetime capstone project with AI grading at each stage; metric investigation workbench; parameterised, method-revealing practice generators |

**Topics with essentially nothing usable:** Reissner-Nordström and inner/Cauchy horizons; Penrose diagrams;
Kerr dynamics; black-hole shadows and optics; gravitational lensing images; interferometer response, noise and data
analysis; ringdown and QNMs; CMB, structure formation and inflation; black-hole perturbation theory; QFT in curved
spacetime and the Unruh effect; Hodge duality and Maxwell in forms; a solved inhomogeneous initial-data problem;
equivalence-principle experiments beyond a mention (MICROSCOPE appears only in a table).

---

## 4. Reusable engineering

### 4.1 Physics kernels and independent checks (port first, as TS + Vitest)
- **Pure models** (port verbatim): `web/relativity-models.js` (`starProfile`, `photonExchange`, `cosmicDistances`,
  `evolveDust`, `rk4Step`, `simpson`), `web/mechanics-model.js`, `web/particle-flow-model.js`,
  `web/fluid-shear-model.js`, `web/parallel-transport-model.js`, `web/geometry-foundations-model.js`,
  `web/scene-models.js` (`covectorCrossings`, `conePointVisible`, `embeddingHeight`, `radialProperLength`,
  `waveStrain`, `waveDisplacement`), the `earth-flow.js` kinematics, and `curvature-experiences.js` (`tidalCloud`,
  `canonicalCurvature`). Assets: `engine-lab-records-and-relativity-lab-shell`, `lab-*`, `scene-3d-*`.
- **Checks must not reuse the formula under test.** Examples: RK4 versus the trig solution, a tridiagonal BVP versus
  Couette/Poiseuille, brute-force plane crossings, the Lane-Emden limit, analytic dust and de Sitter distances,
  256-index Riemann symmetries, the RK4 convergence ratio between 12 and 20. Split model checks from browser checks
  (legacy `--models` flags). CI always runs the physics; browser tests run in a separate job.
- **`engine-independent-curvature-checker`**: a finite-difference curvature package used to verify vault claims
  and as a tutor tool.
- **Regression fixtures from QA screenshots**: photon 2→8 r_s = 0.75593 (√(4/7)); star ρ_c = 0.2, step 0.01 →
  R = 0.86584, M = 0.15736, 2M/R = 0.36349; distances z = 2 → D_C = 5179.9, D_A = 1726.6, D_L = 15540 Mpc; evolution
  Euler h = 0.2, t = 4 → A = 3.5571; GPS +45.724/−7.211/+38.514 μs/day; tossed clock 44.615 as; Mercury 42.98″/cy;
  area bound 29.289%; sphere octant −90°. Also encode the §8.3 orientation test (R^φ_θθφ = −1 on the unit sphere,
  octant route gives −π/2) so a sign slip cannot silently flip geodesic deviation.

### 4.2 Lab contract and shell (new, informed by legacy)
- `LabContract<State>` (from `engine-lab-state-narration-qa-contract`, `engine-experiment-tutor-context-contract`,
  `engine-lab-records-and-relativity-lab-shell`) has: a Zod state schema; `describe(state)` for narration;
  `scientificContext(state)` with `{model, parameters+units, readouts, assumptions, equations, limitations, source,
  conceptIds}`; declared `tutorCommands` validated against ranges and undoable; `predictions[]` with expected
  answers; and events emitted **on commit only**.
- **Platform-level** persistence (per user in Drizzle, localStorage fallback), lifecycle (lazy WebGL; pause offscreen
  using the latest IntersectionObserver entry; never integrate hidden time; reduced motion stops autoplay but allows
  an explicit Play; on context loss, redraw as SVG) and SSR fallback. SSR renders a static diagram plus a measurement
  table computed from the same model at its default state (idea from
  `engine-visual-fallbacks-static-measurements`).
- **Threlte `<SceneStage>`** re-implements the good patterns from `engine-threejs-scene-shell` (ref only):
  palette-role materials bound to theme tokens; camera framing from the full parameter envelope (`captureBounds`);
  bounding-sphere fit once per resize; orthographic fixed frustum when angles are measured; a "look straight at"
  button; grids painted in the fragment shader with `fwidth` antialiasing (never coincident line meshes); analytic
  hidden-line dashing (`conePointVisible`); occlusion-aware labels; keyboard orbit; a dispose discipline.
- **Controls:** drop `engine-experiment-controls-helper`. Build shared Svelte `RangeParam`, `SegmentedChoice`,
  `IconButton` and `PlaybackBar`. Use continuous sliders plus play and "next step" instead of presets. Put numerics
  controls (step size, method) under an "audit the numerics" disclosure.
- **2D charts:** compute axis envelopes per series over the parameter range, or use small multiples. Add a QA
  assertion that each series spans a minimum fraction of its axis. Add an equal-scale helper for every spacetime
  diagram. Derive tangents, labels and anchors from the model object and unit-test them (slope equals derivative).

### 4.3 Maths labelling and design tokens
- `engine-math-colour-palette`: reuse the hex pairs as tokens, add surface and material tokens, and check contrast
  in CI.
- `engine-semantic-tex-colouring`: reimagine. Author KaTeX macros (`\metric{g}_{\mu\nu}`, `\riemann{R}`,
  `\connection{\Gamma}`) that emit `\htmlClass` with concept-registry ids. Keep indices neutral. Restore clean TeX in
  the MathML annotation. Identity is scoped **per occurrence** (the τ_plot lesson, F01). Unresolved symbols get no
  colour and no tooltip.
- Figures: pass TeX straight to KaTeX. Drop `engine-or-tool-figure-generator`, `engine-or-tool-figure-typesetter`
  and `tool-figure-and-caption-math-maps`, but mine the formulas and captions. Keep prose out of SVG and design the
  phone layout first. Port `engine-or-tool-figure-geometry-check` as a Playwright test at 320/390/1440 in both
  themes, with a minimum label height.
- Typography: Newsreader for prose, Manrope for UI (OFL), KaTeX with MathML. Choose an icon set with an unambiguous
  licence (Hugeicons has an MIT versus "all rights reserved" conflict; see `design-doc-vendor-notices`).
- Media: reuse the provenance manifest schema from `assets/history/manifest.json` and `assets/earth/manifest.json`
  for all media.

### 4.4 Content, curriculum and learner state
- **Lesson schema** (`curriculum-lesson-template`): question, intuition, steps each with a reason, formal limits,
  predict-check with authored choice ids and per-option feedback, transfer with a required intermediate, variants,
  claim-level sources, takeaway, `placement: preparation | worked-example` with a written reason
  (`curriculum-lesson-sequence`), and depth `core | worked | further` with a narration policy per depth.
- **Validators to port** (`curriculum-chapter-dependency-graph`, `curriculum-skill-map`): acyclicity, route
  closure, exactly one correct choice, unique choice ids, finite answers and tolerances, taught-before-required (now
  on concept ids, **with no exemption for "basic" skills**), core text never pointing into further-depth material,
  no raw TeX or unmatched delimiters in rendered output. Also port the words and equations before the first visual
  (`engine-or-tool-visual-placement-audit`) as a CI report.
- **Learner state** (`engine-learning-state-notebook`, `design-doc-course-architecture-and-learner-state`): Drizzle
  tables for `attempts(item_id, item_version, params, answer, correct, help_level none|hint|solution, at)`,
  `passage_progress(content_hash, last_word, last_seconds)`, `listening_sessions`, `notes`, `experiment_snapshots`.
  Keep **visited, listened, attempted and demonstrated** distinct. Port `parseNumericAnswer`, `evidenceLabel` and
  idempotent merge by event id for offline sync. Replace the 3-day rule with a real spaced scheduler.
- **Stable ids everywhere.** Legacy positional `passage-N` (89% of passages), hash-of-text choice ids and ordinal
  figure numbers all broke downstream keys. `content/section-ids.json` shows why ids must not be derived from
  headings. `tool-section-id-map` itself is D unless old URLs need redirects.

### 4.5 Voice tutor, narration and reader
| Legacy asset | Verdict | Port note for SvelteKit + Better Auth + Drizzle + Vercel |
| --- | --- | --- |
| `engine-or-tool-voice-tool-scheduler` | R | Client dispatcher for GPT-Live function calls. Client tools (navigate, highlight, play, set lab control) and server tools (consult, search, read) go through the same queue. |
| `engine-or-tool-realtime-webrtc-transport` | A | Keep `connectRealtime` on the client. Move `mintRealtimeSecret` to `POST /api/voice/session`: auth session, decrypt the user's stored key, bake in instructions and tools, return only the ephemeral secret. Keep the Voicebook MIT attribution. |
| `app-code-voice-session-controller` | A | Start from `voice.svelte.ts` for structure. **Restore** the legacy per-response queue (the rebuild runs tools on `cleared`, so barge-in can navigate) and the full `interruptedReading` snapshot (passage, seconds, spoken words, lab state). Mic off while narrating. Commit the input buffer only if capture lasted ≥ 100-120 ms. Release on blur, visibility change and Escape. Keep per-turn context small and let tools fetch outlines. |
| `engine-or-tool-hold-to-talk-shortcut` | R | Copy `shortcut.ts`. Store the preference in `user_preferences`. Add a touch press-and-hold button. |
| `engine-or-tool-tutor-prompts-and-tool-definitions` | A | Split into a voice persona prompt, a server text-tutor prompt and per-tool descriptions. Keep: hint before solution; meaning before maths; navigation is not narration; stay silent after handoff; never read ids aloud; retrieved text is data, not instructions; propose one control plus a prediction. Version prompts with an eval set. |
| `engine-or-tool-text-tutor-tool-loop` | I | A server streaming endpoint with bounded rounds, `{error}` returned as tool output, id validation and **citations (concept and passage ids) on every answer**. The same endpoint backs `consult_text_tutor`. |
| `engine-or-tool-provider-clients` | A | `src/lib/server/providers.ts`. Keep the retry policy (429/5xx, no quota errors, retry-after capped at 5 s, max 2 retries, never replay ambiguous network failures) and request-id surfacing. Add usage metering. |
| `engine-or-tool-reading-context-extraction` | A | Port `readingNeighborhood` and `explicitNarrationRange` with tests: exercises retrieved without solutions, hidden depth only with the same depth, proofs ±3 steps. Replace DOM scraping with a typed reader store plus a `LabState` registry. Tag every retrieved passage `visible | hidden | reference`. |
| `engine-or-tool-math-narration-script-generation` | A | Legacy v3 prompt, per-kind word budgets, TeX-rejection validator. Generate at authoring time with reviewer sign-off. Learner edits are per-user overrides. |
| `engine-or-tool-narration-audio-player` | A | Keep `groupPassages` (~1,400 chars), `splitPrepared` (offset-preserving), `previous_text`, a ~2 min prebuffer and follow-scroll. Serve audio from a shared server cache keyed by voice, model and script hash. Preserve pitch at 2×. |
| `engine-or-tool-spoken-word-highlighting` | R | Copy `highlight.ts`, `wordAt` and `captionTokens`. Equations and figures get captions, not in-text highlights. Say so when alignment is missing. |
| `engine-or-tool-passage-segmentation-model` | A | Keep the passage kinds and the depth, noNarration and supplement flags, and section ranges. Use authored stable ids in Postgres. Compute before/after context on demand. |
| `engine-or-tool-selection-to-passages` | A | A Svelte action. Send selections as `{passageIds, text, latex[]}` reference data. |
| `engine-or-tool-safe-math-answer-rendering` | R | Copy `format.ts` (markdown-it with html off, KaTeX, DOMPurify). Needs isomorphic DOMPurify for SSR. |
| `engine-or-tool-book-search` | I | Postgres full-text plus pgvector, with synonyms from concept aliases. Keep the Cmd+K combobox UX. |
| `engine-or-tool-byok-settings-and-local-cache` | I | `provider_credentials` table with envelope encryption, a "test connection" endpoint, keys never sent to the client. Keep the Connections UX (voice picker, remove keys). |
| `engine-or-tool-listening-history` | I | Drizzle `passage_progress`. Keep hash invalidation and merged ranges for prompt compaction. "History is not mastery." |
| `engine-or-tool-reading-position-restore` | A | SvelteKit snapshots with anchor + offset. Persist the last position per user. |
| `app-code-sveltekit-reader-shell`, `app-code-companion-ui-components` | A | Reuse tokens, the pre-hydration theme script, sidebar rail and flyout mechanics, the nonmodal side window that reserves reading width, the Player layout and `IssueNotice`. Drop `{@html}` book mounting and adapter-static. |
| `engine-or-tool-mocked-provider-test-harness` | A | Port the fake RTCPeerConnection and getUserMedia, the WAV + alignment generator and the provider route mocks, retargeted to server proxy routes. **Add** an opt-in live suite and an offline tutor eval corpus. |
| `app-code-legacy-study-companion`, `design-doc-study-companion` | ref | Behaviour spec only (pause-to-ask with resume, dock, selection and equation Listen/Explain, the disclaimer on generated scripts). |
| `engine-or-tool-sveltekit-content-prepare-pipeline`, `app-code-reader-shell`, `engine-or-tool-editorial-narration-notes` (mechanism) | D | Do not carry over. |

---

## 5. Lessons learned (deduplicated)

### 5.1 Scientific pitfalls (turn each into a vault note, tutor guardrail and eval item)
1. A homogeneous massless scalar with V = 0 is stiff matter (p = ε, ε ∝ a⁻⁶), not dust. It becomes dust-like only
   when oscillating fast in a mass potential.
2. Curvature × c² has units of 1/time², not acceleration. A tidal acceleration needs a separation, and curvature
   says nothing about a supported observer's weight.
3. Ricci as initial volume focusing holds only for an initially comoving infinitesimal ball (zero expansion, shear
   and vorticity). A trace-free tide still changes volume later (V/V₀ = 1 − s⁴/2 + …).
4. With x⁰ = ct and SI action, the Einstein-Hilbert prefactor is c³/(16πG) with a matching 1/c on matter, not c⁴.
   T^{0i} is energy flux divided by c.
5. Kerr horizon area depends on spin. A mass-only merger area bound is a nonspinning ideal bound, not an efficiency.
6. Radiation-pressure focusing does not explain the factor of 2 in light bending. The spatial potential Ψ does;
   setting Ψ = 0 halves the deflection.
7. A thermal-looking Hawking spectrum does not rule out correlations. The Euclidean periodicity argument imports
   quantum statistics and does not derive the outgoing flux.
8. A GPS clock offset × c is a ranging scale (11.5 km/day), not a position error.
9. Slogans to avoid: every geodesic globally maximises proper time; R = 0 means flat (R_abcd = 0 ⇒ R_ab = 0 ⇒ R = 0,
   with no converse); the equivalence principle alone gives GR; a hovering clock at the horizon; c⁴/G is a proven
   maximum force.
10. Nonzero Christoffels, position-dependent g, coordinate acceleration and clock-rate differences do not prove
    curvature. Test case: N(z) = 1 + az/c² is flat, while N = e^{kz} gives R = −2k².
11. Never reuse a symbol across dimensions or meanings (legacy K was both Kretschmann and a tidal component, F02; A,
    ω, β and the curvature two-form also collided). Use scoped symbol registries.
12. A trace-zero matrix diag(2,−1,−1) is not "compression". A two-parameter strip is not a congruence. Plane-wave
    coordinates are not both null when g^{VV} ≠ 0. A trial displacement needs length units.
13. Keep the black-hole radii distinct: 2m horizon, 3m photon sphere, 6m ISCO, b_crit = 3√3 m. A shadow or EHT ring
    is not a photograph of the horizon. Do not draw light rays on Flamm's paraboloid (a spatial embedding). A
    coordinate singularity must not be rendered as light freezing.
14. Lensing: source angle β, image angle θ and the bend angle α are different quantities. Rays, images,
    magnification and delay must come from one model.
15. Stress-energy: the first index is the direction crossed and the second the quantity carried. Pressure as
    momentum flux has the opposite sign to Cauchy stress. A boosted density comes from transforming the tensor, not
    from re-speeding the particles. p = ε/3 needs 3D directions.
16. Embedded-surface transport is dV/ds = −(V·dn/ds)n. Projection plus renormalisation is not exact transport. The
    cylinder is intrinsically flat. The surface picture is Riemannian, so bridge to Lorentzian geometry explicitly.
17. A noncommuting frame is not torsion. Teach [X,Y] before torsion. The flow-commutator sign is
    convention-dependent.
18. The tidal-cloud deformation (1+2s, 1−s, 1−s) preserves volume only to first order. A constant-matrix model is not
    a Schwarzschild congruence.
19. Loose linear-algebra wording: "one negative, three positive eigenvalues" is basis-dependent; Sylvester's
    signature is the invariant (4.4). Twenty Riemann components are not twenty polarisations.
20. Research claims (GW170817 speed, EHT, NANOGrav, DESI DR2, GWTC-5.0, Kerr stability) go into dated
    research-window cards. Evolving dark energy is not established.

### 5.2 Sequencing problems
- **First-use leaks were systematic.** Metric, connection coefficients and Ricci appeared in Ch 0-3. The Lie bracket
  was used in Ch 7 but developed in Ch 15. The Poynting vector was assumed in 11.6. sinh/cosh were cited from a
  collapsed block. Complex exponentials came before any lesson on them. Extrinsic curvature was used before its
  definition. The orbit equation was imported from 17.5 into 16.6. The LT rate was imported from 17.7. Global
  causal definitions came after the singularity theorems used them. **Fix:** a concept registry with introduces and
  requires on every section, plus a build check. A keyword blacklist is not enough.
- **Order tides before Ricci/Weyl** (9.2 already depends on Ch 10). Pair 9.4-9.5 (Bianchi) with 12.2 (half trace) as
  one "left-hand side" unit. Put the GHY toy before GHY. Put the Schwarzschild orbit equation before Mercury.
- **Placement fails both ways.** Auto-insertion after headings put machinery before its explanation (26 of 36
  lessons belonged after the exposition; 8 labs were misplaced). A blanket "picture after explanation" rule left 29
  to 38 equations before any visual (Ch 7, 15, 18, 21). **Fix:** explicit anchors with a role (observe, construct,
  compare, derive) and a written reason, and an opening visual state in plain language.
- **Required content must not hide behind optional-looking depth.** Seven "Further calculation" blocks (including
  the only quantitative holonomy derivation) were collapsed *and* skipped by narration. Derivation panels
  disappeared without JS.
- **Chapter-level prerequisites and bundling inflate routes.** The "short" black-hole route needed 22 of 25 chapters
  because Ch 22 bundled singularity theorems (which need forms) with Hawking temperature (which does not). Model
  prerequisites at concept granularity. Keep unrelated destinations in separate clusters. Derive "optional" and
  "required" badges from one source.
- **Grab-bag chapters must be split:** Ch 15 (flows, Noether, energy, Λ, Mach), 4.8 (four ideas in 450 words), 6.5,
  Ch 17 (derivation, observers, Kerr, TOV, redshift), Ch 22 (classical versus semiclassical), 11.6 (EM primer inside
  tensors).
- **A three-step bridge cannot teach a prerequisite subject** (EM, thermal physics, quantum states). Either build a
  real optional module or state the boundary.
- **Practice kept apart from the teaching does not work.** Appendix A had inline solutions. Ch 2-8 had no in-text
  exercises. Distribute items to the point of use and hide solutions behind an attempt.
- **Prose that narrates a demo** ("The animation below…", §1.10, §4.5, §6.6, the Ch 8 opening) must be ported with
  its demo or rewritten. Track demo-dependent sentences. **A quantity must never live only in a demo** (Ω and E(z)
  existed only in the distances lab record).

### 5.3 Design and interaction principles
- Teach each experience as **observe → predict → try (one control, one legible change) → compare → name and
  calculate → transfer**. The default state already shows the effect (the routes lab opens with 90° visible). Prose
  stays coherent if Play is never pressed.
- **Organise every scene around one measurement the learner performs.** Crossings, the fluid cut and photon wave
  strips worked. The funnel embedding, sliding ADM planes and a lattice scaling about its centre did not. Use 3D only
  when depth is the idea, with a 2D companion for unambiguous measurement.
- **Put the teaching feature on the default screen.** A readout that can never change (local c = 1) is a statement,
  not a measurement. Axes tuned to one state hide others (D_A on a 50 Gpc axis, the star's maximum mass).
- **Continuous parameters beat presets.** Old preset-only lessons felt like slideshows.
- **One idea, one primary representation.** Retire superseded interfaces: Ch 4, 6 and 8 each showed two interfaces
  for one idea. A static figure becomes the fallback or reference for its interactive.
- **One colour means one role everywhere**, backed by shape or labels. One sign convention per quantity, shown
  identically in label and readout. Notation must match across prose, figure, narration and tutor (q/λ versus x/ε;
  transposed stress-energy labels).
- **Write an annotation spec per teaching state** (entities, units, anchor, occlusion fallback). Nothing essential
  depends on hover. Labels sit beside objects with leaders. On phones, stack rather than shrink.
- **Honesty rule:** every visual names its model, its exaggeration and what it does not show. Feed those caveats to
  the tutor so narration repeats them.
- **Show visual claims in the picture itself** (caustic paths continuing past the focus; Page-curve branches). A
  reader should be able to point at the part of the image that justifies the caption.
- **Caveats belong in a fine-print or tutor layer and in misconception checks**, not trailing every sentence. Keep
  one core claim per step.
- **AI and voice:** navigation and narration are separate tools; the voice model is the front end and delegates
  physics to a text model; the tutor reads semantic state, never pixels; tutor commands are validated and undoable;
  simulation output, analytic calculation and conceptual explanation stay labelled as distinct; hints come before
  solutions; the core course must be excellent without AI.

### 5.4 Process lessons
- **Passing tests is not teaching.** 74 page checks, 680 lesson interactions and 80 figure renders all passed while
  Chapter 0 failed novices and a tooltip called τ_plot "proper time". Target named failure modes (definition before
  use, notation consistency, missing labels), not mirrors of the implementation's own formulas. Pair every automated
  gate with a human screenshot review at 390 and 1440 px in both themes, which caught overlit surfaces, tiny cones
  and colliding labels.
- **Every interactive needs a behavioural test** (move a control, assert the readout changes). The SvelteKit port
  shipped inert GPS and twin widgets that static screenshots could not catch.
- **Refactors must carry their tests.** The `app/` rebuild silently dropped the per-response tool queue, consult
  citations, passage visibility tags, IDF search and the interrupted-reading lab state.
- **Budget a learner-observation pass** before calling anything novice-ready. Use the protocol in
  `design-doc-course-architecture-and-learner-state`. **Budget a live AI evaluation** covering the ten tutor eval
  families, spoken-maths fidelity, latency and cost per chapter-hour. None was ever run.
- **Review documents go stale within hours.** The TOV "missing" finding was already fixed the same day. Figure
  dispositions changed after review, and counts in architecture and credits docs drifted. Keep status in one place
  (the vault), date every finding, re-check before acting and generate counts from content.
- **Status vocabulary matters:** keep shipped, implemented-and-pushed, partial and open distinct. Definition of
  done: visual and surrounding teaching implemented together, maths verified, both themes and widths inspected,
  real controls exercised.
- **Authoring format matters.** One-line `String.raw` JS objects and a 481-line one-liner component hindered
  scientific review. Use schema-validated files with one field per line.
- **Keyword-derived topic tags are unreliable** ("Shapiro" matched BSSN). Tag concepts only after reading, with a
  line reference.
- **Add prose linting**: revision artefacts ("The worked example now obtains…", §19.11) and lowercase sentence
  starts (§20.3, §23.3) slipped past maths and link checks.
- **Answer position leaks** (all 13 original correct answers at index 0). Reusing one item as diagnostic, transfer
  and skill check spoiled all three. Numeric-only checks cannot see the method.

---

## 6. Unbuilt backlog

### 6.1 Planned experiences never built (with a spec source)
| Experience | Spec / source id | Priority for grbook.ai |
| --- | --- | --- |
| Stationary action as a comparison of whole histories (free-particle minimum, oscillator saddle with ω = 1/s and T = 4 s, localised bump → Euler-Lagrange residual) | `design-doc-backlog-stationary-action-histories`, `design-doc-action-study` | High: underpins geodesics, Einstein-Hilbert and Hamiltonian units |
| Clock-and-radar special-relativity lab | `design-doc-backlog-new-laboratories` | High: best early SR investment |
| Gravitational lens builder (Experience F) | `design-doc-backlog-gravitational-lens-builder` | High: low numerical risk, showpiece |
| Black-hole observer sky with selectable rays (Experience G; CPU reference integrator plus GPU sky, check Bruneton BSD-3) | `design-doc-backlog-black-hole-observer-sky` | High, large: flagship 3D |
| Penrose/Kruskal compactification sequence, collapse diagram, RN with Cauchy horizon, domain-of-dependence painter | `design-doc-backlog-penrose-kruskal-causal-structure`, `lesson-kruskal-and-causal-maps`, `manuscript-section-22-5-trapped-surfaces-causal-structure` | High: no spec yet, write one first |
| Forms and Stokes: level-set pairings, interior-edge cancellation grid, oriented flux | `design-doc-backlog-differential-forms-stokes`, `lesson-oriented-stokes` | Medium |
| Metric investigation workbench (tutor poses a metric, verifies learner Christoffels and curvature) | `design-doc-backlog-new-laboratories` + `engine-independent-curvature-checker` | High for AI-centred design |
| Interferometer and waveform lab with noise; chirp from masses; GW150914 overlay | `design-doc-backlog-new-laboratories`, `manuscript-chapter-18-gravitational-waves` | Medium |
| Initial-data / constraint lab (puncture data) and 1+1 gauge-wave or CFL demo | `design-doc-backlog-new-laboratories`, `manuscript-section-20-7-numerical-evolution-lab` | Low (advanced) |
| One geometry in several charts (inertial versus Rindler, invariants fixed) | `design-doc-backlog-new-laboratories` | Medium |
| Einstein's elevator; horizon crossing with synchronised clocks and signals; GPS constellation; draw-a-worldline; curvature microscope | `design-doc-experience-ideas` (#6, #7, #8, #10, #11) | Medium-high |
| Symbol inspection; unfolding derivations; predict-then-reveal; test-a-misconception; explain-it-back; narration with timed scene cues; scratchpad with unit and index checks | `design-doc-experience-ideas` (#1, #2, #12, #13, #14, #16, #17) | High for AI features (#3 voice-driven labs and #17 visual score first) |
| Chapter-coverage first visuals: Killing energy along a symmetry flow (15), light-exchange detector (18), null-ray bundle with area marks and trapped surfaces (22), matter-to-curvature measurement link (12), geodesic built by carrying a tangent (5), trace versus shape with a transported family (9) | `design-doc-backlog-chapter-visual-coverage-map` | Needs specs |
| Field-energy / Poynting-flux lab | `review-doc-field-energy-preparation` | Medium |
| Effective-potential plus orbit integrator (2m/3m/6m, zoom-whirl, shadow b_crit); Kerr 3D ergoregion with ZAMO paths and spin ISCO; Friedmann mixed-component solver; interactive conformal diagram; two-pebble tidal drop; trace-reversal calculator; black-hole thermometer; scale-ladder EFT plot | Reuse notes in `manuscript-section-17-5-orbits-isco-photon-sphere`, `manuscript-section-17-7-kerr`, `manuscript-section-19-1-friedmann-derivation`, `figure-cosmic-horizons`, `manuscript-section-1-10-watching-neighboring-objects-fall`, `manuscript-chapter-12-einstein-field-equation`, `manuscript-section-22-7-black-hole-thermodynamics`, `manuscript-section-23-2-eft-power-counting` | Orbits, Friedmann and two-pebble are high |

### 6.2 Unfinished pieces of built labs (do during the port)
- **Transport** (`scene-3d-parallel-transport-loop` / `-two-routes`): shaded signed area with an orientation arrow;
  unrolled cylinder; second vector; noncontractible loop; angle/area → K readout; R(X,Y)V infinitesimal mode; fix the
  unsigned arc label.
- **Polar and vector field** (`lab-polar-coordinates-two-addresses`, `lab-vector-field-two-arrows`): unit versus
  coordinate basis toggle; area element / determinant cell; moving markers; divergence flux box; Δθ → 0 limit
  readout.
- **Flow order**: computed ratio, second field pair, four-leg loop. **Riemann count**: commit-not-hover, dimension
  selector, colour and numbering fixes.
- **Fluid / particle** (`lab-particle-stress-energy-crossings`): movable subvolume, observer boost, photon gas (the
  ledger marks this lab "Partial").
- **Star**: M-R / M(ρ_c) family with turning point, physical units, lapse overlay. **Photon**: spacetime diagram,
  travel-time readout, free-fall receiver, distinct default curves. **Distances**: D_A visibility, Ω prose,
  presets, allowed region, data overlay. **Evolution**: autoscale, log-log convergence, Λ/curvature.
- **Scenes**: Earth grid (thinner, marked pairs, finite-radius release, identify the unexplained teal ring); covector
  (selectable covector, draggable tip, highlight crossings); light cone (vector classifier, boost, de-emphasised past
  cone); tidal cloud (physical parameters, eigen matrix); wave rings (face-on first, L-arm response, chirp);
  embedding (measurement-first rebuild); expansion (observer-centred, Friedmann-driven, photon); ADM (fixed spacetime,
  lapse control); precession (log magnification, geodesic mode).
- **Replace** `lab-gps-clock-rates` and `lab-twin-paradox-clocks` (both rough and inert in `app/`) with a
  clock-budget demo and a worldline diagram.

### 6.3 Content fixes and gaps to close when porting text
- Show the 8.1 first-derivative cancellations. Derive or clearly label the 8.3 small-loop formula (the sign is
  correct and should be unit-tested). Promote the sphere area derivation and cut cone to core, and narrate them.
- Worked 1D/polar example before the 7.4 transformation law. Split 4.8. Add a hyperbolic-motion example to 3.8.
  Fix the 4.4 eigenvalue wording. Fix the §5.3 back-reference to rapidity.
- Figure fixes if reused: `figure-stress-energy` labels transposed and σ versus Π; `figure-action-variation` x/ε
  versus q/λ; unequal axis scales in `figure-rindler-worldlines` and `figure-horizon-cones`; `figure-polar-metric`
  edge labels on the wrong edges; `figure-boundary-variation` tangents 10% off and nearly invisible;
  `figure-light-bending` 5 px reference offset; `figure-cosmic-horizons` missing Hubble radius; unmapped "1912-13"
  on the timeline.
- One symbol for the curvature two-form (21.x versus A.28 Ω). Unify guide titles with headings. Remove revision
  artefacts (19.11) and lowercase starts (20.3, 23.3).
- Define critical density, Ω and E(z) in cosmology prose. Add Kerr beyond orientation, Reissner-Nordström,
  Penrose diagrams, a solved initial-data problem, Maxwell in forms and the Hodge star, a worked EFT power-counting
  observable, and a curved-spacetime capstone (`lesson-a-curved-universe-capstone` is the seed).
- Practice: 3-5 checks per lesson (predict, calculate, diagnose); structured answers for Appendix A; transfer
  variants for every item; answers for the 17 base-skill check prompts in `curriculum-skill-map`; distinct
  diagnostic, transfer and review pools.
- **AI:** tutor evaluation corpus (ten families, public and held-out splits, seeded from §5.1 and
  `design-doc-misconception-diagnostics`); live provider suite; authored or reviewed narration for critical
  equations (only 9 of 4,695 passages had authored narration); restore the `app/` regressions listed in §4.5.
- **Learning evidence:** a think-aloud learner study across three entry backgrounds before any novice-readiness
  claim.
