# Technical design — rulings F–I addendum (tech-director)

> ## ✅ APPLIED ADDENDUM — DO NOT RE-APPLY
>
> All eight pairs were merged into the master GDD on 2026-08-04, together with
> `ux_rulings-f-g.md` (3 pairs) in one 11-pair application. Master md5
> `f327f0cf6a92e53fe59fab8550558e2e` → `5075d853166d99858fd3a5a4b7dfc27c`.
>
> **All eight pairs are replacements. None is an insertion**, so no OLD anchor
> survives on the merged master. Classified by substring test over the final
> bytes. Note Pair 8 is a replacement despite its NEW opening and closing with
> its OLD's words — the addition sits *between* them, so the OLD is not a
> contiguous substring of the NEW. Every OLD was verified against the **master**
> before anything was written, each matching exactly once, and the apply refused
> to write unless all eleven did.
>
> Gate: run `rulings-f-i-3`, **PASS**, 0 violations. History: `rulings-f-i-1`
> BLOCK 1 → `-2` **PASS** 0 → `-3` **PASS** 0. The second PASS was re-run rather
> than merged because the gate **escalated without filing** at `-2`: it declined
> to relitigate a ruling but flagged that classifying `isGuidedMarked` an
> unmarked MIRROR strained Stub 8's definition. That escalation was correct and
> produced **Ruling J** — the field is **DECLARED DERIVED**. Had the `-2` PASS
> been merged, the document would have carried a field that **T-UI-05 clause (a)
> fails**, since an unmarked field must equal its named module-side value exactly
> and this one is a boolean over a hex reference. A PASS is not the same as
> correct; read what the gate says beside its verdict.
>
> The `-1` violation was a `contradiction` in Pair 5, and its shape is worth
> keeping: the new presentation-block member was given DONE's lifecycle — *clears
> when the turn does* — while §2.11.6-B scopes the guided-opening lock to beat
> 1a, which retires **inside turn 1** on the marked Infantry's move. **A member
> added beside an existing one inherits its neighbour's lifecycle by default, and
> that default is not checked by anything.**
>
> §4.5 does **not** move: 71 written / 52 green / 19 unclosed, 17 IDs in rows
> 8–10, 9 verified ledger rows; §3's uncovered count stays 9. No ID is minted.
> Row 8 stays `*pending*`, and no code implements anything this round adds.
>
> Over-90-char non-table lines: **126 before, 126 after**. `.txt` and `.pdf`
> rebuilt with the recipes control-tested earlier the same day.

## Placement
§4.4, §4.7 (Spec Stub 7, Spec Stub 8), §4.7's open-questions register (Q27),
§4.9. Exact OLD/NEW pairs against the master at md5 `f327f0cf`. Nothing in §2 is
paired.

---

### Pair 1 — Stub 7's `guidedOpening` note: the disposition it recorded

Stub 7 recorded that marked/locked stays out of the Stub-8 view-model entirely.
Ruling F places each half, so the note states where each one went.

**OLD**

```
                                   other source for the pair. The guidance layer
                                   reads this field from the loaded scenario
                                   directly — marked/locked is presentation
                                   state, not rules state, so it stays out of
                                   the Stub-8 snapshot.
```

**NEW:**

```
                                   other source for the pair. The guidance layer
                                   reads this field from the loaded scenario
                                   directly. Its two halves sit in two places
                                   (ruled 2026-08-04): MARKED is the per-unit
                                   Stub-8 snapshot field `isGuidedMarked`,
                                   DECLARED DERIVED at that stub on this
                                   field; LOCKED THIS TURN is per-unit and
                                   per-turn, owned by the guidance layer, and
                                   is a member of Stub 8's presentation block
                                   rather than of the snapshot.
```

---

### Pair 2 — Stub 8's scope paragraph: what the presentation block is

The scope paragraph defines the block as the selection machine's state. Ruling F
gives the block a second member under a second owner, so the definition names
owners member by member instead of naming one owner for the block.

**OLD**

```
         The VIEW-MODEL is the rules-produced SNAPSHOT below plus a declared
         PRESENTATION BLOCK: the per-unit state §2.11.1's SELECTION MACHINE
         owns and no rules field expresses. It is declared here rather than
         improvised in a widget because T-INT-05 (§4.9) rebuilds from the
         view-model: state in the block satisfies it, state in a widget does
         not.
```

**NEW:**

```
         The VIEW-MODEL is the rules-produced SNAPSHOT below plus a declared
         PRESENTATION BLOCK: per-unit state that no rules field expresses,
         held by owners named member by member at the block below. It is
         declared here rather than improvised in a widget because T-INT-05
         (§4.9) rebuilds from the view-model: state in the block satisfies
         it, state in a widget does not.
```

---

### Pair 3 — Stub 8's per-unit snapshot group: the *marked* field

Ruling F makes *marked* a snapshot field; Ruling J makes it DECLARED DERIVED, on
the Stub-7 scenario file's `guidedOpening.infantry`.

**OLD**

```
         per-unit  {id, side, unitId, hex, hp, hpMax, isFlag, hasMoved,
                    hasActed, captureProgress}
```

**NEW:**

```
         per-unit  {id, side, unitId, hex, hp, hpMax, isFlag, hasMoved,
                    hasActed, captureProgress, isGuidedMarked}
                    `isGuidedMarked` is DECLARED DERIVED: true exactly on the
                    placement that the Stub-7 scenario file's
                    `guidedOpening.infantry` names for that unit's seat —
                    T-SCN-02 makes a hex identify one placement — and false
                    on every other unit, computed by the module and never
                    widget-side. It is a property of the placement, not of
                    the unit's current hex, so it does not move when the unit
                    does.
```

---

### Pair 4 — Stub 8's per-side group: the three declared-derived derivations

Ruling G fixes `incomePerTurn` on turn 1. Ruling H states the other two
derivations by citing §2.8's criterion text. T-UI-05 clause (b) recomputes each,
so each needs a stated derivation to recompute.

**OLD**

```
         per-side  {fameTotal, fameCombat, objectivesHeld X of N, survivingHP,
                    incomePerTurn}
                    `fameTotal` and `fameCombat` are mirrors. The other
                    three are DECLARED DERIVED: `objectivesHeld X of N` and
                    `survivingHP` on §2.8's definitions of tiebreak criteria
                    2 and 3 — GATE-CAP-PARTIAL already gates the first's one
                    edge case, a capture in progress counting for nobody —
                    and `incomePerTurn` as §2.7's rate over that side's held
                    factories (+100 each) and towns (+25 each), computed by
                    the module so that no surface sums it widget-side
                    (T-UI-03's no-arithmetic clause).
```

**NEW:**

```
         per-side  {fameTotal, fameCombat, objectivesHeld X of N, survivingHP,
                    incomePerTurn}
                    `fameTotal` and `fameCombat` are mirrors. The other three
                    are DECLARED DERIVED, and each derivation is stated here
                    so that T-UI-05 clause (b) has one to recompute.
                    `objectivesHeld X of N` is §2.8 criterion 2 in that
                    criterion's own words: "the factories and captured towns
                    a side owns at the cap, as X of N. Ownership only: a
                    capture in progress (§2.7) counts for nobody until the
                    objective flips." X is that side's count under that text;
                    N is the same count taken over every factory and
                    capturable town the scenario supplies (§2.11.4). Citing
                    the criterion mints no rule — the criterion text is the
                    derivation. GATE-CAP-PARTIAL gates its one edge case, a
                    capture in progress counting for nobody.
                    `survivingHP` is §2.8 criterion 3 in that criterion's own
                    words: "total remaining HP of a side's units" — the sum
                    of `hp` over that side's units in the per-unit group
                    above, and likewise no new rule.
                    `incomePerTurn` is §2.7's rate over that side's held
                    factories (+100 each) and towns (+25 each), computed by
                    the module so that no surface sums it widget-side
                    (T-UI-03's no-arithmetic clause). It is the STANDING
                    rate, and that is what it reads on turn 1: the amount
                    those holdings will pay at the start of that side's turn
                    2, not the 0 that Q8(a) pays on turn 1. The field is the
                    rate the holdings carry and never the accrual of the
                    current turn.
```

---

### Pair 5 — Stub 8's presentation block: the second member and its owner

Ruling F. The block goes to two members under two owners, and each owner is
named beside its own member.

**OLD**

```
Presentation block (NOT produced by the rules module; owned by §2.11.1's
         selection machine, which is a state machine and not a widget; its
         membership is that machine's per-unit state and nothing else):
         per-unit  {done}
                    §2.11.1's DONE bit — this unit takes no further command
                    this turn. Per-turn: it clears when the owner's next turn
                    begins. It is the selection machine's only per-unit bit,
                    and so the block's sole member. It is in the view-model
                    rather than in a widget precisely so that T-INT-05 (§4.9)
                    can rebuild the screen from the view-model alone. The
                    guided opening's marked/locked state is not here: the
                    guidance layer reads it from the loaded scenario (Stub
                    7's `guidedOpening` note), and where it belongs is not
                    decided at this stub.
```

**NEW:**

```
Presentation block (NOT produced by the rules module; TWO members, each with
         its owner named beside it, and neither owner a widget):
         per-unit  {done}
                    OWNER: §2.11.1's selection machine, which is a state
                    machine and not a widget.
                    §2.11.1's DONE bit — this unit takes no further command
                    this turn. Per-turn: it clears when the owner's next turn
                    begins. It is the selection machine's only per-unit bit.
                    It is in the view-model rather than in a widget precisely
                    so that T-INT-05 (§4.9) can rebuild the screen from the
                    view-model alone.
         per-unit  {lockedThisTurn}
                    OWNER: the guidance layer, which is neither the rules
                    module nor a widget.
                    §2.11.6 turn 1a's `Locked this turn.` — this unit is not
                    selectable under the guided opening while beat 1a is
                    outstanding. It clears when 1a retires, which §2.11.6-B
                    states is when the marked Infantry's move completes.
                    Ruled 2026-08-04, which is the question this stub
                    previously left undecided; the guided opening's other
                    half, marked, is the snapshot field `isGuidedMarked`
                    above and is not in this block.
```

---

### Pair 6 — T-INT-05's statement of its own subject (§4.9)

Ruling F: T-INT-05 reaches both halves and is not narrowed. Its closing sentence
named one bit from a one-member block, so it now names its subject as the whole
view-model and both block members.

**OLD**

```
  T-INT-05  (editor, Automation) presentation statelessness: after any event
            sequence, rebuilding all widgets/actors from the current view-model
            alone — §4.7 Stub 8's snapshot plus its presentation block —
            reproduces the same displayed values (nothing lives only in a
            widget). §2.11.1's selection machine is not a widget, so its DONE
            bit satisfies this gate from the presentation block
```

**NEW:**

```
  T-INT-05  (editor, Automation) presentation statelessness: after any event
            sequence, rebuilding all widgets/actors from the current view-model
            alone — §4.7 Stub 8's snapshot plus its presentation block —
            reproduces the same displayed values (nothing lives only in a
            widget). The subject is every member of the view-model, and the
            presentation block has two: §2.11.1's selection machine is not a
            widget, so its DONE bit satisfies this gate from the block, and
            the guidance layer is not a widget either, so its `lockedThisTurn`
            bit satisfies it from the block on the same footing. The guided
            opening's other half, `isGuidedMarked`, is a snapshot field and
            satisfies this gate from there
```

---

### Pair 7 — Q27's Blocks cell

Q27's dependency cell rests on Stub 7's superseded disposition. Ruling F.

**OLD**

```
no stub or `T-` ID gates the directive strip, and Stub 7 deliberately keeps the guidance layer out of Stub 8's snapshot.
```

**NEW:**

```
no stub or `T-` ID gates the directive strip. Stub 7 kept the guidance layer out of Stub 8's view-model entirely; since 2026-08-04 it does not — *marked* is the snapshot field `isGuidedMarked` and *locked this turn* is the presentation-block member `lockedThisTurn` (§4.7 Stub 8), and T-INT-05 reaches both.
```

---

### Pair 8 — §4.4 week 3

Ruling I schedules T-UI-05 at week 3 with rows 4–5, on the principle §4.4 states
under its own table.

**OLD**

```
Only T-SAVE-07 still waits — for wk 4's self-play logs. AI second pass
```

**NEW:**

```
Only T-SAVE-07 still waits — for wk 4's self-play logs. **T-UI-05 is scheduled here too** (ruled 2026-08-04), and not as one of those re-runs: it is headless, and it asserts over the per-factory build record, which `Build` reaches and which rows 4–5 supply — the piece landing in the week the thing that consumes it runs, the principle stated below this table. AI second pass
```

---

## Sites checked, no pair needed

- §4.7 Stub 8, T-UI-05 clause (c) and its exclusion of the presentation block —
  neither member has a module-side counterpart or a derivation from one.
- §4.7 Stub 8, `spawnBlocked` — already carries a stated derivation.
- §4.7 Stub 8, Determinism line; Acceptance line.
- §4.7 Stub 8, per-hex, per-factory and match snapshot groups.
- §4.9 command/event bullet naming the view-model as snapshot plus presentation
  block.
- §4.10 canonical state hash and its omission rule.
- §4.11 rows 7 and 8 (dependency cells, acceptance sets), and the † bullet for
  T-UI-03/04.
- §4.5's risk row; §4.7's heading and open-questions preamble.
- §3's ledger paragraph and the UI evidence cell.
- §2.11.4, §2.11.5, §2.11.6, §2.11.1 — reached by Rulings F–I, and §2 is not
  paired this round (`ux-onboarding-designer` owns §2.11).

## Change requests

None filed.

## Open questions for the Director

None found.

## Grounding

- Ruling F, both halves and T-INT-05's non-narrowing, and Ruling J's field kind
  for `isGuidedMarked`: the 2026-08-04 ruling set supplied with this round.
- Field-kinds paragraph and the scenario file as a source a snapshot field may
  draw on: §4.7 Stub 8 snapshot preamble; T-UI-05 clauses (a) and (b).
- A hex identifies one placement: Stub 7's `guidedOpening` note, citing T-SCN-02.
- `Locked this turn.` as the guided opening's hover state, and beat 1a retiring
  when the marked Infantry's move completes: §2.11.6-B, turn 1a.
- §2.8 criterion 2 and criterion 3 text: §2.8's attrition-tiebreak list, keys 2
  and 3. N supplied by the scenario: §2.11.4.
- No accrual on turn 1; income from turn 2: Q8(a), §2.7.
- Income rates +100 factory / +25 town: §2.7, as already cited at Stub 8.
- Each piece lands in the week the thing that consumes it runs: §4.4's note
  under the milestone table (Q20, Q23).
- `Build` arriving with §4.11 rows 4–5: §4.4 weeks 2 and 3.
- No code implements T-UI-05, the per-factory block, `incomePerTurn`, or
  anything Rulings F–I add, at crew `main` `7c36303`: §4.7 Stub 8's acceptance
  line, §4.5's risk row, §3's UI evidence cell.
