---
type: "concept"
id: "cyclic-identity"
title: "Cyclic (first Bianchi) identity"
domain: "curvature"
tier: "core"
aliases: ["first Bianchi identity", "algebraic Bianchi identity", "R^a_[bcd] = 0"]
prerequisites: ["symmetries-of-the-riemann-tensor", "torsion-free-connection"]
leads_to: ["number-of-independent-riemann-components", "weyl-tensor", "killing-vector-ricci-identity", "sectional-curvature"]
sources: ["dinverno:ch06", "gifted-amateur:ch11", "gifted-amateur:ch35", "legacy:lab-riemann-independent-components", "schutz:ch06"]
review: "fixed"
---

# Cyclic (first Bianchi) identity

> Hold the first index of the Riemann tensor fixed and run the other three through their three cyclic orders: the three components always add up to zero. This is automatic for any connection without torsion, and once the pair symmetries are in place it only says something new when all four indices are different, which in four dimensions removes exactly one component and leaves twenty.

## Explanations by level

### Intuition

Think of curvature as a rule that says how much a tiny loop turns a direction you carry around it. Now take a tiny box and look at one corner, where three edges meet. Each pair of edges makes a face, and the third edge is left over. Carry the left-over edge direction around its face, and do this for all three faces, always going round in the same cyclic order. The cyclic identity says the three small changes cancel exactly. It holds because, in the geometry used by general relativity, tiny parallelograms close up (no torsion). The simplification here: the identity is a statement about the curvature numbers at one point, not something you would measure with a single experiment, and in the count of curvature numbers for four-dimensional spacetime it removes just one of the twenty-one that the other symmetries leave, although it is also used behind the scenes in several later results.

**Picture to hold:** Three faces of a small box meeting at a corner; around each face you carry the direction of the edge that is not part of that face, and the three turn-changes sum to nothing.

**Assumes:** [[holonomy]], [[torsion-free-connection]]

### Working

With the course convention the Riemann tensor R^ρ_σμν has the transported vector in slot σ and the loop directions in slots μ and ν. The identity is R^ρ_σμν + R^ρ_μνσ + R^ρ_νσμ = 0, compactly R^ρ_[σμν] = 0. Two quick proofs. (1) From the definition: the derivative terms pair up as ∂_μΓ^ρ_νσ against ∂_μΓ^ρ_σν, and so on, and cancel because the Christoffel symbols are symmetric in their lower indices; the six quadratic terms cancel in pairs for the same reason. No metric is used, so any torsion-free connection obeys it. (2) In normal coordinates at a point P the lowered tensor is R_ρσμν = ½(∂_σ∂_μ g_ρν − ∂_σ∂_ν g_ρμ + ∂_ρ∂_ν g_σμ − ∂_ρ∂_μ g_σν); cycling σ, μ, ν gives twelve terms that cancel in pairs by symmetry of g and of mixed partials, and since both sides are tensors the result holds in every coordinate system. When does it matter? If two of the four indices coincide, the pair symmetries already force the cyclic sum to vanish, so it is a genuinely new condition only for four distinct index values. In four dimensions that is the single relation R_0123 + R_0231 + R_0312 = 0 (equivalently R_0123 − R_0213 + R_0312 = 0), which takes the pair-symmetry count of 21 down to 20. Unlike the pair symmetries, which identify components up to sign, this is a linear relation among three different components.

**Picture to hold:** An index wheel: the first slot is pinned, the other three slots rotate one click at a time, and the three readings sum to zero.

**Assumes:** [[symmetries-of-the-riemann-tensor]], [[riemann-tensor-in-normal-coordinates]], [[torsion-free-connection]]

### Formal

Let ∇ be an affine connection with torsion T(u,v) = ∇_u v − ∇_v u − [u,v] and curvature operator R(u,v) = [∇_u, ∇_v] − ∇_[u,v]. For all vector fields u, v, w the first Bianchi identity reads 𝔖 R(u,v)w = 𝔖 [T(T(u,v),w) + (∇_u T)(v,w)], where 𝔖 is the sum over cyclic permutations of (u,v,w). For a torsion-free connection the right side vanishes and R(u,v)w + R(v,w)u + R(w,u)v = 0; the proof expands the left side, uses ∇_v w − ∇_w v = [v,w], and reduces it to the Jacobi identity of the Lie bracket. In components, with R(e_μ,e_ν)e_σ = R^ρ_σμν e_ρ, this is R^ρ_[σμν] = 0. For the Levi-Civita connection, lowering the index and combining with antisymmetry in each pair and pair exchange gives the equivalent statements R_ρ[σμν] = 0 and R_[ρσμν] = 0: the space of tensors with the pair symmetries, Sym²(Λ²V) of dimension M(M+1)/2 with M = n(n−1)/2, splits as the algebraic curvature tensors plus Λ⁴V, and the cyclic identity removes the Λ⁴V part of dimension C(n,4). In four dimensions this is the single scalar condition ε^ρσμν R_ρσμν = 0. In the language of forms, the torsion-free first structure equation dθ^a + ω^a_b ∧ θ^b = 0, differentiated once, gives Ω^a_b ∧ θ^b = 0. The identity is algebraic and pointwise; it should not be confused with the differential Bianchi identity ∇_[λ R_ρσ]μν = 0.

**Assumes:** [[torsion-tensor]], [[riemann-curvature-operator]], [[symmetries-of-the-riemann-tensor]], [[lie-bracket]]

## Prerequisites

- [[symmetries-of-the-riemann-tensor]] — The identity is only meaningful, and its reach (four distinct indices) only visible, once antisymmetry in each pair and pair exchange are known.
- [[torsion-free-connection]] — The identity holds exactly because the connection is symmetric in its lower indices; with torsion extra terms appear.

## Leads to

- [[number-of-independent-riemann-components]] — It supplies the final constraint that turns 21 into 20 in four dimensions and C(n,4) constraints in n dimensions.
- [[weyl-tensor]] — The Weyl tensor inherits the cyclic identity, which is part of what makes it a legitimate curvature-like tensor.
- [[killing-vector-ricci-identity]] — The formula expressing second derivatives of a Killing vector through curvature is derived with the cyclic identity.
- [[sectional-curvature]] — Recovering the whole Riemann tensor from sectional curvatures of all planes relies on the cyclic identity.

## Related

- [[bianchi-identity]] — The differential (second) Bianchi identity is a different, derivative statement; learners often mix the two names.
- [[torsion-tensor]] — With torsion the cyclic sum equals torsion terms instead of zero.
- [[cartan-first-structure-equation]] — Differentiating the torsion-free structure equation gives the forms version Ω^a_b ∧ θ^b = 0.
- [[maxwell-equations-in-differential-forms]] — The electromagnetic cyclic identity dF = 0 is automatic for the same kind of reason: it follows from how the field is built.
- [[riemann-tensor-in-normal-coordinates]] — The quickest proof reads the identity off the second-derivative form of Riemann at a point.

## Key equations

### Cyclic identity (mixed components)

$$
R^\rho{}_{\sigma\mu\nu} + R^\rho{}_{\mu\nu\sigma} + R^\rho{}_{\nu\sigma\mu} = 0 \quad\Longleftrightarrow\quad R^\rho{}_{[\sigma\mu\nu]} = 0
$$

With the upper index fixed, summing over the three cyclic orders of the lower indices gives zero; true for any torsion-free connection. *(SCH ch06 §6.5 p.158; GA ch11 §11.4 p.126; DIV ch06 §6.12 p.106)*

**Convention:** Course slot order: sigma is the transported vector, mu and nu the loop directions. Schutz, Blundell-Lancaster and d'Inverno use the same slots and sign, so their forms translate by renaming only.

### Cyclic identity (all indices lowered)

$$
R_{\rho\sigma\mu\nu} + R_{\rho\mu\nu\sigma} + R_{\rho\nu\sigma\mu} = 0 \quad\Longleftrightarrow\quad R_{[\rho\sigma\mu\nu]} = 0
$$

The same identity with the first index lowered; together with the pair symmetries it is equivalent to the vanishing of the totally antisymmetric part. *(SCH ch06 §6.5 p.158; GA ch35 §35.3 p.369; DIV ch06 §6.12 p.106)*

**Convention:** Equivalence with the total antisymmetrization uses the pair symmetries, so it needs the metric (Levi-Civita) connection.

### Riemann tensor in normal coordinates (proof tool)

$$
R_{\rho\sigma\mu\nu}\big|_P = \tfrac12\left(\partial_\sigma\partial_\mu g_{\rho\nu} - \partial_\sigma\partial_\nu g_{\rho\mu} + \partial_\rho\partial_\nu g_{\sigma\mu} - \partial_\rho\partial_\mu g_{\sigma\nu}\right)
$$

Where the Christoffel symbols vanish, curvature is four second derivatives of the metric; cycling the last three indices makes the twelve terms cancel in pairs. *(SCH ch06 §6.5 p.158; GA ch11 Example 11.5; legacy:manuscript-section-8-4-8-6-flatness-count-sphere-curvature)*

**Convention:** Valid only in coordinates with Gamma = 0 at P; the cyclic identity derived from it is a tensor equation and holds everywhere.

### The one new relation in four dimensions

$$
R_{0123} + R_{0231} + R_{0312} = 0
$$

After the pair symmetries, the only components with four distinct indices are these three (up to sign); the identity ties them, reducing 21 to 20. *(SCH ch06 Ex 6.18 p.167; legacy:lab-riemann-independent-components)*

**Convention:** The legacy lab writes it as R_0123 - R_0213 + R_0312 = 0, which is the same relation because R_0213 = -R_0231.

### Index-free form

$$
\mathcal{R}(u,v)w + \mathcal{R}(v,w)u + \mathcal{R}(w,u)v = 0, \qquad \mathcal{R}(u,v) = [\nabla_u,\nabla_v] - \nabla_{[u,v]}
$$

Carry each of three directions around the small loop spanned by the other two, in cyclic order; the three changes cancel. *(legacy:manuscript-chapter-08-curvature-holonomy)*

**Convention:** Components: R(e_mu, e_nu) e_sigma = R^rho_{sigma mu nu} e_rho.

### First Bianchi identity with torsion (formal)

$$
\mathfrak{S}_{u,v,w}\, \mathcal{R}(u,v)w = \mathfrak{S}_{u,v,w}\left[T(T(u,v),w) + (\nabla_u T)(v,w)\right]
$$

For a general connection the cyclic sum is built from the torsion and its derivative; setting T = 0 recovers the course identity.

**Convention:** T(u,v) = nabla_u v - nabla_v u - [u,v]; the cyclic symbol sums over the three cyclic orders of (u,v,w). None of the three books treats torsion here.

## Conventions across the books

| Issue | Schutz | Gifted Amateur | d'Inverno | Course choice |
| --- | --- | --- | --- | --- |
| Riemann slot order and overall sign (decides which three indices are cycled) | R^α_βμν = Γ^α_βν,μ − Γ^α_βμ,ν + Γ^α_σμ Γ^σ_βν − Γ^α_σν Γ^σ_βμ; slot β is the transported vector (MTW convention). Cyclic sum over the last three lower indices. | Same slots and sign as MTW (GA ch11 §11.3, ch35 §35.1): second slot takes the vector, last two the loop directions. | R^a_bcd = ∂_c Γ^a_bd − ∂_d Γ^a_bc + ..., with [∇_c, ∇_d] X^a = R^a_bcd X^b; same slots as MTW. | R^ρ_σμν with [∇_μ, ∇_ν] V^ρ = R^ρ_σμν V^σ; the identity cycles σ, μ, ν. A book that put the transported index last would cycle the first three lower indices instead; always check before copying the pattern. |
| Written form of the identity | All indices lowered: R_αβμν + R_ανβμ + R_αμνβ = 0 (Eq. 6.70), listed next to the pair symmetries (6.69). | All indices lowered: R_αβγδ + R_αδβγ + R_αγδβ = 0 (Eqs. 11.25, 35.31, 35.33). | Mixed, with the identity sign: R^a_bcd + R^a_dbc + R^a_cdb ≡ 0 (6.79), bracket form R^a_[bcd] ≡ 0 (Exercise 6.24); a lowered version appears with the pair symmetries after (6.82). | State it as R^ρ_[σμν] = 0 and write it out as R^ρ_σμν + R^ρ_μνσ + R^ρ_νσμ = 0; use the plain equals sign and say in words that it holds for every torsion-free connection. |
| Name | 'Cyclic identity'; the name 'Bianchi identities' is kept for the differential identities of §6.6. | 'Cyclic identity' (no Bianchi name in ch11 or ch35); 'Bianchi identity' is the differential identity of ch13 (Eq. 13.27). | Stated as an unnamed identity (6.79) derived from the symmetry of the connection; 'Bianchi identities' means the differential identities (6.83). | Call it the cyclic identity, with alias first (algebraic) Bianchi identity; 'Bianchi identity' on its own always means the differential one. |
| Lower-index order of the Christoffel symbols (invisible without torsion) | Derivative index last: V^α_;β = V^α_,β + Γ^α_μβ V^μ. | Derivative index first: ∇_μ e_ν = Γ^α_μν e_α (GA ch35 §35.2). | Derivative index last: ∇_c X^a = ∂_c X^a + Γ^a_bc X^b. | Derivative index first, ∇_μ V^ν = ∂_μ V^ν + Γ^ν_μλ V^λ. For the symmetric connections of GR the order does not matter; it matters only when torsion terms are added to the identity. |
| Metric signature (sign of the lowered tensor) | (−,+,+,+). | (−,+,+,+). | (+,−,−,−); flipping the metric flips the sign of R_abcd but not of R^a_bcd. | (−,+,+,+). The identity is linear and homogeneous, so a signature change never affects it. |

## How the sources teach it

### schutz

**Route:** After defining Riemann from a small loop, Schutz goes to a locally inertial frame, writes the lowered tensor as four second derivatives of the metric (6.68), and reads off the pair symmetries and the cyclic identity by inspection. He argues that as tensor equations proved in one frame they hold in all, then states that together they leave 20 components, matching the 20 second derivatives no coordinate change can remove.

**Representation:** Component formulas in locally flat coordinates; verification and the count left to Exercise 6.18.

**Strengths:** Very economical: one formula makes every algebraic symmetry visible, and the link to the local-flatness count gives the identity a purpose.

**Weaknesses:** No geometric meaning and no statement that the identity rests on zero torsion. It does not show which index patterns make the identity trivial; that is buried in the exercise. *(SCH ch06 §6.5 p.158; SCH ch06 §6.5 p.159; SCH ch06 Ex 6.18 p.167)*

### gifted-amateur

**Route:** Chapter 11 uses the local-inertial-frame formula for Riemann (Example 11.5), lists the pair symmetries with a spoken rule for sign changes, and adds the cyclic identity as something one can check. Chapter 35 recalls it as the source of the constraints subtracted in the general-n component count, noting that only four distinct indices give a new condition.

**Representation:** Component formulas, a margin note on the 256 naive components, and a combinatorial argument in Example 35.6.

**Strengths:** Gentle entry, and the ch35 remark about distinct indices is exactly the insight learners need for counting.

**Weaknesses:** The check is not written out, the torsion-free assumption is left implicit, and the later count does not explain why each set of four indices gives exactly one independent relation. *(GA ch11 §11.4 p.126; GA ch11 Example 11.5; GA ch35 §35.3 p.369; GA ch35 Example 35.6)*

### dinverno

**Route:** Section 6.12 derives the identity (6.79) from the symmetry of the connection before any index is lowered, then uses geodesic coordinates for pair exchange and deduces first-pair antisymmetry. It collects all four algebraic identities in (6.82) and states the n^2(n^2−1)/12 count. Exercise 6.24 asks for the proof and the bracket form. The identity returns for the Weyl tensor and in the Killing-vector identity.

**Representation:** Index calculus with the triple-bar identity sign and antisymmetrization brackets.

**Strengths:** Makes clear which property needs only a torsion-free connection (cyclic identity, last-pair antisymmetry) and which needs the metric (pair exchange, first-pair antisymmetry). The bracket notation prepares for forms.

**Weaknesses:** Terse: the proof is an exercise and there is no picture or count of how many relations the identity actually imposes. *(DIV ch06 §6.12 p.106; DIV ch06 Ex 6.24 p.110; DIV ch07 Ex 7.15; DIV ch23 §23.7 p.472)*

### legacy

**Route:** Chapter 8 proves the Riemann symmetries in explicitly constructed Γ = 0 coordinates. The three-phase component lab then pairs the indices into a 6x6 grid, matches mirror entries to reach 21, and in phase 3 highlights the single cyclic relation that brings the count to 20.

**Representation:** Interactive tile grid with named components and sign rules; a static pair-matrix figure.

**Strengths:** Makes the cyclic relation a visible, located object in the component grid and separates it clearly from the pair symmetries. Conventions are verified exhaustively over all 256 index choices.

**Weaknesses:** Numbering gaps and inconsistent colours in phase 3. The static figure does not locate the cyclic relation. There is no geometric reading and no dimension selector. *(legacy:lab-riemann-independent-components; legacy:figure-curvature-count; legacy:manuscript-chapter-08-curvature-holonomy)*

## Recommended teaching path

1. **Pose the leftover question** — After the pair symmetries, show the three components with indices 0,1,2,3 in different arrangements, R_0123, R_0231, R_0312, and ask whether all three are free numbers. *Why:* Gives the identity a job before it is stated, and focuses attention on the only index pattern where it matters. *(SCH ch06 Ex 6.18 p.167; GA ch35 Example 35.6)*
2. **Picture the three faces** — Draw a small box corner: transport each edge direction around the face made by the other two, in cyclic order, and assert the three changes cancel when there is no torsion. *Why:* Connects the identity to the loop meaning of curvature that the learner already holds, so it is not just index juggling. *(legacy:manuscript-chapter-08-curvature-holonomy)*
3. **Prove it the quick way** — In normal coordinates write the four-term second-derivative form and let the learner cancel the twelve terms of the cyclic sum pair by pair; stress that a tensor equation true in one chart is true in all. *Why:* A short, checkable derivation that reuses the tool already used for the pair symmetries. *(SCH ch06 §6.5 p.158; GA ch11 Example 11.5)*
4. **Locate the real assumption** — Redo the proof straight from the Christoffel definition, showing each cancellation uses Γ^ρ_μν = Γ^ρ_νμ and no metric; mention that torsion would leave extra terms. *Why:* Prevents the belief that the identity is a property of all connections, and separates it from the pair symmetries that need the metric. *(DIV ch06 §6.12 p.106; DIV ch06 Ex 6.24 p.110)*
5. **Check which index patterns matter** — Have the learner test a repeated-index case (for example R_1123 + R_1231 + R_1312) and see it vanish by pair symmetries alone, then contrast with four distinct indices. *Why:* Establishes that the identity adds one condition per set of four distinct indices, the fact the component count needs. *(GA ch35 §35.3 p.369; legacy:lab-riemann-independent-components)*
6. **Cash it in** — Use it to go from 21 to 20 in four dimensions and to C(n,4) constraints in n dimensions, and note the four-dimensional form ε^ρσμν R_ρσμν = 0; preview its later use for Killing vectors and the Weyl tensor. *Why:* Shows the identity's consequences immediately so it is remembered as useful rather than decorative. *(SCH ch06 §6.5 p.159; DIV ch07 Ex 7.15; DIV ch23 §23.7 p.472)*

## Analogies

- **The Jacobi identity for cross products** (working): For ordinary vectors, a×(b×c) + b×(c×a) + c×(a×b) = 0: a cyclic sum of a two-slot operation acting on the third vector vanishes. The cyclic identity has the same shape, with the curvature of the plane spanned by two directions acting on the third, and its proof in index-free form literally reduces to the Jacobi identity of the Lie bracket. *Limits:* The cross product is an algebraic operation on fixed vectors in flat 3-space; curvature is a tensor field defined through derivatives, exists in any dimension and depends on the connection. The analogy explains the pattern, not why it holds.
- **Three faces of a small box** (intuition): At a corner of a tiny box, carry each edge direction around the face formed by the other two edges, going round in cyclic order. The three changes produced by curvature cancel. Tiny parallelograms closing up (no torsion) is what makes this bookkeeping come out even. *Limits:* Only meaningful for infinitesimal loops of matching size at one point, and the individual changes are not separately measurable in the picture. With torsion the faces do not close and the cancellation fails. *(legacy:manuscript-chapter-08-curvature-holonomy)*
- **The homogeneous Maxwell equations are automatic** (working): If the field strength comes from a potential, the cyclic sum of its derivatives vanishes without any physics input. Likewise the cyclic sum of Riemann vanishes automatically because Riemann is built from a symmetric connection. Both are identities that follow from how the object is constructed. *Limits:* The electromagnetic identity involves derivatives, and in the gauge-theory dictionary it corresponds to the differential Bianchi identity, not to this algebraic one. Use it only to convey 'true by construction'. *(GA ch42 §42.2 p.456)*

## Misconceptions

- **The cyclic identity and the Bianchi identity are the same thing.** — The cyclic identity is algebraic, involves no derivatives and holds pointwise. The (second) Bianchi identity is a differential statement, a cyclic sum of covariant derivatives of Riemann, and is the one that leads to the divergence-free Einstein tensor. *Why tempting:* Both are cyclic sums that vanish and some texts call both 'Bianchi identities'. *Diagnostic:* Which of the two identities would still hold if you only knew the Riemann tensor at a single point, with no information about its neighbourhood? *(SCH ch06 §6.5 p.158; GA ch13 §13.3 p.146; DIV ch06 §6.12 p.106)*
- **Any sum of three index rearrangements works, for example R_0123 + R_0213 + R_0312 = 0.** — Only the cyclic orders of the last three indices are summed: (123), (231), (312). The arrangement 213 is an odd permutation, and R_0213 = −R_0231, so the proposed sum equals −2R_0231, which need not vanish. *Why tempting:* The indices look similar and an unnoticed transposition changes a sign. *Diagnostic:* Rewrite R_0123 + R_0213 + R_0312 using only the three cyclic arrangements. Is it zero? *(legacy:lab-riemann-independent-components)*
- **The cyclic identity follows from the pair symmetries and adds no information.** — It is independent of them. It is automatic when two indices coincide, but for four distinct indices it is a genuine new linear relation, removing C(n,4) components: one in four dimensions. *Why tempting:* In every low-dimensional or repeated-index example the identity checks out trivially, and in three dimensions it imposes nothing. *Diagnostic:* In three dimensions the cyclic identity removes no components, but in four it removes one. What property of the index values explains the difference? *(GA ch35 §35.3 p.369; SCH ch06 Ex 6.18 p.167)*
- **The cyclic identity is a symmetry that makes components equal up to sign, like the pair symmetries.** — Pair symmetries identify components in pairs; the cyclic identity is a linear relation among three different components, so it lets one be expressed as a combination of the other two. *Why tempting:* It is listed together with the symmetries and all are loosely called 'symmetries'. *Diagnostic:* If R_0123 = 2 and R_0231 = 5 at some point, what is R_0312, and is it simply ± one of the others? *(legacy:lab-riemann-independent-components; GA ch11 §11.4 p.126)*
- **Every connection satisfies the cyclic identity.** — It requires zero torsion. For a connection with torsion the cyclic sum equals terms built from the torsion and its covariant derivative. *Why tempting:* General relativity always uses the torsion-free Levi-Civita connection, so the assumption is never visible. *Diagnostic:* In the proof from the Christoffel formula, which single property of Γ is used to cancel every term? *(DIV ch06 §6.12 p.106)*

## Visualizations

### Index wheel on a live curvature tensor · interactive-2d · high priority

A ring with the first index pinned and three rotating slots; each click lights the corresponding tile in a 6x6 pair grid of a real Riemann tensor, shows its signed value, and keeps a running cyclic sum that always returns to zero.

**Interaction:** Choose the four index values (including repeats); rotate the wheel; press 'new random geometry'; toggle 'add torsion' to see the sum become nonzero; toggle 'wrong permutation' to see the sign error from swapping two slots.

**Model:** Draw random second derivatives of a 4D metric at a point and build R_ρσμν from the normal-coordinate formula; for the torsion toggle build R^ρ_σμν from a connection with an antisymmetric part using the course definition. Sums are exact in floating point.

**Inspired by:** SCH ch06 §6.5 p.158; GA ch11 Example 11.5; legacy:lab-riemann-independent-components

**Legacy assets:** lab-riemann-independent-components, figure-curvature-count

### Twelve terms cancelling · animated-2d · medium priority

The cyclic sum written in normal coordinates appears as twelve coloured second-derivative chips; matching chips (equal by symmetry of g or of mixed partials) glide together and annihilate.

**Interaction:** Step through cancellations one at a time or let them play; tap a chip to see which symmetry justifies its partner.

**Model:** Symbolic: the three copies of the four-term formula with σ, μ, ν cycled; pairing rules g_ab = g_ba and ∂_a∂_b = ∂_b∂_a.

**Inspired by:** SCH ch06 Ex 6.18 p.167; DIV ch06 Ex 6.24 p.110

### Three faces of a box · interactive-3d · medium priority

A small cube in a curved 3D space; for each face adjacent to a chosen corner, the leftover edge vector is parallel transported around the face and its change drawn as a short red arrow at the corner. The three red arrows add head-to-tail to zero.

**Interaction:** Rotate the cube, change its orientation relative to the curvature, and switch between a torsion-free connection and one with torsion (the arrows then fail to close).

**Model:** Constant-curvature 3-space or a random algebraic curvature tensor; changes computed to leading order as −R(u,v)w ε² for each face.

**Inspired by:** legacy:manuscript-chapter-08-curvature-holonomy

**Legacy assets:** manuscript-chapter-08-curvature-holonomy

## Worked examples

- **Riemann symmetries from the locally inertial form** (working): Lowered Riemann as four second derivatives of the metric at a point, from which the pair symmetries and the cyclic identity are read off and promoted to all frames. *(SCH ch06 §6.5 p.158)*
- **Example 11.5: a form of Riemann that shows its symmetries** (working): The same local-inertial-frame route, with a spoken rule for the sign changes and the cyclic identity stated as checkable. *(GA ch11 Example 11.5)*
- **Cyclic identity from a symmetric connection** (formal): The identity stated for R^a_bcd before lowering, as a consequence of the symmetry of the connection, with the bracket form R^a_[bcd] = 0. *(DIV ch06 §6.12 p.106)*
- **Example 35.6: the cyclic constraints in the component count** (working): The identity used as C(n,4) constraints, relevant only for four distinct indices. *(GA ch35 Example 35.6)*

## Exercises

- (standard) Derive the pair symmetries and the cyclic identity from the locally inertial form of Riemann, then show the cyclic identity adds exactly one relation beyond the pair symmetries in four dimensions. *Skill:* Index manipulation and constraint counting *(SCH ch06 Ex 6.18 p.167)*
- (standard) Prove the cyclic identity and pair exchange symmetry using geodesic coordinates, and show the cyclic identity is equivalent to the vanishing of the antisymmetrized lower indices. *Skill:* Proofs with special coordinates and antisymmetrization brackets *(DIV ch06 Ex 6.24 p.110)*
- (challenging) Use the cyclic identity to show that second covariant derivatives of a Killing vector are determined by the curvature acting on the vector. *Skill:* Applying the identity in a derivation *(DIV ch07 Ex 7.15)*

## Checks for understanding

- **Q (intuition):** Why does the cyclic identity remove no components in three dimensions, but one in four?
  - **A:** The identity is automatically satisfied whenever two of the four indices coincide, because the pair symmetries already force the cyclic sum to zero. A new condition appears only for four distinct index values. In three dimensions there are no four distinct values, so nothing is removed; in four there is exactly one set {0,1,2,3}, so one component is removed (21 → 20). *(targets: The cyclic identity follows from the pair symmetries and adds no information.)*
- **Q (working):** A classmate writes the four-dimensional cyclic identity as R_0123 + R_0213 + R_0312 = 0. Is this right?
  - **A:** No. The cyclic orders of (1,2,3) are (1,2,3), (2,3,1), (3,1,2), so the identity is R_0123 + R_0231 + R_0312 = 0. Because R_0213 = −R_0231 (antisymmetry in the last pair), the classmate's sum equals (R_0123 + R_0231 + R_0312) − 2R_0231 = −2R_0231, which is generally nonzero. A correct alternative form is R_0123 − R_0213 + R_0312 = 0. *(targets: Any sum of three index rearrangements works, for example R_0123 + R_0213 + R_0312 = 0.)*
- **Q (working):** Show that R_1123 + R_1231 + R_1312 = 0 follows from the pair symmetries alone.
  - **A:** R_1123 = 0 because the first pair is antisymmetric and both indices are 1. By pair exchange R_1312 = R_1213, and by antisymmetry in the last pair R_1213 = −R_1231. So the sum is 0 + R_1231 − R_1231 = 0, without using the cyclic identity.
- **Q (formal):** Using R^ρ_σμν = ∂_μΓ^ρ_νσ − ∂_νΓ^ρ_μσ + Γ^ρ_μλΓ^λ_νσ − Γ^ρ_νλΓ^λ_μσ, show that the cyclic sum over (σ,μ,ν) vanishes when Γ is symmetric in its lower indices. Where would the proof fail with torsion?
  - **A:** The three cyclic copies contribute derivative terms ∂_μΓ^ρ_νσ − ∂_νΓ^ρ_μσ + ∂_νΓ^ρ_σμ − ∂_σΓ^ρ_νμ + ∂_σΓ^ρ_μν − ∂_μΓ^ρ_σν. Pair ∂_μΓ^ρ_νσ with −∂_μΓ^ρ_σν, −∂_νΓ^ρ_μσ with ∂_νΓ^ρ_σμ, and −∂_σΓ^ρ_νμ with ∂_σΓ^ρ_μν: each pair cancels if Γ^ρ_ab = Γ^ρ_ba. The quadratic terms Γ^ρ_μλΓ^λ_νσ − Γ^ρ_νλΓ^λ_μσ + Γ^ρ_νλΓ^λ_σμ − Γ^ρ_σλΓ^λ_νμ + Γ^ρ_σλΓ^λ_μν − Γ^ρ_μλΓ^λ_σν cancel in the same way (first with sixth, second with third, fourth with fifth). With torsion the lower indices cannot be swapped, each pair leaves a difference proportional to the torsion, and the sum becomes torsion terms instead of zero. *(targets: Every connection satisfies the cyclic identity.)*
- **Q (formal):** In four dimensions, show that given the pair symmetries the cyclic identity is equivalent to ε^ρσμν R_ρσμν = 0.
  - **A:** Only components with four distinct indices survive the contraction. Each is related by the pair symmetries to one of R_0123, R_0231, R_0312, and each class has 8 members. A swap within a pair flips both the permutation parity and the component's sign, and a pair exchange is an even permutation leaving the component unchanged, so all 8 members of a class contribute with the same sign. (0231) and (0312) are 3-cycles of (0123), so they are even too. Hence ε^ρσμν R_ρσμν = 8 ε^0123 (R_0123 + R_0231 + R_0312), which vanishes exactly when the cyclic identity holds.

## Tutor guidance

**Opening questions**

- After the pair symmetries, which Riemann components in four dimensions still have all four indices different?
- If curvature is a rule for how a small loop turns a carried direction, what might three loops around a box corner have to do with each other?
- Do you remember which property of the Christoffel symbols comes from 'no torsion'?

**Common questions**

- *Why is it called the first Bianchi identity if Schutz never calls it that?* — Naming varies. Many modern texts call the algebraic cyclic identity the first Bianchi identity and the derivative identity the second. Schutz and d'Inverno keep 'Bianchi' for the derivative one. In this course we say 'cyclic identity' and treat 'Bianchi identity' alone as the differential one.
- *Does it hold for the Ricci tensor too?* — Not as such, because Ricci has only two indices. But contracting the upper index of the cyclic identity with the first lower one gives R_μν − R_νμ = R^ρ_ρμν. For the metric connection R^ρ_ρμν vanishes (it is the trace over the antisymmetric first pair), so the Ricci tensor is symmetric. For a torsion-free connection that is not metric, Ricci can have an antisymmetric part equal to that trace.
- *Why does holding the first index fixed matter?* — In the mixed tensor R^ρ_σμν the upper index plays a different role, so you cycle the three lower slots. For the all-lower tensor with the pair symmetries, cycling any three slots gives an equivalent statement, because the identity is the same as the total antisymmetric part vanishing.
- *Is there anything physical in it?* — It is a consistency property rather than a measurable law. Its physical footprint is indirect: it makes Ricci symmetric, trims the curvature count to 20, and constrains Killing vectors.

**Pitfalls when explaining**

- Do not call it a 'symmetry' without saying it is a three-term linear relation; learners then try to pair components.
- Do not skip the torsion-free assumption, even though GR never relaxes it.
- Say which slots are cycled in the course convention before writing indices; copying a pattern from a book with different slot order gives a wrong identity.
- Keep it separate from the differential Bianchi identity in wording and notation.

**When to show a demo**

- When the learner asks whether all 21 remaining components are independent, open the index wheel on the {0,1,2,3} tiles.
- After the Christoffel proof, flip the torsion toggle to show the sum becoming nonzero.
- When counting in n dimensions, use the wheel with repeated indices to show the sum vanishing for free.

**Saying it aloud:** Say: 'R, upper rho, lower sigma mu nu, plus R upper rho lower mu nu sigma, plus R upper rho lower nu sigma mu, equals zero.' Then the compact version: 'antisymmetrize the three lower indices and you get zero.' For the 4D case say 'R zero one two three plus R zero two three one plus R zero three one two is zero', stressing 'two three one' and 'three one two' as the cyclic shifts. Never read brackets aloud as symbols; say 'antisymmetrized over'.

## Sources

- schutz ch06 (developed): p.158 §6.5, p.159 §6.5, p.167 §Exercises
- gifted-amateur ch11 (introduced): p.126 §11.4
- gifted-amateur ch35 (revisited): p.369 §35.3, p.370 §35.3
- dinverno ch06 (developed): p.106 §6.12, p.110 §Exercises
- legacy lab-riemann-independent-components (introduced)

## Review

**Verdict:** fixed

**Fixes**

- Common question on Ricci: the old answer said contracting the cyclic identity 'with the metric' makes Ricci symmetric. Replaced it with the correct contraction R_μν − R_νμ = R^ρ_ρμν, which vanishes for the Levi-Civita connection but not for a general torsion-free one.
- Intuition level: removed the overstatement that the identity's 'only job' is the 21 → 20 reduction, since it is also used for Ricci symmetry, Killing vectors and the Weyl tensor.

**Concerns**

- The index-free form cites only a legacy asset, and the torsion version of the identity (Kobayashi-Nomizu Thm III.5.3, checked) has no book ref, because none of the three books treats torsion here.
- Checked and correct: every equation against SCH (6.68)-(6.70), GA (11.25)/(35.31), DIV (6.40), (6.41), (6.79), (6.82), plus the course Riemann definition; the working of all five checks, including the 12-term Christoffel cancellation and the ε-contraction factor of 8.
- Ref spot-checks: SCH §6.5 p.158/159, Ex 6.18 p.167, GA §11.4 p.126, Example 35.6 p.369, DIV §6.12 p.106, Ex 6.24 p.110 all match the source copies.
