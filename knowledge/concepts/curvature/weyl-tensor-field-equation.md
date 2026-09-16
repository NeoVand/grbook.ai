---
type: "concept"
schema_version: 2
id: "weyl-tensor-field-equation"
title: "Weyl tensor field equation"
tagline: "How the Bianchi identity lets matter shape curving far from where it sits"
domain: "curvature"
tier: "advanced"
status: "physics-reviewed"
revision: 4
updated: "2026-09-16"
aliases: ["Bianchi identity as a field equation for Weyl", "Weyl divergence equation", "C^abcd_;d = J^abc"]
prerequisites: ["weyl-tensor", "bianchi-identity", "einstein-field-equations", "newtonian-tidal-tensor"]
leads_to: ["ricci-focusing-versus-weyl-shear", "petrov-classification", "weyl-curvature-hypothesis"]
visuals: ["falling-ring-of-crumbs", "cube-of-small-loops"]
---

# Weyl tensor field equation

*How the Bianchi identity lets matter shape curving far from where it sits*

`weyl-tensor-field-equation` · curvature · advanced · physics-reviewed (revision 4)

**Needs:** [[weyl-tensor]] (entry) · [[bianchi-identity]] (entry) · [[einstein-field-equations]] (working) · [[newtonian-tidal-tensor]] (working)  
**Opens:** [[ricci-focusing-versus-weyl-shear]] · [[petrov-classification]] · [[weyl-curvature-hypothesis]]  
**Related:** [[contracted-bianchi-identity]] · [[maxwell-equations-in-tensor-form]] · [[gravitational-wave]]  
**Visuals:** [[falling-ring-of-crumbs]] · [[cube-of-small-loops]]

> Beside a planet there is no matter, yet a ball of crumbs let go there changes shape. Take the box rule of the Bianchi identity and remove the part of curving that matter sets. What remains says where that shape change can start: only where the amount of matter, or its motion, changes from place to place. Empty space then hands it on, so matter shapes curving far from where it sits.

## You will be able to

**Entry**
- Predict where a ball of crumbs only shrinks and where it only changes shape, for a uniform planet, and say where the shape change is switched on. `objectives/locate-the-switch-on` ← `checks/crumbs-at-the-centre-and-halfway`, `problems/centre-and-three-radii`
- State how the shape change fades with distance from a round planet, and why it fades faster than weight. `objectives/state-the-fading-rule` ← `checks/twice-as-far-one-eighth`

**Working**
- Derive the divergence law for the trace-free tidal tensor from Poisson's equation, and use it to get the inverse-cube law and the surface jump. `objectives/derive-the-newtonian-shadow` ← `problems/inverse-cube-from-balance`
- Distinguish the algebraic Einstein equation from the differential Weyl equation, and say which sources feed the Weyl current. `objectives/distinguish-algebraic-from-propagating` ← `checks/which-equation-propagates`

**Formal**
- Derive the Weyl divergence equation in n dimensions from the Bianchi identity, and count its independent components. `objectives/derive-and-count` ← `checks/count-the-components`
- Prove that the Weyl current is identically conserved, and reduce it for a static perfect fluid to a density-gradient term. `objectives/prove-current-properties` ← `checks/current-is-conserved`, `problems/static-fluid-current`

**Research**
- Explain why the Bel–Robinson tensor is divergence-free in vacuum and what that conservation is used for. `objectives/explain-super-energy` ← `checks/bel-robinson-divergence`

## Ways in

### 1. The shape change starts at the surface · entry · picture

*Beside a planet no matter sits where the crumbs are. Where does the shape-changing part of their drift start?*

**Recap:** Let go of a small ball of crumbs, at rest, in a cabin falling freely. Compared with the centre crumb, the crumbs slowly drift. The room-changing part of the drift is the same in every direction, all in or all out, and matter right at the spot sets it. The shape-changing part stretches the ball along one line and squeezes it across, changing its shape but not its room. The Weyl tensor holds the shape-changing part.

Picture a made-up planet: a huge round cloud of fine dust, uniform, with a sharp surface. Let the whole cloud go, so it falls freely toward its centre, and let a cabin fall with it, the dust at rest around it. Inside, a ball of crumbs is let go.

Anywhere inside the cloud, the ball shrinks and keeps its shape. It shrinks because dust at the spot sets a room-changing part.

It keeps its shape because a uniform cloud pulls in step with the distance from its centre: nothing at the centre, half as strong halfway out. Seen from the centre crumb, that is a pull toward the centre crumb, growing in step with distance from it, the same in every direction. So every pair of crumbs drifts together by the same amount.

Just outside the surface no dust sits at the spot, so the room-changing part is gone. Pure shape change is left: the ball stretches along the line to the centre and squeezes across it.

So the shape-changing part is switched on at the surface, where the amount of matter changes.

**Takeaway:** Inside a round, uniform planet a ball of crumbs only shrinks. Just outside it only changes shape. The shape-changing part is switched on at the surface, where the amount of matter changes.

*What this leaves out:* A round, uniform planet, at rest or falling in on itself evenly. Where matter moves in other ways, or spins, its motion can also make a shape-changing part.

*Builds on:* [[weyl-tensor]]<br>*Visuals:* [[falling-ring-of-crumbs]]<br>*See:* `checks/crumbs-at-the-centre-and-halfway`

### 2. Empty space hands the shape change on · entry · structure

*What carries the shape-changing part from the planet's surface out to a satellite, across empty space?*

**Recap:** Carry an arrow around each of the six faces of a tiny box and add up the changes. Every edge is walked once each way, so the six changes add up to nothing. Opposite faces nearly cancel, and their three leftovers must add up to nothing. So how curving changes in one direction is tied to how it changes in the other two. This box rule is the Bianchi identity, and it holds in every smoothly curved space.

The box rule carries the shape change from the surface to a satellite. Split the rule's curving into its two parts. Matter at each spot sets the room-changing part, so its changes are known wherever the matter is known. Take them out; what is left is a rule for the shape-changing part alone.

In empty space, step from a spot in three directions at right angles, and note how much the shape-changing part changes along each step. The three changes add up to nothing. So the shape-changing part cannot start or stop in empty space: each thin layer passes it on to the next, out to the satellite.

Where the amount of matter changes from place to place, the three changes add up to an amount set by how fast it changes. There the shape-changing part is made.

**Takeaway:** In empty space the changes of the shape-changing part along three directions add up to nothing, so it cannot start or stop there: each layer of empty space passes it on. It is made only where the amount of matter, or its motion, changes.

*What this leaves out:* The shape-changing part is a table of numbers, and the adding-up rule holds row by row, with the entries mixed in a fixed way the working rung writes out.

*Continues:* `ways_in/shape-change-starts-at-the-surface`<br>*Builds on:* [[bianchi-identity]]<br>*Visuals:* [[cube-of-small-loops]]

### 3. The shape change fades faster than weight · entry · calculation

*How does the shape change fade with distance from a round planet, and why faster than weight?*

Passed on from layer to layer by the box rule, the shape change thins out: around a round planet, one eighth as strong at twice the distance from the centre.

Weight, the planet's pull, falls to one quarter when the distance doubles: a rule of gravity taken as known here. The shape change is the difference between the pulls on the ball's near and far crumbs. Twice as far, each pull is a quarter as strong. And the ball's width is half as big a part of the distance. So the difference is a quarter of a half: one eighth, one step faster than weight.

**Try it:** Three times as far gives one twenty-seventh: divide by three, three times over. Now the Sun. It pulls Earth about 180 times harder than the Moon, but it is about 390 times farther away. The shape change fades one step faster than a pull, so compare pull divided by distance: 180 divided by 390 is a bit less than one half. So the Sun's tide should be a bit less than half the Moon's. Look at a tide table, the list of high-water heights a harbour publishes, for a month. The tides are highest near new Moon and full Moon, when the Sun's shape change lines up with the Moon's, and lowest near the quarter Moons. The Sun shows, but never overpowers the Moon.

**Takeaway:** Twice as far from a round planet the shape change is one eighth as strong, weight one quarter. It fades one step faster because it is the difference of pulls across the ball. So the Sun raises a smaller tide than the Moon.

*Picture:* A round planet with a ball of crumbs just above its surface and another at twice the distance from the centre. The far ball is drawn with its stretch one eighth as long, beside scales that read one quarter.

*What this leaves out:* The one-eighth rule holds outside a round body at rest, or one falling in on itself evenly.

*Continues:* `ways_in/empty-space-hands-it-on`<br>*Builds on:* [[weyl-tensor]]<br>*See:* `checks/twice-as-far-one-eighth`

### 4. Split the Riemann tensor and take the divergence · working · calculation

*How does the Bianchi identity become an equation for the Weyl tensor alone, and what is its source?*

The rule that hands the shape change on across empty space is the Bianchi identity with the Ricci part of curvature removed. In four dimensions the Riemann tensor splits as

$$R_{\rho\sigma\mu\nu} = C_{\rho\sigma\mu\nu} + \tfrac12\big(g_{\rho\mu}R_{\sigma\nu} - g_{\rho\nu}R_{\sigma\mu} + g_{\sigma\nu}R_{\rho\mu} - g_{\sigma\mu}R_{\rho\nu}\big) - \tfrac{R}{6}\big(g_{\rho\mu}g_{\sigma\nu} - g_{\rho\nu}g_{\sigma\mu}\big),$$

with $C$ the Weyl tensor. Contracted once, the Bianchi identity reads $\nabla^\rho R_{\rho\sigma\mu\nu} = \nabla_\mu R_{\sigma\nu} - \nabla_\nu R_{\sigma\mu}$; contracted twice, $\nabla^\rho R_{\rho\mu} = \tfrac12\nabla_\mu R$. Take the divergence of the split on the first index. The metric passes through $\nabla$, so the Ricci block gives $\nabla_\mu R_{\sigma\nu} - \nabla_\nu R_{\sigma\mu}$ plus $\tfrac12(g_{\sigma\nu}\nabla_\mu R - g_{\sigma\mu}\nabla_\nu R)$, and the scalar block gives $g_{\sigma\nu}\nabla_\mu R - g_{\sigma\mu}\nabla_\nu R$. Collecting the coefficients, $1 - \tfrac12$ and $-\tfrac14 + \tfrac16$, leaves

$$\nabla^\rho C_{\rho\sigma\mu\nu} = \nabla_{[\mu}R_{\nu]\sigma} - \tfrac16\, g_{\sigma[\nu}\nabla_{\mu]}R,$$

where square brackets average the two orderings with a sign, $X_{[\mu\nu]} = \tfrac12(X_{\mu\nu} - X_{\nu\mu})$. The derivation "Divergence of the Weyl decomposition" gives every step. Call the right side the Weyl current $J_{\sigma\mu\nu}$. It is antisymmetric in $\mu\nu$, and its trace on $\sigma\mu$ vanishes, as it must, because the Weyl tensor is trace-free.

Einstein's equation turns the current into matter. Trace-reversing $G_{\mu\nu} + \Lambda g_{\mu\nu} = (8\pi G/c^4)T_{\mu\nu}$ gives $R_{\mu\nu} = (8\pi G/c^4)(T_{\mu\nu} - \tfrac12 T g_{\mu\nu}) + \Lambda g_{\mu\nu}$, and the $\Lambda$ term has zero covariant derivative. So

$$\nabla^\rho C_{\rho\sigma\mu\nu} = \frac{8\pi G}{c^4}\Big(\nabla_{[\mu}T_{\nu]\sigma} - \tfrac13\, g_{\sigma[\nu}\nabla_{\mu]}T\Big).$$

Three things stand out. The source is not the stress-energy tensor but its derivatives: where $T_{\mu\nu}$ is covariantly constant the current vanishes, so the surface of a uniform body is a source and its interior is not. The cosmological constant drops out, so dark energy of the simplest kind, a cosmological constant, never feeds the current. And in vacuum the equation is homogeneous, $\nabla^\rho C_{\rho\sigma\mu\nu} = 0$; with the Bianchi identity itself it then governs how Weyl curvature travels through empty space.

**Takeaway:** The divergence of the Weyl decomposition turns the Bianchi identity into a divergence equation for the Weyl tensor, sourced by derivatives of the Ricci tensor, hence of the stress-energy tensor, with no cosmological-constant term.

*Continues:* `ways_in/empty-space-hands-it-on`<br>*Builds on:* [[weyl-tensor]], [[bianchi-identity]], [[einstein-field-equations]]<br>*See:* `derivations/divergence-of-the-weyl-decomposition`, `derivations/current-from-einstein-equation`

### 5. Gravity's Maxwell equation · working · bridge

*In what sense is this gravity's version of Maxwell's equation with a current, and where does the likeness stop?*

The divergence equation for the Weyl tensor has the shape of Maxwell's equation with a current, $\nabla_\nu F^{\mu\nu} = \mu_0 J^\mu$: an antisymmetric field, its divergence on one index, and a source on the right. The likeness is closest in a weak static field. There a freely falling observer measures the electric part of the Weyl tensor, $E_{ij} = c^2 C_{\hat\imath\hat 0\hat\jmath\hat 0}$, which is the trace-free part of the Newtonian tidal tensor, $E_{ij} = \partial_i\partial_j\Phi - \tfrac13\delta_{ij}\nabla^2\Phi$. Poisson's equation $\nabla^2\Phi = 4\pi G\rho$ then gives

$$\partial_j E_{ij} = \frac{8\pi G}{3}\,\partial_i\rho,$$

and the same law follows from the $\sigma = 0$, $\mu = i$, $\nu = 0$ component of the Weyl current. Compare Gauss's law, $\nabla\cdot\mathbf E = \rho_{\rm e}/\varepsilon_0$: electric flux starts on charge, and tidal flux, row by row of $E_{ij}$, starts where the mass density changes.

Symmetry now does the work it does for Coulomb's field. Outside a round body, the only trace-free symmetric tensor built from the radial unit vector $\mathbf n$ is $E_{ij} = A(r)(\delta_{ij} - 3n_in_j)$, and $\partial_jE_{ij} = 0$ forces $rA' + 3A = 0$, so $A \propto r^{-3}$. Fixing the constant at the surface of a uniform ball, where the density drops by $\rho$, gives $A = GM/r^3$ outside and $A = 0$ inside: the radial tide $E_{rr} = -2GM/r^3$ appears at the surface with a jump of $-(8\pi G/3)\rho$, which for Earth's mean density is $3.1\times10^{-6}$ metres per second squared for every metre of separation. The inverse cube is why the Sun, whose pull on Earth is 179 times the Moon's, raises a tide only 0.46 times as high.

In vacuum the equation is source-free, and with the Bianchi identity it makes the Weyl tensor obey a wave equation, exactly so in linearized gravity: gravitational waves are Weyl curvature on the move, and the tidal field a detector reads is $E_{ij} = -\tfrac12\ddot h_{ij}$ in transverse-traceless gauge, a result stated here from the gravitational-wave notes.

The likeness stops in three places. The equation is nonlinear, because $\nabla$ and $g$ contain the field it governs. The current is built from derivatives of $T_{\mu\nu}$, not from $T_{\mu\nu}$, and in general it also contains the motion of the matter. And $E_{ij}$ alone closes only in the Newtonian limit; in general it is coupled to a magnetic part, as $\mathbf E$ is to $\mathbf B$. Einstein's equation, by contrast, is algebraic: it sets the Ricci part of curvature from matter at the same event and carries nothing anywhere.

**Takeaway:** In a weak static field the divergence of the trace-free tidal tensor is eight pi G over three times the density gradient: a Gauss law sourced by density changes, giving the inverse cube by symmetry and waves in vacuum.

*What this leaves out:* The Newtonian form keeps only the electric part, for matter at rest in a weak field.

*Continues:* `ways_in/split-riemann-and-take-the-divergence`<br>*Builds on:* [[newtonian-tidal-tensor]], [[weyl-tensor]]<br>*Visuals:* [[falling-ring-of-crumbs]]<br>*See:* `derivations/newtonian-shadow-from-poisson`, `worked_examples/jump-at-the-surface-of-a-uniform-ball`, `checks/which-equation-propagates`, `analogies/gauss-law-for-charge`

### 6. Cotton current, component count, and the vacuum wave equation · formal · structure

*What precisely does the identity say in n dimensions, how many independent components has it, and what does it imply for the current and in vacuum?*

Gravity's Maxwell equation is, precisely, the trace-free part of the once-contracted Bianchi identity. Let $(M, g)$ be a pseudo-Riemannian manifold of dimension $n \ge 4$ with its Levi-Civita connection, and set $G = c = 1$. Write the Riemann tensor as

$$R_{\rho\sigma\mu\nu} = C_{\rho\sigma\mu\nu} + g_{\rho\mu}P_{\sigma\nu} - g_{\rho\nu}P_{\sigma\mu} - g_{\sigma\mu}P_{\rho\nu} + g_{\sigma\nu}P_{\rho\mu},\qquad P_{\mu\nu} = \frac{1}{n-2}\Big(R_{\mu\nu} - \frac{R}{2(n-1)}\,g_{\mu\nu}\Big),$$

with $P$ the Schouten tensor; for $n = 4$ this is the four-dimensional split. The twice-contracted identity gives $\nabla^\rho P_{\rho\nu} = \nabla_\nu P$ with $P = g^{\mu\nu}P_{\mu\nu}$, and the once-contracted identity then yields

$$\nabla^\rho C_{\rho\sigma\mu\nu} = (n-3)\big(\nabla_\mu P_{\nu\sigma} - \nabla_\nu P_{\mu\sigma}\big).$$

The bracket is the Cotton tensor. In four dimensions it is the Weyl current $J_{\sigma\mu\nu}$, and the coefficients $\tfrac12$ and $-\tfrac1{12}$ of the working rung are those of $P$.

*Hypotheses and content.* Nothing beyond metric compatibility, vanishing torsion and $n \ge 4$ is used; no field equation enters. $J_{\sigma\mu\nu}$ is antisymmetric in $\mu\nu$, has vanishing cyclic sum $J_{[\sigma\mu\nu]} = 0$, and is trace-free, $g^{\sigma\mu}J_{\sigma\mu\nu} = 0$; so is the left side, by the algebraic symmetries of $C$. In four dimensions that leaves $24 - 4 - 4 = 16$ independent components. The once-contracted Bianchi identity $\nabla^\rho R_{\rho\sigma\mu\nu} = \nabla_\mu R_{\sigma\nu} - \nabla_\nu R_{\sigma\mu}$ has twenty: its trace-free part is the Weyl equation, and its trace is the contracted Bianchi identity $\nabla^\mu G_{\mu\nu} = 0$, four more. The Weyl equation therefore contains no conservation law; it is the rest of the identity.

*The current is conserved.* $\nabla^\sigma J_{\sigma\mu\nu} = 0$ identically. Sketch: $\nabla^\sigma\nabla_\mu R_{\nu\sigma} = \tfrac12\nabla_\mu\nabla_\nu R + [\nabla^\sigma,\nabla_\mu]R_{\nu\sigma}$, and by the Ricci identity the commutator equals $R_{\mu\lambda}R^\lambda{}_\nu - R_{\lambda\nu\kappa\mu}R^{\lambda\kappa}$, which is symmetric in $\mu\nu$ by the pair symmetry of the Riemann tensor. The antisymmetrization in $\mu\nu$ kills it, together with the $\nabla_\mu\nabla_\nu R$ terms. This is the analogue of charge conservation, and like it, it holds whatever the sources do.

*Vacuum.* If $R_{\mu\nu} = \Lambda g_{\mu\nu}$ then $P_{\mu\nu} = \tfrac{\Lambda}{6}g_{\mu\nu}$ and $J = 0$. The Bianchi identity itself becomes $\nabla_{[\lambda}C_{\rho\sigma]\mu\nu} = 0$, and because the left and right duals of the Weyl tensor coincide, this cyclic form is equivalent to $\nabla^\rho C_{\rho\sigma\mu\nu} = 0$: one equation plays the roles of both of Maxwell's. Applying $\nabla^\lambda$ to the cyclic form and commuting derivatives gives

$$\Box C_{\rho\sigma\mu\nu} = -[\nabla^\lambda,\nabla_\rho]C_{\sigma\lambda\mu\nu} - [\nabla^\lambda,\nabla_\sigma]C_{\lambda\rho\mu\nu},$$

a wave equation whose right side is a sum of contractions of the Riemann tensor with $C$, quadratic in $C$ when $\Lambda = 0$. In linearized theory the right side is second order and drops: $\Box C_{\rho\sigma\mu\nu} = 0$.

*Static fluids.* For a perfect fluid $T_{\mu\nu} = (\rho + p)u_\mu u_\nu + p\,g_{\mu\nu}$ at rest in a static spacetime, so that $\nabla_\mu u_\nu = -u_\mu a_\nu$ and $(\rho + p)a_\nu = -D_\nu p$, the pressure gradient cancels against the acceleration term, and

$$J_{\sigma\mu\nu} = 8\pi\Big(u_\sigma u_{[\nu}D_{\mu]}\rho + \tfrac13\, g_{\sigma[\nu}D_{\mu]}\rho\Big).$$

Only the density gradient sources the Weyl tensor. Inside a star of uniform density $J = 0$, and indeed the constant-density interior solution is conformally flat, its Weyl tensor zero at every point; the exterior Weyl tensor is switched on at the surface.

*Limits.* For $n = 3$ the Weyl tensor vanishes identically and the identity reads $0 = 0$; the Cotton tensor is then unconstrained, and its vanishing is the criterion for conformal flatness. The equation is an identity about a given metric, not by itself a determined system for $C$: given the metric it holds; given $J$ it does not fix $C$, since every vacuum solution adds a homogeneous piece.

**Takeaway:** The divergence of the Weyl tensor is n minus three times the Cotton tensor: in four dimensions the trace-free sixteen of the twenty once-contracted Bianchi components, with an identically conserved current and a vacuum wave equation.

*What this leaves out:* Torsion-free, metric-compatible connection only; with torsion the identity acquires torsion terms.

*Continues:* `ways_in/gravitys-maxwell-equation`<br>*Builds on:* [[weyl-tensor]], [[bianchi-identity]], [[contracted-bianchi-identity]]<br>*See:* `derivations/cotton-form-in-n-dimensions`, `checks/count-the-components`, `checks/current-is-conserved`, `problems/static-fluid-current`

### 7. The 1+3 split, super-energy and peeling · research · bridge

*How do relativists use the equation in practice, and what does it feed today?*

The Cotton current and the vacuum wave equation become working tools once an observer field $u^\mu$ splits the Weyl tensor into an electric part $E_{\mu\nu} = C_{\mu\alpha\nu\beta}u^\alpha u^\beta$ and a magnetic part $H_{\mu\nu}$, its dual contracted the same way, each symmetric, trace-free and orthogonal to $u$, five components apiece. Projecting the Weyl equation and the Bianchi identity along and across $u$ gives four equations shaped like Maxwell's in a medium: two constraints, the divergences of $E$ and $H$, and two evolution equations for $\dot E$ and $\dot H$ with curls of the other field. For dust the $E$ constraint reads $D^\nu E_{\mu\nu} = \tfrac{8\pi}{3}D_\mu\rho$ plus products of the shear and vorticity with $E$ and $H$: the Newtonian shadow with its relativistic corrections. This is the 1+3 covariant formalism of cosmology, the way large-scale structure is followed without a background metric and the tidal field of a lump is separated from the local expansion.

The same split raised a live question. Setting $H = 0$ for irrotational dust closes the equations into ordinary differential equations along each worldline, the silent universes. Whether the constraint $H = 0$ survives the evolution turned out to fail in general; only special families, the Szekeres dust models among them, are consistent.

The vacuum equation also has an energy. The Bel–Robinson tensor

$$T_{\alpha\beta\gamma\delta} = C_{\alpha\rho\gamma\sigma}C_\beta{}^\rho{}_\delta{}^\sigma + {}^*C_{\alpha\rho\gamma\sigma}\,{}^*C_\beta{}^\rho{}_\delta{}^\sigma$$

is totally symmetric and trace-free, and $\nabla^\alpha T_{\alpha\beta\gamma\delta} = 0$ in vacuum follows from $\nabla^\rho C_{\rho\sigma\mu\nu} = 0$ and the cyclic identity, as the conservation of the Maxwell stress-energy follows from the source-free Maxwell equations. It is no local energy density of gravity, having the dimension of curvature squared, but it gives positive quantities that can be estimated: the proof of the nonlinear stability of Minkowski space treats the Bianchi identities as a Maxwell-like system for $C$ and controls Bel–Robinson energies along it.

Along outgoing null rays in an asymptotically flat spacetime the same equations propagate the five complex components of the Weyl tensor in a null frame and force the peeling pattern: successive components fall like $r^{-1}, r^{-2}, \dots, r^{-5}$, the $r^{-1}$ piece being the radiation field a detector reads. Friedrich's conformal field equations use the Weyl equation as an evolution system for the rescaled Weyl tensor itself. Each of these is the Weyl equation at work: matter and boundary data fixing curvature at a distance.

**Takeaway:** Split by an observer, the equation becomes Maxwell-like constraint and evolution equations for the electric and magnetic Weyl parts; its vacuum form conserves the Bel–Robinson super-energy and drives the peeling of the radiation field.

*Continues:* `ways_in/cotton-current-and-component-count`<br>*Builds on:* [[weyl-tensor]]<br>*See:* `checks/bel-robinson-divergence`

## Glossary

| Term | Say | In plain words | Concept |
| --- | --- | --- | --- |
| fall freely | — | To move with nothing but gravity acting: no air pushing, and no floor or rope holding you. | — |
| drift | — | How a crumb slowly moves compared with the centre crumb after both are let go at rest, measured with a ruler in the falling cabin. | — |
| room-changing part | — | The part of the drift that is the same in every direction, all in or all out. It makes the room a ball of crumbs takes up start to change, and matter right at the spot sets it. | [[ricci-tensor]] |
| shape-changing part | — | What is left of the drift once the room-changing part is taken away. It stretches a ball of crumbs along one line and squeezes it across by balancing amounts, so the room stays the same at first. | [[weyl-tensor]] |
| Weyl tensor | VILE tensor | The table, kept at every place, that holds the shape-changing part of the drift. | [[weyl-tensor]] |
| uniform | — | Spread evenly, so that every cubic metre holds the same amount of matter. | — |
| room | — | How much a thing takes up; physicists say volume. | — |
| centre crumb | — | The crumb at the centre of the ball. Every other crumb's drift is measured against it, with a ruler fixed to the falling cabin. | — |
| tide | — | The rise and fall of the sea through the day. The shape-changing part at Earth, made by the Moon and the Sun, stretches the sea along the line to each of them. | — |
| box rule | — | The Bianchi identity in words. For an arrow carried around the six faces of any tiny box, the three leftovers add up to nothing. So how curving changes in one direction is tied to how it changes in the other two. | [[bianchi-identity]] |
| weight | — | The pull of a planet on you, as bathroom scales read it while you stand still. | — |

## Key equations

### Weyl divergence equation · working

$$
\nabla^\rho C_{\rho\sigma\mu\nu} = \nabla_{[\mu}R_{\nu]\sigma} - \tfrac16\, g_{\sigma[\nu}\nabla_{\mu]}R
$$

The divergence of the Weyl tensor on its first index is fixed by derivatives of the Ricci tensor and scalar; this is the Bianchi identity with its Ricci part removed.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $C_{\rho\sigma\mu\nu}$ | Weyl tensor, all indices down | the Weyl tensor |
| $R_{\mu\nu},\ R$ | Ricci tensor and Ricci scalar | the Ricci tensor and the Ricci scalar |
| $X_{[\mu\nu]}$ | antisymmetrization, $\tfrac12(X_{\mu\nu} - X_{\nu\mu})$ | antisymmetrized in mu and nu |

**Holds when:** Four dimensions, Levi-Civita connection; no field equation used.  
**Say it:** “The divergence of the Weyl tensor on its first index equals the antisymmetrized derivative of the Ricci tensor, minus one sixth of the metric times the antisymmetrized gradient of the Ricci scalar.”  
**Justified by:** `derivations/divergence-of-the-weyl-decomposition`

### Weyl current from matter · working

$$
\nabla^\rho C_{\rho\sigma\mu\nu} = \frac{8\pi G}{c^4}\Big(\nabla_{[\mu}T_{\nu]\sigma} - \tfrac13\, g_{\sigma[\nu}\nabla_{\mu]}T\Big),\qquad T = g^{\alpha\beta}T_{\alpha\beta}
$$

With Einstein's equation the current is built from derivatives of the stress-energy tensor; a cosmological constant contributes nothing.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $T_{\mu\nu}$ | stress-energy tensor of matter | the stress-energy tensor |
| $T$ | its trace | the trace of the stress-energy tensor |
| $8\pi G/c^4$ | Einstein's constant | eight pi G over c to the fourth |

**Holds when:** Einstein's equation with any cosmological constant; SI units.  
**Say it:** “The divergence of the Weyl tensor equals eight pi G over c to the fourth, times the antisymmetrized derivative of the stress-energy tensor minus one third of the metric times the antisymmetrized gradient of its trace.”  
**Justified by:** `derivations/current-from-einstein-equation`

### Newtonian shadow of the Weyl equation · working

$$
\partial_j E_{ij} = \frac{8\pi G}{3}\,\partial_i\rho,\qquad E_{ij} = \partial_i\partial_j\Phi - \tfrac13\,\delta_{ij}\nabla^2\Phi
$$

In a weak static field the divergence of the trace-free tidal tensor is set by the gradient of the mass density: tidal flux starts where the density changes.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $E_{ij}$ | electric part of the Weyl tensor, the trace-free Newtonian tidal tensor | the trace-free tidal tensor |
| $\Phi$ | Newtonian potential | the Newtonian potential |
| $\rho$ | mass density | the mass density |

**Holds when:** Weak static field, matter at rest, Cartesian coordinates; $E_{ij}$ in units of inverse seconds squared.  
**Say it:** “The divergence of the trace-free tidal tensor equals eight pi G over three times the gradient of the mass density.”  
**Justified by:** `derivations/newtonian-shadow-from-poisson`

### Cotton form in n dimensions · formal

$$
\nabla^\rho C_{\rho\sigma\mu\nu} = (n-3)\big(\nabla_\mu P_{\nu\sigma} - \nabla_\nu P_{\mu\sigma}\big),\qquad P_{\mu\nu} = \frac{1}{n-2}\Big(R_{\mu\nu} - \frac{R}{2(n-1)}\,g_{\mu\nu}\Big)
$$

In any dimension the divergence of the Weyl tensor is n minus three times the Cotton tensor, the antisymmetrized derivative of the Schouten tensor.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $P_{\mu\nu}$ | Schouten tensor | the Schouten tensor |
| $n$ | dimension of the manifold | the dimension |

**Holds when:** Pseudo-Riemannian manifold of dimension at least three with its Levi-Civita connection; $G = c = 1$.  
**Say it:** “The divergence of the Weyl tensor equals n minus three times the antisymmetrized derivative of the Schouten tensor.”  
**Justified by:** `derivations/cotton-form-in-n-dimensions`

## Derivations

### Divergence of the Weyl decomposition · working

**Goal:** Show that $\nabla^\rho C_{\rho\sigma\mu\nu} = \nabla_{[\mu}R_{\nu]\sigma} - \tfrac16 g_{\sigma[\nu}\nabla_{\mu]}R$ in four dimensions.

1. Start from the four-dimensional split $C_{\rho\sigma\mu\nu} = R_{\rho\sigma\mu\nu} - \tfrac12(g_{\rho\mu}R_{\sigma\nu} - g_{\rho\nu}R_{\sigma\mu} + g_{\sigma\nu}R_{\rho\mu} - g_{\sigma\mu}R_{\rho\nu}) + \tfrac{R}{6}(g_{\rho\mu}g_{\sigma\nu} - g_{\rho\nu}g_{\sigma\mu})$.
2. Apply $\nabla^\rho = g^{\rho\alpha}\nabla_\alpha$ to both sides. Metric compatibility, $\nabla g = 0$, lets every metric factor pass through the derivative.
3. Riemann term: the once-contracted Bianchi identity gives $\nabla^\rho R_{\rho\sigma\mu\nu} = \nabla_\mu R_{\sigma\nu} - \nabla_\nu R_{\sigma\mu}$.
4. Ricci block: $\nabla^\rho(g_{\rho\mu}R_{\sigma\nu}) = \nabla_\mu R_{\sigma\nu}$ and $\nabla^\rho(g_{\rho\nu}R_{\sigma\mu}) = \nabla_\nu R_{\sigma\mu}$; the other two, by $\nabla^\rho R_{\rho\mu} = \tfrac12\nabla_\mu R$, give $\tfrac12 g_{\sigma\nu}\nabla_\mu R$ and $\tfrac12 g_{\sigma\mu}\nabla_\nu R$.
5. Scalar block: $\nabla^\rho[R(g_{\rho\mu}g_{\sigma\nu} - g_{\rho\nu}g_{\sigma\mu})] = g_{\sigma\nu}\nabla_\mu R - g_{\sigma\mu}\nabla_\nu R$.
6. Collect: the Ricci-derivative terms carry $1 - \tfrac12 = \tfrac12$, the scalar-gradient terms carry $-\tfrac14 + \tfrac16 = -\tfrac1{12}$.
7. So $\nabla^\rho C_{\rho\sigma\mu\nu} = \tfrac12(\nabla_\mu R_{\sigma\nu} - \nabla_\nu R_{\sigma\mu}) - \tfrac1{12}(g_{\sigma\nu}\nabla_\mu R - g_{\sigma\mu}\nabla_\nu R)$, which is the bracketed form.
8. Check: the $g^{\sigma\mu}$ trace of the right side is $-\tfrac14\nabla_\nu R + \tfrac14\nabla_\nu R = 0$, as the trace-free Weyl tensor requires.

**Result:** $\nabla^\rho C_{\rho\sigma\mu\nu} = \nabla_{[\mu}R_{\nu]\sigma} - \tfrac16\, g_{\sigma[\nu}\nabla_{\mu]}R$, antisymmetric in $\mu\nu$ and trace-free on $\sigma\mu$.

### The current in terms of matter · working

**Goal:** Write the Weyl current in terms of matter and show that the cosmological constant drops out.

1. Take the trace of $G_{\mu\nu} + \Lambda g_{\mu\nu} = \kappa T_{\mu\nu}$ with $\kappa = 8\pi G/c^4$: $-R + 4\Lambda = \kappa T$, so $R = 4\Lambda - \kappa T$.
2. Solve for the Ricci tensor: $R_{\mu\nu} = \kappa(T_{\mu\nu} - \tfrac12 T g_{\mu\nu}) + \Lambda g_{\mu\nu}$.
3. Differentiate: $\nabla_{[\mu}R_{\nu]\sigma} = \kappa(\nabla_{[\mu}T_{\nu]\sigma} - \tfrac12 g_{\sigma[\nu}\nabla_{\mu]}T)$, the $\Lambda g$ term dropping because $\nabla g = 0$ and $\Lambda$ is constant.
4. Likewise $-\tfrac16 g_{\sigma[\nu}\nabla_{\mu]}R = +\tfrac{\kappa}{6}g_{\sigma[\nu}\nabla_{\mu]}T$, the $4\Lambda$ having no gradient.
5. Add: $-\tfrac12 + \tfrac16 = -\tfrac13$, so the current is $\kappa(\nabla_{[\mu}T_{\nu]\sigma} - \tfrac13 g_{\sigma[\nu}\nabla_{\mu]}T)$.
6. In vacuum, $T_{\mu\nu} = 0$, the right side vanishes whatever $\Lambda$ is.

**Result:** $\nabla^\rho C_{\rho\sigma\mu\nu} = \dfrac{8\pi G}{c^4}\big(\nabla_{[\mu}T_{\nu]\sigma} - \tfrac13 g_{\sigma[\nu}\nabla_{\mu]}T\big)$, with no cosmological-constant term.

### The Newtonian shadow from Poisson's equation · working

**Goal:** Show that the electric part of the Weyl tensor in a weak static field obeys $\partial_j E_{ij} = \tfrac{8\pi G}{3}\partial_i\rho$, and that the Weyl current gives the same.

1. In a weak static field $c^2 R_{\hat\imath\hat 0\hat\jmath\hat 0} = \partial_i\partial_j\Phi$; the Weyl tensor removes the trace, so $E_{ij} = c^2 C_{\hat\imath\hat 0\hat\jmath\hat 0} = \partial_i\partial_j\Phi - \tfrac13\delta_{ij}\nabla^2\Phi$.
2. Take the divergence: $\partial_jE_{ij} = \partial_i\nabla^2\Phi - \tfrac13\partial_i\nabla^2\Phi = \tfrac23\partial_i\nabla^2\Phi$.
3. Poisson's equation $\nabla^2\Phi = 4\pi G\rho$ gives $\partial_jE_{ij} = \tfrac{8\pi G}{3}\partial_i\rho$.
4. From the full equation, for dust at rest ($T_{00} = \rho c^2$, $T = -\rho c^2$, $g_{00} = -1$), the $\sigma = 0$, $\mu = i$, $\nu = 0$ component of the current is $\kappa(\tfrac12\partial_i T_{00} - \tfrac16 g_{00}\partial_i T) = \tfrac{\kappa c^2}{3}\partial_i\rho$.
5. The left side is $\partial_j C_{j0i0} = \partial_jE_{ji}/c^2$, so $\partial_jE_{ij} = \tfrac{\kappa c^4}{3}\partial_i\rho = \tfrac{8\pi G}{3}\partial_i\rho$: the same law.

**Result:** $\partial_j E_{ij} = \tfrac{8\pi G}{3}\,\partial_i\rho$: in the Newtonian limit the Weyl equation is a Gauss law whose source is the density gradient.

### The Cotton form in n dimensions · formal

**Goal:** Show that $\nabla^\rho C_{\rho\sigma\mu\nu} = (n-3)(\nabla_\mu P_{\nu\sigma} - \nabla_\nu P_{\mu\sigma})$ for the Schouten tensor $P$.

1. Write $R_{\rho\sigma\mu\nu} = C_{\rho\sigma\mu\nu} + g_{\rho\mu}P_{\sigma\nu} - g_{\rho\nu}P_{\sigma\mu} - g_{\sigma\mu}P_{\rho\nu} + g_{\sigma\nu}P_{\rho\mu}$ with $P_{\mu\nu} = \tfrac{1}{n-2}\big(R_{\mu\nu} - \tfrac{R}{2(n-1)}g_{\mu\nu}\big)$; for $n = 4$ this is the four-dimensional split.
2. Traces: $P = g^{\mu\nu}P_{\mu\nu} = \tfrac{R}{2(n-1)}$ and $R_{\sigma\nu} = (n-2)P_{\sigma\nu} + g_{\sigma\nu}P$.
3. The twice-contracted Bianchi identity $\nabla^\rho R_{\rho\nu} = \tfrac12\nabla_\nu R$ gives $\nabla^\rho P_{\rho\nu} = \tfrac{1}{n-2}\big(\tfrac12 - \tfrac{1}{2(n-1)}\big)\nabla_\nu R = \nabla_\nu P$.
4. Divergence of the split: $\nabla^\rho R_{\rho\sigma\mu\nu} = \nabla^\rho C_{\rho\sigma\mu\nu} + \nabla_\mu P_{\sigma\nu} - \nabla_\nu P_{\sigma\mu} - g_{\sigma\mu}\nabla_\nu P + g_{\sigma\nu}\nabla_\mu P$.
5. The once-contracted identity: $\nabla^\rho R_{\rho\sigma\mu\nu} = \nabla_\mu R_{\sigma\nu} - \nabla_\nu R_{\sigma\mu} = (n-2)(\nabla_\mu P_{\sigma\nu} - \nabla_\nu P_{\sigma\mu}) + g_{\sigma\nu}\nabla_\mu P - g_{\sigma\mu}\nabla_\nu P$.
6. Subtract the two expressions; the $\nabla P$ terms cancel and $(n-2) - 1 = n - 3$ remains.

**Result:** $\nabla^\rho C_{\rho\sigma\mu\nu} = (n-3)\big(\nabla_\mu P_{\nu\sigma} - \nabla_\nu P_{\mu\sigma}\big)$; for $n = 4$ the bracket is the Weyl current, and for $n = 3$ both sides vanish identically.

## Worked examples

### The tidal jump at the surface of a uniform ball · working

**Problem:** A ball of uniform density $\rho$ and radius $R$ sits at rest. Find $E_{ij}$ inside and outside, check the surface jump against the divergence law, and evaluate it for Earth's mean density, $5.51\times10^3$ kilograms per cubic metre.

1. Inside, $\Phi = \tfrac{2\pi G\rho}{3}r^2 + \text{const}$, so $\partial_i\partial_j\Phi = \tfrac{4\pi G\rho}{3}\delta_{ij}$: pure trace. Hence $E_{ij} = 0$ inside.
2. Outside, $\Phi = -GM/r$ with $M = \tfrac{4\pi}{3}\rho R^3$, so $E_{ij} = \partial_i\partial_j\Phi = \tfrac{GM}{r^3}(\delta_{ij} - 3n_in_j)$, already trace-free; along the radius $E_{rr} = -2GM/r^3$.
3. At $r = R^+$, $E_{rr} = -2GM/R^3 = -\tfrac{8\pi G}{3}\rho$; at $R^-$ it is zero. The radial component jumps by $-\tfrac{8\pi G}{3}\rho$ going outward.
4. Across the surface, $\partial_jE_{rj}$ has the delta-function piece $[E_{rr}]\,\delta(r - R)$ and $\tfrac{8\pi G}{3}\partial_r\rho = -\tfrac{8\pi G}{3}\rho\,\delta(r - R)$: they agree.
5. Numerically, $\tfrac{8\pi G}{3}\rho = \tfrac{8\pi \times 6.674\times10^{-11}\times 5513}{3} = 3.08\times10^{-6}$ per second squared: crumbs one metre apart along the radius separate with relative acceleration $3.1\times10^{-6}$ metres per second squared.

**Answer:** $E_{ij} = 0$ inside; $E_{ij} = \tfrac{GM}{r^3}(\delta_{ij} - 3n_in_j)$ outside; the radial component jumps by $-\tfrac{8\pi G}{3}\rho \approx -3.1\times10^{-6}$ per second squared at the surface, exactly the source the divergence law places there.

**Takeaway:** The Weyl current lives where the density changes; a uniform body sources its exterior tidal field entirely at its surface.

## Problems

### `centre-and-three-radii` · entry · difficulty 1 · conceptual

A made-up planet is a round, uniform cloud of dust, let go so that it all falls freely toward its centre. One ball of crumbs is let go at rest by someone falling with the dust at the planet's centre. Another is let go the same way three planet-radii from the centre, two radii above the surface. Say what each ball does. Then compare the shape change at the far ball with the shape change just above the surface: one third, one ninth, or one twenty-seventh?

**Hints**

1. Is there matter at the spot where each ball is let go?
2. Twice as far gives one eighth. What does three times as far give?

**Answer:** At the centre the ball shrinks and keeps its shape. Three radii out it keeps its room at first and changes shape: it stretches along the line to the centre and squeezes across it. The shape change there is one twenty-seventh of the shape change just above the surface.

**Must contain:** At the centre: shrinks, keeps its shape; Three radii out: keeps its room, changes shape; One twenty-seventh

**Numeric:** shape change at three radii as a fraction of the surface value = 0.037 1 (magnitude, ±10%)

**Solution**

1. At the centre, dust at the spot sets a room-changing part: the ball shrinks. The planet is uniform, so its pull grows in step with distance from the centre, and every pair of crumbs drifts together by the same amount: the shape does not change.
2. Three radii out there is no matter at the spot, so there is no room-changing part. The shape-changing part, handed on from the surface, stretches the ball along the line to the centre and squeezes it across.
3. The shape change fades to one eighth each time the distance doubles, because it divides by the distance times itself three times over. Three times as far gives one over three times three times three, one twenty-seventh.

**Targets:** `stretch-is-strongest-where-matter-is`, `stretch-fades-like-weight`

### `inverse-cube-from-balance` · working · difficulty 2 · calculation

Outside a round body at rest, the trace-free tidal tensor must have the form $E_{ij} = A(r)(\delta_{ij} - 3n_in_j)$ with $\mathbf n$ the radial unit vector. (a) Impose the vacuum divergence law $\partial_jE_{ij} = 0$ and find $A(r)$ up to a constant. (b) The body is a uniform ball of radius $R$ and density $\rho$. Use the jump condition at its surface to fix the constant. (c) A satellite orbits at $r = 3R$. Find the relative acceleration of two test masses one metre apart along the radius there, for a ball of Earth's mean density, $5.51\times10^3$ kilograms per cubic metre.

**Hints**

1. Use $\partial_j n_i = (\delta_{ij} - n_in_j)/r$ and $\partial_j n_j = 2/r$.
2. Inside a uniform ball $E_{ij} = 0$; the radial component outside is $E_{rr} = -2A$.

**Answer:** (a) $rA' + 3A = 0$, so $A = K/r^3$. (b) $E_{rr}$ jumps from $0$ to $-\tfrac{8\pi G}{3}\rho$ at $r = R$, so $K = \tfrac{4\pi G}{3}\rho R^3 = GM$ and $E_{ij} = \tfrac{GM}{r^3}(\delta_{ij} - 3n_in_j)$. (c) At $r = 3R$, $|E_{rr}| = \tfrac{8\pi G\rho}{3\cdot 27} = 1.14\times10^{-7}$ per second squared: the masses separate with relative acceleration $1.1\times10^{-7}$ metres per second squared.

**Must contain:** Divergence-free plus spherical symmetry forces A proportional to one over r cubed; The surface jump fixes the constant as G M; One twenty-seventh of the surface value at three radii

**Numeric:** relative acceleration of two masses one metre apart along the radius at three radii = 1.14e-07 m/s^2 (magnitude, ±5%)

**Solution**

1. (a) $\partial_j[A(\delta_{ij} - 3n_in_j)] = A'n_j(\delta_{ij} - 3n_in_j) - 3A(n_j\partial_jn_i + n_i\partial_jn_j) = A'(n_i - 3n_i) - 3A(0 + 2n_i/r) = -(2A' + 6A/r)n_i$. Setting this to zero gives $rA' + 3A = 0$, whose solution is $A = K/r^3$.
2. (b) Inside, $\partial_i\partial_j\Phi = \tfrac{4\pi G\rho}{3}\delta_{ij}$ is pure trace, so $E_{ij} = 0$. Across the surface, where $\partial_r\rho = -\rho\,\delta(r - R)$, the divergence law makes $E_{rr}$ jump by $-\tfrac{8\pi G}{3}\rho$. Since $E_{rr} = -2A$, $A(R^+) = \tfrac{4\pi G}{3}\rho$ and $K = GM$.
3. (c) $|E_{rr}(3R)| = \tfrac{2GM}{27R^3} = \tfrac{8\pi G\rho}{81} = 1.14\times10^{-7}$ per second squared: over one metre, a relative acceleration of $1.14\times10^{-7}$ metres per second squared, one twenty-seventh of the surface value.

**Targets:** `stretch-fades-like-weight`

### `static-fluid-current` · formal · difficulty 3 · derivation

With $G = c = 1$, a perfect fluid $T_{\mu\nu} = (\rho + p)u_\mu u_\nu + p\,g_{\mu\nu}$ is at rest in a static spacetime, so that $\nabla_\mu u_\nu = -u_\mu a_\nu$ and $(\rho + p)a_\nu = -D_\nu p$, with $D$ the derivative projected orthogonally to $u$. Show that $J_{\sigma\mu\nu} = 8\pi\big(u_\sigma u_{[\nu}D_{\mu]}\rho + \tfrac13 g_{\sigma[\nu}D_{\mu]}\rho\big)$, so the pressure gradient drops out, and say what follows inside a star of uniform density.

**Hints**

1. Expand $\nabla_\mu T_{\nu\sigma}$ and antisymmetrize in $\mu\nu$; the term $u_\mu u_\nu \partial_\sigma p$ is symmetric and drops.
2. The trace is $T = -\rho + 3p$; the static condition makes $u^\lambda\partial_\lambda\rho = u^\lambda\partial_\lambda p = 0$.
3. Collect the pressure terms from the $\nabla T$ block and from the trace block separately.

**Answer:** $J_{\sigma\mu\nu} = 8\pi\big(u_\sigma u_{[\nu}D_{\mu]}\rho + \tfrac13 g_{\sigma[\nu}D_{\mu]}\rho\big)$: only the density gradient sources the Weyl tensor. Inside a uniform-density star $J = 0$, so the Weyl divergence vanishes there, consistent with the interior solution being conformally flat, and the exterior Weyl tensor is switched on at the surface where $\rho$ drops.

**Must contain:** Pressure terms cancel between the derivative block and the trace block; The acceleration term equals the pressure gradient by hydrostatic equilibrium; Only the density gradient remains; zero current inside a uniform star

**Solution**

1. Differentiate: $\nabla_\mu T_{\nu\sigma} = \partial_\mu(\rho + p)u_\nu u_\sigma + (\rho + p)(\nabla_\mu u_\nu)u_\sigma + (\rho + p)u_\nu\nabla_\mu u_\sigma + \partial_\mu p\,g_{\nu\sigma}$.
2. Insert $\nabla_\mu u_\nu = -u_\mu a_\nu$ and $(\rho + p)a_\nu = -\partial_\nu p$ (static, so $\partial_\nu p = D_\nu p$): the second term is $u_\mu u_\sigma\partial_\nu p$ and the third is $u_\mu u_\nu\partial_\sigma p$.
3. Antisymmetrize in $\mu\nu$. The third term is symmetric and drops. The first and second give $u_\sigma(u_{[\nu}\partial_{\mu]}\rho + u_{[\nu}\partial_{\mu]}p + u_{[\mu}\partial_{\nu]}p) = u_\sigma u_{[\nu}\partial_{\mu]}\rho$. The fourth gives $g_{\sigma[\nu}\partial_{\mu]}p$.
4. Trace block: $T = -\rho + 3p$, so $-\tfrac13 g_{\sigma[\nu}\nabla_{\mu]}T = \tfrac13 g_{\sigma[\nu}\partial_{\mu]}\rho - g_{\sigma[\nu}\partial_{\mu]}p$.
5. Add the blocks: the pressure terms $g_{\sigma[\nu}\partial_{\mu]}p$ cancel, leaving $J_{\sigma\mu\nu} = 8\pi\big(u_\sigma u_{[\nu}D_{\mu]}\rho + \tfrac13 g_{\sigma[\nu}D_{\mu]}\rho\big)$.
6. Check: for $\sigma = 0$, $\mu = i$, $\nu = 0$ with $u_0 = g_{00} = -1$ the bracket is $(\tfrac12 - \tfrac16)D_i\rho$, matching the Newtonian shadow $\tfrac{8\pi}{3}\partial_i\rho$.
7. For uniform density $D\rho = 0$ inside, so $J = 0$: the Weyl divergence vanishes throughout the interior, in agreement with the conformal flatness of the constant-density interior solution, and the Weyl tensor of the exterior is switched on at the surface.

**Targets:** `source-is-matter-not-its-change`

## Observations

- **The Sun raises a smaller ocean tide than the Moon although it pulls Earth far harder; spring and neap tides show both at work.** (measured, working). Tides are the electric part of the Weyl tensor at Earth, sourced at the Sun and Moon and carried across empty space by the source-free equation, which with spherical symmetry gives the inverse cube; the pull falls only as the inverse square. *Numbers:* Pull ratio Sun to Moon $(M_\odot/M_{\rm Moon})(d_{\rm Moon}/d_\odot)^2 = 179$; tidal ratio $(M_\odot/M_{\rm Moon})(d_{\rm Moon}/d_\odot)^3 = 0.46$; distance ratio $389$.
- **Gravitational waves from the binary black hole merger GW150914, measured by LIGO.** (measured, working). Far from the source the Weyl tensor obeys the vacuum equation and propagates as a wave. The detectors read its electric part: the relative acceleration of their mirrors is $-E_{ij}\xi^j$ with $E_{ij} = -\tfrac12\ddot h_{ij}$. *Numbers:* Peak strain $1.0\times10^{-21}$ near $150$ hertz gives $|E| \approx \tfrac12 h(2\pi f)^2 = 4.4\times10^{-16}$ per second squared: a relative acceleration of $1.8\times10^{-12}$ metres per second squared between mirrors $4$ kilometres apart. *Reference:* B. P. Abbott, R. Abbott, T. D. Abbott, M. R. Abernathy and others (2016), *Observation of Gravitational Waves from a Binary Black Hole Merger*, Physical Review Letters 116, 061102, doi:10.1103/PhysRevLett.116.061102

## Teaching arc

1. **Ask where the shape change starts** (entry). Set up the uniform dust-cloud planet, let go so that it falls freely, ask for a prediction about a ball of crumbs deep inside, then reveal that it only shrinks and that the shape change appears at the surface. *Why:* The surprise that dust all around gives no shape change makes the source, a change in matter, memorable. *Predict:* Deep inside a round, uniform planet, with dust all around, does a ball of crumbs change its shape more than it does just outside the planet? *Visual:* [[falling-ring-of-crumbs]] *Uses:* `ways_in/shape-change-starts-at-the-surface`, `checks/crumbs-at-the-centre-and-halfway`
2. **Hand the shape change across empty space** (entry). Restate the box rule, remove the room-changing part, and show that empty space can only pass the shape change on; then have the learner predict the fading and count the eighth as a difference of pulls. *Why:* The identity becomes the reason matter shapes curving far away, and the one-eighth rule a consequence rather than a fact. *Predict:* At twice the distance from the planet's centre, is the shape change a half, a quarter, or an eighth of its value at the surface? *Visual:* [[cube-of-small-loops]] *Uses:* `ways_in/empty-space-hands-it-on`, `ways_in/fading-faster-than-weight`, `checks/twice-as-far-one-eighth`
3. **Derive the equation and its Newtonian shadow** (working). Take the divergence of the Weyl decomposition, substitute Einstein's equation, then reduce to the tidal divergence law and work the uniform-ball jump. *Why:* The same equation seen as identity, as matter, and as Newton fixes what the current is and is not. *Uses:* `ways_in/split-riemann-and-take-the-divergence`, `derivations/divergence-of-the-weyl-decomposition`, `derivations/newtonian-shadow-from-poisson`, `worked_examples/jump-at-the-surface-of-a-uniform-ball`
4. **Contrast with Einstein's equation** (working). Put Maxwell's equation, the Weyl equation and Einstein's equation side by side, and ask which carries curvature away from its source and whether a cosmological constant sources anything. *Why:* Learners pair Einstein's equation with Maxwell's; the algebraic-versus-differential contrast corrects that. *Predict:* Dark energy fills all space with energy. Does it feed the Weyl current? *Uses:* `ways_in/gravitys-maxwell-equation`, `checks/which-equation-propagates`, `analogies/gauss-law-for-charge`
5. **Cotton form, count, conservation, vacuum** (formal). Redo the derivation with the Schouten tensor in n dimensions, count the components, prove the current is conserved, and derive the vacuum wave equation and the static-fluid reduction. *Why:* The formal rung owns the hypotheses, exact content and limits of the identity. *Uses:* `ways_in/cotton-current-and-component-count`, `checks/count-the-components`, `checks/current-is-conserved`, `problems/static-fluid-current`
6. **The 1+3 split and beyond** (research). Project the equation with an observer field into constraints and evolution equations for the electric and magnetic parts, then present Bel–Robinson conservation and peeling as vacuum consequences. *Why:* Shows the equation at work in cosmology, mathematical relativity and radiation theory. *Uses:* `ways_in/electric-magnetic-split-and-super-energy`, `checks/bel-robinson-divergence`

## Analogies

### Gauss's law for electric charge · working

Gauss's law $\nabla\cdot\mathbf E = \rho_{\rm e}/\varepsilon_0$ says electric flux starts on charge, is source-free in empty space, and by symmetry falls as the inverse square around a point charge. The Newtonian shadow $\partial_jE_{ij} = \tfrac{8\pi G}{3}\partial_i\rho$ says the same for each row of the trace-free tidal tensor, with the density gradient as charge and the inverse cube around a round body.

| In the analogy | Stands for |
| --- | --- |
| the electric field | a row of the trace-free tidal tensor $E_{ij}$ |
| charge density | the gradient of the mass density |
| Maxwell's conserved current | the Weyl current, conserved identically |

*Limits:* The full equation is nonlinear and couples the electric part to a magnetic part; the rows of $E_{ij}$ are not independent fields; and the row-by-row Gauss law holds only in the weak static limit.

## Misconceptions

### “The shape change is strongest deep inside a planet, where the most matter is around you.” · entry · `stretch-is-strongest-where-matter-is`

- **Why it is tempting:** Matter causes gravity, so more matter nearby should mean more of every gravitational effect.
- **What is true:** Inside a round, uniform planet a ball of crumbs only shrinks; matter at the spot sets the room-changing part only. The shape change is made where the amount of matter changes, at the surface.
- **Exposed by:** `checks/crumbs-at-the-centre-and-halfway`

### “Twice as far from a planet, the shape change is a quarter as strong, like weight.” · entry · `stretch-fades-like-weight`

- **Why it is tempting:** Weight is the only gravitational fading most people know.
- **What is true:** The shape change is the difference of pulls across the ball of crumbs, so it fades one step faster: one eighth at twice the distance. That is why the Sun's tide is smaller than the Moon's.
- **Exposed by:** `checks/twice-as-far-one-eighth`

### “The Weyl current is the stress-energy tensor, so wherever there is matter there is a source of Weyl curvature.” · working · `source-is-matter-not-its-change`

- **Why it is tempting:** Einstein's equation has the stress-energy tensor on its right-hand side.
- **What is true:** The current is built from derivatives of the stress-energy tensor; where it is covariantly constant, as inside a uniform body at rest, the current vanishes. Only changes of matter, such as a surface, source the Weyl tensor.
- **Exposed by:** `checks/which-equation-propagates`

### “Einstein's equation is gravity's version of Maxwell's equations: field on the left, source on the right.” · working · `einstein-equation-is-the-maxwell-analogue`

- **Why it is tempting:** Both are presented as the field equations of their theories, with sources on the right-hand side.
- **What is true:** Einstein's equation is algebraic in the Ricci part and fixes curvature at the same event as its source. The Maxwell-like differential equation is the Weyl divergence equation, whose vacuum solutions carry curvature away from matter.
- **Exposed by:** `checks/which-equation-propagates`

### “The Weyl current is conserved only when Einstein's equation holds, as a consequence of energy conservation.” · formal · `conservation-needs-the-field-equation`

- **Why it is tempting:** Maxwell's current is conserved because charge is conserved, a physical law.
- **What is true:** The current's divergence vanishes identically for any metric, by the Ricci identity and the pair symmetry of the Riemann tensor. No field equation is used.
- **Exposed by:** `checks/current-is-conserved`

## Checks

1. **Entry · predict** `checks/crumbs-at-the-centre-and-halfway`. Picture a made-up planet: a huge round cloud of dust, uniform, holding as much matter in each cubic metre as Earth does on average. It is let go at one moment, so that it all falls freely toward its centre. A cabin falls with the dust, and inside it a ball of crumbs is let go at rest. Predict what the ball does when the cabin is halfway from the surface to the centre, and again at the centre. Then the ball is let go the same way just above the surface. Does it shrink there, and does it change shape? Inside the planet, how far do two crumbs a metre apart move toward each other in one minute: about three millimetres, three centimetres, or three metres?
   - **Hints:** Is there dust at the spot where the ball is let go? / Inside a uniform cloud, the pull halfway out is half the pull at the surface.
   - **Answer:** Halfway from the surface to the centre and at the centre the ball does the same thing: it shrinks and keeps its shape. It shrinks because dust at the spot sets a room-changing part. It keeps its shape because a uniform cloud pulls in step with distance from its centre. Seen from the centre crumb, that is a pull toward the centre crumb which is the same in every direction. So every pair of crumbs drifts together by the same amount. For a planet holding as much matter in each cubic metre as Earth does on average, two crumbs a metre apart move about three millimetres closer in the first minute. Just above the surface no dust sits at the spot, so the ball does not shrink. It changes shape. Crumbs along the line to the centre drift apart, about five millimetres in a minute. Crumbs across that line drift together, about three millimetres.
   - **Must contain:** Inside, the ball shrinks and keeps its shape, the same halfway down and at the centre; Just outside, it keeps its room and changes shape; About three millimetres in a minute inside
   - **Numeric:** distance two crumbs a metre apart move toward each other inside the planet in one minute = 2.8 mm (magnitude, ±0.6)
   - **Targets:** `stretch-is-strongest-where-matter-is`
   - **Visual:** [[falling-ring-of-crumbs]]
2. **Entry · numeric** `checks/twice-as-far-one-eighth`. A satellite circles a round planet at twice the surface's distance from the centre. Compared with the shape change just above the surface, how strong is it at the satellite: one half, one quarter, or one eighth? If the satellite were held still there on scales, what fraction of its surface weight would they read?
   - **Hints:** Weight falls to one quarter when the distance doubles. Does the shape change fall by more?
   - **Answer:** One eighth. Around a round planet, the box rule for the shape-changing part makes the shape change fall to one eighth each time the distance from the centre doubles. Weight falls to one quarter, so the scales read one quarter. The shape change fades faster than weight because it is the difference of pulls across the ball. The pulls fall to a quarter, and the ball's width becomes half as big a part of the distance. That is why the Sun raises a smaller tide than the Moon. It pulls Earth about 180 times harder, but it is about 390 times farther away. Compare pull divided by distance: 180 divided by 390 is a bit less than one half.
   - **Must contain:** One eighth for the shape change; One quarter for weight; The shape change fades faster than weight
   - **Numeric:** shape change at twice the distance as a fraction of the surface value = 0.125 1 (magnitude, ±5%); weight at twice the distance as a fraction of the surface value = 0.25 1 (magnitude, ±5%)
   - **Targets:** `stretch-fades-like-weight`
3. **Working · evaluate-claim** `checks/which-equation-propagates`. Evaluate the claim: "Einstein's equation is the gravitational counterpart of Maxwell's equations, because both put the field on the left and the source on the right." Say also what the source of the Maxwell-like equation is inside a uniform body at rest.
   - **Hints:** Which of the two equations has derivatives of curvature in it?
   - **Answer:** The claim mistakes the roles. Maxwell's equation is differential: its solutions carry the field into empty space, away from the current. Einstein's equation is algebraic in the Ricci tensor: it fixes ten curvature components at an event from the stress-energy at that same event, and says nothing directly about the ten Weyl components, which describe curvature in empty space. The counterpart of Maxwell's equation is the Weyl divergence equation, whose current is built from derivatives of the stress-energy tensor and whose vacuum form gives a wave equation. Inside a uniform body at rest that current is zero; the source sits on the surface, where the density changes.
   - **Must contain:** Einstein's equation is algebraic and local in the Ricci part; The Weyl divergence equation is the differential, Maxwell-like one; Its current is a derivative of the stress-energy tensor, zero inside a uniform body
   - **Targets:** `einstein-equation-is-the-maxwell-analogue`, `source-is-matter-not-its-change`
4. **Formal · explain** `checks/count-the-components`. How many independent components does the Weyl divergence equation have in four dimensions, and how does that number sit inside the once-contracted Bianchi identity?
   - **Hints:** Which algebraic conditions does the left side satisfy automatically?
   - **Answer:** $J_{\sigma\mu\nu}$ is antisymmetric in $\mu\nu$: $4\times6 = 24$ slots. Its totally antisymmetric part vanishes, removing $4$, and its trace $g^{\sigma\mu}J_{\sigma\mu\nu}$ vanishes, removing $4$ more: $16$ components, and the left side has the same symmetries. The once-contracted identity has $24 - 4 = 20$ components: its trace-free part is the Weyl equation, $16$, and its trace is the contracted Bianchi identity $\nabla^\mu G_{\mu\nu} = 0$, $4$.
   - **Must contain:** Twenty-four minus four cyclic minus four trace gives sixteen; Sixteen plus the four of the contracted identity is twenty
   - **Numeric:** independent components of the Weyl divergence equation in four dimensions = 16 1 (magnitude, ±0)
5. **Formal · derive** `checks/current-is-conserved`. Show that $\nabla^\sigma J_{\sigma\mu\nu} = 0$ for the Weyl current $J_{\sigma\mu\nu} = \nabla_{[\mu}R_{\nu]\sigma} - \tfrac16 g_{\sigma[\nu}\nabla_{\mu]}R$, without using any field equation.
   - **Hints:** Write $\nabla^\sigma\nabla_\mu R_{\nu\sigma}$ as $\nabla_\mu\nabla^\sigma R_{\nu\sigma}$ plus a commutator.
   - **Answer:** The scalar block gives $-\tfrac1{12}(\nabla_\nu\nabla_\mu R - \nabla_\mu\nabla_\nu R) = 0$. In the Ricci block, $\nabla^\sigma\nabla_\mu R_{\nu\sigma} = \tfrac12\nabla_\mu\nabla_\nu R + g^{\sigma\alpha}(-R^\lambda{}_{\nu\alpha\mu}R_{\lambda\sigma} - R^\lambda{}_{\sigma\alpha\mu}R_{\nu\lambda})$ by the Ricci identity. The first commutator term is $-R_{\lambda\nu\sigma\mu}R^{\lambda\sigma}$, symmetric in $\mu\nu$ by pair symmetry; the second is $+R_{\mu\lambda}R^\lambda{}_\nu$, symmetric too. Antisymmetrizing in $\mu\nu$ kills both and the $\nabla\nabla R$ term, so $\nabla^\sigma J_{\sigma\mu\nu} = 0$ for every metric.
   - **Must contain:** Commute the derivatives with the Ricci identity; Both curvature-squared terms are symmetric in mu nu; The antisymmetrization removes everything; no field equation needed
   - **Targets:** `conservation-needs-the-field-equation`
6. **Research · explain** `checks/bel-robinson-divergence`. Why is the Bel–Robinson tensor divergence-free in vacuum, and why does that not make it a local energy density of the gravitational field?
   - **Hints:** Which two first-order conditions on the Weyl tensor hold in vacuum?
   - **Answer:** Its divergence is a sum of terms $(\nabla C)\,C$ and $(\nabla\,{}^*C)\,{}^*C$, in which each derivative appears as the divergence $\nabla^\rho C_{\rho\sigma\mu\nu}$ or, through the dual, as the cyclic derivative $\nabla_{[\lambda}C_{\rho\sigma]\mu\nu}$. In vacuum both vanish, and because the two duals of the Weyl tensor coincide they are one condition; so $\nabla^\alpha T_{\alpha\beta\gamma\delta} = 0$ whenever $R_{\mu\nu} = \Lambda g_{\mu\nu}$. It is not an energy density: quadratic in curvature, it has the dimension of inverse length to the fourth, and it enters no conservation law with matter. It is a super-energy, non-negative when contracted with future-directed timelike vectors, which is what estimates need.
   - **Must contain:** Divergence reduces to the vacuum Weyl equation and its dual; Vanishes for Ricci equal to Lambda times the metric; Wrong dimension for an energy density

## Notation traps

| Issue | Course choice | Variants you will meet |
| --- | --- | --- |
| Index of the divergence and sign of the current | The divergence is on the first index: $\nabla^\rho C_{\rho\sigma\mu\nu} = \nabla_{[\mu}R_{\nu]\sigma} - \tfrac16 g_{\sigma[\nu}\nabla_{\mu]}R$, with $X_{[\mu\nu]} = \tfrac12(X_{\mu\nu} - X_{\nu\mu})$ and Einstein's constant $8\pi G/c^4$. | Some texts contract the last index and write $C^{\mu\nu\alpha\beta}{}_{;\beta} = J^{\mu\nu\alpha}$ with $J^{\mu\nu\alpha} = R^{\alpha[\mu;\nu]} + \tfrac16 g^{\alpha[\nu}R^{;\mu]}$; by the Weyl symmetries this is the same equation, the sign of the moved contraction absorbed by the reversed bracket. |
| Sign and index order of the Cotton tensor | $P_{\mu\nu} = \tfrac{1}{n-2}\big(R_{\mu\nu} - \tfrac{R}{2(n-1)}g_{\mu\nu}\big)$ and the Cotton tensor is the bracket $\nabla_\mu P_{\nu\sigma} - \nabla_\nu P_{\mu\sigma}$, so that $\nabla^\rho C_{\rho\sigma\mu\nu} = (n-3)$ times it. | Some texts define the Cotton tensor with the opposite sign, with the free index first, or with the factor $n - 2$ absorbed into the Schouten tensor. Check the index placement and sign before comparing. |

## Visuals

- [[falling-ring-of-crumbs]] (core): The entry experience: a ball of crumbs let go inside and outside a uniform dust-cloud planet that falls freely in on itself, shrinking with unchanged shape inside and changing shape only outside. *Sketch:* This concept adds a dust-cloud mode: a see-through uniform cloud of dust with a sharp surface, just let go so that it falls freely toward its centre, and a slider that moves the cabin, falling with the dust, from the centre out to three radii. No shaft or cavity: a hollow shaft inside a solid body changes the drift there, so the cabin must sit among the dust. The two-part readout of the ball mode stays on: inside, the same-in-every-direction arrows are steady and the shape-change arrows read zero; crossing the surface, the shape-change arrows switch on and the uniform arrows vanish; outside, the shape-change readout falls as the inverse cube, with a marker at two radii reading one eighth. A density-profile toggle swaps the uniform cloud for one with a dense core, where a small shape change appears inside the outer layer.
- [[cube-of-small-loops]] (supporting): The box rule with its room-changing part greyed out, leaving the balance of the shape-changing part. *Sketch:* This concept adds a split toggle beside the leftover readouts: each leftover is shown as a room-changing piece plus a shape-changing piece. In the space around a star at one moment the room-changing pieces are zero and the three shape-changing pieces still sum to zero; a second scene inside a uniform ball shows the opposite.

## Tutor moves

**Open with**

- Picture a made-up planet that is a huge round cloud of dust, spread evenly. It is let go, so it all falls freely toward its centre. You fall with the dust in a cabin and let go of a ball of crumbs deep inside, with dust all around. Does the ball change its shape more there than just outside the cloud, where there is no dust at all? *(prediction)*

**If the learner is stuck**

- *The learner insists that dust all around must stretch the ball somehow.* → Say how a uniform cloud pulls: nothing at the centre, half of the surface pull halfway out. Then show that two crumbs a metre apart, along the line to the centre or across it, drift together by the same fixed amount. *Uses:* `ways_in/shape-change-starts-at-the-surface`, `checks/crumbs-at-the-centre-and-halfway`
- *The learner cannot see how a derivative of the Ricci tensor becomes a derivative of the stress-energy tensor.* → Trace-reverse Einstein's equation first; every metric factor and the constant pass through the covariant derivative, so only derivatives of the stress-energy tensor and its trace survive. *Uses:* `derivations/current-from-einstein-equation`

**Common questions**

- *If the shape change is made only where the amount of matter changes, what happens inside a planet made of layers, like Earth with its dense core?* (entry) Then there is some shape change inside too. The box rule adds up the changes of matter from the centre outward. At a spot, the result is one comparison. Take how much matter the cubic metres closer to the centre hold on average. Set it against how much the cubic metre right there holds. Where a dense core sits under lighter rock, the rock above is stretched along the line to the centre. In a uniform planet the two amounts are equal, so the comparison gives nothing. *Uses:* `ways_in/shape-change-starts-at-the-surface`
- *Why is the source a derivative of the stress-energy tensor and not the stress-energy tensor itself?* (working) Einstein's equation has already spent $T_{\mu\nu}$ on the Ricci part, algebraically. The Bianchi identity relates derivatives of curvature, so the Weyl part is tied to derivatives of matter. Dimensions agree: $\nabla C$ and $(8\pi G/c^4)\nabla T$ are both inverse lengths cubed. *Uses:* `ways_in/split-riemann-and-take-the-divergence`, `derivations/newtonian-shadow-from-poisson`
- *Is the Weyl equation an evolution equation for the Weyl tensor?* (formal) By itself it is an identity satisfied by every metric, so it determines nothing. With the Ricci part fixed by matter and an observer field chosen, its projections split into constraints and evolution equations for the electric and magnetic parts; the system closes only with the equations for the observer field's kinematics. *Uses:* `ways_in/cotton-current-and-component-count`, `ways_in/electric-magnetic-split-and-super-energy`

**Switching levels**

- To working when: asks for the formula behind the one-eighth rule; mentions Poisson's or Gauss's law. Derive the Newtonian shadow first, then climb to the full divergence equation. *Uses:* `ways_in/gravitys-maxwell-equation`, `derivations/newtonian-shadow-from-poisson`
- To formal when: asks about other dimensions, the number of equations, or conservation of the current. Go to the Cotton form, count the components, and prove conservation. *Uses:* `ways_in/cotton-current-and-component-count`, `checks/count-the-components`
- To research when: asks about electric and magnetic parts, Bel–Robinson, or numerical relativity. Present the 1+3 split and the super-energy. *Uses:* `ways_in/electric-magnetic-split-and-super-energy`, `checks/bel-robinson-divergence`

**Pronunciations:** Weyl → VILE; Bianchi → bee-AHN-kee; Schouten → SKHOW-ten; Szekeres → SEH-keh-resh

**Voice notes:** At the entry rung say only shape change and room change; keep tensor and current for the working rung. Read square brackets as antisymmetrized in the two indices named.

## History

- **Hermann Weyl (1918).** Introduced the conformal curvature tensor, the trace-free part of the Riemann tensor that is unchanged by rescaling the metric. Hermann Weyl (1918), *Reine Infinitesimalgeometrie*, Mathematische Zeitschrift 2, 384–411, doi:10.1007/BF01199420
- **Achille Matte (1953).** Split the vacuum curvature into electric and magnetic parts and wrote the vacuum Bianchi identities in a form modelled on Maxwell's equations. Achille Matte (1953), *Sur de nouvelles solutions oscillatoires des équations de la gravitation*, Canadian Journal of Mathematics 5, 1–16, doi:10.4153/CJM-1953-001-3
- **Stephen Hawking (1966).** Used the Weyl-tensor form of the Bianchi identities to follow perturbations of an expanding universe without a background metric. S. W. Hawking (1966), *Perturbations of an expanding universe*, Astrophysical Journal 145, 544–554, doi:10.1086/148793
- **George Ellis (1971).** Systematized the 1+3 covariant form of the equation: divergence and evolution equations for the electric and magnetic parts of the Weyl tensor in a fluid. G. F. R. Ellis (1971), *Relativistic cosmology*, General Relativity and Cosmology, Proceedings of the International School of Physics Enrico Fermi, Course XLVII, ed. R. K. Sachs, Academic Press, 104–182; reprinted in General Relativity and Gravitation 41, 581–660 (2009), doi:10.1007/s10714-009-0760-7

## Research horizon

- **The 1+3 covariant approach to cosmology.** The projected Weyl equations are the backbone of the covariant treatment of large-scale structure: the electric part is the tidal field that drives collapse, the magnetic part carries gravitational waves and frame effects, and their constraints and evolution equations are studied for consistency, as in the silent-universe problem. Christos G. Tsagas, Anthony Challinor, Roy Maartens (2008), *Relativistic cosmology and large-scale structure*, Physics Reports 465, 61–147, doi:10.1016/j.physrep.2008.03.003; Roy Maartens, Bruce A. Bassett (1998), *Gravito-electromagnetism*, Classical and Quantum Gravity 15, 705–717, doi:10.1088/0264-9381/15/3/018; Henk van Elst, Claes Uggla, William M. Lesame, George F. R. Ellis, Roy Maartens (1997), *Integrability of irrotational silent cosmological models*, Classical and Quantum Gravity 14, 1151–1162, doi:10.1088/0264-9381/14/5/018
- **Bel–Robinson super-energy and nonlinear stability.** The vacuum Weyl equation conserves the Bel–Robinson tensor, and the energy estimates built on it, with the Bianchi identities treated as a Maxwell-like system for the Weyl tensor, are the engine of the proof that Minkowski space is stable under small perturbations. Demetrios Christodoulou, Sergiu Klainerman (1993), *The Global Nonlinear Stability of the Minkowski Space*, Princeton Mathematical Series 41, Princeton University Press; José M. M. Senovilla (2000), *Super-energy tensors*, Classical and Quantum Gravity 17, 2799–2841, doi:10.1088/0264-9381/17/14/313
- **Peeling of the Weyl tensor at null infinity.** Integrated along outgoing null rays, the Bianchi identities for the Weyl tensor give the peeling theorem: the components in a null frame fall off with successive powers of the distance, and the slowest, the radiation field, is what gravitational-wave detectors read. Rainer K. Sachs (1962), *Gravitational waves in general relativity. VIII. Waves in asymptotically flat space-time*, Proceedings of the Royal Society A 270, 103–126, doi:10.1098/rspa.1962.0206; Ezra Newman, Roger Penrose (1962), *An approach to gravitational radiation by a method of spin coefficients*, Journal of Mathematical Physics 3, 566–578, doi:10.1063/1.1724257

## Review: novice

**Verdict:** fixed (2026-09-16, revision 4)

**Retell attempt:** Next to a planet there's nothing there, but a ball of crumbs still gets stretched, and this note is about where that stretching comes from. If the planet is the same all the way through, a ball of crumbs deep inside only shrinks, it doesn't change shape, and the shape change only switches on at the surface where the rock stops. I'm not sure why it doesn't change shape inside, something about weight being half halfway down, and I don't get how the cabin is inside the rock if it's in a shaft with no rock around it. Then the box rule from the Bianchi note, with the matter part taken off, says empty space just passes the shape change outward, it can't make it or lose it. But then it also says it fades to one eighth when you go twice as far, which sounds like losing it, and I don't know where the eighth comes from. The Sun pulls harder than the Moon but makes a smaller tide, somehow because of the eighth.

**Stumbles (19)**

- “A cabin falls down a shaft toward the centre, with a ball of crumbs let go inside.”: The first what-if a teenager tries: the shaft is hollow, so there is no rock at the spot where the crumbs are, which contradicts the next sentence. It is also a physics error: inside a hollow shaft through a solid uniform body the drift is pure stretch along the shaft, not a shrink, so the claim that the ball only shrinks fails there.
- “It shrinks because rock at the spot sets a room-changing part.”: In a shaft there is no rock at the spot; with the dust cloud the matter really is at the spot, as in the prerequisite's dust-cloud test.
- “scales halfway down the shaft read half your surface weight”: A rule the reader cannot follow in the new setting: nobody can stand on scales while falling with the dust. The fact needed is how the pull grows, not a weight reading.
- “Pulls that grow in step drift every pair of crumbs together by the same amount.”: A step left implicit: why a pull toward the planet's centre moves a pair of crumbs lying across that line together by the same amount as a pair lying along it.
- “Where does their shape-changing drift start?”: A third name for one idea beside shape-changing part and shape change.
- “every cubic metre holds the same amount of rock”: The prerequisite says spread evenly and this note says uniform; the glossary tied uniform to packed the same way, a third phrase.
- “What remains is a rule for the shape-changing part alone.”: Remains after what? The sentence before only splits the curving; nothing was taken away.
- “The three changes cancel.”: The prerequisite says add up to nothing; cancel is a second word for the same idea, and a change is a number that can be positive or negative.
- “So in empty space it cannot appear or fade on its own; each thin shell hands it on to the next”: Cannot fade contradicts the one-eighth fading two sentences later, and shell is an undefined word.
- “the three changes stop cancelling, by an amount set by that change”: Ambiguous that change: the change of matter or one of the three changes.
- “The rule also fixes the fading around a round planet: twice as far from the centre, one eighth as strong, while weight only falls to one quarter.”: A surprising number with no reason or count, and a second new idea in a way whose question is what carries the shape change (rule 17).
- “So the Sun, pulling Earth about 180 times harder than the Moon, raises a smaller tide.”: No reason why a harder pull gives a smaller tide, and tide was not in the glossary although the tutor notes forbid it at entry.
- “Look at a tide table for any coast for a month.”: Tide table is unfamiliar.
- “makes the shape change fall by eight each time the distance from the centre doubles. Weight falls by four”: Fall by eight reads as subtracting eight.
- “and 180 divided by 390 is less than one half”: Why divide the pull by the distance? The step is left implicit.
- “Predict what the ball does when the cabin is halfway down, and again at the centre.”: Halfway down what? The starting state is ambiguous without the shaft.
- “Compared with the centre crumb, the crumbs slowly drift ... changing its shape but not its room.”: Centre crumb and room are used in the recap but were not in the glossary.
- “the average density of all the matter closer to the centre against the density right there”: Density is not an entry word here, and the comparison is stated with no reason.
- “it divides by the cube of the distance ratio”: Cube and ratio are squeezed maths words in an entry solution.

**Fixes**

- Replaced the shaft through a solid planet with a uniform dust cloud let go from rest, the cabin falling with the dust, in the first way, its simplifies, the check crumbs-at-the-centre-and-halfway, the problem centre-and-three-radii, the opening question, the if_stuck move, the teaching arc and the falling-ring-of-crumbs sketch. A hollow shaft would give a pure stretch along the shaft, not a shrink, so the old picture was wrong as well as confusing.
- First way: replaced the scales-in-the-shaft weight reading with the pull of a uniform cloud (nothing at the centre, half at halfway) and made explicit why such a pull drifts every pair of crumbs together by the same amount.
- Second way: made the removal of the room-changing changes an explicit step, used the prerequisite's add up to nothing instead of cancel, replaced cannot fade and shell with cannot start or stop and layer, and moved the fading and the Sun-Moon tide out of it.
- Added the entry way fading-faster-than-weight (calculation) with the quarter-of-a-half count; its try_it holds the one-twenty-seventh, the Sun-Moon comparison as pull divided by distance, and the tide-table test, moved there to keep the entry explanations within the cap. The teaching arc step hand-it-on and the check refs now point to it.
- To fit the three entry ways into the 440-word allowance, the entry explanations were trimmed of repeated phrases only (the setting sentences, the reason for the pull growing in step, and the empty-space paragraph); no claim was dropped. The lowest-value entry item, the one-twenty-seventh sentence, moved from the way to its try_it.
- Glossary: added room, centre crumb and tide; uniform now reads spread evenly. Tutor voice note no longer forbids tide at entry.
- Check answers: fall to one eighth and to one quarter instead of by eight and by four; the Sun-Moon division now says why the pull is divided by the distance; the common question on layered planets says what is compared and that the box rule does the adding.

**Concerns**

- Entry way explanations are now 439 words, past the 400 cap for an advanced note but within the 10 percent review allowance, and the way extras are 834 of 800 for the same reason; any further entry addition must drop something.
- The entry rung now assumes a rule of gravity stated as known: weight falls to one quarter when the distance from the centre doubles. It is said to be taken as known; a prerequisite note on the inverse-square pull would be a cleaner home for it.
- For the physics reviewer: the new setting is a uniform dust cloud let go from rest, the cabin falling with the dust. The entry claims need the interior Weyl tensor of a homogeneous dust ball to vanish while it collapses and the exterior to be that of a static body of the same mass; both hold for homogeneous collapse, but please confirm the wording of the simplifies fields (at rest or falling in on itself evenly) and the pull-grows-in-step statement at the moment of release.
- The falling-ring-of-crumbs sketch (author-facing) was changed from a shaft mode to a dust-cloud mode for the same physics reason; the visual author should not draw a shaft or cavity.
- The working rung uses index notation; the index-notation prerequisite is reached only through the weyl-tensor prerequisite and is not listed directly.
- The check numbers (about three millimetres inside, five and three millimetres outside, in one minute) are unchanged and hold at the moment of release for Earth's mean density.

**Re-read** (2026-09-16, revision 4): 2 stumbles in 9 changed passages

- “only where the matter, or how it moves, changes from place to place.”: 'The matter changes' could mean the kind of matter, and the nested 'or how it moves' is hard to parse aloud; the way takeaway says 'the amount of matter, or its motion', so the summary used different words for the same idea.
- “The cosmological constant is absent, so a cosmological constant, the simplest dark energy, never feeds the current.”: Working rung: 'the cosmological constant is absent, so a cosmological constant' says the same noun twice in one breath and reads as a slip.
- Fix: Summary: 'the matter, or how it moves' became 'the amount of matter, or its motion', matching the empty-space takeaway; same claim.
- Fix: Working way split-riemann-and-take-the-divergence: reworded the cosmological-constant sentence to avoid the doubled noun; same claim.
- Fix: Not changed: the empty-space takeaway's 'or its motion' is not backed by that way's explanation, which only names a change in the amount of matter. Adding it there would add a claim to the explanation and exceed the entry budget (439 of 440 with allowance), so it is reported instead.

## Review: physics

**Verdict:** fixed (2026-09-16, revision 4)

**Verification**

- Once-contracted Bianchi identity ∇^ρ R_ρσμν = ∇_μ R_σν − ∇_ν R_σμ with the course Ricci definition R_μν = R^ρ_μρν.: Contracted g^{λρ} into the cyclic identity by hand; R^ρ_σνρ = −R_σν by antisymmetry in the last pair. → Correct as written in the working way and both derivations.
- Weyl divergence equation ∇^ρ C_ρσμν = ∇_[μ R_ν]σ − (1/6) g_σ[ν ∇_μ] R, coefficients 1 − 1/2 and −1/4 + 1/6 = −1/12, trace on σμ zero.: Re-derived every step of divergence-of-the-weyl-decomposition by hand from the course four-dimensional split; trace computed with ∇^ρ R_ρμ = (1/2)∇_μ R. → Correct; the bracket form matches the expanded form, and the σμ trace gives −(1/4)∇_ν R + (1/4)∇_ν R = 0.
- Current from matter: R_μν = κ(T_μν − (1/2)T g_μν) + Λ g_μν, coefficient −1/2 + 1/6 = −1/3, Λ drops out.: Traced G + Λg = κT with signature (−,+,+,+): −R + 4Λ = κT; differentiated; python for the fractions. → Correct; the equation weyl-current-from-matter holds with Einstein's constant 8πG/c^4.
- Newtonian shadow ∂_j E_ij = (8πG/3) ∂_i ρ from E_ij = ∂_i∂_jΦ − (1/3)δ_ij ∇²Φ, and from the σ=0, μ=i, ν=0 component of the current with T_00 = ρc², T = −ρc², g_00 = −1.: Checked that c²C_i0j0 equals the trace-free tidal tensor in the weak static field using R_00 = ∇²Φ/c², R_ij = δ_ij∇²Φ/c², R = 2∇²Φ/c²; worked the component: κ(1/2 − 1/6)c²∂_iρ, and κc⁴/3 = 8πG/3 numerically (5.59e−10 SI both ways). → Correct; the geodesic-deviation sign with the course convention gives relative acceleration −E_ij ξ^j, so E_rr < 0 is a radial stretch, as the note says.
- Uniform ball: E_ij = 0 inside, GM/r³(δ_ij − 3n_in_j) outside, E_rr = −2GM/r³, surface jump −(8πG/3)ρ, value 3.08e−6 s⁻² for ρ = 5513 kg/m³, equal to 2GM/R³ for Earth.: Hand derivatives of −GM/r and (2πGρ/3)r²; python: 8πGρ/3 = 3.082e−6 s⁻², 2GM_E/R_E³ = 3.083e−6 s⁻². → Correct, including the delta-function bookkeeping of the jump against (8πG/3)∂_rρ.
- Problem inverse-cube-from-balance: ∂_j[A(δ_ij − 3n_in_j)] = −(2A′ + 6A/r)n_i, A = K/r³, K = GM, |E_rr(3R)| = 8πGρ/81 = 1.14e−7 s⁻².: Hand calculation with ∂_j n_i = (δ_ij − n_in_j)/r and ∂_j n_j = 2/r; python: 3.082e−6/27 = 1.142e−7. → Correct; numeric answer 1.14e−7 m/s² per metre with rel_tol 0.05 holds.
- Entry check numbers: inside a uniform cloud of Earth's mean density two crumbs 1 m apart close by about 3 mm in the first minute; just outside, 5 mm apart along the radius and 3 mm together across it.: python: (1/2)(4πGρ/3)(60 s)² = 2.77 mm; (1/2)(8πGρ/3)(60 s)² = 5.55 mm; transverse 2.77 mm. Free-fall time 895 s, so the density rises by 0.8 percent in the first minute, negligible. → Correct; numeric 2.8 mm with abs_tol 0.6 holds. For homogeneous dust collapse from rest the interior is a closed FLRW patch with R_î0ĵ0 = (4πGρ/3)δ_ij exactly and zero Weyl tensor; the exterior is Schwarzschild by Birkhoff, whose tidal components for a radially falling observer are exactly −2GM/r³ and +GM/r³.
- Scope wording 'a round, uniform planet, at rest or falling in on itself evenly' and 'the pull grows in step with distance, half as strong halfway out'.: Static case: the constant-density interior Schwarzschild solution is conformally flat (Weyl zero), and the static-fluid current reduces to the density gradient. Collapsing case: Oppenheimer–Snyder interior is FLRW. Newtonian g(r) = (4πGρ/3) r inside a round uniform body; the relative acceleration −(4πGρ/3)ξ is isotropic and linear at release. → Both statements hold; 'round' was missing from the takeaway, simplifies, misconception correction and problem statement and was added, since a uniform oblate body has a constant but anisotropic interior tidal tensor.
- Entry fading count: one eighth at twice the distance, one twenty-seventh at three times; Sun/Moon pull ratio about 180, distance ratio about 390, 180/390 a bit less than one half.: python with M_sun/M_moon = 2.709e7 and d_moon/d_sun = 2.569e−3: pull ratio 178.9, tidal ratio 0.460, distance ratio 389.2; 180/390 = 0.462, 179/389 = 0.460. → Correct; the observation's 179, 0.46 and 389 agree.
- Layered-planet common question: lighter rock over a dense core is stretched along the radius.: Derived E_rr = (8πG/3)(ρ(r) − ρ̄(r)) for any spherical profile, with ρ̄ the mean density inside r; checked by finite differences on a two-layer model in python (−1.726e−6 both ways). → Correct: ρ < ρ̄ gives E_rr < 0, a stretch along the line to the centre, and the uniform case gives zero.
- Cotton form: P trace R/(2(n−1)), ∇^ρ P_ρν = ∇_ν P, ∇^ρ C_ρσμν = (n−3)(∇_μ P_νσ − ∇_ν P_μσ); n = 4 reproduces 1/2 and −1/12.: Hand algebra of every step of cotton-form-in-n-dimensions; python for the trace coefficient. → Correct.
- Component count 24 − 4 − 4 = 16, once-contracted identity 20 = 16 + 4.: Dimension of the trace-free (2,1) hook representation of GL(4): n(n²−1)/3 − n = 20 − 4 = 16; the once-contracted identity has the (2,1) symmetry without the trace condition. → Correct.
- Conservation of the current: the two commutator terms −R_λνσμ R^λσ and +R_μλ R^λ_ν are symmetric in μν.: Ricci identity for a (0,2) tensor with the course Riemann sign, contraction R^λα_αμ = −R^λ_μ checked by hand, pair symmetry for the first term. → Correct in the formal way and in the check current-is-conserved.
- Static perfect fluid: pressure cancels between the derivative block and the trace block; J_σμν = 8π(u_σ u_[ν D_μ] ρ + (1/3) g_σ[ν D_μ] ρ); the 0i0 component gives (1/2 − 1/6)D_iρ.: Expanded ∇_μ T_νσ with ∇_μ u_ν = −u_μ a_ν and (ρ + p)a_ν = −D_ν p; antisymmetrized; T = −ρ + 3p. → Correct, and consistent with the Newtonian shadow.
- Vacuum: P = (Λ/6) g, the cyclic and divergence forms are equivalent through the equal duals of the Weyl tensor, and the wave equation follows from ∇^λ applied to the cyclic form.: Hand derivation; the two commutator terms match the note's expression. → Correct; the right side is quadratic in C only when Λ = 0, as stated.
- E_ij = −(1/2) ḧ_ij in TT gauge and GW150914 numbers.: Linearized Riemann with the course sign: R_i0j0 = −(1/2)∂_0² h_ij; python: (1/2)(1e−21)(2π·150 Hz)² = 4.44e−16 s⁻², times 4000 m = 1.78e−12 m/s². → Correct.
- Notation trap variant C^{μναβ}_{;β} = R^{α[μ;ν]} + (1/6) g^{α[ν} R^{;μ]}.: Pair symmetry and antisymmetry of C move the contraction to the first index with one sign, which the reversed bracket absorbs. → Correct.
- Research statements: E and H five components each, dust div-E constraint (8π/3)D_μρ, silent universes generally inconsistent with Szekeres consistent, Bel–Robinson totally symmetric, trace-free, divergence-free in vacuum, dimension curvature squared, peeling r^−1 to r^−5.: Compared with the 1+3 covariant equations and the peeling theorem as stated in the verified references. → Accurate.
- References: Weyl 1918; Matte 1953; Hawking 1966; Ellis 1971/2009; Tsagas, Challinor and Maartens 2008; Maartens and Bassett 1998; van Elst et al. 1997; Christodoulou and Klainerman 1993; Senovilla 2000; Sachs 1962; Newman and Penrose 1962; Abbott et al. 2016.: One web search each against publisher, ADS, arXiv or Cambridge Core records. → All twelve confirmed with the listed venues, DOIs and arXiv ids; Matte's DOI 10.4153/CJM-1953-001-3 added. One record gives the Ellis lectures as pp. 104–179; the Golden Oldie republication and Ellis's own citations give 104–182, kept.

**Counterexamples tried**

- Uniform oblate (spinning, flattened) planet: the interior tidal tensor of a uniform ellipsoid is constant but anisotropic, so a ball inside does change shape. Broke 'inside a uniform planet a ball of crumbs only shrinks' wherever 'round' was missing; 'round' added to the takeaway, simplifies, misconception correction and problem statement.
- Uniformly spinning round uniform body: the amount of matter changes only at the surface, yet the varying momentum density sources a magnetic Weyl part inside (div H ∝ ρω). Broke the summary and the second way's takeaway 'made only where the amount of matter changes'; both now say 'or how it moves'.
- Dynamical dark energy with spatial gradients: sources the current although a cosmological constant does not. 'Dark energy never feeds the current' rescoped to a cosmological constant.
- Hollow shaft through a solid uniform body: the removed cylinder gives a pure stretch along the shaft (the novice reviewer's finding); the dust-cloud setting avoids it and the sketch forbids a cavity. Confirmed.
- Point between two equal masses: the pulls cancel but the tidal tensors add, so the shape change does not vanish there; 'cannot start or stop in empty space' survives.
- Three dimensions: the Weyl tensor vanishes and the identity reads 0 = 0; the note states this limit.
- Cosmological constant only: J = 0 and P = (Λ/6)g; the vacuum statements hold with Λ.

**Fixes**

- Summary: 'only where the matter, or how it moves, changes from place to place'.
- First entry way: takeaway and simplifies now say 'round, uniform planet'; the misconception correction and the entry problem statement likewise.
- Second entry way takeaway: 'where the amount of matter, or its motion, changes'.
- Working way split-riemann-and-take-the-divergence: 'a cosmological constant, the simplest dark energy, never feeds the current'.
- Teaching arc ask-where-it-starts: 'dust all around' instead of 'rock all around' in the why and the spoken prediction, matching the dust-cloud setting.
- Matte 1953 DOI added; all twelve references marked verified.

**Concerns**

- The formal way says n ≥ 4 while the key equation cotton-form says dimension at least three; both are true (for n = 3 both sides vanish), left as is.
- The entry rung takes the inverse-square fading of weight as known; a prerequisite note on the inverse-square pull would be the cleaner home, as the novice reviewer noted.
- Registry: prerequisites einstein-field-equations and newtonian-tidal-tensor have registry entries but no notes yet, and the registry lists only weyl-tensor and bianchi-identity; sync_registry.py after review. Visuals falling-ring-of-crumbs and cube-of-small-loops remain proposed with sketches.
- The physics fixes changed learner-visible entry text (summary, two takeaways, a simplifies, a misconception correction, a problem statement); revision bumped to 3 for the novice post-review check of exactly those strings.

**Diff check** (2026-09-16, revision 4)

- Summary and empty-space takeaway: the shape-changing (Weyl) part is made only where the amount of matter, or its motion, changes from place to place.: Read as a necessary condition ('only where'). Tried the note's counterexamples: uniform collapsing dust (FLRW interior, motion varies but Weyl zero, consistent with 'only where'); static uniform-density fluid with pressure gradient (interior Schwarzschild is conformally flat); uniformly spinning uniform body (varying momentum density sources magnetic Weyl). → True within the entry scope stated in simplifies; the rewrite keeps the claim.
- 'Round' in the takeaway, simplifies, misconception, problem and spoken prediction.: Uniform ball: Newtonian tidal tensor (4πGρ/3)δ_ij, isotropic, so no shape change; uniform ellipsoid has a constant but anisotropic interior tidal tensor, so a ball inside does change shape. → Correct and needed.
- The cosmological constant drops out of the Weyl current.: With Λ, R_μν = 8πG(T_μν − ½ g_μν T) + Λ g_μν and R = −8πG T + 4Λ. In ∇_[μ R_ν]ρ − (1/6) g_ρ[ν ∇_μ] R the Λ g_μν term has zero covariant derivative and the constant 4Λ has zero gradient. → Correct; the reworded sentence keeps the claim. 'Simplest kind of dark energy' is standard usage for a cosmological constant.
