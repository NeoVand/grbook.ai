---
type: "concept"
schema_version: 2
id: "angular-excess"
title: "Angular excess"
tagline: "How the corners of a triangle on a ball add up to more than half a turn"
domain: "curvature"
tier: "foundation"
status: "physics-reviewed"
revision: 8
updated: "2026-09-13"
aliases: ["angle excess", "spherical excess", "Girard's theorem"]
prerequisites: ["curvature", "great-circle-geodesics", "gaussian-curvature"]
leads_to: ["holonomy", "theorema-egregium"]
visuals: ["orange-segments-around-a-triangle", "carry-an-arrow-around-a-loop"]
---

# Angular excess

*How the corners of a triangle on a ball add up to more than half a turn*

`angular-excess` · curvature · foundation · physics-reviewed (revision 8)

**Needs:** [[curvature]] (entry) · [[great-circle-geodesics]] (working) · [[gaussian-curvature]] (working)  
**Opens:** [[holonomy]] · [[theorema-egregium]]  
**Related:** [[parallel-postulate]] · [[hyperbolic-plane]]  
**Visuals:** ★ [[orange-segments-around-a-triangle]] · [[carry-an-arrow-around-a-loop]]

> Tear the three corners off a paper triangle and they always fill half a turn, 180 degrees. On a ball, walk the three sides of a triangle without ever steering left or right, and its corners add up to more. The extra, called the angle excess, is 720 degrees times the share of the ball's surface the triangle covers. So measuring a big enough triangle tells someone who never leaves the ball's surface that the ball is curved.

## You will be able to

**Entry**
- Explain why a triangle of straight walks on a ball has corners adding up to more than 180 degrees. `objectives/explain-extra-corners` ← `checks/north-pole-triangle-corners`
- Compute an angle excess on a ball from the share of the ball a triangle covers. `objectives/use-the-share-rule` ← `checks/small-triangle-on-a-field`, `problems/twenty-triangle-ball`

**Working**
- Compute a geodesic triangle's area from its angles on a sphere or a hyperbolic plane. `objectives/compute-area-from-angles` ← `checks/hyperbolic-triangle-area`, `problems/radius-from-an-excess`
- Explain why the excess rule needs geodesic sides. `objectives/require-geodesic-sides` ← `checks/latitude-side-triangle`

**Formal**
- State Gauss's theorem for geodesic triangles with its hypotheses, and apply it to cone points and large regions. `objectives/state-gauss-theorem-with-limits` ← `checks/cone-tip-triangle`, `checks/both-regions-of-the-sphere`
- Prove that geodesic triangles on a surface of constant negative curvature have bounded area. `objectives/prove-hyperbolic-area-bound` ← `problems/hyperbolic-triangles-have-bounded-area`

## Ways in

### 1. A triangle with three right angles · entry · picture

*Can the three corners of a triangle add up to more than half a turn?*

Draw a triangle on a sheet of paper with a ruler. Tear off its three corners and lay them side by side, with their tips touching. Whatever triangle you drew, the three corners fill exactly half a turn, 180 degrees.

Now imagine a walker on a huge, smooth ball. The walker never steers left or right. Walking like this is called walking straight. The path bends over the ball's curve, but the walker never steers, so the path counts as straight.

Seen from outside, as on a globe, call the top point the North Pole and the circle around the middle the equator. The equator is a straight walk, and so is each line printed on a globe from the North Pole to the equator. For each of these paths, the ball on one side is a mirror image of the ball on the other side. So a walker has no reason to steer either way. A small circle around the North Pole is not a straight walk: to stay on it, a walker must keep steering toward the North Pole.

Now walk a triangle of straight walks. Start at the North Pole and walk to the equator. Turn left onto the equator and walk a quarter of the way around it. Turn left again and walk back to the North Pole. The triangle is the piece of the ball on your left as you walk. Each of its corners is the angle between two of its sides, measured on that piece.

Each line from the North Pole meets the equator at a right angle, as any globe shows. That makes both corners on the equator right angles.

For the corner at the North Pole, think of an orange cut from top to bottom into four equal segments. The four corners where the segments meet at the top fill a full turn, so neighbouring cuts meet there at a quarter turn, a right angle. Neighbouring cuts are also a quarter of the way apart around the middle. Your first and last paths reach the equator a quarter of the way around apart, so they run along two neighbouring cuts. This triangle therefore has three right angles, adding up to 270 degrees.

The amount by which a triangle's corners add up to more than 180 degrees is called its angle excess. This triangle's angle excess is 90 degrees.

**Try it:** Stretch a rubber band around the middle of an orange. Stretch two more from top to bottom, crossing at the top at a right angle. Each band should split the orange into two halves of the same size, which makes each band a straight walk. Pick one of the eight triangles the three bands make. At each of its corners, press a postcard's corner onto that point, with the card lying over the triangle. Each time, the postcard's two edges set off along the two bands, so all three corners are right angles.

**Takeaway:** On flat paper a triangle's corners add up to 180 degrees, but a triangle of straight walks on a ball can have three right angles, adding up to 270.

*Visuals:* [[carry-an-arrow-around-a-loop]] (preset `octant`)<br>*See:* `checks/north-pole-triangle-corners`

### 2. Walkers who start parallel meet · entry · contrast

*Why can a triangle on a ball have corners that add up to more than a triangle on flat ground?*

**Recap:** Walking without ever steering left or right is called walking straight. Two straight walkers start parallel when they stand side by side on a straight walk, facing the same way at a right angle to it. On flat ground their gap never changes. That includes a surface that only looks bent, like a can's label, which unrolls onto a table without stretching. On a ball, walkers who start parallel draw together.

In "A triangle with three right angles", a paper triangle's corners filled half a turn, but the North Pole triangle's corners made three quarters of a turn.

On flat ground, stand two walkers at the two ends of a short straight walk. Both face the same way, at a right angle to that straight walk, so they start parallel. Each walker's path makes a right angle with the straight walk, so these two corners of a triangle already add up to half a turn. On flat ground their gap never changes, so their paths never meet and no triangle closes.

To close a triangle on flat ground, the walkers must set off heading a little toward each other. That makes the two starting corners smaller. The torn paper corners show that the three corners of a flat triangle still add up to half a turn. The corner where their paths meet is therefore exactly as big as the amount taken off the two starting corners.

Now stand the two walkers on a ball's equator, both facing the North Pole. Again they start parallel. Each walker's path makes a right angle with the equator, so these two corners add up to half a turn. On a ball, though, walkers who start parallel draw together. Each walker follows one of the globe's lines to the North Pole, so they meet there. The triangle closes with a third corner at the North Pole, on top of that half turn. So the whole corner at the North Pole is angle excess.

**Takeaway:** On flat ground, walkers who start parallel never meet, so a triangle's corners make exactly half a turn; on a ball they meet, and the corner where they meet is extra.

*Continues:* `ways_in/three-right-angles-on-a-ball`<br>*Builds on:* [[curvature]]

### 3. The excess follows the share of the ball · entry · calculation

*What decides how big the angle excess of a triangle on a ball is?*

**Recap:** Walking without ever steering left or right is called walking straight. The angle excess is the amount by which a triangle's corners add up to more than 180 degrees. The North Pole triangle runs from the North Pole to the equator, a quarter of the way around the equator, and back. It has three right angles, so its angle excess is 90 degrees. Two walkers who stand on the equator, both facing the North Pole, start parallel. They meet at the North Pole, and the whole corner there is angle excess.

In "Walkers who start parallel meet", two walkers left the equator side by side and met at the North Pole, and the whole corner there was angle excess.

Picture the ball as an orange with the North Pole at the top. Cut it from top to bottom into 36 equal segments. The 36 corners where the segments meet at the top fill a full turn. So neighbouring cuts meet there at one thirty-sixth of a full turn, which is 10 degrees.

Now stand two walkers where two neighbouring cuts cross the equator, both facing the North Pole. They walk along the two cuts and meet at the North Pole, at a corner of 10 degrees. That whole corner is angle excess, so their triangle has an angle excess of 10 degrees.

That triangle is the top half of one segment, the part between the equator and the North Pole. One segment covers one thirty-sixth of the ball's surface, so the triangle covers one seventy-second. And 72 times 10 degrees is 720 degrees.

The North Pole triangle fits too. It is half of one of four equal segments, so it covers one eighth of the ball's surface, and 8 times 90 degrees is 720 degrees.

Both fit one rule. The angle excess is 720 degrees times the share of the ball the triangle covers. The share is the triangle's own area as a fraction of the ball's whole surface. The rule holds for every triangle of straight walks on a smooth, round ball. Take that on trust here; the working level proves it with orange segments.

The three sides cut the ball into two pieces, so the corners and the share must be measured on the same piece. For the North Pole triangle, that is the piece covering one eighth of the ball, where all three corners are right angles.

So small triangles have small excesses. Earth's surface is about 510 million square kilometres. A triangle joining three towns, each 100 kilometres from the other two, covers about 4,300 square kilometres. That is one part in about 118,000 of Earth's surface. Its angle excess is 720 degrees divided by 118,000, about six thousandths of a degree. That is about the width of a hair held at arm's length, as an angle at your eye. No protractor shows that, which is why the corners of triangles marked out on the ground seem to add up to exactly 180 degrees.

**Takeaway:** On a smooth, round ball, a triangle's angle excess is 720 degrees times the share of the ball it covers, so small triangles have tiny excesses.

*Continues:* `ways_in/walkers-who-start-parallel-meet`<br>*Visuals:* [[orange-segments-around-a-triangle]]<br>*See:* `checks/small-triangle-on-a-field`, `problems/twenty-triangle-ball`

### 4. Orange segments prove Girard's theorem · working · calculation

*Why does the angle excess on a sphere equal the area divided by the radius squared, and what replaces that rule on other surfaces?*

The rule of "The excess follows the share of the ball", an angle excess of 720 degrees times the share of the ball, becomes an equation in radians. A straight walk is a geodesic, and on a sphere every geodesic runs along a great circle. A sphere of radius $a$ has area $4\pi a^2$, so a region of area $A$ is the share $A/4\pi a^2$ of it, and $720^\circ$ is $4\pi$ rad. So a geodesic triangle, one whose sides are great-circle arcs, with interior angles $\alpha_1, \alpha_2, \alpha_3$ and area $A$ has angle excess

$$E \equiv \alpha_1 + \alpha_2 + \alpha_3 - \pi = \frac{A}{a^2}.$$

This is Girard's theorem, and orange segments prove it. A lune, the shape of one orange segment's peel, is the region between two great semicircles that join a pair of antipodal points and meet there at angle $\alpha$. It is the fraction $\alpha/2\pi$ of the sphere, so its area is $2\alpha a^2$. Extend the triangle's sides to three full great circles. At each vertex, the lune of angle $\alpha_i$ containing the triangle, together with the antipodal lune, has area $4\alpha_i a^2$. These six lunes cover the triangle and its antipodal copy three times each and the rest of the sphere once, so

$$4a^2(\alpha_1 + \alpha_2 + \alpha_3) = 4\pi a^2 + 4A.$$

Dividing by $4a^2$ gives Girard's theorem. The derivation "Girard's theorem by counting lunes" writes out each move.

The sphere's Gaussian curvature is $K = 1/a^2$, so $E = KA$. On the hyperbolic plane, whose small pieces are saddle-shaped, $K = -1/a^2$ everywhere and $E = -A/a^2$: the angles fall short of $\pi$ by the area over $a^2$. This is Lambert's result, and it means no hyperbolic triangle has an area of $\pi a^2$ or more.

Both are cases of Gauss's theorem, taken on trust at this rung: a geodesic triangle on a smooth surface that bounds a region $S$ with no cone points or holes has

$$E = \iint_S K\,dA.$$

So a small triangle near a point of curvature $K$ has $E \approx KA$, and on a plane or a cylinder, where $K = 0$, every such triangle has $E = 0$. The sides must be geodesics. A side that bends along the surface adds its own turning, as the check "A triangle with a latitude side" shows.

**Takeaway:** On a sphere the angle excess is the area over the radius squared; on any surface it is the Gaussian curvature added up over the region a geodesic triangle bounds.

*Continues:* `ways_in/excess-follows-the-share-of-the-ball`<br>*Builds on:* [[great-circle-geodesics]], [[gaussian-curvature]]<br>*Visuals:* [[orange-segments-around-a-triangle]]<br>*See:* `derivations/girard-by-counting-lunes`, `worked_examples/equilateral-thousand-kilometre-triangle`, `checks/hyperbolic-triangle-area`, `checks/latitude-side-triangle`

### 5. Surveyors measure the excess · working · operational

*How do surveyors on Earth meet the angle excess, and how large is it for their triangles?*

Girard's theorem from "Orange segments prove Girard's theorem" turns up whenever surveyors measure large triangles. A theodolite is a telescope on a levelled base that reads horizontal angles. Aimed at two distant signals, it gives the angle between the two vertical planes through them. On a sphere every vertical plane contains the centre, so it meets the surface along a great circle. The theodolite therefore reads the angles of the geodesic triangle.

One arcsecond is $1/3600$ of a degree, $4.848\times10^{-6}$ rad. On Earth, with $a = 6371$ km, $a^2$ times one arcsecond is $197$ km². So every 197 km² of triangle adds one arcsecond to the angle sum. In Gauss's survey of the Kingdom of Hanover in the 1820s, the largest triangle joined the summits of the Brocken, the Hoher Hagen and the Inselsberg. Its sides are about 69, 85 and 107 km and its area about 2930 km², so its angles add up to $180^\circ$ plus about 15 arcseconds.

Surveyors handle the excess with Legendre's theorem. Subtract one third of the excess from each angle of a small spherical triangle, and the result is the flat triangle with the same side lengths. The theorem is not exact in general, so each reduced angle differs by a small error from the true angle of that flat triangle. For a triangle whose sides are of order $\ell$, the ratio of this error to the excess is $(\ell/a)^2$ times a small numerical factor set by the triangle's shape. The factor is zero for an equilateral triangle, where the reduction is exact at every size. For the Hanover triangle the error is below $10^{-4}$ arcseconds. The flat triangle is then solved with ordinary trigonometry.

Run backwards, the excess measures curvature: measured angles and area give $K = E/A$, and so a radius. Earth is slightly flattened at the poles, so its Gaussian curvature there is about 1.3% smaller than at the equator, and precise surveys use the local value.

**Takeaway:** A theodolite reads the angles of geodesic triangles, which on Earth exceed 180 degrees by one arcsecond for every 197 square kilometres of area.

*What this leaves out:* Treats Earth as a sphere and light rays as straight. On the flattened Earth, planes through the local vertical cut the surface along curves that differ very slightly from geodesics, and survey reductions correct for this and for refraction.

*Continues:* `ways_in/orange-segments-prove-it`<br>*See:* `observations/hanover-survey-triangle`, `problems/radius-from-an-excess`

### 6. Gauss's theorem for geodesic triangles · formal · structure

*Under what hypotheses does the angle excess of a geodesic triangle equal its total curvature, and why?*

Girard's theorem of "Orange segments prove Girard's theorem" needs constant curvature; Gauss proved the general statement. Let $(M, g)$ be a smooth Riemannian surface. A geodesic triangle $\Delta \subset M$ is a closed region homeomorphic to a disk, bounded by three geodesic arcs meeting at vertices $p, q, r$ with interior angles $\alpha_p, \alpha_q, \alpha_r \in (0, 2\pi)$ measured within $\Delta$.

*Theorem (Gauss).* $\alpha_p + \alpha_q + \alpha_r - \pi = \iint_\Delta K\,dA$.

*Proof sketch.* First let $\Delta$ lie in a normal neighbourhood of $p$, with each radial geodesic from $p$ inside the angle $\alpha_p$ crossing the side $qr$ once. In geodesic polar coordinates about $p$, $ds^2 = dr^2 + G(r,\phi)\,d\phi^2$, with $\sqrt G = r - K(p)\,r^3/6 + O(r^4)$ and $K = -\partial_r^2\sqrt G/\sqrt G$. The side $qr$ is $r = \rho(\phi)$ for $0 \le \phi \le \alpha_p$, so

$$\iint_\Delta K\,dA = -\int_0^{\alpha_p}\!\!\int_0^{\rho(\phi)}\partial_r^2\sqrt G\,dr\,d\phi = \int_0^{\alpha_p}\Big(1 - \partial_r\sqrt G\,\big|_{r = \rho(\phi)}\Big)\,d\phi.$$

Let $\psi$ be the angle from $\partial_r$ to the tangent of $qr$, measured toward increasing $\phi$. Along a geodesic $d\psi = -\partial_r\sqrt G\,d\phi$, and $\psi$ runs from $\pi - \alpha_q$ at $q$ to $\alpha_r$ at $r$. The integral is therefore $\alpha_p + \alpha_r - (\pi - \alpha_q)$. A general triangle is cut into small triangles of this kind. Excess is additive: in a subdivision with $F$ triangles, $L$ edges and $V$ vertices, each interior vertex carries $2\pi$ of angle, each vertex inside a side carries $\pi$, and $F - L + V = 1$ makes these extra angles cancel.

*Consequences.* $K(p) = \lim E/A$ as non-degenerate geodesic triangles shrink to $p$, an intrinsic definition of $K$. The angles exceed $\pi$ when $K > 0$ throughout $\Delta$ and fall short when $K < 0$ throughout. For constant $K \neq 0$, triangles with equal angles have equal areas.

*Limits.* A cone point of total angle $2\pi - \delta$ inside $\Delta$ adds $\delta$ to the right-hand side. Sides that are not geodesics add $\oint_{\partial\Delta}\kappa_g\,ds$, with $\kappa_g$ positive where a side bends toward $\Delta$: the local Gauss–Bonnet theorem. A region $S$ bounded by geodesic arcs but not a disk obeys $\iint_S K\,dA + \sum_i(\pi - \alpha_i) = 2\pi\chi(S)$. In higher dimensions a geodesic triangle need not lie in a totally geodesic surface, so the theorem does not apply as stated. Toponogov's theorem compares instead: in a complete manifold with sectional curvature at least $k$, a triangle of minimizing geodesics has angles no smaller than those of the triangle with the same side lengths on the surface of constant curvature $k$, under the standard side-length conditions when $k > 0$.

**Takeaway:** For a geodesic triangle bounding a smooth disk, the angle sum minus pi is the integrated Gaussian curvature; cone points, bending sides and other topologies add known terms.

*Continues:* `ways_in/orange-segments-prove-it`<br>*Builds on:* [[gaussian-curvature]]<br>*See:* `checks/cone-tip-triangle`, `checks/both-regions-of-the-sphere`, `problems/hyperbolic-triangles-have-bounded-area`

## Glossary

| Term | Say | In plain words | Concept |
| --- | --- | --- | --- |
| walk straight | — | To walk without ever steering left or right, even where the path bends over a curved surface. | [[geodesic]] |
| start parallel | — | Two straight walkers start parallel when they stand side by side on a straight walk, facing the same way at a right angle to it. | — |
| angle excess | — | The amount by which the three corners of a triangle add up to more than 180 degrees. On flat ground it is zero. | [[angular-excess]] |
| flat | — | Having no curving that walkers can find: straight walkers who start parallel keep their gap, even where the surface looks bent, like a can's label. | [[flat-metric]] |

## Key equations

### Girard's theorem · working

$$
\alpha_1 + \alpha_2 + \alpha_3 - \pi = \frac{A}{a^2}
$$

On a sphere, a geodesic triangle's angles exceed $\pi$ by its area in units of the radius squared.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $\alpha_1, \alpha_2, \alpha_3$ | interior angles in radians, measured inside the region | the three angles |
| $A$ | area of the region | the area |
| $a$ | radius of the sphere | the radius |

**Holds when:** Sides are great-circle arcs; the angles and the area belong to the same one of the two regions the sides bound.  
**Say it:** “The three angles minus pi equal the area divided by the radius squared.”  
**Justified by:** `derivations/girard-by-counting-lunes`

### Gauss's theorem for geodesic triangles · working

$$
\alpha_1 + \alpha_2 + \alpha_3 - \pi = \iint_S K\,dA
$$

On any smooth surface, a geodesic triangle's angle excess is the Gaussian curvature added up over the region it bounds.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $S$ | the region the triangle bounds, where the angles are measured | the region |
| $K$ | Gaussian curvature, $+1/a^2$ on a sphere | the Gaussian curvature |

**Holds when:** Smooth surface; geodesic sides; $S$ homeomorphic to a disk, with no cone points or holes.  
**Say it:** “The three angles minus pi equal the Gaussian curvature integrated over the region.”  
**Justified by:** `stated`

## Derivations

### Girard's theorem by counting lunes · working

**Goal:** Show that a geodesic triangle on a sphere of radius $a$ with angles $\alpha_i$ and area $A$ has $\alpha_1 + \alpha_2 + \alpha_3 = \pi + A/a^2$.

1. A lune of angle $\alpha$ is bounded by two great semicircles from a point to its antipode. Rotating one semicircle by $\alpha$ about the axis through those points sweeps out the lune, so it is the fraction $\alpha/2\pi$ of the sphere, with area $2\alpha a^2$.
2. Extend the three sides of the triangle $T$ to full great circles. Each pair of great circles meets at two antipodal points, so the antipodal image $T'$ is bounded by the same circles and has area $A$.
3. At vertex $i$, two of the circles bound a lune of angle $\alpha_i$ that contains $T$, and the antipodal lune that contains $T'$. The pair has area $4\alpha_i a^2$.
4. The three circles cut the sphere into eight triangles. Every point of $T$ or $T'$ lies in all three pairs of lunes, and every point of the other six triangles lies in exactly one pair.
5. Adding the three pairs counts the sphere once and $T$ and $T'$ twice more each: $4a^2(\alpha_1 + \alpha_2 + \alpha_3) = 4\pi a^2 + 4A$.
6. Divide by $4a^2$.

**Result:** $\alpha_1 + \alpha_2 + \alpha_3 - \pi = A/a^2$ for a triangle whose angles are each less than $\pi$. The other region, with angles $2\pi - \alpha_i$ and area $4\pi a^2 - A$, satisfies the same relation.

## Worked examples

### A triangle with 1000 km sides on Earth · working

**Problem:** On a sphere of Earth's mean radius, $a = 6371$ km, a geodesic triangle has three sides of 1000 km. Find its angles from the spherical law of cosines, then its angle excess and area, and compare with a flat equilateral triangle with the same sides.

1. Each side subtends $c = 1000/6371 = 0.15696$ rad at the centre.
2. For an equilateral triangle the spherical law of cosines, taken on trust, gives $\cos\alpha = \cos c/(1 + \cos c) = 0.49690$, so $\alpha = 60.2044^\circ$.
3. The excess is $E = 3\alpha - 180^\circ = 0.6131^\circ = 0.010701$ rad, about 37 arcminutes.
4. Girard's theorem gives $A = E a^2 = 0.010701 \times (6371\ \text{km})^2 = 4.3435\times10^5$ km².
5. The flat triangle has area $(\sqrt3/4)(1000\ \text{km})^2 = 4.3301\times10^5$ km², 0.31% less; dividing it by $a^2$ gives $0.6112^\circ$, close to the true excess.
6. Each angle exceeds $60^\circ$ by $0.2044^\circ$, one third of the excess.

**Answer:** Angles of $60.204^\circ$, excess $0.613^\circ$ (0.0107 rad), and area $4.34\times10^5$ km², 0.3% more than the flat triangle.

**Takeaway:** For a triangle small compared with the sphere, $K$ times the flat area gives the excess closely, and one third of it sits in each angle.

## Problems

### `twenty-triangle-ball` · entry · difficulty 2 · calculation

A ball's whole surface is divided into 20 identical triangles, each made of three straight walks. Five triangles meet at every point where corners touch. How big is each corner of a triangle? What is each triangle's angle excess, and does it fit the rule that the excess is 720 degrees times the share of the ball?

**Hints**

1. The five corners that meet at one point fit around it with no gaps, so they fill a full turn.
2. What share of the ball does one triangle cover?

**Answer:** Each corner is 72 degrees, so the corners add up to 216 degrees and the angle excess is 36 degrees. One triangle covers one twentieth of the ball, and 720 degrees divided by 20 is also 36 degrees.

**Must contain:** Each corner is 72 degrees; The angle excess is 36 degrees; 720 degrees times one twentieth is also 36 degrees

**Numeric:** angle excess of one triangle = 36 deg (magnitude, ±1)

**Solution**

1. Five identical corners meet at each point and fill a full turn, 360 degrees, so each corner is 360 divided by 5, which is 72 degrees.
2. Three corners of 72 degrees add up to 216 degrees, which is 36 degrees more than 180. So the angle excess is 36 degrees.
3. The 20 identical triangles cover the ball, so each covers one twentieth of it. 720 degrees divided by 20 is 36 degrees, so the rule fits.

### `radius-from-an-excess` · working · difficulty 2 · estimate

Surveyors on a round planet measure the angles of a geodesic triangle of area 2930 km² and find that they add up to 180° plus 14.9 arcseconds. Treating the planet as a sphere, find its radius. By what fraction does the radius change if the excess is uncertain by 0.5 arcseconds?

**Hints**

1. One arcsecond is $4.848\times10^{-6}$ rad.
2. Solve Girard's theorem for the radius.

**Answer:** $a = \sqrt{A/E} \approx 6370$ km. An uncertainty of 0.5 arcseconds is 3.4% of the excess, and $a \propto E^{-1/2}$, so the radius is uncertain by about 1.7%, roughly 110 km.

**Must contain:** The excess is 7.22 millionths of a radian; The radius is the square root of area over excess, about 6370 kilometres; The radius goes as the excess to the minus one half, so 3.4 percent becomes 1.7 percent

**Numeric:** radius = 6369 km (magnitude, ±1%)

**Solution**

1. $E = 14.9 \times 4.848\times10^{-6} = 7.224\times10^{-5}$ rad.
2. Girard's theorem $E = A/a^2$ gives $a = \sqrt{A/E} = \sqrt{2930\ \text{km}^2/7.224\times10^{-5}} = 6369$ km.
3. $0.5/14.9 = 3.4\%$. Since $a \propto E^{-1/2}$, $\delta a/a = \tfrac12\,\delta E/E = 1.7\%$, about 110 km: the excesses 14.4 and 15.4 arcseconds give 6478 km and 6264 km.

### `hyperbolic-triangles-have-bounded-area` · formal · difficulty 2 · proof

On a complete, simply connected surface of constant curvature $K = -1/a^2$, prove that every geodesic triangle has area less than $\pi a^2$, and that the bound is approached.

**Hints**

1. Apply Gauss's theorem with constant $K$.
2. Follow an equilateral triangle as its side grows without bound.

**Answer:** $A = a^2(\pi - \alpha_1 - \alpha_2 - \alpha_3) < \pi a^2$ since every angle is positive. Equilateral triangles with side $s \to \infty$ have angles tending to zero, so their areas tend to $\pi a^2$.

**Must contain:** Area equals a squared times pi minus the angle sum; Positive angles make the area less than pi a squared; Angles of large equilateral triangles tend to zero, so the bound is approached

**Solution**

1. A geodesic triangle bounds a disk with no cone points, so Gauss's theorem gives $\sum\alpha_i - \pi = \iint K\,dA = -A/a^2$, that is $A = a^2(\pi - \sum\alpha_i)$.
2. Each interior angle is positive, so $A < \pi a^2$.
3. For an equilateral triangle of side $s$, the hyperbolic law of cosines, taken on trust, gives $\cos\alpha = \cosh(s/a)/(1 + \cosh(s/a))$, which tends to 1 as $s \to \infty$. So $\alpha \to 0$ and $A \to \pi a^2$; at $s = 0$ the same formula gives $\alpha = 60^\circ$, the flat limit.

**Targets:** `curved-means-more-than-half-a-turn`

## Observations

- **The angle excess of the largest triangle in Gauss's survey of Hanover, joining the Brocken, the Hoher Hagen and the Inselsberg** (measured, working). Theodolite angles at the three summits are the angles of a geodesic triangle on Earth's surface, so they add up to more than $180^\circ$ by the area over the radius squared. Gauss quoted this triangle, with an excess of 14.85 arcseconds, as a worked example in his 1828 paper on curved surfaces. *Numbers:* Sides about 69, 85 and 107 km, area about 2930 km²: excess $A/a^2 = 14.9$ arcseconds with $a = 6371$ km, and 14.8 arcseconds with the local Gaussian radius of the flattened Earth near latitude $51.5^\circ$. *Reference:* Carl Friedrich Gauss (1828), *Disquisitiones generales circa superficies curvas*, Commentationes Societatis Regiae Scientiarum Gottingensis Recentiores 6, 99–146

## Teaching arc

1. **Predict the corners on a ball** (entry). Have the learner tear the corners off a paper triangle, then predict the corners of the North Pole triangle. *Why:* The paper result makes 270 degrees a real surprise. *Predict:* On a ball, will the three corners of a triangle made of straight walks add up to half a turn? *Visual:* [[carry-an-arrow-around-a-loop]] (preset `octant`) *Uses:* `ways_in/three-right-angles-on-a-ball`, `checks/north-pole-triangle-corners`
2. **Explain and count** (entry). Show that the corner where parallel walkers meet is the whole excess, then find the 720-degree rule from orange segments. *Why:* It answers why the excess exists and how big it is. *Predict:* If a triangle covers half as much of the ball, what happens to its angle excess? *Visual:* [[orange-segments-around-a-triangle]] *Uses:* `ways_in/walkers-who-start-parallel-meet`, `ways_in/excess-follows-the-share-of-the-ball`, `checks/small-triangle-on-a-field`
3. **Prove it and measure Earth** (working). Count lunes to prove Girard's theorem, change the sign on a hyperbolic plane, then turn an excess into a radius. *Why:* It fixes the sign and makes the theorem a measurement. *Uses:* `derivations/girard-by-counting-lunes`, `checks/hyperbolic-triangle-area`, `problems/radius-from-an-excess`
4. **Mark the hypotheses** (formal). Sketch Gauss's proof, then break its hypotheses with a cone point and a region larger than half the sphere. *Why:* Each limit adds a term the learner can compute. *Uses:* `ways_in/gauss-theorem-for-geodesic-triangles`, `checks/cone-tip-triangle`, `checks/both-regions-of-the-sphere`

## Misconceptions

### “The corners of every triangle add up to 180 degrees.” · entry · `corners-always-half-a-turn`

- **Why it is tempting:** School geometry proves it, and every triangle we draw agrees.
- **What is true:** That holds on flat ground, where walkers who start parallel never meet. On a ball, a triangle of straight walks can have three right angles.
- **Exposed by:** `checks/north-pole-triangle-corners`

### “If my triangle's corners add up to 180 degrees as far as I can measure, the ground is flat.” · entry · `measured-180-means-flat`

- **Why it is tempting:** Every triangle measured in daily life seems to give 180 degrees.
- **What is true:** On a ball the excess is 720 degrees times the share of the ball, so a small triangle on Earth has an excess far too small to measure with a protractor.
- **Exposed by:** `checks/small-triangle-on-a-field`

### “Any three-cornered region on a sphere has an angle excess equal to its area over the radius squared.” · working · `excess-for-any-three-sided-region`

- **Why it is tempting:** Girard's theorem is often quoted without saying that the sides must be great circles.
- **What is true:** A side that is not a geodesic, such as a circle of latitude, adds its integrated geodesic curvature to the angle sum.
- **Exposed by:** `checks/latitude-side-triangle`

### “On any curved surface, the angles of a triangle add up to more than 180 degrees.” · working · `curved-means-more-than-half-a-turn`

- **Why it is tempting:** The sphere is the curved surface everyone meets first.
- **What is true:** Where the Gaussian curvature is negative, as on a hyperbolic plane, the angles add up to less, by the area times the size of the curvature.
- **Exposed by:** `checks/hyperbolic-triangle-area`

## Checks

1. **Entry · predict** `checks/north-pole-triangle-corners`. On a giant smooth ball, you walk a triangle of three straight walks. You go from the North Pole to the equator, turn left, walk a quarter of the way around the equator, turn left again, and walk back to the North Pole. Measure each corner on the piece of the ball on your left as you walk. What do the three corners add up to, and what is the triangle's angle excess?
   - **Hints:** What angle does a line from the North Pole make with the equator?
   - **Answer:** They add up to 270 degrees, so the angle excess is 90 degrees. Each line from the North Pole meets the equator at a right angle, so the two corners on the equator are right angles. Think of an orange cut from top to bottom into four equal segments. The four corners at the top fill a full turn, so neighbouring cuts meet there at a right angle. Your first and last paths reach the equator a quarter of the way around apart, so they run along two neighbouring cuts and meet at a right angle too. Three right angles add up to 270 degrees, which is 90 degrees more than 180.
   - **Must contain:** The corners add up to 270 degrees; All three corners are right angles; The angle excess is 90 degrees
   - **Numeric:** sum of the corners = 270 deg (magnitude, ±5); angle excess = 90 deg (magnitude, ±5)
   - **Targets:** `corners-always-half-a-turn`
   - **Visual:** [[carry-an-arrow-around-a-loop]] (preset `octant`)
2. **Entry · evaluate-claim** `checks/small-triangle-on-a-field`. On a school field, a student marks a triangle of straight walks with three sides of 100 metres. Her protractor reads to half a degree, and the corners add up to 180 degrees. She says: "So Earth's surface is flat." Is she right?
   - **Hints:** How many square metres is her triangle, and how many square metres is Earth's surface?
   - **Answer:** No. On a ball, the angle excess is 720 degrees times the share of the ball the triangle covers. Her triangle is the triangle joining three towns 100 kilometres apart, shrunk a thousand times in each direction. So its area is a million times smaller, about 4,300 square metres. Earth's surface is about 510 million square kilometres, and each square kilometre is a million square metres. So her triangle covers one part in about 120 billion of Earth's surface. The angle excess is 720 degrees divided by 120 billion, about six billionths of a degree. Her protractor cannot show that, so her measurement cannot tell Earth from flat ground.
   - **Must contain:** No; The excess is about six billionths of a degree, far too small to measure
   - **Numeric:** angle excess = 6.1e-09 deg (magnitude, ±15%)
   - **Targets:** `measured-180-means-flat`
3. **Working · numeric** `checks/hyperbolic-triangle-area`. A hyperbolic plane has Gaussian curvature of minus one over 25 km² everywhere, so its length scale is 5 km. A geodesic triangle there has angles of 50°, 40° and 30°. What is its area? Can a geodesic triangle there have angles of 100°, 50° and 40°?
   - **Hints:** Convert the shortfall below 180° to radians.
   - **Answer:** The angles add up to 120°, short of 180° by 60°, which is $\pi/3 = 1.0472$ rad. Lambert's result, with $a = 5$ km, gives $A = a^2 \times 1.0472 = 25\ \text{km}^2 \times 1.0472 = 26.2$ km². The second set adds up to 190°, which would need a negative area, so no such triangle exists where $K < 0$ everywhere.
   - **Must contain:** The area is a squared times the shortfall of pi over 3, about 26.2 square kilometres; An angle sum above 180 degrees is impossible there
   - **Numeric:** area = 26.18 km^2 (magnitude, ±1%)
   - **Targets:** `curved-means-more-than-half-a-turn`
4. **Working · evaluate-claim** `checks/latitude-side-triangle`. On a sphere of radius 1000 km, a region is bounded by two meridians 90° apart and by the arc of the circle of latitude 45° between them, on the side of the pole. All three corners are right angles. A student concludes from Girard's theorem that its area is 1.571 million km². Evaluate the claim.
   - **Hints:** Which of the three sides is a great-circle arc?
   - **Answer:** Wrong, because the latitude arc is not a geodesic. With $a = 1000$ km, the region is a quarter of the polar cap, with area $\tfrac14 \cdot 2\pi a^2(1 - \cos 45^\circ) = 0.460\,a^2 = 0.460$ million km², not $1.571\,a^2$. The missing $1.111$ rad is the arc's integrated geodesic curvature: $\kappa_g = \cot 45^\circ/a = 1/a$, bending toward the region, over a length $\tfrac{\pi}{2}a\sin 45^\circ = 1.111\,a$. So $0.460 + 1.111 = \pi/2$, the angle sum minus $\pi$.
   - **Must contain:** The latitude arc is not a geodesic, so Girard's theorem does not apply; The true area is about 0.460 million square kilometres
   - **Numeric:** area = 460076 km^2 (magnitude, ±1%)
   - **Targets:** `excess-for-any-three-sided-region`
5. **Formal · derive** `checks/cone-tip-triangle`. A flat cone is made by removing a wedge of 60° from a sheet and joining the cut edges. A geodesic triangle avoids the tip but bounds a region containing it. Find the angle sum, say which hypothesis of Gauss's theorem fails, and repair the theorem.
   - **Hints:** Unroll the cone and count the angles of the flat polygon you get.
   - **Answer:** The angle sum is $240^\circ$, with wedge angle $\delta = 60^\circ$. Cut the cone along a geodesic from the tip to one vertex and unroll it. The triangle becomes a flat pentagon whose angles are the three triangle angles, with one split in two, plus $2\pi - \delta$ at the tip. A flat pentagon's angles add up to $3\pi$, so $\alpha_1 + \alpha_2 + \alpha_3 = \pi + \delta$. The smoothness hypothesis fails at the tip, where $K$ is undefined, while $K = 0$ elsewhere. Assigning the tip concentrated curvature $\delta$, the limit of rounding it off, restores $\sum\alpha_i - \pi = \iint K\,dA$.
   - **Must contain:** The angle sum is 240 degrees, pi plus delta; Counting curvature delta at the cone point repairs the theorem
   - **Numeric:** angle sum = 240 deg (magnitude, ±1)
6. **Formal · derive** `checks/both-regions-of-the-sphere`. On the unit sphere, three geodesic arcs bound a triangle and divide the sphere into two regions, each homeomorphic to a disk. Show that the angle excesses of the two regions, each with its angles measured inside it, add up to 720°, and relate this to the Gauss–Bonnet theorem for the whole sphere.
   - **Hints:** At each vertex, the two regions' angles fill a full turn.
   - **Answer:** If one region has angles $\alpha_i$, the other has $2\pi - \alpha_i$ at the same vertices. The excesses are $\sum\alpha_i - \pi$ and $\sum(2\pi - \alpha_i) - \pi = 5\pi - \sum\alpha_i$, which add up to $4\pi$. By Gauss's theorem each excess is the integral of $K = 1$ over its region, so their sum is the sphere's total curvature, $4\pi = 2\pi\chi(S^2)$ with $\chi(S^2) = 2$. For the octant triangle the two excesses are $\pi/2$ and $7\pi/2$.
   - **Must contain:** The two excesses add up to 4 pi; 4 pi is the sphere's total curvature, 2 pi times its Euler characteristic
   - **Numeric:** sum of the two excesses = 12.566 rad (magnitude, ±0.01)

## Notation traps

| Issue | Course choice | Variants you will meet |
| --- | --- | --- |
| Excess, defect and deficit | The angle excess is $E = \alpha_1 + \alpha_2 + \alpha_3 - \pi$, negative where $K < 0$. With the course sign $K = +1/a^2$ for a sphere, $E = \iint K\,dA$. | Some texts call $\pi - \sum\alpha_i$ the defect or deficit and quote it as positive for hyperbolic triangles. A cone's deficit angle is $2\pi$ minus its total angle at the tip. |

## Visuals

- ★ [[orange-segments-around-a-triangle]] (flagship): Builds any triangle on a ball and proves Girard's theorem by counting lunes. *Sketch:* A ball with three draggable vertices joined by great-circle arcs, with readouts of each angle, the angle sum, the excess and area over radius squared. A step mode extends the sides to great circles and lights the six lunes one at a time, tallying areas until the count closes. A switch measures the other region.
- [[carry-an-arrow-around-a-loop]] (supporting): Its angle-excess readout on the North Pole triangle.

## Tutor moves

**Open with**

- Picture a giant smooth ball. You walk a triangle on it made of three straight walks, never steering along each side. Do you think its three corners add up to half a turn, like a triangle on paper, or to something else? *(prediction)*

**If the learner is stuck**

- *The learner cannot find what share of the ball a triangle covers.* → Start from orange segments: if a segment's two cuts meet at the top at 10 degrees, the segment covers 10 parts in 360 of the ball, and the triangle between the equator and the North Pole is half of that segment. *Uses:* `ways_in/excess-follows-the-share-of-the-ball`

**Common questions**

- *Can the corners of a triangle ever add up to less than 180 degrees?* (entry) Yes. On saddle-shaped ground, like the part of a swim ring around its hole, walkers who start parallel spread apart. So to close a triangle there, two walkers must set off heading toward each other, which makes their two starting corners smaller, as on flat ground. As they walk, the spreading keeps pulling their paths apart, compared with lines on flat ground. When they meet, they are heading more nearly the same way than walkers on flat ground would be. So the corner where they meet is smaller than the amount the two starting corners lost, and the three corners add up to less than half a turn. The working level shows how much less. *Uses:* `ways_in/orange-segments-prove-it`, `checks/hyperbolic-triangle-area`

**Switching levels**

- To working when: asks why the rule holds for every triangle. Prove Girard's theorem by counting lunes, then change the sign on a hyperbolic plane. *Uses:* `ways_in/orange-segments-prove-it`, `derivations/girard-by-counting-lunes`
- To formal when: asks which surfaces the theorem needs; knows geodesic polar coordinates. State Gauss's theorem with its hypotheses, then test it on a cone point. *Uses:* `ways_in/gauss-theorem-for-geodesic-triangles`, `checks/cone-tip-triangle`

**Pronunciations:** Girard → zhee-RAR; Legendre → luh-ZHAHN-druh; Lambert → LAHM-bairt; Gauss → GOWSS; Harriot → HAIR-ee-ut; Toponogov → tuh-puh-NOH-guff; Inselsberg → IN-zels-bairk; Hoher Hagen → HOH-er HAH-gen

## History

- **Thomas Harriot (1603).** Found the area of a spherical triangle from its angle excess, in unpublished manuscripts.
- **Albert Girard (1629).** Published the spherical excess rule, which Harriot had found but not published. Albert Girard (1629), *Invention nouvelle en l'algèbre*, Amsterdam
- **Johann Heinrich Lambert (1766).** In a study of the parallel postulate, showed that if triangles' angles fall short of $\pi$, the shortfall is proportional to area; written in 1766 and published in 1786.
- **Carl Friedrich Gauss (1827).** Proved that a geodesic triangle's excess equals its total curvature on any smooth surface in space. Presented in 1827 and published in 1828. Carl Friedrich Gauss (1828), *Disquisitiones generales circa superficies curvas*, Commentationes Societatis Regiae Scientiarum Gottingensis Recentiores 6, 99–146

## Review: novice

**Verdict:** fixed (2026-09-13, revision 8)

**Retell attempt:** A paper triangle's torn-off corners always make half a turn, 180 degrees. On a ball it is different: start at the North Pole, walk down to the equator, turn left, go a quarter of the way round, turn left again, and walk back up, and all three corners are right angles, so they make 270 and the extra 90 is the angle excess. The reason is that two walkers who set off side by side from the equator, both facing the North Pole, get drawn together and meet at the pole, and that meeting corner is all extra; on flat ground they would never meet. The size of the excess is 720 degrees times the share of the ball the triangle covers, which I could check with an orange cut into 36 segments: 10 degrees for one seventy-second of the ball. On Earth a triangle of towns 100 kilometres apart is only about six thousandths of a degree over, about a hair's width at arm's length, so nobody notices. Things I stumbled on: 'so it counts as straight', where I could not tell whether 'it' was the path or the walking; 'Turn left', which never says how far; 'Each of these two walks along one of the globe's lines', which I read as being about two walks and had to go back over; 'these two corners', when no triangle had been made yet; and 'the fraction of the ball's surface inside the triangle's sides', which seemed to clash with the next paragraph telling me the sides cut the ball into two pieces and I must pick one.

**Stumbles (15)**

- “On a ball, a triangle made of straight walks has corners that add up to more.”: The summary is the first thing a reader meets or hears, and 'straight walks' is a term the ways define later. A reader who has not met it cannot picture the triangle.
- “The extra, called the angle excess, is 720 degrees times the share of the ball the triangle covers.”: In the summary there is nothing to settle what 'the share of the ball' is a share of, so it reads as a share of the whole solid ball rather than of its surface.
- “So someone who never leaves a ball can find out that it is curved, by measuring the corners of a big enough triangle.”: 'Never leaves a ball' reads as never leaving the object, not its surface, and 'it' has two candidates, the ball and the triangle.
- “The path bends over the ball's curve, but the walker never steers, so it counts as straight.”: 'It' could be the path or the walking, and the sentence is the one that fixes what 'straight' means, so the reader cannot afford to guess.
- “Turn left and walk a quarter of the way around the equator.”: A rule the reader cannot follow as written: it does not say how far to turn. Naming an amount would be worse here, because a quarter turn at that corner is also the size of the corner, and the two are different things.
- “Each band should split the orange into two equal halves.”: A step left implicit. The reader is not told why halving matters, so the instruction looks like fussiness instead of the thing that makes each band a straight walk.
- “That includes ground that only looks bent, like a can's label, which unrolls onto a table without stretching.”: A can's label is not ground, so the example does not match the noun; the glossary calls the same thing a surface, so one idea has two words.
- “Each walker's path makes a right angle with the straight walk, so these two corners already add up to half a turn.”: 'These two corners' are corners of nothing yet: the sentence before only stands the walkers side by side, and the sentence after says no triangle closes.
- “Each of these two walks along one of the globe's lines to the North Pole, so they meet there.”: 'These two walks' reads as a noun phrase, so the sentence has to be read twice. The note uses 'walk' as a noun for a path elsewhere, which makes the garden path worse.
- “That triangle is the half of one segment between the North Pole and the equator.”: Has to be reread: 'between the North Pole and the equator' attaches to 'segment' on a first reading, and a segment runs from top to bottom.
- “The angle excess is 720 degrees times the share of the ball the triangle covers, meaning the fraction of the ball's surface inside the triangle's sides.”: 'Inside the triangle's sides' says inside a loop on a closed surface, which picks out nothing, and the next paragraph has to take it back by saying the sides cut the ball into two pieces.
- “The three sides cut the ball into two pieces, so the corners and the share must be taken on the same piece.”: 'Taken on' for measuring. The way 'A triangle with three right angles' says corners are 'measured on that piece', so one idea has two words.
- “No protractor shows that, which is why triangles marked out on the ground seem to add up to exactly 180 degrees.”: Triangles do not add up; their corners do. The sentence drops the noun the rest of the note keeps.
- “Her triangle is the three-towns triangle, 100 kilometres a side, shrunk a thousand times in each direction.”: 'The three-towns triangle' is a name the entry ways never give, so the reader has to guess which triangle the answer means.
- “a segment whose cuts meet at the top at some number of degrees covers that number divided by 360 of the ball”: The tutor says this out loud, and 'that number divided by 360 of the ball' cannot be followed by ear on one hearing.

**Fixes**

- Summary: gives the rule instead of the undefined term ('walk the three sides of a triangle without ever steering left or right'), says share of the ball's surface, and drops the ambiguous 'it'. Still four sentences, average 19 words.
- Entry way 'A triangle with three right angles': 'so the path counts as straight' names the noun; 'Turn left onto the equator' makes the turn doable without naming an amount a reader could mistake for the corner angle; the try-it now says why each band must halve the orange.
- Entry way 'Walkers who start parallel meet': the recap says surface, not ground, for a can's label; 'these two corners of a triangle'; 'Each walker follows one of the globe's lines' removes the walks-for-walkers garden path.
- Entry way 'The excess follows the share of the ball': the share is now defined as the triangle's own area over the ball's whole surface, with no 'inside the sides'; 'the top half of one segment'; 'measured on the same piece'; 'the corners of triangles marked out on the ground'.
- Entry check 'small-triangle-on-a-field': the earlier triangle is named by its description instead of by a name the ways never give.
- Tutor if-stuck move 'finding-the-share': a concrete 10-degree segment replaces 'that number divided by 360 of the ball', so the move can be followed by ear.
- Ladder: read the working and formal ways as a stronger student. Each non-entry way's first sentence names the way it continues; the bridges from straight walk to geodesic, from 'a quarter of the ball' to A over 4 pi a squared, and from Girard's theorem to Gauss's theorem are all present; no index notation appears at the working rung. Nothing was missing, so no bridge was added.
- Nothing was dropped. Entry explanations rose from 1070 to 1083 words, inside the review allowance of 1100 on the foundation cap of 1000, all for recorded stumble fixes. Way extras 576 of 650, tutoring 1892 of 2200, total 6025 of 7000.
- Bumped the revision to 5 and set the status to novice-reviewed, because eight learner-visible strings changed after the physics sign-off.
- This was a second, independent novice pass, over revision 4. The schema holds one novice stage record, so the first pass's verdict and its 25 stumbles are replaced by this one; its re-read of the physics changes is kept in rereads, and its concerns that are still live are carried into concerns.

**Concerns**

- Eight learner-visible strings changed after the physics review signed revision 4, all at the entry rung, so they need a physics diff check before the status returns to physics-reviewed. None touches a number or an equation. The one claim worth checking is the added try-it clause 'which makes each band a straight walk': a circle on a sphere cuts the surface into two pieces of the same area exactly when it is a great circle.
- Entry explanations sit at 1083 words, past the foundation cap of 1000 and inside the review allowance. Any further entry addition must drop something; the lowest-value candidate is still the which-piece paragraph of 'The excess follows the share of the ball', which could become an entry check.
- Rule 17: 'The excess follows the share of the ball' carries the 720-degree rule and then the which-piece scope, which is close to a second idea in one entry way. I left it, because the scope is what keeps the rule true, but if that way is ever split, the which-piece paragraph is the part to move.
- Carried forward: course-conventions.md still has no row for an angle-excess symbol or its sign. The note's E as the angle sum minus pi, negative where the Gaussian curvature is negative, stays note-local until a row is added.
- Carried forward: the prerequisite great-circle-geodesics has no note yet, so the entry ways restate straight walks on a ball in their own words, including the small-circle sentence and the new try-it clause. Align them when that note is written.
- Carried forward: the flagship visual orange-segments-around-a-triangle is still a proposal. When it is catalogued it should name the triangle as the piece on the walker's left and use 'share of the ball' for the surface fraction, to match this note.

**Re-read** (2026-09-13, revision 4): 1 stumbles in 3 changed passages

- “Gauss quoted this triangle, with an excess of 14.85 arcseconds, as a worked example in his memoir on curved surfaces.”: Word used in two senses: to most readers a 'memoir' is an autobiography, so the sentence suggests Gauss wrote about the triangle in his life story rather than in a research paper.
- Fix: Observation hanover-survey-triangle: 'his memoir on curved surfaces' became 'his 1828 paper on curved surfaces', matching the reference's year and kind; the claim and the 14.85-arcsecond figure are unchanged.
- Fix: Way surveyors-measure-the-excess: the corrected sentence on Earth's curvature being about 1.3% smaller at the flattened poles reads cleanly in its paragraph ('flattened' and 'smaller curvature' point the same way); no change.

**Re-read** (2026-09-13, revision 7): 2 stumbles in 2 changed passages

- “The error falls as $(\ell/a)^2$ relative to the excess for sides of length $\ell$, with a small numerical factor that vanishes when the triangle is equilateral.”: "The error" arrives as a definite noun with nothing to attach it to. The sentence before says the reduction gives the flat triangle with the same sides, so it reads as exact, and then an error appears with no owner. A reader climbing the ladder has to guess whether it is an error in the reduced angles, in the side lengths, or in the excess itself, and has to reread the paragraph to decide.
- “The error falls as $(\ell/a)^2$ relative to the excess for sides of length $\ell$, with a small numerical factor that vanishes when the triangle is equilateral.”: Wording squeezed to fit: one 26-word clause carries three separate things (how the error scales, that the comparison is with the excess and not with the angle, and that the prefactor can be zero), and $\ell$ is used five words before it is defined, so the reader meets the symbol, guesses, then has the guess confirmed at the end of the clause.
- Fix: Way surveyors-measure-the-excess, third paragraph: the single sentence the physics review rewrote became three. The first names the error and says what it is an error in, which also tells the reader that the preceding sentence ('the result is the flat triangle with the same side lengths') is an approximation. The second gives the scaling with $\ell$ defined before it is used. The third carries the equilateral case on its own.
- Fix: The claim is unchanged: the same $(\ell/a)^2$ scaling relative to the excess, the same small numerical factor, the same vanishing for an equilateral triangle, and the same $10^{-4}$ arcsecond bound for the Hanover triangle. Checked against the numbers: for sides 69, 85 and 107 km on a 6371 km sphere the excess is 14.89 arcseconds, the per-angle errors are 3.5e-6, 1.9e-5 and 2.2e-5 arcseconds, the factor is 0.0013 to 0.0080, and for equal sides the error is zero to rounding.
- Fix: Vocabulary held to one word per idea: 'flat triangle' throughout, not 'plane triangle'; 'error' for the departure from Legendre's theorem and 'excess' for the angle excess, never swapped.
- Fix: Budget: the working way goes from 636 to 646 words against a cap of 900, so nothing was dropped or shortened. The entry rung was untouched and stays at 1083 words.
- Fix: Nothing at the entry rung changed in this round, so rule 17 had no target: the one changed string is working-rung text and the entry ways the earlier novice pass signed are untouched.

**Re-read** (2026-09-13, revision 8): 0 stumbles in 3 changed passages


## Review: physics

**Verdict:** fixed (2026-09-13, revision 8)

**Verification**

- Novice rewrite, try-it: 'Each band should split the orange into two halves of the same size, which makes each band a straight walk.': Cap area on a sphere of radius a at angular radius theta is 2 pi a^2 (1 - cos theta), so the share is (1 - cos theta)/2; solved for share 1/2. Also asked whether the implication holds for curves that are not circles. → python: shares 0.067, 0.250, 0.500, 0.750 at theta = 30, 60, 90, 120 degrees, so a circle halves the surface exactly when theta = 90 degrees, that is when it is a great circle, which is a geodesic. True as written, because a rubber band round an orange lies as a circle. The implication is false for general curves (see counterexamples), so the sentence keeps its scope from the word 'band'. No change.
- Novice rewrite, summary: 'On a ball, walk the three sides of a triangle without ever steering left or right, and its corners add up to more.' - no scope word on 'more'.: Girard for both regions the three arcs bound: excess of the complement is 4 pi - E in radians, with 0 < E < 4 pi. → Both pieces have a strictly positive excess, so the sentence is true whichever piece the reader takes as the triangle, and needs no 'most triangles' scope. Correct.
- Novice rewrite, summary: '720 degrees times the share of the ball's surface the triangle covers'.: E(deg) = (180/pi) A/a^2 with share s = A/(4 pi a^2), so E(deg) = 720 s. → Exact. 'Ball's surface' is the right denominator, and is what the working rung uses as 4 pi a^2. Correct.
- Novice rewrite, summary: 'measuring a big enough triangle tells someone who never leaves the ball's surface that the ball is curved'.: Checked that the quantity named is intrinsic: E = integral of K dA needs only angles and area measured within the surface. → Correct and intrinsic; 'big enough' is the necessary scope, since the entry number shows a 100 km triangle gives six thousandths of a degree.
- Novice rewrite, way 'A triangle with three right angles': 'Turn left onto the equator and walk a quarter of the way around it', and 'The triangle is the piece of the ball on your left as you walk.': Traced the three headings with the walker's head along the outward normal: facing south from the pole, left is east; facing east on the equator, left is north; facing north on the second meridian, left is west. → The same octant lies on the left along all three sides, and it is the piece with three right angles, 270 degrees. The new wording does not change the region or the sense. Correct.
- Novice rewrite, way 'Walkers who start parallel meet': 'these two corners of a triangle already add up to half a turn' and 'Each walker follows one of the globe's lines to the North Pole, so they meet there.': Angle sum for the equator-to-pole triangle: 90 + 90 + apex - 180 = apex. Two meridians meet only at the poles. → Both correct: the two base corners are right angles whatever the longitude gap, and the whole apex angle is the excess. Correct.
- Novice rewrite, recap: 'a surface that only looks bent, like a can's label, which unrolls onto a table without stretching'.: Cylinder has K = 0; geodesics that start parallel keep their separation. → Correct; the swap of 'ground' for 'surface' changes no physics.
- Novice rewrite, way 'The excess follows the share of the ball': 'the top half of one segment, the part between the equator and the North Pole', 'The share is the triangle's own area as a fraction of the ball's whole surface', and 'the corners and the share must be measured on the same piece'.: Lune of angle alpha has area 2 alpha a^2, share alpha/2 pi; the equator bisects it by reflection symmetry. Complement check: octant complement has 810 degrees of corner, excess 630 = 720 x 7/8. → A 10-degree lune is 10 parts in 360 of the surface, its top half 1/72, and 72 x 10 = 720. The which-piece sentence is exactly the condition that makes the rule true on either piece. Correct.
- Novice rewrite, entry check small-triangle-on-a-field: 'the triangle joining three towns 100 kilometres apart, shrunk a thousand times in each direction', area about 4,300 square metres, one part in about 120 billion, excess about six billionths of a degree.: python: sqrt(3)/4 x (100 m)^2; Earth's surface 5.10072e14 m^2; 720 degrees divided by the share. → 4330 m^2, one part in 1.178e11, excess 6.112e-9 degrees. Matches the numeric field 6.1e-9 within its 15% tolerance, and the renaming introduces no new number. Correct.
- Novice rewrite, tutor if-stuck 'finding-the-share': a 10-degree segment covers 10 parts in 360 of the ball, and the triangle between the equator and the North Pole is half of that segment.: Lune share alpha/2 pi = 10/360; reflection symmetry in the equator. → Correct, and it agrees with the entry way's 36-segment orange.
- Girard's theorem E = alpha_1 + alpha_2 + alpha_3 - pi = A/a^2, and its lune proof.: Re-derived: a lune of angle alpha is the fraction alpha/2 pi of the sphere, area 2 alpha a^2; the three lune pairs have total area 4 a^2 sum(alpha_i) and cover the sphere once plus T and its antipodal copy twice more each, giving 4 a^2 sum(alpha_i) = 4 pi a^2 + 4A. → Correct, including the factor 4 and the coverage count (six lunes, T and T' three times, the other six triangles once). Divided by 4 a^2 gives the theorem. The complementary region satisfies the same relation: sum(2 pi - alpha_i) - pi = 4 pi - A/a^2 = (4 pi a^2 - A)/a^2.
- 720 degrees is 4 pi radians, and the entry rule is the same statement as Girard's theorem.: Arithmetic. → Correct.
- Gauss's theorem E = double integral of K dA, with K = +1/a^2 on a sphere, negative-curvature case E = -A/a^2, and no hyperbolic triangle of area pi a^2 or more.: Checked against the conventions rows for sectional curvature (sphere K = +1/a^2) and orientation; the bound follows from every interior angle being positive. → Signs agree with the course conventions. A = a^2(pi - sum alpha) < pi a^2. Correct.
- Formal proof sketch: geodesic polar coordinates ds^2 = dr^2 + G dphi^2, sqrt G = r - K r^3/6 + O(r^4), K = -(d_r^2 sqrt G)/sqrt G, integral of K dA = integral of (1 - d_r sqrt G) dphi, d psi = -d_r sqrt G dphi, psi from pi - alpha_q at q to alpha_r at r.: Re-derived each step; tested on the flat plane with p = (0,0), q = (1,0), r = (0,1), where sqrt G = r. → d_r sqrt G = 1 at r = 0 supplies the '1'; on the plane psi(q) = 135 degrees = pi - alpha_q and psi(r) = 45 degrees = alpha_r, and the total is alpha_p + alpha_r - (pi - alpha_q) = 0. Correct.
- Additivity of excess over a subdivision using F - L + V = 1.: Counted 3F = 2L_interior + L_boundary, L_boundary = 3 + V_side, V = 3 + V_interior + V_side. → Gives 2 V_interior + V_side - F = -1, exactly the cancellation of 2 pi per interior vertex and pi per side vertex. Correct.
- Formal limits: a cone point of total angle 2 pi - delta adds delta; non-geodesic sides add the integral of kappa_g, positive where a side bends toward the region; a region that is not a disk obeys integral K dA + sum(pi - alpha_i) = 2 pi chi.: Local Gauss-Bonnet with corners, checked against the note's own latitude-side check, and specialised to a disk with three vertices. → The disk case returns sum alpha - pi = integral K dA, and the latitude case balances numerically (below). Signs correct.
- Toponogov comparison as stated for higher dimensions.: Compared with the standard globalisation statement: complete manifold, sectional curvature at least k, minimizing sides, perimeter restriction when k > 0. → Correct as stated, with 'the standard side-length conditions when k > 0' carrying the perimeter hypothesis.
- Entry number: a triangle joining three towns 100 km apart covers about 4,300 km^2, one part in about 118,000 of Earth's 510 million km^2, excess about six thousandths of a degree, a hair's width at arm's length.: python: sqrt(3)/4 x (100 km)^2; cross-checked the excess both as 720/share and as A/a^2 with a = 6371 km; converted the angle to a width at 0.65 m. → 4330 km^2; one part in 117,796; 0.006112 degrees by both routes; 1.067e-4 rad subtends 69 micrometres at 65 cm, a typical hair. Correct.
- Worked example, 1000 km equilateral triangle: cos alpha = cos c/(1 + cos c) = 0.49690, alpha = 60.2044 degrees, E = 0.6131 degrees = 0.010701 rad, A = 4.3435e5 km^2, flat area 4.3301e5 km^2 (0.31% less), flat area over a^2 = 0.6112 degrees, each angle one third of the excess above 60 degrees.: Derived the equilateral law of cosines from cos c = cos a cos b + sin a sin b cos C; python, cross-checked against the general spherical law of cosines. → c = 0.156961 rad, cos alpha = 0.496908, alpha = 60.20437 degrees, E = 0.613123 degrees = 0.0107010 rad (36.79 arcminutes), A = 4.34351e5 km^2, flat 4.33013e5 km^2 which is 0.308% less, flat/a^2 = 0.611235 degrees, and alpha - 60 = 0.204374 = E/3 exactly. All values correct as quoted.
- Working way: one arcsecond is 4.848e-6 rad and a^2 times one arcsecond is 197 km^2 on Earth.: python with a = 6371 km. → 4.84814e-6 rad; 196.78 km^2. Correct to the quoted precision.
- Hanover triangle: sides about 69, 85 and 107 km, area about 2930 km^2, angles adding to 180 degrees plus about 15 arcseconds; observation quotes Gauss's 14.85 arcseconds and 14.8 with the local Gaussian radius.: python: Heron's formula; A/a^2 with a = 6371 km; WGS84 meridional and normal radii M and N at latitude 51.5 degrees, local Gaussian radius sqrt(MN). → Heron area 2929.4 km^2; excess 14.89 arcseconds at a = 6371 km; sqrt(MN) = 6382.9 km gives 14.83 arcseconds. Gauss's quoted 14.85348 arcseconds sits between them. Correct.
- Legendre's theorem error: 'smaller than the excess by a factor of order (l/a)^2 for sides of length l; for the Hanover triangle it is below 1e-4 arcseconds'.: python: exact spherical angles from the spherical law of cosines, minus E/3, compared with the plane angles of the same sides, for the Hanover shape scaled by 1, 2, 4 and 8, and for a scan of shapes with sides 10-200 km. → The scaling is right - the ratio error/(E (l/a)^2) is a constant 0.0053 for the Hanover shape at every size - but the numerical factor is about 1/190, so the stated order estimate gives 4.2e-3 arcseconds while the true error is 2.2e-5 arcseconds, contradicting the same sentence's 'below 1e-4 arcseconds' by a factor near 200. The factor is shape-dependent (up to about 0.04 for near-degenerate shapes) and is exactly zero for an equilateral triangle, since (pi + E)/3 - E/3 = pi/3 identically. Sentence rewritten; the 1e-4 figure is confirmed (errors 1.9e-5, 3.5e-6, -2.2e-5 arcseconds).
- Earth's Gaussian curvature is about 1.3% smaller at the poles than at the equator.: python: K = 1/(MN) on the WGS84 ellipsoid, so K_pole/K_equator = (1 - f)^4. → 0.98666, that is 1.334% smaller at the flattened poles. Correct in size and sense.
- Problem twenty-triangle-ball: five triangles at a vertex give 72-degree corners, sum 216, excess 36 degrees = 720/20.: Hand arithmetic for the icosahedral geodesic tiling; cross-checked with E = A/a^2 for one twentieth of the sphere. → 360/5 = 72; 3 x 72 - 180 = 36; (1/20) x 4 pi = 0.6283 rad = 36.0 degrees. Correct; numeric field 36 deg +/- 1.
- Problem radius-from-an-excess: a = sqrt(A/E) = 6369 km; 0.5 arcseconds is 3.4% of the excess, so the radius moves 1.7%, about 110 km, with 14.4 and 15.4 arcseconds giving 6478 and 6264 km.: python. → E = 7.2237e-5 rad, a = 6368.7 km, 3.356%, half of that 1.678%, 106.9 km; 6478.4 and 6264.5 km. Correct; numeric field 6369 km +/- 1%.
- Check hyperbolic-triangle-area: K = -1/(25 km^2), a = 5 km, angles 50 + 40 + 30 = 120 degrees, area 26.2 km^2; angles of 100 + 50 + 40 impossible.: python: A = a^2 (pi - sum alpha); sign of the integral of K where K < 0 everywhere on a simply connected surface, where every geodesic triangle bounds a disk. → shortfall pi/3 = 1.04720 rad, area 26.180 km^2, inside the 1% tolerance of the numeric field. A sum of 190 degrees needs a positive integral of K, impossible. Correct.
- Check latitude-side-triangle: true area 0.460 a^2 = 460,076 km^2, not 1.571 a^2; kappa_g = cot 45 degrees/a over a length 1.111 a makes up the difference.: python: quarter cap area (1/4) 2 pi a^2 (1 - cos 45 degrees); geodesic curvature of a latitude circle at colatitude theta is cot(theta)/a; local Gauss-Bonnet with three right-angle corners. → 460,075.6 km^2 (numeric field 460,076 km^2); 0.46008 + 1.11072 = 1.57080 = pi/2 exactly; and 0.46008 + 1.11072 + 3 x (pi/2) = 2 pi, so Gauss-Bonnet closes. The arc bends toward the polar region, so the sign is positive. The student's Girard value 1.571 million km^2 is what the note says it is. Correct.
- Check cone-tip-triangle: wedge 60 degrees removed, angle sum 240 degrees = pi + delta.: Cut from the tip to one vertex and unroll: a flat pentagon with the tip angle 2 pi - delta, one triangle angle split in two, and angle sum 3 pi. → (2 pi - delta) + sum alpha = 3 pi gives sum alpha = pi + delta = 240 degrees. Correct; numeric field 240 deg +/- 1.
- Check both-regions-of-the-sphere: the two excesses add to 4 pi = 2 pi chi(S^2), and the octant pair is pi/2 and 7 pi/2.: python; the complement's angles are 2 pi - alpha_i at the same vertices. → (sum alpha - pi) + (5 pi - sum alpha) = 4 pi = 12.566 rad, matching the numeric field within 0.01. The octant pair pi/2 and 7 pi/2 agrees with the conventions file's orientation row, which quotes 7 pi/2 for the reversed octant loop. Correct.
- Entry common question on saddle-shaped ground: the meeting corner is smaller than the amount the two starting corners lost, so the three corners add up to less than half a turn.: Hyperbolic second law of cosines cos C = -cos A cos B + sin A sin B cosh c with A = B = 70 degrees and curvature -1, against the flat apex of 40 degrees. → c = 0.1 gives 39.60 degrees, c = 0.5 gives 28.51 degrees, and no triangle exists beyond c = 0.724, consistent with the sentence 'to close a triangle there'. The relation is correct in sign as well as in size.
- Problem hyperbolic-triangles-have-bounded-area: A = a^2(pi - sum alpha) < pi a^2, approached by equilateral triangles as the side grows, with cos alpha = cosh(s/a)/(1 + cosh(s/a)).: Derived the equilateral hyperbolic law of cosines from cosh c = cosh a cosh b - sinh a sinh b cos C; python limits. → s/a = 0 gives 60 degrees (flat limit), s/a = 5 gives 9.35 degrees and area 2.652 a^2, s/a = 20 gives 0.0052 degrees and area 3.1413 a^2, approaching pi a^2. Correct.
- Sign and sense: E = sum alpha - pi = integral of K dA, positive where K > 0, with the region on the walker's left.: Conventions file rows for sectional curvature and for orientation and rotation sense. → Consistent: the walk described in the entry way keeps the octant on the left and gives a positive excess, and the leads_to claim that an arrow returns turned by the excess matches the holonomy row. The conventions file still has no row naming a symbol for the angle excess; reported again.
- Reference: Gauss (1828), Disquisitiones generales circa superficies curvas, Commentationes Societatis Regiae Scientiarum Gottingensis Recentiores 6, 99-146.: Web search of library, archive and history-of-mathematics records. → Confirmed: read to the Gottingen society on 8 October 1827 and printed in volume 6 (1828), pages 99-146. No DOI or arXiv id exists. verified stays true.
- Reference: Girard (1629), Invention nouvelle en l'algebre, Amsterdam.: Web search (MacTutor, Gallica, Internet Archive, survey articles on spherical geometry). → Confirmed, including the section on the area of spherical triangles and polygons, published in Amsterdam in 1629. verified stays true.
- History scope: Harriot 1603 unpublished; Girard published the rule in 1629; Lambert's proportionality written 1766 and published 1786; Gauss proved the general theorem for surfaces in space, presented 1827 and published 1828; Gauss's quoted excess 14.85 arcseconds.: Web search for each claim. → All confirmed. Harriot found the spherical-excess area rule in 1603 and did not publish it; Lambert's Theorie der Parallellinien was written in 1766 and published in 1786, and the area-proportional-to-defect result sits under his acute-angle hypothesis in a study of the parallel postulate, which is how the note scopes it; Gauss's 14.85348 arcseconds for the Hohehagen-Brocken-Inselsberg triangle is confirmed. One nuance worth recording rather than writing into the note: some accounts hold Girard's argument incomplete and credit the first full proof to a contemporary three years later, so the note's wording 'published the spherical excess rule' is the safe scope and stays.
- Structure: prerequisites direct and acyclic; assumes at or below each way's rung; formal rung has two formal checks and one formal problem; every check and problem evidences an objective at its own rung; misconception and check links agree; visual ids and presets exist or are proposed with sketches.: Read the registry and the prerequisite notes' own prerequisite lists; listed objectives, checks, problems and misconceptions from the JSON; listed the presets of carry-an-arrow-around-a-loop. → No cycle: neither curvature nor gaussian-curvature depends on angular-excess. assumes are curvature (entry) in an entry way and gaussian-curvature and great-circle-geodesics (working) in working and formal ways. Formal: two checks and one problem. Every objective is evidenced at its own rung and every check and problem is used. diagnosed_by and targets agree. Preset 'octant' exists in the catalogued visual; orange-segments-around-a-triangle is a proposal with a sketch. Nothing names or quotes a source book.

**Counterexamples tried**

- Great circle: the sphere's own geodesics, so 'straight walk' has the meaning the ways give it; the equator and the meridians used in the entry ways are great circles and the excess rule applies to them.
- A curve that halves the surface but is not a geodesic: take a great circle and push it out on one side and in on the other by equal areas. It splits the sphere into two equal pieces yet is not a straight walk, so 'halves the orange, therefore straight' is false for curves in general. The try-it sentence survives because its subject is a stretched rubber band, which lies as a circle on the orange, and among circles only the great circle halves the surface (a cap of angular radius theta covers (1 - cos theta)/2).
- The other piece of the sphere (a region bigger than half): the octant's complement has 810 degrees of corner angle and excess 630 = 720 x 7/8, so the entry rule holds only with the note's sentence that the corners and the share are measured on the same piece. Sentence present and necessary.
- Cone tip: breaks the smoothness hypothesis. The formal check adds the deficit delta, the working statement excludes cone points, and the entry ways use a smooth ball only.
- Bent but flat surface (a can's label, a cylinder): K = 0, so every geodesic triangle bounding a disk has zero excess. The entry recap uses exactly this case to separate looking bent from being curved. A geodesic loop round the cylinder bounds no disk and is excluded by the word 'such' in the working way.
- Non-geodesic side (a circle of latitude): the excess rule fails by the integrated geodesic curvature; handled by the working check, by the misconception on three-sided regions, and by the entry sentence that a small circle round the North Pole is not a straight walk.
- Negative curvature (the inner part of a swim ring, the hyperbolic plane): the angles fall short. Covered by the working way, the misconception, the entry common question and the numerical hyperbolic comparison.
- Figure-eight loop: not a geodesic triangle and not a simple closed curve, so it is outside every statement in the note; nothing in the note claims otherwise.
- Mobius band: not orientable, so 'the piece on your left' would not be globally defined. The note works only on a ball and on disks, so no statement is affected.
- Degenerate and near-degenerate triangles: for an equilateral spherical triangle Legendre's reduction is exact, and for a near-degenerate one its error coefficient is largest (about 0.04 of E (l/a)^2); both are why the order-of-magnitude form of the old Legendre sentence was wrong.
- Triangles with a side longer than half a great circle: the lune derivation is scoped to angles below pi and their complements, while Girard's theorem still holds through Gauss's theorem for any region homeomorphic to a disk. The key equation's conditions do not exclude these.
- Tiny triangles: the excess is too small to measure, which is why the summary's 'big enough triangle' scope is necessary; the entry number gives six thousandths of a degree for 100 km sides.
- Higher dimensions: a geodesic triangle need not lie in a totally geodesic surface, so the formal way says the theorem does not apply as stated and offers Toponogov comparison instead.
- Walkers who start parallel at antipodal points of the equator: their two meridians form one great circle and they still meet at the pole, so 'walkers who start parallel draw together' holds there too.

**Fixes**

- Working way 'Surveyors measure the excess': the Legendre error sentence said the error is 'smaller than the excess by a factor of order (l/a)^2', which predicts about 4e-3 arcseconds for the Hanover triangle and so contradicted the same sentence's correct figure of below 1e-4 arcseconds by a factor near 200. It now reads: 'The error falls as (l/a)^2 relative to the excess for sides of length l, with a small numerical factor that vanishes when the triangle is equilateral. For the Hanover triangle the error is below 1e-4 arcseconds.' The scaling (a coefficient of 0.0053 for this shape, constant as the triangle is scaled) and the vanishing for equilateral triangles, which follows from (pi + E)/3 - E/3 = pi/3, were both checked numerically.
- Nothing else was changed. All eight entry strings from the second novice pass were checked and are accurate; the try-it clause about a band halving the orange is true for a band, which lies as a circle, and the counterexample that makes it false for general curves is recorded rather than written into the entry prose.
- Nothing was dropped. The change adds 12 words to the working way, which moves from 627 to 639 words against a cap of 900. Entry explanations are untouched at 1083 words, still inside the review allowance but past the foundation cap, so the budget concern is carried forward, not worsened.
- Bumped the revision to 6 and set the status to physics-reviewed; one learner-visible string changed, at the working rung.

**Concerns**

- The one learner-visible change is at the working rung, in 'Surveyors measure the excess'. A novice re-read covers that sentence only; nothing at the entry rung moved.
- Carried forward: course-conventions.md still has no row for an angle-excess symbol or its sign. The note's E = alpha_1 + alpha_2 + alpha_3 - pi, negative where K < 0, is consistent with the sectional-curvature and orientation rows but stays note-local until a row is added. This needs an owner decision.
- Carried forward: entry way explanations are 1083 words against the foundation cap of 1000, inside the 10% review allowance. Any further entry addition must drop something; the lowest-value candidate remains the which-piece paragraph of 'The excess follows the share of the ball', which could become an entry check. Note that the paragraph is what keeps the share rule true on either piece, so it must move, not vanish.
- Carried forward: the prerequisite great-circle-geodesics has no note, so the entry ways restate straight walks on a ball in their own words. Align them when that note is written, and keep the band-halves-the-orange test with them, since it is the entry-level test for a great circle.
- Carried forward: the registry does not list gaussian-curvature among this note's prerequisites; sync_registry.py applies reviewed notes.
- Carried forward: the flagship visual orange-segments-around-a-triangle is still a proposal. When catalogued it should name the triangle as the piece on the walker's left, use 'share of the ball' for the surface fraction, and let its 'other region' switch show the complement's excess of 720 degrees minus the triangle's.
- The derivation 'Girard's theorem by counting lunes' covers triangles whose angles are each below pi, and their complements. Triangles with a side longer than half a great circle rely on Gauss's theorem instead; this is stated in the derivation's result, not in the key equation's conditions, which is the right place but worth remembering if the derivation is ever reused.
- Some historical accounts treat Girard's 1629 argument as incomplete and credit the first full proof to a contemporary in 1632. The note claims only that Girard published the rule, which is safe; if the history entry is ever expanded, that nuance belongs with it.

**Diff check** (2026-09-13, revision 4)

- Observation hanover-survey-triangle, connection: Gauss quoted this triangle, with an excess of 14.85 arcseconds, as a worked example in his 1828 paper on curved surfaces (was 'memoir').: Compared with the old sentence: only the description of the work changed. Web search confirmed that Disquisitiones generales circa superficies curvas was read to the Gottingen society on 8 October 1827 and printed in Commentationes Societatis Regiae Scientiarum Gottingensis Recentiores 6 (1828), pp. 99-146. That matches the reference's year, venue and kind. Web search (historical accounts of the Hohehagen-Brocken-Inselsberg triangle) confirmed Gauss's stated spherical excess of 14.85348 arcseconds. Recomputed in python3: Heron area for sides 69, 85, 107 km is 2929 km^2, and A/a^2 with a = 6371 km gives 14.89 arcseconds, consistent with the numbers field. → True, and it claims the same as before. 'Paper' and '1828' match the reference, which is dated by publication, not by the 1827 lecture. Excess, area and numbers are unchanged and consistent.

**Diff check** (2026-09-13, revision 8)

- The one changed string, ways_in[surveyors-measure-the-excess].explanation, paragraph 3: the error of Legendre's theorem scales so that error/excess is a numerical factor times $(\ell/a)^2$.: Recomputed from scratch in python3 with numerically stable formulas (half-angle tangents for the spherical and plane angles, L'Huilier for the excess; the naive spherical cosine rule loses twelve digits to cancellation for 100 km sides and gave spurious factors). For the Hanover shape 69 : 85 : 107 on $a = 6371$ km, and the same shape scaled by 1, 1/2 and 1/4, the ratio error$/(E(\ell/a)^2)$ with $\ell$ the root-mean-square side is (+0.00651, +0.00125, -0.00776) at every scale, stable to three digits. → True. The ratio is scale-free, so error/excess does go as $(\ell/a)^2$ and the error itself as $\ell^4/a^4$. The three per-angle errors sum to zero exactly, as they must, since the reduced angles and the flat angles each sum to $\pi$.
- That numerical factor is small, and it is a pure number only once the triangle's shape is fixed.: Swept shapes on a 200x200 grid of side ratios at fixed first side 100 km, taking $\ell$ as the root-mean-square side. Recorded the largest per-angle $|$factor$|$ for each shape. → Small is right: $|$factor$|$ stays below about 0.017 over the whole sweep, reached in the needle limit (100, 100, 2.5) km. But it is not one number: it runs from 0 at the equilateral shape to 0.017, so it is set by the shape, not universal. The written sentence said only 'a small numerical factor', which a reader could take for a constant. Fixed.
- 'For sides of length $\ell$' is the right scope for that sentence.: Read the sentence pair literally against the sentence after it. 'Sides of length $\ell$' names one length for all three sides, which is an equilateral triangle; the next sentence says the factor vanishes for an equilateral triangle. → False as written, and self-defeating: taken literally the two sentences together say the ratio is always zero. The Hanover triangle the paragraph is about has three different sides, so the sentence did not even cover its own example. $\ell$ is a size scale, not a common side length. Fixed to 'a triangle whose sides are of order $\ell$'.
- 'The theorem is not exact' holds without conditions.: Checked against the equilateral case the next sentence raises. For an equilateral spherical triangle every angle is $\alpha$, so $E = 3\alpha - \pi$ and each reduced angle is $\alpha - E/3 = \pi/3$, which is exactly the angle of the plane equilateral triangle with those sides, for any $\alpha$. Confirmed in python3 at sides 69, 1000 and 5000 km and at the octant triangle (side $\pi a/2 = 10008$ km, three right angles, $E = 90^\circ$): the reduced angle is 60.000000000000 degrees in every case. → Too strong as a bare universal. The theorem is exact for equilateral triangles at every size, not merely to leading order. Scoped to 'not exact in general', and the equilateral sentence now states the exactness rather than only the vanishing of the factor.
- 'For the Hanover triangle the error is below $10^{-4}$ arcseconds' (unchanged, but it is the sentence the changed scaling claim feeds).: python3, stable formulas, sides 69, 85, 107 km on $a = 6371$ km. → True. $E = 14.8869$ arcseconds and the per-angle errors are $+1.87\times10^{-5}$, $+3.59\times10^{-6}$ and $-2.22\times10^{-5}$ arcseconds, the largest well under $10^{-4}$.
- Surrounding unchanged numbers in the same way still hold, so the edited paragraph sits in a correct context.: python3: one arcsecond is $4.84814\times10^{-6}$ rad; $a^2$ times one arcsecond with $a = 6371$ km is 196.8 km$^2$; the excess 14.887 arcseconds gives an area of 2929.5 km$^2$. Oblateness: with WGS84 semi-axes $a_e = 6378.137$ km and $c = 6356.752$ km, $K_{\rm pole}/K_{\rm eq} = (c/a_e)^4 = 0.98666$. → All true. 197 km$^2$ per arcsecond, about 2930 km$^2$ and about 15 arcseconds are right, and the Gaussian curvature at the pole is 1.33% smaller than at the equator, matching the way's 'about 1.3% smaller' including its sign (an oblate Earth is flatter at the poles, so $K$ is smaller there).
- No convention is broken by the new wording.: Checked course-conventions.md. $a$ is the sphere radius throughout this way, matching 'with $a = 6371$ km'; $\ell$ appears nowhere else in the note; the working rung uses SI with accepted non-SI units, and the arcsecond is given its SI value on first use. No index notation is introduced. → Consistent. No new symbol or sign choice is needed, so no conventions gap is opened.
- Fix: Way surveyors-measure-the-excess, paragraph 3, sentence 'The theorem is not exact, so each reduced angle differs...': scoped to 'The theorem is not exact in general, so each reduced angle differs...'. Without the scope it contradicts the equilateral case two sentences later, where the reduction is exact.
- Fix: Same paragraph, 'For sides of length $\ell$, the ratio of this error to the excess is a small numerical factor times $(\ell/a)^2$.' became 'For a triangle whose sides are of order $\ell$, the ratio of this error to the excess is $(\ell/a)^2$ times a small numerical factor set by the triangle's shape.' Two fixes in one sentence: 'sides of length $\ell$' names a single length for all three sides, which is the equilateral triangle the next sentence excludes and is not the three-sided Hanover triangle the paragraph is about, so $\ell$ is now a size scale; and the factor is shape dependent, running from 0 to about 0.017 across shapes, so calling it only 'a small numerical factor' let a reader take it for a universal constant.
- Fix: Same paragraph, 'The factor vanishes when the triangle is equilateral.' became 'The factor is zero for an equilateral triangle, where the reduction is exact at every size.' The stronger statement is exactly true: an equilateral spherical triangle of any size reduces to exactly 60 degrees, so a reader is not left asking to what order the factor vanishes.
- Fix: The scaling claim itself is unchanged: the same $(\ell/a)^2$ dependence relative to the excess, the same smallness of the factor, the same vanishing at the equilateral shape, and the same $10^{-4}$ arcsecond bound for Hanover. Only the scope and the shape dependence were missing.
- Fix: Vocabulary held to the paragraph's existing words: 'flat triangle', not 'plane triangle'; 'error' for the departure from Legendre's theorem and 'excess' for the angle excess; 'reduction' is used once, and the paragraph already says 'reduced angle'.
- Fix: Budget: nothing was dropped or shortened. The working way gains 12 words against a 900-word cap. The entry rung was not touched and stays at 1083 words.
