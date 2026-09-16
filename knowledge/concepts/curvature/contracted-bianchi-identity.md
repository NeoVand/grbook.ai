---
type: "concept"
schema_version: 2
id: "contracted-bianchi-identity"
title: "Contracted Bianchi identity"
tagline: "Why one table of curving always balances, and why matter must balance too"
domain: "curvature"
tier: "core"
status: "physics-reviewed"
revision: 8
updated: "2026-09-13"
aliases: ["twice-contracted Bianchi identity", "divergence-free Einstein tensor"]
prerequisites: ["bianchi-identity", "ricci-tensor", "ricci-scalar", "metric-compatibility", "levi-civita-connection", "diffeomorphism-invariance"]
leads_to: ["einstein-tensor", "einstein-field-equations", "ricci-tensor-field-equation", "propagation-of-constraints", "equations-of-motion-from-field-equations", "einstein-space"]
visuals: ["dial-the-half-beside-a-star", "counting-box-in-a-narrowing-hose"]
---

# Contracted Bianchi identity

*Why one table of curving always balances, and why matter must balance too*

`contracted-bianchi-identity` · curvature · core · physics-reviewed (revision 8)

**Needs:** [[bianchi-identity]] (entry) · [[ricci-tensor]] (entry) · [[ricci-scalar]] (working) · [[metric-compatibility]] (working) · [[levi-civita-connection]] (formal) · [[diffeomorphism-invariance]] (formal)  
**Opens:** [[einstein-tensor]] · [[einstein-field-equations]] · [[ricci-tensor-field-equation]] · [[propagation-of-constraints]] · [[equations-of-motion-from-field-equations]] · [[einstein-space]]  
**Related:** [[covariant-conservation-of-energy-momentum]] · [[cosmological-constant]] · [[fluid-equation]] · [[lovelock-theorem]] · [[conservation-law-from-diffeomorphism-invariance]] · [[charge-conservation]]  
**Visuals:** ★ [[dial-the-half-beside-a-star]] · [[counting-box-in-a-narrowing-hose]]

> Water flowing through a hose balances. The water in any tiny box changes only by what flows in or out. The contracted Bianchi identity says that the Einstein tensor, a table made from the curving of spacetime, balances in the same way in every smoothly curved spacetime. Einstein's equation ties this table to the matter at each place, so the energy and momentum of matter must balance in every tiny box too.

## You will be able to

**Entry**
- Explain what it means for an amount to balance, and why a balanced amount can still differ from place to place. `objectives/explain-balance` ← `checks/sun-and-empty-space`, `problems/water-in-a-tub`
- Explain why a law of gravity that set the Ricci tensor equal to the matter table could not describe a planet or a star. `objectives/explain-the-failed-guess` ← `checks/first-guess-and-a-planet`
- Explain why the Einstein tensor balances in every smoothly curved spacetime, whatever its matter does. `objectives/tell-identity-from-matter` ← `checks/invented-spacetime`

**Working**
- Derive the twice-contracted identity and show that only the coefficient one half makes the Ricci combination divergence-free. `objectives/derive-the-half` ← `checks/coefficient-of-the-half`
- Distinguish a divergence-free Einstein tensor from a constant one. `objectives/distinguish-divergence-free-from-constant` ← `checks/radiation-in-a-growing-box`
- Use the identity to relate the expansion equations of a flat universe to the energy budget of its contents. `objectives/use-identity-in-cosmology` ← `problems/acceleration-equation-for-free`, `checks/radiation-in-a-growing-box`

**Formal**
- Explain from the identity why four components of Einstein's equation contain no second time derivatives of the metric. `objectives/explain-constraints` ← `checks/constraints-without-second-time-derivatives`
- Derive conservation of mass and geodesic motion of dust from Einstein's equation and the identity. `objectives/derive-motion-of-dust` ← `checks/dust-must-fall-freely`
- Prove that an Einstein manifold of dimension three or more has constant Ricci factor, and that a cosmological term must be constant. `objectives/prove-constant-einstein-factor` ← `problems/einstein-space-constant-factor`
- Derive a divergence-free tensor from the invariance of a metric action under changes of coordinates. `objectives/derive-identity-from-invariance` ← `problems/identity-from-relabelling`

## Ways in

### 1. A table of curving that balances · entry · picture

*What rule does the contracted Bianchi identity give for the curving of spacetime?*

**Recap:** The curvature table is a table kept at every place that describes the curving there. The Ricci tensor is a smaller table made by adding up some of its entries. For a small ball of crumbs let go at rest by someone falling freely, the Ricci tensor gives the total of their drifts. Where matter fills the space among the crumbs, that total counts the matter right there. The Bianchi identity is a rule about how curving may change from place to place, and it holds in every smoothly curved space.

Picture a garden hose, pinched in the middle so that it is narrower there. Each minute, 20 litres of water enter one end. Once the water runs steadily, it fills the hose completely, and water cannot be squeezed into less room.

Picture a tiny imaginary box anywhere inside the hose. Water flows into the box through one side and out through the other. No water is made or destroyed inside the box. The box is always full, and the water cannot be squeezed, so the water in the box cannot pile up. So each second, as much water leaves the box as enters it.

No water piles up anywhere, so the same 20 litres pass through every part of the hose each minute. Where the hose's opening has half the area, the water must move twice as fast to get them through. So the water's speed changes from place to place. Yet in no tiny box does water appear or vanish. When an amount changes only by what flows in or out, in every tiny box, we say it balances.

Einstein's theory describes gravity as the curving of space and time together. Space and time taken together are called spacetime.

Some tables made from the curving of spacetime can be read like a record of flowing water. At each place, such a table lists a few amounts, and how fast each one flows in each direction. One of these tables is made from the Ricci tensor by a fixed recipe. It is called the Einstein tensor.

The Einstein tensor balances. Picture a tiny box carried by someone falling freely, without spinning. Each amount of the Einstein tensor changes in that box only by what flows in or out. The box must fall freely, because only then does gravity drop out of the count, just as a floating astronaut feels no weight.

This rule is called the contracted Bianchi identity. It comes from the Bianchi identity, so it holds in every smoothly curved spacetime, whatever that spacetime contains.

Balancing does not mean being the same everywhere. The water in the hose moves faster in the narrow part. In the same way, the Einstein tensor is far larger inside the Sun than in the nearly empty space around it. That is because the Ricci tensor counts the matter right where it is, and the Einstein tensor is made from the Ricci tensor. Yet the Einstein tensor balances in both places.

**Try it:** Turn a kitchen tap on to a thin, smooth stream. Compare the stream just below the tap with the stream a hand's width lower. Lower down it is thinner, because the water falls faster there. No water piles up between the two places, so the same amount passes both each second. So where the water moves faster, the stream must be thinner.

**Takeaway:** An amount balances when it changes in every tiny box only by what flows in or out. The contracted Bianchi identity says the Einstein tensor, a table made from curving, balances in every smoothly curved spacetime.

*Builds on:* [[bianchi-identity]], [[ricci-tensor]]<br>*Visuals:* [[counting-box-in-a-narrowing-hose]]<br>*See:* `checks/sun-and-empty-space`

### 2. True in every curved spacetime · entry · structure

*Why does the Einstein tensor balance in every smoothly curved spacetime, whatever fills it?*

**Recap:** An amount balances when, in every tiny box carried by someone falling freely without spinning, it changes only by what flows in or out. The Einstein tensor is a table made from the Ricci tensor. The Ricci tensor is made by adding up entries of the curvature table. Carry an arrow around each of the six faces of a tiny box, every face counterclockwise seen from outside. Each edge is shared by two faces, so every edge is walked once in each direction, and the six changes the arrow picks up add up to nothing. Opposite faces nearly cancel, and what each pair leaves over is called its leftover. The Bianchi identity says the three leftovers add up to nothing.

In "A table of curving that balances", the Einstein tensor balanced inside the Sun and in the empty space around it. Could some other spacetime break that balance?

Start with a rule about numbers. Fill a grid of three rows and three columns so that each row adds up to zero. Then all nine numbers together add up to zero, whatever numbers you chose. Adding up a rule that holds for every row gives a rule that holds for the whole grid.

The contracted Bianchi identity comes from the same kind of adding. Add up some of the many rules in the Bianchi identity, much as the Ricci tensor adds up entries of the curvature table. Most of the detail cancels, and what remains says that the Einstein tensor balances. This adding takes algebra with many entries, so here we take this step on trust.

The Bianchi identity itself holds in every smoothly curved spacetime, one with no sharp tips, tears or sudden jumps. Its reason uses only how tiny changes add and how the edges of a box are shared, never what fills the space. In spacetime, a box covers a little time as well as a little space, and that reason still works.

Adding up a rule that always holds gives a rule that always holds. So the Einstein tensor balances in every smoothly curved spacetime, real or invented, with matter or without. A rule like this, which holds whatever the world is like, is called an identity.

**Try it:** On paper, draw a grid of three rows and three columns. Fill each row with three numbers that add up to zero, such as 5, minus 2 and minus 3. Add all nine numbers: you get zero, whichever rows you chose. Now change a single number, and the total is no longer zero.

**Takeaway:** The Einstein tensor balances in every smoothly curved spacetime, because its balance comes from adding up the Bianchi identity, which holds whatever fills the space. It is an identity, not a law of nature.

*Picture:* A three-by-three grid of numbers, each row adding up to zero, with the whole grid's total of zero written beside it. Next to it, a tiny box with an arrow walked around each face, its three leftovers adding up to nothing.

*Continues:* `ways_in/a-table-of-curving-that-balances`<br>*Builds on:* [[bianchi-identity]], [[ricci-tensor]]<br>*See:* `checks/invented-spacetime`

### 3. The first guess would forbid stars · entry · historical-puzzle

*Why is Einstein's equation not simply the Ricci tensor set equal to matter?*

**Recap:** An amount balances when, in every tiny box carried by someone falling freely without spinning, it changes only by what flows in or out. The contracted Bianchi identity says the Einstein tensor balances in every smoothly curved spacetime. The Einstein tensor is made from the Ricci tensor by a fixed recipe. For a small ball of crumbs let go at rest by someone falling freely, the Ricci tensor gives the total of their drifts. Where matter fills the space among the crumbs, that total counts the matter right there.

In "A table of curving that balances", the Einstein tensor balanced in every tiny box. Why would a law of gravity need a table like that?

In November 1915, Einstein was searching for the law of gravity. He wanted a rule linking the curving of spacetime at each place to the matter there. Matter is described by a table too. At each place, that table lists the energy and momentum of the matter, and how they flow. This table is called the matter table.

Energy balances. In a tiny box carried by someone falling freely, without spinning, energy changes only by what flows in or out. Momentum balances in the same way, once every push across the box's walls is itself momentum flowing in or out. A push passes motion across the wall, so it is a kind of flow.

So the matter table balances. A tempting first guess sets the Ricci tensor equal to a fixed number times the matter table. Under that guess, the Ricci tensor would have to balance too. But does it?

At each place, the entries of the Ricci tensor add up, in a fixed way, to one number. This number is called the grand total. Adding up the Bianchi identity shows when the Ricci tensor fails to balance. Where its grand total changes from place to place, or from moment to moment, the Ricci tensor fails to balance, by exactly half of that change. That step takes algebra, so here we take it on trust.

Under the guess, the Ricci tensor must balance everywhere, so its grand total could never change. The guess also ties that grand total to the grand total of the matter table. For ordinary matter, such as rock or gas, the matter table's grand total comes almost entirely from the energy locked up in its mass. So the mass in each cubic metre could never change either, and matter would have to be spread evenly through all of space.

That rules out every star. A cubic metre of the Sun holds about 1,400 kilograms, on average. A cubic metre of space between the planets holds far less than a billionth of a gram.

Einstein's final equation, of 25 November 1915, fixed the Ricci tensor by taking away half its grand total, spread over the table in a fixed way. Taking away half the grand total also takes away half of its change. That exactly cancels the Ricci tensor's failure to balance. The result is the Einstein tensor, which balances. So matter can clump into stars and still balance.

**Takeaway:** Setting the Ricci tensor equal to a fixed number times the matter table would force ordinary matter to spread evenly, so no star could exist. Taking away half the Ricci tensor's grand total gives the Einstein tensor, which balances.

*What this leaves out:* Leaves out the cosmological constant, a tiny extra term that also balances and does not rescue the guess.

*Continues:* `ways_in/a-table-of-curving-that-balances`<br>*Visuals:* [[dial-the-half-beside-a-star]]<br>*See:* `checks/first-guess-and-a-planet`

### 4. Two contractions of the Bianchi identity · working · calculation

*How do two contractions of the Bianchi identity give a divergence-free Einstein tensor, and why the factor one half?*

The grand total in "The first guess would forbid stars" is the Ricci scalar $R = g^{\mu\nu}R_{\mu\nu}$, and the Ricci tensor's imbalance comes from contracting the Bianchi identity twice. Start from that identity for the torsion-free connection built from the metric, the Levi-Civita connection, in course conventions:

$$\nabla_\lambda R^\rho{}_{\sigma\mu\nu} + \nabla_\mu R^\rho{}_{\sigma\nu\lambda} + \nabla_\nu R^\rho{}_{\sigma\lambda\mu} = 0.$$

First set $\lambda = \rho$ and sum. With $R_{\sigma\nu} = R^\rho{}_{\sigma\rho\nu}$ and antisymmetry in the last pair, this gives the once-contracted identity $\nabla_\rho R^\rho{}_{\sigma\mu\nu} = \nabla_\mu R_{\sigma\nu} - \nabla_\nu R_{\sigma\mu}$, which uses no metric. Then contract with $g^{\sigma\mu}$. Two facts rest on $\nabla g = 0$: the inverse metric passes through $\nabla$, and $R_{\rho\sigma\mu\nu}$ is antisymmetric in its first pair, which turns the left side into $-\nabla_\rho R^\rho{}_\nu$. The derivation "Contracting the Bianchi identity twice" gives each move, ending at

$$\nabla_\mu R^\mu{}_\nu = \tfrac12\nabla_\nu R.$$

The divergence of the Ricci tensor is half the gradient of the Ricci scalar: the imbalance that ruled out the first guess. Since $\nabla_\mu(\delta^\mu{}_\nu R) = \nabla_\nu R$, it rearranges to

$$\nabla_\mu G^{\mu\nu} = 0,\qquad G_{\mu\nu} = R_{\mu\nu} - \tfrac12 R\,g_{\mu\nu}.$$

These are four equations, one for each $\nu$, and they hold for every metric. In a freely falling frame at a point, where the Christoffel symbols vanish, they read $\partial_\mu G^{\mu\nu} = 0$: each $G^{0\nu}$ is a density whose fluxes $G^{i\nu}$ carry all its change. That is the balance in every tiny box of "A table of curving that balances". $G^{\mu\nu}$ is symmetric, so the divergence may be taken on either index.

Why one half? For a candidate $R^{\mu\nu} + BRg^{\mu\nu} + \Lambda g^{\mu\nu}$ with constants $B$ and $\Lambda$, the identity and $\nabla g = 0$ give the divergence $(\tfrac12 + B)\nabla^\nu R$. Many metrics have $\nabla R \neq 0$, so only $B = -\tfrac12$ works for all of them, while $\Lambda g^{\mu\nu}$ is divergence-free by itself.

Taking the divergence of Einstein's equation $G_{\mu\nu} + \Lambda g_{\mu\nu} = (8\pi G/c^4)T_{\mu\nu}$ now gives $\nabla_\mu T^{\mu\nu} = 0$: the equation is consistent only with a conserved source. The first guess $R_{\mu\nu} = \kappa T_{\mu\nu}$ with a conserved source forces $\nabla R = 0$, so the trace $T = R/\kappa$ is constant. For a perfect fluid $T = -\rho c^2 + 3p$, which is nonzero inside any star of ordinary matter and zero in the vacuum around it.

Two cautions. Zero divergence is not constancy: in the worked example "The Einstein tensor of a flat universe balances", $G_{00} = 3H^2/c^2$ changes with time. And the identity does not choose Einstein's equation, since $\Lambda g_{\mu\nu}$ is divergence-free too.

**Takeaway:** Contracting the Bianchi identity twice makes the divergence of the Ricci tensor half the gradient of the Ricci scalar, so the Einstein tensor is divergence-free for every metric, and only the factor one half achieves this.

*What this leaves out:* Uses the Levi-Civita connection throughout; the formal rung says which steps need the metric.

*Continues:* `ways_in/the-first-guess-would-forbid-stars`<br>*Builds on:* [[bianchi-identity]], [[ricci-scalar]], [[metric-compatibility]]<br>*See:* `derivations/contracting-twice`, `checks/coefficient-of-the-half`, `worked_examples/flat-universe-balance`

### 5. An energy budget for the expanding universe · working · operational

*What does the identity let a comoving observer check about the energy of the cosmic fluid?*

The divergence-free Einstein tensor of "Two contractions of the Bianchi identity" can be put to work in the expanding universe. Take the spatially flat model $ds^2 = -c^2dt^2 + a(t)^2(dx^2 + dy^2 + dz^2)$. A comoving observer, at rest in these coordinates, measures three quantities: with local instruments, the mass density $\rho$ and pressure $p$ of the cosmic fluid around her, and from the redshifts and distances of nearby galaxies, the Hubble rate $H = \dot a/a$.

Einstein's equation with $\Lambda = 0$, taken on trust here, gives two expansion equations:

$$H^2 = \frac{8\pi G}{3}\rho,\qquad 2\frac{\ddot a}{a} + H^2 = -\frac{8\pi Gp}{c^2}.$$

The identity supplies a third relation for free. The worked example "The Einstein tensor of a flat universe balances" shows that the time component of $\nabla_\mu G^{\mu\nu} = 0$ holds for every $a(t)$. Inserting the expansion equations, as the derivation "Energy budget from the expansion equations" does, gives

$$\dot\rho = -3H\Big(\rho + \frac{p}{c^2}\Big),$$

the time component of $\nabla_\mu T^{\mu\nu} = 0$. For a box that moves with the fluid, with volume $V \propto a^3$, it reads $d(\rho c^2V)/dt = -p\,dV/dt$: the energy in the box changes only by the work its pressure does on the growing walls.

For dust, $p = 0$ and $\rho \propto a^{-3}$, so the mass in the box stays fixed. For radiation that trades no energy with matter, $p = \rho c^2/3$ and $\rho \propto a^{-4}$. Radiation's energy density goes as the fourth power of its temperature, so $T \propto 1/a = 1 + z$, with $a = 1$ today and $z$ the redshift of light emitted when the scale factor was $a$. The microwave background is at 2.7255 K today, so the budget predicts 8.18 K at $z = 2$, and the excitation of molecules in distant gas clouds, warmed by that radiation, follows this scaling.

So the observer can never find both expansion equations holding while the budget fails. Given the first expansion equation, the budget follows from the second, and the second follows from the budget whenever $H \neq 0$.

**Takeaway:** For a comoving observer the identity turns the expansion equations into an energy budget: energy in a box moving with the cosmic fluid changes only by the work its pressure does, so radiation cools as the universe expands.

*What this leaves out:* A spatially flat model with no cosmological constant, and each fluid trading no energy with the others.

*Continues:* `ways_in/two-contractions-of-the-box-rule`<br>*See:* `worked_examples/flat-universe-balance`, `derivations/energy-budget-from-expansion`, `observations/cmb-temperature-at-high-redshift`, `problems/acceleration-equation-for-free`, `checks/radiation-in-a-growing-box`

### 6. What the identity forces, and what it does not · formal · structure

*Under what hypotheses does the identity hold, why must it exist, and what does it force on Einstein's equation?*

The two contractions in "Two contractions of the Bianchi identity" hold on any pseudo-Riemannian manifold $(M, g)$ of dimension $n \geq 2$ with a $C^3$ metric and its Levi-Civita connection. Set $G = c = 1$.

*Theorem.* $\nabla^\mu G_{\mu\nu} = 0$, with $G = \mathrm{Ric} - \tfrac12 R\,g$.

The first contraction needs only zero torsion. The second needs $\nabla g = 0$ twice: to pass $g^{\sigma\mu}$ through $\nabla$, and for antisymmetry of $R_{\rho\sigma\mu\nu}$ in its first pair. For a connection that does not preserve $g$ the step fails, and Ric need not even be symmetric.

*Dimension.* For $n = 2$, $\mathrm{Ric} = \tfrac12 Rg$, so $G \equiv 0$ and the theorem is empty. For $n = 3$ the Riemann tensor is fixed by Ric, and the theorem is equivalent to the full second Bianchi identity. For $n = 4$ it carries 4 of that identity's 20 independent relations at a point.

*Why it must exist.* Let $S[g] = \int L\sqrt{|g|}\,d^nx$ with $L$ a scalar built from $g$ and its derivatives, and define the symmetric $E^{\mu\nu}$ by $\delta S = \int E^{\mu\nu}\delta g_{\mu\nu}\sqrt{|g|}\,d^nx$ for compactly supported variations. Moving points along a compactly supported field $\xi$ changes $g_{\mu\nu}$ by $\nabla_\mu\xi_\nu + \nabla_\nu\xi_\mu$ and leaves $S$ unchanged. Integrating by parts gives $\nabla_\mu E^{\mu\nu} = 0$ for every metric, as the problem "Divergence-free from relabelling" proves. This is an identity of the kind Noether found for symmetries that depend on arbitrary functions. For $L = R$, $E^{\mu\nu} = -G^{\mu\nu}$.

*Consequences.*

- Einstein's equation $G_{\mu\nu} + \Lambda g_{\mu\nu} = 8\pi T_{\mu\nu}$ forces $\nabla^\mu T_{\mu\nu} = 0$. For matter with a diffeomorphism-invariant action the same law follows from the matter's own field equations, so the coupled system is consistent rather than overdetermined. For dust the law is geodesic motion.
- Because the theorem holds for every metric, the four components $G^{0\nu}$ contain no second $x^0$-derivatives of $g$, so the corresponding equations constrain data on a slice. In vacuum, once the six equations $R_{ij} = 0$ hold everywhere, the identity is a linear homogeneous first-order system for the constraint quantities. Under uniqueness conditions, such as analytic data or a hyperbolic formulation, constraints that vanish on one slice keep vanishing.
- In $n = 4$, a symmetric tensor built locally from $g$ and its first two derivatives that is divergence-free for every metric has the form $aG^{\mu\nu} + bg^{\mu\nu}$ (Lovelock). Higher-derivative actions, or $n > 4$, give further divergence-free tensors, so the identity alone does not select the theory.
- On a connected Einstein manifold with $n \geq 3$, $\mathrm{Ric} = fg$ forces $f$ to be constant.

*Limits.* Zero divergence is $n$ equations, far weaker than $\nabla G = 0$. The local law $\nabla_\mu T^{\mu\nu} = 0$ gives a conserved total only with extra structure: for a Killing field $\xi$, $J^\mu = T^\mu{}_\nu\xi^\nu$ obeys $\nabla_\mu J^\mu = 0$, and Gauss's theorem applies. The identity says nothing about which metric nature realises.

**Takeaway:** The Einstein tensor of any metric is divergence-free, as invariance under changes of coordinates demands; this forces conserved sources and constraints, but selects no metric and gives no conserved totals without a symmetry.

*What this leaves out:* Restricted to the Levi-Civita connection; with torsion or a connection that does not preserve the metric, the contractions change.

*Continues:* `ways_in/two-contractions-of-the-box-rule`<br>*Builds on:* [[levi-civita-connection]], [[diffeomorphism-invariance]]<br>*See:* `problems/identity-from-relabelling`, `checks/constraints-without-second-time-derivatives`, `checks/dust-must-fall-freely`, `problems/einstein-space-constant-factor`

## Glossary

| Term | Say | In plain words | Concept |
| --- | --- | --- | --- |
| spacetime | — | Space and time taken together, as one whole in which every event has both a place and a moment. | [[spacetime]] |
| smoothly curved | — | Curved with no sharp tips, tears or sudden jumps anywhere. | — |
| fall freely | — | To move with nothing but gravity acting: no air pushing, and no floor or rope holding you. | [[free-fall]] |
| balance | — | An amount balances when, in every tiny box, it changes only by what flows in or out across the box's walls. Nothing is made or destroyed inside, though the amount can still change over time, like water in a filling bathtub. In curved spacetime the box is carried by someone falling freely, without spinning. Falling freely takes gravity out of the count. Not spinning keeps out the pushes felt on a spinning roundabout, such as the sideways push on anyone walking across it. | [[continuity-equation]] |
| curvature table | — | A table kept at every place that describes the curving there. Some of its entries describe how crumbs let go in a freely falling cabin drift apart or together. | [[riemann-curvature-tensor]] |
| Ricci tensor | REE-chee | A table kept at every place, made by adding up entries of the curvature table. For a small ball of crumbs let go at rest by someone falling freely, it gives the total of their drifts. Where matter fills the space among the crumbs, that total counts the matter right there. | [[ricci-tensor]] |
| Bianchi identity | bee-AHN-kee | The rule that, for an arrow carried around each of the six faces of any tiny box, the three leftovers add up to nothing. It ties how curving changes in one direction to how it changes in the others. | [[bianchi-identity]] |
| leftover | — | What remains after adding the changes of an arrow carried around two opposite faces of a tiny box. | [[bianchi-identity]] |
| grand total | — | One number at each place, made by adding up the entries of the Ricci tensor in a fixed way. | [[ricci-scalar]] |
| Einstein tensor | — | A table made from the Ricci tensor by taking away half its grand total, spread over the table in a fixed way. It balances in every smoothly curved spacetime. | [[einstein-tensor]] |
| contracted Bianchi identity | bee-AHN-kee | The rule that the Einstein tensor balances in every smoothly curved spacetime. It comes from adding up some of the many rules in the Bianchi identity, much as the Ricci tensor adds up entries of the curvature table. | [[contracted-bianchi-identity]] |
| identity | — | A rule that holds whatever the world is like, because of how the things it talks about are built. | — |
| momentum | — | The amount of motion a moving thing carries: its mass times its speed, together with the direction it moves. | — |
| matter table | — | A table kept at every place that lists the energy and momentum of the matter there, and how they flow. | [[stress-energy-tensor]] |
| Einstein's equation | — | The law of gravity in general relativity. It sets the Einstein tensor at each place, plus a tiny extra term that also balances, equal to a fixed number times the matter table there. | [[einstein-field-equations]] |

## Key equations

### Twice-contracted Bianchi identity · working

$$
\nabla_\mu R^\mu{}_\nu = \tfrac12\nabla_\nu R
$$

The divergence of the Ricci tensor equals half the gradient of the Ricci scalar.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $\nabla_\mu R^\mu{}_\nu$ | divergence of the Ricci tensor | the divergence of Ricci |
| $R$ | Ricci scalar, $g^{\mu\nu}R_{\mu\nu}$ | the Ricci scalar |

**Holds when:** Levi-Civita connection of any metric with continuous third derivatives, in any dimension.  
**Say it:** “The divergence of the Ricci tensor equals one half the gradient of the Ricci scalar.”  
**Justified by:** `derivations/contracting-twice`

### Divergence-free Einstein tensor · working

$$
\nabla_\mu G^{\mu\nu} = 0,\qquad G_{\mu\nu} = R_{\mu\nu} - \tfrac12 R\,g_{\mu\nu}
$$

The Einstein tensor has zero divergence, one equation for each free index, whatever the metric.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $G^{\mu\nu}$ | Einstein tensor, symmetric | the Einstein tensor |
| $g_{\mu\nu}$ | metric | the metric |

**Holds when:** Every metric, with its Levi-Civita connection. It does not imply $\nabla_\lambda G_{\mu\nu} = 0$.  
**Say it:** “Nabla mu of G mu nu is zero: the Einstein tensor is divergence-free, for every metric.”  
**Justified by:** `derivations/contracting-twice`

### Conservation forced by Einstein's equation · working

$$
G_{\mu\nu} + \Lambda g_{\mu\nu} = \frac{8\pi G}{c^4}T_{\mu\nu}\;\Longrightarrow\;\nabla_\mu T^{\mu\nu} = 0
$$

The left side of Einstein's equation is divergence-free for every metric, so the equation can hold only for a conserved stress-energy tensor.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $T_{\mu\nu}$ | stress-energy tensor of the matter | the stress-energy tensor |
| $\Lambda$ | cosmological constant | Lambda |

**Holds when:** Einstein's equation holds; $\Lambda$ is constant. The conservation is local.  
**Say it:** “If G mu nu plus Lambda g mu nu equals eight pi G over c to the fourth times T mu nu, then the divergence of T is zero.”  
**Justified by:** `derivations/contracting-twice`

### Energy budget of the cosmic fluid · working

$$
\dot\rho = -3H\Big(\rho + \frac{p}{c^2}\Big)
$$

In a flat expanding universe the density of a fluid changes only through dilution and the work its pressure does.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $\rho$ | mass density measured by a comoving observer | rho |
| $p$ | pressure | the pressure |
| $H$ | Hubble rate $\dot a/a$ | the Hubble rate |

**Holds when:** Spatially flat model with $\Lambda = 0$; a comoving perfect fluid exchanging no energy with other components.  
**Say it:** “Rho dot equals minus three H times rho plus p over c squared.”  
**Justified by:** `derivations/energy-budget-from-expansion`

### Divergence-free tensor from an invariant action · formal

$$
\nabla_\mu E^{\mu\nu} = 0,\qquad \delta S = \int E^{\mu\nu}\,\delta g_{\mu\nu}\sqrt{|g|}\,d^nx
$$

Any metric action invariant under changes of coordinates has a divergence-free field-equation tensor, for every metric; for the scalar curvature it is minus the Einstein tensor.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $S$ | an action built from a scalar function of the metric and its derivatives | the action |
| $E^{\mu\nu}$ | symmetric field-equation tensor of the action | E mu nu |

**Holds when:** Scalar Lagrangian; variations of compact support; no field equation imposed.  
**Say it:** “The divergence of E mu nu vanishes, where E mu nu is the variation of the action with respect to the metric.”  
**Justified by:** `stated`

## Derivations

### Contracting the Bianchi identity twice · working

**Goal:** Derive $\nabla_\mu R^\mu{}_\nu = \tfrac12\nabla_\nu R$, then $\nabla_\mu G^{\mu\nu} = 0$, then conservation of the source of Einstein's equation.

1. Start from the Bianchi identity for the Levi-Civita connection: $\nabla_\lambda R^\rho{}_{\sigma\mu\nu} + \nabla_\mu R^\rho{}_{\sigma\nu\lambda} + \nabla_\nu R^\rho{}_{\sigma\lambda\mu} = 0$.
2. Set $\lambda = \rho$ and sum. Contraction commutes with $\nabla$, so each term is the derivative of a contracted tensor.
3. Use $R_{\sigma\nu} = R^\rho{}_{\sigma\rho\nu}$ and last-pair antisymmetry: $R^\rho{}_{\sigma\nu\rho} = -R_{\sigma\nu}$ and $R^\rho{}_{\sigma\rho\mu} = R_{\sigma\mu}$. So $\nabla_\rho R^\rho{}_{\sigma\mu\nu} = \nabla_\mu R_{\sigma\nu} - \nabla_\nu R_{\sigma\mu}$.
4. Multiply by $g^{\sigma\mu}$ and sum. Because $\nabla g = 0$, $g^{\sigma\mu}$ passes through each $\nabla$, and the right side becomes $\nabla_\mu R^\mu{}_\nu - \nabla_\nu R$.
5. On the left, first-pair antisymmetry $R_{\alpha\sigma\mu\nu} = -R_{\sigma\alpha\mu\nu}$ gives $g^{\sigma\mu}R_{\alpha\sigma\mu\nu} = -R_{\alpha\nu}$, so the left side is $-\nabla_\rho R^\rho{}_\nu$.
6. Equate the two sides: $-\nabla_\rho R^\rho{}_\nu = \nabla_\mu R^\mu{}_\nu - \nabla_\nu R$, so $\nabla_\mu R^\mu{}_\nu = \tfrac12\nabla_\nu R$.
7. Write $\nabla_\nu R = \nabla_\mu(\delta^\mu{}_\nu R)$ to get $\nabla_\mu\big(R^\mu{}_\nu - \tfrac12\delta^\mu{}_\nu R\big) = 0$. Raise $\nu$ with $g^{\nu\alpha}$, again through $\nabla$: $\nabla_\mu G^{\mu\alpha} = 0$.
8. Take the divergence of $G^{\mu\nu} + \Lambda g^{\mu\nu} = (8\pi G/c^4)T^{\mu\nu}$. The left side gives $0 + 0$ for every metric, so $\nabla_\mu T^{\mu\nu} = 0$.

**Result:** $\nabla_\mu R^\mu{}_\nu = \tfrac12\nabla_\nu R$, $\nabla_\mu G^{\mu\nu} = 0$ for every metric, and $\nabla_\mu T^{\mu\nu} = 0$ wherever Einstein's equation holds.

### Energy budget from the expansion equations · working

**Goal:** Show that the expansion equations of a flat universe, with the identity, give $\dot\rho = -3H(\rho + p/c^2)$.

1. The worked example "The Einstein tensor of a flat universe balances" gives, for every $a(t)$, $\frac{d}{dt}(3H^2) + 9H^3 - 3H\big(2\ddot a/a + H^2\big) = 0$.
2. The first expansion equation, $3H^2 = 8\pi G\rho$, turns the first term into $8\pi G\dot\rho$ and the second into $3H(8\pi G\rho)$.
3. The second expansion equation, $2\ddot a/a + H^2 = -8\pi Gp/c^2$, turns the last term into $+3H(8\pi Gp/c^2)$.
4. Divide by $8\pi G$: $\dot\rho + 3H\rho + 3Hp/c^2 = 0$.
5. For a comoving box, $V \propto a^3$ gives $\dot V = 3HV$, so $\frac{d}{dt}(\rho c^2V) = (\dot\rho + 3H\rho)c^2V = -3HpV = -p\dot V$.

**Result:** $\dot\rho = -3H(\rho + p/c^2)$, equivalently $d(\rho c^2V)/dt = -p\,dV/dt$ for a comoving box.

## Worked examples

### The Einstein tensor of a flat universe balances · working

**Problem:** For $ds^2 = -c^2dt^2 + a(t)^2(dx^2 + dy^2 + dz^2)$ with $x^0 = ct$, the Einstein tensor is $G_{00} = 3H^2/c^2$, $G_{0i} = 0$ and $G_{ij} = -(2a\ddot a + \dot a^2)\delta_{ij}/c^2$, with $H = \dot a/a$. Check that $\nabla_\mu G^{\mu\nu} = 0$ for every $a(t)$, although $G_{00}$ changes with time.

1. Raise indices with $g^{00} = -1$ and $g^{ij} = a^{-2}\delta^{ij}$: $G^{00} = 3H^2/c^2$ and $G^{ij} = -(2\ddot a/a + H^2)\delta^{ij}/(a^2c^2)$.
2. The nonzero Christoffel symbols are $\Gamma^0{}_{ij} = a\dot a\,\delta_{ij}/c$ and $\Gamma^i{}_{0j} = \Gamma^i{}_{j0} = (H/c)\,\delta^i{}_j$, so $\Gamma^\mu{}_{\mu 0} = 3H/c$.
3. For a symmetric tensor, $\nabla_\mu G^{\mu\nu} = \partial_\mu G^{\mu\nu} + \Gamma^\mu{}_{\mu\lambda}G^{\lambda\nu} + \Gamma^\nu{}_{\mu\lambda}G^{\mu\lambda}$.
4. For $\nu = 0$, with $\partial_0 = c^{-1}\partial_t$: $\partial_0G^{00} = 6H\dot H/c^3$, $\Gamma^\mu{}_{\mu0}G^{00} = 9H^3/c^3$, and $\Gamma^0{}_{ij}G^{ij} = -3H(2\ddot a/a + H^2)/c^3$.
5. Use $\ddot a/a = \dot H + H^2$: the last term is $-(6H\dot H + 9H^3)/c^3$, which cancels the first two.
6. For $\nu = i$: nothing depends on $x^j$, $G^{0i} = 0$, $\Gamma^\mu{}_{\mu j} = 0$, and $\Gamma^i{}_{\mu\lambda}G^{\mu\lambda} = 2\Gamma^i{}_{0j}G^{0j} = 0$.

**Answer:** $\nabla_\mu G^{\mu\nu} = 0$ for every $a(t)$, while $G_{00} = 3H^2/c^2$ changes whenever $H$ does.

**Takeaway:** The identity holds for any expansion history: zero divergence ties how the components change together, not whether they change.

## Problems

### `water-in-a-tub` · entry · difficulty 1 · calculation

A bathtub holds 60 litres of water. The tap adds 12 litres each minute, and the drain lets out 8 litres each minute. (a) How much water is in the tub after 5 minutes? (b) A friend says the water cannot balance, because the amount in the tub keeps changing. Is your friend right?

**Hints**

1. How many more litres flow in than out each minute?
2. Does balancing mean the amount stays fixed, or that it changes only by flowing in or out?

**Answer:** (a) 80 litres. (b) No. The water balances, because it changes only by what flows in and out.

**Must contain:** Each minute 4 more litres flow in than out; After 5 minutes the tub holds 80 litres; Balancing means changing only by flow, not staying fixed

**Numeric:** water in the tub after 5 minutes, in litres = 80 1 (magnitude, ±0.5)

**Solution**

1. Each minute, 12 litres flow in and 8 flow out. So the tub gains 12 minus 8, which is 4 litres.
2. In 5 minutes it gains 5 times 4, which is 20 litres. So it holds 60 plus 20, which is 80 litres.
3. No water is made from nothing, and none vanishes. Every litre gained came in through the tap, and every litre lost went out through the drain. So the water balances, even though the amount in the tub changes.

**Targets:** `balanced-means-uniform`

### `acceleration-equation-for-free` · working · difficulty 2 · derivation

In a spatially flat expanding universe with $\Lambda = 0$, take as given the first expansion equation $H^2 = 8\pi G\rho/3$ and the energy budget $\dot\rho = -3H(\rho + p/c^2)$, where $H = \dot a/a$. Derive $\ddot a/a$, and show that it satisfies the second expansion equation $2\ddot a/a + H^2 = -8\pi Gp/c^2$. Where does the argument fail?

**Hints**

1. Differentiate the first expansion equation with respect to time.
2. Use $\ddot a/a = \dot H + H^2$.

**Answer:** $\ddot a/a = -\tfrac{4\pi G}{3}(\rho + 3p/c^2)$, which satisfies the second expansion equation. The argument divides by $H$, so it fails at an instant when $H = 0$.

**Must contain:** When H is not zero, H dot equals minus four pi G times rho plus p over c squared; a double dot over a equals minus four pi G over three times rho plus three p over c squared; The argument fails where H is zero

**Solution**

1. Differentiate $H^2 = 8\pi G\rho/3$: $2H\dot H = \tfrac{8\pi G}{3}\dot\rho$.
2. Insert the budget: $2H\dot H = -8\pi GH(\rho + p/c^2)$.
3. If $H \neq 0$, divide by $2H$: $\dot H = -4\pi G(\rho + p/c^2)$.
4. Then $\ddot a/a = \dot H + H^2 = -4\pi G(\rho + p/c^2) + \tfrac{8\pi G}{3}\rho = -\tfrac{4\pi G}{3}(\rho + 3p/c^2)$.
5. Check: $2\ddot a/a + H^2 = -\tfrac{8\pi G}{3}(\rho + 3p/c^2) + \tfrac{8\pi G}{3}\rho = -8\pi Gp/c^2$, the second expansion equation.
6. At an instant with $H = 0$ the first step reads $0 = 0$ and fixes no acceleration, so there the second equation says something the other two do not.

### `einstein-space-constant-factor` · formal · difficulty 2 · proof

(a) On a connected pseudo-Riemannian manifold of dimension $n \geq 3$, suppose $R_{\mu\nu} = f\,g_{\mu\nu}$ for a smooth function $f$. Prove that $f$ is constant, and say why the argument fails for $n = 2$. (b) In four dimensions with $G = c = 1$, suppose Einstein's equation holds with the source $T_{\mu\nu} = -\lambda(x)\,g_{\mu\nu}/8\pi$ and nothing else. Show that $\lambda$ is constant.

**Hints**

1. Compute $R$ and $\nabla_\mu R^\mu{}_\nu$ from the assumed form, using $\nabla g = 0$.
2. For part (b), take the divergence of both sides of Einstein's equation.

**Answer:** (a) The identity gives $(1 - n/2)\,\partial_\nu f = 0$, so $f$ is constant for $n \geq 3$. For $n = 2$ the factor vanishes and $f$ is the Gaussian curvature, which varies on an ellipsoid. (b) $\partial_\nu\lambda = 0$: a vacuum energy that varied from place to place, with nothing to exchange energy with, could not source Einstein's equation.

**Must contain:** The Ricci scalar is n times f; The identity gives one minus n over two times the gradient of f equals zero; In two dimensions every metric has this form and f may vary; The divergence of minus lambda times the metric is minus the gradient of lambda

**Solution**

1. $R = g^{\mu\nu}R_{\mu\nu} = nf$ and $R^\mu{}_\nu = f\,\delta^\mu{}_\nu$.
2. Since $\nabla g = 0$, $\nabla_\mu R^\mu{}_\nu = \partial_\nu f$ and $\tfrac12\nabla_\nu R = \tfrac n2\,\partial_\nu f$.
3. The contracted identity equates them: $(1 - \tfrac n2)\,\partial_\nu f = 0$.
4. For $n \geq 3$ the factor is nonzero, so $df = 0$, and on a connected manifold $f$ is constant.
5. For $n = 2$, $R_{\mu\nu} = \tfrac12 R\,g_{\mu\nu}$ holds for every metric, so $f = K$, the Gaussian curvature, which varies on an ellipsoid; the identity is empty there.
6. (b) Einstein's equation gives $G_{\mu\nu} = -\lambda\,g_{\mu\nu}$. Its divergence is $0 = \nabla_\mu G^\mu{}_\nu = -\partial_\nu\lambda$, so $\lambda$ is constant.

### `identity-from-relabelling` · formal · difficulty 3 · proof

Let $S[g] = \int_U L\sqrt{-g}\,d^4x$, where $L$ is a scalar built from the metric and its derivatives, and define the symmetric tensor $E^{\mu\nu}$ by $\delta S = \int_U E^{\mu\nu}\delta g_{\mu\nu}\sqrt{-g}\,d^4x$ for variations supported inside $U$. (a) Moving points along a vector field $\xi$ that vanishes near the boundary of $U$ varies the metric by $\delta g_{\mu\nu} = \nabla_\mu\xi_\nu + \nabla_\nu\xi_\mu$. Use this to prove $\nabla_\mu E^{\mu\nu} = 0$ for every metric. (b) Given $\delta(\sqrt{-g}R) = \sqrt{-g}\,G_{\mu\nu}\delta g^{\mu\nu}$ plus a total derivative, find $E^{\mu\nu}$ for $L = R$.

**Hints**

1. Why does moving points along $\xi$ leave $S$ unchanged?
2. Integrate $E^{\mu\nu}\nabla_\mu\xi_\nu$ by parts; the boundary term vanishes.
3. Use $\delta g^{\mu\nu} = -g^{\mu\alpha}g^{\nu\beta}\delta g_{\alpha\beta}$.

**Answer:** (a) $0 = \delta S = 2\int_U E^{\mu\nu}\nabla_\mu\xi_\nu\sqrt{-g}\,d^4x = -2\int_U(\nabla_\mu E^{\mu\nu})\xi_\nu\sqrt{-g}\,d^4x$ for every such $\xi$, so $\nabla_\mu E^{\mu\nu} = 0$. (b) $E^{\mu\nu} = -G^{\mu\nu}$, so the contracted Bianchi identity follows from invariance alone.

**Must contain:** A change of coordinates that is the identity near the boundary leaves the action unchanged; The metric changes by the Lie derivative along xi; Integration by parts turns the variation into minus twice the divergence of E contracted with xi; For the Einstein-Hilbert action E is minus the Einstein tensor

**Solution**

1. Moving points along the flow of $\xi$ is a change of coordinates inside $U$ that is the identity near its boundary. $L\sqrt{-g}\,d^4x$ is invariant, so $S$ does not change and $\delta S = 0$ to first order.
2. The first-order change of the metric is its Lie derivative, $\delta g_{\mu\nu} = \nabla_\mu\xi_\nu + \nabla_\nu\xi_\mu$, which has compact support in $U$.
3. Since $E^{\mu\nu}$ is symmetric, $\delta S = 2\int_U E^{\mu\nu}\nabla_\mu\xi_\nu\sqrt{-g}\,d^4x$.
4. Write $E^{\mu\nu}\nabla_\mu\xi_\nu = \nabla_\mu(E^{\mu\nu}\xi_\nu) - (\nabla_\mu E^{\mu\nu})\xi_\nu$. The first term integrates to a boundary term, which vanishes because $\xi = 0$ near the boundary.
5. So $\int_U(\nabla_\mu E^{\mu\nu})\xi_\nu\sqrt{-g}\,d^4x = 0$ for every such $\xi$, which forces $\nabla_\mu E^{\mu\nu} = 0$ at every point of $U$. No field equation was used.
6. (b) With $\delta g^{\mu\nu} = -g^{\mu\alpha}g^{\nu\beta}\delta g_{\alpha\beta}$, $\delta(\sqrt{-g}R) = -\sqrt{-g}\,G^{\alpha\beta}\delta g_{\alpha\beta}$ plus a total derivative, whose integral vanishes for variations supported in $U$. So $E^{\mu\nu} = -G^{\mu\nu}$ and $\nabla_\mu G^{\mu\nu} = 0$.

## Observations

- **The temperature of the cosmic microwave background in the distant past, read from molecules in far-away gas clouds** (measured, working). The energy budget $\dot\rho = -3H(\rho + p/c^2)$, which the expansion equations contain because of the contracted identity, gives $\rho \propto a^{-4}$ for radiation and so $T \propto 1 + z$. Carbon monoxide in gas clouds at high redshift is excited by the background radiation, and the excitation temperatures inferred from its absorption lines follow this scaling. The measurement tests the energy balance of the radiation, which the identity makes a consequence of the expansion equations; it does not test the identity itself, which holds for every metric. *Numbers:* Today $T_0 = 2.7255$ K, so the scaling predicts $8.18$ K at $z = 2$. Fitting $T(z) = T_0(1 + z)^{1 - \beta}$ to these and other measurements gives $\beta = -0.007 \pm 0.027$, consistent with zero. *Reference:* Pasquier Noterdaeme, Patrick Petitjean, Raghunathan Srianand, Cédric Ledoux, Sebastián López (2011), *The evolution of the cosmic microwave background temperature: Measurements of T_CMB at high redshift from carbon monoxide excitation*, Astronomy & Astrophysics 526, L7, doi:10.1051/0004-6361/201016140

## Teaching arc

1. **Picture balance** (entry). Run the hose and the tub, then state that the Einstein tensor balances in every tiny box of every smoothly curved spacetime. *Why:* Balance must mean changing only by flow before any curving appears. *Predict:* Water moves faster where the hose narrows. Is water being made there? *Visual:* [[counting-box-in-a-narrowing-hose]] *Uses:* `ways_in/a-table-of-curving-that-balances`, `checks/sun-and-empty-space`
2. **Separate identity from law** (entry). Add up a grid whose rows each total zero, then show the balance is the Bianchi identity added up, so it holds with or without matter. *Why:* Learners otherwise think the curving balances because matter does. *Predict:* In an invented spacetime where energy could appear from nothing, would the Einstein tensor still balance? *Uses:* `ways_in/true-in-every-curved-spacetime`, `checks/invented-spacetime`
3. **Break the first guess** (entry). Set the Ricci tensor equal to matter and follow the balance to an evenly spread universe. *Why:* A plausible law that fails shows why the half is needed rather than decorative. *Predict:* If the Ricci tensor had to balance, what would that say about how matter is spread? *Visual:* [[dial-the-half-beside-a-star]] *Uses:* `ways_in/the-first-guess-would-forbid-stars`, `checks/first-guess-and-a-planet`
4. **Contract twice** (working). Derive the twice-contracted identity, naming both uses of the metric, then find the coefficient. *Why:* The derivation is short and shows the result is pure geometry. *Predict:* Which multiple of the Ricci scalar times the metric makes the divergence vanish for every metric? *Visual:* [[dial-the-half-beside-a-star]] *Uses:* `ways_in/two-contractions-of-the-box-rule`, `derivations/contracting-twice`, `checks/coefficient-of-the-half`
5. **Balance a universe** (working). Check the identity on a flat expanding universe, then turn the expansion equations into the energy budget of radiation. *Why:* It puts the identity to work on a measurement and separates zero divergence from constancy. *Uses:* `ways_in/energy-budget-of-an-expanding-universe`, `worked_examples/flat-universe-balance`, `problems/acceleration-equation-for-free`, `observations/cmb-temperature-at-high-redshift`
6. **Mark what it forces** (formal). State the hypotheses, derive the identity from invariance, then draw out constraints and the motion of dust. *Why:* Graduate readers need its origin and its limits. *Uses:* `ways_in/what-the-identity-forces`, `problems/identity-from-relabelling`, `checks/constraints-without-second-time-derivatives`, `checks/dust-must-fall-freely`

## Misconceptions

### “If the Einstein tensor balances, it must be the same everywhere.” · entry · `balanced-means-uniform`

- **Why it is tempting:** Balancing sounds like nothing changes.
- **What is true:** Balancing means an amount changes only by flowing, not that it is equal everywhere. Water speeds up in the narrow part of a hose, and the Einstein tensor is far larger inside the Sun than around it, yet both balance.
- **Exposed by:** `checks/sun-and-empty-space`

### “Einstein could just as well have set the Ricci tensor equal to matter; the half of the grand total is a detail.” · entry · `ricci-could-equal-matter`

- **Why it is tempting:** The Ricci tensor already counts the matter right where it is.
- **What is true:** The Ricci tensor fails to balance wherever its grand total changes. Setting it equal to matter would force its grand total, and with it the density of ordinary matter, to be the same everywhere, so no star could exist.
- **Exposed by:** `checks/first-guess-and-a-planet`

### “The Einstein tensor balances because the energy of matter balances.” · entry · `balance-comes-from-matter`

- **Why it is tempting:** The two balances appear side by side in Einstein's equation.
- **What is true:** The Einstein tensor balances in every smoothly curved spacetime, with or without matter, because its balance comes from adding up the Bianchi identity. It is Einstein's equation that passes this balance on to matter.
- **Exposed by:** `checks/invented-spacetime`

### “A divergence-free tensor, such as the Einstein tensor, must be covariantly constant.” · working · `divergence-free-means-constant`

- **Why it is tempting:** People say its derivative vanishes and drop the word divergence.
- **What is true:** Zero divergence is four equations on one contraction of the derivative, far weaker than every component of the derivative vanishing. In an expanding universe the density and the Einstein tensor change with time while both stay divergence-free.
- **Exposed by:** `checks/radiation-in-a-growing-box`

### “Since the divergence of the stress-energy tensor vanishes, the total energy in any region of curved spacetime stays constant.” · working · `local-balance-means-conserved-total`

- **Why it is tempting:** In flat spacetime the same-looking equation does give conserved totals.
- **What is true:** The covariant law is local and gives a conserved total only with a symmetry such as a time-translation Killing vector. Radiation in a comoving box of an expanding universe loses energy while obeying the local law.
- **Exposed by:** `checks/radiation-in-a-growing-box`

### “Einstein's equation fixes the geometry, and how matter moves must be added as separate equations.” · formal · `field-equation-silent-on-motion`

- **Why it is tempting:** In Newtonian gravity, Poisson's equation says nothing about how the source moves.
- **What is true:** Through the contracted identity, Einstein's equation forces its source to be conserved, which for dust is geodesic motion. Matter's own equations must agree with this rather than add to it freely.
- **Exposed by:** `checks/dust-must-fall-freely`

## Checks

1. **Entry · evaluate-claim** `checks/sun-and-empty-space`. The Einstein tensor is far larger inside the Sun than in the nearly empty space around it. A friend says: 'So it changes from place to place, and it cannot balance.' Is your friend right?
   - **Hints:** Does water in a narrowing hose move at the same speed everywhere?
   - **Answer:** No. An amount balances when, in every tiny box, it changes only by what flows in or out. That rule says nothing about the amount being the same everywhere. Water in a pinched hose moves twice as fast where the opening has half the area, yet no water appears or vanishes in any box. In the same way, the Einstein tensor can be large inside the Sun, where the Ricci tensor counts the Sun's matter, and nearly zero in the empty space outside. It still balances in every tiny box, because the contracted Bianchi identity holds in every smoothly curved spacetime.
   - **Must contain:** Your friend is wrong; Balancing means changing only by flow, not being the same everywhere; The identity holds in every smoothly curved spacetime
   - **Targets:** `balanced-means-uniform`
   - **Visual:** [[counting-box-in-a-narrowing-hose]]
2. **Entry · explain** `checks/first-guess-and-a-planet`. Suppose the law of gravity set the Ricci tensor equal to a fixed number times the matter table. A planet made of rock floats in nearly empty space. Explain step by step why this guess cannot describe the planet.
   - **Hints:** What must be true of any table set equal to the matter table? / When does the Ricci tensor fail to balance?
   - **Answer:** Energy and momentum balance, so the matter table balances. Under the guess, the Ricci tensor is a fixed number times the matter table, so the Ricci tensor must balance too. But the Ricci tensor fails to balance wherever its grand total changes, by half of that change. So its grand total could not change from place to place. The guess ties that grand total to the grand total of the matter table, and for rock that comes almost entirely from the mass in each cubic metre. So the rock would have to be as dense as the empty space around it. A cubic metre of rock holds thousands of kilograms, and a cubic metre of nearly empty space holds almost nothing. So the guess fails.
   - **Must contain:** Under the guess the Ricci tensor must balance, like matter; The Ricci tensor fails to balance by half the change in its grand total; So rock and empty space would need the same density
   - **Targets:** `ricci-could-equal-matter`
   - **Visual:** [[dial-the-half-beside-a-star]]
3. **Entry · evaluate-claim** `checks/invented-spacetime`. A friend says: 'The Einstein tensor balances only because energy balances. In an invented curved spacetime where energy could appear from nothing, the Einstein tensor would fail to balance too.' Is she right?
   - **Hints:** What did the reason for the Bianchi identity use?
   - **Answer:** No. The balance of the Einstein tensor comes from adding up the Bianchi identity. The Bianchi identity uses only how tiny changes add and how the edges of a box are shared, not what fills the spacetime. Adding up a rule that always holds gives a rule that always holds. So the balance holds in every smoothly curved spacetime, invented or real, whatever its matter does. The link runs the other way. Einstein's equation ties the Einstein tensor to the matter table. So wherever that equation holds, matter must balance. In the invented spacetime, Einstein's equation would simply fail.
   - **Must contain:** She is wrong; The balance comes from adding up the Bianchi identity; Einstein's equation passes the balance to matter
   - **Targets:** `balance-comes-from-matter`
4. **Working · derive** `checks/coefficient-of-the-half`. For constants $A$, $B$ and $\Lambda$, show that $\nabla_\nu(AR^{\mu\nu} + BRg^{\mu\nu} + \Lambda g^{\mu\nu})$ vanishes for every metric only if $B = -A/2$, whatever $\Lambda$. Why can a single metric not decide?
   - **Hints:** Which terms does $\nabla g = 0$ simplify?
   - **Answer:** Metric compatibility gives $\nabla_\nu(\Lambda g^{\mu\nu}) = 0$ and $\nabla_\nu(BRg^{\mu\nu}) = B\nabla^\mu R$. The contracted identity gives $\nabla_\nu(AR^{\mu\nu}) = \tfrac A2\nabla^\mu R$. The total is $(\tfrac A2 + B)\nabla^\mu R$. Metrics with $\nabla R \neq 0$ exist: the flat universe with $a \propto t^{2/3}$ has $R = 6(\ddot a/a + H^2)/c^2 = 4/(3c^2t^2)$. So the divergence vanishes for every metric only if $B = -A/2$. A metric with constant $R$, such as a round sphere or the Schwarzschild spacetime, gives zero for every $B$, so it cannot decide.
   - **Must contain:** The divergence is A over two plus B times the gradient of R; A varying Ricci scalar forces B equals minus A over two
   - **Visual:** [[dial-the-half-beside-a-star]]
5. **Working · numeric** `checks/radiation-in-a-growing-box`. A flat expanding universe is filled with radiation, $p = \rho c^2/3$. Use $\dot\rho = -3H(\rho + p/c^2)$ to find how $\rho$ depends on $a$. By what factor does the energy in a box that moves with the radiation change when $a$ doubles? Does the change contradict $\nabla_\mu T^{\mu\nu} = 0$?
   - **Hints:** Write $\dot\rho/\rho$ in terms of $\dot a/a$ and integrate.
   - **Answer:** With $p = \rho c^2/3$, $\dot\rho = -4H\rho = -4\rho\,\dot a/a$, so $\rho \propto a^{-4}$. The box's volume grows as $a^3$, so its energy $\rho c^2V \propto a^{-1}$ falls to $0.5$ of its value when $a$ doubles. There is no contradiction. The budget reads $d(\rho c^2V)/dt = -p\,dV/dt$, so the energy lost is the work the radiation's pressure does on the growing box. $\nabla_\mu T^{\mu\nu} = 0$ is a local balance. It therefore does not make $T^{\mu\nu}$ constant, since $\rho$ falls as $a^{-4}$. Nor does it give a conserved total by itself: that needs a symmetry as well, such as a time-translation Killing vector, which this radiation-filled universe lacks.
   - **Must contain:** Rho falls as the scale factor to the minus four; The energy in the box halves; Local balance gives neither constancy nor a conserved total
   - **Numeric:** factor by which the energy in the box changes when a doubles = 0.5 1 (magnitude, ±0.01)
   - **Targets:** `local-balance-means-conserved-total`, `divergence-free-means-constant`
6. **Formal · explain** `checks/constraints-without-second-time-derivatives`. In coordinates $(x^0, x^i)$, the Einstein tensor is linear in second derivatives of $g_{\mu\nu}$, with coefficients built from $g$ and its first derivatives. Use $\nabla_\mu G^{\mu\nu} = 0$ to show that the four components $G^{0\nu}$ contain no second derivatives of the metric with respect to $x^0$. What does this mean for Einstein's equation?
   - **Hints:** Move $\partial_0 G^{0\nu}$ to one side and count time derivatives in each term.
   - **Answer:** Write the identity as $\partial_0 G^{0\nu} = -\partial_i G^{i\nu} - \Gamma^\mu{}_{\mu\lambda}G^{\lambda\nu} - \Gamma^\nu{}_{\mu\lambda}G^{\mu\lambda}$. Each term on the right contains at most second $x^0$-derivatives of $g$: $\partial_i$ adds only a spatial derivative, and the $\Gamma G$ products add none to $G$. If $G^{0\nu}$ contained $\partial_0^2 g$, the left side would contain $\partial_0^3 g$ with coefficients built from $g$, and nothing on the right could cancel them. The identity holds for every metric, so those coefficients must vanish. So the four equations $G^{0\nu} + \Lambda g^{0\nu} = 8\pi T^{0\nu}$, with $G = c = 1$, restrict the data on a slice of constant $x^0$ rather than evolving them: they are constraints, and only six components can serve as evolution equations.
   - **Must contain:** The right side of the identity has at most second time derivatives; So G zero nu cannot contain second time derivatives; The four equations are constraints on initial data
7. **Formal · derive** `checks/dust-must-fall-freely`. Set $G = c = 1$. Einstein's equation $G_{\mu\nu} = 8\pi T_{\mu\nu}$ holds with dust, $T^{\mu\nu} = \rho u^\mu u^\nu$, where $u_\mu u^\mu = -1$ and $\rho > 0$. Show that the mass current of the dust is conserved and that its worldlines are geodesics.
   - **Hints:** Contract with $u_\nu$.
   - **Answer:** The contracted identity makes the divergence of the left side vanish, so $\nabla_\mu(\rho u^\mu u^\nu) = 0$, that is $\nabla_\mu(\rho u^\mu)\,u^\nu + \rho\,u^\mu\nabla_\mu u^\nu = 0$. Differentiating $u_\nu u^\nu = -1$ gives $u_\nu\nabla_\mu u^\nu = 0$. Contracting with $u_\nu$ therefore gives $-\nabla_\mu(\rho u^\mu) = 0$: the mass current $\rho u^\mu$ is conserved. The remaining term is $\rho\,u^\mu\nabla_\mu u^\nu = 0$, and $\rho > 0$ gives $u^\mu\nabla_\mu u^\nu = 0$, the geodesic equation. The field equation alone decides how the dust moves.
   - **Must contain:** Contracting with u gives a conserved mass current; The rest is the geodesic equation
   - **Targets:** `field-equation-silent-on-motion`

## Notation traps

| Issue | Course choice | Variants you will meet |
| --- | --- | --- |
| Which statement the name contracted Bianchi identity refers to | The twice-contracted statement $\nabla_\mu R^\mu{}_\nu = \tfrac12\nabla_\nu R$, equivalently $\nabla_\mu G^{\mu\nu} = 0$. The intermediate $\nabla_\rho R^\rho{}_{\sigma\mu\nu} = \nabla_\mu R_{\sigma\nu} - \nabla_\nu R_{\sigma\mu}$ is the once-contracted identity. $G^{\mu\nu}$ is symmetric, so the divergence may be taken on either index. | Some texts call the once-contracted form the contracted Bianchi identities and the final form the twice-contracted ones, or simply the Bianchi identities. |
| Signs of the Ricci scalar and of the cosmological term | Signature $(-,+,+,+)$, a sphere of radius $a$ has $R = +2/a^2$, and Einstein's equation is $G_{\mu\nu} + \Lambda g_{\mu\nu} = (8\pi G/c^4)T_{\mu\nu}$. | With signature $(+,-,-,-)$ and the same Riemann convention, $R$ and mixed components such as $G^\mu{}_\nu$ change sign while $R_{\mu\nu}$, $G_{\mu\nu}$ and $G^{\mu\nu}$ do not, and the cosmological term may appear as $-\Lambda g_{\mu\nu}$ with the same physics. The identity is homogeneous, so it reads the same in every convention. |

## Visuals

- ★ [[dial-the-half-beside-a-star]] (flagship): Flagship: only one multiple of the Ricci scalar makes a table of curving balance everywhere, for a star and for an expanding universe. *Sketch:* A star of adjustable density sits in nearly empty space; a second scene runs a dust-filled expanding universe forward in time. The learner predicts, then turns a dial for $B$ in $R^{\mu\nu} + BRg^{\mu\nu}$ and a slider for $\Lambda$. A colour map and a time plot show the imbalance $(\tfrac12 + B)\nabla^\nu R$, which vanishes everywhere only at $B = -\tfrac12$, whatever $\Lambda$.
- [[counting-box-in-a-narrowing-hose]] (core): The entry picture of balance: flow that changes along a hose while every tiny box balances. *Sketch:* Water flows through a hose that narrows and widens. The learner drags a small counting box along it; readouts show litres per second flowing in, flowing out, and piling up, with in and out always equal. A switch to a bathtub with a tap and a drain shows an amount that piles up by exactly in minus out. A last panel shows the Einstein tensor inside and around a star, large inside and nearly zero outside, with the same zero imbalance in every box.

## Tutor moves

**Open with**

- Picture water running through a garden hose that narrows in the middle. The water moves faster in the narrow part. Is water being made there, or does something else explain the faster flow? *(prediction)*

**If the learner is stuck**

- *The learner treats balanced as meaning the same everywhere.* → Return to the hose: count the water into and out of a box in the wide part and in the narrow part, then compare with the Sun. *Uses:* `ways_in/a-table-of-curving-that-balances`, `checks/sun-and-empty-space`
- *The learner cannot say why the Einstein tensor balances when no matter is present.* → Do the three-by-three grid: rows that each add to zero force a zero total, whatever the numbers. Then name the rows as the Bianchi identity. *Uses:* `ways_in/true-in-every-curved-spacetime`, `checks/invented-spacetime`

**Common questions**

- *Does this identity prove that energy is conserved?* (entry) Not by itself. The identity holds in every smoothly curved spacetime, whatever matter does. Only when Einstein's equation ties the Einstein tensor to matter does that equation force the energy and momentum of matter to balance in every tiny box. Matter obeys its own laws of motion too, and those give the same balance, so the two stories fit together. Balancing in every tiny box does not by itself give one fixed total of energy for a whole galaxy or universe. Each tiny box is carried by its own freely falling person, and in curved spacetime their counts cannot in general simply be added. For example, take light crossing the expanding universe. Each galaxy along the light's path is moving away from the galaxy before it, because the universe expands. So an astronomer in each galaxy measures a longer wave, and less energy, than an astronomer in the galaxy before it measured. *Uses:* `ways_in/the-first-guess-would-forbid-stars`, `ways_in/true-in-every-curved-spacetime`, `checks/invented-spacetime`

**Switching levels**

- To working when: uses index notation; asks where the half comes from. Go to the two contractions and the coefficient check. *Uses:* `ways_in/two-contractions-of-the-box-rule`, `checks/coefficient-of-the-half`
- To formal when: asks why the identity has to exist; asks how many of Einstein's equations are independent. Give the invariance argument, then the constraint count. *Uses:* `ways_in/what-the-identity-forces`, `checks/constraints-without-second-time-derivatives`
- To research when: asks about numerical relativity, higher-dimensional gravity, or the total energy of a spacetime. Open the research horizon. *Uses:* `research_horizon/constraint-damping`, `research_horizon/lovelock-gravity`, `research_horizon/energy-in-general-relativity`

**Pronunciations:** Bianchi → bee-AHN-kee; Ricci → REE-chee; Riemann → REE-mahn; Levi-Civita → LEH-vee CHEE-vee-tah; Friedmann → FREED-mahn; Noether → NUR-tuh; Voss → FOSS; Fourès-Bruhat → foo-REZ brew-AH

**Voice notes:** Say 'balances' at the entry rung and 'is divergence-free' at the working rung, never 'the Einstein tensor is conserved', which learners hear as constant.

## History

- **Aurel Voss (1880).** Derived a contracted form of the differential curvature identity, decades before it was used in gravitation. Aurel Voss (1880), *Zur Theorie der Transformation quadratischer Differentialausdrücke und der Krümmung höherer Mannigfaltigkeiten*, Mathematische Annalen 16, 129–179, doi:10.1007/BF01446384
- **Albert Einstein (1915).** Earlier in November 1915 Einstein set a Ricci-type tensor proportional to the energy-momentum tensor. This paper of 25 November added the trace term and gave the final field equations, compatible with conservation of energy and momentum. Albert Einstein (1915), *Die Feldgleichungen der Gravitation*, Sitzungsberichte der Königlich Preußischen Akademie der Wissenschaften (Berlin), 844–847
- **Emmy Noether (1918).** Showed that symmetries depending on arbitrary functions force identities among field equations; for the freedom to change coordinates in general relativity these are the contracted Bianchi identities. Emmy Noether (1918), *Invariante Variationsprobleme*, Nachrichten von der Gesellschaft der Wissenschaften zu Göttingen, Mathematisch-Physikalische Klasse 1918, 235–257

## Research horizon

- **Constraint propagation and damping in numerical relativity.** Through the contracted identity, constraints that hold on an initial slice keep holding under exact evolution, which underlies the local existence theorem for Einstein's equation. In simulations, numerical error excites constraint violations, so modern formulations add terms that damp them. A damped harmonic formulation carried the first simulations of binary black holes through orbit, merger and ringdown. Yvonne Fourès-Bruhat (1952), *Théorème d'existence pour certains systèmes d'équations aux dérivées partielles non linéaires*, Acta Mathematica 88, 141–225, doi:10.1007/BF02392131; Carsten Gundlach, Gioel Calabrese, Ian Hinder, José M. Martín-García (2005), *Constraint damping in the Z4 formulation and harmonic gauge*, Classical and Quantum Gravity 22, 3767–3773, doi:10.1088/0264-9381/22/17/025; Frans Pretorius (2005), *Evolution of binary black-hole spacetimes*, Physical Review Letters 95, 121101, doi:10.1103/PhysRevLett.95.121101
- **Lovelock gravity.** In four dimensions the Einstein tensor and the metric are the only symmetric divergence-free tensors built locally from the metric and its first two derivatives. In more dimensions, higher-curvature Lovelock tensors such as the Gauss–Bonnet tensor also qualify, and they give field equations that stay second order. Theories in four dimensions that escape the theorem must add fields, higher derivatives or nonlocal terms. David Lovelock (1971), *The Einstein tensor and its generalizations*, Journal of Mathematical Physics 12, 498–501, doi:10.1063/1.1665613; David Lovelock (1972), *The four-dimensionality of space and the Einstein tensor*, Journal of Mathematical Physics 13, 874–876, doi:10.1063/1.1666069
- **Energy and momentum of a spacetime.** The local balance does not in general integrate to conserved totals, so total energy needs extra structure: a Killing symmetry, asymptotic flatness, or a quasi-local construction on a finite surface. The ADM energy of an isolated system is the best-known total, and quasi-local definitions remain an active and unsettled field. Richard Arnowitt, Stanley Deser, Charles W. Misner (1962), *The dynamics of general relativity*, In Gravitation: An Introduction to Current Research, ed. L. Witten, Wiley, New York, 227–265, arXiv:gr-qc/0405109; László B. Szabados (2009), *Quasi-local energy-momentum and angular momentum in general relativity*, Living Reviews in Relativity 12, 4, doi:10.12942/lrr-2009-4

## Review: novice

**Verdict:** fixed (2026-09-13, revision 8)

**Retell attempt:** Water in a hose that gets narrower speeds up, but none is made, so it balances: in every tiny box it only changes by what flows in or out, and a bathtub balances too even while it fills. Spacetime has tables made from curving, and one of them, the Einstein tensor, always balances in any curved spacetime because of the box rule somehow. I didn't follow how adding up leftovers 'the way the Ricci tensor adds up drifts' gives that, why the box has to be carried by someone falling, or whether that box is the same as the box rule's box. It's big inside the Sun and tiny outside but still balances, though I don't know why it's big in the Sun. Einstein first tried setting the Ricci tensor equal to matter, but matter balances and the Ricci tensor is off by half the change in its grand total, so the grand total couldn't change and matter would have to be spread evenly, which rules out stars. Adjusting by half the grand total fixes it. I don't see why the grand total is basically the mass, or what 'trading energy with gravity' means.

Second independent reading, revision 5, 13 September 2026, before any fix: Water in a hose cannot pile up anywhere, so where the hose is pinched it has to go faster. That is what balancing means: in any tiny box the amount changes only by what flows in or out, so a filling bathtub balances too. Spacetime has tables made from its curving, and one of them, the Einstein tensor, balances in a tiny box carried by someone falling freely, freely so that gravity drops out of the count. Balancing is not being the same everywhere: the Einstein tensor is huge inside the Sun and almost nothing outside, and it still balances. It balances in every smoothly curved spacetime because it comes from adding up the Bianchi identity, the way a grid whose rows each add to zero has all nine numbers adding to zero, and the reason for the Bianchi identity never mentions what fills the space. Einstein first thought of setting the Ricci tensor equal to matter, but matter balances and the Ricci tensor balances only where its grand total stays put, so everything would have to be spread evenly and no star could exist; taking away half the grand total fixes that and gives the Einstein tensor. What I could not say back: which way round you walk the six faces of the box, what 'how the edges of a box are shared' means, and what a box stretching along time is. I also had to read the line about galaxies measuring the light twice.

**Stumbles (24)**

- “Water running through a hose with no taps or holes balances. In every tiny box, as much water flows out as flows in.”: The summary uses 'balances' before saying what it means, and 'as much flows out as in' is true only once the hose is full and running steadily, so it teaches balance as 'nothing changes'.
- “Einstein's equation sets that table equal to matter”: False for a reader who never sees simplifies: the equation has a fixed number and a tiny extra term.
- “Turn on a garden hose that narrows in the middle. Each second, 3 litres of water enter its wide end.”: A hose narrowed in the middle has two wide ends, and 3 litres each second is about ten times what a garden hose delivers, so the everyday number feels wrong.
- “No tap adds water inside the box, and no hole lets water escape. So each second, as much water leaves the box as enters it.”: A step is missing: a bathtub also has no tap inside it, yet water piles up. The real reason is that the box is always full and water cannot be squeezed.
- “Where the hose has half as much room across, the water moves twice as fast. It has to, because the same 3 litres pass through every part of the hose each second.”: 'Half as much room across' could mean half the width, which would be a quarter of the area; and why the same litres pass every part is left implicit.
- “When an amount obeys this rule in every tiny box, we say it balances.”: Reread: 'this rule' was stated for the whole tub, not for tiny boxes.
- “The same amount of water passes both places each second, so where it moves faster, the stream must be thinner.”: The try-it takes the equal amounts on trust.
- “Take a tiny box carried by someone falling freely.”: A rule with no reason: why must the box fall?
- “Why does it always hold? Start from the box rule. Add up its leftovers the way the Ricci tensor adds up drifts. Most of the detail cancels, and the balance of the Einstein tensor is what remains.”: Rule 17: after learning what balance is and that the Einstein tensor balances, the reader must also take in why an identity holds everywhere. The step is taken on trust without saying so, and the Ricci tensor is made by adding entries of the curvature table, not by adding drifts.
- “The Bianchi identity, the box rule ... Start from the box rule ... Adding up the box rule”: One word for two ideas: 'box' is both the counting box of balance and the six-faced box of arrows, so 'the box rule' reads like the rule about balance in every tiny box.
- “the three leftovers of any tiny box add up to nothing”: The recap uses 'leftovers' and the curving table without saying what they are, so an out-of-sequence reader cannot follow it.
- “every smoothly curved spacetime”: 'Smoothly' is undefined, and a teenager's first what-if is a sharp tip or a tear.
- “The box rule holds in every smoothly curved space, so this balance does too.”: The Bianchi reason was about a box in space with three directions; the first what-if is whether it still works in spacetime, with time.
- “In the same way, the Einstein tensor is far larger inside the Sun than in the nearly empty space around it.”: A surprising claim with no reason.
- “Energy and momentum balance. For someone falling freely, the energy in a tiny box changes only by what flows in or out, and so does the momentum.”: A push changes momentum with nothing visibly flowing, so a teenager would object at once.
- “So any table of curving set equal to the matter table must balance too. A tempting first guess sets the Ricci tensor equal to the matter table.”: Two statements of one law: the glossary says 'a fixed number times the matter table', the way says 'equal to'.
- “Adding up the box rule shows how the Ricci tensor fails to balance. Its imbalance is exactly half of how fast its grand total changes across space and time.”: Reread: 'imbalance' is new, 'how fast it changes across space' is hard to picture, and the step is taken on trust without saying so.
- “So under the guess, the grand total could never change.”: The link is implicit: it follows because the Ricci tensor must balance everywhere.
- “For ordinary matter, such as rock or gas, the grand total would be set almost entirely by the mass in each cubic metre.”: Why the Ricci tensor's grand total has anything to do with mass is left unsaid.
- “adjusts the Ricci tensor by half its grand total. That adjustment cancels the imbalance, because the imbalance is exactly half of how the grand total changes.”: 'Adjusts' gives no direction, and why the adjustment cancels is left for the reader to work out. The glossary repeats 'adjusting'.
- “This balance is a rule for tiny boxes. Over large regions, matter can gain or lose energy by trading it with gravity.”: A surprising claim with no reason, and a second idea at the end of the way; a teenager hears 'energy is not conserved'. The common question repeats it.
- “The balance of the Einstein tensor comes from the box rule, added up the way the Ricci tensor adds up drifts. The box rule uses only how tiny changes add and how the edges of a box are shared.”: The check was not self-contained: no entry way of this note gave these reasons.
- “Start from that identity for the Levi-Civita connection”: Ladder: the working reader has the Levi-Civita connection only as a formal prerequisite.
- “$$\nabla_\mu G^{\mu\nu} = 0 ...$$ These are four equations, one for each $\nu$”: Ladder: nothing connects the entry picture of balance in a tiny box to zero divergence.

**Fixes**

- Compared the retelling with the entry takeaways: the hose picture and the failed guess came through, but the reason the balance holds everywhere, the free-fall box, the link from grand total to mass, and the direction of the fix did not.
- Added the entry way true-in-every-curved-spacetime (structure) for the second idea in a-table-of-curving-that-balances: why the balance holds in every smoothly curved spacetime. It has a grid try-it and prepares checks/invented-spacetime. A teaching-arc step and an if-stuck move point to it.
- Renamed learner-visible 'box rule' to 'Bianchi identity' everywhere, including the working way title and the derivation title, and updated the quoted titles in the working and formal ways. Ids are unchanged.
- Rewrote the summary, the recaps, the hose paragraphs, the try-it, the first-guess chain, the three entry checks' answers, two misconceptions, the common question, and the glossary entries for balance, Ricci tensor, Bianchi identity, Einstein tensor and contracted Bianchi identity.
- Added glossary entries: curvature table, leftover, smoothly curved, identity.
- Added a bridge in the working way from balance in a tiny box to zero divergence, in a freely falling frame at a point.
- Dropped to stay within the 10% review allowance on entry explanations: the bathtub paragraph of a-table-of-curving-that-balances (the definition of balance moved into the hose paragraph; the point that a balanced amount can change over time now lives in the balance glossary entry and problems/water-in-a-tub); the sentence 'Einstein's own attempts early that month were close to this guess' (history/einstein-1915 carries it); the general sentence about any table set equal to the matter table, folded into the first-guess paragraph; and the tea-cup example of energy balance. A comparison with a law of nature, and a Sun-centre pressure figure, were drafted and not kept for the same reason.

**Concerns**

- The prerequisite note bianchi-identity uses 'balance' for three leftovers adding up to nothing (its summary and its leftovers way). This note uses 'balance' for changing only by flow. A reader climbing from that note meets one word in two senses; that note should say 'cancel' or 'add up to nothing' instead.
- For the physics reviewer: the entry sentence that, for someone falling freely, gravity drops out of the count holds at a point (leading order in a tiny box). 'Add up the Bianchi identity in the same way that the Ricci tensor adds up entries of the curvature table' glosses over the second contraction's use of the metric. The common-question sentences about counts of different boxes not adding, and light losing energy as galaxies along its path measure it, need an accuracy check.
- Entry way explanations now sit at the cap plus most of the 10% allowance; the next learner-visible addition at entry must be paid for by a drop.
- The Einstein tensor note is still in the old format; when rewritten it should reuse 'balance', 'matter table' and 'grand total', and the Ricci scalar note's ring-test picture should be bridged to 'grand total' in its working rung.
- Owed after this reading: the physics stage has not covered revision 6. The five changed learner-visible strings are listed in review.novice.rereads for 2026-09-13; the two that need a physics eye are 'every face counterclockwise seen from outside' plus the shared-edge sentence in the recap of true-in-every-curved-spacetime, and 'Each galaxy along the light's path measures a longer wave, and less energy, than the galaxy before it.' in the common question.
- 'Count' still does three jobs in entry text: the tally in a tiny box ('gravity drops out of the count'), measuring ('the Ricci tensor counts the matter right where it is'), and reckoning ('counts as'). The third use is gone, but the first two remain and a future pass may want one word for each.
- Entry way explanations are at 1094 of the 1,000 cap plus the 10% review allowance, and other way fields at 846 of 800 plus allowance. Any further entry addition must be paid for by a drop.
- analogies is still empty and tutor_moves has one opening question and one common question. Both are legal, but a note whose only picture is the hose would be stronger with a second route in from a different setting.

**Re-read** (2026-09-13, revision 4): 3 stumbles in 10 changed passages

- “Add up entries of the Bianchi identity, much as the Ricci tensor adds up entries of the curvature table.”: The reader knows entries as the numbers in a table, but the Bianchi identity was met as a rule about leftovers. Adding up the entries of a rule does not make sense, and it breaks the link to the grid just above, where rules for rows are added up.
- “It comes from adding up entries of the Bianchi identity, much as the Ricci tensor adds up entries of the curvature table.”: Same stumble in the glossary: a rule has no entries.
- “Picture a tiny box carried by someone falling freely, without spinning.”: Step taken on trust: the next sentence explains why the box must fall freely, but nothing says why it must not spin, so a curious reader asks what spinning would spoil.
- Fix: Replaced 'entries of the Bianchi identity' with 'some of the many rules in the Bianchi identity' in the way 'true-in-every-curved-spacetime' and in the glossary entry for the contracted Bianchi identity. Claim unchanged: the contraction adds up components of the identity.
- Fix: Added the reason for 'without spinning' to the glossary entry for balance, not the way: entry explanations sit at 1098 words, near the 1100 review ceiling, and putting it in the way would have meant dropping the hose paragraph's contrast sentence.
- Fix: Read and found clear: 'space between the planets', 'ordinary matter' in the first-guess takeaway (defined in the explanation as rock or gas), 'without spinning' in both recaps, and the two reference titles.

**Re-read** (2026-09-13, revision 5): 0 stumbles in 1 changed passages


**Re-read** (2026-09-13, revision 6): 7 stumbles in 15 changed passages

- “It holds in every smoothly curved spacetime, whatever it contains, because it comes from the Bianchi identity.”: Two different 'it's in one sentence: the first and third mean the rule, the second means the spacetime. I had to read it twice to sort them out.
- “Carry an arrow around each of the six faces of a tiny box, and see how it comes back changed.”: A rule I could not follow: which way round each face? The answer matters, because walking a face the other way round reverses its change, and the next sentence's claim that opposite faces nearly cancel only holds when all six are walked the same way round. 'See how it comes back changed' also leaves 'it' hanging between the arrow and the box.
- “Its reason uses only how tiny changes add and how the edges of a box are shared, never what fills the space.”: 'How the edges of a box are shared' is never said anywhere an entry reader meets, here or in the recap, so I could repeat the phrase but not mean anything by it. The same phrase carries the answer to checks/invented-spacetime, which is supposed to be answerable from the entry ways alone.
- “In spacetime, a box can stretch along time as well as along space, and that reason still works.”: I cannot picture a box stretching along time, and 'stretch' is used elsewhere in the note for waves getting longer, so one word does two jobs.
- “Matter is described by a table too. At each place, it lists the energy and momentum of the matter, and how they flow.”: 'It' sits between two candidates, matter and the table, in the sentence right after both are named.
- “Momentum balances in the same way, once every push across the box's walls counts as momentum flowing in.”: Balance was defined as changing only by what flows in or out, so 'flowing in' alone left me asking what the push on the opposite wall does. 'Counts as' is also a third sense of 'count' beside 'gravity drops out of the count' and 'the Ricci tensor counts the matter'.
- “For example, as galaxies along its path measure it, light crossing the expanding universe loses energy as its waves stretch.”: Reread: the measurer clause comes before the thing measured, and 'its path', 'measure it' and 'its waves' are three pronouns for two different things. The tutor speaks this sentence aloud, where the reader cannot go back over it.
- Fix: Compared the second retelling with the three entry takeaways: all three came back, including that a balanced amount need not be the same everywhere and that the balance is an identity rather than a law. What did not come back was the walking sense of the six faces, the shared edges, and the box that stretches along time; those are the stumbles fixed here.
- Fix: Way a-table-of-curving-that-balances: split the two senses of 'it' in the contracted-Bianchi sentence.
- Fix: Way true-in-every-curved-spacetime: gave the six faces their walking sense and the shared edges in the recap, so 'how the edges of a box are shared' in the explanation and in checks/invented-spacetime now rests on something the entry reader has met; replaced 'a box can stretch along time' with 'a box covers a little time as well as a little space', which also frees 'stretch' for the waves.
- Fix: Way the-first-guess-would-forbid-stars: named the table in 'that table lists'; made a push 'itself momentum flowing in or out', matching the definition of balance on both directions.
- Fix: Common question does-it-prove-energy-conservation: 'does that equation force' in place of an ambiguous 'it', and the redshift example split into two spoken sentences with the measurer first.
- Fix: Dropped to pay for these additions and stay inside the review allowance on entry explanations (1094 of the 1,000 cap plus 10%): the sentence 'Where its grand total stays the same, the Ricci tensor balances.' in the-first-guess-would-forbid-stars, with the sentence before it changed to 'shows when the Ricci tensor fails to balance'. It stated the converse case, which the failure case already implies, and the argument of the way and of checks/first-guess-and-a-planet uses only the failure case.
- Fix: Read the working and formal ways as a stronger student: each opens by naming the way it continues ('The grand total in "The first guess would forbid stars"', 'The divergence-free Einstein tensor of "Two contractions of the Bianchi identity"', 'The two contractions in "Two contractions of the Bianchi identity"'), and the working way already bridges balance in a tiny box to zero divergence in a freely falling frame. No new bridge needed; no edits made above the entry rung.

**Re-read** (2026-09-13, revision 8): 2 stumbles in 2 changed passages

- “Each galaxy along the light's path is moving away from the galaxy before it, because the universe expands. So each galaxy measures a longer wave, and less energy, than the one before it.”: Two stumbles in the new pair of sentences, both in the second one. A galaxy does not measure anything, so the measurement has no measurer, and this answer is about whose counts can be added, which is exactly where the measurer matters. And 'the one before it' is a second name for the thing the sentence before calls 'the galaxy before it', so I had to check that the two meant the same; as written it also compares a wave with a galaxy rather than with what that galaxy's astronomer measured.
- “$\nabla_\mu T^{\mu\nu} = 0$ is a local balance: it does not make $T^{\mu\nu}$ constant, since $\rho$ falls as $a^{-4}$, and it gives a conserved total only with a symmetry such as a time-translation Killing vector, which this radiation-filled universe lacks.”: Squeezed into one 44-word sentence: a colon, a subordinate 'since' clause and an 'and' clause carry three separate statements, and the new scoping clause 'which this radiation-filled universe lacks' arrives at the end of the chain, where it is easy to attach to the wrong noun. I read it twice to see that 'it' is the local balance in both clauses, not $T^{\mu\nu}$.
- Fix: Entry, $.tutor_moves.common_questions[does-it-prove-energy-conservation].answer: 'So each galaxy measures a longer wave, and less energy, than the one before it.' became 'So an astronomer in each galaxy measures a longer wave, and less energy, than an astronomer in the galaxy before it measured.' Wording only: the same two measurements, compared the same way round, now with a measurer at each end and with 'the galaxy before it' named the same way as in the sentence before.
- Fix: Working, $.checks[radiation-in-a-growing-box].answer: the closing sentence was split into three, with 'therefore' and 'Nor ... by itself: that needs a symmetry as well' carrying the links the colon and the 'and' carried before. Claim unchanged: local balance, no constancy because $\rho \propto a^{-4}$, and a conserved total only with a symmetry such as a time-translation Killing vector, which this radiation-filled universe lacks.
- Fix: Read and left alone: 'because the universe expands' in the same entry answer. The sentence says what moves away from what, so the expansion has its comparison, and every shorter gloss I tried ('the distances between galaxies grow') either added a universal claim the physics stage has just had to scope, or pushed the picture towards galaxies flying apart through space.
- Fix: Nothing was dropped to pay for the two additions: the tutoring bucket rose by 8 words and the equations-and-checks bucket by 9.

## Review: physics

**Verdict:** fixed (2026-09-13, revision 8)

**Verification**

- Once-contracted identity: setting lambda = rho in the second Bianchi identity gives nabla_rho R^rho_{sigma mu nu} = nabla_mu R_{sigma nu} - nabla_nu R_{sigma mu}, with no metric.: Hand contraction with course Ricci R_{sigma nu} = R^rho_{sigma rho nu} and last-pair antisymmetry, term by term. → Correct; signs match the conventions Riemann and Ricci rows.
- Twice-contracted identity nabla_mu R^mu_nu = (1/2) nabla_nu R, using nabla g = 0 twice (pass g^{sigma mu} through nabla; first-pair antisymmetry gives g^{sigma mu}R_{alpha sigma mu nu} = -R_{alpha nu}).: Re-derived every step of derivations/contracting-twice by hand. → Correct, including the sign of the left side and the factor one half.
- Candidate R^{mu nu} + B R g^{mu nu} + Lambda g^{mu nu} has divergence (1/2 + B) nabla^nu R; checks/coefficient-of-the-half with A: (A/2 + B).: Hand algebra; example metric a proportional to t^{2/3} has R = 6(a''/a + H^2)/c^2. → Correct; python: a''/a = -2/(9t^2), H^2 = 4/(9t^2), R = 4/(3 c^2 t^2). Sphere and Schwarzschild have constant R, so cannot decide.
- First guess R_{mu nu} = kappa T_{mu nu} with conserved source forces nabla R = 0, so the trace T = R/kappa is constant; perfect-fluid trace T = -rho c^2 + 3p.: Hand algebra with the course perfect-fluid row: (rho + p/c^2)(-c^2) + 4p. → Correct. Inside the Sun p/(rho c^2) is about 1e-6 at the centre, so the trace is almost entirely -rho c^2, backing the entry claim that the matter table's grand total comes almost entirely from the energy in its mass (as a magnitude).
- Worked example flat-universe-balance: G_00 = 3H^2/c^2, G_ij = -(2a a'' + a'^2) delta_ij / c^2, Christoffels Gamma^0_ij = a a' delta_ij / c, Gamma^i_0j = (H/c) delta^i_j, and cancellation of the nu = 0 component.: Recomputed Christoffels from the metric with x^0 = ct; checked G_ij sign against the second expansion equation; did the nu = 0 and nu = i sums by hand. → Correct; 6H H' + 9H^3 - 3H(2H' + 3H^2) = 0 identically. Gamma^i_00 and Gamma^i_jk vanish, so the nu = i line is complete.
- Expansion equations H^2 = 8 pi G rho / 3 and 2a''/a + H^2 = -8 pi G p / c^2, and the derivation energy-budget-from-expansion.: Compared with the acceleration equation a''/a = -(4 pi G/3)(rho + 3p/c^2); re-did each substitution, including d(rho c^2 V)/dt = -p dV/dt. → Correct, with signs.
- Problem acceleration-equation-for-free: a''/a = -(4 pi G/3)(rho + 3p/c^2), failing at H = 0.: Worked the solution to the end. → Correct.
- Check radiation-in-a-growing-box: rho proportional to a^-4, box energy factor 0.5 when a doubles.: python: 2^-4 * 2^3 = 0.5; tolerance 0.01 sensible. → Correct.
- CMB scaling: 2.7255 K times (1 + 2) = 8.18 K.: python: 8.1765. → Correct to the quoted figures.
- Entry numbers: the Sun holds about 1,400 kg per cubic metre on average; space between the planets holds far less than a billionth of a gram per cubic metre; rock holds thousands of kilograms.: python: mean solar density 1.989e30 kg / (4/3 pi (6.957e8 m)^3) = 1410 kg/m^3; solar wind about 5 protons per cm^3 gives 8e-18 g per m^3. → Correct after the fix. The earlier 'space near Earth' failed: at low-orbit altitudes the air density is about 1e-12 kg per cubic metre, a billionth of a gram.
- Entry: in a tiny box carried by someone falling freely, gravity drops out of the count, so each amount changes only by flow.: In local inertial (normal) coordinates at a point, Gamma = 0 so nabla_mu G^{mu nu} = partial_mu G^{mu nu}; for a box of size L the Gamma G corrections are of order L times curvature, vanishing as the box shrinks. In a box held at rest on Earth, partial_mu T^{mu i} = -Gamma^i_00 T^00, the weight. → True for a tiny non-rotating freely falling box. A spinning freely falling box has Gamma^i_0j nonzero, so momentum-like entries change without flow; fixed by 'without spinning'.
- Entry: add up the Bianchi identity 'in the same way that the Ricci tensor adds up entries of the curvature table'.: Compared the index pairings: the first contraction pairs the upper index with the derivative index in one term and Ricci-like slots in the other two; the second contraction uses the metric, as the Ricci scalar does. → Not literally the same way. Rewritten as 'Add up entries of the Bianchi identity, much as the Ricci tensor adds up entries of the curvature table', which is true.
- Entry: the Einstein tensor balances in every smoothly curved spacetime, whatever it contains; the matter table balances wherever Einstein's equation holds.: Theorem holds for any C^3 metric with its Levi-Civita connection; Lambda g is divergence-free too. → Correct; 'smoothly curved' covers the C^3 hypothesis, and GR's connection is Levi-Civita.
- Common question: counts from different freely falling boxes cannot in general be added; light crossing the expanding universe loses energy as galaxies along its path measure it.: Photon energy measured by comoving observers scales as 1/a; covariant conservation gives integral totals only with a Killing field or asymptotic structure. → Correct as scoped ('in general', 'as galaxies measure it').
- Working bridge: in a freely falling frame at a point, partial_mu G^{mu nu} = 0, a density G^{0 nu} with fluxes G^{i nu}.: Normal coordinates at a point; with x^0 = ct this is partial_0 G^{0 nu} + partial_i G^{i nu} = 0. → Correct; 'at a point' stated.
- Formal: second Bianchi relation count (n = 3 equivalent to the contracted identity; n = 4 the contracted identity is 4 of 20).: python count: components of nabla Riem n*n^2(n^2-1)/12 minus independent ones n^2(n^2-1)(n+2)/24 gives 0, 3, 20 relations for n = 2, 3, 4. → Correct.
- Formal: Noether identity with E^{mu nu} = -G^{mu nu} for L = R; problem identity-from-relabelling.: delta(sqrt(-g) R) = sqrt(-g) G_{mu nu} delta g^{mu nu} and delta g^{mu nu} = -g^{mu a} g^{nu b} delta g_{ab}; integration by parts with compact support. → Correct.
- Formal checks: constraints-without-second-time-derivatives, dust-must-fall-freely; problem einstein-space-constant-factor.: Worked each: third x^0-derivatives cannot cancel; contraction with u_nu using u_nu nabla u^nu = 0; (1 - n/2) df = 0; for n = 2 f = K varies on an ellipsoid; Killing current divergence vanishes by symmetry of T and Killing antisymmetry. → Correct. Added 'with G = c = 1' in the constraints answer, which used 8 pi T without saying so.
- Notation trap: with (+,-,-,-) and the same Riemann convention, R and G^mu_nu flip sign while R_{mu nu}, G_{mu nu}, G^{mu nu} do not; Lambda term may appear as -Lambda g.: Tracked g to -g through Christoffels, Riemann, contractions and T^{mu nu} = rho u u. → Correct.
- History: Einstein 1915, 'Die Feldgleichungen der Gravitation', Sitzungsberichte Berlin 844-847, session of 25 November 1915; earlier November versions set a Ricci-type tensor proportional to T.: Wikisource bibliographic record (session date 25 November 1915, pages 844-847). → Verified. The 25 November paper wrote the trace-reversed form R = -kappa(T - g T/2), equivalent to subtracting half the trace; the entry description of the fix is an equivalent form.
- History: Noether 1918, 'Invariante Variationsprobleme', Nachr. Ges. Wiss. Göttingen, Math.-phys. Kl., 235-257.: Wikisource bibliographic record. → Verified.
- History: Voss 1880, Mathematische Annalen 16, 129-179.: Crossref record, DOI 10.1007/BF01446384; added as the work. → Bibliographic details verified. The attribution of a contracted identity to this paper is the standard historical account; the contribution is scoped as 'a contracted form'.
- Observation reference: Noterdaeme, Petitjean, Srianand, Ledoux, López 2011, A&A 526, L7; beta = -0.007 +/- 0.027.: Crossref record (DOI 10.1051/0004-6361/201016140) and arXiv abstract 1012.3164. → Verified; title punctuation corrected to the journal's colon; DOI and arXiv added.
- Research references: Fourès-Bruhat 1952 Acta Math. 88, 141-225; Gundlach, Calabrese, Hinder, Martín-García 2005 CQG 22, 3767-3773; Pretorius 2005 PRL 95, 121101; Lovelock 1971 JMP 12, 498-501; Lovelock 1972 JMP 13, 874-876; ADM 1962 in Witten (ed.), Wiley, 227-265; Szabados 2009 LRR 12, 4.: Crossref records by DOI and arXiv abstract pages. → All verified; DOIs added for Gundlach et al., Pretorius and both Lovelock papers. Pretorius's generalized-harmonic code with constraint damping ran plunge, merger and ringdown, supporting the horizon sentence.
- Revision 6 pass. Twice-contracted identity nabla_mu R^mu_nu = (1/2) nabla_nu R and nabla_mu G^{mu nu} = 0 in the course conventions (signature (-,+,+,+), Riemann R^rho_{sigma mu nu} = d_mu Gamma^rho_{nu sigma} - ..., Ricci R_{mu nu} = R^rho_{mu rho nu}).: Wrote an independent finite-difference curvature code in plain python3 (no sympy): Christoffels, Riemann, Ricci, R, G, and the covariant divergence. Ran it on a generic non-symmetric Lorentzian metric eta plus smooth trigonometric perturbations at a generic point. → div_mu R^mu_nu = (-0.00403, -0.00206, -0.00117, -0.00016) against half the gradient of R = (-0.00403, -0.00205, -0.00117, -0.00016); nabla_mu G^{mu nu} = O(1e-6) against |G^{mu nu}| ~ 0.024, i.e. zero to finite-difference precision. Sign and factor one half confirmed independently of the hand derivation.
- Revision 6 pass. Conventions sanity: a sphere of radius a has R = +2/a^2, and the flat model a proportional to t^(2/3) has R = 4/(3 c^2 t^2) (used in checks/coefficient-of-the-half).: Same code on ds^2 = -dt^2 + a^2(dtheta^2 + sin^2 theta dphi^2) + dz^2 with a = 2.5, and on flat FLRW with a = t^(2/3) at t = 0.8 and t = 1.7. → R = 0.320000 against 2/a^2 = 0.320000; R = 2.083333 and 0.461361 against 4/(3t^2) = 2.083333 and 0.461361. Both correct.
- Revision 6 pass. Worked example flat-universe-balance: G_00 = 3H^2/c^2, G_ij = -(2 a a'' + a'^2) delta_ij / c^2 with x^0 = ct, and nabla_mu G^{mu nu} = 0 for every a(t).: Same code with c = 1 on a cubic a(t) = 1 + 0.3t + 0.1t^2 - 0.05t^3 at t = 0.37, comparing components and the divergence; the c factors restored by hand from x^0 = ct (a' = adot/c, a'' = addot/c^2). → G_00 = 0.29765047 against 3H^2 = 0.29765047; G_11 = -0.32468156 against -(2 a addot + adot^2) = -0.32468151; R = 1.07117 against 6(addot/a + H^2); divergence 5e-7 against |G^00| = 0.30. Correct, including the 1/c^2 in both components.
- Novice rewrite (entry recap of true-in-every-curved-spacetime): 'Carry an arrow around each of the six faces of a tiny box, every face counterclockwise seen from outside. Each edge is shared by two faces, so every edge is walked once in each direction, and the six changes the arrow picks up add up to nothing.': Two checks. (1) Enumerated the twelve edges of a unit cube with all six faces oriented counterclockwise as seen from outside (outward normal by the right-hand rule) in python3. (2) Parallel-transported a vector numerically (RK4 along each coordinate edge, using the same generic curved metric) around all six faces of a cube of side eps from a home corner, with out-and-back trips along the connecting edges, and summed the six changes. → (1) 24 directed edges, each traversed exactly once, and every edge's reverse present: the shared-edge claim and the walking sense are exactly right, and they match the prerequisite's picture, which uses the same convention. (2) eps = 0.2, 0.1, 0.05 gave a sum of 1.35e-6, 9.2e-8, 6.0e-9 against a largest single face change of 9.5e-4, 2.4e-4, 6.1e-5: the sum falls as eps^4 while one face's change falls as eps^2, so for a tiny box the six changes add up to nothing, as stated. The leading eps^3 terms cancel by the Bianchi identity itself.
- Novice rewrite (entry, a-table-of-curving-that-balances): 'It comes from the Bianchi identity, so it holds in every smoothly curved spacetime, whatever that spacetime contains.' Claim unchanged by the split of the two senses of 'it'.: Compared with the formal hypotheses: any pseudo-Riemannian metric of class C^3 with its Levi-Civita connection, no condition on the matter content. → True and the same claim as the sentence it replaced.
- Novice rewrite (entry, the-first-guess-would-forbid-stars): 'Adding up the Bianchi identity shows when the Ricci tensor fails to balance. Where its grand total changes from place to place, or from moment to moment, the Ricci tensor fails to balance, by exactly half of that change.' The dropped sentence stated the converse.: nabla_mu R^mu_nu = (1/2) nabla_nu R: the imbalance in each direction is exactly half the change of R in that direction, and it is nonzero exactly where nabla R is nonzero, in space or in time. Checked that the way's argument and checks/first-guess-and-a-planet use only the failure direction. → Correct, with 'by exactly half' matching the factor one half. Dropping the converse ('Where its grand total stays the same, the Ricci tensor balances', which is also true) removes no step of the argument.
- Novice rewrite (entry): 'Momentum balances in the same way, once every push across the box's walls is itself momentum flowing in or out.': The stresses T^{ij} are the flux of the i-th momentum component across a wall with normal j; a push on one wall and the push on the opposite wall enter the count with opposite signs, so the two directions are both needed. → Correct, and more accurate than the previous 'counts as momentum flowing in', which named only one direction.
- Novice rewrite (entry): 'In spacetime, a box covers a little time as well as a little space, and that reason still works.': In four dimensions the Bianchi identity's box has faces spanned by two of the four coordinate directions, including time-space faces; the edge-sharing argument is unchanged. Checked that the explanation attributes the extension to the shared edges, not to the word counterclockwise, which belongs to the recap's box in space. → Correct. The recap's 'counterclockwise seen from outside' is stated for the box in space, and the explanation extends only the edge-sharing part, which needs no viewpoint.
- Novice rewrite (entry, common question): 'Each galaxy along the light's path measures a longer wave, and less energy, than the galaxy before it.': Wavelength measured by successive comoving observers along a null geodesic scales as the scale factor, so the statement is exactly true for galaxies carried apart by the expansion. Tried galaxies with peculiar motion: members of a cluster move at a few hundred kilometres per second, which is a fractional shift of about 0.001, while the expansion shift between galaxies a few megaparsecs apart is smaller than that. → Error of scope. For two nearby galaxies the peculiar motion can dominate, and a galaxy moving toward the source measures a shorter wave than the one before it. Fixed by giving the sentence its condition: the galaxies are moving away from one another because the universe expands.
- Check radiation-in-a-growing-box: 'it gives a conserved total only with a symmetry such as a time-translation Killing vector, which an expanding universe lacks.': Tried the standard expanding counterexamples: the Milne form of flat spacetime (a proportional to t), which is Minkowski spacetime in disguise and carries the full Poincare algebra including timelike translations, and de Sitter spacetime in flat slicing, whose static patch has a timelike Killing field. → Error. Some expanding universes do have a time-translation Killing field. The radiation-filled flat model of this check has none, so the claim was scoped to it: 'which this radiation-filled universe lacks'. The physics of the check is unchanged.
- Revision 6 pass. Every number in the note.: python3: mean solar density 1.98892e30 / ((4/3) pi (6.957e8)^3); interplanetary medium at 5 protons per cubic centimetre; tub 60 + (12 - 8) x 5; radiation box factor 2^-4 x 2^3; CMB 2.7255 x 3; solar-centre 3p/(rho c^2) with p = 2.4e16 Pa and rho = 1.5e5 kg per cubic metre; Riemann-derivative relation counts n n^2(n^2-1)/12 - n^2(n^2-1)(n+2)/24. → 1410 kg per cubic metre (note: about 1,400); 8.4e-18 g per cubic metre, far below a billionth of a gram; 80 litres; 0.5; 8.1765 K (note: 8.18 K); 3p/(rho c^2) = 5e-6, so the matter table's grand total is the mass energy to one part in 200,000; relations 0, 3, 20 for n = 2, 3, 4 (note: 4 of 20 in four dimensions). All correct.
- Revision 6 pass. Problems and formal checks reworked to their final answers.: acceleration-equation-for-free: differentiated H^2 = 8 pi G rho/3 with the budget, got Hdot = -4 pi G(rho + p/c^2), addot/a = -(4 pi G/3)(rho + 3p/c^2), and checked 2 addot/a + H^2 = -8 pi G p/c^2 term by term. einstein-space-constant-factor: R = nf, (1 - n/2) d_nu f = 0, and for the lambda source the divergence of -lambda g is -d_nu lambda. identity-from-relabelling: integration by parts with compact support, delta g^{mu nu} = -g^{mu a} g^{nu b} delta g_{ab}, E = -G for L = R. constraints-without-second-time-derivatives and dust-must-fall-freely worked in full. → All correct, with signs, and the stated failure cases (H = 0; n = 2) are the right ones.
- Revision 6 pass. Every reference.: Crossref records by DOI and the arXiv abstract page: 10.1051/0004-6361/201016140 (with arXiv 1012.3164 for the fitted beta), 10.1007/BF01446384, 10.1088/0264-9381/22/17/025, 10.1007/BF02392131, 10.1063/1.1665613, 10.1063/1.1666069, 10.1103/PhysRevLett.95.121101. → All confirmed: authors, year, title, venue, volume and pages match the note, and the abstract gives beta = -0.007 +/- 0.027. The two history items without DOIs (Einstein 1915, session of 25 November, pages 844-847; Noether 1918, pages 235-257) were confirmed in the earlier pass and are unchanged. Every reference keeps verified: true.

**Counterexamples tried**

- A freely falling but spinning box: momentum-like entries of the Einstein tensor change along the rotating axes without any flow, breaking 'each amount changes only by what flows in or out'. Fixed by 'without spinning' in the first entry way, the recaps, the first-guess way and the balance glossary.
- A box held at rest on Earth's surface: momentum changes by the weight term Gamma^i_00 T^00, which is not flow. Supports the entry claim that the box must fall freely.
- Low Earth orbit as 'space near Earth': air density there is about a billionth of a gram per cubic metre, breaking 'far less than a billionth of a gram'. Replaced by 'space between the planets'.
- Radiation, whose trace is zero, and a neutron-star core, where 3p can approach rho c^2: matter with near-constant trace could evade the first-guess argument. The entry scopes the argument to ordinary matter; the takeaway now says 'ordinary matter' too.
- Two dimensions: G vanishes identically and the Einstein-manifold factor need not be constant. The formal way and problem state n >= 3.
- A non-metric torsion-free connection: first-pair antisymmetry fails and Ricci need not be symmetric, so the second contraction fails. The formal way and simplifies say so.
- Constant-R metrics (sphere, Schwarzschild): they cannot fix the coefficient B. The check says so.
- An expanding universe: zero divergence while G_00 and rho change with time. Covered by the worked example and misconception divergence-free-means-constant.
- An isolated asymptotically flat system does have a conserved total (ADM); the common question says the local balance does not 'by itself' give a total, which remains true.
- Galaxies with their own motion: cluster members move at a few hundred kilometres per second, so the galaxy farther along a light path can measure a shorter wave than the one before it. Breaks the common question's per-galaxy claim, which is now conditioned on the galaxies moving away from one another because the universe expands.
- Milne coordinates (flat spacetime written as an expanding universe) and the static patch of de Sitter spacetime: expanding universes that do have a time-translation Killing field, and hence a conserved total energy. Breaks 'which an expanding universe lacks' in checks/radiation-in-a-growing-box, now scoped to this radiation-filled universe.
- A box with one face walked the other way round: that face's change reverses, so the six no longer add up to nothing. Removed by the recap's 'every face counterclockwise seen from outside'; an enumeration of the cube's twelve edges confirms every edge is then walked once in each direction.
- A box of finite size: the six face changes cancel only in the limit. Numerically the sum falls as the fourth power of the edge length while one face's change falls as the square, so the recap's 'tiny box' carries the claim, as in the prerequisite.

**Fixes**

- Entry, a-table-of-curving-that-balances, true-in-every-curved-spacetime and the-first-guess-would-forbid-stars, plus the balance glossary: freely falling box now 'without spinning'.
- Entry, true-in-every-curved-spacetime and the contracted-Bianchi glossary: 'in the same way that the Ricci tensor adds up' became 'Add up entries of the Bianchi identity, much as the Ricci tensor adds up entries of the curvature table', since the two contractions are not the Ricci contraction.
- Entry, the-first-guess-would-forbid-stars: 'space near Earth' became 'space between the planets'; takeaway scoped to 'ordinary matter'.
- Dropped to stay within the entry allowance: the sentence 'The guess cannot describe both.', whose point 'That rules out every star' already makes. Entry explanations now 1094 words.
- Formal: 'Zero divergence is 4 equations' became '$n$ equations', since the way is in n dimensions; constraints check answer now says 'with $G = c = 1$'.
- References: all confirmed and set verified; DOIs added (Noterdaeme et al., Gundlach et al., Pretorius, Lovelock 1971 and 1972), arXiv 1012.3164 added, the Noterdaeme title punctuation corrected, and Voss 1880 added as the work of history/voss-1880.
- Revision 6 pass, entry, tutor_moves common question does-it-prove-energy-conservation: 'Each galaxy along the light's path measures a longer wave, and less energy, than the galaxy before it.' became 'Each galaxy along the light's path is moving away from the galaxy before it, because the universe expands. So each galaxy measures a longer wave, and less energy, than the one before it.' The sentence needed its condition, since galaxies with their own motion can break the order, and the split also gives the reason before the result.
- Revision 6 pass, working, checks/radiation-in-a-growing-box: 'which an expanding universe lacks' became 'which this radiation-filled universe lacks'. Milne and de Sitter are expanding universes with a time-translation Killing field.
- No other learner-visible text changed. The novice reviewer's five rewrites at revision 6 were re-derived and stand: the six-face walking sense and shared edges, the split of the two senses of 'it', 'a box covers a little time as well as a little space', the push as momentum flowing in or out, and 'shows when the Ricci tensor fails to balance' with its dropped converse.

**Concerns**

- Other way fields are at 819 of 800 words (within the 10% allowance); the added 'without spinning' in the two recaps cost 4 words.
- Entry explanations are at 1094 of 1,000 plus allowance; any further entry addition needs a matching drop.
- The 25 November 1915 paper wrote the trace-reversed form; the entry way's 'taking away half its grand total' is the equivalent modern form. If the history item is expanded, say so.
- Registry still needs syncing for ricci-scalar, levi-civita-connection and diffeomorphism-invariance; both proposed visuals await catalog entries; the counting-box visual should show a non-spinning box.
- The prerequisite note bianchi-identity uses 'balance' in a different sense (noted by the novice reviewer); not edited here.
- The symbol kappa for the first-guess coupling is local to the working way; the conventions file uses kappa for surface gravity. No clash within this note.
- Revision 6 pass: the recap of true-in-every-curved-spacetime gives the walking sense for a box in space ('counterclockwise seen from outside'), while the explanation extends the reason to a box that covers a little time. Only the edge-sharing half of the reason is extended, which needs no viewpoint, so the text is accurate; a reader who asks how to walk a face that covers time is asking a working-rung question.
- Revision 6 pass: the common question now runs three sentences on the redshift example, and the tutoring bucket sits at about 3,040 of 3,300 words. Entry way explanations were not touched, so they stay at 1,094.
- Revision 6 pass: review.novice covers revision 6, the note is at revision 7. The two changed strings (one entry, one working) need a novice re-read; that warning is expected and only that stage can clear it.
- Standing and not fixed here: the registry prerequisites still differ for ricci-scalar, levi-civita-connection and diffeomorphism-invariance; both visuals are still proposals; and the prerequisite note bianchi-identity uses 'balance' for three leftovers adding up to nothing, a second sense of this note's word.

**Diff check** (2026-09-13, revision 5)

- Way true-in-every-curved-spacetime and the contracted-Bianchi glossary: 'Add up some of the many rules in the Bianchi identity, much as the Ricci tensor adds up entries of the curvature table.' It must claim what 'adding up entries of the Bianchi identity' claimed.: Compared with the working derivation: nabla_[lambda R^rho_sigma|mu nu] = 0 is a set of component equations, one per index choice. Contracting lambda = rho, then sigma with mu through the metric, sums a subset of them, weighted by metric entries, just as R_{sigma nu} = R^rho_{sigma rho nu} sums a subset of Riemann components. Checked against the prerequisite's entry picture: one rule of three leftovers per box tilt set and arrow, so spacetime gives many rules. Checked against the grid paragraph: rules for rows are added. → True, and the same claim as before. 'Some' is right, since only contracted components enter. 'Adding up' leaves out the metric weights, as the Ricci clause already does at entry.
- Balance glossary: 'Falling freely takes gravity out of the count.': In a freely falling frame, the connection coefficients Gamma^i_tt vanish at the box's centre (no acceleration). So the extra terms in nabla_a T^ab relative to the plain flow count d_a T^ab lose the gravity term Gamma^i_tt T^tt there. Compared with the way a-table-of-curving-that-balances ('only then does gravity drop out of the count'). → True at the box's centre, and consistent with the way. Tidal effects vanish as the box shrinks.
- Balance glossary (reread wording): 'Not spinning keeps out the outward push that riders on a spinning roundabout feel.': Computed in python3 the Christoffel symbols of a rotating frame in flat spacetime (c = 1, omega = 0.7): ds^2 = -(1 - omega^2(x^2+y^2))dt^2 + 2 omega(x dy - y dx)dt + dx^2+dy^2+dz^2. At the centre only Gamma^x_ty = -0.7 and Gamma^y_tx = +0.7 are nonzero: the sideways (Coriolis) terms. The outward (centrifugal) term Gamma^x_tt = -omega^2 x is zero there (-0.0049 at x = 0.01). No Gamma^t term is nonzero at the centre, so the energy count is untouched, and the momentum count gains omega times the momentum flow T^ty. → Error. At the centre of the carried box the outward push is zero. What spinning adds to the count is the sideways push on moving matter. Naming only the outward push gives the wrong reason.
- Fixed wording: 'Not spinning keeps out the pushes felt on a spinning roundabout, such as the sideways push on anyone walking across it.': Same computation. A rotating frame brings both apparent pushes. The sideways one acts on anything moving relative to the roundabout, perpendicular to its motion, and it is the term that survives at the box's centre. Checked with the entry recaps and ways, which say only 'without spinning' and give no other reason. → True. It names the push that actually spoils the momentum count, and it is consistent with the rest of the note.
- Fix: Balance glossary: 'Not spinning keeps out the outward push that riders on a spinning roundabout feel.' became 'Not spinning keeps out the pushes felt on a spinning roundabout, such as the sideways push on anyone walking across it.' The outward push is zero at the carried box's centre. The sideways (Coriolis) push is what spinning adds to the momentum count.
- Fix: No change to the two 'some of the many rules' rewordings or to 'Falling freely takes gravity out of the count.': all verified true.

**Diff check** (2026-09-13, revision 8)

- Scope of this check. note_diff between the pre-re-read snapshot (revision 7) and the note lists exactly two changed learner-visible strings: entry $.tutor_moves.common_questions[does-it-prove-energy-conservation].answer, and working $.checks[radiation-in-a-growing-box].answer. Both were read inside their whole field.: python3 knowledge/_tools/note_diff.py on the before-re-read snapshot against the note; then read each containing field in full and compared it with the note's misconceptions local-balance-means-conserved-total and divergence-free-means-constant, with the working way's cosmology paragraph, and with course-conventions.md (perfect fluid, FLRW metric, redshift rows). → Two strings, one entry and one working. No other learner-visible text moved.
- Entry, common question: 'So an astronomer in each galaxy measures a longer wave, and less energy, than an astronomer in the galaxy before it measured.' It must claim exactly what 'So each galaxy measures a longer wave, and less energy, than the one before it.' claimed.: Both sentences compare two measurements of the same light made at two neighbouring galaxies along its path, in the direction of travel, under the condition the sentence before states: each galaxy is moving away from the galaxy before it because the universe expands. Checked the direction of the comparison (the later astronomer is the one who finds the longer wave), the sense of the shift (recession gives redshift, 1 + z = lambda_r/lambda_e > 1, the conventions redshift row), and the energy step (a longer wave carries less energy per photon). Checked that naming the measurer adds no new claim: comoving galaxies carry the astronomers who make these measurements, and the chain of neighbour-to-neighbour Doppler shifts is exactly the cosmological redshift. → True, and the same claim as the old sentence, with the same scope. The measurer is now named at both ends and the comparison is measurement against measurement rather than wave against galaxy. Nothing about whose counts may be added was weakened or strengthened.
- Working check answer, new sentence: 'nabla_mu T^{mu nu} = 0 is a local balance. It therefore does not make T^{mu nu} constant, since rho falls as a^{-4}.': Read as 'a local balance does not force T^{mu nu} to be constant', which is what the old single sentence said, and confirmed both readings of the 'since' clause are true here. Recomputed the components in comoving coordinates for the perfect fluid of the conventions row with p = rho c^2/3: T^{00} = (rho + p/c^2)c^2 + p g^{00} = (4/3)rho c^2 - rho c^2/3 = rho c^2, which goes as a^{-4}; T^{ij} = p g^{ij} = (rho c^2/3)a^{-2}delta^{ij}, which goes as a^{-6}. Also checked covariant constancy directly: nabla_0 T^{00} = d(rho c^2)/dt = -4H rho c^2 is nonzero, so T^{mu nu} is not covariantly constant either, which is the belief the misconception divergence-free-means-constant states. → True on both readings, and unchanged in claim. The split into two sentences keeps 'it' pointing at the local balance in each, as the single sentence did.
- Working check answer, new sentence: 'Nor does it give a conserved total by itself: that needs a symmetry as well, such as a time-translation Killing vector, which this radiation-filled universe lacks.' It must preserve the old 'only with a symmetry' scope.: Checked the mechanism: for a Killing vector xi, J^mu = T^{mu nu}xi_nu has nabla_mu J^mu = T^{mu nu}nabla_mu xi_nu = 0, because T is symmetric and nabla_(mu xi_nu) = 0, so Gauss's theorem gives a conserved charge; without such a symmetry nabla_mu T^{mu nu} = 0 alone integrates to no charge. Checked the 'lacks' clause for flat radiation FLRW, a = t^{1/2}: computed in python3 R_tt = -3 addot/a = (3/4)t^{-2}, R_ij = (a addot + 2 adot^2)delta_ij = (1/4)t^{-1}delta_ij, R = 0 (as the vanishing trace of radiation stress-energy requires), and R_{mu nu}R^{mu nu} = (3/4)t^{-4}. That invariant varies from slice to slice, and its level sets are the comoving t = const slices, so no isometry can move a point off its slice and the spacetime has no timelike Killing vector at all, in particular no time-translation one. Also checked d/dt g_ij = 2 a adot delta_ij is nonzero, so the obvious candidate d/dt is not Killing. → True, and the same scope: 'not by itself; that needs a symmetry as well' is the old 'only with a symmetry'. It matches the correction of misconception local-balance-means-conserved-total word for word in scope.
- The whole changed check still works to its final answer, with the right numeric field.: Integrated rhodot = -3H(rho + p/c^2) with p = rho c^2/3 in python3 along a = t^{1/2} from t = 1 to t = 4 (a = 1 to a = 2): rho a^4 stayed at 1.000000 and rho fell to 0.06250, so rho goes as a^{-4}. Comoving volume V goes as a^3, so rho c^2 V goes as a^{-1} and the energy factor came out 0.499999 when a doubles, matching the numeric field value 0.5, unit 1, sign magnitude, abs_tol 0.01. Checked the budget identity: d(rho c^2 V)/dt = c^2 V(rhodot + 3H rho) = -3H p V = -p dV/dt. → All correct. The numeric answer, its tolerance and the three key_points still match the answer text after the split.
- Counterexamples tried against the two changed sentences.: Entry sentence: cluster galaxies with peculiar motions of a few hundred kilometres per second (a galaxy farther along the path can approach the source and measure a shorter wave); a contracting or static universe. Working sentences: a static uniform fluid in flat spacetime (divergence-free and constant); dust, p = 0, rho going as a^{-3}, where the mass in a comoving box is fixed; Schwarzschild, which has a timelike Killing vector; an asymptotically flat spacetime, where the ADM energy is conserved without an exact timelike Killing vector. → None breaks a changed sentence. The entry sentence begins with 'So' and inherits the condition stated in the sentence before it, that each galaxy is moving away from the galaxy before it because the universe expands, which excludes the peculiar-motion and non-expanding cases. The static fluid does not break 'does not make T^{mu nu} constant', which denies forcing, not compatibility; dust is the same local law with a different power. Schwarzschild is the 'with a symmetry' branch the sentence names. The ADM case rests on the asymptotic time-translation symmetry at spatial infinity, so it sits inside 'that needs a symmetry as well', which names the Killing vector as an example and not as the only symmetry.
- Fix: No change. Both re-read rewordings claim exactly what the physics-reviewed sentences claimed, and both are true at their rung: the entry sentence keeps the recession condition it inherits and now names a measurer at each end; the working split keeps the 'only with a symmetry' scope as 'not by itself: that needs a symmetry as well'.
- Fix: Nothing dropped or shortened: the note stands at 8,500 of 9,500 words, tutoring at 3,054 of 3,300, with no part near its cap, so the review allowance was not needed.
