---
type: "concept"
id: "ricci-identity"
title: "Ricci identity"
domain: "curvature"
tier: "core"
aliases: ["commutator of covariant derivatives", "[nabla_c, nabla_d]", "non-commuting covariant derivatives"]
prerequisites: ["riemann-curvature-tensor", "second-covariant-derivative", "torsion-free-connection"]
leads_to: ["geodesic-deviation-equation", "raychaudhuri-equation", "null-raychaudhuri-equation", "integrability-condition-for-parallel-fields", "gauss-codazzi-equations", "killing-vector-ricci-identity"]
sources: ["dinverno:ch06", "dinverno:ch10", "dinverno:ch14", "dinverno:ch23", "gifted-amateur:ch35", "gifted-amateur:ch44", "gifted-amateur:ch50", "legacy:manuscript-section-8-1-8-3-riemann-commutator-and-loop", "schutz:ch06"]
review: "fixed"
---

# Ricci identity

> In curved spacetime the order of two covariant derivatives matters: swap them on a vector and the difference is the Riemann tensor acting on that same vector, with the two derivative directions filling its last two slots. Every index of a bigger tensor contributes its own curvature term, with a plus sign for upper indices and a minus sign for lower ones, while a scalar feels nothing. It is the tiny-loop picture of curvature squeezed down to a single point.

## Explanations by level

### Intuition

Imagine holding an arrow on a globe and keeping it as straight as you can while you step. Take a tiny step east and then a tiny step north; separately, take the north step first and then the east step. On a flat table both routes deliver the arrow pointing the same way at the far corner. On the globe the two arrows disagree by a small twist, and the twist gets bigger when the patch is bigger or the surface is more strongly curved. The Ricci identity is the precise version of this: the disagreement between the two orders of differentiating is controlled only by the curvature at that spot and by the arrow you carried, and not at all by how the arrows happen to vary nearby. What is simplified here: the identity is about derivatives, so it describes the limit of vanishingly small steps; real finite loops need the effect added up, and the east-north picture works cleanly only when the two step directions form a closed little patch, as coordinate directions do.

**Picture to hold:** Two routes around a tiny patch of a globe, east-then-north and north-then-east, handing over arrows that differ by a small twist.

**Assumes:** [[parallel-transport]], [[curvature]]

### Working

For the torsion-free (Levi-Civita) connection, [∇_μ, ∇_ν] V^ρ = ∇_μ ∇_ν V^ρ - ∇_ν ∇_μ V^ρ = R^ρ_σμν V^σ. Read the slots as jobs: μ and ν are the two differentiation directions (the plane of an infinitesimal loop), σ receives the vector, and ρ labels the output component. Three facts carry the physics. First, no derivatives of V survive on the right, so the result is linear in the value of V at the point: that is why R is a tensor. Second, on a covector the sign flips, [∇_μ, ∇_ν] ω_ρ = -R^σ_ρμνω_σ, and on a scalar the commutator is zero. The minus sign is forced: ω_ρ V^ρ is a scalar, so the two curvature terms produced by the product rule must cancel. A tensor with several indices gets one such term per index. Third, the fastest derivation uses a local inertial frame at P, where Γ = 0 but its derivatives do not vanish: ∇_μ ∇_ν V^ρ reduces to the second partial of V plus (∂_μ Γ^ρ_νσ) V^σ. Swapping μ and ν and subtracting kills the symmetric second partials and leaves ∂_μ Γ^ρ_νσ - ∂_ν Γ^ρ_μσ, which is exactly the Riemann tensor at P because the Γ-Γ terms vanish there. Both sides are tensors, so the equation holds in every coordinate system. Contracting ρ with μ gives the form used for focusing of geodesics: ∇_μ ∇_ν V^μ - ∇_ν ∇_μ V^μ = R_σν V^σ.

**Picture to hold:** A two-by-two ledger: the mixed partial derivatives cancel, the connection-times-derivative terms cancel in pairs, and only a curvature-times-vector term is left standing.

**Assumes:** [[second-covariant-derivative]], [[riemann-curvature-tensor]], [[local-inertial-frame]], [[covariance-of-tensor-equations]]

### Formal

Let ∇ be an affine connection on a manifold M. Its curvature operator acts on vector fields X, Y, Z by R(X,Y)Z = ∇_X ∇_Y Z - ∇_Y ∇_X Z - ∇_[X,Y] Z, which is C-infinity linear in all three arguments and has components (R(X,Y)Z)^ρ = R^ρ_σμν Z^σ X^μ Y^ν, with the course convention R^ρ_σμν = ∂_μ Γ^ρ_νσ - ∂_ν Γ^ρ_μσ + Γ^ρ_μλ Γ^λ_νσ - Γ^ρ_νλ Γ^λ_μσ. Write ∇_μ ∇_ν Z^ρ for the components of the (1,2) tensor ∇(∇ Z), the rightmost derivative acting first. Then [∇_μ, ∇_ν] Z^ρ = R^ρ_σμν Z^σ - T^λ_μν ∇_λ Z^ρ, with torsion T^λ_μν = Γ^λ_μν - Γ^λ_νμ in the course index order (derivative index first on Γ). For the Levi-Civita connection T = 0. On a general tensor, [∇_μ, ∇_ν] acts as a derivation: each contravariant index α contributes + R^α_λμν with λ put in that slot, each covariant index β contributes - R^λ_βμν with λ put in that slot, and on scalars [∇_μ, ∇_ν] f = -T^λ_μν ∂_λ f. The operator form and the component form differ by bookkeeping only: ∇_X(∇_Y Z) = X^μ Y^ν ∇_μ ∇_ν Z + ∇_(∇_X Y) Z, and with zero torsion ∇_X Y - ∇_Y X = [X,Y], so the bracket term in R(X,Y)Z exactly removes the derivatives of X and Y. Consequences: for a torsion-free connection all second covariant derivatives of all tensors commute if and only if R = 0; a field with ∇ V = 0 must satisfy R^ρ_σμν V^σ = 0 (integrability condition); applied to a gradient, the identity yields the cyclic identity R^ρ_[σμν] = 0; and the Jacobi identity for commutators of covariant derivatives yields the differential Bianchi identity.

**Picture to hold:** The curvature operator R(X,Y) as an infinitesimal linear transformation of the tangent space attached to the plane spanned by X and Y.

**Assumes:** [[riemann-curvature-operator]], [[lie-bracket]], [[torsion-tensor]], [[covariant-derivative-of-a-tensor]]

## Prerequisites

- [[riemann-curvature-tensor]] — The identity says the commutator equals this tensor acting on the vector, so the component definition and index roles must already be known.
- [[second-covariant-derivative]] — The objects being compared are second covariant derivatives, including the correction for the derivative index and the order convention.
- [[torsion-free-connection]] — The clean form with no extra derivative term needs a symmetric connection; torsion adds a term proportional to ∇ V.

## Leads to

- [[geodesic-deviation-equation]] — Tidal acceleration follows in a few lines by swapping derivative order along a family of geodesics.
- [[raychaudhuri-equation]] — Reordering the derivatives in the rate of change of the expansion is where the Ricci term that drives focusing enters.
- [[null-raychaudhuri-equation]] — The same reordering along a null congruence gives the propagation equations for light-beam expansion and twist.
- [[integrability-condition-for-parallel-fields]] — A covariantly constant field must be annihilated by the curvature, which is the identity with the left side set to zero.
- [[gauss-codazzi-equations]] — Applying the identity on a hypersurface and in spacetime and comparing the two gives the Gauss and Codazzi relations.
- [[killing-vector-ricci-identity]] — Combined with Killing's equation it fixes second derivatives of a symmetry generator in terms of curvature.

## Related

- [[riemann-curvature-operator]] — Equivalent index-free statement, with the Lie-bracket correction needed for non-coordinate vector fields.
- [[holonomy]] — The finite-loop version: integrating the commutator around a small loop gives the rotation of a transported vector.
- [[lie-bracket]] — Explains why a bracket term must be subtracted when the two differentiation directions come from non-commuting fields.
- [[torsion-tensor]] — Supplies the extra term in the commutator for connections that are not symmetric.
- [[gauge-field-strength]] — The same construction in gauge theory: commuting gauge-covariant derivatives yields the field strength.
- [[cyclic-identity]] — Follows by applying the torsion-free identity to the gradient of a scalar.
- [[bianchi-identity]] — Follows from the Jacobi identity for commutators of covariant derivatives.

## Key equations

### Ricci identity for a vector

$$
[\nabla_\mu,\nabla_\nu]V^\rho \equiv \nabla_\mu\nabla_\nu V^\rho-\nabla_\nu\nabla_\mu V^\rho = R^\rho{}_{\sigma\mu\nu}\,V^\sigma
$$

Swapping the order of two covariant derivatives on a vector costs exactly the Riemann tensor contracted with that vector; the last two slots of R are the two derivative directions. Valid for zero torsion. *(SCH ch06 §6.5 p.160; GA ch35 §35.1 p.366; DIV ch06 §6.5 p.94; legacy:manuscript-section-8-1-8-3-riemann-commutator-and-loop)*

**Convention:** Identical in all three books and the legacy course once written with the rightmost ∇ acting first.

### Ricci identity for a covector

$$
[\nabla_\mu,\nabla_\nu]\omega_\rho = -R^\sigma{}_{\rho\mu\nu}\,\omega_\sigma
$$

A lower index picks up a curvature term of the opposite sign, which keeps the commutator of the scalar ω_ρ V^ρ equal to zero. *(SCH ch06 §6.5 p.160; legacy:manuscript-section-8-1-8-3-riemann-commutator-and-loop)*

**Convention:** Schutz writes lower-index terms with a plus sign using R_ρ^σ_μν, which equals -R^σ_ρμν by first-pair antisymmetry.

### Ricci identity for a mixed tensor

$$
[\nabla_\mu,\nabla_\nu]F^\alpha{}_\beta = R^\alpha{}_{\lambda\mu\nu}F^\lambda{}_\beta - R^\lambda{}_{\beta\mu\nu}F^\alpha{}_\lambda,\qquad [\nabla_\mu,\nabla_\nu]f=0
$$

One curvature term per index, plus for upper and minus for lower; a scalar function is unaffected when torsion vanishes. *(SCH ch06 §6.5 p.160; DIV ch06 Exercise 6.10 p.109)*

**Convention:** Schutz eq. 6.78 writes both terms with plus signs, placing the metric-shifted index first on R in the second term.

### Commutator with torsion

$$
[\nabla_\mu,\nabla_\nu]V^\rho = R^\rho{}_{\sigma\mu\nu}V^\sigma - T^\lambda{}_{\mu\nu}\nabla_\lambda V^\rho,\qquad T^\lambda{}_{\mu\nu}=\Gamma^\lambda{}_{\mu\nu}-\Gamma^\lambda{}_{\nu\mu}
$$

For a non-symmetric connection a derivative term survives; it disappears for the Levi-Civita connection used in general relativity. *(DIV ch06 §6.5 p.94)*

**Convention:** d'Inverno writes the extra term as (Γ^e_cd - Γ^e_dc) ∇_e X^a with the derivative index last on Γ; translated to the course order (derivative index first) it becomes the minus-torsion term shown.

### Index-free curvature operator

$$
R(X,Y)Z=\nabla_X\nabla_Y Z-\nabla_Y\nabla_X Z-\nabla_{[X,Y]}Z,\qquad \big(R(X,Y)Z\big)^\rho=R^\rho{}_{\sigma\mu\nu}Z^\sigma X^\mu Y^\nu
$$

Along arbitrary vector fields the bracket term removes the part of the mismatch caused by the fields themselves not closing into a loop; in a coordinate basis the bracket vanishes. *(GA ch35 §35.1 p.366; DIV ch10 §10.3 p.174; DIV ch06 Exercise 6.11 p.109)*

### Contracted Ricci identity

$$
\nabla_\mu\nabla_\nu V^\mu-\nabla_\nu\nabla_\mu V^\mu = R_{\sigma\nu}V^\sigma
$$

Exchanging a divergence and a gradient on a vector produces the Ricci tensor; this is the step that brings Ricci curvature into the Raychaudhuri equation. *(GA ch50 §50.2 p.549; GA ch35 Exercise 35.2 p.372)*

**Convention:** Uses the course contraction R_σν = R^μ_σμν, which all three books share.

## Conventions across the books

| Issue | Schutz | Gifted Amateur | d'Inverno | Course choice |
| --- | --- | --- | --- | --- |
| Sign and slot order of the Riemann tensor in the commutator | R^α_βμν = Γ^α_βν,μ - Γ^α_βμ,ν + ...; [∇_α, ∇_β] V^μ = R^μ_ναβ V^ν (MTW ordering). | Same MTW ordering: [∇_μ, ∇_ν] c^α = R^α_βμν c^β (eqn 35.13); slot 2 takes the vector, slots 3-4 the directions. | R^a_bcd = ∂_c Γ^a_bd - ∂_d Γ^a_bc + ...; ∇_c ∇_d X^a - ∇_d ∇_c X^a = R^a_bcd X^b, the same index convention as MTW. | R^ρ_σμν = ∂_μ Γ^ρ_νσ - ∂_ν Γ^ρ_μσ + Γ Γ terms, so [∇_μ, ∇_ν] V^ρ = +R^ρ_σμν V^σ. No sign translation is needed from any of the three books. |
| Order of indices when repeated covariant derivatives are written with semicolons | Prefers operator notation, writing ∇_α ∇_β V^μ = ∇_α(V^μ_;β), so the outer derivative is written on the left. | c^α_;νμ means (c^α_;ν)_;μ, the components of ∇_μ ∇_ν c; the commutator is therefore written c^α_;νμ - c^α_;μν. The dossier flags this reversal as essential for the sign. | Same semicolon rule: in ch23 l^a_;bc - l^a_;cb = R^a_dcb l^d, where the last index is the outer derivative, consistent with the ch06 commutator. | Write ∇_μ ∇_ν V^ρ with the rightmost ∇ acting first. If semicolons appear, V^ρ_;νμ means ∇_μ ∇_ν V^ρ, and the tutor says so explicitly before any sign is compared. |
| Sign attached to lower indices in commutators of higher-rank tensors | Eq. 6.78 gives every index a plus sign by writing the covariant-index term with R_ν^σ_αβ (index shifted with the metric); this equals -R^σ_ναβ. | States only the vector case and its contraction; no general-rank rule is displayed. | Exercise 6.10 gives the (1,1) case with a minus sign in front of R^e_bcd for the lower index. | Use standard placement R^λ_βμν and a minus sign for each lower index; mention Schutz's all-plus form only as an equivalent rewriting. |
| Torsion term and the index order of Christoffel symbols | Derivative index last on Γ; assumes a symmetric connection throughout, so no torsion term appears. | ∇_μ e_ν = Γ^α_μν e_α (derivative index first); torsion-free assumed, with the Lie-bracket correction discussed for non-coordinate fields. | Derivative index last; keeps the torsion term (Γ^e_cd - Γ^e_dc) ∇_e X^a in eq. 6.39 before restricting to symmetric connections. | Derivative index first, ∇_μ V^ν = ∂_μ V^ν + Γ^ν_μλ V^λ; with torsion the commutator carries -T^λ_μν ∇_λ V^ρ, and for general relativity T = 0. |
| Name and normalization | Called the commutator of covariant derivatives; the name Ricci identity is not used. | Called the Ricci identity in ch50; the operator form is the Riemann curvature operator in ch35. | Also writes ∇_[c ∇_d] X^a = (1/2) R^a_bcd X^b, where square brackets antisymmetrize with a factor one half; the name Ricci identity appears in ch23. | Call it the Ricci identity and write the commutator explicitly (no factor one half); if bracket notation is used, state its normalization. |
| Metric signature | (-,+,+,+). | (-,+,+,+). | (+,-,-,-). | (-,+,+,+). The identity with R^ρ_σμν and the contracted form with R_σν do not change under an overall sign flip of the metric, so no translation is needed here. |

## How the sources teach it

### schutz

**Route:** Right after defining Riemann by parallel transport around a small coordinate loop, asks what happens when two covariant derivatives are applied in the two orders. Evaluates at a point in a local inertial frame (Γ = 0, derivatives nonzero), swaps and subtracts, recognizes the Riemann definition, promotes the tensor equation to all coordinates, states the (1,1) rule, and ties the result back to the loop.

**Representation:** Component calculus in a special frame; quantum-mechanics commutator notation; verbal link to loop transport.

**Strengths:** Very short and consistent with the book's recurring move of computing in a local inertial frame and promoting tensor equations. Explicitly stresses that second covariant derivatives are not symmetric even though partials are.

**Weaknesses:** The frame shortcut hides the cancellations of the connection-times-derivative terms, which learners most need to see. Does not use the name Ricci identity, silently assumes zero torsion, gives no non-coordinate (Lie bracket) version, and the all-plus lower-index form invites sign errors. *(SCH ch06 §6.5 p.159; SCH ch06 §6.5 p.160; SCH ch06 Exercise 6.20 p.167; SCH ch06 Exercise 6.21 p.167)*

### gifted-amateur

**Route:** Rewrites geodesic deviation with covariant derivatives and finds a commutator [∇_n, ∇_u] u; notes that arbitrary edge vectors need not close a loop, introduces the Lie-bracket correction and the Riemann curvature operator, quotes the component identity with proof left to Exercise 35.2. Ch44 compares it with the gauge field strength; ch50 uses it to derive the Raychaudhuri equation.

**Representation:** Index-free operators and slot notation, a loop figure, a gauge-theory comparison table, and component equations with semicolons.

**Strengths:** Physically motivated by tides; explains the bracket term geometrically; the gauge analogy shows curvature as a field strength; the ch50 application demonstrates why reordering derivatives matters.

**Weaknesses:** The component identity is asserted in the text rather than derived. The semicolon order runs opposite to the operator order, and ∇_μ is used both as a directional operator and for components, which can confuse. No general-rank rule is given. *(GA ch35 §35.1 p.366; GA ch35 Exercise 35.2 p.372; GA ch44 §44.2 p.482; GA ch50 §50.2 p.549; GA ch50 Example 50.1)*

### dinverno

**Route:** Opens the Riemann section with the remark that covariant differentiation need not commute, expands the commutator on a vector for a general connection, isolates a curvature piece and a torsion piece, and defines the Riemann tensor as the coefficient (tensorial because the left side is a tensor and X is arbitrary). Exercises give the (1,1) and index-free forms; later chapters use it for geodesic deviation, the Gauss equation and optical scalars.

**Representation:** Full component algebra with an explicit torsion term, starred equalities for coordinate-specific statements, abstract index-free vector fields in exercises.

**Strengths:** The most complete derivation: all terms are visible and the torsion assumption is explicit. Defining Riemann from the commutator makes its tensor character immediate, and repeated later use shows the identity's power.

**Weaknesses:** No picture or physical motivation when introduced; the link to holonomy comes separately in §6.7. The one-half normalization of antisymmetrization brackets and the derivative-last Γ order need translation. *(DIV ch06 §6.5 p.94; DIV ch06 §6.5 p.95; DIV ch06 Exercise 6.11 p.109; DIV ch10 §10.3 p.174; DIV ch14 §14.5 p.245; DIV ch23 §23.9 p.475)*

### legacy

**Route:** After a two-route transport lab, §8.1 contrasts commuting mixed partials of a scalar with vectors, boxes the commutator definition in course conventions, expands ∇_μ ∇_ν V^ρ including the often-forgotten correction for the derivative index, and states which terms cancel; §8.2 gives the index-free form with the bracket and the covector sign; §8.3 connects to loop holonomy with explicit orientation.

**Representation:** Course-convention components with named index roles, index-free operator, loop orientation discussion.

**Strengths:** Matches the course conventions exactly, names each index's job, flags the forgotten correction term, and argues tensoriality from the absence of derivatives of V. Unusually honest about orientation signs.

**Weaknesses:** The cancellations are asserted rather than displayed, the small-loop formula is stated rather than derived, and there is no general-rank table. *(legacy:manuscript-section-8-1-8-3-riemann-commutator-and-loop; legacy:manuscript-chapter-08-curvature-holonomy)*

## Recommended teaching path

1. **Ask whether derivative order matters** — Start from the familiar fact that mixed partial derivatives of a smooth function commute. Ask the learner to predict whether the same holds for covariant derivatives, test it on a scalar (it does, with zero torsion), then pose the question for a vector field on a sphere. *Why:* Creates a concrete expectation to be broken, and separates the harmless scalar case from the interesting vector case. *(SCH ch06 §6.5 p.159; DIV ch06 §6.5 p.94; legacy:manuscript-section-8-1-8-3-riemann-commutator-and-loop)*
2. **Show the two orders on a curved surface** — Run the two-orders demo on a sphere: transport a vector a small step along θ then φ, and along φ then θ, and display the gap at the shared corner. Shrink the step and show the gap divided by the step squared settling to a curvature-times-vector value, while a flat plane gives zero. *Why:* Gives the identity a visible meaning before any algebra and ties it to the loop definition of curvature the learner already has. *(SCH ch06 §6.5 p.160; GA ch35 §35.3 p.368; legacy:manuscript-chapter-08-curvature-holonomy)*
3. **Derive it quickly in a local inertial frame** — At P choose coordinates with Γ(P) = 0. Write ∇_μ ∇_ν V^ρ there, swap, subtract, and match the surviving derivative-of-Γ terms to the Riemann definition. Then promote: both sides are tensors. *Why:* The shortest correct derivation, and it reinforces the promotion principle that recurs throughout the course. *(SCH ch06 §6.5 p.159; GA ch11 Example 11.5)*
4. **Open the full ledger** — In general coordinates expand both orders term by term, including the correction for the derivative index. Let the learner cross off cancelling pairs: symmetric second partials, the connection-times-first-derivative pairs, and the derivative-index correction (zero by symmetry of Γ, or a torsion term otherwise). *Why:* Shows that no derivatives of V survive, which is the real reason curvature is a tensor, and exposes exactly where torsion would enter. *(DIV ch06 §6.5 p.94; legacy:manuscript-section-8-1-8-3-riemann-commutator-and-loop)*
5. **Extend to all tensors and to arbitrary directions** — Derive the covector sign from the scalar ω_ρ V^ρ, state the one-term-per-index rule, then move to vector fields X and Y that do not commute and show why ∇_[X,Y] must be subtracted. *Why:* Prevents the two most common sign and bracket errors and prepares the operator language used in later chapters. *(SCH ch06 §6.5 p.160; GA ch35 §35.1 p.366; DIV ch06 Exercise 6.11 p.109)*
6. **Check with numbers** — On the unit sphere use R^θ_φθφ = sin^2 θ and R^φ_θθφ = -1 to predict the commutator on the basis vectors, and compare with the demo's measured gaps. Contract the identity to get the Ricci form. *Why:* A quantitative check fixes the sign convention in memory and connects the identity to the Ricci tensor. *(legacy:manuscript-section-8-4-8-6-flatness-count-sphere-curvature; GA ch35 Exercise 35.2 p.372)*
7. **Use it** — Derive geodesic deviation from [u, ξ] = 0 and the identity, then preview focusing (Raychaudhuri) and the gauge-theory field strength as the same idea in other settings. *Why:* Learners remember the identity as the engine behind tides and focusing rather than as an isolated formula. *(DIV ch10 §10.3 p.174; GA ch50 Example 50.1; GA ch44 §44.2 p.482)*

## Analogies

- **Turning a book about two axes in different orders** (intuition): Rotate a book a quarter turn about a horizontal axis and then about a vertical axis, then repeat in the other order: it ends up facing differently. For very small turns the difference is second order, proportional to the product of the two angles, just as the curvature term appears at second order in the two step sizes. *Limits:* The book lives in flat space; its order-dependence comes from the structure of rotations, not from curvature. The commutator in the Ricci identity vanishes completely in flat space, and it acts on the carried vector, not on the directions of motion.
- **Two orders of stepping around a tiny patch** (intuition): Changing a vector field first along one direction and then another, and subtracting the opposite order, is the infinitesimal version of carrying the vector around the edges of a small loop. *Limits:* Only exact in the limit of a vanishing loop; for loops built from non-commuting directions a Lie-bracket gap must be closed first, and the sign depends on which order is subtracted from which. *(SCH ch06 §6.5 p.160; GA ch35 §35.3 p.368)*
- **Field strength in electromagnetism** (working): For a charged field the gauge-covariant derivatives D_μ fail to commute by i q F_μν. In gravity the covariant derivatives fail to commute by the Riemann tensor, so Riemann plays the role of the field strength of the spacetime connection. *Limits:* The electromagnetic field strength acts by multiplication by a number, while Riemann acts as a matrix on vectors. The gravitational connection is tied to the metric and to spacetime directions, which gives Riemann extra symmetries (pair exchange, cyclic identity) with no electromagnetic counterpart. *(GA ch44 §44.2 p.482)*
- **Commutator brackets from quantum mechanics** (working): The bracket notation borrowed from quantum mechanics is a reminder that the order of two operations matters. *Limits:* The resemblance is only notational: nothing here is about uncertainty or measurement, and the commutator of covariant derivatives vanishes entirely in flat space. *(SCH ch06 §6.5 p.159)*

## Misconceptions

- **Covariant derivatives commute just like partial derivatives.** — Second covariant derivatives of a vector differ by R^ρ_σμν V^σ. They commute on all tensors only when the Riemann tensor (and the torsion) vanish. *Why tempting:* Mixed partials commute, and ∇ looks like a partial derivative plus a correction that can even be made zero at a point. *Diagnostic:* On a unit sphere, is ∇_θ ∇_φ V^θ equal to ∇_φ ∇_θ V^θ for the field with components (V^θ, V^φ) = (0, 1)? If not, by how much do they differ? *(SCH ch06 §6.5 p.159; DIV ch06 §6.5 p.94)*
- **Because Γ = 0 at P in a local inertial frame, second covariant derivatives at P equal second partial derivatives and the commutator must vanish there.** — ∇_μ(∇_ν V^ρ) contains the derivative of Γ, which does not vanish at P. That derivative is exactly what survives the commutator and becomes curvature. *Why tempting:* First covariant derivatives do reduce to partials at P, and it is natural to assume the same for the second step. *Diagnostic:* At the origin of normal coordinates on a sphere all Christoffel symbols are zero. Which quantity in ∇_1 ∇_2 V^1 is still nonzero there, and why? *(SCH ch06 §6.5 p.159; legacy:manuscript-section-8-1-8-3-riemann-commutator-and-loop)*
- **Every index of a tensor gets the same plus-sign curvature term, including lower indices written in the usual placement.** — With R^λ_βμν in standard placement a lower index needs a minus sign. Schutz's all-plus form is equivalent only because the index shifted with the metric sits first on R, which introduces a hidden minus sign. *Why tempting:* Schutz's eq. 6.78 displays plus signs for both indices, and upper and lower indices look symmetric on the page. *Diagnostic:* Apply [∇_μ, ∇_ν] to the scalar ω_ρ V^ρ using the product rule. What must the covector term be for the result to vanish? *(SCH ch06 §6.5 p.160; legacy:manuscript-section-8-1-8-3-riemann-commutator-and-loop)*
- **For any two vector fields X and Y, ∇_X ∇_Y Z - ∇_Y ∇_X Z is the curvature acting on Z, so a nonzero result proves the space is curved.** — When [X,Y] is not zero the term ∇_[X,Y] Z must be subtracted before the remainder is curvature; with torsion a further derivative term appears. Only the torsion-free component commutator, or the bracket-corrected operator, measures curvature. *Why tempting:* In coordinate bases the bracket vanishes, so the correction is easy to forget when switching to orthonormal or other non-coordinate frames. *Diagnostic:* In the flat plane take X = e_r and Y = e_θ-hat = (1/r) ∂_θ. Compute ∇_X ∇_Y e_r - ∇_Y ∇_X e_r. Is it zero? What does the bracket term do? *(GA ch35 §35.1 p.366; DIV ch06 Exercise 6.11 p.109; legacy:manuscript-section-8-1-8-3-riemann-commutator-and-loop)*
- **The commutator depends on how the vector field varies around the point, not just on its value there.** — All terms containing derivatives of V cancel, so the commutator at P depends only on V(P) and the curvature at P. This is what makes the Riemann tensor a tensor. *Why tempting:* The left side is built from second derivatives of the field, so it seems it should know about the field's shape nearby. *Diagnostic:* Two vector fields agree at P but differ everywhere else. Do their commutators [∇_μ, ∇_ν] V^ρ agree at P? *(DIV ch06 §6.5 p.95; legacy:manuscript-section-8-1-8-3-riemann-commutator-and-loop)*

## Thought experiments

- **Two surveyors from one corner**: Two surveyors start at the same corner of a tiny patch with identical gyroscope-stabilized arrows. One walks a short leg along one coordinate line and then along the other; the second walks the legs in the opposite order. They meet at the far corner and compare arrows. *Lesson:* On a flat plane the arrows agree. On a curved surface they differ by an amount proportional to the product of the leg lengths and to the curvature contracted with the arrow, which is the finite-step shadow of the Ricci identity. *(SCH ch06 §6.5 p.160)*

## Visualizations

### Two orders on a sphere · interactive-3d · high priority

Make the commutator visible as a gap between two transported arrows that reach the same corner by different routes, and show that the gap per unit patch area converges to the Riemann tensor acting on the arrow.

**Interaction:** The learner drags a base point on a sphere, sets the initial vector, picks the two step directions (θ and φ, or arbitrary coordinate directions) and a step size with a slider. Both routes animate; the gap vector appears at the corner with a readout of gap divided by step squared beside the predicted value. Toggles switch the surface to a flat plane (gap goes to zero) and reverse which route is subtracted (sign flips).

**Model:** Levi-Civita transport on the unit sphere, dV^ρ/dlambda = -Γ^ρ_μσ (dx^μ/dlambda) V^σ with Γ^θ_φφ = -sin θ cos θ and Γ^φ_θφ = cot θ, integrated by RK4. For coordinate steps a along direction μ then b along ν, (route μ-first minus route ν-first) = -R^ρ_σμν V^σ a b + O(step^3); with R^θ_φθφ = sin^2 θ and R^φ_θθφ = -1 (checked numerically at θ = 1 with steps 0.01-0.02).

**Inspired by:** SCH ch06 §6.5 p.160; GA ch35 §35.3 p.368; legacy:manuscript-chapter-08-curvature-holonomy

**Legacy assets:** manuscript-chapter-08-curvature-holonomy, manuscript-section-8-1-8-3-riemann-commutator-and-loop

### Commutator ledger · interactive-2d · medium priority

A term-by-term expansion of ∇_μ ∇_ν V^ρ and ∇_ν ∇_μ V^ρ in general coordinates, where the learner cancels matching terms and watches the Riemann tensor assemble from what remains.

**Interaction:** Terms are tiles; clicking two tiles that cancel removes both with a short reason (mixed partials commute, pair of Γ times dV terms, symmetry of Γ). A torsion switch keeps the derivative-index correction alive as a torsion term. A rank selector adds a lower or second upper index and shows the extra curvature term with its sign.

**Model:** Symbolic algebra in course conventions: ∇_μ V^ν = ∂_μ V^ν + Γ^ν_μλ V^λ, Riemann as in course-conventions.md, torsion T^λ_μν = Γ^λ_μν - Γ^λ_νμ.

**Inspired by:** DIV ch06 §6.5 p.94; legacy:manuscript-section-8-1-8-3-riemann-commutator-and-loop

**Legacy assets:** manuscript-section-8-1-8-3-riemann-commutator-and-loop

### From commutator to tides · animated-2d · medium priority

Animate the four-line derivation of geodesic deviation on a family of great circles leaving the equator, highlighting the moment the Ricci identity swaps derivative order and produces the curvature term that pulls the geodesics together.

**Interaction:** The learner scrubs along the geodesics; each derivation line lights up with the corresponding geometric object (u, ξ, ∇_u ξ = ∇_ξ u, the swapped second derivative) and the deviation acceleration arrow grows as predicted.

**Model:** Meridians leaving the equator of a unit sphere parallel to each other, with separation ξ proportional to cos s in arc length s from the equator; D^2 ξ / ds^2 = -K ξ with K = 1, obtained from [u, ξ] = 0 and the Ricci identity.

**Inspired by:** DIV ch10 §10.3 p.174; GA ch35 §35.1 p.366

**Legacy assets:** manuscript-chapter-10-tides-geodesic-deviation

### Field strength side by side · static-2d · low priority

A two-column comparison: the gauge covariant derivative and its commutator giving the Faraday tensor, next to the Levi-Civita covariant derivative and its commutator giving Riemann.

**Interaction:** Hovering a symbol in one column highlights its counterpart in the other; a note appears where the analogy breaks (matrix action on vectors, extra symmetries of Riemann).

**Inspired by:** GA ch44 §44.2 p.482

## Worked examples

- **Commutator in a local inertial frame** (working): The quickest route: with Γ zero at P only derivative-of-Γ terms survive, they match the Riemann definition, and the tensor equation is then promoted to all coordinates. *(SCH ch06 §6.5 p.159)*
- **Full commutator for a general connection** (working): Every term of both orderings written out; first-derivative terms cancel, leaving a curvature piece linear in X and a torsion piece proportional to its covariant derivative. *(DIV ch06 §6.5 p.94)*
- **Expansion with the derivative-index correction** (working): Course-convention expansion that flags the easily forgotten correction for the index of the first derivative and states which groups cancel. *(legacy:manuscript-section-8-1-8-3-riemann-commutator-and-loop)*
- **Geodesic deviation from the commutator** (working): A geodesic-ruled 2-surface gives [V, ξ] = 0; differentiating along V and swapping derivative order with the identity produces the Riemann term of the deviation equation. *(DIV ch10 §10.3 p.174)*
- **Rate of change of convergence of a congruence** (formal): Writing the derivative of the convergence as a double covariant derivative and reordering with the contracted identity brings in the Ricci tensor that controls focusing. *(GA ch50 Example 50.1)*
- **Gauss equation for a hypersurface** (formal): The identity for the induced derivative on a slice, expanded with projectors, relates intrinsic 3-curvature to spacetime curvature plus extrinsic-curvature products. *(DIV ch14 §14.5 p.245)*
- **Propagation of expansion and twist of a null congruence** (formal): The identity applied to the null tangent and contracted gives an evolution equation in which positive Ricci curvature focuses light beams. *(DIV ch23 §23.9 p.475)*

## Exercises

- (intro) Fill in the algebra behind the second covariant derivative at the origin of a local inertial frame. *Skill:* Expanding a second covariant derivative and dropping terms that vanish at a point *(SCH ch06 Exercise 6.20 p.167)*
- (standard) Explain why the sign argument for curvature terms does not carry over to the signs of Christoffel terms in first covariant derivatives. *Skill:* Distinguishing tensorial curvature terms from non-tensorial connection terms *(SCH ch06 Exercise 6.21 p.167)*
- (standard) Prove the component commutator identity in a coordinate frame and contract it to relate a swapped divergence and gradient to the Ricci tensor. *Skill:* Second covariant derivatives and index contraction *(GA ch35 Exercise 35.2 p.372)*
- (standard) Show that promoting a flat-space vector wave equation by replacing partial with covariant derivatives is ambiguous, and relate the two versions through a Ricci term. *Skill:* Minimal coupling and the commutator identity *(GA ch35 Exercise 35.3 p.372)*
- (standard) Derive the commutator of covariant derivatives on a mixed (1,1) tensor. *Skill:* One curvature term per index with correct signs *(DIV ch06 Exercise 6.10 p.109)*
- (challenging) Show that the bracket-corrected commutator along vector fields equals the Riemann tensor contracted with the three fields. *Skill:* Index-free curvature operator and the Lie bracket *(DIV ch06 Exercise 6.11 p.109)*
- (standard) Find the condition for a globally parallel vector field from equality of mixed partial derivatives and rewrite it with the Riemann tensor. *Skill:* Integrability conditions *(SCH ch06 Exercise 6.11 p.166)*
- (standard) Write the commutator on a covector and combine it with Killing's equation to obtain a contracted identity involving the Ricci tensor. *Skill:* Ricci identity with Killing vectors *(DIV ch07 Exercise 7.14)*
- (challenging) Derive the tensor form of the Raychaudhuri equation for the velocity-gradient tensor of a congruence. *Skill:* Reordering derivatives along a congruence *(GA ch50 Exercise 50.2(c))*
- (challenging) Read a set of Penrose tensor diagrams, including one that encodes a curvature identity for derivatives, and translate each back into index notation. *Skill:* Recognizing the commutator identity in diagrammatic form *(GA ch31 Ex 31.7)*

## Checks for understanding

- **Q (intuition):** On a flat sheet, does it ever matter in which order you take two covariant derivatives of an arrow field? On a sphere it does; if you halve both step sizes, what happens to the mismatch, and what stays fixed?
  - **A:** On a flat sheet the Riemann tensor is zero, so the order never matters for any field. On a sphere the mismatch shrinks like the product of the two step sizes, so halving both cuts it by a factor of four; the mismatch divided by the patch area stays fixed and equals the curvature acting on the arrow.
- **Q (working):** Starting from [∇_μ, ∇_ν] V^ρ = R^ρ_σμν V^σ and the fact that the commutator annihilates scalars, derive the rule for a covector ω_ρ.
  - **A:** The scalar f = ω_ρ V^ρ has [∇_μ, ∇_ν] f = 0. By the product rule (first derivatives cancel in the commutator) this equals ([∇_μ, ∇_ν] ω_ρ) V^ρ + ω_ρ R^ρ_σμν V^σ. Relabel the second term as ω_σ R^σ_ρμν V^ρ. Since V is arbitrary, [∇_μ, ∇_ν] ω_ρ = -R^σ_ρμνω_σ. *(targets: Every index of a tensor gets the same plus-sign curvature term, including lower indices written in the usual placement.)*
- **Q (working):** At the origin of Riemann normal coordinates on a unit sphere, the metric is the identity, all Christoffel symbols vanish, and R_1212 = 1. For a vector field with V = (0, 1) at the origin, compute [∇_1, ∇_2] V^1 there.
  - **A:** [∇_1, ∇_2] V^1 = R^1_σ 12 V^σ = R^1_2 12 V^2. With the metric equal to the identity at the origin, R^1_212 = R_1212 = 1, so the commutator is 1, not zero, even though every Christoffel symbol vanishes at that point. *(targets: Because Γ = 0 at P in a local inertial frame, second covariant derivatives at P equal second partial derivatives and the commutator must vanish there.)*
- **Q (formal):** In the flat plane with X = e_r and Y = e_θ-hat = (1/r) ∂_θ, compute ∇_X ∇_Y e_r - ∇_Y ∇_X e_r and then R(X,Y) e_r.
  - **A:** Using Γ^θ_r θ = 1/r and Γ^r_θθ = -r: ∇_Y e_r = (1/r) e_θ-hat and ∇_X e_θ-hat = 0, so ∇_X ∇_Y e_r = -(1/r^2) e_θ-hat, while ∇_X e_r = 0 gives ∇_Y ∇_X e_r = 0. The difference is -(1/r^2) e_θ-hat, which is not zero. But [X,Y] = -(1/r^2) ∂_θ = -(1/r) e_θ-hat, so ∇_[X,Y] e_r = -(1/r^2) e_θ-hat, and R(X,Y) e_r = -(1/r^2) e_θ-hat + (1/r^2) e_θ-hat = 0, as it must be in flat space. *(targets: For any two vector fields X and Y, ∇_X ∇_Y Z - ∇_Y ∇_X Z is the curvature acting on Z, so a nonzero result proves the space is curved.)*
- **Q (formal):** Apply the torsion-free Ricci identity to the gradient ω_λ = ∇_λ f and use the symmetry of ∇_μ ∇_ν f to show that R^σ_λμν + R^σ_μνλ + R^σ_νλμ = 0.
  - **A:** The identity gives ∇_μ ∇_ν ∇_λ f - ∇_ν ∇_μ ∇_λ f = -R^σ_λμν ∇_σ f. Sum this over the three cyclic orderings of (λ, μ, ν). Because ∇_ν ∇_λ f is symmetric, each third-derivative term on the left cancels against one from another ordering, so the left side sums to zero. Hence (R^σ_λμν + R^σ_μνλ + R^σ_νλμ) ∇_σ f = 0 for every f, and since gradients at a point are arbitrary the cyclic sum vanishes.

## Applications

- **Tidal acceleration**: Swapping derivative order along a family of free-fall worldlines turns the relative acceleration of neighbours into a curvature term, giving the geodesic deviation equation in course form D^2 ξ^μ/dtau^2 = -R^μ_νρσ u^νξ^ρ u^σ. *(DIV ch10 §10.3 p.174)*
- **Focusing of matter and light**: The contracted identity introduces R_μν u^μ u^ν into the evolution of the expansion of a congruence; with positive energy conditions this forces focusing, the key input to singularity theorems. *(GA ch50 Example 50.1; DIV ch23 §23.9 p.475)*
- **Minimal coupling ambiguity**: Replacing partial by covariant derivatives in a second-order flat-space equation is ambiguous because derivative order matters; different orderings differ by Ricci terms, as in the vector-potential wave equation. *(GA ch35 Exercise 35.3 p.372)*
- **Initial-value constraints**: Applied on a spatial slice and in spacetime, the identity yields the Gauss and Codazzi relations that underlie the Hamiltonian and momentum constraints of the 3+1 formulation. *(DIV ch14 §14.5 p.245)*

## History

- **Gregorio Ricci-Curbastro, Tullio Levi-Civita (1900):** Ricci built his absolute differential calculus from the late 1880s onward, and the rule for exchanging the order of covariant derivatives belongs to that work; the 1900 memoir he wrote with Levi-Civita gave the calculus its standard form. The identity is named after Ricci, not after the Ricci tensor that its contraction produces.

## Tutor guidance

**Opening questions**

- If you differentiate a smooth function first with respect to x and then y, and then in the other order, what do you get? Would you bet on the same for arrows on a globe?
- When a Christoffel symbol is zero at a point, does that tell you anything about its derivative there?
- When you carry an arrow around a small loop on a sphere, what comes back different, and what does it depend on?

**Common questions**

- *Why do no derivatives of V appear on the right-hand side?* — In the full expansion the second partials cancel because partials commute, the Γ-times-dV terms cancel in pairs, and the derivative-index correction cancels because Γ is symmetric. What is left multiplies V itself, which is why the Riemann tensor is a genuine tensor.
- *Why does a lower index come with a minus sign?* — Contract a covector with a vector to get a scalar, whose commutator is zero. The vector's plus-sign term must be cancelled by the covector's term, so the covector's curvature term has the opposite sign.
- *Is this the same Riemann tensor as the one from parallel transport around a loop?* — Yes. The loop result is the integrated version of the commutator: going round a small parallelogram with edges a then b changes a vector by -R^ρ_σμν V^σ a^μ b^ν in the course convention, and reversing the loop flips the sign.
- *Why is it named after Ricci when the Riemann tensor appears?* — It is named after Gregorio Ricci-Curbastro, who developed tensor calculus. Contracting it does produce the Ricci tensor, but the name honours the person, not that contraction.
- *Do I need the Lie-bracket term when I work in coordinates?* — No. Coordinate basis vectors commute, so the bracket vanishes and the component identity applies directly. The bracket matters for orthonormal frames and other non-coordinate fields.
- *What changes if the connection has torsion?* — An extra term -T^λ_μν ∇_λ V^ρ appears, and even scalars stop commuting. General relativity uses the torsion-free Levi-Civita connection, so it is absent.

**Pitfalls when explaining**

- Do not forget the correction for the derivative index when expanding ∇_μ(∇_ν V^ρ); without it the torsion term and several cancellations are invisible.
- Do not read a semicolon string in the same order as operator notation: V^ρ_;νμ is ∇_μ ∇_ν V^ρ.
- State the torsion-free assumption whenever writing the clean identity.
- Do not claim the frame-specific intermediate steps (with Γ = 0) hold everywhere; only the final tensor equation is promoted.
- When relating the commutator to a finite loop, say which route is subtracted from which and which way the loop is traversed; otherwise sign comparisons across books fail.
- Avoid saying the commutator of any two directional derivatives is curvature; the bracket term is required for non-commuting fields.

**When to show a demo**

- When the learner suggests that Γ = 0 at a point should make derivatives commute, run the two-orders demo and shrink the step: the scaled gap refuses to go away.
- When deriving the covector sign, open the ledger with the rank selector on a covector and let the learner watch the sign appear.
- Right before geodesic deviation, play the commutator-to-tides animation so the derivation has a picture attached.

**Saying it aloud:** Say it in words first: 'swap the order of two covariant derivatives on a vector, and the difference is the Riemann tensor fed that vector, with the two derivative directions in its last two slots.' Then the symbols: 'nabla mu nabla nu minus nabla nu nabla mu, acting on V upper rho, equals R upper rho, lower sigma mu nu, times V upper sigma.' For a covector say 'the same with a minus sign, and the covector's index sits in the second slot of R.' For the contracted form say 'swapping a divergence and a gradient on a vector gives the Ricci tensor acting on the vector.'

## Sources

- schutz ch06 (core): p.159 §6.5, p.160 §6.5
- gifted-amateur ch35 (developed): p.366 §35.1, p.372
- gifted-amateur ch44 (revisited): p.482 §44.2
- gifted-amateur ch50 (revisited): p.549 §50.2
- dinverno ch06 (core): p.94 §6.5, p.95 §6.5
- dinverno ch10 (developed): p.174 §10.3
- dinverno ch14 (revisited): p.245 §14.5, p.246 §14.6
- dinverno ch23 (revisited): p.475 §23.9
- legacy manuscript-section-8-1-8-3-riemann-commutator-and-loop (developed)

## Review

**Verdict:** fixed

**Fixes**

- Softened the history entry: the old wording credited the exchange rule specifically to the 1900 memoir. It now places the rule in Ricci's absolute calculus and treats the memoir as the standard presentation, without claiming a precise first appearance.
- Added GA ch31 Exercise 31.7 (Penrose-diagram form of the identity) to the exercises. The evidence lists it, but the note had left it out.

**Concerns**

- Independently re-checked: the torsion term (−T^λ_μν ∇_λ V^ρ with the course Γ order, matching d'Inverno eq. 6.39 once his Γ index order is converted), the covector and mixed-tensor signs, Schutz's all-plus eq. 6.78, the contracted form, the polar-frame bracket check, the cyclic-identity proof, and the sphere two-route sign by RK4 integration (route along θ first minus route along φ first, divided by ε², matched −R^ρ_σθφ V^σ to 0.2% at θ = 1). No errors found.
- The prerequisite torsion-free-connection and the leads_to ids killing-vector-ricci-identity and integrability-condition-for-parallel-fields are not in the curvature registry entry. The validator accepts them, but they should be confirmed as registry ids when those domains are finalized.
- Exercise refs GA ch31 Ex 31.7, GA ch50 Exercise 50.2(c) and DIV ch07 Exercise 7.14 have no page number. GA 50.2 was found in the reading copy (Exercises, printed pp.552-553).
