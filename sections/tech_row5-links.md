# Technical design — row5-links addendum (tech-director)

> ## ✅ APPLIED ADDENDUM — DO NOT RE-APPLY
>
> All five pairs were merged into the master GDD on 2026-08-03.
> Master md5 `5bad314bcb34e52a88bff92727f5fcc5` →
> `f5284420e237b1cbedbf3fd7d46f0988`.
>
> Gate: run `row5-links-2`, **PASS**, 0 violations, after `row5-links-1`
> (BLOCK, 1 — a `contradiction`: a derivation sentence claimed the §4.5
> green-count list was bare for every commit, and `9086d6a` is linked inside
> that very list; its own parenthetical entailed the link, so it was
> self-refuting). Fixed by **deleting** the paragraph outright, substituting
> nothing — the correct statement of the fact already stood elsewhere in the
> file.
>
> **All five pairs are replacements. None is an insertion**, so no OLD anchor
> survives on the merged master. Every OLD was verified against the **master**
> before anything was written, each matching exactly once, and the apply refused
> to write unless all five did.
>
> **What this round did:** removed the citation exception the `row5-rebuild`
> addendum created. That exception was correct when written — `6ccd40b` was
> unpushed and no link to it would resolve — and it expired when the commit was
> pushed. `6ccd40b` now carries **4 linked citations and 10 bare mentions**,
> matching how its sibling commits are cited; the three exception sentences and
> the lead-in's pointer to them are deleted, and the parenthetical's *links*
> reverted to *cites*.
>
> **No commit in this document is linked at every mention** — every one is cited
> in both forms. An earlier orchestrator recommendation to "relink all 16" rested
> on a raw string count (a linked citation contains the sha twice) and would have
> made `6ccd40b` the only commit linked everywhere, replacing one exception with
> another. It was corrected before the author was briefed.
>
> §2 was **byte-identical across this merge** (103,435 chars, compared as
> strings), so `kb/rules.md` needed no re-sync.

## Placement

Addendum to the merged master. Base document: `source/gdd.md`, md5
**`5bad314bcb34e52a88bff92727f5fcc5`**. Nothing here redrafts a section; every
change is an exact `OLD` → `NEW` pair.

**5 pairs. 5 replacements, 0 insertions.** Classification is the substring-prefix
test run on the final bytes below — for each pair, does `NEW` contain its `OLD`
verbatim as a prefix? For all five it does not, so all five are replacements.

Placement by pair:

| # | Line in base | Structural site |
|---|---|---|
| 1 | 1511 | §3 provenance-ledger lead-in, *Status* italic — the head-commit clause and the link-exception pointer |
| 2 | 1511 | §3 lead-in — the **Row 5 was then rebuilt** landing announcement |
| 3 | 1520 | §3 ledger table, **Turn loop & win / tiebreak** evidence cell |
| 4 | 1528 | §3 paragraph below the table — row 5's closure-commit evidence sentence |
| 5 | 1528 | §3 paragraph below the table — the link-resolution parenthetical |

Every `OLD` was verified to match **exactly once document-wide** by
`rg -o` on the base file, counting occurrences rather than matching lines
(a bare `` `6ccd40b` `` occurs sixteen times, so occurrence counting is the only
check that means anything here).

---

## Draft

### Where the links go, and why those four sites

`6ccd40b` is given a link at the sites its sibling commits carry one, and left
bare at the sites they are bare. The pattern was derived from the document, not
assumed. Measured across `647d4df`, `ad77b13`, `d8284f1` and `9086d6a`, three
structural positions carry a link every time:

1. the §3 lead-in's **landing announcement** — *"Row N then landed, at
   [`X`](…)"*;
2. the §3 ledger table's **evidence cell** — `@ [`X`](…)`, true of every cell
   in the table;
3. the **paragraph below the table**'s per-row evidence sentence — *"<System>
   joined at [`X`](…)"*.

That yields four link sites for `6ccd40b` — the head-commit clause in the
*Status* line, whose immediate neighbour `9086d6a` is already linked in the same
clause as its parent; the landing announcement; the evidence cell; and row 5's
closure-commit sentence below the table, which is the sentence carrying row 5's
verification evidence in the position *"joined at [`X`]"* occupies for every
other row. Ten mentions stay bare. Two are deleted with the exception.

After the patch `6ccd40b` reads **4 linked / 10 bare**, which is the same shape
as `647d4df` (3/6), `ad77b13` (3/7) and `d8284f1` (3/6). It is no longer the one
commit with zero links, and it is not made the one commit linked everywhere.

## Pair 1 — §3 lead-in, *Status* line

Links the head commit and deletes the pointer to the exception. The pointer's
referent is deleted by pair 5, so the pointer goes with it rather than dangling.

**OLD**

```
at commit `6ccd40b` in the crew repo, whose parent is [`9086d6a`](https://github.com/jakemartin/stratocracy-crew/commit/9086d6a); `6ccd40b` is cited without a link, for the reason the paragraph below the table gives.
```

**NEW**

```
at commit [`6ccd40b`](https://github.com/jakemartin/stratocracy-crew/commit/6ccd40b) in the crew repo, whose parent is [`9086d6a`](https://github.com/jakemartin/stratocracy-crew/commit/9086d6a).
```

## Pair 2 — §3 lead-in, the landing announcement

The position at which `647d4df`, `ad77b13`, `d8284f1` and `9086d6a` are each
linked.

**OLD**

```
**Row 5 was then rebuilt**, at `6ccd40b`,
```

**NEW**

```
**Row 5 was then rebuilt**, at [`6ccd40b`](https://github.com/jakemartin/stratocracy-crew/commit/6ccd40b),
```

## Pair 3 — §3 ledger table, row 5's evidence cell

Every other evidence cell in the table links its commit. The cell's second
mention of `6ccd40b` — *"`6ccd40b` is the rebuild at which the **full** set
closes"* — stays bare: it is a back-reference within the cell, and the cell's
citation slot is the linked one.

**OLD**

```
`cpp_reference/test_turn.cpp` @ `6ccd40b` · T-TURN-01..10, all ten closing
```

**NEW**

```
`cpp_reference/test_turn.cpp` @ [`6ccd40b`](https://github.com/jakemartin/stratocracy-crew/commit/6ccd40b) · T-TURN-01..10, all ten closing
```

## Pair 4 — §3 paragraph below the table, row 5's closure commit

Row 5's *"joined at"* slot is held by `ad77b13`, already linked; this is the
sentence that carries the commit row 5's acceptance set actually closes at, and
it is the paragraph's first mention of it. The later *"closes at one commit —
`6ccd40b`, not `ad77b13` —"* stays bare, where `ad77b13` is bare too.

**OLD**

```
green at the `6ccd40b` rebuild under clang++ and MSVC both, on **11 printed checks over those ten IDs**.
```

**NEW**

```
green at the [`6ccd40b`](https://github.com/jakemartin/stratocracy-crew/commit/6ccd40b) rebuild under clang++ and MSVC both, on **11 printed checks over those ten IDs**.
```

## Pair 5 — the link-resolution parenthetical: the exception is deleted

Three sentences go and one word reverts.

The word: last round narrowed the claim from every commit this section **cites**
to every commit it **links**, solely so the unlinked `6ccd40b` would not falsify
it. With the exception gone the narrowing has no purpose, and the wider claim is
the one that is **true of the post-patch document**: §3 cites `5ffa8d6`,
`c224825`, `9f87ecd`, `647d4df`, `ad77b13`, `d8284f1`, `9086d6a` and `6ccd40b`,
and every one of them is reachable from the head of `main`, which is `6ccd40b`
itself. The consequent — *so every commit link above resolves* — is unchanged
and is the operative claim. The three deleted sentences are not restated
anywhere; there is nothing left to maintain.

**OLD**

```
*(Every commit this section **links** — `d8284f1`, row 6's, included — is reachable from the head of `main` in the crew repo, so every commit link above resolves. **`6ccd40b`, row 5's rebuild, carries no link anywhere in this section**: it is committed on `main` and not yet pushed, so it is reachable in the working repository and not on GitHub, and the section states the commit rather than a link that would fail. Pushing it is what makes the link form available, and this sentence is the only one that has to move when it does. The **file** paths resolve too,
```

**NEW**

```
*(Every commit this section **cites** — `d8284f1`, row 6's, included — is reachable from the head of `main` in the crew repo, so every commit link above resolves. The **file** paths resolve too,
```

## Sites deliberately left alone

- §4.5's *Specification outruns the build* cell, both mentions — *"**green at
  `6ccd40b`**"* and *"**1** at `6ccd40b`"*. In that cell `c224825`, `647d4df`,
  `ad77b13` and `d8284f1` are all bare and only `9086d6a` is linked; the
  majority form is bare, so `6ccd40b` is bare. Linking it there would join an
  anomaly rather than a convention. Filed as an open question below.
- §4.11's build-order lead-in, *"row 5 at `6ccd40b` — its rebuild…"*. Every
  commit named in that passage is bare.
- The five remaining running-prose mentions in the §3 lead-in and the second
  mention in each of the ledger cell and the paragraph below it, as set out
  above.

## Scope item 4 — the search for other push-state or link-form claims

I did not trust last round's claim that the parenthetical was the only such
site; I re-ran it against the merged document, over the whole file rather than
§3, for `push`/`pushed`/`unpushed`, `GitHub`, `working repository`, `carries no
link`, `without a link`, `reachable from`, and `resolves`.

Two sites assert anything about `6ccd40b`'s push state or link form: the §3
lead-in pointer (pair 1) and the parenthetical (pair 5). No third site exists.

## Build order

No build-order row moves in this round. `6ccd40b` is row 5's rebuild commit and
its acceptance set (`T-TURN-01..10`, 11 printed checks over ten IDs) is
unchanged by a citation edit.

| # | System (ledger row) | Depends on | Headless? | Acceptance test IDs |
|---|---|---|---|---|
| — | none | — | — | none — citation form only, no evidence claim moves |

## Change requests

| Existing § | Current text | Proposed change | Why |
|---|---|---|---|
| — | — | none | Every edit this round is inside a pair above; no number, rule or evidence claim changes. |

## Open questions for the Director

1. **§4.5's green-count list is internally inconsistent about link form, and
   this round does not fix it.** In that one cell `9086d6a` is linked while
   `c224825`, `647d4df`, `ad77b13` and `d8284f1` are bare. I left `6ccd40b`
   bare there to match the majority, but the cell will keep attracting this
   question until it is uniform in one direction. Same for `9086d6a`'s link at
   §2.13's Q32 registration (line 2504), which is the only commit link outside
   §3 and §4.5.
2. **The parenthetical's aside *"— `d8284f1`, row 6's, included —"* is kept and
   is still true, but it singles out a commit that is no longer the newest one
   §3 cites.** I did not touch it, because it asserts nothing false and this
   round prefers deletion to restatement — but if it was written to name the
   most recent landing, it is now stale in intent rather than in fact, and the
   fix is to delete the aside, not to renumber it.

## Handoffs

None. This round touches citation form in §3 only; no rule, map, screen or
schema is affected.

## Grounding

- Link sites and bare sites for `647d4df`, `ad77b13`, `d8284f1`, `9086d6a`,
  `c224825`, `5ffa8d6` and `9f87ecd`: measured on `source/gdd.md` at md5
  `5bad314bcb34e52a88bff92727f5fcc5`, lines 1511, 1515–1525, 1528, 1582, 2504,
  2743–2745.
- The sixteen mentions of `6ccd40b`: eight at line 1511, two at 1520, three at
  1528, two at 1582, one at 2744.
- `main` in `stratocracy-crew` is at `6ccd40b` and is pushed; the commit page at
  `https://github.com/jakemartin/stratocracy-crew/commit/6ccd40b` was fetched
  and resolves unauthenticated — supplied as a verified fact for this round, not
  inferred by me from the push.
- Row 5's evidence (`T-TURN-01..10`, 11 printed checks over ten IDs, clang++ and
  MSVC both, at `6ccd40b`) is quoted from §3 as already merged; this round adds
  no evidence claim.
