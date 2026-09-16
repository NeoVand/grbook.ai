---
type: "concept"
schema_version: 2
id: "einstein-tensor"
title: "Einstein tensor"
tagline: "The table of curving that adds up the rings around you, not the tides"
domain: "curvature"
tier: "core"
status: "physics-reviewed"
revision: 4
updated: "2026-09-16"
aliases: ["G_ab", "trace-reversed Ricci tensor", "Einstein tensor from sectional curvatures"]
prerequisites: ["ricci-tensor", "ricci-scalar", "contracted-bianchi-identity", "sectional-curvature"]
leads_to: ["einstein-field-equations", "trace-reversed-einstein-equations", "constraint-equations", "lovelock-theorem"]
visuals: ["six-entry-curvature-table", "three-rings-around-a-spot", "falling-ring-of-crumbs", "rings-in-an-expanding-grid"]
---

# Einstein tensor

*The table of curving that adds up the rings around you, not the tides*

`einstein-tensor` · curvature · core · physics-reviewed (revision 4)

**Needs:** [[ricci-tensor]] (entry) · [[ricci-scalar]] (entry) · [[contracted-bianchi-identity]] (working) · [[sectional-curvature]] (working)  
**Opens:** [[einstein-field-equations]] · [[trace-reversed-einstein-equations]] · [[constraint-equations]] · [[lovelock-theorem]]  
**Related:** [[weyl-tensor]] · [[sectional-curvature]] · [[einstein-hilbert-action]] · [[hamiltonian-constraint]] · [[stress-energy-tensor]]  
**Visuals:** ★ [[six-entry-curvature-table]] · [[three-rings-around-a-spot]] · [[falling-ring-of-crumbs]] · [[rings-in-an-expanding-grid]]

> At any spot, the curving of spacetime has six parts. Three are tides, read with crumbs let go. Three are rings, drawn on the floor and two walls. The Ricci table's reading for someone at rest adds up the three tides. Where nothing changes with time, the Einstein table's reading adds up the three rings instead. Einstein's law of gravity sets that reading by the matter right there.

## You will be able to

**Entry**
- Explain which three of the six parts each table's reading adds, and use it above a planet. `objectives/say-which-planes-each-table-counts` ← `checks/rings-not-tides`, `problems/ring-and-crumb-survey`
- Build the Einstein table's diagonal from a Ricci diagonal with the half-the-grand-total rule. `objectives/build-from-the-ricci-table` ← `checks/build-the-water-table`

**Working**
- Compute the Einstein tensor from the Ricci tensor and scalar or from orthonormal plane curvatures, take its trace, and invert the trace reversal. `objectives/compute-from-ricci-or-planes` ← `problems/constant-curvature-einstein`
- Use an observer's own Einstein component as an energy-density gauge, and distinguish a vanishing Einstein tensor from flat spacetime and rings in space from planes in spacetime. `objectives/read-the-density-gauge` ← `checks/zero-einstein-not-flat`, `checks/flat-universe-not-zero`

**Formal**
- Prove the trace formula in n dimensions, the vanishing of the Einstein tensor in two dimensions, and the equivalence of G = 0 and Ric = 0 for n at least three. `objectives/prove-dimension-facts` ← `checks/two-dimensions-vanish`, `problems/dimension-facts`
- State the hypotheses of the divergence identity and the observer plane sum, and explain why conservation alone does not fix the field equation. `objectives/state-hypotheses-and-limits` ← `checks/conservation-does-not-fix-the-equation`

## Ways in

### 1. Three tides and three rings · entry · picture

*What does the Einstein table's reading for someone at rest add up, and how is that different from the Ricci table's?*

**Recap:** Two tests read the curving at a spot. In the crumb test, a small ball of crumbs is let go, and the crumbs drift apart or together relative to each other. Those drifts are the tides. In the ring test, a ring is drawn by measuring the same short distance out from a centre in every direction with a tight string. Its length is then compared with the length it would have where nothing is curved.

Float at rest above an airless planet that does not spin, held up by a small rocket, inside a box-shaped cabin. Nothing around you moves or changes. At your spot, the curving of spacetime has six parts, and you can read all six. Why six? Spacetime has four directions: time, up-down, left-right and front-back. Each pair of directions gives one part, and four directions make six pairs.

Three of the parts pair time with one space direction, and those are the tides. Let go of a small ball of crumbs beside you. The whole ball drops away toward the planet, because nothing holds it up. Ignore that fall and watch only how the crumbs drift relative to each other, just after you let go. The crumbs that lie on the up-down line through the ball's middle drift apart. The crumbs that lie across that line, left-right or front-back, drift together. So the tides come as three drifts: one along the up-down line, two across it.

The other three parts pair two space directions, and those are the rings. Draw a small ring on the cabin floor, one on the wall to your left, and one on the wall in front of you. The floor ring lies level, and the two wall rings stand upright. Each ring pairs the two directions that run along its floor or wall. Compare each ring with its playground length, the length it would have where nothing is curved. The ring on the floor comes out short. Each ring on a wall comes out too long, by half as much as the floor ring is short. The string, not a guess, decides which ring is the short one. What the ring test already told you, above a planet, is that the three add up to zero: the two long rings exactly undo the short one.

Each table of curving gives one number to each person at a spot. That number is the table's reading for that person.

The Ricci table is the table of the Ricci tensor note, and its reading for you adds up the three tides. The Einstein table is a second table built from the same six parts, and its reading for you adds up the three rings instead. The two tables differ only in which three parts each one adds.

Try the numbers above the planet. Call the floor ring's shortfall two units. Each wall ring is then too long by one unit, and too long counts as minus one. So the ring total is two minus one minus one, which is zero. The tides come in the same sizes: apart along the up-down line by two units, together across it by one unit each way, and together counts as minus one. So the tides total two minus one minus one, which is zero too, as the Ricci tensor note found. Both readings are zero above the planet, though the tides are strong.

Why keep a second table at all? Because the Einstein table has a property the Ricci table lacks, called balance, which Einstein's law needs. The contracted Bianchi identity note explains it.

Daily life hides the rings. Near Earth's surface, draw a ring one kilometre out from its centre, holding the string level and straight, because the ground itself curves. It falls short of its playground length by less than a thousandth of the width of one atom. Two rings of the same size drawn upright, like the wall rings, are each too long by half of that.

**Takeaway:** At any spot the curving has six parts: three tides and three rings. The Ricci table's reading for someone at rest adds up the three tides; where nothing changes with time, the Einstein table's reading adds up the three rings.

*What this leaves out:* The rings read the Einstein table only where nothing moves or changes with time, as above this planet. Where space itself is stretching, as in the expanding universe, rings drawn in space miss part of the reading; the working level shows what they miss.

*Builds on:* [[ricci-tensor]], [[ricci-scalar]]<br>*Visuals:* [[six-entry-curvature-table]]<br>*See:* `checks/rings-not-tides`, `problems/ring-and-crumb-survey`

### 2. Half the grand total off · entry · calculation

*How is the Einstein table built from the Ricci table, entry by entry?*

**Recap:** The Ricci table has four entries down its diagonal: one for time and three for space. Its grand total adds the three space entries and takes away the time entry.

In "Three tides and three rings", both readings above the planet came out zero. To see the Einstein table built from the Ricci table, take a place where the readings are not zero. Go deep inside a huge ball of still water, far from any planet or star.

The Ricci table has a row and a column for each of the four directions of spacetime: time, up-down, left-right and front-back. The four entries where a direction meets itself run down the table's diagonal: one time entry and three space entries. Inside still water, Einstein's law makes all four the same size. Take that on trust here; it holds where the water is at rest and its pressure is too small to count. Call that size one unit. So the Ricci diagonal reads one, one, one, one.

First find the grand total. It adds the three space entries and takes away the time entry, because time counts the opposite way from space in every such sum. That opposite sign is a rule of spacetime, taken on trust here. So the grand total is three minus one, which is two units. This grand total is the Ricci scalar of spacetime, and it takes in the time entry. It is not the ring total of the Ricci scalar note, which uses rings drawn in space only; inside still water the two happen to agree, but they need not.

Now the building rule. Take half the grand total off each space entry, and add that same half to the time entry. Half of two is one. Each space entry becomes one minus one, which is zero. The time entry becomes one plus one, which is two. So the Einstein diagonal reads two, zero, zero, zero.

The time entry gets the half added, not taken off. The reason is the same one that takes time away in the grand total: time and space enter every such sum with opposite signs.

Read the result. The time entry is the Einstein reading for someone at rest in the water, and it is two units. Einstein's law sets that reading by the water right there: twice as much water in each cubic metre would give twice the reading. The rings must agree, because the Einstein reading adds up the three rings. Inside this ball of still water all three rings come out short, and their shortfalls total two units. The space entries are zero. Einstein's law sets those by pressure, and still water's own pressure is far too small to count here.

Above the planet there is no matter at your spot, and Einstein's law then makes every Ricci entry zero, not only the tides total. So the rule gives all zeros again, matching the zero ring total. The Einstein table adds nothing new to the six parts. It is the Ricci table re-sorted, so that its reading adds up the rings.

**Try it:** Do the rule on paper for a Ricci diagonal of three, one, one, one, time first. The grand total is one plus one plus one minus three, which is zero. Half of zero is zero, so nothing changes: the Einstein diagonal is also three, one, one, one. The rule can leave a table alone.

**Takeaway:** Take half the Ricci table's grand total off each space entry and add it to the time entry. For still water that leaves only the time entry, two units, set by the water right there.

*What this leaves out:* The rule as stated covers the four diagonal entries. The tables also have entries that pair two different directions, and those are copied from the Ricci table unchanged.

*Continues:* `ways_in/three-tides-and-three-rings`<br>*Builds on:* [[ricci-tensor]], [[ricci-scalar]]<br>*Visuals:* [[six-entry-curvature-table]]<br>*See:* `checks/build-the-water-table`

### 3. Trace reversal and plane sums · working · calculation

*What is the Einstein tensor as a formula, and which Riemann components does each of its diagonal entries add up?*

The building rule of "Half the grand total off" is one formula,

$$G_{\mu\nu} = R_{\mu\nu} - \tfrac12 R\,g_{\mu\nu},$$

with $R_{\mu\nu} = R^\rho{}_{\mu\rho\nu}$ the Ricci tensor and $R = g^{\mu\nu}R_{\mu\nu}$ its trace, the grand total. $G_{\mu\nu}$ is symmetric because both terms are, so it has ten independent components in four dimensions, with units of inverse length squared. The metric supplies the signs: in an orthonormal frame $g_{\hat0\hat0} = -1$ and $g_{\hat\imath\hat\imath} = +1$, so $G_{\hat0\hat0} = R_{\hat0\hat0} + \tfrac12 R$ while $G_{\hat\imath\hat\imath} = R_{\hat\imath\hat\imath} - \tfrac12 R$, and off-diagonal components are copied unchanged.

Trace both sides with $g^{\mu\nu}$, using $g^{\mu\nu}g_{\mu\nu} = 4$: the trace $G \equiv g^{\mu\nu}G_{\mu\nu}$ is $R - 2R = -R$. The map flips the sign of the trace and leaves the trace-free part alone, which is why it is called trace reversal. Applied twice it gives the identity, so $R_{\mu\nu} = G_{\mu\nu} - \tfrac12 G\,g_{\mu\nu}$: the Einstein tensor carries exactly the information of the Ricci tensor, no more and no less.

Now the plane sums. In an orthonormal frame at a point, the six components $R_{\hat a\hat b\hat a\hat b}$ with $a < b$ are the six parts of the entry picture. Each space-space one is the sectional curvature $K$ of that plane, positive where rings come out short. Each time-space one is minus the sectional curvature of its plane, $R_{\hat0\hat\imath\hat0\hat\imath} = -K(e_0, e_i)$, and $K(e_0,e_i)$ is positive where free neighbours along $e_i$ accelerate apart. In mixed form the Ricci diagonal $R^{\hat a}{}_{\hat a}$ adds the curvatures of the three planes that contain $e_a$; summing over $a$ counts each plane twice, so $R = 2\sum_{\text{planes}} K$. Then, with no sum on $a$,

$$G^{\hat a}{}_{\hat a} = R^{\hat a}{}_{\hat a} - \tfrac12 R = \sum_{\text{planes}\ni a} K - \sum_{\text{all planes}} K = -\sum_{\text{planes}\not\ni a} K.$$

Trace reversal is the switch from the three planes containing a direction to the three that leave it out. For the time direction $G_{\hat0\hat0} = -G^{\hat0}{}_{\hat0}$, so

$$G_{\hat0\hat0} = K(e_1,e_2) + K(e_2,e_3) + K(e_3,e_1) = R_{\hat1\hat2\hat1\hat2} + R_{\hat2\hat3\hat2\hat3} + R_{\hat3\hat1\hat3\hat1},$$

the ring total of the entry picture. The derivation "Plane sums from the definition" does the bookkeeping.

Check it on the static frame outside a spherical mass $M$, with $m = GM/c^2$. In units of $m/r^3$ the six components are $R_{\hat t\hat r\hat t\hat r} = -2$, $R_{\hat t\hat\theta\hat t\hat\theta} = R_{\hat t\hat\phi\hat t\hat\phi} = +1$, $R_{\hat r\hat\theta\hat r\hat\theta} = R_{\hat r\hat\phi\hat r\hat\phi} = -1$ and $R_{\hat\theta\hat\phi\hat\theta\hat\phi} = +2$. The three space planes give $G_{\hat t\hat t} = -1 - 1 + 2 = 0$. The planes leaving out $r$ give $G_{\hat r\hat r} = R_{\hat t\hat\theta\hat t\hat\theta} + R_{\hat t\hat\phi\hat t\hat\phi} - R_{\hat\theta\hat\phi\hat\theta\hat\phi} = 1 + 1 - 2 = 0$, and the angular entries vanish the same way. Outside matter the Einstein tensor is zero while every one of the six parts is not.

One more fact, proved in the contracted Bianchi identity: $\nabla_\mu G^{\mu\nu} = 0$ for every metric. The Ricci tensor has no such property, and this is what fits $G_{\mu\nu}$ to face a conserved stress-energy tensor.

**Takeaway:** The Einstein tensor is the Ricci tensor minus half its trace times the metric; each diagonal entry, in mixed form, is minus the sum of the sectional curvatures of the three planes that leave that direction out.

*Continues:* `ways_in/half-the-grand-total-off`<br>*Builds on:* [[sectional-curvature]], [[contracted-bianchi-identity]]<br>*Visuals:* [[six-entry-curvature-table]]<br>*See:* `derivations/plane-sums-from-the-definition`, `derivations/trace-reversal-inverts-itself`, `checks/zero-einstein-not-flat`

### 4. What an observer's own component reads · working · operational

*What does an observer's own Einstein component measure, and how does an expanding universe expose the difference between rings in space and planes in spacetime?*

The plane sum $G_{\hat0\hat0}$ of "Trace reversal and plane sums" is the component an observer with four-velocity $u$ reads for their own time direction, $G_{\hat0\hat0} = G_{\mu\nu}u^\mu u^\nu/c^2$. Einstein's equation, stated here and derived in its own note, fixes it:

$$G_{\hat0\hat0} = \frac{8\pi G}{c^2}\,\rho + \Lambda,$$

where $\rho c^2 = T_{\mu\nu}u^\mu u^\nu/c^2$ is the energy density that observer measures, the $c^2$ undoing the two factors of $u^{\hat0} = c$ in the observer's own frame, and $\Lambda$ is the cosmological constant. So the sum of the curvatures of an observer's three space planes is a density gauge: it reads the energy density right there, whoever the observer is, with no pressure term. The Ricci component differs, $R_{\hat0\hat0} = 4\pi G(\rho + 3p/c^2)/c^2 - \Lambda$: pressure counts three times in the tides and not at all in the rings.

Where nothing changes with time, three rings drawn in space read the gauge directly. A static observer's slice of space is not bending in spacetime, so a ring of radius $s$ in a plane of curvature $K$ comes out short by the fraction $Ks^2/6$, and the three shortfalls add to $G_{\hat0\hat0}s^2/6$. That is the ring total of the Ricci scalar note.

An expanding universe shows what rings can miss. Comoving observers in a universe with scale factor $a(t)$ and curvature index $k$ have

$$G_{\hat t\hat t} = \frac{3}{c^2}\Big(\frac{\dot a}{a}\Big)^2 + \frac{3k}{a^2},$$

assembled in "The expanding universe from six plane curvatures". Rings drawn in the space of a $k = 0$ universe come out at their playground length, yet $G_{\hat t\hat t} = 3H^2/c^2$ with $H = \dot a/a$. The reason is that every comoving pair is moving apart: the slice of space is bending in spacetime, and each space-space plane of spacetime carries curvature $(\dot a/a)^2/c^2$ that the slice's own geometry does not show. So the Hubble constant measures our own Einstein component. With $H_0 = 67.4$ km/s/Mpc it is $3H_0^2/c^2 = 1.6\times10^{-52}\ \mathrm{m^{-2}}$, and the density the gauge demands, $3H_0^2/8\pi G = 8.5\times10^{-27}$ kg per cubic metre, is the critical density: about five hydrogen atoms per cubic metre.

**Takeaway:** An observer's own Einstein component is a density gauge: eight pi G over c squared times the energy density they measure, plus the cosmological constant, with no pressure term; rings in space read it only where space is not bending in time.

*What this leaves out:* The value of the coupling constant and the role of the cosmological constant belong to the field-equation note; here the equation is used, not derived.

*Continues:* `ways_in/trace-reversal-and-plane-sums`<br>*Builds on:* [[ricci-scalar]], [[sectional-curvature]]<br>*Visuals:* [[rings-in-an-expanding-grid]]<br>*See:* `worked_examples/expanding-universe-from-planes`, `checks/flat-universe-not-zero`, `observations/critical-density-from-hubble`

### 5. The object in n dimensions · formal · structure

*What are the Einstein tensor's defining properties on a manifold of any dimension, what does it determine, and what fixes its role in the field equations?*

The density gauge of "What an observer's own component reads" is one face of a general object. Let $(M,g)$ be a pseudo-Riemannian manifold of dimension $n$ with its Levi-Civita connection, and set $G = c = 1$ in this way. The Einstein tensor is the symmetric $(0,2)$ field $G = \mathrm{Ric} - \tfrac12 R\,g$. Four facts fix what it is.

*Divergence.* $\nabla^\mu G_{\mu\nu} = 0$ for every metric, by the twice-contracted Bianchi identity; the hypotheses are a torsion-free, metric-compatible connection. The identity is the Noether identity of diffeomorphism invariance of $\int R\sqrt{|g|}$, so it holds off-shell. For $G_{\mu\nu} = 8\pi T_{\mu\nu}$ in $n = 4$: of ten component equations, four are tied by identities, leaving six to determine a metric whose ten components carry four coordinate freedoms.

*Trace.* Since $g^{\mu\nu}g_{\mu\nu} = n$, $\operatorname{tr} G = (1 - n/2)R$. For $n = 2$ the Riemann tensor has one component, $R_{\mu\nu\rho\sigma} = \tfrac12 R(g_{\mu\rho}g_{\nu\sigma} - g_{\mu\sigma}g_{\nu\rho})$, so $\mathrm{Ric} = \tfrac12 R g$ and $G \equiv 0$ for every 2-metric: the field equation then says nothing about the geometry and forces $T_{\mu\nu} = -\Lambda g_{\mu\nu}/8\pi$. For $n \ge 3$ the map is invertible, $\mathrm{Ric} = G - \frac{1}{n-2}(\operatorname{tr}G)\,g$, so $G = 0$ if and only if $\mathrm{Ric} = 0$. For $n = 3$ the Weyl tensor vanishes identically and Riemann is an algebraic function of Ricci, so $G = 0$ forces local flatness: three-dimensional vacuum gravity has no local degrees of freedom. For $n = 4$ Riemann has twenty components; $G$ carries the ten of Ricci, and the ten of Weyl are invisible to it. That is the tidal curvature outside matter.

*Observer sums.* For a unit timelike $u$ and any orthonormal basis $e_1, e_2, e_3$ of $u^\perp$, $G(u,u) = \sum_{i<j} K(e_i,e_j)$ with $K$ the sectional curvature in the course sign. The right side is the trace of the curvature operator restricted to $\Lambda^2(u^\perp)$, so it does not depend on the basis. The Gauss equation, stated here without proof, relates this spacetime sum to a spacelike hypersurface $\Sigma$ with unit normal $n$ and extrinsic curvature $K_{ij}$:

$$2\,G_{\mu\nu}n^\mu n^\nu = {}^{(3)}\!R + K^2 - K_{ij}K^{ij},$$

insensitive to the sign convention for $K_{ij}$ because the right side is quadratic in it. Only at a moment of time symmetry, $K_{ij} = 0$, do rings drawn in $\Sigma$ read $G(n,n)$; comoving slices of an expanding universe have $K_{ij} = \pm H h_{ij}$, which supplies the $6H^2$. The four components $G_{\mu\nu}n^\mu$ contain no second derivatives of the metric off $\Sigma$, so the corresponding field equations constrain initial data instead of evolving it: the Hamiltonian and momentum constraints.

*Variation and uniqueness.* $G_{\mu\nu}$ is the Euler–Lagrange tensor of the Einstein–Hilbert density, $\delta(\sqrt{-g}R) = \sqrt{-g}\,G_{\mu\nu}\,\delta g^{\mu\nu} + \sqrt{-g}\,\nabla_\sigma v^\sigma$, the boundary term being removed by fixing the boundary metric and adding the Gibbons–Hawking–York term. Lovelock's theorem closes the circle: in four dimensions every symmetric, divergence-free tensor built from $g$ and its first two derivatives is $aG_{\mu\nu} + b\,g_{\mu\nu}$. Conservation plus second-order equations thus single out the Einstein tensor and a cosmological term, but fix neither $a$, $b$ nor the coupling; those come from the Newtonian limit and observation.

*Limits.* With torsion, the Ricci tensor of the full connection is not symmetric and its Einstein tensor is not divergence-free in this sense; everything above is for the Levi-Civita connection. Restoring units, $G_{\mu\nu}$ keeps dimensions of inverse length squared and faces $8\pi G T_{\mu\nu}/c^4$.

**Takeaway:** Divergence-free for every metric, invertible trace reversal of Ricci except in two dimensions where it vanishes, the sum of an observer's three space-plane curvatures, and with the metric the only second-order candidate in four dimensions.

*Picture:* At one event, the six planes spanned by an orthonormal frame; each diagonal Einstein entry shades the three planes that leave its direction out, and the Weyl part of the curvature, invisible to every entry, sits beside the table.

*Continues:* `ways_in/what-an-observer-reads`<br>*Builds on:* [[contracted-bianchi-identity]], [[sectional-curvature]]<br>*See:* `checks/two-dimensions-vanish`, `checks/conservation-does-not-fix-the-equation`, `problems/dimension-facts`

## Glossary

| Term | Say | In plain words | Concept |
| --- | --- | --- | --- |
| spacetime | — | Space and time taken together as one whole, with four directions: three of space and one of time. | — |
| at rest | — | Not moving relative to the planet, star or cabin named in the sentence, for example held up by a rocket rather than falling. | — |
| tides | — | The slow drifts apart or together, relative to each other, of the crumbs in a small ball just let go: one drift for each of three directions at right angles. The ball itself may fall; the tides are the drifts among the crumbs. | [[ricci-tensor]] |
| ring test | — | Measure the same short distance out from a centre in every direction with a tight string, draw the ring through the far ends, and compare its length with its playground length. | [[ricci-scalar]] |
| playground length | — | The length a ring would have where nothing is curved: about 6.28 times the distance measured out from its centre. A ring can come out short of it or too long. | [[ricci-scalar]] |
| Ricci table | REE-chee table | A table of numbers kept at every place, made from the bigger table that describes the curving there. Its reading for a person adds up the three tides read with crumbs let go beside that person. | [[ricci-tensor]] |
| Einstein table | — | A table made from the Ricci table by taking half its grand total off each space entry and adding it to the time entry. For someone at rest where nothing changes with time, its reading adds up the three rings. | [[einstein-tensor]] |
| reading | — | The one number a table gives to a particular person at a spot. It is the table's time entry when the table's four directions are taken as that person's own: their time, up-down, left-right and front-back. | — |
| grand total | — | One number at each place, made from the Ricci table by adding its three space entries and taking away its time entry. | [[ricci-scalar]] |
| Ricci scalar | REE-chee scalar | One number at each spot; scalar means a single number. The Ricci scalar of space measures the ring total of three small rings drawn there. The Ricci scalar of spacetime is the grand total of the Ricci table, which takes in the time entry too. | [[ricci-scalar]] |
| time entry | — | A table has one entry for each pair of directions. The four entries that pair a direction with itself are its diagonal: the time entry pairs time with time, and the three space entries pair a space direction with itself. | — |
| balance | — | An amount balances when, in every tiny box, it changes only by what flows in or out across the box's walls, like water in a hose. | [[contracted-bianchi-identity]] |
| contracted Bianchi identity | contracted bee-AHN-kee identity | The rule that the Einstein table balances in every smoothly curved spacetime, whatever fills it. | [[contracted-bianchi-identity]] |
| Einstein's law | — | The law of gravity in general relativity. It sets the Einstein table at each place, plus a tiny extra term, equal to a fixed number times the table of the matter there. | [[einstein-field-equations]] |
| pressure | — | How hard matter pushes outward on each bit of its surroundings. | — |

## Key equations

### Definition of the Einstein tensor · working

$$
G_{\mu\nu} = R_{\mu\nu} - \tfrac12 R\,g_{\mu\nu} = G_{\nu\mu}
$$

The Einstein tensor is the Ricci tensor with half the Ricci scalar times the metric taken off; it is symmetric and has units of inverse length squared.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $G_{\mu\nu}$ | Einstein tensor | the Einstein tensor |
| $R_{\mu\nu}$ | Ricci tensor, $R^\rho{}_{\mu\rho\nu}$ | the Ricci tensor |
| $R$ | Ricci scalar, $g^{\mu\nu}R_{\mu\nu}$ | the Ricci scalar |
| $g_{\mu\nu}$ | metric | the metric |

**Holds when:** Levi-Civita connection, course Ricci contraction on the first and third slots, signature $(-,+,+,+)$.  
**Say it:** “The Einstein tensor equals the Ricci tensor minus one half of the Ricci scalar times the metric.”  
**Justified by:** `stated`

### Identically vanishing divergence · working

$$
\nabla_\mu G^{\mu\nu} = 0
$$

The covariant divergence of the Einstein tensor vanishes for every metric, as an identity rather than a law.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $\nabla_\mu$ | covariant derivative of the Levi-Civita connection | the covariant derivative |
| $G^{\mu\nu}$ | Einstein tensor with both indices raised | the Einstein tensor |

**Holds when:** Torsion-free, metric-compatible connection.  
**Say it:** “The divergence of the Einstein tensor is zero.”  
**Justified by:** `contracted-bianchi-identity`

### Trace and inverse in four dimensions · working

$$
g^{\mu\nu}G_{\mu\nu} = -R,\qquad R_{\mu\nu} = G_{\mu\nu} - \tfrac12\,G\,g_{\mu\nu},\quad G \equiv g^{\mu\nu}G_{\mu\nu}
$$

In four dimensions the trace of the Einstein tensor is minus the Ricci scalar, and the same rule applied to the Einstein tensor gives back the Ricci tensor.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $G$ | trace of the Einstein tensor, not Newton's constant | the trace of the Einstein tensor |
| $R$ | Ricci scalar | the Ricci scalar |

**Holds when:** Four dimensions; the derivation gives the general-$n$ form.  
**Say it:** “The trace of the Einstein tensor is minus the Ricci scalar, and the Ricci tensor is the Einstein tensor minus one half of its trace times the metric.”  
**Justified by:** `derivations/trace-reversal-inverts-itself`

### Diagonal entries as plane sums · working

$$
G^{\hat a}{}_{\hat a} = -\sum_{\text{planes}\not\ni a} K,\qquad G_{\hat0\hat0} = K(e_1,e_2) + K(e_2,e_3) + K(e_3,e_1)
$$

In an orthonormal frame, each mixed diagonal entry is minus the sum of the sectional curvatures of the three planes that leave its direction out; the time-time entry is the sum of the three spatial plane curvatures.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $G^{\hat a}{}_{\hat a}$ | mixed diagonal component in an orthonormal frame, no sum on $a$ | the mixed diagonal Einstein component |
| $K$ | sectional curvature of a plane spanned by two frame vectors, course sign | the sectional curvature |
| $e_i$ | the three spatial frame vectors | the spatial frame vectors |

**Holds when:** Orthonormal frame with $e_0$ timelike; $K(e_0,e_i) = -R_{\hat0\hat\imath\hat0\hat\imath}$ and $K(e_i,e_j) = R_{\hat\imath\hat\jmath\hat\imath\hat\jmath}$.  
**Say it:** “Each mixed diagonal Einstein component is minus the sum of the sectional curvatures of the three planes that leave that direction out; the time-time component is the sum of the three spatial plane curvatures.”  
**Justified by:** `derivations/plane-sums-from-the-definition`

### An observer's own component as a density gauge · working

$$
G_{\hat0\hat0} = \frac{G_{\mu\nu}u^\mu u^\nu}{c^2} = \frac{8\pi G}{c^2}\,\rho + \Lambda
$$

Einstein's equation makes an observer's own Einstein component read the energy density they measure, divided by $c^2$, plus the cosmological constant.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $u^\mu$ | observer's four-velocity, $u_\mu u^\mu = -c^2$ | the observer's four-velocity |
| $\rho$ | mass density measured by the observer, $T_{\mu\nu}u^\mu u^\nu/c^4$, so that $\rho c^2$ is the energy density | the measured density |
| $G$ | Newton's constant in the fraction, distinct from the tensor on the left | Newton's constant |
| $\Lambda$ | cosmological constant | the cosmological constant |

**Holds when:** Einstein's equation $G_{\mu\nu} + \Lambda g_{\mu\nu} = 8\pi G T_{\mu\nu}/c^4$ assumed; stated here.  
**Say it:** “The observer's own Einstein component equals eight pi G over c squared times the density they measure, plus the cosmological constant.”  
**Justified by:** `stated`

### Normal-normal component in slice data · formal

$$
2\,G_{\mu\nu}n^\mu n^\nu = {}^{(3)}\!R + K^2 - K_{ij}K^{ij}
$$

Twice the normal-normal Einstein component of a spacelike slice equals the slice's own scalar curvature plus a quadratic in its extrinsic curvature; no second time derivatives appear.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $n^\mu$ | future unit normal to the slice | the unit normal |
| ${}^{(3)}\!R$ | scalar curvature of the slice's own metric | the three-dimensional scalar curvature |
| $K_{ij}$ | extrinsic curvature of the slice, either overall sign; $K$ is its trace | the extrinsic curvature |

**Holds when:** Spacelike hypersurface in a four-dimensional Lorentzian spacetime, $G = c = 1$; from the Gauss equation, stated here.  
**Say it:** “Twice the normal-normal Einstein component equals the slice's scalar curvature plus the trace of the extrinsic curvature squared minus its square.”  
**Justified by:** `stated`

## Derivations

### Plane sums from the definition · working

**Goal:** Show that in an orthonormal frame each mixed diagonal Einstein component is minus the sum of the sectional curvatures of the three planes that leave its direction out, and read off $G_{\hat0\hat0}$ and $G_{\hat1\hat1}$.

1. In an orthonormal frame $\eta = \mathrm{diag}(-1,1,1,1)$, the Ricci contraction is $R_{\hat a\hat b} = \sum_c \eta^{cc}R_{\hat c\hat a\hat c\hat b}$. On the diagonal the $c = a$ term vanishes by antisymmetry, and pair symmetry gives $R_{\hat a\hat a} = \sum_{c\ne a}\eta^{cc}R_{\hat a\hat c\hat a\hat c}$.
2. Define $P_{ac} = \eta^{aa}\eta^{cc}R_{\hat a\hat c\hat a\hat c}$ for $a \ne c$. By the course definition this is the sectional curvature $K(e_a,e_c)$, since the denominator $g(e_a,e_a)g(e_c,e_c)$ equals $\eta_{aa}\eta_{cc}$. Raising one index, $R^{\hat a}{}_{\hat a} = \eta^{aa}R_{\hat a\hat a} = \sum_{c\ne a}P_{ac}$: the planes containing $e_a$.
3. The Ricci scalar is $R = \sum_a R^{\hat a}{}_{\hat a} = \sum_a\sum_{c\ne a}P_{ac} = 2\sum_{a<c}P_{ac}$, because each plane contains two of the four directions.
4. Then $G^{\hat a}{}_{\hat a} = R^{\hat a}{}_{\hat a} - \tfrac12 R = \sum_{c\ne a}P_{ac} - \sum_{b<c}P_{bc} = -\sum_{\{b,c\}\not\ni a}P_{bc}$, with no sum on $a$.
5. For $a = 0$: $G_{\hat0\hat0} = \eta_{00}G^{\hat0}{}_{\hat0} = P_{12} + P_{23} + P_{31} = R_{\hat1\hat2\hat1\hat2} + R_{\hat2\hat3\hat2\hat3} + R_{\hat3\hat1\hat3\hat1}$.
6. For $a = 1$: $G_{\hat1\hat1} = G^{\hat1}{}_{\hat1} = -(P_{02} + P_{03} + P_{23})$, and $P_{0i} = -R_{\hat0\hat\imath\hat0\hat\imath}$, so $G_{\hat1\hat1} = R_{\hat0\hat2\hat0\hat2} + R_{\hat0\hat3\hat0\hat3} - R_{\hat2\hat3\hat2\hat3}$.
7. Off the diagonal $\eta_{ab} = 0$, so $G_{\hat a\hat b} = R_{\hat a\hat b}$ unchanged.

**Result:** $G^{\hat a}{}_{\hat a} = -\sum_{\text{planes}\not\ni a}K$ with no sum on $a$; in particular $G_{\hat0\hat0}$ is the sum of the three spatial plane curvatures.

### Trace reversal inverts itself · working

**Goal:** Find the trace of the Einstein tensor in $n$ dimensions and solve the definition for the Ricci tensor.

1. Trace the definition with $g^{\mu\nu}$, using $g^{\mu\nu}R_{\mu\nu} = R$ and $g^{\mu\nu}g_{\mu\nu} = n$: $\operatorname{tr}G = R - \tfrac12 nR = (1 - n/2)R$. For $n = 4$ this is $-R$.
2. For $n \ne 2$ solve for the Ricci scalar: $R = -\dfrac{2}{n-2}\operatorname{tr}G$.
3. Substitute into $R_{\mu\nu} = G_{\mu\nu} + \tfrac12 R g_{\mu\nu}$: $R_{\mu\nu} = G_{\mu\nu} - \dfrac{1}{n-2}(\operatorname{tr}G)\,g_{\mu\nu}$. For $n = 4$ the coefficient is $\tfrac12$, the same rule as the definition, so the map is its own inverse there.
4. For $n = 2$ the Riemann tensor's single component forces $R_{\mu\nu} = \tfrac12 R g_{\mu\nu}$, so $G_{\mu\nu} = 0$ identically and nothing can be inverted.

**Result:** $\operatorname{tr}G = (1 - n/2)R$; for $n \ne 2$, $R_{\mu\nu} = G_{\mu\nu} - \tfrac{1}{n-2}(\operatorname{tr}G)g_{\mu\nu}$; for $n = 4$, $R_{\mu\nu} = G_{\mu\nu} - \tfrac12 G g_{\mu\nu}$.

## Worked examples

### The expanding universe from six plane curvatures · working

**Problem:** For comoving observers in the course FLRW metric, the six frame plane components are $R_{\hat t\hat\imath\hat t\hat\imath} = -\ddot a/(c^2 a)$ and $R_{\hat\imath\hat\jmath\hat\imath\hat\jmath} = (\dot a^2/c^2 + k)/a^2$; take these as given. Assemble $G_{\hat t\hat t}$ and $G_{\hat x\hat x}$, and evaluate $G_{\hat t\hat t}$ today for $k = 0$ and $H_0 = 67.4$ km/s/Mpc.

1. The time-time entry adds the three space-space planes: $G_{\hat t\hat t} = 3(\dot a^2/c^2 + k)/a^2 = 3H^2/c^2 + 3k/a^2$ with $H = \dot a/a$.
2. The $x$ entry adds the two time-space planes that leave $x$ out and subtracts the one space-space plane that does: $G_{\hat x\hat x} = R_{\hat t\hat y\hat t\hat y} + R_{\hat t\hat z\hat t\hat z} - R_{\hat y\hat z\hat y\hat z} = -2\ddot a/(c^2a) - (\dot a^2/c^2 + k)/a^2$.
3. With $H_0 = 67.4\ \mathrm{km/s}$ per $3.086\times10^{19}$ km $= 2.18\times10^{-18}\ \mathrm{s^{-1}}$, $G_{\hat t\hat t} = 3H_0^2/c^2 = 1.6\times10^{-52}\ \mathrm{m^{-2}}$.
4. The density gauge, with $\Lambda$ inside $\rho$, gives $\rho = 3H_0^2/8\pi G = 8.5\times10^{-27}\ \mathrm{kg/m^3}$.

**Answer:** $G_{\hat t\hat t} = 3H^2/c^2 + 3k/a^2$ and $G_{\hat x\hat x} = -2\ddot a/(c^2a) - (\dot a^2/c^2 + k)/a^2$; today $G_{\hat t\hat t} = 1.6\times10^{-52}\ \mathrm{m^{-2}}$.

**Takeaway:** The plane rule assembles both Friedmann left sides in two lines, and the time-time entry is nonzero even when space is flat.

## Problems

### `ring-and-crumb-survey` · entry · difficulty 1 · conceptual

A surveyor floats at rest, held by a small rocket, at a spot where nothing changes with time. Crumbs she lets go drift apart along the up-down line by four units. Across that line they drift together by two units each way. A ring she draws level, like a floor, is short by four units, and each ring she draws upright, like a wall, is too long by two units. What is the Ricci table's reading for her, and what is the Einstein table's reading? Could this spot be deep inside a huge ball of still water, far from any planet?

**Hints**

1. Which three parts does each reading add up?
2. Inside still water, do the three rings come out short, or too long, or mixed?

**Answer:** Both readings are zero. The spot cannot be inside still water, where all three rings come out short and their total is not zero; it looks like empty space near a planet.

**Must contain:** The Ricci reading adds the tides: four minus two minus two is zero; The Einstein reading adds the rings: four minus two minus two is zero; Inside still water all three rings come out short, so the ring total is not zero

**Numeric:** Einstein reading = 0 1 (magnitude, ±0)

**Solution**

1. The Ricci reading adds the three tides. Drifting apart counts plus and drifting together counts minus, so it is four minus two minus two, which is zero.
2. The Einstein reading adds the three rings. A short ring counts plus and a long ring counts minus, so it is four minus two minus two, which is also zero.
3. Inside a ball of still water every ring comes out short, so the ring total there is three shortfalls added together, not zero. A zero ring total with strong tides is what empty space near a planet gives.

**Targets:** `tides-set-the-einstein-reading`

### `constant-curvature-einstein` · working · difficulty 2 · calculation

A four-dimensional spacetime of constant curvature has $R_{\mu\nu\rho\sigma} = K(g_{\mu\rho}g_{\nu\sigma} - g_{\mu\sigma}g_{\nu\rho})$ with $K$ constant. Find $R_{\mu\nu}$, $R$ and $G_{\mu\nu}$. If the spacetime is empty apart from a cosmological constant, what $\Lambda$ does it need? Evaluate for $K = H_0^2/c^2$ with $H_0 = 67.4$ km/s/Mpc.

**Hints**

1. Contract on the first and third slots with $g^{\mu\rho}$, remembering $g^{\mu\rho}g_{\mu\rho} = 4$.

**Answer:** $R_{\mu\nu} = 3Kg_{\mu\nu}$, $R = 12K$, $G_{\mu\nu} = -3Kg_{\mu\nu}$, and $\Lambda = 3K$; for $K = H_0^2/c^2$, $\Lambda = 1.6\times10^{-52}\ \mathrm{m^{-2}}$.

**Must contain:** Ricci tensor is 3K times the metric; Ricci scalar is 12K; Einstein tensor is minus 3K times the metric; Lambda equals 3K

**Numeric:** cosmological constant = 1.59e-52 m^-2 (signed, ±3%)

**Solution**

1. $R_{\nu\sigma} = g^{\mu\rho}R_{\mu\nu\rho\sigma} = K(4g_{\nu\sigma} - g_{\nu\sigma}) = 3Kg_{\nu\sigma}$.
2. $R = g^{\nu\sigma}R_{\nu\sigma} = 12K$.
3. $G_{\mu\nu} = 3Kg_{\mu\nu} - 6Kg_{\mu\nu} = -3Kg_{\mu\nu}$; its trace $-12K$ is $-R$, as it must be.
4. Vacuum with a cosmological constant needs $G_{\mu\nu} + \Lambda g_{\mu\nu} = 0$, so $\Lambda = 3K$: de Sitter space is the constant-curvature vacuum.
5. With $H_0 = 2.18\times10^{-18}\ \mathrm{s^{-1}}$, $\Lambda = 3H_0^2/c^2 = 1.6\times10^{-52}\ \mathrm{m^{-2}}$.

### `dimension-facts` · formal · difficulty 2 · proof

Prove: (a) the Einstein tensor vanishes identically for every two-dimensional metric; (b) for $n \ge 3$, $G_{\mu\nu} = 0$ if and only if $R_{\mu\nu} = 0$; (c) in three dimensions the Einstein tensor determines the whole Riemann tensor, and write the formula. How many independent components does the Riemann tensor have in three dimensions?

**Hints**

1. In two dimensions the Riemann tensor is antisymmetric in each pair, so it has one component; write it as a multiple of $g_{\mu\rho}g_{\nu\sigma} - g_{\mu\sigma}g_{\nu\rho}$.
2. Use the trace formula $\operatorname{tr}G = (1 - n/2)R$, then count components in three dimensions.

**Answer:** (a) $R_{\mu\nu\rho\sigma} = \tfrac12 R(g_{\mu\rho}g_{\nu\sigma} - g_{\mu\sigma}g_{\nu\rho})$ gives $R_{\mu\nu} = \tfrac12 Rg_{\mu\nu}$, so $G = 0$. (b) $R_{\mu\nu} = G_{\mu\nu} - \tfrac{1}{n-2}(\operatorname{tr}G)g_{\mu\nu}$. (c) $R_{abcd} = g_{ac}R_{bd} - g_{ad}R_{bc} - g_{bc}R_{ad} + g_{bd}R_{ac} - \tfrac12 R(g_{ac}g_{bd} - g_{ad}g_{bc})$ with $R_{ab} = G_{ab} - (\operatorname{tr}G)g_{ab}$; six independent components.

**Must contain:** In two dimensions Ricci is half R times the metric, so G vanishes; For n at least three the inverse formula recovers Ricci from G; In three dimensions Weyl vanishes and Riemann is the Ricci part alone; Six independent components in three dimensions

**Numeric:** independent Riemann components in three dimensions = 6 1 (signed, ±0)

**Solution**

1. (a) In two dimensions the only antisymmetric pair is $(1,2)$, so $R_{\mu\nu\rho\sigma} = f(g_{\mu\rho}g_{\nu\sigma} - g_{\mu\sigma}g_{\nu\rho})$ for some function $f$. Contracting once gives $R_{\nu\sigma} = f(2 - 1)g_{\nu\sigma} = fg_{\nu\sigma}$, contracting again gives $R = 2f$, so $R_{\mu\nu} = \tfrac12 Rg_{\mu\nu}$ and $G_{\mu\nu} = 0$.
2. (b) Tracing the definition gives $\operatorname{tr}G = (1 - n/2)R$, so for $n \ne 2$, $R = -2\operatorname{tr}G/(n-2)$ and $R_{\mu\nu} = G_{\mu\nu} - \tfrac{1}{n-2}(\operatorname{tr}G)g_{\mu\nu}$. If $G = 0$ then $\operatorname{tr}G = 0$ and $R_{\mu\nu} = 0$; the converse is immediate from the definition.
3. (c) The Riemann tensor has $n^2(n^2-1)/12$ independent components, six for $n = 3$, the same as the symmetric Ricci tensor, so the Weyl tensor has none. So the Riemann tensor equals its Ricci part, $R_{abcd} = g_{ac}R_{bd} - g_{ad}R_{bc} - g_{bc}R_{ad} + g_{bd}R_{ac} - \tfrac12 R(g_{ac}g_{bd} - g_{ad}g_{bc})$, as a contraction on $a$ and $c$ confirms: $3R_{bd} - R_{bd} - R_{bd} + g_{bd}R - \tfrac12 R(3g_{bd} - g_{bd}) = R_{bd}$.
4. For $n = 3$ the inverse map is $R_{ab} = G_{ab} - (\operatorname{tr}G)g_{ab}$, so $G$ fixes Ricci, hence Riemann; in particular $G = 0$ forces local flatness.

**Targets:** `inverse-rule-in-every-dimension`

## Observations

- **The measured Hubble constant fixes the time-time Einstein component read by comoving observers, and hence the critical density of the universe** (measured, working). For comoving observers in a spatially flat universe $G_{\hat t\hat t} = 3H_0^2/c^2$, and the density gauge turns this into the total energy density, cosmological constant included. Cosmic microwave background measurements give $H_0$ and find the spatial curvature term consistent with zero. *Numbers:* $H_0 = 67.4 \pm 0.5$ km/s/Mpc gives $G_{\hat t\hat t} = 1.6\times10^{-52}\ \mathrm{m^{-2}}$ and a critical density of $8.5\times10^{-27}\ \mathrm{kg/m^3}$, about five hydrogen atoms per cubic metre. *Reference:* Planck Collaboration, N. Aghanim, Y. Akrami, M. Ashdown and others (2020), *Planck 2018 results. VI. Cosmological parameters*, Astronomy and Astrophysics 641, A6, doi:10.1051/0004-6361/201833910
- **Mercury's perihelion advances by about 43 arcseconds per century beyond what the other planets cause, inside a region where the Einstein tensor vanishes** (measured, working). Outside the Sun the Einstein tensor is zero, so all ten Ricci components vanish; the advance comes from the ten Weyl components the Einstein tensor cannot see, so a vanishing Einstein tensor is not flat spacetime. *Numbers:* General relativity predicts $42.98$ arcseconds per century; ranging to the MESSENGER spacecraft confirmed the advance to well under one percent. *Reference:* Ryan S. Park, William M. Folkner, Alexander S. Konopliv, James G. Williams, David E. Smith, Maria T. Zuber (2017), *Precession of Mercury's Perihelion from Ranging to the MESSENGER Spacecraft*, The Astronomical Journal 153, 121, doi:10.3847/1538-3881/aa5be2

## Teaching arc

1. **Lay out the six parts, then build the table** (entry). Set the scene above the planet, read the tides and the rings, ask for the two totals, then give the still-water Ricci diagonal and have the learner apply the rule. *Why:* The learner sees that both tables share their six inputs and differ only in the split, and one round of arithmetic fixes the sign twist between time and space. *Predict:* The tides above the planet are strong. Will the Einstein table's reading be large, small, or zero? *Visual:* [[six-entry-curvature-table]] *Uses:* `ways_in/three-tides-and-three-rings`, `checks/rings-not-tides`, `ways_in/half-the-grand-total-off`, `checks/build-the-water-table`
2. **Write the formula and derive the plane rule** (working). State the definition, take the trace, then derive the plane sums and test them on the six components outside a spherical mass. *Why:* The plane rule turns index algebra into a picture the learner already owns and shows a vanishing tensor with nonzero parts. *Uses:* `ways_in/trace-reversal-and-plane-sums`, `derivations/plane-sums-from-the-definition`, `checks/zero-einstein-not-flat`
3. **Read the density gauge and spring the expanding-universe trap** (working). Introduce the observer's own component as a density gauge, then ask what comoving observers read in a flat expanding universe before assembling it from the plane rule. *Why:* Rings in space versus planes in spacetime is the one place the entry picture can mislead, and the Hubble number makes the reading real. *Predict:* Space is flat in this universe. Is the comoving time-time Einstein component zero? *Visual:* [[rings-in-an-expanding-grid]] *Uses:* `ways_in/what-an-observer-reads`, `worked_examples/expanding-universe-from-planes`, `checks/flat-universe-not-zero`
4. **Place the object in n dimensions** (formal). Work through the trace in $n$ dimensions, the two- and three-dimensional degeneracies, the Gauss-equation form of the observer sum, and Lovelock's uniqueness. *Why:* A graduate student needs the hypotheses and the failures, not only the four-dimensional formula. *Uses:* `ways_in/the-object-in-n-dimensions`, `checks/two-dimensions-vanish`, `checks/conservation-does-not-fix-the-equation`

## Misconceptions

### “Where the tides are strong, the Einstein table's reading for me must be large.” · entry · `tides-set-the-einstein-reading`

- **Why it is tempting:** Tides are the most visible sign of curving, and the Ricci table's reading does add them up.
- **What is true:** The Einstein reading adds the three rings, not the tides. Above a planet the tides are strong and both totals are still zero.
- **Exposed by:** `checks/rings-not-tides`

### “The rule takes half the grand total off every diagonal entry, the time entry included.” · entry · `half-off-the-time-entry-too`

- **Why it is tempting:** The rule is usually said in one breath as taking half the grand total off.
- **What is true:** Time and space enter with opposite signs, so the time entry gets the half added. For still water that gives two, zero, zero, zero, not zero, zero, zero, zero.
- **Exposed by:** `checks/build-the-water-table`

### “Where the Einstein tensor vanishes there is no curvature.” · working · `zero-einstein-means-flat`

- **Why it is tempting:** The vacuum field equation is often summarized as no matter, no curvature.
- **What is true:** A vanishing Einstein tensor means a vanishing Ricci tensor, ten of Riemann's twenty components. The other ten, the Weyl part, give the tides outside the Sun.
- **Exposed by:** `checks/zero-einstein-not-flat`

### “Rings drawn in space always read an observer's time-time Einstein component, so a universe with flat space has a zero one.” · working · `space-rings-always-give-the-reading`

- **Why it is tempting:** The entry picture identifies the reading with the ring total, and it works above a planet.
- **What is true:** Rings read the slice's own curvature, which equals the spacetime plane sum only when the slice is not bending in time. Comoving slices of an expanding universe bend, adding three times the Hubble rate squared.
- **Exposed by:** `checks/flat-universe-not-zero`

### “The inverse rule, Ricci equals the Einstein tensor minus half its trace times the metric, holds in every dimension.” · formal · `inverse-rule-in-every-dimension`

- **Why it is tempting:** In four dimensions trace reversal is its own inverse, and the formula looks dimension-free.
- **What is true:** The inverse coefficient is one over n minus two, which equals a half only for n equal to four. For n equal to two the Einstein tensor vanishes identically and nothing can be inverted.
- **Exposed by:** `checks/two-dimensions-vanish`

### “Because both the Einstein tensor and the stress-energy tensor are divergence-free, conservation alone forces the field equation.” · formal · `conservation-forces-the-equation`

- **Why it is tempting:** The matching of two identities reads like a derivation.
- **What is true:** The metric is divergence-free too, so a cosmological term is allowed, and Lovelock's theorem gives a two-parameter family. Matching divergences is necessary, not sufficient.
- **Exposed by:** `checks/conservation-does-not-fix-the-equation`

## Checks

1. **Entry · evaluate-claim** `checks/rings-not-tides`. Someone floats at rest above an airless planet that does not spin, inside a cabin, where nothing changes with time. Crumbs she lets go drift apart along the up-down line and together across it. She says: the tides here are strong, so the Einstein table's reading for me must be large. Is she right?
   - **Hints:** Which three parts does the Einstein table add? / How do the two wall rings compare with the floor ring?
   - **Answer:** No. The Einstein table's reading adds up the three rings, not the tides. Above the planet her floor ring comes out short by two units, and each wall ring too long by one unit. So the ring total is two minus one minus one, which is zero, and her Einstein reading is zero. The tides are strong, but they total zero too: apart by two, together by one and one.
   - **Must contain:** The Einstein reading adds the rings, not the tides; Floor ring short by two, wall rings long by one each; The reading is zero although the tides are strong
   - **Targets:** `tides-set-the-einstein-reading`
   - **Visual:** [[six-entry-curvature-table]]
2. **Entry · numeric** `checks/build-the-water-table`. Deep inside still water, the Ricci table's diagonal reads one, one, one, one: the time entry first, then the three space entries. Build the Einstein table's diagonal. What is its time entry, and what are its space entries?
   - **Hints:** Does the time entry count plus or minus in the grand total? / Is the half taken off the time entry, or added to it?
   - **Answer:** The grand total adds the three space entries and takes away the time entry: three minus one is two. Half of two is one. Each space entry becomes one minus one, which is zero. The time entry gets the half added, because time and space enter with opposite signs, so it becomes one plus one, which is two. The Einstein diagonal is two, zero, zero, zero.
   - **Must contain:** Grand total is three minus one, which is two; Space entries become zero; Time entry becomes two, because the half is added to it
   - **Numeric:** time entry = 2 1 (signed, ±0); each space entry = 0 1 (signed, ±0)
   - **Targets:** `half-off-the-time-entry-too`
   - **Visual:** [[six-entry-curvature-table]]
3. **Working · explain** `checks/zero-einstein-not-flat`. Outside the Sun the Einstein tensor vanishes. Does that make spacetime flat there? In the static frame, which of the six plane components $R_{\hat a\hat b\hat a\hat b}$ are zero?
   - **Hints:** How many independent components has the Riemann tensor, and how many does the Ricci tensor carry?
   - **Answer:** No. In four dimensions $G_{\mu\nu} = 0$ is equivalent to $R_{\mu\nu} = 0$, which fixes ten of the Riemann tensor's twenty components and leaves the ten Weyl components free. Outside a mass none of the six plane components is zero: in units of $GM/c^2r^3$ they are $-2, +1, +1$ for the time-space planes and $-1, -1, +2$ for the space-space planes. Each Einstein entry adds three of them to zero, yet the $-2$ entry is the tide that stretches a falling body along the radius.
   - **Must contain:** Vanishing Einstein tensor means vanishing Ricci tensor only; The Weyl components survive; None of the six plane components vanishes; each Einstein sum does
   - **Targets:** `zero-einstein-means-flat`
   - **Visual:** [[six-entry-curvature-table]]
4. **Working · evaluate-claim** `checks/flat-universe-not-zero`. In a spatially flat expanding universe, rings drawn in space at one cosmic time come out at their playground length. A learner concludes that comoving observers read $G_{\hat t\hat t} = 0$. Evaluate the claim, and give today's value for $H_0 = 67.4$ km/s/Mpc.
   - **Hints:** Are the space-space planes of spacetime the same as planes in the slice?
   - **Answer:** The claim is false. The rings measure the slice's own curvature, which is zero for $k = 0$. But $G_{\hat t\hat t}$ adds the curvatures of the three space-space planes of spacetime, each equal to $(\dot a/a)^2/c^2$ because comoving neighbours are moving apart, so $G_{\hat t\hat t} = 3H^2/c^2$. Today that is $3H_0^2/c^2 = 1.6\times10^{-52}\ \mathrm{m^{-2}}$.
   - **Must contain:** Rings read the slice's curvature, zero for k equal to zero; The spacetime space-space planes carry the Hubble rate squared; Today's value is about 1.6 times ten to the minus 52 per square metre
   - **Numeric:** comoving time-time Einstein component today = 1.59e-52 m^-2 (signed, ±5%)
   - **Targets:** `space-rings-always-give-the-reading`
   - **Visual:** [[rings-in-an-expanding-grid]]
5. **Formal · derive** `checks/two-dimensions-vanish`. Show that the Einstein tensor of every two-dimensional metric vanishes, and explain why the four-dimensional inverse rule $R_{\mu\nu} = G_{\mu\nu} - \tfrac12 G g_{\mu\nu}$ cannot hold in two dimensions or in any dimension other than four.
   - **Hints:** How many independent components has the Riemann tensor in two dimensions?
   - **Answer:** In two dimensions the Riemann tensor has one independent component, so $R_{\mu\nu\rho\sigma} = f(g_{\mu\rho}g_{\nu\sigma} - g_{\mu\sigma}g_{\nu\rho})$; contracting gives $R_{\mu\nu} = fg_{\mu\nu}$ and $R = 2f$, so $R_{\mu\nu} = \tfrac12 Rg_{\mu\nu}$ and $G_{\mu\nu} = 0$ for every metric. In general $\operatorname{tr}G = (1 - n/2)R$, so the inverse is $R_{\mu\nu} = G_{\mu\nu} - \tfrac{1}{n-2}(\operatorname{tr}G)g_{\mu\nu}$; the coefficient equals one half only for $n = 4$, and for $n = 2$ the map is not invertible at all, since it sends every Ricci tensor to zero.
   - **Must contain:** Two-dimensional Riemann has one component, so Ricci is half R times the metric; The inverse coefficient is one over n minus two; For n equal to two the map is not invertible
   - **Targets:** `inverse-rule-in-every-dimension`
6. **Formal · evaluate-claim** `checks/conservation-does-not-fix-the-equation`. Claim: since $\nabla_\mu T^{\mu\nu} = 0$ and $\nabla_\mu G^{\mu\nu} = 0$, conservation of energy and momentum forces the field equation $G_{\mu\nu} = \kappa T_{\mu\nu}$. Evaluate the claim.
   - **Hints:** Is there another symmetric tensor whose covariant divergence vanishes for every metric?
   - **Answer:** The claim overreaches. Matching divergences is necessary, which is why the Ricci tensor fails. It is not sufficient: $g_{\mu\nu}$ is divergence-free too, so $G_{\mu\nu} + \Lambda g_{\mu\nu} = \kappa T_{\mu\nu}$ is equally consistent, and Lovelock's theorem shows that $aG_{\mu\nu} + bg_{\mu\nu}$ exhausts the symmetric divergence-free tensors built from the metric and its first two derivatives in four dimensions. The constants $a$, $b$ and $\kappa$ come from the Newtonian limit and observation.
   - **Must contain:** Divergence-free is necessary but not sufficient; The metric term with Lambda is also allowed; Lovelock gives a two-parameter family; constants come from the Newtonian limit and observation
   - **Targets:** `conservation-forces-the-equation`

## Notation traps

| Issue | Course choice | Variants you will meet |
| --- | --- | --- |
| The letter G for the tensor, for Newton's constant and for Green's functions | The Einstein tensor always carries its indices, $G_{\mu\nu}$ or $G^{\mu\nu}$, and its trace is written $g^{\mu\nu}G_{\mu\nu}$ wherever Newton's constant $G$ is nearby. | Some texts write a bold or index-free $\mathbf G$ for the tensor and $G = 8\pi T$ in geometrized units, where the plain letter is the tensor; others reuse $G$ for a Green's function in the same chapter. |
| Trace-free Ricci tensor versus trace-reversed Ricci tensor | The Einstein tensor is $R_{\mu\nu} - \tfrac12 Rg_{\mu\nu}$, trace reversed, with trace $-R$ in four dimensions. The trace-free Ricci tensor $R_{\mu\nu} - \tfrac14 Rg_{\mu\nu}$ is named as such and never called the Einstein tensor. | Some texts call the quarter-subtracted tensor trace-reversed or label it with the same letter; for null vectors all three agree, since $k^\mu k^\nu g_{\mu\nu} = 0$. |

## Visuals

- ★ [[six-entry-curvature-table]] (flagship): The central experience: six plane tiles at one event with Ricci and Einstein readouts, showing which three tiles each diagonal entry adds and the planet and still-water cases. *Sketch:* This concept adds Einstein readouts beside the Ricci ones. Choosing a diagonal Einstein entry lights the three tiles that leave its direction out; presets load the planet values (time-space $-2,+1,+1$; space-space $-1,-1,+2$) and the still-water values.
- [[three-rings-around-a-spot]] (supporting): The ring readings of the entry picture, with the Einstein reading beside the ring total. *Sketch:* This concept adds a readout naming the ring total as the Einstein reading for the people at rest, and a switch to a spot inside still water where all three rings come out short.
- [[falling-ring-of-crumbs]] (supporting): The tide readings of the entry picture, with the tides total labelled as the Ricci reading. *Sketch:* This concept adds a readout of the three drifts and their total, labelled as the Ricci reading, beside the ring total labelled as the Einstein reading.
- [[rings-in-an-expanding-grid]] (supporting): Rings drawn in flat expanding space come out at their playground length while the comoving time-time Einstein component reads three times the Hubble rate squared. *Sketch:* A grid of comoving dots expands with a scale-factor slider. Rings drawn among the dots read a zero shortfall, while a spacetime side view shows the comoving worldlines diverging, with readouts of the plane curvature $(\dot a/a)^2/c^2$ and of $G_{\hat t\hat t} = 3H^2/c^2$.

## Tutor moves

**Open with**

- Picture yourself floating at rest above an airless planet, inside a small cabin. Crumbs you let go drift apart up and down and together sideways. You also draw three small rings, one on the floor and one on each of two walls. Which rings come out short, which too long, and do the three add up to something or cancel? *(prediction)*

**If the learner is stuck**

- *The learner keeps adding tides into the Einstein reading or rings into the Ricci reading.* → Lay out the six parts as two rows, tides and rings, and have the learner point to the row each table adds. *Uses:* `ways_in/three-tides-and-three-rings`
- *The learner subtracts the half from the time entry as well, or adds the four Ricci entries as a plain sum.* → Return to the grand total: ask whether the time entry counts plus or minus there, then apply the same opposite-sign rule to the half. *Uses:* `ways_in/half-the-grand-total-off`, `checks/build-the-water-table`

**Common questions**

- *If both tables come from the same six parts, why keep two of them?* (entry) Because they answer different questions. The Ricci table's reading says whether a ball of crumbs starts to shrink, and pressure counts in that. The Einstein table balances: in every tiny box, its amount changes only by what flows in or out through the box's walls. Water flowing along a hose balances in the same way: none is made or lost on the way. The table of matter balances in the same way, so Einstein's law can set the two tables equal. That is why the law uses the Einstein table. *Uses:* `ways_in/three-tides-and-three-rings`, `contracted-bianchi-identity/ways_in/a-table-of-curving-that-balances`

**Switching levels**

- To working when: asks for the formula or the trace; starts naming components. Write the definition, take the trace, and go to the plane rule with the planet components. *Uses:* `ways_in/trace-reversal-and-plane-sums`, `ways_in/what-an-observer-reads`
- To formal when: asks about other dimensions or what fixes the field equation; asks about slices, torsion or the action. Move to the n-dimensional statement, the Gauss equation form, and Lovelock's theorem. *Uses:* `ways_in/the-object-in-n-dimensions`

**Pronunciations:** Ricci → REE-chee; Bianchi → bee-AHN-kee; Lovelock → LUV-lock

**Voice notes:** Always say "the Einstein tensor" or "the Einstein table" in full, never "G" alone, which the learner hears as Newton's constant. Introduce "component" only at the working rung.

## History

- **Albert Einstein (1915).** After first proposing the Ricci tensor as the geometric side in November 1915, arrived within weeks at the equations with the trace term, the combination that is divergence-free and consistent with conservation of energy and momentum; it has carried his name since. Albert Einstein (1915), *Die Feldgleichungen der Gravitation*, Sitzungsberichte der Königlich Preußischen Akademie der Wissenschaften (Berlin), 844–847
- **David Hilbert (1915).** Presented on 20 November 1915 and printed in March 1916, after Einstein's paper of 25 November. Derived the gravitational field equations from a variational principle, in which the Einstein tensor appears as the metric variation of the scalar curvature density rather than being engineered for conservation. David Hilbert (1915), *Die Grundlagen der Physik. (Erste Mitteilung)*, Nachrichten von der Gesellschaft der Wissenschaften zu Göttingen, Mathematisch-Physikalische Klasse, 395–407

## Research horizon

- **Lovelock's theorem and higher-dimensional Einstein tensors.** In four dimensions the Einstein tensor and the metric are the only symmetric divergence-free tensors built from the metric and its first two derivatives. In five or more dimensions further such tensors exist, the Lovelock tensors, whose field equations remain second order; their study underlies Gauss–Bonnet gravity and the classification of modified theories. David Lovelock (1971), *The Einstein Tensor and Its Generalizations*, Journal of Mathematical Physics 12, 498–501, doi:10.1063/1.1665613; David Lovelock (1972), *The Four-Dimensionality of Space and the Einstein Tensor*, Journal of Mathematical Physics 13, 874–876, doi:10.1063/1.1666069
- **The constraint equations and the initial-value problem.** The Einstein components with one index along a slice's normal contain no second time derivatives, so the field equations split into four constraints on initial data and six evolution equations. Solving the constraints, and proving that the evolution is well posed and preserves them, is the mathematical foundation of numerical relativity and of existence theorems for spacetimes. Yvonne Fourès-Bruhat (1952), *Théorème d'existence pour certains systèmes d'équations aux dérivées partielles non linéaires*, Acta Mathematica 88, 141–225, doi:10.1007/BF02392131; Robert Bartnik, Jim Isenberg (2004), *The constraint equations*, In P. T. Chruściel and H. Friedrich (eds), The Einstein Equations and the Large Scale Behavior of Gravitational Fields, Birkhäuser, 1–38, arXiv:gr-qc/0405092
- **Positive energy from the normal-normal component.** Through the Hamiltonian constraint, the dominant energy condition makes the normal-normal Einstein component nonnegative, which at a moment of time symmetry is nonnegative scalar curvature of the slice. The positive mass theorem turns this local inequality into a global one: the total mass of an asymptotically flat slice is nonnegative and vanishes only for flat space. Richard Schoen, Shing-Tung Yau (1979), *On the proof of the positive mass conjecture in general relativity*, Communications in Mathematical Physics 65, 45–76, doi:10.1007/BF01940959; Edward Witten (1981), *A new proof of the positive energy theorem*, Communications in Mathematical Physics 80, 381–402, doi:10.1007/BF01208277

## Review: novice

**Verdict:** fixed (2026-09-16, revision 4)

**Retell attempt:** At a spot there are six parts of curving: three tides from crumbs and three rings drawn on the floor and two walls. The Ricci table adds up the tides and the Einstein table adds up the rings. Above a planet the floor ring is short by two and each wall ring is long by one, so the rings add to zero, and the tides add to zero too, so both readings are zero. I don't know why there are six parts, why the floor ring is the short one, or why the crumbs I let go while hanging from a rocket don't just fall. The Einstein table comes from the Ricci table by taking half the grand total off the space entries and adding it to the time entry; in still water one, one, one, one becomes two, zero, zero, zero, but I'm not sure what an entry or a diagonal is, and I thought the Ricci scalar was the ring total, so what is the grand total? Something about a hose makes Einstein's law use this table, which I did not follow.

**Stumbles (22)**

- “At your spot, the curving of spacetime has six parts, and you can read all six.”: A surprising count with no reason; the reader cannot tell where six comes from or which parts are tides and which are rings.
- “Let go of a small ball of crumbs, at rest beside you.”: The reader is held up by a rocket, so the first what-if is that the crumbs simply fall to the floor; the sentence says nothing about that.
- “The crumbs across that line drift together, in both across directions.”: The two across directions are never named, although the walls are named a paragraph later.
- “one on the left wall and one on the front wall”: Left and front with no reference: whose left, seen from where.
- “The ring on the floor comes out short. Each ring on a wall comes out too long, by half as much as the floor ring is short.”: A surprising claim with no reason or count within two sentences.
- “The Ricci table's reading for you adds up the three tides.”: The new term reading is used before it is given its own sentence; the glossary defines it through the time entry, which the reader has not met yet.
- “The tides also come in the sizes two, minus one, minus one, and their total is zero too.”: Which drift is which, and why apart counts plus and together counts minus, is left implicit.
- “Because the ring count is the one that balances everywhere, like water flowing through a hose.”: Ring count and ring total are two words for one idea; balances is undefined in its sentence; the hose is a simile with no explanation; and the paragraph asks the reader to hold balance, the contracted Bianchi identity and Einstein's law at once.
- “a level ring drawn one kilometre out from its centre ... The two upright rings”: Level and upright arrive as new words for the floor ring and the wall rings, and the same pair appears unexplained in the survey problem.
- “In the crumb test, someone falling freely lets go of a small ball of crumbs at rest.”: The recap has someone falling freely, but the way has the reader at rest on a rocket letting the crumbs go.
- “The Ricci table has four entries down its diagonal: one for time, and three for space”: Entry and diagonal are new words with no sentence of their own; the reader does not know what a table's diagonal is.
- “Inside still water, Einstein's law makes all four the same size.”: A surprising claim with no reason and no scope; the reader cannot tell whether it is a fact to trust or something to work out.
- “deep inside a tank of still water ... Inside still water all three rings come out short, by the same amount”: The first what-if is a tank on Earth, and there the two wall rings still come out too long because the planet's curving dominates; only the ring total is set by the water.
- “and it is two units: it counts the water.”: Counts the water is vague; the reader cannot say what the number has to do with the water.
- “Above the planet the Ricci table is all zeros, so the rule gives all zeros again, as the ring count said.”: The reader only knows from the Ricci tensor note that the tides total is zero, not every entry; and ring count is again used for ring total.
- “First find the grand total.”: The Ricci scalar note taught the reader that the Ricci scalar is the ring total; here the ring total is the Einstein reading and the Ricci scalar appears as a grand total, with no bridge between the two names.
- “Above the planet her floor ring comes out short by two units”: The check's question puts her above a planet with no cabin, so there is no floor or wall to draw on.
- “A surveyor floats at rest at a spot where nothing changes with time. ... Her level ring is short by four units, and each upright ring is too long by two units.”: At rest relative to what is not said, and level and upright rings are named without the floor and wall picture.
- “The Einstein table balances everywhere, like water in a hose, so it can be set equal to the table of matter, which also balances.”: In the common question the hose simile is again given without saying what balances means.
- “the time entry of the table written in that person's own directions”: Glossary wording a novice cannot parse: written in directions.
- “The slow drifts apart or together of crumbs let go at rest by someone falling freely”: The glossary ties the tides to someone falling freely, while the way has them read by someone at rest whose crumbs fall.
- “the Einstein table's reading adds up the three rings.”: The way's takeaway drops the scope that the summary and simplifies carry: rings read the Einstein table only where nothing changes with time.

**Fixes**

- Way three-tides-and-three-rings: gave the count of six as pairs of the four directions and said which pairs are tides and which are rings; made the crumbs fall and the drifts relative; named the across directions; referenced the walls to the reader; introduced level and upright once; backed the floor-short, wall-long fact with the zero ring total the reader already owns; gave reading its own sentence; wrote out which tide counts plus and which minus; cut the balance paragraph to a three-sentence pointer naming balance and the contracted Bianchi identity note, with the explanation moved to the common question why-two-tables; dropped the ring-drawing sentence that the recap already carries; split the Earth sentence that ran to 33 words.
- Way half-the-grand-total-off: moved the still water to a huge ball far from any planet, so that all three rings come out short is true for the first what-if; described the table's rows, columns and diagonal before using entry and diagonal; scoped and marked as taken on trust the claim that all four Ricci entries are equal; added the bridge between the grand total (Ricci scalar of spacetime) and the ring total of the Ricci scalar note; replaced it counts the water with a proportionality statement; gave a reason for every Ricci entry being zero above the planet; replaced ring count with ring total and counts with adds up throughout.
- Recap of the first way, glossary entries tides, Ricci table and reading, a new glossary entry Ricci scalar (the entry text now uses the term), the check rings-not-tides, the problem ring-and-crumb-survey, the common question why-two-tables, the first way's takeaway and the tagline reworded as the stumbles record. No item was dropped. Entry explanations grew from 736 to 1089 words, over the 1000 core cap and inside the 10% review allowance; the growth is the six-pairs count, the falling-crumbs caveat, the rows-and-diagonal description and the grand-total bridge, each recorded above.

**Concerns**

- Entry explanations stand at 1089 words, inside the review allowance but over the 1000 cap. Any further entry addition needs a cut; the first candidate is the three-sentence balance pointer in the first way, whose content the common question why-two-tables carries.
- The Ricci scalar note's entry rung calls the ring total the Ricci scalar, while this note's entry rung makes the ring total the Einstein reading and names the spacetime Ricci scalar the grand total. The bridge sentence added here says the two totals agree inside still water but need not in general; the physics reviewer should confirm that wording (the ring total is proportional to the slice's own scalar curvature, twice the observer's Einstein component in a static slice).
- The physics reviewer should check the new sentence that crumbs released by an observer held up by a rocket show the same tides among themselves just after release: the initial relative drifts are the geodesic deviation for the static observer's four-velocity, which is what the entry way needs.
- The problem ring-and-crumb-survey and the check build-the-water-table give crumb drifts and ring shortfalls in the same abstract units; the way now says whatever its actual size once. A tutor should be ready for the question units of what.
- The four proposed visuals are unchanged; six-entry-curvature-table is cited by the entry ways with no preset or tour.

**Re-read** (2026-09-16, revision 4): 2 stumbles in 4 changed passages

- “hold the string level and straight, not along the ground, and draw a ring one kilometre out from its centre.”: An instruction with a prohibition and no reason: the reader cannot tell what is wrong with laying the string along the ground, so the 'not' reads as an arbitrary rule.
- “the $c^2$ coming from $u_\mu u^\mu = -c^2$”: Names a true fact but not how it makes the factor: a reader does not see why a norm produces a division by $c^2$ in a contraction with two copies of $u$.
- Fix: Entry ring sentence reordered, word-neutral (23 words), with the implied reason for not following the ground made explicit; entry stays at 1096 words, inside the 10% allowance.
- Fix: Working c^2 explanation now says the contraction carries two factors of the frame component u^0 = c, which the division undoes; same claim, same equation.

## Review: physics

**Verdict:** fixed (2026-09-16, revision 4)

**Verification**

- Static-frame Schwarzschild plane components: R_trtr = -2, R_tθtθ = R_tφtφ = +1, R_rθrθ = R_rφrφ = -1, R_θφθφ = +2 in units of GM/c²r³; plane rule gives G_tt = G_rr = 0.: python3 finite-difference Riemann from the course Christoffel and Riemann definitions at r = 10M; frame components, Ricci diagonal, plane sums; 2-sphere control gives R = +2/a². → All six match to 4 decimals; Ricci diagonal and R vanish to 1e-3 relative; radial relative acceleration +2 (apart), transverse -1 (together). Entry sizes 2, -1, -1 for both tides and rings confirmed.
- Entry still-water setting: Ricci diagonal 1,1,1,1 (each 4πGρ/c²), grand total 2 (8πGρ/c²), Einstein diagonal 2,0,0,0, and all three rings short by equal amounts.: Hand: R_μν = κ(T_μν - ½Tg_μν) with T = -ρc² + 3p, p → 0. python3 numeric Riemann of the uniform-density interior Schwarzschild metric (M = 1, R* = 100) at r = 10, 30, 60. → Space planes K = 8πGρ/3c² each (all positive and equal: the slice is a piece of a 3-sphere), time-space planes K = -4πGρ/3c², G_tt/8πρ = 1.000, G_rr/8πρ = p/ρ = 0.003 to 0.005, Ricci diagonal within 1.5% of 4πGρ/c². Confirmed.
- Crumbs let go by a static observer show the tides of the static four-velocity just after release.: Geodesic deviation for the congruence of crumbs, whose tangent at release equals the static observer's u with zero relative velocity; the initial relative acceleration is -R^μ_νρσ u^ν ξ^ρ u^σ with that u. → Correct; the ball's overall fall is the geodesic motion of the centre, the drifts among the crumbs are the deviation. Wording kept.
- Bridge: the ring total of the Ricci scalar note is the Ricci scalar of space; the grand total is the Ricci scalar of spacetime; they agree inside still water but need not in general.: Ring total (sum of missing fractions) = R₃ s²/12 = (K12 + K23 + K31) s²/6 = G_nn s²/6 for a time-symmetric slice, by the Gauss equation 2G_nn = R₃ + K² - K_ijK^ij. Compared with R₄ = 8πG(ρ - 3p/c²)/c² + 4Λ. → In unit terms the ring total is G_00 = 8πGρ/c² (2 units) and the grand total is 8πG(ρ - 3p/c²)/c² (2 units at p → 0): they agree for still water. Radiation (p = ρc²/3) gives grand total 0 with ring total nonzero, so 'need not' is right. Digest of the Ricci scalar note confirms its entry scalar is 'one number at each spot of space' with three-ring-total = R s²/12. Wording accurate.
- Tank of water on Earth: wall rings still too long, so the still-water setting must be far from any planet.: python3: Earth GM/c²r³ = 1.72e-23 m⁻² per wall plane against water's 8πGρ/c² = 1.87e-23 m⁻² total, at most 0.62e-23 per plane. → Novice's numbers and rescoping confirmed.
- Earth ring number: a level ring one kilometre out falls short by less than a thousandth of an atom's width; upright rings are too long by half of that.: python3: shortfall = 2πs·(2GM/c²r³)·s²/6 with s = 1 km at r = 6371 km. → 3.6e-14 m = 0.00036 of 1e-10 m; walls 1.8e-14 m. True. But a string laid along the ground would read Earth's surface curvature, 2.6e-5 m, so the sentence 'on the ground' was rewritten to hold the string level and straight.
- G_00 = 8πGρ/c² + Λ from the Einstein equation, with ρc² the measured energy density; R_00 = 4πG(ρ + 3p/c²)/c² - Λ.: Contracted G_μν + Λg_μν = 8πG T_μν/c⁴ with u^μu^ν/c², u·u = -c², T_μν u^μ u^ν = ρc⁴ for a perfect fluid; traced for R = 4Λ - κT. → Equation and Ricci form correct. The prose wrote ρc² = T_μν u^μ u^ν, off by c²: fixed to T_μν u^μ u^ν/c², and the symbol table now gives ρ = T_μν u^μ u^ν/c⁴.
- FLRW frame components R_titi = -ä/(c²a), R_ijij = (ȧ²/c² + k)/a²; G_tt = 3H²/c² + 3k/a², G_xx = -2ä/(c²a) - (ȧ²/c² + k)/a²; Gauss equation with K_ij = ±Hh_ij supplies 6H².: python3 numeric Riemann for a = t^(2/3), k = 0 and a = 1 + 0.3t, k = +1; hand: K = 3H, K_ijK^ij = 3H². → All match to 1e-4; the k = 0 slice has R₃ = 0 while G_tt = 3H²/c². Confirmed.
- Numbers: H0 = 67.4 km/s/Mpc gives 3H0²/c² = 1.6e-52 m⁻², critical density 8.5e-27 kg/m³, about five hydrogen atoms per cubic metre; Λ = 3K for de Sitter.: python3 with Mpc = 3.0857e19 km. → H0 = 2.184e-18 s⁻¹, 1.5925e-52 m⁻², 8.533e-27 kg/m³, 5.1 atoms. Numeric fields 1.59e-52 with rel_tol 0.03 and 0.05 pass.
- Derivation plane-sums-from-the-definition and trace-reversal-inverts-itself; problems constant-curvature-einstein and dimension-facts.: Re-derived by hand: Ricci diagonal as η^cc R_caca, P_ac = K(e_a,e_c), R = 2ΣP, G^a_a = -Σ_{planes ∌ a} P, G_00 = -G^0_0; tr G = (1 - n/2)R; 3K g, 12K, -3K g, Λ = 3K; 2D Riemann one component; 3D Riemann formula contracted on a,c gives R_bd; n²(n²-1)/12 = 6 and 20. → All steps and answers correct, index placement and signs consistent with the course Riemann and sectional-curvature rows.
- Formal way: divergence identity, 2D vanishing, n ≥ 3 inversion, 3D Weyl = 0, Gauss equation sign-insensitivity, Einstein–Hilbert variation with GHY term, Lovelock's theorem, torsion caveat, 10 - 4 = 6 counting.: Checked against standard results; Lovelock 1971 and 1972 abstracts confirm the four-dimensional uniqueness statement. → Accurate. The Gauss equation is now marked as stated without proof in the prose, matching justified_by.
- References: Planck 2018 VI (A&A 641, A6, 2020); Park et al. 2017 (AJ 153, 121); Einstein 1915 (Sitzungsberichte 844–847, session 25 Nov 1915); Hilbert 1915 (Nachr. Göttingen 395–407, presented 20 Nov 1915, printed March 1916); Lovelock 1971 (JMP 12, 498) and 1972 (JMP 13, 874); Fourès-Bruhat 1952 (Acta Math. 88, 141–225); Bartnik and Isenberg 2004 (Chruściel and Friedrich eds, Birkhäuser, gr-qc/0405092); Schoen and Yau 1979 (CMP 65, 45–76); Witten 1981 (CMP 80, 381–402).: One web search per reference against ADS, publisher or arXiv records. → All ten confirmed and set verified: true; editors added to the Bartnik–Isenberg venue; Hilbert contribution scoped by presentation and printing dates.

**Counterexamples tried**

- Non-static case (flat expanding universe): rings at playground length while G_tt = 3H²/c². The entry sentences are scoped 'where nothing changes with time' and the simplifies field names the case; the working way and check flat-universe-not-zero work it. Survives.
- Spinning planet: the static slice of a rotating spacetime has K_ij ≠ 0, so rings miss G_nn by a term quadratic in the spin; for Earth this is far below the 3.6e-14 m shortfall. The way says 'does not spin'; the summary's 'nothing changes with time' is true to that accuracy. Survives.
- Still water with non-uniform density: K_rθ = 4πG(ρ - ρ̄/3)/c² can be negative near the surface of a centrally condensed star, so 'all three rings come out short' needs uniform density. A ball of water is uniform to the accuracy needed. Survives as scoped.
- Radiation (p = ρc²/3): Ricci diagonal 3,1,1,1, grand total zero, ring total nonzero; the try_it and the bridge sentence 'need not agree' cover it.
- Tank of water on Earth: walls still long by the planet's Weyl curvature; the novice's rescoping to a ball far from any planet is required and kept.
- Two dimensions: G ≡ 0; three dimensions: G = 0 forces flatness; both stated at the formal rung with proofs in the problem.
- Null vectors: G(k,k) = R(k,k) = trace-free Ricci on k, recorded in the notation trap.
- Cosmological constant alone (de Sitter): ρ = 0 but G_00 = Λ; the density gauge includes Λ and the entry glossary for Einstein's law names the tiny extra term.

**Fixes**

- Way what-an-observer-reads: energy density written as ρc² = T_μν u^μ u^ν/c², with the reason u·u = -c²; the density-gauge symbol table now defines ρ as T_μν u^μ u^ν/c⁴, the mass density.
- Way three-tides-and-three-rings: the Earth ring is drawn with the string held level and straight, not along the ground, so the measured shortfall is spacetime's 3.6e-14 m and not the ground's own 2.6e-5 m.
- Way the-object-in-n-dimensions: the Gauss equation is said to be stated without proof, matching its justified_by.
- Equation diagonal-plane-rule: K described as the sectional curvature of a plane spanned by two frame vectors, not of a 'coordinate plane', which the sectional-curvature note flags as a misconception.
- History hilbert-1915: contribution scoped with the presentation and printing dates; Bartnik–Isenberg venue names the editors; all ten references set verified after confirmation.

**Concerns**

- Entry explanations stand at 1096 words after the Earth-ring rewrite, inside the 10% review allowance; the balance pointer in the first way remains the first candidate for a cut.
- The summary says 'where nothing changes with time'; strictly the ring reading of G_nn needs a time-symmetric slice (no spin as well as no change). The way names a planet that does not spin and the spin correction is negligible for any planet, so the entry wording was kept.
- The extrinsic-curvature sign convention is still not fixed in course-conventions.md; the formal way uses only the sign-insensitive quadratic combination.
- Prerequisites differ from the registry (sectional-curvature added at working); sync_registry.py should apply this reviewed note. Four visuals remain proposals with sketches; the catalog is empty.

**Diff check** (2026-09-16, revision 4)

- A level, straight-string ring of radius 1 km at Earth's surface falls short of 2*pi*s by less than a thousandth of an atom's width; upright rings are long by half of that.: python3: K(theta,phi) = 2GM/c^2 R^3 for the static slice, shortfall pi K s^3/3; wall planes K = -GM/c^2 R^3; control with the ground's own curvature 1/R^2. → K = 3.43e-23 per m^2, shortfall 3.59e-14 m < 1e-13 m; wall excess 1.80e-14 m = half. A string along the ground would give 2.6e-5 m instead, so 'because the ground itself curves' is the correct reason; the level string sits 8 cm above the ground at 1 km, physically doable.
- rho = T_{mu nu} u^mu u^nu / c^4 and rho c^2 = T u u / c^2, with the c^2 from (u^0hat)^2 = c^2; G_00hat = 8 pi G rho / c^2 + Lambda; plane-rule symbol K spans two frame vectors.: Hand and python3: perfect fluid T = (rho + p/c^2) u u + p g with u.u = -c^2 gives T u u = rho c^4 (pressure cancels); contract the Einstein equation with u u / c^2, Lambda g u u / c^2 = -Lambda; G^a_a = -sum of K over planes not containing a re-derived from R_aa = eta_aa sum_b K(a,b) and R = 2 sum_pairs K, consistent with K(e_0,e_i) = -R_0i0i in the course sign. → All confirmed; T u u / c^4 = rho numerically for p != 0; the two working symbol meanings and the rewritten prose are consistent with each other, with the displayed equation and with course-conventions.md.
- Fix: None beyond the two novice wording rewrites, both re-checked as claims: unchanged physics.
