---
type: "concept"
id: "symmetries-of-the-riemann-tensor"
title: "Symmetries of the Riemann tensor"
domain: "curvature"
tier: "core"
aliases: ["pair antisymmetry", "pair-exchange symmetry", "algebraic symmetries of the Riemann tensor"]
prerequisites: ["riemann-tensor-in-normal-coordinates", "symmetric-and-antisymmetric-tensors", "raising-and-lowering-indices", "covariance-of-tensor-equations", "metric-compatibility"]
leads_to: ["cyclic-identity", "number-of-independent-riemann-components", "ricci-tensor", "bianchi-identity", "sectional-curvature", "curvature-of-the-two-sphere", "weyl-tensor"]
sources: ["dinverno:ch06", "gifted-amateur:ch11", "gifted-amateur:ch13", "gifted-amateur:ch35", "gifted-amateur:ch36", "legacy:lab-riemann-independent-components", "legacy:manuscript-section-8-4-8-6-flatness-count-sphere-curvature", "schutz:ch06"]
review: "fixed"
---

# Symmetries of the Riemann tensor

> Lower the first index of the Riemann tensor and three rules appear: swapping the first two indices flips the sign, swapping the last two flips the sign, and trading the first pair for the last pair changes nothing. Together with the cyclic identity these rules shrink the 256 slots of a four-index object in four dimensions to 20 independent numbers, and because they are tensor equations they hold in every basis.

## Explanations by level

### Intuition

Think of the Riemann tensor as answering a question about tiny loops: 'if I carry an arrow around a small loop lying in one plane, how much does the arrow turn, as seen in some other plane?' So each pair of indices names a plane. Walk the loop the other way round and the turn reverses: that is why swapping the last two indices flips the sign. The carried arrow keeps its length, so what happens to it is a pure rotation, and a rotation from direction one toward direction two is the reverse of a rotation from two toward one: that is why swapping the first two indices flips the sign. Finally there is a reciprocity: the turning that a loop in plane A causes within plane B equals the turning a loop in plane B causes within plane A, which is why the two pairs can be exchanged. Because of these rules, curvature in four dimensions fits in a symmetric six-by-six table of planes rather than a huge array. What is simplified: in spacetime some of the 'planes' include time and the 'rotations' include boosts, and the reciprocity rule is not obvious from pictures; it follows from the other rules plus the cyclic identity.

**Picture to hold:** A six-by-six table whose rows and columns are the oriented planes tx, ty, tz, xy, xz, yz, mirror-symmetric about its diagonal.

**Assumes:** [[holonomy]], [[riemann-curvature-tensor]]

### Working

Define R_αβμν = g_αλ R^λ_βμν. Then R_αβμν = -R_βαμν = -R_αβνμ = R_μναβ, and in addition R_αβμν + R_αμνβ + R_ανβμ = 0 (the cyclic identity). Where each comes from: antisymmetry in the last pair is built into the definition (the commutator [∇_μ, ∇_ν] is antisymmetric, and reversing a loop reverses the change). Antisymmetry in the first pair comes from metric compatibility: applying the Ricci identity to the metric gives 0 = [∇_μ, ∇_ν] g_αβ = -R_βαμν - R_αβμν. Pair exchange follows from the other three rules, or can be seen by inspection in the normal-coordinate formula R_αβμν = (1/2)(g_αν,βμ - g_αμ,βν + g_βμ,αν - g_βν,αμ). Since these are relations between tensor components, proving them in one coordinate system proves them in all. Practical consequences: any component with a repeated index inside a pair is zero (R_00 μν = 0, R_αβ 33 = 0); computing one component fixes its partners up to sign; in two dimensions everything reduces to R_1212, with R_αβμν = K(g_αμ g_βν - g_αν g_βμ); the Ricci tensor R_μν = R^ρ_μρν is symmetric and is essentially the only contraction. Counting: an antisymmetric pair has N = n(n-1)/2 values (6 in 4D), pair exchange makes a symmetric N-by-N array (21), and the cyclic identity removes one more in 4D, leaving 20. Careful: the rules are stated for all indices lowered; the mixed tensor R^α_βμν is not antisymmetric in α and β.

**Picture to hold:** Tiles on a 6-by-6 board: mirror tiles across the diagonal carry equal values, reversing a pair's order flips a tile's sign, and one extra relation ties together the three tiles with all four indices different.

**Assumes:** [[symmetric-and-antisymmetric-tensors]], [[raising-and-lowering-indices]], [[riemann-tensor-in-normal-coordinates]], [[covariance-of-tensor-equations]]

### Formal

Let ∇ be an affine connection with curvature R^ρ_σμν (course convention). (i) For any connection R^ρ_σμν = -R^ρ_σνμ. (ii) If ∇ is torsion-free, R^ρ_[σμν] = 0. (iii) If ∇ is metric-compatible, ∇ g = 0, then R_αβμν = g_αλ R^λ_βμν satisfies R_αβμν = -R_βαμν; equivalently, each curvature endomorphism R(X,Y) is skew-adjoint with respect to g and so lies in the Lie algebra of the pseudo-orthogonal group so(p,q). (iv) For the Levi-Civita connection, (i)-(iii) imply R_αβμν = R_μναβ, by writing the cyclic identity four times, once with each of α, β, μ, ν in the fixed first slot, and combining the four equations using the antisymmetries. Hence at each point R defines a symmetric bilinear form on the space of bivectors, Λ^2 T_pM of dimension N = n(n-1)/2, subject to the algebraic Bianchi condition R_α[βμν] = 0. Given (i), (iii) and pair exchange, the cyclic condition is a single constraint for each set of four distinct indices, so the space of algebraic curvature tensors has dimension N(N+1)/2 - C(n,4) = n^2(n^2-1)/12: 0, 1, 6, 20 for n = 1, 2, 3, 4. The sectional curvature K(u,v) = R_αβμν u^α v^β u^μ v^ν / (g(u,u)g(v,v) - g(u,v)^2) is well defined (independent of the basis of the plane) precisely because of these symmetries, and it determines R completely. For a torsion-free connection not derived from a metric only (i) and (ii) hold; in particular R^ρ_ρμν = ∂_μ Γ^ρ_νρ - ∂_ν Γ^ρ_μρ need not vanish and there is no pair exchange. An overall change of signature, g to -g, flips the sign of every R_αβμν but leaves all of the symmetry relations intact.

**Picture to hold:** Riemann as a symmetric operator on the six-dimensional space of bivectors, with the cyclic identity removing its completely antisymmetric part.

**Assumes:** [[metric-compatibility]], [[torsion-free-connection]], [[bivector]], [[levi-civita-connection]]

## Prerequisites

- [[riemann-tensor-in-normal-coordinates]] — The four-term second-derivative formula is where the pair symmetries can be read off by inspection.
- [[symmetric-and-antisymmetric-tensors]] — The statements are symmetry and antisymmetry properties under index exchange, and the counting uses the sizes of such arrays.
- [[raising-and-lowering-indices]] — The symmetries hold for the all-lower tensor; moving the first index with the metric is essential and changes what the rules look like.
- [[covariance-of-tensor-equations]] — The symmetries are proved in special coordinates and promoted to every basis because they are tensor equations.
- [[metric-compatibility]] — Antisymmetry in the first pair, and hence pair exchange, requires a connection that preserves the metric.

## Leads to

- [[cyclic-identity]] — The fourth algebraic identity, which together with the pair symmetries completes the set.
- [[number-of-independent-riemann-components]] — The symmetries reduce 256 components to 21, and the cyclic identity to 20.
- [[ricci-tensor]] — The symmetries make the Ricci tensor symmetric and essentially the only independent contraction.
- [[bianchi-identity]] — Its contraction to the conservation law for the Einstein tensor uses the pair antisymmetries.
- [[sectional-curvature]] — The symmetries make curvature a well-defined function of two-planes.
- [[curvature-of-the-two-sphere]] — In two dimensions the symmetries leave a single component, so one calculation gives the whole tensor.
- [[weyl-tensor]] — The Weyl tensor inherits all the Riemann symmetries and adds tracelessness.

## Related

- [[cyclic-identity]] — Part of the full set of algebraic identities; pair exchange can be derived from it and the antisymmetries.
- [[riemann-curvature-operator]] — First-pair antisymmetry says the curvature operator is an infinitesimal rotation or boost.
- [[bivector]] — Each antisymmetric index pair is a bivector, so Riemann is a symmetric matrix on the space of bivectors.
- [[curvature-2-form]] — Antisymmetry of the curvature 2-form in its frame indices is the first-pair antisymmetry in form language.
- [[ricci-identity]] — Applied to the metric it gives a one-line proof of first-pair antisymmetry.
- [[torsion-free-connection]] — Needed for the cyclic identity; without it only last-pair antisymmetry is guaranteed.

## Key equations

### All-lower Riemann tensor

$$
R_{\alpha\beta\mu\nu}=g_{\alpha\lambda}\,R^\lambda{}_{\beta\mu\nu}
$$

The symmetries are statements about this version, with the first index lowered by the metric. *(SCH ch06 §6.5 p.158; GA ch11 §11.4 p.126; DIV ch06 §6.12 p.106)*

**Convention:** All three books and the legacy course lower the first index.

### Pair antisymmetries and pair exchange

$$
R_{\alpha\beta\mu\nu}=-R_{\beta\alpha\mu\nu}=-R_{\alpha\beta\nu\mu}=R_{\mu\nu\alpha\beta}
$$

A swap inside either pair flips the sign; exchanging the pairs as wholes leaves the value unchanged. *(SCH ch06 §6.5 p.158; GA ch11 §11.4 p.126; DIV ch06 §6.12 p.106; legacy:manuscript-section-8-4-8-6-flatness-count-sphere-curvature)*

**Convention:** d'Inverno writes the same relations in the order R_abcd = -R_abdc = -R_bacd = R_cdab.

### Cyclic identity

$$
R_{\alpha\beta\mu\nu}+R_{\alpha\mu\nu\beta}+R_{\alpha\nu\beta\mu}=0\iff R_{\alpha[\beta\mu\nu]}=0
$$

Cycling the last three indices and adding gives zero; it adds exactly one new constraint in four dimensions, tying together components with four different indices. *(SCH ch06 §6.5 p.158; GA ch11 §11.4 p.126; DIV ch06 §6.12 p.106)*

**Convention:** Gifted Amateur and d'Inverno cycle the last three indices in the other direction; the identities are equivalent.

### First-pair antisymmetry from metric compatibility

$$
0=[\nabla_\mu,\nabla_\nu]\,g_{\alpha\beta}=-R^\lambda{}_{\alpha\mu\nu}g_{\lambda\beta}-R^\lambda{}_{\beta\mu\nu}g_{\alpha\lambda}=-\left(R_{\beta\alpha\mu\nu}+R_{\alpha\beta\mu\nu}\right)
$$

Because the metric is covariantly constant, the curvature acting on it must vanish, which forces antisymmetry in the first pair. This one-line proof is the course's own: it combines the one-term-per-index commutator rule with metric compatibility, whereas the books prove the rule in geodesic or inertial coordinates. *(SCH ch06 §6.5 p.160; DIV ch06 §6.10 p.104; legacy:manuscript-section-8-4-8-6-flatness-count-sphere-curvature)*

### Vanishing components

$$
R_{\alpha\alpha\mu\nu}=0,\qquad R_{\alpha\beta\mu\mu}=0\quad(\text{no sum})
$$

A repeated index inside either pair gives zero, so only components whose pairs are genuine planes survive. *(GA ch11 §11.4 p.126)*

### Two-dimensional Riemann tensor

$$
R_{\alpha\beta\mu\nu}=K\left(g_{\alpha\mu}g_{\beta\nu}-g_{\alpha\nu}g_{\beta\mu}\right),\qquad R_{1212}=K\,\det g
$$

In two dimensions the symmetries leave one component, fixed by the Gaussian curvature K; for a sphere of radius a, R_θφθφ = a^2 sin^2 θ. *(GA ch11 Example 11.6 p.127; GA ch36 Example 36.4; legacy:manuscript-section-8-4-8-6-flatness-count-sphere-curvature)*

**Convention:** Course sign: a sphere has K = +1/a^2.

### Number of independent components

$$
\frac{N(N+1)}{2}-\binom{n}{4}=\frac{n^2(n^2-1)}{12},\qquad N=\frac{n(n-1)}{2};\quad n=4:\ 21-1=20
$$

Counting symmetric arrays of antisymmetric pairs and subtracting cyclic constraints gives 1, 6 and 20 independent components in 2, 3 and 4 dimensions. *(GA ch35 Example 35.6; SCH ch06 Exercise 6.18 p.167; legacy:lab-riemann-independent-components)*

### Symmetry of the Ricci tensor

$$
R_{\mu\nu}=R^\rho{}_{\mu\rho\nu}=g^{\rho\sigma}R_{\sigma\mu\rho\nu}=R_{\nu\mu}
$$

Pair exchange makes the Ricci contraction symmetric; the antisymmetries make other contractions vanish or reduce to plus or minus Ricci. *(GA ch11 §11.5 p.127; DIV ch06 §6.12 p.106)*

## Conventions across the books

| Issue | Schutz | Gifted Amateur | d'Inverno | Course choice |
| --- | --- | --- | --- | --- |
| Which index is lowered and how the symmetries are listed | R_αβμν := g_αλ R^λ_βμν; R_αβμν = -R_βαμν = -R_αβνμ = R_μναβ (eq. 6.69). | R_αβγδ = g_αμ R^μ_βγδ; the same three relations (eqn 11.24), stated in words as 'swaps within a pair earn a minus sign'. | Lowers the first index; lists R_abcd = -R_abdc = -R_bacd = R_cdab (6.82). | Lower the first index and list the rules as first-pair antisymmetry, last-pair antisymmetry, pair exchange, then the cyclic identity. All sources agree; no translation needed. |
| Written order of the cyclic identity | R_αβμν + R_ανβμ + R_αμνβ = 0 (eq. 6.70). | R_αβγδ + R_αδβγ + R_αγδβ = 0 (eqn 11.25). | On the mixed tensor, R^a_bcd + R^a_dbc + R^a_cdb = 0 (6.79); lowered, R_abcd + R_adbc + R_acdb = 0; also written R^a_[bcd] = 0 with normalized brackets. | R_αβμν + R_αμνβ + R_ανβμ = 0, equivalently R_α[βμν] = 0. Every listed form is a cyclic permutation of the last three indices and is equivalent. |
| Metric signature and the sign of lowered components | (-,+,+,+). | (-,+,+,+). | (+,-,-,-): for the same spacetime every R_abcd has the opposite sign to the course value, while R^a_bcd agrees; the symmetry relations themselves are unchanged. | (-,+,+,+). Flip the sign of d'Inverno's lowered components when comparing numbers; never change the symmetry rules. |
| Assumptions behind each symmetry | Works with the metric connection throughout and reads all identities off the local-inertial-frame formula, without separating which assumption each needs. | Same approach in ch11; the torsion-free, metric-compatible connection is assumed implicitly. | Separates them: last-pair antisymmetry is immediate from the definition, the cyclic identity uses symmetry of the connection, pair exchange is shown for the metric connection via geodesic coordinates, and first-pair antisymmetry follows by combination. | Teach the assumption ladder explicitly: any connection gives last-pair antisymmetry; zero torsion adds the cyclic identity; metric compatibility adds first-pair antisymmetry; together they give pair exchange. |
| Name of the cyclic identity | No special name; referred to by equation number. | 'Cyclic identity' or 'cyclic symmetry'. | Listed among the algebraic identities, distinct from the differential Bianchi identities. | Call it the cyclic identity (also known as the first or algebraic Bianchi identity) and reserve 'Bianchi identity' for the differential one, to avoid the naming clash in the legacy text. |

## How the sources teach it

### schutz

**Route:** First motivates last-pair antisymmetry and linearity from the loop picture (doubling an edge doubles the change, reversing the loop flips it). After evaluating Riemann in a local inertial frame, declares the pair symmetries and cyclic identity easy to verify from the four-term formula, promotes them as tensor equations, and connects the resulting count of 20 to the 20 irremovable second derivatives found earlier; later uses the symmetries to show the Ricci tensor is the only contraction.

**Representation:** Component formula in a special frame, promotion of tensor equations, counting exercise with index pairs.

**Strengths:** Fastest route, with a big payoff: the number 20 from the symmetries matches the local-flatness count. The loop thought experiment gives last-pair antisymmetry a geometric reason.

**Weaknesses:** First-pair antisymmetry and pair exchange receive no geometric interpretation; the verification and count are left to an exercise; the role of the metric connection is not flagged. *(SCH ch06 §6.5 p.157; SCH ch06 §6.5 p.158; SCH ch06 §6.5 p.159; SCH ch06 Exercise 6.18 p.167)*

### gifted-amateur

**Route:** Opens by noting a four-index object naively has 256 components, derives the local-inertial-frame formula, states the three rules in plain words plus the cyclic identity, and tabulates independent components by dimension (0, 1, 6, 20), with a two-dimensional example having a single component. The count is proved much later (ch35), and the rules are used in practice when computing the sphere's curvature with forms (ch36) and in contracting the Bianchi identity (ch13).

**Representation:** Plain-language rules, a small table by dimension, margin notes on vanishing components, worked computations that exploit the rules.

**Strengths:** Very accessible statement and immediate practical use; the dimension table makes the reduction concrete.

**Weaknesses:** No geometric reason for any rule; the proof of the count is deferred by many chapters; the assumptions about the connection are not mentioned. *(GA ch11 §11.4 p.126; GA ch11 Example 11.5; GA ch35 Example 35.6; GA ch36 Example 36.4; GA ch13 Example 13.3)*

### dinverno

**Route:** In the curvature-tensor section, builds the identities in order of the assumptions they need: last-pair antisymmetry from the definition, the cyclic identity from a symmetric connection, pair exchange for the metric connection using geodesic coordinates, first-pair antisymmetry by combining; then quotes the count n^2(n^2-1)/12 and moves to the differential Bianchi identities. In ch23 the same symmetries let the Weyl tensor act as a symmetric 6-by-6 matrix on bivectors for classification.

**Representation:** Abstract component identities with identity signs, geodesic coordinates, later the bivector viewpoint.

**Strengths:** Makes clear which property of the connection each symmetry relies on; compact and precise; the later bivector use shows why the symmetries matter structurally.

**Weaknesses:** Proofs are exercises, there is no physical or geometric motivation, the count is stated without derivation, and the opposite signature changes the signs of lowered components relative to the course. *(DIV ch06 §6.12 p.105; DIV ch06 §6.12 p.106; DIV ch06 Exercise 6.24 p.110; DIV ch23 §23.7 p.472)*

### legacy

**Route:** §8.5 lowers the first index, lists the symmetries and cyclic identity, constructs a chart with vanishing connection explicitly, verifies the rules from the second-derivative formula, and counts with index pairs as single labels (6-by-6, symmetric 21, minus one cyclic relation, 20), noting that 20 is not a number of wave polarizations. A three-phase tile lab lets learners pair indices, match mirror tiles and apply the cyclic identity.

**Representation:** Course-convention components, explicit chart, combinatorial pair picture, an interactive tile board with exhaustive symmetry tests.

**Strengths:** Construction shown rather than assumed; the pair-as-label picture makes the count tactile; an explicit scope note separates the algebraic count from propagating degrees of freedom.

**Weaknesses:** Calls the cyclic identity the algebraic Bianchi identity, which collides with the differential one; no geometric meaning for pair exchange; the lab has numbering and colour inconsistencies and no dimension selector. *(legacy:manuscript-section-8-4-8-6-flatness-count-sphere-curvature; legacy:lab-riemann-independent-components)*

## Recommended teaching path

1. **Pose the bookkeeping problem** — Point out that a four-index object in four dimensions has 256 slots, and ask whether curvature really needs that many numbers. Recall that the local-flatness count suggested 20. *Why:* A concrete discrepancy (256 versus 20) motivates looking for relations between components. *(GA ch11 §11.4 p.126; SCH ch06 §6.5 p.159)*
2. **Give each pair a geometric job** — Using the loop picture, identify the last pair as the plane and orientation of a tiny loop (reverse it and the change reverses) and the first pair, once lowered, as the plane in which the carried vector rotates (a length-preserving change is antisymmetric). *Why:* Two of the three rules become obvious before any algebra, and the learner sees why lowering the index matters. *(SCH ch06 §6.5 p.157; legacy:manuscript-chapter-08-curvature-holonomy)*
3. **Read the rules off the normal-coordinate formula** — Write the four-term formula at P and check each swap: exchanging α and β flips the sign, exchanging μ and ν flips the sign, exchanging the pairs permutes the four terms among themselves. State that these are tensor equations and therefore hold everywhere. *Why:* Short, complete verification that also reinforces the promotion principle. *(SCH ch06 §6.5 p.158; GA ch11 Example 11.5; legacy:manuscript-section-8-4-8-6-flatness-count-sphere-curvature)*
4. **Climb the assumption ladder** — Separate what each rule needs: last-pair antisymmetry for any connection, the cyclic identity for zero torsion, first-pair antisymmetry for metric compatibility (one-line proof from [∇_μ, ∇_ν] g = 0), and pair exchange from the rest. *Why:* Prevents the belief that the symmetries are automatic for any connection and prepares learners for alternative-connection discussions. *(DIV ch06 §6.12 p.105; DIV ch06 §6.12 p.106)*
5. **Count on the tile board** — Open the Riemann tile board: collapse to 6 pairs, fold the 6-by-6 array along its diagonal to 21, apply the cyclic identity to reach 20; switch the dimension to 2 and 3 to see 1 and 6. *Why:* Turns an opaque formula into a sequence of visible reductions and links 2D to Gaussian curvature. *(GA ch35 Example 35.6; legacy:lab-riemann-independent-components)*
6. **Check on a sphere** — Compute R_θφθφ = a^2 sin^2 θ for a sphere of radius a, then generate every other nonzero component from the rules, including the mixed components R^θ_φθφ = sin^2 θ and R^φ_θφθ = 1, and verify R_αβμν = K(g g - g g) with K = 1/a^2. *Why:* A worked case shows the time saved and exposes the mixed-index trap. *(GA ch36 Example 36.4; legacy:manuscript-section-8-4-8-6-flatness-count-sphere-curvature; SCH ch06 Exercise 6.29 p.167)*
7. **Use the rules downstream** — Show that the Ricci tensor is symmetric and the only contraction, and that in an orthonormal frame the Einstein tensor's energy density component is a sum of spatial plane curvatures. *Why:* Connects the symmetries to the objects that appear in Einstein's equation. *(GA ch11 §11.5 p.127; GA ch21 Exercise 21.3)*

## Analogies

- **An infinitesimal rotation matrix** (working): A small rotation changes a vector by δ V_α = ω_αβ V^β with ω antisymmetric, which is exactly what keeps the length fixed. First-pair antisymmetry says the change produced by a tiny loop is such a rotation, with the loop plane choosing which rotation. *Limits:* In spacetime the 'rotations' include Lorentz boosts, and antisymmetry holds only with both indices lowered by the metric; the mixed matrix of a boost looks symmetric. The property also requires a metric-compatible connection. *(SCH ch06 §6.5 p.157)*
- **A mileage chart** (intuition): A road atlas prints distances between cities in a triangular table because the distance from A to B equals the distance from B to A. Pair exchange lets curvature be stored the same way, as a triangular table of planes, which is where 21 comes from in four dimensions. *Limits:* A mileage chart has zeros on its diagonal, while Riemann's diagonal entries (plane-with-itself, the sectional curvatures) carry much of the information; entries also carry signs tied to orientation; and the cyclic identity has no analogue in a mileage chart.
- **A table of electromagnetic field tensors** (working): The Faraday tensor is antisymmetric and has six components (three electric, three magnetic). Each index pair of Riemann is of the same antisymmetric type, so Riemann is like a symmetric six-by-six matrix indexed by such pairs. *Limits:* The Faraday tensor is one antisymmetric object; Riemann is a symmetric bilinear form on such objects and obeys the extra cyclic constraint. Splits of curvature into 'electric' and 'magnetic' parts exist but are observer-dependent and only loosely analogous. *(DIV ch23 §23.7 p.472)*

## Misconceptions

- **The Riemann tensor carries 256 independent pieces of information in four-dimensional spacetime.** — The pair antisymmetries, pair exchange and the cyclic identity leave only 20 independent components in four dimensions (6 in three, 1 in two). *Why tempting:* A four-index object in four dimensions naively has 4^4 = 256 components. *Diagnostic:* How many independent numbers describe the curvature of a two-dimensional surface at a point, and which component carries it? *(GA ch11 §11.4 p.126)*
- **Symmetries derived in a local inertial frame hold only in that frame.** — They relate components of one tensor under index permutations, which is a tensor equation; once true in one basis it is true in all bases. *Why tempting:* The derivation explicitly used special coordinates in which Γ vanishes at the point. *Diagnostic:* We showed R_αβμν = R_μναβ using coordinates with Γ = 0 at P. Does it hold for Schwarzschild components computed in Schwarzschild coordinates? Why? *(GA ch11 §11.4 p.126; SCH ch06 §6.5 p.158)*
- **The mixed tensor R^α_βμν is antisymmetric in α and β, so its index positions can be ignored when applying the rules.** — First-pair antisymmetry holds only once both indices are at the same level. R^α_βμν and R^β_αμν differ by metric factors: on a sphere of radius a, R^θ_φθφ = sin^2 θ, but R^φ_θθφ = -1, not -sin^2 θ. *Why tempting:* Books state the rules compactly and the mixed tensor is what most calculations produce first. *Diagnostic:* On a sphere of radius a, R^θ_φθφ = sin^2 θ. What are R^φ_θφθ and R^φ_θθφ? *(GA ch36 §36.4 p.382; legacy:manuscript-section-8-4-8-6-flatness-count-sphere-curvature)*
- **All the Riemann symmetries hold for any connection.** — Only last-pair antisymmetry is universal. The cyclic identity needs zero torsion, and first-pair antisymmetry and pair exchange need metric compatibility; for a general symmetric connection R^ρ_ρμν need not vanish. *Why tempting:* General relativity always uses the Levi-Civita connection, so the assumptions are rarely stated. *Diagnostic:* For a torsion-free connection not derived from any metric, which of the four algebraic identities survive? Must R^ρ_ρμν be zero? *(DIV ch06 §6.12 p.105)*
- **Swapping single indices across the two pairs is also a symmetry, for example R_0101 = R_0011.** — Only exchanging whole pairs preserves the value. Moving a single index from one pair to the other is not a symmetry; R_0011 is zero by antisymmetry while R_0101 generally is not. Cross-pair moves are constrained only through the cyclic identity. *Why tempting:* Pair exchange moves indices between positions, which can look like permission to move any index. *Diagnostic:* Is R_0101 equal to R_0011? Is R_0101 equal to R_1010? *(GA ch11 §11.4 p.126; legacy:lab-riemann-independent-components)*
- **Twenty independent Riemann components means twenty independent gravitational-wave polarizations or degrees of freedom.** — Twenty is an algebraic count of curvature values at one event. The field equations constrain them (in vacuum the Ricci part vanishes, leaving the 10 Weyl components), and gravitational waves have only two polarizations. *Why tempting:* Counts of components are often equated with counts of physical freedoms in other field theories. *Diagnostic:* In vacuum, how many of the 20 components remain unconstrained by Einstein's equation at a point, and how many polarizations does a gravitational wave have? *(legacy:manuscript-section-8-4-8-6-flatness-count-sphere-curvature)*

## Thought experiments

- **Resizing and reversing the tiny loop**: Carry a vector around a very small loop, then repeat with one edge doubled, then again traversing the loop in the opposite sense. *Lesson:* The change doubles with the edge and flips sign with the orientation, so it is linear in each edge vector and antisymmetric in their order, which is the last-pair antisymmetry. *(SCH ch06 §6.5 p.157)*

## Visualizations

### Riemann tile board · interactive-2d · high priority

A board of index-pair tiles on which learners watch the symmetries reduce the component count step by step, and then fill the surviving tiles with real values from a chosen metric.

**Interaction:** A dimension selector (2 to 5) sets the board. Phase 1 collapses antisymmetric pairs; phase 2 folds the board along its diagonal and highlights mirror tiles; phase 3 selects any four distinct indices and shows the cyclic relation removing one tile. Clicking a tile shows its value, its mirror partner and the sign flips under reversing either pair. A metric menu (sphere, Schwarzschild, flat FLRW) fills tiles with computed values, and a drag-to-permute tool lets the learner move indices and see whether the value is preserved, flipped or unrelated.

**Model:** All-lower Levi-Civita Riemann tensor in course conventions; canonical labels for (pair, pair) with pair exchange; cyclic constraints for four distinct indices; count n^2(n^2-1)/12; component values from symbolic computation of the chosen metric.

**Inspired by:** GA ch35 Example 35.6; GA ch11 §11.4 p.126; SCH ch06 Exercise 6.18 p.167; legacy:lab-riemann-independent-components

**Legacy assets:** lab-riemann-independent-components

### Loop plane and rotation plane · interactive-3d · medium priority

Make the two index pairs geometric: one plane where a tiny loop is walked, another where the carried vector turns, with orientation reversal and length preservation visible.

**Interaction:** In a curved three-dimensional space the learner draws a small loop in a chosen coordinate plane and picks its orientation; a transported vector returns slightly rotated, with the rotation plane highlighted. Reversing the loop reverses the rotation; the readout confirms that the change is perpendicular to the vector. A matrix panel shows the 3-by-3 table of loop planes against rotation planes and lets the learner test whether entry (A,B) equals entry (B,A).

**Model:** Small-loop holonomy δ V^ρ = -R^ρ_σμν V^σ a^μ b^ν (course convention, route +a,+b,-a,-b) on a three-dimensional Riemannian metric, for example a constant-curvature space R_abcd = K(g_ac g_bd - g_ad g_bc) or an anisotropic metric with computed components.

**Inspired by:** SCH ch06 §6.5 p.157; legacy:manuscript-chapter-08-curvature-holonomy

**Legacy assets:** manuscript-chapter-08-curvature-holonomy

### Symmetry detective · interactive-2d · medium priority

Compute all components of R for a real metric and group them into symmetry classes, so learners predict zeros and equalities before seeing numbers.

**Interaction:** The learner chooses a metric, then for a shown component guesses 'zero', 'equal to', or 'minus' another component; the app reveals the answer and the rule used. A summary view sorts all 256 slots into classes with their shared values.

**Model:** Symbolic Christoffel symbols and Riemann tensor in course conventions for 2D and 4D metrics; classes generated by first-pair antisymmetry, last-pair antisymmetry and pair exchange.

**Inspired by:** GA ch36 Example 36.4; GA ch21 Exercise 21.3

## Worked examples

- **Symmetries from the local-frame formula** (working): Lowering the index in the second-derivative expression makes the three pair rules and the cyclic identity checkable by inspection. *(SCH ch06 §6.5 p.158)*
- **A form that shows the symmetries** (working): Local flatness reduces Riemann to four metric second derivatives, and the symmetry of g and of partials exposes the rules. *(GA ch11 Example 11.5)*
- **Independent components in n dimensions** (working): Counts antisymmetric pairs, symmetric pairs of pairs and cyclic constraints to reach n^2(n^2-1)/12. *(GA ch35 Example 35.6)*
- **Curvature of a sphere with partner components** (working): After one frame component is computed from the curvature 2-form, the symmetries supply its partner, and coordinate and frame components are related. *(GA ch36 Example 36.4)*
- **Contracting the Bianchi identity** (formal): Pair antisymmetries turn two terms into Ricci tensors, giving the divergence of Ricci in terms of the gradient of the scalar curvature. *(GA ch13 Example 13.3)*
- **Explicit chart, symmetry check and count** (working): Course-convention verification of the rules in a constructed Γ-free chart, followed by the 6-by-6 pair count to 20 and the single 2D component. *(legacy:manuscript-section-8-4-8-6-flatness-count-sphere-curvature)*

## Exercises

- (standard) Derive the pair symmetries and cyclic identity from the local-frame formula, reduce 256 components to 21 using pairs, and show the cyclic identity removes exactly one more. *Skill:* Index-pair counting *(SCH ch06 Exercise 6.18 p.167)*
- (standard) Show the Ricci tensor is the only independent contraction of Riemann and that it is symmetric. *Skill:* Using the symmetries in contractions *(SCH ch06 Exercise 6.25 p.167)*
- (standard) Compute the curvature of a unit sphere using the fact that two dimensions allow one independent component. *Skill:* Generating all components from one *(SCH ch06 Exercise 6.29 p.167)*
- (standard) Establish the cyclic identity and pair exchange using geodesic coordinates, and rewrite the cyclic identity with antisymmetrization brackets. *Skill:* Proofs in special coordinates *(DIV ch06 Exercise 6.24 p.110)*
- (standard) Relate Schwarzschild Riemann components with swapped index order and convert them to orthonormal-frame values. *Skill:* Index symmetries with raising and lowering *(GA ch11 Exercise 11.2 p.130)*
- (standard) Use the Riemann symmetries to justify writing Einstein components in an orthonormal frame as sums of plane-type Riemann components. *Skill:* Symmetries in contractions to Ricci and Einstein *(GA ch21 Exercise 21.3)*
- (challenging) Use the cyclic identity to express second covariant derivatives of a Killing vector through curvature acting on the vector. *Skill:* Cyclic identity in applications *(DIV ch07 Exercise 7.15)*

## Checks for understanding

- **Q (intuition):** Without any equations: why should reversing the direction in which you walk around a tiny loop flip the sign of the corresponding curvature component?
  - **A:** Walking the loop backwards undoes the rotation the forward walk produced, so the change in the carried vector is reversed. The last two indices of Riemann name the loop's plane in a definite order, so exchanging them must flip the sign.
- **Q (working):** Which of these vanish without calculation, and how are the others related: R_0012, R_1233, R_0101, R_0110, R_1010, R_0011?
  - **A:** R_0012 = 0 and R_1233 = 0 (repeated index in a pair), and R_0011 = 0 for the same reason. R_0101 is not forced to vanish. R_0110 = -R_0101 (swap in the last pair) and R_1010 = R_0101 (swap in both pairs, or pair exchange). In particular R_0101 is not equal to R_0011, because moving a single index across pairs is not a symmetry. *(targets: Swapping single indices across the two pairs is also a symmetry, for example R_0101 = R_0011.)*
- **Q (working):** For a sphere of radius a, R^θ_φθφ = sin^2 θ. Find R_θφθφ, R^φ_θφθ and R^φ_θθφ.
  - **A:** Lower with g_θθ = a^2: R_θφθφ = a^2 sin^2 θ. By pair exchange R_φθφθ = a^2 sin^2 θ, so R^φ_θφθ = g^φφ R_φθφθ = (1/(a^2 sin^2 θ)) a^2 sin^2 θ = 1. By last-pair antisymmetry R^φ_θθφ = -1. Naively swapping the upper and first lower index of the mixed component would wrongly give -sin^2 θ. *(targets: The mixed tensor R^α_βμν is antisymmetric in α and β, so its index positions can be ignored when applying the rules.)*
- **Q (formal):** Prove first-pair antisymmetry for the Levi-Civita connection using the Ricci identity and ∇ g = 0.
  - **A:** Apply the commutator to the (0,2) tensor g_αβ: [∇_μ, ∇_ν] g_αβ = -R^λ_αμν g_λβ - R^λ_βμν g_αλ. The left side is zero because ∇ g = 0. Lowering gives -R_βαμν - R_αβμν = 0, so R_αβμν = -R_βαμν. *(targets: All the Riemann symmetries hold for any connection.)*
- **Q (formal):** Count the independent components of Riemann in three dimensions from the symmetries, and explain why in three dimensions the Ricci tensor determines Riemann completely.
  - **A:** Antisymmetric pairs: N = 3 (12, 13, 23). Pair exchange gives a symmetric 3-by-3 array: 6 components. With only three index values there is no set of four distinct indices, so the cyclic identity adds no constraint: 6 remain, matching n^2(n^2-1)/12 = 6. The Ricci tensor is a symmetric 3-by-3 matrix with 6 components and, because the contraction map is invertible in three dimensions, Riemann can be rebuilt from Ricci and the metric. *(targets: The Riemann tensor carries 256 independent pieces of information in four-dimensional spacetime.)*

## Applications

- **Saving work in curvature calculations**: For a spherically symmetric spacetime one computes a handful of plane components and fills in the rest by symmetry, which is the standard workflow for Schwarzschild and stellar interiors. Key numbers: 4D: 20 independent components out of 256 slots. *(GA ch36 Example 36.4; GA ch11 Exercise 11.2 p.130)*
- **Structure of the field equations**: The symmetries make the Ricci tensor symmetric, so the Einstein tensor is a symmetric tensor that can be equated to the symmetric stress-energy tensor, and the contracted Bianchi identity follows cleanly. *(GA ch13 Example 13.3; GA ch11 §11.5 p.127)*
- **Algebraic classification of spacetimes**: Treating Riemann or Weyl as a symmetric matrix on six-dimensional bivector space underlies the Petrov classification of gravitational fields. Key numbers: Weyl tensor: 10 independent components in 4D. *(DIV ch23 §23.7 p.472)*

## Tutor guidance

**Opening questions**

- How many components would you expect a quantity with four indices to have in four dimensions? Does curvature plausibly need that many?
- If you walk around a small loop the opposite way, what should happen to the change in a carried arrow?
- When an arrow is parallel transported it keeps its length. What kind of matrix describes a small change that keeps length?

**Common questions**

- *Why must the first index be lowered before the rules apply?* — First-pair antisymmetry expresses that the loop change is a rotation, which is an antisymmetric matrix only when both of its indices are at the same level. With one index up, the metric enters and the simple sign rule fails.
- *Is pair exchange an independent assumption?* — No. For the Levi-Civita connection it follows from the two antisymmetries plus the cyclic identity, though it is easiest to see directly in the normal-coordinate formula.
- *Why does the cyclic identity remove only one component in four dimensions?* — With the other symmetries, it only adds a new condition when all four indices are different, and in four dimensions there is just one such set, 0123.
- *Do the symmetries change with the sign convention or signature?* — No. Conventions can flip the overall sign of R or of its lowered components, but every symmetry relation is homogeneous, so it survives unchanged.
- *What do the diagonal entries of the six-by-six table mean?* — An entry like R_1212 pairs a plane with itself; divided by the squared area of that plane it is the sectional curvature, the Gaussian curvature of the surface swept out by geodesics in that plane.

**Pitfalls when explaining**

- Always say 'with all indices lowered' when stating the rules.
- Do not present pair exchange as swapping individual indices; it exchanges whole pairs.
- Name the assumptions: metric compatibility for first-pair antisymmetry, zero torsion for the cyclic identity.
- Avoid calling the cyclic identity simply 'the Bianchi identity' without qualification, since the differential Bianchi identity is a different statement.
- When quoting numbers from d'Inverno, remember lowered components carry the opposite sign because of the signature.
- Keep the algebraic count of 20 separate from physical degrees of freedom and polarizations.

**When to show a demo**

- When the count 256 comes up, open the tile board at phase 1 and let the learner collapse it.
- When the learner asks why the first pair is antisymmetric, show the loop-and-rotation demo with the length readout.
- After computing one sphere component, use the symmetry detective to predict the rest before revealing them.

**Saying it aloud:** State the rules in words: 'with all indices down, swapping the first two indices flips the sign, swapping the last two flips the sign, and swapping the first pair with the last pair changes nothing.' Then the symbols: 'R alpha beta mu nu equals minus R beta alpha mu nu, equals minus R alpha beta nu mu, equals R mu nu alpha beta.' For the cyclic identity say 'keep the first index fixed, cycle the other three, and the three terms add to zero.' For the count say 'six planes, a symmetric six-by-six table gives twenty-one, and the cyclic identity takes away one, leaving twenty.'

## Sources

- schutz ch06 (core): p.158 §6.5, p.159 §6.5
- gifted-amateur ch11 (core): p.126 §11.4, p.127 §11.5
- gifted-amateur ch13 (mention): p.146 §13.3
- gifted-amateur ch35 (revisited): p.369 §35.3, p.370 §35.3
- gifted-amateur ch36 (revisited): p.382 §36.4, p.383 §36.4
- dinverno ch06 (core): p.105 §6.12, p.106 §6.12
- legacy manuscript-section-8-4-8-6-flatness-count-sphere-curvature (developed)
- legacy lab-riemann-independent-components (developed)

## Review

**Verdict:** fixed

**Fixes**

- Misconception 'mixed tensor is antisymmetric in α and β': the correction compared R^θ_φθφ with R^φ_θφθ, a pair-exchanged component that does not test first-pair antisymmetry. It now compares R^θ_φθφ = sin²θ with R^φ_θθφ = −1, the component the naive rule would call −sin²θ.
- Key equation 'first-pair antisymmetry from metric compatibility': neither book proves the rule this way, so the meaning now says the proof is the course's own. The d'Inverno ref points to metric compatibility, eq. 6.74 (DIV ch06 §6.10 p.104), instead of §6.12, and the legacy ref was added.
- Key equation 'two-dimensional Riemann tensor': GA ch11 has no displayed K(gg − gg) formula at §11.4 p.127. The ref now points to GA ch11 Example 11.6 p.127 (a single independent component in 2D). The K form is supported by GA ch36 Example 36.4 and the legacy section.

**Concerns**

- Checked every convention row against the dossiers: Schutz eqs. 6.69 and 6.70, GA eqns 11.24 and 11.25, and d'Inverno eqs. 6.78-6.82 with the order of their proofs. Also checked each check-for-understanding answer (sphere components, the 3D count, the metric-commutator proof, vanishing components), the formal dimension count, the trace R^ρ_ρμν for non-metric connections, and the invariance of the symmetry relations under g → −g.
- The exercise refs GA ch21 Exercise 21.3 and DIV ch07 Exercise 7.15 have no page number. DIV ch06 Exercise 6.24 was confirmed on printed p.110.
- The prerequisites covariance-of-tensor-equations and metric-compatibility go beyond the registry entry, and the registry was not updated.
