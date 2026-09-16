---
type: "visual"
schema_version: 2
id: "paper-rolled-into-a-tube-and-a-cone"
title: "Paper rolled into a tube and a cone"
kind: "interactive-3d"
priority: "core"
status: "specified"
revision: 3
rungs: ["entry", "working"]
serves: ["intrinsic-versus-extrinsic-curvature", "flatness-criterion", "intrinsic-geometry", "second-fundamental-form"]
builds_on: ["paced-ring-on-a-ball-and-a-plain"]
leads_to: ["carry-an-arrow-around-a-loop", "card-touching-a-curved-patch"]
---

# Paper rolled into a tube and a cone

`paper-rolled-into-a-tube-and-a-cone` · interactive-3d · core · specified · rungs: entry, working

> A sheet of paper rolled into a tube or a cone looks bent, yet every length drawn on it stays the same, while a ball changes them.

## What it makes visible

A printed sheet with a string-drawn ring and a triangle rolls into a tube, closes into a cone, or folds into a cube corner, and every length and angle along the paper stays what it was on the flat sheet: the ring length, the triangle's sides and corner sum, and the turn of an arrow carried around the ring, which stays zero. What changes is only what an outsider sees: the gap through the air between the sheet's edges and the tilt of the printed face as one walks across the sheet. Beside them a ball refuses the paper, bunching it into folds, and there the ring comes out short, the corners add up to more than a straight angle, the arrow returns turned, and both tilts are nonzero with a nonzero product. The tip of the cone and the corner of the cube show that a surface can be flat everywhere except at one point, where a loop around that point still turns the arrow by the missing wedge. In the working rung two panels split the same picture into the metric, which never changes under rolling, and the second fundamental form, which does.

## The picture

A printed sheet with a light blue grid lies in the scene, its printed face pale and its blank face grey. A grey dot marks the chosen spot; an orange ring drawn with a string of the chosen length surrounds it, and a green dashed triangle joins three points on the ring. A slider rolls the sheet into a tube, closes a sector into a cone, or folds three squares into a cube corner; a faded flat copy of the sheet, with the same ring and triangle, stays beside it. A purple arrow at the spot shows which way the printed face points, and two short purple arrows one string length away, across and along, show how far it has tilted. A red cardboard arrow is carried around the ring, with faded copies left behind; at the start a grey dashed copy waits to be compared with the returned solid red arrow. On the ball preset the paper disc bunches into folds at its rim and the ring, triangle and arrow are drawn on the ball itself. Readouts list ring length, rim stretch, triangle side, corner sum, edge gap, tilt across, tilt along, tilt product, and, once the walk closes, the turn. Two optional panels show the metric and the second fundamental form in the paper's own coordinates.

| Element | Shows |
| --- | --- |
| Printed sheet with a light blue grid, pale printed face and grey blank face | the paper whose lengths along it never change when it bends without stretching |
| Faded flat copy of the sheet beside the rolled one | the same paper before rolling, for a side-by-side comparison of every drawn length |
| Grey dot and orange ring drawn with a string | the ring test: a ring of points one string length from the spot along the paper |
| Green dashed triangle with corners on the ring | sides and corner angles an ant measures with tape and protractor along the paper |
| Purple arrows at the spot and one string length across and along | the printed-face normal and how it tilts, the bending an outsider sees |
| Red carried arrow with faded copies and a grey dashed start copy | the arrow test around the ring, and the turn, if any, when it closes |
| Ball with a bunched paper disc | a surface no flat paper can cover, where every readout departs from the flat values |
| Metric panel and second fundamental form panel | what rolling keeps and what rolling changes, in the paper's own coordinates |

## Book figure

Three panels. Left: the flat printed sheet with the grey dot, the orange ring of a 4 centimetre string and the green dashed triangle inside it, with the ring length 25.1 cm and corner sum 180 degrees written beside them. Middle: the same sheet rolled into a tube 30 cm around with the printed face outside; the ring wraps around the tube, the same numbers stand beside it, and two purple arrows show the printed face tilting 48 degrees across and 0 degrees along. Right: a ball of radius 10 cm with a paper disc bunched into folds at its rim, and the 4 centimetre ring drawn on the ball with its length 24.5 cm and corner sum 192.5 degrees.

Labels: flat sheet, ring 25.1 cm, corners 180 degrees, tube, 30 cm around, tilt across 48 degrees, tilt along 0 degrees, ball, radius 10 cm, ring 24.5 cm, corners 192.5 degrees, folds. Aspect 3:1. Alt text: A flat sheet with a ring and a triangle drawn on it; the same sheet rolled into a tube, where the ring's length and the triangle's corner sum are unchanged although the printed face tilts across the tube; and a ball on which a paper disc bunches into folds and the same ring comes out shorter with corners adding up to more than 180 degrees.

## Variants

- **static** `static-card` (fallback): The print figure as an SVG card with the three panels and their numbers, used when 3D is unavailable and as a summary card.
- **interactive-2d** `unroll-view-2d`: The flat sheet with the ring and triangle beside an end-on view of the tube or cone as a curve, with the roll slider, the edge gap and the two tilts; no 3D rendering.
- **interactive-3d** `full-3d`: The full experience: rolling, closing and folding in 3D with the faded flat copy, the ball with its bunched disc, the carried arrow, the panels and every preset.

## Parameters

| Id | Label | Type | Options or range | Default | Available when | Effect |
| --- | --- | --- | --- | --- | --- | --- |
| `surface` | Surface | enum | tube, cone, cube-corner, ball | "tube" | — | Chooses the shape. The tube sheet is 20 cm along by 30 cm around, so the closed tube is 30 cm around. The cone sheet is a sector of slant radius 20 cm with the chosen wedge removed. The cube corner is three 20 cm squares sharing a corner. On the ball a paper disc of one string length in radius is pressed onto the ball and bunches at its rim; the ring, triangle and arrow are drawn on the ball itself. |
| `ink-face` | Printed face | enum | outside, inside | "outside" | — | Which face of the paper ends up facing the tube's axis, the cone's axis, the inside of the cube corner, or the ball's centre. It flips the sign of both tilts and of the second fundamental form, and nothing else. |
| `roll` | Roll | number | 0–1 step 0.05 | 1 | surface in tube, cone, cube-corner | How far the sheet is rolled, closed or folded: 0 is the flat sheet, 1 is the closed tube, the closed cone or the finished cube corner with its seam taped. The tube's bend is proportional to roll; the cone's half-angle sine falls from 1 to 1 minus the wedge over a full turn; the cube's two folds each turn by roll times a right angle. Every readout that is a length or angle along the paper is unchanged by roll. |
| `wedge-angle` | Missing wedge | number | 0–240 step 5 deg | 60 | surface in cone | The wedge cut from the disc before its two straight edges are taped together. Zero leaves a flat disc; 240 leaves a sector of 120 degrees, the sharpest cone offered, so the ring around the spot never wraps around the cone. |
| `ball-radius` | Ball radius | number | 5–50 step 1 cm | 10 | surface in ball | Radius of the ball. Bigger balls bring every readout closer to the flat values; the string is kept shorter than a quarter of the way around. |
| `string-length` | String length | number | 1–6 step 0.5 cm | 4 | — | Length of the string tied at the ring's centre and pulled tight along the paper or the ball; it is the ring's radius along the surface and sets the walk length over which the tilts are read. |
| `spot-distance` | Spot distance from the tip | number | 8–14 step 1 cm | 12 | surface in cone, cube-corner | Distance along the paper from the cone's tip, or the cube's corner, to the grey spot, measured along the sector's centre line or the middle face's diagonal. The spot is always farther from the tip than one string length, so the ring around the spot never reaches the tip. |
| `loop` | Where the ring is drawn | enum | around-the-spot, around-the-tip (surface in cone, cube-corner) | "around-the-spot" | — | Centres the ring, the triangle and the carried arrow's walk on the grey spot or on the tip. Choosing the tip sets roll to 1, because that ring crosses the taped seam. The tilt readouts always refer to the grey spot. |
| `walk-direction` | Walking direction | enum | centre-on-left, centre-on-right | "centre-on-left" | — | Which side the ring's centre is on for a walker standing on the printed face. Reversing it mirrors the arrowheads along the ring and changes the sign of the turn. |
| `walk` | Arrow walk | progress | 0–1 step 0.01 | 0 | — | Carries the red arrow around the ring without letting it swing; the turn readout appears only at 1. |
| `panels` | Metric and bending panels | boolean | — | false | — | Shows two panels: the metric in the paper's own coordinates, u across and v along, and the second fundamental form in the same coordinates, with the normal on the printed side. On the ball the panels use an orthonormal frame at the spot and say so. |

## Presets

- `flat-sheet` Flat sheet: surface="tube", roll=0
- `half-rolled-tube` Sheet curled into a trough: surface="tube", roll=0.5
- `tube-ink-outside` Tube, printed face outside: surface="tube", roll=1, ink-face="outside"
- `tube-ink-inside` Tube, printed face inside: surface="tube", roll=1, ink-face="inside"
- `cone-spot` Cone, ring around a spot away from the tip: surface="cone", wedge-angle=60, roll=1, spot-distance=12, loop="around-the-spot"
- `cone-tip` Cone, ring around the tip: surface="cone", wedge-angle=60, roll=1, loop="around-the-tip"
- `cone-tip-reversed` Cone, ring around the tip walked the other way: surface="cone", wedge-angle=60, roll=1, loop="around-the-tip", walk-direction="centre-on-right"
- `cube-face` Cube corner, ring around a spot on a face: surface="cube-corner", roll=1, loop="around-the-spot"
- `cube-tip` Cube corner, ring around the corner: surface="cube-corner", roll=1, loop="around-the-tip"
- `ball` Ball of radius 10 cm: surface="ball", ball-radius=10, string-length=4
- `ball-ink-inside` Ball, printed face inside: surface="ball", ball-radius=10, string-length=4, ink-face="inside"
- `ball-reversed` Ball, ring walked the other way: surface="ball", ball-radius=10, string-length=4, walk-direction="centre-on-right"
- `ball-tiny-ring` Tiny ring on a big ball: surface="ball", ball-radius=50, string-length=1
- `ball-long-string` Long string on a small ball: surface="ball", ball-radius=5, string-length=6

## Readouts

- `ring-length` Ring length along the paper (cm; visible always; 2 decimals): “the ring measured along the surface is {value} centimetres long”
- `rim-stretch` Rim stretch the paper needs (percent; visible always; 4 decimals; range (-100, 100]; sense: positive when the paper's rim must stretch to lie on the surface; negative when it must shrink, so the paper bunches into folds): “the paper's rim fits with {abs} percent of stretch” / “the paper's rim must shrink by {abs} percent to fit, so it bunches into folds”
- `triangle-side` Triangle side along the paper (cm; visible always; 2 decimals): “each side of the triangle is {value} centimetres along the surface”
- `corner-sum` Corner sum (deg; visible always; 1 decimals; range (0, 540]): “the triangle's three corners add up to {value} degrees”
- `edge-gap` Edge gap through the air (cm; visible always; 2 decimals): “the gap through the air between the sheet's free edges is {value} centimetres”
- `tilt-across` Tilt across (deg; visible always; 1 decimals; range (-180, 180]; sense: positive when the paper bends toward its printed face; the bend at the spot times the string length, which is the angle the printed-face normal tilts over one string length walked across the sheet; exact on the tube and the ball, to second order on the cone): “over one string length walked across the surface, the bend toward the printed face is {abs} degrees” / “over one string length walked across the surface, the bend away from the printed face is {abs} degrees”
- `tilt-along` Tilt along (deg; visible always; 1 decimals; range (-180, 180]; sense: positive when the paper bends toward its printed face; the bend at the spot times the string length, which is the angle the printed-face normal tilts over one string length walked along the sheet; exact on the tube and the ball, to second order on the cone): “over one string length walked along the surface, the bend toward the printed face is {abs} degrees” / “over one string length walked along the surface, the bend away from the printed face is {abs} degrees”
- `tilt-product` Tilt product (1; visible always; 4 decimals; range (-10, 10]; sense: positive when both bends go toward the same face of the paper; zero when either bend is zero): “the two tilts, each divided by 57.3 degrees, multiplied together give {value}” / “the two tilts, each divided by 57.3 degrees, multiplied together give minus {abs}, because the bends go toward opposite faces”
- `gauss-curvature` Gaussian curvature (m^-2; visible on-demand; 2 decimals; sense: positive when both bends go toward the same face, as on a ball): “the Gaussian curvature at the spot is {value} per square metre” / “the Gaussian curvature at the spot is minus {abs} per square metre”
- `loop-turn` Turn (deg; visible on-complete; 2 decimals; range (-180, 180]; sense: positive toward the walker's left, for a walker standing on the printed face): “the arrow came back turned {abs} degrees to the walker's left” / “the arrow came back turned {abs} degrees to the walker's right”

## Tours

### `roll-the-poster` · for [[intrinsic-versus-extrinsic-curvature]] · entry

1. `meet-the-sheet` (entry, await none) state: preset="flat-sheet"  
   *Flat printed sheet with the blue grid; grey dot, orange ring of a 4 cm string, green dashed triangle inside it; readouts ring length 25.13 cm, corner sum 180, edge gap 30, tilt across 0, tilt along 0.*  
   Say: “Here is a flat sheet of paper with a blue grid printed on one face. The grey dot is our spot. An ant tied a 4 centimetre string to the dot, pulled it tight along the paper, and drew the orange ring. The ring is 25.1 centimetres long, which is what a 4 centimetre string always gives for a circle on flat paper. Inside the ring she drew the green dashed triangle, with its three corners on the ring.”  
   Describe: A flat sheet with a grid. A ring of radius 4 centimetres is drawn around a dot, with a triangle inside it. The readouts say ring length 25.1 centimetres, corner sum 180 degrees, tilt across 0 degrees, tilt along 0 degrees.
2. `predict-the-ring` (entry, await prediction) state: preset="flat-sheet"; evidences `intrinsic-versus-extrinsic-curvature/checks/lampshade-for-an-ant`  
   *Same flat sheet, paused; the roll slider highlighted.*  
   Predict: “I am about to roll the sheet into a tube, printed face outward, without stretching it. Will the ring the ant measures along the paper get longer, get shorter, or stay 25.1 centimetres?”  
   Say: “Before I roll it, make a guess. I will roll the sheet into a tube, printed face outward, without stretching it. Will the ring the ant measures along the paper get longer, get shorter, or stay 25.1 centimetres?”  
   Describe: The flat sheet waits, with the ring length readout at 25.1 centimetres.
3. `roll-it-up` (entry, await none) state: preset="flat-sheet"; animate roll → 1 over 5 s  
   *The sheet rolls up until its two short edges meet and are taped; the orange ring wraps around the tube; a faded flat copy stays beside it. Ring length stays 25.13; edge gap falls from 30 to 0; tilt across runs from 0 to minus 48.*  
   Say: “I roll the sheet until its two short edges meet, and I tape them. The orange ring now wraps around the tube. The ring length readout stays at 25.1 centimetres the whole time, because no bit of paper stretched. The edge gap readout, the distance through the air between the sheet's two short edges, shrinks from 30 centimetres to zero. The ring length and the corner sum, the numbers the ant measures along the paper, have not changed. The edge gap and the two tilt readouts have, and all three are measured through the air. We come to the tilts next.”  
   Describe: The sheet rolls into a tube 30 centimetres around. The ring length readout stays at 25.1 centimetres. The edge gap readout falls from 30 centimetres to zero, and the tilt across readout from 0 to minus 48 degrees.
4. `predict-the-tilts` (entry, await prediction) state: preset="tube-ink-outside"; evidences `second-fundamental-form/checks/card-on-a-can`  
   *Closed tube, printed face outside; purple normal arrow at the spot, with the two tilt readouts hidden behind a reveal.*  
   Predict: “The purple arrow sticks straight out of the printed face at the spot, so it shows which way that face is facing. Walk 4 centimetres along the tube and stand a second purple arrow straight out of the printed face there. Then do the same after walking 4 centimetres across the sheet, which on the tube means around it. Compared with the arrow at the spot, does the new arrow tilt by the same amount on both walks?”  
   Say: “The purple arrow sticks straight out of the printed face at the spot, so it shows which way that face is facing. Walk 4 centimetres along the tube and stand a second purple arrow straight out of the printed face there. Then do the same after walking 4 centimetres across the sheet, which on the tube means around it. Compared with the arrow at the spot, does the new arrow tilt by the same amount on both walks?”  
   Describe: A closed tube with the spot on its side. A purple arrow at the spot sticks straight out of the printed face.
5. `reveal-the-tilts` (entry, await none) state: preset="tube-ink-outside"  
   *Two short purple arrows one string length from the spot, along and around; tilt along 0.0, tilt across minus 48.0, tilt product 0.*  
   Say: “Along the tube, the short purple arrow 4 centimetres from the spot points the same way as the arrow at the spot, so tilt along reads zero. Across the sheet, around the tube, the short purple arrow has tilted 48 degrees over the 4 centimetre walk. The paper there bends away from its printed face, so tilt across reads minus 48. The tube bends around, and not along. The two tilts multiplied together give zero, and the ant's ring found no change either: 25.1 centimetres, its flat length. Bent, seen from outside, is not the same as curved for the ant.”  
   Describe: The readouts say tilt along 0 degrees, tilt across minus 48 degrees, and tilt product 0. The ring length is still 25.1 centimetres.
6. `predict-the-lampshade` (entry, await prediction) state: preset="cone-spot", roll=0; evidences `intrinsic-versus-extrinsic-curvature/checks/lampshade-for-an-ant`  
   *Flat sector with a 60 degree wedge missing; the spot 12 cm from the tip with its ring and triangle.*  
   Predict: “This flat card, with a wedge cut out, will close into a cone like a lampshade. The spot sits 12 centimetres from the card's centre, which will become the cone's tip. The ant runs the same 4 centimetre ring test there. How long is her ring on the cone?”  
   Say: “Now a different sheet: a flat card with a wedge cut out of it. I will tape the two straight edges together, and it will close into a cone, like a lampshade. The spot sits 12 centimetres from the card's centre, which will become the cone's tip. The ant runs the same 4 centimetre ring test there. How long is her ring on the cone?”  
   Describe: A flat card shaped like a disc with a 60 degree slice missing. The spot with its ring sits 12 centimetres from the centre.
7. `close-the-cone` (entry, await none) state: preset="cone-spot", roll=0; animate roll → 1 over 5 s  
   *The sector closes into a cone; ring length stays 25.13; tilt across reads minus 12.7, tilt along 0, tilt product 0.*  
   Say: “The card closes into a cone. The ring is still 25.1 centimetres, its flat card length, because closing the card stretched nothing. Tilt across, which on the cone means around it, reads minus 12.7 degrees, a smaller tilt than the tube's 48. Tilt along, up the slope toward the tip, reads zero. So the cone is bent, as seen from outside, but for the ant it is not curved.”  
   Describe: The card closes into a cone. The ring length readout stays at 25.1 centimetres. Tilt across reads minus 12.7 degrees and tilt along reads 0 degrees.
8. `ball-is-different` (entry, await none) state: preset="ball"  
   *Ball of radius 10 cm; paper disc bunched into folds at its rim; the ring and triangle drawn on the ball; ring length 24.47, rim stretch minus 2.6454 percent, tilt across and along minus 22.9, tilt product 0.16.*  
   Say: “Here is a ball with a radius of 10 centimetres. No sheet of paper can lie smoothly against it in one layer. A paper disc as wide as the ring bunches into folds at its rim. The readout says its rim must shrink by 2.6 percent to fit. So the ant draws her 4 centimetre ring on the ball itself. It comes out 24.5 centimetres, short of 25.1. Both tilts read minus 22.9 degrees, and their product is not zero. The ball is bent, and for the ant it is also curved.”  
   Describe: A ball of radius 10 centimetres with a paper disc bunched into folds. The readouts say ring length 24.5 centimetres, rim stretch minus 2.6 percent, tilt across minus 22.9 degrees, tilt along minus 22.9 degrees, tilt product 0.16.

### `paper-test-beside-arrow-test` · for [[flatness-criterion]] · entry

1. `paper-fits-the-tube` (entry, await none) state: preset="tube-ink-outside", walk=0  
   *Closed tube with the squared paper lying against it in one layer; the red arrow waits on the orange ring beside its grey dashed start copy.*  
   Say: “The squared paper is the sheet with the blue grid. It lies against the tube in one layer, taped along its seam, with no fold and no stretch. A red cardboard arrow waits on the orange ring, on top of its grey dashed starting copy. I will carry it once around the ring and never let it swing. I walk standing on the printed face, keeping the ring's centre on my left.”  
   Describe: A tube covered by squared paper. A red arrow waits at a point of the ring around the spot, lying on a dashed copy of itself.
2. `carry-around-the-tube-ring` (entry, await none) state: preset="tube-ink-outside", walk=0; animate walk → 1 over 4 s  
   *The red arrow slides around the ring leaving faded copies, keeping its angle to the grid lines; at the end it lies on the dashed copy; turn 0.00.*  
   Say: “The red arrow slides around the ring, keeping its angle to the blue grid lines the whole way. Back at the start it lies exactly on its grey dashed copy. The turn readout says zero degrees. Paper that fits, and an arrow that comes back matching, go together.”  
   Describe: The arrow travels once around the ring and returns pointing the same way. The turn readout says 0 degrees.
3. `predict-the-tiny-square` (entry, await prediction) state: preset="ball-tiny-ring", walk=0; evidences `flatness-criterion/checks/shrink-the-patch`  
   *Ball of radius 50 cm with a 2 cm paper disc; the 1 cm ring around the spot; readouts hidden behind a reveal.*  
   Predict: “A friend presses a tiny piece of squared paper, 2 centimetres across, on a ball with a radius of 50 centimetres. The friend says it lies perfectly against the ball, in one layer, with no stretch at all. Is the friend exactly right?”  
   Say: “Now a ball with a radius of 50 centimetres. A friend presses a tiny piece of squared paper, 2 centimetres across, onto it. The friend says it lies perfectly against the ball, in one layer, with no stretch at all. Is the friend exactly right?”  
   Describe: A large ball with a tiny paper disc pressed on it, and a ring of radius 1 centimetre drawn around the spot.
4. `tiny-but-not-zero` (entry, await none) state: preset="ball-tiny-ring", walk=0; animate walk → 1 over 3 s  
   *Rim stretch minus 0.0067 percent; the arrow walks the 1 cm ring and returns turned 0.07 degrees to the left.*  
   Say: “The rim stretch readout says minus 0.0067 percent. The rim must shrink by about seven parts in a hundred thousand of its length: far too small to see, but not zero. And the red arrow carried around the 1 centimetre ring comes back turned 0.07 degrees to the left. Tiny, not zero. A patch of a ball is never exactly flat, however small.”  
   Describe: The readouts say rim stretch minus 0.0067 percent and turn 0.07 degrees to the left.
5. `bigger-ring-bigger-turn` (entry, await none) state: preset="ball", walk=1  
   *Ball of radius 10 cm with the 4 cm ring; paper disc bunched; rim stretch minus 2.6454 percent; turn 28.42 to the left.*  
   Say: “With a 4 centimetre string on a ball of radius 10 centimetres, the turn grows to 28.4 degrees to the left, and the rim must shrink by 2.6 percent. The paper disc bunches into folds you can see. The two tests fail together, and by matching amounts. From the tiny ring to this one, the turn grew about four hundred times, from 0.07 degrees to 28.4. The shrink grew about four hundred times too, from 0.0067 percent to 2.6.”  
   Describe: A smaller ball with a paper disc bunched into folds. The readouts say rim stretch minus 2.6 percent and turn 28.4 degrees to the left.
6. `cone-away-from-the-tip` (entry, await none) state: preset="cone-spot", walk=1  
   *Closed cone; the ring around the spot 12 cm from the tip; paper lying flat against it; turn 0.00.*  
   Say: “On the cone, away from the tip, the squared paper fits with no fold, and the red arrow carried around the ring comes back matching its grey dashed copy: zero degrees. Every spot on the cone away from its tip passes both tests.”  
   Describe: A cone with a ring around a spot away from the tip. The turn readout says 0 degrees.
7. `predict-the-cube-corner` (entry, await prediction) state: preset="cube-tip", walk=0; evidences `flatness-criterion/problems/cube-corner`  
   *Cube corner made of three folded squares; the ring circles the corner crossing all three faces; the red arrow waits on its dashed copy.*  
   Predict: “Three faces of a cube meet at this corner. The orange ring circles the corner, crossing all three faces. I will carry the red arrow once around it, with the corner on my left as I walk standing on the printed face, outside the cube. Will it come back matching its start?”  
   Say: “Here three square faces fold together into the corner of a cube. The orange ring circles the corner, crossing all three faces. I will carry the red arrow once around it, with the corner on my left as I walk standing on the printed face, outside the cube. Will it come back matching its start?”  
   Describe: Three squares folded into a cube corner. A ring around the corner crosses all three faces, and the arrow waits on it.
8. `a-quarter-turn-at-the-corner` (entry, await none) state: preset="cube-tip", walk=0; animate walk → 1 over 4 s  
   *The arrow crosses the three faces and returns turned 90 degrees to the left; ring length 18.85; rim stretch minus 25 percent.*  
   Say: “The red arrow comes back turned 90 degrees to the left, a quarter turn, though it never swung. The ring is only 18.8 centimetres long, a quarter short of its flat length, so no squared paper can cover the corner without a cut. Every spot away from the corner is flat. The corner itself is not.”  
   Describe: The arrow returns a quarter turn to the left. The readouts say turn 90 degrees to the left, ring length 18.8 centimetres, rim stretch minus 25 percent.

### `curl-the-page` · for [[intrinsic-geometry]] · entry

1. `triangle-on-the-flat-sheet` (entry, await none) state: preset="flat-sheet"  
   *Flat sheet; green dashed triangle with corners on the 4 cm ring; triangle side 6.93 cm, corner sum 180, edge gap 30 cm.*  
   Say: “On this flat sheet the green dashed triangle has three equal sides of 6.9 centimetres and three corners of 60 degrees, so its corner sum is 180 degrees. The edge gap readout, 30 centimetres, is the distance through the air between the sheet's two short edges.”  
   Describe: A flat sheet with a triangle drawn on it. The readouts say triangle side 6.9 centimetres, corner sum 180 degrees, edge gap 30 centimetres.
2. `predict-the-curled-triangle` (entry, await prediction) state: preset="flat-sheet"; evidences `intrinsic-geometry/checks/curled-triangle`  
   *Flat sheet, paused; the roll slider highlighted at 0.*  
   Predict: “I will curl the sheet into a trough, like half of a pipe, without stretching, cutting or taping it. An ant on the paper measures the sides with a tape laid along the paper and the corners with a protractor lying on it. What will she measure afterwards?”  
   Say: “Now guess. I will curl the sheet into a trough, like half of a pipe, without stretching, cutting or taping it. An ant on the paper measures the sides with a tape laid along the paper, and the corners with a protractor lying on it. What will she measure afterwards?”  
   Describe: The flat sheet waits, with the triangle readouts at 6.9 centimetres and 180 degrees.
3. `curl-into-a-trough` (entry, await none) state: preset="flat-sheet"; animate roll → 0.5 over 4 s  
   *The sheet curls into a half-pipe trough; triangle side stays 6.93, corner sum stays 180; edge gap falls from 30 to 19.10; tilt across runs from 0 to minus 24.*  
   Say: “The sheet curls into a trough. The sides stay 6.9 centimetres and the corner sum stays 180 degrees, because her tape and protractor lie against the paper and nothing stretched. The numbers that change, the edge gap and the tilt across, are measured through the air, where the ant cannot go. The gap falls from 30 centimetres down to 19.1 centimetres. For her, the trough and the flat sheet are the same world.”  
   Describe: The sheet curls into a trough. The triangle readouts stay at 6.9 centimetres and 180 degrees. The edge gap readout falls from 30 centimetres to 19.1, and the tilt across readout from 0 to minus 24 degrees.
4. `predict-the-video-claim` (entry, await prediction) state: preset="ball"; evidences `intrinsic-geometry/checks/curved-into-what`  
   *Ball of radius 10 cm with the ring and triangle drawn on it; readouts hidden behind a reveal.*  
   Predict: “A video says space can only be curved if it bends into some extra direction we cannot see. On this ball, does the ant need a view from outside to find that her world is not flat paper?”  
   Say: “Now the ball. A video says space can only be curved if it bends into some extra direction we cannot see. On this ball, does the ant need a view from outside to find that her world is not flat paper?”  
   Describe: A ball with a ring and a triangle drawn on it, and an ant's tape and protractor on the surface.
5. `the-ring-alone-tells` (entry, await none) state: preset="ball"  
   *Ring length 24.47 cm, triangle side 6.88 cm, corner sum 192.5 degrees; the bunched paper disc beside the ring.*  
   Say: “No. Her 4 centimetre ring comes out 24.5 centimetres instead of 25.1, and her triangle's corners add up to 192.5 degrees instead of 180. Both numbers come from her tape and protractor on the ball's surface. The bend into the room is something only we see. The short ring is something she measures, and that is what curved means for her.”  
   Describe: The readouts say ring length 24.5 centimetres, triangle side 6.9 centimetres, corner sum 192.5 degrees.

### `metric-stays-bending-changes` · for [[second-fundamental-form]] · working

1. `panels-on-the-flat-sheet` (working, await none) state: preset="flat-sheet", panels=true  
   *Flat sheet with both panels open: metric panel g = (1, 0; 0, 1) in u across, v along; second fundamental form panel all zeros.*  
   Say: “With the panels open, the left panel shows the metric in the paper's own coordinates, u across the sheet and v along it: one, zero, zero, one, the same at every point. The right panel shows the second fundamental form, with the unit normal on the printed side: every entry zero on the flat sheet.”  
   Describe: Two panels beside the flat sheet. The metric panel reads one, zero, zero, one. The second fundamental form panel reads zero, zero, zero, zero.
2. `predict-the-rolled-sheet-claim` (working, await prediction) state: preset="tube-ink-outside", panels=true; evidences `second-fundamental-form/checks/rolled-sheet-claim`  
   *Closed tube, printed face outside, panels open but their entries hidden behind a reveal.*  
   Predict: “Claim: a sheet rolled into a tube is still flat for anyone living on it, so its second fundamental form is zero. Is the claim right?”  
   Say: “I have rolled the sheet into a tube 30 centimetres around, printed face outside. Here is a claim: a sheet rolled into a tube is still flat for anyone living on it, so its second fundamental form is zero. Is the claim right?”  
   Describe: A closed tube with the two panels beside it, their entries not yet shown.
3. `reveal-the-panels` (working, await none) state: preset="tube-ink-outside", panels=true  
   *Metric panel unchanged (1, 0; 0, 1); second fundamental form panel K u u = minus 0.209 per cm, K v v = 0, K u v = 0; tilt across minus 48.0.*  
   Say: “The metric panel has not changed: one, zero, zero, one. The second fundamental form panel now reads K u u equals minus one over the tube's radius of 4.77 centimetres, that is minus 0.209 per centimetre with the printed-face normal, and K v v equals zero. The tilt across readout shows the same number as an angle: minus 48 degrees over the 4 centimetre string. So the premise of the claim is right and its conclusion is wrong.”  
   Describe: The metric panel still reads one, zero, zero, one. The second fundamental form panel reads minus 0.209 per centimetre, zero, zero, zero. Tilt across reads minus 48 degrees.
4. `flip-the-printed-face` (working, await none) state: preset="tube-ink-inside", panels=true  
   *Tube rolled with the printed face inside; K u u = plus 0.209 per cm; tilt across plus 48.0; metric panel unchanged.*  
   Say: “Rolling the same sheet with the printed face inward puts the bend on the other side of the normal. K u u becomes plus 0.209 per centimetre, and tilt across reads plus 48 degrees: the paper now bends toward its printed face. The metric panel still reads one, zero, zero, one. The sign of the second fundamental form belongs to the choice of normal, not to the paper.”  
   Describe: The tube is now rolled with the printed face inside. The second fundamental form panel reads plus 0.209 per centimetre, zero, zero, zero. Tilt across reads plus 48 degrees. The metric panel is unchanged.
5. `predict-the-cone-bend` (working, await prediction) state: preset="cone-spot", panels=true; evidences `second-fundamental-form/checks/cone-principal-curvature`  
   *Closed cone with the 60 degree wedge; spot 12 cm from the tip; K u u = minus 0.0553 per cm, K v v = 0; tilt across minus 12.7.*  
   Predict: “On the cone, at 12 centimetres from the tip, tilt across reads minus 12.7 degrees. If I move the spot to 8 centimetres from the tip, what will tilt across read?”  
   Say: “On the cone, at 12 centimetres from the tip, the second fundamental form panel reads K u u equals minus 0.0553 per centimetre and K v v equals zero, and tilt across reads minus 12.7 degrees. If I move the spot to 8 centimetres from the tip, what will tilt across read?”  
   Describe: A cone with the spot 12 centimetres from the tip. The second fundamental form panel reads minus 0.0553 per centimetre, zero, zero, zero. Tilt across reads minus 12.7 degrees.
6. `slide-toward-the-tip` (working, await none) state: preset="cone-spot", panels=true; animate spot-distance → 8 over 3 s  
   *The spot slides to 8 cm from the tip; K u u grows to minus 0.0829 per cm; tilt across minus 19.0; metric panel unchanged; tilt product 0.*  
   Say: “The spot slides toward the tip, and K u u grows to minus 0.0829 per centimetre: tilt across reads minus 19.0 degrees, twelve eighths of its old value. On a cone the bend across is the cotangent of the half-angle divided by the distance from the tip, and the bend along the slant is zero everywhere. The metric panel never moves, and the product of the two bends stays zero.”  
   Describe: The spot moves to 8 centimetres from the tip. Tilt across reads minus 19.0 degrees, tilt along 0 degrees, tilt product 0. The metric panel is unchanged.
7. `the-product-the-ant-can-measure` (working, await none) state: preset="ball", panels=true  
   *Ball of radius 10 cm; panels in an orthonormal frame at the spot: metric (1, 0; 0, 1), second fundamental form minus 0.1 per cm on both diagonal entries; Gaussian curvature 100 per square metre; ring 24.47 cm.*  
   Say: “On the ball the panels use an orthonormal frame at the spot. The second fundamental form has minus 0.1 per centimetre on both diagonal entries, so its determinant is one over 100 square centimetres: 100 per square metre. That product is the Gaussian curvature, the one combination of the bends the ant can measure. It shows in her ring, 24.5 centimetres instead of 25.1. Rolling can change each bend, but never this product.”  
   Describe: The second fundamental form panel reads minus 0.1 per centimetre, zero, zero, minus 0.1 per centimetre. The Gaussian curvature readout says 100 per square metre. The ring length readout says 24.5 centimetres.

### `two-bends-and-their-product` · for [[intrinsic-versus-extrinsic-curvature]] · working

1. `tube-bends-one-way` (working, await none) state: preset="tube-ink-outside"  
   *Closed tube; tilt across minus 48.0, tilt along 0.0, tilt product 0; Gaussian curvature 0 on demand.*  
   Say: “On the tube the two principal curvatures are minus one over the radius, 4.77 centimetres, around the tube, and zero along it. Tilt across reads minus 48 degrees, tilt along zero, and their product is zero. Each bend is extrinsic: it changes under rolling and flips sign with the normal. The product is what the ring test reads, and it is zero.”  
   Describe: A closed tube. The readouts say tilt across minus 48 degrees, tilt along 0 degrees, tilt product 0, ring length 25.1 centimetres.
2. `cone-bends-one-way-too` (working, await none) state: preset="cone-spot"  
   *Closed cone; tilt across minus 12.7, tilt along 0.0, tilt product 0; ring length 25.13.*  
   Say: “On the cone the bend across is the cotangent of the half-angle over the distance from the tip, and the bend along the slant is zero. Tilt across reads minus 12.7 degrees, tilt along zero, product zero, and the ring is 25.1 centimetres. A sheet bent without stretching keeps one principal curvature zero at every point, so its Gaussian curvature stays zero.”  
   Describe: A closed cone. The readouts say tilt across minus 12.7 degrees, tilt along 0 degrees, tilt product 0, ring length 25.1 centimetres.
3. `ball-product-matches-the-ring` (working, await none) state: preset="ball"  
   *Ball of radius 10 cm; tilts minus 22.9 and minus 22.9; tilt product 0.16; Gaussian curvature 100 per square metre; rim stretch minus 2.6454 percent.*  
   Say: “On the ball both principal curvatures are minus one over 10 centimetres, so both tilts read minus 22.9 degrees and their product, in radians, is 0.16: the Gaussian curvature, one over 100 square centimetres, times the string length squared. To leading order the ring falls short by that product over six, 2.67 percent; the exact readout says 2.65. The product is the intrinsic number, and the ring test reads it.”  
   Describe: A ball of radius 10 centimetres. The readouts say tilt across minus 22.9 degrees, tilt along minus 22.9 degrees, tilt product 0.16, rim stretch minus 2.6 percent.
4. `flip-the-normal-keep-the-product` (working, await none) state: preset="ball-ink-inside"  
   *Ball with the printed face inside; tilts plus 22.9 and plus 22.9; tilt product 0.16 unchanged.*  
   Say: “Pressing the paper with its printed face against the ball reverses the normal. Both tilts now read plus 22.9 degrees, yet the product is still 0.16. Reversing the normal reverses both principal curvatures and leaves their product, and the ring, untouched.”  
   Describe: The same ball with the printed face inward. The readouts say tilt across plus 22.9 degrees, tilt along plus 22.9 degrees, tilt product 0.16.

## Design rules

- **Whenever roll is above zero, keep a faded flat copy of the sheet, with the same ring and triangle, beside the rolled sheet.** Because: Seeing one ring on both sheets, with one readout, turns 'bent but not curved' from a claim into a comparison the learner makes. Prevents `intrinsic-versus-extrinsic-curvature/misconceptions/bent-means-intrinsically-curved`.
- **Compute ring length, triangle side and corner sum from the flat sheet once, and never re-animate or re-round them while rolling.** Because: A readout that even flickers during rolling suggests the ant's measurements respond to the bend. Prevents `intrinsic-geometry/misconceptions/looks-bent-so-curved`.
- **Show tilt across, tilt along and their product side by side, and never the product alone.** Because: The tube's zero product beside its nonzero tilt across shows that a tube bends although it is intrinsically flat. Prevents `second-fundamental-form/misconceptions/tube-has-no-bending`.
- **On the ball, draw the paper disc bunched into folds at its rim and keep the rim stretch readout visible; never draw paper lying smooth on the ball.** Because: Paper that appears to fit a ball would show the very thing the visual denies. Prevents `intrinsic-versus-extrinsic-curvature/misconceptions/sheet-bends-any-way`.
- **Report rim stretch to four decimals of a percent and the turn to two decimals of a degree, so the tiny ring on the big ball shows small numbers and never zero.** Because: A small patch of a ball is never exactly flat; a readout rounded to zero would say the opposite. Prevents `flatness-criterion/misconceptions/tiny-patch-is-flat`.
- **Draw the cone's tip and the cube's corner as sharp points, keep the grey spot away from them, and offer the ring around the tip one click from the ring around the spot.** Because: The two rings side by side show a surface flat at every spot yet with a loop that turns the arrow, so zero curvature on a region says nothing about loops around a missing point. Prevents `flatness-criterion/misconceptions/one-flat-grid-everywhere`.
- **Never show the turn while the red arrow is moving; show it only when the walk completes.** Because: Arrows at different points cannot be compared independently of the route; the turn exists only when the loop closes.
- **Choosing the ring around the tip sets roll to 1 and shows the taped seam; the ring is drawn across the seam only when the seam is closed.** Because: A ring around the tip is intact only once the two edges are taped, and a ring broken by a gap would give a length that means nothing.
- **Distinguish the start and returned arrows, and the printed and blank faces, by line style and texture as well as colour.** Because: Colour alone fails for colour-blind learners and in print.

## Model

Every surface except the ball is a developable surface built from a flat sheet by an isometry: rolling, closing a sector, or folding, so lengths and angles along the paper are computed once on the flat sheet and mapped through the embedding. The tilts are the principal curvatures at the grey spot, with the unit normal on the printed side, times the string length. The ring, triangle and turn on the ball come from spherical trigonometry and the area rule. Readouts that are undefined in a state are hidden: the edge gap on the ball, and the turn until the walk completes. Coordinates on the paper are arc lengths $u$ across and $v$ along, so the metric is $\delta_{\mu\nu}$ for every roll, and at the grey spot $u$, $v$ are principal directions on every surface offered. Each tilt readout is the bend at the spot times the string length; the short purple arrow one string length away is drawn with the true normal there, which matches the readout exactly on the tube and the ball and to second order on the cone.

**Bends of the rolled sheet**

$$
\kappa_u = \pm\frac{2\pi f}{W},\qquad \kappa_v = 0
$$

Holds when: Tube sheet of width $W = 30$ cm around; roll fraction $f$; sign $+$ when the printed face is inside, $-$ when it is outside. The tube's radius is $W/2\pi f$.

**Bends of the closing sector**

$$
\sin\alpha' = 1 - \frac{f\,\delta}{2\pi},\qquad \kappa_u = \pm\frac{\cot\alpha'}{s},\qquad \kappa_v = 0
$$

Holds when: Missing wedge $\delta$; roll $f$; $s$ the distance from the tip to the spot along the paper, with the spot never at the tip; same sign rule as the tube. At $f = 1$ the cone has half-angle $\alpha$ with $\sin\alpha = 1 - \delta/2\pi$.

**Tilt readouts**

$$
\text{tilt}_u = \kappa_u\,\rho,\qquad \text{tilt}_v = \kappa_v\,\rho,\qquad \text{tilt product} = \kappa_u\kappa_v\,\rho^2 = K\rho^2
$$

Holds when: String length $\rho$; by Weingarten's equation the printed-face normal tilts by $\kappa\rho$ over a walk of length $\rho$ along a principal direction. The cube corner's faces have $\kappa_u = \kappa_v = 0$. The readout is this product; the drawn arrow one string length away along the parallel shows the true normal, whose angle to the arrow at the spot is exactly $\kappa\rho$ on the tube and on the ball (a great circle) and, on the cone, $\arccos\big(\sin^2\alpha + \cos^2\alpha\cos(\rho/s\sin\alpha)\big)$: 12.61 against 12.67 degrees at the cone-spot preset, 18.80 against 19.00 at 8 cm, and 116.6 against 121.5 at the extreme wedge 240, spot 8 cm, string 6 cm.

**Second fundamental form in paper coordinates**

$$
K_{\mu\nu} = \hat{\mathbf n}\cdot\partial_\mu\partial_\nu\mathbf X,\qquad K_{uu} = \kappa_u,\quad K_{vv} = \kappa_v,\quad K_{uv} = 0,\qquad g_{\mu\nu} = \delta_{\mu\nu}
$$

Holds when: $\hat{\mathbf n}$ the unit normal on the printed side, so $K_{\mu\nu}$ is positive where the surface bends toward the printed face, as in the course convention $K_{\mu\nu} = n\cdot\partial_\mu\partial_\nu X$. On the ball the panels use an orthonormal frame at the spot, where $K_{\mu\nu} = \pm\delta_{\mu\nu}/a$.

**Gaussian curvature at the spot**

$$
K = \kappa_u\kappa_v = \frac{\det K_{\mu\nu}}{\det g_{\mu\nu}}
$$

Holds when: Zero on the tube, the cone away from its tip, and the cube faces; $+1/a^2$ on a ball of radius $a$. Reported in per square metre from centimetre inputs, multiplying by ten thousand.

**Gap through the air between the free edges**

$$
d_{\rm tube} = W\,\frac{\sin \pi f}{\pi f},\qquad d_{\rm cone} = 2L\sin\alpha'\,\sin\frac{2\pi - \delta}{2\sin\alpha'},\qquad d_{\rm cube} = \sqrt{2}\,L\cos\frac{\pi f}{2}
$$

Holds when: Chord distance between the far ends of the two edges that meet at roll 1. Sheet width $W = 30$ cm; slant radius and face size $L = 20$ cm; at $f = 0$ the tube gap is $W$ and the cube gap is $\sqrt 2 L$; every gap is $0$ at $f = 1$. Hidden on the ball.

**Ring and triangle around a spot**

$$
C = 2\pi\rho,\qquad \sigma = \sqrt 3\,\rho,\qquad \Sigma = \pi
$$

Holds when: Tube, cone away from the tip, and cube faces, for every roll, because rolling and folding are isometries. Rim stretch is $(C - 2\pi\rho)/2\pi\rho$, zero here. The triangle's corners sit on the ring at bearings one third of a turn apart.

**Ring and triangle around a tip**

$$
C = (2\pi - \delta)\,\rho,\qquad \sigma = 2\rho\sin\frac{2\pi - \delta}{6},\qquad \Sigma = \pi + \delta
$$

Holds when: Cone with wedge $\delta$ at roll 1, or cube corner with $\delta = \pi/2$; the three corners at distance $\rho$ from the tip, one third of the remaining angle apart; each side is the straight segment in the development of the two faces or the sector it crosses. Rim stretch is $-\delta/2\pi$.

**Ring and triangle on the ball**

$$
C = 2\pi a\sin\frac{\rho}{a},\qquad \cos\frac{\sigma}{a} = \cos^2\frac{\rho}{a} - \tfrac12\sin^2\frac{\rho}{a},\qquad \cos A = \frac{\cos(\sigma/a)}{1 + \cos(\sigma/a)},\qquad \Sigma = 3A
$$

Holds when: String shorter than a quarter of the way around, $\rho < \pi a/2$. Small rings: rim stretch $\approx -\rho^2/6a^2 = -\text{tilt product}/6$.

**Turn of the arrow carried around the ring**

$$
\Delta\alpha = \iint_S K\,dA + \sum_{\text{tips in } S}\delta_i \pmod{2\pi}
$$

Holds when: Region $S$ on the walker's left, for a walker standing on the printed face; positive toward the walker's left. Ball: $2\pi(1 - \cos(\rho/a))$ when the centre is on the left, its negative when on the right. Tip: $\pm\delta$. Tube, cone away from the tip, cube faces: $0$. Reported on $(-180^\circ, 180^\circ]$; exactly $-180^\circ$ is reported as $180$.

**Method:** Closed form throughout. The paper surfaces are drawn by mapping the flat sheet through the isometric embedding of the tube, the partly closed cone, or the folded squares; the ring, triangle and carried arrow are computed in the flat development, where transport is translation and folds change nothing, and mapped to 3D. On the ball the ring and triangle use spherical trigonometry and the arrow is transported along the small circle by the exact rotation. The two short purple arrows stand one string length from the spot, across along the parallel or around the tube and along the generator or axis, and carry the true unit normal there. The turn is reduced to the reported branch. The component clamps the spot and string so that the ring never reaches a tip and never crosses the seam of a still-open sheet.

| Test | State | Expect | Hidden | Note |
| --- | --- | --- | --- | --- |
| `flat-sheet-values` | preset="flat-sheet", walk=0 | ring-length = 25.1327412 ±0.0001; rim-stretch = 0 ±1e-09; triangle-side = 6.9282032 ±0.0001; corner-sum = 180 ±1e-06; edge-gap = 30 ±1e-06; tilt-across = 0 ±1e-09; tilt-along = 0 ±1e-09; tilt-product = 0 ±1e-09; gauss-curvature = 0 ±1e-09 | loop-turn | The flat case: every bend zero, the gap equal to the sheet's width, and no turn shown before the walk. |
| `tube-printed-face-outside` | preset="tube-ink-outside", walk=1 | ring-length = 25.1327412 ±0.0001; rim-stretch = 0 ±1e-09; corner-sum = 180 ±1e-06; edge-gap = 0 ±1e-09; tilt-across = -48 ±1e-06; tilt-along = 0 ±1e-09; tilt-product = 0 ±1e-09; loop-turn = 0 ±1e-09 | — | Tube 30 cm around: $\kappa_u = -2\pi/30$ per cm, times 4 cm is $-0.8378$ rad $= -48^\circ$; along-the-paper readouts unchanged; no turn. |
| `tube-printed-face-inside` | preset="tube-ink-inside", walk=1 | tilt-across = 48 ±1e-06; tilt-along = 0 ±1e-09; tilt-product = 0 ±1e-09; ring-length = 25.1327412 ±0.0001; loop-turn = 0 ±1e-09 | — | Flipping the printed face flips the sign of the tilt and nothing else. |
| `trough-halfway` | preset="half-rolled-tube", walk=0 | edge-gap = 19.0985932 ±0.0001; tilt-across = -24 ±1e-06; triangle-side = 6.9282032 ±0.0001; corner-sum = 180 ±1e-06 | loop-turn | Half rolled: the sheet is a half-pipe, gap $30\sin(\pi/2)/(\pi/2) = 19.10$ cm, tilt half the closed value. |
| `tube-long-string` | preset="tube-ink-outside", string-length=6, walk=1 | ring-length = 37.6991118 ±0.0001; tilt-across = -72 ±1e-06; triangle-side = 10.3923048 ±0.0001; loop-turn = 0 ±1e-09 | — | The tilt scales with the string length; the ring stays its flat length. |
| `cone-spot-values` | preset="cone-spot", walk=1 | ring-length = 25.1327412 ±0.0001; corner-sum = 180 ±1e-06; edge-gap = 0 ±1e-09; tilt-across = -12.6685735 ±0.0001; tilt-along = 0 ±1e-09; tilt-product = 0 ±1e-09; loop-turn = 0 ±1e-09 | — | Wedge 60: $\sin\alpha = 5/6$, $\cot\alpha = 0.6633$, over 12 cm gives $0.05528$ per cm, times 4 cm is $0.2211$ rad $= 12.67^\circ$, away from the printed face. |
| `cone-half-closed` | preset="cone-spot", roll=0.5, walk=0 | edge-gap = 10.3301938 ±0.0001; tilt-across = -8.3266941 ±0.0001; ring-length = 25.1327412 ±0.0001 | loop-turn | Half closed: $\sin\alpha' = 11/12$; the gap is the chord between the sector's edges on the wider cone. |
| `cone-spot-nearer-the-tip` | preset="cone-spot", spot-distance=8, walk=1 | tilt-across = -19.0028603 ±0.0001; tilt-product = 0 ±1e-09; loop-turn = 0 ±1e-09 | — | The bend across grows as one over the distance from the tip: $12/8$ times the 12 cm value. |
| `cone-without-a-wedge-is-a-disc` | preset="cone-spot", wedge-angle=0, roll=0.5, walk=1 | tilt-across = 0 ±1e-09; edge-gap = 0 ±1e-09; loop-turn = 0 ±1e-09 | — | Boundary: with no wedge removed the sector is a full disc, its edges coincide, and roll cannot bend it. |
| `cone-tip-ring` | preset="cone-tip", walk=1 | ring-length = 20.943951 ±0.0001; rim-stretch = -16.6666667 ±0.0001; triangle-side = 6.1283555 ±0.0001; corner-sum = 240 ±1e-06; loop-turn = 60 ±1e-06; tilt-across = -12.6685735 ±0.0001 | — | Around the tip: ring $(2\pi - \delta)\rho$, one sixth short; corners $180 + 60$; the arrow turns by the wedge. The tilts still refer to the grey spot. |
| `cone-tip-ring-walked-the-other-way` | preset="cone-tip-reversed", walk=1 | loop-turn = -60 ±1e-06; ring-length = 20.943951 ±0.0001 | — | Reversing the walk reverses the turn: 60 degrees to the right. |
| `half-turn-branch-boundary` | preset="cone-tip-reversed", wedge-angle=180, walk=1 | loop-turn = 180 ±1e-06; corner-sum = 360 ±1e-06; rim-stretch = -50 ±1e-06 | — | A half turn to the right is reported as 180, never as minus 180. |
| `widest-wedge-wraps` | preset="cone-tip", wedge-angle=240, walk=1 | loop-turn = -120 ±1e-06; ring-length = 8.3775804 ±0.0001; corner-sum = 420 ±1e-06 | — | A turn of 240 degrees to the left wraps to 120 degrees to the right on the branch; the corner sum is not reduced. |
| `cube-face-values` | preset="cube-face", walk=1 | ring-length = 25.1327412 ±0.0001; tilt-across = 0 ±1e-09; tilt-along = 0 ±1e-09; edge-gap = 0 ±1e-09; loop-turn = 0 ±1e-09 | — | A spot on a face of the folded corner is flat, and a ring that crosses a fold keeps its flat length. |
| `cube-unfolded-and-half-folded` | preset="cube-face", roll=0.5, walk=0 | edge-gap = 20 ±1e-06; corner-sum = 180 ±1e-06 | loop-turn | Half folded, each fold at 45 degrees: gap $\sqrt 2 \cdot 20\cos 45^\circ = 20$ cm; unfolded it would be $28.28$ cm. |
| `cube-corner-ring` | preset="cube-tip", walk=1 | ring-length = 18.8495559 ±0.0001; rim-stretch = -25 ±1e-06; triangle-side = 5.6568542 ±0.0001; corner-sum = 270 ±1e-06; loop-turn = 90 ±1e-06 | — | Three right angles meet, a missing wedge of 90 degrees: the ring is a quarter short and the arrow turns a quarter turn. |
| `ball-values` | preset="ball", walk=1 | ring-length = 24.4678761 ±0.0001; rim-stretch = -2.6454144 ±0.0001; triangle-side = 6.8798034 ±0.0001; corner-sum = 192.4847497 ±0.0001; tilt-across = -22.9183118 ±0.0001; tilt-along = -22.9183118 ±0.0001; tilt-product = 0.16 ±1e-08; gauss-curvature = 100 ±1e-06; loop-turn = 28.4180422 ±0.0001 | edge-gap | Radius 10 cm, string 4 cm: ring $2\pi\cdot10\sin 0.4$; both bends $-1/10$ per cm; turn $2\pi(1 - \cos 0.4)$ rad; the edge gap has no meaning on the ball. |
| `ball-printed-face-inside` | preset="ball-ink-inside", walk=1 | tilt-across = 22.9183118 ±0.0001; tilt-along = 22.9183118 ±0.0001; tilt-product = 0.16 ±1e-08; loop-turn = 28.4180422 ±0.0001 | edge-gap | Reversing the normal reverses both bends and keeps their product; the turn, defined by the region on the walker's left, is unchanged. |
| `ball-walked-the-other-way` | preset="ball-reversed", walk=1 | loop-turn = -28.4180422 ±0.0001 | edge-gap | With the centre on the walker's right the region on the left is the rest of the ball: $4\pi - $ cap, which is $-$cap modulo $2\pi$. |
| `tiny-ring-leading-order` | preset="ball-tiny-ring", walk=1 | rim-stretch = -0.0066665 ±1e-06; tilt-product = 0.0004 ±1e-10; loop-turn = 0.0719976 ±1e-06; corner-sum = 180.0297752 ±1e-06 | edge-gap | Small-size limit: rim stretch equals minus the tilt product over six to leading order ($-0.006667$ percent against $-0.0066665$), and nothing rounds to zero at the reported precision. |
| `long-string-wraps-the-turn` | preset="ball-long-string", walk=1 | loop-turn = -130.4487916 ±0.0001; tilt-across = -68.7549354 ±0.0001; rim-stretch = -22.3300762 ±0.0001; corner-sum = 347.3202729 ±0.0001 | edge-gap | Radius 5 cm, string 6 cm: the cap turn $229.57^\circ$ to the left wraps to $130.45^\circ$ to the right on the branch. |
| `no-turn-while-walking` | preset="ball", walk=0.5 | — | loop-turn, edge-gap | Design rule no-running-turn. |

## Serves

- [[intrinsic-versus-extrinsic-curvature]]: the roll slider with the flat copy beside the rolled sheet, the tilt readouts that change while the ring length does not, and the ball where both tilts and their product are nonzero
- [[flatness-criterion]]: the squared paper lying against the tube and cone beside the carried arrow that returns matching, the ball where the paper bunches and the arrow returns turned, and the tip and cube-corner rings where paper fails at a single point
- [[intrinsic-geometry]]: the triangle's sides and corner sum that survive curling into a trough while the edge gap through the air shrinks
- [[second-fundamental-form]]: the metric and second fundamental form panels in paper coordinates, the sign flip with the printed face, and the cone's bend growing toward the tip

## In the visual network

- **Builds on:** [[paced-ring-on-a-ball-and-a-plain]]
- **Leads to:** [[carry-an-arrow-around-a-loop]], [[card-touching-a-curved-patch]]

## Accessibility

Every tour beat has a spoken description of the surface, the ring and the readouts. Lengths and angles are announced in centimetres and degrees, tilts as toward or away from the printed face, and the turn as degrees to the left or right. Printed and blank faces differ in texture as well as colour, the start and returned arrows differ in line style, and every control works from the keyboard.

Static alternative: A flat sheet with a ring and a triangle drawn on it is rolled into a tube. The ring's length and the triangle's corner sum stay the same, while the printed face tilts across the tube and not along it. On a ball a paper disc bunches into folds, the same ring comes out shorter, the corners add up to more than 180 degrees, and an arrow carried around the ring comes back turned.

- `Left and Right arrows`: roll, close or fold the sheet
- `Space`: play or pause the arrow's walk around the ring
- `1 to 4`: choose tube, cone, cube corner, or ball
- `F`: flip the printed face inside or outside
- `T`: move the ring between the spot and the tip
- `R`: reverse the walking direction
- `P`: show or hide the metric and bending panels

## Starting material

Earlier course assets: `scene-3d-parallel-transport-loop`, `lesson-measure-curvature-with-a-string`, `manuscript-section-4-8-curvature-bending-local-frames`

The earlier course's transport scene already carries an arrow on a plane, a tube and a cone in their unrolled charts, and its string-ring lesson gives the ring test; both can be ported as TypeScript modules. New work: the rolling, closing and folding animations with the faded flat copy, the ball with its bunched disc, the tilt arrows, the tip and cube-corner rings, and the metric and second fundamental form panels. Merges the earlier proposal 'curl a page with a triangle' as the trough preset and the curl-the-page tour.

## Review: novice

**Verdict:** fixed (2026-09-16, revision 3)

**Retell attempt:** A sheet with a grid on one side gets rolled into a tube and taped, and an ant with a 4 centimetre string draws a ring that stays 25.1 centimetres long, because rolling does not stretch paper. Only the gap between the edges changes. On the tube a purple arrow sticking out of the paper tilts by 48 degrees if you go around the tube but not if you go along it, and the two tilts multiplied together are zero, which somehow matches the ring being unchanged. A cone made from a card with a wedge cut out is the same: ring still 25.1. A ball is different: paper wrinkles on it, the ring comes out shorter, and both tilts are nonzero. Then a red arrow carried around the ring, keeping its angle to the grid, comes back exactly the same on the tube and on the cone, but on a ball it comes back turned, even a tiny bit on a huge ball. On a cube corner the ring around the corner is a quarter short and the arrow comes back turned a quarter turn, so the corner point is not flat although every face is. The triangle keeps its 6.9 centimetre sides and 180 degrees when the sheet curls into a trough, but on a ball its corners add up to 192.5. So 'bent' is what we see from outside and 'curved' is what the ant measures, and only the ball is curved for the ant.

- Stumble: “The ring is 25.1 centimetres long, as any circle with that string is on flat paper.”: I reread it twice: 'as any circle with that string is' does not say what the ring is being compared with.
- Stumble: “The edge gap readout shrinks from 30 centimetres to zero.”: Nobody in this tour has said what the edge gap is; I only find out in the curl-the-page tour.
- Stumble: “The purple arrow at the spot shows which way the printed face points. Now walk 4 centimetres along the tube, then 4 centimetres around it. Does the purple arrow tilt by the same amount on both walks?”: A face does not point, and the arrow at the spot never moves, so I could not picture what tilts. I also did not know who walks or where the second arrow comes from, and the readout I am predicting is called 'tilt across' while the say line says 'around'.
- Stumble: “Along the tube the purple arrow keeps its direction, so tilt along reads zero.”: The say line does not name what is on screen: two short purple arrows have appeared, and I did not know which purple arrow is meant.
- Stumble: “Around the tube it tilts by 48 degrees over the 4 centimetre walk, away from the printed face, so tilt across reads minus 48.”: 'It' is the arrow, but what goes away from the printed face is the paper's bend, so I read the arrow as tilting away from the face and got the picture wrong.
- Stumble: “The tube bends one way only.”: 'One way' could mean one direction or one line; I took it as 'only toward the blank face'.
- Stumble: “The two tilts multiplied together give zero, and zero is what the ant's ring found.”: The ant's ring found 25.1 centimetres, not zero, so I stopped to work out what 'zero' meant.
- Stumble: “the two tilts, in radians, multiplied together give {value}”: I do not know radians, and multiplying the two readouts I can see, minus 22.9 and minus 22.9, gives 524, not 0.16.
- Stumble: “The spot sits 12 centimetres from the tip.”: On the flat card there is no tip yet, and the describe line says 'from the centre', so I looked for a tip on the flat card.
- Stumble: “The ring is 25.1 centimetres again, its flat card length,”: 'Again' sounds as if the ring changed and came back, but the readout never moved.
- Stumble: “Tilt across reads minus 12.7 degrees, less than on the tube, and tilt along reads zero.”: Across what, on a cone? And minus 12.7 is bigger than minus 48, so 'less than' made me pause.
- Stumble: “No sheet of paper can lie against it: the paper disc bunches into folds at its rim,”: My first what-if: surely a small enough piece lies against a ball? And 'the paper disc' had not been introduced, so I did not know how big it is.
- Stumble: “The squared paper lies against the tube in one layer,”: Until now the paper was 'the sheet with the blue grid'; 'squared paper' sounded like a new object.
- Stumble: “keeping the ring's centre on my left, and never let it swing.”: Left for whom, standing where? On a tube I could be inside or outside.
- Stumble: “The rim must shrink by about seven millionths of its length: far too small to see, but not zero.”: I checked with a calculator: 0.0067 percent is 0.0067 per hundred, which is 67 millionths, not seven. Not changed, because it is a number; listed in concerns.
- Stumble: “The two tests fail together, and they fail by matching amounts.”: 28.4 degrees and 2.6 percent do not look like matching amounts, and nothing tells me how to compare them, so I took it on trust.
- Stumble: “I will carry the red arrow once around it, with the corner on my left.”: Left for whom, standing where? The corner of a cube has an inside and an outside.
- Stumble: “Only the edge gap changes, from 30 centimetres down to 19.1.”: The unit dropped off the second number, so I heard '19.1' and wondered 19.1 what.
- Stumble: “Both numbers come from her tape and protractor on the ground.”: The ball has been 'the ball' all along; 'the ground' sounded like a different surface.
- Stumble: “the paper's rim must stretch by {abs} percent to fit”: On the flat sheet this reads 'must stretch by 0 percent to fit', which sounds wrong when nothing needs to stretch.
- Stumble: “walking one string length across, the paper bends {abs} degrees toward its printed face”: Across what? And on the flat sheet it reads 'bends 0 degrees toward its printed face', which sounds like a bend.
- Stumble: “the arrow came back turned {abs} degrees to the left”: Whose left? The walker's, standing on the printed face, but the readout alone does not say.
- Fixed: Reworded 'as any circle with that string is' in meet-the-sheet.
- Fixed: Defined the edge gap where it is first spoken, in roll-it-up.
- Fixed: Rewrote predict-the-tilts (say, predict, describe) so the arrow sticks out of the face, the walker stands a second arrow at the end of each walk, and 'across the sheet' is tied to 'around the tube'.
- Fixed: Rewrote reveal-the-tilts to name the short purple arrows, put the 'away from the printed face' on the paper's bend, replace 'bends one way only', and say what the ring found instead of 'zero'.
- Fixed: Replaced 'from the tip' with 'from the card's centre, which will become the cone's tip' in predict-the-lampshade (say and predict).
- Fixed: Replaced 'again' with 'still' and added the across and along references in close-the-cone.
- Fixed: Scoped 'no sheet of paper can lie against it' to 'smoothly, in one layer' and sized the paper disc in ball-is-different.
- Fixed: Named the squared paper as the grid sheet and gave 'my left' its reference in paper-fits-the-tube and predict-the-cube-corner.
- Fixed: Added a bridge after 'matching amounts' in bigger-ring-bigger-turn.
- Fixed: Restored the unit on 19.1 in curl-into-a-trough and replaced 'the ground' with 'the ball's surface' in the-ring-alone-tells.
- Fixed: Reworded the rim-stretch, tilt-across, tilt-along and loop-turn say templates so zero values read naturally and every direction has its reference; the tilt-product templates now say 'each divided by 57.3 degrees' instead of 'in radians'.
- Fixed: Split the long sentences the validator flagged in reveal-the-tilts, ball-is-different and paper-fits-the-tube.
- Concern: tiny-but-not-zero says the rim must shrink 'by about seven millionths of its length', but the readout minus 0.0067 percent is 0.0067 per hundred, about 67 millionths (6.7 parts in a hundred thousand). Left unchanged because it is a number; the physics reviewer should correct it.
- Concern: The tilt readouts are visible_when 'always', so during roll-it-up the tilt across readout visibly runs from 0 to minus 48, and during curl-into-a-trough to minus 24. That contradicts 'That gap is the only number that has changed so far' and 'Only the edge gap changes'; either hide the tilts until reveal-the-tilts and in the curl-the-page tour, or change the claim to name the tilt as a second through-the-air number.
- Concern: The tilt-product readout is the product of the two tilts in radians; I reworded it as 'each divided by 57.3 degrees' to keep it checkable at entry without the word radian. The physics reviewer should confirm the rounding wording is acceptable or prefer a working-only readout.
- Concern: Templates with {abs} still read 'turned 0 degrees to the walker's left' and 'the bend toward the printed face is 0 degrees' at zero; a say_zero template, if the schema allowed one, would read better.
- Concern: 'They fail by matching amounts' in bigger-ring-bigger-turn is a quantitative claim the entry learner cannot check from the two readouts shown; I added a bridge rather than weaken it, but the physics reviewer may prefer to drop 'matching amounts'.
- Concern: Readout labels 'Tilt across' and 'Tilt along' carry no reference on the label itself; the say templates now say 'across the surface' and 'along the surface', and the entry beats tie across to around the tube or cone.

**Re-read** (2026-09-16, revision 3)

- Fixed: Read every changed spoken line. "The numbers that change, the edge gap and the tilt across, are measured through the air, where the ant cannot go" keeps the point of the beat and now names both readouts that move. "From the tiny ring to this one, the turn grew about four hundred times, from 0.07 degrees to 28.4" replaces a bare claim of matching amounts with two numbers a listener can check. No stumble; nothing changed.
- Fixed: Editor sign-off, not an agent: the run that would have done this stopped at the monthly spend limit.

## Review: physics

**Verdict:** fixed (2026-09-16, revision 3)

- Verified: tube-bends: kappa_u = 2 pi f / W, kappa_v = 0, sign minus with the printed face outside: Cylinder of circumference W/f has radius W/(2 pi f); normal curvature around it is 1/R, along it 0; with the course convention K = n . d2X, an outward (printed-face) normal on a surface bending toward the axis gives a negative value → Correct; 4 cm times 2 pi/30 per cm is 0.8378 rad = 48.000 degrees exactly
- Verified: cone-bends: sin alpha' = 1 - f delta/2 pi, kappa_u = cot alpha'/s, kappa_v = 0: A sector of angle 2 pi - delta wrapped on a cone of half-angle alpha' covers azimuth (2 pi - delta)/sin alpha', which reaches 2 pi at f = 1; the parallel at slant s has radius s sin alpha' and meets the normal at angle alpha', so its normal curvature is cos alpha'/(s sin alpha') → Correct; wedge 60 gives sin alpha = 5/6, cot alpha = 0.66332, at 12 cm 0.055277 per cm, times 4 cm 12.6686 degrees; at 8 cm 19.0029 degrees, twelve eighths as spoken
- Verified: tilts and tilt product: kappa rho in degrees, K rho^2: Weingarten dn = -K T along a principal direction gives |dn/ds| = kappa; python recomputation of every tilt in the tests; the drawn normal one string length away compared with the readout on each surface → Readouts correct. The drawn angle equals kappa rho exactly on the tube (planar rotation) and the ball (great circle), and on the cone is arccos(sin^2 alpha + cos^2 alpha cos(rho/(s sin alpha))): 12.610 against 12.669 degrees at the cone-spot preset. Scoped in the model and the readout senses
- Verified: second-fundamental-form-panel: K_uu = kappa_u, K_vv = kappa_v, K_uv = 0, g = delta: Arc-length Cartesian coordinates on the flat sheet are isometric under rolling, closing and folding; at the spot the u line is tangent to the parallel and the v line to the generator or axis, which are the principal directions → Correct at the spot; the summary now says 'at the grey spot', since the coordinate lines leave the parallels elsewhere on the cone
- Verified: gaussian-curvature: K = kappa_u kappa_v = det K / det g; 100 per square metre on the 10 cm ball: 1/(10 cm)^2 = 0.01 per cm^2 = 100 per m^2; zero wherever one bend is zero → Correct
- Verified: edge-gap: W sin(pi f)/(pi f), 2 L sin alpha' sin((2 pi - delta)/(2 sin alpha')), sqrt 2 L cos(pi f/2): Chord between the far ends of the edges that meet at f = 1: 2R sin(pi f) on the arc of angle 2 pi f; chord between two points at radius L sin alpha' separated by azimuth (2 pi - delta)/sin alpha'; folding the two outer squares about perpendicular hinges by pi f/2 puts the far ends at (-L cos, 0, L sin) and (0, -L cos, L sin) → Correct: 30, 19.0986, 0 for the tube; 10.3302 at half closure and 0 at f = 1 for the cone; 28.28, 20, 0 for the cube; the wedge-0 disc gives 0 at every f
- Verified: ring-and-triangle-on-the-flat-sheet: 2 pi rho, sqrt 3 rho, 180 degrees: Isometry of the development; ring of radius 6 around a spot at 8 cm from the cone tip subtends 97.2 degrees at the tip, less than the 120 degree sector of the sharpest cone, and stays 60 degrees short of the seam; on the cube the disc crosses folds but stays within the three-square net → Correct for every offered state; 25.1327, 6.9282, 180
- Verified: ring-and-triangle-around-a-tip: (2 pi - delta) rho, 2 rho sin((2 pi - delta)/6), 180 + delta degrees, rim stretch -delta/2 pi: Three corners at distance rho from the tip, (2 pi - delta)/3 apart, each side the base of an isosceles triangle in the development of the faces or sector it crosses; each corner of the inscribed triangle is two base angles, pi - (2 pi - delta)/3 → Correct: cone 60 gives 20.944, 6.1284, 240, -16.667 percent; cube gives 18.850, 5.6569, 270, -25 percent; wedge 180 gives 360; wedge 240 gives 420
- Verified: ring-and-triangle-on-the-ball: 2 pi a sin(rho/a); spherical law of cosines with corners 120 degrees apart; cos A = cos sigma / (1 + cos sigma); 3A: Spherical law of cosines for the side; for the equilateral spherical triangle cos A = (cos s - cos^2 s)/sin^2 s = cos s/(1 + cos s); python → Correct: 24.4679 cm, 6.8798 cm, 192.4847 degrees at a = 10, rho = 4; 180.0298 for the tiny ring; 347.32 for the long string; rho < pi a/2 holds for every offered pair (max 6 against 7.85)
- Verified: turn-of-the-carried-arrow: cap angle 2 pi (1 - cos(rho/a)) on the ball, delta around a tip, 0 on flat regions, sign from the side of the centre, branch (-180, 180]: Gauss-Bonnet with the region on the walker's left, left defined with the head along the printed-face normal, consistent with the course rotation convention; region on the right is the complement, 4 pi - cap = -cap mod 2 pi; branch reduction with -180 reported as 180 → Correct: 28.4180, -28.4180, 0.0720, 229.57 wrapping to -130.449, 60, -60, 180, 240 wrapping to -120, 90. Unchanged by the printed-face flip because both the walk direction and the sense of left flip together
- Verified: All 22 tests: Independent python model (scratchpad model_check.py) resolving preset, defaults and overrides, computing every readout and its visibility, and comparing with abs_tol → 22 of 22 pass, every hidden readout hidden, edge gap hidden on the ball, turn hidden below walk 1
- Verified: Contract buildable: ranges, steps, defaults, available_when, animations: Every preset and tour state uses params available on its surface; animate targets roll 1, roll 0.5, walk 1, spot-distance 8 are inside their ranges; corner-sum stays in [0, 540] (max 420 and 347), tilts in (-180, 180] (max 121.5 on the cone, 72 on the tube, 68.75 on the ball), tilt product in [-10, 10] (max 1.44) → Buildable
- Verified: Spoken numbers: 25.1, 6.9, 48, 12.7, 19.0, 24.5, 192.5, 2.6, 22.9, 0.16, 0.07, 0.0067 percent, 18.8, 4.77 cm, 0.209, 0.0553, 0.0829, 100 per square metre, 2.67 percent leading order: python → All correct; 'seven millionths' was wrong (0.0067 percent is 6.67 parts in a hundred thousand) and is fixed; 'matching amounts' is now the checkable factor of about 400 (394.7 for the turn, 396.8 for the shrink, both (0.4/0.02)^2 to leading order); the 57.3 degree wording gives 0.15998, rounding to 0.16
- Verified: Beat checks and design-rule misconceptions exist in the served notes and are evidenced: note_digest of the four served notes and the check prompts → All resolve and match, after replacing the two addresses under curved-surfaces, which has no note: predict-the-ring now evidences intrinsic-versus-extrinsic-curvature/checks/lampshade-for-an-ant (ring on a bent card keeps its flat length) and the flat-copy rule names bent-means-intrinsically-curved
- Verified: No source book named or reproduced; links resolve: grep for book names; visual_ids for builds_on and leads_to → Clean; paced-ring-on-a-ball-and-a-plain, carry-an-arrow-around-a-loop and card-touching-a-curved-patch are in the catalog
- Counterexample: Flat sheet, roll 0: every bend 0, gap 30 cm, ring 25.13, corner sum 180, turn hidden until the walk closes; passes.
- Counterexample: Wedge 0 at roll 0.5: the sector is a full disc, sin alpha' = 1, bend 0, gap 0; passes.
- Counterexample: Sharpest cone, wedge 240, spot 8 cm, string 6 cm: ring subtends 97.2 degrees at the tip, under the 120 degree sector, so it never wraps; tilt across -121.5 degrees inside the range; the drawn normal differs from the readout by 5 degrees there, recorded in the model.
- Counterexample: Cube face, spot 8 cm, string 6 cm: the ring crosses both folds and keeps 37.70 cm, corner sum 180, turn 0.
- Counterexample: Ball, radius 5 cm, string 6 cm (rho/a = 1.2, under pi/2): ring 29.28, rim -22.33 percent, tilt -68.75, cap turn 229.57 reported as -130.45; corner sum 347.3 under 540.
- Counterexample: Ball, radius 50 cm, string 1 cm: rim -0.0066665 percent and turn 0.0720 degrees, neither rounding to zero at the reported decimals.
- Counterexample: Both walking directions on the ball and the cone tip: turn changes sign only; half-turn boundary (wedge 180 walked the other way) reported as 180, not -180.
- Counterexample: Printed face inside on the tube and the ball: both bends change sign, product, ring, corner sum and turn unchanged.
- Counterexample: Tilt monotonicity behind 'a bigger turn goes with a bigger shrink': true in rho/a on (0, pi/2) for the cap angle, but the reported turn wraps for the long-string preset, so the claim was replaced by the two concrete ratios.
- Fixed: tiny-but-not-zero: 'seven millionths' corrected to 'seven parts in a hundred thousand'.
- Fixed: roll-it-up and curl-into-a-trough: dropped the false 'only number that changed' claims, since tilt across is always visible and runs to -48 and -24; the beats now name the ant's unchanged numbers against the through-the-air numbers that change, in say, show and describe.
- Fixed: bigger-ring-bigger-turn: 'matching amounts' made checkable with the factor of about four hundred from the tiny ring to the 4 cm ring.
- Fixed: predict-the-ring check and the flat-copy design rule pointed at existing addresses in intrinsic-versus-extrinsic-curvature instead of the missing curved-surfaces note.
- Fixed: Model: principal directions scoped to the spot; tilt readout defined as bend times string length with the drawn normal's exact angle on the cone recorded; readout senses say so.
- Fixed: Status set to specified; revision bumped to 3 for the learner-visible changes.
- Concern: On the cone the drawn purple arrow one string length away shows the true normal, which differs from the readout in the last displayed digit at 8 cm from the tip (18.8 against 19.0) and by 5 degrees at the extreme wedge 240, spot 8, string 6. The tours use only settings where the two differ by at most 0.2 degrees; a builder may cap the string at 4 cm on the cone or draw the arrow along the u geodesic and say so.
- Concern: The tilt readouts stay visible_when 'always'; the reveals mentioned in predict-the-tilts, predict-the-tiny-square, predict-the-video-claim and predict-the-rolled-sheet-claim are tutor overlays, not readout states, and must be built as such.
- Concern: Templates with {abs} read '0 degrees to the walker's left' and 'the bend toward the printed face is 0 degrees' at zero; the beats speak the zero cases themselves, and a say_zero template would need a schema change.
- Concern: The tilt-product template's 'each divided by 57.3 degrees' gives 0.15998 for the 10 cm ball, rounding to the displayed 0.16; acceptable at entry.
- Concern: provenance.source_units is still empty; the writer should list the study units behind the ring, lampshade and card-on-a-can ideas.
- Concern: The print figure label 'tilt across 48 degrees' omits the sign of the readout (-48); harmless in print, where the arrows show the direction.
