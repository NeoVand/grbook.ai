---
type: book-profile
book: gifted-amateur
book_short: GA
title: General Relativity for the Gifted Amateur
authors:
  - Stephen J. Blundell
  - Tom Lancaster
edition: First edition (Oxford University Press; preface dated November 2024)
units: 54 dossier units (ch00-ch50, appB, appC, appD); front matter read separately; appA (further reading) and appE (answers) have no dossiers
signature: "A patient, conversational spiral through general relativity in short chapters: it teaches each tool first in components with friendly metaphors (slot machines, light-cone fields, effective potentials), cashes it in on physics, and later rebuilds the same tool rigorously with forms and field theory, all in -+++ signature with the MTW curvature sign."
units_needing_attention:
  - ch06  # says the true light bending is three times the equivalence-principle estimate (it is twice); conflicts with ch24
  - ch11  # eqn 11.38 drops the minus sign in geodesic deviation (repeated in ch13 margin eqn 13.4)
  - ch13  # geodesic-deviation sign; misleading explanation of why positive Lambda repels
  - ch17  # eqn 17.23 radiation coefficient; rho_c written inverted and unsquared; 2k/a for 2k/a^2
  - ch18  # pre-1998 framing (Lambda = 0 'standard models', 'missing mass'); factor error in eqn 18.35
  - ch21  # TOV eqn 21.28 missing its minus sign; eqn 21.35 missing square root; Birkhoff stated without 'vacuum'
  - ch26  # Kretschmann scalar printed as 12M^2/r^6 (should be 48); sign of cross term in eqn 26.26
  - ch28  # dimensionally wrong pair lifetime; heat-capacity formula does not follow; dated information-loss discussion
  - ch29  # horizon area integrand uses g not sqrt(det); summary calls the stationary limit the horizon
  - ch36  # printed Einstein components in eqn 36.81 wrong; inverted time vielbein in Example 36.6 margin
  - ch40  # swapped rule labels and sign slips in the Einstein-Hilbert variation (final result correct)
  - ch46  # historical dates wrong; J formula dimensionally wrong; circular-orbit formula applied to Hulse-Taylor
  - ch50  # calls the strong energy condition 'weak'
  - appB  # margin notes reverse the covariant/contravariant naming used in ch02
---

# General Relativity for the Gifted Amateur (GA): teaching profile

All claims below come from the verified unit dossiers in `knowledge/sources/gifted-amateur/chapters/`, the TOC, and the preface (`front`). Locators use unit ids plus section (§), figure, example or equation numbers and printed pages (p.). All 54 dossiers have the verification verdict **fixed**: an audit pass corrected them and none remain unverified. Everything is paraphrased. Where this profile adds its own judgement (rankings, reading paths, tutor advice), it says so.

---

## 1. Identity and audience

**Who it is for.** The preface (front) defines the "gifted amateur" as a reader who already has a physics background but is not an expert. The label is meant to encourage non-specialists to have a go at a hard subject. The book follows the authors' *Quantum Field Theory for the Gifted Amateur* in format and voice (front, p. v-vi). The Overture ends with a reader profile and a map of the Parts (ch00 §0.6).

**Assumed prerequisites** (collected from the dossiers' background lists):
- First- and second-year mechanics, including Lagrangians and central-force orbits (ch00, ch02 §2.4, ch20).
- Vector calculus with the divergence theorem (ch00 §0.4, ch38).
- Electromagnetism: Gauss's law, Poisson's equation, potentials and Maxwell's equations (ch00, ch13, ch42).
- Linear algebra: matrices, inverses, determinants and eigenproblems (ch02, ch05 §5.4, ch30).
- Hyperbolic functions and the calculus of variations, which ch01 §1.4 re-teaches.
- Special relativity is re-derived, but the ch01 dossier judges the chapter a brisk refresher and says a true first-timer would want more diagrams.
- Later parts assume more:
  - Thermodynamics (ch17, ch39, ch41).
  - Quantum mechanics: uncertainty, angular momentum, the particle on a ring (ch28, ch47, ch48, ch49).
  - Light topology (ch38, appC).

**Level.**
- The level is upper undergraduate, rising to early graduate in Parts V-VI.
- Maths ratings run from 2 (ch00, ch01, ch03, ch05, ch06, ch14, ch17, ch20, ch25, appB, appD) up to 5 (ch40).
- Novice-friendliness is 4 in Part I and in the Newtonian or orbit chapters (ch00, ch01, ch03, ch05, ch06, ch14, ch20, ch22, appD).
- It drops to 2 through most of Part V and VI (ch33-ch38, ch40, ch42, ch43, ch45, ch47, ch48, ch50). See section 10.

**Tone.**
- Conversational and often funny. Chapters carry literary epigraphs (for example Lucretius in ch50, Gibbon in ch14).
- The jokes range from the Death Star and Shakespeare (ch03) to Achilles and the tortoise and Brad Pitt (ch25). ch28 has a spoof newspaper and a steak cooked by acceleration.
- The authors are open about limits:
  - They say where a heuristic falls short (ch06).
  - They quote the Kerr metric because deriving it is famously hard (ch29 margin essay).
  - They call finding connection forms guesswork (ch36).
  - They call one derivation untidy (ch39 note 12).
  - They call the flat-background picture a fiction (ch45).

**Length and granularity.**
- There is an Overture (ch00) and 50 chapters in six Parts (TOC), followed by Appendices A-E and an index at p. 614.
- The printed text runs to about 613 pages.
- Chapters are short, typically 6-17 pages (ch09 and ch14 are 6-7 pages; ch39, ch40, ch46 and ch49 are 17-20).
- The dossiers record 540 formal worked examples and about 302 end-of-chapter exercises.
- The dossiers count 1,032 margin notes. By type: clarification 261, technical detail 235, forward pointer 132, backward pointer 113, caution 87, biography 60, reference 56, humour or aside 52, history 36.

**What it deliberately omits or only gestures at** (per the dossiers):
- **Curved-spacetime QFT.** No quantum field theory in curved spacetime: Hawking radiation is argued heuristically and the exact result is quoted (ch28).
- **Metrics quoted, not derived.** The Reissner-Nordström and Kerr metrics are simply stated (ch29).
- **Global causal methods.** These are mostly left out. ch50 previews the Penrose-Hawking-Geroch style in a compressed proof sketch.
- **Uniqueness of the field equation.** Not argued: no Lovelock theorem (ch13).
- **Boundary term.** The Gibbons-Hawking-York term is never mentioned (ch40).
- **3+1 methods.** They appear only in exercises: projection tensors and Gauss-Codazzi in ch30 Exercises 30.7-30.8.
- **Inflationary perturbations.** No e-folds, slow-roll parameters or perturbation spectra (ch41).
- **Detector physics.** No antenna patterns and no detector response beyond a face-on + wave (ch46).
- **Non-perfect fluids.** Viscosity and heat flux are dropped (ch39).
- **Modern cosmology.** Observational cosmology appears only as a short Λ-CDM status report (ch49 §49.8). The zoo of model universes in ch18 keeps the pre-1998 framing.

---

## 2. The authors' stated goals and philosophy

Paraphrased from the preface (front) and the organizing material in ch00, ch06, ch14 and ch34:

1. **Access.** Everyone should get to engage with general relativity. The authors hold that its concepts rest on simple ideas from the physics of fields. What is hard is the machinery, which needs mathematics many physics students have not met. The payoff justifies the effort, and GR deserves a more central place in the curriculum (front).
2. **Patience over prestige.** The authors remember finding the material hard. They aim to be a gentler, more illuminating guide than the large standard tomes (front).
3. **Format commitments carried over from QFTGA** (front):
   - Short, digestible chapters.
   - Mathematical steps spelled out in worked examples.
   - Hand-drawn figures.
   - New in this book, at readers' request: many problems with worked solutions (Appendix E answers selected problems).
4. **Planned spiral** (front):
   - Parts I-II carry the reader to the field equations and then outline their main consequences.
   - Parts III and IV work out cosmology and then orbits and black holes in detail.
   - Part V gives a more mathematical treatment of geometry for readers with the appetite.
   - Part VI returns to field theory. It frames GR as a classical field theory and looks toward quantum gravity.
5. **Non-linear reading is allowed.** The first double-ruled skip box in the book (ch00, p. 9) says the chapters need not be read in order. Later boxes mark optional chapters or sections:
   - ch09, ch10 from §10.2, ch19, ch26, ch30 and ch33 §33.4.
   - ch34, ch38, ch39, the fluid derivation in ch40, ch43 and ch47.
6. **Programme statements inside the text.**
   - ch06's six numbered "Lessons" are the contract Part II fulfils.
   - ch14 is framed as the view from the summit after the climb to the field equation.
   - ch34 offers a one-sentence definition of GR as the destination of the geometry part: a manifold with a Lorentzian metric whose curvature is sourced by matter, drawn as a four-level structure.

---

## 3. Architecture

### 3.1 Parts and chapter flow (dependency outline)

```
ch00 Overture (vocabulary, Newtonian field gravity, units)
│
Part I  Geometry and mechanics in flat spacetime (p.11)
│  ch01 SR as geometry → ch02 4-vectors, index machinery, action
│  → ch03 coordinates & bases → ch04 1-forms, tensors, dust T
│  → ch05 metric field, light cones, volume element
│
Part II Curvature and general relativity (p.67)
│  ch06 equivalence + covariance ("Lessons 1-6")
│  → ch07 connection, parallel transport → ch08 geodesics
│  → ch09 Γ from metric (optional recipe) → ch10 measurement frames (optional from §10.2)
│  → ch11 Riemann, Ricci → ch12 energy-momentum tensor → ch13 field equations
│  → ch14 triumphs (Newtonian limit derived; previews of GWs, orbits, BHs, cosmology)
│
├── Part III Cosmology (p.157)                ├── Part IV Orbits, stars, black holes (p.217)
│   ch15 cosmological principle, Univ. 0-1    │   ch20 Newtonian orbits (template)
│   → ch16 Robertson-Walker, redshift         │   → ch21 Schwarzschild + TOV → ch22 motion, Killing recipe
│   → ch17 Friedmann → ch18 Universes 2-11     │   → ch23 orbits, perihelion → ch24 photons, lensing, shadow
│   → ch19 Penrose diagrams, horizons          │   → ch25 black holes → ch26 singularities, EF coords
│        (language reused in Part IV) ─────────┼──→ ch27 Kruskal → ch28 Hawking → ch29 RN, Kerr
│
Part V  Geometry (p.307): rigorous second pass
│  ch30 classical curvature → ch31 vectors as derivatives → ch32 forms
│  → ch33 exterior & Lie derivatives, Killing → ch34 connection, torsion, ∇g=0
│  → ch35 Riemann revisited, Weyl → ch36 Cartan → ch37 Hodge, volume form → ch38 Stokes
│
Part VI Classical and quantum fields (p.411)
   ch39 fluids → ch40 Lagrangian field theory, Einstein-Hilbert, Noether → ch41 inflation
   → ch42 electromagnetism (indices, then forms) → ch43 charge conservation & Bianchi
   → ch44 gauge fields as connections → ch45 linearized gravity → ch46 gravitational waves
   → ch47 gravitons → ch48 Kaluza-Klein → ch49 routes to quantum gravity, Λ-CDM → ch50 Big-Bang singularity
Appendices: A reading, B conventions, C manifolds & bundles, D embedding, E answers
```

**Structural notes.**
- Cosmology (Part III) comes *before* the Schwarzschild solution (Part IV). The first exact use of the full field equation is therefore de Sitter space (ch15), not a star. This order is uncommon among GR texts (profile's judgement).
- Parts III and IV both depend only on Part II plus ch10's orthonormal frames. Part IV reuses ch19's Penrose-diagram language (ch25, ch27, ch29).
- The digest's part field is empty for ch24, ch43 and ch49, although the TOC places them in Parts IV, VI and VI. This is a metadata gap, not a content issue.
- The briefing that commissioned this profile described "Parts VI-VII". The TOC shows six Parts only: fields, gauge theory, waves, quantum gravity and the singularity theorem all sit in Part VI.

### 3.2 Where the pivotal ideas first appear

| Idea | Preview | First real treatment | Later passes |
|---|---|---|---|
| Special relativity | ch00 §0.1 (principles in shaded boxes, light cones) | ch01 §1.2-1.4 (interval, boost as hyperbolic rotation, twin paradox by variational calculus) | ch02 (4-vectors), ch10 (observer frames) |
| Vectors, 1-forms | ch01 events and intervals | ch02 (vectors), ch04 §4.1-4.2 (1-forms as stacks of surfaces) | ch31-ch32 (derivative operators, p-forms), appC |
| Tensors | ch00 (bold G, T named) | ch04 §4.3-4.4 (slot machines, transformation law) | ch31 §31.4-31.5 (slot operations) |
| Equivalence principle | ch00 juggler (Fig. 1), ch01 altitude remark | ch06 §6.1 (Example 6.1, tidal test Fig. 6.2) | ch08 (inertial forces), ch11 §11.2 (tides) |
| Manifolds and metric | ch00 §0.3 (metric as field) | ch05 (metric field, line element, light cones); ch07 (manifold named) | ch31 §31.1, appC (charts, atlases), appD (embedding) |
| Local flatness | ch05 §5.4 (street-map picture) | ch06 (value and slope matched, curvature not) | ch35 §35.2 (Riemann normal coordinates) |
| Connection, parallel transport | ch03 (derivatives of basis vectors) | ch07 §7.2-7.5; ch08 (geodesics); ch09 §9.2 (Christoffel formula) | ch34 (axioms, torsion, ∇g = 0), ch36 (connection 1-forms), ch44 (gauge connection) |
| Curvature | ch00 (non-parallel lines), ch03 Exercises (circle deficit, Girard) | ch11 §11.1-11.6 (loop derivation, symmetries, Ricci) | ch30 (Gauss), ch35 (operator, Weyl), ch36 (Cartan), ch43 (Bianchi) |
| Stress-energy | ch00 word equation | ch04 §4.5 (dust as J ⊗ p); ch12 (perfect fluid, div T = 0) | ch39 (fluid mechanics), ch40 (Hilbert T), appC Example C.10 (from diffeomorphism invariance) |
| Field equations | ch00 §0.3 word equation | ch13 §13.3-13.4 | ch14 §14.1 (Newtonian limit), ch40 §40.4 (action), ch45 (linearized) |
| Schwarzschild | ch06 §6.5 (g_00, GPS), ch14 §14.3 | ch21 (derivation, TOV, operational coordinates) | ch22-ch24 (motion, orbits, photons), ch36 Example 36.6 (Cartan) |
| Orbits and tests | ch00 (Mercury, GPS); ch06 §6.5 (redshift); ch08 §8.4 (Shapiro delay) | ch23 §23.3 (perihelion 6πM/r0, Mercury); ch24 §24.1 (4M/b bending) | ch46 §46.4 (Hulse-Taylor) |
| Black holes | ch00 (dark star), ch05 (baby EF cone tipping) | ch25 (horizon, tortoise coordinate, collapse) | ch26 (EF), ch27 (Kruskal), ch28 (Hawking), ch29 (RN, Kerr) |
| Gravitational waves | ch14 §14.2 (ring of masses, wave ladder) | ch45 (Lorenz gauge wave equation) → ch46 (TT gauge, quadrupole, GW150914) | ch47 (spin 2) |
| Cosmology | ch14 (RW metric preview) | ch15-ch19 | ch41 (inflation), ch49 §49.8 (Λ-CDM), ch50 (singularity theorem) |
| Advanced topics | ch00 (classical vs quantum remark) | ch40 onward: Lagrangian fields (ch40), EM (ch42), gauge (ch44), gravitons (ch47), Kaluza-Klein (ch48), strings, loop quantum gravity, AdS (ch49) | |

### 3.3 The spiral: explicit debts and repayments

The book often uses a result early "on trust" and proves it later, sometimes with a grey signpost saying so (ch34):

- **Weak-field metric.** Quoted as eqn 5.22 (ch05) → derived by undoing the trace reversal in ch14 Example 14.2 → redone with gauge machinery in ch45.
- **Transformation law of Γ and tensor covariant derivatives.** Quoted in ch07 (eqns 7.11, 7.34, 7.40) and used in ch12 (eqn 12.37) → proved in ch34.
- **Killing-vector recipe for conserved quantities.** Given without proof in ch22 → justified in ch33 §33.5.
- **Geodesic deviation equation and Riemann component count.** Stated in ch11 → derived index-free and counted in ch35.
- **Local flatness.** Claimed in ch06 → Riemann normal coordinates in ch35 §35.2.
- **Bianchi identity.** Quoted as a tool in ch13 → derived from "the boundary of a boundary is zero" in ch43.
- **Rindler spacetime.** Toy metric in ch05 → exercise in ch09 → coordinate-singularity rehearsal in ch26 → Kruskal analogy in ch27 → Unruh effect in ch28.
- **Energy-momentum tensor.** ch04 → ch12 → ch39 → ch40 → appC.
- **Newtonian orbits.** ch20 is the explicit template recycled line by line in ch22-ch24.
- **Cosmological singularity.** a = 0 found in ch16 and ch18 → shown to be generic in ch50.
- **Gravitational waves.** Previewed in ch14 → full treatment in ch46.

---

## 4. Conventions and notation (consolidated)

**Signature.** (−,+,+,+) throughout, with η = diag(−1,1,1,1). Timelike vectors have negative squares and u·u = −1 (ch01, ch02, appB). ch01 compares the choice of sign convention to driving on the left or right.

**Units.**
- SI in ch00-ch01 (called "real-world" units).
- c = 1 from ch02, p. 23.
- G = c = 1 from Part III on. M then stands for GM/c², a length (ch15, ch21, ch22).
- Exceptions:
  - ch20 keeps G explicit.
  - ch28 keeps ħ and k_B.
  - ch48 uses ħ = c = 1, with actions made dimensionless by Planck-mass powers.
  - Electromagnetism uses Heaviside-Lorentz units: no ε₀ or μ₀ (appB, ch42).
- One conversion rule handles everything: multiply a quantity of SI dimension L^n T^m M^p by c^m (G/c²)^p, with a table (ch00 §0.6).

**Index and typography conventions.**
- **Index alphabets.** Greek indices run 0-3 and Latin indices 1-3. 3-vectors carry arrows; 4-vectors and tensors are bold; 1-forms are bold with a tilde; orthonormal-frame indices carry hats (ch10, appB).
- **Frames and vielbeins.**
  - Frame changes are marked by priming the index, not the symbol: X^{μ'}, e_{α'} (ch02).
  - The Lorentz matrix Λ^{μ'}_ν and its inverse Λ^ν_{μ'} are told apart only by where the prime sits (ch02, ch03, ch04).
  - Vielbeins are written (e_μ)^{ν̂}, following Hartle (ch10). For a diagonal metric, the orthonormal frame follows by the square-root rule (ch10, appB).
- **Valence.** (m,n) counts upper (1-form) slots, then lower (vector) slots. Empty-slot notation T( , ) shows how many arguments a tensor takes. Angle brackets ⟨σ, v⟩ denote the pairing (ch04, ch31, appB).
- **Derivatives.** A comma is a partial derivative and a semicolon a covariant one (ch07). "Comma goes to semicolon" is the named upgrade rule (ch12). D/dλ is the covariant derivative along a curve. appB insists on writing (Dv/dτ)^α, never Dv^α/dτ.
- **Symmetrization and wedges.** Round and square brackets on indices (symmetrize, antisymmetrize) carry 1/2. The wedge product has **no** 1/2: u∧v = u⊗v − v⊗u. p-forms are expanded with 1/p!, or with vertical bars restricting to ordered sums (ch31, ch32, appB).
- **Connection index order.** Γ^λ_{αμ} with the derivative (direction) index first: ∇_α e_μ = Γ^λ_{αμ} e_λ (ch07 eqn 7.6, ch34, ch35, ch36).
- **Levi-Civita and Hodge.**
  - ε_{0123} = +1, so ε^{0123} = −1 (ch37, ch38, ch42).
  - The Hodge star maps multivectors to forms and forms to multivectors. The input fills the *first* slots of the volume tensor (ch37). Most texts map p-forms to (n−p)-forms, often contracting into the last slots.
- **Linearized gravity.**
  - x' = x + ξ gives h → h − 2ξ_(μ,ν) (ch45); many texts use the opposite sign.
  - An overbar marks trace reversal, and the d'Alembertian is written ∂², not □ (ch14, ch45).

**Curvature signs** (MTW-type, and consistent across ch11, ch13, ch15, ch35, ch45):
- Riemann: R^α_{βμν} = ∂_μ Γ^α_{νβ} − ∂_ν Γ^α_{μβ} + ΓΓ terms. The first lower index is the transported vector and the last two label the loop plane.
- As an operator: R(u,v) = [∇_u, ∇_v] − ∇_[u,v] (ch35).
- A sphere has positive curvature (ch30, ch36).
- Ricci: R_{μν} = R^α_{μαν}, contracting the first and third slots.
- Einstein equation: G_{μν} = 8πT_{μν} − Λg_{μν}. Positive Λ is positive vacuum energy and repulsive (ch13, ch15, ch17).
- Geodesic deviation: D²ξ/dτ² = −R(·, u, ξ, u), as in ch11 eqns 11.6 and 11.39.

**Distinctive names and devices a learner will meet only here** (or used in a non-standard sense):
- "Linear slot machines" (ch04 title).
- "Lessons 1-6" (ch06).
- "Steps I-V", also called the "five-point method" (ch09).
- "Universe 0" to "Universe 11" for numbered models (ch15, ch18).
- "Extended present" for the region outside the light cone (ch01).
- "Halfway-house" coordinates for Eddington-Finkelstein (ch26).
- "Rain coordinates" in exercises (ch25).
- "Ideas 1-3" and a six-box flowchart for Cartan's method (ch36).
- "Rules 1-3" for the metric-variation identities (ch40).
- "Method I / method II" for induced metrics (appD).
- "Maxwell tensor" for ⋆F (ch42).
- Ẽ, L̃ for energy and angular momentum per unit rest mass, script E for effective energy, and W_eff (photons) versus V_eff (massive particles) (ch22-ch24).
- "Proper motion" for peculiar velocity (ch15).
- "Spherical/flat/hyperbolic" preferred over "closed/flat/open" (ch16).
- **Non-standard usages to flag for learners:**
  - "Affine versus non-affine connection" for what is really a property of a curve's parametrization (ch34).
  - "The extrinsic curvature" for the trace k₁ + k₂, which is twice the mean curvature (ch30).
  - Older weak and strong equivalence-principle terminology (ch06).

**Internal inconsistencies the dossiers found.**
1. **Geodesic deviation sign.** Present in eqns 11.6 and 11.39, missing in eqn 11.38 and in ch13 margin eqn 13.4.
2. **Light bending split.** ch06 says the equivalence-principle estimate is one third of the truth; ch24 says GR gives twice the Newtonian value. The standard split is half from g_tt and half from spatial curvature. ch23's exercises assign perihelion precession one third to space and two thirds to time, a split that depends on coordinates.
3. **Connection index order.** Swapped on ch07 p. 89 relative to eqn 7.6. ch10's Exercise 10.2 and its Appendix E answer treat the other lower index as the derivative direction.
4. **Covariant/contravariant naming.** Reversed in appB margin notes 4 and 6 relative to ch02 §2.2.
5. **Wedge normalization.** An extra 1/2 in ch36 Example 36.2 versus ch34 eqn 34.38.
6. **Null-coordinate letters.** They swap roles between ch26 (lowercase logarithmic, capital exponentiated) and ch27 (the reverse). ch26 also reuses U, V with two meanings.
7. **"de Sitter" label.** Applied to the general spatially flat Robertson-Walker family with arbitrary a(t) (ch16, ch36 Example 36.5).
8. **Name clash on "trace-reversed".** ch35 eqn 35.37 calls R_{μν} − ¼Rg_{μν} "trace-reversed" and names it G, clashing with the Einstein tensor.
9. **Robertson-Walker Ricci component.** The margin prints 2k/a instead of 2k/a² in both ch16 and ch17.
10. **Symbol overloads.**
    - G: Einstein tensor, Newton's constant and a Green's function (ch13).
    - K: three meanings (ch30).
    - u: 4-velocity and specific internal energy (ch39).
    - η: Minkowski metric and conformal time; τ: proper time and conformal time (ch19).
    - l: two unrelated lengths (ch48).
    - a: Landau coefficient and scale factor (ch41).
    - T: tensor and its trace (ch47).
11. **Second covariant derivative order.** ch40 footnote 13 differentiates in the opposite order to ch50's stated convention.
12. **Wrong-signature tetrad.** ch10 Exercise 10.6 uses Newman-Penrose normalizations belonging to the (+,−,−,−) signature.

---

## 5. Pedagogical signature

### 5.1 Recurring explanatory moves

- **Propose, then refute.** A plausible wrong theory is built and then killed by a consistency test, so the right answer arrives as a repair.
  - ch06: Poisson's equation promoted to a wave equation fails because density is not a scalar.
  - ch13 §13.3: R^{μν} = κT^{μν}, labelled an "incorrect guess", is destroyed by the contracted Bianchi identity plus div T = 0.
  - ch20 exercises and ch42 Exercise 42.13: flat-spacetime scalar gravity fails to bend light.
  - ch47: the trace coefficient α is fixed by demanding exactly two polarizations.
- **Flat control case before curvature.**
  - Plane polar coordinates carry every new idea in ch03. The same flat plane shows nonzero Γ with zero curvature in ch07 §7.2, ch11 and ch36 Example 36.1.
  - ch05 shows one flat spacetime in three coordinate systems.
  - ch26 rehearses horizon removal on flat metrics in disguise (a 1/t⁴ metric, then Rindler).
- **The Newtonian mirror.** Relativistic results are arranged to look like their Newtonian counterparts, with the difference isolated.
  - ch00 recasts Newtonian gravity in field language ending at Poisson's equation, the explicit target.
  - ch17 opens with a Newtonian Friedmann derivation.
  - ch20 is a template chapter; ch22-ch24 point to one extra term (−ML²/r³, 3u²).
  - ch35 runs a Newtonian shadow derivation whose steps match the covariant proof.
  - ch39 builds every fluid law twice: Newtonian, then relativistic.
- **Electromagnetism as template for gravity.**
  - ch13 Fig. 13.2: one-way versus loop solving.
  - ch42 notes every pointer forward to gravity. ch43 runs parallel scroll panels for dF = 0 and dR = 0.
  - ch44 ends on a dictionary table linking Γ, A and the connection.
  - ch45 matches EM step by step. ch46 replays EM plane waves with one more index. ch47 does photon exchange first.
- **Pick the easy frame, then trust invariance.** The twin paradox is computed in the Earth frame (ch01 §1.4). Invariants are evaluated where trivial: −X·u, u·v = −γ (ch02 §2.3). The energy-momentum tensor is built diagonal in the rest frame (ch12 §12.2).
- **Bracketed word equations before symbols.**
  - The Einstein equation as "curvature = matter energy" (ch00).
  - Covariant derivative = change in vector minus change due to coordinates (ch07 eqns 7.1, 7.4, 7.27-7.30; reused for the gauge derivative in ch44 eqns 44.13, 44.17).
  - Loop change = curvature × vector × area (ch11 §11.3).
- **Boxed-arrow dependency maps.** [dg] → [Γ] and [dg, d²g] → [R] set expectations before derivations (ch07, ch11).
- **Numbered checklists and recipes.**
  - Lessons 1-6 (ch06); Steps I-V with each example line labelled by step (ch09).
  - The three-step Killing recipe (ch22); Ideas 1-3 plus the flowchart (ch36).
  - Rules 1-3 and Steps 0-V (ch40); method I and method II (appD).
- **Answer first, then earn it.**
  - The Penrose triangle is shown before the map is derived (ch19 Fig. 19.5(b)).
  - The Schwarzschild metric appears on page one (ch21).
  - The geodesic deviation equation is boxed before its derivation (ch35).
  - The generalized Stokes theorem is stated at the start (ch38).
  - The wished-for gauge condition is stated before it is justified (ch45).
- **Staged failures.**
  - V = 1/v blows up the metric, forcing a conformal factor (ch19).
  - A local phase change spoils invariance until a gauge field repairs it (ch44).
  - "The mass doesn't move" in TT coordinates, rescued by proper distance (ch46).
  - The hyperbolic plane needs an imaginary slope until one sign of the host metric is flipped (appD).
- **Numbered model zoo.** Universes 0-11 change one ingredient at a time and are compressed into a k-by-Λ grid (ch15, ch18 Fig. 18.10).
- **Straw-man list with scheduled demolition.** ch01 numbers four common-sense beliefs and margin notes declare each dead as the refuting result is derived.
- **Debt signposts and permission to skip.** Repayments are named (ch14, ch33, ch34). Curly-arrow skip boxes are frequent (see section 2).

### 5.2 Preferred representations

1. **Components first, index-free second.**
   - Parts I-II work in components with slot-machine language. Part V redoes vectors as derivatives (ch31), p-forms (ch32), ∇ axioms (ch34) and the curvature operator (ch35).
   - ch42 derives electromagnetism twice: indices, then forms (§42.4).
2. **The slot machine.** A tensor is a box with slots and a crank that outputs a number (ch04 Figs. 4.5-4.6).
   - Observer measurements come from feeding u into slots: E = −p̃(u), n = −J̃(u), energy density T(u,u) (ch04 §4.5, ch12 §12.1).
   - The same device recurs for slot surgery in ch31, for volume by slot filling in ch37 (σ(u) gives measured volume), and in appB.
3. **Light-cone fields.** Parade-ground versus drunken cones (ch00 Fig. 3); ds² = 0 solved locally to draw cones (ch05 §5.3). Reused for horizons (ch25 Fig. 25.2, ch26 Fig. 26.5) and Kerr (ch29 Fig. 29.6).
4. **Effective potentials with an energy line.** Classical orbits (ch20 Figs. 20.5-20.8); Schwarzschild orbits and photons (ch14 Fig. 14.2, ch22 Fig. 22.3, ch23 Fig. 23.2, ch24 Fig. 24.2). Also the scale factor (ch18 Fig. 18.9), Kerr (ch29), the inflaton (ch41) and the AdS boundary bounce (ch49).
5. **Sheets, tubes and cells.**
   - 1-forms as surface stacks pierced by arrows (ch04 Fig. 4.3); 2-forms as tube lattices (ch32 Fig. 32.1); d adds a sheet family (ch33 Fig. 33.1).
   - Integration as counting (ch38); the magnetic field as tube circulation (ch42 Fig. 42.2).
6. **Penrose diagrams.** Built on the Einstein static cylinder as a common canvas (ch19). Reused for collapse (ch25), Kruskal (ch27 Fig. 27.9), evaporation (ch28), RN and Kerr towers (ch29) and the horizon problem (ch41 Fig. 41.1).
7. **Orthonormal frames and vielbeins.** Hatted components are "what a lab measures" (ch10), used through ch12, ch15-ch17, ch21-ch25 and ch36.

### 5.3 Analogies and thought experiments

The book is analogy-dense. Many are rated "strong" in the dossiers:
- **Relativity and frames.** A juggler on four kinds of train (ch00). Rotation versus boost (ch01).
- **Vectors in curved space.** An arrow from New York to Tokyo tunnels through the Earth (ch03). A tangent arrow pointed north from Oxford ends in mid-air above Durham (ch04).
- **Curvature and connection.** Ants on a football judge parallelism from inside (ch07). A swingball game (ch08). Synge's cliff: blame the geodesic, not gravity (ch09). Tidal spring constants (ch11). A tin can versus a ball, and shoelaces that can always be straightened (ch30). A transparent Sun lensing light (ch35).
- **Black holes.** Achilles and the tortoise for r* (ch25). Kruskal is inertial and Schwarzschild accelerated, like Minkowski versus Rindler (ch27 eqn 27.12). Cooking a steak by acceleration (ch28).
- **Forms, gauge and fields.** A river drift for the Lie derivative (ch33). A knob at every point (ch44, ch48). A buckling strut and a magnet for symmetry breaking (ch41). A parallel civilization that invented QFT before geometry (ch47).
- **Foundations.** A clay mug that becomes a doughnut (appC). Coleman's alias versus alibi for passive versus active transformations (appB).

Recurring thought experiments:
- The freely falling astronaut who cannot feel her weight (ch06, ch08).
- Two particles released side by side to reveal tides (ch00, ch06, ch11).
- The ring of free test masses (ch14, ch46).
- A clock dropped from far away (ch06).
- The torch-carrying astronaut beaconing while she falls (ch25-ch27).
- Seeing the back of your own head in a closed universe or at r = 3M (ch16, ch19, ch25).

### 5.4 Figure style

- **Drawing.** Hand-drawn schematics (front). Most are cartoons, geometric constructions, spacetime diagrams and potential plots. Observational data appear rarely (ch18 Fig. 18.14, ch46 Figs. 46.3 and 46.5). Some chapters have almost no figures: ch17, ch21 and ch45 have none, and ch09, ch13 and ch36 have one or two.
- **Characteristic layouts.**
  - Paired panels: potential curve beside the orbit it produces (ch14, ch20, ch23).
  - Stacked-slice 3D cartoons encoding spatial geometry and size history (ch15 Figs. 15.1 and 15.3, ch18).
  - Side-by-side scroll panels for EM and gravity (ch43 Fig. 43.3).
  - A flip-book of embedding diagrams for the wormhole (ch27 Figs. 27.7-27.8).
  - Photographs of rods through a ring for trivial versus twisted bundles (appC Fig. C.20).
- **Weaknesses (details in section 8).** Amplitudes are exaggerated without saying so (ch14 Figs. 14.1, 14.3). A flat-page drawing hides what parallel transport does (ch07 Fig. 7.6). Primed axes are drawn untilted (ch02 Fig. 2.3). Some figures have orientation or sign mismatches (ch32 Fig. 32.4, ch37 Fig. 37.1).

### 5.5 Worked-example style

- **Scale and placement.** Formal shaded "Example N.M" boxes, 540 in total, 5-18 per chapter. The main derivation often *lives inside* examples:
  - The Newtonian limit (ch14 Example 14.2).
  - The Einstein-Hilbert variation (ch40 Example 40.10).
  - The three-step dR = 0 proof (ch43 Examples 43.4-43.6).
- **Examples as stories.** Some examples are narratives rather than drills. ch00 Example 0.3 grows from weighing the Earth to a Newtonian dark star.
- **Annotation.** ch09 labels each line of its examples with the step being executed. ch50 follows each boxed calculation with a "pause and interpret" paragraph.
- **Sanity checks are habitual.**
  - Flat-Cartesian collapse after each new definition (ch07 Examples 7.6, 7.10).
  - Switching off a parameter: the paraboloid with a → 0 (ch09).
  - Limit checks right after quoting a metric (ch29).
  - Numbers right after formulas: strain 5×10⁻²¹ and 10⁴⁷ W (ch46); Mercury's precession bookkeeping (ch23 Example 23.6).

### 5.6 Exercise style

- **Numbers and answers.** About 302 exercises (dossier estimates). Appendix E answers selected problems. Some answers there are wrong or garbled (ch00 Exercise 0.3, ch03 Exercise 3.3, ch32 Exercise 32.2(e), ch37 Exercise 37.5).
- **Exercises carry new material.** Many exercises teach content the text does not:
  - A curvature limit and Girard's theorem (ch03).
  - The de Sitter hyperboloid and its slicings (ch18).
  - Horizon-regular rain coordinates (ch25 Exercise 25.2); the Euclidean route to Hawking temperature (ch28 Exercise 28.4).
  - Gauss-Codazzi (ch30); holonomy equal to enclosed area (ch38 Exercise 38.4).
  - Gyroscope precession (ch45); the Raychaudhuri equation (ch50).
  - A numerical orbit integrator (ch23); the Kaluza-Klein Ricci scalar by Cartan's method (ch48, its only exercise).
- **Difficulty jumps.** Exercises are often much harder than the text: ch06 Exercises 6.5-6.6, ch25 rain coordinates, ch38 Exercise 38.4, ch44 Exercise 44.1.
- **Gaps.** ch14 has no exercises.

### 5.7 Margin notes

Margin notes are a second channel (1,032 counted):
- **Content.** One-line proofs and technical details (ch01, ch12); cautions, for example "coordinates are not vectors" (ch03).
- **Navigation.** Forward and backward pointers, and "spoiler" notes (ch04).
- **Colour.** Biographies (Kepler in ch20, the Bernoullis in ch39); historical asides (even Feynman did not know the Bianchi identity's geometric meaning, ch43); jokes.
- **Reference tables.** Lookups sit in the margin: a table of Hodge duals (ch37); Robertson-Walker Ricci components (ch16, ch17); vielbeins beside every Cartan example (ch36).
- **Notable margin essays.** The Kerr-derivation essay (ch29) and the words-only recap of the Bianchi argument for readers lost in indices (ch13).
- **Risk.** Essential arguments sometimes live only in margins: energy at infinity and the falling frame (ch22), the vielbein proofs (ch10).

---

## 6. Best explanations by topic

| Topic | Unit(s) and locators | Why this treatment is especially good |
|---|---|---|
| Inertial frames, relativity and equivalence previewed | ch00 §0.1, Fig. 1 | One juggler on four kinds of platform (at rest, steady velocity, steady acceleration, jolting) sets up both the relativity principle and the equivalence principle. |
| Lorentz boost | ch01 §1.2-1.3, Fig. 1.2(b) | Same 2×2 template as a rotation, with cos and sin replaced by cosh and sinh, matched to the identities. Invariance of the interval is argued, not assumed. |
| Maximal proper time, twin paradox | ch01 §1.4; ch08 §8.1, Fig. 8.2 | The variational method is taught on the Euclidean straight line, then transplanted, where the minus sign turns a minimum into a maximum. The null zigzag shows proper time has no minimum. |
| What counts as a 4-vector | ch02 §2.3, Table 2.1 | A candidate is admitted only if its self-product is frame independent: dx/dt fails, dx/dτ passes. The "shopping vector" counterexample makes the criterion memorable. |
| Coordinate versus non-coordinate bases | ch03 §3.1, Figs. 3.2-3.3 | Applying the law blindly gives e_θ of length r, and the surprise is kept. A four-step loop walk tests closure. |
| 1-forms and up/down components | ch04 §4.1-4.2, Figs. 4.3-4.4 | Stacks of sheets pierced by arrows; matter-wave fronts as sheets. Parallelogram versus perpendicular projections on the same skewed basis. |
| Observer measurements | ch04 §4.5; ch10 §10.1, Figs. 10.1-10.2 | Feed an observer's 4-velocity into a slot to get E, n and energy density. ch10 attaches a frame to a world line and derives E = −p·u in one line. |
| Reading a metric | ch05 §5.3-5.4, Fig. 5.1 | Draw local light cones from ds² = 0: a baby Eddington-Finkelstein metric first, then the warp-drive hook. Volume elements are built from proper lengths before determinants. |
| Equivalence principle and tides | ch06 §6.1, Example 6.1, Fig. 6.2 | An explicit coordinate change makes g vanish from an N-body equation while the pair forces survive. A uniform field equals no field; only tidal drift is evidence. |
| Gravitational time dilation | ch06 §6.5 | Derived twice: from g_00, and from a falling clock using special-relativistic γ at escape speed. Grounded with GPS and a 2022 lattice-clock exercise. |
| Covariant derivative and connection | ch07 §7.2-7.4, Figs. 7.1, 7.6 | Product rule on v^μe_μ exposes the basis-change term named Γ. The insider's versus outsider's verdict on parallelism. A four-step transport-back recipe. |
| Geodesics: minimum or saddle | ch08 §8.1, Fig. 8.1 | A spray of particles refocusing at the antipode diagnoses saddles without a second variation. A deliberately failing latitude circle. |
| Γ from the metric | ch09 §9.1-9.2, Fig. 9.1 | A boxed Steps I-V machine drilled on the sphere, then the paraboloid, then the Poincaré half plane. The same recipe on the particle action yields the Christoffel formula. |
| Riemann tensor | ch11 §11.2-11.3, §11.7, Fig. 11.5 | The Newtonian Hessian is named R first; the loop derivation follows. Curvature components read as tidal spring constants in a falling frame. |
| Energy-momentum tensor and its limits | ch12 §12.1-12.2, §12.4 | Every measured quantity comes from slot feeding; the fluid tensor is peeled into u⊗u plus a projector. A two-line calculation shows div T = 0 is not global energy conservation. |
| Why the Einstein tensor | ch13 §13.3-13.4 | The Ricci guess is killed by conservation plus the contracted Bianchi identity, and the Einstein tensor enters as the repair. κ is fixed last from Poisson's equation. |
| Newtonian limit | ch14 §14.1, Example 14.2 | Undoing the trace reversal with explicit 4×4 matrices shows −2Φ spreading equally into the space slots. |
| Hubble law and comoving geometry | ch15 §15.2-15.3, Figs. 15.3, 15.5 | Uniform scaling of separation vectors removes the "we are the centre" reading. Slices pierced by threads come before any metric. |
| Cosmological redshift | ch16 §16.3, Fig. 16.6 | Splitting two null-ray integrals so their long shared middle cancels leaves one period at each end. |
| Friedmann equations | ch17 | A Newtonian shell-energy warm-up. The fluid equation from the first law. Proof that the second equation is redundant; dilution laws derived twice. |
| Model universes | ch18 §18.3, Figs. 18.9-18.10 | One ingredient changed at a time. Einstein's static universe linearized. Loitering explained with an effective potential. |
| Penrose diagrams and horizons | ch19 §19.1-19.2, Figs. 19.5, 19.11, 19.17 | The answer diagram shown first; arctangent squashing; the Einstein cylinder as a common canvas. Horizons read off boundary shapes, with a mnemonic for event horizons. |
| Why orbits close | ch20 §20.3, §20.5 | One effective-potential picture classifies every trajectory. u = 1/r makes the orbit a harmonic oscillator in angle. Closure answered three ways. |
| Deriving Schwarzschild; TOV | ch21 §21.2-21.3 | Integration functions are named for their future meaning (Φ, m(r)). One pair of equations gives both the exterior and TOV. Coordinates are made operational. |
| Conserved quantities and the plunge | ch22 §22.1, §22.4, Figs. 22.5-22.7 | A three-step Killing recipe replaces the geodesic equation. One plunge on three graphs shows finite proper time against divergent Schwarzschild time. |
| ISCO and perihelion precession | ch23 §23.1, §23.3, Fig. 23.2 | Two thresholds of L̃/M (√12 and 4) organize all orbit types. Rescaling the angle turns precession into a period mismatch. Full Mercury bookkeeping. |
| Light bending, lensing, shadow | ch24 §24.1-24.2, Figs. 24.2, 24.6 | Energy equation "renamed" for light. Deflection by perturbing a straight line. The lens analogy is deliberately broken. Time reversal turns capture into a dark patch on the sky. |
| The horizon | ch25 §25.1-25.3, Figs. 25.2, 25.5 | Freeze three coordinates and check the sign of ds² ("the future is inwards"). Two clocks for one fall. Tidal stretching decides what is really singular. |
| Coordinate versus curvature singularities | ch26 §26.1-26.2 | Flat spacetimes in disguise first. Light rays as graph-paper coordinates. Redshift of the infaller read off one constant null label. |
| Kruskal coordinates | ch27 §27.1-27.3, eqn 27.12, Figs. 27.8-27.9 | The Rindler recipe replayed. The intuition flipped: Kruskal is the inertial chart. A wormhole flip-book shows non-traversability. |
| Hawking radiation | ch28 §28.1-28.2; Exercise 28.4 | An estimate whose free height ε cancels. Local energy versus Killing energy. The Euclidean no-cone-tip argument gives the exact temperature. |
| Ergosphere and Penrose process | ch29 §29.2, Figs. 29.3, 29.6 | Frame dragging in two lines. The stationary limit defined by counter-rotating light. The Penrose process reuses the Killing-vector sign flip from ch28. |
| Intrinsic versus extrinsic curvature | ch30, Figs. 30.4, 30.8 | Swept angle per length for curves, swept solid angle per area for surfaces. Tin can versus ball. |
| Vectors as derivatives | ch31 §31.2 | "Remove the point" from dP/dλ to leave the operator; components and basis read straight off the chain rule. |
| Forms, commutator, Lie derivative | ch32 §32.1; ch33 §33.2-33.3, Figs. 33.2(c), 33.5(c) | The wedge product built from intersecting sheet stacks. The failed-parallelogram picture reused, relabelled, as the Lie derivative. |
| Covariant derivative rules and metric compatibility | ch34 §34.3-34.4 | The minus sign for 1-forms forced by differentiating a constant pairing. Torsion as the leftover gap of a quadrilateral. |
| Ricci versus Weyl | ch35 §35.4, Fig. 35.4 | Converging lens versus astigmatic lens, seen through a transparent Sun. Ricci as the trace of the tidal matrix. |
| Efficient curvature computation | ch36 §36.4, Fig. 36.1 | Five-step Cartan flowchart. Flat control first. Einstein components as sums of sectional curvatures. |
| Stokes' theorem | ch38 §38.1, §38.4-38.5, Figs. 38.1-38.2 | Telescoping sums explain boundary terms. The Jacobian falls out of the wedge product. One theorem, four classical faces. |
| Fluids and geodesics | ch39 §39.4 | The relativistic Euler equation placed next to the geodesic equation: only transverse pressure gradients push flow off free fall. |
| Action to field equations and T | ch40 §40.4-40.6 | Three variation rules proven before the algebra. T defined as what makes the variation reproduce G = 8πT. Noether's theorem via Lie dragging. |
| Spontaneous symmetry breaking | ch41 §41.1, Fig. 41.4 | The Euler strut shows symmetry breaking needs neither thermodynamics nor quantum theory. The Landau free energy is relabelled as a field potential. |
| Maxwell in forms | ch42 §42.4 | Gauge invariance in one line from dd = 0. Half of Maxwell's equations come free from F = dA. |
| Bianchi identity | ch43 §43.1-43.3, Fig. 43.3 | "Boundary of a boundary is zero" gives charge conservation, dF = 0 and dR = 0 in parallel. |
| Gauge fields as connections | ch44 §44.1-44.2 | Break-then-repair; knobs at every point; a three-column gravity-gauge dictionary. |
| Linearized gravity and gravitomagnetism | ch45 | Shows the formidable intermediate equation, then earns the gauge simplification. Gravitomagnetism found by ordering sources in v/c. |
| Gravitational waves | ch46 §46.2-46.4, §46.6, Figs. 46.1, 46.4 | The EM rerun with square matrices. The "mass doesn't move" paradox. Conservation laws as radiation selection rules. Negative binding energy makes orbits spin up. |
| Spin 2 and trace reversal | ch47 §47.2-47.3 | Sign counting explains attraction. Trace reversal is recovered from demanding two polarizations. |
| Charge quantization, extra dimensions | ch48 §48.2 | A fibre phase promoted to a coordinate; charge as momentum around the circle. |
| Singularity theorem | ch50 §50.1-50.3 | Euclidean proxy pictures, a Riccati inequality, and a disappointment rescued by running time backwards. |

---

## 7. Weaknesses and gaps

### 7.1 Where novices stumble

- **Index machinery arrives early and dense.**
  - ch02 uses η^{μν} and lowered indices before defining them.
  - Primed-index Jacobians in ch03-ch05 are distinguished only by where the prime sits.
- **Sign logic.** ch07's "subtract the coordinate change" wording sits beside an added Γ term. Eqn 7.26 drops u^α without comment.
- **Quoted rather than derived.** Many results are used on trust early:
  - The Riemann components in ch11 §11.7 and ch21.
  - The linearized equation and gauge in ch14.
  - The Kerr and RN metrics in ch29.
  - The Bianchi identity in ch13.
  - A novice may not realize the proof comes much later.
- **Conceptually crowded chapters.**
  - ch19 (novice rating 2) and ch25-ch27: coordinates swapping causal roles, charts that do not cover spacetime.
  - ch29: two global structures, ring singularity, closed timelike curves and ergosphere in ten pages.
  - ch49: six research programmes in twenty pages.
- **Part V assumes fluency with the Part V machinery itself.** ch33-ch38 are rated maths 4 and novice 2. The authors flag ch34, ch38 and ch43 as skippable.
- **ch40 is the hardest chapter** (maths 5): an index-heavy Einstein-Hilbert variation with mislabelled rules, and a long optional fluid derivation.
- **Essential reasoning sometimes sits only in margins or exercises** (ch10, ch22, ch23's space/time precession split, ch50's Raychaudhuri equation).

### 7.2 Terse, loose or dated material

- **Cosmology is dated.**
  - ch18 calls Λ = 0 the "standard models", uses "missing mass", and never mentions accelerating expansion or Λ-CDM.
  - ch15 quotes H₀ = 70 km/s/Mpc to about 10%.
  - ch41 omits e-folds, slow-roll parameters and perturbations.
  - ch49 §49.8 numbers date to around 2020.
- **Observational astrophysics is dated.**
  - ch25: old Cygnus X-1 mass, no M87* image, and a claimed mass gap since contradicted by gravitational-wave events.
  - ch28: no complementarity, firewalls, Page curve or islands.
  - ch13: an old G value; ch21: dated stellar-evolution notes.
- **Loose physics statements.**
  - General covariance is presented without the Kretschmann objection (ch06).
  - Negative pressure is explained as "wanting to expand" (ch15).
  - "Classical" is glossed as incompatible with quantum mechanics (ch00).
  - Swingball's centrifugal force is called "felt" (ch08).
  - The rubber-sheet figure is credited with light bending (ch24 Fig. 24.4).
  - Circular compactification is called curvature (ch48).
  - The strong energy condition is called the weak one (ch50).
- **Missing standard names and theorems.**
  - No Levi-Civita uniqueness theorem (ch34), no Lovelock (ch13), no Hilbert's embedding theorem (appD), no Bertrand (ch20).
  - Surface gravity is not tied to the 4M e-folding time (ch26).
  - Irreducible mass is absent (ch29).

### 7.3 Printed errors found (highest learner impact first)

Every item below was checked in the dossiers against the page renders.

| Unit | Error |
|---|---|
| ch06 | Full light bending said to be 3× the equivalence-principle estimate (it is 2×). Timelike curves called geodesics (Example 6.3). |
| ch11, ch13 | Geodesic-deviation minus sign missing in eqn 11.38 and margin eqn 13.4. |
| ch14 | Weak-field criterion printed as (GM/rc)² ≪ 1 (should be GM/(rc²)). Unit mix in eqns 14.18-14.19. |
| ch16, ch17 | 2k/a for 2k/a² in the Ricci margin. Eqn 17.23 gives radiation the dust coefficient. ρ_c^(0) written as 8πH₀/3. Eqn 17.31 missing H₀². |
| ch18 | Eqn 18.35 coefficient ε/3 (should be √(2ε/3)). Exercise 18.6(c) pairs sinh and cosh solutions with the wrong k. Exercise 18.8 prints (1−x) for (1−x²). |
| ch19 | Future infinity given as t' = −π/2. Margin note 16 sign. Eqn 19.37 has sin²φ. Big-Bang edge labelled scri⁻. Conformal time range for closed dust wrong (Example 19.9). |
| ch20 | K₁ missing 1/r₁². Eqn 20.37 prefactor inverted. Fig. 20.8 caption range. |
| ch21 | TOV eqn 21.28 missing its minus sign. Eqn 21.35 missing square root. |
| ch23 | Eqn 23.6 has 2M²/L² (should be 12M²/L²). Eqn 23.9 power of r₊. Eqn 23.22 has "=" for "+". |
| ch24 | Eqn 24.22 has (3 + 2cosφ) for (3 + cos2φ). Refractive index given as √(−g₀₀) (should be its inverse). |
| ch25 | Eqn 25.10 sign would make proper time decrease during infall. |
| ch26 | Kretschmann scalar 12M²/r⁶ (should be 48). Eqn 26.26 cross-term sign. |
| ch27 | Eqn 27.4 "du du". Eqn 27.11 keeps dx². Captions call spacelike slices "timelike". |
| ch28 | Pair lifetime written ΔE/ħ. Heat capacity eqn 28.23 does not follow from S and T. M_CMB off by a factor of 10. |
| ch29 | Area integrand uses g, not √det. Eqn 29.6 has Δ² for Δ. The summary calls the stationary limit the event horizon. |
| ch30 | Sphere height expansion wrong. Eqns 30.64, 30.68-30.69 slips. |
| ch33 | Schwarzschild line element eqn 33.56 missing the minus on dt². |
| ch36 | Eqn 36.81 Einstein components wrong. Eqn 36.85 index errors. Time vielbein inverted in the Example 36.6 margin. |
| ch37 | ⋆(e_y∧e_x) for ⋆(e_y∧e_z) (Example 37.4). Sign of eqn 37.39. Eqn 37.66 curl sign. Exercise 37.5 logic. |
| ch40 | Rule labels swapped. Eqns 40.49-40.55 sign bookkeeping (final result correct). Canonical S^{αβ} = −T^{αβ} called "the same". |
| ch41 | Eqn 41.9 has φ² for φ. Eqn 41.22 missing the square on φ̇. |
| ch42 | Eqn 42.73 magnetic signs. Helix initial condition wrong (Example 42.9). |
| ch44 | Commutator written D_μD_ν − D_μD_ν. Horizontal transport condition missing ψ. |
| ch45 | Eqn 45.7 is identically zero as printed. Sign of eqn 45.39. |
| ch46 | Einstein's prediction dated 1906, Michelson born "1952", LIGO arms given as 4.2 km. J formula dimensionally wrong. Circular-orbit formula applied to the eccentric Hulse-Taylor binary. |
| ch47 | L_z sign. Missing minus sign before eqn 47.16 (would flip α). |
| ch49 | G printed as l_P/(m_P t_P²) (should be l_P³/(m_P t_P²)). String momentum prefactor. Schwarzschild radius missing its factor 2. |
| ch50 | "Weak" energy condition for strong. |
| appB | Covariant/contravariant naming reversed. Eqn B.3 repeats e_μ. |
| Part I | ch01 eqns 1.17-1.18 (dx)² twice. ch02 eqn 2.67 and Example 2.9 sign. ch05 eqn 5.40 signs. ch08 eqn 8.38 inverted. ch09 eqn 9.28 index. |

### 7.4 Conceptual omissions worth supplying

- **Uniqueness of the field equation.** Lovelock's theorem (ch13).
- **Boundary term and Λ.** The Gibbons-Hawking-York term, and Λ as the other allowed term in the action (ch40).
- **Wave details.** The transverse-traceless projection in the text, detector antenna patterns, and the Isaacson averaging requirement (ch46).
- **Self-coupled spin 2.** A consistently self-coupled spin-2 field rebuilds full GR (ch47).
- **Inner horizon.** Its instability, and the idealized nature of maximal extensions (ch29).
- **Distance measures.** The distinction between measured and recession velocities, and superluminal recession (ch15, ch16).
- **Figure scales.** Exaggerated scales in figures should be flagged to learners (ch14, ch18 Fig. 18.10, ch22 Fig. 22.3).

---

## 8. Visual language

### 8.1 What the figures do well

- **Paired causes and effects.** Potential curves are drawn beside orbits with the energy line and turning points marked (ch14 Fig. 14.2, ch20 Figs. 20.5-20.6, ch23 Fig. 23.2, ch24 Fig. 24.2).
- **Causal structure as a field.** Rows of cones that narrow and tip (ch00 Fig. 3, ch05 Fig. 5.1, ch25 Fig. 25.2, ch26 Figs. 26.5-26.7, ch29 Fig. 29.6).
- **One canvas reused across spacetimes.** The Einstein static cylinder (ch19 Figs. 19.11-19.12). The Penrose triangle reused across ch19, ch25, ch27, ch29 and ch41.
- **Tangible pictures of abstract algebra.**
  - Sheets, tubes and cells for forms (ch04 Fig. 4.3, ch32 Figs. 32.1-32.5, ch33 Fig. 33.1).
  - The failed parallelogram, reused for the commutator and the Lie derivative (ch33 Figs. 33.2, 33.5) and for torsion (ch34 Fig. 34.1).
  - Tube circulation for B (ch42 Fig. 42.2).
- **Operational diagrams.** Stacked slices for cosmic time (ch15). The two-ray redshift timing diagram (ch16 Fig. 16.6). The ring of masses at two instants and in two polarizations (ch14 Fig. 14.1, ch46 Fig. 46.1). A deformed ring overlaid on an interferometer (ch46 Fig. 46.4).
- **Physical props.** Photographs of rods through a ring for cylinder versus Möbius (appC Fig. C.20). A buckling strut (ch41 Fig. 41.4). A transparent Sun (ch35 Fig. 35.4).

**Recurring visual weaknesses the dossiers flag:**
- **Missing constructions.** No tilted primed axes or simultaneity lines in ch01. Fig. 2.3 draws the primed frame untilted.
- **Pictures that cannot show the point.** Flat-page transport (ch07 Fig. 7.6). Rubber sheet (ch24 Fig. 24.4). Horizons drawn as vertical timelike lines (ch28 Fig. 28.1).
- **Scale and orientation.** Unflagged exaggeration (ch14 Figs. 14.1, 14.3). Orientation or sign mismatches (ch32 Fig. 32.4, ch37 Fig. 37.1). Panels not to common scale (ch18 Fig. 18.10). Barrier height misdrawn (ch22 Fig. 22.3).
- **Incomplete diagrams.** A collapse diagram with no matter drawn (ch25 Fig. 25.10). Phase-only arrows that hide amplitude and A (ch44 Figs. 44.1, 44.3).

### 8.2 The 15 most redesign-worthy figures (ranked)

Ranking is the profile's judgement. It weighs reuse across chapters, conceptual centrality, and whether the static figure hides or distorts the key idea. All app ideas come from the dossiers' high-priority redesign fields, sometimes merged across units.

| # | Unit | Figure | Locator | App idea |
|---|---|---|---|---|
| 1 | ch05 (with ch00, ch25, ch26, ch29) | Fig. 5.1(a)-(c) | p. 60, §5.3 (also ch00 Fig. 3 p. 3; ch25 Fig. 25.2 p. 264; ch26 Fig. 26.5 p. 276; ch29 Fig. 29.6 p. 304) | **Universal cone-field explorer.** Type or pick a line element (Minkowski, Rindler, baby EF → real EF by a slider, Schwarzschild, Kerr equatorial). Draw local cones and integrated null curves. Switch to EF coordinates to watch pinching cones become smoothly tilting ones. A probe tries to straighten cones and shows it works only near one point. |
| 2 | ch19 | Fig. 19.5(b) (with Figs. 19.4, 19.7(a)) | p. 203-205, §19.1 | **Penrose-diagram component reused course-wide.** Morph the t-r grid into the triangle via arctan. Hovering a boundary names it (i±, i⁰, scri±) and shows which curves end there. A light-pulse emitter and a draggable observer shade the causal past. |
| 3 | ch27 | Fig. 27.9 (with Fig. 27.1) | p. 281, 286, §27.1, §27.3 | **Kruskal-to-Penrose compactifier.** Toggle constant-r and constant-t grids and region shading on the Kruskal plane, hover for (t, r) or "undefined", then slide a compactification so hyperbolae bow and infinity pulls into corners while light stays at 45°. |
| 4 | ch23 (with ch20, ch14, ch22, ch24) | Fig. 23.2(a) | p. 247, §23.1 (ch20 Fig. 20.6 p. 222; ch22 Fig. 22.3 p. 241; ch24 Fig. 24.2 p. 256) | **Linked potential-and-orbit lab.** A draggable energy line on V_eff (Newtonian ghosted, r⁻³ term shaded, r₊ and r₋ merging at 6M) drives a live geodesic integration. Presets: photon W_eff, capture, zoom-whirl. |
| 5 | ch46 (with ch14) | Fig. 46.1(c) and Fig. 46.4(b) | p. 499, 507, §46.2, §46.6 (ch14 Fig. 14.1 p. 154) | **Polarization mixer tied to an interferometer.** A ring of beads driven by h₊ and h× amplitudes and phases (linear, tilted, circular) with a tidal quiver overlay. One phase slider also drives exaggerated arm lengths and the output phase trace. Discover that a 45° rotation turns + into ×. |
| 6 | ch01 (with ch02) | Fig. 1.6 and Fig. 2.3 | p. 16, §1.3; p. 24, §2.2 | **Proper Minkowski diagram with sweeping simultaneity.** A velocity slider scissors the primed axes. Coordinates of an event are read off both grids. The line of constant t' tilts and paints the extended-present wedge. This fixes the book's lack of tilted axes. |
| 7 | ch25 (with ch22) | Fig. 25.5 | p. 266, §25.3 (ch22 Figs. 22.5-22.6 p. 243) | **Two-clock plunge.** An astronaut falls while τ(r) and t(r) plot in sync. Torch pulses at equal proper-time intervals arrive ever later at a distant observer, and the log-scale spacing reveals the 4M e-folding time. |
| 8 | ch11 (with ch38) | Fig. 11.2 | p. 121, §11.1 (ch38 Exercise 38.4) | **Draw-your-own loop on a globe.** Sketch any closed path; a vector is transported step by step and its net rotation is compared with enclosed area / a². A shrinking-loop panel (ch11 Fig. 11.5) shows convergence to the Riemann component. |
| 9 | ch07 | Fig. 7.6 | p. 87, §7.4 | **Covariant derivative on an unrolled cone.** The cone is rolled beside its flat development, so transport is exact and visible. The four-step "carry back, subtract, divide, limit" construction is animated. This fixes the flat-page figure that hides transport. |
| 10 | ch33 (with ch34) | Figs. 33.2(c) and 33.5(c) | p. 343-345, §33.2-33.3 (ch34 Fig. 34.1 p. 352) | **Commutator-closure to Lie-derivative stepper.** Two user-chosen fields and both routes from a base point; the gap vector matches [u,v]. The same quadrilateral relabelled as the dragged v versus the local v. A toggle adds covariant edge corrections to show torsion. |
| 11 | ch32 (with ch04, ch31, ch38) | Fig. 32.1 | p. 334, §32.1 (ch04 Fig. 4.3 p. 44; ch31 Fig. 31.9 p. 327; ch38 Fig. 38.2(a) p. 407) | **Sheet-intersection sandbox.** Controllable stacks of planes; a signed and fractional crossing counter for a dragged arrow. A second stack lights tube lattices; a patch counts pierced tubes. A path over level lines verifies f(B) − f(A). |
| 12 | ch18 | Fig. 18.10 (with Fig. 18.9(a)) | p. 194-195, §18.3 | **Continuous (Ω_m, Ω_Λ) explorer** replacing the discrete k-by-Λ grid. Regions coloured by origin and fate, with a bead in V_eff(a) and the a(t) curve linked. A modern marker corrects the chapter's dated Λ = 0 framing. |
| 13 | ch24 | Fig. 24.6 | p. 259, §24.2 | **Lighthouse at radius r.** A static emitter fires exact null geodesics coloured escape or capture, with the critical cone ψ_c in the local frame. Reverse the film to render the observer's black patch on the sky (both branches of the critical angle made visible). |
| 14 | ch35 | Fig. 35.4 | p. 371, §35.4 | **Transparent-Sun lensing simulator.** Background stars behind a non-refracting star whose density and mass the learner sets. Ray bundles through the weak-field metric show Ricci focusing inside matter and Weyl shear outside. |
| 15 | ch29 | Fig. 29.3 (with Fig. 29.5(a)) | p. 301, 303, §29.2 | **Honest Kerr anatomy viewer.** Surfaces r₀(θ), r₊, r₋ and the ring computed and embedded via the Boyer-Lindquist Cartesian map. A spin slider reshapes the meridian plot, and a probe reports whether hovering is allowed. |

Strong runners-up from the dossiers:
- ch06 Fig. 6.2(b), tidal test lab.
- ch09 Fig. 9.2, half-plane walker with shrinking rulers.
- ch16 Fig. 16.6, redshift area-under-1/a.
- ch27 Fig. 27.8, wormhole flip-book.
- ch41 Fig. 41.7, coupled inflation simulator.
- appC Fig. C.20, twist slider from cylinder to Möbius band.

---

## 9. Tutor guidance

### 9.1 Which learners this book's approach suits

- **Physics undergraduates (year 2-4) and returning self-learners.** They know mechanics and electromagnetism and want every algebraic step shown in boxed examples. The novice-4 chapters (ch00, ch01, ch03, ch05, ch06, ch14, ch20, ch22, appD) are ideal entry points.
- **Learners who think in fields and analogies with EM.** Poisson's equation as template (ch13), gauge freedom (ch42-ch45) and photon-to-graviton exchange (ch47) make GR feel continuous with physics they already own.
- **Learners intimidated by abstraction.** The components-first pass in Parts I-II, with slot machines and pictures, defers forms and manifolds until the learner has already used the objects.
- **Learners heading toward QFT or high-energy theory.** Part VI (Lagrangian fields, gauge connections, gravitons, Kaluza-Klein) is a rare bridge, written in the voice of the authors' QFT book.
- **Less suited to:**
  - Mathematicians wanting axiomatic rigour from the start. Part V and appC are informal in places.
  - Learners who need up-to-date observational cosmology or gravitational-wave astrophysics.
  - Readers who will be confused by non-standard terms (see section 4) when cross-reading other texts.

### 9.2 Moments when the tutor should reach for GA

| Learner moment | Draw on |
|---|---|
| "Why can't gravity just be a force field?" | ch00 §0.2 (what versus how); ch06 §6.1 Example 6.1 (g cancels); the failed wave-Poisson theory (ch06) |
| First contact with indices and up/down components | ch02 differentials-versus-derivatives mnemonic; ch04 slot machines, sheet stacks and Fig. 4.4 dual constructions |
| "Is my space curved or are my coordinates weird?" | Polar-coordinate flat controls (ch03, ch07 §7.2, ch11); flat metrics in disguise (ch26) |
| Confusion about what an observer measures | ch04 §4.5 slot feeding; ch10 §10.1 E = −p·u |
| "Where does Einstein's equation come from?" | ch13 propose-and-refute; ch14 Example 14.2 matrices; later ch40 action |
| Orbits feel opaque | ch20 → ch22-ch24 Newtonian mirror; effective-potential energy lines |
| Horizon paradoxes (the infaller "never arrives") | Sequence ch25 (two clocks, sign test) → ch26 (null grids, EF) → ch27 (Kruskal, Rindler inversion) |
| Penrose diagrams | ch19's answer-first triangle and arctangent squashing |
| Gravitational-wave polarization or detection | ch14 Fig. 14.1 and ch46 ring of masses; "mass doesn't move" paradox |
| Ready for forms, Lie derivatives, Cartan | ch31-ch36 sheet and tube pictures and the parallelogram; Cartan flowchart |
| Gauge theory connection | ch44 dictionary table; ch48 knob-at-every-point |

### 9.3 How the AI tutor should use this book

1. **Use its moves, not its prose.** Rebuild explanations from the named signature moves in sections 5-6 in the tutor's own words. Quote at most a short phrase. Equations may be transcribed.
2. **Correct errors proactively.** When a learner works from GA, check the section 7.3 list before trusting a printed equation, especially:
   - TOV (ch21), geodesic deviation (ch11, ch13), light bending factors (ch06, ch24).
   - Friedmann acceleration (ch17), Kretschmann (ch26), energy conditions (ch50).
   - The Einstein components in ch36.
3. **Update dated content explicitly.** Pair ch18 with the accelerating universe and Λ-CDM (Universe 4 plus radiation is essentially Λ-CDM, per the ch18 dossier). Refresh ch25 and ch46 observations and ch28's information-paradox status.
4. **Flag conventions when cross-referencing.**
   - The -+++ and MTW Riemann sign match most modern texts.
   - Warn about GA's Hodge star direction (ch37), the appB covariant/contravariant reversal, "affine connection" (ch34), "extrinsic curvature" (ch30) and the equivalence-principle terminology (ch06).
   - Warn about ch45's gauge sign and ch26/ch27's swapped null-coordinate letters.
5. **Respect the spiral; do not front-load Part V.**
   - Suggested fast path (profile's judgement): ch00 → ch01-ch08 → ch11-ch14 → then Part IV (ch20-ch25) or Part III (ch15-ch18).
   - Pull in ch09, ch10 and ch19 as tools when a computation needs them.
   - Offer ch31-ch36 only when the learner asks why a quoted result holds. Point to the specific repayment (section 3.3).
6. **Supply what GA quotes.** When a learner asks for the geodesic deviation derivation, go to ch35. For Killing conservation, go to ch33 §33.5; for local flatness, ch35 §35.2.
   - For the Kerr metric, uniqueness of the field equation, or Hawking's actual calculation, say that GA does not derive them and give a sketch.
7. **Use the dossiers' tutor openers.** Examples:
   - ch00: ask when juggling on a train would get hard.
   - ch14: ask what would convince you the field equation is right (it must reduce to Newton, predict something new that is observed, and describe the Universe).
   Let the learner rediscover the chapter's structure.
8. **Avoid the book's weaker pictures.** Do not use the rubber sheet (ch24 Fig. 24.4). Do not draw horizons as timelike (ch28 Fig. 28.1). Always state figure exaggeration (ch14). Prefer the redesign apps in section 8.2.
9. **Treat exercises as a teaching resource.** Many key results live in exercises (section 5.6). When a learner is ready, set those exercises as guided discovery rather than repeating the text.

---

## 10. Unit index

Ratings: **M** = mathematical level (1-5), **C** = conceptual level (1-5), **N** = novice friendliness (1-5, higher is friendlier). **Verdict** is the dossier verification outcome ("fixed" means an audit pass corrected the dossier).

| Unit | Title | Printed pages | M | C | N | One-line summary | Verdict |
|---|---|---|---|---|---|---|---|
| ch00 | Overture | 1-10 | 2 | 2 | 4 | Vocabulary of relativity, light cones and the metric field; Newtonian gravity rebuilt as a field theory; geometrized units. | fixed |
| ch01 | Special relativity | 11-21 | 2 | 3 | 4 | Interval, boost as hyperbolic rotation, demolished common-sense beliefs, twin paradox as maximal proper time, evidence. | fixed |
| ch02 | Vectors in flat spacetime | 22-35 | 3 | 2 | 3 | 4-vector index machinery, invariants, velocity, momentum and acceleration, uniform acceleration, action −m∫dτ. | fixed |
| ch03 | Coordinates | 36-42 | 2 | 3 | 4 | Transformations in polar coordinates; coordinate versus non-coordinate bases, Lie bracket, no position vector, sphere geometry. | fixed |
| ch04 | Linear slot machines | 43-55 | 3 | 3 | 3 | 1-forms as sheet stacks, tensors as slot machines, transformation law, dust energy-momentum tensor read by an observer. | fixed |
| ch05 | The metric | 56-66 | 2 | 3 | 4 | Metric as a field; line elements visualized by local light cones (Rindler, EF, warp drive); lengths, areas and √−g d⁴x. | fixed |
| ch06 | Finding a theory of gravitation | 67-80 | 2 | 3 | 4 | Equivalence and covariance as six Lessons; tides, local flatness, a failed scalar theory, gravitational redshift and GPS. | fixed |
| ch07 | Parallel lines and the covariant derivative | 81-90 | 3 | 3 | 3 | Insider parallelism, Γ from changing bases, covariant derivative, parallel transport, metric compatibility. | fixed |
| ch08 | Free fall and geodesics | 91-100 | 3 | 3 | 3 | Geodesics as extremal and self-parallel curves; conjugate points; connection as inertial force; null rays and the Shapiro delay. | fixed |
| ch09 | Geodesic equations and connection coefficients | 101-107 | 3 | 2 | 3 | Optional five-step recipe from metric to Γ on sphere, paraboloid and half plane; derivation of the Christoffel formula. | fixed |
| ch10 | Making measurements in relativity | 108-119 | 3 | 3 | 3 | Observer orthonormal frames, E = −p·u, vielbeins, stationary and freely falling frames. | fixed |
| ch11 | Riemann curvature and the Ricci tensor | 120-130 | 4 | 3 | 3 | Geodesic deviation and loop transport; Riemann from a loop; symmetries; Ricci; plane and sphere checks; tidal stretching. | fixed |
| ch12 | The energy-momentum tensor | 131-140 | 3 | 3 | 3 | Slot reading of T, perfect fluid, point particles, local conservation, div T = 0 is not global energy conservation. | fixed |
| ch13 | The gravitational field equations | 141-150 | 3 | 3 | 3 | Poisson template; Ricci guess refuted via Bianchi; Einstein tensor; κ from the Newtonian limit; trace-reversed and Λ forms. | fixed |
| ch14 | The triumphs of general relativity | 151-156 | 2 | 3 | 4 | Newtonian limit derived; previews of gravitational waves, Schwarzschild orbits and precession, black holes and RW cosmology. | fixed |
| ch15 | An introduction to cosmology | 157-168 | 3 | 3 | 3 | Cosmological principle, Hubble law from scaling, cosmic time and fundamental observers; empty and de Sitter universes. | fixed |
| ch16 | Robertson-Walker spaces | 169-180 | 3 | 3 | 3 | Constant spatial curvature and k = ±1, 0; circles, triangles, embeddings; cosmological redshift; initial singularity. | fixed |
| ch17 | The Friedmann equations | 181-187 | 2 | 3 | 3 | Friedmann equations from RW plus perfect fluid; fluid equation and dilution laws; critical density and Ω; age integral. | fixed |
| ch18 | Universes of the past and future | 188-200 | 3 | 3 | 3 | Numbered model zoo (Universes 2-11), Einstein static instability, Lemaître loitering, historical route (dated framing). | fixed |
| ch19 | Causality, infinity, and horizons | 201-216 | 3 | 4 | 2 | Conformal compactification, Penrose diagrams on the Einstein cylinder, particle and event horizons, spacelike singularities. | fixed |
| ch20 | Newtonian orbits | 217-228 | 2 | 2 | 4 | Kepler problem toolkit: conservation laws, effective potential, u = 1/r conics, why bound orbits close. | fixed |
| ch21 | The Schwarzschild geometry | 229-236 | 3 | 3 | 3 | Static spherical ansatz through the field equation; mass function, exterior solution, TOV; operational meaning of r and t. | fixed |
| ch22 | Motion in the Schwarzschild geometry | 237-245 | 3 | 3 | 4 | Killing-vector constants plus normalization; gravitational redshift; relativistic effective potential; radial plunge. | fixed |
| ch23 | Orbits in the Schwarzschild geometry | 246-253 | 3 | 3 | 3 | Circular, capture and precessing orbits; ISCO at 6M; Kepler III in coordinate time; perihelion advance and Mercury. | fixed |
| ch24 | Photons in the Schwarzschild geometry | 254-261 | 3 | 3 | 3 | Photon potential and photon sphere; 4M/b deflection and 1919; point-mass lensing; critical angle and black-hole shadow. | fixed |
| ch25 | Black holes | 262-271 | 2 | 4 | 3 | Light cones at and inside r = 2M; tortoise coordinate; proper versus coordinate time; tides; the view inside; collapse. | fixed |
| ch26 | Black-hole singularities | 272-279 | 3 | 4 | 3 | Coordinate versus curvature singularities, geodesic completeness, null-grid recipe on toy metrics, EF coordinates, fading infaller. | fixed |
| ch27 | Kruskal-Szekeres coordinates | 280-288 | 3 | 4 | 3 | Kruskal chart via the Rindler recipe; four regions, wormhole and white hole; non-traversability; Kruskal Penrose diagram. | fixed |
| ch28 | Hawking radiation | 289-296 | 3 | 4 | 3 | Heuristic pair splitting and temperature; evaporation; surface gravity; entropy and black-hole mechanics; information; Unruh effect. | fixed |
| ch29 | Charged and rotating black holes | 297-306 | 3 | 4 | 3 | No-hair; RN horizons and tower; Kerr ring singularity, frame dragging, ergosphere, Penrose process. | fixed |
| ch30 | Classical curvature | 307-321 | 3 | 3 | 3 | Curves (Frenet-Serret) and surfaces (principal curvatures, second fundamental form); Gauss's intrinsic curvature; Riemann's generalization. | fixed |
| ch31 | A reintroduction to geometry | 322-333 | 3 | 4 | 3 | Metric-free rebuild: vectors as derivatives, 1-forms as differentials, tensor slot operations. | fixed |
| ch32 | Differential forms | 334-339 | 3 | 3 | 3 | Wedge products as sheet intersections; 2-forms as tubes, 3-forms as cells; p-vectors and tube-counting pairing. | fixed |
| ch33 | Exterior and Lie derivatives | 340-350 | 4 | 4 | 2 | d and dd = 0; commutator as failed parallelogram; Lie derivative by dragging; Killing vectors and conservation. | fixed |
| ch34 | Geometry of the connection | 351-362 | 4 | 4 | 2 | Axioms for ∇, torsion, Γ as components, ±Γ rule for tensors, metric compatibility and affine parameters. | fixed |
| ch35 | Riemann curvature revisited | 363-373 | 4 | 4 | 2 | Index-free geodesic deviation; curvature operator by two routes; normal coordinates; 20 components; Ricci versus Weyl. | fixed |
| ch36 | Cartan's method | 374-385 | 4 | 4 | 2 | Connection 1-forms, structure equations, a five-step recipe run on plane, sphere, flat FRW and static star. | fixed |
| ch37 | Duality and the volume form | 386-396 | 3 | 3 | 2 | Hodge star via the volume form; duals in 3D and Minkowski; signed areas, 4-volumes, 3-volume 1-form, flux elements. | fixed |
| ch38 | Forms, chains, and Stokes' theorem | 397-410 | 4 | 4 | 2 | Integration as pairing forms with chains; boundary operator; generalized Stokes theorem unifying the classical theorems. | fixed |
| ch39 | Fluids as dry water | 411-427 | 4 | 3 | 3 | Newtonian perfect fluid, then relativistic: projected conservation laws, first law, relativistic Euler versus geodesics. | fixed |
| ch40 | Lagrangian field theory | 428-444 | 5 | 4 | 2 | Field Lagrangians, Einstein-Hilbert variation, Hilbert T, Noether currents via Killing fields, perfect fluid from an action. | fixed |
| ch41 | Inflation | 445-452 | 3 | 3 | 3 | Flatness and horizon problems; Landau symmetry breaking to φ⁴; Hubble-damped scalar; slow roll and flattening. | fixed |
| ch42 | The electromagnetic field | 453-466 | 4 | 3 | 2 | Faraday tensor from minimal coupling; Maxwell in indices; gauges and retarded potentials; stress tensor; F = dA and d⋆F = ⋆J. | fixed |
| ch43 | Charge conservation and the Bianchi identity | 467-475 | 4 | 4 | 2 | Boundary of a boundary gives charge conservation, dF = 0 and gravitational dR = 0; Weyl field equation. | fixed |
| ch44 | Gauge fields | 476-484 | 3 | 4 | 3 | Local phase invariance forces A; D = d + iqA as connection; [D,D] = iqF as curvature; bundle pictures and dictionary. | fixed |
| ch45 | Weak gravitational fields | 485-493 | 4 | 3 | 2 | Linearized curvature, coordinate gauge freedom, Lorenz gauge wave equation, Newtonian metric check, gravitomagnetism. | fixed |
| ch46 | Gravitational waves | 494-511 | 4 | 4 | 3 | TT gauge and +/× polarizations, quadrupole formula and luminosity, binary inspiral and Hulse-Taylor, exact plane wave, detection. | fixed |
| ch47 | The properties of gravitons | 512-519 | 3 | 4 | 2 | Field-theorist's route: massless spin-2 mediator, photon then graviton exchange, trace subtraction, helicity ±2, non-renormalizability. | fixed |
| ch48 | Higher dimensional spacetime | 520-526 | 4 | 4 | 2 | Kaluza-Klein: gauge phase as fifth coordinate, 5D metric splits into Einstein plus Maxwell, charge quantization, EFT remark. | fixed |
| ch49 | From classical to quantum gravity | 527-546 | 3 | 4 | 3 | Survey: extra dimensions and Planck scale, Nambu-Goto string, cosmic strings, superspace, LQG tetrahedron, AdS, Λ-CDM. | fixed |
| ch50 | The Big-Bang singularity | 547-553 | 4 | 4 | 2 | Geroch-style sketch: maximal curves, focusing of normal congruences, past timelike incompleteness of expanding universes. | fixed |
| appB | Conventions and notation | 562-564 | 2 | 2 | 2 | Reference card: units, typography, index rules, vielbein notation, covariant-derivative notations. | fixed |
| appC | Manifolds and bundles | 565-580 | 3 | 4 | 3 | Sets, topology, charts, atlases, diffeomorphisms (div T = 0 from invariance), compactness, tangent vectors, fibre bundles. | fixed |
| appD | Embedding | 581-586 | 2 | 3 | 4 | Induced-metric recipes; wormhole embedding; hyperbolic plane fails in R³ and fits as a hyperboloid in pseudo-Euclidean space. | fixed |

Not covered by dossiers: `front` (preface, read directly for section 2), appA (further reading, p. 554-561) and appE (answers to selected problems, p. 587-613).
