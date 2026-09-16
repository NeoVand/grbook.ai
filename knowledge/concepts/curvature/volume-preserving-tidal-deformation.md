---
type: "concept"
schema_version: 2
id: "volume-preserving-tidal-deformation"
title: "Volume-preserving tidal deformation"
tagline: "Why tidal drift reshapes a falling ball with nothing inside long before its volume changes"
domain: "curvature"
tier: "core"
status: "novice-reviewed"
revision: 4
updated: "2026-09-16"
aliases: ["tidal ellipsoid", "shape change without volume change", "volume preservation of a freely falling cloud in vacuum"]
prerequisites: ["relativistic-tidal-tensor", "ricci-tensor", "poisson-equation-for-gravity"]
leads_to: ["raychaudhuri-equation", "geodesic-deviation-in-gravitational-wave", "gravitational-wave-polarization", "tidal-derivation-of-vacuum-field-equations", "ricci-focusing-versus-weyl-shear", "focusing-theorem"]
visuals: ["falling-ring-of-crumbs", "two-stars-and-a-distant-ring"]
---

# Volume-preserving tidal deformation

*Why tidal drift reshapes a falling ball with nothing inside long before its volume changes*

`volume-preserving-tidal-deformation` · curvature · core · novice-reviewed (revision 4)

**Needs:** [[relativistic-tidal-tensor]] (entry) · [[ricci-tensor]] (working) · [[poisson-equation-for-gravity]] (working)  
**Opens:** [[raychaudhuri-equation]] · [[geodesic-deviation-in-gravitational-wave]] · [[gravitational-wave-polarization]] · [[tidal-derivation-of-vacuum-field-equations]] · [[ricci-focusing-versus-weyl-shear]] · [[focusing-theorem]]  
**Related:** [[tidal-force]] · [[spaghettification]] · [[weyl-tensor]] · [[strong-energy-condition]] · [[expansion-shear-and-rotation]]  
**Visuals:** ★ [[falling-ring-of-crumbs]] · [[two-stars-and-a-distant-ring]]

> Let go of crumbs at rest on a small imaginary ball, inside a cabin that falls freely near a planet, with nothing among them. Tidal drift stretches the ball along the line toward the planet's centre. It squeezes the ball half as much in each of the two directions across that line. The three changes cancel, so the ball becomes an egg that at first takes up the same room. By Newton's law of gravity, only mass inside the ball makes that room start to change.

## You will be able to

**Entry**
- Explain why tidal drift turns a small falling ball of crumbs into an egg that at first takes up the same room. `objectives/explain-the-egg-keeps-its-room` ← `checks/room-in-the-egg`
- Predict whether a ball of crumbs let go at rest starts to shrink, from whether mass sits inside it. `objectives/predict-which-balls-shrink` ← `checks/which-balls-shrink`, `problems/ball-around-the-moon`

**Working**
- Compute the initial volume acceleration of a released cloud of any size from the mass it encloses. `objectives/compute-from-enclosed-mass` ← `checks/big-cloud-beside-earth`, `problems/cube-around-earth`
- Use the zero trace of vacuum tides to find a gravitational wave's squeeze from its stretch, and the change in a ring's area. `objectives/use-the-budget-for-a-wave` ← `checks/mirror-arms-in-a-wave`

**Formal**
- State the hypotheses under which a small freely falling ball keeps its volume at first, and give a counterexample when each fails. `objectives/state-the-hypotheses` ← `checks/released-with-a-shear`
- Use the fourth-order vacuum volume law to compare how soon balls released by different observers at one event lose volume. `objectives/compare-how-long-the-balance-lasts` ← `checks/passer-loses-volume-sooner`
- Prove that every freely falling observer at an event finds a zero initial volume acceleration exactly when the stress-energy tensor vanishes there. `objectives/prove-the-matter-equivalence` ← `problems/every-observer-keeps-volume`

## Ways in

### 1. The egg that takes up the ball's room · entry · picture

*Tidal drift pulls a small falling ball of crumbs into an egg shape. Does the egg take up more room than the ball, less, or the same?*

**Recap:** A cabin falls freely when nothing but gravity acts on it: no air pushing, no floor or rope holding it. Crumbs let go at rest inside such a cabin drift compared with a crumb at their centre, because the planet's pull is slightly different at each crumb's place. Outside a round planet they drift away from that centre crumb along the line toward the planet's centre, and in toward it across that line, half as far. This is called tidal drift. Time it with the cabin's clock and measure it with a ruler fixed to the cabin.

Picture a cabin falling freely down a tall tower on Earth, with the air pumped out. Inside, hundreds of crumbs are held still in the cabin, spread over the surface of an imaginary ball 2 metres across. One more crumb, the centre crumb, sits at the ball's centre, and nothing else floats among them. Then all of them are let go together, at rest in the cabin.

Watch for ten seconds by the cabin's clock. Two crumbs sit 1 metre out on the line toward Earth's centre, one on each side of the centre crumb. Each drifts away from the centre crumb by 0.154 millimetres. A crumb 1 metre out across that line drifts in by half as far, 0.077 millimetres. So the ball becomes egg-shaped: longer along the line, narrower across it, and the same at both ends.

Does the egg take up more room than the ball, or less? Write each drift as a fraction of the 1 metre it belongs to. A metre is 1,000 millimetres, so 0.154 millimetres is 154 millionths of a metre. Along the line, the egg is longer by 154 parts in a million. Across the line there are two directions at right angles, and in each the egg is narrower by 77 parts in a million.

For small changes, the room a shape takes up changes by the sum of these fractions. A box shows why. A box 1 metre on each side holds 1 cubic metre. Make it 2 thousandths longer and 1 thousandth narrower each way, so the three fractions add to zero. Multiplying 1.002 by 0.999 by 0.999 gives 0.999997 cubic metres, only 3 millionths less. An egg's room is also set by its length times its two widths, so the rule works for the egg too.

For the egg the three fractions are plus 154, minus 77 and minus 77. They add to zero. So the stretch along the line pays for both squeezes across it, and at first the egg takes up the same room the ball took.

Preserving means keeping, and a deformation is a change of shape. So a change of shape by tidal drift that keeps the room the same is called a volume-preserving tidal deformation.

The words "at first" matter, because adding the fractions works only while they stay small. Once the egg is much longer than it is wide, the sum no longer gives its room, and the room does slowly shrink.

You never notice any of this. After those ten seconds the egg is longer than it is wide by less than half a millimetre, about the width of six hairs. Shape and room are two different questions, and this is a case where the shape changes and the room does not.

**Try it:** On a calculator, multiply 1.002 by 0.999 by 0.999. You should see 0.999997: the box has lost only 3 millionths of its room. Now multiply 1.2 by 0.9 by 0.9. You should see 0.972. Both boxes have fractions that add to zero: plus 2 thousandths against minus 1 thousandth twice, then plus 2 tenths against minus 1 tenth twice. Yet the second box has lost nearly 3 hundredths of its room. So the adding rule works only while the changes stay small.

**Takeaway:** Tidal drift stretches a small falling ball of crumbs along the line toward the planet's centre. It squeezes the ball half as much across that line, so at first its shape changes and its room does not.

*What this leaves out:* Keeps the ball small compared with Earth, and treats Earth as a perfect ball that does not spin.

*Builds on:* [[relativistic-tidal-tensor]]<br>*Visuals:* [[falling-ring-of-crumbs]]<br>*See:* `checks/room-in-the-egg`

### 2. Which balls of crumbs shrink · entry · contrast

*What makes a falling ball of crumbs start to shrink, instead of keeping the room it takes up?*

**Recap:** In a cabin falling freely near Earth, crumbs let go at rest drift compared with a crumb at their centre. A small ball of them grows longer along the line toward Earth's centre by some fraction. It grows narrower by half that fraction in each of two directions across the line. For small changes, the room a shape takes up changes by the sum of such fractions. One fraction minus two halves of it is zero, so at first the ball keeps its room.

Now make the ball enormous. Picture crumbs spread over an imaginary ball drawn around the whole Earth, 400 kilometres above the ground, higher than almost all of the air. Earth sits at the ball's centre. Each crumb is held still relative to Earth's centre, and then all of them are let go together.

Every crumb falls toward Earth's centre. Measured with rulers that stay still relative to Earth's centre, each falls about 435 metres in ten seconds. All the crumbs start the same distance from Earth's centre, so none falls ahead of the others, and each moves inward by the same amount. So this ball stays round, and it shrinks.

By how much? The ball's radius is 6,771 kilometres, and 435 metres is 64 parts in a million of that. The ball grows narrower by that fraction in every direction. So pick three directions at right angles and add their three fractions. The room this ball takes up shrinks by about 193 parts in a million.

Compare the small ball in the falling cabin. Its crumbs fall toward the very same Earth, yet at first it keeps its room. What differs is what lies inside each ball. The huge ball holds all of Earth. The small ball holds nothing but empty space among its crumbs.

That difference decides how the crumbs move. With Earth inside, every crumb is pulled toward the ball's centre, so the whole ball draws in. With Earth outside, crumbs nearer Earth fall ahead of the centre crumb while crumbs farther from Earth lag behind, so some move out and some move in.

Newton's law of gravity, which we take on trust here, gives one rule for a ball of any size. A ball of crumbs let go at rest starts to change the room it takes up only if mass sits inside it. The more mass inside, the faster it shrinks. Mass outside changes only the ball's shape at first, however heavy and however close.

The rule covers the small ball in the cabin too. Its cabin's walls lie outside it, so their pull does not start the room changing. The centre crumb does lie inside. Yet a crumb is so light that in ten seconds its pull moves the others far less than the width of an atom.

**Takeaway:** By Newton's law of gravity, a ball of crumbs let go at rest starts to shrink only when mass sits inside it. Mass outside it changes only its shape at first.

*What this leaves out:* Treats Earth as a perfect ball that does not spin, and uses Newton's law of gravity, which describes gravity near Earth extremely well.

*Continues:* `ways_in/egg-with-the-same-room`<br>*Visuals:* [[falling-ring-of-crumbs]]<br>*See:* `checks/which-balls-shrink`, `problems/ball-around-the-moon`

### 3. Gauss's law counts the mass inside · working · calculation

*How does the mass a released cloud encloses fix its initial volume change, and what takes over in general relativity?*

The huge ball in "Which balls of crumbs shrink" lost volume while the small egg beside Earth kept it. Newtonian gravity makes that contrast exact. Take free particles covering a closed surface $S$ that encloses volume $V$, all at rest at $t = 0$. The derivation "Volume acceleration from Gauss's law" gives

$$\ddot V(0) = \oint_S \mathbf g\cdot d\mathbf A = -4\pi G M_{\rm enc}.$$

This holds for a cloud of any size and shape, at the instant of release. A cloud beside Earth, however large, encloses no mass and starts with $\ddot V = 0$, even though tides distort it into no simple shape. For a sphere of radius $r$ centred on a spherical mass, $\ddot V/V = -3GM/r^3$. At 400 km above Earth, $r = 6771$ km gives $-3.85\times10^{-6}\ \mathrm{s^{-2}}$, so in 10 s the volume falls by $\tfrac12(3.85\times10^{-6}\ \mathrm{s^{-2}})(10\ \mathrm s)^2 = 1.93\times10^{-4}$: the 193 parts in a million of that way.

Shrink the cloud to a point, so that $M_{\rm enc} = \rho\,\delta V$, and

$$\frac{\ddot{\delta V}}{\delta V} = -4\pi G\rho = -\nabla^2\Phi = -\operatorname{tr}\big(\partial_i\partial_j\Phi\big).$$

The same matrix $\partial_i\partial_j\Phi$ fixes the shape. Along an eigenvector with eigenvalue $\lambda_i$, a separation released at rest goes as $\ell_i \approx \ell_0(1 - \tfrac12\lambda_it^2)$. Just outside a spherical mass the eigenvalues are $(GM/r^3)(-2, 1, 1)$. At Earth's surface $GM/r^3 = 1.54\times10^{-6}\ \mathrm{s^{-2}}$, so in 10 s a 1 m semi-axis along the radius grows by 0.154 mm while each transverse one shrinks by 0.077 mm. The fractional changes sum to $-\tfrac12t^2\sum_i\lambda_i$, which vanishes because the trace does. Since $\delta V/V \approx \sum_i \delta\ell_i/\ell_i$ for small changes, this is the entry rule that the fractions add, with its zero now traced to $\nabla^2\Phi = 0$.

In general relativity the trace of a freely falling observer's tidal tensor is $R_{\mu\nu}u^\mu u^\nu$, and the local law becomes $\ddot{\delta V}/\delta V = -R_{\mu\nu}u^\mu u^\nu$ for a small ball released at rest. For matter at rest relative to that observer it equals $-4\pi G(\rho + 3p/c^2) + \Lambda c^2$. Outside matter, with $\Lambda = 0$, Einstein's equation gives $R_{\mu\nu} = 0$, so the trace vanishes for every observer whatever their velocity. An observer passing a spherical mass sideways at $0.6c$ measures the tidal tensor $(GM/r^3)\,\mathrm{diag}(-3.69, 2.69, 1)$: a different egg, with the same zero sum.

The finite-cloud law is Newtonian only. In general relativity the volume of a finite cloud depends on which events are counted as simultaneous, so only the small-ball law is local and exact.

**Takeaway:** A cloud released at rest starts with volume acceleration minus four pi G times the mass it encloses; for a small ball that is minus the trace of the tides, which vanishes in vacuum for every observer.

*What this leaves out:* The finite-cloud law assumes Newtonian gravity; the relativistic law keeps only the leading order in the ball's size and in the time since release.

*Continues:* `ways_in/balls-that-shrink`, `ways_in/egg-with-the-same-room`<br>*Builds on:* [[ricci-tensor]], [[poisson-equation-for-gravity]]<br>*See:* `derivations/volume-acceleration-from-gauss`, `checks/big-cloud-beside-earth`, `problems/cube-around-earth`

### 4. A ring of mirrors in a gravitational wave · working · operational

*What does the zero trace of vacuum tides look like in a gravitational wave, and what can a detector measure of it?*

The zero trace in "Gauss's law counts the mass inside" holds for every tide in vacuum, including one that travels. Far from its source a gravitational wave is such a tide. Take on trust here that a plane wave of plus polarization travelling along $z$ gives a freely falling observer the tidal tensor $-\tfrac12\ddot h_+\,\mathrm{diag}(1, -1, 0)$ in her $x, y, z$ axes. Free masses a distance $L$ apart, at rest before the wave arrives, then move to first order in $h_+$ as

$$\frac{\delta L_x}{L} = +\frac{h_+}{2},\qquad \frac{\delta L_y}{L} = -\frac{h_+}{2},\qquad \frac{\delta L_z}{L} = 0.$$

The budget is now one stretch against one equal squeeze, in the plane across the wave, instead of one stretch against two half-size squeezes. These fractional changes sum to zero at every moment, not only at release, because the wave's tidal tensor stays trace-free as it goes by. So a ring of free masses in the $xy$ plane keeps its area, and a small ball its volume, to first order in $h_+$; the product of the two first-order length factors is $1 - h_+^2/4$. The cross polarization does the same along axes turned by $45^\circ$.

A laser interferometer uses the mirrors hanging at the ends of two perpendicular arms as free masses. At the frequencies of a signal each suspended mirror moves freely along its arm, and the instrument measures $\delta L_x - \delta L_y$, which is $h_+L$ for a plus wave arriving along $z$. GW150914 reached a peak strain of about $1.0\times10^{-21}$. Each 4 km arm therefore changed by about $2\times10^{-18}$ m, and the difference by about $4\times10^{-18}$ m, some 400 times smaller than a proton's width.

One detector measures only that difference. By itself it cannot tell an area-preserving wave from a breathing wave, which would stretch both transverse directions together and change a ring's area, as some alternatives to general relativity predict. Detectors pointed differently respond to the two patterns differently, so a network can test which patterns a signal carries.

**Takeaway:** A gravitational wave stretches one direction across its path and squeezes the perpendicular one by the same fraction, so a ring or a ball of free masses keeps its area or volume to first order in the strain.

*What this leaves out:* Keeps first order in the strain, for masses much closer together than a wavelength and a wave arriving along one axis.

*Continues:* `ways_in/gauss-law-counts-the-mass-inside`<br>*Builds on:* [[relativistic-tidal-tensor]]<br>*Visuals:* [[two-stars-and-a-distant-ring]]<br>*See:* `checks/mirror-arms-in-a-wave`, `observations/gw170814-polarization-test`

### 5. Volume and shear of a released ball · formal · structure

*Under exactly which hypotheses does a small freely falling ball keep its volume, and for how long?*

The small-ball law in "Gauss's law counts the mass inside" is the first term of an exact evolution equation. Set $G = c = 1$. Let $u$ be a timelike geodesic congruence near an event $p$, and split $B_{\mu\nu} = \nabla_\nu u_\mu$ into expansion $\theta$, shear $\sigma_{\mu\nu}$ and rotation $\omega_{\mu\nu}$. For a small ball of its geodesics $\theta = d\ln\delta V/d\tau$, and the Raychaudhuri equation reads

$$\frac{d\theta}{d\tau} = -\frac{\theta^2}{3} - \sigma_{\alpha\beta}\sigma^{\alpha\beta} + \omega_{\alpha\beta}\omega^{\alpha\beta} - R_{\mu\nu}u^\mu u^\nu.$$

*Proposition.* Suppose (i) the ball is released at rest, so $B_{\mu\nu}(0) = 0$; (ii) $R_{\mu\nu} = 0$ along its worldlines, which Einstein's equation gives in vacuum with $\Lambda = 0$; (iii) the ball's size $\ell$ is small compared with the curvature radius and with the length over which the curvature changes. Then

$$\ln\frac{\delta V}{\delta V_0} = -\tfrac{1}{12}E_{ij}E_{ij}\,\tau^4 + O(\tau^5),$$

where $E_{ij} = R_{\hat\imath\hat 0\hat\jmath\hat 0}$ at $p$ in a parallel-propagated orthonormal frame; in vacuum this is the electric part of the Weyl tensor. *Sketch.* $\dot B = -B^2 - E$ with $B(0) = 0$ gives $B = -E\tau + O(\tau^2)$. The zero trace then kills the $\tau^2$ and $\tau^3$ terms of $\ln\delta V$, while the shear that grows meanwhile drives $\dot\theta = -E_{ij}E_{ij}\tau^2 + O(\tau^3)$. The derivation "Fourth-order volume loss in vacuum" gives every step.

Each hypothesis earns its place.

- *Release at rest.* A ball released with pure shear has $\ddot{\delta V}/\delta V = -\sigma_{\alpha\beta}\sigma^{\alpha\beta}$ from the start, even in flat spacetime. A nonzero initial expansion changes the volume already at first order in $\tau$, and rotation opposes the focusing.
- *Vacuum with $\Lambda = 0$.* With $R_{\mu\nu} = \Lambda g_{\mu\nu}$ one has $R_{\mu\nu}u^\mu u^\nu = -\Lambda$, so a ball released at rest starts to grow at $\ddot{\delta V}/\delta V = +\Lambda$, about $1\times10^{-35}\ \mathrm{s^{-2}}$ in SI for today's value.
- *Smallness.* The deviation equation keeps only first order in $\ell$, so corrections of relative order $\ell/L$ appear where the tidal field varies over a length $L$. Newtonian gravity alone has an exact finite-cloud law, $\ddot V(0) = -4\pi M_{\rm enc}$.

*What observers share.* With $\Lambda = 0$, $R_{\mu\nu} = 8\pi(T_{\mu\nu} - \tfrac12 Tg_{\mu\nu})$, and this trace reversal is invertible in four dimensions. A symmetric tensor that vanishes on every timelike vector vanishes. So every freely falling observer at $p$ finds a zero initial volume acceleration exactly when $T_{\mu\nu}(p) = 0$. The fourth-order coefficient is not shared: $E_{ij}E_{ij}$ changes under boosts, so observers who agree that a released ball starts with an unchanged volume disagree on how long it stays nearly unchanged. In vacuum the Kretschmann scalar is $R_{\alpha\beta\gamma\delta}R^{\alpha\beta\gamma\delta} = 8(E_{ij}E_{ij} - B_{ij}B_{ij})$, with $B_{ij}$ the magnetic part of the Weyl tensor, so only that difference is invariant. A static observer outside a spherical mass has $B_{ij} = 0$ and $E_{ij}E_{ij} = 6M^2/r^6$, and a boosted observer's larger $E_{ij}E_{ij}$ comes with a nonzero $B_{ij}$.

*Light.* The same argument runs for a thin bundle of null geodesics with vanishing initial expansion and shear. In vacuum the Ricci term drops out of the focusing equation, so the bundle's cross-sectional area is unchanged through third order in the affine parameter; the Weyl tensor acts only by building shear, which then focuses the bundle.

**Takeaway:** In vacuum with no cosmological constant, a small ball released at rest keeps its volume through third order in proper time, and the shear that the Weyl tensor builds removes volume at fourth order.

*Picture:* A small sphere of geodesics released at rest: its axes follow the eigenvectors of the electric Weyl tensor, its volume curve is flat through third order, and it bends down at fourth order as the shear builds.

*What this leaves out:* Uses the Levi-Civita connection in four dimensions and a nonrotating, parallel-propagated frame.

*Continues:* `ways_in/gauss-law-counts-the-mass-inside`<br>*Builds on:* [[ricci-tensor]]<br>*See:* `derivations/fourth-order-loss-in-vacuum`, `checks/released-with-a-shear`, `checks/passer-loses-volume-sooner`, `problems/every-observer-keeps-volume`

## Glossary

| Term | Say | In plain words | Concept |
| --- | --- | --- | --- |
| fall freely | — | To move with nothing but gravity acting: no air pushing, and no floor or rope holding you. | [[free-fall]] |
| tidal drift | — | The slow drift of neighbouring freely falling objects apart or together, because gravity pulls them slightly differently. Outside a round planet they drift apart along the line toward its centre and together across that line. | [[tidal-force]] |
| centre crumb | — | The crumb at the centre of a ball of crumbs. Every other crumb's drift is measured against it, because it is the one the falling cabin keeps pace with. | — |
| volume | — | The amount of room something takes up. | — |
| volume-preserving tidal deformation | VOL-yoom pri-ZUR-ving TIE-dul dee-for-MAY-shun | A change of shape caused by tidal drift that keeps the volume the same, like a small ball of crumbs becoming an egg that takes up the same room. Preserving means keeping, and a deformation is a change of shape. | [[volume-preserving-tidal-deformation]] |

## Key equations

### Volume acceleration of a released cloud · working

$$
\ddot V(0) = \oint_S \mathbf g\cdot d\mathbf A = -4\pi G M_{\rm enc}
$$

A cloud of free particles released at rest starts to change its volume at a rate set only by the mass it encloses.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $V$ | volume enclosed by the surface of free particles | the volume |
| $\mathbf g$ | gravitational field at the particles | the gravitational field |
| $M_{\rm enc}$ | mass inside the surface | the enclosed mass |

**Holds when:** Newtonian gravity; every particle of the surface at rest at $t = 0$; any size and shape; valid at that instant only.  
**Say it:** “At release, the second time derivative of the volume is minus four pi G times the enclosed mass.”  
**Justified by:** `derivations/volume-acceleration-from-gauss`

### Initial volume law for a small ball · working

$$
\left.\frac{\ddot{\delta V}}{\delta V}\right|_{\tau = 0} = -R_{\mu\nu}u^\mu u^\nu
$$

A small ball released at rest starts to change its volume at a rate set by the trace of the tides, which is zero in vacuum.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $\delta V$ | volume of the small ball | the small volume |
| $u^\mu$ | four-velocity of the central particle, with $u_\mu u^\mu = -c^2$ | the four-velocity |
| $R_{\mu\nu}$ | Ricci tensor in the course convention | the Ricci tensor |

**Holds when:** Small ball released at rest, at that instant only. For matter at rest relative to the observer the right side is $-4\pi G(\rho + 3p/c^2) + \Lambda c^2$; a weak static field gives $-4\pi G\rho$.  
**Say it:** “At release, the small volume's second derivative divided by the volume is minus the Ricci tensor contracted twice with the four-velocity.”  
**Justified by:** `ricci-tensor`

### Free masses in a plus-polarized wave · working

$$
\frac{\delta L_x}{L} = +\frac{h_+}{2},\qquad \frac{\delta L_y}{L} = -\frac{h_+}{2},\qquad \frac{\delta L_z}{L} = 0
$$

A wave travelling along $z$ stretches one transverse direction by as much as it squeezes the other, and does nothing along its path.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $h_+$ | plus-polarization strain of the wave | h plus |
| $L$ | separation of two free masses before the wave arrives | the separation |

**Holds when:** Plane wave along $z$ with the course polarization convention; free masses at rest before it arrives and much closer together than a wavelength; first order in $h_+$.  
**Say it:** “The fractional change along x is plus h plus over two, along y minus h plus over two, and along z zero.”  
**Justified by:** `stated`

### Fourth-order volume loss in vacuum · formal

$$
\ln\frac{\delta V}{\delta V_0} = -\tfrac{1}{12}E_{ij}E_{ij}\,\tau^4 + O(\tau^5)
$$

In vacuum, a small ball released at rest first loses volume at fourth order in proper time, at a rate set by the square of the tides.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $E_{ij}$ | tidal tensor $R_{\hat\imath\hat 0\hat\jmath\hat 0}$ at release, which in vacuum is the electric part of the Weyl tensor ($G = c = 1$) | E i j |
| $\tau$ | proper time of the central particle | tau |
| $\delta V_0$ | the ball's volume at release | the volume at release |

**Holds when:** Released at rest; $R_{\mu\nu} = 0$ along the worldlines; ball small compared with the curvature radius; parallel-propagated orthonormal frame.  
**Say it:** “The log of the volume ratio is minus one twelfth of E i j E i j times tau to the fourth.”  
**Justified by:** `derivations/fourth-order-loss-in-vacuum`

## Derivations

### Volume acceleration from Gauss's law · working

**Goal:** Show that a Newtonian cloud of free particles released at rest has $\ddot V(0) = -4\pi G M_{\rm enc}$, and $\ddot{\delta V}/\delta V = -4\pi G\rho$ when the cloud is small.

1. The particles covering the closed surface $S$ move with velocity $\mathbf v$, so the enclosed volume changes as $\dot V = \oint_S \mathbf v\cdot d\mathbf A$.
2. Differentiate, following the particles: $\ddot V = \oint_S \dot{\mathbf v}\cdot d\mathbf A + \oint_S \mathbf v\cdot\frac{d}{dt}(d\mathbf A)$.
3. At $t = 0$ every particle is at rest, so the second integral vanishes, and $\dot{\mathbf v} = \mathbf g$ because the particles are free. Hence $\ddot V(0) = \oint_S \mathbf g\cdot d\mathbf A$.
4. Gauss's law for gravity is $\nabla\cdot\mathbf g = -4\pi G\rho$, so the divergence theorem gives $\oint_S \mathbf g\cdot d\mathbf A = -4\pi G M_{\rm enc}$.
5. For a small cloud around a point, $M_{\rm enc} = \rho\,\delta V$, so $\ddot{\delta V}/\delta V = -4\pi G\rho = -\nabla^2\Phi$, which is minus the trace of the tidal matrix $\partial_i\partial_j\Phi$.

**Result:** $\ddot V(0) = -4\pi G M_{\rm enc}$ for a released cloud of any size, and $\ddot{\delta V}/\delta V = -4\pi G\rho$ for a small one; both vanish where the cloud encloses no mass.

### Fourth-order volume loss in vacuum · formal

**Goal:** With $G = c = 1$, show that a small ball released at rest where $R_{\mu\nu} = 0$ has $\ln(\delta V/\delta V_0) = -\tfrac1{12}E_{ij}E_{ij}\tau^4 + O(\tau^5)$.

1. In a parallel-propagated orthonormal frame along the central geodesic, $B_{ij} = \nabla_j u_i$ obeys $\dot B_{ij} = -B_{ik}B_{kj} - E_{ij}$, with $E_{ij} = R_{\hat\imath\hat 0\hat\jmath\hat 0}$.
2. Released at rest means $B(0) = 0$. Then $B^2 = O(\tau^2)$, so integrating once gives $B_{ij} = -E_{ij}(0)\,\tau + O(\tau^2)$. $B$ stays symmetric, so the rotation stays zero.
3. Take the trace. In vacuum $\operatorname{tr}E = R_{\hat 0\hat 0} = 0$ along the worldline, so $\dot\theta = -B_{ik}B_{ki} = -E_{ij}(0)E_{ij}(0)\,\tau^2 + O(\tau^3)$.
4. Integrate with $\theta(0) = 0$: $\theta = -\tfrac13E_{ij}E_{ij}\tau^3 + O(\tau^4)$.
5. With $\theta = d\ln\delta V/d\tau$, integrate once more: $\ln(\delta V/\delta V_0) = -\tfrac1{12}E_{ij}E_{ij}\tau^4 + O(\tau^5)$.
6. Check it against an exactly constant tide $E = \mathrm{diag}(-2, 1, 1)/\tau_0^2$. The axes then go as $\cosh(\sqrt2\,s)$ and $\cos s$ with $s = \tau/\tau_0$, and $\cosh(\sqrt2\,s)\cos^2 s = 1 - \tfrac12 s^4 + O(s^6)$, while $\tfrac1{12}E_{ij}E_{ij} = \tfrac{6}{12}$ in the same units.

**Result:** $\ln(\delta V/\delta V_0) = -\tfrac1{12}E_{ij}E_{ij}\tau^4 + O(\tau^5)$: no change through third order, then a loss set by the square of the trace-free tide.

## Worked examples

### A one-minute fall near Earth · working

**Problem:** A nonrotating cabin falls freely from rest high above Earth, in vacuum, and a small ball of free particles is released at rest inside it. Take the tidal eigenvalues as constant at $(GM/r^3)(-2, 1, 1)$ with $GM/r^3 = 1.54\times10^{-6}\ \mathrm{s^{-2}}$. Find the fractional changes of the ball's semi-axes and of its volume after 60 s, and compare them.

1. Along an eigen-direction with eigenvalue $\lambda$, a separation released at rest obeys $\ddot\ell = -\lambda\ell$. Writing $q = GM/r^3$, the radial semi-axis grows as $\cosh(\sqrt{2q}\,t)$ and each transverse semi-axis shrinks as $\cos(\sqrt q\,t)$.
2. $\sqrt q\,t = (1.2415\times10^{-3}\ \mathrm{s^{-1}})(60\ \mathrm s) = 0.074492$, so $\cosh(\sqrt2\times0.074492) = \cosh(0.105347) = 1.005554$ and $\cos(0.074492) = 0.997227$.
3. The radial semi-axis is longer by 0.555 per cent and each transverse one shorter by 0.277 per cent, so the egg is longer than it is wide by 0.835 per cent.
4. The volume ratio is $1.005554\times0.997227^2 = 0.9999846$, a loss of $1.54\times10^{-5}$.
5. At order $t^2$ the fractional axis changes are $+qt^2$ once and $-\tfrac12qt^2$ twice, which sum to zero. The whole loss therefore comes from order $t^4$, and $\tfrac12q^2t^4 = 1.54\times10^{-5}$ matches.
6. In 60 s the cabin falls about 17.7 km, which changes $q$ by under 1 per cent, so constant eigenvalues are good enough at this precision.

**Answer:** Radial semi-axis $+0.555$ per cent, each transverse semi-axis $-0.277$ per cent, volume $-1.54\times10^{-5}$. The shape changes about 540 times more than the volume.

**Takeaway:** The zero trace cancels the volume change at order $t^2$, so in the first minute the ball's shape changes hundreds of times more than its volume.

## Problems

### `ball-around-the-moon` · entry · difficulty 1 · calculation

Crumbs are spread over a huge imaginary ball drawn around the whole Moon, 100 kilometres above its surface, so the ball's radius is 1,837 kilometres. All of them are let go at rest, with nothing holding them and no air among them. In ten seconds each crumb falls about 73 metres toward the Moon's centre. The rulers that measure this stay still relative to the Moon's centre. By about how many parts in a million does the room this ball takes up shrink? And why does a small ball of crumbs let go at rest just above the Moon's surface not shrink at first?

**Hints**

1. What fraction of the ball's radius is 73 metres?
2. The ball stays round. In how many directions at right angles does it grow narrower by that fraction?

**Answer:** About 120 parts in a million. The huge ball holds the whole Moon, while a small ball above the Moon's surface holds no mass at all.

**Must contain:** The radius shrinks by about 40 parts in a million; Three directions at right angles add to about 120 parts in a million; Only the huge ball has mass inside it

**Numeric:** fraction of the ball's volume lost in ten seconds = 0.000119 1 (magnitude, ±8%)

**Solution**

1. The radius shrinks by 73 metres out of 1,837,000 metres. That is 73 divided by 1,837,000, about 40 parts in a million.
2. Every crumb falls the same distance toward the Moon's centre, so the ball stays round. It grows narrower by about 40 parts in a million in each of three directions at right angles.
3. For small changes the room a shape takes up changes by the sum of the three fractions: about 120 parts in a million.
4. A small ball just above the Moon's surface holds nothing but empty space among its crumbs. Its stretch along the line toward the Moon's centre balances its two squeezes across that line, so at first it keeps its room.

**Targets:** `mass-nearby-shrinks-the-ball`

### `cube-around-earth` · working · difficulty 2 · calculation

A cube of free particles 100,000 km on each side, centred on Earth, is released from rest; the Moon lies well outside it. With $GM_\oplus = 3.986\times10^{14}\ \mathrm{m^3\,s^{-2}}$, find $\ddot V/V$ at release and the fraction of the cube's volume lost in the first 60 s. Would a sphere of the same volume centred on Earth start any differently?

**Hints**

1. At release the volume acceleration depends only on the mass the surface encloses.

**Answer:** $\ddot V/V = -5.01\times10^{-9}\ \mathrm{s^{-2}}$, and the cube loses about $9.0\times10^{-6}$ of its volume in the first 60 s. A sphere of the same volume centred on Earth starts identically; only the way the two distort differs.

**Must contain:** The volume acceleration is minus four pi G times Earth's mass; Divided by the volume it is about minus 5.01 times ten to the minus nine per second squared; About 9.0 millionths of the volume is lost in 60 seconds; Any shape of the same volume around the same enclosed mass starts the same

**Numeric:** fraction of the cube's volume lost in 60 s = 9e-06 1 (magnitude, ±3%)

**Solution**

1. The cube's corners sit $\sqrt3\times50{,}000 \approx 86{,}600$ km from Earth's centre, well inside the Moon's orbit of about 384,000 km, so the enclosed mass is Earth's alone.
2. Released at rest, $\ddot V(0) = -4\pi GM_\oplus = -4\pi(3.986\times10^{14}\ \mathrm{m^3\,s^{-2}}) = -5.009\times10^{15}\ \mathrm{m^3\,s^{-2}}$.
3. $V = (1.0\times10^{8}\ \mathrm m)^3 = 1.0\times10^{24}\ \mathrm{m^3}$, so $\ddot V/V = -5.01\times10^{-9}\ \mathrm{s^{-2}}$.
4. For a short time $\Delta V/V \approx \tfrac12(\ddot V/V)t^2 = -\tfrac12(5.01\times10^{-9}\ \mathrm{s^{-2}})(3600\ \mathrm{s^2}) = -9.0\times10^{-6}$. The face-centre particles fall only about 300 m in that time, under a hundred-thousandth of the cube's half-width, so the short-time form is accurate.
5. The law depends only on the enclosed mass, so a sphere of equal volume centred on Earth has the same $\ddot V(0)$ and loses the same fraction at first.

### `every-observer-keeps-volume` · formal · difficulty 2 · proof

Set $G = c = 1$ and $\Lambda = 0$. Prove that at an event $x$ every freely falling observer's small ball released at rest has $\ddot{\delta V}(0) = 0$ if and only if $T_{\mu\nu}(x) = 0$. Then show that one observer's zero is not enough, using a perfect fluid with pressure $P = -\rho/3$.

**Hints**

1. Start from the initial volume law, then use the trace-reversed Einstein equation.
2. A symmetric bilinear form that vanishes on every timelike vector vanishes.

**Answer:** Every observer finds zero exactly when $R_{\mu\nu}(x) = 0$, which with $\Lambda = 0$ holds exactly when $T_{\mu\nu}(x) = 0$. For the fluid, the comoving observer finds $R_{\mu\nu}u^\mu u^\nu = 4\pi(\rho + 3P) = 0$, while an observer moving relative to it with Lorentz factor $\gamma$ finds $\tfrac{16\pi}{3}\rho(\gamma^2 - 1) > 0$.

**Must contain:** Vanishing on every timelike vector forces the Ricci tensor to vanish; Trace reversal is invertible in four dimensions, so zero Ricci means zero stress-energy; The fluid with pressure minus one third of its density gives zero only for its own comoving observer

**Solution**

1. For a ball released at rest the initial volume law gives $\ddot{\delta V}/\delta V = -R_{\mu\nu}u^\mu u^\nu$ for the observer with unit four-velocity $u$.
2. If $T_{\mu\nu}(x) = 0$ then Einstein's equation in its trace-reversed form, $R_{\mu\nu} = 8\pi(T_{\mu\nu} - \tfrac12Tg_{\mu\nu})$, gives $R_{\mu\nu}(x) = 0$, so every observer finds zero.
3. Conversely, suppose $R_{\mu\nu}u^\mu u^\nu = 0$ for every unit timelike $u$, hence by scaling for every timelike vector. For timelike $u$ and any $v$, the vector $u + \epsilon v$ is timelike for small $|\epsilon|$, so $2\epsilon R(u,v) + \epsilon^2R(v,v) = 0$ on an interval of $\epsilon$, which forces $R(v,v) = 0$ for every $v$. Polarization then gives $R_{\mu\nu}(x) = 0$.
4. Taking the trace of the trace-reversed equation gives $R = -8\pi T$, so $T = 0$, and then $T_{\mu\nu} = R_{\mu\nu}/8\pi + \tfrac12Tg_{\mu\nu} = 0$.
5. For the perfect fluid, $T_{\mu\nu}u'^\mu u'^\nu = (\rho + P)\gamma^2 - P$ and $T = -\rho + 3P$, so $R_{\mu\nu}u'^\mu u'^\nu = 8\pi\big[(\rho + P)\gamma^2 - \tfrac12\rho + \tfrac12P\big]$.
6. With $P = -\rho/3$ this is $8\pi\cdot\tfrac23\rho(\gamma^2 - 1) = \tfrac{16\pi}{3}\rho(\gamma^2 - 1)$: zero for the comoving observer, where $\gamma = 1$, and positive for every other one, although $T_{\mu\nu} \neq 0$.

## Observations

- **Gravity gradients above Earth measured by the GOCE satellite from 2009 to 2013** (measured, working). GOCE carried three perpendicular pairs of accelerometers whose differences give the Newtonian tidal matrix of a freely falling instrument. Once the satellite's own rotation is taken out, the three diagonal gradients add to zero within the instrument's noise across its measurement band. That zero sum is the volume budget of a small released ball, checked in orbit outside Earth's mass. *Numbers:* About 255 km up, for a spherical Earth, the diagonal entries are $-2.74\times10^{-6}\ \mathrm{s^{-2}}$ along the radius and $+1.37\times10^{-6}\ \mathrm{s^{-2}}$ along each horizontal axis, in the sign convention where a stretch is negative. A 1 m semi-axis released at rest there would grow by 0.137 mm along the radius and shrink by 0.069 mm across it in 10 s. *Reference:* Reiner Rummel, Weiyong Yi, Claudia Stummer (2011), *GOCE gravitational gradiometry*, Journal of Geodesy 85, 777-790, doi:10.1007/s00190-011-0500-0 _(unverified)_
- **A polarization test with GW170814, the first gravitational-wave signal recorded by three detectors** (measured, working). The two LIGO detectors and Virgo point their arms in different directions, so they respond differently to the area-preserving tensor waves of general relativity and to breathing scalar waves, which would change a ring's area. Comparing the three responses, the analysis favoured a purely tensor polarization over purely vector and purely scalar alternatives. *Numbers:* Reported Bayes factors of about 200 for purely tensor against purely vector polarization, and about 1000 against purely scalar. *Reference:* B. P. Abbott, R. Abbott, T. D. Abbott and others (2017), *GW170814: A Three-Detector Observation of Gravitational Waves from a Binary Black Hole Coalescence*, Physical Review Letters 119, 141101, doi:10.1103/PhysRevLett.119.141101 _(unverified)_

## Teaching arc

1. **Predict the egg's room** (entry). Ask for a prediction, then add the three fractional changes and test the adding rule on a calculator. *Why:* The visible stretch makes an unchanged room a real surprise. *Predict:* When tidal drift stretches the ball into an egg, does the egg take up more room, less, or the same? *Visual:* [[falling-ring-of-crumbs]] *Uses:* `ways_in/egg-with-the-same-room`, `checks/room-in-the-egg`
2. **Put the planet inside the ball** (entry). Swap the small ball for a huge ball drawn around the whole Earth, then sort the three balls of the choice check. *Why:* It isolates mass inside the ball as the only thing that starts the volume changing. *Predict:* A huge ball of crumbs drawn around the whole Earth is let go at rest. Does it keep its room, like the small one? *Visual:* [[falling-ring-of-crumbs]] *Uses:* `ways_in/balls-that-shrink`, `checks/which-balls-shrink`
3. **Count the mass inside** (working). Derive the release law from Gauss's law, then test it on a large cloud beside Earth that encloses nothing. *Why:* One flux argument covers every size and shape, unlike the small-ball picture. *Predict:* A cloud 20,000 km across is released beside Earth, with Earth outside it. Does it start to lose volume? *Uses:* `derivations/volume-acceleration-from-gauss`, `ways_in/gauss-law-counts-the-mass-inside`, `checks/big-cloud-beside-earth`
4. **Ride a gravitational wave** (working). Read the wave's equal stretch and squeeze off its trace-free tidal tensor, then work the detector arms. *Why:* The same budget appears with one squeeze instead of two, and it is measured. *Predict:* As a gravitational wave squeezes a ring of free masses into an oval, does the area inside the ring change? *Visual:* [[two-stars-and-a-distant-ring]] *Uses:* `ways_in/ring-of-mirrors-in-a-gravitational-wave`, `checks/mirror-arms-in-a-wave`, `observations/gw170814-polarization-test`
5. **Break each hypothesis** (formal). Run the Raychaudhuri argument to fourth order, break two hypotheses, then compare two observers at one event. *Why:* Graduate readers need what the statement assumes and how long it lasts. *Predict:* In empty flat spacetime, does a small ball released with a gentle shear keep its volume at first? *Uses:* `ways_in/volume-and-shear-of-a-released-ball`, `checks/released-with-a-shear`, `checks/passer-loses-volume-sooner`

## Analogies

### A drop of dye in a slowly stirred glass of water · working

Stir a glass of water gently and add a drop of dye. The blob is drawn out into a long thin ribbon, yet the amount of water in it never changes. In a fluid the fractional rate at which a small blob's volume changes is $\partial_iv_i$, the trace of the velocity-gradient matrix $\partial_iv_j$. Water resists compression, so stirring sets up only flows of zero trace, leaving the trace-free part to do all the reshaping. A released ball of test particles splits the same way.

| In the analogy | Stands for |
| --- | --- |
| the dye blob | the small ball of test particles |
| the velocity-gradient matrix $\partial_iv_j$ of the flow | the matrix $B_{ij}$ of the particles' relative velocities |
| its trace, held at zero by the liquid | the expansion $\theta$, held at zero to leading order in vacuum |
| the trace-free shear of the flow | the trace-free tides, the electric Weyl tensor in vacuum |

*Limits:* Water's trace is zero at every moment, so the blob's volume is conserved exactly. Gravity fixes only the trace of the tides, which sets how fast the expansion changes rather than the expansion itself, so the shear the tides build takes volume away at fourth order in proper time. Diffusion also blurs the dye, with no counterpart here.

## Misconceptions

### “Gravity pulls everything together, so tidal drift squashes a falling ball of crumbs and makes it smaller.” · entry · `tides-squash-the-ball`

- **Why it is tempting:** Gravity attracts, so any change it causes seems to pull things in.
- **What is true:** The stretch along the line toward the planet's centre equals the two squeezes across that line added together. So a small ball let go at rest changes shape at first without changing its room.
- **Exposed by:** `checks/room-in-the-egg`

### “A heavy planet right beside a ball of crumbs squeezes it harder, so that ball must lose room.” · entry · `mass-nearby-shrinks-the-ball`

- **Why it is tempting:** Bigger drifts look like a stronger squeeze.
- **What is true:** A heavier planet makes the stretch and both squeezes bigger together, so they still add to zero. Only mass inside the ball starts its room changing.
- **Exposed by:** `checks/which-balls-shrink`

### “Only a tiny cloud keeps its volume; a big cloud beside Earth must shrink, because its near side is pulled much harder.” · working · `big-cloud-must-shrink`

- **Why it is tempting:** The volume budget is usually derived only for a small ball, so its scope looks narrow.
- **What is true:** In Newtonian gravity a released cloud of any size starts with volume acceleration minus four pi G times the mass inside it. With none inside, only its shape starts to change.
- **Exposed by:** `checks/big-cloud-beside-earth`

### “A gravitational wave squeezes a ring of free masses into an oval, so the area inside the ring shrinks and grows as the wave passes.” · working · `wave-changes-area`

- **Why it is tempting:** Pictures of a passing wave show the ring squashed, and a squashed ring looks smaller.
- **What is true:** The ring stretches along one direction by the fraction it squeezes along the perpendicular one, so its area holds to first order in the strain. Changing it would take a breathing polarization, which general relativity does not have.
- **Exposed by:** `checks/mirror-arms-in-a-wave`

### “In any vacuum region a small ball of free particles keeps its volume at first, however it is released.” · formal · `vacuum-always-keeps-volume`

- **Why it is tempting:** Vacuum tides are trace-free, and the slogan usually drops the conditions on the release and on the cosmological constant.
- **What is true:** A ball released with shear loses volume at once, even in flat spacetime. A positive cosmological constant makes a ball released at rest start to grow.
- **Exposed by:** `checks/released-with-a-shear`

### “Observers at one event who agree that a released ball keeps its volume at first also agree on how long it stays nearly unchanged.” · formal · `balance-lasts-equally-for-all`

- **Why it is tempting:** The zero trace holds for every observer, so the whole volume history seems observer-independent.
- **What is true:** The fourth-order loss is set by the square of the electric Weyl tensor, which changes under boosts. A ball released by an observer passing a mass sideways loses volume sooner.
- **Exposed by:** `checks/passer-loses-volume-sooner`

## Checks

1. **Entry · predict** `checks/room-in-the-egg`. Crumbs are let go at rest on an imaginary ball 2 metres across, around a centre crumb, in a cabin falling freely above a planet. Nothing else is among them. In one minute a crumb 1 metre out along the line toward the planet's centre drifts away from the centre crumb by 0.60 millimetres. A crumb 1 metre out across that line drifts in by 0.30 millimetres. A friend says gravity pulls everything together, so the ball must end up taking less room. Is the friend right?
   - **Hints:** Write each drift as a fraction of 1 metre, then add the three, counting narrower as negative.
   - **Answer:** No. Inside a falling cabin only the differences in pull show, and they stretch the ball as well as squeeze it. A metre is 1,000 millimetres, so 0.60 millimetres is 600 millionths of a metre. Along the line the ball is longer by 600 parts in a million. Across it, in each of two directions, the ball is narrower by 300 parts in a million. For small changes the room changes by the sum of those fractions. Since 600 minus 300 minus 300 is zero, the room stays the same, to better than one part in a million.
   - **Must contain:** The room stays the same; Plus 600, minus 300 and minus 300 parts in a million add to zero
   - **Numeric:** fractional change in the room the ball takes up = 0 1 (signed, ±1e-06)
   - **Targets:** `tides-squash-the-ball`
   - **Visual:** [[falling-ring-of-crumbs]]
2. **Entry · choice** `checks/which-balls-shrink`. Three balls of crumbs are let go at rest, with no air among them. Ball A is 2 metres across, beside a planet where every drift is 8 times as big as near Earth's surface. Ball B is 2 metres across, just above the Moon's surface. Ball C is drawn around the whole Moon, 100 kilometres above its surface. Which start to shrink?
   - **Hints:** Which of the three balls has any mass inside it?
   - **Answer:** Only ball C. A ball of crumbs let go at rest starts to change the room it takes up only if mass sits inside it. Ball A holds nothing but empty space. Its planet makes the stretch 8 times as big, but it makes both squeezes 8 times as big too, so the three fractions still add to zero. Ball B is the same, with the Moon's smaller drifts. Ball C holds the whole Moon, so each of its crumbs falls toward the Moon's centre by the same amount and the ball shrinks.
   - **Must contain:** Only ball C shrinks; Only mass inside a ball starts its room changing, and bigger drifts still add to zero
   - **Targets:** `mass-nearby-shrinks-the-ball`
3. **Working · evaluate-claim** `checks/big-cloud-beside-earth`. A spherical cloud of free particles 20,000 km across is centred 20,000 km from Earth's centre, so Earth lies outside it, and every particle is released from rest. Claim: the near side is pulled much harder than the far side, so the cloud must start to lose volume. Treat Earth as a Newtonian point mass. Evaluate the claim, and say what does start to change.
   - **Hints:** At release, what does Gauss's law say about the flux of the gravitational field through the cloud's surface?
   - **Answer:** The claim is false. At release every particle is at rest, so $\ddot V(0) = \oint_S \mathbf g\cdot d\mathbf A$, the flux of the field through the surface. Gauss's law makes that flux $-4\pi G M_{\rm enc}$, and this cloud encloses no mass, so $\ddot V(0) = 0$ exactly, whatever its size. The near side does accelerate faster than the centre, but the far side lags behind it and the sides converge, and these cancel in the flux. The shape is what changes: the cloud lengthens toward Earth and narrows across, and since the tidal field varies strongly over a cloud this large, that shape is not a simple ellipsoid.
   - **Must contain:** At release the volume acceleration is the flux of the field, which Gauss's law makes zero with no mass inside; Only the shape starts to change, and not into a simple ellipsoid
   - **Targets:** `big-cloud-must-shrink`
4. **Working · numeric** `checks/mirror-arms-in-a-wave`. A plus-polarized gravitational wave arrives along the $z$ axis of a freely falling observer. At one instant it has lengthened a 4 km row of free masses along $x$ by $2.0\times10^{-18}$ m. How do equal rows along $y$ and $z$ change, and by what fraction does the area of a ring in the $xy$ plane change, to first order in the strain?
   - **Hints:** Find the strain from the change along $x$, then multiply the fractional changes along $x$ and $y$.
   - **Answer:** $\delta L_x/L = h_+/2 = (2.0\times10^{-18}\ \mathrm m)/(4000\ \mathrm m) = 5.0\times10^{-22}$, so $h_+ = 1.0\times10^{-21}$. Since $\delta L_y/L = -h_+/2$, the row along $y$ shortens by $2.0\times10^{-18}$ m, and along the direction of travel nothing changes. The area scales as $(1 + h_+/2)(1 - h_+/2) = 1 - h_+^2/4$, unchanged to first order; the leftover $h_+^2/4 = 2.5\times10^{-43}$ is far beyond any measurement. That is the vacuum budget, one stretch against one equal squeeze, because the wave's tidal tensor is trace-free.
   - **Must contain:** The row along y shortens by the same amount that x lengthened, and z does not change; The ring's area is unchanged to first order in the strain
   - **Numeric:** change in the row along y = -2e-18 m (signed, ±2%); change in the row along z = 0 m (signed, ±1e-20); first-order fractional change in the ring's area = 0 1 (signed, ±1e-30)
   - **Targets:** `wave-changes-area`
   - **Visual:** [[two-stars-and-a-distant-ring]]
5. **Formal · evaluate-claim** `checks/released-with-a-shear`. Claim: in any vacuum region a small ball of free particles keeps its volume at first. Test it twice. (a) In flat spacetime a ball is released with $v_i = S_{ij}x_j$, where $S = \mathrm{diag}(s, -s, 0)$ and $s = 1.0\times10^{-3}\ \mathrm{s^{-1}}$; find its volume ratio after 60 s. (b) In de Sitter spacetime, where $R_{\mu\nu} = \Lambda g_{\mu\nu}$, a ball is released at rest. Which hypothesis fails in each case?
   - **Hints:** With no forces, write each particle's position at time $t$ and take the determinant.
   - **Answer:** It fails both times. (a) No forces act, so $x(t) = (1 + St)x_0$ and $V/V_0 = \det(1 + St) = (1 + st)(1 - st) = 1 - s^2t^2 = 0.9964$ after 60 s. So $\ddot V/V = -2s^2 = -2\times10^{-6}\ \mathrm{s^{-2}}$ from the start, comparable with Earth's tidal entries. Raychaudhuri agrees: with $\theta = \omega = 0$, $R_{\mu\nu} = 0$ and $\sigma_{\alpha\beta}\sigma^{\alpha\beta} = 2s^2$, $\dot\theta = -2s^2$. Release at rest is the hypothesis that fails. (b) Here $R_{\mu\nu}u^\mu u^\nu = -\Lambda c^2$, so $\ddot{\delta V}/\delta V = +\Lambda c^2$ and the ball starts to grow, at about $1\times10^{-35}\ \mathrm{s^{-2}}$ today. Here $R_{\mu\nu} = 0$ fails, since vacuum gives it only when $\Lambda = 0$.
   - **Must contain:** The sheared ball's volume ratio is 0.9964 after 60 seconds; Shear removes volume at once, even with zero curvature, and a positive cosmological constant makes a released ball grow
   - **Numeric:** volume ratio of the sheared ball after 60 s = 0.9964 1 (magnitude, ±0.05%)
   - **Targets:** `vacuum-always-keeps-volume`
6. **Formal · numeric** `checks/passer-loses-volume-sooner`. Set $G = c = 1$. Just outside a spherical mass, a freely falling observer momentarily at rest measures the tidal tensor $q\,\mathrm{diag}(-2, 1, 1)$, with $q = M/r^3$ and the first axis along the radius. One passing sideways at $\beta = 0.6$ measures $q\,\mathrm{diag}(-3.6875, 2.6875, 1)$, her second axis along her motion. Each releases a small ball at rest. Find $E_{ij}E_{ij}$ for each, and the ratio of their proper times for the same small fractional volume loss.
   - **Hints:** Square and add the diagonal entries, then hold the fractional loss fixed and solve for the proper time.
   - **Answer:** Both traces vanish, $-2 + 1 + 1 = 0$ and $-3.6875 + 2.6875 + 1 = 0$, so both balls keep their volume through third order in proper time. The fourth-order law $\ln(\delta V/\delta V_0) = -\tfrac1{12}E_{ij}E_{ij}\tau^4$ separates them. At rest $E_{ij}E_{ij} = (4 + 1 + 1)q^2 = 6q^2$; for the passer, $(13.598 + 7.223 + 1)q^2 = 21.82q^2$. A fixed small loss needs $\tau^4 \propto 1/E_{ij}E_{ij}$, so her proper time is $(6/21.82)^{1/4} = 0.724$ of his. Her ball loses volume sooner, because $E_{ij}E_{ij}$ is not invariant under boosts although its vanishing trace is.
   - **Must contain:** Both tidal tensors have vanishing trace; E i j E i j is 6 and about 21.82 in units of q squared; The ratio of the times is about 0.724
   - **Numeric:** E i j E i j for the passer in units of q squared = 21.82 1 (magnitude, ±1%); ratio of the passer's proper time to the resting observer's = 0.724 1 (magnitude, ±1%)
   - **Targets:** `balance-lasts-equally-for-all`

## Notation traps

| Issue | Course choice | Variants you will meet |
| --- | --- | --- |
| What the strain of a gravitational wave measures | With $h^{\rm TT}_{ij} = h_+e^+_{ij} + h_\times e^\times_{ij}$ and $e^+_{ij} = p_ip_j - q_iq_j$, free masses along $\mathbf p$ change their separation by $\delta L/L = h_+/2$, and arms along $\mathbf p$ and $\mathbf q$ give $(\delta L_x - \delta L_y)/L = h_+$ for a wave arriving along $\mathbf n$. | Detector papers call the difference $(\delta L_x - \delta L_y)/L$ the strain $h(t)$, and sometimes describe one arm as changing by $hL$, twice the single-arm change for an optimally oriented plus wave. Always say whether a quoted strain is one arm or the difference. |

## Visuals

- ★ [[falling-ring-of-crumbs]] (flagship): The central picture: a falling ball of crumbs becomes an egg whose volume meter stays flat at first, beside a ball drawn around the whole planet, which shrinks. *Sketch:* This concept adds a volume meter and a size switch. Presets: a small ball beside the planet, a large cloud beside it that does not contain it, and a ball drawn around the whole planet. Readouts give the fractional stretch along the line to the planet's centre, each squeeze across it, their sum, and the volume ratio. A time slider runs past the first minute, so the slow fourth-order loss shows while the sum stays at zero. A shear-at-release toggle and a cosmological-constant slider break the balance one hypothesis at a time.
- [[two-stars-and-a-distant-ring]] (supporting): The zero trace in a travelling tide: a distant ring of free masses stretches one way and squeezes the other equally, so its area holds. *Sketch:* This concept adds an area readout for the distant ring, fractional stretch readouts along two perpendicular axes with their sum, and a switch to an invented breathing wave that grows and shrinks the ring evenly. The area readout moves only in that invented case.

## Tutor moves

**Open with**

- Picture a small ball of crumbs let go at rest inside a cabin that falls freely near Earth, with nothing among the crumbs. Tidal drift stretches it into an egg shape. Does the egg take up more room than the ball, less, or the same? *(prediction)*
- Now picture crumbs spread over a huge ball drawn around the whole Earth, high above the air, all let go at rest. Does this ball keep its room at first, like the small one? *(prediction)*

**If the learner is stuck**

- *The learner does not believe that small fractional changes of a length and two widths add up to the change in the room.* → Multiply out 1.002 by 0.999 by 0.999, then 1.2 by 0.9 by 0.9, and compare each with the sum of its fractions. *Uses:* `ways_in/egg-with-the-same-room`
- *The learner accepts that the fractions add to zero but cannot see why a nearby planet does nothing to the room.* → Take the ball's near side and far side one at a time, and have the learner say which way each crumb moves compared with the centre crumb. *Uses:* `ways_in/balls-that-shrink`, `checks/which-balls-shrink`
- *The learner answers a question about the room with a statement about the shape, or the other way round.* → Ask for both answers separately, in numbers: how much longer than wide the egg is, and by what fraction its room changed. *Uses:* `worked_examples/one-minute-fall-near-earth`

**Common questions**

- *Does the egg keep the room it takes up forever?* (entry) No, only at first. As the egg grows longer and thinner, the rule that the fractions add stops working, and the room does start to shrink. Near Earth that is very slow. After a whole minute of falling freely, the egg is longer than it is wide by about eight parts in a thousand. Yet its room has shrunk by only about fifteen parts in a million. *Uses:* `ways_in/egg-with-the-same-room`, `worked_examples/one-minute-fall-near-earth`
- *Is the volume law exact, or only a first approximation?* (working) Two statements are in play. In Newtonian gravity $\ddot V(0) = -4\pi G M_{\rm enc}$ is exact for a released cloud of any size and shape, but only at the instant of release. In general relativity the exact statement is local: $\ddot{\delta V}/\delta V = -R_{\mu\nu}u^\mu u^\nu$ holds in the limit of a small ball, because a finite cloud's volume depends on which events count as simultaneous. Past the first instant the Raychaudhuri equation takes over. *Uses:* `ways_in/gauss-law-counts-the-mass-inside`, `ways_in/volume-and-shear-of-a-released-ball`

**Switching levels**

- To working when: asks for a formula for the volume change; asks whether a cloud has to be small for the rule to hold. Derive the release law from Gauss's law, then read off a wave's equal stretch and squeeze. *Uses:* `ways_in/gauss-law-counts-the-mass-inside`, `ways_in/ring-of-mirrors-in-a-gravitational-wave`
- To formal when: asks how long the volume stays constant; asks what exactly released at rest means. Give the Raychaudhuri argument to fourth order, then break each hypothesis with the sheared ball and the cosmological constant. *Uses:* `ways_in/volume-and-shear-of-a-released-ball`, `checks/released-with-a-shear`
- To research when: asks about visualizing black-hole mergers, weak lensing, or testing general relativity with wave polarizations. Open the research horizon. *Uses:* `research_horizon/tidal-tendex-lines`, `research_horizon/lensing-convergence-and-shear`, `research_horizon/polarization-tests`

**Pronunciations:** Ricci → REE-chee; Weyl → VILE; Raychaudhuri → ray-CHOWD-hoo-ree; Poisson → pwah-SOHN; Kretschmann → KRETCH-mahn; GOCE → GOH-chay; LIGO → LIE-go; Virgo → VUR-go

**Voice notes:** At entry, say "at first" every time the balance is stated, and keep "room" for the everyday word and "volume" for the named one.

## History

- **Simeon Denis Poisson (1813).** Extended Laplace's equation for the gravitational potential to points inside matter, in modern notation $\nabla^2\Phi = 4\pi G\rho$: the Newtonian statement that the trace of the tides is set by the local density.
- **Albert Einstein (1915).** Gave the final field equations, whose vacuum form $R_{\mu\nu} = 0$ makes the tidal trace vanish for every freely falling observer outside matter. Albert Einstein (1915), *Die Feldgleichungen der Gravitation*, Sitzungsberichte der Koeniglich Preussischen Akademie der Wissenschaften (Berlin), 844-847 _(unverified)_
- **Amal Kumar Raychaudhuri (1955).** Derived, for the freely falling dust of a cosmological model, the evolution equation for the expansion of its worldlines, with separate terms for shear, rotation and the Ricci tensor. Amal Kumar Raychaudhuri (1955), *Relativistic cosmology. I*, Physical Review 98, 1123-1126, doi:10.1103/PhysRev.98.1123 _(unverified)_

## Research horizon

- **Tidal tendex lines.** In vacuum the tidal tensor is trace-free at every event, so along its three eigen-directions a stretch is always paid for by squeezes. Drawing the eigenvector fields as tendex lines, labelled by their eigenvalues, maps where merging black holes stretch and squeeze nearby matter, and how those patterns travel away as gravitational waves. Robert Owen, Jeandrew Brink, Yanbei Chen, Jeffrey D. Kaplan and others (2011), *Frame-dragging vortexes and tidal tendexes attached to colliding black holes: visualizing the curvature of spacetime*, Physical Review Letters 106, 151101, doi:10.1103/PhysRevLett.106.151101 _(unverified)_
- **Convergence and shear of light beams.** For a narrow bundle of light rays, matter inside the beam focuses it through the Ricci term, while mass beside the beam enters only through the Weyl term, which shears the beam's cross-section: the light-ray twin of the egg. Weak-lensing surveys measure that shear in the shapes of background galaxies to map mass, dark matter included, lying beside the lines of sight. Matthias Bartelmann, Peter Schneider (2001), *Weak gravitational lensing*, Physics Reports 340, 291-472, doi:10.1016/S0370-1573(00)00082-X _(unverified)_
- **Testing the polarizations of gravitational waves.** General relativity allows only two polarizations, both transverse and trace-free, so a ring of free masses keeps its area. General metric theories allow up to six, including a breathing mode that changes the area. Networks of differently oriented detectors compare each signal with these patterns, a programme that began with the first three-detector event. Clifford M. Will (2014), *The Confrontation between General Relativity and Experiment*, Living Reviews in Relativity 17, 4, doi:10.12942/lrr-2014-4 _(unverified)_; B. P. Abbott, R. Abbott, T. D. Abbott and others (2017), *GW170814: A Three-Detector Observation of Gravitational Waves from a Binary Black Hole Coalescence*, Physical Review Letters 119, 141101, doi:10.1103/PhysRevLett.119.141101 _(unverified)_

## Review: novice

**Verdict:** fixed (2026-09-13, revision 4)

**Retell attempt:** In a cabin falling freely down a tower, you let go of crumbs on a ball 2 metres across. In ten seconds the ones along the line to Earth's centre drift out 0.154 millimetres and the ones across drift in half as far, so the ball turns into an egg. You turn those into parts in a million and add: 154 minus 77 minus 77 is zero, so the egg takes up the same room at first, which you can check by multiplying on a calculator. A giant ball around the whole Earth does shrink, because Earth is inside it; mass outside only changes the shape. I wasn't sure whether the crumbs fill the ball or sit on its outside, how millimetres became parts in a million, why adding fractions works for an egg when the check used a box, why the egg later shrinks instead of growing, and whether the centre crumb counts as mass inside.

**Stumbles (30)**

- “How tides reshape a small falling ball of crumbs”: Two words for one idea: the tagline says 'tides' while every entry field says 'tidal drift', and 'tides' makes a reader think of the sea.
- “Let go of a small ball of crumbs ... so the ball becomes an egg with, at first, the same volume.”: 'A ball of crumbs' reads as a clump of crumbs, and the comma-wrapped 'at first' made the sentence a reread.
- “Only mass inside a ball of falling crumbs makes its volume start to change.”: Fails the first what-if: crumbs thrown outward change volume with no mass inside, and Einstein's theory adds a tiny growth in empty space. The rule is Newton's, for a release at rest.
- “Crumbs let go at rest inside it slowly drift compared with a centre crumb”: A step left implicit: nothing says why they drift, yet the first check's answer relies on 'only differences in pull show'.
- “Near a round planet they drift away along the line toward the planet's centre”: 'Away' from what?
- “hundreds of crumbs are held still on an imaginary ball 2 metres across, around one centre crumb”: Unclear whether the crumbs fill the ball or sit on its surface, held still relative to what, and where the centre crumb is.
- “A crumb 1 metre out on the line toward Earth's centre drifts away from the centre crumb by 0.154 millimetres.”: There are two such crumbs, one nearer Earth and one farther; the reader wonders whether the far one drifts too.
- “The ball becomes egg-shaped, longer along the line and narrower across it.”: First what-if: a real egg is fatter at one end, but this shape is the same at both ends.
- “Measure each change as a fraction of 1 metre. Along the line, the egg is longer by 154 parts in a million.”: A missing step: how 0.154 millimetres becomes 154 parts in a million.
- “You can check this with a box: 1.002 metres long and 0.999 metres wide and deep, it holds 0.999997 cubic metres.”: The reader must supply the comparison with 1 cubic metre and the zero sum of the box's fractions, and gets no reason for the tiny leftover.
- “For the egg, the sum is 154 minus 77 minus 77, which is zero.”: The check used a box, and an egg is not a box; the link is left implicit.
- “is called a volume-preserving tidal deformation”: 'Preserving' and 'deformation' are unfamiliar words.
- “Over a much longer fall, the egg's volume does start to shrink slowly.”: A surprise with no reason or number: why shrink rather than grow, and how slowly?
- “a block 2 parts in 100 longer ... for big changes, the fractions no longer add up.”: 'Block' and 'box' name one object, and 'the fractions no longer add up' is ambiguous: they still add to zero, but the sum stops giving the volume.
- “tidal drift stretches a small falling ball of crumbs along one line and squeezes it half as much in two directions across”: The takeaway names no line and drops 'let go at rest', so it fails for crumbs thrown apart.
- “Crumbs let go at rest in a cabin that falls freely near Earth drift.”: A reread: the verb arrives after a long subject. The recap also leaves out why the sum is zero.
- “400 kilometres above the ground, beyond the air. ... Each crumb is held still”: Not quite true (a thin trace of air remains at 400 kilometres), no everyday anchor for the height, and held still relative to what?
- “All the crumbs are the same distance from Earth's centre, so none falls ahead of the others. The ball stays round and shrinks.”: A step left implicit: falling toward Earth's centre is moving inward because Earth's centre is the ball's centre.
- “The ball's radius is 6,771 kilometres”: Where 6,771 comes from is not shown.
- “The ball is narrower by that fraction in each of three directions at right angles.”: Which three directions? A round ball shrinks in every direction.
- “Compare the small ball beside Earth.”: Which small ball, and is it fair to compare a ball measured with cabin rulers against one measured with rulers still relative to Earth?
- “The difference is what sits inside each ball. ... Newton's law of gravity turns this into a rule, which we take on trust here.”: A surprising claim with no reason: why should mass inside matter and mass outside not? 'Turns this into a rule' is vague.
- “Its walls pull on the crumbs very slightly, but they sit outside the small ball, so they cannot start to change its volume either.”: 'Its' and 'they' have two candidates each, and the first what-if is unanswered: the centre crumb is itself mass inside the ball.
- “A ball of crumbs let go at rest starts to shrink only when mass sits inside it.”: The takeaway is unscoped, while the way takes Newton's law on trust and Einstein's theory adds a tiny growth in empty space.
- “a ball of crumbs 2 metres across is let go at rest, with nothing among the crumbs ... drifts away from the centre crumb”: The check uses 'the centre crumb' without introducing it, and the starting arrangement is ambiguous.
- “The volume stays the same, to within 2 parts in 100 million.”: The entry ways gave no way to reach this figure.
- “with no air around them”: Air among the crumbs is what would matter, not only around them.
- “the ball stretches along the line toward the planet's centre by as much as it squeezes across that line in total”: A reread: 'in total' arrives at the end, after the reader has pictured one squeeze.
- “about 150 parts in a million, which is 0.015 per cent”: A missing step from parts in a million to per cent.
- “After a whole minute of falling,”: No setting: falling where? The numbers hold only near Earth.

**Fixes**

- Rewrote the tagline and summary to use 'tidal drift', spread the crumbs over the surface of an imaginary ball, and scoped the only-mass-inside rule to Newton's law and a release at rest.
- Egg way: said why crumbs drift, named both crumbs on the line, placed the centre crumb, converted millimetres to parts in a million, walked the box check step by step, and gave the reason for the tiny leftover. Added the sentence linking the box to the egg, defined 'preserving' and 'deformation' in the sentence before the term and in the glossary, added the one-minute number, and marked 'shrinks rather than grows' as taken on trust.
- Egg way try_it: one word ('box') for the object, and it now says the fractions still add to zero while the volume has changed.
- Whole-Earth way: gave Earth's radius, the space station as a height anchor, 'above almost all of the air', and the step that falling toward Earth's centre is moving inward. Said why cabin and ground rulers can be compared, and gave the reason mass inside and mass outside differ (all inward, against ahead-and-lag balancing). Answered the centre-crumb what-if with a size, and scoped the takeaway to Newton's law.
- Checks, problem, misconception and common question: introduced the centre crumb in the first check, said where its 2-parts-in-100-million leftover comes from, put the air among the crumbs, spelled out the per cent step, and gave the common question its setting.
- Checked numbers with python3: 1.002 x 0.999 x 0.999 = 0.999997; (1 + 154e-6)(1 - 77e-6)^2 = 1 - 1.8e-8, under 2 parts in 100 million; one crumb of 1 milligram 1 metre away moves a crumb about 3e-15 metres in ten seconds, far smaller than an atom; 435 m / 6,771 km = 64 parts in a million.
- Ladder: the working way 'Gauss's law counts the mass inside' now names the 193 parts in a million of 'A ball around the whole Earth shrinks' instead of 'the entry figure', and bridges from the entry rule that small fractions add to $\delta V/V \approx \sum_i \delta\ell_i/\ell_i$. Every non-entry way's first sentence already names the way it continues, index notation at working is covered through ricci-tensor, and the five ways use five different kinds.
- Budget: entry explanations grew from 646 to about 990 words, still under the 1,000 cap; extras 700 of 800; nothing was dropped or compressed.
- Bumped the revision to 2.

**Concerns**

- Physics reviewer: confirm the new entry claims: that the volume loss over a longer fall is a shrink (the entry prose takes this on trust), that a centre crumb's own pull is negligible (about 3e-15 metres in ten seconds for 1 milligram), and that cabin and ground rulers agree on the ball's size far more closely than 193 parts in a million.
- The entry prose attributes the only-mass-inside rule to Newton's law. It says nothing about the cosmological constant making a ball grow in empty space, beyond 'as closely as anyone could ever measure' in the egg way; the ricci-tensor entry way covers that exception.
- Entry explanations now sit near the 1,000-word core cap, so later entry additions will need cuts elsewhere.
- The 'egg' shape is a symmetric oval (both ends alike); the proposed visual falling-ring-of-crumbs should draw it that way, not as a real egg with one pointed end.
- Carried over from drafting: the conventions file has no symbols for an observer's tidal tensor or the electric and magnetic Weyl parts, and the GW170814 Bayes factors and the Bartelmann and Schneider reference still need checking.

**Re-read** (2026-09-16, revision 4): 18 stumbles in 30 changed passages

- “Why tidal drift changes a falling ball's shape long before it changes its volume”: Unscoped: the note's own huge ball around Earth changes its volume at once and its shape not at all.
- “Near a round planet they drift away from that centre crumb ... and in toward it from across that line, half as far.”: 'Near' includes inside the planet, where the half-as-far rule fails; 'in toward it from across' is a reread.
- “A small ball of them grows longer along the line toward Earth's centre by some fraction, and narrower by half that fraction in each of two directions across the line.”: Thirty-word sentence pushed the recap's average past 20 words (validator warning).
- “The centre crumb sits at the ball's centre, and nothing else floats among them.”: 'The centre crumb' arrives as if already known; the term is new here (rule 4).
- “An egg's room is also its length times its two widths”: Read literally it is false: an egg's room is about half that product. The rule needs only that the room is set by the product.
- “at first the egg takes up exactly the room the ball took”: 'Exactly' contradicts the box check two sentences earlier, which left 3 millionths over.
- “Both boxes have fractions that add to zero, plus 2 against minus 1 twice”: The two boxes use thousandths and tenths; 'plus 2 against minus 1' names neither, and the 32-word sentence needed a reread.
- “Measured from Earth's centre, each falls about 435 metres in ten seconds.”: A measurement without its instrument (rule 7): measured with what, held still relative to what?
- “crumbs nearer Earth fall ahead of the centre crumb while crumbs farther from it lag behind”: 'It' could be Earth or the centre crumb.
- “By Newton's law of gravity, which we take on trust here, this holds for a ball of any size.”: 'This' points at the previous sentence about crumbs moving out and in, but the rule it means comes next.
- “Its cabin's walls lie outside it, so their pull does not count.”: 'Does not count' toward what? The rule is about starting the room changing.
- “In ten seconds each crumb falls about 73 metres toward the Moon's centre, measured from the Moon's centre.”: No instrument for the measurement (rule 7).
- “a small ball of crumbs floating just above the Moon's surface”: 'Floating' suggests the crumbs hover; they are let go at rest and fall.
- “In one minute a crumb 1 metre out along the line toward the planet's centre drifts away by 0.60 millimetres, and one 1 metre out across that line drifts in by 0.30 millimetres.”: Thirty-five-word sentence (validator warning); 'drifts away' from what; 'one 1 metre' reads as a typo.
- “A metre is 1,000 millimetres, so the ball is longer by 600 parts in a million along the line, and narrower by 300 parts in a million across it in each of two directions.”: Thirty-five-word sentence (validator warning) that skips the step from 0.60 millimetres to 600 millionths.
- “Ball C is drawn around the whole Moon, 100 kilometres up.”: 'Up' from where (rule 6)?
- “After a whole minute of falling freely, the egg is longer than it is wide by about eight parts in a thousand, yet its room has shrunk by only about fifteen parts in a million.”: Thirty-five-word sentence (validator warning).
- “At release, what does Gauss's law say about the flux through the cloud's surface?”: Working rung: flux of what? The key point names the field.
- Fix: Entry: scoped the tagline to a ball with nothing inside; recap of the egg way says 'Outside a round planet'; introduced the centre crumb as a new term; 'set by its length times its two widths'; dropped 'exactly'; try_it names thousandths and tenths and is split in two; whole-Earth way names the rulers, replaces 'it' with 'Earth', replaces the dangling 'this' and 'does not count'; Moon problem names the rulers and replaces 'floating' with 'let go at rest'; ball C is 100 kilometres above the Moon's surface; the three 35-word sentences in room-in-the-egg and does-it-last and the 30-word recap sentence were split without dropping words.
- Fix: Working: the big-cloud hint names the gravitational field; the wave way no longer calls 1 - h^2/4 the exact area factor; the mirror-arms answer calls 2.5e-43 the leftover of the first-order product; 17.6 km became 17.7 km in the one-minute example.
- Fix: No claim was changed except where the physics pass required it (tagline scope, 'exactly', 'exact area factor', 17.7 km). Entry way explanations 867 words, extras 700, within the caps.

## Review: physics

**Verdict:** fixed (2026-09-16, revision 4)

**Verification**

- Egg way and checks: 0.154 mm and 0.077 mm drifts at 1 m in 10 s near Earth's surface; egg longer than wide by under half a millimetre.: python3: q = GM/r^3 = 1.541e-6 s^-2 at r = 6371 km; q t^2 = 1.54e-4 m; half for transverse; 2(1+154e-6) - 2(1-77e-6) = 0.462 mm. → Correct; 0.462 mm is about six hairs of 70 micrometres.
- Box checks: 1.002 x 0.999 x 0.999 = 0.999997 (3 millionths lost) and 1.2 x 0.9 x 0.9 = 0.972.: python3. → 0.999997002 and 0.972; correct.
- room-in-the-egg: +600, -300, -300 parts in a million leave the room unchanged to better than one part in a million.: python3: 1.0006 x 0.9997^2 - 1 = -2.7e-7. → Correct; numeric answer 0 with abs_tol 1e-6 matches.
- Whole-Earth way: 435 m fall in 10 s at 400 km, 64 parts in a million of 6,771 km, 193 parts in a million of the volume; working way's -3.85e-6 s^-2 and 1.93e-4.: python3: g = GM/r^2 = 8.694 m/s^2, half g t^2 = 434.7 m; 3 x 434.7/6.771e6 = 1.926e-4; 3GM/r^3 = 3.852e-6 s^-2. → Correct.
- ball-around-the-moon: 73 m fall in 10 s at 1,837 km from the Moon's centre; about 40 then 120 parts in a million.: python3 with GM_moon = 4.9048e12 m^3 s^-2: g = 1.453 m/s^2, fall 72.7 m, 73/1.837e6 = 3.97e-5, times 3 = 1.19e-4. → Correct; numeric 1.19e-4 with rel_tol 0.08 matches.
- which-balls-shrink: only ball C shrinks; a planet 8 times the drifts scales stretch and both squeezes alike.: Release law: V''(0) = -4 pi G M_enc for any released cloud; the tidal matrix scales with GM/r^3 and stays trace-free. → Correct.
- cube-around-earth: V''(0) = -5.009e15 m^3 s^-2, V''/V = -5.01e-9 s^-2, 9.0e-6 lost in 60 s, corners at 86,600 km, face centres fall about 300 m.: python3: -4 pi x 3.986e14; /1e24; half x 5.01e-9 x 3600; sqrt(3) x 50,000; half x GM/(5e7)^2 x 3600 = 287 m. → Correct; 287 m is 5.7e-6 of the half-width, under a hundred-thousandth.
- one-minute-fall-near-earth: sqrt(q) t = 0.074492, cosh(0.105347) = 1.005554, cos = 0.997227, egg longer than wide by 0.835 per cent, volume loss 1.54e-5, ratio about 540, cabin falls 17.7 km.: python3 with q = 1.5414e-6 s^-2: values 1.0055542, 0.9972268, 0.0083506, 1.537e-5 (series 0.5 q^2 t^4 = 1.540e-5), ratio 543, half g t^2 = 17,676 m. → All correct except the fall distance: 17.7 km, not 17.6 km; fixed. Either value changes q by 0.84 per cent, under 1 per cent as stated.
- GOCE numbers: -2.74e-6 and +1.37e-6 s^-2 at 255 km in the convention where a stretch is negative; 0.137 mm and 0.069 mm in 10 s.: python3: GM/r^3 at r = 6626 km = 1.370e-6 s^-2; radial entry -2GM/r^3; 1 m x 1.37e-6 x 100 s^2. → Correct; sign matches the course tidal matrix, radial eigenvalue of d_i d_j Phi negative outside a mass.
- small-ball-volume-law conditions: for matter at rest relative to the observer, -R_mu nu u^mu u^nu = -4 pi G (rho + 3p/c^2) + Lambda c^2.: Hand algebra from R_mu nu = (8 pi G/c^4)(T_mu nu - T g_mu nu/2) + Lambda g_mu nu with the course perfect fluid: T_mu nu u u = rho c^4, T = -rho c^2 + 3p, g_mu nu u u = -c^2. → Correct, including the sign of the Lambda term and the units (Lambda c^2 in s^-2).
- Boosted observer at 0.6c sideways past a spherical mass sees (GM/r^3) diag(-3.69, 2.69, 1).: Transverse boost of the Schwarzschild electric Weyl tensor: diag(-(2 + 3 gamma^2 beta^2), 1 + 3 gamma^2 beta^2, 1) with gamma^2 beta^2 = 0.5625. → -3.6875, 2.6875, 1; trace zero; correct.
- mirror-arms-in-a-wave: h_+ = 1.0e-21 from 2.0e-18 m over 4000 m; y row shortens by the same; area factor 1 - h^2/4 with leftover 2.5e-43; 4e-18 m is about 400 proton widths smaller.: python3: 2e-18/4000 = 5e-22; h^2/4 = 2.5e-43; 1.7e-15/4e-18 = 425. → Arithmetic correct. 'The exact area factor' was overstated: the length law is first order in h_+, and the exact TT-gauge proper lengths give a different second-order term (about h^2/2), so the way now calls it the product of the two first-order factors and the check calls 2.5e-43 the leftover of that product.
- Tidal tensor of a plus wave -(1/2) h''_+ diag(1,-1,0) and the length law delta L/L = +-h_+/2, 0.: Geodesic deviation in TT gauge xi''_i = (1/2) h''_ij xi_j, with the course sign E_ij = R_i0j0 so xi'' = -E xi; integrate twice from rest. → Consistent with the course convention; unchanged claim.
- Dye analogy: fractional volume rate of a fluid blob is d_i v_i; incompressible stirring is trace-free; volume loss of a released ball is fourth order in proper time.: Continuity equation; Raychaudhuri with theta(0) = 0, sigma proportional to tau, theta' = -sigma^2 - R_uu, so theta ~ tau^3 and delta V ~ tau^4; matches 0.5 q^2 t^4. → Correct. B_ij, theta and the electric Weyl tensor are defined at the formal rung of this note, so the working-rung mapping leans upward; noted as a concern.
- Release law derivation: V' = surface integral of v, V''(0) = flux of g, Gauss gives -4 pi G M_enc, small-cloud limit -nabla^2 Phi.: Re-derived: Reynolds transport with particles at rest at t = 0, divergence theorem, Poisson equation with the course potential. → Correct.

**Counterexamples tried**

- Ball with mass inside (huge ball around Earth or Moon): breaks the old tagline 'changes a falling ball's shape long before it changes its volume'; tagline now says 'with nothing inside'.
- Crumbs inside a planet: 'Near a round planet' drift rule fails there, so the egg recap now says 'Outside a round planet' as the glossary does.
- Cosmological constant: an empty ball's volume does change at second order in time; the entry rung attributes the rule to Newton's law, and the working way gives the Lambda c^2 term, so the scope holds.
- Crumbs thrown outward instead of released at rest: every changed rule keeps 'let go at rest' or 'released at rest'.
- Boosted observer in vacuum: trace still zero (checked with the 0.6c numbers).
- Cabin walls and the centre crumb as mass inside or outside: the whole-Earth way answers both; the centre crumb's pull moves a neighbour by about 3e-15 m in 10 s for a milligram crumb.

**Fixes**

- Tagline scoped to a ball with nothing inside.
- Egg way: 'exactly the room' became 'the same room'; 'is also its length times its two widths' became 'is also set by'; recap 'Near a round planet' became 'Outside a round planet'.
- Wave way and mirror-arms check: 1 - h^2/4 is now the product of the two first-order length factors, and 2.5e-43 its leftover, not 'the exact area factor' or 'the second-order change'.
- One-minute example: 17.6 km became 17.7 km.

**Concerns**

- This note reached the post-review checker at revision 1, status draft, with no review block, although the before-physics snapshot was revision 2, novice-reviewed, with a full novice record. The physics stage evidently rewrote the file wholesale and dropped the metadata. The novice record was restored from the snapshot, the revision set to 4 (2 novice, 3 physics, 4 this check), the status restored to novice-reviewed, and this physics record written from the post-review check alone. An editor should decide whether the physics stage's own verdict can be signed; the prior run's 27-item physics record (snapshot prior-run, revision 3) covers older text and was not restored.
- The dye analogy at working rung maps onto B_ij, the expansion theta and the electric Weyl tensor, which this note defines only at the formal rung.
- Carried over: the conventions file has no symbols for an observer's tidal tensor or the electric and magnetic Weyl parts; registry prerequisites lack poisson-equation-for-gravity (validator note).

**Diff check** (2026-09-16, revision 4)

- All entry and working numbers changed by the physics review (drifts, box products, 435 m, 193 ppm, 73 m, 120 ppm, cube, one-minute example, GOCE, LIGO arms, boosted tidal tensor).: Recomputed with python3 as listed in the verification array. → All correct except 17.6 km (should be 17.7 km); fixed.
- Changed general sentences: tagline, egg-way rule sentences, release law, small-ball law with pressure and Lambda, wave area statement, dye analogy.: Conditions, frames and counterexamples checked as recorded; hand algebra for the Lambda term and the boost. → Tagline needed the 'nothing inside' scope; 'exactly' and 'exact area factor' overstated; 'Near a round planet' needed 'Outside'. Fixed; every other changed sentence is accurate within its scope.
- Novice rewrites made in this check.: Re-read each as the adversarial physicist. → None changes a claim; all remain true.
- Fix: Tagline scope; 'the same room'; 'set by its length times its two widths'; 'Outside a round planet'; 'product of the two first-order length factors'; 'the leftover h_+^2/4'; 17.7 km.
