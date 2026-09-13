---
type: "concept"
id: "curvature-sign-conventions"
title: "Curvature sign conventions"
domain: "curvature"
tier: "core"
aliases: ["Riemann sign and index conventions", "curvature conventions", "MTW sign table", "sign switches"]
prerequisites: ["riemann-curvature-tensor", "ricci-tensor", "metric-signature-convention"]
leads_to: ["einstein-field-equations", "cosmological-constant", "geodesic-deviation-equation", "space-of-constant-curvature", "curvature-of-the-two-sphere", "einstein-hilbert-action"]
sources: ["dinverno:ch06", "legacy:lesson-what-a-tidal-instrument-measures", "legacy:manuscript-chapter-08-curvature-holonomy", "schutz:ch06"]
review: "fixed"
---

# Curvature sign conventions

> Textbooks make three independent sign choices: the signature of the metric, the overall sign of the Riemann tensor, and which pair of Riemann slots is traced to build the Ricci tensor. Those choices change the printed signs of the Ricci scalar, the cosmological-constant term and the geodesic deviation equation, but never a single prediction. Before mixing formulas from two sources, calibrate: a round sphere must have positive scalar curvature, and ordinary matter must make a small ball of falling dust start to shrink.

## Explanations by level

### Intuition

Physics does not care which way you write your minus signs, but equations do. Relativity textbooks each make a few bookkeeping choices, a bit like two shops that record refunds as negative or as positive numbers in their ledgers. Both ledgers describe the same money; the trouble starts only when you copy a line from one ledger into the other without translating. In general relativity there are three such choices: whether time or space gets the minus sign in the spacetime interval, which overall sign the main curvature tensor carries, and which of its slots are summed to make the smaller curvature tensors. A formula copied from another book can therefore come out with the wrong sign even though both books are right. The cure is to test your formulas on cases whose answer you know physically: the surface of a ball is curved like a globe, which our course calls positive curvature, and a cloud of dust left to fall freely under its own gravity starts to collapse, never to swell. The simplification here is that 'positive curvature' is itself a naming choice; what cannot change is the measured behaviour, such as triangles on a globe having angle sums above 180 degrees.

**Picture to hold:** Two ledgers recording the same purchases with opposite sign habits, and a trusted receipt (a globe, a collapsing dust cloud) used to check which habit each ledger follows.

**Assumes:** [[curvature]], [[metric-signature-convention]]

### Working

Our course uses signature (-,+,+,+), the Riemann tensor R^rho_{sigma mu nu} = d_mu Gamma^rho_{nu sigma} - d_nu Gamma^rho_{mu sigma} + Gamma Gamma terms, so that the commutator of covariant derivatives gives +R^rho_{sigma mu nu} V^sigma, and the Ricci tensor R_{mu nu} = R^rho_{mu rho nu} (upper index traced with the third slot). Schutz, Gifted Amateur and d'Inverno all share the Riemann formula and the Ricci contraction; d'Inverno alone flips the signature to (+,-,-,-). Track what each switch does. Flipping the signature (g -> -g) leaves Christoffel symbols, R^rho_{sigma mu nu} and the lower-index R_{mu nu} unchanged, but flips the Ricci scalar R = g^{mu nu} R_{mu nu}, the all-lower Riemann components, the trace T of the stress-energy tensor, and the written sign of the Lambda term (d'Inverno writes G_ab - Lambda g_ab = 8 pi T_ab, which is our G + Lambda g = 8 pi G T). Flipping the Riemann sign, or tracing the upper index with the fourth slot instead of the third, flips R_{mu nu} and R, so an author who does either must also write Einstein's equation with -8 pi G T to describe the same universe. Three quick calibrations test the Riemann sign and the Ricci slot together: the unit 2-sphere must give R_{theta theta} = +1 and R = +2; for slow, weak fields R_00 should come out as +nabla^2 Phi (with c = 1); and R_{mu nu} u^mu u^nu should equal +4 pi G (rho + 3p) for ordinary matter, so geodesic deviation makes dust converge. None of these three can see the signature, because the lower-index Ricci tensor and the components u^mu are untouched by g -> -g; to check the signature, look at the sign of u_mu u^mu (course: -1) or of R inside dust (course: +8 pi G rho).

**Picture to hold:** A switchboard with three toggles (signature, Riemann sign, Ricci slot) wired to a panel of warning lights: sphere scalar curvature, sign of the Lambda term, sign in the deviation equation, sign of R for dust.

**Assumes:** [[riemann-curvature-tensor]], [[ricci-tensor]], [[ricci-scalar]], [[christoffel-symbols]], [[metric-signature]]

### Formal

Let a source differ from the course by three independent signs: its Minkowski metric is s1 diag(-1,1,1,1), its Riemann tensor is s2 times the course expression (equivalently [nabla_mu, nabla_nu] V^rho = s2 R^rho_{sigma mu nu} V^sigma), and its Ricci tensor is s3 R^rho_{mu rho nu} (s3 = -1 corresponds to tracing the upper index against the fourth slot). Because Christoffel symbols are invariant under g -> -g, the source's curvature objects relate to ours as R^rho_{sigma mu nu} = s2 R^rho_{sigma mu nu}(course), R_{rho sigma mu nu} = s1 s2 (course), R_{mu nu} = s2 s3 (course), R^mu_nu = s1 s2 s3 (course) and R = s1 s2 s3 (course). The lower-index stress-energy tensor T_{mu nu} is the same in every convention once T_00 is required to be the positive energy density, while its trace T flips with s1. The same physics is then written G_{mu nu} + s1 s2 s3 Lambda g_{mu nu} = s2 s3 (8 pi G) T_{mu nu}, geodesic deviation reads D^2 xi^mu/d tau^2 = -s2 R^mu_{nu rho sigma} u^nu xi^rho u^sigma, and the tidal trace is R_{mu nu} u^mu u^nu = s2 s3 [4 pi G (rho + 3p) - Lambda]. Sign conventions for a positive-definite metric involve only s2 s3: a round sphere of radius a has R = s2 s3 (2/a^2). This parametrization is the idea behind the convention table on the inside cover of Misner, Thorne and Wheeler, to which d'Inverno refers. The course, Schutz and Gifted Amateur have (s1, s2, s3) = (+,+,+); d'Inverno has (-,+,+). Two cautions: the visible sign of a term also depends on slot order (R^a_{bcd} V^b V^c xi^d equals -R^a_{bdc} V^b xi^d V^c), so compare index positions before comparing signs; and a sphere check calibrates only s2 s3, never the signature, which needs a Lorentzian test such as the sign of R for dust or for de Sitter space.

**Picture to hold:** A three-bit label (s1, s2, s3) attached to every formula card, with a translation rule that multiplies each curvature object by its own product of bits.

**Assumes:** [[riemann-curvature-tensor]], [[ricci-tensor]], [[ricci-scalar]], [[einstein-field-equations]], [[geodesic-deviation-equation]], [[metric-signature-convention]]

## Prerequisites

- [[riemann-curvature-tensor]] — The overall sign and slot order of Riemann are the main things that differ between books.
- [[ricci-tensor]] — The choice of contracted slot fixes the sign of Ricci and everything built from it.
- [[metric-signature-convention]] — Signature is the first of the three switches and flips R, T and the written Lambda term.

## Leads to

- [[einstein-field-equations]] — The sign in front of 8 pi G T and of the Lambda term depends on all three switches.
- [[cosmological-constant]] — Learners meet G - Lambda g in (+,-,-,-) books and must recognise it as the same repulsive Lambda.
- [[geodesic-deviation-equation]] — Its visible sign depends on the Riemann sign and on slot order, and is calibrated by tidal physics.
- [[space-of-constant-curvature]] — The sign of the constant K for de Sitter and anti-de Sitter space depends on signature.
- [[curvature-of-the-two-sphere]] — The sphere is the standard calibration that fixes the product of Riemann and Ricci signs.
- [[einstein-hilbert-action]] — The sign of R, and so of the gravitational Lagrangian relative to matter, follows the conventions.

## Related

- [[ricci-scalar]] — Its sign is the quickest convention diagnostic, and it flips with signature.
- [[riemann-curvature-operator]] — The index-free definition via [nabla_X, nabla_Y] - nabla_[X,Y] fixes the Riemann sign without coordinates.
- [[ricci-identity]] — The commutator of covariant derivatives is where the Riemann sign is set.
- [[relativistic-tidal-tensor]] — Books define the tidal matrix with opposite signs, a common source of apparent disagreement.
- [[trace-reversed-einstein-equations]] — The trace relation R = -8 pi G T keeps its form but T and R both flip with signature.

## Key equations

### Course Riemann tensor and commutator

$$
R^\rho{}_{\sigma\mu\nu} = \partial_\mu \Gamma^\rho{}_{\nu\sigma} - \partial_\nu \Gamma^\rho{}_{\mu\sigma} + \Gamma^\rho{}_{\mu\lambda}\Gamma^\lambda{}_{\nu\sigma} - \Gamma^\rho{}_{\nu\lambda}\Gamma^\lambda{}_{\mu\sigma},\qquad [\nabla_\mu,\nabla_\nu]V^\rho = R^\rho{}_{\sigma\mu\nu}V^\sigma
$$

Fixes the overall Riemann sign: the derivative along the third slot enters with a plus sign, and the commutator of covariant derivatives returns +Riemann acting on the vector. *(SCH ch06 §6.5 p.157; GA ch11 §11.6 eqn 11.28 p.128; DIV ch06 §6.5 p.94)*

**Convention:** Identical in Schutz (Eq. 6.63), Gifted Amateur (eqn 11.28) and d'Inverno (§6.5); all follow MTW here.

### Course Ricci contraction

$$
R_{\mu\nu} = R^\rho{}_{\mu\rho\nu},\qquad R = g^{\mu\nu}R_{\mu\nu}
$$

The upper index is traced against the third slot; tracing against the fourth slot would give minus this tensor. *(SCH ch06 §6.6 Eq. 6.91 p.162; GA ch11 §11.5 eqn 11.26 p.127; DIV ch06 §6.12 (6.84) p.106)*

**Convention:** All three books contract first and third indices: SCH Eq. 6.91, GA eqn 11.26, DIV (6.84).

### Sign bookkeeping between conventions

$$
R_{\mu\nu} = s_2 s_3\,R^{(\mathrm{course})}_{\mu\nu},\qquad R = s_1 s_2 s_3\,R^{(\mathrm{course})},\qquad R_{\rho\sigma\mu\nu} = s_1 s_2\,R^{(\mathrm{course})}_{\rho\sigma\mu\nu}
$$

s1 is the signature sign, s2 the Riemann sign, s3 the Ricci-slot sign relative to the course. Christoffel symbols do not change under g -> -g, which is why R^rho_{sigma mu nu} carries only s2. *(DIV ch06 §6.8 p.100; DIV ch06 §6.12 p.106; SCH ch06 §6.5 p.158)*

**Convention:** Course, Schutz and Gifted Amateur: (+,+,+). d'Inverno: (-,+,+).

### Einstein equation in a general convention

$$
G_{\mu\nu} + s_1 s_2 s_3\,\Lambda\, g_{\mu\nu} = s_2 s_3\,8\pi G\, T_{\mu\nu}
$$

The same physical law written with each book's signs; with (+,+,+) it is the course equation G + Lambda g = 8 pi G T, and with d'Inverno's (-,+,+) it becomes G - Lambda g = 8 pi T (G = 1). *(SCH ch08 §8.1 p.184; GA ch17 §17.1 p.182; DIV ch13 §13.3 (13.5) p.220)*

**Convention:** Restore c^4 in the denominator of 8 pi G in SI units. T_{mu nu} with lower indices is convention independent once T_00 is the positive energy density.

### Calibration: the round sphere

$$
R^\theta{}_{\phi\theta\phi} = \sin^2\theta,\quad R_{\theta\theta} = 1,\quad R_{\phi\phi} = \sin^2\theta,\quad R = \frac{2}{a^2}
$$

For ds^2 = a^2(d theta^2 + sin^2 theta d phi^2) every correct course-convention computation gives positive values; a negative R signals a flipped Riemann sign or Ricci slot. *(GA ch11 Example 11.8 p.128; SCH ch06 Ex 6.29 p.167; legacy:manuscript-section-8-4-8-6-flatness-count-sphere-curvature)*

**Convention:** This test fixes only the product s2 s3; a positive-definite metric has no signature choice.

### Calibration: tides and focusing

$$
\frac{D^2\xi^\mu}{d\tau^2} = -R^\mu{}_{\nu\rho\sigma}u^\nu\xi^\rho u^\sigma,\qquad R^i{}_{0j0} \approx \partial_i\partial_j\Phi,\qquad R_{\mu\nu}u^\mu u^\nu = 4\pi G(\rho + 3p) - \Lambda
$$

A Newtonian tidal field and ordinary matter give definite signs: the Hessian of the potential, a positive trace inside matter, and convergence of freely falling dust. These test the Riemann and Ricci signs in a Lorentzian setting. *(SCH ch06 §6.5 Eq. 6.87 p.162; DIV ch10 §10.3 (10.21) p.175; GA ch35 §35.4 eqn 35.41 p.371; legacy:lesson-what-a-tidal-instrument-measures)*

**Convention:** Schutz writes the deviation as +R^alpha_{mu nu beta} V^mu V^nu xi^beta and d'Inverno as D^2 xi^a - R^a_{bcd} V^b V^c xi^d = 0; both equal the course form after swapping the last two Riemann slots.

## Conventions across the books

| Issue | Schutz | Gifted Amateur | d'Inverno | Course choice |
| --- | --- | --- | --- | --- |
| Metric signature | (-,+,+,+); eta = diag(-1,1,1,1), timelike vectors have negative norm (ch06 §6.2). | (-,+,+,+) throughout, u.u = -1. | (+,-,-,-), which the book calls signature -2; it notes that other authors use +2 (ch06 §6.8 p.100). | (-,+,+,+). When quoting d'Inverno, flip the signs of g_ab, of the Lambda term and of the trace T, and expect R to flip. |
| Overall sign and slot meaning of the Riemann tensor | R^alpha_{beta mu nu} = Gamma^alpha_{beta nu,mu} - Gamma^alpha_{beta mu,nu} + Gamma Gamma terms (Eq. 6.63), read as a machine fed a transported vector and two loop edges; a footnote warns that other books differ (§6.5 p.158). | R^mu_{nu alpha beta} = d_alpha Gamma^mu_{beta nu} - d_beta Gamma^mu_{alpha nu} + Gamma Gamma terms (eqn 11.28); first lower slot is the transported vector, last two label the loop plane. | R^a_{bcd} = d_c Gamma^a_{bd} - d_d Gamma^a_{bc} + Gamma Gamma terms, so [nabla_c, nabla_d] X^a = R^a_{bcd} X^b (§6.5 p.94). | Same as all three books (MTW form): [nabla_mu, nabla_nu] V^rho = +R^rho_{sigma mu nu} V^sigma. |
| Which Riemann slots are traced to form the Ricci tensor | R_{alpha beta} = R^mu_{alpha mu beta}, first with third (Eq. 6.91). | R_{nu beta} = R^mu_{nu mu beta}, upper index with third slot (eqn 11.26). | R_ab = R^c_{acb} = g^{cd} R_{dacb}, first with third (6.84); d'Inverno warns that some authors' Riemann or Ricci has the opposite sign (§6.12 p.106). | R_{mu nu} = R^rho_{mu rho nu}. Tracing with the fourth slot, or using the opposite Riemann sign (as in Weinberg's 1972 text), flips Ricci and R and forces G = -8 pi G T. |
| Written form of the Einstein equation with Lambda | G^{alpha beta} + Lambda g^{alpha beta} = 8 pi T^{alpha beta} (ch08 §8.1 p.184). | R_{mu nu} - (1/2) g_{mu nu} R = 8 pi T_{mu nu} - Lambda g_{mu nu}, Lambda moved to the right (ch17 §17.1 p.182). | G_ab - Lambda g_ab = 8 pi T_ab 'with our sign conventions' (ch13 §13.3 p.220); the minus sign comes from the signature, and positive Lambda is still repulsive. | G_{mu nu} + Lambda g_{mu nu} = (8 pi G/c^4) T_{mu nu}. |
| Visible sign of the geodesic deviation equation and of the tidal matrix | nabla_V nabla_V xi^alpha = R^alpha_{mu nu beta} V^mu V^nu xi^beta (Eq. 6.87 p.162), no separate tidal matrix. | D^2 n^mu/d lambda^2 = (-R^mu_{nu alpha beta} u^nu u^beta) n^alpha, with K^mu_alpha defined as the bracket, so D^2 n = +K n (ch35 eqns 35.38-35.40 p.371). | The second absolute derivative of xi^a equals R^a_{bcd} V^b V^c xi^d; with its tidal tensor K^a_b = R^a_{cbd} V^c V^d this reads D^2 xi + K xi = 0 (ch10 (10.21)-(10.23) p.175). | D^2 xi^mu/d tau^2 = -R^mu_{nu rho sigma} u^nu xi^rho u^sigma, with tidal tensor E^mu_rho = R^mu_{nu rho sigma} u^nu u^sigma (same sign as d'Inverno's K, opposite to Gifted Amateur's K). All three books state the same tensor law. |
| Sign of the Ricci scalar for matter and for constant-curvature spacetimes | Not discussed in the checked chapters; its (-,+,+,+) signature with MTW Riemann and Ricci conventions gives the course signs (dust R > 0, de Sitter R > 0). | R = -8 pi G T (ch13 §13.4 p.148), so dust with T = -rho has R > 0; de Sitter has R_{mu nu alpha beta} = K(g g - g g) with K = +1/alpha^2 and R > 0 (ch49 §49.7 p.540). | Same trace relation, but in (+,-,-,-) dust has T = +rho and R < 0, and de Sitter has K < 0; the book nevertheless labels K > 0 as de Sitter, a sign slip flagged in the dossier (ch25 §25.9 p.527). | Dust: R = +8 pi G rho. De Sitter: R = 4 Lambda = 12 H^2 > 0 with K = H^2 > 0. Always state the signature when quoting a sign of R for a Lorentzian spacetime. |

## How the sources teach it

### schutz

**Route:** Defines the Riemann tensor from parallel transport around a small loop, then flags in a footnote that authors differ in its overall sign and index order; defines the Ricci tensor by tracing first and third indices and remarks that other contractions vanish or give plus or minus Ricci. The sphere computation that would calibrate the sign is set as an exercise.

**Representation:** Component formulas derived in locally inertial coordinates, with Riemann read as a machine with slots for a vector and two loop edges.

**Strengths:** The warning sits exactly where the definition is made, and the slot reading lets a learner see why swapping two slots flips a sign. Its choices match MTW, the most common modern set.

**Weaknesses:** A footnote is easy to miss (it was even dropped from the text export), there is no translation table and no worked calibration; the learner must do Exercise 6.29 to see that the sphere comes out positive. *(SCH ch06 §6.5 p.158; SCH ch06 §6.6 p.162; SCH ch06 Ex 6.25 p.167; SCH ch06 Ex 6.29 p.167)*

### dinverno

**Route:** Sets the signature to -2 when the metric is introduced, noting that other authors use +2; closes the list of curvature tensors (Ricci, scalar, Einstein) with a one-sentence caution that some authors' Riemann or Ricci has the opposite sign. Earlier it states that it follows the Landau-Lifshitz timelike convention and points to the MTW convention table.

**Representation:** Terse remarks attached to boxed component definitions; no worked translation.

**Strengths:** Names both kinds of difference (signature and Riemann/Ricci sign) and points readers to a standard table, which is the right habit for self-study across sources.

**Weaknesses:** Its own later chapters show how easily signs slip: the de Sitter constant-curvature sign in ch25 and the sign of the spatial scalar curvature with a negative-definite induced metric in ch14. No calibration example is offered. *(DIV ch06 §6.8 p.100; DIV ch06 §6.12 p.106; DIV ch05; DIV ch13 §13.3 p.220; DIV ch25 §25.9 p.527; DIV ch14 §14.4 p.244)*

### gifted-amateur

**Route:** Does not treat conventions as a topic. It fixes the -+++ signature and MTW curvature sign early, compares the signature choice to a national driving-side rule, and its worked sphere example produces a positive scalar curvature that serves as an unannounced calibration.

**Representation:** Friendly analogy for signature; explicit component computations for the plane and the sphere.

**Strengths:** The sphere and polar-plane examples are exactly the calibration computations a learner should keep; the tidal matrix sign is spelled out when Ricci is reinterpreted.

**Weaknesses:** It defines its tidal matrix K with the opposite sign to d'Inverno's K without comment, and never warns what changes when a reader meets a +2 or opposite-Riemann text. *(GA ch01; GA ch11 §11.5 p.127; GA ch11 Example 11.8 p.128; GA ch35 §35.4 p.371)*

### legacy

**Route:** Chapter 8 of the earlier course computes the sphere's Riemann, Ricci and scalar curvature and uses R = 2/a^2 explicitly to pin the sign convention; the loop section discusses orientation and why loop order must be stated before comparing signs; the tidal-instrument lesson calibrates the curvature sign against a measured relative acceleration; the reference sheet collects formulas in one convention and proposes adding a translation note.

**Representation:** Operational sign fixing (sphere, tidal cloud), orientation diagrams for small loops, and a formula reference sheet.

**Strengths:** Treats signs as something you calibrate against geometry and measurement, not something you memorise; its sphere and octant hand checks were verified in review.

**Weaknesses:** The translation table to other textbooks was planned but never written; orientation caveats are scattered across sections. *(legacy:manuscript-chapter-08-curvature-holonomy; legacy:manuscript-section-8-1-8-3-riemann-commutator-and-loop; legacy:lesson-what-a-tidal-instrument-measures; legacy:manuscript-chapter-appendix-b-reference-sheet)*

## Recommended teaching path

1. **1. Motivating puzzle** — Show the same cosmological-constant equation as printed in d'Inverno (G - Lambda g = 8 pi T) and in Schutz (G + Lambda g = 8 pi T) and ask: does one book have Lambda attracting and the other repelling? *Why:* A concrete apparent contradiction makes the need for translation felt before any machinery. *(DIV ch13 §13.3 p.220; SCH ch08 §8.1 p.184)*
2. **2. Picture: three switches** — Name the three independent choices (signature, Riemann sign, Ricci slot) and show them as toggles in the switchboard demo, with the physical outcomes (a globe, a collapsing dust ball) fixed and unchanging. *Why:* Separating bookkeeping from physics is the core idea; the fixed physical panel prevents the learner from thinking signs change predictions. *(DIV ch06 §6.12 p.106; SCH ch06 §6.5 p.158; legacy:manuscript-chapter-appendix-b-reference-sheet)*
3. **3. Formalism: what each switch touches** — Show that Christoffel symbols survive g -> -g unchanged, so R^rho_{sigma mu nu} and R_{mu nu} do too, while R, T and the written Lambda term flip; then show that tracing a different slot or flipping the Riemann sign flips Ricci and forces a sign in front of 8 pi G T. Summarise with the s1 s2 s3 rule. *Why:* One short derivation replaces memorising a table and lets the learner translate any formula themselves. *(DIV ch06 §6.8 p.100; DIV ch13 §13.3 p.220; SCH ch06 Ex 6.25 p.167)*
4. **4. Check: sphere calibration** — Have the learner compute R^theta_{phi theta phi}, the Ricci components and R for a sphere of radius a, and confirm R = +2/a^2. Then ask what a book with the opposite Ricci slot would find. *Why:* The sphere is small enough to finish by hand and is the universal convention detector for the Riemann and Ricci signs. *(GA ch11 Example 11.8 p.128; SCH ch06 Ex 6.29 p.167; legacy:manuscript-section-8-4-8-6-flatness-count-sphere-curvature)*
5. **5. Check: a Lorentzian calibration** — First show that the physical focusing test, R_{mu nu} u^mu u^nu = 4 pi G rho > 0 for dust, comes out the same in (-,+,+,+) and (+,-,-,-): like the sphere, it checks only the Riemann sign and Ricci slot. Then calibrate the signature with a quantity that contains one inverse metric: the trace T and the scalar R. In (-,+,+,+) dust has T = -rho and R = +8 pi G rho; in (+,-,-,-) both signs reverse. *Why:* Learners must discover that neither the sphere nor dust convergence can see the signature, and learn which objects can: those with an odd number of metric factors. *(GA ch35 §35.4 eqn 35.41 p.371; GA ch13 §13.4 p.148; legacy:lesson-what-a-tidal-instrument-measures)*
6. **6. Application: translate a formula** — Translate three formulas into course conventions: d'Inverno's Lambda equation, d'Inverno's geodesic deviation equation (noting the slot swap), and the de Sitter constant-curvature sign. *Why:* Translation is the skill the learner will actually use when reading papers or other books. *(DIV ch10 §10.3 p.175; GA ch49 §49.7 p.540; DIV ch25 §25.9 p.527)*

## Analogies

- **Two ledgers with opposite sign habits** (intuition): One shop writes money coming in as positive, another writes money going out as positive. Both are correct and describe the same transactions, but a total copied from one ledger into the other without flipping signs is wrong. *Limits:* Relativity has three independent sign habits, not one, and different objects flip under different combinations; a single 'multiply by -1' rule does not work. *(DIV ch06 §6.12 p.106)*
- **Driving on the left or on the right** (intuition): A country's driving side is a convention: either works, but everyone on the same road must agree. The metric signature is chosen in the same spirit. *Limits:* Covers only the signature choice, not the Riemann sign or the Ricci slot; and unlike roads, mixing conventions in one calculation fails silently rather than visibly. *(GA ch01)*
- **Calibrating a thermometer against boiling water** (working): Before trusting an unlabelled scale you test it on something whose temperature you know. The round sphere and a collapsing dust cloud are the known reference points for curvature signs. *Limits:* A calibration point only tells you the product of signs it is sensitive to: the sphere detects the Riemann-times-Ricci sign but is blind to the signature. *(legacy:manuscript-chapter-08-curvature-holonomy; legacy:lesson-what-a-tidal-instrument-measures)*
- **A three-bit label on every formula card** (formal): Treat each book's conventions as a code (s1, s2, s3). Translating a curvature object means multiplying by the product of the bits it depends on, which is a small, checkable rule. *Limits:* The rule assumes the book's Christoffel symbols are the Levi-Civita ones and that T_00 is positive energy density; books that also change Lagrangian signs or index-placement habits need extra care. *(DIV ch05; DIV ch11 §11.1 p.187)*

## Misconceptions

- **There is one correct sign for the Riemann tensor, so a book with the other sign has made a mistake.** — The overall sign of Riemann, the Ricci slot and the signature are conventions; consistent books differ in signs while agreeing on every measurable prediction. *Why tempting:* Each book presents its definition as the definition, and identical symbols suggest identical objects. *Diagnostic:* Two books give the unit sphere scalar curvature as +2 and -2. Can both books still predict the same angle sum for a triangle on a globe? *(SCH ch06 §6.5 p.158; DIV ch06 §6.12 p.106)*
- **Flipping the metric signature flips the sign of every curvature quantity.** — Under g -> -g the Christoffel symbols, R^rho_{sigma mu nu} and the lower-index Ricci tensor are unchanged; the Ricci scalar, the all-lower Riemann tensor, mixed Ricci R^mu_nu and the trace T flip. *Why tempting:* Signature feels like a global minus sign, so learners expect it to multiply everything. *Diagnostic:* If you replace g_{mu nu} by -g_{mu nu}, what happens to Gamma^lambda_{mu nu}, to R_{mu nu} and to R? *(DIV ch13 §13.3 p.220; DIV ch14 §14.4 p.244)*
- **A minus sign in front of the Riemann term in one book's geodesic deviation equation means that book uses the opposite curvature sign.** — The visible sign also depends on slot order: R^a_{bcd} V^b V^c xi^d = -R^a_{bdc} V^b xi^d V^c. Schutz, d'Inverno, Gifted Amateur and the course all state the same law. *Why tempting:* Learners compare signs at a glance without checking which slot holds the separation vector. *Diagnostic:* d'Inverno writes D^2 xi^a - R^a_{bcd} V^b V^c xi^d = 0 and the course writes D^2 xi^mu = -R^mu_{nu rho sigma} u^nu xi^rho u^sigma. Rewrite one in the other's slot order and decide whether they disagree. *(DIV ch10 §10.3 p.175; SCH ch06 §6.5 Eq. 6.87 p.162; GA ch35 §35.4 p.371)*
- **If my sphere check gives R = +2/a^2, all my conventions match the course.** — A positive-definite sphere tests only the Riemann and Ricci signs together. Signature needs a Lorentzian check, for example the sign of R for dust or de Sitter space, or the sign of the Lambda term. *Why tempting:* The sphere check is advertised as the convention test, and it passes for d'Inverno too. *Diagnostic:* d'Inverno's sphere also gives +2/a^2. What value does its convention give for the Ricci scalar of a dust-filled region, and why does the sphere not reveal this? *(SCH ch06 §6.6 p.162; GA ch13 §13.4 p.148; DIV ch25 §25.9 p.527)*
- **The sign of the Lambda term tells you whether Lambda is attractive or repulsive in that book.** — G - Lambda g in (+,-,-,-) and G + Lambda g in (-,+,+,+) describe the same repulsive positive Lambda; the sign difference is the flip of g_{mu nu}. *Why tempting:* A minus sign looks like a physically different term. *Diagnostic:* Translate d'Inverno's G_ab - Lambda g_ab = 8 pi T_ab into (-,+,+,+). Is positive Lambda still an accelerating influence? *(DIV ch13 §13.3 p.220; GA ch17 §17.1 p.182)*
- **De Sitter space is 'positively curved', so its Ricci scalar is positive in every book.** — In (-,+,+,+) de Sitter has R = 4 Lambda > 0, but in (+,-,-,-) the same spacetime has R < 0 and constant-curvature K < 0. Words like 'positive curvature' for Lorentzian spaces need a stated convention. *Why tempting:* De Sitter space embeds as a hyperboloid often described as the Lorentzian cousin of a sphere. *Diagnostic:* Using R_{abcd} = K(g_ac g_bd - g_ad g_bc), what happens to K when g -> -g? *(GA ch49 §49.7 p.540; DIV ch25 §25.9 p.527)*

## Thought experiments

- **Two astronauts with two textbooks**: Two astronauts release identical dust clouds and each predicts the cloud's evolution using a different textbook, one with signature (-,+,+,+) and one with (+,-,-,-). One computes R > 0 in the dust, the other R < 0. *Lesson:* Both must predict the same shrinking cloud; the sign of R is a label, while the convergence rate R_{mu nu} u^mu u^nu is the same number in both books because the lower-index Ricci tensor and the four-velocity components do not change. *(GA ch35 §35.4 p.371; DIV ch10 §10.4 p.175)*

## Visualizations

### Convention switchboard · interactive-2d · high priority

A panel of three toggles (signature s1, Riemann sign s2, Ricci slot s3) next to a fixed physical scene: a globe with a geodesic triangle and a freely falling dust ball. As the toggles change, printed formulas and numbers update, but the physical scene never does.

**Interaction:** Learner flips toggles or picks a preset (Course/Schutz/Gifted Amateur, d'Inverno, an opposite-Riemann text). Readouts update live: sphere R_{theta theta} and R, the dust ball's R and R_{mu nu} u^mu u^nu, the written Einstein equation with Lambda, the deviation equation, the de Sitter K. A 'translate' button converts a chosen formula into course conventions with the multiplying signs highlighted.

**Model:** Course values multiplied by products of s1, s2, s3: R_{mu nu} by s2 s3, R by s1 s2 s3 (sphere: s2 s3), Lambda term by s1 s2 s3, 8 pi G T by s2 s3, deviation Riemann term by s2; dust convergence rate fixed at 4 pi G rho.

**Inspired by:** DIV ch06 §6.12 p.106; SCH ch06 §6.5 p.158; GA ch11 Example 11.8 p.128

**Legacy assets:** manuscript-chapter-appendix-b-reference-sheet

### Loop orientation and the sign of Riemann · interactive-3d · medium priority

A vector is parallel transported around a small loop on a sphere; the net rotation is shown against the loop's orientation and compared with the formula Delta V^rho = -R^rho_{sigma mu nu} V^sigma a^mu b^nu for the course convention.

**Interaction:** Learner draws or resizes a loop, reverses its direction, and toggles the Riemann sign convention. The rotation arrow on the sphere stays physical (it reverses only when the loop reverses), while the predicted sign from the formula flips with the toggle until the learner matches them.

**Model:** Exact Levi-Civita transport on a sphere of radius a; rotation angle equals enclosed signed area divided by a^2; small-loop formula uses R^theta_{phi theta phi} = sin^2 theta.

**Inspired by:** legacy:manuscript-section-8-1-8-3-riemann-commutator-and-loop; SCH ch06 §6.5 p.158

**Legacy assets:** scene-3d-parallel-transport-loop, manuscript-section-8-1-8-3-riemann-commutator-and-loop

### Dust-ball calibration strip · animated-2d · low priority

An animated strip where a small ball of dust released at rest inside matter shrinks, and a tidal cloud outside a planet stretches and squeezes. Beside each, the tidal tensor and its trace are printed in the chosen convention.

**Interaction:** Learner switches between book conventions and checks which printed sign of the trace corresponds to the shrinking seen on screen; a quiz asks which convention a mystery formula uses.

**Model:** Newtonian-limit tidal tensor E_ij = d_i d_j Phi; uniform dust interior E = (4 pi G rho/3) delta_ij; point-mass exterior E = (GM/r^3) diag(-2, 1, 1); xi'' = -E xi.

**Inspired by:** legacy:lesson-what-a-tidal-instrument-measures; DIV ch10 §10.4 p.175; GA ch35 §35.4 p.371

**Legacy assets:** lab-tidal-cloud-geodesic-deviation, lesson-what-a-tidal-instrument-measures

## Worked examples

- **Riemann, Ricci and scalar curvature of a sphere** (working): A full component computation that returns R^theta_{phi theta phi} = sin^2 theta, R_{theta theta} = 1 and R = 2/a^2, the standard calibration of the Riemann and Ricci signs. *(GA ch11 Example 11.8 p.128; legacy:manuscript-section-8-4-8-6-flatness-count-sphere-curvature)*
- **The flat plane in polar coordinates** (working): Non-zero Christoffel symbols but vanishing Riemann components; a control case showing that sign errors cannot hide behind cancellations when the answer must be zero. *(GA ch11 Example 11.7 p.128; SCH ch06 Ex 6.19 p.167)*
- **The cosmological term in two signatures** (working): d'Inverno's G_ab - Lambda g_ab = 8 pi T_ab and why it is the same equation as the course form once g_ab changes sign. *(DIV ch13 §13.3 p.220)*
- **Tidal tensor trace and the vacuum equation** (working): d'Inverno defines K^a_b = R^a_{cbd} V^c V^d, sets its trace to zero in vacuum and obtains R_ab = 0; comparing with Gifted Amateur's K (opposite sign) shows how tidal matrices differ by convention only. *(DIV ch10 §10.4 p.175; GA ch35 Example 35.8 p.371)*

## Exercises

- (standard) Show that every contraction of the Riemann tensor other than the Ricci one either vanishes or is plus or minus the Ricci tensor, and that Ricci is symmetric. *Skill:* Using Riemann symmetries to see how the choice of contracted slot changes the sign. *(SCH ch06 Ex 6.25 p.167)*
- (standard) Compute the Riemann tensor of a unit sphere using the single independent component in two dimensions; extend to Ricci and scalar curvature. *Skill:* Running the sphere calibration by hand. *(SCH ch06 Ex 6.29 p.167; GA ch11 Example 11.8 p.128)*
- (intro) Check that contracting the Einstein tensor with the metric gives minus the Ricci scalar, and use it to relate R to the trace of T. *Skill:* Tracing with the metric and seeing which quantities depend on signature. *(GA ch13 Ex 13.3 p.150)*
- (standard) Translate a set of formulas (Lambda equation, deviation equation, de Sitter curvature constant) from (+,-,-,-) sources into course conventions and verify with the dust and sphere calibrations. *Skill:* Applying the three-sign bookkeeping rule. *(DIV ch13 §13.3 p.220; DIV ch25 §25.9 p.527)*

## Checks for understanding

- **Q (intuition):** Two textbooks disagree about the sign of the Ricci scalar inside a star. Does one of them predict that a small ball of dust inside the star expands while the other predicts it shrinks?
  - **A:** No. The sign of the Ricci scalar depends on bookkeeping choices, mainly the metric signature. Both books predict that the dust ball starts to shrink, because the physically measured convergence rate is R_{mu nu} u^mu u^nu = 4 pi G (rho + 3p), which is the same number in both conventions. *(targets: There is one correct sign for the Riemann tensor, so a book with the other sign has made a mistake.)*
- **Q (working):** A text uses signature (-,+,+,+) and the course Riemann tensor, but defines Ricci as R_{mu nu} = R^rho_{mu nu rho}. What does it find for the Ricci scalar of a sphere of radius a, and how must it write Einstein's equation?
  - **A:** Tracing with the fourth slot gives R^rho_{mu nu rho} = -R^rho_{mu rho nu}, so its Ricci tensor and scalar are minus the course ones: R = -2/a^2 for the sphere. Since G_{mu nu} also flips while T_{mu nu} does not, it must write G_{mu nu} = -8 pi G T_{mu nu} (and G - Lambda g = -8 pi G T) to describe the same physics.
- **Q (formal):** Show that the Christoffel symbols are unchanged when g_{mu nu} is replaced by -g_{mu nu}, and deduce what happens to R_{mu nu}, R and the lower-index Riemann tensor.
  - **A:** Gamma^lambda_{mu nu} = (1/2) g^{lambda sigma}(d_mu g_{sigma nu} + d_nu g_{sigma mu} - d_sigma g_{mu nu}) contains one inverse metric and one derivative of the metric; both change sign, so Gamma is unchanged. R^rho_{sigma mu nu} is built only from Gamma, so it is unchanged, and so is R_{mu nu} = R^rho_{mu rho nu}. R = g^{mu nu} R_{mu nu} flips sign, and R_{rho sigma mu nu} = g_{rho lambda} R^lambda_{sigma mu nu} flips sign. *(targets: Flipping the metric signature flips the sign of every curvature quantity.)*
- **Q (working):** Your sphere check gives R = +2/a^2 in a book you are reading. Name one further check that would reveal whether the book's signature differs from the course, and state the course answer.
  - **A:** Use a Lorentzian test: compute R for pressureless dust from the traced field equation. The course gives T = -rho and R = +8 pi G rho; a (+,-,-,-) book gives T = +rho and R = -8 pi G rho. Equivalently, check the written sign of the Lambda term (course: G + Lambda g) or the sign of R for de Sitter space (course: +4 Lambda). *(targets: If my sphere check gives R = +2/a^2, all my conventions match the course.)*

## Applications

- **Reading research papers and other textbooks**: Before using a formula for the Einstein equation, the Raychaudhuri equation or a curvature invariant from another source, identify its three signs and translate; many published sign disagreements are convention mismatches. *(DIV ch06 §6.12 p.106; SCH ch06 §6.5 p.158)*
- **Unit tests for symbolic and numerical curvature tools**: Calibration geometries (plane in polar coordinates: R = 0; sphere: R = 2/a^2; Schwarzschild: Ricci = 0 with Kretschmann 48 M^2/r^6; flat FLRW: R = 6(a''/a + H^2)) catch sign and slot errors in code. Key numbers: Sphere R = 2/a^2; Schwarzschild Kretschmann 48 M^2/r^6 *(legacy:manuscript-section-24-3-calculation-checklist; legacy:engine-independent-curvature-checker)*

## Tutor guidance

**Opening questions**

- If two books print opposite signs in front of the cosmological constant, which of them do you think is wrong?
- What physical fact about a globe or a cloud of falling dust could you use to check a curvature sign?
- When you change the metric signature, which quantities do you expect to change sign?

**Common questions**

- *Why don't physicists just agree on one convention?* — Different communities settled on different habits for good local reasons: particle physicists like positive energies squared with (+,-,-,-), relativists like positive spatial distances with (-,+,+,+). The course follows MTW, which matches Schutz, Gifted Amateur and most modern relativity texts, and we always say so when a sign matters.
- *Is d'Inverno's Riemann tensor different from ours?* — No. Its Riemann formula and Ricci contraction match ours; only the signature differs. That leaves R^a_{bcd} and R_ab unchanged but flips the Ricci scalar, the trace of T and the written sign of the Lambda term.
- *How do I check which convention a paper uses if it never says?* — Look for a known result: the sign of the Lambda term, the sign of R for de Sitter or dust, the sign in the Raychaudhuri equation's Ricci term, or the sphere's scalar curvature if one appears. Each pins a product of the three signs.
- *Does the sign convention change the value of physical observables like tidal accelerations?* — Never. Tidal accelerations, redshifts, orbital periods and wave strains are measured numbers. Conventions only change how the same numbers are expressed through curvature symbols.

**Pitfalls when explaining**

- Do not say 'd'Inverno has the opposite Riemann sign'; its Riemann tensor matches ours and only the signature differs.
- Do not compare signs of two formulas without first aligning slot order; many apparent disagreements are slot swaps.
- Do not present the sphere test as a complete convention check; it cannot see the signature.
- Avoid calling a Lorentzian spacetime 'positively curved' without naming the signature.

**When to show a demo**

- After naming the three switches, open the convention switchboard and flip the signature toggle: the sphere readout stays at +2/a^2 and the dust convergence rate stays at 4 pi G rho, while the dust R and the trace T change sign.
- When the learner first meets d'Inverno's Lambda equation, use the switchboard's translate button to show the extra minus sign coming from g_ab.
- During geodesic deviation, run the loop-orientation demo to show that reversing a loop reverses the rotation, while flipping a convention only changes the formula.

**Saying it aloud:** Say the Riemann definition as 'R upper rho, lower sigma mu nu, equals d-mu of Gamma rho nu sigma, minus d-nu of Gamma rho mu sigma, plus Gamma-Gamma terms'. Say the Ricci contraction as 'trace the top index against the third slot'. Name the three switches aloud as 'signature, Riemann sign, Ricci slot', and when quoting a sign add 'in our minus-plus-plus-plus convention'.

## Sources

- schutz ch06 (introduced): p.158 §6.5, p.162 §6.6
- dinverno ch06 (introduced): p.100 §6.8, p.106 §6.12
- legacy manuscript-chapter-08-curvature-holonomy (mention)
- legacy lesson-what-a-tidal-instrument-measures (mention)

## Review

**Verdict:** fixed

**Fixes**

- Working level claimed its three calibrations (sphere, R_00, R_uu) catch most errors; all three are blind to the signature. Added the statement and a genuine signature check (sign of u.u, sign of R or T for dust).
- Teaching step 5 said dust convergence calibrates the signature; R_{mu nu} u^mu u^nu is signature independent. Rewrote the step so learners find that only objects with one inverse metric (T, R) reveal the signature.
- Filled the null Schutz entry for the sign of R with a statement derived from Schutz's confirmed signature and curvature conventions, marked as not discussed in the book.
- Corrected Schutz Eq. 6.87 page from p.161 to p.162 (three refs), checked against the reading copy.
- Demo moment now states that the convergence rate stays fixed when the signature toggle flips.

**Concerns**

- Verified in reading copies: d'Inverno (13.5) G - Lambda g = 8 pi T and (13.7) (R + 2 Lambda) sqrt(-g); (10.21)-(10.23) deviation and K; (25.57)-(25.58) giving Lambda = -3K yet K > 0 labelled de Sitter; Schutz (8.7) G + Lambda g = kT; GA 11.26, 11.28, 35.38-35.41, 49.48, the ch01 driving analogy. The three-sign algebra (s1, s2, s3) was re-derived and is correct.
- Weinberg (1972) as an opposite-Riemann-sign text is general knowledge, not a cited source unit; it is correct (same signature as MTW, opposite Riemann sign, G = -8 pi G T).
- Schutz's warning footnote in §6.5 p.158 is known only from the dossier (dropped from the text export).
- The 'three-bit label' analogy cites DIV ch05 and DIV ch11 loosely; they support the conventions context rather than the analogy itself.
