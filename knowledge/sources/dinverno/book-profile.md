---
type: book-profile
book: dinverno
book_short: DIV
title: "Introducing Einstein's Relativity: A Deeper Understanding"
authors: ["Ray d'Inverno", "James Vickers"]
edition: "Second edition (2022), Oxford University Press"
units: 26
signature: "A self-study route that retraces Einstein's own path, from radar-and-clock special relativity drawn on spacetime diagrams, through a compulsory components-first tensor apprenticeship, to field equations reached twice (heuristically, then variationally) and a replayed black-hole programme, stated throughout as numbered principles and boxed axioms."
units_needing_attention: []
---

# DIV book profile: d'Inverno and Vickers, *Introducing Einstein's Relativity* (2nd ed.)

All 26 chapter dossiers (ch01-ch26) carry the verification verdict "fixed". Nothing is left open, so `units_needing_attention` is empty. The front matter (a one-paragraph foreword by Roger Penrose, `front`) has no dossier of its own; the authors' own statement of purpose is chapter 1 (ch01). Locators below give the unit id, then section and printed page (p.) where known.

---

## 1. Identity and audience

**Who it is for.** The book grew out of mid-1970s lecture notes for a UK third-year undergraduate option that MSc and early PhD students later took too. The second edition deliberately serves both groups (ch01 §1.1 p.1). Graduate material is marked "Level 2" with a hatched bar in the margin. Unmarked "Level 1" material is the core thread and may not be skipped (ch01 §1.1, §1.4). Penrose's foreword calls the route gentle but comprehensive (front). Two signed notes speak to the two ends of the ability range: Ray's to the "less able" student (§1.5 p.6) and James's to the "more able" (§1.6 p.7) (ch01).

**Assumed prerequisites** (ch01 §1.4 p.5, graded by the authors):
- *Essential:* calculus through partial differentiation; simple ODEs; Taylor series; basic algebra and some matrices (eigenvalues can be taken on trust); vectors, vector spaces and bases; Newtonian mechanics and gravitation, ideally with the potential.
- *Helpful:* Maxwell's equations, Navier-Stokes, waves.
- *Needed later:* basic astronomy, plus much broader contemporary physics for ch26.

Individual dossiers add Lagrangian and Hamiltonian mechanics (ch08), elementary group theory (ch08), PDE classification and analyticity (ch13, ch14), Bessel functions and distributions (ch22), and black-body and particle physics (ch26 §26.3, flagged as Level 2).

**Level and difficulty profile.** Ratings are math / conceptual / novice-friendliness on 1-5 scales (section 10).
- Part A (ch02-ch04) is gentle: math 2, novice 3-4.
- Part B (ch05-ch07) climbs to math 4 with novice 2.
- ch09 drops back to math 2 with novice 4.
- The late advanced chapters are the hardest in the book: ch14 and ch23 reach math 5, and ch20 and ch23 reach conceptual 5.
- The authors warn that Part B is the real motivational test (ch01 §1.4).

**Tone.** In the prose chapters (ch01, ch09, ch17 §17.11-17.12, ch26 §26.8-26.9) the voice is personal, candid and at times philosophical: it discusses fashion and reputation in research, admits the authors do not grasp every idea, and closes with open questions. The technical chapters (ch05-ch07, ch11, ch14) are in a terse, lemma-and-exercise register.

**Length.** 572 printed pages in 26 chapters and six Parts (A-F). The dossiers record about 273 figures and tables, about 242 worked derivations or examples embedded in the text, and roughly 369 end-of-chapter exercises. These match the authors' own claims of more than 250 diagrams and more than 350 exercises (ch01 §1.1-1.2).

**Deliberate omissions and boundaries.**
- Differential forms and the index-free machinery are left out on purpose. The authors choose the index route for practicality and point to Penrose's abstract indices as the next step (ch05 §5.1, Gaps).
- Quantum gravity is discussed only sociologically (ch01 §1.3).
- The astrophysics of gravitational-wave sources and cosmological parameter estimation is summarized rather than developed (ch01 §1.6; ch21 §21.13-21.14; ch26 §26.3 onward).
- The Bondi radiation treatment is restricted to axisymmetric, reflection-symmetric sources (ch23).
- Kerr global structure is shown only on the axis (ch20 §20.9).
- Part D is openly modelled on Hawking and Ellis and meant as a stepping stone to it; the authors admit to close paraphrase in places (ch01 §1.6).

---

## 2. The authors' stated goals and philosophy (paraphrased)

From ch01 (the organization chapter) and the foreword (front):

1. **Physical insight together with mathematical grounding.** Relativity fascinates, but mastering it takes both, and the book tries to supply each (ch01 §1.1).
2. **Follow Einstein's route.** Part C is built to mirror how Einstein reached the theory: principles, field equations motivated physically, the same equations re-derived from an action, then the source, the structure of the equations, the simplest solution and the solar-system tests. The authors present this as the path to deeper understanding, not just a history lesson (ch01 §1.1; realized in ch09-ch16).
3. **Tensor fluency comes first.** You cannot handle field equations confidently without fluent tensor manipulation, so Part B precedes GR and its exercises are compulsory (ch01 §1.1; ch05 §5.1).
4. **Relativity via spacetime pictures.** The authors call their contribution mainly one of organization. They credit the Bondi-Milne k-calculus for the insight its diagrams give from the very start, and they name spacetime diagrams as the book's unifying theme (ch01 §1.2).
5. **Demystification.** Eddington's "only three people understand it" story is countered twice: by the claim that a century of hindsight lets GR be assembled in simple steps, and by Ray's own story of learning GR at fifteen by working every calculation in Lillian Lieber's illustrated book (ch01 §1.2, §1.5).
6. **Study method.** Understanding comes in layers. Skim first, re-read without stalling, then study with the exercises. When stuck on a multi-part problem, assume the earlier result and press on. Prefer short, frequent sessions (ch01 §1.4).
7. **The second edition broadens the view.** Einstein's equations are now also treated as a PDE evolution system, alongside the curved-geometry picture (hence the expanded ch13 and the new ch14). Precision data (LIGO, binary pulsars, CMB) drive the enlarged ch21 and the new ch26. Living Reviews in Relativity anchors the further reading (ch01 §1.6).
8. **Honesty about limits.** The book says plainly where it stops being self-contained, and it presents stopping after Part C as a respectable achievement (ch01 §1.5-1.6).

---

## 3. Architecture

### Parts and dependency outline

```
ch01 Organization (no physics)
 |
Part A  Special relativity (no tensors)
 ch02 k-calculus (radar, k, simultaneity, clock paradox, Lorentz, interval)
  -> ch03 standard Lorentz derivation, rapidity, calibration hyperbolae, hyperbolic motion/horizons, twins, Doppler
  -> ch04 relativistic mechanics (relativistic mass, E = mc^2, photons)
 |
Part B  Tensor formalism (pure mathematics, compulsory exercises)
 ch05 tensor algebra (charts, transformation laws, tangent/gradient prototypes, Lie bracket)
  -> ch06 tensor calculus (Lie derivative, connection, parallel transport, geodesics, Riemann, metric, Bianchi, Weyl)
  -> ch07 densities, integration, variational geodesics (K-Lagrangian), Killing vectors
 |
Part C  General relativity
 ch08 SR revisited as flat Lorentzian geometry; Axioms I and II (§8.5)
  -> ch09 principles (Mach, equivalence, covariance, minimal coupling, correspondence)
  -> ch10 field equations from tidal analogy + Newtonian limit; GR = axioms with flatness clause replaced (§10.8)
  -> ch11 same equations from an action (Palatini identity, Bianchi from covariance)
  -> ch12 energy-momentum tensors (dust, fluid, Maxwell), kappa, dominant energy condition
  -> ch13 structure of the equations (gauge, Lambda, motion from conservation, Cauchy problem, hole argument)
  -> ch14 3+1 and 2+2 formalisms (Gauss-Codazzi-Ricci, lapse/shift, numerical-relativity survey)
  -> ch15 Schwarzschild (Killing-vector definitions, Birkhoff, TOV)
  -> ch16 classical tests, Einstein equivalence principle, PPN, rubber sheet
 |
Part D  Black holes          ch17 horizons/EF -> ch18 Kruskal + Penrose diagrams -> ch19 Reissner-Nordstrom -> ch20 Kerr, mass, singularity theorems, Hawking
Part E  Gravitational waves  ch21 linearized + detection -> ch22 exact waves -> ch23 Bondi radiation, Petrov, peeling
Part F  Cosmology            ch24 RW + Friedmann + redshift/distance -> ch25 classical models, horizons, dS/AdS, conformal diagrams -> ch26 Omega plane, CMB, LambdaCDM, inflation
```

Parts D, E and F each depend on Part C. The key links:
- Part D uses the Killing machinery of ch07, the Schwarzschild solution of ch15, the Penrose diagrams of ch18 and the Maxwell tensor of ch12.
- Part E uses the geodesic deviation of ch10, the Maxwell gauge analogy of ch12 and the radar method of ch02.
- ch23 draws on ch13, ch14, ch17, ch18 and ch20.
- Part F uses the Weyl-tensor fact of ch06, the perfect fluid of ch12, the Λ term of ch13, and the conformal compactification of ch18.

### Where the pivotal ideas first appear

| Idea | First substantive treatment | Later development |
|---|---|---|
| Special relativity | ch02 (k-calculus, §2.7 p.19; Lorentz boost §2.13 p.25; interval) | ch03 standard route and rapidity (§3.1 p.31); ch04 dynamics; ch08 tensorial restatement and axioms (§8.5 p.142) |
| Vectors and covectors ("one-forms") | ch05 §5.5-5.6 p.71-72 (contravariant vector modelled on a curve tangent, covariant vector on a gradient) | ch05 §5.10 p.78 tangent and cotangent spaces, vector field as a derivative operator. The book says "covariant vector" or "co-vector"; forms are never developed (ch05 Gaps) |
| Tensors | ch05 (defined by transformation laws, type (p,q), contraction) | ch07 §7.1 densities; gothic density notation ch11 |
| Equivalence principle | Foreshadowed ch03 Table 3.1 (acceleration is absolute in SR); stated ch09 §9.4 p.162 with lift experiments | ch10 §10.1 p.171 non-local (two-ball) lifts; ch16 §16.4 p.294 Einstein equivalence principle with its three clauses |
| Manifolds and metric | ch05 §5.2 informal manifold with charts and atlas | Metric, signature and index gymnastics in ch06 (from about §6.8); ch08 Minkowski as a flat manifold |
| Connection and parallel transport | ch06 §6.3 p.90 (affine connection via a "parallel" vector at a neighbouring point) | ch06 affine vs metric geodesics (Fig. 6.11, §6.10); ch07 §7.6 p.125 K-Lagrangian recipe |
| Curvature | ch06 §6.5 (Riemann tensor from the commutator of covariant derivatives), §6.7 p.96 (transport round an infinitesimal loop, affine flatness); identities §6.12 p.105; Weyl §6.13 | Physical meaning first given in ch10 §10.3 p.173 (geodesic deviation as relativistic tides) |
| Stress-energy | Foreshadowed ch04 ((E/c, p) transforms like (ct, x)); introduced as a source ch10 §10.8 p.184; variational definition ch11 | ch12 in full (dust §12.2 p.203, κ §12.3 p.206, dominant energy condition §12.9 p.214) |
| Field equations | ch10 (vacuum R_ab = 0 by tidal analogy, §10.4; full equations §10.8) | ch11 action; ch13 structure and Λ; ch14 constraints and evolution |
| Schwarzschild | ch15 §15.5 p.277 (algebra precomputed in Exercise 6.32) | ch16 tests; ch17 horizons; ch18 Kruskal |
| Orbits and tests | ch16 (redshift §16.2 p.290, perihelion §16.6 p.298, light bending §16.7 p.303, PPN §16.9 p.309) | Effective potential, ISCO and photon sphere appear only in ch16 exercises; effective-potential reasoning resurfaces in ch19 Fig. 19.5 and ch26 §26.1 |
| Black holes | ch17 (coordinate vs curvature singularity §17.2 p.323; Eddington-Finkelstein §17.6 p.328; black holes §17.8 p.332) | ch18 Kruskal and Penrose diagrams; ch19 RN; ch20 Kerr and global theorems |
| Gravitational waves | Previewed by Birkhoff (no monopole radiation, ch15 §15.6) and rubber-sheet ripples (ch16 §16.11); linearized theory ch21 §21.3 p.405 | ch22 exact waves; ch23 Bondi mass loss |
| Cosmology | Λ and the Einstein static universe first discussed in ch13 §13.3; ch24 (Newtonian cosmology §24.3 p.484, Friedmann §24.9 p.499) | ch25 model catalogue and horizons; ch26 ΛCDM and inflation |
| Advanced topics | Cauchy problem ch13 §13.5 p.223; 3+1 ch14; conformal compactification ch18 §18.4 p.347 | Komar and ADM mass and singularity theorems (ch20 §20.12-20.13); Petrov, peeling and optical scalars (ch23 §23.7-23.9); AdS (ch25 §25.9); inflation (ch26 §26.7) |

### Spiral and revisit structure

The book returns to its core ideas on purpose, and many chapters are explicitly "the same again with one new ingredient":

- **Special relativity three times:** from radar and k (ch02), by the conventional light-sphere route (ch03, with explicit back-references to the ch02 equations), and as a flat Lorentzian manifold with two axioms (ch08). ch08 closes each derivation by citing the Part A formula it reproduces (ch08 Signature moves).
- **Axioms edited, not replaced.** ch08 §8.5 splits SR into a geometry axiom and a physics axiom. ch10 §10.8 then defines GR by swapping one clause (flatness) for the field equations.
- **Field equations four ways:** heuristically (ch10), variationally (ch11), as a PDE system (ch13) and geometrically sliced (ch14).
- **Lift pictures reused:** the ch09 lifts return in ch10 with a second ball to isolate tides (ch10 Signature moves).
- **Radar method reused:** the k of ch02 reappears as the redshift ratio in ch16 §16.2 and as radar timing in a gravitational-wave spacetime (ch21 §21.12).
- **Black-hole template replayed:** the programme metric → singularity diagnosis → Eddington-Finkelstein → Kruskal → Penrose diagram is run on Schwarzschild (ch17-ch18), Reissner-Nordström (ch19) and Kerr (ch20). Each chapter introduces its constructions as analogues of the earlier ones.
- **Horizons in flat space first:** hyperbolic motion and its horizons (ch03 §3.8) are recalled for black holes (ch17) and for cosmological horizons (ch25 §25.7).
- **Energy-equation reasoning:** the g_00 curve as an effective potential (ch19 Fig. 19.5), Friedmann's equation read as a particle energy equation (ch25), and a bead in V(R̃) (ch26 §26.1).
- **Killing vectors:** built in ch07 §7.7, then used to define stationarity and staticity (ch15), for Kerr symmetries (ch20) and for wave symmetries (ch22).
- **Exercise 6.32** (Einstein tensor of a general spherical metric) is cashed in by ch15 and ch24.

---

## 4. Conventions and notation (consolidated)

### Signature, units, indices

- **Metric signature (+,−,−,−)**, which the book calls "signature −2". It is used from ch02 onward (ds² = dt² − dx² − dy² − dz²), with η_ab = diag(1,−1,−1,−1) (ch08) and u^a u_a = +1 (ch12, ch15). A flat 5D metric with one plus and four minus signs is called "signature −3" (ch18). The book says it follows the Landau-Lifshitz timelike convention and points to the convention table inside the cover of MTW (ch05 Notation).
- **Units.**
  - ch02 sets c = 1 through the radar definition of distance ("relativistic units").
  - ch03 and ch04 restore c and call this "non-relativistic units", meaning c is written explicitly.
  - From ch10 §10.8 onward, G = c = 1 and κ = 8π (ch10). With constants restored, κ = 8πG/c⁴ (ch12 §12.3).
  - Geometric mass is m = GM/c² (ch15).
  - Electromagnetism is declared Heaviside-Lorentz but uses Gaussian 1/4π and 1/8π factors (ch12). ch20's point-charge check uses Lorentz-Heaviside.
- **Index ranges.**
  - ch05 works in n dimensions with indices 1..n.
  - From ch07 on, Latin a, b, c run 0-3 with x⁰ timelike, and Greek α, β run 1-3 (spatial).
  - Bold indices (**i**, **j**) label tetrad legs and are moved with η_ij (ch06, ch10 §10.5, ch17, ch20).
  - In ch14's 2+2 sections, bold A, B = 0,1 and i, j = 2,3.
- **Primes go on the kernel letter, not the index:** x'^a, X'^a (ch05).
- **Special signs.**
  - Starred equality (=*) marks a relation valid only in special coordinates (ch06 onward; heavily used in ch11, ch14, ch15).
  - ≡ marks an identity.
  - := means "is defined as".
  - Comma denotes a partial derivative; semicolon or ∇ a covariant derivative.
  - Symmetrization (ab) and antisymmetrization [ab] brackets carry a 1/r! factor (ch05).

### Curvature and field-equation conventions

- **Riemann:** R^a_bcd = ∂_c Γ^a_bd − ∂_d Γ^a_bc + Γ^e_bd Γ^a_ec − Γ^e_bc Γ^a_ed, so that [∇_c, ∇_d] X^a = R^a_bcd X^b (ch06 Notation; restated ch10, ch11).
- **Ricci:** R_ab = R^c_acb, contracting the first and third indices (ch06, ch10). ch21 writes the same contraction as R_ab = η^cd R_cadb.
- **Einstein:** G_ab = R_ab − ½ g_ab R, with the contracted Bianchi identity ∇_b G^ab = 0 (ch06 §6.12).
- **Field equations with Λ:** G_ab − Λ g_ab = 8π T_ab (ch13 §13.3). The ch13 dossier notes that in (−,+,+,+) with the same Ricci convention this becomes G_ab + Λ g_ab = 8πT_ab, as in MTW.
- **Geodesic deviation:** D²ξ^a/Dτ² − R^a_bcd V^b V^c ξ^d = 0 (ch10). This is the same physics as the MTW form (ch10 Gaps).
- **Energy-momentum from an action:**
  - ch11 writes I = ∫(L_G + 2κ L_M) dΩ with T^ab = (2/√−g) δL_M/δg_ab.
  - ch12 writes T_ab = −(2/√−g) δL_M/δg^ab.
  - The scalar-field Lagrangian carries a sign opposite to the usual particle-physics form, and ch11 and ch12 agree with each other on it (ch11, ch12 Notation).
  - The Maxwell field is F_ab = ∂_b φ_a − ∂_a φ_b, an index order that differs from common usage (ch12).
- **Perfect fluid:** T_ab = (ρ + p) u_a u_b − p g_ab (ch24).
- **Weak field:** g_00 = 1 + 2φ/c² (ch10 §10.6).

### Distinctive symbols and names

- **Lorentz factors:** β(v) is the factor for the relative speed of two frames; γ(u) is the factor for a particle's speed (ch03, ch04, ch08). Most other books use γ for both.
- **Relativistic mass** m = γm₀, with m₀ the rest mass, is used without caveat (ch04, ch08, ch12).
- **Law and principle labels:** N1 (ch02); N2, N3, UG (ch04); Postulates I and II (ch02); M1-M3 and P1-P4 (ch09); Axioms I(i)-(iii) and II(i)-(iii) (ch08).
- **Density conventions:** Jacobian J taken old-with-respect-to-new, so √−g has weight +1. Gothic (fraktur) letters denote densities. The alternating symbols ε^{0123} = ε_{0123} = +1 are not related by the metric (ch07).
- **Hypersurface geometry:** h_ab is the induced metric (negative definite), γ = −h is positive definite, and K is minus the projected gradient of the unit normal. The lapse is written N (also α), the shift β^a (ch14).
- **Black-hole symbols:** charge is ε, not Q (ch19, ch20). Null coordinates are v (advanced) and w (retarded) (ch17-ch19). Kerr uses ρ² = r² + a² cos²θ and Δ = r² − 2mr + a². The null tetrad is normalized l·n = +1, m·m̄ = −1 (ch20).
- **Wave symbols:** the + and × waves are called the "h22-wave" and "h23-wave", and the gauge is called "Lorentz gauge" (ch21). Plane-wave null coordinates u = t − x, v = t + x give a flat metric du dv (ch22).
- **Cosmology symbols:** R(t) is the scale factor (colliding with the Ricci scalar). d_A means *absolute* (proper) distance. d_L = r₁R₀ without the (1+z) factor (ch24-ch26). Density parameters are Ω_r, Ω_m, Ω_Λ, and Ω_c = −k/(H₀²R₀²) (ch26).
- **Conformal infinity:** 𝒥± ("scri"), i±, i⁰ (ch18). Petrov type O is drawn as "0" (ch23).
- **Typography:** key results sit in tinted or grey panels. Figures and captions sit in the wide outer margin. Exercises are keyed "N.M (§N.K)" to a section (ch01, ch02 Notation).

### Internal inconsistencies found by the dossiers

1. **Equivalence-principle naming is reversed.** ch09 calls universality of free fall the "strong" principle and universal coupling the "weak" one, which is the opposite of modern usage and of the book's own ch16 §16.4 (ch09 Gaps).
2. **Sign of constant curvature.** With the book's field equations and signature, de Sitter has K < 0, yet ch25 labels K > 0 de Sitter and K < 0 anti-de Sitter (ch25 Gaps).
3. **4-momentum index placement.** The canonical 4-momentum in ch08 has the wrong exponent, and p_a = (E, **p**) does not fit signature −2 (ch08 Gaps).
4. **Index moving in ch14.** §14.10 says Greek indices are moved with γ, but several equations carry the signs that result from moving with h. The note after (14.31) claiming the Hamiltonian constraint is unchanged under h → −h fails for ³R (ch14 Gaps).
5. **Electromagnetic units:** Heaviside-Lorentz declared, Gaussian factors used (ch12).
6. **Poisson's equation:** printed with 8πGρ on ch10 p.183, but (4.5) has 4πGρ (ch10 Gaps).
7. **Hypersurface character naming.** ch17 calls a level hypersurface "timelike" when g^(a)(a) > 0, i.e. it names the hypersurface after its normal, which is non-standard (ch17 Gaps).
8. **A 2D theorem applied beyond its statement.** ch18 cites a theorem from ch06 §6.13 that is stated only for Riemannian 2-metrics, and applies it to a Lorentzian 2-space (ch06 Gaps).
9. **Signature slips.** A parenthetical cylinder metric in ch18 is written with (−,+,+) against the book's signature (ch18 Gaps). ch07 uses "Riemannian manifold" loosely to include the Lorentzian case (ch07 Notation).
10. **Propagation direction flips** between x and z in ch21, so h22 and h23 refer to different axes in different sections (ch21 Gaps).
11. **Stale first-edition cross-references:**
    - ch13 points to §22.3 for Newtonian cosmology (now §24.3).
    - ch17 points to "Chapters 18 and 19" for charged and rotating holes (now ch19 and ch20).
    - ch24 and ch25 point to "Chapter 25" for modern cosmology (now ch26).
12. **Heavily overloaded symbols:**
    - λ has three meanings, and ρ and φ two each (ch15).
    - k is both a redshift ratio and a conserved quantity, m both a reduced mass and GM/c², and ε has three meanings (ch16).
    - n and m are both tetrad legs and hypersurface normals (ch20).
    - U, V and W are recycled for Killing vectors, coordinates and metric functions (ch22).
    - θ is both the polar angle and the expansion scalar (ch23).
    - τ is both reception time and conformal time (ch25).
    - K is recycled across the Newtonian and relativistic tidal tensors (ch10).
13. **Misc terminology.** The Euler-Lagrange equations of a particle are called "field equations" (ch08). The Euler equation is called Navier-Stokes (ch12). The Level 2 bar in ch26 covers far less than the text says (ch26 Gaps).

---

## 5. Pedagogical signature

**Recurring explanatory moves**

- **Operational definitions before formulas.**
  - Coordinates come from a radar protocol, so c = 1 follows from the definition of distance (ch02).
  - Mass is measured by mutual accelerations (ch04 §4.1).
  - Stationarity is defined by a Killing vector (ch15).
  - The stationary limit is found by making a photon circle at fixed r and θ (ch20 §20.8).
  - The lapse is read as proper time per coordinate time (ch14 §14.9).
- **Principles as numbered, boxed statements, often impossibility statements** (ch02 Postulates I and II; ch09 M1-M3 and P1-P4; ch08 Axioms; ch24 cosmological principle and Weyl's postulate). Competing versions are numbered so they can be checked against the finished theory later (ch09).
- **Newtonian first, then the relativistic upgrade:**
  - Newtonian tides written in index form before geodesic deviation (ch10 §10.2).
  - Binet's equation before the relativistic orbit equation (ch16 §16.5-16.6).
  - Newtonian cosmology before Friedmann (ch24 §24.3).
  - The Newtonian dark star before the black hole (ch17 §17.9).
- **Analogy as a conjecture generator, then a consistency check.** R_ab = 0 is guessed from Laplace's equation read as a trace condition, then tested against the Newtonian limit (ch10). T_ab ansätze are fixed by classical limits (ch12).
- **Prove in special coordinates, then promote to all coordinates:** geodesic coordinates for the Palatini identity (ch11), adapted charts marked with =* (ch15), and the flatness theorems (ch06).
- **Rehearse on a toy first.** The flat wave equation is solved by Taylor series before the Einstein Cauchy problem (ch13 §13.5). The trivial Lagrangian √−g is worked before √−g R (ch11 §11.3).
- **Counting arguments as narrative:** 10 equations − 4 identities − 4 coordinate functions (ch13); degrees of freedom falling from 10 to 2 (ch14).
- **Deliberately show the ugly or misleading thing:** the brute-force expansion of √−g R (ch11); a page of computer-algebra output for R_00 (ch13 Fig. 13.4); the misleading Schwarzschild-coordinate diagram (ch17 Fig. 17.7); scrambled coordinate labels (ch17 §17.1).
- **Two independent routes to one answer:** the Lorentz transformation twice (ch02, ch03); the binary luminosity twice, both giving 128/5 (ch21 §21.9); tidal strain three ways (ch21 §21.12).
- **Template reuse with one new ingredient** (ch19, ch20; see section 3).
- **Honest closing surveys** that list objections and open problems (ch17 §17.12, ch20 §20.13-20.14, ch26 §26.9).

**Preferred representations.** Components and indices are the default (ch05 §5.1 justifies this). Spacetime diagrams with 45° light rays dominate Parts A and D. Penrose diagrams become the global language from ch18 on. Embedding diagrams appear in ch16 §16.11, ch18 §18.3, ch24 §24.8 and ch25 §25.9. Energy-line and potential plots appear in ch19, ch25 and ch26. The main geometric (index-free) excursions are ch05 §5.10 and ch14.

**Analogies and thought experiments.**
- Classic thought experiments recast: Einstein's train (ch02 §2.10), a three-observer clock relay that takes acceleration out of the picture (ch02 §2.12), Newton's bucket and "hold the bucket still and spin the universe" (ch09 §9.2), four lift cases arranged as two matched pairs (ch09 §9.4), a gravitational perpetual-motion bucket chain (ch16 §16.2), the hole argument (ch13 §13.8), the explorer behind a cosmological "curtain" (ch25 §25.7), and the traveller through a charged or rotating hole (ch19, ch20).
- Analogy strength is uneven: strong ones include the reversed Pythagoras of the metric's minus signs (ch03) and the vase-and-television no-hair cartoon (ch20); weak ones include the Hawking-pair picture (ch20) and the dominant energy condition tied to sound speed (ch12).

**Figure style.**
- Black-and-white line drawings in the outer margin, with paraphrasable captions (ch02 Notation).
- Conventions (ch17 Notation): time vertical, light rays at 45°, wavy lines for curvature singularities, hatching for matter, perspective ellipses for circular fronts.
- Cartoon strips carry the physics in ch09 (Galileo, lifts), ch10 (two-ball lifts), ch15 (gas in a pipe), ch17 (astronaut) and ch20 (Penrose-process engineering, no-hair).
- Late chapters reproduce observational data: Hulse-Taylor (Fig. 21.5), GW150914 (Fig. 21.12), Sandage's Hubble diagram (Fig. 24.13), Planck (Fig. 26.4) and Liddle's Ω plane (Fig. 26.2, Fig. 26.5).
- Pure-maths chapters are almost figure-free: ch11 has none, ch12 one, ch07 two.

**Worked-example style.** There are no labelled "Example" boxes (the dossiers' worked-example labels are all null). Worked calculations are woven into the running text and end in a boxed result. Routine steps are handed off with inline "(exercise)", "(check)" and "(why?)" prompts, so the argument is completed in the exercise list (ch06, ch07, ch11, ch14 Signature moves). The running numerical example is rare. A tutor can supply one, for example v = 0.6, k = 2 in ch02 (ch02 tutor notes).

**Exercise style.**
- Roughly 369 exercises, keyed to sections. Most fill in omitted steps (ch01 §1.1).
- Part B exercises are declared mandatory (ch05 §5.1). ch06 alone has about 32.
- Several exercises are load-bearing for later chapters: Exercise 6.32 (spherical Einstein tensor) feeds ch15 and ch24; Exercise 6.31 gives the Lorentzian 2D conformal-flatness result that ch18 needs.
- Major results live only in exercises: the Killing-vector count in flat space (ch07, ch08 Exercise 8.5), the effective potential, ISCO and photon sphere (ch16), and the Friedmann equations themselves (ch24).
- ch01's exercises are research-literacy tasks: browsing Living Reviews and arXiv gr-qc, and reading an Einstein biography.
- The dossiers record no solutions.

**Margin notes.** 202 margin notes were catalogued: clarifications 43, references 38, forward pointers 32, cautions 23, technical details 15, backward pointers 11, historical 7, humour 4. Neither ch23 nor ch25 has any recorded margin notes. Examples: N1 in a shaded panel and the etymology of *c* (ch02 §2.4, §2.6).

---

## 6. Best explanations by topic

| Topic | Unit(s) and locator | Why this treatment is especially good |
|---|---|---|
| Radar coordinates and the k-factor | ch02 §2.7 p.19 (Figs 2.7-2.9) | Coordinates come from a clock plus a flashlight. One measurable ratio k is the primitive, velocities are derived from it, and k's compose by plain multiplication. The boost reads as a stretch along one light direction and a squeeze along the other (ch02 Gems). |
| Relativity of simultaneity | ch02 §2.10 p.22 (Fig. 2.12) | Shown with the observer's own radar times (equal round trips, different start times), not as a light-delay illusion. Tutor warning: the train passage in the same section mislabels events (ch02 Gaps). |
| Clock paradox without acceleration | ch02 §2.12 p.24 (Fig. 2.15) | Three inertial observers with a clock-reading handover remove the "acceleration did it" escape. Objections are posed and dismantled one by one. |
| Boost as hyperbolic rotation; calibration | ch03 §3.1 p.31, §3.6 p.38 (Figs 3.1, 3.7) | cos/sin become cosh/sinh, so rapidity adds and velocity addition is a tanh identity. Invariant hyperbolae calibrate every frame on one diagram. |
| Twin paradox | ch03 §3.9 p.42 (Figs 3.9-3.10) | Resolved three ways in a row: the jump in the traveller's simultaneity lines, a numerical estimate, and the minus signs of the metric (the bent world-line is shorter in proper time). |
| Tensors from prototypes | ch05 §5.5-5.6 p.71-72 | A curve tangent and a gradient are expressed in two charts; the chain rule gives the transformation law, which is promoted to the definition. Invariance proofs go by cancelling matrices into δ. Arrows live in the tangent space (Fig. 5.6). |
| Why derivatives need extra structure | ch06 §6.2-6.3 p.86-90 | One diagnosis (subtracting tensors at different points) motivates the Lie derivative, the connection and the metric. The connection is defined through a triangle of arrows at Q (Fig. 6.5). |
| Curvature as loop holonomy; flatness | ch06 §6.5, §6.7 p.96 (Figs 6.8-6.9) | Curvature is the second-order failure of a vector to return round a tiny parallelogram, computed by Taylor expansion. Flatness comes from a parallel frame whose dual covectors are gradients. |
| Geodesics via the K-Lagrangian | ch07 §7.6 p.125 | The square-root Lagrangian is used first to expose the reparametrization term, then K = ½ g ẋẋ as the efficient recipe; Christoffel symbols are read off the Euler-Lagrange equations. This recipe is reused through ch16-ch17. |
| SR as geometry and axioms | ch08 §8.5 p.142 | Two short axioms (geometry, then physics) are written so that GR differs by one clause. Flat space in polar coordinates separates non-zero Γ from curvature. |
| Principles of GR | ch09 §9.2-9.4 p.154-162 | Newtonian "coincidences" (inertial force ∝ m; m^I = m^P; inertial frames not rotating relative to the stars) are treated as clues. Three masses are distinguished. Christoffel terms are read as inertial forces, so the metric is the potential. |
| Vacuum field equations from tides | ch10 §10.2-10.4 p.172-175 | Newtonian deviation with a trace-free tidal tensor mirrors geodesic deviation symbol by symbol. Requiring the trace condition for every observer yields R_ab = 0, then checked in the Newtonian limit (§10.6 p.178). |
| Bianchi identity from covariance | ch11 §11.2 p.188 | The divergence-free Euler-Lagrange tensor follows from the coordinate invariance of any action before a Lagrangian is chosen. The fourth-order puzzle is resolved by a total divergence (§11.5). |
| Fixing κ and reading T^ab | ch12 §12.2-12.3 p.203-206 | T^00 = γ²ρ₀ is explained as more energy per particle times fewer cubic metres per particle. Rows of the 4×4 matrix read as conservation laws. Trace reversal plus g_00 produces the 8π. |
| Structure of Einstein's equations | ch13 §13.2-13.6 p.218-226 | The balance sheet of equations, identities and gauge. Dust conservation gives geodesic motion in four lines. Locating second time derivatives exposes gauge and constraints at once. Constraints persist because zero stays zero. |
| Hole argument | ch13 §13.8 p.231 (Fig. 13.3) | Points get identity only from the metric; the resolution is pictured as a deformed grid. |
| 3+1 split | ch14 §14.4-14.10 p.243-252 | Layered geometry: a slice (h, K), then a foliation (lapse, Ricci equation), then threads (shift). A curvature "scorecard": Gauss, Codazzi and Ricci supply the tangential, one-normal and two-normal components. The lapse-shift triangle (Fig. 14.4). |
| Static vs stationary; Birkhoff | ch15 §15.1 p.269, §15.6 p.279 | Gas in a pipe (pumped, steady, still) anchors the three notions. A reflection argument kills cross terms. The leftover h(t) is pure coordinate choice, which is exactly why a spherical vacuum is static. |
| Redshift, perihelion, light bending | ch16 §16.2 p.290, §16.6 p.298, §16.7 p.303 | Redshift from an energy-conservation paradox and crest counting in world time. The secular term resummed into a rotating ellipse. Deflection read from the asymptote angles. The PPN split shows which half of the bending is space curvature (§16.9). |
| Reading a black-hole metric | ch17 §17.1-17.6 p.321-328 (Figs 17.7, 17.8, 17.10) | Coordinates are classified by the sign of g^(a)(a). A curvature scalar arbitrates singularities. A misleading diagram is refuted by a proper-time plot. Coordinates are designed so ingoing light is straight. Light-cone diagrams are taught by stacking flat-space snapshots first (Fig. 17.4). |
| Kruskal and Penrose diagrams | ch18 §18.2-18.5 p.343-351 | One freedom (relabelling each null coordinate) drives both constructions. The arctan graph is the whole idea of compactification. Minkowski is compactified completely before black holes. The bridge opens and pinches off (Fig. 18.3). Trapped surfaces are defined by the areas of wave fronts (Fig. 18.11). |
| Causal structure from one graph | ch19 §19.2-19.4 p.357-361 (Figs 19.2, 19.3, 19.5) | The zeros and sign of g_00 give horizons and the time coordinate. Light-cone slopes are read as (1+f)/(1−f) without integrating. The same curve serves as an effective potential. |
| Kerr anatomy and mass | ch20 §20.5 p.374, §20.8 p.381, §20.12 p.388 | Spin is read off discrete symmetries. The gap between g_00 = 0 and g^11 = 0 is the ergosphere. The stationary limit is operational. The Komar mass is built by copying Gauss's law. Singularity theorems follow one three-slot template (§20.13). |
| Linearized waves and polarization | ch21 §21.2-21.4 p.403-410 | Gauge is introduced by the Maxwell analogy. Wave existence is argued from □ on Riemann, not on the gauge-dependent h. The × polarization is obtained by rotating the + line element 45°. Test masses stay at fixed TT coordinates while their proper separation oscillates. |
| Quadrupole formula and orbital decay | ch21 §21.7-21.10 p.417-427 | Conservation does the physics (double divergence of stresses). The luminosity is computed twice. Hulse-Taylor data are confronted. (Correct the printed period-decay sign; see section 7.) |
| Exact waves and focusing | ch22 §22.3-22.5 p.454-457 | One wave in Rosen coordinates (a deforming grid) and Brinkmann coordinates (a fixed grid). The impulsive wave is two flat halves glued with a delta of curvature. The collision diagram is labelled by curvature type. |
| Nonlinear mass loss | ch23 §23.6 p.468 (Fig. 23.1) | The answer is drawn first (a world tube narrowing between null cones). Mass loss is minus an integral of a square, so the source loses mass exactly when the news is non-zero. |
| Petrov types, peeling, optical scalars | ch23 §23.7-23.9 p.471-474 | Each algebraic type gets a tidal fingerprint on a particle cloud. Peeling is shown as layers in 1/r. Optical scalars are a shadow that grows, rotates and shears. |
| Friedmann, redshift, distance | ch24 §24.3 p.484, §24.9 p.499, §24.10 p.502 | A Newtonian ball reproduces Friedmann's equation. The concave-graph tangent bounds the age. Two successive pulses give 1+z = R₀/R₁ with no velocity. Flux is dimmed by (1+z) twice. |
| Catalogue of models and horizons | ch25 §25.3 p.516, §25.7 p.523, §25.9 p.527 | Ṙ² = F(R) is read like a particle energy equation. One grid of sketches covers every (k, Λ). De Sitter's expansion is unmasked as a coordinate effect. The horizon appears as a limit of past light cones. The hyperboloid shows the flat slicing covers only half. |
| Ω plane, CMB, inflation | ch26 §26.1 p.539, §26.3 p.547, §26.7 p.560 | A bead in V(R̃) with energy Ω_c/2. The (Ω_m, Ω_Λ) map is built from theory, then data are overlaid. The black body stays black because ν/T is invariant. One horizon integral gives two answers (radiation vs exponential). Hubble friction is a rolling ball. |

---

## 7. Weaknesses and gaps

### Where novices stumble

- **The Part B wall.** ch06 (math 4, novice 2) builds connection, parallel transport, geodesics and curvature with no concrete example in the text: no sphere, no polar-coordinate plane. Physical meaning is withheld until ch10 (ch06 Gaps). ch07 packs three toolkits into 18 nearly picture-free pages (ch07 Difficulty).
- **Typographic distinctions that carry meaning.** Bold frame indices versus Roman coordinate indices vanish in handwriting and OCR (ch10 §10.5). The starred equality, β vs γ, and gothic densities are similar traps.
- **Compressed conceptual bridges.** The step from "Christoffel symbols are inertial forces" to "the metric must be curved" is short (ch09 §9.4). R_ab = 0 is easily mistaken for flatness (ch10 Misconceptions). The Newman-Janis trick is unmotivated (ch20 §20.2).
- **Delegated algebra.** Key steps sit in exercises:
  - the γ simplification (ch04);
  - the Friedmann equations (ch24);
  - the RN field equations (ch19 §19.1);
  - the Kruskal transformation (ch18, Exercise 18.2).
- **Survey sections with little derivation:** ch14 §14.12-14.14, ch20 §20.11-20.14, ch22 §22.5-22.6, and most of ch23.

### Dated or terse material

- **Relativistic mass framing** throughout ch04, ch08 and ch12, which later chapters and modern courses must undo (ch04 Gaps).
- **Numerical relativity** (ch14 §14.12): no weak-hyperbolicity diagnosis, BSSN, generalized harmonic formulation, moving punctures or the 2005 breakthrough.
- **Precision tests and GPS** (ch16): quoted precisions are dated. The GPS fractional effects are printed about 100 times too large, and the two effects are wrongly said to act in the same direction.
- **Black-hole astrophysics** (ch17 §17.11): the Event Horizon Telescope is called optical; neutron-star and Cygnus X-1 masses are outdated; the Galactic Centre radius and density figures are wrong; there is no 2020 Nobel or Sgr A* image.
- **Gravitational-wave survey** (ch21 §21.13-21.14): frozen at about 2020. It wrongly says LIGO could see supermassive mergers, ignores Hulse-Taylor eccentricity (a factor of about 12), predates the 2023 pulsar-timing background, and gives the old LISA timeline.
- **Bondi-era framing:** peeling presented as universal and BMS only mentioned (ch23). Colliding-wave singularities presented as generic (ch22 §22.6).
- **Cosmology numbers:** H₀ = 72 ± 8, "10 billion years", and a d_L convention that clashes with modern papers (ch24-ch26).
- **Dated statements:** every known matter field is said to obey the dominant energy condition (ch12 §12.9). Computer-algebra tools are 1980s-vintage (ch13 §13.9).

### Printed errors found (selection; see each dossier's Gaps)

- **ch03 p.39:** skew angle written tan(v/c) for arctan(v/c); swapped coordinate reading rule; unlabelled point E.
- **ch04:** the verbal statement of universal gravitation omits the square.
- **ch08:** relativistic-mass exponent sign; y = r sin θ sin φ printed as x; Hamiltonian written u·u − L.
- **ch10 p.183:** Poisson's equation with 8πGρ; (10.38) missing τ.
- **ch11:** Exercise 11.10 index and sign misprints.
- **ch13:** (13.15) missing 1/n!.
- **ch14:** (14.87), (14.89)-(14.90) metric blocks; (14.121) prints −18 for −1/8; (14.142) wrong power in the conformal 2-structure.
- **ch15:** (15.77) prints r for R; (15.41) exponent reversed.
- **ch16:** (16.76) dt² for dr²; (16.79) sign; (16.82) D_S vs D_S².
- **ch18:** Kruskal pinch-off time and compactification range.
- **ch19:** (19.32) exponents halved.
- **ch20:** (20.33), (20.43); Hawking temperature scale printed proportional to M; Komar sign.
- **ch21:** (21.147) period-decay sign (a shrinking orbit is said to lengthen the period); resonance factors; fringe intensity; (21.179).
- **ch22:** (22.9) exponential weight sign; Weber-Wheeler γ missing a square; the claim that one can move from region II into III is impossible causally.
- **ch24:** (24.26) Ricci components garbled; the acceleration-equation recipe reversed.
- **ch25:** (25.1) ΛṘ/3 for ΛR²/3; p = 3ρ for radiation; conformal-time range for k = +1.
- **ch26:** Planck peak condition; "Ω_m = 0.7" in the age formula; T_eq; (26.62) exponent sign; (26.71) missing 8π.

### Omissions

- **Maths toolkit:** differential forms (ch05); a physical reading of Riemann, Ricci and Weyl in ch06; Noether's theorem, the Gibbons-Hawking-York boundary term, and Lovelock's theorem as the justification for √−g R and G_ab (ch11, ch13); Frobenius' theorem is never named (ch15, ch22); the word "diffeomorphism" is absent from the hole argument (ch13).
- **Tides and Schwarzschild:** tidal stretching along the fall line (ch10 Figs 10.3-10.4); Buchdahl's bound (ch15); Oppenheimer-Snyder collapse (ch17).
- **Orbits:** the effective potential and ISCO are left to exercises (ch16).
- **Black holes:** surface gravity, entropy S = A/4, and the tension between the area theorem and evaporation (ch20); off-axis Kerr global structure (ch20).
- **Waves:** eccentric-binary emission (ch21); C-energy and axis regularity (ch22).
- **Cosmology:** a particle-horizon formula (ch25); inflationary e-folds, the shrinking comoving Hubble radius, and reheating (ch26).
- **Quantum gravity survey:** loop quantum gravity, asymptotic safety and holography are not mentioned (ch01).

---

## 8. Visual language

**What the figures do well.**
- **Light-ray constructions carry proofs in Part A.** The k-factor, radar coordinates, simultaneity and the Lorentz transformation are all read off 45° zigzags (ch02 Figs 2.7-2.17).
- **One-diagram calibration.** Invariant hyperbolae compare any number of frames without redrawing (ch03 Fig. 3.7).
- **Build-up from flat space.** Flash snapshots are stacked into cones before curvature appears (ch17 Fig. 17.4). Minkowski is compactified before Kruskal (ch18 Fig. 18.9).
- **Honest "wrong" pictures.** The misleading Schwarzschild-coordinate diagram is shown on purpose (ch17 Fig. 17.7).
- **Graph-as-argument.** The g_00 plots and 1±f curves decide causal structure in ch19 (Figs 19.2-19.5). One grid of sketches catalogues every Friedmann model (ch25 Fig. 25.1).
- **Penrose diagrams as a common stage.** They are placed on the Einstein static cylinder for every cosmology (ch25 Figs 25.13-25.17).
- **Physical cartoons with bite:** the lifts (ch09-ch10), gas in a pipe (ch15 Fig. 15.1), the perpetual-motion buckets (ch16 Fig. 16.1), and a civilization mining a Kerr hole (ch20 Fig. 20.11).

**Limits.** All figures are static black-and-white drawings. The differential-geometry chapters have almost none (ch06 has no curved surface; ch07 has a blob; ch11 has none). Some key figures are only sketches: the horizon problem (ch26 Fig. 26.7) and the gravitational-wave spectrum with a reversed axis (ch21 Fig. 21.10). A few mislead: tides shown only sideways (ch10 Fig. 10.4), and the spatial analogue that reverses the inequality (ch02 Fig. 2.16).

### The 15 most redesign-worthy figures (ranked)

| # | Unit | Figure | Locator | Why it matters and the app idea |
|---|---|---|---|---|
| 1 | ch03 | Fig. 3.7 (calibration hyperbolae), with Fig. 3.6 | §3.6 p.38-39 | Reading skewed, rescaled axes is Part A's biggest conceptual hurdle (ch03 Difficulty). **Live Minkowski grid:** hyperbolae drawn once; the learner adds frames by rapidity, unit ticks snap to the hyperbolae, and a draggable event shows both coordinate pairs. |
| 2 | ch02 | Fig. 2.17 (two observers radar-coordinate one event), with Figs 2.8 and 2.12 | §2.13 p.25 | The book's signature derivation. **Lorentz from radar:** drag an event, see both observers' four radar times linked by factors of k, toggle to B's rest frame and watch the line of simultaneity tilt. |
| 3 | ch17 | Fig. 17.7 vs Fig. 17.10 | §17.4 p.326; §17.6 p.330 | The misleading-then-corrected pair is the heart of Part D. **Chart comparison lab:** the same null rays and infalling probe in Schwarzschild and Eddington-Finkelstein coordinates side by side, with a proper-time readout (linking to Fig. 17.8). |
| 4 | ch18 | Fig. 18.1 + Fig. 18.10 | §18.2 p.346; §18.5 p.352 | The global picture the rest of the book leans on. **Linked triple view:** Schwarzschild (t, r), Kruskal and Penrose panels share one cursor, world-line and light signals. |
| 5 | ch06 | Fig. 6.8 (path-dependent transport), with Fig. 6.9 | §6.7 p.96-97 | Supplies the concrete sphere the book never draws (ch06 Gaps). **Two-path transport on a sphere:** transported-vector mismatch vs enclosed area, and a loop-shrinker converging to the curvature component. |
| 6 | ch09 | Fig. 9.9 (four lift cases), with Figs 10.1 and 10.4 | §9.4 p.163; §10.1 p.171-172 | Equivalence and its failure in one scene. **Four-lift guessing game:** drop balls in a hidden situation, then widen the lift and add a ring of particles to reveal tidal squeeze *and* stretch (fixing Fig. 10.4's omission). |
| 7 | ch21 | Figs 21.2-21.3 (+ and × rings) | §21.4 p.410-411 | Polarization geometry is the gateway to detection. **Polarization playground:** h₊ and h× sliders with a phase dial (circular polarization), next to an electromagnetic comparison showing 45° vs 90°. |
| 8 | ch25 | Fig. 25.1 (table of Friedmann model sketches) | §25.3 p.517 | Replaces 14 static sketches with a continuous parameter space. **Live Friedmann explorer:** a (Λ/Λ_c, k) plane beside a numerically integrated R(t), with the book's labels marked. Pair with the ch26 Fig. 26.2 Ω-plane atlas. |
| 9 | ch19 | Fig. 19.5 (energy lines on g_00) | §19.4 p.361 | Shows the book's best graph-as-argument move. **Energy-line playground:** drag the energy level, a bead moves in r, and a linked Penrose ladder traces the world-line into the next universe (fixes the unflagged "new exterior" gap). |
| 10 | ch16 | Fig. 16.8 (precessing orbit) | §16.6 p.302 | Makes the secular-term resummation visible. **Integrator:** exact relativistic Binet solution vs first-order perturbation (which blows up) vs rotating ellipse, with a dial for ε. |
| 11 | ch03 | Fig. 3.8 (uniformly accelerated world-lines) | §3.8 p.42 | Horizons in flat spacetime seed ch17 and ch25; the book states them without proof (ch03 Gaps). **Rindler wedge explorer:** emit light from any event and see which hyperbolic observers it reaches; a radar tool shows constant radar distance. |
| 12 | ch14 | Fig. 14.4 (lapse and shift split of the evolution vector), with Fig. 14.3 | §14.10 p.252 | 3+1 is abstract and index-heavy. **Lapse-shift triangle builder:** paint a lapse profile and drag threading curves over flat or Schwarzschild slices; the induced metric blocks update live. |
| 13 | ch20 | Fig. 20.3 (nested Kerr surfaces) | §20.5 p.376 | Kerr has no 3D picture in the book. **Spin-dial anatomy:** a 3D cutaway of the stationary limit surfaces, horizons and ring in Kerr-Schild coordinates as a/m goes from 0 to 1 and beyond. |
| 14 | ch02 | Fig. 2.15 (clock paradox relay), with Fig. 2.16 | §2.12 p.24 | The spatial analogue (Fig. 2.16) silently reverses the inequality (ch02 Gaps). **Clock relay race with a Euclidean vs Minkowski toggle:** one drag handle bends both paths; the bent path gets longer in the plane and shorter in proper time. |
| 15 | ch26 | Fig. 26.7 (horizon problem) | §26.7 p.562 | The book's figure is a sketch, not a true conformal diagram (ch26 Gaps). **Conformal-diagram horizon lab:** our past cone, the last-scattering line and two sky points' cones, plus an inflation slider that extends conformal time downward until the cones overlap. |

---

## 9. Tutor guidance

### Learners this book suits

- **Mathematically inclined undergraduates and beginning graduates** who want every step derivable and are willing to do the exercises. The book's promise is that small steps plus persistence are enough (ch01 §1.5).
- **Self-studiers who want an explicit, layered reading plan** (ch01 §1.4) and a clear stopping point after Part C.
- **Learners heading toward mathematical relativity or numerical relativity.** The book prepares them through ch13-ch14 (Cauchy problem, 3+1, 2+2), ch18 (conformal methods), ch23 (Bondi, Petrov), and its explicit bridge to Hawking and Ellis (ch01 §1.6).
- **Visual or operational thinkers meeting SR for the first time.** The k-calculus (ch02) needs only algebra and diagrams (novice 4).

It suits less well learners who want geometric, index-free intuition before components; there Part B's components-first style (ch05 §5.1) may frustrate. It also suits less well anyone needing current observational numbers, since ch16, ch17, ch21 and ch26 are dated.

### Moments where the book's approach is the right tool

1. **First encounter with SR, or confusion about simultaneity and time dilation.** Use ch02's radar and k construction.
   - Start by asking how to measure distance with only a clock and a flashlight.
   - Keep v = 0.6 (k = 2) as the running example, as the ch02 tutor notes suggest.
   - Reach for ch03 hyperbolae only after that.
2. **"What is a tensor, really?"** Use the ch05 prototype-then-definition move: a tangent and a gradient in polar coordinates, then the cancellation into δ. Supply the concrete computations the text leaves to exercises.
3. **"Why curvature and not just a force?"** Walk the ch09 → ch10 chain:
   - the coincidences of Newtonian gravity;
   - Christoffel symbols as inertial forces;
   - two-ball lifts;
   - Newtonian deviation in index form;
   - geodesic deviation;
   - the trace condition for every observer.

   Ask the learner to label which principle drives each link, following the numbered recap of §10.7 and its exercise.
4. **"Why these field equations?"** Complement ch10 with ch11 §11.2: the Bianchi identity follows from covariance. Add Lovelock's theorem, which the book omits.
5. **"Are Einstein's equations deterministic? What are constraints?"** Use ch13's counting balance sheet and wave-equation rehearsal, then ch14's layered slice → foliation → threads picture.
6. **Horizons and coordinate artefacts.** Use the ch17 sequence: scrambled labels, the g^(a)(a) sign test, the misleading diagram refuted by proper time, then Eddington-Finkelstein. Follow with ch18's arctan-first compactification and ch19's graph reading.
7. **Cosmological dynamics.** Use the energy-equation readings (ch25 §25.3, ch26 §26.1) and the two-pulse redshift argument (ch24 §24.10), which avoids "galaxies flying through space".

### How the AI tutor should draw on DIV

- **Translate conventions every time.**
  - The signature is (+,−,−,−): flip signs of g_ab, of Λ's term and of the matter Lagrangian when quoting (−,+,+,+) sources.
  - DIV's β is the frame Lorentz factor; its d_L lacks (1+z), so its second-order Hubble law differs from modern formulas; its "strong/weak" EP labels in ch09 are reversed.
  - Replace relativistic mass with invariant mass, and E = γmc².
- **Pre-empt printed errors.** Before a learner verifies a DIV equation, check the Gaps list for that unit. Highest-traffic traps:
  - ch02 train passage;
  - ch03 p.39 reading rule;
  - ch10 Poisson's 8π;
  - ch14 metric blocks and h/γ signs;
  - ch16 GPS numbers and (16.79);
  - ch21 period-decay sign;
  - ch24 acceleration-equation recipe;
  - ch25 de Sitter curvature sign and p = 3ρ;
  - ch26 Planck peak and the Ω_m = 0.7 age slip.
- **Fill the concreteness gaps.** Give ch06 and ch07 a sphere and a polar plane: Christoffel symbols, transport round a latitude, Killing vectors of S². Show tidal stretching as well as squeezing (ch10). Supply the Friedmann-equation derivation (ch24) and the RN field equations (ch19).
- **Use the book's exercise philosophy, but scaffold it.** Keep "(exercise)" steps as active tasks for the learner, give hints the book does not, and reuse DIV's hierarchical advice: assume the earlier part, move on, come back (ch01 §1.4).
- **Keep the book's candour.** Mention open questions where DIV does (ch17 §17.12, ch26 §26.9), and update them with current facts: GW catalogues, EHT images, the Hubble tension, and the pulsar-timing background.
- **Paraphrase only.** Present DIV's arguments in your own words and your own worked numbers; quote at most one short sentence, rarely. Equations may be transcribed.
- **Map difficulty to learner state** using section 10. Offer ch09, ch16, ch17 and ch24 (novice 3-4) as re-entry points for a discouraged learner. Treat ch14, ch20 and ch23 as graduate material.

---

## 10. Unit index

Ratings are math / conceptual / novice-friendliness (1-5). Every dossier's verification verdict is "fixed".

| Unit | Title | Printed pp. | Math | Concept | Novice | One-line summary | Verdict |
|---|---|---|---|---|---|---|---|
| front | Foreword (Penrose) | n/a | n/a | n/a | n/a | One-paragraph endorsement praising clarity, illuminating diagrams and a gentle but comprehensive route to cosmology, rotating black holes and gravitational waves. | no dossier |
| ch01 | The organization of the book | 1-10 | 1 | 2 | 4 | Orientation: origin as lecture notes, Level 1/2 scheme, the Part A-F roadmap following Einstein's route, research sociology, study advice, prerequisites, and two authors' letters. | fixed |
| ch02 | The k-calculus | 11-30 | 2 | 3 | 4 | SR from radar coordinates and the Doppler ratio k: velocity addition, simultaneity, light cone, clock paradox, Lorentz boost, invariant interval. | fixed |
| ch03 | The key attributes of special relativity | 31-48 | 2 | 3 | 3 | Conventional Lorentz derivation, rapidity, contraction and dilation, calibrated diagrams, hyperbolic motion and horizons, twin paradox, Doppler. | fixed |
| ch04 | The elements of relativistic mechanics | 49-61 | 2 | 3 | 3 | Relativistic mass from a symmetric sticking collision, E = mc², the energy-momentum invariant and its transformation, photons, E/ν invariance. | fixed |
| ch05 | Tensor algebra | 62-84 | 3 | 3 | 3 | Charts, Jacobians, summation convention, contravariant and covariant tensors from tangent and gradient prototypes, tensor algebra, tangent spaces, Lie bracket. | fixed |
| ch06 | Tensor calculus | 85-114 | 4 | 4 | 2 | Lie derivative, affine connection, parallel transport, geodesics, Riemann and flatness theorems, metric and Levi-Civita connection, Bianchi, Ricci, Einstein, Weyl. | fixed |
| ch07 | Integration, variation, and symmetry | 115-132 | 4 | 3 | 2 | Tensor densities and invariant volume, covariant divergence theorem, Euler-Lagrange equations and the K-Lagrangian for geodesics, Killing's equation. | fixed |
| ch08 | Special relativity revisited | 133-152 | 3 | 3 | 2 | Minkowski space as a flat manifold, null-cone classification, Lorentz and Poincaré groups, proper time, two-axiom SR, variational particle mechanics and 4-vectors. | fixed |
| ch09 | The principles of general relativity | 153-170 | 2 | 4 | 4 | Mach, equivalence (lifts), general covariance, minimal coupling and correspondence; Christoffel symbols as forces, the metric as potential. | fixed |
| ch10 | The field equations of general relativity | 171-186 | 4 | 3 | 3 | Newtonian tides in index form, geodesic deviation, R_ab = 0 by analogy, freely falling tetrad, Newtonian limit, G^ab = κT^ab, GR as edited axioms. | fixed |
| ch11 | General relativity from a variational principle | 187-202 | 4 | 4 | 2 | Palatini identity, Bianchi identity from covariance, varying √−g R directly and indirectly, second-order nature, Palatini variation, variational T^ab. | fixed |
| ch12 | The energy-momentum tensor | 203-216 | 4 | 3 | 2 | Dust, perfect fluid and Maxwell sources; κ from the Newtonian limit; tensor Maxwell theory and its Lagrangian; eigenframe of T_ab; dominant energy condition. | fixed |
| ch13 | The structure of the field equations | 217-238 | 4 | 4 | 2 | Under-determinacy and gauge, non-linearity, Λ, motion from conservation, Cauchy problem (analytic and harmonic), hole argument, equivalence problem, exact solutions. | fixed |
| ch14 | The 3+1 and 2+2 formalisms | 239-268 | 5 | 4 | 2 | Induced metric and extrinsic curvature, Gauss-Codazzi-Ricci, lapse and shift, ADM evolution and constraints, conformal data and gauges, sketch of 2+2. | fixed |
| ch15 | The Schwarzschild solution | 269-288 | 4 | 3 | 2 | Invariant definitions of stationary, static and spherical; reduction of the metric; Schwarzschild and Birkhoff; isotropic coordinates; TOV and the constant-density interior. | fixed |
| ch16 | Classical experimental tests of general relativity | 289-318 | 3 | 3 | 3 | Redshift, perihelion advance, light deflection and Shapiro delay derived and compared with data; Einstein equivalence principle; PPN β, γ; rubber sheet and embeddings. | fixed |
| ch17 | Non-rotating black holes | 319-342 | 3 | 4 | 3 | Meaning of coordinates, coordinate vs curvature singularities, light-cone diagrams, Eddington-Finkelstein extension, horizons, collapse, tides, evidence and doubts. | fixed |
| ch18 | Maximal extension and conformal compactification | 343-354 | 3 | 4 | 2 | Kruskal extension and diagram, Einstein-Rosen bridge, conformal compactification of Minkowski, Penrose diagrams of Kruskal and collapse, trapped surfaces. | fixed |
| ch19 | Charged black holes | 355-366 | 4 | 4 | 2 | Reissner-Nordström from Einstein-Maxwell, horizon classification, EF-type diagram from light-cone slopes, repulsive core, maximal extension as an infinite Penrose ladder. | fixed |
| ch20 | Rotating black holes | 367-397 | 4 | 5 | 2 | Kerr via Newman-Janis, rotation, ring singularity, horizons and ergosphere, global structure, Kerr-Newman, no-hair, Penrose process, Komar and ADM mass, singularity theorems, Hawking radiation. | fixed |
| ch21 | Linearized gravitational waves and their detection | 398-450 | 4 | 4 | 2 | Linearized gauge and TT waves, + and × polarizations, retarded solution and quadrupole formula, binary waveform, Isaacson flux and orbital decay, detector response, detections. | fixed |
| ch22 | Exact gravitational waves | 451-460 | 4 | 4 | 2 | Einstein-Rosen cylindrical waves, plane waves in Rosen and Brinkmann forms, impulsive waves, Penrose-Khan and Szekeres colliding waves with singularities. | fixed |
| ch23 | Radiation from an isolated source | 461-478 | 5 | 5 | 2 | Bondi's nonlinear programme: characteristic null surfaces, radiation coordinates, news and exact mass loss; Petrov types, peeling, optical scalars, Goldberg-Sachs. | fixed |
| ch24 | Relativistic cosmology | 479-510 | 3 | 3 | 3 | Olbers and Newtonian cosmology, cosmological principle and Weyl's postulate, Robertson-Walker metric, Friedmann equations, redshift, luminosity distance, Hubble law. | fixed |
| ch25 | The classical cosmological models | 511-538 | 4 | 4 | 2 | Integrating and classifying dust Friedmann models; Einstein static, de Sitter, radiation and steady state; horizons; de Sitter and AdS as hyperboloids; Penrose diagrams; qualitative cosmic history. | fixed |
| ch26 | Modern cosmology | 539-572 | 3 | 4 | 3 | Ω parameters and the (Ω_m, Ω_Λ) plane via a potential, H₀, CMB, nucleosynthesis, dark matter, supernovae and CMB constraints to ΛCDM, thermal history, inflation, anthropics, open questions. | fixed |
