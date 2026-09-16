---
type: "visual"
schema_version: 2
id: "cube-of-small-loops"
title: "Cube of small loops"
kind: "interactive-3d"
priority: "flagship"
status: "proposed"
revision: 2
rungs: ["entry", "working", "formal", "research"]
serves: ["bianchi-identity", "cyclic-identity", "holonomy", "weyl-tensor-field-equation"]
builds_on: ["carry-an-arrow-around-a-loop", "four-legs-around-a-tiny-loop"]
leads_to: ["falling-ring-of-crumbs", "twenty-of-256-slots"]
---

# Cube of small loops

`cube-of-small-loops` · interactive-3d · flagship · proposed · rungs: entry, working, formal, research

> Carry an arrow around each face of a tiny box without letting it swing, and the changes cancel in two different ways.

## What it makes visible

One tiny box carries both curvature identities. Walk its three corner faces, each carrying the edge its own face lacks, and the three changes add to nothing: the cyclic identity. Walk all six faces the same way round seen from outside, pair them off, and the three leftovers add to nothing: the Bianchi identity. Each single face is a small loop, so the whole picture rests on holonomy. Splitting every face change into its Ricci part and its Weyl part turns the same box into the Weyl divergence equation, whose source is the change in the matter, not the matter itself.

## The picture

A small translucent box floats in a shaded field of curvature. Its twelve edges are solid lines; the face being walked is tinted and carries small arrowheads showing the walking direction. The carried arrow is drawn in orange at the home corner, with a faded copy at each step. Beside the box, the returned changes are laid tip to tail as short bars on a stub axis, one colour per face or per opposite pair and each bar labelled with its number, with the running total at the end. A split toggle draws every bar as a pale room-changing stub plus a solid shape-changing stub. Readouts appear only when a face trip closes.

| Element | Shows |
| --- | --- |
| Translucent box with twelve solid edges | the tiny region of space and time whose faces are the loops |
| Tinted face with arrowheads | the loop being walked and the direction it is walked in |
| Orange carried arrow with faded copies | the arrow carried without swinging |
| Short bars laid tip to tail on a stub axis | the changes each trip brings back, and their running total |
| Pale and solid halves of each bar | the room-changing part and the shape-changing part of one face change |
| Readouts: face change, corner sum, leftover, leftover sum, shrink slope | the two identities as numbers, shown only once a trip closes |

## Book figure

Two panels sharing one small box. Left: the three faces meeting at the home corner, each with the arrow that points along the edge that face lacks, and the three returned changes laid tip to tail closing on the starting point. Right: all six faces, paired into three opposite pairs by colour, with the three leftover bars laid tip to tail and closing on the starting point.

Labels: home corner, first edge, second edge, third edge, three corner trips, three leftovers, total: nothing. Aspect 2:1. Alt text: A tiny box in curved space. Three trips around the faces at one corner give three changes that close into a triangle, and the three leftovers from opposite faces close into a triangle as well.

## Variants

- **static** `static-card` (fallback): The print figure as an SVG card: the corner triple and the six-face pairing side by side, used when 3D cannot run.
- **interactive-2d** `flattened-net`: The box opened out as a flat net, with each face's trip and returned change drawn on its own tile and the shared edges marked, so the cancellation of edges can be followed by eye.
- **interactive-3d** `full-3d`: The whole demonstration: a choice of space and time, a choice of three axes for the box, both carry rules, the edge-length slider, the split toggle, and every readout.

## Parameters

| Id | Label | Type | Options or range | Default | Available when | Effect |
| --- | --- | --- | --- | --- | --- | --- |
| `spacetime` | Space and time | enum | minkowski, de-sitter, plane-wave, point-mass, star-inside | "plane-wave" | — | Chooses the geometry the box sits in. Flat gives zero everywhere; same-curving-everywhere has $\nabla R = 0$, so every leftover is zero on its own; the ripple is a linearized plane wave running along $z$, the only choice with components carrying four different directions; outside a round star is Ricci-flat with curvature changing in every direction; inside a round star adds a Ricci part and a nonzero Weyl current. |
| `cube-axes` | Box edges run along | enum | xyz, txy, txz, tyz | "xyz" | — | Picks the three of the four spacetime directions the box's edges run along, in the order listed. Writing them $(a, b, c)$, the three faces that touch the home corner are $(b, c)$, then $(c, a)$, then $(a, b)$, and opposite pair number one is the pair stacked along $a$, pair two along $b$, pair three along $c$. |
| `faces` | Faces walked | enum | home-three, all-six | "all-six" | — | Three corner faces show the cyclic identity; all six, paired off, show the Bianchi identity. |
| `carry-rule` | Which arrow is carried | enum | fixed, missing-edge (faces in home-three) | "fixed" | — | The fixed rule carries one chosen arrow around every face. The missing-edge rule carries, on each corner face, the arrow pointing along the box edge that face does not use; that is the rule the cyclic identity needs, so it is offered only with the three corner faces. |
| `carried-axis` | Carried arrow points along | enum | t, x, y, z | "t" | carry-rule in fixed | Sets the unit frame vector carried around every face when the fixed carry rule is chosen. |
| `read-axis` | Reading direction | enum | t, x, y, z | "t" | — | The frame direction whose component of each returned change the readouts report. Choosing a direction the box's edges do not run along is what makes the cyclic sum a new condition. |
| `highlight` | Highlighted face or pair | integer | 1–3 step 1 | 1 | — | Picks which of the three corner faces, or which of the three opposite pairs, the face and leftover readouts report. |
| `edge` | Box edge | number | 0.005–0.5 step 0.005 scene units | 0.1 | — | The coordinate length of every edge of the box. Drawn changes scale with it; the per-unit-area and per-unit-volume readouts are extrapolated to zero edge and do not. |
| `progress` | Walk progress | progress | 0–1 step 0.01 | 0 | — | Moves the arrow through the chosen face trips in order; readouts marked on-complete appear only at 1. |
| `split` | Split each change | boolean | — | false | — | Draws every returned change as a room-changing part built from the Ricci tensor and the metric, plus a shape-changing part built from the Weyl tensor. |
| `curvature-radius` | Curvature radius | number | 0.5–20 step 0.5 scene units | 2 | spacetime in de-sitter | The length $L$ of the same-curving-everywhere choice, whose Riemann tensor is $L^{-2}(g_{\mu\rho}g_{\nu\sigma} - g_{\mu\sigma}g_{\nu\rho})$. |
| `plus-amplitude` | Stretch amplitude | number | 0–0.2 step 0.01 | 0.1 | spacetime in plane-wave | The amplitude of the plus polarization of the ripple, which stretches along $x$ while squeezing along $y$. |
| `cross-amplitude` | Diagonal amplitude | number | 0–0.2 step 0.01 | 0.1 | spacetime in plane-wave | The amplitude of the cross polarization of the ripple. It alone gives the components whose four directions all differ, so setting it to zero empties the cyclic sum. |
| `wave-phase` | Ripple phase at the box | number | 0–345 step 15 deg | 45 | spacetime in plane-wave | The phase $\omega(t - z)$ of the ripple at the home corner, with $\omega = 1$ per scene unit. At zero phase the curvature vanishes while its rate of change does not. |
| `mass` | Star mass | number | 0.1–2 step 0.1 scene units | 1 | spacetime in point-mass, star-inside | The star's mass in geometrized units, where a mass is a length. |
| `mass-distance` | Distance from the star's centre | number | 1–50 step 1 scene units | 10 | spacetime in point-mass, star-inside | How far the home corner sits from the centre. The centre lies in the fixed direction with components two sevenths, three sevenths and six sevenths from the home corner, chosen off every box axis so that no component is zero by symmetry alone. |
| `star-radius` | Star radius | number | 2–20 step 1 scene units | 3 | spacetime in star-inside | The radius $R$ of a star whose density falls straight to zero at the surface, $\rho(r) = (3M/\pi R^3)(1 - r/R)$. |

## Presets

- `flat-cube` A box in flat space and time: spacetime="minkowski", cube-axes="xyz", faces="all-six", carry-rule="fixed", carried-axis="t", read-axis="t", highlight=1, edge=0.1
- `de-sitter-face` One face where the curving is the same everywhere: spacetime="de-sitter", curvature-radius=2, cube-axes="xyz", faces="home-three", carry-rule="fixed", carried-axis="x", read-axis="y", highlight=3, edge=0.1
- `de-sitter-corner` Three corner trips where the curving is the same everywhere: spacetime="de-sitter", curvature-radius=2, cube-axes="xyz", faces="home-three", carry-rule="missing-edge", read-axis="t", highlight=1, edge=0.1
- `de-sitter-cube` All six faces where the curving is the same everywhere: spacetime="de-sitter", curvature-radius=2, cube-axes="xyz", faces="all-six", carry-rule="fixed", carried-axis="x", read-axis="y", highlight=1, edge=0.1
- `wave-corner` Three corner trips in a passing ripple: spacetime="plane-wave", plus-amplitude=0.1, cross-amplitude=0.1, wave-phase=45, cube-axes="xyz", faces="home-three", carry-rule="missing-edge", read-axis="t", highlight=1, edge=0.05
- `wave-cube` All six faces in a passing ripple: spacetime="plane-wave", plus-amplitude=0.1, cross-amplitude=0.1, wave-phase=45, cube-axes="txz", faces="all-six", carry-rule="fixed", carried-axis="y", read-axis="t", highlight=1, edge=0.05
- `wave-at-zero-phase` A ripple caught where its curving passes through zero at the box: spacetime="plane-wave", plus-amplitude=0.1, cross-amplitude=0.1, wave-phase=0, cube-axes="txz", faces="all-six", carry-rule="fixed", carried-axis="y", read-axis="t", highlight=1, edge=0.05
- `point-mass-cube` All six faces outside a round star: spacetime="point-mass", mass=1, mass-distance=10, cube-axes="xyz", faces="all-six", carry-rule="fixed", carried-axis="x", read-axis="y", highlight=1, edge=0.1
- `star-cube` All six faces inside a round star: spacetime="star-inside", mass=1, star-radius=3, mass-distance=1, cube-axes="xyz", faces="all-six", carry-rule="fixed", carried-axis="x", read-axis="y", highlight=1, edge=0.1, split=true

## Readouts

- `face-turn` Turn on the highlighted face (deg; visible on-demand; 6 decimals; range (-180, 180]; sense: positive when the arrow turns from the face's first edge toward its second edge, which is toward the walker's left with the walker's head along the first edge crossed into the second): “the arrow came back turned {abs} degrees from the first edge toward the second” / “the arrow came back turned {abs} degrees from the second edge toward the first”
- `face-coefficient` Change per unit area on the highlighted face (per scene unit squared; visible on-complete; 8 decimals; sense: positive when the arrow's tip moves along the reading direction): “the change per unit area is {abs} along the reading direction” / “the change per unit area is {abs} against the reading direction”
- `corner-sum` Sum over the three corner faces (per scene unit squared; visible on-complete; 12 decimals; sense: positive when the total moves along the reading direction): “measured along the reading direction, the three corner trips add to {abs}” / “measured along the reading direction, the three corner trips add to minus {abs}”
- `leftover` Leftover of the highlighted opposite pair (per scene unit cubed; visible on-complete; 8 decimals; sense: positive when what is left over moves along the reading direction): “this pair leaves over {abs} per unit volume along the reading direction” / “this pair leaves over {abs} per unit volume against the reading direction”
- `leftover-sum` Sum of the three leftovers (per scene unit cubed; visible on-complete; 12 decimals; sense: positive when the total moves along the reading direction): “measured along the reading direction, the three leftovers add to {abs}” / “measured along the reading direction, the three leftovers add to minus {abs}”
- `shrink-slope` Shrink slope (no unit; visible on-demand; 3 decimals; range (0, 6]): “the highlighted change falls off as the box edge to the power {value}”
- `ricci-part` Room-changing part of the face change (per scene unit squared; visible on-demand; 8 decimals; sense: positive when this part moves the arrow's tip along the reading direction): “the room-changing part is {abs} along the reading direction” / “the room-changing part is {abs} against the reading direction”
- `weyl-part` Shape-changing part of the face change (per scene unit squared; visible on-demand; 8 decimals; sense: positive when this part moves the arrow's tip along the reading direction): “the shape-changing part is {abs} along the reading direction” / “the shape-changing part is {abs} against the reading direction”
- `weyl-divergence` Divergence of the Weyl tensor (per scene unit cubed; visible on-demand; 8 decimals; sense: positive when the component taken with the reading direction and the highlighted face's two edges, in the order the face is walked, is positive): “the divergence of the shape-changing table reads {abs}” / “the divergence of the shape-changing table reads minus {abs}”
- `weyl-current` Weyl current (per scene unit cubed; visible on-demand; 8 decimals; sense: positive when the component taken with the reading direction and the highlighted face's two edges, in the order the face is walked, is positive): “the current built from the change in the matter reads {abs}” / “the current built from the change in the matter reads minus {abs}”

## Tours

### `six-loops-around-a-box` · for [[bianchi-identity]] · entry

1. `meet-the-box` (entry, await none) state: preset="point-mass-cube", progress=0  
   *A tiny box floating in the space around a star, with one orange arrow resting at the home corner.*  
   Say: “Here is a tiny box floating in the space around a star. Its twelve edges are drawn as solid lines. One corner is marked, and I call it the home corner. An orange arrow rests there. I will carry that arrow around each face in turn, and I will never let it swing.”  
   Describe: A small box hangs in the curved space near a star. One corner is marked as home, and a single arrow rests at that corner.
2. `predict-the-total` (entry, await prediction) state: preset="point-mass-cube", progress=0; evidences `bianchi-identity/checks/the-sixth-trip`  
   *The same view, paused, with the six faces briefly tinted one after another.*  
   Predict: “I walk each of the six faces the same way round, seen from outside the box. What do the six changes add up to?”  
   Say: “Guess before I walk. I go around every one of the six faces, each the same way round, seen from outside the box. Each trip brings the arrow back a little changed. What do the six changes add up to?”  
   Describe: The box waits with the arrow at the home corner. Each of the six faces lights up in turn, so you can count them.
3. `walk-the-six` (entry, await none) state: preset="point-mass-cube", progress=0; animate progress → 1 over 14 s  
   *The arrow travels around all six faces in order; a short bar is laid tip to tail for each returned change.*  
   Say: “Watch the arrow go round, face after face. A short bar appears for each trip, laid tip to tail beside the box. Every edge of the box belongs to two faces. I walk each edge once one way and once the other way. So every step one way is undone by the same step the other way, and the six bars close back on the starting point, where the first bar began. They add up to nothing.”  
   Describe: The arrow travels around six faces in turn. Six short bars are laid end to end beside the box, and the last one ends where the first one began.
4. `pair-the-opposite-faces` (entry, await none) state: preset="point-mass-cube", progress=1, highlight=1  
   *Only the highlighted opposite pair is tinted; its two bars are drawn nose to nose with the small leftover between them.*  
   Say: “Now take just one pair of faces that sit opposite each other. Seen from one and the same side of the box, they are walked opposite ways round. So their two bars nearly cancel. What is left between them is small, and the leftover readout gives it. This pair leaves over about one and a half ten-thousandths per unit of volume.”  
   Describe: Two opposite faces of the box are tinted. Their bars point almost exactly against each other, and a short gap remains between the tips.
5. `three-leftovers` (entry, await none) state: preset="point-mass-cube", progress=1; evidences `bianchi-identity/checks/leftover-of-the-third-pair`  
   *All three pairs tinted in three colours and labelled one, two and three; the three leftover bars laid tip to tail in the same order, closing on the starting point.*  
   Say: “A box has three pairs of opposite faces, so there are three leftovers. Two of them point one way and the third points back the other way. Laid tip to tail, the three close on the starting point. They add up to nothing. That is the rule, and it is called the Bianchi identity.”  
   Describe: Three leftover bars, in three colours and labelled one, two and three, are laid end to end. Two point one way and the third points back, and the last tip lands on the first tail.
6. `try-to-break-it` (entry, await none) state: preset="wave-cube", progress=1; evidences `bianchi-identity/checks/an-experiment-to-break-it`  
   *The same six-face walk in a passing ripple; the three leftovers again close on the starting point.*  
   Say: “Try another choice from the space and time list. Here a ripple of curving is passing through the box. The three leftovers are different numbers now, and they still close on the starting point. No space in the list breaks the rule. The reason is that every edge of the box belongs to two faces, and the two trips walk it opposite ways. That is true of any box in any space, so no experiment could ever catch the rule failing.”  
   Describe: The box now sits in a passing ripple. The three leftover bars have different lengths from before, and they still close on the starting point.
7. `shrink-the-box` (working, await none) state: preset="point-mass-cube", progress=1, highlight=1; animate edge → 0.01 over 5 s  
   *The box shrinks while the shrink-slope readout settles; the drawn bars shorten sharply while the per-unit readouts hold still.*  
   Say: “Now I shrink the box. One face's change falls off as the square of the edge, so the shrink slope reads two. A pair's leftover falls off as the cube, so its slope reads three. Divide each one by the area or by the volume it belongs to, and the readouts hold still: those are the numbers the identity is really about.”  
   Describe: The box shrinks steadily. The drawn bars shorten much faster than the box does, while the per-unit readouts stay at the same values.

### `leftovers-in-components` · for [[bianchi-identity]] · working

1. `name-the-three-leftovers` (working, await none) state: preset="point-mass-cube", progress=1  
   *Each leftover bar labelled with the derivative index and the two face-edge indices it carries.*  
   Say: “Each opposite pair sits across one box axis. Pair one is stacked along x and its faces have edges along y and z. Its leftover per unit volume is minus the covariant derivative along x of the Riemann component whose slots are the reading direction, the carried direction, and then y and z. The other two pairs give the same expression with x, y and z moved one place around a ring.”  
   Describe: Three leftover bars, one for each box axis. Each is labelled by the direction the pair is stacked along and by the two directions its faces span.
2. `does-it-forbid-change` (working, await prediction) state: preset="point-mass-cube", progress=1, highlight=2; animate mass-distance → 20 over 4 s; evidences `ricci-bianchi-and-einstein-tensors/checks/an-egg-and-the-bianchi-identity`  
   *The box drifts outward; every leftover shrinks in size while their sum stays pinned at zero.*  
   Predict: “I move the box twice as far from the star, so the curvature there is eight times weaker. Does the identity stop the curvature from changing from place to place?”  
   Say: “I move the box twice as far from the star. The curvature there is eight times weaker, so every leftover shrinks. Predict first: does the identity forbid the curvature from changing from place to place? The identity ties the three rates of change to each other. It never forbids curvature from changing from place to place.”  
   Describe: The box drifts outward from the star. All three leftover bars shrink together, and the readout for their sum stays at zero.
3. `constant-curvature-kills-each-one` (working, await none) state: preset="de-sitter-cube", progress=1  
   *Same-curving-everywhere: each face change is large, every leftover bar has zero length.*  
   Say: “Switch to the space whose curving is the same everywhere. Each single face still changes the arrow, and the face readout is a quarter per unit area. Every leftover is zero on its own, not just the sum, because the covariant derivative of the Riemann tensor vanishes. A zero sum does not mean uniform curving; uniform curving means three separate zeros.”  
   Describe: In the space with the same curving everywhere, each face still changes the arrow, and all three leftover bars have no length at all.
4. `curvature-zero-leftovers-not` (formal, await none) state: preset="wave-at-zero-phase", progress=1  
   *The ripple caught at zero phase: every face bar has zero length while two leftover bars do not.*  
   Say: “Here is the opposite case. I catch the ripple at the phase where its curvature passes through zero at the home corner. Every face change is zero, so no single loop turns the arrow at all. Two of the three leftovers are one twentieth per unit volume, one along the reading direction and one against it, and the third is zero. The identity constrains the derivative of the curvature, not the curvature.”  
   Describe: The ripple is caught at the moment its curvature vanishes at the box. No face changes the arrow, yet two of the three leftovers are still there and cancel each other.
5. `which-identity-is-this` (formal, await none) state: preset="wave-corner", progress=1; evidences `bianchi-identity/checks/which-identity-at-one-point`  
   *The control switches to the three corner faces and the missing-edge carry rule; the readouts change from leftovers to face changes.*  
   Say: “One more thing to keep straight. The switch to the three corner faces, with each face carrying the edge it lacks, gives a different rule. That one holds at a single event and needs no derivative at all. The six-face rule needs the curvature at two nearby places, one per face of each pair. They are two separate identities that share one box.”  
   Describe: The demonstration switches to three faces at one corner. The readouts now report face changes at one event, not leftovers across the box.

### `three-trips-at-a-cube-corner` · for [[cyclic-identity]] · entry

1. `three-faces-meet-here` (entry, await none) state: preset="wave-corner", progress=0  
   *Only the three faces touching the home corner are drawn; the three edges leaving that corner are thickened.*  
   Say: “Look at one corner of this tiny box, and I call it the home corner. Three edges leave it, and I have made them thick. Three faces meet there, and each face is made by two of those edges. So every face leaves one of the three edges out.”  
   Describe: At one corner of the box, three thick edges leave in three directions. Three faces meet there, and each uses two of the three edges.
2. `the-missing-edge-rule` (entry, await none) state: preset="wave-corner", progress=0  
   *For each of the three faces in turn, an arrow appears pointing along the edge that face leaves out.*  
   Say: “Here is the rule for which arrow to carry. On each face I point the arrow along the edge that face leaves out. So from trip to trip, the arrow and the two edges each step on to the next of the three directions, and after three trips they are back where they started. Nothing else changes.”  
   Describe: Each of the three faces is shown with its own arrow. The arrow always points along the one edge that face does not use.
3. `predict-the-third-trip` (entry, await prediction) state: preset="wave-corner", progress=0.67; evidences `cyclic-identity/checks/third-trip-at-a-cube-corner`  
   *Two bars drawn nose to nose, the third face tinted and waiting.*  
   Predict: “The first two trips are done, and their changes are the same size and point opposite ways. What will the third trip bring back?”  
   Say: “Two trips are done. Their two bars are the same length and point opposite ways, so laid tip to tail they already close. The third face is tinted and waiting. Guess what the third trip will bring back.”  
   Describe: Two bars of the same length point opposite ways and already close on each other. The third face is tinted and has not been walked.
4. `lay-them-tip-to-tail` (entry, await none) state: preset="wave-corner", progress=0.67; animate progress → 1 over 4 s  
   *The third trip runs and brings back nothing; the three bars close on the starting point and the corner-sum readout stays at zero.*  
   Say: “The third trip leaves the arrow exactly as it set off, so its bar has no length. All three bars laid tip to tail close on the starting point. In every space that general relativity uses, those three changes add up to nothing. Curvature is a table of numbers with rules it must obey, and this is the fourth of them.”  
   Describe: The third trip leaves the arrow as it was. The three bars laid end to end finish exactly where they started, and the sum readout stays at zero.
5. `why-they-cancel` (entry, await none) state: preset="wave-corner", progress=1; evidences `cyclic-identity/checks/a-space-with-twist`  
   *A ghost overlay of two short two-step routes from the corner, meeting at the far end with no gap.*  
   Say: “The reason is that tiny four-sided walks close up. Go a short way along one edge and then along a second, or take the same two steps in the other order. In every space general relativity uses, both routes end at the same spot. In some other spaces the two routes miss, by a gap that grows in step with the area of the little walk. Such a space is said to have twist, and there these three changes need not cancel.”  
   Describe: Two short two-step routes leave the corner in opposite orders. Both end at the same spot, with no gap between them.
6. `nothing-new-in-space` (entry, await none) state: preset="wave-corner", progress=1, read-axis="z"; evidences `cyclic-identity/checks/fourth-rule-in-space`  
   *The reading direction switches to a direction the box's edges already run along; a badge reads only three different directions.*  
   Say: “Each change is measured along one chosen direction, and so far that direction has been time. Now I measure along one of the box's own edge directions instead. A badge lights up to say that only three different directions are in play. The three numbers still add up to nothing, and the earlier rules of the table already forced that. So in ordinary space the fourth rule adds nothing new.”  
   Describe: The reading direction is switched to one of the box's own edge directions. The three numbers still add to nothing, and a badge says only three directions are in play.

### `the-one-new-link` · for [[cyclic-identity]] · working

1. `read-along-a-box-axis` (working, await none) state: preset="wave-corner", progress=1, read-axis="z"  
   *Reading direction z, cube axes x, y, z; the three corner numbers printed with their index strings.*  
   Say: “Take the box edges along x, y and z, and read the changes along z. The three numbers are the Riemann components with first index z and last three x, y, z moved one place around a ring. The third has a repeated first pair, so antisymmetry makes it zero. The other two are forced to be opposite by pair exchange and last-pair antisymmetry. The sum was already fixed at zero.”  
   Describe: With the reading direction along one of the box's own edges, one of the three numbers is zero and the other two are exact opposites.
2. `read-along-the-fourth` (working, await prediction) state: preset="wave-corner", progress=1; evidences `cyclic-identity/checks/three-entries-and-a-wrong-sum`  
   *Reading direction time; a badge reads four different directions; the three components printed as the components with time, x, y and z.*  
   Predict: “I switch the reading direction to time, which the box's edges do not run along. Do the earlier rules of the table still force these three numbers to add to nothing?”  
   Say: “Now I read along time, which the box's edges do not run along. All four directions differ, and the badge says so. These three numbers are the components with time first and then x, y, z moved one place around a ring. Nothing earlier in the table relates them. Their sum is the one genuinely new condition, and in spacetime there is exactly one such set of four directions.”  
   Describe: The reading direction is switched to time. A badge says all four directions differ, and the three numbers are now unrelated by the earlier rules.
3. `two-numbers-fix-the-third` (working, await none) state: preset="wave-corner", progress=1, highlight=3; evidences `symmetries-and-identities/checks/count-in-five-dimensions`  
   *The third corner bar highlighted with its value, and the other two shown as the numbers that fix it.*  
   Say: “Look at the third bar. The first two corner trips give plus and minus thirty-five thousandths per unit area, so the identity forces the third to be zero, and the readout agrees. In this ripple it is zero because the curvature is of the pure radiative kind, but it is the identity that ties any two of the three to the third. That one link is what cuts twenty-one numbers to twenty.”  
   Describe: The third bar is highlighted and has no length. The other two have equal and opposite lengths, which is what forces the third to be zero.
4. `switch-off-the-diagonal` (working, await none) state: preset="wave-corner", progress=1, cross-amplitude=0  
   *The ripple with only the stretch polarization: all three corner bars vanish while the face turns stay.*  
   Say: “Turn the diagonal polarization of the ripple down to zero. All three corner numbers drop to zero, because only the diagonal polarization gives components whose four directions all differ. Each face still turns the arrow, so the face turn readout is unchanged. An empty identity and an uncurved space are not the same thing.”  
   Describe: With only the stretching polarization left, all three corner numbers are zero, while each single face still turns the arrow as before.

### `one-face-is-one-small-loop` · for [[holonomy]] · working

1. `one-face-one-loop` (working, await none) state: preset="de-sitter-face", progress=0; animate progress → 1 over 5 s  
   *A single face of the box walked as a four-legged loop; the returned arrow drawn solid orange against the grey dashed start arrow.*  
   Say: “Before the box, take one face on its own. It is a four-legged loop, walked out along the first edge, along the second, back along the first, back along the second. I carry the arrow around it without letting it swing. Back at the home corner, the grey dashed arrow is the start and the solid orange arrow is the return. Here the turn is fourteen hundredths of a degree, from the first edge toward the second.”  
   Describe: One face of the box is walked as a small four-legged loop. At the corner, a dashed arrow shows the start and a solid arrow shows the return, a small angle apart.
2. `no-running-angle` (working, await none) state: preset="de-sitter-face", progress=0.5; evidences `holonomy/checks/halfway-readout`  
   *The walk paused halfway; every change readout is blank.*  
   Say: “Pause halfway. Every change readout goes blank, and that is deliberate. Halfway round, the carried arrow and the arrow at the home corner sit at different places, and on a curved manifold there is no route-free way to compare them. A turn exists only once the loop closes.”  
   Describe: The walk is paused halfway round the face. All the change readouts are blank until the loop closes.
3. `area-and-tilt` (working, await prediction) state: preset="de-sitter-face", progress=1, curvature-radius=1; evidences `holonomy/problems/small-loop-cell-other-vector`  
   *Curvature radius halved; the face coefficient jumps from a quarter to one and the turn from fourteen to fifty-seven hundredths of a degree.*  
   Predict: “I halve the curvature radius, which quadruples the curvature. What happens to the change per unit area and to the turn on the face?”  
   Say: “I halve the curvature radius, so the curvature is four times larger. The change per unit area goes from a quarter to one, and the turn goes from fourteen hundredths to fifty-seven hundredths of a degree. The change is minus the Riemann component with the carried direction and the face's two edges, times the area, and the small-loop law is exactly that.”  
   Describe: The curvature radius is halved. Both the change per unit area and the turn on the face grow four times larger.
4. `two-tilts-in-a-ripple` (working, await none) state: preset="wave-corner", progress=1, highlight=2  
   *Two faces of the ripple box side by side, their turns equal in size and opposite in sign.*  
   Say: “A single number per loop is not enough once loops can be tilted many ways. In this ripple, the face spanned by y then z turns the arrow five thousandths of a degree from the second edge toward the first, and the face spanned by z then x turns it the same amount the other way. Same box, same event, opposite turns: that is why curvature needs a table and not a number.”  
   Describe: Two faces of the same box turn the arrow by the same amount in opposite senses, at the same event.
5. `a-flat-box` (working, await none) state: preset="flat-cube", progress=1  
   *The flat case: every bar has zero length and every change readout reads zero.*  
   Say: “Switch to flat space and time with nothing in it. Every face returns the arrow exactly as it set off, every bar has no length, and every change readout reads zero. That is the control the rest of the picture is measured against.”  
   Describe: In flat space and time, every face returns the arrow unchanged and every change readout is zero.

### `what-empty-space-passes-on` · for [[weyl-tensor-field-equation]] · working

1. `split-inside-the-star` (working, await none) state: preset="star-cube", progress=1, highlight=3  
   *Inside the star with the split on: the highlighted face bar drawn as a long pale room-changing stub plus a short solid shape-changing stub.*  
   Say: “The box now sits one third of the way out inside a round star. The split is on, so each face bar is drawn in two pieces. On the highlighted face, the pale room-changing piece is about two tenths per unit area and the solid shape-changing piece is about fifteen thousandths. The pale piece is built from the Ricci tensor and the metric, and the matter right at the box sets it.”  
   Describe: Inside the star, the highlighted face change splits into a long pale piece set by the matter at the box and a much shorter solid piece.
2. `step-outside` (working, await prediction) state: preset="point-mass-cube", progress=1, highlight=3, split=true; evidences `weyl-tensor-field-equation/checks/which-equation-propagates`  
   *Outside the star: every pale room-changing stub has zero length while the solid shape-changing stubs remain.*  
   Predict: “I move the box outside the star, where no matter sits. Which of the two pieces of each face change survives?”  
   Say: “Now I move the box outside the star, where no matter sits. Predict first. Every pale room-changing piece drops to zero, because the Ricci tensor vanishes in vacuum. The solid shape-changing pieces stay: twelve ten-thousandths per unit area on this face. Shape change survives where matter does not.”  
   Describe: Outside the star, the pale pieces of every bar vanish and only the solid shape-changing pieces are left.
3. `the-current-is-the-change` (working, await none) state: preset="star-cube", progress=1, highlight=1  
   *Two readouts side by side: the divergence of the Weyl tensor and the current built from derivatives of the stress-energy tensor, both reading the same number.*  
   Say: “Two readouts now appear side by side. One is the divergence of the shape-changing table for this face. The other is the current built from how the matter changes from place to place. Inside the star both read four hundred and twenty-three ten-thousandths. Outside the star both read zero, although the shape-changing table itself is not zero there. The source is the change in the matter, not the matter.”  
   Describe: Two readouts agree exactly: the divergence of the shape-changing table and the current built from the way the matter changes.
4. `both-signs` (working, await none) state: preset="star-cube", progress=1, highlight=3  
   *The third pair highlighted; both readouts now negative and still equal.*  
   Say: “Highlight the third pair instead. Both readouts turn negative together, at minus one hundred and forty-one ten-thousandths, and they still match each other exactly. The equation is a component equation, so its sign follows the reading direction and the order the face is walked in, not the strength of the matter.”  
   Describe: With the third pair highlighted, both readouts are negative and still equal to each other.
5. `the-identity-behind-it` (formal, await none) state: preset="star-cube", progress=1, highlight=1; evidences `weyl-tensor-field-equation/checks/current-is-conserved`  
   *The six-face leftovers redrawn beside the two readouts, with the once-contracted form written out.*  
   Say: “Where does the equation come from? It is the six-face rule with one index contracted and the Weyl and Ricci parts separated. Contracting the box rule once gives the divergence of the Riemann tensor in terms of derivatives of the Ricci tensor. Inserting the split cancels every pure-trace term, and what is left is the divergence of the Weyl tensor equal to the Cotton tensor. A cosmological constant drops out, because the covariant derivative of the metric vanishes.”  
   Describe: The three leftover bars are drawn beside the two readouts, to show that the equation is the same box rule with one index contracted.
6. `the-radiative-case` (research, await none) state: preset="wave-cube", progress=1  
   *The ripple box: Ricci and current readouts at zero, the leftovers nonzero and cancelling.*  
   Say: “Last, the case with no matter anywhere. In the passing ripple the Ricci part is zero everywhere, so the current is zero and the divergence of the Weyl tensor is zero. The leftovers are still there and still cancel. That vacuum equation is what makes shape-changing curvature propagate, and linearized it is the wave equation whose solutions these ripples are. Split by an observer it becomes a Maxwell-like pair for the electric and magnetic parts of the Weyl tensor.”  
   Describe: In the passing ripple, the matter readouts all sit at zero while the leftovers remain and cancel each other.

## Design rules

- **Show no sum, leftover, or face change while a trip is in progress; the readouts appear only when a face trip closes.** Because: Two arrows at different places on a curved manifold cannot be compared without naming a route, so a running angle is not a number the picture has. Prevents `holonomy/misconceptions/running-angle-halfway`.
- **Always draw the three leftover bars individually beside their total; never show the total alone.** Because: A zero total invites the reading that nothing varies across the box, when in fact each leftover is usually nonzero and only their sum cancels. Prevents `bianchi-identity/misconceptions/zero-total-means-uniform-curving`.
- **Keep the three-corner-faces setting with the missing-edge carry rule on one control and the six-face setting on another, and label each with the identity it shows.** Because: The cyclic identity holds at one event with no derivative; the Bianchi identity compares two nearby events. Sharing a box makes them easy to merge. Prevents `bianchi-identity/misconceptions/same-as-cyclic-identity`.
- **Label every readout as a component in the stated orthonormal frame, and never offer a coordinate chart in which the readouts are claimed to be special.** Because: The short proof runs in coordinates where the connection vanishes at a point, which invites the belief that the identity itself needs such coordinates. Prevents `bianchi-identity/misconceptions/only-in-special-coordinates`.
- **Keep the sum readouts pinned at zero for every space, every box orientation, every carried arrow and every edge length, with no parameter anywhere that can make them nonzero.** Because: A control that could break the sum would teach that the identity is a law of nature an experiment might catch failing. Prevents `bianchi-identity/misconceptions/identity-is-a-law-of-nature`.
- **Draw the three corner trips in one colour ramp, lay their bars tip to tail, and animate the arrow and the two edges rotating together one place around the ring between trips.** Because: Three separate faces with three different arrows look like three unrelated experiments unless the shared ring is visible. Prevents `cyclic-identity/misconceptions/three-trips-are-unrelated`.
- **Show a badge saying whether the reading direction and the three box axes are four different directions or only three, and say in the badge whether the sum is a new condition.** Because: Without it, a zero sum read along a box axis looks like the same fresh result as the zero sum read along the fourth direction. Prevents `cyclic-identity/misconceptions/rule-cuts-the-space-count`.
- **Draw the density profile beside the current readout, with a marker at the box, so the current is always seen next to the slope of the matter rather than its amount.** Because: The current is built from derivatives of the stress-energy tensor, so it can vanish in the densest place and be large where there is little matter. Prevents `weyl-tensor-field-equation/misconceptions/source-is-matter-not-its-change`.
- **When the split is on, always draw both halves of every bar, including halves of zero length, and keep their scale shared.** Because: Hiding the empty half lets the room-changing part look strongest where the matter is densest and lets the shape-changing part look absent in vacuum. Prevents `weyl-tensor-field-equation/misconceptions/stretch-is-strongest-where-matter-is`.
- **Hide the face-turn readout whenever the highlighted face has one edge along time, and say why in its place.** Because: Transport around such a face is a boost, not a rotation, so an angle in degrees would be the wrong kind of number.
- **Name every direction by the box's own edges and the named reading direction, never by where the viewer's camera sits.** Because: The box can be rotated freely in the scene, so screen-relative words would change meaning between beats. Prevents `holonomy/misconceptions/never-swung-so-never-turned`.

## Model

Every preset is an analytic metric whose Riemann tensor and its covariant derivative are known in closed form in one orthonormal frame at the home corner, so no chart-dependent step enters the readouts. The arrow is carried by integrating the transport equation around each face loop. Readouts quoted per unit area or per unit volume are extrapolated to zero edge length, so they equal the frame components exactly; the face turn is the measured angle at the chosen edge length, reported on the branch from minus 180 degrees, exclusive, to 180 degrees. The four weak-field presets are linearized, exact to first order in the mass or the amplitude; the frame correction to a curvature component is second order and is dropped.

**One face is one small loop**

$$
\Delta V^\rho = -R^\rho{}_{\sigma\mu\nu}\,V^\sigma a^\mu b^\nu
$$

Holds when: Leading order in the edge length; $a$ is the face's first edge and $b$ its second, in the order walked.

**Three corner trips**

$$
R^\rho{}_{\sigma\mu\nu} + R^\rho{}_{\mu\nu\sigma} + R^\rho{}_{\nu\sigma\mu} = 0
$$

Holds when: Any torsion-free connection. With box edges $(a, b, c)$ and each face carrying the edge it lacks, the three corner face changes are these three terms.

**Three opposite-face leftovers**

$$
\nabla_\lambda R^\rho{}_{\sigma\mu\nu} + \nabla_\mu R^\rho{}_{\sigma\nu\lambda} + \nabla_\nu R^\rho{}_{\sigma\lambda\mu} = 0
$$

Holds when: Any torsion-free connection. The pair stacked along $\lambda$, whose faces span $\mu$ and $\nu$, leaves over $-\epsilon^3\nabla_\lambda R^\rho{}_{\sigma\mu\nu}V^\sigma$.

**Room-changing and shape-changing parts**

$$
R_{\mu\nu\rho\sigma} = C_{\mu\nu\rho\sigma} + \big(g_{\mu[\rho}R_{\sigma]\nu} - g_{\nu[\rho}R_{\sigma]\mu}\big) - \tfrac13 R\, g_{\mu[\rho}g_{\sigma]\nu}
$$

Holds when: Four dimensions; square brackets are antisymmetrization with weight one half.

**The Weyl field equation**

$$
\nabla^\rho C_{\rho\sigma\mu\nu} = (n-3)\big(\nabla_\mu P_{\nu\sigma} - \nabla_\nu P_{\mu\sigma}\big),\qquad P_{\mu\nu} = \frac{1}{n-2}\Big(R_{\mu\nu} - \frac{R}{2(n-1)}g_{\mu\nu}\Big)
$$

Holds when: Metric compatibility, zero torsion and $n \ge 3$. In four dimensions the right side is the Weyl current, which Einstein's equation writes from derivatives of the stress-energy tensor.

**The passing ripple**

$$
h_{ij} = H_{ij}\,\sin\!\big(\omega(t-z)\big),\qquad R_{\mu\nu\rho\sigma} = \tfrac12 f''\big(\ell_\nu \ell_\rho H_{\mu\sigma} + \ell_\mu \ell_\sigma H_{\nu\rho} - \ell_\nu \ell_\sigma H_{\mu\rho} - \ell_\mu \ell_\rho H_{\nu\sigma}\big)
$$

Holds when: First order in the amplitude; $\ell_\mu = (1, 0, 0, -1)$, $H_{xx} = -H_{yy} = A_+$, $H_{xy} = H_{yx} = A_\times$, and $\nabla_\lambda R = \tfrac12 f''' \ell_\lambda(\cdots)$ with the same bracket.

**The two star presets**

$$
g_{00} = -(1 + 2\Phi),\quad g_{ij} = (1 - 2\Phi)\delta_{ij},\qquad \nabla^2\Phi = 4\pi\rho
$$

Holds when: First order in $\Phi$; outside, $\Phi = -M/r$ with $\nabla^2\Phi = 0$; inside, $\rho(r) = (3M/\pi R^3)(1 - r/R)$ gives $\Phi'(r) = M(4r/R^3 - 3r^2/R^4)$.

**Method:** Riemann and its covariant derivative are assembled in closed form at the home corner: exactly for the constant-curvature preset, and from second and third partial derivatives of $h_{\mu\nu}$ for the linearized presets, where covariant derivatives equal partial ones to first order. The orthonormal frame is the coordinate basis, whose correction is second order. Face changes come from fourth-order Runge-Kutta integration of the transport equation around each face loop; the per-unit readouts are Richardson extrapolations over a halving sequence of edge lengths, and the shrink slope is a least-squares fit of the logarithm of the drawn change against the logarithm of the edge length. Every preset is checked against the two identities, against the trace-free property of the Weyl tensor, and against the equality of the Weyl divergence with the Cotton tensor before it is offered.

| Test | State | Expect | Hidden | Note |
| --- | --- | --- | --- | --- |
| `flat-gives-zero` | preset="flat-cube", progress=1 | face-turn = 0 ±1e-12; face-coefficient = 0 ±1e-12; leftover = 0 ±1e-12; leftover-sum = 0 ±1e-12; ricci-part = 0 ±1e-12; weyl-part = 0 ±1e-12; weyl-divergence = 0 ±1e-12; weyl-current = 0 ±1e-12 | — | The flat limit: nothing anywhere. |
| `nothing-while-walking` | preset="point-mass-cube", progress=0.5 | — | face-coefficient, corner-sum, leftover, leftover-sum | Design rule no-total-before-the-last-face. |
| `constant-curvature-face` | preset="de-sitter-face", progress=1 | face-coefficient = 0.25 ±1e-09; corner-sum = 0.25 ±1e-09; ricci-part = 0.25 ±1e-09; weyl-part = 0 ±1e-09; face-turn = 0.143239448783 (rel 0.01); shrink-slope = 2 ±0.02 | — | Curvature radius 2 gives $K = 1/4$ per unit area, and the turn is $\epsilon^2 K = 0.0025$ radians, which is $0.1432394488$ degrees. The space is conformally flat, so the whole change is its room-changing part. The face turn carries a relative tolerance covering the fourth-order correction to the small-loop law at edge $0.1$. |
| `constant-curvature-face-reversed` | preset="de-sitter-face", progress=1, carried-axis="y", read-axis="x" | face-coefficient = -0.25 ±1e-09; corner-sum = -0.25 ±1e-09; ricci-part = -0.25 ±1e-09 | — | Swapping the carried and reading directions reverses the sign, because the small-loop change is antisymmetric in those two slots on this face. |
| `constant-curvature-stronger` | preset="de-sitter-face", progress=1, curvature-radius=1 | face-coefficient = 1 ±1e-09; face-turn = 0.572957795131 (rel 0.01) | — | Quartering the curvature radius squared quadruples both readouts. |
| `smallest-box` | preset="de-sitter-face", progress=1, edge=0.01 | face-coefficient = 0.25 ±1e-09; face-turn = 0.00143239448783 (rel 0.001) | — | Boundary case at the smallest edge on the grid. The turn falls by a hundred while the per-unit-area readout does not move at all. |
| `constant-curvature-leftovers-vanish` | preset="de-sitter-cube", progress=1 | leftover = 0 ±1e-12; leftover-sum = 0 ±1e-12; weyl-divergence = 0 ±1e-12; weyl-current = 0 ±1e-12 | — | Constant curvature has $\nabla R = 0$, so each leftover vanishes on its own; an Einstein space has no Weyl current. |
| `constant-curvature-corner-sum` | preset="de-sitter-corner", progress=1 | face-coefficient = 0 ±1e-12; corner-sum = 0 ±1e-12; face-turn = 0.143239448783 (rel 0.01) | — | For constant curvature every cyclic term vanishes by itself, since a component with four different slots is built only from products of metric deltas. The face still turns the arrow. |
| `ripple-corner-first-term` | preset="wave-corner", progress=1, highlight=1 | face-coefficient = 0.0353553390593274 ±1e-10; corner-sum = 0 ±1e-12; face-turn = -0.00506427927838 (rel 0.01); shrink-slope = 2 ±0.02 | — | The first corner term is $-R^t{}_{xyz} = \tfrac12 \|f''\| A_\times$ with $f'' = -\sin 45^\circ$ and $A_\times = 0.1$, so $0.03535533906$. Its face, spanned by $y$ then $z$, turns the arrow the other way, by $\epsilon^2 R_{yzyz}$ with $\epsilon = 0.05$. |
| `ripple-corner-second-term` | preset="wave-corner", progress=1, highlight=2 | face-coefficient = -0.0353553390593274 ±1e-10; face-turn = 0.00506427927838 (rel 0.01) | — | The second corner term is the exact opposite of the first, and its face turns the arrow the opposite way as well: both signs of both readouts appear on one box. |
| `ripple-corner-third-term` | preset="wave-corner", progress=1, highlight=3 | face-coefficient = 0 ±1e-12; face-turn = 0 ±1e-12 | — | The third term is zero because a linearized plane wave is of the purely radiative kind, which has no component with slots $t$, $z$, $x$, $y$ in that pattern. |
| `ripple-corner-read-along-a-box-axis` | preset="wave-corner", progress=1, read-axis="z" | face-coefficient = 0.0353553390593274 ±1e-10; corner-sum = 0 ±1e-12 | — | Reading along a box axis leaves only three different directions, so the sum is forced to zero by the earlier symmetries alone. The component is still the same number here. |
| `ripple-corner-without-the-diagonal` | preset="wave-corner", progress=1, cross-amplitude=0 | face-coefficient = 0 ±1e-12; corner-sum = 0 ±1e-12; face-turn = -0.00506427927838 (rel 0.01) | — | Boundary case: with only the stretch polarization there is no component whose four slots all differ, so every cyclic term is zero while the face still turns the arrow. |
| `ripple-leftovers` | preset="wave-cube", progress=1, highlight=1 | face-coefficient = 0.0353553390593274 ±1e-10; leftover = 0.0353553390593274 ±1e-10; leftover-sum = 0 ±1e-12; shrink-slope = 3 ±0.02; weyl-current = 0 ±1e-12 | — | With the box edges along time, $x$ and $z$ and the arrow along $y$, the pair stacked along time leaves over $\tfrac12 \|f'''\| A_\times = 0.03535533906$ at phase 45 degrees, where $f''' = -\cos 45^\circ$. |
| `ripple-leftover-other-sign-and-hidden-turn` | preset="wave-cube", progress=1, highlight=3 | leftover = -0.0353553390593274 ±1e-10 | face-turn | The third pair's leftover is the exact opposite of the first, and the second pair's is zero, so the three add to nothing. This pair's faces are spanned by time and $x$, so transport around them is a boost and the turn readout is hidden. |
| `ripple-at-zero-curvature` | preset="wave-at-zero-phase", progress=1, highlight=1 | face-coefficient = 0 ±1e-12; face-turn = 0 ±1e-12; leftover = 0.05 ±1e-10; leftover-sum = 0 ±1e-12 | — | Boundary case: at zero phase $f'' = 0$ and $f''' = -1$, so the curvature vanishes at the home corner while its derivative does not. Every face change is zero and the first leftover is $\tfrac12 A_\times = 0.05$. |
| `outside-a-star-three-leftovers` | preset="point-mass-cube", progress=1, highlight=1 | face-coefficient = 0.00073469387755102 ±1e-12; leftover = 0.000152186588921283 ±1e-13; leftover-sum = 0 ±1e-14; ricci-part = 0 ±1e-14; weyl-part = 0.00073469387755102 ±1e-12; weyl-divergence = 0 ±1e-14; weyl-current = 0 ±1e-14; shrink-slope = 3 ±0.02 | — | Mass 1 at distance 10 in the direction with components two, three and six sevenths, box edges along $x$, $y$, $z$, arrow along $x$, read along $y$. The three leftovers are $0.000152186588921$, $0.0000209912536443$ and $-0.000173177842566$, which add to zero. Vacuum, so the whole change is its shape-changing part and the current vanishes. |
| `outside-a-star-third-leftover` | preset="point-mass-cube", progress=1, highlight=3 | face-coefficient = 0.00120408163265306 ±1e-12; leftover = -0.000173177842565598 ±1e-13; face-turn = 0.000689887957402 (rel 0.01) | — | The third leftover carries the opposite sign to the other two, which is how three nonzero numbers can add to nothing. |
| `inside-a-star-split` | preset="star-cube", progress=1, highlight=3 | face-coefficient = 0.212396069538927 ±1e-10; ricci-part = 0.197530864197531 ±1e-10; weyl-part = 0.0148652053413958 ±1e-10; leftover = -0.0550696469063816 ±1e-10; leftover-sum = 0 ±1e-12; weyl-divergence = -0.0141093474426808 ±1e-10; weyl-current = -0.0141093474426808 ±1e-10 | — | Mass 1, radius 3, box at distance 1 from the centre. The room-changing part is $16/81 = 0.197530864198$, and the two Weyl readouts must agree to the last figure, since one is computed from the Weyl tensor and the other from the Schouten tensor. Both signs of both appear across this preset. |
| `inside-a-star-positive-current` | preset="star-cube", progress=1, highlight=1 | ricci-part = 0 ±1e-12; weyl-part = 0.0090702947845805 ±1e-10; leftover = 0.0291545189504373 ±1e-10; weyl-divergence = 0.0423280423280423 ±1e-10; weyl-current = 0.0423280423280423 ±1e-10 | — | The same star, first pair highlighted: the current is positive here and negative on the third pair, and its value $24/567$ comes from the density gradient, not the density. |
| `inside-a-star-reversed-slots` | preset="star-cube", progress=1, highlight=3, carried-axis="y", read-axis="x" | ricci-part = -0.197530864197531 ±1e-10; weyl-part = -0.0148652053413958 ±1e-10; leftover = 0.0550696469063816 ±1e-10; weyl-divergence = 0.0211640211640212 ±1e-10; weyl-current = 0.0211640211640212 ±1e-10 | — | Swapping the carried and reading directions flips every face and leftover readout. The divergence readout changes value as well as sign, because its first slot is the reading direction of a tensor with no symmetry between those slots. |

## Serves

- [[bianchi-identity]]: the six-face walk, the pairing of opposite faces, the three leftover bars and the sum readout that no control can move off zero
- [[cyclic-identity]]: the three corner faces with the missing-edge carry rule, and the badge that says whether the reading direction makes four different directions
- [[holonomy]]: each single face as a small loop, with the face turn, the blank readouts while the walk is in progress, and the shrink slope of two
- [[weyl-tensor-field-equation]]: the split of every face change into a room-changing and a shape-changing part, and the pair of readouts showing the Weyl divergence beside the current built from the change in the matter

## In the visual network

- **Builds on:** [[carry-an-arrow-around-a-loop]], [[four-legs-around-a-tiny-loop]]
- **Leads to:** [[falling-ring-of-crumbs]], [[twenty-of-256-slots]]

## Accessibility

Every beat says which face is being walked, which edge the arrow points along, and where each returned change points relative to the named reading direction. Every number is announced in words with its sense. The three corner trips and the three opposite pairs are distinguished by bar position and by label as well as by colour, and every control works from the keyboard.

Static alternative: A tiny box in curved space. Three trips around the faces at one corner give three changes that close into a triangle, and the three leftovers from opposite faces close into a triangle as well.

- `Space`: play or pause the walk
- `Left and Right arrows`: scrub through the face trips
- `1 to 3`: highlight the first, second or third face or opposite pair
- `F`: switch between the three corner faces and all six
- `C`: switch the carry rule between one fixed arrow and the missing edge
- `R`: step the reading direction through time, x, y and z
- `S`: turn the room-changing and shape-changing split on or off
- `Comma and full stop`: shrink or grow the box edge

## Starting material

Earlier course assets: `engine-independent-curvature-checker`, `lab-riemann-independent-components`, `scene-3d-parallel-transport-loop`, `manuscript-section-09-bianchi-einstein-tensor`, `figure-ricci-weyl`

The earlier course's finite-difference curvature checker already builds Riemann, Ricci and Weyl from an arbitrary four-dimensional metric, and becomes the independent oracle the unit tests compare the closed-form presets against. Its transport loop scene supplies the arrow-carrying code. The Ricci-versus-Weyl figure becomes the split legend. New work: the box geometry with its face ordering and carry rules, the Richardson extrapolation behind the per-unit readouts, the Weyl current readout, and the badge counting how many different directions are in play.

## Review: novice

**Verdict:** fixed (2026-09-16, revision 1)

**Retell attempt:** A tiny box floats near a star. You carry an arrow around each of its six faces, never letting it swing, and each trip brings the arrow back a bit changed. Each change is drawn as a short bar. Every edge of the box belongs to two faces and gets walked once each way, so the six bars close up and add to nothing. Then you take the faces in opposite pairs. The two faces of a pair are walked opposite ways round, so their bars nearly cancel and leave a small bit over. Three pairs means three leftovers: two point one way, the third points back, and laid end to end they close up too. That is the Bianchi identity, and no choice of space in the list breaks it. The other tour uses only the three faces at the home corner. Each of those faces leaves out one of the three edges at that corner, and on each face you carry the arrow along the edge that face leaves out. The first two trips give equal and opposite changes and the third brings back nothing, so the three add to nothing again. That is the cyclic identity, and the reason is that a tiny four-sided walk really does close up. What I could not say back: what 'reading the changes in a direction' means, since nothing told me the changes were being measured along anything; what number 'fifteen hundredths of a thousandth per unit of room' is; and what the first three rules of 'the curvature table' are, so I do not know what the fourth rule is fourth of. I was also stuck on one thing that seemed to contradict itself: one beat says all six faces are walked the same way round seen from outside the box, and a later beat says two opposite faces are walked opposite ways round seen from outside the box.

- Stumble: “Seen from outside the box, they are walked opposite ways round.”: Three beats earlier the tutor said all six faces are walked the same way round, seen from outside the box. With the same reference named both times, the two sentences contradict each other and I could not tell which one to believe.
- Stumble: “So the six trips retrace every step, and the six bars close back on the starting point.”: "Retrace" sounds like walking the same steps the same way again, which is the opposite of the cancelling that is meant. And "the starting point" is a place on the bar chain that has not been named, so I looked back at the box corner instead.
- Stumble: “This pair leaves over about fifteen hundredths of a thousandth per unit of room.”: I had to do two divisions in my head to find out how big that number is. "Per unit of room" is also a third name for one idea: the readout says "per unit volume", and "room-changing" is used later for something else entirely.
- Stumble: “What is left between them is small, and the readout gives it.”: There are ten readouts on screen and the line does not say which one to look at.
- Stumble: “The reason is only that a box's edges are shared, so no experiment could ever catch the rule failing.”: "A box's edges are shared" does not say shared with what, and the word "only" made me read the reason as an excuse. The jump from shared edges to "no experiment could ever" is one step too big.
- Stumble: “All three pairs tinted in three colours; the three leftover bars laid tip to tail, closing on the starting point.”: The three pairs and their three bars are told apart by colour alone, so I could not match a bar to a pair, and neither could anyone reading this in one colour.
- Stumble: “A face leaves out exactly one edge: the one that is not part of it.”: The sentence says the same thing twice and teaches nothing: the edge that is left out is the one that is not part of the face.
- Stumble: “Look at the home corner of this tiny box.”: This tour opens with "the home corner" as if I already knew which corner that is; nothing in this tour has named it.
- Stumble: “So from trip to trip, the arrow and the two edges all move one place around a ring of the three directions.”: There is no ring on screen, and I could not picture directions moving around one. I could not tell whether the ring closes after three trips.
- Stumble: “The third trip brings back nothing at all.”: "Brings back nothing" first sounded to me as if the arrow did not come back, rather than coming back unchanged.
- Stumble: “That is the fourth rule of the curvature table.”: No curvature table and no first three rules have been mentioned, so "the fourth rule" has nothing to be fourth of.
- Stumble: “A space where they miss by a gap that keeps pace with the area has twist, and there these three changes need not cancel.”: One sentence carries a new word, a condition on the size of a gap, and a consequence. "Keeps pace with the area" was the part I could not picture.
- Stumble: “Now I read the changes in a direction the box's edges already run along.”: This is the first time the tour says the changes are read along any direction at all. Until here I thought each number was just the length of a bar, so "in a direction" arrived with nothing behind it, and I did not know what direction had been used before.
- Stumble: “Every face returns the arrow exactly as it set off, every bar has no length, and every readout reads zero.”: Not every readout reads zero here: the shrink slope is a power, not a change, and a shrink slope of zero would mean the change does not shrink at all.
- Stumble: “The solid shape-changing pieces stay: one twelve ten-thousandths per unit area on this face.”: "One twelve ten-thousandths" is not a number I can say or hear. The test for this state gives twelve ten-thousandths, so the stray "one" only garbles it.
- Stumble: “the three corner trips add to {abs} along the reading direction”: This sum is zero in every state the demonstration can reach, so what the tutor always says aloud is "add to zero along the reading direction", which gives a direction to a zero. The same goes for the sum of the three leftovers.
- Stumble: “Time, and the other pair”: I could not work out which pair is "the other" one, because the option above it says only "two space directions" without saying which two.
- Stumble: “A ripple caught at zero curving”: The label sounds as if the ripple has no curving anywhere, when the beat says its curving passes through zero just at the box.
- Stumble: “Its leftover per unit volume is minus the covariant derivative along x of the Riemann component with the carried direction and then y and z.”: Three slots are named for a tensor that has four; the reading direction, which the readout actually reports, is left out of the list.
- Stumble: “Predict what happens to the sum.”: The written prediction asks whether the identity stops the curvature from changing from place to place, but the spoken prompt asks about the sum instead, and the sum was already said to stay at zero. The two prompts do not match.
- Stumble: “Each single face still changes the arrow, so the face readout is a quarter per unit area.”: The "so" promises that the value follows from the face changing the arrow, and it does not; only the curvature radius fixes the quarter.
- Fixed: Removed the contradiction between the six faces being walked the same way round seen from outside the box and the opposite pair being walked opposite ways: the pair beat now says "seen from one and the same side of the box".
- Fixed: Replaced "retrace every step" with "every step one way is undone by the same step the other way", and said once where the starting point of the bar chain is.
- Fixed: Gave the entry number in one unit word: "one and a half ten-thousandths per unit of volume" in place of "fifteen hundredths of a thousandth per unit of room", and used "volume" in the shrink beat too, so "room" is left to mean only the room-changing part.
- Fixed: Named the readout being quoted in the opposite-pair beat.
- Fixed: Spelled out the shared-edge reason in the try-to-break-it beat instead of asserting it, and named the control as the space and time list.
- Fixed: Added number labels beside the three colours for the three pairs, in the beat, its description and the picture composition.
- Fixed: Rewrote the circular sentence about the edge a face leaves out, and introduced the home corner in the corner tour before using the name.
- Fixed: Replaced the unexplained "ring of the three directions" with a step-to-the-next-direction sentence that says it closes after three trips.
- Fixed: Replaced "brings back nothing at all" with a line that says the arrow comes back unchanged and its bar has no length.
- Fixed: Gave "the fourth rule of the curvature table" a table to be the fourth rule of.
- Fixed: Split the torsion sentence so "twist" gets its own sentence, and replaced "keeps pace with the area" with "grows in step with the area of the little walk".
- Fixed: Said in the entry corner tour that each change is measured along a chosen direction, and that the direction so far has been time, before switching it to a box edge direction.
- Fixed: Narrowed "every readout reads zero" in the flat beat to "every change readout", since the shrink slope is not a change.
- Fixed: Removed the stray "one" from "one twelve ten-thousandths".
- Fixed: Reworded the two sums that are identically zero so the direction qualifies the measurement rather than the value: "measured along the reading direction, the three corner trips add to {abs}", with a matching minus form.
- Fixed: Made the three time-plus-two-space box axis labels name their directions.
- Fixed: Renamed the zero-phase preset so it does not read as a ripple with no curving anywhere.
- Fixed: Added the reading direction to the list of slots in the working leftover formula.
- Fixed: Matched the spoken prediction prompt to the written prediction in the move-the-box-outward beat.
- Fixed: Replaced a false "so" with "and" in the constant-curvature beat.
- Concern: The entry tours quote every number in scene units (per unit of area, per unit of volume) with no everyday anchor and never say why daily life hides the effect, which the novice contract asks for. A number tied to something a 16-year-old can picture would need a new state or a new beat, so I have not invented one.
- Concern: The entry tour for the Bianchi identity draws each returned change as a bar with a length and a direction, but every readout is one component along the reading direction, and the entry tour never says so. The corner tour now says it in one sentence; the six-face tour would need a beat of its own to say it properly.
- Concern: The shrink-slope readout has no sensible value in the flat preset, where the change is exactly zero and no power fits it. Its range starts at 0, and a spoken "falls off as the box edge to the power zero" would claim the change does not shrink. Either hide the readout when the change is zero or give it a stated blank.
- Concern: "Room-changing" (the Ricci part) and "per unit of room" (per unit volume) were two senses of one word. I moved the measure to "volume" everywhere it is spoken, but the compound "room-changing" still means volume-changing, so a later stage may want to rename it "volume-changing" throughout.
- Concern: The "Divergence of the Weyl tensor" readout label is the only learner-visible place that uses the technical name; every beat calls it "the divergence of the shape-changing table". The label should probably match the spoken phrase.
- Concern: The corner-sum readout is labelled and spoken as a sum over three corner faces, but it is shown and tested in states where only one face is highlighted and in all-six states as well. It is not clear from the wording what it reports when the six-face setting is on.
- Concern: The entry beat that asks for a prediction about the six changes comes before anything on screen has shown what one trip does, so the only ground for a guess is the entry way the reader has already read. A short first trip before the prediction would make it a prediction rather than a guess.
