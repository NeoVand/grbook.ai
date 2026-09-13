---
type: "visual"
schema_version: 2
id: "carry-an-arrow-around-a-loop"
title: "Carry an arrow around a loop"
kind: "interactive-3d"
priority: "flagship"
rungs: ["entry", "working"]
serves: ["parallel-transport", "path-dependence-of-parallel-transport", "holonomy", "gaussian-curvature", "angular-excess", "intrinsic-versus-extrinsic-curvature", "curvature-of-the-two-sphere", "flatness-criterion"]
builds_on: ["slide-an-arrow-along-a-path"]
leads_to: ["shrink-the-loop-to-find-riemann", "paper-cone-with-a-missing-wedge", "arrow-around-a-circle-of-latitude"]
review: null
---

# Carry an arrow around a loop

`carry-an-arrow-around-a-loop` · interactive-3d · flagship · rungs: entry, working

> Carry an arrow around a closed path without turning it: on a ball it comes back turned, and on a flat sheet it does not.

## What it makes visible

An arrow moved without ever being turned comes back turned on a curved surface, but not on a flat or merely bent one. The turn grows with the area the loop encloses and reverses when the loop is walked the other way. It is the one picture behind parallel transport, path dependence, holonomy, Gaussian curvature, and the meaning of the Riemann tensor.

## The picture

A shaded surface with a faint grid fills the scene. A closed path is drawn on it, the region it encloses is lightly tinted, and a small arrowhead on the path shows the walking direction. Faded copies of the carried arrow mark its progress. An inset at the base point shows the starting arrow and the returned arrow side by side, with an arc between them. Readouts for the turn and the enclosed area appear only when the loop closes.

| Element | Shows |
| --- | --- |
| Surface with intrinsic grid | the space the walker lives in: plane, tube, ball, saddle, or cone |
| Closed path with direction arrowhead | the loop and which way it is walked |
| Tinted enclosed region | the area whose curvature produces the turn |
| Faded arrow copies along the path | the arrow being carried without turning |
| Base-point inset with start arrow (grey, dashed) and returned arrow (accent, solid) | the holonomy as an angle between two arrows at the same point |
| Readouts: turn, area, area over radius squared, angular excess | the area law, shown only once the loop closes |

## Variants

- **static-card**: The octant loop on a ball with the base-point inset, showing a quarter turn. Serves as the fallback without WebGL and as a summary card.
- **interactive-2d**: Unrolled views of the tube and the cone, where carrying the arrow is plain sliding and the seam adds any turn.
- **interactive-3d**: The full experience on all surfaces, with presets, loop editing, reversal, radius changes, and scrubbing.

## Interaction

| Control | Effect |
| --- | --- |
| Surface: plane, tube, ball, saddle, cone | Controls first, then positive and negative curvature, then curvature concentrated at a tip. |
| Presets: octant triangle, circle of latitude, two routes to one point | Loads the canonical cases in one click. |
| Drag vertices or sketch a free loop | Area and shape change live; the turn updates when the loop is closed. |
| Reverse direction | The direction arrowhead and the sign of the turn flip together. |
| Radius slider (ball) | A triangle with fixed angles keeps its turn; a loop of fixed size in metres turns less on a bigger ball. |
| Scrub along the loop | Moves the arrow; the angle readout stays hidden until the loop closes. |
| Unroll (tube and cone) | Shows the flat sheet beside the surface. |

## Guided tour

1. *Ball with the octant loop from the North Pole down to the equator, a quarter of the way along it, and back. The arrow sits at the pole, pointing down the first path.*  
   “Here is a ball and a closed path. I will carry this arrow along the path, and I will never turn it.”
2. *The arrow reaches the equator. The path turns left, and the arrow keeps pointing south.*  
   “At the corner I turn to follow the path. The arrow does not turn. It keeps pointing the way it was pointing.”
3. *Back at the pole. The inset shows the starting arrow and the returned arrow, a right angle apart.*  
   “We are home. Compare the two arrows. The arrow has made a quarter turn, and nobody turned it.”
4. *Switch to the flat plane and walk a square.*  
   “Now a walk on a flat floor, with four corners. The arrow comes back exactly as it left.”
5. *Switch to the tube, walk a loop around it, then open the unrolled view.*  
   “A rolled-up tube looks curved, but the arrow comes back unturned. Unroll it and you see why. It is a flat sheet.”
6. *Back on the ball, shrink the loop to half the area. The readout shows half the turn.*  
   “Fence in half as much of the ball, and the turn is half as big. The turn measures how much curving is inside the loop.”

## Design rules

- **Never show a running angle while the arrow is moving.** Because: Arrows at different places on a curved surface cannot be compared independently of the route; the turn exists only when the loop closes.
- **Keep the plane and the tube one click away from the ball.** Because: Learners otherwise blame the corners, the walking rule, or mere bending for the turn.
- **Make reversal visibly symmetric: the same path, a mirrored direction arrowhead, and the opposite turn.** Because: Many learners believe the direction of travel does not matter.
- **On the cone, make loops that miss the tip the easiest thing to draw.** Because: Seeing them return unchanged, next to a loop around the tip that does not, is the whole lesson about flat regions and non-shrinkable loops.
- **Distinguish start and returned arrows by line style as well as colour.** Because: Colour alone fails for colour-blind learners and in print.

## Model

The arrow is carried by integrating the parallel transport equation in the surface's own coordinates. The 3D arrow is drawn by mapping its components through the surface embedding, so the embedding never affects the physics.

$$
\frac{dV^a}{ds} + \Gamma^a{}_{bc}\,\frac{dx^b}{ds}\,V^c = 0
$$

$$
\Delta\alpha = \iint_S K\,dA \pmod{2\pi}
$$

$$
\text{sphere of radius } a:\quad \Delta\alpha = A/a^2
$$

$$
\text{cone with deficit angle } \delta:\quad \Delta\alpha = \delta \text{ for loops around the tip, } 0 \text{ otherwise}
$$

**Method:** Fourth-order Runge–Kutta in surface coordinates, switching to a rotated chart near coordinate poles. Great-circle legs are cross-checked against exact rotations. Gaussian curvature comes from the metric, and the enclosed curvature is integrated numerically for the readout. Tube and cone use their unrolled flat charts, where transport is translation and the seam identification adds any rotation.

| Test case | Expected |
| --- | --- |
| Octant triangle on a ball of any radius | Turn of π/2 (90°), in the same sense as the circulation |
| Circle of latitude at colatitude 60° | Turn of π (180°); generally 2π(1 − cos θ₀) modulo 2π |
| Any loop on the plane, and any loop on the tube including one around it | Turn of 0 |
| Cone with a 60° wedge removed, loop around the tip | Turn of 60°; a loop not enclosing the tip gives 0 |
| Same loop walked in reverse | Exactly the negative turn |
| Arrow length along any loop | Conserved to 1e-9 relative error |
| Small loop on the saddle | Matches the numerically integrated curvature to 1e-4 rad, with the opposite sense to the circulation |

## Serves

- [[parallel-transport]]: the faded arrow copies and the no-turn rule
- [[path-dependence-of-parallel-transport]]: the two-routes preset
- [[holonomy]]: the returned arrow and the base-point inset
- [[gaussian-curvature]]: the area readout on the ball and the saddle's opposite turn
- [[angular-excess]]: the angle-sum readout for triangles
- [[intrinsic-versus-extrinsic-curvature]]: the tube and its unrolled view
- [[curvature-of-the-two-sphere]]: the radius slider and the area over radius squared readout
- [[flatness-criterion]]: the plane, tube, and cone controls

## In the visual network

- **Builds on:** [[slide-an-arrow-along-a-path]]
- **Leads to:** [[shrink-the-loop-to-find-riemann]], [[paper-cone-with-a-missing-wedge]], [[arrow-around-a-circle-of-latitude]]

## Accessibility

Each tour beat has a spoken description of where the arrow points relative to the path: ahead, left, right, or behind. The returned turn is announced in degrees. Every control works from the keyboard, and the static card is the fallback when 3D is unavailable.

## Starting material

Earlier course assets: `scene-3d-parallel-transport-loop`, `scene-3d-parallel-transport-two-routes`, `figure-sphere-holonomy`, `scene-3d-sphere-holonomy`

The earlier course's transport model and its checks can be ported almost unchanged as a TypeScript module, and the two-routes lab becomes a preset of this one. The octant SVG becomes the static card. New work: saddle and cone surfaces, the unrolled views, and the area readouts.
