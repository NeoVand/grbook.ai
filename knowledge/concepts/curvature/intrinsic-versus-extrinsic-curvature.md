---
type: "concept"
schema_version: 2
id: "intrinsic-versus-extrinsic-curvature"
title: "Intrinsic versus extrinsic curvature"
tagline: "Bent as seen from outside, or curved for someone measuring along the surface"
domain: "curvature"
tier: "foundation"
status: "physics-reviewed"
revision: 6
updated: "2026-09-13"
aliases: ["intrinsic curvature", "extrinsic curvature of a surface"]
prerequisites: ["curvature", "intrinsic-geometry", "curvature-of-a-curve", "embedding", "levi-civita-connection"]
leads_to: ["gaussian-curvature", "theorema-egregium", "second-fundamental-form", "extrinsic-curvature-of-a-hypersurface"]
visuals: ["paper-rolled-into-a-tube-and-a-cone", "best-fit-circle-along-a-bend", "carry-an-arrow-around-a-loop"]
---

# Intrinsic versus extrinsic curvature

*Bent as seen from outside, or curved for someone measuring along the surface*

`intrinsic-versus-extrinsic-curvature` · curvature · foundation · physics-reviewed (revision 6)

**Needs:** [[curvature]] (entry) · [[intrinsic-geometry]] (entry) · [[curvature-of-a-curve]] (working) · [[embedding]] (formal) · [[levi-civita-connection]] (formal)  
**Opens:** [[gaussian-curvature]] · [[theorema-egregium]] · [[second-fundamental-form]] · [[extrinsic-curvature-of-a-hypersurface]]  
**Related:** [[holonomy]] · [[embedding-diagram]]  
**Visuals:** ★ [[paper-rolled-into-a-tube-and-a-cone]] · [[best-fit-circle-along-a-bend]] · [[carry-an-arrow-around-a-loop]]

> Roll a poster into a tube, and it looks bent, yet an ant measuring along the paper finds every length the same as on the flat poster. Bending seen from the space around a surface is extrinsic curvature, and the rolled poster has it. Curving that shows up in measurements along the surface, as on a ball, is intrinsic curvature.

## You will be able to

**Entry**
- Distinguish intrinsic from extrinsic curvature for a rolled sheet, a lampshade and a ball. `objectives/tell-the-two-meanings-apart` ← `checks/lampshade-for-an-ant`
- Explain why a bent wire can never have intrinsic curvature, while a surface can. `objectives/explain-why-a-wire-hides-its-bend` ← `checks/bead-on-a-wavy-wire`
- Predict which shapes a sheet can take without stretching. `objectives/predict-what-a-sheet-can-do` ← `checks/curl-the-slice`, `checks/saddle-shaped-crisp`

**Working**
- Compute principal curvatures and their product, and decide from them whether a surface is intrinsically curved. `objectives/compute-bends-and-their-product` ← `problems/lampshade-bends`
- Explain how cosmic space can be intrinsically flat yet extrinsically curved inside spacetime, with numbers. `objectives/explain-curved-slices-of-flat-space` ← `checks/flat-yet-expanding`

**Formal**
- Use the Gauss equation to relate intrinsic curvature to the second fundamental form in Euclidean and Lorentzian ambient spaces. `objectives/use-the-gauss-equation` ← `checks/flat-slice-curved-spacetime`
- Prove that a compact surface in Euclidean space has a point of positive curvature, and apply it to the flat torus. `objectives/decide-where-a-geometry-fits` ← `problems/compact-surface-has-a-dome-point`, `checks/flat-torus-homes`

## Ways in

### 1. Two meanings of curved · entry · picture

*When we call a surface curved, what can that word mean?*

**Recap:** The ring test: walk straight, never steering left or right, the same distance from a centre in many directions. Then measure the ring of end marks along the ground. On a flat plain the ring is about 6.28 times the distance walked; on a ball it is shorter. A path that never steers on a rolled sheet never steers on the unrolled sheet either.

Roll a poster into a tube to carry it home, and slip a rubber band around it. Seen from the room, the poster is now bent. Hold a ball next to it. The ball looks bent too. Are the two curved in the same way?

Ask an ant who lives on the paper and measures only along it. She runs the ring test with short walks, well away from the paper's edges. Rolling the poster did not stretch or squash the paper anywhere. So every length along the paper stayed the same, including the distances she walks and the ring she measures.

Her walks and her ring are therefore the same ones she would get on the unrolled poster. On that flat paper, the ring comes out 6.28 times the distance walked. On the tube, it comes out 6.28 times too.

An ant on the ball finds something else. Her ring comes out shorter than 6.28 times the distance walked. So she can tell, without leaving the ball, that her world is not a flat plain.

The word curved therefore has two meanings. The first meaning is bent, as seen from the space around a surface. This is called extrinsic curvature.

The second meaning is curving that shows up in measurements made along the surface. This is called intrinsic curvature.

The rolled poster has extrinsic curvature but no intrinsic curvature. The ball has both. A flat floor has neither.

On a ball as big as Earth, the ring test shows almost nothing over a short walk. A ring paced out 1 kilometre from its centre comes out short by about 0.026 millimetres. That is less than half the width of a hair, so nobody notices it on a walk.

**Takeaway:** Extrinsic curvature is bending seen from the space around a surface; intrinsic curvature shows up in measurements along it. A rolled poster has only the first; a ball has both.

*Builds on:* [[intrinsic-geometry]]<br>*Visuals:* [[paper-rolled-into-a-tube-and-a-cone]]<br>*See:* `checks/lampshade-for-an-ant`

### 2. A wire hides its bend · entry · contrast

*Why can a surface be curved for someone living on it, but a wire never?*

**Recap:** Extrinsic curvature is bending seen from the space around a surface; intrinsic curvature shows up in measurements along it. In the ring test, you walk straight out the same distance in many directions and measure the ring of marks. On a flat plain it is about 6.28 times the distance; on a ball, shorter.

Bend a coat-hanger wire into a wavy line, leaving its two ends free. Imagine a creature the size of a bead who lives on the wire and can only slide along it. Her only tool is a tiny tape measure, laid along the wire. So all she can measure are lengths along the wire, such as the distance between two paint dots.

Now pull the wire straight, carefully, without stretching it. Every length along the wire stays the same. So every length she measures comes out the same on the wavy wire and on the straight wire. For her, the bend is invisible.

For a wire, intrinsic curvature would be curving that shows up in measurements along the wire. A wire, or a thread, can therefore have extrinsic curvature but never intrinsic curvature. Joining the ends into a hoop does not change this. A round hoop and a wavy hoop of the same length give her the same lengths, so she cannot tell them apart.

A surface gives its ant more to measure. She can walk straight out from a centre in many directions and pace out a ring. Then she compares two lengths: the distance walked out, and the ring. On a flat plain, the ring is always 6.28 times the distance. On a ball, the ring is shorter.

Bending a surface without stretching keeps both lengths, so it keeps how they compare. Such bending cannot make a ball's rings come out 6.28 times the distance. Nor can it make a flat sheet's rings come out short.

The creature on the wire can only slide forward or back, so she cannot pace out a ring. Any set of lengths she measures fits a straight wire just as well, or a round hoop if the ends are joined. So none of her lengths can reveal a bend.

**Takeaway:** A wire can be reshaped without stretching, keeping every length along it, so it never has intrinsic curvature. A surface can have intrinsic curvature, because its rings can disagree with a flat plain's.

*Continues:* `ways_in/two-meanings-of-curved`<br>*Visuals:* [[best-fit-circle-along-a-bend]]<br>*See:* `checks/bead-on-a-wavy-wire`

### 3. Curl a slice and it stops drooping · entry · picture

*Why does a pizza slice stop drooping when you curl its crust?*

**Recap:** Intrinsic curvature shows up in measurements along a surface. On a ball, rings come out shorter than 6.28 times the distance walked. Around a swim ring's hole, two walkers who start side by side, both facing the same way at a right angle to the line between them, spread apart. Bending without stretching keeps every length along a sheet, so it creates no intrinsic curvature.

Hold a slice of pizza by its crust, topping side facing the ceiling, without curling it. The tip droops. Now pinch the crust so that the slice curls into a U across its width, with the U's sides rising. The tip stops drooping and sticks out. Why does a U across the slice stop it bending along its length?

Pizza dough hardly stretches, so treat the slice as a sheet that bends but never stretches. The sheet has two faces: the topping face and the bottom face.

Pick a spot on the sheet. Picture short lines drawn along the sheet through that spot, pointing in every direction like the spokes of a wheel. Each line is the path of an ant walking straight. Along each line, the sheet may bend or stay unbent. In a rain gutter, a line across the gutter bends into a U, while a line along the gutter stays unbent.

At a spot where a surface bends at all, its lines show one of three patterns. On a ball, every line through the spot bends, all toward the same face. On a saddle, some lines bend toward one face, and others toward the other face. On a rolled poster, every line bends toward the same face except one, running along the tube, which stays unbent.

A horse's saddle shows the second pattern. So does the part of a swim ring beside its hole. Going around the tube, the ring's surface there bends toward the air sealed inside the tube. Going around the hole, it bends toward the hole.

Any spot that bends like a ball or like a saddle has intrinsic curvature. The ball's short rings show this for a ball, and the walkers spreading apart near the swim ring's hole show it for a saddle. The rule holds at every such spot, for a reason that needs more mathematics. You can test it with paper: press a flat sheet snugly onto an orange, or onto a saddle-shaped potato crisp. Either way, the paper creases, because fitting snugly would need it to stretch.

A sheet bent without stretching never gains intrinsic curvature. Away from creases and a cone's sharp point, it can only bend in the rolled-poster pattern, or not at all. At every spot, all its bent lines bend toward the same face, and at least one line stays unbent.

Now look at the pizza slice again. The U bends every line through a spot toward the topping face, except the line running from crust to tip. That line is the only unbent one, and the sheet must keep one. Drooping would bend it toward the bottom face, which is the saddle pattern. So the tip cannot droop, as long as the U reaches all the way to the tip. A soggy slice can still droop, because its dough stretches, or its U flattens out near the tip.

**Try it:** Hold a sheet of printer paper flat by one short edge: the far end droops. Now curl the edge you hold into a gentle U. The far end lifts and sticks out, although you touch only one edge. The U leaves only the lines running from your hand to the far end unbent, so the paper cannot droop along them.

**Takeaway:** Away from creases and a cone's sharp point, a sheet bent without stretching bends toward only one face at each spot, and keeps an unbent line through that spot. So once it is curled into a U across, it cannot also droop along its length.

*Continues:* `ways_in/two-meanings-of-curved`<br>*Builds on:* [[curvature]]<br>*See:* `checks/curl-the-slice`, `checks/saddle-shaped-crisp`

### 4. Two bends and their product · working · calculation

*How do the bends of a surface in different directions combine into the curvature insiders measure?*

The curled slice in "Curl a slice and it stops drooping" kept an unbent line through every spot, while a ball bends along every line. Principal curvatures turn this into numbers. At a point $p$ of a smooth surface in Euclidean space, choose a unit normal $\hat{\mathbf n}$. The plane through $p$ containing $\hat{\mathbf n}$ and a unit tangent $\hat{\mathbf t}$ cuts the surface in a curve, a normal section. Its curvature at $p$, counted positive when it bends toward $\hat{\mathbf n}$, is the normal curvature $\kappa(\hat{\mathbf t})$. As $\hat{\mathbf t}$ rotates, $\kappa$ has a largest value $\kappa_1$ and a smallest $\kappa_2$, reached in perpendicular directions when they differ: the principal curvatures.

Each principal curvature is extrinsic: reversing $\hat{\mathbf n}$ reverses its sign, and bending without stretching can change it. Their product is intrinsic. Taken on trust here, and derived in "The Gauss equation",

$$K = \kappa_1\kappa_2,$$

where $K$ is the Gaussian curvature, the number the ring test reads: a small ring at walked distance $\rho$ has circumference $C = 2\pi\rho(1 - K\rho^2/6 + \dots)$. Reversing $\hat{\mathbf n}$ reverses both factors and leaves $K$ unchanged.

- Sphere of radius $a$, outward normal: $\kappa_1 = \kappa_2 = -1/a$, so $K = +1/a^2$.
- Cylinder of radius $R$, outward normal: $\kappa = -1/R$ around it and $0$ along it, so $K = 0$, while the mean curvature $\tfrac12(\kappa_1 + \kappa_2) = -1/2R$ is not zero. It is bent but intrinsically flat.
- Saddle $z = (x^2 - y^2)/2R$ at the origin, normal along $+z$: $\kappa_1 = 1/R$ and $\kappa_2 = -1/R$. Their sum vanishes, yet $K = -1/R^2$.

The worked example "Principal curvatures of a swim ring" checks the product against curvatures that walkers on the ring measure. A smooth sheet bent without stretching keeps $K = 0$, so at every point at least one principal curvature vanishes. On the slice's centre line, the slice's mirror symmetry across that line makes the directions across the width and along the slice the principal directions. Where the U curls, the normal curvature across the width is not zero. Their product $K$ is zero, so the normal curvature along the centre line is zero, and the centre line cannot droop there.

**Takeaway:** Each principal curvature is extrinsic, but their product is the Gaussian curvature that insiders measure; a sheet bent without stretching keeps that product zero.

*Continues:* `ways_in/curl-a-slice-and-it-stops-drooping`, `ways_in/two-meanings-of-curved`<br>*Builds on:* [[curvature-of-a-curve]]<br>*Visuals:* [[paper-rolled-into-a-tube-and-a-cone]]<br>*See:* `worked_examples/swim-ring-product`, `problems/lampshade-bends`, `curvature/worked_examples/swim-ring-curvature`

### 5. Flat space that bends inside spacetime · working · operational

*Can extrinsic curvature matter in physics when nothing sits outside spacetime?*

The rolled poster in "Two meanings of curved" was bent relative to a room that really exists. Spacetime has no such room: general relativity describes gravity through spacetime's intrinsic curvature alone. Extrinsic curvature returns for things that do sit inside spacetime, above all space at one moment, a three-dimensional slice of four-dimensional spacetime. Cosmology measures both curvatures of that slice.

Take a spatially flat expanding universe, whose metric is taken on trust here,

$$ds^2 = -c^2dt^2 + a(t)^2\left(dx^2 + dy^2 + dz^2\right),$$

and slice it at constant $t$, the time on clocks carried by galaxies moving with the average cosmic flow.

- *Intrinsic.* Within one slice the distance rule is a constant $a(t)^2$ times the flat rule. Rings and triangles laid out in the slice have Euclidean proportions, so every plane in it has zero Gaussian curvature.
- *Extrinsic.* Push the slice along its unit normal, the four-velocity of those galaxies divided by $c$, by a proper time $d\tau$. Distances between the galaxies, measured within the slice, grow by the factor $1 + H\,d\tau$, where $H = \dot a/a$. How fast distances in a slice change under this push is its extrinsic curvature. Here its principal values all have size $H/c$; their sign depends on a convention.

Both numbers are measured. Planck satellite maps of the microwave background give $H_0 = 67.4 \pm 0.5$ km s$^{-1}$ Mpc$^{-1}$ in the standard cosmological model, where 1 Mpc $= 3.086\times10^{22}$ m. So $c/H_0 = 4.45$ Gpc, about 14.5 billion light-years. Nearby supernovae, with distances calibrated by Cepheid variable stars, give about 73 in the same units, a tension not yet resolved. Combined with galaxy surveys, the same maps give $\Omega_K = 0.001 \pm 0.002$, and the intrinsic curvature of space is $|\Omega_K|H_0^2/c^2$ in size. For $|\Omega_K| \le 0.005$ its radius exceeds 60 Gpc. Space today is intrinsically flat within errors, yet as a slice of spacetime it is clearly curved, and that curvature is the expansion.

**Takeaway:** Space at one moment is intrinsically flat within measurement, yet as a slice of spacetime its extrinsic curvature has size H over c: the expansion.

*What this leaves out:* Uses the cosmic-time slicing. Other slicings change both curvatures of the slices: de Sitter spacetime has flat, spherical and hyperbolic slicings.

*Continues:* `ways_in/two-meanings-of-curved`, `ways_in/two-bends-and-their-product`<br>*Builds on:* [[metric-tensor]]<br>*See:* `observations/planck-flat-but-expanding`, `checks/flat-yet-expanding`

### 6. The Gauss equation · formal · structure

*How exactly is intrinsic curvature tied to the second fundamental form, and where does the tie stop?*

The product $K = \kappa_1\kappa_2$ of "Two bends and their product" and the curved slices of "Flat space that bends inside spacetime" both follow from one identity; set $G = c = 1$. Let $f: (M, g) \to (N, \bar g)$ be an isometric immersion, $f^*\bar g = g$, with metrics of any signature and $g$ nondegenerate. For vector fields $X, Y$ tangent to $M$, split the ambient Levi-Civita derivative:

$$\bar\nabla_XY = \nabla_XY + \mathrm{II}(X,Y).$$

By uniqueness the tangential part is the Levi-Civita connection of $g$. The normal part $\mathrm{II}$, the second fundamental form, is symmetric because $[X,Y]$ is tangent, and being vector-valued it needs no sign choice. For a hypersurface with unit normal $\nu$, $\bar g(\nu,\nu) = \epsilon = \pm1$, write $h = \bar g(\mathrm{II},\nu)$; the shape operator $S$, with $g(SX,Y) = h(X,Y)$, obeys $\bar\nabla_X\nu = -SX$. Intrinsic means built from $g$ and preserved by isometries; $\mathrm{II}$, $S$ and the mean curvature vector $\tfrac1n\mathrm{tr}_g\mathrm{II}$ depend on $f$. With $R(X,Y) = [\nabla_X,\nabla_Y] - \nabla_{[X,Y]}$, the Gauss equation is

$$g(R(X,Y)Z,W) = \bar g(\bar R(X,Y)Z,W) + \bar g(\mathrm{II}(Y,Z),\mathrm{II}(X,W)) - \bar g(\mathrm{II}(X,Z),\mathrm{II}(Y,W)).$$

- *Theorema egregium.* In $\mathbb R^3$, $\bar R = 0$ and $\epsilon = 1$. For orthonormal $e_1, e_2$, $K = g(R(e_1,e_2)e_2,e_1) = h_{11}h_{22} - h_{12}^2 = \det S = \kappa_1\kappa_2$, and the left side is intrinsic.
- *Spacelike slices.* With $\epsilon = -1$ the quadratic terms change sign. Flat cosmological slices have $R = 0$ and $h = \pm Hg$, so every plane tangent to a slice has spacetime sectional curvature $+H^2$.
- *Rigidity.* For a hypersurface of $\mathbb R^{n+1}$ whose shape operator has rank at least 3 everywhere, $g$ fixes $\mathrm{II}$ up to sign (Beez–Killing). A surface fixes only $\det S$, which is why paper bends.
- *Existence.* On a simply connected domain, a metric and a symmetric tensor satisfying the Gauss and Codazzi equations come from a surface in $\mathbb R^3$, unique up to rigid motion (Bonnet).

Limits. A one-dimensional $M$ has $R \equiv 0$, so a curve's curvature is wholly extrinsic. Extrinsic is relative to $N$: the flat torus has $\mathrm{II} \neq 0$ in $\mathbb R^4$ and no smooth isometric embedding in $\mathbb R^3$, since a compact surface there has a point with $K > 0$. By Hilbert's theorem the complete hyperbolic plane has no smooth isometric immersion in $\mathbb R^3$. Spacetime itself needs no $N$; $\mathrm{II}$ enters for hypersurfaces within it, where the Gauss and Codazzi equations constrain initial data.

**Takeaway:** The Gauss equation sets intrinsic curvature equal to ambient curvature plus products of the second fundamental form, so only some combinations of bending are intrinsic.

*Continues:* `ways_in/two-bends-and-their-product`, `ways_in/flat-space-in-curved-spacetime`<br>*Builds on:* [[embedding]], [[levi-civita-connection]], [[manifold]]<br>*See:* `derivations/gauss-equation-from-splitting`, `problems/compact-surface-has-a-dome-point`, `checks/flat-torus-homes`, `checks/flat-slice-curved-spacetime`

## Glossary

| Term | Say | In plain words | Concept |
| --- | --- | --- | --- |
| extrinsic curvature | ex-TRIN-zik | Bending of a surface or a line, as seen from the space around it. A rolled-up poster has it. | [[intrinsic-versus-extrinsic-curvature]] |
| intrinsic curvature | in-TRIN-zik | Curving that shows up in measurements made along a surface or a line, without leaving it. A ball has it. A rolled-up poster does not, and neither does a wire. | [[intrinsic-versus-extrinsic-curvature]] |
| ring test | — | Walk straight out the same distance from a centre in many directions, then measure the ring of end marks along the ground. On a flat plain it is about 6.28 times the distance walked. | [[circumference-to-radius-test]] |
| walk straight | — | To walk without ever steering left or right, even where the path bends over a curved surface. | [[geodesic]] |

## Key equations

### Gaussian curvature as a product of bends · working

$$
K = \kappa_1\kappa_2
$$

The two principal curvatures depend on how the surface sits in space, but their product is the intrinsic Gaussian curvature.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $K$ | Gaussian curvature, positive on a sphere | K |
| $\kappa_1, \kappa_2$ | principal curvatures, the largest and smallest normal curvatures, signed relative to one chosen unit normal | kappa one and kappa two |

**Holds when:** Smooth surface in three-dimensional Euclidean space; either choice of unit normal gives the same product.  
**Say it:** “K equals kappa one times kappa two.”  
**Justified by:** `stated`

### Gauss equation · formal

$$
g(R(X,Y)Z,W) = \bar g(\bar R(X,Y)Z,W) + \bar g(\mathrm{II}(Y,Z),\mathrm{II}(X,W)) - \bar g(\mathrm{II}(X,Z),\mathrm{II}(Y,W))
$$

The intrinsic curvature of a submanifold equals the ambient curvature on its tangent planes plus terms quadratic in its second fundamental form.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $R, \bar R$ | Riemann curvature of the submanifold and of the ambient space, $R(X,Y) = [\nabla_X,\nabla_Y] - \nabla_{[X,Y]}$ | R and R bar |
| $\mathrm{II}$ | second fundamental form, the normal part of the ambient derivative of tangent fields | two |
| $X, Y, Z, W$ | vector fields tangent to the submanifold | X, Y, Z, W |

**Holds when:** Isometric immersion with nondegenerate induced metric, Levi-Civita connections on both manifolds; any codimension and signature.  
**Say it:** “The curvature of the submanifold equals the ambient curvature, plus two of Y Z dotted with two of X W, minus two of X Z dotted with two of Y W.”  
**Justified by:** `derivations/gauss-equation-from-splitting`

## Derivations

### The Gauss equation from splitting the ambient derivative · formal

**Goal:** Relate the curvature of $(M, g)$ to the curvature of $(N, \bar g)$ and the second fundamental form.

1. For tangent fields, $\bar\nabla_XY = \nabla_XY + \mathrm{II}(X,Y)$, where $\nabla$ is the Levi-Civita connection of $g$ and $\mathrm{II}$ is normal.
2. For a normal field $\xi$ and tangent $W$, $\bar g(\xi, W) = 0$; differentiating along $X$ gives $\bar g(\bar\nabla_X\xi, W) = -\bar g(\xi, \mathrm{II}(X,W))$.
3. Differentiate the split along $X$ and pair with $W$: the tangential part of $\bar\nabla_X(\nabla_YZ)$ is $\nabla_X\nabla_YZ$, and step 2 handles $\bar\nabla_X\mathrm{II}(Y,Z)$, so $\bar g(\bar\nabla_X\bar\nabla_YZ, W) = g(\nabla_X\nabla_YZ, W) - \bar g(\mathrm{II}(Y,Z), \mathrm{II}(X,W))$.
4. Swap $X$ and $Y$ and subtract. Since $[X,Y]$ is tangent, $\bar g(\bar\nabla_{[X,Y]}Z, W) = g(\nabla_{[X,Y]}Z, W)$.
5. With $R(X,Y) = [\nabla_X,\nabla_Y] - \nabla_{[X,Y]}$ on both manifolds, $\bar g(\bar R(X,Y)Z,W) = g(R(X,Y)Z,W) - \bar g(\mathrm{II}(Y,Z),\mathrm{II}(X,W)) + \bar g(\mathrm{II}(X,Z),\mathrm{II}(Y,W))$.
6. Check the sign on the unit sphere in $\mathbb R^3$: with the outward normal $h = -g$, so $g(R(e_1,e_2)e_2,e_1) = h_{22}h_{11} - h_{12}^2 = 1$, the positive curvature the course conventions give a sphere.

**Result:** $g(R(X,Y)Z,W) = \bar g(\bar R(X,Y)Z,W) + \bar g(\mathrm{II}(Y,Z),\mathrm{II}(X,W)) - \bar g(\mathrm{II}(X,Z),\mathrm{II}(Y,W))$; for a hypersurface with $\bar g(\nu,\nu) = \epsilon$ the quadratic terms are $\epsilon\,[h(Y,Z)h(X,W) - h(X,Z)h(Y,W)]$.

## Worked examples

### Principal curvatures of a swim ring · working

**Problem:** A swim ring is a torus with tube radius $r = 10$ cm and centre-circle radius $R = 25$ cm. At a point of its outer circle and a point of its inner circle, halfway up the tube, find the principal curvatures with the outward normal and their product. Compare with the Gaussian curvatures that walkers on the ring measure, $+1/350$ cm$^{-2}$ and $-1/150$ cm$^{-2}$.

1. By mirror symmetry the principal directions are around the tube and around the ring's axis.
2. Around the tube, the normal section is a circle of radius $r$ bending toward the tube's centre line, away from the outward normal at both points: $\kappa = -1/r = -1/10$ cm$^{-1}$.
3. At the outer circle the outward normal points away from the axis. The circle about the axis, of radius $R + r = 35$ cm, lies in the normal plane and bends toward the axis, away from the normal: $\kappa = -1/35$ cm$^{-1}$.
4. At the inner circle the outward normal points toward the axis. The circle about the axis, of radius $R - r = 15$ cm, bends toward the axis, toward the normal: $\kappa = +1/15$ cm$^{-1}$.
5. Outer product: $(-1/10)(-1/35) = +1/350$ cm$^{-2}$. Inner product: $(-1/10)(+1/15) = -1/150$ cm$^{-2}$.

**Answer:** Outer circle: $-1/10$ and $-1/35$ cm$^{-1}$, $K = +2.86\times10^{-3}$ cm$^{-2}$. Inner circle: $-1/10$ and $+1/15$ cm$^{-1}$, $K = -6.67\times10^{-3}$ cm$^{-2}$. Both equal the walkers' values.

**Takeaway:** Two outsider numbers multiply to the one number insiders measure, and the sign of $K$ records whether the two bends go toward the same side.

## Problems

### `lampshade-bends` · working · difficulty 2 · calculation

A lampshade is a cone with its top cut off. Each straight line on it makes 30 degrees with the axis, and its rims have radii 10 cm and 20 cm. (a) At a point of the bottom rim, find both principal curvatures in size and the Gaussian curvature. (b) The shade is made from flat card without stretching. Find the shape of the card.

**Hints**

1. Around the rim, only the part of the rim circle's curvature along the surface normal counts.
2. Unrolled, the card is part of a flat ring centred on the cone's apex.

**Answer:** (a) $0$ along the straight lines and $\cos 30^\circ/(20\ \text{cm}) = 0.0433$ cm$^{-1}$ around the rim, a normal-section radius of 23.1 cm, so $K = 0$. (b) Half of a flat ring with radii 20 cm and 40 cm.

**Must contain:** Zero along the straight lines, cos 30 degrees over 20 centimetres around the rim; The card is half of a flat ring between 20 and 40 centimetres

**Numeric:** radius of the normal section around the bottom rim = 23.09 cm (magnitude, ±2%); angle spanned by the flat card = 180 deg (magnitude, ±2)

**Solution**

1. Each straight line of the cone lies in the surface, so the normal curvature along it is $0$; for a surface of revolution the lines through the apex and the rim circles give the principal directions.
2. The rim circle has curvature $1/(20\ \text{cm})$, pointing toward the axis. The surface normal is perpendicular to the straight line, which makes $30^\circ$ with the axis, so the normal makes $30^\circ$ with the horizontal direction toward the axis.
3. The normal curvature is the component of the rim's curvature along the normal: $\cos 30^\circ/(20\ \text{cm}) = 0.0433$ cm$^{-1}$, radius $23.1$ cm. The rest of the rim's curvature is sideways steering along the surface.
4. $K = 0 \times 0.0433 = 0$, so the card can be flat.
5. Along a straight line the rims lie $20/\sin 30^\circ = 40$ cm and $10/\sin 30^\circ = 20$ cm from the apex. The bottom rim, $2\pi \times 20 = 125.7$ cm long, is an arc of radius 40 cm spanning $125.7/40 = \pi$ rad, which is $180^\circ$.

**Targets:** `bent-means-intrinsically-curved`

### `compact-surface-has-a-dome-point` · formal · difficulty 2 · proof

Let S be a compact smooth surface in three-dimensional Euclidean space. Prove that S has a point where its Gaussian curvature is positive. Conclude that no flat torus is smoothly and isometrically embedded in that space.

**Hints**

1. Take a point $p$ of $S$ farthest from the origin.
2. Differentiate $|\gamma(s)|^2$ twice along a unit-speed curve in $S$ through $p$.

**Answer:** At a farthest point $p$, at distance $r$, every normal curvature with the outward normal $p/r$ is at most $-1/r$, so $K = \kappa_1\kappa_2 \ge 1/r^2 > 0$. A flat torus has $K = 0$ everywhere, so it has no such embedding.

**Must contain:** At a farthest point every normal curvature is at most minus one over r; So K is at least one over r squared there

**Solution**

1. $|x|^2$ is continuous on compact $S$, so it attains a maximum $r^2 > 0$ at some $p$; its gradient $2p$ is then normal to $S$, so $\nu = p/r$ is a unit normal.
2. Let $\gamma$ be a unit-speed curve in $S$ with $\gamma(0) = p$ and $\gamma'(0) = t$. Since $|\gamma|^2$ has a maximum at $0$, $\tfrac{d^2}{ds^2}|\gamma|^2 = 2(|\gamma'|^2 + \gamma\cdot\gamma'') \le 0$ there, so $p\cdot\gamma''(0) \le -1$.
3. The normal part of $\gamma''(0)$ is $\kappa(t)\,\nu$, and its tangential part is orthogonal to $p$, so $p\cdot\gamma''(0) = r\,\kappa(t)$. Hence $\kappa(t) \le -1/r$ for every unit tangent $t$.
4. Both principal curvatures are then at most $-1/r$, so $K = \kappa_1\kappa_2 \ge 1/r^2 > 0$.
5. A smooth isometric embedding preserves $K$ by the theorema egregium. A flat torus is compact with $K = 0$ everywhere, so its image would contradict the result.

**Targets:** `every-geometry-fits-in-space`

## Observations

- **The curvature of space and the expansion rate, from the Planck satellite's maps of the cosmic microwave background** (measured, working). In the slicing by cosmic time, $\Omega_K$ measures the intrinsic curvature of space at one moment, and $H_0$ fixes the extrinsic curvature of that slice within spacetime, whose principal values have size $H_0/c$. Space is intrinsically flat within errors while its slice is extrinsically curved. *Numbers:* $\Omega_K = 0.001 \pm 0.002$ with baryon acoustic oscillation data, so for $|\Omega_K| \le 0.005$ any intrinsic radius of curvature exceeds 60 Gpc. $H_0 = 67.4 \pm 0.5$ km s$^{-1}$ Mpc$^{-1}$ in the standard model, so $c/H_0 = 4.45$ Gpc. *Reference:* N. Aghanim, Y. Akrami, M. Ashdown, J. Aumont and others (2020), *Planck 2018 results. VI. Cosmological parameters*, Astronomy & Astrophysics 641, A6, doi:10.1051/0004-6361/201833910

## Teaching arc

1. **Two ants, two answers** (entry). Ask the opening question, then run the ring test on the poster and the ball. *Why:* Measuring splits curved into two meanings. *Predict:* Will the ant's ring on the rolled poster come out shorter than on the flat poster? *Visual:* [[paper-rolled-into-a-tube-and-a-cone]] *Uses:* `ways_in/two-meanings-of-curved`, `checks/lampshade-for-an-ant`
2. **Straighten a wire, curl a slice** (entry). Straighten a wire, then curl a pizza slice. *Why:* The wire shows why intrinsic curvature needs two directions; the slice shows what bending cannot do. *Predict:* Curl the crust into a U: will the tip droop? *Uses:* `ways_in/a-wire-hides-its-bend`, `ways_in/curl-a-slice-and-it-stops-drooping`, `checks/curl-the-slice`
3. **Multiply the bends** (working). Compute principal curvatures and their product, then read the cosmic expansion as extrinsic curvature. *Why:* The product survives bending; the sum does not. *Uses:* `ways_in/two-bends-and-their-product`, `worked_examples/swim-ring-product`, `ways_in/flat-space-in-curved-spacetime`, `checks/flat-yet-expanding`

## Misconceptions

### “A rolled-up poster is curved in the same way a ball is.” · entry · `bent-means-intrinsically-curved`

- **Why it is tempting:** Both look bent in a room.
- **What is true:** Rolling stretches nothing, so an ant on the paper measures a flat plain's rings. Only the ball's curving shows in her measurements.
- **Exposed by:** `checks/lampshade-for-an-ant`

### “A tiny creature in a bent wire could find the bend by measuring along it.” · entry · `wire-can-sense-its-bend`

- **Why it is tempting:** A bent wire looks very different from a straight one.
- **What is true:** Straightening without stretching keeps every length along the wire, and lengths are all she can measure.
- **Exposed by:** `checks/bead-on-a-wavy-wire`

### “Paper can be bent into any smooth shape without stretching.” · entry · `sheet-bends-any-way`

- **Why it is tempting:** Paper bends so easily one way that it seems to bend every way.
- **What is true:** Away from creases and a cone's sharp point, a sheet that cannot stretch bends toward only one face at each spot, keeping an unbent line through that spot. That is why a curled slice stops drooping.
- **Exposed by:** `checks/curl-the-slice`

### “Bends toward one face along one line and toward the other face along another cancel, so the surface counts as flat.” · entry · `opposite-bends-cancel`

- **Why it is tempting:** Equal bends each way seem to add up to nothing.
- **What is true:** Bends toward opposite faces at one spot make the saddle pattern, which has intrinsic curvature, so no flat sheet takes that shape without stretching.
- **Exposed by:** `checks/saddle-shaped-crisp`

### “Extrinsic curvature means bending into an extra dimension, so it plays no part in real physics.” · working · `extrinsic-needs-an-extra-dimension`

- **Why it is tempting:** The first examples are surfaces bent in a room, and nothing surrounds spacetime.
- **What is true:** Space at one moment sits inside spacetime, and its extrinsic curvature there is the expansion.
- **Exposed by:** `checks/flat-yet-expanding`

### “Every intrinsic geometry of a surface can be built as a smooth surface in ordinary space.” · formal · `every-geometry-fits-in-space`

- **Why it is tempting:** Every surface we handle sits in ordinary space.
- **What is true:** Compact surfaces in ordinary space have a point of positive curvature, so a flat torus has a smooth isometric embedding only in four or more dimensions.
- **Exposed by:** `checks/flat-torus-homes`

### “If space at each moment is intrinsically flat, spacetime is flat.” · formal · `flat-space-means-flat-spacetime`

- **Why it is tempting:** Flat slices seem to leave nowhere for curvature to hide.
- **What is true:** The Gauss equation adds products of the slices' extrinsic curvature, so flat expanding slices give tangent planes spacetime curvature H squared.
- **Exposed by:** `checks/flat-slice-curved-spacetime`

## Checks

1. **Entry · predict** `checks/lampshade-for-an-ant`. A lampshade is made of flat card, bent without stretching into a cone with its top cut off. Its top and bottom rims are 20 centimetres apart along the card. An ant stands on the card halfway between the rims. She walks straight out 5 centimetres in many directions all around, and measures the ring of marks along the card. How long is the ring? In which meaning of curved, if either, is the lampshade curved?
   - **Hints:** Did bending change any length along the card?
   - **Answer:** About 31.4 centimetres. Bending did not stretch the card, so every length along it matches the flat card, including her walks and her ring. On the flat card the ring is 6.28 times 5 centimetres, about 31.4 centimetres, so on the shade it is the same. She therefore finds no intrinsic curvature. Seen from the room, the shade is bent, so it has extrinsic curvature.
   - **Must contain:** About 31.4 centimetres, as on flat card; Extrinsic curvature yes, intrinsic curvature no
   - **Numeric:** ring length = 31.4 cm (magnitude, ±3%)
   - **Targets:** `bent-means-intrinsically-curved`
   - **Visual:** [[paper-rolled-into-a-tube-and-a-cone]]
2. **Entry · evaluate-claim** `checks/bead-on-a-wavy-wire`. A bead-sized creature lives on a wavy coat-hanger wire with free ends, and can only slide along it. Her only tool is a tape measure laid along the wire. Two paint dots are 30 centimetres apart along the wire. She says: "If someone pulled my wire straight without stretching it, my measurements would change." Is she right?
   - **Hints:** What is the only kind of thing she can measure?
   - **Answer:** No. Straightening without stretching keeps every length along the wire, so the dots stay 30 centimetres apart. Lengths along the wire are all she can measure, so her measurements come out the same, wavy or straight. A wire can be bent, seen from the room, but never has intrinsic curvature.
   - **Must contain:** Every length along the wire stays the same; A line has no intrinsic curvature
   - **Numeric:** distance between the dots along the straightened wire = 30 cm (magnitude, ±0.5)
   - **Targets:** `wire-can-sense-its-bend`
3. **Entry · predict** `checks/curl-the-slice`. You hold a pizza slice, 25 centimetres long, by its crust, topping side facing the ceiling, without curling it, and its tip droops. You pinch the crust so the slice curls into a U across its width, all the way to the tip, with the U's sides rising. Treat the dough as a sheet that bends but never stretches. Does the tip droop now? Why?
   - **Hints:** Which line through a spot does the U leave unbent?
   - **Answer:** No, it stops drooping. Away from creases and a cone's sharp point, a sheet that never stretches bends toward only one face at each spot, and keeps an unbent line through that spot. The U bends every line through a spot toward the topping face, except the crust-to-tip line. Drooping would bend that line toward the bottom face. The slice would then bend toward both faces, the saddle pattern, which the sheet cannot take. So the crust-to-tip line stays unbent, and the tip sticks out.
   - **Must contain:** The tip stops drooping; The U leaves only the crust-to-tip line unbent, and the sheet must keep one
   - **Targets:** `sheet-bends-any-way`
4. **Entry · evaluate-claim** `checks/saddle-shaped-crisp`. A potato crisp 5 centimetres across is shaped like a saddle. Through its middle spot, it bends toward one face along one line, and toward the other face along the line at a right angle. A friend says: "The bends cancel, so an ant on the crisp would measure it like a flat sheet." Is the friend right?
   - **Hints:** Could paper be pressed snugly onto the crisp?
   - **Answer:** No. Bends toward opposite faces at one spot are the saddle pattern. Any spot that bends in the saddle pattern has intrinsic curvature, so the ant's measurements there differ from a flat sheet's. Walkers who start side by side at the middle spot spread apart, as near a swim ring's hole. The paper test agrees: a flat sheet pressed snugly onto the crisp creases, because fitting would need it to stretch.
   - **Must contain:** No: bends toward opposite faces are the saddle pattern; Any saddle-pattern spot has intrinsic curvature, so walkers spread apart
   - **Targets:** `opposite-bends-cancel`
5. **Working · evaluate-claim** `checks/flat-yet-expanding`. A student argues: "Microwave-background data show space is flat, so space at one moment has no curvature of any kind, and the expansion is not geometry." Evaluate this, and find the size of the curvature it misses for a Hubble constant of 67.4 kilometres per second per megaparsec.
   - **Hints:** Which curvature does a triangle laid out within space measure?
   - **Answer:** The data give $\Omega_K \approx 0$: within errors, a constant-time slice has zero intrinsic curvature, the curvature read from lengths and angles within it. Pushed along its unit normal by proper time $d\tau$, the slice's distances grow by $1 + H\,d\tau$. So it has extrinsic curvature with principal values of size $H_0/c = 7.29\times10^{-27}$ m$^{-1}$, radius $c/H_0 = 4.45$ Gpc. That extrinsic curvature is the expansion.
   - **Must contain:** Flat means zero intrinsic curvature of the slice; The expansion is extrinsic curvature of size H over c, radius 4.45 gigaparsecs
   - **Numeric:** radius c over H0 = 4.45 Gpc (magnitude, ±2%)
   - **Targets:** `extrinsic-needs-an-extra-dimension`
6. **Formal · explain** `checks/flat-torus-homes`. A square flat torus is a square with opposite sides glued, with the flat metric. Does it have a smooth isometric embedding in three-dimensional Euclidean space? In four-dimensional Euclidean space? If so, is its second fundamental form zero?
   - **Answer:** Not in $\mathbb R^3$: a compact smooth surface there has a point with $K > 0$, and the flat torus has $K = 0$. For side $2\pi$, $(u,v) \mapsto (\cos u, \sin u, \cos v, \sin v)$ embeds it isometrically in $\mathbb R^4$. There $\mathrm{II}(\partial_u,\partial_u) = -(\cos u, \sin u, 0, 0)$ and $\mathrm{II}(\partial_v,\partial_v) = -(0, 0, \cos v, \sin v)$ are orthogonal unit normals and $\mathrm{II}(\partial_u,\partial_v) = 0$. So $\mathrm{II} \neq 0$, while the Gauss equation gives $K = 0$.
   - **Must contain:** None in three dimensions: compact surfaces there have a point of positive curvature; In four dimensions the embedding is isometric with nonzero second fundamental form
   - **Targets:** `every-geometry-fits-in-space`
7. **Formal · numeric** `checks/flat-slice-curved-spacetime`. In the spatially flat expanding universe, sliced at constant cosmic time, use the Gauss equation to find the spacetime sectional curvature of a plane tangent to a slice. Evaluate it today for a Hubble constant of 67.4 kilometres per second per megaparsec.
   - **Answer:** The normal is timelike, $\epsilon = -1$, so for orthonormal $X, Y$ in the slice $g(R(X,Y)Y,X) = \bar g(\bar R(X,Y)Y,X) - [h(X,X)h(Y,Y) - h(X,Y)^2]$. The slice is flat, so the left side is $0$, and $h = \pm(H/c)\,g$ makes the bracket $H^2/c^2$. So the sectional curvature is $+H^2/c^2 = 5.31\times10^{-53}$ m$^{-2}$ today, matching $R_{\hat x\hat y\hat x\hat y} = \dot a^2/(a^2c^2)$.
   - **Must contain:** A timelike normal flips the quadratic terms; Plus H squared over c squared, about 5.3 times ten to the minus 53 per square metre
   - **Numeric:** sectional curvature of a plane tangent to the slice = 5.31e-53 m^-2 (signed, ±3%)
   - **Targets:** `flat-space-means-flat-spacetime`

## Notation traps

| Issue | Course choice | Variants you will meet |
| --- | --- | --- |
| Signs of principal curvatures, and what the letter K names | $\kappa_1, \kappa_2$ are signed relative to a chosen unit normal; $K = \kappa_1\kappa_2$ is not, and a sphere has $K = +1/a^2$ as in the course conventions. | Some texts give a sphere positive principal curvatures. Relativity texts often write $K_{ij}$, with either overall sign, for a slice's extrinsic curvature and $K$ for its trace. |

## Visuals

- ★ [[paper-rolled-into-a-tube-and-a-cone]] (flagship): Rolling keeps every length along the sheet while its bends change. *Sketch:* A grid sheet rolls into a tube or a cone while grid lengths stay fixed. Add a ring-test readout that never changes, readouts of both bends and their product, and a ball that the sheet covers only by tearing.
- [[best-fit-circle-along-a-bend]] (supporting): A wire pulled straight keeps every length along it. *Sketch:* A reshapable wire with paint dots; a button pulls it straight while the spacings along the wire stay fixed.
- [[carry-an-arrow-around-a-loop]] (supporting): The tube and its unrolled view: the arrow test ignores bending.

## Tutor moves

**Open with**

- Roll a poster into a tube and hold it next to a ball. One ant lives on the paper and another lives on the ball, and each measures only along her own surface. Would their measurements tell them the same thing about curving? *(prediction)*

**If the learner is stuck**

- *The learner cannot see which lines through a spot bend.* → Lay a ruler against the outside of a paper U, through one spot, in several directions: it lies snugly along the sheet in one direction only. On a ball it lies snugly along none. *Uses:* `ways_in/curl-a-slice-and-it-stops-drooping`

**Common questions**

- *Is the curving of space and time in gravity the bent kind or the measured kind?* (entry) The measured kind. Einstein's theory describes gravity through measurements made within space and time, and it needs nothing outside them. The bent kind still turns up in one place. All of space at one instant, timed by clocks that ride along with the galaxies, is one slice of space and time, and that slice can be bent within them. For our universe, that bending shows up as the distances between galaxies growing. *Uses:* `ways_in/two-meanings-of-curved`, `ways_in/flat-space-in-curved-spacetime`

**Switching levels**

- To working when: asks how sharply a surface bends; uses radii of best-fit circles. Go to principal curvatures, their product and the swim-ring example. *Uses:* `ways_in/two-bends-and-their-product`, `worked_examples/swim-ring-product`
- To formal when: knows connections and asks why the product is intrinsic. Derive the Gauss equation and apply it to the flat torus. *Uses:* `derivations/gauss-equation-from-splitting`, `checks/flat-torus-homes`

**Pronunciations:** theorema egregium → thee-oh-RAY-muh eh-GRAY-gee-um; Beez–Killing → BAYTS KILL-ing; de Sitter → duh SIT-er

## History

- **Carl Friedrich Gauss (1827).** Proved that the product of a surface's principal curvatures is fixed by lengths measured along it, so bending without stretching cannot change it. Carl Friedrich Gauss (1828), *Disquisitiones generales circa superficies curvas*, Commentationes Societatis Regiae Scientiarum Gottingensis Recentiores 6, 99–146

## Review: novice

**Verdict:** fixed (2026-09-13, revision 6)

**Retell attempt:** Second novice pass, reading revision 4. Curved means two different things. Roll a poster up and it looks bent from the room, but an ant who measures only along the paper still gets a ring 6.28 times the distance she walked, exactly as on the flat poster, so nothing changed for her. That outside kind is extrinsic curvature. On a ball her ring comes out short, so she can tell from inside, and that is intrinsic curvature; a ball has both. On Earth a ring paced out a kilometre from its centre is short by only about 0.026 millimetres, so nobody notices. A bead creature on a wire can never find the bend, because you can pull the wire straight without stretching it and every length along it stays the same, and lengths are all she has; a hoop is the same story. A surface gives more, because its ant can compare the walk out with the ring. In the pizza part a sheet has a topping face and a bottom face, and through any spot you can draw lines like spokes, and each line either bends toward a face or stays unbent: ball spots bend every line toward the same face, saddle spots bend toward both faces, poster spots bend all but one line. Paper can only do the poster one, so curling the crust into a U uses up the bending everywhere except along the crust-to-tip line, and drooping would make that spot a saddle, which paper cannot be. Three places stopped me. I was told to hold the slice flat and then that the tip droops, which sounded like a contradiction. The rule was stated away from creases and sharp tips, while the whole question is about the slice's tip, so I could not tell whether the rule covered the place I needed it. And when the tutor said all of space at one instant, I wondered: one instant by whose clock?

First novice pass, reading revision 1. The word curved means two things. If you roll a poster into a tube it looks bent from the room, but an ant measuring rings on the paper still gets 6.28 times, like on the flat poster, so for her nothing is curved. That outside kind is extrinsic. On a ball her rings come out short, so she can tell, and that is intrinsic; a ball has both. A bead on a wavy wire can't tell it's bent because you can pull the wire straight and the lengths stay the same, so a wire only has the outside kind. I wasn't sure what happens if the wire is a closed ring, or why a surface having a 'second direction' matters, since she can compare two lengths on a wire too. The pizza part lost me: I didn't know which 'side' a sheet bends toward, or why a sheet can only bend like a poster just because a ball and a saddle have intrinsic curvature. I got that curling the crust into a U stops the tip drooping because one line has to stay unbent. On Earth the short ring is less than a hair over a kilometre.

**Stumbles (37)**

- “Bending seen only from the space around a surface is extrinsic curvature.”: 'Only' reads as 'bending that can be seen only from outside', which suggests a ball's visible bend is not extrinsic curvature, although the way says a ball has both.
- “finds every length unchanged”: Unchanged compared with what? The ant was never told she had measured the flat poster first.
- “A ring that fits on the paper comes out 6.28 times the distance walked, just as on the flat poster.”: 'Fits on the paper' names no rule, and a teenager's first what-if, a long walk that wraps around the tube or runs off the rolled poster's edge, breaks it. The step from 'lengths are kept' to 'her straight walks and ring match the flat poster's' is also left implicit.
- “On a ball as big as Earth, the ring test barely shows.”: 'Barely shows' has no object: shows what?
- “Imagine a creature the size of a bead who lives in the wire”: 'In the wire' pictures a creature inside the metal.
- “So every measurement she can make comes out the same on the wavy wire and on the straight wire.”: First what-if: sliding fast round a bend, she would feel pushed sideways, like a passenger in a turning car. 'Every measurement' is false unless her tools are limited.
- “A wire, or any line, can have extrinsic curvature but never intrinsic curvature.”: Intrinsic curvature was defined only for surfaces, so applying it to a wire is a step taken on trust; 'any line' also suggests a line drawn on paper.
- “A wire can be pulled straight without stretching, so it never has intrinsic curvature”: False first what-if: a wire whose ends are joined into a hoop cannot be pulled straight. The answer sat only in simplifies, which a reader may never see.
- “a surface can, because its rings can disagree with a flat plain's.”: Ambiguous: 'a surface can' reads as 'a surface can be pulled straight'.
- “That is why bending can never hide a ball's intrinsic curvature, or create any.”: Reread: 'that' and 'any' need unpacking, and 'hide' is a new metaphor for the ring comparison.
- “A wire has no second direction for a ring, so it has nothing to compare.”: Missing link: she can compare two lengths along a wire too, so why does that not count?
- “Around a swim ring's hole, which is saddle-shaped, walkers who start side by side ... spread apart.”: The swim ring's hole was never called saddle-shaped in the prerequisite, and the recap asks the reader to accept it with no picture.
- “On a ball, it bends along every line through the spot, all toward the same side.”: 'Side' of a sheet is undefined and reads as left or right. The whole way depends on it.
- “Picture every line you could draw along the sheet through that spot.”: What it means for a sheet to 'bend along a line' is never shown, and lines drawn on a curved surface could wiggle.
- “A bent surface can bend in three ways at a spot.”: False what-if: a bent surface can have a spot where it does not bend at all.
- “On a rolled poster, it bends toward one side along some lines, but along one line, running down the tube, it does not bend at all.”: 'Some lines' undersells it: every line except one bends. 'Down the tube' is a direction without a reference.
- “A ball and a saddle both have intrinsic curvature. A sheet bent without stretching never gains intrinsic curvature. So a sheet can only bend like the rolled poster.”: The biggest gap in the note: the conclusion needs every spot with the ball or saddle pattern to have intrinsic curvature, not just balls and saddles as whole objects. The claim is surprising and had no reason or test near it.
- “Through every spot, it bends toward one side only, and it keeps at least one line along which it does not bend.”: A folded crease and a paper cone's tip break the rule; the explanation scoped only the takeaway.
- “That line must stay unbent, so the tip cannot droop.”: Missing link: why must that line stay unbent? Also a false what-if: a soggy slice still droops.
- “Hold a slice of pizza flat by its crust. ... curls into a U across its width.”: Which way does the U open? The faces argument needs the topping face and the U's direction fixed.
- “So curling it one way stops it bending the other way.”: 'One way' and 'the other way' could mean faces or directions: the note uses both.
- “An ant on the card walks straight out 5 centimetres from a spot in its middle”: The middle of a lampshade could be the empty centre, and nothing says the 5-centimetre walks stay on the card.
- “Is the lampshade curved?”: Uses the very word the note splits into two meanings, so either answer could be marked wrong.
- “About 31 centimetres, 6.28 times 5.”: The answer states the number before its reason, and 31 does not match 6.28 times 5.
- “my measurements would show it.”: 'It' could be the wire, the bend or the pulling; the check also did not limit her tools.
- “Drooping would bend that line too, so the slice would bend along every line or toward both sides.”: Reread; and with the tip drooping toward the bottom face, only the 'both sides' case applies.
- “The crisp bends toward opposite sides, so no flat sheet can take its shape without stretching ... an ant would find walkers who start side by side spreading apart.”: Missing link: that paper cannot fit the crisp does not show what an ant on the crisp measures.
- “Would an ant living on the paper and an ant living on the ball find their worlds curved in the same way?”: It presumes both worlds are curved, and does not say the ants only measure.
- “The bent kind appears for space at one moment, which sits within space and time.”: 'Space sits within space and time' reads as a contradiction; 'nothing sits outside to see them bent' also claims more than the theory needs.
- “Lay a ruler through one spot of a paper U in several directions: it lies along the sheet in one direction only.”: Inside a U, a ruler laid across touches both rims, so the test cannot be followed there.
- “Away from creases and sharp tips, a sheet bent without stretching bends toward only one face at each spot, and keeps an unbent line through that spot.”: One word in two senses (also in the way's explanation). The excluded 'sharp tips' are places where a sheet is pinched to a point, as at the top of a paper cone, but 'the tip' in this same way is the pizza slice's pointed end, and the whole argument is applied there. A careful reader cannot tell whether the rule covers the very spot it is used on.
- “Hold a slice of pizza by its crust, topping side facing the ceiling, and keep it flat. The tip droops.”: Reread: 'keep it flat' is an instruction the next sentence says fails, so the two sentences read as a contradiction. The intended meaning is 'do not curl it'.
- “You hold a pizza slice, 25 centimetres long, flat by its crust, topping side facing the ceiling, and its tip droops.”: The same contradiction in the check's starting state: 'flat' and 'droops' describe the same slice at the same moment, so the starting state is ambiguous.
- “All of space at one instant is one slice of space and time, and that slice can be bent within them.”: A 'same moment' with no clock named. Which places count as being at one instant is a choice, and the note's working rung makes that choice (clocks carried by galaxies moving with the average cosmic flow) while the spoken entry answer hides it.
- “Curving that shows up in measurements made along a surface, without leaving it. A ball has it. A rolled-up poster does not.”: The glossary defines intrinsic curvature for surfaces only, while the entry way 'A wire hides its bend' applies the term to a wire and denies it there. A reader who checks the glossary after that way finds the word defined for something else.
- “Around a swim ring's hole, walkers who start side by side, facing the same way, spread apart.”: A direction without its reference. The prerequisite's rule fixes which way the two walkers face relative to the line between them; the recap drops that, so a reader could picture them one behind the other, or facing along their gap.
- “She runs the ring test on a small ring, well away from the paper's edges.”: Circular wording: the ring test was defined as walking out and then measuring the ring of marks, so the ring is its result, not something you run the test on. The scope that matters is that her walks are short.

**Fixes**

- Compared the retelling with the takeaways: 'Two meanings of curved' came back whole; 'A wire hides its bend' came back without the hoop case or the reason a surface differs; 'Curl a slice and it stops drooping' came back without its central step. The fixes target those gaps.
- Pizza way rebuilt around one chain: two named faces, spoke lines as straight-walk paths with a rain-gutter example, three patterns scoped to spots that bend at all, the saddle pattern tied to the swim ring's hole with face-based directions, the explicit rule that every ball- or saddle-pattern spot has intrinsic curvature (with the orange and crisp paper test beside it), and 'away from creases and sharp tips' in the explanation, not only in the takeaway.
- Replaced 'side' of a sheet with 'face' everywhere at entry: the pizza way, both slice and crisp checks, and the misconceptions sheet-bends-any-way and opposite-bends-cancel.
- Wire way: the creature's only tool is a tape measure (so the sideways push of a fast slide is excluded), intrinsic curvature is stated for a wire before it is denied, the hoop case moved from simplifies into the explanation (simplifies is now null), and the reason a wire cannot disagree with a straight wire replaces 'no second direction'.
- Poster way and summary: small ring away from the edges, an explicit step from 'lengths kept' to 'walks and ring match the unrolled poster', and the recap now restates that a path that never steers on a rolled sheet never steers unrolled.
- Entry checks: the lampshade gives rim spacing and the ant's spot, asks which meaning of curved applies, and gives the reason before 31.4 centimetres; the bead check limits her tools and removes the ambiguous 'it'; the slice check fixes the topping face, the U's direction and its reach, and states the saddle-pattern step; the crisp check links saddle pattern to intrinsic curvature before the paper test.
- Tutor: opening question no longer presumes both worlds are curved; the entry common question about gravity no longer says space sits within space and time; the if-stuck ruler test is done on the outside of the U.
- Ladder: the working way 'Two bends and their product' now says what rho and C are in the ring-test series, uses 'normal curvature' for the slice argument, and says 'droop' rather than 'sag', matching the entry word. First sentences of the working and formal ways already name the ways they continue; kinds are picture, contrast, picture, calculation, operational, structure.
- Budget: entry explanations rose from 727 to about 1,080 words, within the 10% review allowance of the 1,000 cap, all for recorded stumble fixes. Nothing was compressed; one repeated sentence in the wire way was merged into its neighbour. Tutoring rose to about 1,890, under its 2,200 cap.
- Bumped the revision to 2.
- SECOND NOVICE PASS (independent re-read of the whole entry rung at revision 4; the entries above it record the first pass, which read revision 1). Compared the retelling with the entry takeaways: 'Two meanings of curved' and 'A wire hides its bend' came back whole, including the hoop and the Earth number; 'Curl a slice and it stops drooping' came back whole except for its scope phrase, which the reader could not apply to the slice's own tip. Seven stumbles, all at entry, all recorded above.
- Replaced the scope 'away from creases and sharp tips' with 'away from creases and a cone's sharp point' in the explanation and takeaway of 'Curl a slice and it stops drooping', so that the excluded places are no longer named by the same word as the pizza slice's tip. The excluded set is unchanged: creases and the point where a sheet is pinched together.
- Removed the flat-yet-drooping contradiction from the slice's starting state, in the way's opening sentence and in the check curl-the-slice: the reader is now told not to curl the slice, rather than to keep it flat.
- Entry common question 'which-kind-for-gravity': the instant that defines the slice is now timed by clocks riding along with the galaxies, matching the working way's cosmic-time slicing, which the spoken answer had left unsaid.
- Glossary: intrinsic curvature now covers a line as well as a surface, and says a wire has none, so the term is defined for everything the entry ways apply it to.
- Recap of 'Curl a slice and it stops drooping': the spreading walkers now start the way the prerequisite defines, side by side and facing the same way at a right angle to the line between them.
- 'Two meanings of curved': the ant now runs the ring test with short walks rather than 'on a small ring', which keeps the scope that excludes walks wrapping round the tube or running off the paper.
- Budget: entry explanations 1096 to 1097 words (cap 1000, inside the 10% review allowance), way extras 521 to 535 of 650, tutoring 1913 to 1932 of 2200, total 5910 of 7000. Nothing was compressed or dropped. Revision bumped to 5; status back to novice-reviewed.

**Concerns**

- The physics reviewer should check three new entry claims: that at a spot where a surface bends at all the patterns are exactly ball, saddle or rolled-poster (elliptic, hyperbolic, parabolic); that the part of a swim ring beside its hole bends toward the air inside the ring around the tube and toward the hole around the hole; and that a U-curled slice's droop toward the bottom face is the saddle case.
- The entry rule 'any spot that bends like a ball or a saddle has intrinsic curvature' is taken on trust at entry ('a reason that needs more mathematics'); the working rung also takes K = kappa1 kappa2 on trust until the formal Gauss equation. A beginner has only the paper test as support.
- Entry explanations now sit about 8% over the 1,000-word cap, and way extras at 520 of 650. A later edit that adds entry text must cut elsewhere, for example the Earth ring number in 'Two meanings of curved', which repeats a prerequisite's number.
- The working way 'Flat space that bends inside spacetime' uses four-velocity and proper time without a bridge, and assumes metric-tensor, which is not a direct prerequisite; the validator accepts it through a prerequisite chain. Worth a look by an editor.
- The proposed visual sketches (paper-rolled-into-a-tube-and-a-cone, best-fit-circle-along-a-bend) were not edited; when built, their narration should use 'face' rather than 'side' and 'droop' rather than 'sag'.
- SECOND NOVICE PASS. Seven entry strings changed, all wording rather than claims, so they need a physics diff check before the note returns to physics-reviewed. The only one that touches a physical statement is the scope phrase 'away from creases and a cone's sharp point', which is meant to exclude exactly what 'sharp tips' excluded, and the cosmic-time clocks added to the spoken gravity answer.
- 'Curl a slice and it stops drooping' remains the heaviest entry way: faces, spoke lines, three patterns, the rule that ball- and saddle-pattern spots have intrinsic curvature, and the droop argument. It is one chain answering one question, and the retelling came back whole, so I did not split it; but if a later pass finds beginners dropping the chain, the three patterns deserve their own entry way.
- The entry rung still has only one everyday number, the 0.026 millimetre shortfall on Earth, and it repeats a number from a prerequisite. With entry explanations at 1097 of 1000 words there is no room for a second one without a cut, so I left it.

**Re-read** (2026-09-13, revision 4): 5 stumbles in 9 changed passages

- “bends toward one face only at each spot, and keeps an unbent line through it”: 'It' could mean the sheet or the spot, and 'one face only at each spot' can be misread as 'bends only at spots'. Reread in the takeaway of 'Curl a slice and it stops drooping', the curl-the-slice answer and the sheet-bends-any-way correction.
- “mirror symmetry makes the directions across the width and along the slice principal”: Working reader: whose mirror symmetry, across what? 'Principal' as a trailing adjective reads oddly.
- “the normal curvature across the width is not zero, so the normal curvature along the centre line is zero”: Step taken on trust: the 'so' relies on the product K = 0 from two sentences before, without saying so.
- “Nearby supernovae with distances calibrated by Cepheid stars give about 73”: Working reader may not know Cepheids are variable stars used as distance markers, and '73' has no unit.
- “zero intrinsic curvature, within errors, of a constant-time slice, from lengths and angles within it”: Chain of commas after the physics insert; which noun 'within errors' and 'from lengths and angles' attach to is unclear on first reading.
- Fix: Applied all five rewrites as recorded; no claim, number, condition or sign changed.
- Fix: Checked and left unchanged: the wire way's hoop sentence, the swim-ring 'air sealed inside the tube' sentence, the opposite-bends-cancel correction, and the four-velocity divided by c.
- Fix: Nothing dropped; the entry explanations total is unchanged (edits touched a takeaway, a check answer, a correction and working text).

**Re-read** (2026-09-13, revision 6): 2 stumbles in 2 changed passages

- “Away from creases and a cone's sharp point, a sheet that never stretches bends toward only one face at each spot, and keeps an unbent line through that spot.”: Reread once. The question is about a pizza slice, and a cone arrives in the answer's second sentence with nothing to picture: the entry rung names a cone's sharp point only as a place the rule fails, and never lets the reader make one. So the beginner meets two exceptions before the rule they need, and has to decide whether the slice's own tip is one of them.
- “Away from creases and a cone's sharp point, a sheet that cannot stretch bends toward only one face at each spot, keeping an unbent line through that spot.”: The tutor speaks this to a learner who has just said paper bends any way. Spoken, the first eight words are exceptions, so the correction itself arrives late, and a listener cannot look back the way a reader can.
- Fix: No fix applied, and no learner-visible text changed. Both stumbles have the same root, and every rewrite that stays inside these two strings costs more than it gains: the same rule is taught in the same words in four places, two of them in the way 'Curl a slice and it stops drooping', which this re-read's diff does not cover. Rewording two of the four would leave a learner meeting the rule twice in two shapes.
- Fix: Rewrites tried and rejected inside the two strings: moving the scope after the rule dangles it ('keeps an unbent line through that spot, away from creases and a cone's sharp point' reads as where the line is); 'except at creases' collides with the answer's later 'except the crust-to-tip line', which would use one word in two senses; splitting the misconception's correction into rule, exceptions and slice would make three sentences, one past the correction's cap.
- Fix: Checked and left unchanged in both strings: sentence lengths (30 and 28 words, inside the 32-word limit); no math, no symbols and no unit abbreviations, so the spoken correction stays speakable; 'point' is used only of a cone and 'tip' only of the slice, so neither word does double duty.
- Fix: Neither changed string is a way, so rule 17 does not apply to them, and neither shows compression: both grew by the words the scope needed, and the note's totals are unchanged at entry 1097 and total 5925.

## Review: physics

**Verdict:** fixed (2026-09-13, revision 6)

**Verification**

- Gauss equation g(R(X,Y)Z,W) = gbar(Rbar(X,Y)Z,W) + gbar(II(Y,Z),II(X,W)) - gbar(II(X,Z),II(Y,W)) with R(X,Y) = [nabla_X,nabla_Y] - nabla_[X,Y].: Re-derived each step of gauss-equation-from-splitting by hand (Weingarten step 2, tangential projection step 3, antisymmetrization with [X,Y] tangent). Compared R(X,Y) with the course Riemann row: its components are R^rho_sigma mu nu X^mu Y^nu Z^sigma, and g(R(X,Y)Y,X) matches the course sectional-curvature formula. → Correct, including the hypersurface form with epsilon h h. Unit sphere with outward normal: h = -g, S = -I, nabla_X nu = X = -SX, so K = h11 h22 - h12^2 = +1, the course sign.
- Shape operator g(SX,Y) = h(X,Y), nabla_X nu = -SX for either epsilon; II = epsilon h nu.: Differentiated gbar(nu,Y) = 0 and gbar(nu,nu) = epsilon. → Correct for both signatures of the normal.
- Normal curvature sign (positive toward the chosen normal), sphere kappa = -1/a with outward normal, K = kappa1 kappa2 = +1/a^2; C = 2 pi rho (1 - K rho^2/6).: Consistency with h = gbar(II,nu); sphere ring 2 pi a sin(rho/a) expanded. → Correct. The sign of normal curvature is fixed in the note, not in course-conventions.md; reported as a concern.
- Cylinder kappa = -1/R and 0, mean curvature -1/2R; saddle z = (x^2 - y^2)/2R gives +1/R and -1/R, K = -1/R^2.: Hand computation of normal sections. → Correct once the cylinder normal is named; added "outward normal".
- Slice argument in the working way: nonzero normal curvature across the width forces zero normal curvature along the slice.: Euler formula kappa(theta) = kappa1 cos^2 theta for a parabolic point. → False in general: if the ruling is tilted, both directions have nonzero normal curvature. True on the centre line, where mirror symmetry makes width and length principal. Rewritten with that condition; a geodesic centre line with zero normal curvature is a straight segment, so it cannot droop.
- Swim-ring worked example r = 10 cm, R = 25 cm: kappa -1/10, -1/35 outer; -1/10, +1/15 inner; K = +1/350, -1/150 cm^-2.: python; K = cos v / (r (R + r cos v)); compared with curvature/worked_examples/swim-ring-curvature. → 2.857e-3 and -6.667e-3 cm^-2, radii 18.7 and 12.2 cm. Match the curvature note.
- Problem lampshade-bends: normal curvature cos 30 deg / 20 cm = 0.0433 cm^-1, radius 23.09 cm; card is half a flat ring, radii 20 and 40 cm, 180 deg.: python; Meusnier; cross-check with the cone formula 1/(s tan psi), s = 40 cm. → 0.04330 cm^-1, 23.094 cm both ways; arc 125.66 cm over radius 40 cm = pi rad = 180 deg. Tolerances fine.
- Problem compact-surface-has-a-dome-point.: Worked every step: maximum of |x|^2, second derivative along a unit-speed curve, Meusnier decomposition. → Correct: every normal curvature <= -1/r, K >= 1/r^2.
- Check flat-torus-homes: (cos u, sin u, cos v, sin v) is isometric, II(u,u) and II(v,v) orthogonal unit normals, II(u,v) = 0, Gauss gives K = 0.: Hand differentiation. → Correct.
- Check flat-slice-curved-spacetime: sectional curvature +H^2/c^2 = 5.31e-53 m^-2 for H0 = 67.4.: Gauss with epsilon = -1, h = +-(H/c) g; cross-check with flat FLRW R_xyxy (orthonormal) = adot^2/(a^2 c^2) and with de Sitter (all planes H^2); python with 1 Mpc = 3.0857e22 m. → H0/c = 7.286e-27 m^-1, square 5.308e-53 m^-2. Sign and value correct.
- Extrinsic curvature of cosmic-time slices has principal values of size H/c; distances grow by 1 + H dtau.: K_ij = (1/2c) d g_ij/dt = (H/c) g_ij with x^0 = ct. → Correct. The unit normal is u/c under the course convention u.u = -c^2; the way now says so.
- c/H0 = 4.45 Gpc = 14.5 billion light-years; |Omega_K| <= 0.005 gives curvature radius > 60 Gpc; spatial curvature size |Omega_K| H0^2/c^2.: python; Omega_K = -k c^2/(a0^2 H0^2). → 4448 Mpc, 14.51 Gly, 62.9 Gpc. Correct.
- Planck 2018: H0 = 67.4 +- 0.5 (CMB with lensing), Omega_K = 0.001 +- 0.002 with BAO.: Planck 2018 VI parameter tables (67.36 +- 0.54; 0.0007 +- 0.0019), confirmed via WebSearch of the paper record. → Correct to the quoted rounding. DESI DR2 BAO with CMB now prefers slightly positive Omega_K at about 2 sigma; "flat within errors" still fair, see concerns.
- "Nearby supernovae give about 73".: WebSearch: SH0ES Cepheid-calibrated 73.0-73.5; CCHP JWST TRGB/JAGB-calibrated about 70. → Supernova ladders with other calibrators give about 70, so the sentence now says Cepheid-calibrated.
- Entry: Earth ring of 1 km is short by about 0.026 mm.: python: 2 pi r - 2 pi R sin(r/R), R = 6371 km. → 0.0258 mm. Correct; less than half a typical 0.07 mm hair.
- Entry check lampshade-for-an-ant: 6.28 x 5 = 31.4 cm.: python. → 31.40 (exact 31.42). Tolerance 3% fine.
- Entry claim: at a spot where a surface bends at all, the pattern is ball, saddle or rolled poster.: Classification of non-planar points by the sign of det II: elliptic, hyperbolic, parabolic. Parabolic kappa(theta) = kappa1 cos^2 theta vanishes in exactly one line direction; normal curvature of a geodesic equals its whole space curvature, so "a straight-walk line bends toward a face" is exact. → Exhaustive and each description correct.
- Entry claim: the part of a swim ring beside its hole bends toward the air in the tube around the tube, and toward the hole around the hole.: Inner-equator normal sections: tube circle centred on the tube centre line (away from the axis); circle of radius R - r centred on the axis. → Opposite faces, K < 0. Correct, but "the air inside the ring" can be read as the hole, which would make the sentence false; now "the air sealed inside the tube".
- Entry claim: the U-curled slice drooping toward the bottom face is the saddle case.: Topping face up, U sides rising: cross line concave toward the topping face; drooping centre line concave toward the bottom face. → Opposite faces, hyperbolic. Correct; drooping upward would be the ball pattern, also excluded.
- Entry: every ball- or saddle-pattern spot has intrinsic curvature; a sheet bent without stretching has only rolled-poster or unbent spots; paper pressed snugly onto an orange or crisp creases.: K = kappa1 kappa2; K = 0 for a smooth isometric image of a flat sheet; a C1 local isometry between surfaces of different K is impossible. → Correct within the stated scope away from creases and sharp tips.
- Entry wire way: lengths along a wire fit a straight wire; hoops of equal length are indistinguishable.: One-dimensional Riemannian manifolds are locally isometric to a line; closed ones of equal length are isometric. → The closing sentence "fits a straight wire" failed for a hoop (along-wire distances never exceed half its length). Now "or a round hoop if the ends are joined".
- Beez-Killing rigidity (rank of S at least 3), Bonnet existence and uniqueness, Hilbert theorem on the hyperbolic plane, no flat torus in R^3.: Checked against standard statements. → Correctly stated with their hypotheses (smooth, local rank condition, simply connected domain, complete).
- Reference: Planck Collaboration (N. Aghanim, Y. Akrami, M. Ashdown, J. Aumont, ...), 2020, Planck 2018 results. VI. Cosmological parameters, A&A 641, A6, doi 10.1051/0004-6361/201833910, arXiv 1807.06209.: WebSearch (ADS, arXiv, Princeton records). → Confirmed; verified set true.
- History: Gauss, Disquisitiones generales circa superficies curvas, presented 8 October 1827, Commentationes Societatis Regiae Scientiarum Gottingensis Recentiores 6 (1828), 99-146; proved the theorema egregium.: WebSearch (Internet Archive, bibliographic records). → Confirmed year, venue, volume and pages; contribution correctly scoped. Verified set true.
- Second physics pass (note at revision 5). Gauss equation and its hypersurface form, re-derived from scratch rather than reread.: Split bar-nabla_X Y = nabla_X Y + II(X,Y); differentiated gbar(xi,W) = 0 for xi normal; projected bar-nabla_X bar-nabla_Y Z on W; antisymmetrized using [X,Y] tangent. Wrote II = epsilon h nu from gbar(nu,nu) = epsilon and checked gbar(II(Y,Z),II(X,W)) = epsilon h(Y,Z) h(X,W). → Reproduces the note's derivation steps 1-5, its result line and the key equation exactly, including the hypersurface bracket epsilon [h(Y,Z)h(X,W) - h(X,Z)h(Y,W)]. Index-ordering cross-check: g(R(X,Y)Y,X) equals the course sectional-curvature numerator, and the unit sphere with outward normal (h = -g) gives +1.
- Weingarten relation bar-nabla_X nu = -SX with g(SX,Y) = h(X,Y), for a normal of either causal character.: gbar(nu,nu) = epsilon constant makes bar-nabla_X nu tangent; gbar(bar-nabla_X nu, Y) = X gbar(nu,Y) - gbar(nu, II(X,Y)) = -h(X,Y). → Correct with no epsilon factor, as the formal way states. Sphere of radius a, outward normal: S = -(1/a) identity, kappa = -1/a, det S = +1/a^2.
- Normal-curvature sign is used the same way in every rung of the note: positive when the normal section bends toward the chosen unit normal.: Traced the convention through the working way (sphere -1/a, cylinder -1/R, saddle +-1/R), the worked example, the lampshade problem, derivation step 6 (h = -g on the sphere) and the compact-surface proof (kappa <= -1/r at a farthest point with the outward normal). → Internally consistent everywhere, and every product K comes out with the course sign. course-conventions.md still fixes no sign here; carried as a concern.
- Entry number: a ring paced out 1 km from its centre on an Earth-sized ball is about 0.026 mm short.: python3: 2 pi rho - 2 pi R sin(rho/R) with R = 6371 km, and the series pi rho^3/(3 R^2). → 0.02580 mm both ways. 'About 0.026 millimetres' correct; the comparison with half a hair holds for a typical 0.07 mm hair.
- Working way's three examples: sphere (+1/a^2), cylinder (K = 0, mean curvature -1/2R), saddle z = (x^2 - y^2)/2R (K = -1/R^2), and C = 2 pi rho (1 - K rho^2/6 + ...).: Normal sections by hand; for the saddle also K = f_xx f_yy - f_xy^2 at a critical point; sphere ring 2 pi a sin(rho/a) expanded to third order. → All correct, including the mean curvature sign under the note's normal convention.
- Worked example swim-ring-product (r = 10 cm, R = 25 cm) and its comparison with the walkers' Gaussian curvatures.: python3 with K = cos u / (r (R + r cos u)) at u = 0 and u = pi; normal sections checked to lie in the plane spanned by the normal and the tangent (meridian circle of radius r; horizontal circles of radius 35 cm and 15 cm). → +2.857e-3 cm^-2 and -6.667e-3 cm^-2, matching the stated +1/350 and -1/150 and the quoted 2.86e-3 and -6.67e-3. Signs of the two normal curvatures at the inner circle (-1/10 and +1/15) are right because the outward normal there points toward the axis.
- Problem lampshade-bends, both parts and both numeric fields.: python3: normal curvature cos 30 deg / 20 cm, its radius, slant distances rho/sin 30 deg, arc angle 2 pi (20 cm) / 40 cm; independent check that the rim's normal and geodesic curvatures satisfy hypot(0.04330, 0.02500) = 0.05000 = 1/(20 cm). → 0.04330 cm^-1, radius 23.094 cm (field 23.09, rel_tol 0.02), slants 40 cm and 20 cm, arc 180.000 deg (field 180, abs_tol 2). K = 0. All correct.
- Problem compact-surface-has-a-dome-point, every step of the solution.: Worked the proof independently: maximum of |x|^2 on a compact surface, gradient 2p normal, second derivative of |gamma|^2 at a maximum, p . gamma''(0) = r kappa(t) since the tangential part of gamma'' is orthogonal to p. → Correct: kappa(t) <= -1/r for every unit tangent, so K >= 1/r^2 > 0, and a flat torus (compact, K = 0) has no smooth isometric embedding. The Nash-Kuiper C1 tori do not contradict it, because the statement says smooth.
- Check flat-torus-homes: (u,v) -> (cos u, sin u, cos v, sin v) is an isometry of the side-2pi flat torus, with II(du,du) and II(dv,dv) orthogonal unit normals and II(du,dv) = 0.: Differentiated the parametrization twice; checked the induced metric is du^2 + dv^2 and each second derivative is orthogonal to both tangents. → Correct, and the Gauss equation then gives K = gbar(II(Y,Y),II(X,X)) - |II(X,Y)|^2 = 0 because the two normals are orthogonal.
- Check flat-slice-curved-spacetime and the observation: sectional curvature +H^2/c^2 = 5.31e-53 m^-2, H0/c = 7.29e-27 m^-1, c/H0 = 4.45 Gpc, radius > 60 Gpc for |Omega_K| <= 0.005, spatial curvature |Omega_K| H0^2/c^2.: Gauss equation with epsilon = -1 and h = +-(H/c) g; cross-checked against flat FLRW orthonormal R_xyxy = adot^2/(a^2 c^2) and against de Sitter, where every plane has H^2. python3 with c = 299792458 m/s and 1 Mpc = 3.0857e22 m. → H0/c = 7.2860e-27 m^-1, its square 5.3086e-53 m^-2 (field 5.31e-53, rel_tol 0.03), c/H0 = 1.3725e26 m = 4.448 Gpc = 14.51 billion light-years, and 62.9 Gpc at |Omega_K| = 0.005. All correct, sign of the sectional curvature positive as claimed.
- References re-verified independently of the first pass.: WebSearch of the journal and archive records. → Planck 2018 results VI, A&A 641, A6 (2020), doi 10.1051/0004-6361/201833910, arXiv 1807.06209, first authors N. Aghanim, Y. Akrami, M. Ashdown, J. Aumont: confirmed, and its abstract quotes H0 = 67.4 +- 0.5 km/s/Mpc exactly as the note does. Gauss, Disquisitiones generales circa superficies curvas: lecture to the Gottingen society 8 October 1827, printed in Commentationes Societatis Regiae Scientiarum Gottingensis Recentiores 6 (1828), 99-146: confirmed. Both stay verified true.
- Scope of the entry rule about sheets bent without stretching, as the note now words it.: Compared the four places that state the rule: the way's explanation, the way's takeaway, the check curl-the-slice answer and the misconception sheet-bends-any-way correction. → The way and its takeaway carried 'away from creases and a cone's sharp point'; the check answer carried only 'away from creases' and the misconception correction carried no scope, so both asserted the rule at a cone's point, where a sheet has no unbent line and no single face to bend toward. Both fixed to the way's wording.

**Counterexamples tried**

- Hoop (wire with joined ends): broke "any set of lengths fits a straight wire"; fixed. Its closed topology is detectable but is not curvature, consistent with the note.
- S-shaped wave of paper: bends toward the topping face in one region and the bottom face in another. Broke the takeaway and two corrections that said "bends toward one face only" without "at each spot"; fixed in the takeaway, the curl-the-slice answer and sheet-bends-any-way.
- Tilted rulings (a slice curled conically, rulings converging): breaks the working claim that nonzero curvature across the width forces zero along the slice; true only on the symmetric centre line, now stated. The entry wording "the line running from crust to tip" is accurate on the centre line, which carries the droop argument.
- Paper cone tip and a crease: excluded by "away from creases and sharp tips". Paper Mobius band: developable, consistent.
- Monkey saddle centre (II = 0): a spot that does not bend at all, covered by "at a spot where a surface bends at all".
- Nash-Kuiper C1 isometric embeddings of a flat torus in R^3 and C1 corrugated flat sheets: they evade the rolled-poster rule, but the note says smooth at working and formal rungs, and the entry scope excludes creases; fine wrinkles are not real paper.
- Narrow cone lampshade: if the card sector angle is below 60 degrees, a 5 cm walk from a point 10 cm from the apex could wrap around; realistic lampshades (and the 30-degree shade of the problem, sector 180 degrees) are far from this. Not changed.
- Long walks on the tube (beyond half its circumference): excluded by "a small ring, well away from the paper edges".
- Different slicing: de Sitter has flat, spherical and hyperbolic slicings; the working way scopes to cosmic time in simplifies. Different observer: galaxies with peculiar velocity define a tilted slicing; the way names the comoving galaxies.
- Flat slices, curved spacetime vs flat spacetime with curved slices (Milne slicing of Minkowski: hyperbolic slices, K_ij = g/t): consistent with the Gauss equation, since -1/t^2 intrinsic + 1/t^2 extrinsic gives zero ambient curvature.
- Ring on a ball larger than a hemisphere: still shorter than 6.28 times the walk, since sin(x) < x for x > 0. Statement true.
- Second pass. Cone apex of a rolled sheet: a spot of a sheet bent without stretching that has no unbent line and no well-defined bend; it breaks the rule as the check curl-the-slice answer and the misconception sheet-bends-any-way stated it, and both now exclude it in the way's own words.
- Compact surface with boundary (a flat cardboard disc, K = 0 everywhere): it would break the formal problem's conclusion, but a surface in Euclidean space means a submanifold without boundary throughout this note, so the statement stands as written; recorded rather than reworded.
- Umbilic and planar points: a sphere has kappa_1 = kappa_2 everywhere, so 'reached in perpendicular directions' needs the note's 'when they differ', which it has; a planar point (monkey-saddle centre) is covered by 'at a spot where a surface bends at all'.
- Milne slicing of flat spacetime re-run as a sign check on the Gauss equation with epsilon = -1: hyperbolic slices with intrinsic -1/t^2 and extrinsic terms +1/t^2 give zero ambient curvature, so the epsilon = -1 bracket sign used in flat-slice-curved-spacetime is right.
- Ring test walked past a ball's antipode, and walks longer than half a tube's circumference: the first keeps the ring shorter than 6.28 times the walk (2 pi a |sin(rho/a)| <= 2 pi rho), the second is excluded by the entry scope 'short walks, well away from the paper's edges'.

**Fixes**

- Wire way: final sentence now covers the hoop ("or a round hoop if the ends are joined"; "none of her lengths can reveal a bend").
- Pizza way: "the air inside the ring" became "the air sealed inside the tube", so it cannot be read as the hole.
- Pizza takeaway, curl-the-slice answer and misconception sheet-bends-any-way: "toward one face only at each spot", because a wavy sheet bends toward different faces in different places.
- Misconception opposite-bends-cancel: no longer equates bends with intrinsic curvature; the saddle pattern has intrinsic curvature.
- Working "Two bends and their product": cylinder normal named; slice argument restricted to the centre line with the mirror-symmetry reason.
- Working "Flat space that bends inside spacetime": unit normal is the four-velocity divided by c; the value near 73 attributed to Cepheid-calibrated supernova distances.
- Check flat-yet-expanding: "zero intrinsic curvature, within errors".
- Notation trap: relativity texts use either overall sign for K_ij.
- Both references verified. Entry explanations now 1096 words, inside the 10% allowance; nothing compressed or dropped. Revision bumped to 3.
- Second pass (note at revision 5): check curl-the-slice answer now reads 'Away from creases and a cone's sharp point', matching the way it is answered from; before, its general rule covered the cone point, where it is false.
- Second pass: misconception sheet-bends-any-way correction gained the same scope phrase, so the tutor speaks the rule with its conditions.
- Nothing else changed: every equation, number, tolerance and reference re-derived or recomputed from scratch and found correct. Revision bumped to 6; tutoring words 1932 -> 1944 of 2200, total 5910 -> 5922 of 7000.

**Concerns**

- course-conventions.md makes no choice for the sign of normal curvature, the scalar second fundamental form h, the shape operator, or the extrinsic curvature K_ij of a spacetime slice (nor its symbol, which clashes with Gaussian K). This note uses positive-toward-the-chosen-normal and h = gbar(II, nu), nabla_X nu = -SX, and avoids fixing a sign for K_ij. An editor should add a conventions row before extrinsic-curvature-of-a-hypersurface and second-fundamental-form are reviewed.
- Entry explanations sit at 1096 of 1000 words (inside the 10% allowance). Any further entry addition needs a cut, for example the Earth ring number that repeats a prerequisite.
- The working way "Flat space that bends inside spacetime" uses four-velocity and proper time and assumes metric-tensor only through a prerequisite chain; consider a bridge or a direct prerequisite.
- DESI DR2 BAO combined with CMB gives Omega_K near 0.002 +- 0.001, about 2 sigma from zero, while the note quotes Planck with earlier BAO. "Flat within errors" remains fair; revisit when curvature constraints settle.
- Registry prerequisites differ from the note (curvature-of-a-curve, embedding, levi-civita-connection); run sync_registry.py. Registry aliases still list "genuine curvature" and "developable surface", which are not true synonyms.
- Second pass: the entry rung is still at 1097 of 1000 words for explanations (inside the 10% review allowance) and carries only one everyday number, the 0.026 mm Earth ring shortfall that repeats a prerequisite's number. An editor wanting a second entry number must cut something first.
- Second pass: the note's own aliases 'intrinsic curvature' and 'extrinsic curvature of a surface' name the two halves of the contrast rather than synonyms of it, and 'extrinsic curvature of a surface' overlaps second-fundamental-form. Left alone because ids and aliases are addressing, but an editor should decide.
- Second pass: check lampshade-for-an-ant does not fix the shade's rim radii, so a 5 cm ring around the ant is a Euclidean circle only if the shade's girth there exceeds about 10 cm. Every real lampshade is far from that, so the wording was left as it is.

**Diff check** (2026-09-13, revision 4)

- Pizza takeaway, curl-the-slice answer, sheet-bends-any-way correction: away from creases (and sharp tips), a sheet bent without stretching bends toward only one face at each spot and keeps an unbent line through that spot.: Compared with the revision-3 wording ('toward one face only at each spot ... through it'); tried the S-shaped wave of paper, a planar spot, a cone near its tip, a crease, and the C1 corrugated sheet. → Same claim with the referent made explicit. The wave bends toward different faces at different spots, allowed by 'at each spot'. A planar spot has unbent lines and no bend toward a second face, as before. Tip and crease are excluded by scope, and the entry scope rules out C1 corrugations. Accurate.
- Check flat-yet-expanding: within errors, a constant-time slice has zero intrinsic curvature, the curvature read from lengths and angles within it; extrinsic principal values of size H0/c = 7.29e-27 m^-1, radius c/H0 = 4.45 Gpc.: Reread the reordered sentence against the old one; recomputed with python3 for H0 = 67.4 km/s/Mpc, c = 299792.458 km/s, 1 Mpc = 3.0857e22 m. → Same claim: 'within errors' still qualifies the zero intrinsic curvature, and the appositive defines intrinsic curvature correctly. c/H0 = 4448 Mpc = 4.45 Gpc (14.5 billion light-years), H0/c = 7.29e-27 m^-1. The numeric field 4.45 Gpc with rel_tol 0.02 is consistent. Accurate.
- Flat-space-in-curved-spacetime: nearby supernovae, with distances calibrated by Cepheid variable stars, give about 73 in the same units, a tension not yet resolved.: Checked that 'the same units' refers to the km s^-1 Mpc^-1 of the preceding Planck value; compared with the distance-ladder result, about 73 km/s/Mpc, against Planck's 67.4 +/- 0.5. → The units reference is unambiguous, Cepheids are variable stars, and the value and the unresolved tension are correct as of 2026. No new reference was added. Accurate.
- Two-bends-and-their-product: the slice's mirror symmetry across its centre line makes the across and along directions principal there; the normal curvature across is nonzero where the U curls; since their product K is zero, the normal curvature along the centre line is zero.: Symmetry argument: the reflection fixes the point and maps the surface to itself, so it commutes with the shape operator, whose eigenvectors are then along and across the line. With these principal, K = kappa_1 kappa_2 = kappa_across kappa_along, and K = 0 for a sheet bent without stretching. Tried a conically curled slice with converging rulings: if the cone is symmetric about the centre line, the ruling in the symmetry plane is the centre line, so this is consistent. → The split into two sentences adds the step (the product is K = 0) that the old sentence left implicit. It claims exactly what the old one did, and the added step is true. Accurate.
- Fix: None needed. All six changed learner-visible strings are accurate; no text changed and the revision stays at 4.

**Diff check** (2026-09-13, revision 6)

- Novice re-read wording: 'Hold a slice of pizza by its crust, topping side facing the ceiling, without curling it' (way and check curl-the-slice question), replacing 'and keep it flat' / 'flat by its crust'.: Compared the initial state each version sets: an uncurled slice held horizontally by the crust, topping upward. Checked that the droop claim depends only on that state. → Same physical setting, with 'flat' no longer doing double duty for a surface and for how the slice is held. Accurate.
- Glossary intrinsic curvature: 'Curving that shows up in measurements made along a surface or a line, without leaving it. ... A rolled-up poster does not, and neither does a wire.': Checked against the note's own theorem statement that a one-dimensional manifold has R identically zero, and against the wire way and the objective that says a wire never has intrinsic curvature. → Correct and now consistent with the wire way, which applies the term to a line and denies it there. Accurate.
- Spoken entry answer: 'All of space at one instant, timed by clocks that ride along with the galaxies, is one slice of space and time.': Compared with the working way's slicing, constant cosmic time, the time on clocks carried by galaxies moving with the average cosmic flow; checked that the added clause names the measurer required for a statement about one instant everywhere. → It names exactly the cosmic-time slicing the rest of the note uses, and adds no math to a spoken field. Accurate.
- Scope phrase 'away from creases and a cone's sharp point' replacing 'away from creases and sharp tips' in the way's explanation and takeaway.: Listed the places where a sheet bent without stretching fails to be smooth: creases, and conical points where it is pinched. Checked that the new phrase excludes the same set, and that it no longer collides with the pizza slice's own tip, which the way argues about. → Same exclusions, said without reusing 'tip' in two senses. The rule remains true everywhere else: K = 0 forces at least one vanishing principal curvature, so the normal curvature kappa_1 cos^2 theta keeps one sign and vanishes along exactly one line. Accurate.
- Recap: 'two walkers who start side by side, both facing the same way at a right angle to the line between them, spread apart' around a swim ring's hole.: Checked the initial conditions of geodesic deviation: separation orthogonal to the direction of travel and no initial relative velocity, in the region near the hole where K < 0. → The added right-angle condition is the one the spreading claim needs, and it matches the prerequisite's statement of the walkers' test. Accurate.
- 'She runs the ring test with short walks, well away from the paper's edges' replacing 'on a small ring'.: Checked what the scope must exclude on a rolled poster: walks long enough to wrap around the tube, and walks reaching the paper's edges. The controlled quantity is the walked distance, not the ring. → The new wording scopes the right quantity and is not circular. On a tube of radius R, a walk shorter than pi R gives a ring of exactly 6.28 times the walk, as the way claims. Accurate.
- Fix: All seven novice rewrites are accurate; none was changed.
- Fix: Two other entry strings that state the same sheet rule had been left behind by that rewrite and did not carry its scope: the check curl-the-slice answer ('Away from creases' only) and the misconception sheet-bends-any-way correction (no scope). Both now read 'Away from creases and a cone's sharp point', so revision 6.
