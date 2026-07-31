> # ✅ APPLIED ADDENDUM — DO NOT RE-APPLY
>
> Every replacement pair in this file **has been applied to the master GDD**, and
> the master has moved on since. Its Old blocks no longer match, so re-applying is
> a no-op at best; its quoted "current" text, register extents, and open items are
> a **snapshot of the moment it was written**, not the state of the document.
>
> Specifically: its Q21 proposal was routed and applied by the Director, so the cell it quotes as "current" is stale and re-proposing it would double-apply.
>
> **The master GDD is the source of truth** — read `source/gdd.md`. Further changes
> to a merged section go in a *new* addendum file.

# Technical design — post-merge-3 addendum (tech-director)

> **Read this first.** `sections/tech.md` (nine pairs) and
> `sections/tech_post-merge-2.md` (two pairs) are **applied**; their Old blocks
> no longer match and neither file is edited here. Every passage below is an
> exact old→new replacement against `source/gdd.md`
> (md5 `a576f78ea88395e0e4fde38b0a649468`, the re-sync carrying
> `scenario-designer`'s §2.13 rework and my Amendments A and B).
>
> **Nothing in this file outside an OLD/NEW pair is meant to be merged.** That
> was the `post-merge-2` violation and it is not repeated: every cross-reference
> inside a replacement block resolves to a section number, a test ID, a field
> name, or arithmetic the reader can redo on the page. No block cites "the note
> above", a gate run, or a section file.

## Placement

| # | Amendment | Target | Required? |
|---|---|---|---|
| A | T-SCN-08 — new justification, new fixtures | §4.7 Stub 7, invariants | **Yes** — both current sentences are false |
| B | New `symmetry` field, appended at the tail | §4.7 Stub 7, `Fields:` | **Yes** — Q24 already cites it |
| C | New invariant **T-SCN-09** — declared symmetry verified in axial | §4.7 Stub 7, invariants | **Yes if B lands** |
| D | `Acceptance: T-SCN-01..08` → `..09` | §4.7 Stub 7 | With C |
| E | Row 7 test IDs and "eight invariants" | §4.11 | With C |
| F | Q-register extent sentences + new **Q25** row | §4.7 open questions | With C |

Amendments A and B are independent of each other. C–F land together or not at
all. No existing invariant is renumbered: T-SCN-05 (not mine) is untouched,
T-SCN-06/07 are untouched, T-SCN-08 keeps its ID, and T-SCN-09 is the next free
number.

## Draft

### Amendment A — §4.7 Stub 7, T-SCN-08

The behaviour does not change: **computes, never infers** is still right, and
§2.13.1 explicitly keeps it. What is replaced is the *reason* — which repeated
the false inference §2.13.1 has now retracted — and the *fixture data*, which
cites a `mirror` declaration that is no longer a legal value on lane numbers
that no longer exist.

The new justification rests on three reasons the flag cannot substitute **even
when it is correct**, which is a stronger position than the old one:

1. It is an **authored declaration**. Measurement is the only thing that catches
   an author declaring the wrong one — §2.13.1's own argument, and the thing
   that actually happened: the flag said mirrored, the numbers said 3 and 4.
2. A **`none`-declared map offers nothing to infer from at all.** *Ferrum
   Crossing* is the map that ships; on it, inference has no input.
3. Even a **verified** `rot180` implies equal lane cost only if the two
   `guidedOpening` entries are themselves ρ-images — which §2.13.1 nowhere
   requires and T-SCN-09 does not assert (Q25, below). Both stretch maps happen
   to be drawn that way, which is *why* their numbers come out equal. The
   equality is a measured result, not a theorem.

Plus the fixture `scenario-designer` offered, which is worth taking because it
is the one case no symmetry argument of any kind can price: **cheapest path is
not fewest hexes.**

**OLD**

```
  T-SCN-08  measured, not inferred: the validator COMPUTES and REPORTS each
            entry's lane cost as an integer, from Stub-3 pathing. The declared-
            symmetry flag (§2.13.1) is not an input and cannot substitute — an
            odd-r row offset lets a mirrored or rotated layout price the two
            seats' lanes differently. Fixtures: a mirror-declared scenario whose
            lanes cost 3 and 4 PASSES and reports both numbers (Longwater March,
            §2.13.1); one whose lanes both cost 7 FAILS. The reported integers
            are the source of truth for §2.13.1's lane table, so a map edit that
            lengthens a lane surfaces as a changed number rather than a still-
            green boolean.
```

**NEW**

```
  T-SCN-08  measured, not inferred: the validator COMPUTES and REPORTS each
            entry's lane cost as an integer, from Stub-3 pathing. The declared-
            symmetry flag (§2.13.1) is not an input and cannot substitute. Not
            because the flag is unreliable in principle — a verified rot180 IS
            an isometry and does imply equal cost between IMAGE lanes (§2.13.1,
            T-SCN-09) — but for three reasons that hold even when it is right:
            (i) it is an AUTHORED DECLARATION, and measurement is the only
            thing that catches the author declaring the wrong one, which is
            what happened here (the flag said mirrored; the numbers said 3 and
            4; the numbers were right, §2.13.1); (ii) a `none`-declared map
            offers nothing to infer from at all, and `none` is what the SHIPPED
            map declares (§2.13.2); (iii) even a verified rot180 forces equal
            lane cost only if the two guidedOpening entries are themselves
            rho-images, which §2.13.1 does not require and T-SCN-09 does not
            assert (Q25) — so equal numbers on a symmetric map are a result,
            not a theorem. And no symmetry argument of any kind prices a lane,
            because cheapest path is not fewest hexes.
            Fixtures:
              (a) The Causeway (§2.13.6) PASSES, reporting 3 and 3. Its West
                  lane (1,2)->(1,1)->(2,1)->(3,2) is THREE hexes costing 3 MP
                  through the town; the TWO-hex route over the Mountain at
                  (2,2) costs 4 (§2.3). An implementation that counts hexes
                  instead of summing MoveCost reports 2, and nothing else in
                  this suite catches it.
              (b) Longwater March (§2.13.5), rot180 on 13 x 8, PASSES and
                  reports 4 and 4 — COMPUTED equal, never assumed equal.
              (c) A scenario whose lanes both cost 7 FAILS the T-SCN-06
                  ceiling, and the refusal reason CARRIES BOTH MEASURED
                  INTEGERS: an author needs to read 7 against 6, not merely
                  "too far" (Determinism, "refuses with a reason").
            The reported integers are the source of truth for §2.13.1's lane
            table, so a map edit that lengthens a lane surfaces as a changed
            number rather than a still-green boolean.
```

### Amendment B — §4.7 Stub 7, the `symmetry` field

**Decision: Stub 7 carries it.** Q24's Blocks column names "Stub 7's `symmetry`
field," and the field does not exist — the enum lives only in §2.13.1's
validation-invariant prose. Three arguments, and I think the first is
sufficient on its own:

- §2.13.1 lists "declared symmetry is machine-verified in axial" among the
  invariants the `validate_scenario` tool checks *against the schema in §4.7
  Stub 7*. **A claim the file cannot state is a claim the validator cannot
  check.** Today the declaration exists only in §2.13's prose tables, which the
  loader never reads.
- It belongs in the `scenarioHash` preimage. A map redrawn from `mirror` to
  `rot180` — which is exactly what just happened to both stretch maps — is a
  content change, and a content hash that does not move for it is not a content
  hash.
- It is the only field that can carry Q24's even-row precondition to the point
  of load, where refusing costs one comparison instead of H×W of them.

Appended at the tail after `guidedOpening`, per the append-only preimage policy
this stub already pins. **Required, not optional**: an absent value defaulting
to `none` is exactly the silent default §4.8's loader principle forbids. I do
not rule Q24 — the field is written to the reading §2.13.1 carries **today**,
and cites Q24 as pending, so a ruling either way changes this text and nothing
else.

**OLD**

```
                                   directly — marked/locked is presentation
                                   state, not rules state, so it stays out of
                                   the Stub-8 snapshot.
Invariants:
```

**NEW**

```
                                   directly — marked/locked is presentation
                                   state, not rules state, so it stays out of
                                   the Stub-8 snapshot.
           symmetry        enum    REQUIRED. `rot180` or `none`, the two values
                                   §2.13.1 declares (pending Q24; `mirror` is
                                   not a value, because no odd-r rectangle has
                                   a mirror axis at any dimension). Absent or
                                   unrecognized is a hard load failure, never a
                                   default of `none` — a scenario that forgets
                                   to declare must not silently claim the
                                   weakest claim. This is not a balance or
                                   layout field: it is the AUTHORED CLAIM that
                                   T-SCN-09 verifies hex by hex, and it exists
                                   in the schema because §2.13.1 asks
                                   validate_scenario to machine-verify a
                                   declaration the file previously had no place
                                   to make. Appended at the tail per the
                                   scenarioHash policy above; it moves every
                                   scenario's hash, which costs nothing while
                                   no scenario file exists and is the point of
                                   the policy once one does.
Invariants:
```

### Amendment C — §4.7 Stub 7, new invariant T-SCN-09

§2.13.1's "declared symmetry is machine-verified in axial" is a machine check
that **no §4.7 invariant asserts**. T-SCN-05 supplies the axial frame and
asserts nothing about symmetry. So the document currently promises a gate that
does not exist — the same shape of gap as the `guidedOpening` fields before
`post-merge-1`, and it is the reason the false `mirror` declarations survived
as long as they did.

One derivation is load-bearing enough to go in the document, because without it
an implementer has to choose between two ways of rotating and one of them is
wrong. §2.13 authors ρ in offset coordinates, ρ(c, r) = (W−1−c, H−1−r), but
T-SCN-05 forbids loaded state from holding `(col, row)`, so the check must run
in axial. Composing ρ with the odd-r conversion `q = c − (r − (r&1))/2` gives,
**on an even row count**, a single parity-free affine map:

```
    rho(q, r) = (W - H/2 - q,  H - 1 - r)
```

with no even/odd case split — which is the concrete sense in which symmetry
"lives in axial." **On an odd row count the two forms come apart**: the offset
expression is still a well-defined index permutation and will happily produce
comparisons, but it is no longer an isometry, and the isometry's axial constant
`W − H/2` is a half-integer, so no hex has a hex image at all. On 9 × 9 the
constant is 4.5 and hex (1,1) rotates to column 6.5. That is why the even row
count must be a **precondition** and not a comparison: on odd H there is
nothing to compare, and an author who declares `rot180` there deserves one
refusal rather than a scatter of failed hex tests.

(The algebra behind the formula is in **Grounding**, not in the GDD — the
invariant cites only the formula and arithmetic a reader can redo in place.)

**OLD** (T-SCN-08 is currently the last invariant; its closing lines, as
Amendment A leaves them, followed by the `Determinism:` line)

```
            The reported integers are the source of truth for §2.13.1's lane
            table, so a map edit that lengthens a lane surfaces as a changed
            number rather than a still-green boolean.
Determinism: pure parse + validation; any failure refuses the whole file with a
```

**NEW**

```
            The reported integers are the source of truth for §2.13.1's lane
            table, so a map edit that lengthens a lane surfaces as a changed
            number rather than a still-green boolean.
  T-SCN-09  declared symmetry is VERIFIED, not trusted — the gate §2.13.1's
            "machine-verified in axial" clause names, and which no other
            invariant asserts (T-SCN-05 supplies the axial frame and asserts
            nothing about symmetry).
            `symmetry` == `none` asserts nothing and is always well-formed.
            `symmetry` == `rot180` asserts, for EVERY in-bounds hex h:
              - terrain(rho(h)) == terrain(h);
              - ownership maps onto itself with the two sides EXCHANGED — each
                home factory's image is the other side's home, each neutral
                capturable's image is neutral (§2.7);
              - the placement set maps onto itself with sides exchanged and
                unitId and isFlag preserved, which is what §2.13.5 and §2.13.6
                mean by "East is the exact rho-image of West."
            SCOPE per Q25: guidedOpening is NOT bound, so a rot180 map may name
            lanes that are not each other's image and report unequal costs
            (T-SCN-08 (iii)). Both stretch maps satisfy the stronger reading as
            drawn, so ruling Q25 either way moves no layout.
            rho RUNS IN AXIAL, after the T-SCN-05 conversion, because no loaded
            state holds (col, row) to rotate. On an even row count §2.13's
            authored rho(c, r) = (W-1-c, H-1-r) and the 180-degree isometry are
            the same map, and in axial it is one parity-free affine map:
                rho(q, r) = (W - H/2 - q,  H - 1 - r)
            The EVEN ROW COUNT is a PRECONDITION, not a comparison: on odd H
            that constant W - H/2 is a half-integer, so no hex has a hex image
            and the file is REFUSED WITH A REASON before any comparison runs
            (§2.13.1, pending Q24). On 9 x 9 the constant is 4.5 and (1,1)
            rotates to column 6.5 — one refusal, rather than the offset index
            permutation quietly producing geometrically meaningless
            comparisons.
            Structural: no pathing, so this lands with rows 1-2 (§4.11).
Determinism: pure parse + validation; any failure refuses the whole file with a
```

### Amendment D — §4.7 Stub 7, the Acceptance line

**OLD**

```
Acceptance: T-SCN-01..08 headless. The §4.2 validate_scenario MCP tool wraps the
```

**NEW**

```
Acceptance: T-SCN-01..09 headless. The §4.2 validate_scenario MCP tool wraps the
```

### Amendment E — §4.11, row 7 and the critical-path paragraph

T-SCN-09 is structural — it needs the T-SCN-05 conversion and Stub 1's hex
math, no path — so it joins the half that can start once rows 1–2 land. The
priced half is unchanged at three invariants; only the denominator moves.

**OLD**

```
| 7 | Scenario file & validator (Stub 7) | 1, 2 for the structural half (T-SCN-01..03, 05, 07); **3 for the priced half** — T-SCN-04, 06, 08 all cost a path | Yes; MCP tool wraps it in-editor, manual fallback stands | T-SCN-01..08 |
```

**NEW**

```
| 7 | Scenario file & validator (Stub 7) | 1, 2 for the structural half (T-SCN-01..03, 05, 07, 09); **3 for the priced half** — T-SCN-04, 06, 08 all cost a path | Yes; MCP tool wraps it in-editor, manual fallback stands | T-SCN-01..09 |
```

**OLD**

```
(T-SCN-01..03, 05, 07) starts once 1–2 land, but three of its eight
invariants — T-SCN-04's flag reachability and T-SCN-06/08's opening-capture
```

**NEW**

```
(T-SCN-01..03, 05, 07, 09) starts once 1–2 land, but three of its nine
invariants — T-SCN-04's flag reachability and T-SCN-06/08's opening-capture
```

### Amendment F — §4.7, the Q register

Two extent sentences and one appended row. The first extent sentence is already
stale by one — it says `Q1–Q23` and the register runs to Q24.

**OLD**

```
state, the gate is parameterized on a numbered open question (Q1–Q23, Open
questions below) — the Director rules, the gate then pins the ruling.
```

**NEW**

```
state, the gate is parameterized on a numbered open question (Q1–Q25, Open
questions below) — the Director rules, the gate then pins the ruling.
```

**OLD**

```
gating §2.13.1's opening-capture invariant (Q21–Q22), and the milestone
contradiction the document knowingly carries (Q23) — so that each question
```

**NEW**

```
gating §2.13.1's opening-capture invariant (Q21–Q22), the milestone
contradiction the document knowingly carries (Q23), and the two raised by the
§2.13 symmetry correction (Q24–Q25) — so that each question
```

The Q25 row is a pure append, so its pair is anchored on the tail of Q24's row
and the heading that follows the table. Q24's row is not modified.

**OLD**

```
no layout moves. |

### 4.8 Data contract — DataTable schemas
```

**NEW**

```
no layout moves. |
| **Q25** | What a `rot180` declaration binds. §2.13.1 says declared symmetry is machine-verified but never says over *what*. Terrain only? Terrain + ownership + placements — the reading both stretch maps are actually drawn to (§2.13.5 "every one of those is a ρ-pair"; §2.13.6 "East is the exact ρ-image of West")? And does it bind `guidedOpening`, so the two seats' lanes must themselves be ρ-images? | T-SCN-09's assertion set; and T-SCN-08's fixture (b), whose equal 4 / 4 is a *theorem* if `guidedOpening` is bound and only a *measurement* if it is not | Terrain + ownership (sides exchanged) + placements (sides exchanged), as gated in T-SCN-09. `guidedOpening` is **not** bound: §2.13.1 requires each seat's lane to be its own neutral within 6 MP, never that the two be images of each other, so a `rot180` map may legitimately name non-image lanes and report a split. Costless either way today — both stretch maps satisfy the *stronger* reading as drawn (*Longwater*: ρ(1,2) = (11,5) and ρ(4,1) = (8,6); *Causeway*: ρ(1,2) = (7,5) and ρ(3,2) = (5,5)), so ruling `guidedOpening` in would fail no shipped map, and ruling terrain-only would merely loosen T-SCN-09. |

### 4.8 Data contract — DataTable schemas
```

## Build order

Rows 1–10 stand as merged. Row 7 gains one structural invariant and no
dependency; nothing that was gated becomes ungated, and no ledger row changes
status. The eight `*pending*` rows are still pending — `Source/` is still the
stock Unreal template, and the only green rows remain Combat, its test suite,
Repair and Type-effectiveness at `5ffa8d6` (17/17).

| # | System (ledger row) | Depends on | Headless? | Acceptance test IDs |
|---|---|---|---|---|
| 7 | Scenario file & validator (§4.7 Stub 7) | 1, 2 for the structural half (T-SCN-01..03, 05, 07, **09**); 3 for the priced half — T-SCN-04, 06, 08 all cost a path | Yes; MCP tool wraps it in-editor, manual fallback stands | T-SCN-01..**09** |

Sequencing note, unchanged in substance: T-SCN-09 is the cheapest invariant in
the stub — one affine map and a full-board comparison, no pathing, no data
table beyond terrain Ids. It can be written and passing before movement exists,
which means the symmetry claim on both stretch maps is machine-checked in week
1 rather than at week 4 when the maps are drawn.

## Change requests

| Existing § | Current text | Proposed change | Why |
|---|---|---|---|
| — | — | None against another author's section | Q24's Blocks column names a field that did not exist; **Amendment B resolves that by making the referent exist**, not by editing `scenario-designer`'s row. Same move as `post-merge-1` made for §2.13.1's `guidedOpening.infantry` citation: when a forward reference points into my schema, the schema is what is wrong. |

## Open questions for the Director

**One new: Q25** (drafted in Amendment F). It is a genuine gap — §2.13.1 says
symmetry is machine-verified and never says over what — and it surfaced only
because writing T-SCN-09 forced the assertion set to be enumerated. The stated
reading is gated so nothing is blocked, and it costs nothing either way today.

**Q24 is not ruled here.** Amendment B writes the field to §2.13.1's current
reading and cites Q24 as pending. Amendment C's precondition clause says
"pending Q24" for the same reason. If the Director rules the other way — hex
comparisons instead of a refusal — the only edits are those two clauses, and
the derivation in T-SCN-09 stands either way, since it explains *why* the odd-H
comparisons would be meaningless rather than asserting what to do about them.

**Q21 — yes, its cell should be updated, and I would go further.** Two things
in the current cell are now false: it cites "§2.13.1's measured 5/5, 3/4, 2/3"
(the last two are dead numbers — they are 4/4 and 3/3), and it says "If the
Director rules 'as deployed,' all three maps need re-measuring," which §2.13.1
now contradicts directly: both stretch lanes are clear of their seat's own
starting units and price identically under either reading, so only *Ferrum
Crossing* is exposed. I have **not** written a pair for it, because the cell is
in the shared register and `scenario-designer` has just edited the section it
cites — you asked me to say whether it should move, not to move it. Proposed
replacement text for the two clauses, if you want to route it:

- `the reading that reproduces §2.13.1's measured 5/5, 3/4, 2/3` →
  `the reading that reproduces §2.13.1's measured 5/5, 4/4, 3/3`
- `If the Director rules "as deployed," all three maps need re-measuring and
  §2.13.1's numbers may move.` → `If the Director rules "as deployed," only
  *Ferrum Crossing* is exposed — §2.13.1 records that both stretch lanes are
  clear of their own seat's other four units and price identically under either
  reading. Q21 is now a one-map question.`

That narrowing is worth having on the record even before Q21 is ruled: it drops
the blast radius of the ruling from three maps to one, which is the difference
between a ruling that can wait and one that cannot.

**Not a Q, but flagged once** — an implementation trap for whoever writes Stub
1, which I found while deriving ρ in axial and which needs no ruling. T-SCN-05
forbids loaded state from holding `(col, row)`, and the axial image of an
odd-r rectangle is a **sheared parallelogram**, not a `0..W−1 × 0..H−1` box:
on *The Causeway*, offset (0,3) is axial (−1, 3), a negative `q`. So T-HEX-05's
"inBounds agrees with the Q1 dimensions" cannot be a naive range check on `q`
— it has to invert the shear. That is a one-line fix if it is known in advance
and a whole afternoon of wrong bounds failures if it is not.

## Handoffs

- **`scenario-designer`** — your fixture candidate is taken as written and is
  now fixture (a) of T-SCN-08, with the 3-hex/3-MP town route and the
  2-hex/4-MP Mountain route both named, because the numbers are the whole
  demonstration. Two things to know: (1) T-SCN-09 asserts `rot180` over
  terrain, ownership **and** placements, which both your maps satisfy as drawn
  — if you ever draw a `rot180` map with deliberately asymmetric deployment,
  that gate refuses it and Q25 is the place to argue for it; (2) T-SCN-09 does
  **not** bind `guidedOpening`, so your two seats' lanes are free to be
  non-images, and their being images on both maps is why the reported costs
  come out equal. That is recorded in the invariant, not assumed by it.
- **Director / merge** — A and B are independent; C–F land together. If C is
  rejected, D/E/F must be dropped with it, or the acceptance line, the
  build-order row and the register extents will name an invariant and a question
  that do not exist. That is the failure mode this addendum is fixing, so I would
  rather state it than rely on it being obvious.
- **`rules-designer`, `ux-onboarding-designer`** — no interaction. Nothing here
  touches §2.7, §2.8, or §2.11; the guided opening's two fields and their gates
  (T-SCN-06/07) are unchanged.

## Grounding

| Claim | Backed by |
|---|---|
| Both sentences of the current T-SCN-08 are false | `source/gdd.md` §2.13.1: "**Declared symmetry does imply equal lane cost** … a 1 MP split … is proof the layout is not symmetric. An earlier draft of this section argued the opposite from the odd-r row offset; that confused a storage convention with a geometry." And `mirror` "is therefore not a declarable value (Q24)." |
| §2.13.1 keeps "computes, never infers", and why | §2.13.1: "The validator still **measures and records each seat's cost as a number** (T-SCN-08) … because it is an *authored declaration* and measurement is the only thing that catches it being wrong. That is exactly what it caught here." |
| Fixture (a)'s numbers | §2.13.6: "The West lane is (1,2)→(1,1)→(2,1)→(3,2), through the town rather than over the Mountain at (2,2) — the 2-hex route costs 4 MP and the 3-hex route costs 3, which is the case T-SCN-08's 'computes, never infers' wording exists for." Costs per §2.3 (Mountains 3, Town 1, Plains 1). |
| Fixture (b)'s numbers and dimensions | §2.13.1 lane table (*Longwater March* 4 MP / 4 MP); §2.13.5 dimensions 13 × 8, `rot180`, ρ(c, r) = (12−c, 7−r) |
| *Ferrum Crossing* declares `none` | §2.13.7 scenario-set summary, Symmetry column: "Asymmetric (Fame-correctable)"; untouched at 11 × 9 |
| §2.13.1 asks for a machine check that no §4.7 invariant asserts | §2.13.1 validation-invariant bullet: "declared symmetry is machine-verified **in axial** (§4.7's T-SCN-05 forbids loaded state from holding `(col, row)` at all, so the check has no other place to run)". T-SCN-05's own text asserts only round-trip conversion and adjacency. |
| Q24 cites a field that does not exist | §4.7 Q24, Blocks column: "§2.13.1's validation-invariant list; Stub 7's `symmetry` field and T-SCN-08's fixtures". Stub 7's `Fields:` block ends at `guidedOpening`. |
| Required-not-optional, no silent default | §4.8's loader principle: "Missing column or unparseable value = hard load failure, never a silent default." |
| **ρ in axial** = `(W − H/2 − q, H − 1 − r)` on even H | Derivation: with `q = c − (r − (r&1))/2` and ρ(c,r) = (W−1−c, H−1−r), for even `r` the image row is odd, giving `q' = W−1−q − r/2 − (H−2−r)/2 = W−1−q−(H−2)/2`; for odd `r` the image row is even, giving `q' = W−1−q − (r−1)/2 − (H−1−r)/2 = W−1−q−(H−2)/2`. Both collapse to `W − H/2 − q`. |
| …and it is verified, not just derived | *Longwater* (W13 H8, K = 9): home (1,3)→axial (0,3); ρ→(9,4); East home (11,4)→axial (9,4) ✓. Neutral (4,1)→(4,1); ρ→(5,6); (8,6)→(5,6) ✓. *Causeway* (W9 H8, K = 5): flag (0,3)→(−1,3); ρ→(6,4); (8,4)→(6,4) ✓. Infantry (1,2)→(0,2); ρ→(5,5); (7,5)→(5,5) ✓. |
| On odd H the constant is a half-integer, and (1,1) → column 6.5 on 9 × 9 | K = 9 − 9/2 = 4.5. Hex (1,1) → axial (1,1); ρ → (3.5, 7); back to offset `c = 3.5 + (7−1)/2 = 6.5`. Independently reproduces the counterexample the Director verified before applying §2.13.1. |
| On odd H the offset form is still a well-defined permutation | ρ(c,r) = (W−1−c, H−1−r) is integer-valued for any W, H — which is precisely the hazard: it produces comparisons that are not an isometry's. Consistent with §2.13.1 fact 2 ("column W−1 of every odd row is left without an image"), which describes the same breakage in the offset frame. |
| Both stretch maps satisfy the stronger Q25 reading | *Longwater* ρ(c,r) = (12−c, 7−r): ρ(1,2) = (11,5) ✓ and ρ(4,1) = (8,6) ✓ against §2.13.5's guided opening. *Causeway* ρ(c,r) = (8−c, 7−r): ρ(1,2) = (7,5) ✓ and ρ(3,2) = (5,5) ✓ against §2.13.6's. |
| Q21's cell cites dead numbers | §4.7 Q21 says "5/5, 3/4, 2/3"; §2.13.1's table now reads 5/5, **4/4**, **3/3**. §2.13.1 also now states both stretch lanes "price identically under either reading of Q21 — the shipped map is the only one whose numbers a Q21 ruling could move." |
| The axial image of an odd-r rectangle is sheared | Same conversion: *Causeway* offset (0,3) → `q = 0 − (3−1)/2 = −1`. Negative `q` is in bounds. |
| Nothing else in §4 makes a symmetry claim | §4.7 Shared conventions carries the odd-r → axial contract only; `symmetry` appears nowhere in §4.8–§4.11. |
