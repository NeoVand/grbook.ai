---
type: "concept"
id: "bianchi-identity"
title: "Bianchi identity"
domain: "curvature"
tier: "core"
aliases: ["second Bianchi identity", "differential Bianchi identity", "Bianchi identities"]
prerequisites: ["riemann-tensor-in-normal-coordinates", "symmetries-of-the-riemann-tensor", "covariant-derivative-of-a-tensor"]
leads_to: ["contracted-bianchi-identity", "weyl-tensor-field-equation", "bianchi-identity-in-differential-forms"]
sources: ["dinverno:ch06", "gifted-amateur:ch13", "gifted-amateur:ch43", "legacy:manuscript-section-09-bianchi-einstein-tensor", "schutz:ch06"]
review: "fixed"
---

# Bianchi identity

> The Bianchi identity is a rule every curvature tensor obeys: take the covariant derivative of the Riemann tensor, cycle the derivative index through the two loop-plane slots, and the three terms always add to zero. It is not a law of physics but a consistency condition, the curved-space cousin of 'the divergence of a curl vanishes' and of the magnetic half of Maxwell's equations. Contracting it gives the divergence-free Einstein tensor, which is why it sits underneath the field equations.

## Explanations by level

### Intuition

Imagine a tiny cardboard box floating in curved space. For each of its six faces, carry an arrow once around the edges of that face and note how much it has turned when it gets back; that turn is how much curvature 'passes through' the face. Now add up the turns for all six faces, each face walked in the outward sense. The total is always zero, whatever the space. The reason is bookkeeping, not physics: every edge of the box belongs to two faces and gets walked once in each direction, so the edge contributions cancel completely. A closed surface has no loose edge left over, and so curvature through a closed box cannot fail to balance. That balancing act, written for an infinitely small box, is the Bianchi identity. What it tells you is that curvature cannot vary from place to place in an arbitrary way: how it changes in one direction is tied to how it changes in the other two. The simplification here is that turns on different faces happen at slightly different places, so simply adding them is only exact in the limit of a vanishingly small box.

**Picture to hold:** A small cube with a curled arrow drawn on each face showing the rotation picked up round that face; opposite faces nearly cancel, and the leftover differences from the three pairs of faces add to exactly nothing.

**Assumes:** [[holonomy]], [[boundary-of-a-boundary-vanishes]]

### Working

In course conventions the identity reads ∇_λ R^ρ_σμν + ∇_μ R^ρ_σνλ + ∇_ν R^ρ_σλμ = 0: keep the first two slots of Riemann fixed and cycle the derivative index λ together with the loop-plane pair μν. Because Riemann is already antisymmetric in μν, this is the same as saying the antisymmetrised derivative ∇_[λ R^ρ_|σ|μν] vanishes. The cleanest proof picks locally inertial (normal) coordinates at a point P, where the Christoffel symbols vanish but their derivatives need not. There the covariant derivative of Riemann is just the partial derivative of the two ∂Γ terms, because any derivative of a ΓΓ product still carries a vanishing Γ. The cyclic sum then contains six third-order terms of the form ∂∂Γ that cancel in pairs since partial derivatives commute. The left side is a tensor, so if its components vanish in one chart at P they vanish in every chart, and P was arbitrary. The identity is automatic when some pair of the three cycled indices coincide, so in two dimensions it says nothing; the content starts in three dimensions. Its most important use is contraction: tracing ρ with μ and then σ with ν, using metric compatibility, gives ∇_μ R^μ_ν = ½ ∇_ν R, the divergence-free Einstein tensor. Do not confuse it with the cyclic (first, algebraic) identity R^ρ_[σμν] = 0, which involves no derivatives and removes one component from the Riemann count.

**Picture to hold:** Six ∂∂Γ tiles laid out in a ring; swapping the order of two partial derivatives pairs each tile with its negative, leaving an empty ring.

**Assumes:** [[riemann-curvature-tensor]], [[riemann-tensor-in-normal-coordinates]], [[symmetries-of-the-riemann-tensor]], [[covariant-derivative-of-a-tensor]], [[geodesic-coordinates]]

### Formal

Let ∇ be a torsion-free affine connection on a manifold of dimension n with curvature R(X,Y) = [∇_X, ∇_Y] − ∇_[X,Y], components R^ρ_σμν as in the course conventions. The second (differential) Bianchi identity is ∇_[λ R^ρ_|σ|μν] = 0, equivalently the three-term cyclic sum over (λ, μ, ν). It holds identically, for every such connection; no field equation or metric is needed, although for the Levi-Civita connection one may lower ρ and write it as ∇_[λ R_|ρσ|μν] = 0, and pair symmetry then lets the cycle run over the first pair instead. Proof: at any P choose coordinates with Γ(P) = 0 (possible exactly when torsion vanishes); then (∇_λ R^ρ_σμν)(P) = ∂_λ∂_μ Γ^ρ_νσ − ∂_λ∂_ν Γ^ρ_μσ, and the cyclic sum vanishes by symmetry of mixed partials; tensoriality extends the statement to all charts. Index-free, in Cartan language, it says the curvature 2-form has vanishing exterior covariant derivative, DΩ = dΩ + ω∧Ω − Ω∧ω = 0, while the individual component forms dΩ^ρ_σ are generally non-zero. With torsion the Cartan statement DΩ = 0 still holds, but the component identity picks up extra torsion-times-curvature terms, because coordinates with Γ(P) = 0 no longer exist. Content by dimension: in n = 2 it is empty; in n = 3, where Riemann is fixed by Ricci, it is equivalent to the contracted identity (3 relations); in n = 4 it imposes 20 independent linear relations on the 80 components of ∇R, leaving 60, which matches the count of third metric derivatives at P not removable by coordinate choice (200 − 140). Contractions: once, ∇_ρ R^ρ_σμν = ∇_μ R_σν − ∇_ν R_σμ; twice, ∇_μ G^μ_ν = 0. Substituting the Weyl decomposition turns it into a divergence equation for the Weyl tensor sourced by derivatives of Ricci (the Weyl field equation). Conventions: the identity is linear and homogeneous in R, so the overall sign of Riemann and the metric signature do not affect it; only index order and which slots are cycled must be read carefully.

**Picture to hold:** The curvature 2-form as an operator-valued flux: DΩ = 0 is the statement that its total flux through the boundary of any infinitesimal 3-cell vanishes.

**Assumes:** [[torsion-free-connection]], [[riemann-curvature-operator]], [[curvature-2-form]], [[exterior-covariant-derivative]], [[levi-civita-connection]]

## Prerequisites

- [[riemann-tensor-in-normal-coordinates]] — The standard proof works at a point where the Christoffel symbols vanish, so the learner needs curvature written in locally inertial coordinates.
- [[symmetries-of-the-riemann-tensor]] — Antisymmetry in the last pair is what makes the three-term cycle equal an antisymmetrisation and fixes the signs when contracting.
- [[covariant-derivative-of-a-tensor]] — The identity is about covariant derivatives of a rank-four tensor, so the learner must be able to read and manipulate them.

## Leads to

- [[contracted-bianchi-identity]] — Two contractions turn it into the statement that the Einstein tensor is divergence-free.
- [[weyl-tensor-field-equation]] — Rewriting it with the Weyl decomposition gives a Maxwell-like equation in which matter gradients source the Weyl curvature.
- [[bianchi-identity-in-differential-forms]] — The same content in Cartan language, DΩ = 0, with the boundary-of-a-boundary reading made exact.

## Related

- [[cyclic-identity]] — The algebraic (first) Bianchi identity; same cyclic shape but no derivative, and a completely different job.
- [[boundary-of-a-boundary-vanishes]] — The topological fact the identity expresses for curvature viewed as a flux.
- [[maxwell-equations-in-differential-forms]] — dF = 0 is its electromagnetic twin: the homogeneous Maxwell equations are the Bianchi identity of a gauge field.
- [[identity-versus-equation]] — The identity holds for every metric and so carries no physical information by itself, unlike a field equation.
- [[ricci-identity]] — Curvature as a commutator of covariant derivatives; an alternative proof applies the Jacobi identity to three such commutators.

## Key equations

### Differential Bianchi identity (course form)

$$
\nabla_\lambda R^\rho{}_{\sigma\mu\nu} + \nabla_\mu R^\rho{}_{\sigma\nu\lambda} + \nabla_\nu R^\rho{}_{\sigma\lambda\mu} = 0
$$

Cycle the derivative index through the loop-plane slots of Riemann and the sum vanishes, for every torsion-free connection and hence every metric. *(SCH ch06 (6.90) §6.6 p.162; GA ch13 (13.27) §13.3 p.146; GA ch43 (43.49) §43.3 p.474; DIV ch06 (6.83) §6.12 p.106)*

**Convention:** Riemann as in the course conventions, [∇_μ, ∇_ν]V^ρ = R^ρ_σμν V^σ. Schutz writes the all-lower version with semicolons, Gifted Amateur the mixed version with semicolons, d'Inverno the all-lower version with ∇ and an identity sign; all are equivalent.

### Antisymmetrised form

$$
\nabla_{[\lambda} R^\rho{}_{|\sigma|\mu\nu]} = 0 \quad\Longleftrightarrow\quad \nabla_{[\lambda} R_{|\rho\sigma|\mu\nu]} = 0
$$

Because Riemann is antisymmetric in its last two indices, full antisymmetrisation over the derivative and loop-plane indices is one third of the cyclic sum. *(GA ch43 (43.48) §43.3 p.474; DIV ch06 §6.12 p.106; DIV ch06 Ex 6.25)*

**Convention:** Vertical bars exclude σ (or ρσ) from the antisymmetrisation.

### Proof step in normal coordinates

$$
\left(\nabla_\lambda R^\rho{}_{\sigma\mu\nu}\right)(P) = \partial_\lambda\partial_\mu \Gamma^\rho{}_{\nu\sigma} - \partial_\lambda\partial_\nu \Gamma^\rho{}_{\mu\sigma} \quad (\Gamma(P) = 0)
$$

At a point where the connection coefficients vanish, the ΓΓ terms and the Christoffel corrections in ∇ drop out; the cyclic sum of these six terms cancels because partial derivatives commute. *(SCH ch06 (6.88)-(6.89) §6.6 p.162; legacy:manuscript-section-09-bianchi-einstein-tensor)*

**Convention:** Schutz does the equivalent step with third derivatives of the metric (Eq. 6.88); the Γ version shows the metric is not needed.

### Once-contracted identity

$$
\nabla_\rho R^\rho{}_{\sigma\mu\nu} = \nabla_\mu R_{\sigma\nu} - \nabla_\nu R_{\sigma\mu}
$$

The divergence of Riemann on its first index equals a 'curl' of the Ricci tensor; in vacuum (Ricci zero) the Riemann tensor is divergence-free. *(SCH ch06 (6.93) §6.6 p.163; GA ch13 (13.28) §13.3 p.146)*

**Convention:** Obtained by setting ρ = λ and using R^ρ_σνρ = −R_σν. Schutz's Eq. 6.93 and GA's Eq. 13.28 are the same relation with other index names.

### Cartan form

$$
D\Omega^\rho{}_\sigma \equiv d\Omega^\rho{}_\sigma + \omega^\rho{}_\lambda \wedge \Omega^\lambda{}_\sigma - \Omega^\rho{}_\lambda \wedge \omega^\lambda{}_\sigma = 0
$$

The curvature 2-form is covariantly closed; the connection terms compensate for the fact that the component forms themselves are not closed. *(GA ch43 (43.28)-(43.29) §43.3 p.471; GA ch43 Example 43.6 §43.3 p.472)*

**Convention:** Gifted Amateur writes this as d𝓡 = 0 for the operator 𝓡 = ½(e_μ∧e_ν)𝓡^μν, and its Step I (Eq. 43.29) is this component equation.

## Conventions across the books

| Issue | Schutz | Gifted Amateur | d'Inverno | Course choice |
| --- | --- | --- | --- | --- |
| Index placement and which slots are cycled | All indices lowered: R_αβμν;λ + R_αβλμ;ν + R_αβνλ;μ = 0, first pair fixed, last pair and derivative index cycled (Eq. 6.90). | First index up: R^α_βγδ;λ + R^α_βλγ;δ + R^α_βδλ;γ = 0 (Eq. 13.27, 43.49), plus the compact form R^α_β[μν;λ] = 0; the printed Eq. 43.56 drops the β. | All lowered with Latin indices and the derivative in front: ∇_a R_debc + ∇_c R_deab + ∇_b R_deca ≡ 0 (Eq. 6.83), equivalently R_de[ab;c] ≡ 0. | ∇_λ R^ρ_σμν + ∇_μ R^ρ_σνλ + ∇_ν R^ρ_σλμ = 0 with ∇ in front and first index up, matching the course Riemann definition; all three book forms are the same identity. |
| Derivative notation and the identity sign | Semicolon for covariant derivative, comma for partial; the proof passes from commas to semicolons because Γ = 0 at the point. | Semicolons in components; exterior derivative d acting on operator-valued forms (d𝓡 = 0) in ch43, with hats marking local-inertial-frame components. | ∇ notation with a triple-bar ≡ to mark identities valid for every metric, and a starred equals for steps valid only in geodesic coordinates. | Write ∇ and say 'for every metric' in words rather than using ≡; when a step holds only in special coordinates, say so explicitly. |
| What the name 'Bianchi identity' refers to | 'Bianchi identities' for the differential identity; also says the twice-contracted form is often simply called the Bianchi identities. | 'Bianchi identity' for the differential identity, and also for the electromagnetic dF = 0 and the gauge-field version in ch42-44; the algebraic cyclic identity is not given this name. | 'Bianchi identities' for the differential identity; the algebraic cyclic relation is listed among the symmetries in Eq. 6.82 without a separate name. | 'Bianchi identity' means the differential identity; the algebraic one is the 'cyclic identity'; always add 'contracted' when the Ricci or Einstein form is meant. |
| Special coordinates used in the proof | Locally inertial coordinates at a point, working from the second-derivative-of-metric form of Riemann. | Riemann normal coordinates and a small coordinate cube (component proof), after a frame-based Cartan proof. | Geodesic coordinates; the proof itself is Exercise 6.25. | Say 'locally inertial (normal) coordinates at P' and stress that only Γ(P) = 0 is used, which requires zero torsion but not a metric. |
| Riemann sign and metric signature | MTW-type Riemann with signature (−,+,+,+). | MTW-type Riemann with signature (−,+,+,+). | Same Riemann and Ricci index conventions as MTW, but signature (+,−,−,−). | Course Riemann and signature (−,+,+,+). The identity is linear and homogeneous in curvature, so neither a sign flip of Riemann nor the signature changes it. |

## How the sources teach it

### schutz

**Route:** Right after the symmetries of Riemann, differentiates the locally inertial expression of Riemann in terms of second metric derivatives, notes the cyclic sum cancels because partial derivatives commute and the metric is symmetric, promotes commas to semicolons since Γ vanishes at the point, and declares a tensor identity. Immediately defines Ricci and contracts to reach the divergence-free Einstein tensor, previewing G = 8πT and energy conservation.

**Representation:** Pure component algebra in a local inertial frame; no picture.

**Strengths:** Short, complete and honest about the key logical move (a tensor vanishing in one chart vanishes in all); ties the identity directly to its payoff two equations later.

**Weaknesses:** The cancellation itself is left to Exercise 6.24, no geometric meaning is offered, and learners arrive without having computed a single Riemann component; the metric-derivative route hides that only Γ(P) = 0 is needed. *(SCH ch06 §6.6 p.162; SCH ch06 (6.88)-(6.90) §6.6 p.162; SCH ch06 Ex 6.24)*

### gifted-amateur

**Route:** Chapter 13 quotes the identity without proof inside Example 13.3, with the slogan that the boundary of a boundary is zero (as behind div curl = 0), and uses it only to contract. Chapter 43 returns with a full geometric route: charge conservation, then dF = 0 for electromagnetism from Stokes and a small cube, then the gravitational version d𝓡 = 0 proved in three Cartan steps, then the closed-cube curvature-flux argument in Riemann normal coordinates to recover components, and finally the Weyl field equation.

**Representation:** Differential forms, parallel scroll diagrams for electromagnetism and gravity (Fig. 43.3), an explicit cube calculation, and a Maxwell analogy for the Weyl tensor.

**Strengths:** The only source that says what the identity means; the electromagnetism-first template lets learners transfer a familiar argument; the Weyl field-equation reframing explains vacuum curvature propagating from matter.

**Weaknesses:** Separated from its use by thirty chapters; the Cartan proof is long and index-heavy; the finite-integral language glosses over the fact that vectors in different tangent spaces cannot be added, so the argument is exact only infinitesimally; a printed index is dropped in Eq. 43.56. *(GA ch13 Example 13.3 §13.3 p.146; GA ch43 §43.3 p.471; GA ch43 Fig. 43.3 §43.3 p.472; GA ch43 Example 43.6 §43.3 p.472; GA ch43 §43.3 p.473; GA ch43 Example 43.8 §43.3 p.474)*

### dinverno

**Route:** Lists the algebraic symmetries of the lowered curvature tensor, counts components, then states the differential identity as most easily proved in geodesic coordinates and immediately defines Ricci, the curvature scalar and the Einstein tensor with its contracted identity. Proofs are exercises. The identity resurfaces in later chapters through its contracted form.

**Representation:** Terse component statement with the identity sign ≡; no geometric interpretation.

**Strengths:** Compact reference statement with the equivalent antisymmetrised form; clear signal that this is an identity, not an equation; warns that other authors flip Riemann or Ricci signs.

**Weaknesses:** No motivation, picture or worked proof in the text; learners who skip Exercise 6.25 never see why it holds or what it means. *(DIV ch06 §6.12 p.106; DIV ch06 (6.83) §6.12 p.106; DIV ch06 Ex 6.25)*

### legacy

**Route:** Placed after Ricci and Weyl: proves the cyclic differential identity in normal coordinates by showing the second derivatives of Γ cancel pairwise, contracts it to div Ricci = ½ grad R, defines G and notes Λg is also divergence-free, then warns that divergence-free is not constant and closes with dimension facts (G vanishes in 2D, Weyl vanishes in 3D).

**Representation:** Index derivation with every contraction shown; a fluid-outflow analogy for divergence-free versus constant.

**Strengths:** Uses the Γ-based proof (cleaner than the metric one), keeps the payoff adjacent, and anticipates the divergence-free-means-constant error.

**Weaknesses:** Contains an unused Jacobi-identity aside and no concrete divergence-free example; no picture of what the identity means geometrically. *(legacy:manuscript-section-09-bianchi-einstein-tensor; legacy:manuscript-chapter-09-ricci-weyl-einstein)*

## Recommended teaching path

1. **1. Motivating question** — Ask: at each point curvature is twenty numbers, but can those numbers change from place to place in any way we like, or does geometry itself forbid some patterns? Remind the learner that the metric's second derivatives are the curvature, so derivatives of curvature are third derivatives of the metric, and those are not all independent. *Why:* It frames the identity as a constraint that must exist, rather than a formula dropped from nowhere. *(SCH ch06 §6.6 p.162; legacy:manuscript-section-09-bianchi-einstein-tensor)*
2. **2. Warm up with a familiar identity** — Revisit div curl = 0 and dF = 0 with a small cube: sum the circulation of a field around all six faces and watch each edge appear twice with opposite orientation. *Why:* Learners already trust this flat-space fact, and the cube bookkeeping transfers directly to curvature. *(GA ch13 §13.3 p.146; GA ch43 Example 43.2 §43.2 p.469)*
3. **3. The curvature picture** — Replace circulation by holonomy: each face of a tiny cube rotates a transported vector by an amount set by Riemann in that face's plane. Opposite faces differ by a derivative; the three differences must add to zero. Show this live in the curvature-flux cube demo. *Why:* Gives the identity a meaning (zero net curvature flux through a closed surface) before any indices appear. *(GA ch43 Fig. 43.3 §43.3 p.472; GA ch43 §43.3 p.473)*
4. **4. The proof in normal coordinates** — Choose coordinates with Γ(P) = 0. Write ∇R at P as two ∂∂Γ terms, form the cyclic sum, and let the learner pair the six terms. Then state the tensor argument: zero components in one chart at an arbitrary point means zero everywhere. *Why:* It is the shortest rigorous route, and doing it with Γ rather than the metric reveals that only zero torsion is needed. *(SCH ch06 (6.88)-(6.90) §6.6 p.162; DIV ch06 §6.12 p.106; legacy:manuscript-section-09-bianchi-einstein-tensor)*
5. **5. Check and contrast** — Have the learner show the identity is empty in two dimensions (some pair of cycled indices always coincides) and contrast it with the algebraic cyclic identity, which works at a single point and trims the component count from 21 to 20. *Why:* Guards against the common merger of the two identities and against believing the proof holds only in special coordinates. *(legacy:lab-riemann-independent-components; DIV ch06 §6.12 p.106)*
6. **6. Payoff and preview** — Contract once (divergence of Riemann equals a curl of Ricci) and twice (∇_μ R^μ_ν = ½∇_ν R), hand off to the contracted identity and the Einstein tensor, and for advanced learners show the Weyl field-equation reading. *Why:* Learners see immediately why an abstract identity matters: it builds conservation into gravity and explains how vacuum curvature is sourced by distant matter. *(SCH ch06 §6.6 p.163; GA ch13 Example 13.3 §13.3 p.146; GA ch43 Example 43.8 §43.3 p.474)*

## Analogies

- **The divergence of a curl is always zero** (intuition): In vector calculus, a field that is a curl has no sources, because the flux of a curl through a closed surface is a circulation around the surface's boundary, and a closed surface has none. The Bianchi identity is the same structural fact for curvature, which is the 'curl' of the connection. *Limits:* The connection is not a vector field and curvature is matrix valued, so there are extra connection terms (the D in DΩ); the analogy fixes the shape of the statement, not its details. *(GA ch13 §13.3 p.146)*
- **Electromagnetism as a template: F = dA and dF = 0 versus curvature from the connection and DΩ = 0** (working): The field strength is built from a potential, and that alone forces the homogeneous Maxwell equations (no magnetic monopoles, Faraday's law). Curvature is built from the connection in the same way, and that alone forces the Bianchi identity. *Limits:* In gravity the forms are operator valued, the exterior derivative of a vector does not square to zero, and finite integrals of vectors across different tangent spaces are undefined; the parallel is exact only for infinitesimal regions. Also, dF = 0 is half of Maxwell's field equations, whereas the gravitational identity is not a field equation at all. *(GA ch43 §43.3 p.472; GA ch43 Fig. 43.3 §43.3 p.472; GA ch42 §42.2 p.456)*
- **A shared-edge ledger** (intuition): Picture a box made of six rooms that each keep a ledger of arrows walked around their walls. Every wall edge is shared by two rooms that record it with opposite signs, so the combined ledger for the whole box always sums to zero, no matter what entries the rooms made. *Limits:* Captures the cancellation but not that the 'entries' are rotations which do not commute; the cancellation of commuting pieces is exact only at leading order in the box size. *(GA ch44 Fig. 44.5 p.483)*
- **Bianchi identity as a Maxwell equation for the Weyl tensor** (formal): Splitting Riemann into Weyl and Ricci parts, the identity becomes 'divergence of Weyl equals a current made from derivatives of Ricci', just as the divergence of F equals the charge current. Since Ricci is fixed locally by matter, matter gradients act as sources of the tidal curvature that reaches empty regions. *Limits:* The 'current' involves derivatives of matter, not matter itself, and the equation is nonlinear through the covariant derivative; it is suggestive of propagation rather than a solvable wave equation on its own. *(GA ch43 Example 43.8 §43.3 p.474)*

## Misconceptions

- **The Bianchi identity is an extra law of nature, like a field equation, that spacetimes must be made to satisfy.** — It is an identity: it holds for the curvature of any torsion-free connection, whatever the metric, whether or not any physics is imposed. It restricts nothing about which spacetimes exist; it only says derivatives of curvature are not independent. *Why tempting:* In electromagnetism dF = 0 is listed among Maxwell's equations, which look like physical laws, and the Bianchi identity appears right next to the Einstein equation. *Diagnostic:* Take any metric you like, even one with no physical meaning. Does its Riemann tensor satisfy the Bianchi identity? What does your answer imply about whether the identity contains physics? *(GA ch43 §43.2 p.469; DIV ch06 §6.12 p.106)*
- **Because the proof uses locally inertial (normal) coordinates, the identity is only valid in those coordinates.** — The special coordinates are a calculational convenience at one point. The left side is a tensor; if all its components vanish in one chart at P they vanish in every chart at P, and P is arbitrary. *Why tempting:* Learners are rightly warned that Γ = 0 and 'commas become semicolons' are coordinate-specific, and over-apply the warning. *Diagnostic:* The Christoffel symbols vanish at P only in special coordinates, yet we conclude the Bianchi identity holds in polar coordinates too. What property of the expression makes that step legitimate, and why would the same step fail for a statement like Γ = 0? *(SCH ch06 §6.6 p.162; GA ch43 §43.3 p.474)*
- **The Bianchi identity and the cyclic identity R^ρ_[σμν] = 0 are the same thing (or one implies the other).** — The cyclic (first, algebraic) identity involves no derivatives and constrains curvature at a single point, removing one component in four dimensions. The differential (second) identity involves ∇R and constrains how curvature varies between points. They have different content and different consequences. *Why tempting:* Both are three-term cyclic sums, and many texts call them the first and second Bianchi identities. *Diagnostic:* If someone hands you the values of R^ρ_σμν at a single point and nothing else, which of the two identities can you check, and which cannot even be stated? *(legacy:lab-riemann-independent-components; DIV ch06 §6.12 p.106)*
- **dR = 0 in Cartan language means each component curvature 2-form Ω^ρ_σ is closed, dΩ^ρ_σ = 0.** — The component forms are generally not closed: dΩ^ρ_σ = Ω^ρ_λ∧ω^λ_σ − ω^ρ_λ∧Ω^λ_σ. Only the covariant exterior derivative, which includes the rotation of the basis, vanishes. *Why tempting:* The notation d𝓡 = 0 looks like a component statement, and in electromagnetism the components of dF vanish directly. *Diagnostic:* In an orthonormal frame on a sphere of radius a, is the single curvature 2-form closed? Is that enough to decide whether dΩ^ρ_σ = 0 holds component by component in four dimensions? *(GA ch43 (43.29) §43.3 p.471; GA ch43 §43.3 p.472)*
- **The Bianchi identity by itself proves that matter conserves energy and momentum.** — The identity gives ∇_μ G^μν = 0 for geometry alone. Conservation of T follows only once the field equation G = 8πT is imposed (or, independently, from the matter field equations). The identity is what makes the field equation consistent with conservation. *Why tempting:* Popular summaries say the Bianchi identity 'encodes energy conservation'. *Diagnostic:* In a toy universe where matter does not couple to curvature at all, does the Bianchi identity still hold? Does it then say anything about the matter's energy? *(SCH ch06 §6.6 p.164; legacy:manuscript-section-15-noether-killing-charges-redshift)*

## Thought experiments

- **The closed box of curvature**: Enclose an infinitesimal region of a curved three-dimensional space in a cube and, for each face, transport a vector around the face's boundary, recording the rotation. Walk each face in the outward sense and add the six rotations to leading order in the cube size. *Lesson:* The total vanishes for every geometry because every edge is walked twice in opposite directions; written out, the leftover differences between opposite faces are exactly the three terms of the Bianchi identity. *(GA ch43 §43.3 p.473; GA ch44 Fig. 44.5 p.483)*

## Visualizations

### Curvature-flux cube · interactive-3d · high priority

A small cube sits inside a chosen curved 3-geometry. Each face shows the rotation a transported vector picks up around it (an axis-and-angle glyph built from Riemann in that face's plane). Opposite-face differences appear as derivative arrows for the x, y and z pairs, and a sum dial adds the three terms of the cyclic identity.

**Interaction:** Pick a geometry (3-sphere, hyperbolic 3-space, spatial Schwarzschild slice, or a draggable Gaussian bump in a conformally flat metric), drag the cube around, rotate it, and shrink or grow it. Toggle 'remove one face' to see the sum stop cancelling. A readout shows each term and the residual relative to the largest term as the cube shrinks.

**Model:** Metric g_ij(x) given analytically; Christoffel symbols and Riemann from finite differences; covariant derivatives of Riemann computed with the Christoffel corrections included (they vanish in normal coordinates at the cube centre). Face rotation ≈ R^a_bjk times face area; the cyclic sum reads zero up to discretisation error scaling as h². Constant-curvature presets (3-sphere, hyperbolic space) have ∇R = 0, so each of the three terms vanishes on its own; they are the control case. The Schwarzschild slice and the bump show three nonzero terms cancelling. In three dimensions the identity carries only three independent relations, the same content as the contracted identity.

**Inspired by:** GA ch43 Fig. 43.3 §43.3 p.472; GA ch43 §43.3 p.473

**Legacy assets:** engine-independent-curvature-checker

### Six tiles that cancel: the normal-coordinate proof · interactive-2d · medium priority

A step-through card where ∇_λR, ∇_μR and ∇_νR at P expand into six ∂∂Γ tiles on a ring. The learner drags tiles that differ only in the order of partial derivatives onto each other and they annihilate.

**Interaction:** Step buttons for 'set Γ(P) = 0', 'drop ΓΓ terms', 'expand', 'pair'; a side panel explains why each step is allowed; a final button applies the tensor argument and switches the display to a generic chart.

**Model:** Symbolic: course Riemann definition evaluated at a point with vanishing connection; commutation of partial derivatives.

**Inspired by:** SCH ch06 (6.88)-(6.90) §6.6 p.162; DIV ch06 Ex 6.25

**Legacy assets:** manuscript-section-09-bianchi-einstein-tensor

### Electromagnetism and gravity side by side · interactive-2d · medium priority

Two synchronized columns run the same boundary-of-a-boundary argument: potential A to field F to dF = 0, and connection to curvature to DΩ = 0. Each row highlights the corresponding object and flags where gravity needs an extra connection term.

**Interaction:** Step both columns together or independently; hover any object to see its counterpart; a toggle reveals the Weyl-as-Maxwell dictionary (F to Weyl, current to Ricci gradients).

**Inspired by:** GA ch43 Fig. 43.3 §43.3 p.472; GA ch43 Example 43.2 §43.2 p.469; GA ch43 Example 43.8 §43.3 p.474

### Two cyclic identities, two jobs · interactive-2d · low priority

A split panel: on the left a single-point Riemann component board (the 21 to 20 reduction via the algebraic cyclic identity); on the right a strip of neighbouring points where the differential identity links how components vary.

**Interaction:** Select components on the left to see the one algebraic relation; move along the strip on the right to see the three derivative terms of the Bianchi identity balance; a dimension switch (2, 3, 4) shows the differential identity is empty in 2D.

**Model:** Algebraic curvature tensor at a point; Riemann of a simple 3D metric along a line for the derivative panel.

**Inspired by:** DIV ch06 §6.12 p.106

**Legacy assets:** lab-riemann-independent-components

## Worked examples

- **From the local-inertial form of Riemann to the Bianchi identity and onward to G** (working): The full chain in a few lines: differentiate, cancel in the cyclic sum, promote to a tensor identity, then contract twice to reach the divergence-free Einstein tensor. *(SCH ch06 §6.6 p.162)*
- **Electromagnetic cube: extracting the component form of dF = 0** (working): Summing the potential around the edges of all faces of a coordinate cube gives zero identically, and written face by face that zero is a cyclic sum of derivatives of F; the template for the gravitational case. *(GA ch43 Example 43.2 §43.2 p.469)*
- **Cartan proof that the curvature operator is covariantly closed** (formal): How the non-closedness of the component curvature forms is exactly compensated by the rotation of the basis bivectors. *(GA ch43 Example 43.4 §43.3 p.471; GA ch43 Example 43.6 §43.3 p.472)*
- **Gravitational cube in Riemann normal coordinates** (working): Opposite faces of a small cube contribute curvature in that plane evaluated at two positions; their differences, summed over the three pairs, give the component Bianchi identity. *(GA ch43 §43.3 p.473; GA ch43 (43.46)-(43.49) §43.3 p.474)*
- **Bianchi identity as a Weyl field equation** (formal): Substituting the Weyl decomposition gives a divergence of Weyl sourced by derivatives of Ricci, the gravitational analogue of Maxwell's sourced equations. *(GA ch43 Example 43.8 §43.3 p.474)*
- **Legacy normal-coordinate proof with every contraction shown** (working): The Γ-based cancellation, the once- and twice-contracted identities, and the dimension remarks, in course conventions. *(legacy:manuscript-section-09-bianchi-einstein-tensor)*

## Exercises

- (intro) Carry out the cancellation that turns the differentiated local-inertial Riemann expression into the cyclic sum identity. *Skill:* index bookkeeping with commuting partial derivatives *(SCH ch06 Ex 6.24)*
- (standard) Prove the differential identity in geodesic coordinates, show it is equivalent to the antisymmetrised form, and deduce the contracted identity for the Einstein tensor. *Skill:* proof in special coordinates and contraction *(DIV ch06 Ex 6.25)*
- (intro) Check that the cyclic Bianchi sum can be written compactly as an antisymmetrisation over the derivative index and the last two Riemann slots (watch the dropped index in the printed statement). *Skill:* antisymmetrisation notation *(GA ch43 Ex 43.1)*
- (challenging) Show that the Weyl divergence equation is equivalent to a contraction of the Bianchi identity, using the contracted identity. *Skill:* Weyl decomposition and index gymnastics *(GA ch43 Ex 43.2)*
- (challenging) Show that if the Riemann tensor has the maximally symmetric form at every point, its scalar coefficient cannot vary in space (a Schur-type result from the contracted identity). *Skill:* using the identity to constrain geometry *(GA ch16 Ex 16.5)*
- (challenging) For a gauge field, sum three composite loop paths over a closed cube to obtain the cyclic sum of covariant derivatives of the field strength, and relate its vanishing to the Jacobi identity. *Skill:* holonomy bookkeeping for non-abelian fields *(GA ch44 Ex 44.1)*

## Checks for understanding

- **Q (intuition):** A classmate says: 'The Bianchi identity is one of the rules that tells spacetime how to curve in response to matter.' What is wrong with this?
  - **A:** The Bianchi identity holds for the curvature of every metric, including ones with no physical meaning, so it cannot encode any response to matter. It is a consistency condition on how curvature varies, like div curl = 0. The rule linking curvature to matter is the Einstein field equation; the Bianchi identity only guarantees that equation is compatible with energy-momentum conservation. *(targets: The Bianchi identity is an extra law of nature that spacetimes must be made to satisfy.)*
- **Q (working):** Show that the Bianchi identity is automatically satisfied whenever two of the three cycled indices λ, μ, ν are equal, and conclude what it says on a two-dimensional surface.
  - **A:** If μ = ν the first term contains R^ρ_σμμ = 0 and the other two are ∇_μ R^ρ_σμλ + ∇_μ R^ρ_σλμ = 0 by antisymmetry in the last pair. The cases λ = μ and λ = ν work the same way. In two dimensions the three indices take only two values, so two always coincide and the identity holds trivially: it carries no information about a 2D geometry.
- **Q (working):** Contract ρ with λ in ∇_λ R^ρ_σμν + ∇_μ R^ρ_σνλ + ∇_ν R^ρ_σλμ = 0. Express the result using the Ricci tensor R_σν = R^ρ_σρν.
  - **A:** The first term becomes ∇_ρ R^ρ_σμν. The second contains R^ρ_σνρ = −R^ρ_σρν = −R_σν, giving −∇_μ R_σν. The third contains R^ρ_σρμ = R_σμ, giving +∇_ν R_σμ. Hence ∇_ρ R^ρ_σμν = ∇_μ R_σν − ∇_ν R_σμ: the divergence of Riemann is a curl of Ricci. In vacuum, where Ricci vanishes, Riemann is divergence-free.
- **Q (formal):** The proof sets the Christoffel symbols to zero at P. Why is that legitimate for concluding the identity in any coordinates, and does the argument need a metric?
  - **A:** The quantity ∇_λR^ρ_σμν + cyclic is a tensor, so if its components vanish at P in one chart they vanish at P in every chart; P was arbitrary. Coordinates with Γ(P) = 0 exist precisely when the connection is torsion-free, and the calculation uses only the definition of Riemann in terms of Γ, so no metric is required. The metric enters only if we lower indices or contract. *(targets: Because the proof uses locally inertial coordinates, the identity is only valid in those coordinates.)*
- **Q (intuition):** Which of these can you test with the curvature components at one point only: the cyclic identity R^ρ_[σμν] = 0 or the Bianchi identity? Explain.
  - **A:** Only the cyclic identity, which is algebraic. The Bianchi identity involves covariant derivatives of Riemann and so needs the curvature in a neighbourhood of the point. *(targets: The Bianchi identity and the cyclic identity are the same thing.)*

## Applications

- **Consistency of the Einstein field equations**: Twice contracted, the identity makes the Einstein tensor divergence-free for every metric, so equating it to a conserved stress-energy tensor is consistent; this is how Einstein's left-hand side is selected. *(SCH ch06 §6.6 p.163; SCH ch08 §8.1 p.184)*
- **Vacuum curvature sourced by distant matter**: Rewritten for the Weyl tensor, the identity shows how gradients of matter density act as sources for tidal curvature in empty regions, the background to gravitational waves and the tides around stars. *(GA ch43 Example 43.8 §43.3 p.474)*
- **Checking linearized curvature**: At first order about flat spacetime the covariant derivatives become partial derivatives, and the linearized Riemann tensor built from h_μν satisfies the cyclic sum identically, a quick consistency test for any hand-derived linearized curvature. *(DIV ch21 (21.8)-(21.9) §21.1 p.402)*

## History

- **Aurel Voss, Gregorio Ricci-Curbastro, Luigi Bianchi (1880-1902):** A contracted form was found by Voss in 1880; Ricci-Curbastro is reported to have had the full identity around 1889; Bianchi published it in 1902, and it carries his name. *(GA ch43 p.467)*

## Tutor guidance

**Opening questions**

- Why is the divergence of a curl always zero? Can you explain it with a small box rather than with components?
- Curvature is made of second derivatives of the metric. If you take one more derivative, do you expect all the resulting numbers to be independent?
- What is the difference between an identity and an equation? Give an example of each from electromagnetism.

**Common questions**

- *Is this the same as the 'first Bianchi identity' I have seen elsewhere?* — No. The first (algebraic, cyclic) identity says the cyclic sum of Riemann over its last three slots vanishes at a point, with no derivatives. What we call the Bianchi identity is the second, differential one, about derivatives of curvature. Both are three-term cyclic sums, which is why they get confused.
- *If it holds for every metric, why is it useful?* — Precisely because it holds for every metric, it tells us something any field equation must respect. Contracted twice it says the Einstein tensor has zero divergence automatically, so G = 8πT forces matter to conserve energy and momentum, and it shows that four of the ten Einstein equations are not independent.
- *Does the Bianchi identity need the metric?* — No. It holds for any torsion-free connection; the proof uses only coordinates where the connection coefficients vanish at a point. The metric is needed only when we lower indices or contract to get Ricci and Einstein tensors.
- *What does 'boundary of a boundary is zero' have to do with it?* — Curvature is like the circulation of the connection around small loops. The total of that circulation over all the faces of a closed box is a sum over edges, and every edge is counted twice with opposite signs. So the curvature flux through any closed surface vanishes, and for an infinitesimal box that statement is the Bianchi identity.

**Pitfalls when explaining**

- Do not call it a law or an equation of motion; always say identity and give the div-curl comparison.
- When using normal coordinates, say explicitly that only Γ(P) = 0 is used and that the conclusion is promoted by tensoriality; otherwise learners think it holds only in those coordinates.
- State which slots are being cycled; learners often cycle all four indices or the first three, which gives a different (wrong or algebraic) statement.
- Do not present the finite cube argument as exact: rotations on different faces live at different points and do not simply add except to leading order.
- Keep the name 'Bianchi identity' for the differential identity; use 'cyclic identity' for the algebraic one to avoid merging them.
- Do not demonstrate the cancellation only on a sphere or hyperbolic space: there ∇R = 0 and every term is zero separately, so the learner sees no balancing at all.

**When to show a demo**

- After the div-curl warm-up, open the curvature-flux cube and let the learner drag it into a region of strong curvature: the face rotations change a lot, but the sum dial stays at zero.
- Use the 'remove one face' toggle when a learner doubts the cancellation is automatic.
- During the proof, hand control of the six-tile card to the learner and let them find the pairs themselves.

**Saying it aloud:** Say the equation as: 'the covariant derivative of the Riemann tensor, cycled around the derivative index and the last two indices, adds up to zero.' For the course form: 'nabla lambda of R rho sigma mu nu, plus nabla mu of R rho sigma nu lambda, plus nabla nu of R rho sigma lambda mu, equals zero.' Stress the pattern (lambda mu nu, then mu nu lambda, then nu lambda mu) rather than every index. For the once-contracted form say 'the divergence of Riemann equals the curl of Ricci.' Pronounce nabla as 'del' or 'nabla' consistently within a lesson.

## Sources

- schutz ch06 (core): p.162 §6.6, p.163 §6.6
- gifted-amateur ch13 (introduced): p.146 §13.3
- gifted-amateur ch43 (core): p.467, p.471 §43.3, p.472 §43.3, p.473 §43.3, p.474 §43.3
- dinverno ch06 (core): p.106 §6.12
- legacy manuscript-section-09-bianchi-einstein-tensor (core)

## Review

**Verdict:** fixed

**Fixes**

- Formal level: the torsion remark was ambiguous; now says DΩ = 0 survives with torsion while the component identity gains torsion-times-curvature terms.
- Curvature-flux cube demo: noted that constant-curvature presets have ∇R = 0 (each term zero, a control case) and that nontrivial cancellation needs the Schwarzschild slice or bump; added the 3D content remark.
- Added an application on linearized curvature (DIV ch21) from the evidence, and a tutor pitfall about demoing only on constant-curvature spaces.

**Concerns**

- Independently checked the writer's counting claim: third metric derivatives 200 minus fourth-order coordinate freedom 140 gives 60 free components of ∇R in 4D, so the identity imposes 80 - 60 = 20 relations; 3D gives 18 - 15 = 3 and 2D gives 0, matching n²(n²-1)(n+2)/24. Also re-derived the normal-coordinate cancellation, the once-contracted form, the twice-contracted form and the Cartan form DΩ = dΩ + ω∧Ω - Ω∧ω = 0.
- Spot-checked refs against dossiers (SCH ch06 Eqs. 6.88-6.93, GA ch43 Eqs. 43.28/43.49/43.56 and Examples 43.2/43.6/43.8, GA ch44 Fig. 44.5 and Ex 44.1, GA ch43 p.467 history, DIV ch06 Eq. 6.83 and Ex 6.25, legacy asset ids): all present.
- The per-domain _index.md was not regenerated in this review.
