---
type: "source-unit"
book: "gifted-amateur"
book_short: "GA"
unit: "appD"
title: "Embedding"
part: null
printed_pages: [581, 586]
pdf_pages: [598, 603]
math_level: 2
conceptual_level: 3
novice_friendliness: 4
style_tags: ["example-driven", "computational-recipe", "diagram-driven", "conversational-informal", "geometric-first"]
concepts: ["embedding", "intrinsic description of geometry", "induced metric", "embedding coordinates versus object coordinates", "Euclidean line element in R^N", "method I (parametric embedding)", "method II (implicit-surface elimination)", "metric tensor", "coordinate transformation of a line element", "circle metric", "2-sphere metric", "3-sphere metric", "embedding diagram", "surface-of-revolution ansatz", "Einstein-Rosen bridge", "Flamm's paraboloid", "wormhole throat", "asymptotic flatness", "geometry versus topology", "traversable wormhole and negative energy", "hyperbolic plane", "non-embeddability of the hyperbolic plane in R^3", "partial embedding", "Minding's theorem", "Gaussian curvature", "pseudo-Euclidean space", "two-sheet hyperboloid", "one-sheet hyperboloid", "Lorentzian induced metric", "induced metric in a pseudo-Euclidean ambient space", "Rindler coordinates as an embedding", "paraboloid induced metric", "torus induced metric", "Nash embedding theorem", "Minkowski metric", "Schwarzschild radius"]
verification: "fixed"
---

# GA appD · Embedding

> A short appendix that teaches two recipes for the induced metric of a surface sitting in flat space (parametric 'method I' and implicit-surface 'method II'), checks them on the circle and 2-sphere, runs the logic backwards to draw a picture of the Einstein-Rosen bridge, shows that the hyperbolic plane refuses to fit in ordinary 3-space, and rescues it by mounting hyperboloids in a flat space with one minus sign.

**Pages:** printed 581–586 · pdf 598–603 · **Difficulty:** math 2/5, conceptual 3/5, novice-friendliness 4/5

The calculations are chain-rule and trigonometric or hyperbolic identities, well within undergraduate calculus. Conceptual load rises in the second half: the reverse embedding problem, geometry versus topology, a pseudo-Euclidean host, and a Lorentzian induced metric presented without comment. Symbol slips (theta and phi swapping, a D.1 reference that should be D.2) and the terse 'embedding is impossible' claim can trip novices, and the wormhole is never identified as a Schwarzschild slice.

## Role in the book

The main text insists that spacetime must be described from the inside, with no higher-dimensional container (Chapters 7, 11 and Appendix C). This appendix is the practical counterweight: a toolkit for turning a line element into a picture, or a picture into a line element, used as a visual crutch rather than as physics. Chapter 5 points here as the second way (besides light cones) to visualize a metric; Chapter 16 leans on it for the k = +1 sphere and k = -1 hyperboloid Robertson-Walker spaces; Chapters 18, 19 and 49 reuse the hyperboloid-in-Minkowski construction for de Sitter and anti-de Sitter spacetime; Exercise 23.5 embeds Flamm's paraboloid; and Chapter 27 returns to the wormhole with Kruskal coordinates. It is placed at the back so the main line of argument never depends on embedding.

## Learning objectives

- Reader can explain why GR does not assume spacetime lives inside a bigger flat space, yet still finds embeddings useful for two jobs: computing an induced metric and visualizing a given metric.
- Reader can derive g_{mu nu} = sum_alpha (dX^alpha/dx^mu)(dX^alpha/dx^nu) from the flat line element by the chain rule (method I).
- Reader can find an induced metric by eliminating one embedding coordinate with the surface equation and then picking adapted coordinates (method II).
- Reader can compute the induced metrics of a circle of radius a, the unit 2-sphere, a paraboloid, a torus and the 3-sphere.
- Reader can recognise that two different-looking line elements (d theta^2 + sin^2 theta d phi^2 and dr^2/(1-r^2) + r^2 d phi^2) describe the same geometry via r = sin theta.
- Reader can embed a rotationally symmetric 2D metric as a surface of revolution by fixing the circumference with (r cos phi, r sin phi) and solving an ODE for the height Z(r).
- Reader can reproduce the Einstein-Rosen bridge embedding Z^2 = 4 r_S (r - r_S) and describe the throat and two asymptotically flat sheets.
- Reader can state that a metric fixes local geometry but not global topology, using the two wormhole gluings of Fig. D.5.
- Reader can show why the surface-of-revolution ansatz for the hyperbolic metric d chi^2 + sinh^2 chi d phi^2 in R^3 demands an imaginary slope, and explain the geometric reason (circumference grows too fast).
- Reader can embed the hyperbolic plane as the two-sheet hyperboloid X^2 + Y^2 - W^2 = -1 in pseudo-Euclidean space and verify the induced metric.
- Reader can compute the induced metric on the one-sheet hyperboloid, notice that it is Lorentzian, and avoid misreading its sphere-like r-form as a sphere.
- Reader can generalize method I to a Minkowski ambient space using eta_{alpha beta} and recover the Rindler metric from T = x sinh t, X = x cosh t.

## Assumed background

- Line element ds^2 = g_{mu nu} dx^mu dx^nu and reading metric components off it — earlier-in-this-book (GA ch3, ch5 §5.1)
- Einstein summation convention for repeated indices — earlier-in-this-book (GA ch2, ch4)
- Chain rule for partial derivatives and total differentials — undergrad-calculus
- Spherical polar and cylindrical polar coordinates in 3D — undergrad-calculus (GA ch3 §3.1)
- Hyperbolic functions and the identity cosh^2 - sinh^2 = 1 — undergrad-calculus
- Solving a separable first-order ODE by direct integration — undergrad-calculus
- Minkowski metric with signature (-,+,+,+) and the meaning of a minus sign in a line element — earlier-in-this-book (GA ch1, ch2)
- Intrinsic versus extrinsic curvature; beings confined to a surface — earlier-in-this-book (GA ch7 §7.1, ch11 opening)
- Rindler metric -x^2 dt^2 + dx^2 for accelerated observers (for Exercise D.5) — earlier-in-this-book (GA ch5 §5.3)
- Schwarzschild radius r_S = 2GM/c^2 (helps recognise the Example D.2 metric, though not required) — earlier-in-this-book (GA ch21)
- Notion of topology as connectivity independent of distances — advanced-math (GA appC)

## Teaching approach

Recipe-first and example-driven. After a one-page philosophical framing (a beetle confined to a bowl), the appendix hands the reader two mechanical procedures and immediately runs each on the same simple objects so the answers can be compared. It then reverses direction (metric to picture) with one physically loaded example, the wormhole, and deliberately stages a failure (hyperbolic space) so the reader learns the limits of the method and the fix of changing the signature of the ambient space. Pictures are schematic sketches; the real content is in short boxed calculations, with generalizations pushed into five exercises.

**Style:** example-driven, computational-recipe, diagram-driven, conversational-informal, geometric-first

**Narrative arc**

1. Motivating tension: we see a bowl's curvature because it sits in 3D space, but there is no evidence spacetime sits in anything, so geometry must be done by a confined geometer; embedding is kept only as a calculational and visual aid.
2. Start with the easier direction: an object already placed in flat R^N, whose metric in its own coordinates is the induced metric.
3. Method I: write the embedding coordinates as functions of object coordinates, expand dX^alpha by the chain rule, and read off g_{mu nu} as a sum of products of derivatives.
4. Method II: use the surface equation to eliminate one embedding coordinate, then guess convenient object coordinates.
5. Check both methods on the circle (1D in R^2) and the unit 2-sphere (2D in R^3); reconcile the different-looking method-II form through r = sin theta.
6. Reverse the problem: given a line element, find a surface with that metric. Use a surface-of-revolution ansatz on the Einstein-Rosen bridge metric and solve for Z(r).
7. Interpret the picture: two flat sheets joined by a throat; stress that the metric says nothing about topology, so the throat could join distant regions or separate universes; note negative energy would be needed to build one.
8. Stage a failure: the same ansatz for the constant-negative-curvature metric d chi^2 + sinh^2 chi d phi^2 gives an imaginary dZ/d chi.
9. Two escapes: embed only part of the surface (Exercise D.4, with Minding's theorem), or change the ambient space to pseudo-Euclidean dX^2 + dY^2 - dW^2.
10. Two-sheet hyperboloid reproduces the hyperbolic metric; one-sheet hyperboloid gives -d chi^2 + cosh^2 chi d theta^2, rewritten in a sphere-like form with a warning not to read it as a sphere; pointer to cosmology.
11. One-bullet summary, then exercises generalize: paraboloid, 3-sphere, torus, partial hyperbolic embedding, and Rindler coordinates in Minkowski space.

**Signature moves**

- Solve every example twice (method I and method II) so that agreement of the two answers is the built-in check.
- Treat an apparently different line element as a coordinate puzzle: find the substitution (r = sin theta, cosh chi = r) that maps one form to the other.
- Use a cylindrically symmetric ansatz (r cos phi, r sin phi, Z(r)) that automatically satisfies the angular metric component, leaving a single ODE for the profile.
- Show the failure of the method explicitly (square root of a negative number) before offering the fix, so the limitation is earned rather than asserted.
- Rescue a failed embedding by flipping one sign in the ambient metric, turning an impossible Euclidean embedding into a natural hyperboloid.
- Pair a geometric picture with an explicit disclaimer: the embedding shows geometry, not topology, and a sphere-like formula is not a sphere.
- Push generalizations (3-sphere, torus, Minkowski ambient metric with eta) into exercises with hints rather than the main text.

## Section by section

### Opening: the confined geometer and why embed at all — p.581 (pdf 598)

Opens with Einstein's image of a blind beetle on a curved branch. Everyday curvature (a bowl) is visible because the object sits in 3D Euclidean space, but nothing suggests spacetime sits inside a larger flat space, so adding one would be unwarranted structure. We are like a beetle unable to leave the bowl, whose length measurements use only two coordinates. Embedding is nonetheless kept for two jobs: deriving a curved space's metric in the insider's coordinates, and visualizing a given metric. The induced metric is defined as the metric expressed in the object's own coordinates after relating them to Euclidean ones. Margin notes cite Zee as the source of the treatment and mention Nash's embedding theorems.

**Concepts:** embedding, intrinsic description of geometry, induced metric, Nash embedding theorem, Euclidean line element in R^N

**Key moves**
- Contrast an embedded bowl with spacetime, which has no known container, to justify an intrinsic description.
- Keep embedding for two limited purposes: metric from shape, and picture from metric.
- Name the object coordinates (internal) versus the embedding coordinates (Euclidean) and define the induced metric.
- Recall the Pythagorean line element in R^3 (D.1) as the starting point.

### Two methods for the induced metric — p.582 (pdf 599)

Generalizes the flat line element to N dimensions and considers a D-dimensional object in R^N. Method I applies when each embedding coordinate is an explicit function of the object coordinates: the chain rule turns the sum of squared dX^alpha into a quadratic form in dx^mu whose coefficients are the induced metric components (D.5). Method II applies when the shape is given as an equation in the embedding coordinates, such as Z = f(X, Y): the equation eliminates one coordinate from the flat line element, and then a good choice of object coordinates tidies the result.

**Concepts:** induced metric, method I (parametric embedding), method II (implicit-surface elimination), Euclidean line element in R^N, embedding coordinates versus object coordinates

**Key moves**
- Write the Euclidean interval as a sum over alpha of (dX^alpha)^2 (D.2).
- Expand dX^alpha = (dX^alpha/dx^mu) dx^mu (D.3) and substitute (D.4).
- Compare with ds^2 = g_{mu nu} dx^mu dx^nu to read off g_{mu nu} (D.5).
- For method II, use the constraint Z = f(X, Y) to remove dZ, then choose adapted coordinates.

### Example D.1: circle and 2-sphere, both methods — p.582 (pdf 599)

Part (a) embeds a circle of radius a in the plane. Method I with X = a cos theta, Y = a sin theta gives g_theta theta = a^2. Method II writes the circle as Y = sqrt(a^2 - X^2), expresses ds^2 in terms of dX, and recovers a^2 d theta^2 after X = a cos theta. Part (b) embeds the unit 2-sphere in R^3: method I with the usual spherical parametrization gives d theta^2 + sin^2 theta d phi^2 with no cross term. Method II eliminates Z using X^2 + Y^2 + Z^2 = 1, switches to cylindrical (r, phi), and obtains dr^2/(1 - r^2) + r^2 d phi^2, which matches after r = sin theta.

**Concepts:** circle metric, 2-sphere metric, method I (parametric embedding), method II (implicit-surface elimination), coordinate transformation of a line element

**Key moves**
- Differentiate the parametrization and sum squares: sin^2 + cos^2 collapses the circle to a^2.
- In method II, factor dX^2 out of dX^2 + dY^2 and insert the slope of the graph.
- For the sphere, compute g_theta theta, g_phi phi and g_theta phi separately.
- Eliminate Z via Z dZ = -(X dX + Y dY), then exploit cylindrical symmetry.
- Reconcile the two sphere forms by r = sin theta, so dr^2/(1 - r^2) = d theta^2.

### Example D.2: visualizing the Einstein-Rosen bridge — p.584 (pdf 601)

Turns to the reverse task of drawing a surface whose metric is given. For the 2D metric r dr^2/(r - r_S) + r^2 d phi^2, method I requires the derivative sums to match g_rr and g_phi phi. The trial embedding (r cos, r sin, Z(r)) takes care of the angular part automatically and leaves 1 + (dZ/dr)^2 = r/(r - r_S), solved by Z^2 = 4 r_S (r - r_S). Revolving this sideways parabola gives two asymptotically flat sheets joined by a narrow throat. Because a metric encodes local geometry but not topology, the throat could join two remote places in one universe (a possible shortcut) or two separate universes; a margin note adds that building one would need negative energy, like the Alcubierre drive.

**Concepts:** embedding diagram, Einstein-Rosen bridge, Flamm's paraboloid, surface-of-revolution ansatz, wormhole throat, asymptotic flatness, geometry versus topology, traversable wormhole and negative energy

**Key moves**
- Write the two method-I conditions as equations for unknown embedding functions (D.20).
- Choose X^1, X^2 as r cos and r sin so the circumference condition holds identically.
- Reduce the radial condition to an ODE for Z(r) (D.21) and integrate to a parabola.
- Use both signs of the square root to obtain upper and lower sheets meeting at r = r_S.
- Separate what the metric fixes (local distances) from what it leaves open (global connectivity).

### Example D.3: the hyperbolic plane will not fit in R^3 — p.584 (pdf 601)

Presents hyperbolic space, d chi^2 + sinh^2 chi d phi^2, as the key example of a surface that resists Euclidean embedding. With the symmetric trial X = sinh chi cos phi, Y = sinh chi sin phi, the angular condition forces Z to be independent of phi, but the radial condition demands (dZ/d chi)^2 = 1 - cosh^2 chi = -sinh^2 chi, which has no real solution. The attempt fails.

**Concepts:** hyperbolic plane, non-embeddability of the hyperbolic plane in R^3, surface-of-revolution ansatz, method I (parametric embedding)

**Key moves**
- Reuse the cylindrically symmetric ansatz with circumference radius sinh chi.
- Show dZ/d phi = 0 from the angular condition.
- Show the radial condition needs a negative square, since the horizontal part alone already contributes cosh^2 chi > 1.

### Pseudo-Euclidean rescue and Example D.4: hyperboloids — p.585 (pdf 602)

Declares the Euclidean embedding impossible and offers two ways out: embed only a piece (Exercise D.4) or use a flat ambient space with metric dX^2 + dY^2 - dW^2. Part (a): the two-sheet hyperboloid X^2 + Y^2 - W^2 = -1, parametrized with sinh and cosh, has exactly the hyperbolic metric as its induced metric (Fig. D.6). Part (b): the one-sheet hyperboloid X^2 + Y^2 - W^2 = 1 gives -d chi^2 + cosh^2 chi d theta^2; with cosh chi = r this becomes dr^2/(1 - r^2) + r^2 d theta^2, formally the 2-sphere expression, obtainable directly with W = sqrt(r^2 - 1). The authors warn that the surface is not a sphere: eliminating W leaves concentric circles with distances encoded between them, and r = sin theta cannot satisfy r^2 - W^2 = 1 while r = cosh chi can. Chapter 18 is cited for cosmological uses.

**Concepts:** pseudo-Euclidean space, two-sheet hyperboloid, one-sheet hyperboloid, hyperbolic plane, Lorentzian induced metric, partial embedding, coordinate transformation of a line element

**Key moves**
- Change the ambient signature by giving W a minus sign (D.26).
- Parametrize the two-sheet hyperboloid so that the surface equation holds identically (D.27).
- Let the minus sign on dW^2 cancel the excess cosh^2 chi that broke the Euclidean attempt (D.28).
- Repeat for the one-sheet hyperboloid and find the sign of the d chi^2 term flips (D.30).
- Substitute cosh chi = r to produce a sphere-like form and caution against a literal reading (D.31, D.32).

### Chapter summary — p.585 (pdf 602)

A single bullet: embedding lets one visualize a space with a metric by placing it inside a flat space of higher dimension. The summary omits the induced-metric recipes, the failure case and the pseudo-Euclidean fix, which the tutor should restore.

**Concepts:** embedding, embedding diagram

**Key moves**
- Restate the purpose of embedding as visualization.

### Exercises D.1-D.5 — p.586 (pdf 603)

Five exercises extend the recipes: a paraboloid by method II, the 3-sphere in R^4, the torus by method I, a partial Euclidean embedding of a different constant-negative-curvature metric d chi^2 + cosh^2 chi d phi^2 justified by Minding's theorem, and Rindler coordinates embedded in 2D Minkowski space using the eta-weighted version of eqn D.5. Figures of the paraboloid and torus accompany the problems.

**Concepts:** paraboloid induced metric, 3-sphere metric, torus induced metric, partial embedding, Minding's theorem, induced metric in a pseudo-Euclidean ambient space, Rindler coordinates as an embedding

**Key moves**
- Paraboloid: dZ = a(X dX + Y dY) = a r dr, so g_rr = 1 + a^2 r^2.
- 3-sphere: eliminate W, get dr^2/(1 - r^2) + r^2 d Omega_2^2, then r = sin psi.
- Torus: parametrize by two angles before applying method I.
- Hyperbolic collar: the same ansatz works while sinh chi < 1.
- Rindler: weight products of derivatives by eta_{alpha beta} to get -x^2 dt^2 + dx^2.

## Concepts

### embedding

*definition · core* · also: isometric embedding, mounting a space in a higher-dimensional space

Placing a D-dimensional space inside a higher-dimensional flat space by a smooth, one-to-one map such that distances measured along the placed surface with the ambient metric equal the distances given by the space's own metric.

**How introduced:** Motivated by everyday objects such as a bowl, whose curvature we notice because it sits in 3D space; then demoted from a physical claim about spacetime to a tool for computing and drawing metrics.

**Prerequisites:** metric tensor, Euclidean line element in R^N

$$
X^\alpha = X^\alpha(x^1,\dots,x^D),\ \alpha = 1,\dots,N
$$

**Notes:** The book uses 'embed' loosely for both isometric embeddings and partial or local ones; strictly, several examples are local immersions of patches.

**Where:** GA p.581 (pdf 598); GA p.582 (pdf 599); GA p.585 (pdf 602)

### intrinsic description of geometry

*principle · developed* · also: confined geometer viewpoint, beetle on the bowl

Geometry of a space should be expressed using only coordinates and measurements available to an observer who cannot leave that space, without assuming any higher-dimensional container.

**How introduced:** Einstein's blind-beetle epigraph and a beetle stuck on a bowl; the authors argue no evidence supports spacetime sitting in a bigger flat space, so adding one would be unnecessary structure.

**Prerequisites:** embedding

**Notes:** Revisits the insider theme of GA ch7 and ch11; Appendix C makes it rigorous through manifolds.

**Where:** GA p.581 (pdf 598)

### induced metric

*definition · core* · also: pullback metric, first fundamental form (for surfaces)

The metric a submanifold inherits from its ambient space: its components in the object coordinates are obtained by substituting the embedding functions into the ambient line element.

**How introduced:** Introduced as the easier half of the embedding problem: an object already sitting in R^N has a metric in its own coordinates obtained by relating those to the Euclidean ones; computed by two methods.

**Prerequisites:** embedding, metric tensor, chain rule for partial derivatives

$$
g_{\mu\nu}=\sum_{\alpha}\frac{\partial X^{\alpha}}{\partial x^{\mu}}\frac{\partial X^{\alpha}}{\partial x^{\nu}}
$$

$$
g_{\mu\nu}=\eta_{\alpha\beta}\frac{\partial X^{\alpha}}{\partial x^{\mu}}\frac{\partial X^{\beta}}{\partial x^{\nu}}
$$

**Notes:** Chapter 30 Exercise 30.7 and Chapter 49 §49.2 (string world sheet) reuse the same construction.

**Where:** GA p.581 (pdf 598); GA p.582 (pdf 599)

### embedding coordinates versus object coordinates

*convention · introduced* · also: Euclidean coordinates X^alpha, internal coordinates x^mu

Two coordinate systems in play: N ambient Cartesian coordinates X^alpha labelling points of the flat container, and D coordinates x^mu that an inhabitant of the surface uses to label points within it.

**How introduced:** Set up in the opening and at the start of method I; the circle uses theta, the sphere (theta, phi), the wormhole (r, phi).

**Prerequisites:** embedding

**Where:** GA p.581 (pdf 598); GA p.582 (pdf 599)

### Euclidean line element in R^N

*definition · revisited* · also: flat N-dimensional metric

In N-dimensional Euclidean space with Cartesian coordinates the squared distance between neighbouring points is the sum of the squares of the coordinate differences.

**How introduced:** Recalled for R^3 and generalized to R^N as the starting point of both methods.

**Prerequisites:** metric tensor

$$
\mathrm{d}s^2=\sum_{\alpha=1}^{N}(\mathrm{d}X^\alpha)^2
$$

**Where:** GA p.581 (pdf 598); GA p.582 (pdf 599)

### method I (parametric embedding)

*technique · core* · also: method I, Jacobian method for the induced metric

When each ambient coordinate is known as a function of the object coordinates, the induced metric component g_{mu nu} equals the sum over ambient directions of the product of derivatives of X^alpha with respect to x^mu and x^nu.

**How introduced:** Derived by expanding dX^alpha with the chain rule inside the flat line element and matching to g_{mu nu} dx^mu dx^nu; applied to circle, sphere, wormhole, hyperbolic surface, torus.

**Prerequisites:** induced metric, chain rule for partial derivatives, Einstein summation convention

$$
g_{\mu\nu}=\sum_{\alpha}\frac{\partial X^{\alpha}}{\partial x^{\mu}}\frac{\partial X^{\alpha}}{\partial x^{\nu}}
$$

**Notes:** Used in reverse (unknown X^alpha, known g) it becomes a set of nonlinear PDEs; symmetry ansatzes reduce them to ODEs.

**Where:** GA p.582 (pdf 599); GA p.583 (pdf 600); GA p.584 (pdf 601)

### method II (implicit-surface elimination)

*technique · core* · also: method II

When the object is given by an equation among the ambient coordinates, differentiate that equation to express one differential in terms of the others, substitute into the flat line element, and then change to convenient object coordinates.

**How introduced:** Described after method I and demonstrated on the circle (graph Y of X) and sphere (eliminating Z, then cylindrical coordinates); Exercises D.1 and D.2 practise it.

**Prerequisites:** induced metric, total differential, coordinate transformation of a line element

$$
\mathrm{d}s^2=\mathrm{d}X^2+\mathrm{d}Y^2+\left(\frac{\partial f}{\partial X}\mathrm{d}X+\frac{\partial f}{\partial Y}\mathrm{d}Y\right)^2\ \text{for } Z=f(X,Y)
$$

**Notes:** Solving the constraint for one coordinate (a square root) only covers one branch, e.g. the upper semicircle or one hemisphere.

**Where:** GA p.582 (pdf 599); GA p.583 (pdf 600); GA p.586 (pdf 603)

### metric tensor

*mathematical-object · revisited* · also: line element, g_{mu nu}

A symmetric tensor field that assigns squared lengths to infinitesimal displacements, ds^2 = g_{mu nu} dx^mu dx^nu, and so fixes all local distances and angles in a space.

**How introduced:** Assumed from earlier chapters and used as the target that the embedding reproduces.

$$
\mathrm{d}s^2=g_{\mu\nu}\mathrm{d}x^\mu\mathrm{d}x^\nu
$$

**Where:** GA p.582 (pdf 599)

### coordinate transformation of a line element

*operation · developed* · also: reparametrization, change of variables in ds^2

Substituting new coordinates and their differentials into a line element produces a different-looking expression for the same geometry; two metrics are the same geometry if some substitution maps one to the other.

**How introduced:** Arises when method II gives the sphere as dr^2/(1-r^2) + r^2 d phi^2 and r = sin theta turns it into the method-I form; reused with cosh chi = r for the one-sheet hyperboloid.

**Prerequisites:** metric tensor

$$
r=\sin\theta\ \Rightarrow\ \frac{\mathrm{d}r^2}{1-r^2}=\mathrm{d}\theta^2
$$

**Notes:** The substitution must also respect the allowed range: r = sin theta needs r <= 1, which is why it fails on the one-sheet hyperboloid where r >= 1.

**Where:** GA p.583 (pdf 600); GA p.585 (pdf 602)

### circle metric

*solution-or-model · introduced* · also: 1D induced metric of a circle

A circle of radius a in the plane, labelled by angle theta, has induced line element a^2 d theta^2: proper length is a times the angle.

**How introduced:** First warm-up of Example D.1 by both methods.

**Prerequisites:** method I (parametric embedding), method II (implicit-surface elimination)

$$
\mathrm{d}s^2=a^2\mathrm{d}\theta^2
$$

**Notes:** A 1D space has no intrinsic curvature; the circle's curvature is purely extrinsic, a point worth making even though the book does not.

**Where:** GA p.582 (pdf 599); GA p.583 (pdf 600)

### 2-sphere metric

*solution-or-model · developed* · also: unit sphere line element, round metric on S^2

The unit sphere in R^3 carries the induced line element d theta^2 + sin^2 theta d phi^2, equivalently dr^2/(1 - r^2) + r^2 d phi^2 with r = sin theta the distance from the axis.

**How introduced:** Example D.1(b) computes it by method I from spherical parametrization and by method II via cylindrical coordinates.

**Prerequisites:** method I (parametric embedding), method II (implicit-surface elimination), coordinate transformation of a line element

$$
\mathrm{d}s^2=\mathrm{d}\theta^2+\sin^2\theta\,\mathrm{d}\phi^2
$$

$$
\mathrm{d}s^2=\frac{\mathrm{d}r^2}{1-r^2}+r^2\mathrm{d}\phi^2
$$

**Notes:** The r-form is the template for the k = +1 Robertson-Walker spatial metric in GA ch16.

**Where:** GA p.583 (pdf 600)

### 3-sphere metric

*solution-or-model · introduced* · also: S^3 line element, d Omega_3^2

The unit 3-sphere X^2 + Y^2 + Z^2 + W^2 = 1 in R^4 has induced metric dr^2/(1 - r^2) + r^2 d Omega_2^2, or d psi^2 + sin^2 psi d Omega_2^2 with r = sin psi.

**How introduced:** Exercise D.2, solved by method II in Appendix E by analogy with the 2-sphere.

**Prerequisites:** 2-sphere metric, method II (implicit-surface elimination)

$$
\mathrm{d}\Omega_3^2=\mathrm{d}\psi^2+\sin^2\psi\,\mathrm{d}\Omega_2^2
$$

**Notes:** Spatial section of the closed (k = +1) universe in GA ch16.

**Where:** GA p.586 (pdf 603)

### embedding diagram

*technique · core* · also: visualizing a metric by embedding, rubber-sheet-style picture

A picture of a 2D slice of a curved space drawn as a surface in flat 3D space whose induced metric equals the slice's metric; only distances measured along the surface are meaningful, and the extra direction has no physical meaning.

**How introduced:** Introduced as the reverse problem (metric given, shape wanted), illustrated by the Einstein-Rosen bridge; Chapter 5 cites it as one of two ways to picture a metric.

**Prerequisites:** embedding, induced metric, surface-of-revolution ansatz

**Notes:** The book does not say that the wormhole metric is a constant-time equatorial slice of Schwarzschild, nor that the Z direction is unphysical; tutors should add both.

**Where:** GA p.583 (pdf 600); GA p.584 (pdf 601)

### surface-of-revolution ansatz

*technique · developed* · also: cylindrically symmetric trial embedding

For a metric of the form g_uu(u) du^2 + R(u)^2 d phi^2, try X = R cos phi, Y = R sin phi, Z = Z(u); the angular condition then holds automatically and the radial condition becomes (dR/du)^2 + (dZ/du)^2 = g_uu, an ODE for Z that has real solutions only where (dR/du)^2 <= g_uu.

**How introduced:** Used for the wormhole (success), the hyperbolic plane (failure), and the cosh-type hyperbolic metric in Exercise D.4 (partial success).

**Prerequisites:** method I (parametric embedding)

$$
\left(\frac{\mathrm{d}R}{\mathrm{d}u}\right)^2+\left(\frac{\mathrm{d}Z}{\mathrm{d}u}\right)^2=g_{uu}
$$

**Notes:** The general criterion |dR/du| <= sqrt(g_uu) is not stated in the book but unifies all three cases.

**Where:** GA p.584 (pdf 601); GA p.586 (pdf 603)

### Einstein-Rosen bridge

*solution-or-model · developed* · also: wormhole, Schwarzschild wormhole

The geometry of a spatial slice of the maximally extended Schwarzschild solution, with 2D line element r dr^2/(r - r_S) + r^2 d phi^2 for r >= r_S, which joins two asymptotically flat regions through a throat of circumference 2 pi r_S.

**How introduced:** Example D.2 presents the metric with r_S simply called a constant length and embeds it to show a throat between two flat sheets.

**Prerequisites:** embedding diagram, surface-of-revolution ansatz, Schwarzschild radius

$$
\mathrm{d}s^2=\frac{r\,\mathrm{d}r^2}{r-r_{\mathrm S}}+r^2\mathrm{d}\phi^2
$$

**Notes:** Equals the t = const, theta = pi/2 slice of Schwarzschild with r_S = 2GM/c^2. GA ch27 §27.2 shows it is not traversable.

**Where:** GA p.584 (pdf 601)

### Flamm's paraboloid

*solution-or-model · introduced* · also: embedding of the Schwarzschild spatial slice

The surface of revolution Z^2 = 4 r_S (r - r_S) in R^3, whose induced metric is the equatorial spatial Schwarzschild metric; its profile is a parabola lying on its side with vertex at r = r_S.

**How introduced:** Obtained in Example D.2 by integrating 1 + (dZ/dr)^2 = r/(r - r_S); named Flamm's paraboloid only later, in GA Exercise 23.5.

**Prerequisites:** Einstein-Rosen bridge, surface-of-revolution ansatz

$$
Z(r)=\pm\left[4r_{\mathrm S}(r-r_{\mathrm S})\right]^{1/2}
$$

**Notes:** Slope dZ/dr = sqrt(r_S/(r - r_S)) is vertical at the throat and tends to zero far away, but Z itself grows like sqrt(r); the sheets never become literal planes. Gaussian curvature is -r_S/(2 r^3) (own addition).

**Where:** GA p.584 (pdf 601)

### wormhole throat

*definition · introduced* · also: neck of the wormhole, minimal circumference surface

The narrowest part of a wormhole geometry, where the circumferential radius reaches its minimum (r = r_S for the Einstein-Rosen bridge) and the two sheets meet.

**How introduced:** Visible in Figs. D.3 and D.4 as the vertex of the parabola and the neck of the tube.

**Prerequisites:** Einstein-Rosen bridge

$$
r_{\min}=r_{\mathrm S}
$$

**Where:** GA p.584 (pdf 601)

### asymptotic flatness

*definition · mention* · also: asymptotically flat region

A region of a space or spacetime is asymptotically flat if its geometry approaches flat space at large distances from the central structure.

**How introduced:** Margin note naming the far regions of the wormhole sheets.

**Prerequisites:** metric tensor

**Where:** GA p.584 (pdf 601)

### geometry versus topology

*principle · developed* · also: local metric does not fix global shape, topology of spacetime

A metric specifies distances and curvature locally, but the same local geometry can be glued together in different global ways, so connectivity and large-scale shape (topology) are extra information.

**How introduced:** Drawn from the wormhole: the throat could link distant points of one universe (Fig. D.5a) or appear as a handle on one sheet (Fig. D.5b), or join separate universes.

**Prerequisites:** metric tensor, Einstein-Rosen bridge

**Notes:** The sphere versus flat-torus or plane versus cylinder pairs are simpler illustrations a tutor can add.

**Where:** GA p.584 (pdf 601)

### traversable wormhole and negative energy

*phenomenon · mention* · also: wormhole shortcut

A wormhole that travellers could actually pass through, possibly as a shortcut between distant regions; known constructions require matter with negative energy density.

**How introduced:** Speculative shortcut and 'another universe' suggestions in Example D.2, with a margin note comparing the energy requirement to the Alcubierre warp drive of Chapter 5.

**Prerequisites:** Einstein-Rosen bridge, geometry versus topology

**Notes:** The Schwarzschild bridge itself is not traversable (GA ch27 §27.2); the appendix leaves this implicit.

**Where:** GA p.584 (pdf 601)

### hyperbolic plane

*solution-or-model · developed* · also: hyperbolic space (2D), surface of constant negative curvature

The complete 2D space of constant negative Gaussian curvature -1, with line element d chi^2 + sinh^2 chi d phi^2, in which the circumference of a circle of radius chi is 2 pi sinh chi and grows exponentially.

**How introduced:** Example D.3 introduces it as the most important non-embeddable surface; Example D.4(a) realizes it as a two-sheet hyperboloid.

**Prerequisites:** metric tensor, Gaussian curvature

$$
\mathrm{d}s^2=\mathrm{d}\chi^2+\sinh^2\chi\,\mathrm{d}\phi^2
$$

**Notes:** Spatial geometry of the k = -1 open universe (GA ch16 §16.2); the Poincaré disc picture appears in GA Fig. 16.5.

**Where:** GA p.584 (pdf 601); GA p.585 (pdf 602)

### non-embeddability of the hyperbolic plane in R^3

*theorem · developed* · also: Hilbert's theorem (not named in the book)

The complete hyperbolic plane admits no smooth isometric embedding (or even immersion) into Euclidean 3-space, although pieces of it can be embedded and the whole can be embedded in higher-dimensional Euclidean spaces.

**How introduced:** Shown heuristically in Example D.3: the symmetric ansatz requires (dZ/d chi)^2 = -sinh^2 chi; the text then asserts the embedding is impossible.

**Prerequisites:** hyperbolic plane, surface-of-revolution ansatz

$$
\frac{\partial Z}{\partial\chi}=(1-\cosh^2\chi)^{1/2}=(-\sinh^2\chi)^{1/2}
$$

**Notes:** If one ansatz fails, that proves nothing in general. The general result is Hilbert's 1901 theorem: no complete surface of constant negative curvature can be immersed in R^3 with C^2 regularity. The Nash-Kuiper theorem does allow C^1 (non-smooth) isometric embeddings, so 'impossible' means impossible for smooth ones. Nash's theorem (margin note 2) guarantees a smooth embedding in some higher-dimensional R^N.

**Where:** GA p.584 (pdf 601); GA p.585 (pdf 602)

### partial embedding

*technique · introduced* · also: embedding a patch, local embedding

Embedding only a bounded region of a space isometrically when the whole cannot be embedded, e.g. the band 0 <= chi <= arcsinh 1 of the metric d chi^2 + cosh^2 chi d phi^2 in R^3.

**How introduced:** Offered as the first way out after Example D.3 and worked in Exercise D.4.

**Prerequisites:** surface-of-revolution ansatz, non-embeddability of the hyperbolic plane in R^3

$$
\frac{\partial Z}{\partial\chi}=(1-\sinh^2\chi)^{1/2},\quad 0\le\chi\le\sinh^{-1}1
$$

**Where:** GA p.585 (pdf 602); GA p.586 (pdf 603)

### Minding's theorem

*theorem · introduced*

Any two surfaces with the same constant Gaussian curvature are locally isometric: small patches of one can be mapped onto the other preserving all distances.

**How introduced:** Quoted in Exercise D.4 to justify treating the cosh-form metric as representative of hyperbolic geometry.

**Prerequisites:** Gaussian curvature, hyperbolic plane

**Notes:** Local only: d chi^2 + cosh^2 chi d phi^2 with periodic phi is a hyperbolic annulus (a quotient), not globally the hyperbolic plane.

**Where:** GA p.586 (pdf 603)

### Gaussian curvature

*physical-quantity · mention* · also: intrinsic curvature of a surface, constant negative curvature

The intrinsic curvature K of a 2D surface, determined by its metric alone; for ds^2 = d chi^2 + f(chi)^2 d phi^2 it equals -f''/f, giving +1 for sin, 0 for linear f and -1 for sinh or cosh.

**How introduced:** Mentioned only in passing (constant negative curvature in Exercise D.4); relied on implicitly when grouping sphere and hyperbolic examples.

**Prerequisites:** metric tensor

$$
K=-\frac{f''(\chi)}{f(\chi)}\ \text{for}\ \mathrm{d}s^2=\mathrm{d}\chi^2+f^2\mathrm{d}\phi^2
$$

**Notes:** Formula K = -f''/f is supplied here for tutors; the book develops Gaussian curvature in GA ch30.

**Where:** GA p.586 (pdf 603)

### pseudo-Euclidean space

*mathematical-object · developed* · also: flat space with indefinite metric, (2+1)-dimensional Minkowski space

A flat space whose line element has at least one minus sign in Cartesian coordinates, such as dX^2 + dY^2 - dW^2; with one negative direction it is Minkowski space.

**How introduced:** Offered as the more satisfying alternative host after the hyperbolic plane fails in R^3.

**Prerequisites:** Euclidean line element in R^N, Minkowski metric

$$
\mathrm{d}s^2=\mathrm{d}X^2+\mathrm{d}Y^2-\mathrm{d}W^2
$$

**Notes:** Consistent with the book's (-,+,+,+) signature, W plays the role of time.

**Where:** GA p.585 (pdf 602)

### two-sheet hyperboloid

*solution-or-model · developed* · also: hyperboloid of two sheets, hyperboloid model of the hyperbolic plane

The surface X^2 + Y^2 - W^2 = -1 in pseudo-Euclidean 3-space; each sheet (the book draws W >= 1) inherits the positive-definite hyperbolic metric d chi^2 + sinh^2 chi d theta^2.

**How introduced:** Example D.4(a) parametrizes it with sinh and cosh and shows the minus sign on dW^2 cancels the excess that defeated the Euclidean attempt.

**Prerequisites:** pseudo-Euclidean space, hyperbolic plane, method I (parametric embedding)

$$
X=\sinh\chi\cos\theta,\ Y=\sinh\chi\sin\theta,\ W=\cosh\chi
$$

**Notes:** Its upper sheet is the set of unit future timelike vectors (velocity space), which is why the Lorentzian ambient metric induces a Euclidean-signature metric on it.

**Where:** GA p.585 (pdf 602)

### one-sheet hyperboloid

*solution-or-model · introduced* · also: hyperboloid of one sheet, 2D de Sitter space (not named in the book)

The surface X^2 + Y^2 - W^2 = +1 in pseudo-Euclidean 3-space, whose induced metric -d chi^2 + cosh^2 chi d theta^2 is Lorentzian: it is 2D de Sitter spacetime.

**How introduced:** Example D.4(b) computes the metric, rewrites it with cosh chi = r in a sphere-like form, and warns that the surface is not a sphere.

**Prerequisites:** pseudo-Euclidean space, Lorentzian induced metric, coordinate transformation of a line element

$$
\mathrm{d}s^2=-\mathrm{d}\chi^2+\cosh^2\chi\,\mathrm{d}\theta^2
$$

$$
\mathrm{d}s^2=\frac{\mathrm{d}r^2}{1-r^2}+r^2\mathrm{d}\theta^2,\ r\ge1
$$

**Notes:** GA ch18 exercises and ch19 §19.2 build de Sitter spacetime from the 4D analogue; ch49 §49.7 does anti-de Sitter.

**Where:** GA p.585 (pdf 602)

### Lorentzian induced metric

*definition · introduced* · also: signature of an induced metric

If the ambient flat space has an indefinite metric, a surface inside it can inherit a positive-definite metric (every tangent direction spacelike), a Lorentzian one (some tangent directions timelike), or a degenerate one (where a tangent plane touches the light cone).

**How introduced:** Implicit in Example D.4: the two-sheet hyperboloid gets a positive-definite metric while the one-sheet hyperboloid gets -d chi^2 + ...; the sign change is visible in the formulas but not discussed.

**Prerequisites:** pseudo-Euclidean space, induced metric

**Notes:** Name supplied here; the book does not comment on the signature.

**Where:** GA p.585 (pdf 602)

### induced metric in a pseudo-Euclidean ambient space

*technique · introduced* · also: method I with eta

Method I generalized to a flat ambient space with metric eta_{alpha beta}: g_{mu nu} = eta_{alpha beta} (dX^alpha/dx^mu)(dX^beta/dx^nu).

**How introduced:** Pointed to by a margin note in Example D.4 and given as the hint to Exercise D.5.

**Prerequisites:** method I (parametric embedding), Minkowski metric

$$
g_{\mu\nu}=\eta_{\alpha\beta}\frac{\partial X^{\alpha}}{\partial x^{\mu}}\frac{\partial X^{\beta}}{\partial x^{\nu}}
$$

**Where:** GA p.585 (pdf 602); GA p.586 (pdf 603)

### Rindler coordinates as an embedding

*solution-or-model · introduced* · also: Rindler wedge parametrization

The map T = x sinh t, X = x cosh t from coordinates (t, x) into 2D Minkowski space induces the Rindler metric -x^2 dt^2 + dx^2, covering the wedge X > |T|.

**How introduced:** Exercise D.5, using the eta-weighted induced-metric formula; answer given in Appendix E.

**Prerequisites:** induced metric in a pseudo-Euclidean ambient space

$$
\mathrm{d}s^2=-x^2\mathrm{d}t^2+\mathrm{d}x^2
$$

**Notes:** Connects to GA ch5 §5.2, ch26 and ch27 where Rindler space is used as a model horizon.

**Where:** GA p.586 (pdf 603)

### paraboloid induced metric

*solution-or-model · introduced*

The paraboloid Z = (a/2)(X^2 + Y^2) has induced line element (1 + a^2 r^2) dr^2 + r^2 d theta^2 in cylindrical coordinates.

**How introduced:** Exercise D.1 by method II.

**Prerequisites:** method II (implicit-surface elimination)

$$
\mathrm{d}s^2=(1+a^2r^2)\mathrm{d}r^2+r^2\mathrm{d}\theta^2
$$

**Where:** GA p.586 (pdf 603)

### torus induced metric

*solution-or-model · introduced* · also: doughnut metric

A torus with tube radius a and centre-circle radius c, parametrized by X = (c + a cos v) cos u, Y = (c + a cos v) sin u, Z = a sin v, has induced line element (c + a cos v)^2 du^2 + a^2 dv^2.

**How introduced:** Exercise D.3 by method I after parametrizing the implicit surface equation.

**Prerequisites:** method I (parametric embedding)

$$
\mathrm{d}s^2=(c+a\cos v)^2\mathrm{d}u^2+a^2\mathrm{d}v^2
$$

**Notes:** Appendix E prints the second term as a dv^2; it should be a^2 dv^2.

**Where:** GA p.586 (pdf 603)

### Nash embedding theorem

*theorem · mention* · also: Nash embedding theorems

Every Riemannian manifold can be isometrically embedded in a Euclidean space of sufficiently high dimension.

**How introduced:** Margin note on John Nash accompanying the remark about how many extra dimensions an embedding needs.

**Prerequisites:** embedding

**Notes:** Guarantees existence in some R^N but not in D + 1 dimensions; applies to positive-definite metrics, not directly to Lorentzian spacetimes.

**Where:** GA p.581 (pdf 598)

### Minkowski metric

*mathematical-object · mention* · also: eta_{alpha beta}

The flat spacetime metric, in this book diag(-1, +1, +1, +1) in inertial coordinates.

**How introduced:** Assumed; appears as the ambient metric in Exercise D.5 and implicitly in D.26.

$$
\eta_{\alpha\beta}=\mathrm{diag}(-1,1)\ \text{in 2D}
$$

**Where:** GA p.586 (pdf 603)

### Schwarzschild radius

*physical-quantity · mention* · also: r_S

The length r_S = 2GM/c^2 that sets the scale of the Schwarzschild geometry of a mass M.

**How introduced:** Appears in Example D.2 only as an unexplained constant length in the wormhole metric.

$$
r_{\mathrm S}=\frac{2GM}{c^2}
$$

**Notes:** Identification supplied here; the appendix does not make it.

**Where:** GA p.584 (pdf 601)

## Key equations

### (D.1) Euclidean 3-space line element · supporting · GA p.581 (pdf 598)

$$
\mathrm{d}s^2=\mathrm{d}X^2+\mathrm{d}Y^2+\mathrm{d}Z^2
$$

Pythagorean squared distance between neighbouring points in R^3; the ambient metric for 2D embeddings.

**Symbols:** X, Y, Z Cartesian coordinates

### (D.2) Euclidean N-space line element · supporting · GA p.582 (pdf 599)

$$
\mathrm{d}s^2=\sum_{\alpha=1}^{N}(\mathrm{d}X^\alpha)^2
$$

Flat metric in N dimensions; the host for a D-dimensional object.

**Symbols:** X^alpha ambient Cartesian coordinates, N ambient dimension

### (D.3) Chain rule for embedding coordinates · derivation-step · GA p.582 (pdf 599)

$$
X^\alpha+\mathrm{d}X^\alpha=X^\alpha+\frac{\partial X^\alpha}{\partial x^\mu}\mathrm{d}x^\mu
$$

A small step dx^mu within the object moves the ambient point by the Jacobian times the step.

**Symbols:** x^mu object coordinates (mu = 1..D)

### (D.4) Substituting into the flat metric · derivation-step · GA p.582 (pdf 599)

$$
\mathrm{d}s^2=\sum_\alpha(\mathrm{d}X^\alpha)^2=\sum_\alpha\frac{\partial X^\alpha}{\partial x^\mu}\mathrm{d}x^\mu\frac{\partial X^\alpha}{\partial x^\nu}\mathrm{d}x^\nu=g_{\mu\nu}\mathrm{d}x^\mu\mathrm{d}x^\nu
$$

Rewrites ambient distance as a quadratic form in object displacements.

**Symbols:** Summation over mu, nu implied; explicit sum over alpha

### (D.5) Induced metric (method I) · central · GA p.582 (pdf 599)

$$
g_{\mu\nu}=\sum_{\alpha}\frac{\partial X^{\alpha}}{\partial x^{\mu}}\frac{\partial X^{\alpha}}{\partial x^{\nu}}
$$

Metric components on the object are sums of products of the embedding Jacobian; the core formula of the appendix.

**Symbols:** g_{mu nu} induced metric; dX^alpha/dx^mu Jacobian of the embedding

### (D.6) Circle parametrization · supporting · GA p.582 (pdf 599)

$$
X=a\cos\theta,\quad Y=a\sin\theta
$$

Embedding of a circle of radius a in R^2.

**Symbols:** a radius, theta object coordinate

### (D.7) · derivation-step · GA p.582 (pdf 599)

$$
\frac{\partial X}{\partial\theta}=-a\sin\theta,\quad\frac{\partial Y}{\partial\theta}=a\cos\theta
$$

Jacobian of the circle embedding.

### (D.8) · derivation-step · GA p.583 (pdf 600)

$$
g_{\theta\theta}=a^2\sin^2\theta+a^2\cos^2\theta=a^2
$$

Single induced metric component of the circle.

### (D.9) Circle line element · supporting · GA p.583 (pdf 600)

$$
\mathrm{d}s^2=g_{\theta\theta}\,\mathrm{d}\theta\,\mathrm{d}\theta=a^2\mathrm{d}\theta^2
$$

Arc length is radius times angle.

### (D.10) Method II for a planar curve · derivation-step · GA p.583 (pdf 600)

$$
\mathrm{d}s^2=\mathrm{d}X^2+\mathrm{d}Y^2=\mathrm{d}X^2\left[1+\left(\frac{\partial Y}{\partial X}\right)^2\right]
$$

Arc length of a graph Y(X) in the plane.

**Symbols:** The partial derivative is really an ordinary derivative here

### (D.11) · derivation-step · GA p.583 (pdf 600)

$$
\frac{\partial Y}{\partial X}=\frac{-X}{(a^2-X^2)^{1/2}}
$$

Slope of the upper semicircle Y = sqrt(a^2 - X^2).

### (D.12) · derivation-step · GA p.583 (pdf 600)

$$
\mathrm{d}s^2=\mathrm{d}X^2\left(1+\frac{X^2}{a^2-X^2}\right)
$$

Circle metric in the X coordinate; singular at X = +-a where the graph is vertical.

### (D.13) · derivation-step · GA p.583 (pdf 600)

$$
\mathrm{d}s^2=a^2\mathrm{d}\theta^2
$$

Method II agrees with method I after X = a cos theta.

### Unit sphere parametrization · supporting · GA p.583 (pdf 600)

$$
(X,Y,Z)=(\sin\theta\cos\phi,\ \sin\theta\sin\phi,\ \cos\theta)
$$

Method-I embedding of the unit 2-sphere.

**Symbols:** theta polar angle, phi azimuth

### (D.14) · derivation-step · GA p.583 (pdf 600)

$$
g_{\theta\theta}=\left(\frac{\partial X}{\partial\theta}\right)^2+\left(\frac{\partial Y}{\partial\theta}\right)^2+\left(\frac{\partial Z}{\partial\theta}\right)^2=\cos^2\theta\cos^2\phi+\cos^2\theta\sin^2\phi+\sin^2\theta=1
$$

Polar component of the sphere metric.

### (D.15) · derivation-step · GA p.583 (pdf 600)

$$
g_{\phi\phi}=\left(\frac{\partial X}{\partial\phi}\right)^2+\left(\frac{\partial Y}{\partial\phi}\right)^2+\left(\frac{\partial Z}{\partial\phi}\right)^2=\sin^2\theta\sin^2\phi+\sin^2\theta\cos^2\phi=\sin^2\theta
$$

Azimuthal component; circles of latitude shrink toward the poles. The printed first line carries a premature '= sin^2 theta'.

### (D.16) 2-sphere line element · central · GA p.583 (pdf 600)

$$
\mathrm{d}s^2=\mathrm{d}\theta^2+\sin^2\theta\,\mathrm{d}\phi^2
$$

Induced metric of the unit sphere, with g_theta phi = 0.

### (D.17) Sphere after eliminating Z · derivation-step · GA p.583 (pdf 600)

$$
\mathrm{d}s^2=\mathrm{d}X^2+\mathrm{d}Y^2+\frac{(X\,\mathrm{d}X+Y\,\mathrm{d}Y)^2}{1-X^2-Y^2}
$$

Method II: dZ eliminated using Z dZ = -(X dX + Y dY).

### (D.18) Sphere in cylindrical form · central · GA p.583 (pdf 600)

$$
\mathrm{d}s^2=\frac{\mathrm{d}r^2}{1-r^2}+r^2\mathrm{d}\phi^2
$$

Same sphere with r the distance from the axis; matches D.16 via r = sin theta. The book writes X = r cos theta but the result uses phi.

**Symbols:** r cylindrical radius, 0 <= r < 1

### Reconciling substitution · derivation-step · GA p.583 (pdf 600)

$$
r=\sin\theta,\quad \mathrm{d}r^2=\cos^2\theta\,\mathrm{d}\theta^2\ \Rightarrow\ \frac{\mathrm{d}r^2}{1-r^2}=\mathrm{d}\theta^2
$$

Shows D.18 and D.16 are the same geometry.

### (D.19) Einstein-Rosen bridge 2D metric · central · GA p.584 (pdf 601)

$$
\mathrm{d}s^2=\frac{r\,\mathrm{d}r^2}{r-r_{\mathrm S}}+r^2\mathrm{d}\phi^2
$$

Metric to be visualized; equivalently dr^2/(1 - r_S/r) + r^2 d phi^2, the equatorial constant-time Schwarzschild slice.

**Symbols:** r_S constant length (Schwarzschild radius), r >= r_S

### (D.20) Method-I conditions for the wormhole · derivation-step · GA p.584 (pdf 601)

$$
\sum_{i=1}^{3}\left(\frac{\partial X^i}{\partial r}\right)^2=g_{rr}=\frac{r}{r-r_{\mathrm S}},\qquad \sum_{i=1}^{3}\left(\frac{\partial X^i}{\partial \phi}\right)^2=g_{\phi\phi}=r^2
$$

Equations that unknown embedding functions must satisfy; printed with theta instead of phi in the second derivative.

### Surface-of-revolution trial embedding · supporting · GA p.584 (pdf 601)

$$
(X^1,X^2,X^3)=(r\cos\phi,\ r\sin\phi,\ Z(r))
$$

Satisfies the angular condition identically, leaving one ODE.

### (D.21) Profile ODE · derivation-step · GA p.584 (pdf 601)

$$
1+\left(\frac{\mathrm{d}Z}{\mathrm{d}r}\right)^2=\frac{r}{r-r_{\mathrm S}}
$$

Radial condition for the height of the embedded surface.

### Flamm's paraboloid profile · central · GA p.584 (pdf 601)

$$
Z(r)^2=4r_{\mathrm S}(r-r_{\mathrm S}),\quad Z(r)=\pm\left[4r_{\mathrm S}(r-r_{\mathrm S})\right]^{1/2}
$$

Solution of D.21; revolving it gives the wormhole surface with throat at r = r_S and two sheets from the two signs.

### (D.22) Hyperbolic plane metric · central · GA p.584 (pdf 601)

$$
\mathrm{d}s^2=\mathrm{d}\chi^2+\sinh^2\chi\,\mathrm{d}\phi^2
$$

Constant negative curvature (K = -1) surface; circumference grows as sinh chi.

**Symbols:** chi geodesic radial distance

### (D.23) Method-I conditions for hyperbolic space · derivation-step · GA p.584 (pdf 601)

$$
1=\left(\frac{\partial X}{\partial\chi}\right)^2+\left(\frac{\partial Y}{\partial\chi}\right)^2+\left(\frac{\partial Z}{\partial\chi}\right)^2,\qquad \sinh^2\chi=\left(\frac{\partial X}{\partial\phi}\right)^2+\left(\frac{\partial Y}{\partial\phi}\right)^2+\left(\frac{\partial Z}{\partial\phi}\right)^2
$$

Requirements on an embedding in R^3.

### (D.24) · derivation-step · GA p.584 (pdf 601)

$$
X=\sinh\chi\cos\phi,\quad Y=\sinh\chi\sin\phi
$$

Cylindrically symmetric trial.

### (D.25) Embedding obstruction · central · GA p.584 (pdf 601)

$$
\frac{\partial Z}{\partial\chi}=(1-\cosh^2\chi)^{1/2}=(-\sinh^2\chi)^{1/2}
$$

No real solution for chi > 0: the horizontal motion alone already exceeds the allowed length, so the R^3 embedding of this form fails.

### (D.26) Pseudo-Euclidean ambient metric · central · GA p.585 (pdf 602)

$$
\mathrm{d}s^2=\mathrm{d}X^2+\mathrm{d}Y^2-\mathrm{d}W^2
$$

Flat (2+1) space with one negative direction, used to host hyperbolic surfaces.

**Symbols:** W the negative-sign (timelike) coordinate

### Two-sheet hyperboloid · supporting · GA p.585 (pdf 602)

$$
X^2+Y^2-W^2=-1
$$

Surface realizing the hyperbolic plane.

### (D.27) · supporting · GA p.585 (pdf 602)

$$
X=\sinh\chi\cos\theta,\quad Y=\sinh\chi\sin\theta,\quad W=\cosh\chi
$$

Parametrization of the upper sheet.

### (D.28) Hyperbolic metric recovered · central · GA p.585 (pdf 602)

$$
\mathrm{d}s^2=\mathrm{d}X^2+\mathrm{d}Y^2-\mathrm{d}W^2=\mathrm{d}\chi^2+\sinh^2\chi\,\mathrm{d}\theta^2
$$

The minus sign subtracts sinh^2 chi d chi^2, turning cosh^2 chi into 1: the embedding works.

### One-sheet hyperboloid · supporting · GA p.585 (pdf 602)

$$
X^2+Y^2-W^2=1
$$

Second hyperboloid of Example D.4.

### (D.29) · supporting · GA p.585 (pdf 602)

$$
X=\cosh\chi\cos\theta,\quad Y=\cosh\chi\sin\theta,\quad W=\sinh\chi
$$

Parametrization of the one-sheet hyperboloid.

### (D.30) One-sheet hyperboloid metric · central · GA p.585 (pdf 602)

$$
\mathrm{d}s^2=-\mathrm{d}\chi^2+\cosh^2\chi\,\mathrm{d}\theta^2
$$

Lorentzian induced metric (2D de Sitter), chi acting as time.

### (D.31) Sphere-like rewrite · supporting · GA p.585 (pdf 602)

$$
\mathrm{d}s^2=\frac{\mathrm{d}r^2}{1-r^2}+r^2\mathrm{d}\theta^2\quad(\cosh\chi=r,\ r\ge1)
$$

Formally identical to D.18, but with r >= 1 the dr^2 coefficient is negative, so it is not a sphere.

### (D.32) · derivation-step · GA p.585 (pdf 602)

$$
X=r\cos\theta,\quad Y=r\sin\theta,\quad W=(r^2-1)^{1/2}
$$

Direct parametrization yielding D.31.

### (D.33) Paraboloid surface · supporting · GA p.586 (pdf 603)

$$
Z=\frac{a}{2}(X^2+Y^2)
$$

Surface of Exercise D.1.

**Symbols:** a curvature parameter

### (D.34) Paraboloid induced metric · supporting · GA p.586 (pdf 603)

$$
\mathrm{d}s^2=(1+a^2r^2)\mathrm{d}r^2+r^2\mathrm{d}\theta^2
$$

Target result of Exercise D.1.

### 3-sphere induced metric (Exercise D.2 answer) · supporting · GA p.586 (pdf 603)

$$
\mathrm{d}s^2=\frac{\mathrm{d}r^2}{1-r^2}+r^2\mathrm{d}\Omega_2^2=\mathrm{d}\psi^2+\sin^2\psi\,\mathrm{d}\Omega_2^2
$$

Method II for X^2+Y^2+Z^2+W^2=1; the answer is printed in Appendix E.

**Symbols:** dOmega_2^2 = d theta^2 + sin^2 theta d phi^2; r = sin psi

### (D.35) Torus surface · supporting · GA p.586 (pdf 603)

$$
\left[c-(X^2+Y^2)^{1/2}\right]^2+Z^2=a^2
$$

Implicit equation of a torus with tube radius a centred on a circle of radius c.

### Torus induced metric (Exercise D.3 answer, corrected) · supporting · GA p.586 (pdf 603)

$$
\mathrm{d}s^2=(c+a\cos v)^2\mathrm{d}u^2+a^2\mathrm{d}v^2
$$

From X = (c + a cos v) cos u, Y = (c + a cos v) sin u, Z = a sin v; Appendix E prints a dv^2 by mistake.

**Symbols:** u around the symmetry axis, v around the tube

### (D.36) Alternative hyperbolic metric · supporting · GA p.586 (pdf 603)

$$
\mathrm{d}s^2=\mathrm{d}\chi^2+\cosh^2\chi\,\mathrm{d}\phi^2
$$

Also has K = -1; used for a partial embedding.

### (D.37) Partial-embedding slope · supporting · GA p.586 (pdf 603)

$$
\frac{\partial Z}{\partial\chi}=(1-\sinh^2\chi)^{1/2}
$$

Real for sinh chi <= 1, i.e. chi up to arcsinh 1 (about 0.881).

### (D.38) Rindler embedding in Minkowski space · supporting · GA p.586 (pdf 603)

$$
T=x\sinh t,\quad X=x\cosh t
$$

Maps Rindler coordinates into the right wedge of 2D Minkowski space.

### (D.39) Induced metric with an indefinite ambient metric · central · GA p.586 (pdf 603)

$$
g_{\mu\nu}=\eta_{\alpha\beta}\frac{\partial X^\alpha}{\partial x^\mu}\frac{\partial X^\beta}{\partial x^\nu}
$$

Generalization of D.5 to a Minkowski host; for Exercise D.5 it gives -x^2 dt^2 + dx^2.

**Symbols:** eta_{alpha beta} = diag(-1, 1) for (T, X)

## Figures

### Fig. D.1 · geometric-construction · GA p.582 (pdf 599)

`book-sources/gifted-amateur/pages/page-599/img-379.jpeg`

**Caption (paraphrased):** A circle sitting in the flat plane R^2.

**What it shows:** Two perpendicular arrowed axes meet at the lower left; the vertical one carries the label R^2 near its top. A plain unlabelled circle floats in the quadrant, well away from the origin. No radius, angle or coordinate marks are drawn.

**What it teaches:** Sets the scene for Example D.1(a): a 1D object whose points are labelled by one internal coordinate while living in a 2D container.

**Concepts:** embedding, circle metric, embedding coordinates versus object coordinates

**App redesign (interactive-2d, medium priority):** Dual-coordinate circle explorer: the circle with a draggable point labelled both by theta (object coordinate) and by (X, Y) (embedding coordinates), plus a toggle between method I and method II views. — *Interaction:* Learner drags the point and a small step d theta; readouts show dX, dY, their squares, and ds = a d theta. In method II mode only the upper semicircle is highlighted as the graph Y(X) and the factor 1 + (dY/dX)^2 is plotted, visibly blowing up near X = +-a while ds stays finite.

### Fig. D.2 · geometric-construction · GA p.583 (pdf 600)

`book-sources/gifted-amateur/pages/page-600/img-380.jpeg`

**Caption (paraphrased):** The unit 2-sphere placed in R^3.

**What it shows:** Three arrowed axes radiate from a corner in perspective (one vertical labelled R^3, one toward the lower right, one emerging to the right from behind the sphere). A grey-shaded solid ball with a small double white highlight arc sits in the middle; no grid lines or coordinate labels.

**What it teaches:** Provides the picture behind Example D.1(b): a 2D surface described by (theta, phi) inside 3D Cartesian space.

**Concepts:** 2-sphere metric, embedding, method I (parametric embedding)

**App redesign (interactive-3d, high priority):** Sphere with switchable coordinate grids: spherical (theta, phi) and cylindrical (r, phi) projected from the equatorial plane, with a small coordinate cell whose side lengths are annotated. — *Interaction:* Learner drags a coordinate cell over the sphere; side lengths d theta and sin theta d phi update. Switching to cylindrical mode shows the same cell's radial side as dr/sqrt(1 - r^2), growing near the equator; a toggle reveals that Z = +sqrt(1 - r^2) covers only the northern hemisphere, and a slider animates r = sin theta mapping one grid to the other.

### Fig. D.3 · function-plot · GA p.584 (pdf 601)

`book-sources/gifted-amateur/pages/page-601/img-381.jpeg`

**Caption (paraphrased):** The height function Z(r) of the embedded wormhole, both signs of the square root.

**What it shows:** A graph with vertical axis labelled Z(r) and horizontal axis r. A parabola lies on its side, opening to the right, with its vertex on the r axis at a point marked r_S by a dotted tick. The upper branch rises and the lower branch falls symmetrically; nothing is drawn for r < r_S.

**What it teaches:** Shows that the embedding profile exists only for r >= r_S, has a vertical tangent at the throat, and has two mirror branches that become the two sheets.

**Concepts:** Flamm's paraboloid, wormhole throat, Einstein-Rosen bridge

**App redesign (interactive-plot, medium priority):** Linked profile plot: Z(r) beside g_rr(r) = r/(r - r_S) and the slope dZ/dr, with a sweep line tying them together and a button that revolves the profile into 3D. — *Interaction:* Learner moves a vertical cursor in r; readouts show g_rr, dZ/dr and the proper radial length element sqrt(g_rr) dr. Changing r_S rescales the curve. Pressing revolve animates the curve sweeping round the vertical axis to form the surface of Fig. D.4.

### Fig. D.4 · embedding-diagram · GA p.584 (pdf 601)

`book-sources/gifted-amateur/pages/page-601/img-382.jpeg`

**Caption (paraphrased):** The wormhole surface drawn in R^3.

**What it shows:** Hand-sketched perspective drawing of two horizontal gridded square sheets, one above the other, labelled R^3 at upper right. The upper sheet sinks into a funnel whose mouth is outlined by a dotted ring; the funnel narrows into a vertical tube with grid lines running along it, pinches at a waist, and flares out into the lower sheet. Grid lines bend smoothly into the funnel on both sheets.

**What it teaches:** Gives the visual meaning of the Einstein-Rosen metric: two asymptotically flat regions joined by a throat of minimum circumference.

**Concepts:** embedding diagram, Einstein-Rosen bridge, wormhole throat, asymptotic flatness

**App redesign (interactive-3d, high priority):** Live Flamm-paraboloid builder: the surface generated from Z = +-sqrt(4 r_S (r - r_S)) with a draggable ring of constant r and a geodesic ruler along the surface. — *Interaction:* Learner drags the ring: readouts compare circumference 2 pi r with proper radial distance from the throat measured along the surface, showing extra radial distance near the throat. A slider for r_S resizes the throat. A toggle overlays an honest-scale profile versus the book's stylized flat sheets, and a caption badge reminds that the vertical direction is not physical space.

### Fig. D.5 · embedding-diagram · GA p.584 (pdf 601)

`book-sources/gifted-amateur/pages/page-601/img-383.jpeg`

**Caption (paraphrased):** Two topologically equivalent ways the wormhole could connect space: (a) a folded sheet whose two faraway parts are joined by a tube; (b) a single flat sheet with a handle.

**What it shows:** Panel (a): a gridded sheet bent back on itself into a C shape, its upper and lower parts parallel; a hole in the upper part leads into a tube that reaches the lower part inside the fold. Panel (b): a flat gridded sheet with two holes, joined beneath the sheet by a U-shaped gridded tube, like a handle.

**What it teaches:** The same local throat geometry can be glued into space in different global ways, so the metric alone does not decide whether a wormhole is a shortcut within one universe or a bridge between two.

**Concepts:** geometry versus topology, Einstein-Rosen bridge, traversable wormhole and negative energy

**App redesign (animated-3d, high priority):** Topology morph: a continuous animation between the folded-sheet picture and the handle picture, plus a third option of two disconnected sheets, all sharing the identical throat geometry. — *Interaction:* Learner scrubs a morph slider and picks two marked points; the app shows path length through the throat versus along the sheet, updating as the fold separation changes. A switch selects 'one universe' versus 'two universes' gluing while a panel shows the unchanged local metric, emphasising that only topology changed.

### Fig. D.6 · embedding-diagram · GA p.585 (pdf 602)

`book-sources/gifted-amateur/pages/page-602/img-384.jpeg`

**Caption (paraphrased):** One sheet of the two-sheet hyperboloid in pseudo-Euclidean space.

**What it shows:** Axes X (to the right), Y (receding) and W (vertical) meet at an origin. An upward-opening bowl with a dotted elliptical rim is drawn above the X-Y plane; its lowest point lies on the W axis, and a small double-headed arrow labelled 1 marks that height above the plane via a dashed line. Two curved arrows labelled chi run up the bowl's surface from the vertex. The lower sheet is not shown.

**What it teaches:** Visualizes the hyperbolic plane as the surface W = sqrt(1 + X^2 + Y^2), with chi measured along the surface from the vertex, in a space where W carries a minus sign.

**Concepts:** two-sheet hyperboloid, pseudo-Euclidean space, hyperbolic plane

**App redesign (interactive-3d, high priority):** Hyperboloid inside a faint light cone in (X, Y, W) space, linked to a Poincaré-disc projection and a comparison panel of Euclidean versus Minkowski lengths. — *Interaction:* Learner drags a point up the sheet: displayed chi (Minkowski arc length) grows slowly while the Euclidean-looking length in the picture grows faster, and the circle through the point has circumference 2 pi sinh chi. A second panel projects from (0, 0, -1) onto the disc so geodesics become arcs meeting the boundary at right angles, matching GA Fig. 16.5. A toggle adds the one-sheet hyperboloid outside the cone.

### Fig. D.7 · curve-or-surface · GA p.586 (pdf 603)

`book-sources/gifted-amateur/pages/page-603/img-385.jpeg`

**Caption (paraphrased):** A paraboloidal bowl placed in R^3 for Exercise D.1.

**What it shows:** Axes labelled x, y, z with R^3 at top right. A bowl with stippled inner face and plain shaded outer face sits above the origin, cut off by a horizontal elliptical rim; no grid lines or dimension marks.

**What it teaches:** Pictures the surface whose induced metric (1 + a^2 r^2) dr^2 + r^2 d theta^2 the reader must derive by method II.

**Concepts:** paraboloid induced metric, method II (implicit-surface elimination)

**App redesign (interactive-3d, low priority):** Paraboloid with polar coordinate grid and a curvature slider, shown next to the Flamm paraboloid to contrast Z quadratic in r with r quadratic in Z. — *Interaction:* Learner changes a; radial grid spacing on the surface stretches as g_rr = 1 + a^2 r^2 grows, with a live readout of proper distance from the bottom to a chosen ring versus its coordinate r.

### Fig. D.8 · curve-or-surface · GA p.586 (pdf 603)

`book-sources/gifted-amateur/pages/page-603/img-386.jpeg`

**Caption (paraphrased):** A torus placed in R^3 for Exercise D.3.

**What it shows:** Axes labelled x, y, z with R^3 at top right. A thick doughnut with curved meridian lines drawn around its tube and a darker central hole; no parameters marked.

**What it teaches:** Pictures the torus whose induced metric the reader derives by method I after parametrizing with two angles.

**Concepts:** torus induced metric, method I (parametric embedding)

**App redesign (interactive-3d, low priority):** Torus with sliders for c and a, coloured by the metric factor (c + a cos v)^2 and by Gaussian curvature sign. — *Interaction:* Learner adjusts c and a and moves a point around the tube angle v; readouts show g_uu and g_vv and the local curvature (positive outside, negative inside), illustrating that one embedded surface can carry both signs.

## Worked examples

### Example D.1(a) · intro · GA p.582 (pdf 599)

**Problem:** Find the induced line element of a circle of radius a in the plane using both methods.

**Method:** Method I: parametrize by the angle, differentiate, sum squares of derivatives. Method II: treat the upper semicircle as a graph Y(X), write arc length with 1 + (dY/dX)^2, then substitute X = a cos theta.

**Key insight:** Both routes must agree; method II passes through a coordinate (X) that is bad at the ends of the semicircle, but the final geometry is the same.

**Result:** ds^2 = a^2 d\theta^2

**Concepts:** circle metric, method I (parametric embedding), method II (implicit-surface elimination)

### Example D.1(b) · intro · GA p.583 (pdf 600)

**Problem:** Find the induced metric of the unit 2-sphere in R^3 by both methods and show the answers agree.

**Method:** Method I with the spherical parametrization gives g_theta theta, g_phi phi and zero cross term. Method II eliminates Z via the sphere equation, switches to cylindrical coordinates (r, phi), then identifies r = sin theta.

**Key insight:** Different-looking line elements can be the same geometry; the substitution r = sin theta is the bridge, and it previews the Robertson-Walker k = +1 form.

**Result:** ds^2 = d\theta^2 + \sin^2\theta d\phi^2 = dr^2/(1-r^2) + r^2 d\phi^2

**Concepts:** 2-sphere metric, coordinate transformation of a line element

### Example D.2 · standard · GA p.584 (pdf 601)

**Problem:** Visualize the Einstein-Rosen bridge metric r dr^2/(r - r_S) + r^2 d phi^2 by finding a surface in R^3 with that induced metric.

**Method:** Write the method-I conditions, adopt the surface-of-revolution trial (r cos phi, r sin phi, Z(r)) to satisfy the angular one, integrate 1 + Z'^2 = r/(r - r_S), and revolve the profile.

**Key insight:** Symmetry turns an embedding PDE problem into one ODE; the two signs of the square root give two sheets joined at a throat, and the picture shows geometry but not topology.

**Result:** Z^2 = 4 r_S (r - r_S): two asymptotically flat sheets joined by a throat at r = r_S

**Concepts:** Einstein-Rosen bridge, Flamm's paraboloid, surface-of-revolution ansatz, geometry versus topology

### Example D.3 · standard · GA p.584 (pdf 601)

**Problem:** Try to embed the hyperbolic metric d chi^2 + sinh^2 chi d phi^2 in R^3.

**Method:** Use the symmetric trial X = sinh chi cos phi, Y = sinh chi sin phi, deduce Z depends only on chi, then solve the radial condition for dZ/d chi.

**Key insight:** The horizontal part of the trial already contributes cosh^2 chi to the radial length, more than the metric allows, so the vertical slope would have to be imaginary.

**Result:** (dZ/d chi)^2 = -sinh^2 chi: no real embedding of this form

**Concepts:** hyperbolic plane, non-embeddability of the hyperbolic plane in R^3

### Example D.4(a) · standard · GA p.585 (pdf 602)

**Problem:** Show the two-sheet hyperboloid X^2 + Y^2 - W^2 = -1 in pseudo-Euclidean space carries the hyperbolic metric.

**Method:** Parametrize with X = sinh chi cos theta, Y = sinh chi sin theta, W = cosh chi (which satisfies the surface equation), differentiate and substitute into dX^2 + dY^2 - dW^2.

**Key insight:** The single sign flip in the ambient metric subtracts exactly the excess sinh^2 chi d chi^2 that broke the Euclidean attempt.

**Result:** ds^2 = d\chi^2 + \sinh^2\chi d\theta^2

**Concepts:** two-sheet hyperboloid, pseudo-Euclidean space, hyperbolic plane

### Example D.4(b) · challenging · GA p.585 (pdf 602)

**Problem:** Find the induced metric of the one-sheet hyperboloid X^2 + Y^2 - W^2 = 1 and interpret its alternative form.

**Method:** Parametrize with cosh and sinh swapped, obtain -d chi^2 + cosh^2 chi d theta^2, substitute cosh chi = r, and cross-check by the direct choice W = sqrt(r^2 - 1).

**Key insight:** A sphere-like formula is not a sphere: r >= 1 here so r = sin theta is unavailable, and the metric is actually Lorentzian.

**Result:** ds^2 = -d\chi^2 + \cosh^2\chi d\theta^2 = dr^2/(1-r^2) + r^2 d\theta^2 with r >= 1

**Concepts:** one-sheet hyperboloid, Lorentzian induced metric, coordinate transformation of a line element


## Analogies and intuitions

### A blind beetle crawling on a curved branch cannot see that its track bends (Einstein epigraph). → intrinsic description of geometry · useful · GA p.581 (pdf 598)

Frames the whole appendix: an observer inside a space has no outside view, yet the curvature is real and can be uncovered by thought.

**Where it breaks down:** A beetle's path on a branch can be curved extrinsically without intrinsic curvature; the image does not by itself separate the two notions.

**App idea:** Beetle's-eye view: a first-person camera constrained to a surface, with a button that pulls the camera out to reveal the embedding.

### A beetle trapped on the surface of a bowl only has two coordinates with which to measure distances. → embedding coordinates versus object coordinates · strong · GA p.581 (pdf 598)

Motivates distinguishing the 3 ambient coordinates of the bowl from the 2 internal coordinates the beetle would use, which is exactly the split method I formalizes.

**Where it breaks down:** A bowl really does sit in 3D space; spacetime has no known container, so the analogy illustrates the mathematics rather than a physical fact.

**App idea:** Toggle a bowl between 'outside view' (X, Y, Z readouts) and 'beetle view' (only r, theta readouts) while the beetle walks.

### Slicing a surface into concentric circles and recording how far apart neighbouring circles are. → coordinate transformation of a line element · useful · GA p.585 (pdf 602)

Explains why the one-sheet hyperboloid can be written in a sphere-like form: eliminating W leaves a family of circles, and the metric only stores the spacing between them, not the shape of the original surface.

**Where it breaks down:** The slicing picture hides the sign of the radial term, so it can obscure that the metric is Lorentzian.

**App idea:** Stack of rings whose radii and separations are read from a line element; the learner stacks rings for sphere and hyperboloid and sees they cannot be assembled into the same shape.

### The name wormhole, which the authors tie to the narrow hole running down the middle of the embedded surface (the fruit-worm tunnel image is the usual etymology, not spelled out in the book). → Einstein-Rosen bridge · weak · GA p.584 (pdf 601)

A one-line aside giving an everyday reading of the embedding picture: a narrow passage connecting two regions.

**Where it breaks down:** The hole and the vertical direction exist only in the picture; nothing in the physical space corresponds to a tunnel outside it, and the Schwarzschild bridge cannot be traversed.

### Folding a sheet of paper so two distant points lie on top of each other, then punching a tube between them. → geometry versus topology · useful · GA p.584 (pdf 601)

Fig. D.5(a) shows how a throat could shorten the trip between regions far apart along the sheet, and (b) shows the same connectivity redrawn as a handle.

**Where it breaks down:** Folding suggests the ambient space matters; in GR only the intrinsic connectivity counts, and the fold separation is not a physical distance.

**App idea:** Fold-and-punch sandbox: learner folds a gridded sheet, inserts a throat, then unfolds to the handle picture while path lengths are displayed.

### Comparing wormhole construction to the Alcubierre warp drive: both need negative energy. → traversable wormhole and negative energy · weak · GA p.584 (pdf 601)

Signals that the shortcut idea is speculative and tied to exotic matter, linking back to Chapter 5.

**Where it breaks down:** Only a pointer; no energy condition or field-equation argument is given.

### Circumference grows faster than radius allows: the hyperbolic plane has too much room to fit in flat 3D space. → non-embeddability of the hyperbolic plane in R^3 · strong · GA p.584 (pdf 601)

Intuition behind D.25 (implicit in the book): with circumference radius sinh chi, the horizontal spread per unit radial distance is cosh chi > 1, leaving no length budget for the vertical direction.

**Where it breaks down:** Explains failure of the rotationally symmetric ansatz; the full impossibility needs Hilbert's theorem.

**App idea:** Crochet-style ruffle simulator: a disc whose ring circumferences follow 2 pi sinh chi, forced to ruffle when pushed into 3D.


## Misconceptions addressed

### Curved spacetime must actually be bent inside some higher-dimensional flat space. · GA p.581 (pdf 598)

**Correction:** GR describes curvature intrinsically; embedding is a drawing aid with no evidence of physical reality, and adding a container would be surplus structure.

**Why tempting:** Every curved thing we see (bowls, balls, branches) is curved inside 3D space, and rubber-sheet pictures reinforce this.

### If two line elements look different, they describe different spaces. · GA p.583 (pdf 600)

**Correction:** Coordinate changes alter the appearance of a metric; d theta^2 + sin^2 theta d phi^2 and dr^2/(1-r^2) + r^2 d phi^2 are the same sphere via r = sin theta.

**Why tempting:** Learners compare formulas symbol by symbol rather than asking whether a substitution links them.

### If a line element has the same form as the sphere's, the space is a sphere. · GA p.585 (pdf 602)

**Correction:** The one-sheet hyperboloid can be written as dr^2/(1-r^2) + r^2 d theta^2 but with r >= 1, making it Lorentzian and incompatible with r = sin theta; form alone does not fix the geometry, ranges and signs matter.

**Why tempting:** Pattern-matching on a memorized formula feels like recognition.

### A metric tells you the full shape of a space, including how its regions are connected. · GA p.584 (pdf 601)

**Correction:** A metric fixes local distances and curvature only; global topology is extra, so the same wormhole throat could link one universe to itself or join two universes.

**Why tempting:** In everyday Euclidean settings topology is never in question, so it goes unnoticed as separate data.

### The vertical direction and the hole in a wormhole embedding diagram are real places one could move into. · GA p.584 (pdf 601)

**Correction:** Only distances along the surface are meaningful; the third axis is a device to make the induced metric match, and there is no 'outside' or 'inside' of the throat in physical space.

**Why tempting:** The picture is drawn in 3D and looks like a funnel one could fall into, much like rubber-sheet gravity demos.

*Inferred: the book guards against this implicitly.*

### The embedding diagram of the wormhole is a picture of spacetime. · GA p.584 (pdf 601)

**Correction:** It shows a 2D spatial slice (constant time, equatorial plane) of the geometry; time is not represented, even though the text itself calls the result spacetime.

**Why tempting:** The book's own wording says the rotated curve generates a spacetime, and 'wormhole spacetime' is a common phrase.

*Inferred: the book guards against this implicitly.*

### The Einstein-Rosen bridge is a usable shortcut between distant regions. · GA p.584 (pdf 601)

**Correction:** The Schwarzschild bridge pinches off before anything can cross (no timelike or null path connects the two regions, GA ch27 §27.2); traversable wormholes require negative energy, as the margin note hints.

**Why tempting:** The appendix speaks of a potential shortcut and of visiting another universe, and science fiction does the rest.

*Inferred: the book guards against this implicitly.*

### When one embedding ansatz fails, the space is proven impossible to embed, or is not a legitimate geometry. · GA p.584 (pdf 601)

**Correction:** Failure of a symmetric trial is only evidence; the impossibility of embedding the full hyperbolic plane in R^3 is a separate theorem (Hilbert), patches can be embedded (Exercise D.4), and higher-dimensional or pseudo-Euclidean hosts work.

**Why tempting:** The text passes from 'this equation has no real solutions' straight to 'this embedding is indeed impossible'.

*Inferred: the book guards against this implicitly.*

### Any D-dimensional space fits into a flat space with just one extra dimension. · GA p.581 (pdf 598)

**Correction:** The 2-sphere does, but the hyperbolic plane does not fit in R^3; Nash's theorems guarantee embedding only in some sufficiently high dimension.

**Why tempting:** Surfaces in R^3 are the only examples most learners have seen; the book's phrasing about needing one more dimension is also ambiguous.

*Inferred: the book guards against this implicitly.*

### A surface inside Minkowski-like space always inherits a Lorentzian metric. · GA p.585 (pdf 602)

**Correction:** The two-sheet hyperboloid inherits a positive-definite (hyperbolic) metric because all its tangent directions are spacelike; the one-sheet hyperboloid inherits a Lorentzian one.

**Why tempting:** People associate minus signs in the host with time on everything inside it.

*Inferred: the book guards against this implicitly.*

### Arc length on a curve is the change in the Cartesian coordinate you parametrize with. · GA p.583 (pdf 600)

**Correction:** Method II shows ds depends on the slope: near X = +-a on a circle dX is tiny while ds is not, which is why a factor 1 + (dY/dX)^2 appears.

**Why tempting:** Horizontal coordinates look like natural distance measures on a graph.

*Inferred: the book guards against this implicitly.*


## Thought experiments

### Geometer confined to a bowl · GA p.581 (pdf 598)

**Setup:** A beetle (or geometer) lives on a bowl's surface and can measure lengths only with two surface coordinates, never leaving the surface.

**Lesson:** Everything needed to describe the geometry must be expressible in those two coordinates; the third dimension is optional scaffolding.

**App idea:** Measuring game: the learner, restricted to surface readouts, must decide whether a hidden surface is a bowl, a cylinder or a plane.

### Explorer through the wormhole throat · GA p.584 (pdf 601)

**Setup:** A traveller enters the throat of the embedded wormhole, either emerging far away in the same universe (if the path through the throat is shorter than along the sheet) or in a separate universe.

**Lesson:** The local geometry of the throat does not settle which outcome occurs; that depends on topology, and traversability requires exotic negative energy.

**App idea:** Route planner on the folded-sheet wormhole comparing path lengths, with a warning panel on why the Schwarzschild bridge closes before crossing.


## Applications and observations

- **Wormholes as possible shortcuts or links to other universes** (astrophysical-system, GA p.584 (pdf 601)): Speculative interpretation of the embedded Einstein-Rosen geometry: if the route through the throat is shorter than along the sheet, distant regions could be linked; construction would require negative energy. No observational evidence is discussed.
- **Scale of the Schwarzschild throat for a solar-mass object (own estimate)** (numerical-estimate, GA p.584 (pdf 601)): Own estimate, not in the book: plugging a solar mass into r_S = 2GM/c^2 sets the throat size of the Example D.2 geometry. The embedding height reaches Z = 2 r_S at r = 2 r_S and 6 r_S at r = 10 r_S, where the slope has dropped to 1/3. Key numbers: r_S about 2.95 km; throat circumference 2 pi r_S about 18.6 km; dZ/dr = 1/3 at r = 10 r_S
- **Extent of the partial Euclidean embedding in Exercise D.4** (numerical-estimate, GA p.586 (pdf 603)): The cosh-form hyperbolic metric can be embedded as a surface of revolution only while sinh chi <= 1. The decimal value is our evaluation of the book's arcsinh 1. Key numbers: chi_max = arcsinh 1 = ln(1 + sqrt 2) about 0.881; circumference radius grows from 1 to sqrt 2 over this band
- **Hyperbolic and hyperboloid spaces in cosmology** (observation, GA p.585 (pdf 602)): The authors point to Chapter 18 for cosmological use of the hyperboloid spaces: the two-sheet hyperboloid is the spatial geometry of an open (k = -1) universe, and hyperboloids in Minkowski space model de Sitter spacetime.
- **Accelerated observers via Rindler coordinates** (technology, GA p.586 (pdf 603)): Exercise D.5 treats uniformly accelerated observers' coordinates as an embedding of a 2D patch into Minkowski space, recovering the Rindler metric used for horizon physics later in the book. Key numbers: Induced metric -x^2 dt^2 + dx^2

## Historical notes

- **Albert Einstein:** Epigraph attributed to Einstein comparing himself to a beetle that notices the curvature a blind beetle on a branch does not. — Sets the insider-versus-outsider theme of curvature for the appendix. (GA p.581 (pdf 598))
- **John Nash, Sylvia Nasar:** Margin biography of Nash (1928-2015), noted for economics and for embedding theorems showing any Riemannian manifold fits isometrically in some Euclidean space; recommends Nasar's biography over the film of the same name. — Shows embedding is always possible in principle, which bounds how seriously to take failures in low dimensions. (GA p.581 (pdf 598))
- **Ferdinand Minding:** Minding (1806-1885) credited with the theorem that constant-curvature surfaces share the same local geometry. — Justifies using a partially embeddable cosh-form metric as representative of hyperbolic geometry in Exercise D.4. (GA p.586 (pdf 603))
- **Albert Einstein, Nathan Rosen:** The wormhole metric is presented under the name Einstein-Rosen bridge (the book gives no date or history). — Connects the embedding exercise to a named object revisited with Kruskal coordinates in Chapter 27. (GA p.584 (pdf 601))

## Notation and conventions

- **Embedding versus object coordinates:** Capital X^alpha (alpha = 1..N) for ambient Cartesian coordinates, lower-case x^mu (mu = 1..D) for coordinates on the embedded object; D is the object dimension, N the ambient dimension. (GA p.582 (pdf 599))
- **Summation in the induced-metric formula:** An explicit sum sign over alpha is written in D.4 and D.5 because both alpha indices sit upstairs with a Euclidean (Kronecker) ambient metric; mu and nu use the summation convention. — D.39 restores index balance with eta_{alpha beta}, after which the explicit sum is unnecessary. (GA p.582 (pdf 599))
- **Method I and method II:** Book-specific names: method I = induced metric from an explicit parametrization X^alpha(x^mu); method II = eliminate a coordinate using the surface equation, then choose coordinates. (GA p.582 (pdf 599))
- **Pseudo-Euclidean ambient metric:** dX^2 + dY^2 - dW^2, with W the negative direction; consistent with the book-wide (-,+,+,+) signature where the timelike coordinate carries the minus sign. — Exercise D.5 uses eta = diag(-1, 1) for (T, X). (GA p.585 (pdf 602))
- **Metric signature:** Book-wide (-,+,+,+); Euclidean examples use all plus signs; the one-sheet hyperboloid metric -d chi^2 + ... inherits the minus from W. (GA p.585 (pdf 602))
- **Angle labels theta and phi:** Used inconsistently: in Example D.1(b) theta is first the polar angle, then briefly the cylindrical angle (X = r cos theta) while the result uses phi; in D.20 derivatives are taken with respect to theta but the component is g_phi phi; Example D.4 switches the azimuth to theta. — Tutors should fix one symbol for the azimuth (phi) throughout. (GA p.583 (pdf 600))
- **r_S and chi:** r_S is a constant length in the wormhole metric (the Schwarzschild radius, not named as such); chi is the geodesic radial coordinate on hyperbolic surfaces and hyperboloids. (GA p.584 (pdf 601))
- **Partial versus total derivatives:** Partial-derivative symbols are used even for single-variable functions such as Y(X), Z(r) and Z(chi). — Harmless but can confuse beginners about what is held fixed. (GA p.583 (pdf 600))
- **Unit sphere metric shorthand:** Appendix E answer to Exercise D.2 writes d Omega_2^2 = d theta^2 + sin^2 theta d phi^2 and d Omega_3^2 = d psi^2 + sin^2 psi d Omega_2^2. (GA p.586 (pdf 603))

## Margin notes

- *reference* — The appendix's treatment follows Zee's textbook, recommended for more detail. (GA p.581 (pdf 598))
- *biography* — Biography of John Nash: best known for Nobel-recognized economics, but also proved embedding theorems stating every Riemannian manifold fits isometrically into some Euclidean space; Nasar's biography praised and distinguished from the loosely related film. (GA p.581 (pdf 598))
- *clarification* — The far-out flat regions of the wormhole surface are called asymptotically flat. (GA p.584 (pdf 601))
- *backward-pointer* — Making a wormhole, like the Alcubierre warp drive of Chapter 5, would need negative energy. (GA p.584 (pdf 601))
- *forward-pointer* — Embedding just a portion of the hyperbolic surface is worked in Exercise D.4. (GA p.585 (pdf 602))
- *forward-pointer* — Exercise D.5 shows how method I generalizes to an ambient space with a minus sign in its metric. (GA p.585 (pdf 602))

## Exercises

About 5 exercises (pdf pages 603).

**Solutions:** Appendix E answers D.1, D.2, D.3 and D.5 but not D.4. The D.3 answer has typos: its final metric (E.474) has a dv^2 where a^2 dv^2 is correct, and one derivative in E.473 is labelled dY/dy instead of dY/du.

**Skills practiced**
- applying method II to a surface given as a graph and converting to polar coordinates
- generalizing the 2-sphere computation to the 3-sphere in R^4
- parametrizing an implicit surface (torus) and applying method I
- finding the range where a surface-of-revolution embedding has real solutions
- using Minding's theorem to relate different constant-curvature line elements
- computing an induced metric in a Minkowski ambient space with eta
- recognising the Rindler metric as a patch of flat spacetime

- **D.1** (intro): Derive the polar-coordinate induced metric of a paraboloid of revolution by eliminating the height coordinate. — *Cleanest one-line method-II practice; contrasts nicely with Flamm's paraboloid where r, not Z, is quadratic.* Skills: method II, polar substitution X dX + Y dY = r dr
- **D.2** (standard): Find the induced metric on the unit 3-sphere in four-dimensional Euclidean space by method II. — *Produces the spatial geometry of the closed Robertson-Walker universe used in GA ch16; answer in Appendix E.* Skills: method II in higher dimension, recognising d Omega_2, substitution r = sin psi
- **D.3** (standard): Obtain the induced metric of a torus specified by its implicit equation, using method I after choosing two angular parameters. — *Requires inventing the parametrization the problem does not supply; Appendix E's printed answer drops a factor of a on the dv^2 term.* Skills: parametrizing an implicit surface, method I
- **D.4** (standard): Embed part of a surface of constant negative curvature written in cosh form, find where the embedding slope is real, and connect it to hyperbolic geometry through Minding's theorem. — *Turns the failure of Example D.3 into a partial success and introduces the idea that local geometry is shared by all equal-curvature surfaces. No answer in Appendix E.* Skills: surface-of-revolution ansatz, range analysis, local isometry of constant-curvature surfaces
- **D.5** (intro): Compute the metric induced on Rindler coordinates by their hyperbolic embedding in two-dimensional Minkowski space, using the eta-weighted formula. — *Bridges embedding to spacetime physics: shows an apparently curved-looking metric is just flat spacetime in accelerated coordinates.* Skills: method I with eta, hyperbolic identities, recognising Rindler space

## Cross-references

- *backward* → **GA ch5 §5.2-§5.3**: Footnote 10 in §5.2 names embedding a slice as one of two ways to picture a metric and sends readers here; the Alcubierre warp drive (margin note 4) and Rindler spacetime (Exercise D.5) both appear in §5.3.
- *backward* → **GA ch7 §7.1**: Figure 7.2 uses a sphere embedded in R^3 to show why parallelism must be defined intrinsically, the same insider-versus-embedding tension this appendix opens with.
- *backward* → **GA ch11 (opening)**: The chapter's opening paragraph, just before §11.1, says we are stuck inside spacetime and cannot step out to see it embedded, which motivates intrinsic curvature.
- *backward* → **GA ch16 §16.1**: Robertson-Walker spaces are compared with the 2-spaces of this appendix; the r = sin chi and r = sinh chi substitutions are borrowed from here.
- *backward* → **GA ch16 §16.2**: The k = +1 space is embedded as a 3-sphere in R^4 and the k = -1 space as a two-sheet hyperboloid in Minkowski space, generalizing Examples D.1(b) and D.4(a).
- *backward* → **GA ch18 Exercises 18.5-18.8**: Explicitly cited in Example D.4(b); de Sitter universes built as hyperboloids in Minkowski space using the method from Appendix D.
- *backward* → **GA ch19 §19.1**: A margin note realizes a cylinder-shaped spacetime by embedding a cylinder in (2+1)- and (4+1)-dimensional Minkowski space, referring to this appendix.
- *backward* → **GA ch21**: Source of the Schwarzschild metric whose equatorial constant-time slice is the Example D.2 wormhole metric with r_S = 2GM/c^2.
- *backward* → **GA ch23 Exercise 23.5**: Embeds the Schwarzschild slice as Flamm's paraboloid with a hint pointing to this appendix; Appendix E adds that rubber-sheet slices can mislead about gravity.
- *backward* → **GA ch27 §27.2**: Kruskal extension revisits the wormhole and shows the two asymptotic regions cannot be connected by timelike or null paths, correcting any impression that the bridge is a usable shortcut.
- *backward* → **GA ch30 §30.5**: Intrinsic versus extrinsic curvature of embedded surfaces, Gauss's equation, and in Exercise 30.7 an induced metric on a hypersurface.
- *backward* → **GA ch49 §49.2**: The induced metric on a string world sheet is the same pullback construction as eqn D.5.
- *backward* → **GA ch49 §49.7**: De Sitter and anti-de Sitter spacetimes as hyperboloids in flat spaces with one or two timelike directions, eliminated by 'the embedding routine from Appendix D'.
- *backward* → **GA appC**: Appendix C argues for intrinsic manifolds rather than embeddings; this appendix supplies the embedding tools for visualization.
- *external* → **A. Zee, Einstein Gravity in a Nutshell (Princeton, 2013)**: Stated source of the appendix's approach and recommended for further details.
- *external* → **S. Nasar, A Beautiful Mind (biography of John Nash)**: Recommended in the Nash margin note.
- *external* → **J. Nash, isometric embedding theorems (1950s)**: Mentioned as guaranteeing that any Riemannian manifold embeds in some Euclidean space.

## Teaching gems

### Frame embedding as two opposite tasks: shape to metric (induced metric) and metric to shape (embedding diagram), doing the easy direction first. · GA p.581 (pdf 598)

**Why it works:** Learners build confidence computing metrics of familiar shapes before facing the underdetermined inverse problem, and they see the same formula used both ways.

**App idea:** Two-way toggle: 'I have a surface' (pick a shape, get ds^2) versus 'I have a metric' (type ds^2, the app searches for a surface of revolution), sharing one 3D viewport.

### Solve the same object by two independent methods and require the answers to agree, reconciling different-looking results with a coordinate substitution. · GA p.583 (pdf 600)

**Why it works:** Agreement is a self-check, and the reconciliation step (r = sin theta) teaches that metrics are only defined up to coordinate changes.

**App idea:** Side-by-side derivation panes for method I and II with a substitution slider that morphs one line element into the other symbol by symbol.

### Choose the angular embedding functions so the circumference condition is automatic, reducing embedding to a single ODE for the height profile. · GA p.584 (pdf 601)

**Why it works:** Symmetry turns a scary PDE problem into integration, and the same trick handles wormholes, spheres and hyperbolic surfaces.

**App idea:** Profile builder: user specifies R(u) and g_uu; the app integrates dZ/du live, draws the surface of revolution and shades red where no real slope exists.

### Stage a deliberate failure: show the hyperbolic metric needs an imaginary slope before explaining why and how to escape. · GA p.584 (pdf 601)

**Why it works:** A visible contradiction is memorable and motivates both partial embeddings and a change of ambient signature.

**App idea:** Length-budget bar: for each chi, a bar shows the radial length allowed by the metric versus the horizontal length already used by the circumference; the vertical slope is the leftover, which goes negative for sinh-form metrics.

### Rescue a failed embedding by flipping one sign in the host metric, so the hyperbolic plane becomes an ordinary-looking hyperboloid. · GA p.585 (pdf 602)

**Why it works:** Shows students that 'flat space' can have indefinite signature and connects hyperbolic geometry to Minkowski velocity space and cosmology.

**App idea:** Sign switch on the ambient metric: with + the hyperboloid's measured arc lengths mismatch the target metric; with - they match, displayed as a live residual.

### Use two topologically equivalent drawings of the same wormhole to separate local geometry from global topology. · GA p.584 (pdf 601)

**Why it works:** The comparison is visual and immediate, and it inoculates against assuming a metric determines connectivity.

**App idea:** Morphing animation between folded-sheet and handle views with fixed throat metric and a topology selector including disconnected universes.

### Warn explicitly that a sphere-like line element on the one-sheet hyperboloid does not make it a sphere, checking coordinate ranges against the defining equation. · GA p.585 (pdf 602)

**Why it works:** Trains the habit of checking domains and signs, not just formula shapes.

**App idea:** Formula-matching quiz where each candidate surface's r-range and sign of g_rr must be set before the app accepts a match.

### Partial embedding plus Minding's theorem: embed a band of a constant-negative-curvature surface and argue it represents hyperbolic geometry locally. · GA p.586 (pdf 603)

**Why it works:** Gives a tangible 3D object for negative curvature and introduces local isometry without heavy machinery.

**App idea:** Interactive collar surface for d chi^2 + cosh^2 chi d phi^2 that grows until chi = arcsinh 1, with patches that can be dragged onto a Poincaré disc to show local match.


## Gaps and pitfalls

- **The opening says an embedding needs more than one extra dimension, yet the 2-sphere embeds in R^3 with exactly one extra; the intended claim is presumably 'at least one', and in general many more may be needed.** — Confusion about dimension counting and about why the hyperbolic plane fails in R^3. *Suggestion:* State: at least one extra dimension is needed; D + 1 suffices for some spaces (spheres) but not all; Nash guarantees some finite N.
- **Footnote 2 says any Riemannian manifold can be embedded in Euclidean space, while the text later says some surfaces cannot be embedded in Euclidean space.** — Apparent contradiction. *Suggestion:* Qualify both: embedding in R^3 can fail (hyperbolic plane), but higher-dimensional Euclidean embeddings always exist.
- **'This embedding is indeed impossible' follows only from the failure of one rotationally symmetric ansatz; the general impossibility (Hilbert's theorem for the complete hyperbolic plane in R^3) is neither proved nor named.** — Learners may think any failed guess proves impossibility. *Suggestion:* Name Hilbert's theorem, explain the length-budget intuition, and note pieces embed (Exercise D.4, the pseudosphere).
- **The Example D.2 metric is never identified as the constant-time equatorial slice of the Schwarzschild geometry, and r_S is just called a constant length.** — Readers miss the connection to black holes and Flamm's paraboloid (only named in Exercise 23.5). *Suggestion:* Derive it from the Schwarzschild metric with dt = 0 and theta = pi/2, and name Flamm's paraboloid.
- **The text says the revolved profile 'generates the spacetime' and calls the sheets flat spacetime, although the picture is of a 2D spatial slice.** — Reinforces confusion between space and spacetime pictures and the rubber-sheet misconception. *Suggestion:* Say 'spatial slice' explicitly, stress that time is suppressed and that the vertical axis has no physical meaning.
- **The wormhole is described as a potential shortcut or route to another universe without saying that the Schwarzschild bridge is not traversable.** — Learners leave with a science-fiction impression that Chapter 27 later has to undo. *Suggestion:* Add a note that no timelike path crosses the Schwarzschild throat (GA ch27 §27.2) and that traversable wormholes need negative energy.
- **The induced metric of the one-sheet hyperboloid is Lorentzian (2D de Sitter), but the book presents its r-form as 'simply the metric for the 2-sphere' without mentioning signature.** — Learners may think the formal match is real and miss the de Sitter connection used in Chapters 18, 19 and 49. *Suggestion:* Point out r >= 1 makes the dr^2 coefficient negative, and identify the surface as 2D de Sitter spacetime with chi as time.
- **Symbol slips: D.4 cites D.1 rather than D.2; D.15 has a stray '= sin^2 theta' on its first line; D.18's derivation writes X = r cos theta but the result uses phi; D.20 differentiates with respect to theta while the component is g_phi phi.** — Beginners tracking indices lose confidence or copy the errors. *Suggestion:* Use phi consistently for the azimuth and reference the N-dimensional D.2.
- **Method II's square-root elimination (Y = +sqrt(a^2 - X^2), Z = +sqrt(1 - X^2 - Y^2)) covers only one branch, and the coordinate X is singular at the ends; the book does not comment.** — Learners may think method II describes the whole circle or sphere. *Suggestion:* Highlight the branch covered and the coordinate singularity where the graph becomes vertical.
- **Fig. D.4 draws the far regions as literally flat planes and exaggerates the tube length; the true profile keeps rising as sqrt(r) with slope tending to zero.** — Misleading intuition about how quickly the geometry becomes flat. *Suggestion:* Render the exact profile to scale alongside the stylized sketch.
- **Exercise D.4 calls the space 'hyperbolic spacetime' and presents Minding's theorem without stressing it is local; the cosh-form metric with periodic phi is a hyperbolic annulus, not globally the hyperbolic plane.** — Blurs space versus spacetime and local versus global geometry, just after the book emphasised topology. *Suggestion:* Say 'space', and add that equal constant curvature guarantees local, not global, equivalence.
- **Exercise D.3 supplies the torus as an implicit equation but asks for method I, leaving the parametrization to the reader; Appendix E's answer prints a dv^2 instead of a^2 dv^2.** — Stuck students or wrong answers accepted as correct. *Suggestion:* Give the parametrization as a hint and correct the printed answer.
- **Gaussian curvature of the embedded examples is never computed, so the link between embedding shape and intrinsic curvature (positive sphere, negative hyperboloid, both signs on a torus, negative Flamm paraboloid) is left implicit.** — Embedding feels like pure drawing rather than a window on curvature. *Suggestion:* Add K = -f''/f for metrics d chi^2 + f^2 d phi^2 and tabulate K for each example; point to GA ch30.
- **The one-bullet chapter summary omits the induced-metric recipes, the pseudo-Euclidean fix and the topology caveat.** — Revision from the summary alone misses most of the content. *Suggestion:* Use a fuller summary: two methods, reverse problem, failure in R^3, hyperboloids, geometry versus topology.

## Tutor notes

- Open with: 'How do you know a bowl is curved, and how would a beetle that can never leave it find out?' Then ask whether spacetime has a 'bowl' around it; steer to the idea that embeddings are pictures, not physics.
- Teach method I first with the circle: have the learner write X(theta), Y(theta), differentiate, and sum squares before showing the general formula D.5; then generalize to the sphere.
- Check understanding by asking the learner to predict g_theta phi for the sphere before computing it, and to explain why it vanishes (orthogonal coordinate lines).
- When method II gives dr^2/(1 - r^2) + r^2 d phi^2, pause and ask 'is this a different surface?' Let them find r = sin theta themselves; mention this exact form reappears for the closed universe in Chapter 16.
- For the wormhole, first tell the learner it is the Schwarzschild spatial slice at fixed time in the equatorial plane; then set up the surface-of-revolution ansatz and let them solve for Z(r).
- Immediately after the wormhole picture, ask 'what does the vertical direction represent?' Correct answer: nothing physical, only distances along the surface matter. Follow with 'can you travel through it?' and point to Chapter 27 for why not.
- Use Fig. D.5 to separate geometry from topology with a simpler example first: a flat sheet versus a cylinder have the same local metric but different connectivity.
- Before showing D.25, ask the learner to compute how much radial length the horizontal motion alone uses when the circle radius is sinh chi; the length-budget argument makes the failure intuitive.
- When introducing dX^2 + dY^2 - dW^2, connect it to Minkowski space with W as time and the book's (-,+,+,+) signature; ask why the upper hyperboloid sheet is a natural home for hyperbolic geometry (all its tangents are spacelike).
- For the one-sheet hyperboloid, insist on checking the range r >= 1 and the sign of the dr^2 coefficient; reveal it is 2D de Sitter spacetime if the learner is heading toward cosmology.
- Common learner questions: 'Does spacetime really live in higher dimensions?' (no evidence; Kaluza-Klein and string ideas in Chapters 48-49 are separate speculation); 'Why not always embed in more dimensions?' (possible by Nash, but pictures stop being drawable); 'Is Flamm's paraboloid a picture of gravity pulling things down?' (no: it shows only spatial geometry at fixed time, and the Appendix E answer to Exercise 23.5, citing Zee, warns that such slices mislead about the origin of gravitational effects).
- Pace: novices can do Examples D.1 and D.2 in one sitting; hold Examples D.3-D.4 and Exercises D.4-D.5 for learners comfortable with hyperbolic functions and Minkowski signature.

## Verification

**Verdict:** fixed

**Fixes applied**
- Section 'Example D.2' locator moved from pdf 600/printed 583 to pdf 601/printed 584, where the example box begins (only the one-sentence lead-in is on p.583).
- Assumed-background pointers corrected: the Rindler metric is introduced in GA §5.3 (not §5.2); the 'cannot lift ourselves out of spacetime' passage is the Chapter 11 opening, before §11.1.
- Cross-references fixed: the ch5 entry wrongly put Alcubierre and Rindler in §5.2 (both are in §5.3); the ch11 entry pointed to §11.1, but the passage it means is the chapter opening.
- Hyperbolic non-embeddability note made precise: Hilbert's theorem is about C^2 immersions, and Nash-Kuiper C^1 embeddings exist, so the book's 'impossible' should be read as 'impossible for smooth embeddings'.
- Lorentzian induced metric definition now includes the degenerate (null tangent plane) case, not just the two signatures.
- Exercise solutions note checked against Appendix E: the a dv^2 typo in E.474 is confirmed, and a second typo (dY/dy in E.473) was added.

**Residual concerns**
- All locators set 'section' to null because the appendix has no numbered sections. Example-level placement is carried by the section titles instead.
- The ch18 cross-reference cites Exercises 18.5-18.8. Only 18.5 was confirmed to mention Appendix D; the rest of that range was not checked one by one.
- Cross-references to later chapters are marked 'backward' because those chapters come before this appendix in print, even though conceptually they build on it.

**Coverage:** toc_sections: 0, sections: 8, inventory_figures: 8, figures: 8, inventory_examples: 0, worked_examples: 6, concepts: 36, key_equations: 47, locators_checked: 24, locators_wrong: 1, pages_rendered: 4
