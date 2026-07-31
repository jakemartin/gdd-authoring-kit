> # ✅ APPLIED ADDENDUM — DO NOT RE-APPLY
>
> Every replacement pair in this file **has been applied to the master GDD**, and
> the master has moved on since. Its Old blocks no longer match, so re-applying is
> a no-op at best; its quoted "current" text, register extents, and any hash it
> names are a **snapshot of the moment it was written**, not the current state.
>
> **The master GDD is the source of truth** — read `source/gdd.md`. Further changes
> to a merged section go in a *new* addendum file.

# Scenario & map design — post-merge-4 draft (scenario-designer)

## Placement

All four edits land **inside §2.13** and nowhere else.

| # | Target | Kind |
|---|---|---|
| 1 | §2.13.1, opening-capture invariant, numbered note **3** | replace |
| 2 | §2.13.2, *Ferrum Crossing* **Starting positions** table, Infantry row | replace |
| 3 | §2.13.2, immediately **after** the Starting positions table and **before** "Terrain as economics, hex by hex" | insert |
| 4 | §2.13.2, **Asymmetry and its handicap story** paragraph | replace |

No rule, unit, terrain, dimension, factory count, town count, turn cap or
match-length estimate changes. One starting placement moves. The 99-hex
terrain distribution is untouched because no terrain hex is touched.

---

## Draft

### The verdict first

**T-SCN-11 passes after one unit moves.** *Ferrum Crossing*'s East second
Infantry relocates from **(9,5)** to **(9,1)**. Both guided entries then
report **5 against 6**. Nothing else on the map moves, and I do **not**
recommend relocating the South factory — the reasoning is in edit 3 and the
rejected alternatives are in Open questions.

I did not conclude the map has to give something up that the Director must
weigh first. It gives up one thing, it is small, it is stated in the prose,
and it is the thing the map's own tactical claim already said East should
give up: East's second Infantry stops picketing the south.

### Measurement method (used for every number below)

Pathed, not reasoned. Odd-r `(col, row)` → axial `q = col − ⌊row/2⌋`, cube
distance as the lower bound, then a hand-run Dijkstra on the §2.13.2 glyph
grid with §2.3 move costs: **Plains 1 · Woods 2 · Mountains 3 · Town 1 ·
Bridge 1 · Factory 1 · Water impassable to land**. Cost counts **every hex
entered including the objective** (the T-MOVE-01 accounting T-SCN-06 and
T-SCN-11 both use). Occupancy excluded (**Q21**, ruled). Bridges permitted
on opposing routes, forbidden on the two guided lanes (**T-SCN-11 (ii)**,
**T-SCN-06**). Adjacency checked hex-by-hex against odd-r neighbour rules on
every route printed.

Where my figures overlap `tech-director`'s and the Director's, they agree:
West guided **5**, East guided-to-South **6**, East-(9,5)-to-South **5**
(the tie), East guided-to-North **5**, West cheapest-to-North **6** (the
Q22 register row's "*Ferrum Crossing*'s East lane 6 vs 5"). Three
pathfinders, one set of integers.

---

### Edit 1 — §2.13.1, numbered note 3

*Note: this is the "the first lesson is not a race" correction. The old
sentence was false twice over — it was never measured, and on the map as
drawn it was contradicted by a 5-MP tie. The replacement states the
guarantee as the inequality it actually is, and says plainly what a 1 MP
margin does and does not buy at Infantry Move 3.*

**OLD**

```
  3. **Uncontested, not merely reachable.** The designated lane is the seat's
     *own* neutral — West → South, East → North on the shipped map — so the
     first lesson is not a race. Player-first IGOUGO (§2.1) also means the
     player occupies the hex before the AI's second turn.
```

**NEW**

```
  3. **Uncontested, and exactly what that buys.** The designated lane is the
     seat's *own* neutral — West → South, East → North on the shipped map —
     and under Q22/Q28 that is a **measured inequality**, not an authorial
     claim: the opposing seat's cheapest Infantry route to the same
     objective, ranging over **every** Infantry that seat deploys, must cost
     **strictly more MP** than the owning seat's lane (T-SCN-11, §4.7).
     Measured on the set: *Ferrum Crossing* **5 against 6** in both seats,
     *The Causeway* **3 against 5**, *Longwater March* **4 against 8**.

     An earlier draft of this note said "the first lesson is not a race" and
     stopped there. That was wrong on both counts. It was unmeasured; and on
     the shipped map as first drawn, East's *second* Infantry at (9,5) tied
     West's South lane at 5 MP flat — a race under any reading, and the
     reason §2.13.2's deployment now reads (9,1). What is true, stated at
     the resolution the number supports:

     - **No opposing Infantry can arrive for fewer MP.** That is the whole
       of the inequality, it holds on all six lanes in the set, and it is
       the property the gate checks.
     - **On the shipped map it does not buy a turn.** 5 MP and 6 MP are
       *both* two turns at Infantry Move 3 (§2.4). A 1 MP margin is daylight
       in movement points, not in turns. What converts it into "you get
       there first" is **player-first IGOUGO** (§2.1): the player's seat
       moves before the AI inside every turn, so on the shared arrival turn
       the player stands on the factory hex first and an opposing Infantry
       walking the same lane finds the hex occupied and the capture pip
       already placed.
     - **Deployment carries the rest of the load, and is meant to.** After
       the correction neither East Infantry has a cheaper errand in the
       south: both sit 5 MP from East's *own* North objective and 6–7 MP
       from West's South one. The southern contest is not merely lost on
       distance, it is uneconomic — which is a stronger guarantee than the
       gate can express and a weaker one than the gate can enforce, so the
       gate keeps the inequality and this note keeps the reasoning.
     - **The stretch maps do buy a turn**, and that is the difference an
       honest note has to show. *The Causeway*'s 3-against-5 is a one-turn
       lane against a two-turn one; *Longwater March*'s 4-against-8 is two
       turns against three. The shipped map is the tightest in the set, on
       slack (1 MP, note 2) and on contest (1 MP) alike, and both facts have
       the same cause: it is the only map in the set that is not drawn to a
       symmetry.
```

---

### Edit 2 — §2.13.2, Starting positions table, Infantry row

*Note: the only placement change on the map. Guided hexes are bolded, which
also brings this table into line with §2.13.5's and §2.13.6's convention.*

**OLD**

```
| Infantry ×2 | (1,3), (1,5) | (9,3), (9,5) |
```

**NEW**

```
| Infantry ×2 | (1,3), **(1,5)** | **(9,3)**, (9,1) |
```

---

### Edit 3 — §2.13.2, insert after the Starting positions table

*Note: the anchor is the table's last row plus the paragraph that currently
follows it; both are reproduced verbatim in NEW so the insertion point is
unambiguous. This adds the guided-opening declaration *Ferrum Crossing* has
never carried in §2.13.2 (the other two maps both carry one), the eight
measured routes, and the justification for the relocation.*

**OLD**

```
| Recon | (0,5) | (10,3) |

**Terrain as economics, hex by hex.** The river spans rows 0–5 only, crossed
```

**NEW**

```
| Recon | (0,5) | (10,3) |

**Guided opening** (§2.13.1). `guidedOpening.infantry` = **(1,5)** West /
**(9,3)** East; `guidedOpening.objective` = **South (5,7)** West / **North
(6,2)** East. Distinct objectives (T-SCN-07); **5 MP each**, Bridge-free
(T-SCN-06); 1 MP of slack against the 6 MP ceiling, in both seats. This map
previously named its guided units only in §2.13.1's lane table; they are
declared here now, with the map they belong to.

**Non-contention, measured (T-SCN-11; Q22 ruled, Q28 ruled).** Q28 rules
that "the opposing seat's Infantry" means **every** Infantry that seat owns,
not only its marked guided unit — so this map is checked on **eight** routes,
not two. All eight, priced identically: Stub-3 cheapest path, terrain alone
with occupancy excluded (Q21), every hex entered counted including the
objective, Bridges permitted on opposing routes and forbidden on the two
guided lanes.

| Infantry | → North **(6,2)** | → South **(5,7)** |
|---|---|---|
| West (1,3) | **6** — (2,3)(3,2)(4,2)(4,1)(5,1)B(6,2) | **6** — (2,4)(3,4)(3,5)(4,5)(5,6)(5,7) |
| West **(1,5)** *guided* | 7 — (2,4)(2,3)(3,2)(3,1)T(4,1)(5,1)B(6,2) | **5** — (2,6)(3,6)(3,7)(4,7)(5,7) |
| East **(9,3)** *guided* | **5** — (8,3)(7,3)(6,3)w(6,2) | **6** — (9,4)F(8,5)(8,6)(7,7)(6,7)(5,7) |
| East (9,1) | 5 — (9,2)(8,2)(7,2)w(6,2) | **7** — (9,2)(8,3)(8,4)(7,5)(7,6)T(6,7)(5,7) |

**Both entries pass, and both report the same pair: 5 against 6.** West's
South lane costs 5; East's cheapest Infantry route to (5,7) costs 6, from
the guided hex (9,3). East's North lane costs 5; West's cheapest route to
(6,2) costs 6, from (1,3) over the north Bridge. Strictly longer in both
seats, which is the ruled comparison — equality fails, and equality is what
this map used to report.

Two structural facts the table makes visible. **Every route to North costs
exactly 1 MP more than its hex distance**, because the Water column forces
West onto a Bridge and the Woods ring — (6,1)(7,2)(6,3), the only land
approaches to (6,2) that are not the Bridge — forces East through cover.
**Every route to South is a plain geodesic at 1 MP per hex**, because rows
6–8 are open Plains that the two pass Mountains do not close. That is the
map's economy in two lines: the north is priced by terrain, the south is
priced by distance alone, and the south is therefore the half where
deployment is the *only* thing standing between two Infantry and the same
factory.

**Why East's second Infantry sits at (9,1) and not (9,5).** At (9,5) it was
5 MP from *West's* South objective — a dead tie with West's own lane, which
T-SCN-11 refuses, correctly: a tie is a race and a race is what the
invariant exists to prevent. It could not be nudged and stay southern.
Every **free** hex in East's southern quarter measures 4–5 MP to (5,7); the
only two hexes down there that clear 5 are (10,5) and (10,4) — the
Artillery's and the Flag Tank's — so staying southern means pushing a
fragile ranged unit or the flag itself onto the outer column for 1 MP of
margin. The cause is geometric and worth stating: East's south town (7,6)
is only 2 hexes from South (5,7), so by the triangle inequality anything
within 3 MP of that town is within 5 MP of that factory. A capturer that
covers East's southern town is *necessarily* a racer for West's southern
factory.

So the fix is a change of flank, not a shuffle — and it costs East nothing
in opening income. East's second Infantry was ever only the early capturer
for **one** town; at (9,1) it is adjacent to the north town **(8,1)** and
captures on turn 1 exactly as it did at (9,5) for (7,6). One town in the
opening either way; north instead of south. What East actually gives up is
the southern picket: town (7,6) now waits for a turn-1 Infantry build — 100
of the 200 starting Fame (§2.7), spawning on the deliberately empty home
factory (9,4), 3 MP and therefore one turn from (7,6) — and East's opening
south flank is Artillery (10,5) behind the Flag Tank (10,4). That is a
one-turn, 25-Fame-per-turn delay on one town, paid for out of starting Fame,
against a guided lane that stops being a race. It is also the deployment
finally agreeing with the sentence this section has always printed: *East's
prize is North.*

**Terrain as economics, hex by hex.** The river spans rows 0–5 only, crossed
```

---

### Edit 4 — §2.13.2, Asymmetry and its handicap story

*Note: the "each seat is closer to a different neutral factory" correction.
As drawn the sentence was false for East, which was equidistant at 5/5. The
relocation makes it true; the replacement states it as a measurement with
its margin rather than as an assertion, so the next map edit that breaks it
breaks a number instead of a mood.*

**OLD**

```
**Asymmetry and its handicap story.** Starting Fame and forces are
identical; the asymmetry is purely spatial and intended to be
self-balancing — each seat is closer to a different neutral factory, and
each seat's advantage (West: tempo and open approaches; East: cover and a
crossing-free path to its prize) is the other's problem.
```

**NEW**

```
**Asymmetry and its handicap story.** Starting Fame and forces are
identical; the asymmetry is purely spatial and intended to be
self-balancing. Each seat is closer to a *different* neutral factory —
measured, and by exactly **1 MP in each seat**: West's cheapest Infantry
route is **5 MP to South against 6 to North**, East's is **5 MP to North
against 6 to South** (all four figures in the eight-route table above).
Earlier drafts asserted that sentence without pricing it, and for East it
was simply false: with an Infantry at (9,5), East was **equidistant** — 5 MP
to South and 5 MP to North — so the seat the map called the northern one had
no measurable preference at all, and West's southern lane was a tie rather
than a lane. The deployment above is what makes the sentence true, and the
four numbers, not the sentence, are the claim. Each seat's advantage (West:
tempo and open approaches; East: cover and a crossing-free path to its
prize) is the other's problem. If §4.1 self-play shows either seat above
~55% win rate, the corrective is the existing §2.9 dial — a per-seat
starting-Fame offset — never a terrain rework. This is also the replay
lever: the two seats are two different deterministic puzzles (see 2.13.4).
```

*(Edit 4's NEW absorbs the two sentences that currently close the paragraph —
the §2.9 handicap sentence and the replay-lever sentence — unchanged, so the
paragraph is replaced whole rather than spliced. Nothing after "is the
other's problem." in the current text is altered in wording.)*

---

### Invariants re-checked after the change

| Guarantee | Source | Status |
|---|---|---|
| Guided lane ≤ 6 MP, both seats | T-SCN-06, §2.13.1 | 5 and 5 — unchanged |
| Guided lane Bridge-free, both seats | T-SCN-06 | West all Plains; East one Woods, no Bridge, no Water |
| Guided objectives distinct + neutral; named units are CanCapture, `isFlag` false | T-SCN-07 | (5,7) ≠ (6,2), both neutral; (1,5) and (9,3) unchanged |
| Non-contention, strictly longer, over every Infantry | T-SCN-11 (Q22, Q28) | **5 vs 6 both seats — PASSES** |
| All deployment hexes free and land-passable | §2.13.1 | (9,1) is Plains, in-bounds, previously unoccupied |
| Both home-factory hexes empty at start | §2.13.1 | (1,4) and (9,4) still empty; (9,1) ≠ (9,4) |
| 99-hex terrain distribution | §2.13.2 | Plains 75 · Woods 8 · Mountains 2 · Water 4 · Bridge 2 · Town 4 · Factory 4 — **no terrain hex touched** |
| 5 units per side, 4 factories, 4 towns, 11 × 9, cap 20 | §2.13.2, §2.13.7 | unchanged |
| `symmetry: none`, deliberate asymmetry | §2.13.4, Q24 | unchanged, and *increased*: the deployments are now further from mirror images, which a `none` declaration asserts nothing about and T-SCN-09 does not check |
| Contact turn 3–4, economy online turn 3–4, 12–16 turn estimate | §2.13.3 | unchanged — both near Infantry still reach their closest neutral in 2 turns |
| Connectivity: every land-passable hex reaches every factory | §2.13.1 | unchanged — no terrain moved |
| Flags mutually reachable | T-SCN-04 | unchanged — no terrain moved, and units do not block under Q21 |

---

## Change requests

Everything below is outside §2.13 and therefore outside my lane. Each becomes
false or stale the moment edit 2 lands.

| Existing § | Current text | Proposed change | Why |
|---|---|---|---|
| §4.7, Stub 7, **T-SCN-11 asymmetry (iii)** | "Measured on all three §2.13 maps as drawn, (b) passes all six lanes and (a) **FAILS one** — on Ferrum Crossing, East's SECOND Infantry at (9,5) reaches West's South objective (5,7) in 5 MP … exactly TYING West's 5 MP lane from (1,5)" | Rewrite to the post-fix state: under the ruled reading (a), **all six lanes pass**; *Ferrum Crossing* reports 5 against 6 in both seats. Keep the (9,5) tie as the recorded *reason the reading was ruled*, in past tense, and drop "written and blocked". | `tech-director`'s. The measurement was right and the refusal to redraw was right; the map has now moved, so the fixture prose must follow it. Preserving the tie as history is what keeps the ruling legible. |
| §4.7, Stub 7, **Acceptance** line | "T-SCN-01..09 and T-SCN-11 headless (10 reserved-unwritten on Q26; **11 blocked on Q28**)" | Drop the block on 11 once the Director routes Q28's ruling. | `tech-director`'s and the Director's. Q28 is ruled per this task's brief; T-SCN-11 has a passing fixture on all three maps. Not my edit — reporting the numbers is. |
| §4.11, ledger row 7 note | "**T-SCN-11** … Its *dependency* is settled even though its *assertion* is not: the invariant is written and blocked on **Q28**, which … under its stricter reading, **refuses *Ferrum Crossing* as drawn**" | Same: the stricter reading no longer refuses the shipped map. The two-lookups-per-entry path budget is unaffected and should stay. | `tech-director`'s. Only the blocked-status clause is stale; the cost analysis it sits inside is still correct. |
| §4.11, ledger row 7 gate list | "T-SCN-01..09, 11 (10 reserved-unwritten on Q26; **11 blocked on Q28**)" | Same as the Acceptance line. | Director's, at ruling time. |
| §4.7 open-questions register, **Q22** rationale | "The sixth does not. On *Ferrum Crossing*, East's **second** Infantry at **(9,5)** … **exactly tying** West's 5 MP lane … T-SCN-11 is written and blocked on it." | Append the resolution rather than rewrite the history: the sixth lane now clears at 5 vs 6 after (9,5) → (9,1), so all six clear. | Director's register. Q22's ruling is unchanged and was correct; only its "the sixth does not" needs a closing line. |
| §4.7 open-questions register, **Q28** | The whole row, including "(a) refuses *Ferrum Crossing* until either East's second Infantry at (9,5) moves or West's guided objective does, and **both are `scenario-designer`'s call**" | Mark **RULED (a)**, and record the outcome: the second Infantry moved, not the objective; the map passes under (a); no rules change was needed. | Director's register. The row correctly predicted the two available fixes and correctly routed the choice to me. This is the record of which one was taken. |
| §4.7 open-questions register, **Q21** rationale | "**Scope narrowed by the §2.13 symmetry correction:** both stretch lanes are now clear of their own seat's starting units … so an 'as deployed' ruling could only move *Ferrum Crossing*'s numbers" | Verify or retire. I measured both *Ferrum Crossing* guided lanes against the post-fix deployment and **neither passes through any of that seat's own units** — West's (2,6)(3,6)(3,7)(4,7)(5,7) and East's (8,3)(7,3)(6,3)(6,2) are all empty at start. If that was already true pre-fix, the sentence was stale before I touched anything. | `tech-director`'s / Director's. Q21 is **ruled** (terrain alone), so this is cosmetic — but it is a live sentence asserting a false-looking thing about my map, and I would rather flag it than quietly leave it. Not urgent, not blocking. |

---

## Open questions for the Director

**No new Q number filed.** The fix needs no ruling: it is a placement change
inside §2.13, using only ruled inputs (Q4 N = 1 assumed-in-force, Q21 ruled,
Q22 ruled, Q28 ruled as reading (a)). The register stays at **Q1–Q28**.

Three things I decided rather than escalated, each recorded with the option
I declined, in case the Director wants a different trade:

1. **Margin: 1 MP, not 2.** The ruled comparison is "strictly longer", and
   1 MP satisfies it — the same margin the North lane has always carried and
   which the Director has already accepted there. But 5 MP and 6 MP are both
   two turns at Move 3, so 1 MP does not separate the arrivals by a turn;
   player-first IGOUGO does. **A two-turn separation is available** and costs
   two more placement moves: put East's *guided* Infantry at (9,1) and its
   second at (10,2) (both 5 MP to North, both **7** MP to South), and West's
   second Infantry at (1,6) (7 MP to North, 2 MP to the south town (2,7)).
   Both lanes then read **5 against 7** — two turns against three, real
   daylight. The price is that each seat's *entire* capture pair commits to
   one flank and each seat's far town slips a turn. I did not take it because
   it is four placement moves to over-satisfy a rule that one move satisfies,
   and because concentration that total makes the opening less interesting,
   not more. Say the word and I will draft it as edits 2′/3′.
2. **I did not move the South factory.** (4,7) works arithmetically — West 4
   MP, East 6 — but it drags the prize out from behind the pass mouth onto
   West's own side of the Mountains, weakens the "which neutral do you race"
   question that is the map's stated tactical premise, and shortens West's
   guided lane to 4 MP, which changes §2.11.6-B's two-turn walk into a
   one-and-a-bit. Moving a unit is cheaper than moving an objective, and this
   failure was caused by a unit.
3. **Unowned, flagged not fixed:** the Q21 rationale sentence in the register
   (last row of Change requests). It appears to have been stale before this
   task and is cosmetic now that Q21 is ruled. I have not touched it.

---

## Handoffs

- **`tech-director`** — three §4.7/§4.11 change requests above (T-SCN-11
  fixture (iii), the Acceptance line, the ledger row 7 note). The eight
  measured integers in edit 3 are yours to use as T-SCN-08's expected
  fixture values for this map; the two T-SCN-11 comparisons are **5 vs 6**
  and **5 vs 6**. Path budget is unchanged at two lookups per
  `guidedOpening` entry. Also: `guidedOpening` is now declared in §2.13.2
  itself for *Ferrum Crossing*, so Stub 7's fields have an antecedent on all
  three maps rather than two.
- **Director** — Q28 ruling record, Q22 closing line, and the T-SCN-11
  unblock, per your note that you would route it.
- **`ux-onboarding-designer`** — no change to §2.11.6-B. The guided lane is
  still 5 MP over two turns with 1 MP of slack, the pip still appears turn 3
  at N = 1, and the marked Infantry hexes are still (1,5) West / (9,3) East.
  One thing worth knowing: the guarantee that the player reaches the factory
  first now rests partly on player-first IGOUGO, not on distance alone —
  if guidance ever narrates "you'll get there first", that is why.
- **`rules-designer`** — nothing. No rule, cost, or comparison changed; the
  6 MP ceiling still derives from §2.4 Infantry Move 3, and capture N = 1
  remains an assumption in force under Q4, asserted nowhere in this draft.

---

## Grounding

| Decision | Traced to |
|---|---|
| Move cost model used for every route (Plains/Town/Bridge/Factory 1, Woods 2, Mountains 3, Water impassable to land) | §2.3 terrain table |
| 6 MP guided ceiling; 5 MP and 6 MP both being two turns | §2.4 Infantry **Move 3**; §2.13.1's "2 × Infantry Move" derivation |
| Cost counts every hex entered including the objective; occupancy excluded | T-SCN-06 accounting; **Q21 ruled** (terrain alone) |
| Bridges forbidden on guided lanes, permitted on opposing routes | T-SCN-06 Bridge-free clause; T-SCN-11 asymmetry (ii) |
| "Strictly longer", equality fails | **Q22 ruled**; T-SCN-11 "EQUALITY FAILS" |
| Opposing route ranges over every Infantry the seat owns | **Q28 ruled**, reading (a) |
| Why (9,5) had to move at all | Its 5 MP tie with West's 5 MP lane — measured three times: `tech-director`, the Director's independent pathfinder, and this draft |
| Why no southern hex works | Town (7,6) is axial distance **2** from factory (5,7); every free hex in East's southern quarter prices 4–5 MP to (5,7); only (10,5) and (10,4) clear 5, and both are occupied by the Artillery and the Flag Tank respectively |
| Why (9,1) specifically | 7 MP to (5,7) — the largest margin available; 5 MP to North, so it does not undercut the named guided lane; **adjacent to the north town (8,1)**, so East's one-town opening survives intact |
| The south town's replacement capturer costs one turn | §2.7 build-and-spawn on the home factory; (9,4) → (7,6) is 3 MP = one turn at Move 3; Infantry 100 Fame against 200 starting Fame (§2.4, §2.7, §2.13.1) |
| Home factory hex left empty so the build spawns there | §2.13.1 |
| Terrain distribution preserved | No terrain hex edited; §2.13.2's 99-hex line stands unchanged |
| Asymmetry preserved and deliberate | §2.13.4; `symmetry: none` under **Q24**; T-SCN-09 asserts nothing for `none` |
| North lane pricing (+1 MP over hex distance in all four routes) | Water at (5,2)(5,3) forces West to the Bridge (5,1); (6,2)'s only non-Bridge land neighbours (6,1)(7,2)(6,3) are all Woods, §2.13.2 key coordinates |
| South lane pricing (geodesic, 1 MP per hex) | Rows 6–8 are Plains except the two pass Mountains (4,6)(6,6) and town (2,7); the river stops at row 5, §2.13.2 |
| Match-length estimate untouched | §2.13.3 — both near Infantry still reach their nearest neutral in 2 turns; no factory, town or home-separation change |
| Stretch-map comparison figures (Causeway 3 vs 5, Longwater 4 vs 8) | §4.7 T-SCN-11 (ii); Q22 register row |
