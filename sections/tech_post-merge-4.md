> # ✅ APPLIED ADDENDUM — DO NOT RE-APPLY
>
> Every replacement pair in this file **has been applied to the master GDD**, and
> the master has moved on since. Its Old blocks no longer match, so re-applying is
> a no-op at best; its quoted "current" text, register extents, and any hash it
> names are a **snapshot of the moment it was written**, not the current state.
>
> **The master GDD is the source of truth** — read `source/gdd.md`. Further changes
> to a merged section go in a *new* addendum file.

# Technical design — post-merge-4 addendum (tech-director)

> **Read this first.** `sections/tech.md`, `sections/tech_post-merge-2.md` and
> `sections/tech_post-merge-3.md` are **applied**; their Old blocks no longer
> match and none of them is edited here. Every passage below is an exact
> old→new replacement against `source/gdd.md`
> (md5 `3a46006757d147dd4ed5924c2467152d`).
>
> **Nothing outside an OLD/NEW pair is meant to be merged.** Every explanatory
> note sits *before* its `**OLD**` marker, never between the marker and its
> fence.

## Placement

Two independent items, eight pairs. Both land in §4; nothing outside §4 is
touched.

| # | Pair | Target | Item | Required? |
|---|---|---|---|---|
| 1 | Dev-time cost table A, restated so it composes | §4.6 | 2 | **Yes** — three numbers in one table disagree |
| 2 | Runtime cost table B, arithmetic closed | §4.6 | 2 | **Yes** — two derived figures are wrong |
| 3 | Headline totals | §4.6 | 2 | **Yes** — carries pair 1's error |
| 4 | §4.7 preamble register extent `Q1–Q25` → `Q1–Q26` | §4.7 | 1 | With Q26 |
| 5 | Stub 7 `symmetry` field description | §4.7 | 1 | **Yes** — repeats the false claim |
| 6 | Reserved **T-SCN-10** note after T-SCN-09 | §4.7 | 1 | With Q26 |
| 7 | Open-questions preamble extent sentence | §4.7 | 1 | With Q26 |
| 8 | New **Q26** row | §4.7 register | 1 | With Q26 |

Pairs 1–3 are Item 2 and are independent of Item 1. Pair 5 is required
whatever the Director does with Q26; pairs 4, 6, 7, 8 land together or not at
all. **If Q26 is declined**, pair 5 still applies with its penultimate sentence
changed from `... and Q26 asks which one is intended.` to `... and no scenario
in §2.13 is drawn to a horizontal mirror, so the schema does not offer the
value.` No test ID is renumbered anywhere: T-SCN-05 is untouched, T-SCN-06/07/08
are untouched, T-SCN-09 keeps its ID and its assertions, and T-SCN-10 is the
next free number and asserts nothing.

**Sites I am replacing, so nothing is double-applied.** Item 1 touches exactly
**one** site in the merged text: §4.7 Stub 7's `symmetry` field description
(pair 5). I am **not** touching §2.13.1 fact 1, §2.13.5's Symmetry row, or the
Q24 row's question text or its assumption column — all four are
`scenario-designer`'s in this run, including the Q24 row even though the
register table physically sits inside §4.7. My Q26 row cross-references Q24
rather than editing it, so the two addenda cannot collide on a line. One
possible **fifth** site is flagged under Handoffs.

---

## Draft

### Item 1 — the geometry, and what it does and does not cost

**What is false and what is not.** The merged claim, *"No odd-r rectangle has a
mirror axis, at any dimension,"* is true of the **vertical** axis and false of
the **horizontal** one. The original derivation is a vertical-axis argument:
even rows occupy columns 0…W−1 centred on (W−1)/2, odd rows sit ½ hex east
centred on W/2, and one vertical line cannot serve both parities — correct, at
every W, and unaffected by anything below. The horizontal axis is a different
map and a different parity condition:

    mu_offset(c, r) = (c, H-1-r)

With **H odd**, `H−1` is even, so `r` and `H−1−r` always share a parity; every
row therefore keeps its ½-hex offset, the column is unchanged, and the board
closes. **11 × 9 *Ferrum Crossing* carries this axis** — μ(c, r) = (c, 8−r) —
which is the counterexample.

It is a genuine isometry, not an index permutation, and that is checkable in
axial where the module actually works. Converting `q = c − (r − (r&1))/2` on
both sides, with H odd so the parity term cancels:

    mu(q, r) = (q + r - (H-1)/2,  H-1-r)          [H odd; (H-1)/2 is an integer]

Distance preservation follows from the axial metric
`(|dq| + |dr| + |dq+dr|) / 2` directly. Under μ:
`dq' = dq + dr`, `dr' = −dr`, `dq' + dr' = dq`. The three absolute terms are
therefore a **permutation** of the original three, so the sum — and the
distance — is identical. μ is the reflection that swaps two of the three cube
axes, composed with a translation. On *Ferrum Crossing*, (H−1)/2 = 4 and
μ(q, r) = (q + r − 4, 8 − r): offset (0,0) → axial (0,0) → μ → (−4, 8) →
offset (0,8), and offset (10,1) → axial (10,1) → μ → (7,7) → offset (10,7).
Both are hexes; nothing lands off-lattice.

**The two symmetries are mutually exclusive, and that is the useful part.**
`rot180` needs an **even** row count (the axial constant `W − H/2` is a
half-integer otherwise — that derivation is untouched by this correction and
stays right). A horizontal mirror needs an **odd** one. A vertical mirror never
exists. And their composition would *be* a vertical mirror, so there is no
fourth case. **At most one non-`none` value is ever well-formed on a given
map**, which means admitting a second value could not widen what any single
scenario is allowed to declare.

**Does Q24's proposed enum survive? Yes — its justification does not.** Q24
makes three claims. Two are untouched: `rot180` is well-formed only on even H,
and `rot180` on odd H is a hard refusal before any hex comparison. The middle
claim — *"`mirror` is a value the validator could never legally accept"* — is
now true only of the vertical axis. So `rot180 | none` can still be the enum,
but as a **scope** decision: no §2.13 map is drawn to a horizontal mirror, and
the one shipped odd-H map declares `none` because its terrain is asymmetric, not
because the geometry forbids the claim.

The Director should weigh one consequence, because the failure mode changes.
Under the impossibility reading, an author who writes `mirror` is writing
nonsense and refusing them is obviously right. Under the scope reading, an
author of an odd-H map who has genuinely drawn a horizontal mirror is writing a
**true** claim that the schema forces down to `none` — and `none` asserts
nothing, so a verifiable property is silently lost rather than an error caught.
That is Q26. It is not a rules question and it blocks nothing today: no
scenario file exists, and no shipped map wants the value.

**Does T-SCN-09 need a horizontal-mirror case? No — it is correct as written.**
T-SCN-09 is quantified on the *declared* value, not on the map's geometry:
`none` asserts nothing and is always well-formed; `rot180` asserts ρ over
terrain, ownership and placements; its odd-H clause refuses `rot180` on odd H,
which stays right for exactly the reason it always did. T-SCN-09 cannot be
wrong about a horizontal mirror because it never claims anything about one. The
gate that does not exist is the one that would verify a horizontal
*declaration* — and it does not exist because the value does not exist. It is
reserved as **T-SCN-10** against Q26, in the same manner as T-MOVE-07 against
Q2: named, derived, and asserting nothing until the Director rules.

**Nothing else in my lane moves.** T-SCN-08's three fixtures are unaffected —
(a) *The Causeway* 9 × 8 and (b) *Longwater March* 13 × 8 both declare
`rot180` on an even row count, and (c) is synthetic. T-SCN-08's clause (i)
recounts that an earlier draft's flag said mirrored while the numbers said 3
and 4; that remains true as a historical fact about a wrong declaration and
does not depend on which axis was meant. T-SCN-05, T-SCN-06 and T-SCN-07 are
untouched, and §4.11's row 7 is unchanged.

### Item 2 — §4.6, restating the dev-time cost so it composes

**The ~22% gap is not slack; it is the Opus escalation, folded in once and then
applied again.** The per-task figure is right and is derivable from the
published rates I may not change: 300k input at ⅔ cache is 100k fresh + 200k
cache read, so
`100k × $2/M + 200k × $0.20/M + 45k × $10/M = $0.20 + $0.04 + $0.45 = $0.69`.
Rounded, the table's `~$0.70`. Against 210 tasks that is **$145**, and the
stated subtotal is $180 — a gap of $33, or 22.5%.

The same 210 tasks priced on Opus 4.8 cost
`100k × $5/M + 200k × $0.50/M + 45k × $25/M = $1.725` each. Escalating 15% of
tasks — 31.5 of them — from Sonnet to Opus costs the *delta*:
`31.5 × ($1.725 − $0.69) = $32.6`. And `$144.9 + $32.6 = $177.5 ≈ $180`, to the
dollar. The subtotal already contained the escalation; the clause after it then
charged for it a second time. I am therefore surfacing it as a named line rather
than adjusting a figure, exactly as the gate preferred — the missing 22% is a
real cost, correctly computed once.

The `≈ $225` is a separate, third error and cannot be rescued by any reading:
15% of $180 is $207, and no stated base times any stated percentage yields
$225. Removing the second application removes it.

The reading pinned here is that escalation **substitutes** for Sonnet on those
tasks rather than running **in addition** to it. That is a cost-model
assumption, not a rule, and I state it in the table because it is not
self-evident — but it is the reading the document already made, since it
reproduces its own $180 to the dollar. The alternative (Opus re-runs *on top
of* Sonnet) would put the escalation line at `31.5 × $1.725 = $54` and the
subtotal at ≈ $200.

**Part B and the headline.** Part B's per-turn cost is right
(`2.5k × $1/M + 1.5k × $0.10/M + 0.4k × $5/M = $0.0047`) and its per-match
$0.09 and Haiku $18 follow. Two figures do not: 20 turns × 4.4k is **88k**, not
~80k, so 200 matches is **17.6M** tokens rather than ~16M; and the
`~$60 (Sonnet 5)` alternative is computed at the **$3/$15 standard** rate, not
the $2/$10 introductory rate §4.6 says applies to this project — at the
introductory rate the same volume is **$37**. I keep both, labelled, because
both are true against a rate the document cites and neither rate is mine to
change.

**The headline token figure survives.** 72.45M dev-time + 17.6M runtime = 90.05M
— the `~90M` was right, arriving there through two errors that happened to
cancel. The cost band does not survive: the true all-in is **$197 (Haiku
commander)** to **$215 (Sonnet 5 commander)**, with **$178** if the stretch
commander never ships. The old `$200–$300` top end is recoverable as an
*overrun* figure rather than a baseline — at 1.5× task volume (315 tasks) the
dev-time line is `315 × $0.69 + 47 × $1.035 ≈ $267` and the all-in lands near
$290 — which is worth stating explicitly, because a band whose ceiling has no
derivation is not a transparent ceiling.

---

## Replacement pairs

### Pair 1 — §4.6, dev-time table A

Replaces the six-line table only; the paragraph above it (rates, models, unit of
work) is unchanged, as are the rates themselves.

**OLD**

```
| Line item | Estimate |
|---|---|
| Tokens per substantial task | ~300k input (≈⅔ served from cache) + ~45k output |
| Cost per task | ~$0.70 (Sonnet 5, cached) |
| Task volume | 5 agent roles × ~6 tasks/wk × 7 wk ≈ **210 tasks** |
| **Dev-time subtotal** | **≈ 75M tokens · ≈ $180**, + ~15% Opus escalation → **≈ $225** |
```

**NEW**

```
| Line item | Estimate |
|---|---|
| Tokens per substantial task | ~300k input (≈⅔ from cache: ~100k fresh + ~200k cache read) + ~45k output = **345k**. The ~30% overhead margin above is already inside these figures and is not applied again below |
| Cost per task — Sonnet 5 | 100k × $2/M + 200k × $0.20/M + 45k × $10/M = $0.20 + $0.04 + $0.45 = **$0.69** |
| Cost per task — Opus 4.8 | 100k × $5/M + 200k × $0.50/M + 45k × $25/M = $0.50 + $0.10 + $1.13 = **$1.73** |
| Task volume | 5 agent roles × ~6 tasks/wk × 7 wk ≈ **210 tasks** |
| Sonnet-only base | 210 × $0.69 ≈ **$145** · 210 × 345k ≈ **72M tokens** |
| **Opus escalation — a line, not a multiplier** | ~15% of tasks (≈ 32) run on Opus *instead of* Sonnet, same tokens at a higher rate: 32 × ($1.73 − $0.69) ≈ **+$33** |
| **Dev-time subtotal** | **≈ 72M tokens · ≈ $178** ($145 + $33) |

**The escalation is priced once.** It is a *delta* between two models on the
same task, so it belongs inside the subtotal and there is no further uplift
after it — an earlier draft folded it into the subtotal silently and then
applied it a second time to reach $225, which is why three figures in one table
disagreed. Every number above is re-derivable from the two rate lines and the
task count, which is the property that made the error visible. The escalation
assumes Opus **substitutes** for Sonnet on those tasks; if it instead runs *in
addition* (a re-run rather than a substitution) the line is 32 × $1.73 ≈ +$55
and the subtotal ≈ $200.
```

### Pair 2 — §4.6, runtime table B

Replaces the six-line table only. Rates are unchanged; the Sonnet 5 line now
names which of the two published rates each figure uses.

**OLD**

```
| Line item | Estimate |
|---|---|
| Tokens per AI turn | ~2.5k fresh input + ~1.5k cached rules + ~0.4k output |
| Cost per AI turn | ~$0.005 (Haiku) |
| Per match (~20 AI turns) | ~80k tokens · ~$0.09 |
| 200 self-play + playtest matches | ~16M tokens · ~$18 (Haiku) / ~$60 (Sonnet 5) |
```

**NEW**

```
| Line item | Estimate |
|---|---|
| Tokens per AI turn | ~2.5k fresh input + ~1.5k cached rules + ~0.4k output = **4.4k** |
| Cost per AI turn | 2.5k × $1/M + 1.5k × $0.10/M + 0.4k × $5/M ≈ **$0.0047** (Haiku 4.5) |
| Per match (~20 AI turns) | 88k tokens · ≈ **$0.09** |
| 200 self-play + playtest matches | ≈ **17.6M tokens** · ≈ **$19** (Haiku 4.5) |
| Same volume on Sonnet 5 | ≈ **$37** at the introductory $2/$10 rate this project runs inside · ≈ **$56** at the $3/$15 standard rate that resumes 1 Sep 2026 |
```

### Pair 3 — §4.6, headline

**OLD**

```
**Headline.** Development authoring dominates; the whole jam lands near **~90M tokens, roughly $200–$300**, of which the runtime commander is a small, stretch-only slice. Cost scales linearly with task volume, so if agent authorship runs hotter than planned the ceiling stays transparent rather than surprising.
```

**NEW**

```
**Headline.** Development authoring dominates. Dev-time alone is **≈ 72M tokens · ≈ $178**; the stretch runtime commander adds **≈ 18M tokens** and **$19 (Haiku 4.5)** to **$37 (Sonnet 5)**. The whole jam therefore lands at **≈ 90M tokens** and **≈ $178 without the commander, ≈ $197–$215 with it**. Cost scales linearly with task volume, and the overrun case is stated rather than buried in a wide band: at **1.5× task volume** (315 rather than 210 tasks) the dev-time line is 315 × $0.69 + 47 × $1.03 ≈ **$267**, putting the all-in near **$290**. That is the ceiling, and it is a derivation rather than a round number — as is every figure in the two tables above.
```

### Pair 4 — §4.7 preamble, register extent

**OLD**

```
that certified Combat (§3 ledger). Where a stub needs a rule the GDD does not
state, the gate is parameterized on a numbered open question (Q1–Q25, Open
questions below) — the Director rules, the gate then pins the ruling.
```

**NEW**

```
that certified Combat (§3 ledger). Where a stub needs a rule the GDD does not
state, the gate is parameterized on a numbered open question (Q1–Q26, Open
questions below) — the Director rules, the gate then pins the ruling.
```

### Pair 5 — §4.7 Stub 7, the `symmetry` field

The only §4 site of the corrected claim. Behaviour is unchanged: the field is
still REQUIRED, still `rot180 | none`, still a hard load failure when absent.
What is replaced is the *reason* the enum is narrow — impossibility becomes
scope — plus the counterexample and the mutual-exclusivity fact that make the
scope reading safe. The continuation indent is 35 columns, matching the
surrounding field block.

**OLD**

```
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
```

**NEW**

```
           symmetry        enum    REQUIRED. `rot180` or `none`, the two values
                                   §2.13.1 declares (pending Q24). The enum is
                                   narrow by SCOPE, not by impossibility, and
                                   the difference is load-bearing. An odd-r
                                   rectangle has no VERTICAL mirror axis at any
                                   dimension (§2.13.1) — but on an ODD row
                                   count it does have a HORIZONTAL one,
                                   mu(c, r) = (c, H-1-r): with H odd, H-1 is
                                   even, so r and H-1-r share a parity, every
                                   row keeps its offset and the column is
                                   unchanged. 11 x 9 Ferrum Crossing carries
                                   that axis geometrically and still declares
                                   `none`, because its terrain is not drawn to
                                   it. So `mirror` is a claim the schema gives
                                   an author no way to STATE, not one the
                                   validator could never ACCEPT — two different
                                   failure modes, and Q26 asks which one is
                                   intended. Admitting the value could widen
                                   nothing: rot180 needs an even H and a
                                   horizontal mirror an odd one, their
                                   composition would be the vertical mirror
                                   that never exists, so at most ONE non-`none`
                                   value is well-formed on any given map.
                                   Absent or unrecognized is a hard load
                                   failure, never a default of `none` — a
                                   scenario that forgets to declare must not
                                   silently claim the weakest claim. This is
                                   not a balance or layout field: it is the
                                   AUTHORED CLAIM that T-SCN-09 verifies hex by
                                   hex, and it exists in the schema because
                                   §2.13.1 asks validate_scenario to
                                   machine-verify a declaration the file
                                   previously had no place to make. Appended at
                                   the tail per the scenarioHash policy above;
                                   it moves every scenario's hash, which costs
                                   nothing while no scenario file exists and is
                                   the point of the policy once one does.
```

### Pair 6 — §4.7 Stub 7, reserved T-SCN-10 after T-SCN-09

T-SCN-09's assertions are unchanged. This appends a reserved note in the same
form as T-MOVE-07 under Stub 3: named, derived, asserting nothing. The OLD text
is T-SCN-09's closing line.

**OLD**

```
            Structural: no pathing, so this lands with rows 1-2 (§4.11).
```

**NEW**

```
            Structural: no pathing, so this lands with rows 1-2 (§4.11).
  (T-SCN-10 reserved: verification of a HORIZONTAL mirror declaration on an odd
   row count. In axial, after the T-SCN-05 conversion, that map is
       mu(q, r) = (q + r - (H-1)/2,  H-1-r)
   with the ODD row count as the precondition — (H-1)/2 is an integer exactly
   when H is odd, mirroring rot180's even-H precondition, and the two are
   therefore mutually exclusive on one map. It is a true isometry, not an index
   permutation: it sends (dq, dr) to (dq+dr, -dr), which permutes the three
   terms of the axial metric and leaves the distance unchanged. Blocked on Q26;
   no gate is written until the schema admits the value.)
```

### Pair 7 — §4.7 open-questions preamble

**OLD**

```
**Open questions (Director rulings owed).** Every gap found while writing the
§4.7 gates (Q1–Q10), the stage-2 additions (Q11–Q13), the rules- and
scenario-side rulings folded in here (Q14–Q20), the two gaps found while
gating §2.13.1's opening-capture invariant (Q21–Q22), the milestone
contradiction the document knowingly carries (Q23), and the two raised by the
§2.13 symmetry correction (Q24–Q25) — so that each question
carries exactly one ID across the whole document.
```

**NEW**

```
**Open questions (Director rulings owed).** Every gap found while writing the
§4.7 gates (Q1–Q10), the stage-2 additions (Q11–Q13), the rules- and
scenario-side rulings folded in here (Q14–Q20), the two gaps found while
gating §2.13.1's opening-capture invariant (Q21–Q22), the milestone
contradiction the document knowingly carries (Q23), the two raised by the
§2.13 symmetry correction (Q24–Q25), and the one raised by correcting that
correction (Q26) — so that each question
carries exactly one ID across the whole document.
```

### Pair 8 — new Q26 row

Appended after Q25, the current last row. The OLD block is the Q25 row exactly
as it stands; it is reproduced unchanged so the insertion point is unambiguous.
Q24's row is `scenario-designer`'s in this run and is not touched here — Q26
cross-references it instead.

**OLD**

```
| **Q25** | What a `rot180` declaration binds. §2.13.1 says declared symmetry is machine-verified but never says over *what*. Terrain only? Terrain + ownership + placements — the reading both stretch maps are actually drawn to (§2.13.5 "every one of those is a ρ-pair"; §2.13.6 "East is the exact ρ-image of West")? And does it bind `guidedOpening`, so the two seats' lanes must themselves be ρ-images? | T-SCN-09's assertion set; and T-SCN-08's fixture (b), whose equal 4 / 4 is a *theorem* if `guidedOpening` is bound and only a *measurement* if it is not | Terrain + ownership (sides exchanged) + placements (sides exchanged), as gated in T-SCN-09. `guidedOpening` is **not** bound: §2.13.1 requires each seat's lane to be its own neutral within 6 MP, never that the two be images of each other, so a `rot180` map may legitimately name non-image lanes and report a split. Costless either way today — both stretch maps satisfy the *stronger* reading as drawn (*Longwater*: ρ(1,2) = (11,5) and ρ(4,1) = (8,6); *Causeway*: ρ(1,2) = (7,5) and ρ(3,2) = (5,5)), so ruling `guidedOpening` in would fail no shipped map, and ruling terrain-only would merely loosen T-SCN-09. |
```

**NEW**

```
| **Q25** | What a `rot180` declaration binds. §2.13.1 says declared symmetry is machine-verified but never says over *what*. Terrain only? Terrain + ownership + placements — the reading both stretch maps are actually drawn to (§2.13.5 "every one of those is a ρ-pair"; §2.13.6 "East is the exact ρ-image of West")? And does it bind `guidedOpening`, so the two seats' lanes must themselves be ρ-images? | T-SCN-09's assertion set; and T-SCN-08's fixture (b), whose equal 4 / 4 is a *theorem* if `guidedOpening` is bound and only a *measurement* if it is not | Terrain + ownership (sides exchanged) + placements (sides exchanged), as gated in T-SCN-09. `guidedOpening` is **not** bound: §2.13.1 requires each seat's lane to be its own neutral within 6 MP, never that the two be images of each other, so a `rot180` map may legitimately name non-image lanes and report a split. Costless either way today — both stretch maps satisfy the *stronger* reading as drawn (*Longwater*: ρ(1,2) = (11,5) and ρ(4,1) = (8,6); *Causeway*: ρ(1,2) = (7,5) and ρ(3,2) = (5,5)), so ruling `guidedOpening` in would fail no shipped map, and ruling terrain-only would merely loosen T-SCN-09. |
| **Q26** | Is a **horizontal** mirror declarable? Q24 narrowed the enum to `rot180 \| none` partly on the ground that `mirror` is a value the validator could never legally accept. That holds for the **vertical** axis at every dimension, but not for the horizontal one: μ(c, r) = (c, H−1−r) is a genuine isometry of an odd-r rectangle whenever the **row count is odd** — H−1 is then even, so r and H−1−r share a parity, the offset is preserved and the column is unchanged. *Ferrum Crossing* is 11 × **9** and carries that axis geometrically (§2.13.1). So Q24's enum survives, but as a **scope** decision, not an impossibility. Add `mirrorH` with an odd-row-count precondition — the exact counterpart of `rot180`'s even-row-count one — or keep the enum at two values and accept that a true horizontal mirror is undeclarable? | Stub 7's `symmetry` field (§4.7); the reserved **T-SCN-10**; nothing else — no gate asserts anything about a value the schema does not admit, and no §2.13 map is drawn to a horizontal mirror | The enum stays `rot180 \| none` and T-SCN-10 stays unwritten: adding a value to a REQUIRED enum moves every scenario's hash, and no shipped map needs it — *Ferrum Crossing* declares `none` because its terrain is asymmetric, and both stretch maps are even-H `rot180`. The conservative reading is the narrow one, so a later ruling only ever *widens* the accepted set and *adds* an assertion; nothing that passes today would start failing. The cost of leaving it narrow, stated plainly: an author who genuinely draws a horizontal mirror on an odd-H map must declare `none`, and `none` asserts nothing — a verifiable property is silently discarded rather than an authoring error caught, which is the opposite of the failure mode Q24 was choosing between. Note the two are never in competition: `rot180` needs even H, a horizontal mirror needs odd H, and their composition would be the vertical mirror that never exists, so at most one non-`none` value is well-formed on any given map. |
```

---

## Build order

Unchanged. Item 1 adds no dependency and Item 2 adds no work; the affected row
is reproduced for completeness and moves in no column.

| # | System (ledger row) | Depends on | Headless? | Acceptance test IDs |
|---|---|---|---|---|
| 7 | Scenario file & validator (Stub 7) | 1, 2 for the structural half (T-SCN-01..03, 05, 07, 09); **3 for the priced half** — T-SCN-04, 06, 08 all cost a path | Yes; MCP tool wraps it in-editor, manual fallback stands | T-SCN-01..09 (**T-SCN-10 reserved, blocked on Q26, not counted**) |

T-SCN-10 is deliberately *not* added to §4.11's acceptance column: a reserved
ID that asserts nothing must not make a ledger row look larger than it is, and
T-MOVE-07 sets that precedent under row 3. Pair 6 puts it only inside the stub,
where the derivation lives.

---

## Change requests

| Existing § | Current text | Proposed change | Why |
|---|---|---|---|
| §4.7 Stub 7, `symmetry` | "`mirror` is not a value, because no odd-r rectangle has a mirror axis at any dimension" | Pair 5 — vertical/horizontal qualified; the enum re-justified as scope, with the 11 × 9 counterexample and the mutual-exclusivity fact | The unqualified claim is false: μ(c, r) = (c, H−1−r) is an isometry on every odd row count, and the shipped map has one |
| §4.7, T-SCN-09 | (ends at "Structural: no pathing...") | Pair 6 — reserved T-SCN-10 note | The horizontal case has a derivation but no ruling; T-MOVE-07's form records exactly that state without asserting it |
| §4.7 register | Q1–Q25, ending at Q25 | Pairs 4, 7, 8 — extent sentences and the Q26 row | A rule gap found while writing the gate, filed rather than assumed |
| §4.6 table A | "Cost per task ~$0.70 … 210 tasks … **≈ 75M tokens · ≈ $180**, + ~15% Opus escalation → **≈ $225**" | Pair 1 — Sonnet base $145, Opus escalation surfaced as a named +$33 line, subtotal ≈ 72M · $178 | 210 × $0.69 = $145, not $180; the $33 difference *is* the escalation, already inside the subtotal and then charged again. $225 follows from nothing — 15% of $180 is $207 |
| §4.6 table B | "~80k tokens", "~16M tokens", "~$60 (Sonnet 5)" | Pair 2 — 88k, 17.6M, and $37 introductory / $56 standard, each labelled by rate | 20 × 4.4k = 88k, not 80k; $60 is the standard-rate figure quoted in an introductory-rate table |
| §4.6 headline | "~90M tokens, roughly $200–$300" | Pair 3 — 90M confirmed; band restated as $178 / $197–$215, with $290 derived as the 1.5×-overrun ceiling | The token figure is right; the cost band carried table A's double-count, and its top end had no derivation |

None of these changes an API rate. Every figure in pairs 1–3 is arithmetic on
the rates §4.6 already cites as verified against published pricing on
23 Jul 2026.

---

## Open questions for the Director

**Q26 — is a horizontal mirror declarable?** Filed in full as pair 8; the next
free ID, the register having run Q1–Q25. It is the only rule gap this run
produced. I have deliberately **not** ruled Q24: its proposed `rot180 | none`
enum survives the correction intact, and the only thing that changes is why —
scope rather than impossibility — plus the failure mode that follows from it.
Q26 is the question Q24 can no longer answer for itself.

**Not a Q, and blocking no gate: one cost-model assumption made explicit.**
Pair 1 pins that Opus escalation *substitutes* for Sonnet on ~15% of tasks
rather than running in addition to it. I adopted that reading because it
reproduces §4.6's own $180 subtotal to the dollar, which is evidence it was
intended, and pair 1 states the alternative and its ≈ $200 subtotal in the
table itself. If the Director prefers the other reading, one line moves and no
gate is affected. It is not in the Q register because that register is for
rulings that block a test gate, and this blocks none.

---

## Handoffs

- **`scenario-designer` — a possible fifth site.** §2.13.6's Symmetry row reads
  "Rotation is not a preference here but the only symmetry an odd-r rectangle
  has (§2.13.1)". Read as scoped to that map it is **true**: *The Causeway* is
  9 × **8**, and on an even row count `rot180` genuinely is the only non-trivial
  symmetry — the vertical mirror never exists and the horizontal one needs odd
  H. Only the generalising phrase "an odd-r rectangle" is loose. It is in
  §2.13, so it is theirs to keep or qualify; I flag it because the Director's
  list of four sites did not include it.
- **`scenario-designer` — the fact-1 replacement wording.** If §2.13.1's fact 1
  is restated as a vertical-axis claim plus the horizontal exception, the two
  results are complementary preconditions (even H → `rot180`, odd H → mirror,
  never both), which is a cleaner pair of facts than the current two and is
  what pair 5 and Q26 both cite. Their wording governs; pair 5 references
  §2.13.1 for the vertical derivation only, so it stays correct under any
  restatement that keeps that derivation.
- **`rules-designer` / `ux-onboarding-designer`** — nothing. Neither item
  touches a rule, a number a player sees, or a screen.
- **Director** — Q26 and the pair-1 cost-model reading are the only two
  decisions here; everything else is a correction with a derivation attached.

---

## Grounding

| Claim | Backed by |
|---|---|
| Vertical mirror never exists on an odd-r rectangle | §2.13.1's own derivation (row centres differ by ½ hex at every W) — unchanged and reused, not re-derived |
| Horizontal mirror exists exactly when H is odd | Derived here: μ(c, r) = (c, H−1−r); H−1 even ⟹ r and H−1−r share parity ⟹ offset preserved, column unchanged |
| μ in axial is (q + r − (H−1)/2, H−1−r) | Derived from §4.7's own odd-r → axial conversion `q = col − (row − (row & 1)) / 2` (Shared conventions, gated by T-SCN-05) |
| μ is an isometry | The axial metric §4.7 Shared conventions states, `(|dq| + |dr| + |dq+dr|)/2`: μ sends (dq, dr) → (dq+dr, −dr), permuting the three terms |
| 11 × 9 *Ferrum Crossing* is a live counterexample | §2.13.2 Dimensions "11 × 9 = 99 hexes"; §2.13.7 scenario-set summary. Worked: offset (0,0) ↔ (0,8), (10,1) ↔ (10,7) |
| `rot180` still needs even H | §2.13.1 fact 2 and T-SCN-09's precondition clause — untouched by this correction |
| At most one non-`none` value per map | The two preconditions are complementary and their composition is the vertical mirror, which never exists |
| T-SCN-09 needs no horizontal case | T-SCN-09's own text: it is quantified on the declared value; `none` asserts nothing, `rot180` asserts ρ under an even-H precondition |
| T-SCN-08's fixtures unaffected | T-SCN-08 fixtures (a) 9 × 8 and (b) 13 × 8 both even-H `rot180`; (c) is synthetic |
| Reserved-ID form | T-MOVE-07 under §4.7 Stub 3 — "reserved … blocked on the Q2 ruling; no gate is written until the rule exists" |
| Sonnet per-task $0.69 | §4.6 published rates ($2/$10, $0.20/M cache read, verified 23 Jul 2026) applied to §4.6's own 300k ⅔-cached + 45k split |
| Opus per-task $1.73 | Same split at §4.6's Opus 4.8 rates ($5/$25, $0.50/M cache read) |
| The $33 gap **is** the escalation | 31.5 × ($1.725 − $0.69) = $32.6; $144.9 + $32.6 = $177.5, reproducing §4.6's own $180 |
| $225 follows from nothing | 15% of $180 is $207; no stated base × any stated percentage gives $225 |
| Haiku per-turn $0.0047 | §4.6 Haiku 4.5 rates ($1/$5, $0.10/M cache read) on §4.6's own 2.5k/1.5k/0.4k split — the one part-B figure that was already right |
| The `~$60` Sonnet figure is a standard-rate number | $3/$15 (the reversion rate §4.6 itself names) on the same volume gives $56; the introductory $2/$10 gives $37 |
| ~90M token headline survives | 72.45M + 17.6M = 90.05M |
| 1.5× overrun ≈ $290 | 315 × $0.69 + 47.25 × $1.035 = $266.3, + $19 Haiku runtime |
| Register runs Q1–Q25, so Q26 is next free | §4.7 open-questions table, last row Q25; §4.7 preamble "Q1–Q25" |
