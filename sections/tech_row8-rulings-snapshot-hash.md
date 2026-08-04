# Row-8 rulings addendum — snapshot fidelity, view-model, and the state hash (tech-director)

> ## ✅ APPLIED ADDENDUM — DO NOT RE-APPLY
>
> All twenty-two pairs were merged into the master GDD on 2026-08-04, together
> with `ux_row8-rulings-view-model.md` (5 pairs) in one 27-pair application.
> Master md5 `a5c266b921ea3ea7a3ce79c89137cc66` →
> `f327f0cf6a92e53fe59fab8550558e2e`.
>
> **Eighteen pairs are replacements. Four are INSERTIONS — Pairs 2, 8, 10 and
> 11** — each NEW containing its OLD verbatim, so **those four anchors survive
> on the merged master by design** and this file is not safe to apply twice.
>
> **Read that list, not the prose above it.** The Draft describes Pair 8b as an
> "Insertion at the group header" and Pair 9 as "Insertion plus replacement";
> both are true about the *content* and false about the *anchor*, because each
> edits the text it anchors on — 8b turns the header's colon into a period, 9
> rewrites the `per-side` line. Mechanically neither anchor survives, and the
> post-check was driven by a substring test over the final bytes rather than by
> those labels. Every OLD was verified against the **master** before anything
> was written, each matching exactly once, and the apply refused to write unless
> all twenty-seven did.
>
> Gate: run `row8-rulings-7`, **PASS**, 0 violations, after `row8-rulings-1`
> (BLOCK, 3) → `-2` (1) → `-3` (1) → `-4` (2) → `-5` (1) → `-6` (2).
>
> **§4.5 now reads 71 written / 52 green / 19 unclosed**, 17 IDs in rows 8–10,
> 9 verified ledger rows; §3's uncovered count moved 8 → 9. `T-UI-05` is
> written, unblocked, asserting and **not green** — no code implements it, nor
> the per-factory block, `incomePerTurn`, `spawnBlocked` or the widened hash.
> Row 8's ledger row stays `*pending*`.
>
> Over-90-char non-table lines: **126 before, 126 after** — no reflow needed.
> `kb/rules.md` untouched; the round's §2 edits are the ux addendum's and reach
> no subsection the KB mirrors. `.txt` and `.pdf` rebuilt, each recipe
> control-tested against the committed artifact before use.

Exact OLD/NEW pairs against `source/gdd.md`. §3 and §4 only. No section is
redrafted; nothing outside §3 and §4 carries a pair.

## What this round rules

Director rulings of 2026-08-04, all filed by row 8 (UI binding, Stub 8):

- **A — view-model = snapshot + presentation block.** The presentation block
  holds the per-unit state §2.11.1's selection machine owns; §2.11.1's DONE
  bit is its sole member today. DONE is derivable from neither `hasMoved` nor
  `hasActed`, so no module-produced field is added and no acceptance ID is
  minted. T-INT-05 binds to the view-model.
- **B — `T-UI-05`**, a headless, unmarked snapshot-fidelity check asserting
  that the Stub 8 snapshot tells the truth about the state the module holds —
  `GameState` plus the §4.8 tables and the Stub-7 scenario file it loaded
  (§4.9). Written, unblocked, asserting, **not green**: no code implements it,
  and row 8's ledger row stays `*pending*`.
- **C — snapshot gains a per-factory block** `{hex, owner, hasBuiltThisTurn,
  buildWaiting}` **and a per-side `incomePerTurn`**. Both expose state the
  module already holds. No acceptance ID.
- **D — the §4.10 canonical state hash gains both per-unit turn flags and the
  per-factory build record**, every added field an integer and every added
  collection in canonical hex order.
- **E — the per-factory block gains `spawnBlocked`**, board geometry (no free
  hex at or adjacent to the factory), computed by the module and **declared
  derived**. It is distinct from `buildWaiting`, which keeps its narrow
  meaning. It does **not** enter the §4.10 hash — it is recomputable from
  fields the hash already carries. No acceptance ID.

Minting T-UI-05 is what carries this round outside Stub 8: it adds an ID that
is unclosed and not green, so every sentence saying the in-editor pass is the
whole of what row 8 lacks, and every count of what is unclosed, becomes false.
Those sites were found by grepping `T-UI-`, the §4.5 counts, and row 8's
ledger row and record document-wide, and Ruling A's terms by grepping *view
model* and *view-model* in both spellings.

## §4.5 arithmetic

| Quantity | Before | After | Derivation |
|---|---|---|---|
| Written acceptance IDs | 70 | **71** | T-UI-05 is the only ID minted this round; Rulings A, C, D and E mint none |
| Green | 52 | **52** | no code implements T-UI-05 |
| Unclosed | 18 | **19** | 71 − 52 = 19 |
| IDs in rows 8–10 | 16 | **17** | row 8 T-UI-01..05 = 5 (GATE-CAP-PARTIAL mints none), row 9 T-INT-01..05 = 5, row 10 T-SAVE-01..07 = 7 |
| Verified ledger rows (§3) | 9 | **9** | no row flips |

The unclosed 19, itemised, is T-DATA-05 (1) + T-SCN-08, 09, 11 (3) + T-UI-03,
04 (2) + T-UI-05 (1) + the 12 in rows 9–10 = 19. §3's uncovered-ID count moves
with it: 8 → **9**, of which 2 stay unwritten (T-MOVE-07 on Q2, T-SCN-10 on
Q26) and 6 → **7** are written and not green.

## Draft

### Pair 1 — §3, the ledger lead-in's per-acceptance-ID clause

Minting T-UI-05 falsifies this enumeration as written. Line-internal to §3's
unwrapped status paragraph, so the NEW stays on one line.

**OLD**

```
and the path IDs still written and asserting without being green are **T-UI-03** and **T-UI-04**
```

**NEW:**

```
and the path IDs still written and asserting without being green are **T-UI-03**, **T-UI-04** and **T-UI-05**
```

### Pair 2 — §3, row 8's landing record, the three known-absent snapshot fields

**Insertion** — the OLD sentence is a true record of `7c36303` and is kept
whole; the NEW adds what has been ruled since. Without it the record reads as
the current state of the stub, which it no longer is. The per-factory block is
listed with the members Rulings C and E give it, so §3 and Stub 8 agree.

**OLD**

```
and three known-absent snapshot fields were left absent — the per-factory record of builds taken this turn, the income rate, and §2.11.1's DONE bit.
```

**NEW:**

```
and three known-absent snapshot fields were left absent — the per-factory record of builds taken this turn, the income rate, and §2.11.1's DONE bit. **All three have since been ruled into §4.7 Stub 8**, on 2026-08-04: the first two as snapshot fields — the per-factory block `{hex, owner, hasBuiltThisTurn, buildWaiting, spawnBlocked}` and the per-side `incomePerTurn` — and the DONE bit into the stub's **presentation block**, which the rules module does not produce and which is the second half of the view-model beside the snapshot. **No code implements any of the three**, and the same rulings minted **`T-UI-05`**, a headless snapshot-fidelity check that no code implements either, so what row 8 lacks after this commit is no longer the in-editor pass alone.
```

### Pair 2b — §3, the debug driver's `snapshot` command

The sentence was true while *view model* and *snapshot* named one thing. Pair
7 splits them, and the presentation block is implemented by no code, so what
the binary prints at `7c36303` is the snapshot. Line-internal to §3's
unwrapped status paragraph, so the NEW stays on one line.

**OLD**

```
The debug driver's `snapshot` command now prints the view model rather than refusing on row 8's account
```

**NEW:**

```
The debug driver's `snapshot` command now prints the snapshot rather than refusing on row 8's account — the snapshot and not the whole view-model, whose other half, §4.7 Stub 8's presentation block, is produced by no rules field and implemented by no code at that commit or since
```

### Pair 3 — §3, the ledger's UI evidence cell

The cell states the in-editor pass as the sole reason the acceptance set is
incomplete. T-UI-05 is a second reason and a different one. Single-line: the
cell is a table row.

**OLD**

```
**T-UI-03 and T-UI-04 have not run**: both are in-editor Unreal Automation over widget bindings and no in-editor pass exists at this commit, so the acceptance set is incomplete and Q29, read per ID, keeps the row unverified |
```

**NEW:**

```
**T-UI-03, T-UI-04 and T-UI-05 have not run**: T-UI-03 and T-UI-04 are in-editor Unreal Automation over widget bindings and no in-editor pass exists at this commit; **T-UI-05** was minted 2026-08-04, after this commit, is headless, and no code implements it. The acceptance set is incomplete on both counts and Q29, read per ID, keeps the row unverified |
```

### Pair 4 — §3, the uncovered-ID decomposition below the table

T-UI-05's state is stated in its own terms — headless and unimplemented — and
not folded into the in-editor group it does not belong to.

**OLD**

```
Eight IDs are still recorded as **uncovered** rather than omitted, in **two states that are not the same state**. Two are **unwritten**: **T-MOVE-07**, reserved on Q2, and **T-SCN-10**, reserved on Q26 — no invariant text exists for either, so neither asserts and neither is waiting on a run. Six are **written and not green**: **T-DATA-05**, the in-editor Unreal Automation half, which has not run; **T-SCN-08**, **T-SCN-09** and **T-SCN-11**, each written, unblocked and asserting, each having run only part of its fixture set; and **T-UI-03** and **T-UI-04**, written, unblocked and asserting, in-editor Unreal Automation for which no in-editor pass exists at row 8's commit.
```

**NEW:**

```
Nine IDs are still recorded as **uncovered** rather than omitted, in **two states that are not the same state**. Two are **unwritten**: **T-MOVE-07**, reserved on Q2, and **T-SCN-10**, reserved on Q26 — no invariant text exists for either, so neither asserts and neither is waiting on a run. Seven are **written and not green**: **T-DATA-05**, the in-editor Unreal Automation half, which has not run; **T-SCN-08**, **T-SCN-09** and **T-SCN-11**, each written, unblocked and asserting, each having run only part of its fixture set; **T-UI-03** and **T-UI-04**, written, unblocked and asserting, in-editor Unreal Automation for which no in-editor pass exists at row 8's commit; and **T-UI-05**, written, unblocked and asserting, headless, minted 2026-08-04 and implemented by no code — it waits on neither a harness nor a rule but on an implementation.
```

### Pair 5 — §3, why the UI row carries evidence without a ✓

The paragraph's per-row attribution names only the two in-editor IDs.

**OLD**

```
and T-UI-03 and T-UI-04 are why **UI** does the same at [`7c36303`](https://github.com/jakemartin/stratocracy-crew/commit/7c36303).
```

**NEW:**

```
and T-UI-03, T-UI-04 and T-UI-05 are why **UI** does the same at [`7c36303`](https://github.com/jakemartin/stratocracy-crew/commit/7c36303) — the first two for want of an in-editor pass, the third because no code implements it.
```

### Pair 6a — §4.5, the written-ID count and what has been written since `c224825`

The row's *reduced and re-scoped* framing is kept, and the direction T-UI-05
moves the gap is stated rather than absorbed by it. Single-line: the cell is a
table row.

**OLD**

```
| **Specification outruns the build** — **70** written acceptance IDs at this revision (§4.7–§4.11) against **9** verified ledger rows (§3). **Reduced and re-scoped at 2026-08-04, not retired:** one new ID has been written since `c224825` — `T-TURN-10`, minted this revision into Spec Stub 5 for the per-turn build limit Q8(b) ruled — and it is **green at `6ccd40b`**, the rebuild at which row 5's widened acceptance set closes in full (§3); row 6's GATE-AI-SMOKE is acceptance that deliberately mints none, so it closes a check without moving this count. **52** of the 70 are green:
```

**NEW:**

```
| **Specification outruns the build** — **71** written acceptance IDs at this revision (§4.7–§4.11) against **9** verified ledger rows (§3). **Reduced and re-scoped at 2026-08-04, not retired:** two new IDs have been written since `c224825`. `T-TURN-10`, minted into Spec Stub 5 for the per-turn build limit Q8(b) ruled, is **green at `6ccd40b`**, the rebuild at which row 5's widened acceptance set closes in full (§3). `T-UI-05`, minted 2026-08-04 into Spec Stub 8 for the snapshot-fidelity check row 8's landing left ungated, is **implemented by no code** and **widens this gap by one** — the two movements are counted separately and the second is not absorbed by the first. Row 6's GATE-AI-SMOKE is acceptance that deliberately mints none, so it closes a check without moving this count; the same holds for row 8's GATE-CAP-PARTIAL, and for the presentation block and the snapshot fields ruled beside T-UI-05 on the same day, which mint no ID at all. **52** of the 71 are green:
```

### Pair 6b — §4.5, the unclosed enumeration

T-UI-05 is itemised in its own state. Single-line: same table cell.

**OLD**

```
**18 IDs remain unclosed**: T-DATA-05, which leaves row 2 unflipped; T-SCN-08, T-SCN-09 and T-SCN-11, which are written, unblocked and asserting, but ran only part of their fixture sets, and which leave row 7 unflipped; T-UI-03 and T-UI-04, which are written, unblocked and asserting, and for which no in-editor pass exists at row 8's commit, and which leave row 8 unflipped; and the **12** in rows 9–10, which hold no code
```

**NEW:**

```
**19 IDs remain unclosed**: T-DATA-05, which leaves row 2 unflipped; T-SCN-08, T-SCN-09 and T-SCN-11, which are written, unblocked and asserting, but ran only part of their fixture sets, and which leave row 7 unflipped; T-UI-03 and T-UI-04, which are written, unblocked and asserting, and for which no in-editor pass exists at row 8's commit; T-UI-05, which is written, unblocked, asserting and headless, and which no code implements — so row 8 stays unflipped on it whatever the editor pass does; and the **12** in rows 9–10, which hold no code
```

### Pair 7 — §4.7 Stub 8, Scope: the view-model is snapshot plus presentation block

Ruling A, at the stub's own definition site: what the block holds, and why it
is declared at the stub rather than left to a widget.

**OLD**

```
Scope:   NOT layout or visual design (§2.11's lane) — this is
         the contract for how every widget is fed. Widgets bind to a view-model
         snapshot plus the §4.9 event list, and hold no rules state (§4.1).
```

**NEW:**

```
Scope:   NOT layout or visual design (§2.11's lane) — this is
         the contract for how every widget is fed. Widgets bind to the
         VIEW-MODEL plus the §4.9 event list, and hold no rules state (§4.1).
         The VIEW-MODEL is the rules-produced SNAPSHOT below plus a declared
         PRESENTATION BLOCK: the per-unit state §2.11.1's SELECTION MACHINE
         owns and no rules field expresses. It is declared here rather than
         improvised in a widget because T-INT-05 (§4.9) rebuilds from the
         view-model: state in the block satisfies it, state in a widget does
         not.
```

### Pair 8 — §4.7 Stub 8, the per-unit flags note

**Insertion** — the existing note is kept whole and gains where the DONE bit
lives. Ruling A: DONE is derivable from neither flag, so no module-produced
field is added for it.

**OLD**

```
                    `hasMoved` and `hasActed` are the TWO INDEPENDENT flags
                    T-TURN-01 asserts, carried into the snapshot as two
                    fields: one field cannot express a unit that has spent
                    exactly one of them. Neither is §2.11.1's DONE bit, and
                    no §2.11 surface reading "has not acted" binds to
                    either — §2.11.1 states where those bind.
```

**NEW:**

```
                    `hasMoved` and `hasActed` are the TWO INDEPENDENT flags
                    T-TURN-01 asserts, carried into the snapshot as two
                    fields: one field cannot express a unit that has spent
                    exactly one of them. Neither is §2.11.1's DONE bit, and
                    no §2.11 surface reading "has not acted" binds to
                    either — §2.11.1 states where those bind. The DONE bit
                    is DERIVABLE FROM NEITHER, and from no pair of them:
                    Wait and RMB-in-MOVED both reach DONE without spending
                    the act flag (§2.11.1). It is therefore not a snapshot
                    field, the module produces no field for it, and it sits
                    in the presentation block below.
```

### Pair 8b — §4.7 Stub 8, the snapshot header: the two kinds a field may be

**Insertion** at the group header — the contract T-UI-05 binds to, so that
every snapshot field has a kind and a source a check can reach.

The kinds were checked against every field the stub lists, since an earlier
wording named `GameState` alone and was false of several. **`GameState`
mirrors:** per-hex `owner`; per-unit `id`, `side`, `hex`, `hp`, `isFlag`,
`hasMoved`, `hasActed`, `captureProgress`; per-factory `owner`,
`hasBuiltThisTurn`, `buildWaiting`; per-side `fameTotal`, `fameCombat`; match
`turn`, `sideToMove`, `resultTier or null`. **§4.8-table mirrors:** per-unit
`unitId` and `hpMax`, the latter being the `HP` column loaded into
`strat::UnitDef` (§4.8). **Scenario-file mirrors:** per-hex `terrainId`; the
per-factory `hex`; match `turnCap` (Q7, Stub 7's field). **Declared derived:**
per-factory `spawnBlocked`; per-side `objectivesHeld X of N`, `survivingHP`,
`incomePerTurn`. Every field the stub lists falls in exactly one of those
groups, and none falls in two.

**OLD**

```
Snapshot fields (read-only, produced by the rules module):
```

**NEW:**

```
Snapshot fields (read-only, produced by the rules module). Every field in the
         snapshot groups that follow has one of TWO KINDS. A MIRROR — the
         unmarked default — equals, unchanged, the module-side value it
         names, in the authoritative `GameState`, in the §4.8 tables the
         bridge loaded, or in the Stub-7 scenario file it loaded; §4.9 names
         those three separately, and a mirror may draw on any of them.
         A field marked DECLARED DERIVED is computed from them instead, and
         its derivation is stated beside it. Within these groups those are
         the only two kinds, and T-UI-05 asserts both:
```

### Pair 9 — §4.7 Stub 8, per-factory block and per-side income

Rulings C and E. **Insertion plus replacement**: the per-factory lines are new
and the per-side line is replaced to carry `incomePerTurn`. `hasBuiltThisTurn`
and `buildWaiting` are state the module already holds; `spawnBlocked` is board
geometry and is declared derived, as are the two per-side fields that were
already derived before this round.

**OLD**

```
         per-side  {fameTotal, fameCombat, objectivesHeld X of N, survivingHP}
```

**NEW:**

```
         per-factory {hex, owner, hasBuiltThisTurn, buildWaiting,
                    spawnBlocked}
                    `hasBuiltThisTurn` is T-TURN-10's per-factory build
                    allowance and `buildWaiting` the §2.7 build that holds
                    the factory's slot until it spawns (T-FAME-04); both
                    mirror state the module already holds, and this exposes
                    it rather than adding it. The `hex` mirrors the scenario
                    file's factory placement (Stub 7). `spawnBlocked` is
                    DECLARED DERIVED: true exactly when no hex at or
                    adjacent to the factory is free (board geometry, §2.7's
                    spawn rule), computed by the module and never
                    widget-side. It and `buildWaiting` are DISTINCT, and the
                    difference is the case §2.11.5 must display: a boxed-in
                    factory with nothing queued has `spawnBlocked` true and
                    `buildWaiting` false, which `buildWaiting` alone cannot
                    express. Q31 asks whether a player may queue into a
                    boxed-in factory; `buildWaiting` is the field such a
                    ruling would bind to, and nothing here rules it — today
                    the waiting build is an AI-only path (Q31) and no gate
                    asserts a player-queued one.
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

### Pair 10 — §4.7 Stub 8, the presentation block

**Insertion** after the last snapshot group. Ruling A's second half: the block
is declared, its owner is named, and its membership is that owner's per-unit
state. The closing clause names one instance and defers it.

**OLD**

```
         match     {turn, turnCap, sideToMove, resultTier or null}
```

**NEW:**

```
         match     {turn, turnCap, sideToMove, resultTier or null}
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

### Pair 11 — §4.7 Stub 8, the T-UI-05 invariant

**Insertion** after T-UI-04. Ruling B: that the snapshot tells the truth about
the module's own state is asserted by nothing else in the stub. Clauses (a)
and (c) are written in the two kinds Pair 8b declares and move with it.

**OLD**

```
  T-UI-04  the production menu binds to the buildlist derived from the four
           Stub-2 unit rows plus current fameTotal; the flag never appears
           (T-SCN-01's non-producible clause, enforced at the UI layer too)
```

**NEW:**

```
  T-UI-04  the production menu binds to the buildlist derived from the four
           Stub-2 unit rows plus current fameTotal; the flag never appears
           (T-SCN-01's non-producible clause, enforced at the UI layer too)
  T-UI-05  snapshot fidelity: the snapshot tells the truth about the state
           the module holds — the authoritative `strat::GameState`, the §4.8
           tables and the Stub-7 scenario file it loaded (§4.9) — field by
           field, in three parts. (a) MIRRORS: every unmarked field equals
           the module-side value it names, exactly, with nothing widened,
           narrowed, rounded or reordered. (b) DECLARED DERIVED: every field
           marked DECLARED DERIVED equals the derivation stated beside it at
           this stub, recomputed inside the check rather than read back out
           of the snapshot — so a wrong derivation fails here and is not
           merely reproduced. (c) NO OTHER KIND: a snapshot field that is
           neither an unmarked mirror of a named module-side value nor a
           marked field with a stated derivation FAILS this invariant, which
           is what stops a field entering the snapshot without a contract.
           Asserted by rebuilding the snapshot after each command of a fixed
           command sequence and comparing every field under (a), (b) and
           (c). The presentation block is NOT in this invariant's subject:
           it has no module-side counterpart and no derivation from one.
           Headless, unmarked (§4.11)
```

### Pair 12 — §4.7 Stub 8, Determinism

The determinism line names the snapshot where T-INT-05 now binds to the
view-model.

**OLD**

```
Determinism: widgets are pure functions of snapshot + events; asserted
         end-to-end by T-INT-05 (§4.9).
```

**NEW:**

```
Determinism: widgets are pure functions of view-model + events — snapshot
         plus presentation block; asserted end-to-end by T-INT-05 (§4.9).
```

### Pair 13 — §4.7 Stub 8, Acceptance

T-UI-05 joins the headless half, and the NEW records what no code does yet.

**OLD**

```
Acceptance: T-UI-01..02 headless (the queries are headless functions);
         T-UI-03..04 in-editor Automation; GATE-CAP-PARTIAL headless, on the
         snapshot rather than on a widget — which is why it carries no † and
         does not stand down if the editor pass does. A marked ID may not
         guard a rules invariant (§4.11's † note), and T-CAP-05 is one.
```

**NEW:**

```
Acceptance: T-UI-01..02 and T-UI-05 headless (the queries and the snapshot
         builder are headless functions); T-UI-03..04 in-editor Automation;
         GATE-CAP-PARTIAL headless, on the snapshot rather than on a widget —
         which is why it carries no † and does not stand down if the editor
         pass does. A marked ID may not guard a rules invariant (§4.11's †
         note), and T-CAP-05 is one. T-UI-05 was minted 2026-08-04 and NO
         CODE IMPLEMENTS IT: it is written, unblocked and asserting, and it
         is not green — four states this document keeps distinct. Nothing in
         the snapshot additions ruled with it is implemented either.
```

### Pair 14 — §4.9, the bridge's rebind contract

Ruling A's vocabulary at the one §4.9 site that names what widgets rebind
from.

**OLD**

```
Actors and widgets animate and rebind **from events and
  the view-model snapshot only** (§4.7 Stub 8).
```

**NEW:**

```
Actors and widgets animate and rebind **from events and
  the view-model only** — §4.7 Stub 8's snapshot plus its presentation
  block (§4.7).
```

### Pair 15 — §4.9, T-INT-05's subject

Ruling A: T-INT-05 binds to the view-model, which is what makes it
satisfiable.

**OLD**

```
  T-INT-05  (editor, Automation) presentation statelessness: after any event
            sequence, rebuilding all widgets/actors from the current view-model
            snapshot alone reproduces the same displayed values (nothing lives
            only in a widget)
```

**NEW:**

```
  T-INT-05  (editor, Automation) presentation statelessness: after any event
            sequence, rebuilding all widgets/actors from the current view-model
            alone — §4.7 Stub 8's snapshot plus its presentation block —
            reproduces the same displayed values (nothing lives only in a
            widget). §2.11.1's selection machine is not a widget, so its DONE
            bit satisfies this gate from the presentation block
```

### Pair 16 — §4.10, the canonical state hash

Ruling D. The per-unit turn flags and the per-factory build record join the
hash, each added field an integer and the added collection in the canonical
hex order the per-unit list already uses. The exclusion that keeps
`spawnBlocked` out is written as recomputability from the hashed fields rather
than as a rule about derived values, because §4.10's Policies call a waiting
build and capture-in-progress derived pending state and the hash carries both.

**OLD**

```
**Canonical state hash.** Defined once, in the headless module: serialize the
`GameState` in a fixed field order — turn counter, side to move, per-side
`fameTotal`/`fameCombat`, objective ownership, per-unit `{id, side, hex, hp,
isFlag, captureProgress, pendingBuilds}` sorted by the canonical hex order
(§4.7 conventions, T-HEX-07) — then hash the bytes. Every field is an
**integer** (`eff` and the HP ratio exist only transiently inside
`resolveDamage`), so the hash is platform-stable by construction; T-INT-02
proves it across compilers.
```

**NEW:**

```
**Canonical state hash.** Defined once, in the headless module: serialize the
`GameState` in a fixed field order — turn counter, side to move, per-side
`fameTotal`/`fameCombat`, objective ownership, per-unit `{id, side, hex, hp,
isFlag, hasMoved, hasActed, captureProgress, pendingBuilds}` sorted by the
canonical hex order (§4.7 conventions, T-HEX-07), then the per-factory build
record `{hex, hasBuiltThisTurn, buildWaiting}` (T-TURN-10) in that same
canonical hex order — then hash the bytes. Every field is an **integer**, the
four turn and build flags written as 0 or 1 (`eff` and the HP ratio exist only
transiently inside `resolveDamage`), so the hash is platform-stable by
construction; T-INT-02 proves it across compilers. **The flags are hashed
because a save is accepted mid-turn** (Policies below): at hash time a unit may
have spent one of its two flags and a factory may have taken its build for the
turn, so a hash without them is identical across states the rules distinguish,
and T-INT-02 and T-SAVE-06 would both agree over that difference rather than
catch it. **What the hash omits is anything recomputable from the fields it
already carries**, since such a value can add no distinction and only one more
way for two builds of one state to disagree: §4.7 Stub 8's `spawnBlocked` is
that case, being a function of the unit positions this hash carries and the
terrain the scenario file fixes, whose own `scenarioHash` is a header field
above. That is a narrower test than "derived", and deliberately so — the
Policies below call a waiting build and capture-in-progress derived *pending*
state because they are a function of the log, and both are hashed. Row 10 holds
no code and no save file exists, so widening the hash costs nothing at this
revision and would not stay free.
```

### Pair 17 — §4.11, the lead-in's account of row 8's partial pass

The lead-in gives the in-editor half as the whole reason row 8 is unflipped.

**OLD**

```
**Row 8 has since landed too**, at `7c36303`, on a partial pass
that leaves its ledger row unflipped, as row 7's does (§3): T-UI-03 and
T-UI-04 are the in-editor half and no in-editor pass exists at that commit.
```

**NEW:**

```
**Row 8 has since landed too**, at `7c36303`, on a partial pass
that leaves its ledger row unflipped, as row 7's does (§3): T-UI-03 and
T-UI-04 are the in-editor half and no in-editor pass exists at that commit,
and **T-UI-05 is headless and unimplemented** — minted 2026-08-04, after that
commit, so the editor pass is not the whole of what this row still lacks.
```

### Pair 18 — §4.11, row 8's acceptance-ID cell

The table is authoritative for the † split, so T-UI-05 must appear here to be
readable as unmarked. Nothing else in the row moves: T-UI-05 is headless and
sits under the cell's existing "Contract + queries yes".

**OLD**

```
| 8 | UI binding (Stub 8) | 5, 7 (snapshot needs full state) | Contract + queries yes; widgets in-editor | T-UI-01..04 (**T-UI-03, 04 †**) + GATE-CAP-PARTIAL |
```

**NEW:**

```
| 8 | UI binding (Stub 8) | 5, 7 (snapshot needs full state) | Contract + queries yes; widgets in-editor | T-UI-01..05 (**T-UI-03, 04 †**) + GATE-CAP-PARTIAL |
```

### Pair 19 — §4.11, the † bullet for row 8

The bullet enumerates the unmarked T-UI IDs, and T-UI-05 is one.

**OLD**

```
- **T-UI-03, 04** — in-editor Automation over widget bindings, where a Director
  reading the screen is a real check. T-UI-01/02 stay unmarked: they are
  headless queries, and T-UI-01 is what makes §2.11.3's forecast equal the
  resolution.
```

**NEW:**

```
- **T-UI-03, 04** — in-editor Automation over widget bindings, where a Director
  reading the screen is a real check. T-UI-01/02 and T-UI-05 stay unmarked:
  all three are headless, T-UI-01 is what makes §2.11.3's forecast equal the
  resolution, and T-UI-05 is the sole assertion that the snapshot tells the
  truth about the state the module holds — the contract every other ID in the
  row reads through.
```

## Checked, and needing no pair

- **§4.8's schemas** are unedited. Pair 8b cites the `HP` → `strat::UnitDef`
  `hpMax` row to place `unitId` and `hpMax` as §4.8-table mirrors; it changes
  no column, type or field name there, and "nothing is authored twice" still
  holds, since the snapshot mirrors those values rather than restating them.
- **§4.7 Stub 7's `guidedOpening` note and Q27** are unedited and unpaired.
  Stub 7 keeps the guided opening's marked/locked state out of Stub 8's
  snapshot and has the guidance layer read it from the loaded scenario
  directly; Q27 rides on the same reasoning. Nothing ruled this round reaches
  the guidance layer. What that leaves unresolved is filed as a change request
  below.
- **T-TURN-10's per-side-turn renewal boundary** is present in the master:
  Stub 5's T-TURN-10 reads "The allowance renews at the start of the owner's
  turn", and T-TURN-01(e) names the same moment. **Unconstrained command
  ordering** is present too: T-TURN-01 reads "IN EITHER ORDER" and its clause
  (b) asserts that an attack-then-move by one unit completes. Both were filed
  as missing from Stub 5's invariant text and both are there. No edit.
- **§4.10's Policies list** stands unedited, and Pair 16 is written so it can:
  the *Mid-match saves* bullet calls a waiting build and capture-in-progress
  derived pending state — derived from the **log** — and both are hashed.
- **§4.4's week-2 cell** — "every field of the §4.10 hash is an integer except
  the transients inside `resolveDamage`" — survives Ruling D, because the
  added flags are hashed as 0 or 1, and Ruling E, because `spawnBlocked`
  enters no hash. Its "which `Attack` already reaches" survives too: `Move`
  sets `hasMoved` and `Attack` sets `hasActed`, so the week-2 `{Move, Attack}`
  log exercises both added per-unit fields. The per-factory record needs
  `Build`, which arrives with rows 4–5 — the same re-opening §4.4 and §4.11
  row 9 already state, so neither moves.
- **§4.9's parity-gate paragraph** and **§4.11's † bullet for T-INT-02, 05 and
  T-SAVE-06** describe what the parity pair proves, and neither is falsified:
  the widened hash adds integer fields to a comparison that already ran, so
  the compiler-divergence class those gates catch is unchanged, and Ruling E
  reaches neither, since it adds no hashed field.
- **Stub 5's "the §4.10 hash is taken from this state"** stays true — the hash
  additions are Stub 5's own state. `spawnBlocked` is not Stub 5 state and is
  not hashed.
- **The view-model split's other sites.** Grepping *view model* and
  *view-model* in both spellings returned one unpaired site, §3's driver
  sentence (Pair 2b). §4.1's *Presentation layer*, §4.4's week 2, §4.9's
  *Presentation submits commands* and §4.11 row 9's *Presentation bridge* name
  the presentation layer rather than the view-model, and none claims that
  layer holds no state of its own; §4.1's "never own rules" is unaffected,
  since the presentation block holds no rule. Two further hits for
  `presentation` are inside the word *representation* (§4.7 Q10, §4.8).
- **§4.7's open-question register** gains no row and loses none. Q31 is
  untouched: Pair 9 records where a Q31 ruling would land and rules nothing.
- **Row 8's ledger row stays `*pending*`**, and no §3 count of verified rows
  moves. Ruling E mints no acceptance ID.

## Filed for the Director — §2 sites this round reaches, not paired here

`ux-onboarding-designer` owns §2.11 this round and is writing the DONE-bit,
BUILD-pulse and income-rate half there, in the same two terms — **view-model**
and **presentation block** — and is rebinding §2.11.5's boxed-in footer to
`spawnBlocked`. Observations, filed rather than paired:

1. §2.11.2's hovered-unit line and its unacted-pip row already bind to
   §2.11.1's DONE bit rather than to a raw flag, which is what Ruling A
   ratifies. Nothing there is falsified; whether either restates the binding
   in view-model terms is §2.11's call.
2. §2.11.2 names an income rate on the HUD. Ruling C gives it a snapshot
   field (`incomePerTurn`); which surface displays it, and how, is §2.11's.
3. §2.11.5's disabled Build buttons and its `Boxed in — build waits for a
   free hex.` footer are what Ruling E's `spawnBlocked` exists to feed. Stub 8
   now carries the field; the binding is §2.11.5's and is not written here.

Nothing else in §2 is falsified by these rulings. Neither §2 use of
*presentation* is the view-model's — §2.11.2's turn banner names presentation
pacing — and no §2 sentence quantifies over acceptance IDs or over what row 8
lacks.

## Open questions for the Director

- **Change request — where the guided opening's marked/locked state lives,
  and whether T-INT-05 reaches it.** §4.7 Stub 7 keeps that state out of
  Stub 8's snapshot and has the guidance layer read it from the loaded
  scenario directly. That was a complete disposition while Stub 8 held only
  rules-produced fields. It is no longer, because T-INT-05 now asserts that
  rebuilding from the **view-model alone** reproduces every displayed value,
  and the marked Infantry and its locked state are displayed (§2.11.6) while
  sitting in neither half of the view-model. This is the shape of the problem
  Ruling A was made to fix for the DONE bit, at a second site with a different
  owner. Three dispositions are visible — admit it to the presentation block
  under a second owner; leave it outside and narrow T-INT-05's subject; or
  leave both as they stand and accept that one displayed value is outside that
  gate — and **none is taken here**. Bounding the block by ownership, which is
  what this round did, keeps every sentence in the document true and decides
  none of the three. Q27 and Stub 7's note are untouched for the same reason.
- **What `incomePerTurn` reads on turn 1.** §2.7 pays no income on turn 1
  (Q8(a)), so on turn 1 the field is either the rate that will pay at the
  start of turn 2 or the 0 that pays now, and the two differ on the one turn a
  new player is most likely to read it. T-UI-05 compares the field against the
  derivation the stub states, and the stub states §2.7's rate — so under the
  second reading the gate would be asserting the wrong thing rather than
  failing usefully. The display is §2.11's; the rule is stated nowhere.
- **Whether §2.8 states the two older derived fields precisely enough to
  gate.** T-UI-05 clause (b) asserts each declared derived field against its
  stated derivation. `incomePerTurn` and `spawnBlocked` carry formulas at the
  stub; `objectivesHeld X of N` and `survivingHP` carry a pointer to §2.8's
  criteria instead, which is where they have always been defined. If the
  Director wants clause (b) to bind on those two as tightly as on the new
  ones, the two derivations need writing out — I have not written them, since
  doing so would be inventing a rule §2.8 states in its own words.
- **T-UI-05 has no owner in the calendar.** §4.4 schedules no work after row
  8's landing that would implement it, and rows 9–10 are the next scheduled
  work. The ID is written and asserting and nothing in §4.4 says when it runs.

## Grounding

- Rulings A–E, and the vocabulary **view-model** / **presentation block** /
  **declared derived**: Director, 2026-08-04, as relayed to this round.
- The three module-side sources a mirror may draw on, and the subject T-UI-05
  asserts over — the authoritative `strat::GameState`, the loaded
  `strat::UnitDef` / `strat::TerrainDef` / effectiveness tables, and
  `strat::loadScenario` on the scenario asset: §4.9's bridge bullet, which
  lists them separately.
- `hpMax` as the `data/units.csv` `HP` column loaded into `strat::UnitDef`,
  and `unitId` as that table's row key: §4.8's unit schema.
- `turnCap` as per-scenario data in Stub 7's field: Q7, ruled. Terrain per hex
  and factory placement as scenario-file content: §4.7 Stub 7.
- The presentation block's owner and its per-unit DONE bit: §2.11.1's
  selection machine and its "What DONE means" paragraph.
- The guided opening's marked/locked state as presentation state read from the
  loaded scenario and kept out of Stub 8: §4.7 Stub 7's `guidedOpening` field
  note; Q27's dependency column.
- `hasMoved`/`hasActed` as two independent snapshot fields, DONE reachable
  without spending the act flag: §4.7 Stub 8's per-unit note; §2.11.1.
- T-TURN-10's per-factory build record and its renewal boundary: §4.7 Stub 5,
  T-TURN-10 and T-TURN-01(e).
- The spawn rule `spawnBlocked` derives from — spawn on the factory hex if
  free, else an adjacent free hex, else the build waits: §2.7's build-and-spawn
  bullet.
- A waiting build and capture-in-progress as *derived pending state*, derived
  from the log: §4.10 Policies, "Mid-match saves". `captureProgress` and
  `pendingBuilds` in the hash, and `scenarioHash` as a header field: §4.10's
  canonical-state-hash paragraph and file-layout table as they stand.
- Income rates (+100 factory, +25 town), no accrual on turn 1: §2.7, Q8(a).
- `objectivesHeld X of N` and `survivingHP` as §2.8's tiebreak criteria 2
  and 3; the capture-in-progress edge case as GATE-CAP-PARTIAL: §2.8, §4.7
  Stub 8.
- The debug driver's `snapshot` command and `GATE-DRV-01..12` at `7c36303`:
  §3's row-8 landing record.
- Row 8's gate — T-UI-01, T-UI-02, GATE-CAP-PARTIAL, 14/14 under clang++ and
  MSVC — and the absent in-editor pass: §3's row-8 landing record and the
  ledger's UI evidence cell, both at `7c36303`.
- Counts 70 / 52 / 18 before this round, and the 16 IDs in rows 8–10: §4.5's
  risk row and §4.11's rows 8, 9 and 10.
- GATE-AI-SMOKE and GATE-CAP-PARTIAL minting no ID: §3's row-6 and row-8
  landing records; §4.7 Stub 8's GATE-CAP-PARTIAL entry.
- Q29's per-ID reading, which is what keeps row 8 unflipped on T-UI-05:
  §4.7 register, Q29.
- Saves accepted between atomic commands during the player's turn: §4.10
  Policies, "Save points".
- No code implements T-UI-05, the per-factory block, `incomePerTurn`,
  `spawnBlocked` or the widened hash — stated as of crew `main` `7c36303`, the
  commit row 8's record cites. No commit is claimed for any of them.
