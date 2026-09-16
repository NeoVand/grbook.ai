---
type: "concept"
schema_version: 2
id: "cartan-karlhede-algorithm"
title: "Cartan–Karlhede algorithm"
tagline: "Measuring a surface in rounds, until a round brings nothing new"
domain: "curvature"
tier: "frontier"
status: "physics-reviewed"
revision: 7
updated: "2026-09-13"
aliases: ["Karlhede algorithm", "Karlhede classification", "Cartan–Karlhede classification"]
prerequisites: ["equivalence-problem", "orthonormal-frame", "gaussian-curvature", "isometry-group", "petrov-classification"]
leads_to: []
visuals: ["rounds-that-fix-the-walkers-arrow", "curvature-fingerprint-curves", "staircase-of-invariants-and-isotropy"]
---

# Cartan–Karlhede algorithm

*Measuring a surface in rounds, until a round brings nothing new*

`cartan-karlhede-algorithm` · curvature · frontier · physics-reviewed (revision 7)

**Needs:** [[equivalence-problem]] (entry) · [[orthonormal-frame]] (working) · [[gaussian-curvature]] (working) · [[isometry-group]] (working) · [[petrov-classification]] (formal)  
**Related:** [[hawking-ellis-classification]] · [[scalar-invariant]] · [[exact-plane-gravitational-wave]] · [[exact-solution]] · [[homogeneity]] · [[kretschmann-scalar]]  
**Visuals:** ★ [[rounds-that-fix-the-walkers-arrow]] · [[curvature-fingerprint-curves]] · [[staircase-of-invariants-and-isotropy]]

> Two distance rules written for different painted grids can describe the same surface. The Cartan–Karlhede algorithm compares them by measuring in rounds: first how much small loops turn an arrow at each spot, then which way that turn grows fastest, and so on. The rounds stop at the first one that finds neither a direction to line up with nor a new number. Try pairing the spots of two surfaces. If some pairing makes every number from the rounds match, the surfaces are the same near those spots.

## You will be able to

**Entry**
- Explain why a direction found from arrow-test results, unlike a line of a painted grid, is the same for every walker who follows the recipe. `objectives/explain-rounds-fix-directions` ← `checks/two-walkers-line-up-alike`
- Explain when the rounds stop, using a ball as the example. `objectives/explain-when-rounds-stop` ← `checks/ball-stops-after-round-two`

**Working**
- Run the algorithm on a surface of revolution to find the counts, the stopping order and the number of independent symmetries. `objectives/run-rounds-on-a-surface` ← `checks/sphere-and-power-law-counts`, `problems/order-two-data-of-power-law-surfaces`
- Explain why the classification needs the order after the frame is fixed. `objectives/explain-order-after-fixing` ← `checks/frame-fixed-is-not-finished`

**Formal**
- Derive the dimension of the local isometry group from the stopping counts, and state the hypotheses it needs. `objectives/derive-isometry-dimension` ← `problems/isometry-dimension-from-self-equivalence`, `checks/bifurcation-sphere-counts`
- Run the algorithm on highly symmetric spacetimes and read off their symmetry groups. `objectives/classify-standard-spacetimes` ← `problems/flrw-dust-stops-at-first-order`
- Distinguish matching counts and algebraic types from local equivalence. `objectives/distinguish-counts-from-equivalence` ← `checks/same-counts-different-spacetimes`
- Explain why frame components separate spacetimes that every scalar invariant confuses. `objectives/explain-frames-beat-scalars` ← `checks/plane-wave-at-order-zero`

**Research**
- Evaluate claims about how many derivatives the algorithm needs in practice and in the worst case. `objectives/evaluate-cost-claims` ← `checks/seven-derivatives-claim`

## Ways in

### 1. Rounds that line up the walker's arrow · entry · operational

*How can a walker build a description of her surface that no painted grid can change, and know when it is complete?*

**Recap:** A distance rule says how far apart neighbouring spots of a painted grid are. Two distance rules written for different grids can describe the same surface. The arrow test: press a cardboard arrow against a surface and carry it around a loop, a path that ends where it began. Never let the arrow swing left or right, and walk so that the small piece the loop marks off stays on your left. The turn is how far the arrow comes back turned from its starting direction. On a ball, small loops of one size give the same turn at every spot. On an egg, a small loop near the pointed end gives a bigger turn than the same-size loop at the middle. Paint plays no part in the test.

Picture a walker on a smooth egg. She has no paint, only a cardboard arrow. She wants a description of the egg that no painted grid could change.

In round one, she does the arrow test at spot after spot, with small loops of one size. She walks each loop with its small piece on her left, and writes down its turn.

In round two, she compares the turns at spots close around her. She finds the direction in which the turn grows fastest, like the steepest way up a hillside. At spots near the pointed end, but not at the tip, that direction runs along the egg toward the tip. That direction comes from turns, which paint cannot change. So she lines her arrow up with it, and so does any walker who follows the recipe.

In round three, she measures how that growth changes as she moves along her arrow and across it. Each later round measures how the previous round's results change.

A round can bring two kinds of news: a direction to line up with, or a number she could not work out from her earlier numbers. At the first round with no news, she stops. Every number in that round, and in every round after it, can be worked out from earlier ones, so no later round brings news. This recipe is called the Cartan–Karlhede algorithm.

On a ball, every spot gives the same turn, so the turn grows in no direction. Round two finds no direction and no new number, and she stops there.

Now compare two surfaces. If their spots can be paired so that all their numbers match, the surfaces are the same near those spots. If no pairing works, they are different surfaces.

For the curved space and time of gravity, the recipe never needs more than eight rounds near ordinary spots. To use the recipe there, you need calculus and the mathematics of curving in four dimensions.

**Takeaway:** The Cartan–Karlhede algorithm measures a surface in rounds. Each round can find a direction to line up with or a new number, and the rounds stop at the first round that finds neither.

*What this leaves out:* At a few special spots, such as the tips of an egg or the ring around it where the turn is smallest, no direction wins in round two. The recipe is used near ordinary spots, where every nearby spot gives the same amount of news in each round. The eight rounds are for smooth four-dimensional space and time.

*Builds on:* [[equivalence-problem]]<br>*Visuals:* [[rounds-that-fix-the-walkers-arrow]]<br>*See:* `checks/ball-stops-after-round-two`, `checks/two-walkers-line-up-alike`

### 2. Run the rounds on a surface of revolution · working · calculation

*What do the rounds compute on a curved surface, and what do the final counts say about its symmetries?*

The walker in "Rounds that line up the walker's arrow" lined her arrow up with the direction in which the turn grows fastest. Here are her rounds as formulas, for a surface of revolution with metric

$$ds^2 = dr^2 + f(r)^2\,d\phi^2,\qquad f > 0.$$

Its Gaussian curvature, the turn per unit area around a small loop counted positive toward the walker's left, is $K = -f''/f$, a result taken from the equivalence problem.

An orthonormal frame $(e_1, e_2)$ at a point is a pair of perpendicular unit vectors. Any two frames differ by a rotation, possibly combined with a reflection, so the components of a vector depend on the rotation angle. The algorithm removes that freedom using measured quantities. Two counts record progress at each order $q$ of differentiation: $s_q$, the number of continuous parameters of frame freedom left, and $t_q$, the number of functionally independent functions among all components found so far. Her round one is order 0, the curvature itself, and each later round is one more derivative. A direction to line up with lowers $s_q$, and a number she could not work out from earlier ones, meaning one that is not a function of them, raises $t_q$.

*Order 0.* $K$ is one number, the same in every frame, so no rotation is removed and $s_0 = 1$. If $K$ varies, $t_0 = 1$; if $K$ is constant, $t_0 = 0$.

*Order 1.* The gradient has components $(e_1K, e_2K)$, which rotate with the frame. Where $\nabla K \ne 0$, choose $e_1 = \nabla K/|\nabla K|$. The components become $(|\nabla K|, 0)$, and only the reflection $e_2 \to -e_2$ survives, so $s_1 = 0$. On this surface $K$ depends on $r$ alone, so $e_1 = \pm\partial_r$, $e_2 = f^{-1}\partial_\phi$, and the new component $|K'|$ is again a function of $r$: $t_1 = 1$.

*Order 2.* In the fixed frame the Hessian of $K$ has components $H_{11} = K''$, $H_{22} = (f'/f)K'$ and $H_{12} = 0$, as the derivation "Rounds on a surface of revolution" shows. All are functions of $r$, so $t_2 = 1$ and $s_2 = 0$. Neither count changed, so the algorithm stops at $q = 2$, and $p = q - 1 = 1$. That no later order can then bring anything new is taken on trust here. An egg is a surface of revolution, so near its ordinary spots the walker stops at round three.

The output is a set of relations, not a list of numbers. Near points where $K' \ne 0$, $K$ itself can label the points, and the classification is three functions of it:

$$F_1(K) = |\nabla K|^2,\qquad F_2(K) = H_{11},\qquad F_3(K) = H_{22}.$$

Two such surfaces are locally equivalent near points with equal $K$ exactly when all three functions agree near that value of $K$. The second order is not a formality: two surfaces can share $K$ and $F_1$ and still differ in $F_3$.

The final counts also count symmetries. Where the counts are locally constant, the local isometries form a group of dimension

$$d_{\rm iso} = n - t_p + s_p,$$

with $n$ the dimension, taken on trust here and sketched in "The algorithm in four dimensions". For the surface of revolution, $2 - 1 + 0 = 1$: the rotations $\phi \to \phi + c$. The unit sphere has $t_0 = 0$ and $s_0 = 1$; its gradient vanishes, so order 1 changes nothing, $q = 1$, $p = 0$, and $2 - 0 + 1 = 3$, its three independent rotations. If $K$ and $|\nabla K|^2$ are independent, $t_1 = 2$ and $s_1 = 0$. Neither count can move further, so the algorithm stops at $q = 2$ and the surface has no continuous symmetry.

**Takeaway:** On a surface of revolution the gradient of the curvature fixes the frame at first order, the algorithm stops at second order, and the counts give one symmetry.

*What this leaves out:* Riemannian surfaces at points where $K' \ne 0$ and the counts are locally constant; discrete symmetries such as reflections are not counted.

*Continues:* `ways_in/rounds-that-fix-the-walkers-arrow`<br>*Builds on:* [[orthonormal-frame]], [[gaussian-curvature]], [[isometry-group]]<br>*Visuals:* [[curvature-fingerprint-curves]]<br>*See:* `derivations/rounds-on-a-surface-of-revolution`, `key_equations/isometry-dimension`, `checks/sphere-and-power-law-counts`, `checks/frame-fixed-is-not-finished`, `problems/order-two-data-of-power-law-surfaces`

### 3. The algorithm in four dimensions · formal · structure

*What exactly does the algorithm compute for a spacetime, why does it stop, and what do its counts prove?*

The surface of revolution in "Run the rounds on a surface of revolution" stopped at second order with one symmetry. Here is the same procedure for spacetime, with the results that make it a decision method. Set $G = c = 1$.

*Setting.* Let $(M, g)$ be a smooth spacetime of signature $(-,+,+,+)$ and $F$ its bundle of orthonormal frames, acted on by the Lorentz group $O(1,3)$ of dimension 6. The same construction works in any dimension $n$ and signature. The Cartan invariants of order $q$ at a frame $u$ are the hatted components of $R, \nabla R, \dots, \nabla^qR$ in $u$.

*Canonical frames.* At order 0, bring the Weyl and Ricci parts to a normal form fixed by their algebraic types, the Petrov and Segre types. The frames that do so form a subbundle $F_0 \subset F$ whose structure group $H_0$ is the isotropy group of the curvature. Inductively, use $H_{q-1}$ to bring the order-$q$ components to a normal form; this defines $F_q$ and $H_q \subseteq H_{q-1}$. Let $s_q = \dim H_q$, and let $t_q$ be the number of functionally independent functions on $M$ among the canonical components up to order $q$.

*Algorithm.* Compute orders $q = 0, 1, 2, \dots$ and stop at the first $q \ge 1$ with $t_q = t_{q-1}$ and $s_q = s_{q-1}$; put $p = q - 1$. The classification is the list of types, the counts $(t_k, s_k)$, and the canonical components up to order $q$ written as functions of $t_p$ independent ones, $I_1, \dots, I_{t_p}$.

*Hypothesis.* Near the points considered, the types and the counts are constant.

*Stopping theorem.* After a stall at $q = p + 1$, no higher order adds invariants or removes frame freedom. Sketch: on $F_p$, the connection components outside the Lie algebra of $H_p$ are exactly those that move the order-$p$ normal form, so they are fixed linearly by the order-$(p+1)$ canonical components. After the stall, these connection components and the frame derivatives $e_{\hat a}(I_\alpha)$ are functions of the $I_\alpha$. Each order-$(p+2)$ component is a frame derivative of an order-$(p+1)$ component plus connection terms, so it is again a function of the $I_\alpha$, invariant under $H_p$. Induction covers every order. The data up to order $q$ are therefore complete, and Cartan's theorem from the equivalence problem takes this form: two spacetimes are locally equivalent at $(x, \bar x)$ exactly when their types and counts agree, their canonical components up to order $q$ are the same functions of corresponding independent invariants, and those invariants take equal values at $x$ and $\bar x$.

*Symmetry theorem.* The local isometries form a Lie pseudogroup of dimension $n - t_p + s_p$, with orbits of dimension $n - t_p$ and isotropy of dimension $s_p$. Sketch: fix a canonical frame $u$ at $x$. By the equivalence theorem applied to $g$ and itself, a local isometry sends $u$ to a canonical frame $\bar u$ exactly when the independent invariants agree at the two base points, and it is determined by $\bar u$. Those base points form a level set of dimension $n - t_p$, and the canonical frames over each point form a fibre of dimension $s_p$.

*Bounds.* Before the stop, each order raises $t$ or lowers $s$, with $0 \le t \le 4$ and $0 \le s \le 6$. Combining this count with the possible isotropy groups of a nonzero curvature tensor, Karlhede's analysis, taken on trust here, shows that no derivative beyond the seventh is needed. Cartan's frame-bundle count gave order 10.

*Limits.* The theorems are local. Where counts jump, as on the bifurcation sphere of the Kruskal extension, counts read at a single point mislead. Deciding whether two functions coincide, and solving $I_\alpha(x) = \bar I_\alpha(\bar x)$ for the map, is not algorithmic in general. Finally, the method compares frame components, not scalars. A vacuum plane wave has every scalar polynomial invariant equal to zero, yet its Riemann tensor is nonzero, so no frame makes its order-0 components vanish, and the algorithm separates it from Minkowski spacetime at once.

**Takeaway:** Canonical frames reduce the Cartan invariants to finitely many functions; once the counts stall, the data decide local equivalence, and the counts give the dimension of the isometry group.

*What this leaves out:* Smooth metrics near points where the algebraic types and counts are locally constant; local statements only.

*Continues:* `ways_in/run-the-rounds-on-a-surface-of-revolution`<br>*Builds on:* [[orthonormal-frame]], [[isometry-group]], [[petrov-classification]], [[equivalence-problem]]<br>*Visuals:* [[staircase-of-invariants-and-isotropy]]<br>*See:* `key_equations/stopping-rule`, `key_equations/isometry-dimension`, `worked_examples/schwarzschild-through-the-rounds`, `problems/isometry-dimension-from-self-equivalence`, `checks/bifurcation-sphere-counts`, `checks/plane-wave-at-order-zero`

### 4. From order ten to routine classification · research · historical-puzzle

*Why did a correct equivalence theorem take decades to become a working tool, and what is known now about its cost and reach?*

The stopping theorem of "The algorithm in four dimensions" turns Cartan's local equivalence theorem into a finite computation. Getting from the theorem to the tool took decades.

*The cost problem.* Cartan's method bounds the order by the dimension of the frame bundle, 10 for spacetime, with derivatives taken in frames that are not yet fixed. That was out of reach by hand and, for a long time, by machine. Brans adapted the method to general relativity in 1965. Karlhede's 1980 review reorganized it: fix the frame as early as possible with the Petrov and Segre types, carry only the residual isotropy, and stop when the counts stall. His bound was seven derivatives.

*Is the bound sharp?* Familiar examples stop far earlier: spaces of constant curvature at first order, Friedmann–Lemaître–Robertson–Walker models at first order, and the Schwarzschild spacetime at second. Milson and Pelavas showed that the bound is attained: type N null radiation on an anti-de Sitter background needs the seventh derivative. Their examples are curvature homogeneous to second order: in suitable frames the components of $R$, $\nabla R$ and $\nabla^2R$ are constants, although the spacetime is not homogeneous. The first independent invariant appears at the third derivative, the fourth, fifth and sixth add one each, and the seventh is needed to see the stall. Sharper bounds have been proved for some restricted classes.

*Computer classification.* Computer algebra implementations compute canonical frames, counts and functional relations, and are used to recognize a claimed new exact solution as a known one written in other coordinates. The last step, deciding whether two relations are identical, requires recognizing when an expression is zero, which is undecidable for general classes of expressions, so some comparisons still need insight.

*Where scalars fail.* A four-dimensional Lorentzian metric that is not locally characterized by its scalar polynomial invariants must be degenerate Kundt, and the spacetimes whose scalar invariants all vanish form a subclass that includes the pp-waves. For these metrics the Cartan invariants remain a complete local classification, and the Karlhede counts measure how much the scalars miss.

*Homogeneous spaces.* When $t_p = 0$, every canonical component is constant and the symmetry theorem makes the spacetime locally homogeneous, with an isometry group of dimension $4 + s_p$. For Riemannian manifolds Singer proved a strong form of the converse: constancy of the curvature and its covariant derivatives up to a finite order, compared by linear isometries between tangent spaces, already forces local homogeneity. Curvature-homogeneous spaces that are not homogeneous exist, which is why the algorithm cannot stop at order zero.

**Takeaway:** Karlhede's frame fixing turned Cartan's order-ten bound into at most seven derivatives, a bound attained by Kundt examples; computer algebra made classification routine, and frame invariants still work where scalars fail.

*What this leaves out:* Four-dimensional spacetimes, except where the homogeneous case is stated for Riemannian manifolds.

*Continues:* `ways_in/the-algorithm-in-four-dimensions`<br>*See:* `checks/seven-derivatives-claim`, `research_horizon/sharpness-of-the-karlhede-bound`, `research_horizon/classification-by-computer-algebra`, `research_horizon/frame-invariants-where-scalars-fail`, `research_horizon/local-homogeneity-from-finitely-many-derivatives`

## Glossary

| Term | Say | In plain words | Concept |
| --- | --- | --- | --- |
| spot | — | Any place on a surface. A painted grid gives each spot a name, but the spot is there whether or not anyone paints. | — |
| painted grid | — | A set of lines painted on a surface to name its spots. Two people can paint different grids on one surface, and each then writes a different distance rule for it. | — |
| loop | — | A path that ends exactly where it began. | — |
| swing | — | To change which way the arrow points, left or right, while it lies against the surface. The arrow test never lets it swing. | — |
| arrow test | — | Carry a cardboard arrow around a loop, pressed against the surface, never letting it swing, then compare its direction with its starting direction. | [[holonomy]] |
| turn | — | How far an arrow carried around a loop in the arrow test comes back turned from its starting direction. | [[holonomy]] |
| distance rule | — | A statement of how far apart neighbouring spots on a painted grid are, for every part of the grid. | [[metric-tensor]] |
| round | — | One stage of measuring in the Cartan–Karlhede algorithm. Round one records the turn at each spot; each later round measures how the previous round's results change from spot to spot. | — |
| Cartan–Karlhede algorithm | kar-TAHN KARL-hay-deh | A recipe that describes a surface, or space and time, by measurements in rounds. It stops at the first round that finds no direction to line up with and no new number. | [[cartan-karlhede-algorithm]] |

## Key equations

### Stopping rule · working

$$
q = \min\{k \ge 1 : t_k = t_{k-1},\ s_k = s_{k-1}\},\qquad p = q - 1
$$

The algorithm stops at the first order that adds no functionally independent invariant and removes no frame freedom.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $t_k$ | number of functionally independent canonical components up to order $k$ | t sub k |
| $s_k$ | dimension of the isotropy group of the canonical components up to order $k$ | s sub k |
| $q,\ p$ | the stopping order and the order before it | q and p |

**Holds when:** Algebraic types and counts constant near the points considered.  
**Say it:** “Stop at the first order where neither the number of independent invariants nor the leftover frame freedom changes; p is one less.”  
**Justified by:** `stated`

### Dimension of the local isometry group · working

$$
d_{\rm iso} = n - t_p + s_p
$$

The local isometries have orbits of dimension $n - t_p$ and isotropy of dimension $s_p$, so they form a family of dimension $n - t_p + s_p$.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $d_{\rm iso}$ | dimension of the local isometry group | the number of independent symmetries |
| $n$ | dimension of the manifold | n |
| $t_p,\ s_p$ | the counts at the order just before the stop | t sub p and s sub p |

**Holds when:** Smooth metric; types and counts constant near the point; continuous symmetries only.  
**Say it:** “The number of independent symmetries is the dimension, minus the number of independent invariants, plus the leftover frame freedom.”  
**Justified by:** `stated`

### Second-order data on a surface of revolution · working

$$
H_{11} = K'',\qquad H_{22} = \frac{f'}{f}\,K',\qquad H_{12} = 0
$$

In the frame fixed by the gradient of the curvature, the Hessian of $K$ on $dr^2 + f(r)^2d\phi^2$ has these components.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $H_{ab}$ | components of the Hessian $\nabla\nabla K$ in the orthonormal frame $e_1 = \pm\partial_r$, $e_2 = f^{-1}\partial_\phi$, with the sign of $e_1$ chosen to point along $\nabla K$; these components do not depend on that sign | the Hessian components |
| $K$ | Gaussian curvature, $-f''/f$, a function of $r$ | K |
| $f(r)$ | length of the circle of fixed $r$ per unit change of $\phi$ | f of r |

**Holds when:** Riemannian surface with $f > 0$; primes are derivatives with respect to $r$.  
**Say it:** “H one one is K double prime, H two two is f prime over f times K prime, and the mixed component is zero.”  
**Justified by:** `derivations/rounds-on-a-surface-of-revolution`

## Derivations

### Rounds on a surface of revolution · working

**Goal:** Run orders 0, 1 and 2 of the algorithm on $ds^2 = dr^2 + f(r)^2d\phi^2$ where $K' \ne 0$, and find the Hessian components in the canonical frame.

1. The nonzero Christoffel symbols are $\Gamma^r{}_{\phi\phi} = -ff'$ and $\Gamma^\phi{}_{r\phi} = \Gamma^\phi{}_{\phi r} = f'/f$. The vectors $e_1 = \partial_r$ and $e_2 = f^{-1}\partial_\phi$ form an orthonormal frame.
2. Order 0: $K = -f''/f$ is a scalar, unchanged by rotating the frame, so $s_0 = 1$; it varies, so $t_0 = 1$.
3. Order 1: $K$ depends on $r$ alone, so $e_1K = K'$ and $e_2K = 0$. A frame rotated by an angle $\alpha$ has components $K'(\cos\alpha, -\sin\alpha)$, so requiring the second to vanish and the first to be positive fixes $\alpha$; take $K' > 0$, so $e_1 = \partial_r$. Only $e_2 \to -e_2$ remains: $s_1 = 0$, and $|\nabla K| = K'$ gives $t_1 = 1$.
4. The Hessian is $H(X, Y) = X(YK) - (\nabla_XY)K$.
5. Radial lines are geodesics: $\Gamma^r{}_{rr} = \Gamma^\phi{}_{rr} = 0$, so $\nabla_{e_1}e_1 = 0$ and $H_{11} = K''$.
6. $\nabla_{e_2}e_2 = f^{-2}\Gamma^r{}_{\phi\phi}\,\partial_r = -(f'/f)\,\partial_r$, and $e_2(e_2K) = 0$, so $H_{22} = +(f'/f)K'$.
7. $\nabla_{e_1}e_2 = \partial_r(f^{-1})\,\partial_\phi + f^{-1}\Gamma^\phi{}_{r\phi}\,\partial_\phi = (-f'/f^2 + f'/f^2)\,\partial_\phi = 0$, and $e_1(e_2K) = 0$, so $H_{12} = 0$.
8. Every order-2 component is a function of $r$, hence of $K$, and the frame is already fixed: $t_2 = 1$, $s_2 = 0$. The counts stalled, so $q = 2$.

**Result:** $H_{11} = K''$, $H_{22} = (f'/f)K'$, $H_{12} = 0$; the counts are $(1,1)$, $(1,0)$, $(1,0)$, so the algorithm stops at $q = 2$ with $d_{\rm iso} = 2 - 1 + 0 = 1$.

## Worked examples

### Schwarzschild through the rounds · formal

**Problem:** Run the Cartan–Karlhede algorithm on the Schwarzschild exterior, $r > 2M$, with $G = c = 1$, starting from the static orthonormal frame. Find the counts, the stopping order and the dimension of the isometry group, and restore SI units for the size of the order-0 components at the Sun's surface.

1. Order 0: in the static frame the nonzero components, up to symmetries, are $R_{\hat t\hat r\hat t\hat r} = -2M/r^3$, $R_{\hat t\hat\theta\hat t\hat\theta} = R_{\hat t\hat\phi\hat t\hat\phi} = M/r^3$, $R_{\hat r\hat\theta\hat r\hat\theta} = R_{\hat r\hat\phi\hat r\hat\phi} = -M/r^3$ and $R_{\hat\theta\hat\phi\hat\theta\hat\phi} = 2M/r^3$, in the course sign convention. The Ricci tensor vanishes, and the Weyl tensor has Petrov type D.
2. A boost of rapidity $\beta$ in the $\hat t\hat r$ plane leaves $e_{\hat t}\wedge e_{\hat r}$ unchanged and sends $R_{\hat t\hat\theta\hat t\hat\theta}$ to $\cosh^2\beta\,(M/r^3) + \sinh^2\beta\,(-M/r^3) = M/r^3$, with mixed terms proportional to $M/r^3 - M/r^3 = 0$. Rotations in the $\hat\theta\hat\phi$ plane also preserve every component, while a boost in the $\hat t\hat\theta$ plane does not. So $s_0 = 2$, and the components vary with $r$, so $t_0 = 1$.
3. Order 1: the Kretschmann scalar $I = 48M^2/r^6$ has $\nabla_eI = 2R^{abcd}\nabla_eR_{abcd}$, a contraction of $\nabla R$ with $R$. Its gradient $dI = -288M^2r^{-7}\,dr$ has squared norm $(1 - 2M/r)(288M^2/r^7)^2 > 0$: it is spacelike and radial.
4. A nontrivial boost in the $\hat t\hat r$ plane fixes no nonzero vector of that plane, so it cannot fix $dI$, and therefore cannot fix $\nabla R$. Rotations about $e_{\hat r}$ are isometries that fix the point, so they preserve $\nabla^kR$ there for every $k$. So $s_1 = 1$.
5. Staticity and spherical symmetry make every component at every order a function of $r$ alone, so $t_1 = t_2 = 1$, and $s_2 = 1$ by the same rotations. The counts stall at $q = 2$, with $p = 1$.
6. The symmetry theorem gives $d_{\rm iso} = 4 - 1 + 1 = 4$: orbits of dimension 3, the surfaces of constant $r$, and isotropy of dimension 1, the rotations about the radial direction. These are time translation and the three rotations.
7. In SI units the components have size $GM/c^2r^3$. At the Sun's surface, $GM_\odot/c^2 = 1476.6$ m and $r = 6.957\times10^8$ m, so $M/r^3 = 4.39\times10^{-24}\ \mathrm{m^{-2}}$ and $R_{\hat t\hat r\hat t\hat r} = -8.77\times10^{-24}\ \mathrm{m^{-2}}$.

**Answer:** Counts $(t, s) = (1, 2), (1, 1), (1, 1)$; the algorithm stops at $q = 2$; the isometry group has dimension 4. At the Sun's surface the order-0 components are of size $4.39\times10^{-24}\ \mathrm{m^{-2}}$.

**Takeaway:** The gradient of a scalar built from the curvature breaks the boost freedom at first order, and spherical symmetry keeps one rotation, so four symmetries follow from the counts alone.

## Problems

### `order-two-data-of-power-law-surfaces` · working · difficulty 2 · derivation

Take $ds^2 = dr^2 + r^{2a}\,d\phi^2$ for $r > 0$, with $a$ real and $a(a-1) \ne 0$. (a) Find $K$, $F_1 = |\nabla K|^2$, $F_2 = H_{11}$ and $F_3 = H_{22}$ as functions of $r$. (b) Show that $F_2 = \tfrac12\,dF_1/dK$ on every surface of revolution where $K' \ne 0$, so that at second order only $F_3$ can carry new information. (c) Show that the exponents $a$ and $1 - a$ give the same $K$, $F_1$ and $F_2$, and different $F_3$ unless $a = \tfrac12$. What does that say about local equivalence? (d) For $a = 3$ and $a = -2$, find $F_3/K^2$.

**Hints**

1. With $f = r^a$, $f''/f = a(a-1)/r^2$.
2. Use the chain rule: $K'' = \dfrac{dK'}{dK}\,K'$.
3. Check that $a(a-1)$ does not change when $a$ is replaced by $1 - a$, while $f'/f = a/r$ does.

**Answer:** (a) $K = -a(a-1)/r^2$, $F_1 = 4a^2(a-1)^2/r^6$, $F_2 = -6a(a-1)/r^4$, $F_3 = 2a^2(a-1)/r^4$. (b) $K'' = K'\,dK'/dK = \tfrac12\,d(K'^2)/dK$. (c) $K$, $F_1$ and $F_2$ depend on $a$ only through $a(a-1)$, while $F_3$ for $1 - a$ is $-2a(a-1)^2/r^4$; the ratio of the two $F_3$ values at equal $r$, hence equal $K$, is $a/(1-a)$, which is 1 only for $a = \tfrac12$. So the two surfaces are nowhere locally equivalent unless $a = \tfrac12$, when they coincide. (d) $F_3/K^2 = 1$ for $a = 3$ and $-2/3$ for $a = -2$.

**Must contain:** K is minus a times a minus one over r squared; F two is half the derivative of F one with respect to K; Only F three distinguishes the exponents a and one minus a; The two surfaces are not locally equivalent unless a is one half

**Numeric:** F3 over K squared for a = 3 = 1 1 (signed, ±0.01); F3 over K squared for a = -2 = -0.6667 1 (signed, ±0.01)

**Solution**

1. With $f = r^a$: $f'/f = a/r$ and $f''/f = a(a-1)/r^2$, so $K = -a(a-1)/r^2$.
2. $K' = 2a(a-1)/r^3$ and $K'' = -6a(a-1)/r^4$, so $F_1 = K'^2 = 4a^2(a-1)^2/r^6$ and $F_2 = K'' = -6a(a-1)/r^4$.
3. $F_3 = (f'/f)K' = (a/r)\cdot 2a(a-1)/r^3 = 2a^2(a-1)/r^4$.
4. Where $K' \ne 0$, $K$ labels points, and $K'' = \dfrac{dK'}{dr} = \dfrac{dK'}{dK}K' = \tfrac12\dfrac{d(K'^2)}{dK} = \tfrac12\dfrac{dF_1}{dK}$.
5. Replacing $a$ by $1 - a$ gives $(1-a)(-a) = a(a-1)$, so $K$, $F_1$ and $F_2$ are unchanged as functions of $r$, and therefore as functions of $K$.
6. For $1 - a$, $F_3 = 2(1-a)^2(-a)/r^4 = -2a(a-1)^2/r^4$. Dividing, $F_3(a)/F_3(1-a) = a^2(a-1)/[-a(a-1)^2] = a/(1-a)$.
7. A local isometry maps points of equal $K$ to each other and canonical frames to canonical frames, up to $e_2 \to -e_2$, which leaves $H_{22}$ unchanged, so it would preserve $F_3$ as a function of $K$. The ratio is 1 only for $a = \tfrac12$, so otherwise no local equivalence exists anywhere.
8. $a = 3$: $K^2 = 36/r^4$ and $F_3 = 36/r^4$, so $F_3/K^2 = 1$. $a = -2$: $K^2 = 36/r^4$ and $F_3 = 2\cdot4\cdot(-3)/r^4 = -24/r^4$, so $F_3/K^2 = -2/3$.

**Targets:** `frame-fixed-means-done`

### `isometry-dimension-from-self-equivalence` · formal · difficulty 3 · proof

Let $(M, g)$ be smooth, of dimension $n$, with types and counts constant near $x$, stopping at $q = p + 1$. Assume Cartan's theorem in canonical form, applied to $g$ and itself: for canonical frames $u$ at $x$ and $\bar u$ at $\bar x$ near $x$, a local isometry with $x \mapsto \bar x$ and $u \mapsto \bar u$ exists exactly when the independent invariants agree, $I_\alpha(x) = I_\alpha(\bar x)$. Prove that the local isometries near $x$ form a family of dimension $n - t_p + s_p$, with orbits of dimension $n - t_p$ and isotropy of dimension $s_p$.

**Hints**

1. An isometry of a connected neighbourhood is fixed by the image of one frame.
2. Count the admissible image frames.

**Answer:** Fix a canonical frame $u$ at $x$. Local isometries correspond one to one with canonical frames $\bar u$ over the level set $L = \{I_\alpha = I_\alpha(x)\}$. $L$ has dimension $n - t_p$ because the $t_p$ invariants have independent differentials, and each fibre of canonical frames has dimension $s_p$, so the family has dimension $n - t_p + s_p$. The orbit of $x$ is $L$ and the isotropy is the fibre over $x$.

**Must contain:** An isometry is fixed by the image of one frame; Isometries map canonical frames to canonical frames and preserve invariants; Admissible image frames lie over a level set of dimension n minus t p; Each fibre of canonical frames has dimension s p

**Solution**

1. Uniqueness: a local isometry maps geodesics from $x$ to geodesics, so on a connected normal neighbourhood it is determined by $\bar u$, the image of $u$.
2. Necessity: canonical forms are defined by the curvature and its derivatives alone, so an isometry maps canonical frames to canonical frames, and the invariants satisfy $I_\alpha(\bar x) = I_\alpha(x)$. So $\bar u$ lies over $L = \{y : I_\alpha(y) = I_\alpha(x)\}$.
3. Sufficiency: by the assumed theorem every canonical frame $\bar u$ over $L$ near $x$ is the image of $u$ under some local isometry. So local isometries near the identity correspond one to one, smoothly, with canonical frames over $L$.
4. The $t_p$ invariants have linearly independent differentials near $x$, so $L$ is a submanifold of dimension $n - t_p$.
5. Over each point of $L$ the canonical frames form an orbit of $H_p$, of dimension $s_p$. The set of admissible $\bar u$ therefore has dimension $(n - t_p) + s_p$, which is the dimension of the family of local isometries.
6. The base points $\bar x$ reached fill $L$, so the orbit of $x$ has dimension $n - t_p$; the isometries fixing $x$ correspond to the canonical frames over $x$, so the isotropy has dimension $s_p$.

**Targets:** `counts-read-at-a-point`

### `flrw-dust-stops-at-first-order` · formal · difficulty 2 · calculation

A spatially flat Friedmann–Lemaître–Robertson–Walker dust model, with $G = c = 1$, has zero Weyl tensor and $R_{\mu\nu} = 8\pi\rho\,(u_\mu u_\nu + \tfrac12 g_{\mu\nu})$, where $u$ is the comoving four-velocity and $\rho(t) > 0$ decreases. (a) Find $s_0$ and $t_0$. (b) Using isotropy about each comoving worldline and homogeneity of the slices, find $s_1$ and $t_1$. (c) Give $q$, the isometry group dimension, the orbit dimension and the isotropy. (d) What changes for de Sitter spacetime, whose curvature is $R_{\mu\nu\rho\sigma} = (\Lambda/3)(g_{\mu\rho}g_{\nu\sigma} - g_{\mu\sigma}g_{\nu\rho})$?

**Hints**

1. Which Lorentz transformations leave $u_\mu u_\nu$ unchanged?
2. Rotations about a comoving point are isometries that fix it.

**Answer:** (a) $s_0 = 3$, $t_0 = 1$. (b) $s_1 = 3$, $t_1 = 1$. (c) $q = 1$; $d_{\rm iso} = 4 - 1 + 3 = 6$, with orbits the three-dimensional flat slices and isotropy the rotations $SO(3)$. (d) De Sitter has $s_0 = 6$, $t_0 = 0$ and $\nabla R = 0$, so $q = 1$ and $d_{\rm iso} = 4 - 0 + 6 = 10$.

**Must contain:** Rotations about u preserve the dust curvature, so s zero is three; The varying density gives t zero equal to one; Both counts stall at first order; Six symmetries for the dust model, ten for de Sitter

**Numeric:** isometry group dimension for the dust model = 6 1 (magnitude, ±0); isometry group dimension for de Sitter = 10 1 (magnitude, ±0)

**Solution**

1. With zero Weyl tensor, the Riemann tensor is fixed by $R_{\mu\nu}$ and $g_{\mu\nu}$. A Lorentz transformation preserves $R_{\mu\nu}$ exactly when it preserves $u_\mu u_\nu$, that is, when it maps $u$ to $\pm u$. The continuous ones are the rotations of the rest space of $u$, so $s_0 = 3$.
2. The only nonconstant component is proportional to $\rho(t)$, and $d\rho \ne 0$, so $t_0 = 1$.
3. Rotations of the rest space about a comoving point are isometries fixing that point, so they preserve $\nabla R$ there: $s_1 = 3$. Homogeneity of the slices makes every component a function of $t$ alone, so $t_1 = 1$.
4. Both counts stall at order 1, so $q = 1$ and $p = 0$. The symmetry theorem gives $4 - 1 + 3 = 6$: orbits of dimension $4 - 1 = 3$, the slices of constant $t$, and isotropy of dimension 3. These are three translations and three rotations of each flat slice.
5. For de Sitter, every Lorentz transformation preserves $g_{\mu\rho}g_{\nu\sigma} - g_{\mu\sigma}g_{\nu\rho}$, so $s_0 = 6$; the components are the constant $\Lambda/3$, so $t_0 = 0$; $\nabla g = 0$ gives $\nabla R = 0$, so order 1 changes nothing and $q = 1$. Then $4 - 0 + 6 = 10$.

**Targets:** `always-seven-derivatives`

## Teaching arc

1. **Walk the rounds on an egg** (entry). Walk the three rounds on an egg, then ask when a walker on a ball should stop. *Why:* It shows the two kinds of news and the stopping rule before any formula. *Predict:* On a ball, how many rounds of measuring does the walker need before a round brings no news? *Visual:* [[rounds-that-fix-the-walkers-arrow]] *Uses:* `ways_in/rounds-that-fix-the-walkers-arrow`, `checks/ball-stops-after-round-two`
2. **Run the algorithm on surfaces** (working). Compute the counts for the sphere and a power-law surface, then separate two surfaces at second order. *Why:* Learners see the frame fixed by a gradient, the stopping rule, and why the order after fixing matters. *Predict:* Two surfaces agree on the curvature and on its gradient everywhere. Must they be the same surface? *Visual:* [[curvature-fingerprint-curves]] *Uses:* `ways_in/run-the-rounds-on-a-surface-of-revolution`, `derivations/rounds-on-a-surface-of-revolution`, `checks/sphere-and-power-law-counts`, `checks/frame-fixed-is-not-finished`
3. **Classify spacetimes and count symmetries** (formal). State the stopping and symmetry theorems, then run Schwarzschild and the dust universe through them. *Why:* The counts turn into symmetry groups the learner already knows, which checks the theorems. *Visual:* [[staircase-of-invariants-and-isotropy]] *Uses:* `ways_in/the-algorithm-in-four-dimensions`, `worked_examples/schwarzschild-through-the-rounds`, `problems/flrw-dust-stops-at-first-order`, `problems/isometry-dimension-from-self-equivalence`
4. **Mark the limits** (formal). Test the symmetry formula on the bifurcation sphere, then separate a plane wave from flat spacetime at order zero. *Why:* It fixes the constant-count hypothesis and the difference between frame components and scalars. *Uses:* `checks/bifurcation-sphere-counts`, `checks/plane-wave-at-order-zero`, `checks/same-counts-different-spacetimes`
5. **Discuss cost and reach** (research). Trace the bound from ten to seven, its sharpness, and where scalar invariants fail. *Why:* It places the algorithm in current practice without overstating its cost or its reach. *Uses:* `ways_in/from-order-ten-to-routine-classification`, `checks/seven-derivatives-claim`

## Misconceptions

### “You would have to keep measuring how each change changes, forever, so the list is never finished.” · entry · `rounds-never-end`

- **Why it is tempting:** Every round measures changes of the round before, so there always seems to be another round.
- **What is true:** After a round with no news, every number in that round and in every round after it can be worked out from earlier numbers, so no later round brings news. On a ball the rounds stop after round two.
- **Exposed by:** `checks/ball-stops-after-round-two`

### “Lining the arrow up with a direction you found is just painting another grid, so it depends on who does it.” · entry · `found-directions-are-paint`

- **Why it is tempting:** A painted line and a found direction both give the arrow something to line up with.
- **What is true:** A painter can draw lines any way she likes, but the direction in which the turn grows fastest comes from arrow-test results. So every walker who follows the recipe finds the same direction.
- **Exposed by:** `checks/two-walkers-line-up-alike`

### “Once the gradient of the curvature fixes the frame, the classification is complete.” · working · `frame-fixed-means-done`

- **Why it is tempting:** No frame freedom is left, so the next order seems to have nothing to do.
- **What is true:** The frame freedom changed at that order, so the next order is still needed, and its components can separate surfaces that agree so far.
- **Exposed by:** `checks/frame-fixed-is-not-finished`

### “Two spacetimes with the same algebraic types and the same counts at every order are locally equivalent.” · formal · `same-counts-same-spacetime`

- **Why it is tempting:** The counts and types are the most visible output of the algorithm.
- **What is true:** The counts say how many invariants there are, not what they are. The canonical components must be the same functions of the independent invariants.
- **Exposed by:** `checks/same-counts-different-spacetimes`

### “An invariant classification compares scalar invariants, so a curved spacetime whose scalar invariants all vanish cannot be told apart from flat spacetime.” · formal · `invariant-means-scalar`

- **Why it is tempting:** Scalars are the first invariants learners meet, and in Riemannian geometry they suffice.
- **What is true:** Cartan invariants are components in canonical frames, and a nonzero tensor has nonzero components in every frame. So a vacuum plane wave differs from Minkowski spacetime at order zero.
- **Exposed by:** `checks/plane-wave-at-order-zero`

### “The counts, and so the number of symmetries, can be read off at any single point.” · formal · `counts-read-at-a-point`

- **Why it is tempting:** Ranks and isotropy groups are defined point by point.
- **What is true:** The theorems need counts that are constant near the point. Where counts jump, as on a black hole's bifurcation sphere, the symmetry formula fails.
- **Exposed by:** `checks/bifurcation-sphere-counts`

### “The algorithm always needs the seventh covariant derivative of the curvature, so it is impractical.” · research · `always-seven-derivatives`

- **Why it is tempting:** Seven is the most quoted number about the algorithm.
- **What is true:** Seven is the worst case in four dimensions. The algorithm stops at the first stall, after one derivative for constant curvature and two for Schwarzschild.
- **Exposed by:** `checks/seven-derivatives-claim`

## Checks

1. **Entry · predict** `checks/ball-stops-after-round-two`. A walker on a smooth ball follows the rounds of the Cartan–Karlhede algorithm. In round one, every small loop of one size turns her cardboard arrow by the same amount. What does round two find? Does she go on to a round three?
   - **Hints:** If the turn is the same at every spot, in which direction does it grow?
   - **Answer:** Round two finds no news, so she stops without a round three. The turn is the same at every spot, which means it grows in no direction. Round two therefore gives her no direction to line up with. The growth is zero everywhere, and she could work that out from round one, because equal turns everywhere mean no growth. So round two brings no new number either. A round with no news ends the recipe, because every later round would only measure how those same zero results change.
   - **Must contain:** Round two finds no direction and no new number; Equal turns everywhere mean no growth; A round with no news ends the recipe
   - **Targets:** `rounds-never-end`
   - **Visual:** [[rounds-that-fix-the-walkers-arrow]]
2. **Entry · explain** `checks/two-walkers-line-up-alike`. Two walkers visit the same spot on a smooth egg at different times, without paint. The spot is near the pointed end, but not at the tip. Each does round two there: she finds the direction in which the turn grows fastest, and lines up her cardboard arrow with it. Both walk their loops with the small piece on their left, as the recipe says. Do their arrows point the same way? Could you be sure of that if each had instead lined up her arrow with a line of her own painted grid?
   - **Hints:** Does anything in the arrow test depend on who does it?
   - **Answer:** Yes, their arrows point the same way. The turns come from the arrow test, which uses no paint. Both walkers walk their loops the same way round, so both find the same turns around that spot. The direction in which the turn grows fastest depends only on those turns, so both find the same direction, along the egg toward the tip. With painted grids you could not be sure. Each walker could paint her lines at any angle she liked, so their arrows could point different ways.
   - **Must contain:** Yes, the arrows agree; The direction comes from arrow-test results, which use no paint; Painted lines can point any way the painter chooses
   - **Targets:** `found-directions-are-paint`
   - **Visual:** [[rounds-that-fix-the-walkers-arrow]]
3. **Working · numeric** `checks/sphere-and-power-law-counts`. Run the algorithm on (a) the unit sphere, $ds^2 = d\theta^2 + \sin^2\theta\,d\phi^2$, and (b) $ds^2 = dr^2 + r^4\,d\phi^2$ for $r > 0$. For each, give the counts at each order computed, the stopping order $q$, and the dimension of the local isometry group.
   - **Hints:** Use $K = -f''/f$ with $f = \sin\theta$ or $f = r^2$.
   - **Answer:** (a) $K = 1$, so $t_0 = 0$ and $s_0 = 1$. The gradient of $K$ vanishes, so order 1 fixes nothing: $t_1 = 0$, $s_1 = 1$. The counts stall at $q = 1$, and $d_{\rm iso} = 2 - 0 + 1 = 3$. (b) $f = r^2$ gives $K = -2/r^2$, which varies: $t_0 = 1$, $s_0 = 1$. The gradient $K' = 4/r^3$ is nonzero and fixes the frame, so $s_1 = 0$, and $|\nabla K| = 4/r^3$ is a function of $r$, so $t_1 = 1$. The order-2 components are also functions of $r$, so $t_2 = 1$ and $s_2 = 0$. The counts stall at $q = 2$, and $d_{\rm iso} = 2 - 1 + 0 = 1$.
   - **Must contain:** Sphere: q is one, three symmetries; Power-law surface: q is two, one symmetry
   - **Numeric:** stopping order for the sphere = 1 1 (magnitude, ±0); isometry group dimension for the sphere = 3 1 (magnitude, ±0); stopping order for the r to the fourth surface = 2 1 (magnitude, ±0); isometry group dimension for the r to the fourth surface = 1 1 (magnitude, ±0)
4. **Working · evaluate-claim** `checks/frame-fixed-is-not-finished`. Claim: "The surfaces $ds^2 = dr^2 + r^4\,d\phi^2$ and $ds^2 = dr^2 + r^{-2}\,d\phi^2$, $r > 0$, both have $K = -2/r^2$ and $|\nabla K|^2 = -2K^3$, and the gradient fixes the frame at first order. So the classification is complete and the surfaces are locally equivalent." Evaluate the claim by computing $H_{22}$ in the canonical frame of each.
   - **Hints:** Did either count change at first order? / Use $H_{22} = (f'/f)K'$ with $f = r^2$ and $f = 1/r$.
   - **Answer:** The claim is false. The frame freedom changed at first order, from $s_0 = 1$ to $s_1 = 0$, so the algorithm must compute second order. There $H_{22} = (f'/f)K'$ with $K' = 4/r^3$. For $f = r^2$, $H_{22} = (2/r)(4/r^3) = 8/r^4 = 2K^2$. For $f = 1/r$, $H_{22} = (-1/r)(4/r^3) = -4/r^4 = -K^2$. A local isometry maps points of equal $K$ to each other and canonical frames to canonical frames, up to $e_2 \to -e_2$, which leaves $H_{22}$ unchanged. So it would preserve $H_{22}$ as a function of $K$. The two functions differ at every $K$, so the surfaces are nowhere locally equivalent, although both have $H_{11} = -3K^2$.
   - **Must contain:** A count changed at first order, so second order is required; H two two is two K squared for one surface and minus K squared for the other; So the surfaces are not locally equivalent
   - **Numeric:** H22 over K squared for r to the fourth = 2 1 (signed, ±0.01); H22 over K squared for r to the minus two = -1 1 (signed, ±0.01)
   - **Targets:** `frame-fixed-means-done`
   - **Visual:** [[curvature-fingerprint-curves]]
5. **Formal · evaluate-claim** `checks/same-counts-different-spacetimes`. Claim: "Two spacetimes whose algebraic types agree at every order and whose counts $(t_k, s_k)$ agree are locally equivalent." Test it on de Sitter spacetimes with $\Lambda_1 \ne \Lambda_2$, both positive, and on Schwarzschild spacetimes with $M_1 \ne M_2$, using the Kretschmann scalar $I = 48M^2/r^6$ as the independent invariant.
   - **Hints:** Write $|\nabla I|^2$ as a function of $I$ and $M$.
   - **Answer:** The claim is false. Both de Sitter spacetimes have $s_0 = 6$, $t_0 = 0$ and stop at $q = 1$, yet their canonical order-0 components are the constants $\Lambda_1/3$ and $\Lambda_2/3$, which must be equal for an equivalence. Both Schwarzschild spacetimes have counts $(1,2), (1,1), (1,1)$. At order 0, $M/r^3 = \sqrt{I/48}$ is the same function for every mass, so order 0 cannot separate them. At order 1, $|\nabla I|^2 = (1 - 2M/r)(288M^2/r^7)^2$. Eliminating $r = (48M^2/I)^{1/6}$ gives $2M/r = 2M^{2/3}(I/48)^{1/6}$ and $M^4r^{-14} = M^{-2/3}(I/48)^{7/3}$, so the relation between $|\nabla I|^2$ and $I$ depends on $M$. The canonical components are different functions of the independent invariant, so the spacetimes are not locally equivalent.
   - **Must contain:** Counts and types do not give the invariants' values; De Sitter spacetimes differ in their constant curvature; For Schwarzschild the gradient relation contains the mass
   - **Targets:** `same-counts-same-spacetime`
6. **Formal · explain** `checks/plane-wave-at-order-zero`. The vacuum plane wave $ds^2 = -2\,du\,dv + (x^2 - y^2)\,a(u)\,du^2 + dx^2 + dy^2$ has $R_{uxux} = -a(u)$, and every scalar polynomial curvature invariant vanishes, as in Minkowski spacetime. At which order does the Cartan–Karlhede algorithm separate the two where $a \ne 0$, and why do frame components succeed where scalars fail?
   - **Hints:** Can a change of frame turn a nonzero tensor into the zero tensor?
   - **Answer:** At order 0. Frame changes act on components by invertible linear maps, so a nonzero tensor has at least one nonzero component in every frame, while Minkowski curvature components vanish in every frame. So no canonical form of one matches the other. Scalars fail because the curvature is null: boosts along the wave's direction of propagation multiply every component by a factor that can be made as small as desired. A polynomial invariant is constant along that family and continuous, so it equals its value at zero curvature. Cartan invariants keep track of the frame and compare normal forms, not limits of orbits.
   - **Must contain:** Separated at order zero; A nonzero tensor has a nonzero component in every frame; Boosts shrink null curvature toward zero, so continuous scalar invariants vanish
   - **Targets:** `invariant-means-scalar`
7. **Formal · explain** `checks/bifurcation-sphere-counts`. In the Kruskal extension of the Schwarzschild spacetime, the bifurcation sphere $U = V = 0$ has $r = 2M$ and $dr = 0$. At one of its points, count independent invariants by the rank of their differentials there, and apply $n - t_p + s_p$ with the isotropy dimension 2 found there. Compare with the true orbit and isotropy, and name the failed hypothesis.
   - **Hints:** What are the counts at points just off the sphere?
   - **Answer:** Every invariant is a function of $r$, and $dI = I'(r)\,dr = 0$ there, so the rank at the point is 0. With isotropy 2, the formula gives $4 - 0 + 2 = 6$, and an orbit of dimension 4. The true isometry group has dimension 4. The static Killing field vanishes on the bifurcation sphere and generates a boost there, and rotations about the point add one more, so the isotropy is 2; the orbit through the point is the bifurcation sphere itself, of dimension 2, and $2 + 2 = 4$. The failed hypothesis is that the counts are constant near the point: at nearby points $t = 1$ and $s = 1$, where the formula correctly gives $4 - 1 + 1 = 4$.
   - **Must contain:** Every invariant has zero differential at the point; The pointwise count gives six, the true dimension is four; The counts are not constant near the point
   - **Numeric:** true isometry group dimension = 4 1 (magnitude, ±0); orbit dimension through a point of the bifurcation sphere = 2 1 (magnitude, ±0)
   - **Targets:** `counts-read-at-a-point`
8. **Research · evaluate-claim** `checks/seven-derivatives-claim`. Claim: "The Karlhede algorithm must compute the seventh covariant derivative of the curvature for every spacetime, so it is too expensive to use." Evaluate the claim.
   - **Hints:** At which order does the Schwarzschild classification stop?
   - **Answer:** The claim is wrong on both counts. Seven is the worst-case bound in four dimensions, and it is attained, by type N null radiation on an anti-de Sitter background. The algorithm stops at the first order where the counts stall: spaces of constant curvature and Friedmann–Lemaître–Robertson–Walker models at first order, the Schwarzschild spacetime at second. Classifications of known exact solutions usually stop after a few derivatives, and computer algebra performs them routinely. The hard step is often the final comparison of functional relations, not the number of derivatives.
   - **Must contain:** Seven is a sharp worst-case bound, not a requirement; Common spacetimes stop at first or second order; The final comparison of relations can be the harder step
   - **Targets:** `always-seven-derivatives`
   - **Visual:** [[staircase-of-invariants-and-isotropy]]

## Notation traps

| Issue | Course choice | Variants you will meet |
| --- | --- | --- |
| Which frames and components the canonical forms use | Orthonormal-frame components with hats, in signature $(-,+,+,+)$, with the course Riemann tensor, for which a sphere of radius $a$ has $R = +2/a^2$. | Most classification tables use null tetrads, spinor components of the Weyl and Ricci tensors, or signature $(+,-,-,-)$; the course has not yet fixed conventions for null tetrads or spinors. Translate a published canonical form into hatted orthonormal components, and check the overall sign of the Riemann tensor, before comparing it with a course computation. |

## Visuals

- ★ [[rounds-that-fix-the-walkers-arrow]] (flagship): Entry picture: rounds of measurement on an egg and a ball, with tallies of the two kinds of news and a stop lamp. *Sketch:* A walker on a smooth egg, switchable to a ball or a flat floor. Round one tints the surface by the turn of small loops of one size. Round two draws a short arrow along the way the turn grows fastest wherever one direction wins, and marks the tips and the ring of smallest turn, where none does. Round three shows how that growth changes along and across the arrow. Two tallies count directions to line up with and numbers that cannot be worked out from earlier ones; a stop lamp lights at the first round that adds to neither. On the ball the lamp lights at round two. A second walker, placed anywhere, lines up the same way, while a painted-grid toggle shows arbitrary line directions.
- [[curvature-fingerprint-curves]] (core): Shows that the classification is a set of relations: surfaces can share $K$ and $|\nabla K|^2$ against $K$, and separate in the second-order component $H_{22}$. *Sketch:* Left: a surface of revolution $dr^2 + f(r)^2d\phi^2$ chosen from presets ($\sin r$, $\sinh r$, $e^r$, $r^2$, $1/r$, $r^3$, $r^{-2}$). Right: three stacked plots against $K$ of $|\nabla K|^2$, $H_{11}$ and $H_{22}$ in the canonical frame. The pairs $r^2$, $1/r$ and $r^3$, $r^{-2}$ overlap in the first two plots and split in the third; constant-curvature presets collapse to points. A marker dragged along the surface moves along all three curves.
- [[staircase-of-invariants-and-isotropy]] (core): The counts of the algorithm as two staircases, with the stopping order and the symmetry dimension read off. *Sketch:* For a chosen spacetime (Minkowski, de Sitter, flat dust universe, Schwarzschild exterior, a surface of revolution, a surface without symmetry) plot $t_q$ rising and $s_q$ falling against the order $q$. A stop marker sits at the first order where both steps are flat. Readouts give $q$, the orbit dimension $n - t_p$, the isotropy dimension $s_p$ and $d_{\rm iso}$. A Schwarzschild toggle to the bifurcation sphere shows the pointwise counts jumping and the formula failing there. A band marks the four-dimensional bound of seven derivatives.

## Tutor moves

**Open with**

- Picture a walker on a smooth ball. She measures how much small loops turn her arrow at spot after spot, then which way that turn grows fastest, and so on. How many rounds will she need before a round tells her nothing new? *(prediction)*
- Suppose you live on a surface you can never see from outside, and you have no paint. What would you measure first, to describe it in a way nobody's painted grid could change? *(reflection)*

**If the learner is stuck**

- *The learner cannot tell what counts as news in a round.* → Keep two tallies per round, directions to line up with and new numbers, and replay the ball before the egg. *Uses:* `ways_in/rounds-that-fix-the-walkers-arrow`, `checks/ball-stops-after-round-two`
- *The learner stops the algorithm as soon as the frame is fixed.* → Ask whether a count changed at that order, then compute $H_{22}$ for $r^2$ and $1/r$. *Uses:* `checks/frame-fixed-is-not-finished`

**Common questions**

- *Why not just search for a repainting that turns one distance rule into the other?* (entry) You can try, but a repainting has to match one distance rule to the other at every spot. You have more conditions to meet than choices to make, so guesses usually fail. A failed guess proves nothing either, because some repainting you have not tried might still work. The rounds instead give numbers you can compare directly, and they tell you when you have measured enough. *Uses:* `ways_in/rounds-that-fix-the-walkers-arrow`, `equivalence-problem/checks/count-the-equations`
- *What is this used for in real physics?* (entry) Physicists who find new possible shapes of space and time, allowed by Einstein's theory of gravity, run this recipe on computers. It checks whether a shape is really new, or a known one described with a different grid. The rounds also reveal how many independent ways a space can be rotated or slid without changing it. A ball, for example, can be rotated about three different lines through its centre. Every other rotation of the ball can be built from those three. *Uses:* `ways_in/from-order-ten-to-routine-classification`

**Switching levels**

- To working when: asks what a round computes. Run the rounds on a surface of revolution, then the power-law pair. *Uses:* `ways_in/run-the-rounds-on-a-surface-of-revolution`, `checks/frame-fixed-is-not-finished`
- To formal when: asks why the algorithm stops or why counts give symmetries. State the stopping and symmetry theorems and work Schwarzschild. *Uses:* `ways_in/the-algorithm-in-four-dimensions`, `worked_examples/schwarzschild-through-the-rounds`
- To research when: asks about bounds, computer classification, or where scalar invariants fail. Open the history of the bound and the degenerate Kundt class. *Uses:* `ways_in/from-order-ten-to-routine-classification`, `research_horizon/frame-invariants-where-scalars-fail`

**Pronunciations:** Cartan → kar-TAHN; Karlhede → KARL-hay-deh; Kundt → KOONT; Kruskal → KRUS-kul; Petrov → PET-roff; Segre → SEG-reh; Lemaître → leh-METR

**Voice notes:** At entry say "rounds" and "news"; at the working rung say once that a round is an order of covariant derivative.

## History

- **Élie Cartan (1946).** Set out the solution of the local equivalence problem for Riemannian metrics by comparing frame components of the curvature and its covariant derivatives, part of his general method of equivalence. Élie Cartan (1946), *Leçons sur la géométrie des espaces de Riemann*, Gauthier-Villars, Paris (second edition)
- **Carl H. Brans (1965).** Adapted Cartan's method of equivalence to the metrics of general relativity. Carl H. Brans (1965), *Invariant approach to the geometry of spaces in general relativity*, Journal of Mathematical Physics 6, 94–102, doi:10.1063/1.1704268
- **Anders Karlhede (1980).** Turned the method into a staged procedure that fixes frames order by order, stops when the counts stall, bounds the derivative order in four dimensions, and yields the dimensions of the isometry and isotropy groups. Anders Karlhede (1980), *A review of the geometrical equivalence of metrics in general relativity*, General Relativity and Gravitation 12, 693–707, doi:10.1007/BF00771861

## Research horizon

- **Sharpness of the Karlhede bound.** The four-dimensional bound of seven covariant derivatives is attained by type N null radiation on an anti-de Sitter background. These examples are curvature homogeneous to second order, so no independent invariant appears before the third derivative; whether the lower bounds conjectured for other algebraic types are sharp remains open. Anders Karlhede (1980), *A review of the geometrical equivalence of metrics in general relativity*, General Relativity and Gravitation 12, 693–707, doi:10.1007/BF00771861; Robert Milson, Nicos Pelavas (2008), *The type N Karlhede bound is sharp*, Classical and Quantum Gravity 25, 012001, doi:10.1088/0264-9381/25/1/012001
- **Classification by computer algebra.** Implementations of the algorithm compute canonical frames, counts and functional relations, and are used to decide whether a claimed new exact solution is a known one. The final comparison of relations needs zero recognition of expressions, which limits full automation. Malcolm A. H. MacCallum (2018), *Computer algebra in gravity research*, Living Reviews in Relativity 21, 6, doi:10.1007/s41114-018-0015-6
- **Frame invariants where scalars fail.** All four-dimensional spacetimes with vanishing scalar curvature invariants are Kundt, and a metric not locally characterized by its scalar polynomial invariants must be degenerate Kundt. For these metrics the Cartan invariants of the algorithm remain a complete local classification. Vojtěch Pravda, Alena Pravdová, Alan Coley, Robert Milson (2002), *All spacetimes with vanishing curvature invariants*, Classical and Quantum Gravity 19, 6213–6236, doi:10.1088/0264-9381/19/23/318; Alan Coley, Sigbjørn Hervik, Nicos Pelavas (2009), *Spacetimes characterized by their scalar curvature invariants*, Classical and Quantum Gravity 26, 025013, doi:10.1088/0264-9381/26/2/025013
- **Local homogeneity from finitely many derivatives.** When no invariant is functionally independent, the counts make a space locally homogeneous. For Riemannian manifolds Singer showed that agreement of the curvature and its covariant derivatives up to a finite order, under linear isometries between tangent spaces, already implies local homogeneity. Isadore M. Singer (1960), *Infinitesimally homogeneous spaces*, Communications on Pure and Applied Mathematics 13, 685–697, doi:10.1002/cpa.3160130408

## Review: novice

**Verdict:** fixed (2026-09-13, revision 7)

**Retell attempt:** A walker on an egg has only a cardboard arrow and no paint. First she goes to spot after spot, walks small loops all of one size with the little patch on her left, and writes down how far the arrow comes back turned. That is round one. In round two she compares the turns at spots close around her and picks the direction where the turn grows fastest; near the pointed end it runs toward the tip. That direction comes from the arrow, not from paint, so any other walker finds the same one and lines her arrow up the same way. Round three measures how that growth changes along her arrow and sideways. Then each later round measures how the last round came out, and I had to stop there, because 'the last round' sounded like the final round, which is exactly the thing the note says exists. A round counts as news if it gives a direction to line up with or a number she could not already work out, and she stops at the first round with no news. Why can nothing new ever turn up afterwards? The note answers only for the numbers, and I had just been told there are two kinds of news, so I could not see why round six could not suddenly hand her a direction. On a ball she stops at round two, because the turn is the same everywhere. On the egg I never learn when she stops, although I followed her the whole way. To compare two surfaces you try to pair their spots so that all the numbers match. For the curved space and time of gravity you never need more than eight rounds, and 'Using it there first needs calculus' I read twice before it came out right.

**Stumbles (14)**

- “Each later round measures how the last round's results change.”: 'The last round' reads as the final round, which is exactly the thing the recipe is building towards, so the sentence had to be reread. The glossary entry for 'round' already says 'the previous round's results': one idea, two words.
- “Every number in that round can be worked out from earlier ones, so how those numbers change is no news either.”: Two sentences earlier the reader is told news comes in two kinds. This reason closes only the number kind, so the reader is left to take on trust that no later round can hand the walker a direction to line up with. It is the note's central surprise and its reason is half given.
- “like the steepest path on a hillside”: A direction with no sense given: the steepest path down a hillside is just as steep as the steepest path up it, and the walker needs one direction, not two.
- “Using it there first needs calculus and the mathematics of curving in four dimensions.”: 'Using it there first needs' is a garden path, read once as 'needs first' and once as 'first needs'. 'It' also has 'the rounds' and 'ordinary spots' standing nearer than the recipe.
- “keep the small piece the loop marks off on your left”: Reread: 'marks off on your left' first parses as one phrase, as though the loop did the marking on your left. The rule is something the walker does while walking, and should read that way.
- “where nearby spots get the same amount of news in each round”: Spots do not get news; the walker does. Everywhere else the note says a spot gives a turn.
- “If some pairing makes all these numbers match, the surfaces are the same near those spots.”: 'These numbers' points back over two sentences to no named list, so the reader has to guess which numbers are meant.
- “Explain when the rounds of measurements stop, using a ball as the example.”: 'Rounds of measurements' for what the rest of the note calls rounds: two phrasings for one idea.
- “Physicists who find new possible shapes of space and time, allowed by Einstein's theory of gravity, run it on computers.”: 'It' names nothing in the sentence. The nouns actually present are the theory and the shapes, and both are wrong.
- “A ball, for example, can be rotated in three independent ways.”: 'Independent' is not a word this reader can cash out, and this is the answer's only number, so the number lands on an idea the reader cannot picture.
- “a repainting must satisfy more conditions than it has free choices, so guessing usually fails, and a failed guess proves nothing”: Three steps in one sentence, none of them shown: what a repainting has to achieve, what its free choices are, and why a failed guess settles nothing.
- “The rounds give lists you can compare directly”: 'Lists' where the way, the summary and the takeaway all say numbers.
- “A distance rule says how far apart neighbouring spots of a painted grid are.”: The recap's first sentence uses 'spot' and 'painted grid', and neither is in this note's glossary, although the note does gloss loop, swing, arrow test and distance rule from the same prerequisite. A reader who meets the recap cold has two undefined terms in the opening line.
- “After a round with no news, every number can be worked out from earlier numbers, so how those numbers change brings no news either.”: The tutor says this aloud, and it carries the same half-answer as the entry way: it closes the number kind of news and leaves the direction kind open.

**Fixes**

- Entry way: the stopping reason now covers both kinds of news ('Every number in that round, and in every round after it, can be worked out from earlier ones, so no later round brings news'), and the misconception correction rounds-never-end was aligned with it word for word.
- Entry way: 'the last round's results' became 'the previous round's results', matching the glossary entry for 'round'; 'the steepest path on a hillside' became 'the steepest way up a hillside'; the closing sentence became 'To use the recipe there, you need calculus and the mathematics of curving in four dimensions.'
- Entry recap: the walking rule now reads as something done while walking ('walk so that the small piece the loop marks off stays on your left'). Simplifies: spots give news, they do not get it.
- Summary: 'all these numbers' became 'every number from the rounds'. The claim is unchanged (some pairing of nearby spots matching every canonical number gives sameness near those spots); the commas around 'written for different painted grids' were dropped to stay inside the 500-character limit, which also makes the phrase restrictive, as intended.
- Takeaway: 'the first one that finds neither' became 'the first round that finds neither'. The summary keeps 'the first one', where the subject 'The rounds' stands in the same sentence and the character limit is tight.
- Entry objective explain-when-rounds-stop: 'the rounds of measurements' became 'the rounds'.
- Glossary: added 'spot' and 'painted grid', so the recap's opening line has no undefined term.
- Entry common questions: why-not-just-find-the-repainting split into three sentences that say what a repainting must match, why guesses fail, and why a failed guess proves nothing, and says 'numbers' instead of 'lists'; what-is-it-used-for names the recipe instead of an unattached 'it', and replaces 'three independent ways' with three lines through the ball's centre and rotations built from them.
- Nothing was dropped. The entry explanation went from 324 to 329 words, inside the 330 the review allowance permits over the frontier cap of 300, and every added word belongs to a stumble recorded here.
- Ladder checked: each non-entry way opens by naming the way it continues; the four ways use four different kinds; index-notation is in the prerequisite closure through orthonormal-frame, so the working way's component notation is allowed; the working way already bridges 'a number she could not work out from earlier ones' to 'not a function of them'.
- This record is an independent second novice pass, made at revision 4 and signing revision 5. It replaces the earlier novice record for revisions 1 to 4, which survives in git history at the previous commit of this file; that pass's re-read log is kept below in rereads.
- Bumped the revision to 5 and set the status back to novice-reviewed, because these entry-rung changes came after the physics sign-off at revision 4.

**Concerns**

- The entry way never says at which round the egg walker stops, although she is the reader's companion from the first sentence; only the ball is finished. The working way gives round three. There is no budget for it: the entry explanation is at 329 of the 330 words the review allowance permits. Proposed sentence for an editor who frees room, at the end of the ball paragraph: 'Near an ordinary spot on the egg she stops one round later, at round three.'
- Two changed entry sentences need the physics lens at revision 5: 'Every number in that round, and in every round after it, can be worked out from earlier ones, so no later round brings news' (the entry form of the stopping theorem, now claiming both no new invariant and no further reduction of frame freedom at every later order), and 'A ball can be rotated about three different lines through its centre. Every other rotation of the ball can be built from those three.'
- The summary now runs to five sentences against the guide's two or three. Each carries a step that the physics review or the revision-4 re-read added, so merging them would compress rather than shorten; an editor should decide whether to accept five or to move a step into the entry way.
- Still no observations and no everyday measured number at the entry rung; the only numbers are round counts (a ball stops after round two, gravity never needs more than eight rounds). Both earlier reviews raised this and left it to an editor.
- The entry rung is full: 329 of 330 words. Any further entry addition needs a cut named in the review that makes it.
- Carried forward, unresolved upstream: the conventions file fixes no null-tetrad or Newman-Penrose conventions, so the note stays in hatted orthonormal components and says so in notation_traps; it also fixes no bookkeeping notation for t_q, s_q, q and p.
- Carried forward: the registry lists only two of the note's five prerequisites, and the three linked visuals are proposals with sketches only.

**Re-read** (2026-09-13, revision 4): 3 stumbles in 4 changed passages

- “Surfaces whose spots pair up so all these numbers match are the same near those spots.”: Squeezed: nobody does the pairing, so spots seem to 'pair up' by themselves, and the reader must unpack a long subject before reaching the verb. It also no longer matches the entry way's 'can be paired'.
- “Neither count changed, so the stopping rule, taken on trust here, ends the algorithm at $q = 2$”: Step taken on trust without naming what is trusted: the reader cannot tell whether the rule itself or the reason it is safe is left unexplained, and the rule is not restated in this way.
- “$e_1 = \pm\partial_r$ along $\nabla K$, $e_2 = f^{-1}\partial_\phi$; the sign of $e_1$ does not change them”: '$\pm\partial_r$ along $\nabla K$' is compressed, and 'them' is far from its noun, with the frame vectors as other candidates (rule 11).
- Fix: Summary: last sentence split in two, naming the two surfaces and a pairing of their spots, matching the entry way; claim unchanged (some pairing of nearby spots with all numbers matching gives sameness near those spots). Split keeps the average sentence length within the validator's aim.
- Fix: Working way on the surface of revolution: the stopping sentence split in two, naming what is taken on trust (that a round with no change means no later order adds anything); the stop at q = 2 and p = 1 are unchanged.
- Fix: Hessian symbol meaning: sign choice spelled out and 'them' replaced by 'these components'; claim unchanged.
- Fix: Read and left as is: the gloss 'meaning one that is not a function of them' and 'agree near that value of K', both clear at the working rung. Nothing dropped; no budget allowance used beyond a few words.

**Re-read** (2026-09-13, revision 7): 1 stumbles in 2 changed passages

- “There are more conditions to meet than choices you can make, so guesses usually fail.”: Reread once. The answer's other sentences speak to 'you', but this one starts with 'There are', so both counted things arrive with no owner: the reader has to work out that the conditions are the ones the previous sentence sets and that the choices are the ones she would make while repainting. The imbalance also carried the weight of the word 'far' before; with the count now simply 'more', the comparison has to be legible on one hearing, and 'conditions to meet' against 'choices you can make' is not parallel.
- Fix: Entry common question 'why-not-just-find-the-repainting': the counting sentence now names who does the counting and makes the two sides parallel ('conditions to meet' against 'choices to make'), matching the 'You can try' that opens the answer. The claim is untouched: more conditions than choices, so guesses usually fail. One word shorter, so no budget allowance used.
- Fix: Read and left as is: the rest of the answer ('A failed guess proves nothing either...' and 'The rounds instead give numbers you can compare directly...'), which reads cleanly after the change. Nothing dropped.

## Review: physics

**Verdict:** fixed (2026-09-13, revision 7)

**Verification**

- Surface of revolution ds^2 = dr^2 + f(r)^2 dphi^2: K = -f''/f; Christoffels Gamma^r_phiphi = -f f', Gamma^phi_rphi = f'/f, Gamma^r_rr = Gamma^r_rphi = 0.: Re-derived the Christoffels from the course formula. Tested K = -f''/f numerically on f = sin r (sphere), f = e^r (K = -1) and f = sqrt(1+r^2), the arclength form of the catenoid, against the independent catenoid value -1/cosh^4 t. → Correct: 1.000000, -1.000000 and -0.37180249 against -0.37180250.
- Hessian in the canonical frame: H11 = K'', H22 = (f'/f)K', H12 = 0, with e1 = +-d_r along grad K and the components independent of that sign.: Two independent routes. (i) Frame route: H(X,Y) = X(YK) - (nabla_X Y)K with nabla_e1 e1 = 0, nabla_e2 e2 = -(f'/f) d_r, nabla_e1 e2 = 0. (ii) Coordinate route: H_mn = d_m d_n K - Gamma^l_mn d_l K, giving H_rr = K'', H_phiphi = f f' K', H_rphi = 0, then normalized by f^2. Repeated with e1 = -d_r for K' < 0; H11 is quadratic in e1, H22 and H12 do not involve its sign. → Both routes agree, and agree for either sign of e1. Radial lines are geodesics (Gamma^l_rr = 0), which is what makes H11 the plain second derivative K''.
- Counts on a surface of revolution with K' != 0: (t,s) = (1,1), (1,0), (1,0); q = 2, p = 1, d_iso = 2 - 1 + 0 = 1, the rotations phi -> phi + c.: Applied the stopping rule order by order: at k = 1, t is unchanged but s drops from 1 to 0, so no stop; at k = 2 both are unchanged, so q = 2. Checked the rotation-angle argument: a frame turned by alpha has gradient components K'(cos alpha, -sin alpha), so demanding the second vanish and the first be positive fixes alpha and leaves only e2 -> -e2. → Correct.
- Unit sphere: K = 1, t0 = 0, s0 = 1, gradient vanishes, q = 1, p = 0, d_iso = 2 - 0 + 1 = 3. Generic surface with K and |grad K|^2 independent: t1 = 2, s1 = 0, q = 2, no continuous symmetry.: K = -f''/f with f = sin theta gives 1. Hand count with the ceiling t <= n = 2 and the floor s >= 0, which is why neither count can move past order 1 in the generic case. → Correct; 3 matches dim SO(3) and 0 matches a surface with no Killing field.
- Classification of surfaces of revolution by F1 = |grad K|^2, F2 = H11, F3 = H22 as functions of K is complete near points with K' != 0, and F2 is redundant.: Independent reconstruction: (dK/dr)^2 = F1(K) fixes K(r) up to a shift and a reflection of r; F3 = (f'/f)K' then fixes f'/f, hence f up to a constant factor that a rescaling of phi absorbs. Chain rule gives F2 = K'' = (1/2) dF1/dK on any such surface. → Correct, and the 'exactly when' is a genuine iff with the stated near-that-value-of-K scope. F2 is redundant, as problem part (b) says.
- Problem order-two-data-of-power-law-surfaces, f = r^a: K = -a(a-1)/r^2, F1 = 4a^2(a-1)^2/r^6, F2 = -6a(a-1)/r^4, F3 = 2a^2(a-1)/r^4; F3(a)/F3(1-a) = a/(1-a); F3/K^2 = 1 for a = 3 and -2/3 for a = -2.: python3 at r = 1.3 and 1.7 for a = 3, -2, 2, -1, 0.5, with a finite-difference cross-check of K' and K''; hand algebra for the chain rule and for a -> 1-a, which leaves a(a-1) fixed. → All reproduced: F3/K^2 = 1.000000 and -0.666667; ratios -1.5 for a = 3, -2.0 for a = 2, 1.0 for a = 0.5. Tolerances 0.01 are ample. F3 never vanishes because a = 0 and a = 1 are excluded, so the ratio argument is safe.
- Check frame-fixed-is-not-finished: f = r^2 and f = 1/r both give K = -2/r^2, |grad K|^2 = -2K^3 and H11 = -3K^2, while H22 = 2K^2 and -K^2.: python3: F1/(-2K^3) = 1.000000 and F2/K^2 = -3.0000 for both; F3/K^2 = 2.000000 and -1.000000. Checked that the two H22 functions meet only at K = 0, which the surfaces never reach. → Correct, and the numeric answers 2 and -1 are right with sign.
- Check sphere-and-power-law-counts: sphere q = 1, d = 3; f = r^2 surface q = 2, d = 1.: Hand count against the stopping rule, as above. → Correct.
- Schwarzschild static-frame components R_trtr = -2M/r^3, R_tThtTh = R_tPhtPh = M/r^3, R_rThrTh = R_rPhrPh = -M/r^3, R_ThPhThPh = 2M/r^3; Ricci zero; Kretschmann 48M^2/r^6.: Sign fixed by the course geodesic-deviation row (radial stretch for a static observer needs R^r_trt < 0). Built the full 4-index array in python3 from these components with all index symmetries, contracted with eta to get the Ricci tensor and the Kretschmann scalar. → max |Ricci| = 0 and Kretschmann = 48.000000 in units M = r = 1. Correct in the course convention.
- Schwarzschild order 0 and 1: boosts in the t-r plane and rotations in the theta-phi plane preserve every component, so s0 = 2; dI = -288 M^2 r^-7 dr with |dI|^2 = (1 - 2M/r)(288M^2/r^7)^2 > 0 for r > 2M; s1 = 1, t = 1, q = 2, p = 1, d_iso = 4 - 1 + 1 = 4.: Applied the boost e_t -> cosh b e_t + sinh b e_r explicitly: the transformed R_tThtTh is cosh^2(M/r^3) + sinh^2(-M/r^3) = M/r^3, and the transformed mixed component R_tThrTh is cosh b sinh b (M/r^3 - M/r^3) = 0, which is exactly the note's phrasing. A t-theta boost instead gives cosh^2(-2M/r^3) + sinh^2(-M/r^3), not invariant. A nontrivial boost in a timelike plane fixes only null directions of that plane, so it cannot fix the spacelike radial dI. → Correct; d_iso = 4 matches the four Killing fields (time translation and three rotations), with orbits the r = const surfaces and isotropy the rotations about the radial direction.
- SI numbers at the Sun's surface: GM/c^2 = 1476.6 m, M/r^3 = 4.39e-24 m^-2, R_trtr = -8.77e-24 m^-2.: python3 with G = 6.67430e-11 m^3 kg^-1 s^-2, M = 1.98847e30 kg, c = 2.99792458e8 m/s, r = 6.957e8 m. → 1476.67 m, 4.3855e-24 m^-2, 8.7710e-24 m^-2. Correct to the quoted figures, and the units m^-2 are right for GM/(c^2 r^3).
- Check same-counts-different-spacetimes: M/r^3 = sqrt(I/48); 2M/r = 2 M^(2/3) (I/48)^(1/6); M^4 r^-14 = M^(-2/3) (I/48)^(7/3), so |grad I|^2 as a function of I carries M.: Hand algebra from r = (48M^2/I)^(1/6), exponent by exponent: r^-14 = (I/48)^(7/3) M^(-14/3) and 4 - 14/3 = -2/3. → Correct. Two de Sitter spacetimes with different Lambda likewise share types and counts, so the misconception is genuinely diagnosed.
- Problem flrw-dust-stops-at-first-order: R_mn = 8 pi rho (u_m u_n + g_mn/2); s0 = 3, t0 = 1, s1 = 3, t1 = 1, q = 1, d_iso = 6; de Sitter s0 = 6, t0 = 0, d_iso = 10.: Trace-reversed the course Einstein equation with T_mn = rho u_m u_n and T = -rho, giving R = 8 pi rho and the stated Ricci tensor. Contracted R_mnrs = (Lambda/3)(g_mr g_ns - g_ms g_nr) to R_mn = Lambda g_mn and checked G_mn + Lambda g_mn = 0. Checked that grad R for dust is built from u and g, so the rotations survive at order 1. → Correct: 6 for the flat dust model (three translations, three rotations) and 10 for de Sitter.
- Check plane-wave-at-order-zero: ds^2 = -2 du dv + (x^2-y^2) a(u) du^2 + dx^2 + dy^2 is vacuum and has R_uxux = -a(u).: Computed the Christoffels of ds^2 = -2 du dv + H du^2 + dx^2 + dy^2 (nonzero: Gamma^v_uu = -H_u/2, Gamma^v_ui = -H_i/2, Gamma^i_uu = -H_i/2) and then R^x_uxu = d_x Gamma^x_uu = -H_xx/2, all quadratic terms vanishing, so R_uxux = -H_xx/2. With H = (x^2-y^2)a: H_xx = 2a and H_yy = -2a. → Correct: R_uxux = -a, R_uyuy = +a, and H_xx + H_yy = 0 makes it vacuum. The orbit-closure reason given for the vanishing scalars (boosts along the propagation direction scale every component, and a continuous polynomial invariant is then forced to its value at zero curvature) is the standard argument and is stated correctly.
- Check bifurcation-sphere-counts: pointwise rank 0 gives 4 - 0 + 2 = 6, the true dimension is 4, orbit 2 and isotropy 2.: r is a function of UV in the Kruskal extension, so dr is proportional to U dV + V dU, which vanishes at U = V = 0; every invariant is a function of r, so every differential vanishes there. The static Killing field vanishes on the bifurcation sphere and acts as a boost on the tangent space, and the rotations fixing a point of that 2-sphere form a one-parameter group, so isotropy is 2 and 2 + 2 = 4. → Correct, and the named failed hypothesis (counts constant near the point) is the right one: just off the sphere t = 1 and s = 1 give 4 - 1 + 1 = 4.
- Formal way: stopping theorem sketch, symmetry theorem sketch, Cartan's criterion in canonical form, and problem isometry-dimension-from-self-equivalence.: Read each step for gaps. The stopping sketch needs the order-(p+1) components to fix the connection components outside the Lie algebra of H_p and then the order-(p+2) components to be H_p-invariant functions of the I_alpha; the symmetry sketch needs uniqueness of a local isometry from the image of one frame, the level set of dimension n - t_p, and the fibre of dimension s_p. → Sound as proof sketches under the stated constant-count hypothesis. Checked the formula against four independent cases: Minkowski 4 - 0 + 6 = 10 (Poincare), de Sitter and anti-de Sitter 10, flat dust 6, Schwarzschild 4, sphere 3, surface of revolution 1.
- Bounds: Cartan's frame-bundle count gives order 10 in four dimensions (4 + 6 = dim of the orthonormal frame bundle, with O(1,3) of dimension 6); Karlhede's analysis gives seven derivatives; t runs 0..4 and s runs 0..6.: Checked dim O(1,3) = 6 and dim F = 10; checked 0 <= t <= n = 4 and 0 <= s <= 6 against the definitions; the seven-derivative bound is marked as taken on trust in the note and is confirmed by the Karlhede and Milson-Pelavas records below. → Correct, and the note does not claim the naive t-and-s count reproduces either bound.
- Entry: 'For the curved space and time of gravity, the recipe never needs more than eight rounds near ordinary spots.': Round k of the entry way is order k-1, as the working way states. The Karlhede bound is q <= 7, i.e. orders 0 through 7, which is eight rounds. Cross-checked against Milson and Pelavas, where grad^7 R is needed. → Correct: eight rounds, and the ordinary-spot scope carries the constant-count hypothesis.
- Entry and simplifies: on an egg, a small loop near the pointed end turns the arrow more than a same-size loop at the middle; near the pointed end but not at the tip, the direction of fastest growth of the turn runs toward the tip; at the tips and at the ring where the turn is smallest, no direction wins.: python3 on a model egg rho(z) = 0.75 sqrt(1-z^2) sqrt(1-kz) for k = 0.2 and 0.4, using K = -rho''/(rho (1+rho'^2)^2) for a surface of revolution about z. → Correct. K is about 2.82 (k = 0.2) and 3.30 (k = 0.4) near the pointed tip against about 1.00 at the middle; K has a single minimum ring (z = 0.19 and 0.33) and increases monotonically from it to the pointed tip, so grad K points toward the tip; grad K vanishes on that ring and, by rotational symmetry, at both tips.
- Entry stopping rule as rewritten at revision 5: 'A round can bring two kinds of news: a direction to line up with, or a number she could not work out from her earlier numbers. At the first round with no news, she stops. Every number in that round, and in every round after it, can be worked out from earlier ones, so no later round brings news.': Compared with the stopping theorem in the formal way. t_q = t_(q-1) makes every order-q canonical component a function of the t_p independent invariants, which is the first clause; the theorem then makes every higher-order component a function of the same invariants AND invariant under H_p, which closes the direction half as well as the number half. → Accurate, and this closes the concern the revision-4 review recorded: the earlier wording ('so how those numbers change is no news either') settled only the new-number half, while the new wording covers both kinds of news and is exactly what the theorem gives. No change needed.
- Entry common question as rewritten at revision 5: 'A ball, for example, can be rotated about three different lines through its centre. Every other rotation of the ball can be built from those three.': Checked against dim SO(3) = 3 and against the note's own d_iso = 2 - 0 + 1 = 3 for the sphere. Checked the 'built from those three' claim: three mutually perpendicular axes give every rotation by yaw-pitch-roll, and rotations about any two distinct axes already generate SO(3), so the sentence is true for any three distinct lines through the centre. → Accurate, and a true strengthening of the revision-4 wording 'can be rotated in three independent ways', which left 'independent' undefined.
- Entry summary as rewritten at revision 5: 'If some pairing makes every number from the rounds match, the surfaces are the same near those spots.': Compared with Cartan's criterion in canonical form and retried the pointwise counterexample (two surfaces of revolution with equal F1(K) whose F3(K) curves cross at one value of K). → Accurate; 'every number from the rounds' is the canonical components up to the stopping order, and the existential pairing over nearby spots keeps the revision-3 fix intact.
- Other revision-5 entry rewrites: 'the steepest way up a hillside'; 'Each later round measures how the previous round's results change'; 'walk so that the small piece the loop marks off stays on your left'; 'where every nearby spot gives the same amount of news in each round'; 'stop at the first round that finds neither'; the rounds-never-end correction; the new glossary entries for 'spot' and 'painted grid'.: Read each against the mathematics it stands for: gradient as steepest ascent; round k as order k-1; the course orientation row (a loop bounding a region on the walker's left has positive turn); the constant-count hypothesis; the stopping rule. → All accurate. The recap's left-hand rule now names an action the walker performs, which matches the conventions row exactly.
- Entry common question: 'There are far more conditions to meet than choices you can make, so guesses usually fail.': Counted the equations and unknowns of the transformation law in the reader's own setting. On a surface a repainting has 2 free functions against 3 independent metric components; in four dimensions it is 4 against 10. → Overstated for surfaces, which is the whole setting of the entry rung: 3 against 2 is more, not far more. Changed to 'more conditions to meet than choices you can make', which is true in both settings and equally simple. The overdetermination, not its size, is what makes guesses fail.
- Reference Cartan 1946, Lecons sur la geometrie des espaces de Riemann, second edition, Gauthier-Villars; contribution scoped as 'set out', not 'first'.: Publisher and library records; re-read the contribution wording for scope. → Confirmed; verified stays true.
- Reference Brans 1965, Invariant approach to the geometry of spaces in general relativity, J. Math. Phys. 6, 94-102, doi 10.1063/1.1704268.: WebSearch: journal table of contents for 1965 and the author's own copy of the paper. → Confirmed; verified stays true.
- Reference Karlhede 1980, A review of the geometrical equivalence of metrics in general relativity, Gen. Rel. Grav. 12, 693-707, doi 10.1007/BF00771861.: WebSearch and the Springer record, including the abstract. → Confirmed, volume, pages and year all right; the abstract confirms that the method gives the dimensions of the isometry group and its isotropy subgroup, which is what the contribution claims. Verified stays true.
- Reference Milson and Pelavas 2008, The type N Karlhede bound is sharp, Class. Quantum Grav. 25, 012001, doi 10.1088/0264-9381/25/1/012001, arXiv 0710.0688; and the note's description of the examples.: Fetched the arXiv abstract page and read the abstract verbatim. → Confirmed. The abstract says the spacetimes are null radiation, type N solutions on an anti-de Sitter background, properly curvature homogeneous of order 2, with tetrad components of R, grad R and grad^2 R constant, essential coordinates first at grad^3 R, one further invariant at each of orders 4, 5 and 6, and grad^7 R needed for the classification. Every clause of the research way, the seven-derivatives check and the sharpness horizon topic matches this. Verified stays true.
- Reference Pravda, Pravdova, Coley, Milson 2002, All spacetimes with vanishing curvature invariants, Class. Quantum Grav. 19, 6213-6236, doi 10.1088/0264-9381/19/23/318, arXiv gr-qc/0209024.: Fetched the arXiv abstract page. → Confirmed; the result is that the vanishing-invariant spacetimes form a subclass of the Kundt class, which is what the horizon topic claims. Verified stays true.
- Reference Coley, Hervik, Pelavas 2009, Spacetimes characterized by their scalar curvature invariants, Class. Quantum Grav. 26, 025013, doi 10.1088/0264-9381/26/2/025013, arXiv 0901.0791; and the note's 'must be degenerate Kundt'.: Fetched the arXiv abstract and the paper's main theorem. → Confirmed. The theorem states that a spacetime metric is either I-non-degenerate or in the Kundt class, and the paper narrows the exceptional case to the degenerate Kundt metrics it names, so the note's stronger wording is supported. Verified stays true.
- Reference MacCallum 2018, Computer algebra in gravity research, Living Rev. Relativ. 21, 6, doi 10.1007/s41114-018-0015-6.: WebSearch: journal and PubMed records. → Confirmed; verified stays true. It is the review the frontier tier requires.
- Reference Singer 1960, Infinitesimally homogeneous spaces, Comm. Pure Appl. Math. 13, 685-697, doi 10.1002/cpa.3160130408; and the note's Riemannian scoping of the theorem.: WebSearch: Wiley record with volume, issue, year and pages. → Confirmed, including the page range. The note keeps the theorem scoped to Riemannian manifolds, which is right, since the Lorentzian statement is a separate and weaker story. Verified stays true.
- Structure: prerequisites direct and acyclic; formal rung has at least two formal checks and one formal problem; every check and problem evidences an objective; visual ids are proposals with sketches; no source book is named anywhere a reader can see.: Read the five prerequisites and confirmed none of them lists this concept; counted three formal checks and two formal problems; matched every check and problem id against objectives[].evidenced_by; read all three visual entries for sketches; grepped the learner-visible fields for book names, authors used as convention labels, and chapter or equation numbers. → All hold. Observations are empty, which is honest for a frontier note about a classification procedure, but see concerns.

**Counterexamples tried**

- Cone away from its tip: K = 0, so t0 = 0, s0 = 1, q = 1 and the formula gives 2 - 0 + 1 = 3 local symmetries, although the cone has only a one-parameter global isometry group. Correct, because the symmetry theorem is about local isometries, which the formal way's Limits paragraph states; the entry and working ways never claim a global count.
- Flat cylinder, flat torus and plane: all have K = 0 everywhere, all pair up, and all are locally the same, which is right (a bent but flat surface is intrinsically flat) and again shows the counts are local.
- Helicoid against catenoid: locally isometric although only one is a surface of revolution. The classification by F1, F2, F3 as functions of K gives them identical data, as it must. The working way's 'surface of revolution' scope limits the computation, not the result.
- Pointwise matching (summary): two surfaces of revolution with the same F1(K) whose F3(K) curves cross at one value K*. At spots with K = K* every number agrees, yet the surfaces are not the same near those spots. The summary's existential pairing over nearby spots still blocks this.
- Two balls of different size: no pairing matches the turn, so they are different; each stops after round two with three symmetries.
- Egg tips and the ring of smallest turn: grad K vanishes, no direction wins, and the ordinary-spot scope in simplifies covers it.
- Walking the loop the other way round, or on the inside of an eggshell: the turn changes sign and the found direction reverses. The recipe's left-hand rule fixes the sense for walkers on the same side, which the recap and the two-walkers check both state.
- Mobius band: the algorithm uses O(2) frames including reflections and every statement is local, so non-orientability costs nothing; the entry way's left-hand rule is a local choice.
- Great circles, figure-eight loops and regions bigger than half a closed surface: none arise, because the entry way uses only small loops of one size, where the turn is K times the area with no modulo ambiguity.
- Minkowski spacetime: t0 = 0, s0 = 6, q = 1, d_iso = 4 - 0 + 6 = 10, the Poincare group. Anti-de Sitter likewise 10. Both confirm the symmetry formula at the flat and maximally symmetric ends.
- Bifurcation sphere of the Kruskal extension: pointwise counts give 6 instead of 4, which the formal check uses to name the constant-count hypothesis.
- Vacuum plane wave against Minkowski: every scalar polynomial invariant agrees, frame components separate them at order 0.
- de Sitter with different Lambda, and Schwarzschild with different M: identical types and counts, not equivalent; the counts are not the invariants.
- Surfaces with t1 = 1 that are not of revolution: H22 need not be a function of K, so they can continue past order 2; the working statements are scoped to surfaces of revolution.

**Fixes**

- Entry common question why-not-just-find-the-repainting: 'far more conditions to meet than choices you can make' is an overstatement in the entry rung's own setting, where a repainting of a surface has 2 free functions against 3 conditions. Changed to 'more conditions to meet than choices you can make', which is true for a surface and for four dimensions alike, and keeps the sentence just as simple. This is the only learner-visible change of this pass.
- Bumped the revision to 6 and set review.physics.reviewed_revision to 6.
- Nothing dropped; the tutoring part loses one word and stays well inside its cap.

**Concerns**

- The entry way never says when the egg walker stops, although she is the reader's companion from the first sentence. The novice reviewer proposed 'Near an ordinary spot on the egg she stops one round later, at round three.' for the end of the ball paragraph, and I confirm it is correct: a surface of revolution with K' non-zero stalls at q = 2, which is round three, exactly as the working way states. It could not be added because the entry explanation is at 327 words against a frontier cap of 300, i.e. at the ceiling the 10 per cent review allowance permits. An editor who frees budget should add it; the physics is settled.
- The entry rung is full. Nothing more can go in without a named cut, so the gloss that 'a number she could not work out from earlier ones' means 'a number that is a function of the earlier ones' still lives only in the working way.
- No observations and no everyday measured number at the entry rung. The entry way's only numbers are round counts. Honest for a note about a classification procedure, but rule 12 of the novice contract is not met, and an editor should confirm.
- The summary runs to five sentences against the guide's two or three, and is 2 characters under the schema's 500-character ceiling. Carried forward from the novice review for an editor to decide; every sentence carries a step, so merging would compress rather than shorten.
- Upstream of this note: course-conventions.md still leaves spinors, tetrads beyond hatted components and Newman-Penrose unfixed, and fixes no bookkeeping notation for t_q, s_q, q and p. The note works around the first with the frames-for-canonical-forms notation trap, which tells readers to translate published canonical forms into hatted orthonormal components, and defines t_q, s_q, q and p in place.
- The registry lists only two of the five prerequisites (gaussian-curvature, isometry-group and petrov-classification are missing); sync_registry.py should be run. No cycle exists: none of the five lists this concept.
- All three visuals are still proposals with sketches only, not yet in knowledge/visuals/.
- Record-keeping: this record is an independent second physics pass, signing revision 6. It replaces the record for revisions 1-4, which survives in the pre-edit snapshot at /private/tmp/claude-501/-Users-neo-repos-general-relativity/bdf94c63-cbec-4edd-ba4c-fe7299d5507b/scratchpad/snapshots/notes-curvature/cartan-karlhede-algorithm.before-physics.json; that pass's diff check is preserved in review.physics.diff_checks.

**Diff check** (2026-09-13, revision 4)

- Summary: 'Try pairing the spots of two surfaces. If some pairing makes all these numbers match, the surfaces are the same near those spots.' claims exactly what the revision-3 sentence claimed.: Compared scope with the revision-3 wording and the entry way's 'can be paired'; retried the pointwise counterexample (surfaces of revolution with equal F1(K) whose F3(K) curves cross at one value K*) and plane against cylinder; checked that a pairing matching every round's numbers at every spot of the neighbourhoods forces the relations F_i(K) to agree on the shared range of K. → Accurate. The existential 'some pairing' over nearby spots keeps the fix from the physics review: a single matching spot no longer suffices, the plane and cylinder still come out the same, and the ordinary-spot scope is unchanged.
- Working way: 'Neither count changed, so the algorithm stops at q = 2, and p = q - 1 = 1. That no later order can then bring anything new is taken on trust here.': Checked the stopping rule against the order-by-order counts in the same way (s_1 = s_2 = 0, t_1 = t_2 = 1 since H11 = K'' and H22 = (f'/f)K' are functions of r, hence of K where K' != 0) and against the Karlhede convention t_p = t_{p+1}, s_p = s_{p+1}; checked that the trusted statement is the theorem that once both counts stall, all higher-order components in the fixed frame are functions of lower-order ones and no frame freedom is removed. → Accurate. q = 2 and p = 1 are right, the trusted statement is the correct content of the theorem, and it matches the entry way's 'how those numbers change is no news either' and d_iso = 2 - 1 + 0 = 1.
- Hessian symbol: frame e1 = +-d_r, e2 = f^{-1} d_phi, with the sign of e1 chosen to point along grad K; the components do not depend on that sign.: Re-derived H_ab = d_a d_b K - Gamma^c_ab d_c K with Gamma^r_phiphi = -f f', giving H_rr = K'', H_phiphi = f f' K', normalized H22 = (f'/f)K', H12 = 0; grad K = K' d_r since g_rr = 1, so e1 = sign(K') d_r. H11 and H22 are quadratic or independent in e1 and H12 = 0, so flipping e1 changes nothing; numerical check with f = r^1.5 + 0.3 r^3 at r = 0.9 gave H11 = -8.679, H22 = 6.503, H12 = 0 for both signs. → Accurate; same claim as revision 3, stated more clearly.
- Fix: None; no learner-visible text changed and the revision stays at 4.

**Diff check** (2026-09-13, revision 7)

- Only one learner-visible string changed since the physics review: the entry common question 'why-not-just-find-the-repainting' now says 'You have more conditions to meet than choices to make, so guesses usually fail.' in place of 'There are more conditions to meet than choices you can make, so guesses usually fail.': Ran note_diff.py between the pre-re-read snapshot and the current note to fix the scope (one entry string), then read the changed sentence inside its four-sentence answer. Recounted the comparison the sentence makes: matching one distance rule to the other gives one equation per independent component of a symmetric matrix, n(n+1)/2, against the n functions of a repainting; computed both counts in python for n = 1 to 6. Checked the counts against the note's own linked check equivalence-problem/checks/count-the-equations and against the note's glossary, which defines a distance rule on a surface. → Accurate, and the same claim as before. On a surface the counts are 3 conditions against 2 choices, in four dimensions 10 against 4, so 'more conditions than choices' holds throughout the note's scope; the counts are equal only in one dimension, which the note never treats. Naming 'you' as the party is right: the reader picks the repainting's functions and must satisfy the matching equations, and the note's other sentences in this answer already address the same reader ('You can try', 'a repainting you have not tried').
- The hedge 'so guesses usually fail' still carries the right scope after the rewording.: Tried the first what-ifs a reader would try against the changed sentence and the one it leads into: two identical distance rules (the identity repainting works), a flat plane against a rolled cylinder patch (an unrolling works), and a ball against a plane (no repainting exists). Checked that the sentence claims failure of guesses, not absence of a repainting, and that it agrees with the next sentence, 'A failed guess proves nothing either'. → Accurate. 'Usually' covers the cases where a guess can succeed, the sentence makes no claim that a repainting never exists, and the overdetermined count is the reason the search is impractical rather than impossible. This matches the linked check's 'a map usually does not exist, and failing to guess one proves nothing either way'.
- Fix: None; the changed sentence is accurate, so no learner-visible text changed in this diff check and the revision stays at 7.
