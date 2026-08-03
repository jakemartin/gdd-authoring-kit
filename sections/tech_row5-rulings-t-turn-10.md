> ## ✅ APPLIED ADDENDUM — DO NOT RE-APPLY
>
> All thirteen pairs were merged into the master GDD on 2026-08-03, **together
> with** `sections/rules_row5-rulings-and-t-cap-05.md` (6 pairs). This file
> applied second. Master md5 `95655234f1d18805e69d4abea942bcf5` →
> `7dc635b4f06589f89b46e2fa1b7ad86b`.
>
> Gate: run `row5-rulings-3`, **PASS**, 0 violations, after `row5-rulings-1`
> (BLOCK, 1 — a Grounding survey generalised from `§4.5's 69 stands` to the
> figure and missed a fifth site; the root cause was the orchestrator's phrase
> grep, not the author's) and `row5-rulings-2` (BLOCK, 1 — an arithmetic pair had
> silently replaced §4.5's conclusion clause, de-syncing it from §3's untouched
> parallel sentence; **restored verbatim**).
>
> **Pair 11 is an insertion — its OLD anchor is retained deliberately.** Post-check
> on the merged master: every NEW present exactly once; pair 11's OLD present
> **once**, the other twelve **zero** times. This file is **not safe to apply
> twice**.
>
> **`T-TURN-10` is minted WRITTEN, UNBLOCKED, ASSERTING and NOT GREEN** — the code
> it gates does not exist yet. §4.5 moves written **69 → 70** and unclosed
> **20 → 21** while green **stays 49**. Row 5's ledger row is **untouched** and
> stays flipped on `ad77b13`, per the Director's sequencing ruling.
>
> **Owed to the rebuild's addendum, verified and not fixed here:** §3 line 1504
> says row 5 *"leaves no ID uncovered … its full acceptance set closes at one
> commit"* and tallies six/four IDs. Once row 5's acceptance set is
> `T-TURN-01..10` with `T-TURN-10` unclosed, those become candidates for
> seven/five. It is left because the Director's ruling reserves row 5's status
> for the rebuild — not because it was missed.

# Technical design — row-5 rulings addendum (tech-director)

## Placement

An OLD/NEW addendum against `source/gdd.md` @ md5 `ca397f4f2eca447b451fca2ca2393092`.
Thirteen pairs, in file order: **§3**'s five sentences that name §4.5's written
total as a figure (5), **§4.5**'s "Specification outruns the build" risk cell (2),
**§4.7 Spec Stub 4** (1), **§4.7 Spec Stub 5** (4), **§4.11** row 5's line (1).

The §3 pairs are scoped to exactly those five sentences, which pair 6 falsifies by
moving the total. Nothing else in §3 is touched: no ledger table row, no row-4 or
row-5 status, and not the `per-unit act flags` phrase, which is accurate for
`ad77b13` and stays filed as a change request for row 5's rebuild addendum.

`T-TURN-10` is **written, unblocked and asserting, and not green**; the code
satisfying it does not exist yet, so §4.5's green count does not move.

---

## Pair 1 — §3, the debug-driver clause at `9f87ecd` (replacement)

**OLD**

```
so §4.5's 69-ID count does not move and **no ledger row flips on the driver's account**.
```

**NEW**

```
so §4.5's written-ID count does not move at this landing and **no ledger row flips on the driver's account**.
```

## Pair 2 — §3, row 4's evidence sentence (replacement)

**OLD**

```
so §4.5's 69 stands and its green count moves 18 → 27.
```

**NEW**

```
so §4.5's written-ID count does not move at this landing and its green count moves 18 → 27.
```

## Pair 3 — §3, row 5's evidence sentence (replacement)

**OLD**

```
so §4.5's 69 stands and its green count moves 27 → 36.
```

**NEW**

```
so §4.5's written-ID count does not move at this landing and its green count moves 27 → 36.
```

## Pair 4 — §3, row 6's evidence sentence (replacement)

**OLD**

```
IDs close: §4.5's 69 stands and its green count moves 36 → 42.
```

**NEW**

```
IDs close: §4.5's written-ID count does not move at this landing and its green count moves 36 → 42.
```

## Pair 5 — §3, row 7's evidence sentence (replacement)

**OLD**

```
so §4.5's 69 stands and its green count moves 42 → 49.
```

**NEW**

```
so §4.5's written-ID count does not move at this landing and its green count moves 42 → 49.
```

Each of these five keeps its own causal claim and drops only the figure it
borrowed from §4.5 — pairs 2–5 that their row minted no acceptance ID, pair 1 that
the driver's IDs are deliberately not `T-*` because the driver is not a §4.7 stub.
All five claims stay true. One name and one tense across all five: **written-ID
count**, present tense, which is the tense of the `green count moves` verb beside
it in the same clause. The four green-count deltas are §3's own arithmetic and are
unchanged; they still reach the 49 green that pair 6 leaves standing.

## Pair 6 — §4.5, risk-cell head (replacement)

**OLD**

```
**69** written acceptance IDs at this revision (§4.7–§4.11) against **9** verified ledger rows (§3). **Reduced and re-scoped at 2026-08-03, not retired:** no new ID has been written since `c224825` — row 6's GATE-AI-SMOKE is acceptance that deliberately mints none, so it closes a check without moving this count — and **49** of the 69 are green:
```

**NEW**

```
**70** written acceptance IDs at this revision (§4.7–§4.11) against **9** verified ledger rows (§3). **Reduced and re-scoped at 2026-08-03, not retired:** one new ID has been written since `c224825` — `T-TURN-10`, minted this revision into Spec Stub 5 for the per-turn build limit Q8(b) ruled — and it is **written, unblocked and asserting, and not green**, because the code that satisfies it does not exist yet; row 6's GATE-AI-SMOKE is acceptance that deliberately mints none, so it closes a check without moving this count. **49** of the 70 are green:
```

## Pair 7 — §4.5, risk-cell tail (replacement)

**OLD**

```
— so everything on the critical path but row 8 is evidence rather than schedule. **20 IDs remain unclosed**: T-DATA-05, which leaves row 2 unflipped; T-SCN-08, T-SCN-09 and T-SCN-11, which are written, unblocked and asserting, but ran only part of their fixture sets, and which leave row 7 unflipped; and the **16** in rows 8–10, which hold no code
```

**NEW**

```
— so everything on the critical path but row 8 is evidence rather than schedule. **21 IDs remain unclosed**: T-DATA-05, which leaves row 2 unflipped; T-SCN-08, T-SCN-09 and T-SCN-11, which are written, unblocked and asserting, but ran only part of their fixture sets, and which leave row 7 unflipped; `T-TURN-10`, written this revision, unblocked and asserting — the code it gates does not exist yet, so it has not run and is not green; and the **16** in rows 8–10, which hold no code
```

The conclusion clause is carried over verbatim; this pair changes the arithmetic
only — `20` → `21` and one entry added to the enumeration. Arithmetic:
1 + 3 + 1 + 16 = **21**, and 49 + 21 = **70**.

## Pair 8 — §4.7 Spec Stub 4, `T-FAME-04` (replacement)

**OLD**

```
  T-FAME-04  spawn: on the factory hex if free, else an adjacent free hex, else
             the build waits (§2.7). One build per factory per turn; a waiting
             build HOLDS that factory's slot until it spawns; Fame is committed
             at queue time, never at spawn time, and is not refundable (Q8,
             ruled)
```

**NEW**

```
  T-FAME-04  spawn: on the factory hex if free, else an adjacent free hex, else
             the build waits (§2.7). A waiting build HOLDS that factory's slot
             until it spawns; Fame is committed at queue time, never at spawn
             time, and is not refundable (Q8, ruled). The PER-TURN half of
             §2.7's build limit is deliberately NOT asserted here: this module
             is handed the turn number rather than owning it (§3), so it is
             gated in Stub 5 as T-TURN-10
```

Stub 4's Acceptance line is unchanged — `T-FAME-01..09` — so §4.11 row 4's
acceptance cell does not change and no pair is written against it.

## Pair 9 — §4.7 Spec Stub 5, Inputs (replacement)

**OLD**

```
Inputs:  game state; per-unit act flags; the turn counter and cap (Q7, stored in
         the scenario file, Stub 7); commands incl. EndTurn{}.
```

**NEW**

```
Inputs:  game state; per-unit move and act flags — TWO flags per unit, not one
         (T-TURN-01); the per-factory record of builds taken this turn
         (T-TURN-10); the turn counter and cap (Q7, stored in the scenario
         file, Stub 7); commands incl. EndTurn{}.
```

## Pair 10 — §4.7 Spec Stub 5, `T-TURN-01` (replacement)

**OLD**

```
  T-TURN-01  strict alternation; each unit acts at most once per own turn, in
             any order the owner chooses (§2.1)
```

**NEW**

```
  T-TURN-01  strict alternation; each unit carries TWO independent flags in its
             own turn and may move at most once AND act at most once, per
             §2.1's select → move → act sequence — moving never consumes the
             act, so a unit that has moved is still a legal attacker that turn
             — and the owner takes its units in any order it chooses (§2.1).
             The gate asserts that a move-then-attack by one unit COMPLETES,
             and that a second move, or a second act, by that unit is refused
```

## Pair 11 — §4.7 Spec Stub 5, mint `T-TURN-10` (insertion)

**OLD**

```
  T-TURN-09  determinism: the same command sequence from the same scenario →
             identical result tier and identical state at every step
```

**NEW**

```
  T-TURN-09  determinism: the same command sequence from the same scenario →
             identical result tier and identical state at every step
  T-TURN-10  one build per factory per turn, player and AI alike (§2.7; Q8(b),
             ruled): a Build naming a factory that has already taken its build
             this turn is REFUSED, and fameTotal is unchanged by the refusal —
             Fame is committed at queue time (Q8(c)), and a refused Build never
             queues. BOTH dispositions of the first build count against the
             allowance: one that spawned immediately, and one that waits and
             holds the slot (T-FAME-04). The allowance renews at the start of
             the owner's turn. This ID lives in Stub 5 rather than Stub 4
             because the check needs the turn number, and the economy module
             takes the turn as an argument rather than owning it (§3) — Stub 4
             gates the half it can enforce without a turn, this gates the half
             it cannot
```

Substring test on the final bytes: NEW **contains** OLD verbatim as a prefix, so
this pair is an **insertion**, not a replacement.

## Pair 12 — §4.7 Spec Stub 5, Acceptance (replacement)

**OLD**

```
Acceptance: T-TURN-01..09.
```

**NEW**

```
Acceptance: T-TURN-01..10.
```

## Pair 13 — §4.11 row 5 (replacement)

**OLD**

```
| 5 | Turn loop & win/tiebreak (Stub 5) | 4 + verified Combat/Repair @ 5ffa8d6 | Yes | T-TURN-01..09 |
```

**NEW**

```
| 5 | Turn loop & win/tiebreak (Stub 5) | 4 + verified Combat/Repair @ 5ffa8d6 | Yes | T-TURN-01..10 |
```

---

## Anchor and overlap checks

Re-run over the current bytes of this file.

- Every OLD above was re-grepped against `source/gdd.md` and matched **exactly
  once** — the five §3 anchors included. Pair 1's anchor is distinguished by
  `69-ID count does not move`; pairs 2–5 by their green-count deltas.
- **Classification by substring test:** pair 11 is an **insertion** (its NEW
  contains its OLD verbatim as a prefix). All twelve others are **replacements**
  (no NEW contains its OLD). **12 replacements, 1 insertion.** Pair 7 was
  re-tested after its conclusion clause was restored: its NEW carries `**21 IDs
  remain unclosed**` where its OLD carries `**20**`, so the NEW does not contain
  the OLD and the pair stays a replacement.
- **Overlap check, three sites where it was needed.**
  1. *§3's evidence paragraph* carries pairs 1–5 on one line. Their byte order was
     established by pairwise `A.*B` greps rather than assumed, and it is **pair 1
     first**: the debug-driver clause precedes all four row clauses, which then run
     18 → 27, 27 → 36, 36 → 42, 42 → 49. None of the five OLDs is a substring of
     any other, and each is separated from the next by prose that is in no OLD.
     Disjoint, and the pairs are numbered in that order.
  2. *§4.5's risk-cell line* carries pairs 6 and 7, separated by the per-commit
     green list (`**18** at c224825 … **7** at 9086d6a`), which is in neither OLD.
     Disjoint.
  3. *Stub 5's fenced block* carries pairs 9, 10, 11 and 12 — the Inputs lines, the
     T-TURN-01 lines, the T-TURN-09 lines and the Acceptance line. Four disjoint
     regions in ascending order.
- Pair order in this file is ascending file order throughout.

## Open questions for the Director

1. **Which commands set the act flag?** §2.1's loop reads `act (attack / capture
   / build)`, but §2.9 issues builds at a factory in the economy phase rather
   than as a unit's action. `T-TURN-01` cannot be asserted until the flag-setting
   command set is enumerated: Attack and Capture are certain; whether a Build
   consumes the acting unit's act flag — or consumes no unit flag at all — is
   unstated. Reachable in ordinary play.
2. **A factory captured mid-turn.** If a factory changes hands during a turn,
   does its new owner inherit "has already taken its build this turn"? `T-FAME-06`
   flips income on capture and `T-TURN-10` needs the per-factory build record's
   disposition on the same event. Also reachable in ordinary play.
3. **May a unit act before it moves?** §2.1's sequence reads move-then-act, and
   `T-TURN-01` as written above asserts move-then-attack completes. Whether
   attack-then-move is legal under the two-flag rule is not stated anywhere, and
   the gate needs it either as a permitted sequence or as a refusal.
4. **Where the row-5 status restatement is written.** §4.11's preamble says row 5
   is green at `ad77b13`, and after this merge §4.5 lists `T-TURN-10` among the
   unclosed IDs on Stub 5's acceptance set, which Q29 measures at one commit.
   C7 reserves row 5's status for the rebuild's own addendum, so no pair here
   touches either sentence — confirming that the rebuild addendum is where
   §4.11's preamble is restated, and not this one.

None of the four is resolved in a pair.

## Change requests

| Existing § | Current text | Proposed change | Why |
|---|---|---|---|
| §4.7 Spec Stub 8, snapshot per-unit field list | `per-unit  {id, side, unitId, hex, hp, hpMax, isFlag, hasActed, captureProgress}` | Add a second flag field beside `hasActed` | Under the two-flag rule the snapshot carries one bit where the rules module now holds two, so no widget can distinguish a unit that has moved from one that has acted. Row 8's to write when it is built; out of scope this round (fact F), so filed rather than written. |
| §3, the row-5 evidence paragraph | describes Stub 5's inputs as "per-unit act flags" | Restate when row 5's rebuild is recorded | Accurate for what row 5 did at `ad77b13`, so this round does not falsify it; it is the same singular-flag wording pair 9 changes in Stub 5's Inputs line. Belongs to the rebuild addendum. |

## Handoffs

- **`rules-designer` (§2.8).** §2.8's alias-map preamble reads "`T-CAP-01..08` is
  §2.8's own numbering for the procedure §4.7 Spec Stub 5 gates as
  `T-TURN-01..09`, so there is one suite, not two." Pairs 11 and 12 make Stub 5's
  suite `T-TURN-01..10`, so that range goes stale on merge. §2.8 is yours this
  round; I have written no pair there. The alias map's eight rows need no new
  row: no `T-CAP-` invariant aliases onto `T-TURN-10`, since §2.8's numbering
  covers the win/tiebreak procedure and not the build limit.
- **`rules-designer` (§2.1, §2.7).** `T-TURN-01` and `T-TURN-10` cite §2.1's
  `select → move → act` sequence and §2.7's "One build per factory per turn, for
  the player and the AI alike" as the rules they gate. Both citations are to text
  that exists today; if either sentence's wording moves, the gate cites the moved
  wording rather than the other way round.
- **`ux-onboarding-designer`.** Whether the HUD greys a moved-but-unacted unit
  differently from a fully-spent one is a §2.11 call, not mine; the snapshot field
  it would bind to is the Stub 8 change request above.

## Grounding

- **69 → 70, green stays 49, unclosed 20 → 21** — C5. The 69, the 49, the 20 and
  the 16-in-rows-8–10 breakdown are all read from §4.5's existing risk cell; the
  only new operand is the +1 for `T-TURN-10`.
- **The five §3 sentences paired above** — each names §4.5's written total as a
  figure, which pair 6 moves.
- **`T-TURN-10`'s rule** — §2.7: "**One build per factory per turn**, for the
  player and the AI alike (§2.9)"; Q8(b), ruled: "one build per factory per turn,
  player and AI alike". No new rule is invented; the ID gives a ruled rule a gate.
- **Its non-refundability clause** — Q8(c), ruled: Fame committed at queue time,
  not refundable.
- **Why it lives in Stub 5** — §3's row-4 evidence paragraph: the economy module
  "never advances a turn and never decides whose turn it is, taking the turn
  number as an argument, which is why it could land before row 5" (B3).
- **`T-FAME-04`'s dropped clause** — C1 and C4: row 4 keeps spawn placement, the
  waiting build's slot, and queue-time commitment; the per-turn half moves. B4
  records that the shipped test at `9086d6a` never covered a second same-turn
  build.
- **`T-TURN-01`'s two flags** — C2 and C4; B5 records the sentence being replaced;
  B1 records the single shared act flag in the shipped source at `9086d6a`.
- **`T-TURN-10`'s status wording** — E: written, unblocked and asserting, and not
  green, on the `GATE-CAP-PARTIAL` precedent, which §4.7's register states as
  "row 8 holds no code, so that gate has not run — it asserts, and it is not
  green."
- **Row 5's ledger row untouched** — C7. §4.5's "**9** at `ad77b13`, where
  T-TURN-01..09 closed row 5" sits between pairs 6 and 7 and is left as the dated
  record of that commit; no pair reaches it, and no §3 ledger table row is paired.
