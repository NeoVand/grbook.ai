---
type: "concept"
id: "einstein-tensor"
title: "Einstein tensor"
domain: "curvature"
tier: "core"
aliases: ["G_ab", "trace-reversed Ricci tensor", "Einstein tensor from sectional curvatures"]
prerequisites: ["ricci-tensor", "ricci-scalar", "contracted-bianchi-identity"]
leads_to: ["einstein-field-equations", "trace-reversed-einstein-equations", "vacuum-einstein-equations", "linearized-einstein-equations", "friedmann-equation", "hamiltonian-constraint"]
sources: ["dinverno:ch06", "dinverno:ch10", "gifted-amateur:ch00", "gifted-amateur:ch11", "gifted-amateur:ch13", "gifted-amateur:ch21", "gifted-amateur:ch36", "gifted-amateur:ch40", "legacy:lesson-contract-curvature-by-hand", "legacy:manuscript-section-12-trace-subtraction-and-reversal", "schutz:ch06", "schutz:ch08"]
review: "fixed"
---

# Einstein tensor

> The Einstein tensor is the Ricci tensor with half the scalar curvature times the metric taken away: G_μν = R_μν − ½ R g_μν. It is symmetric, has zero divergence for every metric, and is the Ricci tensor with its trace reversed, which is exactly what lets it stand opposite the conserved stress-energy tensor in Einstein's equation. For any observer, its time-time component is the sum of the curvatures of the three spatial planes around them.

## Explanations by level

### Intuition

Stand still somewhere in spacetime and look at the three flat sheets that meet where you are: the floor, and two walls at right angles. Each sheet has its own curvature, a single number saying whether nearby straight lines drawn in that sheet converge or spread. Add the three numbers. That sum is what the Einstein tensor reports along your own time direction, and Einstein's equation says it is proportional to the energy density you measure. Other entries of the tensor mix time and space planes and correspond to pressures and flows of momentum. The Einstein tensor is not all of curvature: it is a particular summary, chosen because its bookkeeping balances automatically, so it can be set equal to matter without contradiction. Around the Sun, where there is no matter, the summary is zero even though tides are real; the curvature that makes tides lives in a different part of the Riemann tensor. The simplification here is that 'the curvature of a sheet' means the curvature of a two-dimensional slice of spacetime, which includes how space is stretching in time, not just the shape of space at one instant.

**Picture to hold:** An observer at the corner of a room with three wall-planes lit up, each with a curvature dial; the three dials feed a single gauge labelled 'energy density here'.

**Assumes:** [[curvature]], [[sectional-curvature]], [[energy-density]]

### Working

Definition: G_μν = R_μν − ½ R g_μν, built from the Ricci tensor R_μν = R^ρ_μρν and the scalar R = g^μν R_μν. It is symmetric (10 components in four dimensions) and has units of inverse length squared. Three facts do most of the work. First, its divergence vanishes identically, ∇_μ G^μν = 0, by the contracted Bianchi identity; this is why G_μν + Λ g_μν = 8π T_μν (G = c = 1) is consistent with conservation of T, whereas R_μν = κ T_μν would force the trace of T to be constant everywhere. Second, it is the trace reverse of Ricci: its trace is g^μν G_μν = −R in four dimensions, and the map is its own inverse, R_μν = G_μν − ½ G g_μν with G = g^μν G_μν. Hence G_μν = 0 exactly when R_μν = 0, so vacuum means Ricci-flat, not flat. Third, in an orthonormal frame each diagonal component is a sum of plane curvatures: G_t̂t̂ = R^{x̂ŷ}_{x̂ŷ} + R^{ŷẑ}_{ŷẑ} + R^{ẑx̂}_{ẑx̂}, the sum of sectional curvatures of the three planes orthogonal to the observer, and G^x̂_x̂ = −(sum over the three planes not containing x̂). Off-diagonal components add Riemann components sharing one index, for example G^t̂_x̂ = R^{t̂ŷ}_{x̂ŷ} + R^{t̂ẑ}_{x̂ẑ}. Quick calibrations: a 2-sphere of any radius has G = 0; a flat expanding universe has G_t̂t̂ = 3H² (Friedmann's equation 3H² = 8πρ) and G_îî = −2ä/a − H²; a static star with g_rr = (1 − 2m(r)/r)⁻¹ has G_t̂t̂ = 2m′/r², so 8πρ = 2m′/r² gives m′ = 4πr²ρ; in the weak field −(1 + 2Φ)dt² + (1 − 2Ψ)dx², G_t̂t̂ ≈ 2∇²Ψ, which with G_t̂t̂ = 8πρ is Poisson's equation.

**Picture to hold:** A six-tile board of plane curvatures in the observer's frame (three time-space planes, three space-space planes); choosing a component of G lights up the tiles it sums, with signs.

**Assumes:** [[ricci-tensor]], [[ricci-scalar]], [[contracted-bianchi-identity]], [[orthonormal-frame]], [[metric-tensor]]

### Formal

On a pseudo-Riemannian manifold (M, g) of dimension n with Levi-Civita connection, the Einstein tensor is the symmetric (0,2) field G = Ric − ½ R g, with course conventions R_μν = R^ρ_μρν and R = g^μν R_μν (sphere R = +2/a²). Properties: (i) div G = 0 identically, by the twice-contracted second Bianchi identity; (ii) tr G = (1 − n/2) R, so for n ≠ 2, Ric = G − (1/(n − 2)) (tr G) g and G = 0 ⇔ Ric = 0; for n = 2, Ric = ½ R g and G ≡ 0 for every metric; for n = 3, G determines Ric and hence the full Riemann tensor, since the Weyl tensor vanishes; for n = 4, G carries the 10 Ricci components and none of the 10 Weyl components. (iii) For any unit timelike u, G(u,u) is the sum of the sectional curvatures of any three mutually orthogonal spacelike planes in u^⊥; by the Gauss equation this equals ½(³R + K² − K_ij K^ij) for the hypersurface orthogonal to u, so G(n,n) = 8πρ is the Hamiltonian constraint. (iv) Variational origin: δ∫√−g R d⁴x = ∫√−g G_μν δg^μν d⁴x plus a boundary term, so G is (up to sign and density weight) the Euler-Lagrange tensor of the Einstein-Hilbert action; diffeomorphism invariance then gives (i) independently. (v) Uniqueness (Lovelock): in four dimensions the only symmetric, identically divergence-free (0,2) tensors built locally from g and its first two derivatives are a G + b g. (vi) Linearization about Minkowski with h̄_μν = h_μν − ½η_μν h: in Lorenz gauge ∂^μ h̄_μν = 0, G_μν = −½ □h̄_μν. (vii) Maximally symmetric 4-space with R_μνρσ = K(g_μρ g_νσ − g_μσ g_νρ): Ric = 3K g, R = 12K, G = −3K g, a vacuum with Λ = 3K. Convention notes: G_μν and G^μν are invariant under g → −g with the same Riemann definition, but R and G^μ_ν change sign; the combination G_μν + Λ g_μν in signature (−,+,+,+) corresponds to G_ab − Λ g_ab in (+,−,−,−). The field equation assigning G to matter belongs to the einstein-field-equations note; here G is a purely geometric object.

**Picture to hold:** The Ricci part of curvature projected into a form whose flux through every closed infinitesimal 3-surface vanishes; the Weyl part is invisible to it.

**Assumes:** [[levi-civita-connection]], [[sectional-curvature]], [[gauss-codazzi-equations]], [[einstein-hilbert-action]], [[lovelock-theorem]], [[weyl-tensor]], [[trace-reversed-metric-perturbation]]

## Prerequisites

- [[ricci-tensor]] — The Einstein tensor is built from Ricci, and its sign and index conventions pass straight through.
- [[ricci-scalar]] — The trace term subtracted from Ricci is the scalar curvature times the metric.
- [[contracted-bianchi-identity]] — The defining property that makes this combination special, zero divergence for every metric, is the contracted identity.

## Leads to

- [[einstein-field-equations]] — The Einstein tensor is the geometric side of G_μν + Λg_μν = 8πT_μν.
- [[trace-reversed-einstein-equations]] — Undoing the trace reversal rewrites the field equations as Ricci equals a trace-adjusted source.
- [[vacuum-einstein-equations]] — Because G = 0 exactly when Ricci = 0, the vacuum equations become Ricci-flatness.
- [[linearized-einstein-equations]] — To first order in Lorenz gauge the Einstein tensor is a wave operator on the trace-reversed perturbation.
- [[friedmann-equation]] — The time-time Einstein component of the expanding universe, 3H² plus curvature, is the left side of Friedmann's equation.
- [[hamiltonian-constraint]] — The normal-normal component of G contains no second time derivatives and gives the energy constraint on initial data.

## Related

- [[ricci-tensor-field-equation]] — The rejected alternative that the Einstein tensor replaces; comparing the two explains the half-trace term.
- [[sectional-curvature]] — Diagonal Einstein components in an orthonormal frame are sums of sectional curvatures.
- [[weyl-tensor]] — The part of curvature the Einstein tensor cannot see; it carries tides and waves in vacuum.
- [[lovelock-theorem]] — States that in four dimensions a G + b g is the only local divergence-free option, making the choice essentially unique.
- [[cosmological-constant]] — Λ g_μν is the other divergence-free term that can accompany G.
- [[variation-of-the-einstein-hilbert-action]] — Varying √−g R with respect to the metric produces the Einstein tensor directly.
- [[einstein-space]] — Spaces with Ricci proportional to the metric have Einstein tensor proportional to the metric, the vacuum-with-Λ case.
- [[ricci-flat-spacetime]] — Zero Einstein tensor is the same as zero Ricci tensor in four dimensions.

## Key equations

### Definition

$$
G_{\mu\nu} = R_{\mu\nu} - \tfrac12 R\, g_{\mu\nu} = G_{\nu\mu}
$$

Ricci minus half its trace times the metric; symmetric, ten components in four dimensions, units of inverse length squared. *(SCH ch06 (6.98) §6.6 p.163; GA ch13 (13.30) §13.3 p.146; GA ch13 (13.52) p.150; DIV ch06 (6.86) §6.12 p.106)*

**Convention:** Course Ricci R_μν = R^ρ_μρν and sphere R = +2/a². Schutz and Gifted Amateur also write the upper-index form; d'Inverno uses Latin G_ab.

### Identically zero divergence

$$
\nabla_\mu G^{\mu\nu} = 0
$$

Holds for every metric; four identities among the ten components, and the reason G can equal a conserved source. *(SCH ch06 (6.99) §6.6 p.163; GA ch13 (13.33) §13.3 p.146; DIV ch06 (6.87) §6.12 p.106; DIV ch10 §10.8 p.184)*

### Trace and trace reversal

$$
g^{\mu\nu}G_{\mu\nu} = \left(1 - \tfrac{n}{2}\right) R \;\overset{n=4}{=}\; -R, \qquad R_{\mu\nu} = G_{\mu\nu} - \tfrac{1}{n-2}\, G\, g_{\mu\nu} \;\overset{n=4}{=}\; G_{\mu\nu} - \tfrac12 G\, g_{\mu\nu}
$$

In four dimensions the Einstein tensor is Ricci with its trace sign flipped, and flipping again gives Ricci back; hence G = 0 if and only if Ricci = 0 (n ≠ 2). *(GA ch13 Ex 13.3; DIV ch06 Ex 6.26; legacy:manuscript-section-12-trace-subtraction-and-reversal)*

**Convention:** G without indices here is the trace g^μν G_μν, not Newton's constant. The ½ in the definition of G is the same in every dimension; the coefficient in the inverse relation is 1/(n − 2).

### Einstein components from plane curvatures (orthonormal frame)

$$
G_{\hat 0\hat 0} = R^{\hat1\hat2}{}_{\hat1\hat2} + R^{\hat2\hat3}{}_{\hat2\hat3} + R^{\hat3\hat1}{}_{\hat3\hat1}, \quad G^{\hat1}{}_{\hat1} = -\left(R^{\hat0\hat2}{}_{\hat0\hat2} + R^{\hat0\hat3}{}_{\hat0\hat3} + R^{\hat2\hat3}{}_{\hat2\hat3}\right), \quad G^{\hat0}{}_{\hat1} = R^{\hat0\hat2}{}_{\hat1\hat2} + R^{\hat0\hat3}{}_{\hat1\hat3}
$$

Each diagonal component is minus the sum of plane curvatures over the three planes that exclude its direction; for the time direction the sign flips on lowering, so G_0̂0̂ is the sum of sectional curvatures of the observer's three spatial planes. *(GA ch21 §21.2 p.231; GA ch36 §36.4 p.384; GA ch21 Ex 21.3)*

**Convention:** Gifted Amateur states the mixed forms G^0_0 and G^1_1 in a margin note; with η_00 = −1, G_0̂0̂ = −G^0̂_0̂. Other components follow by permuting indices.

### Calibration: flat FLRW and a static star

$$
G_{\hat t\hat t} = 3\left(\frac{\dot a}{a}\right)^2,\quad G_{\hat i\hat i} = -2\frac{\ddot a}{a} - \left(\frac{\dot a}{a}\right)^2; \qquad g_{rr} = \left(1 - \frac{2m(r)}{r}\right)^{-1} \Rightarrow G_{\hat t\hat t} = \frac{2m'(r)}{r^2}
$$

Left sides of the Friedmann equations and of the mass equation of stellar structure; with G_t̂t̂ = 8πρ they give 3H² = 8πρ and m′ = 4πr²ρ. *(GA ch36 Example 36.5 §36.4 p.382; GA ch36 (36.81) §36.4 p.383; SCH ch10 (10.14) §10.2 p.271; legacy:manuscript-section-24-3-calculation-checklist)*

**Convention:** Gifted Amateur's Eq. 36.81 is printed with typos (ä where ȧ belongs); the forms here follow from direct substitution. Schutz writes the static coordinate component G_00 = e^{2Φ} r⁻² d/dr[r(1 − e^{−2Λ})] with Λ(r) a metric function; with e^{−2Λ} = 1 − 2m/r this equals e^{2Φ} times 2m′/r².

### Linearized Einstein tensor in Lorenz gauge

$$
G_{\mu\nu} = -\tfrac12 \Box \bar h_{\mu\nu}, \qquad \bar h_{\mu\nu} = h_{\mu\nu} - \tfrac12\eta_{\mu\nu} h,\quad \partial^\mu \bar h_{\mu\nu} = 0
$$

For weak fields the Einstein tensor is a wave operator acting on the trace-reversed perturbation, the starting point for gravitational waves. *(SCH ch08 (8.41) §8.3 p.192; SCH ch08 Ex 8.8; GA ch45 (45.14) §45.2 p.488)*

**Convention:** □ = −∂_t² + ∇². With G_μν = 8πT_μν this gives □h̄_μν = −16πT_μν, as in the course conventions.

### Metric variation of the Einstein-Hilbert Lagrangian

$$
\delta\left(\sqrt{-g}\,R\right) = \sqrt{-g}\,G_{\mu\nu}\,\delta g^{\mu\nu} + \sqrt{-g}\,\nabla_\sigma v^\sigma
$$

Up to a total divergence, varying √−g R produces the Einstein tensor, so it is the natural geometric Euler-Lagrange tensor. *(GA ch40 (40.50) §40.4 p.436; DIV ch11 (11.34) §11.5 p.193)*

**Convention:** Varying with respect to g_μν instead gives −√−g G^μν δg_μν, the sign seen in d'Inverno (11.27) and Gifted Amateur (40.50).

## Conventions across the books

| Issue | Schutz | Gifted Amateur | d'Inverno | Course choice |
| --- | --- | --- | --- | --- |
| Index placement and alphabet in the definition | Upper indices: G^αβ ≡ R^αβ − ½ g^αβ R (Eq. 6.98), Greek indices. | Upper G^μν in the derivation (Eq. 13.30), lower G_μν in the field equation and summary; bold G for the index-free tensor. | Lower G_ab = R_ab − ½ g_ab R (Eq. 6.86) with Latin indices; mixed G_a^b in the divergence identity and in the constraint analysis. | G_μν = R_μν − ½ R g_μν with Greek indices; always show indices to avoid confusion with Newton's constant. |
| Metric signature and the sign of R and mixed components | (−,+,+,+), MTW Riemann and Ricci. | (−,+,+,+), MTW-style Riemann and Ricci (Riemann-tensor contraction on first and third slots). | (+,−,−,−) with MTW Riemann and Ricci index conventions: R and mixed G^a_b have the opposite sign to the course, while G_ab, G^ab and the energy-density component G_00 = 8πρ agree. | (−,+,+,+). When translating from d'Inverno flip R and any mixed component; lower-index and upper-index G need no change. |
| The letter G | G for the Einstein tensor with G = 1 units, so Newton's constant is rarely visible (G^αβ = 8πT^αβ). | Bold G for the Einstein tensor, plain G for Newton's constant (G = 8πG T appears), and G(x, x′) for a Green's function in the same chapter; in Chapter 35 the symbol G is also used for R_μν − ¼ R g_μν. | G_ab for the Einstein tensor; Newton's constant appears inside κ = 8πG/c⁴. | Einstein tensor always written with indices, G_μν; Newton's constant named in words and shown only when restoring SI units; the trace-free Ricci tensor gets its own symbol, never G. |
| What 'trace-reversed' means | Uses 'trace reverse' for h̄_αβ and shows the linearized Einstein tensor is the trace reverse of linearized Ricci (Exercise 8.8). | Calls G the trace-reversed Ricci tensor in Chapter 13 (correct), but in Chapter 35 attaches the same name to R_μν − ¼ R g_μν, which is the trace-free Ricci tensor. | Does not use the name for G; writes the trace-reversed perturbation as φ_ab = h_ab − ½η_ab h. | In four dimensions 'trace-reversed' means subtracting half the trace times the metric (trace becomes minus the original); 'trace-free' means subtracting a quarter. The Einstein tensor is trace-reversed Ricci. |
| Sign and side of the cosmological term | G^αβ + Λg^αβ = 8πT^αβ. | R_μν − ½g_μν R = 8πG T_μν − Λg_μν. | G_ab − Λg_ab = 8πT_ab in signature (+,−,−,−); the same physics as the course form. | G_μν + Λg_μν = 8πG T_μν/c⁴ (8πT_μν with G = c = 1); positive Λ is repulsive. |
| Which components are quoted for exact solutions | Coordinate components such as G_00, G_rr, G_θθ for the static metric (Chapter 10), carrying factors e^{2Φ}, e^{2Λ}, r². | Orthonormal static-observer (hatted) components, often mixed, G^t̂_t̂ = −G_t̂t̂, assembled from plane curvatures. | Mixed coordinate components G^a_b (for example the spherically symmetric G^2_2 in Chapter 15). | Say which basis is used; prefer the orthonormal frame of the relevant observer for physical reading (G_t̂t̂ = 8πρ) and convert explicitly. |
| Sign of K for a constant-curvature spacetime | Not used for the Einstein tensor in the cited chapters. | Signature (−,+,+,+); de Sitter treated through Ricci = (R/4) g, giving Λ = R/4 with R > 0 (Exercise 15.3), the same as the course. | Writes R_abcd = K(g_ac g_bd − g_ad g_bc) in signature (+,−,−,−). Flipping the metric flips the lowered Riemann tensor but not the bracket, so his K is minus the course K; with G_ab − Λg_ab = 0 he gets Λ = −3K. | R_μνρσ = K(g_μρ g_νσ − g_μσ g_νρ) with K > 0 for de Sitter, G_μν = −3K g_μν and Λ = 3K. Translate d'Inverno's K by a sign change. |

## How the sources teach it

### schutz

**Route:** Chapter 6 lets the Einstein tensor fall out of the twice-contracted Bianchi identity as 'the' divergence-free curvature tensor and previews G = 8πT with automatic conservation. Chapter 8 argues for it: the field equation needs a symmetric second-order operator on the metric; the family Ricci + μ g R + Λ g is natural; conservation for every metric forces μ = −½; the four identities then explain why only six equations are independent. Later sections linearize it in terms of h̄ and quote exact-solution components.

**Representation:** Components and prose logic; no picture of what G measures.

**Strengths:** The consistency argument makes the form feel forced; clear link to counting of equations and to linearized theory.

**Weaknesses:** No geometric interpretation of any component; linearized and exact-solution components (Chapters 8 and 10) are stated or left to exercises, so learners cannot check them. *(SCH ch06 §6.6 p.163; SCH ch08 §8.1 p.184; SCH ch08 §8.2 p.187; SCH ch08 §8.3 p.191; SCH ch10 §10.2 p.271)*

### gifted-amateur

**Route:** Named early with a warning not to confuse it with Newton's constant. Chapter 13 builds it inside the refutation of the Ricci guess (define, take divergence, use the contracted identity, show the guess forces a uniform universe) and then adopts G = κT, fixing κ from the Newtonian limit in Example 13.4. Chapter 21 offers the orthonormal shortcut expressing Einstein components as sums of plane curvatures, reused in Chapter 36 with Cartan's method for the static star and the expanding universe. Chapter 40 obtains it again as the metric variation of the Einstein-Hilbert action.

**Representation:** Motivation by a failed guess, a geometry-versus-physics route map (Fig. 13.1), component shortcuts from curvature 2-forms, and a variational derivation.

**Strengths:** Three complementary routes (conservation, frame shortcut, action); the plane-sum rules give fast calculation and a geometric meaning; the Newtonian calibration is worked in full.

**Weaknesses:** Symbol overload for G; Chapter 35 misnames R_μν − ¼Rg_μν as trace-reversed; Eq. 36.81 is printed with typos; a sign inconsistency between Eqs. 40.50 and 40.53; the reading copy of the Chapter 11 margin note shows a coefficient of 1/3 (the correct value is ½). *(GA ch00 §0.6 p.10; GA ch11 §11.5 p.127; GA ch13 §13.3 p.146; GA ch13 Fig. 13.1 p.141; GA ch13 Example 13.4 §13.4 p.147; GA ch21 §21.2 p.231; GA ch36 §36.4 p.383; GA ch40 Example 40.10 §40.4 p.436)*

### dinverno

**Route:** Chapter 6 defines G_ab from Ricci and the curvature scalar with no physical motivation, states the contracted identities, and sets G = 0 ⇔ Ricci = 0 as an exercise. Chapter 10 recalls it as the natural left side once matter is included, because its divergence vanishes like that of T_ab. Chapter 11 derives it as minus the densitized Euler-Lagrange tensor of the Einstein Lagrangian, first by brute force and then by the efficient indirect variation. Later chapters use its projections as constraints and its mixed components in exact solutions.

**Representation:** Axiomatic definitions, identity signs, variational calculus.

**Strengths:** Clean definitions and a careful variational derivation; the exercise on G = 0 ⇔ Ricci = 0 is exactly the right check.

**Weaknesses:** No interpretation of G's components in Chapter 6; Chapter 10 suggests proportionality to T without mentioning Λ until Chapter 13 and never names Lovelock's uniqueness result. *(DIV ch06 §6.12 p.106; DIV ch06 Ex 6.26; DIV ch10 §10.8 p.184; DIV ch11 §11.4 p.191; DIV ch11 §11.5 p.193)*

### legacy

**Route:** Chapter 9 reaches G from the normal-coordinate Bianchi proof and adds dimension facts (G vanishes in 2D) and the warning that divergence-free is not constant. Chapter 12 opens with a symbol table for the field equation, derives the half-trace by demanding a divergence-free combination while stating that this does not prove uniqueness, performs trace reversal including the d-dimensional coefficient, and calibrates κ with both potentials (G_00 = 2∇²Ψ). Chapters 17, 19 and 24 use G components as the working layer for Schwarzschild, Friedmann and a metric-interpretation checklist; a six-entry curvature table lesson shows Ricci (and so G) vanishing while curvature does not.

**Representation:** Tables, derivations with explicit 'derived versus chosen' labels, numerically checked calibration geometries.

**Strengths:** Honest about uniqueness, careful about the dimension dependence of trace reversal, and verified by an independent curvature checker.

**Weaknesses:** The pieces are spread over several chapters; the plane-sum reading of G is absent; the anatomy poster figure is static. *(legacy:manuscript-section-09-bianchi-einstein-tensor; legacy:manuscript-section-12-trace-subtraction-and-reversal; legacy:manuscript-chapter-12-einstein-field-equation; legacy:lesson-contract-curvature-by-hand; legacy:manuscript-section-24-3-calculation-checklist)*

## Recommended teaching path

1. **1. What must sit opposite matter?** — List the requirements for the geometric side of a field equation: a symmetric two-index tensor, built from the metric and at most its second derivatives, reducing to something like the Laplacian of the potential, and divergence-free for every metric because T is conserved. Ask which curvature object the learner would try first. *Why:* Turns the Einstein tensor into the answer to a design problem the learner has already posed. *(SCH ch08 §8.1 p.184; GA ch13 Fig. 13.1 p.141)*
2. **2. Ricci fails, the half-trace fixes it** — Try Ricci = κT, take the divergence, use the contracted identity, and expose the constant-trace contradiction; then show that subtracting half the scalar curvature times the metric removes the problem. *Why:* The learner sees why the extra term is necessary rather than memorizing it. *(GA ch13 §13.3 p.146; legacy:manuscript-section-12-trace-subtraction-and-reversal)*
3. **3. Trace reversal and what G forgets** — Compute the trace (−R in 4D), invert the relation, and conclude G = 0 exactly when Ricci = 0. Then use the six-plane board with the Schwarzschild pattern to show nonzero curvature with zero G. *Why:* Prevents 'G = 0 means flat' and sets up the vacuum equations and the Weyl tensor. *(GA ch13 Ex 13.3; DIV ch06 Ex 6.26; legacy:lesson-contract-curvature-by-hand)*
4. **4. The picture: an observer's three planes** — In an orthonormal frame, show that the time-time component is the sum of the curvatures of the three spatial planes, and that other diagonal components exclude their own direction. Let the learner light up tiles on the board for each component. *Why:* Gives every component a geometric meaning and a fast calculation route. *(GA ch21 §21.2 p.231; GA ch21 Ex 21.3)*
5. **5. Calibrate on known geometries** — Check a 2-sphere (G = 0), a flat expanding universe (G_t̂t̂ = 3H² although space is flat), a static star (G_t̂t̂ = 2m′/r²) and a constant-curvature spacetime (G = −3Kg). *Why:* Concrete numbers catch sign and convention errors and preview Friedmann, stellar structure and de Sitter. *(GA ch36 Example 36.5 §36.4 p.382; SCH ch10 §10.2 p.271; DIV ch25 §25.9 p.527; legacy:manuscript-section-24-3-calculation-checklist)*
6. **6. Application: fix the coupling from Newton** — In the weak, slow limit only G_t̂t̂ survives at leading order; with G_t̂t̂ ≈ 2∇²Ψ, the spatial equations setting Ψ = Φ for non-relativistic matter, and Poisson's equation, the coupling must be 8π (8πG/c⁴ in SI). *Why:* Connects the abstract tensor to a law the learner knows and hands off to the field equations. *(GA ch13 Example 13.4 §13.4 p.147; legacy:manuscript-chapter-12-einstein-field-equation)*
7. **7. Deeper reasons (advanced)** — Show that varying √−g R yields the Einstein tensor, and state Lovelock's theorem that a G + b g is the only local divergence-free option in four dimensions. *Why:* Replaces 'a clever combination' with 'the unique natural object', and explains why Λ is the only freedom. *(GA ch40 Example 40.10 §40.4 p.436; DIV ch11 §11.5 p.193; legacy:manuscript-section-12-trace-subtraction-and-reversal)*

## Analogies

- **An observer's room: add the curvatures of floor and walls** (intuition): The time-time Einstein component seen by an observer is the sum of the curvatures of three mutually perpendicular spatial planes through their position, like reading three dials on a room's floor and two walls and adding them. *Limits:* The 'planes' are two-dimensional slices of spacetime, so their curvature includes how the slice is bending in time (extrinsic curvature), not just the intrinsic shape of space; a flat expanding universe has flat space yet nonzero G_t̂t̂. *(GA ch21 §21.2 p.231)*
- **A balanced ledger for geometry** (intuition): Of all the ways to summarise curvature with a two-index table, this one keeps its books balanced at every point for any geometry, just as matter's energy-momentum books balance; only balanced ledgers can be equated. *Limits:* Balance is local and says nothing about global energy; Λ times the metric is another balanced ledger, so balance alone does not single out G. *(SCH ch08 §8.1 p.184; legacy:manuscript-section-12-trace-subtraction-and-reversal)*
- **Two parallel production lines meeting at an equals sign** (working): Geometry runs metric → curvature → Einstein tensor; physics runs fields → energy → stress-energy tensor. Each line must deliver a symmetric, divergence-free product before the two can be joined. *Limits:* The lines are not independent in practice: matter moves on the geometry it creates, so the equation is solved together, not assembled from separate parts. *(GA ch13 Fig. 13.1 p.141)*
- **A shadow that captures the Ricci part and misses the Weyl part** (working): Contracting Riemann to Ricci and then trace-reversing is like casting a shadow of a 3D object onto a wall: some features survive, others vanish. The Einstein tensor keeps the ten Ricci components and loses the ten Weyl components that carry tides and gravitational waves in empty space. *Limits:* Unlike a shadow, nothing is lost that matter could have supplied: the Weyl part is not locally tied to matter at all, and it is constrained through the Bianchi identity rather than simply discarded. *(legacy:manuscript-chapter-09-ricci-weyl-einstein; legacy:manuscript-section-10-curvature-invariants-and-summary-table)*

## Misconceptions

- **Because T_μν has two indices, the Ricci tensor, which also has two, should simply be set proportional to it.** — Matching the number of indices is necessary but not sufficient; the geometric side must also be divergence-free for every metric. Ricci is not, and Ricci = κT would force the scalar curvature and so the trace of T to be constant throughout spacetime, contradicting any lump of matter. The Einstein tensor meets the requirement. *Why tempting:* Ricci is the simplest curvature object of the right shape, and Einstein himself proposed it in 1915. *Diagnostic:* If Ricci = κT held, what would the contracted Bianchi identity plus ∇_μ T^μν = 0 imply about the trace of T inside a star and in the vacuum around it? *(GA ch13 §13.3 p.145; GA ch13 §13.3 p.147)*
- **Where the Einstein tensor vanishes, spacetime is flat: no matter means no curvature.** — G = 0 is the same as Ricci = 0, which leaves the ten Weyl components free. Outside the Sun G = 0, but tides, light bending and gravitational waves are all Weyl curvature. Flatness requires the full Riemann tensor to vanish. *Why tempting:* The vacuum field equation is often summarised as 'curvature is zero where there is no matter'. *Diagnostic:* Two astronauts float freely near Earth in empty space, one above the other. Does their separation change? What does that say about whether spacetime there is flat, given G = 0? *(DIV ch22 §22.4 p.456; legacy:lesson-contract-curvature-by-hand; legacy:manuscript-chapter-09-ricci-weyl-einstein)*
- **Subtracting a quarter of the scalar curvature times the metric gives the trace-reversed Ricci tensor (the Einstein tensor).** — In four dimensions subtracting ¼ R g gives the trace-free Ricci tensor (trace zero). Trace reversal subtracts ½ R g, making the trace −R. The two agree only when contracted with null vectors, where the metric term drops out. *Why tempting:* One textbook example uses the name 'trace-reversed' and the letter G for the quarter version, and both operations 'do something to the trace'. *Diagnostic:* Compute the trace of R_μν − ¼ R g_μν and of R_μν − ½ R g_μν in four dimensions. Which one deserves the name trace-reversed? *(GA ch35 §35.4 p.370; GA ch13 Ex 13.3)*
- **The G in G = 8πT is Newton's gravitational constant.** — In geometrized form the bold or indexed G is the Einstein tensor, a curvature field with units of inverse length squared; Newton's constant has been set to 1. Restored to SI the equation is G_μν = (8πG/c⁴)T_μν, containing both. *Why tempting:* Identical letters, often in the same equation. *Diagnostic:* What are the units of each side of G_μν = 8πT_μν in geometrized units, and where does Newton's constant reappear when you restore SI units? *(GA ch00 §0.6 p.10; GA ch13 §13.3 p.146)*
- **The ½ in trace reversal works in every dimension, so R_μν = G_μν − ½ G g_μν always.** — The ½ in the definition G = Ric − ½Rg is the same in every dimension (it is what makes the divergence vanish), but inverting it gives Ric = G − (1/(n − 2))(tr G) g. The coefficients coincide only in four dimensions; in two dimensions G vanishes identically and cannot be inverted. *Why tempting:* In four dimensions both coefficients are ½, which hides the dimension dependence. *Diagnostic:* In three dimensions, what is the trace of the Einstein tensor in terms of R, and what coefficient recovers Ricci from G? *(legacy:manuscript-section-12-trace-subtraction-and-reversal; SCH ch13 (13.10) §13.2 p.425)*
- **The time-time Einstein component measures only the curvature of space at one instant, so a universe with flat spatial slices has G_t̂t̂ = 0.** — The sum of plane curvatures uses the spacetime Riemann tensor restricted to spatial planes, which by the Gauss equation includes extrinsic-curvature terms from how the slice is embedded. A flat expanding universe has flat slices yet G_t̂t̂ = 3H², which is Friedmann's equation. *Why tempting:* The plane-sum rule names only spatial planes, and 'spatially flat' sounds like 'no curvature there'. *Diagnostic:* The flat FLRW universe has Euclidean spatial slices. Using G_t̂t̂ = 8πρ, can it contain matter? Where does the nonzero curvature come from? *(GA ch36 Example 36.5 §36.4 p.382; legacy:manuscript-section-19-1-friedmann-derivation)*
- **Zero scalar curvature R means the Einstein tensor vanishes.** — If R = 0 then G_μν = R_μν, which can be nonzero. Radiation and electromagnetic fields have traceless stress-energy, so R = 0 there while G_μν = 8πT_μν ≠ 0. *Why tempting:* 'Zero curvature scalar' sounds like 'no curvature', and the trace term is the only difference between G and Ricci. *Diagnostic:* A region filled with pure electromagnetic radiation has T^μ_μ = 0. What are R and G_μν there? *(legacy:manuscript-section-12-trace-subtraction-and-reversal)*

## Thought experiments

- **Counting planes from a static observer**: A static observer inside a star reads off the curvature of the three spatial planes around them (radial-angular, radial-angular, and angular-angular) and adds them; a second observer does the same just outside the surface. *Lesson:* Inside, the sum equals 2m′/r², proportional to the local density; outside it is zero even though individual plane curvatures are not, because the radial-angular and angular-angular contributions cancel. The Einstein tensor measures local matter, not the presence of curvature. *(GA ch21 Example 21.1 §21.2 p.231; GA ch36 Example 36.6 §36.4 p.383)*

## Visualizations

### Six-plane curvature board · interactive-2d · high priority

Six tiles hold the plane curvatures of an orthonormal frame at one event: three time-space planes and three space-space planes. Live readouts show the Ricci components, R, all diagonal Einstein components (with their contributing tiles highlighted and signed), and the Kretschmann scalar.

**Interaction:** Drag tile values or load presets: Schwarzschild pattern (G = 0 with nonzero Kretschmann), flat FLRW dust (space-space tiles H², time-space tiles −ä/a), de Sitter (all planes equal magnitude), a static-star interior. Click an Einstein component to highlight the planes it sums; a 'find a vacuum' challenge asks for nonzero tiles giving G = 0.

**Model:** Algebraic curvature tensor at a point with only plane-type components, lowered entries (A,B,C) = R_0̂î0̂î and (D,E,F) = R_1̂2̂1̂2̂, R_1̂3̂1̂3̂, R_2̂3̂2̂3̂. Then R_0̂0̂ = A+B+C, R_1̂1̂ = −A+D+E, R_2̂2̂ = −B+D+F, R_3̂3̂ = −C+E+F, G_0̂0̂ = D+E+F, G_1̂1̂ = B+C−F, and Kretschmann = 4(A²+B²+C²+D²+E²+F²). Schwarzschild preset q(−2,1,1,−1,−1,2) with q = M/r³.

**Inspired by:** GA ch21 §21.2 p.231; GA ch21 Ex 21.3

**Legacy assets:** lesson-contract-curvature-by-hand

### Build a star, read its Einstein tensor · interactive-plot · medium priority

The learner sketches a density profile ρ(r). The app integrates m(r), plots G_t̂t̂ = 2m′/r² on top of 8πρ, and shows that outside the surface G vanishes while the radial tidal curvature −2m/r³ does not.

**Interaction:** Draw or drag control points of ρ(r); toggle between orthonormal and coordinate components (with the e^{2Φ} factor shown); a probe observer walks outward displaying the three plane curvatures and their sum.

**Model:** Static spherical metric with g_rr = (1 − 2m/r)⁻¹, m′ = 4πr²ρ; orthonormal plane curvatures for the spatial part; exterior Schwarzschild.

**Inspired by:** SCH ch10 (10.14) §10.2 p.271; GA ch21 Example 21.1 §21.2 p.231; GA ch36 Example 36.6 §36.4 p.383

**Legacy assets:** manuscript-section-17-1-schwarzschild-derivation, engine-independent-curvature-checker

### Trace-reversal calculator · interactive-2d · medium priority

Choose a source (dust, radiation, a perfect fluid with pressure slider, vacuum energy, an electromagnetic field). The app shows T_μν, its trace, the Einstein tensor it demands, the trace-reversed source that fixes Ricci, and R, flagging cases like R = 0 with G ≠ 0.

**Interaction:** Pick the source and the observer's frame; toggle dimension n = 3, 4, 5 to see the ½ in G stay fixed while the inversion coefficient changes; a Ricci-guess toggle shows which sources would violate the constant-trace condition.

**Model:** G_μν + Λg_μν = 8πT_μν, R = −8πT (Λ = 0, n = 4), R_μν = 8π(T_μν − ½T g_μν); general n with coefficient 1/(n − 2).

**Inspired by:** GA ch13 §13.3 p.146

**Legacy assets:** manuscript-chapter-12-einstein-field-equation, manuscript-section-12-trace-subtraction-and-reversal

### Geometry and matter route map · interactive-2d · low priority

Two columns unfold on click: metric → connection → Riemann → Ricci and R → Einstein tensor, and fields → energy → stress-energy tensor. The equals sign between them locks only when both sides pass a divergence check.

**Interaction:** Click nodes to reveal the defining equation and a one-line meaning; swap the Einstein tensor for Ricci and watch the lock fail with an explanation; add Λg and watch it stay locked.

**Inspired by:** GA ch13 Fig. 13.1 p.141

## Worked examples

- **Divergence of the Einstein tensor and refutation of the Ricci guess** (working): The half-trace term is exactly what cancels the gradient of R left over by the contracted identity; without it matter would have to be uniform. *(GA ch13 §13.3 p.146)*
- **Fixing the coupling constant from Newtonian gravity** (working): In the weak-field, slow-motion limit only the time-time component survives; for a pressureless source G^00 = 2R_00 once the field equation holds, and R_00 = ∇²Φ then reproduces Poisson's equation with coupling 8πG/c⁴. *(GA ch13 Example 13.4 §13.4 p.147; legacy:manuscript-chapter-12-einstein-field-equation)*
- **Einstein components of the static spherical metric from plane curvatures** (working): Four curvature functions determine all components, each Einstein component being a sum over the planes that exclude its direction. *(GA ch21 Example 21.1 §21.2 p.231; GA ch36 Example 36.6 §36.4 p.383)*
- **Curvature and Einstein tensor of the flat expanding universe** (working): Flat spatial slices still give G_t̂t̂ = 3H² and G_îî = −2ä/a − H², the left sides of the Friedmann equations (the printed forms contain typos; use the corrected ones). *(GA ch36 Example 36.5 §36.4 p.382; legacy:manuscript-section-19-1-friedmann-derivation)*
- **Einstein tensor of a constant-curvature spacetime** (working): Contracting the maximally symmetric Riemann tensor gives Ricci = 3Kg, R = 12K and G = −3Kg, so such spacetimes are vacua with a cosmological constant. *(DIV ch25 §25.9 p.527)*
- **The Einstein tensor from varying the Einstein-Hilbert action** (formal): Only the variations of the volume element and of the inverse metric survive; the curvature variation is a boundary term, and the survivors assemble into the Einstein tensor. *(GA ch40 Example 40.10 §40.4 p.436; DIV ch11 §11.5 p.193)*
- **Solving the spherical vacuum equations with mixed Einstein components** (working): The time-time component integrates to the 1 − C/r form, a combination of time-time and radial components fixes the lapse, and the Newtonian limit sets C = 2GM/c². *(legacy:manuscript-section-17-1-schwarzschild-derivation)*

## Exercises

- (intro) Check that contracting the Einstein tensor with the metric gives minus the Ricci scalar. *Skill:* tracing with the metric *(GA ch13 Ex 13.3)*
- (intro) Show that the Einstein tensor vanishes if and only if the Ricci tensor vanishes. *Skill:* trace reversal *(DIV ch06 Ex 6.26)*
- (standard) Prove the orthonormal-frame rules expressing Einstein components as sums of plane-type Riemann components. *Skill:* Riemann symmetries and contraction *(GA ch21 Ex 21.3)*
- (standard) Derive the linearized Einstein tensor as the trace reverse of the linearized Ricci tensor and reduce it using the trace-reversed perturbation. *Skill:* linearized curvature *(SCH ch08 Ex 8.8)*
- (challenging) Show from the linearized Einstein tensor that the time-time and time-space components contain no second time derivatives, and reconcile this with the gauge-fixed wave equations. *Skill:* constraints versus evolution equations *(SCH ch08 Ex 8.9)*
- (intro) Treat de Sitter space as having Ricci proportional to the metric, find its Einstein tensor and the implied cosmological constant, and check against the scale-factor form of R. *Skill:* Einstein tensor of symmetric spacetimes *(GA ch15 Ex 15.3; DIV ch25 Ex 25.13)*
- (challenging) Compute Christoffel symbols, Ricci, the scalar and the mixed Einstein tensor for the general time-dependent spherically symmetric metric. *Skill:* full curvature computation *(DIV ch06 Ex 6.32)*
- (challenging) Derive both Friedmann equations by computing the Ricci and Einstein tensors of the Robertson-Walker metric. *Skill:* Einstein tensor for cosmology *(DIV ch24 Ex 24.12)*

## Checks for understanding

- **Q (intuition):** The Einstein tensor is zero everywhere outside the Sun. A friend concludes that spacetime there is flat. How would you convince them otherwise?
  - **A:** G = 0 only says the Ricci tensor vanishes. The Weyl part of curvature is untouched, and it is real: two freely falling objects one above the other drift apart (tides), light bends, and gravitational waves pass through empty space. Flatness needs the whole Riemann tensor to vanish, and outside the Sun it does not (for example, the Kretschmann scalar is nonzero). *(targets: Where the Einstein tensor vanishes, spacetime is flat.)*
- **Q (working):** In n dimensions, compute g^μν G_μν and express R_μν in terms of G_μν. What happens when n = 2?
  - **A:** g^μν G_μν = R − ½ n R = (1 − n/2)R. Writing G for the trace, R = G/(1 − n/2) = −2G/(n − 2), so R_μν = G_μν + ½R g_μν = G_μν − (1/(n − 2)) G g_μν. In four dimensions this is R_μν = G_μν − ½G g_μν, and the trace of G is −R. For n = 2 the trace of G is zero and in fact G_μν ≡ 0 for every metric (Ricci = ½Rg), so Ricci cannot be recovered from G. *(targets: The ½ in trace reversal works in every dimension.)*
- **Q (working):** Compute the Einstein tensor of a 2-sphere of radius a and of a 3-sphere of radius a (Riemannian).
  - **A:** 2-sphere: R_ab = (1/a²)g_ab and R = 2/a², so G_ab = (1/a²)g_ab − ½(2/a²)g_ab = 0. 3-sphere: R_ij = (2/a²)g_ij and R = 6/a², so G_ij = (2/a²)g_ij − (3/a²)g_ij = −(1/a²)g_ij.
- **Q (working):** For the flat expanding universe the lowered orthonormal plane curvatures are R_t̂ît̂î = −ä/a for each time-space plane and R_îĵîĵ = H² for each space-space plane. Use the plane-sum rules to find G_t̂t̂ and G_x̂x̂, and explain why G_t̂t̂ ≠ 0 even though space is flat.
  - **A:** G_t̂t̂ is the sum of the three space-space planes: 3H². G_x̂x̂ = G^x̂_x̂ = −(R^{t̂ŷ}_{t̂ŷ} + R^{t̂ẑ}_{t̂ẑ} + R^{ŷẑ}_{ŷẑ}). Raising a time index flips the sign, so R^{t̂ŷ}_{t̂ŷ} = +ä/a, giving G_x̂x̂ = −(2ä/a + H²). The spatial slices are intrinsically flat, but the spacetime curvature of a spatial plane includes the stretching of the slice in time (extrinsic curvature), which contributes H² per plane. *(targets: The time-time Einstein component measures only the curvature of space at one instant.)*
- **Q (working):** Show that for a static star with g_rr = (1 − 2m(r)/r)⁻¹ the relation G_t̂t̂ = 2m′/r² turns the time-time field equation into the mass equation of stellar structure.
  - **A:** With G_t̂t̂ = 8πρ (G = c = 1, Λ = 0), 2m′/r² = 8πρ, so m′(r) = 4πr²ρ(r), the relativistic mass function obeying the same equation as Newtonian enclosed mass; in SI, dm/dr = 4πr²ρ with m measured in kilograms via 2Gm/(c²r).
- **Q (formal):** Prove that in four dimensions G_μν = 0 if and only if R_μν = 0, and use the result to state the vacuum Einstein equations without Λ in terms of Ricci.
  - **A:** If R_μν = 0 then R = 0 and G_μν = 0. Conversely, if G_μν = 0 its trace −R vanishes, so R = 0 and G_μν = R_μν = 0. Hence the vacuum equations G_μν = 0 are equivalent to R_μν = 0.
- **Q (formal):** A four-dimensional spacetime has R_μνρσ = K(g_μρ g_νσ − g_μσ g_νρ) with constant K. Find G_μν and the cosmological constant for which it solves G_μν + Λg_μν = 0.
  - **A:** Contracting: R_νσ = g^μρ R_μνρσ = K(4g_νσ − g_νσ) = 3K g_νσ, R = 12K, so G_μν = 3Kg_μν − 6Kg_μν = −3K g_μν. Then G + Λg = 0 requires Λ = 3K (positive for de Sitter, negative for anti-de Sitter, in course conventions; d'Inverno's signature flips the sign of K, so he writes Λ = −3K).

## Applications

- **Friedmann equations**: The time-time and space-space Einstein components of the Robertson-Walker metric set equal to the perfect-fluid source give the expansion and acceleration equations of cosmology. Key numbers: Flat case: 3H² = 8πρ in geometrized units, H² = 8πGρ/3 in SI with ρ a mass density; H₀ ≈ 70 km/s/Mpc gives a critical density 3H₀²/(8πG) ≈ 9.2 × 10⁻²⁷ kg/m³. *(GA ch36 Example 36.5 §36.4 p.382; legacy:manuscript-section-19-1-friedmann-derivation)*
- **Stellar structure**: The time-time component gives the mass function and the radial component gives the relativistic pressure-gradient equation, together the Tolman-Oppenheimer-Volkoff system. *(GA ch21 §21.2 p.231; SCH ch10 §10.2 p.271)*
- **Initial data for numerical relativity**: The normal-normal and normal-tangential components of the Einstein tensor contain no second time derivatives; set equal to matter they are the Hamiltonian and momentum constraints every simulation must solve first. *(SCH ch08 Ex 8.9; DIV ch14 §14.4 p.244)*

## History

- **Albert Einstein (1915):** Einstein first equated the Ricci tensor to matter in the autumn of 1915 and within weeks arrived at the version with the trace term, compatible with energy-momentum conservation; the combination now bears his name because he first recognised its importance for gravity. *(GA ch13 §13.3 p.145; SCH ch06 §6.6 p.164)*

## Tutor guidance

**Opening questions**

- If you had to write 'curvature equals matter', which two-index curvature object would you try first, and what test must it pass?
- Picture yourself at one point in space: which three planes pass through you, and what could 'the curvature of a plane' mean?
- Can there be curvature where there is no matter? Name an effect that would show it.

**Common questions**

- *Why subtract exactly half of R times the metric?* — Because the divergence of Ricci equals half the gradient of R (the contracted Bianchi identity). Subtracting half R times the metric subtracts exactly that gradient, leaving zero divergence for every metric; any other coefficient leaves a leftover proportional to the gradient of R.
- *Does the Einstein tensor contain all the curvature?* — No. In four dimensions it carries the ten Ricci components and none of the ten Weyl components. The Weyl part is the curvature present even in empty space: tides, light bending, gravitational waves.
- *Why call it trace-reversed?* — Take its trace in four dimensions and you get minus the trace of Ricci. Doing the same operation again gives back Ricci. Be careful: subtracting a quarter of R times the metric instead makes the trace zero, which is called trace-free, not trace-reversed.
- *What does the time-time component mean physically?* — For an observer with four-velocity u, G_μν u^μ u^ν is the sum of the sectional curvatures of three perpendicular spatial planes around them, and Einstein's equation sets it equal to 8π times the energy density that observer measures (plus a Λ term).
- *Is the Einstein tensor unique?* — In four dimensions, yes up to adding a multiple of the metric: Lovelock's theorem says the only symmetric, automatically divergence-free tensors built locally from the metric and its first two derivatives are a combination of G and g. That is why the field equations have only one extra freedom, the cosmological constant.

**Pitfalls when explaining**

- Never write or say a bare G when Newton's constant could also be meant; say 'Einstein tensor' and write G_μν with indices.
- Do not describe G as 'the curvature'; say 'the Ricci part of curvature, trace-reversed'.
- When using the plane-sum rules, keep track of index height: raising or lowering a time index flips a sign in the orthonormal frame.
- State the basis for components: coordinate G_00 for a static metric carries a factor e^{2Φ} that orthonormal G_t̂t̂ does not.
- Keep the ½ in the definition separate from the coefficient in the inverse relation, which depends on dimension.
- Do not let the flat-space-slices case suggest G_t̂t̂ is purely spatial curvature.

**When to show a demo**

- Right after defining G, open the six-plane board with the Schwarzschild preset: all Einstein readouts are zero while the tiles and Kretschmann are not.
- When a learner asks what a component means, click that component on the board and let them see which planes light up.
- During the star example, let the learner draw a density bump and watch G_t̂t̂ track 8πρ and drop to zero outside while the tidal tile stays nonzero.
- When the Ricci guess is proposed, use the trace-reversal calculator's Ricci-guess toggle to show which sources break it.

**Saying it aloud:** Say the definition as 'G mu nu equals R mu nu minus one half R g mu nu: the Ricci tensor minus half the scalar curvature times the metric.' Say the identity as 'the divergence of the Einstein tensor is zero for every metric.' For the trace: 'in four dimensions the trace of the Einstein tensor is minus R.' For the observer reading: 'the time-time part, for this observer, is the sum of the curvatures of the three spatial planes around them.' Pronounce hats as 'in the observer's frame' rather than reading index decorations, and say 'Einstein tensor' and 'Newton's constant' in full whenever both could be heard as G.

## Sources

- schutz ch06 (core): p.163 §6.6, p.164 §6.6
- schutz ch08 (core): p.184 §8.1, p.187 §8.2, p.191 §8.3
- gifted-amateur ch00 (mention): p.10 §0.6
- gifted-amateur ch11 (mention): p.127 §11.5
- gifted-amateur ch13 (core): p.146 §13.3, p.147 §13.4, p.150
- gifted-amateur ch21 (developed): p.231 §21.2, p.235
- gifted-amateur ch36 (revisited): p.383 §36.4, p.384 §36.4
- gifted-amateur ch40 (revisited): p.436 §40.4, p.437 §40.5
- dinverno ch06 (core): p.106 §6.12
- dinverno ch10 (revisited): p.183 §10.7, p.184 §10.8
- legacy manuscript-section-12-trace-subtraction-and-reversal (core)
- legacy lesson-contract-curvature-by-hand (developed)

## Review

**Verdict:** fixed

**Fixes**

- Teaching-path step 6 used G_t̂t̂ ≈ 2∇²Φ while the working level (correctly) uses Ψ; now says 2∇²Ψ with Ψ = Φ from the spatial equations for non-relativistic matter.
- Newtonian-calibration worked example: G^00 = 2R_00 only holds on shell for a pressureless source; now stated.
- Added a conventions entry for the sign of K in constant-curvature spacetimes: d'Inverno's (+,−,−,−) K is minus the course K, so his Λ = −3K, while the course and GA give Λ = 3K. Check 7 now flags the difference.

**Concerns**

- Independently verified the writer's orthonormal-frame rules and six-entry table: R_0̂0̂ = A+B+C, R_1̂1̂ = −A+D+E, G_0̂0̂ = D+E+F, G_1̂1̂ = B+C−F, the mixed off-diagonal G^0̂_1̂, Kretschmann 4Σ(entries²). The Schwarzschild pattern q(−2,1,1,−1,−1,2) gives G = 0 and Kretschmann 48M²/r⁶. Flat FLRW gives 3H² and −2ä/a − H². de Sitter gives G = −3Kg.
- Also checked: trace (1 − n/2)R and the 1/(n − 2) inverse; the 2-sphere and 3-sphere Einstein tensors; static-star 2m′/r² against Schutz Eq. 10.14; linearized G = −½□h̄ against the course □h̄ = −16πT; the metric variation sign against DIV 11.27 and GA 40.50/40.53; the Hamiltonian-constraint form against DIV 14.29.
- The linearized key equation cites SCH ch08 Ex 8.8, which derives the linearized Einstein tensor; the dossier attributes the Lorenz-gauge reduction (Eq. 8.41) to Exercise 8.10, which is not among its summarized exercises.
- The per-domain _index.md was not regenerated in this review.
