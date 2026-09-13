---
type: "concept"
id: "riemann-tensor-in-normal-coordinates"
title: "Riemann tensor in normal coordinates"
domain: "curvature"
tier: "core"
aliases: ["Riemann tensor in a local inertial frame", "metric expansion in Riemann normal coordinates", "curvature as irreducible second derivatives of the metric", "g = eta - (1/3) R x x"]
prerequisites: ["riemann-curvature-tensor", "local-flatness-theorem", "riemann-normal-coordinates", "christoffel-symbols-from-the-metric"]
leads_to: ["symmetries-of-the-riemann-tensor", "cyclic-identity", "number-of-independent-riemann-components", "bianchi-identity", "linearized-riemann-tensor"]
sources: ["gifted-amateur:ch11", "gifted-amateur:ch35", "legacy:manuscript-section-10-normal-coordinates-and-counting", "legacy:manuscript-section-8-4-8-6-flatness-count-sphere-curvature", "schutz:ch06"]
review: "fixed"
---

# Riemann tensor in normal coordinates

> Choose coordinates that make spacetime look as flat as possible at one event: the metric equals Minkowski there and its first derivatives vanish. At that event the all-lower Riemann tensor is simply half of a four-term, sign-alternating combination of second derivatives of the metric, and in Riemann normal coordinates the metric nearby reads eta minus one third of Riemann times the displacement twice. The metric's value and slope are coordinate artefacts; the twenty curvature numbers are what no choice of coordinates can remove.

## Explanations by level

### Intuition

Picture making a paper map of your neighbourhood on a round planet, centred on your front door. You can draw it so that, right at your door, distances are exactly correct, and even so that the error does not start growing as you take your first steps away. What you cannot do is keep the error away for good: a little further out the map starts to lie, and the lie grows like the square of the distance from the door. The pattern of that square-law error is the curvature. Spacetime works the same way. A freely falling laboratory removes the value and the slope of gravity at one event, which is why free fall feels weightless, but tidal stretching creeps back in quadratically, and that leftover is the Riemann tensor. What is simplified: a map of a surface has only space directions and a single curvature number, while spacetime includes time and needs twenty numbers; and the statement is about one event, not a whole region.

**Picture to hold:** Straight rays fanned out from a point on a globe: small circles drawn around the point come out slightly shorter than 2 π r, with no error at first order and a shortfall growing like r cubed.

**Assumes:** [[local-inertial-frame]], [[tidal-force]], [[curvature]]

### Working

Step 1: by the local flatness theorem, at an event P choose coordinates with g_μν(P) = η_μν and ∂_λ g_μν(P) = 0, so every Christoffel symbol vanishes at P. Step 2: in the Riemann tensor the Γ-Γ terms then drop out and only derivatives of Γ remain, R^ρ_σμν = ∂_μ Γ^ρ_νσ - ∂_ν Γ^ρ_μσ at P. Step 3: differentiate the Christoffel formula; because first derivatives of g vanish at P only second derivatives survive. Lowering the first index and using the symmetry of g and of mixed partials gives R_αβμν = (1/2)(∂_β ∂_μ g_αν - ∂_β ∂_ν g_αμ + ∂_α ∂_ν g_βμ - ∂_α ∂_μ g_βν). This holds only at P and only in such coordinates, because the right side is built from partial derivatives; in general coordinates extra terms g_ρσ(Γ^ρ_βμ Γ^σ_αν - Γ^ρ_βν Γ^σ_αμ) appear. Its value is that the index symmetries of Riemann can be read off by inspection. Step 4: Riemann normal coordinates are a specific way to achieve Step 1: shoot a geodesic from P with initial tangent X and label its point at unit affine parameter by the components X^μ. Then g_μν(x) = η_μν - (1/3) R_μανβ(P) x^α x^β + O(x^3): no linear term, and the first correction is curvature. Step 5: counting confirms the picture. In four dimensions the metric has 10 values, 40 first derivatives and 100 second derivatives at P; a coordinate change supplies 16, 40 and 80 adjustable Taylor coefficients at the matching orders. The 6 spare numbers at zeroth order are Lorentz transformations, first order is matched exactly, and 100 - 80 = 20 second derivatives are true geometry: the independent components of Riemann.

**Picture to hold:** A Taylor-coefficient ledger for the metric at P: value and slope columns fully cancelled by coordinate freedom, the curvature column left with exactly twenty entries.

**Assumes:** [[local-flatness-theorem]], [[christoffel-symbols-from-the-metric]], [[riemann-curvature-tensor]], [[riemann-normal-coordinates]], [[taylor-series]]

### Formal

Let (M, g) be a pseudo-Riemannian manifold with its Levi-Civita connection and p in M. (a) If coordinates satisfy Γ^ρ_μν(p) = 0, equivalently ∂_λ g_μν(p) = 0 by metric compatibility, then at p R_αβμν = (1/2)(g_αν,βμ - g_αμ,βν + g_βμ,αν - g_βν,αμ), with R_αβμν = g_αλ R^λ_βμν and commas denoting partial derivatives; g(p) itself need not be η. In arbitrary coordinates the exact expression adds g_ρσ(Γ^ρ_βμ Γ^σ_αν - Γ^ρ_βν Γ^σ_αμ). (b) Given an orthonormal basis e_a of T_pM, the exponential map exp_p is a diffeomorphism from a star-shaped neighbourhood of 0 in T_pM onto a normal neighbourhood U of p, and x^μ(exp_p(X^a e_a)) = X^μ defines Riemann normal coordinates. Radial curves x^μ = λ X^μ are geodesics, so Γ^ρ_μν(x) x^μ x^ν = 0 throughout U. This gives Γ(p) = 0, ∂_(α Γ^ρ_μν)(p) = 0 (symmetrized over all three lower indices), and, solving with the Riemann definition, ∂_α Γ^ρ_μν(p) = -(1/3)(R^ρ_μνα + R^ρ_νμα). Differentiating ∂_λ g_μν = g_μβ Γ^β_λν + g_νβ Γ^β_λμ once at p yields ∂_α ∂_β g_μν(p) = -(1/3)(R_μανβ + R_μβνα), hence g_μν(x) = η_μν - (1/3) R_μανβ(p) x^α x^β + O(|x|^3). (c) The normal neighbourhood is limited by the injectivity of exp_p (conjugate and cut points), and only geodesics through p are straight coordinate lines. (d) Counting: in n dimensions the metric's second derivatives at p number [n(n+1)/2]^2 and the third derivatives of a coordinate change number n * n(n+1)(n+2)/6; their difference is n^2(n^2-1)/12, which equals the number of algebraically independent Riemann components (20 for n = 4). The zeroth-order surplus n^2 - n(n+1)/2 = n(n-1)/2 is the dimension of the Lorentz (or rotation) group. Neither the four-term formula nor the expansion is a tensor equation; only statements about R itself may be promoted to other coordinates.

**Picture to hold:** The exponential map wrapping the flat tangent space onto a neighbourhood of p, exact along radial lines and distorted at second order transverse to them.

**Assumes:** [[riemann-normal-coordinates]], [[levi-civita-connection]], [[metric-compatibility]], [[conjugate-point]], [[covariance-of-tensor-equations]]

## Prerequisites

- [[riemann-curvature-tensor]] — The formula evaluates this tensor's component definition in special coordinates.
- [[local-flatness-theorem]] — Guarantees coordinates with Minkowski metric and vanishing first derivatives at the event, which kills the Γ-Γ terms.
- [[riemann-normal-coordinates]] — The metric expansion with the minus one third coefficient refers to this specific geodesic construction.
- [[christoffel-symbols-from-the-metric]] — Converting derivatives of Γ into second derivatives of the metric uses the Christoffel formula.

## Leads to

- [[symmetries-of-the-riemann-tensor]] — The four-term formula makes pair antisymmetry and pair exchange visible by inspection.
- [[cyclic-identity]] — Adding the three cyclic permutations of the four-term formula cancels every second derivative in pairs.
- [[number-of-independent-riemann-components]] — The twenty irreducible second derivatives of the metric match the twenty independent Riemann components.
- [[bianchi-identity]] — The differential Bianchi identity is most easily proved at the origin of normal coordinates.
- [[linearized-riemann-tensor]] — In weak fields the same four-term combination of second derivatives appears with the metric perturbation in place of g.

## Related

- [[local-inertial-frame]] — The physical face of the same construction: free fall removes gravity to first order, never tides.
- [[geodesic-coordinates]] — d'Inverno's quadratic coordinate change that makes Γ vanish at a point, sufficient for the four-term formula.
- [[einstein-equivalence-principle]] — The expansion states precisely how far local physics can look special-relativistic.
- [[newtonian-tidal-tensor]] — Newtonian analogue: the potential's value and gradient are removable, its second derivatives are the tides.
- [[geodesic-deviation-equation]] — An alternative derivation of the minus one third coefficient uses deviation of the radial geodesics.
- [[covariance-of-tensor-equations]] — Explains which results found in these coordinates may be promoted to all coordinates.

## Key equations

### Locally inertial coordinates at P

$$
g_{\mu\nu}(P)=\eta_{\mu\nu},\qquad \partial_\lambda g_{\mu\nu}(P)=0\ \Longrightarrow\ \Gamma^\rho{}_{\mu\nu}(P)=0
$$

The metric's value and first derivatives at one event can always be made Minkowskian; the connection then vanishes there, although its derivatives generally do not. *(SCH ch06 §6.2 p.145; GA ch11 Example 11.5; DIV ch06 §6.6 p.95)*

**Convention:** d'Inverno's geodesic coordinates impose only Γ(P) = 0, without normalizing the metric; that is enough for the curvature formula below.

### Riemann at the origin of such coordinates

$$
R^\rho{}_{\sigma\mu\nu}(P)=\partial_\mu\Gamma^\rho{}_{\nu\sigma}-\partial_\nu\Gamma^\rho{}_{\mu\sigma}
$$

With Γ zero at P the quadratic terms of the Riemann tensor vanish and only the variation of the connection is left. *(SCH ch06 §6.5 p.158)*

### Lowered Riemann as second derivatives of the metric

$$
R_{\alpha\beta\mu\nu}(P)=\tfrac12\left(\partial_\beta\partial_\mu g_{\alpha\nu}-\partial_\beta\partial_\nu g_{\alpha\mu}+\partial_\alpha\partial_\nu g_{\beta\mu}-\partial_\alpha\partial_\mu g_{\beta\nu}\right)
$$

At P, in coordinates with vanishing first metric derivatives, curvature is half a signed sum of four second derivatives; its index symmetries are visible at a glance. Not a tensor equation. *(SCH ch06 §6.5 p.158; GA ch11 §11.4 p.126; legacy:manuscript-section-8-4-8-6-flatness-count-sphere-curvature)*

**Convention:** Identical to Schutz eq. 6.68 and Gifted Amateur eqn 11.23 (MTW sign). With d'Inverno's signature (+,-,-,-) both sides change sign together, so the form is the same.

### Lowered Riemann in arbitrary coordinates

$$
R_{\alpha\beta\mu\nu}=\tfrac12\left(g_{\alpha\nu,\beta\mu}-g_{\alpha\mu,\beta\nu}+g_{\beta\mu,\alpha\nu}-g_{\beta\nu,\alpha\mu}\right)+g_{\rho\sigma}\left(\Gamma^\rho{}_{\beta\mu}\Gamma^\sigma{}_{\alpha\nu}-\Gamma^\rho{}_{\beta\nu}\Gamma^\sigma{}_{\alpha\mu}\right)
$$

The general expression; the connection-squared correction is what the special coordinates remove. Checks: it gives zero for the polar-coordinate plane (-1 from the derivatives, +1 from the Γ terms) and sin^2 θ for R_θφθφ on the unit sphere. *(GA ch11 §11.4 p.126)*

### Riemann normal coordinates

$$
x^\mu\big(\exp_P(\lambda\,u)\big)=\lambda\,u^\mu
$$

Travel an affine distance λ along the geodesic leaving P with initial tangent u (components in an orthonormal basis at P); that event gets coordinates λ u^μ. *(GA ch35 §35.2 p.367; legacy:manuscript-section-10-normal-coordinates-and-counting)*

**Convention:** Gifted Amateur writes ζ^α = λ u^α with origin O; the course writes x^μ with origin P.

### Metric expansion in normal coordinates

$$
g_{\mu\nu}(x)=\eta_{\mu\nu}-\tfrac13\,R_{\mu\alpha\nu\beta}(P)\,x^\alpha x^\beta+O(x^3)
$$

Minkowskian at P, no linear correction, and the leading departure is fixed by the curvature at P. On a unit sphere it predicts geodesic circles of circumference 2 π r (1 - r^2/6). *(GA ch35 §35.2 p.368; legacy:manuscript-section-10-normal-coordinates-and-counting)*

### Derivatives of the connection and metric at P

$$
\partial_\alpha\Gamma^\rho{}_{\mu\nu}(P)=-\tfrac13\left(R^\rho{}_{\mu\nu\alpha}+R^\rho{}_{\nu\mu\alpha}\right),\qquad \partial_\alpha\partial_\beta g_{\mu\nu}(P)=-\tfrac13\left(R_{\mu\alpha\nu\beta}+R_{\mu\beta\nu\alpha}\right)
$$

In normal coordinates every first derivative of Γ and every second derivative of the metric at P is determined by curvature; the Taylor factor one half and the two equal terms combine into the minus one third of the expansion. *(GA ch35 Exercise 35.4 p.373; legacy:manuscript-section-10-normal-coordinates-and-counting)*

**Convention:** Gifted Amateur Exercise 35.4 obtains these via geodesic deviation of the radial geodesics; its Γ has the derivative index first, as in the course.

### Counting curvature through coordinate freedom

$$
\underbrace{\big[\tfrac{n(n+1)}{2}\big]^2}_{\partial\partial g}-\underbrace{n\cdot\tfrac{n(n+1)(n+2)}{6}}_{\partial^3 x}=\frac{n^2(n^2-1)}{12}\ \xrightarrow{\ n=4\ }\ 100-80=20
$$

Second derivatives of the metric that no coordinate change can remove number exactly as many as the independent Riemann components. *(SCH ch06 §6.2 p.149; legacy:manuscript-section-10-normal-coordinates-and-counting)*

## Conventions across the books

| Issue | Schutz | Gifted Amateur | d'Inverno | Course choice |
| --- | --- | --- | --- | --- |
| Sign and slot order of the Riemann tensor in the second-derivative formula | R_αβμν = (1/2)(g_αν,βμ - g_αμ,βν + g_βμ,αν - g_βν,αμ) at P (eq. 6.68), MTW sign. | Same four-term expression in hatted local-inertial-frame components (eqn 11.23), with the general-coordinate version including Γ-Γ terms in a margin note. | Does not display the four-term formula; uses geodesic coordinates to prove the Riemann identities. Its Riemann definition matches MTW's index convention. | Use the four-term formula exactly as written in Schutz and Gifted Amateur, always labelled 'at P, in coordinates with vanishing first metric derivatives'. |
| Metric signature and its effect on lowered components | (-,+,+,+); η = diag(-1, 1, 1, 1). | (-,+,+,+). | (+,-,-,-). Lowered components R_abcd change sign relative to the course for the same geometry, but R^a_bcd does not, and both the four-term formula and g = η - (1/3) R x x keep their form because both sides flip together. | (-,+,+,+). When quoting d'Inverno's lowered components, flip their sign; formulas relating R_αβμν to metric derivatives need no change. |
| Names and construction of the special coordinates | 'Local inertial frame' or 'local Lorentz frame': g = η and first derivatives zero at P, justified by the Taylor counting argument; no explicit geodesic construction. | 'Local inertial frame' with hatted indices in ch11; 'Riemann normal coordinates' ζ^α = λ u^α built from geodesics and an orthonormal frame in ch35, with hats dropped in Example 35.4 and Exercise 35.4. | 'Geodesic coordinates': x'^a = x^a + (1/2) Q^a_bc x^b x^c with Q = Γ(P), making Γ vanish at P without normalizing the metric; equations valid only in such coordinates carry a starred equals sign. | 'Locally inertial coordinates at P' means g(P) = η and d g(P) = 0; 'Riemann normal coordinates' means the exponential-map construction, which additionally fixes the symmetrized derivatives of Γ and gives the minus one third expansion. Coordinate-specific equations are flagged in words. |
| Christoffel index order in derivative-of-Γ formulas | Derivative index last on Γ (V^α_;β = V^α_,β + Γ^α_μβ V^μ). | Derivative index first in ch35 (∇_μ e_ν = Γ^α_μν e_α), which is how Exercise 35.4 is written. | Derivative index last. | Derivative index first. For the symmetric Levi-Civita connection every formula here is unchanged, but the order matters when matching printed index strings term by term. |

## How the sources teach it

### schutz

**Route:** In §6.2 asks whether coordinates can make the metric Minkowskian with zero first and second derivatives at a point, and answers by counting Taylor coefficients (16 vs 10, 40 vs 40, 80 vs 100): the 20 unremovable second derivatives are declared real geometry. In §6.5, after defining Riemann by loop transport, evaluates it in a local inertial frame, differentiates the Christoffel formula, lowers an index to get the four-term formula, reads off the symmetries, and notes that the component count is again 20.

**Representation:** Taylor expansions and counting; component formulas in a special frame; explicit remarks on which equations can be promoted.

**Strengths:** Predicts the number twenty before the Riemann tensor exists and then pays it off, giving curvature a clear meaning as irremovable second-derivative information. Warns explicitly that the partial-derivative formula is not a tensor equation.

**Weaknesses:** The counting argument is a plausibility argument (independence of the conditions is assumed) and no explicit coordinate construction or metric expansion is given. A printed index slip in the intermediate formula can stall careful readers. *(SCH ch06 §6.2 p.148; SCH ch06 §6.2 p.149; SCH ch06 §6.5 p.158; SCH ch06 §6.5 p.159)*

### gifted-amateur

**Route:** Ch11 Example 11.5 invokes the local flatness theorem to reduce Riemann to derivatives of the connection and then to four second derivatives of the metric, with a margin note giving the general-coordinate formula for reassurance. Ch35 Example 35.4 builds normal coordinates first in the flat plane (a numerical point on a ray) and then with geodesics, quotes the metric expansion, and leaves the derivation of the minus one third to an eight-part guided exercise based on geodesic deviation.

**Representation:** Hatted frame components, a three-panel geometric construction figure, and a guided exercise.

**Strengths:** Shows the construction with a picture and a concrete number; derives the coefficient from tidal physics rather than pure algebra; the general-coordinate formula prevents over-promotion.

**Weaknesses:** Describes the result as a flat frame, which invites the belief that the neighbourhood is flat. The expansion is quoted before it is justified, symbols are overloaded in the exercise, and the size of the normal neighbourhood is not discussed. *(GA ch11 Example 11.5; GA ch11 §11.4 p.126; GA ch35 Example 35.4; GA ch35 §35.2 p.368; GA ch35 Exercise 35.4 p.373)*

### legacy

**Route:** §8.5 constructs Γ-free coordinates explicitly with the quadratic change x' = x + (1/2) Γ(0) x x, checks the symmetries with the second-derivative formula and promotes them. §10.6 defines Riemann normal coordinates via the exponential map, boxes the minus one third expansion with an optional derivation, contrasts Fermi coordinates along a worldline, and states the laboratory-size condition. §10.10 repeats the Taylor-coefficient count.

**Representation:** Course-convention components, explicit coordinate transformation, boxed expansion, verbal limits of the equivalence principle.

**Strengths:** The construction is shown rather than assumed; it is honest that the neighbourhood is not flat and that only radial geodesics become straight lines; it distinguishes event-centred from worldline-centred coordinates.

**Weaknesses:** Graduate-level density on a novice path; the derivation of the coefficient sits in a disclosure that narration skips; there is no picture of geodesic rays or grid distortion. *(legacy:manuscript-section-8-4-8-6-flatness-count-sphere-curvature; legacy:manuscript-section-10-normal-coordinates-and-counting)*

## Recommended teaching path

1. **Ask what is real in the metric** — Pose the question: at one event, which features of the metric are genuine geometry and which are just a choice of labels? Recall that free fall removes gravity locally, so the value and slope of the metric should be removable. *Why:* Frames the whole topic as separating coordinate artefacts from invariant content, which is the idea the learner needs to keep. *(SCH ch06 §6.2 p.149; legacy:manuscript-section-10-normal-coordinates-and-counting)*
2. **Count the freedom** — Build the Taylor ledger together: 10, 40, 100 metric numbers against 16, 40, 80 coordinate numbers. Interpret the 6 spare as Lorentz transformations and the 20 missing as curvature. *Why:* Arithmetic the learner can check gives the number twenty a meaning before any tensor algebra. *(SCH ch06 §6.2 p.148)*
3. **See normal coordinates on a globe** — Use the normal-coordinate map demo: rays from a point on a sphere define the coordinates; show that metric errors start at second order and that small circles fall short of 2 π r by a cubic amount. *Why:* A picture of 'flat to first order, curved at second' anchors both the formula and its limits. *(GA ch35 Example 35.4; GA ch35 Fig. 35.2(c) p.367; legacy:manuscript-section-10-normal-coordinates-and-counting)*
4. **Derive the four-term formula** — At P set Γ = 0, keep only derivatives of Γ in Riemann, substitute the differentiated Christoffel formula, lower the index and simplify. Immediately label the result as valid only at P in these coordinates, and show the general formula with Γ-Γ terms. *Why:* The derivation is short and exposes why curvature is second-derivative information; the label blocks the most common promotion error. *(SCH ch06 §6.5 p.158; GA ch11 Example 11.5; DIV ch06 §6.6 p.95)*
5. **Check on the unit sphere** — Give the normal-coordinate metric of the unit sphere to second order, g_11 = 1 - y^2/3, g_22 = 1 - x^2/3, g_12 = xy/3, and have the learner compute R_1212 = 1 from the four-term formula. Contrast with applying the formula naively in polar coordinates on the flat plane, where it wrongly gives -1. *Why:* One success and one instructive failure make both the formula and its conditions stick. *(legacy:manuscript-section-8-4-8-6-flatness-count-sphere-curvature; GA ch11 §11.4 p.126)*
6. **State and justify the expansion** — Present g = η - (1/3) R x x, explain that there is no linear term, and outline where the one third comes from: radial lines must be geodesics, which fixes the symmetrized derivative of Γ. Offer the geodesic-deviation derivation as an extended exercise. *Why:* Learners see that the coefficient is forced by the construction, not a convention. *(GA ch35 Exercise 35.4 p.373; legacy:manuscript-section-10-normal-coordinates-and-counting)*
7. **Apply it** — Read off the Riemann symmetries from the four-term formula, then turn to physics: how large a freely falling laboratory can be before tides show (roughly |R| L^2 much less than 1, plus small curvature gradients), and why accelerometers cannot see curvature but pairs of free particles can. *Why:* Connects the local algebra to the symmetries lesson and to the operational meaning of the equivalence principle. *(SCH ch06 §6.5 p.158; legacy:manuscript-section-10-normal-coordinates-and-counting)*

## Analogies

- **A map centred on your front door** (intuition): A map that keeps true distance and bearing from its centre (the azimuthal equidistant projection) is exactly normal coordinates on a globe. Right at the centre it is perfect, nearby its errors start only at second order, and circles drawn around the centre represent real circles whose true circumference is a little shorter than the map suggests. *Limits:* It shows a two-dimensional space with one curvature number and no time direction; spacetime normal coordinates carry twenty curvature components and include timelike directions. The projection also breaks down at the antipode, the analogue of the normal neighbourhood ending at conjugate points. *(GA ch35 Example 35.4)*
- **A stiff board against a curved hill** (intuition): You can always place a board so it touches a hillside at one point and matches its tilt, but no board matches its bending. Position and slope are removable by placement; the second-order shape is not. *Limits:* The hill's bending is extrinsic: it describes how the surface sits in the surrounding space. The Riemann tensor is intrinsic and can be measured without leaving the surface. A rolled-up sheet of paper is visibly bent yet has zero Riemann curvature, because its inner geometry is unchanged: an ant on it measures flat triangles. So the board shows that shape at second order cannot be placed away, but whether a surface looks bent from outside is the wrong test of curvature. Also, in spacetime coordinate freedom does absorb most second derivatives of the metric (80 of 100 in four dimensions), which the rigid-board picture does not capture.
- **Newtonian potential, force and tides** (working): In Newtonian gravity the potential's value is arbitrary and its gradient can be cancelled by falling freely, but its second derivatives, the tidal tensor, cannot be removed. The metric plays the potential's role, and Riemann plays the tidal tensor's. *Limits:* The Newtonian tidal tensor is a symmetric 3-by-3 matrix; Riemann has twenty components, including parts with no Newtonian counterpart. The correspondence R_0i0j with second derivatives of the potential holds only in the weak-field, slow-motion limit. *(SCH ch06 §6.2 p.149)*

## Misconceptions

- **In a local inertial frame, or in Riemann normal coordinates, spacetime is flat in a small neighbourhood.** — Only the metric's value and first derivatives are Minkowskian, and only at the single event P. The second derivatives equal minus one third of curvature combinations and cannot be removed, so tidal effects remain. *Why tempting:* Phrases like 'locally flat' and 'the frame is flat with vanishing connection' are common paraphrases of the equivalence principle. *Diagnostic:* In Riemann normal coordinates centred on a point of a unit sphere, what is the second derivative of g_22 with respect to x^1 twice at the origin? *(GA ch35 §35.2 p.368; legacy:manuscript-section-10-normal-coordinates-and-counting)*
- **Gravity or curvature shows up in the first derivatives of the metric, so nonzero Christoffel symbols prove spacetime is curved.** — First derivatives, and hence Christoffel symbols, can always be removed at a point by a coordinate choice. Curvature lives in the second derivatives that survive; flat space in polar coordinates has nonzero Christoffel symbols. *Why tempting:* Newtonian gravitational acceleration is the first derivative of the potential, and the geodesic equation's 'force' term is a Christoffel symbol. *Diagnostic:* The flat plane in polar coordinates has Γ^r_θθ = -r. Is the plane curved? Which quantity would settle the question? *(SCH ch06 §6.2 p.149; legacy:manuscript-section-8-4-8-6-flatness-count-sphere-curvature)*
- **Anything proved in a local inertial frame, including the four-term second-derivative formula, holds in every coordinate system.** — Only genuine tensor equations can be promoted. Relations among components of R (such as its symmetries) are tensor equations; the formula expressing R through partial derivatives of g, and the statement Γ = 0, hold only at P in those coordinates. *Why tempting:* The course repeatedly computes in a special frame and then promotes the result, so the step starts to feel automatic. *Diagnostic:* Which of these may be used in Schwarzschild coordinates: R_αβμν = -R_βαμν; R_αβμν = (1/2)(second derivatives of g); Γ^ρ_μν = 0? *(SCH ch06 §6.5 p.158; GA ch11 §11.4 p.126)*
- **With enough cleverness a coordinate change could also remove the second derivatives of the metric at a point.** — At second order a coordinate change offers 80 adjustable numbers in four dimensions but the metric has 100 second derivatives; 20 combinations always remain, and they are the Riemann components. One can make Γ vanish along a whole curve, but not make curvature vanish. *Why tempting:* The first two orders work out so neatly (with numbers to spare at zeroth order) that it seems the pattern should continue. *Diagnostic:* How many third derivatives of the coordinate transformation can you choose at P in four dimensions, and how many second derivatives of the metric would you need to set to zero? *(SCH ch06 §6.2 p.149; legacy:manuscript-section-10-normal-coordinates-and-counting)*
- **In Riemann normal coordinates every geodesic near P is a straight coordinate line.** — Only the geodesics passing through P are straight lines through the origin. Others curve in these coordinates; if all geodesics were straight, curvature would have been erased. *Why tempting:* The construction is phrased as 'geodesics become straight lines', and Γ vanishes at the origin. *Diagnostic:* In normal coordinates centred at P on a sphere, is the great circle that passes a short distance from P, but not through it, a straight line on the coordinate chart? *(legacy:manuscript-section-10-normal-coordinates-and-counting)*

## Visualizations

### Normal-coordinate map of a curved surface · interactive-3d · high priority

Build Riemann normal coordinates live on a surface of constant curvature and show that the metric is exact at the origin, has no linear error, and departs quadratically as the minus one third formula predicts.

**Interaction:** The learner picks a surface (sphere, flat plane, hyperbolic) and a curvature K, sets the origin, and sees geodesic rays fan out. A side panel shows the flat (x^1, x^2) chart coloured by the exact g_ij - δ_ij, a second colouring shows the prediction -(K/3)(r^2 δ_ij - x_i x_j), and a third shows their difference. Hovering a chart point draws its geodesic on the surface; a circle tool compares true circumference with 2 π r.

**Model:** Exact normal-coordinate metric of a constant-curvature surface: ds^2 = dr^2 + S_K(r)^2 dphi^2 with S_K = sin(sqrt(K) r)/sqrt(K) (sinh for K < 0, r for K = 0). In Cartesian normal coordinates g_ij = xhat_i xhat_j + (S_K/r)^2 (δ_ij - xhat_i xhat_j), which expands to δ_ij - (K/3)(r^2 δ_ij - x_i x_j) + O(r^4); circumference 2 π S_K(r) = 2 π r (1 - K r^2/6 + ...).

**Inspired by:** GA ch35 Fig. 35.2(c) p.367; GA ch35 Fig. 35.2(a) p.367; legacy:manuscript-section-10-normal-coordinates-and-counting

**Legacy assets:** manuscript-section-10-normal-coordinates-and-counting

### Taylor-coefficient budget · interactive-2d · medium priority

A ledger comparing, order by order, the metric's Taylor coefficients at a point with the coordinate transformation's adjustable coefficients, so the twenty curvature numbers appear as an unavoidable shortfall.

**Interaction:** A dimension selector (n = 2 to 5) updates three rows of paired bars: order 0 (metric values vs Jacobian entries), order 1 (first derivatives vs second derivatives of the map) and order 2 (second derivatives vs third derivatives). Surplus at order 0 is labelled rotations and boosts; the order-2 shortfall is labelled curvature and linked to the Riemann tile board.

**Model:** Counts: metric values n(n+1)/2, first derivatives n * n(n+1)/2, second derivatives [n(n+1)/2]^2; coordinate freedom n^2, n * n(n+1)/2, n * n(n+1)(n+2)/6. Surplus n(n-1)/2 at order 0, zero at order 1, shortfall n^2(n^2-1)/12 at order 2 (1, 6, 20, 50 for n = 2 to 5).

**Inspired by:** SCH ch06 §6.2 p.148; legacy:manuscript-section-10-normal-coordinates-and-counting

**Legacy assets:** manuscript-section-10-normal-coordinates-and-counting, lab-riemann-independent-components

### Kill Gamma, keep R · interactive-2d · medium priority

Show on a concrete 2D metric that a quadratic coordinate change can drive the Christoffel symbols at a point to zero while the curvature readout does not move, and that the four-term formula becomes valid exactly when the connection vanishes.

**Interaction:** The learner chooses a metric (sphere in latitude-longitude, polar plane, a paraboloid) and a point, then drags sliders for the coefficients Q of x' = x + (1/2) Q x x while the coordinate grid warps. Live readouts show Γ at the point, R_1212 from the full formula (constant), and R_1212 from the four-term formula, which matches only when Q equals Γ.

**Model:** Transformation of the connection at the origin under x' = x + (1/2) Q x x: Γ'(P) = Γ(P) - Q. Curvature from the exact general-coordinate expression with Γ-Γ terms; four-term formula evaluated in the new coordinates.

**Inspired by:** DIV ch06 §6.6 p.95; legacy:manuscript-section-8-4-8-6-flatness-count-sphere-curvature

**Legacy assets:** manuscript-section-8-4-8-6-flatness-count-sphere-curvature

### How big can a free-fall lab be? · animated-3d · low priority

A freely falling box near a massive body in which residual tidal displacements grow with box size, making the second-order limit of local inertial frames tangible.

**Interaction:** The learner sets the central mass, orbital radius, box size L and experiment duration; test particles inside drift apart; a readout compares tidal displacement (about R L T^2) with an adjustable measurement precision and flags when the lab stops being inertial.

**Model:** Newtonian-limit tidal field around a point mass: radial stretching 2GM/r^3 and transverse squeezing GM/r^3 applied to particle offsets, matching R_0i0j in the weak-field limit.

**Inspired by:** legacy:manuscript-section-10-normal-coordinates-and-counting

**Legacy assets:** manuscript-chapter-10-tides-geodesic-deviation

## Worked examples

- **Local flatness by counting** (working): Taylor-expands the coordinate transformation and the metric and compares adjustable numbers with conditions order by order, leaving 20 second-derivative combinations as geometry. *(SCH ch06 §6.2 p.148)*
- **Riemann components at a point** (working): Differentiates the Christoffel formula in a local inertial frame, drops Γ-squared terms, lowers an index and reaches the four-term formula with its symmetries. *(SCH ch06 §6.5 p.158)*
- **A form of Riemann that shows its symmetries** (working): The same reduction phrased through the local flatness theorem, with the general-coordinate formula supplied for comparison. *(GA ch11 Example 11.5)*
- **Constructing Riemann normal coordinates** (working): Labels points by distance along rays times unit direction in the flat plane, then replaces rays with geodesics from an orthonormal frame, giving vanishing connection at the origin. *(GA ch35 Example 35.4)*
- **Explicit Gamma-free chart and symmetry check** (working): The quadratic change x' = x + (1/2) Γ(0) x x cancels the connection at a point; the second-derivative formula then verifies the symmetries in course conventions. *(legacy:manuscript-section-8-4-8-6-flatness-count-sphere-curvature)*
- **Deriving the minus one third** (formal): Radial geodesics force the symmetrized derivative of Γ to vanish; solving with the Riemann definition and differentiating metric compatibility yields the expansion coefficient. *(legacy:manuscript-section-10-normal-coordinates-and-counting)*

## Exercises

- (intro) Verify the counts of independent first, second and third derivatives used in the local-flatness argument. *Skill:* Counting components of arrays symmetric in several indices *(SCH ch06 Exercise 6.4 p.166)*
- (standard) Derive the pair symmetries and cyclic identity from the four-term formula and count the independent components. *Skill:* Reading symmetries from a local-frame formula; counting with index pairs *(SCH ch06 Exercise 6.18 p.167)*
- (standard) Prove the differential Bianchi identity at a point, taking care not to differentiate a formula that holds only at that point. *Skill:* Using normal coordinates correctly beyond first order *(SCH ch06 Exercise 6.23 p.167)*
- (challenging) For a weak-field metric, construct first-order local inertial coordinates at a point and find their acceleration relative to the original coordinates. *Skill:* Building local inertial frames explicitly *(SCH ch06 Exercise 6.36 p.168)*
- (challenging) Guided eight-part derivation of the normal-coordinate metric expansion from geodesic deviation of radial geodesics. *Skill:* Taylor expansion of the connection and metric; geodesic deviation *(GA ch35 Exercise 35.4 p.373)*
- (intro) Explain in words why Christoffel symbols can vanish at a point in normal coordinates while the Riemann tensor does not. *Skill:* Separating coordinate artefacts from curvature *(legacy:practice-set-appendix-a-thirty-exercises)*

## Checks for understanding

- **Q (intuition):** A friend says: 'Inside a freely falling elevator gravity disappears, so spacetime inside the elevator is flat.' What is right and what is wrong about this?
  - **A:** Right: at the elevator's centre and to first order in distance, free fall makes the metric Minkowskian, so no uniform gravitational field is felt. Wrong: second derivatives of the metric cannot be removed. The metric's departure from Minkowski grows with the square of the distance from the centre, in proportion to the curvature, so particles released at rest across the elevator slowly drift apart or together (tides). Spacetime is not flat in any region unless the Riemann tensor vanishes there. *(targets: In a local inertial frame, or in Riemann normal coordinates, spacetime is flat in a small neighbourhood.)*
- **Q (working):** Near the origin of normal coordinates on a unit sphere the metric is g_11 = 1 - y^2/3, g_22 = 1 - x^2/3, g_12 = xy/3 (up to fourth order). Use R_1212 = (1/2)(d_2 d_1 g_12 - d_2 d_2 g_11 + d_1 d_2 g_21 - d_1 d_1 g_22) to find R_1212 at the origin.
  - **A:** d_1 d_2 g_12 = 1/3 (twice, since g_12 = g_21), d_2 d_2 g_11 = -2/3 and d_1 d_1 g_22 = -2/3. So R_1212 = (1/2)(1/3 + 2/3 + 1/3 + 2/3) = 1, matching Gaussian curvature K = 1 of the unit sphere with the course sign convention.
- **Q (working):** Apply the four-term formula to the flat plane in polar coordinates, ds^2 = dr^2 + r^2 dtheta^2, to compute R_r θ r θ. What do you get, why is it wrong, and how does the full formula fix it?
  - **A:** Only g_θθ = r^2 has a nonzero second derivative, ∂_r ∂_r g_θθ = 2, which enters with a minus sign: the formula gives (1/2)(-2) = -1. It is wrong because polar coordinates do not have vanishing first metric derivatives (Γ^θ_r θ = 1/r, Γ^r_θθ = -r are nonzero). The general formula adds g_ρσ(Γ^ρ_θ r Γ^σ_r θ - Γ^ρ_θθ Γ^σ_r r) = g_θθ (1/r)^2 - 0 = +1, so R_r θ r θ = -1 + 1 = 0, as flatness demands. *(targets: Anything proved in a local inertial frame, including the four-term second-derivative formula, holds in every coordinate system.)*
- **Q (formal):** Repeat the coefficient count in three dimensions: how many second derivatives of the metric, how many third derivatives of a coordinate change, and how many curvature components remain?
  - **A:** The metric has 6 components, so 6 x 6 = 36 second derivatives. A coordinate change has 3 functions, each with 10 independent third derivatives, giving 30. The shortfall is 36 - 30 = 6, which equals n^2(n^2 - 1)/12 = 9 x 8/12 = 6, the number of independent Riemann components in three dimensions (the same as the six components of the Ricci tensor there). *(targets: With enough cleverness a coordinate change could also remove the second derivatives of the metric at a point.)*
- **Q (formal):** From g_μν = η_μν - (1/3) R_μανβ x^α x^β, show that the circumference of a small geodesic circle of radius r on a surface of Gaussian curvature K is 2 π r (1 - K r^2/6). Use R_abcd = K(g_ac g_bd - g_ad g_bc).
  - **A:** At the origin R_i a j b x^a x^b = K(δ_ij r^2 - x_i x_j). Along the circle the tangent t = (-sin φ, cos φ) is perpendicular to x, so g_ij t^i t^j = 1 - (K/3)(r^2 - 0) = 1 - K r^2/3. The circumference is the integral of r sqrt(1 - K r^2/3) dphi, about 2 π r (1 - K r^2/6). No linear correction appears, and the cubic shortfall measures K.

## Applications

- **Limits of the equivalence principle**: The expansion quantifies how large and how long an experiment can be before a freely falling laboratory reveals curvature: roughly when |R| L^2 is no longer negligible, with extra care if curvature varies across the region. Key numbers: Near Earth's surface GM/r^3 is about 1.5e-6 s^-2, so two masses 1 m apart drift by about 1 micrometre in 1 s. *(legacy:manuscript-section-10-normal-coordinates-and-counting)*
- **Proving curvature identities**: Normal coordinates turn the symmetries, the cyclic identity and the differential Bianchi identity into short checks with partial derivatives at one point, which are then promoted as tensor equations. *(SCH ch06 §6.5 p.158; legacy:manuscript-section-09-bianchi-einstein-tensor)*
- **Weak-field and gravitational-wave curvature**: The linearized Riemann tensor has the same four-term second-derivative structure with the metric perturbation h in place of g, which is why it is gauge invariant at first order. *(SCH ch06 §6.5 p.158)*

## Tutor guidance

**Opening questions**

- If you are falling freely, which parts of gravity can you no longer feel, and which can you still detect?
- Can you choose coordinates at a point where all Christoffel symbols vanish? Does that make the space flat?
- On a globe, if you draw a small circle of radius r around a point, is its circumference more or less than 2 π r?

**Common questions**

- *Why is there a factor one half in the four-term formula?* — It comes straight from the one half in the Christoffel formula; differentiating Γ once and lowering the index keeps that factor, and the symmetric terms pair up without doubling it.
- *Where does the minus one third come from?* — In normal coordinates the radial lines must be geodesics, which forces the fully symmetrized derivative of Γ to vanish. Solving that condition together with the Riemann definition gives derivatives of Γ equal to minus one third of two Riemann terms; the one half from Taylor's formula and two equal terms then combine into minus one third.
- *Is a local inertial frame the same thing as Riemann normal coordinates?* — Every Riemann normal coordinate system is locally inertial at its origin, but not conversely. Any coordinates with g = η and zero first derivatives at P are locally inertial and give the four-term formula; the minus one third expansion needs the extra normal-coordinate conditions.
- *Can I compute curvature in practice with the four-term formula?* — Only if you already have coordinates with vanishing first metric derivatives at the point. Usually it is easier to compute Christoffel symbols and use the general Riemann formula, then use the four-term formula for proofs.
- *Why exactly twenty?* — In four dimensions the metric has 100 second derivatives at a point and a coordinate change can adjust only 80 of them; the 20 left over match the independent components allowed by the Riemann symmetries.
- *What about Fermi coordinates?* — They extend the idea along a whole free-fall worldline instead of a single event: the metric is Minkowskian with zero first derivatives all along the worldline, and curvature appears quadratically in the transverse distance, for example g_00 = -1 - R_0i0j x^i x^j.

**Pitfalls when explaining**

- Never say the neighbourhood is flat; say the metric is Minkowskian to first order at one event.
- Label every coordinate-specific equation in speech ('at P, in these coordinates') before using it.
- Do not differentiate the four-term formula to get identities that need third derivatives; it holds only at P, so derivatives of it are meaningless.
- Keep 'locally inertial coordinates' (value and slope fixed) distinct from 'Riemann normal coordinates' (geodesic construction); the minus one third belongs to the latter.
- In spacetime the geodesic rays include timelike and null directions and the 'distance' is an affine parameter; do not describe the construction purely in terms of spatial lengths.
- When quoting d'Inverno's lowered Riemann components, remember the sign flip from the opposite signature.

**When to show a demo**

- When the learner claims a freely falling lab is flat, open the normal-coordinate map, grow the region, and watch the metric error colour in quadratically.
- When deriving the four-term formula, use 'Kill Γ, keep R' to show that the formula's validity switches on exactly when the Christoffel symbols at the point reach zero.
- When introducing the number twenty, run the Taylor-coefficient budget with the dimension selector before revealing Riemann's symmetries.

**Saying it aloud:** Say the expansion in words first: 'near the chosen event the metric starts out exactly Minkowskian, has no correction linear in distance, and its first correction is minus one third of the curvature times the displacement taken twice.' Then: 'g mu nu equals eta mu nu minus one third R mu alpha nu beta, x alpha, x beta.' For the four-term formula say 'at that event, all-lower Riemann is one half of a signed sum of four second derivatives of the metric,' and only read index strings if the learner is writing them down. Always add 'only at that point, only in those coordinates.'

## Sources

- schutz ch06 (core): p.145 §6.2, p.149 §6.2, p.158 §6.5, p.159 §6.5
- gifted-amateur ch11 (developed): p.126 §11.4
- gifted-amateur ch35 (developed): p.367 §35.2, p.368 §35.2, p.373
- legacy manuscript-section-10-normal-coordinates-and-counting (developed)
- legacy manuscript-section-8-4-8-6-flatness-count-sphere-curvature (developed)

## Review

**Verdict:** fixed

**Fixes**

- Rewrote the limits of the stiff-board analogy. The old text said a rolled sheet has zero Riemann curvature 'because coordinate freedom at second order removes most, but not all' second derivatives, which is a non sequitur. It now says the sheet is intrinsically flat (extrinsic bending is not Riemann curvature) and states separately that coordinate freedom absorbs 80 of the 100 second derivatives.

**Concerns**

- Independently re-checked: the four-term formula against Schutz eq. 6.68 and GA eqn 11.23; the general-coordinate formula (GA eqn 11.22) on the polar plane (−1 + 1 = 0) and the unit sphere (−cos 2θ + cos²θ = sin²θ); the sphere normal-coordinate metric and R_1212 = 1; ∂Γ = −(1/3)(R + R), checked by substituting back into the Riemann definition with the cyclic identity; ∂∂g = −(1/3)(R_μανβ + R_μβνα); the counts 100 − 80 = 20, 36 − 30 = 6, 1 and 50 for n = 2 and 5; the circumference 2πr(1 − Kr²/6); the Fermi form g_00 = −1 − R_0i0j x^i x^j; the Earth tidal numbers; and the connection shift Γ' = Γ − Q under x' = x + ½Qxx. No other errors found.
- d'Inverno is cited for geodesic coordinates (DIV ch06 §6.6 p.95) but is not a registry source for this concept, so there is no d'Inverno how_books_teach entry. Its treatment is covered in the conventions table.
- The prerequisite christoffel-symbols-from-the-metric goes beyond the registry prerequisites, and the writer did not edit the registry.
