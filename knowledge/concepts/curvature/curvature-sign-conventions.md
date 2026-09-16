---
type: "concept"
schema_version: 2
id: "curvature-sign-conventions"
title: "Curvature sign conventions"
tagline: "Why careful writers give the same curving opposite signs, and how to check"
domain: "curvature"
tier: "core"
status: "physics-reviewed"
revision: 5
updated: "2026-09-13"
aliases: ["Riemann sign and index conventions", "curvature conventions"]
prerequisites: ["riemann-curvature-tensor", "ricci-tensor", "metric-signature-convention"]
leads_to: ["einstein-field-equations", "cosmological-constant", "geodesic-deviation-equation", "space-of-constant-curvature", "einstein-hilbert-action"]
visuals: ["three-sign-toggles-beside-a-ball", "falling-ring-of-crumbs"]
---

# Curvature sign conventions

*Why careful writers give the same curving opposite signs, and how to check*

`curvature-sign-conventions` · curvature · core · physics-reviewed (revision 5)

**Needs:** [[riemann-curvature-tensor]] (entry) · [[ricci-tensor]] (working) · [[metric-signature-convention]] (working)  
**Opens:** [[einstein-field-equations]] · [[cosmological-constant]] · [[geodesic-deviation-equation]] · [[space-of-constant-curvature]] · [[einstein-hilbert-action]]  
**Related:** [[ricci-scalar]] · [[curvature-of-the-two-sphere]] · [[relativistic-tidal-tensor]] · [[holonomy]] · [[raychaudhuri-equation]]  
**Visuals:** ★ [[three-sign-toggles-beside-a-ball]] · [[falling-ring-of-crumbs]]

> Carry an arrow around a loop on a ball, never letting it swing, and most loops bring it back turned. One writer records that turn with a plus sign, another with a minus sign. Neither is wrong, because which way counts as plus is a choice. Writers on gravity make several such choices. So before borrowing a formula, start by testing its signs on a ball, whose behaviour everyone agrees on. A ball reveals some of these choices, though not all.

## You will be able to

**Entry**
- Distinguish a change of sign convention, which flips one writer's record, from a change in the walk, which flips every writer's record. `objectives/distinguish-choice-from-change` ← `checks/two-tables-one-ball`, `problems/walk-it-the-other-way`
- Use walkers drawing together on a ball to find which way a stranger's table of curving numbers counts as plus, and predict the sign that table gives a saddle. `objectives/calibrate-with-a-ball` ← `checks/stranger-table-saddle`

**Working**
- Compute how the Christoffel symbols, the Riemann and Ricci tensors, the Ricci scalar and the Einstein equation change under each of the three sign switches. `objectives/track-each-switch` ← `checks/signature-flip-what-changes`
- Identify a source's three signs from its sphere value, its deviation equation and its four-velocity norm, and translate its formulas into course conventions. `objectives/identify-and-translate` ← `problems/identify-the-switches`, `checks/dust-reveals-signature`, `checks/lambda-term-other-signature`

**Formal**
- Prove how any curvature object scales under the three sign switches, and derive the Einstein equation in a general convention. `objectives/prove-factor-counting` ← `problems/einstein-equation-any-convention`, `checks/kretschmann-unchanged`
- State which signs of Lorentzian constant curvature depend on the convention and which do not. `objectives/state-lorentzian-curvature-signs` ← `checks/de-sitter-curvature-constant`

## Ways in

### 1. Two tables for one ball · entry · picture

*Can two careful writers give the same turn on a ball opposite signs, and both be right?*

**Recap:** The arrow test: press a cardboard arrow against the ground and walk a loop, a path that ends where it began. Never let the arrow swing to your left or right. On a flat floor it comes back matching its start. On a ball, most loops bring it back turned. The Riemann curvature tensor is a table kept at every place. It lists how an arrow comes back changed after a trip around a tiny loop there.

Ana and Ben stand side by side on a huge smooth ball. Together they walk one small loop with four corners, turning left at each corner. The four parts of the walk between corners are called stretches. Ana carries a cardboard arrow pressed against the ground and never lets it swing. At the start, the arrow points ahead, along their first stretch.

Back at the start, they turn to face along their first stretch again. Both of them see the same thing: the arrow now points a little to the left of that stretch.

Now each of them writes the turn down. Ana writes a turn toward the walker's left as a plus number. Ben writes a turn toward the walker's left as a minus number. So for this one loop, Ana writes plus 5 thousandths of a degree. Ben writes minus 5 thousandths of a degree.

Which of them made a mistake? Neither. Both watched the same arrow, and both recorded the same size of turn. They differ only in which way each of them chose to count as plus. Nothing about the arrow makes that choice for them, because left and right are equally good choices for plus.

A choice like this, about which way counts as plus, is called a sign convention. A sign convention changes how a result is written. It never changes what the arrow does.

Some things no sign convention can change. A loop on a flat floor brings the arrow back matching its start, so both of them write zero. A turn twice as big gets a number twice as big in both records.

The Riemann curvature tensor lists turns like these for tiny loops. So one writer's table for a ball can hold plus numbers where another writer's table holds minus numbers. Both tables can describe the same ball correctly.

Writers on gravity make several sign choices of this kind. So a formula borrowed from another writer can carry the opposite sign to the one you would write, even when that writer made no mistake.

**Takeaway:** Which way counts as plus is a choice, so two careful writers can record the same turn of the same arrow with opposite signs, and both be right.

*Picture:* Two notebooks beside one ball. Each shows the same loop and the same returned arrow, with plus 5 thousandths of a degree in one notebook and minus 5 thousandths in the other.

*Builds on:* [[riemann-curvature-tensor]]<br>*See:* `checks/two-tables-one-ball`

### 2. Test the signs on a ball · entry · operational

*How can you tell which way a stranger's table of curving counts as plus?*

**Recap:** A sign convention is a choice about which way counts as plus. It changes how a result is written, never what happens. The Riemann curvature tensor is a table kept at every place, listing how an arrow comes back changed after a trip around a tiny loop there. For a surface, one number at each spot is enough to describe the curving there: the turn divided by the loop's area. A round ball curves the same everywhere, so one number covers the whole of it. Different writers can give that number opposite signs for the same surface.

You find a table of curving numbers for surfaces, made by a stranger. It does not say which way its writer counts as plus. To find out, test the table on a surface whose curving you can measure yourself.

Here is a measurement anyone can make. Two people stand side by side, a short gap apart, facing the same way. Both walk ahead the same distance, never steering left or right. Walking without ever steering is called walking straight. Then they measure the gap between them.

On a flat floor, the gap stays the same. On a ball, the gap shrinks: the two walkers draw together. The gap goes on shrinking at least until they have walked a quarter of the way around the ball. For example, two walkers who leave the equator side by side, both walking straight toward the North Pole, meet there, as any globe shows.

A saddle is shaped differently from a ball. Wherever you stand on a ball, the ground falls away from you in every direction. Stand at the middle of a horse's saddle, facing along the horse. The saddle rises ahead of you and behind you, but falls away to your left and right. On a saddle, the gap between two walkers grows: they spread apart, whichever way they set off from the middle. This course takes that fact on trust here.

These results do not depend on anyone's sign convention. A gap that shrinks is shrinking for everybody. So this course makes one choice: curving that makes the gap shrink, like a ball's, gets a plus number. Testing a table on a surface whose behaviour everyone agrees on is called calibrating the table.

This choice agrees with Ana's way of counting in "Two tables for one ball". She counts a turn toward the walker's left as plus. Ana and Ben turned left at every corner, so the small piece of ground their loop went round stayed on their left. Their arrow came back turned toward their left. On a ball, any small loop walked that way brings the arrow back turned toward the walker's left. A ball also makes the gap between two walkers shrink. So on a ball the leftward turn and the shrinking gap come together, and both get a plus number here.

Now look up a ball in the stranger's table. If the table gives a ball a plus number, its writer counts like this course. If the table gives a ball a minus number, its writer counts the other way. In that case, flip the sign of every number in that table before you use it.

A saddle makes the gap grow, the opposite of a ball. So in any one writer's table, a saddle's number has the opposite sign to a ball's. This means a minus sign alone never tells you that a surface is shaped like a saddle. First find what that writer gives a ball.

There is more than one kind of curving number, and a writer keeps a table for each kind. Each of those tables needs its own test on a ball. Tables that describe space and time together involve further sign choices, and a ball cannot test all of them.

On Earth, two walkers who leave the equator 1 kilometre apart and walk 100 kilometres toward the North Pole end up only about 12 centimetres closer. That is why nobody notices the shrinking on an ordinary walk.

**Try it:** Take a round orange and two rubber bands. Stretch each band once around the orange, passing over the stalk and over the spot opposite the stalk. A tight band takes the shortest way around, and on a ball the shortest way never steers left or right. Halfway between the stalk and the opposite spot, slide the bands until they lie side by side, 1 centimetre apart. Now follow the two bands toward the stalk. The gap between them shrinks, and the bands meet at the stalk.

**Takeaway:** Measure something everyone agrees on, such as walkers drawing together on a ball, and find which sign the stranger's table gives a ball. In that same table, a saddle gets the other sign.

*What this leaves out:* For space and time together, writers make more than one sign choice, and a ball can reveal only some of them.

*Continues:* `ways_in/two-tables-one-ball`<br>*Builds on:* [[riemann-curvature-tensor]]<br>*Visuals:* [[three-sign-toggles-beside-a-ball]]<br>*See:* `checks/stranger-table-saddle`

### 3. What each switch flips · working · calculation

*Which curvature quantities change sign under each of the three convention choices, and why?*

Ana and Ben in "Two tables for one ball" made one sign choice about the same arrow's turn. Gravity involves three independent choices, and the course fixes all of them:

- signature $(-,+,+,+)$;
- $R^\rho{}_{\sigma\mu\nu} = \partial_\mu\Gamma^\rho{}_{\nu\sigma} - \partial_\nu\Gamma^\rho{}_{\mu\sigma} + \Gamma^\rho{}_{\mu\lambda}\Gamma^\lambda{}_{\nu\sigma} - \Gamma^\rho{}_{\nu\lambda}\Gamma^\lambda{}_{\mu\sigma}$, so that $[\nabla_\mu,\nabla_\nu]V^\rho = R^\rho{}_{\sigma\mu\nu}V^\sigma$;
- $R_{\mu\nu} = R^\rho{}_{\mu\rho\nu}$, the upper index traced against the third slot.

Describe any other source by three signs relative to the course. Its metric is $\tilde g_{\mu\nu} = s_g\,g_{\mu\nu}$. Its Riemann tensor is $s_R$ times the course expression built from its own Christoffel symbols. Its Ricci tensor traces the upper index against the third slot, $s_{\rm Ric} = +1$, or the fourth, $s_{\rm Ric} = -1$; antisymmetry in the last pair gives $R^\rho{}_{\mu\nu\rho} = -R^\rho{}_{\mu\rho\nu}$. A tilde marks the source's quantities.

Follow each switch. A Christoffel symbol contains one inverse metric and one derivative of the metric, so under $g \to -g$ both change sign and $\Gamma^\lambda{}_{\mu\nu}$ is unchanged. The tensor $R^\rho{}_{\sigma\mu\nu}$ is built from $\Gamma$ alone, so it carries only $s_R$. Every further factor of $g_{\mu\nu}$ or $g^{\mu\nu}$ brings one $s_g$. The derivation "Sign rules for the three switches" collects the results:

$$\tilde R_{\rho\sigma\mu\nu} = s_gs_R\,R_{\rho\sigma\mu\nu},\qquad \tilde R_{\mu\nu} = s_Rs_{\rm Ric}\,R_{\mu\nu},\qquad \tilde R = s_gs_Rs_{\rm Ric}\,R.$$

The Einstein tensor $\tilde G_{\mu\nu} = \tilde R_{\mu\nu} - \tfrac12\tilde R\,\tilde g_{\mu\nu}$ carries $s_Rs_{\rm Ric}$, because the two factors $s_g$ in its second term cancel. The stress-energy tensor with lower indices is the same array in every convention that gives matter a positive energy density. Taking the course Einstein equation on trust, the same law in the source reads

$$\tilde G_{\mu\nu} + s_gs_Rs_{\rm Ric}\,\Lambda\,\tilde g_{\mu\nu} = s_Rs_{\rm Ric}\,\frac{8\pi G}{c^4}\,T_{\mu\nu}.$$

The ball test of "Test the signs on a ball" becomes a calculation. Calibrate with a sphere of radius $a$, $ds^2 = a^2(d\theta^2 + \sin^2\theta\,d\phi^2)$. The course gives $R^\theta{}_{\phi\theta\phi} = \sin^2\theta$ and $R = +2/a^2$. This metric is positive definite for every writer, so the source finds $\tilde R = s_Rs_{\rm Ric}\,(2/a^2)$. The sphere tests the product of the Riemann and Ricci signs, and it cannot see the signature.

**Takeaway:** The signature flips objects with an odd number of metric factors, the Riemann sign flips anything linear in Riemann, and the Ricci slot flips Ricci and what is linear in it; a sphere sees only the last two together.

*What this leaves out:* Assumes the Levi-Civita connection and the loop-plane indices in the last two Riemann slots; a source with another slot layout needs an index permutation first.

*Continues:* `ways_in/two-tables-one-ball`, `ways_in/calibrate-on-a-ball`<br>*Builds on:* [[riemann-curvature-tensor]], [[ricci-tensor]], [[metric-signature-convention]]<br>*Visuals:* [[three-sign-toggles-beside-a-ball]]<br>*See:* `derivations/switch-rules`, `checks/signature-flip-what-changes`

### 4. Calibrate with tides and cosmic acceleration · working · operational

*Which measurements fix the Riemann sign and the signature, which a sphere cannot see?*

The walkers drawing together on a ball in "Test the signs on a ball" calibrate only the product $s_Rs_{\rm Ric}$, as "What each switch flips" found. Measurements fix the other two signs.

*The Riemann sign from tides.* Test masses falling freely near Earth, separated along the line to its centre, accelerate apart. A gravity gradiometer measures this. Outside a spherical mass the relative acceleration per unit separation is $2GM/r^3$, which is $3.08\times10^{-6}\ \mathrm{s^{-2}}$ at Earth's surface. The course deviation equation, taken on trust from the Riemann tensor,

$$\frac{D^2\xi^\mu}{d\tau^2} = -R^\mu{}_{\nu\rho\sigma}\,u^\nu\xi^\rho u^\sigma,$$

then requires the orthonormal component $R^{\hat r}{}_{\hat 0\hat r\hat 0} = -2GM/c^2r^3$. A source with $s_R = -1$ writes this equation, in the same slot order, with a plus sign and finds the component positive; it predicts the same drift apart. Compare slot orders before comparing signs: antisymmetry in the last pair turns $-R^\mu{}_{\nu\rho\sigma}u^\nu\xi^\rho u^\sigma$ into $+R^\mu{}_{\nu\sigma\rho}u^\nu\xi^\rho u^\sigma$ with no change of convention.

*The signature from a normalisation.* A four-velocity has $u_\mu u^\mu = -c^2$ in the course and $+c^2$ when $s_g = -1$. Among curvature quantities, those with an odd number of metric factors reveal it. For dust of density $\rho$, with $\Lambda$ neglected, the course gives $R = 8\pi G\rho/c^2$. The focusing term $R_{\mu\nu}u^\mu u^\nu = 4\pi G\rho$ carries only $s_Rs_{\rm Ric}$, so it is as blind to the signature as the sphere.

*The cosmological constant.* Supernova distances and the cosmic microwave background show that the expansion of the universe is speeding up. In the standard fit to the course Einstein equation this needs $\Lambda \approx 1.1\times10^{-52}\ \mathrm{m^{-2}}$, positive. A source with $s_g = -1$ and the course Riemann and Ricci signs writes $G_{\mu\nu} - \Lambda g_{\mu\nu} = 8\pi GT_{\mu\nu}/c^4$ for the same positive, accelerating $\Lambda$.

Three readings therefore identify a source: its sphere value gives $s_Rs_{\rm Ric}$, its slot-aligned deviation equation gives $s_R$, and its $u_\mu u^\mu$ gives $s_g$.

**Takeaway:** Tides fix the Riemann sign, a four-velocity's norm fixes the signature, and the sphere then fixes the Ricci slot; the measured drifts and acceleration are the same in every convention.

*What this leaves out:* Uses the weak static field outside a spherical mass for the tidal value, and assumes every source gives matter a positive energy density.

*Continues:* `ways_in/calibrate-on-a-ball`, `ways_in/what-each-switch-flips`<br>*Builds on:* [[ricci-tensor]], [[metric-signature-convention]]<br>*Visuals:* [[falling-ring-of-crumbs]]<br>*See:* `worked_examples/earth-tide-three-conventions`, `observations/goce-radial-gradient`, `observations/accelerating-expansion`, `problems/identify-the-switches`

### 5. Conventions as three sign flips · formal · structure

*What exactly does a change of curvature convention do to every tensor, and what can it never change?*

The sign rules of "What each switch flips" follow from one counting argument about metric factors. Set $G = c = 1$. Let $(M, g)$ be a spacetime with Levi-Civita connection $\nabla$ and course curvature operator $\mathcal R(X,Y) = [\nabla_X,\nabla_Y] - \nabla_{[X,Y]}$. A convention is a triple $(s_g, s_R, s_{\rm Ric}) \in \{\pm1\}^3$. It uses the metric $\tilde g = s_g\,g$, the curvature operator $\tilde{\mathcal R} = s_R\,\mathcal R_{\tilde g}$, and $\widetilde{\mathrm{Ric}}(Y,Z) = s_{\rm Ric}\operatorname{tr}\big(X \mapsto \tilde{\mathcal R}(X,Z)Y\big)$.

*Lemma.* The metrics $\tilde g$ and $g$ have the same Levi-Civita connection. The Koszul formula expresses $2g(\nabla_XY, Z)$ through terms linear in $g$, so replacing $g$ by $s_g g$ multiplies both sides by $s_g$. Hence $\tilde{\mathcal R} = s_R\,\mathcal R$ as a $(1,3)$ tensor.

*Proposition.* Let $Q$ be built from $\mathcal R$ by $k$ metric factors, counting every raising, lowering or multiplication by $g_{ab}$ or $g^{ab}$, and by $m$ Ricci traces, plus metric-free operations. Then $\tilde Q = s_R\,s_g^k\,s_{\rm Ric}^m\,Q$. A product of such objects multiplies their signs, and a sum of terms that all carry one sign carries that sign, which is how $G_{ab}$ is covered. Each operation is linear in the one factor it adds, and $\tilde g^{-1} = s_g\,g^{-1}$, so raising and lowering both contribute $s_g$. Translations compose: the eight conventions form the group $\mathbb Z_2^3$, and translating from one source to another uses the componentwise product of their two triples, since each sign is its own inverse.

So $\tilde R_{abcd} = s_gs_RR_{abcd}$, $\widetilde{\mathrm{Ric}} = s_Rs_{\rm Ric}\mathrm{Ric}$, $\tilde R = s_gs_Rs_{\rm Ric}R$ and $\tilde G_{ab} = s_Rs_{\rm Ric}G_{ab}$. The quadratic invariants $R_{abcd}R^{abcd}$, $R_{ab}R^{ab}$ and $R^2$ are the same in all eight conventions. Sectional curvature $K(X,Y) = R(X,Y,X,Y)/\big(g(X,X)g(Y,Y) - g(X,Y)^2\big)$ has one metric factor in its numerator and two in its denominator, so $\tilde K = s_gs_RK$. The constant of a space of constant curvature, $R_{abcd} = K(g_{ac}g_{bd} - g_{ad}g_{bc})$, obeys the same rule.

*Physics fixes the rest.* An observer is the same vector $u^a$ in every convention, with $\tilde g(u,u) = -s_g$. Proper time is defined by $d\tau^2 = -s_g\,\tilde g(dx,dx)$, so $\tau$, the components $u^a$ and the deviation components $\xi^a$ are the same for everyone. The variational definition $T_{ab} = -2s_g(-\tilde g)^{-1/2}\,\delta S_{\rm m}/\delta\tilde g^{ab}$ keeps $T_{ab}u^au^b = \rho$; in four dimensions $\det\tilde g = \det g$. The source therefore writes $\tilde G_{ab} + s_gs_Rs_{\rm Ric}\Lambda\tilde g_{ab} = 8\pi s_Rs_{\rm Ric}T_{ab}$ and $D^2\xi^a/d\tau^2 = -s_R\tilde R^a{}_{bcd}u^b\xi^cu^d$. Relative accelerations, focusing, redshifts and those three quadratic invariants are convention-free.

*Limits.* The counting assumes the source's Riemann slots mean the same thing, with the loop plane last, and differ only by sign. Permuted slot layouts, and commutators written with antisymmetrizing brackets that carry a factor $\tfrac12$, must be translated first. With torsion, the order of the Christoffel indices becomes a further choice. In $n$ dimensions $\det\tilde g = s_g^n\det g$, so the equality of volume elements used above needs $n$ even; in odd dimensions write $\sqrt{|\det g|}$ explicitly. On a spacelike hypersurface with $s_g = -1$ the induced metric is negative definite, so its intrinsic scalar curvature carries $s_gs_Rs_{\rm Ric}$. A round spatial 3-sphere of radius $a$ then has scalar curvature $-6/a^2$ with the course Riemann and Ricci signs, and the sphere calibration of "What each switch flips" does not apply to it unchanged. Signs of actions, of Wick rotation, and of a source's tidal or Weyl tensors need the same care.

**Takeaway:** A convention is three signs; each object picks up the product of the signs of the metric factors, Riemann factors and Ricci traces it contains, while observables and the Kretschmann scalar never change.

*What this leaves out:* Restricted to the Levi-Civita connection and to conventions that differ from the course only by signs, not by slot layout or normalisation.

*Continues:* `ways_in/what-each-switch-flips`<br>*Builds on:* [[levi-civita-connection]]<br>*See:* `problems/einstein-equation-any-convention`, `checks/kretschmann-unchanged`, `checks/de-sitter-curvature-constant`

## Glossary

| Term | Say | In plain words | Concept |
| --- | --- | --- | --- |
| loop | — | A path that ends exactly where it began. | — |
| swing | — | To change which way the arrow points, left or right, while it lies against the ground. In the arrow test the arrow never swings. | — |
| stretch | — | One part of a walk from one corner to the next. | — |
| walk straight | — | To walk without ever steering left or right. On a ball, the equator and the lines from the North Pole to the equator are straight walks. | [[geodesic]] |
| sign convention | — | A choice about which way counts as plus when a result is written down. It changes how the result is written, never what happens. | [[curvature-sign-conventions]] |
| calibrate | — | To test a table or an instrument on a case whose result everyone agrees on, and so find out how it counts. | — |
| Riemann curvature tensor | REE-mahn | A table kept at every place that describes the curving there. For each tilt of a tiny loop and each starting direction of an arrow, it lists how the arrow comes back changed after a trip around the loop. | [[riemann-curvature-tensor]] |
| saddle | — | A surface shaped like the seat of a horse's saddle or a curved potato crisp. For someone standing at its middle and facing along the horse, it rises ahead and behind and falls away to the left and right. Walkers who set off side by side from its middle spread apart. | — |

## Key equations

### Course Riemann tensor · working

$$
R^\rho{}_{\sigma\mu\nu} = \partial_\mu\Gamma^\rho{}_{\nu\sigma} - \partial_\nu\Gamma^\rho{}_{\mu\sigma} + \Gamma^\rho{}_{\mu\lambda}\Gamma^\lambda{}_{\nu\sigma} - \Gamma^\rho{}_{\nu\lambda}\Gamma^\lambda{}_{\mu\sigma},\qquad [\nabla_\mu,\nabla_\nu]V^\rho = R^\rho{}_{\sigma\mu\nu}V^\sigma
$$

Fixes the overall Riemann sign: the commutator of covariant derivatives returns plus the Riemann tensor acting on the vector.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $\Gamma^\rho{}_{\mu\nu}$ | Christoffel symbols of the Levi-Civita connection | the Christoffel symbols |
| $R^\rho{}_{\sigma\mu\nu}$ | Riemann tensor, with the loop plane in the last two slots | the Riemann tensor |

**Holds when:** Torsion-free connection; course convention.  
**Say it:** “The commutator of two covariant derivatives on a vector equals plus the Riemann tensor acting on that vector.”  
**Justified by:** `riemann-curvature-tensor`

### Course Ricci tensor and scalar · working

$$
R_{\mu\nu} = R^\rho{}_{\mu\rho\nu},\qquad R = g^{\mu\nu}R_{\mu\nu}
$$

The upper Riemann index is traced against the third slot; the scalar needs one inverse metric.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $R_{\mu\nu}$ | Ricci tensor | R mu nu |
| $R$ | Ricci scalar | the Ricci scalar |

**Holds when:** Course convention; a sphere of radius $a$ has $R = +2/a^2$.  
**Say it:** “R mu nu is the Riemann tensor traced on its upper index and third slot, and R is its trace with the inverse metric.”  
**Justified by:** `ricci-tensor`

### Sign rules for the three switches · working

$$
\tilde R^\rho{}_{\sigma\mu\nu} = s_RR^\rho{}_{\sigma\mu\nu},\quad \tilde R_{\rho\sigma\mu\nu} = s_gs_RR_{\rho\sigma\mu\nu},\quad \tilde R_{\mu\nu} = s_Rs_{\rm Ric}R_{\mu\nu},\quad \tilde R = s_gs_Rs_{\rm Ric}R
$$

A source's curvature quantities, marked with a tilde, equal the course ones times the product of the switches each contains.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $s_g$ | $+1$ for signature $(-,+,+,+)$, $-1$ for $(+,-,-,-)$ | the signature sign |
| $s_R$ | overall sign of the source's Riemann tensor relative to the course | the Riemann sign |
| $s_{\rm Ric}$ | $+1$ if Ricci traces the third slot, $-1$ if the fourth | the Ricci slot sign |

**Holds when:** Levi-Civita connection; Riemann slots in the course order.  
**Say it:** “The source's mixed Riemann tensor carries the Riemann sign, the lowered one also the signature sign, Ricci the Riemann and slot signs, and the scalar all three.”  
**Justified by:** `derivations/switch-rules`

### Einstein equation in any sign convention · working

$$
\tilde G_{\mu\nu} + s_gs_Rs_{\rm Ric}\,\Lambda\,\tilde g_{\mu\nu} = s_Rs_{\rm Ric}\,\frac{8\pi G}{c^4}\,T_{\mu\nu}
$$

The course law written with a source's signs; positive $\Lambda$ accelerates the expansion in every convention.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $\tilde G_{\mu\nu}$ | the source's Einstein tensor | the source's Einstein tensor |
| $T_{\mu\nu}$ | stress-energy tensor with lower indices, the same array in every convention | T mu nu |

**Holds when:** Every convention gives matter a positive energy density; with all three signs $+1$ it is the course equation.  
**Say it:** “G tilde plus the product of all three signs times Lambda g tilde equals the Riemann and slot signs times eight pi G over c to the fourth times T.”  
**Justified by:** `derivations/switch-rules`

### Sphere calibration · working

$$
\tilde R_{\rm sphere} = s_Rs_{\rm Ric}\,\frac{2}{a^2}
$$

A round sphere's Ricci scalar tests the product of the Riemann and Ricci signs and nothing else.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $a$ | radius of the sphere | the radius |

**Holds when:** Positive-definite metric $a^2(d\theta^2 + \sin^2\theta\,d\phi^2)$; blind to the signature.  
**Say it:** “The sphere's Ricci scalar is the Riemann sign times the slot sign times two over a squared.”  
**Justified by:** `derivations/switch-rules`

## Derivations

### Sign rules for the three switches · working

**Goal:** Find how a source with signs $(s_g, s_R, s_{\rm Ric})$ writes the Riemann, Ricci and Einstein tensors and the Einstein equation.

1. The source metric is $\tilde g_{\mu\nu} = s_gg_{\mu\nu}$, so its inverse is $\tilde g^{\mu\nu} = s_gg^{\mu\nu}$.
2. $\Gamma^\lambda{}_{\mu\nu} = \tfrac12g^{\lambda\sigma}(\partial_\mu g_{\sigma\nu} + \partial_\nu g_{\sigma\mu} - \partial_\sigma g_{\mu\nu})$ has one inverse metric and one metric derivative, so $\tilde\Gamma^\lambda{}_{\mu\nu} = s_g^2\,\Gamma^\lambda{}_{\mu\nu} = \Gamma^\lambda{}_{\mu\nu}$.
3. The source builds its Riemann tensor from these same symbols with overall sign $s_R$: $\tilde R^\rho{}_{\sigma\mu\nu} = s_RR^\rho{}_{\sigma\mu\nu}$.
4. Lower with the source metric: $\tilde R_{\rho\sigma\mu\nu} = \tilde g_{\rho\lambda}\tilde R^\lambda{}_{\sigma\mu\nu} = s_gs_RR_{\rho\sigma\mu\nu}$.
5. Trace: with $s_{\rm Ric} = -1$ the source uses $\tilde R^\rho{}_{\mu\nu\rho} = -\tilde R^\rho{}_{\mu\rho\nu}$, by antisymmetry in the last pair. In both cases $\tilde R_{\mu\nu} = s_Rs_{\rm Ric}R_{\mu\nu}$.
6. Trace again: $\tilde R = \tilde g^{\mu\nu}\tilde R_{\mu\nu} = s_gs_Rs_{\rm Ric}R$.
7. Combine: $\tilde G_{\mu\nu} = s_Rs_{\rm Ric}R_{\mu\nu} - \tfrac12(s_gs_Rs_{\rm Ric}R)(s_gg_{\mu\nu}) = s_Rs_{\rm Ric}G_{\mu\nu}$.
8. $T_{\mu\nu}$ is the same array in every convention that gives matter a positive energy density. Substitute $G_{\mu\nu} = s_Rs_{\rm Ric}\tilde G_{\mu\nu}$ and $g_{\mu\nu} = s_g\tilde g_{\mu\nu}$ into the course equation $G_{\mu\nu} + \Lambda g_{\mu\nu} = 8\pi GT_{\mu\nu}/c^4$, taken on trust, and multiply by $s_Rs_{\rm Ric}$.
9. A sphere's metric is positive definite for every writer, so no $s_g$ enters, and the course value $2/a^2$ becomes $s_Rs_{\rm Ric}\,(2/a^2)$.

**Result:** $\tilde R_{\rho\sigma\mu\nu} = s_gs_RR_{\rho\sigma\mu\nu}$, $\tilde R_{\mu\nu} = s_Rs_{\rm Ric}R_{\mu\nu}$, $\tilde R = s_gs_Rs_{\rm Ric}R$, and $\tilde G_{\mu\nu} + s_gs_Rs_{\rm Ric}\Lambda\tilde g_{\mu\nu} = s_Rs_{\rm Ric}(8\pi G/c^4)T_{\mu\nu}$; a sphere gives $s_Rs_{\rm Ric}\,(2/a^2)$.

## Worked examples

### Earth's tide in three conventions · working

**Problem:** At Earth's surface take $r = 6371$ km and $GM = 3.986\times10^{14}\ \mathrm{m^3\,s^{-2}}$. Two test masses 1 m apart along the line to Earth's centre fall freely, at rest relative to each other. Find their relative acceleration and the components $R^{\hat r}{}_{\hat 0\hat r\hat 0}$ and $R_{\hat r\hat 0\hat r\hat 0}$ in the course, in a source with $s_R = -1$, and in a source with $s_g = -1$.

1. Newtonian tides give a relative acceleration along the radius of $2GM/r^3$ per unit separation, apart: $2(3.986\times10^{14})/(6.371\times10^{6})^3 = 3.08\times10^{-6}\ \mathrm{s^{-2}}$, so $3.08\times10^{-6}\ \mathrm{m\,s^{-2}}$ for 1 m.
2. In the masses' orthonormal frame $u^\mu = c\,\delta^\mu{}_{\hat 0}$, so the course deviation equation reads $\ddot\xi^{\hat r} = -c^2R^{\hat r}{}_{\hat 0\hat r\hat 0}\,\xi^{\hat r}$.
3. Match: $R^{\hat r}{}_{\hat 0\hat r\hat 0} = -2GM/c^2r^3 = -3.08\times10^{-6}/(2.998\times10^8)^2 = -3.43\times10^{-23}\ \mathrm{m^{-2}}$. Lowering with $g_{\hat r\hat r} = +1$ gives the same $R_{\hat r\hat 0\hat r\hat 0}$.
4. A source with $s_R = -1$ has $\tilde R^{\hat r}{}_{\hat 0\hat r\hat 0} = \tilde R_{\hat r\hat 0\hat r\hat 0} = +3.43\times10^{-23}\ \mathrm{m^{-2}}$, and its deviation equation carries a plus sign.
5. A source with $s_g = -1$ keeps $\tilde R^{\hat r}{}_{\hat 0\hat r\hat 0} = -3.43\times10^{-23}\ \mathrm{m^{-2}}$, but $\tilde g_{\hat r\hat r} = -1$ makes $\tilde R_{\hat r\hat 0\hat r\hat 0} = +3.43\times10^{-23}\ \mathrm{m^{-2}}$.

**Answer:** The masses accelerate apart at $3.08\times10^{-6}\ \mathrm{m\,s^{-2}}$ in every convention. Course: both components $-3.43\times10^{-23}\ \mathrm{m^{-2}}$. With $s_R = -1$: both $+3.43\times10^{-23}\ \mathrm{m^{-2}}$. With $s_g = -1$: mixed $-3.43\times10^{-23}\ \mathrm{m^{-2}}$, lowered $+3.43\times10^{-23}\ \mathrm{m^{-2}}$.

**Takeaway:** One measured drift, three printed signs: the Riemann sign flips both components, while the signature flips only the lowered one.

## Problems

### `walk-it-the-other-way` · entry · difficulty 1 · conceptual

On a huge smooth ball, Ana and Ben walk a small loop together, turning left at every corner. Ana's cardboard arrow first points along their first stretch and never swings. Back at the start, facing along that stretch again, they find the arrow turned a little to their left. Ana writes plus 4 thousandths of a degree, and Ben writes minus 4 thousandths. Next they walk the same loop the other way round, turning right at every corner, with the arrow again pointing along their new first stretch. Back at the start, facing along that stretch, they find the arrow turned to their right by the same amount. What does each of them write now? Which flipped both records: walking the other way, or their different ways of counting? Finally, suppose Ben switched to Ana's way of counting. Whose record of the first walk would change?

**Hints**

1. Ana counts a turn toward the walker's left as plus. Which way did the arrow turn this time?
2. Did the arrow do something different, or did only the writing change?

**Answer:** Ana writes minus 4 thousandths of a degree, and Ben writes plus 4 thousandths. Walking the other way changed what the arrow did, so it flipped both records. Their different ways of counting only make their two records opposite to each other. If Ben switched to Ana's way of counting, only his record of the first walk would change: he would write plus 4 thousandths, as Ana does.

**Must contain:** Ana writes minus 4 thousandths and Ben writes plus 4 thousandths; Walking the other way changes what the arrow does, so both records flip; Switching one writer's way of counting changes only that writer's record, because the arrow did the same thing

**Numeric:** Ana's record of the second turn = -0.004 deg (signed, ±0.0005, mod 360); Ben's record of the second turn = 0.004 deg (signed, ±0.0005, mod 360)

**Solution**

1. The arrow came back turned toward the walkers' right. Ana counts a turn toward the walker's left as plus, so she writes minus 4 thousandths of a degree.
2. Ben counts a turn toward the walker's left as minus, so a turn toward the right is plus for him. He writes plus 4 thousandths of a degree.
3. Both records flipped because the arrow really did something different. Ana and Ben still disagree in sign, because their sign conventions differ, yet they agree about what the arrow did.
4. For the first walk the arrow turned to the left. If Ben counted like Ana, a turn to the left would be plus for him, so his record would change from minus 4 to plus 4 thousandths. Ana's record would not change, because neither the arrow nor her counting changed.

**Targets:** `opposite-sign-means-mistake`

### `identify-the-switches` · working · difficulty 2 · calculation

A paper never states its conventions, but it gives three results. A sphere of radius $a$ has Ricci scalar $-2/a^2$. The geodesic deviation equation reads $D^2\xi^\mu/d\tau^2 = +R^\mu{}_{\nu\rho\sigma}u^\nu\xi^\rho u^\sigma$, with the Riemann slots in the course order. A four-velocity obeys $u_\mu u^\mu = +c^2$. Find $s_g$, $s_R$ and $s_{\rm Ric}$, and write the paper's Einstein equation with $\Lambda$.

**Hints**

1. Which of the three results contains no curvature at all?
2. The course deviation equation has a minus sign with the same slot order.

**Answer:** $s_g = -1$, $s_R = -1$ and $s_{\rm Ric} = +1$, so the paper writes $G_{\mu\nu} + \Lambda g_{\mu\nu} = -8\pi GT_{\mu\nu}/c^4$.

**Must contain:** The positive four-velocity norm gives a signature sign of minus one; The plus sign in the slot-aligned deviation equation gives a Riemann sign of minus one; The negative sphere value makes the product of Riemann and slot signs minus one, so the slot sign is plus one; The paper writes G plus Lambda g equals minus 8 pi G T over c to the fourth

**Solution**

1. $u_\mu u^\mu = +c^2$ contains one metric factor and no curvature, so $s_g = -1$.
2. In the course slot order a source writes $D^2\xi^\mu/d\tau^2 = -s_R\tilde R^\mu{}_{\nu\rho\sigma}u^\nu\xi^\rho u^\sigma$, so a plus sign means $s_R = -1$.
3. The sphere is positive definite, so $\tilde R = s_Rs_{\rm Ric}(2/a^2) = -2/a^2$ gives $s_Rs_{\rm Ric} = -1$ and $s_{\rm Ric} = +1$.
4. Then $s_gs_Rs_{\rm Ric} = +1$ and $s_Rs_{\rm Ric} = -1$, so the paper writes $\tilde G_{\mu\nu} + \Lambda\tilde g_{\mu\nu} = -(8\pi G/c^4)T_{\mu\nu}$.
5. Check with dust and $\Lambda = 0$: tracing with $\tilde g^{\mu\nu}$ gives $-\tilde R = -(8\pi G/c^4)\tilde T$, with $\tilde T = \tilde g^{\mu\nu}T_{\mu\nu} = +\rho c^2$. So $\tilde R = +8\pi G\rho/c^2$, which is $s_gs_Rs_{\rm Ric}$ times the course value, as the sign rules require.

### `einstein-equation-any-convention` · formal · difficulty 2 · derivation

With $G = c = 1$, use the factor-counting proposition to show that a convention $(s_g, s_R, s_{\rm Ric})$ writes the Einstein equation as $\tilde G_{ab} + s_gs_Rs_{\rm Ric}\Lambda\tilde g_{ab} = 8\pi s_Rs_{\rm Ric}T_{ab}$. Show that for a perfect fluid at rest, with density $\rho$ and pressure $p$, it gives $\widetilde{\mathrm{Ric}}(u,u) = s_Rs_{\rm Ric}\big[4\pi(\rho + 3p) - \Lambda\big]$. Explain why a small ball of dust, released at rest, starts to change its volume at the same rate in every convention.

**Hints**

1. Count the metric factors and Ricci traces in each term of $G_{ab}$.
2. Trace-reverse the course equation first; $\mathrm{Ric}(u,u)$ contains no metric factor.

**Answer:** The stated Einstein equation follows from $\tilde G_{ab} = s_Rs_{\rm Ric}G_{ab}$ and $\tilde g_{ab} = s_gg_{ab}$. The course gives $\mathrm{Ric}(u,u) = 4\pi(\rho + 3p) - \Lambda$, and the source's value carries $s_Rs_{\rm Ric}$. The source's volume law carries the same factor, so the initial volume acceleration $\ddot{\delta V}/\delta V = -4\pi(\rho + 3p) + \Lambda$ is convention-free.

**Must contain:** The Einstein tensor carries only the Riemann and slot signs because its two metric factors cancel; The course fluid value is four pi times density plus three pressure, minus Lambda; The same four-velocity components and the same lower-index stress tensor appear in every convention; The volume law carries the same product of signs, so the initial rate of volume change is unchanged

**Solution**

1. By the proposition, $\tilde R_{ab} = s_Rs_{\rm Ric}R_{ab}$ has one trace and no metric factor, while $\tilde R\,\tilde g_{ab}$ has one trace and two metric factors. So $\tilde G_{ab} = s_Rs_{\rm Ric}G_{ab}$.
2. Substitute $G_{ab} = s_Rs_{\rm Ric}\tilde G_{ab}$ and $g_{ab} = s_g\tilde g_{ab}$ into $G_{ab} + \Lambda g_{ab} = 8\pi T_{ab}$ and multiply by $s_Rs_{\rm Ric}$.
3. Trace-reverse the course equation: $R_{ab} = 8\pi\big(T_{ab} - \tfrac12Tg_{ab}\big) + \Lambda g_{ab}$.
4. For a perfect fluid at rest, $T_{ab}u^au^b = \rho$, $T = -\rho + 3p$ and $g(u,u) = -1$. So $\mathrm{Ric}(u,u) = 8\pi\big(\rho + \tfrac12(-\rho + 3p)\big) - \Lambda = 4\pi(\rho + 3p) - \Lambda$.
5. $\mathrm{Ric}(u,u)$ has one trace and no metric factor, and $u^a$ is the same vector in every convention, so $\widetilde{\mathrm{Ric}}(u,u) = s_Rs_{\rm Ric}\big[4\pi(\rho + 3p) - \Lambda\big]$.
6. The course volume law $\ddot{\delta V}/\delta V = -\mathrm{Ric}(u,u)$ reads $-s_Rs_{\rm Ric}\widetilde{\mathrm{Ric}}(u,u)$ in the source. Both equal $-4\pi(\rho + 3p) + \Lambda$, so the dust ball starts to change its volume at the same rate: it shrinks when $4\pi(\rho + 3p) > \Lambda$ and grows when $\Lambda$ is larger.

## Observations

- **Gravity gradients above Earth measured by the GOCE satellite** (measured, working). From 2009 to 2013 GOCE's gradiometer measured differences in free-fall acceleration across the satellite. With its rotation removed, test masses separated along the line to Earth's centre accelerate apart. That measured sign is convention-free: it requires $R^{\hat r}{}_{\hat 0\hat r\hat 0} < 0$ in the course and a positive value in any source with the opposite Riemann sign. Physical geodesy usually takes the potential as $V = +GM/r$, so it quotes this gradient with the opposite sign to $\partial_r^2\Phi$, one more convention to translate. *Numbers:* At $r = 6626$ km for a spherical Earth: relative acceleration $2GM/r^3 = 2.74\times10^{-6}\ \mathrm{s^{-2}}$ per unit separation, apart, so $R^{\hat r}{}_{\hat 0\hat r\hat 0} = -3.05\times10^{-23}\ \mathrm{m^{-2}}$ in the course. *Reference:* Reiner Rummel, Weiyong Yi, Claudia Stummer (2011), *GOCE gravitational gradiometry*, Journal of Geodesy 85, 777–790, doi:10.1007/s00190-011-0500-0
- **The accelerating expansion of the universe** (measured, working). Supernova distances and the cosmic microwave background show that the expansion speeds up today, which the course Einstein equation fits with a positive cosmological constant. The measured $\Lambda$ is positive in every convention: a source with signature $(+,-,-,-)$ and the course Riemann and Ricci signs writes the term as $-\Lambda g_{\mu\nu}$ for the same accelerating universe. *Numbers:* With $H_0 = 67.4\ \mathrm{km\,s^{-1}\,Mpc^{-1}}$ and $\Omega_\Lambda = 0.685$: $\Lambda = 3\Omega_\Lambda H_0^2/c^2 = 1.09\times10^{-52}\ \mathrm{m^{-2}}$. *Reference:* N. Aghanim, Y. Akrami, M. Ashdown, J. Aumont and others (2020), *Planck 2018 results. VI. Cosmological parameters*, Astronomy & Astrophysics 641, A6, doi:10.1051/0004-6361/201833910

## Teaching arc

1. **Two records of one turn** (entry). After a prediction, show Ana's and Ben's opposite records of the same loop, then the flat floor where both write zero. *Why:* It separates what happens from how it is written before any formula appears. *Predict:* Ana writes plus five thousandths of a degree and Ben writes minus five thousandths for the same loop. Has one of them made a mistake? *Uses:* `ways_in/two-tables-one-ball`, `checks/two-tables-one-ball`
2. **Calibrate a stranger's table** (entry). Have the learner look up a ball in a stranger's table, then predict the sign it gives a saddle. *Why:* Calibration turns a sign from something memorised into something checked. *Predict:* A stranger's table gives a ball a minus number. What sign does it give a saddle? *Visual:* [[three-sign-toggles-beside-a-ball]] *Uses:* `ways_in/calibrate-on-a-ball`, `checks/stranger-table-saddle`
3. **Flip each switch** (working). Derive the sign rules by counting metric factors, then use the sphere to calibrate the Riemann and Ricci signs together. *Why:* One counting argument replaces a memorised translation table. *Predict:* If you flip the signature, do the Christoffel symbols change? *Visual:* [[three-sign-toggles-beside-a-ball]] *Uses:* `ways_in/what-each-switch-flips`, `derivations/switch-rules`, `checks/signature-flip-what-changes`
4. **Identify a source** (working). Use a four-velocity norm, a slot-aligned deviation equation and a sphere to find a paper's three signs, then check with dust. *Why:* Identifying and translating conventions is the skill used when reading other work. *Predict:* Your sphere check comes out positive. Does that prove the paper uses the course signature? *Uses:* `ways_in/calibrate-with-tides-and-the-cosmos`, `problems/identify-the-switches`, `checks/dust-reveals-signature`
5. **Count factors and mark the limits** (formal). Prove the factor-counting proposition, apply it to the Kretschmann scalar and de Sitter space, then state what it cannot translate. *Why:* It shows which curvature statements are physics and which are bookkeeping. *Predict:* Under which of the three switches does the Kretschmann scalar change sign? *Uses:* `ways_in/conventions-as-sign-flips`, `checks/kretschmann-unchanged`, `checks/de-sitter-curvature-constant`

## Misconceptions

### “If two writers give the same ball opposite signs, one of them has made a mistake.” · entry · `opposite-sign-means-mistake`

- **Why it is tempting:** Each writer presents their own sign as simply the sign.
- **What is true:** The sign records which way a writer counts as plus, a choice that changes the writing and not the arrow's turn. Both records describe the same turn.
- **Exposed by:** `checks/two-tables-one-ball`

### “A minus sign in a table of curving means the surface curves like a saddle.” · entry · `minus-means-saddle`

- **Why it is tempting:** In this course, a saddle does get a minus number.
- **What is true:** A minus sign means saddle-like only once you know the writer gives a ball a plus number. In a table that counts the other way, a ball gets a minus number and a saddle gets a plus number.
- **Exposed by:** `checks/stranger-table-saddle`

### “Flipping the metric signature flips the sign of every curvature quantity.” · working · `signature-flips-everything`

- **Why it is tempting:** The signature feels like one overall minus sign on everything.
- **What is true:** The Christoffel symbols, the mixed Riemann tensor and the Ricci and Einstein tensors with lower indices keep their values. Only objects with an odd number of metric factors, such as the Ricci scalar and the lowered Riemann tensor, flip.
- **Exposed by:** `checks/signature-flip-what-changes`

### “If my sphere comes out with Ricci scalar plus two over a squared, all my conventions match the course.” · working · `sphere-check-is-complete`

- **Why it is tempting:** The sphere is the best-known convention test.
- **What is true:** A sphere's metric has no signature choice, so the test fixes only the product of the Riemann and Ricci signs. The signature needs a Lorentzian test, such as a four-velocity norm or the Ricci scalar of dust.
- **Exposed by:** `checks/dust-reveals-signature`

### “The sign in front of the cosmological term tells me whether that writer's cosmological constant speeds up or slows the expansion.” · working · `lambda-sign-sets-attraction`

- **Why it is tempting:** A minus sign looks like a physically different term.
- **What is true:** The written sign of that term is the product of all three convention signs. A positive cosmological constant speeds up the expansion in every convention.
- **Exposed by:** `checks/lambda-term-other-signature`

### “De Sitter space is positively curved, so its curvature constant and Ricci scalar are positive in every convention.” · formal · `de-sitter-positive-everywhere`

- **Why it is tempting:** De Sitter space is often described as the Lorentzian cousin of a sphere.
- **What is true:** Its curvature constant scales with the signature and Riemann signs, and its Ricci scalar with all three. For a Lorentzian space, positive curvature means something only in a stated convention.
- **Exposed by:** `checks/de-sitter-curvature-constant`

## Checks

1. **Entry · evaluate-claim** `checks/two-tables-one-ball`. On a huge smooth ball, Ana and Ben walk the same small loop together, turning left at every corner. Ana's cardboard arrow first points along their first stretch and never swings. Back at the start, facing along that stretch again, they find the arrow turned a little to their left. Ana writes the turn as plus 6 thousandths of a degree. Ben writes it as minus 6 thousandths. Ben says: 'Our numbers disagree, so one of us measured the turn wrong.' Is he right?
   - **Hints:** Did the arrow do something different for Ana than for Ben?
   - **Answer:** No. Both of them watched the same arrow come back turned toward their left, by 6 thousandths of a degree. Ana counts a turn toward the walker's left as plus. Ben counts a turn toward the walker's left as minus. So their numbers differ only because their sign conventions differ. The size and direction of the turn are the same for both, so neither measured it wrong.
   - **Must contain:** Ben is not right; Both records describe the same turn of the same size; The signs differ only because they count different ways as plus
   - **Targets:** `opposite-sign-means-mistake`
2. **Entry · predict** `checks/stranger-table-saddle`. You find a stranger's table of curving numbers for surfaces. For a ball, it gives a minus number. On a ball, walkers who set off side by side draw together, and on a saddle they spread apart. What sign does this table give a saddle? Does a minus sign in this table mean a surface is shaped like a saddle?
   - **Hints:** Which sign does this table give to walkers drawing together?
   - **Answer:** This table gives a saddle a plus number. A ball makes side-by-side walkers draw together, and the table gives that behaviour a minus number. A saddle makes them spread apart, the opposite behaviour, so the same table gives it the opposite sign, plus. So in this table a minus sign means curving like a ball's, not like a saddle's. The stranger counts the other way from this course.
   - **Must contain:** The saddle gets a plus number; A saddle behaves opposite to a ball, so the same table gives it the opposite sign; In this table a minus sign means curving like a ball's
   - **Targets:** `minus-means-saddle`
   - **Visual:** [[three-sign-toggles-beside-a-ball]]
3. **Working · explain** `checks/signature-flip-what-changes`. Replace $g_{\mu\nu}$ by $-g_{\mu\nu}$ while keeping the course Riemann formula and Ricci contraction. Which of these change sign: $\Gamma^\lambda{}_{\mu\nu}$, $R^\rho{}_{\sigma\mu\nu}$, $R_{\rho\sigma\mu\nu}$, $R_{\mu\nu}$, $R$, $G_{\mu\nu}$, and the trace $T = g^{\mu\nu}T_{\mu\nu}$?
   - **Hints:** How many factors of the metric or its inverse does each object contain?
   - **Answer:** Count metric factors. $\Gamma$ has one inverse metric and one metric derivative, so it is unchanged, and $R^\rho{}_{\sigma\mu\nu}$, built from $\Gamma$ alone, is unchanged. $R_{\mu\nu} = R^\rho{}_{\mu\rho\nu}$ needs no metric, so it is unchanged. $R_{\rho\sigma\mu\nu}$ has one lowering metric, and $R$ and $T$ each have one inverse metric, so these three flip. In $G_{\mu\nu} = R_{\mu\nu} - \tfrac12Rg_{\mu\nu}$, $R$ and $g_{\mu\nu}$ flip together, so $G_{\mu\nu}$ is unchanged.
   - **Must contain:** Christoffel symbols, the mixed Riemann tensor, the Ricci tensor and the Einstein tensor are unchanged; The lowered Riemann tensor, the Ricci scalar and the trace of T flip; An odd number of metric factors decides a flip
   - **Targets:** `signature-flips-everything`
4. **Working · numeric** `checks/dust-reveals-signature`. In a text, your sphere check gives $R = +2/a^2$. The text's four-velocities obey $u_\mu u^\mu = +c^2$, and it uses the course Riemann formula and Ricci contraction. For pressureless dust of density $1000\ \mathrm{kg\,m^{-3}}$ with $\Lambda = 0$, what Ricci scalar does the text find, and what focusing term $R_{\mu\nu}u^\mu u^\nu$?
   - **Hints:** Which of the three signs does a four-velocity norm reveal?
   - **Answer:** The positive norm means $s_g = -1$, while $s_R = s_{\rm Ric} = +1$; that is why the sphere passed, since it sees only $s_Rs_{\rm Ric}$. The course gives $R = 8\pi G\rho/c^2 = 1.87\times10^{-23}\ \mathrm{m^{-2}}$ for this dust, so the text finds $\tilde R = s_gs_Rs_{\rm Ric}R = -1.87\times10^{-23}\ \mathrm{m^{-2}}$. The focusing term carries only $s_Rs_{\rm Ric}$, so both find $4\pi G\rho = 8.39\times10^{-7}\ \mathrm{s^{-2}}$, and the dust starts to shrink in both.
   - **Must contain:** The positive four-velocity norm means the opposite signature; The text's Ricci scalar for the dust is minus 1.87e-23 per square metre; The focusing term is 8.39e-7 per second squared in both
   - **Numeric:** Ricci scalar of the dust in that text = -1.87e-23 m^-2 (signed, ±2%)
   - **Targets:** `sphere-check-is-complete`
5. **Working · evaluate-claim** `checks/lambda-term-other-signature`. A text with signature $(+,-,-,-)$ and the course Riemann and Ricci definitions writes $G_{\mu\nu} - \Lambda g_{\mu\nu} = 8\pi GT_{\mu\nu}/c^4$ with a positive $\Lambda$. A student says this text's cosmological constant slows the expansion, because its sign is the opposite of the course's. Evaluate the claim.
   - **Hints:** Which factors in each term change under the signature flip?
   - **Answer:** The claim is wrong. For this text $s_g = -1$ and $s_R = s_{\rm Ric} = +1$, so $\tilde G_{\mu\nu} = G_{\mu\nu}$ and $\tilde g_{\mu\nu} = -g_{\mu\nu}$. Substituting turns its equation into $G_{\mu\nu} + \Lambda g_{\mu\nu} = 8\pi GT_{\mu\nu}/c^4$, the course equation with the same positive $\Lambda$. The minus sign comes from the flipped metric, so $\Lambda$ speeds up the expansion in both.
   - **Must contain:** The claim is wrong; The Einstein tensor is unchanged by the signature while the metric flips; Translated, it is the course equation with the same positive Lambda, which speeds up the expansion
   - **Targets:** `lambda-sign-sets-attraction`
6. **Formal · derive** `checks/de-sitter-curvature-constant`. With $G = c = 1$, the course gives de Sitter space $R_{abcd} = K(g_{ac}g_{bd} - g_{ad}g_{bc})$ with $K = H^2 > 0$ and $R = 12H^2$. Find $\tilde K$ and $\tilde R$ in a convention $(s_g, s_R, s_{\rm Ric})$, and give both for signature $(+,-,-,-)$ with the course Riemann and Ricci signs. Which statements about de Sitter curvature are convention-free?
   - **Hints:** Count metric factors on each side of the constant-curvature form.
   - **Answer:** The lowered Riemann tensor carries $s_gs_R$, while the bracket $g_{ac}g_{bd} - g_{ad}g_{bc}$ has two metric factors and carries nothing, so $\tilde K = s_gs_RK$. The scalar carries all three signs, $\tilde R = s_gs_Rs_{\rm Ric}\,12H^2$. For $(+,-,-,-)$ with the course Riemann and Ricci signs, $\tilde K = -H^2$ and $\tilde R = -12H^2$. Convention-free are $\Lambda = 3H^2 > 0$, the Kretschmann scalar $24H^4$, and the fact that free particles at rest relative to each other accelerate apart.
   - **Must contain:** The curvature constant scales with the signature and Riemann signs; With the opposite signature K is minus H squared and R is minus 12 H squared; Lambda, the Kretschmann scalar and the separation of free particles do not depend on the convention
   - **Targets:** `de-sitter-positive-everywhere`
7. **Formal · numeric** `checks/kretschmann-unchanged`. Show that the Kretschmann scalar $\mathcal K = R_{abcd}R^{abcd}$ has the same value in all eight conventions $(s_g, s_R, s_{\rm Ric})$. A source with $s_g = s_R = -1$ quotes $\mathcal K = 48\,G^2M^2/c^4r^6$ outside a spherical mass. What value does the course give, in units of $G^2M^2/c^4r^6$?
   - **Hints:** How many metric factors does the fully raised Riemann tensor carry?
   - **Answer:** $R_{abcd}$ carries $s_gs_R$. $R^{abcd} = g^{be}g^{cf}g^{dh}R^a{}_{efh}$ has three inverse metrics and one Riemann factor, so it carries $s_g^3s_R = s_gs_R$. The product carries $(s_gs_R)^2 = 1$, and no Ricci trace appears, so $\mathcal K$ is the same in every convention. The course value is also $48\,G^2M^2/c^4r^6$, about $1.4\times10^{-44}\ \mathrm{m^{-4}}$ at Earth's surface.
   - **Must contain:** The lowered Riemann tensor carries the signature and Riemann signs; The raised Riemann tensor carries the same product; The square of that product is one, so the value is 48 in every convention
   - **Numeric:** Kretschmann scalar in units of G squared M squared over c to the fourth r to the sixth = 48 1 (signed, ±0.5)

## Notation traps

| Issue | Course choice | Variants you will meet |
| --- | --- | --- |
| Metric signature | $(-,+,+,+)$, $\eta_{\mu\nu} = \mathrm{diag}(-1,1,1,1)$, so $u_\mu u^\mu = -c^2$. | Some texts use $(+,-,-,-)$. The Christoffel symbols, $R^\rho{}_{\sigma\mu\nu}$, $R_{\mu\nu}$ and $G_{\mu\nu}$ keep their values, while $R_{\rho\sigma\mu\nu}$, $R$, the trace $T$ and the written sign of the $\Lambda$ term flip. |
| Overall sign and slot layout of the Riemann tensor | $[\nabla_\mu,\nabla_\nu]V^\rho = +R^\rho{}_{\sigma\mu\nu}V^\sigma$, with the loop plane in the last two slots. | Some texts reverse the overall sign, or put the loop-plane indices first. With the same Ricci slot, a reversed sign flips $R_{\mu\nu}$, $R$, the sign in front of $8\pi GT_{\mu\nu}$, the written sign of the $\Lambda$ term and the sign of the deviation equation. |
| Which Riemann slot is traced to form the Ricci tensor | $R_{\mu\nu} = R^\rho{}_{\mu\rho\nu}$, so a sphere of radius $a$ has $R = +2/a^2$. | Some texts trace the upper index against the fourth slot, which gives minus this tensor; together with a reversed Riemann sign the two flips cancel. |
| Visible sign of the geodesic deviation equation | $D^2\xi^\mu/d\tau^2 = -R^\mu{}_{\nu\rho\sigma}u^\nu\xi^\rho u^\sigma$. | Some texts put the separation in the fourth slot and write a plus sign with the same Riemann tensor. Align slots before comparing signs. |

## Visuals

- ★ [[three-sign-toggles-beside-a-ball]] (flagship): Separates how curvature is written from what happens: three sign toggles change printed formulas and values, while the scenes beside them never change. *Sketch:* Three toggles, for the signature, the Riemann sign and the Ricci slot, with presets for the course and for each single flip. Beside them sit fixed scenes: walkers drawing together on a ball, two falling test masses drifting apart above a planet, and galaxies accelerating apart. Readouts show the sphere's $R$, the tidal components $R^{\hat r}{}_{\hat 0\hat r\hat 0}$ and $R_{\hat r\hat 0\hat r\hat 0}$, the $R$ of dust, the focusing term, the written Einstein equation with $\Lambda$, and the Kretschmann scalar. A flip changes only the readouts whose sign product contains it. A mystery-paper mode asks the learner to set the toggles that reproduce three quoted results.
- [[falling-ring-of-crumbs]] (supporting): Tidal drift along the radius as the measured calibration of the Riemann sign. *Sketch:* This concept adds a convention toggle beside the ring: the printed radial tidal component changes sign with the Riemann sign, and its lowered form also with the signature, while the crumbs' drift never changes.

## Tutor moves

**Open with**

- Two careful people walk the same small loop on a huge ball, carrying an arrow that never swings. Back at the start, facing the way they first set off, they find the arrow turned a little toward their left. One writes the turn as plus five thousandths of a degree, the other as minus five thousandths. Has one of them made a mistake? *(prediction)*

**If the learner is stuck**

- *The learner treats walking the loop the other way and changing the counting rule as the same thing.* → Have the learner fill a small table with both writers' records for both walking directions, then ask which change flips both records at once and which difference flips only one. *Uses:* `problems/walk-it-the-other-way`
- *The learner loses track of which sign multiplies which quantity.* → Count metric factors and Ricci traces aloud for each object, one object at a time, before writing any sign. *Uses:* `derivations/switch-rules`, `checks/signature-flip-what-changes`

**Common questions**

- *Why don't scientists just agree on one sign?* (entry) Different groups settled on different habits long ago, each for reasons that suited their own work. Rewriting a century of results in one style would cost a great deal of effort. So careful writers state their choices instead, and readers check them on a case everyone agrees on, such as a ball. This course states its choices and tests them the same way. *Uses:* `ways_in/calibrate-on-a-ball`

**Switching levels**

- To working when: asks which formulas change; starts using indices or the metric. Go to the three switches and the sphere calibration. *Uses:* `ways_in/what-each-switch-flips`, `checks/signature-flip-what-changes`
- To formal when: asks for a proof that covers every object; asks about de Sitter space or invariants. Give the factor-counting proposition, then the Kretschmann and de Sitter checks. *Uses:* `ways_in/conventions-as-sign-flips`, `checks/de-sitter-curvature-constant`
- To research when: asks about Euclidean quantum gravity, Ricci flow or singularity theorems. Open the research horizon. *Uses:* `research_horizon/euclidean-quantum-gravity`, `research_horizon/focusing-theorems`

**Pronunciations:** Riemann → REE-mahn; Ricci → REE-chee; Christoffel → KRIS-toff-el; Kretschmann → KRETCH-mahn; de Sitter → duh SIT-er; Koszul → KOH-shool; Minkowski → min-KOFF-skee; GOCE → GO-chay; Raychaudhuri → ray-CHOWD-hoo-ree

**Voice notes:** At the entry rung say 'which way counts as plus', never 'the sign of the tensor'.

## History

- **Bernhard Riemann (1854).** In his 1854 habilitation lecture, published in 1868, extended Gauss's measure of curvature to spaces of any dimension, with a value for each two-dimensional direction at a point, and discussed spaces of constant positive curvature such as the sphere. Bernhard Riemann (1868), *Ueber die Hypothesen, welche der Geometrie zu Grunde liegen*, Abhandlungen der Königlichen Gesellschaft der Wissenschaften zu Göttingen 13, 133–150
- **Hermann Minkowski (1908).** Treated space and time as one four-dimensional geometry, using an imaginary time coordinate so that all four squares enter the interval with the same sign. A real time coordinate instead forces a choice between the two signatures. Hermann Minkowski (1908), *Die Grundgleichungen für die elektromagnetischen Vorgänge in bewegten Körpern*, Nachrichten von der Gesellschaft der Wissenschaften zu Göttingen, Mathematisch-Physikalische Klasse, 53–111
- **Albert Einstein (1917).** Added a term proportional to the metric, with the cosmological constant, to the field equations so that they allow a static closed universe. Albert Einstein (1917), *Kosmologische Betrachtungen zur allgemeinen Relativitätstheorie*, Sitzungsberichte der Königlich Preußischen Akademie der Wissenschaften (Berlin), 142–152

## Research horizon

- **Euclidean quantum gravity.** Rotating time to imaginary values turns signature $(-,+,+,+)$ into a positive-definite metric. With $G = c = 1$ and the course curvature signs, the Lorentzian action $\frac{1}{16\pi}\int(R - 2\Lambda)\sqrt{-g}\,d^4x$ becomes the Euclidean action $I = -\frac{1}{16\pi}\int(R - 2\Lambda)\sqrt{g}\,d^4x$ plus a boundary term, and the path integral weights geometries by $e^{-I}$. Conformal rescalings make this $I$ unbounded below, the conformal factor problem, so every overall sign in the construction must be tracked. G. W. Gibbons, S. W. Hawking (1977), *Action integrals and partition functions in quantum gravity*, Physical Review D 15, 2752–2756, doi:10.1103/PhysRevD.15.2752; G. W. Gibbons, S. W. Hawking, M. J. Perry (1978), *Path integrals and the indefiniteness of the gravitational action*, Nuclear Physics B 138, 141–150, doi:10.1016/0550-3213(78)90161-X
- **Energy conditions and singularity theorems.** In course conventions the Raychaudhuri equation contains $-R_{\mu\nu}u^\mu u^\nu$, and focusing needs $R_{\mu\nu}u^\mu u^\nu \ge 0$, or $R_{\mu\nu}k^\mu k^\nu \ge 0$ for light rays. A source with $s_Rs_{\rm Ric} = -1$ flips both the term and the inequality, so the theorems say the same thing. Penrose's singularity theorem rests on the null version. Amal Kumar Raychaudhuri (1955), *Relativistic cosmology. I*, Physical Review 98, 1123–1126, doi:10.1103/PhysRev.98.1123; Roger Penrose (1965), *Gravitational collapse and space-time singularities*, Physical Review Letters 14, 57–59, doi:10.1103/PhysRevLett.14.57
- **Ricci flow.** Hamilton's flow $\partial_tg_{ij} = -2R_{ij}$ is written so that positive Ricci curvature, as on a round sphere, shrinks the metric. With the opposite Ricci sign the same flow reads $+2R_{ij}$. Copying the formula without translating reverses the flow into an ill-posed backward flow, like running heat flow backward in time. Richard S. Hamilton (1982), *Three-manifolds with positive Ricci curvature*, Journal of Differential Geometry 17, 255–306, doi:10.4310/jdg/1214436922

## Review: novice

**Verdict:** fixed (2026-09-13, revision 5)

**Retell attempt:** If you carry an arrow around a loop on a ball it comes back turned. Two people can write that same turn as plus or as minus, depending on which way each decided counts as plus, and both are right. That choice is called a sign convention. To find out how a stranger counts, you test their table on a ball: two people walking side by side on a ball get closer, and that happens for everyone, so if the stranger gives a ball a minus sign they count the other way from the course. A saddle gets the opposite sign to a ball. I don't get why the gap grows on a saddle, or what 'curves the opposite way' means. I'm not sure how I'd draw a straight line on an orange. And the first part was about arrows turning, but the test is about walkers getting closer, so I'm not sure how the two go together. Also, does one ball test settle everything about a writer's signs?

Second novice pass, reading revision 3 in full before any fix. An arrow carried round a loop on a ball comes back turned. Ana writes that turn as plus and Ben as minus, and neither is wrong, because which way counts as plus is a choice called a sign convention. To find out how a stranger counts, test their table on something everyone agrees about: two people walking side by side on a ball get closer, and on a saddle they get further apart. If the stranger's table gives a ball a minus number, they count the other way, so flip every number in it, and in that same table a saddle gets the opposite sign to a ball. What I could not say back. The first way said the number for a surface is an arrow's turn divided by the loop's area, then the whole test switched to gaps between walkers, and nobody told me the two give the same sign, so I could not tell whether Ana's plus is this course's plus. On the saddle I wondered whether it matters which way the two walkers set off, because I had just been told the saddle rises one way and falls the other. I read 'a writer may keep more than one table of curving numbers' twice, because until then a table was either the thing kept at every place or the stranger's list of surfaces. The summary told me everyone agrees on a ball's curving, which sounded like the opposite of the story, where two writers give a ball opposite numbers. And I had to guess what a 'stretch' was.

**Stumbles (28)**

- “So before borrowing a formula, test its signs on a ball, whose curving everyone can measure.”: False first what-if: the summary makes the ball test sound like a complete check, but the ball test way's own simplifies says a ball reveals only some sign choices. The entry prose must be true for a reader who never sees simplifies.
- “Back at the start, both of them see the same thing: the arrow has come back turned a little toward their left.”: A direction without a reference: their left while facing which way? The walkers have turned at every corner, and the arrow's starting direction was never given.
- “They differ only in which way they agreed to count as plus.”: 'Agreed' suggests Ana and Ben agreed with each other, which is the opposite of what happened; I had to reread it.
- “so a borrowed formula can arrive with the wrong sign even when its writer made no mistake.”: 'Wrong sign' contradicts the way's own point that neither sign is wrong, and it does not say wrong for whom.
- “with plus 5 written in one notebook and minus 5 in the other”: The picture drops the unit, so 'plus 5' does not match the 5 thousandths of a degree in the explanation.
- “Both walk straight ahead, never steering left or right.”: 'Straight' on a ball is a wording trap and is used here both as a direction ('straight ahead') and as a walk that never steers, and the term is never introduced in its own sentence although the glossary lists it. The sentence also does not say how far they walk before measuring.
- “On a saddle, which curves the opposite way, the gap grows.”: Two gaps: 'curves the opposite way' names no shape I can picture, and the growing gap is a surprise with no reason, count or test.
- “curving that makes the gap shrink, like a ball's, gets plus numbers. ... If its numbers are plus, the writer counts like this course.”: A step left implicit: the first way said the table lists arrow turns, and this way switches to walkers' gaps without saying which number in the table is being read. 'Its numbers are plus' is also not quite true, since a full table lists each loop one chosen way round and so holds entries of both signs.
- “So this course makes one agreement:”: An agreement needs two parties; it is a choice.
- “If they are minus, the writer counts the other way. Then flip the sign of every number in that table before you use it.”: 'Then' reads as a next step for every table, not only for the minus case.
- “Now look up a ball in the stranger's table.”: False first what-if: a teenager asks whether one ball test settles all of a writer's signs. The only scope sits in simplifies.
- “Extend each dash toward the stalk as straight as the peel allows.”: A rule I cannot physically follow: nothing tells me what straight means on peel, so I could draw lines that curve toward each other or not.
- “It curves the opposite way to a ball, so walkers who set off side by side on it spread apart.”: The glossary's 'so' presents spreading as following from an unexplained shape.
- “For a ball, it lists minus numbers.”: The check uses 'numbers' where the entry way now reads one number for a ball's curving; two words for one idea.
- “Which change flipped both records, and which difference flips only one?”: Reread twice: the difference between Ana's and Ben's counting flips nothing in this story, so 'flips only one' has no event to point at, and the objective's 'a change of convention flips one writer's record' is never actually tested.
- “This time the arrow comes back turned toward their right, by the same amount.”: The reverse walk has a different first stretch, so 'their right' has no stated facing, and the arrow's starting direction for the second walk is unclear.
- “One writes the turn as plus five, the other as minus five.”: The spoken opening question and the entry teaching-arc prediction give numbers with no unit, unlike the way they point at.
- “So before borrowing a formula, start by testing its signs on a ball, whose curving everyone agrees on.”: It reads as if every writer gives a ball the same curving number, which is the opposite of the note's own story, where one writer's table gives a ball a minus number. What everyone agrees on is what a ball does, not the number written for it.
- “At the start, the arrow points ahead, along their first stretch.”: Undefined word on first use. 'Stretch' is never introduced, yet it carries the arrow's starting direction here and in the entry check and the entry problem.
- “So this course makes one choice: curving that makes the gap shrink, like a ball's, gets a plus number.”: A step left implicit, and the gap the first retell fell into. The first entry way's choice was about which way an arrow's turn counts as plus; this way's choice is about which behaviour of two walkers counts as plus. Nothing says the two choices agree, so the reader cannot tell whether Ana's plus is this course's plus.
- “On a saddle, the gap between two walkers grows.”: A false-looking first what-if. The two sentences before it say the saddle rises ahead and behind but falls away to left and right, so the obvious question is whether walkers who set off along the horse behave like walkers who set off across it. The sentence answers neither.
- “A writer may keep more than one table of curving numbers, and each table needs its own test on a ball.”: One word in a third sense. A table has been the Riemann tensor kept at every place, then the stranger's list of surfaces; here it means a different kind of curving number. I reread the sentence trying to work out which of the two earlier tables was being multiplied.
- “On a ball, walkers who set off side by side draw together, and on a saddle they spread apart.”: Two phrasings for one idea. The entry way says the gap shrinks and the gap grows; the check, the glossary and the takeaway say draw together and spread apart. The reader meets the second phrasing first in the check and has to map it back.
- “For a surface, one number at each spot is enough to describe the curving there: the turn divided by the loop's area.”: A step left implicit. One number per spot does not by itself give one number for a whole ball, yet the next paragraphs look up 'a ball' in the table and read off a single number.
- “Two careful people walk the same small loop on a huge ball and watch an arrow that never swings come back turned toward their left.”: A direction without a reference: their left while facing which way? The walkers turned at every corner, so 'their left' needs the facing that the entry way is careful to give.
- “A stranger's table gives a ball minus numbers. What sign does it give a saddle?”: Two words for one idea again: the entry way and the check both read 'a minus number' for a ball, so the plural here reads as a different claim about the table.
- “to find which way a stranger's table of curving counts as plus”: 'A table of curving' is not the phrase used anywhere else; I had to reread it as 'a table of curving numbers'.
- “Measure something everyone agrees on, such as walkers drawing together on a ball, and see which sign the stranger's table gives a ball.”: One sentence uses 'measure' for an experiment and 'see' for looking up a number in a table, which blurs the note's own separation of what happens from how it is written.

**Fixes**

- Summary: scoped the ball test as a start that reveals some choices, not all.
- Two tables for one ball: gave the arrow a starting direction and the walkers a facing when they compare; replaced 'agreed' with 'each of them chose'; replaced 'wrong sign' with 'the opposite sign to the one you would write' in its own paragraph; added the unit to the picture.
- Test the signs on a ball: recap restates the prerequisite's one number per spot for a surface; introduced 'walking straight' in its own sentence and said the walkers go the same distance; added a saddle-shape picture and marked the saddle's spreading as taken on trust; replaced 'agreement' with 'choice'; the table test now reads the number given to a ball; scoped the minus case with 'In that case'; added a paragraph saying each table needs its own ball test and spacetime tables have choices a ball cannot test; replaced the undoable orange try-it with two rubber bands through the stalk.
- Glossary saddle: shape described from a named standpoint, and the unsupported 'so' removed.
- Check stranger-table-saddle, misconception minus-means-saddle and objective calibrate-with-a-ball: 'a plus number' or 'a minus number' for a ball, matching the entry way.
- Check two-tables-one-ball and problem walk-it-the-other-way: arrow start and walker facing stated; the problem now asks what happens when Ben switches his counting, so it evidences the objective's 'flips one writer's record' half; answer, key points and solution extended.
- Opening question two-writers-one-turn and teaching arc same-turn-two-records: added 'thousandths of a degree'.
- Ladder: What each switch flips now also continues 'Test the signs on a ball' and says the ball test becomes the sphere calculation; teaching arc flip-each-switch and the working level switch no longer point at the fourth-slot sphere check the writer dropped; fixed a missing space after 'So' in the formal way.
- Validator follow-up: split the Two tables for one ball picture and the Test the signs on a ball takeaway into two sentences each, since each ran past 32 words; wrote 'tables that describe space and time together' instead of the unglossed 'spacetime'.
- No items were dropped; every part stays within its cap.
- Second novice pass (revision 3 to 4), 11 stumbles.
- Summary: a ball's behaviour, not its curving, is what everyone agrees on.
- Two tables for one ball: the loop is given four corners and 'stretch' is introduced in its own sentence; 'stretch' added to the glossary.
- Test the signs on a ball: new bridge paragraph tying the arrow's leftward turn to the shrinking gap, so the reader can see that Ana's plus and this course's plus are the same choice.
- Test the signs on a ball: the saddle sentence now says the walkers spread apart whichever way they set off from the middle; the recap says a round ball curves the same everywhere, so one number covers it; 'more than one table of curving numbers' became 'more than one kind of curving number', so 'table' keeps one meaning; the gap and the walkers' wordings are paired once each; the takeaway says 'find' rather than 'see'.
- Objective calibrate-with-a-ball, teaching arc calibrate-a-stranger and opening question two-writers-one-turn: 'table of curving numbers', 'a minus number', and the walkers' facing when they compare the arrow.
- No item was dropped. Entry way explanations went from 773 to 918 words against a cap of 1000; every other part is unchanged.

**Concerns**

- The saddle's spreading of side-by-side walkers is taken on trust at entry, as in the Riemann curvature tensor and geodesic deviation notes. No household test is known to show it cleanly. A shared visual of walkers on a saddle or near a swim ring's hole would back it across notes.
- The rubber-band try-it relies on a tight band on a near-round orange following the shortest way around. The physics reviewer should confirm that the wording 'the shortest way never steers left or right' is acceptable at entry.
- Working and formal content was not changed beyond the bridge and pointer fixes. The writer's GOCE sign remark and unverified references remain for the physics review.
- The note's comparison symbols s_g, s_R and s_Ric are not in course-conventions.md; an editor may want to adopt them there.
- Second pass: the new bridge paragraph states that on a ball any small loop walked with the enclosed piece on the walker's left brings the arrow back turned toward that walker's left. It follows from the course orientation row and from the note's own Ana and Ben walk, but it is new learner-visible physics text and needs a physics diff check.
- Second pass: the saddle scoping 'whichever way they set off from the middle' is new learner-visible physics text and needs a physics diff check. It holds because a saddle has negative curving at its middle, so nearby straight walks separate in every direction, but the entry rung still takes the saddle on trust.
- This pass changed learner-visible text after the physics stage had signed revision 3, so review.physics.reviewed_revision is now behind the note. Status was set back to novice-reviewed; an editor should not publish until a physics diff check covers revision 4.

**Re-read** (2026-09-13, revision 3): 0 stumbles in 2 changed passages

- Fix: No wording changes. The gap sentence reads cleanly in its paragraph: 'they' can only mean the two walkers, 'walked a quarter of the way around' is measured from their start, and the next sentence's equator-to-North-Pole example shows the quarter at which the walkers meet. The German title spelling 'Ueber' is a work title and needs no gloss.

**Re-read** (2026-09-13, revision 5): 1 stumbles in 3 changed passages

- “Walkers who set off side by side from its middle spread apart.”: A step taken on trust, and only in this standalone definition: it does not say that the walkers never steer. A reader who meets the word saddle on its own can answer that any two people spread apart if they walk in different directions, even on a flat floor, so the sentence sounds true of everything and the saddle loses its meaning. The way that uses the word supplies the rule two paragraphs earlier, so a reader arriving in sequence is safe. Adding the rule would add a condition to the sentence, so it is left for an editor.
- Fix: No wording changes, so the revision is unchanged at 5. The one entry sentence the physics review changed, the saddle definition's scoping to 'from its middle', reads cleanly in place: the sentence before it already puts one person 'standing at its middle', so two walkers setting off from the middle needs no further picture, and 'spread apart' matches the way's own 'they spread apart, whichever way they set off from the middle'. The one stumble recorded here needs a condition added to the sentence, which is outside a re-read's licence, so it is proposed for an editor instead of applied.

## Review: physics

**Verdict:** fixed (2026-09-13, revision 5)

**Verification**

- Christoffel symbols unchanged under g -> -g; mixed Riemann carries s_R; lowered Riemann s_g s_R; Ricci s_R s_Ric; scalar s_g s_R s_Ric; Einstein tensor s_R s_Ric.: Counted metric factors in the course Christoffel and Riemann formulas; traced with R^rho_{mu nu rho} = -R^rho_{mu rho nu}. → Correct in the working way, key equation switch-rules, derivation and check signature-flip-what-changes.
- Einstein equation in any convention: G~ + s_g s_R s_Ric Lambda g~ = s_R s_Ric (8 pi G/c^4) T.: Substituted G = s_R s_Ric G~, g = s_g g~ into the course equation; python check over all eight sign triples with random values; compared with a known (-,+,+,+), reversed-Riemann literature form R - (1/2)gR - lambda g = -8 pi G T. → Correct; all eight triples pass and the literature form matches (s_g,s_R,s_Ric) = (+,-,+).
- T_mu nu with lower indices is the same array in every convention.: Perfect fluid in (+,-,-,-): (rho+p)u_mu u_nu - p g~_mu nu with u_mu flipped twice and g~ = -g; formal variational definition -2 s_g (-g~)^(-1/2) dS/dg~^ab with det g~ = det g in four dimensions. → Correct; trace T flips.
- Sphere: R^theta_{phi theta phi} = sin^2 theta, R = +2/a^2; sectional K = +1/a^2.: Hand computation from Gamma^theta_{phi phi} = -sin cos, Gamma^phi_{theta phi} = cot; python finite difference at theta = 0.7. → 0.415016 vs sin^2 0.7 = 0.415016. Correct, and independent of a.
- Sectional curvature and constant-curvature K transform as s_g s_R.: One lowered Riemann in numerator, two metric factors in denominator or bracket. → Correct.
- Formal lemma: Koszul formula linear in g, so g and s_g g share the Levi-Civita connection; curvature operator R(X,Y) = [nabla_X, nabla_Y] - nabla_[X,Y] and Ric(Y,Z) = tr(X -> R(X,Z)Y) reproduce the course component definitions.: Component comparison with [nabla_mu, nabla_nu]V^rho = R^rho_{sigma mu nu}V^sigma. → Correct.
- Formal limits: odd dimensions need sqrt|det g|; a round spatial 3-sphere has induced scalar curvature -6/a^2 when s_g = -1.: det(s_g g) = s_g^n det g; R~ = s_g s_R s_Ric (6/a^2). → Correct as stated (for a negative-definite induced metric).
- Entry: walkers leaving the equator 1 km apart and walking 100 km toward the North Pole end about 12 cm closer.: python: 1 km x (1 - cos(100/6371)). → 12.3 cm. Correct.
- Entry: side-by-side walkers on a ball draw together; on a saddle they spread apart.: Jacobi equation J'' = -K J with J'(0) = 0: on a sphere J = J0 cos(s/a), on a surface with K < 0 J grows monotonically. → Sphere: gap shrinks only until a quarter of the way around, then the walkers cross and the gap grows. The entry sentence was universal; scoped. Saddle: true for a surface with negative curvature along the walk.
- Entry try-it: a tight rubber band through the stalk and the opposite spot takes the shortest way around, and on a ball the shortest way never steers.: A taut elastic on a smooth convex surface rests on a length-critical curve, a geodesic; on a sphere the band through two antipodal points is a great circle through both; two such meridians are parallel at the equator and meet at the poles. → Acceptable at entry for a near-round orange; the convergence shown is the meridian convergence of the globe example.
- Entry sign stories: left-turning small loop on a ball returns the arrow turned left; reversed loop turns it right by the same amount; Ana +5/+6/+4, Ben the opposite; switching Ben's counting changes only his record.: Local Gauss-Bonnet with the conventions orientation row: holonomy = +K A for the region on the walker's left, -K A when reversed. → Correct in check two-tables-one-ball and problem walk-it-the-other-way; numeric values and tolerances fine.
- Check stranger-table-saddle: within one table a saddle's number has the opposite sign to a ball's.: Gaussian curvature of a surface transforms by one overall factor per table. → Correct.
- Tides at Earth's surface: 2GM/r^3 = 3.08e-6 s^-2; R^r_0r0 = -2GM/c^2 r^3 = -3.43e-23 m^-2 in the course; s_R = -1 gives both +; s_g = -1 keeps the mixed component and flips the lowered one.: python with GM = 3.986e14, r = 6.371e6 m; Newtonian limit R^i_0j0 = d_i d_j Phi / c^2 with Phi = -GM/r and the course deviation equation. → 3.083e-6 s^-2, 3.430e-23 m^-2. All signs correct.
- Slot-order remark: -R^mu_{nu rho sigma} u xi u = +R^mu_{nu sigma rho} u xi u.: Antisymmetry in the last pair. → Correct; notation trap deviation-slot-order agrees.
- Dust: R = 8 pi G rho/c^2 = 1.87e-23 m^-2 and focusing term 4 pi G rho = 8.39e-7 s^-2 for 1000 kg/m^3; the (+,-,-,-) text finds -1.87e-23.: Trace of the course equation with T = -rho c^2; trace reversal with u^mu = (c,0,0,0); python. → 1.866e-23 m^-2 and 8.387e-7 s^-2. Correct; rel_tol 0.02 fine.
- Problem identify-the-switches: s_g = -1, s_R = -1, s_Ric = +1; paper writes G + Lambda g = -8 pi G T/c^4; dust check gives R~ = +8 pi G rho/c^2.: Worked each step, including the trace with T~ = +rho c^2. → Correct.
- Check lambda-term-other-signature.: Substituted G~ = G, g~ = -g. → Correct.
- Formal problem: Ric(u,u) = 4 pi (rho + 3p) - Lambda; volume law dV''/dV = -Ric(u,u) at zero expansion, shear and rotation.: Trace reversal R_ab = 8 pi (T_ab - T g_ab/2) + Lambda g_ab; Raychaudhuri equation. → Correct; the ball shrinks only when 4 pi (rho + 3p) > Lambda, so 'starts to shrink' was scoped to 'starts to change its volume'.
- de Sitter: K = H^2, R = 12H^2, Lambda = 3H^2, Kretschmann 24H^4; free particles at rest accelerate apart; K~ = s_g s_R K, R~ = s_g s_R s_Ric R.: Constant-curvature contractions in n = 4 (R = n(n-1)K, Kretschmann 2n(n-1)K^2); vacuum Einstein equation; deviation gives xi'' = +H^2 xi. → Correct.
- Kretschmann 48 G^2M^2/c^4 r^6 unchanged in all eight conventions; about 1.4e-44 m^-4 at Earth's surface.: Sign counting (s_g s_R)^2; python. → 1.41e-44 m^-4. Correct.
- GOCE: 2009-2013; r = 6626 km (255 km altitude); 2GM/r^3 = 2.74e-6 s^-2; R^r_0r0 = -3.05e-23 m^-2; geodesy potential V = +GM/r gives V_rr = +2GM/r^3, opposite to d_r^2 Phi.: python; sign of the geodesy convention. → 2.740e-6 s^-2, 3.049e-23 m^-2. Correct.
- Lambda = 3 Omega_Lambda H0^2/c^2 = 1.09e-52 m^-2 with H0 = 67.4 km/s/Mpc, Omega_Lambda = 0.685.: python with 1 Mpc = 3.0857e22 m. → 1.091e-52 m^-2 (1.090e-52 with 0.6847). Correct.
- Euclidean action I = -(1/16 pi) int (R - 2 Lambda) sqrt g plus boundary term, weight e^-I, conformal factor problem.: Wick rotation t = -i tau of the course Lorentzian action: iS = -I. → Correct in course curvature signs.
- Raychaudhuri focusing term -R_mu nu u u, null convergence for Penrose's theorem; Hamilton flow dg/dt = -2 Ric shrinks a round sphere; the reversed flow is ill-posed.: Standard forms re-derived and compared. → Correct.
- Minkowski 1908 used an imaginary time coordinate.: Wikisource full text of the Grundgleichungen paper. → Confirmed: he works with it in place of t. Venue Nachr. Ges. Wiss. Goettingen, Math.-Phys. Kl. 1908, 53-111.
- References: Rummel, Yi, Stummer 2011; Planck 2018 VI; Gibbons-Hawking 1977; Raychaudhuri 1955; Penrose 1965; Hamilton 1982.: Matched against the records already confirmed in the physics reviews of number-of-independent-riemann-components, parallel-postulate, second-fundamental-form, geodesic-deviation-equation and ricci-tensor (web search budget was exhausted in this session). → Authors, years, titles, venues and DOIs agree; verified.
- Gibbons, Hawking, Perry 1978, Nucl. Phys. B 138, 141-150.: Crossref API query. → Confirmed; DOI 10.1016/0550-3213(78)90161-X added.
- Einstein 1917, Sitzungsber. Preuss. Akad. Wiss. Berlin, 142-152; added Lambda term for a static closed universe.: Wikipedia citation record for Einstein's static universe. → Confirmed.
- Riemann 1868, Abh. Kgl. Ges. Wiss. Goettingen 13, 133-150; 1854 habilitation lecture.: Vault records from earlier physics reviews (a facsimile text archive gives 133-150; some catalogues give 133-152). → Venue, volume and year confirmed; title spelled 'Ueber' as printed; page range kept at 133-150 with the discrepancy noted in concerns.
- Second physics pass over revision 4. The novice reviewer's new bridge paragraph in 'Test the signs on a ball': a small loop walked with the enclosed piece of ground on the walker's left brings the arrow back turned toward the walker's left on a ball, and this agrees with Ana's counting in 'Two tables for one ball'.: Numerical parallel transport on the unit sphere by composing exact great-circle rotations, 16004 steps. (a) Octant loop from the equator: east a quarter turn, to the pole, back down the starting meridian, with the octant on the left at every leg; compared the returned arrow with the first-stretch direction using left = n x ahead, n the outward normal (the walker's head). (b) Small coordinate square, phi in [0, 0.02], theta from pi/2 to pi/2 - 0.01, traversed with the region on the left; compared with K*A = a sin b. → (a) +90.000000 degrees, exactly the octant area pi/2, toward the walker's left. (b) +1.9999666684e-4 rad against K*A = 1.9999666668e-4, ratio 1.0000000000. Reversed traversal gives the same magnitude with a minus sign. The bridge paragraph, the conventions orientation-and-rotation-sense row, and the entry problem walk-it-the-other-way all agree.
- Novice rewrite: 'The gap goes on shrinking at least until they have walked a quarter of the way around the ball.': Jacobi equation on a sphere of radius a for walkers starting side by side, xi'' = -xi/a^2 with xi'(0) = 0, so xi = xi0 cos(s/a); first zero at s = pi a/2 against a great-circle circumference 2 pi a. → The gap shrinks monotonically to zero at exactly a quarter of the way around, so 'at least until' is true and conservative. The equator-to-pole example sits exactly at that quarter: pi/2 x 6371 km = 10008 km.
- Novice rewrite: on a saddle the gap grows 'whichever way they set off from the middle'.: Gaussian curvature is a function of the point alone, not of the direction, so xi'' = -K xi with K < 0 at the middle gives xi'' > 0 for every starting direction; checked against z = x^2 - y^2, where K = -4/(1 + 4x^2 + 4y^2)^2 < 0 everywhere. → Correct, and the direction-independence is exact on a surface. The scoping to the middle is what makes the sentence safe on a real saddle seat, whose rim need not have K < 0.
- Novice addition to the recap of 'Test the signs on a ball': 'A round ball curves the same everywhere, so one number covers the whole of it.': Gaussian curvature of a round sphere of radius a is 1/a^2 at every point. → Correct.
- Glossary entry 'saddle' claimed without scope that side-by-side walkers spread apart.: Counterexample: a real saddle seat or a torus-like swim ring has K >= 0 at parts of its rim, where side-by-side walkers do not spread apart. The way's text scopes the claim to the middle; the glossary did not. → Fixed: the glossary now says walkers who set off side by side from its middle spread apart.
- Formal proposition as stated covers the Einstein tensor.: Applied the proposition literally to G_ab = R_ab - (1/2) R g_ab. The term R g_ab multiplies by the metric, which is neither a raising, a lowering, nor a metric-free operation, so the proposition as written did not cover the very object the formal problem asks the reader to obtain from it. Recounted: R_ab has k = 0, m = 1; R g_ab has k = 2, m = 1; both carry s_R s_Ric, so the sum does too. → Fixed: the proposition now counts every metric factor, including multiplications by g_ab or g^ab, and states that a sum of terms carrying one sign carries that sign. The conclusion G~_ab = s_R s_Ric G_ab is unchanged and correct.
- Notation trap riemann-overall-sign listed what a reversed Riemann sign flips.: With s_R = -1 and the course signature and Ricci slot, s_g s_R s_Ric = -1, so the written sign of the Lambda term flips as well; the trap's list omitted it while the signature trap lists it. → Fixed: the Lambda term added to the list, so the trap now translates a whole Einstein equation.
- All eight conventions: G~_ab = s_R s_Ric G_ab and G~ + s_g s_R s_Ric Lambda g~ = s_R s_Ric (8 pi G/c^4) T.: python loop over the eight sign triples with arbitrary numerical R_mn, R, g_mn, Lambda. → All eight pass, both identities exact.
- Recomputed every number in the note at this revision.: python with G = 6.674e-11, GM = 3.986e14 m^3/s^2, R_earth = 6.371e6 m, c = 2.998e8 m/s, 1 Mpc = 3.0857e22 m. → Entry 1 km x (1 - cos(100/6371)) = 12.3 cm; 2GM/r^3 at the surface 3.083e-6 s^-2 and R^r_0r0 = -3.430e-23 m^-2; GOCE at r = 6626 km, 2.740e-6 s^-2 and -3.049e-23 m^-2; dust at 1000 kg/m^3, R = 1.866e-23 m^-2 and 4 pi G rho = 8.387e-7 s^-2; Lambda = 1.091e-52 m^-2; Kretschmann 48 G^2M^2/c^4 r^6 = 1.412e-44 m^-4 at the surface. Every printed value and tolerance stands.
- Sphere components and the constant-curvature contractions re-derived by hand.: R^theta_{phi theta phi} from Gamma^theta_{phi phi} = -sin theta cos theta and Gamma^phi_{theta phi} = cot theta in the course Riemann formula; R_{abcd} = K(g_ac g_bd - g_ad g_bc) contracted as R_mn = R^rho_{m rho n} in n = 4. → R^theta_{phi theta phi} = sin^2 theta, R = +2/a^2; R = n(n-1)K = 12H^2, Kretschmann 2n(n-1)K^2 = 24H^4, Lambda = 3H^2, and geodesic deviation gives xi'' = +H^2 xi. All as printed.
- References re-verified independently at this revision.: Crossref API for each DOI: Rummel, Yi, Stummer 2011; Planck 2018 VI; Gibbons-Hawking 1977; Gibbons, Hawking, Perry 1978; Raychaudhuri 1955; Penrose 1965; Hamilton 1982. Web records for Riemann 1868 and Hamilton's page range. → Authors, years, titles, venues, volumes and page ranges all match the note. Hamilton 1982 confirmed as J. Differential Geometry 17, 255-306. Riemann 1868 remains split: a digitized-volume catalogue record gives 133-152, a text archive gives 133-150; the note keeps 133-150 and the concern stands.
- The novice reviewer's wording-only rewrites carry no physics: 'stretch' glossary entry and 'four parts of the walk between corners', 'table of curving numbers', 'whose behaviour everyone agrees on', 'a ball a minus number', 'find which sign', and the split opening question.: Read each against the claim it replaces; checked that the split opening question still names the loop, the non-swinging arrow, the re-facing at the start and the leftward turn. → No physics changed. The opening question states the observed turn without naming the walking sense, which is consistent with way 1, the check and the problem.

**Counterexamples tried**

- Walk farther than a quarter of the way around the ball: side-by-side walkers cross and their gap then grows. Broke the entry sentence 'On a ball, the gap shrinks'; scoped to 'at least until they have walked a quarter of the way around the ball'. The equator-to-pole example is exactly a quarter and stays true.
- Reversed loop (region on the walker's right): the arrow turns right; problem walk-it-the-other-way already handles it correctly.
- Large loop enclosing half the ball: arrow returns matching, both writers write zero; covered by 'most loops' in the recap and summary.
- Flat floor and a rolled paper tube: zero for every convention; entry says both write zero on a flat floor. True.
- Saddle far from its middle: curvature of a real saddle seat need not stay negative at its rim; the entry places the walkers at the middle, so the statement holds there.
- Signature flip alone (s_g = -1): sphere check passes but R of dust flips; handled by misconception sphere-check-is-complete and check dust-reveals-signature.
- Opposite Riemann sign with fourth-slot Ricci: the two flips cancel in Ricci, R and the Einstein equation but not in the lowered or mixed Riemann tensor or the deviation equation; the notation trap and switch rules say so.
- Weinberg-type convention (-,+,+,+) with reversed Riemann sign: G - lambda g = -8 pi G T; reproduced by the any-convention equation.
- Odd dimension: det(s_g g) = -det g, so sqrt(-g) fails; the formal limits paragraph says so.
- Spacelike slice with s_g = -1: the induced metric is negative definite and a round 3-sphere has R = -6/a^2; the formal way says the sphere calibration does not apply unchanged.
- Large positive Lambda with dust: 4 pi rho < Lambda makes a small ball grow, not shrink. Broke the formal problem's 'starts to shrink'; rescoped to 'change its volume'.
- Permuted slot layouts and antisymmetrizer factors of one half: outside the sign counting; stated in both simplifies and the formal limits.
- Lambda-term sign under s_R = -1 with the course signature: it flips too, so 'depending on the signature' in leads_to cosmological-constant was incomplete; fixed to the product of the three signs.
- Figure-eight small loop on a ball: no single piece of ground stays on the walker's left, so the bridge sentence's 'walked that way' does not apply to it and no false claim is made.
- Small loop walked with the ground on the walker's right (right turns at every corner): the arrow returns turned toward the right. Excluded by 'walked that way' and handled head-on by problem walk-it-the-other-way, which is the point of that problem.
- Saddle rim: a real saddle seat or a swim ring has K >= 0 somewhere away from the middle, so side-by-side walkers there do not spread apart. Broke the unscoped glossary sentence; scoped it to the middle, matching the way's text.
- Einstein tensor against the formal proposition: the term R g_ab is a metric multiplication, not a raising or lowering, so the proposition as stated did not cover G_ab. Fixed by counting every metric factor and adding the rule for sums.
- Timelike plane in spacetime: free-fall pairs that draw together have negative sectional curvature there, the opposite of a ball, so the entry rule 'shrinking gap counts as plus' must not be carried into spacetime. The note never does: its entry text says a ball cannot test the choices that describe space and time together, and the working rung quotes tidal components rather than a sectional curvature.
- Rolled paper tube: side-by-side straight walkers keep their gap and every convention writes zero, so the entry's ball-versus-saddle pair is not presented as exhaustive.

**Fixes**

- Entry way 'Test the signs on a ball': 'the gap shrinks' scoped to 'at least until they have walked a quarter of the way around the ball' (true for long walks, where the walkers cross).
- Formal problem einstein-equation-any-convention: statement, spoken statement, key point and last solution step say the dust ball 'starts to change its volume' at the same rate, and the solution states when it shrinks or grows.
- leads_to cosmological-constant: the written sign of the Lambda term depends on the product of all three signs, not only the signature. leads_to space-of-constant-curvature: flips with the Riemann sign too.
- References: DOI added for Gibbons, Hawking, Perry 1978; Riemann title spelled as printed; all references verified.
- Nothing dropped; word counts change by a few words.
- Second pass, revision 4 to 5. Glossary 'saddle': 'Walkers who set off side by side on it spread apart' scoped to 'from its middle', which is where the entry way places them and where a real saddle seat has negative curving.
- Formal way 'Conventions as three sign flips': the proposition now counts k metric factors, including multiplications by $g_{ab}$ or $g^{ab}$, and states that a sum of terms carrying one sign carries that sign, so it really covers the Einstein tensor the formal problem builds from it.
- Notation trap riemann-overall-sign: the written sign of the $\Lambda$ term added to the list of things a reversed Riemann sign flips.
- Nothing dropped; the note gains about twenty words and stays well inside every cap.

**Concerns**

- CARRIED FORWARD, still unresolved: $s_g$, $s_R$ and $s_{\rm Ric}$, and the three-sign description of a convention, are not in course-conventions.md, while the working and formal rungs lean on them throughout. An editor should adopt them there, for example in a 'Translating conventions' row, or the note is carrying a note-local convention against the conventions file's own rule.
- CARRIED FORWARD: Riemann 1868 page range. A digitized-volume catalogue record gives Abhandlungen 13, 133-152; a text archive that indexes only the lecture proper gives 133-150. The vault is split six notes to three in favour of 133-150, which this note keeps. An editor should settle one value across the vault rather than have single notes diverge.
- CARRIED FORWARD: both visuals are proposals, not catalog entries. The flagship three-sign-toggles-beside-a-ball carries this concept's central demonstration, and falling-ring-of-crumbs is cited by many curvature notes; neither exists in knowledge/visuals/ yet.
- CARRIED FORWARD: the saddle's spreading of side-by-side walkers is still taken on trust at the entry rung, here and in the Riemann and geodesic-deviation notes. Scoping it to the middle makes it true but supplies no evidence a reader can gather at home; a shared saddle or swim-ring visual would back it across all three notes.
- The entry rung's rule 'a shrinking gap counts as plus' is a Riemannian rule. It does not survive into a timelike plane, where free-fall pairs that draw together have negative sectional curvature. The note stays on the right side of this, but any future entry or working sentence that carries the ball rule into spacetime would be wrong; the conventions file's sectional-curvature row is the guard.
