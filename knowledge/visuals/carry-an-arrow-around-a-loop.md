---
type: "visual"
schema_version: 2
id: "carry-an-arrow-around-a-loop"
title: "Carry an arrow around a loop"
kind: "interactive-3d"
priority: "flagship"
status: "proposed"
revision: 1
rungs: ["entry", "working"]
serves: ["parallel-transport", "path-dependence-of-parallel-transport", "holonomy", "gaussian-curvature", "angular-excess", "intrinsic-versus-extrinsic-curvature", "curvature-of-the-two-sphere", "flatness-criterion"]
builds_on: ["slide-an-arrow-along-a-path"]
leads_to: ["shrink-the-loop-to-find-riemann", "paper-cone-with-a-missing-wedge", "arrow-around-a-circle-of-latitude"]
---

# Carry an arrow around a loop

`carry-an-arrow-around-a-loop` · interactive-3d · flagship · proposed · rungs: entry, working

> Carry an arrow around a loop without letting it swing: on a ball it usually comes back turned, and on a flat sheet it never does.

## What it makes visible

An arrow carried around a loop without ever swinging comes back turned on a ball, but not on a flat floor or a rolled-up tube. On a ball the turn grows with the fenced-off area, wrapping around after a full turn, so the equator returns the arrow unchanged. The turn reverses when the loop is walked the other way. It is the one picture behind parallel transport, path dependence, holonomy, Gaussian curvature, and the meaning of the Riemann tensor.

## The picture

A shaded surface with a faint grid fills the scene. A loop is drawn on it, the region on the walker's left is lightly tinted, and small arrowheads along the loop show the walking direction. Faded copies of the carried arrow mark its progress. At the base point, an inset shows the starting arrow as a grey dashed line and the returned arrow as a solid orange line, with an arc between them. Readouts for the turn and the area appear only when the loop closes.

| Element | Shows |
| --- | --- |
| Surface with a faint grid | the world the walker lives on: flat floor, tube, ball, saddle, or cone |
| Loop with direction arrowheads | the path and which way it is walked |
| Tinted region on the walker's left | the fenced-off patch whose curvature sets the turn |
| Faded arrow copies along the loop | the arrow being carried without swinging |
| Base-point inset with a grey dashed start arrow and a solid orange returned arrow | the holonomy as the angle between two arrows at the same point |
| Readouts: turn, area, area over radius squared, angle excess | the area rule, shown only once the loop closes |

## Book figure

Two panels. Left: a ball with the three-stretch loop from the North Pole, the arrow drawn at each stretch (ahead, right, behind), and an inset at the pole showing the dashed start arrow and the solid returned arrow a right angle apart. Right: a square walk on a flat sheet, where every arrow copy points the same way.

Labels: North Pole, equator, start, return, quarter turn, flat sheet. Aspect 2:1. Alt text: On a ball, an arrow carried around a three-sided loop from the North Pole returns a quarter turn away from its start; on a flat sheet, an arrow carried around a square returns unchanged.

## Variants

- **static** `static-card` (fallback): The print figure as an SVG card, used when 3D is unavailable and as a summary card.
- **interactive-2d** `unrolled-2d`: Unrolled views of the tube and the cone, where carrying the arrow is plain sliding and the seam adds any turn.
- **interactive-3d** `full-3d`: The full experience on every surface, with presets, loop editing, reversal, radius changes, and scrubbing.

## Parameters

| Id | Label | Type | Options or range | Default | Effect |
| --- | --- | --- | --- | --- | --- |
| `surface` | Surface | enum | plane, tube, ball, saddle, cone | "ball" | Switches the surface; the loop is rebuilt on it. |
| `loop` | Loop | enum | octant-triangle, square, latitude-circle, bracelet, around-tip, avoid-tip, two-routes, free | "octant-triangle" | Chooses the loop shape; not every shape exists on every surface. |
| `direction` | Walking direction | enum | counterclockwise, clockwise | "counterclockwise" | Reverses the walk; arrowheads and the sign of the turn flip together. |
| `area-fraction` | Loop size | number | 0.05–1 | 1 | Scales the fenced-off area relative to the chosen shape. |
| `radius` | Ball radius | number | 0.5–10 scene units | 1 | Changes the ball's size; the loop keeps its angles. |
| `colatitude` | Colatitude | number | 5–175 deg | 60 | Moves the circle of latitude, measured down from the North Pole. |
| `wedge-angle` | Missing wedge | number | 0–300 deg | 60 | Sets the wedge removed to make the cone. |
| `windings` | Times around the tip | integer | 1–4 | 1 | Repeats the loop around the cone's tip. |
| `progress` | Walk progress | progress | 0–1 | 0 | Moves the arrow along the loop; readouts appear only at 1. |
| `unrolled` | Unroll | boolean | — | false | Shows the flat sheet beside the tube or cone. |
| `path` | Drawn loop | path | — | null | Vertices of a user-drawn loop when the loop is set to draw your own. |

## Presets

- `octant` North Pole triangle: surface="ball", loop="octant-triangle", direction="counterclockwise"
- `octant-reversed` North Pole triangle, walked the other way: surface="ball", loop="octant-triangle", direction="clockwise"
- `octant-half-area` Half-size triangle: surface="ball", loop="octant-triangle", area-fraction=0.5
- `latitude-circle` Circle of latitude: surface="ball", loop="latitude-circle", colatitude=60
- `two-routes` Two routes to one point: surface="ball", loop="two-routes"
- `flat-square` Square on a flat floor: surface="plane", loop="square"
- `tube-bracelet` Around the tube: surface="tube", loop="bracelet"
- `tube-unrolled` Around the tube, unrolled: surface="tube", loop="bracelet", unrolled=true
- `saddle-square` Square on a saddle: surface="saddle", loop="square"
- `cone-around-tip` Around the cone's tip: surface="cone", loop="around-tip", wedge-angle=60
- `cone-avoid-tip` Away from the cone's tip: surface="cone", loop="avoid-tip", wedge-angle=60

## Readouts

- `turn` Turn (deg), visible on-complete: “the arrow came back turned by {value} degrees”
- `area` Fenced-off area (scene units squared), visible on-complete: “the loop fences off an area of {value}”
- `area-over-radius-squared` Area over radius squared (rad), visible on-complete: “the area divided by the radius squared is {value}”
- `angle-excess` Angle excess (deg), visible on-complete: “the corners add up to {value} degrees more than half a turn”
- `arrow-length` Arrow length (scene units), visible on-demand: “the arrow's length is {value}”

## Guided tour

1. `meet-the-walk` (entry, await none) state: preset="octant", progress=0  
   *Ball with the three-stretch loop; the arrow at the North Pole points along the first stretch.*  
   Say: “Here is a ball. The path starts at the top, goes straight to the middle line, runs a quarter of the way along it, and comes straight back to the top. I will carry this arrow along the path and never let it swing left or right.”  
   Describe: A ball with a three-sided path that starts at the top. A flat arrow sits at the top, pointing along the first side.
2. `predict-the-return` (entry, await prediction) state: preset="octant", progress=0  
   *Same view, paused.*  
   Predict: “When the arrow gets back to the top, will it point the same way it points now?”  
   Say: “Before we walk, make a guess. When the arrow gets back to the top, will it point the same way it points now?”  
   Describe: The arrow waits at the top of the ball, pointing along the first side of the path.
3. `first-stretch` (entry, await none) state: preset="octant", progress=0; animate progress → 0.33 over 4 s  
   *The arrow travels to the equator, pointing along the path.*  
   Say: “On the first stretch, the arrow points straight ahead of the walker.”  
   Describe: The arrow moves from the top to the middle line, pointing along the path the whole way.
4. `first-corner` (entry, await none) state: preset="octant", progress=0.33; animate progress → 0.67 over 5 s  
   *At the corner the path turns left; the arrow keeps its direction and travels along the equator pointing to the walker's right.*  
   Say: “At the corner, the walker turns left by a quarter turn. The arrow does not swing, so now it points to the walker's right. It keeps pointing right along the middle line.”  
   Describe: The path turns left along the middle line. The arrow now points to the right of the direction of travel.
5. `second-corner` (entry, await none) state: preset="octant", progress=0.67; animate progress → 1 over 4 s  
   *At the second corner the path turns left again; the arrow travels back to the pole pointing behind the walker.*  
   Say: “At the next corner, the walker turns left again. Now the arrow points straight behind the walker, all the way back to the top.”  
   Describe: The path turns left toward the top. The arrow points backward along the path until it reaches the top.
6. `compare-at-home` (entry, await none) state: preset="octant", progress=1  
   *Inset at the pole: grey dashed start arrow and solid orange returned arrow, a right angle apart; turn readout shows 90 degrees.*  
   Say: “We are back at the top. The grey dashed arrow shows how the arrow pointed when we left. The solid orange arrow shows how it points now. They are a quarter turn apart, yet the arrow never swung.”  
   Describe: Two arrows at the top of the ball, one dashed and one solid, at a right angle to each other. The readout says 90 degrees.
7. `flat-floor-control` (entry, await none) state: preset="flat-square", progress=1  
   *Square walk on the flat floor; the solid arrow lies exactly on the dashed one.*  
   Say: “Now a square walk on a flat floor, with four corners. The solid arrow lands exactly on the dashed one. On a flat floor, the arrow comes back unturned.”  
   Describe: A square path on a flat floor. The start arrow and the returned arrow point the same way. The readout says 0 degrees.
8. `tube-control` (entry, await none) state: preset="tube-unrolled", progress=1  
   *Loop around the tube, with the unrolled sheet beside it; arrows on the sheet all point the same way.*  
   Say: “A rolled-up tube looks curved, but a loop around it brings the arrow back unturned. Look at the unrolled sheet. Nothing stretched, and the arrow slides straight across the flat paper, so it did not turn on the tube either.”  
   Describe: A tube with a loop around it, and beside it the same paper laid flat. On the flat paper the loop is a straight line and every arrow copy points the same way.
9. `half-the-patch` (working, await none) state: preset="octant-half-area", progress=1  
   *A smaller triangle fencing off half the area; turn readout shows 45 degrees.*  
   Say: “Now the loop fences off half as much of the ball, on our left as we walk. The turn is half as big, an eighth of a turn instead of a quarter.”  
   Describe: A smaller triangle on the ball. The readout says 45 degrees.

## Design rules

- **Never show a turn angle while the arrow is moving.** Because: Arrows at different places on a curved surface cannot be compared independently of the route; the turn exists only when the loop closes. Prevents `holonomy/misconceptions/running-angle-halfway`.
- **Keep the flat floor and the tube one click away from the ball.** Because: Learners otherwise blame the corners for the turn. Prevents `holonomy/misconceptions/corners-caused-the-turn`.
- **Show the unrolled sheet beside the tube whenever the tube is on screen.** Because: Seeing the flat sheet is what dissolves the belief that a tube must turn the arrow. Prevents `holonomy/misconceptions/tube-must-turn`.
- **Make reversal visibly symmetric: the same loop, mirrored arrowheads, and the opposite turn.** Because: Many learners believe the walking direction does not matter. Prevents `holonomy/misconceptions/direction-does-not-matter`.
- **Describe the arrow relative to the path (ahead, right, behind), never with compass words.** Because: At the North Pole every direction is south, so compass words hide the turn and make the result sound contradictory. Prevents `holonomy/misconceptions/never-swung-so-never-turned`.
- **On the cone, make loops that avoid the tip the easiest thing to draw.** Because: Seeing them return unchanged, next to a loop around the tip that does not, is the whole lesson about flat regions and loops that cannot be shrunk. Prevents `holonomy/misconceptions/flat-along-loop-means-no-turn`.
- **Distinguish the start and returned arrows by line style as well as colour.** Because: Colour alone fails for colour-blind learners and in print.

## Model

The arrow is carried by integrating the transport equation in the surface's own coordinates. The 3D arrow is drawn by mapping its components through the surface embedding, so the embedding never affects the physics. The tube and cone use their unrolled flat charts, where transport is translation and the seam identification adds any rotation.

**Transport rule**

$$
\frac{dV^a}{ds} + \Gamma^a{}_{bc}\,\frac{dx^b}{ds}\,V^c = 0
$$

Holds when: Surface coordinates; Levi-Civita connection of the surface metric.

**Turn from enclosed curvature**

$$
\Delta\alpha = \iint_S K\,dA \pmod{2\pi}
$$

Holds when: Simple loop; region $S$ on the walker's left, containing no cone point or hole; positive in the sense of the walk.

**Turn on a ball**

$$
\Delta\alpha = A/a^2 \pmod{2\pi}
$$

Holds when: Simple loop on a sphere of radius $a$.

**Turn around a circle of latitude**

$$
\Delta\alpha = 2\pi(1 - \cos\theta_0) \pmod{2\pi}
$$

Holds when: Walking east around the circle at colatitude $\theta_0$.

**Turn around a cone's tip**

$$
\Delta\alpha = n\,\delta
$$

Holds when: Loop winding $n$ times around the tip of a cone made by removing a wedge of angle $\delta$, in the sense of circulation; zero for loops that do not enclose the tip.

**Method:** Fourth-order Runge–Kutta in surface coordinates, switching to a rotated chart near coordinate poles. Great-circle legs are cross-checked against exact rotations. The enclosed curvature for the readouts is integrated numerically from the metric.

| Test | State | Expect | Note |
| --- | --- | --- | --- |
| `octant-unit-radius` | preset="octant" | turn = 90 ±1e-06; area-over-radius-squared = 1.5707963268 ±1e-08; angle-excess = 90 ±1e-06 | Three right angles; one eighth of the sphere. |
| `octant-any-radius` | preset="octant", radius=2.5 | turn = 90 ±1e-06 | A triangle with fixed angles keeps its turn on a bigger ball. |
| `octant-reversed` | preset="octant-reversed" | turn = -90 ±1e-06 | The turn readout is positive counterclockwise, seen from outside the ball. |
| `half-area` | preset="octant-half-area" | turn = 45 ±1e-06 | Half the area gives half the turn. |
| `latitude-45` | preset="latitude-circle", colatitude=45 | turn = 105.44155877 ±0.0001 | Counterclockwise form of the same rotation as 254.56 degrees clockwise. |
| `flat-square` | preset="flat-square" | turn = 0 ±1e-09 | A flat floor never turns the arrow. |
| `tube-bracelet` | preset="tube-bracelet" | turn = 0 ±1e-09 | A tube is intrinsically flat, including loops that go around it. |
| `cone-around-tip` | preset="cone-around-tip" | turn = 60 ±1e-06 | Turn equals the wedge angle. |
| `cone-twice-around` | preset="cone-around-tip", windings=2 | turn = 120 ±1e-06 | Two windings give twice the wedge angle. |
| `cone-avoid-tip` | preset="cone-avoid-tip" | turn = 0 ±1e-09 | Loops that do not enclose the tip return unchanged. |
| `length-conserved` | preset="latitude-circle", colatitude=30 | arrow-length = 1 ±1e-09 | Transport preserves length. |

## Serves

- [[parallel-transport]]: the faded arrow copies and the no-swing rule
- [[path-dependence-of-parallel-transport]]: the two-routes preset
- [[holonomy]]: the returned arrow, the base-point inset, and every control case
- [[gaussian-curvature]]: the area readouts on the ball and the saddle's opposite turn
- [[angular-excess]]: the angle-excess readout for triangles
- [[intrinsic-versus-extrinsic-curvature]]: the tube and its unrolled view
- [[curvature-of-the-two-sphere]]: the radius slider and the area over radius squared readout
- [[flatness-criterion]]: the flat floor, tube, and cone cases

## In the visual network

- **Builds on:** [[slide-an-arrow-along-a-path]]
- **Leads to:** [[shrink-the-loop-to-find-riemann]], [[paper-cone-with-a-missing-wedge]], [[arrow-around-a-circle-of-latitude]]

## Accessibility

Every tour beat has a spoken description of where the arrow points relative to the path. The returned turn is announced in degrees. Start and returned arrows differ in line style as well as colour, and every control works from the keyboard.

Static alternative: On a ball, an arrow carried around a three-sided loop from the North Pole returns a quarter turn away from its start. On a flat floor and on a tube, arrows carried around loops return unchanged.

- `Space`: play or pause the walk
- `Left and Right arrows`: scrub along the loop
- `R`: reverse the walking direction
- `1 to 5`: choose flat floor, tube, ball, saddle, or cone
- `U`: unroll the tube or cone

## Starting material

Earlier course assets: `scene-3d-parallel-transport-loop`, `scene-3d-parallel-transport-two-routes`, `figure-sphere-holonomy`, `scene-3d-sphere-holonomy`

The earlier course's transport model and its checks can be ported almost unchanged as a TypeScript module, and its two-routes lab becomes a preset of this visual. Its octant SVG becomes the static card. New work: saddle and cone surfaces, unrolled views, area readouts, and preset-driven state.
