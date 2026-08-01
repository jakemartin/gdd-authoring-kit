> # ✅ APPLIED ADDENDUM — DO NOT RE-APPLY
>
> Every replacement pair in this file **has been applied to the master GDD**, and
> the master has moved on since. Its Old blocks no longer match, so re-applying is
> a no-op at best; its quoted "current" text, register extents, and any hash it
> names are a **snapshot of the moment it was written**, not the current state.
>
> **The master GDD is the source of truth** — read `source/gdd.md`. Further changes
> to a merged section go in a *new* addendum file.

# Technical design — post-merge-12 draft (tech-director)

## Placement

Five pairs, all in **§4.7**: three inside the **Stub 7** fenced block (T-SCN-11's
`PRINT CONVENTION`, T-SCN-11 asymmetry (ii)'s *Ferrum Crossing* bullet,
T-SCN-11 asymmetry (ii)'s `WHY THIS IS STATED AS A REASON` paragraph), two in
the **open-questions register** (its preamble, and one new row **Q30**).

No other section is touched. No map hex, no lane number in the asserted
(Bridge-allowed) reading, no terrain figure, no week number and no `T-` ID
moves. T-SCN-10 stays reserved and unwritten. The register goes **Q1–Q29 →
Q1–Q30**, still **ten ruled** (Q7, Q20, Q21, Q22, Q23, Q24, Q25, Q26, Q27,
Q28); Q30 ships unruled with a conservative reading in force. Nothing in
`sections/` is edited; this file is the whole delta.

## Draft

### The question, answered

**Does a bare "X against Y" assert a minimum over the seat's whole Infantry
set, or is it scoped to the named hex?**

**It asserts a set minimum.** The convention says a bare pair is
`OWNING against OPPOSING (this invariant)`, and *this invariant* defines its
opposing term nine lines above the convention:

```
    min over the opposing seat's Infantry of cost(hex, objective)
      >  the owning lane's cost
```

with Q28 fixing the range as every CanCapture-row unit the seat deploys. The
right-hand term of a bare pair is that quantity. There is no other quantity it
could be — a bare pair has exactly two slots, the left one is the owning lane,
and the right one is the thing the owning lane is compared against, which is the
set minimum by definition.

So the gate read it correctly and I did not. **"5 against 14" is wrong.** The
figure is **13**, and the margin is **8 MP**, not 9.

The scoping argument I made in `post-merge-11` was not a defence of the number.
It was a defence of a *different* number — 14 is a true statement about (1,3) —
smuggled into a slot that means something else. That is precisely the defect the
last four rounds have been about, at one more level of resolution: a figure
measured on one object, printed in a form that quantifies over the set.

### The measurement

The Director's route is adjacency-valid, Bridge-free and costs 13. I reproduce
it and then prove it minimal, because a counterfactual that is corrected once
and wrong again is worse than one left alone.

**Route** (using §2.13.2's own guided South lane as its first five hexes):

| Step | Hex | Terrain | Cost |
|---|---|---|---|
| 1 | (2,6) | Plains | 1 |
| 2 | (3,6) | Plains | 1 |
| 3 | (3,7) | Plains | 1 |
| 4 | (4,7) | Plains | 1 |
| 5 | (5,7) | **Factory** (South objective) | 1 |
| 6 | (6,7) | Plains | 1 |
| 7 | (7,6) | **Town** | 1 |
| 8 | (6,5) | Plains | 1 |
| 9 | (6,4) | Woods | 2 |
| 10 | (6,3) | Woods | 2 |
| 11 | (6,2) | Factory (North objective) | 1 |
| | | | **13** |

Adjacency checks under odd-r offset (odd rows shifted right, as §2.13.2 draws
them): (1,5)→(2,6) is a down-right from an odd row; (3,6)→(3,7) and
(5,6)→(5,7) are down-rights from even rows; (6,7)→(7,6) is an up-right from an
odd row; (7,6)→(6,5) is an up-left from an even row; (6,5)→(6,4), (6,4)→(6,3),
(6,3)→(6,2) are the same up-left/up-right pattern that §2.13.2's own East
(9,3)→North route uses at (6,3)→(6,2). No hex on it is a Bridge: the two
Bridges are (5,1) and (5,4), and the route touches column 5 once, at (5,7).

**Minimality.** Bridge-free, column 5 is impassable at rows 0–5 — Water
(5,0)(5,2)(5,3)(5,5), Bridges (5,1)(5,4) excluded — so *every* Bridge-free path
from the west bank to (6,2) crosses column 5 at (5,6), (5,7) or (5,8). One
reverse Dijkstra from (6,2) prices the three tails; axial distance prices the
three approaches:

| Crossing | Tail to (6,2) | From (1,5) | Total | From (1,3) | Total |
|---|---|---|---|---|---|
| (5,6) | 9 | 5 | 14 | 5 | **14** |
| **(5,7)** | **8** | **5** | **13** | 6 | **14** |
| (5,8) | 9 | 5 | 14 | 6 | 15 |

So d(1,5) = **13**, d(1,3) = **14**, and the set minimum over West's Infantry is
**13**. Both approach legs are axial geodesics on Plains, so neither can be
beaten; the (5,7) tail of 8 is the Dijkstra value, and the 9s are the mountain
route `(6,6)m(6,5)(6,4)w(6,3)w(6,2)` and its equal-cost southern twin.

**Three things this measurement says that the number alone does not.**

1. **Excluding the Bridges moves the minimising unit.** With them permitted,
   West's cheapest to North is (1,3) at 6, against (1,5) at 7 (§2.13.2's route
   table). Without them it is (1,5) at 13, against (1,3) at 14. A figure taken
   from the *shipped* minimiser is therefore not the counterfactual minimum —
   which is exactly why a hex-scoped figure printed bare goes wrong here and
   would have been harmless on a map where the minimiser did not move.
2. **The Mountain is not the cause,** so the Director's route is right but its
   stated reason is not quite. (1,3) has a mountain-free 14 as well —
   `(2,4)(3,4)(4,4)(4,5)(5,6)(5,7)F(6,7)(7,6)T(6,5)(6,4)w(6,3)w(6,2)` — so
   avoiding (6,6) saves (1,3) nothing. The whole 1 MP is the approach: (1,5)
   reaches (5,7) in 5 and (1,3) in 6, and the tail is 8 for both. I have written
   the cause into the GDD text as the approach, not the Mountain.
3. **Bridge-free, West's road to the northern objective runs through West's own
   southern objective.** That is a real property of *Ferrum Crossing* and worth
   one clause in the bullet.

### Does the 13-vs-14 discrepancy change my view on filing? Yes.

My `post-merge-11` reasoning was: no invariant computes the counterfactual, so a
future deployment edit could invalidate it and nothing would notice — therefore
it is unguarded, not gapped, and the register carries gaps and not observations.

That reasoning answers *"is this figure guarded?"* It does not answer *"is this
figure true?"* — and I let the first question stand in for the second. A printed
integer is a claim the moment it is printed, whether or not a gate recomputes
it; §3's standard is that the document does not assert what it has not measured,
and this one asserted a set minimum nobody had measured. The correct test for
filing was never "would a gate catch a later drift," it was "does the document
assert something it has not measured." It did, and I should have said so.

**But the rule gap is not the one the Director framed, and that is why it is
still worth an ID.** "Does the convention quantify?" is *derivable* — the answer
is yes, from the formula plus Q28, and I have just derived it. Filing that alone
would register a deduction, not a gap. The real gap is one level over: **the
convention names two relations and provides two printed forms, and there are
three quantities.** T-SCN-06's budget got a distinguishing form ("7 against the
6 MP ceiling"); the opposing route got the bare form; a cost measured *from a
named hex* got nothing. So a hex-scoped figure has nowhere to go except the bare
form, which means something else — and that is mechanically how "5 against 14"
got written. A convention with a quantity it cannot print is a rule gap, and
which way it closes (a third printed form, or a prohibition) is the Director's
call, not mine. **That is Q30.**

I file it, and I write the conservative reading into the convention now, because
it is free: it costs words and never a map, a gate, an integer or a fixture.

### The sweep this finding forces

Every "against" print in the document, checked at set-quantifier resolution —
because if one hex-scoped figure reached a bare slot, others might have.

| Site | Right-hand term | Set minimum? | Verdict |
|---|---|---|---|
| §2.13.2 "both report the same pair: 5 against 6" | North: West's min over {(1,3)=6, (1,5)=7}. South: East's min over {(9,3)=6, (9,1)=7} | 6 and 6 | **Holds** |
| Stub 7 asymmetry (iii) "passes in both seats at 5 against 6" | Same two minima | Yes | **Holds** |
| Stub 7 fixture (a) "5 against 6 each way", naming (1,3) and (9,3) | Names the minimising hex *and* the minimum; they coincide | Yes | **Holds** — naming the hex is safe when it *is* the minimiser |
| Stub 7 fixture (b) "5 against 5" from (9,5) | Pre-fix East min over {(9,3)=6, (9,5)=5} | 5 | **Holds** |
| Stub 7 fixture (b) "under the Q28 reading REFUSED, (b) passes at 5 against 6" | Explicitly the narrow reading, and says so | n/a — labelled | **Holds** |
| Stub 7 fixture (c) *Causeway* "3 against 5 in both seats" | §2.13.6's opposing minima | Not re-derived here | **Out of scope** — no Bridge-free counterfactual is printed for it |
| T-SCN-08 fixture (c) "7 against the 6 MP ceiling" | A budget, in the ceiling form | n/a | **Holds** |
| Stub 7 (ii) `WHY` "5 against 14" | Claimed set minimum; is (1,3)-scoped | **No — 13** | **False → Pairs 1, 2** |

One defect, and it is the one under discussion. Fixture (a)'s habit of naming
the minimising hex beside the minimum is the *right* pattern and is what Pair 1
generalises: name the hex, and say whether it is the minimiser.

---

### The pairs

**Pair 1 — Stub 7, T-SCN-11 asymmetry (ii), the *Ferrum Crossing* bullet.
REQUIRED (the correction).** The bullet keeps the (1,3) figure of 14 — it is
true and it is the shipped minimiser's Bridge-free cost, which is the fact the
bullet was reaching for — but labels it **from (1,3) alone, not a set minimum**,
and prints beside it the figure the invariant actually compares: 13, from (1,5),
with its route and its decomposition. **New numbers, all measured above and all
in play per the brief:** 13, its route, the 5 + 8 split, and the observation
that the minimiser moves. Everything else is verbatim — 6, 14, the 14 MP route
string, `(9,4)F(8,5)(8,6)(7,7)(6,7)(5,7)`, (5,5), "rows 0–5", and the whole
southern half.

**OLD**

```
                    - Ferrum Crossing (§2.13.2) EXERCISES it, but on ONE
                      of fixture (a)'s TWO opposing routes, not both.
                      West's cheapest route to North (6,2) — 6 MP from
                      (1,3) — runs over the north Bridge (5,1).
                      Bridge-free, the cheapest route from that hex to
                      that objective costs 14 MP:
                      (2,3)(3,4)(3,5)(4,5)(5,6)(6,6)m(6,5)(6,4)w(6,3)w
                      (6,2) — around the river's southern end, then up
                      through the Woods ring. More than double. The
                      OTHER opposing route in that fixture is already
                      Bridge-free and does not move: East's cheapest
                      route to South (5,7), 6 MP from (9,3), is
                      (9,4)F(8,5)(8,6)(7,7)(6,7)(5,7), which reaches
                      column 5 only at the objective itself, on row 7,
                      below the river's southern end at (5,5) — the
                      river spans rows 0–5 only. Excluding an edge can
                      only RAISE a shortest path, and that 6 MP witness
                      uses no excluded edge, so 6 stands under either
                      reading. The allowance binds ONE of this map's two
                      objectives, the northern one.
```

**NEW**

```
                    - Ferrum Crossing (§2.13.2) EXERCISES it, but on ONE
                      of fixture (a)'s TWO opposing routes, not both.
                      West's cheapest route to North (6,2) — 6 MP from
                      (1,3) — runs over the north Bridge (5,1). TWO
                      Bridge-free figures follow and they are DIFFERENT
                      QUANTITIES, so each is labelled where it stands.
                      FROM (1,3) ALONE, not a set minimum: 14 MP,
                      (2,3)(3,4)(3,5)(4,5)(5,6)(6,6)m(6,5)(6,4)w(6,3)w
                      (6,2) — around the river's southern end, then up
                      through the Woods ring. More than double that
                      hex's own 6.
                      MINIMISED OVER WEST'S INFANTRY — this invariant's
                      opposing term (Q28), and the only figure a BARE
                      pair may carry: 13 MP, from the OTHER West
                      Infantry (1,5),
                      (2,6)(3,6)(3,7)(4,7)(5,7)F(6,7)(7,6)T(6,5)
                      (6,4)w(6,3)w(6,2). Its first five hexes are West's
                      own guided South lane (§2.13.2): 5 MP to (5,7),
                      then 8 MP up the east bank. Bridge-free, West's
                      road to the NORTHERN objective runs through West's
                      own SOUTHERN one.
                      EXCLUDING THE BRIDGES MOVES THE MINIMISER, which
                      is the whole reason the two figures differ: with
                      Bridges permitted West's cheapest is (1,3) at 6
                      against (1,5) at 7 (§2.13.2); without them it is
                      (1,5) at 13 against (1,3) at 14. The 1 MP is the
                      APPROACH, not the Mountain — (1,5) reaches (5,7)
                      in 5 and (1,3) in 6, while the tail from (5,7)
                      costs 8 for both, and (1,3) has a Mountain-free 14
                      as well. So a figure measured from the SHIPPED
                      minimiser is NOT the counterfactual minimum, and
                      that is the trap this bullet exists to name.
                      The OTHER opposing route in that fixture is
                      already Bridge-free and does not move: East's
                      cheapest route to South (5,7), 6 MP from (9,3), is
                      (9,4)F(8,5)(8,6)(7,7)(6,7)(5,7), which reaches
                      column 5 only at the objective itself, on row 7,
                      below the river's southern end at (5,5) — the
                      river spans rows 0–5 only. Excluding an edge can
                      only RAISE a shortest path, and that 6 MP witness
                      uses no excluded edge, so 6 stands under either
                      reading. The allowance binds ONE of this map's two
                      objectives, the northern one.
```

---

**Pair 2 — Stub 7, T-SCN-11 asymmetry (ii), the `WHY THIS IS STATED AS A REASON`
paragraph. REQUIRED (the wrong figure).** The bare pair takes the set minimum,
so 14 → 13 and the margin 9 MP → 8 MP; one clause says which quantity the
right-hand term is, so the pair cannot be misread back. The argument is
unchanged and unweakened: both seats still pass the counterfactual, no gate
still catches it, and the widening is still single-digit and still unremarked.
**No number is new to this file** — 13 and 8 are Pair 1's measurement and its
subtraction 13 − 5.

**OLD**

```
                    WHY THIS IS STATED AS A REASON AND NOT A PERMISSION:
                    a Bridge-free reading does not FAIL Ferrum Crossing
                    in EITHER seat, so no gate in this suite catches it.
                    North still passes, at 5 against 14 — strictly more
                    than the owning lane, on a number that describes a
                    walk around the entire river. South still passes at
                    5 against 6, exactly as drawn, because its opposing
                    route never crossed a Bridge. What the counterfactual
                    changes is ONE margin of the two: North's opposing
                    figure goes from 6 to 14 against an unchanged owning
                    5, widening that margin from 1 MP to 9 MP — a
                    single-digit widening, and an unremarked one, because
                    this invariant asserts a strict inequality and NO
                    CEILING (asymmetry (i)). South's margin stays at 1 MP
                    and never depended on the allowance at all.
```

**NEW**

```
                    WHY THIS IS STATED AS A REASON AND NOT A PERMISSION:
                    a Bridge-free reading does not FAIL Ferrum Crossing
                    in EITHER seat, so no gate in this suite catches it.
                    North still passes, at 5 against 13 — a BARE pair,
                    so its right-hand term is the SET minimum over West's
                    Infantry, the (1,5) route above, and NOT the 14
                    measured from (1,3) alone. Strictly more than the
                    owning lane on either figure, and either way a number
                    that describes a walk around the entire river. South
                    still passes at 5 against 6, exactly as drawn,
                    because its opposing route never crossed a Bridge.
                    What the counterfactual changes is ONE margin of the
                    two: North's opposing figure goes from 6 to 13
                    against an unchanged owning 5, widening that margin
                    from 1 MP to 8 MP — a single-digit widening, and an
                    unremarked one, because this invariant asserts a
                    strict inequality and NO CEILING (asymmetry (i)).
                    South's margin stays at 1 MP and never depended on
                    the allowance at all.
```

---

**Pair 3 — Stub 7, T-SCN-11's `PRINT CONVENTION`. REQUIRED (the scoping, at the
site that governs every other site).** Pairs 1 and 2 fix one passage; this fixes
the reason the passage was writable. The convention gains the quantifier it
always implied and a rule for the quantity it had no form for, and names Q30 as
the open half. **No relation, order rule or existing form changes** — the two
bullets are verbatim; this is an addition after them.

**OLD**

```
              - MEASURED against BUDGET (T-SCN-06's ceiling, reported by
                T-SCN-08 fixture (c)). The right-hand term is written as
                the CEILING it is — "7 against the 6 MP ceiling" — never
                as a bare integer. A bare pair is therefore always the
                first relation.
```

**NEW**

```
              - MEASURED against BUDGET (T-SCN-06's ceiling, reported by
                T-SCN-08 fixture (c)). The right-hand term is written as
                the CEILING it is — "7 against the 6 MP ceiling" — never
                as a bare integer. A bare pair is therefore always the
                first relation.
            WHAT A BARE PAIR QUANTIFIES OVER, stated because it was only
            DERIVABLE and was read the other way by a careful reader: the
            right-hand term of a bare pair IS this invariant's opposing
            term, so it is the MINIMUM over every CanCapture-row unit the
            opposing seat deploys (Q28). It is a SET figure. It is never
            a cost measured from one named hex.
            A HEX-SCOPED COST IS A THIRD QUANTITY WITH NO BARE FORM.
            Print it with its hex and the words "from (c,r) alone, not
            the set minimum," or do not print it in an "against" at all.
            Naming the hex beside a bare pair is safe ONLY when that hex
            IS the minimiser, which is what fixture (a) does. The danger
            is concrete, not stylistic: the minimising unit can CHANGE
            under a counterfactual, so a figure taken from the shipped
            minimiser stops being the minimum — asymmetry (ii)'s Ferrum
            Crossing bullet is exactly that case, where excluding the
            Bridges moves West's minimiser from (1,3) to (1,5) and the
            figure from 14 to 13.
            WHETHER THE THIRD FORM IS A PRINTED FORM OR A PROHIBITION IS
            Q30, unruled. The reading in force is the one written here,
            and it binds prose only: no invariant, fixture, reported
            integer or refusal condition depends on it.
```

---

**Pair 4 — register preamble, the enumeration. REQUIRED (companion to Pair 5).**
The preamble lists every ID range and its origin; Q30 joins it. **Substring
replacement**, unique in the master (`scoping the week-2 parity gate to its
command set (Q29)` occurs once).

**OLD**

```
scoping the week-2 parity gate to its command set (Q29)
— so that each question
```

**NEW**

```
scoping the week-2 parity gate to its command set (Q29), and the quantifier the
T-SCN-11 print convention never stated at a print site, found when a hex-scoped
figure was read as a set minimum (Q30)
— so that each question
```

---

**Pair 5 — register, new row Q30. REQUIRED (the filed gap).** Appended after
Q29, before the `### 4.8` heading. The OLD block is the tail of Q29's answer
cell plus the blank line and the heading, which anchors the insertion point
unambiguously; Q29's cell is not otherwise touched. Q30 ships **unruled with a
conservative reading in force**, which the register's own convention permits
here because the conservative reading is *free* — it costs words and never a
map, a gate, an integer or a fixture, so a later ruling can only relax the
labelling. That is the ordinary case, not the Q28 case where the conservative
reading refused a shipped map.

**OLD**

```
that is a §3 presentation decision, not a technical one, which is why it is registered rather than assumed. |

### 4.8 Data contract — DataTable schemas
```

**NEW**

```
that is a §3 presentation decision, not a technical one, which is why it is registered rather than assumed. |
| **Q30** | What a T-SCN-11 "against" print quantifies over, and what form a hex-scoped route cost takes. The print convention (§4.7 Stub 7) names two relations and gives two printed forms — a bare pair for owning-against-opposing, a named ceiling for measured-against-budget — but there are **three** quantities in play, and the third has no form. The bare pair's right-hand term is this invariant's opposing term and is therefore the **minimum over every CanCapture-row unit the opposing seat deploys** (Q28); that is derivable from the formula, was never stated at a print site, and was read the other way by a reader looking specifically for it. A cost measured **from one named hex** is neither of the two printed relations, so it has nowhere to go but the bare form, which means something else. That is mechanically how asymmetry (ii)'s Bridge-free counterfactual came to print "5 against 14": 14 is West's Bridge-free cost from **(1,3) alone**, while the set minimum is **13**, from **(1,5)** — `(2,6)(3,6)(3,7)(4,7)(5,7)F(6,7)(7,6)T(6,5)(6,4)w(6,3)w(6,2)`, West's own guided South lane plus 8 MP up the east bank. The two differ because **excluding the Bridges moves the minimising unit**: with them permitted West's cheapest is (1,3) at 6 against (1,5) at 7, without them it is (1,5) at 13 against (1,3) at 14. Should the convention gain a **third printed form** for a hex-scoped cost ("14 from (1,3) alone, not the set minimum"), or should a hex-scoped cost be **forbidden** inside an "against" print entirely? | **Nothing computable.** T-SCN-11's inputs, formula, unit set, reported integers, refusal conditions and all three fixtures are identical either way, and no map, lane cost or deployment moves. It governs only what §4.7's **prose** may claim from a measured integer — which is where the error was, and is the one place this suite has no gate. | **Conservative reading in force, and written into the convention this revision:** a bare pair is **set-quantified**, and a hex-scoped cost is printed only with its hex and the words "from (c,r) alone, not the set minimum." Naming the hex beside a bare pair stays legal when that hex **is** the minimiser, which is what fixture (a) does. Free in the conservative direction — it costs words, never a map, a gate, an integer or a fixture, so a later ruling can only relax the labelling and nothing passing today would start failing. The counterfactual figures are corrected to this reading here: **5 against 13**, margin **8 MP**, with **14 retained** as the explicitly (1,3)-scoped figure it always was. The alternative worth weighing, since it is the stricter one: forbid the third quantity outright, which would delete the 14 rather than label it — cheaper to police, but it discards the one figure that shows the shipped minimiser's own Bridge-free cost, and that figure is why the bullet was written. |

### 4.8 Data contract — DataTable schemas
```

---

### Re-read of the new text, not only the replaced text

Every assertable claim in the five NEW blocks, checked against `source/gdd.md`
and against my own arithmetic rather than against the draft it came from.

| New text | Check | Source |
|---|---|---|
| 13 MP route is adjacency-valid | Odd-r offset neighbours, step by step: down-right ×1 from an odd row, ×2 from even rows, up-right, then up-left ×4. Same neighbour pattern §2.13.2's East (9,3)→North route uses at (6,3)→(6,2) | §2.13.2 layout block |
| 13 MP route terrain and cost | (2,6)p1 (3,6)p1 (3,7)p1 (4,7)p1 (5,7)F1 (6,7)p1 (7,6)T1 (6,5)p1 (6,4)w2 (6,3)w2 (6,2)F1 = **13** | §2.13.2 layout rows r2–r7; §2.3 costs |
| It is Bridge-free | Bridges are (5,1) and (5,4); the route touches column 5 once, at (5,7) | §2.13.2 key coordinates |
| 13 is the **set** minimum | Bridge-free, column 5 is sealed rows 0–5 (Water (5,0)(5,2)(5,3)(5,5) + excluded Bridges), so all paths cross at (5,6)/(5,7)/(5,8); tails 9/8/9 by reverse Dijkstra from (6,2); (1,5) approaches all three in 5 (axial geodesics on Plains) → min 13. West's Infantry set is {(1,3), (1,5)} | §2.13.2 key coordinates + starting positions; T-MOVE-01 accounting |
| 14 is d(1,3), unchanged | (1,3) approaches at 5/6/6 → min(5+9, 6+8, 6+9) = 14. Matches the document's existing route | Current §4.7 text; measurement above |
| (1,3) has a Mountain-free 14 | `(2,4)(3,4)(4,4)(4,5)(5,6)(5,7)F(6,7)(7,6)T(6,5)(6,4)w(6,3)w(6,2)` = 14, no (6,6) | Measurement above |
| The 1 MP is the approach, not the Mountain | Tail from (5,7) is 8 for both units; approaches are 5 and 6 | Table above |
| Bridges permitted: (1,3)=6, (1,5)=7 | §2.13.2's eight-route table, West rows → North column | §2.13.2 |
| The minimiser moves (1,3) → (1,5) | 6 < 7 permitted; 13 < 14 excluded | Both of the above |
| First five hexes are West's guided South lane | §2.13.2: West **(1,5)** *guided* → South = `5 — (2,6)(3,6)(3,7)(4,7)(5,7)` | §2.13.2 route table |
| "5 MP to (5,7), then 8 MP up the east bank" | 5 + 8 = 13 | Above |
| "5 against 13" is owning-first and bare | Owning = East's North lane = 5 (fixture (a)); opposing = the set minimum 13 | Print convention; fixture (a) |
| Margin 1 MP → 8 MP | 6 − 5 = 1; 13 − 5 = 8. Single-digit | Above |
| "does not FAIL in EITHER seat" still holds | North 13 > 5; South 6 > 5. T-SCN-11 asserts strict inequality only, NO CEILING | Stub 7 formula, asymmetry (i) |
| South half untouched and still true | Route `(9,4)F(8,5)(8,6)(7,7)(6,7)(5,7)` carries no `B`; touches column 5 only at (5,7), row 7, below (5,5); gate re-verified this at `post-merge-11` | §2.13.2; gate report |
| Bare pair = set minimum | §4.7 Stub 7, T-SCN-11 formula `min over the opposing seat's Infantry … > the owning lane's cost`, range fixed by Q28 | Stub 7 formula + asymmetry (iii) |
| Fixture (a) names the minimiser | It names (1,3) and (9,3), which are the minima 6 and 6 in §2.13.2's table | fixture (a); §2.13.2 |
| Q30 blocks nothing computable | No fixture, integer, refusal condition, deployment or lane cost differs under either ruling | Stub 7 fixtures (a)(b)(c) |
| Register extent | Q1–Q29 today → Q1–Q30; ruled rows Q7, Q20, Q21, Q22, Q23, Q24, Q25, Q26, Q27, Q28 = ten, unchanged (Q30 ships unruled) | §4.7 register |
| Preamble substring is unique | `scoping the week-2 parity gate to its command set (Q29)` occurs once | §4.7 register preamble |
| Source is current | `source/MANIFEST.txt`: `gdd.md … md5=68991030a238c1804a3234db2fa0485f`, the hash the Director names | MANIFEST |

**What I deliberately did not do.**

- **I did not delete the 14.** It is a true measurement of the shipped
  minimiser's Bridge-free cost, and it is the figure that makes the bullet's
  point about how far the Bridge is worth. It stays, labelled. If the Director
  rules Q30 the strict way, deleting it is a one-line follow-up.
- **I did not touch the asserted reading anywhere.** 6, the eight-route table,
  fixture (a)'s "1 MP each way", the deployments, the terrain distribution and
  every `T-`/`Q` ID are as they were. Only the counterfactual figure, its
  scoping, and the convention that governs scoping move.
- **I did not re-derive *The Causeway*'s "3 against 5".** No Bridge-free
  counterfactual is printed for it, so the defect class cannot apply; §2.13.6's
  own numbers are `scenario-designer`'s.
- **I did not add a Bridge-free column to §2.13.2's table.** That remains a
  change request I am not making — the counterfactual belongs in §4.7's
  reasoning, not in the map's shipped route table, and pricing map cells is not
  my lane.

## Build order

Unchanged. No week number, dependency, acceptance set or `T-` ID moves. Restated
for completeness only:

| # | System (ledger row) | Depends on | Headless? | Acceptance test IDs |
|---|---|---|---|---|
| 7 | Scenario file & validator (Stub 7) | 1, 2 structural; **3** for the priced half (T-SCN-04, 06, 08, 11) | Yes | T-SCN-01..09, 11 — **unchanged**; T-SCN-10 reserved-unwritten (Q26) |

Nothing here changes what any gate computes. All five pairs change what the
document *claims about* T-SCN-11 — one counterfactual integer, its scoping, the
print rule that governs scoping, and one register row. The validator's inputs,
formula, unit set, reported integers and refusal conditions are identical before
and after, and every fixture reports the same pair it reported before this file.

Worth stating once, because it is the standing risk this round exposes: **§4.7's
prose is the one part of row 7 with no gate.** Every integer inside a fenced
spec block that a fixture does not recompute is an unguarded assertion, and this
document now holds at least one class of them — counterfactual measurements. The
cheap mitigation is not a new invariant; it is the Q30 labelling rule, which
makes an unguarded figure *say* what it is scoped to, so a reader can check it
without re-running Dijkstra. That is why I filed the convention gap rather than
proposing a gate for a number no build will ever compute.

## Change requests

| Existing § | Current text | Proposed change | Why |
|---|---|---|---|
| §4.7 Stub 7, T-SCN-11 `PRINT CONVENTION` | Two relations, two printed forms, no quantifier stated at any print site | **Pair 3** | The bare pair's right-hand term is the set minimum by the invariant's own formula, but the convention never says so where figures are printed, and it offers no form at all for a hex-scoped cost. Two forms, three quantities. |
| §4.7 Stub 7, T-SCN-11 (ii), *Ferrum* bullet | "Bridge-free, the cheapest route **from that hex** to that objective costs **14** MP" | **Pair 1** | True of (1,3), and now labelled as such. The bullet also prints the quantity the invariant compares — **13**, from (1,5) — and the fact that excluding the Bridges moves the minimising unit, which is why the two figures differ. |
| §4.7 Stub 7, T-SCN-11 (ii), `WHY` paragraph | "North still passes, at **5 against 14** … widening that margin from 1 MP to **9 MP**" | **Pair 2** | A bare pair asserts the set minimum, which is **13**, not 14. Margin **8 MP**. The argument is unchanged: both seats still pass, no gate still catches it, the widening is still single-digit. |
| §4.7 register preamble | Enumeration ends at Q29 | **Pair 4** | Q30 joins the enumeration. |
| §4.7 register | No Q30 row | **Pair 5** | Files the gap. Blocks nothing computable; conservative reading in force and free. |

## Open questions for the Director

**One new: Q30.** The register goes **Q1–Q30**, still **ten ruled** (Q7, Q20,
Q21, Q22, Q23, Q24, Q25, Q26, Q27, Q28). Q30 ships **unruled with a
conservative reading in force**, which is the register's ordinary state — the
conservative reading here costs words only, unlike Q28, where it would have
refused a shipped map.

**Q30 — what a T-SCN-11 "against" print quantifies over, and what form a
hex-scoped route cost takes.** Full row in Pair 5. The choice in one line:
*third printed form* ("14 from (1,3) alone, not the set minimum") or
*prohibition* (a hex-scoped cost may not appear in an "against" at all). I have
written the third-form reading into the convention and the bullet because it is
the reading that keeps the most information; the prohibition is stricter and
cheaper to police, and would delete the 14.

**What is not a question, and why I resolved it rather than filing it.** Whether
the printed 14 asserts a set minimum is *derivable* — the formula plus Q28
settle it, and the answer is yes, which is why the figure is wrong and Pairs 1
and 2 correct it to 13 without waiting on a ruling. Filing that would have
registered a deduction and left a wrong integer in the document pending an
answer. The gap I filed is the one a ruling can actually close.

**And the correction to my own last round, stated plainly since the Director
asked.** In `post-merge-11` I declined to file this on the ground that no
invariant computes the counterfactual, so nothing would notice a later drift.
That was an answer to "is it guarded," used as an answer to "is it true." The
figure was already wrong when I wrote that sentence. I have changed the test I
apply: **a printed integer is an assertion whether or not a gate recomputes it,
and the register carries the gaps that let a wrong assertion be written** —
which is what Q30 is, and what "no gate would notice" is not a defence against.

**Still unowned, unchanged:** title / lineage framing (`narrative-designer`,
Tier 2, not in this kit).

## Handoffs

- **`scenario-designer`** — **no action required, and one thing to know before
  editing *Ferrum Crossing*.** No cell of §2.13.2 moves: the eight-route table,
  the deployments, the terrain distribution and the layout block are untouched,
  and the 13 MP route is built out of that table's own guided South lane. The
  thing to know: **West's Bridge-free minimum to North is achieved by (1,5), not
  by (1,3)**, and it runs through (5,7) — so a future edit to the southern pass,
  to (7,6), or to West's second Infantry deployment changes a figure §4.7
  prints. That figure is not gate-computed, so nothing will flag it. If you want
  it guarded rather than labelled, the ask is a Bridge-free column on the
  eight-route table, which is yours to price and mine to gate — but I am not
  requesting it, because no invariant asserts the counterfactual.
- **`rules-designer`** — no action. No rule, cost, comparison, operator or
  ruling changes. `>` stays the ruled comparison, equality still fails, Q21,
  Q22, Q26 and Q28 keep their rulings verbatim, and Q29's cell is not edited —
  Pair 5 only appends after it.
- **`ux-onboarding-designer`** — no action. §2.11.6's guided-opening beats and
  the directive strip are untouched. Note for context only: the 13 MP route
  passes through West's own guided South objective, which is a fact about
  pathing, not about anything the player is shown.
- **`continuity-gate`** — Pairs 1, 2 and 3 must land together. Pair 2's "the
  (1,5) route above" reads against Pair 1's route; Pair 3's Ferrum example reads
  against both. Pairs 4 and 5 are a matched register pair. The re-read table
  above gives the operands for every new integer, including the reverse-Dijkstra
  tails (9/8/9) and the approaches (5/5/5 and 5/6/6) that make 13 minimal —
  those are the numbers to re-derive if you re-measure.
- **Director** — all five pairs are corrections or the register row that records
  why the correction was needed. Only Q30 needs a ruling, and nothing waits on
  it: the conservative reading is written in and is free.

## Grounding

| Claim | Backed by |
|---|---|
| A bare pair's right-hand term is the set minimum | §4.7 Stub 7, T-SCN-11 formula: `min over the opposing seat's Infantry of cost(hex, objective) > the owning lane's cost`; range fixed by asymmetry (iii) and Q28 ("every CanCapture-row unit that seat deploys") |
| The convention gives a bare pair to owning-vs-opposing | §4.7 Stub 7 PRINT CONVENTION: "the pair is written BARE — '5 against 6' — and always owning first" |
| The convention has no form for a hex-scoped cost | §4.7 Stub 7 PRINT CONVENTION lists exactly two relations and two forms; no third is named anywhere in the stub |
| West's Bridge-free minimum to North is 13, from (1,5) | Route `(2,6)(3,6)(3,7)(4,7)(5,7)F(6,7)(7,6)T(6,5)(6,4)w(6,3)w(6,2)`, priced off §2.13.2's layout under §2.3 costs; minimality from the sealed-column argument and the reverse-Dijkstra tails 9/8/9 at (5,6)/(5,7)/(5,8) |
| Column 5 is sealed at rows 0–5 Bridge-free | §2.13.2 key coordinates: Water (5,0)(5,2)(5,3)(5,5), Bridges (5,1)(5,4); Water impassable to land units (§2.3; Q16, Recon is a land unit) |
| The first five hexes are West's guided South lane | §2.13.2 route table, West **(1,5)** *guided* → South: `5 — (2,6)(3,6)(3,7)(4,7)(5,7)` |
| d(1,3) Bridge-free = 14, unchanged | §4.7 Stub 7 (ii) current text and its printed route; independently re-derived as min(5+9, 6+8, 6+9) |
| Excluding the Bridges moves the minimiser | §2.13.2 route table gives (1,3)=6, (1,5)=7 with Bridges; measurement gives (1,5)=13, (1,3)=14 without |
| The Mountain is not the cause of the 1 MP | (1,3) has a Mountain-free 14: `(2,4)(3,4)(4,4)(4,5)(5,6)(5,7)F(6,7)(7,6)T(6,5)(6,4)w(6,3)w(6,2)`; the tail from (5,7) is 8 for both units |
| Margin 8 MP | 13 − 5, owning lane 5 from fixture (a) |
| Both seats still pass the counterfactual | North 13 > 5; South 6 > 5 (unchanged, no `B` on `(9,4)F(8,5)(8,6)(7,7)(6,7)(5,7)`); T-SCN-11 asserts strict inequality with NO CEILING (asymmetry (i)) |
| South's opposing 6 stands under either reading | Gate-verified at `post-merge-11`: adjacency-valid, 6 MP, equal to the axial geodesic, touches column 5 only at (5,7) below (5,5), uses no Bridge |
| Q30 blocks nothing computable | §4.7 Stub 7 fixtures (a)(b)(c) and the Determinism/Acceptance lines are identical under either ruling; no deployment, lane cost or map hex depends on a print form |
| Register extent and ruled count | §4.7 register rows Q1–Q29 today; ruled Q7, Q20, Q21, Q22, Q23, Q24, Q25, Q26, Q27, Q28 = ten. Q30 appended unruled |
| The register may hold an unruled row with a reading in force | §4.7 register preamble: "where a reading is stated, it is the conservative one … chosen so that a later ruling loosens behavior rather than invalidating a passing gate"; and "where the conservative reading is not free, this register states no reading and waits" — here it is free |
| Source is current | `source/MANIFEST.txt`: `gdd.md <- …\Stratocracy_Prototype_GDD.md md5=68991030a238c1804a3234db2fa0485f` |
