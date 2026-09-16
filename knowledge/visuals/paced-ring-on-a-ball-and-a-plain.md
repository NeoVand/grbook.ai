---
type: "visual"
schema_version: 2
id: "paced-ring-on-a-ball-and-a-plain"
title: "Paced ring on a ball and a plain"
kind: "interactive-3d"
priority: "flagship"
status: "proposed"
revision: 2
rungs: ["entry", "working"]
serves: ["circumference-to-radius-test", "intrinsic-geometry", "gaussian-curvature", "curvature-of-the-two-sphere", "space-of-constant-curvature", "riemann-tensor-in-normal-coordinates", "ricci-scalar", "theorema-egregium"]
builds_on: ["two-walkers-set-off-side-by-side"]
leads_to: ["carry-an-arrow-around-a-loop", "three-rings-around-a-spot", "slide-a-patch-across-a-ball-and-an-egg"]
---

# Paced ring on a ball and a plain

`paced-ring-on-a-ball-and-a-plain` · interactive-3d · flagship · proposed · rungs: entry, working

> A string pulled tight along the ground draws a ring 6.28 times its length on a flat plain, but a shorter ring on a ball.

## What it makes visible

A ring drawn the same distance from a centre, with a tight string or by straight walks of equal length, is 6.28 times that distance on a flat plain, shorter on a ball, longer on a saddle, and exactly the plain's length on a paper tube. The shortfall grows as the square of the distance, so a small ring reads the Gaussian curvature at its centre; the ball's radius comes out of one ring; the same test at many spots tells constant curvature from an egg; a flat map drawn from the centre must draw the ring too long, which is why no flat map of a ball is exact. The notebook of readings works with the outside view hidden, which is the intrinsic viewpoint in one switch.

## The picture

A shaded surface with a faint grid fills the scene: a flat plain, a ball, a paper tube, a saddle, an egg, or a disc map of the hyperbolic plane. A red peg marks the centre. A solid blue string, or a fan of thin dotted blue straight walks, reaches out from the peg along the surface, and a solid orange ring is drawn through the far ends as the walk around the peg completes. A notebook panel on the right lists the distance walked, the tape reading along the ring, the playground length, the shortfall in millimetres and the missing fraction, with on-demand rows for the curvature estimate, the matching ball, the recovered ball radius, the Ricci scalar of the surface and the survey spread. Optional panels show the flat map drawn from the centre with a dashed orange map circle, and a plot of the missing fraction against the square of the distance with a grey line of slope K over 6. A survey switch tints the surface by its small-ring curvature at every spot. An outside-view switch hides the scene and leaves only the notebook.

| Element | Shows |
| --- | --- |
| Surface with a faint grid | the world of the surveyors: flat plain, ball, paper tube, saddle, egg, or hyperbolic disc map |
| Red peg | the centre of the ring, the spot whose curvature the ring reads |
| Solid blue string or thin dotted blue straight walks | the distance walked along the surface in every direction, the ring's radius measured along the ground |
| Solid orange ring | the ring through the far ends of the walks, whose length the tape reads along the surface |
| Notebook panel | everything the surveyors can know without leaving the surface |
| Map panel with a dashed orange circle | the flat map drawn from the centre with every straight walk at true length, whose circle is longer than the ground ring |
| Plot of missing fraction against distance squared | the small-ring law: a straight line of slope K over 6 near the origin |
| Survey tint | the small-ring curvature at every spot: uniform on a ball, a plain and a tube, varying on an egg and a saddle |

## Book figure

Two panels. Left: a ball with a red peg at its North Pole, a solid blue string pulled tight along the ball down to the equator, and the equator drawn as a solid orange ring; a tape reading of 70 centimetres beside it and the playground length of 110 centimetres crossed out. Right: a flat plain with the same string and its orange ring, tape reading 110 centimetres. Below both: a small notebook table with distance walked, ring length, and ring over distance, 4.00 for the ball and 6.28 for the plain.

Labels: peg, string 17.5 centimetres, ring 70 centimetres, ring 110 centimetres, ball, flat plain, ring over distance: 4.00 and 6.28. Aspect 2:1. Alt text: On a ball, a string a quarter of the way around draws the equator as its ring, 70 centimetres instead of the 110 centimetres the same string draws on a flat plain; the notebook shows ring over distance 4.00 on the ball and 6.28 on the plain.

## Variants

- **static** `static-card` (fallback): The print figure as an SVG card, used when 3D is unavailable and as a summary card.
- **interactive-2d** `notebook-and-map-2d`: The notebook, the flat map panel and the plot without a 3D scene: sliders for the surface, its radius and the distance walked drive the readouts, with the unrolled tube sheet drawn flat.
- **interactive-3d** `full-3d`: The full experience on every surface, with the string or walkers animated around the peg, the survey tint, the map and plot panels, the unrolled tube, and the outside-view switch.

## Parameters

| Id | Label | Type | Options or range | Default | Available when | Effect |
| --- | --- | --- | --- | --- | --- | --- |
| `surface` | Surface | enum | plain, ball, tube, saddle, egg, hyperbolic | "ball" | — | Switches the surface; the peg, the walks and the ring are rebuilt on it. The hyperbolic plane is shown as a disc map with its true ring lengths in the notebook. |
| `drawing` | How the ring is drawn | enum | string (surface in plain, ball, tube, egg), walkers | "string" | — | A tight string lies along a straight walk only where the surface bulges toward it, so the string is offered on the plain, the ball, the tube and the egg; on the saddle and the hyperbolic plane the ring is drawn by walkers who never steer. Both draw the same ring. |
| `radius` | Size of the surface | number | 0.01–10000000 step None m | 0.1114 | surface in ball, tube, egg, saddle, hyperbolic | The ball's radius a; the tube's radius; the egg's half-width b; the saddle's scale R in z = (x² − y²)/(2R) over \|x\|, \|y\| ≤ 0.5R; the hyperbolic plane's curvature radius a, with K = −1/a². Slider on a logarithmic scale from 1 centimetre to 10,000 kilometres. |
| `egg-aspect` | Egg length over width | number | 1–2 step 0.05 1 | 1.5 | surface in egg | The egg is a spheroid of half-width b (the radius param) and half-length c = aspect × b, with both ends the same shape; aspect 1 is a ball. |
| `centre-latitude` | Latitude of the centre | number | 0–90 step 5 deg | 90 | surface in ball, egg | Moves the peg: 90 is the pole of the ball or the tip of the egg, 0 is the equator or the egg's widest part. On the ball the readouts never change with it. |
| `walk-distance` | Distance walked from the peg | number | 0.001–10000000 step None m | 0.05 | — | The string's length, or the length of every straight walk, measured along the surface. On the ball it is clamped to $\pi a$, the walk to the far pole. Slider on a logarithmic scale. |
| `progress` | Drawing progress | progress | 0–1 step 0.01 | 0 | — | Sweeps the string, or sends the walkers out, once around the peg; the ring closes and the on-complete readouts appear only at 1. |
| `outside-view` | Show the outside view | boolean | — | true | — | When false, the 3D scene is hidden and only the notebook panel remains; every readout keeps its value. |
| `unrolled` | Unroll the tube | boolean | — | false | surface in tube | Shows the flat sheet beside the tube with the same peg, walks and ring drawn on it. |
| `map-panel` | Show the flat map from the centre | boolean | — | false | — | Shows a flat map that draws every straight walk from the peg at its true length and direction; the ring's map circle is dashed orange, and the playground length readout doubles as its length. |
| `plot-panel` | Show the small-ring plot | boolean | — | false | — | Plots the missing fraction against the square of the distance walked, for distances up to the current one, with a grey line of slope K over 6 through the origin, K being the surface's curvature at the peg. |
| `survey` | Survey every spot | boolean | — | false | surface in plain, ball, tube, egg, saddle | Tints the surface by its small-ring Gaussian curvature at every spot, orange deeper where small rings come out shorter, purple where they come out longer, white where they match flat ground, and shows the survey spread readout. |

## Presets

- `plain-string` String ring on a flat plain: surface="plain", drawing="string", walk-distance=0.05
- `football-short-string` Football, 5 centimetre string: surface="ball", drawing="string", radius=0.1114, walk-distance=0.05
- `football-double-string` Football, 10 centimetre string: surface="ball", drawing="string", radius=0.1114, walk-distance=0.1
- `football-equator-string` Football, string to the equator: surface="ball", drawing="string", radius=0.1114, walk-distance=0.175
- `football-tiny-string` Football, 1 millimetre string: surface="ball", drawing="string", radius=0.1114, walk-distance=0.001
- `football-two-millimetres` Football, 2 millimetre string: surface="ball", drawing="string", radius=0.1114, walk-distance=0.002
- `marble-two-millimetres` Marble, 2 millimetre string: surface="ball", drawing="string", radius=0.01, walk-distance=0.002
- `ball-to-the-far-pole` Ball, string to the far pole: surface="ball", drawing="string", radius=0.1, walk-distance=0.3141593
- `ball-centre-moved` Football, peg at latitude 30: surface="ball", drawing="string", radius=0.1114, walk-distance=0.05, centre-latitude=30
- `earth-one-kilometre` Earth, 1 kilometre walk: surface="ball", drawing="walkers", radius=6371000, walk-distance=1000
- `earth-five-kilometres` Earth, 5 kilometre walk, with map: surface="ball", drawing="walkers", radius=6371000, walk-distance=5000, map-panel=true
- `earth-ten-kilometres` Earth, 10 kilometre walk, with map: surface="ball", drawing="walkers", radius=6371000, walk-distance=10000, map-panel=true
- `earth-twenty-kilometres` Earth, 20 kilometre walk, with map: surface="ball", drawing="walkers", radius=6371000, walk-distance=20000, map-panel=true
- `earth-thirty-kilometres` Earth, 30 kilometre walk: surface="ball", drawing="walkers", radius=6371000, walk-distance=30000
- `earth-thousand-kilometres` Earth, 1,000 kilometre walk, with map: surface="ball", drawing="walkers", radius=6371000, walk-distance=1000000, map-panel=true
- `moon-to-the-equator` Small moon, notebook only: surface="ball", drawing="walkers", radius=636619.77, walk-distance=1000000, outside-view=false
- `notebook-only-football` Football, notebook only: surface="ball", drawing="walkers", radius=0.1114, walk-distance=0.1, outside-view=false
- `notebook-only-tube` Paper tube, notebook only: surface="tube", drawing="walkers", radius=0.0477465, walk-distance=0.05, outside-view=false
- `tube-short-string` Paper tube, 5 centimetre string: surface="tube", drawing="string", radius=0.0477465, walk-distance=0.05
- `tube-unrolled` Paper tube, unrolled, with map: surface="tube", drawing="string", radius=0.0477465, walk-distance=0.05, unrolled=true, map-panel=true
- `tube-long-string` Paper tube, 20 centimetre string: surface="tube", drawing="string", radius=0.0477465, walk-distance=0.2
- `saddle-centre` Saddle, 10 centimetre walks: surface="saddle", drawing="walkers", radius=1, walk-distance=0.1
- `egg-tip` Egg, ring at a tip: surface="egg", drawing="walkers", radius=0.02, egg-aspect=1.5, centre-latitude=90, walk-distance=0.002
- `egg-widest` Egg, ring at the widest part: surface="egg", drawing="walkers", radius=0.02, egg-aspect=1.5, centre-latitude=0, walk-distance=0.002
- `egg-halfway` Egg, ring halfway to a tip: surface="egg", drawing="walkers", radius=0.02, egg-aspect=1.5, centre-latitude=45, walk-distance=0.002
- `hyperbolic-one-metre` Hyperbolic plane, 1 metre walks: surface="hyperbolic", drawing="walkers", radius=1, walk-distance=1
- `hyperbolic-five-metres` Hyperbolic plane, 5 metre walks: surface="hyperbolic", drawing="walkers", radius=1, walk-distance=5
- `hyperbolic-surveyors` Surveyors' ring, 2 kilometres on a hyperbolic plane: surface="hyperbolic", drawing="walkers", radius=10000, walk-distance=2000
- `survey-ball` Survey a ball: surface="ball", drawing="walkers", radius=0.03, walk-distance=0.002, survey=true
- `survey-egg` Survey an egg: surface="egg", drawing="walkers", radius=0.02, egg-aspect=1.5, walk-distance=0.002, survey=true
- `survey-tube` Survey a paper tube: surface="tube", drawing="walkers", radius=0.02, walk-distance=0.002, survey=true
- `survey-saddle` Survey a saddle: surface="saddle", drawing="walkers", radius=1, walk-distance=0.1, survey=true
- `plot-football` Football with the small-ring plot: surface="ball", drawing="string", radius=0.1114, walk-distance=0.05, plot-panel=true

## Readouts

- `ring-length` Ring length along the surface (m; visible on-complete; 4 decimals): “the tape laid along the ring reads {value} metres”
- `playground-length` Playground length (m; visible on-complete; 4 decimals): “on a flat plain the same distance would draw a ring {value} metres long”
- `shortfall` Shortfall (mm; visible on-complete; 3 decimals; sense: positive when the ring is shorter than its playground length): “the ring is short by {abs} millimetres” / “the ring is too long by {abs} millimetres”
- `missing-fraction` Missing fraction (percent; visible on-complete; 4 decimals; sense: positive when the ring is shorter than its playground length): “the missing fraction is {abs} per cent” / “the ring is too long by {abs} per cent of its playground length”
- `ring-over-walk` Ring length over distance walked (1; visible on-complete; 3 decimals): “the ring is {value} times the distance walked”
- `curvature-estimate` Gaussian curvature from this ring (m^-2; visible on-demand; 6 decimals; sense: positive where the ring comes out short): “this ring gives a Gaussian curvature of {abs} per square metre, with no minus sign” / “this ring gives a Gaussian curvature of {abs} per square metre, with a minus sign”
- `matching-ball-radius` Matching ball radius (m; visible on-demand; 4 decimals): “the matching ball has a radius of {value} metres”
- `recovered-radius` Ball radius recovered from this ring (m; visible on-demand; 4 decimals): “from this one ring the ball's radius comes out as {value} metres”
- `ricci-scalar` Ricci scalar of this surface (m^-2; visible on-demand; 6 decimals; sense: positive where small rings come out short): “the Ricci scalar of this surface is {abs} per square metre, with no minus sign” / “the Ricci scalar of this surface is {abs} per square metre, with a minus sign”
- `survey-spread` Survey spread (m^-2; visible on-demand; 6 decimals): “the biggest and smallest small-ring curvature readings across the surface differ by {value} per square metre”

## Tours

### `ring-test-first-look` · for [[circumference-to-radius-test]] · entry

1. `ring-on-the-plain` (entry, await none) state: preset="plain-string", progress=0; animate progress → 1 over 4 s  
   *Flat plain with the red peg, the solid blue string pulled tight along the ground, and the solid orange ring being drawn as the string sweeps once around the peg. The notebook then shows ring length 0.3142 metres and playground length 0.3142 metres.*  
   Say: “Here is a flat plain. The red dot is a peg pushed into the ground. The solid blue line is a string tied to the peg, 5 centimetres long, pulled tight along the ground. I walk once around the peg, and chalk at the string's far end draws the solid orange ring. A soft tape laid along the ring reads about 31.4 centimetres, which is 6.28 times the string. Because 6.28 times the string is what a flat plain always gives, I call it the ring's playground length.”  
   Describe: A string 5 centimetres long is swept once around a peg on flat ground, drawing a ring. The notebook reads a ring length of 0.3142 metres and a playground length of 0.3142 metres, the same number.
2. `predict-the-equator-ring` (entry, await prediction) state: preset="football-equator-string", progress=0; evidences `circumference-to-radius-test/checks/string-ring-on-a-football`  
   *Football with the peg at the North Pole and the solid blue string pulled tight along the ball down to the equator; no ring drawn yet.*  
   Predict: “This string is 17.5 centimetres long, a quarter of the way around the ball, so its ring is the ball's equator. What will the tape read along the ring, compared with 110 centimetres on a plain?”  
   Say: “Now the peg is stuck to a football, 70 centimetres around its middle. Call the peg the North Pole. The solid blue string is 17.5 centimetres long, a quarter of the way around the ball, so its far end sits on the equator, the line around the ball's middle. I keep the string pressed to the ball, never through the air. Before I draw the ring, guess. On a plain, this string draws a ring about 110 centimetres long. What will the tape read here?”  
   Describe: A string 17.5 centimetres long reaches from the ball's North Pole to its equator along the surface. The ring is not drawn yet, and a prediction is asked for.
3. `draw-the-equator-ring` (entry, await none) state: preset="football-equator-string", progress=0; animate progress → 1 over 4 s  
   *The string sweeps around the pole and the solid orange ring closes along the equator. The notebook shows ring length 0.6999 metres, playground length 1.0996 metres, ring over distance 4.000.*  
   Say: “I sweep the string once around the pole. The solid orange ring is the equator, and the tape along it reads 70 centimetres. The playground length was 110 centimetres, so the ring is short by more than a third. The string lay along the ball the whole way, so the ring's radius is the string, measured along the ball. The distance through the air from the ring to the ball's centre, deep inside the ball, is not something anyone on the ball can measure.”  
   Describe: The ring closes along the equator. The notebook reads a ring length of 0.6999 metres against a playground length of 1.0996 metres, and the ring is 4.00 times the distance walked instead of 6.28.
4. `short-string` (entry, await none) state: preset="football-short-string", progress=1  
   *Football with a 5 centimetre string and its ring; notebook: ring length 0.3037 metres, shortfall 10.442 millimetres, missing fraction 3.3239 per cent.*  
   Say: “Now the string is 5 centimetres, the same string as on the plain. The tape reads about 30.4 centimetres, so the ring misses about 1 centimetre of its playground length. Dividing the missing length by the playground length gives the missing fraction, about 3 parts in 100. Even this small ring comes out short, so the ball is curved everywhere, not only near the equator.”  
   Describe: With a 5 centimetre string on the football, the notebook reads a ring length of 0.3037 metres. The shortfall is 10.4 millimetres and the missing fraction 3.32 per cent.
5. `double-the-string` (entry, await none) state: preset="football-double-string", progress=1  
   *Football with a 10 centimetre string and its ring; notebook: ring length 0.5473 metres, shortfall 81.048 millimetres, missing fraction 12.8992 per cent.*  
   Say: “I double the string to 10 centimetres. The tape reads about 54.7 centimetres, and the ring misses about 8 centimetres, which is about 13 parts in 100. Doubling the string made the missing fraction about four times bigger, not twice. The reason is that the ball draws two strings laid out in neighbouring directions together only gently at first, and more strongly the farther they reach.”  
   Describe: With a 10 centimetre string, the notebook reads a ring length of 0.5473 metres. The shortfall is 81 millimetres and the missing fraction 12.9 per cent, about four times the fraction for the 5 centimetre string.
6. `predict-the-tube` (entry, await prediction) state: preset="tube-short-string", progress=0; evidences `curved-surfaces/checks/ring-on-a-paper-tube`  
   *Paper tube 30 centimetres around with the peg on its side and a 5 centimetre solid blue string pulled tight along the paper; no ring yet.*  
   Predict: “This paper tube looks bent. Its string is 5 centimetres, less than half of the 15 centimetres from the peg around to the wall opposite it. Will the tape read less than, the same as, or more than 31.4 centimetres?”  
   Say: “Here is a sheet of paper rolled into a tube 30 centimetres around and held closed with sticky tape. From outside it looks bent. The peg is pushed into the tube's curved wall, and the solid blue string is 5 centimetres, pulled tight along the paper. Guess first. Will the tape read less than, the same as, or more than 31.4 centimetres?”  
   Describe: A 5 centimetre string is held tight along a paper tube 30 centimetres around. The ring is not drawn yet, and a prediction is asked for.
7. `unroll-the-tube` (entry, await none) state: preset="tube-unrolled", progress=1  
   *The ring drawn on the tube, and beside it the unrolled sheet with the same peg, string and ring; notebook: ring length 0.3142 metres, shortfall 0.000 millimetres.*  
   Say: “The tape reads 31.4 centimetres, the playground length exactly. To see why, I peel off the sticky tape and unroll the sheet, shown on the right of the tube. Paper does not stretch, so every point of the solid orange ring still sits 5 centimetres from the peg. On the flat sheet that is an ordinary circle. The tube looks bent to us, but for the string and the tape it is flat.”  
   Describe: The tube's ring is 0.3142 metres long, with zero shortfall. Beside the tube, the same sheet lies flat, and the ring on it is an ordinary circle 5 centimetres from the peg.
8. `predict-the-saddle` (entry, await prediction) state: preset="saddle-centre", progress=0; evidences `circumference-to-radius-test/checks/a-ring-that-is-too-long`  
   *Saddle surface with the peg at its middle and thin dotted blue straight walks starting out; no ring yet.*  
   Predict: “On this saddle, walkers step out 10 centimetres from the peg in every direction without steering. Will their ring be shorter than, the same as, or longer than 62.8 centimetres?”  
   Say: “This surface is shaped like a horse's saddle: it rises in front and behind, and falls away on both sides. A string pulled tight here would lift off the surface, like a string pulled across the inside of a cup, so walkers draw the ring instead. Each walker leaves the red peg, walks 10 centimetres without ever steering, and stops. The thin dotted blue lines are their walks. Guess first. Will the ring through their stopping places be shorter or longer than 62.8 centimetres?”  
   Describe: Walkers set out 10 centimetres from a peg at the middle of a saddle-shaped surface. The ring is not drawn yet, and a prediction is asked for.
9. `too-long-on-the-saddle` (entry, await none) state: preset="saddle-centre", progress=1  
   *The ring through the walkers' stopping places; notebook: ring length 0.6294 metres, shortfall −1.041 millimetres, missing fraction −0.1657 per cent.*  
   Say: “The tape along the solid orange ring reads 62.9 centimetres, about 1 millimetre more than the playground length. The notebook shows the shortfall with a minus sign, because the ring is too long. Neighbouring walks on a saddle spread apart faster than on a plain, so the gaps between stopping places grow faster. Too short means positive curvature, like a ball. Too long means negative curvature, like this saddle.”  
   Describe: The ring on the saddle is 0.6294 metres long, about 1 millimetre longer than its playground length. The notebook reports the ring as too long, which means negative curvature at the peg.
10. `earth-thirty-kilometres` (entry, await none) state: preset="earth-thirty-kilometres", progress=1  
   *Earth as a smooth ball with a 30 kilometre ring drawn around the peg; notebook: ring length 188494.8626 metres, shortfall 696.589 millimetres.*  
   Say: “Last, the ball is Earth, treated as smooth, 40,000 kilometres around. Walkers pace 30 kilometres from the peg. The tape along the ring reads about 188 kilometres, and the ring misses its playground length by about 70 centimetres. That is less than 4 millimetres in each kilometre of ring. So nobody notices the curving on a walk, and it takes surveying instruments to find it.”  
   Describe: On a smooth Earth, a ring paced out 30 kilometres from its centre is 188.5 kilometres long and falls short of its playground length by 70 centimetres.

### `small-ring-law` · for [[circumference-to-radius-test]] · working

1. `plot-the-fraction` (working, await none) state: preset="plot-football", progress=1  
   *Football with the 5 centimetre ring, and the plot panel: orange points of missing fraction against distance squared for distances up to 5 centimetres, with a grey line of slope K over 6 through the origin.*  
   Say: “The plot on the right shows the missing fraction against the square of the string's length, as orange points. Near the origin they lie on the grey line, whose slope is the Gaussian curvature K divided by 6. That is the small-ring law: the ring length is 2 pi rho minus pi over 3 times K times rho cubed, plus smaller terms. On a ball K is 1 over a squared, and the exact ring length is 2 pi a times the sine of rho over a.”  
   Describe: A plot of missing fraction against distance squared. The points follow a straight line through the origin with slope K over 6, where K is the Gaussian curvature at the peg.
2. `estimate-converges` (working, await none) state: preset="football-tiny-string", progress=1  
   *Football with a 1 millimetre string; on-demand row: Gaussian curvature from this ring 80.580112 per square metre; the ball's 1 over a squared is 80.580437.*  
   Say: “The notebook's on-demand row turns one ring into a curvature estimate: 3 times the missing length, divided by pi times the string length cubed. With a 1 millimetre string on the football it reads 80.580 per square metre. One over the radius squared is 80.580 per square metre too, matching to 4 parts in a million. The estimate approaches K as the string shrinks, and the 5 centimetre string gave 79.77, one per cent low.”  
   Describe: With a 1 millimetre string the curvature estimate reads 80.580 per square metre, matching one over the ball's radius squared to a few parts in a million.
3. `predict-the-surveyors-ring` (working, await prediction) state: preset="hyperbolic-surveyors", progress=1; evidences `circumference-to-radius-test/checks/curvature-from-one-ring`  
   *Disc map of a hyperbolic plane with the peg and a 2 kilometre ring; notebook: ring length 12650.3141 metres, playground length 12566.3706 metres; on-demand rows hidden until the reveal.*  
   Predict: “Surveyors walk 2 kilometres from a centre and measure the ring at 12,650.3 metres, against 12,566.4 on a plain. What is the Gaussian curvature at the centre, with its sign, and the radius of curvature?”  
   Say: “Now the surveyors' notebook only. They walked 2 kilometres out in every direction and taped the ring at 12,650.3 metres. On a plain it would be 12,566.4 metres. Before I open the on-demand rows, work out the Gaussian curvature at the centre, with its sign, and the radius of curvature, 1 over the square root of its size.”  
   Describe: A ring of radius 2 kilometres measures 12,650.3 metres, longer than the 12,566.4 metres of a flat plain. A prediction of the curvature and its sign is asked for.
4. `reveal-the-surveyors-curvature` (working, await none) state: preset="hyperbolic-surveyors", progress=1  
   *Same state with the on-demand rows open: Gaussian curvature from this ring −0.000000010 per square metre, matching ball radius 9990.0055 metres.*  
   Say: “The ring is too long by 84 metres, so the missing fraction is minus 0.668 per cent and the curvature is negative: minus 1.00 times 10 to the minus 8 per square metre, which is minus 0.0100 per square kilometre. The radius of curvature is about 9,990 metres. This surface is a hyperbolic plane with curvature radius 10 kilometres, and the estimate misses the last tenth of a per cent because 2 kilometres is not tiny next to 10.”  
   Describe: The on-demand rows show a Gaussian curvature of minus 1.00 times 10 to the minus 8 per square metre and a matching ball radius of 9,990 metres, close to the surface's true curvature radius of 10 kilometres.
5. `ring-splits-on-the-tube` (working, await none) state: preset="tube-long-string", progress=1  
   *Paper tube with a 20 centimetre string, longer than half the way around; the ring is two solid orange loops around the tube; notebook: ring length 0.6784 metres, missing fraction 46.0107 per cent; the curvature rows are hidden.*  
   Say: “One caution. On the tube the string is now 20 centimetres, more than the 15 centimetres to the back of the tube. The far ends form two solid orange loops around the tube, and their total length, 4 rho times the arcsine of pi a over rho, is only 67.8 centimetres. The missing fraction is 46 per cent, yet the tube's curvature is zero. The law reads curvature only from one small simple ring, so the notebook hides the estimate here.”  
   Describe: With a 20 centimetre string on a tube 30 centimetres around, the ring splits into two loops of total length 0.6784 metres, a missing fraction of 46 per cent, although the tube is flat. The curvature estimate is hidden because the ring is not one small loop.

### `surveyors-notebook` · for [[intrinsic-geometry]] · entry

1. `hide-the-outside` (entry, await none) state: preset="notebook-only-football", progress=1  
   *The 3D scene is hidden; only the notebook panel: distance walked 0.1 metres, ring length 0.5473 metres, playground length 0.6283 metres, ring over distance 5.473.*  
   Say: “I have switched off the outside view. What is left is the surveyors' notebook, and surveyors can never leave their ground. They walked 10 centimetres out from the peg in every direction and measured the ring with their tape at 54.7 centimetres. Ring over distance reads 5.47. On a flat plain that number is always 6.28. So from the notebook alone they know their world is not a plain.”  
   Describe: Only the notebook is shown. Distance walked 0.1 metres, ring length 0.5473 metres, ring over distance 5.47 instead of the 6.28 of a flat plain.
2. `notebook-on-the-tube` (entry, await none) state: preset="notebook-only-tube", progress=1  
   *Notebook only: distance walked 0.05 metres, ring length 0.3142 metres, ring over distance 6.283.*  
   Say: “Here is a second notebook. Distance walked 5 centimetres, ring 31.4 centimetres, ring over distance 6.28. Every ring these surveyors draw comes out at its playground length. Their notebook cannot tell their world from a flat plain, however many rings they draw.”  
   Describe: A second notebook: distance walked 0.05 metres, ring length 0.3142 metres, ring over distance 6.28, exactly as on a flat plain.
3. `reveal-the-tube` (entry, await none) state: preset="tube-unrolled", progress=1  
   *Outside view back on: the second notebook's world is a paper tube, shown with its unrolled sheet beside it.*  
   Say: “I switch the outside view back on. The second world is a paper tube. To us it looks bent, but rolling paper stretches nothing, so no length along the paper changed. The unrolled sheet on the right shows the same solid orange ring as an ordinary circle. Bent is something only an outsider can see. Curved is something the surveyors' tape can find.”  
   Describe: The outside view shows that the second notebook came from a paper tube. Beside it the same sheet lies flat with the same ring, an ordinary circle.
4. `predict-the-moon-ring` (entry, await prediction) state: preset="moon-to-the-equator", progress=1; evidences `intrinsic-geometry/checks/ring-on-a-small-moon`  
   *Notebook only: distance walked 1000000 metres, ring length 4000000.0000 metres; the playground length row is covered until the reveal.*  
   Predict: “Surveyors on a small, smooth, round moon walk 1,000 kilometres from a centre in every direction and measure the ring with their tape at 4,000 kilometres. How long would a ring of radius 1,000 kilometres be on a flat plain, and what does the difference tell them?”  
   Say: “A third notebook, with the outside view off. Surveyors on a small, smooth, round moon walked 1,000 kilometres from a centre in every direction. They measured the ring with their tape at 4,000 kilometres. How long would a ring of radius 1,000 kilometres be on a flat plain? And what does the difference tell them about their moon?”  
   Describe: A third notebook: distance walked 1,000 kilometres, ring length 4,000 kilometres. A prediction of the flat-plain length is asked for.
5. `reveal-the-moon` (entry, await none) state: preset="moon-to-the-equator", progress=1, outside-view=true  
   *The moon appears: a ball with the peg at its pole and the ring along its equator; notebook: playground length 6283185.3072 metres, ring over distance 4.000; on-demand row recovered radius 636619.77 metres.*  
   Say: “On a plain the ring would be 6,283 kilometres, so this ring is short by more than a third. Short means their moon is curved like a ball. Ring over distance is exactly 4. That is the equator's number, because the equator is four times the walk from a pole down to it. So the walk was a quarter of the way around, the moon is about 4,000 kilometres around, and its radius, 4,000 divided by 6.28, is about 637 kilometres. Nothing in this needed a view from outside.”  
   Describe: The playground length is 6,283 kilometres, so the 4,000 kilometre ring is short by more than a third. The ring is the moon's equator, and the recovered radius reads 637 kilometres, found from the notebook alone.

### `matching-ball` · for [[gaussian-curvature]] · entry

1. `ring-at-the-tip` (entry, await none) state: preset="egg-tip", progress=1  
   *Smooth egg 6 centimetres long and 4 wide with the peg at a tip; a ring of 2 millimetre walks; notebook: missing fraction 0.3718 per cent; on-demand rows: matching ball radius 0.0134 metres, Gaussian curvature 5577.10 per square metre.*  
   Say: “This is a smooth plastic egg, 6 centimetres long and 4 centimetres wide, with both ends the same shape. The red peg is at one tip. Walkers step out 2 millimetres in every direction, along the thin dotted blue lines, and the solid orange ring passes through their stopping places. The ring misses about 0.37 per cent of its playground length. The matching ball row asks which ball gives the same missing fraction for the same walk: a ball of radius 1.34 centimetres.”  
   Describe: At the tip of the egg, a ring of 2 millimetre walks misses 0.37 per cent of its playground length. The matching ball, the ball whose ring would miss the same fraction, has a radius of 1.34 centimetres.
2. `ring-at-the-widest-part` (entry, await none) state: preset="egg-widest", progress=1  
   *Peg moved to the egg's widest part; notebook: missing fraction 0.0741 per cent; on-demand rows: matching ball radius 0.0300 metres, Gaussian curvature 1112.12 per square metre.*  
   Say: “I move the peg to the egg's widest part, halfway between the tips, and the walkers step out 2 millimetres again. Now the ring misses only 0.074 per cent, one fifth of the tip's fraction. The matching ball here has a radius of 3.0 centimetres, wider than the egg itself, because from tip to tip the shell curves only gently. The Gaussian curvature row divides 1 by the matching radius in metres times itself: 1,112 per square metre, which is 0.11 per square centimetre. At the tip it read 5,577, five times as big.”  
   Describe: At the widest part, the ring misses 0.074 per cent, five times less than at the tip. The matching ball radius is 3.0 centimetres and the Gaussian curvature 1,112 per square metre, against 5,577 at the tip.
3. `predict-marble-against-football` (entry, await prediction) state: preset="marble-two-millimetres", progress=1; evidences `gaussian-curvature/checks/marble-and-football`  
   *A marble of radius 1 centimetre with a 2 millimetre string ring; the on-demand curvature row is covered until the reveal.*  
   Predict: “A marble has a radius of 1 centimetre and a football a radius of 11 centimetres. Both get a 2 millimetre string ring. How many times bigger is the marble's Gaussian curvature? A friend guesses 11 times.”  
   Say: “Now a marble, radius 1 centimetre, with a 2 millimetre string ring. Next I will draw the same ring on the football, radius 11 centimetres. On a ball every spot's matching ball is the ball itself. How many times bigger is the marble's Gaussian curvature than the football's? A friend guesses 11 times.”  
   Describe: A marble of radius 1 centimetre carries a 2 millimetre ring. A prediction is asked for: how many times bigger the marble's Gaussian curvature is than a football's, radius 11 centimetres.
4. `reveal-marble-against-football` (entry, await none) state: preset="football-two-millimetres", progress=1  
   *The football with a 2 millimetre ring; on-demand curvature row 80.58 per square metre, and the marble's 9980.02 per square metre shown for comparison.*  
   Say: “The marble's ring gives 9,980 per square metre. The football's ring gives 80.6 per square metre. That is about 124 times, close to 11 times 11, which is 121. Doubling a ball's radius makes the radius times itself four times bigger, so the curvature drops to a quarter, not a half. The reading is a little over 121 because 2 millimetres is not tiny next to a 1 centimetre marble; a shorter string brings it closer.”  
   Describe: The marble's ring gives a Gaussian curvature of 9,980 per square metre and the football's 80.6, a ratio of about 124, close to 11 squared. The curvature falls with the square of the radius.
5. `negative-on-the-saddle` (entry, await none) state: preset="saddle-centre", progress=1  
   *Saddle with the 10 centimetre ring; on-demand rows: Gaussian curvature −0.994 per square metre, matching ball radius 1.0028 metres.*  
   Say: “On the saddle the ring came out too long. The matching ball is the ball whose ring would fall short by the same fraction that this ring is too long: radius about 1 metre. The Gaussian curvature row shows 1 divided by 1 times itself, with a minus sign in front: minus 0.99 per square metre. Positive means rings too short, zero means rings as on flat paper, negative means rings too long.”  
   Describe: On the saddle the ring is too long. The notebook reports a Gaussian curvature of minus 0.99 per square metre, and a matching ball radius of about 1 metre; the curvature row carries the minus sign.

### `radius-without-leaving` · for [[curvature-of-the-two-sphere]] · entry

1. `one-ring-gives-the-radius` (entry, await none) state: preset="football-short-string", progress=1  
   *Football with the 5 centimetre ring; on-demand row: ball radius recovered from this ring 0.1114 metres.*  
   Say: “An explorer on a round ball who can never leave it can still find its radius. The notebook's recovered radius row works the radius out from one ring's two numbers, the string and the ring. With the 5 centimetre string and its 30.4 centimetre ring, it reads 11.14 centimetres. That is the football's radius, 70 centimetres around divided by 6.28.”  
   Describe: From the 5 centimetre ring the notebook recovers a ball radius of 0.1114 metres, the football's true radius.
2. `any-string-same-radius` (entry, await none) state: preset="football-equator-string", progress=1  
   *Football with the equator ring; recovered radius row still 0.1114 metres.*  
   Say: “I change to the 17.5 centimetre string, whose ring is the equator. The recovered radius still reads 11.14 centimetres. Whatever the string, a round ball gives the same answer, because one rule links the string, the ring and the radius on every round ball. That is the tape-measure reading of the ball's curvature.”  
   Describe: With the string reaching the equator, the recovered radius row still reads 0.1114 metres. Every ring on a round ball gives the same radius.
3. `string-to-the-far-pole` (entry, await none) state: preset="ball-to-the-far-pole", progress=1  
   *A ball of radius 10 centimetres with the string reaching the far pole; the ring is a single point; notebook: ring length 0.0000 metres; recovered radius 0.1000 metres.*  
   Say: “On this ball, radius 10 centimetres, I lengthen the string until it reaches the far pole, the spot exactly opposite the peg. That is 31.4 centimetres along the surface. Whichever way the string points, its far end now sits on that one spot. So the solid orange ring shrinks to a point, and the tape reads zero. Even then the recovered radius reads 10 centimetres. The string is half the way around, so the radius is the string divided by 3.14.”  
   Describe: With the string reaching the far pole of a 10 centimetre ball, the ring shrinks to a point and its length reads zero, yet the recovered radius still reads 0.1 metres.
4. `predict-moving-the-peg` (entry, await prediction) state: preset="ball-centre-moved", progress=0; evidences `curvature-of-the-two-sphere/checks/same-loop-anywhere`  
   *Football with the peg at latitude 30 degrees, 5 centimetre string, no ring yet.*  
   Predict: “I move the peg from the pole down to latitude 30 degrees and keep the 5 centimetre string. Will the ring, the missing fraction, or the recovered radius change?”  
   Say: “The peg now sits at latitude 30 degrees, a third of the way from the equator up to the pole, instead of at the pole, with the same 5 centimetre string. Guess first. Will the ring, the missing fraction, or the recovered radius change?”  
   Describe: The peg has moved from the pole to latitude 30 degrees with the same 5 centimetre string. A prediction is asked for.
5. `every-spot-alike` (entry, await none) state: preset="ball-centre-moved", progress=1  
   *The ring drawn at latitude 30; notebook: ring length 0.3037 metres, missing fraction 3.3239 per cent, recovered radius 0.1114 metres, all unchanged.*  
   Say: “Nothing changes. The tape reads 30.4 centimetres, the missing fraction 3.32 per cent, the recovered radius 11.14 centimetres. Every spot of a round ball is shaped like every other spot. The painted lines on a globe crowd together near its poles, but they are only paint; the ball under them is the same everywhere.”  
   Describe: At latitude 30 the ring length, missing fraction and recovered radius are unchanged. Every spot of a round ball gives the same readings.

### `constant-curvature-survey` · for [[space-of-constant-curvature]] · entry

1. `survey-the-ball` (entry, await none) state: preset="survey-ball", progress=1  
   *A ball of radius 3 centimetres tinted a single even orange all over; on-demand row: survey spread 0.000000 per square metre.*  
   Say: “The survey switch runs the ring test at every spot at once, with 2 millimetre walks, and tints each spot by its answer: deeper orange where the ring misses more. This ball, 6 centimetres wide, is one even orange all over. The survey spread row, the biggest answer minus the smallest, reads zero. A surface whose ring test gives the same Gaussian curvature at every spot has constant curvature.”  
   Describe: A ball surveyed at every spot with 2 millimetre rings shows the same reading everywhere; the survey spread is zero, so the ball has constant curvature.
2. `predict-egg-and-tube` (entry, await prediction) state: preset="survey-egg", progress=0; evidences `space-of-constant-curvature/checks/ball-egg-and-tube`  
   *The egg, not yet tinted, beside the ball; a prediction is asked for.*  
   Predict: “Three ants run the ring test at many spots with 2 millimetre walks. One lives on this ball, one on a smooth egg 6 centimetres long and 4 wide, one on a paper tube 4 centimetres wide. Which worlds have constant curvature, and why?”  
   Say: “Next I will survey a smooth egg, 6 centimetres long and 4 centimetres wide, and then a paper tube 4 centimetres wide. Guess first. Three ants run the ring test at many spots on the ball, the egg and the tube, walking 2 millimetres out each time. Which of these worlds have constant curvature, and why?”  
   Describe: An egg and a paper tube are about to be surveyed. A prediction is asked for: which of ball, egg and tube have constant curvature.
3. `survey-the-egg` (entry, await none) state: preset="survey-egg", progress=1  
   *The egg tinted deep orange at both tips and pale orange around its widest part; survey spread 4513.888889 per square metre.*  
   Say: “The egg comes out deep orange at both tips and pale around its widest part. Rings at a tip miss about five times as much as rings at the widest part. The survey spread reads 4,514 per square metre, the tip's 5,625 minus the widest part's 1,111. The egg is smooth and rounded all over, but its curving is not the same everywhere. So the egg does not have constant curvature.”  
   Describe: The egg's survey varies from a Gaussian curvature of 5,625 per square metre at the tips to 1,111 at the widest part, a spread of 4,514. The egg does not have constant curvature.
4. `survey-the-tube` (entry, await none) state: preset="survey-tube", progress=1  
   *The paper tube white all over; survey spread 0.000000 per square metre.*  
   Say: “The tube comes out white everywhere, the tint for rings that match flat ground, and the survey spread reads zero. The tube bends around its middle but not along its length, yet that bend is only for outsiders. Rolling paper changes no length along it, so every small ring is 6.28 times its walk. Zero at every spot is the same number at every spot, so the tube has constant curvature too, like flat ground.”  
   Describe: The tube's survey reads zero curvature at every spot, with a spread of zero. Like flat ground, the tube has constant curvature.
5. `hyperbolic-rings` (entry, await none) state: preset="hyperbolic-one-metre", progress=1  
   *Disc map of the hyperbolic plane with a 1 metre ring; notebook: ring length 7.3840 metres, playground length 6.2832 metres, missing fraction −17.5201 per cent.*  
   Say: “Constant curvature comes in three kinds: like a ball, like flat ground, and a third kind. The third kind fits in no ordinary room. So it is shown as a flat disc map, like a world map of a globe. It is called the hyperbolic plane. Every small ring on it comes out too long by the same fraction. On this one, that fraction is the one a ball of radius 1 metre makes rings too short by. Walkers step out 1 metre, and the tape along the solid orange ring reads 7.4 metres, not 6.3. Step out 5 metres, and the ring is 466 metres long, because neighbouring walks spread apart faster and faster.”  
   Describe: On the hyperbolic plane with curvature radius 1 metre, a ring of 1 metre walks is 7.38 metres long, too long by 17.5 per cent. A ring of 5 metre walks is 466 metres long.

### `map-from-one-spot` · for [[riemann-tensor-in-normal-coordinates]] · entry

1. `draw-the-map` (entry, await none) state: preset="earth-ten-kilometres", progress=1  
   *Earth with 10 kilometre walks from the peg and their ring; the map panel draws each walk as a straight ray at true length, with the dashed orange map circle; notebook: ring length 62831.8273 metres, playground length 62831.8531 metres, shortfall 25.800 millimetres.*  
   Say: “The peg is a front door on Earth, treated as a smooth ball. Walkers go straight 10 kilometres in every direction. The map panel on the right draws each walk as a straight line out from the door's dot, at its true length and direction. Their ends form the dashed orange map circle, 62.8 kilometres around. The tape on the ground reads 26 millimetres less. Along every walk the map is exact; sideways, from one walk to the next, it goes wrong.”  
   Describe: A flat map drawn from a door on Earth places the ends of 10 kilometre walks on a circle 62.8 kilometres around. The tape along the ground ring reads 26 millimetres less.
2. `predict-twice-as-far` (entry, await prediction) state: preset="earth-twenty-kilometres", progress=0; evidences `riemann-tensor-in-normal-coordinates/problems/twice-as-far`  
   *Earth with 20 kilometre walks starting from the door; no ring yet.*  
   Predict: “The walkers now go 20 kilometres instead of 10. The fraction by which the ground ring falls short of the map circle was about 4 parts in 10 million. By what factor does it grow?”  
   Say: “Now the walkers go 20 kilometres. With 10 kilometres, the ground ring fell short of the map circle by about 4 parts in 10 million. Guess first. Twice the walk: by what factor does that fraction grow?”  
   Describe: The walks are doubled to 20 kilometres. A prediction is asked for: by what factor the missing fraction grows.
3. `four-times-the-fraction` (entry, await none) state: preset="earth-twenty-kilometres", progress=1  
   *The 20 kilometre ring and its map circle; notebook: shortfall 206.397 millimetres, missing fraction 0.000164 per cent, four times the 10 kilometre fraction.*  
   Say: “The ground ring is now 206 millimetres short of the map circle. The fraction is about 16 parts in 10 million, four times bigger for twice the walk. A ring 10 times smaller falls short by a fraction 100 times smaller. So close to the door the map's error fades away fast. In that sense the map is exact at the door.”  
   Describe: At 20 kilometres the shortfall is 206 millimetres and the missing fraction is 16 parts in 10 million, four times the fraction at 10 kilometres.
4. `predict-a-cleverer-map` (entry, await prediction) state: preset="earth-ten-kilometres", progress=1; evidences `riemann-tensor-in-normal-coordinates/checks/a-cleverer-map-maker`  
   *Back to the 10 kilometre map with its dashed orange circle and the 26 millimetre shortfall.*  
   Predict: “A map-maker says she can draw a flat map of everything within 10 kilometres of her door with every ground distance correct to scale, using a cleverer method than straight walks. Is she right?”  
   Say: “Back to the 10 kilometre map. A map-maker says she can draw a flat map of everything within 10 kilometres of her door with every ground distance correct to scale. She just needs a cleverer method than straight walks. Is she right?”  
   Describe: The 10 kilometre map is shown again. A prediction is asked for: whether any flat map of the patch can keep every ground distance correct.
5. `no-map-hides-the-shortfall` (entry, await none) state: preset="tube-unrolled", progress=1  
   *The paper tube with its unrolled sheet and map panel; notebook: shortfall 0.000 millimetres, the map circle and the ground ring equal.*  
   Say: “She is not. On any map with every distance correct, the places 10 kilometres from the door would sit 10 kilometres from the door's dot, on a circle 62.8 kilometres around. Going around that circle in short hops, each hop correct, the ground ring would add up to 62.8 kilometres too. But the tape on the ground reads 26 millimetres less, and no drawing changes the ground. A paper tube is different: its map, the unrolled sheet shown here, has zero shortfall, because nothing stretched.”  
   Describe: No flat map of a patch of a ball can keep every distance correct, because the ground ring is shorter than any such map's circle. On a paper tube the unrolled sheet is an exact map with zero shortfall.
6. `the-metric-near-the-door` (working, await none) state: preset="plot-football", progress=1  
   *Football with the small-ring plot: the grey line of slope K over 6 through the origin.*  
   Say: “In the map's coordinates, normal coordinates, the metric at the door is the identity with zero first derivatives, and its second derivatives are the Riemann tensor: g equals delta minus one third R x x, plus smaller terms. Integrating around the map circle gives the ring length 2 pi rho times 1 minus K rho squared over 6, which is the grey line on the plot. The map's leftover error at second order is the curvature.”  
   Describe: The plot's line of slope K over 6 is the second-order term of the metric in normal coordinates, where the Riemann tensor is what survives of the metric's second derivatives.

### `ricci-scalar-of-a-surface` · for [[ricci-scalar]] · working

1. `twice-the-gaussian-curvature` (working, await none) state: preset="football-short-string", progress=1  
   *Football with the 5 centimetre ring; on-demand rows: Gaussian curvature from this ring 79.77 per square metre, Ricci scalar of this surface 159.55 per square metre.*  
   Say: “For a surface there is one plane at each point, so its Ricci scalar is 2 times its Gaussian curvature. The notebook's Ricci scalar row reads 159.5 per square metre beside the curvature row's 79.8. On a ball of radius a the Ricci scalar is 2 over a squared, positive in our conventions, and the small-ring law can be read as: missing fraction equals R times rho squared over 12.”  
   Describe: The notebook shows a Gaussian curvature of 79.8 per square metre and a Ricci scalar of 159.5, twice as much, for a ring on the football.
2. `predict-moving-the-peg` (working, await prediction) state: preset="ball-centre-moved", progress=0; evidences `ricci-scalar/checks/sphere-diagonal-sum`  
   *Football with the peg at latitude 30 degrees, no ring yet.*  
   Predict: “In coordinates theta and phi a student finds the Ricci components 1 and sine squared theta, adds them, and says the Ricci scalar of the sphere is 1 plus sine squared theta. I move the peg to latitude 30 degrees. Will the Ricci scalar row change?”  
   Say: “A student computes the sphere's Ricci tensor in theta and phi, gets 1 and sine squared theta on the diagonal, adds them, and says the Ricci scalar is 1 plus sine squared theta. I move the peg from the pole to latitude 30 degrees. Guess first. Will the Ricci scalar row change?”  
   Describe: The peg moves to latitude 30 degrees. A prediction is asked for: whether the Ricci scalar reading depends on the latitude.
3. `same-everywhere` (working, await none) state: preset="ball-centre-moved", progress=1  
   *The ring at latitude 30; Ricci scalar row unchanged at 159.55 per square metre.*  
   Say: “The row is unchanged at 159.5 per square metre. The sine squared theta in the component belongs to the coordinates: the phi direction's basis vector shrinks toward the pole, and g phi phi shrinks with it. The trace must be taken with the inverse metric, which divides the sine squared away and leaves 2 over a squared at every point.”  
   Describe: At latitude 30 the Ricci scalar row still reads 159.5 per square metre. Tracing with the inverse metric removes the sine squared factor, so the scalar is the same at every point of the sphere.
4. `sign-follows-the-ring` (working, await none) state: preset="saddle-centre", progress=1  
   *Saddle with its too-long ring; Ricci scalar row −1.989 per square metre.*  
   Say: “On the saddle, where the ring is too long, the Ricci scalar row reads minus 1.99 per square metre. The sign follows the ring: positive where small rings come out short, negative where they come out too long. One caution: 2 times the Gaussian curvature is the Ricci scalar of a surface only. In three-dimensional space it is a total over three rings at right angles, which can be zero while every ring is off.”  
   Describe: On the saddle the Ricci scalar reads minus 1.99 per square metre. The rule Ricci scalar equals twice the Gaussian curvature holds for surfaces only; in space it becomes a total over three rings.

### `no-perfect-town-map` · for [[theorema-egregium]] · entry

1. `predict-the-town-map` (entry, await prediction) state: preset="earth-five-kilometres", progress=0; evidences `theorema-egregium/checks/perfect-town-map`  
   *Earth with 5 kilometre walks starting from the peg and the map panel open; no ring yet.*  
   Predict: “A town covers a round area 5 kilometres in radius on a smooth Earth. Its mapmaker says the town is too small for the curving to matter, so her flat map is exactly to scale everywhere. Can it be?”  
   Say: “The peg is the centre of a town, and the walkers will go 5 kilometres, the town's radius. The map panel draws each walk at its true length. The town's mapmaker says the town is far too small for Earth's curving to matter, so her flat map is exactly to scale everywhere. Guess first. Can it be?”  
   Describe: Walkers are about to pace 5 kilometres from a town centre on a smooth Earth. A prediction is asked for: whether a flat map of the town can be exactly to scale everywhere.
2. `three-millimetres-short` (entry, await none) state: preset="earth-five-kilometres", progress=1  
   *The 5 kilometre ring and its dashed orange map circle; notebook: ring length 31415.9233 metres, playground length 31415.9265 metres, shortfall 3.225 millimetres.*  
   Say: “The map circle is 31,415.9 metres around, and the tape along the ground ring reads 3.2 millimetres less. Nobody could see that error on a town map. But an exactly to-scale map, enlarged to full size, would be the town's ground laid flat without stretching. Gauss's theorem says bending without stretching never changes the ring test's number, the Gaussian curvature. Flat paper's number is zero and Earth's is not, so no flat map of the town is exact, only very nearly.”  
   Describe: The ground ring is 3.2 millimetres shorter than the map's circle of 31,415.9 metres. The error is invisible on a town map, but it cannot be zero, because a flat sheet cannot be bent to fit a ball without stretching.
3. `a-continent` (entry, await none) state: preset="earth-thousand-kilometres", progress=1  
   *Earth with a 1,000 kilometre ring and its map circle; notebook: ring length 6257417.44 metres, playground length 6283185.31 metres, missing fraction 0.4101 per cent.*  
   Say: “Now the walkers go 1,000 kilometres, the size of a country. The ground ring is 6,257 kilometres, and the map circle is 6,283 kilometres: 26 kilometres too long, 0.4 per cent. For a continent the errors are large. That is why on many world maps Greenland looks as big as Africa, which has 14 times its area.”  
   Describe: For 1,000 kilometre walks the ground ring is 6,257 kilometres and the map circle 6,283, an error of 26 kilometres, 0.4 per cent.
4. `the-tube-keeps-its-number` (entry, await none) state: preset="tube-unrolled", progress=1  
   *The paper tube with its unrolled sheet beside it; notebook: shortfall 0.000 millimetres.*  
   Say: “The tube is the other half of the theorem. Bending the sheet into a tube changed no length along the paper, so every ring keeps its playground length and the ring test's number stays zero. Bend a surface however you like without stretching, and the number at each spot stays. Stretching is the only way to change it, which is why orange peel tears when pressed flat.”  
   Describe: Rolling a sheet into a tube changes no ring length, so the ring test's number stays zero. Bending without stretching never changes it; only stretching can.

## Design rules

- **Draw the string pressed to the surface at every point, and label the walk distance as measured along the surface; never draw or mention a straight line through the air to the ball's middle.** Because: Learners otherwise take the ring's radius to be the distance through the air and keep the 6.28 rule. Prevents `circumference-to-radius-test/misconceptions/radius-through-the-air`.
- **On the saddle and the hyperbolic plane offer only walkers, and say once that a tight string would lift off the surface there.** Because: A string pulled tight on a surface of negative curvature does not lie along a straight walk, so a string ring there would be a rule that cannot be carried out.
- **Keep the saddle one click away from the ball and report its ring as too long, in words and with a minus sign.** Because: Learners who only ever see the ball believe curvature can only shorten a ring. Prevents `circumference-to-radius-test/misconceptions/curving-only-shortens`.
- **Whenever the tube is on screen, offer the unrolled sheet beside it with the same peg, string and ring.** Because: Seeing the ring as an ordinary circle on the flat sheet dissolves the belief that a bent sheet is curved for the surveyors. Prevents `intrinsic-geometry/misconceptions/looks-bent-so-curved`.
- **Hiding the outside view must leave every readout unchanged, and the notebook must still tell the ball from the plain.** Because: The switch shows that surveyors can find their world's shape without leaving it. Prevents `intrinsic-geometry/misconceptions/insiders-cannot-tell`.
- **Show the ring length, shortfall and fraction only when the ring has closed.** Because: A half-drawn ring has no length to compare, and a running number invites reading a partial ring as a result.
- **Label the curvature row 'from this ring', hide it together with the matching ball, the recovered radius and the Ricci scalar whenever the ring is not one simple loop (the tube with a string longer than half its circumference, the ball at the far pole excepted), and keep the small-ring plot one click away.** Because: The missing fraction of a ring that has split into two loops around the tube is large although the tube is flat; the law reads curvature only from one small loop.
- **Keep a ball of twice the radius one click away with the same string, and let the missing fraction drop to a quarter on screen.** Because: Learners expect a ball twice as wide to curve half as strongly. Prevents `gaussian-curvature/misconceptions/wider-ball-linearly-gentler`.
- **The survey tint must come from the small-ring curvature at each spot, so the tube tints white all over next to the egg's varying orange.** Because: Learners believe a tube that bends around but not along cannot have the same curving everywhere. Prevents `space-of-constant-curvature/misconceptions/tube-bends-so-not-constant`.
- **In survey mode, show the egg's tint deepening toward the tips and the survey spread readout beside it.** Because: A smooth, rounded shape looks as if it curves the same everywhere. Prevents `space-of-constant-curvature/misconceptions/smooth-round-means-uniform`.
- **Let the peg move over the ball, and keep every readout identical wherever it sits.** Because: The crowded painted lines near a globe's poles make learners think the poles curve more. Prevents `curvature-of-the-two-sphere/misconceptions/poles-curve-more`.
- **Label the Ricci scalar row 'of this surface', and say in its tour that in three-dimensional space the Ricci scalar is a total over three rings at right angles.** Because: Learners otherwise carry 'twice the Gaussian curvature' into space and spacetime, where it is false. Prevents `ricci-scalar/misconceptions/twice-gaussian-everywhere`.
- **The map panel must draw every straight walk at its true length and show the map circle's length beside the ground ring's length.** Because: Seeing the map exact along every walk and wrong sideways is what shows that no cleverer map removes the error. Prevents `riemann-tensor-in-normal-coordinates/misconceptions/a-cleverer-map-could-fix-it`.
- **Report the shortfall in millimetres so that a town-sized ring shows a nonzero error instead of rounding to zero.** Because: A readout of zero would confirm the belief that a small map can be exactly to scale. Prevents `theorema-egregium/misconceptions/small-maps-can-be-perfect`.
- **Distinguish the string, the walks, the ground ring and the map circle by line style as well as colour: solid blue, thin dotted blue, solid orange, dashed orange.** Because: Colour alone fails for colour-blind learners and in print.

## Model

The ring is the geodesic circle of radius $\rho$ (the walk distance measured along the surface) about the peg. Its length $C$ is closed-form on the plain, the ball, the tube and the hyperbolic plane, and is computed by geodesic shooting on the egg (away from its tips) and the saddle. The notebook reports $C$, the playground length $2\pi\rho$, the shortfall $2\pi\rho - C$, the missing fraction, the ratio $C/\rho$, the small-ring curvature estimate $3(2\pi\rho - C)/(\pi\rho^3)$ and the readouts built from it, plus the ball radius solved exactly from $C = 2\pi a\sin(\rho/a)$. On the ball the walk distance is clamped to $\pi a$. The survey tint uses the closed-form Gaussian curvature of each surface at every spot.

**Playground length**

$$
C_0 = 2\pi\rho
$$

Holds when: Flat plain; also the length of the ring's circle on the map drawn from the centre.

**Ring on a ball**

$$
C(\rho) = 2\pi a\sin\frac{\rho}{a},\qquad 0 \le \rho \le \pi a
$$

Holds when: Sphere of radius $a$; the walk is clamped to $\pi a$, where the ring is the far pole. Independent of where the peg sits.

**Ring on the hyperbolic plane**

$$
C(\rho) = 2\pi a\sinh\frac{\rho}{a}
$$

Holds when: Constant curvature $K = -1/a^2$.

**Ring on a paper tube**

$$
C(\rho) = \begin{cases} 2\pi\rho & \rho \le \pi a \\ 4\rho\,\arcsin\dfrac{\pi a}{\rho} & \rho > \pi a \end{cases}
$$

Holds when: Cylinder of radius $a$, unrolled to the plane with $x$ identified modulo $2\pi a$; the set of points at surface distance $\rho$ from the peg is one circle for $\rho \le \pi a$ and two closed loops around the tube for $\rho > \pi a$. Continuous at $\rho = \pi a$ and tending to $4\pi a$ as $\rho \to \infty$.

**Small-ring law**

$$
C(\rho) = 2\pi\rho - \frac{\pi}{3}K(p)\,\rho^3 + O(\rho^4),\qquad \frac{2\pi\rho - C}{2\pi\rho} = \frac{K\rho^2}{6} + O(\rho^3)
$$

Holds when: Smooth surface, peg at a smooth point $p$, ring a single simple loop; the plot panel's grey line has slope $K(p)/6$.

**Curvature from one ring**

$$
K_{\rm est} = \frac{3\,(2\pi\rho - C)}{\pi\rho^3} = \frac{6}{\rho^2}\cdot\frac{2\pi\rho - C}{2\pi\rho}
$$

Holds when: Reported only when the ring is one simple loop; equals $K(p)$ in the limit $\rho \to 0$ and differs from it at finite $\rho$ by the higher-order terms.

**Matching ball radius**

$$
r_{\rm m} = \frac{1}{\sqrt{|K_{\rm est}|}}
$$

Holds when: Hidden when $K_{\rm est} = 0$; for negative $K_{\rm est}$ it is the ball whose ring falls short by the fraction this ring is too long.

**Ball radius recovered from one ring**

$$
2\pi a\sin\frac{\rho}{a} = C \quad\Longrightarrow\quad a
$$

Holds when: Ball only. $a\sin(\rho/a)$ increases with $a$ for $\rho/a \in (0, \pi)$, so the root is unique; at the far pole $C = 0$ gives $a = \rho/\pi$.

**Ricci scalar of a surface**

$$
R = 2K
$$

Holds when: Two dimensions only; a sphere of radius $a$ has $R = +2/a^2$. The row reports $2K_{\rm est}$.

**Gaussian curvature of the egg**

$$
K(u) = \frac{c^2}{\big(b^2\sin^2 u + c^2\cos^2 u\big)^2},\qquad x = b\cos u\cos\phi,\; y = b\cos u\sin\phi,\; z = c\sin u
$$

Holds when: Spheroid with half-width $b$ and half-length $c = \text{aspect}\times b$; at a tip $K = c^2/b^4$, at the widest part $K = 1/c^2$. Survey spread $= c^2/b^4 - 1/c^2$ for $c > b$.

**Saddle surface and its curvature**

$$
z = \frac{x^2 - y^2}{2R},\qquad K = -\frac{1}{R^2}\left(1 + \frac{x^2 + y^2}{R^2}\right)^{-2}
$$

Holds when: Over $|x|, |y| \le 0.5R$; the peg sits at the centre, where $K = -1/R^2$. Survey spread $= (1 - 4/9)/R^2 = 5/(9R^2)$, between the centre and the corners at $x^2 + y^2 = R^2/2$.

**Ring length by shooting**

$$
C(\rho) = \int_0^{2\pi} \left|\frac{\partial\gamma_\alpha(\rho)}{\partial\alpha}\right| d\alpha
$$

Holds when: $\gamma_\alpha$ is the unit-speed geodesic leaving the peg at angle $\alpha$; used on the egg away from its tips and on the saddle. At an egg tip the ring is the parallel at meridian arc length $\rho$, with $C = 2\pi b\cos u$.

**Method:** Closed forms on the plain, ball, tube and hyperbolic plane. On the egg and the saddle, fourth-order Runge–Kutta integrates the geodesic equation in surface coordinates ($u, \phi$ on the spheroid, $x, y$ on the Monge patch) from the peg in $N$ launch directions to arc length $\rho$, and the ring length is the length of the polyline through the endpoints, with $N$ chosen so the relative error is below $10^{-6}$; at an egg tip the meridian arc length is inverted by quadrature. The recovered radius is found by bisection on $a\sin(\rho/a)$. The survey tint samples the closed-form curvature on a grid, and the spread is its maximum minus its minimum over the drawn patch. Readouts computed with this method are cross-checked on a sphere against the closed form.

| Test | State | Expect | Hidden | Note |
| --- | --- | --- | --- | --- |
| `plain-flat-gives-zero` | preset="plain-string", progress=1 | ring-length = 0.3141593 ±1e-07; playground-length = 0.3141593 ±1e-07; shortfall = 0 ±1e-09; missing-fraction = 0 ±1e-09; ring-over-walk = 6.2831853 ±1e-06; curvature-estimate = 0 ±1e-09 | matching-ball-radius, recovered-radius, survey-spread | Flat case: every ring has its playground length; no matching ball exists, and the recovered radius is a ball-only row. |
| `football-short-string` | preset="football-short-string", progress=1 | ring-length = 0.303717 ±1e-06; shortfall = 10.442218 ±0.001; missing-fraction = 3.323861 ±0.0001; curvature-estimate = 79.772668 ±0.001; matching-ball-radius = 0.111963 ±1e-05; recovered-radius = 0.1114 ±1e-06; ricci-scalar = 159.545337 ±0.001 | survey-spread | $2\pi a\sin(\rho/a)$ with $a = 0.1114$ m, $\rho = 0.05$ m. The estimate is one per cent below $1/a^2 = 80.58$ because the ring is not tiny. |
| `football-double-string` | preset="football-double-string", progress=1 | ring-length = 0.5472702 ±1e-06; shortfall = 81.048305 ±0.001; missing-fraction = 12.899238 ±0.0001; recovered-radius = 0.1114 ±1e-06 | — | Doubling the string gives 3.88 times the missing fraction, close to the small-ring factor 4. |
| `football-equator-string` | preset="football-equator-string", progress=1 | ring-length = 0.6999468 ±1e-06; playground-length = 1.0995574 ±1e-06; ring-over-walk = 3.9996962 ±1e-06; recovered-radius = 0.1114 ±1e-06 | — | A string of $0.175$ m on a ball $0.700$ m around reaches the equator to within a hundredth of a degree; the ring is the equator, four times the walk. |
| `small-string-leading-order` | preset="football-tiny-string", progress=1 | curvature-estimate = 80.580437 (rel 0.0001); missing-fraction = 0.001343 ±1e-07; shortfall = 8.438e-05 ±1e-08 | — | Small-size limit: with $\rho/a = 0.009$ the estimate matches $1/a^2$ to $4\times10^{-6}$, since the next term is $\rho^2/(20a^2)$ relative. |
| `marble-two-millimetres` | preset="marble-two-millimetres", progress=1 | curvature-estimate = 9980.019037 ±0.01; missing-fraction = 0.665335 ±1e-05; recovered-radius = 0.01 ±1e-06 | — | Marble of radius 1 cm; the estimate is $0.2$ per cent below $1/a^2 = 10000$ because $\rho/a = 0.2$. |
| `football-two-millimetres` | preset="football-two-millimetres", progress=1 | curvature-estimate = 80.579138 ±0.001; missing-fraction = 0.005372 ±1e-06 | — | Same string on the football: the marble's estimate is 123.9 times this one, against $(11.14/1)^2 = 124.1$ for the true curvatures. |
| `ball-to-the-far-pole` | preset="ball-to-the-far-pole", progress=1 | ring-length = 0 ±1e-06; missing-fraction = 100 ±1e-06; recovered-radius = 0.1 ±1e-06 | — | Boundary case: the walk is clamped to $\pi a$, the ring is the far pole, and $a = \rho/\pi$. |
| `ball-centre-moved` | preset="ball-centre-moved", progress=1 | ring-length = 0.303717 ±1e-06; missing-fraction = 3.323861 ±0.0001; recovered-radius = 0.1114 ±1e-06; ricci-scalar = 159.545337 ±0.001 | — | Every spot of a ball is alike: identical to football-short-string. |
| `earth-one-kilometre` | preset="earth-one-kilometre", progress=1 | shortfall = 0.0258 ±0.0001; missing-fraction = 4.1061e-07 ±1e-10; recovered-radius = 6371000 (rel 1e-06) | — | Earth as a smooth ball of radius 6371 km: a 1 km ring is 0.026 mm short. |
| `earth-five-kilometres` | preset="earth-five-kilometres", progress=1 | playground-length = 31415.9265 ±0.001; shortfall = 3.224953 ±0.0001 | — | Town-sized ring: 3.2 mm short of the map circle. |
| `earth-ten-kilometres` | preset="earth-ten-kilometres", progress=1 | playground-length = 62831.8531 ±0.001; shortfall = 25.799623 ±0.0001; missing-fraction = 4.10614e-05 ±1e-10 | — | The map circle is 62.8 km around and the ground ring 25.8 mm shorter. |
| `earth-twenty-kilometres-quadruples` | preset="earth-twenty-kilometres", progress=1 | shortfall = 206.396905 ±0.001; missing-fraction = 0.000164245 ±1e-09 | — | Twice the walk: the missing fraction is 4.0000 times the 10 km value to five figures. |
| `earth-thirty-kilometres` | preset="earth-thirty-kilometres", progress=1 | ring-length = 188494.8626 ±0.001; shortfall = 696.589 ±0.01 | — | A 30 km ring on Earth is 188.5 km long and 70 cm short. |
| `earth-thousand-kilometres` | preset="earth-thousand-kilometres", progress=1 | ring-length = 6257417.44 ±1; shortfall = 25767863.4 ±10; missing-fraction = 0.410108 ±1e-05; recovered-radius = 6371000 (rel 1e-06) | — | A country-sized ring: 26 km short of the map circle, 0.41 per cent; the recovered radius is still exact. |
| `moon-to-the-equator` | preset="moon-to-the-equator", progress=1 | ring-length = 4000000 ±1; playground-length = 6283185.3072 ±0.01; ring-over-walk = 4 ±1e-06; recovered-radius = 636619.77 ±0.01 | — | A moon of radius $2000/\pi$ km: a 1000 km walk reaches the equator, 4000 km around. Hiding the outside view changes no readout. |
| `notebook-only-football` | preset="notebook-only-football", progress=1 | ring-length = 0.5472702 ±1e-06; ring-over-walk = 5.4727023 ±1e-06 | — | Design rule notebook-unchanged-when-hidden: same numbers as football-double-string. |
| `notebook-only-tube` | preset="notebook-only-tube", progress=1 | ring-length = 0.3141593 ±1e-07; ring-over-walk = 6.2831853 ±1e-06; missing-fraction = 0 ±1e-09 | matching-ball-radius, recovered-radius | The tube's notebook cannot be told from the plain's. |
| `tube-short-string` | preset="tube-short-string", progress=1 | ring-length = 0.3141593 ±1e-07; shortfall = 0 ±1e-09; curvature-estimate = 0 ±1e-09 | matching-ball-radius, recovered-radius | A tube is intrinsically flat: $\rho = 0.05 < \pi a = 0.15$ m, so the ring is one circle of playground length. |
| `tube-long-string-splits` | preset="tube-long-string", progress=1 | ring-length = 0.6784497 ±1e-06; missing-fraction = 46.010691 ±0.0001 | curvature-estimate, matching-ball-radius, recovered-radius, ricci-scalar | Boundary case: $\rho = 0.2 > \pi a = 0.15$ m, two loops of total length $4\rho\arcsin(\pi a/\rho)$; the curvature rows are hidden because the ring is not one small loop. |
| `saddle-centre` | preset="saddle-centre", progress=1 | ring-length = 0.6293598 ±5e-06; shortfall = -1.0413 ±0.005; missing-fraction = -0.165728 ±0.001; curvature-estimate = -0.994367 ±0.005; ricci-scalar = -1.988734 ±0.01; matching-ball-radius = 1.002828 ±0.003 | recovered-radius | Geodesic shooting on $z = (x^2 - y^2)/2$ with $\rho = 0.1$ m: the ring is too long; the leading-order fraction is $-\rho^2/6R^2 = -0.1667$ per cent and the estimate is $0.6$ per cent below $\|K\| = 1$ because $K$ weakens away from the centre. |
| `egg-tip` | preset="egg-tip", progress=1 | ring-length = 0.01251965 ±2e-07; missing-fraction = 0.371807 ±0.002; matching-ball-radius = 0.01339 ±2e-05; curvature-estimate = 5577.1 ±3 | recovered-radius | Spheroid $b = 2$ cm, $c = 3$ cm, tip, $\rho = 2$ mm: the ring is the parallel at meridian arc length $\rho$. True $K = c^2/b^4 = 5625$; the estimate is $0.85$ per cent low at this $\rho$. |
| `egg-widest` | preset="egg-widest", progress=1 | ring-length = 0.01255705 ±2e-07; missing-fraction = 0.074141 ±0.002; matching-ball-radius = 0.029986 ±5e-05; curvature-estimate = 1112.1 ±3 | recovered-radius | Widest part of the same egg by shooting: true $K = 1/c^2 = 1111.1$; the tip's fraction is 5.01 times this one. |
| `egg-halfway` | preset="egg-halfway", progress=1 | ring-length = 0.01254851 ±2e-07; curvature-estimate = 2132.2 ±3 | — | Latitude 45 on the egg by shooting: true $K = c^2/(b^2\sin^2 u + c^2\cos^2 u)^2 = 2130.2$. |
| `hyperbolic-one-metre` | preset="hyperbolic-one-metre", progress=1 | ring-length = 7.3840069 ±1e-06; shortfall = -1100.821566 ±0.001; missing-fraction = -17.520119 ±0.0001 | recovered-radius | $2\pi\sinh 1$: the ring is too long, so the shortfall and the fraction are negative. |
| `hyperbolic-five-metres` | preset="hyperbolic-five-metres", progress=1 | ring-length = 466.232522 ±0.001; ring-over-walk = 93.246504 ±0.0001 | — | $2\pi\sinh 5$: each extra metre multiplies the ring by about 2.7. |
| `hyperbolic-surveyors` | preset="hyperbolic-surveyors", progress=1 | ring-length = 12650.31413 ±0.001; curvature-estimate = -1.0020019e-08 ±1e-12; matching-ball-radius = 9990.0055 ±0.01; ricci-scalar = -2.0040038e-08 ±2e-12 | recovered-radius | Curvature radius 10 km, $\rho = 2$ km: negative estimate $-0.01002$ per km$^2$ against the true $-0.0100$; both signs of the signed rows are now covered. |
| `survey-ball-uniform` | preset="survey-ball", progress=1 | survey-spread = 0 ±1e-09 | — | Constant curvature: the same $K = 1/a^2$ at every spot. |
| `survey-tube-uniform` | preset="survey-tube", progress=1 | survey-spread = 0 ±1e-09 | — | Constant curvature zero everywhere, like flat ground. |
| `survey-egg-varies` | preset="survey-egg", progress=1 | survey-spread = 4513.888889 ±0.01 | — | $c^2/b^4 - 1/c^2 = 5625 - 1111.1$ per m$^2$ for $b = 2$ cm, $c = 3$ cm. |
| `survey-saddle-varies` | preset="survey-saddle", progress=1 | survey-spread = 0.555556 ±1e-06 | — | $\|K\|$ runs from $1/R^2$ at the centre to $(4/9)/R^2$ at the corners of the drawn patch, $R = 1$ m. |
| `no-readouts-while-drawing` | preset="football-short-string", progress=0.5 | — | ring-length, playground-length, shortfall, missing-fraction, ring-over-walk | Design rule readouts-only-when-the-ring-closes. |

## Serves

- [[circumference-to-radius-test]]: the string and walker rings on the plain, the ball, the tube and the saddle, the shortfall and missing-fraction readouts, the doubling of the string, the small-ring plot, and the split ring on the tube as the limit of the law
- [[intrinsic-geometry]]: the outside-view switch: the notebook alone tells the ball from the plain but not the tube from the plain, and the unrolled sheet beside the tube
- [[gaussian-curvature]]: the egg presets with the matching-ball and curvature rows, the marble against the football, and the saddle's negative reading
- [[curvature-of-the-two-sphere]]: the recovered-radius row, the same for every string length up to the far pole, and the peg moved over the ball with nothing changing
- [[space-of-constant-curvature]]: the survey mode with its spread readout on the ball, the egg, the tube and the saddle, and the hyperbolic disc map with rings that grow as two pi a sinh of rho over a
- [[riemann-tensor-in-normal-coordinates]]: the map panel drawn from the peg with every walk at true length, the quadrupling of the fraction when the walk doubles, and the plot's slope K over 6 as the second-order term of the metric
- [[ricci-scalar]]: the Ricci scalar row, twice the Gaussian curvature of the surface, unchanged when the peg moves and negative on the saddle
- [[theorema-egregium]]: the map panel on the town-sized and country-sized rings, and the tube whose rings keep their length under bending without stretching

## In the visual network

- **Builds on:** [[two-walkers-set-off-side-by-side]]
- **Leads to:** [[carry-an-arrow-around-a-loop]], [[three-rings-around-a-spot]], [[slide-a-patch-across-a-ball-and-an-egg]]

## Accessibility

Every tour beat has a spoken description of the surface, the distance walked and the ring's length, and the notebook's readouts are announced in words with the sign spelled out as short or too long. The string, the walks, the ground ring and the map circle differ in line style as well as colour, the survey tint is paired with the spread readout, and every control works from the keyboard.

Static alternative: A string pulled tight along a ball from its North Pole to its equator draws the equator as its ring, 70 centimetres long, where the same string on a flat plain draws a ring 110 centimetres long. The notebook shows ring length over distance walked as 4.00 on the ball and 6.28 on the plain.

- `Space`: play or pause the drawing of the ring
- `Left and Right arrows`: scrub the drawing around the peg
- `Up and Down arrows`: lengthen or shorten the walk
- `1 to 6`: choose flat plain, ball, paper tube, saddle, egg, or hyperbolic plane
- `O`: show or hide the outside view
- `M`: show or hide the flat map from the centre
- `P`: show or hide the small-ring plot
- `S`: survey every spot
- `U`: unroll the tube

## Starting material

Earlier course assets: `lesson-measure-curvature-with-a-string`, `manuscript-section-10-normal-coordinates-and-counting`, `manuscript-section-4-8-curvature-bending-local-frames`

The earlier course's string lesson gives the entry storyline and its checks. The exemplar loop visual's surface module (ball, tube, saddle, cone charts with RK4 geodesics) can be shared as a TypeScript module; the egg spheroid, the hyperbolic disc map, the notebook panel, the map and plot panels, the survey tint and the outside-view switch are new work. This entry absorbs the planned visual straight-walks-from-one-spot: its fan of geodesics and flat map are the map panel here.

## Review: novice

**Verdict:** fixed (2026-09-16, revision 2)

**Retell attempt:** If you push a peg into flat ground, tie a string to it and swing it round, the chalk ring is always 6.28 times the string; that is the playground length. On a football the same 5 centimetre string draws a ring about 1 centimetre shorter, and a string reaching the equator draws a ring only 4 times the string instead of 6.28. The ring comes out short because the ball pulls the string's paths together, and a string twice as long misses about four times the fraction. A paper tube looks bent but its ring is exactly the playground length, because you can unroll the paper and nothing stretched. On a saddle the ring comes out a bit too long, which the notebook shows with a minus sign; too short is positive curvature like a ball and too long is negative. On Earth a 30 kilometre walk gives a ring only 70 centimetres short of 188 kilometres, so you would never notice. Surveyors who can never leave their ground can still tell a ball from a plain from the notebook alone, but not a tube from a plain. The matching ball is the ball that would miss the same fraction, and Gaussian curvature is 1 divided by that radius times itself, with a minus sign on a saddle. One ring on a ball also gives you the ball's radius, and it is the same wherever the peg sits. A ball, flat ground and a tube have the same curvature at every spot, an egg does not, and the hyperbolic plane is the third kind where every small ring is too long. A flat map drawn from one door is exact along each walk but its circle is a little longer than the ground ring, and the fraction grows four times when the walk doubles; no cleverer map can fix that, which is why no town map is exactly to scale and Greenland looks too big.

- Stumble: “The distance through the air to the ball's middle is not something anyone on the ball can measure.”: 'Middle' was just used for the equator ('70 centimetres around its middle'); here it means the centre point inside the ball, a second sense of one word.
- Stumble: “the ball draws neighbouring strings together only gently at first”: There is one string on screen; 'neighbouring strings' has no picture until it is said that they are the same string laid in neighbouring directions.
- Stumble: “The peg is on its side, and the solid blue string is 5 centimetres”: 'On its side' reads as lying sideways; the reference (the tube's curved wall) is missing.
- Stumble: “less than half of the 15 centimetres to the back of the tube”: 'To the back of the tube' has no reference: from where, along what.
- Stumble: “I peel off the tape and unroll the sheet”: 'Tape' has been the measuring tape all tour; here it is the sticky tape holding the tube shut, a second sense. 'Taped to a football' and 'rolled into a tube and taped' carry the same double sense.
- Stumble: “This surface is shaped like a saddle.”: Undefined picture for a reader who has not sat on a horse; the shape needs one sentence.
- Stumble: “They walked 10 centimetres out from the peg in every direction and taped the ring at 54.7 centimetres.”: 'Taped the ring at' is surveyors' shorthand; I read it as sticking tape on the ring.
- Stumble: “Ring over distance is exactly 4, which happens when the walk reaches the equator.”: Step taken on trust: nothing says why 4 is the equator's number, and 'its radius is about 637 kilometres' arrives without its sum.
- Stumble: “Now the ring misses only 0.074 per cent, five times less.”: 'Five times less' is a phrase I had to reread; one fifth is the idea.
- Stumble: “The Gaussian curvature row divides 1 by the matching radius times itself: 1,112 per square metre”: With the radius just given as 3.0 centimetres, 1 divided by 3 times 3 is not 1,112; the unit the sum uses is missing.
- Stumble: “The Gaussian curvature row shows 1 over 1 squared with a minus sign”: 'Squared' and '1 over' are working-rung words; every other entry beat says 'times itself' and 'divides 1 by'.
- Stumble: “a matching ball radius of about 1 metre carrying the minus sign”: The notebook row on screen reads 1.0028 metres with no minus sign; the spoken line puts the minus sign on the curvature row. The describe text contradicts the screen.
- Stumble: “The notebook's recovered radius row does the sum from one ring.”: 'The sum' is never shown, so the sentence asks for trust; say what goes in.
- Stumble: “I lengthen the string until it reaches the far pole. ... Every string now ends at the same spot.”: 'The far pole' has no reference on a ball whose only named spot is the peg, and there is one string, not many.
- Stumble: “The peg now sits at latitude 30 degrees instead of the pole”: Latitude 30 needs its reference for a reader who last met latitude in geography class.
- Stumble: “The tube bends around but not along, yet that bend is only for outsiders.”: 'Around' and 'along' lack their reference: around what, along what.
- Stumble: “The third kind is shown as a flat disc map, because it fits in no ordinary room. ... This one matches a ball of radius 1 metre the opposite way.”: 'The third kind' points at a list this tour never gave (it showed a ball, an egg and a tube), 'disc map' arrives with no picture, and 'matches a ball the opposite way' does not say what matches.
- Stumble: “draws each walk from the door's dot as a straight ray”: 'Ray' is an undefined word at entry.
- Stumble: “the places 10 kilometres from the door would sit on a circle 62.8 kilometres around”: Why a circle is a step on trust; the map keeps the 10 kilometres, so the places sit 10 kilometres from the door's dot.
- Stumble: “bending without stretching never changes the ring test's number”: 'The ring test's number' could be the ring length, the missing fraction or the curvature; name it.
- Stumble: “this ring gives a Gaussian curvature of {abs} per square metre, positive”: On the flat plain the row reads zero and the tutor would say 'zero per square metre, positive', which sounds wrong; the Ricci scalar row has the same template.
- Stumble: “across the surface the small-ring curvature varies by {value} per square metre”: For a ball the row reads zero, and 'varies by zero' sounds like a contradiction of the word varies.
- Stumble: “so its far end sits on the equator”: The ball's equator has not been placed relative to the peg; the football's 'middle' was named but not tied to the word equator.
- Fixed: Removed the double sense of 'tape' and 'middle': sticky tape is named as such, the peg is 'stuck to' the football, and the through-the-air distance is to the ball's centre deep inside it.
- Fixed: Gave every direction its reference: the peg in the tube's curved wall, the 15 centimetres from the peg around to the opposite wall, the far pole as the spot opposite the peg, latitude 30 as a third of the way from the equator to the pole, the tube bending around its middle but not along its length, the unrolled sheet to the right of the tube.
- Fixed: Backed the moon reveal with its reasons: 4 is the equator's number because the equator is four times the pole-to-equator walk, and 637 is 4,000 divided by 6.28.
- Fixed: Replaced working-rung words in entry beats: 'squared' and '1 over' became 'times itself' and 'divided by', 'ray' became 'straight line', 'five times less' became 'one fifth', 'does the sum' became 'works the radius out from the string and the ring', and the matching radius is 'in metres' before it is multiplied.
- Fixed: Introduced the three kinds of constant curvature before 'the third kind', likened the disc map to a world map, and said what the hyperbolic plane matches on the 1 metre ball.
- Fixed: Aligned the saddle describe line with the screen: the curvature row, not the matching ball radius, carries the minus sign.
- Fixed: Readout speech: the curvature and Ricci scalar rows say 'with no minus sign' or 'with a minus sign' so zero no longer reads as 'positive'; the survey spread says 'differ by' instead of 'varies by'.
- Fixed: Named the ring test's number as the Gaussian curvature in the town-map beat, and the 'straight walkers stopping places' wording is used for the egg walkers too.
- Concern: short-string (entry): 'Even this small ring comes out short, so the ball is curved everywhere, not only near the equator' is a jump: one small ring at the peg shows curving near the peg, not everywhere. A truer wording is 'so the ball is curved right here at the peg too, not only out by the equator'; every-spot-alike later carries the 'everywhere'.
- Concern: notebook-on-the-tube (entry): 'Every ring these surveyors draw comes out at its playground length ... however many rings they draw' is false for a string longer than 15 centimetres on this tube, where the ring splits and reads 46 per cent short (ring-splits-on-the-tube). The claim needs scoping to rings shorter than halfway around, or to small rings.
- Concern: survey-the-ball (entry) says the survey 'runs the ring test at every spot at once, with 2 millimetre walks', but the model's survey tint uses the closed-form curvature, and survey-the-egg quotes 5,625 and 1,111, not the 2 millimetre ring estimates 5,577 and 1,112 heard in the matching-ball tour. A learner who did both tours will ask why the tip's number changed. Either say the survey uses ever smaller rings, or make the survey numbers the 2 millimetre estimates.
- Concern: predict-the-tube: the prediction says 5 centimetres is 'less than half of' the 15 centimetres to the opposite wall; the condition the model uses is only that the walk is at most the 15 centimetres, so 'half of' is an unexplained extra margin.
- Concern: picture.composition places the notebook panel on the right, and the tours also put the map panel and the unrolled sheet 'on the right'; the layout should say where each sits when several are open, or the spoken 'on the right' will point at the wrong panel.
