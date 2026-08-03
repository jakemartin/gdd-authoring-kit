> ## ✅ APPLIED ADDENDUM — DO NOT RE-APPLY
>
> All four pairs were merged into the master GDD on 2026-08-02.
> Master md5 `94c67ebe95a09414485cc2a07822f9b5` → `cc07e1f0db78b4955059933520194360`.
>
> Gate: run `t-cap-alias-4`, **PASS**, 0 violations, after three blocking runs
> (`-1` BLOCK 2 → `-2` BLOCK 3 → `-3` BLOCK 1 → `-4` PASS).
>
> All four pairs are **replacements**, none an insertion: pair 2 splits its OLD
> anchor around the new map, so the anchor does not survive. Post-check on the
> merged master: every NEW present exactly once, every OLD present zero times.
>
> `kb/rules.md` was **not** re-synced. §2 changed (96,921 → 98,194 chars), but
> the delta is gate-ID glossing only — no number, threshold, or rule — and
> `kb/rules.md` contains no `T-CAP` or `T-TURN` identifier.

# Rules — T-CAP alias ruling addendum (rules-designer)

Four replacement pairs recording the Director's ruling that **`T-CAP` is an
alias for `T-TURN`**. Two are in **§2.8**, one in **§2.0**'s PX table, one in
**§4.7**'s Q register. Nothing is renumbered: §2.8 keeps T-CAP-01..08.

---

## Pair 1 — §2.8, the invariants lead-in

**OLD**
```
*Invariants (each phrases directly as a `T-CAP-` test):*
```
**NEW**
```
*Invariants. `T-CAP-01..08` is §2.8's own numbering for the procedure §4.7
Spec Stub 5 gates as `T-TURN-01..09`, so there is one suite, not two. The map
below names, for each invariant, the ID or IDs that gate it; one row names
none.*
```

## Pair 2 — §2.8, the alias map, after item 8

Insertion. The T-CAP-08 item and the delete-test blockquote are retained as
anchors; the map goes between them.

**OLD**
```
8. **T-CAP-08** — Controlling every factory at the start of your turn ends the
   match immediately as a Decisive win; towns do not count toward domination.

> **Why this shape (the delete-test).** Every piece of the apparatus was
```
**NEW**
```
8. **T-CAP-08** — Controlling every factory at the start of your turn ends the
   match immediately as a Decisive win; towns do not count toward domination.

*Alias map — the ID or IDs that gate each invariant above; one row names none:*

| §2.8 | Aliases to | Why |
|---|---|---|
| T-CAP-01 | **T-TURN-02** | flag death ends the match at once; the tiebreak is never evaluated |
| T-CAP-02 | **T-TURN-05** | the mutual-passivity guard |
| T-CAP-03 | **T-TURN-05** | T-TURN-05's fixture is 4 objectives + zero kills losing to 1 objective + one 50-Fame kill. That combat Fame excludes passive income is **T-FAME-01** |
| T-CAP-04 | **T-TURN-02** | no capped tally can contain the +500, because a flag kill ends the match before the cap |
| T-CAP-05 | **nothing** | see below |
| T-CAP-06 | **T-TURN-07** | tiers are categorical |
| T-CAP-07 | **T-TURN-09** | determinism |
| T-CAP-08 | **T-TURN-03** | domination, factories only |

**T-CAP-05 is the exception.** No `T-TURN-` ID asserts it. It is discharged
*structurally* by T-FAME-05 and T-FAME-06 — an objective's owner does not
change until the capture completes, and the tally counts owners — but **no
gate asserts it end to end, and it appears in no acceptance set.**

> **Why this shape (the delete-test).** Every piece of the apparatus was
```

## Pair 3 — §2.0, PX-4's Observable check cell

Single table line.

**OLD**
```
| PX-4 | Fighting is always better than hiding. There is no line of play where sealing a corner and running the clock wins. | §2.7, §2.8 | A side with zero combat Fame never wins a capped match (T-CAP-02, T-CAP-03). |
```
**NEW**
```
| PX-4 | Fighting is always better than hiding. There is no line of play where sealing a corner and running the clock wins. | §2.7, §2.8 | A side with zero combat Fame never wins a capped match (T-CAP-02, T-CAP-03 — both gated as **T-TURN-05**). |
```

## Pair 4 — §4.7, Q14's Blocks cell

Single table line.

**OLD**
```
| **Q14** | Capture-in-progress at the cap. Does a partially captured objective count toward "objectives held" (§2.8 criterion 2)? | T-CAP-05; the kb victory table | It counts for nobody until the objective flips — §2.7's flip-on-capture wording grants nothing before the flip. Partial credit would need a fractional-count rule and would invert T-CAP-05. |
```
**NEW**
```
| **Q14** | Capture-in-progress at the cap. Does a partially captured objective count toward "objectives held" (§2.8 criterion 2)? | T-CAP-05 — the one `T-CAP-` ID with no `T-TURN-` counterpart and no gate of its own (§2.8's alias map); the kb victory table | It counts for nobody until the objective flips — §2.7's flip-on-capture wording grants nothing before the flip. Partial credit would need a fractional-count rule and would invert T-CAP-05. |
```

---

## Placement

| Pair | Section | Exact site |
|---|---|---|
| 1 | §2.8 | The italic invariants lead-in, immediately above item 1 |
| 2 | §2.8 | Between list item 8 and the delete-test blockquote (insertion) |
| 3 | §2.0 | The PX table, PX-4's *Observable check* cell |
| 4 | §4.7 | The Q register, Q14's *Blocks* cell |

Pairs 1 and 2 are disjoint spans of §2.8 and apply in any order. No pair
touches §3, §4.5, §4.11, §4.7's register-head paragraph, or any Q row other
than Q14.

## Grounding

Every **OLD** block was grepped against `source/gdd.md` (md5
`94c67ebe95a09414485cc2a07822f9b5`) and returns **exactly one** match. The
alias map in pair 2 is the Director's verified mapping, checked against §4.7
Spec Stub 5's T-TURN-01..09 text and the shipped gate `cpp_reference/test_turn.cpp`
at `ad77b13`; it is transcribed here and neither re-derived nor extended.
T-CAP-03's row rests on T-TURN-05's own fixture, read off that file, and names
T-FAME-01 — §4.11 row 4 — for the passive-income half. T-CAP-05's structural
discharge is read from T-FAME-05 and T-FAME-06; the negative beside it — no
gate, no acceptance set — is the Director's grep of the identifier across the
whole document. Pairs 3 and 4 cite only IDs the map supplies.

## Open questions for the Director

1. **T-CAP-05 has no gate and no acceptance-set home.** Pair 2 records that as
   a standing gap rather than closing it. Whether it gets an asserting test is
   a Director call — plausible homes are row 8's Stub 8 snapshot and a row-4
   fixture. This blocks nothing in the merge; it blocks any future claim that
   §2.8 is fully gated.

## Change requests

None. No number, threshold, or rule changes; the ruling is an alias.

## Handoffs

None owed. No pair states a new rule, map fact, screen layout, or schema.
