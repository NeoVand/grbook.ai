---
type: "concept"
schema_version: 2
id: "space-of-constant-curvature"
title: "Space of constant curvature"
tagline: "A world whose curving, measured with small rings, is the same at every spot"
domain: "curvature"
tier: "core"
status: "physics-reviewed"
revision: 5
updated: "2026-09-16"
aliases: ["maximally symmetric space", "constant-curvature space", "spacetime of constant curvature"]
prerequisites: ["gaussian-curvature", "riemann-curvature-tensor", "ricci-scalar", "contracted-bianchi-identity", "killing-vector"]
leads_to: ["robertson-walker-metric", "de-sitter-spacetime", "anti-de-sitter-spacetime", "cosmic-topology"]
visuals: ["slide-a-patch-across-a-ball-and-an-egg", "paced-ring-on-a-ball-and-a-plain", "distant-ruler-in-three-spaces", "hyperboloids-in-flat-spacetime"]
---

# Space of constant curvature

*A world whose curving, measured with small rings, is the same at every spot*

`space-of-constant-curvature` · curvature · core · physics-reviewed (revision 5)

**Needs:** [[gaussian-curvature]] (entry) · [[riemann-curvature-tensor]] (working) · [[ricci-scalar]] (working) · [[contracted-bianchi-identity]] (formal) · [[killing-vector]] (formal)  
**Opens:** [[robertson-walker-metric]] · [[de-sitter-spacetime]] · [[anti-de-sitter-spacetime]] · [[cosmic-topology]]  
**Related:** [[einstein-space]] · [[sectional-curvature]] · [[hyperbolic-plane]] · [[three-sphere]] · [[conformally-flat-metric]]  
**Visuals:** ★ [[slide-a-patch-across-a-ball-and-an-egg]] · [[paced-ring-on-a-ball-and-a-plain]] · [[distant-ruler-in-three-spaces]] · [[hyperboloids-in-flat-spacetime]]

> On some surfaces, small rings drawn the same distance from their centres come out alike at every spot. A ball, flat ground, a paper tube, and a saddle-like surface called the hyperbolic plane are like this. These surfaces have constant curvature. On them, a small patch cut from one spot fits snugly at every other spot, turned by any amount about its own centre, if you bend it without stretching it. An egg is not like this.

## You will be able to

**Entry**
- Explain, with the ring test at many spots, why a ball, flat ground and a paper tube have constant curvature and an egg does not. `objectives/explain-constant-curvature-with-rings` ← `checks/ball-egg-and-tube`
- Predict whether a patch from one spot of a surface can fit snugly at another without stretching. `objectives/predict-where-a-patch-fits` ← `checks/patch-from-the-tip`
- Sort surfaces into the three kinds of constant curvature and pick out those whose curving varies. `objectives/name-the-three-kinds` ← `checks/which-surfaces-qualify`

**Working**
- Compute the Ricci tensor, Ricci scalar and cosmological constant of a constant-curvature space from K. `objectives/compute-ricci-from-k` ← `problems/de-sitter-radius-from-lambda`
- Use the ring function to recognize constant curvature in a metric whose components vary. `objectives/recognize-constant-curvature-in-a-metric` ← `checks/components-vary`
- Turn a measured curvature parameter into a curvature radius and a change in a distant ruler's angle. `objectives/estimate-curvature-from-a-ruler` ← `problems/curvature-bound-from-a-distant-ruler`

**Formal**
- Prove Schur's lemma and the bound of n(n+1)/2 Killing vectors. `objectives/prove-schur-and-killing-bound` ← `checks/schur-in-two-and-three`, `problems/killing-vector-count`
- Distinguish constant spacetime curvature from constant spatial curvature and from the Einstein condition. `objectives/distinguish-weaker-conditions` ← `checks/flat-slices-curved-spacetime`, `checks/einstein-space-not-enough`
- Predict the sign of free-fall deviation in de Sitter spacetime. `objectives/predict-deviation-in-de-sitter` ← `checks/falling-apart-in-de-sitter`

## Ways in

### 1. The same ring test at every spot · entry · operational

*How can an ant tell whether her world curves by the same amount at every spot?*

**Recap:** Walking without ever steering left or right is called walking straight. The ring test: walk straight out the same short distance from a centre in every direction, then measure the ring through the marks at the ends of the walks. On flat ground the ring is about 6.28 times the distance walked. On a ball it comes out short. A spot's matching ball is the ball whose small rings fall short by the same fraction as the spot's rings. To get the spot's Gaussian curvature, multiply the matching ball's radius by itself and divide 1 by the result.

Picture two ants. One lives on a smooth plastic egg, 6 centimetres long and 4 centimetres wide, with both ends the same shape. The other lives on a smooth plastic ball, 6 centimetres wide. Each ant runs the ring test at many spots, walking 2 millimetres out each time.

On the ball, every ring falls short by the same fraction, wherever the ant stands, because every spot of a ball is shaped like every other. So every spot has the same matching ball: the ball itself, with a radius of 3 centimetres. 3 times 3 is 9, so the Gaussian curvature is 1 ninth per square centimetre at every spot.

On the egg, rings at the pointed tips fall short by about five times as much as rings on the widest part. So the egg's matching balls change from spot to spot. A tip's matching ball has a radius of 1 and a third centimetres. 1 and a third times itself is 16 ninths, and 1 divided by 16 ninths is 9 sixteenths. So the Gaussian curvature at a tip is 9 sixteenths per square centimetre, against 1 ninth on the widest part.

A surface whose Gaussian curvature is the same at every spot is said to have constant curvature. The ball has it. The egg does not.

Flat ground counts too. Its small rings come out 6.28 times the distance walked at every spot, so its Gaussian curvature is zero everywhere. Zero at every spot is the same number at every spot. A rolled-up paper tube also counts. Rolling paper changes no length along the paper, so the tube's small rings match flat paper's at every spot.

Earth's ground is nearly, but not exactly, a ball, because Earth's spin squashes it slightly. Surveys show that its matching balls differ in radius by up to about 43 kilometres, out of about 6,400. A ring walked 1 kilometre out falls short by about 26 thousandths of a millimetre. Between the poles and the equator, that shortfall differs by only about a third of a thousandth of a millimetre. So nobody could notice the difference with rings drawn on a walk.

**Takeaway:** A surface has constant curvature when the ring test gives the same Gaussian curvature at every spot: a ball, flat ground and a paper tube do, and an egg does not.

*Builds on:* [[gaussian-curvature]]<br>*Visuals:* [[paced-ring-on-a-ball-and-a-plain]]<br>*See:* `checks/ball-egg-and-tube`, `observations/earth-matching-balls`

### 2. A patch that fits anywhere · entry · picture

*What can you do on a surface of constant curvature that you cannot do on an egg?*

**Recap:** Walking without ever steering left or right is called walking straight. The ring test: walk straight out the same short distance from a centre in every direction. Then measure the ring through the marks at the ends of the walks. A surface has constant curvature when the ring test gives the same answer at every spot, as on a ball. Take a plastic egg 6 centimetres long and 4 centimetres wide. Small rings at its tips fall short by about five times as much as on its widest part.

Cut a small round patch from an old ping-pong ball. Lay it on a second ping-pong ball, outer side out, at any spot. Spin it around its centre by any amount. It sits snugly every time, with no gap under it. In this note, "turned by any amount" always means spun like this, outer side out.

Now take the plastic egg, 6 centimetres long and 4 centimetres wide. Cut a patch from its pointed tip, and lay it on the egg's widest part. The patch rocks on its middle, and a gap opens under its rim. Could you bend the patch to fit, without stretching it?

Before cutting, run the ring test at the tip, and draw the ring on the shell. Bending without stretching changes no length along the patch. So the ring keeps its length, and every point of the ring stays the same distance from the patch's centre, measured along the patch. On the widest part, a ring drawn that distance from a centre falls short by only about a fifth as much, so it is longer than the patch's ring. The patch's ring is too short to lie there, and the patch cannot fit, however you bend it.

The same reasoning works on any surface. A patch carries its ring-test answer wherever it goes. So if a patch from any spot fits snugly at every other spot, the surface has constant curvature.

The surprise is that this also works the other way round. On a surface of constant curvature, a small enough patch cut from any spot fits at every other spot, turned by any amount, if you bend it without stretching. The mathematician Ferdinand Minding proved this in 1839.

Minding's result also covers two surfaces whose curvature is the same number everywhere. A paper tube's curvature is zero at every spot, like flat paper's. So a square cut from flat paper should fit the tube anywhere, turned by any amount.

This means that on a surface of constant curvature, an ant measuring lengths along the surface finds every spot like every other spot. She also finds every direction at a spot like every other direction.

**Try it:** Roll a sheet of paper into a tube and tape it. Cut a square about 3 centimetres wide from another sheet. Press the square against the outside of the tube, first with one edge along the tube, then turned an eighth of a turn. Both times it bends to lie snugly, with no creases. Then press the same square against a tennis ball. Whichever way you turn it, its edges crease or lift, because paper cannot stretch to follow a ball.

**Takeaway:** A small patch cut from a surface of constant curvature fits at every other spot, turned by any amount, if bent without stretching; on an egg it does not.

*What this leaves out:* "Small enough" means much smaller than the surface. A strip of paper longer than the way around a tube, for example, would overlap itself if you wrapped it around the tube.

*Continues:* `ways_in/same-ring-test-at-every-spot`<br>*Visuals:* [[slide-a-patch-across-a-ball-and-an-egg]]<br>*See:* `checks/patch-from-the-tip`

### 3. Shaped like a saddle everywhere · entry · contrast

*Can a surface curve like a saddle by the same amount at every spot?*

**Recap:** Walking without ever steering left or right is called walking straight. In the ring test you walk straight out the same short distance from a centre in every direction. Then you measure the ring through the ends of the walks. Gaussian curvature is positive where small rings come out too short, as on a ball. It is negative where they come out too long, as near the middle of a saddle. A surface has constant curvature when this number is the same at every spot.

A saddle-shaped potato crisp curves most strongly at its middle, where small rings come out too long. Toward its edges it curves more gently, and its rings come out closer to 6.28 times the distance walked. So a crisp does not have constant curvature.

Can a surface make small rings too long by the same fraction at every spot? Yes, and mathematicians of the 1800s worked out its geometry. Such a surface is called the hyperbolic plane.

Pick the hyperbolic plane that matches a ball 1 metre in radius, but the opposite way. Its small rings come out too long by the same fraction that the ball's small rings come out too short. 1 times 1 is 1, so its Gaussian curvature is minus 1 per square metre at every spot.

In that surface, bigger rings grow astonishingly fast. Here are rings walked out from one centre, with the lengths on flat ground in brackets:

- 1 metre out: 7.4 metres (6.3 metres)
- 2 metres out: 22.8 metres (12.6 metres)
- 3 metres out: 63 metres (18.8 metres)
- 4 metres out: 171 metres (25.1 metres)
- 5 metres out: 466 metres (31.4 metres)

Once you are a few metres out, each extra metre makes the ring about 2.7 times as long. You can check it: 63 times 2.7 is about 171, and 171 times 2.7 is about 466. The reason is that neighbouring walks from the centre spread apart, and the wider their gap, the faster it widens. So the gap keeps multiplying, like savings that earn interest on their interest.

People crochet close copies of small pieces of this surface. Each round of stitches is made a fixed number of times as long as the round before. The pieces ruffle like kale leaves. Each round is too long to lie on a table around the round before, so it waves above and below the table.

A Gaussian curvature can be positive, zero or negative. So surfaces of constant curvature come in three kinds: like a ball, like flat ground, and like the hyperbolic plane.

**Takeaway:** Surfaces of constant curvature come in three kinds: like a ball, like flat ground, and like the hyperbolic plane, where every small ring comes out too long by the same fraction.

*What this leaves out:* The crocheted pieces are only close copies of the hyperbolic plane, and each covers only a small part of it. The whole hyperbolic plane cannot be built as a smooth surface in ordinary space.

*Continues:* `ways_in/same-ring-test-at-every-spot`<br>*Visuals:* [[paced-ring-on-a-ball-and-a-plain]]<br>*See:* `checks/which-surfaces-qualify`

### 4. One number fills the whole curvature table · working · calculation

*What does constant curvature say about the Riemann tensor in any number of dimensions?*

The ball in "The same ring test at every spot" had one Gaussian curvature at every spot. In more dimensions a point offers many planes. For each nondegenerate plane spanned by $X$ and $Y$, meaning one whose area factor $g(X,X)g(Y,Y) - g(X,Y)^2$ does not vanish, the geodesics leaving the point within that plane sweep out a surface, and that surface's Gaussian curvature at the point is the sectional curvature

$$K(X,Y) = \frac{R_{\mu\nu\rho\sigma}X^\mu Y^\nu X^\rho Y^\sigma}{g(X,X)\,g(Y,Y) - g(X,Y)^2}.$$

A space of constant curvature has the same $K(X,Y) = K$ for every plane at every point. A tensor with the symmetries of the Riemann tensor is fixed by its sectional curvatures, an algebraic fact taken here on trust, so this happens exactly when

$$R_{\rho\sigma\mu\nu} = K\,(g_{\rho\mu}g_{\sigma\nu} - g_{\rho\nu}g_{\sigma\mu}).$$

Inserting $X, Y, X, Y$ on the right returns $K$ times the denominator, as it must. A sphere of radius $a$ has $K = +1/a^2$.

Contracting once and then again (derivation "Contract the constant-curvature tensor") gives, in $n$ dimensions,

$$R_{\sigma\nu} = (n-1)K\,g_{\sigma\nu}, \qquad R = n(n-1)K.$$

A surface has $R = 2K$. A three-dimensional space has $R_{ij} = 2Kg_{ij}$ and $R = 6K$. A four-dimensional spacetime has $R_{\mu\nu} = 3Kg_{\mu\nu}$, $R = 12K$ and Einstein tensor $G_{\mu\nu} = -3Kg_{\mu\nu}$. Taking the course Einstein equation $G_{\mu\nu} + \Lambda g_{\mu\nu} = 8\pi G T_{\mu\nu}/c^4$ on trust, such a spacetime solves it with $T_{\mu\nu} = 0$ and $\Lambda = 3K$: empty space with a cosmological constant.

Constant curvature does not mean constant metric components. On the unit sphere, $d\theta^2 + \sin^2\theta\,d\phi^2$, the component $g_{\phi\phi}$ changes from place to place, yet $K = 1$ everywhere.

**Takeaway:** Constant curvature fixes the whole Riemann tensor as K times a combination of metrics, so the Ricci tensor is (n minus 1) K times the metric and, in four dimensions, the cosmological constant is 3K.

*Continues:* `ways_in/same-ring-test-at-every-spot`<br>*Builds on:* [[riemann-curvature-tensor]], [[ricci-scalar]]<br>*See:* `derivations/contract-the-constant-curvature-tensor`, `problems/de-sitter-radius-from-lambda`

### 5. Rings and triangles in closed form · working · calculation

*What exact lengths, areas and angles does constant curvature give?*

The fast-growing rings of the hyperbolic plane in "Shaped like a saddle everywhere" follow from one function. Around any point of a surface, geodesic polar coordinates give $ds^2 = d\rho^2 + f(\rho)^2\,d\phi^2$, with $\rho$ the distance walked along a geodesic, so a ring at distance $\rho$ has circumference $2\pi f(\rho)$. The Gaussian curvature is then $K = -f''/f$, a standard result taken here on trust. For constant $K$ with a smooth centre, the worked example "Rings from the distance rule" finds the ring function

$$\mathrm{sn}_K(\rho) = \frac{\sin\sqrt{K}\rho}{\sqrt K}\ (K>0), \qquad \rho\ (K=0), \qquad \frac{\sinh\sqrt{-K}\rho}{\sqrt{-K}}\ (K<0).$$

A ring at distance $\rho$ has circumference $2\pi\,\mathrm{sn}_K(\rho) = 2\pi\rho\,(1 - K\rho^2/6 + \dots)$, and the disc of geodesic radius $\rho$ around the centre has area $4\pi\,\mathrm{sn}_K(\rho/2)^2$. With $K = -1$ m$^{-2}$, the ring at $\rho = 5$ m is $2\pi\sinh 5 = 466$ m long.

A geodesic triangle of area $A$ has angle sum $\pi + KA$ at every size, by the local Gauss–Bonnet theorem, taken here on trust. On the hyperbolic plane the angles fall short of $\pi$, so no triangle's area reaches $\pi/|K|$.

In $n$ dimensions, stated here without proof, the metric of a constant-curvature space around any point is $d\rho^2 + \mathrm{sn}_K(\rho)^2\,d\Omega^2_{n-1}$, out to where geodesics from the centre first meet again ($\rho = \pi/\sqrt K$ for $K > 0$). Setting $r = \mathrm{sn}_K(\rho)$ gives

$$ds^2 = \frac{dr^2}{1 - Kr^2} + r^2\,d\Omega^2_{n-1},$$

which for $n = 3$ is the bracketed spatial metric of the Robertson–Walker form, with $k$ in place of $K$. For $K > 0$ the radius $r$ covers only half of the sphere, up to $\rho = \pi/2\sqrt K$.

**Takeaway:** Constant curvature gives rings of length 2 pi times the ring function, triangle angle sums of pi plus K times the area, and a metric around any point fixed by K alone.

*Continues:* `ways_in/saddle-shaped-everywhere`, `ways_in/one-number-fills-the-table`<br>*Builds on:* [[gaussian-curvature]]<br>*Visuals:* [[paced-ring-on-a-ball-and-a-plain]]<br>*See:* `worked_examples/rings-from-the-distance-rule`, `checks/components-vary`

### 6. A distant ruler weighs space · working · operational

*How can astronomers measure the curvature of space itself?*

The ring function of "Rings and triangles in closed form" also sets how large a distant object looks. In a three-dimensional space of constant curvature, the sphere at distance $D$ from an observer has area $4\pi\,\mathrm{sn}_K(D)^2$. So a ruler of length $L \ll D$ held across the line of sight subtends

$$\theta = \frac{L}{\mathrm{sn}_K(D)}.$$

Positive curvature makes the ruler look larger than in flat space, and negative curvature makes it look smaller, by a fraction of about $KD^2/6$. So the ruler must be very far away.

Cosmology supplies one. If the universe is homogeneous and isotropic, space at each cosmic time is a space of constant curvature, $K = k/a(t)^2$ in the Robertson–Walker metric. Sound waves in the early plasma left a preferred spacing, seen in the microwave background and in galaxy clustering. At the release of the microwave background that spacing is about 144 megaparsecs in today's units (1 Mpc $= 3.086\times10^{22}$ m); the slightly later epoch that galaxy clustering records gives about 147 megaparsecs. In conformal time $\eta$, with $c\,d\eta = c\,dt/a$, the metric is $a^2$ times a static metric. An overall factor like this changes neither the paths of light rays nor angles at the observer, so the formula holds with $L$, $D$ and $K$ all taken on today's slice.

The microwave background shows this ruler at about 13,900 Mpc, with its angle measured to 0.03 per cent. Alone, that angle cannot separate curvature from other unknowns of the expansion history. Combined with galaxy clustering it gives $\Omega_K = -Kc^2/H_0^2 = 0.001 \pm 0.002$, consistent with flat space. In this definition a positive $\Omega_K$ means negative curvature.

**Takeaway:** A distant ruler looks larger in positively curved space and smaller in negatively curved space; the sound-wave ruler of the early universe finds space consistent with flat.

*What this leaves out:* Treats the ruler as small and the universe as exactly homogeneous and isotropic; the quoted $\Omega_K$ assumes the standard expansion model.

*Continues:* `ways_in/rings-and-triangles-in-closed-form`<br>*Visuals:* [[distant-ruler-in-three-spaces]]<br>*See:* `observations/spatial-curvature-from-planck-and-bao`, `problems/curvature-bound-from-a-distant-ruler`

### 7. Isotropy forces constancy · formal · structure

*Why does curvature that looks the same in every direction have to be the same everywhere, and what does it determine?*

The tensor form of "One number fills the whole curvature table" follows from symmetry, and it pins down the local geometry. Let $(M,g)$ be a connected pseudo-Riemannian manifold of dimension $n \ge 2$, with $G = c = 1$.

*Pointwise isotropy.* If at $p$ every nondegenerate 2-plane has the same sectional curvature $K(p)$, then $R_{\rho\sigma\mu\nu} = K(p)(g_{\rho\mu}g_{\sigma\nu} - g_{\rho\nu}g_{\sigma\mu})$ at $p$. In Riemannian signature this holds whenever the isometries fixing $p$ act transitively on its 2-planes.

*Schur's lemma.* If the form holds at every point and $n \ge 3$, then $K$ is constant. Contracting gives $R_{\mu\nu} = (n-1)Kg_{\mu\nu}$ and $R = n(n-1)K$ with $K$ a function, and the contracted Bianchi identity $\nabla^\mu R_{\mu\nu} = \tfrac12\nabla_\nu R$ becomes $(n-1)\nabla_\nu K = \tfrac12 n(n-1)\nabla_\nu K$, that is $(n-1)(n-2)\nabla_\nu K = 0$. For $n = 2$ the factor vanishes: a surface has one plane at each point, so the form holds everywhere, and an egg's $K$ can vary.

*Maximal symmetry.* A Killing vector obeys $\nabla_\mu\nabla_\nu\xi_\rho = R_{\sigma\mu\nu\rho}\xi^\sigma$, so it is fixed by $\xi_p$ and the 2-form $(\nabla_\mu\xi_\nu)_p$, giving at most $n(n+1)/2$ independent Killing fields. The integrability conditions of this system leave all that data free exactly when the curvature is constant, so constant curvature is equivalent to local maximal symmetry.

*Local uniqueness.* In Riemannian signature, Jacobi fields along unit-speed geodesics from $p$ obey $J'' + KJ = 0$, so $J = \mathrm{sn}_K(\rho)E$ with $E$ parallel, and the metric in normal coordinates is forced to be $d\rho^2 + \mathrm{sn}_K(\rho)^2 d\Omega^2_{n-1}$. Two spaces of equal $n$ and $K$ are therefore locally isometric, taking any point and orthonormal frame to any other (Minding for surfaces).

*Global limits.* The complete simply connected models are the sphere of radius $1/\sqrt K$, Euclidean space, and hyperbolic space, the sheet $T > 0$ of $-T^2 + |X|^2 = -1/|K|$ in Minkowski space. Every other complete connected Riemannian example is a quotient of one by a discrete group acting freely (Killing–Hopf theorem): a flat torus, real projective space, a compact hyperbolic manifold. Quotients keep the local geometry but lose global Killing fields; a flat $n$-torus has only $n$. By Hilbert's theorem, no complete surface of constant negative curvature is isometrically immersed in $\mathbb{R}^3$.

**Takeaway:** Pointwise isotropic curvature is constant in three or more dimensions, constant curvature is local maximal symmetry, and K together with dimension and signature fixes the geometry locally but not globally.

*Continues:* `ways_in/one-number-fills-the-table`<br>*Builds on:* [[contracted-bianchi-identity]], [[killing-vector]]<br>*See:* `problems/killing-vector-count`

### 8. Spacetimes of one curvature number · formal · contrast

*What are the Lorentzian spaces of constant curvature, and which weaker conditions are easily mistaken for them?*

The Riemannian models of "Isotropy forces constancy" have Lorentzian twins. With $G = c = 1$, de Sitter spacetime is the hyperboloid $-T^2 + X_1^2 + \dots + X_n^2 = \alpha^2$ in $\mathbb{R}^{1,n}$, with $K = +1/\alpha^2$. Anti-de Sitter is $-T^2 - U^2 + X_1^2 + \dots + X_{n-1}^2 = -\alpha^2$ in $\mathbb{R}^{2,n-1}$, with $K = -1/\alpha^2$; its closed timelike curves disappear in the universal cover. Their isometry groups $O(1,n)$ and $O(2,n-1)$ have dimension $n(n+1)/2$, like the Poincaré group. In four dimensions $\Lambda = 3K$.

*Sign.* For unit timelike $u$ and $\xi \perp u$, the course deviation equation gives $D^2\xi^\mu/d\tau^2 = +K\xi^\mu$ (check "Falling apart in de Sitter"). Free-fall neighbours in de Sitter separate, with e-folding time $\alpha$ at late times; in anti-de Sitter they oscillate and refocus. Spacelike geodesics in de Sitter whose separation lies in a spacelike plane converge, as on a sphere, because that plane has a positive area factor; the sign flips for free-fall neighbours because a timelike plane has a negative one.

*Constant spatial curvature.* A Robertson–Walker spacetime has slices of constant curvature $k/a(t)^2$, yet it has constant spacetime curvature only when empty apart from a cosmological constant: de Sitter, anti-de Sitter, Minkowski or the Milne universe. The flat-sliced Einstein–de Sitter universe is a curved spacetime that is not of constant curvature, while de Sitter admits slicings with $k = +1$, $0$ and $-1$.

*Einstein spaces.* $R_{\mu\nu} = \lambda g_{\mu\nu}$ constrains only the traces. For $n \ge 3$, constant curvature is exactly an Einstein space with vanishing Weyl tensor; in three dimensions the two coincide, but Ricci-flat Schwarzschild has Kretschmann scalar $48M^2/r^6$.

**Takeaway:** De Sitter and anti-de Sitter are the curved Lorentzian spaces of constant curvature, positive K pushes free-fall neighbours apart, and neither curved slices nor an Einstein condition is enough for constant curvature.

*Continues:* `ways_in/isotropy-forces-constancy`<br>*Visuals:* [[hyperboloids-in-flat-spacetime]]<br>*See:* `checks/falling-apart-in-de-sitter`, `checks/flat-slices-curved-spacetime`, `checks/einstein-space-not-enough`

## Glossary

| Term | Say | In plain words | Concept |
| --- | --- | --- | --- |
| walk straight | — | To walk without ever steering left or right, even where the path bends over a curved surface. | [[geodesic]] |
| ring test | — | Walk straight out the same short distance from a centre in every direction, and measure the ring through the marks at the ends of the walks. On flat ground it is about 6.28 times the distance. | [[circumference-to-radius-test]] |
| matching ball | — | For a spot where small rings come out short, the ball whose rings, drawn the same short distance from their centres, fall short by the same fraction. | — |
| Gaussian curvature | GOW-see-un | A number for each spot of a surface. Where small rings come out short, multiply the matching ball's radius by itself and divide 1 by the result. It is zero where small rings come out as on flat ground. Where they come out too long, find the ball whose small rings fall short by that same fraction. Work out that ball's number the same way, and put a minus sign in front. | [[gaussian-curvature]] |
| constant curvature | — | Having the same Gaussian curvature at every spot. A ball, flat ground, a paper tube and the hyperbolic plane have it; an egg does not. | [[space-of-constant-curvature]] |
| hyperbolic plane | hy-per-BOL-ik | A surface curved like a saddle by the same amount at every spot, where every small ring comes out too long by the same fraction. Small pieces of it can be crocheted. | [[hyperbolic-plane]] |

## Key equations

### Riemann tensor of constant curvature · working

$$
R_{\rho\sigma\mu\nu} = K\,(g_{\rho\mu}g_{\sigma\nu} - g_{\rho\nu}g_{\sigma\mu})
$$

One number $K$, the same at every point, fixes every component of the curvature through the metric.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $R_{\rho\sigma\mu\nu}$ | Riemann tensor with all indices lowered, course convention | the Riemann tensor |
| $K$ | the constant sectional curvature, in inverse length squared | K |
| $g_{\mu\nu}$ | the metric | the metric |

**Holds when:** Defines constant curvature; any dimension $n \ge 2$ and signature. A sphere of radius $a$ has $K = 1/a^2$.  
**Say it:** “The Riemann tensor equals K times the metric times the metric, minus the same with the last two indices swapped.”  
**Justified by:** `stated`

### Ricci tensor and scalar of constant curvature · working

$$
R_{\mu\nu} = (n-1)K\,g_{\mu\nu}, \qquad R = n(n-1)K
$$

The traces of the constant-curvature Riemann tensor are proportional to the metric.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $n$ | dimension of the space | n |
| $R_{\mu\nu}$ | Ricci tensor | the Ricci tensor |
| $R$ | Ricci scalar | the Ricci scalar |

**Holds when:** Space of constant curvature $K$ in $n$ dimensions; $R_{\mu\nu} = R^\rho{}_{\mu\rho\nu}$ as in the course conventions.  
**Say it:** “The Ricci tensor is n minus one times K times the metric, and the Ricci scalar is n times n minus one times K.”  
**Justified by:** `derivations/contract-the-constant-curvature-tensor`

### Constant curvature as a vacuum with a cosmological constant · working

$$
G_{\mu\nu} = -3K\,g_{\mu\nu}, \qquad \Lambda = 3K
$$

A four-dimensional spacetime of constant curvature solves the Einstein equation with no matter and cosmological constant $3K$.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $G_{\mu\nu}$ | Einstein tensor | the Einstein tensor |
| $\Lambda$ | cosmological constant, in inverse length squared | lambda |

**Holds when:** Four dimensions, signature $(-,+,+,+)$, course Einstein equation $G_{\mu\nu} + \Lambda g_{\mu\nu} = 8\pi G T_{\mu\nu}/c^4$ with $T_{\mu\nu} = 0$.  
**Say it:** “The Einstein tensor is minus three K times the metric, so the cosmological constant is three K.”  
**Justified by:** `derivations/contract-the-constant-curvature-tensor`

### Metric around any point · working

$$
ds^2 = d\rho^2 + \mathrm{sn}_K(\rho)^2\,d\Omega^2_{n-1} = \frac{dr^2}{1 - Kr^2} + r^2\,d\Omega^2_{n-1}
$$

Around every point, the metric of a Riemannian constant-curvature space depends only on $K$.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $\rho$ | geodesic distance from the centre | rho, the distance walked |
| $\mathrm{sn}_K(\rho)$ | $\sin(\sqrt K\rho)/\sqrt K$, $\rho$, or $\sinh(\sqrt{-K}\rho)/\sqrt{-K}$ for positive, zero or negative $K$ | the ring function of rho |
| $r$ | $\mathrm{sn}_K(\rho)$, the radius read off from ring circumferences | r |
| $d\Omega^2_{n-1}$ | metric of the unit sphere of dimension $n-1$ ($d\phi^2$ for a surface) | the unit sphere's metric |

**Holds when:** Riemannian signature. The first form holds out to where geodesics from the centre first meet; the second only where $\mathrm{sn}_K' > 0$. Derived for surfaces in the worked example; stated for $n > 2$.  
**Say it:** “The metric is d rho squared plus the ring function squared times the unit sphere, or d r squared over one minus K r squared plus r squared times the unit sphere.”  
**Justified by:** `stated`

### Angle sum of a geodesic triangle · working

$$
\alpha_1 + \alpha_2 + \alpha_3 = \pi + KA
$$

Positive curvature makes a triangle's angles overshoot a straight angle, negative curvature makes them fall short, in proportion to the area.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $\alpha_1, \alpha_2, \alpha_3$ | interior angles, in radians | the three angles |
| $A$ | area of the triangle | the area |

**Holds when:** Surface of constant curvature $K$; sides are geodesics bounding a smooth region of area $A$, with no holes or cone points.  
**Say it:** “The three angles add up to pi plus K times the area.”  
**Justified by:** `stated`

### Angle of a distant ruler · working

$$
\theta = \frac{L}{\mathrm{sn}_K(D)}
$$

A small ruler across the line of sight looks larger in positively curved space and smaller in negatively curved space than in flat space.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $\theta$ | angle subtended, in radians | theta |
| $L$ | length of the ruler | L |
| $D$ | geodesic distance to the ruler | D |

**Holds when:** Static three-dimensional space of constant curvature, or today's slice of a Robertson–Walker universe with $L$, $D$ and $K$ scaled to today; $L \ll D$ and, for $K > 0$, $D < \pi/\sqrt K$.  
**Say it:** “The angle is the length of the ruler divided by the ring function of the distance.”  
**Justified by:** `stated`

### Second derivative of a Killing vector · formal

$$
\nabla_\mu\nabla_\nu\xi_\rho = R_{\sigma\mu\nu\rho}\,\xi^\sigma
$$

A Killing field is determined everywhere by its value and its first derivative at one point, which bounds the number of symmetries.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $\xi_\rho$ | a Killing vector field, $\nabla_\mu\xi_\nu + \nabla_\nu\xi_\mu = 0$ | the Killing vector |

**Holds when:** Levi-Civita connection, course Riemann tensor; proved in problem "Counting Killing vectors".  
**Say it:** “Two derivatives of a Killing vector equal the Riemann tensor acting on the Killing vector.”  
**Justified by:** `stated`

## Derivations

### Contract the constant-curvature tensor · working

**Goal:** Find the Ricci tensor, Ricci scalar and Einstein tensor of an $n$-dimensional space of constant curvature $K$.

1. Start from $R_{\rho\sigma\mu\nu} = K(g_{\rho\mu}g_{\sigma\nu} - g_{\rho\nu}g_{\sigma\mu})$ and raise the first index with $g^{\lambda\rho}$: $R^\lambda{}_{\sigma\mu\nu} = K(\delta^\lambda_\mu g_{\sigma\nu} - \delta^\lambda_\nu g_{\sigma\mu})$.
2. Contract $\lambda$ with $\mu$, as $R_{\sigma\nu} = R^\lambda{}_{\sigma\lambda\nu}$ requires. The first term gives $\delta^\lambda_\lambda g_{\sigma\nu} = n\,g_{\sigma\nu}$.
3. The second term gives $\delta^\lambda_\nu g_{\sigma\lambda} = g_{\sigma\nu}$, so $R_{\sigma\nu} = K(n-1)g_{\sigma\nu}$.
4. Trace with $g^{\sigma\nu}$, using $g^{\sigma\nu}g_{\sigma\nu} = n$: $R = n(n-1)K$.
5. Form $G_{\mu\nu} = R_{\mu\nu} - \tfrac12Rg_{\mu\nu} = \big[(n-1) - \tfrac12 n(n-1)\big]Kg_{\mu\nu} = -\tfrac12(n-1)(n-2)Kg_{\mu\nu}$.
6. For $n = 4$ this is $G_{\mu\nu} = -3Kg_{\mu\nu}$. In the course Einstein equation with $T_{\mu\nu} = 0$, $-3Kg_{\mu\nu} + \Lambda g_{\mu\nu} = 0$, so $\Lambda = 3K$. For $n = 2$ the Einstein tensor vanishes identically.

**Result:** $R_{\mu\nu} = (n-1)Kg_{\mu\nu}$, $R = n(n-1)K$, $G_{\mu\nu} = -\tfrac12(n-1)(n-2)Kg_{\mu\nu}$; in four dimensions $\Lambda = 3K$.

## Worked examples

### Rings from the distance rule · working

**Problem:** For $ds^2 = d\rho^2 + f(\rho)^2d\phi^2$ the Gaussian curvature is $K = -f''/f$. Find $f$ when $K$ is constant and the centre is smooth, show that $r = f(\rho)$ gives $dr^2/(1 - Kr^2) + r^2d\phi^2$, and find how much a ring of geodesic radius 1000 km on a sphere of radius 6371 km falls short of $2\pi\rho$.

1. Constant $K$ turns $K = -f''/f$ into $f'' + Kf = 0$, a linear equation with constant coefficients.
2. A smooth centre needs small rings of length $2\pi\rho$, so $f(0) = 0$ and $f'(0) = 1$.
3. The solution is $\sin(\sqrt K\rho)/\sqrt K$ for $K > 0$, $\rho$ for $K = 0$, and $\sinh(\sqrt{-K}\rho)/\sqrt{-K}$ for $K < 0$: the ring function $\mathrm{sn}_K(\rho)$.
4. In each case $f'^2 + Kf^2 = 1$: $\cos^2 + \sin^2 = 1$, $1 + 0 = 1$, or $\cosh^2 - \sinh^2 = 1$.
5. With $r = f(\rho)$, $dr = f'\,d\rho$, so $d\rho^2 = dr^2/f'^2 = dr^2/(1 - Kr^2)$ wherever $f' > 0$.
6. On the sphere, $\sqrt K\rho = 1000/6371 = 0.15696$, so $C = 2\pi(6371\ \text{km})\sin 0.15696 = 6257.4$ km, while $2\pi\rho = 6283.2$ km.

**Answer:** $f = \mathrm{sn}_K(\rho)$; the ring is $6257.4$ km long, $25.8$ km or $0.410$ per cent short, matching $K\rho^2/6 = 0.411$ per cent to leading order.

**Takeaway:** One ordinary differential equation gives the rings of all three kinds of constant-curvature surface, and the substitution $r = \mathrm{sn}_K(\rho)$ produces the Robertson–Walker radial form.

## Problems

### `de-sitter-radius-from-lambda` · working · difficulty 1 · calculation

Take the measured cosmological constant as $\Lambda = 1.1\times10^{-52}$ m$^{-2}$. A universe containing nothing but this cosmological constant is de Sitter spacetime, a space of constant curvature. Find its curvature $K$, its Ricci scalar $R$, and its radius $\alpha = 1/\sqrt K$ in metres and in light-years ($1$ ly $= 9.461\times10^{15}$ m).

**Hints**

1. In four dimensions $\Lambda = 3K$ and $R = 12K$.

**Answer:** $K = 3.67\times10^{-53}$ m$^{-2}$, $R = 4.4\times10^{-52}$ m$^{-2}$, and $\alpha = 1.65\times10^{26}$ m, about $17.5$ billion light-years.

**Must contain:** K is one third of lambda; R is twelve K, four lambda; The radius is about 17.5 billion light-years

**Numeric:** curvature K = 3.67e-53 m^-2 (signed, ±3%); radius alpha = 1.745e+10 ly (magnitude, ±3%)

**Solution**

1. From $\Lambda = 3K$: $K = 1.1\times10^{-52}/3 = 3.67\times10^{-53}$ m$^{-2}$, positive as de Sitter requires.
2. $R = 12K = 4\Lambda = 4.4\times10^{-52}$ m$^{-2}$.
3. $\alpha = 1/\sqrt{3.67\times10^{-53}\ \text{m}^{-2}} = 1.65\times10^{26}$ m.
4. $1.65\times10^{26}/9.461\times10^{15} = 1.75\times10^{10}$ ly, about 17.5 billion light-years.

### `curvature-bound-from-a-distant-ruler` · working · difficulty 2 · estimate

Measurements give $\Omega_K = 0.001 \pm 0.002$, where today's spatial curvature is $K_0 = -\Omega_K H_0^2/c^2$ and $H_0 = 67.4$ km s$^{-1}$ Mpc$^{-1}$. (a) Treating the error as Gaussian and taking two standard deviations, how large must the curvature radius $1/\sqrt{|K_0|}$ be, in Mpc? (b) At the most negative allowed curvature, by what fraction does a ruler at $D = 13{,}900$ Mpc look smaller than in flat space?

**Hints**

1. The two-standard-deviation range is $-0.003$ to $0.005$; the largest magnitude sets the smallest radius.
2. $c/H_0 = 4448$ Mpc, and for small $|K|D^2$ the angle changes by a fraction of about $KD^2/6$.

**Answer:** (a) At least about 63,000 Mpc, some four and a half times the distance to the last-scattering surface. (b) About 0.8 per cent smaller.

**Must contain:** The largest allowed magnitude of omega K is 0.005; Curvature radius is c over H nought divided by the square root of 0.005, about 63 thousand megaparsecs; Negative curvature shrinks the angle by about 0.8 per cent at that bound

**Numeric:** minimum curvature radius = 62900 Mpc (magnitude, ±3%); fractional decrease of the angle = 0.81 percent (magnitude, ±0.1)

**Solution**

1. Two standard deviations give $-0.003 \le \Omega_K \le 0.005$, so $|\Omega_K| \le 0.005$ and $|K_0| \le 0.005\,H_0^2/c^2$.
2. $c/H_0 = 299{,}792$ km s$^{-1}$ $/\ 67.4$ km s$^{-1}$ Mpc$^{-1} = 4448$ Mpc.
3. $1/\sqrt{|K_0|} \ge 4448/\sqrt{0.005}$ Mpc $= 62{,}900$ Mpc.
4. The most negative curvature is $\Omega_K = 0.005$, so $|K_0|D^2 = 0.005\times(13{,}900/4448)^2 = 0.049$.
5. $\mathrm{sn}_K(D)/D = \sinh(x)/x$ with $x = \sqrt{0.049} = 0.221$, which is $1.0082$; so $\theta$ is smaller by a factor $1/1.0082$, about 0.8 per cent, matching $|K_0|D^2/6 = 0.0081$.

### `killing-vector-count` · formal · difficulty 3 · proof

On a connected manifold of dimension $n$ with its Levi-Civita connection and the course Riemann tensor, let $\xi$ satisfy Killing's equation $\nabla_\mu\xi_\nu + \nabla_\nu\xi_\mu = 0$. (a) Show that $\nabla_\mu\nabla_\nu\xi_\rho = R_{\sigma\mu\nu\rho}\xi^\sigma$. (b) Deduce that there are at most $n(n+1)/2$ linearly independent Killing vectors. (c) Show that Euclidean space attains the bound.

**Hints**

1. For a covector, the Ricci identity reads $[\nabla_\mu, \nabla_\nu]\omega_\rho = R_{\rho\sigma\mu\nu}\omega^\sigma$.
2. Write $T_{\mu\nu\rho} = \nabla_\mu\nabla_\nu\xi_\rho$, antisymmetric in its last two indices, and add cyclic permutations of the Ricci identity.
3. Along a curve, treat $\xi_\rho$ and $\nabla_\nu\xi_\rho$ together as the unknowns of a first-order linear system.

**Answer:** (a) The Ricci identity, Killing's equation and the cyclic identity give $\nabla_\mu\nabla_\nu\xi_\rho = R_{\sigma\mu\nu\rho}\xi^\sigma$. (b) A Killing field is fixed by $\xi_p$ and the antisymmetric $(\nabla\xi)_p$, which is $n + n(n-1)/2 = n(n+1)/2$ numbers. (c) The $n$ translations and $n(n-1)/2$ rotations.

**Must contain:** Ricci identity combined with Killing antisymmetry and the cyclic identity; A Killing field is determined by its value and derivative at one point; Initial data have dimension n plus n times n minus one over two; Translations and rotations of Euclidean space attain the bound

**Solution**

1. For the covector $\xi_\rho$, $T_{\mu\nu\rho} - T_{\nu\mu\rho} = -R^\sigma{}_{\rho\mu\nu}\xi_\sigma = R_{\rho\sigma\mu\nu}\xi^\sigma$. Killing's equation makes $T_{\nu\mu\rho} = -T_{\nu\rho\mu}$, so $T_{\mu\nu\rho} + T_{\nu\rho\mu} = R_{\rho\sigma\mu\nu}\xi^\sigma$.
2. Permuting cyclically, $T_{\nu\rho\mu} + T_{\rho\mu\nu} = R_{\mu\sigma\nu\rho}\xi^\sigma$ and $T_{\rho\mu\nu} + T_{\mu\nu\rho} = R_{\nu\sigma\rho\mu}\xi^\sigma$.
3. Adding the first and third and subtracting the second: $2T_{\mu\nu\rho} = (R_{\rho\sigma\mu\nu} - R_{\mu\sigma\nu\rho} + R_{\nu\sigma\rho\mu})\xi^\sigma$.
4. First-pair antisymmetry turns the bracket into $-R_{\sigma\rho\mu\nu} + R_{\sigma\mu\nu\rho} - R_{\sigma\nu\rho\mu}$. The cyclic identity $R_{\sigma\rho\mu\nu} + R_{\sigma\mu\nu\rho} + R_{\sigma\nu\rho\mu} = 0$ makes this $2R_{\sigma\mu\nu\rho}$, proving (a). Check on the unit sphere with $\xi = \partial_\phi$: $\nabla_\theta\nabla_\theta\xi_\phi = -\sin^2\theta = R_{\phi\theta\theta\phi}\xi^\phi$.
5. (b) Along a curve $x(s)$ from $p$, set $F_{\nu\rho} = \nabla_\nu\xi_\rho$. Then $D\xi_\rho/ds = \dot x^\nu F_{\nu\rho}$ and $DF_{\nu\rho}/ds = \dot x^\mu R_{\sigma\mu\nu\rho}\xi^\sigma$, a linear first-order system whose solution is fixed by $(\xi_p, F_p)$.
6. Every point of a connected manifold is joined to $p$ by a curve, so the linear map $\xi \mapsto (\xi_p, F_p)$ is injective. Its target has dimension $n + n(n-1)/2 = n(n+1)/2$, because $F_p$ is antisymmetric.
7. (c) In Cartesian coordinates the $n$ fields $\partial_i$ and the $n(n-1)/2$ fields $x^i\partial_j - x^j\partial_i$ ($i < j$) satisfy Killing's equation, and their values and derivatives at the origin are independent, so the bound is attained.

## Observations

- **Earth's Gaussian curvature varies over its surface** (measured, working). Earth's spin flattens it, so its ground is close to, but not exactly, a surface of constant curvature. Geodetic surveys give the principal radii of curvature at each latitude, and their product gives $K = 1/MN$. The variation is small enough that a sphere of radius 6371 km serves most estimates. *Numbers:* GRS80 ellipsoid: $K = 2.475\times10^{-14}$ m$^{-2}$ at the equator, matching radius 6356.8 km, and $2.442\times10^{-14}$ m$^{-2}$ at the poles, matching radius 6399.6 km: 1.35 per cent apart. *Reference:* Helmut Moritz (1980), *Geodetic Reference System 1980*, Bulletin Géodésique 54, 395–405, doi:10.1007/BF02521480
- **The spatial curvature of the universe, from the cosmic microwave background combined with baryon acoustic oscillations in galaxy clustering** (measured, working). In a homogeneous, isotropic universe each spatial slice is a space of constant curvature, so the angle of the sound-horizon ruler measures $\mathrm{sn}_K$ at the distance of the last-scattering surface. Galaxy clustering at lower redshift breaks the degeneracy between curvature and the expansion history. The result is consistent with flat slices. *Numbers:* $\Omega_K = 0.001 \pm 0.002$ (68 per cent), with $\Omega_K = -K_0c^2/H_0^2$ positive for negative curvature. Taking two standard deviations and $H_0 = 67.4$ km s$^{-1}$ Mpc$^{-1}$, the curvature radius exceeds about $63{,}000$ Mpc, against about $13{,}900$ Mpc to the last-scattering surface. *Reference:* N. Aghanim, Y. Akrami, M. Ashdown, J. Aumont and others (2020), *Planck 2018 results. VI. Cosmological parameters*, Astronomy & Astrophysics 641, A6, doi:10.1051/0004-6361/201833910

## Teaching arc

1. **Ask the ant's question** (entry). Ask how an ant could check whether her world curves the same everywhere, then compare the ball, the egg and the tube. *Why:* It defines constant curvature by a measurement, and the tube shows that zero counts. *Predict:* If the ant on the paper tube runs the ring test at many spots, will her answers all agree? *Visual:* [[paced-ring-on-a-ball-and-a-plain]] *Uses:* `ways_in/same-ring-test-at-every-spot`, `checks/ball-egg-and-tube`
2. **Move a patch** (entry). Slide a patch across the ball and the egg, and let the learner use the ring on the patch to explain the egg. *Why:* It turns the definition into symmetry, which cosmology uses. *Predict:* Will a patch cut from the egg's pointed tip sit snugly on its widest part if you bend it without stretching? *Visual:* [[slide-a-patch-across-a-ball-and-an-egg]] *Uses:* `ways_in/a-patch-that-fits-anywhere`, `checks/patch-from-the-tip`
3. **Meet the third kind** (entry). Contrast the crisp with the hyperbolic plane and its fast-growing rings. *Why:* Few learners expect a saddle-like world that is the same everywhere. *Predict:* In a world curved like a saddle by the same amount everywhere, is a ring walked 5 metres out longer or shorter than 31 metres? *Uses:* `ways_in/saddle-shaped-everywhere`, `checks/which-surfaces-qualify`
4. **Fill the curvature table with one number** (working). Write the tensor form, contract it, and reach the cosmological constant. *Why:* It links constant curvature to Ricci curvature and empty space with a cosmological constant. *Uses:* `ways_in/one-number-fills-the-table`, `derivations/contract-the-constant-curvature-tensor`, `problems/de-sitter-radius-from-lambda`
5. **Weigh space with a ruler** (working). Derive the ring function, then read the measured curvature bound through the distant-ruler angle. *Why:* It ties the geometry to a measurement of our universe. *Predict:* In a positively curved space, does a distant ruler look bigger or smaller than in flat space? *Visual:* [[distant-ruler-in-three-spaces]] *Uses:* `ways_in/rings-and-triangles-in-closed-form`, `ways_in/a-distant-ruler-weighs-space`, `problems/curvature-bound-from-a-distant-ruler`
6. **Mark the limits** (formal). Prove Schur's lemma, separate constant curvature from curved slices and Einstein spaces, and fix the de Sitter sign. *Why:* These confusions follow students into cosmology. *Predict:* De Sitter has positive curvature like a sphere. Do free-fall neighbours there draw together? *Visual:* [[hyperboloids-in-flat-spacetime]] *Uses:* `ways_in/isotropy-forces-constancy`, `ways_in/spacetimes-of-one-curvature-number`, `checks/falling-apart-in-de-sitter`, `checks/schur-in-two-and-three`

## Misconceptions

### “A tube bends around but not along, so its curving cannot be the same everywhere.” · entry · `tube-bends-so-not-constant`

- **Why it is tempting:** From outside, the tube's bends differ with direction.
- **What is true:** Bends that change no length along the surface do not affect the ring test. A tube's small rings match flat paper's everywhere.
- **Exposed by:** `checks/ball-egg-and-tube`

### “An egg is smooth and rounded all over, so its curving is the same everywhere.” · entry · `smooth-round-means-uniform`

- **Why it is tempting:** An egg has no corners or dents, and it looks evenly round.
- **What is true:** Small rings at an egg's tips fall short by about five times as much as on its widest part.
- **Exposed by:** `checks/patch-from-the-tip`

### “Only a ball can curve the same amount everywhere; flat things have no curving and saddles always vary.” · entry · `only-balls-qualify`

- **Why it is tempting:** A ball is the only everyday object that looks the same from every side.
- **What is true:** Zero everywhere is constant, and the hyperbolic plane makes rings too long by the same fraction everywhere.
- **Exposed by:** `checks/which-surfaces-qualify`

### “Constant curvature means the metric components are constant.” · working · `constant-components`

- **Why it is tempting:** The word constant seems to describe the numbers in the metric.
- **What is true:** Curvature comes from second derivatives of the metric and can be constant while components vary, as on a sphere.
- **Exposed by:** `checks/components-vary`

### “If every spatial slice of a universe has constant curvature, the spacetime has constant curvature too.” · formal · `curved-slices-mean-constant-spacetime`

- **Why it is tempting:** The same phrase describes the slices and de Sitter spacetime.
- **What is true:** Spacetime curvature also contains the time derivatives of the scale factor. Flat-sliced dust universes are curved spacetimes.
- **Exposed by:** `checks/flat-slices-curved-spacetime`

### “A Ricci tensor proportional to the metric means constant curvature.” · formal · `einstein-space-is-constant`

- **Why it is tempting:** Constant curvature implies the Einstein condition, and the converse looks symmetric.
- **What is true:** The Einstein condition fixes only the Ricci part; the Weyl part can be nonzero, as for Schwarzschild.
- **Exposed by:** `checks/einstein-space-not-enough`

### “Positive constant curvature pulls free-fall neighbours together, as on a sphere.” · formal · `positive-curvature-means-converge`

- **Why it is tempting:** Geodesics on a sphere, which has positive curvature, converge.
- **What is true:** A timelike tangent has negative norm, which flips the deviation, so de Sitter neighbours accelerate apart.
- **Exposed by:** `checks/falling-apart-in-de-sitter`

## Checks

1. **Entry · explain** `checks/ball-egg-and-tube`. Three ants run the ring test at many spots, walking 2 millimetres out each time. One lives on a smooth ball 6 centimetres wide. One lives on a smooth egg 6 centimetres long and 4 centimetres wide. One lives on a rolled-up paper tube 4 centimetres wide. Which of these worlds have constant curvature, and why?
   - **Hints:** Does rolling paper into a tube change any length along the paper?
   - **Answer:** The ball and the tube, but not the egg. On the ball, every small ring falls short by the same fraction, because every spot of a ball is shaped like every other. So every spot has the same matching ball, the ball itself, 3 centimetres in radius. 3 times 3 is 9, so its Gaussian curvature is 1 ninth per square centimetre everywhere. On the egg, rings at the pointed tips fall short by about five times as much as rings on the widest part, so its Gaussian curvature changes from spot to spot. The tube bends around but not along. Yet rolling paper changes no length along the paper, so its small rings come out as on flat paper at every spot. So its Gaussian curvature is zero everywhere, and zero at every spot counts as constant.
   - **Must contain:** The ball and the tube have constant curvature, the egg does not; The tube's small rings match flat paper at every spot
   - **Targets:** `tube-bends-so-not-constant`
   - **Visual:** [[paced-ring-on-a-ball-and-a-plain]]
2. **Entry · predict** `checks/patch-from-the-tip`. You cut a small round patch from a ping-pong ball. You cut another from the pointed tip of a hollow plastic egg, 6 centimetres long and 4 centimetres wide, with both ends the same shape. You lay the ping-pong patch on a second ping-pong ball, and the egg's patch on the egg's widest part. Each goes outer side out, turned a quarter turn. You may bend a patch, but never stretch it. Which patch can sit snugly?
   - **Hints:** Draw a small ring on the egg's patch. What happens to its length when you bend the patch?
   - **Answer:** Only the ping-pong patch. The ball has constant curvature, so a small patch from any spot fits at every other spot, turned by any amount. For the egg, run the ring test at the tip before cutting, and draw the ring on the patch. Bending without stretching keeps the ring's length, and keeps every point of the ring the same distance from the patch's centre. On the widest part, a ring drawn that distance from a centre falls short by only about a fifth as much. So the patch's ring is too short to lie there, and the egg's patch cannot sit snugly, however you bend it.
   - **Must contain:** Only the ping-pong patch fits; Bending without stretching keeps the ring's length
   - **Targets:** `smooth-round-means-uniform`
   - **Visual:** [[slide-a-patch-across-a-ball-and-an-egg]]
3. **Entry · choice** `checks/which-surfaces-qualify`. Imagine each of these as perfectly smooth, and use only small rings. Which have constant curvature? (a) a basketball; (b) a flat table top; (c) a saddle-shaped potato crisp that curves most strongly at its middle; (d) the hyperbolic plane; (e) a hen's egg.
   - **Hints:** For each surface, ask whether small rings behave the same way at every spot.
   - **Answer:** (a), (b) and (d). On the basketball, small rings fall short by the same fraction everywhere. On the table top, they come out as on flat ground at every spot, and zero everywhere is a constant. On the hyperbolic plane, they come out too long by the same fraction at every spot. The crisp's rings come out too long by more at its middle than near its edges. The egg's rings fall short by more at its pointed end than on its widest part. So neither of those two is constant.
   - **Must contain:** Basketball, table top and hyperbolic plane; Zero at every spot counts as constant
   - **Targets:** `only-balls-qualify`
4. **Working · evaluate-claim** `checks/components-vary`. A classmate says the metric $ds^2 = d\rho^2 + \sinh^2\rho\,d\phi^2$, with lengths in metres, cannot have constant curvature, because $g_{\phi\phi}$ changes with $\rho$. Evaluate the claim.
   - **Hints:** Use $K = -f''/f$ for $ds^2 = d\rho^2 + f(\rho)^2d\phi^2$.
   - **Answer:** False. With $f = \sinh\rho$, $f'' = \sinh\rho$, so $K = -f''/f = -1$ m$^{-2}$ at every point: this is the hyperbolic plane. Curvature is built from second derivatives of the metric and can be constant while components vary, as $g_{\phi\phi} = \sin^2\theta$ does on the unit sphere.
   - **Must contain:** K is minus f double prime over f, minus one per square metre everywhere; Varying components do not mean varying curvature
   - **Numeric:** Gaussian curvature = -1 m^-2 (signed, ±0.01)
   - **Targets:** `constant-components`
5. **Formal · derive** `checks/schur-in-two-and-three`. On a surface, the sectional curvature at a point is automatically the same for every plane, yet an egg's curvature varies from point to point. Show that in three or more dimensions, curvature that is the same for every plane at each point must be the same at every point.
   - **Hints:** Take the divergence of the Ricci tensor.
   - **Answer:** Contracting $R_{\rho\sigma\mu\nu} = K(g_{\rho\mu}g_{\sigma\nu} - g_{\rho\nu}g_{\sigma\mu})$, with $K$ a function, gives $R_{\mu\nu} = (n-1)Kg_{\mu\nu}$ and $R = n(n-1)K$. The contracted Bianchi identity $\nabla^\mu R_{\mu\nu} = \tfrac12\nabla_\nu R$ then reads $(n-1)(n-2)\nabla_\nu K = 0$. For $n \ge 3$, $\nabla K = 0$, so $K$ is constant on a connected space. For $n = 2$ the factor vanishes, so nothing forces an egg's $K$ to be constant.
   - **Must contain:** Contract to get the Ricci tensor and scalar in terms of K; The contracted Bianchi identity gives (n minus 1)(n minus 2) times the gradient of K equal to zero; In two dimensions the factor vanishes
6. **Formal · evaluate-claim** `checks/flat-slices-curved-spacetime`. In the flat-sliced universe filled with dust, the Einstein–de Sitter universe, every slice of constant cosmic time is flat. A student concludes that its spacetime is a space of constant curvature with zero curvature. Evaluate the claim.
   - **Hints:** Compute one Riemann component that involves time derivatives of $a$.
   - **Answer:** False. Zero constant curvature would make the Riemann tensor vanish. With $c = 1$, $ds^2 = -dt^2 + a^2(dx^2 + dy^2 + dz^2)$, $\Gamma^x{}_{tx} = \dot a/a$ and $\Gamma^t{}_{xx} = a\dot a$ give $R^x{}_{txt} = -\ddot a/a$, which for $a \propto t^{2/3}$ is $2/(9t^2) \neq 0$. No other constant $K$ works either, because the dust makes $R_{\mu\nu}$ contain $u_\mu u_\nu$ terms, not only $g_{\mu\nu}$. Flat slices constrain only the induced metric.
   - **Must contain:** Zero curvature would need a vanishing Riemann tensor; A Riemann component minus a double dot over a is nonzero; The dust spoils proportionality of Ricci to the metric
   - **Targets:** `curved-slices-mean-constant-spacetime`
7. **Formal · evaluate-claim** `checks/einstein-space-not-enough`. Outside a non-rotating black hole the Ricci tensor vanishes, so it is zero times the metric. Is the Schwarzschild exterior therefore a space of zero constant curvature? When does a Ricci tensor proportional to the metric imply constant curvature?
   - **Hints:** Which part of the Riemann tensor does the Ricci tensor not see?
   - **Answer:** No. Constant curvature with $K = 0$ means $R_{\rho\sigma\mu\nu} = 0$, but Schwarzschild has Kretschmann scalar $R_{\rho\sigma\mu\nu}R^{\rho\sigma\mu\nu} = 48M^2/r^6 \neq 0$. The Einstein condition fixes only the traces of the Riemann tensor; the Weyl tensor carries the rest. For $n \ge 3$, an Einstein space has constant $\lambda$, and it has constant curvature $K = \lambda/(n-1)$ exactly when its Weyl tensor vanishes. In three dimensions the Weyl tensor always vanishes, so there the two conditions agree.
   - **Must contain:** Schwarzschild is Ricci-flat but not flat; Constant curvature is an Einstein space with vanishing Weyl tensor
   - **Targets:** `einstein-space-is-constant`
8. **Formal · derive** `checks/falling-apart-in-de-sitter`. De Sitter spacetime has constant curvature $K = +1/\alpha^2$ ($c = 1$). Using the course geodesic deviation equation, find how the separation of two nearby freely falling observers, initially at rest relative to each other, changes with proper time. Contrast this with nearby geodesics on a sphere of the same $K$.
   - **Hints:** Insert the constant-curvature Riemann tensor into $D^2\xi^\mu/d\tau^2 = -R^\mu{}_{\nu\rho\sigma}u^\nu\xi^\rho u^\sigma$.
   - **Answer:** With $R^\mu{}_{\nu\rho\sigma} = K(\delta^\mu_\rho g_{\nu\sigma} - \delta^\mu_\sigma g_{\nu\rho})$, $u\cdot u = -1$ and $u\cdot\xi = 0$, the deviation equation gives $D^2\xi^\mu/d\tau^2 = -K(\xi^\mu\,u\cdot u - u^\mu\,u\cdot\xi) = +\xi^\mu/\alpha^2$. Starting at rest relative to each other, the separation grows as $|\xi_0|\cosh(\tau/\alpha)$: the observers accelerate apart. On a sphere the unit tangent has $u\cdot u = +1$, giving $\xi'' = -\xi/\alpha^2$ and convergence. The same positive $K$ acts oppositely because a timelike plane has a negative area factor.
   - **Must contain:** The separation's second derivative is plus the separation over alpha squared; It grows as the hyperbolic cosine of proper time over alpha; The sign differs from the sphere because u dot u is minus one
   - **Targets:** `positive-curvature-means-converge`
   - **Visual:** [[hyperboloids-in-flat-spacetime]]

## Notation traps

| Issue | Course choice | Variants you will meet |
| --- | --- | --- |
| The letters K and k for constant curvature | $K$ is the constant sectional curvature, never the Kretschmann scalar. A Robertson–Walker slice whose bracketed metric has curvature $k$ has $K = k/a(t)^2$. | Some texts normalize $k$ to $+1$, $0$ or $-1$ and give $a$ units of length; others keep $a$ dimensionless. Some flip the overall sign of the Riemann form. |
| Signs of K and of the cosmological constant for de Sitter | With signature $(-,+,+,+)$ and the course Riemann tensor, de Sitter has $K = +1/\alpha^2$, $R = 12/\alpha^2$ and $\Lambda = 3K$. | With the opposite sign of the Riemann tensor, the Ricci contraction or the Einstein equation, de Sitter appears with $K < 0$ or $\Lambda = -3K$. |

## Visuals

- ★ [[slide-a-patch-across-a-ball-and-an-egg]] (flagship): Flagship: a patch that fits everywhere, turned by any amount, only on surfaces of constant curvature. *Sketch:* A patch with a drawn ring, cut from a chosen spot of a ball, a flat sheet, a tube, an egg or a piece of the hyperbolic plane. The learner drags and turns it; it bends without stretching, and gaps show where it cannot fit. Readouts give the ring's length on the patch and the ring-test answer beneath it.
- [[paced-ring-on-a-ball-and-a-plain]] (core): The ring test repeated at many spots, and rings on the hyperbolic plane. *Sketch:* This concept adds a survey mode that tints a ball, an egg, a tube or a crisp by its ring-test answer at each spot, uniform only on the constant-curvature surfaces, and a hyperbolic-plane mode on a disc map whose rings grow as $2\pi\sinh\rho$.
- [[distant-ruler-in-three-spaces]] (supporting): How curvature changes the angle of a distant ruler. *Sketch:* A two-dimensional slice of closed, flat and open space with an observer, sight lines and a ruler at adjustable distance. Readouts compare $L/\mathrm{sn}_K(D)$ with the flat angle; a slider sets the curvature radius, with the measured bound marked.
- [[hyperboloids-in-flat-spacetime]] (supporting): De Sitter and anti-de Sitter as hyperboloids, with the sign of free-fall deviation. *Sketch:* Two-dimensional de Sitter and anti-de Sitter drawn as hyperboloids in flat three-dimensional spacetimes. Free-fall pairs separate on one and refocus on the other; de Sitter can be sliced into closed, flat or open slices.

## Tutor moves

**Open with**

- Picture a tiny ant on a perfectly smooth ball and another on a smooth egg. Each draws small rings at many spots, always walking the same short distance out from each ring's own centre. Whose rings will all come out alike? *(prediction)*
- Imagine an eggshell that bends like thin card but never stretches. If you cut a small patch from its pointed tip, could you make the patch sit snugly on the egg's widest part? *(prediction)*

**If the learner is stuck**

- *The learner insists the tube cannot count because it bends one way and not the other.* → Unroll the tube and point out that rings drawn on it keep their lengths, so the ring test gives the flat answer at every spot. *Uses:* `ways_in/same-ring-test-at-every-spot`, `checks/ball-egg-and-tube`
- *The learner expects positive curvature to pull falling neighbours together.* → Have the learner compute $u\cdot u$ for a timelike and a spacelike unit tangent, then insert each into the deviation equation. *Uses:* `checks/falling-apart-in-de-sitter`

**Common questions**

- *What does this have to do with the universe?* (entry) Astronomers who map millions of galaxies find that, on the largest scales, the universe is much the same everywhere and in every direction. If space itself is like that, a small chunk of space from one place would fit anywhere else, turned by any amount. So space would curve by the same amount everywhere. It would be a three-dimensional version of a ball's surface, of flat ground, or of the hyperbolic plane. Measurements of light from the young universe find space's curving too gentle to tell apart from flat. *Uses:* `ways_in/a-patch-that-fits-anywhere`, `ways_in/a-distant-ruler-weighs-space`
- *Why are these spaces called maximally symmetric?* (formal) Locally they have $n(n+1)/2$ independent Killing vectors, the most possible, since a Killing field is fixed by its value and derivative at one point. Quotients such as a flat torus can have fewer globally. *Uses:* `ways_in/isotropy-forces-constancy`, `problems/killing-vector-count`

**Switching levels**

- To working when: asks for a formula for the rings; mentions the Riemann or Ricci tensor. Go to the tensor form and its contractions, then the ring function. *Uses:* `ways_in/one-number-fills-the-table`, `ways_in/rings-and-triangles-in-closed-form`
- To formal when: asks why isotropy forces constancy; asks about de Sitter or anti-de Sitter. Prove Schur's lemma, then contrast the Lorentzian models with curved slices and Einstein spaces. *Uses:* `ways_in/isotropy-forces-constancy`, `ways_in/spacetimes-of-one-curvature-number`
- To research when: asks about holography, cosmic topology or classifying three-dimensional spaces. Open the research horizon. *Uses:* `research_horizon/holography-in-anti-de-sitter`, `research_horizon/topology-of-constant-curvature-universes`

**Pronunciations:** Minding → MIN-ding; Schur → SHOOR; de Sitter → duh SIT-er; Riemann → REE-mahn; Beltrami → bel-TRAH-mee; Killing vector → KILL-ing vector, after Wilhelm Killing; Milne → MILN

**Voice notes:** Read $\mathrm{sn}_K(\rho)$ as 'the ring function of rho'.

## History

- **Ferdinand Minding (1839).** Showed that surfaces of equal constant Gaussian curvature are locally isometric.
- **Bernhard Riemann (1854).** In his 1854 lecture, published in 1868, described spaces of constant curvature in any dimension and wrote their metric as a position-dependent multiple of the flat one. Bernhard Riemann (1868), *Über die Hypothesen, welche der Geometrie zu Grunde liegen*, Abhandlungen der Königlichen Gesellschaft der Wissenschaften zu Göttingen 13, 133–150
- **Eugenio Beltrami (1868).** Showed that surfaces of constant negative curvature carry, locally, the non-Euclidean geometry of Bolyai and Lobachevsky.
- **Friedrich Schur (1886).** Proved that curvature which is the same for every plane at each point is constant, in three or more dimensions.
- **David Hilbert (1901).** Proved that no complete surface of constant negative curvature can be isometrically immersed in three-dimensional Euclidean space. David Hilbert (1901), *Ueber Flächen von constanter Gaussscher Krümmung*, Transactions of the American Mathematical Society 2, 87–99, doi:10.1090/S0002-9947-1901-1500557-5
- **Willem de Sitter (1917).** Found the empty universe with a cosmological constant now called de Sitter spacetime. Willem de Sitter (1917), *On Einstein's theory of gravitation and its astronomical consequences. Third paper*, Monthly Notices of the Royal Astronomical Society 78, 3–28, doi:10.1093/mnras/78.1.3

## Research horizon

- **Holography in anti-de Sitter spacetime.** Gauge/gravity duality relates string theory on five-dimensional anti-de Sitter spacetime times a five-sphere to a four-dimensional conformal field theory on its boundary. The isometry group of that anti-de Sitter spacetime, $SO(2,4)$, is the conformal group of four-dimensional Minkowski space, which is why constant negative curvature is the natural stage. Juan Maldacena (1998), *The large N limit of superconformal field theories and supergravity*, Advances in Theoretical and Mathematical Physics 2, 231–252, arXiv:hep-th/9711200
- **Topology of a constant-curvature universe.** Constant curvature fixes only the local geometry of space. A flat or hyperbolic universe could be a finite quotient of its model space, and if light had crossed it since the microwave background was released, the background would show pairs of matched circles. Searches for such circles have so far found none. Neil J. Cornish, David N. Spergel, Glenn D. Starkman (1998), *Circles in the sky: finding topology with the microwave background radiation*, Classical and Quantum Gravity 15, 2657–2670, doi:10.1088/0264-9381/15/9/013
- **Geometrization of three-dimensional manifolds.** Thurston conjectured that every closed orientable three-manifold can be cut into pieces carrying one of eight model geometries, three of them the constant-curvature geometries. Perelman proved the conjecture using Ricci flow, so constant curvature sits at the centre of the classification of possible spatial topologies. William P. Thurston (1982), *Three dimensional manifolds, Kleinian groups and hyperbolic geometry*, Bulletin of the American Mathematical Society (New Series) 6, 357–381, doi:10.1090/S0273-0979-1982-15003-0

## Review: novice

**Verdict:** fixed (2026-09-13, revision 5)

**Retell attempt:** Every spot of a surface gets a curving number from the ring test: walk straight out a short way in every direction and see how short the ring comes out. If that number is the same at every spot, the surface has constant curvature. A 6-centimetre ball gives 1 ninth per square centimetre everywhere. An egg does not, because its tips are about five times more curved than its middle, 9 sixteenths against 1 ninth, though I could not see how 16 ninths became 9 sixteenths and just assumed you flip the fraction. Flat ground counts because zero is still one number, and a rolled paper tube counts because rolling changes no length along the paper. Earth is nearly but not quite one of these, and the gap is far too small to walk out. On a constant-curvature surface a small patch fits anywhere, turned by any amount, if you bend it without stretching; Minding proved that in 1839. The egg's tip patch cannot fit the widest part because the ring drawn on it keeps its length. It says every point of the ring stays the same distance from the centre, but when I bend a patch the distance through the air changes, so I was not sure which distance was meant. Then the widest part's ring "falls short by only about a fifth as much" and the patch's ring is "too short" — I had to stop and work out that falling short by less means longer. The tube test cuts its square from flat paper, not from the tube, so I was not sure it was the same claim. There is also a saddle surface that is the same everywhere, the hyperbolic plane, whose rings blow up: 466 metres at 5 metres out, each extra metre multiplying by about 2.7 because the gaps between walks keep widening. Its curvature is minus 1 per square metre, though I did not see where the 1 came from. People crochet it and it ruffles like kale. So three kinds: like a ball, like flat ground, like the hyperbolic plane. For the universe, space could be "a three-dimensional version of a ball" — but a ball is already three-dimensional, so that stopped me; I think they mean a ball's surface with one more dimension.

**Stumbles (42)**

- “A world that curves by the same amount at every spot and in every direction”: The first what-if is the tube: from outside it bends around but not along, so 'in every direction' reads as false, and it contradicts the note's own tube misconception.
- “On some surfaces the ring test gives the same answer at every spot”: 'The same answer' is ambiguous: ring lengths depend on the distance walked, so the reader cannot tell what must agree.
- “walk straight out the same short distance from a centre (all three entry recaps)”: 'Walk straight' is used without its meaning, although the recap must make the way self-sufficient.
- “A spot's Gaussian curvature is 1 divided by its matching ball's radius times itself. The matching ball is the ball whose small rings fall short by the same fraction.”: The matching ball is used before it is defined, and '1 divided by the radius times itself' had to be reread for grouping; the prerequisite words it differently.
- “measure the ring through the end marks”: 'End marks' is never explained.
- “That makes the Gaussian curvature 1 ninth per square centimetre at every spot.”: A step left implicit: where 1 ninth comes from.
- “It is 9 sixteenths per square centimetre at a tip, and 1 ninth on the widest part.”: A number with no source: the tip's matching-ball radius is never given, so 9 sixteenths cannot be checked.
- “On the ball, every ring falls short by the same fraction, wherever the ant stands.”: A claim given without a reason.
- “Flat ground counts too. Its small rings come out 6.28 times the distance walked at every spot, so its Gaussian curvature is zero everywhere.”: A teenager objects that zero is no curving at all; the link from 'zero everywhere' to 'constant' is left implicit.
- “Rolling paper changes no length along it”: Ambiguous 'it': the paper or the tube.
- “So no walker could ever notice.”: Notice what is unclear, and 'never' contradicts the previous sentence, where surveys do detect it.
- “Lay it on a second ping-pong ball, at any spot, turned any way.”: 'Turned any way' admits flipping the patch over, and a flipped ping-pong patch does not sit snugly on a ball; the rule is not something the reader can follow as meant.
- “A gap opens under part of it.”: Which part is not said, so the reader cannot picture or test it.
- “First draw a small ring on the patch.”: Which ring? A ring drawn anywhere on the patch is not a ring-test ring, and 'first' after cutting is too late to run the test on the shell.
- “Bending without stretching changes no length along the patch, so the ring keeps its length.”: A step left implicit: the argument also needs every point of the ring to stay the same distance from the centre, or the ring would no longer be a ring-test ring.
- “On the widest part, the same ring must fall short by only about a fifth as much.”: Reread: 'the same ring must' is contradictory, and the reader must work out that a less-short ring is longer, so the patch's ring is too short.
- “The reverse is the surprise.”: 'Reverse' of what is unclear; the reader had to reread to find the two directions of the argument.
- “a small enough patch”: A first what-if with no answer: how small is small enough, and why does size matter?
- “A paper tube lets you test it, because a patch of tube can bend to fit the tube along its length or around it.”: The try-it cuts its square from flat paper, not from the tube, so the test does not match the claim; the link that flat paper and the tube share zero curvature is missing.
- “Every direction at a spot is also like every other direction.”: False-sounding for the tube seen from outside; the sentence needs its measurer.
- “draw a small ring on it. ... Both times it bends to lie snugly, with no creases.”: The try-it asks for a ring but never says what to see about it, and it gives no contrast showing that a fit is not automatic.
- “Yes. Such a world is called the hyperbolic plane.”: A surprising claim with no backing, and 'world' and 'surface' name one idea with two words.
- “Picture one whose small rings come out too long by the fraction that a ball 1 metre in radius makes them too short.”: Reread twice: the comparison is packed into one clause, and the Gaussian curvature it gives is not stated.
- “1 metre out ... 3 metres out”: The table skips 2 metres, and a reader checking the 2.7 rule wonders what happens there.
- “each extra metre makes the ring about 2.7 times as long”: A surprise with a count but no reason.
- “by adding stitches faster and faster in each round. The pieces ruffle like kale leaves, because the extra length has no room to lie flat.”: 'Lie flat' uses 'flat' for a position, a wording trap, and 'faster and faster' gives no rule a crocheter could follow.
- “So surfaces of constant curvature come in three kinds”: The 'so' does not follow from the crisp paragraph; the reason for exactly three is left implicit.
- “You lay each patch on another spot of its own surface, turned a quarter turn.”: Ambiguous starting state: the ping-pong ball now has a hole, the patch could be flipped, and the egg's size, which fixes the 'about a fifth' in the answer, is not given.
- “If you cut a small patch from the pointed tip of an eggshell, could you make it sit snugly on the egg's widest part without stretching it?”: A rule the reader cannot follow: a real eggshell cracks rather than bends.
- “Each draws small rings at many spots.”: The opening question does not say the rings share one walking distance, so 'alike' is ambiguous.
- “On the largest scales, the universe looks much the same everywhere”: 'Looks' without a measurer, and 'in three directions instead of two' is vague.
- “On them, a small patch cut from one spot fits snugly at every other spot, turned by any amount, if you bend it without stretching it.”: The summary is the first thing the reader meets, but "turned by any amount" is only pinned down inside "A patch that fits anywhere". Read on its own, it lets the reader flip the patch over, and a flipped patch does not sit snugly.
- “A tip's matching ball has a radius of 1 and a third centimetres, and 1 and a third times itself is 16 ninths. So the Gaussian curvature at a tip is 9 sixteenths per square centimetre”: A step left implicit. The ball's number is worked out in full ("3 times 3 is 9"), but the harder step here, dividing 1 by a fraction, is skipped, so 16 ninths turning into 9 sixteenths has to be taken on trust.
- “every point of the ring stays the same distance from the patch's centre”: A measurement with no measurer. Bending a patch does change the straight-line distance through the air from its centre to its rim; only the distance along the patch is kept, and that is the one the argument needs.
- “On the widest part, a ring drawn that distance from a centre falls short by only about a fifth as much. So the patch's ring is too short to lie there”: A step left implicit, and I had to reread. Falling short by less means being longer, and only after working that out does "too short" follow.
- “A paper tube lets you test Minding's result. The tube's curvature is zero at every spot, like flat paper's. So a square cut from flat paper should fit the tube anywhere”: Minding's result, as the way states it, is about a patch cut from a surface fitting elsewhere on that same surface. The square here is cut from flat paper, not from the tube, so the test does not follow from what the reader has been told.
- “In this note, "turned by any amount" always means spun like this, with the same side facing out.”: Two wordings for one idea four sentences apart: the patch was laid down "outer side out", and the rule is then given as "with the same side facing out".
- “Its small rings come out too long by the same fraction that the ball's small rings come out too short. So its Gaussian curvature is minus 1 per square metre at every spot.”: A number with a skipped step: where the 1 comes from is left to the reader, although the ball's and the egg's numbers are both worked out in full.
- “It is zero where small rings come out as on flat ground, and negative where they come out too long.”: The glossary gives a rule for the size of a positive Gaussian curvature but none for a negative one, so the minus 1 per square metre in "Shaped like a saddle everywhere" cannot be checked against the definition.
- “Each draws small rings at many spots, always walking the same short distance out from the centre.”: "The centre" is ambiguous: many rings at many spots have many centres, so the opening question does not say what is held fixed.
- “It would be a three-dimensional version of a ball, of flat ground, or of the hyperbolic plane. Measurements of light from the young universe find its curving too gentle to tell apart from flat.”: A ball is already a three-dimensional object, so "a three-dimensional version of a ball" reads as nonsense; the entry ways always mean the surface an ant lives on. And "its" has two candidates, the young universe and space.
- “You cut a small round patch from a ping-pong ball, and another from the pointed tip of a hollow plastic egg 6 centimetres long and 4 centimetres wide.”: The check's answer says the widest part's ring falls short by "about a fifth as much", which holds only for the egg of the entry ways, whose two ends are the same shape. The check leaves the shape open, and the sentence runs long.

**Fixes**

- Tagline and summary: removed 'in every direction' (false for the tube seen from outside) and said what must agree: rings drawn the same distance from their centres.
- All three entry recaps now define walking straight; the first recap defines the matching ball before using it and words the Gaussian-curvature rule as the prerequisite does.
- Ring-test way: showed the 3-times-3 and 1-and-a-third steps behind 1 ninth and 9 sixteenths, gave the ball's reason, made 'zero everywhere counts' explicit, and fixed the Earth sentence that contradicted the surveys.
- Patch way: defined 'turned by any amount' as spinning outer side out (a flipped patch does not fit), said where the gap opens, specified the ring as a ring-test ring drawn before cutting, added the distance-from-centre step, matched the tube test to a flat-paper square, and gave the ant as the measurer for 'every direction is alike'. The try-it now shows a contrast on a tennis ball. The egg's size is in the recap so 'about a fifth' is backed.
- Saddle way: backed the existence of the hyperbolic plane, used 'surface' throughout instead of 'world', split the matching-ball comparison and stated K = minus 1 per square metre, added the 2-metre row (2 pi sinh 2 = 22.8 m, checked in python), gave a reason for the fast growth (the wider the gap, the faster it widens), replaced 'lie flat' and 'faster and faster' with a doable crochet rule, and gave the reason for exactly three kinds.
- Entry checks: patch check now fixes the egg's size, a second ping-pong ball and outer side out; both entry answers show the same steps as the ways.
- Tutor moves: the eggshell opening question now imagines a shell that bends; the universe common question names who measures.
- Glossary: ring test, matching ball, Gaussian curvature and hyperbolic plane reworded to match the entry ways.
- Ladder: the sectional-curvature bridge in 'One number fills the whole curvature table' now says a plane's sectional curvature is the Gaussian curvature of the surface its geodesics sweep out, linking back to the ring test; the algebraic uniqueness fact and K = -f''/f are marked as taken on trust; 'the disc inside' became 'the disc of geodesic radius rho around the centre' (closed sphere); the distant-ruler way defines the conformal factor through conformal time.
- Budget: entry explanations went from 793 to 1,065 words. To stay under the review allowance, the 'small enough' strip reason moved from the patch explanation to its simplifies, and the surveyor sentence in the ring-test way was dropped. Tutoring rose to 2,721 of 3,300, way extras to 812 of 800 (within the 10% allowance).
- Bumped the revision to 2.
- Second novice pass (over revision 2; the stumbles above list the first pass's 31 findings first, then this pass's 11). Revision bumped to 3.
- Summary: "turned by any amount" now says "about its own centre", so the reader who never reaches "A patch that fits anywhere" cannot read it as flipping the patch over.
- Ring-test way: added the step 1 divided by 16 ninths is 9 sixteenths, so the tip's number is worked out as fully as the ball's.
- Patch way: said that the ring's distance from the patch's centre is measured along the patch (bending does change the straight-line distance); added the step that a ring falling short by less is longer; and replaced "A paper tube lets you test Minding's result" with Minding's result for two surfaces of the same curvature number, since the test square is cut from flat paper rather than from the tube. Also settled on one wording, "outer side out".
- Saddle way: added "1 times 1 is 1" so the minus 1 per square metre is worked out, not asserted.
- Glossary: Gaussian curvature now gives the rule for the size of a negative value, not only its sign.
- Tutor moves: the opening question names each ring's own centre; the universe question says "a ball's surface" (a ball is already three-dimensional) and replaces an ambiguous "its" with "space's".
- Check "patch-from-the-tip": split the long opening sentence and pinned the egg's shape, which the answer's "about a fifth" depends on.
- Ladder: at working, "nondegenerate plane" now says what it means (the area factor does not vanish) instead of leaving a strong undergraduate to infer it from the denominator. Every non-entry way's first sentence was checked against the way title it names, and all eight titles match.
- Budget: entry way explanations went from 1,065 to 1,093 words, inside the 1,100 review ceiling on the core cap of 1,000. Nothing was dropped; the only shortening was the duplicate phrase "with the same side facing out", which the stumble list records.

**Concerns**

- Entry way explanations now sit at 1,093 words, against the core cap of 1,000 and the 1,100 review ceiling. The physics reviewer has almost no room: any added entry sentence must be paid for by dropping a lower-value one, and the fixes must say which.
- The summary runs to five sentences where the guide asks for two or three. I did not merge them, because each carries a distinct claim and merging would push sentences past 32 words. An editor should decide whether to move the paper-tube example out of the summary.
- "World" (tagline, the first way's question, the ball-egg-and-tube check) and "surface" (everywhere else) name one idea. The first pass fixed this only in the saddle way. I left the rest, because the tagline must also cover three-dimensional spaces and spacetimes, where "surface" would be wrong. An editor should settle on one umbrella word and apply it everywhere.
- Physics reviewer: confirm the two claims this pass added. (1) "Minding's result also covers two surfaces whose curvature is the same number everywhere" — that two surfaces of equal constant Gaussian curvature are locally isometric, which is what the paper-tube test needs. (2) The glossary's new rule for a negative Gaussian curvature: that a hyperbolic spot of curvature minus 1 over a squared makes small rings too long by the same fraction that a ball of radius a makes them too short, which holds to leading order in the ring's radius, the order the entry rung works at.
- Carried from the first novice pass: the entry ways read the egg as a spheroid "with both ends the same shape", while the choice check offers "a hen's egg", which has one blunt end. The reasoning transfers, but the numbers are the spheroid's. No change made.
- Carried from the first novice pass: the visual sketches, especially slide-a-patch-across-a-ball-and-an-egg, should adopt the spin-in-place meaning of "turned by any amount" and draw the ring as a ring-test ring made before cutting.
- Carried from the writer: the conventions file does not fix the normalization of k in the Robertson-Walker form, does not define Omega_K, and has no entry for the ring function sn_K. The note handles all three locally in notation_traps rather than inventing a convention, but they belong in the conventions file before the next note reuses them.
- Carried from the writer, for the physics reviewer: "about 144 megaparsecs ... seen in the microwave background and in galaxy clustering" in "A distant ruler weighs space" runs together two epochs whose comoving sound horizons differ by about 2 per cent, in a paragraph that quotes 0.03 per cent precision; name one epoch or widen the hedge. And in "Spacetimes of one curvature number", "The flat-sliced Einstein-de Sitter universe is curved" means it is not of constant spacetime curvature, which the bare word "curved" does not carry.

**Re-read** (2026-09-16, revision 5): 2 stumbles in 2 changed passages

- “At the release of the microwave background it is about 144 megaparsecs”: The pronoun 'it' sits two clauses away from 'a preferred spacing', and the nearest noun phrase is 'galaxy clustering', so a reader has to backtrack to find what is 144 megaparsecs.
- “the slightly later epoch that galaxy clustering records gives about 147.”: The second number has no unit; the reader must infer megaparsecs from the earlier clause.
- Fix: Working way 'A distant ruler weighs space': 'it is' became 'that spacing is' and 'about 147' became 'about 147 megaparsecs' (wording only, claims unchanged).
- Fix: History title 'Ueber Flächen von constanter Gaussscher Krümmung' read as the novice: a German title as printed, no stumble.

## Review: physics

**Verdict:** fixed (2026-09-16, revision 5)

**Verification**

- Egg numbers at entry: spheroid 6 cm long, 4 cm wide has K = 9/16 per cm^2 at a tip (matching radius 4/3 cm) and 1/9 per cm^2 on the widest part; tips fall short about five times as much (81/16 = 5.06), the widest part about a fifth (0.198).: Principal radii of a prolate spheroid, semi-axes 3 and 2 cm; python3. → Confirmed.
- Ball 6 cm wide: K = 1/9 per cm^2; flat ring 6.28 times the distance.: Hand. → Confirmed.
- Earth: GRS80 K = 2.475e-14 m^-2 at the equator (matching radius 6356.8 km), 2.442e-14 at the poles (6399.6 km), 1.35 per cent and 43 km apart; a ring 1 km out falls short by about 26 thousandths of a millimetre, differing by about a third of a thousandth between poles and equator.: K = 1/(MN) from a = 6378137 m, 1/f = 298.257222101; shortfall 2pi(rho - sn_K(rho)); python3. → Confirmed: 6356.75 km, 6399.59 km, 42.8 km, 1.352 per cent, 0.0259 and 0.0256 mm, difference 0.00035 mm.
- Hyperbolic rings with K = -1 m^-2: 7.4, 22.8, 63, 171, 466 m at 1 to 5 m (flat 6.3, 12.6, 18.8, 25.1, 31.4); successive ratio about 2.7.: 2 pi sinh(rho); python3. → Confirmed (ratios 2.72).
- Matching hyperbolic plane of a 1 m ball has K = -1 per m^2 and rings too long by the same fraction the ball's are too short.: 2 pi sn_K(rho) = 2 pi rho (1 - K rho^2/6 + ...), sign of K. → Confirmed to leading order in rho, the order small rings work at; the entry text says small rings.
- Constant-curvature Riemann form, contraction to (n-1)K g and n(n-1)K, G = -(1/2)(n-1)(n-2)K g, Lambda = 3K in four dimensions.: Re-derived with the course Riemann and Ricci conventions; sphere check R_thetaphithetaphi = K g g = sin^2 theta, positive as the conventions require. → Confirmed, signs and factors agree with the course Einstein equation.
- Ring function: f'' + K f = 0 with f(0) = 0, f'(0) = 1; f'^2 + K f^2 = 1; dr^2/(1 - K r^2); disc area 4 pi sn_K(rho/2)^2; series 1 - K rho^2/6.: Solved by hand; disc areas 2 pi a^2 (1 - cos) and 2 pi (cosh - 1) compared numerically; python3. → Confirmed.
- Worked example: ring 1000 km out on a 6371 km sphere is 6257.4 km, 25.8 km or 0.410 per cent short, against K rho^2/6 = 0.411 per cent.: python3. → Confirmed (6257.42 km, 25.77 km, 0.4101 per cent, 0.4106 per cent).
- Angle sum pi + K A and hyperbolic area bound pi/|K|.: Local Gauss-Bonnet; also checked for a region larger than a hemisphere with interior angles measured inside the region. → Confirmed.
- Ruler angle theta = L/sn_K(D), larger for K > 0 by about K D^2/6; conformal factor leaves null paths and angles unchanged.: Area of the sphere at distance D; series of 1/sn_K. → Confirmed.
- Sound horizon about 144 Mpc, ruler at about 13,900 Mpc, angle known to 0.03 per cent, Omega_K = 0.001 +/- 0.002.: Planck 2018 VI: r_* = 144.43 Mpc, r_drag = 147.09 Mpc, 100 theta_* = 1.04110 +/- 0.00031, Omega_K = 0.0007 +/- 0.0019 with BAO; D_M = r_*/theta_* computed. → Confirmed (D_M = 13,873 Mpc, 0.030 per cent). The 144 Mpc figure is the last-scattering value; galaxy clustering uses the 147 Mpc drag-epoch value, now said.
- Problem de-sitter-radius-from-lambda: K = 3.67e-53 m^-2, R = 4.4e-52 m^-2, alpha = 1.65e26 m = 17.5 billion ly.: python3. → Confirmed (1.6514e26 m, 1.7455e10 ly).
- Problem curvature-bound-from-a-distant-ruler: c/H_0 = 4448 Mpc, radius at least 62,900 Mpc (4.5 times 13,900), |K| D^2 = 0.049, sinh(x)/x = 1.0082, angle 0.81 per cent smaller.: python3. → Confirmed (4447.96 Mpc, 62,904 Mpc, 0.0488, 1.00816, 0.809 per cent).
- Check components-vary: K = -f''/f = -1 m^-2 for f = sinh rho.: Hand. → Confirmed.
- Schur's lemma: contracted Bianchi identity gives (n-1)(n-2) grad K = 0.: Re-derived: (n-1) grad K = (1/2) n (n-1) grad K. → Confirmed; connectedness is assumed at the start of the way.
- Killing identity nabla_mu nabla_nu xi_rho = R_sigma mu nu rho xi^sigma in course conventions, and the unit-sphere check with xi = d/dphi.: Re-derived from [nabla_mu, nabla_nu] omega_rho = R_rho sigma mu nu omega^sigma (course sign), Killing antisymmetry and the cyclic identity; computed nabla_theta nabla_theta xi_phi = -sin^2 theta and R_phi theta theta phi = -sin^2 theta by hand. → Confirmed, including the sign of the covector Ricci identity in the hint.
- Killing bound n(n+1)/2, attained by Euclidean space; O(1,n) and O(2,n-1) have dimension n(n+1)/2.: Counting; dim O(p,q) = (p+q)(p+q-1)/2. → Confirmed.
- De Sitter deviation D^2 xi/d tau^2 = +K xi for unit timelike u, growth cosh(tau/alpha), e-folding time alpha; sphere gives -K xi.: Inserted the constant-curvature Riemann tensor into the course deviation equation with u.u = -1 and u.xi = 0. → Confirmed. The sentence on spacelike geodesics gave the timelike-plane reason for the wrong case; reworded.
- Einstein-de Sitter: Gamma^x_tx = adot/a, Gamma^t_xx = a adot, R^x_txt = -addot/a = 2/(9 t^2) for a ~ t^(2/3).: Course Riemann formula by hand. → Confirmed.
- Robertson-Walker spacetime has constant spacetime curvature only for T proportional to g: de Sitter, anti-de Sitter, Minkowski, Milne.: G = -3K g forces rho + p = 0 and constant rho; k = +1 with Lambda = 0 has no solution. → Confirmed.
- Schwarzschild Kretschmann 48 M^2/r^6; Einstein space with zero Weyl tensor is constant curvature for n >= 3; Weyl vanishes in three dimensions.: Standard results checked against the Weyl decomposition. → Confirmed.
- Conformally flat factor (1 + K|x|^2/4)^-2; Riemann's 1854 metric.: Stereographic form of the constant-curvature metric. → Confirmed.
- References: Moritz 1980; Planck 2018 VI; Riemann 1868; Hilbert 1901; de Sitter 1917; Maldacena 1998; Cornish, Spergel and Starkman 1998; Thurston 1982; history years for Minding 1839, Beltrami 1868, Schur 1886.: One web search each. → All confirmed; DOIs added for Hilbert, de Sitter, Cornish et al. and Thurston; Hilbert's title spelled Ueber as printed. Riemann's page range is listed as 133-150 by the Deutsches Textarchiv and 133-152 by another record; the note's 133-150 kept.

**Counterexamples tried**

- Cone tip: a patch containing the tip does not fit elsewhere although K = 0 away from the tip; the note requires smooth surfaces and small patches, and the checks say perfectly smooth.
- Paper tube and Möbius band: bent but flat; small rings and patches match flat paper, as the note says; a strip longer than the way around the tube overlaps, recorded in simplifies.
- Region larger than half a closed surface: the angle-sum formula still holds with interior angles measured inside the region; the second metric form r = sn_K covers only half the sphere, stated.
- Hole (flat torus, compact hyperbolic manifold): local geometry constant, global Killing fields lost; stated in the global-limits paragraph and the common question.
- Timelike versus spacelike planes: positive K separates free-fall neighbours in de Sitter and converges spacelike geodesics in spacelike planes; sentence corrected.
- Non-static case: Robertson-Walker slices of constant curvature with a curved, non-constant-curvature spacetime (Einstein-de Sitter), handled by a check.
- Einstein space that is not constant curvature: Schwarzschild, handled by a check.
- Lorentzian signature for global theorems: Killing-Hopf and Hilbert's theorem are Riemannian statements; scope added.

**Fixes**

- Working way 'A distant ruler weighs space': the 144 Mpc sound horizon is the last-scattering value; galaxy clustering uses the drag-epoch value of about 147 Mpc. Both are now named (novice concern).
- Formal way 'Spacetimes of one curvature number': the sentence on spacelike geodesics in de Sitter gave the negative area factor of a timelike plane as the reason for convergence in a spacelike plane; reworded so the reason matches the case. 'The Einstein-de Sitter universe is curved' now says it is a curved spacetime that is not of constant curvature (novice concern).
- Formal way 'Isotropy forces constancy': the Killing-Hopf statement is scoped to complete connected Riemannian examples.
- References: all eight verified; DOIs added for Hilbert 1901, de Sitter 1917, Cornish-Spergel-Starkman 1998 and Thurston 1982; Hilbert's title spelled as printed.
- Revision bumped to 4 because the working-rung ruler sentence changed.

**Concerns**

- The conventions file does not define Omega_K, the normalization of k in the Robertson-Walker form, or the ring function sn_K; the note handles them locally, as the novice reviewer also noted.
- Riemann 1868 page range: records disagree (133-150 versus 133-152); kept 133-150.
- Maldacena 1998 has no DOI recorded; the arXiv id and venue are confirmed.

**Diff check** (2026-09-16, revision 5)

- Sound-horizon spacing about 144 Mpc at the release of the microwave background (last scattering) and about 147 Mpc at the slightly later epoch that galaxy clustering records (baryon drag).: Web search of Planck 2018 VI parameter tables: r_* = 144.4 to 144.5 Mpc, r_drag = 147.1 to 147.2 Mpc depending on the data combination; drag epoch z about 1060 is later than last scattering z about 1090; both are comoving, so 'in today's units' is right. → Confirmed; both round to the quoted 144 and 147 Mpc.
- 1 Mpc = 3.086e22 m.: 3.0857e22 m by hand from 1 pc = 3.0857e16 m. → Confirmed.
- Hilbert 1901 title spelled 'Ueber Flächen von constanter Gaussscher Krümmung', Trans. Amer. Math. Soc. 2, 87-99, DOI 10.1090/S0002-9947-1901-1500557-5.: Web search: AMS journal page and JSTOR record for volume 2 (1901), pp. 87-99, title printed with 'Ueber'. → Confirmed.
- Novice rewrite 'that spacing is about 144 megaparsecs' and 'about 147 megaparsecs' keeps the claims.: Reread: the noun 'spacing' is the preferred spacing left by the sound waves, the same quantity the sentence measured before; unit added to the second number matches the first. → Confirmed; no change of claim, sense or scope.
