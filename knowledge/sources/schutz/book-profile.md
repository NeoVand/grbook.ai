---
type: book-profile
book: schutz
book_short: SCH
title: A First Course in General Relativity
authors:
  - Bernard Schutz
edition: Third edition (2022), Cambridge University Press
units: [front, ch01, ch02, ch03, ch04, ch05, ch06, ch07, ch08, ch09, ch10, ch11, ch12, ch13, appA]
signature: "A geometry-first undergraduate course that rebuilds special relativity from spacetime pictures, teaches tensors as machines and one-forms as stacks of surfaces, and gets every formal result from a physical measurement or a local-inertial-frame argument before cashing it in on stars, black holes, gravitational-wave data and cosmology."
units_needing_attention: []
---

# SCH: Schutz, *A First Course in General Relativity* (3rd ed.): teaching profile

Every unit dossier (ch01-ch13, appA) came back from verification as **fixed**: problems were found, corrected in the dossier, and nothing is left open. No unit is flagged for re-work. The printed book does contain errors, though, and they are listed in Section 7. The front matter was read from `book-sources/_chapters/schutz/front.md`. That reading copy starts partway through the third-edition preface, so the opening lines of that preface are missing. The prefaces to the second and first editions are complete. Locators are given as unit id, section and printed page.

---

## 1. Identity and audience

- **Who it is for.** Undergraduates, and graduate students moving faster. The first-edition preface says the book grew out of a full-year undergraduate course taught 1975-1980. The author came away convinced that GR is not much harder than undergraduate electromagnetism or quantum mechanics (front, p. xiii). Three goals: understand the basic concepts and their experimental consequences, solve elementary problems, and arrive ready for advanced texts.
- **Prerequisites (front, p. xiv).** Special relativity including the Lorentz transformation and relativistic mechanics. Euclidean vector calculus. Ordinary and simple partial differential equations. Thermodynamics and hydrostatics. Newtonian gravity. Enough quantum mechanics to know what a photon is. Unusually, the book does **not** assume covariant electromagnetism, electromagnetic wave theory or fluid dynamics. Fluids are built in ch04, and the wave equation is developed from scratch for gravitational waves (ch08 §8.3, ch09 §9.2). The dossiers confirm that ch01 assumes prior algebraic SR (ch01 difficulty notes) and that ch10 §10.7 and ch13 §13.4 need quantum statistics, astronomy and some particle physics (ch10 and ch13 background lists).
- **Level and difficulty curve.** Math ratings climb from 2 (ch01-ch02) to 3 (ch03-ch05), peak at 4 in ch06 (curved manifolds), ch09 (GW generation and energy) and ch11 (black holes), then settle at 3 for ch12-ch13. Novice-friendliness is 4 for ch01-ch03, ch05 and ch07, and 3 elsewhere (Section 10).
- **Tone.** Conversational, first person, patient. The text anticipates objections: "Why distinguish one-forms from vectors?", "circular reasoning?" (ch03 §3.3-3.6). It uses humour, such as graduate students riding clocks (ch01 §1.13) and a joke about naming apses (ch11 margin note, p. 303). It is candid about what is guessed rather than derived: Einstein's equations are presented as a well-motivated guess (ch08 §8.1), and h is called a "convenient fiction" (ch08 §8.3).
- **Length.** 471 printed pages in 13 chapters plus a 4-page linear-algebra appendix. The book has no formal Parts (toc.json `parts: []`). Chapters 1-8 (201 pp.) cover the foundations, and chapters 9-13 (266 pp.) are long and increasingly observational. ch09 (65 pp.), ch11 (64 pp.), ch12 (55 pp.) and ch13 (53 pp.) are each longer than any foundation chapter.
- **What it deliberately omits (front, pp. xiii-xiv; dossiers).**
  - Nonmetric manifold theory, Lie derivatives and fibre bundles. Lie brackets appear only in Exercise 6.39 (ch06).
  - Quantization, apart from a heuristic Hawking-radiation argument (ch11 §11.5).
  - A systematic chapter on experimental tests and alternative theories. Tests are handled as they come up.
  - Exact nonlinear solutions beyond the plane-wave and spherical cases. Kerr is quoted and examined, not derived (ch11 §11.3).
  - A variational or action derivation of the field equations. ch08 motivates G + Λg = 8πT instead.
  - Killing vectors, except in an exercise (ch07 Exercise 7.10).
  - Penrose (conformal) diagrams, and the inner Kerr horizon and ring singularity (ch11 gaps).
  - Initial-value, 3+1 and numerical-relativity machinery. These are only mentioned (ch08 §8.2).
  - Solutions to exercises. They were removed from the book at the second edition (front, p. xii).

## 2. The author's stated goals and philosophy (paraphrased)

1. **Accessible without being watered down** (front, first-edition preface). Keep prerequisites minimal, but introduce differential geometry in full rather than relying only on curved-surface analogies. Give the full nonlinear field equations, not just linearized theory. In each topic, lay enough foundation that the student can go on to advanced texts without starting over.
2. **Geometry is the durable foundation.** The second- and third-edition prefaces say the geometric approach of chapters 1-8 has held up. Revisions there were minor: modernizing, fixing typos, simplifying. The effort went into the applications. ch01's dossier records the same stance in the teaching: SR is re-taught geometrically, following Minkowski, because that picture leads to GR (ch01 role).
3. **GR belongs to modern astronomy.** The later chapters were reorganized around observation. Gravitational waves now get two chapters (theory in ch09, detectors, data analysis and detections in ch12). The stellar and black-hole chapters absorb what gravitational-wave observations have taught. Cosmology (ch13) opens with what is observed and ends with open problems in fundamental physics (front, third-edition preface; ch09 §9.1 recasts GR as central to astronomy rather than a theory of tiny corrections).
4. **Derivations other introductions skip.** The preface highlights four "accessible insights" the author considers distinctive:
   - a physical derivation of gravitational-wave energy flux built on Feynman's sticky-bead argument (ch09 §9.5);
   - an order-of-magnitude derivation of Hawking radiation from vacuum fluctuations near the horizon (ch11 §11.5);
   - equatorial Kerr orbits using a factorized potential (ch11 §11.3);
   - the Forward-Berman argument that inspiralling binaries are standard sirens because GR has no intrinsic scale (ch09 §9.6).
5. **Problems are part of understanding.** The preface insists that a student who cannot solve reasonable problems does not truly understand the concepts. Separating conceptual fascination from problem-solving is called false and dangerous. The easy early exercises are described as essential practice. Several chapters have more than 30 exercises, and some need a computer.
6. **Notation follows MTW, pedagogy does not.** Conventions are essentially those of Misner, Thorne and Wheeler, and MTW is suggested as a follow-on text. The style is described as very different, aimed at a wider audience (front, p. xiv).
7. **Suggested course routes (front, pp. xiv-xv).**
   - The whole book in one year.
   - Half-year on gravitational waves and black holes for students who know EM waves: skim ch01-03, skip most of ch04, ch07 and ch10. The preface's chapter numbers are from the first edition, and the chapter list has changed since.
   - Half-year on stars and cosmology: move fast through the SR chapters and skip the waves and black-hole chapters.
   - Graduate students: the whole text in half a year.

## 3. Architecture

### Dependency outline

```
ch01 SR from spacetime diagrams (interval, light cones, hyperbolae, twin paradox)
  └─ ch02 Four-vectors, index machinery, U, p, -p·U_obs, photons
       └─ ch03 Tensors as multilinear machines; one-forms; metric as vector→one-form map; ∇T in flat space
            └─ ch04 Perfect fluids in SR: N, T^{αβ}, T^{αβ}_{,β}=0, Euler eq., "T must gravitate"
                 └─ ch05 Physical case for curvature (redshift, EP, tides) + covariant derivative rehearsed in flat polar coords
                      └─ ch06 Manifolds, local flatness, ∇, parallel transport, geodesics, Riemann, deviation, Bianchi, G
                           └─ ch07 Physics in curved spacetime: EP postulates, comma→semicolon, Newtonian limit, conserved -p_0, p_φ
                                └─ ch08 Field equations G+Λg=8πT; geometrized units; linearized theory; far-field mass
                                     ├─ ch09 GW theory: TT gauge, detection, quadrupole formula, energy flux, chirp mass, sirens
                                     │    └─ ch12 GW astronomy: sources, detector tensor, matched filtering, detections (needs ch11 too)
                                     ├─ ch10 Static spherical stars: TOV, Schwarzschild exterior, Buchdahl 4/9, compact objects
                                     │    └─ ch11 Schwarzschild orbits and tests, horizon, Kruskal, Kerr, astrophysical BHs, Hawking
                                     └─ ch13 Cosmology: FRW (borrowing ch10's Einstein tensor), distances, Friedmann, Λ, CMB, inflation
appA Linear-algebra look-up sheet (used from ch02 onward)
```

The flow is strictly linear through ch08. After that ch09 and ch10 both hang off ch08. The capstones ch12 and ch13 draw on nearly everything: ch13's dossier lists back-references to ch04, ch06, ch07, ch08, ch09, ch10, ch11 and ch12.

### Where the pivotal ideas first appear

| Idea | First appearance | Developed / revisited |
|---|---|---|
| Special relativity | ch01 §1.1 (p. 1), geometric rebuild; Lorentz transformation only at §1.9 (p. 21) | ch02 (four-vectors), ch03 §3.1 (metric) |
| Vectors | ch02 §2.1 (p. 33), provisional "components transform like Δx" | ch05 §5.2 (tangent to a curve), ch06 §6.1 (on manifolds) |
| One-forms | ch03 §3.3 (p. 58); gradient as a one-form §3.4 (p. 62) | ch04 §4.3 (one-forms as surfaces, flux), ch05 §5.2 (polar), ch12 §12.3 (detector tensor) |
| Tensors | ch03 §3.1-3.2 (p. 56), dot product reread as a machine; (M N) tensors §3.7 | ch04 §4.4 (stress-energy), ch06 §6.1 |
| Equivalence principle | ch05 §5.1 (p. 111), redshift tower, falling frames, tides | ch07 §7.1 (p. 170), numbered postulates (WEP IV, EEP IV') |
| Manifolds and metric | Metric tensor ch03 §3.1; metric in curvilinear coordinates ch05 §5.2; manifolds ch06 §6.1-6.2 (pp. 141-143) | ch06 §6.2 local-flatness theorem |
| Connection and parallel transport | Christoffel symbols in flat polar coordinates ch05 §5.3-5.4 (pp. 124-130); curved case ch06 §6.3; parallel transport and geodesics ch06 §6.4 (p. 152) | ch07 §7.2 (weak-field geodesics) |
| Curvature | Heuristic as the failure of parallelism, ch05 §5.1 (p. 117); Riemann tensor ch06 §6.5 (p. 156) | ch06 §6.6 (Ricci, Einstein), ch09 §9.2 (wave tidal field) |
| Stress-energy | ch04 §4.4 (p. 91); perfect fluid §4.7 (p. 100) | ch07 §7.1 (curved), ch08 §8.1 (source), ch10 §10.3, ch13 §13.3 |
| Field equations | Previewed via the Bianchi identities ch06 §6.6 (p. 162); stated ch08 §8.2 (p. 186) | ch08 §8.3-8.4 (linearized), ch10, ch13 §13.3 |
| Schwarzschild | Named in ch07 Exercise 7.7; derived as exterior ch10 §10.4 (p. 273) | ch11 (whole chapter) |
| Orbits and classical tests | ch11 §11.1 (p. 296): effective potentials, perihelion, light bending, lensing | ch12 (binaries), Hulse-Taylor ch09 §9.5 |
| Black holes | Buchdahl limit as the doorway, ch10 §10.6-10.7; horizon ch11 §11.2 (p. 315) | ch11 §11.3 (general BHs, Kerr), §11.4 (astronomy), §11.5 (Hawking); ch12 detections |
| Gravitational waves | Homogeneous solutions noted ch08 §8.3; ch09 §9.2 (p. 203) | ch12 (whole chapter), ch13 §13.4 (B-modes) |
| Cosmology | Λ introduced and parked ch08 §8.2; ch13 §13.1 (p. 415) | Standard sirens from ch09 §9.6 and ch12 §12.4 |
| Advanced topics | Kerr, ergosphere, Penrose process ch11 §11.3; Hawking radiation and BH thermodynamics §11.5; GW data analysis ch12 §12.3; inflation and quantum-gravity ideas ch13 §13.4 | None; no 3+1 or conformal-diagram chapters |

### Spiral and revisit structure

- **Flat first, then curved.** Covariant differentiation is fully rehearsed in the flat plane in polar coordinates, where Cartesian coordinates can check every result (ch05 §5.2-5.5). ch06 then transfers it "nearly unchanged" (ch05 role).
- **The MCRF idea recurs.** It appears first for particles (ch02 §2.3), then for fluid elements (ch04), and becomes the template for local inertial frames (ch05 §5.1, ch06 §6.2) (ch04 role).
- **Tensor calculus is rehearsed before GR needs it.** The closing remark of ch03 §3.9, that differentiating components works only because the basis is constant, is set up as the reason the covariant derivative is needed (ch03 role).
- **Conserved momenta are reused.** -p_0 and p_φ come from ch07 §7.4 and are reused for stellar redshift (ch10 §10.2), Schwarzschild and Kerr orbits (ch11) and cosmological redshift (ch13 §13.2).
- **Coordinate coverage.** The twin paradox is analysed as a coordinate-coverage failure (ch01 §1.13), and the idea returns at the horizon (ch11 §11.2).
- **Energy methods for orbits return in cosmology.** The effective-potential method of ch11 §11.1 comes back as the Friedmann equation read as an energy equation (ch13 §13.3).
- **Pressure as a source.** Active mass ρ + 3p (ch08 exercises) drives relativistic collapse (ch04 §4.8, ch10 §10.5) and cosmic acceleration (ch13 §13.3).
- **Toy systems carried through.** The spring-and-masses toy is used as detector, emitter and energy calibrator in turn (ch09 §9.3-9.5). Chirp mass and sirens (ch09 §9.6) become real data in ch12 and H_0 in ch13.

## 4. Conventions and notation (consolidated)

**Signature and units**
- Signature (-,+,+,+): η = diag(-1,1,1,1). Timelike intervals are negative, U·U = -1, p·p = -m² (ch01 notation; ch02; ch03 §3.1).
- c = 1 from ch01 §1.3, with time measured in metres. Consequences: energy and momentum in kg, pressure and energy density in kg/m³ (ch01 notation).
- G = c = 1 from ch08 §8.1, justified by metrology: GM for the Earth is known to nine figures, G to only four. The conversion is G/c² = 7.425e-28 m/kg (ch08 notation and gem). ch05 §5.1 already uses c = 1 silently (ch05 gap).
- ch12 normalizes formulas to one solar mass (about 4.93e-6 s) and a benchmark frequency (ch12 notation).

**Indices and typography**
- Greek indices run 0-3 and Latin indices 1-3. Coordinates are ordered (t, x, y, z) = (x⁰, …, x³) (ch01). In the Euclidean plane of ch05 §5.2-5.5, Greek indices take only 2 values.
- ch01 writes explicit Σ sums. The summation convention (one index up, one down) starts in ch02 §2.2.
- Typography: arrow over a symbol for a vector, tilde for a one-form, bold for a general tensor, bold for a three-vector (ch02, ch03 notation).
- A "has components in frame O" arrow is used, so a vector is never equated with a list of numbers (ch02 §2.1).
- Frames are marked by **bars on the indices**, never on the vector symbol. For the Lorentz matrix Λ^ᾱ_β, the velocity argument is how the upper-index frame moves as seen from the lower-index frame (ch02 notation).
- Comma for partial derivative, semicolon for covariant derivative. The derivative index comes last. The book does not use ∂_α notation (ch03 margin note, p. 65; ch05).
- Tensor type (M N) means M one-form slots (upper indices) and N vector slots (lower indices) (ch03 notation).
- Symmetrization brackets include the factor 1/2 (ch03).
- Orthonormal-basis components get hats, e.g. e_θ̂ (ch05 §5.5).

**Curvature signs (MTW)**
- Christoffel symbol Γ^μ_{αβ}: the upper index is the component, the first lower index goes with the differentiated vector, the last lower index is the direction of differentiation. It is symmetric in the lower pair (ch05, ch06 notation).
- Riemann tensor, with slots (component, transported vector, loop edges); the overall sign is flagged in a footnote as convention-dependent (ch06 §6.5, p. 158):
  R^α_{βμν} = Γ^α_{βν,μ} - Γ^α_{βμ,ν} + Γ^α_{σμ}Γ^σ_{βν} - Γ^α_{σν}Γ^σ_{βμ}
- Ricci tensor: R_{αβ} = R^μ_{αμβ}, contracting the first index with the third. Ricci scalar R = g^{μν}R_{μν}, positive for a sphere (ch06 notation; ch06 tutor note).
- Einstein tensor: G^{αβ} = R^{αβ} - ½g^{αβ}R. Field equations G^{αβ} + Λg^{αβ} = 8πT^{αβ}, with positive G^{00} for positive energy density (ch08 notation).
- Geodesic deviation: d²ξ^α/dτ² = R^α_{μνβ}U^μU^νξ^β. The tidal part is -R^i_{0j0}ξ^j (ch09 notation).

**Linearized theory and gravitational waves**
- h̄_{αβ} = h_{αβ} - ½η_{αβ}h.
- The gauge condition h̄^{μν}_{,ν} = 0 is called the "Lorentz gauge"; harmonic and de Donder are mentioned as synonyms.
- □ = -∂_t² + ∇², and the linearized field equation is □h̄ = -16πT (ch08 notation).
- Quadrupole I^{lm} = ∫T⁰⁰x^l x^m with no trace removed and no factor 3 (the MTW convention); the trace-free version is written with a bar.
- In binary formulas, ω is the orbital frequency and the wave is at 2ω (ch09 notation).

**Distinctive names and symbols**
- MCRF (momentarily comoving reference frame). Dust means pressureless matter.
- ρ is total energy density in the rest frame (MCRF), not rest-mass density; ρ₀ = mn (ch04 notation).
- For static spherical metrics: Φ and Λ in g₀₀ = -e^{2Φ}, g_rr = e^{2Λ}; mass function m(r) (ch10).
- Ẽ, J̃, Ṽ are per-unit-rest-mass quantities for massive particles; untilded symbols are used for photons. Effective potentials are plotted as V² (ch11 notation).
- Kerr: a = J/M, Δ, ρ², with the ergosphere (bounding surface) distinguished from the ergoregion (ch11).
- ch13 writes "Hubble-Lemaître" throughout and "Friedmann-Robertson-Walker" rather than FLRW. R(t) is the scale factor (ch13).
- Spelling and style: "spacetime", "world line", MTW-style (ch01).

**Internal inconsistencies the dossiers found**
- **Frame marks (ch01):** the same moving frame is marked with both tilde and overbar in nearby passages. A double bar marks a third frame and is easy to lose (ch01 gaps).
- **Hypersurface naming (ch03 §3.6, Exercise 3.21):** surfaces are named after their normal, so t = const is "timelike". Most texts name surfaces after their tangents and call that surface "spacelike" (ch03 gap).
- **Type labels and slot order (ch03):** the label switches from (M N) in §3.7 to (N M) in §3.8. Slot ordering for T and ∇T is inconsistent between Eqs. 3.61, 3.66 and R(p; A) (ch03 gaps).
- **"Magnitude" (ch02):** the word and the symbol A² are used for the signed quantity A·A (ch02 gap). appA instead defines |A| = sqrt(|A·A|) (appA notation).
- **Rapidity and Lorentz factor:** ch01 has no symbol for the Lorentz factor, uses v = tanh u, and never uses the word rapidity. ch02 introduces γ (ch01, ch02 notation).
- **Riemannian:** the word covers Lorentzian metrics too. ch06 writes (-g)^{1/2} in the text but |g|^{1/2} in the summary. Eq. 6.78's "every index gets a plus sign" holds only for a particular index layout (ch06 notation and gaps).
- **Symbol overloads, by unit:**
  - ch07: Φ versus φ for the Newtonian potential.
  - ch08: Λ is both the Lorentz matrix and the cosmological constant; bars mark index frames one page before a bar marks trace reversal.
  - ch09: ξ, φ, R, ψ, A each carry several meanings; M is each star's mass in the Hulse-Taylor section but total mass in §9.6.
  - ch10: p is both pressure and momentum; R, Λ and k are overloaded.
  - ch11: u, v, y and ε are redefined across subsections, with ε changing sign; tildes are dropped for part of the orbit discussion.
  - ch12: ε, M, N, T, Ω and ι are all overloaded; cross-correlation is called "convolution".
  - (ch07-ch12 notation and gaps)
- **ch12 detector response:** with the book's definitions the antenna functions F₊ and F× come out twice the conventional values (ch12 gap, from our own check).
- **appA:** switches to lower Latin indices, explicit sums, and a dot used for three different operations, all unlike the main text (appA notation).

## 5. Pedagogical signature

**Recurring explanatory moves**
1. **Geometry before algebra.** The Lorentz transformation arrives last in ch01, transcribed from axes already drawn (ch01 §1.5-1.9). Covariant-derivative results are drawn (ch05 Fig. 5.6) before being formalized.
2. **Define an object by what it does.** Tensors are fed arguments, and components are values on basis elements (ch03 §3.2-3.7). Partially filled slots manufacture new tensors: g(V, ) is a one-form (ch03 §3.6). The same reading gives the Riemann tensor as a four-slot machine (ch06 §6.5, p. 158) and detector response as d:h (ch12 §12.3, p. 375).
3. **Compute where it is easy, then promote the tensor equation.**
   - Fluid tensors: MCRF components first, then a covariant expression (ch04 §4.7, p. 100).
   - Metric compatibility and symmetric Γ: Cartesian first, then "it is a tensor equation" (ch05 §5.4).
   - Local-inertial-frame promotion for ∇g = 0, the commutator, geodesic deviation and Bianchi (ch06).
4. **Operational definitions.**
   - Simultaneity by light echo (ch01 §1.5).
   - Proper time as what a clock reads (ch01 §1.8).
   - Energy measured by an observer as -p·U_obs (ch02 §2.6).
   - Mass by weighing with distant orbits (ch08 §8.4, p. 195).
   - Areal radius (ch10 §10.1).
   - Luminosity distance by counting photons (ch13 §13.2, p. 431).
5. **Counting arguments before theorems.**
   - 16/10, 40/40, 80/100 Taylor coefficients predict 20 curvature components (ch06 §6.2, p. 149).
   - 10 − 4 = 6 physical metric functions (ch08 §8.2, p. 187).
   - Ten metric functions against four coordinate functions shows stationarity is special (ch07 §7.4).
   - Unknown polarizations against detector streams gives the null stream (ch12 §12.3, p. 388).
   - Counting γ factors reveals tensor rank (ch04 §4.4, p. 91).
6. **Provoke a paradox from a coordinate choice, then dissolve it with an invariant.**
   - TT gauge "nothing moves" (ch09 §9.2, p. 206).
   - Constant e_x with changing polar components (ch05 §5.3, p. 124).
   - The r = 2M coordinate singularity (ch11 §11.2).
   - Twin-paradox coverage gap (ch01 §1.13).
7. **Counterfactual and rival laws.**
   - (nU^α)_{;α} = qR² shows the equivalence principle is physics (ch07 §7.1, p. 173).
   - A perpetual-motion tower forces the redshift (ch05 §5.1, p. 112).
   - A Newtonian dark star as foil (ch11 §11.1, p. 297).
   - A Newtonian cosmology with boundary dependence (ch13 §13.1).
8. **Derive twice and check.** Coordinate position versus proper distance, metric integration versus geodesic deviation (ch09 §9.2-9.3). k-calculus and Doppler in ch01/ch02 check each other.
9. **Honesty about status.** Justified, not derived (ch08 §8.1). "No magic here" after the Newtonian limit (ch07 §7.2, p. 176). Labelled fictions (ch08 §8.3). Dated "mid-2021" observations (ch09, ch12, ch13).
10. **Scaling and dimensional reasoning in the astrophysics.**
    - Chandrasekhar mass from p ∝ ρ^{4/3} (ch10 §10.7, p. 284).
    - Luminosity bound c⁵/G (ch09 §9.5).
    - Scale-freedom giving chirp mass (ch09 §9.6).
    - Solar-mass-normalized formulas (ch12 §12.2).

**Preferred representations**
- Spacetime diagrams with invariant hyperbolae as rulers (ch01 §1.7).
- One-forms as stacks of surfaces and contour maps (ch03 Figs. 3.1, 3.3).
- The sphere and the 2D ant for curvature (ch06 §6.4).
- Effective-potential energy diagrams with lettered energy lines (ch11 Figs. 11.1-11.3).
- The ring of test particles for polarizations (ch09 Fig. 9.1).
- Embeddings: a three-sphere and a Minkowski hyperboloid for k = ±1 (ch13 §13.2, p. 427).
- ch03's dossier tags the book as index-free-abstract in definitions but components-first in computation.

**Analogies and thought experiments**
- Everyday and physical analogies are rated strong more often than weak:
  - soup on a train versus soup in orbit (ch01);
  - hiking across contours (ch03);
  - bras and kets (ch03, optional);
  - weight as the floor pushing you, and astronauts at ~300 km (ch07 §7.1, p. 172);
  - a cloud-covered Earth finding the Moon through tides (ch07);
  - the sea horizon and the pole of spherical coordinates (ch11);
  - GW detection as listening, standard sirens (ch09);
  - the Friedmann equation as particle energy, and rubber-band tension (ch13).
- The thought experiments are concrete and often numerical: Diana and Artemis at 0.96c aging 14 versus 50 years (ch01 §1.13), Einstein's tower and Schild's crests (ch05), Feynman's sticky beads (ch09), late-arriving gas and the teleological horizon (ch11 §11.3, p. 324), and a virtual photon pair straddling the horizon (ch11 §11.5).

**Figure style**
- Figures are line drawings, mostly spacetime diagrams (ch01 alone has 21 figures, 16 of them rated high priority for redesign), geometric constructions and potential plots.
- The first eight chapters are thinly illustrated: ch07 has no figures, ch08 has only tables, ch10 has one figure.
- The astrophysics chapters add observational data and images: EHT, supernova Hubble diagram, LIGO strain and noise curves (ch11-ch13).
- Captions carry real content and were sometimes lost in the reading-copy export, e.g. Fig. 3.1 (ch03 margin note, p. 61) and Fig. 2.3 (ch02 gap).

**Worked-example style**
- The book has no labelled "Example" headings: every dossier inventory shows 0 formal examples.
- Worked reasoning is embedded in the running text. The dossiers extracted 4-19 in-text examples per unit (ch09 and ch11 have 19 each), typically a short calculation followed straight away by a physical gloss or real numbers (Mercury, Hulse-Taylor, GW170817).
- Heavier algebra is often left as "it is easy to show", "fill in the algebra" or an exercise (ch01 §1.6, ch06, ch08 §8.3, ch09 §9.2).

**Exercise style**
- Roughly 360 exercises across the book: 21, 35, 34, 25, 22, 39, 10, 20, 56, 19, 43, 11, 25 for ch01-ch13. They are numbered N.M, with the section they support in parentheses (ch01, ch12 notation).
- They range from trivial index drills to extended problems.
- The exercise sets are **part of the exposition**: key derivations live there.
  - TT gauge construction (Exercise 9.5).
  - Linearized Riemann and Einstein tensors (Exercises 8.5-8.12).
  - Schwarzschild curvature proving r = 2M is regular (Exercise 11.21).
  - Horizon-regular Painlevé-Gullstrand and Eddington-Finkelstein charts (Exercises 11.23-11.24).
  - Killing's equation (Exercise 7.10).
  - Curvature of the sphere and cylinder (ch06).
- Several are computational: TOV integrators (Exercises 10.15, 10.17), numerical perihelion advance (Exercise 11.10), FFT operation counts (ch12). The notable-exercise lists in the ch10, ch11 and ch12 dossiers give the details.

**Margin notes and footnotes**
- Footnotes rather than side panels: references, cautions, forward pointers, humorous or historical asides (margin-note type counts in every dossier).
- Examples: why "dust" is called dust (ch04, p. 85); Einstein's heart palpitations over Mercury (ch11, p. 303); the Riemann sign-convention warning (ch06, p. 158).
- Several footnotes are missing from the text export and were recovered from page renders (ch01, ch02, ch09, ch12, ch13).

## 6. Best explanations by topic

| Topic | Unit / locator | Why this treatment is especially good |
|---|---|---|
| Relativity of simultaneity | ch01 §1.5, p. 8, Fig. 1.4 | The moving frame's x-axis is built from one light-echo experiment with no formula, so simultaneity is forced by the light postulate alone. |
| Invariance of the interval | ch01 §1.6, p. 9 | Structural proof: two quadratic forms that share a light cone must be proportional, and symmetry fixes the constant. It avoids circularity and previews GR-style reasoning. |
| Reciprocal time dilation | ch01 §1.7-1.8, pp. 15-20, Figs. 1.11, 1.14 | Hyperbola calibration plus clock counting: each observer uses two of its own clocks against one of the other's, so they are doing different experiments. |
| Twin paradox | ch01 §1.13, pp. 25-27 | Treated as a coordinate-coverage gap (Diana's two frames skip a triangle of Earth history) rather than an acceleration story. The idea pays off at horizons. |
| Four-velocity; observer-measured energy | ch02 §2.3, p. 41; §2.6, p. 48 | U as the rest frame's time basis vector gives U·U = -1 without computation. E = -p·U_obs builds the habit of writing invariant observables. |
| Minkowski orthogonality | ch02 §2.5, p. 45, Fig. 2.4 | "Orthogonal = mirror images about the light line" is drawable, explains the scissoring axes, and makes a null vector self-orthogonal. |
| One-forms and the gradient | ch03 §3.3-3.4, pp. 61-63, Figs. 3.1-3.3 | Stacked sheets pierced by an arrow, a contour-map walk with explicit crossing counts, and the gradient derived from dφ/dτ along a world line. |
| Why vectors and one-forms differ | ch03 §3.6, p. 69 | The Euclidean metric is the identity, so only the Minkowski minus sign exposes the difference. This answers "why was I never told?" |
| Stress-energy tensor | ch04 §4.3-4.4, pp. 89-92 | Density as flux through a t = const slice. Rank found by counting γ factors, and slot meaning by asking "which momentum component, which surface". |
| Symmetry of T, Euler equation, ρ + p as inertia | ch04 §4.5, p. 97; §4.7, pp. 100-102 | A shrinking spinning cube shows stress symmetry. T^{αβ}_{,β} = 0 split along and across U gives the first law and F = ma with inertia ρ + p. |
| Gravitational redshift and the equivalence principle | ch05 §5.1, pp. 112-117 | Perpetual-motion tower, then Schild's congruent crests, then the rocket reversal, then a free-fall Doppler check. Each step forces the next conclusion. |
| Christoffel symbols and the covariant derivative | ch05 §5.3-5.4, pp. 124-131 | Learned in flat polar coordinates where Cartesian checks exist. The e_x paradox motivates Γ, and deriving the polar Laplacian is the reward. |
| Local flatness | ch06 §6.2, p. 149 | Degree-of-freedom arithmetic predicts both the 6 Lorentz freedoms and the 20 curvature components before Riemann is defined. |
| Parallel transport and curvature | ch06 §6.4, p. 153, Fig. 6.3 | An arrow carried around a three-right-angle triangle on a sphere comes back turned 90°; the same loop in the plane does nothing. Euclid's "extend a line" becomes the geodesic condition. |
| Riemann tensor, geodesic deviation | ch06 §6.5, pp. 156-162 | Loop transport read as a four-slot machine, matched to the commutator of covariant derivatives, then read as tidal acceleration. |
| Why the Einstein tensor | ch06 §6.6, p. 163; ch08 §8.1, p. 184 | Divergence-freeness is forced by consistency with conservation (the Bianchi identities), not by experiment. |
| Equivalence principle as physics, not notation | ch07 §7.1, pp. 172-173 | A rival law that agrees with SR but predicts particle creation from curvature; weight recast as the floor pushing you; tides as the only real signature. |
| Conserved energy and angular momentum | ch07 §7.4, pp. 178-179 | A one-line symmetric-times-antisymmetric cancellation, with -p_0 unpacked into rest, potential and kinetic energy. |
| Motivating the field equations | ch08 §8.1-8.2, pp. 183-187 | Sources eliminated in order (ρ is one observer's, T⁰⁰ is one frame's, so all of T), then a count of physical degrees of freedom. |
| Linearized gravity, gauge | ch08 §8.3, pp. 189-191 | h is explicitly named a fiction; a non-tensor equation is read aloud; trace reversal explains the (1 - 2φ) spatial metric. |
| Mass of a relativistic body | ch08 §8.4, p. 195 | Mass defined by Kepler orbits in the far field, which settles the binding-energy and pressure puzzles. |
| GW effect on matter | ch09 §9.2, pp. 206-209, Fig. 9.1 | The TT gauge "proves" nothing moves, and proper distance overturns that. The wave is rewritten as a Newtonian tidal force in a local frame. |
| How interferometers detect | ch09 §9.3, pp. 222-223 | Differentiating the radar return time collapses the integral to endpoint values; the arms are placed inside the ring-of-particles picture as two clocks. |
| GW energy flux | ch09 §9.5, pp. 240-243 | Energy absorbed by a detector sheet (Feynman sticky beads), with detector parameters cancelling out. The same oscillator serves as detector, emitter and calibrator. |
| Chirp mass, standard sirens | ch09 §9.6, p. 250 | Scale-freedom: luminosity depends only on orbits remaining, and the chirp reveals the chirp mass. |
| Areal radius, static spherical metrics | ch10 §10.1-10.2, pp. 268-270, Fig. 10.1 | A throat surface with circles and no centre dislodges "r is distance"; each metric function gets an operational meaning before solving. |
| TOV and Buchdahl limit | ch10 §10.5-10.6, pp. 275-277 | TOV read factor by factor against Newtonian hydrostatics; the uniform-density star exposes the 4/9 limit as the doorway to collapse. |
| Chandrasekhar limit | ch10 §10.7, pp. 282-286 | Radius cancels in the scaling; the white-dwarf/neutron-star density gap is traced to the neutron-electron mass ratio; compactness orders everything. |
| Orbits, ISCO, photon sphere | ch11 §11.1, pp. 299-301, Figs. 11.1-11.3 | One energy diagram for particles and photons with lettered energy lines; ISCO at 6M as a property of the geometry alone. |
| Light bending factor 2 | ch11 §11.1, p. 312 | Slow planets feel only g₀₀; light feels g₀₀ and g_rr equally, so bending measures spatial curvature. |
| Nature of r = 2M | ch11 §11.2, pp. 315-320, Figs. 11.11-11.12 | Invariant questions modelled on the pole of spherical coordinates, closing light cones, then a guided eight-remark tour of the Kruskal diagram. |
| Event horizon as a global object | ch11 §11.3, p. 324, Fig. 11.13 | Late-arriving gas shows the horizon was already growing, which exposes the "snapshot" misconception. |
| Negative energy, Penrose process, Hawking | ch11 §11.3, p. 334; §11.5, pp. 347-349 | Negative relative to a local forward-in-time observer (ZAMO or infaller) unifies both effects; an uncertainty-principle estimate gives T ∝ 1/M and S = A/4. |
| Matched filtering and significance | ch12 §12.3, pp. 381-386 | A sampled sinusoid in white noise gives the √N gain, with resampling to show N counts cycles; false-alarm probabilities turned into counts per year. |
| Networks and antenna patterns | ch12 §12.3, pp. 375, 388; §12.4, p. 400 | Detector tensor contraction; counting unknowns against streams gives the null stream; Virgo's near-silence localized GW170817. |
| FRW geometry | ch13 §13.2, pp. 424-427 | A constant curvature scalar imposed on ch10's spherical Einstein tensor; k = -1 as a Minkowski hyperboloid on which boosts act as rotations. |
| Cosmological distances | ch13 §13.2, p. 431 | "How did distance get into v = Hd?": through flux. Photon counting gives two separate factors of (1+z). |
| Friedmann dynamics and Λ | ch13 §13.3, pp. 441-444 | Energy-equation reading with -k/2 as total energy; acceleration from ρ + 3p and tension as negative pressure; an Ω budget that must balance. |

## 7. Weaknesses and gaps

**Where novices stumble**
- **ch01:** assumes prior algebraic SR (ch01 background). Linearity of transformations is simply assumed. Key algebra is waved off as "easy to show" (ch01 gaps).
- **ch02:** the sign convention for Λ matrices is a real source of sign errors (Eq. 2.21 carries velocity -v implicitly) (ch02 gaps).
- **ch03:** the abstraction jump to multilinear maps, the terse §3.9, and the non-standard hypersurface naming (ch03 difficulty).
- **ch04:** §4.5 (defining T and S by integrating factor, the torque proof) and §4.7 (first genuine tensor calculus) (ch04 difficulty).
- **ch05:** §5.5 mixes hats, bars, tildes and primes (ch05 gap).
- **ch06:** the densest chapter. Long index derivations are compressed, local-frame promotion is overused so its limits are easy to forget, and there is **no explicit curvature calculation in the text**: sphere, cylinder and polar computations are all exercises (ch06 gaps).
- **ch08:** linearized Riemann and Einstein tensors and the h̄ gauge change are asserted and left to exercises. The chapter has no figures (ch08 gaps).
- **ch09 §9.4-9.5:** the math peak (Helmholtz and Gauss, virial identity, TT projection, planar sum with a convergence factor for an integral that does not converge) (ch09 difficulty and gaps).
- **ch11:** Kruskal coordinates are given without derivation, and the Hawking argument mixes local and conserved energies (ch11 difficulty and gaps).
- **ch13 §13.4:** a qualitative survey dense with unfamiliar numbers and particle-physics terms (ch13 difficulty).

**Terse or dated material**
- The observational material in ch09-ch13 is explicitly frozen at about mid-2021 (ch09, ch12, ch13 gaps). Examples:
  - SKA "perhaps by 2025"; pulsar timing arrays still seeking a detection (ch09). PTA evidence for a nanohertz background arrived in 2023, and LISA was adopted in 2024 (ch09, ch12 tutor notes).
  - The quoted WEP bound (10⁻¹³) predates MICROSCOPE's ~10⁻¹⁵ (ch07 gap).
  - M87* mass given as 2e9 solar masses (EHT found ~6.5e9); no Sgr A* image; ringdown called unmeasured (ch11 gap).
  - Chandrasekhar limit quoted as ~1.3 solar masses rather than ~1.44 (ch10 gap).
  - Nothing after mid-2021: no O4 events, JWST, DESI BAO or updated H_0 (ch12, ch13 gaps).
- Physically muddled passages to re-teach rather than repeat:
  - How the CMB measures H_0; the sound waves are said to travel in the dark matter (ch13 gap).
  - The claim that gravitational waves make no CMB temperature anisotropy (ch13 gap).
  - E/B modes treated as an ordinary vector field (ch13 gap).
  - Singularity theorems asserted without their energy conditions (ch13 gap).
  - The r-process described as fission (ch12 gap).
- Missing standard results:
  - The eccentric perihelion formula and the critical impact parameter 3√3 M (ch11 gaps).
  - The exact d_L(z) integral and the ΛCDM age (ch13 gaps).
  - Coloured-noise matched filtering (ch12 gap).
  - Named ADM/Komar mass (ch08 gap).

**Printed errors found (confirmed or corrected in the dossiers; selection)**
- **ch01:** Eq. 1.8 frame subscript; Exercise 1.12(b) factor applies to AE, not AC; Exercise 1.15(b) factor inverted.
- **ch02:** Planck's constant units printed as J s⁻¹; Exercise 2.1 lists C₃₃ twice.
- **ch03:** Eq. 3.36 attributes symmetry of g to Eq. 3.26.
- **ch04:** Eq. 4.21, momentum density printed ρvⁱ(1 - v²) instead of ρvⁱ/(1 - v²); Eq. 4.56 advective term printed (a·∇)a; moment of inertia scaling written as l² instead of l⁵.
- **ch05:** Fig. 5.2 labels both crest intervals Δt_bot.
- **ch06:** Eq. 6.67 index g_{βμ,βν} should be g_{βμ,σν}; step list of Eq. 6.62; "0" for O in Eq. 6.3.
- **ch07:** Eq. 7.22 sign; Eq. 7.33 p⁰ for p_0; ∂φ/∂τ in Eq. 7.15; ρ_α for p_α in Exercise 7.7(a).
- **ch08:** "0" for O in Eq. 8.60; Λ said to have been introduced "many years later" (it was 1917).
- **ch09:**
  - plane-wave Christoffel symbol printed 2ḟ/f instead of 2fḟ;
  - Eq. 9.58 argument sign; Eqs. 9.83, 9.106-9.107 sign and label slips; Eqs. 9.88, 9.92 and 9.124 missing factors;
  - Eq. 9.147 dP/dt conversion should be ~-7.6e-5 s/yr, not -7.2e-15;
  - Hulse-Taylor distance 8 kpc printed as 2.4e17 m (it is ~2.5e20 m).
- **ch10:**
  - proper-volume factor after Eq. 10.42;
  - sign of V dp_f/dV;
  - Eq. 10.85 prefactor;
  - binding factor printed sqrt(1 - M/R) instead of sqrt(1 - 2M/R) (8% should be ~16%);
  - Exercise 10.15 adiabatic index definition;
  - neutronization density too low.
- **ch11:**
  - Eqs. 11.34 and 11.36 have J² where J⁴ is dimensionally required;
  - Eq. 11.64 missing the inverse power;
  - isotropic-coordinate expansion slips;
  - Eq. 11.79 sign; Eq. 11.127 spurious dr² term;
  - "GALAXY" for the GRAVITY collaboration; Exercise 11.42 distance off by 10×.
- **ch12:**
  - sensitivity scalings printed with the wrong exponent sign (T^{1/2}, T^{1/4});
  - matched-filter slips in Eqs. 12.15, 12.18 and 12.19, and the variance formula;
  - factor 2 in the detector response (non-standard F₊, F×);
  - Eq. 12.29 missing factor 2; Eq. 12.47 missing ½;
  - Exercise 12.9 dimensionally inconsistent;
  - GW150914 date and times wrong (14 Sept, 09:50:45 UTC); Virgo joining O2 dated 2016 (it was 2017); O1 "16 months" (it ran about four);
  - Table 12.1 GW190521 distance labelled Mpc (it is Gpc).
- **ch13:**
  - Planck time given as GM_Pl/c² (dimensions of length);
  - nucleosynthesis at "~50 keV = n-p mass difference" (that difference is 1.29 MeV);
  - matter-radiation equality and decoupling numbers off (z ~ 2000 versus 1090);
  - 20-30 e-folds (standard ~50-60);
  - Eq. 13.15 sign;
  - Γ^θ_{φφ} sign in Exercise 13.14;
  - exercise cross-references mismatched;
  - string theory "eleven dimensions".
- **appA:** (1,1) entry of the 2×2 product printed A₁₂B₂₂ instead of A₁₂B₂₁.

**Omissions (beyond Section 1)**
- Tangent vectors as derivatives are postponed to ch05/ch06; ch02-ch03 use "things like Δx" (ch03 gap).
- Timelike geodesics maximizing proper time is not stated (ch06 gap).
- Strong equivalence principle and spinning/self-gravitating bodies are absent (ch07 gap).
- Causality problems of Eckart-type relativistic heat conduction go unmentioned (ch04 gap).
- Hubble sphere and superluminal recession are deferred to Davis and Lineweaver (ch13 gap).
- appA lacks transpose, trace, eigenvalues and det(AB) (appA gap).

## 8. Visual language

**What the figures do well**
- The ch01 spacetime diagrams make every SR result readable off the page: tilted axes built from echoes, hyperbolae as calibrated rulers, simultaneity lines hugging a fast world line (ch01 Figs. 1.4-1.16).
- A small set of iconic pictures each carries one core idea:
  - one-form sheets (ch03 Fig. 3.1);
  - basis-vector difference quotients (ch05 Fig. 5.6);
  - spherical triangle transport (ch06 Fig. 6.3);
  - ring of particles (ch09 Fig. 9.1);
  - lettered effective potentials (ch11 Fig. 11.1);
  - Kruskal diagram (ch11 Fig. 11.12).
- Later chapters show real data (LIGO strain, noise curves, supernova Hubble diagram, H_0 posterior), so theory is tied to observation.

**Limitations**
- All static line art; ch06-ch08 and ch10 are almost figure-free.
- Several figures depend on subtle labelling: Fig. 1.7's perspective drawing; point labels crowded in Fig. 1.15; T₀ bracket placement (ch01 gaps); the Fig. 5.2 label slip (ch05).
- Many dynamic ideas (boosts, orbits, wave strain, expansion) are exactly what static print handles worst.

**The 15 most redesign-worthy figures (ranked)**

| Rank | Unit | Label | Locator | App idea |
|---|---|---|---|---|
| 1 | ch11 | Figure 11.1 (with 11.2, 11.3a) | §11.1, p. 300-302 | Linked effective-potential explorer: drag the energy line and the J slider, watch r(φ) orbits and photon rays launch, and see the ISCO appear as peak and well merge at 6M. |
| 2 | ch01 | Figure 1.5(a)/(b) with 1.11 | §1.5, p. 8; §1.7, p. 15 | Boost "scissor" explorer: both axis pairs close about the light line as v changes, a frame-swap animation slides events along invariant hyperbolae, and unit ticks are calibrated with a Euclidean ruler for contrast. |
| 3 | ch11 | Figure 11.12 | §11.2, p. 320 | Interactive Kruskal diagram: hover for (t, r), launch observers and light signals, watch interior signals fail to escape, toggle a collapsing-star mask over regions III-IV. |
| 4 | ch03 | Figure 3.1 | §3.3, p. 61 | Sheet counter: a draggable arrow through a controllable family of planes with a live crossing count equal to p_α A^α, and a 3D mode. |
| 5 | ch06 | Figure 6.3 | §6.4, p. 153 | 3D globe: drag geodesic-triangle vertices, a tangent arrow walks the loop, and the net rotation is compared with angle excess and area; switch to a cylinder where the rotation vanishes. |
| 6 | ch09 | Figure 9.1 | §9.2, p. 210 | Ring (or lattice of rings) of test particles driven by adjustable h₊, h× and relative phase, with interferometer arms overlaid and a displacement/tidal-acceleration toggle. |
| 7 | ch01 | Figure 1.15 (with 1.16a) | §1.13, pp. 25-27 | Twin-trip simulator with a sweeping "now" line that jumps at turnaround and paints the uncovered triangle of Earth history. |
| 8 | ch11 | Figure 11.11 | §11.2, p. 319 | Coordinate switcher: the same radial light cones and infall world line morphing between Schwarzschild, Eddington-Finkelstein, Painlevé-Gullstrand and Kruskal charts, with a finite proper-time clock. |
| 9 | ch13 | Figure 13.4 | §13.3, p. 446 | Clickable Ω_m-Ω_Λ atlas linked to R(t), the Friedmann effective-potential curve and the Hubble-diagram curve for the chosen point. |
| 10 | ch13 | Figure 13.3 | §13.2, p. 437 | Live supernova Hubble diagram with sliders for H_0, Ω_m, Ω_Λ, a residual panel, and an "H_0 only shifts, never bends" demonstration. |
| 11 | ch04 | Figure 4.4 | §4.3, p. 89 | Rotatable (t, x, y) spacetime with a bundle of world lines piercing x = const and t = const sheets; a unit patch counts N^x and N⁰ as ⟨ñ, N⟩. |
| 12 | ch05 | Figure 5.3 | §5.1, p. 116 | Falling lattice versus falling dust beside a mass: residual relative accelerations reveal tidal stretching and squeezing, so only local inertial frames exist. |
| 13 | ch11 | Figure 11.13 | §11.3, p. 323 | Collapse-and-horizon builder in ingoing EF coordinates: find the boundary ray, then add a later shell and watch the horizon re-trace at earlier times. |
| 14 | ch12 | Figure 12.4 (with 12.3) | §12.3, pp. 374-376 | Globe of network sensitivity: place and orient detectors, scrub sidereal time, read F₊, F× and the arm-length change d:h for any sky direction and polarization angle. |
| 15 | ch10 | Figure 10.1 | §10.1, p. 268 | Reshapeable surface of revolution (bump, funnel, two-sheeted throat) comparing areal radius C/2π with proper distance, including a throat with no centre. |

Honourable mentions: ch02 Fig. 2.4, Minkowski protractor (§2.5, p. 45); ch06 Fig. 6.5, the loop derivation cell (§6.5, p. 156); ch09 Fig. 9.3, explorable interferometer with noise budget (§9.3, p. 225); ch13 Fig. 13.2, conformal-time horizon diagram (§13.2, p. 422).

## 9. Tutor guidance

**Learners and moments this approach suits**
- **Visual and geometric learners meeting SR and tensors for the second time.** The ch01-ch03 diagram- and machine-first style is at its best when a student can already push Lorentz transformations around but has no picture (ch01 role; ch03 tutor notes).
- **The "why do I need one-forms?" moment.** Use ch03 §3.3-3.6 (sheet picture, contour counts, Euclidean identity metric).
- **The first encounter with Christoffel symbols.** ch05's flat polar-coordinate route is gentler than starting on a curved manifold, and every result can be checked (ch05 difficulty notes).
- **The "is gravity a force?" moment.** Weight as the floor pushing, the cloud-covered Earth, the qR² rival law (ch07 §7.1).
- **Students who want astrophysical payoff.** ch09-ch13 tie formulas to real systems. ch12 is the vault's go-to unit for how GW data analysis actually reasons (matched filter, false alarms, null streams).
- **Less suitable for:**
  - learners who need worked computations before derivations: ch06 and ch08 leave key calculations to exercises;
  - learners wanting rigorous differential geometry;
  - anyone needing current observational numbers: ch09-ch13 are a 2021 snapshot.

**How the AI tutor should draw on it**
1. **Open with the book's hooks, and let the learner commit first.** From the tutor notes:
   - who decides whether firecrackers on a train are simultaneous (ch01);
   - does rotating graph paper change the arrow (ch02);
   - what does the dot product eat and return (ch03);
   - is a lab on Earth inertial (ch05);
   - how could an ant tell its surface is curved (ch06);
   - do two free marbles move when a wave passes (ch09);
   - where is the centre of the expansion (ch13).
2. **Follow the explanation orders recorded in the dossiers.**
   - ch01: postulates, then grid observers, then c = 1, then diagrams, then echo axes, then invariance, then cones, then hyperbolae, then dilation.
   - ch11: dark star, effective potential, ISCO and photon orbit, factor-2 bending, horizon diagnosis, Kruskal, Kerr, Hawking.
   - ch13: observations, then cosmic time, then FRW, then redshift, then distances, and only then Einstein's equations.
3. **Teach the reusable moves explicitly as named tools.**
   - "Feed it basis elements."
   - "Compute in the MCRF or local inertial frame, then promote only tensor equations." Quiz which equations may be promoted (ch06 tutor note: 6.67 no, 6.69 yes).
   - "Ask an invariant question."
   - "Count freedoms before computing."
4. **Supply the calculations the book leaves out.** Do the unit two-sphere Riemann computation (R_θφθφ = sin²θ, R = 2) in ch06. Work a numerical trace reversal with h̄⁰⁰ = -4φ in ch08. Show horizon-regular charts before Kruskal in ch11 (Exercises 11.23-11.24).
5. **Pre-empt printed errors.** When a learner works from the book, flag the known slips in Section 7 before they lose confidence in correct algebra. Every dossier's tutor notes ask for this.
6. **Translate conventions.** Warn about the non-standard hypersurface naming (ch03), the Lorentz-gauge name, the book's F₊/F× factor of 2 (ch12), "Hubble-Lemaître" and FRW, and signature and Riemann sign differences when a learner consults other texts. Recommend checking the sign of Ricci on a sphere (ch06 tutor note).
7. **Update and correct the astrophysics and cosmology.** Treat ch10 §10.7, ch11 §11.4, ch12 and ch13 §13.4 numbers as dated and cross-check against the vault's current data. Do **not** repeat the book's CMB H_0 mechanism or its claim of no GW temperature anisotropy (ch13 tutor note and gaps).
8. **Adapt depth.**
   - Beginners: stay on the t-x diagram with v = 0.6 (ch01); skip the quadratic-form invariance proof, the Helmholtz derivation (ch09) and the Buchdahl algebra (ch10).
   - Advanced learners: reproduce the invariance proof, code a TOV integrator (Exercises 10.15/10.17), derive Christoffel symbols for FRW (Exercise 13.14), and use the noise-weighted inner product (ch12).
9. **Treat appA as just-in-time support** for matrix products (ch02), the inverse metric (ch03), Jacobians (ch05) and metric determinants (ch06). Its skew-basis problem (A = 6e₁ + e₂) is a good seed for lowered indices (appA tutor notes).

## 10. Unit index

| Unit | Title | Printed pp. | Math | Concept | Novice | One-line summary | Verification |
|---|---|---|---|---|---|---|---|
| front | Front matter (prefaces to 3rd, 2nd, 1st editions) | xi-xv | none | none | none | Aims (accessible, not watered down), prerequisites, MTW conventions, course routes, edition changes (two GW chapters, observation-first cosmology). No JSON dossier; reading copy starts mid-way through the 3rd-edition preface. | n/a (reading copy) |
| ch01 | Special relativity | 1-32 | 2 | 3 | 4 | SR rebuilt from spacetime diagrams: light-echo axes, structural proof of interval invariance, hyperbola calibration, dilation and contraction, a late Lorentz transformation, and the twin paradox as coordinate coverage. | fixed |
| ch02 | Vector analysis in special relativity | 33-55 | 2 | 3 | 4 | Four-vector and index machinery (Λ, summation convention, basis transformation, η) applied to four-velocity, four-momentum, conservation, orthogonality, photons and Doppler. | fixed |
| ch03 | Tensor analysis in special relativity | 56-83 | 3 | 3 | 4 | Dot product reread as a bilinear machine; one-forms as stacks of surfaces, gradient, outer products, metric as vector-to-one-form map, (M N) tensors, index gymnastics, flat-space ∇T. | fixed |
| ch04 | Perfect fluids in special relativity | 84-110 | 3 | 3 | 3 | Dust to perfect fluid: number-flux N, one-forms as surfaces, T^{αβ} as a flux table and its symmetry, conservation, Euler equation with inertia ρ + p, 4D Gauss law, why T gravitates. | fixed |
| ch05 | Preface to curvature | 111-140 | 3 | 3 | 4 | Redshift, equivalence principle and tides force curved spacetime; the covariant-derivative toolkit (Γ, metric compatibility, Γ from g, noncoordinate bases) built in the flat plane with polar coordinates. | fixed |
| ch06 | Curved manifolds | 141-169 | 4 | 4 | 3 | Manifolds, local flatness by counting, ∇ via local inertial frames, proper volume, parallel transport and geodesics, Riemann from a loop, geodesic deviation, Bianchi identities and the Einstein tensor. | fixed |
| ch07 | Physics in a curved spacetime | 170-182 | 3 | 3 | 4 | Postulates linking geometry to measurement; WEP and EEP; comma-to-semicolon rule; Newtonian limit from weak-field geodesics; conserved -p_0 and p_φ from metric symmetries. | fixed |
| ch08 | The Einstein field equations | 183-201 | 3 | 4 | 3 | G + Λg = 8πT motivated from Poisson plus covariance plus conservation; geometrized units; degree-of-freedom count; linearized theory in Lorentz gauge; Newtonian limit fixes 8π; mass from the far field. | fixed |
| ch09 | Fundamentals of gravitational radiation | 202-266 | 4 | 4 | 3 | Plane waves and TT polarizations, tidal effects, bar/radar/interferometer detection, quadrupole formula, sticky-bead energy flux, Hulse-Taylor decay, chirp mass and standard sirens. | fixed |
| ch10 | Spherical solutions for stars | 267-295 | 3 | 3 | 3 | Static spherical metrics, TOV and mass function, Schwarzschild exterior and Birkhoff, uniform-density and Buchdahl interiors with the 4/9 limit, degenerate matter, Chandrasekhar limit, neutron stars and supernovae. | fixed |
| ch11 | Schwarzschild geometry and black holes | 296-359 | 4 | 4 | 3 | Effective-potential orbits (ISCO 6M, photon orbit 3M), perihelion shift, light bending and lensing, r = 2M and Kruskal coordinates, event horizons and theorems, Kerr and Penrose process, astrophysical black holes, heuristic Hawking radiation. | fixed |
| ch12 | Gravitational wave astronomy | 360-414 | 3 | 3 | 3 | Source classes with scaling laws; detector tensor and antenna patterns; noise, matched filtering, false alarms, coincidence, null streams, CW and stochastic searches; first LIGO-Virgo detections as case studies. | fixed |
| ch13 | Cosmology | 415-467 | 3 | 4 | 3 | FRW geometry from constant curvature, redshift and operational distances, H_0 and acceleration, Friedmann and acceleration equations with Λ as a fluid, then a mid-2021 survey of thermal history, CMB, dark matter, nucleosynthesis and inflation. | fixed |
| appA | Summary of linear algebra | 468-471 | 2 | 2 | 3 | Look-up sheet: vector spaces, bases, possibly indefinite inner products, matrices, determinants by cofactors, inverses; a skew-basis problem shows components depend on the whole basis. | fixed |
