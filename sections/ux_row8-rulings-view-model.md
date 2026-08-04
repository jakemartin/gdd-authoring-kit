# §2.11 row-8 rulings — view-model bindings (ux-onboarding-designer)

> ## ✅ APPLIED ADDENDUM — DO NOT RE-APPLY
>
> All five pairs were merged into the master GDD on 2026-08-04, together with
> `tech_row8-rulings-snapshot-hash.md` (22 pairs) in one 27-pair application.
> Master md5 `a5c266b921ea3ea7a3ce79c89137cc66` →
> `f327f0cf6a92e53fe59fab8550558e2e`.
>
> **All five pairs are replacements. None is an insertion**, so no OLD anchor
> survives on the merged master. The classification was derived by substring
> test from the final bytes, not by eye. Every OLD was verified against the
> **master** before anything was written, each matching exactly once, and the
> apply refused to write unless all twenty-seven did.
>
> Gate: run `row8-rulings-7`, **PASS**, 0 violations, after `row8-rulings-1`
> (BLOCK, 3) → `-2` (1) → `-3` (1) → `-4` (2) → `-5` (1) → `-6` (2). Not one
> violation in any run was in a pair's substance; the last four found only
> framing prose, and a deletion sweep by category produced the PASS.
>
> **`kb/rules.md` was not re-synced, and that was decided by reading it.** These
> five pairs are the round's only §2 edits, and §2 changed **only** in §2.11.1,
> §2.11.2 and §2.11.5 — enumerated by comparing every §2 heading block before
> and after. The KB mirrors §2.3, §2.4, §2.7 and §2.8 only; all four are
> **byte-identical** across the merge, and the overlap with the changed set is
> empty. Its md5 is unchanged at `024523449be1873c9d545dbea6d3bc9d`.
>
> Over-90-char non-table lines: **126 before, 126 after** — no reflow needed.
> `.txt` and `.pdf` rebuilt, each recipe control-tested by rebuilding the
> pre-merge master and comparing against the committed artifact.

Addendum of exact OLD/NEW pairs against `source/gdd.md`. §2.11 only.
Nothing outside §2.11 is paired here.

## What this round rules

Four of the Director's rulings of 2026-08-04 reach §2.11:

- **Ruling A** — per-unit presentation state lives in the **view-model** (the
  rules-produced snapshot plus a declared **presentation block**), not in a
  widget. §2.11.1's DONE bit is that block's sole member today. No
  module-produced DONE field, no acceptance ID.
- **Ruling C** — the snapshot gains a per-factory block and a per-side
  `incomePerTurn`. These are what the §2.11.5 production surfaces and the
  §2.11.2 Fame widget bind to. No acceptance ID.
- **Ruling E** — the per-factory block gains **`spawnBlocked`**, a declared
  derived field computed by the module: no free hex at or adjacent to the
  factory. That, not `buildWaiting`, is what §2.11.5's boxed-in footer and
  its disabled Build buttons bind to. `buildWaiting` keeps its narrow §2.7 /
  T-FAME-04 meaning — a build holding the factory's slot until it spawns —
  and a boxed-in factory need not have anything queued. The block is
  therefore `{hex, owner, hasBuiltThisTurn, buildWaiting, spawnBlocked}`.
  Ruling E mints no acceptance ID and moves no §4.5 count.
- **Ruling B** — `T-UI-05`, the snapshot-fidelity check, is `tech-director`'s
  to write in §4.5/§4.7. It bears on §2.11 only in that the surfaces below
  now name fields whose fidelity that check will assert; no §2.11 sentence
  states an acceptance ID, so no pair here carries one.

Ruling D (the §4.10 hash) touches no §2.11 sentence.

Five pairs follow: one on §2.11.1's DONE paragraph, two on §2.11.2 (the
info-panel line and two audit-table rows), and one on §2.11.5's two
production-menu bullets.

## Draft

### Pair 1 — §2.11.1, the paragraph defining DONE

Ruling A places the DONE bit in the view-model's presentation block. The
paragraph currently says only that DONE is "this machine's own" bit, which
leaves a reader free to read it as widget-local state. It also does not say
that the rules module has no such bit — a negative worth stating, because
§4.7 Stub 8's per-unit fields are `hasMoved` and `hasActed` and neither is
this one.

**OLD**

```
**What DONE means, and what binds to it.** DONE is this machine's own per-unit bit — *this unit takes no further command this turn* — and it is not the act flag. It is per-turn: it clears when the owner's next turn begins.
```

**NEW:**

```
**What DONE means, and what binds to it.** DONE is this machine's own per-unit bit — *this unit takes no further command this turn* — and it is not the act flag. It lives in the **view-model** — the rules-produced snapshot plus a declared **presentation block** — as that block's sole member. The rules module has no DONE bit and no Wait command; no snapshot field mirrors this bit and none is asked for. It is per-turn: it clears when the owner's next turn begins.
```

### Pair 2 — §2.11.2, the info panel's hovered-unit line

The line already refuses to read `ready`/`done` off a raw flag. Ruling A lets
it say where the bit is read from instead of only what it is not.

**OLD**

```
- Hovered unit: name, HP as `12/20`, Atk/Def/Move/Range, and `ready` or `done` — the machine's DONE bit (§2.11.1), not a raw flag name: a waited unit reads `done` while its act flag is unspent.
```

**NEW:**

```
- Hovered unit: name, HP as `12/20`, Atk/Def/Move/Range, and `ready` or `done` — the machine's DONE bit (§2.11.1), read from the view-model's presentation block and not from a snapshot flag: a waited unit reads `done` while its act flag is unspent.
```

### Pair 3 — §2.11.2, earn-your-pixels audit, the unacted-pip row

The audit table is where each element's binding is on the record. Ruling A
changes where this element's bit lives, so the row's Rule-surfaced cell names
the presentation block.

**OLD**

```
| Unacted pip on own units | Which units I can still give an order to | §2.1 per-unit loop, via the DONE bit of §2.11.1's machine |
```

**NEW:**

```
| Unacted pip on own units | Which units I can still give an order to | §2.1 per-unit loop, via the DONE bit of §2.11.1's machine, carried in the view-model's presentation block |
```

### Pair 4 — §2.11.2, earn-your-pixels audit, the Fame pool row

Factories pay +100/turn and towns +25/turn (§2.7), and the scoreboard's
Objectives figure is an undifferentiated *X of N* (§2.11.4). The `+X/turn`
rate was therefore stated without any field that could produce it. Ruling C's
per-side `incomePerTurn` is what the widget reads.

**OLD**

```
| Fame pool + `+X/turn` | Build now vs. save; which neutral factory is worth a fight | §2.7 income (+100 factory / +25 town), costs |
```

**NEW:**

```
| Fame pool + `+X/turn` | Build now vs. save; which neutral factory is worth a fight | §2.7 income (+100 factory / +25 town), costs — the `+X/turn` figure is the snapshot's per-side `incomePerTurn`, not a figure derived from the scoreboard's *X of N*, which does not separate factories from towns |
```

### Pair 5 — §2.11.5, the two production-menu bullets that read factory state

The `BUILD` pulse's not-built-this-turn half and the footer's boxed-in swap
each stated a condition with no snapshot field behind it. Ruling C's
`hasBuiltThisTurn` and Ruling E's `spawnBlocked` supply those two, and each
bullet names the field it reads so no widget is left to scan the board for
itself. The footer binds to `spawnBlocked` and not to `buildWaiting`: the two
come apart at a boxed-in factory with nothing queued, which is the case the
footer exists for. Nothing this round ruled reaches the pulse's affordability
half, so neither bullet says anything about it.

**OLD**

```
- The spawn rule (§2.7: factory hex if free, else an adjacent free hex) is one static line in the footer. If the factory is fully boxed in, the footer swaps to `Boxed in — build waits for a free hex.` and Build buttons disable: the space-throttle (§2.7) explains itself at the moment it applies.
- When any unit is affordable and the factory has not built this turn, the factory tile shows a small `BUILD` pulse — the nudge that connects hoarded Fame to an army (a first-session failure mode, §2.11.6 ledger).
```

**NEW:**

```
- The spawn rule (§2.7: factory hex if free, else an adjacent free hex) is one static line in the footer. If the factory is fully boxed in, the footer swaps to `Boxed in — build waits for a free hex.` and Build buttons disable: the space-throttle (§2.7) explains itself at the moment it applies. Both the swap and the disable read the snapshot's per-factory `spawnBlocked` — board geometry, computed by the module, no board scan the widget runs for itself. They do not read `buildWaiting`, which is the narrower §2.7 fact that a build is holding this factory's slot until it spawns: a boxed-in factory need not have anything queued.
- When any unit is affordable and the factory has not built this turn, the factory tile shows a small `BUILD` pulse — the nudge that connects hoarded Fame to an army (a first-session failure mode, §2.11.6 ledger). The second half of that condition is read rather than inferred: the factory's own `hasBuiltThisTurn` — the per-factory build record the rules module already holds — out of the snapshot's per-factory block `{hex, owner, hasBuiltThisTurn, buildWaiting, spawnBlocked}`.
```

## Sites checked, no pair needed

- **§2.11.2, the three-information-layers list.** Layer 1 names "Fame pool +
  income rate" and "unacted-unit pips" as elements without stating a binding,
  so no ruling falsifies it. Layer 3's "income toasts restate what the Fame
  widget's `+X/turn` already shows" stays true under Pair 4 — the rate's
  source changed, not what the toast restates. Adding the field names here
  would only duplicate the audit table two paragraphs below.
- **§2.11.4, the Objectives row.** It reads *X of N* over factories +
  capturable towns as §2.8 criterion 2, which is the tiebreak's own
  undifferentiated count. That row is correct as written; it is the Fame
  widget's rate, not this row, that needed a field.
- **§2.11.6-D, the "Fame income & build" ledger row.** Its "`BUILD` pulse when
  affordable" is a back-reference to §2.11.5, which Pair 5 amends in place.
- **§2.11.1's list of surfaces that bind to DONE**, and §2.11.6-D's spawned-
  unit pip. Ruling A relocates the bit without changing which surfaces read
  it, so every one of those sentences stays true unedited.

## Filed for the Director

Two things outside §2.11, noted here and not paired, because §3 and §4 are
`tech-director`'s this round:

1. §4.7 Stub 8's field list carries `per-side {fameTotal, fameCombat,
   objectivesHeld X of N, survivingHP}` and a per-unit line, and no
   per-factory block. Pairs 4 and 5 above name `incomePerTurn`,
   `hasBuiltThisTurn` and `spawnBlocked` as fields §2.11 surfaces read. Until
   Stub 8's field list carries them, §2.11 names fields the stub does not.
2. No code implements the per-factory block, `incomePerTurn`, `spawnBlocked`,
   T-UI-05, or the widened hash. The surfaces amended by Pairs 4 and 5 remain
   unfeedable in the build at crew `main` `7c36303` — three fields now, not
   two — and row 8's ledger row stays `*pending*`. Nothing in this addendum
   changes that, and no §2.11 sentence claims otherwise.

## Grounding

| Pair | UX decision | Mechanic / ruling it serves |
|---|---|---|
| 1 | DONE is named as the view-model's presentation-block member | Ruling A; §2.1 per-unit loop; the module's two independent flags `hasMoved`/`hasActed` (§4.7 Stub 8) are not this bit |
| 2 | `ready`/`done` in the info panel reads the presentation block | Ruling A; §2.11.1's machine retires a unit on Wait or RMB-in-MOVED without spending the act flag |
| 3 | The unacted pip's audit row records the same source | Ruling A; §2.11.2's rule that every element names the rule it surfaces |
| 4 | The Fame widget's `+X/turn` reads `incomePerTurn` | Ruling C; §2.7's two income rates (+100 factory, +25 town), which an *X of N* count cannot distinguish |
| 5, first bullet | The boxed-in footer and disabled Build buttons read `spawnBlocked` | Ruling E; §2.7's spawn rule (factory hex if free, else an adjacent free hex) is board geometry, which `buildWaiting`'s T-FAME-04 slot-holding meaning does not express |
| 5, second bullet | The `BUILD` pulse reads `hasBuiltThisTurn` | Ruling C; §2.7's build rules; T-TURN-10's per-factory build record, already held by the module |
