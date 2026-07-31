> # ✅ APPLIED ADDENDUM — DO NOT RE-APPLY
>
> Every replacement pair in this file **has been applied to the master GDD**, and
> the master has moved on since. Its Old blocks no longer match, so re-applying is
> a no-op at best; its quoted "current" text, register extents, and open items are
> a **snapshot of the moment it was written**, not the state of the document.
>
> Specifically: R3's NEW block predates the applied CR-1 window change and still reads "turns 1–3". Re-applying it would revert the guided window.
>
> **The master GDD is the source of truth** — read `source/gdd.md`. Further changes
> to a merged section go in a *new* addendum file.

# Scenario & map design — post-merge-2 addendum (scenario-designer)

> **This file is an addendum, not a redraft.** `sections/scenario.md` is
> SUPERSEDED and must not be re-merged. Every change below is an exact
> old→new replacement passage against `source/gdd.md`
> (md5 `0eedea2dfd7b17a508e162427682ce64`). Nothing outside these pairs is
> proposed. Two violations are addressed and nothing else:
> **V1** §2.13.1's lane table vs. §2.13.5/§2.13.6 Symmetry rows (`contradiction`),
> **V2** §2.13.1's Causeway lane hexes with no antecedent (`invented-fact`).

## Placement

No new section. Eleven in-place replacements inside the merged **§2.13**:
four in **§2.13.1**, three in **§2.13.5**, three in **§2.13.6**, one in
**§2.13.7**. One new row (**Q24**) appended to the §4.7 open-questions table,
after Q23. No other section is touched.

---

## The ruling behind the fix (read this first)

The gate asked me to pick one of two options: correct the layouts so the
declared symmetry holds, or drop the declarations. Measuring the maps
produced a third fact that decides it for me:

**Both declared symmetries are geometrically impossible at the dimensions
declared, so neither layout could ever have been corrected in place.**

- **No odd-r rectangle has a vertical mirror axis, at any dimension.** Even
  rows occupy x = 0 … W−1 and are centred on (W−1)/2; odd rows are shifted
  +½ and are centred on W/2. The two centres differ by exactly ½ hex for
  every W, so one axis cannot serve both row parities. *Longwater March*
  could not be mirrored at 13×9, or at any other size.
- **An odd-r rectangle admits a 180° rotation only when the row count is
  even.** The rotation must pair row r with row H−1−r. With H odd those two
  rows have the *same* parity, so the even-row reflection (c ↔ W−1−c) and
  the odd-row reflection (c ↔ W−c) demand two different centres and column
  W−1 of every odd row has no image. With H **even** the parities alternate
  and the map closes exactly: **ρ(c, r) = (W−1−c, H−1−r)**. This is why the
  gate's own worked example lands where it does — on 9×9, (1,1) rotates to
  (6,7), leaving (7,7) unpaired and column 8 of every odd row with nowhere
  to go. *The Causeway* could not be rotational at 9×9 either.

So the fix is: **keep both symmetry declarations, change both maps to an even
row count, and redraw both layouts so ρ closes on every hex.** That preserves
both rationales the gate flagged as load-bearing — *Longwater*'s "factory
count is the only variable under test" and *The Causeway*'s "each seat's near
bridge on the opposite flank" — and, because ρ is an isometry, it equalises
the lanes as the gate expected. *Longwater March* becomes **13 × 8**;
*The Causeway* becomes **9 × 8**. Both match-length dials (§2.13.3: factory
count × home separation) are unchanged by the redraw — homes stay 10 and 6
hexes apart respectively — so both turn estimates stand.

**V2 is closed by the same redraw:** §2.13.6 now carries a full deployment
table in the shape §2.13.2 uses, so `guidedOpening.infantry` has an
antecedent and T-SCN-06/07/08 can be evaluated against *The Causeway*.

Re-measured lanes, cheapest legal path, Bridge-free, every entered hex
counted including the objective (§2.3 costs; T-SCN-06 accounting):

| Map | Seat | Path | Cost |
|---|---|---|---|
| *Longwater March* | West | (1,2)p → (1,1)p → (2,1)p → (3,1)p → **(4,1)F** | 1+1+1+1 = **4 MP** |
| *Longwater March* | East | (11,5)p → (11,6)p → (10,6)p → (9,6)p → **(8,6)F** | 1+1+1+1 = **4 MP** |
| *The Causeway* | West | (1,2)p → (1,1)**T** → (2,1)p → **(3,2)F** | 1+1+1 = **3 MP** |
| *The Causeway* | East | (7,5)p → (7,6)**T** → (6,6)p → **(5,5)F** | 1+1+1 = **3 MP** |

Each East path is the ρ-image of its West path hex for hex, which is the
check that the layout is genuinely symmetric rather than nearly so.

Worth naming, because it is the case the "measured, not inferred" rule exists
for: *The Causeway*'s West lane is **not** the shortest lane. (1,2) is 2 hexes
from (3,2), but the only 2-hex route runs through the Mountain perch at (2,2)
(cost 3, §2.3) for 4 MP. The 3-hex route through the town is cheaper. A
validator that counted hexes instead of pricing them would report the wrong
number and still go green.

Both stretch lanes are also **Q21-invariant**: no path hex above is occupied
by any of that seat's own five starting units, so the lane prices the same
whether the Director rules "terrain alone" or "board as deployed."

---

## Draft — replacement passages

### R1 — §2.13.1, validation-invariants bullet (V1)

**OLD**

```
- **Validation invariants** (for the §4.2 `validate_scenario` tool — schema
  per §4.7 Stub 7): every land-passable hex reaches every factory
  (Bridges are the only Water crossings, §2.3, and there is no sea unit —
  connectivity is a build-time check, not a hope); all deployment hexes are
  free and land-passable; factory count in the map file equals the count the
  domination check uses; declared symmetry (mirror/rotation/none) is
  machine-verified.
```

**NEW**

```
- **Validation invariants** (for the §4.2 `validate_scenario` tool — schema
  per §4.7 Stub 7): every land-passable hex reaches every factory
  (Bridges are the only Water crossings, §2.3, and there is no sea unit —
  connectivity is a build-time check, not a hope); all deployment hexes are
  free and land-passable; factory count in the map file equals the count the
  domination check uses; declared symmetry is machine-verified **in axial**
  (§4.7's T-SCN-05 forbids loaded state from holding `(col, row)` at all, so
  the check has no other place to run). The declarable values are
  **`rot180` or `none`** — `mirror` is not one of them, because an odd-r
  rectangle has no mirror axis at any dimension, and `rot180` is well-formed
  only on an **even row count** (see the symmetry note at the end of this
  section). Both constraints are pending Q24, §4.7.
```

---

### R2 — §2.13.1, lane table, rows 2 and 3 (V1, V2)

**OLD**

```
  | *Longwater March* | (1,3) → **(4,2)**, **3 MP** | (11,3) → **(8,2)**, **4 MP** |
  | *The Causeway* | (1,3) → **(3,2)**, **2 MP** | (6,5) → **(5,6)**, **3 MP** |
```

**NEW**

```
  | *Longwater March* | (1,2) → **(4,1)**, **4 MP** (all Plains) | (11,5) → **(8,6)**, **4 MP** (all Plains) |
  | *The Causeway* | (1,2) → **(3,2)**, **3 MP** (via the town at (1,1)) | (7,5) → **(5,5)**, **3 MP** (via the town at (7,6)) |
```

*(The *Ferrum Crossing* row is unchanged. The stretch rows are re-measured
against the redrawn 13×8 and 9×8 layouts in §2.13.5 and §2.13.6; each named
deployment hex is now a row in that map's deployment table, so every hex in
this table has an antecedent. Paths: *Longwater* West
(1,2)→(1,1)→(2,1)→(3,1)→(4,1); *Longwater* East (11,5)→(11,6)→(10,6)→(9,6)→(8,6);
*Causeway* West (1,2)→(1,1)→(2,1)→(3,2); *Causeway* East (7,5)→(7,6)→(6,6)→(5,5).
On *The Causeway* the cheapest lane is deliberately **not** the shortest: the
2-hex route crosses the Mountain perch at (2,2) for 4 MP, the 3-hex route
through the town costs 3.)*

---

### R3 — §2.13.1, "Slack is not uniform" bullet (V1)

**OLD**

```
  2. **Slack is not uniform.** *Ferrum Crossing* carries only 1 MP of slack
     against the 6, so a turn-1 move spent walking away from the lane pushes
     the pip to turn 3 — still inside the guided window (turns 1–3). The
     stretch maps carry 2–4 MP of slack.
```

**NEW**

```
  2. **Slack is not uniform.** *Ferrum Crossing* carries only 1 MP of slack
     against the 6, so a turn-1 move spent walking away from the lane pushes
     the pip to turn 3 — still inside the guided window (turns 1–3).
     *Longwater March* carries 2 MP of slack on both lanes, *The Causeway* 3
     on both; being symmetric, each carries the *same* slack in both seats,
     which is what makes them usable as controlled tests. Both stretch lanes
     are also clear of that seat's own four other starting units, so they
     price identically under either reading of Q21 (§4.7) — the shipped map
     is the only one whose numbers a Q21 ruling could move.
```

---

### R4 — §2.13.1, closing symmetry paragraph (V1 — the sentence that licenses the false inference)

**OLD**

```
  Declared symmetry does not imply equal lane cost: an odd-r grid's row
  offset means a mirrored or rotated layout can still price the two seats'
  lanes 1 MP apart (*Longwater March*: 3 MP west, 4 MP east). The validator
  therefore **measures and records each seat's cost as a number** rather than
  inferring it from the symmetry flag.
```

**NEW**

```
  **Declared symmetry does imply equal lane cost — and that is what makes it
  worth declaring.** A 180° rotation of a hex board is an isometry: it
  preserves hex distance, and because it maps every hex to a hex of identical
  terrain it preserves *path cost* too. On a genuinely symmetric map the two
  seats' lanes therefore cost exactly the same, and a 1 MP split is not an
  offset artefact — it is proof the layout is not symmetric. An earlier draft
  of this section argued the opposite from the odd-r row offset; that
  confused a storage convention with a geometry. §4.7's T-SCN-05 forbids
  loaded state from holding `(col, row)` at all, so the symmetry check
  necessarily runs in axial, where no offset exists and a declared symmetry
  is an isometry or it is nothing.

  Two facts about offset rectangles follow, and both stretch maps are drawn
  to them:

  1. **No odd-r rectangle has a mirror axis, at any dimension.** Even rows
     occupy columns 0…W−1 and are centred on (W−1)/2; odd rows sit ½ hex east
     and are centred on W/2. The centres differ by ½ hex for every W, so a
     single vertical axis cannot serve both parities. `mirror` is therefore
     not a declarable value (Q24, §4.7).
  2. **An odd-r rectangle admits a 180° rotation only when the row count is
     even.** The rotation pairs row r with row H−1−r. With H odd those rows
     share a parity, and the even-row reflection (c ↔ W−1−c) and the odd-row
     reflection (c ↔ W−c) then demand two different centres — column W−1 of
     every odd row is left without an image. With H even the parities
     alternate and the board closes exactly under
     **ρ(c, r) = (W−1−c, H−1−r)**. This is why *Longwater March* is 13 × **8**
     and *The Causeway* is 9 × **8** rather than nine rows each.

  The validator still **measures and records each seat's cost as a number**
  (T-SCN-08) rather than reading it off the symmetry flag. Not because the
  flag is untrustworthy in principle, but because it is an *authored
  declaration* and measurement is the only thing that catches it being wrong.
  That is exactly what it caught here: the flag said mirrored, the numbers
  said 3 and 4, and the numbers were right.
```

---

### R5 — §2.13.5 spec table, Dimensions and Symmetry rows (V1)

**OLD**

```
| Dimensions | 13 × 9 = 117 hexes |
```

**NEW**

```
| Dimensions | **13 × 8 = 104 hexes** — eight rows, not nine, because a 180° rotation only closes on an even row count (§2.13.1) |
```

**OLD**

```
| Symmetry | **Mirrored** — fair and admittedly dull; chosen so the factory-count dial is the only variable under test |
```

**NEW**

```
| Symmetry | **180° rotational**, ρ(c, r) = (12−c, 7−r) — fair and admittedly dull; chosen so the factory-count dial is the only variable under test. *Mirrored* was the earlier declaration and is withdrawn: no odd-r rectangle has a mirror axis (§2.13.1). Rotation costs this map nothing it wanted from mirroring — it is equally distance-preserving, so both seats' lanes cost 4 MP and the only asymmetry left is the one under test. |
```

---

### R6 — §2.13.5 layout grid (V1)

**OLD**

```
r0:  m  p  p  p  p  p  T  p  p  p  p  p  m
r1:   p  p  p  p  p  p  p  p  p  p  p  p  p
r2:  p  p  p  p  F  p  p  p  F  p  p  p  p
r3:   p  p  p  p  p  p  w  p  p  p  p  p  p
r4:  p  F  p  T  p  w  p  w  p  T  p  F  p
r5:   p  p  p  p  p  p  w  p  p  p  p  p  p
r6:  p  p  p  p  F  p  p  p  F  p  p  p  p
r7:   p  p  p  p  p  p  p  p  p  p  p  p  p
r8:  m  p  p  p  p  p  T  p  p  p  p  p  m
```

**NEW**

```
r0:  m  p  p  p  p  p  T  p  p  p  p  p  m
r1:   p  p  p  p  F  p  p  p  F  p  p  p  p
r2:  p  p  p  p  p  p  p  p  p  p  p  p  p
r3:   p  F  p  T  p  w  w  p  p  p  p  p  p
r4:  p  p  p  p  p  p  w  w  p  T  p  F  p
r5:   p  p  p  p  p  p  p  p  p  p  p  p  p
r6:  p  p  p  p  F  p  p  p  F  p  p  p  p
r7:   m  p  p  p  p  p  T  p  p  p  p  p  m
```

---

### R7 — §2.13.5 key-coordinates paragraph, plus the deployment table it never had (V1)

**OLD**

```
Homes (1,4)/(11,4); neutrals (4,2)(8,2)(4,6)(8,6); towns
(6,0)(3,4)(9,4)(6,8); central Woods knot (6,3)(5,4)(7,4)(6,5); corner
Mountains. Deployment mirrors Ferrum Crossing's pattern around each home
(flag on the outside edge, factory hex free). **No Water at all** — the map
that teaches what the chokepoint map can't: open-field maneuver, Recon (move
7) flanking wide, and expansion tempo deciding who holds 4-of-6 **factories**
at the cap. Criterion 2 counts factories *and* captured towns (§2.8), so this
map's denominator is **N = 10** — 6 factories + 4 towns, against N = 8 on
*Ferrum Crossing* (§2.11.4). The factory half of that spread is what the
extra neutrals buy: a **0–6 factory swing inside a 10-objective sort**, where
the shipped map can swing only 0–4.
```

**NEW**

```
**Key coordinates.** Home factories: West **(1,3)**, East **(11,4)** — 10
hexes apart, unchanged from the 13 × 9 draft, so §2.13.3's contact-turn
arithmetic is untouched. Neutral factories **(4,1)(8,1)(4,6)(8,6)** · Towns
**(6,0)(3,3)(9,4)(6,7)** · central Woods knot **(5,3)(6,3)(6,4)(7,4)** ·
corner Mountains **(0,0)(12,0)(0,7)(12,7)**.

Every one of those is a ρ-pair under ρ(c, r) = (12−c, 7−r), and the pairing
is the map's whole warrant: (1,3)↔(11,4) homes, (4,1)↔(8,6) and
(8,1)↔(4,6) neutrals, (3,3)↔(9,4) and (6,0)↔(6,7) towns, (5,3)↔(7,4) and
(6,3)↔(6,4) woods, (0,0)↔(12,7) and (12,0)↔(0,7) mountains. Rows 2 and 5 are
all Plains and map to each other. Note that ρ has no fixed hex on an even-row
board, so the homes sit on *different rows* (3 and 4) — that is the rotation
working, not a drafting slip.

**Terrain distribution (104 hexes):** Plains 86 · Woods 4 · Mountains 4 ·
Water 0 · Bridge 0 · Town 4 · Factory 6. Even more open than the shipped map
(83% Plains vs. 76%), which is the point: this is the maneuver map, and the
only terrain that slows anyone is the four-hex Woods knot standing between
the two home rows.

**Starting positions** (all on Plains; home factory hex left free; East is
the exact ρ-image of West, which is what "one variable at a time" means here):

| Unit | West | East |
|---|---|---|
| Flag Tank | (0,3) | (12,4) |
| Infantry ×2 | **(1,2)**, (1,4) | **(11,5)**, (11,3) |
| Artillery | (0,2) | (12,5) |
| Recon | (0,4) | (12,3) |

**Guided opening** (§2.13.1): `guidedOpening.infantry` = **(1,2)** West /
**(11,5)** East; `guidedOpening.objective` = **(4,1)** West / **(8,6)** East —
distinct objectives, 4 MP each, no Bridge on the map at all. 2 MP of slack
against the 6 MP ceiling, identical in both seats.

**No Water at all** — the map that teaches what the chokepoint map can't:
open-field maneuver, Recon (move 7) flanking wide, and expansion tempo
deciding who holds 4-of-6 **factories** at the cap. Criterion 2 counts
factories *and* captured towns (§2.8), so this map's denominator is
**N = 10** — 6 factories + 4 towns, against N = 8 on *Ferrum Crossing*
(§2.11.4). The factory half of that spread is what the extra neutrals buy: a
**0–6 factory swing inside a 10-objective sort**, where the shipped map can
swing only 0–4.
```

*(The 16–20-turn estimate and the "frequently reaching the cap" claim stand
unchanged: §2.13.3's two dials are factory count — still 6 — and home
separation — still 10 hexes. The board lost one row, 117→104 hexes, which
tightens the §2.7 board-space throttle very slightly in the same direction
the estimate already leans.)*

---

### R8 — §2.13.6 spec table, Dimensions and Symmetry rows (V1)

**OLD**

```
| Dimensions | 9 × 9 = 81 hexes |
```

**NEW**

```
| Dimensions | **9 × 8 = 72 hexes** — eight rows, not nine, because a 180° rotation only closes on an even row count (§2.13.1) |
```

**OLD**

```
| Symmetry | **180° rotational** — fair, and rotation (unlike mirroring) puts each seat's near bridge on the opposite flank, so seat-swap stays non-cosmetic even on a symmetric map |
```

**NEW**

```
| Symmetry | **180° rotational**, ρ(c, r) = (8−c, 7−r) — fair, and rotation puts each seat's near bridge on the opposite flank (West's is north at (4,2), East's is south at (4,5)), so seat-swap stays non-cosmetic even on a symmetric map. Rotation is not a preference here but the only symmetry an odd-r rectangle has (§2.13.1); the row count is even so that it actually closes. |
```

---

### R9 — §2.13.6 layout grid (V1)

**OLD**

```
r0:  p  p  p  p  ~  p  p  p  p
r1:   p  T  p  w  ~  p  p  p  p
r2:  p  p  m  F  B  p  p  p  p
r3:   p  p  p  w  ~  p  p  p  p
r4:  p  F  p  p  ~  p  p  F  p
r5:   p  p  p  p  ~  w  p  p  p
r6:  p  p  p  p  B  F  m  p  p
r7:   p  p  p  p  ~  w  p  T  p
r8:  p  p  p  p  ~  p  p  p  p
```

**NEW**

```
r0:  p  p  p  p  ~  p  p  p  p
r1:   p  T  p  w  ~  p  p  p  p
r2:  p  p  m  F  B  p  p  p  p
r3:   p  F  p  w  ~  p  p  p  p
r4:  p  p  p  p  ~  w  p  F  p
r5:   p  p  p  p  B  F  m  p  p
r6:  p  p  p  p  ~  w  p  T  p
r7:   p  p  p  p  ~  p  p  p  p
```

---

### R10 — §2.13.6 key-coordinates paragraph, plus the deployment specification T-SCN-07 needs (V1, V2)

**OLD**

```
Water fills column 4 end to end except Bridges (4,2) and (4,6) — **a full
bisection, the deliberate opposite of Ferrum Crossing.** Homes (1,4)/(7,4);
neutral factories (3,2) and (5,6) each guard the approach to their adjacent
bridge: +15% defense *and* a spawn point at the chokepoint (§2.7
build-and-spawn makes a held bridge-factory a reinforcement faucet exactly
where reinforcements matter). Woods overlook each bridge for defenders;
single Mountains (2,2)/(6,6) are Artillery perches — range 2–3 covers the
bridge hex from +40% cover with no counter (§2.3, §2.4).
```

**NEW**

```
Water fills column 4 end to end except Bridges **(4,2)** and **(4,5)** — **a
full bisection, the deliberate opposite of Ferrum Crossing.** Column 4 is its
own ρ-image, which is why the bisection survives the rotation intact. Homes
**(1,3)**/**(7,4)** — 6 hexes apart, unchanged. Neutral factories **(3,2)**
and **(5,5)** each guard the approach to their adjacent bridge from their own
seat's bank: +15% defense *and* a spawn point at the chokepoint (§2.7
build-and-spawn makes a held bridge-factory a reinforcement faucet exactly
where reinforcements matter). Woods **(3,1)(3,3)** flank the north bridge on
West's bank and **(5,4)(5,6)** flank the south bridge on East's; each seat's
own crossing is the one it defends from cover, and each seat's *far* landing —
(5,2) north, (3,5) south — is bare Plains, so attacking a bridge is always
the uncovered half of the trade. Single Mountains **(2,2)**/**(6,5)** are
Artillery perches — range 2–3 covers their bridge hex from +40% cover with no
counter (§2.3, §2.4), and reaches the far landing at range 3.

ρ-pairs, exhaustively: (1,1)↔(7,6) towns, (3,1)↔(5,6) and (3,3)↔(5,4) woods,
(2,2)↔(6,5) mountains, (3,2)↔(5,5) neutral factories, (1,3)↔(7,4) homes,
(4,2)↔(4,5) bridges, and the six Water hexes in pairs (4,0)↔(4,7),
(4,1)↔(4,6), (4,3)↔(4,4). Everything else is Plains.

**Terrain distribution (72 hexes):** Plains 52 · Woods 4 · Mountains 2 ·
Water 6 · Bridge 2 · Town 2 · Factory 4. The tightest board in the set, and
the only one where a single terrain type — Water — decides the topology.

**Starting positions** (all on Plains; home factory hex left free; East is
the exact ρ-image of West). *This map previously specified none, which left
§2.13.1's lane figures without an antecedent and made T-SCN-06/07/08
unevaluable against it:*

| Unit | West | East |
|---|---|---|
| Flag Tank | (0,3) | (8,4) |
| Infantry ×2 | **(1,2)**, (1,4) | **(7,5)**, (7,3) |
| Artillery | (0,2) | (8,5) |
| Recon | (0,4) | (8,3) |

**Guided opening** (§2.13.1): `guidedOpening.infantry` = **(1,2)** West /
**(7,5)** East; `guidedOpening.objective` = **(3,2)** West / **(5,5)** East.
Distinct objectives (T-SCN-07); 3 MP each, Bridge-free and confined to the
seat's own bank (T-SCN-06); 3 MP of slack. The West lane is
(1,2)→(1,1)→(2,1)→(3,2), through the town rather than over the Mountain at
(2,2) — the 2-hex route costs 4 MP and the 3-hex route costs 3, which is the
case T-SCN-08's "computes, never infers" wording exists for.

Note what the deployment does *not* do: neither seat starts within reach of a
bridge. West's forward Infantry at (1,2) is 3 hexes from (4,2); the guided
opening walks it away from the crossing, to a factory on its own bank. The
first lesson on the bisection map is still capture, not crossing — the map
earns its lockout premise from turn 3 onward, not turn 1.
```

---

### R11 — §2.13.7 summary table, rows 2 and 3 (V1)

**OLD**

```
| *Longwater March* | Stretch P1 (wk 4) | 13×9 | 5 | 6 | 4 | Mirrored | factory count → cap pressure | 16–20 |
| *The Causeway* | Stretch P2 (wk 4) | 9×9 | 5 | 4 | 2 | Rotational | bridge lockout → decisiveness | 8–12 |
```

**NEW**

```
| *Longwater March* | Stretch P1 (wk 4) | 13×8 | 5 | 6 | 4 | 180° rotational | factory count → cap pressure | 16–20 |
| *The Causeway* | Stretch P2 (wk 4) | 9×8 | 5 | 4 | 2 | 180° rotational | bridge lockout → decisiveness | 8–12 |
```

*(Both stretch maps now declare the same symmetry, which is the honest
outcome: `rot180` is the only symmetry an odd-r board has. The two maps stay
distinct on the columns that matter — factory count and topology — not on a
symmetry label. *Ferrum Crossing*'s row is unchanged and declares `none`.)*

---

### R12 — §4.7 open questions, new row appended after Q23

**OLD**

```
| **Q23** | ~~Milestone-vs-build-order contradiction.~~ **RULED (this revision).** §4.11's critical path makes the baseline AI (row 6) depend on row 5, which depends on row 4 Capture & Fame — but §4.4 promises a working vertical slice *with* the baseline AI in week 2, and §2.10 states capture + Fame production "land wk 3, not wk 1–2." The two schedules cannot both hold. | §4.4's week 1–2 milestones; §2.10's IN row; §4.11's critical path; and Q20, which is the same decision for save/replay | Ruled: the vertical-slice milestone moves to **week 3**, and week 2 delivers **move + attack only** (§4.4). §4.4, §2.10 and §4.11 now describe one schedule. |
```

**NEW**

```
| **Q23** | ~~Milestone-vs-build-order contradiction.~~ **RULED (this revision).** §4.11's critical path makes the baseline AI (row 6) depend on row 5, which depends on row 4 Capture & Fame — but §4.4 promises a working vertical slice *with* the baseline AI in week 2, and §2.10 states capture + Fame production "land wk 3, not wk 1–2." The two schedules cannot both hold. | §4.4's week 1–2 milestones; §2.10's IN row; §4.11's critical path; and Q20, which is the same decision for save/replay | Ruled: the vertical-slice milestone moves to **week 3**, and week 2 delivers **move + attack only** (§4.4). §4.4, §2.10 and §4.11 now describe one schedule. |
| **Q24** | Symmetry as a declarable value. §2.13.1 previously offered `mirror / rotation / none`, but an odd-r offset rectangle has **no** mirror axis at any dimension, and admits a 180° rotation only when the row count is even. So `mirror` is a value the validator could never legally accept, and `rot180` is only well-formed against an even-H map. Narrow the field to `rot180 \| none` with an even-row-count precondition, and make `rot180` on an odd row count a hard refusal rather than a failed hex comparison? | §2.13.1's validation-invariant list; Stub 7's `symmetry` field and T-SCN-08's fixtures (§4.7, `tech-director`-owned) | Narrowed, as §2.13.1 now reads: `rot180 \| none`, and `rot180` declared on an odd row count refuses the file with a reason (a wrong dimension is an authoring error, not a balance question). Both stretch maps are redrawn on 8 rows and declare `rot180` (§2.13.5, §2.13.6); *Ferrum Crossing* declares `none`. If the Director rules otherwise, the only consequence is that a bad declaration surfaces as N failed hex comparisons instead of one refusal — no layout moves. |
```

---

## Change requests

| Existing § | Current text | Proposed change | Why |
|---|---|---|---|
| §4.7, Stub 7, **T-SCN-08** | "The declared-symmetry flag (§2.13.1) is not an input and cannot substitute — an **odd-r row offset lets a mirrored or rotated layout price the two seats' lanes differently.** Fixtures: **a mirror-declared scenario whose lanes cost 3 and 4 PASSES** and reports both numbers (**Longwater March, §2.13.1**); one whose lanes both cost 7 FAILS." | Keep the invariant exactly as gated. Replace the *justification clause* with: "the flag is an authored declaration and the cost is a measurement; the validator reports the measurement so a wrong declaration surfaces as a number, not as a green boolean." Replace the pass fixture with one that no longer contradicts §2.13.5: a **`rot180`-declared scenario whose lanes both cost 4 PASSES and reports both numbers (*Longwater March*, §2.13.1)**; keep the "both cost 7 FAILS" ceiling fixture. Optionally add a third fixture — a `rot180`-declared map whose lanes measure 3 and 4 — which must now FAIL the symmetry check, since unequal lanes on a declared-symmetric map are proof the layout is broken. | The clause states the same false inference §2.13.1 has just retracted, and the pass fixture cites a map whose lanes are no longer 3 and 4. T-SCN-08's behaviour does not change — only its stated reason and its fixture data. `tech-director` owns the stub; I am not rewriting it. |
| §4.7, Stub 7, scenario schema | `symmetry` field, implicitly `mirror / rotation / none` per §2.13.1's old wording | Narrow the enum to `rot180 \| none`, with a precondition that `rot180` requires an even row count and refuses the file otherwise. Filed as **Q24**. | `mirror` is unrepresentable on an odd-r grid; a schema that can express it invites another map that declares it. |
| §4.7, **Q16** | "All three maps are priced on this reading." | No text change requested — confirming the claim still holds. Recon is priced as a land unit on both redrawn maps; *The Causeway*'s bisection and lockout premise depend on it exactly as before. | Flagging that the redraw does not weaken Q16's stated assumption, so nobody has to re-check it. |

---

## Open questions for the Director

1. **Q24 (new, filed above).** Narrow `symmetry` to `rot180 | none` with an
   even-row-count precondition? My assumption in force is *yes*; nothing in
   the layouts depends on the ruling.
2. **Two stretch maps now declare the same symmetry.** That is geometrically
   forced, but it costs the scenario set a talking point: the set no longer
   contrasts "mirrored vs. rotational." Is the contrast worth buying back by
   declaring *Longwater March* **`none`** and drawing it deliberately
   near-symmetric — accepting unequal lanes as a designed handicap rather
   than a bug? I recommend **no**: §2.13.5's entire purpose is to isolate
   factory count as the single variable, and an asymmetric long map cannot do
   that. Recorded because it is a real cost of the fix, not a free one.
3. **Q21 interaction, now narrowed.** Both stretch lanes are clear of their
   own seat's starting units, so a "board as deployed" ruling would move only
   *Ferrum Crossing*'s numbers. Q21 is now a one-map question rather than a
   three-map question; the Director may want to re-scope its "Blocks" column
   accordingly. I have not edited Q21.
4. **Q22 is unaffected but slightly better off.** On *The Causeway* each
   seat's objective is on its own bank behind a bisecting river, so the
   opposing seat's cheapest lane to the same tile must cross a bridge — the
   non-contention Q22 asks about holds *by topology* here even though the
   validator does not assert it. Worth knowing if Q22 is ever ruled "assert
   it": *The Causeway* would pass without a redraw.

---

## Handoffs

- **`tech-director`** — the two §4.7 change requests above (T-SCN-08's
  justification clause and pass fixture; the Stub 7 `symmetry` enum + Q24).
  T-SCN-08's fixture currently names lane costs 3 and 4 for *Longwater March*
  and will contradict §2.13.5 the moment this addendum merges. This is the
  only cross-lane dependency in the fix and it is a text/data change, not a
  behaviour change.
- **`rules-designer`** — nothing. No rule, cost, stat, or victory condition
  is touched; capture N stays an assumption in force under Q4.
- **`ux-onboarding-designer`** — informational only: §2.11.6-B's turn-2
  guided opening still holds on all three maps, with slack now 1 MP
  (*Ferrum*), 2 MP (*Longwater*), 3 MP (*Causeway*). No screen or copy
  change is implied.
- **Director / kb re-sync** — §2.13 changes again, so `kb/rules.md`'s parse of
  §2 needs the usual re-sync at merge (CLAUDE.md merge checklist step 3).

---

## Grounding

| Decision | Traced to |
|---|---|
| Symmetry check runs in axial, so a mirror must be an isometry | §4.7 T-SCN-05: "no authored file stores axial, and no loaded state stores (col, row)"; §4.7 Shared conventions, `q = col − (row − (row & 1)) / 2` |
| No odd-r rectangle has a mirror axis | Geometry of the odd-r convention as defined in §2.13.1 ("odd rows offset +½ hex east"): even-row centre (W−1)/2 vs. odd-row centre W/2 |
| 180° rotation requires an even row count | Same convention; ρ pairs r with H−1−r, which preserves row parity iff H is odd. The gate's own counterexample — 9×9, (1,1)→(6,7) not (7,7) — is this fact in one hex |
| *Longwater March* 13×8, *The Causeway* 9×8 | Forced by the line above; dimensions are per-scenario data, not a global constant (Q1, §4.7) |
| Lane ceiling 6 MP, Bridge-free | §2.4 Infantry Move 3 × 2 turns; §2.13.1's opening-capture invariant; §4.7 T-SCN-06, which derives the ceiling from the loaded table |
| Every entered hex counted, objective included | §4.7 T-SCN-06 ("Factory MoveCost 1, §2.3 — the same accounting as T-MOVE-01") |
| Path costs 1/1/1 Plains, Town, Factory; 3 for Mountain; 2 for Woods | §2.3 terrain table |
| Distinct objectives per seat | §4.7 T-SCN-07's distinctness clause; §2.13.1's "the seat's own neutral" |
| Both seats' lanes equal on a symmetric map | Isometry: ρ maps each West path hex to the East path hex of identical terrain, so cost is preserved hex for hex — shown explicitly in the path table above |
| Homes 10 hexes apart (*Longwater*) and 6 (*Causeway*), unchanged | §2.13.3's dial — "factory count × home separation"; keeping both fixed is what lets the 16–20 and 8–12 estimates stand through a redraw |
| 6 factories on *Longwater*, 4 on *Causeway*; 4 and 2 towns | Unchanged from the merged §2.13.5/§2.13.6; §2.7's "~4 factories total" and Q19's ruling-in-force that ~4 describes the shipped map |
| Bridges as the only Water crossing; column-4 bisection is a true lockout | §2.3 Bridge row; §2.13.6's lockout argument; Q16's reading that Recon is a land unit |
| Home factory hex left free in both deployments | §2.13.1 ("home factory hex starts empty… so the turn-1 build spawns on the factory itself", §2.7 spawn rule) |
| 5 units per side, same composition on every map | §2.13.1 standard force; Q15, §4.7 (pending Director approval, not silently adopted) |
| Neutral factories start neutral, so both objectives are capturable | §2.13.1 ("each side owns exactly one home factory at start; all others are neutral"); §4.7 T-SCN-07's `ownership` clause |
