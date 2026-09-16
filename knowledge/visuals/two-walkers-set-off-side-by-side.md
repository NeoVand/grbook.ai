---
type: "visual"
schema_version: 2
id: "two-walkers-set-off-side-by-side"
title: "Two walkers set off side by side"
kind: "interactive-3d"
priority: "flagship"
status: "specified"
revision: 4
rungs: ["entry", "working"]
serves: ["parallel-postulate", "curvature", "deviation-vector", "geodesic-deviation-equation"]
builds_on: []
leads_to: ["elastic-arrow-between-two-beads", "falling-ring-of-crumbs", "carry-an-arrow-around-a-loop"]
---

# Two walkers set off side by side

`two-walkers-set-off-side-by-side` · interactive-3d · flagship · specified · rungs: entry, working

> Two walkers start side by side and never steer. On a playground the tape between them never changes, on a ball it shrinks until they meet, and around a swim ring's hole it grows.

## What it makes visible

Two walkers who start side by side on a straight walk, facing the same way at a right angle to it, and never steer. A tape laid along the ground joins them at matching step counts and reads their gap. On a playground and on a can's label the tape never changes; on a ball it shrinks to nothing at the North Pole whatever the starting gap; around a swim ring's hole it grows, and on the ring's outer part it shrinks. Tick marks at equal stretches print the tape's reading, so the shrinking is seen to speed up stretch by stretch, and the extra per stretch, divided by the gap, reads the curvature. A head start for one walker splits the string into a sideways piece and an along-path piece. It is the one picture behind the parallel postulate, the sign of curvature, the deviation vector and the geodesic deviation equation.

## The picture

A shaded surface with a faint grid fills the scene: a playground, a can's label, a football, Earth, or a swim ring. A white dashed line marks the straight walk the walkers leave. A blue walker on the left and an orange walker on the right, seen from behind them, stand on it, facing the same way at a right angle to it. As they walk, a solid blue trail and a solid orange trail grow behind them, and a solid green tape joins them at matching counts with its reading printed beside it. White tick marks across both trails divide the walk into equal stretches, each with the tape's reading printed at it. On a ball a black star marks the North Pole where the trails meet. With a head start, a grey dashed string slants from the blue walker to the orange one, split into a purple dotted along-path piece and the green sideways tape. Readouts show the gap, its change since the start in millimetres, its share of the starting gap, and the extra per stretch.

| Element | Shows |
| --- | --- |
| Surface with a faint grid | the world the walkers live on: playground, can's label, football, Earth, or swim ring |
| White dashed starting line | the straight walk both walkers leave at a right angle, toward the same side |
| Blue walker and orange walker with solid trails | two straight walks that start parallel |
| Solid green tape with a printed reading | the gap between the paths, measured along the ground at matching counts |
| White tick marks with printed readings | equal stretches of the walk, so the shrinking or growing per stretch can be compared |
| Grey dashed string with a purple dotted along-path piece | the deviation vector when one walker starts behind the other, split into its two parts |
| Black star | the North Pole, where every straight walk leaving the equator at a right angle meets |
| Readouts: gap, change since start, share of starting gap, extra share per stretch | the tape reading, how daily life hides the effect, the cosine law, and the curvature read from the speeding up |

## Book figure

Three panels. Left: a playground with two parallel trails and three green tapes across them, every tape the same length. Middle: a ball with two trails leaving the equator at right angles and meeting at the North Pole, with tapes at equal stretches getting shorter faster and faster, and readings 100, 96.6, 86.6, 70.7, 50 and 0 metres. Right: a swim ring seen from above, with two trails running from the inner circle over the top to the outer circle like two neighbouring cuts of a sliced cake, and tapes growing from 3 to 7 millimetres.

Labels: playground, start parallel, equator, North Pole, 100 metres, 70.7 metres, inner circle, outer circle, 3 millimetres, 7 millimetres. Aspect 3:1. Alt text: Three panels: on a playground two straight walkers keep a fixed gap; on a ball two straight walkers leaving the equator draw together faster and faster and meet at the North Pole; on a swim ring two straight walkers leaving the inner circle spread apart toward the outer circle.

## Variants

- **static** `static-card` (fallback): The print figure as an SVG card, used when 3D is unavailable and as a summary card.
- **plot** `gap-plot`: The tape reading plotted against distance walked for the chosen world, with the stretch ticks and the printed readings, beside the 3D scene or on its own.
- **interactive-3d** `full-3d`: The full experience on every world, with presets, gap and head-start controls, stretch marks, scrubbing, and the readouts.

## Parameters

| Id | Label | Type | Options or range | Default | Available when | Effect |
| --- | --- | --- | --- | --- | --- | --- |
| `world` | World | enum | playground, can-label, football, earth, swim-ring | "football" | — | Switches the world and rebuilds the starting line and the walk on it. Playground: a flat floor, 100 metre walk. Can's label: a tube 30 cm around, walkers start on a ring around the can and walk 30 cm along it. Football: a ball 70 cm around, walkers start on the equator and walk to the North Pole, 17.5 cm. Earth: a ball 40 000 km around, walkers start on the equator and walk to the North Pole, 10 000 km. Swim ring: a torus with tube radius 10 cm and centre-line radius 25 cm, walkers start on the inner or outer circle and walk over the top of the tube to the other circle, 31.4 cm. Walkers can be placed only on these straight walks. |
| `gap-m` | Starting gap | number | 1–1000 step 1 m | 10 | world in playground, earth | Distance between the walkers along the starting line at the start, on the metre-sized worlds. The orange walker stands this far to the blue walker's right. |
| `gap-cm` | Starting gap | number | 0.2–10 step 0.1 cm | 2 | world in can-label, football, swim-ring | Distance between the walkers along the starting line at the start, on the hand-sized worlds. The orange walker stands this far to the blue walker's right. |
| `start-circle` | Starting circle | enum | inner, outer | "inner" | world in swim-ring | Chooses which of the swim ring's two straight circles the walkers leave. From the inner circle they walk over the top of the tube to the outer circle and spread apart; from the outer circle they walk over the top to the inner circle and draw together. |
| `head-start-m` | Head start of the blue walker | number | 0–10 step 0.5 m | 0 | world in playground, earth | The orange walker starts this far behind the blue walker along the walking direction (on Earth, on the side of the equator away from the North Pole) and counts steps from there. At matching counts the string from the blue walker to the orange one then has an along-path piece of this length, drawn purple and dotted, beside the green sideways tape. When this is zero or unavailable, the along-path and whole-string readouts are hidden. |
| `stretches` | Stretches | integer | 2–12 step 1 | 6 | — | Number of equal stretches the walk is cut into by white tick marks; the tape's reading is printed at each tick, and the extra-share readout uses one stretch as its step. |
| `progress` | Walk progress | progress | 0–1 step None | 0 | — | Moves both walkers along their paths at matching counts. 1 is the end of the world's walk: 100 m on the playground, 30 cm along the can, the North Pole on a ball, and the far circle on the swim ring. Continuous: tours and tests set any value from 0 to 1, such as one thousandth for 10 kilometres on Earth or two thirds for latitude 60 degrees; the arrow keys scrub in hundredths. |

## Presets

- `playground` Playground, 10 metres apart: world="playground", gap-m=10
- `playground-head-start` Playground, orange walker 3 metres behind: world="playground", gap-m=1, head-start-m=3
- `can-label` Can's label, 2 centimetres apart: world="can-label", gap-cm=2
- `football` Football, 2 centimetres apart on the equator: world="football", gap-cm=2
- `earth-equator` Earth, 100 metres apart on the equator: world="earth", gap-m=100, stretches=6
- `earth-twelve-stretches` Earth, 100 metres apart, twelve stretches: world="earth", gap-m=100, stretches=12
- `earth-one-metre` Earth, 1 metre apart on the equator: world="earth", gap-m=1
- `earth-head-start` Earth, 1 metre apart, orange walker 3 metres behind: world="earth", gap-m=1, head-start-m=3
- `swim-ring-inner` Swim ring, from the inner circle, 3 millimetres apart: world="swim-ring", gap-cm=0.3, start-circle="inner"
- `swim-ring-outer` Swim ring, from the outer circle, 3 millimetres apart: world="swim-ring", gap-cm=0.3, start-circle="outer"

## Readouts

- `gap` Gap between the paths (m; visible always; 5 decimals): “the green tape between the walkers reads {value} metres”
- `gap-change` Change since the start (mm; visible always; 4 decimals; sense: positive when the walkers are farther apart than at the start, which is spreading apart): “the gap is {abs} millimetres wider than at the start” / “the gap is {abs} millimetres narrower than at the start”
- `gap-share` Share of the starting gap (percent; visible always; 2 decimals): “the gap is {value} percent of its starting size”
- `extra-share` Extra share per stretch (percent; visible on-demand; 3 decimals; sense: positive when this stretch's change of the gap is shifted toward shrinking compared with the stretch before, which is drawing together that speeds up or spreading apart that slows; negative when it is shifted toward growing): “compared with a repeat of the stretch before, this stretch leaves the gap shorter by {abs} percent of the gap” / “compared with a repeat of the stretch before, this stretch leaves the gap longer by {abs} percent of the gap”
- `along-path-part` Along-path piece of the string (m; visible on-demand; 2 decimals): “the purple along-path piece is {value} metres long, pointing behind the blue walker”
- `string-length` Whole string (m; visible on-demand; 5 decimals): “the whole grey string from the blue walker to the orange walker is {value} metres long”

## Tours

### `two-friends-set-off` · for [[parallel-postulate]] · entry

1. `meet-the-playground` (entry, await none) state: preset="playground", progress=0  
   *Flat playground; blue walker Asha on the left and orange walker Ben on the right stand on the white dashed chalk line, facing the same way at a right angle to it; the green tape between them reads 10 metres.*  
   Say: “Here is a flat playground. The blue walker is Asha and the orange walker is Ben. Ben stands 10 metres to Asha's right, on the white dashed chalk line. Both face the same way, at a right angle to the line. The green tape laid on the ground between them reads 10 metres.”  
   Describe: A flat playground. Two walkers stand on a chalk line, 10 metres apart, both facing the same way at a right angle to the line. A tape on the ground between them reads 10 metres.
2. `walk-the-playground` (entry, await none) state: preset="playground", progress=0; animate progress → 1 over 5 s  
   *Both walkers move ahead; blue and orange trails stay parallel; the tape reads 10 metres at every tick.*  
   Say: “Now both walk ahead without ever steering left or right. Watch the green tape. It reads 10 metres the whole way, and the blue and orange trails stay side by side. On the playground, straight walkers who start parallel keep their gap. That is the rule called the parallel postulate, one of Euclid's starting rules.”  
   Describe: The walkers move 100 metres ahead. The tape between them reads 10 metres at every moment, and their trails stay side by side.
3. `football-setup` (entry, await none) state: preset="football", progress=0  
   *Football with the white dashed equator; the walkers stand on it 2 centimetres apart, facing the black star at the North Pole.*  
   Say: “Now the same test on a football, the round kind used in soccer, 70 centimetres around. The white dashed line is the ball's equator, and the black star at the top is the North Pole. Asha and Ben stand on the equator 2 centimetres apart, both facing the North Pole. Each leaves the equator at a right angle, so they start parallel.”  
   Describe: A round football with its equator marked. The two walkers stand on the equator 2 centimetres apart, both facing the North Pole at the top of the ball.
4. `predict-the-meeting` (entry, await prediction) state: preset="football", progress=0; evidences `parallel-postulate/checks/pairs-near-and-far`  
   *Same view, paused before the walk.*  
   Predict: “Both will walk straight ahead without steering. Will the green tape keep reading 2 centimetres all the way? And if they started only half a centimetre apart instead, would they meet sooner?”  
   Say: “Before they walk, make a guess. Will the green tape keep reading 2 centimetres all the way? And if they started only half a centimetre apart instead, would they meet sooner?”  
   Describe: The walkers wait on the equator, 2 centimetres apart, facing the North Pole.
5. `football-walk` (entry, await none) state: preset="football", progress=0; animate progress → 1 over 6 s  
   *The trails bend toward each other over the ball and meet at the black star; the tape shrinks to zero.*  
   Say: “They draw together. The blue and orange trails close in on each other, and the green tape shrinks to nothing at the black star, the North Pole. That happens after 17 and a half centimetres, a quarter of the way around the ball. Neither walker steered, yet the tape changed. So the ball fails the parallel postulate.”  
   Describe: The walkers move toward the North Pole. The tape between them shrinks, slowly at first, then faster, and reads zero when they meet at the North Pole after 17 and a half centimetres.
6. `closer-pair` (entry, await none) state: preset="football", gap-cm=0.5, progress=1  
   *A closer pair, half a centimetre apart at the equator, with trails that also meet at the black star.*  
   Say: “Now Ben starts only half a centimetre from Asha. Their trails still meet at the black star, after the same 17 and a half centimetres. Every straight walk that leaves the equator at a right angle passes through the North Pole. So the starting gap makes no difference to where they meet.”  
   Describe: The walkers now start half a centimetre apart on the equator. Their trails still meet at the North Pole, after the same 17 and a half centimetres.
7. `earth-short-walk` (entry, await none) state: preset="earth-equator", progress=0.001  
   *Earth with the walkers 100 metres apart on the equator after 10 kilometres; the tape looks unchanged, and the change readout says about a tenth of a millimetre narrower.*  
   Say: “Finally Earth, 40 thousand kilometres around, with Asha and Ben 100 metres apart on the equator, both facing the North Pole. After 10 kilometres the green tape still reads 100 metres to the eye. The change readout beside it says the gap is about a tenth of a millimetre narrower, the thickness of a sheet of paper. So with an ordinary tape measure, a walk you could take in a day cannot tell Earth's ground from the playground.”  
   Describe: Earth, with the walkers 100 metres apart on the equator, both facing the North Pole. After 10 kilometres the tape still reads 100 metres, and the change readout says about a tenth of a millimetre narrower than at the start.

### `three-worlds-three-answers` · for [[curvature]] · entry

1. `ball-draws-together` (entry, await none) state: preset="football", progress=1  
   *Football with both trails complete and meeting at the black star; the readings at the ticks shrink from 2 centimetres to zero.*  
   Say: “On the football, Asha's blue trail and Ben's orange trail left the equator side by side and met at the black star. The readings printed at the white ticks shrink from 2 centimetres to nothing. Where straight walkers who start parallel begin to draw together, the curvature is called positive.”  
   Describe: The football with both walks finished. The tape readings printed at the ticks shrink from 2 centimetres to zero at the North Pole.
2. `swim-ring-setup` (entry, await none) state: preset="swim-ring-inner", progress=0  
   *Swim ring on a table; the white dashed inner circle runs around the hole halfway up the tube; the walkers stand on it 3 millimetres apart, facing over the top of the tube away from the hole.*  
   Say: “Now a swim ring lying on a table, 70 centimetres across with a hole 30 centimetres across. The white dashed line is the inner circle, halfway up the tube and closest to the hole. Asha and Ben stand on it 3 millimetres apart. Both face over the top of the tube, away from the hole, at a right angle to the circle.”  
   Describe: A swim ring lying on a table. The walkers stand on the inner circle, the circle closest to the hole, 3 millimetres apart, both facing over the top of the tube away from the hole.
3. `predict-the-ring` (entry, await prediction) state: preset="swim-ring-inner", progress=0; evidences `curvature/checks/hole-side-is-not-flat`  
   *Same view, paused.*  
   Predict: “Both walk straight over the top of the tube toward the outer circle. Will the green tape shrink, stay at 3 millimetres, or grow?”  
   Say: “Make a guess. Both walk straight over the top of the tube toward the outer circle. Will the green tape shrink, stay at 3 millimetres, or grow?”  
   Describe: The walkers wait on the inner circle, 3 millimetres apart.
4. `ring-walk` (entry, await none) state: preset="swim-ring-inner", progress=0; animate progress → 1 over 6 s  
   *The trails run over the top of the tube like two neighbouring cake cuts, seen from above; the tape grows to 7 millimetres at the outer circle.*  
   Say: “The tape grows. Seen from above the table, the blue and orange trails run like two neighbouring cuts of a sliced cake, narrow at the hole and wide at the outer circle. At the outer circle the green tape reads 7 millimetres. Where straight walkers who start parallel begin to spread apart, the curvature is called negative.”  
   Describe: The walkers cross the top of the tube to the outer circle. The tape between them grows from 3 millimetres to 7 millimetres.
5. `ring-outer-start` (entry, await none) state: preset="swim-ring-outer", progress=0; animate progress → 1 over 6 s  
   *The walkers start on the white dashed outer circle facing over the top toward the hole; the tape shrinks to about 1.3 millimetres at the inner circle.*  
   Say: “Start the same pair on the outer circle instead, facing over the top of the tube toward the hole. Now the green tape shrinks, from 3 millimetres to about 1.3 millimetres at the inner circle. So one swim ring has positive curvature on its outer part and negative curvature around its hole.”  
   Describe: The walkers start on the outer circle and cross the top of the tube toward the hole. The tape shrinks from 3 millimetres to about 1.3 millimetres.
6. `predict-the-can` (entry, await prediction) state: preset="can-label", progress=0; evidences `curvature/checks/can-label`  
   *Tin can with its paper label; the walkers stand on the white dashed ring around the can, 2 centimetres apart, paused.*  
   Predict: “From outside, the label looks bent around the can. Will the green tape shrink as they walk, as it did on the football, or keep reading 2 centimetres?”  
   Say: “Last, the paper label on a tin can, 30 centimetres around. Asha and Ben start on the white dashed ring around the can, 2 centimetres apart. Both face along the can's length, at a right angle to the ring, toward the same end of the can. Make a guess. From outside, the label looks bent around the can. Will the green tape shrink as they walk, as it did on the football, or keep reading 2 centimetres?”  
   Describe: A tin can with a paper label. The walkers wait on a ring around the can, 2 centimetres apart, both facing along the can's length toward the same end.
7. `can-label` (entry, await none) state: preset="can-label", progress=0; animate progress → 1 over 4 s  
   *Tin can with its paper label; the walkers start on a white dashed ring around the can and walk along it; the tape reads 2 centimetres at every tick.*  
   Say: “Both walk along the can's length, toward the same end of the can. From outside the label looks bent. Yet the green tape reads 2 centimetres at every white tick. The walkers keep their gap, so the label's curvature is zero. Bent is not curved.”  
   Describe: A tin can with a paper label. The walkers start on a ring around the can and walk 30 centimetres along the can's length, at a right angle to the ring. The tape reads 2 centimetres the whole way.

### `string-at-matching-counts` · for [[deviation-vector]] · entry

1. `string-setup` (entry, await none) state: preset="earth-one-metre", progress=0  
   *Earth with the walkers 1 metre apart on the equator, facing the North Pole; small count numbers along the trails; the green tape drawn as a stretchy string.*  
   Say: “Here is Earth, 40 thousand kilometres around, with Asha and Ben on the equator 1 metre apart, both facing the North Pole. Each takes steps 1 metre long and counts them. The small numbers along the trails are their counts. The green tape is a stretchy string tied to both walkers, so it can shrink or grow, and it always joins them at the same count.”  
   Describe: Earth, with the walkers 1 metre apart on the equator, facing the North Pole. Each counts steps of 1 metre. A stretchy string joins the two walkers at matching counts.
2. `predict-two-thirds` (entry, await prediction) state: preset="earth-one-metre", progress=0; evidences `deviation-vector/checks/shrinking-string-on-a-ball`  
   *Same view, paused.*  
   Predict: “Two thirds of the way to the North Pole, how long will the green tape be?”  
   Say: “Make a guess. Two thirds of the way to the North Pole, how long will the green tape be?”  
   Describe: The walkers wait on the equator, 1 metre apart.
3. `two-thirds-reveal` (entry, await none) state: preset="earth-one-metre", progress=0; animate progress → 0.6666667 over 6 s  
   *The walkers reach the circle two thirds of the way to the pole; the tape reads 50 centimetres; that circle is highlighted.*  
   Say: “Two thirds of the way, the green tape reads 50 centimetres. At matching counts both walkers stand on the same circle around the ball, the one now highlighted. The tape covers the same share of that circle as it did of the equator. That circle is half as long as the equator, so the tape has halved.”  
   Describe: The walkers stop two thirds of the way to the North Pole. The tape between them reads 50 centimetres, half its starting length, because the circle they both stand on is half as long as the equator.
4. `head-start` (entry, await none) state: preset="earth-head-start", progress=0  
   *Ben stands 3 metres behind Asha and 1 metre to her right; a grey dashed string slants from Asha to Ben, split into a purple dotted piece along Asha's trail and the green tape across to Ben.*  
   Say: “Now Ben starts 3 metres behind Asha, on the side of the equator away from the North Pole, still 1 metre to her right. The grey dashed string slants back from Asha to Ben. It splits into two pieces. The purple dotted piece runs 3 metres back along Asha's path, and the green tape crosses 1 metre to Ben at a right angle to her path.”  
   Describe: The orange walker now starts 3 metres behind the blue walker and 1 metre to her right. The string between them slants backward and is shown as two pieces: 3 metres back along the blue walker's path, then 1 metre across to the orange walker.
5. `predict-the-whole-string` (entry, await prediction) state: preset="earth-head-start", progress=0; evidences `deviation-vector/checks/late-start-string`  
   *Same view, paused.*  
   Predict: “Two thirds of the way to the North Pole, the green tape will have halved to 50 centimetres. Will the whole grey string have halved too? And how far apart will the two paths be?”  
   Say: “Make a guess. Two thirds of the way to the North Pole, the green tape will have halved to 50 centimetres. Will the whole grey string have halved too? And how far apart will the two paths be?”  
   Describe: The blue walker waits on the equator; the orange walker waits 3 metres behind her and 1 metre to her right.
6. `head-start-walk` (entry, await none) state: preset="earth-head-start", progress=0; animate progress → 0.6666667 over 6 s  
   *Two thirds of the way: the green tape reads 50 centimetres, the purple piece still 3 metres, the whole grey string about 3 metres.*  
   Say: “Two thirds of the way, the green tape has halved to 50 centimetres, but the purple piece is still 3 metres. The whole grey string went from about 3.2 metres to about 3 metres, not to half. Where the walkers start counting only sets the purple piece. Only the green sideways piece tells how far apart the paths are.”  
   Describe: Two thirds of the way, the sideways piece has halved to 50 centimetres. The along-path piece is still 3 metres. So the whole string has gone from about 3.2 metres to about 3 metres.

### `stretch-by-stretch` · for [[geodesic-deviation-equation]] · entry

1. `six-stretches` (entry, await none) state: preset="earth-equator", progress=0  
   *Earth with the walkers 100 metres apart on the equator; six white ticks cut the walk to the North Pole into equal stretches.*  
   Say: “Asha and Ben stand on Earth's equator, 100 metres apart, facing the North Pole. White ticks across the trails cut the walk to the pole into six equal stretches, each about 1670 kilometres long. At every tick the green tape's reading will be printed.”  
   Describe: Earth, with the walkers 100 metres apart on the equator. The walk to the North Pole is cut into six equal stretches, each about 1670 kilometres long.
2. `first-three-stretches` (entry, await none) state: preset="earth-equator", progress=0; animate progress → 0.5 over 6 s  
   *The walkers pass three ticks; printed readings 96.6, 86.6 and 70.7 metres.*  
   Say: “Watch the printed readings. After the first stretch the tape reads 96.6 metres, after the second 86.6, after the third 70.7. So the first stretch shrank the tape by 3.4 metres, the second by 10, and the third by 15.9. Each stretch shrinks it more than the stretch before.”  
   Describe: The walkers pass the first three ticks. The tape reads 96.6 metres, then 86.6, then 70.7. The tape shrinks by 3.4 metres, then 10, then 15.9: more in each stretch.
3. `predict-the-fourth-stretch` (entry, await prediction) state: preset="earth-equator", progress=0.5; evidences `geodesic-deviation-equation/checks/next-stretch-on-the-ball`  
   *Paused at the third tick.*  
   Predict: “The tape reads 70.7 metres, and the third stretch shrank it by 15.9 metres. By about how much will the fourth stretch shrink it?”  
   Say: “Make a guess. The tape reads 70.7 metres, and the third stretch shrank it by 15.9 metres. By about how much will the fourth stretch shrink it?”  
   Describe: The walkers wait at the third tick, halfway to the North Pole, with the tape reading 70.7 metres.
4. `fourth-stretch` (entry, await none) state: preset="earth-equator", progress=0.5; animate progress → 0.6666667 over 3 s  
   *The fourth tick prints 50 metres; the extra-share readout shows about 6.8 percent.*  
   Say: “The fourth stretch shrinks the tape by 20.7 metres, to 50 metres. That is about 5 metres more than the stretch before. And 5 is about 7 hundredths of 70.7, the tape's length at the start of that stretch. The extra share readout shows this share as a percentage, near 7 percent, at every stretch. The extra shrinking is in proportion to the tape's length.”  
   Describe: At the fourth tick the tape reads 50 metres. This stretch shrank the tape by 20.7 metres, about 5 metres more than the stretch before, and 5 is about 7 hundredths of 70.7. The extra share readout shows near 7 percent at every stretch.
5. `playground-zero-extra` (entry, await none) state: preset="playground", progress=1  
   *Playground with every printed reading 10 metres; extra-share readout zero.*  
   Say: “On the playground every printed reading is 10 metres. No stretch shrinks the tape at all, so the extra share readout reads zero. Zero extra is what flat ground means.”  
   Describe: On the playground the tape reads 10 metres at every tick, and the extra share readout reads zero.
6. `ring-negative-extra` (entry, await none) state: preset="swim-ring-inner", progress=0; animate progress → 1 over 6 s  
   *Swim ring from the inner circle; the extra-share readout starts at minus 17.9 percent, rises through zero at the top of the tube, and ends at plus 7.7 percent at the outer circle while the printed readings grow from 3 to 7 millimetres.*  
   Say: “On the swim ring, starting at the inner circle, the printed readings grow from 3 millimetres to 7. Near the hole they grow by more in each stretch than in the one before. So while the walkers are near the hole, the extra share readout is below zero. There the tape has an extra growing instead of an extra shrinking. That is what negative curvature means. By the outer circle the readout has climbed above zero. On the outer part the tape still grows, but by less in each stretch than in the one before, because the ring's outer part draws walkers together, like the ball.”  
   Describe: On the swim ring, from the inner circle, the printed readings grow from 3 millimetres to 7 millimetres, by more in each early stretch than in the one before. Near the hole the extra share readout is below zero; by the outer circle it has risen above zero.

### `gap-law-on-a-sphere` · for [[parallel-postulate]] · working

1. `cosine-law` (working, await none) state: preset="earth-equator", progress=0  
   *Earth with the walkers 100 metres apart on the equator; the gap-share readout reads 100 percent.*  
   Say: “On a sphere of radius a, the two trails are great circles leaving the equator at right angles. After each has walked a distance s, the green tape, laid along their circle of latitude, reads D equals D zero times the cosine of s over a. The share readout shows D over D zero as a percentage.”  
   Describe: Earth, with the walkers 100 metres apart on the equator. The share readout reads 100 percent. The gap law is D equals D zero times the cosine of s over a.
2. `predict-halfway` (working, await prediction) state: preset="earth-equator", progress=0; evidences `parallel-postulate/checks/ships-halfway-to-meeting`  
   *Same view, paused.*  
   Predict: “Halfway to the meeting point, s equals pi times a over four. Is half the gap gone by then?”  
   Say: “Halfway to the meeting point, s equals pi times a over four. Is half the gap gone by then?”  
   Describe: The walkers wait on the equator.
3. `halfway-reveal` (working, await none) state: preset="earth-equator", progress=0; animate progress → 0.5 over 5 s  
   *The walkers stop halfway; the share readout reads 70.71 percent.*  
   Say: “The share readout reads 70.71 percent, the cosine of 45 degrees. Only 29 percent of the gap is gone halfway, because the gap starts closing with zero rate. Near the start, D is about D zero times one minus s squared over two a squared, so the loss grows with the square of the distance walked.”  
   Describe: Halfway to the North Pole the share readout reads 70.71 percent, the cosine of 45 degrees, so only 29 percent of the gap is gone.
4. `ten-kilometres` (working, await none) state: preset="earth-equator", progress=0.001  
   *The walkers after 10 kilometres; the change readout reads 0.1234 millimetres narrower.*  
   Say: “For D zero of 100 metres and s of 10 kilometres on Earth, the loss is D zero times s squared over two a squared, 0.12 millimetres, and the change readout agrees. Differentiating the cosine twice gives D double prime equals minus D over a squared. On any surface, for small gaps, D double prime equals minus K times D, with K the Gaussian curvature.”  
   Describe: After 10 kilometres the change readout reads 0.1234 millimetres narrower, matching D zero times s squared over two a squared. The gap law is D double prime equals minus K times D.
5. `extra-reads-k` (working, await none) state: preset="earth-twelve-stretches", progress=0.5  
   *Twelve ticks on the walk; the extra-share readout reads 1.711 percent, against 6.815 percent for six stretches.*  
   Say: “The extra share readout is minus the second difference of D over one stretch of length h, divided by D, in percent. On a sphere it equals 200 times one minus the cosine of h over a, which is about 100 times K times h squared. With six stretches on Earth it reads 6.815 percent; with twelve, as now, 1.711 percent, four times smaller for half the stretch.”  
   Describe: With twelve stretches the extra share readout reads 1.711 percent, four times smaller than the 6.815 percent for six stretches, because the extra share is about K times the stretch length squared.

### `read-the-curvature-from-the-extra` · for [[geodesic-deviation-equation]] · working

1. `sphere-extra` (working, await none) state: preset="football", progress=0.5  
   *Football with six ticks; the extra-share readout reads 6.815 percent at every position.*  
   Say: “On the football the extra share readout reads 6.815 percent wherever the walkers stand. The stretch h is 2.92 centimetres and the radius a is 11.14 centimetres, so K times h squared is 6.85 percent, close to the readout. Dividing the extra by h squared reads the curvature, which is the geodesic deviation equation D double prime equals minus K times D in finite steps.”  
   Describe: On the football the extra share readout reads 6.815 percent at every position. Dividing by the stretch length squared, 2.92 centimetres squared, gives close to the curvature, one over 11.14 centimetres squared.
2. `ring-sign-change` (working, await none) state: preset="swim-ring-inner", progress=0; animate progress → 1 over 6 s  
   *Swim ring from the inner circle; the extra-share readout runs from minus 17.9 percent at the start through zero at the top of the tube to plus 7.7 percent at the outer circle.*  
   Say: “On the swim ring the readout changes along the walk. At the inner circle it reads minus 17.9 percent, at the top of the tube zero, and at the outer circle plus 7.7 percent. The torus has K equals the cosine of psi, divided by r times the quantity R c plus r times the cosine of psi, with psi the angle around the tube, negative near the hole, zero at the top, positive outside.”  
   Describe: On the swim ring the extra share readout runs from minus 17.9 percent at the inner circle, through zero at the top of the tube, to plus 7.7 percent at the outer circle, following the sign of the Gaussian curvature.
3. `flat-worlds-zero` (working, await none) state: preset="can-label", progress=1  
   *Can's label with every printed reading 2 centimetres; the extra-share readout reads zero.*  
   Say: “On the can's label the readout reads zero, as on the playground. Rolling paper into a tube keeps every length along it, so D stays D zero and its second difference vanishes. The tube is bent in the room but has K equals zero, and the walkers' tape cannot tell it from the playground.”  
   Describe: On the can's label every printed reading is 2 centimetres and the extra share readout reads zero, the same as on the playground.

## Design rules

- **Offer walkers only on the built-in straight walks of each world, leaving them at a right angle, and never let a learner place them on a steered path such as a small circle around the pole.** Because: A steady gap between steered paths, like railway tracks or runners in lanes, would look like a passed test; the parallel postulate is tested only between straight walks that start parallel. Prevents `parallel-postulate/misconceptions/same-gap-means-parallel`.
- **Draw the tape only between the two walkers at the same count, print the count at both ends, and never let the tape join other points of the two trails.** Because: The gap between the paths is the length of the string at matching counts; joining other points gives a length that is not the distance between the paths. Prevents `deviation-vector/misconceptions/any-moments-will-do`.
- **Draw the tape as a stretchy string tied to both walkers, visibly changing length, and never as a rigid arrow held by one walker.** Because: A rigid carried arrow keeps its length; the deviation vector is tied to both walkers and grows or shrinks with their paths. Prevents `deviation-vector/misconceptions/string-is-a-carried-arrow`.
- **Cut every walk into equal stretches and print the tape's reading at each tick, so that the shrinking per stretch can be read off and compared.** Because: Without the printed readings the closing looks steady; the list 3.4, 10, 15.9, 20.7 makes the speeding up plain, and the extra per stretch is what the geodesic deviation equation fixes. Prevents `geodesic-deviation-equation/misconceptions/shrinks-at-a-steady-rate`.
- **On Earth, show the change since the start in millimetres beside the tape, which to the eye still reads its starting length.** Because: A learner who sees an unchanged tape after 10 kilometres concludes the ground is flat; the millimetre readout shows the effect exists and why daily life hides it. Prevents `curvature/misconceptions/looks-flat-so-flat`.
- **Keep the swim ring's inner and outer starting circles one click apart, so that spreading apart and drawing together are seen on one surface.** Because: Learners who have only seen the ball believe curvature can only draw walkers together. Prevents `curvature/misconceptions/only-closing-means-curved`.
- **Keep the can's label one click away from the ball, with the tape reading printed at every tick.** Because: A surface that looks bent from outside but keeps the gap is the control that separates bent from curved. Prevents `curvature/misconceptions/bent-means-curved`.
- **Mark the North Pole with a black star that stays fixed while the starting gap changes, so that the same pair, restarted closer together, is seen to meet at the same star after the same distance.** Because: Seeing pairs with different starting gaps meet at the same star, after the same distance, dissolves the belief that a closer pair meets sooner. Prevents `parallel-postulate/misconceptions/closer-start-meets-sooner`.
- **Distinguish the along-path piece, the sideways tape and the whole string by line style as well as colour: purple dotted, green solid, grey dashed. Tell the blue and orange trails apart by more than colour as well: print each walker's name at the end of their trail.** Because: Colour alone fails for colour-blind learners and in print, and the two pieces must be told apart to see which one measures the distance between the paths.

## Model

Every world uses straight walks with a closed-form gap law, so no integration is needed. The gap $D(s)$ is measured along the curve of matching counts, which crosses both trails at right angles: on the ball a circle of latitude, on the swim ring a circle around the hole. On the playground and the can's label $D = D_0$. On a ball of radius $a$ the trails are meridians and $D = D_0\cos(s/a)$. On the swim ring the trails are the symmetric cuts through the hole's centre, which are geodesics, and $D$ is proportional to the distance from the hole's axis. The change readout is $D - D_0$ in millimetres, the share readout is $100\,D/D_0$, and the extra-share readout is minus the second difference of $D$ over one stretch $h$, divided by $D(s)$, in percent; it is about $100\,K h^2$. With a head start $b$ the along-path piece is $b$ and the whole string is $\sqrt{D^2 + b^2}$, exact on the playground and correct to the order kept on Earth, where the string is tiny compared with the ball. The along-path and whole-string readouts are hidden when the head start is zero or unavailable.

**Gap law**

$$
\frac{d^2D}{ds^2} = -K\,D
$$

Holds when: Straight walks that start parallel, gap measured along the curve of matching counts, small gaps; exact on the constant-curvature ball, on the flat worlds, and on the swim ring's symmetric cuts.

**Gap on the playground and the can's label**

$$
D(s) = D_0
$$

Holds when: Plane and tube; rolling paper into a tube keeps every length along it.

**Gap on a ball**

$$
D(s) = D_0\cos\!\left(\frac{s}{a}\right),\qquad 0 \le s \le \frac{\pi a}{2}
$$

Holds when: Meridians leaving the equator at right angles on a sphere of radius $a$; the football has $a = 70/2\pi$ cm and Earth $a = 40\,000/2\pi$ km. The walk ends at the North Pole, $s = \pi a/2$.

**Gap on the swim ring**

$$
D(s) = D_0\,\frac{R_c \mp r\cos(s/r)}{R_c \mp r},\qquad 0 \le s \le \pi r
$$

Holds when: Torus with centre-line radius $R_c = 25$ cm and tube radius $r = 10$ cm; trails are the planar cuts through the hole's axis, which are geodesics by mirror symmetry; $s$ is the arc length along the tube from the starting circle.

**Curvature of the swim ring**

$$
K = \frac{\cos\psi}{r\,(R_c + r\cos\psi)}
$$

Holds when: $\psi$ is the angle around the tube, zero on the outer circle and $\pi$ on the inner circle; $K = -1/(r(R_c - r))$ on the inner circle, zero on the top circle, $+1/(r(R_c + r))$ on the outer circle. The torus gap law satisfies $D'' = -KD$ exactly.

**Extra share per stretch**

$$
E(s) = -\,\frac{D(s+h) - 2D(s) + D(s-h)}{D(s)} \times 100\,\%,\qquad h = \frac{L}{n}
$$

Holds when: $L$ is the walk length and $n$ the number of stretches; $D$ is continued through $s = 0$ and past $s = L$ by the same law, which is even in $s$. On a ball $E = 200(1 - \cos(h/a))$ at every $s$ with $D \ne 0$, and the readout takes this same value at the North Pole, where the quotient is $0/0$; for small $h$, $E \approx 100\,K h^2$.

**String with a head start**

$$
\xi_\parallel = b,\qquad \xi_\perp = D(s),\qquad |\xi| = \sqrt{D(s)^2 + b^2}
$$

Holds when: Orange walker starts $b$ behind the blue one and counts from there. Exact on the playground; on Earth correct to first order in the string's size over the radius.

**Method:** Closed forms only. The 3D trails are the meridians of the ball and the planar cuts of the torus, drawn from their parametrizations; the tape is drawn along the circle of matching counts, which is the circle of latitude on the ball and the circle around the hole on the ring. The extra-share readout evaluates the gap law at $s - h$, $s$ and $s + h$ by the formula, so it is defined at every position including the start; at the North Pole on a ball, where $D = 0$, the readout shows the ball's constant value $200(1 - \cos(h/a))$ instead of the quotient. The football and Earth share one code path with different radii and units; the gap-m and gap-cm parameters are converted to metres for the readouts.

| Test | State | Expect | Hidden | Note |
| --- | --- | --- | --- | --- |
| `playground-keeps-gap` | preset="playground", progress=1 | gap = 10 ±1e-09; gap-change = 0 ±1e-09; gap-share = 100 ±1e-09; extra-share = 0 ±1e-09 | along-path-part, string-length | Flat case: the gap never changes and the extra is zero. No head start, so the string readouts stay hidden. |
| `can-label-keeps-gap` | preset="can-label", progress=1 | gap = 0.02 ±1e-09; gap-change = 0 ±1e-09; gap-share = 100 ±1e-09; extra-share = 0 ±1e-09 | along-path-part, string-length | A tube is bent but flat: 2 cm is 0.02 m at every count. |
| `football-start` | preset="football", progress=0 | gap = 0.02 ±1e-09; gap-change = 0 ±1e-09; gap-share = 100 ±1e-09 | along-path-part, string-length | Boundary: at the start the gap is the starting gap. |
| `football-halfway` | preset="football", progress=0.5 | gap = 0.0141421356 ±1e-08; gap-change = -5.8578644 ±1e-05; gap-share = 70.7106781 ±1e-05; extra-share = 6.8148347 ±1e-05 | — | $2\cos 45^\circ$ cm; the change is negative, drawing together. Extra share $200(1 - \cos 15^\circ)$ for six stretches, against $100Kh^2 = 6.854$ with $a = 11.14$ cm and $h = 2.917$ cm. |
| `football-meeting` | preset="football", progress=1 | gap = 0 ±1e-09; gap-change = -20 ±1e-08; gap-share = 0 ±1e-09 | — | Boundary: the walkers meet at the North Pole after a quarter of the way around. |
| `football-closer-pair` | preset="football", gap-cm=0.5, progress=1 | gap = 0 ±1e-09; gap-change = -5 ±1e-08 | — | A closer pair meets at the same point after the same distance. |
| `football-twelve-stretches` | preset="football", stretches=12, progress=0.25 | extra-share = 1.7110277 ±1e-05 | — | Halving the stretch divides the extra share by about four: $200(1 - \cos 7.5^\circ)$, independent of position on a ball. |
| `earth-ten-kilometres` | preset="earth-equator", progress=0.001 | gap = 99.99987663 ±1e-06; gap-change = -0.12337 ±0.0001; gap-share = 99.99987663 ±1e-06 | — | Small-size leading order: loss $D_0 s^2/2a^2$ with $D_0 = 100$ m, $s = 10$ km, $a = 6366.2$ km, which is 0.123 mm. |
| `earth-five-kilometres` | preset="earth-equator", progress=0.0005 | gap-change = -0.0308425 ±1e-05 | — | Half the distance, a quarter of the loss: about three hundredths of a millimetre. |
| `earth-first-stretch` | preset="earth-equator", progress=0.1666667 | gap = 96.592583 ±0.0001; gap-change = -3407.417 ±0.1; gap-share = 96.59258 ±0.0001; extra-share = 6.8148347 ±1e-05 | — | End of the first of six stretches: $100\cos 15^\circ$; the first stretch shrinks the string by 3.4 m. |
| `earth-halfway` | preset="earth-equator", progress=0.5 | gap = 70.7106781 ±1e-05; gap-share = 70.7106781 ±1e-05 | — | Halfway to the meeting point only 29 percent of the gap is gone: $\cos 45^\circ$. |
| `earth-meeting` | preset="earth-equator", progress=1 | gap = 0 ±1e-09; gap-change = -100000 ±1e-06; gap-share = 0 ±1e-09 | — | Boundary: the whole 100 m gap is gone at the North Pole. |
| `earth-twelve-stretches` | preset="earth-twelve-stretches", progress=0.5 | extra-share = 1.7110277 ±1e-05 | — | Twelve stretches on Earth: near 1.7 hundredths, a quarter of the six-stretch value. |
| `earth-one-metre-two-thirds` | preset="earth-one-metre", progress=0.6666667 | gap = 0.5 ±1e-06; gap-share = 50 ±0.0001 | along-path-part, string-length | Two thirds of the way to the pole is latitude 60 degrees, where the circle is half the equator: $\cos 60^\circ = 1/2$. |
| `earth-head-start-two-thirds` | preset="earth-head-start", progress=0.6666667 | gap = 0.5 ±1e-06; along-path-part = 3 ±1e-09; string-length = 3.0413813 ±1e-06 | — | The sideways piece halves, the along-path piece stays 3 m, and the whole string goes from $\sqrt{10} = 3.162$ m to $\sqrt{9.25} = 3.041$ m. |
| `playground-head-start` | preset="playground-head-start", progress=0.3 | gap = 1 ±1e-09; along-path-part = 3 ±1e-09; string-length = 3.1622777 ±1e-06 | — | Pythagoras on the playground: the string is $\sqrt{10}$ m at every count. |
| `ring-inner-start` | preset="swim-ring-inner", progress=0 | gap = 0.003 ±1e-09; gap-change = 0 ±1e-09; extra-share = -17.8632795 ±1e-05 | — | Negative branch of the extra: at the inner circle $K = -1/150$ per cm squared, and $100Kh^2 = -18.28$ with $h = \pi\cdot 10/6$ cm; the finite-step value is $-200(1 - \cos(h/r))\,r/(R_c - r)$. |
| `ring-inner-top-of-tube` | preset="swim-ring-inner", progress=0.5 | gap = 0.005 ±1e-09; gap-change = 2 ±1e-08; gap-share = 166.6666667 ±1e-05; extra-share = 0 ±1e-09 | — | Boundary between the signs: on the top circle of the tube $K = 0$, so the extra vanishes while the gap is still growing. Positive branch of the change readout. |
| `ring-inner-to-outer-circle` | preset="swim-ring-inner", progress=1 | gap = 0.007 ±1e-09; gap-change = 4 ±1e-08; gap-share = 233.3333333 ±1e-05; extra-share = 7.6556912 ±1e-05 | — | 3 mm times 35 over 15 is 7 mm; at the outer circle the extra turns positive, $K = +1/350$ per cm squared. |
| `ring-outer-to-inner-circle` | preset="swim-ring-outer", progress=1 | gap = 0.0012857143 ±1e-09; gap-change = -1.7142857 ±1e-06; gap-share = 42.8571429 ±1e-05; extra-share = -17.8632795 ±1e-05 | — | From the outer circle the gap shrinks by 15 over 35; arriving at the inner circle the extra is the negative inner-circle value. |

## Serves

- [[parallel-postulate]]: the playground walk where the tape never changes, the football walk where every pair meets at the black star after the same distance, and the Earth walk where 10 kilometres loses a tenth of a millimetre
- [[curvature]]: the sign from three worlds: drawing together on the ball and the ring's outer part, spreading apart around the ring's hole, and a fixed gap on the playground and the can's label
- [[deviation-vector]]: the stretchy string at matching counts, the halving two thirds of the way, and the head-start presets that split the string into a sideways piece and an along-path piece
- [[geodesic-deviation-equation]]: the printed readings at equal stretches, the extra per stretch in proportion to the string's length, and the extra-share readout that reads the curvature, negative on the ring's hole side and zero on flat worlds

## In the visual network

- **Leads to:** [[elastic-arrow-between-two-beads]], [[falling-ring-of-crumbs]], [[carry-an-arrow-around-a-loop]]

## Accessibility

Every tour beat has a spoken description of where the walkers stand and what the tape reads. The tape reading, its change since the start in millimetres, and its share of the starting gap are announced as numbers. The along-path piece, the sideways tape and the whole string differ in line style as well as colour, and every control works from the keyboard.

Static alternative: Two walkers start side by side, facing the same way at a right angle to a straight line, and never steer. On a playground the tape between them never changes. On a ball it shrinks faster and faster until they meet at the North Pole, whatever their starting gap. Around a swim ring's hole it grows.

- `Space`: play or pause the walk
- `Left and Right arrows`: scrub along the walk
- `1 to 5`: choose playground, can's label, football, Earth, or swim ring
- `S`: swap the swim ring's starting circle
- `Plus and Minus`: widen or narrow the starting gap
- `B`: cycle how far behind the orange walker starts
- `T`: cycle the number of stretches

## Starting material

No earlier course asset draws two geodesics with a tape between them; the closest are the tidal-cloud labs, which this visual leads to. New work throughout: the five worlds, the closed-form gap laws, the count markers, the head-start split, and the stretch ticks with printed readings. The orange and bagel try-its in the notes give the static card its look.

## Review: novice

**Verdict:** fixed (2026-09-16, revision 4)

**Retell attempt:** Asha and Ben stand on a chalk line on a playground, 10 metres apart, both facing the same way at a right angle to the line, and walk without steering. The green tape between them reads 10 metres the whole way, which is the parallel postulate. On a football they stand on the equator facing the North Pole, and even though neither steers, the tape shrinks to nothing at the black star, after 17 and a half centimetres. A pair that starts closer meets at the same star after the same distance. On Earth, 10 kilometres of walking only loses a tenth of a millimetre, so you would never notice. Where walkers draw together the curvature is positive, like the ball; on a swim ring, starting at the hole, the tape grows from 3 to 7 millimetres, so around the hole it is negative; starting on the outside the tape shrinks, so one ring has both. On a can's label the tape stays 2 centimetres, so bent is not curved. The tape is a stretchy string tied to both walkers at the same count; two thirds of the way to the pole it has halved, because the circle they stand on is half the equator. If Ben starts 3 metres behind, the string slants and splits into a purple piece of 3 metres along Asha's path and the green piece across; only the green piece tells how far apart the paths are. With six stretches the readings go 96.6, 86.6, 70.7, 50, so the shrinking speeds up, and the extra each stretch is about 7 percent of the tape's length; on the playground the extra is zero and near the ring's hole it is below zero. I was unsure whether the string and the tape were the same thing, and whether the football was the pointed kind.

- Stumble: “Now the same test on a football, 70 centimetres around.”: A football can be the pointed oval ball; the entry way says the round kind, and the tour never does.
- Stumble: “The blue and orange trails bend toward each other, and the green tape shrinks to nothing”: Bend was the word for a path bending over the ball's curve without steering; here it sounds as if the walkers steered toward each other.
- Stumble: “A second pair starts half a centimetre apart on the equator.”: The spoken line says Ben now starts half a centimetre from Asha, the description says a second pair; I could not tell whether one pair moved or a second pair was added.
- Stumble: “Earth again, with Asha and Ben on the equator 1 metre apart”: Again points to an earlier tour I may not have heard; the tour should stand on its own and say how big Earth is.
- Stumble: “how long will the green string be?”: The thing on screen is the green tape in one sentence and the string in the next, so I was not sure they were the same thing; the whole grey string with a head start also needs the word string.
- Stumble: “and the green tape crosses 1 metre to Ben at a right angle.”: A right angle to what is not said.
- Stumble: “The extra share readout shows this share, near 7 hundredths, at every stretch.”: The readout on screen says 6.8 percent while I hear hundredths, so I had to convert before I could match them.
- Stumble: “so the extra share readout there is below zero.”: At the end of this beat the walkers stand at the outer circle and the readout reads plus 7.7 percent, so there did not match what I saw; the wording now names where the readout is below zero, and the state is raised in concerns.
- Stumble: “and walk along the can.”: Along the can does not say which way: around it, or along its length, and toward which end.
- Stumble: “each stretch shrinks the gap by {abs} percent of its length more than the stretch before”: Its length could be the stretch's length or the gap's; and more than the stretch before what?
- Stumble: “cycle the orange walker's head start”: The control is labelled head start of the blue walker and the presets say the orange walker starts behind, so this key sounded like the opposite control.
- Stumble: “narrow at the hole and wide outside.”: Outside sounded like outside the ring rather than at its outer circle.
- Stumble: “the gap is {abs} millimetres wider than at the start”: At the start, and on the playground and the can's label, this reads the gap is 0 millimetres wider than at the start, which sounds like a change; the templates have no form for zero.
- Stumble: “K equals cosine of psi over r times R plus r cosine of psi”: Spoken, the grouping is lost: over r times R could be cosine over r, then times R; and the equation writes R c, not R.
- Fixed: Named the football as the round kind used in soccer in the football-setup beat, its description, and the world option label.
- Fixed: Replaced bend toward each other with close in on each other in football-walk, keeping bend for a path bending over the ball's curve.
- Fixed: Made the closer-pair description match its spoken line: the same walkers moved to half a centimetre apart, not a second pair.
- Fixed: Opened the string-at-matching-counts tour with Here is Earth, 40 thousand kilometres around, instead of Earth again.
- Fixed: Called the on-screen sideways piece the green tape in every entry beat and readout, saying once that it is a stretchy string; string now names only the whole grey string with a head start.
- Fixed: Gave every right angle and every walking direction its reference: to her path in head-start, along the can's length toward the same end in can-label, both facing the North Pole in earth-short-walk.
- Fixed: Spoke the extra share in percent, matching the readout, in fourth-stretch and in the working sphere-extra beat.
- Fixed: In ring-negative-extra, said where the readout is below zero (while the walkers are near the hole) instead of there.
- Fixed: Rewrote the extra-share readout templates so the percentage is of the gap and the comparison is with what the stretch before did.
- Fixed: Reworded the B key action so it names the orange walker starting behind, matching the parameter label and presets.
- Fixed: Said wide at the outer circle instead of wide outside in ring-walk.
- Fixed: Spoke the torus curvature with explicit grouping and R c in ring-sign-change.
- Fixed: Attributed the parallel postulate as one of Euclid's starting rules rather than a name Euclid used.
- Fixed: Gave the picture composition's left and right their viewpoint (seen from behind the walkers).
- Fixed: Split the can-label and ring-negative-extra spoken lines into shorter sentences after validator warnings.
- Concern: Beat ring-negative-extra sits at progress 1, where the extra-share readout reads plus 7.7 percent, while the lesson is the negative value near the hole; consider state progress 0 (readout minus 17.9 percent) or animating progress 0 to 1 while the readout is watched.
- Concern: Beat closer-pair replaces the 2 centimetre pair with a half centimetre pair, but design rule meeting-star-stays-put asks for a closer pair added beside the first; a second-pair param or a two-pair preset would let the beat show both meeting at one star.
- Concern: The blue and orange trails differ by colour only, both solid; add a second cue (a different dash pattern, or the walkers' names printed at the trail ends) as the design rule split-string-by-style does for the string pieces.
- Concern: Readout templates have no zero form: gap-change at zero says 0 millimetres wider than at the start, and extra-share at zero says 0 percent more than the stretch before did; a say_zero field or a rule that the tutor says unchanged at zero would fix this.
- Concern: The gap and string readouts speak metres on the hand-sized worlds (0.01414 metres on the football, 0.003 metres on the ring) while the tours speak centimetres and millimetres; the writer's note stands.
- Concern: Beat can-label carries curvature/checks/can-label with await none and no predict line, so the check is not evidenced by a prediction; a short predict (will the tape change?) before the walk would match the other check beats.
- Concern: The prediction-to-check matches could be confirmed only by check id and misconception list from the digest (pairs-near-and-far with closer-start-meets-sooner, ships-halfway-to-meeting with gap-closes-steadily, hole-side-is-not-flat, can-label, shrinking-string-on-a-ball, late-start-string, next-stretch-on-the-ball); the physics reviewer should confirm each question against the check text.
- Concern: Beat two-thirds-reveal says the circle is now highlighted; give the highlight a style cue (a thicker dashed circle) as well as a colour so it is not colour only.

**Re-read** (2026-09-16, revision 4)

- Stumble: “By the outer circle the readout has climbed above zero, because the ring's outer part draws walkers together, like the ball.”: In this beat the tape grows the whole way, so a reader asks how the outer part can be drawing the walkers together; the reason for the readout climbing is missing.
- Fixed: ring-negative-extra say: split the last sentence and say that the tape still grows on the outer part but by less in each stretch, which is why the readout climbs above zero

## Review: physics

**Verdict:** fixed (2026-09-16, revision 4)

- Verified: flat-gap: D = D0 on the playground and the can's label: A tube is isometric to the plane, so parallel straight walks keep their separation; independent python model → holds; tests playground-keeps-gap and can-label-keeps-gap reproduce 10 m, 0.02 m, change 0, share 100, extra 0
- Verified: sphere-gap: D = D0 cos(s/a), walk length pi a/2: Meridians leave the equator at right angles; at arc s the colatitude is pi/2 - s/a and the latitude circle arc between meridians dphi apart is a sin(colatitude) dphi = D0 cos(s/a); a = 70/2pi cm = 11.14 cm and 6366.2 km → holds; D'' = -D/a^2 = -K D with K = +1/a^2 in course conventions
- Verified: torus-gap: D = D0 (Rc -/+ r cos(s/r))/(Rc -/+ r); the cuts through the axis are geodesics leaving the inner and outer circles at right angles: Meridian circles of a torus lie in mirror planes through the axis, so they are geodesics; the inner and outer circles are parallels of extremal radius, so they are geodesics, and meridians cross parallels at right angles; D is proportional to the distance Rc + r cos(psi) from the axis → holds; D'' equals -K D exactly, checked numerically at five points on the walk to 1e-7 relative
- Verified: torus-curvature K = cos(psi)/(r (Rc + r cos(psi))), -1/150 per cm^2 at the inner circle, 0 at the top, +1/350 at the outer circle: Standard Gaussian curvature of a torus of revolution in the sphere-positive convention; evaluated in python → holds; signs match the spoken lines (negative near the hole, zero at the top, positive outside)
- Verified: extra-share E = -(D(s+h) - 2D(s) + D(s-h))/D(s) x 100, equal to 200(1 - cos(h/a)) on a ball, about 100 K h^2: Sum formula cos(x+y) + cos(x-y) = 2 cos x cos y; six stretches give h/a = 15 degrees, twelve give 7.5 degrees → 6.8148 and 1.7110 percent reproduced; on the ring -17.863, 0 and +7.656 percent reproduced; 100 K h^2 gives 6.854 on the football and -18.28 at the inner circle as the notes say
- Verified: string-parts: along-path piece b, whole string sqrt(D^2 + b^2): Pythagoras on the playground; on Earth the exact great-circle distance from Asha at colatitude 30 degrees to Ben 3 m further south on a meridian 1 m east at the equator was computed with a haversine → sqrt(9.25) = 3.041381 m; the exact distance differs by less than 1e-7 m, inside the 1e-6 tolerance
- Verified: All 21 model tests: Independent python model of the five worlds evaluated at each test state, with hidden readouts decided from the head-start availability → every expected value within its tolerance; every expect_hidden correct
- Verified: Spoken numbers: readings 100, 96.6, 86.6, 70.7, 50; shrinks 3.4, 10, 15.9, 20.7; extra about 5 m, about 7 hundredths of 70.7; stretch about 1670 km; 10 km loses 0.12 mm; football walk 17.5 cm; ring walk 31.4 cm; outer-to-inner 1.3 mm; inner-to-outer 7 mm: python from the gap laws → all agree (4.82 m extra is 6.81 percent of 70.71 m; 0.1234 mm; 1.2857 mm)
- Verified: Beat states and animations are buildable: Checked every tour state against the presets and available_when, every animate against the progress range → all presets exist and every override is available in its world; four progress values (0.001, 0.0005, 1/6, 2/3) were unreachable with step 0.01, so progress is now continuous
- Verified: Each check beat evidences its check: Compared each predict line with the served check text → pairs-near-and-far, ships-halfway-to-meeting, hole-side-is-not-flat, shrinking-string-on-a-ball and next-stretch-on-the-ball match their predictions; can-label and late-start-string sat on reveal beats with no prediction, so prediction beats now carry them
- Verified: Design rules name real misconceptions: Compared each address with the digest misconception lists → all eight addresses exist and the rule prevents the named belief
- Verified: The 30 strings the novice review changed: Read each against the model and the states → no number, sign, state or claim was altered; the torus curvature is spoken with correct grouping
- Counterexample: Flat case: playground and can's label at every progress and any stretch count give D = D0, change 0, share 100, extra 0.
- Counterexample: North Pole on a ball: the extra-share quotient is 0/0 (floating point gave 70.8 percent on the football and -0 on Earth); the method now states that the readout shows the ball's constant limit there.
- Counterexample: Largest gap on the football (10 cm): halfway up, the tape laid along the latitude circle is 1.4 percent longer than the shortest path between the walkers; the readouts report the tape, as the model states, and the gap law is exact for the tape.
- Counterexample: Ring from the outer circle, arriving at the inner circle: the gap is still shrinking while the extra share reads -17.9 percent, so the old say_negative template (each stretch grows the gap) was false there; likewise from the inner circle past the top the gap grows while the extra share is +5.9 percent. The templates now compare with a repeat of the stretch before, which is true in both directions.
- Counterexample: Ring with two stretches: extra share -133 percent at the inner circle, defined; twelve stretches: -4.54 percent.
- Counterexample: Ring with the largest gap (10 cm): 23.3 cm at the outer circle, share 233 percent, as the law predicts.
- Counterexample: Earth with gap 1000 m and two stretches at the midpoint: extra share 58.6 percent = 200(1 - cos 45 degrees).
- Counterexample: Head start 10 m with gap 1 m on the playground: string 10.05 m at every count.
- Counterexample: Progress 0 on every world: the extra share uses D(-h) = D(h) by evenness and is defined.
- Counterexample: Beat ring-negative-extra at progress 1 read +7.7 percent while the lesson was the negative value; the beat now animates from the inner circle and says what the final positive reading means.
- Fixed: Made the progress parameter continuous (step null) because tour and test states use 0.001, 0.0005, one sixth and two thirds, which a hundredths step cannot reach.
- Fixed: Rewrote the extra-share readout sense, say and say_negative so they are true when a shrinking gap slows or a growing gap slows: the reading compares this stretch with a repeat of the stretch before.
- Fixed: Stated in the model that at the North Pole, where D = 0, the extra-share readout shows the ball's constant value instead of the 0/0 quotient.
- Fixed: Moved beat ring-negative-extra to start at the inner circle and animate to the outer circle, and added the sentence that explains the readout climbing above zero on the outer part.
- Fixed: Added a prediction beat predict-the-can carrying curvature/checks/can-label and a prediction beat predict-the-whole-string carrying deviation-vector/checks/late-start-string; the reveal beats no longer carry checks.
- Fixed: Named the instrument in earth-short-walk: with an ordinary tape measure a day's walk cannot tell Earth from the playground.
- Fixed: Restored the minus sign and the percent unit in the working line that defines the extra-share readout.
- Fixed: Reworded design rule meeting-star-stays-put to the contract's actual behaviour (the same pair restarted closer) instead of a second pair the params cannot add.
- Fixed: Extended design rule split-string-by-style to the two trails: print each walker's name at the trail end so they are told apart without colour.
- Concern: The gap, along-path and whole-string readouts speak metres on the hand-sized worlds (0.003 metres on the ring) while the tours speak millimetres; a per-world unit would need a schema change.
- Concern: Readout templates have no zero form; the tutor should say the gap is unchanged when a signed readout is zero.
- Concern: The tape on a ball is laid along the circle of latitude, which for the largest gaps is slightly longer than the shortest path between the walkers; entry tours only use gaps where the difference is far below the spoken precision.
- Concern: leads_to elastic-arrow-between-two-beads and falling-ring-of-crumbs are proposed in notes and not yet in the catalog.

**Diff check** (2026-09-16, revision 4)

- Verified: extra-share say and say_negative: a positive readout means this stretch leaves the gap shorter, by E percent of the gap, than a repeat of the stretch before would: E = -(D(s+h) - 2D(s) + D(s-h))/D(s) x 100; the end gap after this stretch minus the end gap after a repeated previous change is (D(s+h) - D(s)) - (D(s) - D(s-h)) = -E D(s)/100 → holds for shrinking, growing, speeding and slowing gaps; sign and branch intact
- Verified: extra-reads-k: the readout in percent equals 200(1 - cos(h/a)) on a sphere, about 100 K h^2: python: h = pi a/12 gives 6.815 percent and 100 (h/a)^2 = 6.85; h = pi a/24 gives 1.711 percent → the changed line said the percent readout equals 2(1 - cos(h/a)), a factor 100 short; fixed
- Verified: ring-negative-extra: on the outer part the tape still grows but by less in each stretch, and the readout is above zero at the outer circle: on a meridian cut D is proportional to R - r cos(s/r); D' = sin(s/r) falls after the top of the tube and D'' < 0 there, so K > 0 and E > 0; physics review reported +7.7 percent at the outer circle → holds; describe said above zero again although the readout had never been above zero in the beat; fixed
- Verified: predict-the-whole-string: two thirds of the way to the pole the 1 metre tape reads 50 centimetres: latitude 60 degrees, 100 cm x cos 60 degrees → holds; the describe put both walkers on the equator although the orange walker starts 3 metres on the far side of it; fixed
- Verified: predict-the-can and can-label: the tape keeps 2 centimetres on the label: a cylinder is isometric to the plane; unchanged claim restated in the split beats → holds; earth-short-walk's tape-measure scope also holds, 0.12 millimetres over 10 kilometres
- Fixed: extra-reads-k say: 200 times one minus the cosine of h over a, about 100 times K times h squared, so the sphere value is in the readout's percent
- Fixed: ring-negative-extra describe: has risen above zero, not above zero again
- Fixed: predict-the-whole-string describe: only the blue walker waits on the equator; the orange walker waits 3 metres behind her
