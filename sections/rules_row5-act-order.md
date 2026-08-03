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
> **This file applied first. Both pairs are replacements — no anchor is retained.**
> Post-check on the merged master: each NEW present exactly once, each OLD **zero**
> times. This file is **not safe to apply twice**.
>
> Pair 2 was written at `row5-flags-2` in place of an open question: the Director's
> ruling that the rules module has **no current unit** answered it, so it is written
> rather than asked. Both of this file's open questions were withdrawn for that
> reason — the second by the ruling that §2.1 owes no economy or build step.

# Rules — row5-flags addendum (rules-designer)

## Placement

An OLD/NEW addendum against `source/gdd.md` @ md5 `7dc635b4f06589f89b46e2fa1b7ad86b`.
**Two pairs**, both inside **§2.1's fenced core-loop block**, which holds **six
body lines** (**eight** including both ``` delimiters):

- **Pair 1** — the per-unit body line beginning `select →`, five leading spaces,
  the **third body line** of the fence.
- **Pair 2** — the loop header `for each of your units (any order):`, two leading
  spaces, the **second body line**.

Nothing else in §2.1 is touched: not `Player turn:`, not `end turn`, not
`Opponent turn: same, driven by AI`, not the `repeat until …` line, and not the
sentence below the fence (`I-GO-U-GO alternation. No simultaneous resolution.`).
What I concluded about each of them is under **Anchor and survey** below.

Not touched, and each belongs to someone writing in this same sitting: §2.11.1's
state machine and its `(§2.1: select → move → act → done, any unit order)`
parenthetical, §2.11.2's `has acted` displays, and §4.7 Spec Stub 5's
`T-TURN-01` text. All four are under **Handoffs**. §2.7 is not touched at all.

---

## Pair 1 — §2.1, the core-loop body line (replacement)

**OLD**

```
     select → move (within range, terrain-costed) → act (attack / capture / build) → done
```

**NEW**

```
     select → move (within range, terrain-costed) and/or act (attack), in either order → done
              (two independent flags: at most one move and at most one act per
               unit in its own turn, and neither is required — gated as
               T-TURN-01; capture and build set no act flag, §2.7)
```

Three things leave the line and one arrives. `capture` and `build` leave the act
list because neither sets a unit's act flag. The mandatory `move → act` ordering
leaves, replaced by `and/or … in either order`, which also carries the case of a
unit that attacks without having moved. What arrives is the *at most one of each*
limit, which the old line stated only by the shape of its arrows and which the
new wording would otherwise drop — without it §2.1 would read as permitting two
attacks.

## Pair 2 — §2.1, the loop header (replacement)

**OLD**

```
  for each of your units (any order):
```

**NEW**

```
  for each of your units (any order; a unit may be given its remaining command
    with other units' commands in between — the rules module has no current unit):
```

The header's `for each … :` over a body that ends `→ done` implied one visit per
unit, which is the same implicit ordering claim pair 1 removes from the arrows,
one level out. The rules module has no current unit, so the two flags may be
spent in two separate visits; `done` in the body line is reached when the owner
stops commanding that unit, not at a point the loop fixes.

---

## Anchor and survey

**Anchors.** Each was counted against `source/gdd.md`:

- Pair 1: `^     select → move` matches **once** (`rg -c`). The OLD is a superset
  of that prefix and is present, so it matches **exactly once**. Five leading
  spaces are part of the anchor.
- Pair 2: `^  for each of your units \(any order\):$` matches **exactly once**,
  and the looser `for each of your units` also matches exactly once, so no
  near-miss exists. Two leading spaces are part of the anchor.

**Overlap.** The two anchors are adjacent body lines of one fence, disjoint —
neither OLD is a substring of the other, and neither NEW reaches into the other's
line. They are numbered in the order they were written, not in file order: pair 2
is the second body line and precedes pair 1, which is the third. Applying them in
either order gives the same bytes.

**Classification by substring test on the bytes above:**

- **Pair 1** — NEW does **not** contain OLD: after the shared indent both read
  `select → move (within range, terrain-costed) `, then OLD reads `→ act` and NEW
  reads `and/or act`. **Replacement.**
- **Pair 2** — NEW does **not** contain OLD: both read `  for each of your units
  (any order`, then OLD reads `):` and NEW reads `; a unit may be given`.
  **Replacement.**

**Two pairs, two replacements, zero insertions.**

**The property surveyed:** every site that states or implies an ordering between
a unit's move and its act, that names what a unit's act may be, or that states
when a unit stops being available for further commands in its own turn. Sites
found, and their disposition:

| Site | Disposition |
|---|---|
| §2.1, the body line | **Falsified. Pair 1.** |
| §2.1, `for each of your units (any order):` | **Falsified** — the loop shape implied one visit per unit, and there is no current unit in the rules module. **Pair 2.** |
| §2.1, the other four fence lines and the sentence below the fence | Not falsified. None states an order between move and act, names an act, or says when a unit stops taking commands. |
| §2.9, AI unit phase, *"if an enemy is within reach after moving, attack"* | Not falsified. It states the routine the AI runs, not a constraint on what is legal; move-then-attack stays one of the two legal orders. |
| §2.11.1's machine, vocabulary sentence and input table | Falsified in part, and **not mine** — rulings 5 and 7 make the narrowing, including the retirement at the act, UI-only. Handoff 1. |
| §2.11.2 `has acted` / unacted pips; §2.11.6-D's *"unacted pip"* | One displayed bit against two rules-layer flags. Handoff 3; the ask is already filed by `tech-director` and I do not duplicate it. |
| §4.7 Stub 5, `T-TURN-01` | Quotes the words pair 1 removes. **Not mine** — handoff 2. |
| §3's row-5 evidence paragraph, *"per-unit act flags"*; §4.7 Stub 8's `hasActed` | Already carried as `tech-director` change requests for the rebuild round. Not re-filed. |

No site outside §2.1 is falsified by these rulings and left unassigned.

## Change requests

| Existing § | Current text | Proposed change | Why |
|---|---|---|---|
| — | — | — | None. Neither pair states a number, and neither moves one. |

## Open questions for the Director

None. Both questions this file carried at run `row5-flags-1` are **withdrawn**,
each answered by a ruling that landed after they were written:

1. *Withdrawn — may a unit be returned to?* **Ruling 7** answers it: there is no
   current unit in the rules module, and a unit may be given its remaining
   command with other units' commands in between. Pair 2 writes that answer into
   the loop header instead of asking it.
2. *Withdrawn — does §2.1's block still owe a build line?* **Ruling 8** answers
   it: §2.1 owes no economy or build step and stays the per-unit loop, routing
   build to §2.7 — which is what pair 1's parenthetical already does.

## Handoffs

- **`ux-onboarding-designer` (§2.11.1).** The state-machine preamble reads
  `The core loop (§2.1: select → move → act → done, any unit order) maps to four
  UI states:`. It quotes §2.1 by the exact words pair 1 removes, so the
  quotation goes stale on merge. §2.11.1 is yours this sitting under rulings 3,
  5 and 7; I have written no pair there.
- **`tech-director` (§4.7 Spec Stub 5).** `T-TURN-01` reads `per §2.1's select →
  move → act sequence` and asserts `that a move-then-attack by one unit
  COMPLETES`. The quoted sequence is what pair 1 removes, and move-then-attack
  is now one of two permitted orders rather than the order. Your text; no pair
  from me.
- **`ux-onboarding-designer` (§2.11.2, §2.11.6-D).** The sites that show one bit
  where the rules layer holds two: §2.11.2's persistent `unacted-unit pips`, its
  info-panel `has acted` flag, the `Enter` row's `3 units have not acted. End
  turn?`, §2.11.1's `Tab` row (`Cycle to the next unit that has not acted`), and
  §2.11.6-D's `carrying its unacted pip`. Naming the sites is all this is —
  `tech-director` has already filed the Stub 8 snapshot field and handed the
  display call to you, and I am not re-filing it.

## Grounding

- **`build` and `capture` leave the act list** — ruling 1: build and capture set
  no unit act flag; building is the factory's own interaction and capture is by
  presence, and the per-turn build record is per-factory. The rules they do
  belong to are §2.7's **Build & spawn** and **Capture** bullets, which is the
  §2.7 pair 1 cites.
- **`and/or … in either order`** — ruling 2: the two flags are truly
  independent; a unit may move at most once and act at most once in its own turn,
  in either order.
- **`neither is required`** — ruling 3: a unit may attack without having moved.
  The converse half (move without acting) is already in the document as
  §2.11.1's `Wait`, and the neither half as §2.11.1's `Enter` row, which ends a
  turn with units that have not acted.
- **`at most one move and at most one act`** — ruling 2, and the phrase already
  exists in the document at §4.7 Stub 5's `T-TURN-01` (`may move at most once AND
  act at most once`). No number is introduced.
- **Pair 2's `the rules module has no current unit` and `its remaining command
  with other units' commands in between`** — ruling 7, in its own terms. The same
  ruling makes §2.11.1's retirement of the unit at the act a UI-only narrowing,
  which is why pair 2 changes §2.1 and no §2.11 text.
- **§2.1's fence gains no economy or build step** — ruling 8.
- **`gated as T-TURN-01`** — §4.7 Spec Stub 5. Cited rather than restated: its
  text is `tech-director`'s this sitting.
- **T-MOVE-03 is not cited and not restated.** Ruling 3 leaves it untouched;
  nothing in either pair makes standing still a move or makes a unit's own hex a
  destination, and §4.7's `T-MOVE-03` (`a move never ends on an occupied hex`)
  continues to own that.
- **Flag clearing is absent from both pairs on purpose** — ruling 4 assigns the
  start-of-turn clearing, and `T-TURN-10`'s allowance renewal beside it, to
  `tech-director`. Neither pair says when the flags clear, only when they are
  spent.
- **No claim about code is made anywhere above.** Row 5's shipped code at
  `ad77b13` implements one act flag, not two; the rebuild is a later round.
- **Classification** — stated as a falsifiable claim about the bytes written
  above: neither NEW contains its OLD, so both pairs are replacements.
