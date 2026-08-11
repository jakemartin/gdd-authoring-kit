# Ruling — the ledger does not need a reading point

**Ruled by the Director, 2026-08-11.** Closes open question 1 of the
`stamp-scope` addendum (`sections/tech_stamp-scope.md`, gated PASS at run
`stamp-scope`, committed `d8e200d`).

This record is **kit-local bookkeeping**. It is not master content, and nothing
here has been written into the GDD. If the ruling should appear in the master,
that is a future addendum's work. **The gated draft was not edited to mark this
question answered** — it is sealed against the accept record and editing it would
break that match.

## The question as filed

> **Does the ledger need a reading point at all, and if so what encloses it?**
> Pair 1 disclaims one rather than moving one, because none can be established
> from what was measured: the enumeration behind the eleven late commits sees
> `\b[0-9a-f]{7}\b` tokens only, so it is a floor and not a ceiling, and a
> re-pin to any later pair of shas would assert an enclosure over text the
> probe cannot see. If a reading point is wanted, the rule for establishing one
> — what must be shown to be an ancestor of what, over which set of citations —
> is yours to write, and I will write the gate for it.

## The ruling

**The ledger does not need a reading point.**

Consequences, stated so they are not re-derived:

1. **Pair 1's form stands.** Disclaiming the scope rather than moving it is the
   ruled outcome, not merely the option the author preferred.
2. **The re-pin stays rejected**, and the reason no longer needs re-arguing: no
   pair of shas is to be asserted as enclosing the block.
3. **No gate is owed for establishing a reading point.** The author offered to
   write one if a rule were wanted; no rule is wanted, so that offer lapses.

## What the ruling does not close

Open questions **2** and **3** of the same addendum remain open and unruled.

## A clause the ruling reaches, filed so it is not re-discovered

MEASURED against `source/gdd.md` md5 `1f27e981b623c7af2f6402d9a5b6a62b`, on a
whitespace-collapsed copy, control-tested against a known-absent variant (0 hits):
the phrase `the §3 status line above` occurs **3** times, all on line 1533 and all
inside one parenthetical.

| Site | Status |
|---|---|
| `it matches the §3 status line above, whose substance is unchanged` | repaired by Pair 3 |
| `which is the defect the §3 status line above records` | untouched by Pair 1; survives |
| `each commit cited since is pinned at the landing that cites it, and the §3 status line above **carries that pinning**` | **no pair repairs it** |

The third turns on a verb the round never disambiguated, and it bears two
readings:

- **Exhibits** — each commit the status line cites is pinned at its own landing.
  This is the author's reading (*"Pair 1 leaves it standing and does not lean on
  it"*). On it, Pair 1 is consistent and nothing is owed.
- **Supplies** — the status line furnishes the pin for commits cited since
  `ec15be6`. On this reading the clause *is* a reading point, and Pair 1
  falsifies it, since Pair 1's replacement states the line dates its own reading
  and nothing else.

**Which was meant is a question about intent and was not measured.** What the
ruling settles is that the second reading is no longer a legitimate option going
forward, so the clause should not be left able to bear it.

**This belongs with open question 2, not in a round of its own.** Question 2 asks
whether `each commit cited since is pinned at the landing that cites it` is a rule
or a measurement; the `carries that pinning` clause is the second half of that same
coordinate structure. Repairing one half without the other is how a repair makes
the other false — the shape that cost four gate runs in an earlier round.

**No replacement prose is offered here.** The defect is named; whoever authors the
repair measures the site.
