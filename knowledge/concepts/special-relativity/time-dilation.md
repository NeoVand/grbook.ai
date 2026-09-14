---
type: "concept"
schema_version: 2
id: "time-dilation"
title: "Time dilation"
tagline: "Why a clock moving past your clocks counts less time than they do"
domain: "special-relativity"
tier: "foundation"
status: "physics-reviewed"
revision: 7
updated: "2026-09-13"
aliases: ["moving clocks run slow", "reciprocity of time dilation", "kinematic time dilation"]
prerequisites: ["invariance-of-the-speed-of-light", "principle-of-relativity", "relativity-of-simultaneity", "proper-time", "lorentz-factor", "four-velocity"]
leads_to: ["twin-paradox", "atmospheric-muon-time-dilation", "relativistic-doppler-effect", "ives-stilwell-experiment", "gps-relativistic-corrections"]
visuals: ["light-clock-on-a-passing-ship", "one-clock-against-a-line-of-clocks"]
---

# Time dilation

*Why a clock moving past your clocks counts less time than they do*

`time-dilation` · special-relativity · foundation · physics-reviewed (revision 7)

**Needs:** [[invariance-of-the-speed-of-light]] (entry) · [[principle-of-relativity]] (entry) · [[relativity-of-simultaneity]] (entry) · [[proper-time]] (working) · [[lorentz-factor]] (working) · [[four-velocity]] (formal)  
**Opens:** [[twin-paradox]] · [[atmospheric-muon-time-dilation]] · [[relativistic-doppler-effect]] · [[ives-stilwell-experiment]] · [[gps-relativistic-corrections]]  
**Related:** [[length-contraction]] · [[clock-hypothesis]] · [[gravitational-time-dilation]]  
**Visuals:** ★ [[light-clock-on-a-passing-ship]] · [[one-clock-against-a-line-of-clocks]]

> Picture a clock moving past you at a steady speed while you coast steadily. Time it with your synchronized clocks placed along its path. While the moving clock counts one second, your clocks count more than one second. People riding with it notice nothing odd. This stretch is tiny at everyday speeds and has no upper limit as the speed nears light's. While both sides coast steadily, those people find your clocks stretched too.

## You will be able to

**Entry**
- Explain with a light clock why a station's clocks find each tick of a passing ship's clock taking longer. `objectives/explain-light-clock-stretch` ← `checks/station-times-the-trip`, `checks/half-light-speed`, `problems/half-hour-at-eight-tenths`
- Explain why every clock on the ship shares the stretch while the crew notices nothing. `objectives/explain-all-clocks-alike` ← `checks/wristwatch-beside-the-light-clock`, `checks/crew-reads-their-own-clock`
- Describe how a station times a passing clock with two of its own clocks, and why the crew finds the station's clocks stretched too. `objectives/describe-two-clock-timing` ← `checks/each-side-finds-the-other-stretched`, `checks/side-by-side-readings`

**Working**
- Compute dilated times and small-speed lags in a chosen inertial frame. `objectives/compute-dilated-times` ← `problems/gps-motion-lag`, `checks/round-trip-reunion`
- Distinguish the tick spacing a watcher receives from the measured stretch. `objectives/distinguish-seen-from-measured` ← `checks/approach-and-recede`

**Formal**
- Prove that the inner-product factor is at least 1 and that inertial paths have the most proper time. `objectives/prove-factor-at-least-one` ← `problems/reversed-cauchy-schwarz`
- State why the Lorentz factor does not give the rate ratio of separated clocks in curved spacetime. `objectives/state-limits-of-the-factor` ← `checks/distant-clocks-in-curved-spacetime`
- Reconcile the mutual stretch by computing where each observer's slices meet a clock. `objectives/locate-reciprocity-on-slices` ← `checks/head-start-from-level-sets`

## Ways in

### 1. A light clock on a passing ship · entry · picture

*Why do a station's clocks find each tick of a passing ship's clock taking longer?*

**Recap:** Two facts, both tested many times. First, everyone who measures the speed of light in empty space gets about 300,000 kilometres per second, however they move relative to the light's source. Second, inside a ship that coasts steadily in a straight line, engines off, no experiment can reveal the ship's speed without looking outside.

Picture a spaceship coasting in a straight line past a space station. Measured with the station's rulers and clocks, the ship's speed is 6 tenths of light speed, about 180,000 kilometres per second.

Inside the ship, the crew builds a clock from two facing mirrors, one on the cabin floor and one on the ceiling, 4 metres away. So the line between them is at right angles to the ship's motion. A flash of light bounces between the mirrors, and each round trip is one tick. This is called a light clock.

Measured by the crew, the flash crosses the 4-metre gap. The station team measures the same 4-metre gap, because the gap lies across the ship's motion. But they measure a different path for the flash. While the flash crosses, the ship moves forward, so the flash travels on a slant to reach the other mirror. The station team measures the flash at light speed and the ship at 6 tenths of that. So the ship moves 6 tenths as far as the flash.

How long is the slant? Try 5 metres. Then the ship moves 3 metres, which is 6 tenths of 5. The 3 metres, the 4-metre gap and the 5-metre slant fit a right-angled triangle, because 3 times 3 plus 4 times 4 is 5 times 5. That is Pythagoras' rule, so 5 metres is right. The trip back is the same.

Light has the same speed for both teams, and a trip's time is its length divided by that speed. By the station's measurements, each crossing is 5 metres instead of 4, so it takes 5 quarters, or 1.25 times, as long. So by the station's clocks, each tick takes 1.25 times as long as the ship's clock counts.

This stretching of a moving clock's ticks, measured by clocks it moves past, is called time dilation. The station needs a line of clocks to measure it, as 'One travelling clock, two station clocks' shows.

The stretch, 1.25 here, is called the Lorentz factor. It depends only on the speed. At 99 hundredths of light speed, the ship moves almost as far as the flash, so the slant is about 7 times the gap and the factor is about 7. The factor has no upper limit as the speed nears light's.

Is only the light clock stretched? Suppose a wristwatch beside it were stretched by a different amount. Then on board their readings would drift apart, by an amount that depends on the ship's speed. The crew could then work out their speed without looking outside, which no experiment in a steadily coasting ship can do. So every clock on board, heartbeats included, is stretched by the same factor, measured by the station's clocks.

The crew notice nothing odd.

At everyday speeds the factor is almost exactly 1. Take a ship passing the station at a jet airliner's speed, 900 kilometres per hour. In 80 years of station time, its clocks would fall behind by under a thousandth of a second. That is why nobody notices time dilation in daily life.

**Try it:** On squared paper, mark a dot. Mark a second dot 4 squares above it, and a third dot 3 squares to the right of the second. Draw a line from the first dot to the third. Measure it with a ruler against the side of one square: it is 5 squares long. That line is the flash's slanted crossing by the station's measurements, longer than the 4-square crossing the crew measure.

**Takeaway:** By the station's measurements, the flash in a passing light clock takes a longer, slanted path. Light has one speed for everyone, so the station's clocks find every tick on board stretched.

*What this leaves out:* The ship coasts steadily in a straight line, far from planets, and the mirrors are perfect. Clocks at different heights near a planet also disagree, but that is a separate effect of gravity.

*Builds on:* [[invariance-of-the-speed-of-light]], [[principle-of-relativity]]<br>*Visuals:* [[light-clock-on-a-passing-ship]]<br>*See:* `checks/station-times-the-trip`

### 2. One travelling clock, two station clocks · entry · operational

*How does the station team actually time a passing clock?*

**Recap:** Light has one speed, about 300,000 kilometres per second, for everyone who measures it. A ship coasts past a station at 6 tenths of light speed. By the station's clocks, each tick of every ship clock takes 1.25 times as long as the ship's own count.

A passing clock never stays beside one station clock. So the station team times it with a long line of station clocks along the ship's path, like road markers.

First the team sets the clocks to agree. Long before the ship arrives, a flash leaves one of the clocks, clock A, carrying a coded message: clock A's reading as the flash left. At each other clock, a helper sets the clock to that reading plus the light's travel time. The travel time is the distance, measured with station rulers, divided by light's speed. For 300,000 kilometres, that adds 1 second. Clocks set like this are called synchronized.

The ship passes clock A. Side by side, the ship's clock and clock A both read zero. The ship coasts on to clock B, 9 million kilometres further. At 180,000 kilometres per second, that takes 50 seconds. Side by side at clock B, clock B reads 50 seconds and the ship's clock reads 40. Fifty is 1.25 times 40, the light clock's stretch.

No light delay spoils these readings, because each pair was read side by side.

**Takeaway:** The station times a passing ship clock with two synchronized station clocks, each read side by side with it.

*Continues:* `ways_in/light-clock-on-a-passing-ship`<br>*Visuals:* [[one-clock-against-a-line-of-clocks]]<br>*See:* `checks/side-by-side-readings`

### 3. The crew time a station clock · entry · operational

*How can the crew find the station's clocks stretched too?*

**Recap:** Light has one speed for everyone who measures it. Nobody inside a steadily coasting ship or station can find its speed without looking outside. A station sets a line of clocks to agree, using a flash from clock A and allowing for light's travel time. Such clocks are called synchronized. A ship coasts past the station at 6 tenths of light speed. From station clock A to station clock B, the ship's clock counts 40 seconds and the station's clocks count 50.

Turn around the timing of one travelling clock against two station clocks. The crew cannot find their speed without looking outside, so the same reasoning works for them. Measured by the crew, the station slides toward the ship's rear at 6 tenths of light speed. So by the crew's own line of synchronized clocks, coasting beside the ship, each tick of a station clock takes 1.25 times as long as that clock's own count.

The crew time station clock B from the moment the ship passes clock A. At that moment, by the crew's clocks, one crew clock is beside clock B. Clock B slides back to the ship, arriving when the ship's clock reads 40. So 40 seconds pass by crew clocks, and clock B, stretched 1.25 times, counts 40 divided by 1.25, only 32 seconds. Clock B reads 50 on arrival, so by the crew's clocks it read 18 at the start.

Why that head start? Measured by the crew, the station's line slides toward the ship's rear, so clock B moved toward the flash from clock A that set it. The flash reached clock B sooner than the station team allowed for, so clock B was set ahead. By station measurements, light takes 30 seconds to cross the 9 million kilometres from clock A to clock B. The head start is 6 tenths of those 30 seconds.

The teams disagree about which readings on distant clocks happen at the same moment. That is why both stretches hold while both sides coast steadily.

**Takeaway:** Each side times one of the other side's clocks with two of its own synchronized clocks. The teams disagree about how distant clocks were set, so each finds the other's clocks stretched.

*What this leaves out:* Both stretches hold only while both sides coast steadily. A ship clock that flies out, turns around and comes back returns showing less time than the station clock it left. The two sides are then not alike: only the station coasted steadily the whole time.

*Continues:* `ways_in/one-ship-clock-two-station-clocks`<br>*Builds on:* [[principle-of-relativity]], [[relativity-of-simultaneity]]<br>*Visuals:* [[one-clock-against-a-line-of-clocks]]<br>*See:* `checks/each-side-finds-the-other-stretched`

### 4. The Lorentz factor from the light clock · working · calculation

*What is the exact stretch for any speed, and how large is it for real clocks?*

The 3-4-5 triangle of the light clock on a passing ship gave a Lorentz factor of 1.25 at $0.6c$. The same triangle works for any speed $v < c$. Let the mirrors be a distance $L$ apart. For the crew a tick is a round trip, so it lasts $\Delta\tau = 2L/c$ by the ship's clock. This is the proper time between the two tick events: the time read by the one clock present at both.

For the station the tick lasts $\Delta t$, read on two synchronized station clocks. In half of it the flash runs $c\Delta t/2$ along the slant while the mirrors move $v\Delta t/2$. The gap is still $L$, because distances at right angles to the relative motion agree for both teams; otherwise two equal hoops sliding through each other along their common axis would each pass inside the other. Pythagoras gives $(c\Delta t/2)^2 = L^2 + (v\Delta t/2)^2$, and the derivation 'Time dilation from the light clock' solves it:

$$\Delta t = \gamma\,\Delta\tau, \qquad \gamma = \frac{1}{\sqrt{1 - v^2/c^2}}.$$

The gap has dropped out, and by the principle of relativity every clock riding with the mirrors shares the factor. The invariant interval gives the same result directly: the tick events are $v\Delta t$ apart for the station and at one place for the crew, so $-c^2\Delta t^2 + v^2\Delta t^2 = -c^2\Delta\tau^2$.

Three features matter. First, $\gamma \ge 1$, with equality only for $v = 0$. Second, it grows slowly and then without bound: $\gamma = 1.005$ at $0.1c$, $1.155$ at $0.5c$, $1.25$ at $0.6c$ and $7.09$ at $0.99c$. Third, only $v^2$ appears, so the measured stretch is the same for a clock approaching or receding.

For $v \ll c$, $\gamma \approx 1 + v^2/2c^2$, so the moving clock falls behind by $\Delta t - \Delta\tau \approx (v^2/2c^2)\,\Delta t$. At 900 km/h, $250$ m/s, the fraction is $3.5\times10^{-13}$: $0.88$ ms in 80 years.

Real clocks confirm the formula at both extremes. Muons circulating in a storage ring with $\gamma = 29.33$ lived that many times longer, by laboratory clocks, than muons at rest, although the ring gave them proper accelerations near $10^{18}g$. Aluminium-ion optical clocks detected the fraction $v^2/2c^2$ for an ion oscillating at root-mean-square speeds of a few metres per second.

**Takeaway:** By a frame's synchronized clocks, a clock moving at speed v takes gamma times its own proper time per tick, where gamma is one over the square root of one minus v squared over c squared.

*What this leaves out:* Steady relative motion in flat spacetime, with crosswise distances equal for both teams.

*Continues:* `ways_in/light-clock-on-a-passing-ship`<br>*Builds on:* [[proper-time]], [[lorentz-factor]]<br>*See:* `derivations/light-clock-derivation`, `worked_examples/storage-ring-muons`, `observations/muons-in-a-storage-ring`, `observations/aluminium-ion-clocks`

### 5. What a telescope shows is not the stretch · working · contrast

*Does a clock rushing toward you look slow, and why does a telescope view differ from the measured stretch?*

In the timing with one travelling clock and two station clocks, each pair of clocks was read side by side, so no light had to cross any distance. A watcher at one place who looks through a telescope gets something else, because the light from successive ticks crosses a changing distance.

Let the ship's lamp flash once per tick $\Delta\tau$ of the ship's clock while the ship recedes directly from a station watcher at speed $v$. By the station's synchronized clocks the flashes leave $\gamma\Delta\tau$ apart. Meanwhile the ship moves $v\gamma\Delta\tau$ farther away, so the next flash arrives later by an extra $v\gamma\Delta\tau/c$. The derivation 'Received spacing of a clock’s flashes' collects this into

$$\Delta t_{\text{rec}} = \gamma\left(1 \pm \frac{v}{c}\right)\Delta\tau = \sqrt{\frac{1 \pm v/c}{1 \mp v/c}}\;\Delta\tau,$$

with the upper signs for a receding clock and the lower signs for an approaching one.

At $v = 0.6c$ a receding clock's flashes arrive $2\Delta\tau$ apart and an approaching clock's flashes arrive $0.5\Delta\tau$ apart. Through the telescope the approaching clock looks twice as fast as its own count. Yet in both cases the measured stretch, with the travel time removed, is $1.25$. The received spacing mixes two effects: time dilation, which ignores the direction of motion, and the changing light-travel distance, which does not.

The two fit together over a round trip. For a clock that flies out and back at $0.6c$, spending equal times on each leg by its own count, the station receives outbound flashes spread by 2 and return flashes squeezed by $0.5$. The total reception time is $(2 + 0.5)/2 = 1.25$ times the clock's own total: exactly the measured stretch, since the last flash arrives at the reunion.

For flashes sent when the clock is at its nearest point to the watcher, by the station's measurements, the distance is momentarily not changing, and for closely spaced ticks the received spacing is $\gamma\Delta\tau$: pure time dilation.

**Takeaway:** A telescope view mixes the stretch with the changing light-travel distance, so an approaching clock can look fast even though measured clocks find it stretched.

*What this leaves out:* Motion directly toward or away from the watcher, apart from the nearest-point case; other directions add an angle-dependent factor.

*Continues:* `ways_in/one-ship-clock-two-station-clocks`<br>*Visuals:* [[one-clock-against-a-line-of-clocks]]<br>*See:* `derivations/received-flash-spacing`, `checks/approach-and-recede`

### 6. The factor as a product of four-velocities · formal · structure

*What is time dilation without coordinates, and where does the statement stop being meaningful?*

The Lorentz factor from the light clock, and the timing of one travelling clock against two station clocks, have a coordinate-free form. Set $c = 1$ in this way.

An inertial observer with unit future-directed timelike four-velocity $n$ builds synchronized clocks whose readings define the time function $t_n(p) = -\eta(n, p - o)$ for a reference event $o$. Its level sets, the observer's surfaces of simultaneity, are the hyperplanes orthogonal to $n$. A second inertial clock with four-velocity $u$ ticks at events $p$ and $q = p + \Delta\tau\,u$, so by linearity

$$\Delta t_n = -\eta(n, u)\,\Delta\tau.$$

Split $u = \gamma(n + V)$ with $\eta(n, V) = 0$. The observer measures the clock's velocity as $V$, of speed $v = \sqrt{\eta(V, V)}$, and the normalization $\eta(u, u) = -1$ gives $\gamma = (1 - v^2)^{-1/2} = -\eta(n, u) = \cosh\phi$ for rapidity $\phi$.

*Theorem (reversed Cauchy–Schwarz inequality).* For future-directed unit timelike vectors $n$ and $u$, $-\eta(n, u) \ge 1$, with equality exactly when $u = n$. So between two ticks, a clock in relative motion records less proper time than the observer's synchronized clocks assign.

Reciprocity is the symmetry $\eta(n, u) = \eta(u, n)$: the time function $t_u$ assigns a clock at rest with $n$ the same factor. The two statements concern different pairs of events, because $t_n$ and $t_u$ have different level sets. When the crew time a station clock, the 18-second head start of clock B is the proper time along clock B's world line between the level sets $t_n = 0$ and $t_u = 0$ through the event where the ship passes clock A, restoring $c$.

For a clock on any timelike world line that obeys the clock hypothesis, $dt_n/d\tau = -\eta(n, u(\tau)) = \gamma(\tau)$, so $\Delta t_n = \int \gamma\,d\tau \ge \Delta\tau$. Comparing world lines between two fixed timelike-separated events instead gives the reverse triangle inequality: in Minkowski spacetime the inertial world line has the greatest proper time, which is the content of the twin effect.

Limits of validity. In Minkowski spacetime, vectors at different events are compared by translation, so $-\eta(n, u)$ is meaningful for any two inertial observers, and $t_n$ is a global time function. In curved spacetime there is no global inertial frame, so a synchronized time function like $t_n$ holds only approximately, within a local inertial frame, and $-g(n, u)$ is defined only for four-velocities at the same event. Distant four-velocities can be compared only by transporting one to the other along a chosen curve, so rate differences between distant clocks, such as gravitational or cosmological ones, are not the Lorentz factor of a relative speed. In SI units $\gamma = (1 - v^2/c^2)^{-1/2}$.

**Takeaway:** The dilation factor is minus the inner product of two unit four-velocities: at least 1, symmetric in the two observers, and in curved spacetime defined only for clocks at the same event.

*Continues:* `ways_in/gamma-from-the-light-clock`, `ways_in/crew-time-a-station-clock`<br>*Builds on:* [[four-velocity]]<br>*See:* `derivations/dot-product-form`, `problems/reversed-cauchy-schwarz`, `checks/distant-clocks-in-curved-spacetime`

## Glossary

| Term | Say | In plain words | Concept |
| --- | --- | --- | --- |
| light clock | — | A clock made of two facing mirrors with a flash of light bouncing between them; each round trip is one tick. | — |
| time dilation | time dye-LAY-shun | The stretching of the time between a clock's ticks, when the clock is timed by synchronized clocks that it moves past. | [[time-dilation]] |
| Lorentz factor | LOR-ents factor | How many times as long each tick of a clock lasts by synchronized clocks it moves past, compared with the clock's own count. | [[lorentz-factor]] |
| synchronized | SIN-kruh-nized | Set to agree by a method that allows for light's travel time between the clocks. | [[clock-synchronization]] |

## Key equations

### Time dilation · working

$$
\Delta t = \gamma\,\Delta\tau,\qquad \gamma = \frac{1}{\sqrt{1 - v^2/c^2}}
$$

Between two ticks of a clock moving at speed $v$, the synchronized clocks of a frame it moves through read $\gamma$ times the clock's own proper time.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $\Delta t$ | time between the ticks on the frame's synchronized clocks | the frame's time |
| $\Delta\tau$ | proper time between the ticks, read on the moving clock | the clock's own time |
| $\gamma$ | Lorentz factor | gamma |
| $v$ | the clock's speed in that frame | the speed |

**Holds when:** Inertial frame; clock at constant velocity; flat spacetime. Accelerated clocks need the clock hypothesis.  
**Say it:** “The frame's time equals gamma times the clock's own time, where gamma is one over the square root of one minus v squared over c squared.”  
**Justified by:** `derivations/light-clock-derivation`

### Lag at small speeds · working

$$
\Delta t - \Delta\tau \approx \frac{v^2}{2c^2}\,\Delta t
$$

At everyday speeds the moving clock falls behind by the fraction $v^2/2c^2$ of the elapsed time.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $\Delta t - \Delta\tau$ | how far the moving clock falls behind | the lag |

**Holds when:** $v \ll c$; corrections of order $v^4/c^4$.  
**Say it:** “The lag is about v squared over two c squared times the elapsed time.”  
**Justified by:** `derivations/light-clock-derivation`

### Received spacing of a clock's flashes · working

$$
\Delta t_{\text{rec}} = \gamma\left(1 \pm \frac{v}{c}\right)\Delta\tau = \sqrt{\frac{1 \pm v/c}{1 \mp v/c}}\,\Delta\tau
$$

What one watcher receives from a clock moving directly away (upper signs) or toward (lower signs).

| Symbol | Meaning | Say |
| --- | --- | --- |
| $\Delta t_{\text{rec}}$ | spacing of arrivals on the watcher's clock | the received spacing |

**Holds when:** Motion along the line of sight; watcher at rest in the frame.  
**Say it:** “The received spacing is gamma times one plus or minus v over c, times the clock's own tick.”  
**Justified by:** `derivations/received-flash-spacing`

### Dilation factor as an inner product · formal

$$
\frac{dt_n}{d\tau} = -\eta(n, u) = \gamma \ge 1 \qquad (c = 1)
$$

An observer's synchronized time advances along a clock's world line at minus the inner product of their four-velocities.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $n$ | the observer's unit four-velocity | n |
| $u$ | the clock's unit four-velocity | u |
| $t_n$ | the observer's synchronized time function | the observer's time |

**Holds when:** Inertial observer in Minkowski spacetime; future-directed unit timelike vectors; clock hypothesis for accelerated clocks.  
**Say it:** “The rate of the observer's time along the clock is minus eta of n and u, which is gamma, at least one.”  
**Justified by:** `derivations/dot-product-form`

## Derivations

### Time dilation from the light clock · working

**Goal:** Show that $\Delta t = \gamma\,\Delta\tau$ for a light clock, and find the small-speed lag.

1. In the ship the mirrors are $L$ apart, at right angles to the motion, so one tick lasts $\Delta\tau = 2L/c$.
2. The station finds the same gap $L$, because crosswise distances agree for both frames.
3. In the station frame a tick lasts $\Delta t$; in half of it the flash runs $c\Delta t/2$ along the slant, since light has speed $c$ in every inertial frame, while the mirrors move $v\Delta t/2$.
4. Pythagoras: $(c\Delta t/2)^2 = L^2 + (v\Delta t/2)^2$.
5. Substitute $L = c\Delta\tau/2$ and multiply by 4: $c^2\Delta t^2 = c^2\Delta\tau^2 + v^2\Delta t^2$.
6. Collect terms: $\Delta t^2(1 - v^2/c^2) = \Delta\tau^2$, so $\Delta t = \gamma\,\Delta\tau$, taking positive durations.
7. For $v \ll c$, the binomial expansion gives $\gamma \approx 1 + v^2/2c^2$.
8. So $\Delta t - \Delta\tau = (1 - 1/\gamma)\,\Delta t \approx (v^2/2c^2)\,\Delta t$.

**Result:** $\Delta t = \gamma\,\Delta\tau$ with $\gamma = (1 - v^2/c^2)^{-1/2}$, and a lag of about $(v^2/2c^2)\,\Delta t$ at small speeds.

### Received spacing of a clock's flashes · working

**Goal:** Find the spacing of flashes received from a clock moving directly away from or toward a watcher.

1. The clock flashes once per proper tick $\Delta\tau$; by the watcher's synchronized clocks the flashes leave $\gamma\Delta\tau$ apart.
2. Receding, the clock moves $v\gamma\Delta\tau$ farther away between flashes.
3. The later flash needs extra travel time $v\gamma\Delta\tau/c$, so $\Delta t_{\text{rec}} = \gamma(1 + v/c)\Delta\tau$.
4. Since $\gamma = 1/\sqrt{(1 - v/c)(1 + v/c)}$, this equals $\sqrt{(1 + v/c)/(1 - v/c)}\,\Delta\tau$.
5. Approaching, the distance shrinks instead, so $\Delta t_{\text{rec}} = \gamma(1 - v/c)\Delta\tau = \sqrt{(1 - v/c)/(1 + v/c)}\,\Delta\tau$.

**Result:** $\Delta t_{\text{rec}} = \sqrt{(1 \pm v/c)/(1 \mp v/c)}\,\Delta\tau$, upper signs receding.

### The factor as an inner product · formal

**Goal:** With $c = 1$, show $\Delta t_n/\Delta\tau = -\eta(n, u) = \gamma$ for an inertial clock timed by an inertial observer.

1. The observer's synchronized time is $t_n(p) = -\eta(n, p - o)$; in its inertial coordinates, with $n = e_0$, this is $x^0$.
2. Two ticks of the clock are at $p$ and $q = p + \Delta\tau\,u$.
3. By linearity, $\Delta t_n = -\eta(n, q - p) = -\eta(n, u)\,\Delta\tau$.
4. Split $u = \gamma(n + V)$ with $\eta(n, V) = 0$; the displacement per unit $t_n$ is $V$, so the measured speed is $v = \sqrt{\eta(V, V)}$, and $-\eta(n, u) = \gamma$.
5. Normalization: $-1 = \eta(u, u) = \gamma^2(-1 + v^2)$, so $\gamma = (1 - v^2)^{-1/2}$.

**Result:** $\Delta t_n = -\eta(n, u)\,\Delta\tau = \gamma\,\Delta\tau$; restoring $c$, $\gamma = (1 - v^2/c^2)^{-1/2}$.

## Worked examples

### Muons in a storage ring · working

**Problem:** Muons circulate in a storage ring 14 m across with $\gamma = 29.33$. At rest their mean lifetime is 2.197 microseconds. Find their mean lifetime by laboratory clocks, their speed, the distance covered in that time, and the number of laps.

1. Laboratory lifetime: $\Delta t = \gamma\,\Delta\tau = 29.33 \times 2.197 = 64.44$ microseconds.
2. Speed: $v/c = \sqrt{1 - 1/\gamma^2} = 0.99942$.
3. Distance: $v\,\Delta t = 0.99942 \times (2.998\times10^8\ \text{m/s}) \times (6.444\times10^{-5}\ \text{s}) = 19.3$ km.
4. Laps: the circumference is $\pi \times 14\ \text{m} = 44.0$ m, and $19{,}300/44.0 \approx 440$.

**Answer:** About 64.4 microseconds, $v = 0.99942c$, 19.3 km, and about 440 laps.

**Takeaway:** Without the stretch a typical muon would cover about 660 m, some 15 laps; the ring makes the 29-fold stretch directly countable.

## Problems

### `half-hour-at-eight-tenths` · entry · difficulty 1 · calculation

A ship coasts past a space station at 8 tenths of the speed of light, measured by the station. Between passing two station clocks, the ship's own clock counts 30 minutes. Use a light-clock triangle to find how long the trip takes by the station's synchronized clocks, and how far apart the two station clocks are by the station's rulers. Take the speed of light as 300,000 kilometres per second.

**Hints**

1. While light travels 5 metres on the slant, how far does the ship move?
2. Find the gap with Pythagoras, then compare the slant with the gap.

**Answer:** 50 minutes, and about 720 million kilometres.

**Must contain:** The triangle has sides 3, 4 and 5, with the ship moving 4; Each tick takes 5 thirds as long by the station's clocks; 50 minutes and about 720 million kilometres

**Numeric:** trip time by the station's clocks = 50 min (magnitude, ±2%); distance between the markers = 7.2e+08 km (magnitude, ±2%)

**Solution**

1. While light travels 5 metres on its slant, the ship moves 8 tenths as far, 4 metres.
2. By Pythagoras' rule, the gap times itself is 5 times 5 minus 4 times 4, which is 9, so the gap is 3 metres.
3. The slant is 5 thirds of the gap, so each tick takes 5 thirds as long by the station's clocks, and 30 minutes becomes 50 minutes.
4. 50 minutes is 3,000 seconds. The ship covers 8 tenths of 300,000 kilometres, or 240,000 kilometres, each second, and 240,000 times 3,000 is 720 million kilometres.

### `gps-motion-lag` · working · difficulty 2 · estimate

A GPS satellite moves at 3.87 km/s relative to the Earth-centred frame that does not rotate with Earth. Using only time dilation from this speed, estimate how far its clock falls behind clocks at rest in that frame in one day, and how far light travels in that time. Why does the real correction for GPS clocks have the opposite sign?

**Hints**

1. Use the small-speed lag, with one day equal to 86,400 s.

**Answer:** About 7.2 microseconds per day, about 2.2 km of light travel. Height makes the clock gain about six times more, so for a spherical, non-rotating Earth it gains about 38.5 microseconds per day on a ground clock.

**Must contain:** The fraction v squared over two c squared is about 8.3 times ten to the minus eleven; About 7.2 microseconds per day; The gain from height is larger and opposite

**Numeric:** lag per day from motion = 7.2e-06 s (magnitude, ±3%); light-travel distance of the lag = 2.16 km (magnitude, ±5%)

**Solution**

1. $v^2/2c^2 = (3870\ \text{m/s})^2/\big(2 \times (2.998\times10^8\ \text{m/s})^2\big) = 8.33\times10^{-11}$.
2. Over one day: $8.33\times10^{-11} \times 86{,}400\ \text{s} = 7.2\times10^{-6}$ s, and light covers $2.16$ km in that time.
3. Height gives the fraction $GM(1/R - 1/r)/c^2 = 5.29\times10^{-10}$ with $r = 26{,}560$ km, 45.7 microseconds per day, so the net is a gain of 38.5.

### `reversed-cauchy-schwarz` · formal · difficulty 2 · proof

With $c = 1$, prove that future-directed unit timelike vectors $n, u$ satisfy $-\eta(n, u) \ge 1$, with equality only if $u = n$. Then show that two inertial legs $p \to q \to r$ with proper times $\tau_1, \tau_2$ and four-velocities $u_1 \neq u_2$ record less proper time than the inertial path from $p$ to $r$.

**Hints**

1. Split $u = a\,n + w$ with $\eta(n, w) = 0$.
2. Write $r - p = \tau_1 u_1 + \tau_2 u_2$.

**Answer:** $-\eta(n, u) = a = \sqrt{1 + \eta(w, w)} \ge 1$, and $\tau_{pr}^2 = \tau_1^2 + \tau_2^2 + 2\tau_1\tau_2\,\gamma_{12} > (\tau_1 + \tau_2)^2$, since $\gamma_{12} = -\eta(u_1, u_2) > 1$.

**Must contain:** Vectors orthogonal to a timelike vector are spacelike; a squared equals one plus a non-negative number; The cross term with gamma above one makes the straight path longest in proper time

**Solution**

1. Write $u = a\,n + w$ with $\eta(n, w) = 0$; $w$ is spacelike or zero, so $\eta(w, w) \ge 0$.
2. Normalization: $-1 = -a^2 + \eta(w, w)$, so $a^2 = 1 + \eta(w, w) \ge 1$.
3. Both vectors are future-directed, so $a = -\eta(n, u) > 0$; hence $a \ge 1$, with equality exactly when $w = 0$.
4. For the legs, $-\eta(r - p, r - p) = \tau_1^2 + \tau_2^2 + 2\tau_1\tau_2\,\gamma_{12}$, with $\gamma_{12} > 1$ because $u_1 \neq u_2$.
5. So $\tau_{pr}^2 > (\tau_1 + \tau_2)^2$. Check: legs of 3 years at $\pm 0.8$ give $\gamma_{12} = 41/9$ and $\tau_{pr} = 10$ years.

**Targets:** `reciprocity-means-equal-ages`

## Observations

- **Lifetimes of muons circulating near the speed of light in a storage ring** (measured, working). Muons with $\gamma = 29.33$ circulated in a ring 14 m across. Timed by laboratory clocks, their mean lifetimes were $\gamma$ times the rest lifetime, although the magnetic field gave them proper accelerations near $10^{18}g$, which also supports the clock hypothesis. *Numbers:* Positive muons: $64.419 \pm 0.058$ microseconds, about 29.3 times the rest lifetime of 2.197 microseconds; the dilation factor was confirmed to $2\times10^{-3}$ at 95% confidence. *Reference:* J. Bailey, K. Borer, F. Combley, H. Drumm and others (1977), *Measurements of relativistic time dilatation for positive and negative muons in a circular orbit*, Nature 268, 301–305, doi:10.1038/268301a0
- **Time dilation at a sprinter's speed, measured with two aluminium-ion optical clocks** (measured, working). The ion in one clock was pushed slightly off the centre of its trap, so it oscillated rapidly. Compared through 75 m of optical fibre with a second clock, its frequency was lower by the fraction $\langle v^2\rangle/2c^2$. *Numbers:* Root-mean-square speeds from a few metres per second to about 36 m/s; the shift is $-5.6\times10^{-16}$ at 10 m/s and about $-7.2\times10^{-15}$ at 36 m/s. *Reference:* C. W. Chou, D. B. Hume, T. Rosenband, D. J. Wineland (2010), *Optical Clocks and Relativity*, Science 329, 1630–1633, doi:10.1126/science.1192720

## Teaching arc

1. **Ask the passing-ship question** (entry). Pose the coasting ship and its light clock, and ask for a prediction. *Why:* A committed guess makes the triangle stick. *Predict:* By the station's clocks, does a tick of the ship's light clock last longer than a tick of an identical station light clock, or not? *Visual:* [[light-clock-on-a-passing-ship]] *Uses:* `ways_in/light-clock-on-a-passing-ship`
2. **Draw the triangle** (entry). Build the 3-4-5 triangle, then try half light speed. *Why:* Half light speed breaks a common guess. *Uses:* `checks/station-times-the-trip`, `checks/half-light-speed`
3. **Turn the timing around** (entry). Run the two-clock timing, then let the crew time a station clock. *Why:* The mutual stretch drives most worries about contradiction. *Predict:* When the crew time a station clock with their own clocks, will they find it stretched, squeezed, or normal? *Visual:* [[one-clock-against-a-line-of-clocks]] *Uses:* `ways_in/one-ship-clock-two-station-clocks`, `ways_in/crew-time-a-station-clock`, `checks/each-side-finds-the-other-stretched`
4. **Derive and size the factor** (working). Derive gamma, then meet it in storage-ring muons and the GPS lag. *Why:* One formula covers both extremes. *Uses:* `derivations/light-clock-derivation`, `worked_examples/storage-ring-muons`, `problems/gps-motion-lag`
5. **Separate seeing from measuring** (working). Compare received flash spacings with the measured stretch. *Why:* It removes the light-delay illusion. *Uses:* `ways_in/seen-ticks-versus-measured-ticks`, `checks/approach-and-recede`
6. **Make it invariant** (formal). Write the factor as an inner product, prove it is at least 1, and mark its limits. *Why:* It prepares clock comparisons in curved spacetime. *Uses:* `ways_in/dilation-as-a-dot-product`, `problems/reversed-cauchy-schwarz`, `checks/distant-clocks-in-curved-spacetime`

## Misconceptions

### “Only the light clock is stretched; a wristwatch on the ship is not.” · entry · `only-light-clocks-stretch`

- **Why it is tempting:** The argument only mentions light and mirrors.
- **What is true:** Clocks drifting apart on board would reveal a steadily coasting ship's speed, which no experiment can do. So every clock shares the stretch.
- **Exposed by:** `checks/wristwatch-beside-the-light-clock`

### “The crew would feel everything on board happen in slow motion.” · entry · `crew-feels-slowed`

- **Why it is tempting:** The slogan that moving clocks run slow sounds like a breakdown.
- **What is true:** Every process on board is stretched together, so on-board comparisons find nothing odd.
- **Exposed by:** `checks/crew-reads-their-own-clock`

### “If each side finds the other's clocks stretched, one side must be wrong.” · entry · `both-cannot-be-stretched`

- **Why it is tempting:** It sounds like each clock is slower than the other.
- **What is true:** Each side times one clock with two of its own, and the sides disagree about how distant clocks were set. So they compare different pairs of readings.
- **Exposed by:** `checks/each-side-finds-the-other-stretched`, `checks/head-start-from-level-sets`

### “The stretch is an illusion caused by light's travel time.” · entry · `just-light-delay`

- **Why it is tempting:** Light delay is familiar, like thunder after lightning.
- **What is true:** Side-by-side readings involve no light travel. A telescope view does, and it can make an approaching clock look fast.
- **Exposed by:** `checks/side-by-side-readings`, `checks/approach-and-recede`

### “At half light speed, each tick takes twice as long.” · entry · `stretch-follows-speed`

- **Why it is tempting:** Most everyday effects grow in step with speed.
- **What is true:** The stretch comes from a right-angled triangle, so at half light speed it is only about 1.15.
- **Exposed by:** `checks/half-light-speed`

### “A clock coming toward me runs fast, and one going away runs slow.” · working · `approaching-clock-runs-fast`

- **Why it is tempting:** That is what a telescope shows.
- **What is true:** Received spacing adds a changing light-travel distance. With that removed, the stretch is the same both ways.
- **Exposed by:** `checks/approach-and-recede`

### “Since the stretch is mutual, a traveller who returns is the same age as the stay-at-home.” · working · `reciprocity-means-equal-ages`

- **Why it is tempting:** Each leg looks symmetric.
- **What is true:** The mutual stretch holds only between steadily coasting clocks, and the traveller turns around. At reunion the returning clock shows less time.
- **Exposed by:** `checks/round-trip-reunion`

### “In curved spacetime, two distant clocks' rate ratio is the Lorentz factor of their relative speed.” · formal · `gamma-for-distant-clocks`

- **Why it is tempting:** The inner-product form looks fully general.
- **What is true:** In curved spacetime that product is defined only at one event. Static clocks at different heights have no relative speed yet differ in rate.
- **Exposed by:** `checks/distant-clocks-in-curved-spacetime`

## Checks

1. **Entry · numeric** `checks/station-times-the-trip`. A ship coasts past a station at 6 tenths of light speed, measured by the station. The ship's clock counts 20 minutes between passing station clocks A and B. How long is the trip by the station's synchronized clocks?
   - **Hints:** Which triangle goes with 6 tenths of light speed?
   - **Answer:** 25 minutes. At 6 tenths of light speed, the light-clock triangle has a 4-metre gap and a 5-metre slant. Light has one speed for everyone, so by the station's clocks every ship tick takes 5 quarters, or 1.25 times, the ship's count. 20 times 1.25 is 25.
   - **Must contain:** 25 minutes; The stretch at 6 tenths of light speed is 1.25
   - **Numeric:** trip time by the station's clocks = 25 min (magnitude, ±2%)
   - **Visual:** [[light-clock-on-a-passing-ship]]
2. **Entry · numeric** `checks/half-light-speed`. A ship passes a station at half light speed, measured by the station. A student says each ship tick takes twice as long by the station's clocks. Use a light-clock triangle with a 2-metre slant to find the real stretch.
   - **Hints:** Which number times itself makes 3?
   - **Answer:** About 1.15. The ship moves half as far as the flash: 1 metre for a 2-metre slant. By Pythagoras' rule, the gap times itself is 2 times 2 minus 1 times 1, which is 3. So the gap is about 1.73 metres, since 1.73 times 1.73 is about 3. Each crossing is 2 metres instead of 1.73, and 2 divided by 1.73 is about 1.15.
   - **Must contain:** The gap is about 1.73 metres; The stretch is about 1.15, not 2
   - **Numeric:** stretch factor = 1.155 1 (magnitude, ±2%)
   - **Targets:** `stretch-follows-speed`
   - **Visual:** [[light-clock-on-a-passing-ship]]
3. **Entry · explain** `checks/wristwatch-beside-the-light-clock`. On the coasting ship, a wristwatch lies beside the light clock. By the station's clocks, each light-clock tick is stretched 1.25 times. Does the wristwatch escape the stretch?
   - **Hints:** What would the crew notice if the two clocks kept different paces?
   - **Answer:** No. If the wristwatch were stretched by a different amount, the readings of the two clocks would drift apart in the cabin, by an amount that depends on the ship's speed. The crew could then work out their speed without looking outside, which no experiment in a steadily coasting ship can do. So the wristwatch is stretched by 1.25 too.
   - **Must contain:** No; Otherwise the drift would reveal the ship's speed on board
   - **Targets:** `only-light-clocks-stretch`
4. **Entry · predict** `checks/crew-reads-their-own-clock`. At home, a crew member counts 60 heartbeats in each minute of her light clock. On the ship, coasting past the station at 6 tenths of light speed, how many heartbeats does she count in each minute of the same light clock?
   - **Hints:** Is her heart stretched differently from her clock?
   - **Answer:** 60. Her heart and her light clock ride together, so the station's clocks find both stretched by 1.25. She compares them side by side on board, so the stretch cancels.
   - **Must contain:** 60 beats; Heart and clock are stretched together
   - **Numeric:** beats per minute of the light clock = 60 1 (magnitude, ±1)
   - **Targets:** `crew-feels-slowed`
5. **Entry · explain** `checks/each-side-finds-the-other-stretched`. The station times the ship's clock with clocks A and B and finds a stretch of 1.25. The crew time station clock B with two of their own clocks and also find 1.25. Must one team be wrong?
   - **Hints:** Were clocks A and B set to agree, by the crew's measurements?
   - **Answer:** No. Each team times one clock with two of its own. The station compares the ship's 40 seconds with its own 50. Measured by the crew, clock B moved toward the flash from clock A that set it, so clock B was set ahead. By crew clocks the ship takes 40 seconds to reach clock B. Clock B, stretched 1.25 times, counts only 32 of them. Clock B reads 50 on arrival, so when the ship passed clock A, by crew clocks, clock B read 50 minus 32, or 18. The station's 50 divided by 40 and the crew's 40 divided by 32 both equal 1.25.
   - **Must contain:** No, both are right; The teams disagree about how clock B was set
   - **Targets:** `both-cannot-be-stretched`
   - **Visual:** [[one-clock-against-a-line-of-clocks]]
6. **Entry · evaluate-claim** `checks/side-by-side-readings`. Someone says the ship's clock only seems stretched because its light takes time to reach the station. Judge this for the timing in which the ship passes station clocks A and B.
   - **Hints:** How far apart were the two clocks at each reading?
   - **Answer:** Wrong for this timing. At clock A, and again at clock B, the ship's clock and the station clock were read side by side. No light crossed any distance between them, so light delay cannot enter.
   - **Must contain:** Each reading is side by side; No light delay enters
   - **Targets:** `just-light-delay`
7. **Working · numeric** `checks/approach-and-recede`. A ship coasts at 6 tenths of light speed along a line of station clocks, with watcher W1 behind it and W2 ahead, both at rest in the station frame. Its lamp flashes once per second of ship time. Find the received spacing at W1 and at W2, and the emission spacing by station clocks.
   - **Hints:** Start with the emission spacing in the station frame.
   - **Answer:** Emission spacing: $\gamma = 1.25$, so 1.25 s. Between emissions the ship moves $0.6 \times 1.25 = 0.75$ light-seconds farther from W1, so flashes reach W1 2.0 s apart. For W2 the distance shrinks by 0.75 light-seconds: 0.5 s. Only received spacings depend on direction.
   - **Must contain:** Emission spacing 1.25 s; 2.0 s behind and 0.5 s ahead
   - **Numeric:** spacing received by W1 = 2 s (magnitude, ±2%); spacing received by W2 = 0.5 s (magnitude, ±2%); emission spacing by station clocks = 1.25 s (magnitude, ±2%)
   - **Targets:** `just-light-delay`, `approaching-clock-runs-fast`
   - **Visual:** [[one-clock-against-a-line-of-clocks]]
8. **Working · numeric** `checks/round-trip-reunion`. Measured by a station, a ship flies at 8 tenths of light speed to a beacon 4 light-years away, turns around quickly, and returns at the same speed. How much time passes on each clock, and does the mutual stretch make them equal?
   - **Hints:** Which clock is inertial for the whole trip?
   - **Answer:** Use the station's frame, inertial throughout. Each leg takes $4/0.8 = 5$ years, and with $\gamma = 5/3$ the ship's clock records 3. At reunion the clocks read 10 and 6 years. The mutual stretch relates two inertial clocks; the ship changes frame at the turnaround.
   - **Must contain:** 10 years and 6 years; Only the station is inertial throughout
   - **Numeric:** station clock = 10 yr (magnitude, ±1%); ship clock = 6 yr (magnitude, ±1%)
   - **Targets:** `reciprocity-means-equal-ages`
9. **Formal · evaluate-claim** `checks/distant-clocks-in-curved-spacetime`. Claim: two clocks at rest on a bench, one 33 cm above the other, tick at different rates, so a Lorentz factor of their relative velocity must give their rate ratio. Evaluate the claim.
   - **Hints:** What is the Lorentz factor at zero relative speed?
   - **Answer:** False. The clocks keep a constant radar distance, so their relative speed is zero and the Lorentz factor is 1. The measured difference, near $gh/c^2 = 3.6\times10^{-17}$ with the upper clock faster, is gravitational. In curved spacetime $-g(n, u)$ compares four-velocities only at one event; static rates follow $\sqrt{-g_{tt}}$ at each place.
   - **Must contain:** No relative speed; The difference is gravitational
   - **Targets:** `gamma-for-distant-clocks`
10. **Formal · numeric** `checks/head-start-from-level-sets`. Set $c = 1$. Ship $u = \gamma(n + V)$, $v = 0.6$, passes station $n$ at event $o$. Station clocks read $t_n(p) = -\eta(n, p - o)$, and clock B lies $D = 30$ light-seconds along $e = V/v$. With $t_u(p) = -\eta(u, p - o)$, find B's reading where $t_u = 0$, and the $t_u$ elapsed from there until the ship reaches B.
   - **Hints:** Evaluate $t_u$ on $o + D\,e + s\,n$.
   - **Answer:** 18 s and 40 s. Clock B's world line is $p(s) = o + D\,e + s\,n$, with $s$ its reading. Because $\eta(u, n) = -\gamma$ and $\eta(u, e) = \gamma v$, $t_u = \gamma(s - vD)$, which vanishes at $s = vD = 18$ s, not at $s = 0$. The ship reaches B at $s = D/v = 50$ s, so there $t_u = 1.25 \times 32 = 40$ s, the ship's own reading. So each observer's slices pair different events, and both factors of $\gamma$ hold.
   - **Must contain:** B reads 18 s on the ship's slice; B then counts 32 s while ship time advances 40 s; The slices pair different events
   - **Numeric:** clock B's reading on the ship's slice through o = 18 s (magnitude, ±1%); ship time elapsed until the ship reaches B = 40 s (magnitude, ±1%)
   - **Targets:** `both-cannot-be-stretched`

## Notation traps

| Issue | Course choice | Variants you will meet |
| --- | --- | --- |
| Sign of the interval between two ticks of a clock | Signature $(-,+,+,+)$: two ticks of a resting clock have $\Delta s^2 = -c^2\Delta\tau^2$. | With signature $(+,-,-,-)$ the ticks have $\Delta s^2 = +c^2\Delta\tau^2$; the dilation formula is unchanged. |

## Visuals

- ★ [[light-clock-on-a-passing-ship]] (flagship): The light clock seen by crew and station. *Sketch:* Split view: the crew's flash crossing a 4 m gap, and the station's slanted path. A speed slider redraws the triangle and shows the stretch; a wristwatch stays in step.
- [[one-clock-against-a-line-of-clocks]] (core): Two-clock timing, the mutual stretch, the telescope view. *Sketch:* A ship clock passes station clocks A and B. A toggle hands the timing to the crew's row, showing clock B set ahead; a telescope readout gives received spacings.

## Tutor moves

**Open with**

- A spaceship coasts past a space station at six tenths of light speed. Timed with the station's clocks, does one tick of the ship's light clock last longer than a tick of an identical light clock on the station, shorter, or the same? *(prediction)*

**If the learner is stuck**

- *The learner insists on knowing whose clock is really slow.* → Ask which clocks each team compared, then list the readings. *Uses:* `ways_in/crew-time-a-station-clock`, `checks/each-side-finds-the-other-stretched`

**Common questions**

- *Do astronauts on the International Space Station age differently from people on the ground?* (entry) Very slightly. The International Space Station circles Earth at almost eight kilometres per second. Compared with clocks on the ground, clocks aboard it fall behind by a little under five thousandths of a second every six months. That already includes a smaller, opposite effect of its height, which comes from gravity. *Uses:* `ways_in/light-clock-on-a-passing-ship`

**Switching levels**

- To working when: asks for the formula; asks how big the effect is at a given speed. Derive the factor from the light clock, then work the storage-ring muons. *Uses:* `derivations/light-clock-derivation`, `worked_examples/storage-ring-muons`
- To formal when: knows four-vectors; asks whether time dilation is invariant. Write the factor as an inner product and prove it is at least 1. *Uses:* `ways_in/dilation-as-a-dot-product`, `problems/reversed-cauchy-schwarz`

**Pronunciations:** Lorentz → LOR-ents; Cauchy–Schwarz → koh-SHEE shvarts; muon → MEW-on; Stilwell → STILL-well

**Voice notes:** Name the measurer whenever a duration is spoken.

## History

- **Albert Einstein (1905).** Deduced from the two postulates that a uniformly moving clock lags the synchronized clocks it passes by the factor now written $\gamma$. Albert Einstein (1905), *Zur Elektrodynamik bewegter Körper*, Annalen der Physik 17 (322), 891–921, doi:10.1002/andp.19053221004
- **Herbert E. Ives, G. R. Stilwell (1938).** Measured the second-order Doppler shift that time dilation predicts, in light from fast hydrogen atoms formed from accelerated hydrogen ions. Ives himself read the result within an ether theory. Herbert E. Ives, G. R. Stilwell (1938), *An Experimental Study of the Rate of a Moving Atomic Clock*, Journal of the Optical Society of America 28, 215–226, doi:10.1364/JOSA.28.000215

## Review: novice

**Verdict:** fixed (2026-09-13, revision 7)

**Retell attempt:** A spaceship flies past a space station really fast, 6 tenths of light speed. Inside, light bounces between two mirrors 4 metres apart, and that is a clock. The station people say the light goes on a slant because the ship moves, so it travels 5 metres instead of 4. Light has the same speed for everyone, so each tick takes 1.25 times longer by their clocks. That is time dilation, and 1.25 is the Lorentz factor. All the ship's clocks are stretched too, otherwise the crew could tell their speed, and the crew don't notice anything. At plane speeds it's less than a thousandth of a second in 80 years. Then the station uses a line of clocks, and the crew do the same thing back and find the station's clocks stretched, because clock B was set 18 seconds ahead. I didn't get where the 18 came from, why the crew also get 1.25, why the slant is 5 and not some other number, or which way the mirrors face.

**Stumbles (26)**

- “Time a clock that moves past you, using clocks at rest relative to you. Your clocks find each of its ticks lasting longer than its own count says.”: 'Time' at the start reads as a noun, and 'longer than its own count says' is hard to picture: a clock always counts one tick per tick.
- “Its riders notice nothing odd.”: 'Riders' of a clock is an odd image.
- “The mirrors face each other across the cabin, 4 metres apart, at right angles to the ship's motion.”: Ambiguous: a mirror 'at right angles to the motion' could have its line to the other mirror along the motion, which is the opposite layout.
- “The ship moves 6 tenths as far as the light does.”: A step is left implicit: this holds only because the station measures the flash at light speed, a fact the text used before it was invoked.
- “So while the light travels 5 metres on its slant, the ship moves 3 metres forward. The gap, the 3 metres and the 5 metres form a right-angled triangle, because 9 plus 16 is 25.”: The reader cannot see where 5 metres came from, and '9 plus 16' leaves the squaring unsaid.
- “Now use the light rule.”: 'The light rule' was never named; the recap says 'two facts'.
- “each tick takes 5 quarters of the crew's count, 1.25 times as long”: '5 quarters of the crew's count' needs rereading, and 'time is length divided by speed' was left implicit.
- “This stretching of a clock's ticks, measured by clocks it moves past, is called time dilation.”: The ship moves away from any one station clock, so the reader wonders which station clock times the tick.
- “At 99 hundredths of light speed it is about 7, because the slant is then about 7 times the gap.”: The reason restates the claim, and the summary's 'grows without limit' is never backed in the way.
- “Suppose a wristwatch beside the light clock kept a different pace. Then the crew could compare the two and work out their speed”: A step is missing: why would a different pace reveal the speed? The drift has to depend on the speed.
- “Slide the second dot 3 squares to the right”: You cannot slide an ink dot; the try-it's steps could not be followed as written.
- “no experiment inside a ship that coasts steadily, engines off, can reveal the ship's speed”: First what-if: look out of the window. The rule needs 'without looking outside' and 'in a straight line'.
- “As the flash reaches each clock further along, that clock is set to clock A's reading when the flash left, plus the light's travel time.”: Two steps are left implicit. How does the far clock know clock A's reading, and how is the travel time known?
- “The ship's clock and clock A sit side by side, and both read zero. The ship coasts on to clock B, about 9 million kilometres further along. Side by side again, clock B reads 50 seconds”: Where does 50 come from? The count distance divided by speed is left for the reader, and 'about' hides an exact number.
- “each later flash from its clock has less distance to travel, so the clock can even look fast”: 'Look fast' has no reference.
- “By the ship's clocks, each tick of the station clock takes 1.25 times as long.”: This is the most surprising claim of the note, and no reason is given for why the crew get the same number.
- “They carry a long line of their own synchronized clocks, coasting with the ship, and time one station clock”: The reader objects that a ship cannot carry a line of clocks millions of kilometres long, and which two crew clocks are used is never said.
- “Measured by the crew, the station's line slides backward”: 'Backward' has no reference.
- “By the crew's clocks, clock B already read 18 seconds when the ship passed clock A.”: The 18 seconds is taken on trust, with no count the reader can check.
- “A clock that flies out and comes back returns showing less time than the station clock it left.”: A surprising claim with no reason, right after the claim that the stretch is mutual.
- “so it was set 18 seconds ahead”: 'Ahead' of what? (the each-side check)
- “Between passing two station markers”: The problem says 'markers' while the ways say 'station clocks': two words for one thing.
- “Do astronauts on the space station age differently?”: 'Space station' collides with the note's fictional station, where the measuring team lives, while the astronauts here play the crew's role.
- “does each tick of its light clock take longer than the crew's count, shorter, or the same?”: 'Longer than the crew's count' is hard to picture, and 'its' could mean the station's or the ship's.
- “counts 60 heartbeats per minute of her light clock”: 'Per minute of her light clock' needs rereading.
- “The gap times itself is 4 minus 1, which is 3”: Where 4 and 1 come from is left implicit.

**Fixes**

- Summary and tagline: replaced 'longer than its own count says' with a doable comparison (while the moving clock counts one second, your clocks count more), and scoped the mutual stretch to steady coasting.
- Light-clock way: fixed the mirror layout (floor and ceiling), gave the reason the ship moves 6 tenths as far, turned the 3-4-5 triangle into a 'try 5 metres' check with Pythagoras named, spelled out 'time equals length divided by speed', backed 'about 7 at 99 hundredths' and 'no upper limit', added the speed dependence to the wristwatch argument, gave 6 tenths of light speed in km/s, and pointed to the two-clock way for why the station needs a line of clocks.
- Light-clock try-it rewritten as steps a reader can follow on squared paper; recap now says 'in a straight line' and 'without looking outside'.
- Two-clock way: explained how a far clock learns clock A's reading and the travel time, computed the 50 seconds, gave the principle-of-relativity reason why the crew also find 1.25, named the two crew clocks used, derived the 18-second head start from 40/1.25 = 32 and 50 - 32, gave the head-start rule as a checkable count (6 tenths of 30 s), and gave directions a reference (toward the ship's rear). Simplifies now says why a round trip breaks the symmetry.
- Checked every new number with python: 9 million km / 180,000 km/s = 50 s; head start 0.6 x 30 s = 18 s; gamma(0.99c) = 7.09; gamma(0.5c) = 1.155; 900 km/h over 80 years gives 0.88 ms; ISS net lag about 4.45 ms in six months (7.66 km/s, 420 km, ground rotation included).
- Entry checks, problem and tutor items: filled missing Pythagoras steps, said what 'ahead' is measured against, unified 'station clocks' (never 'markers'), renamed the real space station 'International Space Station' so it is not confused with the note's station, and reworded the opening question and arc prediction to compare with an identical station light clock.
- Ladder: the working way now opens by recalling the factor of 1.25 at 0.6c from the light-clock way. The formal way ties the 18-second head start to the gap between the level sets t_n = 0 and t_u = 0 along clock B's world line.
- Budgets: to stay under the foundation caps (entry 1,000, tutoring 2,200), trimmed wording in way paragraphs, working and formal check answers, misconception why_tempting and corrections, the analogy, notation traps and teaching-arc fields, without removing any item.
- Bumped the revision to 2.

**Concerns**

- Course conventions have no row for the Lorentz factor symbol gamma or for beta = v/c; the note uses gamma and avoids beta. A conventions row should be added (writer also raised this).
- The physics reviewer should confirm the new entry claims: the head-start rule (6 tenths of the light-crossing time of the station distance, measured by the crew) and the reason 'only the station coasted steadily' given for the round trip.
- The two-clock way asks a novice to follow two sets of synchronized clocks; even after the fixes it is the hardest entry passage and would benefit most from the proposed visual one-clock-against-a-line-of-clocks with a toggle for the crew's view.
- Prerequisite notes (invariance-of-the-speed-of-light, principle-of-relativity, relativity-of-simultaneity, proper-time, lorentz-factor) do not exist in v2, so recaps restate the facts used; glossaries and pictures should be aligned when they are written.
- Entry explanations are at 1,000 of 1,000 words and tutoring at 2,198 of 2,200; further additions need cuts elsewhere.
- If the builder script build_time_dilation.py is re-run, it will overwrite these review edits.

**Re-read** (2026-09-13, revision 4): 11 stumbles in 20 changed passages

- “How does the station team actually time a passing clock, and how can the crew find the station's clocks stretched too?”: Rule 17: the two-clock way asks a beginner to hold two new ideas at once, how a line of distant clocks is set and read, and why the crew find the station's clocks stretched with an 18-second head start. Its own question has two halves.
- “A telescope view is different. As a ship approaches, each later flash from it has less distance to travel, so its clock can even look faster than a clock beside you.”: A third new idea in the same way (received flash spacing), with a surprise whose reason needs its own picture; the way's question is not about telescopes.
- “The station team measures the same gap, since it lies across the motion, but a different path.”: Physics-review wording: two ideas in one sentence with a reason wedged in the middle, so 'measures ... a different path' has to be reread.
- “Long before the ship arrives, a flash leaves clock A”: Clock A is named before the reader is told it is one of the station's line of clocks.
- “The crew time station clock B, starting when the ship passes clock A, with a crew clock beside clock B at that moment by crew clocks.”: Three clauses and 'clock' five times; the reader rereads to find which clock is where, and 'by crew clocks' dangles.
- “So clock B counts 40 divided by 1.25, only 32 seconds.”: A step taken on trust: the reader must supply that 40 seconds pass on the crew's clocks and that clock B is the stretched one.
- “The head start is 6 tenths of 30 seconds, light's time to cross 9 million kilometres by station measurements.”: Physics-review addition squeezed into an appositive: the reader cannot tell at first whether 'by station measurements' belongs to the head start, the 30 seconds or the distance.
- “The stretch is tiny at everyday speeds”: Summary: 'the stretch' has not been named; the previous sentences speak of clocks counting more than one second.
- “How many times longer each tick of a clock takes, measured by synchronized clocks it moves past, than the clock's own count.”: Glossary, physics-review wording: the inserted 'measured by' clause separates 'longer' from 'than', so the comparison has to be reread.
- “so clock B was set 18 seconds ahead. So the crew compare clock B's count from 18 to 50, which is 32 seconds, with their own 40.”: Entry check answer: the 18 seconds is taken on trust and the 32 is derived from it, so the because-chain runs backwards and has a missing link.
- “Pythagoras gives the gap: 25 minus 16 is 9, so the gap is 3 metres. ... The ship covers 240,000 kilometres each second”: Entry problem solution: where 25 and 16 come from (squaring) is left implicit, and 240,000 kilometres per second is not linked to 8 tenths of light speed.
- Fix: Split the two-clock way. 'One travelling clock, two station clocks' (id kept) now answers only how the station times a passing clock: question shortened to its first half, recap drops the no-speed-inside fact and the term time dilation (neither is used in that way any more), new takeaway, simplifies set to null, assumes emptied, refs checks/side-by-side-readings.
- Fix: Added entry way crew-time-a-station-clock ('The crew time a station clock', operational, continues one-ship-clock-two-station-clocks): the reciprocity, 32-second count and head-start paragraphs moved verbatim apart from the stumble rewrites; its first sentence names the timing it turns around; it carries the original takeaway and simplifies (both stretches hold only while both sides coast steadily), a recap restating light speed, the no-speed-inside fact, how the line is synchronized with a flash from clock A, and the 40 and 50 second readings; assumes principle-of-relativity and relativity-of-simultaneity; refs checks/each-side-finds-the-other-stretched; visual one-clock-against-a-line-of-clocks.
- Fix: Links updated for the split: formal way dilation-as-a-dot-product continues crew-time-a-station-clock and names 'When the crew time a station clock' for the 18-second head start; teaching arc turn-the-timing-around and if-stuck wants-the-real-slow-clock use the new way.
- Fix: Moved the telescope aside out of the entry two-clock way; the working way seen-ticks-versus-measured-ticks already states it with its reason, and the entry misconception just-light-delay stays diagnosed by side-by-side-readings.
- Fix: Rewrote the light-clock gap sentence, the clock A introduction, the crew-clock sentence, the 32-second step and the head-start sentence; summary 'The stretch' to 'This stretch'; Lorentz factor glossary definition; each-side check answer chain; half-hour problem solution steps. No number, condition, sign or scope changed.
- Fix: Budget offsets, to hold entry explanations (1,000), other way fields (650) and tutoring (2,200): dropped the sentence 'So each side times one of the other side's clocks with two of its own.' from the new way's last paragraph (it repeats the takeaway); dropped the opening question why-nobody-notices (the light-clock way's last paragraph answers it with the 80-year airliner number); set the formal way's simplifies to null (its explanation already states inertial observers and the clock hypothesis). No entry sentence or check answer was compressed.
- Fix: Bumped the revision from 3 to 4; status kept at physics-reviewed; a physics diff check of these changes should follow.

**Re-read** (2026-09-13, revision 7): 2 stumbles in 3 changed passages

- “Clock B, stretched 1.25 times, counts only 32 of them, so at the start, by crew clocks, it read 50 minus 32, or 18.”: Step taken on trust: the answer never says that 50 is clock B's reading when the ship arrives, so the reader must go back to the way to see why 32 is taken from 50. 'At the start' also leaves the reader to work out which moment is meant.
- “Both ratios are 1.25.”: 'Both ratios' asks the reader to rebuild which two numbers are divided; the crew's 40 and 32 were never shown as a ratio.
- Fix: checks/each-side-finds-the-other-stretched answer: split the head-start sentence, stated that clock B reads 50 on arrival (as the way crew-time-a-station-clock says), named the start as the moment the ship passed clock A, and named the two ratios. No number, measurer, sign or scope changed.
- Fix: Removed if-stuck move cannot-see-the-slant: no learner-visible text to read; the light-clock way's slant paragraph, its try-it and the flagship visual still cover that stumble, so no stumble recorded.
- Fix: Tutoring words rise by about 16 over the 2,200 cap, inside the 10% review allowance, only for these recorded fixes. Revision bumped from 6 to 7; status kept at physics-reviewed; a physics diff check of the check answer should follow.

## Review: physics

**Verdict:** fixed (2026-09-13, revision 7)

**Verification**

- Light-clock derivation: (c dt/2)^2 = L^2 + (v dt/2)^2 gives dt = gamma dtau with gamma = (1 - v^2/c^2)^(-1/2); interval check -c^2 dt^2 + v^2 dt^2 = -c^2 dtau^2.: Re-derived each step by hand in signature (-,+,+,+); checked the crosswise-length (hoops) argument and positive-root choice. → Correct.
- Small-speed lag dt - dtau = (1 - 1/gamma) dt ~ (v^2/2c^2) dt, relative corrections O(v^4/c^4).: Binomial expansion of sqrt(1 - beta^2). → Correct.
- gamma values 1.005 (0.1c), 1.155 (0.5c), 1.25 (0.6c), 5/3 (0.8c), 7.09 (0.99c); entry 'slant about 7 times the gap' at 0.99c.: python3. → 1.00504, 1.15470, 1.25, 1.66667, 7.0888. Correct.
- Entry 3-4-5 triangle at 0.6c, half-light-speed check (gap 1.732 m, stretch 1.155), 0.8c problem (3-4-5 with ship 4, 50 min, 720 million km), station check 25 min.: python3 and hand arithmetic. → All correct.
- Jet airliner 900 km/h over 80 years lags by less than a thousandth of a second (working: 3.5e-13, 0.88 ms).: python3 with 250 m/s and Julian years. → v^2/2c^2 = 3.48e-13; 0.878 ms. Correct.
- Two-clock timing: 9 million km at 180,000 km/s takes 50 s; ship clock 40 s; crew find clock B counting 32 s and reading 18 at the start.: python3 plus an explicit Lorentz transformation (t' = gamma(t - v x/c^2)) of the events 'ship passes A' and 'ship passes B'. → Arrival at t' = 40 s; on the crew slice t' = 0, clock B reads v D/c^2 = 18 s ahead of zero (B lies ahead of the ship's motion). 50 - 32 = 18. Correct.
- Novice rewrite: head start = 6 tenths of the 30 s light takes to cross 9 million km, and 'clock B moved toward the flash that set it, so it was set ahead'.: Compared with v D/c^2 and checked the sign of the synchronization offset in the crew frame. → Rule and sign correct, but only with D and D/c measured by the station (crew-measured distance 7.2 million km would give 14.4 s). Fixed by adding 'by station measurements'. The flash argument is a correct qualitative reason for the sign.
- Novice rewrite: round trip returns less time on the ship clock because 'only the station coasted steadily the whole time'.: Twin check: 4 ly at 0.8c gives 10 yr station, 6 yr ship; reverse triangle inequality in the formal problem (legs 3 yr at +-0.8c, gamma_12 = 41/9, tau = 10 yr). → Correct as the reason the symmetry breaks in flat spacetime; the station's inertial world line maximizes proper time. It is not claimed that acceleration itself causes the lag.
- Received spacing gamma(1 +- v/c) dtau = sqrt((1 +- v/c)/(1 -+ v/c)) dtau; 2.0 s and 0.5 s at 0.6c; round-trip average (2 + 0.5)/2 = 1.25; closest-approach emission gives gamma dtau.: Hand derivation and python3. → Correct, including sign convention (upper receding) and the closest-approach case (emission at closest point in the watcher frame).
- Formal: t_n(p) = -eta(n, p - o), dt_n = -eta(n,u) dtau, u = gamma(n + V), gamma = cosh phi, reversed Cauchy-Schwarz with equality iff u = n, reciprocity eta(n,u) = eta(u,n).: Hand derivation with n = e_0; normalization -1 = gamma^2(-1 + v^2). → Correct.
- Formal: the 18 s head start is the proper time along clock B between the slices t_n = 0 and t_u = 0 through the event 'ship passes A'.: Lorentz transformation of clock B's world line. → Correct: B is at rest in the station frame, so its proper time equals t_n, and t_u = 0 meets it at t_n = 18 s.
- Reversed Cauchy-Schwarz problem solution and numeric check.: Hand algebra and python3. → a^2 = 1 + eta(w,w) >= 1; tau_pr^2 = tau1^2 + tau2^2 + 2 tau1 tau2 gamma12 > (tau1 + tau2)^2; 41/9 and 10 yr. Correct.
- Storage-ring muons: 29.33 x 2.197 = 64.44 microseconds, v/c = 0.99942, 19.3 km, about 440 laps in a 14 m ring; about 660 m and 15 laps without the stretch; proper acceleration near 1e18 g.: python3 with proper acceleration gamma^2 v^2/r. → 64.44 microseconds, 0.999419, 19.31 km, 439 laps, 658 m, 15.0 laps, 1.1e18 g. Correct.
- Observation numbers: tau+ = 64.419(58) microseconds at gamma = 29.33, dilation factor confirmed to 2e-3 at 95% confidence.: Checked the abstract of the Nature paper (ADS and nature.com record). → Matches the abstract. 64.419/2.197 = 29.32. Correct.
- Aluminium-ion clocks: 75 m fibre, rms speeds from a few m/s to about 36 m/s, shifts -5.6e-16 at 10 m/s and -7.2e-15 at 36 m/s; 33 cm height gives gh/c^2 = 3.6e-17.: Read the published paper (Fig. 2, Eq. 1-2, text); python3 for v^2/2c^2 and gh/c^2. → Fig. 2 spans about 3 to 36 m/s rms; fibre 75 m; motion from displacement off the RF null (micromotion); 5.56e-16, 7.21e-15; gh/c^2 = 3.60e-17, measured (4.1 +- 1.6)e-17. Correct.
- GPS: v = 3.87 km/s gives 8.33e-11, 7.2 microseconds/day, 2.16 km of light travel; height term 5.29e-10, 45.7 microseconds/day, net gain 38.5 for a spherical non-rotating Earth.: python3 with GM = 3.986e14, R = 6371 km, r = 26,560 km. → 8.33e-11, 7.20 microseconds, 2.16 km, 5.29e-10, 45.7, 38.5; ratio 6.35 ('about six times'). Correct with the stated scope.
- ISS common question: a little under five thousandths of a second per six months, net of the height effect.: python3: v = 7.66 km/s, h = 420 km, ground clock rotation at 40 degrees latitude. → Net fraction 2.83e-10, 4.46 ms per six months (motion alone 5.15 ms). Correct.
- Analogy roads crossing: projection gives cos(theta) times the odometer, mapped to gamma = cosh(phi).: Compared Euclidean projection with Minkowski slicing, with signs. → Magnitude map correct, but in the Euclidean case the other car's odometer reads more than one's own coordinate, while a moving clock reads less: the inequality reverses. Limits said 'only the symmetry survives'; rewritten to state the reversal.
- Reference: Bailey, Borer, Combley, Drumm et al. (12 authors), 1977, Nature 268, 301-305, doi 10.1038/268301a0.: WebSearch: nature.com, ADS, PhilPapers author list. → Confirmed; verified set true.
- Reference: Chou, Hume, Rosenband, Wineland, 2010, Optical Clocks and Relativity, Science 329, 1630-1633, doi 10.1126/science.1192720.: WebSearch (PubMed, science.org) and the published PDF. → Confirmed, four authors; verified set true.
- Reference: Ives and Stilwell 1938, An Experimental Study of the Rate of a Moving Atomic Clock, JOSA 28, 215-226, doi 10.1364/JOSA.28.000215; contribution scope.: WebSearch and the Optica record. → Confirmed. Emitters were excited hydrogen atoms formed from H2+ and H3+ canal-ray ions, and Ives interpreted the result in an ether framework; contribution reworded. Verified set true.
- Reference: Einstein 1905, Zur Elektrodynamik bewegter Koerper, Annalen der Physik 17 (322), 891-921, doi 10.1002/andp.19053221004; contribution scope.: WebSearch: Wiley record and ADS. → Confirmed; continuous volume 322 added. Contribution makes no priority claim (earlier Larmor and Lorentz results exist), so it is correctly scoped. Verified set true.
- Prerequisites direct and acyclic; assumes consistent with needed_for.: Python walk of the registry prerequisite graph for all six prerequisites. → No prerequisite has time-dilation as an ancestor; each assumes id is a prerequisite at or below its way's rung. Registry lists only proper-time and lorentz-factor (sync pending).

**Counterexamples tried**

- Non-relativistic limit: gamma -> 1 + v^2/2c^2 and zero stretch at v = 0; the entry 'almost exactly 1' and the 80-year jet number survive.
- Massless case: no clock rides with light; the note only says the factor has no upper limit 'as the speed nears light's' and never assigns a factor at light speed. Survives.
- Non-inertial timer ('you' on a rotating platform, where light-based synchronization around a loop fails): broke the summary, which did not say you coast or that your clocks allow for light's travel time. Fixed.
- Unsynchronized station clocks: any stretch could be manufactured by mis-set clocks; broke the glossary definitions of time dilation and Lorentz factor. Fixed with 'synchronized'.
- Different slicing (crew frame): the head-start rule gives 14.4 s instead of 18 s if the crew-measured distance 7.2 million km is used. Scoped to station measurements.
- Non-inertial clock (turnaround): mutual stretch fails and the ship returns younger; the note scopes the mutual stretch to steady coasting, and the station's one-way stretch still holds per the clock hypothesis. Survives.
- Extreme acceleration (muons near 1e18 g): the factor still equals gamma of the instantaneous speed; supports the clock hypothesis statement. Survives.
- Approaching clock through a telescope: looks faster by gamma(1 - v/c) < 1 for every v > 0, so 'can even look faster' is true. Survives.
- Transverse view: reception, not emission, at closest approach gives a blueshift 1/gamma; the note specifies emission at the nearest point by the station's measurements. Survives.
- Strong field / curved spacetime: clocks 33 cm apart at rest differ by gh/c^2 with zero relative speed; the formal way and check exclude gamma for distant clocks. Survives.
- Euclidean analogy with signs: the inequality reverses (odometer exceeds coordinate, clock falls behind). The limits sentence understated this. Fixed.
- Takeaway causal chain: invariance of light speed is not what makes the path slanted (ship motion does); it is what turns the longer path into a longer time. Reordered.

**Fixes**

- Summary: added 'while you coast steadily' and that the timing clocks are synchronized, within the 450-character cap.
- Light-clock way: states that the station measures the same 4-metre gap because it lies across the motion (the entry triangle silently used this); trimmed 'because every clock and heartbeat on board keeps step' (already given by the previous sentence) and 'less than' to 'under' to hold the entry budget; takeaway reordered so light-speed invariance explains the longer time, not the slant.
- Two-clock way: head-start rule now says the 30 s and 9 million km are station measurements; 'like markers along a road' shortened to 'like road markers'.
- Formal way: curved-spacetime limit now says there is no global inertial frame, so a synchronized time function like t_n holds only approximately.
- Glossary: time dilation and Lorentz factor definitions now say 'synchronized clocks'.
- Analogy limits: states that the minus sign reverses the inequality while the mutual symmetry survives.
- Budget offsets: shortened the reciprocity misconception correction, the round-trip check answer, and 'each pair of clocks' to 'each pair' in the two-clock way, without changing content.
- History: Ives-Stilwell contribution now names the emitters correctly (fast hydrogen atoms from accelerated ions) and notes Ives's ether reading; leads_to reason matched; Einstein venue gains the continuous volume 322.
- All four references verified and marked verified: true.

**Concerns**

- Course conventions have no row for the Lorentz factor gamma, beta = v/c, or proper time tau; the note's notation trap course_choice relies on them. A conventions row should be added.
- Physics fixes change learner-visible entry text (summary, light-clock gap sentence and takeaway, head-start sentence, glossary). Revision kept at 2 as in the exemplar; an editor may prefer a bump and a quick novice re-read of those sentences.
- Entry explanations remain at the 1,000-word cap and tutoring near its 2,200 cap; further additions need cuts.
- Registry prerequisites list only proper-time and lorentz-factor; the note's extra direct prerequisites are acyclic and should be synced with sync_registry.py. The registry id ives-stillwell-experiment misspells Stilwell; ids are permanent, but its title should use the correct spelling.
- The 'set ahead' reason in the two-clock way is qualitative: it fixes the sign of the head start, while the count 6 tenths of 30 s is given as a rule. A visual toggle for the crew's slice would help.
- The two proposed visuals are still missing from the catalog; the builder script build_time_dilation.py is stale and must not be re-run.

**Diff check** (2026-09-13, revision 5)

- Formal check head-start-from-level-sets: on B's world line o + D e + s n, t_u = gamma(s - vD) vanishes at s = vD = 18 s; the ship meets B at s = D/v = 50 s, where t_u = 1.25 x 32 = 40 s, the ship's proper time; both ratios are 1.25.: Hand derivation with eta(u,n) = -gamma, eta(u,e) = gamma v in signature (-,+,+,+); python3 with explicit components n = (1,0), e = (0,1), u = gamma(1, v). → s0 = 18.0, t_u(B(50)) = 40.0 = 50/gamma, B counts 32, ratio 1.25. Numeric fields 18 s and 40 s, magnitude, rel_tol 0.01 correct. Sign correct: B lies ahead along e, so it reads ahead on the ship's slice. Error: the question never fixed the zero of the station clocks, so 'B's reading' was undetermined (any station time origin shifts it); the answer assumed t_n(p) = -eta(n, p - o). Fixed.
- Formal objective locate-reciprocity-on-slices and misconception both-cannot-be-stretched diagnosed_by the new check.: Read against the check and the formal way's reciprocity paragraph. → Consistent: the check computes where the ship's slice meets clock B and shows the two gammas relate different event pairs; targets and diagnosed_by agree.
- Entry way crew-time-a-station-clock: station slides toward the ship's rear at 0.6c by crew measurement; crew line of synchronized clocks finds each station tick 1.25 times as long; one crew clock beside B at the start by crew clocks; B reaches the ship when the ship's clock reads 40; 40 / 1.25 = 32; 50 - 32 = 18.: Lorentz transformation t' = gamma(t - v x / c^2) of the events 'ship passes A' (0,0) and 'ship meets B' (50 s, 9 million km); python3. → t' = 40 s at the meeting; on the crew slice t' = 0 through 'ship passes A', B's reading is v D / c^2 = 18 s; B counts 32 s. Correct, and every duration names its measurer.
- Re-read split of the head-start sentence: 'By station measurements, light takes 30 seconds to cross the 9 million kilometres from clock A to clock B. The head start is 6 tenths of those 30 seconds.': Compared with the physics-review wording and with v D / c^2, D measured by the station. → Same claim as before; the station scope now attaches to the 30 s and the distance, which is what makes 0.6 x 30 = 18 true (the crew-measured 7.2 million km would give 14.4 s). 9e6 / 3e5 = 30. Correct.
- 'Measured by the crew, ... clock B moved toward the flash from clock A that set it, so clock B was set ahead' (way and entry check).: Direction check in the crew frame: the flash runs from A toward B along the ship's motion while the station moves toward the ship's rear. → B moves toward the flash, the flash arrives early by crew clocks, and B, set to A's reading plus 30 s, is ahead on the crew slice. Sign correct.
- Entry check each-side-finds-the-other-stretched, reworded chain: by crew clocks the ship takes 40 s to reach B; B, stretched 1.25 times, counts 32 of them; so it read 50 - 32 = 18 at the start.: Worked forward from the crew's 40 s, as the new chain does; checked the measurer of 'at the start'. → Correct. The chain now derives 18 instead of assuming it. 'At the start' is scoped by the preceding 'By crew clocks' and the opening 'Measured by the crew'; by station clocks B read 0 then, which the answer does not contradict.
- Recap and takeaway of crew-time-a-station-clock, the simplifies moved from one-ship-clock-two-station-clocks, and assumes principle-of-relativity and relativity-of-simultaneity.: Read against the explanation; round-trip scope checked with the round-trip-reunion numbers (10 yr station, 6 yr ship). → Unchanged claims, moved verbatim; the mutual stretch stays scoped to steady coasting in the explanation itself, so the entry prose is true without simplifies. Both assumes ids are entry prerequisites.
- One-ship-clock-two-station-clocks after the split: new question and takeaway ('two synchronized station clocks, each read side by side with it'), recap without the no-speed-inside fact and the term time dilation, telescope aside removed, refs side-by-side-readings, assumes emptied, simplifies null.: Checked each remaining sentence for a dependence on the removed material, and the removed telescope claim against the working way seen-ticks-versus-measured-ticks (gamma(1 - v/c) = 0.5 at 0.6c). → Correct. The way no longer uses simultaneity of distant events beyond the synchronization it describes, and the telescope claim survives with its reason at the working rung.
- Light-clock gap sentence split: 'The station team measures the same 4-metre gap, because the gap lies across the ship's motion. But they measure a different path for the flash.': Compared with the previous wording. → Same claim (transverse lengths agree). Correct.
- Glossary Lorentz factor: 'How many times as long each tick of a clock lasts by synchronized clocks it moves past, compared with the clock's own count.' Summary 'This stretch'.: Compared with the previous wording; first what-if at v = 0 gives 1. → Equivalent claims. Correct.
- Problem half-hour-at-eight-tenths solution steps: gap squared = 5 x 5 - 4 x 4 = 9, gap 3 m; 8 tenths of 300,000 km = 240,000 km per second; 240,000 x 3,000 = 720 million km.: python3. → 9, 240,000, 7.2e8. Correct.
- Formal way dilation-as-a-dot-product: head-start sentence now opens 'When the crew time a station clock'; continues crew-time-a-station-clock; simplifies removed.: Read against the explanation, which states inertial observers and the clock hypothesis. → Same claim; no hypothesis lost.
- Removed items: analogy roads-crossing-at-an-angle, notation trap letter-for-the-factor, common question would-i-live-longer, opening question why-nobody-notices; teaching arc and if-stuck uses repointed.: grep for dangling addresses across concepts and visuals; checked that the conventions row for gamma and tau is still honoured without the trap. → No dangling references; all uses resolve. Removal introduces no false statement.
- Fix: checks/head-start-from-level-sets question: added 'Station clocks read $t_n(p) = -\eta(n, p - o)$, and' so clock B's reading is defined; question_spoken gained 'Station clocks read zero on the station's slice through o, and' and 'along the ship's path' (was 'along its path', where 'its' could mean B's).
- Fix: Budget offset for tutoring (2,217 to 2,189 of 2,200): dropped the if-stuck move cannot-see-the-slant, whose drawing repeats the light-clock way's slant paragraph, its try-it and the flagship visual's split view.
- Fix: Revision bumped from 4 to 5; review.physics.reviewed_revision set to 5; the novice stage now lags by one revision, only for the formal check question (graduate rung) and the removed if-stuck move.

**Diff check** (2026-09-13, revision 7)

- Entry check each-side-finds-the-other-stretched, new sentence 'Clock B, stretched 1.25 times, counts only 32 of them.': Read with the preceding 'By crew clocks the ship takes 40 seconds to reach clock B'; python3 with gamma = 1.25 at 0.6c. → 40 / 1.25 = 32. 'Them' refers to the crew's 40 seconds, the only candidate. Same claim as the first half of the old sentence. Correct.
- New sentence 'Clock B reads 50 on arrival, so when the ship passed clock A, by crew clocks, clock B read 50 minus 32, or 18.': Lorentz transformation t' = gamma(t - v x/c^2) with ship passes A at (0, 0) and ship meets B at (50 s, 9 million km); python3. Checked that 50 is B's own side-by-side reading (way one-ship-clock-two-station-clocks) and that 'when the ship passed clock A, by crew clocks' names the crew slice t' = 0 through that event. → The meeting is at t' = 40 s; the crew slice t' = 0 meets B at station time v D/c^2 = 18 s, and B counts 50 - 18 = 32 s up to the meeting. The event 'B reads 18' has t' = 0.0. The measurer is attached to the simultaneity, which is where it is needed; by station clocks B read 0 then, which the sentence does not contradict. Same claim as the old 'at the start', now with the moment named. Correct.
- New sentence 'The station's 50 divided by 40 and the crew's 40 divided by 32 both equal 1.25.' (was 'Both ratios are 1.25.'): python3; checked each ratio is 'measuring team's elapsed time over the other side's clock count'. → 50/40 = 1.25 (station time over ship clock count), 40/32 = 1.25 (crew time over clock B's count); the two ratios compare different event pairs, consistent with the formal check head-start-from-level-sets. Correct.
- First what-ifs on the chain: slower and faster ships.: python3 at 0.1c and 0.8c over the same 9 million km, repeating the chain (station time, ship count, head start v D/c^2, B count, both ratios). → 0.1c: 300 s, 298.50 s, head start 3 s, B counts 297 s, both ratios 1.00504. 0.8c: 37.5 s, 22.5 s, head start 24 s, B counts 13.5 s, both ratios 5/3. The reasoning holds at every speed; the answer's numbers are stated only for 0.6c. No change needed.
- Consistency with the rest of the note.: Compared with ways_in/crew-time-a-station-clock, key_points, hints, targets, and misconception both-cannot-be-stretched. → Same numbers, sign (B set ahead) and measurers as the way; key_points and targets unchanged and still met.
- Fix: None. The re-read's rewording of the check answer claims exactly what the revision-6 wording did, with the moment and the two ratios named. No learner-visible text changed, so the revision stays at 7 and no novice sign-off is needed.
