# Technical design — t-cap-05-and-rebuild addendum (tech-director)

> ## ✅ APPLIED ADDENDUM — DO NOT RE-APPLY
>
> All four pairs were merged into the master GDD on 2026-08-04.
> Master md5 `d2cfe86d6decad525a9a002d3f2c17b8` →
> `a5c266b921ea3ea7a3ce79c89137cc66`.
>
> **All four pairs are replacements. None is an insertion**, so no OLD anchor
> survives on the merged master. The classification was re-derived from the final
> bytes after the remediation round. Every OLD was verified against the
> **master** before anything was written, each matching exactly once, and the
> apply refused to write unless all four did.
>
> Gate: run `t-cap-05-rebuild-2`, **PASS**, 0 violations, after
> `t-cap-05-rebuild-1` (BLOCK, 2 — both inside Pair 3's NEW cell).
>
> **The blocking `contradiction` was the orchestrator's bad fact, not the
> author's.** The brief supplied "`T-SCN-08` (c) … **was accepted as closing**",
> and T-SCN-08 does **not** close — §3 records it as having run part of its
> fixture set, and §4.5 counts it among the 18 unclosed, a figure this addendum's
> own Grounding derives correctly. The same false claim had propagated into a
> Grounding bullet and was corrected there too. **The ruling survives on the
> corrected precedent and rests on it better:** what fixture (c) establishes is
> that a synthetic fixture is legitimate where the stub calls for one **and
> counts when it runs**, while T-SCN-08 stays open for an unrelated reason — its
> fixtures (a) and (b) need an unauthored stretch map. That contrast is the
> argument: `GATE-CAP-PARTIAL` has one written fixture and it ran, so no part of
> its set is outstanding. The second violation was a `dead-reference` — "the row
> above it", written inside Q14's own cell, denotes Q13.
>
> **What this round did — two Director rulings, both closing questions the
> document recorded as unruled.**
>
> **Ruling 1: T-CAP-05 closes. It is green at `7c36303`.** `GATE-CAP-PARTIAL`
> passed there under clang++ and MSVC both, on a fixture configured with
> `captureTurns = 2`. The invariant's own text entails N ≥ 2 — it raises a unit's
> `captureProgress` *short of completion*, a state that does not exist at N = 1 —
> so that fixture is the configuration the invariant is about, not a stand-in for
> a map nobody authored. N is per-scenario data (§2.7), not a constant.
> **This rules the closure sub-question only**: Q14's own rules question keeps
> its stated reading and stays open, so the register's **15-ruled / 17-open**
> counts do not move. **No §4.5 figure moves either** — the 70 is scoped
> §4.7–§4.11 and decomposes as 52 green + 18 unclosed with T-CAP-05 in neither,
> it being §2.8's numbering and the one ID that aliases onto no `T-TURN-`
> counterpart.
>
> **Ruling 2: a behaviour-changing rebuild re-opens §4.4's "Playable via debug
> commands", and the goal was met again at `6ccd40b`.** §3's rule re-opened the
> goal at each system that *lands*, and a rebuild is not a landing, so the rule as
> first written did not reach one. Row 5's rebuild changed what a human can reach
> at the REPL: before it, `move` and `attack` spent one shared flag, so §2.1's
> move-and-act sequence was unimplementable there. **Row 8's own landing at
> `7c36303` is met again and deliberately unwritten**, on the rows-6 and -7
> precedent, because §3's standing rule already produces it.
>
> **§2 changed again** — Pair 1 edits §2.8's T-CAP-05 exception block, 8,414 →
> 8,449 chars — and **`kb/rules.md` again needed nothing**, decided by reading
> it: the KB contains **no gate-status vocabulary at all** (zero hits for
> *green*, *asserting*, *unruled*, *not run*, `T-CAP-`, `GATE-`). It carries the
> rule; this round changed only a gate's status.

## Placement

An addendum against `source/gdd.md` at md5 `d2cfe86d6decad525a9a002d3f2c17b8`.
It redrafts no section. Four exact OLD/NEW pairs, each OLD verbatim in
`source/gdd.md` and each anchoring uniquely (verified by literal search, one hit
per pair). All four are **replacements**; there are **no insertions**.

Sites: §2.8 (the T-CAP-05 exception paragraph), §4.7's register preamble, §4.7's
**Q14** register row, and §3's provenance-ledger status paragraph.

Ruling 1 is recorded in full **once**, in Q14's own row. §2.8 and the §4.7
preamble state the closure and point there.

---

## Draft

### Pair 1 — §2.8, the T-CAP-05 exception paragraph

The sentence that asserts the closure question is open.

**OLD**

```
**Whether that closes T-CAP-05 is unruled** (§4.7, Q14).
```

**NEW:**

```
**That closes T-CAP-05** — ruled 2026-08-04; the reasoning is recorded once, at
§4.7's Q14.
```

### Pair 2 — §4.7, register preamble

The same assertion in the preamble's T-CAP-05 exception clause. The two
sentences either side of it — that `GATE-CAP-PARTIAL` mints no acceptance ID and
that no §4.5 count moves on its account — are true after the ruling and are left
untouched (see **§4.5 arithmetic** below).

**OLD**

```
and whether T-CAP-05 itself closes on a fixture no
shipped map can reach is unruled (Q14).
```

**NEW:**

```
and **T-CAP-05 closes there**, ruled
2026-08-04 (Q14).
```

### Pair 3 — §4.7, register row **Q14**, Blocks column

The ruling's home. The OLD ends at the column's next list item (`the kb victory
table`), which the NEW preserves so the cell's structure is unchanged.

**OLD**

```
Whether T-CAP-05 closes on a fixture no shipped map can reach is not ruled here; the kb victory table
```

**NEW:**

```
**T-CAP-05 closes at that commit — ruled 2026-08-04.** The fixture is the configuration the invariant is about, not a stand-in for a map nobody authored: the invariant raises a unit's `captureProgress` *short of completion*, a state that does not exist at N = 1, so its own text entails N ≥ 2. N is per-scenario data (§2.7) rather than a constant, so a rule that governs every scenario is properly gated at a value that rule is about, and a synthetic fixture is legitimate exactly where the stub calls for one and counts when it runs — the precedent is **T-SCN-08 (c)**, whose stub asks for a scenario whose lanes both cost 7 and names no map, and which ran and was counted at `9086d6a`. T-SCN-08 itself does not close, on fixtures (a) and (b), which need a stretch map nobody has authored — and that contrast is what carries this ruling: `GATE-CAP-PARTIAL` has **one** written fixture and it ran, under clang++ and MSVC both, so no part of its set is outstanding and Q29, read per ID, is satisfied here where it is not satisfied there. **This rules the closure only, and not Q14's own rules question** — whether a partially captured objective counts toward "objectives held" — which keeps the stated reading in the next column and stays open; the kb victory table
```

### Pair 4 — §3, provenance-ledger status paragraph

Ruling 2. One edit: the existing re-opening rule gains the rebuild case, and the
goal is recorded as met again at `6ccd40b` on that account.

**OLD**

```
The goal is therefore **provisionally met** — met against the feature set that existed at the commit it was ruled on, and **re-opened by each system that lands after it**, rows 5–8 included. The bare word *met* is a current-state acceptance and not a permanent closure.
```

**NEW:**

```
The goal is therefore **provisionally met** — met against the feature set that existed at the commit it was ruled on, **re-opened by each system that lands after it**, rows 5–8 included, and **re-opened equally by a rebuild of an already-landed row that changes what a human can reach at the REPL** (ruled 2026-08-04: a rebuild is not a landing, so the rule as first written did not reach one). On that second account the goal was **met again at [`6ccd40b`](https://github.com/jakemartin/stratocracy-crew/commit/6ccd40b)**, where the move/act split into two independent per-unit flags made §2.1's *move and act, in either order* reachable at the REPL for the first time; before it the two commands spent one shared flag, so that sequence was unimplementable there. The bare word *met* is a current-state acceptance and not a permanent closure.
```

---

## Build order

Unchanged by this round. No milestone, dependency, acceptance set or ledger row
moves. The §4.11 row-8 cell below is reproduced **verbatim from the master** and
no pair in this round edits it; row 8 stays unflipped on T-UI-03 and T-UI-04,
which have not run.

| # | System (ledger row) | Depends on | Headless? | Acceptance test IDs |
|---|---|---|---|---|
| 8 | UI binding (Stub 8) | 5, 7 (snapshot needs full state) | Contract + queries yes; widgets in-editor | T-UI-01..04 (**T-UI-03, 04 †**) + GATE-CAP-PARTIAL |

## Change requests

None. Both rulings are recorded where the document already carried the question;
neither needs a rule the GDD does not state.

## Open questions for the Director

1. **Does Ruling 1 flip Q14's own row status?** I read it as ruling the closure
   sub-question, not Q14's rules question ("does a partially captured objective
   count toward objectives held?"), which keeps its stated reading. So Q14 stays
   in the register's open-but-readable list and **the 15-ruled / 17-open counts
   do not move**. Pair 3 says this in the cell. If you intend Q14 itself to flip,
   the counts become 16 and 16 and the list `Q10–Q19` must split to
   `Q10–Q13, Q15–Q19` — one further pair, which I have not written.
2. **Nothing gates "Playable via debug commands."** It is a judgement goal with
   two rulings and now a re-opening rule, and no `GATE-DRV-` ID asserts any part
   of it. That is stated in §3 already; whether it should acquire a check, or
   stay explicitly a judgement, is yours.

## Handoffs

None. Neither ruling reaches rules text, map data or screen layout.

## Grounding

- §2.8's alias map and the T-CAP-05 exception paragraph, including the
  `captureTurns = 2` run and the "unruled" sentence Pair 1 replaces —
  `source/gdd.md` §2.8.
- The invariant text Ruling 1 turns on — "raising a unit's `captureProgress`
  short of completion" — §4.7 Spec Stub 8's `GATE-CAP-PARTIAL` block.
- N is per-scenario data — §2.7, and Q4's ruling in §4.7's register.
- T-SCN-08 (c) as the synthetic-fixture precedent — §4.7's T-SCN-08 fixture
  list. §3's row-7 paragraph records that (c) ran at `9086d6a` while (a) and (b)
  did not, each needing a stretch map authored as a scenario file, and that
  T-SCN-08 therefore **does not close**; §4.5 counts it among the 18 unclosed.
- Q29 read per acceptance ID — Q29's register row, and §3's row-7 and row-8
  paragraphs, which apply it that way.
- `GATE-CAP-PARTIAL` green at `7c36303` under clang++ and MSVC both, pass 1
  refused on the partial-credit differential — §3's row-8 paragraph and the UI
  evidence cell.
- The `6ccd40b` rebuild's move/act split into two independent per-unit flags, and
  T-TURN-01's second printed check (`two-independent-flags-in-either-order`) —
  §3's row-5-rebuild paragraph.
- §2.1's "move ... and/or act (attack), in either order" with two independent
  flags — §2.1's core-loop block.
- The re-opening rule and its 2026-08-02 amendment — §3's status paragraph.
- §4.5 arithmetic: **the 70 is 52 + 18 and T-CAP-05 is in neither list.** Green
  52 = 18 (`c224825`) + 9 (`647d4df`) + 9 (`ad77b13`) + 6 (`d8284f1`) + 7
  (`9086d6a`) + 1 (`6ccd40b`) + 2 (`7c36303`). Unclosed 18 = T-DATA-05 + T-SCN-08
  + T-SCN-09 + T-SCN-11 + T-UI-03 + T-UI-04 + 12 in rows 9–10. T-CAP-05 is §2.8's
  numbering and aliases onto no `T-TURN-` ID; its gate `GATE-CAP-PARTIAL` mints
  no acceptance ID on the `GATE-AI-SMOKE` precedent. **No §4.5 figure moves**, and
  the preamble clause saying so is retained in Pair 2.
- `source/kb_rules.md`: its only capture-at-the-cap text is the **Objectives
  held** line — "a capture in progress counts for nobody until the objective
  flips". It states the rule and no gate status, so this round falsifies nothing
  there and the file is untouched.
