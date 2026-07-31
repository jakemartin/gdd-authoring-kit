> # ✅ APPLIED ADDENDUM — DO NOT RE-APPLY
>
> Every replacement pair in this file **has been applied to the master GDD**, and
> the master has moved on since. Its Old blocks no longer match, so re-applying is
> a no-op at best; its quoted "current" text, register extents, and any hash it
> names are a **snapshot of the moment it was written**, not the current state.
>
> **The master GDD is the source of truth** — read `source/gdd.md`. Further changes
> to a merged section go in a *new* addendum file.

# Technical design — post-merge-10 draft (tech-director)

## Placement

Five pairs, all in **§4.7** (Pending-system gate plan): three inside the
**Stub 7** fenced block (T-SCN-08 fixture (c), T-SCN-11's print paragraph,
T-SCN-11 asymmetry (ii)), two in the **open-questions register** (rows **Q21**
and **Q17**). No other section is touched. No map, lane number, terrain
figure, week number, `T-` ID or `Q` ID moves. T-SCN-10 stays reserved and
unwritten. The register stays **Q1–Q29, ten ruled**.

## Draft

### Violation 1 — the claim is false, and the correction is a reframe

The gate is right and the fixture in my own stub already said so. Fixture (a)
prices *Ferrum Crossing*'s North objective as **5 against 6**, where the 6 is
"West's cheapest 6 from (1,3) **over the north Bridge (5,1)**" — a Bridge, on
an opposing route, on the shipped map. §2.13.2's route table prints the same
cell with the `B` glyph: `6 — (2,3)(3,2)(4,2)(4,1)(5,1)B(6,2)`. So "no other
map in the set has a Bridge on any opposing route" is false for *Ferrum
Crossing*, and the sentence containing it is the sentence I corrected last
round.

I re-derived the counterfactual before writing the replacement, and it changes
what the clause should *say*, not merely what it should not:

| Route | Bridges permitted | Bridges excluded |
|---|---|---|
| West (1,3) → North (6,2) | **6 MP**, over (5,1)ᴮ (§2.13.2) | **14 MP** — `(2,3)(3,4)(3,5)(4,5)(5,6)(6,6)m(6,5)(6,4)w(6,3)w(6,2)` |

Column 5 is Water at rows 0, 2, 3, 5 and Bridge at rows 1 and 4, so a
Bridge-free crossing must run through rows 6–8 and then climb the east bank's
Woods ring. **The allowance is load-bearing, not permitted.** And the sharp
part: a Bridge-free reading would **still pass** *Ferrum Crossing* — 14 is
strictly more than the owning lane's 5 — so no gate in the suite catches it.
It would simply replace a measured 1 MP margin, the thinnest in the set, with
a double-digit number describing a detour nobody walks. That is why the new
text states the allowance as the *reason the margin is real* rather than as a
liberty the invariant never exercises, exactly as the gate suggested.

Only ***Longwater March*** has no Bridge on any opposing route, and only
because its terrain distribution is Water 0, Bridge 0 (§2.13.5).

### Violation 2 — the disambiguation is rebuilt without integer order

The gate's finding stands: a T-SCN-11 refusal whose opposing route is *cheaper*
prints "7 against 5" — larger integer first — so "the one relation whose
failing form prints the larger integer first" separates nothing. Both relations
lead with the larger number when they fail:

| Relation | Site | Passing form | Failing form |
|---|---|---|---|
| owning vs opposing | T-SCN-11 | smaller first (5 against 6) | larger first (7 against 5), or equal on a tie (5 against 5) |
| measured vs budget | T-SCN-06, reported by T-SCN-08 (c) | — (a pass prints no pair) | larger first (7 against the 6 MP ceiling) |

So the convention I own is now: **the relation is named at the site, and
integer order identifies nothing.** Concretely — a bare integer pair is always
owning-against-opposing; a budget comparison always writes its right-hand term
as the ceiling it is ("the 6 MP ceiling"), never as a bare integer; two
integers joined by "and" are the two seats' own lanes and assert no inequality.
That is checkable by looking at one site, needs no cross-reference, and does
not depend on magnitude. Pair 2 states it at the definition; pair 3 makes
fixture (c) rest on it and withdraws the false half explicitly, so the
withdrawn reading cannot be re-derived by a later editor.

### The class sweep the gate asked for

**Class:** a claim quantified over *the set of maps* (or over the document)
rather than measured per map. **Fourteen sites in §4.7 carry one.** One is
false, one is overstated, one is ambiguous, eleven hold. Line numbers are
against `source/gdd.md` md5 `d940fbb7…`.

| Line | Site | The quantified claim | Verdict |
|---|---|---|---|
| 1458 | §4.7 preamble | "nothing else in this document names a range of them" (quantified over the whole GDD) | **Holds** — every `Q<n>` reference in the master outside §4.7 names a single ID (Q4, Q5, Q6, Q11, Q15, Q19, Q21, Q22, Q24, Q26, Q27, Q28). The only ranges are at lines 2035–2043, inside the register itself. |
| 1702–1707 | Stub 7 `symmetry` | "at most ONE non-`none` value is well-formed on any given map" | **Holds** — a parity theorem (rot180 needs even H, a horizontal mirror odd H), not a survey. |
| 1793–1794 | T-SCN-08 (ii) | "`none` is what the SHIPPED map declares" | **Holds** — singular, per map (§2.13.2). |
| 1836–1837 | T-SCN-09 | "Both stretch maps satisfy the stronger reading as drawn" | **Holds** — re-derived: *Longwater* ρ(1,2)=(11,5), ρ(4,1)=(8,6); *Causeway* ρ(1,2)=(7,5), ρ(3,2)=(5,5), each against that map's own `guidedOpening`. |
| **1916–1918** | **T-SCN-11 (ii)** | **"no other map in the set has a Bridge on any opposing route"** | **FALSE for *Ferrum Crossing*** → **Pair 1** |
| 1933–1936 | T-SCN-11 (iii) | "the only free southern hexes clearing 5 MP were the Artillery's and the Flag Tank's" | **Holds** — map-internal and stated per hex in §2.13.2, not set-quantified. |
| 1954–1955 | T-SCN-11 fixture (a) | "the thinnest in the set"; "the one map that declares `symmetry: none`" | **Holds** — margins are 1 (*Ferrum*), 2 (*Causeway*), 4 (*Longwater*); *Ferrum* is the only `none`. |
| 2081 (Q16) | Recon as a land unit | "All three maps are priced on this reading" | **Holds** — vacuous on *Longwater* (Water 0), true on the two river maps. |
| **2082 (Q17)** | Cross-Water fire | **"both river maps price a bridge lock on it"** | **Ambiguous** — §2.13.2 states the opposite of a lock for *Ferrum* ("tempo, not a topological wall") → **Pair 5, optional** |
| 2086 (Q21) | scope re-check | "no starting unit sits on any of the eight routes *Ferrum Crossing* now prices" | **Holds** — checked all eight routes in §2.13.2's table against all ten starting hexes; East's home factory (9,4) is on one route and is deliberately empty. |
| 2086 (Q21) | scope re-check | "both stretch lanes were already clear" | **Holds** — *Causeway* West (1,1)(2,1)(3,2) and its ρ-image; *Longwater*'s 4 MP lane and its ρ-image; no starting hex on either. |
| **2086 (Q21)** | slack | **"it remains the only map where a future deployment edit … flips a gate instead of being absorbed"** | **Overstated** — true as a margin ranking, false as a universal → **Pair 4** |
| 2091 (Q26) | enum scope | "no shipped map needs it"; "both stretch maps are even-H `rot180`" | **Holds** — 13×8 and 9×8; *Ferrum* declares `none`. |
| 2093 (Q28) | the forced relocation | "the only free southern hexes clearing 5 MP were the Artillery's and the Flag Tank's" | **Holds** — same per-hex basis as line 1933. |

**What the pattern says.** All three defects across the last two rounds sit in
the same construction: a superlative or a negative universal over "the set,"
written next to numbers that were measured one map at a time. The measured
numbers have been right every time; the sentence *around* them has been wrong
three times. The two required pairs below therefore replace the quantifier with
the per-map measurement rather than repairing the quantifier — after Pair 1 and
Pair 4, §4.7 contains no negative universal over the map set that is not either
a parity theorem or accompanied by the per-map figures that establish it.

§4.11's row-7 prose was swept too and carries no claim of this class.

---

### The pairs

**Pair 1 — Stub 7, T-SCN-11 asymmetry (ii). REQUIRED (violation 1).**
The false clause is removed and the allowance is restated as a reason. Every
figure is either already in the document (6 MP from §2.13.2's route table;
3 against 5 from fixture (c); Water 0 / Bridge 0 from §2.13.5) or the gate's
independently-verified 14 MP counterfactual, which is printed with its route so
it is re-derivable from §2.13.2's ASCII map. No lane number, terrain figure or
map changes; 14 MP is a counterfactual measurement of a Bridge-free reading
that is *not* asserted, not a route the shipped validator ever prices.

**OLD**

```
              (ii)  BRIDGES ARE ALLOWED on the opposing route. T-SCN-06's
                    Bridge-free clause is a property of the GUIDED lane —
                    what makes the first lesson a walk rather than a
                    crossing — not a constraint the enemy is under.
                    Excluding Bridges would make the opposing route
                    NON-EXISTENT on a bisected map (The Causeway, §2.13.6)
                    and pass that map vacuously, so allowing them is the
                    STRICTER reading and it is the one asserted. Measured, it
                    costs nothing: The Causeway passes 3 against 5 in both
                    seats with the crossing permitted, and no other map in
                    the set has a Bridge on any opposing route.
```

**NEW**

```
              (ii)  BRIDGES ARE ALLOWED on the opposing route, and on the
                    shipped map that allowance is LOAD-BEARING rather than
                    merely permitted. T-SCN-06's Bridge-free clause is a
                    property of the GUIDED lane — what makes the first
                    lesson a walk rather than a crossing — not a constraint
                    the enemy is under. Excluding Bridges would make the
                    opposing route NON-EXISTENT on a bisected map (The
                    Causeway, §2.13.6) and pass that map vacuously, so
                    allowing them is the STRICTER reading and it is the one
                    asserted. Measured PER MAP, never quantified over the
                    set:
                    - Ferrum Crossing (§2.13.2) EXERCISES it. The opposing
                      figure in fixture (a) — West's cheapest route to
                      North (6,2), 6 MP from (1,3) — runs over the north
                      Bridge (5,1). Bridge-free, the cheapest route from
                      that hex to that objective costs 14 MP:
                      (2,3)(3,4)(3,5)(4,5)(5,6)(6,6)m(6,5)(6,4)w(6,3)w
                      (6,2) — around the river's southern end, then up
                      through the Woods ring. More than double.
                    - The Causeway (§2.13.6) EXERCISES it too, passing
                      3 against 5 in both seats with the crossing
                      permitted; exclude Bridges and it reports "no route"
                      instead of 5 (fixture (c)).
                    - Longwater March (§2.13.5) is the ONE map with no
                      Bridge on any opposing route, and only because it
                      has no Water and no Bridge hexes at all — its
                      terrain distribution is Water 0, Bridge 0.
                    WHY THIS IS STATED AS A REASON AND NOT A PERMISSION: a
                    Bridge-free reading does not FAIL Ferrum Crossing. 14
                    is still strictly more than the owning lane's 5, so the
                    invariant still passes — it passes on a number that
                    describes a walk around the entire river, and fixture
                    (a)'s 1 MP margin, the thinnest in the set, evaporates
                    into a double-digit one. Nothing in this suite catches
                    an integer that has merely stopped meaning anything.
                    The Bridge is what makes that margin a margin.
```

---

**Pair 2 — Stub 7, T-SCN-11's print paragraph. REQUIRED (violation 2, cause).**
The convention is rebuilt so it never appeals to magnitude. It keeps the two
things that were sound — owning-first order, and "and" meaning two seats' own
lanes — and adds the naming rule plus an explicit statement that order carries
no information, with the reason. Replaces the paragraph pair 4 of post-merge-9
introduced at the same location.

**OLD**

```
            PRINT ORDER, stated here at the definition and used at every
            site below: a measured pair reads OWNING FIRST, THEN OPPOSING.
            "a against b" passes exactly when a < b, so on a PASSING map the
            SMALLER integer comes first. Two integers joined by "and"
            instead (T-SCN-08's fixtures, "3 and 3") are the two SEATS' own
            lanes — a different pair, asserting no inequality.
```

**NEW**

```
            PRINT CONVENTION, stated here at the definition and used at
            every site below: THE RELATION IS NAMED AT THE SITE, and
            integer order identifies nothing. Two relations in this stub
            print an "against":
              - OWNING against OPPOSING (this invariant). Both terms are
                measured route costs; the pair is written BARE — "5
                against 6" — and always owning first.
              - MEASURED against BUDGET (T-SCN-06's ceiling, reported by
                T-SCN-08 fixture (c)). The right-hand term is written as
                the CEILING it is — "7 against the 6 MP ceiling" — never
                as a bare integer. A bare pair is therefore always the
                first relation.
            ORDER CARRIES NO INFORMATION, neither about which relation is
            in play nor about pass or fail, and that is a correction
            rather than a restatement: BOTH relations print the larger
            integer first on their FAILING form. T-SCN-06 fails when the
            measurement exceeds its ceiling; T-SCN-11 fails whenever the
            opposing route is no dearer than the owning lane, which prints
            "7 against 5" when the enemy is closer and "5 against 5" on a
            tie. Magnitude order separates neither the two relations from
            each other nor a pass from a refusal — only the naming does,
            so every site names its relation and no site relies on which
            integer is bigger. Two integers joined by "and" instead
            (T-SCN-08's fixtures, "3 and 3") are the two SEATS' own
            lanes — a different pair, asserting no inequality.
```

---

**Pair 3 — Stub 7, T-SCN-08 fixture (c). REQUIRED (violation 2, instance).**
The sound half — naming both sides of the comparison — now carries the whole
disambiguation, and the false half is withdrawn *in the text* so the
retracted reasoning cannot be reconstructed by a later editor. Numbers
unchanged: 7 measured, 6 MP ceiling.

**OLD**

```
              (c) A scenario whose lanes both cost 7 FAILS the T-SCN-06
                  ceiling, and the refusal reason CARRIES BOTH MEASURED
                  INTEGERS: an author needs to read the measured 7 against
                  the 6 MP CEILING, not merely "too far" (Determinism,
                  "refuses with a reason"). This is the only "against" in
                  this stub that is not owning-vs-opposing: it compares a
                  measurement to a budget, and it is the one relation whose
                  FAILING form prints the larger integer first, so it names
                  both sides rather than relying on the print order.
```

**NEW**

```
              (c) A scenario whose lanes both cost 7 FAILS the T-SCN-06
                  ceiling, and the refusal reason CARRIES BOTH MEASURED
                  INTEGERS: an author needs to read the measured 7 against
                  the 6 MP CEILING, not merely "too far" (Determinism,
                  "refuses with a reason"). This is the only "against" in
                  this stub that is not owning-vs-opposing: it compares a
                  MEASUREMENT to a BUDGET, and it SAYS SO at the site —
                  the right-hand term is printed as "the 6 MP ceiling",
                  never as a bare integer, per T-SCN-11's print
                  convention. NAMING THE RELATION IS THE WHOLE OF THE
                  DISAMBIGUATION. Integer order does not separate the two,
                  because a T-SCN-11 refusal whose opposing route is
                  cheaper prints the larger integer first as well; the
                  earlier reading — that this was the one relation whose
                  failing form led with the larger number — was false and
                  is withdrawn.
```

---

**Pair 4 — register row Q21, the slack sentence. REQUIRED (sweep, overstated
universal).** "The only map where a deployment edit flips a gate" is true as a
margin *ranking* and false as a universal: a large enough edit flips *The
Causeway* too, at 2 MP of T-SCN-11 margin. The replacement prints the per-map
slack instead of asserting a superlative, which is the same repair Pair 1
makes. **No figure is new** — *Longwater*'s 2 MP ceiling slack is stated in
§2.13.5, *The Causeway*'s 3 MP in §2.13.6, and the two margins are subtractions
of pairs this same register already prints at Q22 (4 against 8; 3 against 5).
Q21's ruling, its scope re-check and its one-reverse-Dijkstra consequence are
untouched. This is a single-line substring of the Q21 cell.

**OLD**

```
It stays a live question rather than a dead one because of slack: *Ferrum Crossing* carries 1 MP against T-SCN-06's ceiling and 1 MP against T-SCN-11's inequality, so it remains the only map where a future deployment edit landing in a priced route flips a gate instead of being absorbed.
```

**NEW**

```
It stays a live question rather than a dead one because of slack — measured per map, not asserted over the set: *Ferrum Crossing* carries 1 MP against T-SCN-06's ceiling and 1 MP against T-SCN-11's inequality; *Longwater March* carries 2 MP and 4 MP; *The Causeway* 3 MP and 2 MP. No figure there is new — each ceiling slack is stated in that map's own section (§2.13.5, §2.13.6) and each margin is a subtraction of the owning/opposing pair this register already prints at Q22. So *Ferrum Crossing* is the **tightest map in the set on both gates at once**, and the one where a deployment edit landing in a priced route is likeliest to flip a gate rather than be absorbed — which is a ranking, not the claim that the other two maps cannot be flipped at all.
```

---

**Pair 5 — register row Q17. OPTIONAL, PRECISION ONLY, SAFE TO SKIP.**
Not a factual error and not one of the two violations. "Both river maps price a
bridge lock on it" is the same construction as the two claims that were wrong,
and it reads across §2.13.2, which states the opposite in terms: "bridge
control here is *tempo*, not a topological wall," and reserves full lockout for
*The Causeway*. Under the charitable reading — locking a bridge *by fire* — the
sentence is true of both maps; under the other it contradicts the shipped map's
own section. The rewrite says per map what each map prices, changes no ruling,
no number and no dependency, and leaves the answer cell untouched. **If the
Director reads "bridge lock" as fire-lock and prefers the shorter cell, drop
this pair and nothing downstream changes.**

**OLD**

```
| **Q17** | Cross-Water Artillery fire. With LOS blocking a stretch goal (§2.2), bank-to-bank fire across a one-hex river is legal at ship, and both river maps price a bridge lock on it. | §2.13.2 and §2.13.6 balance, if LOS ever ships | Legal. If LOS blocking ships, Water must not block — or those two maps need a redesign pass. |
```

**NEW**

```
| **Q17** | Cross-Water Artillery fire. With LOS blocking a stretch goal (§2.2), bank-to-bank fire across a one-hex river is legal at ship, and the two river maps price it **per map, not alike**: *Ferrum Crossing* prices contested **bank control** on it — opposite banks are distance 2, inside Artillery range, so fire crosses before units do (§2.13.2, which states as explicitly that bridge control there is *tempo, not a topological wall*); *The Causeway* prices its **Mountain perches** on it — range 2–3 covers the bridge hex from +40% cover with no counter (§2.13.6). *Longwater March* has no Water and prices nothing on it (§2.13.5). | §2.13.2 and §2.13.6 balance, if LOS ever ships | Legal. If LOS blocking ships, Water must not block — or those two maps need a redesign pass. |
```

## Build order

Unchanged by this revision. No week number, dependency or acceptance set moves.
Row 7 still straddles the critical path, still closes on row 3, and its
acceptance set is still `T-SCN-01..09, 11 (10 reserved-unwritten on Q26)`.
Restated for completeness only:

| # | System (ledger row) | Depends on | Headless? | Acceptance test IDs |
|---|---|---|---|---|
| 7 | Scenario file & validator (Stub 7) | 1, 2 structural; **3** for the priced half (T-SCN-04, 06, 08, 11) | Yes | T-SCN-01..09, 11 — **unchanged**; T-SCN-10 reserved-unwritten by the Q26 ruling |

Nothing in this revision changes what any gate computes. Pairs 1–3 change what
the document *claims about* T-SCN-08 and T-SCN-11; pairs 4–5 change what the
register claims about the map set. The validator's inputs, formulas, reported
integers and refusal conditions are identical before and after.

## Change requests

| Existing § | Current text | Proposed change | Why |
|---|---|---|---|
| §4.7 Stub 7, T-SCN-11 (ii) | "…and no other map in the set has a Bridge on any opposing route." | **Pair 1** | False for *Ferrum Crossing*: its opposing route to North runs over Bridge (5,1) at 6 MP; Bridge-free the same trip is 14 MP. The allowance is load-bearing, and a Bridge-free reading would pass anyway — so it must be stated as a reason, not a permission. |
| §4.7 Stub 7, T-SCN-11 print paragraph | "on a PASSING map the SMALLER integer comes first" | **Pair 2** | Order-based disambiguation does not work: both relations print the larger integer first when they fail. Replaced with naming the relation at every site. |
| §4.7 Stub 7, T-SCN-08 (c) | "the one relation whose FAILING form prints the larger integer first" | **Pair 3** | Same defect, the instance the gate caught. The claim is withdrawn in the text; naming both sides carries the fix alone. |
| §4.7 register, Q21 | "it remains the only map where a future deployment edit … flips a gate instead of being absorbed" | **Pair 4** | Overstated universal over the map set; replaced by the per-map slack, all four figures already in the document. |
| §4.7 register, Q17 | "both river maps price a bridge lock on it" | **Pair 5** (*optional*) | Same construction as the two failures, and reads across §2.13.2's "tempo, not a topological wall." Precision, not correctness. |

## Open questions for the Director

**None new. No ID is filed. The register stays Q1–Q29, ten ruled** (Q7, Q20,
Q21, Q22, Q23, Q24, Q25, Q26, Q27, Q28).

Both violations were factual/wording defects against rules that already exist —
§2.13.2's route table supplies the Bridge fact, and the print convention is
mine to set, which the gate said explicitly. Neither needs a Director ruling.

**One candidate was considered and deliberately not filed.** While re-deriving
the Bridge route I found that *Ferrum Crossing*'s West (1,3) → North lane has
at least two equal-cost 6 MP witnesses: §2.13.2 prints
`(2,3)(3,2)(4,2)(4,1)(5,1)B(6,2)`, and `(2,3)(3,2)(3,1)T(4,1)(5,1)B(6,2)` also
costs 6. The obvious question — *which* witness a validator reports — is **not
a gap**, because T-SCN-08 and T-SCN-11 report **costs, never routes** ("carries
BOTH measured integers"), and the cost is unique regardless of which equal-cost
path the tie-break selects. T-MOVE-04's canonical-order tie-break makes the
*executed* path reproducible, which is a different and already-ruled concern.
Filing a Q here would add an ID for a question the specification already
answers by not asking it. Flagged rather than filed, per the standing rule that
the register carries gaps and not observations.

## Handoffs

- **`scenario-designer`** — no action required, one observation. §2.13.2's
  eight-route table is the authority I corrected §4.7 *to*, and no cell of it
  moves. The observation: the routes it prints are *witnesses* of a cheapest
  cost, not unique paths — the West (1,3) → North cell has at least one other
  6 MP route. Nothing depends on this today (no gate reports a route), so it
  needs no edit; it would only matter if §2.13 ever started claiming its
  printed routes are the unique cheapest ones.
- **`rules-designer`** — no action. No rule, cost, comparison or ruling
  changes; Q21, Q22, Q26 and Q28 keep their rulings verbatim.
- **`ux-onboarding-designer`** — no action. §2.11.6's guided-opening beats and
  the directive strip are untouched; nothing here reaches a widget.
- **Director** — pairs 1–4 are corrections; **pair 5 needs a yes/no** and is
  safe to drop.

## Grounding

| Claim | Backed by |
|---|---|
| *Ferrum Crossing* has a Bridge on an opposing route | §2.13.2 route table, West (1,3) → North: `6 — (2,3)(3,2)(4,2)(4,1)(5,1)B(6,2)`; §4.7 T-SCN-11 fixture (a), "West's cheapest 6 from (1,3) over the north Bridge (5,1)" |
| Bridge-free, that route costs 14 MP | Gate's independent Dijkstra (`post-merge-9` finding), re-derived here against §2.13.2's ASCII map: column 5 is Water at r0/r2/r3/r5 and Bridge at r1/r4, so a Bridge-free crossing runs rows 6–8; costs `1+1+1+1+1+3(m)+1+2(w)+2(w)+1 = 14` |
| A Bridge-free reading still passes the map | 14 > 5, the owning lane (fixture (a)); T-SCN-11 asserts strict inequality only, "NO CEILING" (asymmetry (i)) |
| *Longwater March* is the only map with no Bridge on an opposing route | §2.13.5 terrain distribution: Water 0 · Bridge 0 |
| *The Causeway* exercises the allowance | §4.7 T-SCN-11 fixture (c) and asymmetry (ii); §2.13.6, Water fills column 4 except Bridges (4,2)/(4,5) |
| Both relations print the larger integer first when they fail | T-SCN-06 fails on measured > ceiling; T-SCN-11 fails on owning ≥ opposing, i.e. "7 against 5" or "5 against 5" (fixtures (b), and Q22's tie) |
| Margins are 1 / 2 / 4 and ceiling slacks 1 / 3 / 2 | *Ferrum*: 5 against 6, "1 MP of slack against the 6 MP ceiling" (§2.13.2); *Causeway*: 3 against 5 (Q22), "3 MP of slack" (§2.13.6); *Longwater*: 4 against 8 (Q22), "2 MP of slack" (§2.13.5) |
| Both stretch maps' guided lanes are ρ-images | §2.13.5 `guidedOpening` (1,2)/(11,5), (4,1)/(8,6) under ρ(c,r)=(12−c,7−r); §2.13.6 (1,2)/(7,5), (3,2)/(5,5) under ρ(c,r)=(8−c,7−r) |
| No starting unit sits on any of the eight priced *Ferrum* routes | §2.13.2 starting positions (0,4)(1,3)(1,5)(0,3)(0,5)/(10,4)(9,3)(9,1)(10,5)(10,3) checked against every hex of the eight-route table; (9,4) is on one route and is the deliberately empty home factory |
| No Q range is named outside §4.7 | Every `Q<n>` occurrence in the master: outside §4.7 all are single IDs (lines 203, 205, 404, 423, 594, 635, 716, 732, 735, 757, 768, 770, 775, 848, 930, 934, 1050, 1095, 1390–1398, 2124, 2263, 2333–2362) |
| §2.13.2 refuses a lockout reading for *Ferrum* | §2.13.2, "If one side holds both bridges: the other side is not locked out … bridge control here is *tempo*, not a topological wall" |
| Register extent | §4.7 register rows Q1–Q29; ruled rows Q7, Q20, Q21, Q22, Q23, Q24, Q25, Q26, Q27, Q28 = ten |
| Source is current | `source/MANIFEST.txt`: `gdd.md … md5=d940fbb7bc11469c5aef3d5b869bb19b` |
