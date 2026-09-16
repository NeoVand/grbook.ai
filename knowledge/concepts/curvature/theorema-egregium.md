---
type: "concept"
schema_version: 2
id: "theorema-egregium"
title: "Theorema egregium"
tagline: "Why bending a surface without stretching never changes its Gaussian curvature"
domain: "curvature"
tier: "foundation"
status: "physics-reviewed"
revision: 5
updated: "2026-09-13"
aliases: ["Gauss's remarkable theorem"]
prerequisites: ["gaussian-curvature", "intrinsic-geometry", "riemann-curvature-tensor"]
leads_to: ["embedding-diagram", "second-fundamental-form", "gauss-codazzi-equations"]
visuals: ["half-ball-closes-into-a-lemon", "paced-ring-on-a-ball-and-a-plain", "funnel-drawn-over-a-star"]
---

# Theorema egregium

*Why bending a surface without stretching never changes its Gaussian curvature*

`theorema-egregium` · curvature · foundation · physics-reviewed (revision 5)

**Needs:** [[gaussian-curvature]] (entry) · [[intrinsic-geometry]] (entry) · [[riemann-curvature-tensor]] (formal)  
**Opens:** [[embedding-diagram]] · [[second-fundamental-form]] · [[gauss-codazzi-equations]]  
**Related:** [[principal-curvatures]]  
**Visuals:** ★ [[half-ball-closes-into-a-lemon]] · [[paced-ring-on-a-ball-and-a-plain]] · [[funnel-drawn-over-a-star]]

> Bend a thin shell without stretching or creasing it. At each smooth spot, the sharpest and gentlest bends can change, but the Gaussian curvature built from them stays the same. Gauss proved this in 1827 and called it his remarkable theorem, because an ant measuring only along the surface can find that number. Flat paper's number is zero, and a round Earth's is not. So no flat map shows every distance in even a small area of Earth exactly to scale.

## You will be able to

**Entry**
- Explain why bending a shell without stretching can change the two bends at a spot but not the Gaussian curvature there, and predict one bend from the other. `objectives/explain-why-bends-trade` ← `checks/squeeze-a-shell-from-a-ball`
- Explain why no flat map of a region of Earth is exactly to scale everywhere, and why a town map still looks perfect. `objectives/explain-why-maps-distort` ← `checks/perfect-town-map`

**Working**
- Compute a surface of revolution's Gaussian curvature from its line element and from its bends, and show that the line element fixes only their product. `objectives/compute-both-routes-on-a-surface-of-revolution` ← `problems/lemon-from-a-third-of-a-ball`
- Read the curvature of a slice of space from its embedding diagram, and say which features of the drawing carry geometry. `objectives/read-curvature-from-an-embedding-diagram` ← `checks/funnel-wall-at-the-horizon`

**Formal**
- Derive the Gaussian curvature of an orthogonal metric, and show that no chart of a sphere has a constant scale. `objectives/derive-k-from-an-orthogonal-metric` ← `problems/curvature-from-an-orthogonal-metric`
- Use the Gauss equation for surfaces in curved spaces and for hypersurfaces of higher dimension. `objectives/apply-the-gauss-equation-beyond-flat-space` ← `checks/flat-torus-in-the-three-sphere`, `checks/hypersurface-in-four-dimensions`

## Ways in

### 1. A half-ball closes into a lemon · entry · picture

*When you bend a curved shell without stretching it, what happens to the two bends at a spot?*

**Recap:** Walking without ever steering left or right is called walking straight. Where a path bends, one circle matches the bend best. This is called its best-fit circle; the smaller it is, the sharper the bend. An outsider, looking from the room around a shell, finds a spot's sharpest and gentlest bends. When both go toward the same face, multiply the radii of their circles and divide 1 by the result: this is the spot's Gaussian curvature. If one of the two does not bend at all, as along a rolled poster, the number is zero. An ant who never leaves the surface can find that same number from rings she walks out and measures along the surface. Her number and the outsider's agree at every smooth spot.

Picture a thin, hollow plastic ball, 20 centimetres across. Mark two dots on it exactly opposite each other, like the stalk end of an orange and the point across from it. Cut the ball in half along a circle through both dots, the way you would cut an orange through its stalk end. Keep one half. This half-ball is shaped like a bowl. The plastic bends easily, but it never stretches or creases.

Every spot on the half-ball curves like the ball it came from. Through any spot, every path an ant could walk straight along bends with a best-fit circle that goes all the way around the ball. The ball is 20 centimetres across, so that circle is too, and its radius is half of 20, which is 10 centimetres. 10 times 10 is 100, so the Gaussian curvature there is 1 divided by 100. That is 1 hundredth per square centimetre.

The two dots split the half-ball's rim into two half-circles. Squeeze the half-ball so that these two half-circles come toward each other, until they meet along their whole length. Tape them together. The shell is now a lemon shape, and the two dots are its sharp tips. Every other spot of the lemon is smooth.

Now look at the middle path, the path along the shell halfway between the two dots. On the half-ball, the middle path was half of the ball's circle halfway between the dots. That circle is 6.28 times 10, or 62.8 centimetres around, so the middle path was 31.4 centimetres long. Its two ends lay on the rim, one on each half-circle, so taping the half-circles together joined them. On the lemon, the middle path closes into a whole circle, still 31.4 centimetres around. Its radius is 31.4 divided by 6.28, which is 5 centimetres. Half the radius means a bend twice as sharp.

Nothing stretched, so every length along the shell stayed the same. That means the ant's rings at the lemon's middle come out exactly as they did on the half-ball. Her number there is 1 hundredth per square centimetre, as before. The outsider's number must agree with hers, because the two numbers agree at every smooth spot.

At the lemon's middle, the outsider's sharpest bend is now the middle path, with radius 5 centimetres. The gentlest is the path from tip to tip, which crosses the middle path at a right angle. Both of these bends go toward the shell's inside face, as every bend did on the half-ball. So the radius of the tip-to-tip bend times 5 must make 100, and 1 divided by the product is again 1 hundredth. That radius is therefore 20 centimetres, and the path from tip to tip bends more gently than before. A careful drawing of the lemon's outline confirms the 20 centimetres.

Bending without stretching traded one bend against the other, but it did not change the Gaussian curvature. The same reasoning works at every smooth spot of every smooth surface, because rings measured along a surface never change when nothing stretches. This fact is called the theorema egregium, Latin for remarkable theorem. Gauss proved it in 1827.

Why cut the ball first? A whole, closed ball cannot be bent into any other smooth shape without stretching. Press a dent into a ping-pong ball, and the plastic creases sharply around the dent.

Why remarkable? Each bend alone can be seen only from outside the surface, and bending can change each bend. Yet the number built from both bends is one an ant can measure without ever leaving the surface.

**Try it:** Roll a sheet of paper into a tube about 4 centimetres across, and tape the edge. Lay a pencil on the outside of the tube, alongside the taped edge. The pencil touches the paper along its whole length, because the path along the tube does not bend. Now squeeze the tube gently into an oval, pressing evenly along its whole length, without creasing it. The bend around the tube gets sharper in some places and gentler in others. Yet lay the pencil anywhere on the outside of the tube, pointing the same way as the taped edge, and it touches the paper along its whole length. The path along the tube stays unbent, so the Gaussian curvature stays zero, as the theorem says it must.

**Takeaway:** Bending a shell without stretching can make one bend sharper and the other gentler, but it never changes the Gaussian curvature at a smooth spot.

*Builds on:* [[gaussian-curvature]]<br>*Visuals:* [[half-ball-closes-into-a-lemon]]<br>*See:* `checks/squeeze-a-shell-from-a-ball`

### 2. No flat map is to scale everywhere · entry · operational

*Can a flat paper map show every distance in a region of Earth exactly to scale?*

**Recap:** The theorema egregium: bending a surface without stretching never changes its Gaussian curvature at any smooth spot. On a ball, the Gaussian curvature is 1 divided by the radius times itself, and on flat paper it is zero. Walking without ever steering left or right is called walking straight. The ring test: walk straight out the same distance from a centre in many directions, then measure the ring of end marks along the ground. On flat paper the ring is about 6.28 times the distance walked; on a ball it comes out shorter.

Surveyors, people who measure land for a living, measure distances along the ground between towns, rivers and hills. A mapmaker then draws those distances on flat paper at one scale, say 1 centimetre on the map for every 10 kilometres of ground. A map is called exactly to scale if every distance on it matches the ground in that same way. Can a flat map of an area of ground be exactly to scale everywhere?

Suppose it could. Ten kilometres is a million centimetres, so picture the map enlarged a million times. Every distance on the enlarged map would then equal the matching distance along the ground. The enlarged map would be a copy of the ground with every length kept, but lying flat. So the ground could be bent flat without stretching, into the shape of the enlarged map.

Gauss's theorem forbids this. Treat Earth as a smooth ball 6,371 kilometres in radius. 6,371 times 6,371 is about 40.6 million, so Earth's Gaussian curvature is 1 divided by 40.6 million, per square kilometre. Flat paper's Gaussian curvature is zero. Bending without stretching cannot turn the one number into the other. So no flat map of an area of a round Earth is exactly to scale everywhere, not even a map of one town.

How big is the error for one kind of map? Surveyors walk straight out 1,000 kilometres from a centre in many directions, and measure the ring of end marks along the ground. The ring comes out about 6,257 kilometres long. Suppose the map keeps every distance from the centre correct. Then it draws the end marks on a circle 1,000 kilometres from the centre, at the map scale. That circle is a little over 6.28 times 1,000 kilometres, which comes to about 6,283 kilometres around. So the ring on the map is about 26 kilometres too long, 0.4 per cent.

For a town, the error is tiny. A ring walked 10 kilometres from a town's centre comes out only about 2.6 centimetres shorter than a ring walked 10 kilometres from a centre on flat paper. Both rings are almost 63 kilometres around. So a map that keeps every distance from the centre correct draws that ring about 2.6 centimetres too long, out of almost 63 kilometres. Nobody could see that error on a town map.

For a whole continent, or the whole world, the errors are large. On many world maps, Greenland looks about as big as Africa. In fact, Africa has about 14 times Greenland's area.

**Takeaway:** A flat map exactly to scale everywhere would be the ground bent flat without stretching, which the theorem forbids on a round Earth. The error is tiny for a town and large for a continent.

*Continues:* `ways_in/a-shell-closes-into-a-lemon`<br>*Builds on:* [[intrinsic-geometry]]<br>*Visuals:* [[paced-ring-on-a-ball-and-a-plain]]<br>*See:* `checks/perfect-town-map`

### 3. Two routes to one number on a surface of revolution · working · calculation

*How do the bends and the line element give the same Gaussian curvature on a surface of revolution, and what does the line element leave free?*

The lemon of "A half-ball closes into a lemon" is a surface of revolution, and for every such surface both routes to $K$ can be written down. The outsider's sharpest and gentlest bends, signed relative to a unit normal, are the principal curvatures, and the ant's rings are coded in the line element. Let $\rho$ be arc length along a profile, $r(\rho)$ the distance from the axis, $z(\rho)$ the height, with $r'^2 + z'^2 = 1$, and $\phi$ the angle around the axis. The line element is $ds^2 = d\rho^2 + r^2\,d\phi^2$, so the spacing formula $K = -\partial_\rho^2 f/f$ for $ds^2 = d\rho^2 + f^2\,d\phi^2$, with $f = r$, gives the insider's value $K = -r''/r$.

The outsider places the surface at $\mathbf X = (r\cos\phi, r\sin\phi, z)$ with unit normal $\hat{\mathbf n} = (-z'\cos\phi, -z'\sin\phi, r')$. The profile and the circles are principal directions, with principal curvatures, counted positive when the surface bends toward $\hat{\mathbf n}$,

$$\kappa_{\rm m} = r'z'' - z'r'', \qquad \kappa_{\rm p} = \frac{z'}{r}.$$

Differentiating $r'^2 + z'^2 = 1$ turns $z'\kappa_{\rm m}$ into $-r''$, so $\kappa_{\rm m}\kappa_{\rm p} = -r''/r$: the two routes agree at every point, as the derivation "The product of the bends is the spacing formula" shows move by move.

Now fix the line element and vary the shape. The lemons $r = b\sin(\rho/a)$ with $0 < b \le a$ all have $r'' = -r/a^2$, so $K = 1/a^2$: each is locally isometric to a sphere of radius $a$, matching $\phi_{\rm sphere} = (b/a)\phi$. At the middle, $\rho = \pi a/2$, $r' = 0$ and $z' = 1$, so $\kappa_{\rm p} = 1/b$ and $\kappa_{\rm m} = b/a^2$. The half-ball has $b = a/2$: radii 5 cm and 20 cm for $a = 10$ cm. The line element fixes the product, not the factors.

Two what-ifs mark the family's limits. Near a tip $r \approx (b/a)\rho$, so small rings measure $2\pi(b/a)\rho$: a cone point unless $b = a$. For $b > a$, $|r'| \le 1$ holds only where $|\cos(\rho/a)| \le a/b$, so the surface exists only as a band around the middle, a barrel with no tips.

**Takeaway:** On a surface of revolution the principal curvatures multiply to minus r double-prime over r, the line element's Gaussian curvature; the lemons share a sphere's line element but not its principal curvatures.

*Continues:* `ways_in/a-shell-closes-into-a-lemon`<br>*Builds on:* [[gaussian-curvature]], [[intrinsic-versus-extrinsic-curvature]]<br>*Visuals:* [[half-ball-closes-into-a-lemon]]<br>*See:* `derivations/product-equals-spacing-formula`, `problems/lemon-from-a-third-of-a-ball`

### 4. Rulers around a star read the funnel · working · operational

*When a slice of space around a star is drawn as a funnel, which feature of the drawing do rulers in that space confirm?*

The two routes of "Two routes to one number on a surface of revolution" also read a real curved space. Take a static, spherical, non-rotating body of mass $M$ and the plane through its centre at one moment. Observers at rest relative to the body lay rulers in that plane, and label each ring by $r$, its measured circumference divided by $2\pi$. Outside the body, general relativity gives the distance rule, taken on trust here,

$$d\ell^2 = \frac{dr^2}{1 - r_s/r} + r^2\,d\phi^2, \qquad r_s = \frac{2GM}{c^2}.$$

*Insiders.* With ruler distance $\rho$ outward, $r' = \sqrt{1 - r_s/r}$ and $r'' = r_s/2r^2$, so the spacing formula gives $K = -r_s/2r^3 = -GM/c^2r^3$. It is negative: the plane curves like a saddle.

*The drawing.* A surface of revolution in flat three-dimensional space with the same $r(\rho)$ needs $z' = \sqrt{1 - r'^2} = \sqrt{r_s/r}$, which gives the funnel $z = 2\sqrt{r_s(r - r_s)}$. The formulas of "Two routes to one number on a surface of revolution" then give $\kappa_{\rm p} = z'/r = \sqrt{r_s/r^3}$ and $\kappa_{\rm m} = -r''/z' = -\tfrac12\sqrt{r_s/r^3}$, toward opposite faces. Their product is $-r_s/2r^3$, the value the rulers give.

So the theorema egregium says exactly what an embedding diagram can be trusted for. Lengths along the funnel stand for ruler readings, and the Gaussian curvature read from its bends is the curvature those rulers measure. The funnel's height stands for no direction in space. The worked example "The funnel over the Sun" puts numbers on the Sun and Earth, and radio tracking of the Cassini spacecraft has tested the coefficient behind them.

**Takeaway:** Rulers in the plane through a star fix the Gaussian curvature outside the star, minus G M over c squared r cubed. The funnel drawn for the plane has bends whose product matches the curvature. The funnel's height stands for nothing in space.

*Continues:* `ways_in/two-routes-on-a-surface-of-revolution`<br>*Builds on:* [[gaussian-curvature]]<br>*Visuals:* [[funnel-drawn-over-a-star]]<br>*See:* `worked_examples/funnel-over-the-sun`, `observations/cassini-fixes-the-slice-curvature`, `checks/funnel-wall-at-the-horizon`

### 5. Why the product is intrinsic, and where the theorem stops · formal · structure

*What exactly does the theorem assert, how is it proved, and where does it stop holding?*

The identity $\kappa_{\rm m}\kappa_{\rm p} = -r''/r$ of "Two routes to one number on a surface of revolution" used rotational symmetry; the general statement needs none. Let $(M, g)$ be a two-dimensional Riemannian manifold and $f: M \to \mathbb R^3$ an isometric immersion of class $C^3$, $f^*\delta = g$. In a chart with a unit normal $\hat{\mathbf n}$, the Gauss formula defines $\Gamma$ and the second fundamental form $h$:

$$\partial_\mu\partial_\nu f = \Gamma^\lambda{}_{\mu\nu}\,\partial_\lambda f + h_{\mu\nu}\,\hat{\mathbf n}.$$

The shape operator $S^\lambda{}_\mu = g^{\lambda\nu}h_{\nu\mu}$ obeys $\partial_\mu\hat{\mathbf n} = -S^\lambda{}_\mu\,\partial_\lambda f$; its eigenvalues are the principal curvatures, and $\det S = \det h/\det g$ is unchanged when $\hat{\mathbf n}$ is reversed.

*Theorem.* With $R$ the course Riemann tensor of the Levi-Civita connection of $g$, $R_{1212} = \det h$ in every chart. Hence $\det S = R_{1212}/\det g = K$, the sectional curvature of $g$, built from $g_{\mu\nu}$ and its first two derivatives. If $\varphi: M \to M'$ is a local isometry between surfaces immersed in $\mathbb R^3$, then $K'\circ\varphi = K$.

*Proof sketch.* Dotting the Gauss formula with $\partial_\sigma f$ and differentiating $g_{\nu\sigma} = \partial_\nu f\cdot\partial_\sigma f$ identifies $\Gamma$ as the Christoffel symbols of $g$. Differentiate the Gauss formula along $x^\rho$, use the formula for $\partial_\rho\hat{\mathbf n}$, and antisymmetrize in $\rho\mu$, since third partial derivatives of $f$ commute. The tangential part is the Gauss equation $R_{\sigma\nu\rho\mu} = h_{\rho\sigma}h_{\mu\nu} - h_{\mu\sigma}h_{\rho\nu}$; the normal part is the Codazzi equation $\nabla_\rho h_{\mu\nu} = \nabla_\mu h_{\rho\nu}$. The derivation "The Gauss equation from commuting derivatives" gives each move.

*Limits.*

- The converse fails twice. The metric does not fix the immersion: the lemons are locally isometric to a sphere with different principal curvatures. And equal $K$ at corresponding points does not make two surfaces isometric when $K$ varies.
- A curved ambient space adds a term: for a surface in a Riemannian three-manifold, $K = \bar K(T_pM) + \det S$. In $\mathbb R^{2+k}$, $K = \sum_a \det S_a$ over an orthonormal frame of normals.
- For a hypersurface of $\mathbb R^{n+1}$, each principal plane has sectional curvature $\kappa_i\kappa_j$. Where $S$ has rank at least 3 on an open set, $g$ fixes $S$ there up to sign (Beez–Killing), so a nontrivial bending needs rank at most 2, which every surface has.
- Bending can be blocked globally. By Liebmann's theorem a compact connected $C^2$ surface in $\mathbb R^3$ with constant $K$ is a round sphere, so a whole sphere cannot be bent into any other $C^2$ closed surface. Smoothness matters: Nash–Kuiper $C^1$ isometric embeddings crumple a sphere into an arbitrarily small ball.
- Riemann's extension defines curvature from $g$ alone in every dimension, which is why spacetime needs no surrounding space.

**Takeaway:** For a surface in Euclidean space the Gauss equation makes the determinant of the shape operator equal the sectional curvature of the metric; the metric fixes that product but need not fix the bends, and a curved ambient space adds a term.

*Continues:* `ways_in/two-routes-on-a-surface-of-revolution`<br>*Builds on:* [[riemann-curvature-tensor]], [[intrinsic-versus-extrinsic-curvature]]<br>*See:* `derivations/gauss-equation-from-commuting-derivatives`, `checks/flat-torus-in-the-three-sphere`, `checks/hypersurface-in-four-dimensions`, `problems/curvature-from-an-orthogonal-metric`

## Glossary

| Term | Say | In plain words | Concept |
| --- | --- | --- | --- |
| theorema egregium | thee-oh-RAY-muh eh-GRAY-gee-um | Gauss's remarkable theorem: bending a surface without stretching never changes its Gaussian curvature at a smooth spot, since lengths along the surface fix that number. | [[theorema-egregium]] |
| Gaussian curvature | GOW-see-un | A number for each spot of a smooth surface. From outside, multiply the radii of the spot's sharpest and gentlest bends and divide 1 by the result. On a saddle, use the sharpest bend toward each face and add a minus sign. An ant gets the same number from small rings. | [[gaussian-curvature]] |
| best-fit circle | — | At a place where a path or line bends, the circle that matches the bend best. The smaller the circle, the sharper the bend. | [[curvature-of-a-curve]] |
| walk straight | — | To walk without ever steering left or right, even where the path bends over a curved surface. | [[geodesic]] |
| ring test | — | Walk straight out the same distance from a centre in many directions, and measure the ring of end marks along the ground. On flat paper the ring is about 6.28 times that distance. | [[circumference-to-radius-test]] |
| face | — | One of the two sides of a sheet or a shell, such as the inside and the outside of an eggshell. | — |
| smooth spot | — | A spot on a surface with no crease, sharp tip or corner. | — |
| exactly to scale | — | Said of a map on which every distance matches the distance along the ground, shrunk by the same amount everywhere. | — |

## Key equations

### Bends and line element agree on a surface of revolution · working

$$
\kappa_{\rm m}\,\kappa_{\rm p} = \big(r'z'' - z'r''\big)\,\frac{z'}{r} = -\frac{r''}{r} = K
$$

The principal curvatures of a surface of revolution multiply to the Gaussian curvature its line element gives.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $\kappa_{\rm m},\ \kappa_{\rm p}$ | principal curvatures along the profile and around the axis | kappa m and kappa p |
| $r,\ z$ | distance from the axis and height; primes are derivatives along the profile | r and z |
| $K$ | Gaussian curvature | K |

**Holds when:** Profile parametrized by arc length, $r > 0$; either unit normal; exact.  
**Say it:** “Kappa m times kappa p is minus r double prime over r, which is K.”  
**Justified by:** `derivations/product-equals-spacing-formula`

### Gauss equation for a surface in Euclidean space · formal

$$
R_{\sigma\nu\rho\mu} = h_{\rho\sigma}h_{\mu\nu} - h_{\mu\sigma}h_{\rho\nu}, \qquad K = \frac{R_{1212}}{\det g} = \frac{\det h}{\det g} = \det S
$$

The metric's Riemann tensor is built from the second fundamental form, so the determinant of the shape operator is intrinsic.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $R_{\sigma\nu\rho\mu}$ | course Riemann tensor of $g$, first index lowered | R sigma nu rho mu |
| $h_{\mu\nu}$ | second fundamental form | h mu nu |
| $S$ | shape operator | S |

**Holds when:** Surface immersed isometrically in $\mathbb R^3$, class $C^3$; any chart; either unit normal.  
**Say it:** “R sigma nu rho mu is h rho sigma h mu nu minus h mu sigma h rho nu, so K is det h over det g.”  
**Justified by:** `derivations/gauss-equation-from-commuting-derivatives`

## Derivations

### The product of the bends is the spacing formula · working

**Goal:** Show that the principal curvatures of a surface of revolution multiply to $-r''/r$.

1. Place the surface at $\mathbf X = (r\cos\phi, r\sin\phi, z)$ with $r'^2 + z'^2 = 1$. Then $\mathbf X_\rho = (r'\cos\phi, r'\sin\phi, z')$ and $\mathbf X_\phi = (-r\sin\phi, r\cos\phi, 0)$ are orthogonal, with lengths $1$ and $r$, so $ds^2 = d\rho^2 + r^2d\phi^2$.
2. The unit normal is $\hat{\mathbf n} = \mathbf X_\rho\times\mathbf X_\phi/r = (-z'\cos\phi, -z'\sin\phi, r')$.
3. Dot the second derivatives with $\hat{\mathbf n}$: $\mathbf X_{\rho\rho}\cdot\hat{\mathbf n} = r'z'' - z'r''$, $\mathbf X_{\phi\phi}\cdot\hat{\mathbf n} = rz'$ and $\mathbf X_{\rho\phi}\cdot\hat{\mathbf n} = 0$.
4. The mixed term vanishes and the line element is diagonal, so $\partial_\rho$ and $\partial_\phi$ are principal, with $\kappa_{\rm m} = r'z'' - z'r''$ and $\kappa_{\rm p} = rz'/r^2 = z'/r$.
5. Differentiate $r'^2 + z'^2 = 1$: $r'r'' + z'z'' = 0$.
6. Multiply $\kappa_{\rm m}$ by $z'$ and use that result: $z'\kappa_{\rm m} = r'(z'z'') - z'^2r'' = -r'^2r'' - z'^2r'' = -r''$.
7. So $\kappa_{\rm m}\kappa_{\rm p} = z'\kappa_{\rm m}/r = -r''/r$, the spacing formula $K = -\partial_\rho^2 f/f$ with $f = r$.

**Result:** $\kappa_{\rm m}\kappa_{\rm p} = -r''/r = K$ wherever $r > 0$, for either unit normal.

### The Gauss equation from commuting derivatives · formal

**Goal:** For a surface $f: M \to \mathbb R^3$, show $R_{\sigma\nu\rho\mu} = h_{\rho\sigma}h_{\mu\nu} - h_{\mu\sigma}h_{\rho\nu}$ with the course Riemann tensor, so that $R_{1212} = \det h$.

1. Write $e_\mu = \partial_\mu f$, so $g_{\mu\nu} = e_\mu\cdot e_\nu$, and split $\partial_\mu e_\nu = \Gamma^\lambda{}_{\mu\nu}e_\lambda + h_{\mu\nu}\hat{\mathbf n}$; both $\Gamma^\lambda{}_{\mu\nu}$ and $h_{\mu\nu}$ are symmetric in $\mu\nu$.
2. Dot with $e_\sigma$: $\partial_\mu e_\nu\cdot e_\sigma = \Gamma_{\sigma\mu\nu} \equiv g_{\sigma\lambda}\Gamma^\lambda{}_{\mu\nu}$. Then $\partial_\mu g_{\sigma\nu} = \Gamma_{\nu\mu\sigma} + \Gamma_{\sigma\mu\nu}$, and $\tfrac12(\partial_\mu g_{\sigma\nu} + \partial_\nu g_{\sigma\mu} - \partial_\sigma g_{\mu\nu}) = \Gamma_{\sigma\mu\nu}$: these are the Christoffel symbols of $g$.
3. From $\hat{\mathbf n}\cdot\hat{\mathbf n} = 1$, $\partial_\rho\hat{\mathbf n}$ is tangent; from $\hat{\mathbf n}\cdot e_\nu = 0$, $\partial_\rho\hat{\mathbf n}\cdot e_\nu = -h_{\rho\nu}$. So $\partial_\rho\hat{\mathbf n} = -h_\rho{}^\lambda e_\lambda$ with $h_\rho{}^\lambda = g^{\lambda\nu}h_{\rho\nu}$.
4. Differentiate the split along $x^\rho$ and keep the component along $e_\sigma$: $\partial_\rho\Gamma^\sigma{}_{\mu\nu} + \Gamma^\sigma{}_{\rho\lambda}\Gamma^\lambda{}_{\mu\nu} - h_{\mu\nu}h_\rho{}^\sigma$.
5. Third partial derivatives of $f$ commute, so this component is symmetric in $\rho\mu$. Subtracting its $\rho\leftrightarrow\mu$ swap gives $\partial_\rho\Gamma^\sigma{}_{\mu\nu} - \partial_\mu\Gamma^\sigma{}_{\rho\nu} + \Gamma^\sigma{}_{\rho\lambda}\Gamma^\lambda{}_{\mu\nu} - \Gamma^\sigma{}_{\mu\lambda}\Gamma^\lambda{}_{\rho\nu} = h_{\mu\nu}h_\rho{}^\sigma - h_{\rho\nu}h_\mu{}^\sigma$.
6. The left side is the course $R^\sigma{}_{\nu\rho\mu}$. Lowering $\sigma$ gives $R_{\sigma\nu\rho\mu} = h_{\rho\sigma}h_{\mu\nu} - h_{\mu\sigma}h_{\rho\nu}$.
7. Set $(\sigma,\nu,\rho,\mu) = (1,2,1,2)$: $R_{1212} = h_{11}h_{22} - h_{12}^2 = \det h$. Check on the unit sphere with the outward normal: $h = -g$, so $R_{1212} = \det g$ and $K = +1$, as the course conventions require.

**Result:** $R_{\sigma\nu\rho\mu} = h_{\rho\sigma}h_{\mu\nu} - h_{\mu\sigma}h_{\rho\nu}$, so $K = R_{1212}/\det g = \det h/\det g$.

## Worked examples

### The funnel over the Sun · working

**Problem:** Find the Gaussian curvature of the plane through the Sun's centre, just outside its surface, and the bends of its funnel. Compare Earth. Use $GM_\odot = 1.327\times10^{20}$ m$^3$ s$^{-2}$, $R_\odot = 6.957\times10^8$ m, $GM_\oplus = 3.986\times10^{14}$ m$^3$ s$^{-2}$, $R_\oplus = 6.371\times10^6$ m.

1. $r_s = 2GM_\odot/c^2 = 2953$ m.
2. $K = -r_s/2R_\odot^3 = -2953/(2\times3.367\times10^{26})$ m$^{-2}$ $= -4.38\times10^{-24}$ m$^{-2}$, so $|K|^{-1/2} = 4.78\times10^{11}$ m, or $3.19$ au with 1 au $= 1.496\times10^{11}$ m.
3. On the funnel, $\kappa_{\rm p} = \sqrt{r_s/R_\odot^3}$ has radius $2.26$ au, and $\kappa_{\rm m} = -\tfrac12\kappa_{\rm p}$ has radius $4.51$ au, toward the opposite face. Then $2.26\times4.51 = 10.2 = 3.19^2$.
4. For Earth, $r_s = 8.87$ mm and $K = -1.72\times10^{-23}$ m$^{-2}$, a radius of $1.61$ au: $K = -GM/c^2R^3$ follows the mean density, and Earth is 3.9 times denser than the Sun.

**Answer:** Sun: $K = -4.4\times10^{-24}$ m$^{-2}$, radius 3.2 au, funnel bends of radii 2.3 au and 4.5 au. Earth: $K = -1.7\times10^{-23}$ m$^{-2}$, radius 1.6 au.

**Takeaway:** Space at a body's surface curves in proportion to its mean density, and the funnel's bends reproduce that curvature.

## Problems

### `lemon-from-a-third-of-a-ball` · working · difficulty 2 · calculation

A third of a thin spherical shell of radius 9 cm, cut between two half-circles from pole to pole that meet at 120 degrees, is closed up without stretching into a lemon. (a) Show that its Gaussian curvature equals the sphere's. (b) Find both principal curvatures at the lemon's middle. (c) Does the line element fix each principal curvature?

**Hints**

1. Every circle around the axis keeps a third of its length.
2. At the middle $r' = 0$; use $z'\kappa_{\rm m} = -r''$.

**Answer:** (a) $K = 1/81$ cm$^{-2}$. (b) $1/3$ and $1/27$ cm$^{-1}$, radii 3 cm and 27 cm. (c) No: only their product is fixed.

**Must contain:** K is one over eighty-one per square centimetre, as for the sphere; The bend radii at the middle are 3 and 27 centimetres, and only their product is fixed

**Numeric:** radius of the bend along the lemon at its middle = 27 cm (magnitude, ±2%)

**Solution**

1. Every circle around the axis keeps a third of its length, so the lemon is $r = b\sin(\rho/a)$ with $a = 9$ cm and $b = 3$ cm.
2. $r'' = -(b/a^2)\sin(\rho/a) = -r/a^2$, so $K = -r''/r = 1/a^2 = 1/81$ cm$^{-2}$, whatever $b$ is.
3. At the middle, $\rho = \pi a/2$, $r' = 0$ and $z' = 1$, so $\kappa_{\rm p} = z'/r = 1/3$ cm$^{-1}$ and $\kappa_{\rm m} = -r''/z' = b/a^2 = 1/27$ cm$^{-1}$.
4. Through $\phi_{\rm sphere} = (b/a)\phi$ the lemon is locally isometric to the sphere, whose bends at the corresponding point both have radius 9 cm. So the line element fixes $\kappa_{\rm m}\kappa_{\rm p}$ but not each factor.

**Targets:** `each-bend-is-intrinsic`

### `curvature-from-an-orthogonal-metric` · formal · difficulty 3 · derivation

(a) For $ds^2 = E\,du^2 + G\,dv^2$ with $E, G > 0$, show from the course Riemann tensor that $K = R_{uvuv}/EG = -\frac{1}{2\sqrt{EG}}\big[\partial_u(\partial_uG/\sqrt{EG}) + \partial_v(\partial_vE/\sqrt{EG})\big]$. (b) Mercator's chart of a sphere of radius $a$ has $ds^2 = \mathrm{sech}^2(v/a)\,(du^2 + dv^2)$, with $u = a\phi$ and $\sin\lambda = \tanh(v/a)$ at latitude $\lambda$. Find $K$ and compare it with the product of the principal curvatures. (c) Show that no chart of any region of the sphere has constant $E$ and $G$, and find by what factor the Mercator chart enlarges lengths at latitude $60^\circ$.

**Hints**

1. Only six Christoffel symbols can be nonzero; write each in terms of $E$, $G$ and one first derivative.
2. For (b), $\partial_vE/E = -(2/a)\tanh(v/a)$.

**Answer:** (a) $R_{uvuv} = -\tfrac12(E_{vv} + G_{uu}) + (E_v^2 + E_uG_u)/4E + (G_u^2 + E_vG_v)/4G$, which divided by $EG$ is the stated form. (b) $K = 1/a^2 = \kappa_1\kappa_2$. (c) Constant $E$ and $G$ give $K = 0 \neq 1/a^2$; Mercator enlarges lengths by $\sec\lambda$, a factor of 2 at $60^\circ$.

**Must contain:** K depends only on E, G and their first two derivatives; Mercator gives one over a squared, the product of the principal curvatures; No chart of a sphere has a constant scale; Mercator doubles lengths at sixty degrees

**Numeric:** Mercator enlargement of lengths at latitude 60 degrees = 2 1 (magnitude, ±1%)

**Solution**

1. Subscripts on $E$ and $G$ denote partial derivatives. The nonzero Christoffel symbols are $\Gamma^u{}_{uu} = E_u/2E$, $\Gamma^u{}_{uv} = E_v/2E$, $\Gamma^u{}_{vv} = -G_u/2E$, $\Gamma^v{}_{uu} = -E_v/2G$, $\Gamma^v{}_{uv} = G_u/2G$ and $\Gamma^v{}_{vv} = G_v/2G$.
2. The course definition gives $R^u{}_{vuv} = \partial_u\Gamma^u{}_{vv} - \partial_v\Gamma^u{}_{uv} + \Gamma^u{}_{u\lambda}\Gamma^\lambda{}_{vv} - \Gamma^u{}_{v\lambda}\Gamma^\lambda{}_{uv}$, and $R_{uvuv} = E\,R^u{}_{vuv}$.
3. Substituting and collecting terms: $R_{uvuv} = -\tfrac12(E_{vv} + G_{uu}) + (E_v^2 + E_uG_u)/4E + (G_u^2 + E_vG_v)/4G$.
4. Expanding $\partial_u(G_u/\sqrt{EG})$ and $\partial_v(E_v/\sqrt{EG})$ and multiplying by $-\sqrt{EG}/2$ returns the same expression, so $K = R_{uvuv}/EG$ has the stated form: only $E$, $G$ and their first two derivatives enter.
5. Mercator: $E = G = \mathrm{sech}^2(v/a)$, so $G_u = 0$ and $K = -\frac{1}{2E}\partial_v(E_v/E) = -\frac{1}{2E}\cdot\big(-\tfrac{2}{a^2}\mathrm{sech}^2(v/a)\big) = 1/a^2$. A sphere of radius $a$ has $\kappa_1 = \kappa_2 = \pm1/a$, product $1/a^2$.
6. Constant $E$ and $G$ make every derivative vanish, so $K = 0$, which contradicts $K = 1/a^2$ on any region of the sphere.
7. Ground length is $\mathrm{sech}(v/a) = \cos\lambda$ times chart length, so the chart enlarges lengths by $\sec\lambda$: at $60^\circ$, by $2$.

## Observations

- **Radio tracking of the Cassini spacecraft as its signals passed close to the Sun in 2002** (measured, working). To first order, the plane through the Sun's centre has $K = -\gamma\,GM_\odot/c^2r^3$, where the post-Newtonian parameter $\gamma$ sets how strongly mass curves space; general relativity has $\gamma = 1$. The radio signals fixed $\gamma$, and so this curvature, from inside the Solar System. *Numbers:* $\gamma - 1 = (2.1 \pm 2.3)\times10^{-5}$. *Reference:* B. Bertotti, L. Iess, P. Tortora (2003), *A test of general relativity using radio links with the Cassini spacecraft*, Nature 425, 374–376, doi:10.1038/nature01997

## Teaching arc

1. **Predict the lemon** (entry). Close the half-ball into a lemon after a prediction, then run the shell check. *Why:* Watching one bend sharpen while the other softens shows what survives the bending. *Predict:* When the half-ball closes into a lemon, does the path from tip to tip bend more sharply or more gently than before? *Visual:* [[half-ball-closes-into-a-lemon]] *Uses:* `ways_in/a-shell-closes-into-a-lemon`, `checks/squeeze-a-shell-from-a-ball`
2. **Ask for a perfect map** (entry). Ask whether a town map can be exactly to scale, then compare a town with a continent. *Why:* It ties the theorem to maps everyone has used. *Predict:* Could a map of your town be exactly to scale everywhere? *Visual:* [[paced-ring-on-a-ball-and-a-plain]] *Uses:* `ways_in/no-flat-map-is-to-scale`, `checks/perfect-town-map`
3. **Compute both routes, then read a funnel** (working). Derive the product formula, then read the funnel drawn for a black hole. *Why:* It shows which parts of an embedding diagram are physics. *Predict:* Where the funnel turns vertical, is space infinitely curved? *Visual:* [[funnel-drawn-over-a-star]] *Uses:* `derivations/product-equals-spacing-formula`, `ways_in/rulers-around-a-star-read-the-funnel`, `checks/funnel-wall-at-the-horizon`

## Misconceptions

### “If I bend a shell more sharply one way, its Gaussian curvature goes up.” · entry · `bending-changes-the-number`

- **Why it is tempting:** A sharper bend looks like more curving.
- **What is true:** Without stretching, the Gaussian curvature stays the same. On a shell cut from a ball, one bend getting sharper makes the other gentler by the same factor.
- **Exposed by:** `checks/squeeze-a-shell-from-a-ball`

### “A map of a small place, like a town, can be exactly to scale everywhere.” · entry · `small-maps-can-be-perfect`

- **Why it is tempting:** Town maps match the streets as well as anyone can measure.
- **What is true:** Such a map would be the ground bent flat without stretching, which cannot change its Gaussian curvature. For a town a few kilometres across, the error is real but only millimetres.
- **Exposed by:** `checks/perfect-town-map`

### “If the line element fixes the product of the principal curvatures, it fixes each one too.” · working · `each-bend-is-intrinsic`

- **Why it is tempting:** For a sphere the line element seems to fix the whole shape.
- **What is true:** The lemons share a sphere's line element locally but not its principal curvatures.
- **Exposed by:** `checks/hypersurface-in-four-dimensions`

### “Where the funnel drawn for a black hole turns vertical, space is infinitely curved.” · working · `vertical-funnel-means-infinite-curvature`

- **Why it is tempting:** A vertical wall looks like the most extreme bend in the drawing.
- **What is true:** The steepness belongs to the drawing; the product of the bends, which rulers fix, stays finite there.
- **Exposed by:** `checks/funnel-wall-at-the-horizon`

### “A surface's Gaussian curvature is the product of its principal curvatures in any surrounding space.” · formal · `product-rule-in-any-space`

- **Why it is tempting:** In ordinary space the theorem makes the two equal everywhere.
- **What is true:** A curved surrounding space adds its own sectional curvature to the Gauss equation.
- **Exposed by:** `checks/flat-torus-in-the-three-sphere`

## Checks

1. **Entry · numeric** `checks/squeeze-a-shell-from-a-ball`. A thin shell cut from a ball of radius 12 centimetres bends easily, but it never stretches or creases. At one smooth spot, you bend the shell until the sharpest bend there has a best-fit circle of radius 8 centimetres. Both bends there still go toward the face that was on the inside of the ball. What is the radius of the gentlest bend at that spot? A friend says the Gaussian curvature there has gone up. Is the friend correct?
   - **Hints:** What did the two radii multiply to before the bending?
   - **Answer:** The gentlest bend has a radius of 18 centimetres, and the friend is wrong. Before bending, the sharpest and the gentlest bend at the spot each had a radius of 12 centimetres. 12 times 12 is 144, so the Gaussian curvature was 1 divided by 144, per square centimetre. Nothing stretched, so the theorem says the Gaussian curvature is still 1 divided by 144. Both bends go toward the same face, so 1 divided by the product of their radii must be 1 divided by 144. That means the radii must multiply to 144 again. 144 divided by 8 is 18. The sharper bend is paid for by a gentler one.
   - **Must contain:** The gentlest bend has a radius of 18 centimetres; The Gaussian curvature stays 1 divided by 144 per square centimetre
   - **Numeric:** radius of the gentlest bend = 18 cm (magnitude, ±3%)
   - **Targets:** `bending-changes-the-number`
   - **Visual:** [[half-ball-closes-into-a-lemon]]
2. **Entry · evaluate-claim** `checks/perfect-town-map`. Treat Earth as a smooth ball. A town covers a round area 5 kilometres in radius. Its mapmaker says the town is too small for Earth's curving to matter, so her flat map is exactly to scale everywhere. Compare two rings, each walked 5 kilometres from a centre: one on flat paper, one on a smooth ball the size of Earth. The ring on the ball comes out about 3 millimetres shorter. Can a flat map of the town be exactly to scale everywhere, and would anyone notice the difference?
   - **Hints:** What would a perfect map be, enlarged to the town's size?
   - **Answer:** No flat map of the town can be exactly to scale everywhere, but nobody could notice the error. Suppose such a map existed, and enlarge it until 1 centimetre on the map stands for 1 centimetre of ground. It would then be the town's ground, bent flat without stretching. Bending without stretching never changes the Gaussian curvature. The ground's Gaussian curvature is 1 divided by about 40.6 million, per square kilometre, and flat paper's is zero. So such a map cannot exist. The ring gives the size of the error. A map that keeps every distance from the centre correct draws that ring about 3 millimetres too long, out of more than 31 kilometres.
   - **Must contain:** No flat map of an area of a round Earth is exactly to scale everywhere, however small the area; For this town the error is only about 3 millimetres
   - **Targets:** `small-maps-can-be-perfect`
   - **Visual:** [[paced-ring-on-a-ball-and-a-plain]]
3. **Working · evaluate-claim** `checks/funnel-wall-at-the-horizon`. For the plane through a non-rotating black hole of 10 solar masses at one moment, the funnel drawing turns vertical at the horizon. A poster says space is infinitely curved there. Evaluate the claim, and find the plane's radius of curvature at the horizon: one over the square root of the size of its Gaussian curvature.
   - **Hints:** Which feature of the funnel does the theorem tie to the rulers?
   - **Answer:** The claim is wrong. The funnel $z = 2\sqrt{r_s(r - r_s)}$ has slope $dz/dr = \sqrt{r_s/(r - r_s)}$, which diverges at $r = r_s$; that steepness belongs to how the drawing sits in its invented height direction. The theorem ties the product of the bends to $K = -r_s/2r^3$, which rulers in the plane fix; at $r = r_s$ it is $-1/2r_s^2$, finite, and so are the bends $\kappa_{\rm p} = 1/r_s$ and $\kappa_{\rm m} = -1/2r_s$. For $10M_\odot$, $r_s = 29.5$ km and $|K|^{-1/2} = \sqrt2\,r_s = 41.8$ km.
   - **Must contain:** The steepness is not a curvature; K is minus one over two r s squared, finite; The radius of curvature is about 42 kilometres
   - **Numeric:** radius of curvature of the plane at the horizon = 41.8 km (magnitude, ±2%)
   - **Targets:** `vertical-funnel-means-infinite-curvature`
   - **Visual:** [[funnel-drawn-over-a-star]]
4. **Formal · explain** `checks/flat-torus-in-the-three-sphere`. The Clifford torus, the product of two circles of radius one over the square root of 2, lies in the unit three-sphere in four-dimensional Euclidean space, and its induced metric is flat. Within the three-sphere its principal curvatures are plus 1 and minus 1. A student concludes that its Gaussian curvature, their product, is minus 1. Resolve the contradiction.
   - **Hints:** What does the Gauss equation add when the ambient space is curved?
   - **Answer:** The student used the Euclidean form of the theorem in a curved ambient space. For a surface in a Riemannian three-manifold the Gauss equation reads $K = \bar K(T_pM) + \det S$. Every plane in the unit $S^3$ has sectional curvature $+1$, so $K = 1 + (-1) = 0$, as the flat metric requires. In $\mathbb R^4$ the torus has two unit normals: the position vector gives $\det S = +1$ and the normal within $S^3$ gives $\det S = -1$, and $K = \sum_a\det S_a = 0$ again.
   - **Must contain:** A curved ambient space adds its sectional curvature, plus one here, to the Gauss equation; In four-dimensional Euclidean space the determinants over the two normals add to zero
   - **Numeric:** Gaussian curvature of the Clifford torus = 0 1 (signed, ±0.01)
   - **Targets:** `product-rule-in-any-space`
5. **Formal · numeric** `checks/hypersurface-in-four-dimensions`. A three-dimensional hypersurface in four-dimensional Euclidean space has principal curvatures 2, 3 and 6 per metre at a point. (a) Find the sectional curvatures of the three principal planes. (b) Show that these intrinsic numbers fix the principal curvatures up to one overall sign. (c) Why does the same argument fail for a surface in three-dimensional Euclidean space?
   - **Hints:** Multiply two of the sectional curvatures and divide by the third.
   - **Answer:** (a) In flat ambient space the Gauss equation gives $K_{ij} = \kappa_i\kappa_j$: $6$, $12$ and $18$ m$^{-2}$. (b) $\kappa_1^2 = K_{12}K_{13}/K_{23} = 4$ m$^{-2}$, and likewise $\kappa_2^2 = 9$ and $\kappa_3^2 = 36$ m$^{-2}$. Every $K_{ij}$ is positive, so the signs agree: $\pm(2, 3, 6)$ m$^{-1}$. The three values differ, so the curvature operator of $g$ also picks out the principal planes. (c) A surface has one sectional curvature, $\kappa_1\kappa_2$, for two unknowns, so one parameter stays free, the one the lemons use.
   - **Must contain:** The sectional curvatures are 6, 12 and 18 per square metre; Each principal curvature squared is a product of two of them divided by the third; a surface has only one
   - **Numeric:** sectional curvature of the plane of the two largest principal curvatures = 18 m^-2 (signed, ±1%)
   - **Targets:** `each-bend-is-intrinsic`

## Visuals

- ★ [[half-ball-closes-into-a-lemon]] (flagship): One bend sharpens, the other softens, the curvature stays. *Sketch:* A slider sets how much of a thin ball is kept, and the kept shell closes into a lemon. At a draggable spot, readouts give both bend radii and their unchanging product.
- [[paced-ring-on-a-ball-and-a-plain]] (supporting): The ring count behind map errors. *Sketch:* This concept adds a map panel: the ring drawn on paper with distances from the centre kept, beside its true length, for a town, a country and a continent.
- [[funnel-drawn-over-a-star]] (core): Separates the drawing from what rulers fix. *Sketch:* A plane through a star or black hole beside its funnel. Sliders set mass and radius; readouts give the rulers' curvature, both bends and the slope, which alone diverges at a horizon.

## Tutor moves

**Open with**

- Picture half of a thin plastic ball, shaped like a bowl, that bends but never stretches. Pinch its rim at two opposite points, and squeeze the rim's two halves together until they meet, closing it into a lemon. Around its middle, the lemon bends more sharply than the half-ball did. Along the lemon from tip to tip, is the bend sharper, gentler, or the same as before? *(prediction)*

**If the learner is stuck**

- *The learner cannot see why one radius must grow when the other shrinks.* → Multiply the radii before and after, 10 times 10 and then 5 times 20, and tie the product to the unchanged rings. *Uses:* `ways_in/a-shell-closes-into-a-lemon`

**Common questions**

- *Why is this theorem called remarkable?* (entry) Each of a surface's two bends can be seen only from outside, and bending without stretching can change either one. Yet the Gaussian curvature, built from both bends, never changes, and an ant who never leaves the surface can measure it with rings. That link between the outside view and the inside view was the surprise. It is also why general relativity can describe curved space and time with nothing outside to look from. *Uses:* `ways_in/a-shell-closes-into-a-lemon`

**Switching levels**

- To working when: asks how to calculate the bends; mentions line elements. Derive the product formula for a surface of revolution and vary the lemon. *Uses:* `ways_in/two-routes-on-a-surface-of-revolution`, `derivations/product-equals-spacing-formula`
- To formal when: knows the Riemann tensor; asks for a general proof. Prove the Gauss equation, then test the flat torus in the three-sphere. *Uses:* `derivations/gauss-equation-from-commuting-derivatives`, `checks/flat-torus-in-the-three-sphere`

**Pronunciations:** theorema egregium → thee-oh-RAY-muh eh-GRAY-gee-um; Gauss → GOWSS; Codazzi → ko-DAHT-see; Liebmann → LEEP-mahn; Riemann → REE-mahn; Cassini → kuh-SEE-nee

## History

- **Carl Friedrich Gauss (1827).** Proved that the product of the principal curvatures depends only on lengths along the surface; presented 1827, published 1828. Carl Friedrich Gauss (1828), *Disquisitiones generales circa superficies curvas*, Commentationes Societatis Regiae Scientiarum Gottingensis Recentiores 6, 99–146
- **Bernhard Riemann (1854).** Defined curvature from the distance rule alone, in any dimension; published 1868. Bernhard Riemann (1868), *Über die Hypothesen, welche der Geometrie zu Grunde liegen*, Abhandlungen der Königlichen Gesellschaft der Wissenschaften zu Göttingen 13, 133–152

## Review: novice

**Verdict:** fixed (2026-09-13, revision 5)

**Retell attempt:** A plastic ball 20 centimetres across gets cut in half through two opposite dots, and you squeeze the bowl shut into a lemon with the dots as its tips. Nothing stretches, so the ant's rings do not change, so the Gaussian curvature stays one hundredth per square centimetre. Around the lemon's middle the bend is twice as sharp, radius 5 instead of 10, so the bend from tip to tip has to go gentle, radius 20, because 5 times 20 is 100 again. That trade is Gauss's remarkable theorem. I had to stop twice: I could not tell where the 10 centimetres came from, since the ball was given as 20 across, and I could not see why the half of the middle circle turns into a whole circle when you tape the lemon up. I also was not sure whether the ant's number is the same everywhere on a surface or just the same as the outsider's number. With a paper tube, one direction never bends, so the number is zero however you squeeze it, though I kept rereading the sentence about laying the pencil alongside the taped edge. And no flat map of Earth can be exactly to scale, because a perfect map blown up would be the ground bent flat, and Earth's number is one over 40.6 million per square kilometre while paper's is zero. For a town it is centimetres out of 63 kilometres; on world maps Africa is really 14 times Greenland.

**Stumbles (40)**

- “Gauss proved this in 1827 and named it his remarkable theorem: an ant measuring only along the surface can find that number. So no flat map shows every distance of even a small part of Earth at the right scale.”: The colon hides why the ant makes it remarkable, and the jump to maps skips the step that flat paper's number is zero while Earth's is not. 'Right' doubles as a direction in speech.
- “Seen from outside, a spot's Gaussian curvature comes from its sharpest and gentlest bends. Multiply the radii of their best-fit circles, and divide 1 by the result.”: The recap does not restate walking straight or the best-fit circle, both used in the explanation, and the rule is false on a saddle without saying both bends go toward one face. The try-it needs the rolled-poster zero rule, which the recap never gives.
- “with a dot at its top and a dot at its bottom ... The cut edge runs from the top dot down to the bottom dot”: Top and bottom have no meaning on a ball (wording trap).
- “At the middle of the half-ball, every path an ant could walk straight through that spot bends alike.”: 'The middle of the half-ball' could be the deepest point of the bowl or the line halfway between the dots, and every spot of the half-ball curves alike anyway.
- “So the Gaussian curvature there is 1 divided by 10 times 10, which is 1 hundredth per square centimetre.”: Reread: '1 divided by 10 times 10' can be read as one tenth times ten, which is 1.
- “Bend the half-ball gently until the two sides of the cut edge meet along their whole length, and tape them.”: Not doable as written: the cut edge is a circle, so its 'two sides' are unclear, and 'gently' suggests a small change when the shell must close completely.
- “with a sharp tip at each end.”: First what-if: the takeaway says 'at a smooth spot', but the reader is not told the tips are the exception.
- “Before, the line halfway between the dots was half of the ball's middle circle ... So the path around the lemon bends twice as sharply as before.”: One idea under three names (line halfway between the dots, that line, path around the lemon), and the steps from 31.4 centimetres to radius 5 and from half the radius to twice the bend are left to the reader.
- “So an ant on the shell measures the same rings as before, and her number is 1 hundredth per square centimetre, as before. The outsider's number must agree with hers.”: Two sentences in a row start with 'So', and 'must agree' gives no reason; 'the outsider' was never introduced.
- “This means the path along the lemon, from tip to tip, must bend more gently than before. Its radius times 5 must make 100, so its radius is 20 centimetres. A careful drawing of the lemon's outline confirms it.”: Ambiguous 'this' and 'it'; the reason the product must be 100 is implicit; and the reader is not told that the middle path and the tip-to-tip path are the sharpest and gentlest bends.
- “Gauss proved that this holds at every smooth spot of every smooth surface.”: A leap from one lemon to every surface with no reason given.
- “(whole way) A half-ball closes into a lemon”: First what-if a teenager tries: squeeze a whole ball, such as a ping-pong ball. The way never says why the ball had to be cut.
- “Lay a pencil along the outside of the tube ... Squeeze the tube gently into an oval ... Yet the pencil lies snugly wherever you lay it along the tube.”: 'Along the tube' gives no direction the reader can check, 'lies snugly' is a different test from 'touches along its whole length', and creasing is not ruled out.
- “The ring test: walk straight out the same distance from a centre in many directions, then measure the ring through the end marks along the ground.”: The map way uses 'walk straight' and a ball's Gaussian curvature of 1 over the radius times itself without restating either.
- “at one scale, say 1 centimetre for every 10 kilometres. Can every distance on the map be right?”: 'To scale' is never defined, and 'right' doubles as a direction.
- “Picture the map enlarged a million times, so that it is as big as the region. ... So the enlarged map would be the region's ground, bent flat without stretching.”: Why a million is left to the reader, and the step from equal distances to 'the ground bent flat' is a surprise with no link.
- “Its Gaussian curvature is then 1 divided by 6,371 times 6,371, per square kilometre.”: Same misreading as '1 divided by 10 times 10', and the final step from 'not zero' to 'no map' is implicit.
- “So no map is exactly to scale everywhere, not even a map of one town.”: False for the first what-ifs: a globe is to scale, and a map of an area whose ground is not ball-shaped is not covered.
- “Suppose the map keeps every distance from the centre right. Then it draws that ring as a circle about 6,283 kilometres around, at the map scale.”: Step skipped: why the drawn ring is 6,283 kilometres.
- “A ring walked 10 kilometres from the town centre is short by only about 2.6 centimetres. So a town map can be right to far better than the width of a street.”: The ground ring is short but the map ring is too long; the link between the two is missing.
- “on many world maps, Greenland looks about as big as Africa, which is really 14 times larger.”: 'Which' could be Greenland or Africa, and a world map is not a continent.
- “With both bends still toward the shell's inside face ... A friend says the Gaussian curvature there has gone up.”: A shell piece has no obvious inside face, and the friend's claim is not posed as a question.
- “Its mapmaker says the town is too small for Earth's curving to matter, so the map is exactly to scale everywhere. ... Is the mapmaker right?”: Ambiguous: the mapmaker is right in everyday life and wrong exactly, so a correct everyday answer would be marked wrong; the setting (a smooth ball) comes only later.
- “For a town the error is real but only millimetres.”: Contradicts the map way, where a 10 kilometre ring is off by 2.6 centimetres.
- “Close it into a lemon, so it bends more sharply around its middle. Does the path from tip to tip bend more sharply, more gently, or the same as before?”: The reader cannot picture how to close a half-ball, and 'the same as before' has no named before.
- “glossary: (no entries for 'smooth spot' or 'exactly to scale'); Gaussian curvature: 'with a minus sign on a saddle'”: Two terms the entry rung relies on are undefined, and the saddle rule omits 'toward each face'.
- “At each smooth spot, its sharpest and gentlest bends can change, but the Gaussian curvature built from them stays the same.”: Ambiguous 'its': the nearest noun is the shell, but the bends belong to the spot.
- “An ant who never leaves the surface gets the same number at every smooth spot, from rings she walks out and measures along the surface.”: Reread: 'the same number at every smooth spot' reads as though the number is the same all over the surface, which is false on an egg. The meaning is that her number matches the outsider's.
- “Where a path bends, one circle matches the bend best; the smaller the circle, the sharper the bend.”: The explanation and the check both say 'best-fit circle', but the recap never names the term, so the reader meets the name cold.
- “Picture a thin, hollow plastic ball, 20 centimetres across. ... every path an ant could walk straight along bends with a best-fit circle of radius 10 centimetres.”: Two steps left implicit: where 10 comes from when the ball was given as 20 across, and why a straight walk's best-fit circle is a circle of the ball itself.
- “On the half-ball, the middle path was half of the ball's middle circle.”: A ball has no one middle circle; which one is meant depends on the two dots, and that is not said.
- “On the lemon, the middle path closes into a whole circle 31.4 centimetres around.”: Surprising claim with the reason left out: why does half a circle become a whole one, and why is its length unchanged?
- “Its radius times 5 must make 100, so that 1 divided by the product is again 1 hundredth.”: The recap's rule works only when both bends go toward the same face, and the way never says they still do at the lemon's middle; 'Its' also has two candidates in the sentence before.
- “Yet wherever you lay the pencil alongside the taped edge, it touches the paper along its whole length.”: Reread: 'wherever' promises many places, but 'alongside the taped edge' names one. The rule the reader should follow, keep the pencil pointing along the tube, is lost.
- “Can a flat paper map show every distance in a region of Earth at the right scale?”: The note's own recaps use 'right' as a direction, in 'without ever steering left or right', so using it for 'correct' gives one word two senses. The first pass replaced 'right' inside the explanation but left it in the way's question and in a check.
- “Surveyors measure distances along the ground between towns, rivers and hills.”: An entry way must stand alone, and 'surveyor' is defined only in a prerequisite note.
- “A ring walked 10 kilometres from a town's centre is short by only about 2.6 centimetres.”: A change with no reference: short of what? The town-map check names the comparison, this sentence does not.
- “At one smooth spot, you bend the shell until its sharpest bend has a best-fit circle of radius 8 centimetres.”: Ambiguous 'its': read plainly it is the shell's sharpest bend, but the question is about one spot.
- “Explain why no flat map is exactly to scale everywhere, and why a town map still looks perfect.”: The objective drops the scope the map way was careful to add: a globe is to scale, and the claim is about flat maps of a round Earth.
- “Explain why bending a shell without stretching can change its two bends but not its Gaussian curvature, and predict one bend from the other.”: 'its two bends' and 'its Gaussian curvature' attach to the shell, but both belong to a single spot.

**Fixes**

- Shell way: two opposite dots instead of top and bottom; a doable squeeze of the rim's two half-circles; one name, the middle path, with every arithmetic step spelled out; the outsider's sharpest and gentlest bends named at the lemon's middle; the jump to every surface given a reason; the tips named as the only non-smooth spots; a what-if on squeezing a whole ball (a dented ping-pong ball creases). Dropped the unexplained 29 centimetre tip-to-tip length rather than add its reason.
- Shell way recap restates walking straight, the best-fit circle, the same-face condition, the rolled-poster zero rule, and the ant's rings, so the way and its try-it stand alone.
- Try-it: the pencil lies alongside the taped edge, the squeeze is without creasing, and one test (touches along its whole length) is used before and after.
- Map way: defined 'exactly to scale', explained the million, linked equal lengths to the ground bent flat, gave Earth's number as 1 divided by 40.6 million, scoped the conclusion to flat maps of an area of a round Earth, spelled out the 6,283 kilometre circle, linked the short ground ring to the long map ring, and replaced 'right' with 'correct'. Recap now gives walking straight and the ball and flat-paper numbers.
- Entry checks: the shell check names the face and asks about the friend; the town-map check names its setting first and asks two separate questions so an everyday answer is not marked wrong.
- Summary split so the map conclusion follows from zero versus not zero; takeaway and Gaussian curvature glossary split under 32 words; glossary gained smooth spot and exactly to scale; the misconception correction is scoped to towns a few kilometres across; the opening question describes how to close the half-ball.
- Ladder: the working way 'Two routes to one number on a surface of revolution' now names the entry's sharpest and gentlest bends as the principal curvatures and restates the spacing formula before using it with f = r. Other non-entry ways already refer back to the way they continue; the five ways are genuinely different routes.
- Budgets after review: entry explanations 956 of 1,000 words, other way fields 593 of 650. Nothing was compressed.
- Bumped the revision to 2.
- SECOND NOVICE PASS over revision 2, by a fresh reader of the entry rung. The stumbles above this line were recorded in the first pass against revision 1; the fourteen below it are new, quoted from revision 2, and every one is fixed in revision 3.
- Shell way: the best-fit circle is named in the recap; the 10 centimetre radius is derived from the 20 centimetre ball and from the fact that a straight walk's circle goes all the way around it; the ball's 'middle circle' is now the circle halfway between the dots; the middle path's ends are followed onto the rim, so closing into a whole circle of the same length has a reason; the same-face condition is restated at the lemon's middle before the rule is used, and the ambiguous 'Its radius' is replaced by the tip-to-tip bend.
- Shell recap: the ant's number is said to match the outsider's, instead of 'the same number at every smooth spot', which read as constant over the surface.
- Try-it: the pencil may be laid anywhere on the tube as long as it points the same way as the taped edge, so 'wherever' and the single named place no longer fight.
- Map way: 'surveyors' is glossed in place; the ring's shortfall names what it is short of; the way's question and the shell check use 'exactly to scale' and 'correct', so 'right' keeps only its direction sense across the note.
- Objectives: the map objective is scoped to a region of Earth, and both entry objectives attach the bends and the curvature to a spot rather than to the shell.
- Budgets after this pass: entry explanations 1,048 words against a 1,000 cap, inside the review allowance of 1,100 and used only for the recorded stumble fixes; other way fields 623 of 650. Nothing was compressed and nothing was dropped.
- Bumped the revision to 3.

**Concerns**

- The physics reviewer should confirm two entry claims: a whole closed ball cannot be bent into another smooth shape without stretching (rigidity of closed convex surfaces), and a dented ping-pong ball creases around the dent.
- New in this pass, for the physics reviewer: the added sentence 'every path an ant could walk straight along bends with a best-fit circle that goes all the way around the ball' asserts that straight walks on a ball are its great circles, and the added 'Both of these bends go toward the shell's inside face' asserts the sign at the lemon's middle. Both look right to me but are mine, not the writer's.
- The working misconception each-bend-is-intrinsic is diagnosed only by the formal check hypersurface-in-four-dimensions; no working-rung check exposes it, although the problem lemon-from-a-third-of-a-ball targets it.
- Entry explanations now sit at 1,048 words, above the 1,000 cap and inside the review allowance. Any further entry addition needs a cut, and an editor may want to trim this rung back under the cap.
- The vault spells the theorem's pronunciation two ways (this note, intrinsic-geometry and intrinsic-versus-extrinsic-curvature versus second-fundamental-form); an editor should pick one.
- The second fundamental form and the shape operator have no conventions row, and h_{mu nu} clashes with the linearized-gravity perturbation; this affects only the working and formal rungs.
- The flagship visual half-ball-closes-into-a-lemon should use this note's words: two opposite dots, the rim's two half-circles, and the middle path.
- All three visuals are still proposals with sketches rather than catalog entries, and the note's prerequisites differ from the registry for riemann-curvature-tensor, so sync_registry.py should run.

**Re-read** (2026-09-13, revision 5): 7 stumbles in 7 changed passages

- “On a smooth ball the size of Earth, a ring walked 5 kilometres from a centre comes out about 3 millimetres shorter than a ring walked 5 kilometres out on flat paper.”: One sentence names the same walk two ways, "walked 5 kilometres from a centre" and "walked 5 kilometres out", so I stopped to check whether the second ring was measured from a centre too. Saying it once runs the sentence past 32 words, so the comparison is split in two.
- “Before bending, both bends at the spot had a radius of 12 centimetres.”: "Both bends" does not say which two of the many paths through the spot are meant, and the answer only names them as sharpest and gentlest two sentences later.
- “On flat paper it is about 6.28 times that distance.”: "It" could be the ring, the ground or the walk, and a ring is a thing while 6.28 times a distance is a length, so I had to reread to see that the ring's length is meant.
- “If one of the two does not bend at all, as along a rolled poster, the number is zero.”: "The two" names nothing. The sentence before ends on the Gaussian curvature, so I had to go back two sentences to the sharpest and gentlest bends. Naming them costs six characters, and the recap stands at 698 of its 700-character cap, so the clearer wording does not fit; every other sentence in the recap is used by the lemon explanation, so there is nothing low-value to trim. Recorded for an editor rather than fixed.
- “That circle is a little over 6.28 times 1,000, or about 6,283 kilometres around.”: "Or" reads as "that is", so I multiplied 6.28 by 1,000, got 6,280, and could not make it agree with 6,283. Also 1,000 carries no unit here.
- “A ring walked 10 kilometres from a town's centre comes out only about 2.6 centimetres shorter than a ring walked 10 kilometres out on flat paper. So a map that keeps every distance from the centre correct draws that ring about 2.6 centimetres too long, out of almost 63 kilometres.”: Two stops. The same walk is named two ways again, and the flat ring is no longer given a length, so the "almost 63 kilometres" in the next sentence arrives from nowhere and I had to work out 6.28 times 10 myself.
- “Rulers in the plane through a star fix its Gaussian curvature outside the star, minus G M over c squared r cubed, and the funnel drawn for that plane has bends whose product matches it; the funnel's height stands for nothing in space.”: Forty words and three claims in one sentence, squeezed against the 240-character takeaway cap. "Its" can be the plane's or the star's, and "matches it" can be the curvature or the product of the rulers' readings.
- Fix: checks/perfect-town-map question and ways_in/no-flat-map-is-to-scale explanation: both rings are now walked the same way, "from a centre". In the check the comparison became two sentences, "Compare two rings, each walked 5 kilometres from a centre: one on flat paper, one on a smooth ball the size of Earth. The ring on the ball comes out about 3 millimetres shorter.", because one sentence ran to 34 words.
- Fix: ways_in/no-flat-map-is-to-scale explanation: added "Both rings are almost 63 kilometres around." The physics fix removed "6.28 times 10 kilometres", which was the only support for the "out of almost 63 kilometres" in the next sentence; the new sentence states no number the paragraph did not already claim, and the flat ring is 62.83 kilometres.
- Fix: ways_in/no-flat-map-is-to-scale explanation: "or about 6,283 kilometres around" became "which comes to about 6,283 kilometres around", and 1,000 gained its unit, so the reader is not invited to read 6.28 times 1,000 as an exact equality.
- Fix: checks/squeeze-a-shell-from-a-ball answer: "both bends" became "the sharpest and the gentlest bend", naming the two the question and the recap use.
- Fix: glossary/ring-test: the pronoun "it" became "the ring".
- Fix: ways_in/rulers-around-a-star-read-the-funnel takeaway: split into three sentences, "its" became "the", and "matches it" became "matches the curvature". The three claims, their conditions and the value are unchanged; it lands at exactly the 240-character cap, so "drawn for that plane" became "drawn for the plane" to fit.
- Fix: Not fixed, and left for an editor: the recap's "If one of the two" (stumble 4), because the clearer wording needs six characters the 700-character recap cap does not have.
- Fix: Read the two changed entry ways against rule 17: neither physics fix adds a second new idea to its way, and the one sentence added carries a number, not an idea. Nothing was dropped, and entry prose was not compressed.

## Review: physics

**Verdict:** fixed (2026-09-13, revision 5)

**Verification**

- Entry lemon: half of a ball 20 cm across, cut through two opposite dots and closed up, keeps K = 1 hundredth per square centimetre and has bends of radii 5 cm and 20 cm at its middle.: Modelled the closed lune as the surface of revolution r = b sin(rho/a) with b = a times (lune angle)/(full turn); hand algebra plus python. → A half-ball is a half-turn lune, so b = a/2 = 5 cm. kappa_p = 1/b = 1/5 and kappa_m = b/a^2 = 1/20, product 1/100 = 1/a^2. The middle path is 31.4 cm before and after, giving radius 10 cm then 5 cm. Every number in the way is correct, including the 20 cm read off the outline (the profile's plane curvature at the middle is -r'' = b/a^2 = 1/20).
- Novice rewrite: 'every path an ant could walk straight along bends with a best-fit circle that goes all the way around the ball'.: Straight walks on a sphere are great circles; the osculating circle of a great circle is the great circle itself. → Correct. Radius equals the ball's radius, 10 cm, and the circle does go all the way around the ball.
- Novice rewrite: 'Both of these bends go toward the shell's inside face, as every bend did on the half-ball.': Unit normal n = (-z' cos phi, -z' sin phi, r'); at the lemon's middle r' = 0 and z' = 1, so n points at the axis. Signs of kappa_p and kappa_m taken against it. → Correct: both are positive against the inward normal. K = 1/a^2 > 0 also forces the two bends to share a face at every smooth spot of any shell cut from a ball; only a flip of both together (a reflected cap) is possible, which is why the entry check is right to state the condition.
- Entry recap rule: 'If one path does not bend at all, as along a rolled poster, the number is zero.': Tried the standard saddle counterexample: at a saddle point the asymptotic directions have zero normal curvature. → False as written, since a straight walk in an asymptotic direction does not bend there while K < 0. Fixed to 'if one of those two paths' (a principal direction), which is exactly true: a vanishing principal curvature forces K = 0.
- Entry claim: a whole, closed ball cannot be bent into any other smooth shape without stretching.: A bending preserves K, so the image is a compact connected surface of constant K; the farthest-point argument gives K > 0, Hadamard gives convexity, and Liebmann (or, with no smoothness at all, the Alexandrov-Pogorelov uniqueness theorem for closed convex surfaces) forces a round sphere. → Correct for C^2 and above, which the word 'smooth' carries. The C^1 escape is Nash-Kuiper, which the formal way already names, so entry and formal do not contradict each other.
- Entry claim: a dented ping-pong ball creases sharply around the dent.: Reflecting a spherical cap through the plane of its boundary circle is an isometry of the shell that leaves a ridge along that circle; real thin shells buckle into such a ridge. → Correct, and it is the right reason for cutting the ball first.
- Entry try-it: squeezing a paper tube into an oval keeps the path along the tube unbent, so K stays zero.: A cylinder over any convex plane curve is developable: the rulings stay straight and parallel to the axis, and one principal curvature is zero everywhere. → Correct. A straight pencil laid anywhere on the outside along a ruling touches along its whole length, as the text says, as long as the squeezed cross-section stays convex, which 'gently into an oval' scopes.
- Map numbers: Earth radius 6,371 km, K = 1 over about 40.6 million per square kilometre; ring at 1,000 km is 6,257 km against a flat 6,283 km, 26 km and 0.4 per cent; rings at 10 km and 5 km fall short by 2.6 cm and 3 mm; Africa is about 14 times Greenland.: python, with ring length 2 pi a sin(s/a) and areas 30.37 and 2.166 million square kilometres. → 6,371^2 = 40,589,641; ring 6,257.4 km against 6,283.2 km, short by 25.8 km or 0.41 per cent; 2.58 cm out of 62.83 km; 3.22 mm out of 31.42 km; ratio 14.0. All correct. But two comparisons were made against '6.28 times', which cannot carry them: 6.28 times 1,000 is 6,280, not 6,283, and 6.28 times 10 km sits 31.8 m below the true flat ring, 1,200 times the 2.6 cm effect. Both now compare with the ring on flat paper, and the glossary's ring test says 'about 6.28 times'.
- Entry check squeeze-a-shell-from-a-ball: from a ball of radius 12 cm, a sharpest bend of radius 8 cm forces a gentlest bend of radius 18 cm, with K unchanged at 1/144 per square centimetre.: Arithmetic, plus a realizability test with the lemon family a = 12 cm, b = 8 cm. → 144/8 = 18 exactly, and b = 8 is at most a = 12, so an actual bending reaches this state; kappa_p = 1/8 and kappa_m = b/a^2 = 1/18. Tolerance of 3 per cent is fine. The answer's 'every bend at the spot had a radius of 12 centimetres' was false for paths that are not straight walks (a small circle on a ball has a smaller best-fit circle), so it now reads 'both bends'.
- Working derivation: normal, kappa_m = r'z'' - z'r'', kappa_p = z'/r, z' kappa_m = -r'', and kappa_m kappa_p = -r''/r = K on a surface of revolution.: Re-derived every move by hand: the cross product X_rho x X_phi / r, the three second-derivative dot products, the vanishing mixed term, and the arc-length identity r'r'' + z'z'' = 0. → Every step correct. The mixed term vanishes and the line element is diagonal, so the profile and the circles are principal; the product matches the spacing formula for either unit normal, as the conditions say.
- Working: the lemons r = b sin(rho/a) with 0 < b <= a all have K = 1/a^2, match the sphere through phi_sphere = (b/a) phi, have cone points unless b = a, and for b > a exist only as a band.: Hand algebra and python. → All correct: r'' = -r/a^2; a dphi_sphere = b dphi; near a tip r is about (b/a) rho so small rings measure 2 pi (b/a) rho; |r'| <= 1 needs |cos(rho/a)| <= a/b.
- Working problem lemon-from-a-third-of-a-ball: a = 9 cm, a third of the shell, K = 1/81 per square centimetre, bends of radii 3 cm and 27 cm.: python, with b = a times (120 degrees / full turn) = 3 cm. → Correct throughout; the 120-degree lune is exactly a third of the shell, and (1/3)(1/27) = 1/81. Numeric answer 27 cm with 2 per cent tolerance is fine.
- Working: the slice outside a static spherical body has K = -r_s/2r^3 = -GM/c^2 r^3, and the funnel z = 2 sqrt(r_s(r - r_s)) has kappa_p = sqrt(r_s/r^3) and kappa_m = -(1/2) sqrt(r_s/r^3), whose product is that K.: Differentiated r' = sqrt(1 - r_s/r) to get r'' = r_s/2r^2, applied the spacing formula, then integrated z' = sqrt(r_s/r) to get the funnel; checked the metric against the conventions' Schwarzschild row. → All correct, including the negative sign (the plane curves like a saddle) and the opposite faces of the two bends.
- Worked example: Sun r_s = 2,953 m, K = -4.39e-24 per square metre, radius 3.19 au, funnel radii 2.26 au and 4.51 au; Earth r_s = 8.87 mm, K = -1.72e-23, radius 1.61 au, 3.9 times denser.: python with GM_sun = 1.327e20, R_sun = 6.957e8, GM_earth = 3.986e14, R_earth = 6.371e6, c = 2.99792458e8. → r_s = 2,952.97 m; K = -4.3849e-24, so the three-figure value is -4.38e-24, not -4.39e-24: corrected (the two-figure answer -4.4e-24 stands). |K|^-1/2 = 4.776e11 m = 3.192 au; bend radii 2.257 au and 4.514 au, product 10.19 against 3.19^2 = 10.18. Earth: 8.870 mm, -1.7150e-23, 1.614 au. Density ratio 3.911 equals the K ratio exactly, as K = -(4 pi G/3c^2) times mean density requires. The displayed chain keeps its rounded intermediates, so recomputing from 2953 and 3.367 gives 4.385e-24; the corrected figure is the three-figure value of the exact quantity.
- Working check funnel-wall-at-the-horizon: r_s = 29.5 km for 10 solar masses, K = -1/2 r_s^2 there, radius of curvature sqrt(2) r_s = 41.8 km, slope diverges.: python; dz/dr = sqrt(r_s/(r - r_s)). → 29.53 km and 41.76 km; correct within the 2 per cent tolerance. The divergence lives only in the drawing's invented height direction, while K and both bends stay finite, as the answer says.
- Formal derivation: R_{sigma nu rho mu} = h_{rho sigma} h_{mu nu} - h_{mu sigma} h_{rho nu} and R_1212 = det h in the course convention, plus the Codazzi equation.: Re-derived every move by hand, matching the antisymmetrized left side index by index against the conventions' Riemann row; then an independent python check on a generic non-symmetric graph surface, computing metric, second fundamental form, Christoffel symbols and the course Riemann tensor by finite differences. → R_1212 = det h agreed to seven digits at two sample points, and K = det h / det g. Sign matches the conventions: the unit sphere with the outward normal gives h = -g and K = +1. The Codazzi normal part checks out by hand as well.
- Formal problem (a): K = R_uvuv/EG for ds^2 = E du^2 + G dv^2, the six Christoffel symbols, the R_uvuv expansion and the standard closed form.: python finite-difference computation of the course Riemann tensor for three metrics (a sphere in geodesic polars, a generic orthogonal metric, and Mercator), compared with both the stated expansion and the standard form. → All three agree to eight digits, including sign (the sphere comes out positive). The Christoffel list and the index pattern of R^u_{vuv} match the conventions exactly.
- Formal problem (b) and (c): Mercator ds^2 = sech^2(v/a)(du^2 + dv^2) with sin(latitude) = tanh(v/a) gives K = 1/a^2, and the chart enlarges lengths by sec(latitude), a factor 2 at 60 degrees.: Checked that the chart metric is the round sphere's by substituting the latitude relation; conformal curvature formula; hand algebra for the scale factor. → Correct: the metric is the sphere's, K = 1/a^2 = kappa_1 kappa_2, ground length is cos(latitude) times chart length so the chart enlarges by sec(latitude), and sec 60 degrees = 2 exactly. Constant E and G would give K = 0, so no chart of a region of the sphere has a constant scale.
- Formal check flat-torus-in-the-three-sphere: K = ambient sectional curvature plus det S gives 0, and the two normals in four-dimensional Euclidean space give +1 and -1.: Clifford torus as the product of two circles of radius 1/sqrt(2) in the unit three-sphere; second fundamental form for the position-vector normal. → Correct. Every plane in the unit three-sphere has sectional curvature +1 and the torus is minimal there with principal curvatures +1 and -1, so K = 1 - 1 = 0; the position vector gives h = -g and det S = +1, the three-sphere normal gives -1, and the sum is zero.
- Formal check hypersurface-in-four-dimensions: principal curvatures 2, 3, 6 per metre give sectional curvatures 6, 12 and 18 per square metre, and each principal curvature squared is a product of two divided by the third.: Arithmetic. → Correct: 6 times 12 over 18 = 4, 6 times 18 over 12 = 9, 12 times 18 over 6 = 36, so the triple is fixed up to one overall sign. The named plane carries the two largest, 3 and 6, giving the stated 18 per square metre.
- Formal limits: Beez-Killing rigidity at rank at least 3, K = ambient sectional curvature plus det S in a Riemannian three-manifold, K = sum of det S over an orthonormal frame of normals in higher codimension, Liebmann, Nash-Kuiper.: Compared each statement with the standard results and checked the scope words. → All correct as scoped. A surface's shape operator has rank at most 2, so the Beez-Killing obstruction never bites for surfaces, which is the point the way makes.
- Observation: the plane through the Sun has K = -gamma GM/c^2 r^3 to first order, and Cassini gave gamma - 1 = (2.1 +/- 2.3)e-5.: Computed the Gaussian curvature of the equatorial slice of the post-Newtonian isotropic metric g_ij = (1 + 2 gamma M/r) delta_ij with the conformal formula, K = -Laplacian of (gamma M/r) = -gamma M/r^3 to first order. → Correct, and it matches the conventions' post-Newtonian row; gamma = 1 recovers the exact Schwarzschild value -GM/c^2 r^3. The quoted measurement is the published one.
- References: Bertotti, Iess and Tortora 2003; Gauss 1828; Riemann 1868.: Crossref record for the Cassini paper; EuDML record for Riemann; bibliographic records for the Gauss memoir; web search for each. → Cassini: Nature 425, 374-376 (2003), doi 10.1038/nature01997, with gamma - 1 = (2.1 +/- 2.3)e-5 - confirmed. Gauss: Disquisitiones generales circa superficies curvas, Commentationes Societatis Regiae Scientiarum Gottingensis Recentiores 6 (1828), 99-146, presented 8 October 1827 - confirmed, so the history entry's 1827 date and its scope are right. Riemann: Abhandlungen der Koeniglichen Gesellschaft der Wissenschaften zu Goettingen 13 (1868), 133-152, from the 1854 habilitation lecture - confirmed. All three set verified; neither older work has a DOI.
- Structure: prerequisites direct and acyclic, assumes legal, formal rung sized for a foundation note.: Walked the registry graph from gaussian-curvature, intrinsic-geometry and riemann-curvature-tensor; checked every id in each way's assumes against the prerequisites and their prerequisites; counted formal items. → No cycles. intrinsic-versus-extrinsic-curvature is a prerequisite of gaussian-curvature, so its use in assumes is legal. Two formal checks and one formal problem, two problems in total spanning two rungs, one worked example, one real observation: the foundation tier's requirements are met. The registry still lists only two prerequisites, so sync_registry.py should run.

**Counterexamples tried**

- Saddle point and its asymptotic directions: broke the entry recap's zero rule, since a straight walk in an asymptotic direction does not bend while K is negative. Fixed by restricting the rule to the two principal paths.
- Small circle on a ball (a path that is not a straight walk): its best-fit circle is smaller than the ball's, which broke 'every bend at the spot had a radius of 12 centimetres' in the entry check. Fixed to 'both bends'.
- Reflected spherical cap: an isometry that turns both bends toward the other face. This is exactly why the entry check must say that both bends still go toward the inner face, and it does.
- Whole closed sphere: a case where the metric does fix the bends, which broke the formal takeaway's 'the metric fixes that product, not the bends'. Softened to 'need not fix the bends'; the way's limits already carried Liebmann.
- Nash-Kuiper C^1 embeddings: break any unqualified 'cannot be bent'. The entry says 'any other smooth shape' and the formal way names the C^1 escape, so both survive.
- Rolled poster and the squeezed oval tube: bent but flat, K = 0 throughout. The try-it survives, since a cylinder over a convex curve keeps straight rulings.
- Cone point: the lemon's own tips, with a turn of b/a of a full turn. Every claim in the note is restricted to smooth spots, and the working way states the cone point explicitly, so nothing breaks.
- Barrel with no tips (b > a): another surface with the same line element and no tips at all; already in the note, and it confirms that the family, not the sphere, is what the metric fixes.
- Clifford torus in the three-sphere: breaks K = product of the bends in a curved ambient space; carried by its own formal check.
- Region bigger than half a closed surface, a hole, a Moebius band: the theorem here is local and the determinant of the shape operator is unchanged by reversing the normal, so none of these break any statement in the note; no orientability hypothesis is needed.
- Horizon of the funnel: the drawing's slope diverges while K stays at -1/2 r_s^2; carried by its own working check.
- Inside a star: the way's formula K = -GM/c^2 r^3 is a vacuum result, so the working takeaway now says 'outside the star'.

**Fixes**

- Entry recap: 'If one path does not bend at all' became 'If one of the two does not bend at all', naming the outsider's two bends, because a saddle's asymptotic direction does not bend while the Gaussian curvature is not zero. Kept to six characters so the recap stays inside its 700-character cap.
- Entry map way: 'That circle is 6.28 times 1,000, or about 6,283 kilometres around' became 'a little over 6.28 times 1,000', since 6.28 times 1,000 is 6,280 and the gap is a tenth of the 26 kilometre error being quoted.
- Entry map way: the town ring is now 'about 2.6 centimetres shorter than a ring walked 10 kilometres out on flat paper' instead of 'short of 6.28 times 10 kilometres', because the rounded 6.28 is itself 31.8 metres off, more than a thousand times the effect.
- Glossary ring test: 'On flat paper it is about 6.28 times that distance', for the same reason.
- Entry check perfect-town-map: the 3 millimetre shortfall is now measured against a ring walked 5 kilometres out on flat paper, not against 6.28 times 5 kilometres.
- Entry check squeeze-a-shell-from-a-ball: 'every bend at the spot had a radius of 12 centimetres' became 'both bends at the spot', since a path that is not a straight walk can have a smaller best-fit circle.
- Worked example: the Sun's Gaussian curvature at three figures is -4.38e-24 per square metre, not -4.39e-24. The two-figure answer was already right.
- Working takeaway of the funnel way: 'fix its Gaussian curvature outside the star', since the formula is a vacuum result.
- Formal takeaway: 'the metric fixes that product but need not fix the bends', since a whole sphere is rigid.
- All three references verified against Crossref, EuDML and bibliographic records; authors, years, titles, venues and page ranges all confirmed as written, and the Cassini DOI checked.
- Bumped the revision to 4.

**Concerns**

- Missing convention, still open: course-conventions.md has no row for the second fundamental form or the shape operator, neither the symbol nor the sign tied to the choice of unit normal, and h_{mu nu} here collides with the linearized-gravity metric perturbation in that file. The note's own use is self-consistent (h from the Gauss formula with an explicit normal, and det S normal-independent in two dimensions), and notation_traps is left empty because a trap's course_choice must come from the conventions file. An editor should add the row, then this note can carry the trap about the opposite sign choice.
- The entry way's chain leans on the recap's 'Her number and the outsider's agree at every smooth spot', which is the theorem itself, imported from gaussian-curvature. The physics is fine and the note never claims to prove that agreement at entry, but an editor should check that gaussian-curvature really establishes it, or the entry way reads circular to a careful beginner.
- The entry rung now sits at about 1,055 words against a 1,000 word cap, inside the review allowance, and every word past the cap is tied to a recorded fix. Other way fields are at 631 of 650. Nothing was compressed.
- In practice a real hemisphere shell closes into the lemon through creased intermediate states; only the two end shapes are isometric, which is all the theorem needs. The flagship visual should not animate a crease-free morph without saying so.
- Inherited and still open: the working misconception each-bend-is-intrinsic is diagnosed only by the formal check hypersurface-in-four-dimensions, with no working-rung check, although the problem lemon-from-a-third-of-a-ball targets it.
- Inherited and still open: the vault spells the theorem's pronunciation two ways, 'thee-oh-RAY-muh' in this note, intrinsic-geometry and intrinsic-versus-extrinsic-curvature against 'tay-oh-RAY-mah' in second-fundamental-form. Not a physics question; an editor should pick one.
- All three visuals are proposals with sketches rather than catalog entries, and the note's prerequisites still differ from the registry for riemann-curvature-tensor, so sync_registry.py should run now that both reviews have signed.

**Diff check** (2026-09-13, revision 5)

- Entry check perfect-town-map, question: 'Compare two rings, each walked 5 kilometres from a centre: one on flat paper, one on a smooth ball the size of Earth. The ring on the ball comes out about 3 millimetres shorter.': Recomputed with python3: ring on a sphere of radius 6,371 km at geodesic distance 5 km is 2 pi a sin(s/a) = 31.415924 km; the flat ring is 2 pi s = 31.415927 km; the shortfall is 3.22e-6 km. Repeated with the equatorial radius 6,378 km, which gives 3.22 mm as well, since the shortfall scales as 1/a squared. → Accurate. 3.2 millimetres rounds to 'about 3 millimetres', and the split into two sentences changes no claim, number or condition: the comparison is still flat paper against a ball the size of Earth at the same 5 kilometres.
- Entry check perfect-town-map, answer, unchanged but re-checked against the reworded question: 'about 3 millimetres too long, out of more than 31 kilometres.': Same computation: both rings are 31.4159 km, so 'more than 31 kilometres' is true whichever ring the reader takes it for, and the map error equals the shortfall. → Accurate. The 31 kilometres is no longer stated in the question, so the reader meets it first in the answer; that is a readability call for an editor, not an error.
- Entry check squeeze-a-shell-from-a-ball, answer: 'Before bending, the sharpest and the gentlest bend at the spot each had a radius of 12 centimetres.': On a sphere of radius 12 cm every normal section has curvature 1/12 per centimetre, so the largest and the smallest of them coincide at a radius of 12 cm. Worked the check to its answer: K = 1/144 per square centimetre is unchanged by bending without stretching, both bends stay toward the same face, so the radii multiply to 144 and 144/8 = 18 cm, matching the numeric field (18 cm, magnitude, rel_tol 0.03). → Accurate, and it claims exactly what 'both bends at the spot' claimed while naming which two bends are meant.
- Glossary ring test: 'On flat paper the ring is about 6.28 times that distance.': On flat paper the end marks of straight walks of length s from a centre lie on a circle of radius s, of length 2 pi s = 6.2832 s. Checked that 'that distance' can only refer to the walked distance named in the previous sentence. → Accurate. Replacing 'it' by 'the ring' names the subject and claims the same thing.
- Entry way no-flat-map-is-to-scale: 'That circle is a little over 6.28 times 1,000 kilometres, which comes to about 6,283 kilometres around.': 2 pi times 1,000 km = 6,283.185 km with python3; 6.28 times 1,000 km = 6,280 km, so 'a little over' is right and the kilometres are now attached to the multiplication. Checked the sentences that use it: the measured ring is 2 pi a sin(1000/a) = 6,257.4 km, so the map ring is 25.8 km too long, 0.41 per cent, matching 'about 26 kilometres' and '0.4 per cent'. → Accurate; the added unit changes no number.
- Entry way no-flat-map-is-to-scale: 'A ring walked 10 kilometres from a town's centre comes out only about 2.6 centimetres shorter than a ring walked 10 kilometres from a centre on flat paper. Both rings are almost 63 kilometres around.': With python3: flat ring 2 pi times 10 km = 62.83185 km; ring on a 6,371 km ball 62.83183 km; shortfall 2.58e-5 km = 2.58 cm. Checked the new sentence against both rings, since 'both' must be true of each: 62.8318 km and 62.8318 km, both under 63 km and within 0.17 km of it. → Accurate. The added sentence states no number the paragraph did not already imply, and it anchors the 'out of almost 63 kilometres' in the next sentence. 'From a centre on flat paper' claims the same as the old 'out on flat paper'.
- Working way rulers-around-a-star-read-the-funnel, takeaway: 'Rulers in the plane through a star fix the Gaussian curvature outside the star, minus G M over c squared r cubed. The funnel drawn for the plane has bends whose product matches the curvature. The funnel's height stands for nothing in space.': Re-derived in course conventions. For d(ell) squared = dr squared / (1 - r_s/r) + r squared d(phi) squared, write the profile by ruler distance rho: dr/d(rho) = sqrt(1 - r_s/r), so d squared r / d(rho) squared = r_s / 2 r squared and K = -(d squared r / d(rho) squared)/r = -r_s/2 r cubed = -G M / c squared r cubed with r_s = 2 G M / c squared. For the funnel z = 2 sqrt(r_s (r - r_s)) in flat three-space: dz/d(rho) = sqrt(r_s/r), kappa_parallel = sqrt(r_s/r cubed), kappa_meridian = -(1/2) sqrt(r_s/r cubed) toward the opposite face, product -r_s/2 r cubed. Signs agree, and the sign is negative, the saddle the way describes. Checked the vacuum condition ('outside the star') and the slicing (observers at rest relative to a static, spherical, non-rotating body, one moment of their time), both stated in the explanation. → Accurate. Splitting one sentence into three keeps every claim: the curvature value, the vacuum restriction, the product of the funnel's two bends, and the warning about the height. 'The Gaussian curvature' for 'its Gaussian curvature' and 'the plane' for 'that plane' lose nothing, since the way names only one plane.
- Consistency of the changed sentences with the rest of the note and with course conventions.: Re-read the lemon way, the map way, the funnel way, both changed checks and the glossary together. Checked the entry rung for a second sense of 'ring', 'bend' and 'centre'; checked that entry numbers stay in everyday units with no scientific notation; checked that the funnel takeaway stays plain text with symbols in words, at 240 characters against the 240 cap. → Consistent. No convention in course-conventions.md is touched by any changed sentence, and no number in the note now disagrees with another.
- Fix: No errors found in the changed sentences; nothing edited, so the revision stays 5.
