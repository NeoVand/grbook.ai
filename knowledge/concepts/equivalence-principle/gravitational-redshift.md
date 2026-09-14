---
type: "concept"
schema_version: 2
id: "gravitational-redshift"
title: "Gravitational redshift"
tagline: "Why light sent up to a higher detector arrives with a lower frequency"
domain: "equivalence-principle"
tier: "foundation"
status: "physics-reviewed"
revision: 5
updated: "2026-09-13"
aliases: ["Einstein shift", "gravitational frequency shift"]
prerequisites: ["equivalence-of-gravity-and-acceleration", "relativistic-doppler-effect", "mass-energy-equivalence", "newtonian-gravitational-potential", "energy-measured-by-an-observer", "conserved-quantity-from-killing-vector", "rindler-coordinates"]
leads_to: ["gravitational-time-dilation", "schilds-redshift-argument", "pound-rebka-experiment", "surface-redshift"]
visuals: ["lamp-and-detector-in-a-rocket", "drop-a-lump-send-up-light", "two-clocks-trading-crests"]
---

# Gravitational redshift

*Why light sent up to a higher detector arrives with a lower frequency*

`gravitational-redshift` · equivalence-principle · foundation · physics-reviewed (revision 5)

**Needs:** [[equivalence-of-gravity-and-acceleration]] (entry) · [[relativistic-doppler-effect]] (entry) · [[mass-energy-equivalence]] (entry) · [[newtonian-gravitational-potential]] (working) · [[energy-measured-by-an-observer]] (formal) · [[conserved-quantity-from-killing-vector]] (formal) · [[rindler-coordinates]] (formal)  
**Opens:** [[gravitational-time-dilation]] · [[schilds-redshift-argument]] · [[pound-rebka-experiment]] · [[surface-redshift]]  
**Related:** [[local-position-invariance]] · [[cosmological-redshift]]  
**Visuals:** ★ [[lamp-and-detector-in-a-rocket]] · [[drop-a-lump-send-up-light]] · [[two-clocks-trading-crests]]

> Put a lamp low down and a detector higher up, both held still. The detector, counting on its own clock, gets fewer wave crests each second than a clock beside the lamp counts leaving it. So the light arrives with a lower frequency: this is gravitational redshift. Light sent down arrives with a higher frequency. Near the ground on Earth, the change is about one part in ten million billion for each metre of height.

## You will be able to

**Entry**
- Explain, with a rocket speeding up, why light sent up arrives with a lower frequency and light sent down with a higher one. `objectives/explain-with-a-rocket` ← `checks/light-sent-down`
- Explain why climbing light that kept its frequency would let a tower make energy from nothing. `objectives/explain-with-energy` ← `problems/a-heavier-lump-each-round`
- Distinguish what is the same at every height (a lamp counted beside its clock, the speed of light) from what changes when light is counted at another height. `objectives/separate-local-from-compared` ← `checks/lamps-and-light-at-the-ceiling`
- Estimate the frequency change over a height on Earth, and say why nobody notices it. `objectives/estimate-the-size-on-earth` ← `checks/crests-over-a-tower`

**Working**
- Derive the first-order shift from a Doppler argument or from energy conservation. `objectives/derive-first-order-shift` ← `checks/energy-route-downward`
- Compute the fractional frequency change between two places from their potentials, with its sign. `objectives/compute-shift-from-potentials` ← `problems/gps-signal-reaching-the-ground`
- Predict how a falling or moving receiver changes the measured shift. `objectives/predict-effect-of-receiver-motion` ← `checks/detector-let-go-at-the-top`
- Explain why a steady redshift means clocks at different heights disagree. `objectives/explain-where-crests-go` ← `checks/where-do-the-crests-go`

**Formal**
- Derive the exact frequency ratio for observers on a timelike Killing vector, without geodesics. `objectives/derive-lapse-ratio` ← `problems/crests-are-time-translates`
- Distinguish redshift between static observers from evidence of curvature. `objectives/separate-redshift-from-curvature` ← `checks/rocket-a-light-year-long`
- State which principle a redshift measurement tests, and why not the field equations. `objectives/state-what-redshift-tests` ← `checks/field-equations-claim`

## Ways in

### 1. Light climbing in a rocket · entry · picture

*Does a detector high in a room count as many light crests each second as a lamp on the floor sends?*

**Recap:** The Doppler effect: when a receiver and a source of waves move apart, the receiver meets wave crests less often. So it counts a lower frequency. Moving closer raises it. The equivalence of gravity and acceleration: in a small closed room, no experiment can tell a room resting on Earth from a rocket speeding up at the rate things fall.

Picture a room about 3 metres tall, with a lamp on the floor and a detector on the ceiling. Both are fixed in place. The lamp shines a steady beam of light up to the detector.

Light is a wave, and a steady beam is a long train of wave crests. Imagine a perfect counter beside the lamp that counts the crests leaving each second, by a clock beside the lamp. That number is called the frequency of the light. For blue-green light it is about 600 thousand billion.

The detector is a perfect counter too, with its own clock. Does it count the same number of crests arriving each second?

First imagine the room is the cabin of a rocket far out in empty space, with its nose beyond the ceiling. Its engine keeps it speeding up toward its nose, gaining about 10 metres per second of speed every second.

For each crest, measure speeds from a space station drifting beside the rocket. At the moment the crest leaves the lamp, the station moves along with the rocket, so the lamp is at rest compared with the station. The crest needs a tiny moment to reach the ceiling, and meanwhile the rocket speeds up a little. So the detector catches the crest while moving away from the station.

A receiver moving away from a source of waves meets the crests less often, and one moving toward it meets them more often. This is called the Doppler effect. The same happens for every crest, so the detector counts fewer crests each second than the lamp sends.

By the equivalence of gravity and acceleration, in a small closed room no experiment can tell this rocket cabin from a room resting on the ground on Earth. Counting crests is an experiment. So on Earth too, light sent from the floor to the ceiling arrives with fewer crests each second. This is called gravitational redshift.

Red is the lowest-frequency colour we see, so any shift to a lower frequency is called a redshift, even when the colour does not visibly change.

Put the lamp on the ceiling and the detector on the floor. While a crest travels down, the rocket speeds up, so the floor meets it moving toward the station. So light sent down arrives with a higher frequency. This is called a blueshift.

A detector at the lamp's height, even across the room, counts no shift. While a crest crosses the room, the detector speeds up across the crest's path, so it moves neither toward the crests nor away from them.

The change is tiny. Near the ground on Earth, each metre of height lowers the frequency by about one part in ten million billion. That is because light crosses one metre in a three-hundred-millionth of a second, so the ceiling gains only about a ten-million-billionth of light's speed.

**Try it:** Stand safely beside a road and listen to a car passing at a steady speed. As it comes toward you, its engine sounds higher-pitched. As it drives away, the sound is lower. That change is the Doppler effect the rocket uses.

**Takeaway:** Counted on each one's own clock, a detector fixed higher up gets fewer crests each second than a lamp below sends; light sent down arrives with more.

*What this leaves out:* Gravity on Earth weakens slowly with height, unlike the rocket's steady speeding up. So one part in ten million billion per metre holds only for heights much smaller than Earth's radius of 6,400 kilometres.

*Builds on:* [[relativistic-doppler-effect]], [[equivalence-of-gravity-and-acceleration]]<br>*Visuals:* [[lamp-and-detector-in-a-rocket]]

### 2. Where the missing crests go · entry · operational

*Where do the crests go that the ceiling detector does not count?*

**Recap:** The equivalence of gravity and acceleration: in a small closed room, no experiment can tell a room resting on Earth from a rocket speeding up at the rate things fall.

Counted on each one's own clock, the ceiling detector in "Light climbing in a rocket" gets fewer crests each second than the floor lamp sends.

A clock beside a lamp counts the same number of crests each second, on the floor or on the ceiling. By the equivalence of gravity and acceleration, a small room anywhere near the ground works like the same rocket cabin, so a lamp and clock side by side cannot tell their height.

The light does not slow down, either. Anyone who measures the speed of passing light, with a ruler and clock beside them, gets about 300,000 kilometres per second, at any height.

Do the missing crests pile up? No. Nothing in the room changes from moment to moment, so every crest makes the same trip. What differs is the clocks. While the same crests pass, the ceiling clock ticks off more seconds than the floor clock, so it counts fewer crests in each second. This is called gravitational time dilation.

**Takeaway:** No crests pile up; the clock higher up ticks off more seconds while the same crests pass.

*Continues:* `ways_in/light-climbing-in-a-rocket`<br>*Builds on:* [[equivalence-of-gravity-and-acceleration]]<br>*Visuals:* [[lamp-and-detector-in-a-rocket]]

### 3. A machine that cannot work · entry · contrast

*Why would light that kept its frequency while climbing let a tower make energy from nothing?*

**Recap:** Mass-energy equivalence: energy has mass, so giving something energy makes it slightly heavier, and in principle matter can be turned entirely into light and back. Frequency: the number of wave crests passing each second, counted on a clock at that place. A redshift is a shift to a lower frequency.

The rocket in "Light climbing in a rocket" showed that light sent up arrives with a lower frequency. Here is a second reason, which needs only energy.

Imagine a tall tower with a perfect machine at the bottom and another at the top. Each can turn matter into light, or light into matter, wasting nothing. At the top, you let go of a lump of matter. It reaches the bottom moving fast, so it carries extra energy gained from the fall.

The bottom machine turns the whole lump, extra energy included, into a flash of light aimed up the tower. At the top, the second machine turns the light back into matter. Energy has mass, so the new lump's mass is set by the energy the light brings.

Now suppose light kept its frequency while climbing. Light comes in tiny packets of energy, and each packet's energy is set by its frequency: double the frequency, double the energy. That is why ultraviolet light, with a higher frequency than violet, causes sunburn, while bright red light does not. Nothing on the way up adds or removes packets. So the flash would reach the top with all its energy.

Then the top machine would make a lump slightly heavier than the one you dropped. You could keep the extra as energy and drop a lump like the first. The tower would make energy from nothing, round after round.

Every careful measurement finds that energy is never created from nothing. If climbing light lost less energy than the lump gained by falling, the tower would make energy. If it lost more, the tower run backwards would make energy, because light sent down would gain more than lifting a lump cost. So climbing light loses exactly the energy the lump gained, and arrives with a lower frequency.

A lump falling one metre near the ground gains about one part in ten million billion of the energy locked in its mass. So light climbing one metre loses that fraction of its frequency, the same size the rocket gives.

**Try it:** Use a calculator. A one-kilogram bag of sugar dropped one metre gains about 10 joules, the unit of energy. The energy locked in its mass is about 90 million billion joules. Divide 10 by that: you get about one ten-million-billionth.

**Takeaway:** If climbing light kept its frequency, a tower could make energy from nothing, so light must lose exactly the energy a falling lump gains and arrive with a lower frequency.

*What this leaves out:* The machines are imaginary. Light gives a tiny push to whatever sends or catches it; the heavy ground takes these pushes but almost no energy.

*Continues:* `ways_in/light-climbing-in-a-rocket`<br>*Builds on:* [[mass-energy-equivalence]]<br>*Visuals:* [[drop-a-lump-send-up-light]]

### 4. Putting numbers on the rocket · working · calculation

*How large is the shift, and how does it depend on height and on the gravitational potential?*

In "Light climbing in a rocket", the ceiling detector is moving away from a drifting station that moved with the lamp as the crest left, so it counts a lower frequency. Put numbers on it. Write $f_e$ for the frequency counted by a clock beside the lamp and $f_r$ for the frequency counted on the detector's clock. Let the rocket's floor have acceleration $g$, measured by an accelerometer on the floor, and let the detector sit a height $H$ above the lamp. Work in that station's inertial frame, in which the rocket is momentarily at rest when a given crest leaves the lamp.

The crest reaches the ceiling after $\Delta t = H/c$, to leading order. By then the ceiling moves at $v = gH/c$ along the light's direction of travel. With $\beta = v/c = gH/c^2 \ll 1$, the Doppler formula for a receding receiver gives

$$\frac{f_r}{f_e} = \sqrt{\frac{1-\beta}{1+\beta}} = 1 - \frac{gH}{c^2} + O\!\left(\frac{g^2H^2}{c^4}\right).$$

Every crest meets the same situation, so this is the ratio of the frequency counted on the detector's clock to the frequency counted on the lamp's clock. The neglected corrections, from the ceiling's motion during the trip and from the slightly different accelerations of a rigid rocket's floor and ceiling, are of second order in $gH/c^2$. The equivalence of gravity and acceleration, taken from its own note, carries the result to a lab at rest in a uniform field with free-fall acceleration $g$.

Real fields vary with height. Stack thin slabs of thickness $dz$, each with its local $g(z)$, so each slab multiplies the frequency by $1 - g\,dz/c^2$. Because $g = d\Phi/dz$ for the Newtonian potential $\Phi$, which increases with height, the slabs combine, to first order, into

$$\frac{f_r - f_e}{f_e} \approx -\frac{\Phi_r - \Phi_e}{c^2}.$$

In a static field, climbing to a higher potential lowers the frequency, descending raises it, and a source and receiver at rest at equal potential agree, however far apart they are.

Near Earth's surface $g/c^2 = 1.09\times10^{-16}$ per metre, so a 22.5 m climb gives a fractional change of $-2.46\times10^{-15}$. From Earth's surface to very far away, $\Phi_r - \Phi_e = GM_\oplus/R_\oplus$ and the change is $-6.96\times10^{-10}$. From the Sun's surface to very far away it is $-2.12\times10^{-6}$.

**Takeaway:** To first order, a receiver a height H above the emitter counts a frequency lower by the fraction g H over c squared; in general, by the potential difference over c squared.

*What this leaves out:* Keeps only first order in the potential difference over the speed of light squared.

*Continues:* `ways_in/light-climbing-in-a-rocket`<br>*Builds on:* [[relativistic-doppler-effect]], [[equivalence-of-gravity-and-acceleration]], [[newtonian-gravitational-potential]]<br>*Visuals:* [[lamp-and-detector-in-a-rocket]]<br>*See:* `derivations/shift-from-doppler-in-a-rocket`, `worked_examples/light-from-the-sun`

### 5. Energy bookkeeping with symbols · working · calculation

*What exactly does energy conservation require of light climbing in a uniform field?*

The tower in "A machine that cannot work" becomes a calculation once each energy has a symbol, and the derivation "Energy bookkeeping for a climbing flash" lays out every step. A lump of rest mass $m$ falls a height $H$ and reaches the bottom with energy $mc^2 + mgH$, to first order in $gH/c^2$. It becomes $n$ photons, the packets of light, of frequency $f_b$, so $nhf_b = mc^2 + mgH$, with $h$ Planck's constant. The photon number does not change during the climb, and at the top the flash becomes a lump of mass $nhf_t/c^2$. Forbidding a gain on every round requires that mass to equal $m$, so

$$\frac{f_t}{f_b} = \frac{mc^2}{mc^2 + mgH} \approx 1 - \frac{gH}{c^2}.$$

This agrees with "Putting numbers on the rocket" without any accelerating frame. It needs only energy conservation in a field that does not change in time, together with $E = mc^2$ and $E = hf$. It also reads as a weight for light: a flash of energy $E$ climbing $H$ loses $(E/c^2)\,gH$, just what a mass $E/c^2$ would lose. The closed form $1/(1 + gH/c^2)$ carries no extra accuracy, because $mgH$ is itself only the Newtonian approximation to the energy gained in the fall.

**Takeaway:** Energy conservation with E equals m c squared and E equals h f forces the same first-order fraction, g H over c squared, as if light of energy E had weight.

*Continues:* `ways_in/a-machine-that-cannot-work`<br>*Builds on:* [[mass-energy-equivalence]]<br>*Visuals:* [[drop-a-lump-send-up-light]]<br>*See:* `derivations/shift-from-energy-conservation`

### 6. Measuring the shift: resonance and clocks · working · operational

*How do experiments measure a frequency shift of a few parts in a million billion, and who counts what?*

The shift in "Putting numbers on the rocket" is only $2.46\times10^{-15}$ for a 22.5 m climb, so measuring it means comparing frequencies with extreme precision. Every such measurement names two things: what emits, and a receiver at rest relative to the emitter that counts on its own clock.

*Resonance matching.* A nucleus absorbs a gamma ray strongly only when the ray's frequency, in the absorber's rest frame, matches its own transition. Through the Mössbauer effect, recoil-free emission and absorption by nuclei bound in a solid, iron-57 emits and absorbs 14.4 keV ($2.31\times10^{-15}$ J) gamma rays with a fractional line width of about $3\times10^{-13}$. With the source at the bottom of a tower and the absorber at the top, the arriving rays are shifted by $-gH/c^2$, about one per cent of that width. Moving the source upward at speed $v$ adds a Doppler blueshift of $v/c$, so absorption is centred when $v = gH/c$, about 0.74 micrometres per second for 22.5 m. Exchanging source and absorber reverses the gravitational shift, which cancels errors that do not depend on direction.

*Clock comparison.* Two identical atomic clocks at different heights each count their own oscillations. A light signal or an optical fibre carries one clock's oscillation to the other, where the two frequencies are compared by counting beats. The higher clock receives the lower clock's signal redshifted, relative to its own oscillation, by the fraction $(\Phi_r - \Phi_e)/c^2$. The lower clock receives the higher clock's signal blueshifted by the same fraction.

*Motion of the receiver.* A receiver moving relative to the emitter adds its own Doppler factor. So the gravitational redshift is defined for receivers at rest relative to the source, and the check "A detector let go at the top" works out what a freely falling receiver measures instead.

**Takeaway:** The shift is measured by matching a sharp nuclear resonance with a known Doppler speed, or by comparing identical clocks, with receivers at rest relative to the emitter.

*What this leaves out:* Ignores Earth's rotation, which changes the potential and the receivers' motion by small, calculable amounts.

*Continues:* `ways_in/putting-numbers-on-the-rocket`<br>*See:* `observations/pound-rebka-tower`, `observations/optical-clocks-33-centimetres`, `checks/detector-let-go-at-the-top`

### 7. Exact ratio from a time symmetry · formal · structure

*What is the exact redshift law, what does it assume, and what does it not show?*

The first-order law of "Putting numbers on the rocket" has an exact form wherever spacetime has a time symmetry. Set $G = c = 1$ in this way. Let $\xi$ be a Killing vector field that is timelike where emitter and receiver are, so the spacetime is stationary there. An observer moving along $\xi$ has four-velocity $u = \xi/N$ with lapse $N \equiv \sqrt{-\xi_\mu\xi^\mu}$. In coordinates with $\xi = \partial_t$, this observer sits at fixed spatial coordinates and $N = \sqrt{-g_{tt}}$. Here "lapse" means this Killing norm; it equals the lapse of the $t = \text{const}$ slicing only when the metric is static, $g_{ti} = 0$.

In geometric optics, light has a null wave vector $k^\mu$ tangent to an affinely parametrized geodesic, and an observer with four-velocity $u$ measures angular frequency $\omega = -k_\mu u^\mu$. The Killing energy $E_\xi = -\xi_\mu k^\mu$ is constant along the ray, because $k^\mu k^\nu \nabla_\mu\xi_\nu = 0$ by Killing's equation. Hence $\omega = E_\xi/N$ for every observer on $\xi$, and

$$\frac{\omega_r}{\omega_e} = \frac{N_e}{N_r}.$$

No field equation enters. The result needs a metric, a timelike Killing vector at both ends, and emitter and receiver moving along it; the problem "Crests are time translates" drops even geometric optics. In a weak static field $g_{tt} = -(1 + 2\Phi)$, so $N \approx 1 + \Phi$ and the first-order law returns. Outside a spherical mass, with the course Schwarzschild metric, $N = \sqrt{1 - 2M/r}$. For light leaving a neutron star with $2M/R = 0.345$ and received far away, the exact ratio is $0.809$, while the first-order law gives $0.828$.

Two limits matter. An observer not moving along $\xi$ measures an extra special-relativistic Doppler factor relative to the static observer at the same event. Where no timelike Killing vector exists, as in an expanding universe, $E_\xi$ is not defined and this construction does not apply.

The ratio is not a curvature diagnostic. In Minkowski spacetime, Rindler coordinates give $ds^2 = -(1 + ax)^2dt^2 + dx^2 + dy^2 + dz^2$, and $\partial_t$ is a Killing vector. Its orbits at fixed $x$ are the parts of a rigid, uniformly accelerating rocket, the one at $x$ having proper acceleration $a/(1 + ax)$. Here $N = 1 + ax$, so $\omega_r/\omega_e = (1 + ax_e)/(1 + ax_r)$ exactly, while the Riemann tensor vanishes. A redshift between static observers measures how their lapse varies; curvature shows up only in effects that no single accelerating frame reproduces, such as tides.

Experimentally the law tests local position invariance. A violation would appear as $\omega_r/\omega_e = 1 - (1 + \alpha)(\Phi_r - \Phi_e)$ with $\alpha \neq 0$, generally different for different kinds of clock; every metric theory obeying the Einstein equivalence principle has $\alpha = 0$.

**Takeaway:** For emitter and receiver moving along a timelike Killing vector, the frequency ratio is exactly the inverse ratio of their lapses, with no field equations and no curvature required.

*What this leaves out:* The Killing-energy route assumes geometric optics and ignores recoil.

*Continues:* `ways_in/putting-numbers-on-the-rocket`<br>*Builds on:* [[conserved-quantity-from-killing-vector]], [[energy-measured-by-an-observer]], [[rindler-coordinates]]<br>*Visuals:* [[two-clocks-trading-crests]]<br>*See:* `derivations/exact-ratio-from-killing-energy`, `problems/crests-are-time-translates`, `checks/rocket-a-light-year-long`

## Glossary

| Term | Say | In plain words | Concept |
| --- | --- | --- | --- |
| crest | — | A high point of a wave. A steady beam of light is a long train of crests. | — |
| frequency | — | The number of wave crests passing a place each second, counted on a clock at that place. | — |
| redshift | — | A shift of light to a lower frequency, as counted by whoever receives it. Red is the lowest-frequency colour we see. | — |
| blueshift | — | A shift of light to a higher frequency, as counted by whoever receives it. | — |
| gravitational redshift | — | The lower frequency a detector held higher up counts, on its own clock, for light from a lamp held lower down. | [[gravitational-redshift]] |
| Doppler effect | DOP-ler | The lower frequency a receiver counts when it and the source of waves move apart, or the higher one when they move closer. | [[relativistic-doppler-effect]] |
| equivalence of gravity and acceleration | — | The rule that in a small closed room, no experiment can tell a room resting on Earth from a rocket in empty space speeding up at the rate things fall. | [[equivalence-of-gravity-and-acceleration]] |
| mass-energy equivalence | — | Energy has mass: giving something energy makes it slightly heavier, and matter can be turned into light and back. | [[mass-energy-equivalence]] |
| packet of light | — | The smallest amount of light that can be sent or caught, with energy set by its frequency; a photon. | [[photon]] |
| gravitational time dilation | — | Clocks at different heights ticking at different rates, compared by light; the higher one ticks faster. | [[gravitational-time-dilation]] |

## Key equations

### Shift over a height in a uniform field · working

$$
\frac{f_r}{f_e} \approx 1 - \frac{gH}{c^2}
$$

A receiver a height $H$ above the emitter, both at rest, counts a lower frequency.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $f_e$ | frequency counted beside the emitter | f e |
| $f_r$ | frequency counted on the receiver's clock | f r |
| $g$ | free-fall acceleration | g |
| $H$ | height of the receiver above the emitter | H |

**Holds when:** Uniform field, or a rocket with acceleration $g$; first order in $gH/c^2$.  
**Say it:** “f r over f e is about one minus g H over c squared.”  
**Justified by:** `derivations/shift-from-doppler-in-a-rocket`

### First-order shift from a potential difference · working

$$
\frac{f_r - f_e}{f_e} \approx -\frac{\Phi_r - \Phi_e}{c^2}
$$

Light received at higher potential than it was emitted at is redshifted.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $\Phi_e,\ \Phi_r$ | Newtonian potential at emitter and receiver, $\Phi = -GM/r$ outside a spherical mass | phi e and phi r |

**Holds when:** Static weak field, $|\Phi|/c^2 \ll 1$; emitter and receiver at rest.  
**Say it:** “The fractional change is minus the potential difference, receiver minus emitter, over c squared.”  
**Justified by:** `derivations/shift-from-doppler-in-a-rocket`

### Exact redshift for stationary observers · formal

$$
\frac{\omega_r}{\omega_e} = \frac{N_e}{N_r},\qquad N = \sqrt{-\xi_\mu \xi^\mu}
$$

Observers moving along a timelike Killing vector measure frequencies in the inverse ratio of their lapses.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $\omega_e,\ \omega_r$ | angular frequencies measured by emitter and receiver | omega e and omega r |
| $\xi$ | Killing vector field, timelike at both ends | xi |
| $N$ | the lapse, here the Killing norm; $\sqrt{-g_{tt}}$ when $\xi = \partial_t$ | N, the lapse |

**Holds when:** $G = c = 1$; emitter and receiver move along $\xi$.  
**Say it:** “omega r over omega e equals N e over N r.”  
**Justified by:** `derivations/exact-ratio-from-killing-energy`

## Derivations

### The shift from a Doppler effect in an accelerating rocket · working

**Goal:** Show that $f_r/f_e \approx 1 - gH/c^2$ in a uniform field, and $-(\Phi_r - \Phi_e)/c^2$ in a static weak field.

1. By the equivalence of gravity and acceleration, use a rocket whose floor has acceleration $g$, with the receiver a height $H$ above the emitter.
2. In the inertial frame where the rocket is at rest as a crest leaves, the crest arrives at $t = H/c$ to leading order.
3. The receiver then recedes at $v = gH/c$.
4. With $\beta = v/c$, $f_r/f_e = \sqrt{(1-\beta)/(1+\beta)} = 1 - \beta + O(\beta^2) = 1 - gH/c^2$.
5. Every crest meets the same situation, so this is the ratio of counted frequencies.
6. For a varying field, a slab $dz$ multiplies the frequency by $1 - g(z)\,dz/c^2$, so $\ln(f_r/f_e) \approx -\int g\,dz/c^2$.
7. With $g = d\Phi/dz$ this gives $(f_r - f_e)/f_e \approx -(\Phi_r - \Phi_e)/c^2$.

**Result:** $f_r/f_e \approx 1 - gH/c^2$, and in general $(f_r - f_e)/f_e \approx -(\Phi_r - \Phi_e)/c^2$, to first order.

### Energy bookkeeping for a climbing flash · working

**Goal:** Show that energy conservation forces $f_t/f_b \approx 1 - gH/c^2$ for light climbing $H$.

1. A lump of rest mass $m$ falls $H$ and arrives with energy $mc^2 + mgH$, to first order.
2. It becomes $n$ photons climbing with $nhf_b = mc^2 + mgH$; the massive ground takes the momentum but negligible energy.
3. The photon number is unchanged, so the flash arrives with $nhf_t$ and becomes a lump of mass $m' = nhf_t/c^2$.
4. If $m' > m$ the cycle creates energy, and if $m' < m$ the reversed cycle does, so $nhf_t = mc^2$.
5. Dividing, $f_t/f_b = mc^2/(mc^2 + mgH) \approx 1 - gH/c^2$.

**Result:** $f_t/f_b \approx 1 - gH/c^2$.

### The lapse ratio from a conserved Killing energy · formal

**Goal:** With $G = c = 1$, show that observers on a timelike Killing vector $\xi$ measure $\omega_r/\omega_e = N_e/N_r$ for light in geometric optics.

1. Killing's equation is $\nabla_\mu\xi_\nu + \nabla_\nu\xi_\mu = 0$, and the null wave vector obeys $k^\nu\nabla_\nu k^\mu = 0$.
2. Along the ray, $k^\nu\nabla_\nu(\xi_\mu k^\mu) = k^\nu k^\mu\nabla_\nu\xi_\mu + \xi_\mu k^\nu\nabla_\nu k^\mu = 0$, by antisymmetry and by the geodesic equation.
3. So $E_\xi = -\xi_\mu k^\mu$ is the same at emission and reception.
4. An observer on $\xi$ has $u^\mu = \xi^\mu/N$, with $N = \sqrt{-\xi_\mu\xi^\mu}$ so that $u_\mu u^\mu = -1$, and measures $\omega = -k_\mu u^\mu = E_\xi/N$.
5. Hence $\omega_r/\omega_e = N_e/N_r$; with $g_{tt} = -(1 + 2\Phi)$, $N \approx 1 + \Phi$ gives the first-order law.

**Result:** $\omega_r/\omega_e = N_e/N_r$ exactly.

## Worked examples

### Sunlight received on Earth · working

**Problem:** Light leaves the Sun's surface ($R_\odot = 6.957\times10^{8}$ m, $GM_\odot = 1.327\times10^{20}\ \mathrm{m^3\,s^{-2}}$) and is received at rest on Earth, $d = 1.496\times10^{11}$ m away. Find the fractional frequency change and the equivalent Doppler speed.

1. At emission, $\Phi_e/c^2 = -GM_\odot/(R_\odot c^2) = -2.122\times10^{-6}$.
2. At reception, the Sun gives $-GM_\odot/(d\,c^2) = -9.87\times10^{-9}$ and Earth gives $-GM_\oplus/(R_\oplus c^2) = -6.96\times10^{-10}$.
3. So $(\Phi_r - \Phi_e)/c^2 = 2.112\times10^{-6}$, and $(f_r - f_e)/f_e \approx -2.112\times10^{-6}$.
4. A source receding at $v \ll c$ gives $-v/c$, so $v = 2.112\times10^{-6}\,c = 633$ m/s.

**Answer:** $(f_r - f_e)/f_e \approx -2.11\times10^{-6}$, like a source receding at 633 m/s.

**Takeaway:** The Sun's surface potential sets almost all of it; real spectra add Doppler shifts of similar or larger size from moving gas and rotation.

## Problems

### `a-heavier-lump-each-round` · entry · difficulty 1 · conceptual

In the tower machine, suppose light kept its frequency while climbing. Is the lump made at the top lighter, heavier, or the same as the lump you dropped? What happens if you keep repeating the round?

**Hints**

1. What does the lump gain as it falls?

**Answer:** Heavier, and repeating the round would make energy from nothing.

**Must contain:** The new lump would be heavier; Repeating would make energy from nothing

**Solution**

1. The lump gains extra energy as it falls.
2. Light that kept its frequency would carry all of that energy to the top.
3. Energy has mass, so the new lump would be heavier, and each round would add more. That never happens, so climbing light must lose energy.

### `gps-signal-reaching-the-ground` · working · difficulty 2 · calculation

A satellite clock broadcasts at 10.23 MHz, counted on the clock itself, from a circular orbit of radius 26,560 km. Earth has radius 6371 km and surface gravity 9.81 m/s². Counting only the gravitational shift, what fractional change and what frequency difference does a receiver at rest on the ground measure?

**Hints**

1. The signal descends. Which sign do you expect?
2. Earth's $GM$ equals its surface gravity times its radius squared.

**Answer:** A blueshift of $+5.29\times10^{-10}$, about $+5.4$ mHz. Orbital speed adds a separate, opposite shift not counted here.

**Must contain:** The descending signal is blueshifted; About plus 5.3 parts in ten billion, or 5.4 millihertz

**Numeric:** fractional change = 5.29e-10 1 (signed, ±2%); frequency difference = 0.00541 Hz (signed, ±3%)

**Solution**

1. $GM_\oplus = gR_\oplus^2 = 9.81 \times (6.371\times10^{6})^2 = 3.982\times10^{14}\ \mathrm{m^3\,s^{-2}}$, so $GM_\oplus/c^2 = 4.43\times10^{-3}$ m.
2. With $\Phi = -GM/r$, $(\Phi_r - \Phi_e)/c^2 = -(GM_\oplus/c^2)(1/R_\oplus - 1/r) = -4.43\times10^{-3} \times 1.193\times10^{-7} = -5.29\times10^{-10}$.
3. So $(f_r - f_e)/f_e = +5.29\times10^{-10}$, and $f_r - f_e = 5.29\times10^{-10} \times 1.023\times10^{7}$ Hz $= 5.4\times10^{-3}$ Hz.

### `crests-are-time-translates` · formal · difficulty 2 · proof

In coordinates where a stationary metric does not depend on $t$, an emitter and a receiver stay at fixed spatial coordinates, and a signal travels between them along any path through a medium at rest, such as an optical fibre. Without geodesics, show that $\omega_r/\omega_e = \sqrt{g_{tt}(x_e)/g_{tt}(x_r)}$.

**Hints**

1. A crest leaving at $t_1$ arrives at $t_1 + T$. When does one leaving at $t_1 + \Delta t$ arrive?

**Answer:** Every crest takes the same coordinate time, so crests leaving $\Delta t$ apart arrive $\Delta t$ apart; each clock records $\sqrt{-g_{tt}}\,\Delta t$ at its own position.

**Must contain:** The setup is invariant under a shift of t; Crests leave and arrive equal coordinate intervals apart; Proper time at fixed position is the square root of minus g t t times dt

**Solution**

1. The metric, medium and positions are unchanged by $t \to t + \text{const}$, so a crest leaving at $t_1 + \Delta t$ arrives at $t_1 + \Delta t + T$.
2. A clock at fixed $x^i$ records $d\tau = \sqrt{-g_{tt}}\,dt$, even if $g_{ti} \neq 0$, because $dx^i = 0$.
3. The periods are $\sqrt{-g_{tt}(x_e)}\,\Delta t$ and $\sqrt{-g_{tt}(x_r)}\,\Delta t$, so $\omega_r/\omega_e = \sqrt{g_{tt}(x_e)/g_{tt}(x_r)} = N_e/N_r$, with no geodesic or field equation used.

## Observations

- **Gamma rays sent up and down a 22.5 m tower at Harvard, 1960** (measured, working). Iron-57 gamma rays were detected by resonant absorption, with a moving source supplying a compensating Doppler shift and the two directions compared. *Numbers:* Predicted $2.46\times10^{-15}$ each way; measured over predicted $1.05 \pm 0.10$, improved to about 1 per cent by 1965. *Reference:* R. V. Pound, G. A. Rebka Jr. (1960), *Apparent Weight of Photons*, Physical Review Letters 4, 337–341, doi:10.1103/PhysRevLett.4.337
- **A hydrogen maser clock flown on a rocket to about 10,000 km, 1976** (measured, working). Compared by microwave link with a ground maser, with the Doppler shift of the rocket's motion removed, its frequency followed the prediction through the flight. *Numbers:* Gravitational part near 10,000 km about $4.3\times10^{-10}$; agreement within about $7\times10^{-5}$ of the prediction. *Reference:* R. F. C. Vessot, M. W. Levine, E. M. Mattison and others (1980), *Test of Relativistic Gravitation with a Space-Borne Hydrogen Maser*, Physical Review Letters 45, 2081–2084, doi:10.1103/PhysRevLett.45.2081
- **Two aluminium-ion optical clocks compared, one raised by 33 cm, 2010** (measured, working). The clock-comparison method at tabletop height: the raised clock ran faster by the potential difference over $c^2$. *Numbers:* Predicted $3.6\times10^{-17}$; measured $(4.1 \pm 1.6)\times10^{-17}$. *Reference:* C. W. Chou, D. B. Hume, T. Rosenband, D. J. Wineland (2010), *Optical Clocks and Relativity*, Science 329, 1630–1633, doi:10.1126/science.1192720
- **GPS satellite clocks are tuned low before launch** (measured, working). Compared by signals with ground clocks, an orbiting clock gains from its higher potential and loses from its speed; the net is removed on the ground. *Numbers:* Gravitational part $+5.3\times10^{-10}$, speed part $-0.8\times10^{-10}$; factory offset $-4.465\times10^{-10}$. *Reference:* Neil Ashby (2003), *Relativity in the Global Positioning System*, Living Reviews in Relativity 6, 1, doi:10.12942/lrr-2003-1

## Teaching arc

1. **Ask for a prediction** (entry). Pose the lamp-and-detector question before any argument. *Why:* A committed guess makes the argument an answer. *Predict:* Will the ceiling detector count more crests each second than the lamp sends, fewer, or the same? *Uses:* `ways_in/light-climbing-in-a-rocket`
2. **Run the rocket, then turn the room around** (entry). Walk a crest through the rocket, carry it to Earth, then send light down. *Why:* The downward case exposes 'gravity always reddens'. *Visual:* [[lamp-and-detector-in-a-rocket]] *Uses:* `ways_in/light-climbing-in-a-rocket`, `checks/light-sent-down`
3. **Ask where the missing crests go** (entry). Ask whether the missing crests pile up, then compare the floor and ceiling clocks. *Why:* It traces the lower count to the floor and ceiling clocks, not to lost crests. *Predict:* Do the missing crests, the ones the ceiling detector does not count, pile up somewhere in the room? *Visual:* [[lamp-and-detector-in-a-rocket]] *Uses:* `ways_in/where-the-missing-crests-go`, `checks/lamps-and-light-at-the-ceiling`
4. **Show that energy forces it** (entry). Build the tower machine and let the learner find the free energy. *Why:* A second, independent reason. *Visual:* [[drop-a-lump-send-up-light]] *Uses:* `ways_in/a-machine-that-cannot-work`, `problems/a-heavier-lump-each-round`
5. **Put numbers on it and ask who counts** (working). Derive the first-order law, measure it, then drop the detector. *Why:* Ties one formula to experiments and receivers. *Uses:* `ways_in/putting-numbers-on-the-rocket`, `ways_in/measuring-the-shift`, `checks/detector-let-go-at-the-top`
6. **State the exact law and its limits** (formal). Derive the lapse ratio and apply it to a flat accelerating rocket. *Why:* Redshift needs a time symmetry, not curvature. *Visual:* [[two-clocks-trading-crests]] *Uses:* `ways_in/exact-ratio-from-a-time-symmetry`, `checks/rocket-a-light-year-long`

## Misconceptions

### “Gravity makes light redder whichever way the light goes.” · entry · `redshift-whichever-way`

- **Why it is tempting:** The effect is called a redshift.
- **What is true:** Light sent down arrives with a higher frequency. Only light climbing to a higher detector is redshifted.
- **Exposed by:** `checks/light-sent-down`

### “A lamp low down really gives off lower-frequency light.” · entry · `lamp-at-the-bottom-is-different`

- **Why it is tempting:** The detector at the top really does count fewer crests.
- **What is true:** A clock beside the lamp counts the same frequency at any height. The shift appears only when light made at one height is counted at another.
- **Exposed by:** `checks/lamps-and-light-at-the-ceiling`

### “Light slows down as it climbs, like a thrown ball.” · entry · `light-slows-while-climbing`

- **Why it is tempting:** A ball loses speed as it rises.
- **What is true:** Anyone who measures the speed of passing light with a ruler and clock beside them gets the same speed, at any height. Only the number of crests counted each second changes.
- **Exposed by:** `checks/lamps-and-light-at-the-ceiling`

### “If fewer crests arrive each second than leave, crests must pile up in the tower.” · working · `missing-crests-pile-up`

- **Why it is tempting:** Fewer arrivals than departures usually means a build-up.
- **What is true:** Every crest makes the same trip. The clocks at the two heights count different seconds for the same crests.
- **Exposed by:** `checks/where-do-the-crests-go`

### “Any detector at the top measures the redshift, whatever it is doing.” · working · `every-detector-sees-the-shift`

- **Why it is tempting:** The redshift sounds like something done to the light.
- **What is true:** The measured frequency depends on the receiver's motion. A receiver let go from rest as the light leaves measures no shift, to first order.
- **Exposed by:** `checks/detector-let-go-at-the-top`

### “Redshift between clocks at rest relative to each other shows that spacetime is curved.” · formal · `redshift-shows-curvature`

- **Why it is tempting:** Gravity is taught as curvature.
- **What is true:** Accelerating clocks in flat spacetime show the same shift. Curvature shows in effects no accelerating frame reproduces, such as tides.
- **Exposed by:** `checks/rocket-a-light-year-long`

### “Gravitational redshift measurements test Einstein's field equations.” · formal · `redshift-tests-field-equations`

- **Why it is tempting:** It is a classical test of general relativity.
- **What is true:** The shift needs only a metric with a time symmetry. It tests local position invariance.
- **Exposed by:** `checks/field-equations-claim`

## Checks

1. **Entry · predict** `checks/light-sent-down`. In a room resting on Earth, a lamp on the ceiling sends light down to a detector on the floor. Both are fixed. Counted on its own clock, does the detector get more crests each second than a clock beside the lamp counts leaving it, fewer, or the same?
   - **Hints:** While a crest travels down, does the floor move toward the station or away?
   - **Answer:** More. Picture the room as a rocket cabin speeding up toward the ceiling. Measure speeds from a drifting station moving with the lamp as a crest leaves. While the crest travels down, the rocket speeds up, so the floor meets it moving toward the station. A detector moving toward a source meets crests more often. By the equivalence of gravity and acceleration, a detector on Earth also counts more.
   - **Must contain:** More crests each second; The floor meets each crest moving toward the station
   - **Targets:** `redshift-whichever-way`
   - **Visual:** [[lamp-and-detector-in-a-rocket]]
2. **Entry · predict** `checks/lamps-and-light-at-the-ceiling`. In a room on Earth, Ana sits on the floor and Bea stands on a ladder at the ceiling. Each counts crests each second from her own identical lamp, on an identical clock beside it. Bea also counts crests from Ana's lamp and measures that light's speed. Which counts are equal, which is lower, and what speed does Bea find?
   - **Hints:** Does a lamp beside its clock behave differently on the floor?
   - **Answer:** Ana's and Bea's counts of their own lamps are equal. A lamp and clock side by side cannot tell their height. Bea's count of Ana's light is lower, because that light climbed. Its speed is still about 300,000 kilometres per second. Anyone measuring passing light with a ruler and clock beside them gets that speed.
   - **Must contain:** The two lamps counted beside their clocks agree; Ana's light counted by Bea is lower; The speed is still 300,000 kilometres per second
   - **Numeric:** speed of the arriving light = 299792 km/s (magnitude, ±1%)
   - **Targets:** `lamp-at-the-bottom-is-different`, `light-slows-while-climbing`
3. **Entry · numeric** `checks/crests-over-a-tower`. A lamp at the bottom of a 30 metre tower on Earth sends blue-green light, about 600 thousand billion crests each second by a clock beside it. About how many fewer crests each second does a detector at the top count on its own clock?
   - **Hints:** Six hundred thousand billion is six tenths of a million billion.
   - **Answer:** About 2 fewer. Each metre gives one part in ten million billion, so 30 metres gives 30 parts in ten million billion. That is 3 parts in a million billion. The lamp sends six tenths of a million billion crests each second. Three parts in a million billion of that is 3 times 0.6, about 2.
   - **Must contain:** 3 parts in a million billion; About 2 fewer each second
   - **Numeric:** fewer crests each second = 2 Hz (magnitude, ±25%)
4. **Working · evaluate-claim** `checks/where-do-the-crests-go`. A lamp at the bottom of a tower on Earth sends crests steadily by its clock; a detector at the top counts fewer each second by its own clock. A student concludes that crests pile up in the tower. Evaluate this, and say what it implies about the two clocks.
   - **Hints:** If each crest takes the same time to climb, how far apart do they arrive?
   - **Answer:** No crests pile up. Nothing in the setup changes in time, so every crest takes the same time to climb, and crests arrive as far apart in that static time as they left. The same crests then span more seconds on the top clock, $f_e/f_r \approx 1 + gH/c^2$ for height $H$. Compared by light, the higher clock ticks faster by that fraction: gravitational time dilation.
   - **Must contain:** Every crest makes the same trip, so none pile up; The higher clock counts more seconds for the same crests
   - **Targets:** `missing-crests-pile-up`
5. **Working · numeric** `checks/detector-let-go-at-the-top`. At the top of a 22.5 m tower on Earth, a detector is released from rest at the instant a gamma ray leaves a source fixed at the bottom. To first order, what fractional frequency change does the falling detector measure?
   - **Hints:** How fast is the detector moving when the ray arrives?
   - **Answer:** Zero. The ray climbs for $H/c = 7.5\times10^{-8}$ s, so the detector reaches $v = gH/c = 7.4\times10^{-7}$ m/s toward the ray. Relative to a detector at rest there, that adds a Doppler blueshift $+gH/c^2 = +2.46\times10^{-15}$, cancelling the gravitational $-2.46\times10^{-15}$. A freely falling detector is locally inertial.
   - **Must contain:** The detector moves toward the ray at g H over c; Its Doppler blueshift cancels the redshift to first order
   - **Numeric:** fractional frequency change = 0 1 (signed, ±2e-16)
   - **Targets:** `every-detector-sees-the-shift`
   - **Visual:** [[lamp-and-detector-in-a-rocket]]
6. **Working · derive** `checks/energy-route-downward`. Run the tower machine backwards: lift a lump to the top, turn it into light, send it down, and turn it back into a lump. Use energy conservation to find the first-order ratio of the frequency arriving at the bottom to that sent from the top.
   - **Answer:** Lifting a lump of mass $m$ a height $H$ costs $mgH$. At the top it becomes a flash with $nhf_t = mc^2$. No net gain or loss over the cycle requires the flash to bring that energy back, $nhf_b = mc^2 + mgH$; more would create energy, and less would let the forward cycle create it. So $f_b/f_t \approx 1 + gH/c^2$, a blueshift.
   - **Must contain:** The descending light must return the lifting energy; Blueshift by g H over c squared
   - **Visual:** [[drop-a-lump-send-up-light]]
7. **Formal · numeric** `checks/rocket-a-light-year-long`. In flat spacetime, a rigid rocket accelerates so that its rear keeps a constant proper acceleration of 9.81 m/s², and every part keeps a fixed distance from the rear in the rocket's momentary rest frame. A lamp at the rear sends light to a receiver one light-year ahead. Find the ratio of received to emitted frequency, and say what it shows about curvature.
   - **Answer:** In Rindler coordinates, $ds^2 = -(1 + ax/c^2)^2c^2dt^2 + dx^2 + dy^2 + dz^2$, the parts sit at fixed $x$ along the Killing vector $\partial_t$, with lapse $N = 1 + ax/c^2$. With $aL/c^2 = 1.0326$, $\omega_r/\omega_e = 1/(1 + aL/c^2) = 0.492$, where the first-order law fails. The Riemann tensor vanishes, so redshift between mutually static observers does not by itself show curvature.
   - **Must contain:** The lapse is one plus a x over c squared; The ratio is about 0.492; No curvature is implied
   - **Numeric:** frequency ratio = 0.492 1 (magnitude, ±1%)
   - **Targets:** `redshift-shows-curvature`
   - **Visual:** [[two-clocks-trading-crests]]
8. **Formal · evaluate-claim** `checks/field-equations-claim`. Evaluate the claim: "Measuring the redshift of a rocket-borne clock to one part in ten thousand tests Einstein's field equations."
   - **Answer:** Mistaken. The lapse ratio $\omega_r/\omega_e = N_e/N_r$ needs only a metric with a timelike Killing vector and local special relativity; no field equation enters. In a weak field every metric theory has $N \approx 1 + \Phi/c^2$ with $\Phi$ fixed by observed orbits, so all agree at first order. The measurement tests local position invariance, bounding a clock-dependent $\alpha$ in $1 - (1 + \alpha)(\Phi_r - \Phi_e)/c^2$.
   - **Must contain:** The lapse ratio uses no field equation; It tests local position invariance
   - **Targets:** `redshift-tests-field-equations`

## Notation traps

| Issue | Course choice | Variants you will meet |
| --- | --- | --- |
| Sign inside the square root of the clock-rate factor | With signature $(-,+,+,+)$, $N = \sqrt{-g_{tt}}$, and $g_{tt} = -(1 - 2GM/rc^2)$ outside a spherical mass. | With signature $(+,-,-,-)$ the factor is written $\sqrt{g_{00}}$, with $g_{00} \approx 1 + 2\Phi/c^2$. |
| Sign of the potential in the shift | $\Phi = -GM/r$, so $g_{tt} \approx -(1 + 2\Phi/c^2)$ and climbing gives $(f_r - f_e)/f_e < 0$. | Some texts take the potential as $+GM/r$ and flip the sign of the shift. |

## Visuals

- ★ [[lamp-and-detector-in-a-rocket]] (flagship): The rocket argument, carried to Earth. *Sketch:* A rocket cabin beside a room on Earth, each with lamp and detector. Speeds are measured from a station drifting with the lamp at each emission. Change acceleration, height or beam direction, or drop the detector; crest strips and shift readouts match in both rooms. Timed from its own drifting station, each crest makes the same trip, so none pile up, while the ceiling clock ticks off more seconds for the same crests.
- [[drop-a-lump-send-up-light]] (core): The energy argument as a machine. *Sketch:* A lump falls, becomes climbing light, and becomes a lump again, with an energy bar. A switch that keeps the light's frequency makes an energy counter grow every round.
- [[two-clocks-trading-crests]] (supporting): The exact lapse ratio on a spacetime diagram. *Sketch:* Two static world lines, crest world lines drawn as time translates, ticks spaced by proper time. Toggle a flat rocket or a star; the ratio matches the lapses, and the rocket's curvature stays zero.

## Tutor moves

**Open with**

- A lamp on the floor of a room on Earth shines up to a detector on the ceiling, both held still. Will the detector count more crests each second than the lamp sends, fewer, or the same? *(prediction)*
- If light climbing a tower kept all its energy, could a machine on the tower make energy from nothing? *(reflection)*

**If the learner is stuck**

- *The learner cannot tell whether the ceiling moves toward or away from the light.* → Freeze the rocket as a crest leaves, and ask how the ceiling moves, compared with the drifting station, during the trip. *Uses:* `ways_in/light-climbing-in-a-rocket`
- *The learner gets the sign of the potential difference wrong.* → Anchor with $\Phi = -GM/r$, which rises toward zero with height. *Uses:* `worked_examples/light-from-the-sun`

**Common questions**

- *Does the light lose energy on the way up, like a ball thrown up?* (entry) Counted by detectors held still at each height, yes: each packet of light arrives with slightly less energy, by the fraction a lump gains by falling that far. Unlike a ball, light does not slow down. *Uses:* `ways_in/a-machine-that-cannot-work`, `checks/lamps-and-light-at-the-ceiling`
- *Does a clock at my head disagree with a clock at my feet?* (entry) Yes, when the two are compared by sending light between them. The clock at head height ticks faster, by about two parts in ten million billion. Over eighty years that adds up to about half a millionth of a second. *Uses:* `ways_in/where-the-missing-crests-go`, `checks/where-do-the-crests-go`
- *Is gravitational redshift just a Doppler shift?* (working) In the rocket, an inertial observer calls it a Doppler shift. In a lab at rest on Earth, the same counts appear as clocks at different potentials. The lapse ratio states the result in either description. *Uses:* `ways_in/putting-numbers-on-the-rocket`, `ways_in/where-the-missing-crests-go`, `ways_in/exact-ratio-from-a-time-symmetry`

**Switching levels**

- To working when: asks how big the shift is. Go to the first-order law and the Sun example. *Uses:* `ways_in/putting-numbers-on-the-rocket`, `worked_examples/light-from-the-sun`
- To formal when: asks whether the formula is exact; asks about curvature. Derive the lapse ratio and test it on the flat rocket. *Uses:* `ways_in/exact-ratio-from-a-time-symmetry`, `checks/rocket-a-light-year-long`

**Pronunciations:** Mössbauer → MERSS-bow-er; Pound–Rebka → POUND REB-kuh; Rindler → RIND-ler

**Voice notes:** Say "parts in ten million billion" and name whose clock counts.

## History

- **Albert Einstein (1907).** Used the equivalence of gravity and acceleration to predict that clock rates differ by the potential difference over $c^2$, shifting sunlight. Albert Einstein (1907), *Über das Relativitätsprinzip und die aus demselben gezogenen Folgerungen*, Jahrbuch der Radioaktivität und Elektronik 4, 411–462
- **Albert Einstein (1911).** Re-derived the shift from an accelerating frame and from energy, estimating two parts in a million for sunlight. Albert Einstein (1911), *Über den Einfluß der Schwerkraft auf die Ausbreitung des Lichtes*, Annalen der Physik 35, 898–908, doi:10.1002/andp.19113401005

## Review: novice

**Verdict:** fixed (2026-09-13, revision 5)

**Retell attempt:** If a lamp on the floor shines up to a detector on the ceiling, the detector counts fewer wave crests each second, so the light gets 'redshifted'. You see it by pretending the room is a rocket speeding up: by the time a crest reaches the ceiling, the ceiling is going faster, so it is like the detector running away from the light, the way a siren drops after the ambulance passes. Gravity and acceleration can't be told apart, so it happens on Earth too, and light going down gets bluer. The tower machine says the same thing: if light kept its energy going up, you could make energy for free, so it must lose what a falling lump gains. It is one part in ten million billion per metre, so nobody notices. I'm not sure which way the rocket is going, what the ceiling is 'moving away from', why the room is 'tall' but also 'small', why a lamp next to a clock counts normally, where the missing two crests a second go, or why light comes in packets and where the per-metre number comes from.

**Stumbles (24)**

- “Counted on the detector's own clock, fewer wave crests arrive each second than the lamp sends by a clock beside it, so the light arrives with a lower frequency.”: Summary sentence had to be reread: two clocks and two counts packed into one clause order.
- “The Doppler effect: when a receiver and a source of waves move apart, the receiver meets crests less often and measures a lower frequency.”: The recap uses 'crests' before anything says what a crest is, and 'measures' where the rest of the note says 'counts'.
- “Picture a tall room ... In a small closed room, no experiment can tell this rocket cabin from a room resting on the ground”: The room is 'tall' and then must be 'small' for the equivalence rule; the reader wonders whether the rule still applies.
- “Count the crests leaving the lamp each second on a clock beside the lamp.”: A rule nobody could physically follow: no one can count 600 thousand billion crests a second.
- “The engine is on, so the rocket keeps speeding up”: No direction is given, and the whole argument depends on the ceiling being the front of the rocket.
- “So the ceiling moves faster when the crest arrives than the lamp moved when the crest left. Both speeds are compared with a space station floating nearby, with no engine.”: The measurer arrives one sentence after the comparison, so the sentence had to be reread.
- “So the detector is always moving away from the place where each crest set off.”: A step left implicit: 'faster than the lamp was' does not obviously mean 'moving away from a place', and a place in space has no speed of its own.
- “Turn the room around.”: Ambiguous: turn the rocket around, turn the room upside down, or swap lamp and detector? Turning the rocket would change which way it speeds up.
- “A detector at the same height as the lamp measures no shift at all.”: A surprising claim with no reason, and 'measures' for 'counts'.
- “A clock right beside a lamp counts its usual number of crests ... a lamp and a clock side by side behave normally.”: 'Usual' and 'normally' have no named reference: usual compared with what?
- “Across a 3 metre room, that is about 3 parts in ten million billion.”: The first what-if a teenager tries, with the numbers in the crests check: if 2 fewer crests arrive every second, where do the missing ones go? The entry text never answers, so the reader suspects crests pile up.
- “Near the ground on Earth, each metre of height lowers the frequency by about one part in ten million billion.”: A surprising number with no reason or count the reader can check in the rocket way.
- “In empty space, everyone who measures the speed of light passing them gets about 300,000 kilometres per second. By the equivalence of gravity and acceleration, so does a detector on Earth.”: No measurer's tools or place, and a detector counts crests; it does not measure speed.
- “Imagine a tall tower with a perfect machine at the bottom and another at the top.”: 'Perfect machine' is used before the reader knows what the machine does.
- “Light comes in tiny packets of energy, and each packet's energy is set by its frequency”: A surprising claim with no reason or everyday sign, and 'packet' is not in the glossary.
- “Drop that lump, and the next round makes a heavier one still. Each round you could take out the extra energy and use it.”: The two sentences contradict each other: if you take the extra out, the next lump is not heavier.
- “On its way up, the light must lose exactly the energy the lump gained by falling.”: 'Exactly' is unexplained: the argument only shows the light must lose at least that much.
- “A lump falling one metre near the ground gains about one part in ten million billion of the energy locked in its mass.”: A surprising number with nothing the reader can check.
- “the ground takes up the push of the light flash while taking almost no energy”: The push of light was never mentioned, so the simplification is a puzzle rather than a caveat.
- “Which counts agree, which is lower, and what speed does she find?”: Check with an ambiguous state: 'one scientist ... one at the ceiling ... she', so it is unclear whose counts are compared, and 'sits at the ceiling' cannot be pictured.
- “so 30 metres gives 3 parts in a million billion”: A missing step: turning 30 parts in ten million billion into 3 parts in a million billion is not shown.
- “Distinguish what stays normal, a lamp beside its clock and the speed of light, from what changes between heights.”: The commas make the list read as appositions; the objective had to be reread.
- “The clock at head height counts about two parts in ten million billion more seconds.”: 'More seconds' than what, over what stretch? The comparison has no reference.
- “The lower frequency counted by a detector held higher up, for light from a lamp held lower down.”: Glossary definition: 'lower' than what, by whose clock?

**Fixes**

- Rocket way: gave the room a height (3 metres), the rocket a direction (nose beyond the ceiling), the counting a doable device (a perfect counter), and speeds a measurer (a drifting station at rest relative to the lamp as each crest leaves), so the Doppler step is a plain receiver-moving-away case.
- Rocket way: 'turn the room around' became an explicit swap; the same-height claim now carries a reason; 'usual' and 'normally' replaced by a comparison between floor and ceiling.
- Rocket way: added the missing-crests paragraph, which names gravitational time dilation (glossary entry added, concept gravitational-time-dilation), and a checkable reason for one part in ten million billion per metre (python: 10 m/s² × (1 m / c) / c = 1.11e-16).
- Rocket way: the speed-of-light sentence now names the measurer's ruler and clock; the speed fact moved out of the recap to save extras words.
- Tower way: the machines are described before use; packets of light get an everyday sign (sunburn) and a glossary entry; the heavier-lump contradiction is gone; 'exactly' is backed by running the machine both ways; a calculator try_it checks the size (python: 10 J / 9e16 J = 1.1e-16).
- Checks: 'lamps-and-light-at-the-ceiling' names Ana and Bea and makes the three counts unambiguous; 'crests-over-a-tower' shows the unit conversion (python: 6e14 × 30 × 1.09e-16 = 1.96); 'light-sent-down' uses the drifting station.
- Entry common question 'head-older-than-feet' gives a reference for the faster clock (python: 1.7 m gives 1.86e-16; 80 years gives 4.7e-7 s).
- Ladder: 'Putting numbers on the rocket' now defines $f_e$ and $f_r$ and names the station's frame as its inertial frame; 'Energy bookkeeping with symbols' ties photons to the packets of light; 'Measuring the shift' gives the SI value of 14.4 keV (2.31e-15 J) and says what the Mössbauer effect is.
- Budgets: trimmed teaching-arc reasons, several why_tempting lines, objectives, voice notes and a working check question to keep entry explanations at 996, extras 607 and tutoring under 2,200 words.
- Bumped the revision to 2.

**Concerns**

- The entry claim that a detector at the lamp's height counts no shift is backed by 'the rocket's speeding up carries both along in step'. That is a heuristic; the exact reason is equal lapse at equal height. The physics reviewer should confirm it is acceptable at entry.
- The drifting-station framing counts with the station's time, not the detector's own clock; the difference is second order in gH/c². The physics reviewer should confirm that the entry wording stays true. The proposed visual lamp-and-detector-in-a-rocket should use the same station framing.
- New entry claims for the physics reviewer: ultraviolet causes sunburn because each packet carries more energy, while bright red light does not; the sugar-bag numbers; 'light crosses one metre in a three-hundred-millionth of a second, so the ceiling gains about a ten-million-billionth of light's speed'.
- Budgets are at their caps: entry explanations 996 of 1,000, tutoring just under 2,200. Any further entry addition needs a matching cut.
- The writer's conventions gaps still stand: no fixed frequency symbol or redshift z, no weak-field g_tt row, and no 'lapse' term in the conventions file.
- None of the entry prerequisites (relativistic-doppler-effect, equivalence-of-gravity-and-acceleration, mass-energy-equivalence) has a v2 note, so recaps and glossary could not be aligned with their entry ways. The new glossary concept link 'photon' should be checked against the registry id when that note is written.
- The two ways in are genuinely different routes (a Doppler picture and an energy contradiction), and the working, operational and formal ways each open by naming the way they continue. No index notation appears below the formal rung.

**Re-read** (2026-09-13, revision 3): 7 stumbles in 16 changed passages

- “Measure speeds from a space station drifting beside the rocket. At the moment a crest leaves the lamp, the station moves along with the rocket, so the lamp is at rest compared with the station.”: The rocket keeps speeding up, so one drifting station moves along with it at only one moment. When the way then says 'The same happens for every crest', the reader cannot picture which station later crests are measured from.
- “While a crest travels down, the rocket speeds up, so the floor meets it moving toward the station. So light sent down arrives with a higher frequency.”: A step taken on trust. The explanation only says that a receiver moving away meets crests less often; 'moving closer raises it' appears only in the recap, which the book hides from a reader arriving in sequence.
- “While a crest crosses the room, the detector speeds up across the crest's path, not along it.”: Physics-review sentence. The reader is not told why speeding up across the path means no shift; the link to the Doppler rule (toward or away) is missing.
- “Do the missing crests pile up? No. ... This is called gravitational time dilation. / The light does not slow down, either. / A clock beside a lamp counts the same number of crests each second, on the floor or on the ceiling.”: Rule 17: after the rocket argument, the same way asks the beginner to take in a second new idea, that clocks at two heights tick at different rates (with a new term), together with what stays the same at each height. The way's question is only whether the ceiling counts as many crests.
- “If it lost more, the machine run backwards, sending light down, would.”: The sentence ends on 'would' and leaves the reader to supply 'make energy'. It also hides the step that makes the backwards machine win: light sent down gains what climbing light loses, and that would beat the cost of lifting a lump.
- “By the equivalence of gravity and acceleration, Earth gives the same count.”: The question offers 'more, fewer, or the same', so 'the same count' reads as the answer 'the same' rather than 'the same as the rocket'.
- “each packet of light arrives with slightly less energy, the fraction a lump gains by falling that far.”: 'the fraction' dangles: the listener cannot tell whether it is the energy lost or a separate amount.
- Fix: Split the rocket way (rule 17): the paragraphs on a lamp and clock at any height, the speed of light, and the missing crests moved unchanged into a new entry way 'where-the-missing-crests-go' (kind operational, continues light-climbing-in-a-rocket, recap restating the equivalence rule, visual lamp-and-detector-in-a-rocket). Common question head-older-than-feet now uses the new way.
- Fix: Rocket way: one drifting station per crest; the Doppler 'moving toward' half now in the explanation; the equal-height sentence gains its link to the Doppler rule.
- Fix: Tower way: the backwards-machine sentence now names what it makes and why. Physics diff check: this makes explicit that light sent down gains what climbing light loses (static field), which the physics review had accepted as implicit.
- Fix: Check light-sent-down and common question does-light-get-tired: wording fixes only.
- Fix: Budget, to absorb the new way at entry 1,000 and extras under 650, dropped the lowest-value items rather than compressing: the rocket way's siren sentence (its try_it already gives the passing-car test), 'The floor presses on your feet, as the ground does at home.', the 2010 clock sentence (kept at working rung in observation optical-clocks-33-centimetres), the tower way's closing 'Light sent down gains energy and arrives with a higher frequency.' (stated in the rocket way), the rocket try_it's last sentence 'For light crossing a rocket cabin, the change is far too small to see.', the working way energy-bookkeeping-with-symbols' simplifies (the same caveat is in derivation shift-from-energy-conservation step 2), and the working level-switch signal 'uses g, c or potential'.
- Fix: Bumped the revision to 3.

**Re-read** (2026-09-13, revision 5): 3 stumbles in 6 changed passages

- “Ask whether the uncounted crests pile up, then compare the floor and ceiling clocks.”: Rule 5: the step says 'missing crests', the move says 'uncounted crests', and the way they use says 'missing crests'. The spoken move offers a second name for one idea.
- “Do the crests the ceiling detector does not count pile up somewhere in the room?”: Spoken aloud, 'the crests the ceiling detector does not count pile up' runs two verbs together, so the listener has to reread to find where the question's verb starts. It also drops the step's name 'missing crests'.
- “It turns a count of crests into clocks that disagree.”: 'Clocks that disagree' does not say what they disagree about, and 'turns a count into clocks' is a figure of speech the tutor cannot say back plainly. The way's point is that the lower count comes from the clocks, not from lost crests.
- Fix: Teaching-arc step ask-where-the-crests-go: 'uncounted crests' became 'missing crests' in move and predict; predict reordered so its verb is clear; why reworded to name what the clocks explain. Claims unchanged: no crests pile up, and the ceiling clock accounts for the lower count, as the way states.
- Fix: Step title unchanged. Tutoring grows by a few words, inside the 10% review allowance; nothing dropped.
- Fix: Bumped the revision to 5.

## Review: physics

**Verdict:** fixed (2026-09-13, revision 5)

**Verification**

- Entry rocket argument: a receiver moving away from the station (the lamp's rest frame at emission) counts fewer crests, on its own clock.: Relativistic Doppler with the source at rest at emission: f_r = gamma(1-beta) f_S = sqrt((1-beta)/(1+beta)) f_S, which already uses the receiver's proper time. → Correct. The novice concern about station time versus detector clock does not arise: the Doppler factor is stated for the detector's own clock, and the difference between the two is second order in gH/c^2 in any case.
- Entry: a detector at the lamp's height, across the room, counts no shift.: Station frame, first order: light aimed to hit a detector a distance L across has a forward direction component gL/(2c^2); the detector gains gL/c along the rocket axis; Doppler 1 - n.v/c differs from 1 only at second order. Exactly, Rindler observers at equal x have equal lapse. → Claim true (exactly). The novice reason 'carries both along in step' was wrong as a reason, since floor and ceiling also move in step yet show a shift. Replaced by 'the detector speeds up across the crest's path, not along it'.
- Entry: light crosses one metre in a three-hundred-millionth of a second, so the ceiling gains about a ten-million-billionth of light's speed; one part in ten million billion per metre.: python: 1/c = 3.34e-9 s; 10 m/s^2 times that over c = 1.11e-16; g/c^2 = 1.09e-16 per metre. → Correct.
- Entry: blue-green light has about 600 thousand billion crests per second.: python: c/6e14 Hz = 500 nm. → Correct; 500 nm is blue-green.
- Entry: 2010 clocks showed it for a raise of about 30 centimetres.: WebSearch of the Science abstract. → Raise was 33 cm, shift (4.1 +/- 1.6)e-17; 'about 30 centimetres' is fair.
- Entry: ultraviolet causes sunburn and bright red light does not, because packet energy is set by frequency.: Physical reasoning: erythema needs UV photons energetic enough to damage DNA; red photons at any intensity cannot, although intense light can heat. → Acceptable as written.
- Tower way try_it: sugar bag 1 kg falling 1 m gains about 10 J; mc^2 about 9e16 J; ratio about one ten-millionth-billionth.: python: 9.81 J, 8.99e16 J, ratio 1.09e-16. → Correct.
- Tower way: forward cycle forbids losing less, reversed cycle forbids losing more, so the loss is exact.: Logic check: the reversed cycle bounds the gain of descending light, which equals the loss of climbing light because the downward trip is the upward trip reversed (static field). → Correct with that implicit reversibility; acceptable at entry.
- Working: f_r/f_e = sqrt((1-beta)/(1+beta)) = 1 - gH/c^2 + O(g^2H^2/c^4), with beta = gH/c^2.: Series expansion; python at beta = 1e-3: exact 0.99900050 vs 1 - beta + beta^2/2 = 0.9990005. → Correct; the second-order term is beta^2/2 as the O-term says.
- Working: slabs combine to (f_r - f_e)/f_e = -(Phi_r - Phi_e)/c^2 with g = dPhi/dz, Phi = -GM/r.: ln(f_r/f_e) = -integral g dz / c^2 = -(Phi_r - Phi_e)/c^2; sign checked: Phi increases with height, so climbing gives a negative change. → Correct.
- Working numbers: 22.5 m gives -2.46e-15; Earth surface to infinity -6.96e-10; Sun surface to infinity -2.12e-6.: python with GM_E = 3.986e14, R_E = 6371 km, GM_sun = 1.327e20, R_sun = 6.957e8 m. → 2.456e-15, 6.961e-10, 2.1225e-6. Correct.
- Energy route: nhf_b = mc^2 + mgH, nhf_t = mc^2, f_t/f_b approx 1 - gH/c^2; downward check f_b/f_t approx 1 + gH/c^2.: Hand algebra; the local energy of a lump dropped from rest measured by a static observer at the bottom is mc^2 N_top/N_bottom approx mc^2(1 + gH/c^2). → Correct. Photon number renamed from N to n, because N is the lapse in the formal way.
- Mossbauer: 14.4 keV = 2.31e-15 J; fractional width about 3e-13; shift about one per cent of the width; compensating speed 0.74 micrometres per second; upward-moving source gives a blueshift.: python: 14.4 keV = 2.307e-15 J; natural width hbar/tau with tau = 141.8 ns gives 3.2e-13; 2.46e-15/3.2e-13 = 0.76 per cent; gH/c = 7.36e-7 m/s. → Correct.
- Check detector-let-go-at-the-top: H/c = 7.5e-8 s, v = 7.4e-7 m/s, Doppler +2.46e-15 cancels, answer 0 with abs_tol 2e-16.: python. → 7.51e-8 s, 7.36e-7 m/s. Correct; the answer holds for release from rest at emission, and the misconception correction was scoped to that case.
- Check crests-over-a-tower: about 2 fewer per second over 30 m for 6e14 Hz.: python: 6e14 x 30 x 1.09e-16. → 1.96; value 2 with rel_tol 0.25 fine.
- Common question head-older-than-feet: 1.7 m gives two parts in ten million billion; 80 years gives half a millionth of a second.: python. → 1.86e-16; 4.7e-7 s. Correct.
- Worked example light-from-the-sun: -2.112e-6, equivalent 633 m/s.: python including the Sun's potential at 1 au and Earth's surface potential. → 2.1119e-6; 633.1 m/s. Correct.
- Problem gps-signal-reaching-the-ground: +5.29e-10 and +5.4 mHz.: python with GM = gR^2 = 3.982e14, r = 26,560 km. → 5.286e-10, 5.41e-3 Hz. With GM = 3.986e14: 5.291e-10. Tolerances fine. Speed part -0.83e-10 and net 4.46e-10 match the gps-clock-offset observation and the -4.465e-10 factory offset.
- Formal: E_xi = -xi_mu k^mu conserved; omega = -k_mu u^mu = E_xi/N; omega_r/omega_e = N_e/N_r; weak field N approx 1 + Phi.: Re-derived: k^nu nabla_nu(xi_mu k^mu) = k^nu k^mu nabla_(nu xi_mu) + xi_mu k^nu nabla_nu k^mu = 0; with signature (-,+,+,+) and u = (1,0,0,0), -k_0 = omega; g_tt = -(1 + 2Phi) gives N approx 1 + Phi. → Correct. Added that the Killing norm equals the ADM lapse only for static metrics; for stationary rotating metrics the lapse of t = const slices is 1/sqrt(-g^tt).
- Formal: neutron star 2M/R = 0.345, exact 0.810, first order 0.828.: python: sqrt(0.655) = 0.80932; 1 - 0.1725 = 0.8275. → Exact value corrected to 0.809.
- Problem crests-are-time-translates: omega_r/omega_e = sqrt(g_tt(x_e)/g_tt(x_r)), valid with g_ti nonzero.: Time-translation argument; dtau = sqrt(-g_tt) dt at fixed x^i. → Correct.
- Rindler: ds^2 = -(1 + ax)^2 dt^2 + ..., proper acceleration a/(1 + ax), check ratio 1/(1 + aL/c^2) = 0.492 for one light-year at 9.81 m/s^2.: Acceleration from the static observer's 4-acceleration magnitude d ln N/dx; python aL/c^2 = 1.03265, ratio 0.49197. → Correct; Riemann vanishes.
- Observation Gravity Probe A: gravitational part near 10,000 km about 4.3e-10; agreement level.: python GM_E/c^2 (1/R_E - 1/(R_E + 1e7 m)) = 4.25e-10; WebSearch of the PRL abstract (agreement at 70 x 10^-6). → Number correct; agreement changed from 'about 1e-4' to 'about 7e-5'.
- Observation pound-rebka-tower: 1.05 +/- 0.10, about 1 per cent by 1965.: WebSearch of the 1960 PRL and the 1965 follow-up result (0.9990 +/- 0.0076). → Correct.
- Reference Pound and Rebka 1960, Phys. Rev. Lett. 4, 337-341, doi 10.1103/PhysRevLett.4.337.: WebSearch: APS, ADS. → Confirmed; verified.
- Reference Vessot, Levine, Mattison et al. 1980, Phys. Rev. Lett. 45, 2081-2084.: WebSearch: APS, ADS, NTRS. → Confirmed; DOI 10.1103/PhysRevLett.45.2081 added; verified.
- Reference Chou, Hume, Rosenband, Wineland 2010, Science 329, 1630-1633.: WebSearch: PubMed, NIST, Science. → Confirmed; DOI 10.1126/science.1192720 added; verified.
- Reference Ashby 2003, Living Reviews in Relativity 6, 1.: WebSearch: Springer. → Confirmed; DOI 10.12942/lrr-2003-1 added; verified.
- History Einstein 1907, Jahrbuch der Radioaktivitaet und Elektronik 4, 411-462; clock rates and solar line shift from the equivalence principle.: WebSearch: ADS and historical records. → Confirmed (volume 4 is dated 1907; ADS indexes the bibcode as 1908). Scope correct: the paper's final section derives the clock-rate factor and the solar line shift. Verified.
- History Einstein 1911, Annalen der Physik 35, 898-908; accelerating-frame and energy arguments, two parts in a million for sunlight.: WebSearch: Wiley, ADS. → Confirmed; DOI 10.1002/andp.19113401005 added; verified.

**Counterexamples tried**

- Horizontal separation at equal height (equal potential): the novice reason 'carried along in step' failed, because floor and ceiling also move in step. Replaced by the sideways-speed reason; the claim itself holds exactly by equal lapse.
- Moving receiver: a detector released from rest at emission cancels the shift to first order; a detector already falling at another speed would not. The misconception correction 'falling freely during the climb' was scoped to release from rest as the light leaves.
- Strong field (neutron star, 2M/R = 0.345): the first-order law misses by about 2 per cent; the note already says so. Exact value rounding corrected.
- Non-static case (expanding universe): no timelike Killing vector; the formal way states the construction does not apply. Cosmological redshift is linked as a different effect.
- Stationary rotating case (Kerr): the Killing norm differs from the ADM lapse, and inside an ergoregion the Killing vector is not timelike. The condition 'timelike at both ends' covers the second; a terminology clause now covers the first.
- Flat spacetime with accelerating observers (Rindler): redshift without curvature; the note uses this as its contrast, and the one-light-year check shows the first-order law failing.
- Non-relativistic limit and Earth's rotation: the first-order law is the Newtonian potential over c^2; rotation is named in the measuring way's simplifies.
- Light sent down: blueshift is stated at every rung, so 'gravity always reddens' does not survive.

**Fixes**

- Entry rocket way: replaced the incorrect reason for no shift at equal height with 'While a crest crosses the room, the detector speeds up across the crest's path, not along it.' Trimmed 'The engine is on, so the rocket keeps speeding up' to 'Its engine keeps it speeding up' to stay within the entry budget.
- Formal way: neutron-star exact ratio 0.810 corrected to 0.809; added that 'lapse' here means the Killing norm, equal to the lapse of the t = const slicing only for static metrics; key equation symbol N updated to match.
- Photon number renamed from N to n in the energy way, its derivation and the energy-route-downward check, since N is the lapse elsewhere in the note.
- Derivation shift-from-energy-conservation: replaced the invalid KaTeX m\' with m'.
- Misconception every-detector-sees-the-shift: correction scoped to a receiver let go from rest as the light leaves.
- Observation gravity-probe-a: agreement stated as about 7e-5, as published.
- Added DOIs for all four observation references and the 1911 paper; set verified true on all six references.
- Visual sketch lamp-and-detector-in-a-rocket now measures speeds from a station drifting with the lamp at each emission, matching the entry wording.
- Word-budget trims to absorb the fixes: two misconception lines, two visual sketches, and the 1907 history contribution, with meaning unchanged.

**Concerns**

- The fixes change learner-visible entry text (one sentence in the rocket way). Revision kept at 2 so both reviews cover the same text; an editor may bump the revision and ask for a novice re-read of that sentence.
- Conventions file gaps, not invented here: no frequency symbol (f versus nu versus omega), no redshift z, no weak-field g_tt = -(1 + 2Phi/c^2) row, and no definition of 'lapse' (Killing norm versus ADM lapse). The note also uses g for both free-fall acceleration and metric components g_tt in different rungs.
- Four prerequisites (conserved-quantity-from-killing-vector, energy-measured-by-an-observer, newtonian-gravitational-potential, rindler-coordinates) exist in the registry but are not in this concept's registry prerequisite list; none depends on gravitational-redshift, so no cycle. sync_registry.py should apply them.
- Budgets are at their caps: entry explanations 999 of 1,000, tutoring 2,199 of 2,200, links at 300.
- The tower way's 'exactly' relies on the downward trip being the upward trip reversed; this is true in a static field and acceptable at entry, but a future edit should not remove 'run backwards'.

**Diff check** (2026-09-13, revision 3)

- Rocket way: 'For each crest, measure speeds from a space station drifting beside the rocket. At the moment the crest leaves the lamp, the station moves along with the rocket...': Compared with the old wording and the instantaneous rest frame of the lamp at each emission. → Accurate, and sharper than before: 'for each crest' makes clear that a new momentarily co-moving station goes with each emission.
- Rocket way: 'A receiver moving away from a source of waves meets the crests less often, and one moving toward it meets them more often.': Checked sense and conditions against the relativistic Doppler law for a source at rest and a receiver moving along the line of the waves. → Accurate. Motion along the line is implied by 'away' and 'toward'. The added clause supports the blueshift paragraph.
- Rocket way: 'While a crest crosses the room, the detector speeds up across the crest's path, so it moves neither toward the crests nor away from them.': Station-frame calculation for a detector at the lamp's height: receiver velocity gt upward, beam tilted up by about gt/(2c) to meet it, observed ratio gamma(1 - beta.n) computed with python3 for t = 1e-8, 1e-3 and 1 s. Cross-checked against equal lapse at equal height. → Ratio minus 1 is 0 to machine precision. The small along-path component (second order) is cancelled exactly by time dilation, so at entry the sentence claims the same as the accepted 'not along it' and is equally true.
- Rocket way removals: the siren sentence, 'The floor presses on your feet...', the 2010 clock sentence, and the try_it line 'far too small to see'.: Checked each for scope caveats a reader needs and for claims other parts depend on. → No caveat lost. The size is still stated ('The change is tiny', with the per-metre number). The 2010 result is still in observation optical-clocks-33-centimetres. The simplifies on heights much smaller than Earth's radius is kept.
- New entry way where-the-missing-crests-go: opener, lamp and clock at any height, the speed of light at any height, no pile-up, the ceiling clock ticking off more seconds, gravitational time dilation, recap, takeaway and question.: Compared the moved paragraphs word for word with revision 2. Checked the new opener, recap and takeaway against the rocket way, local position invariance, stationarity of the rocket cabin and a static field (each crest has the same coordinate travel time), and the check where-do-the-crests-go (f_e/f_r = 1 + gH/c^2). → Accurate. The paragraphs are unchanged. 'Counted on each one's own clock' names both measurers. The recap restates the equivalence rule as the rocket way does. The takeaway matches the explanation and the check. Common question head-older-than-feet (about 1.9e-16 for 1.7 m; about 4.7e-7 s over 80 years) fits the new way.
- Tower way: 'If it lost more, the tower run backwards would make energy, because light sent down would gain more than lifting a lump cost.': Ran the backward cycle: a lump of mass m becomes light at the top, and light sent down comes back with ratio 1/(1 - e) if climbing loses a fraction e. At the bottom, remake mass m, keep m c^2 e, and lift the lump for m g H. Checked with python3 for e = 2gH/c^2 over H = 1 m. → Accurate for a static field, where the downward trip reverses the upward one (the premise of the earlier concern, and 'run backwards' is kept). Gain 2.2e-16 exceeds lift cost 1.1e-16 per unit rest energy, so a net gain follows whenever e > gH/c^2. The dropped closing blueshift sentence is still stated in the rocket way and in check light-sent-down.
- Working way energy-bookkeeping-with-symbols: the simplifies about ideal converters and ground momentum was removed.: Checked where the caveat still appears. → Not lost. Derivation shift-from-energy-conservation step 2 says the massive ground takes the momentum but negligible energy. The entry tower way's simplifies names imaginary machines and ground pushes, and the working text says 'to first order'.
- Check light-sent-down answer: 'a detector on Earth also counts more'.: Checked sense against the rocket blueshift and against f_floor/f_ceiling = 1 + gH/c^2 in a static field. → Accurate, and more precise than the old 'gives the same count', which could be misread as 'no shift'.
- Common question does-light-get-tired: 'by the fraction a lump gains by falling that far'.: Compared with the old sentence. → Grammar only. Same claim, still true for detectors held still at each height.
- Level-switching signal 'uses g, c or potential' removed.: Checked for physics content. → No physics content. Nothing to verify.

**Diff check** (2026-09-13, revision 5)

- Teaching-arc step ask-where-the-crests-go, step: 'Ask where the missing crests go'.: Read against ways_in/where-the-missing-crests-go, whose question and explanation use 'missing crests' for the crests the ceiling detector does not count. → Accurate. It names a question, makes no claim, and uses the way's term.
- Move: 'Ask whether the missing crests pile up, then compare the floor and ceiling clocks.': Checked that the move leads to the way's answer (no pile-up; the clocks differ) and that the comparison is well defined: proper time at the ceiling between receptions against proper time at the floor between emissions, for the same crests. → Accurate. Both clocks are at rest in the room, and the comparison uses the same crests, so it does not depend on frame.
- Why: 'It traces the lower count to the floor and ceiling clocks, not to lost crests.' (It replaces 'It turns a count of crests into clocks that disagree.'): Exact Rindler calculation for a rocket cabin: floor at x0 = c^2/g, ceiling at x1 = x0 + H. A crest emitted at floor proper time tau_e has x - ct = x0 exp(-g tau_e/c), and it reaches the ceiling at tau_r = (x1/c)[ln(x1/x0) + g tau_e/c]. Tested against the inertial (Doppler) description and against a static field on Earth. → Accurate, and it claims the same as the old wording, only more precisely. tau_r - (x1/x0) tau_e is constant, so every crest makes the same trip and none are lost. dtau_r/dtau_e = x1/x0 = 1 + gH/c^2 exactly (3.3e-16 for H = 3 m), so the lower count per second is fully accounted for by the clocks. In the drifting station's description the same proper-time ratio shows up as a Doppler shift, so the sentence holds in either description.
- Predict: 'Do the missing crests, the ones the ceiling detector does not count, pile up somewhere in the room?': Checked that the question has a definite true answer at entry within the setup: a steady lamp in a static room, or a uniformly accelerating cabin. → Accurate. The answer is no, as the way and check where-do-the-crests-go state. The rewording keeps the old question's meaning.
- Step uses and visual: ways_in/where-the-missing-crests-go, checks/lamps-and-light-at-the-ceiling, visual lamp-and-detector-in-a-rocket.: Read the check and the way. Checked that the check's claims (a lamp and clock side by side agree at any height; light that climbed is counted lower; local light speed is c) support comparing the clocks. → Consistent. The check does not itself test pile-up. At working rung that is done by check where-do-the-crests-go, which targets misconception missing-crests-pile-up.
- Visual sketch sentence, not learner-visible: 'Timed from its own drifting station, each crest makes the same trip, so none pile up, while the ceiling clock ticks off more seconds for the same crests.': Used the same Rindler calculation. The cabin's boost symmetry makes each crest's trip identical in its own momentarily co-moving frame (to first order, travel time H/c, and the ceiling gains gH/c). → Accurate for the rocket cabin, and by equivalence for the room on Earth.
- Common question is-it-really-doppler now uses ways_in/where-the-missing-crests-go.: Compared the answer's 'clocks at different potentials' with the way's gravitational time dilation paragraph. → The link fits. The answer text is unchanged.
