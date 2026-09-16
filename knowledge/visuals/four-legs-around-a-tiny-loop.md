---
type: "visual"
schema_version: 2
id: "four-legs-around-a-tiny-loop"
title: "Four legs around a tiny loop"
kind: "interactive-3d"
priority: "core"
status: "proposed"
revision: 1
rungs: ["entry", "working"]
serves: ["holonomy", "riemann-curvature-tensor", "riemann-curvature-operator", "cyclic-identity"]
builds_on: ["carry-an-arrow-around-a-loop"]
leads_to: ["cube-of-small-loops", "four-terms-that-cancel", "twenty-of-256-slots"]
---

# Four legs around a tiny loop

`four-legs-around-a-tiny-loop` · interactive-3d · core · proposed · rungs: entry, working

> A tiny four-sided walk with a carried arrow. On a ball the arrow comes back turned, by an amount that follows the loop's area. On a flat floor two walking instructions can still miss the start.

## What it makes visible

A small four-sided walk on a ball, a saddle or a flat floor with a pole, with a carried arrow that never swings. Shrinking the cell shows the returned turn falling with the area while the turn divided by the area settles to one number, and the arrow's change divided by the two edge lengths settles to minus a Riemann component. Swapping the edge order flips the sign. Two walking instructions and their reverses can miss the start even on the flat floor; the gap belongs to the instructions, the arrow's change around the closed loop belongs to the curvature, and the bare commutator overstates it. Two routes built from two arrows meet on the floor, miss by a gap that shrinks faster than the area on the ball, and miss by a gap that keeps pace with the area only on a made-up floor with twist.

## The picture

A shaded surface with a faint grey grid fills the scene, seen from slightly above. At a base corner, the first leg is a solid blue line, the second a solid orange line, and the two return legs are dashed blue and dashed orange. When the four legs miss the start, a dotted red closing walk joins the end point to the start. The region on the walker's left is lightly tinted. Faded copies of the carried arrow mark its progress. At the base corner an inset shows the start arrow as a grey dashed line and the returned arrow as a solid green line, with an arc between them. In two-routes mode the two routes are drawn solid blue and solid orange from the same start, their end points are marked with dots, and a dotted red segment measures the gap. An optional side panel plots the turn or the gap against the loop size on log-log axes, with reference lines of slope two and slope three.

| Element | Shows |
| --- | --- |
| Surface with a faint grey grid | the world the walker lives on: a ball, a saddle, a flat floor with a pole, or a made-up floor with twist |
| Solid blue leg, solid orange leg, dashed blue and dashed orange return legs | the four legs of the walk in order: first edge, second edge, first edge reversed, second edge reversed |
| Dotted red closing walk | the gap between the end of the four legs and the start, and the extra walk that closes the loop |
| Tinted region on the walker's left | the region whose curvature sets the turn |
| Grey dashed start arrow and solid green returned arrow in the base-corner inset | the arrow's change around the closed loop |
| Log-log side panel with reference slopes | how the turn or the gap scales with the size of the loop |
| Readout strip | the turn, the area, the turn over area, the change per cell, the Riemann component, the gap and what the bracket predicts |

## Book figure

Three panels. Left: a cell on a ball with the solid blue and orange legs, the dashed return legs, the tinted region on the walker's left, and the inset with the grey dashed start arrow and the solid green returned arrow a small angle apart; a smaller cell beside it with a smaller angle. Middle: the flat floor with a pole, the four legs of the two instructions ending short of the start, the dotted red closing walk, and an inset where the green arrow lies on the grey dashed one. Right: two routes from two arrows on a ball ending a small gap apart, with the gap marked in dotted red.

Labels: first edge, second edge, start, return, closing walk, gap, pole. Aspect 3:1. Alt text: Three drawings. On a ball, an arrow carried around a small four-sided cell comes back turned by a small angle, and a smaller cell gives a smaller angle. On a flat floor with a pole, four legs built from two walking instructions end short of the start, and after a short closing walk the carried arrow comes back matching. On a ball, two routes built from two arrows end a small gap apart.

## Variants

- **static** `static-card` (fallback): The print figure as an SVG card, used when 3D is unavailable and as a summary card.
- **plot** `flat-plots`: The log-log panel alone: turn against size for the cell, gap against size for the instructions and the two routes, with reference slopes two and three.
- **interactive-3d** `full-3d`: The full experience on every surface, with the three walk modes, presets, the size slider, edge-order swap, scrubbing and the side panel.

## Parameters

| Id | Label | Type | Options or range | Default | Available when | Effect |
| --- | --- | --- | --- | --- | --- | --- |
| `walk` | Walk | enum | cell, flow, two-routes | "cell" | — | Chooses what the four legs are. *cell*: walk the first grid direction, then the second, then each back, along grid lines; the legs close exactly. *flow*: walk the two unit instructions (directly away from the pole and around it on the floor; down the ball and along the circle of latitude on the ball), then each in reverse; the legs can miss the start, and a closing walk is added before the arrow is compared. *two-routes*: two arrows of equal length at right angles; route one walks along the first arrow carrying the second and then along the carried second, route two swaps them; a closing walk joins the two ends and the walker returns along route two. |
| `surface` | Surface | enum | plane, ball, saddle (walk in cell), twist (walk in two-routes) | "ball" | — | Switches the surface and rebuilds the walk on it. The floor uses polar coordinates about the pole; the ball has radius one metre and uses colatitude and longitude; the saddle is z = (x² − y²)/(2R) with R = 1 m and the walk starts at its centre; the twist floor is the flat floor with a changed carrying rule and no pole. |
| `size` | Size of each leg | number | 0.05–1 step 0.05 m | 0.5 | — | The length of each leg at the start, in metres. In cell mode the first edge is this long and the second grid step is chosen so that the second edge is this long at the base corner. In flow mode each instruction is followed for this distance. In two-routes mode both arrows are this long. Keep it small on the ball for the small-loop law to apply. |
| `pole-distance` | Distance from the pole | number | 2–20 step 1 m | 10 | surface in plane; walk in cell, flow | Where the walk starts on the flat floor, measured from the pole. Always larger than the size, so no leg reaches the pole. |
| `colatitude` | Colatitude of the start | number | 10–110 step 5 deg | 60 | surface in ball | Where the walk starts on the ball, measured down from the top point. The first grid direction runs down the ball, the second runs along the circle of latitude to the walker's left. |
| `twist-rate` | Twist | number | 0–60 step 5 deg | 20 | surface in twist | The made-up carrying rule: every metre walked along the first arrow's direction turns a carried arrow by this many degrees toward the walker's left; walking along the second arrow's direction leaves it alone. Zero recovers the flat floor. |
| `edge-order` | Edge order | enum | first-then-second, second-then-first | "first-then-second" | walk in cell, flow | Swaps which leg is walked first. The colours stay with the grid directions, so the orange leg is walked first when swapped; the tint moves to the other side and the turn changes sign. |
| `second-edge-factor` | Second edge length factor | number | 0.5–2 step 0.5 | 1 | walk in cell | Multiplies the second edge only, to show that the change is linear in each edge. Two gives two cells side by side. |
| `show-plot` | Show the size plot | boolean | — | false | — | Shows the log-log side panel of the turn (cell and flow modes) or the gap (two-routes mode) against the size, with reference lines of slope two and slope three, and marks the current size and half the current size. |
| `progress` | Walk progress | progress | 0–1 step 0.01 | 0 | — | Moves the walker and the carried arrow along the legs; the closing walk, when there is one, is the last stretch. On-complete readouts appear only at 1. |

## Presets

- `ball-cell` Cell on the ball: walk="cell", surface="ball", colatitude=60, size=0.5
- `ball-cell-small` Small cell on the ball: walk="cell", surface="ball", colatitude=60, size=0.1
- `ball-cell-swapped` Cell on the ball, second edge first: walk="cell", surface="ball", colatitude=60, size=0.5, edge-order="second-then-first"
- `ball-cell-double-second-edge` Two cells side by side on the ball: walk="cell", surface="ball", colatitude=60, size=0.5, second-edge-factor=2
- `polar-cell` Cell on the flat floor with a pole: walk="cell", surface="plane", pole-distance=10, size=1
- `saddle-cell` Cell on the saddle: walk="cell", surface="saddle", size=0.5
- `saddle-cell-small` Small cell on the saddle: walk="cell", surface="saddle", size=0.1
- `playground` Playground: ten metres from the pole: walk="flow", surface="plane", pole-distance=10, size=1
- `playground-near` Playground: five metres from the pole: walk="flow", surface="plane", pole-distance=5, size=1
- `playground-close` Playground: two metres from the pole: walk="flow", surface="plane", pole-distance=2, size=0.5
- `playground-swapped` Playground, instruction B first: walk="flow", surface="plane", pole-distance=10, size=1, edge-order="second-then-first"
- `ball-flow` Two instructions on the ball: walk="flow", surface="ball", colatitude=60, size=0.5
- `ball-flow-swapped` Two instructions on the ball, second first: walk="flow", surface="ball", colatitude=60, size=0.5, edge-order="second-then-first"
- `ball-flow-small` Two short instructions on the ball: walk="flow", surface="ball", colatitude=60, size=0.1
- `ball-flow-30` Two instructions at colatitude thirty degrees: walk="flow", surface="ball", colatitude=30, size=0.2
- `floor-two-routes` Two routes on the flat floor: walk="two-routes", surface="plane", size=0.5
- `ball-two-routes` Two routes on the ball: walk="two-routes", surface="ball", colatitude=60, size=0.5
- `twist-two-routes` Two routes on the floor with twist: walk="two-routes", surface="twist", twist-rate=20, size=0.5

## Readouts

- `turn` Turn of the returned arrow (deg; visible on-complete; 4 decimals; range (-180, 180]; sense: positive toward the walker's left, with the walker's head along the surface's normal: up from the floor, outward from the ball): “the arrow came back turned {abs} degrees to the left” / “the arrow came back turned {abs} degrees to the right”
- `half-size-turn` Turn at half size (deg; visible on-complete; 4 decimals; range (-180, 180]; sense: positive toward the walker's left, as for the turn): “with every leg halved, the arrow would come back turned {abs} degrees to the left” / “with every leg halved, the arrow would come back turned {abs} degrees to the right”
- `area` Area of the finished loop (m^2; visible on-complete; 4 decimals): “the finished loop fences off {value} square metres”
- `turn-over-area` Turn over area (m^-2; visible on-complete; 4 decimals; range (-10, 10]; sense: the turn in radians divided by the loop's area; positive toward the walker's left): “the turn divided by the area is {value} per square metre, toward the left” / “the turn divided by the area is {abs} per square metre, toward the right”
- `change-per-cell` Arrow change per cell (m^-2; visible on-complete; 4 decimals; range (-10, 10]; sense: the returned arrow's component along the second grid direction, in the orthonormal frame at the base corner, divided by the product of the two leg lengths at the start; positive toward the walker's left): “the arrow's sideways change divided by the two leg lengths is {value} per square metre, toward the left” / “the arrow's sideways change divided by the two leg lengths is {abs} per square metre, toward the right”
- `riemann-component` Riemann component (m^-2; visible on-demand; 4 decimals; range (-10, 10]; sense: the component with the returned direction and the carried arrow along the second and first grid directions, and the two edges in walking order, in the orthonormal frame at the base corner; by the small-loop law a positive value sends the arrow toward the walker's right): “the Riemann component for this cell is {value} per square metre” / “the Riemann component for this cell is minus {abs} per square metre”
- `gap` Gap left by the four legs (m; visible on-complete; 4 decimals; range (-10, 10]; sense: the length of the closing walk, positive when the four legs end on the counterclockwise side of the start around the pole, seen from above the floor, or on the east side of the start on the ball): “the four legs end {abs} metres from the start, on the counterclockwise side around the pole or the east side on the ball” / “the four legs end {abs} metres from the start, on the clockwise side around the pole or the west side on the ball”
- `bracket-gap` Gap the bracket predicts (m; visible on-demand; 4 decimals; range (-10, 10]; sense: the size squared times the Lie bracket of the two instruction fields at the start, in walking order; same sign rule as the gap): “the bracket predicts a gap of {abs} metres on the counterclockwise or east side” / “the bracket predicts a gap of {abs} metres on the clockwise or west side”
- `route-gap` Gap between the two route ends (m; visible on-complete; 6 decimals): “the two routes end {value} metres apart”
- `half-size-gap` Gap at half size (m; visible on-complete; 6 decimals): “with every leg halved, the gap would be {value} metres”
- `bare-commutator` Bare commutator (m^-2; visible on-demand; 4 decimals; range (-100, 100]; sense: the component along the second instruction's direction of the bare commutator of the two covariant derivatives applied to the carried arrow, in the orthonormal frame at the start; positive toward the walker's left): “the bare commutator's sideways component is {value} per square metre” / “the bare commutator's sideways component is minus {abs} per square metre”

## Tours

### `shrink-the-cell` · for [[riemann-curvature-tensor]] · entry

1. `meet-the-cell` (entry, await none) state: preset="ball-cell", progress=0  
   *Ball with a faint grey grid; at the base corner the solid blue first edge runs down the ball, the solid orange second edge runs along the circle of latitude to the walker's left, the return legs are dashed; the grey dashed arrow points along the blue edge.*  
   Say: “Here is a ball with a radius of one metre, with faint grey grid lines drawn on it. I stand at the corner where the solid blue line and the solid orange line meet. The blue line runs down the ball, half a metre long. The orange line runs to my left, along a circle of latitude, also half a metre long. I hold a cardboard arrow, drawn grey and dashed, pointing along the blue line, and I will never let it swing.”  
   Describe: A ball with grid lines. A four-sided cell sits on it, half a metre along each side. A cardboard arrow waits at one corner, pointing along the first side.
2. `walk-the-cell` (entry, await none) state: preset="ball-cell", progress=0; animate progress → 1 over 8 s  
   *The walker follows the blue edge, the orange edge, then the dashed blue and dashed orange return legs; faded arrow copies along the way; at the end the inset shows the solid green returned arrow about 16 degrees left of the grey dashed start arrow, and the turn readout appears.*  
   Say: “I walk down the solid blue line, turn left onto the solid orange line, then come back along the dashed blue line and the dashed orange line. The arrow never swings. Back at my corner, the solid green arrow shows where it points now. It is turned about sixteen degrees to my left from the grey dashed start arrow.”  
   Describe: The arrow goes around the four sides and comes back to the corner. The readout says sixteen degrees to the left.
3. `predict-the-half-size-turn` (entry, await prediction) state: preset="ball-cell", progress=1  
   *Same view, paused, with the size slider highlighted.*  
   Predict: “If I make both sides half as long, the cell covers a quarter of the area. Will the turn be a half of sixteen degrees, or a quarter?”  
   Say: “Now I will make both sides half as long, so the cell covers a quarter of the area it covered before. Make a guess. Will the arrow come back turned by half of sixteen degrees, or by a quarter of sixteen degrees?”  
   Describe: The same cell, paused at the end of the walk, before it is shrunk.
4. `quarter-the-area` (entry, await none) state: preset="ball-cell", size=0.25, progress=1  
   *A cell with quarter-metre sides; the turn readout shows 3.8 degrees and the turn-over-area readout shows 1 per square metre.*  
   Say: “Here is the smaller cell, with sides a quarter of a metre long. The solid green arrow is now turned about four degrees to my left, a quarter of sixteen. So the turn follows the area, not the length of a side. Look at the readout for the turn divided by the area. It reads one for the big cell and one for the small cell. That one number is what curving means at this spot on the ball.”  
   Describe: A smaller cell with sides a quarter of a metre long. The turn readout says about four degrees to the left. The turn divided by the area reads one, the same as before.
5. `two-cells-side-by-side` (entry, await none) state: preset="ball-cell-double-second-edge", progress=1  
   *The orange edge is doubled, so the cell is two of the original cells side by side; the turn readout shows 31.5 degrees.*  
   Say: “Now I make the solid orange line twice as long, one metre. That is two of the first cells side by side. The turn is about thirty-two degrees, twice sixteen. Here is why. The two cells share their middle side. Walking around both, I walk that side once each way, and those two trips cancel. So the turns of the two cells add up.”  
   Describe: A cell twice as wide, made of two of the first cells side by side. The readout says about thirty-two degrees to the left, twice the first turn.
6. `predict-the-swapped-order` (entry, await prediction) state: preset="ball-cell", progress=1; evidences `holonomy/checks/reverse-the-loop`  
   *The original cell, paused, with the edge-order control highlighted.*  
   Predict: “I set the arrow back to its start and walk the same cell the other way round: the orange side first, then the blue side. The first trip turned the arrow sixteen degrees to my left. How does the arrow come back now?”  
   Say: “I set the arrow back to its start. Now I walk the same cell the other way round: the solid orange line first, then the solid blue line, then each back. The first trip turned the arrow sixteen degrees to my left. Make a guess. How does the arrow come back this time?”  
   Describe: The first cell again. The arrow is back at its starting direction, and the walk is about to go round the other way.
7. `walk-the-other-way` (entry, await none) state: preset="ball-cell-swapped", progress=0; animate progress → 1 over 8 s  
   *The walker takes the orange edge first; the tint moves to the other side; the returned arrow is 16 degrees to the right; the turn readout shows minus 15.76 degrees.*  
   Say: “I walk along the solid orange line first, turn onto the solid blue line, and come back along the dashed lines. The tinted region is now on my right. The solid green arrow comes back turned sixteen degrees to my right, the same amount the other way. The second trip plays the first trip backwards, so it undoes the first turn.”  
   Describe: The arrow goes round the same cell the other way and comes back turned sixteen degrees to the right.
8. `earth-for-scale` (entry, await none) state: preset="ball-cell-small", progress=1  
   *The small cell on the ball with its readouts; a caption compares with Earth.*  
   Say: “On this one-metre ball, a cell a tenth of a metre on each side turns the arrow by about half a degree. Earth's ground is a ball too, but a huge one. A cell one metre on each side on Earth turns an arrow by about 1.4 trillionths of a degree. That is the angle across a hair's width seen from 3 million kilometres away. So nobody notices it in daily life.”  
   Describe: A small cell on the ball. The readout says about half a degree to the left. A caption gives the number for Earth's ground.

### `gap-is-not-curving` · for [[riemann-curvature-operator]] · entry

1. `two-instructions` (entry, await prediction) state: preset="playground-near", progress=0; evidences `riemann-curvature-operator/checks/playground-gap`  
   *Flat floor with a pole marked by a grey post; the walker stands five metres from it; the planned legs are drawn faintly: solid blue away from the pole, solid orange around it, dashed blue back toward it, dashed orange back around.*  
   Predict: “I do A, then B, then A in reverse, then B in reverse. Do I end at my starting spot? If not, about how far past it does my last walk carry me?”  
   Say: “Here is a flat floor with a pole, drawn as a grey post. I stand five metres from the pole. Instruction A: walk one metre directly away from the pole, along the solid blue line. Instruction B: walk one metre around the pole, keeping it on my left and staying the same distance from it, along the solid orange line. A in reverse means one metre directly toward the pole, the dashed blue line. B in reverse means one metre around the pole with the pole on my right, the dashed orange line. Make a guess. Do I end at my starting spot? If not, about how far past it does my last walk carry me?”  
   Describe: A flat floor with a pole. A walker stands five metres from the pole with four planned legs: away from the pole, around it, back toward it, and back around it.
2. `the-gap` (entry, await none) state: preset="playground-near", progress=0; animate progress → 0.85 over 8 s  
   *The walker follows the four legs and stops about 17 centimetres past the start; a dotted red closing walk appears between the end point and the start.*  
   Say: “I walk the solid blue line, the solid orange line, the dashed blue line and the dashed orange line. My last walk carries me about seventeen centimetres past my starting spot. The dotted red line shows the gap. Here is why. I did B six metres from the pole, and I did B in reverse five metres from the pole. The circle five metres out is only five sixths as long as the circle six metres out. So B in reverse needs only five sixths of a metre to reach my start, and the whole metre carries me one sixth of a metre further.”  
   Describe: The walker finishes the four legs about seventeen centimetres past the start. A dotted line marks the gap.
3. `does-the-gap-prove-curving` (entry, await prediction) state: preset="playground-near", progress=0.85; evidences `riemann-curvature-operator/checks/friend-on-a-flat-floor`  
   *Same view, paused at the gap, with the closing walk highlighted.*  
   Predict: “Maya says this gap proves the floor is curved. Is she right? What test would settle it?”  
   Say: “My friend Maya says this gap proves the floor is curved. Make a guess. Is she right? And what test would settle it?”  
   Describe: The walker stands at the gap, seventeen centimetres from the start, before the closing walk.
4. `close-the-loop-and-compare` (entry, await none) state: preset="playground-near", progress=0.85; animate progress → 1 over 3 s  
   *The walker takes the dotted red closing walk back to the start; the inset shows the solid green returned arrow lying on the grey dashed start arrow; the turn readout shows 0 degrees.*  
   Say: “The test is the arrow test on a finished loop. I walk the dotted red closing walk back to my start, so the path is now a loop. I carried the grey dashed arrow the whole way without letting it swing. The solid green arrow lies exactly on it. The arrow came back matching, as it does on every loop on a flat floor. So the gap came from the instructions, not from the floor.”  
   Describe: The walker closes the loop. The returned arrow points exactly the same way as the start arrow. The readout says zero degrees.
5. `same-instructions-on-a-ball` (entry, await none) state: preset="ball-flow", progress=0; animate progress → 1 over 8 s  
   *Ball with the same kind of instructions: solid blue down the ball, solid orange along the circle of latitude to the left, dashed return legs, a short dotted red closing walk; the returned arrow is about 14 degrees left of the start; the turn readout shows 13.65 degrees.*  
   Say: “Now the same kind of instructions on the one-metre ball. A: walk half a metre down the ball, the solid blue line. B: walk half a metre along the circle of latitude to my left, the solid orange line. Then A in reverse and B in reverse along the dashed lines. Here too the four legs miss the start, by about seven centimetres, and the dotted red closing walk finishes the loop. This time the solid green arrow comes back turned about fourteen degrees to my left. The ball is curved, so the finished loop turns the arrow.”  
   Describe: On the ball, the four legs miss the start by about seven centimetres, a short closing walk finishes the loop, and the arrow comes back turned about fourteen degrees to the left.
6. `predict-the-swapped-instructions` (entry, await prediction) state: preset="ball-flow", progress=1; evidences `riemann-curvature-operator/checks/swap-the-instructions`  
   *Same view, paused, with the edge-order control highlighted.*  
   Predict: “I set the arrow back to its start and do B first: B, then A, then B in reverse, then A in reverse, and the closing walk. How does the arrow come back this time?”  
   Say: “I set the arrow back to its start. Now I do B first: the solid orange line, then the solid blue line, then B in reverse, then A in reverse, and the closing walk. The first trip turned the arrow fourteen degrees to my left. Make a guess. How does the arrow come back this time?”  
   Describe: The arrow is back at its starting direction, and the instructions are about to be followed in the other order.
7. `swapped-instructions` (entry, await none) state: preset="ball-flow-swapped", progress=0; animate progress → 1 over 8 s  
   *The walker takes the orange leg first; the tint moves to the other side; the closing walk lies on the other side of the start; the returned arrow is 14 degrees to the right; the turn readout shows minus 13.65 degrees.*  
   Say: “I walk the solid orange line first, then the solid blue line, then the dashed lines, and the dotted red closing walk. The tinted region is now on my right, and the closing walk lies on the other side of my start. The solid green arrow comes back turned about fourteen degrees to my right. Doing the instructions in the other order walks nearly the same small loop the other way round, so the arrow turns the other way.”  
   Describe: With the instructions in the other order, the arrow comes back turned about fourteen degrees to the right.

### `walks-that-close` · for [[cyclic-identity]] · entry

1. `two-routes-on-the-floor` (entry, await none) state: preset="floor-two-routes", progress=1  
   *Flat floor; from the start, route one is solid blue then solid orange, route two is solid orange then solid blue; the two end dots coincide; the route-gap readout shows 0.*  
   Say: “I stand on a flat floor with two cardboard arrows, each half a metre long. The blue arrow points ahead of me and the orange arrow points to my left. Route one: I walk along the blue arrow to its tip, carrying the orange arrow without letting it swing. Then I walk on for half a metre in the direction the carried orange arrow points. Route two swaps the jobs: along the orange arrow first, carrying the blue one, then along the carried blue arrow. On the floor the two routes trace the four sides of a square, and their end dots sit on the same spot. The gap readout says zero.”  
   Describe: On a flat floor, two routes of two half-metre legs each end at the same spot. The gap readout says zero.
2. `two-routes-on-the-ball` (entry, await none) state: preset="ball-two-routes", progress=1  
   *Ball; the two routes end a small gap apart, marked by a dotted red segment; the route-gap readout shows 0.083 metres and the half-size-gap readout shows 0.011 metres.*  
   Say: “Now the same two routes on the one-metre ball, with the same half-metre arrows. Route one is the solid blue line then the solid orange line, and route two is the solid orange line then the solid blue line. Their end dots miss each other by about eight centimetres, the dotted red segment. So on a ball, walks built from two arrows need not close up.”  
   Describe: On the ball, the two routes end about eight centimetres apart.
3. `halve-the-arrows-on-the-ball` (entry, await none) state: preset="ball-two-routes", size=0.25, progress=1  
   *Both arrows halved to a quarter of a metre; the route-gap readout shows 0.011 metres; the plot panel shows the gap falling with slope three.*  
   Say: “I halve both arrows, to a quarter of a metre each. The square between the routes now covers a quarter of the area it covered before. The gap is about one centimetre, close to an eighth of eight centimetres. So the gap shrinks faster than the area. For a tiny cell that is what closing up means, because curving is measured per unit of area, and a gap that shrinks faster than the area counts for nothing.”  
   Describe: With the arrows halved, the gap falls from eight centimetres to about one centimetre, an eighth, while the area falls to a quarter.
4. `predict-the-twist-floor` (entry, await prediction) state: preset="twist-two-routes", progress=1; evidences `cyclic-identity/checks/a-space-with-twist`  
   *A flat floor drawn with a purple tint and a label that says twist, not allowed in general relativity; the two routes end about 9 centimetres apart.*  
   Predict: “On this made-up floor, every metre walked ahead turns a carried arrow twenty degrees to the left. The two routes end about nine centimetres apart. If I halve both arrows, will the gap become an eighth as big, as on the ball, or a quarter as big?”  
   Say: “Here is a made-up floor, tinted purple and labelled twist. The floor is flat, but the carrying rule is changed. Every metre I walk in the direction of the blue arrow turns any carried arrow twenty degrees to my left. Walking in the direction of the orange arrow leaves carried arrows alone. With the half-metre arrows, the two routes end about nine centimetres apart. Make a guess. If I halve both arrows, will the gap become an eighth as big, as it did on the ball, or a quarter as big?”  
   Describe: A made-up flat floor with a changed carrying rule. The two routes end about nine centimetres apart.
5. `halve-the-arrows-with-twist` (entry, await none) state: preset="twist-two-routes", size=0.25, progress=1  
   *Arrows halved on the twist floor; the route-gap readout shows 0.022 metres, a quarter of 0.087; the plot panel shows the gap falling with slope two; the turn readout shows 0 degrees.*  
   Say: “With the arrows halved, the gap is about two centimetres, a quarter of nine. So here the gap keeps pace with the area, and that is what twist means. The curving test still comes out flat. Look at the turn readout. An arrow carried around the finished loop, out along route one, across the dotted red gap and back along route two, comes back matching. So this floor has twist but no curving. The spaces of general relativity allow no twist, so in them tiny four-sided walks always close up.”  
   Describe: With the arrows halved, the gap falls to a quarter, keeping pace with the area. An arrow carried around the finished loop comes back matching.
6. `gap-orders` (working, await none) state: preset="twist-two-routes", show-plot=true, progress=1  
   *The plot panel with the twist floor's gap against size on the slope-two line and the ball's gap on the slope-three line.*  
   Say: “In the plot panel, the purple points for the twist floor lie on the reference line of slope two, and the ball's points lie on the line of slope three. With twist the gap is minus the torsion fed the two arrows, so it is proportional to the size squared, twenty degrees per metre times a quarter of a square metre gives nine centimetres. On the ball the torsion is zero and the gap is of order the size cubed, about the size cubed divided by the square root of two. That is why the cyclic identity, which cancels the trips' changes in pairs, needs a torsion-free connection and nothing else.”  
   Describe: A plot of gap against size: the twist floor's points follow a line of slope two, the ball's points a line of slope three.

### `small-loop-law` · for [[riemann-curvature-tensor]] · working

1. `name-the-slots` (working, await none) state: preset="ball-cell", progress=1  
   *Cell on the ball at colatitude 60 degrees, half-metre legs; readouts: turn 15.76 degrees, change per cell 1.086 per square metre, Riemann component minus 1 per square metre.*  
   Say: “On the ball I walk the solid blue edge a, along the colatitude direction, then the solid orange edge b, along the longitude direction, then each back. The carried arrow V starts along a. The small-loop law says the change of V is minus the Riemann tensor fed V, a and b, with the edges in walking order. The readout for the arrow's sideways change divided by the two leg lengths reads about 1.09 per square metre, and the Riemann component with the returned direction and the carried arrow along the orange and blue directions, in the orthonormal frame at the corner, reads minus 1 per square metre, which is minus one over the radius squared. The law predicts plus 1 for the change. The cell is not yet tiny.”  
   Describe: A half-metre cell on the ball. The change per cell reads about 1.09 per square metre, and the Riemann component reads minus 1 per square metre.
2. `shrink-to-the-law` (working, await none) state: preset="ball-cell", show-plot=true, progress=1; animate size → 0.1 over 6 s  
   *The cell shrinks to a tenth of a metre; the change-per-cell readout moves from 1.086 to 1.027; the plot shows the turn against size on the slope-two line.*  
   Say: “As I shrink the cell, the change per cell falls from 1.09 toward 1, the value the law predicts, and the turn in the plot panel follows the reference line of slope two: a quarter of the turn for half the size. The leftover at finite size is the second-order law's own error, of relative order the size squared.”  
   Describe: The cell shrinks to a tenth of a metre. The change per cell approaches 1 per square metre, and the plotted turn falls with the square of the size.
3. `predict-the-swap` (working, await prediction) state: preset="ball-cell", progress=1; evidences `riemann-curvature-tensor/checks/swap-the-edges`  
   *Same cell, paused, edge-order control highlighted.*  
   Predict: “Swap the edges: walk b first, then a. What happens to the change, and what happens to the Riemann component the readout prints?”  
   Say: “Now swap the edges: walk the solid orange edge b first, then the solid blue edge a. Predict what happens to the change per cell, and what the Riemann component readout will print with the edges in the new walking order.”  
   Describe: The half-metre cell, paused before the edges are swapped.
4. `swapped-edges` (working, await none) state: preset="ball-cell-swapped", progress=1  
   *The orange edge is walked first; the tint is on the walker's right; readouts: change per cell minus 1.086, Riemann component plus 1.*  
   Say: “With the solid orange edge first, the change per cell reads minus 1.09 per square metre and the Riemann component reads plus 1. Swapping the last two slots flips the sign, because walking the same cell the other way round undoes the first trip. The tensor is antisymmetric in its edge slots.”  
   Describe: With the edges swapped, the change per cell reads minus 1.09 and the Riemann component reads plus 1.
5. `double-one-edge` (working, await none) state: preset="ball-cell-double-second-edge", progress=1  
   *The orange edge doubled; the turn readout shows 31.52 degrees, twice 15.76.*  
   Say: “Doubling the solid orange edge b doubles the turn exactly, from 15.76 to 31.52 degrees. The law is linear in each edge, and on the ball the linearity in b is exact, because the cell's area is the longitude step times a fixed difference of cosines.”  
   Describe: With the second edge doubled, the turn doubles exactly.
6. `predict-the-polar-plane` (working, await prediction) state: preset="polar-cell", progress=0; evidences `riemann-curvature-tensor/checks/polar-plane-zero`  
   *Flat floor with the pole; the cell has the solid blue edge along the radius and the solid orange edge along the circle, one metre each, ten metres from the pole.*  
   Predict: “On this flat floor in polar coordinates the Christoffel symbol Gamma r phi phi equals minus r, which is not zero. A classmate says the floor must be curved. What will the change per cell read?”  
   Say: “Here is the flat floor in polar coordinates, with the grey grid of circles and spokes. The cell has the solid blue edge along a spoke and the solid orange edge along a circle, ten metres from the pole. The Christoffel symbol Gamma r phi phi equals minus r, which is not zero here. A classmate says the floor must be curved. Predict what the change per cell will read.”  
   Describe: A cell on the flat floor in polar coordinates, one metre along a spoke and one metre along a circle.
7. `polar-plane-reads-zero` (working, await none) state: preset="polar-cell", progress=1  
   *The walk completes; the green arrow lies on the grey dashed one; readouts: turn 0, change per cell 0, Riemann component 0.*  
   Say: “The solid green arrow lies exactly on the grey dashed one, and the change per cell reads zero. The derivative term of the component formula gives minus 1 and the product term gives plus 1, so the Riemann component is zero. Christoffel symbols describe the bending of the grid lines; only the Riemann tensor describes curving.”  
   Describe: On the flat floor the arrow comes back matching. The change per cell and the Riemann component both read zero.
8. `saddle-flips-the-sign` (working, await none) state: preset="saddle-cell-small", progress=1  
   *A small cell at the centre of the saddle; readouts: turn minus 0.567 degrees, change per cell minus 0.99, Riemann component plus 1 per square metre.*  
   Say: “At the centre of the saddle, with the same slots, the Riemann component reads plus 1 per square metre and the change per cell reads minus 0.99, toward my right. Here the Gaussian curvature is minus one per square metre. The saddle turns the arrow the other way from the ball, by the same rule.”  
   Describe: A small cell at the centre of the saddle. The arrow comes back turned about half a degree to the right, and the Riemann component reads plus 1 per square metre.

### `operator-minus-the-bracket` · for [[riemann-curvature-operator]] · working

1. `gap-equals-the-bracket` (working, await none) state: preset="playground", progress=1  
   *Playground ten metres from the pole, one-metre instructions; readouts: gap minus 0.0909 metres, bracket gap minus 0.1 metres.*  
   Say: “The instructions are the unit fields e r and e phi on the floor. Flowing one metre along each and back leaves the walker 9.1 centimetres clockwise of the start, the dotted red closing walk. The bracket of e r and e phi is minus e phi over r, so the size squared times the bracket predicts ten centimetres clockwise. The two agree to leading order; the difference is of higher order in the size.”  
   Describe: On the floor, the four legs end 9.1 centimetres clockwise of the start, and the bracket predicts 10 centimetres.
2. `predict-the-bare-commutator` (working, await prediction) state: preset="playground-close", progress=1; evidences `riemann-curvature-operator/checks/polar-unit-frame`  
   *Playground two metres from the pole, half-metre instructions; the closed loop and the matching arrows; the bare commutator readout is on demand.*  
   Predict: “Two metres from the pole, with u equals e r, v equals e phi and the arrow w equals e r, a classmate computes the bare commutator of the covariant derivatives along u and v acting on w, finds minus e phi over four square metres, and concludes the floor is curved. What do the bracket term and the curvature operator give?”  
   Say: “Now two metres from the pole. With u equals e r, v equals e phi and the carried arrow w equals e r, a classmate computes the bare commutator, the covariant derivative along u of the covariant derivative along v of w, minus the same in the other order. The classmate finds minus e phi over four square metres and concludes the floor is curved. Predict what the bracket term and the curvature operator give.”  
   Describe: The four legs two metres from the pole, closed and with the arrow back matching.
3. `subtract-the-bracket-term` (working, await none) state: preset="playground-close", progress=1  
   *Readouts: bare commutator minus 0.25 per square metre, Riemann component 0, turn 0.*  
   Say: “The bare commutator readout confirms minus 0.25 per square metre along e phi. But the fields do not commute: their bracket is minus e phi over r, and the covariant derivative of w along the bracket is also minus e phi over r squared. Subtracting it leaves the curvature operator at zero, which the Riemann component readout prints. The solid green arrow lying on the grey dashed one is the same fact seen on the loop: the bare commutator counts the gap, and the closing walk removes it.”  
   Describe: The bare commutator reads minus 0.25 per square metre, the Riemann component reads zero, and the arrow comes back matching.
4. `predict-on-the-ball` (working, await prediction) state: preset="ball-flow-30", progress=1; evidences `riemann-curvature-operator/problems/sphere-unit-frame`  
   *Ball at colatitude 30 degrees, instructions of a fifth of a metre; the closed loop and a turned arrow.*  
   Predict: “On the ball at colatitude thirty degrees, with u equals e theta, v equals e phi and w equals e theta, how does the bare commutator compare with the curvature operator?”  
   Say: “On the ball at colatitude thirty degrees, take u equals e theta down the ball, v equals e phi along the circle of latitude, and the carried arrow w equals e theta. Predict how the bare commutator compares with the curvature operator here.”  
   Describe: The four legs on the ball at colatitude thirty degrees, closed, with the arrow back turned slightly to the left.
5. `the-operator-on-the-ball` (working, await none) state: preset="ball-flow-30", progress=1  
   *Readouts: bare commutator minus 4 per square metre, Riemann component minus 1 per square metre, turn 2.02 degrees.*  
   Say: “The bare commutator reads minus 4 per square metre along e phi, minus one over sine squared of thirty degrees. The curvature operator reads minus 1 per square metre, minus one over the radius squared. The bare commutator overstates the curvature fourfold, and the bracket term, minus cotangent squared of thirty degrees, makes up the difference.”  
   Describe: The bare commutator reads minus 4 per square metre and the Riemann component reads minus 1 per square metre.
6. `change-is-minus-the-operator` (working, await none) state: preset="ball-flow-small", progress=1  
   *Ball at colatitude 60 degrees, instructions of a tenth of a metre; readouts: change per cell 0.976 per square metre, Riemann component minus 1.*  
   Say: “With short instructions at colatitude sixty degrees, the arrow's change around the closed loop divided by the size squared reads 0.98 per square metre toward my left, approaching minus the curvature operator, plus 1. The closing walk is of order the size squared long and adds no area at that order, so the change around the finished loop is minus the operator times the size squared, exactly as the small-loop law says.”  
   Describe: With short instructions, the change per cell reads 0.98 per square metre, close to plus 1, minus the operator.

### `area-rule-to-riemann` · for [[holonomy]] · working

1. `area-rule-on-a-cell` (working, await none) state: preset="ball-cell", progress=1  
   *Half-metre cell on the ball; readouts: turn 15.76 degrees, area 0.2751 square metres, turn over area 1 per square metre.*  
   Say: “The area rule says the turn is the area on the walker's left divided by the radius squared. The cell fences off 0.275 square metres on my left, the tinted region, and the solid green arrow is 15.76 degrees left of the grey dashed one, which is 0.275 radians. The turn over area readout is exactly 1 per square metre, one over the radius squared, for a cell of any size.”  
   Describe: A half-metre cell on the ball. The turn is 15.76 degrees to the left, the area is 0.275 square metres, and the turn over area reads 1 per square metre.
2. `predict-the-halfway-readout` (working, await prediction) state: preset="ball-cell", progress=0.5; evidences `holonomy/checks/halfway-readout`  
   *The walker paused at the far corner of the cell; no turn readout is shown.*  
   Predict: “The walker is halfway round, at the far corner. What should a turn readout say here?”  
   Say: “I stop halfway round, at the far corner where the solid orange edge ends. Predict what a turn readout should say here.”  
   Describe: The walker is paused at the far corner of the cell. No readout is shown.
3. `no-halfway-turn` (working, await none) state: preset="ball-cell", progress=0.5  
   *Same view; the readout strip stays empty.*  
   Say: “The readout stays hidden, on purpose. The arrow here and the arrow at my start sit at different points of a curved surface, and comparing them needs a route, which changes the answer. The turn is defined only when the loop closes and both arrows sit at the same point.”  
   Describe: The readout strip stays empty while the walker is away from the start.
4. `shrink-and-read-the-tensor` (working, await none) state: preset="ball-cell-small", show-plot=true, progress=1  
   *Small cell; readouts: turn 0.589 degrees, turn over area 1, change per cell 1.027, Riemann component minus 1; the plot shows slope two.*  
   Say: “Shrunk to a tenth of a metre, the turn is 0.59 degrees, but the turn over area is still 1 per square metre. On a surface every tiny loop lies in one tangent plane, so one number serves. In more dimensions a tiny cell can lie in different planes and carry different arrows, so the number becomes a table. The change per cell readout, the arrow's change divided by the two edge lengths, reads 1.03 and approaches minus the Riemann component, minus minus 1: the small-loop law, with the carried arrow, the two edges in order and the returned direction as its four slots.”  
   Describe: A small cell. The turn over area still reads 1 per square metre, and the change per cell reads 1.03, approaching minus the Riemann component.
5. `predict-polar-coordinates` (working, await prediction) state: preset="polar-cell", progress=0; evidences `holonomy/checks/polar-coordinates-plane`  
   *Cell on the flat floor in polar coordinates, ten metres from the pole.*  
   Predict: “In polar coordinates on the flat floor the Christoffel symbol Gamma r phi phi equals minus r is not zero. Does a small loop there return the arrow rotated?”  
   Say: “On the flat floor in polar coordinates, the cell runs along a spoke, the solid blue edge, and along a circle, the solid orange edge. The Christoffel symbol Gamma r phi phi equals minus r is not zero here. Predict whether this small loop returns the arrow rotated.”  
   Describe: A cell on the flat floor in polar coordinates, before the walk.
6. `polar-loop-returns-unchanged` (working, await none) state: preset="polar-cell", progress=1  
   *The walk completes; the green arrow lies on the grey dashed one; readouts: turn 0, Riemann component 0.*  
   Say: “The solid green arrow lies on the grey dashed one: no rotation. The small-loop law sets the change by the Riemann tensor, which vanishes for the flat metric d r squared plus r squared d phi squared. The nonzero Christoffel symbols describe the curved grid lines, not curved ground.”  
   Describe: On the flat floor the arrow comes back matching, and the Riemann component reads zero.

## Design rules

- **Show no turn, area or gap readout while the walker is away from the start; the readout strip fills only when the loop is closed.** Because: Arrows at different points of a curved surface cannot be compared without a route, so a running angle would show a number that has no meaning. Prevents `holonomy/misconceptions/running-angle-halfway`.
- **In flow mode, draw the dotted red closing walk and carry the arrow across it before the inset compares the arrows, and show the gap readout separately from the turn readout.** Because: Learners take the gap itself as a sign of curving; the flat floor's nonzero gap beside its zero turn separates the instructions' failure to commute from curvature. Prevents `riemann-curvature-operator/misconceptions/gap-means-curving`.
- **Draw the flat floor's polar grid of circles and spokes prominently, and keep the flat-floor cell one click away from the ball's cell.** Because: Seeing curved grid lines return the arrow unchanged is what dissolves the belief that nonzero Christoffel symbols mean curvature. Prevents `riemann-curvature-tensor/misconceptions/christoffels-mean-curvature`.
- **Make the edge-order swap visibly symmetric: the same legs with the colours kept on their grid directions, the tint moving to the other side, the closing walk on the other side of the start, and the opposite turn.** Because: Learners expect the two orders to give the same change; the mirrored picture with the opposite readout shows that the swapped order walks nearly the same loop the other way. Prevents `riemann-curvature-operator/misconceptions/order-does-not-matter`.
- **Never show the bare commutator readout alone; show it beside the Riemann component readout and the turn, with the flat floor's nonzero bare commutator and zero turn as a preset.** Because: A nonzero bare commutator on a flat floor is the fastest cure for taking the commutator of covariant derivatives along any two fields as curvature. Prevents `riemann-curvature-operator/misconceptions/bare-commutator-is-curvature`.
- **Tint the twist floor purple, label it as not allowed in general relativity, and show its zero turn beside its nonzero gap.** Because: The cyclic identity holds only where tiny four-sided walks close up; a floor with twist and no curving shows that the rule is about the connection, not a fact about every space. Prevents `cyclic-identity/misconceptions/holds-in-every-space`.
- **Plot the turn or the gap against the leg size on log-log axes with reference lines of slope two and slope three, and mark the current size and half the current size.** Because: The difference between a gap that keeps pace with the area and one that shrinks faster is a difference of slope, which the eye reads from a log-log plot at once.
- **Distinguish the first and second legs, the return legs, the closing walk, and the start and returned arrows by line style as well as colour.** Because: Colour alone fails for colour-blind learners and in print.

## Model

The arrow is carried by integrating the transport equation in the surface's own coordinates; the ball's legs are great-circle arcs and circles of latitude handled exactly by rotations, the flat floor and the twist floor are handled in closed form, and the saddle by fourth-order Runge–Kutta. The turn is the rotation from the start arrow to the returned arrow at the start, positive toward the walker's left with the walker's head along the surface's normal, reported on the branch from minus 180 degrees, exclusive, to 180 degrees. The gap is the geodesic distance from the end of the four legs to the start, signed by the side of the start on which the walker ends, and the closing walk is the geodesic from that end point to the start. The cell, flow and two-routes modes share the surfaces and the readouts; readouts that a mode does not define are hidden in it. Lengths are metres and the ball has radius one metre.

**Transport rule**

$$
\frac{dV^a}{ds} + \Gamma^a{}_{bc}\,\frac{dx^b}{ds}\,V^c = 0
$$

Holds when: Surface coordinates; the Levi-Civita connection of the surface metric on the floor, the ball and the saddle; the twist connection on the twist floor.

**Small-loop law**

$$
\Delta V^\rho = -R^\rho{}_{\sigma\mu\nu}\,V^\sigma a^\mu b^\nu
$$

Holds when: To second order in the edges; $a$ is the first edge walked and $b$ the second. The change-per-cell readout reports $\Delta V^{\hat v}/(|a|\,|b|)$ in the orthonormal frame at the base corner, and the Riemann component readout reports $R^{\hat v}{}_{\hat u\mu\nu}$ there with $\mu\nu$ in walking order, so the readout tends to minus the component as the size tends to zero.

**Components from the connection**

$$
R^\rho{}_{\sigma\mu\nu} = \partial_\mu\Gamma^\rho{}_{\nu\sigma} - \partial_\nu\Gamma^\rho{}_{\mu\sigma} + \Gamma^\rho{}_{\mu\lambda}\Gamma^\lambda{}_{\nu\sigma} - \Gamma^\rho{}_{\nu\lambda}\Gamma^\lambda{}_{\mu\sigma}
$$

Holds when: Coordinate basis. On the ball, $R^\phi{}_{\theta\theta\phi} = -1$ for radius one metre, so the orthonormal component is $-1/a^2$. On the flat floor in polar coordinates, $\Gamma^r{}_{\phi\phi} = -r$ and $\Gamma^\phi{}_{r\phi} = 1/r$ give $R^r{}_{\phi r\phi} = -1 + 1 = 0$. On the saddle at the origin, $R^y{}_{xxy} = +1/R^2$.

**Turn of a grid cell on the ball**

$$
\Delta\alpha = \Delta\phi\,\big(\cos\theta_0 - \cos(\theta_0 + \Delta\theta)\big),\qquad \Delta\theta = \epsilon,\quad \Delta\phi = \frac{f\,\epsilon}{\sin\theta_0}
$$

Holds when: Radius one metre; base corner at colatitude $\theta_0$; first edge down the ball of length $\epsilon$, second edge along the circle of latitude of length $f\epsilon$ at the base corner; walking order colatitude then longitude puts the cell on the walker's left. The swapped order gives $-\Delta\alpha$. Exact by the local Gauss–Bonnet theorem, and exactly linear in $f$.

**Saddle surface**

$$
z = \frac{x^2 - y^2}{2R},\qquad K = -\frac{1}{R^2}\Big(1 + \frac{x^2 + y^2}{R^2}\Big)^{-2},\qquad \Gamma^k{}_{ij} = \frac{f_k\, f_{ij}}{1 + f_x^2 + f_y^2}
$$

Holds when: $R = 1$ m; the cell starts at the centre with the first edge along $x$ and the second along $y$; the turn equals $\iint K\,dA$ over the cell, toward the walker's right.

**Curvature operator and the flow loop**

$$
\mathcal R(u,v)w = \nabla_u\nabla_v w - \nabla_v\nabla_u w - \nabla_{[u,v]}w,\qquad \Delta w = -\epsilon^2\,\mathcal R(u,v)w + O(\epsilon^3)
$$

Holds when: Flow mode: parameter distance $\epsilon$ along $u$, then $v$, then back along each, then the closing geodesic. The four legs end at $\epsilon^2[u,v] + O(\epsilon^3)$ from the start. On the floor $u = e_r$, $v = e_\phi$, $[u,v] = -e_\phi/r$, and with $w = e_r$ the bare commutator is $-e_\phi/r^2$, the bracket term $-e_\phi/r^2$ and the operator $0$. On the ball $u = e_\theta$, $v = e_\phi$, $[u,v] = -\cot\theta\, e_\phi$, and with $w = e_\theta$ the bare commutator is $-e_\phi/\sin^2\theta$, the bracket term $-\cot^2\theta\, e_\phi$ and the operator $-e_\phi$ for radius one metre.

**Gap of the flow loop**

$$
\phi_{\rm end} = \frac{\epsilon}{r_0 + \epsilon} - \frac{\epsilon}{r_0},\qquad g_{\rm floor} = -2 r_0 \sin\frac{|\phi_{\rm end}|}{2};\qquad \phi_{\rm end} = \frac{\epsilon}{\sin(\theta_0+\epsilon)} - \frac{\epsilon}{\sin\theta_0}
$$

Holds when: Grid order, first instruction away from the pole or down the ball. The gap is signed positive on the counterclockwise or east side of the start. On the ball the gap is the great-circle distance between the end point and the start at the same colatitude. The swapped order ends on the other side with the same distance. The enclosed area of the closed loop is the grid cell's area minus the sliver between the closing geodesic and the circle through the start, of order $\epsilon^6$.

**Gap between two routes on the ball**

$$
|{\rm end}_1 - {\rm end}_2| = \sqrt{2}\,\sin\epsilon\,(1 - \cos\epsilon) \approx \frac{\epsilon^3}{\sqrt 2}
$$

Holds when: Unit ball; arrows of length $\epsilon$ at right angles; each leg a great-circle arc and the carried arrow perpendicular to the plane of the arc, so it is unchanged along it. The reported route gap is the great-circle distance $2\arcsin$ of half this chord. The closed loop (route one, the closing geodesic, route two reversed) is a geodesic pentagon whose holonomy equals its area.

**Twist floor**

$$
\Gamma^x{}_{xy} = t,\quad \Gamma^y{}_{xx} = -t,\qquad T^x{}_{xy} = t,\qquad R^\rho{}_{\sigma\mu\nu} = 0,\qquad |{\rm gap}| = 2\epsilon\sin\frac{t\epsilon}{2} \approx t\epsilon^2 = |T(a,b)|
$$

Holds when: Cartesian coordinates on the flat floor with normal up; $t$ is the twist rate in radians per metre; the legs are the floor's straight lines, and autoparallels of the twist connection give the same gap at order $\epsilon^2$. Metric compatible, so lengths are kept. The connection is flat, so every closed loop returns the arrow unchanged. Not a geometry of general relativity, which has zero torsion; the mode exists only to show what zero torsion buys.

**Method:** Ball: legs along meridians and circles of latitude are rotations about the ball's axis or about the meridian's normal, great-circle legs and the closing geodesic are rotations about the arc's normal, and the returned arrow is the composition of these rotations applied to the start arrow; areas of the grid cell and the sliver come from closed forms and one-dimensional quadrature, and the two-routes pentagon's area from its angle excess. Flat floor: closed forms in polar coordinates. Saddle: fourth-order Runge–Kutta transport along the four coordinate legs with 4000 steps per leg, the area and the curvature integral by midpoint quadrature on a 400 by 400 grid; the turn was cross-checked against the curvature integral to seven decimals and the arrow's length against one to nine decimals. Twist floor: closed form. Half-size readouts rerun the same computation with every leg halved. The plot panel samples the turn or the gap at sizes from 0.05 to 1 metre.

| Test | State | Expect | Hidden | Note |
| --- | --- | --- | --- | --- |
| `ball-cell-half-metre` | preset="ball-cell", progress=1 | turn = 15.7592981 ±1e-05; area = 0.2750516 ±1e-06; turn-over-area = 1 ±1e-08; change-per-cell = 1.0863865 ±1e-06; riemann-component = -1 ±1e-09; half-size-turn = 3.8008929 ±1e-05; gap = 0 ±1e-09 | route-gap, bracket-gap, half-size-gap, bare-commutator | Colatitude 60 degrees, edges 0.5 m: the turn equals the cell's area, 0.57735 × (cos 60° − cos 88.65°) = 0.27505 rad; the change per cell is sin(0.27505)/0.25; the orthonormal component is −1/$a^2$ with a = 1 m. Grid legs close, so the gap is zero. |
| `ball-cell-small` | preset="ball-cell-small", progress=1 | turn = 0.5885294 ±1e-06; area = 0.0102718 ±1e-07; change-per-cell = 1.0271596 ±1e-06; turn-over-area = 1 ±1e-08; half-size-turn = 0.1452468 ±1e-06 | route-gap, bracket-gap, half-size-gap, bare-commutator | Small-size leading order: the change per cell approaches minus the component, 1 per square metre, with a leftover of relative order the size squared. |
| `ball-cell-swapped-order` | preset="ball-cell-swapped", progress=1 | turn = -15.7592981 ±1e-05; turn-over-area = -1 ±1e-08; change-per-cell = -1.0863865 ±1e-06; riemann-component = 1 ±1e-09; half-size-turn = -3.8008929 ±1e-05 | route-gap, bracket-gap, half-size-gap, bare-commutator | Walking the second edge first puts the cell on the walker's right: every signed readout flips, and the component with the edges in walking order is R^$φ_θφθ$ = +1. |
| `ball-cell-double-second-edge` | preset="ball-cell-double-second-edge", progress=1 | turn = 31.5185962 ±1e-05; area = 0.5501033 ±1e-06; change-per-cell = 1.0455505 ±1e-06; half-size-turn = 7.6017858 ±1e-05 | route-gap, bracket-gap, half-size-gap, bare-commutator | Doubling the longitude step doubles the turn exactly: two cells side by side, sharing a leg walked once each way. The change per cell divides by the doubled product of leg lengths. |
| `polar-cell-flat` | preset="polar-cell", progress=1 | turn = 0 ±1e-09; area = 1.05 ±1e-09; change-per-cell = 0 ±1e-09; riemann-component = 0 ±1e-12; half-size-turn = 0 ±1e-09; gap = 0 ±1e-09 | route-gap, bracket-gap, half-size-gap, bare-commutator | Flat case: nonzero Christoffel symbols, zero Riemann tensor, no turn. Area 0.1 rad × (11^2 − 10^2)/2 $m^2$ = 1.05 $m^2$. |
| `saddle-cell-half-metre` | preset="saddle-cell", progress=1 | turn = -11.536959 ±0.0002; area = 0.2697592 ±5e-05; turn-over-area = -0.7464357 ±0.0005; change-per-cell = -0.8 ±0.0005; riemann-component = 1 ±1e-09; half-size-turn = -3.3722867 ±0.0002 | route-gap, bracket-gap, half-size-gap, bare-commutator | Negative curvature: the arrow returns toward the walker's right by ∬K dA over the cell, −0.201359 rad; the component at the origin is R^$y_xxy$ = +1/$R^2$. The cell is far from tiny, so the turn over area is well below 1 in size. |
| `saddle-cell-small` | preset="saddle-cell-small", progress=1 | turn = -0.5672942 ±0.0001; change-per-cell = -0.990099 ±0.0005; turn-over-area = -0.9868334 ±0.0005; riemann-component = 1 ±1e-09 | route-gap, bracket-gap, half-size-gap, bare-commutator | Small-size leading order on the saddle: the change per cell approaches minus the component, −1 per square metre. |
| `no-readouts-while-moving` | preset="ball-cell", progress=0.5 | — | turn, half-size-turn, area, turn-over-area, change-per-cell, gap, route-gap, half-size-gap | Design rule no-running-readouts: nothing on-complete shows before the loop closes. |
| `playground-ten-metres` | preset="playground", progress=1 | gap = -0.0909088 ±1e-06; bracket-gap = -0.1 ±1e-09; bare-commutator = -0.01 ±1e-09; riemann-component = 0 ±1e-12; turn = 0 ±1e-09; change-per-cell = 0 ±1e-09; area = 0.9545392 ±1e-06; half-size-gap = 0.0238095 ±1e-06 | route-gap | The four legs end 1/110 rad clockwise at r = 10 m: chord 2 × 10 × sin(1/220) = 0.0909088 m, about 9 centimetres; the bracket predicts $\epsilon$^2/$r_0$ = 0.1 m; the bare commutator is −1/$r_0$^2 along $e_φ$; the floor is flat so the turn is zero. Area: the grid cell 0.9545455 $m^2$ minus the sliver 6.3 × 10^-^6 $m^2$. |
| `playground-five-metres` | preset="playground-near", progress=1 | gap = -0.166659 ±1e-06; bracket-gap = -0.2 ±1e-09; bare-commutator = -0.04 ±1e-09; turn = 0 ±1e-09 | route-gap | The playground-gap check: about 17 centimetres past the start, 1/6 m to leading order. |
| `playground-two-metres` | preset="playground-close", progress=1 | bare-commutator = -0.25 ±1e-09; bracket-gap = -0.125 ±1e-09; gap = -0.0999896 ±1e-06; riemann-component = 0 ±1e-12 | route-gap | The polar-unit-frame check: bare commutator −$e_φ$/(4 $m^2$), operator zero. |
| `playground-swapped-order` | preset="playground-swapped", progress=1 | gap = 0.0909088 ±1e-06; bracket-gap = 0.1 ±1e-09; turn = 0 ±1e-09 | route-gap | Instruction B first: the walker ends the same distance counterclockwise of the start, and the bracket in walking order is [$e_φ$, $e_r$] = +$e_φ$/r. |
| `ball-flow-sixty` | preset="ball-flow", progress=1 | gap = -0.0668625 ±1e-06; bracket-gap = -0.1443376 ±1e-06; bare-commutator = -1.3333333 ±1e-06; riemann-component = -1 ±1e-09; turn = 13.6509292 ±0.0002; change-per-cell = 0.9440239 ±0.0001; area = 0.2382537 ±2e-05; half-size-gap = 0.0251293 ±1e-06 | route-gap | Unit fields at colatitude 60 degrees with half-metre steps: the walker ends west of the start, the bracket −cot 60° $e_φ$ predicts 0.144 m, the bare commutator is $-1/\sin^2 60^\circ$, the operator −1/$a^2$. Turn = grid cell area 0.2382681 minus a sliver of 1.4 × 10^-^5 rad. |
| `ball-flow-swapped-order` | preset="ball-flow-swapped", progress=1 | turn = -13.6509292 ±0.0002; gap = 0.0668625 ±1e-06; bracket-gap = 0.1443376 ±1e-06; change-per-cell = -0.9440239 ±0.0001 | route-gap | The swap-the-instructions check: the same loop the other way round, the walker ending east of the start, the arrow turned the other way. |
| `ball-flow-below-the-equator` | preset="ball-flow", colatitude=110, size=0.1, progress=1 | gap = 0.0037181 ±1e-06; bracket-gap = 0.0036397 ±1e-06; riemann-component = -1 ±1e-09 | route-gap | Below the equator the circles of latitude shrink downward, so the walker ends east of the start in grid order: the gap and the bracket, −cot 110° = +0.36397 per metre, are both positive. |
| `ball-flow-thirty` | preset="ball-flow-30", progress=1 | bare-commutator = -4 ±1e-09; riemann-component = -1 ±1e-09; bracket-gap = -0.069282 ±1e-06; gap = -0.0489475 ±1e-06; turn = 2.017059 ±0.0001 | route-gap | The sphere-unit-frame problem: bare commutator $-1/\sin^2 30^\circ$ = −4 per square metre, operator −1 per square metre; the bare commutator overstates the curvature fourfold. |
| `ball-flow-small-steps` | preset="ball-flow-small", progress=1 | change-per-cell = 0.9757921 ±1e-05; gap = -0.005001 ±1e-06; bracket-gap = -0.0057735 ±1e-06; turn = 0.5590965 ±1e-05 | route-gap | Small-size leading order for the flow loop: the change per cell approaches minus the operator, +1 per square metre, and the gap approaches the bracket's prediction. |
| `floor-two-routes-meet` | preset="floor-two-routes", progress=1 | route-gap = 0 ±1e-09; half-size-gap = 0 ±1e-09; area = 0.25 ±1e-09; turn = 0 ±1e-09 | gap, bracket-gap, bare-commutator, change-per-cell, riemann-component | On the flat floor the two routes trace a square and meet exactly. |
| `ball-two-routes-half-metre` | preset="ball-two-routes", progress=1 | route-gap = 0.0830241 ±1e-06; half-size-gap = 0.010877 ±1e-06; area = 0.2305573 ±1e-06; turn = 13.2099629 ±1e-05; turn-over-area = 1 ±1e-06 | gap, bracket-gap, bare-commutator, change-per-cell, riemann-component | Chord √2 sin 0.5 (1 − cos 0.5) = 0.0830003 m, great-circle distance 0.0830241 m; halving the arrows divides the gap by 7.63, close to 8. The closed pentagon's holonomy equals its area, 0.2305573 rad. |
| `ball-two-routes-small` | preset="ball-two-routes", size=0.1, progress=1 | route-gap = 0.0007053 ±1e-07; half-size-gap = 8.83e-05 ±1e-07; turn = 0.5710529 ±1e-05 | gap, bracket-gap, bare-commutator, change-per-cell, riemann-component | Small-size leading order: gap ≈ $\epsilon$^3/√2 = 0.000707 m, and halving divides it by 7.98. |
| `twist-two-routes-twenty-degrees` | preset="twist-two-routes", progress=1 | route-gap = 0.0871557 ±1e-06; half-size-gap = 0.0218097 ±1e-06; area = 0.228294 ±1e-06; turn = 0 ±1e-09; turn-over-area = 0 ±1e-09 | gap, bracket-gap, bare-commutator, change-per-cell, riemann-component | Gap 2$\epsilon$ sin(t$\epsilon$/2) with t = 20°/m: 0.0872 m against t$\epsilon$^2 = 0.0873 m; halving divides it by 3.996, so the gap keeps pace with the area. The connection is flat, so the closed loop returns the arrow unchanged. |
| `twist-rate-zero` | preset="twist-two-routes", twist-rate=0, progress=1 | route-gap = 0 ±1e-09; area = 0.25 ±1e-09; turn = 0 ±1e-09 | gap, bracket-gap, bare-commutator, change-per-cell, riemann-component | Boundary case: zero twist recovers the flat floor. |
| `twist-largest-legs` | preset="twist-two-routes", size=1, progress=1 | route-gap = 0.3472964 ±1e-06; half-size-gap = 0.0871557 ±1e-06 | gap, bracket-gap, bare-commutator, change-per-cell, riemann-component | Boundary case at the largest size: 2 sin 10° = 0.3473 m, and the half-size gap is the half-metre case. |

## Serves

- [[holonomy]]: the cell on the ball with its turn, area and turn-over-area readouts, shrinking to the small-loop law, the hidden halfway readout, and the polar-coordinate floor
- [[riemann-curvature-tensor]]: the change-per-cell and Riemann-component readouts with the edges in walking order, the edge swap, the doubled edge, the polar floor's zero and the saddle's opposite sign
- [[riemann-curvature-operator]]: the flow mode: the gap the instructions leave, the closing walk, the bracket's prediction, and the bare commutator beside the operator on the floor and the ball
- [[cyclic-identity]]: the two-routes mode: routes that meet on the floor, miss by a gap of order size cubed on the ball, and miss by a gap of order size squared on the twist floor, with the closed loop's zero turn there

## In the visual network

- **Builds on:** [[carry-an-arrow-around-a-loop]]
- **Leads to:** [[cube-of-small-loops]], [[four-terms-that-cancel]], [[twenty-of-256-slots]]

## Accessibility

Every tour beat has a spoken description of the legs, the gap and where the returned arrow points relative to the start. Readouts are announced in degrees, metres and per square metre, with left or right and the side of the start named. Legs, return legs, the closing walk and the two arrows differ in line style as well as colour, and every control works from the keyboard.

Static alternative: On a ball, an arrow carried around a small four-sided cell comes back turned by a small angle to the left, and a cell with half the sides gives a quarter of the angle. On a flat floor with a pole, four legs built from two walking instructions end short of the start, and after a short closing walk the carried arrow comes back matching. Two routes built from two arrows meet on the floor and end a small gap apart on the ball.

- `Space`: play or pause the walk
- `Left and Right arrows`: scrub along the legs
- `Up and Down arrows`: grow or shrink the size
- `S`: swap the edge order
- `1 to 3`: choose the cell, flow, or two-routes walk
- `B, F, D, T`: choose the ball, the flat floor, the saddle, or the twist floor
- `P`: show or hide the size plot

## Starting material

Earlier course assets: `scene-3d-parallel-transport-loop`, `scene-3d-parallel-transport-two-routes`, `lab-flow-order-lie-bracket`, `lab-polar-coordinates-two-addresses`, `figure-polar-metric`

The earlier course's transport module and its two-routes lab give the ball and flat-floor transport; its flow-order lab gives the four legs of two instructions and the gap. New work: the polar grid cell with the change-per-cell and Riemann-component readouts, the closing walk with the bracket and bare-commutator readouts, the saddle, the twist floor, the half-size readouts and the log-log panel. Merged from the planned visuals shrink-the-loop-to-find-riemann, four-legs-that-do-not-close and two-routes-that-meet.
