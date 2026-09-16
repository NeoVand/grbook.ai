---
type: "visual"
schema_version: 2
id: "card-touching-a-curved-patch"
title: "Card touching a curved patch"
kind: "interactive-3d"
priority: "core"
status: "specified"
revision: 3
rungs: ["entry", "working"]
serves: ["second-fundamental-form", "principal-curvatures", "gaussian-curvature"]
builds_on: ["best-fit-circle-along-a-bend"]
leads_to: ["bend-arrow-split-on-a-surface", "plumb-lines-along-a-walk", "paced-ring-on-a-ball-and-a-plain", "lines-of-curvature-on-an-ellipsoid"]
---

# Card touching a curved patch

`card-touching-a-curved-patch` · interactive-3d · core · specified · rungs: entry, working

> A flat see-through card rests on a curved surface at one point, and a ruler turning about that point shows how fast the gap under the card opens in each direction.

## What it makes visible

A flat card touching a curved patch at one point shows the bending of the surface as the gap that opens under a ruler laid along the card: the gap grows with the distance squared, and how quickly it grows depends on the direction of the ruler. Turning the ruler about the touching point finds the sharpest and the gentlest bend, always a quarter turn apart unless every direction bends alike, and a sweep plot traces Euler's formula between them. The two extreme bends, signed by which side of the card the surface goes to, multiply to the Gaussian curvature, and a small ring paced out on the same patch comes out short, exact, or long by the fraction that number predicts. It is the one picture behind the second fundamental form, the principal curvatures, and the outsider's route to the Gaussian curvature.

## The picture

A pale blue patch of surface with a faint grid fills the scene, seen from a little above. A translucent white card with a thin grey edge touches it at the centre, and a green arrow stands on the card at the touching point to mark the chosen side. A red ruler line runs from the touching point along the card, with a red reference tick on the card's edge marking the zero direction. At the ruler's tip an orange bar joins the card to the surface: the gap. Optional layers: an orange sweep plot of the gap against the ruler's direction, two dashed grey lines on the card marking the principal directions, and a purple ring paced out on the surface at the ruler's distance. Readouts sit beside the plot: the gap, the bend along the ruler as a best-fit radius, the two principal bends as radii, their direction, their product, and the ring's length, shortfall and curvature.

| Element | Shows |
| --- | --- |
| Pale blue patch with a faint grid | the surface near the touching point: ball, can, spoon bowl, egg, saddle, crisp, or a custom patch |
| Translucent white card with a grey edge | the tangent plane at the touching point |
| Green arrow on the card | the chosen unit normal, the side toward which bending counts as positive |
| Red ruler line and red reference tick | the direction being probed and the zero of the ruler angle |
| Orange bar at the ruler's tip | the signed gap between the card and the surface at the probe distance |
| Orange sweep plot | the gap at the probe distance against the ruler's direction, Euler's formula |
| Dashed grey lines on the card | the principal directions, a quarter turn apart |
| Purple paced ring | the ant's ring test at the same spot, whose shortfall the product of the two bends predicts |

## Book figure

Two panels. Left: a drinks can on its side with a card resting on it; a ruler across the can shows an orange gap at its tip, and a second ruler along the can lies flat with no gap. Right: an egg on its side with the card at its widest part, the two dashed principal directions a quarter turn apart, and beside it a small polar plot of the gap against direction with its high and low points marked.

Labels: card, across the can, along the can, gap, sharpest bend, gentlest bend, quarter turn. Aspect 2:1. Alt text: Left, a card on a drinks can: a ruler across the can leaves a gap at its tip while a ruler along the can touches the whole way. Right, a card on an egg with its sharpest and gentlest bending directions marked a quarter turn apart, and a plot of the gap against direction.

## Variants

- **static** `static-card` (fallback): The print figure as an SVG card, used when 3D is unavailable and as a summary card.
- **interactive-2d** `slice-view-2d`: A side view of the slice through the normal and the ruler: the parabola of the surface, the flat card, the orange gap at the probe distance, and a slider for the ruler angle that reshapes the parabola.
- **interactive-3d** `full-3d`: The full experience: every surface preset, a draggable ruler, the sweep plot, principal marks, the normal flip, and the paced ring.

## Parameters

| Id | Label | Type | Options or range | Default | Available when | Effect |
| --- | --- | --- | --- | --- | --- | --- |
| `surface` | Surface | enum | ball, can, bowl, egg, saddle, crisp, custom | "ball" | — | Chooses the patch. With the green arrow up, the ball, can and egg bend away from the arrow (the card rests on top), the bowl bends toward it, the saddle bends toward it along the reference tick and away from it a quarter turn on, and the crisp is the saddle turned by 45 degrees so that its principal directions sit at plus and minus 45 degrees from the tick. The custom patch takes its three coefficients directly. |
| `radius-1` | Bend radius along the tick | number | 1–40 step 0.1 cm | 12 | surface in ball, can, bowl, egg, saddle, crisp | Best-fit radius in centimetres of the bend along the reference tick: the ball's radius, the can's radius (across it), the bowl's radius along the tick, the egg's radius around it, and the saddle's or crisp's bend radius in both principal directions. |
| `radius-2` | Bend radius a quarter turn from the tick | number | 1–40 step 0.1 cm | 2 | surface in bowl, egg | Best-fit radius of the bend a quarter turn from the tick: the bowl's radius across the tick and the egg's radius along the egg. |
| `k-xx` | Coefficient K xx | number | -1–1 step 0.01 | 0 | surface in custom | Bend per centimetre along the tick for the custom patch $z = \tfrac12(K_{xx}x^2 + 2K_{xy}xy + K_{yy}y^2)$, with $z$ measured along the green arrow and lengths in centimetres. |
| `k-xy` | Coefficient K xy | number | -1–1 step 0.01 | 0 | surface in custom | Cross coefficient per centimetre of the custom patch; nonzero values turn the principal directions away from the tick. |
| `k-yy` | Coefficient K yy | number | -1–1 step 0.01 | 0 | surface in custom | Bend per centimetre a quarter turn from the tick for the custom patch. |
| `normal` | Green arrow | enum | up, down | "up" | — | Flips the chosen normal. Every signed bend and the gap's sign reverse, the largest and smallest signed bends swap names, and the product of the two bends stays the same. The ruler, its angle and the reference tick stay where they are: angles are always measured on the card seen from above, so the flip negates all three coefficients and nothing else. |
| `ruler-angle` | Ruler direction | number | 0–180 step 5 deg | 0 | — | Turns the red ruler about the touching point, measured from the reference tick, counterclockwise seen from above the card (the side the green arrow points to when it is up). Flipping the arrow does not change this sense or the ruler's position. |
| `probe-distance` | Distance along the ruler | number | 0.5–4 step 0.5 cm | 2 | — | Where along the ruler the gap is read, and the radius of the paced ring when the ring test is on. |
| `sweep-plot` | Sweep plot | boolean | — | false | — | Shows the orange plot of the gap at the probe distance against the ruler's direction, over a half turn. |
| `principal-marks` | Principal marks | boolean | — | false | — | Draws two dashed grey lines on the card along the principal directions and marks the plot's highest and lowest points; on a ball every direction is principal, so the marks follow the tick and the readout says so. |
| `ring-test` | Ring test | boolean | — | false | — | Adds a purple ring paced out on the surface: straight walks of the probe distance from the touching point in every direction, with the ring joined through their ends. The ring readouts appear only when the walk completes. |
| `progress` | Ring walk progress | progress | 0–1 step 0.01 | 0 | — | Paces the ring out around the touching point when the ring test is on, and does nothing otherwise; the ring readouts appear only at 1. |

## Presets

- `basketball` Card on a basketball: surface="ball", radius-1=12, normal="up", ruler-angle=0, probe-distance=2
- `basketball-flipped` Card on a basketball, arrow pointing down: surface="ball", radius-1=12, normal="down", ruler-angle=0, probe-distance=2
- `can-lying-on-its-side` Card on a drinks can, ruler across: surface="can", radius-1=3.3, normal="up", ruler-angle=0, probe-distance=2
- `can-sweep` Drinks can with the sweep plot: surface="can", radius-1=3.3, normal="up", ruler-angle=90, probe-distance=2, sweep-plot=true, principal-marks=true
- `spoon-bowl` Card in a spoon bowl: surface="bowl", radius-1=5, radius-2=2, normal="up", ruler-angle=0, probe-distance=2
- `spoon-bowl-sweep` Spoon bowl with the sweep plot: surface="bowl", radius-1=5, radius-2=2, normal="up", ruler-angle=60, probe-distance=2, sweep-plot=true, principal-marks=true
- `egg-widest-part` Card on an egg at its widest part: surface="egg", radius-1=2, radius-2=4.5, normal="up", ruler-angle=0, probe-distance=1
- `egg-sweep` Egg with the sweep plot and principal marks: surface="egg", radius-1=2, radius-2=4.5, normal="up", ruler-angle=90, probe-distance=1, sweep-plot=true, principal-marks=true
- `saddle` Card through a saddle: surface="saddle", radius-1=6, normal="up", ruler-angle=0, probe-distance=2
- `crisp-turned` Saddle-shaped crisp turned by 45 degrees: surface="crisp", radius-1=6, normal="up", ruler-angle=0, probe-distance=2
- `crisp-sweep` Turned crisp with the sweep plot and principal marks: surface="crisp", radius-1=6, normal="up", ruler-angle=0, probe-distance=2, sweep-plot=true, principal-marks=true
- `flat-sheet` Card on a flat sheet: surface="custom", k-xx=0, k-xy=0, k-yy=0, normal="up", ruler-angle=0, probe-distance=2
- `soap-film-waist` Card on a soap film's waist: surface="custom", k-xx=0.5, k-xy=0, k-yy=-0.5, normal="up", ruler-angle=0, probe-distance=2
- `tilted-custom-patch` Custom patch with turned principal directions: surface="custom", k-xx=0.3, k-xy=-0.1, k-yy=0.1, normal="up", ruler-angle=0, probe-distance=2, principal-marks=true
- `ring-on-basketball` Paced ring on the basketball: surface="ball", radius-1=12, normal="up", ruler-angle=0, probe-distance=2, ring-test=true
- `ring-on-egg` Paced ring on the egg: surface="egg", radius-1=2, radius-2=4.5, normal="up", ruler-angle=0, probe-distance=0.5, ring-test=true, principal-marks=true
- `ring-on-saddle` Paced ring on the saddle: surface="saddle", radius-1=6, normal="up", ruler-angle=0, probe-distance=1, ring-test=true
- `ring-on-can` Paced ring on the drinks can: surface="can", radius-1=3.3, normal="up", ruler-angle=0, probe-distance=2, ring-test=true
- `ring-on-waist` Paced ring on the soap film's waist: surface="custom", k-xx=0.5, k-xy=0, k-yy=-0.5, normal="up", ruler-angle=0, probe-distance=0.5, ring-test=true, principal-marks=true
- `ring-on-flat-sheet` Paced ring on the flat sheet: surface="custom", k-xx=0, k-xy=0, k-yy=0, normal="up", ruler-angle=0, probe-distance=2, ring-test=true

## Readouts

- `height` Gap at the ruler's tip (cm; visible always; 3 decimals; sense: positive when the surface at the ruler's tip lies on the side of the card the green arrow points to): “at the ruler's tip the surface lies {abs} centimetres from the card, toward the green arrow” / “at the ruler's tip the surface lies {abs} centimetres from the card, away from the green arrow”
- `radius-along-ruler` Bend along the ruler, as a best-fit radius (cm; visible always; 3 decimals; sense: positive when the slice along the ruler bends toward the green arrow; shows no bend when the slice is straight): “along the ruler the surface bends toward the green arrow, with a best-fit circle of radius {abs} centimetres” / “along the ruler the surface bends away from the green arrow, with a best-fit circle of radius {abs} centimetres”
- `radius-1` Largest signed bend, as a best-fit radius (cm; visible always; 3 decimals; sense: positive when the largest signed bend goes toward the green arrow; shows no bend when that bend is zero): “the largest signed bend goes toward the green arrow, with a best-fit circle of radius {abs} centimetres” / “the largest signed bend goes away from the green arrow, with a best-fit circle of radius {abs} centimetres”
- `radius-2` Smallest signed bend, as a best-fit radius (cm; visible always; 3 decimals; sense: positive when the smallest signed bend goes toward the green arrow; shows no bend when that bend is zero): “the smallest signed bend goes toward the green arrow, with a best-fit circle of radius {abs} centimetres” / “the smallest signed bend goes away from the green arrow, with a best-fit circle of radius {abs} centimetres”
- `principal-angle` Direction of the largest signed bend (deg; visible always; 1 decimals; range (-90, 90]; sense: positive counterclockwise from the reference tick, seen from above the card, whichever way the green arrow points; reports zero where every direction bends alike): “the largest signed bend lies {abs} degrees counterclockwise from the red tick on the card's edge, seen from above the card” / “the largest signed bend lies {abs} degrees clockwise from the red tick on the card's edge, seen from above the card”
- `gaussian-curvature` Product of the two bends (m^-2; visible always; 2 decimals; sense: positive when the two principal bends go toward the same side of the card): “the two bends multiplied give {abs} per square metre, and the bends do not go to opposite sides” / “the two bends multiplied give minus {abs} per square metre, the bends going to opposite sides of the card”
- `ring-length` Paced ring length (cm; visible on-complete; 4 decimals): “the paced ring is {value} centimetres long”
- `ring-missing-fraction` Ring shortfall (percent; visible on-complete; 4 decimals; sense: positive when the ring is shorter than a flat ring of the same walked distance): “the ring comes out {abs} percent shorter than on flat paper” / “the ring comes out {abs} percent longer than on flat paper”
- `ring-curvature` Ring test curvature (m^-2; visible on-complete; 2 decimals; sense: positive when the ring comes out short): “the ring's shortfall gives the ant's number {abs} per square metre” / “the ring's excess gives the ant's number minus {abs} per square metre”

## Tours

### `gap-under-a-card` · for [[second-fundamental-form]] · entry

1. `meet-the-card` (entry, await none) state: preset="basketball"  
   *Pale blue basketball patch, translucent card on top, green arrow up, red ruler at the reference tick, orange gap bar at 2 cm reading 0.167 cm.*  
   Say: “Here is a basketball, drawn in pale blue, with a flat see-through card resting on top. The card touches the ball at one point. A green arrow stands on the card at the touching point, pointing up, away from the ball. From that point a red line runs along the card, like a ruler. At the ruler's tip, 2 centimetres out, an orange bar drops from the card down to the ball. That bar is the gap under the card, and it reads just under 2 millimetres.”  
   Describe: A flat card rests on a ball and touches it at one point. Two centimetres from the touching point, the gap between the card and the ball is 0.17 centimetres, just under 2 millimetres.
2. `predict-double-distance` (entry, await prediction) state: preset="basketball"; evidences `second-fundamental-form/checks/double-the-distance`  
   *Same view, paused.*  
   Predict: “If I slide the ruler's tip out to 4 centimetres, twice as far from the touching point, how big will the gap be?”  
   Say: “Before I move anything, make a guess. If I slide the ruler's tip out to 4 centimetres, twice as far from the touching point, how big will the gap be?”  
   Describe: The ruler's tip waits at 2 centimetres, where the gap is just under 2 millimetres.
3. `slide-the-tip-out` (entry, await none) state: preset="basketball"; animate probe-distance → 4 over 3 s  
   *The orange bar slides out to 4 cm and grows to 0.667 cm.*  
   Say: “I slide the tip out to 4 centimetres. The orange bar grows to about 7 millimetres, four times as big for twice the distance. Close to the touching point, doubling the distance makes the gap four times bigger. The reason is that the gap grows like the distance multiplied by itself, and 2 times 2 is 4.”  
   Describe: The ruler's tip moves out to 4 centimetres. The gap reads 0.67 centimetres, about four times the gap at 2 centimetres.
4. `bend-at-the-touching-point` (entry, await none) state: preset="basketball", probe-distance=4; animate probe-distance → 0.5 over 3 s  
   *The orange bar slides in to 0.5 cm and shrinks to 0.010 cm.*  
   Say: “Now I slide the tip back in to half a centimetre. The orange bar shrinks to a hundredth of a centimetre, almost nothing. But the bend is not the size of the gap. The bend is how quickly the gap grows as the tip moves out. So the ball is bending right at the touching point too, where the gap is zero.”  
   Describe: The tip moves in to half a centimetre and the gap reads a hundredth of a centimetre. The ball bends there all the same, because bending means how quickly the gap grows.
5. `card-on-a-can` (entry, await prediction) state: preset="can-lying-on-its-side"; evidences `second-fundamental-form/checks/card-on-a-can`  
   *Pale blue can patch, card on top, red ruler pointing across the can, orange bar at 2 cm reading 0.606 cm.*  
   Predict: “If I turn the ruler a quarter turn, so it points along the can's length, how big will the gap be at 2 centimetres?”  
   Say: “Now the card rests on a drinks can lying on its side. The red ruler points across the can, around its round side. At 2 centimetres out, the orange bar reads 6 millimetres. Make a guess. If I turn the ruler a quarter turn, so it points along the can's length, how big will the gap be at 2 centimetres?”  
   Describe: The card rests on a drinks can lying on its side. With the ruler pointing across the can, the gap 2 centimetres out is 0.61 centimetres.
6. `turn-along-the-can` (entry, await none) state: preset="can-lying-on-its-side"; animate ruler-angle → 90 over 3 s  
   *The red ruler turns to 90 degrees, along the can; the orange bar shrinks to zero.*  
   Say: “I turn the red ruler a quarter turn, seen from above, so it points along the can. The orange bar shrinks to nothing. The card lies on the can the whole way along, so the gap stays zero. At this one point, the can bends across but not along.”  
   Describe: The ruler turns to point along the can, and the gap reads zero. The can bends across its round side but not along its length.
7. `gap-for-every-direction` (entry, await none) state: preset="can-sweep"  
   *The sweep plot appears: orange curve of the gap at 2 cm against the ruler angle, highest at 0 and 180 degrees, zero at 90.*  
   Say: “The orange curve on the plot shows the gap at 2 centimetres as the ruler turns. Left to right along the plot is the ruler's direction: across the can, then along it after a quarter turn, then across it again after a half turn. The curve is highest with the ruler across the can and drops to zero with the ruler along it. The gap at a fixed distance shows the bend in each direction. This rule, the bend for every direction at one point, is called the second fundamental form.”  
   Describe: A plot of the gap against the ruler's direction, from across the can, through along it, back to across it. The gap is largest with the ruler across the can and zero with the ruler along it.

### `turn-a-ruler-on-an-egg` · for [[principal-curvatures]] · entry

1. `sharpest-bend-around-the-egg` (entry, await none) state: preset="egg-widest-part"  
   *Pale blue egg patch at its widest part, card on top, red ruler around the egg, orange bar at 1 cm reading 0.25 cm.*  
   Say: “Here is a plastic egg, 4 centimetres wide, lying on its side. The see-through card touches its widest part. The red ruler points around the egg. At 1 centimetre out the orange bar reads 2 and a half millimetres. Of all the directions the ruler can point, this is the sharpest bend.”  
   Describe: A card touches an egg at its widest part. With the ruler pointing around the egg, the gap 1 centimetre out is 0.25 centimetres, the biggest gap in any direction.
2. `predict-the-gentlest` (entry, await prediction) state: preset="egg-widest-part"; evidences `principal-curvatures/checks/helmet-top`  
   *Same view, paused.*  
   Predict: “The sharpest bend is around the egg. When I turn the ruler, where do you expect the gentlest bend, the smallest gap?”  
   Say: “Make a guess before I turn the ruler. The sharpest bend is around the egg. Where do you expect the gentlest bend, the smallest gap?”  
   Describe: The ruler waits pointing around the egg, where the gap is biggest.
3. `turn-along-the-egg` (entry, await none) state: preset="egg-widest-part"; animate ruler-angle → 90 over 4 s  
   *The red ruler turns through a quarter turn to point along the egg; the orange bar shrinks to 0.111 cm.*  
   Say: “I turn the red ruler slowly, seen from above. The orange bar shrinks the whole way. After a quarter turn the ruler points along the egg, from end to end, and the bar reads about 1 millimetre, the smallest gap in any direction. So the sharpest and the gentlest bends are a quarter turn apart. These two bends are called the principal curvatures of the point.”  
   Describe: The ruler turns a quarter turn to point along the egg. The gap shrinks to 0.11 centimetres, the smallest in any direction.
4. `marks-a-quarter-turn-apart` (entry, await none) state: preset="egg-sweep"  
   *Sweep plot on, principal marks on: two dashed grey lines on the card at 0 and 90 degrees; the orange curve peaks at 0 and 180 and dips at 90.*  
   Say: “The orange curve on the plot is the gap for every direction of the ruler. Two dashed grey lines on the card mark the directions of the curve's highest point and lowest point. They cross at a right angle. On any smooth surface the two marks are a quarter turn apart, unless every direction bends alike, as on a ball.”  
   Describe: A plot of the gap against direction, with its highest and lowest points marked. The two marked directions are a quarter turn apart.
5. `saddle-along-the-horse` (entry, await prediction) state: preset="saddle"; evidences `principal-curvatures/checks/mountain-pass`  
   *Pale blue saddle patch, card cutting through it at the level middle, green arrow up, red ruler along the horse, orange bar standing above the card reading +0.333 cm.*  
   Predict: “If I turn the ruler a quarter turn, across the saddle, which way will the surface bend, up toward the green arrow or down away from it?”  
   Say: “Now the see-through card touches the middle of a saddle, where the seat is level, so the seat passes through the card. The green arrow on the card points up; it marks the side of the card we count as up. Along the red ruler, along the horse, the pale blue seat rises on both sides of the touching point, like a valley. So the orange bar now stands above the card, 3 millimetres up. Count bending up, toward the green arrow, as positive. Make a guess. If I turn the ruler a quarter turn, across the saddle, which way will the surface bend, up or down?”  
   Describe: The card touches the level middle of a saddle, and the seat passes through the card. Along the horse the seat rises on both sides, and the surface 2 centimetres out is 0.33 centimetres above the card, on the green arrow's side.
6. `saddle-across-the-horse` (entry, await none) state: preset="saddle"; animate ruler-angle → 90 over 3 s  
   *The ruler turns to 90 degrees; the orange bar now hangs below the card reading −0.333 cm.*  
   Say: “I turn the red ruler a quarter turn, seen from above. Across the horse the seat drops away on both sides, like a hill. The orange bar now hangs below the card, 3 millimetres down, so this bend counts as negative. At a saddle-shaped point like this, one principal curvature is positive and the other negative, and their directions are still a quarter turn apart.”  
   Describe: The ruler turns to point across the horse. The surface 2 centimetres out is 0.33 centimetres below the card, so this bend is negative.
7. `crisp-turned-on-the-table` (entry, await none) state: preset="crisp-sweep"  
   *Crisp patch turned 45 degrees, sweep plot and marks on: dashed grey lines at 45 and −45 degrees; along the reference tick the gap is zero.*  
   Say: “Last, a saddle-shaped crisp, turned on the table by an eighth of a turn compared with the saddle. The dashed grey marks turned with it. They now sit an eighth of a turn to either side of the red tick on the card's edge. One marks where the crisp bends up, the other where it bends down. They are still a quarter turn apart from each other. The red ruler points at the red tick, halfway between the two marks, and there the gap is zero. Halfway between bending up and bending down, the surface runs straight along the ruler.”  
   Describe: A saddle-shaped crisp turned by an eighth of a turn. The marked directions of the sharpest upward and downward bends sit an eighth of a turn to either side of the red tick on the card's edge. They are a quarter turn apart from each other. Along the red tick, halfway between them, the gap is zero.

### `euler-formula-in-a-spoon` · for [[principal-curvatures]] · working

1. `bowl-along-the-tick` (working, await none) state: preset="spoon-bowl"  
   *Pale blue spoon bowl, card at its lowest point inside, green arrow up into the bowl, red ruler along the tick, orange bar above the card reading 0.4 cm; radius readout 5 cm.*  
   Say: “The card touches the bottom of a spoon bowl from inside, and the green arrow points up, into the bowl. Along the red ruler, along the reference tick, the surface rises 4 millimetres at 2 centimetres out. The readout turns that into a bend of 0.2 per centimetre toward the arrow, a best-fit circle of radius 5 centimetres.”  
   Describe: The card sits at the bottom of a spoon bowl. Along the reference direction the surface rises 0.4 centimetres at 2 centimetres out, a best-fit radius of 5 centimetres.
2. `bowl-across-the-tick` (working, await none) state: preset="spoon-bowl"; animate ruler-angle → 90 over 3 s  
   *Ruler turns to 90 degrees; orange bar reads 1.0 cm; radius readout 2 cm.*  
   Say: “A quarter turn on, counterclockwise seen from the arrow's side, the surface rises a full centimetre at 2 centimetres out: a bend of 0.5 per centimetre, radius 2 centimetres. These are the two principal curvatures, 0.5 and 0.2 per centimetre, in perpendicular directions, both toward the arrow.”  
   Describe: The ruler turns a quarter turn. The surface rises 1 centimetre at 2 centimetres out, a best-fit radius of 2 centimetres.
3. `predict-sixty-degrees` (working, await prediction) state: preset="spoon-bowl", ruler-angle=60; evidences `second-fundamental-form/checks/spoon-bowl-directions`  
   *Ruler at 60 degrees, readouts hidden behind the prediction prompt.*  
   Predict: “What is the best-fit radius of the slice at 60 degrees from the reference tick?”  
   Say: “I set the ruler at 60 degrees from the reference tick. Using the two principal curvatures, predict the best-fit radius of the slice along the ruler.”  
   Describe: The ruler points 60 degrees from the reference direction. Predict the best-fit radius there from the principal curvatures 0.2 and 0.5 per centimetre.
4. `reveal-sixty-degrees` (working, await none) state: preset="spoon-bowl-sweep"  
   *Sweep plot on with marks at 0 and 90 degrees; radius readout 2.353 cm at 60 degrees.*  
   Say: “The readout gives a radius of 2.353 centimetres. That is Euler's formula: the bend at an angle is the first principal curvature times cosine squared plus the second times sine squared. Here 0.2 times a quarter plus 0.5 times three quarters is 0.425 per centimetre, and one over 0.425 is 2.353. The orange curve on the plot is that cosine-squared law, with its lowest point at the tick and its highest point a quarter turn on.”  
   Describe: At 60 degrees the best-fit radius is 2.353 centimetres, from Euler's formula: 0.2 times cosine squared of 60 degrees plus 0.5 times sine squared of 60 degrees is 0.425 per centimetre.
5. `flip-the-arrow` (working, await none) state: preset="spoon-bowl-sweep", normal="down"  
   *Green arrow points down; gap reads −0.85 cm; radius along the ruler −2.353 cm; largest signed bend now −0.2 per cm (radius −5) at the tick; product still 1000 per square metre.*  
   Say: “Now I flip the green arrow to point down, away from the bowl. Every signed bend changes sign. The gap along the ruler reads 8 and a half millimetres on the side away from the arrow, and the radius is minus 2.353 centimetres. The principal curvatures become minus 0.2 and minus 0.5 per centimetre, so the one called largest is now the gentler bend, along the tick. The product of the two, 1000 per square metre, does not change.”  
   Describe: With the arrow flipped, every signed bend changes sign and the roles of largest and smallest swap, but the product of the two principal curvatures stays 1000 per square metre.

### `multiply-the-two-bends` · for [[gaussian-curvature]] · entry

1. `two-bends-on-the-egg` (entry, await none) state: preset="egg-sweep", ruler-angle=0  
   *Egg with principal marks on; radius readouts 2 cm (around) and 4.5 cm (along); product readout 1111.11 per square metre.*  
   Say: “Back on the plastic egg at its widest part. The two dashed grey marks on the card show the two principal bends. Around the egg, the best-fit circle, the circle that matches the bend best, has a radius of 2 centimetres. Along the egg, it has a radius of 4 and a half centimetres. The outsider's rule multiplies the two radii, 2 times 4 and a half is 9, and divides 1 by the result: one ninth per square centimetre. A square metre holds 10,000 square centimetres, so that is about 1111 per square metre, which is what the readout shows. This number is called the Gaussian curvature of the spot.”  
   Describe: On the egg's widest part the two principal bends have best-fit radii of 2 centimetres around the egg and 4.5 centimetres along it. One divided by their product is one ninth per square centimetre, about 1111 per square metre, the spot's Gaussian curvature.
2. `pace-a-ring-on-the-egg` (entry, await none) state: preset="ring-on-egg"; animate progress → 1 over 4 s  
   *A purple ring is paced out half a centimetre from the touching point; on completion the ring readouts appear: shortfall 0.452 percent, ring curvature 1085.65 per square metre.*  
   Say: “Now an ant paces out a purple ring on the egg. She walks straight out half a centimetre from the touching point in every direction and joins the ends. The ring comes out about 0.45 percent shorter than on flat paper. Turned into the ant's number, the Gaussian curvature from her matching ball, the ring gives about 1086 per square metre, close to the 1111 from the two bends. The small difference is because the ring is not tiny compared with the egg; a smaller ring gets closer.”  
   Describe: A ring paced half a centimetre from the touching point comes out 0.45 percent short. The ant's number from the ring is about 1086 per square metre, close to the 1111 from multiplying the two bends.
3. `predict-half-the-ball` (entry, await prediction) state: preset="basketball"; evidences `gaussian-curvature/checks/marble-and-football`  
   *Basketball preset; product readout 69.44 per square metre.*  
   Predict: “If I swap the basketball for a ball of half the radius, 6 centimetres, how many times bigger will the two-bends number be?”  
   Say: “On the basketball, radius 12 centimetres, both bends have a radius of 12 centimetres, and the readout gives about 69 per square metre. Make a guess. If I swap the basketball for a ball of half the radius, 6 centimetres, how many times bigger will the two-bends number be?”  
   Describe: On a basketball of radius 12 centimetres the two-bends number is about 69 per square metre.
4. `reveal-half-the-ball` (entry, await none) state: preset="basketball", radius-1=6  
   *Ball radius 6 cm; product readout 277.78 per square metre.*  
   Say: “With the radius halved, the readout jumps to about 278 per square metre, four times bigger, not twice. The reason is that both bends got twice as sharp, and the rule multiplies them: 2 times 2 is 4.”  
   Describe: On a ball of radius 6 centimetres the two-bends number is about 278 per square metre, four times the basketball's.
5. `can-gives-zero` (entry, await none) state: preset="ring-on-can", progress=1  
   *Can with the completed purple ring; largest-bend readout shows no bend, smallest-bend radius −3.3 cm, product 0, ring shortfall 0.*  
   Say: “On the drinks can, the bend across the can has a best-fit radius of 3.3 centimetres. But along the can there is no bend at all: the best-fit circle would be endlessly big, so that readout shows no bend. Dividing 1 by an endlessly big number gives zero, so the product readout is zero. The purple ring agrees: it comes out exactly as on flat paper. The can is bent, yet its Gaussian curvature is zero, because one direction with no bend is enough to make the product zero.”  
   Describe: On the can one principal bend has radius 3.3 centimetres and the other is no bend at all, so the product, the Gaussian curvature, is zero. The paced ring comes out exactly as on flat paper.
6. `predict-the-waist` (entry, await prediction) state: preset="soap-film-waist"; evidences `gaussian-curvature/checks/soap-film-waist`  
   *Soap-film waist patch; green arrow up toward the film's middle line; ruler along the tick with the surface 1 cm above the card.*  
   Predict: “Around the waist the film bends toward the hoops' centre line with radius 2 centimetres, and from hoop to hoop it bends away with radius 2 centimetres. Do the two bends cancel, so the two-bends number is zero?”  
   Say: “Here the card touches the waist of a soap film stretched between two wire hoops. The green arrow points inward, toward the line running through the centres of the two hoops. Along the red ruler, around the waist, the pale blue film bends toward the arrow with a radius of 2 centimetres. A quarter turn on, from hoop to hoop, it bends away from the arrow, also with a radius of 2 centimetres. Make a guess. Do the two bends cancel, so the two-bends number is zero?”  
   Describe: The card touches a soap film's waist between two wire hoops. Around the waist the film bends toward the hoops' centre line with radius 2 centimetres, and from hoop to hoop it bends away with radius 2 centimetres.
7. `reveal-the-waist` (entry, await none) state: preset="ring-on-waist", progress=1  
   *Product readout −2500 per square metre; completed purple ring at 0.5 cm with shortfall −1.007 percent.*  
   Say: “The readout gives minus 2500 per square metre, not zero. Bends toward opposite sides do not cancel; they multiply to a number with a minus sign. Here 2 times 2 is 4, and 1 divided by 4 is a quarter per square centimetre, 2500 per square metre, with the minus sign. The purple ring agrees: paced half a centimetre out, it comes out 1 percent longer than on flat paper, as rings do on a saddle.”  
   Describe: The two-bends number is minus 2500 per square metre, a quarter per square centimetre with a minus sign. The paced ring comes out 1 percent longer than on flat paper, as on a saddle.

### `ring-agrees-with-the-product` · for [[gaussian-curvature]] · working

1. `basketball-both-numbers` (working, await none) state: preset="ring-on-basketball", progress=1  
   *Basketball with the completed purple ring at 2 cm; product 69.44 per square metre; ring shortfall 0.4548 percent; ring curvature 68.22 per square metre.*  
   Say: “On the basketball both principal curvatures are one over 12 centimetres, so their product is one over 0.12 metres squared, 69.4 per square metre. The purple ring paced 2 centimetres out comes back 0.455 percent short. Six times that fraction over the radius squared gives 68.2 per square metre, within 2 percent of the product. One caution: the patch under the card is the ball's best-fit paraboloid, not the sphere itself. On the true sphere the ring would come out 0.462 percent short, a little more, because the paraboloid flattens away from the touching point while the sphere does not.”  
   Describe: The product of the principal curvatures on the basketball is 69.4 per square metre. A ring paced 2 centimetres out is 0.455 percent short, which gives 68.2 per square metre. The patch is the ball's best-fit paraboloid; on the true sphere the shortfall would be 0.462 percent.
2. `smaller-ring-closer` (working, await none) state: preset="ring-on-basketball", probe-distance=0.5, progress=1  
   *Ring at 0.5 cm; shortfall 0.0289 percent; ring curvature 69.38 per square metre.*  
   Say: “With a ring only half a centimetre out, the shortfall is 0.029 percent and the ring curvature is 69.38 per square metre, within a tenth of a percent of the product. The shortfall is K times the radius squared over 6 to leading order, and the leftover terms shrink with the radius to the fourth power.”  
   Describe: A ring half a centimetre out is 0.029 percent short, giving 69.38 per square metre, within a tenth of a percent of the product 69.4.
3. `predict-scale-up` (working, await prediction) state: preset="ring-on-basketball", progress=1; evidences `gaussian-curvature/checks/scale-a-surface-up`  
   *Same view, paused.*  
   Predict: “If every length of the surface is multiplied by 3, so the ball's radius becomes 36 centimetres, what happens to the product of the two bends?”  
   Say: “Predict before I change the ball. If every length is multiplied by 3, so the radius becomes 36 centimetres, what happens to the product of the two bends?”  
   Describe: The basketball waits at radius 12 centimetres, with the product at 69.4 per square metre.
4. `reveal-scale-up` (working, await none) state: preset="ring-on-basketball", radius-1=36, progress=1  
   *Ball radius 36 cm; product 7.72 per square metre; ring curvature 7.70 per square metre.*  
   Say: “The product drops to 7.72 per square metre, one ninth of before, not one third. Each principal curvature is divided by 3, and their product by 9: the Gaussian curvature has units of one over length squared. The ring readout, 7.70, follows it down.”  
   Describe: With the radius tripled to 36 centimetres, the product is 7.72 per square metre, one ninth of its value, and the ring gives 7.70.
5. `bent-can-reads-zero` (working, await none) state: preset="ring-on-can", progress=1; evidences `second-fundamental-form/checks/rolled-sheet-claim`  
   *Can with the completed ring; smallest signed bend radius −3.3 cm, largest shows no bend; product 0; ring shortfall 0.*  
   Say: “On the can the second fundamental form is not zero: across the can the bend has radius 3.3 centimetres, away from the arrow. But along the can the bend is zero, so the product is zero and the purple ring comes out as on flat paper. Bending without stretching changes the second fundamental form and leaves the Gaussian curvature alone.”  
   Describe: On the can one principal curvature is minus one over 3.3 centimetres and the other zero. The product is zero, and the paced ring shows no shortfall.

## Design rules

- **Show the gap as a bar that grows as the tip slides out, and label the readout as a best-fit radius, never as the gap itself; the entry tour slides the tip inward to show a vanishing gap with an unchanged bend.** Because: Learners read a zero gap at the touching point as no bending there; the bend is the rate at which the gap grows. Prevents `second-fundamental-form/misconceptions/gap-zero-so-no-bending`.
- **Keep the ruler draggable in every state, and start the can preset with the ruler across the can so that turning it along the can is the first thing to try.** Because: A fixed ruler suggests one bend per point; turning it is what shows that the bend depends on direction. Prevents `second-fundamental-form/misconceptions/same-bending-every-direction`.
- **Draw the principal marks at their true angle on the card and on the sweep plot, including the turned crisp and custom patches, and never snap them to the card's edges.** Because: Seeing the marks move with the surface while staying a quarter turn apart is the evidence that the extremes are always perpendicular. Prevents `principal-curvatures/misconceptions/extremes-at-any-angle`.
- **Draw the orange gap bar above the card when the surface goes toward the green arrow and below it otherwise, and give every bend readout a signed sense with the arrow named.** Because: On the saddle the two principal bends go to opposite sides; the sign has to be visible, not only in the number. Prevents `principal-curvatures/misconceptions/bends-to-one-side`.
- **Show the product of the two bends and the paced ring's curvature side by side on the same patch at the same distance, on every preset including the waist.** Because: Opposite bends multiply to a negative number and the ring comes out too long; seeing both prevents the belief that they cancel. Prevents `gaussian-curvature/misconceptions/equal-opposite-bends-cancel`.
- **On the can, keep the nonzero bend radius across the can visible beside the zero product and the zero ring shortfall.** Because: Learners who know the can is flat for an ant conclude that its second fundamental form is zero; the readouts show that only the product is. Prevents `second-fundamental-form/misconceptions/tube-has-no-bending`.
- **Make the arrow flip one click away, and animate the readouts changing sign while the product readout stays still.** Because: The sign of every bend depends on the chosen normal and the Gaussian curvature does not; the flip makes both facts visible.
- **Distinguish the ruler, the principal marks and the ring by line style (solid, dashed, dotted) as well as by colour.** Because: Colour alone fails for colour-blind learners and in print.

## Model

The surface is the quadratic patch $z = \tfrac12(K_{xx}x^2 + 2K_{xy}xy + K_{yy}y^2)$ in Cartesian coordinates on the card, with $z$ measured along the chosen normal and lengths in centimetres; each preset fills the three coefficients from its radii, and flipping the normal negates all three. The gap, the normal curvature along the ruler, the principal curvatures and directions, and the Gaussian curvature follow in closed form from the coefficients. Radii are reported signed, as $1/\kappa$, with a zero bend shown as no bend. The paced ring is computed on the same graph surface by integrating unit-speed geodesics from the touching point, so its shortfall carries the higher-order terms of a real ring and agrees with the product only to leading order in the ring's radius.

**Height over the card**

$$
z = \tfrac12\left(K_{xx}x^2 + 2K_{xy}\,xy + K_{yy}\,y^2\right)
$$

Holds when: Cartesian coordinates $(x, y)$ on the tangent plane with origin at the touching point, $x$ along the reference tick, $z$ along the chosen normal $\hat{\mathbf n}$; $K_{ij} = \hat{\mathbf n}\cdot\partial_i\partial_j\mathbf X$, positive where the surface bends toward $\hat{\mathbf n}$. Presets: ball $K_{xx} = K_{yy} = -1/r_1$; can $K_{xx} = -1/r_1$, $K_{yy} = 0$; bowl $K_{xx} = 1/r_1$, $K_{yy} = 1/r_2$; egg $K_{xx} = -1/r_1$, $K_{yy} = -1/r_2$; saddle $K_{xx} = 1/r_1$, $K_{yy} = -1/r_1$; crisp $K_{xy} = 1/r_1$; all with $K_{xy} = 0$ unless stated and with the normal up. The normal down negates every coefficient.

**Gap at the probe distance**

$$
h(d, \phi) = \tfrac12\,\kappa_n(\phi)\,d^2,\qquad \kappa_n(\phi) = K_{xx}\cos^2\phi + 2K_{xy}\cos\phi\sin\phi + K_{yy}\sin^2\phi
$$

Holds when: $\phi$ is the ruler angle from the tick, counterclockwise seen from above the card. The frame $(x, y)$ is fixed to the card and does not flip with $\hat{\mathbf n}$, so flipping the normal negates all three coefficients and leaves $\phi$ alone (with a right-handed frame that flipped with $\hat{\mathbf n}$, $K_{xy}$ would keep its sign instead). The reported radius along the ruler is $1/\kappa_n$, signed; no bend when $\kappa_n = 0$.

**Principal curvatures and directions**

$$
\kappa_{1,2} = H \pm \sqrt{\tfrac14(K_{xx} - K_{yy})^2 + K_{xy}^2},\qquad H = \tfrac12(K_{xx} + K_{yy}),\qquad \tan 2\psi_1 = \frac{2K_{xy}}{K_{xx} - K_{yy}}
$$

Holds when: Orthonormal coordinates on the card, so these are the eigenvalues and eigenvectors of the shape operator. $\psi_1$ is the direction of $\kappa_1 \ge \kappa_2$, measured like $\phi$ (counterclockwise seen from above the card), computed as $\tfrac12\operatorname{atan2}(2K_{xy}, K_{xx} - K_{yy})$ and reported on the branch $(-90^\circ, 90^\circ]$; at an umbilic point ($\kappa_1 = \kappa_2$) the readout reports $0$. Flipping the normal negates $\kappa_1$ and $\kappa_2$ and swaps which direction is called $\psi_1$.

**Euler's formula**

$$
\kappa_n(\phi) = \kappa_1\cos^2(\phi - \psi_1) + \kappa_2\sin^2(\phi - \psi_1)
$$

Holds when: Same sign convention; this is what the sweep plot traces, with the probe distance fixed.

**Product of the two bends**

$$
K = \kappa_1\kappa_2 = K_{xx}K_{yy} - K_{xy}^2
$$

Holds when: Unchanged by flipping the normal. Computed in inverse square centimetres and reported in inverse square metres, a factor ten thousand.

**Paced ring shortfall**

$$
L(\rho) = 2\pi\rho\left(1 - \frac{K\rho^2}{6} + O(\rho^4)\right),\qquad K_{\rm ring} = \frac{6}{\rho^2}\,\frac{2\pi\rho - L(\rho)}{2\pi\rho}
$$

Holds when: $L$ is the length along the surface of the geodesic circle of radius $\rho$ = probe distance about the touching point, computed on the quadratic graph itself. $K_{\rm ring}$ tends to $K$ as $\rho \to 0$; at finite $\rho$ it differs by terms of relative order $\rho^2\kappa^2$, which the tests record.

**Method:** Closed-form readouts from the three coefficients. For the ring, unit-speed geodesics of the graph $z = f(x, y)$ obey $\ddot x = -f_x\,Q/(1 + f_x^2 + f_y^2)$ and $\ddot y = -f_y\,Q/(1 + f_x^2 + f_y^2)$ with $Q = f_{xx}\dot x^2 + 2f_{xy}\dot x\dot y + f_{yy}\dot y^2$; they are integrated from the touching point in $N$ equally spaced directions to arc length $\rho$ by fourth-order Runge–Kutta, and the ring length is the sum of the chords between neighbouring endpoints. The reference values below used $N = 5760$ and 300 steps, and the polygon underestimates the length by a relative $\pi^2/(6N^2) \approx 5\times10^{-8}$, well inside the tolerances. Build notes: add $+0$ before the atan2 (or map $-90^\circ$ to $90^\circ$) so that a negative zero in $2K_{xy}$ cannot report $-90^\circ$ on the can; round every signed value before choosing its speech template, so that a value that rounds to zero (including the negative zero of $K_{xx}K_{yy}$ with one factor zero) uses the positive template; and a radius readout whose bend rounds to zero displays and speaks "no bend" instead of a number, since its value is undefined.

| Test | State | Expect | Hidden | Note |
| --- | --- | --- | --- | --- |
| `basketball-gap` | preset="basketball" | height = -0.1666667 ±1e-06; radius-along-ruler = -12 ±1e-06; radius-1 = -12 ±1e-06; radius-2 = -12 ±1e-06; principal-angle = 0 ±1e-06; gaussian-curvature = 69.4444444 ±0.0001 | ring-length, ring-missing-fraction, ring-curvature | Gap $d^2/2a$ = 0.167 cm at 2 cm on a 12 cm ball, away from the upward normal; umbilic, so the direction readout is 0; $K = 1/(0.12\ \mathrm{m})^2$. |
| `basketball-double-distance` | preset="basketball", probe-distance=4 | height = -0.6666667 ±1e-06 | — | Twice the distance, four times the gap. |
| `basketball-half-centimetre` | preset="basketball", probe-distance=0.5 | height = -0.0104167 ±1e-06; radius-along-ruler = -12 ±1e-06 | — | Small-distance limit: the gap shrinks with $d^2$ while the bend readout does not change. |
| `basketball-flipped` | preset="basketball-flipped" | height = 0.1666667 ±1e-06; radius-along-ruler = 12 ±1e-06; radius-1 = 12 ±1e-06; gaussian-curvature = 69.4444444 ±0.0001 | — | Reversing the normal negates every signed readout and leaves the product unchanged. |
| `ball-half-radius` | preset="basketball", radius-1=6 | gaussian-curvature = 277.7777778 ±0.0001 | — | Half the radius, four times the product. |
| `marble-and-football` | preset="basketball", radius-1=1 | gaussian-curvature = 10000 ±0.001 | — | A 1 cm marble: 121 times a 11 cm football's 82.64 per square metre. |
| `ball-triple-radius` | preset="basketball", radius-1=36 | gaussian-curvature = 7.7160494 ±0.0001 | — | Every length times 3 divides $K$ by 9. |
| `can-across` | preset="can-lying-on-its-side" | height = -0.6060606 ±1e-06; radius-along-ruler = -3.3 ±1e-06; radius-2 = -3.3 ±1e-06; principal-angle = 90 ±1e-06; gaussian-curvature = 0 ±1e-09 | — | Across the can the bend is $-1/3.3$ per cm; the largest signed bend is the zero bend along the can, so radius-1 shows no bend and the direction readout is 90, the branch's upper bound (never −90). |
| `can-along` | preset="can-lying-on-its-side", ruler-angle=90 | height = 0 ±1e-09; gaussian-curvature = 0 ±1e-09 | — | Along the can the gap stays zero; radius-along-ruler shows no bend. |
| `can-diagonal` | preset="can-lying-on-its-side", ruler-angle=45 | height = -0.3030303 ±1e-06; radius-along-ruler = -6.6 ±1e-06 | — | Euler's formula at 45 degrees: half the bend across, twice the radius. |
| `bowl-along-the-tick` | preset="spoon-bowl" | height = 0.4 ±1e-06; radius-along-ruler = 5 ±1e-06; radius-1 = 2 ±1e-06; radius-2 = 5 ±1e-06; principal-angle = 90 ±1e-06; gaussian-curvature = 1000 ±0.0001 | — | $z = x^2/10 + y^2/4$ in cm: principal curvatures 0.5 (across, at 90 degrees) and 0.2 per cm, both toward the normal; $K = 0.1$ per square cm. |
| `bowl-sixty-degrees` | preset="spoon-bowl", ruler-angle=60 | height = 0.85 ±1e-06; radius-along-ruler = 2.3529412 ±1e-06 | — | Euler's formula: $0.2\cos^2 60^\circ + 0.5\sin^2 60^\circ = 0.425$ per cm, radius 2.353 cm; the spoon-bowl check. |
| `bowl-flipped-sixty-degrees` | preset="spoon-bowl-sweep", normal="down" | height = -0.85 ±1e-06; radius-along-ruler = -2.3529412 ±1e-06; radius-1 = -5 ±1e-06; radius-2 = -2 ±1e-06; principal-angle = 0 ±1e-06; gaussian-curvature = 1000 ±0.0001 | — | With the normal down the largest signed bend is $-0.2$ per cm along the tick, so the direction readout moves from 90 to 0 and the product is unchanged. |
| `egg-around` | preset="egg-widest-part" | height = -0.25 ±1e-06; radius-along-ruler = -2 ±1e-06; radius-1 = -4.5 ±1e-06; radius-2 = -2 ±1e-06; principal-angle = 90 ±1e-06; gaussian-curvature = 1111.1111111 ±0.0001 | — | Radii 2 cm around and 4.5 cm along, both away from the upward normal; the largest signed bend is the gentler one along the egg; $K = 1/9$ per square cm. |
| `egg-along` | preset="egg-widest-part", ruler-angle=90 | height = -0.1111111 ±1e-06; radius-along-ruler = -4.5 ±1e-06 | — | The gentlest bend, a quarter turn from the sharpest. |
| `egg-diagonal` | preset="egg-widest-part", ruler-angle=45 | height = -0.1805556 ±1e-06; radius-along-ruler = -2.7692308 ±1e-06 | — | Euler's formula between the two extremes. |
| `egg-flipped` | preset="egg-widest-part", normal="down" | height = 0.25 ±1e-06; radius-1 = 2 ±1e-06; radius-2 = 4.5 ±1e-06; principal-angle = 0 ±1e-06; gaussian-curvature = 1111.1111111 ±0.0001 | — | Flipping the normal swaps which bend is called largest, so the direction readout moves from 90 to 0. |
| `saddle-along-the-horse` | preset="saddle" | height = 0.3333333 ±1e-06; radius-along-ruler = 6 ±1e-06; radius-1 = 6 ±1e-06; radius-2 = -6 ±1e-06; principal-angle = 0 ±1e-06; gaussian-curvature = -277.7777778 ±0.0001 | — | Valley along the tick, hill across it; $K = -1/36$ per square cm. |
| `saddle-across-the-horse` | preset="saddle", ruler-angle=90 | height = -0.3333333 ±1e-06; radius-along-ruler = -6 ±1e-06 | — | The opposite sign a quarter turn on. |
| `saddle-diagonal` | preset="saddle", ruler-angle=45 | height = 0 ±1e-09 | — | The saddle's straight directions at 45 degrees; radius-along-ruler shows no bend. |
| `crisp-along-the-edge` | preset="crisp-turned" | height = 0 ±1e-09; radius-1 = 6 ±1e-06; radius-2 = -6 ±1e-06; principal-angle = 45 ±1e-06; gaussian-curvature = -277.7777778 ±0.0001 | — | $z = xy/6$: no bend along the tick, principal directions at plus and minus 45 degrees, the same product as the saddle. |
| `crisp-diagonal` | preset="crisp-turned", ruler-angle=45 | height = 0.3333333 ±1e-06; radius-along-ruler = 6 ±1e-06 | — | Along the turned valley. |
| `crisp-other-diagonal` | preset="crisp-turned", ruler-angle=135 | height = -0.3333333 ±1e-06 | — | Along the turned hill. |
| `crisp-flipped` | preset="crisp-turned", normal="down", ruler-angle=45 | height = -0.3333333 ±1e-06; principal-angle = -45 ±1e-06 | — | Negative branch of the direction readout: with the normal down the largest signed bend is the other diagonal, 45 degrees clockwise. |
| `flat-sheet` | preset="flat-sheet" | height = 0 ±1e-09; principal-angle = 0 ±1e-09; gaussian-curvature = 0 ±1e-09 | — | Flat case: no gap in any direction, every radius readout shows no bend, product zero. |
| `soap-film-waist-around` | preset="soap-film-waist" | height = 1 ±1e-06; radius-1 = 2 ±1e-06; radius-2 = -2 ±1e-06; principal-angle = 0 ±1e-06; gaussian-curvature = -2500 ±0.0001 | — | Equal bends toward opposite sides: $K = -(1/2)^2 = -0.25$ per square cm, not zero. |
| `soap-film-waist-along` | preset="soap-film-waist", ruler-angle=90 | height = -1 ±1e-06 | — | From ring to ring the film bends away from the arrow. |
| `tilted-custom-patch` | preset="tilted-custom-patch" | height = 0.6 ±1e-06; radius-along-ruler = 3.3333333 ±1e-06; radius-1 = 2.9289322 ±1e-06; radius-2 = 17.0710678 ±1e-06; principal-angle = -22.5 ±1e-06; gaussian-curvature = 200 ±0.0001 | — | $K_{xx} = 0.3$, $K_{xy} = -0.1$, $K_{yy} = 0.1$: eigenvalues $0.2 \pm 0.1\sqrt2$, the largest 22.5 degrees clockwise from the tick, product $0.02$ per square cm. |
| `ring-on-basketball-complete` | preset="ring-on-basketball", progress=1 | ring-length = 12.5092 ±0.001; ring-missing-fraction = 0.4548 ±0.002; ring-curvature = 68.22 ±0.3; gaussian-curvature = 69.4444444 ±0.0001 | — | Geodesic ring of radius 2 cm on the paraboloid $z = -r^2/24$: 1.8 percent below the leading-order $K\rho^2/6 = 0.463$ percent because of the $\rho^4$ terms. |
| `ring-hidden-while-pacing` | preset="ring-on-basketball", progress=0.5 | — | ring-length, ring-missing-fraction, ring-curvature | The ring readouts appear only when the ring closes. |
| `ring-small-leading-order` | preset="ring-on-basketball", probe-distance=0.5, progress=1 | ring-missing-fraction = 0.02891 ±0.0002; ring-curvature = 69.4444444 (rel 0.005) | — | Small-ring limit: the ring curvature (69.38 computed) matches $K$ to a tenth of a percent. |
| `ring-on-egg-complete` | preset="ring-on-egg", progress=1 | ring-missing-fraction = 0.4524 ±0.002; ring-curvature = 1085.65 ±5; gaussian-curvature = 1111.1111111 ±0.0001 | — | Ring of radius 0.5 cm on the egg patch: 2.3 percent below the product, as the entry tour says. |
| `ring-on-saddle-complete` | preset="ring-on-saddle", progress=1 | ring-missing-fraction = -0.456 ±0.002; ring-curvature = -273.62 ±1.5 | — | Negative branch: the ring comes out too long; leading order $-1/36 \times 1/6 = -0.463$ percent. |
| `ring-on-can-complete` | preset="ring-on-can", progress=1 | ring-missing-fraction = 0 ±0.0001; ring-curvature = 0 ±0.05; gaussian-curvature = 0 ±1e-09 | — | The can is a bent flat sheet: the ring is exactly flat to numerical precision. |
| `ring-on-waist-complete` | preset="ring-on-waist", progress=1 | ring-missing-fraction = -1.0075 ±0.003; ring-curvature = -2417.9 ±8; gaussian-curvature = -2500 ±0.0001 | — | Opposite bends of radius 2 cm: the ring 0.5 cm out is 1 percent too long, 3 percent below the leading order in size. |
| `ring-on-flat-sheet-complete` | preset="ring-on-flat-sheet", progress=1 | ring-length = 12.5663706 ±0.0001; ring-missing-fraction = 0 ±0.0001 | — | Flat case: $2\pi \times 2$ cm. |
| `ring-on-tripled-ball` | preset="ring-on-basketball", radius-1=36, progress=1 | ring-curvature = 7.7 ±0.05; gaussian-curvature = 7.7160494 ±0.0001 | — | Scaling every length by 3 divides both numbers by 9. |

## Serves

- [[second-fundamental-form]]: the gap bar at the ruler's tip, its growth with the distance squared, the can's zero gap along its length, and the sweep plot of the gap for every direction
- [[principal-curvatures]]: the turning ruler, the sweep plot's highest and lowest points, the dashed principal marks a quarter turn apart, the saddle's opposite signs, and Euler's formula in the spoon bowl
- [[gaussian-curvature]]: the product-of-bends readout beside the paced ring's shortfall on the same patch, the can's zero, the waist's negative product, and the scaling of both numbers with size

## In the visual network

- **Builds on:** [[best-fit-circle-along-a-bend]]
- **Leads to:** [[bend-arrow-split-on-a-surface]], [[plumb-lines-along-a-walk]], [[paced-ring-on-a-ball-and-a-plain]], [[lines-of-curvature-on-an-ellipsoid]]

## Accessibility

Every tour beat describes the gap in centimetres and which side of the card the surface goes to, and every bend readout is announced as a best-fit radius toward or away from the green arrow. The ruler, the principal marks and the ring differ in line style as well as colour, and every control works from the keyboard.

Static alternative: A flat card touches a curved surface at one point. A ruler laid along the card leaves a gap at its tip that grows with the distance squared and changes with the ruler's direction: on a drinks can it is largest across the can and zero along it. The sharpest and gentlest bends are a quarter turn apart, and their product matches the shortfall of a small ring paced out on the surface.

- `Left and Right arrows`: turn the ruler by 5 degrees
- `Up and Down arrows`: slide the ruler's tip out or in by half a centimetre
- `1 to 7`: choose ball, can, spoon bowl, egg, saddle, crisp, or custom patch
- `N`: flip the green arrow
- `S`: toggle the sweep plot
- `P`: toggle the principal marks
- `R`: toggle the ring test
- `Space`: pace the ring, or pause

## Starting material

Earlier course assets: `scene-3d-manifold-surface-charts`

The earlier course's surface-and-tangent-plane scene supplies the mesh, the tangent-plane card and the camera. New work: the quadratic patch presets, the turning ruler with its gap bar, the sweep plot, the principal marks, the normal flip, and the paced geodesic ring with its on-complete readouts.

## Review: novice

**Verdict:** fixed (2026-09-16, revision 3)

**Retell attempt:** A flat card touching a ball only touches at one spot, and a ruler laid along the card has a gap under its far end. Twice as far out, the gap is four times bigger, because it grows like the distance times itself. So the bend is how fast the gap grows, not the gap itself, and the ball is bending even at the touching spot. On a can lying down, the gap is there across the can but zero along it, so one spot can bend by different amounts in different directions; the rule for the gap in every direction is the second fundamental form. On an egg the biggest gap is around the egg and the smallest along it, and those two directions are a quarter turn apart; they are the principal curvatures. On a saddle one direction bends up and the other down, so one is positive and one negative. For the last number you multiply the two radii, 2 times 4 and a half is 9, and take 1 over that, and somehow that is about 1111 on the readout; an ant pacing a ring gets nearly the same. A can gives zero, and a soap film's waist gives a minus number because the bends go to opposite sides. I am not sure what the green arrow was for until the saddle, what the tick is, or why 1 over 9 becomes 1111.

- Stumble: “Here is a basketball, drawn in pale blue, with a flat see-through card resting on top.”: The green arrow is on screen from the first beat and every readout speaks of the green arrow's side, but no entry say line names the arrow until the saddle beat, four beats into the second tour.
- Stumble: “The orange curve on the plot shows the gap at 2 centimetres for every direction the ruler can point.”: The plot's left-to-right axis is never named, so I could not tell what the curve's high and low points sit above; I had to reread against the show line.
- Stumble: “This rule, the gap for every direction at one point, is called the second fundamental form.”: The previous beat had just insisted the bend is not the gap, so calling the form a rule for the gap made me reread; the note defines it as the bend in every direction.
- Stumble: “Now the card cuts through the middle of a saddle, where the seat is level.”: A card cannot cut a saddle; I pictured the card slicing the seat rather than touching it with the seat passing through the see-through card.
- Stumble: “The green arrow on the card points up.”: First mention of the arrow in a say line, with no word on what it is for, one sentence before its side is used to define positive.
- Stumble: “At a saddle point one principal curvature is positive and the other negative”: Saddle point is a new term; the glossary only has saddle-shaped.
- Stumble: “Along the red ruler, along the card's edge, the gap is zero.”: A surprise with no reason: the crisp is bent both ways yet the ruler finds no gap; and along the card's edge is the first hint of the tick that the readouts and option labels call the reference tick.
- Stumble: “one bending up and one bending down”: Reads as if the dashed marks bend; the marks are directions in which the crisp bends.
- Stumble: “Around the egg, the best-fit circle has a radius of 2 centimetres.”: Best-fit circle appears without its meaning; it is in the glossary but had not been said in any beat.
- Stumble: “The readout shows that number per square metre, about 1111.”: A step on trust: nothing says how one ninth per square centimetre becomes 1111 per square metre.
- Stumble: “Turned into the ant's number, the ring gives about 1086 per square metre”: The ant's number is never tied to the Gaussian curvature or the matching ball that the entry way taught.
- Stumble: “But along the can there is no bend at all, so that readout shows no bend, and the product is zero.”: The entry rule multiplies radii and divides 1 by the result, and a direction with no bend has no radius to multiply; the jump to a zero product was taken on trust.
- Stumble: “because one unbent direction is enough.”: Enough for what is left unsaid, and its number does not say which number.
- Stumble: “a soap film stretched between two rings ... from ring to ring”: Ring is used in two senses in the same tour: the wire rings holding the film and the paced ring of the ring test.
- Stumble: “The green arrow points toward the film's middle line.”: Middle line is undefined; I could not place the arrow's direction.
- Stumble: “The readout gives minus 2500 per square metre, not zero.”: The number 2500 arrives without the count that the egg beat modelled, so I could not check it against the two radii of 2 centimetres.
- Stumble: “the largest signed bend lies {abs} degrees counterclockwise from the reference tick”: The reference tick is never named in a spoken beat; the picture calls it a red tick on the card's edge.
- Stumble: “Drinks can on its side (tick points across the can)”: Option labels say tick without saying which mark on screen it is.
- Fixed: Named the green arrow in the first beat and gave it its role in the saddle beat.
- Fixed: Named the sweep plot's left-to-right axis as the ruler's direction and tied the second fundamental form to the bend in every direction, with the gap at a fixed distance as what shows it.
- Fixed: Replaced cuts through with touches, and saddle point with saddle-shaped point.
- Fixed: Reordered the crisp beat so the marks are introduced before the zero gap, named the red tick on the card's edge, and gave the reason for the zero gap along the ruler.
- Fixed: Glossed the best-fit circle at its first spoken use, added the 10,000 square centimetres step behind 1111 per square metre, and named the Gaussian curvature once at the end of the egg beat.
- Fixed: Tied the ant's number to the Gaussian curvature from her matching ball.
- Fixed: Explained the can's zero product through the entry rule of dividing 1 by an endlessly big radius.
- Fixed: Renamed the soap film's wire rings as hoops, replaced the film's middle line with the line through the hoops' centres, and added the 2 times 2 count behind 2500 per square metre.
- Fixed: Renamed the reference tick as the red tick on the card's edge in the principal-angle readout speech and the surface option labels.
- Fixed: No number, sign, state or claim was changed; the describe and predict fields were updated to match.
- Concern: The product-of-the-bends readout speech has no zero form: on the can it would say the two bends multiplied give 0 per square metre, both bends going to the same side of the card, which is wrong when one bend is zero. The gap readout likewise says 0 centimetres from the card, on the green arrow's side. The schema has only say and say_negative; a zero form or a sense-free wording at zero is needed.
- Concern: The entry tour multiply-the-two-bends now names the Gaussian curvature once, in the egg beat; if that naming is judged a content change it can be moved to a beat of its own.
- Concern: Working tour ring-agrees-with-the-product calls the surface the basketball, but the ring is paced on the quadratic patch: a student recomputing on a true sphere of radius 12 centimetres gets a shortfall of about 0.462 percent at 2 centimetres, not 0.455. A spoken aside that the patch is the ball's best-fit paraboloid, or a sphere-surface ring, would prevent the mismatch.
- Concern: The first tour's turn-along-the-can beat says a quarter turn seen from above without a clockwise or counterclockwise word; the target direction along the can makes it unambiguous, so it was left, but the animate value of 90 degrees implies counterclockwise seen from the arrow's side.

**Re-read** (2026-09-16, revision 3)

- Stumble: “the two bends multiplied give {abs} per square metre, and neither bend goes to the side opposite the other”: A double negative in a spoken line: a listener has to unpack "neither ... opposite the other" while watching the card. The reviewer wrote it to cover the case where one bend is zero, which the old "both bends going to the same side" got wrong.
- Fixed: Reworded the product readout as above: still true when one bend is zero (a flat direction goes to no side, so not to the opposite one), and one clause shorter to hear.
- Fixed: Read the other eight changed strings: "seen from above the card" is clearer than the old "seen from the side the green arrow points to", and the height readout's "toward the green arrow" and "away from the green arrow" are plain. No other stumble.
- Fixed: Editor sign-off, not an agent: the run that would have done this stopped at the monthly spend limit.

## Review: physics

**Verdict:** fixed (2026-09-16, revision 3)

- Verified: patch-height: $K_{ij} = \hat{\mathbf n}\cdot\partial_i\partial_j\mathbf X$ positive toward the normal, ball with the normal away from it $K_{xx} = K_{yy} = -1/r$: Compared with the course extrinsic-curvature row (sphere with outward normal has $K_{\mu\nu} = -h_{\mu\nu}/r$) and expanded $z = -(r - \sqrt{r^2 - x^2 - y^2})$ to second order → Sign and factor $\tfrac12$ agree with the conventions; the preset coefficients for can, bowl, egg, saddle and crisp follow
- Verified: gap-along-the-ruler: $h = \tfrac12\kappa_n d^2$ with $\kappa_n = K_{ij}t^it^j$: Substituted $x = d\cos\phi$, $y = d\sin\phi$ into the patch → Exact on the quadratic patch; on a true sphere of radius 12 cm the gap at 2 cm is 0.1678 cm against the patch's 0.1667, so the entry rounding to just under 2 millimetres holds for both
- Verified: principal-curvatures-and-directions: eigenvalues $H \pm \sqrt{\tfrac14(K_{xx}-K_{yy})^2 + K_{xy}^2}$ and $\tan 2\psi_1 = 2K_{xy}/(K_{xx}-K_{yy})$: Eigen-decomposition of the symmetric 2 by 2 matrix in an orthonormal frame; checked on the tilted custom patch (0.3, -0.1, 0.1) → $\kappa_{1,2} = 0.2 \pm 0.1\sqrt2$, $\psi_1 = -22.5^\circ$, as the test states
- Verified: euler-formula reproduces $\kappa_n(\phi)$: Bowl at 60 degrees: $0.2\cos^2 60^\circ + 0.5\sin^2 60^\circ$ → 0.425 per cm, radius 2.3529 cm, gap 0.85 cm
- Verified: gaussian-curvature: $K = \kappa_1\kappa_2 = K_{xx}K_{yy} - K_{xy}^2$, unchanged by the flip, reported times ten thousand: Determinant of the coefficient matrix; every flipped test recomputed → All flipped products equal the unflipped ones; units check: per square centimetre times $10^4$ is per square metre
- Verified: ring-shortfall: geodesic equations of the graph and the leading term $K\rho^2/6$: Re-derived the geodesic equations from $\ddot{\mathbf X} \parallel \hat{\mathbf n}$ ($\lambda = Q/(1 + f_x^2 + f_y^2)$) and re-integrated every ring test with an independent RK4 (1440 directions, 300 steps, polygon correction $\pi^2/6N^2$) → Basketball 2 cm: length 12.5092, shortfall 0.4548 percent, ring curvature 68.22; 0.5 cm: 0.02890 percent, 69.37; egg 0.4524 percent, 1085.64; saddle -0.4560 percent, -273.62; can $9\times10^{-6}$ percent; waist -1.0075 percent, -2417.9; flat 12.56637 cm; tripled ball 7.70; all within the stated tolerances
- Verified: Sphere versus paraboloid: the working tour's 0.455 percent is the patch's number: Geodesic circle on a sphere of radius 12 cm at 2 cm: $1 - 6\sin(1/6)$ → 0.4623 percent on the sphere against 0.4548 on the paraboloid; a caution was added to the beat so a learner recomputing on the sphere is not misled
- Verified: Every closed-form test expectation (basketball, flipped, half and triple radius, marble, can at 0, 45, 90, bowl at 0, 60 and flipped, egg at 0, 45, 90 and flipped, saddle at 0, 45, 90, crisp at 0, 45, 135 and flipped, flat sheet, waist at 0 and 90, tilted custom patch): Independent python implementation of the model from the state alone → Every value agrees to better than $10^{-9}$; every hidden-readout expectation matches visible_when and the ring-test and progress state
- Verified: Angle convention: the tests take the frame fixed to the card, so the crisp flipped with the ruler at 45 degrees reads a gap of -0.333 cm and a principal direction of -45 degrees: Worked the flip both ways: a right-handed frame that flips with the normal keeps $K_{xy}$ and would give +0.333 cm and +45 degrees there → The tests and the model's negate-all-three rule were consistent with a fixed frame, but the ruler-angle and principal-angle sense texts said seen from the green arrow's side, which is the other convention; the texts were changed to seen from above the card and the flip no longer claims to reverse the ruler-angle sense
- Verified: Spoken numbers in every beat (2, 7 and 0.1 millimetres on the ball; 6 millimetres on the can; 2.5 and 1 millimetres on the egg; 3 millimetres on the saddle; 4, 10 and 8.5 millimetres in the bowl; 69, 278, 1111, 1086, 2500 and 7.72 per square metre; 0.455, 0.029, 1 percent; within 2 percent and within a tenth of a percent): Recomputed from the model → All correct at the precision spoken; 68.22 is 1.76 percent below 69.44 and 69.37 is 0.11 percent below, which the working beats round to 2 percent and a tenth of a percent
- Verified: Beat checks and design-rule misconceptions exist in the served notes and are evidenced by the beats: Note digests of second-fundamental-form, principal-curvatures and gaussian-curvature → All nine check addresses and six misconception addresses exist; each prediction beat asks the check's own question (double the distance, along the can, gentlest a quarter turn on, saddle sign, Euler at 60 degrees, half radius against marble-and-football's inverse square, waist not zero, scale up by 3, rolled sheet)
- Verified: Contract buildable: ranges, steps, defaults, availability, presets, animations: Checked every preset and tour state against the param ranges and available_when; every animate target against its range → All ruler angles are multiples of 5, all radii multiples of 0.1, all probe distances multiples of 0.5; radius-2 appears only on bowl and egg presets, the k coefficients only on custom; every tour state names a declared preset
- Counterexample: Flat sheet (all coefficients 0): gap 0 in every direction, every radius undefined and shown as no bend, angle 0, product 0, ring 12.56637 cm with zero shortfall; the negative zero of the product on the can and the negative zero of $2K_{xy}$ (which would give $-90^\circ$ from atan2) are guarded by the build notes.
- Counterexample: Boundary: ball of radius 1 cm with the probe at 4 cm gives a gap of 8 cm and a ring 39 percent short with a ring curvature of 1473 against a product of 10000; the patch is a quadratic model of the surface near the touching point only, and the ring readout tracks the product only while the walked distance is small against every bend radius. No preset or tour goes there; recorded as a concern.
- Counterexample: Custom patch at the range corners (1, 0, 1), (1, 0, -1) and (0, 1, 0) with the probe at 4 cm: finite readouts, rings 39 percent short or 43 percent long; the geodesic integration stays stable.
- Counterexample: Both directions: the normal flipped on ball, bowl, egg and crisp negates every signed readout, swaps largest and smallest, moves the direction readout between 0 and 90 (or 45 and -45) and leaves the product unchanged.
- Counterexample: Degenerate paths: the ring on the can (a parabolic cylinder, isometric to the plane) closes with a shortfall of $9\times10^{-6}$ percent from integration error only; the saddle's asymptotic directions at 45 degrees and the crisp along the tick give a zero gap with no bend.
- Counterexample: Umbilic: the ball has $\kappa_1 = \kappa_2$, so the direction readout reports 0 by rule rather than by atan2 of 0 over 0.
- Fixed: Made the angle convention consistent with the tests and the negate-all-three flip rule: the ruler angle and the principal direction are measured counterclockwise seen from above the card in a frame fixed to the card, and the normal flip no longer claims to reverse the ruler-angle sense (params, principal-angle readout sense and speech, two equation conditions).
- Fixed: Reworded the gap and product readout speech so that it stays true when the value is zero (the can's zero product no longer says both bends go to the same side).
- Fixed: Added a caution to the working beat basketball-both-numbers that the patch is the ball's best-fit paraboloid and that the true sphere gives 0.462 percent.
- Fixed: Added build notes to the model method: guard the negative zero in atan2, round before choosing a speech template, and speak no bend for an undefined radius.
- Concern: Probe distances comparable to a bend radius (radius 1 cm with the probe at 4 cm, or the custom corners) leave the quadratic patch far from any real ball and the ring readout far from the product; a builder may want to cap the probe distance at half the smallest bend radius, or the tutor should keep to the presets, which all keep the walked distance below a third of the radius.
- Concern: The schema has no zero form for readout speech; the reworded templates are true at zero but a dedicated zero form would read better.
- Concern: The entry beat two-bends-on-the-egg glosses best-fit circle and names Gaussian curvature in one paragraph; both are glossary terms of the served note, so it was left as the novice review wrote it.
