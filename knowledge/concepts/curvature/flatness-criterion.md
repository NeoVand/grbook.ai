---
type: "concept"
schema_version: 2
id: "flatness-criterion"
title: "Flatness criterion"
tagline: "A region is flat exactly when small loops there bring carried arrows back matching"
domain: "curvature"
tier: "core"
status: "physics-reviewed"
revision: 9
updated: "2026-09-13"
aliases: ["flatness theorem", "metric flatness theorem"]
prerequisites: ["path-dependence-of-parallel-transport", "holonomy", "riemann-curvature-tensor", "flat-metric", "rindler-coordinates", "simply-connected-space"]
leads_to: ["ricci-flat-spacetime", "equivalence-problem", "weyl-criterion-for-conformal-flatness", "cosmic-string", "milne-universe"]
visuals: ["paper-rolled-into-a-tube-and-a-cone", "carry-an-arrow-around-a-loop", "falling-ring-of-crumbs", "lamp-and-detector-in-a-rocket", "cross-off-matching-terms"]
---

# Flatness criterion

*A region is flat exactly when small loops there bring carried arrows back matching*

`flatness-criterion` · curvature · core · physics-reviewed (revision 9)

**Needs:** [[path-dependence-of-parallel-transport]] (entry) · [[holonomy]] (entry) · [[riemann-curvature-tensor]] (entry) · [[flat-metric]] (working) · [[rindler-coordinates]] (working) · [[simply-connected-space]] (formal)  
**Opens:** [[ricci-flat-spacetime]] · [[equivalence-problem]] · [[weyl-criterion-for-conformal-flatness]] · [[cosmic-string]] · [[milne-universe]]  
**Related:** [[integrability-condition-for-parallel-fields]] · [[local-flatness-theorem]] · [[nonzero-christoffel-symbols-in-flat-space]] · [[torsion-tensor]] · [[gravitational-redshift]]  
**Visuals:** ★ [[paper-rolled-into-a-tube-and-a-cone]] · [[carry-an-arrow-around-a-loop]] · [[falling-ring-of-crumbs]] · [[lamp-and-detector-in-a-rocket]] · [[cross-off-matching-terms]]

> Squared paper covers a small patch of ground with no holes, without stretching or tearing, exactly when its small loops bring carried arrows back matching. The Riemann curvature tensor records how small loops turn carried arrows. So a region is flat exactly when that tensor is zero throughout it. A pull alone does not show curved spacetime. But a drift between balls let go side by side in a non-spinning cabin does.

## You will be able to

**Entry**
- Explain why squared paper can cover a small patch of ground with no holes, without stretching or tearing, exactly when every small loop on it brings a carried arrow back matching. `objectives/explain-the-two-tests` ← `checks/shrink-the-patch`, `problems/cube-corner`
- Explain why a pull felt in a closed cabin that does not spin does not show curved spacetime, while a drift between balls let go side by side does. `objectives/tell-a-pull-from-curving` ← `checks/rocket-drop`

**Working**
- Decide whether a metric written in unusual coordinates is flat by computing its Riemann tensor. `objectives/test-a-metric` ← `checks/which-surfaces-are-flat`, `problems/clock-rate-curvature`
- Explain why Christoffel symbols that vanish at one event do not make spacetime flat there. `objectives/explain-why-a-region` ← `checks/christoffels-vanish-at-one-event`
- Distinguish clock-rate differences and the acceleration needed to stay put from spacetime curvature. `objectives/separate-redshift-from-curvature` ← `checks/tower-clocks-claim`

**Formal**
- State the flatness criterion with its hypotheses, and distinguish it from Ricci flatness. `objectives/state-the-hypotheses` ← `checks/ricci-flat-by-dimension`
- Explain why zero curvature everywhere gives neither one global flat chart nor trivial holonomy around holes. `objectives/mark-global-limits` ← `checks/cone-torus-verdict`
- Prove that a metric is flat by computing its curvature and constructing constant-metric coordinates. `objectives/prove-flatness-with-coordinates` ← `problems/milne-flat`

## Ways in

### 1. Squared paper or small loops · entry · picture

*Which patches of ground can squared paper cover without stretching, and how does the arrow test tell?*

**Recap:** The arrow test: press a cardboard arrow against the ground and carry it around a loop, a path that ends where it began. Never let the arrow swing to your left or right. Then compare its direction with its starting direction. On a flat floor, an arrow that never swings keeps pointing at the same wall of the room, so it always comes back matching its start. On a ball, even a small loop around a piece of the ball brings the arrow back turned a little.

Take a sheet of squared paper, the kind printed with a grid of equal squares. Press it onto a patch of ground, meaning a piece of surface with no holes, such as a coin-shaped piece. The paper must lie against the ground everywhere, in one layer. It may bend, but it must not stretch, tear or fold over onto itself.

On a table top this is easy. It also works on the side of a tin can, because the paper simply rolls around the can. On a football it fails. However you bend the paper, its edges bunch into folds, unless you stretch or tear it.

Ground is called flat when, around every spot, squared paper can cover some small patch this way. So a table top and the side of a can are flat, although the can looks bent.

Squared paper can cover a small patch exactly when every small loop on that patch brings the arrow back matching its start. A criterion is a rule for deciding something, and this agreement between the two tests is called the flatness criterion.

Here is why paper that fits makes the arrow come back matching. Draw the loop, and the arrow at each step, on the paper while it lies against the ground. The paper did not stretch, so every length and every angle drawn on it is the same as on the ground. You can judge whether the arrow swings from lengths and angles measured along the ground alone.

Now peel the paper off and lay it on a table. The drawn arrows never swing on the table either, because no length or angle changed. On a flat table, an arrow that never swings keeps pointing at the same wall, so it keeps its angle to the printed lines. After the loop it makes the same angle with the lines as at the start, and so it comes back matching its start.

**Try it:** Cut a square of paper about 5 centimetres across. Wrap it around the side of a tin can: it lies smoothly against the metal in one layer. Press it onto an orange: however you push, its edges bunch into small folds or lift off the peel.

**Takeaway:** Squared paper can cover a small patch of ground with no holes, without stretching or tearing, exactly when every small loop on that patch brings a carried arrow back matching its start.

*Builds on:* [[holonomy]], [[path-dependence-of-parallel-transport]]<br>*Visuals:* [[paper-rolled-into-a-tube-and-a-cone]], [[carry-an-arrow-around-a-loop]] (preset `flat-square`)<br>*See:* `ways_in/drawing-squared-paper-with-arrows`, `checks/shrink-the-patch`, `common_questions/is-a-football-pitch-flat`

### 2. Drawing squared paper with arrows · entry · picture

*If every small loop on a patch brings the arrow back matching, how can you draw squared paper that fits the patch?*

**Recap:** The arrow test: press a cardboard arrow against the ground and carry it around a loop, a path that ends where it began. Never let the arrow swing to your left or right. The arrow comes back matching its start when it points the same way as when it set off. A patch is a piece of ground with no holes. Squared paper is paper printed with a grid of equal squares. If squared paper covers a patch in one layer, without stretching or tearing, every loop on the patch brings the arrow back matching its start.

In "Squared paper or small loops", paper that fits a patch made every loop bring the arrow back matching its start. The reason also runs the other way. You can see it by drawing the squared paper yourself.

Suppose every small loop on a patch brings the arrow back matching its start. Pick one spot on the patch. Put two arrows there at a right angle, like the two edges at the corner of a page. Call them the first arrow and the second arrow.

Now carry copies of the two arrows to every other spot of the patch, never letting them swing. Two routes can reach the same spot, so the copies carried along them could arrive pointing different ways. Going out along one route and home along the other makes a loop. Carrying an arrow home along a route undoes carrying it out along that route. So the copies agree exactly when that loop brings an arrow back matching its start.

The patch has no holes, so that loop can be split into small loops, like a field split into small plots. Two small loops side by side turn an arrow by the sum of their turns, because their shared side is walked once each way and those two trips cancel. In the same way, the big loop turns the arrow by the total of all the small loops' turns. Every small loop gives no turn, so the big loop gives none either.

As a result, copies that reach a spot by different routes agree. Every spot gets one first arrow and one second arrow.

Now draw lines on the ground. Some always run along the first arrows, a centimetre apart. Others always run along the second arrows, also a centimetre apart. The two sets of lines cross at right angles everywhere, because the arrows at each spot do. Take on trust here that the lines close into squares one centimetre on each side. On a small patch, those squares are the squared paper that fits it. A long ribbon-shaped patch that winds around could need paper that overlaps itself when flat.

**Takeaway:** On a patch with no holes where every small loop brings the arrow back matching, copies of two arrows at a right angle agree at every spot. If that patch is also small, lines drawn along those copies make the squared paper.

*Picture:* A coin-shaped patch split into small square plots. Two arrows at a right angle sit at one spot, copies of them sit on every plot, and grid lines run along the copies.

*Continues:* `ways_in/squared-paper-or-small-loops`<br>*Builds on:* [[holonomy]], [[path-dependence-of-parallel-transport]], [[riemann-curvature-tensor]]<br>*See:* `problems/cube-corner`

### 3. A rocket or a planet? · entry · operational

*Does feeling a pull inside a closed cabin show that spacetime there is curved?*

**Recap:** Spacetime is space and time taken together. To fall freely is to move with nothing but gravity acting on you. The Riemann curvature tensor is a table kept at every place. It records how tiny loops turn carried arrows, and it also sets how neighbouring falling objects drift together or apart. Spacetime is flat where every entry of that table is zero, just as ground is flat where every small loop brings the arrow back matching. There, balls let go side by side at the same moment never drift, as long as they are inside a cabin that does not spin.

In "Squared paper or small loops", paper and arrows tested ground. Spacetime is harder, because nobody can walk a loop that goes backward in time. So spacetime needs a test you can do inside a room, with things you let fall.

You wake up in a closed cabin with no windows. The cabin does not spin. You put on a spacesuit and pump out the air, so no air pushes anything you let go. Your feet press on the floor, and a ball you let go of falls to it. Is the cabin resting on Earth, or is it a rocket far out in space, speeding up with its engines on?

One ball cannot tell you. In the rocket, nothing pushes the ball once you let go. A friend floating freely outside would measure it moving on at the steady speed it had when you let go. The floor keeps speeding up, so it catches up with the ball. By a ruler fixed to the cabin, the ball speeds up toward the floor, just as on Earth. A feather and a hammer land together, because the floor catches up with both at once.

Far from every star and planet, spacetime is flat, as far as any measurement can tell. So in the rocket your weight comes from the speeding-up floor, not from curved spacetime.

Now try two balls. Hold them side by side at the same height, one metre apart, and let go of both together.

In the rocket, the floating friend measures both balls moving on at the same steady speed, in the same direction. By the cabin's ruler, their gap therefore stays one metre until the floor reaches them.

On Earth, each ball falls toward Earth's centre, 6,371 kilometres below. Like two spokes of a wheel, their paths lead to the same point, so the balls drift together. The gap between two spokes is in proportion to the distance from the centre. A 20-metre drop therefore shrinks their one-metre gap by 20 parts in 6,371,000. That is about three thousandths of a millimetre, a twentieth of a hair's width, which is why nobody notices.

The rocket cannot copy this drift, because balls let go side by side in it always keep their gap. Where every entry of the Riemann curvature tensor is zero, balls let go side by side never drift. The drift on Earth shows that some entry is not zero, so spacetime around Earth is curved.

**Takeaway:** In a cabin that does not spin, a pull that makes everything fall the same way does not show curved spacetime, but a drift between balls let go side by side does.

*What this leaves out:* Ignores Earth's spin and the balls' pull on each other, both far too small to change the answer.

*Continues:* `ways_in/squared-paper-or-small-loops`<br>*Builds on:* [[riemann-curvature-tensor]]<br>*Visuals:* [[falling-ring-of-crumbs]]<br>*See:* `checks/rocket-drop`

### 4. Constant metric exactly when Riemann vanishes · working · calculation

*In coordinates, what exactly does the flatness criterion claim, and why does each direction hold?*

The squared paper of "Squared paper or small loops" is a coordinate grid in which the metric is the same everywhere. So call a metric flat on an open region $U$ if every point of $U$ has coordinates nearby in which $g_{\mu\nu} = \eta_{\mu\nu}$, or $\delta_{ij}$ for a positive-definite metric. For the Levi-Civita connection, whose Christoffel symbols come from the metric, the criterion reads

$$R^\rho{}_{\sigma\mu\nu} = 0 \text{ on } U \iff g \text{ is flat on } U.$$

*Constant metric gives zero curvature.* In the constant-metric coordinates every derivative of $g_{\mu\nu}$ vanishes, so every $\Gamma^\lambda{}_{\mu\nu}$ vanishes on an open set. Their derivatives vanish there too, so every term of $R^\rho{}_{\sigma\mu\nu}$ is zero. Components in any other coordinates are these components times Jacobian factors, so they vanish too.

The open set matters. At a single event, coordinates can make every $\Gamma$ vanish for any metric, as a freely falling laboratory does. The derivatives $\partial\Gamma$ then survive, and they carry the curvature.

*Zero curvature gives a constant metric.* By the small-loop law, $\Delta V^\rho = -R^\rho{}_{\sigma\mu\nu}V^\sigma a^\mu b^\nu$, every small loop returns vectors unchanged when $R^\rho{}_{\sigma\mu\nu} = 0$. On a region with no holes, transport then depends only on the endpoints, so an orthonormal basis at one point spreads to parallel fields $e_{(a)}$. Their dual covectors are curl-free because $\Gamma^\lambda{}_{\mu\nu} = \Gamma^\lambda{}_{\nu\mu}$, so they are gradients $\partial_\mu X^a$, and in the coordinates $X^a$ the metric is $\eta_{ab}$. The derivation "Zero curvature to a constant metric" takes these steps one at a time.

*Coordinates can hide flatness.* The metric $e^{2u}(du^2 + dv^2)$ has Christoffel symbols that are nonzero and the same everywhere. Yet its Riemann tensor vanishes, and $r = e^u$, $\phi = v$ turn it into the plane's polar form $dr^2 + r^2d\phi^2$, as the worked example "A plane with constant Christoffel symbols" shows. Nonzero Christoffel symbols, and metric coefficients that vary from place to place, never prove curvature by themselves.

**Takeaway:** The Riemann tensor vanishes on a region exactly when coordinates near each point make the metric constant; nonzero Christoffel symbols prove nothing.

*What this leaves out:* Smooth metrics and the Levi-Civita connection only.

*Continues:* `ways_in/squared-paper-or-small-loops`, `ways_in/drawing-squared-paper-with-arrows`<br>*Builds on:* [[flat-metric]], [[christoffel-symbols]], [[riemann-curvature-tensor]]<br>*Visuals:* [[cross-off-matching-terms]]<br>*See:* `derivations/zero-curvature-to-constant-metric`, `worked_examples/plane-with-constant-christoffel-symbols`, `checks/christoffels-vanish-at-one-event`

### 5. Clock rates and acceleration without curvature · working · operational

*Do clocks that tick at different rates at different heights show that spacetime is curved?*

The rocket of "A rocket or a planet?" gave its crew weight in flat spacetime, and its clocks tell the same story. Take a static spacetime with $x^0 = ct$,

$$ds^2 = -N(x)^2c^2dt^2 + dx^2,$$

plus $dy^2 + dz^2$ if you like, which changes no conclusion. A clock held at fixed $x$ has $d\tau = N\,dt$, and static observers comparing light signals find $f_{\rm r}/f_{\rm e} = N(x_{\rm e})/N(x_{\rm r})$. Staying at fixed $x$ takes proper acceleration $c^2N'/N$, toward increasing $N$. The Christoffel symbols are $\Gamma^x{}_{00} = NN'$ and $\Gamma^0{}_{0x} = N'/N$, and the course formula gives

$$R^x{}_{0x0} = N N'',$$

taken on trust here and worked out in the problem "Curvature of a clock-rate profile". In two dimensions this is the only independent component, so the spacetime is flat on a range of $x$ exactly when $N'' = 0$ throughout it.

- A rocket whose floor at $x = 0$ accelerates at $g$ has $N = 1 + gx/c^2$. Compared by light signals, clocks at height $h$ tick faster than floor clocks by the factor $1 + gh/c^2$, and the needed acceleration $g/(1 + gx/c^2)$ changes with height, yet $N'' = 0$: flat.
- If every height needs the same acceleration $g$, then $N'/N = g/c^2$, so $N = e^{gx/c^2}$ and $R^x{}_{0x0} = (g^2/c^4)\,e^{2gx/c^2}$. For $g = 9.81\ \mathrm{m\,s^{-2}}$ that is $1.19\times10^{-32}\ \mathrm{m^{-2}}$ at $x = 0$: tiny, but curved.

So redshift between heights, and the acceleration needed to stay put, decide nothing by themselves; the bending of the clock-rate profile does. In a weak static field $N \approx 1 + \Phi/c^2$, so $R^x{}_{0x0} \approx \Phi''/c^2$, the tidal gradient. At Earth's surface, along the vertical, that is $-2GM/c^2r^3 = -3.43\times10^{-23}\ \mathrm{m^{-2}}$.

**Takeaway:** Clocks ticking at different rates at different heights, and the acceleration needed to stay put, occur in flat spacetime; curvature needs the clock-rate profile to bend.

*What this leaves out:* Static metrics of this one form; a general spacetime needs every Riemann component.

*Continues:* `ways_in/rocket-or-planet`, `ways_in/constant-metric-exactly-when-riemann-vanishes`<br>*Builds on:* [[rindler-coordinates]]<br>*Visuals:* [[lamp-and-detector-in-a-rocket]], [[cross-off-matching-terms]]<br>*See:* `problems/clock-rate-curvature`, `observations/pound-rebka-tower`, `checks/tower-clocks-claim`

### 6. Flat charts from a parallel coframe · formal · structure

*What are the exact hypotheses and equivalent forms of the flatness criterion, and how is it proved?*

The two directions of "Constant metric exactly when Riemann vanishes" become a theorem. Let $(M, g)$ be a smooth $n$-manifold with a metric of signature $(s, n-s)$, Levi-Civita connection $\nabla$ and curvature $\mathcal R(X,Y) = [\nabla_X, \nabla_Y] - \nabla_{[X,Y]}$. Let $U \subseteq M$ be open and connected, and let $\eta$ be diagonal with $s$ entries $-1$ and $n - s$ entries $+1$.

*Theorem.* These are equivalent: (a) $\mathcal R = 0$ on $U$; (b) every point of $U$ lies in a chart with $g_{\mu\nu} = \eta_{\mu\nu}$; (c) every point of $U$ has a neighbourhood with an orthonormal frame $e_a$, $\nabla e_a = 0$; (d) the restricted holonomy group $\mathrm{Hol}^0_p(U)$ is trivial.

*Proof sketch.* (b) $\Rightarrow$ (a): every $\Gamma$ vanishes on an open set, and $\mathcal R$ is a tensor. (a) $\Rightarrow$ (c): on a coordinate ball, sweep one curve into another through cells of holonomy $1 - \epsilon^2\mathcal R(\partial_s, \partial_t) + O(\epsilon^3)$. With $\mathcal R = 0$, transport depends only on endpoints, so an orthonormal basis spreads to a parallel frame, orthonormal because $\nabla g = 0$. (c) $\Rightarrow$ (b): the dual coframe obeys $d\theta^a = -\omega^a{}_b \wedge \theta^b + T^a$. A parallel frame has $\omega^a{}_b = 0$ and the torsion $T^a$ vanishes, so $d\theta^a = 0$. On a ball the Poincaré lemma gives $\theta^a = dx^a$, and then $g = \eta_{ab}\,dx^a dx^b$. (a) $\Leftrightarrow$ (d) repeats the sweep for loops.

*Global form.* If $U$ is simply connected, closed forms on $U$ are exact, so the frame and the functions $x^a$ exist on all of $U$. Together they give a local isometry $D: U \to \mathbb R^n_s$, the developing map, which need not be one-to-one: for $e^{2u}(du^2 + dv^2)$ on the whole $(u, v)$ plane it wraps around the punctured plane infinitely often. If $(M, g)$ is connected, simply connected, geodesically complete and flat, $D$ is an isometry onto $\mathbb R^n_s$, Euclidean or Minkowski space.

*Other connections.* For any connection on $TM$, curvature zero still gives local parallel frames, since the sweep never used symmetry. The coframe step shows that a chart with vanishing connection coefficients exists near each point exactly when both the curvature and the torsion vanish.

**Takeaway:** For the Levi-Civita connection, zero curvature on an open set is equivalent to local charts with constant metric, to local parallel orthonormal frames and to trivial restricted holonomy; global charts need topology and completeness.

*Continues:* `ways_in/constant-metric-exactly-when-riemann-vanishes`<br>*Builds on:* [[levi-civita-connection]], [[simply-connected-space]], [[holonomy]]<br>*See:* `problems/milne-flat`

### 7. Where the criterion stops · formal · contrast

*What does the flatness criterion not say about single points, Ricci curvature, topology and torsion?*

The flat charts of "Flat charts from a parallel coframe" exist near each point of an open set, for the Levi-Civita connection. Four near misses mark the edges of that statement; set $G = c = 1$.

- *One point.* Normal coordinates at any point $p$ give $g_{\mu\nu}(p) = \eta_{\mu\nu}$ and $\partial_\lambda g_{\mu\nu}(p) = 0$ for every metric, leaving $\mathcal R(p)$ untouched. Curvature vanishing only on a curve, as on the top and bottom circles of a doughnut's surface, makes no neighbourhood flat.
- *Ricci.* $R_{\mu\nu} = 0$ forces $R_{\rho\sigma\mu\nu} = 0$ only for $n \le 3$. For $n = 4$ the Weyl part survives: outside a static spherical mass, $R_{\mu\nu} = 0$ while $R^{\hat r}{}_{\hat t\hat r\hat t} = -2M/r^3$.
- *Topology.* A flat cylinder and a flat torus have trivial holonomy but are not $\mathbb R^2$. A cone with its tip removed, made by cutting out a wedge of angle $\delta$, has holonomy generated by the rotation through $\delta$. On a flat Möbius band, a loop along the band returns a reflection. Outside an idealized straight cosmic string whose tension equals its mass per length $\mu$, spacetime is flat with deficit angle $8\pi\mu$.
- *Torsion.* On $dx^2 + e^{-2x}dy^2$, declare the orthonormal frame $e_1 = \partial_x$, $e_2 = e^x\partial_y$ parallel. This metric connection has $\mathcal R = 0$, but its torsion is $T(e_1, e_2) = -[e_1, e_2] = -e_2$, so no chart makes its coefficients vanish. The Levi-Civita connection of the same metric has $K = -1$: the hyperbolic plane.

**Takeaway:** The criterion is about open sets and the Levi-Civita connection; single points, Ricci flatness, global shape and connections with torsion each fall outside it.

*What this leaves out:* Idealizes the cone's tip and the string as an exact point and line.

*Continues:* `ways_in/flat-charts-from-a-parallel-coframe`<br>*Builds on:* [[holonomy]], [[simply-connected-space]]<br>*Visuals:* [[carry-an-arrow-around-a-loop]] (preset `cone-around-tip`)<br>*See:* `checks/ricci-flat-by-dimension`, `checks/cone-torus-verdict`

## Glossary

| Term | Say | In plain words | Concept |
| --- | --- | --- | --- |
| loop | — | A path that ends exactly where it began. | — |
| swing | — | To change which way an arrow points, left or right, while it lies against the ground. The arrow test never lets it swing. | — |
| match | — | Two arrows at one spot match when one lies on top of the other, pointing the same way. | — |
| arrow test | — | Carry a cardboard arrow around a loop, pressed against the ground and never swinging, then compare its direction with its starting direction. | [[holonomy]] |
| flat | — | Ground is flat when, around every spot, squared paper can cover some small patch without stretching or tearing, as on a table top or the side of a can. Spacetime is flat where the Riemann curvature tensor is zero. | [[flat-metric]] |
| flatness criterion | FLAT-ness cry-TEER-ee-un | The rule that a region is flat exactly when its Riemann curvature tensor is zero all over it. For ground, squared paper can cover a small patch with no holes exactly when every small loop on it brings a carried arrow back matching its start. | [[flatness-criterion]] |
| spacetime | — | Space and time taken together as one world with four directions: three of space and one of time. | — |
| fall freely | — | To move with nothing but gravity acting: no air pushing, and no floor, rope or hand holding you. | — |
| Riemann curvature tensor | REE-mahn | A table kept at every place that records how small loops there turn carried arrows. In spacetime it also sets how falling neighbours drift together or apart. | [[riemann-curvature-tensor]] |
| drift | — | A slow change in the gap between two neighbours that were let go together side by side and fall freely. | [[tidal-force]] |
| squared paper | — | Paper printed with a grid of equal squares. | — |
| patch | — | A piece of ground with no holes, such as a coin-shaped piece. | — |
| region | — | A piece of ground, or of spacetime, with room around every spot in it, rather than a single spot. A patch is a region of ground with no holes. | — |

## Key equations

### Flatness criterion · working

$$
R^\rho{}_{\sigma\mu\nu} = 0 \ \text{on } U \iff \text{near each point of } U \text{ some coordinates give } g_{\mu\nu} = \eta_{\mu\nu}
$$

The Riemann tensor vanishes throughout a region exactly when coordinates near each of its points make the metric constant.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $R^\rho{}_{\sigma\mu\nu}$ | Riemann tensor of the metric, in the course convention | the Riemann tensor |
| $U$ | an open region | the region U |
| $\eta_{\mu\nu}$ | the constant diagonal metric with entries $\pm1$ of the same signature; $\delta_{\mu\nu}$ for a positive-definite metric | the constant flat metric |

**Holds when:** Levi-Civita connection of a smooth metric; $U$ open. The coordinates are local; one chart on all of $U$ needs further global conditions.  
**Say it:** “The Riemann tensor is zero everywhere in a region exactly when, near each point, some coordinates make the metric constant.”  
**Justified by:** `derivations/zero-curvature-to-constant-metric`

### Curvature of a static clock-rate profile · working

$$
ds^2 = -N(x)^2c^2dt^2 + dx^2 \;\Rightarrow\; R^x{}_{0x0} = N N''
$$

A position-dependent clock rate curves spacetime only where its profile bends.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $N(x)$ | rate of a static clock at $x$ relative to coordinate time, $d\tau/dt$ | the clock rate N |
| $N''$ | second derivative of $N$ with respect to $x$ | N double prime |
| $R^x{}_{0x0}$ | Riemann component with $x^0 = ct$, in inverse metres squared | R upper x, lower zero x zero |

**Holds when:** Static two-dimensional metric of this form, or with flat $dy^2 + dz^2$ added; $x^0 = ct$.  
**Say it:** “For this metric, the Riemann component R upper x, lower zero x zero, equals N times N double prime.”  
**Justified by:** `stated`

## Derivations

### Zero curvature to a constant metric · working

**Goal:** Show that, for the Levi-Civita connection, $R^\rho{}_{\sigma\mu\nu} = 0$ on a region exactly when coordinates near each point make $g_{\mu\nu}$ constant.

1. If $g_{\mu\nu}$ is constant on an open set, the Christoffel formula gives $\Gamma^\lambda{}_{\mu\nu} = 0$ at every point of that set.
2. A function that is zero on an open set has zero derivatives there, so $\partial_\mu\Gamma^\lambda{}_{\nu\sigma} = 0$, and every term of $R^\rho{}_{\sigma\mu\nu}$ vanishes.
3. Riemann components in other coordinates are these components multiplied by Jacobian factors, so they vanish in every coordinate system.
4. Conversely, let $R^\rho{}_{\sigma\mu\nu} = 0$ on a coordinate ball $B$. Two routes in $B$ with the same ends bound a strip that splits into small cells, and each cell changes a vector by $-R^\rho{}_{\sigma\mu\nu}V^\sigma a^\mu b^\nu = 0$, so transport in $B$ depends only on the endpoints.
5. Pick an orthonormal basis $e_{(a)}$ at one point and transport it everywhere in $B$, giving fields with $\partial_\mu e_{(a)}^\nu + \Gamma^\nu{}_{\mu\lambda}e_{(a)}^\lambda = 0$.
6. Transport preserves inner products, so $g_{\mu\nu}e_{(a)}^\mu e_{(b)}^\nu = \eta_{ab}$ at every point.
7. Define dual covectors by $\theta^{(a)}{}_\nu e_{(b)}^\nu = \delta^a_b$. Differentiating this constant shows $\nabla_\mu\theta^{(a)}{}_\nu = 0$, that is $\partial_\mu\theta^{(a)}{}_\nu = \Gamma^\lambda{}_{\mu\nu}\theta^{(a)}{}_\lambda$.
8. The Levi-Civita connection has $\Gamma^\lambda{}_{\mu\nu} = \Gamma^\lambda{}_{\nu\mu}$, so $\partial_\mu\theta^{(a)}{}_\nu - \partial_\nu\theta^{(a)}{}_\mu = 0$.
9. A curl-free covector field on a ball is a gradient, so $\theta^{(a)}{}_\nu = \partial_\nu X^a$ for functions $X^a$.
10. Use $X^a$ as coordinates. Because $dX^a(e_{(b)}) = \delta^a_b$, the coordinate basis vectors $\partial/\partial X^a$ are the fields $e_{(a)}$, so the metric components are $g(e_{(a)}, e_{(b)}) = \eta_{ab}$.

**Result:** In the coordinates $X^a$ the metric is the constant $\eta_{ab}$ throughout $B$, and every Christoffel symbol vanishes there.

## Worked examples

### A plane with constant Christoffel symbols · working

**Problem:** Decide whether $ds^2 = e^{2u}(du^2 + dv^2)$ describes a flat surface, and if it does, find coordinates that make the metric constant.

1. The components are $g_{uu} = g_{vv} = e^{2u}$, and the only nonzero derivatives are $\partial_u g_{uu} = \partial_u g_{vv} = 2e^{2u}$.
2. The Christoffel formula gives $\Gamma^u{}_{uu} = 1$, $\Gamma^u{}_{vv} = -1$ and $\Gamma^v{}_{uv} = \Gamma^v{}_{vu} = 1$, with the rest zero: nonzero, and the same everywhere.
3. In $R^u{}_{vuv} = \partial_u\Gamma^u{}_{vv} - \partial_v\Gamma^u{}_{uv} + \Gamma^u{}_{u\lambda}\Gamma^\lambda{}_{vv} - \Gamma^u{}_{v\lambda}\Gamma^\lambda{}_{uv}$, both derivative terms vanish because the symbols are constant.
4. The product terms give $\Gamma^u{}_{uu}\Gamma^u{}_{vv} - \Gamma^u{}_{vv}\Gamma^v{}_{uv} = (1)(-1) - (-1)(1) = 0$. In two dimensions this is the only independent component, so the Riemann tensor vanishes.
5. Set $r = e^u$ and $\phi = v$. Then $dr = e^u\,du$, so $dr^2 + r^2d\phi^2 = e^{2u}(du^2 + dv^2)$.
6. Finally $x = r\cos\phi$ and $y = r\sin\phi$ give $dx^2 + dy^2$.

**Answer:** Flat: $x = e^u\cos v$ and $y = e^u\sin v$ make the metric $dx^2 + dy^2$ on the plane without its origin. If $v$ runs over all real numbers, this map wraps around that punctured plane infinitely often.

**Takeaway:** Christoffel symbols can be nonzero, and even constant, on a flat plane; the Riemann tensor decides.

## Problems

### `cube-corner` · entry · difficulty 2 · conceptual

Build a cube from card. At each corner, three square faces meet. (a) Can squared paper cover a small patch around a spot in the middle of an edge, in one layer, without stretching or tearing? (b) Can it cover a small patch around a corner? (c) A tiny walker carries a cardboard arrow once around a small loop that circles a corner, crossing all three faces there. Does the arrow come back matching its start?

**Hints**

1. At the corner, add up the angles of the three squares that meet there.
2. Cut along one edge that leads to the corner and lay the three squares flat around it. What gap is left?

**Answer:** (a) Yes. (b) No, because the three squares around a corner fill only three quarters of a turn. (c) No: the arrow comes back turned a quarter turn.

**Must contain:** Paper bends sharply over an edge without stretching, so edges pass the paper test; Three right angles leave a quarter turn missing at a corner; The arrow comes back a quarter turn from its start, so both tests fail at the corner

**Numeric:** turn of the returned arrow = 90 deg (magnitude, ±5)

**Solution**

1. Along an edge, two flat faces meet. Paper bent sharply along the edge lies against both faces in one layer, so a patch around a spot on the edge can be covered.
2. At a corner, three squares meet, each with a right angle there. Together their angles make three quarters of a turn.
3. Flat paper has a full turn of angle around every spot. To lie against the corner in one layer, it would need a quarter-turn wedge cut out, which is tearing. So no patch around a corner can be covered.
4. Cut the cube along one edge that leads to the corner, and lay the three squares flat on a table. They leave a quarter-turn gap between the two sides of the cut.
5. On the flat squares the arrow never swings, so it keeps pointing the same way as the walker goes from one side of the gap to the other.
6. Folding the squares back into the cube closes the gap, and that turns one side of the cut onto the other by a quarter turn. So the arrow comes back a quarter turn from its start.
7. The two tests agree, as the flatness criterion says: both pass on the faces and edges, and both fail at a corner.

### `clock-rate-curvature` · working · difficulty 2 · derivation

For $ds^2 = -N(x)^2c^2dt^2 + dx^2$ with $x^0 = ct$: (a) find the nonzero Christoffel symbols; (b) show that $R^x{}_{0x0} = NN''$; (c) find every $N$ for which the spacetime is flat; (d) for $N = e^{gx/c^2}$ with $g = 9.81\ \mathrm{m\,s^{-2}}$, evaluate $R^x{}_{0x0}$ at $x = 0$.

**Hints**

1. Only $g_{00} = -N^2$ depends on $x$, and $g^{00} = -1/N^2$.
2. Use the course formula with $\rho = x$, $\sigma = 0$, $\mu = x$, $\nu = 0$; one product term survives.

**Answer:** $\Gamma^x{}_{00} = NN'$ and $\Gamma^0{}_{0x} = \Gamma^0{}_{x0} = N'/N$; $R^x{}_{0x0} = NN''$; flat exactly when $N = A + Bx$; for the exponential profile $R^x{}_{0x0}(0) = g^2/c^4 = 1.19\times10^{-32}\ \mathrm{m^{-2}}$.

**Must contain:** Gamma x zero zero equals N N prime, and Gamma zero zero x equals N prime over N; The derivative term gives N prime squared plus N N double prime, and one product term cancels the N prime squared; Flat exactly for linear N, including the accelerating rocket; The exponential profile gives about 1.19 times ten to the minus 32 per metre squared

**Numeric:** Riemann component at x equal to zero for the exponential profile = 1.19e-32 m^-2 (signed, ±2%)

**Solution**

1. $\Gamma^x{}_{00} = -\tfrac12 g^{xx}\partial_x g_{00} = -\tfrac12\partial_x(-N^2) = NN'$.
2. $\Gamma^0{}_{0x} = \tfrac12 g^{00}\partial_x g_{00} = \tfrac12(-1/N^2)(-2NN') = N'/N$. The others vanish, because nothing depends on $t$ and $g_{xx} = 1$.
3. $R^x{}_{0x0} = \partial_x\Gamma^x{}_{00} - \partial_0\Gamma^x{}_{x0} + \Gamma^x{}_{x\lambda}\Gamma^\lambda{}_{00} - \Gamma^x{}_{0\lambda}\Gamma^\lambda{}_{x0}$.
4. The first term is $N'^2 + NN''$. The second and third vanish because $\Gamma^x{}_{x0} = \Gamma^x{}_{xx} = 0$. The fourth is $-\Gamma^x{}_{00}\Gamma^0{}_{x0} = -N'^2$.
5. So $R^x{}_{0x0} = NN''$. In two dimensions this is the only independent component, so the spacetime is flat exactly when $N'' = 0$, that is $N = A + Bx$.
6. For $N = e^{gx/c^2}$, $NN'' = (g^2/c^4)e^{2gx/c^2}$, which at $x = 0$ is $9.81^2/(2.998\times10^8)^4 = 1.19\times10^{-32}\ \mathrm{m^{-2}}$.

**Targets:** `redshift-proves-curvature`

### `milne-flat` · formal · difficulty 2 · proof

With $G = c = 1$, take $ds^2 = -dt^2 + a(t)^2d\chi^2$ for $t > 0$. (a) Show that $R^\chi{}_{t\chi t} = -\ddot a/a$. (b) For $a = t$, find coordinates in which the metric is $-dT^2 + dX^2$, and name the region of the $(T, X)$ plane they cover. (c) Is the metric with $a = t^{2/3}$ flat?

**Hints**

1. $\Gamma^t{}_{\chi\chi} = a\dot a$ and $\Gamma^\chi{}_{t\chi} = \Gamma^\chi{}_{\chi t} = \dot a/a$.
2. Try $T = t\cosh\chi$ and $X = t\sinh\chi$.

**Answer:** $R^\chi{}_{t\chi t} = -\ddot a/a$. For $a = t$ it vanishes, and $T = t\cosh\chi$, $X = t\sinh\chi$ give $-dT^2 + dX^2$ on the wedge $T > |X|$. For $a = t^{2/3}$, $R^\chi{}_{t\chi t} = 2/(9t^2) \neq 0$, so that metric is curved.

**Must contain:** R upper chi, lower t chi t, equals minus a double dot over a; The linear scale factor gives zero curvature, and the hyperbolic substitution gives the Minkowski form; The chart covers the inside of the future light cone of the origin; The two-thirds power law gives nonzero curvature

**Solution**

1. The nonzero Christoffel symbols are $\Gamma^t{}_{\chi\chi} = a\dot a$ and $\Gamma^\chi{}_{t\chi} = \Gamma^\chi{}_{\chi t} = \dot a/a$.
2. $R^\chi{}_{t\chi t} = \partial_\chi\Gamma^\chi{}_{tt} - \partial_t\Gamma^\chi{}_{\chi t} + \Gamma^\chi{}_{\chi\lambda}\Gamma^\lambda{}_{tt} - \Gamma^\chi{}_{t\lambda}\Gamma^\lambda{}_{\chi t} = 0 - (\ddot a/a - \dot a^2/a^2) + 0 - \dot a^2/a^2 = -\ddot a/a$.
3. In two dimensions this is the only independent component. For $a = t$, $\ddot a = 0$, so the curvature vanishes on the whole simply connected region $t > 0$.
4. With $T = t\cosh\chi$ and $X = t\sinh\chi$, $dT = \cosh\chi\,dt + t\sinh\chi\,d\chi$ and $dX = \sinh\chi\,dt + t\cosh\chi\,d\chi$.
5. Then $-dT^2 + dX^2 = -dt^2 + t^2d\chi^2$: the cross terms cancel and $\cosh^2\chi - \sinh^2\chi = 1$.
6. The inverse map $t = \sqrt{T^2 - X^2}$, $\chi = \operatorname{artanh}(X/T)$ is one-to-one onto $T > |X|$, the inside of the future light cone of the origin. This expanding model is a patch of flat spacetime.
7. For $a = t^{2/3}$, $\ddot a/a = -2/(9t^2)$, so $R^\chi{}_{t\chi t} = 2/(9t^2) \neq 0$ and the metric is curved.

## Observations

- **The frequency shift of gamma rays sent up and down a 22.5 m tower, measured by Pound and Rebka** (measured, working). Light climbing a height $h$ arrives with fractional frequency shift $-gh/c^2$. Static observers in the flat rocket metric $N = 1 + gx/c^2$ find the same shift to this order, so the measurement confirms the clock-rate difference but cannot by itself show that spacetime near Earth is curved. *Numbers:* $gh/c^2 = 2.46\times10^{-15}$ for $h = 22.5$ m; the measured shift agreed with the prediction within its uncertainty of about 10 percent. *Reference:* R. V. Pound, G. A. Rebka Jr. (1960), *Apparent Weight of Photons*, Physical Review Letters 4, 337–341, doi:10.1103/PhysRevLett.4.337
- **The vertical gradient of Earth's gravity, measured by comparing two freely falling clouds of atoms** (measured, working). Two laser-cooled atom clouds at different heights fall freely, and the difference of their accelerations per unit separation is $-c^2R^z{}_{0z0}$. A nonzero value is a nonzero Riemann component, so it shows directly that spacetime near Earth is not flat. *Numbers:* Spherical Earth: $2GM/r^3 = 3.08\times10^{-6}\ \mathrm{s^{-2}}$ at the surface, so $R^z{}_{0z0} = -3.43\times10^{-23}\ \mathrm{m^{-2}}$. *Reference:* M. J. Snadden, J. M. McGuirk, P. Bouyer, K. G. Haritos, M. A. Kasevich (1998), *Measurement of the Earth's Gravity Gradient with an Atom Interferometer-Based Gravity Gradiometer*, Physical Review Letters 81, 971–974, doi:10.1103/PhysRevLett.81.971

## Teaching arc

1. **Test flat ground two ways** (entry). Press a paper square onto a can and an orange, then run the arrow test on both. *Why:* The criterion becomes the agreement of two checks the learner can picture. *Predict:* Can a stamp-sized square of paper lie perfectly against a ball? *Visual:* [[paper-rolled-into-a-tube-and-a-cone]] *Uses:* `ways_in/squared-paper-or-small-loops`, `ways_in/drawing-squared-paper-with-arrows`, `checks/shrink-the-patch`
2. **Rocket or planet** (entry). Drop two balls side by side in a rocket and on Earth after a prediction. *Why:* It separates a pull, which flat spacetime can fake, from a drift, which it cannot. *Predict:* In the speeding-up rocket, do two balls let go side by side land closer together than they started? *Visual:* [[falling-ring-of-crumbs]] *Uses:* `ways_in/rocket-or-planet`, `checks/rocket-drop`
3. **Unmask a disguised plane** (working). Compute the curvature of a metric whose Christoffel symbols are nonzero everywhere. *Why:* Seeing the terms cancel ends reading curvature from Christoffel symbols. *Predict:* Every Christoffel symbol here is nonzero. Is the surface curved? *Visual:* [[cross-off-matching-terms]] *Uses:* `ways_in/constant-metric-exactly-when-riemann-vanishes`, `worked_examples/plane-with-constant-christoffel-symbols`, `checks/which-surfaces-are-flat`
4. **Clocks without curvature** (working). Bend the clock-rate profile; curvature appears only when the profile stops being straight. *Why:* It ties the criterion to measured redshift and tides. *Predict:* If clocks at the top of a tower tick faster, must spacetime there be curved? *Visual:* [[lamp-and-detector-in-a-rocket]] *Uses:* `ways_in/clock-rates-without-curvature`, `checks/tower-clocks-claim`, `observations/pound-rebka-tower`
5. **Prove it and mark its edges** (formal). Prove the theorem with a parallel coframe, then test it on the cone, the torus and a connection with torsion. *Why:* Graduate readers need each hypothesis tied to a counterexample. *Visual:* [[carry-an-arrow-around-a-loop]] (preset `cone-around-tip`) *Uses:* `ways_in/flat-charts-from-a-parallel-coframe`, `ways_in/where-the-criterion-stops`, `checks/cone-torus-verdict`

## Misconceptions

### “A small enough patch of a ball is flat.” · entry · `tiny-patch-is-flat`

- **Why it is tempting:** A stamp stuck on a football looks as if it lies perfectly.
- **What is true:** However small the patch, a small loop around a piece of it brings a carried arrow back turned a little. So squared paper can never cover it exactly.
- **Exposed by:** `checks/shrink-the-patch`

### “If things fall to the floor, spacetime there must be curved.” · entry · `pull-means-curved`

- **Why it is tempting:** Gravity is famous for curving spacetime, and falling is what gravity does.
- **What is true:** A rocket speeding up far from every star makes things fall too, with no curving at all. What shows curving is a drift between balls let go side by side, inside a cabin that does not spin.
- **Exposed by:** `checks/rocket-drop`

### “Nonzero Christoffel symbols, or metric coefficients that vary from place to place, mean the space is curved.” · working · `christoffels-mean-curvature`

- **Why it is tempting:** In Cartesian coordinates on a plane the symbols vanish and the coefficients are constant.
- **What is true:** Both depend on the coordinates, and the plane in polar coordinates has nonzero symbols. Only the Riemann tensor decides.
- **Exposed by:** `checks/which-surfaces-are-flat`

### “Clocks ticking at different rates at different heights prove that spacetime is curved.” · working · `redshift-proves-curvature`

- **Why it is tempting:** Gravitational redshift is a famous prediction of general relativity.
- **What is true:** A rocket accelerating in flat spacetime shows the same redshift. Curvature needs the clock-rate profile to bend, which shows up as tides.
- **Exposed by:** `checks/tower-clocks-claim`

### “Where coordinates make every Christoffel symbol vanish at an event, spacetime is flat there.” · working · `zero-christoffels-at-an-event-mean-flat`

- **Why it is tempting:** The equivalence principle is often summed up as spacetime being flat in a small falling laboratory.
- **What is true:** Such coordinates exist at one event for every metric, and the derivatives of the symbols survive in the Riemann tensor.
- **Exposed by:** `checks/christoffels-vanish-at-one-event`

### “Where the Ricci tensor vanishes, spacetime is flat.” · formal · `ricci-flat-means-flat`

- **Why it is tempting:** The vacuum field equation sets the Ricci tensor to zero, and both tensors are called curvature.
- **What is true:** In four dimensions the Weyl part of the Riemann tensor survives, as outside any star. Ricci flatness implies flatness only in two or three dimensions.
- **Exposed by:** `checks/ricci-flat-by-dimension`

### “If the Riemann tensor vanishes everywhere, one constant-metric chart covers the whole space and every loop returns vectors unchanged.” · formal · `one-flat-grid-everywhere`

- **Why it is tempting:** Short statements of the criterion leave out that it is local.
- **What is true:** The criterion gives such charts only near each point. A flat torus has no single one, and a loop around a cone's missing tip rotates vectors.
- **Exposed by:** `checks/cone-torus-verdict`

## Checks

1. **Entry · explain** `checks/shrink-the-patch`. On a huge smooth ball, you press a square of squared paper 2 centimetres across against the ground. A friend says that such a tiny square lies against the ball perfectly, in one layer, without stretching or tearing. Is the friend exactly right? Use the arrow test to explain.
   - **Hints:** What does a small loop on a ball do to a carried arrow?
   - **Answer:** No, not exactly. Suppose the square did lie perfectly. Then an arrow carried around any loop drawn on it would keep its angle to the printed lines, so it would come back matching its start. But on a ball, a small loop around a piece of the ball brings a carried arrow back turned a little, even a loop small enough to fit on the square. So the square cannot lie perfectly, and no patch of a ball, however tiny, can be covered exactly. For a patch this small the turn is far too small to see, which is why the claim looks true.
   - **Must contain:** Not exactly; Paper that fits would make every loop on it bring the arrow back matching; A small loop on a ball still brings the arrow back turned a little
   - **Targets:** `tiny-patch-is-flat`
2. **Entry · numeric** `checks/rocket-drop`. A rocket far from every star and planet is speeding up with its engines on. Its cabin does not spin and has no air. You hold two balls side by side at the same height, 2 metres apart, and let go of both together. By a ruler fixed to the cabin, they fall 3 metres before the floor reaches them. By that ruler, how far apart are they when they land? Would a cabin resting on Earth, with the same drop, give exactly the same answer?
   - **Hints:** After you let go, does anything push either ball in the rocket? / On Earth, where do the balls' paths point?
   - **Answer:** They land 2 metres apart. Once you let go, nothing pushes either ball. So a friend floating freely outside measures both moving on at the same steady speed, in the same direction. The floor reaches both together, and their gap never changes. On Earth, each ball falls toward Earth's centre, 6,371 kilometres below. Their paths lead to the same point, like two spokes of a wheel, so the gap is in proportion to the distance from the centre. A 3-metre drop shrinks the 2-metre gap by 3 parts in 6,371,000 of itself. That is 6 metres divided by 6,371,000, about one millionth of a metre, or one thousandth of a millimetre. So the answers differ. Where every entry of the Riemann curvature tensor is zero, balls let go side by side never drift, so only the cabin on Earth shows curved spacetime.
   - **Must contain:** In the rocket the balls land 2 metres apart; Nothing pushes the released balls, so their gap stays the same; On Earth the gap shrinks by about one thousandth of a millimetre, which shows curving
   - **Numeric:** gap on landing in the rocket = 2 m (magnitude, ±0.01); shrinking of the gap on Earth = 9.4e-07 m (magnitude, ±5%)
   - **Targets:** `pull-means-curved`
   - **Visual:** [[falling-ring-of-crumbs]]
3. **Working · explain** `checks/which-surfaces-are-flat`. For $ds^2 = dr^2 + f(r)^2d\phi^2$ with $r > 0$, the course formula gives $R^r{}_{\phi r\phi} = -ff''$, while $\Gamma^r{}_{\phi\phi} = -ff'$ and $\Gamma^\phi{}_{r\phi} = f'/f$ are nonzero whenever $f' \neq 0$. Which of $f = r + 3$ and $f = \sinh r$ gives a flat surface, and what is it?
   - **Hints:** Compute $f''$ for each choice.
   - **Answer:** $f = r + 3$ has $f'' = 0$, so $R^r{}_{\phi r\phi} = 0$ and the surface is flat, although $\Gamma^r{}_{\phi\phi} = -(r + 3)$ and $\Gamma^\phi{}_{r\phi} = 1/(r + 3)$ are nonzero. With $\rho = r + 3$ the metric becomes $d\rho^2 + \rho^2d\phi^2$ with $\rho > 3$: the plane in polar coordinates, outside a disk of radius 3. $f = \sinh r$ gives $R^r{}_{\phi r\phi} = -\sinh^2 r \neq 0$, and Gaussian curvature $-f''/f = -1$, so that surface is curved.
   - **Must contain:** Flatness is decided by f double prime, not by the Christoffel symbols; r plus 3 gives the flat plane outside a disk; sinh r gives a curved surface with Gaussian curvature minus one
   - **Targets:** `christoffels-mean-curvature`
   - **Visual:** [[cross-off-matching-terms]]
4. **Working · evaluate-claim** `checks/tower-clocks-claim`. Light sent up a 22.5 m tower arrives with fractional frequency shift $-gh/c^2$. A student says: "This measured redshift proves that spacetime near Earth is curved." Compute the shift, and evaluate the claim using $ds^2 = -(1 + gx/c^2)^2c^2dt^2 + dx^2$.
   - **Hints:** Compute $N''$ for the given metric.
   - **Answer:** $gh/c^2 = 9.81 \times 22.5/(2.998\times10^8)^2 = 2.46\times10^{-15}$, so the shift is $-2.46\times10^{-15}$. The given metric has $N = 1 + gx/c^2$, so $N'' = 0$ and $R^x{}_{0x0} = NN'' = 0$: it is a rocket in flat spacetime. Its static observers find $f_{\rm r}/f_{\rm e} = 1/(1 + gh/c^2)$, the same shift to this order. So the redshift alone cannot prove curvature. The tidal gradient, $R^z{}_{0z0} = -3.43\times10^{-23}\ \mathrm{m^{-2}}$ at Earth's surface, does.
   - **Must contain:** The shift is about minus 2.46 times ten to the minus 15; The rocket metric has zero curvature and gives the same shift; Only a tidal gradient shows curvature
   - **Numeric:** fractional frequency shift = -2.46e-15 1 (signed, ±2%)
   - **Targets:** `redshift-proves-curvature`
5. **Working · evaluate-claim** `checks/christoffels-vanish-at-one-event`. A student sets up freely falling coordinates in which every $\Gamma^\lambda{}_{\mu\nu}$ vanishes at one event near Earth. The student concludes: "The Riemann tensor is built from Christoffel symbols, so it vanishes at that event, and spacetime is flat there." Evaluate the claim.
   - **Hints:** Which terms of the Riemann tensor contain no derivatives?
   - **Answer:** The claim is wrong. $R^\rho{}_{\sigma\mu\nu}$ contains derivatives of $\Gamma$ as well as products of $\Gamma$. At the event the products vanish, but the derivatives depend on $\Gamma$ at neighbouring events, where it is not zero. So there $R^\rho{}_{\sigma\mu\nu} = \partial_\mu\Gamma^\rho{}_{\nu\sigma} - \partial_\nu\Gamma^\rho{}_{\mu\sigma}$, which near Earth includes $R^z{}_{0z0} = -3.43\times10^{-23}\ \mathrm{m^{-2}}$. Such coordinates exist at one event for every metric. Flatness needs $\Gamma = 0$ on an open region, which forces the derivatives to vanish too.
   - **Must contain:** Only the product terms vanish at the event; The derivative terms survive and carry the curvature; Flatness needs vanishing curvature on a region, not at a point
   - **Targets:** `zero-christoffels-at-an-event-mean-flat`
6. **Formal · explain** `checks/ricci-flat-by-dimension`. In which dimensions does $R_{\mu\nu} = 0$ on an open set imply that the metric is flat there? Give the reason, and a four-dimensional counterexample with a nonzero component.
   - **Hints:** Count independent Riemann components in three dimensions and compare with the Ricci tensor.
   - **Answer:** In $n = 2$, $R_{\rho\sigma\mu\nu} = \tfrac12 R\,(g_{\rho\mu}g_{\sigma\nu} - g_{\rho\nu}g_{\sigma\mu})$, so $R_{\mu\nu} = 0$ gives $R = 0$ and then $R_{\rho\sigma\mu\nu} = 0$. In $n = 3$ the Riemann tensor is an algebraic function of $R_{\mu\nu}$ and $g_{\mu\nu}$: both have 6 independent components, and the Weyl tensor vanishes identically. So Ricci-flat implies flat for $n \le 3$. For $n \ge 4$ the Weyl tensor carries independent components. Outside a static spherical mass, $R_{\mu\nu} = 0$, yet in a static orthonormal frame $R^{\hat r}{}_{\hat t\hat r\hat t} = -2M/r^3$; at the Sun's surface, restoring SI, $-2GM_\odot/c^2R_\odot^3 = -8.8\times10^{-24}\ \mathrm{m^{-2}}$.
   - **Must contain:** In two and three dimensions the Ricci tensor determines the Riemann tensor; From four dimensions on, the Weyl tensor is independent; The vacuum outside a star is Ricci-flat but has a nonzero radial tidal component
   - **Numeric:** radial tidal component at the Sun's surface = -8.77e-24 m^-2 (signed, ±3%)
   - **Targets:** `ricci-flat-means-flat`
7. **Formal · evaluate-claim** `checks/cone-torus-verdict`. Evaluate: "The flat torus and the cone with its tip removed both have $\mathcal R = 0$, so each is isometric to an open subset of $\mathbb R^2$, and transport around every loop on them is trivial."
   - **Hints:** Which loops on each surface cannot be shrunk to a point?
   - **Answer:** Both parts fail globally, though the local statements hold: by the criterion, every point of each surface has a neighbourhood isometric to a disk in $\mathbb R^2$. The flat torus is compact, and a nonempty open subset of $\mathbb R^2$ never is, so no isometry onto one exists; its holonomy is trivial, because the parallel frame $\partial_x, \partial_y$ of the plane passes to the quotient. The punctured cone, made by removing a wedge of angle $\delta$ with $0 < \delta < 2\pi$, is not simply connected. A loop winding once around the missing tip returns vectors rotated by $\delta$, so it is not isometric to any open subset of $\mathbb R^2$, where every loop has trivial holonomy. Zero curvature guarantees trivial holonomy only for loops that shrink to a point within the flat region.
   - **Must contain:** Local isometry to the plane holds near every point; The torus is compact, so it is not an open subset of the plane, though its holonomy is trivial; The punctured cone has holonomy generated by the rotation through the wedge angle
   - **Targets:** `one-flat-grid-everywhere`
   - **Visual:** [[carry-an-arrow-around-a-loop]] (preset `cone-around-tip`)

## Notation traps

| Issue | Course choice | Variants you will meet |
| --- | --- | --- |
| Which R must vanish | $R$ alone is the Ricci scalar $g^{\mu\nu}R_{\mu\nu}$. Flatness needs the full Riemann tensor, $R^\rho{}_{\sigma\mu\nu} = 0$. | Some texts write "$R = 0$" for a vanishing Riemann tensor, which is easily read as a zero Ricci scalar, a much weaker condition. |
| Sign and slot order when checking a component by hand | $R^\rho{}_{\sigma\mu\nu} = \partial_\mu\Gamma^\rho{}_{\nu\sigma} - \partial_\nu\Gamma^\rho{}_{\mu\sigma} + \Gamma^\rho{}_{\mu\lambda}\Gamma^\lambda{}_{\nu\sigma} - \Gamma^\rho{}_{\nu\lambda}\Gamma^\lambda{}_{\mu\sigma}$, which gives $R^x{}_{0x0} = NN''$ for the clock-rate metric. | Some texts reverse the overall sign or the slot order. Whether the tensor vanishes never depends on these choices, but the sign of a nonzero component does. |

## Visuals

- ★ [[paper-rolled-into-a-tube-and-a-cone]] (flagship): The paper test beside the arrow test. *Sketch:* This concept adds a ball and a cube corner. Readouts give the stretch squared paper needs at a chosen spot and the turn of a small loop there: both zero on the tube and the cone's side, both nonzero on the ball, the cone's tip and the corner.
- [[carry-an-arrow-around-a-loop]] (core): Flat floor, tube and cone controls for the small-loop test. *Sketch:* Cut a wedge of adjustable angle from a flat sheet and glue it into a cone. Loops that avoid the tip return the arrow unchanged; a loop around the tip returns it rotated by the wedge angle.
- [[falling-ring-of-crumbs]] (core): Rocket or planet: balls dropped side by side. *Sketch:* This concept adds a windowless cabin that switches between a rocket speeding up far from every mass and a room on a planet. Two balls dropped side by side land the same distance apart in the rocket and, with the change magnified, closer on the planet.
- [[lamp-and-detector-in-a-rocket]] (core): Redshift without curvature. *Sketch:* This concept adds a plot of clock rate against height that the learner bends, with readouts of the floor-to-ceiling frequency ratio, the acceleration needed at each height, and the curvature component, zero whenever the plot is straight.
- [[cross-off-matching-terms]] (supporting): Christoffel terms cancelling for disguised flat metrics. *Sketch:* This concept adds the log-polar plane, whose Christoffel symbols are constant and nonzero, and the clock-rate metric with a profile the learner bends.

## Tutor moves

**Open with**

- Picture a square of paper and an orange. Can you press the paper onto the peel so that it lies against it everywhere, in one layer, without stretching or tearing it? What do you predict? *(prediction)*
- In a closed cabin with no windows, a ball you let go of falls to the floor. Could the cabin be a rocket speeding up far out in space? What experiment would tell you? *(prediction)*

**If the learner is stuck**

- *The learner cannot see why paper that fits makes the arrow come back matching.* → Draw a loop and a few arrows on a sheet, roll it into a tube, then unroll it: on the flat sheet every arrow keeps its angle to the printed lines. *Uses:* `ways_in/squared-paper-or-small-loops`
- *A flat metric gives the learner a nonzero Riemann component.* → Check the sign convention, then redo the constant-Christoffel plane term by term. *Uses:* `worked_examples/plane-with-constant-christoffel-symbols`, `notation_traps/sign-in-component-checks`

**Common questions**

- *Is the spacetime around us flat?* (entry) Not exactly. Near Earth, two balls let go side by side drift together by a tiny amount. A rocket speeding up in empty space cannot copy that drift, as long as its cabin does not spin. So spacetime around Earth is curved. The drift is so small that only sensitive instruments measure it, such as ones that compare two falling clouds of atoms. *Uses:* `ways_in/rocket-or-planet`, `observations/atom-gradiometer`
- *Is a football pitch exactly flat?* (entry) Not exactly, even ignoring hills, because Earth's ground is nearly a smooth round ball. On such a ball, a small loop that never crosses itself turns a carried arrow, in full turns, by twice the fraction of the ball on your left. A pitch covers about 14 parts in a million million of Earth's surface. So an arrow carried around it turns by about one hundred-millionth of a degree. That is the angle across a hair's width seen from 400 kilometres away, so no ruler or protractor could show it. *Uses:* `ways_in/squared-paper-or-small-loops`, `checks/shrink-the-patch`
- *Is a uniform gravitational field flat?* (working) It depends on what is uniform. A rigid rocket in flat spacetime has $N = 1 + gx/c^2$, so its upper floors need slightly less acceleration. If every height needs the same acceleration, $N = e^{gx/c^2}$ and $R^x{}_{0x0} \neq 0$. A real planet adds tides either way. *Uses:* `ways_in/clock-rates-without-curvature`, `problems/clock-rate-curvature`

**Switching levels**

- To working when: writes down a metric in unusual coordinates; asks how to check flatness by calculation. Go to the two directions of the criterion and the constant-Christoffel plane. *Uses:* `ways_in/constant-metric-exactly-when-riemann-vanishes`, `worked_examples/plane-with-constant-christoffel-symbols`
- To formal when: asks for the hypotheses or a proof; mentions torsion, topology or Ricci-flat spaces. Prove the theorem with a parallel coframe, then mark its edges. *Uses:* `ways_in/flat-charts-from-a-parallel-coframe`, `ways_in/where-the-criterion-stops`
- To research when: asks about flat universes, gravity in three dimensions, or teleparallel gravity. Open the research horizon. *Uses:* `research_horizon/flat-manifolds-and-the-shape-of-space`, `research_horizon/gravity-in-three-dimensions`

**Pronunciations:** Riemann → REE-mahn; Christoffel → kris-TOFF-el; Levi-Civita → LEH-vee CHEE-vee-tah; Rindler → RIND-ler; Poincaré → pwan-kah-RAY; Bieberbach → BEE-ber-bahk; Rebka → REB-kuh; Möbius → MUR-bee-us

**Voice notes:** Say "the full Riemann tensor is zero", never "R is zero".

## History

- **Bernhard Riemann (1861).** In an essay submitted to the Paris Academy, gave the vanishing of certain four-index combinations of a metric's derivatives as the condition for it to be transformable to constant coefficients. The essay was published in 1876, after his death.
- **Elwin Bruno Christoffel, Rudolf Lipschitz (1869).** Independently studied when two quadratic differential forms are related by a change of variables. Christoffel introduced his three-index symbols and the four-index expressions whose vanishing marks a flat form. Elwin Bruno Christoffel (1869), *Ueber die Transformation der homogenen Differentialausdrücke zweiten Grades*, Journal für die reine und angewandte Mathematik 70, 46–70, doi:10.1515/crll.1869.70.46
- **Tullio Levi-Civita (1917).** Defined parallel transport and used vectors carried around small closed circuits to give Riemann's curvature a geometric meaning. Tullio Levi-Civita (1917), *Nozione di parallelismo in una varietà qualunque e conseguente specificazione geometrica della curvatura riemanniana*, Rendiconti del Circolo Matematico di Palermo 42, 173–204, doi:10.1007/BF03014898

## Research horizon

- **Flat manifolds and the shape of space.** A complete flat Riemannian manifold is Euclidean space divided by a group of isometries acting freely and properly discontinuously, and Bieberbach's theorems show that the compact ones are finitely covered by flat tori. A spatially flat universe could therefore close up like a torus, and maps of the cosmic microwave background are searched for the repeated patterns such a shape would leave. Ludwig Bieberbach (1911), *Über die Bewegungsgruppen der Euklidischen Räume*, Mathematische Annalen 70, 297–336, doi:10.1007/BF01564500; Marc Lachièze-Rey, Jean-Pierre Luminet (1995), *Cosmic topology*, Physics Reports 254, 135–214, doi:10.1016/0370-1573(94)00085-H
- **Gravity in three spacetime dimensions.** In three spacetime dimensions the Riemann tensor is fixed by the Ricci tensor, so Einstein's equation makes spacetime flat wherever there is no matter. Point particles leave conical deficit angles, and the dynamics lives in holonomies around them. The theory can be written as a gauge theory and is exactly soluble as a quantum theory. Stanley Deser, Roman Jackiw, Gerard 't Hooft (1984), *Three-dimensional Einstein gravity: dynamics of flat space*, Annals of Physics 152, 220–235, doi:10.1016/0003-4916(84)90085-X; Edward Witten (1988), *2+1 dimensional gravity as an exactly soluble system*, Nuclear Physics B 311, 46–78, doi:10.1016/0550-3213(88)90143-5
- **Teleparallel gravity.** Teleparallel formulations replace the Levi-Civita connection with a metric connection of zero curvature and nonzero torsion, the case the criterion excludes. Their teleparallel equivalent of general relativity has the same field equations as Einstein's theory, and modified versions are studied in cosmology. Ruben Aldrovandi, José Geraldo Pereira (2013), *Teleparallel Gravity: An Introduction*, Springer, Dordrecht (Fundamental Theories of Physics 173), doi:10.1007/978-94-007-5143-9

## Review: novice

**Verdict:** fixed (2026-09-13, revision 9)

**Retell attempt:** If you can press squared paper onto something without stretching or tearing it, it counts as flat, even a can, which looks bent. A football is not flat. The arrow test gives the same answer: on flat stuff, small loops bring the arrow back matching. I sort of get why paper makes the arrow match, because the angles are the same, but I don't see why the paper counts as flat when it's wrapped round the can. I got lost in the part going the other way, with arrow copies everywhere and lines closing into squares. A football pitch is not exactly flat, but I don't see where the one hundred-millionth of a degree comes from. For spacetime: in a closed cabin you can't tell a rocket from Earth with one ball, but two balls side by side drift together on Earth and not in the rocket, so Earth's spacetime is curved. I wasn't sure why the rocket not copying it proves curving, or what 'fall together' means, since the balls on Earth also fall together. And what does a table of zeros have to do with paper?

Second full novice pass, 2026-09-13, reading revision 5 cold: Flat means you can press squared paper onto it without stretching or tearing, and the arrow test agrees, because on flat ground small loops bring the arrow back matching. The side of a can counts as flat even though it looks bent, and a football does not. The second way builds the paper out of the arrows, and I mostly followed it, except that 'out along one route and home along the other' came out of nowhere: I had to go back and work out for myself that there were two routes to the same spot. The cube corner made sense, because three right angles leave a quarter turn missing. For spacetime, one ball cannot tell a rocket from Earth, since the floor catches up with it, but two balls let go side by side drift together on Earth and not in the rocket, so Earth's spacetime is curved, by about three thousandths of a millimetre over a 20-metre drop. I stopped at the summary, though: it talks about paper and loops and then says 'So a region is flat exactly when its Riemann curvature tensor is zero', and nothing had told me the tensor has anything to do with loops. I also wondered how I was awake in a cabin whose air had been pumped out, and whether a 'region' is the same thing as a 'patch'.

**Stumbles (25)**

- “Ground or spacetime is flat exactly where small loops bring carried arrows back matching”: 'Exactly where' reads as a claim about single spots, while the criterion is about regions; the tagline also names two settings at once.
- “The flatness criterion says that a region is flat exactly when its Riemann curvature tensor is zero all over it.”: 'Region' appears beside 'patch' with no link from the paper sentence to the table sentence, so the reader cannot see why the second follows from the first.
- “only a drift between falling neighbours shows curving”: 'Only' is false for the arrow test, and the first what-if, a spinning space station, makes released balls swerve by the cabin's ruler with no curving.
- “Two arrows carried to one spot by different routes arrive matching exactly when an arrow carried out along one route and home along the other comes back matching.”: A 29-word sentence I had to reread, with an 'exactly when' given no reason; it serves only the reverse argument.
- “Take a sheet of squared paper and press it onto a patch of ground.”: 'Squared paper' and 'patch' are undefined, and the no-holes condition the reverse argument needs appears only paragraphs later, so the 'exactly when' is false for a ring around a cone tip.
- “It also works on a large drinks can, because the paper simply rolls around the can.”: First what-if: paper pressed over the can's rim cannot lie in one layer, so 'works on a can' is false as stated; 'drinks can' and 'tin can' in try_it name one object two ways.
- “So a table and a drinks can are flat, although the can looks bent.”: A table's corners and a can's lid rim fail the paper test, so the whole objects are not flat.
- “This agreement between the two tests is called the flatness criterion.”: 'Criterion' is an unfamiliar word with no meaning given.
- “Nothing stretched, so every angle along the paper equals the same angle along the ground.”: Reread: 'angle along the paper' is unclear, and 'nothing' has no named subject.
- “On flat paper, such an arrow keeps its angle to the printed lines.”: A step left implicit: the paper is bent around the can, so 'flat paper' needs a peel-off step, and why the arrow keeps its angle to the lines is not said.
- “The reason also runs the other way. Suppose every small loop on a patch brings the arrow back matching. ... These lines close into squares, a step taken on trust here.”: Rule 17: after the paper test, the arrow test and the forward reason, the same way asks the reader to take in a second construction, spreading arrow copies and drawing a grid.
- “that loop can be split into small loops, like a field split into small plots. Each small loop brings arrows back matching, so the whole loop does too.”: A step taken on trust: why do matching small loops make the big loop match?
- “a loop around a football pitch brings the arrow back turned by about one hundred-millionth of a degree. The pitch covers only about 14 parts in a million million of Earth's surface, so the turn is tiny”: The link from the fraction of Earth's surface to the turn is missing (the twice-the-fraction rule is not restated), and one hundred-millionth of a degree has no everyday comparison.
- “Spacetime is flat where every entry of that table is zero.”: A bare assertion: the reader met flat only through paper and arrows, and the recap never says that the table also sets drifts, which the way's conclusion depends on.
- “Spacetime needs a test you can do inside a room.”: A surprise with no reason: why can the arrow test not be used?
- “so it moves on at a steady speed”: A speed with no measurer: steady by whose ruler, when the cabin's ruler shows it speeding up?
- “A pull that makes everything fall together”: 'Fall together' reads as 'fall toward each other', the very drift the way contrasts it with: one word for two ideas. 'Everything' is also unbacked.
- “Now pump the air out and try two balls.”: A step left implicit: why pump the air out? It also comes after one ball has already been dropped in air.
- “Dropped 20 metres, their gap shrinks by 20 parts in 6,371,000.”: Why the fraction is the drop over Earth's radius is left implicit.
- “The rocket cannot copy this drift. So the drift shows that spacetime around Earth is curved.”: A missing step: failing to match the rocket does not by itself prove curving; the link is that the Riemann table sets drifts. First what-if: a spinning cabin copies a drift in flat spacetime.
- “A friend says that such a tiny square lies against the ball perfectly ... Use the arrow test to explain.”: Check: no specific size, and the answer skipped why paper that fits would force matching arrows.
- “They move 3 metres before the floor reaches them. ... over a 3-metre drop their gap shrinks by 3 parts in 6,371,000, about one thousandth of a millimetre.”: Check: 'move' has no ruler, the cabin could spin, and the answer skips the step from a fraction of the 2-metre gap to a length.
- “The drift is so small that it takes instruments using falling atoms to measure it.”: False first what-if: other gravity gradiometers measure it too.
- “A slow change in the gap between two neighbours that fall freely side by side.”: Glossary: neighbours thrown apart also change their gap; the definition needs a shared start.
- “say_as: cry-TEER-ee-un”: The pronunciation covers only half of the term 'flatness criterion'.

**Fixes**

- Compared the retell with the takeaways: the first way's takeaway was recovered and the rocket takeaway mostly, but the reverse argument and the link from a zero table to flatness were not. Fixed both.
- Split the entry picture way: 'Squared paper or small loops' keeps the paper test, the criterion and the paper-to-arrow reason; the new entry way 'Drawing squared paper with arrows' carries the arrow-to-paper construction, with the loop-splitting step backed by shared sides cancelling. The working way 'Constant metric exactly when Riemann vanishes' now continues both, and the first teaching-arc step uses both.
- Scoped the paper test to patches with no holes and to the side of a can (a can's rim and a table's corners fail), defined squared paper, patch and criterion, and added glossary entries for squared paper and patch.
- Rocket way: gave the reason spacetime needs a test inside a room, a measurer for the steady speed, the air pumped out at the start, a non-spinning cabin (a spinning cabin makes released balls swerve in flat spacetime), the spokes step behind 20 parts in 6,371,000, and the link from drift to the Riemann table, now also restated in the recap. Replaced 'fall together' with 'fall the same way', backed by the feather and hammer.
- Summary and tagline: shorter sentences, the no-holes and non-spinning scopes, and the region claim presented as following from the paper test.
- Checks: the stamp check has a 2-centimetre square and the paper-to-arrow step; the rocket-drop check has a cabin ruler, a non-spinning cabin and the step from 6 metres divided by 6,371,000 to one thousandth of a millimetre (recomputed: 9.4e-7 m).
- Recomputed the football-pitch numbers with python: 105 by 68 metres over 510 million square kilometres is 1.4e-11 of Earth's surface, a turn of 1.01e-8 degrees, the angle of a 0.07 mm hair seen from 398 km.
- Budget: after the fixes the entry explanations reached 1,237 words, so I dropped the lowest-value items: the football-pitch paragraph moved from the first way to a new entry common question 'Is a football pitch exactly flat?', which restates the twice-the-fraction rule; the new way's ring-around-a-cone-tip what-if was dropped; so were the rhetorical question 'Could two routes to the same spot give copies that point different ways?' and the redundant sentences 'The arrow test gives the same verdict.' and 'A football is not flat.' Entry explanations now total 1,088 words, within the 10% allowance.
- Ladder: every non-entry way's first sentence names the way it continues; the ways remain distinct routes (paper picture, arrow-grid construction, operational cabin, calculation, operational clocks, structure, contrast).
- Bumped the revision to 2.

**Concerns**

- The first entry way no longer carries its own everyday number; its 'why don't I notice' number now lives in the entry common question 'Is a football pitch exactly flat?'. An editor may prefer to move it back if the entry budget is rebalanced.
- Entry explanations sit at 1,088 words and tutoring at about 2,930, so little room remains for later entry additions.
- Physics reviewer: please confirm the new entry claims: a can's lid rim is not flat (the rim bends differently as seen from the lid and from the side), a spinning cabin makes released balls seem to swerve with no curving, balls let go together side by side never drift where the Riemann tensor is zero, and on a surface the turns of neighbouring small loops add.
- The spacetime half of the entry rung rests on the Riemann prerequisite's statement that the same table sets tidal drift; if that prerequisite's entry wording changes, the rocket way's recap should follow.
- The proposed visual 'falling-ring-of-crumbs' should show a cabin that does not spin, and 'paper-rolled-into-a-tube-and-a-cone' should press paper on the side of a tube or can, not over a rim.
- Second novice pass: a physics diff check now covers exactly the eight changed learner-visible strings of revision 6. Snapshot for note_diff.py: scratchpad/snapshots/notes-curvature/flatness-criterion.before-novice2.json. The claims to confirm are that the Riemann tensor records how small loops turn carried arrows (the new summary sentence), that a small loop around a piece of a ball always returns the arrow turned while an out-and-back loop does not, and that dropping the rocket way's closing sentence loses no scope.
- Second novice pass, left as a watch item rather than a stumble: the paper-to-arrow argument in 'Squared paper or small loops' ends on the table ('and so it comes back matching its start'), and the last step back to the ground is carried only by the word 'either'. It reads, but if the entry budget is ever rebalanced, one sentence closing the loop on the ground would make it airtight.
- Second novice pass: entry explanations sit at 1,097 of the 1,100 review ceiling. Any further entry addition has to drop something, and nothing redundant is left.

**Re-read** (2026-09-13, revision 4): 3 stumbles in 8 changed passages

- “Whether the arrow swings can be judged from lengths and angles measured along the ground alone.”: A passive sentence with no one doing the judging; I reread it to find who judges and how, since the example that used to follow was removed.
- “On a small patch, those squares are the squared paper that fits it.”: Step taken on trust: the whole argument built squares on any patch with no holes, and 'small' appears at the end with no reason, so I wondered what goes wrong on a big patch.
- “On a patch with no holes where every small loop brings the arrow back matching, copies of two arrows at a right angle agree at every spot. On a small patch, lines drawn along those copies make the squared paper.”: Two different patch conditions in a row read as if 'a small patch' were a new, different patch; I could not tell whether the second sentence still meant the patch with no holes.
- Fix: squared-paper-or-small-loops explanation: made the judging sentence active ('You can judge whether the arrow swings from lengths and angles ...'); claim unchanged.
- Fix: drawing-squared-paper-with-arrows explanation: added a one-sentence reason for the 'small patch' scope (a long winding ribbon-shaped patch could need paper that overlaps itself), taken from the physics review's counterexample.
- Fix: Budget: to keep entry explanations within the 10% allowance (now 1,098 of 1,100), dropped the lowest-value sentence of that way, 'On a ball, this drawing fails, because copies carried by different routes disagree.' The ball contrast remains in the recap and explanation of 'Squared paper or small loops'.
- Fix: drawing-squared-paper-with-arrows takeaway: 'On a small patch, lines drawn ...' became 'If that patch is also small, lines drawn ...', tying the scope to the same patch.
- Fix: No stumbles in the summary, objective, glossary, first way's takeaway and recap, football-pitch answer, or rocket way sentence.

**Re-read** (2026-09-13, revision 5): 0 stumbles in 2 changed passages


**Re-read** (2026-09-13, revision 6): 6 stumbles in 13 changed passages

- “Squared paper covers a small patch of ground with no holes, without stretching, exactly when its small loops bring carried arrows back matching. So a region is flat exactly when its Riemann curvature tensor is zero throughout.”: The 'So' claims a step that is not there. The first sentence is about paper and loops and never mentions the tensor, so the reader has to supply the link that the tensor is what records the loops' turns. This is the same gap the first pass's retell named ('what does a table of zeros have to do with paper?') and the first pass reworded the sentence without closing it. 'without stretching' also drops the 'or tearing' that every other statement of the paper test carries.
- “A region is flat exactly when small loops there bring carried arrows back matching”: 'Region' is never defined, and it sits beside 'patch', which the glossary does define. The reader cannot tell whether the two words name one idea or two.
- “Now carry copies of the two arrows to every other spot of the patch, never letting them swing. Going out along one route and home along the other makes a loop.”: 'The other' has no antecedent: only one route has been walked, and the question the paragraph answers, whether copies carried by two different routes agree, is not asked until the paragraph's last sentence. I reread the paragraph twice. The first pass dropped exactly the sentence that set this up ('Could two routes to the same spot give copies that point different ways?') to stay inside the entry budget.
- “You wake up in a closed cabin with no windows. The cabin does not spin, and its air has been pumped out, so no air pushes anything you let go.”: A rule the reader could not physically follow: the reader is standing in the cabin, letting go of balls, with no air. The airless cabin is needed (a feather and a hammer land together, and the balls must fall freely), so the reader needs a way to be there.
- “However small the patch, a small loop on it brings a carried arrow back turned a little.”: A general sentence that fails for a what-if a reader can try: a loop walked out and straight back along one path brings the arrow back matching, on a ball as on a floor. The first way's recap was already scoped to 'a small loop around a piece of the ball'; this correction was not.
- “But on a ball, even a small loop that fits on the square brings a carried arrow back turned a little.”: The same unscoped claim, and a third wording for one idea: the recap says 'a small loop around a piece of the ball', the misconception said 'a small loop on it', and the check says 'a small loop that fits on the square'.
- Fix: This was a second full novice pass over the whole entry surface, not a diff re-read. The first pass's record (25 stumbles and two re-reads) is kept above unchanged; the six stumbles here are the ones that survived it.
- Fix: Summary: split into five sentences, restored 'or tearing', and supplied the missing link, so the tensor is tied to small loops before the 'So'. Average sentence length fell from 24 words to 14.
- Fix: Glossary: added 'region', defined against the already-defined 'patch', so the tagline, summary and flatness-criterion entry no longer use an undefined word beside a defined near-synonym.
- Fix: Drawing way: added one sentence naming the two routes before 'the other' uses them, restoring the setup the first pass had dropped for budget.
- Fix: Rocket way: the reader now puts on a spacesuit and pumps out the air, instead of waking up in a vacuum. The condition is doable and stays in the explanation rather than moving to simplifies.
- Fix: Misconception tiny-patch-is-flat and check shrink-the-patch: both now scope the loop as 'around a piece of', matching the first way's recap, so one idea has one wording and the out-and-back loop is no longer a counterexample to an entry sentence.
- Fix: Budget: the two entry-explanation additions cost 20 words and the entry rung was at its ceiling of 1,100. Dropped the lowest-value entry sentence, the rocket way's closing 'A pull that makes everything fall the same way shows nothing about curving, but a drift between balls let go side by side does', which repeats the way's takeaway almost word for word; the takeaway still carries it and the paragraph still ends on 'so spacetime around Earth is curved'. Entry explanations are now 1,097 words. No sentence was compressed to fit.
- Fix: Ladder re-read: every non-entry way still opens by naming a way it continues; the seven ways are still seven different routes (paper picture, arrow-grid construction, operational cabin, calculation, operational clocks, structure, contrast); no kind fills more than half; the working rung's index notation is reached through the prerequisites. No bridge was missing.
- Fix: Revision bumped to 6; status returned to novice-reviewed, because review.physics covers revision 5.

**Re-read** (2026-09-13, revision 8): 3 stumbles in 4 changed passages

- “There, in a cabin that does not spin, balls let go together side by side never drift.”: Two things happen at once in one short sentence, which is the squeezed-to-fit shape rule 17 warns about. 'There' points back to the flat-tensor sentence before it, and before I reach who or what the sentence is about I have to take in a brand-new condition about spinning. On top of that, 'let go together side by side' packs the moment of release and the starting positions into one unbroken phrase, so 'together' could mean the balls touch each other. I reread the sentence twice: once to find the subject, once to work out what 'together' meant.
- “A rocket speeding up in empty space, in a cabin that does not spin, cannot copy that drift.”: Two 'in' phrases run into each other, so the sentence first says the rocket is in empty space and then says the rocket is in a cabin. Spoken aloud by the tutor, it sounds as though the rocket sits inside the cabin, when the cabin is the room inside the rocket. I had to stop and rebuild the picture.
- “What shows curving is a drift between balls let go side by side in a cabin that does not spin.”: Spoken, five things hang off 'balls' with no pause: let go, side by side, in a cabin, that does not spin. The line is the tutor's, so a listener gets one pass at it and cannot go back. A small pause before the cabin makes the condition land as its own piece.
- Fix: ways_in[rocket-or-planet].recap: moved the non-spinning condition from between 'There' and the subject to the end of the sentence, and replaced 'let go together side by side' with 'let go side by side at the same moment'. Same condition, same law, same scope; the release is still simultaneous, as the way's explanation states ('let go of both together').
- Fix: tutor_moves.common_questions[is-our-space-flat].answer: 'A rocket speeding up in empty space, in a cabin that does not spin, cannot copy that drift.' became 'A rocket speeding up in empty space cannot copy that drift, as long as its cabin does not spin.' The condition now plainly belongs to the rocket's cabin, which is what the sentence already meant.
- Fix: misconceptions[pull-means-curved].correction: added a pause before the condition and 'in' became 'inside' ('... side by side, inside a cabin that does not spin'). Nothing else changed in the correction.
- Fix: Budget: other way fields went from 740 to 744 of 800 and tutoring from 2,986 to 2,987 of 3,300, so nothing had to be dropped. Entry explanations were not touched and stay at 1,097.
- Fix: Read and left alone: everything else in the three fields, including the Earth drift figure, the atom-clouds sentence, and the first sentence of the correction.

**Re-read** (2026-09-13, revision 9): 0 stumbles in 2 changed passages


## Review: physics

**Verdict:** fixed (2026-09-13, revision 9)

**Verification**

- Paper-to-arrow direction: an unstretched covering carries never-swinging arrows to never-swinging arrows on the table.: Levi-Civita transport is determined by the metric, so an isometry preserves it; tested the stated reason against a conformal (angle-only) map such as a Mercator chart of a sphere. → Conclusion correct, but the reason 'the arrow rule talks only about angles' was false: angle-preserving maps do not preserve transport. Reason now uses lengths and angles.
- Arrow-to-paper direction on a patch with no holes: copies agree, and turns of neighbouring small loops add.: Holonomy in SO(2) is abelian and conjugation by transport preserves the rotation angle on an orientable patch; null-homotopic loops decompose into small cells. → Correct. Grid lines close into squares because the connection is torsion-free (the coframe step). The final 'squares are the paper' needs a small patch: see counterexamples.
- Novice claims: a can's lid rim is not flat; a spinning cabin makes released balls swerve with no curving; side-by-side balls never drift where Riemann is zero.: Rim: the rim is a curved crease joining the lid and the side, a cone-like corner line where paper cannot lie in one layer; spinning cabin: Coriolis and centrifugal effects in flat spacetime; geodesic deviation D^2 xi/dtau^2 = -R u xi u with zero initial relative velocity. → All correct. The rocket-way sentence 'its released balls always keep their gap' was too broad: in a relativistic rocket, balls released at different heights have a cabin-ruler gap shrinking as 1/cosh(g tau/c) in flat spacetime. Rescoped to balls let go side by side.
- Earth drift: 20 m drop shrinks a 1 m gap by 20/6,371,000, about 3 thousandths of a millimetre, a twentieth of a hair.: python; radial free fall from rest at equal heights keeps both balls on radial lines, so the gap scales exactly as r. → 3.14e-6 m; 0.045 of a 0.07 mm hair (about a twenty-second). Correct to the stated rounding.
- Check rocket-drop: rocket gap 2 m; Earth shrink 2 m x 3/6,371,000.: python → 9.42e-7 m; numeric 9.4e-7 with rel_tol 0.05 correct.
- Football pitch: 105 m x 68 m is 14 parts in a million million of Earth's surface; turn 1.01e-8 degree; a 0.07 mm hair at 400 km.: python: 4 pi (6371 km)^2; turn = 2 x fraction x 360 degrees; angle x 400 km. → 1.40e-11; 1.008e-8 degree; 7.04e-5 m. Correct; rule scoped to a small loop, since twice-the-fraction holds only modulo whole turns.
- Cube corner: three right angles leave a quarter turn; the arrow returns turned a quarter turn; edges pass the paper test.: Cone-vertex holonomy equals the angle deficit 2 pi - 3 pi/2. → 90 degrees, magnitude. Correct.
- Working criterion: R = 0 on U iff local coordinates with g = eta; derivation steps 1-10.: Re-derived: Gamma=0 on open set kills all Riemann terms; tensor transformation; path independence from the small-loop law with course sign; dual coframe nabla theta = 0 gives d_mu theta_nu = Gamma^l_{mu nu} theta_l, symmetric, hence closed and exact on a ball; dX^a(e_b) = delta. → Correct, including the course sign of the small-loop law and index placement.
- Worked example e^{2u}(du^2+dv^2): Gamma^u_uu = 1, Gamma^u_vv = -1, Gamma^v_uv = 1; R^u_vuv = 0; r = e^u gives polar form.: Hand computation with the course Christoffel and Riemann formulas; K = -e^{-2phi} Laplacian(phi) = 0. → Correct; the map wraps infinitely often when v ranges over R.
- Clock-rate metric: dtau = N dt, f_r/f_e = N_e/N_r, proper acceleration c^2 N'/N toward increasing N, Gamma^x_00 = NN', Gamma^0_0x = N'/N, R^x_0x0 = NN''.: Hand derivation with x^0 = ct and the course Riemann formula; compared with conventions lapse row. → Correct, including sign: geodesic deviation then gives d^2 xi/dt^2 = -Phi'' xi in the weak field.
- Rocket N = 1 + gx/c^2 flat; N = e^{gx/c^2} gives g^2/c^4 = 1.19e-32 m^-2.: python → 1.191e-32 m^-2. Correct; rel_tol 0.02 fine.
- Weak field R^x_0x0 = Phi''/c^2 = -2GM/c^2 r^3 = -3.43e-23 m^-2 at Earth's surface; 2GM/r^3 = 3.08e-6 s^-2.: Linearized R_{i0j0} = d_i d_j Phi/c^2 for a static field; python with GM = 3.986e14, r = 6371 km. → 3.083e-6 s^-2 and -3.430e-23 m^-2. Correct in sign and size.
- Pound-Rebka: gh/c^2 = 2.46e-15 for 22.5 m; shift -2.46e-15; agreement within about 10 percent.: python; conventions redshift row; the 1960 result was 1.05 plus or minus 0.10 of the prediction. → 2.456e-15. Correct.
- Ricci check: R^r_trt = -2M/r^3 outside a static mass; at the Sun's surface -8.77e-24 m^-2.: Sign from radial stretching in geodesic deviation; python with GM_sun = 1.32712e20, R_sun = 6.957e8 m. → -8.771e-24 m^-2. Correct. Two- and three-dimensional Ricci-determines-Riemann statements correct.
- Milne problem: R^chi_tchi_t = -a''/a; a = t gives -dT^2 + dX^2 on T > |X|; a = t^{2/3} gives 2/(9t^2).: Hand computation with course Riemann formula; hyperbolic substitution checked; a''/a = -2/(9t^2). → Correct; the ambiguous '2/9t^2' was rewritten as 2/(9t^2).
- Formal theorem (a)-(d), developing map, completeness gives R^n_s, torsion criterion for vanishing coefficients.: Cartan structure equation dtheta = -omega wedge theta + T; Poincare lemma; Ambrose-Singer for restricted holonomy; Killing-Hopf and its pseudo-Riemannian analogue. → Correct as stated, with hypotheses open, connected, simply connected and complete where used.
- Torsion example dx^2 + e^{-2x}dy^2 with e_2 = e^x d_y declared parallel: R = 0, T(e_1,e_2) = -e_2, Levi-Civita K = -1.: [e_1,e_2] = e_2; K = -f''/f with f = e^{-x}. → Correct.
- Cosmic string deficit 8 pi mu (G = c = 1); torus top and bottom circles have K = 0.: Standard Vilenkin result 8 pi G mu/c^2; K of a torus of revolution is cos(v)/(r(R + r cos v)). → Correct.
- Check which-surfaces-are-flat: f = r + 3 flat, plane outside radius 3; f = sinh r has K = -1.: Hand computation, R^r_phi r phi = -f f''. → Correct.
- References: Pound and Rebka 1960; Snadden et al. 1998; Christoffel 1869; Levi-Civita 1917; Bieberbach 1911; Lachieze-Rey and Luminet 1995; Deser, Jackiw and 't Hooft 1984; Witten 1988; Aldrovandi and Pereira 2013.: Crossref records (api.crossref.org) for Levi-Civita, Bieberbach, Lachieze-Rey and Luminet, Deser et al., Witten; the other four match physics-verified records elsewhere in the vault (web search budget was exhausted this session). → All confirmed; DOIs added; Levi-Civita page range corrected to 173-204; all set verified.
- History: Riemann's 1861 Paris prize essay gave the flatness condition, published 1876; Christoffel and Lipschitz independently in 1869; Levi-Civita defined parallel transport.: Standard history of the equivalence problem. → Scopes accurate.
- Second physics pass (revision 6 to 7), scope audit: 'balls let go side by side never drift where the Riemann tensor is zero', stated in the rocket way's recap, in the misconception pull-means-curved and in the common question is-our-space-flat without the non-spinning hypothesis.: Tried the standard different-observer counterexample: a cabin rotating with angular velocity omega in flat spacetime. Two balls held at rest relative to the cabin and released have inertial velocities differing by omega x d, so their separation obeys |d(t)|^2 = |d(0)|^2 + t^2 |omega x d(0)|^2, which grows. Compared with the note's own measuring convention, which is always 'by a ruler fixed to the cabin'. → The law is false as stated for a spinning cabin under the note's own ruler, with zero curvature. The rocket way's explanation and takeaway already say the cabin does not spin, but the recap is read on its own by design, and the misconception and common question are spoken on their own. Fixed all three by naming the non-spinning cabin; the explanation sentence was left as it stands, because the same paragraph has already fixed the cabin.
- Second physics pass: the sufficiency direction, that a drift between balls let go side by side in a non-spinning cabin does show curvature.: Geodesic deviation in the course convention, D^2 xi^mu/dtau^2 = -R^mu_nu rho sigma u^nu xi^rho u^sigma, with zero initial relative velocity; and Fermi normal coordinates along a non-rotating accelerated worldline in flat spacetime, ds^2 = -(1 + a.x)^2 c^2 dt^2 + dx^2, in which two free particles released from rest at the same value of a.x have identical coordinate accelerations. → Correct. With R = 0 and no rotation, side-by-side released balls keep their gap exactly, so any such drift needs a nonzero Riemann component. The 'side by side' (equal a.x) condition is load-bearing and is present at every place the note makes the claim.
- Second physics pass: turns of neighbouring small loops add, the step the drawing way rests on.: Numerical parallel transport (RK4, python3) around two coordinate rectangles sharing a side, on dr^2 + f(r)^2 dphi^2 with f = sin r (1 + 0.3 r), a surface of non-constant curvature; compared each angle and their sum with the union's angle and with the Gauss-Bonnet value. → Loop A 0.0262907176, loop B 0.0362527116, union 0.0625434292; A + B minus the union is -1.4e-13. Each matches its Gauss-Bonnet integral to ten digits. The additivity holds because holonomies of an orientable surface lie in SO(2), which is abelian, and conjugation by transport preserves a rotation angle.
- Second physics pass: the entry sphere rule used in the football-pitch answer, that a small simple loop turns the arrow, in full turns, by twice the fraction of the ball on the walker's left.: python3: on a sphere of radius a a simple loop bounding area A has holonomy A/a^2 in the positive sense (region on the walker's left). Compared A/a^2 with 2 x (A/4 pi a^2) x 2 pi for polar angles 0.01, 0.1 and 1.0. → Identical at every size tested (0.000314, 0.031390, 2.888366 radians). The sense matches the conventions row: positive turns the direction of travel toward the walker's left. The rule is quoted only for a small loop, which is what keeps it free of the modulo-2 pi caveat.
- Second physics pass: every number in the note, recomputed from scratch.: python3 with G M_Earth = 3.986004418e14, r = 6371 km, G M_Sun = 1.32712440018e20, R_Sun = 6.957e8 m, c = 2.998e8 m/s and also c exact. → 1 m gap over a 20 m drop shrinks 3.139e-6 m (three thousandths of a millimetre; 1/22 of a 0.07 mm hair, quoted as a twentieth). 2 m gap over a 3 m drop shrinks 9.418e-7 m (numeric 9.4e-7, rel_tol 0.05). Pitch 7140 m^2 over 5.1006e14 m^2 is 1.3998e-11, turn 1.0079e-8 degree, a 0.07 mm hair at 398 km. g^2/c^4 = 1.1913e-32 m^-2. 2GM/r^3 = 3.0828e-6 s^-2 and -3.4299e-23 m^-2. g h/c^2 = 2.4558e-15 for 22.5 m. 2GM_Sun/(c^2 R_Sun^3) = 8.7703e-24 m^-2. All agree with the note within its stated figures and tolerances.
- Second physics pass: every equation and derivation step re-derived in the course conventions.: Hand derivation with the conventions rows for Christoffel symbols, R^rho_sigma mu nu, the small-loop law, geodesic deviation and x^0 = ct. Checked Gamma^x_00 = NN', Gamma^0_0x = N'/N, R^x_0x0 = N'^2 + NN'' - N'^2 = NN''; the static proper acceleration c^2 N'/N toward increasing N from a^x = Gamma^x_00 (u^0)^2 with u^0 = c/N; f_r/f_e = N_e/N_r; the log-polar plane Gamma^u_uu = 1, Gamma^u_vv = -1, Gamma^v_uv = 1 with R^u_vuv = (1)(-1) - (-1)(1) = 0, cross-checked by K = -e^{-2u} Laplacian(u) = 0; R^r_phi r phi = -f f'' for dr^2 + f^2 dphi^2; R^chi_t chi t = -adotdot/a for -dt^2 + a^2 dchi^2, and the hyperbolic substitution T = t cosh chi, X = t sinh chi giving -dT^2 + dX^2 on T > |X|; and the ten steps of the derivation zero-curvature-to-constant-metric. → Every sign, index placement and factor is correct in the course conventions. The weak-field limit R^x_0x0 = Phi''/c^2 = -2GM/c^2 r^3 has the sign that stretches a vertical pair, matching R^{r hat}_{t hat r hat t hat} = -2M/r^3 outside a spherical mass and the gradiometer observation's -c^2 R^z_0z0 = +2GM/r^3.
- Second physics pass: all nine references, checked afresh rather than against vault records.: Crossref metadata API (api.crossref.org) queried for each DOI in the note, comparing authors, title, container, volume, pages and year. → All nine confirmed: Pound and Rebka 1960 PRL 4, 337-341; Snadden, McGuirk, Bouyer, Haritos and Kasevich 1998 PRL 81, 971-974; Christoffel 1869 Crelle 70, 46-70 (Crossref files the volume under the year 1869; the conventional Band 70 is kept); Levi-Civita, Rend. Circ. Mat. Palermo 42, 173-204; Bieberbach 1911 Math. Ann. 70, 297-336; Lachieze-Rey and Luminet 1995 Phys. Rep. 254, 135-214; Deser, Jackiw and 't Hooft 1984 Ann. Phys. 152, 220-235; Witten 1988 Nucl. Phys. B 311, 46-78; Aldrovandi and Pereira 2013, Springer Netherlands (Dordrecht). No detail needed correcting; the earlier pass's concern that four were confirmed only indirectly is now discharged.
- Second physics pass: the formal rung's theorem, its hypotheses, and the near misses that mark its edges.: Re-checked (a) to (d) with Ambrose-Singer for the restricted holonomy group, Cartan's first structure equation dtheta^a + omega^a_b wedge theta^b = T^a, the Poincare lemma on a ball, and Killing-Hopf with its pseudo-Riemannian analogue for the complete simply connected case. Re-checked the near misses: normal coordinates at one point; Ricci determines Riemann for n <= 3 (6 independent components each in n = 3, Weyl identically zero); the doughnut's top and bottom circles from K = cos v / (r (R + r cos v)); the cone's rotation by the wedge angle; the Mobius band's reflection; the cosmic-string deficit 8 pi mu with G = c = 1; and the torsion example on dx^2 + e^{-2x} dy^2, where [e_1, e_2] = e_2 gives T(e_1, e_2) = -e_2 and the Levi-Civita curvature is K = -f''/f = -1. → All correct as stated, with the hypotheses open, connected, simply connected and geodesically complete used exactly where each is needed.

**Counterexamples tried**

- Long flat strip with no holes that winds around, such as a strip of the tangent developable of a helix taken over more than one turn: every small loop returns the arrow matching and the grid can be drawn, yet its development overlaps itself, so no single sheet of paper covers it in one layer. Broke 'squared paper can cover a patch exactly when'; fixed by 'a small patch' in the summary, objective, first way, takeaways and glossary.
- Mercator-style angle-preserving map of a sphere: preserves every angle but not arrow transport, so 'the arrow rule talks only about angles' was false. Reason changed to lengths and angles.
- Balls released at different heights in a relativistic rocket: cabin-ruler gap shrinks in flat spacetime. Broke 'its released balls always keep their gap'; rescoped to balls let go side by side.
- Spinning cabin in flat spacetime: released balls swerve by the cabin's ruler with zero curvature. Already excluded by the non-spinning cabin.
- Ring around a cone tip (a patch with a hole): flat everywhere yet a loop around the tip returns the arrow turned; excluded by 'no holes'.
- Degenerate loop that goes out and back along one path on a ball: no turn. Recap 'even a small loop' now says a small loop around a piece of the ball.
- Loop enclosing more than half of the Earth: twice-the-fraction holds only modulo whole turns; football-pitch answer now scoped to a small loop.
- Single event: normal coordinates kill Gamma for any metric; the note states the open-set hypothesis.
- Ricci-flat Schwarzschild exterior: flat Ricci, nonzero Riemann; handled in the formal contrast way and check.
- Flat torus, cylinder and Mobius band: local flatness without a global chart, and a reflection holonomy; handled formally.
- Metric connection with torsion on the hyperbolic plane: zero curvature, no chart with vanishing coefficients; handled formally.
- Linear clock-rate profile versus uniform acceleration at every height: redshift and acceleration without curvature, and constant acceleration with curvature; correct.
- Cube edge and cube corner: sharp but flat edge passes, corner fails both tests; consistent.
- Non-relativistic limit: Rindler N = 1 + gx/c^2 reproduces the Newtonian uniform field and the Pound-Rebka shift to first order.
- Second pass. Spinning cabin in flat spacetime, applied to the recap and the tutor-facing sentences rather than only to the explanation: released side-by-side balls separate as |d(t)|^2 = |d(0)|^2 + t^2 |omega x d(0)|^2 with zero curvature. Broke the recap's 'balls let go together side by side never drift', the misconception's 'What shows curving is a drift between balls let go side by side' and the common question's 'a rocket speeding up in empty space cannot copy that drift'; all three now name a cabin that does not spin.
- Second pass. Degenerate out-and-back loop on a ball, tried against the rewritten misconception and check: numerical transport returns the arrow exactly unturned, so 'a small loop around a piece of it' is the wording that survives and 'a small loop on it' would not have.
- Second pass. Figure-eight loop on a ball, two lobes walked in opposite senses: the turns add with opposite signs, so equal lobes return the arrow matching with nonzero curvature. Excluded by 'around a piece' in the singular, which names one region; recorded rather than fixed, since scoping it further would cost entry words the rung does not have.
- Second pass. Great-circle loop and a region bigger than half a sphere: holonomy 2 pi and, for the reversed octant, 7 pi/2 which is a turn to the walker's right. Both are excluded by 'small', which every statement of the ball claim now carries.
- Second pass. Surface of non-constant curvature (f = sin r (1 + 0.3 r)) used to test loop additivity rather than the constant-curvature sphere, so the additivity step does not rest on a special case.

**Fixes**

- Summary, objective explain-the-two-tests, first entry way explanation and takeaway, glossary flatness-criterion: the paper test is now claimed for a small patch with no holes (winding flat strip counterexample).
- First entry way: the reason paper keeps arrows now rests on unchanged lengths and angles, not angles alone; recap's ball loop is 'a small loop around a piece of the ball'.
- Drawing squared paper way: 'On a small patch, those squares are the squared paper that fits it', and the same scope in the takeaway.
- Rocket way: 'balls let go side by side in it always keep their gap' instead of 'its released balls'.
- Entry common question on the football pitch: the twice-the-fraction rule is stated for a small loop.
- Milne problem: 2/(9t^2) written unambiguously.
- References: DOIs added to all nine, Levi-Civita pages 173-204, Aldrovandi-Pereira venue with Dordrecht; all verified.
- Revision bumped to 3 for the learner-visible entry and working changes.
- Second physics pass. Rocket way recap: 'There, balls let go together side by side never drift' became 'There, in a cabin that does not spin, balls let go together side by side never drift'. A recap is read on its own, and the hypothesis was only in the explanation. Seven words, taken from the other-way-fields budget, which had room.
- Second physics pass. Misconception pull-means-curved: the correction now reads 'What shows curving is a drift between balls let go side by side in a cabin that does not spin'. The tutor speaks this sentence on its own.
- Second physics pass. Common question is-our-space-flat: the long sentence was split and the rocket given a cabin that does not spin, so the spoken answer no longer claims that a rocket in flat spacetime can never copy the drift.
- Second physics pass. No other change: the eight learner-visible strings the second novice pass changed are all accurate, and every equation, number and reference was re-derived, recomputed or re-queried rather than carried over.
- Revision bumped to 7 for the three learner-visible entry changes.

**Concerns**

- Crossref dates the Levi-Civita paper 1916 (presented in 1916, volume 42 issued 1917); the note keeps the conventional 1917.
- The course conventions do not define 'locally flat' or the entry meaning of 'small patch'; the note uses 'small patch' for a neighbourhood that develops onto the plane without overlap. A conventions row would help.
- Registry prerequisites still differ from the note (flat-metric, holonomy, rindler-coordinates, simply-connected-space), and related integrability-condition-for-parallel-fields is registry has-part; sync on apply.
- Five proposed visuals remain uncatalogued; falling-ring-of-crumbs should show a non-spinning cabin and side-by-side balls only, and paper-rolled-into-a-tube-and-a-cone should press paper on the side of a can, not its rim.
- Entry explanations sit near the 10% review allowance; the physics fixes added about ten entry words.
- Web search budget was exhausted, so four references were confirmed against earlier physics-verified vault records rather than a fresh search.
- Second physics pass, left as a recorded scope rather than a fix: in the rocket way's explanation, 'Where every entry of the Riemann curvature tensor is zero, balls let go side by side never drift' is a general law stated without the non-spinning hypothesis. The same paragraph has already fixed the cabin as one that does not spin, and the entry explanations sit at the ceiling, so naming it again would have to displace a real sentence. If the entry cap is ever rebalanced, this is the sentence to scope.
- Second physics pass, carried forward and still open: the entry rung's word 'turn' covers what a small loop does to a carried arrow in spacetime as well as on ground, where the exact statement is a Lorentz transformation that can be a boost. The note never uses a spacetime turn to argue anything, so nothing rests on it, but a conventions row on the entry meaning of 'turn' would settle it alongside 'small patch'.
- Second physics pass: the figure-eight loop on a ball returns the arrow matching when its two lobes have equal area, so 'a small loop around a piece of it' is carried entirely by the singular 'a piece'. An editor with entry words to spare could say 'a loop that never crosses itself', which the football-pitch answer already uses.
- Second physics pass: the reference concern from the first pass is discharged; all nine were re-queried against Crossref this session. The Levi-Civita date stays at the conventional 1917 while Crossref dates volume 42 to December 1916.

**Diff check** (2026-09-13, revision 5)

- Drawing way explanation, added: 'A long ribbon-shaped patch that winds around could need paper that overlaps itself.': Built the winding-strip counterexample with python3: tangent developable of the helix (cos t, sin t, 0.5 t). Its development is a circle of radius 1/kappa with its tangent segments, so it closes after arc 2 pi/kappa, about 1.118 helix turns. Compared the points 0.3 along the tangents at arc 0 and at arc 2 pi/kappa: 3.59 apart on the surface in space, 0 apart in the plane. Also tried a strip wound helically around a can (develops to a straight strip, no overlap) and a meandering planar strip (no overlap); 'could' and 'winds around' keep the sentence true. Checked against the first way's rule that paper lies in one layer and must not fold over onto itself. → True: a patch with no holes and trivial small loops can fail to be covered by one sheet because its development overlaps. But the unqualified 'paper that overlaps itself' could be read as paper stacked in two layers on the ground, which the ribbon does not need, since on the ground the covering is one layer. Fixed to 'overlaps itself when flat'.
- Drawing way takeaway: 'On a patch with no holes where every small loop brings the arrow back matching, copies of two arrows at a right angle agree at every spot. If that patch is also small, lines drawn along those copies make the squared paper.': Compared with the old 'On a small patch, lines drawn along those copies make the squared paper' and with the formal (a) to (c) to (b) chain: no holes gives endpoint-independent transport; smallness gives a development without overlap. → Accurate. It claims exactly what the old takeaway did, with the two conditions now attached to one patch. Consistent with the winding ribbon, where copies agree yet one sheet fails.
- First way explanation: 'You can judge whether the arrow swings from lengths and angles measured along the ground alone.': Compared with the old passive wording; checked against the Levi-Civita connection being fixed by the metric alone, and the Mercator-map counterexample (angles alone do not fix transport). → Accurate. Same claim as before; lengths and angles are kept together.
- Removed from the drawing way: 'On a ball, this drawing fails, because copies carried by different routes disagree.': Checked whether any scope caveat or later reference depended on it. → No caveat lost. The first way's recap still shows a small loop on a ball returning the arrow turned, and no check or ref cites the removed sentence.
- Fix: Drawing way explanation: 'could need paper that overlaps itself' became 'could need paper that overlaps itself when flat', so the overlap is in the flattened sheet, not a second layer on the ground. Revision bumped to 5.

**Diff check** (2026-09-13, revision 7)

- Summary, new sentence: 'The Riemann curvature tensor records how small loops turn carried arrows.': Compared with the course small-loop law, Delta V^rho = -R^rho_sigma mu nu V^sigma a^mu b^nu, which is exactly the statement that the tensor fixes the change a small loop makes to a carried vector; checked the wording against the glossary entry riemann-curvature-tensor in this note and the entry rung of the prerequisite note, which use the same picture; checked that no other word in the note does the job of 'turn'. → Accurate at the entry rung and consistent in wording. On a surface the loop's effect is exactly a turn; in spacetime the small-loop change of a vector is a Lorentz transformation that can include a boost, so 'turn' is a simplification, but it is the one the prerequisite already makes and the note's own spacetime test is the drift, not a turn. Left as written.
- Summary, the step 'So a region is flat exactly when that tensor is zero throughout it.': Traced the chain the three sentences now make: paper covers a small patch with no holes iff its small loops return arrows matching (first sentence); the tensor records those loops' turns (second); and 'flat' is defined in the glossary as squared paper covering some small patch around every spot. Checked the equivalence itself against the note's own theorem for the Levi-Civita connection of a smooth metric on an open set. → The step is now supported and the equivalence is true with the note's hypotheses. The 'So' no longer asks the reader to supply the missing link.
- Rescoped claim, in the misconception and in check shrink-the-patch: a small loop around a piece of a ball always returns the arrow turned, while an out-and-back loop does not.: Numerical parallel transport (RK4, python3) on the surface of revolution dr^2 + f(r)^2 dphi^2 with f = sin r (1 + 0.3 r), which has non-constant Gaussian curvature. Walked closed coordinate rectangles and a degenerate out-and-back path, and compared the returned arrow with the Gauss-Bonnet value -(f'(r2)-f'(r1))(phi2-phi1). Separately, on a sphere of radius a a simple loop bounding area A gives A/a^2 exactly. → Confirmed. The out-and-back path returns the arrow exactly unturned (components (1.0, 0.0), angle 0). A loop that encircles a region of positive area returns it turned, and on a sphere the turn A/a^2 is nonzero for every small simple loop. The rewrite 'around a piece of it' is what makes the sentence true, and it now matches the first way's recap word for word.
- Drawing way, restored sentence: 'Two routes can reach the same spot, so the copies carried along them could arrive pointing different ways.': Checked against path dependence of parallel transport: on a patch where some small loop has nonzero holonomy the two copies differ, and on a flat patch they agree, so only 'could' is claimed. → Accurate, and it is the antecedent the next sentence's 'the other' needs. No new claim is made.
- Rocket way, replaced sentence: 'You put on a spacesuit and pump out the air, so no air pushes anything you let go.': Checked that the airless cabin is still what the argument needs (no drag or buoyancy on the released balls, so the feather and the hammer are reached by the floor together) and that the rule is one a person could carry out at each step of the thought experiment. → Accurate and doable. The physical condition is unchanged; only who arranges it changed.
- Dropped from the rocket way: 'A pull that makes everything fall the same way shows nothing about curving, but a drift between balls let go side by side does.': Checked every scope the dropped sentence carried against what remains: the takeaway now carries 'In a cabin that does not spin, a pull that makes everything fall the same way does not show curved spacetime, but a drift between balls let go side by side does', and the paragraph still ends on 'so spacetime around Earth is curved'. Checked that no check, objective, misconception or ref cites it. → No scope lost, and the sentence it dropped was in fact weaker than what remains: 'shows nothing about curving' overstates, while the takeaway's 'does not show curved spacetime' is exactly right. Nothing cites the removed sentence.
- Glossary, new entry 'region': a piece of ground, or of spacetime, with room around every spot in it, rather than a single spot; a patch is a region of ground with no holes.: Compared with the working and formal rungs, where the criterion is stated on an open set U, and with the note's own contrast between a single event (where coordinates always kill the Christoffel symbols) and an open region. → A faithful entry-rung rendering of 'open set', and it makes the single-point counterexample sayable at the entry rung. The glossary 'patch' (a piece of ground with no holes) is consistent with it.
- Glossary 'region' forms and term fields.: Checked the plural against the note's uses of 'region' and 'regions'. → Consistent.
- Fix: No fix was needed to any of the eight strings the second novice pass changed; all three claims it asked to be confirmed are confirmed above.

**Diff check** (2026-09-13, revision 9)

- Rocket way recap, reworded by the re-read: 'There, balls let go side by side at the same moment never drift, as long as the cabin does not spin.': Read the recap on its own, as a reader arriving out of sequence does, and asked which frame the words 'never drift' are judged in. Compared with the sentence it replaced, 'There, in a cabin that does not spin, balls let go together side by side never drift', which put the balls in the cabin. Checked the same claim where the note states it elsewhere: the way's takeaway ('In a cabin that does not spin, ...'), the misconception correction ('inside a cabin that does not spin') and check rocket-drop, whose question fixes the frame with 'Its cabin does not spin'. → The claim is true, but the frame it is judged in was left dangling. Nothing in the recap introduces a cabin, and the balls are no longer said to be in one, so the only thing that ties the drift to a non-spinning frame is a definite article with no antecedent. Fixed by naming the frame with the note's own words: 'as long as they are inside a cabin that does not spin'. The claim, its condition and its rung are unchanged.
- The same recap sentence's new simultaneity wording, 'let go side by side at the same moment', replacing 'let go together side by side' - a moment with no clock named.: Asked whose clock sets 'the same moment', since the way's own rocket is an accelerating frame. For two balls side by side, that is at the same height and separated across the direction of the push, the rigid cabin's surfaces of constant time are the inertial hyperplanes through the origin, t = x tanh(aT), which do not involve the two transverse coordinates. So the cabin's clocks and the freely floating friend's clocks pick out the same pair of release events. Checked the Earth case the same way: the two balls sit at the same height, so the static frame and the local freely falling frame agree on their simultaneity at the moment of release, when their relative velocity is zero. → No ambiguity of physical consequence at this rung: for balls released side by side at the same height, every frame in the note agrees on 'the same moment'. The condition is also a real one, not decoration, because balls released at different moments in a speeding-up cabin would not keep their measured gap. Left as written.
- Common question is-our-space-flat, reworded: 'A rocket speeding up in empty space cannot copy that drift, as long as its cabin does not spin.': Compared word by word with the sentence it replaced, 'A rocket speeding up in empty space, in a cabin that does not spin, cannot copy that drift': same rocket, same drift, same non-spinning condition, and 'its cabin' has the rocket as its antecedent. Then tested how conservative the condition is with python3: in flat spacetime a ball released at rest in a cabin spinning at rate Omega moves in a straight line in the inertial frame with velocity Omega x r, so the pair's separation is d0 + t (Omega x d0), and a spin preserves distances, so the cabin measures that same separation. Sampled 20,000 random separation directions over 4 seconds at Omega = 1.7 per second. → Accurate, and claiming exactly what the old sentence claimed. The smallest gap ratio ever reached was 1.0000000, so a spinning cabin in flat spacetime can only push side-by-side balls apart, never draw them together; the drift the answer points at near Earth is a drawing together. The stated condition is therefore sufficient and in fact stronger than needed, which is the safe direction. Left as written.
- Misconception pull-means-curved, reworded: 'What shows curving is a drift between balls let go side by side, inside a cabin that does not spin.': Compared with the sentence it replaced, which read 'in a cabin that does not spin'; the only changes are the pause and the word 'inside'. Checked both readings the comma allows, the one where 'inside a cabin that does not spin' modifies the released balls and the one where it modifies the whole test, and checked that the diagnosing check rocket-drop sets the same scene, with a non-spinning, airless cabin and balls held side by side at the same height. → Identical claim, and now the balls are explicitly in the cabin whose spin the condition is about. Consistent with check rocket-drop and with the way's takeaway.
- Numbers standing next to the changed strings, unchanged by the re-read but re-checked for consistency with them.: Recomputed with python3 the two convergence figures the changed sentences lean on, using Earth's radius 6,371 kilometres and the spokes-of-a-wheel proportion: a 20-metre drop of balls 1 metre apart, and check rocket-drop's 3-metre drop of balls 2 metres apart. → 1 metre times 20 divided by 6,371,000 is 3.14e-6 metres, matching 'about three thousandths of a millimetre'; 2 metres times 3 divided by 6,371,000 is 9.42e-7 metres, matching the check's stored value 9.4e-07 within its 5 per cent tolerance. No number needed changing.
- Fix: Rocket way recap: 'as long as the cabin does not spin' became 'as long as they are inside a cabin that does not spin', so the frame the drift is judged in is named and the balls are back inside it. The re-read's improvement, which is that the condition comes after the claim instead of splitting the subject, is kept. Other way fields go from 744 to 749 words against a cap of 800, so nothing was compressed and nothing dropped.
- Fix: No fix was needed to the other two changed strings, in the misconception correction and in common question is-our-space-flat; both claim exactly what they claimed before.
