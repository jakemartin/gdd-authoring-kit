> ## ✅ APPLIED ADDENDUM — DO NOT RE-APPLY
>
> All six pairs were merged into the master GDD on 2026-08-03, **together with**
> `sections/tech_row5-rulings-t-turn-10.md` (13 pairs). This file applied first.
> Master md5 `ca397f4f2eca447b451fca2ca2393092` →
> `95655234f1d18805e69d4abea942bcf5` → `7dc635b4f06589f89b46e2fa1b7ad86b`.
>
> Gate: run `row5-rulings-3`, **PASS**, 0 violations, after `row5-rulings-1`
> (this file PASS, 0) and `row5-rulings-2` (this file BLOCK, 1 — a false locator
> in Grounding placing line 1558 in §3 when it is §4.5; fixed by **deleting** the
> enumeration, not relabelling it).
>
> **Pair 6 is an insertion — its OLD anchor is retained deliberately.** Its NEW
> opens with its OLD verbatim and appends. Post-check on the merged master: every
> NEW present exactly once; pair 6's OLD present **once**, the other five **zero**
> times. This file is **not safe to apply twice**.
>
> **`kb/rules.md` WAS re-synced** — the first time since row 5. §2 changed across
> this merge (98,195 → 98,953 chars, compared as strings). The §2.7 build bullet's
> slot-vs-per-turn distinction was mirrored into `kb/rules.md`; `pipeline/run.py`
> reproduces **3 still-failing** critic violations both before and after, verified
> by a control run against the pre-edit KB, so none is attributable to this merge.
>
> **No pair for §2.1** — its `select → move → act` pseudocode already stated the
> ruling correctly. A correct passage getting no pair is the outcome, not a gap.

# Rules — row-5 rulings + T-CAP-05 addendum (rules-designer)

## Placement

Six OLD/NEW pairs against `source/gdd.md` at md5 `ca397f4f2eca447b451fca2ca2393092`.

| Pair | Lands in | Kind |
|---|---|---|
| 1 | §2.7, Build & spawn bullet | replacement |
| 2 | §2.8, invariant-list caption | replacement |
| 3 | §2.8, alias-map caption | replacement |
| 4 | §2.8, alias-map T-CAP-05 row | replacement |
| 5 | §2.8, the T-CAP-05 exception paragraph | replacement |
| 6 | §2.13.3, Economy online bullet | insertion |

Each OLD was grepped against `source/gdd.md` and matches **exactly once**.
Classification is by substring test on the bytes below: pair 6's NEW contains
its OLD verbatim as a prefix, so its anchor survives by design; pairs 1–5 do
not, so they are replacements.

Pair 2 carries two changes to one sentence: the stale `T-TURN-` range and the
caption's "one row names none".

**§2.1 receives no pair.** Its fenced pseudocode already states C2's rule:
`for each of your units (any order): select → move (within range,
terrain-costed) → act (attack / capture / build) → done`. One pass per unit
through a move step and an act step is a unit moving once and acting once.
A grep for `at most once|acts once|acted this turn|once per own turn|move or
act` across the whole document returns a single hit, at §4.7's `T-TURN-01`
line. §2 does not state the one-flag rule. A correct passage gets no pair.

## Pair 1 — §2.7, the per-turn limit is not the waiting-build slot

**OLD**
```
  free hex; if the factory is boxed in, the build waits.** A waiting build
  **holds that factory's slot until it spawns**, and its Fame is **committed
  when the build is queued, not when the unit appears, and is not
  refundable** (Q8, §4.7). The **player cannot currently reach the waiting
```

**NEW**
```
  free hex; if the factory is boxed in, the build waits.** A waiting build
  **holds that factory's slot until it spawns**, and its Fame is **committed
  when the build is queued, not when the unit appears, and is not
  refundable** (Q8, §4.7). The slot and the per-turn limit are **two rules,
  not one**: the slot is held only while a build waits and clears the moment
  the unit spawns, while the per-turn limit binds for the rest of that turn
  either way — a factory whose build spawns at once has still spent its
  build for the turn. The **player cannot currently reach the waiting
```

## Pair 2 — §2.8, invariant-list caption: ID range and the "names none" clause

**OLD**
```
*Invariants. `T-CAP-01..08` is §2.8's own numbering for the procedure §4.7
Spec Stub 5 gates as `T-TURN-01..09`, so there is one suite, not two. The map
below names, for each invariant, the ID or IDs that gate it; one row names
none.*
```

**NEW**
```
*Invariants. `T-CAP-01..08` is §2.8's own numbering for the procedure §4.7
Spec Stub 5 gates within `T-TURN-01..10`, so there is one suite, not two. The
map below names, for each invariant, the ID or IDs that gate it; one row names
a gate outside the `T-TURN-` numbering.*
```

## Pair 3 — §2.8, alias-map caption

**OLD**
```
*Alias map — the ID or IDs that gate each invariant above; one row names none:*
```

**NEW**
```
*Alias map — the ID or IDs that gate each invariant above; one row names a
gate outside the `T-TURN-` numbering:*
```

## Pair 4 — §2.8, alias-map T-CAP-05 row

**OLD**
```
| T-CAP-05 | **nothing** | see below |
```

**NEW**
```
| T-CAP-05 | **GATE-CAP-PARTIAL** | not a `T-TURN-` ID; see below |
```

## Pair 5 — §2.8, the T-CAP-05 exception paragraph

**OLD**
```
**T-CAP-05 is the exception.** No `T-TURN-` ID asserts it. It is discharged
*structurally* by T-FAME-05 and T-FAME-06 — an objective's owner does not
change until the capture completes, and the tally counts owners — but **no
gate asserts it end to end, and it appears in no acceptance set.**
```

**NEW**
```
**T-CAP-05 is the exception.** No `T-TURN-` ID asserts it. It is discharged
*structurally* by T-FAME-05 and T-FAME-06 — an objective's owner does not
change until the capture completes, and the tally counts owners — and it is
asserted end to end by **`GATE-CAP-PARTIAL`**, which is named in Spec Stub
8's acceptance set (§4.7). Nothing blocks that gate. **It has not run, so
T-CAP-05 is asserting and not green.**
```

## Pair 6 — §2.13.3, what "the following turn" is relative to

**OLD**
```
  closest neutral factory in ~2 turns; capture at N=1 (fixed from §2.7's
  "start N=1–2" range — Q4, §4.7) flips income the following turn.
```

**NEW**
```
  closest neutral factory in ~2 turns; capture at N=1 (fixed from §2.7's
  "start N=1–2" range — Q4, §4.7) flips income the following turn.
  "The following turn" counts the **capturing side's own turns from the turn
  ownership flips** — not from the turn its Infantry moves onto the tile,
  and not the next turn in the I-GO-U-GO alternation (§2.1), which is the
  opponent's.
```

## Grounding

- **Pair 1.** C1 puts the per-turn half in row 5 and leaves row 4 the slot,
  the spawn placement and queue-time commitment; the distinction the two
  halves rest on is already in §2.7's own words — a waiting build holds the
  slot *until it spawns*, so the slot cannot be what carries the limit
  across the rest of the turn. No module, row or ID is named in the NEW
  text. No number is stated.
- **Pair 2, the range.** `T-TURN-10` is minted this round (C4). Within §2 the
  only site carrying a `T-TURN-` range is this one; every other `T-TURN-`
  mention in §2 is a single ID, not a range. The remaining range sites are
  outside my lane and are handed off. **`gates as` becomes `gates within`**:
  `T-TURN-10` gates §2.7's per-turn build limit, not §2.8's tiebreak
  procedure, so the procedure is gated by IDs drawn from the suite rather
  than by the whole of it. The range already denoted Stub 5's suite rather
  than the procedure's own gates — the alias map below it uses only
  T-TURN-02, 03, 05, 07 and 09.
- **Pairs 2 (the "names none" clause), 3, 4.** D3. `GATE-CAP-PARTIAL` gates
  T-CAP-05 and is not a `T-TURN-` ID, so the alias column's `**nothing**` is
  false under the caption's own contract ("the ID or IDs that gate it").
  Naming the gate makes both captions' "one row names none" false, so both
  move with it.
- **Pair 5.** D1 for both halves being false, D2 for the residual true fact.
  The three states are kept apart per E: the gate asserts, nothing blocks
  it, it has not run, T-CAP-05 is not green. The paragraph does not call it
  unwritten, blocked, or pending a ruling.
- **Pair 6.** C3, plus the shipped bytes, which I read rather than assumed.
  `cpp_reference/Driver.good.cpp` runs repair, then `accrueIncome` (line
  557), then `captureTick` (line 569), before the side acts, and states the
  consequence in its own comment at lines 552–554: *"the tick runs AFTER
  income, so an objective whose capture completes at the start of turn T
  pays its new owner from T+1."* `cpp_reference/Economy.good.cpp` sets
  `turnsHeld = 1` on the first tick at which the unit is present (line 157)
  and fires `if (prog->turnsHeld >= s.captureTurns)` (line 169), so at N=1
  the flip lands on the first tick after arrival. In the capturing side's
  own turns: Infantry arrives in the action phase of turn T, ownership flips
  at the start of T+1, and the first payment to the new owner is at the
  start of T+2. Arrival → income is two own-turns; flip → income is one. The
  OLD clause *"flips income the following turn"* is therefore true on the
  flip-counted reading only, which is why the origin is anchored to the flip
  and not to arrival. The insertion states no ordering and imports no
  sequence from §2.9. "I-GO-U-GO alternation" is §2.1's phrase.
- **No pair for §2.1.** C2's rule is §2.1's existing sequence.

## Change requests

Both rows are in §2.13.3's "Economy online turn 3–4" bullet, and both follow
from pair 6's settled reading: a captured objective first pays its new owner
on the own turn *after* ownership flips, so any figure derived by counting
from the Infantry's arrival to its first income is one own-turn early.
**I have not recomputed either figure.** They are tuning numbers.

| Existing § | Current text | Proposed change | Why |
|---|---|---|---|
| §2.13.3 | `**Economy online turn 3–4.**` | Director to recheck the turn. | The bullet reaches it from "reaches its closest neutral factory in ~2 turns"; on the flip-counted reading the first income lands an own-turn later than an arrival-counted derivation gives. |
| §2.13.3 | `Income ramps 100 → ~225–250 Fame/turn` | Director to recheck the turn each step of the ramp lands on. The rate endpoints (100, ~225–250) are not challenged. | Same shift. What moves is when a step arrives, not the per-turn rate. |

## Open questions for the Director

1. **Is pair 4 a one-off or a precedent?** After it, §2.8's alias column
   holds one non-`T-TURN-` gate name, and both captions say so in the
   singular ("one row"). If a second invariant later aliases onto a `GATE-`
   name, three sites go stale at once. **This blocks** nothing this round;
   it decides whether the captions should instead be written to admit any
   number of such rows.

## Handoffs

- **`T-TURN-01`'s text — tech-director.** The document's only statement of
  the one-flag rule is `T-TURN-01  strict alternation; each unit acts at
  most once per own turn, in ...` in §4.7's Stub 5. C2/B5 make that text
  wrong. It is in tech-director's sections this round, so it gets no pair
  here. §2 needs nothing for it.
- **`T-TURN-10` — tech-director.** Pair 1 states the per-turn limit as a
  rule distinct from the slot; that is the property C4 mints `T-TURN-10`
  for. §2.7 carries no acceptance IDs anywhere in the bullet, so no pointer
  is written into it. Flagged so the minted ID's text can be checked against
  pair 1's wording rather than against the old slot-shaped reading. Pair 2
  assumes `T-TURN-10` lands in Stub 5; if it lands in Stub 4 instead, pair
  2's range change is wrong and I need to be told.
- **`T-FAME-04` — tech-director.** C4 drops its per-turn clause. B4 says its
  test does not cover a second build in the same turn, so pair 1's
  distinction is the wording the amended ID should not re-absorb.
- **`T-TURN-01..09` outside §2 — tech-director / Director.** The range also
  appears at §4.7 Stub 5's `Acceptance:` line and §4.11's row 5 cell, both
  tech-director's, and at §3 ledger sites, which F puts out of scope this
  round. No pair written for any of them.
- **`kb/rules.md` — orchestrator.** §2.7, §2.8 and §2.13.3 change here, so
  the parse of §2 drifts on merge (F).
