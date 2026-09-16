---
type: "visual"
schema_version: 2
id: "best-fit-circle-along-a-bend"
title: "Best-fit circle along a bend"
kind: "interactive-3d"
priority: "flagship"
status: "specified"
revision: 4
rungs: ["entry", "working"]
serves: ["curvature-of-a-curve", "frenet-serret-equations", "intrinsic-versus-extrinsic-curvature"]
builds_on: []
leads_to: ["bend-arrow-split-on-a-surface", "card-touching-a-curved-patch", "paper-rolled-into-a-tube-and-a-cone"]
---

# Best-fit circle along a bend

`best-fit-circle-along-a-bend` · interactive-3d · flagship · specified · rungs: entry, working

> Walk along a bend and watch the circle that matches it best: the sharper the bend, the smaller that circle.

## What it makes visible

A bend has a size you can measure: the degrees your direction of travel turns for every metre along the path. One circle matches the bend best at each place, and the sharper the bend, the smaller that circle. Its radius is one divided by the turning rate, with that rate counted in radians per metre rather than degrees per metre. A second reading, how many degrees the sheet holding that circle tips for every metre, separates a wavy line drawn on a page from a spring that climbs out of it, and the two readings together rebuild the path. Painted dots on the wire keep their spacings while the wire is pulled straight, so every reading here belongs to the room around the wire and none of it to measurements made along it.

## The picture

A wire or path floats in a lightly shaded room with a faint floor grid. A walking marker rides along it. The best-fit circle is drawn in the room's space in orange, touching the path at the marker, with its radius drawn as a thin spoke to its centre. A translucent card, shown on request, fills the sheet that holds that circle; three short sticks, also on request, ride the marker as the direction of travel, the direction toward the inner side of the bend, and a third at right angles to both. Two painted dots sit on the wire a fixed distance apart along it, with a tape between them. A dial panel reads the turn per metre and the tip per metre, and totals for the whole walk appear when the walk finishes.

| Element | Shows |
| --- | --- |
| The path or wire, drawn as a solid dark line | the curve being measured: a ring, a graph, a wavy line on a page, a coil, or a drawn path |
| Orange best-fit circle with a thin spoke to its centre | the circle that matches the bend at the marker, and its radius |
| Translucent card through the best-fit circle | the sheet the bend lies in, whose tipping is the second reading |
| Three short sticks riding the marker | the frame carried along the path: ahead, toward the inner side of the bend, and a third at right angles to both |
| Two painted dots with a tape laid along the wire between them | the only measurement a creature living on the wire can make |
| Dial panel: turn per metre, tip per metre, best-fit radius, totals for the whole walk | the numbers that name the bend, with the totals held back until the walk finishes |

## Book figure

Three panels. Left: a wavy line on a page with the best-fit circle drawn at a crest, small, and a note at the straight spot where no circle fits. Middle: a coil, with the same circle plus the translucent card tipping between two marked places along it. Right: the same wavy wire pulled straight, the two painted dots still the same distance apart along the tape, and the circle gone.

Labels: best-fit circle, radius, straight spot, no circle, card through the bend, card tipped, painted dots, same spacing. Aspect 3:1. Alt text: A wavy line with a small circle matching one of its bends, a coil whose bend-sheet tips as it climbs, and the same wire pulled straight with its painted dots still the same distance apart.

## Variants

- **static** `static-card` (fallback): The print figure as an SVG card, used when 3D is unavailable and as a summary card.
- **interactive-2d** `plane-curves-2d`: A flat panel with the ring, the graph and the wavy line only, where the best-fit circle rides the path and the tip reading is always zero.
- **interactive-3d** `full-3d`: The full experience: every path shape, the card and the three sticks, reversal, mirroring, the straightening slider, and the rebuild mode driven by the two dials.

## Parameters

| Id | Label | Type | Options or range | Default | Available when | Effect |
| --- | --- | --- | --- | --- | --- | --- |
| `path-shape` | Path | enum | circle, wiggle, parabola, helix, straight, rebuilt, drawn | "circle" | — | Chooses the path. The straight wire is 1 metre long. The graph is $y = x^2/L_0$ with $L_0 = 1$ metre, drawn over $-2\,\text{m} \le x \le 2\,\text{m}$. |
| `circle-length` | Distance once round the ring | number | 10–600 step 10 m | 60 | path-shape in circle | The length of one lap. The ring's radius is this length divided by two pi, and its turn per metre is 360 degrees divided by this length. |
| `helix-radius` | Coil radius | number | 0.5–50 step 0.5 m | 15 | path-shape in helix | The radius of the cylinder the coil winds around. |
| `helix-rise` | Climb per turn | number | 0–20 step 0.5 m | 3 | path-shape in helix | How far the coil climbs in one full turn. Zero gives a flat ring, whose tip reading is exactly zero. |
| `helix-turns` | Number of turns | integer | 1–6 step 1 | 2 | path-shape in helix | How many full turns of the coil are drawn; it sets the path length and both totals. |
| `handedness` | Which way the coil winds | enum | right-handed, left-handed | "right-handed" | path-shape in helix | Mirrors the coil. The turn per metre is unchanged and the tip per metre changes sign, as does the climb per turn readout. |
| `wiggle-height` | Height of the waves | number | 0.05–1 step 0.05 m | 0.1 | path-shape in wiggle | The wavy line is $y = A\cos(2\pi x/\lambda)$ in the page, with $A$ this height. |
| `wiggle-spacing` | Length of one wave | number | 0.5–4 step 0.5 m | 1 | path-shape in wiggle | The wavelength $\lambda$; exactly two waves are drawn, so the marker sits on a crest or a trough at each quarter of the walk. |
| `built-turn-per-metre` | Turn per metre to build with | number | 0.01–120 step 0.01 deg/m | 3.82 | path-shape in rebuilt | Held constant along the built path. |
| `built-tip-per-metre` | Tip per metre to build with | number | -60–60 step 0.01 deg/m | 0.12 | path-shape in rebuilt | Held constant along the built path. Its sign decides which way the built coil winds. |
| `built-length` | Length to build | number | 1–400 step 1 m | 100 | path-shape in rebuilt | How much path is built from the two dial settings. |
| `walk-direction` | Which way to walk | enum | forward, backward | "forward" | — | Walks the same shape the other way. The ahead stick and the third stick both flip; the turn and tip readings are unchanged. |
| `straighten` | Pull straight | number | 0–1 step 0.01 | 0 | path-shape in circle, wiggle, parabola, helix, drawn | Scales the turn per metre and the tip per metre by one minus this fraction, rebuilding the wire at the same arc length. Every spacing measured along the wire is unchanged; 1 gives a straight wire. A closed ring opens into an arc as it straightens. |
| `overlay` | What to draw at the walker | enum | none, circle-only, with-plane, with-frame | "circle-only" | — | Chooses what is drawn at the walker. Just the path draws nothing there; the other settings add the best-fit circle, the card that fills the sheet of the bend, and the three sticks carried along the path. |
| `progress` | Walk progress | progress | 0–1 step 0.001 | 0 | — | Moves the marker along the path. It is the fraction of the length walked for every shape except the graph, where it is the fraction of the drawn span in $x$, so $x = -2\,\text{m} + 4\,\text{m}\times{}$progress. Totals for the whole walk appear only at 1. |
| `path` | Drawn path | path | — | null | path-shape in drawn | Control points of a path drawn by the learner. |

## Presets

- `pond-ring` Ring around a pond, 60 metres round: path-shape="circle", circle-length=60
- `lake-ring` Ring around a lake, 300 metres round: path-shape="circle", circle-length=300
- `tight-ring` Tightest ring this demo allows: path-shape="circle", circle-length=10
- `parabola-graph` Graph of a squared law: path-shape="parabola"
- `wiggle-on-a-page` Wavy line on a page: path-shape="wiggle", wiggle-height=0.1, wiggle-spacing=1
- `wire-pulled-straight` The same wavy wire, pulled straight: path-shape="wiggle", wiggle-height=0.1, wiggle-spacing=1, straighten=1
- `straight-wire` Straight wire, 1 metre long: path-shape="straight"
- `spiral-ramp` Spiral ramp: 15 metres from its centre, climbing 3 metres a turn: path-shape="helix", helix-radius=15, helix-rise=3, helix-turns=2, handedness="right-handed"
- `mirror-ramp` Mirror image of the spiral ramp: path-shape="helix", helix-radius=15, helix-rise=3, helix-turns=2, handedness="left-handed"
- `flat-ring-spring` Coil with no climb at all: path-shape="helix", helix-radius=15, helix-rise=0, helix-turns=1, handedness="right-handed"
- `rebuilt-ramp` Path built from the ramp's two readings: path-shape="rebuilt", built-turn-per-metre=3.82, built-tip-per-metre=0.12, built-length=100
- `rebuilt-mirror-ramp` The same build with the tip reversed: path-shape="rebuilt", built-turn-per-metre=3.82, built-tip-per-metre=-0.12, built-length=100

## Readouts

- `turn-per-metre` Turn per metre (deg/m; visible always; 3 decimals): “my direction of travel turns {value} degrees for every metre along the path here”
- `radius-of-curvature` Radius of the best-fit circle (m; visible always; 4 decimals): “the circle that matches this bend best has a radius of {value} metres”
- `tip-per-metre` Tip per metre (deg/m; visible always; 4 decimals; range (-3600, 3600]; sense: positive when the path winds like an ordinary right-handed screw thread, so the card tips toward the side the third stick points to): “the card holding this bend tips {abs} degrees for every metre, counted the way an ordinary screw thread winds” / “the card holding this bend tips {abs} degrees for every metre, counted the way the mirror image of an ordinary screw thread winds”
- `total-turn` Total turn over the whole walk (deg; visible on-complete; 2 decimals; range (0, 48000]): “walking the whole path turned my direction of travel {value} degrees in total”
- `total-tip` Total tip over the whole walk (deg; visible on-complete; 2 decimals; range (-24000, 24000]; sense: positive when the card tips the way an ordinary right-handed screw thread winds): “over the whole path the card tipped {abs} degrees, counted the way an ordinary screw thread winds” / “over the whole path the card tipped {abs} degrees, counted the way the mirror image of an ordinary screw thread winds”
- `dot-spacing` Distance between the painted dots, along the wire (m; visible always; 3 decimals): “the tape laid along the wire reads {value} metres between the two painted dots”
- `path-length` Length of the path (m; visible always; 4 decimals): “the path is {value} metres long”
- `coil-radius` Radius of the coil (m; visible on-demand; 4 decimals): “the coil winds around a cylinder of radius {value} metres”
- `rise-per-turn` Climb per full turn (m; visible on-demand; 4 decimals; range (-18000, 18000]; sense: positive when the coil winds like an ordinary right-handed screw thread): “the coil climbs {abs} metres in one full turn, counted the way an ordinary screw thread winds” / “the coil climbs {abs} metres in one full turn, counted the way the mirror image of an ordinary screw thread winds”
- `graph-slope` Slope of the graph at the walker (no unit; visible on-demand; 3 decimals; range (-100, 100]; sense: positive where the graph climbs toward larger values along the horizontal axis): “the graph climbs {abs} metres for every metre along the horizontal axis here” / “the graph falls {abs} metres for every metre along the horizontal axis here”

## Tours

### `measure-a-bend` · for [[curvature-of-a-curve]] · entry

1. `meet-the-pond-path` (entry, await none) state: preset="pond-ring", progress=0, overlay="none"  
   *A round path around a pond, 60 metres long, with the walking marker at the start and nothing drawn at the walker; the best-fit circle is held back until the wavy wire, where it plainly sits off the path.*  
   Say: “Here is a path that runs once around a pond and comes back to its start. It is sixty metres long. A walker sets off along it. A dial reads how many degrees her direction of travel turns for every metre she walks. Right now it reads six degrees for every metre.”  
   Describe: A round path around a pond, sixty metres long. A walker stands at its start. A dial beside her reads six degrees for every metre.
2. `predict-the-lake-path` (entry, await prediction) state: preset="pond-ring", progress=0, overlay="none"; evidences `curvature-of-a-curve/checks/two-round-paths`  
   *Same view, paused, with no circle drawn and the lake path shown small beside the pond path for comparison.*  
   Predict: “A second round path runs around a lake, and it is three hundred metres long. That is five times the pond path. Will its dial read more degrees for every metre, or fewer?”  
   Say: “Before I walk, make a guess. A second round path runs around a lake, and it is three hundred metres long. That is five times the pond path. Will its dial read more degrees for every metre, or fewer?”  
   Describe: The walker waits at the start of the pond path. A larger round path, the lake path, waits beside it.
3. `walk-the-pond-path` (entry, await none) state: preset="pond-ring", progress=0, overlay="none"; animate progress → 1 over 6 s  
   *The marker goes once around the pond path with no circle drawn; the dial holds at 6 and the total turn reads 360 degrees at the end.*  
   Say: “The walker goes once around the pond path. The dial holds at six degrees for every metre the whole way, because every part of a round path bends alike. One lap brings her back facing the way she set off, so her direction of travel turned all the way round. The total reads three hundred and sixty degrees.”  
   Describe: The walker travels once around the pond path. Her dial holds at six degrees for every metre. At the end, a total of three hundred and sixty degrees appears.
4. `walk-the-lake-path` (entry, await none) state: preset="lake-ring", progress=1, overlay="none"  
   *The lake path walked to the end with no circle drawn; the dial reads 1.2 and the total turn again reads 360 degrees.*  
   Say: “Now the lake path. Its dial reads one point two degrees for every metre. One lap turns her all the way round again, three hundred and sixty degrees. But she walks five times as far to do it. So the pond path bends five times as sharply as the lake path.”  
   Describe: The walker has gone once around the lake path. Her dial reads one point two degrees for every metre, and her total is again three hundred and sixty degrees.
5. `the-circle-that-fits` (entry, await none) state: preset="wiggle-on-a-page", progress=0  
   *A wavy wire on a page, marker at a crest, with the orange best-fit circle touching it there and a spoke drawn to the circle's centre.*  
   Say: “Here is a wavy wire instead, lying on a page. Its bends are not all alike. At the place the walker stands, one circle matches the bend best. It touches the wire there, runs the same way the wire runs there, and bends just as sharply. This one is small: the orange spoke from the wire to the circle’s centre is about twenty five centimetres long.”  
   Describe: A wavy wire on a page. At a crest of the wave, a small orange circle touches the wire, with a spoke of about twenty five centimetres drawn to the circle’s centre.
6. `where-the-wire-runs-straight` (entry, await none) state: preset="wiggle-on-a-page", progress=0.125  
   *Marker at the inflection of the wavy wire; the dial reads 0 and the circle and its radius readout are blank.*  
   Say: “The walker moves on to one point where the wire is not bending at all. The dial falls to zero degrees for every metre. No circle matches a wire that is not bending, so the orange circle and its spoke go blank here.”  
   Describe: The walker reaches the one point on the wavy wire where it is not bending at all. Her dial reads zero degrees for every metre, and no circle is drawn.

### `turning-rate-from-a-formula` · for [[curvature-of-a-curve]] · working

1. `the-graph-at-its-lowest-point` (working, await none) state: preset="parabola-graph", progress=0.5  
   *The graph of y equals x squared over one metre, marker at the vertex, best-fit circle of radius 0.5 m drawn there.*  
   Say: “Here is the graph of y equals x squared over one metre, walked toward larger x. At the lowest point the graph is level: the slope readout shows zero. The dial reads about one hundred and fourteen point five nine degrees per metre, and the best-fit circle has radius zero point five metres. That radius is exactly one over the second derivative, which is two per metre.”  
   Describe: A parabola drawn in a vertical plane, with the walker at its lowest point and a small circle of radius half a metre matching the bend there.
2. `predict-at-one-metre` (working, await prediction) state: preset="parabola-graph", progress=0.5; evidences `curvature-of-a-curve/checks/parabola-at-x-equals-one`  
   *Same view, paused, with the marker about to move to x equals one metre.*  
   Predict: “The second derivative of this graph is two per metre everywhere. At x equals one metre, will the best-fit circle still have radius zero point five metres?”  
   Say: “Here is a prediction to make. The second derivative of this graph is two per metre everywhere, at every value of x. At x equals one metre, will the best-fit circle still have radius zero point five metres?”  
   Describe: The walker waits at the lowest point of the parabola, about to move out to where x is one metre.
3. `the-slope-spoils-the-shortcut` (working, await none) state: preset="parabola-graph", progress=0.5; animate progress → 0.75 over 3 s  
   *Marker moving out to x equals one metre; slope readout 2, dial 10.249 degrees per metre, best-fit circle of radius 5.5902 m.*  
   Say: “At x equals one metre the slope readout shows two, and the dial reads about ten point two five degrees per metre. The best-fit circle has a radius of about five point five nine metres, more than eleven times the radius at the lowest point. The second derivative has not changed at all. So the second derivative on its own is not the turn per metre: divide it by one plus the slope squared, raised to the power three halves.”  
   Describe: The walker sits where x is one metre. The graph slopes at two there, and the matching circle is now more than eleven times as wide as at the lowest point.
4. `the-whole-drawn-span` (working, await none) state: preset="parabola-graph", progress=0.75; animate progress → 1 over 4 s  
   *Marker at the far end of the drawn span; totals appear: total turn 151.93 degrees, total tip 0, path length 9.2936 m.*  
   Say: “Walking the whole drawn span, from x equals minus two metres to x equals two metres, turns the direction of travel one hundred and fifty one point nine three degrees in total. The path is nine point two nine metres long. The total tip reads zero, because the graph lies in one flat sheet from end to end.”  
   Describe: The walker has reached the far end of the drawn parabola. The total turn reads about one hundred and fifty two degrees, the total tip reads zero, and the path is about nine point three metres long.

### `the-sheet-a-bend-lies-in` · for [[frenet-serret-equations]] · entry

1. `a-card-on-a-wavy-wire` (entry, await none) state: preset="wiggle-on-a-page", progress=0, overlay="with-plane"  
   *Wavy wire on a page with the translucent card drawn through the best-fit circle at the marker, lying flat on the page.*  
   Say: “The wavy wire lies flat on a page. A small card sits in the sheet that fits the bend where the walker stands, the same flat sheet that holds the orange best-fit circle. Watch whether that card ever tips as she slides along the wire. A second dial reads how many degrees the card tips for every metre.”  
   Describe: A wavy wire on a page, with a small flat card held in the sheet of the bend at the walker. A second dial reads the tip for every metre.
2. `predict-which-one-tips` (entry, await prediction) state: preset="wiggle-on-a-page", progress=0, overlay="with-plane"; evidences `frenet-serret-equations/checks/wiggle-on-a-page`  
   *Same view, paused, with the coil shown small beside the page for comparison.*  
   Predict: “The wavy wire bends sharply. A spring beside it climbs gently, and its bends are much softer. Which of the two tips its card as you slide along, the wavy wire or the spring?”  
   Say: “Make a guess first. The wavy wire bends sharply. A spring beside it climbs gently, and its bends are much softer. Which of the two tips its card as you slide along, the wavy wire or the spring?”  
   Describe: The walker waits on the wavy wire with her card. A gently climbing spring waits beside the page.
3. `slide-along-the-wavy-wire` (entry, await none) state: preset="wiggle-on-a-page", progress=0, overlay="with-plane"; animate progress → 1 over 6 s  
   *The marker slides the whole wavy wire; the card stays in the page and the tip dial holds at 0, while the turn dial swings up and down.*  
   Say: “The walker slides along the whole wavy wire. The turn dial swings up at every crest and falls to zero at every straight spot. The card stays flat on the page the whole way. Its tip dial holds at zero degrees for every metre. Sharp bends drawn on a flat page do not tip the card at all.”  
   Describe: The walker slides along the wavy wire. Her turn dial rises and falls, while the card stays in the page and the tip dial holds at zero.
4. `slide-along-the-spring` (entry, await none) state: preset="spiral-ramp", progress=0, overlay="with-plane"; animate progress → 1 over 7 s  
   *The marker slides along two turns of the coil; the card tips steadily and the tip dial holds at 0.1215 degrees per metre, with a total tip of 22.91 degrees at the end.*  
   Say: “Now a spring that climbs three metres in one full turn. Its bends are gentler than the wavy wire's: the turn dial reads about three point eight two degrees for every metre. Yet the card tips a little at every step, because the spring keeps climbing out of the sheet that fits each bend. The tip dial holds at about zero point one two degrees for every metre. Over the whole spring the card tipped twenty two point nine one degrees.”  
   Describe: The walker slides along a spring that climbs as it winds. Her card tips steadily, reading about zero point one two degrees for every metre, and tips almost twenty three degrees over the whole spring.

### `two-turns-of-the-frame` · for [[frenet-serret-equations]] · working

1. `three-sticks-on-the-ramp` (working, await none) state: preset="spiral-ramp", progress=0.5, overlay="with-frame"  
   *The coil with the three sticks and the card drawn at the marker; dials read 3.816 and 0.1215 degrees per metre.*  
   Say: “Three sticks ride the spiral ramp. The first points along the direction of travel. The second points toward the inner side of the bend, in the sheet of the card. The third stands at right angles to both, picked by the right-hand rule. The frame turns around the third stick at the turn per metre, the three point eight one six degrees the dial shows. It tips around the first stick at the tip per metre, the zero point one two one five degrees beside it.”  
   Describe: A coil of radius fifteen metres climbing three metres a turn, with three short sticks at right angles riding with the walker and a card through the bend.
2. `predict-four-metres-along` (working, await prediction) state: preset="spiral-ramp", progress=0.5, overlay="with-frame"; evidences `frenet-serret-equations/checks/spiral-ramp`  
   *Same view, paused, with a four metre stretch of the ramp highlighted ahead of the marker.*  
   Predict: “Both dials hold the same reading everywhere on this ramp. Over four metres along it, how many degrees does the direction of travel turn, and how many degrees does the card tip?”  
   Say: “Both dials hold the same reading everywhere on this ramp. Over four metres along it, how many degrees does the direction of travel turn, and how many degrees does the card tip?”  
   Describe: The walker waits halfway along the coil, with a four metre stretch of ramp marked ahead of it.
3. `predict-the-reversal` (working, await prediction) state: preset="spiral-ramp", progress=0.5, overlay="with-frame"; evidences `frenet-serret-equations/checks/walk-the-helix-backwards`  
   *Same view, paused, with the walking direction control highlighted.*  
   Predict: “I now walk the same ramp from its far end instead. Does the tip per metre change sign?”  
   Say: “One more prediction. I now walk the same ramp from its far end instead, along the identical coil. Does the tip per metre change sign?”  
   Describe: The walker waits halfway along the coil. The control that reverses the walk is highlighted.
4. `walk-the-ramp-backwards` (working, await none) state: preset="spiral-ramp", walk-direction="backward", progress=0.5, overlay="with-frame"  
   *The same coil walked from the far end; the first and third sticks have flipped, the second is unchanged, and both dials read as before.*  
   Say: “Walking from the far end flips the first stick, and the third stick flips with it, because the third is the first crossed into the second. The second stick is unchanged: the direction of travel still bends toward the same inner side. So both dials hold: the tip per metre stays at zero point one two one five degrees for every metre, and the ramp still winds like an ordinary screw thread. Handedness belongs to the shape, not to the direction of travel.”  
   Describe: The same coil, now walked from its far end. The ahead stick and the third stick point the other way. Both dials read exactly what they read before.
5. `mirror-the-ramp` (working, await none) state: preset="mirror-ramp", progress=0.5, overlay="with-frame"  
   *The mirror-image coil; the turn dial is unchanged and the tip dial reads minus 0.1215 degrees per metre, with climb per turn reading minus 3 m.*  
   Say: “Here is a mirror image of the ramp. The turn per metre is unchanged at three point eight one six degrees for every metre. The tip per metre reverses to minus zero point one two one five degrees for every metre, winding the mirror way round, and the climb per turn readout reverses to minus three metres. Mirroring is what reverses the tip; reversing the walk is not.”  
   Describe: A coil winding the mirror way round. The turn dial is unchanged, and the tip dial and the climb readout have both changed sign.
6. `rebuild-from-two-numbers` (working, await none) state: preset="rebuilt-ramp", progress=1, overlay="with-frame"  
   *A path built from the two dial settings held for 100 m; coil radius reads 14.9841 m and climb per turn reads 2.9575 m.*  
   Say: “Now feed the two readings back in as settings. Hold a turn of three point eight two degrees per metre and a tip of zero point one two degrees per metre, for one hundred metres of path. What comes out is a coil of radius about fourteen point nine eight metres that climbs about two point nine six metres in a turn. That is the spiral ramp again, to the accuracy of the two rounded settings. Two numbers at every place, with a starting point and a starting frame, fix the path.”  
   Describe: A path built from two constant dial settings. It comes out as a coil of radius about fifteen metres climbing about three metres a turn, matching the spiral ramp.

### `pull-the-wire-straight` · for [[intrinsic-versus-extrinsic-curvature]] · entry

1. `dots-on-a-wavy-wire` (entry, await none) state: preset="wiggle-on-a-page", progress=0  
   *The wavy wire with two painted dots on it and a tape laid along the wire between them, reading 0.300 m.*  
   Say: “Here is the wavy wire again, with two painted dots on it. A tape laid along the wire reads the distance between the dots. It reads thirty centimetres. A bead-sized creature lives on this wire. She can slide along it, and her tape is the only tool she has.”  
   Describe: A wavy wire on a page with two painted dots. A tape laid along the wire between them reads thirty centimetres.
2. `predict-the-tape` (entry, await prediction) state: preset="wiggle-on-a-page", progress=0; evidences `intrinsic-versus-extrinsic-curvature/checks/bead-on-a-wavy-wire`  
   *Same view, paused, with the pull-straight control highlighted.*  
   Predict: “I will now pull this wire straight, without stretching any part of it. Afterwards, will her tape read a different number between the two dots?”  
   Say: “Make a guess before I pull. I will now pull this wire straight, without stretching any part of it. Afterwards, will her tape read a different number between the two dots?”  
   Describe: The wavy wire waits with its two dots and its tape. The control that pulls the wire straight is highlighted.
3. `pull-it-straight` (entry, await none) state: preset="wiggle-on-a-page", progress=0; animate straighten → 1 over 5 s  
   *The wire straightens while the dots hold their spacing along it; the turn dial falls to 0 and the best-fit circle grows and then blanks.*  
   Say: “I pull the wire straight, keeping every piece of it the same length as before. Watch the tape: it holds at thirty centimetres the whole way. The turn dial falls, and the orange best-fit circle grows wider and wider. At the end the dial reads zero degrees for every metre, and no circle is drawn.”  
   Describe: The wavy wire is pulled straight. The tape between the dots holds at thirty centimetres throughout. The turn dial falls to zero and the matching circle disappears.
4. `what-the-creature-learns` (entry, await none) state: preset="wire-pulled-straight", progress=1  
   *The straightened wire, with the dot spacing and the path length readouts unchanged from the wavy state.*  
   Say: “Nothing the creature can measure changed. Lengths along the wire are all she has, and every one of them held. The whole wire is still about two point one eight metres long. The bend showed only on the dials I read from the room around the wire, and in the orange best-fit circle drawn in that room. So a wire can be bent, seen from the room around it. No measurement made along the wire can ever show that bend.”  
   Describe: The wire is now straight. The tape between the dots and the length of the whole wire read what they read before. Only the readings taken from the room around the wire changed.
5. `a-ring-is-no-different` (entry, await none) state: preset="pond-ring", straighten=1, progress=1  
   *The pond ring pulled straight into a 60 m line, with the dot spacing readout unchanged.*  
   Say: “The pond path behaves the same way. Pulled straight, it becomes a line sixty metres long. The tape between its painted dots reads thirty centimetres, just as it did around the pond. Every wire hides its bends from the creature who lives on it.”  
   Describe: The round pond path has been pulled straight into a sixty metre line. The tape between its dots still reads thirty centimetres.

## Design rules

- **Blank the best-fit circle, its radius readout, the card, the third stick and both tip readouts wherever the turn per metre falls below one ten-thousandth of a degree per metre.** Because: At a straight spot no circle matches the path and the sheet of the bend has no direction, so any circle or card drawn there would be an invention of the renderer, not a fact about the path.
- **On the graph, show the slope readout next to the turn-per-metre dial, and never label the second derivative as the turn per metre.** Because: The two agree only where the graph is level, and at $x = 1$ metre they differ by a factor of more than eleven. Prevents `curvature-of-a-curve/misconceptions/curvature-is-the-second-derivative`.
- **Offer no walking-speed control, and label the dial per metre of path, never per second.** Because: A speed control invites the reading that a faster walker meets a sharper bend; the turn per metre belongs to the path alone. Prevents `curvature-of-a-curve/misconceptions/steady-speed-means-no-acceleration`.
- **Keep the painted dots, the tape and both length readouts on screen through every frame of the straightening, and animate it slowly enough to read them.** Because: Watching every spacing hold while the dial falls to zero is the whole argument that lengths along a wire cannot show its bend. Prevents `curvature-of-a-curve/misconceptions/wire-knows-its-bend`.
- **Give a creature living on the wire only the tape along the wire and the painted dots; offer no ring test, no protractor and no side-by-side walkers on the wire.** Because: Those instruments read curving on a surface, and offering them on a wire would suggest that a wire could have some of its own. Prevents `intrinsic-versus-extrinsic-curvature/misconceptions/wire-can-sense-its-bend`.
- **Draw the best-fit circle, the card and the sticks in the room's space, in colours the wire never uses, and never draw them as markings on the wire. On a ring the best-fit circle coincides with the path exactly, so draw nothing at the walker there until a beat on the wavy wire has named the circle and shown it sitting off the path.** Because: The bend is a fact about how the wire sits in the room around it, and drawing the circle as paint on the wire would make it look like something the wire itself carries. Prevents `intrinsic-versus-extrinsic-curvature/misconceptions/bent-means-intrinsically-curved`.
- **Keep the wavy line on a page one click away from the gently climbing coil, and show the tip dial on both.** Because: The wavy line bends nearly sixty times as sharply as the coil, 226.19 degrees per metre against 3.82 and tips nothing, while the coil bends gently and tips steadily. Prevents `frenet-serret-equations/misconceptions/sharp-bends-mean-torsion`.
- **When the walk is reversed, animate the first and third sticks flipping together while the second stick holds, and keep both dials on screen throughout.** Because: Seeing two sticks flip at once is what makes it plain that the tip reading, which compares them, cannot change sign. Prevents `frenet-serret-equations/misconceptions/reversal-flips-torsion`.
- **Distinguish the wire, the best-fit circle and the three sticks by line style and by end markers as well as by colour.** Because: Colour alone fails for colour-blind learners and in print.
- **Where the tip per metre, the total tip or the climb per turn is shown and reads exactly zero, speak it without the winding clause: "the card does not tip here at all", "the card did not tip at all over the whole path", "the coil does not climb at all".** Because: A reading of zero has no handedness, so naming a screw thread beside it invites the learner to hunt for a winding that is not there, on a wavy line drawn on a page or a coil with no climb. The schema carries only a positive and a negative template, so the zero line is a rule for the builder. Prevents `frenet-serret-equations/misconceptions/sharp-bends-mean-torsion`.
- **When a tour quotes what a dial reads, either speak the digits the dial shows, or speak a rounded value with the word "about"; never speak a value the displayed digits do not round to. Where the sentence already uses "about" for an axis of rotation, speak the dial's digits instead.** Because: The turn dial on the spiral ramp shows 3.816 and the tip dial 0.1215, so a bare "three point eight two" sends a learner hunting the screen for a number that is not there, and a second "about" in "turns about the third stick" would name a rotation rather than a rounding.

## Model

Every path is held as a smooth curve in space with an arc-length parametrization. The turn per metre is the size of the rate at which the unit direction of travel changes with distance along the path, and the best-fit circle's radius is its reciprocal, with that rate counted in radians per metre. The tip per metre is the torsion, signed so that a path winding like an ordinary right-handed screw thread reads positive. Both dials are reported in degrees per metre. The totals are accumulated along the walk and are never reduced modulo a full turn, so a total turn of several hundred degrees is normal; a path with no bend anywhere reads zero for both. Straightening rebuilds the wire from scaled-down readings at the same arc length, so every length measured along the wire is exactly preserved.

**Turn per metre and the best-fit circle**

$$
\kappa = \left|\frac{d\hat{\mathbf T}}{ds}\right|,\qquad \hat{\mathbf T} = \frac{d\mathbf r}{ds},\qquad R = \frac{1}{\kappa}
$$

Holds when: Arc-length parametrization. $R$, the principal normal and the whole frame exist only where $\kappa > 0$.

**How the three sticks change**

$$
\frac{d}{ds}\begin{pmatrix}\hat{\mathbf T}\\ \hat{\mathbf N}\\ \hat{\mathbf B}\end{pmatrix} = \begin{pmatrix}0&\kappa&0\\-\kappa&0&\tau\\0&-\tau&0\end{pmatrix}\begin{pmatrix}\hat{\mathbf T}\\ \hat{\mathbf N}\\ \hat{\mathbf B}\end{pmatrix}
$$

Holds when: Where $\kappa > 0$, with $\hat{\mathbf B} = \hat{\mathbf T}\times\hat{\mathbf N}$ and $\kappa \ge 0$, as in the course conventions. A right-handed helix has $\tau > 0$.

**Turning rate of a graph**

$$
k = \frac{y''}{(1 + y'^2)^{3/2}},\qquad \kappa = |k|
$$

Holds when: Plane graph $y(x)$ walked toward increasing $x$; $k > 0$ where the graph is concave up. The visual uses $y = x^2/L_0$ with $L_0 = 1$ metre.

**Readings of a coil**

$$
\kappa = \frac{a}{a^2 + b^2},\qquad \tau = \frac{\varepsilon\, b}{a^2 + b^2},\qquad b = \frac{h}{2\pi},\qquad L = 2\pi n\sqrt{a^2 + b^2}
$$

Holds when: $a > 0$; $\varepsilon = +1$ for a right-handed coil and $-1$ for its mirror image; $n$ full turns. $h = 0$ gives a flat ring with $\tau = 0$.

**The path built from two constant readings**

$$
a = \frac{\kappa}{\kappa^2 + \tau^2},\qquad b = \frac{\tau}{\kappa^2 + \tau^2},\qquad h = 2\pi b
$$

Holds when: Constant $\kappa > 0$ and constant $\tau$; the sign of $\tau$ fixes which way the built coil winds.

**Pulling the wire straight**

$$
\kappa_f(s) = (1 - f)\,\kappa(s),\qquad \tau_f(s) = (1 - f)\,\tau(s),\qquad 0 \le f \le 1
$$

Holds when: The rebuilt wire is integrated from these readings over the same arc-length interval, so every length measured along the wire is unchanged; $f = 1$ gives a straight wire.

**Totals over the whole walk**

$$
\Theta = \int_0^{L}\kappa\,ds,\qquad \Phi = \int_0^{L}\tau\,ds
$$

Holds when: Accumulated, never reduced modulo a full turn. $\Theta \ge 0$ always, since $\kappa \ge 0$; $\Phi$ takes either sign.

**Method:** The ring, the graph, the wavy line and the coil have closed-form readings, evaluated directly. A drawn path is fitted with a natural cubic spline in arc length and differentiated twice. Drawn, rebuilt and partly straightened paths are integrated with fourth-order Runge-Kutta in arc length with a step smaller than one thousandth of the path length, renormalizing the frame each step. The graph is reparametrized by arc length only for its length and total-turn readouts; the marker's position on it is set by the fraction of the drawn span in the horizontal coordinate. The frame, the card, the best-fit circle, the radius readout and both tip readouts are computed only where the turn per metre exceeds one ten-thousandth of a degree per metre, and blank otherwise. Where the turn per metre passes through zero, as at each straight spot of the wavy line, the bend stick and the third stick reverse, because the convention holds the turn per metre positive; the overlay blanks the frame and the card there rather than animating that reversal. The coil readouts are offered only on the coil and on the built path, and the slope readout only on a path drawn as a graph.

| Test | State | Expect | Hidden | Note |
| --- | --- | --- | --- | --- |
| `pond-ring` | preset="pond-ring", progress=1 | turn-per-metre = 6 ±1e-09; radius-of-curvature = 9.549296586 ±1e-06; total-turn = 360 ±1e-06; tip-per-metre = 0 ±1e-09; total-tip = 0 ±1e-09; path-length = 60 ±1e-09 | — | A lap of any ring turns the direction of travel 360 degrees, shared equally along its length: 360 divided by 60 metres is 6 degrees per metre, and the radius is 60 divided by two pi. |
| `lake-ring` | preset="lake-ring", progress=1 | turn-per-metre = 1.2 ±1e-09; radius-of-curvature = 47.746482928 ±1e-06; total-turn = 360 ±1e-06 | — | Five times the pond path's length gives one fifth of its turn per metre, with the same total turn. |
| `tightest-ring-the-slider-allows` | preset="tight-ring", progress=1 | turn-per-metre = 36 ±1e-09; radius-of-curvature = 1.591549431 ±1e-06; total-turn = 360 ±1e-06 | — | Boundary case at the low end of the ring slider. |
| `graph-at-its-lowest-point` | preset="parabola-graph", progress=0.5 | turn-per-metre = 114.591559026 ±1e-06; radius-of-curvature = 0.5 ±1e-09; graph-slope = 0 ±1e-09; tip-per-metre = 0 ±1e-09 | total-turn, total-tip | Progress 0.5 puts the marker at $x = 0$. There the slope is zero, so the turning rate equals the second derivative, 2 per metre, which is 114.591559 degrees per metre, and $R = 0.5$ metres. |
| `graph-at-one-metre` | preset="parabola-graph", progress=0.75 | turn-per-metre = 10.249380625 ±1e-06; radius-of-curvature = 5.590169944 ±1e-06; graph-slope = 2 ±1e-09 | total-turn, total-tip | Progress 0.75 puts the marker at $x = 1$ metre, where $y' = 2$ and $y'' = 2$ per metre, so $\kappa = 2/5^{3/2} = 0.1788854$ per metre and $R = 5.5901699$ metres. The second derivative alone would give 0.5 metres, out by a factor of 11.18. |
| `graph-whole-span` | preset="parabola-graph", progress=1 | total-turn = 151.927513064 ±1e-06; total-tip = 0 ±1e-09; path-length = 9.293567525 ±1e-06 | coil-radius, rise-per-turn | The total turn is the change in the tangent angle, $2\arctan 4 = 151.927513$ degrees. The length is $\int_{-2}^{2}\sqrt{1 + 4x^2}\,dx = 9.2935675$ metres. A plane curve has zero total tip. |
| `wavy-wire-at-a-crest` | preset="wiggle-on-a-page", progress=0 | turn-per-metre = 226.194671058 ±1e-06; radius-of-curvature = 0.253302959 ±1e-07; tip-per-metre = 0 ±1e-09; dot-spacing = 0.3 ±1e-09 | total-turn, total-tip | At a crest the slope is zero, so $\kappa = A(2\pi/\lambda)^2 = 0.1\times 39.478418 = 3.9478418$ per metre, which is 226.194671 degrees per metre and $R = 0.2533030$ metres. The wavy line lies in the page, so the tip is exactly zero. |
| `wavy-wire-at-a-straight-spot` | preset="wiggle-on-a-page", progress=0.125 | turn-per-metre = 0 ±1e-09 | radius-of-curvature, tip-per-metre, total-turn, total-tip | Two waves are drawn, and the arc length of each quarter-wave is equal, so progress 0.125 lands exactly on the first point of inflection. There $\kappa = 0$: no circle matches, and the frame, the card and the tip readings have no direction, so they blank. Design rule no-circle-where-it-runs-straight. |
| `wavy-wire-whole-page` | preset="wiggle-on-a-page", progress=1 | total-turn = 257.135261083 ±1e-06; total-tip = 0 ±1e-09; path-length = 2.184767095 ±1e-06; dot-spacing = 0.3 ±1e-09 | coil-radius, rise-per-turn | The tangent angle swings between plus and minus $\arctan(0.6283185) = 32.141873$ degrees eight times over two waves, giving 257.135261 degrees; the length is from numerical quadrature. The total tip is zero however sharply the line bends: design rule sharp-page-wiggle-next-to-a-gentle-spring. |
| `wire-pulled-straight` | preset="wire-pulled-straight", progress=1 | turn-per-metre = 0 ±1e-09; dot-spacing = 0.3 ±1e-09; path-length = 2.184767095 ±1e-06 | radius-of-curvature, tip-per-metre, total-tip | Flat case. Straightening scales both readings to zero while keeping arc length, so the dot spacing and the whole length match the wavy wire's exactly. |
| `half-straightened-wire` | preset="wiggle-on-a-page", straighten=0.5, progress=1 | turn-per-metre = 113.097335529 ±1e-06; radius-of-curvature = 0.506605918 ±1e-07; total-turn = 128.567630542 ±1e-06; path-length = 2.184767095 ±1e-06; dot-spacing = 0.3 ±1e-09 | — | Halfway through the pull, both dials read half their wavy values and the total turn is halved, while every length along the wire is untouched. Progress 1 lands on a crest, so the turn per metre is half of 226.194671. |
| `straight-wire` | preset="straight-wire", progress=1 | turn-per-metre = 0 ±1e-09; path-length = 1 ±1e-09; dot-spacing = 0.3 ±1e-09 | radius-of-curvature, tip-per-metre, total-tip | Boundary case with no bend anywhere. The total turn reads zero and everything that needs a direction of bend blanks. |
| `spiral-ramp` | preset="spiral-ramp", progress=1 | turn-per-metre = 3.815852367 ±1e-06; tip-per-metre = 0.121462353 ±1e-07; radius-of-curvature = 15.015198178 ±1e-06; path-length = 188.591028005 ±1e-05; total-turn = 719.635520687 ±1e-05; total-tip = 22.906710068 ±1e-06; coil-radius = 15 ±1e-09; rise-per-turn = 3 ±1e-09 | graph-slope | With $a = 15$ m and $b = 3/(2\pi) = 0.4774648$ m, $a^2 + b^2 = 225.227972$ m squared, so $\kappa = 0.0665993$ per metre, which is 3.8158524 degrees per metre, and $\tau = 0.0021200$ per metre, which is 0.1214624 degrees per metre. Two turns run 188.591028 metres. The total turn exceeds 360 degrees, so the totals are accumulated, not wrapped. |
| `spiral-ramp-walked-backwards` | preset="spiral-ramp", walk-direction="backward", progress=1 | turn-per-metre = 3.815852367 ±1e-06; tip-per-metre = 0.121462353 ±1e-07; total-tip = 22.906710068 ±1e-06; rise-per-turn = 3 ±1e-09 | — | Reversal sends the ahead stick and the third stick to their opposites and leaves the bend stick alone, so both readings are unchanged. Every reading here must match the forward test exactly. |
| `mirror-ramp` | preset="mirror-ramp", progress=1 | turn-per-metre = 3.815852367 ±1e-06; tip-per-metre = -0.121462353 ±1e-07; total-tip = -22.906710068 ±1e-06; rise-per-turn = -3 ±1e-09 | — | Negative branch of the tip readouts. Mirroring keeps the turn per metre and reverses the tip and the climb per turn. |
| `coil-with-no-climb` | preset="flat-ring-spring", progress=1 | turn-per-metre = 3.819718634 ±1e-06; tip-per-metre = 0 ±1e-09; total-tip = 0 ±1e-09; radius-of-curvature = 15 ±1e-09; total-turn = 360 ±1e-06; rise-per-turn = 0 ±1e-09 | — | Boundary case at the low end of the climb slider. With $b = 0$ the coil is a flat ring of radius 15 metres: $\kappa = 1/15$ per metre, which is 3.8197186 degrees per metre, and the tip is exactly zero. |
| `rebuilt-from-two-numbers` | preset="rebuilt-ramp", progress=1 | turn-per-metre = 3.82 ±1e-06; tip-per-metre = 0.12 ±1e-07; coil-radius = 14.984108617 ±1e-06; rise-per-turn = 2.957526631 ±1e-06; radius-of-curvature = 14.99889516 ±1e-06; total-turn = 382 ±1e-06; total-tip = 12 ±1e-06 | — | With $\kappa = 3.82$ and $\tau = 0.12$ degrees per metre, that is $0.0666716$ and $0.0020944$ per metre, $a = \kappa/(\kappa^2 + \tau^2) = 14.9841086$ metres and $h = 2\pi\tau/(\kappa^2 + \tau^2) = 2.9575266$ metres. Those differ from 15 and 3 only through the rounding of the two settings. |
| `rebuilt-with-the-tip-reversed` | preset="rebuilt-mirror-ramp", progress=1 | tip-per-metre = -0.12 ±1e-07; coil-radius = 14.984108617 ±1e-06; rise-per-turn = -2.957526631 ±1e-06; total-tip = -12 ±1e-06 | — | Reversing only the tip setting builds the mirror coil: same radius, opposite climb. |
| `no-totals-part-way-along` | preset="spiral-ramp", progress=0.5 | — | total-turn, total-tip | The totals belong to a finished walk and must not be shown part way along it. |
| `widest-ring-the-slider-allows` | preset="lake-ring", circle-length=600, progress=1 | turn-per-metre = 0.6 ±1e-09; radius-of-curvature = 95.492965855 ±1e-06; total-turn = 360.0 ±1e-06; path-length = 600 ±1e-09 | coil-radius, rise-per-turn, graph-slope | Boundary case at the high end of the ring slider. The turn per metre falls to 360 divided by 600 metres while the total turn holds at 360 degrees, the same trade the pond and lake rings show. |
| `tightest-coil-the-sliders-allow` | preset="spiral-ramp", helix-radius=0.5, helix-rise=3, helix-turns=6, progress=1 | turn-per-metre = 59.936251511 ±1e-06; tip-per-metre = 57.23490419 ±1e-07; radius-of-curvature = 0.955945326 ±1e-06; path-length = 26.063494747 ±1e-05; total-turn = 1562.14817642 ±1e-05; total-tip = 1491.741624715 ±1e-05; coil-radius = 0.5 ±1e-09; rise-per-turn = 3 ±1e-09 | graph-slope | Boundary case with the coil sliders at their sharpest: $a = 0.5$ m, $h = 3$ m, six turns. Here $b = 0.4774648$ m is close to $a$, so the tip per metre comes within a twentieth of the turn per metre, the largest tip the coil sliders reach. Both totals run past 1400 degrees, so neither is wrapped. |
| `sharpest-wavy-line-still-does-not-tip` | preset="wiggle-on-a-page", wiggle-height=1, wiggle-spacing=0.5, progress=0 | turn-per-metre = 9047.786842339 ±1e-05; radius-of-curvature = 0.006332574 ±1e-09; tip-per-metre = 0 ±1e-09 | total-turn, total-tip, coil-radius, rise-per-turn | The sharpest bend the page sliders allow: at a crest $\kappa = A(2\pi/\lambda)^2 = 157.91367$ per metre, which is 9047.78684 degrees per metre and a best-fit circle 6.3 millimetres across. The tip per metre is still exactly zero, because the line lies in the page: design rule sharp-page-wiggle-next-to-a-gentle-spring. |

## Serves

- [[curvature-of-a-curve]]: the turn-per-metre dial, the best-fit circle riding the path with its radius spoke, the two ring presets whose dials differ by a factor of five, and the graph where the slope readout separates the turning rate from the second derivative
- [[frenet-serret-equations]]: the card that fills the sheet of the bend, the three sticks and their two turns, the tip dial that stays at zero on a sharply bending page and lifts off zero on a gently climbing coil, the reversal and mirror presets, and the rebuild mode driven by the two dials
- [[intrinsic-versus-extrinsic-curvature]]: the painted dots and the tape along the wire, held on screen while the straightening slider takes the dial to zero, so that every length along the wire is seen to survive a change that the room's instruments register

## In the visual network

- **Leads to:** [[bend-arrow-split-on-a-surface]], [[card-touching-a-curved-patch]], [[paper-rolled-into-a-tube-and-a-cone]]

## Accessibility

Every tour beat says where the marker sits and what each dial reads, in degrees per metre and metres. The tip reading is announced with the way the path winds, as an ordinary screw thread or its mirror image, never by a bare sign. A reading of exactly zero is announced as no tip at all. Blanked readouts are announced as blank, with the reason. The wire, the best-fit circle and the three sticks differ in line style and end markers as well as colour, and every control works from the keyboard.

Static alternative: A wavy wire with a small circle matching the bend at one of its crests, a coil whose bend-sheet tips as it climbs, and the same wavy wire pulled straight with its two painted dots still the same distance apart along it.

- `Space`: play or pause the walk along the path
- `Left and Right arrows`: move the marker along the path
- `1 to 7`: choose the ring, the wavy line, the graph, the coil, the straight wire, the built path, or a drawn path
- `O`: cycle what is drawn at the walker: nothing, then the circle, then the circle and its card, then the circle, the card and the three sticks
- `R`: walk the same path from the other end
- `S`: pull the wire straight, or let it back

## Starting material

Earlier course assets: `manuscript-section-4-8-curvature-bending-local-frames`

The earlier manuscript's treatment of a bending curve and the frame carried along it gives the working-rung wording and the helix worked example. Everything else is new: the turn-per-metre dial, the best-fit circle in 3D, the card and sticks overlay, the straightening slider with its painted dots, and the rebuild mode.

## Review: novice

**Verdict:** fixed (2026-09-16, revision 4)

**Retell attempt:** A bend has a size you can measure: how many degrees your direction of travel turns for every metre you walk. Around the pond path, sixty metres round, that is six degrees for every metre; around the lake path, five times as long, only one point two degrees, and both laps turn you the whole three hundred and sixty degrees, so the pond path bends five times as sharply. At any one place on a wavy wire, one circle matches the bend best, and its radius tells you the same thing the other way round: small circle, sharp bend. Where the wire is not bending, there is no matching circle at all and the dial reads zero. A little card held in the sheet of the bend never tips while you slide along a wavy line drawn on a page, however sharp its bends are, but it tips a little at every step on a spring, because the spring keeps climbing out of that sheet. And if you paint two dots on the wavy wire and pull the wire straight, a tape laid along the wire still reads thirty centimetres between them, and the whole wire is still the same length. So the bend is something you see from the room around the wire, not something a creature living on the wire could ever measure.

- Stumble: “Right now it reads six degrees.”: The dial counts degrees for every metre, but this line drops the "for every metre", so I first heard it as "the path has already turned her six degrees".
- Stumble: “It touches the wire there, heads the same way, and bends just as sharply.”: The same way as what? The circle has no "way" of its own until it is compared with something, and no reference is given.
- Stumble: “the orange spoke from the wire to its centre reads about twenty five centimetres”: A spoke does not read anything; the dials read. And "its centre" could be the wire’s or the circle’s.
- Stumble: “The walker moves on to a place where the wire runs straight for an instant.”: "For an instant" is a length of time, but I am being shown a place along a wire, and the walk has no clock in it.
- Stumble: “No circle matches a straight piece of wire, so the orange circle and its spoke go blank here.”: A "piece" sounds like a stretch of wire I could hold between two fingers, so I could not tell whether the straight part was a stretch or the single point the marker is sitting on.
- Stumble: “A small card sits in the sheet that fits the bend where the walker stands.”: Nothing tied that sheet to anything I can see. The orange circle is on screen and lies in exactly that sheet, and saying so would have shown me where the card is.
- Stumble: “the turn dial reads three point eight two degrees for every metre”: The dial on screen reads three point eight one six. I hunted for the spoken number and could not find it.
- Stumble: “the card holding this bend tips {abs} degrees for every metre, winding like an ordinary screw thread”: The card does not wind; the path does. And on the wavy line drawn on a page this readout is zero, where "winding like an ordinary screw thread" is flatly wrong.
- Stumble: “the coil climbs {abs} metres in one full turn, winding like an ordinary screw thread”: On the coil with no climb at all this reads zero metres, and a flat ring does not wind like a screw thread at all.
- Stumble: “Watch the tape: the dots hold at thirty centimetres the whole way.”: The dots are painted marks; what holds at thirty centimetres is the reading on the tape between them.
- Stumble: “The bend showed only on the dials I read from the room, and in the orange circle drawn in the room.”: Which room? The tours before this one never mention a room, and I am looking at a wire on a page. The circle is also named only by its colour here.
- Stumble: “So a wire can be bent, seen from the room. It can never be curved in the way measurements along it could show.”: "Bent" and "curved" mean the same thing to me, so the pair sounded like a word trick rather than a result, and "in the way measurements along it could show" took three readings to unpick.
- Stumble: “The pond path goes the same way.”: "Goes the same way" sounds like a direction, and the pond path is a ring, so for a moment I thought the two paths ran the same way round.
- Stumble: “Way round the ring”: As the name of a slider this could be a direction as easily as a distance.
- Stumble: “What to draw at the marker”: The tutor always says "the walker", and the screen says "marker", so I looked for two different things. The slope readout is labelled the same way.
- Stumble: “Coil”: The spoken tour calls this shape a spring; the menu calls it a coil, so I did not know they were the same path.
- Stumble: “Spiral ramp: 15 metre coil climbing 3 metres a turn”: I read "15 metre coil" as a coil fifteen metres long. Fifteen metres is how far it runs from its centre.
- Stumble: “Tightest ring the slider allows”: I had not touched a slider yet, so I did not know which one was meant.
- Stumble: “A second reading, the tip of the sheet that holds the best-fit circle, separates a wavy line drawn on a page from a spring that climbs out of it”: "The tip of the sheet" sounds like the pointed end of a sheet of paper, not a tipping of it.
- Stumble: “So both dials hold, and the tip per metre stays at plus zero point one two degrees.”: The visual promises that the tip is always announced with the way the path winds and never by a bare sign, and here it is announced as a bare plus.
- Fixed: Entry tour measure-a-bend: gave the opening dial reading its "for every metre", gave the best-fit circle’s direction its reference, stopped the spoke "reading" a number, and replaced "runs straight for an instant" and "a straight piece of wire" with the point where the wire is not bending (say and describe).
- Fixed: Entry tour the-sheet-a-bend-lies-in: tied the card’s sheet to the orange best-fit circle on screen, and marked the spoken 3.82 and 0.12 as "about", since the dials show 3.816 and 0.1215.
- Fixed: Entry tour pull-the-wire-straight: the tape, not the dots, holds its reading; introduced "the room around the wire" where the room is first spoken of; replaced "can never be curved in the way measurements along it could show" with a plain sentence about measurements along the wire; "behaves the same way" for "goes the same way"; named the circle as the best-fit circle rather than by colour alone.
- Fixed: Readouts tip-per-metre, total-tip and rise-per-turn: the handedness clause now says how the reading is counted rather than claiming the card or a flat ring winds like a screw thread, so the line no longer sounds wrong at zero.
- Fixed: Labels: "Distance once round the ring"; "Coil, like a spring"; "What to draw at the walker"; "Slope of the graph at the walker"; "Tightest ring this demo allows"; "Spiral ramp: 15 metres from its centre, climbing 3 metres a turn".
- Fixed: makes_visible: "the tip of the sheet" replaced by how many degrees that sheet tips for every metre.
- Fixed: Working tours: spoken describe lines now say "the walker" like the entry tours and the labels, and the two tip sentences announce the winding instead of a bare plus or a bare minus.
- Concern: Zero values of the signed readouts still carry a handedness clause. The design rule blanks the tip readouts only where the turn per metre is near zero, so a wavy line on a page and the coil with no climb both speak a tip of zero "counted the way an ordinary screw thread winds". A third template for exactly zero ("the card does not tip here", "the coil does not climb at all") would read better, but the schema has only say and say_negative, so this needs a schema or design-rule decision, not a rewrite.
- Concern: Beat meet-the-pond-path draws the best-fit circle on the ring itself before any beat names it, and on a ring the two coincide exactly. That is the one state where the circle can look like paint on the path, which design rule the-circle-belongs-to-the-room forbids. Either name it in that beat, or hold the circle back until the wavy wire where it clearly sits off the path.
- Concern: Spoken values are rounded against unrounded dials in the working tour too: three point eight two against a dial of 3.816, zero point one two against 0.1215. I added "about" only in the entry beat; a builder should decide whether the tour states round the dials instead.
- Concern: Entry speech uses centimetres (thirty centimetres between the dots, a spoke of twenty five centimetres) while the matching readouts display metres, 0.300 and 0.2533. A learner comparing the spoken number with the dial has to convert; consider displaying centimetres on the page-sized presets.
- Concern: Two different people are called "she" across the visual: the walker in three tours and the bead-sized creature in the straightening tour. They never share a beat, but a builder adding narration between beats should keep them apart by name.
- Concern: The Pull straight slider runs from 0 to 1 with no unit, so its numbers mean nothing on screen; a label such as "none" to "fully straight" at the ends would help.

**Re-read** (2026-09-16, revision 4)

- Stumble: “its radius is one over the turning rate, with the turn counted in radians rather than degrees”: One long sentence carries two separate ideas, and "the turn counted in radians" names a unit for the turn while the rate on the dial is a turn for every metre, so I could not tell what to put into "one over".
- Stumble: “never by a bare sign, and a reading of exactly zero is announced as no tip at all”: The sentence runs to nearly forty words and joins two different rules with "and", so the zero rule arrives after I have stopped following.
- Stumble: “cycle what is drawn at the walker through nothing, circle, circle and card, and circle, card and sticks”: The commas separate items inside a setting and between settings alike, so I could not tell how many settings there are or where one ends.
- Stumble: “The frame turns about the third stick at the turn per metre, the three point eight one six degrees on the dial”: Read aloud, "turns about the third stick" and then a number let me hear "turns about three point eight one six", as if the number were a rounding, and the whole sentence carries both rotations at once.
- Stumble: “the tip per metre stays at zero point one two one five degrees, and the ramp still winds like an ordinary screw thread”: The number is spoken in plain degrees although it is a tip for every metre, and three clauses joined by "and" hide which part is the conclusion.
- Stumble: “The turn per metre is unchanged at three point eight one six degrees.”: Both readings here are named in plain degrees, so they sound like totals for the whole ramp rather than readings for every metre.
- Fixed: Wording only, six lines: makes_visible split in two with the rate named in radians per metre; accessibility.summary split so the zero rule stands alone; the O key action rewritten as a stepped list; three-sticks-on-the-ramp split in two with "around" for the axis so no number can be heard as a rounding; walk-the-ramp-backwards and mirror-the-ramp given "for every metre" on each spoken reading.
- Fixed: No claim, number, sign or state was changed.
- Fixed: The added "about" in what-the-creature-learns, the-graph-at-its-lowest-point, the-slope-spoils-the-shortcut and rebuild-from-two-numbers, and the option label "Just the path", raised no stumble.

## Review: physics

**Verdict:** fixed (2026-09-16, revision 4)

- Verified: Turn per metre and best-fit radius: $\kappa = |d\hat{\mathbf T}/ds|$, $R = 1/\kappa$.: Re-derived in arc length and recomputed with an independent python implementation using $\kappa = |\mathbf r'\times\mathbf r''|/|\mathbf r'|^3$ on each path. → Correct and matches the course conventions ($\kappa \ge 0$). One wording error found: the reciprocal holds only with the rate in radians per metre, while both dials read degrees per metre. Fixed in makes_visible and in the model summary; no tour beat made the claim in degrees.
- Verified: Frenet-Serret matrix and the sense of the tip reading.: Checked against the course conventions row for curves in space ($T' = \kappa N$, $N' = -\kappa T + \tau B$, $B' = -\tau N$, $B = T\times N$, right-handed helix $\tau > 0$), then integrated the frame numerically for one metre of the spiral ramp. → Correct. The component of the bend stick along the old third stick after one metre is 0.0021184, against $\sin\tau = 0.0021199$: the card tips toward the side the third stick points to at the torsion, exactly as the tip-per-metre sense line says.
- Verified: Rings: turn per metre is 360 degrees divided by the lap length, radius is the lap length over two pi.: Recomputed for 60, 300, 10 and 600 metres. → 6, 1.2, 36 and 0.6 degrees per metre; radii 9.5492966, 47.7464829, 1.5915494 and 95.4929659 metres; total turn 360 degrees in every case. All four match the entry tour and the tests.
- Verified: Graph: $k = y''/(1+y'^2)^{3/2}$ on $y = x^2/L_0$ with $L_0 = 1$ metre.: Recomputed at $x = 0$ and $x = 1$ metre, and integrated $\int\kappa\,ds$ and $\int\sqrt{1+y'^2}\,dx$ over $-2 \le x \le 2$ by Simpson's rule, cross-checked against $2\arctan 4$ and the closed form. → 114.5915590 and 10.2493806 degrees per metre; radii 0.5 and 5.5901699 metres, a ratio of 11.1803399, so "more than eleven times" holds; total turn 151.9275131 degrees by both routes; length 9.2935675 metres. Every test value confirmed.
- Verified: Wavy line: $y = A\cos(2\pi x/\lambda)$, two waves, $A = 0.1$ m, $\lambda = 1$ m.: Recomputed the crest and the inflection, the eight quarter-wave arc lengths, the total turn as $8\arctan(A\,2\pi/\lambda)$ and as $\int\kappa\,ds$, and the length by quadrature. → Crest 226.1946711 degrees per metre, radius 0.2533030 metres; the quarter-waves are equal to twelve figures (0.273095886833 m each), so progress 0.125 does land exactly on the first inflection, where $\kappa$ is zero to 8e-15; total turn 257.1352611 degrees by both routes; length 2.1847671 metres. Confirmed.
- Verified: Coil: $\kappa = a/(a^2+b^2)$, $\tau = \varepsilon b/(a^2+b^2)$, $b = h/2\pi$, $L = 2\pi n\sqrt{a^2+b^2}$.: Recomputed for $a = 15$ m, $h = 3$ m, two turns, and cross-checked $\kappa$ and $\tau$ from the cross-product formulas at a point on the curve; repeated for $h = 0$ and for the mirror image. → 3.8158524 and 0.1214624 degrees per metre, radius 15.0151982 metres, length 188.5910280 metres, totals 719.6355207 and 22.9067101 degrees; the cross-product route agrees to 1e-17. $h = 0$ gives 3.8197186 degrees per metre, radius 15 metres, total turn 360 degrees and exactly zero tip. Mirroring reverses the tip and the climb and leaves the turn alone. All confirmed.
- Verified: Reversal leaves both readings unchanged, mirroring reverses the tip only.: Re-derived under $s \to -s$: $\tilde T = -T$, $\tilde N = N$, $\tilde B = -B$, so $\tilde\kappa = \kappa$ and $d\tilde B/d\tilde s = -\tau\tilde N$. → Correct: torsion is invariant under reversal and changes sign under a reflection. The beat walk-the-ramp-backwards and the two reversal tests state exactly this.
- Verified: Rebuild: constant $\kappa$ and $\tau$ give $a = \kappa/(\kappa^2+\tau^2)$, $h = 2\pi\tau/(\kappa^2+\tau^2)$.: Recomputed for 3.82 and 0.12 degrees per metre over 100 metres, and for the reversed tip. → Radius 14.9841086 metres, climb 2.9575266 metres, best-fit radius 14.9988952 metres, totals 382 and 12 degrees; the reversed tip gives the same radius and the opposite climb. The gap from 15 and 3 metres is entirely the rounding of the two settings, as the beat says.
- Verified: Straightening preserves every length measured along the wire.: Checked the map $\kappa_f = (1-f)\kappa$, $\tau_f = (1-f)\tau$ at the same arc length, and recomputed the half-straightened wavy wire. → 113.0973355 degrees per metre at the crest, radius 0.5066059 metres, total turn 128.5676305 degrees, length and dot spacing untouched. Correct, and the totals halve exactly as the readings do.
- Verified: Every readout range covers every value the controls can produce.: Maximized each readout over the declared param ranges. → Three ranges were too narrow: the build sliders reach a total turn of 48000 degrees (120 degrees per metre over 400 metres), a total tip of 24000 degrees, and a climb per turn of $\pi/\kappa_{\min} = 18000$ metres at $\tau = \kappa = 0.01$ degrees per metre. Widened all three. The tip-per-metre range already covers the largest reachable value, 60 degrees per metre.
- Verified: Every tour state is a declared preset, and no state uses an unavailable combination.: Walked all five tours against the preset list and every available_when clause. → All 24 beats name declared presets; straighten is used only on the ring and the wavy line, where it is available, and walk-direction and overlay are available everywhere. Two animations were no-ops, because the beat state already held the value the animation moved to; fixed by starting those two graph beats at the previous beat's position.
- Verified: Each beat's check exists in the served note and is evidenced by that beat's prediction.: Checked the six check addresses against the digests of the three served notes. → two-round-paths, parabola-at-x-equals-one, wiggle-on-a-page, spiral-ramp, walk-the-helix-backwards and bead-on-a-wavy-wire all exist, each at the rung of the tour that cites it, and each prediction asks exactly what its check asks.
- Verified: Design rules match the misconceptions they name.: Checked all nine rules against the misconception lists of the three served notes. → Every named address exists. One rule overstated a ratio ("sixty times as sharply"); the true ratio is 59.3, now stated with its two numbers.
- Verified: Nothing names or reproduces a source book.: Read every reader-facing and tutor-facing field. → Clean. The only source trace is the internal provenance block, which is stripped at runtime.
- Counterexample: Flat case: the straight wire, and the wavy wire pulled fully straight. Turn per metre exactly zero, radius, card, third stick and both tip readouts blank, total turn zero, and every length along the wire unchanged. Holds.
- Counterexample: Degenerate point on a bending path: progress 0.125 on the wavy line is an inflection, where the turn per metre is zero to 8e-15 and the frame has no direction. The blanking rule covers it; added a note to the method that the bend stick and the third stick reverse across such a point, since the convention holds the turn per metre positive, so the overlay must blank rather than animate a flip.
- Counterexample: Ring boundaries: 10 metres round (36 degrees per metre) and 600 metres round (0.6 degrees per metre). Both keep a total turn of 360 degrees. Added the 600 metre case as a test.
- Counterexample: Sharpest page bend the sliders allow: height 1 metre, wavelength 0.5 metres gives 9047.79 degrees per metre, a best-fit circle 6.3 millimetres across, and a tip of exactly zero. Added as a test, because it is the strongest case against "sharp bends mean torsion".
- Counterexample: Sharpest coil the sliders allow: radius 0.5 metres, climb 3 metres, six turns gives 59.94 degrees per metre of turn against 57.23 of tip, with totals of 1562.15 and 1491.74 degrees. Added as a test; it also shows the totals are accumulated, not wrapped.
- Counterexample: Coil with no climb: tip and total tip exactly zero while the turn per metre stays at 3.82 degrees per metre. Holds, and it is the state that made the spoken zero reading with a screw-thread clause sound wrong.
- Counterexample: Both directions: walking from the far end leaves both readings identical; mirroring reverses the tip and the climb and leaves the turn. Re-derived and confirmed against the two tests.
- Counterexample: Extreme build settings: 0.01 degrees per metre of turn with 60 of tip, and 120 with 60. These reach a climb per turn of 18000 metres and a total turn of 48000 degrees, past three declared readout ranges, which are now widened to cover them.
- Counterexample: Ring straightened part way: a closed ring cannot stay closed as it straightens, so it opens into an arc. The straighten param's effect now says so.
- Fixed: makes_visible and the model summary: the best-fit radius is one over the turning rate only with the turn in radians per metre, and both dials read degrees per metre.
- Fixed: Readout ranges widened to cover the build sliders: total turn to 48000 degrees, total tip to 24000 degrees, climb per turn to 18000 metres.
- Fixed: Novice concern settled, zero readings: added design rule say-a-zero-reading-without-handedness, so a tip, total tip or climb of exactly zero is spoken plainly and the winding clause is dropped. The say and say_negative templates stay as the novice review left them, since they are true for every non-zero value.
- Fixed: Novice concern settled, the circle on the ring: added an overlay setting that draws nothing at the walker, and set the four ring beats of the entry tour to it, so the best-fit circle first appears on the wavy wire where it plainly sits off the path. Design rule the-circle-belongs-to-the-room now says so.
- Fixed: Novice concern settled, rounded speech: added design rule speak-the-dial-as-it-reads. The working tour now says "about" where it quotes a rounded dial, and speaks the dial's own digits (three point eight one six, zero point one two one five) in the one sentence where a second "about" would name an axis of rotation.
- Fixed: Two graph beats animated progress to the value their state already held, so nothing moved; they now start at the previous beat's position and animate from there.
- Fixed: Design rule sharp-page-wiggle-next-to-a-gentle-spring: the ratio is 59.3, not 60, and now carries its two readings.
- Fixed: Added three boundary tests (widest ring, tightest coil, sharpest page bend) and recorded which readouts are hidden on paths that are not coils or graphs.
- Fixed: The straighten param's effect now says a closed ring opens into an arc; the method says the frame blanks rather than flips where the turn per metre passes through zero.
- Concern: The build sliders allow a turn per metre of 0.01 degrees, which makes a coil 2865 metres across climbing 18000 metres a turn while at most 400 metres of it is drawn. The readings are right but the picture is not informative; a builder may prefer to raise the lower end of that slider rather than render such a coil.
- Concern: A drawn path is fitted with a spline and differentiated twice, so its tip per metre near an inflection is the noisiest number in the demo: the torsion divides by the square of a curvature that is going to zero. The blanking threshold of one ten-thousandth of a degree per metre was chosen for the closed-form paths; a builder should check it against a hand-drawn path before trusting the tip dial there.
- Concern: The entry tours speak centimetres while the readouts display metres, which the novice review also raised. It is a display decision, not an accuracy one, but it is the last place where a learner still has to convert to match speech against a dial.

**Diff check** (2026-09-16, revision 4)

- Verified: "Its radius is one divided by the turning rate, with that rate counted in radians per metre rather than degrees per metre" says what the earlier line said.: Compared with the model: the best-fit radius is the reciprocal of the curvature, which carries units of radians per metre, and the dial shows the same rate in degrees per metre. → Same claim, with the units of the rate now matched to the reciprocal. Unchanged.
- Verified: "The frame turns around the third stick at the turn per metre" and "tips around the first stick at the tip per metre" keep the axes and senses of the earlier "about".: Re-derived the Darboux rotation from the course Frenet-Serret conventions: the frame's rotation is the tip per metre about the first stick plus the turn per metre about the third. → Axes, rates and senses unchanged; "around" and "about" name the same axis of rotation.
- Verified: The spiral ramp dials read 3.816 and 0.1215 degrees per metre, so the digits spoken in three-sticks-on-the-ramp, walk-the-ramp-backwards and mirror-the-ramp are what the dials show.: Recomputed with python3 for radius 15 m and climb 3 m a turn: b = 0.4774648 m, turn per metre 3.8158524 degrees, tip per metre 0.1214624 degrees, rounded to the readouts' three and four decimals. → 3.816 and 0.1215 confirmed; adding "for every metre" states the unit the dial already carries and changes no value.
- Verified: Walking the ramp from the far end leaves both readings and the handedness alone.: Reversed the arc length: the first and third sticks flip, the second is unchanged, and the turn and tip per metre are both even under the reversal. → Both dials hold and the ramp still winds like an ordinary screw thread. Unchanged.
- Verified: Mirroring reverses the tip per metre and the climb per turn and leaves the turn per metre alone.: Applied a reflection to the helix: the curvature is unchanged and the torsion changes sign, as does the climb per turn. → Minus 0.1215 degrees for every metre and minus 3 metres a turn, with the turn per metre held at 3.816. Unchanged.
- Verified: The keyboard list for O matches the overlay options and their order.: Read the option list: none, circle-only, with-plane, with-frame. → "nothing, then the circle, then the circle and its card, then the circle, the card and the three sticks" matches in order.
- Verified: The split accessibility summary still states the zero-tip rule exactly as the design rule does.: Compared the sentence with design rule say-a-zero-reading-without-handedness. → A reading of exactly zero is announced as no tip at all, with no handedness named. Unchanged.
- Verified: The untouched changed line in the-slope-spoils-the-shortcut quotes the dial correctly.: Recomputed the parabola at x = 1 m: turn per metre 10.24938 degrees, best-fit radius 5.5901699 m, 11.18 times the half metre at the vertex. → Dial 10.249, spoken "about ten point two five", and "more than eleven times" all correct.
- Verified: The untouched changed line in rebuild-from-two-numbers quotes the built coil correctly.: Recomputed from 3.82 and 0.12 degrees per metre held for 100 m. → Coil radius 14.9841 m and climb 2.9575 m a turn, so "about fourteen point nine eight" and "about two point nine six" are correct roundings.
- Verified: The untouched changed lines that only added "about" change no value.: Checked the wavy wire length 2.18 m and the vertex dial 114.59156 degrees per metre against their spoken roundings. → Both are roundings of the displayed values, correctly flagged with "about".
- Fixed: None.
- Fixed: The six novice rewrites were accepted as written.
