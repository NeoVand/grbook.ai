---
type: "visual"
schema_version: 2
id: "carry-an-arrow-around-a-loop"
title: "Carry an arrow around a loop"
kind: "interactive-3d"
priority: "flagship"
status: "proposed"
revision: 4
rungs: ["entry", "working"]
serves: ["parallel-transport", "path-dependence-of-parallel-transport", "holonomy", "gaussian-curvature", "angular-excess", "intrinsic-versus-extrinsic-curvature", "curvature-of-the-two-sphere", "flatness-criterion", "integrability-condition-for-parallel-fields", "normal-curvature"]
builds_on: ["slide-an-arrow-along-a-path"]
leads_to: ["four-legs-around-a-tiny-loop"]
---

# Carry an arrow around a loop

`carry-an-arrow-around-a-loop` · interactive-3d · flagship · proposed · rungs: entry, working

> Carry an arrow around a loop without letting it swing: on a ball it usually comes back turned, and on a flat sheet it never does.

## What it makes visible

An arrow carried around a loop without ever swinging comes back turned on a ball, but not on a flat floor or a rolled-up tube. On a ball the turn follows the area on the walker's left, wrapping around after a full turn, so the equator returns the arrow matching its start. The turn reverses when the loop is walked the other way. It is the one picture behind parallel transport, path dependence, holonomy, Gaussian curvature, and the meaning of the Riemann tensor.

## The picture

A shaded surface with a faint grid fills the scene. A loop is drawn on it, the region on the walker's left is lightly tinted, and small arrowheads along the loop show the walking direction. Faded copies of the carried arrow mark its progress. At the base point, an inset shows the starting arrow as a grey dashed line and the returned arrow as a solid orange line, with an arc between them. Readouts for the turn and the area appear only when the loop closes.

| Element | Shows |
| --- | --- |
| Surface with a faint grid | the world the walker lives on: flat floor, tube, ball, saddle, or cone |
| Loop with direction arrowheads | the path and which way it is walked |
| Tinted region on the walker's left | the region whose curvature sets the turn |
| Faded arrow copies along the loop | the arrow being carried without swinging |
| Base-point inset with a grey dashed start arrow and a solid orange returned arrow | the holonomy as the angle between two arrows at the same point |
| Readouts: turn, area, area over radius squared, angle excess | the area rule, shown only once the loop closes |

## Book figure

Two panels. Left: a ball with the three-stretch loop from the North Pole, the arrow drawn on each stretch (ahead, right, behind), and an inset at the pole showing the dashed start arrow and the solid returned arrow a right angle apart. Right: a square walk on a flat sheet, where every arrow copy points the same way.

Labels: North Pole, equator, start, return, quarter turn, flat sheet. Aspect 2:1. Alt text: On a ball, an arrow carried around a three-sided loop from the North Pole returns a quarter turn away from its start; on a flat sheet, an arrow carried around a square returns unchanged.

## Variants

- **static** `static-card` (fallback): The print figure as an SVG card, used when 3D is unavailable and as a summary card.
- **interactive-2d** `unrolled-2d`: Unrolled views of the tube and the cone, where carrying the arrow is plain sliding and the seam adds any rotation.
- **interactive-3d** `full-3d`: The full experience on every surface, with presets, loop editing, reversal, radius changes, and scrubbing.

## Parameters

| Id | Label | Type | Options or range | Default | Available when | Effect |
| --- | --- | --- | --- | --- | --- | --- |
| `surface` | Surface | enum | plane, tube, ball, saddle, cone | "ball" | — | Switches the surface; the loop is rebuilt on it. |
| `loop` | Loop | enum | octant-triangle (surface in ball), square (surface in plane, saddle), latitude-circle (surface in ball), bracelet (surface in tube), around-tip (surface in cone), avoid-tip (surface in cone), two-routes (surface in ball), free | "octant-triangle" | — | Chooses the loop shape on the current surface. The square on the plane has side 0.4 scene units; on the saddle it is the projection of the square with corners at plus or minus 0.2R. |
| `direction` | Walking direction | enum | counterclockwise, clockwise | "counterclockwise" | — | Reverses the walk; arrowheads, the tinted region, and the sign of the turn change together. |
| `area-fraction` | Loop size | number | 0.05–1 step 0.05 | 1 | loop in octant-triangle, square | Scales the loop about its centroid, along geodesics, so that the enclosed area is this fraction of the preset shape's area. |
| `radius` | Ball radius | number | 0.5–10 step 0.5 scene units | 1 | surface in ball | Changes the ball's size; the loop keeps its angles. |
| `saddle-scale` | Saddle scale R | number | 0.5–5 step 0.5 scene units | 1 | surface in saddle | The saddle is z = (x² − y²)/(2R) over \|x\|, \|y\| ≤ 0.5R. |
| `colatitude` | Colatitude | number | 5–175 step 1 deg | 50 | loop in latitude-circle | Moves the circle of latitude, measured down from the North Pole; the circle is walked eastward. |
| `wedge-angle` | Missing wedge | number | 0–300 step 5 deg | 60 | surface in cone | Sets the wedge removed to make the cone. |
| `windings` | Times around the tip | integer | 1–4 step 1 | 1 | loop in around-tip | Repeats the loop around the cone's tip. |
| `progress` | Walk progress | progress | 0–1 step 0.01 | 0 | — | Moves the arrow along the loop; on-complete readouts appear only at 1. |
| `unrolled` | Unroll | boolean | — | false | surface in tube, cone | Shows the flat sheet beside the tube or cone. |
| `path` | Drawn loop | path | — | null | loop in free | Vertices of a user-drawn loop. |

## Presets

- `octant` North Pole triangle: surface="ball", loop="octant-triangle", direction="counterclockwise"
- `octant-reversed` North Pole triangle, walked the other way: surface="ball", loop="octant-triangle", direction="clockwise"
- `octant-half-area` Half-size triangle: surface="ball", loop="octant-triangle", area-fraction=0.5
- `latitude-circle` Circle of latitude: surface="ball", loop="latitude-circle", colatitude=50
- `two-routes` Two routes to one point: surface="ball", loop="two-routes"
- `flat-square` Square on a flat floor: surface="plane", loop="square"
- `tube-bracelet` Around the tube: surface="tube", loop="bracelet"
- `tube-unrolled` Around the tube, unrolled: surface="tube", loop="bracelet", unrolled=true
- `saddle-square` Square on a saddle: surface="saddle", loop="square"
- `cone-around-tip` Around the cone's tip: surface="cone", loop="around-tip", wedge-angle=60
- `cone-avoid-tip` Away from the cone's tip: surface="cone", loop="avoid-tip", wedge-angle=60

## Readouts

- `turn` Turn (deg; visible on-complete; 1 decimals; range (-180, 180]; sense: positive toward the walker's left, which is counterclockwise seen from outside the surface): “the arrow came back turned {abs} degrees to the left” / “the arrow came back turned {abs} degrees to the right”
- `area` Area on the walker's left (scene units squared; visible on-complete; 3 decimals): “the loop fences off an area of {value} square units”
- `area-over-radius-squared` Area over radius squared (rad; visible on-complete; 3 decimals; range (0, 12.566370614]): “the area divided by the radius squared is {value} radians”
- `angle-excess` Angle excess (deg; visible on-complete; 1 decimals; range (-180, 540]; sense: angle sum minus a straight angle): “the corners add up to {abs} degrees more than a straight angle” / “the corners add up to {abs} degrees less than a straight angle”
- `arrow-length` Arrow length (scene units; visible on-demand; 9 decimals): “the arrow's length is {value}”

## Tours

### `holonomy-first-walk` · for [[holonomy]] · entry

1. `meet-the-walk` (entry, await none) state: preset="octant", progress=0  
   *Ball with the three-stretch loop; the arrow at the North Pole points along the first stretch.*  
   Say: “Here is a ball. The top point is the North Pole, and the circle around the middle is the equator. I will walk straight from the North Pole to the equator, a quarter of the way along the equator, and straight back. I will carry this arrow and never let it swing left or right.”  
   Describe: A ball with a three-sided path that starts at the top. A cardboard arrow sits at the top, pointing along the first side.
2. `predict-the-return` (entry, await prediction) state: preset="octant", progress=0; evidences `holonomy/checks/octant-walk-prediction`  
   *Same view, paused.*  
   Predict: “When the arrow gets back to the North Pole, will it point the same way it points now?”  
   Say: “Before I walk, make a guess. When the arrow gets back to the North Pole, will it point the same way it points now?”  
   Describe: The arrow waits at the North Pole, pointing along the first side of the path.
3. `first-stretch` (entry, await none) state: preset="octant", progress=0; animate progress → 0.33 over 4 s  
   *The arrow travels to the equator, pointing along the path.*  
   Say: “On the first stretch, the arrow points ahead of me.”  
   Describe: The arrow moves from the North Pole to the equator, pointing along the path the whole way.
4. `first-corner` (entry, await none) state: preset="octant", progress=0.33; animate progress → 0.67 over 5 s  
   *At the corner the path heads along the equator; the arrow keeps its direction and points to the walker's right.*  
   Say: “At the corner, I turn left by a quarter turn. The arrow does not swing, so now it points to my right, and it keeps pointing to my right all along the equator.”  
   Describe: The path now runs along the equator. The arrow points to the right of the direction of travel.
5. `second-corner` (entry, await none) state: preset="octant", progress=0.67; animate progress → 1 over 4 s  
   *At the second corner the path heads back to the pole; the arrow points behind the walker.*  
   Say: “At the next corner, I turn left again. Now the arrow points behind me, all the way back to the North Pole.”  
   Describe: The path heads back to the North Pole. The arrow points backward along the path until it arrives.
6. `compare-at-home` (entry, await none) state: preset="octant", progress=1  
   *Inset at the pole: grey dashed start arrow and solid orange returned arrow, a right angle apart; the turn readout shows 90 degrees.*  
   Say: “I am back at the North Pole. The grey dashed arrow shows how the arrow pointed when I set off. The solid orange arrow shows how it points now. They are a quarter turn apart, yet the arrow never swung.”  
   Describe: Two arrows at the North Pole, one dashed and one solid, at a right angle to each other. The readout says 90 degrees to the left.
7. `flat-floor-control` (entry, await none) state: preset="flat-square", progress=1; evidences `holonomy/checks/square-on-a-floor`  
   *Square walk on the flat floor; the solid arrow lies exactly on the dashed one.*  
   Say: “Now I walk a square on a flat floor, with four corners. The solid arrow lands exactly on the dashed one. On a flat floor, the arrow comes back matching its start.”  
   Describe: A square path on a flat floor. The start arrow and the returned arrow point the same way. The readout says 0 degrees.
8. `tube-control` (entry, await none) state: preset="tube-unrolled", progress=1; evidences `holonomy/checks/loop-around-a-tube`  
   *Loop around the tube, with the unrolled sheet beside it; arrow copies on the sheet all point the same way.*  
   Say: “A rolled-up tube looks curved, but a loop around it brings the arrow back matching its start. Look at the unrolled sheet. Nothing stretched, and the arrow slides across the flat paper without swinging.”  
   Describe: A tube with a loop around it, and beside it the same paper laid flat. On the flat paper the loop is a straight line and every arrow copy points the same way.
9. `half-the-patch` (working, await none) state: preset="octant-half-area", progress=1  
   *A smaller triangle fencing off half the area; the turn readout shows 45 degrees.*  
   Say: “Now the piece of the ball on my left is half as big as before. So the turn is half as big, an eighth of a turn instead of a quarter.”  
   Describe: A smaller triangle on the ball. The readout says 45 degrees to the left.

## Design rules

- **Never show a turn angle while the arrow is moving.** Because: Arrows at different places on a curved surface cannot be compared independently of the route; the turn exists only when the loop closes. Prevents `holonomy/misconceptions/running-angle-halfway`.
- **Keep the flat floor and the tube one click away from the ball.** Because: Learners otherwise blame the corners for the turn. Prevents `holonomy/misconceptions/corners-caused-the-turn`.
- **Show the unrolled sheet beside the tube whenever the tube is on screen.** Because: Seeing the flat sheet dissolves the belief that a tube must turn the arrow. Prevents `holonomy/misconceptions/tube-must-turn`.
- **Make reversal visibly symmetric: the same loop, mirrored arrowheads, the tint moving to the other side, and the opposite turn.** Because: Many learners believe the walking direction does not matter. Prevents `holonomy/misconceptions/direction-does-not-matter`.
- **Describe the arrow relative to the path (ahead, right, behind), never with compass words.** Because: At the North Pole every direction is south, so compass words hide the turn and make the result sound contradictory. Prevents `holonomy/misconceptions/never-swung-so-never-turned`.
- **On the cone, make loops that avoid the tip the easiest thing to draw.** Because: Seeing them return unchanged, next to a loop around the tip that does not, is the lesson about flat regions and loops that cannot be shrunk. Prevents `holonomy/misconceptions/flat-along-loop-means-no-turn`.
- **Distinguish the start and returned arrows by line style as well as colour.** Because: Colour alone fails for colour-blind learners and in print.

## Model

The arrow is carried by integrating the transport equation in the surface's own coordinates. The 3D arrow is drawn by mapping its components through the surface embedding, so the embedding never affects the physics. The tube and cone use their unrolled flat charts, where transport is translation and the seam identification adds any rotation. The turn readout reports the rotation from the start arrow to the returned arrow, positive toward the walker's left, on the branch from minus 180 (exclusive) to 180 degrees.

**Transport rule**

$$
\frac{dV^a}{ds} + \Gamma^a{}_{bc}\,\frac{dx^b}{ds}\,V^c = 0
$$

Holds when: Surface coordinates; Levi-Civita connection of the surface metric.

**Turn from enclosed curvature**

$$
\Delta\alpha = \iint_S K\,dA \pmod{2\pi}
$$

Holds when: Simple loop; region $S$ on the walker's left, containing no cone point or hole; positive toward the walker's left.

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
\Delta\alpha = n\,\delta \pmod{2\pi}
$$

Holds when: Loop winding $n$ times around the tip, with the tip on the walker's left, of a cone made by removing a wedge of angle $\delta$; zero for loops that do not enclose the tip.

**Saddle surface**

$$
z = \frac{x^2 - y^2}{2R},\qquad K = -\frac{1}{R^2}\left(1 + \frac{x^2 + y^2}{R^2}\right)^{-2}
$$

Holds when: Over $|x|, |y| \le 0.5R$; the square loop is the projection of the square with corners at $(\pm 0.2R, \pm 0.2R)$, walked counterclockwise seen from above.

**Method:** Fourth-order Runge–Kutta in surface coordinates, switching to a rotated chart near coordinate poles. Great-circle legs are cross-checked against exact rotations. The enclosed curvature for the readouts is integrated numerically from the metric.

| Test | State | Expect | Hidden | Note |
| --- | --- | --- | --- | --- |
| `octant-unit-radius` | preset="octant", progress=1 | turn = 90 ±1e-06; area-over-radius-squared = 1.5707963268 ±1e-08; angle-excess = 90 ±1e-06 | — | Three right angles; one eighth of the sphere. |
| `no-readouts-while-moving` | preset="octant", progress=0.5 | — | turn, area, area-over-radius-squared, angle-excess | Design rule no-running-angle. |
| `octant-any-radius` | preset="octant", radius=2.5, progress=1 | turn = 90 ±1e-06 | — | A triangle with fixed angles keeps its turn on a bigger ball. |
| `octant-reversed` | preset="octant-reversed", progress=1 | turn = -90 ±1e-06 | — | The region on the walker's left is seven eighths of the sphere: $7\pi/2 \equiv -\pi/2$, a quarter turn to the right. |
| `half-area` | preset="octant-half-area", progress=1 | turn = 45 ±1e-06 | — | Half the area gives half the turn. |
| `latitude-50` | preset="latitude-circle", progress=1 | turn = 128.5964605 ±0.0001 | — | $2\pi(1 - \cos 50^\circ)$. |
| `latitude-45` | preset="latitude-circle", colatitude=45, progress=1 | turn = 105.4415588 ±0.0001 | — | The same rotation as 254.56 degrees clockwise. |
| `latitude-150` | preset="latitude-circle", colatitude=150, progress=1 | turn = -48.2308546 ±0.0001 | — | 671.77 degrees wraps to −48.23 on the branch. |
| `latitude-branch-boundary` | preset="latitude-circle", colatitude=60, progress=1 | turn = 180 ±0.0001 | — | Exactly a half turn; implementations must report 180, never −180. |
| `flat-square` | preset="flat-square", progress=1 | turn = 0 ±1e-09 | — | A flat floor never turns the arrow. |
| `tube-bracelet` | preset="tube-bracelet", progress=1 | turn = 0 ±1e-09 | — | A tube is intrinsically flat, including loops around it. |
| `saddle-square` | preset="saddle-square", progress=1 | turn = -8.8169101 ±0.0001 | — | ∬K dA over the projected square, R = 1: −0.1538841 rad, toward the walker's right. |
| `cone-around-tip` | preset="cone-around-tip", progress=1 | turn = 60 ±1e-06 | — | The turn equals the wedge angle. |
| `cone-twice-around` | preset="cone-around-tip", windings=2, progress=1 | turn = 120 ±1e-06 | — | Two windings give twice the wedge angle. |
| `cone-wide-wedge-four-windings` | preset="cone-around-tip", wedge-angle=300, windings=4, progress=1 | turn = 120 ±1e-06 | — | 1200 degrees wraps to 120. |
| `cone-avoid-tip` | preset="cone-avoid-tip", progress=1 | turn = 0 ±1e-09 | — | Loops that do not enclose the tip return unchanged. |
| `length-conserved` | preset="latitude-circle", colatitude=30, progress=1 | arrow-length = 1 ±1e-09 | — | Transport preserves length, for an arrow of unit length. |

## Serves

- [[parallel-transport]]: the faded arrow copies and the no-swing rule
- [[path-dependence-of-parallel-transport]]: the two-routes preset
- [[holonomy]]: the returned arrow, the base-point inset, and every control case
- [[gaussian-curvature]]: the area readouts on the ball and the saddle's opposite turn
- [[angular-excess]]: the angle-excess readout for triangles
- [[intrinsic-versus-extrinsic-curvature]]: the tube and its unrolled view
- [[curvature-of-the-two-sphere]]: the radius slider and the area over radius squared readout
- [[flatness-criterion]]: the flat floor, tube, and cone cases
- [[integrability-condition-for-parallel-fields]]: the cone presets: loops that avoid the tip return the arrow unchanged, loops around the tip turn it by the wedge angle times the windings
- [[normal-curvature]]: the circle-of-latitude preset, whose turn is the area rule for a loop that is not a straight walk

## In the visual network

- **Builds on:** [[slide-an-arrow-along-a-path]]
- **Leads to:** [[four-legs-around-a-tiny-loop]]

## Accessibility

Every tour beat has a spoken description of where the arrow points relative to the path. The returned turn is announced in degrees to the left or right. Start and returned arrows differ in line style as well as colour, and every control works from the keyboard.

Static alternative: On a ball, an arrow carried around a three-sided loop from the North Pole returns a quarter turn away from its start. On a flat floor and on a tube, arrows carried around loops return unchanged.

- `Space`: play or pause the walk
- `Left and Right arrows`: scrub along the loop
- `R`: reverse the walking direction
- `1 to 5`: choose flat floor, tube, ball, saddle, or cone
- `U`: unroll the tube or cone

## Starting material

Earlier course assets: `scene-3d-parallel-transport-loop`, `scene-3d-parallel-transport-two-routes`, `figure-sphere-holonomy`, `scene-3d-sphere-holonomy`

The earlier course's transport model and its checks can be ported almost unchanged as a TypeScript module, and its two-routes lab becomes a preset of this visual. Its octant SVG becomes the static card. New work: saddle and cone surfaces, unrolled views, area readouts, and preset-driven state.
