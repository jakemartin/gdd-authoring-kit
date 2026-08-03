> ## ✅ APPLIED ADDENDUM — DO NOT RE-APPLY
>
> All eleven pairs of this stage were merged into the master GDD on 2026-08-03,
> **together with** the other two files of round `row5-flags`:
> `sections/rules_row5-act-order.md` (2 pairs), `sections/tech_row5-act-order.md`
> (1 pair) and `sections/ux_row5-act-order.md` (8 pairs), applied in that order.
> Master md5 `7dc635b4f06589f89b46e2fa1b7ad86b` → `9742f695f71d625763d9a3eeef21e70b`.
>
> Gate: run `row5-flags-3`, **PASS**, 0 violations, after `row5-flags-1`
> (BLOCK, 4 — two on `rules`, one on `tech`, one on `ux`) and `row5-flags-2`
> (BLOCK, 1 — `ux` alone; `rules` and `tech` both PASS at 0 there and were not
> touched again).
>
> **This file applied second. Its single pair is a replacement — no anchor is
> retained.** Post-check on the merged master: its NEW present exactly once, its OLD
> **zero** times. This file is **not safe to apply twice**.
>
> `T-TURN-01` now carries five lettered checks, the fifth being the flag-clear
> moment. **No acceptance ID was minted or retired**, so §4.5's counts do not move
> at this merge and **no ledger row flips**. `T-TURN-10` remains **WRITTEN,
> UNBLOCKED, ASSERTING and NOT GREEN** — the code satisfying it does not exist yet.
>
> **Still owed, deliberately and not missed:** §4.7 Spec Stub 8's per-unit snapshot
> field `hasActed`, which carries two distinct open requests — this file's, for a
> second rules flag, and `ux-onboarding-designer`'s, for a field the UI's DONE set
> can be derived from. The gate ruled they must be answered in one edit.

# Technical design — row-5 act-order addendum (tech-director)

## Placement

An OLD/NEW addendum against `source/gdd.md` @ md5 `7dc635b4f06589f89b46e2fa1b7ad86b`.

**One pair: §4.7 Spec Stub 5's `T-TURN-01` invariant text.** It is the only site
in §4 that states an ordering between a unit's move and its act, and it is where
the Director's flag-clearing ruling of 2026-08-03 is written.

Stub 5's **Inputs** line carries no pair. It names a count of flags — `per-unit
move and act flags — TWO flags per unit, not one (T-TURN-01)` — and states no
sequence, so no ruling this round reaches it. Stub 5's **Transition** line
carries no pair either; the reason is in Grounding.

No pair is written against §2.1, §3, §4.5, §4.7 Stub 8 or §4.11. No ledger row
moves, and no acceptance ID is minted or retired.

---

## Pair 1 — §4.7 Spec Stub 5, `T-TURN-01` (replacement)

**OLD**

```
  T-TURN-01  strict alternation; each unit carries TWO independent flags in its
             own turn and may move at most once AND act at most once, per
             §2.1's select → move → act sequence — moving never consumes the
             act, so a unit that has moved is still a legal attacker that turn
             — and the owner takes its units in any order it chooses (§2.1).
             The gate asserts that a move-then-attack by one unit COMPLETES,
             and that a second move, or a second act, by that unit is refused
```

**NEW**

```
  T-TURN-01  strict alternation; each unit carries TWO INDEPENDENT flags in
             its own turn — one for its move, one for its act — and may
             move at most once AND act at most once, IN EITHER ORDER
             (Director ruling, 2026-08-03). Moving never consumes the act,
             and acting never consumes the move: a unit that has moved is
             still a legal attacker that turn, and a unit that has attacked
             may still move that turn. The per-unit sequence is §2.1's to
             state; this gate asserts the two flags and reads no ordering
             constraint into them. The owner takes its units in any order
             it chooses (§2.1). The gate asserts: (a) a move-then-attack
             by one unit COMPLETES; (b) an attack-then-move by the same
             unit COMPLETES, leaving both of that unit's flags spent
             exactly as (a) leaves them — the two orders are NOT
             state-equivalent, since the two attacks are made from
             different hexes, so the assertion is on the flags and not on
             a state match; (c) a second move, or a second act, is
             REFUSED whichever of the two the unit spent first; (d) a
             refused command changes nothing (§4.9) — it sets neither
             flag and moves no unit; and (e) BOTH flags clear at the
             start of the owner's turn — the same moment T-TURN-10's
             per-factory build allowance renews — so a unit that spent
             both last turn moves and acts again on this one
```

The assertion list is written as five lettered checks because the rebuild's gate
has to run five distinct sequences. Two guards ride in it that a gate author
would otherwise have to guess: (b) asserts the **flags**, not a state match,
because attacking before moving and attacking after moving are attacks from
different hexes; and (d) is §4.9's existing *an invalid command returns a
rejection reason and changes nothing*, made assertable per-flag.

The text names **Move** and **Attack** for the two completion checks, which is
what the OLD named. Which further commands set the act flag is not stated here
and no check above turns on it.

---

## Anchor and overlap checks

- Pair 1's OLD was grepped against `source/gdd.md` as a single multiline pattern
  and matched **exactly once**. Every amendment since has changed the NEW only,
  so the anchor is the one already verified.
- **Classification by substring test:** pair 1's NEW does **not** contain its OLD
  — the OLD's fragment `at most once, per` appears nowhere in the NEW — so this
  pair is a **replacement**. **1 replacement, 0 insertions.**
- **No overlap check is needed.** One pair, one contiguous region.

## Change requests

| Existing § | Current text | Proposed change | Why |
|---|---|---|---|
| §4.7 Spec Stub 8, snapshot per-unit field list | `per-unit  {id, side, unitId, hex, hp, hpMax, isFlag, hasActed, captureProgress}` | Add a second flag field beside `hasActed` | **Re-filed, still open from the row-5 rulings addendum, and sharpened by pair 1:** *acted-but-not-moved* is now a reachable unit state, and one bit cannot report it in either direction. Row 8's to write when it is built. **Overlap worth naming:** `ux-onboarding-designer` has filed a second, distinct request against this same field, so the two have to be resolved in one edit or the field is edited twice. The §2.11.1 `DONE` bit is **not** the field this request asks for — under the *Wait* ruling it is the state machine's own per-unit bit, and Stub 8's snapshot carries only what the rules module produces. |

**The request against §2.1's core-loop line is withdrawn.** It asked §2.1 to stop
constraining the two flags; `rules-designer` is writing §2.1 in this same stage,
so it has nothing left to ask for.

## Open questions for the Director

**None outstanding.** Both questions this file filed were ruled on 2026-08-03.

1. *At what moment do the two flags clear?* — **Ruled: the start of the owner's
   turn**, the same moment `T-TURN-10`'s allowance renews. Written into pair 1 as
   check (e).
2. *What does Wait do to the flags, and is it a command?* — **Ruled: UI-only.**
   `DONE` is §2.11.1's own per-unit bit, distinct from the act flag; the rules
   module gains no pass or wait command and refuses nothing new. No pair is
   written for it. Its one consequence in §4 is recorded in the Stub 8 change
   request above.

## Handoffs

- **`ux-onboarding-designer` (§2.11).** The sites that key a unit's remaining
  availability to a single *acted* notion, all in your file this round and none
  paired by me: §2.11.1's selection state machine and its `own unacted unit`
  entry state (`IDLE ──LMB on own unacted unit──▶ SELECTED`); its three `unit
  DONE` transitions; the **Tab** row, *Cycle to the next unit that has not
  acted*; the **Enter** row's confirm string, `3 units have not acted. End
  turn?`; §2.11.2's persistent-element list, *unacted-unit pips*; its
  element-audit row *Unacted pip on own units | Which units still have a move*;
  and its hovered-unit panel field, `` `has acted` flag ``. The UI-restriction
  note, the new `SELECTED → attack` transition and the `DONE` bit are all yours;
  I have written no pair in §2.11.
- **`ux-onboarding-designer` (§4.7 Stub 8).** Two requests now sit on the same
  `hasActed` field, named in the change-request table above.
- **`rules-designer` (§2.1).** §2.1 is written in full in this stage and carries
  nothing forward. Pair 1 reprises none of its wording, so nothing in this file
  goes stale if that line moves again.
- **`rules-designer` (§2.7).** The build-limit boundary sentence is deferred out
  of this stage. Check (e) cites `T-TURN-10`'s already-merged renewal sentence
  and does not depend on that deferral resolving.
- **`rules-designer` (§2.8).** §2.8's alias-map preamble reads `T-TURN-01..10`
  and is unaffected: pair 1 changes `T-TURN-01`'s text, not the suite's extent,
  and mints no ID.

## Grounding

- **The either-order ruling** — Director, 2026-08-03: the two per-unit flags are
  truly independent; a unit may move at most once and act at most once in its own
  turn, in either order; attack-then-move is legal in the rules module exactly as
  move-then-attack is.
- **Check (e)'s ruling** — Director, 2026-08-03: both flags clear at the start of
  the owner's turn, the same moment `T-TURN-10`'s allowance renews. The moment was
  named nowhere in the document before this pair.
- **How §2.1 is cited** — by what it states, not by reprising how it states it.
  §2.1's core-loop line is being written in this same stage; a reprise of it here
  would need re-pairing every time that line moves. Pair 1 therefore leaves the
  per-unit sequence to §2.1 and asserts the two flags.
- **Why (e) is in `T-TURN-01`, and not in the Transition line or beside
  `T-TURN-10`.** `T-TURN-01` owns the two flags, and *at most once in its own
  turn* is not assertable until the boundary that resets them is named — a module
  that never clears either flag passes (a) through (d) and fails no check. The
  Transition line is under no acceptance ID, so a rule written there is gated by
  nothing; `T-TURN-10` is the per-factory build limit, and a per-unit rule filed
  there would be asserted by an ID whose subject is a factory.
- **Why it stays two statements rather than one.** The unit flags and the
  per-factory build record are different objects gated by different IDs, and the
  ID is the assertable unit — one shared sentence would sit under one ID and be
  relied on by the other. Check (e) cites `T-TURN-10`'s already-merged renewal
  sentence rather than adding a proposition, so a rebuild cannot implement two
  moments and `T-TURN-10`'s text is left untouched.
- **Why the Transition line carries no pair.** It reads `I-GO-U-GO alternation
  (§2.1); win/loss/draw evaluation (§2.8); start-of-turn repair application
  (§2.7)`, and already omits `T-TURN-10`'s renewal, income and the capture tick.
  Adding one of five omitted items would not make it a list of what that moment
  does.
- **Verdict on the attack-without-moving ruling: check (b) already covers the
  rules half, and nothing was added for it.** (b)'s first operation *is* an attack
  by a unit that has not moved, so (b) cannot pass unless that attack is legal;
  and (b) cannot pass unless the attack left the move flag unspent, since (c)
  refuses a move whose flag is already spent. The prose above (b) states the same
  rule directly — *acting never consumes the move ... a unit that has attacked may
  still move that turn*. The unit retiring afterwards without moving is the `DONE`
  bit, which the same ruling puts in §2.11.1 and not in the rules module.
  `T-MOVE-03` is not cited or altered anywhere in this file.
- **What pair 1 removes** — the OLD anchor's `per §2.1's select → move → act
  sequence`, which anchors the flags to an order the ruling denies, and its
  single-ordering assertion `the gate asserts that a move-then-attack by one unit
  COMPLETES`. Both quotations are of §4.7's own bytes, not §2.1's.
- **What pair 1 keeps** — `strict alternation`, the two flags, `moving never
  consumes the act`, the free unit order, and the refusal of a second move or a
  second act. Each was already in the OLD.
- **(d)'s citation** — §4.9, presentation bridge: *An invalid command returns a
  rejection reason and changes nothing.*
- **Substring classification, as a falsifiable claim about the bytes above** —
  pair 1's NEW does not contain pair 1's OLD; the OLD's fragment `at most once,
  per` occurs zero times in the NEW. Pair 1 is a **replacement**. There is no
  insertion in this file.
- **Sites this addendum leaves alone, named rather than absorbed.** §3's row-5
  evidence sentence and its nine-rows paragraph, §4.5's risk cell, and §4.11's
  ledger row and preamble each record `T-TURN-01..09, 9/9` at `ad77b13` as the
  dated record of that commit. No pair here reaches any of them; the standing
  ruling reserves row 5's restatement to the rebuild's own §3 addendum. Row 5's
  shipped code at `ad77b13` implements one act flag, and this addendum asserts
  nothing about what that code does.
- **No count moves** — pair 1 mints no acceptance ID and retires none, so no
  written, green or unclosed figure in §4.5 is paired.
