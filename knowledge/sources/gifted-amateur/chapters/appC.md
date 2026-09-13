---
type: "source-unit"
book: "gifted-amateur"
book_short: "GA"
unit: "appC"
title: "Manifolds and bundles"
part: null
printed_pages: [565, 580]
pdf_pages: [582, 597]
math_level: 3
conceptual_level: 4
novice_friendliness: 3
style_tags: ["axiomatic-mathematical", "diagram-driven", "example-driven", "conversational-informal", "spiral-revisit", "analogy-driven", "survey-overview"]
concepts: ["embedding versus intrinsic description", "manifold", "pseudo-Riemannian manifold", "singularity as breakdown of the manifold structure", "metric space", "topological space", "open and closed intervals", "Euclidean space R^n", "open ball", "open set", "open cover", "Hausdorff property", "map", "composition of maps", "image and inverse image", "injective map", "surjective map", "bijection", "morphism", "continuous map (topological definition)", "homeomorphism", "coordinate function", "coordinate neighbourhood", "chart", "atlas", "transition map", "coordinate representation of a function", "C^k and smooth functions", "compatible (C^infinity-related) charts", "maximal atlas", "differentiable manifold", "differentiable map between manifolds", "diffeomorphism", "Jacobian determinant", "active coordinate transformation", "diffeomorphism invariance", "Lie derivative as generator of a diffeomorphism", "Killing vector field", "conservation of energy-momentum from diffeomorphism invariance", "energy-momentum tensor from the action", "compactness", "Heine-Borel theorem", "bounded set", "parametrized curve on a manifold", "tangent vector as directional derivative", "derivation", "coordinate basis vectors", "equivalence class of curves", "tangent space", "fibre bundle", "base space and fibre", "canonical projection", "tangent bundle", "trivial (product) bundle", "local versus global triviality", "Moebius bundle", "cross section", "zero section", "gauge fields as bundle structures"]
verification: "fixed"
---

# GA appC · Manifolds and bundles

> A from-scratch tour of the topology and differential structure underneath the whole book: sets and open sets, maps and their classification, homeomorphisms, charts and atlases, smooth transition maps and diffeomorphisms (with a proof that diffeomorphism invariance forces the divergence of T to vanish), compactness, curves, tangent vectors as derivations, and a picture-driven introduction to fibre bundles, sections, and the cylinder versus Moebius contrast.

**Pages:** printed 565–580 · pdf 582–597 · **Difficulty:** math 3/5, conceptual 4/5, novice-friendliness 3/5

Most of the appendix needs only calculus and set notation, and every definition is paired with a sketch and a small example, so the mathematics is light. The conceptual load is high: many definitions arrive in quick succession, composition notation is dense, and several statements are informal or slightly off (Hausdorff gloss, transition-map direction, compactness of a disc with a hole, local triviality). Example C.10 is a sudden jump in level, requiring Lie derivatives, functional derivatives and covariant integration by parts from Chapters 33 and 40. The bundle section is intuitive but stops at pictures.

## Role in the book

An optional appendix that supplies the foundations the main text deliberately kept in the background. Chapter 31 reintroduced geometry with a light-touch manifold definition and Chapter 33 introduced the Lie derivative (and diffeomorphisms in a margin note), both pointing here for rigour; a Chapter 12 margin note promises that nabla . T = 0 can be justified from diffeomorphism invariance, delivered in Example C.10 using the action machinery of Chapter 40. Chapters 15, 19, 44 and 50 also send readers here for the technical meaning of bundles, topology and compactness. It replaces the embedded pictures used earlier (a sphere sitting in R^3 in Chapter 7, the tangent plane to a surface in Chapter 30) with intrinsic constructions, and prepares readers for modern texts, singularity theory (Chapters 26 and 50) and the bundle language behind gauge fields (Chapter 44). It sits between the conventions appendix (B) and the embedding appendix (D).

## Learning objectives

- Reader can explain why general relativity needs an intrinsic manifold description rather than a surface embedded in a bigger Euclidean space.
- Reader can order the layers set, topological space, manifold, and manifold-with-metric, and say what extra structure each layer adds.
- Reader can define open ball, open set, open cover and the Hausdorff property in R^n and sketch a non-Hausdorff branching space.
- Reader can classify a given real function as many-to-one, one-to-one, onto, or bijective by inspecting its graph, and state when an inverse map exists.
- Reader can state the topological definition of continuity and of a homeomorphism, and decide whether pairs such as mug/doughnut, line/circle, disc/square are homeomorphic.
- Reader can define a chart, coordinate neighbourhood and atlas, and show why the circle needs at least two charts while R^m needs one.
- Reader can write a coordinate transformation as the transition map psi o phi^{-1} and the coordinate representation of a function (f o phi^{-1}) or of a map between manifolds (psi o f o phi^{-1}).
- Reader can explain, via f o psi^{-1} = (f o phi^{-1}) o (phi o psi^{-1}), why differentiability on a manifold requires C^infinity-compatible charts, and define a differentiable manifold and maximal atlas.
- Reader can decide whether maps like x, x^2, x^3 and a linear map on R^2 are diffeomorphisms, using injectivity, smoothness of the inverse and the Jacobian.
- Reader can reproduce the argument that invariance of the matter action under diffeomorphisms generated by an arbitrary vector field implies nabla_mu T^{mu nu} = 0.
- Reader can give a working definition of compactness, test it with the sequence 1/n on [0,1] versus (0,1], and list compact and non-compact examples.
- Reader can define a tangent vector as the derivative of f o c along a curve, derive its coordinate form with the chain rule, recover components by acting on coordinate functions, and state the linearity and Leibniz properties.
- Reader can describe the tangent space at a point as the vector space of equivalence classes of curves sharing a tangent, independent of any embedding.
- Reader can describe a fibre bundle by base, fibre, total space and projection, give TS^1 = S^1 x R as a trivial bundle, contrast it with the Moebius bundle, and use sections (pi o s = identity) and the zero section to tell them apart.

## Assumed background

- Functions of several variables, partial derivatives and the chain rule — undergrad-calculus
- Jacobian matrix and determinant of a change of variables — undergrad-calculus
- Vector spaces, basis expansion v = v^mu e_mu — linear-algebra (GA ch02)
- Informal manifold picture: locally flat spaces, S^1, S^2, torus, and non-manifold examples — earlier-in-this-book (GA ch31 §31.1 (Fig. 31.1))
- Coordinate transformations and tangent vectors as directional derivatives in coordinates — earlier-in-this-book (GA ch03, ch31)
- Covariant derivative, metric compatibility g_{ab;c}=0 — earlier-in-this-book (GA ch07, ch09)
- Lie derivative along a vector field and the formula for L_u g — earlier-in-this-book (GA ch33)
- Action principle, functional derivative with respect to g_{mu nu}, energy-momentum tensor from the matter Lagrangian — earlier-in-this-book (GA ch40)
- Meaning of nabla . T = 0 as local energy-momentum conservation — earlier-in-this-book (GA ch12)
- Integration by parts in curved space (covariant divergence with sqrt(-g)) — earlier-in-this-book (GA ch12, ch40)
- Naive set notation (membership, union, intersection) — school-math

## Teaching approach

A deliberately 'forget everything and rebuild' appendix. The authors strip away the metric and embedding, then climb a pyramid of structure (set, topology, manifold, metric) one rung at a time. Each abstract definition is paired with a small sketch of blobs and arrows and followed immediately by a numbered example drawn from the line, the circle, the plane or familiar objects (mug, doughnut, globe). The central device is the composition of maps: every coordinate-level object (coordinates, transformations, function values, curves, tangent vectors) is expressed as a composite with the chart map and read aloud in words ('input ... output ...'). Rigour is only partial: formal alternatives are pushed into margin notes, and physics payoffs (gauge symmetry, conservation of T, gauges and bundles) are signposted rather than developed, apart from one worked field-theory example.

**Style:** axiomatic-mathematical, diagram-driven, example-driven, conversational-informal, spiral-revisit, analogy-driven, survey-overview

**Narrative arc**

1. Motivation: spacetime need not sit inside a higher-dimensional Euclidean space, so an intrinsic, smooth description is required; singularities become places where that description fails.
2. Big picture: split geometry into two ingredients, the smooth manifold and the metric laid on it; flat space, Minkowski spacetime and GR spacetime as manifold plus metric; pyramid figure of layered structure.
3. Primitive vocabulary: intervals, set operations, R^n with Euclidean distance, open balls, open sets, open covers, Hausdorff property.
4. Maps as the basic tool: notation, composition, images and inverse images, many-to-one / one-to-one / into / onto / bijection, checked on four graphs.
5. Structure-preserving maps: topological continuity, homeomorphism, clay-deformation intuition, list of homeomorphic and non-homeomorphic pairs.
6. Manifold defined as locally homeomorphic to R^n; examples and non-examples.
7. Coordinates as a homeomorphism from a patch to R^m; the circle forces two patches; charts, atlases and transition maps psi o phi^{-1}; formal manifold definition collected.
8. Functions and maps on manifolds made concrete through coordinate representations.
9. Problem: chart-level differentiability is chart dependent; fix by requiring C^infinity transition maps; differentiable manifold, maximal atlas, differentiable maps, diffeomorphisms; tests on simple maps.
10. Physics payoff: diffeomorphisms as active transformations and gauge symmetries of GR; Lie derivative generated by a flow; Example C.10 derives nabla . T = 0 from diffeomorphism invariance.
11. Compactness as the generalization of a closed bounded interval, via sequences; examples.
12. Curves as maps from an interval; tangent vectors as derivatives of f along curves; chain rule gives components and coordinate basis; derivation axioms; equivalence classes of curves; tangent space at each point.
13. Fibre bundles by picture: rotate tangent lines vertical and lift them off the curve; base, fibre, projection, product bundle, TS^1 as cylinder, Moebius twist, local vs global triviality, sections and the zero section.
14. Summary bullets re-state manifold, diffeomorphism, compactness, tangent vector and bundle in one line each.

**Signature moves**

- Every composite map is translated into a plain-language input/output sentence immediately after the formula (e.g. put in a coordinate, get a point, get a new coordinate).
- Blob-and-arrow diagrams with a boxed R^m panel: the manifold drawn as an irregular region, the chart image drawn as a gridded patch, maps drawn as curved arrows labelled by their composite.
- Motivate a structural requirement by exhibiting a failure: the circle's angle coordinate double-counts one point, forcing a second chart; chart-dependent differentiability forces smooth transition maps.
- Use a small ladder of test maps (x, x^2, x^3, a shear-like linear map) to separate bijectivity, smoothness and smooth invertibility.
- Magnifying-glass pictures to convey 'locally looks like R^n' for circle, sphere and torus.
- Build the bundle concept by redrawing a familiar picture (tangent lines on a curve) step by step until it becomes fibres standing above a base, and then use physical rod-and-ring photographs for trivial and twisted bundles.
- Push formal alternatives (open-cover compactness, C^k classes, Jacobian computation) into margin notes so the main line stays informal.
- Close the loop to physics inside a mathematics appendix: diffeomorphism invariance of the action delivers nabla . T = 0.

## Section by section

### Opening: why an intrinsic, smooth description — p.565 (pdf 582)

Argues that embedding a curved space in higher-dimensional flat space is a crutch GR cannot rely on, so spacetime must be described intrinsically as a smooth manifold carrying a separately specified metric. Space, Minkowski spacetime and curved spacetime are recast as manifolds with flat or Lorentzian metrics, singularities are characterized as breakdowns of manifold smoothness, and a pyramid (set, topological space, manifold, manifold with metric) frames the appendix. Margin notes add an executive summary.

**Concepts:** embedding versus intrinsic description, manifold, pseudo-Riemannian manifold, singularity as breakdown of the manifold structure

**Key moves**
- Separate geometry into two independent ingredients: the manifold (smoothness) and the metric (lengths and angles).
- Identify R^3 with flat d(,), R^4 with eta(,), and a general M with Lorentz g(,) as three instances of manifold-plus-metric.
- Announce a from-scratch rebuild in which metric notions are temporarily forgotten.

### §C.1 Preliminaries — p.566 (pdf 583)

Distinguishes metric spaces (distances available) from topological spaces (only neighbourhood structure through open subsets). Lists basic notation: open and closed intervals, membership, union, intersection, subset, empty set, R and R^n with Euclidean distance. Defines open balls, open sets as unions of balls, open covers, and the Hausdorff separation property, illustrated by a panel of small sketches including a branching non-Hausdorff space.

**Concepts:** metric space, topological space, open and closed intervals, Euclidean space R^n, open ball, open set, open cover, Hausdorff property

**Key moves**
- Euclidean distance (C.1) makes R^n a metric space, which supplies open balls.
- Open sets defined by the every-point-has-a-ball criterion, then used as the notion of 'nearby' once the metric is dropped.
- Restrict attention to Hausdorff spaces from the outset.

### §C.2 Maps and functions — p.567 (pdf 584)

Introduces a map as a rule assigning to each input in one space a unique output in another, with arrow and maps-to notation, real functions of n variables as maps R^n to R, and composition g o f.

**Concepts:** map, composition of maps

**Key moves**
- Notation f: M -> N (C.2) and x |-> f(x) (C.3).
- Composition g o f is read as g(f(x)), the operation used throughout the rest of the appendix.

### §C.3 One-to-one, into, and onto — p.567 (pdf 584)

Defines image and inverse image and uses them to classify maps as many-to-one, one-to-one, into (defined on the whole domain), onto, and bijective; only bijections have an inverse map. Example C.1 applies the classification to four function graphs.

**Concepts:** image and inverse image, injective map, surjective map, bijection

**Key moves**
- Classify maps by counting inverse images of points.
- Tie existence of a genuine inverse map to bijectivity.
- Check the classification against graphs: exponential-like, wiggly cubic, flattened cubic, parabola.

### §C.4 Continuous maps — p.568 (pdf 585)

Introduces morphisms as structure-preserving maps for comparing spaces and previews the homeomorphism/diffeomorphism pair. Gives the open-set definition of continuity and defines a homeomorphism as a continuous bijection with continuous inverse, pictured as deforming clay without tearing or gluing. Example C.2 lists homeomorphic and non-homeomorphic pairs (disc and square, graph and domain, mug and doughnut; R^m vs R^n, line vs circle).

**Concepts:** morphism, continuous map (topological definition), homeomorphism

**Key moves**
- Continuity phrased with open sets only, so it survives without a metric.
- Clay-deformation intuition for homeomorphism, flagged as a special case.
- Use compactness (defined later) to explain why a line is not homeomorphic to a circle.

### §C.5 Manifolds, coordinates, and charts — p.569 (pdf 586)

Defines a manifold as a set whose points each have a neighbourhood homeomorphic to an open subset of R^n, with the circle, sphere and torus as examples and a line through a plane or a double cone as non-examples. Coordinates are a homeomorphism from a patch to R^m; the circle's angle coordinate cannot include the point where 0 and 2 pi coincide, so two patches are needed. Charts, atlases and transition maps are defined and gathered into a formal manifold definition.

**Concepts:** manifold, coordinate function, coordinate neighbourhood, chart, atlas, transition map

**Key moves**
- Points of a manifold exist without coordinates; coordinates are the map x^mu = phi(P) (C.4) with inverse (C.5).
- Circle example: excluding one point makes phi_1 one-to-one; a second chart with a different excluded point completes the cover.
- A coordinate transformation is the composite psi o phi^{-1} of two chart maps on the overlap (C.6).
- Collect the three defining properties: cover, local homeomorphisms, transition maps on overlaps.

### §C.6 Functions on the manifold — p.571 (pdf 588)

Explains that the familiar formula y = f(x^1,...,x^m) is really the coordinate representation f o phi^{-1} of a function living on the manifold, and extends this to maps between manifolds, represented by psi o f o phi^{-1} between two coordinate spaces (Example C.7).

**Concepts:** coordinate representation of a function, map between manifolds

**Key moves**
- Pull a function back to coordinate space by composing with the inverse chart (C.7).
- Sandwich a manifold-to-manifold map between two charts (C.8).

### §C.7 Differentiation on the manifold — p.572 (pdf 589)

Shows that differentiability judged in one chart need not hold in another unless the transition map is differentiable, leading to C^infinity-related charts, the maximal atlas, and the differentiable manifold. Defines differentiable maps and diffeomorphisms, tests x, x^2, x^3 and a linear map on R^2, and contrasts homeomorphism (continuous deformation) with diffeomorphism (smooth deformation). Diffeomorphisms of a manifold to itself are identified with active transformations and gauge symmetries of GR and underlie the Lie derivative; Example C.10 derives nabla . T = 0 from diffeomorphism invariance of the matter action.

**Concepts:** C^k and smooth functions, compatible (C^infinity-related) charts, maximal atlas, differentiable manifold, differentiable map between manifolds, diffeomorphism, Jacobian determinant, active coordinate transformation, diffeomorphism invariance, Lie derivative as generator of a diffeomorphism, conservation of energy-momentum from diffeomorphism invariance

**Key moves**
- Decompose f o psi^{-1} = (f o phi^{-1}) o (phi o psi^{-1}) (C.9) to locate where differentiability can fail.
- Require phi_i o phi_j^{-1} to be C^infinity on every overlap (C.10).
- Diffeomorphism: invertible map whose coordinate representation and its inverse are both C^infinity; forces equal dimensions.
- x^3 is a smooth bijection but not a diffeomorphism because its inverse is not smooth at 0.
- Set the metric variation equal to the Lie derivative 2 u_(mu;nu), use symmetry, integrate by parts, invoke arbitrariness of u and the action definition of T.

### §C.8 Compact regions — p.575 (pdf 592)

Generalizes the closed interval to compactness: a compact region does not run off to infinity and is missing neither interior pieces nor boundary pieces, made precise by requiring sequences to have accumulation points inside. Example C.11 contrasts [0,1] with (0,1] using 1/n; the Heine-Borel theorem and the closed-and-bounded criterion are cited; Example C.12 lists compact (closed disc, sphere, torus) and non-compact (plane, open disc, punctured disc) spaces. Margin notes give the open-cover definition.

**Concepts:** compactness, Heine-Borel theorem, bounded set

**Key moves**
- Three failure modes of compactness (escaping to infinity, holes, missing boundary).
- Sequence test with 1/n shows the removed endpoint breaks compactness.
- Note that boundedness needs a metric, so the closed-and-bounded criterion is a Euclidean statement.

### §C.9 Curves — p.575 (pdf 592)

Defines a curve as a map from a parameter interval into the manifold and its coordinate description as the composite of the curve with a chart (C.16).

**Concepts:** parametrized curve on a manifold

**Key moves**
- Curve c: [a,b] -> M; coordinates along it x^mu = phi o c(lambda).

### §C.10 Tangent spaces — p.576 (pdf 593)

Rejects arrows as the basic picture of vectors on a manifold and defines a tangent vector at a point as the rate of change of arbitrary functions along a curve. Splitting f o c through the chart and applying the chain rule yields components dx^mu/dlambda and coordinate basis operators partial/partial x^mu (C.20); acting on coordinate functions recovers the components (Example C.13). Tangent vectors are characterized as linear, Leibniz-obeying maps on smooth functions, identified with equivalence classes of curves, and collected into the tangent space at each point.

**Concepts:** tangent vector as directional derivative, derivation, coordinate basis vectors, equivalence class of curves, tangent space

**Key moves**
- Rate of change of f(c(lambda)) at lambda = 0 (C.17).
- Insert the identity phi^{-1} o phi to write f o c = (f o phi^{-1}) o (phi o c) (C.18).
- Chain rule separates curve data (components) from function data (partial derivatives) (C.19, C.20).
- Two curves through P with equal coordinate velocities define the same vector (C.23, C.24).

### §C.11 Fibre bundles — p.578 (pdf 595)

Builds the bundle idea by rotating the tangent lines of a curve to stand vertically and lifting them off, giving a copy of a fibre above every base point. Defines base space, fibre, total space (dimension equal to the sum), canonical projection, and product (trivial) bundles; TS^1 is the cylinder S^1 x R with coordinates (theta, y). The Moebius bundle is locally a product but globally twisted. Cross sections (lifts with pi o s = identity) generalize graphs of functions, and the necessary crossing of the zero section distinguishes the Moebius bundle from the cylinder. A short chapter summary closes the appendix.

**Concepts:** fibre bundle, base space and fibre, canonical projection, tangent bundle, trivial (product) bundle, local versus global triviality, Moebius bundle, cross section, zero section

**Key moves**
- Picture tangent vectors as beads on vertical fibres above the base.
- Projection pi forgets the fibre coordinate.
- TS^1 = S^1 x R with v = y partial_theta.
- Glue two locally trivial pieces with a flip to get the Moebius strip.
- Sections: s followed by pi is the identity; every section of the twisted bundle must hit zero.

## Concepts

### embedding versus intrinsic description

*convention · introduced* · also: extrinsic picture, embedding artifice

A space can be studied by placing it inside a larger flat space (extrinsic, embedded) or purely through structures defined on the space itself (intrinsic); GR adopts the intrinsic view because there is no evidence spacetime sits inside a higher-dimensional Euclidean space.

**How introduced:** Opening paragraph: a sphere is usually pictured inside 3D space, but spacetime cannot be assumed to have such a host; the tangent-plane picture of earlier chapters is contrasted with the intrinsic tangent space in Fig. C.15.

**Notes:** Appendix D takes up embeddings explicitly.

**Where:** GA p.565 (pdf 582); GA §C.10 p.577 (pdf 594)

### manifold

*definition · core* · also: topological manifold, smooth space

A set in which every point has an open neighbourhood that is homeomorphic to an open subset of R^n; equivalently a space covered by charts whose images are open sets of R^n. (Standard definitions also require Hausdorff and second-countable topology.)

**How introduced:** Working definition 'locally flat and Euclidean' in the opening, then a precise local-homeomorphism definition in §C.5 illustrated with magnifying glasses on a circle, sphere and torus, and finally a three-property chart-based definition.

**Prerequisites:** open set, homeomorphism, Euclidean space R^n

$$
\forall P\in\mathcal M\ \exists U\ni P \text{ open},\ \phi:U\to\phi(U)\subset\mathbb R^n \text{ homeomorphism}
$$

**Notes:** The book allows 'for some n', silently permitting different dimensions at different points; it also omits second countability.

**Where:** GA p.565 (pdf 582); GA §C.5 p.569 (pdf 586); GA §C.5 p.571 (pdf 588); GA §Chapter summary p.580 (pdf 597)

### pseudo-Riemannian manifold

*mathematical-object · revisited* · also: Riemann manifold (M, g), manifold with metric, Lorentzian manifold

A differentiable manifold equipped with a smooth symmetric non-degenerate metric tensor g; in GR the metric has Lorentzian signature and, together with its compatible connection, fixes lengths, angles, causal structure and curvature.

**How introduced:** Placed at the apex of the pyramid of structure (set, topology, manifold, metric) in Fig. C.1; flat space and Minkowski spacetime are presented as special cases.

**Prerequisites:** differentiable manifold

**Where:** GA p.565 (pdf 582); GA p.566 (pdf 583)

### singularity as breakdown of the manifold structure

*definition · mention* · also: singularity

A singularity is characterized as a place where spacetime can no longer be described as a smooth manifold.

**How introduced:** Mentioned in the opening as a motivation for caring about smoothness; margin note points to black-hole and cosmological singularity studies.

**Prerequisites:** manifold

**Where:** GA p.565 (pdf 582)

### metric space

*definition · introduced*

A set together with a distance function assigning a non-negative number to each pair of points (symmetric, zero only for equal points, obeying the triangle inequality).

**How introduced:** First line of §C.1, as the richer of two kinds of space; R^n with Euclidean distance is the example.

$$
|x-y| = \left[\sum_\mu (x^\mu-y^\mu)^2\right]^{1/2}
$$

**Notes:** The book does not state the metric-space axioms; this is a different use of 'metric' from the metric tensor g.

**Where:** GA §C.1 p.566 (pdf 583)

### topological space

*definition · introduced*

A set together with a collection of subsets declared open (closed under arbitrary unions and finite intersections, containing the empty set and the whole space), which encodes nearness without distances.

**How introduced:** Contrasted with a metric space in §C.1: less structure, neighbourhoods described via open subsets; second rung of the pyramid in Fig. C.1.

**Prerequisites:** open set

**Notes:** The axioms are not given in the book.

**Where:** GA §C.1 p.566 (pdf 583); GA p.565 (pdf 582)

### open and closed intervals

*definition · mention*

(a,b) is the set of reals strictly between a and b; [a,b] also includes the endpoints.

**How introduced:** First bullet of §C.1 with sketches of bracket and parenthesis symbols; later reused as the model for compactness.

**Where:** GA §C.1 p.566 (pdf 583); GA §C.8 p.575 (pdf 592)

### Euclidean space R^n

*mathematical-object · introduced* · also: n-tuple space, flat space

The set of ordered n-tuples of real numbers with the Euclidean distance; the model space that manifolds resemble locally and in which coordinates live.

**How introduced:** Defined in §C.1 with the distance formula, and reintroduced in §C.5 as 'the space where vectors live'.

**Prerequisites:** metric space

$$
|x-y| = \left[\sum_{\mu=1}^n (x^\mu-y^\mu)^2\right]^{1/2}
$$

**Where:** GA §C.1 p.566 (pdf 583); GA §C.5 p.569 (pdf 586)

### open ball

*definition · introduced*

The set of points of R^n lying at distance strictly less than r from a centre y.

**How introduced:** Defined right after the distance formula as the basic example of an open subset, with a dashed circle in a square as picture.

**Prerequisites:** Euclidean space R^n

$$
B_r(y)=\{x: |x-y|<r\}
$$

**Where:** GA §C.1 p.566 (pdf 583)

### open set

*definition · introduced* · also: open subset, neighbourhood

A subset S of R^n such that each of its points is the centre of some open ball contained in S; equivalently a union of open balls. In a general topological space open sets are the specified collection.

**How introduced:** §C.1 bullet: any region without its boundary is open; open sets are the currency of topology once distances are dropped.

**Prerequisites:** open ball

**Where:** GA §C.1 p.567 (pdf 584)

### open cover

*definition · introduced*

A collection of open sets whose union contains a given set A, so that every point of A lies in at least one member.

**How introduced:** §C.1 with a sketch of overlapping dashed discs; reused in a margin note for the open-cover definition of compactness and implicitly by the chart cover of a manifold.

**Prerequisites:** open set

**Notes:** The book's wording ('every point in A is in the collection O') should be read as 'in some member of O'.

**Where:** GA §C.1 p.567 (pdf 584); GA §C.8 p.575 (pdf 592)

### Hausdorff property

*definition · introduced* · also: separation property, T2

Any two distinct points possess disjoint open neighbourhoods; excludes pathological spaces such as a line that branches or a line with a doubled point.

**How introduced:** §C.1 bullet with a branching picture of a non-Hausdorff space; the authors restrict to Hausdorff spaces thereafter.

**Prerequisites:** open set

**Notes:** The parenthetical gloss about infinite subdivision of a line is not an accurate characterization; the separation statement is the definition.

**Where:** GA §C.1 p.567 (pdf 584)

### map

*definition · developed* · also: function, mapping

A rule f: M -> N assigning to each element of the domain M exactly one element of N.

**How introduced:** §C.2 as the fundamental tool for relating spaces, with a two-blob arrow picture; margin note says map and function are used interchangeably.

$$
f:\mathcal M\to\mathcal N
$$

$$
f: x\mapsto y=f(x)
$$

**Where:** GA §C.2 p.567 (pdf 584)

### composition of maps

*operation · core* · also: composite map

Given f: M -> N and g: N -> L, the composite g o f: M -> L sends x to g(f(x)).

**How introduced:** Defined in §C.2 and then used as the workhorse for coordinates, transformations, function representations, curves and tangent vectors.

**Prerequisites:** map

$$
(g\circ f)(x)=g(f(x))
$$

**Where:** GA §C.2 p.567 (pdf 584); GA §C.5 p.571 (pdf 588); GA §C.6 p.572 (pdf 589); GA §C.10 p.576 (pdf 593)

### image and inverse image

*definition · introduced* · also: preimage

For a map f and subset S of the domain, f(S) is the set of outputs; the inverse image of T is the set of domain points mapped into T.

**How introduced:** Start of §C.3, used to classify maps.

**Prerequisites:** map

$$
T=f(S)
$$

$$
S=f^{-1}(T)
$$

**Where:** GA §C.3 p.567 (pdf 584)

### injective map

*definition · introduced* · also: one-to-one, 1-1

A map in which distinct inputs always give distinct outputs, so every image point has a single inverse-image point.

**How introduced:** §C.3 classification with arrow pictures; margin note gives the synonym and etymology.

**Prerequisites:** image and inverse image

**Where:** GA §C.3 p.567 (pdf 584); GA §C.3 p.568 (pdf 585)

### surjective map

*definition · introduced* · also: onto

A map whose image is the whole target space, so every target point has at least one inverse image.

**How introduced:** §C.3 bullet with French 'sur' etymology in a margin note; contrasted with the book's 'into', which only requires the map to be defined on all of M.

**Prerequisites:** image and inverse image

**Notes:** Some texts use 'into' to mean injective; GA uses it to mean defined on the whole domain.

**Where:** GA §C.3 p.568 (pdf 585)

### bijection

*definition · introduced* · also: bijective map, invertible map

A map that is both one-to-one and onto; exactly these maps have an inverse map, which is itself bijective.

**How introduced:** End of §C.3, then Example C.1 tests four graphs.

**Prerequisites:** injective map, surjective map

$$
f^{-1}:\mathcal N\to\mathcal M
$$

**Where:** GA §C.3 p.568 (pdf 585)

### morphism

*definition · mention* · also: structure-preserving map

A map between two mathematical structures that respects the structure in question, used to decide when spaces are 'the same' for some purpose.

**How introduced:** Opening of §C.4 as the general idea behind homeomorphism (topology) and diffeomorphism (smoothness).

**Prerequisites:** map

**Where:** GA §C.4 p.568 (pdf 585)

### continuous map (topological definition)

*definition · introduced* · also: continuity

phi: M -> N is continuous at x if for every open set V containing phi(x) there is an open set U containing x with phi(U) inside V; continuous means continuous at every point.

**How introduced:** Stated in §C.4 using only open sets so it does not need distances.

**Prerequisites:** open set, map

**Notes:** Reduces to the epsilon-delta definition in R^n.

**Where:** GA §C.4 p.568 (pdf 585)

### homeomorphism

*definition · core* · also: topological equivalence, continuous deformation

A bijection between spaces that is continuous with a continuous inverse; homeomorphic spaces share all topological properties.

**How introduced:** §C.4 with the modelling-clay picture (no tearing, punching holes, gluing or healing), Fig. C.6 mug-to-doughnut, and Example C.2 list of yes/no cases; used next to define manifolds and coordinates.

**Prerequisites:** bijection, continuous map (topological definition)

**Notes:** A margin note stresses that continuous deformation is only one instance; homeomorphisms can act between non-manifolds.

**Where:** GA §C.4 p.568 (pdf 585); GA §C.4 p.569 (pdf 586); GA §C.7 p.574 (pdf 591)

### coordinate function

*mathematical-object · core* · also: coordinate map, chart map, phi

A homeomorphism phi from an open patch U of an m-dimensional manifold onto an open subset of R^m; its m component functions x^mu(P) are the coordinates of P.

**How introduced:** §C.5: points of the manifold exist independently of labels; to name them with numbers we map a patch into R^m (Fig. C.8), with the warning that x denotes both the functions and their values.

**Prerequisites:** homeomorphism, manifold

$$
x^\mu=\phi(\mathcal P)
$$

$$
\mathcal P=\phi^{-1}(x^\mu)
$$

**Where:** GA §C.5 p.570 (pdf 587)

### coordinate neighbourhood

*definition · developed* · also: patch, chart domain

The open subset U of the manifold on which a given coordinate function is defined and one-to-one.

**How introduced:** §C.5: needed because a single homeomorphism usually cannot cover the whole manifold, as the circle shows.

**Prerequisites:** open set, coordinate function

**Where:** GA §C.5 p.570 (pdf 587); GA §C.5 p.571 (pdf 588)

### chart

*definition · core* · also: coordinate system, local coordinates

A pair (U, phi) of an open set of the manifold and a homeomorphism from U onto an open subset of R^m.

**How introduced:** Named in §C.5 after the circle examples; margin note says physicists call it a coordinate system.

**Prerequisites:** coordinate neighbourhood, coordinate function

**Where:** GA §C.5 p.571 (pdf 588)

### atlas

*definition · developed* · also: family of charts

A collection of charts whose domains together cover the manifold.

**How introduced:** §C.5 after Examples C.4-C.5: two angle charts with different excluded points cover the circle; Example C.6 contrasts R^m (one chart) with S^1 (at least two).

**Prerequisites:** chart, open cover

$$
\{(U_i,\phi_i)\}
$$

**Where:** GA §C.5 p.571 (pdf 588)

### transition map

*operation · core* · also: coordinate transformation, overlap map, chart compatibility map

For overlapping charts (U, phi) and (V, psi), the map psi o phi^{-1} from phi(U cap V) to psi(U cap V) that converts one set of coordinates of a point into the other.

**How introduced:** §C.5 via Fig. C.10: go from coordinates back to the point with phi^{-1}, then forward with psi; then built into the formal manifold definition and, in §C.7, required to be smooth.

**Prerequisites:** chart, composition of maps, bijection

$$
y^\mu=\psi\circ\phi^{-1}(x^\mu)
$$

**Notes:** The bullet list on p.571 states the direction of phi_i o phi_j^{-1} backwards.

**Where:** GA §C.5 p.571 (pdf 588); GA §C.7 p.573 (pdf 590)

### coordinate representation of a function

*technique · developed* · also: f o phi^{-1}, function in coordinates

A function f: M -> R is handled in practice through f o phi^{-1}, an ordinary real function of the m coordinates on phi(U); similarly a map f: M -> N is represented by psi o f o phi^{-1} between coordinate spaces.

**How introduced:** §C.6: we only have access to coordinates, so we route the input through the inverse chart (Fig. C.11); Example C.7 extends it to manifold-to-manifold maps (Fig. C.12).

**Prerequisites:** coordinate function, composition of maps

$$
y=f\circ\phi^{-1}(x^1,\dots,x^m)
$$

$$
(y^1,\dots,y^m)=\psi\circ f\circ\phi^{-1}(x^1,\dots,x^m)
$$

**Where:** GA §C.6 p.572 (pdf 589)

### C^k and smooth functions

*definition · introduced* · also: differentiability class, C-infinity, smooth

A function on an open region of R^n is C^k if all partial derivatives of order up to k exist and are continuous; C^infinity (smooth) if this holds for every k.

**How introduced:** Margin note in §C.7 with polynomials as smooth and x^{1/3} as a counterexample whose derivative blows up at the origin.

**Where:** GA §C.7 p.573 (pdf 590)

### compatible (C^infinity-related) charts

*definition · developed* · also: smooth compatibility, C-infinity related charts

Two charts are compatible if on their overlap the transition maps in both directions are infinitely differentiable.

**How introduced:** §C.7: a function can look differentiable in one chart and not in another; the decomposition f o psi^{-1} = (f o phi^{-1}) o (phi o psi^{-1}) shows the transition map must be smooth.

**Prerequisites:** transition map, C^k and smooth functions

$$
\phi_i\circ\phi_j^{-1}\in C^\infty \text{ on } \phi_j(U_i\cap U_j)
$$

**Where:** GA §C.7 p.572 (pdf 589); GA §C.7 p.573 (pdf 590)

### maximal atlas

*definition · developed* · also: complete atlas, differentiable structure

The atlas containing every chart compatible with a given smooth atlas; fixing it removes spurious distinctions between the same manifold described by different atlases.

**How introduced:** §C.7 immediately after compatibility; Example C.8 uses the maximal atlas containing the identity on R.

**Prerequisites:** compatible (C^infinity-related) charts, atlas

**Where:** GA §C.7 p.573 (pdf 590)

### differentiable manifold

*definition · core* · also: smooth manifold

A manifold together with a maximal atlas of mutually C^infinity-compatible charts, so that smoothness of functions, curves and maps is chart independent.

**How introduced:** §C.7 as the fix for chart-dependent differentiability; simplest example R with the identity chart (Example C.8).

**Prerequisites:** manifold, maximal atlas

**Where:** GA §C.7 p.573 (pdf 590)

### differentiable map between manifolds

*definition · developed* · also: smooth map

f: M -> N is differentiable if for all charts (U, phi) of M and (V, psi) of N its representation psi o f o phi^{-1} from R^m to R^n is differentiable.

**How introduced:** §C.7, reusing the sandwich picture of Fig. C.12.

**Prerequisites:** coordinate representation of a function, differentiable manifold

$$
\psi\circ f\circ\phi^{-1}:\mathbb R^m\to\mathbb R^n
$$

**Where:** GA §C.7 p.573 (pdf 590)

### diffeomorphism

*definition · core*

A bijective smooth map between differentiable manifolds whose inverse is also smooth; diffeomorphic manifolds have equal dimension and are regarded as the same smooth manifold.

**How introduced:** §C.7 after differentiable maps, tested on x, x^2, x^3 and a linear map of R^2 (Example C.9), and contrasted with homeomorphism as smooth versus continuous deformation; then related to GR's gauge freedom.

**Prerequisites:** differentiable map between manifolds, bijection, homeomorphism

$$
y=\psi\circ f\circ\phi^{-1}(x)\in C^\infty
$$

$$
x=\phi\circ f^{-1}\circ\psi^{-1}(y)\in C^\infty
$$

**Where:** GA §C.7 p.573 (pdf 590); GA §C.7 p.574 (pdf 591); GA §Chapter summary p.580 (pdf 597)

### Jacobian determinant

*mathematical-object · introduced* · also: Jacobian

The determinant of the matrix of partial derivatives of a map's component functions; a non-zero value at a point guarantees local smooth invertibility there (inverse function theorem).

**How introduced:** Margin note in Example C.9 computes 5/4 for phi(x,y) = (x + y/2, y - x/2).

**Prerequisites:** C^k and smooth functions

$$
J=\det(\partial\phi^i/\partial x^j)
$$

**Notes:** Non-zero Jacobian everywhere gives only local invertibility; the linear example is globally invertible because it is linear.

**Where:** GA §C.7 p.573 (pdf 590)

### active coordinate transformation

*definition · developed* · also: point transformation, active diffeomorphism

A transformation that moves points of the manifold to other points (as opposed to relabelling the same point); a diffeomorphism from a manifold to itself is its most general smooth form.

**How introduced:** §C.7 discussion of why diffeomorphisms matter for GR, and restated in the chapter summary.

**Prerequisites:** diffeomorphism

**Where:** GA §C.7 p.574 (pdf 591); GA §Chapter summary p.580 (pdf 597)

### diffeomorphism invariance

*principle · developed* · also: general covariance, gauge symmetry of GR

Physical content of GR is unchanged when all fields are pushed along by a diffeomorphism of spacetime to itself; configurations related this way describe the same physics, so diffeomorphisms are the gauge symmetries of the theory.

**How introduced:** §C.7: if moving points with a diffeomorphism leaves the physics unchanged, the moved and unmoved configurations are indistinguishable; used in Example C.10.

**Prerequisites:** diffeomorphism, active coordinate transformation

**Where:** GA §C.7 p.574 (pdf 591)

### Lie derivative as generator of a diffeomorphism

*operation · revisited* · also: flow along a vector field, generator

The one-parameter family of diffeomorphisms obtained by flowing along the integral curves of a vector field u has u as its generator, and the Lie derivative L_u measures the first-order change of a tensor under that flow; for the metric (L_u g)_{mu nu} = 2 u_(mu;nu) with a metric-compatible connection.

**How introduced:** §C.7 remark that the Lie derivative of Chapter 33 is most generally defined via diffeomorphisms, with the metric formula recalled in a margin note for Example C.10.

**Prerequisites:** diffeomorphism, tangent vector as directional derivative

$$
(\mathcal L_u g)_{\mu\nu}=u^\sigma g_{\mu\nu;\sigma}+g_{\mu\sigma}u^\sigma{}_{;\nu}+g_{\sigma\nu}u^\sigma{}_{;\mu}=2u_{(\mu;\nu)}
$$

**Where:** GA §C.7 p.574 (pdf 591)

### Killing vector field

*mathematical-object · mention*

A vector field whose flow is an isometry, so L_u g = 0; each one yields a conserved quantity along geodesics.

**How introduced:** Margin note in §C.7: because the Lie derivative is built from diffeomorphisms, so is the notion of Killing vectors.

**Prerequisites:** Lie derivative as generator of a diffeomorphism

$$
u_{(\mu;\nu)}=0
$$

**Where:** GA §C.7 p.574 (pdf 591)

### conservation of energy-momentum from diffeomorphism invariance

*theorem · developed* · also: nabla . T = 0 from general covariance, Noether-type identity

If the matter action is unchanged when the metric is varied by the Lie derivative along any vector field (and the matter fields obey their equations of motion), then the energy-momentum tensor defined from the action has vanishing covariant divergence.

**How introduced:** Example C.10 in §C.7, fulfilling a promise made in Chapter 12 and using the variational definition of T from Chapter 40.

**Prerequisites:** diffeomorphism invariance, Lie derivative as generator of a diffeomorphism, energy-momentum tensor from the action

$$
\nabla_\mu T^{\mu\nu}=0
$$

**Notes:** The book does not mention that the matter field equations must hold for the argument to go through.

**Where:** GA §C.7 p.574 (pdf 591)

### energy-momentum tensor from the action

*definition · revisited* · also: Hilbert stress-energy tensor

T^{mu nu} equals 2/sqrt(-g) times the functional derivative of sqrt(-g) L_m with respect to g_{mu nu}.

**How introduced:** Quoted from Chapter 40 in Example C.10.

$$
T^{\mu\nu}=\frac{2}{\sqrt{-g}}\frac{\delta(\sqrt{-g}\mathcal L_m)}{\delta g_{\mu\nu}}
$$

**Where:** GA §C.7 p.574 (pdf 591)

### compactness

*definition · developed* · also: compact region, compact space

A region is compact if every sequence in it has an accumulation point lying in the region (for metric spaces equivalent to: every open cover has a finite subcover); in R^n this means closed and bounded.

**How introduced:** §C.8 as the upgrade of a closed interval: no escape to infinity, no missing interior pieces, no missing boundary; tested with 1/n on [0,1] and (0,1]; the open-cover version is in a margin note.

**Prerequisites:** open cover, open and closed intervals

**Notes:** Used back in Example C.2 to show a line is not homeomorphic to a circle.

**Where:** GA §C.8 p.575 (pdf 592); GA p.566 (pdf 583); GA §C.4 p.569 (pdf 586)

### Heine-Borel theorem

*theorem · mention*

A subset of R (or R^n) is compact if and only if it is closed and bounded; in particular closed intervals are compact.

**How introduced:** Cited without proof in §C.8 with a pointer to Spivak.

**Prerequisites:** compactness

**Where:** GA §C.8 p.575 (pdf 592)

### bounded set

*definition · mention*

A set that lies within some finite distance of a point; the notion requires a metric.

**How introduced:** Margin note in §C.8 accompanying the closed-and-bounded criterion.

**Prerequisites:** metric space

**Where:** GA §C.8 p.575 (pdf 592)

### parametrized curve on a manifold

*mathematical-object · developed* · also: curve

A map c from an interval of real parameter values into the manifold; its coordinate description is phi o c, giving x^mu(lambda).

**How introduced:** §C.9 with Fig. C.13, as the ingredient needed to define tangent vectors.

**Prerequisites:** map, coordinate function

$$
x^\mu=\phi\circ c(\lambda)
$$

**Where:** GA §C.9 p.575 (pdf 592); GA §C.9 p.576 (pdf 593)

### tangent vector as directional derivative

*definition · core* · also: tangent vector, vector as derivative operator

At P = c(0), the tangent vector of curve c acts on any smooth function f by returning d(f o c)/dlambda at lambda = 0; in coordinates it is v = (dx^mu/dlambda) partial/partial x^mu.

**How introduced:** §C.10: arrows are unavailable on a manifold (no origin or straightness), so a vector is defined by what it does to functions; the chain rule through a chart gives the coordinate form (Fig. C.14).

**Prerequisites:** parametrized curve on a manifold, coordinate representation of a function, composition of maps

$$
v[f]=\left.\frac{d(f\circ c)}{d\lambda}\right|_{0}
$$

$$
v[f]=\left.\frac{dx^\mu(c(\lambda))}{d\lambda}\right|_{0}\frac{\partial f}{\partial x^\mu}
$$

**Where:** GA §C.10 p.576 (pdf 593); GA §C.10 p.577 (pdf 594); GA §Chapter summary p.580 (pdf 597)

### derivation

*definition · developed* · also: linear Leibniz operator

A map v from smooth functions to real numbers at a point that is linear and satisfies the product (Leibniz) rule; at each point derivations are in one-to-one correspondence with tangent vectors.

**How introduced:** §C.10 'firming up' the definition after Example C.13.

**Prerequisites:** tangent vector as directional derivative, C^k and smooth functions

$$
v(\alpha f+\beta g)=\alpha v(f)+\beta v(g)
$$

$$
v(fg)=f\,v(g)+g\,v(f)
$$

**Where:** GA §C.10 p.577 (pdf 594)

### coordinate basis vectors

*mathematical-object · developed* · also: partial/partial x^mu, e_mu

The derivative operators partial/partial x^mu at a point, which form a basis of the tangent space associated with a chart; components are then v^mu = dx^mu/dlambda.

**How introduced:** Read off from the chain-rule expression (C.19)-(C.20), with the order of factors swapped to match v = v^mu e_mu.

**Prerequisites:** tangent vector as directional derivative

$$
v=v^\mu e_\mu,\ e_\mu=\partial/\partial x^\mu
$$

$$
v[x^\nu]=dx^\nu/d\lambda
$$

**Where:** GA §C.10 p.577 (pdf 594); GA §C.11 p.578 (pdf 595)

### equivalence class of curves

*definition · introduced*

Curves through the same point whose coordinate velocities agree at that point are identified; each tangent vector corresponds to one such class.

**How introduced:** §C.10 via (C.23)-(C.24): many curves share a velocity, so a vector cannot be tied to one particular curve.

**Prerequisites:** parametrized curve on a manifold, tangent vector as directional derivative

**Where:** GA §C.10 p.577 (pdf 594)

### tangent space

*mathematical-object · core* · also: T_P M

The vector space of all tangent vectors at a point P of the manifold, with dimension equal to that of the manifold; there is a separate one at each point.

**How introduced:** §C.10: tangent vectors are said to live not in the manifold but in a space 'floating above' each point (Fig. C.15a), contrasted with the embedded tangent plane of earlier chapters (Fig. C.15b).

**Prerequisites:** equivalence class of curves, derivation

**Where:** GA §C.10 p.576 (pdf 593); GA §C.10 p.577 (pdf 594)

### fibre bundle

*mathematical-object · core* · also: bundle, total space B

A manifold B built from a base manifold M and a fibre manifold V, with a continuous projection onto M such that the preimage of each base point is a copy of V and small regions look like products; dim B = dim M + dim V.

**How introduced:** §C.11 by redrawing the tangent lines of a curve as non-intersecting vertical lines and lifting them above the curve (Figs. C.16-C.17); margin note in §C.10 anticipates it.

**Prerequisites:** manifold, tangent space, canonical projection

$$
\dim\mathcal B=\dim\mathcal M+\dim\mathcal V
$$

**Where:** GA §C.10 p.576 (pdf 593); GA §C.11 p.578 (pdf 595); GA §Chapter summary p.580 (pdf 597)

### base space and fibre

*definition · developed* · also: base manifold, fibre V

The base space is the manifold M over which a bundle is built; the fibre is the manifold V of which one copy stands above each base point.

**How introduced:** §C.11 following the lifting construction; tangent vectors at a point pictured as beads on its fibre.

**Prerequisites:** fibre bundle

**Where:** GA §C.11 p.578 (pdf 595)

### canonical projection

*operation · developed* · also: pi, bundle projection

The continuous map pi: B -> M sending every point of a fibre to the base point it lies over, forgetting the fibre coordinate.

**How introduced:** §C.11 as undoing the lifting construction (Figs. C.17-C.18).

**Prerequisites:** fibre bundle

$$
\pi:\mathcal B\to\mathcal M
$$

**Where:** GA §C.11 p.578 (pdf 595)

### tangent bundle

*mathematical-object · developed* · also: TM

The bundle whose fibre over each point is the tangent space there; a point of TM is a point of M together with a tangent vector at it, so dim TM = 2 dim M.

**How introduced:** §C.11 as the motivating special case, with TS^1 as the cylinder in Example C.14 and Fig. C.19.

**Prerequisites:** fibre bundle, tangent space

$$
v=y\,\partial/\partial\theta,\ (\theta,y)\ \text{coordinates on } \mathcal TS^1
$$

**Where:** GA §C.11 p.578 (pdf 595); GA §C.11 p.579 (pdf 596)

### trivial (product) bundle

*definition · developed* · also: product space M x V, globally trivial bundle

A bundle that is globally the Cartesian product M x V, whose points are pairs (a, b) with a in M and b in V.

**How introduced:** §C.11 with a grid-rectangle picture (Fig. C.18); TS^1 = S^1 x R is the cylinder example.

**Prerequisites:** fibre bundle

$$
\mathcal B=\mathcal M\times\mathcal V
$$

**Where:** GA §C.11 p.578 (pdf 595); GA §C.11 p.579 (pdf 596)

### local versus global triviality

*definition · developed* · also: locally trivial bundle, twisted bundle

Every bundle looks like a product over small enough regions of the base (local triviality); it is globally trivial only if a single product description works over the whole base. A twisted bundle is locally but not globally a product.

**How introduced:** §C.11 posed as a question after TS^1, answered by the Moebius example: cutting out a base point leaves something deformable to a cylinder, but gluing the two pieces with a flip does not.

**Prerequisites:** trivial (product) bundle

**Notes:** The book's phrase that bundles are locally trivial 'if they are formed from a product space' blurs the definition; local triviality is part of what a bundle is.

**Where:** GA §C.11 p.578 (pdf 595); GA §C.11 p.579 (pdf 596)

### Moebius bundle

*solution-or-model · developed* · also: Moebius strip, twisted line bundle over S^1

The real line bundle over the circle obtained by gluing the ends of a strip with a reversal of the fibre direction; locally a product, globally not diffeomorphic to the cylinder.

**How introduced:** Example C.15 with a photograph of rods on a ring tilting through a half turn (Fig. C.20b).

**Prerequisites:** local versus global triviality

**Where:** GA §C.11 p.579 (pdf 596)

### cross section

*definition · developed* · also: section, lift s

A continuous map s: M -> B choosing one point on each fibre, so that projecting back gives the identity: pi o s = I; for a product bundle it is the graph of a V-valued function on M, and for a tangent bundle it is a vector field.

**How introduced:** §C.11 formal characterization of bundles, pictured as a wavy loop around a cylinder with upward lift arrows from the base (Fig. C.21).

**Prerequisites:** canonical projection, fibre bundle

$$
\pi\circ s=I
$$

**Notes:** The book does not say explicitly that sections of the tangent bundle are vector fields; this is the key link to physics.

**Where:** GA §C.11 p.579 (pdf 596); GA §Chapter summary p.580 (pdf 597)

### zero section

*definition · introduced*

The section of a vector bundle that picks the zero vector in every fibre.

**How introduced:** Example C.16: any section of the Moebius bundle must meet it, while a section of the cylinder can avoid it, which distinguishes the two bundles.

**Prerequisites:** cross section

**Where:** GA §C.11 p.579 (pdf 596)

### gauge fields as bundle structures

*historical-idea · mention* · also: physics of gauges

Gauge theories are naturally formulated with fields as sections of bundles over spacetime and potentials as connections on those bundles.

**How introduced:** Only signposted in the opening paragraph as the reason bundles appear at the end of the appendix.

**Prerequisites:** fibre bundle

**Where:** GA p.566 (pdf 583)

## Key equations

### (C.1) Euclidean distance in R^n · supporting · GA §C.1 p.566 (pdf 583)

$$
|x-y| = \left[\sum_{\mu=1}^{n}(x^\mu-y^\mu)^2\right]^{1/2}
$$

Makes R^n a metric space; used to define open balls and hence open sets.

**Symbols:** x, y points of R^n with components x^mu, y^mu

### Open ball · supporting · GA §C.1 p.566 (pdf 583)

$$
B_r(y)=\{x\in\mathbb R^n : |x-y|<r\}
$$

The basic open set; open sets are unions of these.

**Symbols:** r radius, y centre

### (C.2) Map notation · supporting · GA §C.2 p.567 (pdf 584)

$$
f:\mathcal M\to\mathcal N
$$

f takes elements of M to elements of N.

**Symbols:** M domain, N target

### (C.3) Map on elements · supporting · GA §C.2 p.567 (pdf 584)

$$
f: x\mapsto y=f(x)
$$

Element-level statement of the same map.

### Composition · supporting · GA §C.2 p.567 (pdf 584)

$$
g\circ f:\mathcal M\to\mathcal L,\quad (g\circ f)(x)=g(f(x))
$$

Chaining maps, the core operation of the appendix.

**Symbols:** f: M -> N, g: N -> L

### (C.4) Coordinates of a point · central · GA §C.5 p.570 (pdf 587)

$$
x^\mu=\phi(\mathcal P)
$$

A chart map turns a point of the manifold into an m-tuple of numbers.

**Symbols:** phi coordinate function on U, P a point in U

### (C.5) Point from coordinates · supporting · GA §C.5 p.570 (pdf 587)

$$
\mathcal P=\phi^{-1}(x^\mu)
$$

Because phi is a homeomorphism it can be inverted: coordinates determine a unique point of U.

### (C.6) Coordinate transformation as transition map · central · GA §C.5 p.571 (pdf 588)

$$
y^\mu=\psi\circ\phi^{-1}(x^\mu)
$$

The coordinates of the same point in a second chart are obtained by going back to the manifold with phi^{-1} and out again with psi.

**Symbols:** (U, phi), (V, psi) overlapping charts; x^mu, y^mu the two coordinate labels of P

### Transition maps in the formal definition (corrected direction) · supporting · GA §C.5 p.571 (pdf 588)

$$
\phi_i\circ\phi_j^{-1}:\ \phi_j(U_i\cap U_j)\to\phi_i(U_i\cap U_j)
$$

On each overlap the composite of one chart with the inverse of another maps between open subsets of R^m.

**Symbols:** U_i, U_j overlapping chart domains

### (C.7) Coordinate representation of a function · central · GA §C.6 p.572 (pdf 589)

$$
y=f\circ\phi^{-1}(x^1,\dots,x^m)
$$

What we usually write as f(x^1,...,x^m) is the manifold function f composed with the inverse chart.

**Symbols:** f: M -> R, phi chart on U

### (C.8) Coordinate representation of a map between manifolds · central · GA §C.6 p.572 (pdf 589)

$$
(y^1,\dots,y^m)=\psi\circ f\circ\phi^{-1}(x^1,\dots,x^m)
$$

A map between manifolds becomes an ordinary tuple-valued function between coordinate spaces once sandwiched between charts.

**Symbols:** (U, phi) chart on M, (V, psi) chart on N

### (C.9) Chart change for a function · derivation-step · GA §C.7 p.572 (pdf 589)

$$
f\circ\psi^{-1}=(f\circ\phi^{-1})\circ(\phi\circ\psi^{-1})
$$

Shows that differentiability of a function in one chart transfers to another chart only if the transition map is differentiable.

### (C.10) Smooth compatibility condition · central · GA §C.7 p.573 (pdf 590)

$$
\phi_i\circ\phi_j^{-1}\in C^\infty\ \text{whenever}\ U_i\cap U_j\neq\varnothing
$$

Defines C^infinity-related charts; a maximal atlas of such charts makes the manifold differentiable.

### Differentiable map between manifolds · supporting · GA §C.7 p.573 (pdf 590)

$$
\psi\circ f\circ\phi^{-1}:\mathbb R^m\to\mathbb R^n\ \text{differentiable for all charts}
$$

Chart-level criterion for smoothness of maps between manifolds.

**Symbols:** m, n dimensions of M and N

### Diffeomorphism condition · central · GA §C.7 p.573 (pdf 590)

$$
y=\psi\circ f\circ\phi^{-1}(x)\in C^\infty,\qquad x=\phi\circ f^{-1}\circ\psi^{-1}(y)\in C^\infty
$$

A diffeomorphism is invertible with both the map and its inverse smooth in coordinates; this forces m = n.

### Jacobian of the test map in Example C.9 · supporting · GA §C.7 p.573 (pdf 590)

$$
\phi(x,y)=\left(x+\tfrac{y}{2},\ y-\tfrac{x}{2}\right),\quad \det\begin{pmatrix}1&\tfrac12\\-\tfrac12&1\end{pmatrix}=\tfrac54
$$

Non-vanishing Jacobian of a linear map of R^2 shows it is invertible and hence a diffeomorphism.

### (C.11) Variation of the matter action with the metric · derivation-step · GA §C.7 p.574 (pdf 591)

$$
\delta S=\int d^4x\,\frac{\delta(\sqrt{-g}\,\mathcal L_m)}{\delta g_{\mu\nu}}\,\delta g_{\mu\nu}
$$

First-order change of the matter action when the metric components change.

**Symbols:** g determinant of the metric, L_m matter Lagrangian density

### (C.12) Lie derivative of the metric (margin note, indices corrected) · supporting · GA §C.7 p.574 (pdf 591)

$$
(\mathcal L_u g)_{\mu\nu}=u^\sigma g_{\mu\nu;\sigma}+g_{\mu\sigma}u^\sigma{}_{;\nu}+g_{\sigma\nu}u^\sigma{}_{;\mu}=2u_{(\mu;\nu)}
$$

Change of the metric under the flow generated by u; the first term vanishes for a metric-compatible connection, leaving the symmetrized covariant derivative.

**Symbols:** u generating vector field; parentheses denote symmetrization with a 1/2

### Metric variation generated by a diffeomorphism · derivation-step · GA §C.7 p.574 (pdf 591)

$$
\delta g_{\mu\nu}=(\mathcal L_u g)_{\mu\nu}=2u_{(\mu;\nu)}
$$

Infinitesimal diffeomorphisms change the metric by the Lie derivative along their generator.

### (C.13) Diffeomorphism invariance condition · derivation-step · GA §C.7 p.574 (pdf 591)

$$
0=\int d^4x\,\frac{\delta(\sqrt{-g}\,\mathcal L_m)}{\delta g_{\mu\nu}}\,u_{\mu;\nu}
$$

Invariance of the action under the metric change; the symmetrization is dropped because the functional derivative is symmetric (factor 2 absorbed into the zero).

### (C.14) After integration by parts · derivation-step · GA §C.7 p.574 (pdf 591)

$$
0=-\int d^4x\,\sqrt{-g}\,u_\nu\,\nabla_\mu\!\left[\frac{1}{\sqrt{-g}}\frac{\delta(\sqrt{-g}\,\mathcal L_m)}{\delta g_{\mu\nu}}\right]
$$

Moving the derivative off u (discarding a boundary term) leaves u times a covariant divergence; since u is arbitrary the bracketed divergence must vanish.

### (C.15) Energy-momentum tensor from the action · supporting · GA §C.7 p.574 (pdf 591)

$$
T^{\mu\nu}=\frac{2}{\sqrt{-g}}\frac{\delta(\sqrt{-g}\,\mathcal L_m)}{\delta g_{\mu\nu}}
$$

Definition quoted from Chapter 40; identifies the bracket in (C.14) with T/2.

### Conservation law · central · GA §C.7 p.574 (pdf 591)

$$
\nabla_\mu T^{\mu\nu}=T^{\mu\nu}{}_{;\mu}=0
$$

Result of Example C.10: local energy-momentum conservation follows from diffeomorphism invariance of the matter action.

### (C.16) Coordinates along a curve · supporting · GA §C.9 p.576 (pdf 593)

$$
x^\mu=\phi\circ c(\lambda)
$$

A curve on the manifold, viewed through a chart, becomes an ordinary parametrized curve in R^m.

**Symbols:** c: [a,b] -> M, lambda parameter

### (C.17) Rate of change along a curve · central · GA §C.10 p.576 (pdf 593)

$$
\left.\frac{d f(c(\lambda))}{d\lambda}\right|_{\lambda=0}=\left.\frac{d(f\circ c)}{d\lambda}\right|_{\lambda=0}
$$

The basic ingredient of a tangent vector: how fast a function changes as one moves along the curve through P = c(0).

**Symbols:** f: M -> R smooth function

### (C.18) Splitting through the chart · derivation-step · GA §C.10 p.576 (pdf 593)

$$
f\circ c=(f\circ\phi^{-1})\circ(\phi\circ c)
$$

Inserting the identity phi^{-1} o phi separates the function's coordinate representation from the curve's coordinate representation.

### (C.19) Chain rule on the manifold · derivation-step · GA §C.10 p.576 (pdf 593)

$$
\frac{d(f\circ c)}{d\lambda}=\frac{\partial}{\partial x^\mu}(f\circ\phi^{-1})\,\frac{d}{d\lambda}(\phi\circ c(\lambda))=\left.\frac{\partial f(x^\mu)}{\partial x^\mu}\frac{dx^\mu(c(\lambda))}{d\lambda}\right|_{\lambda=0}
$$

Ordinary multivariable chain rule applied to the two coordinate representations.

### (C.20) Tangent vector in coordinates · central · GA §C.10 p.577 (pdf 594)

$$
v[f]=\left.\frac{dx^\mu(c(\lambda))}{d\lambda}\right|_{\lambda=0}\frac{\partial f}{\partial x^\mu}
$$

Defines the tangent vector: components are the coordinate velocities of the curve and basis vectors are partial derivative operators, matching v = v^mu e_mu.

**Symbols:** v^mu = dx^mu/dlambda, e_mu = partial/partial x^mu

### (C.21) Coordinate function along the curve · derivation-step · GA §C.10 p.577 (pdf 594)

$$
\phi^\nu\circ c(\lambda)=\phi^\nu(c(\lambda))=x^\nu(\lambda)
$$

The nu-th coordinate evaluated along the curve, used as the test function in Example C.13.

**Symbols:** phi^nu nu-th component of the chart map

### (C.22) Vector acting on a coordinate · supporting · GA §C.10 p.577 (pdf 594)

$$
v[x^\nu]=\frac{dx^\mu}{d\lambda}\frac{\partial x^\nu}{\partial x^\mu}=\left.\frac{dx^\nu(\lambda)}{d\lambda}\right|_{\lambda=0}
$$

Feeding a coordinate function to the vector returns its nu-th component, because partial x^nu/partial x^mu is a Kronecker delta.

### Derivation axioms · central · GA §C.10 p.577 (pdf 594)

$$
v(\alpha f+\beta g)=\alpha\,v(f)+\beta\,v(g),\qquad v(fg)=f\,v(g)+g\,v(f)
$$

Coordinate-free characterization of tangent vectors at a point as linear maps on smooth functions obeying the product rule.

**Symbols:** alpha, beta real numbers; f, g in C^infinity(M); functions evaluated at P

### (C.23) Curves through the same point · derivation-step · GA §C.10 p.577 (pdf 594)

$$
c_1(\lambda=0)=c_2(\lambda=0)=\mathcal P
$$

First condition for two curves to define the same tangent vector.

### (C.24) Equal coordinate velocities · supporting · GA §C.10 p.577 (pdf 594)

$$
\left.\frac{dx^\mu(c_1(\lambda))}{d\lambda}\right|_{\lambda=0}=\left.\frac{dx^\mu(c_2(\lambda))}{d\lambda}\right|_{\lambda=0}
$$

Second condition; together with (C.23) defines the equivalence class of curves identified with a tangent vector.

### Dimension of a bundle · supporting · GA §C.11 p.578 (pdf 595)

$$
\dim\mathcal B=\dim\mathcal M+\dim\mathcal V
$$

The total space has the dimensions of base and fibre added.

### Tangent vector on the circle · supporting · GA §C.11 p.578 (pdf 595)

$$
v=y\,\frac{\partial}{\partial\theta}\equiv y\,e_\theta
$$

Coordinates (theta, y) on TS^1: position on the circle and amplitude along the fibre.

**Symbols:** theta angle on S^1, y fibre coordinate

### (C.25) Section condition · central · GA §C.11 p.579 (pdf 596)

$$
\pi\circ s=I
$$

Lifting the base into the bundle and projecting back returns every base point to itself.

**Symbols:** s: M -> B section, pi: B -> M projection, I identity on M

### (C.26) Summary definition of a tangent vector · central · GA §Chapter summary p.580 (pdf 597)

$$
v[f]=\frac{d(f\circ c)}{d\lambda}
$$

Chapter-summary restatement of the derivative-along-a-curve definition.

## Figures

### Unlabelled figure · other · GA p.565 (pdf 582)

`book-sources/gifted-amateur/pages/page-582/img-346.jpeg`

**Caption (paraphrased):** Appendix badge (no caption).

**What it shows:** A large bold black capital letter C on a plain light-grey background: the appendix identifier tile from the opening page layout.

**What it teaches:** Nothing conceptual; page decoration.

**App redesign (not-worth-redesigning, low priority):** None; decorative chapter tile. — *Interaction:* None.

### Fig. C.1 · schematic · GA p.565 (pdf 582)

`book-sources/gifted-amateur/pages/page-582/img-347.jpeg`

**Caption (paraphrased):** The manifold-with-metric sits on top of a stack of increasingly structured mathematical notions.

**What it shows:** Four stacked rectangles forming a stepped pyramid. From the widest at the bottom upward they read: Set; Topological space; Manifold M; and at the narrow top (M, g).

**What it teaches:** Geometry is layered: each rung adds structure (open sets, local Euclidean charts and smoothness, then a metric) to the one below.

**Concepts:** topological space, manifold, pseudo-Riemannian manifold

**App redesign (interactive-2d, medium priority):** Clickable structure ladder: each layer expands into what it adds, which questions become answerable (is it connected? can we differentiate? how long is this curve?), and which example objects qualify. — *Interaction:* Learner clicks a layer or drags a sample object (branching line, double cone, sphere with round metric) up the ladder; the ladder highlights the highest level the object reaches and explains the failing condition.

### Fig. C.2 (a)-(d) · schematic · GA §C.1 p.566 (pdf 583)

**Caption (paraphrased):** Open interval, closed interval, union of two sets, and intersection of two sets.

**What it shows:** Vector line art that the image export dropped (checked on the page render): (a) a horizontal line cut by two outward-facing round parentheses for an open interval; (b) the same line with square brackets for a closed interval; (c) two overlapping ellipses A and B, both hatched to show the union; (d) the same two overlapping ellipses with only their overlap marked, for the intersection.

**What it teaches:** Notation for intervals and basic set operations.

**Concepts:** open and closed intervals

**App redesign (interactive-2d, low priority):** Venn and interval playground: two draggable shapes with a selector for union, intersection, subset; an interval with toggleable endpoint brackets. — *Interaction:* Learner toggles open/closed endpoints and drags sets; the shaded region and the symbolic expression update together.

### Fig. C.2 (e) · schematic · GA §C.1 p.566 (pdf 583)

`book-sources/gifted-amateur/pages/page-583/img-348.jpeg`

**Caption (paraphrased):** A is a subset of B.

**What it shows:** A small ellipse labelled A drawn completely inside a larger ellipse labelled B, unshaded.

**What it teaches:** Subset notation A inside B.

**App redesign (not-worth-redesigning, low priority):** Merge into the set-operations playground above. — *Interaction:* Drag A; indicator shows whether A is still a subset of B.

### Fig. C.2 (f) · schematic · GA §C.1 p.566 (pdf 583)

`book-sources/gifted-amateur/pages/page-583/img-349.jpeg`

**Caption (paraphrased):** An open ball in the plane.

**What it shows:** A square frame representing R^2 containing a dashed circle; the dashing signals that the boundary circle is excluded.

**What it teaches:** Open balls exclude their boundary; dashed boundaries mean 'not included'.

**Concepts:** open ball, open set

**App redesign (interactive-2d, medium priority):** Open-set tester: learner clicks points of a region; around each point the largest ball fitting inside is drawn, and boundary points visibly fail when the boundary is included. — *Interaction:* Toggle region boundary between included and excluded; click points near the edge and watch whether a ball of positive radius fits.

### Fig. C.2 (g) · schematic · GA §C.1 p.566 (pdf 583)

`book-sources/gifted-amateur/pages/page-583/img-350.jpeg`

**Caption (paraphrased):** An open cover of a subset of the plane.

**What it shows:** Inside a square frame, a cluster of about eight small overlapping dashed circles covers an irregular region.

**What it teaches:** An open cover is a family of open sets whose union contains the set.

**Concepts:** open cover

**App redesign (interactive-2d, medium priority):** Cover-building game: learner places discs to cover a shape, then tries to discard discs while keeping coverage; for an open interval near its missing endpoint a finite subcover cannot be found, previewing compactness. — *Interaction:* Place and remove discs; a coverage meter and a 'finite subcover found?' indicator update.

### Fig. C.2 (h) · schematic · GA §C.1 p.566 (pdf 583)

`book-sources/gifted-amateur/pages/page-583/img-351.jpeg`

**Caption (paraphrased):** A non-Hausdorff space, pictured as branching.

**What it shows:** Two thin grey rectangular sheets crossing each other at right angles, one roughly horizontal and one vertical, intersecting along a common line: a branching or forking surface.

**What it teaches:** Spaces that branch fail the separation property the book assumes; such spaces are excluded.

**Concepts:** Hausdorff property

**App redesign (interactive-2d, low priority):** Line-with-two-origins demo: a real line whose origin is doubled; learner shrinks neighbourhoods of the two origins and sees they always overlap. — *Interaction:* Slider shrinks neighbourhood radius; overlap region stays non-empty for the doubled origin but separates for ordinary distinct points.

### Fig. C.3 · schematic · GA §C.2 p.567 (pdf 584)

`book-sources/gifted-amateur/pages/page-584/img-352.jpeg`

**Caption (paraphrased):** A function viewed as a map from one space to another.

**What it shows:** Two irregular closed blobs labelled M (left) and N (right). A dot x in M is joined by a curved arrow labelled f to a dot f(x) in N.

**What it teaches:** The abstract map picture used for every later construction.

**Concepts:** map

**App redesign (interactive-2d, low priority):** Reusable 'map card' component: drag a point in M and see its image move in N; used as the base widget for all later composite-map diagrams. — *Interaction:* Drag x; f(x) follows; learner can swap f among a few preset maps.

### Fig. C.4 (a) · schematic · GA §C.3 p.567 (pdf 584)

`book-sources/gifted-amateur/pages/page-584/img-353.jpeg`

**Caption (paraphrased):** A many-to-one mapping.

**What it shows:** Blob M (left) contains a small dotted shaded patch holding several points; a bundle of thin arrows from those points converges onto a single point in blob N (right).

**What it teaches:** Several inputs can share one output, so the inverse image of a point need not be a point.

**Concepts:** injective map, image and inverse image

**App redesign (interactive-2d, medium priority):** Arrow-diagram classifier: learner draws arrows from dots in M to dots in N; badges for one-to-one, onto, bijective light up live. — *Interaction:* Click-drag arrows between two finite dot sets; the classification and existence of an inverse update.

### Fig. C.4 (b) · schematic · GA §C.3 p.567 (pdf 584)

`book-sources/gifted-amateur/pages/page-584/img-354.jpeg`

**Caption (paraphrased):** An into mapping that is one-to-one but does not fill the target.

**What it shows:** Blob M fully hatched; about eight arrows from distinct points land at distinct points clustered in a small lightly shaded part of blob N, leaving most of N unreached.

**What it teaches:** A map defined on all of M can be one-to-one yet miss much of N (not onto).

**Concepts:** injective map, surjective map

**App redesign (not-worth-redesigning, low priority):** Same classifier widget with the target region shaded by coverage. — *Interaction:* As above.

### Fig. C.4 (c) · schematic · GA §C.3 p.567 (pdf 584)

`book-sources/gifted-amateur/pages/page-584/img-355.jpeg`

**Caption (paraphrased):** A bijection: one-to-one and onto.

**What it shows:** Both blobs fully hatched; parallel arrows pair each marked point of M with a distinct point of N spread across all of N.

**What it teaches:** Bijections pair up points perfectly, so an inverse map exists.

**Concepts:** bijection

**App redesign (not-worth-redesigning, low priority):** Same classifier widget; reversing all arrows produces the inverse map only when the bijection badge is lit. — *Interaction:* Button 'reverse arrows'; widget explains why the reversed diagram fails to be a map in cases (a) and (b).

### Fig. C.5 (a) · function-plot · GA §C.3 p.568 (pdf 585)

`book-sources/gifted-amateur/pages/page-585/img-356.jpeg`

**Caption (paraphrased):** Graph of a one-to-one but not onto real function (caption misnumbers the example as C.5; it belongs to Example C.1).

**What it shows:** x-y axes with a monotonically increasing curve that hugs a horizontal level just above the x-axis on the left and rises steeply on the right, like an exponential; it never reaches negative y.

**What it teaches:** Strictly increasing means one-to-one; a range bounded below means not onto R.

**Concepts:** injective map, surjective map

**App redesign (interactive-plot, medium priority):** Horizontal-line-test explorer for real functions: learner sweeps a horizontal line and sees the number of intersections, plus shading of the unreached part of the y-axis. — *Interaction:* Drag horizontal line; pick among exponential, cubic with wiggle, x^3, x^2 or type a formula; badges update.

### Fig. C.5 (b) · function-plot · GA §C.3 p.568 (pdf 585)

`book-sources/gifted-amateur/pages/page-585/img-357.jpeg`

**Caption (paraphrased):** Graph of an onto but not one-to-one function.

**What it shows:** Axes with a cubic-like curve rising from the bottom left, making a small hump above the axis and a dip below near the origin, then rising steeply to the top right.

**What it teaches:** Covers every y value but some values are hit three times.

**Concepts:** surjective map, injective map

**App redesign (not-worth-redesigning, low priority):** Covered by the horizontal-line-test explorer. — *Interaction:* As above.

### Fig. C.5 (c) · function-plot · GA §C.3 p.568 (pdf 585)

`book-sources/gifted-amateur/pages/page-585/img-358.jpeg`

**Caption (paraphrased):** Graph of a bijection.

**What it shows:** Axes with an increasing curve that is flat at the origin (horizontal tangent) and steep far from it, like y = x^3, extending from the bottom left to the top right.

**What it teaches:** Monotone and unbounded in both directions: one-to-one and onto. The same shape later reappears as the non-diffeomorphism x^3 of Example C.9.

**Concepts:** bijection, diffeomorphism

**App redesign (interactive-plot, medium priority):** Add a toggle to the explorer that overlays the inverse function's graph and its derivative, showing the inverse's infinite slope at 0. — *Interaction:* Toggle 'show inverse' and 'show derivative of inverse'.

### Fig. C.5 (d) · function-plot · GA §C.3 p.568 (pdf 585)

`book-sources/gifted-amateur/pages/page-585/img-359.jpeg`

**Caption (paraphrased):** Graph of a function that is neither one-to-one nor onto.

**What it shows:** Axes with an upward-opening parabola with its vertex at the origin.

**What it teaches:** Even function hits each positive value twice and never reaches negative values.

**Concepts:** injective map, surjective map

**App redesign (not-worth-redesigning, low priority):** Covered by the horizontal-line-test explorer. — *Interaction:* As above.

### Fig. C.6 · cartoon-or-analogy · GA §C.4 p.569 (pdf 586)

`book-sources/gifted-amateur/pages/page-586/img-360.jpeg`

**Caption (paraphrased):** Continuous deformation of a coffee mug with a handle into a doughnut; a handleless mug could not be deformed this way without making a hole.

**What it shows:** Three hand-drawn objects separated by 'approximately equal' (homeomorphic) symbols: a mug with a handle, an intermediate squashed blob with a loop where the handle was, and a ring-shaped doughnut.

**What it teaches:** Homeomorphism preserves the number of holes; stretching and squashing are allowed, tearing and gluing are not.

**Concepts:** homeomorphism

**App redesign (interactive-3d, high priority):** 3D morph: a clay mug continuously morphs into a torus under a slider; a second object (handleless mug or sphere) tries to morph and a 'tear needed' warning appears at the step where a hole would have to be punched. — *Interaction:* Scrub a morph slider; switch the start object; the hole count (genus) is displayed and stays fixed during legal deformations.

### Fig. C.7 · curve-or-surface · GA §C.5 p.569 (pdf 586)

`book-sources/gifted-amateur/pages/page-586/img-361.jpeg`

**Caption (paraphrased):** Circle, sphere and torus each look locally like R or R^2 under magnification; the torus is a product of two circles.

**What it shows:** (a) A circle labelled S^1 with a magnifying glass held against one point; an arrow leads to the lens showing a straight line labelled R. (b) A globe-like sphere S^2 with latitude and longitude lines and a magnifier showing a flat patch labelled R^2. (c) A shaded torus labelled T^2 = S^1 x S^1 with two bold circles (one around the tube, one around the hole) and a magnifier showing R^2.

**What it teaches:** The defining property of a manifold is local flatness under sufficient magnification, not global flatness; product construction of the torus.

**Concepts:** manifold

**App redesign (interactive-3d, high priority):** Infinite-zoom manifold microscope: learner picks a space (circle, sphere, torus, double cone, plane with a spike) and zooms continuously on any point; for manifolds the view flattens, for non-manifolds the apex or junction never flattens. — *Interaction:* Click a point, scroll to zoom; a flatness meter reports curvature of the visible patch; switch between manifold and non-manifold objects.

### Fig. C.8 · geometric-construction · GA §C.5 p.570 (pdf 587)

`book-sources/gifted-amateur/pages/page-587/img-362.jpeg`

**Caption (paraphrased):** A chart map sends an open patch of the manifold to a region of R^m.

**What it shows:** Left: an irregular blob M containing a smaller curvilinear patch U drawn with a distorted grid. A curved arrow labelled phi leads to a boxed panel labelled R^m containing a region phi(U) with a straightened rectangular grid.

**What it teaches:** Coordinates are a map from part of the manifold to number space; the grid on U is the pullback of the Cartesian grid.

**Concepts:** coordinate function, coordinate neighbourhood

**App redesign (interactive-3d, high priority):** Chart mapper: on a sphere, the learner drags a patch U; the right panel shows its image under a chosen chart (angles, stereographic), with gridlines linked by hover. — *Interaction:* Drag or resize U on the 3D sphere; hover a grid point to highlight its coordinate image; switch chart types and watch the image deform; patches that include a pole show the chart failing.

### Fig. C.9 (a) · geometric-construction · GA §C.5 p.570 (pdf 587)

`book-sources/gifted-amateur/pages/page-587/img-363.jpeg`

**Caption (paraphrased):** The angle chart phi_1 sends points of patch U_1 on the unit circle to theta in R.

**What it shows:** A bold circle inside a thin concentric outline labelled U_1, with the point P marked on its right-hand side where the outline has a small break. A curved arrow labelled phi_1 runs from near P to a vertical bar whose bottom end is theta = 0 and top end is theta = 2 pi.

**What it teaches:** Angular coordinate as a chart on S^1.

**Concepts:** chart, coordinate function

**App redesign (interactive-2d, high priority):** Two-chart circle atlas: a point moves around the circle while two number lines show its theta coordinate in chart 1 (0 to 2 pi) and chart 2 (-pi to pi); each chart's excluded point is drawn as a hollow circle, and the overlap transition map is plotted. — *Interaction:* Drag the point around the circle; watch chart 1 jump at P and chart 2 jump at Q; a third panel plots theta_2 versus theta_1 on the overlap (two line segments with a shift of 2 pi).

### Fig. C.9 (b) · geometric-construction · GA §C.5 p.570 (pdf 587)

`book-sources/gifted-amateur/pages/page-587/img-364.jpeg`

**Caption (paraphrased):** The problem point: the same position on the circle would be assigned both 0 and 2 pi, so it must be removed from U_1.

**What it shows:** The bold circle with the thin surrounding outline U_1 now drawn as a loop that stops short at one point; two curved arrows from that same point go to both the theta = 0 end and the theta = 2 pi end of the vertical bar.

**What it teaches:** A single chart on the circle cannot be one-to-one and onto an open interval; one point must be dropped.

**Concepts:** chart, injective map

**App redesign (interactive-2d, high priority):** Part of the two-chart atlas demo: when the learner forces a single chart to include P, both endpoints of the interval light up and a 'not a function' warning appears. — *Interaction:* Toggle 'include P in U_1'.

### Fig. C.9 (c) · geometric-construction · GA §C.5 p.570 (pdf 587)

`book-sources/gifted-amateur/pages/page-587/img-365.jpeg`

**Caption (paraphrased):** A second chart phi_2 with values in (-pi, pi) omits a different point Q.

**What it shows:** The bold circle with surrounding outline U_2; a point Q marked on the left side; a curved arrow phi_2 from a point near the top to a vertical bar labelled theta = -pi at the bottom and theta = pi at the top.

**What it teaches:** Two charts with different missing points together cover the circle.

**Concepts:** atlas, chart

**App redesign (not-worth-redesigning, low priority):** Part of the two-chart atlas demo. — *Interaction:* As in Fig. C.9(a).

### Fig. C.10 · geometric-construction · GA §C.5 p.571 (pdf 588)

`book-sources/gifted-amateur/pages/page-588/img-366.jpeg`

**Caption (paraphrased):** A coordinate transformation built from two overlapping charts.

**What it shows:** Left: blob M containing two overlapping ovals U (upper) and V (lower); a point P sits in the hatched overlap. Right: a box R^m containing two regions phi(U) (upper) and psi(V) (lower), each with a hatched overlap image containing the labelled points x^mu and y^mu. Arrows: phi from U to phi(U); psi from V to psi(V); phi^{-1}(x) from x^mu back to P; psi(P) from P to y^mu.

**What it teaches:** The transition map is phi^{-1} followed by psi, defined only on the overlap.

**Concepts:** transition map, chart, composition of maps

**App redesign (interactive-3d, high priority):** Transition-map tracer: on a sphere covered by two stereographic charts, the learner picks a point in chart 1's plane; an animated path goes up to the sphere and down into chart 2's plane, while the explicit formula y = x/|x|^2 is evaluated live. — *Interaction:* Drag the point in chart 1; the traced path and the chart-2 coordinates update; moving outside the overlap greys out the transition.

### Fig. C.11 · geometric-construction · GA §C.6 p.572 (pdf 589)

`book-sources/gifted-amateur/pages/page-589/img-367.jpeg`

**Caption (paraphrased):** A function on the manifold is handled through its composite with the inverse chart.

**What it shows:** Blob M with patch U and point P inside. An arrow f runs from P to a point on a vertical real line R at the top right. An arrow phi runs down from P to a point x in a coordinate plane R^m at the bottom left. A curved arrow labelled f o phi^{-1}(x) runs from x to the same point on R, closing a commuting triangle.

**What it teaches:** The familiar f(x^1,...,x^m) is a coordinate representation; the manifold function is chart independent.

**Concepts:** coordinate representation of a function

**App redesign (interactive-3d, medium priority):** Temperature on a globe: a scalar field is painted on a sphere; two chart panels (latitude-longitude and stereographic) show different-looking formulas and contour plots of the same field, with a probe point linked across all three views. — *Interaction:* Move the probe on any view; the value readout is identical in all three while the coordinate formulas differ.

### Fig. C.12 · geometric-construction · GA §C.6 p.572 (pdf 589)

`book-sources/gifted-amateur/pages/page-589/img-368.jpeg`

**Caption (paraphrased):** A map between manifolds and its coordinate representation.

**What it shows:** Two blobs M (left) and N (right), each with a patch (U containing P; V containing f(P)). An arrow f joins P to f(P). Arrows phi and psi go down to two gridded patches in coordinate planes R^m (left, point x) and R^m (right, point y). A curved arrow labelled psi o f o phi^{-1} joins x to y.

**What it teaches:** Maps between manifolds are studied through the chart sandwich psi o f o phi^{-1}; differentiability is defined this way.

**Concepts:** coordinate representation of a function, differentiable map between manifolds

**App redesign (interactive-2d, medium priority):** Commuting-square widget: learner chooses f (a rotation of the sphere, a squash) and charts on both sides; the lower arrow's formula and Jacobian are computed, and changing either chart changes the formula but not the upper map. — *Interaction:* Select map and charts; drag a point; display psi o f o phi^{-1} numerically and its Jacobian determinant.

### Fig. C.13 · geometric-construction · GA §C.9 p.576 (pdf 593)

`book-sources/gifted-amateur/pages/page-593/img-369.jpeg`

**Caption (paraphrased):** A curve on the manifold and its coordinate image.

**What it shows:** Left: a vertical interval from a (bottom) to b (top) with a point lambda. An arrow c goes from lambda to a point c(lambda) on a short curve drawn inside patch U of blob M. An arrow phi descends to a curve in a coordinate plane R^m; a long curved arrow phi o c goes directly from lambda to the corresponding point in R^m.

**What it teaches:** Curves are maps from an interval, and their coordinate description is a composite.

**Concepts:** parametrized curve on a manifold

**App redesign (interactive-3d, medium priority):** Curve scrubber: a slider for lambda moves a bead along a curve on a torus; the chart panel shows the same bead moving along x^mu(lambda), and the reparametrization control shows the same image traced at different speeds. — *Interaction:* Drag lambda slider; choose reparametrization lambda -> lambda^2 or 2 lambda; observe unchanged image but changed velocity.

### Fig. C.14 · geometric-construction · GA §C.10 p.576 (pdf 593)

`book-sources/gifted-amateur/pages/page-593/img-370.jpeg`

**Caption (paraphrased):** A tangent vector expressed through maps: curve, function, and chart.

**What it shows:** An interval from a to b with 0 marked on the left. Arrow c sends 0 to c(0) on a curve in patch U of blob M; a short arrow X is tangent at c(0), and another point c(t) lies along the curve. Arrow f goes from the curve to a vertical real line R on the right. Arrow phi goes down to a point in R^m; arrow phi o c goes from the interval to that point; arrow f o phi^{-1} goes from R^m up to R.

**What it teaches:** The derivative of f o c factors through coordinate space, which is where the chain rule and components come from.

**Concepts:** tangent vector as directional derivative, composition of maps

**App redesign (interactive-3d, high priority):** Directional-derivative lab: a scalar field on a curved surface and a curve through P; the learner changes the function or the curve and watches d(f o c)/dlambda computed both directly and as (dx^mu/dlambda)(partial f/partial x^mu) with matching bars. — *Interaction:* Drag the curve's direction at P and switch functions; two numeric readouts (direct and chain-rule) stay equal; curves with the same velocity at P give identical readouts.

### Fig. C.15 · geometric-construction · GA §C.10 p.577 (pdf 594)

`book-sources/gifted-amateur/pages/page-594/img-371.jpeg`

**Caption (paraphrased):** (a) Many vectors in the tangent space at a point; (b) the embedded tangent-plane picture used earlier in the book.

**What it shows:** (a) A pair of perpendicular axes, off to one side, beside a point P from which about eight short arrows radiate in different directions, with no surface drawn. (b) A hand-drawn gridded dome (like part of a globe) with a flat rectangular card touching it at P; the same starburst of arrows lies in the card.

**What it teaches:** Tangent vectors at P form a vector space; the familiar tangent plane is an embedding-dependent visualization of it.

**Concepts:** tangent space, embedding versus intrinsic description

**App redesign (interactive-3d, high priority):** Intrinsic versus embedded tangent space: split view where the right shows the tangent plane on an embedded sphere and the left shows only the abstract 2D vector space with basis partial_theta, partial_phi; changing the embedding (sphere to ellipsoid) moves the plane but leaves the abstract space and components unchanged. — *Interaction:* Deform the embedding with a slider; pick a curve through P; the vector's components in the abstract panel stay put while the 3D arrow tilts.

### Fig. C.16 · geometric-construction · GA §C.11 p.578 (pdf 595)

`book-sources/gifted-amateur/pages/page-595/img-372.jpeg`

**Caption (paraphrased):** (a) Tangent lines to a wavy one-dimensional manifold at several points; (b) the same tangents redrawn as vertical lines, the fibres of a bundle.

**What it shows:** (a) A bold sinusoidal curve with points p (a crest), q (a trough) and r (a later crest); straight tangent lines at each point extend far enough to cross one another. (b) The same wavy curve with vertical lines through p, q and r.

**What it teaches:** Drawing tangent spaces in place causes overlaps; rotating them to stand vertically separates them and suggests the bundle construction.

**Concepts:** tangent bundle, base space and fibre

**App redesign (animated-2d, high priority):** Animated 'comb the tangents': tangent lines on a curve rotate to vertical and the curve straightens into a base line, producing the fibres of TM; the learner can pick a tangent vector at each point and see it become a bead height. — *Interaction:* Play/scrub the rotation animation; click points to set tangent-vector lengths, which become beads on fibres.

### Fig. C.17 · schematic · GA §C.11 p.578 (pdf 595)

`book-sources/gifted-amateur/pages/page-595/img-373.jpeg`

**Caption (paraphrased):** A bundle B made of fibres V above a base M, with the projection pi collapsing each fibre to a point.

**What it shows:** A dense row of about 25 parallel vertical line segments labelled B; small arrows point to a few of them with the label V. A downward arrow labelled pi points to a horizontal line labelled M below.

**What it teaches:** Total space, fibre, base and projection.

**Concepts:** fibre bundle, canonical projection, base space and fibre

**App redesign (interactive-2d, medium priority):** Bundle anatomy explorer: hover any point of the total space to highlight its fibre and its projected base point; toggle the fibre type (R, circle, finite set). — *Interaction:* Hover and click; switch fibre type to see the total space change (strip, torus, disjoint copies).

### Fig. C.18 · schematic · GA §C.11 p.578 (pdf 595)

`book-sources/gifted-amateur/pages/page-595/img-374.jpeg`

**Caption (paraphrased):** A product bundle M x V and its projection.

**What it shows:** A tall rectangle ruled into a grid, labelled M x V, with a dot marking the point at horizontal position a and vertical position b. Below, a row of thick downward arrows points to a hatched horizontal bar labelled M.

**What it teaches:** Points of a trivial bundle are pairs (a, b); projection keeps a.

**Concepts:** trivial (product) bundle, canonical projection

**App redesign (not-worth-redesigning, low priority):** Fold into the bundle anatomy explorer with a 'product coordinates' overlay. — *Interaction:* Drag the point and read (a, b) and pi(a, b) = a.

### Fig. C.19 · curve-or-surface · GA §C.11 p.579 (pdf 596)

`book-sources/gifted-amateur/pages/page-596/img-375.jpeg`

**Caption (paraphrased):** The tangent bundle of the circle as a cylinder floating above the circle.

**What it shows:** A cylinder drawn with many vertical line segments (solid at the front, dashed at the back) labelled TS^1, above a separate flat ellipse labelled S^1.

**What it teaches:** TS^1 is globally the product of the circle with a line: a cylinder.

**Concepts:** tangent bundle, trivial (product) bundle

**App redesign (interactive-3d, high priority):** 3D cylinder bundle: a point circles the base while a vector (arrow tangent to the circle) at that point is shown both as an arrow on the circle and as a bead on the cylinder's fibre above it; drawing a vector field paints a closed curve on the cylinder. — *Interaction:* Orbit camera; drag beads on fibres to set the vector field; the tangent arrows on the base update.

### Fig. C.20 (a) · apparatus-or-experiment · GA §C.11 p.579 (pdf 596)

`book-sources/gifted-amateur/pages/page-596/img-376.jpeg`

**Caption (paraphrased):** The globally trivial bundle over the circle.

**What it shows:** Photograph of a physical model: a thin white ring with about 30 straight black rods passing through it, all standing vertically and parallel, forming a cylindrical fence.

**What it teaches:** Fibres stay aligned all the way round: a cylinder.

**Concepts:** trivial (product) bundle

**App redesign (interactive-3d, high priority):** Twist slider over the circle: rods start vertical (cylinder) and a slider sets the total rotation of the fibres around the loop; allowed end values are 0 or a half turn (mod a full turn) to close up, giving cylinder or Moebius. — *Interaction:* Drag the twist slider; snap to closed configurations; orbit the 3D view; toggle a surface skin to reveal cylinder or Moebius strip.

### Fig. C.20 (b) · apparatus-or-experiment · GA §C.11 p.579 (pdf 596)

`book-sources/gifted-amateur/pages/page-596/img-377.jpeg`

**Caption (paraphrased):** The twisted bundle, whose fibres form a Moebius strip.

**What it shows:** Photograph of the same ring with black rods, but the rods tilt progressively as one goes around the ring, fanning outward and turning over through half a revolution so that the rods trace out a Moebius band.

**What it teaches:** Locally each rod has neighbours nearly parallel to it (local product), but globally the fibres come back flipped.

**Concepts:** Moebius bundle, local versus global triviality

**App redesign (interactive-3d, high priority):** Same twist-slider model as panel (a). — *Interaction:* As above.

### Fig. C.21 · curve-or-surface · GA §C.11 p.580 (pdf 597)

`book-sources/gifted-amateur/pages/page-597/img-378.jpeg`

**Caption (paraphrased):** A cross section: the base lifted into the bundle as a curve meeting every fibre once, like the graph of a function.

**What it shows:** A cylinder labelled B drawn with dashed horizontal ellipses; a bold wavy closed curve winds once around its middle and a lighter dotted wavy curve runs near the top rim. Below, an ellipse labelled M carries several upward arrows labelled s pointing toward the cylinder.

**What it teaches:** Sections pick one fibre point over each base point; on a product bundle they are graphs of functions.

**Concepts:** cross section

**App redesign (interactive-3d, high priority):** Section painter with zero-section test: learner draws a section on the cylinder or the Moebius band by dragging control points; the zero section is drawn in red and crossings are counted; on the Moebius band the counter never reaches zero. — *Interaction:* Drag heights of control points around the loop; switch between cylinder and Moebius; a crossing counter and an 'avoids zero?' badge update.

## Worked examples

### Example C.1 · intro · GA §C.3 p.568 (pdf 585)

**Problem:** Classify four real functions drawn as graphs as one-to-one, onto, both, or neither.

**Method:** Inspect each graph: monotonicity for injectivity, whether all y values are reached for surjectivity.

**Key insight:** Graph shape alone decides the classification; a bijection needs both strict monotonicity (for continuous functions) and unbounded range.

**Result:** (a) exponential-like: 1-1 not onto; (b) wiggly cubic: onto not 1-1; (c) x^3-like: bijection; (d) parabola: neither.

**Concepts:** injective map, surjective map, bijection

### Example C.2 · intro · GA §C.4 p.569 (pdf 586)

**Problem:** Decide for several pairs of spaces whether they are homeomorphic.

**Method:** Apply the continuous-deformation picture and topological invariants (dimension, number of holes, compactness).

**Key insight:** Homeomorphism ignores shape details but respects holes, dimension and compactness.

**Result:** Homeomorphic: open disc and open square; graph of a differentiable function and its domain; parameter interval and a differentiably parametrized curve; mug and doughnut. Not homeomorphic: R^m and R^n with m different from n; the real line and the circle (circle compact, line not).

**Concepts:** homeomorphism, compactness

### Example C.3 · intro · GA §C.5 p.569 (pdf 586)

**Problem:** List spaces that are and are not manifolds.

**Method:** Check local resemblance to R^n at every point.

**Key insight:** A single bad point (junction, cone apex) is enough to disqualify a space.

**Result:** Manifolds: R^m, S^1, S^2, T^2. Not manifolds: a plane with a line sticking out; a double cone.

**Concepts:** manifold

### Example C.4 · intro · GA §C.5 p.570 (pdf 587)

**Problem:** Try to cover the unit circle with a single angle coordinate running from 0 to 2 pi.

**Method:** Map points to theta; notice the starting point receives both 0 and 2 pi; restore one-to-oneness by deleting that point from the chart domain.

**Key insight:** Global topology (the circle closes up) prevents a single homeomorphism onto an open interval.

**Result:** U_1 = circle minus P; phi_1 is a valid chart there.

**Concepts:** chart, coordinate function, injective map

### Example C.5 · intro · GA §C.5 p.570 (pdf 587)

**Problem:** Complete the covering of the unit circle.

**Method:** Define a second angle chart with values in (-pi, pi), which omits a different point Q, and check that the two domains together contain every point.

**Key insight:** Two charts with different excluded points suffice; overlaps are where transition maps live.

**Result:** U_1 union U_2 = S^1.

**Concepts:** atlas, chart

### Example C.6 · intro · GA §C.5 p.571 (pdf 588)

**Problem:** How many charts are needed for Euclidean space and for the two one-dimensional manifolds?

**Method:** Use the identity chart for R^m and R; recall the circle argument.

**Key insight:** The minimum number of charts reflects global topology, not local structure.

**Result:** R^m and the line: one chart; the circle: at least two.

**Concepts:** atlas

### Example C.7 · standard · GA §C.6 p.572 (pdf 589)

**Problem:** Give the coordinate representation of a map f between two m-dimensional manifolds.

**Method:** Choose charts (U, phi) around P and (V, psi) around f(P) and compose psi o f o phi^{-1}.

**Key insight:** Any map between manifolds becomes an ordinary tuple-valued function once charts are fixed on both sides.

**Result:** (y^1,...,y^m) = psi o f o phi^{-1}(x^1,...,x^m).

**Concepts:** coordinate representation of a function

### Example · standard · GA §C.7 p.572 (pdf 589)

**Problem:** Show why differentiability of f judged in one chart need not persist in another chart.

**Method:** Write f o psi^{-1} as (f o phi^{-1}) composed with the transition map phi o psi^{-1} and apply the chain rule.

**Key insight:** Chart-independence of smoothness is exactly the requirement that transition maps be smooth.

**Result:** Charts must be C^infinity related on overlaps.

**Concepts:** compatible (C^infinity-related) charts, transition map

### Example C.8 · intro · GA §C.7 p.573 (pdf 590)

**Problem:** Exhibit the simplest differentiable manifold.

**Method:** Take R with the identity chart and the maximal atlas containing it; check the identity is infinitely differentiable (margin note lists its derivatives).

**Key insight:** Smooth structure is a choice of maximal atlas even for the real line.

**Result:** (R, maximal atlas containing x -> x) is a differentiable manifold.

**Concepts:** differentiable manifold, maximal atlas

### Example C.9 · standard · GA §C.7 p.573 (pdf 590)

**Problem:** Decide which of f(x)=x, g(x)=x^2, h(x)=x^3 on R and a linear map phi(x,y) = (x + y/2, y - x/2) on R^2 are diffeomorphisms.

**Method:** Check injectivity (g fails since g(2)=g(-2)); for h check smoothness of the inverse x^{1/3}, whose derivative blows up at 0; for phi compute the Jacobian determinant.

**Key insight:** A smooth homeomorphism need not be a diffeomorphism: the inverse must also be smooth.

**Result:** f and phi (Jacobian 5/4) are diffeomorphisms; g and h are not.

**Concepts:** diffeomorphism, Jacobian determinant

### Example C.10 · challenging · GA §C.7 p.574 (pdf 591)

**Problem:** Show that diffeomorphism invariance of the matter action implies nabla_mu T^{mu nu} = 0.

**Method:** Vary the matter action with respect to the metric; take the metric variation to be the Lie derivative 2 u_(mu;nu) along an arbitrary generator u; drop the symmetrization because the functional derivative is symmetric; integrate by parts to move the covariant derivative onto the functional derivative; use arbitrariness of u and the definition of T from Chapter 40.

**Key insight:** Energy-momentum conservation in GR is a consequence of the theory's gauge symmetry (diffeomorphisms), not an extra assumption.

**Result:** T^{mu nu}_{;mu} = 0.

**Concepts:** conservation of energy-momentum from diffeomorphism invariance, Lie derivative as generator of a diffeomorphism, energy-momentum tensor from the action

### Example C.11 · intro · GA §C.8 p.575 (pdf 592)

**Problem:** Show that [0,1] is compact but (0,1] is not, using sequences.

**Method:** Consider 1/n for positive integers n: every term lies in both sets, and its limit 0 lies in [0,1] but not in (0,1].

**Key insight:** Removing a single boundary point destroys compactness.

**Result:** [0,1] compact; (0,1] not compact.

**Concepts:** compactness

### Example C.12 · intro · GA §C.8 p.575 (pdf 592)

**Problem:** Classify some two-dimensional spaces as compact or not.

**Method:** Apply the three failure modes: running off to infinity, missing boundary, missing interior region.

**Key insight:** Closed and finite objects without missing pieces are compact.

**Result:** Compact: closed unit disc, S^2, T^2. Not compact: the plane, the open disc, a closed disc with a hole removed (read: with a point or closed region deleted so that its edge is missing).

**Concepts:** compactness

### Example · standard · GA §C.10 p.576 (pdf 593)

**Problem:** Derive the coordinate form of a tangent vector from the derivative of a function along a curve.

**Method:** Write f o c = (f o phi^{-1}) o (phi o c), apply the multivariable chain rule, and read off components dx^mu/dlambda and basis operators partial/partial x^mu.

**Key insight:** A vector is fully specified by its action on functions, and coordinates only appear through the chart factorization.

**Result:** v[f] = (dx^mu/dlambda) partial f/partial x^mu at lambda = 0.

**Concepts:** tangent vector as directional derivative, coordinate basis vectors

### Example C.13 · intro · GA §C.10 p.577 (pdf 594)

**Problem:** Act with a tangent vector on a coordinate function.

**Method:** Choose f = x^nu, the nu-th coordinate; the partial derivative of x^nu with respect to x^mu is a Kronecker delta, leaving only one term.

**Key insight:** Components of a vector are what the vector returns when it acts on the coordinate functions.

**Result:** v[x^nu] = dx^nu/dlambda at lambda = 0.

**Concepts:** coordinate basis vectors

### Example C.14 · intro · GA §C.11 p.578 (pdf 595)

**Problem:** Describe the tangent bundle of the circle and put coordinates on it.

**Method:** Identify TS^1 with S^1 x R (a cylinder); label a point by angle theta on the base and amplitude y along the fibre, writing v = y partial_theta.

**Key insight:** Because the circle has a nowhere-vanishing vector field partial_theta, its tangent bundle is a product.

**Result:** TS^1 = S^1 x R, a trivial two-dimensional bundle with coordinates (theta, y).

**Concepts:** tangent bundle, trivial (product) bundle

### Example C.15 · standard · GA §C.11 p.579 (pdf 596)

**Problem:** Construct a bundle over the circle that is locally but not globally a product.

**Method:** Build a real line bundle over S^1 whose fibres flip orientation once around the loop (Moebius strip); show local triviality by deleting a base point, then glue two trivial pieces with a twist.

**Key insight:** Local triviality cannot detect global twisting; that information lives in how local pieces are glued.

**Result:** The Moebius bundle is locally like the cylinder but globally different.

**Concepts:** Moebius bundle, local versus global triviality

### Example C.16 · standard · GA §C.11 p.579 (pdf 596)

**Problem:** Use sections to distinguish the cylinder from the Moebius bundle.

**Method:** Draw the zero section; note a section of the cylinder can stay on one side of it, whereas on the Moebius band a section returns with its sign reversed and must cross zero.

**Key insight:** Global properties of bundles are revealed by which sections exist (here: nowhere-zero sections).

**Result:** Every section of the Moebius bundle meets the zero section; the cylinder admits sections that do not.

**Concepts:** cross section, zero section, Moebius bundle


## Analogies and intuitions

### Objects made of mouldable clay that may be stretched and squashed but not torn, pierced, glued, or have holes sealed → homeomorphism · strong · GA §C.4 p.568 (pdf 585)

Gives a concrete mental test for when two spaces are topologically the same; the coffee mug with handle becomes a doughnut, a handleless mug cannot.

**Where it breaks down:** Only covers deformations within an ambient space; many homeomorphisms (e.g. a knotted versus unknotted circle, or maps needing temporary cutting and regluing) are not realizable as physical deformations. The book flags this in a margin note.

**App idea:** Clay-morph 3D demo with a hole counter that stays fixed under legal moves.

### Magnifying glass held against a circle, sphere or torus shows a straight line or flat plane → manifold · strong · GA §C.5 p.569 (pdf 586)

Captures 'locally looks like R^n' pictorially; non-manifolds are points that never look flat at any zoom.

**Where it breaks down:** 'Looks flat under zoom' is really a smoothness intuition, while the definition only asks for a local homeomorphism. The apex of a single cone never looks smooth, yet it is topologically fine (a small neighbourhood is still a disc). The double cone fails for a genuinely topological reason: removing the apex from a small neighbourhood leaves two pieces, which never happens for a punctured disc. The book's 'never looks smooth' wording blurs these two failures.

**App idea:** Infinite-zoom microscope over manifold and non-manifold shapes.

### Tangent vectors as beads on the wires of an abacus standing above each point → fibre bundle · useful · GA §C.11 p.578 (pdf 595)

After rotating tangent lines to vertical and lifting them off, a particular vector is a bead position on the wire above its base point.

**Where it breaks down:** The vertical wires suggest the bundle is always a product and that fibres at different points can be compared directly, which requires extra structure (a connection).

**App idea:** Draggable beads on fibres over a circle, reflected as tangent arrows on the base.

### A cross section as a generalized graph of a function → cross section · strong · GA §C.11 p.579 (pdf 596)

For a product bundle, choosing one fibre point above each base point is exactly plotting a V-valued function over M.

**Where it breaks down:** For twisted bundles there is no global 'vertical axis', so sections are not graphs of ordinary functions.

**App idea:** Section painter on cylinder versus Moebius band.

### Rods pushed through a ring, first all parallel, then twisting round → local versus global triviality · strong · GA §C.11 p.579 (pdf 596)

Photographs of a physical model make the cylinder/Moebius distinction tangible.

**Where it breaks down:** Rods are finite and discrete, whereas fibres are complete lines at every point.

**App idea:** Twist slider applied to rods around a ring in 3D.

### A homeomorphism as continuous deformation versus a diffeomorphism as smooth deformation → diffeomorphism · useful · GA §C.7 p.574 (pdf 591)

Contrasts the two morphisms in one sentence pair, adding that smoothness is guaranteed independent of chart choice.

**Where it breaks down:** Hides that the key failure (e.g. x^3) is a non-smooth inverse, not a visibly rough deformation.

**App idea:** Side-by-side plot of x^3 and its inverse with derivative overlays.

### Diffeomorphisms of spacetime to itself as active coordinate transformations that shift points around → diffeomorphism invariance · useful · GA §C.7 p.574 (pdf 591)

Links the abstract morphism to familiar coordinate changes and to gauge symmetry.

**Where it breaks down:** Passive relabelling and active pushing are mathematically related but conceptually distinct; conflating them leads to hole-argument puzzles.

**App idea:** Toggle between relabelling a grid (passive) and dragging matter and metric together (active) on a 2D spacetime patch.

### A pyramid of mathematical structure: set at the base, topology, manifold, metric at the apex → pseudo-Riemannian manifold · useful · GA p.565 (pdf 582)

Frames the appendix as climbing from the least to the most structured notion.

**Where it breaks down:** Omits intermediate layers (differentiable structure versus topological manifold, connection) and suggests a strict linear order.

**App idea:** Clickable ladder that tests objects against each layer.


## Misconceptions addressed

### Curved spacetime must be curved inside some larger flat space. · GA p.565 (pdf 582)

**Correction:** Manifolds and their geometry are defined intrinsically; no embedding is needed or assumed for the physical universe.

**Why tempting:** Every picture of a curved surface shows it sitting in 3D space, and earlier chapters used tangent planes to surfaces.

### A manifold comes with distances and angles. · GA §C.5 p.569 (pdf 586)

**Correction:** A bare manifold carries only topological and smooth structure; lengths and angles need an extra metric.

**Why tempting:** The model space R^n is usually used with its Euclidean distance.

### One coordinate system should be able to cover any manifold. · GA §C.5 p.570 (pdf 587)

**Correction:** Global topology can prevent it: the circle needs at least two charts, and the sphere also needs two.

**Why tempting:** In flat space a single Cartesian chart works everywhere, and polar coordinates are used as if they covered the whole circle.

### A vector on a manifold is an arrow joining two points. · GA §C.10 p.576 (pdf 593)

**Correction:** There is no origin or notion of straightness on a bare manifold; vectors are directional derivatives at a point and live in the tangent space there.

**Why tempting:** Flat-space vectors are displacements, and pictures of tangent vectors show arrows on surfaces.

### Tangent vectors live in the manifold itself, and vectors at different points belong to one common space. · GA §C.10 p.576 (pdf 593)

**Correction:** Each point has its own tangent space; collecting them gives a separate manifold, the tangent bundle.

**Why tempting:** In R^n all tangent spaces are canonically identified, hiding the distinction.

### A smooth one-to-one onto map is automatically a diffeomorphism. · GA §C.7 p.573 (pdf 590)

**Correction:** The inverse must also be smooth: x^3 is a smooth bijection of R, but its inverse cube root has an infinite derivative at 0.

**Why tempting:** For homeomorphisms one checks continuity both ways, but people forget the analogous requirement for derivatives.

### If a function has nice partial derivatives in one coordinate system it is differentiable on the manifold. · GA §C.7 p.572 (pdf 589)

**Correction:** Differentiability is chart independent only when transition maps are smooth, which is why a differentiable manifold is defined with a C^infinity atlas.

**Why tempting:** In calculus we always use one fixed coordinate system.

### A space that is locally a product is globally a product. · GA §C.11 p.579 (pdf 596)

**Correction:** The Moebius bundle is a product over every small arc of the circle yet is globally twisted and differs from the cylinder.

**Why tempting:** Local charts of both look identical, and local calculations cannot tell them apart.

### The real line and a circle are 'the same' because a circle is just a line bent round. · GA §C.4 p.569 (pdf 586)

**Correction:** They are not homeomorphic; the circle is compact and the line is not, and removing a point disconnects the line but not the circle.

**Why tempting:** Both are one-dimensional and locally identical.

### Conservation of energy-momentum (nabla . T = 0) is an independent postulate added to GR. · GA §C.7 p.574 (pdf 591)

**Correction:** It follows from diffeomorphism invariance of the matter action (given the matter field equations).

**Why tempting:** Chapter 12 presents the law as a requirement, and in special relativity it is often introduced as an assumption.

### A non-zero Jacobian determinant everywhere guarantees that a map is a global diffeomorphism. · GA §C.7 p.573 (pdf 590)

**Correction:** A non-zero Jacobian gives only local invertibility; global injectivity must be checked separately (e.g. (x,y) -> (e^x cos y, e^x sin y) has non-zero Jacobian but is not one-to-one). The book's example is linear, so it works there.

**Why tempting:** Example C.9 infers invertibility directly from the Jacobian.

*Inferred: the book guards against this implicitly.*

### 'Into' means injective. · GA §C.3 p.567 (pdf 584)

**Correction:** In this book, 'into' only means the map is defined on all of the domain; injective is 'one-to-one'. Usage varies across texts.

**Why tempting:** Some mathematics texts use 'into' for injections.

*Inferred: the book guards against this implicitly.*


## Thought experiments

### Deforming a coffee mug into a doughnut · GA §C.4 p.569 (pdf 586)

**Setup:** Imagine a mug of soft clay being continuously reshaped; the handle's hole is kept while the cup's body is squashed into the ring.

**Lesson:** Homeomorphism preserves holes; a handleless mug cannot become a doughnut without piercing.

**App idea:** 3D morph with genus counter and 'tear required' warning.

### Zooming in on a double cone or a spike in a plane · GA §C.5 p.569 (pdf 586)

**Setup:** Magnify ever more around the apex of a double cone or the junction of a line and a plane.

**Lesson:** Some points never look like R^n however far you zoom, so the object is not a manifold. For the double cone and the spike-in-a-plane this is a topological failure as well: a small neighbourhood of the bad point, with the point removed, falls apart differently from a punctured disc.

**App idea:** Manifold microscope applied to non-manifold shapes.

### Wrapping an angle coordinate around a circle · GA §C.5 p.570 (pdf 587)

**Setup:** Try to label every point of a circle with an angle between 0 and 2 pi using one continuous one-to-one map.

**Lesson:** The starting point is labelled twice; one chart cannot do it, so atlases are needed.

**App idea:** Two-chart atlas demo with jumping coordinates.

### Lifting the tangent lines off a curve · GA §C.11 p.578 (pdf 595)

**Setup:** Draw tangent lines on a wavy curve, rotate them all to vertical so they no longer cross, and raise them to float above the curve.

**Lesson:** The collection of all tangent spaces is itself a manifold of double dimension: the tangent bundle.

**App idea:** Animated comb-the-tangents sequence.

### Cutting and regluing a bundle over the circle · GA §C.11 p.579 (pdf 596)

**Setup:** Remove one base point so the bundle over the remaining arc is a flat strip; glue two such strips back together either straight or with a flip.

**Lesson:** Local pieces are identical; the global structure is decided by the gluing, producing a cylinder or a Moebius band.

**App idea:** Drag the ends of a strip together and choose a gluing flip.

### Pushing everything along with a diffeomorphism · GA §C.7 p.574 (pdf 591)

**Setup:** Move every point of spacetime to a new point with a smooth invertible map, carrying all fields along.

**Lesson:** If physics cannot tell the two configurations apart, diffeomorphisms are gauge symmetries, and invariance of the action yields nabla . T = 0.

**App idea:** 2D spacetime patch where a matter blob and the metric grid are dragged together by a flow, with all invariant measurements unchanged.


## Applications and observations

- **Singularities of black holes and cosmology** (astrophysical-system, GA p.565 (pdf 582)): Margin note and opening paragraph: studies of black-hole and Big-Bang singularities rely on manifold ideas, with a singularity characterized as a failure of the smooth manifold description.
- **Jacobian of a linear map of the plane** (numerical-estimate, GA §C.7 p.573 (pdf 590)): Example C.9 computes the Jacobian of (x + y/2, y - x/2) to confirm invertibility. Key numbers: det J = 1 + 1/4 = 5/4

## Historical notes

- **Eduard Heine, Emile Borel:** The theorem linking compactness of subsets of the reals to being closed and bounded carries their names (Heine 1821-1881, Borel 1871-1956). — Connects the abstract notion of compactness to the familiar closed interval. (GA §C.8 p.575 (pdf 592))
- **August Ferdinand Moebius, Johann Benedict Listing:** The one-sided band now called the Moebius strip was found by Moebius (1790-1868) and independently by Listing. — Supplies the standard example of a bundle that is locally but not globally a product. (GA §C.11 p.579 (pdf 596))
- **Euripides:** Epigraph wishing life to be smooth and free of strife. — Playful pun on the smoothness that defines manifolds. (GA p.565 (pdf 582))

## Notation and conventions

- **Manifolds and points:** Calligraphic letters M, N, L for manifolds; calligraphic P, Q for points; calligraphic B for a bundle and V for a fibre; the tangent space at P is written T_P M (plain T) while the tangent bundle uses a calligraphic T (TM, TS^1). (GA §C.2 p.567 (pdf 584))
- **Composition:** g o f means apply f first, then g; all coordinate objects are written as composites with chart maps (phi, psi) or their inverses. (GA §C.2 p.567 (pdf 584))
- **Chart map and coordinates:** phi (or psi) denotes a coordinate function; x^mu = phi(P) and the same symbol x is used for both the coordinate functions and their values; charts are written (U, phi), though §C.7 sometimes writes (phi, U). — The book warns of the double use of x. (GA §C.5 p.570 (pdf 587))
- **Intervals:** (a,b) open, [a,b] closed; (0,1] half-open. (GA §C.1 p.566 (pdf 583))
- **Maps vocabulary:** one-to-one (1-1) = injective; onto = surjective; bijection = both; 'into' = defined on all of the domain. — 'Into' differs from some texts. (GA §C.3 p.567 (pdf 584))
- **Tangent vector action:** Square brackets v[f] for a vector acting on a function; round brackets v(f) in the derivation axioms; components written v^mu with basis e_mu = partial/partial x^mu, order of factors swapped to match v = v^mu e_mu. (GA §C.10 p.577 (pdf 594))
- **Smoothness classes:** C^k: partial derivatives up to order k exist and are continuous; C^infinity = smooth. (GA §C.7 p.573 (pdf 590))
- **Symmetrization and covariant derivatives:** u_{(mu;nu)} is the symmetrized covariant derivative including a factor 1/2; semicolons denote covariant derivatives. — Metric determinant written g, so sqrt(-g) appears; the book's signature (Appendix B) is (-+++). (GA §C.7 p.574 (pdf 591))
- **Identity map:** I denotes the identity map on the base manifold in pi o s = I; eta(x) = x is used for the identity chart on R in Example C.8 (not the Minkowski metric). — eta is reused with a different meaning from the Minkowski metric eta(,) in the opening. (GA §C.11 p.579 (pdf 596))
- **Standard spaces:** R^n Euclidean n-space, S^1 circle (boundary of a disc), S^2 sphere (boundary of a ball), T^2 = S^1 x S^1 torus. (GA §C.5 p.569 (pdf 586))

## Margin notes

- *clarification* — The appendix material underlies the book's differential geometry, is why modern GR looks as it does, and is essential for singularity studies in black holes and cosmology. (GA p.565 (pdf 582))
- *clarification* — Executive summary for readers who stop early: smooth spacetime means manifold; diffeomorphisms replace coordinate transformations; compactness replaces the idea of a boundary; tangent vectors live in tangent spaces; manifold plus tangent spaces make a fibre bundle. (GA p.566 (pdf 583))
- *clarification* — Map and function are used as synonyms. (GA §C.2 p.567 (pdf 584))
- *clarification* — Writing f: R^n -> R is just the map-language version of the usual y = f(x^1,...,x^n). (GA §C.2 p.567 (pdf 584))
- *clarification* — Glossary of injective, surjective and bijective with the French 'sur' and the 'bi' mnemonic. (GA §C.3 p.568 (pdf 585))
- *caution* — Continuous deformation is only one instance of a homeomorphism; the map definition is more general. (GA §C.4 p.568 (pdf 585))
- *clarification* — Physicists usually call a chart a coordinate system. (GA §C.5 p.571 (pdf 588))
- *technical-detail* — Definition of differentiability classes C^k and C^infinity; polynomials are smooth, the cube root fails at the origin. (GA §C.7 p.573 (pdf 590))
- *technical-detail* — The identity map is smooth: derivative 1, higher derivatives 0. (GA §C.7 p.573 (pdf 590))
- *clarification* — Dimension convention for differentiable maps: M has dimension m and N has dimension n, so the coordinate representation runs from R^m to R^n. (GA §C.7 p.573 (pdf 590))
- *caution* — A diffeomorphism needs manifolds on both sides, while homeomorphisms can relate non-manifold spaces. (GA §C.7 p.573 (pdf 590))
- *technical-detail* — Computation of the Jacobian matrix and determinant (5/4) for the linear map in Example C.9. (GA §C.7 p.573 (pdf 590))
- *reference* — Diffeomorphisms are also useful outside GR, giving a geometric picture of Hamiltonian mechanics; Geroch's Geometrical Quantum Mechanics is suggested. (The marker sits on the sentence calling diffeomorphisms the gauge symmetries of GR.) (GA §C.7 p.574 (pdf 591))
- *forward-pointer* — Killing vector fields, which encode conserved quantities, are most generally defined via diffeomorphisms. (GA §C.7 p.574 (pdf 591))
- *backward-pointer* — Recall of the covariant formula for the Lie derivative of the metric, reducing to twice the symmetrized covariant derivative of u (printed with mismatched indices). (GA §C.7 p.574 (pdf 591))
- *technical-detail* — Alternative open-cover definition of compactness (every open cover has a finite subcover). (GA §C.8 p.575 (pdf 592))
- *reference* — Heine-Borel stated without proof; Spivak's Calculus on Manifolds recommended; brief biographical dates for Heine and Borel. (GA §C.8 p.575 (pdf 592))
- *caution* — Boundedness requires a distance, so it only makes sense for spaces with a metric. (GA §C.8 p.575 (pdf 592))
- *forward-pointer* — The picture of tangent spaces floating above the manifold is the fibre bundle idea of the next section. (GA §C.10 p.576 (pdf 593))
- *biography* — Biographical note on Moebius and the independent discovery of the one-sided strip by Listing. (GA §C.11 p.579 (pdf 596))

## Exercises

About 0 exercises (pdf pages n/a).

**Solutions:** The appendix has no exercises; its 16 numbered examples serve as the practice material.

**Skills practiced**
_None recorded._


## Cross-references

- *backward* → **GA ch31 §31.1**: Fig. 31.1 supplies the non-manifold examples (line through a plane, double cone) cited in Example C.3; Chapter 31 gives the lighter version of the manifold definition.
- *backward* → **GA ch33**: Lie derivative along a vector field, here re-grounded as the generator of a diffeomorphism flow; Chapter 33 margin note points to this appendix.
- *backward* → **GA ch40**: Action principle and the variational definition of T used in Example C.10.
- *backward* → **GA ch12**: A Chapter 12 margin note (pdf p.156) says nabla . T = 0 can be proven from invariance under diffeomorphisms and refers to this appendix; Example C.10 delivers that argument.
- *backward* → **GA ch30**: Fig. 30.6 measures curvature using the tangent plane of a surface embedded in three dimensions; Fig. C.15(b) recalls this embedded picture to contrast it with the intrinsic tangent space.
- *backward* → **GA ch02**: Vectors written as v = v^mu e_mu, the convention the tangent-vector definition is made to match.
- *backward* → **GA ch26**: Black-hole singularities, cited as a place where manifold ideas are essential.
- *backward* → **GA ch50**: Chapter 50 (pdf p.564) invokes compactness of the set of causal curves and sends the reader to §C.8; the Big-Bang singularity is also an instance of the manifold description failing.
- *backward* → **GA ch44**: Gauge fields; the opening says bundles lie behind the physics of gauges.
- *backward* → **GA ch22**: Killing vectors and conserved quantities in Schwarzschild motion, mentioned in a margin note as diffeomorphism-based.
- *forward* → **GA appD**: Embedding appendix treats the extrinsic picture this appendix sets aside.
- *backward* → **GA appB**: Conventions (signature, determinant g) assumed in Example C.10.
- *external* → **Spivak, Calculus on Manifolds**: Proofs of Heine-Borel and other topological results about compactness.
- *external* → **Geroch, Geometrical Quantum Mechanics**: Introduction to the geometric (diffeomorphism-based) formulation of Hamiltonian mechanics.
- *backward* → **GA ch15**: Chapter 15 (pdf p.180) uses the word 'bundle' when describing the cosmological spacetime and points to §C.11 for its technical meaning.
- *backward* → **GA ch19**: A Chapter 19 margin pointer (pdf p.219) on conformal diagrams says topology, the study of properties preserved under deformations, is introduced here (§C.4).
- *backward* → **GA ch07**: Fig. 7.2 pictures a sphere embedded in R^3 to explain the failure of parallelism, the kind of extrinsic crutch the opening of this appendix sets aside.

## Teaching gems

### Read every composite map aloud as an input/output sentence (put in a coordinate, phi^{-1} returns the point, psi returns the new coordinate). · GA §C.5 p.571 (pdf 588)

**Why it works:** Turns intimidating symbol chains into procedural steps a learner can trace with a finger on the diagram; the same habit then decodes f o phi^{-1}, psi o f o phi^{-1} and phi o c.

**App idea:** Hover any composite symbol to animate the corresponding arrow path through the manifold-and-chart diagram, with a spoken or captioned input/output sentence.

### Force the need for multiple charts with the circle: the angle coordinate labels one point twice, so drop it and cover it with a second chart. · GA §C.5 p.570 (pdf 587)

**Why it works:** The smallest possible example shows that atlases come from global topology, not from technical fussiness.

**App idea:** Two-chart circle demo with jumping coordinate readouts and a transition-map plot.

### Motivate smooth atlases by the factorization f o psi^{-1} = (f o phi^{-1}) o (phi o psi^{-1}). · GA §C.7 p.572 (pdf 589)

**Why it works:** Shows exactly where chart-dependence would enter and makes the C^infinity transition requirement feel inevitable rather than axiomatic.

**App idea:** Toggle a transition map between smooth and kinked (e.g. using a cube-root reparametrization) and watch a smooth-looking function acquire a kink in the second chart.

### Use x^3 as the minimal counterexample separating a smooth homeomorphism from a diffeomorphism. · GA §C.7 p.573 (pdf 590)

**Why it works:** One familiar function isolates the subtle requirement that the inverse be smooth.

**App idea:** Plot x^3 and its inverse with their derivatives; the inverse's derivative spikes at 0 as the learner zooms.

### Define a tangent vector by what it does to functions along a curve, then insert the chart to derive components with the chain rule. · GA §C.10 p.576 (pdf 593)

**Why it works:** Avoids arrows entirely, works on any manifold, and produces the familiar basis partial/partial x^mu as an output rather than an assumption.

**App idea:** Directional-derivative lab with direct and chain-rule readouts, plus equivalent curves giving identical vectors.

### Build the bundle by redrawing tangent lines on a curve as vertical, non-crossing fibres and lifting them above the base. · GA §C.11 p.578 (pdf 595)

**Why it works:** A few pictorial moves take the learner from a well-known image to the abstract total space with projection.

**App idea:** Animated tangent-combing sequence ending in a tangent bundle with draggable beads.

### Distinguish cylinder and Moebius band by whether a section can avoid the zero section. · GA §C.11 p.579 (pdf 596)

**Why it works:** Gives a concrete, testable global invariant; learners can try and fail to draw a nowhere-zero section.

**App idea:** Section painter with crossing counter on both bundles.

### Derive nabla . T = 0 from diffeomorphism invariance inside a mathematics appendix. · GA §C.7 p.574 (pdf 591)

**Why it works:** Shows that abstract manifold machinery earns its keep physically: conservation is a consequence of gauge symmetry.

**App idea:** Step-through derivation card where each line highlights which ingredient (Lie derivative, symmetry, integration by parts, arbitrariness of u) is used.


## Gaps and pitfalls

- **The third bullet of the formal manifold definition states that phi_i o phi_j^{-1} takes points of phi_i(U_i cap U_j) to phi_j(U_i cap U_j); the correct direction is from phi_j(U_i cap U_j) to phi_i(U_i cap U_j). The same bullet list also drops the index on phi.** — Learners tracing arrows on Fig. C.10 get contradictory directions and may lose trust in the composite-map reading. *Suggestion:* Always check composites right to left: phi_j^{-1} acts first, so the input lives in the image of phi_j.
- **Margin note equation (C.12) writes the left side with indices mu nu but the right side with alpha beta, and the short form as 2u_(alpha;beta).** — Index mismatch confuses readers who try to follow Example C.10 line by line. *Suggestion:* Use (L_u g)_{mu nu} = u^sigma g_{mu nu;sigma} + g_{mu sigma} u^sigma_{;nu} + g_{sigma nu} u^sigma_{;mu} = 2 u_(mu;nu), noting the first term vanishes by metric compatibility.
- **Fig. C.5's caption says it belongs to Example C.5, but it is discussed in Example C.1 (Example C.5 is about the circle).** — Readers searching for the discussion look in the wrong place. *Suggestion:* Link the graphs to Example C.1 in any adapted material.
- **The Hausdorff property is glossed as 'any line can be infinitely subdivided', which is not what the property says.** — Learners may think Hausdorff concerns divisibility or continuity of the real line and miss the separation idea. *Suggestion:* Teach it as: distinct points can be enclosed in non-overlapping neighbourhoods; show the line with two origins as the standard failure.
- **The manifold definition omits second countability (and only implicitly includes Hausdorff), and allows the dimension n to vary from point to point.** — Readers moving to rigorous texts meet extra axioms and pathological examples (long line, line with two origins) without context. *Suggestion:* Mention briefly that standard definitions add Hausdorff and second-countable conditions to rule out such pathologies, and that connected manifolds have a single dimension.
- **Example C.12 lists 'a closed disc with a hole in it' as non-compact; a closed disc minus an open disc (a closed annulus) is compact. Only removing a point or a region together with its edge makes it non-compact.** — Learners may conclude that any hole destroys compactness, conflicting with compact surfaces such as the torus. *Suggestion:* Specify: deleting a single point (punctured disc) destroys compactness; cutting out an open disc leaves a compact annulus.
- **The sequential definition says every sequence must have a limit in the region; strictly, every sequence must have a subsequence converging to a point of the region (an accumulation point). The book mentions accumulation points in passing but its examples only use convergent sequences.** — An oscillating sequence 0,1,0,1,... in [0,1] has no limit, which seems to contradict the definition. *Suggestion:* State the accumulation-point version and demonstrate with an oscillating sequence.
- **Example C.10 omits that the matter fields must satisfy their equations of motion, and takes the diffeomorphism variation of the metric with a sign convention that depends on active versus passive viewpoint; a boundary term is discarded silently.** — Learners may think nabla . T = 0 holds for any field configuration, or be confused by sign differences with other texts. *Suggestion:* Add that diffeomorphisms also change the matter fields, whose variation vanishes on-shell; note that the overall sign of delta g does not affect the conclusion; mention that u is taken to vanish on the boundary.
- **Example C.9 infers invertibility from a non-zero Jacobian, which in general only gives local invertibility.** — Learners may overgeneralize to non-linear maps. *Suggestion:* Note that the example is linear; show a non-linear map with non-zero Jacobian that is not one-to-one.
- **Example C.13 describes the coordinate function as phi^nu o c(lambda), mixing the coordinate function on the manifold with its restriction to the curve.** — Blurs the distinction between a function on M and its values along a curve, which the whole section tries to keep separate. *Suggestion:* Take f = phi^nu (a function on U); then f o c = x^nu(lambda) and v[phi^nu] = dx^nu/dlambda.
- **The text says bundles are 'locally trivial if they are formed from a product space', blurring the definition; local triviality is part of what makes something a fibre bundle. Also the text never states that sections of the tangent bundle are vector fields, nor that comparing fibres needs a connection.** — Learners miss the direct physics link (fields as sections, gauge potentials as connections) that motivates the section. *Suggestion:* Define bundles with local product neighbourhoods up front and state explicitly: a vector field is a section of TM; parallel transport is extra structure on the bundle.
- **The distinction between the book's 'into' (defined on the whole domain) and common usages is not flagged, and the definition of an open cover says points are 'in the collection' rather than in some member of it.** — Minor terminological confusion when reading other sources. *Suggestion:* Use injective/surjective/bijective consistently and phrase covers as 'the union contains A'.
- **Tangent space dimension, linear structure (how to add vectors from different curves) and the correspondence between derivations and equivalence classes are asserted rather than shown.** — Readers may not see why T_P M is a vector space of dimension m. *Suggestion:* Show that v = v^mu partial_mu for arbitrary numbers v^mu is realized by the curve x^mu(lambda) = x^mu(P) + lambda v^mu, so the space is m-dimensional with basis partial_mu.
- **The chapter-summary definition of a manifold asks only for a continuous one-to-one map onto an open set of R^n, dropping the requirement that the inverse be continuous (a homeomorphism), which the main text does state. The compactness bullet is also garbled: it reads as if having a boundary were itself a failure, whereas §C.8 says a compact region must include its boundary.** — A reader revising from the summary alone gets a weaker manifold definition (a continuous bijection need not be a homeomorphism, e.g. wrapping [0, 2 pi) onto the circle) and may think closed intervals are not compact. *Suggestion:* Restate the summary as: every point has an open neighbourhood homeomorphic to an open subset of R^n; compact regions do not run off to infinity and do not have points missing from their interior or their boundary.
- **Section C.7 writes the overlap condition as U intersect V not equal to 0 where the empty set is meant, and uses both (U, phi) and (phi, U) for a chart on consecutive pages.** — Minor notational noise; a novice may read the 0 as a number. *Suggestion:* Write the overlap condition with the empty-set symbol and keep the chart written as (U, phi) throughout.

## Tutor notes

- Opening question: 'If the universe is curved, curved inside what?' Use it to motivate intrinsic geometry and the manifold-plus-metric split before any definitions.
- Recommended order: pyramid of structure -> open sets (only enough to say 'nearby') -> maps and bijections -> homeomorphism with the clay picture -> manifold via magnifying glass -> circle needs two charts -> transition maps -> why smooth transitions -> tangent vectors as derivatives -> bundles by picture. Example C.10 can be deferred until the learner knows Lie derivatives and actions.
- Check for understanding: ask the learner to write the coordinate transformation between the two circle charts explicitly (theta_2 = theta_1 on one part of the overlap and theta_1 - 2 pi on the other) and to say where it is defined.
- Have the learner read composites right to left and narrate them; errors in direction (as in the printed manifold-definition bullet) are a good diagnostic exercise.
- Quick classifier drill: is x^3 a homeomorphism of R? A diffeomorphism? Why the difference? Then x + x^3 (yes to both, since its derivative never vanishes).
- Common learner question: 'Why not just use arrows for vectors?' Answer: arrows need a straight line and a common origin, neither exists on a bare manifold; a derivative along a curve only needs points and functions.
- Common learner question: 'Are the sphere and the ellipsoid the same manifold?' Yes, diffeomorphic; they differ only in metric. Use this to separate manifold from metric.
- For compactness, avoid Heine-Borel formality with beginners: use the three failure modes (escapes to infinity, missing edge, missing point) and the 1/n sequence; mention that the torus and sphere are compact while the plane is not.
- Bundle intuition check: ask the learner to try to draw a closed curve on a Moebius band that never crosses the centre line and returns to its start at the same height; let them discover it is impossible.
- Physics link to emphasize beyond the text: a vector field is a section of the tangent bundle, and gauge potentials in electromagnetism are connections on bundles; the hairy-ball theorem (not in this appendix) shows TS^2 is not trivial, contrasting with TS^1.
- Flag printed issues if the learner is reading the book: transition-map direction on p.571, index mismatch in eqn (C.12), Fig. C.5 caption pointing to the wrong example, the ambiguous 'disc with a hole' in Example C.12, and the weakened manifold definition in the chapter summary (p.580).
- Adapt by level: for novices stop at charts, tangent vectors as derivatives, and cylinder versus Moebius; for advanced learners do Example C.10 in full and discuss why diffeomorphism invariance makes local energy conservation a Bianchi-identity-compatible statement.
- If the learner revises from the chapter summary, correct two items: a manifold needs local homeomorphisms (continuous both ways), not just continuous bijections; and compactness allows (indeed requires) a region to contain its boundary. The map t -> (cos t, sin t) from [0, 2 pi) onto the circle is a quick continuous bijection whose inverse is not continuous.

## Verification

**Verdict:** fixed

**Fixes applied**
- role_in_book: tangent-plane-to-a-surface picture attributed to Chapter 30 (Fig. 30.6), not Chapter 7; added the Chapter 15/19/44/50 pointers to this appendix found by searching the book.
- Cross-reference for the embedded tangent-plane picture of Fig. C.15(b) retargeted from ch7 to ch30 (Fig. 30.6); the ch7 embedded picture is the sphere in R^3, now mentioned in role_in_book.
- Added missing backward cross-references from Chapters 15 (bundles), 19 (topology) and 7 (embedded sphere); all chapter targets normalized to zero-padded ids.
- Fig. C.7 locator section corrected from C.4 to C.5 (it illustrates Example C.3).
- Locators pointing at the chapter summary (pdf 597) relabelled 'Chapter summary' instead of §C.11.
- Magnifying-glass analogy limits rewritten: the old text implied the double-cone apex is topologically a manifold point; only a single-cone apex is, while the double cone fails topologically (its punctured neighbourhood is disconnected).
- Added the two margin notes the dossier had skipped: note 4 (f: R^n -> R as ordinary f(x^1..x^n)) and note 10 (dimensions m and n for maps between manifolds); 20 of 20 notes now covered.
- Added gaps: the chapter-summary manifold definition omits continuity of the inverse and its compactness bullet is garbled; the 'U cap V != 0' empty-set typo in §C.7.

**Residual concerns**
- No suspect short pages or figures-without-image were listed in the inventory; the Fig. C.2 (a)-(d) panels are vector art with no exported image and are described from the page-583 render only.
- Figures not opened individually (img-348, 349, 350, 352, 354, 355, 359, 362, 365, 367, 369, 376) keep the earlier writer's descriptions; the neighbouring panels that were opened all matched, so these are likely accurate.
- Several dossier claims go beyond the book (second countability, on-shell matter fields in Example C.10, sections of TM as vector fields, nonzero Jacobian gives only local invertibility, hairy-ball theorem). They are marked as notes, gaps or tutor notes, not as book content.

**Coverage:** toc_sections: 11, sections: 12, inventory_figures: 33, figures: 34, inventory_examples: 0, worked_examples: 18, concepts: 59, key_equations: 37, locators_checked: 22, locators_wrong: 2, pages_rendered: 4
