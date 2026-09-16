---
type: "visual"
schema_version: 2
id: "falling-ring-of-crumbs"
title: "Falling ring of crumbs"
kind: "interactive-3d"
priority: "flagship"
status: "proposed"
revision: 2
rungs: ["entry", "working", "formal"]
serves: ["relativistic-tidal-tensor", "volume-preserving-tidal-deformation", "ricci-tensor", "weyl-tensor", "weyl-tensor-field-equation", "ricci-flat-spacetime", "einstein-space", "einstein-tensor", "geodesic-deviation-equation", "newtonian-deviation-equation", "deviation-vector", "riemann-curvature-tensor", "riemann-curvature-operator", "ricci-identity", "riemann-tensor-in-normal-coordinates", "symmetries-of-the-riemann-tensor", "number-of-independent-riemann-components", "bianchi-identity", "flatness-criterion", "integrability-condition-for-parallel-fields", "curvature", "curvature-sign-conventions", "sectional-curvature", "kretschmann-scalar", "weyl-criterion-for-conformal-flatness"]
builds_on: ["two-walkers-set-off-side-by-side", "carry-an-arrow-around-a-loop"]
leads_to: ["six-entry-curvature-table", "cube-of-small-loops", "three-gauges-on-a-falling-probe"]
---

# Falling ring of crumbs

`falling-ring-of-crumbs` · interactive-3d · flagship · proposed · rungs: entry, working, formal

> Let go of a ring of crumbs in a cabin falling near a planet. The ring becomes an oval, and a meter shows that the room the ring takes up has not changed.

## What it makes visible

Crumbs let go at rest in a freely falling cabin drift, even though scales in the cabin read zero. Beside a planet the ball of crumbs becomes an egg that keeps its room; inside matter it shrinks. Splitting the drift into a part that is the same in every direction and a balanced leftover separates the Ricci reading from the Weyl reading, and the whole of curvature that a single falling observer can reach: the tidal matrix, its trace, its trace-free part, its gradients, its sign conventions and its invariants.

## The picture

A cutaway cabin falls freely beside a shaded planet, with a marked line drawn from the cabin to the planet's centre. Inside the cabin sit crumbs: a clock-face ring, a small ball, or a single pair, always around one centre crumb. Magnified drift arrows leave each crumb, and a translucent ghost of the starting shape stays in place for comparison. A panel carries the three principal drifts, their total, a room meter, and a switch that splits each drift arrow into a same-in-every-direction part and a balanced leftover. A pair of scales in the corner of the cabin always reads zero.

| Element | Shows |
| --- | --- |
| Cabin falling freely, drawn in cutaway | an observer in free fall, with no floor and no rope |
| Marked line from the cabin to the planet's centre | the reference direction that every drift is named against |
| Centre crumb with a clock-face ring, a small ball, or one pair of crumbs | neighbouring free particles whose separations are the deviation vectors |
| Magnified drift arrows and a ghost of the starting shape | the relative acceleration that free fall cannot remove |
| Room meter beside the shape | the volume, whose change is the trace of the tidal matrix |
| Two-part arrow display: uniform in-or-out arrows and balanced stretch-and-squeeze arrows | the Ricci part and the Weyl part of the drift, never drawn added together |
| Scales in the cabin corner reading zero | that one object on its own cannot detect the curving |
| Three-by-three table of drifts with mirror pairs lit together | the symmetry of the tidal matrix and its six independent numbers |

## Book figure

Three panels sharing one cabin. Left: a cabin beside a planet, the ring of crumbs drawn as a dashed starting circle and a solid returned oval, stretched along the marked line and squeezed across it, with a room meter reading unchanged. Middle: the same cabin inside a uniform planet, where the solid shape is a smaller circle and the room meter has dropped. Right: a cabin far from every mass, where the solid shape lies exactly on the dashed one.

Labels: marked line to the planet's centre, centre crumb, starting ring, drift after ten seconds, room meter, inside matter, far from every mass. Aspect 3:1. Alt text: In a cabin falling beside a planet a ring of crumbs becomes an oval of the same area; inside a uniform planet the ring shrinks; far from every mass it does not change.

## Variants

- **static** `static-card` (fallback): The three-panel print figure as an SVG card, used when 3D is unavailable and as a summary card.
- **interactive-2d** `ring-2d`: A flat slice through the cabin holding the clock-face ring, with the drift arrows, the three readings and the room meter, for small screens.
- **interactive-3d** `full-3d`: The full cabin with every scene, the ball and pair modes, the drift split, the tide table, the gradiometer grid and the scrubbable clock.

## Parameters

| Id | Label | Type | Options or range | Default | Available when | Effect |
| --- | --- | --- | --- | --- | --- | --- |
| `scene` | Where the cabin is | enum | planet-exterior, inside-uniform-planet, falling-dust-cloud, rocket, far-from-everything, dust-universe, dark-energy-universe, plane-wave | "planet-exterior" | — | Chooses the tidal matrix the cabin reads, and what the marked line means: the line to the body's centre, the line the cabin moves along, or the wave's stretch line. |
| `body` | Round body | enum | earth, neutron-star, black-hole | "earth" | scene in planet-exterior, inside-uniform-planet | Sets $GM$: Earth $3.986004418\times10^{14}$, the neutron star $1.4\,GM_\odot$, the black hole $10\,GM_\odot$ with $GM_\odot = 1.32712440018\times10^{20}\ \mathrm{m^3\,s^{-2}}$. |
| `distance` | Distance from the body's centre | number | 1–1000000 step 0.01 km | 6371 | scene in planet-exterior | Moves the cabin along the marked line. The tidal strength $GM/r^3$ falls as the inverse cube. |
| `density` | Density of the matter around the cabin | number | 0–20000 step 10 kg/m^3 | 5500 | scene in inside-uniform-planet, falling-dust-cloud, dust-universe | Sets the matter the crumbs sit among; it fixes the tidal trace through $4\pi G\rho$. |
| `dark-energy-density` | Dark-energy density | number | 0–20000 step 10 kg/m^3 | 1000 | scene in dark-energy-universe | An energy density with pressure $-\rho c^2$, so the tidal trace is $-8\pi G\rho_\Lambda$ and the ball grows in every direction. |
| `depth-in-cloud-radii` | Where the cabin sits in the dust cloud | number | 0–6 step 0.01 1 | 0.5 | scene in falling-dust-cloud | Distance from the cloud's centre in cloud radii. Under 1 the cabin sits among the dust; over 1 it is outside, where the tidal matrix is that of a point mass. |
| `strain` | Wave strain | number | 0–0.5 step 0.001 1 | 0.1 | scene in plane-wave | Peak plus-polarization strain of a wave crossing the cabin. Real strains are far smaller; this one is exaggerated so the shape change is visible. |
| `cabin-motion` | How the cabin moves | enum | falling-from-rest (scene in planet-exterior), moving-sideways (scene in planet-exterior), moving-radially (scene in planet-exterior), at-rest-in-the-dust (scene in dust-universe), moving-through-the-dust (scene in dust-universe) | "falling-from-rest" | scene in planet-exterior, dust-universe | Chooses the four-velocity fed to the Riemann tensor. Sideways motion past a body strengthens the tides across the motion; motion along the marked line changes nothing. |
| `cabin-speed` | Cabin speed as a fraction of the speed of light | number | 0–0.9 step 0.01 1 | 0 | cabin-motion in moving-sideways, moving-radially, moving-through-the-dust | Sets $\beta$, and so $\gamma^2 = 1/(1-\beta^2)$ in the passing observer's tidal matrix. |
| `mode` | What is let go | enum | small-ball, clock-face-ring, two-crumbs | "small-ball" | — | Chooses the arrangement of crumbs around the centre crumb. The readouts are the same in every mode; only the drawing changes. |
| `ring-orientation` | How the ring is set | enum | along-the-line, across-the-line | "along-the-line" | mode in clock-face-ring | Turns the clock-face ring in the cabin. |
| `probe-direction` | Direction of the probe crumb | enum | along-the-line, across-the-line, slanted | "along-the-line" | — | Places the pair of crumbs, and picks the plane whose curvature the plane readout reports. |
| `ball-radius` | Distance of the outer crumbs from the centre crumb | number | 0.1–1000 step 0.1 m | 1 | — | Scales every drift in direct proportion, because the deviation equation is linear in the separation. |
| `clock` | How long the crumbs fall | enum | one-nanosecond, one-microsecond, one-millisecond, one-second, five-seconds, ten-seconds, one-minute, ten-minutes | "ten-seconds" | — | Sets the proper time the clock runs to. Progress 1 means the whole of it. |
| `progress` | Clock progress | progress | 0–1 step 0.01 | 0 | — | Runs the cabin clock from the moment of release to the end of the chosen time. |
| `split-the-drift` | Split each drift in two | boolean | — | false | — | Draws each drift arrow as a same-in-every-direction part and a balanced leftover, and shows the two matching readouts. |
| `tide-table` | Show the three-by-three table of drifts | boolean | — | false | — | Shows the nine readings of a three-arm tide meter, with mirror pairs lit together and a counter of how many different numbers they hold. |
| `whirlpool-table` | Try an invented whirlpool table | boolean | — | false | tide-table in True | Adds an antisymmetric piece of size $GM/r^3$ to the table, which no metric connection allows, so that the ring gains a net forward drift. |
| `gradiometer-grid` | Read the table on a grid of places | boolean | — | false | scene in planet-exterior | Repeats the reading at neighbouring places and reports how one entry changes moving out along the marked line and how another changes moving across it. |
| `show-plane-curvature` | Show the curvature of the chosen plane | boolean | — | false | — | Reports the sectional curvature of the plane spanned by the cabin's four-velocity and the probe direction, as a signed curvature length. |
| `convention` | Another writer's sign conventions | enum | course, flipped-riemann, flipped-signature, flipped-both | "course" | — | Changes only the printed curvature components. The crumbs and every drift reading stay exactly as they are. |
| `shear-at-release` | Let the crumbs go already spreading one way and closing the other | boolean | — | false | — | Gives the crumbs a trace-free spread of starting speeds, which removes room from the very first moment even in vacuum. |
| `magnify` | Arrow magnification | number | 1–1000000 step 1 1 | 1000 | — | Scales the drawn drift arrows only. Every readout is the true value, and the factor is printed beside the cabin. |

## Presets

- `earth-surface-ball` A ball of crumbs beside Earth: scene="planet-exterior", body="earth", distance=6371, mode="small-ball", ball-radius=1, clock="ten-seconds"
- `earth-surface-ring` A clock-face ring beside Earth: scene="planet-exterior", body="earth", distance=6371, mode="clock-face-ring", ring-orientation="along-the-line", ball-radius=1, clock="ten-seconds"
- `earth-orbit-gradiometer` A gradiometer 400 kilometres up: scene="planet-exterior", body="earth", distance=6771, mode="small-ball", ball-radius=1, clock="ten-seconds", gradiometer-grid=true
- `two-crumbs-across` Two crumbs side by side: scene="planet-exterior", body="earth", distance=6371, mode="two-crumbs", probe-direction="across-the-line", ball-radius=1, clock="ten-seconds"
- `two-crumbs-along` Two crumbs one under the other: scene="planet-exterior", body="earth", distance=6371, mode="two-crumbs", probe-direction="along-the-line", ball-radius=1, clock="ten-seconds"
- `slanted-crumb` One crumb on a slant: scene="planet-exterior", body="earth", distance=6371, mode="two-crumbs", probe-direction="slanted", ball-radius=1, clock="ten-seconds"
- `inside-a-rock-planet` Inside a planet of rock: scene="inside-uniform-planet", body="earth", density=5500, mode="small-ball", ball-radius=1, clock="ten-seconds"
- `dust-as-dense-as-water` A universe of dust as dense as water: scene="dust-universe", density=1000, mode="small-ball", ball-radius=1, clock="one-second"
- `moving-through-the-dust` Racing through the dust universe: scene="dust-universe", density=1000, cabin-motion="moving-through-the-dust", cabin-speed=0.6, mode="small-ball", ball-radius=1, clock="one-second"
- `dark-energy-universe` A universe holding only dark energy: scene="dark-energy-universe", dark-energy-density=1000, mode="small-ball", ball-radius=1, clock="one-second"
- `far-from-every-mass` Far from every mass, engines off: scene="far-from-everything", mode="small-ball", ball-radius=1, clock="ten-seconds"
- `rocket-cabin` A rocket speeding up: scene="rocket", mode="two-crumbs", probe-direction="across-the-line", ball-radius=1, clock="ten-seconds"
- `neutron-star-flyby` Passing a neutron star: scene="planet-exterior", body="neutron-star", distance=1200, mode="small-ball", ball-radius=1, clock="one-millisecond"
- `black-hole-horizon` Crossing a black hole's horizon: scene="planet-exterior", body="black-hole", distance=29.54, mode="small-ball", ball-radius=1, clock="one-microsecond"
- `passing-sideways` Racing sideways past Earth: scene="planet-exterior", body="earth", distance=6371, cabin-motion="moving-sideways", cabin-speed=0.6, mode="small-ball", ball-radius=1, clock="ten-seconds"
- `gravitational-wave` A gravitational wave crossing the cabin: scene="plane-wave", strain=0.1, mode="clock-face-ring", ring-orientation="across-the-line", ball-radius=1, clock="one-second"
- `dust-cloud-inside` Among the dust of a falling cloud: scene="falling-dust-cloud", density=5500, depth-in-cloud-radii=0.5, mode="small-ball", ball-radius=1, clock="ten-seconds"
- `dust-cloud-outside` Two cloud radii out from the falling cloud: scene="falling-dust-cloud", density=5500, depth-in-cloud-radii=2, mode="small-ball", ball-radius=1, clock="ten-seconds"
- `split-the-drift-beside-earth` The drift split in two, beside Earth: scene="planet-exterior", body="earth", distance=6371, mode="small-ball", ball-radius=1, clock="ten-seconds", split-the-drift=true
- `split-the-drift-in-dust` The drift split in two, among dust: scene="dust-universe", density=1000, mode="small-ball", ball-radius=1, clock="one-second", split-the-drift=true
- `tide-table-beside-earth` The tide meter's nine readings: scene="planet-exterior", body="earth", distance=6371, mode="clock-face-ring", ring-orientation="along-the-line", ball-radius=1, clock="ten-seconds", tide-table=true
- `whirlpool-table-beside-earth` An invented whirlpool table: scene="planet-exterior", body="earth", distance=6371, mode="clock-face-ring", ring-orientation="along-the-line", ball-radius=1, clock="ten-seconds", tide-table=true, whirlpool-table=true
- `flipped-riemann-sign` A writer with the opposite Riemann sign: scene="planet-exterior", body="earth", distance=6371, mode="small-ball", ball-radius=1, clock="ten-seconds", convention="flipped-riemann"
- `flipped-signature` A writer with the opposite signature: scene="planet-exterior", body="earth", distance=6371, mode="small-ball", ball-radius=1, clock="ten-seconds", convention="flipped-signature"
- `plane-curvature-along` The plane of fall and the marked line: scene="planet-exterior", body="earth", distance=6371, mode="two-crumbs", probe-direction="along-the-line", ball-radius=1, clock="ten-seconds", show-plane-curvature=true
- `plane-curvature-across` The plane of fall and a line across it: scene="planet-exterior", body="earth", distance=6371, mode="two-crumbs", probe-direction="across-the-line", ball-radius=1, clock="ten-seconds", show-plane-curvature=true
- `shear-at-release-beside-earth` Let go with a shear, beside Earth: scene="planet-exterior", body="earth", distance=6371, mode="small-ball", ball-radius=1, clock="ten-seconds", shear-at-release=true

## Readouts

- `drift-along` Drift along the marked line (mm; visible always; 4 decimals; range (-1000, 1000]; sense: positive means the crumb on the marked line has moved away from the centre crumb): “a crumb out along the marked line has drifted {abs} millimetres away from the centre crumb” / “a crumb out along the marked line has drifted {abs} millimetres toward the centre crumb”
- `drift-across` Drift across the marked line (mm; visible always; 4 decimals; range (-1000, 1000]; sense: positive means the crumb out across the marked line has moved away from the centre crumb): “a crumb out across the marked line has drifted {abs} millimetres away from the centre crumb” / “a crumb out across the marked line has drifted {abs} millimetres toward the centre crumb”
- `drift-total` The three drifts added up (mm; visible always; 4 decimals; range (-3000, 3000]; sense: positive means the three drifts together carry crumbs away from the centre crumb): “the three drifts add up to {value} millimetres, counting a drift away from the centre crumb as plus” / “the three drifts add up to {abs} millimetres inward”
- `uniform-part` The same-in-every-direction part of the drift (mm; visible always; 4 decimals; range (-1000, 1000]; sense: positive means this part carries every crumb away from the centre crumb): “the same-in-every-direction part is {value} millimetres, counting a drift away from the centre crumb as plus” / “the same-in-every-direction part is {abs} millimetres inward”
- `shape-part-along` The leftover part along the marked line (mm; visible always; 4 decimals; range (-1000, 1000]; sense: positive means the leftover stretches the ball along the marked line): “the leftover stretches the ball {abs} millimetres along the marked line” / “the leftover squeezes the ball {abs} millimetres along the marked line”
- `volume-change` Change in the room the ball takes up (percent; visible always; 9 decimals; range (-100, 100]; sense: positive means the ball takes up more room than when it was let go): “the ball takes up {value} percent more room than when it was let go” / “the ball takes up {abs} percent less room than when it was let go”
- `along-to-across-ratio` The two drifts compared (1; visible always; 4 decimals; range (-10, 10]; sense: positive means both drifts go the same way, negative means one is outward while the other is inward): “the drift along the marked line is {value} times as big as the drift across it, and the two go the same way” / “the drift along the marked line is {abs} times as big as the drift across it, and the two go opposite ways”
- `net-swirl` Net drift around the ring (mm; visible always; 4 decimals; range (-1000, 1000]; sense: positive means the crumbs are carried around the ring toward rising clock-face numbers): “measured toward rising clock numbers, the net drift of the crumbs around the ring is {abs} millimetres” / “measured toward falling clock numbers, the net drift of the crumbs around the ring is {abs} millimetres”
- `independent-tide-numbers` Different numbers in the tide meter's table (1; visible on-demand; 0 decimals; range (0, 9]): “the nine readings hold {value} different numbers”
- `curvature-length` Curvature length from the squared-and-added invariant (km; visible on-demand; 3 decimals; range (0, 1000000000000]): “the curvature length here is {value} kilometres”
- `plane-curvature-length` Signed curvature length of the chosen plane (km; visible on-demand; 0 decimals; range (-1000000000000, 1000000000000]; sense: positive means free-fall crumbs in that plane speed apart, which on a timelike plane is the opposite of a ball): “the chosen plane curves on a scale of {abs} kilometres, and crumbs in it speed apart” / “the chosen plane curves on a scale of {abs} kilometres, and crumbs in it speed toward each other”
- `printed-mixed-component` Printed component along the marked line, first index up (1; visible on-demand; 1 decimals; range (-10, 10]; sense: the sign this writer prints, in units of G M over c squared r cubed): “this writer prints plus {value}, in units of G M over c squared r cubed” / “this writer prints minus {abs}, in units of G M over c squared r cubed”
- `printed-lowered-component` Printed component along the marked line, first index lowered (1; visible on-demand; 1 decimals; range (-10, 10]; sense: the sign this writer prints once the first index is lowered, in units of G M over c squared r cubed): “with the first index lowered this writer prints plus {value}, in the same units” / “with the first index lowered this writer prints minus {abs}, in the same units”
- `across-entry-change-outward` Change of the across-across entry, moving out along the line (1; visible on-demand; 4 decimals; range (-100, 100]; sense: positive means the entry grows as the cabin moves away from the body): “moving out along the marked line, that entry changes by plus {value}, in units of G M over r to the fourth” / “moving out along the marked line, that entry changes by minus {abs}, in units of G M over r to the fourth”
- `mixed-entry-change-sideways` Change of the across-along entry, moving sideways (1; visible on-demand; 4 decimals; range (-100, 100]; sense: positive means the entry grows as the cabin moves across the marked line): “moving across the marked line, that entry changes by plus {value}, in the same units” / “moving across the marked line, that entry changes by minus {abs}, in the same units”

## Tours

### `first-ring-of-crumbs` · for [[relativistic-tidal-tensor]] · entry

1. `meet-the-cabin` (entry, await none) state: preset="earth-surface-ring", progress=0  
   *Cabin falling beside Earth, twelve crumbs in a ring around a centre crumb, the marked line running through two of them, scales reading zero.*  
   Say: “Here is a cabin falling freely near Earth. Nothing holds it up, and nothing pushes it. Inside I hold twelve crumbs in a ring, around one more crumb in the middle, which I will call the centre crumb. I have drawn a line from the cabin to Earth's centre, and I will call it the marked line. The ring is set so that the marked line runs through two of its crumbs. A set of bathroom scales sits in the corner, and it reads zero.”  
   Describe: A cabin falls near Earth. Inside it, twelve crumbs make a ring around a centre crumb. The marked line runs from the cabin to Earth's centre, through two of the ring crumbs. Bathroom scales in the cabin read zero.
2. `predict-the-shape` (entry, await prediction) state: preset="earth-surface-ring", progress=0; evidences `relativistic-tidal-tensor/checks/crumbs-nearer-and-farther`  
   *Same view, paused at the moment of release.*  
   Predict: “I let every crumb go with no push at all. After ten seconds, will the ring still be a ring?”  
   Say: “Before I let them go, make a guess. I let every crumb go with no push at all. After ten seconds, will the ring still be a ring?”  
   Describe: The crumbs wait in their ring. Nothing has been let go yet.
3. `let-them-go` (entry, await none) state: preset="earth-surface-ring", progress=0; animate progress → 1 over 6 s  
   *Ring stretching along the marked line and squeezing across it, drift arrows magnified one thousand times, ghost of the starting ring left in place.*  
   Say: “The crumbs are free now. The two crumbs on the marked line drift away from the centre crumb. The crumbs across the line drift in toward the centre crumb. The ring becomes an oval. I have made every drift arrow a thousand times longer, so that you can see them at all.”  
   Describe: The ring slowly turns into an oval. It grows along the marked line and narrows across it. A faint copy of the starting ring stays in place behind it.
4. `read-the-two-drifts` (entry, await none) state: preset="earth-surface-ring", progress=1  
   *Readouts: drift along 0.1541 mm, drift across minus 0.0771 mm, for crumbs one metre out after ten seconds.*  
   Say: “Here are the two readings. Each of the two crumbs on the marked line has drifted fifteen hundredths of a millimetre away from the centre crumb. Each crumb across the line has drifted about half as far, toward the centre crumb. That took ten seconds of falling, for crumbs one metre out.”  
   Describe: Two readings. Along the marked line, fifteen hundredths of a millimetre away from the centre crumb. Across it, seven hundredths of a millimetre toward the centre crumb.
5. `a-crumb-on-a-slant` (entry, await none) state: preset="slanted-crumb", progress=1; evidences `relativistic-tidal-tensor/checks/crumb-three-along-four-across`  
   *One probe crumb placed three parts along the line and four parts across it, its place split into two parts, each with its own drift arrow, adding to a slanted drift.*  
   Say: “Now I move one crumb so that it sits neither on the marked line nor straight across it, but on a slant. Its distance from the centre crumb splits into a part along the marked line and a part across it. Each part makes its own drift. The crumb makes both at once, so it drifts on a slant too. One number for the marked line, and one for each of the two directions across it: three numbers give the drift of a crumb placed anywhere near the centre crumb.”  
   Describe: A single crumb sits on a slant from the centre crumb. Its distance from the centre crumb is drawn as two parts, one along the marked line and one across it. Each part has its own drift arrow, and the two arrows add to a slanted one.
6. `inside-a-planet-of-rock` (entry, await none) state: preset="inside-a-rock-planet", progress=1  
   *Ball of crumbs inside a uniform rock planet: every drift is inward and equal, the shape stays round and shrinks.*  
   Say: “Here is the same cabin, now deep inside a planet made of rock. Imagine the crumbs can slip through the rock freely, with nothing but gravity acting on them. Every crumb drifts toward the centre crumb, and all by the same amount. So the shape stays round, and it gets smaller. What the crumbs do depends on the matter around them.”  
   Describe: The cabin is inside a uniform planet of rock. Every crumb drifts toward the centre crumb by the same amount, so the ball stays round and shrinks.

### `the-egg-that-keeps-its-room` · for [[volume-preserving-tidal-deformation]] · entry

1. `a-ball-and-a-meter` (entry, await none) state: preset="earth-surface-ball", progress=0  
   *Small ball of crumbs one metre across around a centre crumb, with the room meter beside it reading no change.*  
   Say: “The cabin is falling freely beside Earth, with a line marked from the cabin to Earth's centre. I call that the marked line. This time the crumbs make a small ball around the centre crumb, and each one is one metre out. Beside the ball is a meter for the room the ball takes up. Right now that meter reads no change.”  
   Describe: Crumbs make a small ball around a centre crumb, each one metre out, and the marked line runs from the cabin to Earth's centre. A meter beside the ball reads no change in the room the ball takes up.
2. `predict-the-room` (entry, await prediction) state: preset="earth-surface-ball", progress=0; evidences `volume-preserving-tidal-deformation/checks/room-in-the-egg`  
   *Paused at release, room meter at zero.*  
   Predict: “The ball is about to become an egg, longer along the marked line. Will the egg take up more room than the ball, less, or the same?”  
   Say: “Make a guess first. The ball is about to become an egg, longer along the marked line. Will the egg take up more room than the ball, less, or the same?”  
   Describe: The ball of crumbs waits at the moment of release, with the room meter reading no change.
3. `watch-it-become-an-egg` (entry, await none) state: preset="earth-surface-ball", progress=0; animate progress → 1 over 6 s  
   *Ball stretching along the marked line and narrowing across it; the room meter stays flat.*  
   Say: “Here they go. The ball grows along the marked line. It narrows in both directions across that line. The room meter hardly moves at all.”  
   Describe: The ball stretches along the marked line and narrows across it. The room meter stays where it was.
4. `the-three-changes-cancel` (entry, await none) state: preset="earth-surface-ball", progress=1  
   *Drift along 0.1541 mm, each across drift minus 0.0771 mm, sum reading 0.0000 mm, room meter flat.*  
   Say: “Now look at why. The stretch along the marked line is fifteen hundredths of a millimetre. There are two squeezes across that line, and each one is about half as big. One stretch out, and two squeezes in of half that size, add up to nothing. So the egg takes up the room the ball had.”  
   Describe: The stretch along the marked line is fifteen hundredths of a millimetre. Each of the two squeezes across it is about half as big. Their sum reads zero, and the room meter has not moved.
5. `a-ball-that-does-shrink` (entry, await none) state: preset="inside-a-rock-planet", progress=1; evidences `volume-preserving-tidal-deformation/checks/which-balls-shrink`  
   *Ball inside a uniform rock planet: the room meter has dropped by about two hundredths of one percent.*  
   Say: “Now put the same ball inside a planet of rock, with rock among the crumbs. Every crumb drifts in toward the centre crumb by the same amount. Nothing cancels, and the room meter drops. Matter inside the ball of crumbs is what makes the room start to change.”  
   Describe: The same ball sits inside a uniform planet of rock. Every crumb drifts inward, the ball stays round, and the room meter has dropped.

### `add-up-the-three-drifts` · for [[ricci-tensor]] · entry

1. `three-drifts-listed` (entry, await none) state: preset="earth-surface-ball", progress=1  
   *The three principal drifts printed: one outward along the marked line, two inward across it.*  
   Say: “A small ball of crumbs has been let go in a cabin falling beside Earth, with a line marked from the cabin to Earth's centre. The ball has three drifts to report. One is along that marked line, and it carries crumbs away from the centre crumb. Two are across the line, and they carry crumbs in toward the centre crumb. Each of the two inward drifts is about half the size of the outward one.”  
   Describe: Three drift readings for the ball beside Earth. One along the marked line to Earth's centre, carrying crumbs away from the centre crumb, and two across that line, carrying crumbs toward it, each about half as big.
2. `predict-the-total` (entry, await prediction) state: preset="earth-surface-ball", progress=1; evidences `ricci-tensor/checks/egg-keeps-its-volume`  
   *The three drifts shown, the total hidden behind a cover.*  
   Predict: “Count a drift away from the centre crumb as plus, and a drift toward it as minus. What do the three drifts add up to here?”  
   Say: “Make a guess before I show the total. Count a drift away from the centre crumb as plus, and a drift toward it as minus. What do the three drifts add up to here?”  
   Describe: The three drift readings stay on screen, with the total covered up.
3. `the-total-reads-zero` (entry, await none) state: preset="earth-surface-ball", progress=1  
   *Total reading 0.0000 mm beside the room meter, which is also flat.*  
   Say: “The total reads zero. That one number is what the table named after Ricci holds, for this cabin at this place. It is the number that says whether the room the ball takes up starts to change. Here it is zero, and the room holds.”  
   Describe: The total of the three drifts reads zero millimetres, and the room meter is flat.
4. `dust-among-the-crumbs` (entry, await none) state: preset="dust-as-dense-as-water", progress=1; evidences `ricci-tensor/checks/denser-dust-faster`  
   *Dust universe as dense as water: all three drifts inward and equal, total minus 0.0004 mm after one second.*  
   Say: “Now I fill the space among the crumbs with dust as dense as water. Every crumb gets an extra drift toward the centre crumb. The total is no longer zero, and the ball shrinks. Denser dust makes that inward total larger.”  
   Describe: The cabin now sits in dust as dense as water. All three drifts go inward, the total is no longer zero, and the room meter drops.
5. `zero-total-is-not-nothing` (entry, await none) state: preset="far-from-every-mass", progress=1; evidences `ricci-tensor/checks/zero-total-is-not-flat`  
   *Far from every mass: every drift reads zero and the shape is unchanged, beside a recall card of the Earth readings.*  
   Say: “Compare that with a cabin far from every mass. Here every single drift reads zero, and the ball keeps its shape. Beside Earth the total was zero too, but the three drifts were not. A zero total does not mean nothing is happening.”  
   Describe: Far from every mass, all three drifts read zero and the ball keeps its shape. A card beside it recalls the Earth readings, where the drifts were not zero.

### `split-the-drift-in-two` · for [[weyl-tensor]] · entry

1. `two-sets-of-arrows` (entry, await none) state: preset="split-the-drift-beside-earth", progress=1  
   *Each drift arrow split into a same-in-every-direction part and a balanced leftover, drawn as two separate sets, never added on screen.*  
   Say: “The cabin is falling freely beside Earth, with a line marked from the cabin to Earth's centre. I can split each crumb's drift into two pieces. The first piece is the same in every direction: every crumb away from the centre crumb, or every crumb toward it. The second piece is what is left over, and it balances: what it stretches one way it squeezes another. I draw the two sets apart, and never on top of each other.”  
   Describe: Every drift arrow is drawn twice, once as a same-in-every-direction part and once as the leftover. The two sets are shown side by side.
2. `predict-which-makes-the-egg` (entry, await prediction) state: preset="split-the-drift-beside-earth", progress=1; evidences `weyl-tensor/checks/ball-above-the-air`  
   *Both readouts covered.*  
   Predict: “Beside Earth, which of the two sets of arrows turns the ball into an egg: the same-in-every-direction set, the leftover set, or both?”  
   Say: “Make a guess. Beside Earth, which of the two sets turns the ball into an egg: the same-in-every-direction set, the leftover set, or both?”  
   Describe: The two arrow sets are on screen with their readings covered.
3. `the-uniform-part-reads-zero` (entry, await none) state: preset="split-the-drift-beside-earth", progress=1  
   *Uniform part reading 0.0000 mm, leftover reading 0.1541 mm along the marked line.*  
   Say: “Beside Earth the same-in-every-direction part reads zero. The leftover does all the work: it stretches the ball along the marked line and squeezes it across. That leftover is what the table named after Weyl holds. No matter sits where the crumbs are, and the leftover is still there.”  
   Describe: The same-in-every-direction reading is zero. The leftover reading stretches the ball along the marked line.
4. `among-dust-the-other-way` (entry, await none) state: preset="split-the-drift-in-dust", progress=1; evidences `weyl-tensor/checks/three-places`  
   *Dust universe: the uniform part is the whole drift and the leftover reads zero.*  
   Say: “In a universe evenly filled with dust, the two readings change places. The same-in-every-direction part is now the whole drift, and the leftover reads zero. So the ball stays round and only shrinks.”  
   Describe: In an evenly filled dust universe the same-in-every-direction part is the whole drift, and the leftover reads zero.
5. `a-wave-with-no-matter` (entry, await none) state: preset="gravitational-wave", progress=0.25  
   *Ring across the wave stretched one way and squeezed the other, uniform part zero, leftover doing all the work.*  
   Say: “Last, a gravitational wave crosses the cabin, with no matter anywhere near. The ring stretches one way across the wave's path and squeezes the other way by the same amount. Again the same-in-every-direction part reads zero, and the leftover does everything.”  
   Describe: A wave crosses the cabin. The ring stretches one way across the wave's path and squeezes the other way by the same amount. The same-in-every-direction reading stays at zero.

### `ricci-flat-is-not-flat` · for [[ricci-flat-spacetime]] · entry

1. `the-cabin-where-nothing-drifts` (entry, await none) state: preset="far-from-every-mass", progress=1  
   *Far from every mass: no drift at all, both lamps off.*  
   Say: “Start far from every mass, with the engines off. No crumb drifts at all. The ball keeps its size and its shape. This is what flat means: nothing drifts, whichever way the cabin moves. Two lamps sit beside the readings, and I will say in a moment what each one tests.”  
   Describe: Far from every mass, no crumb drifts. The ball keeps its size and shape.
2. `predict-the-planet-verdict` (entry, await prediction) state: preset="earth-surface-ball", progress=0; evidences `ricci-flat-spacetime/checks/four-regions-two-tests`  
   *Cabin beside Earth at the moment of release, verdict lamps covered.*  
   Predict: “Beside a planet none of the three drifts is zero, and yet they add up to zero. Does that mean spacetime beside the planet is flat?”  
   Say: “Now move the cabin beside a planet, and make a guess first. Beside a planet none of the three drifts is zero, and yet they add up to zero. Does that mean spacetime beside the planet is flat?”  
   Describe: The cabin sits beside Earth at the moment of release, with the verdict lamps covered.
3. `two-lamps-not-one` (entry, await none) state: preset="earth-surface-ball", progress=1  
   *Two lamps: any drift at all is lit, zero total is lit; the second lamp alone is the Ricci-flat verdict.*  
   Say: “There are two separate lamps here. One says whether any crumb drifts at all. The other says whether the three drifts add to zero. Beside the planet both lamps are lit: crumbs do drift, and the three drifts do add to zero. Zero total is the weaker test, and flat asks for more.”  
   Describe: Two lamps beside the readings. One says that crumbs do drift. The other says the drifts add to zero.
4. `the-wave-passes-the-same-test` (entry, await none) state: preset="gravitational-wave", progress=0.25  
   *Wave scene: crumbs drift, total reads zero, same pair of lamps as the planet case.*  
   Say: “A passing gravitational wave gives the same pair of lamps. Crumbs drift, and the three drifts still add to zero. So a region can pass the zero-total test while crumbs drift all through it.”  
   Describe: In the wave scene the crumbs drift and the three drifts add to zero, lighting the same pair of lamps as the planet case.

### `rocket-or-planet` · for [[flatness-criterion]] · entry

1. `a-windowless-cabin` (entry, await none) state: preset="rocket-cabin", progress=0  
   *Windowless cabin, two crumbs one metre apart, a switch between rocket and planet.*  
   Say: “Here is a windowless cabin with two crumbs held side by side, one metre apart. In one scene the cabin rides a rocket that is speeding up, far from every mass. In the other it falls beside a planet. Everything falls to the floor in both.”  
   Describe: A windowless cabin holds two crumbs one metre apart, side by side. A switch changes the cabin between a speeding-up rocket and a fall beside a planet.
2. `predict-the-gap` (entry, await prediction) state: preset="rocket-cabin", progress=0; evidences `flatness-criterion/checks/rocket-drop`  
   *Both scenes paused at the moment of release.*  
   Predict: “The two crumbs are let go side by side, with no push. In which cabin does the gap between them change?”  
   Say: “Make a guess before I let them go. The two crumbs are let go side by side, with no push. In which cabin does the gap between them change?”  
   Describe: Both cabins are paused at the moment the crumbs are let go.
3. `the-rocket-keeps-the-gap` (entry, await none) state: preset="rocket-cabin", progress=1  
   *Rocket scene after ten seconds: both drift readings exactly zero, crumbs land the same distance apart.*  
   Say: “In the rocket, the crumbs land the same distance apart as they started. The reading is exactly zero, however much I magnify it. A pull that makes everything fall the same way does not curve spacetime.”  
   Describe: In the rocket the crumbs land the same distance apart, and every drift reading is exactly zero.
4. `the-planet-closes-the-gap` (entry, await none) state: preset="two-crumbs-across", progress=1  
   *Planet scene after ten seconds: the gap has closed by about seven hundredths of a millimetre.*  
   Say: “Beside the planet the gap closes, by about seven hundredths of a millimetre in ten seconds. That drift is the test for curved spacetime, and the pull toward the floor is not. A region is flat when the table that records the drift reads zero everywhere in it, and only then.”  
   Describe: Beside the planet the gap between the crumbs closes by about seven hundredths of a millimetre in ten seconds.

### `two-crumbs-and-the-extra` · for [[geodesic-deviation-equation]] · entry

1. `scales-that-read-zero` (entry, await none) state: preset="two-crumbs-across", progress=0; evidences `geodesic-deviation-equation/checks/scales-cannot-tell`  
   *Falling cabin with a clock, bathroom scales reading zero, and two crumbs one metre apart across the marked line.*  
   Say: “The cabin falls beside Earth with a clock and a set of bathroom scales. A line is marked from the cabin to Earth's centre, and I call it the marked line. The scales read zero and stay at zero the whole way down. One object on its own cannot detect the curving. Two crumbs, one metre apart across the marked line, will tell us plenty.”  
   Describe: A falling cabin holds a clock, bathroom scales reading zero, and two crumbs one metre apart across the marked line, which runs from the cabin to Earth's centre.
2. `the-gap-closes-faster-and-faster` (entry, await none) state: preset="two-crumbs-across", progress=0; animate progress → 1 over 8 s  
   *Bar chart of the shrink in each second, each bar taller than the one before by a fixed amount.*  
   Say: “Watch the bars. Each bar is how much the gap closes in one second. Every bar is taller than the bar before it, by the same amount each time. So the closing speeds up, and it speeds up steadily.”  
   Describe: A bar for each second of the fall. Each bar is taller than the one before it, by the same amount each time.
3. `predict-twice-the-gap` (entry, await prediction) state: preset="two-crumbs-across", progress=1; evidences `geodesic-deviation-equation/checks/three-metres-apart`  
   *The one-metre result on screen, the two-metre result covered.*  
   Predict: “Each bar is taller than the bar before it by the same amount, and I call that amount the extra. Now I start the two crumbs two metres apart instead of one. What happens to the extra each second?”  
   Say: “Make a guess. Each bar is taller than the bar before it by the same amount, and I call that amount the extra. Now I start the two crumbs two metres apart instead of one. What happens to the extra each second?”  
   Describe: The one-metre reading stays on screen while the two-metre reading is covered.
4. `twice-the-gap-twice-the-extra` (entry, await none) state: preset="two-crumbs-across", ball-radius=2, progress=1  
   *Two-metre pair after ten seconds: every bar and the drift reading are twice the one-metre values.*  
   Say: “Every bar has doubled, and so has the reading. Twice the gap gives twice the extra each second. Three times the gap would give three times the extra.”  
   Describe: With the crumbs two metres apart, every bar and the drift reading are twice as big as before.
5. `divide-by-the-gap` (entry, await none) state: preset="two-crumbs-across", progress=1  
   *Readout dividing the extra by the gap, the same number for both gaps, labelled as one entry of the curvature table.*  
   Say: “So divide the extra by the gap, and the two pairs give one number. That number belongs to the place, not to the crumbs. It is one entry of the table that describes the curving there.”  
   Describe: The extra divided by the gap gives the same number for both pairs, labelled as one entry of the curvature table.

### `where-the-shape-change-starts` · for [[weyl-tensor-field-equation]] · entry

1. `inside-the-falling-cloud` (entry, await none) state: preset="dust-cloud-inside", progress=1  
   *Cabin among the dust of a uniform cloud falling in on itself: uniform arrows only, leftover reading zero.*  
   Say: “A round cloud of dust has just been let go, and it is falling in on itself. Our cabin falls with the dust, halfway out from the cloud's centre. Each drift here is split in two: a part that is the same in every direction, and a leftover that would change the shape. The ball of crumbs only shrinks, and the leftover reading is exactly zero, so the shape does not change at all.”  
   Describe: The cabin sits among the dust of a falling cloud, halfway out from the cloud's centre. The ball of crumbs shrinks and stays round, and the leftover part of the drift, the part that would change the shape, reads zero.
2. `predict-at-the-surface` (entry, await prediction) state: preset="dust-cloud-inside", progress=1; evidences `weyl-tensor-field-equation/checks/crumbs-at-the-centre-and-halfway`  
   *Cabin at half a cloud radius, with a slider running out to six cloud radii.*  
   Predict: “I slide the cabin out through the cloud's surface, into the empty space beyond it. Where does the shape of the ball start to change?”  
   Say: “Make a guess. I slide the cabin out through the cloud's surface, into the empty space beyond it. Where does the shape of the ball start to change?”  
   Describe: The cabin sits at half a cloud radius, with a slider that can carry it out past the surface.
3. `it-switches-on-at-the-surface` (entry, await none) state: preset="dust-cloud-outside", progress=1  
   *Cabin two cloud radii out: uniform arrows gone, leftover arrows on, ball becoming an egg.*  
   Say: “Crossing the cloud's surface switches the shape change on. Outside, the uniform arrows vanish and the leftover arrows appear. Inside, the amount of dust was the same everywhere, so no shape change started there. The shape change is made where the amount of matter changes.”  
   Describe: Two cloud radii out, the uniform arrows have vanished and the leftover arrows have appeared. The ball is becoming an egg.
4. `twice-as-far-one-eighth` (entry, await none) state: preset="dust-cloud-outside", depth-in-cloud-radii=4, progress=1; evidences `weyl-tensor-field-equation/checks/twice-as-far-one-eighth`  
   *Cabin four cloud radii out: the leftover reading is one eighth of its value two radii out.*  
   Say: “Now I take the cabin twice as far out as that, to four cloud radii. The leftover reading is one eighth of what it was. Empty space cannot make the shape change or destroy it. Each layer of empty space only hands the shape change on, and spreading it over a wider shell is what makes it fade.”  
   Describe: Four cloud radii out, the leftover reading is one eighth of its value at two cloud radii.

### `no-whirlpool-in-the-tides` · for [[symmetries-of-the-riemann-tensor]] · entry

1. `nine-readings-in-a-table` (entry, await none) state: preset="tide-table-beside-earth", progress=1  
   *Three-by-three table of drifts beside the ring, with mirror pairs lit together in matching colours.*  
   Say: “A tide meter has three arms at right angles, and it makes nine readings. Here they are, in a table. Each reading says how far a crumb out along one arm drifts in the direction of another arm. Take the reading for a crumb along the first arm drifting toward the second, and the reading for a crumb along the second arm drifting toward the first. Those two mirror each other, they light up together, and they always match. I will call that the mirror rule.”  
   Describe: A three-by-three table of drift readings sits beside the ring. One reading is for a crumb along the first arm drifting toward the second. It is lit together with the reading for a crumb along the second arm drifting toward the first, and the two are equal.
2. `predict-the-whirlpool` (entry, await prediction) state: preset="tide-table-beside-earth", progress=1; evidences `symmetries-of-the-riemann-tensor/checks/four-crumbs-and-a-whirlpool`  
   *The ring and the table, with the swirl reading covered.*  
   Predict: “Could the drifts carry a ring of falling crumbs round and round, like water going down a drain?”  
   Say: “Make a guess. Could the drifts carry a ring of falling crumbs round and round, like water going down a drain?”  
   Describe: The ring and its table stay on screen, with the reading for drift around the ring covered.
3. `the-swirl-reads-zero` (entry, await none) state: preset="tide-table-beside-earth", progress=1  
   *Net drift around the ring reading 0.0000 mm, mirror pairs equal.*  
   Say: “The drift around the ring reads zero, and it stays at zero all the way down. That is the mirror rule at work. Take two crumbs let go along two directions at right angles. Each one drifts toward the other's direction by the same amount.”  
   Describe: The reading for drift around the ring is zero. The mirror pairs in the table are equal.
4. `an-invented-whirlpool` (entry, await none) state: preset="whirlpool-table-beside-earth", progress=1  
   *Invented table with unmatched mirror pairs: the ring gains a net drift round, and the counter of different numbers rises from six to nine.*  
   Say: “Here is an invented table, one that breaks the mirror rule. Now the crumbs are carried round the ring, and they gain speed every lap. Nothing would be supplying the energy for that. The mirror rule also cuts the nine readings down to six different numbers, and the invented table needs all nine.”  
   Describe: An invented table breaks the mirror rule. The crumbs are carried round the ring, and the counter of different numbers rises from six to nine.

### `six-numbers-of-twenty` · for [[number-of-independent-riemann-components]] · entry

1. `count-the-readings` (entry, await none) state: preset="tide-table-beside-earth", progress=1  
   *Counter showing 9 readings from the three-arm tide meter.*  
   Say: “The tide meter makes nine readings, one for each pairing of its three arms. The counter says nine.”  
   Describe: A counter beside the table says the tide meter makes nine readings.
2. `predict-how-many-are-different` (entry, await prediction) state: preset="tide-table-beside-earth", progress=1; evidences `number-of-independent-riemann-components/checks/what-the-tide-meter-misses`  
   *The counters of different numbers and of the full table are covered.*  
   Predict: “Of those nine readings, how many do you think are really different numbers, and do you think one falling cabin like this catches all the curving at that place?”  
   Say: “Make a guess, and a guess is all I am asking for. Of those nine readings, how many do you think are really different numbers? And do you think one falling cabin like this catches all the curving at that place?”  
   Describe: The table is on screen with the counters of different numbers covered.
3. `six-of-twenty` (entry, await none) state: preset="tide-table-beside-earth", progress=1  
   *Counters reading 9 readings, 6 different numbers, 6 of the 20 entries of the full table.*  
   Say: “Six. A crumb out along one arm drifts toward a second arm exactly as far as a crumb along that second arm drifts toward the first. That mirror rule ties the nine readings in pairs, so they hold six different numbers. The counter beside them says the full table for space and time holds twenty numbers. So one falling cabin with crumbs at rest reads six of the twenty, and misses fourteen.”  
   Describe: The counters read nine readings, six different numbers, and six of the twenty entries of the full table.

### `tides-a-falling-room-cannot-remove` · for [[riemann-tensor-in-normal-coordinates]] · entry

1. `nothing-at-the-centre` (entry, await none) state: preset="earth-surface-ball", progress=0  
   *Cabin falling freely; the centre crumb sits still against the cabin walls, scales reading zero.*  
   Say: “The cabin falls freely, and the centre crumb hangs still against the cabin's walls. The scales read zero. Where that one crumb sits, gravity has been taken away completely.”  
   Describe: The cabin falls freely. The centre crumb hangs still against the cabin walls and the scales read zero.
2. `predict-farther-out` (entry, await prediction) state: preset="earth-surface-ball", progress=0; evidences `riemann-tensor-in-normal-coordinates/checks/crumbs-in-a-falling-room`  
   *Cabin paused at release with the outer crumbs waiting.*  
   Predict: “Is a small falling room exactly like empty space, so that crumbs away from its centre stay put as well?”  
   Say: “Make a guess. Is a small falling room exactly like empty space, so that crumbs away from its centre stay put as well?”  
   Describe: The cabin is paused at release, with the outer crumbs waiting one metre from the centre crumb.
3. `the-drift-is-what-is-left` (entry, await none) state: preset="earth-surface-ball", progress=1  
   *Outer crumbs drifted after ten seconds while the centre crumb has not moved against the walls.*  
   Say: “The centre crumb has not moved, and the outer crumbs have. Falling takes gravity away at one spot, and never in a whole room. What the fall leaves behind is the curving, and choosing how to fall cannot remove it.”  
   Describe: After ten seconds the centre crumb still hangs still, while the crumbs one metre out have drifted.

### `one-total-for-every-cabin` · for [[einstein-space]] · working

1. `read-the-trace-beside-earth` (working, await none) state: preset="earth-surface-ball", progress=1  
   *Three principal drifts in the ratio minus 2, 1, 1 and their sum, which reads zero.*  
   Say: “The three principal drifts stand in the ratio minus two, one, one. Their sum is the tidal trace, which is the Ricci tensor fed this cabin's four-velocity twice. Beside a round body in vacuum it reads zero.”  
   Describe: Three drift readings in the ratio minus two, one, one, with a sum that reads zero.
2. `move-the-cabin-out` (working, await prediction) state: preset="earth-surface-ball", distance=12742, progress=1; evidences `einstein-space/checks/two-cabins-near-the-sun`  
   *Cabin at twice the distance, drifts one eighth as large, sum still reading zero.*  
   Predict: “At twice the distance the drifts drop to one eighth. What happens to their sum?”  
   Say: “At twice the distance each drift is one eighth as large. Predict what happens to their sum, then read it. It is still zero. Drifts that differ by a factor of eight can share one total.”  
   Describe: At twice the distance each drift is one eighth as large, and their sum still reads zero.
3. `race-past-at-six-tenths-of-light` (working, await none) state: preset="passing-sideways", progress=1  
   *Cabin passing sideways at six tenths of the speed of light: drifts much larger, sum still zero.*  
   Say: “Now a cabin races sideways past Earth at six tenths of the speed of light. Its tidal matrix is quite different: the entries across the motion are multiplied by gamma squared times one plus two beta squared. The sum is still zero. That is what an Einstein space asks for, at every place and for every cabin.”  
   Describe: A cabin passing sideways at six tenths of the speed of light reads much larger drifts, and their sum is still zero.
4. `a-dust-universe-fails-the-test` (working, await none) state: preset="moving-through-the-dust", progress=1; evidences `einstein-space/checks/comoving-observers-agree`  
   *Dust universe with the cabin moving at six tenths of the speed of light: the total is 2.125 times the value a cabin at rest in the dust reads.*  
   Say: “A dust universe looks the same at every place, and every cabin at rest in the dust reads the same total. But drive a cabin through the dust at six tenths of the speed of light, and the total rises to two point one two five times that value. The condition must hold for every cabin, so a dust universe is not an Einstein space.”  
   Describe: In the dust universe a cabin moving at six tenths of the speed of light reads a total two point one two five times the value a cabin at rest in the dust reads.

### `readings-that-must-fit-together` · for [[bianchi-identity]] · working

1. `one-reading-per-place` (working, await none) state: preset="earth-orbit-gradiometer", progress=1  
   *Gradiometer grid: the tidal matrix read at a small grid of neighbouring places 400 kilometres up.*  
   Say: “The gradiometer reads the tidal matrix not only here, but at a small grid of neighbouring places. Each place has its own matrix. The identity is a rule about how those matrices differ.”  
   Describe: A gradiometer reads the tidal matrix at a small grid of neighbouring places, 400 kilometres up.
2. `predict-the-two-gradients` (working, await prediction) state: preset="earth-orbit-gradiometer", progress=1; evidences `bianchi-identity/checks/tidal-gradient-at-goce-height`  
   *Both gradient readouts covered.*  
   Predict: “Take the across-across entry and move the cabin out along the marked line. Take the across-along entry and move the cabin sideways instead. How do the two rates of change compare?”  
   Say: “Predict before you read. Take the across-across entry and move the cabin out along the marked line. Take the across-along entry and move the cabin sideways instead. How do the two rates of change compare?”  
   Describe: Two gradient readings sit covered beside the grid of matrices.
3. `the-two-gradients-match` (working, await none) state: preset="earth-orbit-gradiometer", progress=1  
   *Both gradient readouts reading minus 3, in units of G M over r to the fourth.*  
   Say: “Both read minus three, in units of G M over r to the fourth. In a static weak field the identity makes the gradient of the tidal matrix symmetric in all three of its indices. So readings at neighbouring places are not free to differ however they like.”  
   Describe: Both gradient readings are minus three, in units of G M over r to the fourth.
4. `the-identity-permits-variation` (working, await none) state: preset="earth-orbit-gradiometer", distance=12742, progress=1  
   *Cabin at twice the distance: every entry has changed by a factor of eight while the two gradients still match.*  
   Say: “Move out to twice the distance, and every entry changes by a factor of eight. The identity has not forbidden that. It ties the rates of change to one another, and leaves the curving free to vary from place to place.”  
   Describe: At twice the distance every entry has changed by a factor of eight, and the two gradient readings still match.

### `calibrate-a-strangers-table` · for [[curvature-sign-conventions]] · working

1. `the-course-printing` (working, await none) state: preset="earth-surface-ball", progress=1  
   *Course conventions: the printed component along the marked line reads minus 2 with the first index up and minus 2 lowered.*  
   Say: “With the course conventions, the component along the marked line prints as minus two, in units of G M over c squared r cubed. Lowering its first index leaves minus two, because the signature makes that diagonal metric factor plus one.”  
   Describe: With the course conventions, the printed component reads minus two with the first index up, and minus two once it is lowered.
2. `predict-what-the-toggle-moves` (working, await prediction) state: preset="earth-surface-ball", progress=1; evidences `curvature-sign-conventions/checks/signature-flip-what-changes`  
   *Convention toggle highlighted, readings covered.*  
   Predict: “I switch to a writer who defines the Riemann tensor with the opposite sign. Which changes: the printed component, the crumbs' drift, or both?”  
   Say: “Predict first. I switch to a writer who defines the Riemann tensor with the opposite sign. Which changes: the printed component, the crumbs' drift, or both?”  
   Describe: A toggle for the writer's conventions is highlighted, with the readings covered.
3. `only-the-printing-moves` (working, await none) state: preset="flipped-riemann-sign", progress=1  
   *Flipped Riemann sign: printed component now plus 2 up and plus 2 lowered, drift readings unchanged at 0.1541 and minus 0.0771 millimetres.*  
   Say: “The printed component flips to plus two, and so does its lowered form. The drift readings have not moved by a single digit. The crumbs do what they do; a sign convention only decides how a writer records it.”  
   Describe: With the flipped Riemann sign the printed component reads plus two, and the drift readings are unchanged.
4. `the-signature-touches-only-the-lowered-form` (working, await none) state: preset="flipped-signature", progress=1  
   *Flipped signature: printed component minus 2 with the first index up, plus 2 lowered, drifts unchanged.*  
   Say: “Now flip the signature instead. The component with its first index up is untouched, because a Christoffel symbol carries one inverse metric and one metric derivative. Lowering an index brings one more metric factor, so the lowered form flips. To read a stranger's table, calibrate it on drifts everyone agrees on.”  
   Describe: With the flipped signature the component with its first index up is unchanged at minus two, while the lowered form reads plus two. The drifts are unchanged.

### `curvature-length-at-a-horizon` · for [[kretschmann-scalar]] · working

1. `read-the-stretch` (working, await none) state: preset="earth-surface-ball", progress=1  
   *Earth's surface: drift readings, with the curvature length beside them reading about 92 million kilometres.*  
   Say: “Beside a round body in vacuum, the stretch along the marked line fixes the squared-and-added invariant. Its fourth root is a length, and beside Earth that length is about ninety two million kilometres.”  
   Describe: Beside Earth the drift readings sit next to a curvature length of about ninety two million kilometres.
2. `predict-halving-the-distance` (working, await prediction) state: preset="earth-surface-ball", progress=1; evidences `kretschmann-scalar/checks/halve-the-distance`  
   *Distance slider highlighted, invariant covered.*  
   Predict: “I halve the distance from the body's centre, staying outside it. By what factor does the squared-and-added invariant grow?”  
   Say: “Predict before you read. I halve the distance from the body's centre, staying outside it. By what factor does the squared-and-added invariant grow?”  
   Describe: The distance slider is highlighted and the invariant reading is covered.
3. `sixty-four-times` (working, await none) state: preset="black-hole-horizon", distance=59.08, progress=1  
   *Black hole at twice the horizon radius: curvature length 44.897 kilometres.*  
   Say: “The invariant falls as the inverse sixth power of the distance, so halving the distance multiplies it by sixty four. The curvature length shrinks by two to the power three halves. At twice a ten solar mass hole's horizon radius it is about forty five kilometres.”  
   Describe: At twice the horizon radius of a ten solar mass black hole the curvature length is about forty five kilometres.
4. `nothing-blows-up-at-the-horizon` (working, await none) state: preset="black-hole-horizon", progress=1; evidences `kretschmann-scalar/checks/crushed-at-the-horizon`  
   *Cabin at the horizon of a ten solar mass hole: curvature length 15.873 kilometres, drifts finite and small over a millionth of a second.*  
   Say: “At the horizon itself the curvature length is about sixteen kilometres, comparable to the hole's own size. It is a perfectly ordinary number. A metric component blowing up there is the chart's doing, not the geometry's, and only an unbounded invariant along a finite path proves a singularity.”  
   Describe: At the horizon of a ten solar mass black hole the curvature length reads about sixteen kilometres, and the drift readings stay small and finite.

### `planes-read-from-the-drifts` · for [[sectional-curvature]] · working

1. `pick-a-plane` (working, await none) state: preset="plane-curvature-along", progress=1  
   *Plane spanned by the cabin's four-velocity and the marked line, with its signed curvature length printed.*  
   Say: “A pair of crumbs picks out a plane: the cabin's four-velocity and the direction to the probe crumb. The tidal entry along that direction gives the plane its sectional curvature, as minus that entry divided by c squared.”  
   Describe: The plane spanned by the cabin's four-velocity and the marked line is drawn, with its signed curvature length printed.
2. `predict-the-sign` (working, await prediction) state: preset="plane-curvature-along", progress=1; evidences `sectional-curvature/checks/radial-pair-in-a-falling-cabin`  
   *Sign of the plane readout covered.*  
   Predict: “Crumbs along the marked line speed apart. Is the sectional curvature of that plane positive or negative?”  
   Say: “Predict before you read, and be careful. Crumbs along the marked line speed apart. Is the sectional curvature of that plane positive or negative?”  
   Describe: The sign of the plane curvature reading is covered while the drift readings stay visible.
3. `positive-drives-them-apart` (working, await none) state: preset="plane-curvature-along", progress=1  
   *Plane readout positive, about 171 million kilometres, labelled as crumbs speeding apart.*  
   Say: “It is positive. On a timelike plane the squared area in the denominator is negative, so positive sectional curvature drives free-fall neighbours apart. That is the opposite of a ball, where positive curvature draws walkers together. The behaviour is the same in every convention; only the sign of the number is a choice.”  
   Describe: The plane curvature reading is positive, about one hundred and seventy one million kilometres, and the crumbs in that plane speed apart.
4. `the-other-plane-has-the-other-sign` (working, await none) state: preset="plane-curvature-across", progress=1  
   *Plane of fall and a line across the marked line: reading negative, about 241 million kilometres.*  
   Say: “Swing the probe crumb across the marked line, and the plane's curvature changes sign. Crumbs in that plane speed toward each other. One event carries many planes, and they need not agree.”  
   Describe: For the plane containing a direction across the marked line the reading is negative, about two hundred and forty one million kilometres.

## Design rules

- **Keep the room meter beside the shape at every moment, in every scene.** Because: A ball that visibly stretches one way and narrows the other reads as a ball being crushed unless the room is shown at the same time. Prevents `volume-preserving-tidal-deformation/misconceptions/tides-squash-the-ball`.
- **Draw the same-in-every-direction part and the leftover as two separate sets of arrows; never show their sum as a third set.** Because: Once the two are drawn added, a learner reads the change of shape as a change of room. Prevents `ricci-tensor/misconceptions/shape-change-means-volume-change`.
- **Always draw both crumbs on the marked line, the one nearer the body and the one farther from it, with their drift arrows.** Because: Showing only the nearer crumb lets a learner keep the belief that everything is drawn toward the body. Prevents `relativistic-tidal-tensor/misconceptions/far-crumb-closes-in`.
- **Make the slanted probe crumb as easy to choose as the two crumbs on the axes.** Because: Only a crumb off both axes shows a drift that points neither straight out nor straight in. Prevents `relativistic-tidal-tensor/misconceptions/drift-straight-out-or-in`.
- **Keep a set of scales in the cabin corner, reading zero in every scene and at every moment.** Because: Floating is not the absence of gravity, and the drift beside the zero reading is the whole point. Prevents `newtonian-deviation-equation/misconceptions/floating-means-no-gravity`.
- **Keep the speeding-up rocket one click from the planet, with the same crumbs, the same clock and the same magnification.** Because: A pull toward the floor happens in both, and only the drift between the crumbs separates them. Prevents `flatness-criterion/misconceptions/pull-means-curved`.
- **Keep the net drift around the ring on screen whenever the ring is shown, and let it leave zero only when the invented table is switched on.** Because: A whirlpool of falling crumbs would let a crumb gain speed every lap with nothing paying for it. Prevents `symmetries-of-the-riemann-tensor/misconceptions/tides-can-whirl`.
- **Print the three drifts and their total together, never the total alone.** Because: A total that stays the same while the drifts change by factors of thousands is the whole content of the Einstein condition. Prevents `einstein-space/misconceptions/same-total-means-same-curving`.
- **Let the convention toggle change printed components only; every crumb, arrow and drift reading stays exactly as it is.** Because: Which way counts as plus is a choice, and a learner must see that it changes no measurement. Prevents `curvature-sign-conventions/misconceptions/opposite-sign-means-mistake`.
- **Report the squared-and-added invariant as a curvature length, and never let a single chart component drive the horizon display.** Because: The chart component that blows up at the horizon has made generations of readers expect something to happen there. Prevents `kretschmann-scalar/misconceptions/horizon-is-infinite`.
- **Keep the distance between the outer crumbs and the centre crumb adjustable while the drift readings stay on screen.** Because: The drift is proportional to the separation, and only changing the separation shows that. Prevents `geodesic-deviation-equation/misconceptions/distance-apart-does-not-matter`.
- **Show two separate lamps: one for whether any crumb drifts, one for whether the three drifts add to zero.** Because: One lamp would let the weaker test stand in for flatness. Prevents `ricci-flat-spacetime/misconceptions/ricci-flat-is-flat`.
- **In the falling dust cloud the cabin always sits among the dust, with no shaft or cavity cut for it.** Because: A hollow shaft changes the drift inside a body, so the reading would no longer be the reading for that matter. Prevents `weyl-tensor-field-equation/misconceptions/stretch-is-strongest-where-matter-is`.
- **Print the count of different numbers beside the count of the full table's entries, as six of twenty.** Because: A cabin whose crumbs are at rest reads only the entries with two time indices, and a learner should see what is missing. Prevents `number-of-independent-riemann-components/misconceptions/tides-show-all-the-curving`.
- **Print the sectional curvature of a plane with a phrase saying which way its crumbs move, never with the sign alone.** Because: On a timelike plane a positive value drives neighbours apart, the opposite of a ball, and the sign alone invites the wrong reading. Prevents `sectional-curvature/misconceptions/spreading-means-negative`.
- **Measure and label every drift against the centre crumb at the same reading of the cabin clock.** Because: A separation compared at mismatched moments picks up a piece along the worldline, which is a clock offset and not a distance. Prevents `deviation-vector/misconceptions/any-moments-will-do`.
- **Hold the centre crumb still against the cabin walls in every scene, while the outer crumbs drift.** Because: A falling room removes gravity on one worldline, not in a whole room, and the contrast has to be visible in one picture. Prevents `riemann-tensor-in-normal-coordinates/misconceptions/small-falling-room-is-empty-space`.
- **Never offer a scene in which free fall alone removes the drift; only the flat scenes read zero.** Because: Free fall is widely believed to remove gravity completely, and the drift is what it leaves. Prevents `riemann-curvature-tensor/misconceptions/free-fall-removes-all-gravity`.
- **Light the scale-only-map lamp only after the leftover reading has held at zero for every cabin direction the scene offers.** Because: A leftover of zero is not a drift of zero, and one direction is not every direction. Prevents `weyl-criterion-for-conformal-flatness/misconceptions/zero-weyl-means-no-drift`.
- **Print the arrow magnification beside the cabin, and keep every readout at its true value.** Because: Drifts of a tenth of a millimetre have to be magnified to be seen at all, and a learner must know by how much.
- **Mark the readouts as out of the model's range when the cabin's own fall would change the tidal strength by more than one part in a hundred over the chosen clock.** Because: The model holds the tidal matrix at the release event, and a reading outside that range would be reported as exact when it is not.
- **Draw the marked line in every scene and print what it means there: the line to the body's centre, the line the cabin moves along, or the wave's stretch line.** Because: Every direction needs its reference, and the readouts are named against this one line.

## Model

One freely falling observer carries a parallel-propagated orthonormal frame, so the geodesic deviation equation becomes an ordinary equation for the frame components of the separation, driven by the symmetric tidal matrix $E_{ij}$. Each scene supplies its own $E_{ij}$ in the cabin's frame. The matrix is evaluated at the release event and held fixed while the clock runs, and the equation is then solved exactly along its three principal directions. The readouts report the drift of each outer crumb against the centre crumb, the trace, the trace-free remainder, the room the crumbs enclose, and the invariants and gradients built from the same matrix.

**The deviation equation in the cabin's frame**

$$
\frac{d^2\xi^{\hat\imath}}{d\tau^2} = -E_{ij}\,\xi^{\hat\jmath},\qquad E_{ij} = c^2 R^{\hat\imath}{}_{\hat0\hat\jmath\hat0}
$$

Holds when: Orthonormal frame carried by the cabin's gyroscopes along a geodesic; first order in the separation and in the relative velocity.

**Solution along a principal direction**

$$
\xi_k(\tau) = \xi_k(0)\cos\!\big(\sqrt{\lambda_k}\,\tau\big)\ (\lambda_k > 0),\qquad \xi_k(\tau) = \xi_k(0)\cosh\!\big(\sqrt{-\lambda_k}\,\tau\big)\ (\lambda_k < 0)
$$

Holds when: Released at rest relative to the centre crumb, with $E_{ij}$ held at its release value; $\lambda_k$ are the eigenvalues of $E_{ij}$.

**Tidal matrix outside a round body**

$$
E_{ij} = \frac{GM}{r^3}\big(\delta_{ij} - 3\hat x_i\hat x_j\big) = \frac{GM}{r^3}\,\mathrm{diag}(-2, 1, 1)
$$

Holds when: Vacuum outside a non-rotating spherical body, for an observer at rest or falling along the marked line; exact in Schwarzschild with $m = GM/c^2$, and the weak-field limit of $\partial_i\partial_j\Phi$ with $\Phi = -GM/r$.

**Tidal matrix inside uniform matter**

$$
E_{ij} = \frac{4\pi G\rho}{3}\,\delta_{ij}
$$

Holds when: Uniform density $\rho$ with the cabin among the matter and the crumbs passing through it freely; the same matrix serves a comoving cabin in a dust universe.

**The trace and what fills the space**

$$
E_{ii} = c^2 R_{\mu\nu}u^\mu u^\nu = 4\pi G\Big(\rho + \frac{3p}{c^2}\Big) - \Lambda c^2
$$

Holds when: Einstein's equation with a perfect fluid at the cabin; zero outside matter with no cosmological constant. A dark-energy density has $p = -\rho_\Lambda c^2$, so the trace is $-8\pi G\rho_\Lambda$.

**How the room starts to change**

$$
\left.\frac{\ddot{\delta V}}{\delta V}\right|_{\tau = 0} = -E_{ii} = -R_{\mu\nu}u^\mu u^\nu
$$

Holds when: Small ball released at rest relative to the cabin, with no shear at release.

**What the shear takes later**

$$
\ln\frac{\delta V}{\delta V_0} = -\tfrac{1}{12}E_{ij}E_{ij}\,\tau^4 + O(\tau^5)
$$

Holds when: Vacuum, no cosmological constant, released at rest; for the point-mass matrix this is $-\tfrac12 (GM/r^3)^2\tau^4$.

**Splitting the drift in two**

$$
E_{ij} = \tfrac13 E_{kk}\,\delta_{ij} + \Big(E_{ij} - \tfrac13 E_{kk}\,\delta_{ij}\Big)
$$

Holds when: The trace part is fixed by the matter at the cabin through Einstein's equation. The remainder is the electric part of the Weyl tensor, $c^2C_{\hat\imath\hat0\hat\jmath\hat0}$, whenever the matter at the cabin is absent or is dust at rest in the cabin.

**Tides read by a cabin passing sideways**

$$
E_{ij} = \frac{GM}{r^3}\,\mathrm{diag}\big(-\gamma^2(2+\beta^2),\ \gamma^2(1+2\beta^2),\ 1\big)
$$

Holds when: Vacuum outside a round body, boost of speed $\beta$ across the marked line; the entry along the motion is unchanged and the trace stays zero. In a dust universe the same boost gives $E = \tfrac{4\pi G\rho}{3}\mathrm{diag}(1, \gamma^2(1+2\beta^2), \gamma^2(1+2\beta^2))$ with the motion along the first axis.

**Gradients that must fit together**

$$
\partial_k E_{ij} = \partial_j E_{ik},\qquad \partial_k\partial_j\partial_i\Phi = \frac{GM}{r^4}\big[15\,\hat x_i\hat x_j\hat x_k - 3(\hat x_k\delta_{ij} + \hat x_j\delta_{ki} + \hat x_i\delta_{kj})\big]
$$

Holds when: Static weak field, $E_{ij} = \partial_i\partial_j\Phi$ with $\Phi = -GM/r$; the contracted Bianchi identity in this limit. Both readouts take the value $-3$ in units of $GM/r^4$.

**The squared-and-added invariant and its length**

$$
\mathcal K = R_{\mu\nu\rho\sigma}R^{\mu\nu\rho\sigma} = \frac{48\,G^2M^2}{c^4 r^6},\qquad \mathcal K^{-1/4} = \frac{r^{3/2}}{48^{1/4}\,(GM/c^2)^{1/2}}
$$

Holds when: Schwarzschild exterior; finite at the horizon, where the length is the fourth root of four thirds times $GM/c^2$, and unbounded only as the centre is approached.

**Sectional curvature of a plane of fall**

$$
K(u, e) = -\frac{E_{ee}}{c^2},\qquad g\!\left(\xi, \frac{D^2\xi}{d\tau^2}\right) = +K(u,\xi)\,g(\xi,\xi)
$$

Holds when: Timelike plane with $u$ unit timelike and $e$ unit spacelike orthogonal to $u$, in the course's sign; the squared area in the denominator is negative, which is why the sign is opposite to a sphere's.

**A ring in a passing wave**

$$
\frac{\delta L_x}{L} = +\frac{h_+}{2},\qquad \frac{\delta L_y}{L} = -\frac{h_+}{2},\qquad \frac{\delta L_z}{L} = 0
$$

Holds when: Transverse-traceless gauge, free masses at rest before the wave arrives; the enclosed room changes only at second order in the strain, by $-h_+^2/4$ at the peak.

**What a sign convention moves**

$$
\tilde R^\rho{}_{\sigma\mu\nu} = s_R\,R^\rho{}_{\sigma\mu\nu},\qquad \tilde R_{\rho\sigma\mu\nu} = s_g s_R\,R_{\rho\sigma\mu\nu}
$$

Holds when: $s_g$ is the sign of the writer's metric relative to the course's, $s_R$ the overall sign of the writer's Riemann definition; no drift reading changes under either.

**Method:** Constants: $G = 6.67430\times10^{-11}\ \mathrm{m^3\,kg^{-1}\,s^{-2}}$, $c = 2.99792458\times10^8\ \mathrm{m\,s^{-1}}$, $GM_\oplus = 3.986004418\times10^{14}\ \mathrm{m^3\,s^{-2}}$, $GM_\odot = 1.32712440018\times10^{20}\ \mathrm{m^3\,s^{-2}}$, $R_\oplus = 6371\ \mathrm{km}$. Each scene supplies $E_{ij}$ already diagonal in the cabin's frame, with the first axis along the marked line. The frame equation is solved in closed form along each principal direction, so no integrator is needed and the readouts are exact for the stated model. The room the crumbs enclose is the product of the three half-axes, which reproduces the fourth-order vacuum loss to double precision. The tidal matrix is frozen at the release event; the design rule mark-the-frozen-matrix marks any state where the cabin's own fall would move $GM/r^3$ by more than one part in a hundred over the chosen clock. The gradient readouts come from the third-derivative formula, the curvature length from the closed form for the Schwarzschild exterior, and the plane readout from a single tidal entry.

| Test | State | Expect | Hidden | Note |
| --- | --- | --- | --- | --- |
| `earth-surface-ball-ten-seconds` | preset="earth-surface-ball", progress=1 | drift-along = 0.154143819991 ±1e-09; drift-across = -0.0770689400935 ±1e-09; drift-total = 5.93980442609e-06 ±1e-11; uniform-part = 1.9799348087e-06 ±1e-11; shape-part-along = 0.154141840057 ±1e-09; volume-change = -1.18790600689e-06 ±1e-12; along-to-across-ratio = -2.00007707131 ±1e-09; net-swirl = 0 ±1e-12 | independent-tide-numbers, plane-curvature-length, across-entry-change-outward, mixed-entry-change-sideways | The reference state. $a = GM/r^3 = 1.5413986\times10^{-6}\ \mathrm{s^{-2}}$ at Earth's surface, crumbs 1 m out, 10 s. The total is the fourth-order residue $La^2t^4/4$, four decimal places below the drifts, so the readout shows it as zero. |
| `at-the-moment-of-release` | preset="earth-surface-ball", progress=0 | drift-along = 0 ±1e-12; drift-across = 0 ±1e-12; drift-total = 0 ±1e-12; volume-change = 0 ±1e-12 | — | Boundary case: nothing has drifted at the instant the crumbs are let go, and the room is unchanged. |
| `twice-the-gap-twice-the-drift` | preset="earth-surface-ball", ball-radius=2, progress=1 | drift-along = 0.308287639983 ±1e-09; drift-across = -0.154137880187 ±1e-09; along-to-across-ratio = -2.00007707131 ±1e-09 | — | The equation is linear in the separation, so doubling the distance doubles every drift and leaves the ratio alone. |
| `small-ball-leading-order` | preset="earth-surface-ball", ball-radius=0.1, progress=1 | drift-along = 0.0154143819991 ±1e-10; volume-change = -1.18790600689e-06 ±1e-12 | — | Small-size limit: the drift falls to one tenth with the separation, while the fractional room change, which is a ratio, does not depend on the size at all. |
| `two-crumbs-across-two-metres-five-seconds` | preset="two-crumbs-across", ball-radius=2, clock="five-seconds", progress=1 | drift-across = -0.0385348412801 ±1e-09 | — | Two masses released at rest 2 m apart, side by side at Earth's surface, close by about 0.039 mm in 5 s, matching $\tfrac12(GM/r^3)t^2\times 2\ \mathrm{m}$. |
| `earth-orbit-gradients-match` | preset="earth-orbit-gradiometer", progress=1 | drift-along = 0.128406978991 ±1e-09; drift-across = -0.064201428531 ±1e-09; across-entry-change-outward = -3 ±1e-09; mixed-entry-change-sideways = -3 ±1e-09 | — | At $r = 6771\ \mathrm{km}$, $GM/r^3 = 1.2840423\times10^{-6}\ \mathrm{s^{-2}}$. Both gradients equal $-3\,GM/r^4$, the symmetry of $\partial_k\partial_j\partial_i\Phi$ that the contracted Bianchi identity carries in this limit. |
| `inside-a-rock-planet` | preset="inside-a-rock-planet", progress=1 | drift-along = -0.0768814316295 ±1e-09; drift-across = -0.0768814316295 ±1e-09; drift-total = -0.230644294889 ±1e-09; shape-part-along = 0 ±1e-12; along-to-across-ratio = 1 ±1e-12; volume-change = -0.0230626563079 ±1e-10 | across-entry-change-outward, mixed-entry-change-sideways | $4\pi G\rho/3 = 1.5376483\times10^{-6}\ \mathrm{s^{-2}}$ at $\rho = 5500\ \mathrm{kg\,m^{-3}}$. Three equal eigenvalues: the ball stays round, the leftover is exactly zero, and the room drops. |
| `dust-as-dense-as-water` | preset="dust-as-dense-as-water", progress=1 | drift-total = -0.000419358627157 ±1e-12; shape-part-along = 0 ±1e-12; volume-change = -4.19358568537e-05 ±1e-12 | — | A comoving cabin in dust of density $1000\ \mathrm{kg\,m^{-3}}$ after 1 s. The trace is $4\pi G\rho = 8.387\times10^{-7}\ \mathrm{s^{-2}}$, and the leftover is zero, so the Weyl part vanishes. |
| `racing-through-the-dust` | preset="moving-through-the-dust", progress=1 | drift-along = -0.000139786209052 ±1e-12; drift-across = -0.000375675422104 ±1e-12; drift-total = -0.00089113705326 ±1e-12; shape-part-along = 0.000157259475368 ±1e-12 | — | At $\beta = 0.6$, $\gamma^2 = 1.5625$, the trace becomes $4\pi G\rho(2\gamma^2 - 1) = 2.125$ times its comoving value, so the drift total is 2.125 times the comoving one. A dust universe is therefore not an Einstein space. |
| `dark-energy-universe-grows` | preset="dark-energy-universe", progress=1 | drift-along = 0.000279572437645 ±1e-12; drift-total = 0.000838717312934 ±1e-12; shape-part-along = 0 ±1e-12; along-to-across-ratio = 1 ±1e-12; volume-change = 8.38717547413e-05 ±1e-12 | — | Opposite sign of the trace: $p = -\rho_\Lambda c^2$ gives $E_{ii} = -8\pi G\rho_\Lambda$, so the ball grows in every direction. This covers the positive branch of every signed drift readout. |
| `far-from-every-mass-is-flat` | preset="far-from-every-mass", progress=1 | drift-along = 0 ±1e-12; drift-across = 0 ±1e-12; drift-total = 0 ±1e-12; shape-part-along = 0 ±1e-12; volume-change = 0 ±1e-12 | curvature-length, plane-curvature-length, along-to-across-ratio | Flat limit: every reading is zero. The ratio and both curvature lengths are undefined here and stay hidden. |
| `rocket-keeps-the-gap` | preset="rocket-cabin", progress=1 | drift-across = 0 ±1e-12; drift-total = 0 ±1e-12 | curvature-length, plane-curvature-length, along-to-across-ratio | A uniformly accelerating rocket far from every mass is flat: crumbs let go side by side keep their gap exactly. |
| `neutron-star-flyby` | preset="neutron-star-flyby", progress=1 | drift-along = 0.107523579624 ±1e-09; curvature-length = 10984.048143895 ±0.001 | — | $1.4\,M_\odot$ at $1200\ \mathrm{km}$: $GM/r^3 = 107.52\ \mathrm{s^{-2}}$, clock one thousandth of a second, crumbs 1 m out. |
| `black-hole-horizon-is-ordinary` | preset="black-hole-horizon", progress=1 | drift-along = 0.0514853758802 ±1e-09; curvature-length = 15.8734128898 ±0.0001 | — | A $10\,M_\odot$ hole has $GM/c^2 = 14.766\ \mathrm{km}$ and a horizon at $29.5325\ \mathrm{km}$; the cabin sits just outside, at $29.54\ \mathrm{km}$. The curvature length is about 15.9 km, comparable to the hole's size and entirely finite. |
| `twice-the-horizon-radius` | preset="black-hole-horizon", distance=59.08, progress=1 | curvature-length = 44.8967915798 ±0.0001; drift-along = 0.00643562366487 ±1e-11 | — | Doubling the distance multiplies the curvature length by $2^{3/2} = 2.8284$, so the invariant itself falls by $2^6 = 64$. |
| `passing-sideways-at-six-tenths-of-light` | preset="passing-sideways", progress=1 | drift-along = 0.284208828485 ±1e-09; drift-across = -0.207118286952 ±1e-09; along-to-across-ratio = -1.37220538402 ±1e-09; drift-total = 2.16014390819e-05 ±1e-10 | — | $\gamma^2 = 1.5625$: the entry along the marked line becomes $-\gamma^2(2+\beta^2) = -3.6875$ and the entry across the line and across the motion becomes $\gamma^2(1+2\beta^2) = 2.6875$, in units of $GM/r^3$, while the entry along the motion stays 1. The trace is still zero, so the drift total is again only the fourth-order residue. |
| `wave-at-the-peak-of-the-strain` | preset="gravitational-wave", progress=0.25 | drift-along = 50 ±1e-09; drift-across = -50 ±1e-09; drift-total = 0 ±1e-09; along-to-across-ratio = -1 ±1e-09; volume-change = -0.25 ±1e-09 | — | Strain 0.1, crumbs 1 m out, a quarter of the way through the wave's period. The stretch and the squeeze are half the strain each, so the area inside the ring holds to first order; the $-0.25$ percent loss of room is second order, $-h_+^2/4$. |
| `inside-the-falling-dust-cloud` | preset="dust-cloud-inside", progress=1 | drift-total = -0.230644294889 ±1e-09; shape-part-along = 0 ±1e-12 | — | Inside the uniform cloud the matrix is $4\pi G\rho/3$ times the identity whatever the cloud's radius, so the leftover is exactly zero: no shape change is made where the density is uniform. |
| `outside-the-falling-dust-cloud` | preset="dust-cloud-outside", progress=1 | shape-part-along = 0.0192206349799 ±1e-11; drift-total = 9.23578991063e-08 ±1e-13; along-to-across-ratio = -2.00000961032 ±1e-09 | — | Two cloud radii out the matrix is $(4\pi G\rho/3)f^{-3}\mathrm{diag}(-2,1,1)$ with $f = 2$. The leftover has switched on at the surface, where the density changes. |
| `four-cloud-radii-one-eighth` | preset="dust-cloud-outside", depth-in-cloud-radii=4, progress=1 | shape-part-along = 0.00240257600518 ±1e-12 | — | Twice as far gives one eighth: $0.0192206350/0.0024025760 = 8.0000$, the inverse-cube fall-off that the vacuum Weyl equation forces. |
| `no-swirl-with-the-course-table` | preset="tide-table-beside-earth", progress=1 | net-swirl = 0 ±1e-12; independent-tide-numbers = 6 ±0.5 | — | Pair exchange makes the tidal matrix symmetric, so the nine readings hold six different numbers and the net drift around the ring is exactly zero. |
| `the-invented-whirlpool-table` | preset="whirlpool-table-beside-earth", progress=1 | net-swirl = 0.0770699300507 ±1e-09; independent-tide-numbers = 9 ±0.5 | — | The invented antisymmetric piece of size $GM/r^3$ gives $\tfrac12 L a t^2 = 0.07707\ \mathrm{mm}$ of drift around the ring in 10 s and needs all nine numbers. No metric connection allows it. |
| `flipped-riemann-sign` | preset="flipped-riemann-sign", progress=1 | printed-mixed-component = 2 ±1e-12; printed-lowered-component = 2 ±1e-12; drift-along = 0.154143819991 ±1e-09 | — | $s_R = -1$ with the course signature flips both printed forms from $-2$ to $+2$, in units of $GM/c^2r^3$, and moves no crumb. |
| `flipped-signature` | preset="flipped-signature", progress=1 | printed-mixed-component = -2 ±1e-12; printed-lowered-component = 2 ±1e-12; drift-along = 0.154143819991 ±1e-09 | — | $s_g = -1$, $s_R = +1$: a Christoffel symbol is unchanged under $g \to -g$, so the mixed component keeps $-2$ while lowering one index brings a metric factor and flips the lowered one. Both signs of both printed readouts are covered by this test and the previous one. |
| `plane-of-fall-and-the-marked-line` | preset="plane-curvature-along", progress=1 | plane-curvature-length = 170745090 ±2 | — | $K = 2GM/(c^2r^3) = 3.4289\times10^{-23}\ \mathrm{m^{-2}}$, positive, so the signed curvature length is $+1.707\times10^8\ \mathrm{km}$ and the crumbs speed apart. |
| `plane-of-fall-and-a-line-across-it` | preset="plane-curvature-across", progress=1 | plane-curvature-length = -241470023 ±2 | — | $K = -GM/(c^2r^3)$, negative, so the crumbs speed toward each other. This test and the previous one cover both branches of the signed plane readout. |
| `a-minute-of-falling-beside-earth` | preset="earth-surface-ball", clock="one-minute", progress=1 | drift-along = 5.55416882736 ±1e-08; drift-total = 0.00769937155298 ±1e-10; volume-change = -0.00153731091713 ±1e-11 | — | Run the clock long enough and the fourth-order terms show. The room loss matches $-\tfrac12 a^2\tau^4 = -1.5396\times10^{-5}$ as a fraction, and the drift total, which is a different fourth-order combination, is positive. |

## Serves

- [[relativistic-tidal-tensor]]: the clock-face ring turning into an oval, the three principal drifts with their numbers, the slanted probe crumb, and the passing-sideways preset that changes the readings for a second cabin at the same event
- [[volume-preserving-tidal-deformation]]: the room meter beside the shape, the stretch and the two half-size squeezes that cancel, the rock-planet case that does shrink, and the shear-at-release and one-minute states that break the balance one hypothesis at a time
- [[ricci-tensor]]: the sum of the three drifts, read as the Ricci tensor fed the cabin's four-velocity twice, zero in vacuum and negative among dust
- [[weyl-tensor]]: the split of each drift into a same-in-every-direction part and a balanced leftover, with the leftover alone beside a planet and in a wave, and the uniform part alone among dust
- [[weyl-tensor-field-equation]]: the falling dust cloud, where the leftover is exactly zero inside the uniform dust, switches on at the surface, and falls as the inverse cube outside
- [[ricci-flat-spacetime]]: the two lamps, any drift at all and zero total, which separate Ricci-flat from flat across the planet, wave, dust and empty scenes
- [[einstein-space]]: the drifts and their total side by side as the cabin is moved and sped up: the total holds beside a body and in dark energy, and rises with speed in a dust universe
- [[einstein-tensor]]: the three drifts and their total labelled as the Ricci reading, so that the Einstein reading can be introduced as a different sum built from the same event
- [[geodesic-deviation-equation]]: the bar chart of the shrink in each second, whose extra is constant and proportional to the separation, divided by the separation to give one entry of the table
- [[newtonian-deviation-equation]]: the two-crumb mode with its exact gap, the scales that always read zero, and the separation slider that shows the drift in direct proportion to the gap
- [[deviation-vector]]: every drift measured against the centre crumb at one reading of the cabin clock, which is the orthogonal part of the deviation vector
- [[riemann-curvature-tensor]]: the drift divided by the separation, printed as an entry of the table, with presets from Earth to a neutron star and a black hole
- [[riemann-curvature-operator]]: the map from separations to relative accelerations that the crumbs trace out, with eigenvalues minus two, one and one in units of the tidal strength and a zero sum
- [[ricci-identity]]: the drift as the measured face of the swapped order of two covariant derivatives, read off one pair of crumbs
- [[riemann-tensor-in-normal-coordinates]]: the centre crumb held still against the cabin walls while the outer crumbs drift, showing what a falling frame removes and what it leaves
- [[symmetries-of-the-riemann-tensor]]: the three-by-three table with its mirror pairs lit together, the net drift around the ring held at zero, and the invented whirlpool table beside it
- [[number-of-independent-riemann-components]]: the counters: nine readings, six different numbers, six of the twenty entries of the full table
- [[bianchi-identity]]: the gradiometer grid, where the change of one entry moving out along the marked line matches the change of another moving sideways
- [[flatness-criterion]]: the windowless cabin switching between a speeding-up rocket and a fall beside a planet, where only the drift between two crumbs separates them
- [[integrability-condition-for-parallel-fields]]: the measured drift as the failure of a parallel four-velocity field: a switch to the flat scenes leaves the ball untouched, and no scene with drift allows one
- [[curvature]]: the spacetime version of the walker test: neighbours let go side by side draw together or spread apart, and a uniform pull in the rocket changes nothing
- [[curvature-sign-conventions]]: the convention toggle, which flips the printed components while every crumb and every drift reading stays exactly where it is
- [[sectional-curvature]]: the plane readout for the plane spanned by the cabin's four-velocity and the probe direction, positive where crumbs speed apart and negative where they draw together
- [[kretschmann-scalar]]: the curvature length beside the drift readings, growing sixty four times when the distance halves and staying entirely ordinary at a black hole's horizon
- [[weyl-criterion-for-conformal-flatness]]: the leftover reading beside a lamp for a scale-only map, which lights in the dust universe and never beside a planet

## In the visual network

- **Builds on:** [[two-walkers-set-off-side-by-side]], [[carry-an-arrow-around-a-loop]]
- **Leads to:** [[six-entry-curvature-table]], [[cube-of-small-loops]], [[three-gauges-on-a-falling-probe]]

## Accessibility

Every tour beat says where each crumb has drifted relative to the centre crumb, along or across the marked line, and gives the number in millimetres. The room meter, the drift total and the split into a uniform part and a leftover are all spoken as well as drawn. Drift arrows carry arrowheads and line styles that differ as well as colours, the two arrow sets in the split view are drawn apart rather than overlaid, and every control works from the keyboard.

Static alternative: In a cabin falling beside a planet, a ring of crumbs becomes an oval: crumbs on the line toward the planet's centre drift away from the centre crumb, crumbs across that line drift toward it, and a meter shows that the room the ring encloses has not changed. Inside a uniform planet the same ring shrinks and stays round. Far from every mass it does not change at all.

- `Space`: let the crumbs go, or pause the clock
- `Left and Right arrows`: scrub the cabin clock
- `Up and Down arrows`: move the cabin along the marked line
- `1 to 8`: choose the scene, from empty space beside a body to a passing wave
- `B`: switch between the ball, the clock-face ring and one pair of crumbs
- `S`: split each drift into a uniform part and a leftover
- `T`: show the three-by-three table of drifts
- `G`: read the table on a grid of neighbouring places
- `K`: show the curvature lengths
- `C`: cycle the printed sign conventions

## Starting material

Earlier course assets: `scene-3d-tidal-cloud`, `lab-tidal-cloud-geodesic-deviation`, `scene-3d-earth-free-fall-flow`, `scene-3d-gravitational-wave-rings`, `figure-tidal-eigenvalues`, `figure-ricci-weyl`, `lesson-what-a-tidal-instrument-measures`

The earlier course's tidal-cloud scene already integrates a released cloud near a mass and can be ported as a TypeScript module; its eigenvalue figure becomes the static card and its wave-ring scene becomes the plane-wave preset. New work: the closed-form solver with the frozen tidal matrix, the split into a uniform part and a leftover, the falling dust cloud with its surface, the tide table with the invented whirlpool, the gradiometer grid, the sign-convention toggle, and the preset-driven state that the tours and tests drive.

## Review: novice

**Verdict:** fixed (2026-09-16, revision 1)

**Retell attempt:** A cabin falls freely near Earth with nothing holding it up, and a set of scales in its corner reads zero the whole way down. Inside, twelve crumbs sit in a ring around one crumb in the middle, and a line runs from the cabin to Earth's centre through two of them. Let them all go with no push, and after ten seconds the ring is an oval: the crumbs on that line have drifted fifteen hundredths of a millimetre away from the middle crumb, and the crumbs across the line about half as far toward it. The arrows are drawn a thousand times too long, or I would see nothing at all. A crumb put on a slant drifts on a slant, because how far it sits from the middle crumb splits into a part along the line and a part across it. With a ball of crumbs instead of a ring, the ball becomes an egg and the room meter beside it does not move, because one stretch out and two squeezes in of half the size cancel. Count away from the middle crumb as plus and toward it as minus, add the three drifts, and the total is zero; that total is the number that says whether the room starts to change. Inside a planet of rock every crumb drifts in by the same amount, so the ball stays round and shrinks, and dust filling the space does the same. Far from every mass nothing drifts at all, so a zero total is not the same as nothing happening. Each drift splits into a part that is the same in every direction and a leftover that balances: beside Earth the first reads zero and the leftover makes the egg, in dust it is the other way round, and a passing gravitational wave behaves like Earth with no matter anywhere. In a rocket speeding up, two crumbs let go side by side land the same distance apart, while beside a planet the gap closes by seven hundredths of a millimetre in ten seconds, and that drift, not the pull toward the floor, is the test for curved spacetime. The gap closes faster and faster by the same extra each second, twice the gap gives twice the extra, and the extra divided by the gap is a number belonging to the place. A tide meter with three arms gives nine readings holding six different numbers, because mirror pairs always match; an invented table that broke that rule would carry the crumbs round the ring for free. The full table has twenty numbers, so one falling cabin reads six and misses fourteen. Things I could not follow: where twenty comes from, whether the middle crumb and the centre crumb are the same crumb, what the marked line is called before the readings use the name, and how crumbs can pass through solid rock.

- Stumble: “Inside I hold twelve crumbs in a ring, around one more crumb at the centre. A line is drawn from the cabin to Earth's centre.”: The word centre does two jobs in two sentences, the crumb in the middle and Earth's centre, and the name centre crumb is never given before the readings use it.
- Stumble: “The two crumbs on the marked line drift away from the centre crumb.”: The marked line is spoken as a known thing, but no beat ever says that the line drawn to Earth's centre is the one called the marked line.
- Stumble: “The scales in the corner read zero.”: Scales that read zero: zero of what? The instrument is never named until a much later tour calls them bathroom scales.
- Stumble: “The crumbs across the line drift in toward it.”: Toward it could be toward the line or toward the centre crumb, and those are different journeys.
- Stumble: “so that you can see it at all”: It stands for every drift arrow, which was plural in the same sentence.
- Stumble: “The crumb on the marked line has drifted fifteen hundredths of a millimetre away from the centre crumb.”: There are two crumbs on the marked line on screen, and a design rule insists both are drawn, so the crumb made me hunt for which one.
- Stumble: “Now I move one crumb off both lines, so that it sits on a slant.”: Only one line has been drawn and named; the second line has no reference at all.
- Stumble: “Its place splits into a part along the marked line and a part across it.”: A place does not split; what splits is how far the crumb sits from the centre crumb.
- Stumble: “Three numbers give the drift of a crumb placed anywhere near the centre crumb.”: I had seen two readings, along and across, so three arrived with nothing behind it.
- Stumble: “The crumbs pass through the rock freely.”: Stated as a fact about crumbs, this is a rule I cannot carry out; it needs to be offered as something we imagine.
- Stumble: “This time the crumbs sit on a small ball around the centre crumb.”: Sit on a small ball made me look for a ball object for them to rest on, when the crumbs are the ball.
- Stumble: “Each of the two squeezes across it is about half that, and there are two of them.”: The sentence counts the two squeezes twice, so I lost track of how many there were.
- Stumble: “One stretch and two half squeezes cancel.”: Half squeezes sounds like a squeeze that half happened; and the arithmetic that makes them cancel is never said.
- Stumble: “Every crumb drifts inward by the same amount. Nothing cancels, and the room meter drops. Mass inside the ball is what makes the room start to change.”: Inward has no reference here, and the ball could be the ball of crumbs or the planet; mass also arrives as a second word for matter.
- Stumble: “One is along the marked line, and it goes outward. Two are across the line, and they go inward.”: Outward and inward have no reference: out from the centre crumb, or out from Earth?
- Stumble: “That one number is what the Ricci table holds”: Ricci sounded like a kind of table rather than the name of the person it is named after.
- Stumble: “Denser dust makes the total bigger.”: The total here is an inward total, and the readout speaks it as a number inward, so bigger sounds like it is climbing back toward zero.
- Stumble: “The first piece is the same in every direction, all outward or all inward.”: Outward and inward again have no reference.
- Stumble: “No matter sits where the crumbs are, and it is still there.”: It could be the matter, which would be the opposite of what the line means.
- Stumble: “the two readings swap places”: I looked for the two numbers to change position on the panel.
- Stumble: “The ring stretches one way across the wave and squeezes the other way by the same amount.”: Across the wave gives no reference I can see; the wave is not drawn as a thing with a width.
- Stumble: “Start far from every mass, with the engines off. No crumb drifts at all.”: Two lamps are on screen in this beat and nothing is said about them until two beats later.
- Stumble: “Beside a planet the three drifts add up to zero. Does that mean spacetime beside the planet is flat?”: This tour has only shown me a cabin where nothing drifts, so I could not tell whether adding to zero meant each drift was zero.
- Stumble: “Beside the planet the first lamp is lit and the second is lit.”: The and-the-second-is-lit shape sounds like a contrast is coming, and then both say the same thing.
- Stumble: “A pull that makes everything fall the same way does not bend spacetime.”: Everywhere else the word is curve or curving; bend is a second word for the same idea, and bending is what a tube does without being curved.
- Stumble: “That drift is the test for curved spacetime, and the pull on the floor is not.”: The pull on the floor sounds like something pulling the floor; what was meant is the pull toward the floor.
- Stumble: “The table that records the drift is zero over a region exactly when that region is flat.”: Exactly when reads as at the very moment when, and is zero over a region is hard to picture.
- Stumble: “One thing on its own tells us nothing.”: Tells us nothing about what? The scales did tell me the cabin is falling freely.
- Stumble: “What happens to the extra amount each second?”: The extra was never named; the bars were only described as taller by the same amount.
- Stumble: “Our cabin falls with the dust, halfway out from the centre.”: Which centre: the cloud's centre or the centre crumb?
- Stumble: “The leftover reading is exactly zero, so the shape does not change at all.”: This tour never says what the leftover is, so the reading meant nothing to me.
- Stumble: “Crossing the surface switches it on.”: It opens the beat with nothing before it to stand for, and which surface is not said.
- Stumble: “Now I take the cabin twice as far out again. ... Empty space cannot make it or destroy it. Each layer of empty space only hands it on”: Again made me think we had already doubled once from here, and three its in two sentences all stand for something unnamed.
- Stumble: “Each reading says how far a crumb out along one arm drifts along another. Pairs that mirror each other light up together, and they always match.”: Drifts along another arm is a direction with no reference, and which readings mirror each other is shown only by two matching colours, which I cannot use if I cannot tell the colours apart.
- Stumble: “Of two crumbs out along directions at right angles, each drifts toward the other's direction by the same amount.”: One sentence carrying two crumbs, two directions and a comparison; I had to read it three times.
- Stumble: “Nothing would be paying for that.”: Paying with what? The money picture hid the point that energy would be coming from nowhere.
- Stumble: “Of those nine readings, how many are really different numbers, and does the meter catch all the curving at that place?”: Nothing I had seen in this tour could tell me whether the meter catches everything, so the second half was not a prediction I could make.
- Stumble: “The mirror rule ties the readings in pairs, so nine readings hold six different numbers. And the full table for space and time holds twenty numbers.”: This tour never states the mirror rule before using it, and twenty arrives with no count behind it.
- Stumble: “the centre crumb hangs still against its walls ... At the centre of this room”: Its walls sounds like the crumb's walls, and centre is doing a third job here.
- Stumble: “the three drifts add up to {value} millimetres outward”: Beside Earth this total is zero, and zero millimetres outward sounds like a direction that is not there.
- Stumble: “the same-in-every-direction part is {value} millimetres outward”: In the beat that matters most this part reads zero, and zero millimetres outward sounds wrong.
- Stumble: “the crumbs have been carried {abs} millimetres around the ring toward rising clock numbers”: This reading is held at zero almost always, and being carried zero millimetres toward rising clock numbers sounds like something happened.
- Stumble: “the drift along the marked line is {abs} times the drift across it, the other way”: The other way from what? I could not tell whether the drift or the line had turned.
- Stumble: “Inside a uniform planet the crumbs pass through”: Read as a control label it sounds like a planet that the crumbs pass through, and it stops mid-thought.
- Stumble: “Let the crumbs go with a shear”: Shear is a word I have not met and the label does not say what it does.
- Stumble: “a meter shows that the room it takes up has not changed”: It could be the ring, the oval or the cabin.
- Fixed: Named the centre crumb and the marked line where they are first drawn, and repeated the marked line's meaning in the opening beat of the egg, the total, the split and the two-crumb tours so each stands on its own.
- Fixed: Gave every direction its reference: outward and inward now say away from or toward the centre crumb, across the wave became across the wave's path, and the cloud's centre is named as the cloud's.
- Fixed: Replaced pronouns whose noun was not unmistakable: it for the arrows, for the leftover, for the shape change and for the matter.
- Fixed: Turned the crumbs passing through rock into something we imagine, rather than a fact stated about crumbs.
- Fixed: Made the cancelling arithmetic explicit: one stretch out and two squeezes in of half that size add up to nothing.
- Fixed: Named Ricci and Weyl as the people the tables are named after.
- Fixed: Changed bend spacetime to curve spacetime, keeping one word for one idea, and the pull on the floor to the pull toward the floor.
- Fixed: Rewrote the flatness sentence so that exactly when reads as a condition and not as a moment in time.
- Fixed: Named the extra before the prediction that asks about it, and stated the mirror rule inside the tours that use it.
- Fixed: Supplied the missing fact in the Ricci-flat prediction, that none of the three drifts is zero beside a planet, so the guess can be made from the tour.
- Fixed: Marked the counting question about all the curving as a guess rather than a prediction.
- Fixed: Named the counter as the source of the twenty, instead of asserting the number out of nowhere.
- Fixed: Reworded the readouts that are usually zero, the drift total, the same-in-every-direction part and the net drift around the ring, so the spoken line reads correctly at zero.
- Fixed: Made the ratio readout say that the two drifts go the same way or opposite ways, instead of the same way or the other way.
- Fixed: Spelled out the mirror pairs in words in the tide-table beat and its description, so the pairing does not depend on colour alone.
- Fixed: Fixed two control labels, the inside-a-planet scene and the shear release, and the picture caption's floating it.
- Concern: Tour ricci-flat-is-not-flat, beat the-cabin-where-nothing-drifts: the show line says both lamps are off far from every mass, but the second lamp is defined two beats later as whether the three drifts add to zero, and three zero drifts do add to zero. Either that lamp's test or the beat's lamp state needs changing; I left both alone.
- Concern: Tour rocket-or-planet, beat a-windowless-cabin: Everything falls to the floor in both is not what I see beside the planet, where the cabin is in free fall and the crumbs float with it. The claim needs either a cabin held at rest on the planet or a different sentence; I did not touch it.
- Concern: The design rule scales-always-read-zero cannot hold in the rocket scene, where the cabin is speeding up and a set of scales would read the push. The rocket preset needs its own rule for what the scales show, and the tours say nothing about it.
- Concern: The tide table's mirror pairs are lit in matching colours only. The words now name each pair, but the drawing still needs a second cue, a matching letter or frame, and a design rule to hold it.
- Concern: The entry ways of relativistic-tidal-tensor and ricci-flat-spacetime call it the middle crumb, while this visual and every other served note say centre crumb. I kept centre crumb because it is what the catalogue uses, but one word should win, and centre also has to serve the planet's centre.
- Concern: The dust-universe and dark-energy presets use a thousand kilograms in every cubic metre, as dense as water. No spoken line scopes this, so a learner can carry it away as the density of our universe.
- Concern: Tour six-numbers-of-twenty: twenty arrives with no count a sixteen-year-old could follow. The beat now attributes it to the counter on screen, but the number still has no reason behind it at this rung.
- Concern: The entry tours never say what a gravitational wave is before the wave scene runs, in either the split-the-drift tour or the Ricci-flat tour.
