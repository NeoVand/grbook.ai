---
type: "visual"
schema_version: 2
id: "twenty-of-256-slots"
title: "Twenty of 256 slots"
kind: "interactive-2d"
priority: "flagship"
status: "proposed"
revision: 2
rungs: ["entry", "working"]
serves: ["number-of-independent-riemann-components", "symmetries-of-the-riemann-tensor", "cyclic-identity", "riemann-curvature-tensor", "weyl-tensor"]
builds_on: ["four-legs-around-a-tiny-loop", "carry-an-arrow-around-a-loop"]
leads_to: ["falling-ring-of-crumbs", "six-entry-curvature-table", "coordinate-knobs-and-metric-dials"]
---

# Twenty of 256 slots

`twenty-of-256-slots` · interactive-2d · flagship · proposed · rungs: entry, working

> Every way of picking four directions makes one square of the curvature table, and four rules leave only twenty of the 256 squares carrying their own number.

## What it makes visible

The curvature table at one spot starts as a grid with one square for every way of choosing four directions: 256 squares in spacetime. Four rules act on the grid one at a time. Each antisymmetry greys the squares whose loop, or whose arrow, uses one direction twice, and links what is left in plus and minus pairs. Pair exchange folds the grid of index pairs onto its diagonal like a times table. The cyclic identity links three squares whose four directions are all different, so any two fix the third. The counter falls 256, 96, 36, 21, 20, and the dimension slider replays the whole sieve to give 0, 1, 6, 20 and 50 for one to five directions. A bar under the grid splits the survivors into Ricci and Weyl, and loaded example tables show that the entries change with the frame while the count does not.

## The picture

A large square grid fills the left of the frame: rows are the loop's two directions in order, columns are the arrow's starting direction and the reading direction, so each cell is one entry of the table. Live cells are pale blue; cells a rule forces to zero are dark grey. Solid orange lines link cells that hold the same number, dashed orange lines link cells that hold opposite numbers. On the right the same information folds into a small times table of index pairs, with its diagonal marked. A counter strip under both grids shows the running number of independent entries, and a stacked bar shows the Ricci and Weyl shares. When an example table is loaded, each live cell carries its numerical value in units of the curvature scale.

| Element | Shows |
| --- | --- |
| Large grid of pale blue squares | one square for every way of choosing the four directions of an entry |
| Dark grey squares | entries a rule forces to zero, because a loop or an arrow would need one direction twice |
| Solid orange link lines | squares that hold the same number |
| Dashed orange link lines | squares that hold the opposite number |
| Folded times table of index pairs on the right | the pairs left after both antisymmetries, made symmetric by pair exchange |
| Three linked squares lit together | the cyclic identity, which ties entries whose four directions are all different |
| Counter strip and stacked Ricci and Weyl bar | how many numbers survive, and how they split into the part matter fixes and the part it leaves free |

## Book figure

Two panels side by side. Left: the 16 by 16 grid of spacetime index slots, 112 of them shaded dark, the rest pale, with a few solid and dashed link lines drawn and three slots ringed together for the cyclic identity. Right: the folded 6 by 6 times table of index pairs, its diagonal marked, with the single cyclic relation shown as a line joining three of its off-diagonal entries. A counter strip runs under both panels reading 256, 96, 36, 21, 20.

Labels: 256 slots, loop uses one direction twice, arrow uses one direction twice, same number, opposite number, 6 by 6 times table, one cyclic relation, 20 survive. Aspect 2:1. Alt text: A grid of 256 squares beside a folded 6 by 6 table of index pairs, with a counter falling from 256 to 96, 36, 21 and finally 20.

## Variants

- **static** `static-card` (fallback): The print figure as an SVG card: the shaded spacetime grid, the folded pair table, and the counter strip. Used when scripting is unavailable and as a summary card.
- **interactive-2d** `pair-table-only`: Just the folded times table of index pairs with the dimension slider, for narrow screens: the pair count, the symmetric array, and the cyclic subtraction.
- **interactive-2d** `full-sieve`: The whole experience: dimension slider, stage-by-stage sieve with sweeping, link lines with signs, example tables with values, a turnable frame, the Ricci and Weyl bar, and the tide-meter overlay.

## Parameters

| Id | Label | Type | Options or range | Default | Available when | Effect |
| --- | --- | --- | --- | --- | --- | --- |
| `dimension` | Number of directions | integer | 1–5 step 1 | 4 | — | Sets $n$, the number of directions at the spot. The grid is rebuilt with $n^4$ squares and every count is recomputed. |
| `stage` | Rules applied so far | enum | all-slots, last-pair, both-pairs, pair-exchange, cyclic | "all-slots" | — | Applies the rules in order. Each stage greys the squares its rule forces to zero, draws the links its rule creates, and lowers the survivor count. |
| `view` | View | enum | slot-grid, pair-grid (stage in both-pairs, pair-exchange, cyclic; dimension in 2, 3, 4, 5), both (stage in both-pairs, pair-exchange, cyclic; dimension in 2, 3, 4, 5) | "slot-grid" | — | The times table of index pairs only makes sense once both antisymmetries have grouped the slots into pairs, so it unlocks at that stage. |
| `labels` | Direction labels | enum | names (dimension in 2, 3, 4), numbers | "names" | — | Names label the frame's directions in words (a surface: ahead, left; space: ahead, left, up; spacetime: time, ahead, left, up, and for the star example time, toward the star, and two crosswise directions). Numbers label them $0$ to $n-1$, which is the only choice past four directions. |
| `example` | Example table | enum | abstract, round-ball (dimension in 2), round-space (dimension in 3), star-exterior (dimension in 4), even-dust (dimension in 4), cyclic-trio (dimension in 4), flat-spacetime (dimension in 4) | "abstract" | — | Writes numbers into the live squares, in units of the example's curvature scale, computed in the named orthonormal frame. |
| `focus` | Lit square | enum | none, s0101 (dimension in 2, 3, 4, 5), s1001 (dimension in 2, 3, 4, 5), s0011 (dimension in 2, 3, 4, 5), s2323 (dimension in 4, 5), s0123 (dimension in 4, 5), s0231 (dimension in 4, 5), s0312 (dimension in 4, 5), s2301 (dimension in 4, 5) | "none" | — | Rings one square in white and shows its value, its links and its copy sign. The four digits are the reading direction, the arrow's starting direction, and the loop's two edge directions in order. |
| `enforce-cyclic` | Keep the cyclic identity | boolean | — | true | example in cyclic-trio | When on, the third of the three linked entries is fixed by the other two. When off, it can be set by hand, and the grid flags a table that no torsion-free space can have. |
| `third-entry` | Third linked entry | number | -4–4 step 0.5 | -2 | example in cyclic-trio; enforce-cyclic in False | Sets $R_{0312}$ by hand, in units of the curvature scale, while the other two linked entries stay at $3$ and $-1$. |
| `frame-turn` | Turn the frame | number | 0–90 step 5 deg | 0 | example in round-space, star-exterior, even-dust, cyclic-trio | Rotates the orthonormal frame by this angle in the plane of directions $1$ and $2$. The entries change; the counts, the Ricci and Weyl split and the Weyl share do not. |
| `weyl-split` | Ricci and Weyl bar | boolean | — | false | dimension in 3, 4, 5 | Draws a bar under the grid splitting the survivors into a Ricci segment and a Weyl segment. The split is only defined for three or more directions. |
| `tide-overlay` | Tide-meter overlay | boolean | — | false | dimension in 4 | Rings the six survivors a non-spinning tide meter reads in one freely falling frame, and dims the fourteen it cannot reach. |
| `progress` | Sweep progress | progress | 0–1 step 0.01 | 0 | — | Sweeps the current stage's rule across the grid. Counts appear only at 1, when the sweep has finished. |

## Presets

- `all-slots-spacetime` Spacetime, no rule yet: dimension=4, stage="all-slots", view="slot-grid", example="abstract"
- `last-pair-swept` Spacetime, loops swept: dimension=4, stage="last-pair", view="slot-grid", example="abstract"
- `both-pairs-swept` Spacetime, loops and arrows swept: dimension=4, stage="both-pairs", view="slot-grid", example="abstract"
- `pairs-folded` Spacetime, folded into a times table: dimension=4, stage="pair-exchange", view="both", example="abstract"
- `cyclic-applied` Spacetime, all four rules: dimension=4, stage="cyclic", view="both", example="abstract"
- `surface` A surface, all four rules: dimension=2, stage="cyclic", view="both", example="abstract"
- `space` Space, all four rules: dimension=3, stage="cyclic", view="both", example="abstract"
- `a-line` A line, all four rules: dimension=1, stage="cyclic", view="slot-grid", labels="numbers", example="abstract"
- `five-dimensions` Five directions, all four rules: dimension=5, stage="cyclic", view="both", labels="numbers", example="abstract"
- `weyl-bar-spacetime` Spacetime with the Ricci and Weyl bar: dimension=4, stage="cyclic", view="both", example="abstract", weyl-split=true
- `five-dimensions-weyl` Five directions with the Ricci and Weyl bar: dimension=5, stage="cyclic", view="both", labels="numbers", example="abstract", weyl-split=true
- `tide-meter-overlay` Spacetime with the tide-meter overlay: dimension=4, stage="cyclic", view="both", example="abstract", tide-overlay=true
- `ball-surface-table` The surface of a ball, with values: dimension=2, stage="cyclic", view="both", example="round-ball"
- `even-space-table` An evenly curving space, with values: dimension=3, stage="cyclic", view="both", example="round-space", weyl-split=true
- `star-exterior-table` Outside a black hole, with values: dimension=4, stage="cyclic", view="both", example="star-exterior", weyl-split=true
- `dust-table` Inside evenly spread dust, with values: dimension=4, stage="cyclic", view="both", example="even-dust", weyl-split=true
- `flat-table` Flat spacetime, with values: dimension=4, stage="cyclic", view="both", example="flat-spacetime"
- `cyclic-trio-table` The three linked entries: dimension=4, stage="cyclic", view="both", labels="numbers", example="cyclic-trio"
- `cyclic-trio-free` The three linked entries, third one unlocked: dimension=4, stage="cyclic", view="both", labels="numbers", example="cyclic-trio", enforce-cyclic=false, third-entry=-2

## Readouts

- `independent-count` Numbers still needed (no unit; visible on-complete; 0 decimals): “the table needs {value} separate numbers in all”
- `live-slots` Squares not greyed out (no unit; visible on-complete; 0 decimals): “{value} squares are still pale blue”
- `zero-slots` Squares forced to zero (no unit; visible on-complete; 0 decimals): “so far the rules force {value} squares to zero”
- `pair-count` Tilts (no unit; visible on-demand; 0 decimals): “there are {value} different tilts at this spot”
- `cyclic-relations` New links from the cyclic identity (no unit; visible on-complete; 0 decimals): “the cyclic identity adds {value} new links here”
- `slot-value` Value in the lit square (no unit; visible on-demand; 4 decimals; range (-5, 5]; sense: positive when the carried arrow comes back leaning away from the reading direction, the first of the square's four directions): “the lit square holds plus {abs}, in units of the curvature scale” / “the lit square holds minus {abs}, in units of the curvature scale”
- `copy-sign` Copy sign of the lit square (no unit; visible on-demand; 0 decimals; sense: positive when the lit square holds a copy of its group's surviving number, negative when it holds the opposite): “the copy sign reads plus {abs}, so the lit square holds its group's number itself” / “the copy sign reads minus {abs}, so the lit square holds the opposite of its group's number”
- `cyclic-sum` Sum of the three linked entries (no unit; visible on-complete; 4 decimals; range (-3, 7]; sense: positive when the three cyclically linked entries add to more than nothing, in units of the curvature scale): “the three linked entries add up to {value}” / “the three linked entries add up to minus {abs}”
- `ricci-count` Ricci numbers (no unit; visible on-demand; 0 decimals): “matter at the spot fixes {value} of the surviving numbers”
- `weyl-count` Weyl numbers (no unit; visible on-demand; 0 decimals): “{value} of the surviving numbers are left free”
- `weyl-share` Weyl share of the table (zero to one) (no unit; visible on-demand; 3 decimals): “the Weyl share of this table reads {value}, where zero is none and one is all”
- `curvature-scale` Curvature scale of the example (m^-2; visible on-demand; 12 decimals): “the curvature scale here is {value} per metre squared”
- `tide-meter-numbers` Numbers a tide meter reads (no unit; visible on-demand; 0 decimals; range (0, 20]): “a tide meter falling with one crew reads {value} of the surviving numbers”
- `missing-from-tide-meter` Numbers the tide meter misses (no unit; visible on-demand; 0 decimals; range (0, 20]): “the tide meter never reaches {value} of the surviving numbers”

## Tours

### `count-to-twenty` · for [[number-of-independent-riemann-components]] · entry

1. `the-whole-grid` (entry, await none) state: preset="all-slots-spacetime", progress=1  
   *A 16 by 16 grid of 256 pale blue squares, every square live, with the direction names down the side and across the top.*  
   Say: “Here is the curvature table for one spot in space and time. A curvature table says how a carried arrow comes back changed, for every tiny loop at that spot. On screen it is a grid of 256 pale blue squares. Picture yourself standing at the spot. Space and time have four directions: time, ahead, your left and up. Each square fills four slots with directions: the direction the arrow's lean is read in, the direction the arrow starts along, and the loop's two sides. Four times four times four times four gives 256.”  
   Describe: A large grid of 256 pale blue squares, sixteen across and sixteen down. Each square stands for one entry of the curvature table.
2. `guess-the-count` (entry, await prediction) state: preset="all-slots-spacetime", progress=1; evidences `number-of-independent-riemann-components/checks/guess-256`  
   *Same grid, paused, with the counter under it reading 256.*  
   Predict: “Does the curving at one spot really need 256 separate numbers?”  
   Say: “The counter under the grid counts the separate numbers the table needs. Right now it reads 256. Before I switch on any rule, make a guess. Does the curving at one spot really need 256 separate numbers?”  
   Describe: The grid waits with all 256 squares pale blue. The counter under it reads 256.
3. `loops-need-two-directions` (entry, await none) state: preset="last-pair-swept", progress=0; animate progress → 1 over 4 s  
   *The sweep greys 64 squares whose loop uses one direction twice, and draws solid and dashed orange links between the rest. The counter falls to 96.*  
   Say: “Here is the first rule. Walking a loop the other way flips the change the arrow comes back with. A loop needs two different directions. If both its sides run the same way there is no loop to walk, and its entry is zero. Watch the sweep: 64 squares go dark grey. The rest pair up, and each pair needs only one number. A solid orange line joins two squares that hold the same number, and a dashed orange line joins two that hold opposite numbers. The counter has fallen to 96.”  
   Describe: Sixty-four squares turn dark grey. The pale blue squares that remain are joined in pairs by solid and dashed lines. The counter reads 96.
4. `the-lean-rule` (entry, await none) state: preset="both-pairs-swept", progress=0; animate progress → 1 over 4 s; evidences `symmetries-of-the-riemann-tensor/checks/lean-of-the-second-arrow`  
   *The sweep greys 48 more squares, so 112 are grey, and adds dashed links. The counter falls to 36.*  
   Say: “The second rule is the lean rule. Take two equal arrows taped at a right angle and carry them around one loop. One arrow's tip leans toward the other exactly as far as the other's tip leans away. So swapping the arrow's two directions flips the entry. Those two are the direction the arrow starts along and the direction its lean is read in. An entry that uses one direction for both is zero. Another 48 squares go dark grey, and the counter falls from 96 to 36.”  
   Describe: Forty-eight more squares turn dark grey, making 112 grey in all. The counter reads 36.
5. `the-mirror-rule` (entry, await none) state: preset="pairs-folded", progress=0; animate progress → 1 over 4 s  
   *The right panel shows the 6 by 6 times table of tilts folding onto its diagonal, with solid orange links across it. The counter falls to 21.*  
   Say: “The third rule is the mirror rule. A tilt is a pair of two different directions at a spot, like the side of a box or its bottom. Four directions make six tilts. One tilt belongs to the loop and one to the arrow, so the survivors sit in a six by six times table on the right. The mirror rule says that swapping the loop's tilt with the arrow's tilt leaves the entry unchanged. Just as three times four matches four times three, each square off the diagonal matches the square on the other side of it. The table folds onto its diagonal, and the counter reads 21.”  
   Describe: A small six by six table appears on the right. Squares across its diagonal join in pairs, and the counter reads 21.
6. `the-fourth-rule` (entry, await none) state: preset="cyclic-applied", progress=0; animate progress → 1 over 3 s  
   *Three squares of the folded table light together and join with solid orange lines. The counter falls to 20.*  
   Say: “One rule is left, the cyclic identity. It ties together three entries whose four directions are all different. Those three squares light up together, joined by lines that run between all three at once. Their three numbers add up to nothing, so any two of them fix the third. That is one more number gone. The counter reads 20.”  
   Describe: Three squares of the small table light up and are joined. The counter falls from 21 to 20.
7. `a-surface-keeps-one` (entry, await none) state: preset="surface", progress=1  
   *Dimension set to two: a 4 by 4 grid, twelve squares grey, four pale blue, the folded table a single square. The counter reads 1.*  
   Say: “Now I set the number of directions to two, which makes a surface. There are only ahead and left, so the grid shrinks to 16 squares. Twelve of them go grey, and the four that are left share one number, each holding it as a copy or as its opposite. The counter reads 1. One number at each spot says how a surface curves there.”  
   Describe: A small grid of sixteen squares, twelve of them grey. The counter reads 1.
8. `predict-the-fourth-rule-in-space` (entry, await prediction) state: preset="space", stage="pair-exchange", progress=1; evidences `cyclic-identity/checks/fourth-rule-in-space`  
   *Dimension three, three rules applied: the folded table is 3 by 3 and the counter reads 6.*  
   Predict: “In space there are only three directions. Do you think the fourth rule takes one more number away there as well?”  
   Say: “Now space, with three directions: ahead, left and up. The first three rules are on, and the counter reads 6. Before I switch on the fourth rule, make a guess. Does it take one more number away here as well?”  
   Describe: A grid for three directions with a three by three folded table beside it. The counter reads 6.
9. `space-keeps-six` (entry, await none) state: preset="space", progress=1  
   *Dimension three, cyclic stage: nothing greys, no new link is drawn, the counter stays at 6.*  
   Say: “The fourth rule is on now. Nothing went grey, no new line was drawn, and the counter still reads 6. The rule needs four different directions to say anything new, and space has only three. So a rule can be perfectly true and still take nothing away.”  
   Describe: The grid does not change. The counter stays at 6.
10. `a-line-keeps-none` (entry, await none) state: preset="a-line", progress=1; evidences `number-of-independent-riemann-components/checks/ant-in-a-coiled-hose`  
   *Dimension one: a single square, dark grey. The counter reads 0.*  
   Say: “Last, a line. A line has one direction, forward, with backward as its opposite. A loop needs two different directions, so the one square is grey and the counter reads 0. Think of a garden hose coiled on a lawn. Lay it out straight without stretching it. Every distance you measure along the hose with a tape measure is the same as before. So a line keeps no curvature number at all, however it is coiled.”  
   Describe: One square, dark grey. The counter reads 0.

### `three-rules-one-table` · for [[symmetries-of-the-riemann-tensor]] · entry

1. `one-square-up-close` (entry, await none) state: preset="both-pairs-swept", focus="s0101", progress=1  
   *One pale blue square ringed in white; the copy sign reads plus one.*  
   Say: “Here is one square of the table, ringed in white. Its four slots are filled in this order. The first slot is the direction the arrow's lean is read in, which here is time. I will call that the reading direction. The second is the direction the arrow starts along, which is ahead. The last two are the loop's two sides, time then ahead. Under the grid, the copy sign reads plus one. Squares joined by lines make a group that shares one number, and plus one means this square holds that number itself.”  
   Describe: One square of the grid is ringed in white. The copy sign under the grid reads plus one.
2. `the-arrow-swapped` (entry, await prediction) state: preset="both-pairs-swept", focus="s1001", progress=1; evidences `symmetries-of-the-riemann-tensor/checks/lean-of-the-second-arrow`  
   *A second square ringed in white, joined to the first by a dashed orange line; the copy sign reads minus one.*  
   Predict: “This square swaps the arrow's starting direction with the reading direction. Do you think it holds the same number as the first square, or its opposite?”  
   Say: “Now I ring a second square. It keeps the same loop, but the arrow starts along time and its lean is read along ahead, the other way round from before. A dashed orange line joins it to the first square. Before I read the sign, make a guess. Same number, or opposite?”  
   Describe: A second square is ringed in white and joined to the first by a dashed line.
3. `opposite-leans` (entry, await none) state: preset="both-pairs-swept", focus="s1001", progress=1  
   *The copy sign readout reads minus one.*  
   Say: “The copy sign reads minus one, so this square holds the opposite of the first square's number. That is the lean rule. Two equal arrows taped at a right angle cannot change the angle between them, because the tape holds it and the cardboard does not stretch. So the pair can only turn as one piece, and one tip leans toward the other exactly as far as the other leans away.”  
   Describe: The copy sign reads minus one. The two ringed squares hold opposite numbers.
4. `a-square-that-is-zero` (entry, await none) state: preset="both-pairs-swept", focus="s0011", progress=1  
   *A dark grey square ringed in white; no copy sign is shown.*  
   Say: “Here I ring a grey square. Its loop runs along time and along time again, the same direction twice. A loop needs two different directions, so this entry is zero. There is no copy sign under the grid, because a square that is zero belongs to no group of copies.”  
   Describe: A dark grey square is ringed in white. No copy sign is shown.
5. `the-mirror-fold` (entry, await none) state: preset="pairs-folded", focus="s2301", progress=1  
   *The folded 6 by 6 table with one off-diagonal square ringed, joined across the diagonal by a solid orange line; the copy sign reads plus one.*  
   Say: “The third rule is the mirror rule. Swap the loop's tilt with the arrow's tilt and the entry does not change. On the right, the six by six times table folds onto its diagonal. The ringed square joins its mirror with a solid orange line, and the copy sign reads plus one.”  
   Describe: A six by six table with one square ringed and joined across the diagonal by a solid line. The copy sign reads plus one.
6. `predict-surface-and-space` (entry, await prediction) state: preset="both-pairs-swept", progress=1; evidences `symmetries-of-the-riemann-tensor/checks/count-on-a-surface-and-in-space`  
   *Back to the spacetime grid with two rules applied, the dimension slider highlighted.*  
   Predict: “With those three rules and nothing else, how many different numbers does the table need on a surface, and how many in space?”  
   Say: “The grid is back to the two sweeps, but you have met three rules now: walking a loop the other way flips the change, the lean rule, and the mirror rule. Make a guess before I move the slider. How many different numbers does a surface need? How many does space need?”  
   Describe: The spacetime grid, with the dimension slider highlighted and waiting.
7. `one-on-a-surface` (entry, await none) state: preset="surface", progress=1  
   *Dimension two: the counter reads 1 and the folded table is a single square.*  
   Say: “A surface has one tilt only, ahead with left. The loop must have it and the arrow must have it, so there is one square in the folded table. The counter reads 1.”  
   Describe: A single square in the folded table. The counter reads 1.
8. `six-in-space` (entry, await none) state: preset="space", progress=1  
   *Dimension three: the folded table is 3 by 3 and the counter reads 6.*  
   Say: “Space has three tilts: ahead with left, ahead with up, and left with up. The folded table is three by three, with three squares on the diagonal and three above it. The counter reads 6.”  
   Describe: A three by three folded table. The counter reads 6.

### `every-tilt-and-every-arrow` · for [[riemann-curvature-tensor]] · entry

1. `what-one-square-means` (entry, await none) state: preset="all-slots-spacetime", focus="s0101", progress=1  
   *The full 256-square grid with one square ringed in white and its four direction names called out.*  
   Say: “On a surface, one number at a spot is enough. Space has three directions instead of two, so a tiny loop at one spot can lie different ways, and different arrows can be carried round it. The curvature table holds one entry for each of those choices. The ringed square names four directions in order: the direction the arrow's lean is read in, the direction the arrow starts along, and the loop's two sides.”  
   Describe: A grid of 256 squares with one square ringed in white.
2. `predict-the-tilts` (entry, await prediction) state: preset="space", stage="pair-exchange", view="slot-grid", progress=1; evidences `riemann-curvature-tensor/checks/count-the-tilts`  
   *The slot grid for three directions, with the times-table panel hidden.*  
   Predict: “Space has three directions: ahead, left and up. How many different tilts can a tiny loop have, counting ahead with up and up with ahead as one tilt?”  
   Say: “The way a tiny loop lies is its tilt, set by the two directions its sides run along. Space has three directions: ahead, left and up. Make a guess before I open the times table. How many different tilts are there? Count ahead with up and up with ahead as one tilt.”  
   Describe: The slot grid for three directions. The times-table panel is closed.
3. `three-tilts-in-space` (entry, await none) state: preset="space", view="pair-grid", progress=1  
   *The 3 by 3 times table with its three row labels named; the tilt readout shows 3.*  
   Say: “Three tilts: ahead with left, ahead with up, and left with up. The times table has three rows and three columns, one for each. The readout says three tilts at this spot.”  
   Describe: A three by three times table with three named rows. The readout says three tilts.
4. `six-tilts-with-time` (entry, await none) state: preset="pairs-folded", view="pair-grid", progress=1  
   *The 6 by 6 times table for four directions; the tilt readout shows 6.*  
   Say: “Now I add time as a fourth direction. That brings three more tilts: time with ahead, time with left, and time with up. The readout says six tilts, and the times table grows to six rows and six columns.”  
   Describe: A six by six times table. The readout says six tilts.
5. `one-number-is-not-enough` (entry, await none) state: preset="cyclic-applied", progress=1  
   *Spacetime with all four rules; the counter reads 20.*  
   Say: “With all four rules on, the counter reads 20. A surface needed one number and space needed six. So with three directions or more, one number at a spot cannot say how a place curves. A table can, and this is that table.”  
   Describe: The spacetime grid with all four rules applied. The counter reads 20.

### `three-entries-that-add-to-nothing` · for [[cyclic-identity]] · working

1. `the-first-entry` (working, await none) state: preset="cyclic-trio-table", focus="s0123", progress=1  
   *The cyclic-trio table loaded; slot 0123 ringed in white with the value 3.*  
   Say: “I have loaded a made-up curvature table in which only the entries with four different indices are nonzero. The square ringed in white is R zero one two three, and it reads plus 3 in units of the curvature scale.”  
   Describe: A grid with three nonzero entries. The ringed square reads plus 3.
2. `the-second-entry` (working, await none) state: preset="cyclic-trio-table", focus="s0231", progress=1  
   *Slot 0231 ringed in white with the value minus 1, joined to slot 0123 by a solid orange line.*  
   Say: “The second of the three linked entries is R zero two three one. Its last three indices are the first square's last three moved one place around a ring, one two three going to two three one. It reads minus 1.”  
   Describe: A second square is ringed and joined to the first. It reads minus 1.
3. `predict-the-third` (working, await prediction) state: preset="cyclic-trio-table", focus="s0231", progress=1; evidences `cyclic-identity/checks/three-entries-and-a-wrong-sum`  
   *Both linked squares ringed, the third flashing but blanked.*  
   Predict: “The third linked entry is R zero three one two. Given plus 3 and minus 1, what must it read?”  
   Say: “The third square in the ring is R zero three one two, with its last three indices at three one two. The cyclic identity says the three add to nothing. Work it out before I show it.”  
   Describe: Two ringed squares hold plus 3 and minus 1. The third is flashing, with its value hidden.
4. `the-sum-is-nothing` (working, await none) state: preset="cyclic-trio-table", focus="s0312", progress=1  
   *Slot 0312 ringed in white reading minus 2; the sum readout reads zero.*  
   Say: “R zero three one two reads minus 2, and the sum readout under the grid reads zero. Note which three orders count. They are the cyclic orders one two three, two three one and three one two. Swapping any two indices instead gives an odd reordering, which the rule says nothing about.”  
   Describe: The third ringed square reads minus 2. The sum readout reads zero.
5. `unlock-the-third` (working, await none) state: preset="cyclic-trio-free", third-entry=0, focus="s0312", progress=1  
   *The third entry unlocked and set to zero; the sum readout reads plus 2 and the three linked squares outline in red.*  
   Say: “Now I unlock the third entry and set it to zero by hand. The sum readout jumps to plus 2, and the three linked squares take a red outline. The other three rules are all still satisfied, so this is a legitimate symmetric array. It is simply not the curvature of any space whose four-sided walks close up.”  
   Describe: The third entry is zero. The sum readout reads plus 2 and the three linked squares are outlined in red.
6. `predict-five-dimensions` (working, await prediction) state: preset="five-dimensions", stage="pair-exchange", progress=1; evidences `symmetries-and-identities/checks/count-in-five-dimensions`  
   *Dimension five with three rules applied: a 10 by 10 folded table and a counter reading 55.*  
   Predict: “In five dimensions the pair rules leave 55 entries. How many does the cyclic identity take away, and what is the count?”  
   Say: “Five directions give ten tilts, so the folded times table is ten by ten and the counter reads 55. The cyclic identity brings one new link for each set of four different indices. Work out how many sets there are before I switch it on.”  
   Describe: A ten by ten folded table. The counter reads 55.
7. `five-relations-in-five-dimensions` (working, await none) state: preset="five-dimensions", progress=1  
   *Dimension five with all four rules: five separate trios light up and the counter reads 50.*  
   Say: “Five sets of four indices out of five, so five new links, and five trios light up together. The counter falls from 55 to 50. In spacetime there is exactly one such set and exactly one link, which is why 21 became 20.”  
   Describe: Five trios of squares light up. The counter falls from 55 to 50.

### `pairs-and-the-times-table` · for [[number-of-independent-riemann-components]] · working

1. `the-times-table` (working, await none) state: preset="pairs-folded", view="pair-grid", progress=1  
   *The 6 by 6 symmetric array of index pairs; the tilt readout reads 6 and the counter reads 21.*  
   Say: “The two antisymmetries turn a count of components into a count of index pairs. Four directions give six unordered pairs, so the tensor is a six by six array with a pair label on each axis. Pair exchange makes that array symmetric, like a times table: six entries on the diagonal and half of the other thirty, which is 21.”  
   Describe: A six by six symmetric array. The tilt readout reads six and the counter reads 21.
2. `predict-twenty-one` (working, await prediction) state: preset="pairs-folded", progress=1; evidences `number-of-independent-riemann-components/checks/twenty-one-or-twenty`  
   *The folded array with the counter reading 21 and the cyclic stage not yet applied.*  
   Predict: “A student stops here and reports 21 independent components in spacetime, saying the cyclic identity follows from the pair symmetries. Is 21 the right count?”  
   Say: “A student stops here, reports 21, and argues that the cyclic identity follows from the three rules already used. Decide whether 21 is the right count before I go on.”  
   Describe: The folded array with the counter reading 21. The last rule is not yet applied.
3. `one-relation-goes` (working, await none) state: preset="cyclic-applied", progress=1  
   *The cyclic stage applied: one trio of off-diagonal entries lit, the relation counter reading 1 and the survivor counter reading 20.*  
   Say: “The cyclic sum vanishes on its own whenever two of its indices coincide, so the rule only bites on four different indices. In spacetime there is one such set, and it links the three off-diagonal entries zero one with two three, zero two with three one, and zero three with one two. The relation counter reads 1, and the survivor counter reads 20.”  
   Describe: One trio of off-diagonal entries is lit. The relation counter reads 1 and the survivor counter reads 20.
4. `predict-the-tide-meter` (working, await prediction) state: preset="cyclic-applied", progress=1; evidences `number-of-independent-riemann-components/checks/what-the-tide-meter-misses`  
   *The spacetime array with all four rules applied, the overlay not yet on.*  
   Predict: “A crew falls freely with a tide meter that does not spin, and records all nine drift readings. How many separate numbers of the table does that give them, and how many are missing?”  
   Say: “Twenty numbers survive. A crew in free fall carries a tide meter that does not spin and records all nine drift readings of its three crumbs. Work out how many of the twenty they get before I turn on the overlay.”  
   Describe: The spacetime array with the counter reading 20. The overlay is off.
5. `six-of-twenty` (working, await none) state: preset="tide-meter-overlay", progress=1  
   *Six entries ringed, fourteen dimmed; the readouts show 6 read and 14 missed.*  
   Say: “Six entries are ringed and fourteen are dimmed. The ringed six are the entries with time in both the first and the third slot, the ones geodesic deviation reads for this crew's own frame. The mirror rule makes the nine drift readings symmetric, so they hold only six numbers. Fourteen of the twenty lie outside them, and another crew moving past this one would ring a different six.”  
   Describe: Six entries are ringed and fourteen dimmed. The readouts say six read and fourteen missed.

### `ricci-half-and-weyl-half` · for [[weyl-tensor]] · working

1. `the-bar-under-the-grid` (working, await none) state: preset="weyl-bar-spacetime", progress=1  
   *Spacetime, all four rules, with a stacked bar under the grid: a blue segment of 10 and an orange segment of 10.*  
   Say: “Twenty numbers survive in spacetime. The bar under the grid splits them in two. The Ricci segment, drawn in blue, holds ten numbers, which Einstein's equation fixes from the matter at the spot. The Weyl segment, drawn in orange, holds the other ten, which the equation leaves free at that spot.”  
   Describe: A bar under the grid, half Ricci and half Weyl. The readouts say ten Ricci numbers and ten Weyl numbers.
2. `predict-three-dimensions` (working, await prediction) state: preset="weyl-bar-spacetime", progress=1; evidences `number-of-independent-riemann-components/checks/empty-space-three-and-four`  
   *The same bar, with the dimension slider highlighted.*  
   Predict: “Take away the time direction and keep three space directions. How long is the Weyl segment there?”  
   Say: “Now I am about to drop to three directions, where the table keeps six numbers. Ricci is a symmetric array on three directions, so it also carries six. Say what the Weyl segment does before I move the slider.”  
   Describe: The bar, half Ricci and half Weyl, with the dimension slider highlighted.
3. `three-directions-are-all-ricci` (working, await none) state: preset="even-space-table", progress=1  
   *Dimension three with the evenly curving example loaded: the bar is entirely blue, reading 6 and 0, and the Weyl share reads 0.*  
   Say: “The whole bar is the Ricci segment: six Ricci numbers and no Weyl numbers at all. In three directions the traces already carry the whole table, so a space with no matter in it is flat there. The Weyl share readout reads zero. That is why a vanishing Ricci tensor forces flatness in three directions but not in four.”  
   Describe: A bar that is all Ricci, reading six and zero. The Weyl share readout reads zero.
4. `dust-changes-room-not-shape` (working, await none) state: preset="dust-table", progress=1  
   *Spacetime with the evenly spread dust example: every live entry carries a value, the bar shows 10 and 10, and the Weyl share reads 0.*  
   Say: “Back to four directions, inside a cloud of dust spread evenly and at rest around the cabin. All twenty numbers are present and the bar still reads ten and ten, because the bar counts slots, not values. But the Weyl share readout reads zero. Every Weyl number is zero here, so a small ball of crumbs let go at rest shrinks without changing its shape.”  
   Describe: A grid of values with a bar that is half Ricci and half Weyl. The Weyl share readout reads zero.
5. `predict-outside-a-star` (working, await prediction) state: preset="dust-table", progress=1; evidences `weyl-tensor/checks/vacuum-leftover`  
   *The dust table, with the example selector highlighted.*  
   Predict: “Move the cabin out into the vacuum just outside a heavy body, where there is no matter at all and no cosmological constant. How much of the table is Weyl there?”  
   Say: “Now I move the cabin out into the vacuum just outside a heavy body, with no cosmological constant. Say what the Ricci segment holds there and what the Weyl share readout will say.”  
   Describe: The dust table, with the example selector highlighted.
6. `vacuum-is-all-weyl` (working, await none) state: preset="star-exterior-table", progress=1  
   *The star-exterior example: six nonzero entries reading minus 2, 1, 1, minus 1, minus 1 and 2; the Weyl share reads 1.*  
   Say: “Out in that vacuum the Ricci numbers are all zero, so the Weyl tensor equals the whole Riemann tensor and the Weyl share readout reads one. The six nonzero entries read minus 2, 1, 1, minus 1, minus 1 and 2 in units of the curvature scale. The first is the stretch along the line to the body, twice as big as either squeeze across it, and opposite in sign.”  
   Describe: Six nonzero entries with values minus 2, 1, 1, minus 1, minus 1 and 2. The Weyl share readout reads one.
7. `five-directions-split` (working, await none) state: preset="five-dimensions-weyl", progress=1  
   *Dimension five: the bar reads 15 blue and 35 orange out of 50.*  
   Say: “One more step, to five directions. The table keeps fifty numbers, and the bar reads fifteen Ricci against thirty-five Weyl. The Ricci share is a symmetric array, which grows like the square of the number of directions. The Weyl share grows faster, so past four directions most of the curvature is what matter at the spot leaves free.”  
   Describe: A bar reading fifteen Ricci against thirty-five Weyl, out of fifty.

## Design rules

- **Never show a survivor count while a stage's sweep is running; the counters appear only when the sweep finishes.** Because: A half-swept grid gives a number that is not the answer to any rule, and learners quote the number they saw.
- **Keep the cyclic identity as a separate stage that the learner must apply; never fold it into the pair-exchange stage, and hold the counter at 21 until it is applied.** Because: The three pair rules feel complete, and stopping there is the commonest way to report 21 components in spacetime. Prevents `symmetries-and-identities/misconceptions/pair-rules-finish-the-count`.
- **Keep the cyclic stage reachable for one, two and three directions, where it greys nothing, draws no link, and leaves the counter where it was.** Because: Learners assume a rule that exists must remove something everywhere; seeing the counter refuse to move is the cheapest correction. Prevents `cyclic-identity/misconceptions/rule-cuts-the-space-count`.
- **Show the table only with all four indices down, and offer no control that raises one.** Because: Antisymmetry in the first pair holds for the lowered tensor, not for the tensor with its first index up, and a grid that greyed slots of the mixed tensor would teach a false rule. Prevents `symmetries-of-the-riemann-tensor/misconceptions/mixed-tensor-antisymmetric`.
- **Draw every link with its sign in line style as well as colour: solid for a copy, dashed for an opposite.** Because: A copy and an opposite are different facts, and colour alone fails in print and for colour-blind learners.
- **Grey a square only when a rule forces it to zero. A square a rule merely ties to another keeps its colour and gains a link line.** Because: Greying a tied square would say its number is zero rather than a copy of a number elsewhere, hiding that the survivors fix the whole table. Prevents `symmetries-of-the-riemann-tensor/misconceptions/every-slot-is-new`.
- **Whenever the counter reaches 20, print beside it that these are twenty numbers at one spot, tied to neighbouring spots by the Bianchi identity and to matter by the field equation.** Because: A counter that stops at twenty invites the reading that a spacetime carries twenty freely chosen functions. Prevents `riemann-curvature-tensor/misconceptions/twenty-components-are-twenty-freedoms`.
- **Keep one direction on the dimension slider, where every square is grey and the counter reads zero.** Because: A coiled hose looks curved, and the count of zero is the shortest statement that bending a line in a surrounding space is not intrinsic curvature. Prevents `number-of-independent-riemann-components/misconceptions/bent-line-is-curved`.
- **Whenever an example table is loaded, name its orthonormal frame on screen and keep the frame-turn control beside it, with the counters and the Weyl share visibly holding still while the entries change.** Because: Entries are components in a chosen frame; without a turnable frame the numbers on screen read as facts about the place rather than about the frame. Prevents `number-of-independent-riemann-components/misconceptions/components-are-invariants`.
- **Hide the Ricci and Weyl bar and the Weyl share for one and two directions, and label the bar as empty of Weyl in three.** Because: The Weyl tensor is defined only for three or more directions, and an empty orange segment in three directions is a result, not a missing feature. Prevents `weyl-tensor/misconceptions/three-dimensions-conformally-flat`.

## Model

Everything on screen is combinatorics on index slots plus a handful of small explicit curvature tables. For $n$ directions the grid has $n^4$ slots, one per ordered quadruple $(\rho,\sigma,\mu,\nu)$ of the lowered tensor $R_{\rho\sigma\mu\nu}$, read as reading direction, arrow direction, and the loop's two edges in order. Each stage applies one symmetry: a slot is greyed when a rule forces it to zero, and linked with a sign when a rule ties it to another. The survivor count is computed in closed form and cross-checked by an explicit union-find sieve over all $n^4$ slots. Example tables are stored as their independent components in a named orthonormal frame, in units of a curvature scale reported separately in inverse metres squared; the frame-turn control rotates them in the plane of directions $1$ and $2$.

**Slots in the grid**

$$
\#\text{slots} = n^4
$$

Holds when: $n$ directions at one point; the tensor has all four indices down.

**The two antisymmetries**

$$
R_{\rho\sigma\mu\nu} = -R_{\sigma\rho\mu\nu} = -R_{\rho\sigma\nu\mu}
$$

Holds when: Levi-Civita connection of a metric; both rules hold for the tensor with all indices down, and the first-pair rule fails for the tensor with its first index up.

**Pair exchange**

$$
R_{\rho\sigma\mu\nu} = R_{\mu\nu\rho\sigma}
$$

Holds when: Follows from the two antisymmetries together with the cyclic identity; it is not independent of them.

**Cyclic identity**

$$
R^\rho{}_{\sigma\mu\nu} + R^\rho{}_{\mu\nu\sigma} + R^\rho{}_{\nu\sigma\mu} = 0
$$

Holds when: Torsion-free connection, $\Gamma^\lambda{}_{\mu\nu} = \Gamma^\lambda{}_{\nu\mu}$; no metric is needed. The sum vanishes identically unless all four indices differ, so it adds a new relation only for $n \ge 4$.

**Independent components**

$$
N_R(n) = \frac{N(N+1)}{2} - \binom{n}{4} = \frac{n^2(n^2-1)}{12},\qquad N = \frac{n(n-1)}{2}
$$

Holds when: $N$ is the number of unordered index pairs, that is, of tilts. Gives 0, 1, 6, 20 and 50 for $n = 1$ to $5$.

**Counts at each stage**

$$
n^4 \;\to\; n^2 N \;\to\; N^2 \;\to\; \tfrac12 N(N+1) \;\to\; \tfrac12 N(N+1) - \tbinom{n}{4}
$$

Holds when: The greyed count is $n^3$ after the last-pair rule and $2n^3 - n^2$ after both; pair exchange and the cyclic identity grey nothing further, they only link.

**Ricci and Weyl shares**

$$
\frac{n^2(n^2-1)}{12} = \frac{n(n+1)}{2} + \frac{n(n+1)(n+2)(n-3)}{12}
$$

Holds when: For $n \ge 3$, where the Weyl tensor is defined; the split is 6 and 0 for $n = 3$, 10 and 10 for $n = 4$, and 15 and 35 for $n = 5$.

**Weyl tensor**

$$
R_{\rho\sigma\mu\nu} = C_{\rho\sigma\mu\nu} + g_{\rho\mu}P_{\sigma\nu} - g_{\rho\nu}P_{\sigma\mu} - g_{\sigma\mu}P_{\rho\nu} + g_{\sigma\nu}P_{\rho\mu},\qquad P_{\mu\nu} = \frac{1}{n-2}\Big(R_{\mu\nu} - \frac{R}{2(n-1)}g_{\mu\nu}\Big)
$$

Holds when: $n \ge 3$. The Weyl tensor is trace-free on every pair of slots and inherits all four Riemann symmetries.

**Weyl share readout**

$$
\text{share} = \frac{C_{\rho\sigma\mu\nu}C^{\rho\sigma\mu\nu}}{R_{\rho\sigma\mu\nu}R^{\rho\sigma\mu\nu}}
$$

Holds when: Reported only when $R_{\rho\sigma\mu\nu}R^{\rho\sigma\mu\nu} \ne 0$ and $n \ge 3$. For the built-in examples it is $0$ for the evenly curving space and the dust cloud, and $1$ outside the star and for the made-up trio, where the Ricci tensor vanishes and $C = R$.

**Outside a spherical mass**

$$
\mathcal E_{ij} = \frac{GM}{r^3}\,\mathrm{diag}(-2,1,1),\qquad R_{\hat\imath\hat 0\hat\jmath\hat 0} = \mathcal E_{ij}/c^2,\qquad R_{\hat\imath\hat\jmath\hat k\hat l} = \delta_{ik}\tilde{\mathcal E}_{jl} + \delta_{jl}\tilde{\mathcal E}_{ik} - \delta_{il}\tilde{\mathcal E}_{jk} - \delta_{jk}\tilde{\mathcal E}_{il}
$$

Holds when: Static observer's orthonormal frame, direction $1$ toward the star, $\tilde{\mathcal E} = \mathcal E/c^2$ in units of the curvature scale $GM/c^2r^3$. Entries in those units are $R_{0101} = -2$, $R_{0202} = R_{0303} = 1$, $R_{1212} = R_{1313} = -1$, $R_{2323} = 2$, and the Kretschmann scalar is $48$, matching $48G^2M^2/c^4r^6$.

**Inside evenly spread dust at rest**

$$
R_{\hat 0\hat\imath\hat 0\hat\imath} = \tfrac13,\qquad R_{\hat\imath\hat\jmath\hat\imath\hat\jmath} = \tfrac23\quad\text{in units of } 4\pi G\rho/c^2
$$

Holds when: Comoving observer's orthonormal frame, dust of mass density $\rho$ at rest, no pressure and no cosmological constant. Built from $R_{\mu\nu} = 8\pi G(T_{\mu\nu} - \tfrac12 T g_{\mu\nu})/c^4$ with $C = 0$; it reproduces $R_{\hat 0\hat 0} = 4\pi G\rho/c^2$ and $R_{\hat\imath\hat\jmath} = 4\pi G\rho\,\delta_{ij}/c^2$.

**The made-up trio**

$$
R_{0123} = 3,\quad R_{0231} = -1,\quad R_{0312} = -2,\quad\text{all other independent entries } 0
$$

Holds when: In units of a curvature scale of one per metre squared. It satisfies both antisymmetries, pair exchange and, with the third entry at minus two, the cyclic identity; its Ricci tensor vanishes, so it is a pure Weyl tensor, with $R_{\rho\sigma\mu\nu}R^{\rho\sigma\mu\nu} = -112$ in signature $(-,+,+,+)$.

**Turning the frame**

$$
e_{\hat 1}' = \cos\varphi\, e_{\hat 1} + \sin\varphi\, e_{\hat 2},\qquad e_{\hat 2}' = -\sin\varphi\, e_{\hat 1} + \cos\varphi\, e_{\hat 2}
$$

Holds when: Rotation of the spatial frame only; all four indices are transformed. Counts, the Ricci and Weyl split, the Weyl share and the cyclic sum are unchanged.

**Method:** Counts are evaluated in closed form and independently verified by brute force: the component enumerates all $n^4$ slots, marks those with a repeated index inside a pair as zero, merges the rest into equivalence classes under the two antisymmetries and pair exchange with a sign attached to each member, and then subtracts one class representative for each set of four distinct indices. The two counts must agree exactly for $n = 1$ to $5$ or the component throws. Example tables are stored as their independent components in the named frame; the full array is reconstructed by antisymmetrization, and the Ricci tensor, the Weyl tensor and the full contractions are formed with $\eta = \mathrm{diag}(-1,1,1,1)$ in exact rational arithmetic where the stored values are rational. The frame turn applies an exact rotation matrix to all four slots.

| Test | State | Expect | Hidden | Note |
| --- | --- | --- | --- | --- |
| `spacetime-all-slots` | preset="all-slots-spacetime", progress=1 | independent-count = 256 ±0; live-slots = 256 ±0; zero-slots = 0 ±0; pair-count = 6 ±0 | slot-value, copy-sign, cyclic-sum, curvature-scale, weyl-share, ricci-count, weyl-count, tide-meter-numbers, missing-from-tide-meter | The starting grid: $4^4 = 256$ slots, nothing greyed, and no example loaded so no value readouts. |
| `spacetime-last-pair` | preset="last-pair-swept", progress=1 | independent-count = 96 ±0; live-slots = 192 ±0; zero-slots = 64 ±0 | — | Last-pair antisymmetry greys $n^3 = 64$ slots and leaves $n^2 N = 16 \times 6 = 96$ numbers. |
| `spacetime-both-pairs` | preset="both-pairs-swept", progress=1 | independent-count = 36 ±0; live-slots = 144 ±0; zero-slots = 112 ±0 | — | Both antisymmetries grey $2n^3 - n^2 = 112$ slots and leave $N^2 = 36$ numbers. |
| `spacetime-pairs-folded` | preset="pairs-folded", progress=1 | independent-count = 21 ±0; live-slots = 144 ±0; pair-count = 6 ±0 | — | Pair exchange folds a $6 \times 6$ array onto its diagonal: $N(N+1)/2 = 21$. No further slot is greyed. |
| `spacetime-all-four-rules` | preset="cyclic-applied", progress=1 | independent-count = 20 ±0; cyclic-relations = 1 ±0; live-slots = 144 ±0; zero-slots = 112 ±0 | ricci-count, weyl-count, tide-meter-numbers, missing-from-tide-meter, slot-value, cyclic-sum, weyl-share, curvature-scale | $\binom44 = 1$ relation, so $21 - 1 = 20$. With the bar and overlay off and no example loaded, those readouts are absent. |
| `no-count-mid-sweep` | preset="cyclic-applied", progress=0.5 | — | independent-count, live-slots, zero-slots, cyclic-relations, cyclic-sum | Design rule count-only-at-the-end-of-a-sweep: half-swept grids report nothing. |
| `surface-keeps-one` | preset="surface", progress=1 | independent-count = 1 ±0; pair-count = 1 ±0; cyclic-relations = 0 ±0; live-slots = 4 ±0; zero-slots = 12 ±0 | ricci-count, weyl-count, weyl-share | $n = 2$: $2^2(2^2-1)/12 = 1$. The Weyl split is undefined below three directions, so its readouts are absent. |
| `space-keeps-six` | preset="space", progress=1 | independent-count = 6 ±0; pair-count = 3 ±0; cyclic-relations = 0 ±0; live-slots = 36 ±0; zero-slots = 45 ±0 | cyclic-sum | $n = 3$: $9 \times 8/12 = 6$, and $\binom34 = 0$, so the fourth rule removes nothing. With fewer than four directions there is no cyclic trio to sum. |
| `space-before-the-fourth-rule` | preset="space", stage="pair-exchange", progress=1 | independent-count = 6 ±0 | — | The count is already 6 before the cyclic stage, which is exactly what the entry tour asks the learner to predict. |
| `a-line-keeps-none` | preset="a-line", progress=1 | independent-count = 0 ±0; live-slots = 0 ±0; zero-slots = 1 ±0; pair-count = 0 ±0 | ricci-count, weyl-count, weyl-share, cyclic-sum | Boundary case $n = 1$: the single slot $R_{0000}$ is greyed, and $1 \times 0/12 = 0$. |
| `five-dimensions-all-four-rules` | preset="five-dimensions", progress=1 | independent-count = 50 ±0; pair-count = 10 ±0; cyclic-relations = 5 ±0; live-slots = 400 ±0; zero-slots = 225 ±0 | — | Boundary case at the top of the slider: $55 - \binom54 = 55 - 5 = 50 = 25 \times 24/12$. |
| `five-dimensions-pairs-only` | preset="five-dimensions", stage="pair-exchange", progress=1 | independent-count = 55 ±0 | — | The 55 a learner reports who stops at pair exchange; the tour asks for the difference. |
| `weyl-bar-spacetime` | preset="weyl-bar-spacetime", progress=1 | ricci-count = 10 ±0; weyl-count = 10 ±0; independent-count = 20 ±0 | weyl-share, curvature-scale | $n(n+1)/2 = 10$ and $n(n+1)(n+2)(n-3)/12 = 10$. Without a loaded example there is no share to report. |
| `weyl-bar-five-dimensions` | preset="five-dimensions-weyl", progress=1 | ricci-count = 15 ±0; weyl-count = 35 ±0; independent-count = 50 ±0 | — | $5 \times 6/2 = 15$ and $5 \times 6 \times 7 \times 2/12 = 35$, summing to 50. |
| `evenly-curving-space-is-all-ricci` | preset="even-space-table", progress=1 | ricci-count = 6 ±0; weyl-count = 0 ±0; independent-count = 6 ±0; weyl-share = 0 ±1e-12; curvature-scale = 1 ±1e-12 | cyclic-sum | $n = 3$: Weyl vanishes identically, so the bar is all Ricci and the share is exactly zero. The scale is $1/a^2$ with $a$ one metre. |
| `star-exterior-radial-entry` | preset="star-exterior-table", focus="s0101", progress=1 | slot-value = -2 ±1e-09; copy-sign = 1 ±0; weyl-share = 1 ±1e-12; cyclic-sum = 0 ±1e-12; curvature-scale = 5.732836506705128e-10 (rel 1e-09) | — | Negative branch of the signed value: $R_{\hat 0\hat 1\hat 0\hat 1} = -2GM/c^2r^3$, the radial stretch. The scale is $GM/c^2r^3$ at $r = 2GM/c^2$ for ten solar masses, that is $1/(8 (GM/c^2)^2)$ with $GM/c^2 = 14766.250385$ metres. |
| `star-exterior-crosswise-entry` | preset="star-exterior-table", focus="s2323", progress=1 | slot-value = 2 ±1e-09; copy-sign = 1 ±0 | — | Positive branch of the signed value: the purely crosswise entry is $+2GM/c^2r^3$, opposite in sign to the radial one. |
| `star-exterior-swapped-slot` | preset="star-exterior-table", focus="s1001", progress=1 | slot-value = 2 ±1e-09; copy-sign = -1 ±0 | — | Negative branch of the copy sign: $R_{1001} = -R_{0101} = +2$ by first-pair antisymmetry. |
| `forced-zero-slot-has-no-copy-sign` | preset="star-exterior-table", focus="s0011", progress=1 | slot-value = 0 ±1e-12 | copy-sign | $R_{0011} = 0$ by last-pair antisymmetry, and a greyed slot belongs to no group, so no copy sign is offered. |
| `turned-frame-keeps-the-count` | preset="star-exterior-table", frame-turn=45, focus="s0101", progress=1 | slot-value = -0.5 ±1e-09; independent-count = 20 ±0; weyl-share = 1 ±1e-12 | — | Turning the frame by 45 degrees in the 1-2 plane sends $\mathcal E_{11}$ from $-2$ to $-2\cos^2\varphi + \sin^2\varphi = -0.5$, while the count and the share hold still. |
| `turned-frame-crosswise-entry` | preset="star-exterior-table", frame-turn=45, focus="s2323", progress=1 | slot-value = 0.5 ±1e-09 | — | $R_{2323} = \mathcal E_{22} + \mathcal E_{33} = -0.5 + 1 = 0.5$ in the turned frame, against $2$ in the aligned one. |
| `dust-time-space-entry` | preset="dust-table", focus="s0101", progress=1 | slot-value = 0.3333333333 ±1e-09; weyl-share = 0 ±1e-12; curvature-scale = 2.146357290217611e-09 (rel 1e-06) | — | Conformally flat, so the share is exactly zero. The scale is $4\pi G\rho/c^2$ for $\rho = 2.3\times10^{17}$ kilograms per cubic metre. |
| `dust-purely-spatial-entry` | preset="dust-table", focus="s2323", progress=1 | slot-value = 0.6666666667 ±1e-09 | — | Twice the time-space entry, which is what makes $R_{\hat 0\hat 0} = 3 \times \tfrac13$ and $R_{\hat\imath\hat\imath} = -\tfrac13 + \tfrac23 + \tfrac23$ both equal one. |
| `flat-spacetime-is-all-zero` | preset="flat-table", focus="s0101", progress=1 | slot-value = 0 ±1e-12; cyclic-sum = 0 ±1e-12; curvature-scale = 0 ±1e-12; independent-count = 20 ±0 | weyl-share | Flat limit: every entry is zero while the count of slots the rules leave is still 20. The Weyl share is not reported, because $R_{\rho\sigma\mu\nu}R^{\rho\sigma\mu\nu} = 0$. |
| `ball-surface-table` | preset="ball-surface-table", focus="s0101", progress=1 | slot-value = 1 ±1e-09; copy-sign = 1 ±0; independent-count = 1 ±0; curvature-scale = 1 ±1e-12 | cyclic-sum, weyl-share, ricci-count, weyl-count | The one surviving number on a surface is the Gaussian curvature: $R_{\hat1\hat2\hat1\hat2} = K = 1/a^2 = 1$ per metre squared for $a$ one metre. |
| `cyclic-trio-first-entry` | preset="cyclic-trio-table", focus="s0123", progress=1 | slot-value = 3 ±1e-09; cyclic-sum = 0 ±1e-12; weyl-share = 1 ±1e-12; curvature-scale = 1 ±1e-12 | — | The trio's Ricci tensor vanishes, so it is pure Weyl and the share is one even though $R_{\rho\sigma\mu\nu}R^{\rho\sigma\mu\nu} = -112$. |
| `cyclic-trio-second-entry` | preset="cyclic-trio-table", focus="s0231", progress=1 | slot-value = -1 ±1e-09 | — | Negative branch of the value readout on the trio. |
| `cyclic-trio-third-entry` | preset="cyclic-trio-table", focus="s0312", progress=1 | slot-value = -2 ±1e-09; cyclic-sum = 0 ±1e-12 | — | $3 + (-1) + (-2) = 0$: the third entry is fixed by the other two. |
| `cyclic-trio-pair-exchange-partner` | preset="cyclic-trio-table", focus="s2301", progress=1 | slot-value = 3 ±1e-09; copy-sign = 1 ±0 | — | Pair exchange: $R_{2301} = R_{0123} = 3$, a copy rather than an opposite. |
| `broken-cyclic-sum-positive` | preset="cyclic-trio-free", third-entry=0, focus="s0312", progress=1 | cyclic-sum = 2 ±1e-09; slot-value = 0 ±1e-12 | — | Positive branch of the sum readout: $3 + (-1) + 0 = 2$, which no torsion-free space allows. |
| `broken-cyclic-sum-negative` | preset="cyclic-trio-free", third-entry=-4, focus="s0312", progress=1 | cyclic-sum = -2 ±1e-09; slot-value = -4 ±1e-09 | — | Negative branch of the sum readout: $3 + (-1) + (-4) = -2$, with the third entry at the bottom of its range. |
| `cyclic-sum-survives-a-turned-frame` | preset="cyclic-trio-table", frame-turn=45, progress=1 | cyclic-sum = 0 ±1e-09; independent-count = 20 ±0 | — | The identity is a tensor equation, so turning the frame cannot break it even though individual entries move. |
| `tide-meter-overlay` | preset="tide-meter-overlay", progress=1 | tide-meter-numbers = 6 ±0; missing-from-tide-meter = 14 ±0; independent-count = 20 ±0 | — | The nine drift readings of a non-spinning tide meter are symmetric, so they hold $3 \times 4/2 = 6$ numbers; $20 - 6 = 14$ lie outside them. |

## Serves

- [[number-of-independent-riemann-components]]: the whole sieve and the dimension slider: the counter falling 256, 96, 36, 21, 20 in spacetime, and the sequence 0, 1, 6, 20, 50 as the slider runs from one to five directions, with the times-table view showing $N(N+1)/2 - \binom n4$ and the tide-meter overlay showing which six of the twenty one falling crew can read
- [[symmetries-of-the-riemann-tensor]]: the first three stages: each antisymmetry greying the squares that would need one direction twice, the solid and dashed links with their copy signs, and pair exchange folding the array of tilts onto its diagonal
- [[cyclic-identity]]: the fourth stage and the made-up trio: three squares lighting together, the sum readout at zero, the unlock control that breaks the sum, and the dimension slider showing the rule taking nothing away below four directions and five relations at five
- [[riemann-curvature-tensor]]: the grid itself as the meaning of the tensor: one square per choice of reading direction, arrow direction and loop tilt, with the tilt counter going from one on a surface to three in space and six in spacetime
- [[weyl-tensor]]: the stacked bar splitting the survivors into Ricci and Weyl, 6 and 0 in three directions, 10 and 10 in four, 15 and 35 in five, with the Weyl share readout at zero inside evenly spread dust and one outside a star

## In the visual network

- **Builds on:** [[four-legs-around-a-tiny-loop]], [[carry-an-arrow-around-a-loop]]
- **Leads to:** [[falling-ring-of-crumbs]], [[six-entry-curvature-table]], [[coordinate-knobs-and-metric-dials]]

## Accessibility

Every stage announces what it greyed, what it linked and the new count, so the sieve can be followed with no picture at all. Links are drawn solid for a copy and dashed for an opposite, never by colour alone, and greyed squares also carry a hatch. The lit square is read out by its four direction names, its value and its copy sign, and the whole grid can be walked with the arrow keys.

Static alternative: A grid of 256 squares for spacetime, with 112 of them greyed by the two antisymmetries, folded by pair exchange into a symmetric six by six table of index pairs, and cut by one cyclic relation to leave twenty independent numbers.

- `1 to 5`: set the number of directions
- `Space`: apply the next rule and sweep it across the grid
- `Backspace`: undo the last rule
- `Arrow keys`: move the lit square; its four directions, value and copy sign are read out
- `P`: switch between the slot grid, the times table of index pairs, and both
- `E`: cycle through the example tables
- `W`: show or hide the Ricci and Weyl bar
- `T`: show or hide the tide-meter overlay

## Starting material

Earlier course assets: `lab-riemann-independent-components`, `figure-curvature-count`, `figure-ricci-weyl`, `manuscript-section-8-4-8-6-flatness-count-sphere-curvature`

The earlier course's component-counting lab already enumerates the slots and applies the symmetries for a chosen dimension; its enumeration can be ported as the brute-force cross-check behind the closed-form counts. Its counting figure becomes the static card. New work: the sweep animation, the signed link lines, the folded times-table view, the example tables with a turnable frame, the Ricci and Weyl bar and the tide-meter overlay.

## Review: novice

**Verdict:** needs-attention (2026-09-16, revision 1)

**Retell attempt:** A curvature table lives at every spot in space and time, and it says how an arrow you carry around a tiny loop comes back changed. On screen it is a big grid, 256 pale blue squares. I got 256 because there are four directions, time, ahead, left and up, and each square picks one of them four times over. I could not tell you what the four picks are for, though. The tutor said each square makes four choices and then went straight on. Then four rules switch on one at a time. First, walking a loop the other way flips the change, so a loop that uses one direction twice is zero, and 64 squares go grey. Second is the lean rule: two arrows taped at a right angle, one leans toward the other exactly as far as the other leans away, so swapping the arrow's two directions flips the entry, and 48 more squares go grey. Third is the mirror rule: swap the loop's tilt with the arrow's tilt and the entry is the same, so a six by six times table folds onto its diagonal. Fourth is the cyclic identity, which ties three squares whose four directions are all different, and their three numbers add up to nothing. The counter goes 256, 96, 36, 21, 20. I can follow the greying, but I cannot follow the counter. Sixty-four squares go grey and it drops from 256 to 96, which is not 256 take away 64. Forty-eight more go grey and it drops to 36. I would have to guess that the pairs and links are doing something, and I would not be able to say what. At the end the tutor changes the number of directions. A surface keeps 1 number, space keeps 6, a line keeps 0 like a garden hose you can straighten out. In space the fourth rule takes nothing away, because it needs four different directions and space has only three. I liked that a rule can be true and still take nothing away.

- Stumble: “Each square makes four choices, one direction for each of its four slots. Four times four times four times four gives 256.”: The four slots are never said to be slots for what. From the ways I have read, an entry needs a loop's tilt and an arrow's starting direction, which is three directions, not four. So 256 looked like the wrong number until much later, in a different tour.
- Stumble: “Space and time have four directions: time, ahead, left and up.”: Whose left? Left has no reference here, and the whole grid is labelled with it.
- Stumble: “So a loop whose two directions are the same is not a loop at all, and its entry is zero.”: The so does not follow. Walking the other way flipping the change does not by itself say a repeated direction gives zero, and I spent the next beat wondering what I had missed.
- Stumble: “The rest pair up. ... The counter has fallen to 96.”: 256 take away 64 is 192, not 96. Nothing says that a pair only needs one number, so the counter looked broken.
- Stumble: “Another 48 squares go dark grey. The counter reads 36.”: Same trouble again, and worse: 96 take away 48 is 48, not 36. I could not work out where 36 came from.
- Stumble: “So swapping the arrow's two directions flips the entry”: The arrow's two directions have not been named in this tour. I know the arrow has a starting direction; I do not know what the second one is.
- Stumble: “The first slot is the reading direction, which here is time.”: Reading direction is a new term used as if I already had it. The ways I read call it the direction the change is read in, so I did not connect the two.
- Stumble: “That means this square holds its group's own number.”: Group has not been introduced. I did not know which squares are in a group with this one.
- Stumble: “the four that are left all hold the same number, up to sign”: Up to sign is shop talk. It also sounds as if they all hold the same number, which the dashed lines had just told me is not so.
- Stumble: “Those three squares light up and join with solid orange lines.”: Three beats earlier I was told a solid orange line means two squares hold the same number. So I read the cyclic trio as three copies of one number, which is the opposite of what the next sentence says.
- Stumble: “Its loop runs along time and along time again, the same direction twice.”: The square is 0011. By the order the tutor taught me two beats earlier, its last two digits are the loop, and they are ahead and ahead, not time and time. The pair that is time and time is the arrow's. Not fixed here because it changes what the beat claims.
- Stumble: “You have three rules now: walking a loop the other way flips the change, the lean rule, and the mirror rule.”: The screen has gone back to the grid with only two sweeps on it, so the words and the picture disagree.
- Stumble: “In space there is more room, so a tiny loop at one spot can lie different ways”: More room sounds like more space to move about in, not more directions, which is the point.
- Stumble: “So past a surface, one number at a spot cannot say how a place curves.”: Past a surface points by position, and I could not tell whether past meant bigger, later or something else.
- Stumble: “every distance measured along it is the same as before”: Measured by whom, with what? The hose is the only thing in the picture and I cannot tell whether a tape along the hose or a ruler across the lawn is meant.
- Stumble: “The blue segment holds the ten Ricci numbers ... The orange segment holds the ten Weyl numbers”: Blue against orange is the only thing telling the two apart, in the speech and in the picture. Nothing in the design rules asks for a second cue on the bar, so in print or for a colour-blind learner the bar says nothing.
- Stumble: “the table still needs {value} separate numbers”: On a line the count is zero, and still needs 0 separate numbers sounds as if more are coming.
- Stumble: “the three linked entries add up to plus {abs}”: The whole point of the beat is that the sum is zero, and this template would say add up to plus zero.
- Stumble: “matter at the spot fixes {value} of them”: Them has no noun in earshot. The same trouble in the Weyl count and in both tide-meter readouts.
- Stumble: “the copy sign reads plus {abs}: the lit square is a copy of its surviving number”: Its surviving number reads as if the square had a number of its own that survived. And a colon is not something a voice can say.
- Stumble: “the Weyl part carries a share of {value} of this table”: A share of 0 and a share of 1 both sound like mistakes, because nothing says what the top of the scale is.
- Stumble: “Slot 0101”: The tour had just told me a square has four slots. So Slot 0101 sounded like one of those four, not like a whole square.
- Stumble: “Inside evenly spread dust at rest”: At rest compared with what? The tour says at rest around the cabin, but the control does not.
- Stumble: “Now I move the cabin outside a star, into vacuum”: The example the tutor loads is labelled on screen as the horizon of a ten-solar-mass black hole. The words and the control name different places.
- Fixed: Named the four slots of a square the first time the 256 count is spoken, so the count follows from something the learner can see.
- Fixed: Gave left its reference by putting the learner at the spot before the direction names are read out.
- Fixed: Replaced the non-sequitur behind the first greying with the reason the visual uses everywhere else: a loop needs two different directions.
- Fixed: Said that a pair needs only one number, and made the second drop read as a fall from 96 to 36 rather than a subtraction of 48.
- Fixed: Named the arrow's two directions where the lean rule is first spoken.
- Fixed: Introduced the reading direction with its meaning, in the words the ways use, in both tours that say it.
- Fixed: Explained what a group of squares is where the copy sign is first read out.
- Fixed: Dropped up to sign for a plain statement about copies and opposites.
- Fixed: Stopped calling the cyclic trio's links solid orange lines in speech, since that style had just been taught to mean a copy, and said instead that the lines run between all three at once.
- Fixed: Added the times-table reason for the fold, tying it to the way the learner has already read.
- Fixed: Made the mirror rule say unchanged everywhere, matching the glossary.
- Fixed: Said a tilt is a pair of two different directions, matching the glossary.
- Fixed: Acknowledged on screen that the grid is back to two sweeps when the tutor lists three rules.
- Fixed: Replaced more room with more directions, and past a surface with with three directions or more.
- Fixed: Gave the hose measurement its measurer and instrument.
- Fixed: Named the Ricci and Weyl segments by name rather than by colour in every spoken line and in every describe line of the Weyl tour, so the bar can be followed without colour.
- Fixed: Reworded the readouts that would misspeak at zero: the independent count, the zeroed-square count and the cyclic sum.
- Fixed: Gave them a noun in the Ricci, Weyl and two tide-meter readouts, and replaced the spoken colons in the copy-sign templates.
- Fixed: Said what the top of the scale is in the Weyl share readout.
- Fixed: Renamed the eight focus options from Slot to Square, so slot keeps its one meaning as one of a square's four positions.
- Fixed: Said what the dust is at rest with respect to, on the control as well as in the tour.
- Fixed: Made the two vacuum beats name the place the loaded example actually is, a heavy body's vacuum exterior, instead of a star.
- Concern: Beat three-rules-one-table/a-square-that-is-zero points at square 0011 and says its loop runs along time and along time again. By the slot order the visual teaches, 0011 has its loop along ahead and ahead; the pair that is time and time is the arrow's. Square 0011 is also zeroed by both antisymmetries at once, which blunts the one-rule point. Left unchanged because it changes a claim: either add a focus option such as 0100, whose loop alone repeats, or reword the beat to name the arrow's pair.
- Concern: The cyclic trio is drawn with solid orange lines, the same style the tour teaches three beats earlier for two squares that hold the same number. A third style, or a ring drawn around the trio, would stop the picture teaching a false reading. I only removed the style words from the speech.
- Concern: The Ricci and Weyl segments of the bar are told apart by colour alone. The link lines have a design rule requiring a second cue; the bar has none. Suggest a design rule that labels each segment in words or hatches one of them.
- Concern: The entry tour never shows the arithmetic behind 96 and 36. A learner can see 64 and 48 squares go grey and cannot reach either counter value. A visible count of pale squares beside the survivor counter, or one sentence of arithmetic, would close the gap; my wording only signals that a pair, and then a larger group, shares one number.
- Concern: The curvature-scale readout has decimals 12. Spoken aloud that is a dozen digits in a row. Suggest far fewer decimals with a spoken power-of-ten phrasing instead.
- Concern: Beat three-rules-one-table/predict-surface-and-space asks for the count with those three rules and nothing else, but the two answer beats load presets with all four rules applied. The numbers agree in two and three directions, so no claim is wrong, but the states do not match the question.
- Concern: The title and the print labels call a whole square a slot, while the tours call one of a square's four index positions a slot. I renamed the eight focus controls to Square, but left the title Twenty of 256 slots alone because it is the visual's name.
