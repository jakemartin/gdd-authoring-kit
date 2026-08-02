# Technical design — row 5 built (tech-director)

> ✅ **APPLIED ADDENDUM — DO NOT RE-APPLY.**
> All eleven replacement pairs were applied verbatim to the master GDD and merged
> on 2026-08-02. Re-applying them would fail — the OLD anchors no longer match.
> All eleven are straight replacements; none is an insertion, so no anchor is
> retained by design. Gate record: run `row5-2`, PASS, zero violations, after
> `row5-1` (4 violations, all in pair 3 and all in merging text — three accepted
> and fixed, one `placement-collision` withdrawn as a false positive and
> re-derived as such by `row5-2`). Master GDD md5
> `10b9a7ab4c5fbb4a7464faea37821122` → `94c67ebe95a09414485cc2a07822f9b5`. The
> merge precondition below was met: the crew commit was pushed first.
> Later changes to these sections need a NEW addendum file.

Eleven replacement pairs. Seven are in **§3** — three in the italic *Status: live
tracker* line, one in the ledger table, three in the populated-rows paragraph —
two are in **§4.5**'s *Specification outruns the build* row, and two are in
**§4.11**'s preamble.

---

## Pair 1 — §3 status line, the head commit

**OLD**
```
This draft stands at 2026-08-02, at commit [`647d4df`](https://github.com/jakemartin/stratocracy-crew/commit/647d4df) — the head of `main` in the crew repo, whose parent is [`9f87ecd`](https://github.com/jakemartin/stratocracy-crew/commit/9f87ecd).
```
**NEW**
```
This draft stands at 2026-08-02, at commit [`ad77b13`](https://github.com/jakemartin/stratocracy-crew/commit/ad77b13) — the head of `main` in the crew repo, whose parent is [`caa8267`](https://github.com/jakemartin/stratocracy-crew/commit/caa8267).
```

## Pair 2 — §3 status line, what week 1 did not close

**OLD**
```
rows 4–8 held no code then, and **row 4 has since landed** — recorded at the end of this paragraph — so at `647d4df` only rows 5–8 hold none; since §4.11's critical path runs 1 → 3 → 4 → 5 → 6/8, its first three links are evidence rather than schedule and **row 5 (Turn loop & win/tiebreak) is blocked on nothing but itself**.
```
**NEW**
```
rows 4–8 held no code then, and **rows 4 and 5 have since landed** — both recorded at the end of this paragraph — so at `ad77b13` only rows 6–8 hold none; since §4.11's critical path runs 1 → 3 → 4 → 5 → 6/8, its first four links are evidence rather than schedule and **row 6 (Opponent AI) is blocked on nothing but itself**.
```

## Pair 3 — §3 status line, its tail: row 5's record

The row-4 sentence that ends the paragraph today is bound to `647d4df` and stays
true there, so it is kept and row 5's record is added after it, bound to
`ad77b13`.

**OLD**
```
and a setter for the turn number is not the first of those.*
```
**NEW**
```
and a setter for the turn number is not the first of those. **Row 5 then landed**, at [`ad77b13`](https://github.com/jakemartin/stratocracy-crew/commit/ad77b13): **Turn loop & win/tiebreak**, gated **T-TURN-01..09, 9/9 under clang++ and MSVC both** — `g++` is not installed on this machine — while its pass-1 implementation `cpp_reference/Turn.buggy.cpp` is blocked at 6/9, on T-TURN-05, T-TURN-06 and T-TURN-07, under both compilers. Five tracked sources are cited, each probed present at that commit: `spec/turn_spec.md`, `cpp_reference/Turn.h`, `cpp_reference/Turn.good.cpp`, `cpp_reference/Turn.buggy.cpp`, `cpp_reference/test_turn.cpp`. The last of those is a seventh harness, so **nine** tracked sources define `main()` at `ad77b13` — the eight named above plus `cpp_reference/test_turn.cpp` — seven test harnesses, one combat duel simulator, and one debug REPL. **No ID is left uncovered:** row 5 has no in-editor half and no reserved-unwritten ID, so its full acceptance set closes at one commit, Q29 is satisfied, and the row flips in the table below. **No new acceptance ID was written**, so §4.5's 69 stands and its green count moves 27 → 36. §4.4 schedules rows 4–5 for **week 3**, so this row too is **ahead of the milestone table, not behind it**. Rows 3 and 4 declined the turn — row 4 takes the turn number as an argument — so row 5 is the first module to own alternation, per-unit act flags, the start-of-turn moment and the §2.8 result; it owns **no board**, since the §2.8 facts arrive as a caller-supplied `BoardSnapshot`, the same discipline row 4 uses. **T-TURN-04, 05, 06 and 07 encode §2.8's procedure exactly** — one guard, one three-key comparison, one grade — and **Q7 is executed rather than only written**: the cap is per-scenario data and the module refuses a cap below 1 rather than substituting a default, so no literal 20 exists in it. T-TURN-08 asserts only that the loop calls the already-verified `repairAmount` at the right moment with the right board facts, every expectation in it being a direct `cpp_reference/Combat.h` call; the heal values stay green at `5ffa8d6` under T-REPAIR-01..07 and are not re-asserted. Two readings are recorded in `spec/turn_spec.md` as **documented choices, not rules**: a turn is one full I-GO-U-GO round shared by both sides, read off two sites that keep the turn number and the side to move as separate fields — §4.7 Stub 8's UI snapshot `match {turn, turnCap, sideToMove, resultTier or null}`, and §4.10's canonical state hash, which serializes `GameState` in a fixed field order beginning turn counter, side to move — and consistent with §2.7's *both players draw income from turn 2*; and the cap resolves at the **end** of round `turnCap`, since §2.11.4 displays the counter as `N / turnCap`, so turn `turnCap` is a playable turn. Neither is a new rule and neither is filed as a change request. The driver reaches the module: `match <firstSide> <turnCap>`, `endturn`, `standings`, `result` and `flag <side> <id>` are new commands, joined by act-flag and alternation enforcement on `move`/`attack` and active-side gating on `income`/`build`/`capture`, and each is a call into `cpp_reference/Turn.h`, so the driver still holds no rules of its own. `flag` is a **debug designation** standing in for Stub 7's `isFlag` — row 7 is unbuilt and Q10 is open on exactness — the human names the flag unit and the driver never picks one, and it is what makes the flag kill award reachable, paid as the flat 500 through `cpp_reference/Economy.h::killAward`. `turn <n>` remains a debug setter and is now **refused while a match runs**; with no match running the board is the same free sandbox it was at `647d4df`, which is why `GATE-DRV-01..07` are unchanged and still pass. The driver suite is now **GATE-DRV-01..09, 9/9 under clang++ and MSVC both**, and those IDs are still **not** `T-*`: the driver is not a §4.7 stub, has no row in the ledger below, and flips nothing. A **Claude Code session** authored row 5 from the Director-written stub `spec/turn_spec.md`, **not a live CrewAI run**. What `ad77b13` still does not have is **an AI or a scenario file** (rows 6–8): the driver's boards are built-in fixtures plus `place`/`remove`, and no file format is defined or read.*
```

## Pair 4 — §3 ledger table, row 5

Formatted on the **Capture & Fame economy** row above it: the good
implementation and its test at one commit. `cpp_reference/Turn.buggy.cpp` is a
gate fixture and is cited in the status paragraph, not here.

**OLD**
```
| Turn loop & win / tiebreak | *pending* | — | *pending build* |
```
**NEW**
```
| **Turn loop & win / tiebreak** | agent | ✓ | `cpp_reference/Turn.good.cpp` + `cpp_reference/test_turn.cpp` @ [`ad77b13`](https://github.com/jakemartin/stratocracy-crew/commit/ad77b13) · T-TURN-01..09 (9/9) |
```

## Pair 5 — §3 populated-rows paragraph, the count

**OLD**
```
**Seven rows carry a ✓ in the table above, and an eighth carries evidence without one.**
```
**NEW**
```
**Eight rows carry a ✓ in the table above, and a ninth carries evidence without one.**
```

## Pair 6 — §3 populated-rows paragraph, row 5's evidence, its harness, and the ordinal

Row 5 lands against the paragraph's existing second authoring sentence, the one
row 4 joined, so the paragraph still carries two authoring sentences.

**OLD**
```
That check establishes that the file has not moved across those commits; it is not evidence about what any run did, and the harness is reported here because it is known and not because a diff proved it. Two IDs are still recorded as **uncovered** rather than omitted: **T-DATA-05**, the in-editor Unreal Automation half, and **T-MOVE-07**, reserved and unwritten on Q2. The first is why **Data tables** is the eighth row and does *not* flip
```
**NEW**
```
That check establishes that the file has not moved across those commits; it is not evidence about what any run did, and the harness is reported here because it is known and not because a diff proved it. **Turn loop & win / tiebreak** joined at [`ad77b13`](https://github.com/jakemartin/stratocracy-crew/commit/ad77b13) — T-TURN-01..09, **9/9 under clang++ and MSVC both** — and it leaves **no ID uncovered** either: no in-editor half and no reserved ID, so its full acceptance set closes at one commit and Q29 is satisfied rather than blocking. **It belongs to that same second sentence and does not start a third:** a **Claude Code session** authored it from the Director-written stub `spec/turn_spec.md`, again **not a live CrewAI run** — `crew/tasks.py` is **byte-unchanged from `5ffa8d6` to `ad77b13`**, so the file the live crew runs from still describes the Combat spec alone, and that check likewise establishes only that the file has not moved across those commits. Two IDs are still recorded as **uncovered** rather than omitted: **T-DATA-05**, the in-editor Unreal Automation half, and **T-MOVE-07**, reserved and unwritten on Q2. The first is why **Data tables** is the ninth row and does *not* flip
```

## Pair 7 — §3 populated-rows paragraph, the lineage parenthetical

**OLD**
```
*(Commit `647d4df` is the head of `main`; its parent is [`9f87ecd`](https://github.com/jakemartin/stratocracy-crew/commit/9f87ecd), so `5ffa8d6`, `c224825` and `9f87ecd` all remain ancestors and every commit link above resolves.
```
**NEW**
```
*(Commit `ad77b13` is the head of `main`; its parent is [`caa8267`](https://github.com/jakemartin/stratocracy-crew/commit/caa8267), so `5ffa8d6`, `c224825`, `9f87ecd`, `647d4df` and `caa8267` all remain ancestors and every commit link above resolves.
```

## Pair 8 — §4.5, the risk row's arithmetic

**OLD**
```
**Specification outruns the build** — **69** written acceptance IDs at this revision (§4.7–§4.11) against **7** verified ledger rows (§3). **Reduced and re-scoped at 2026-08-02, not retired:** no new ID has been written since `c224825`, and **27** of the 69 are green — **18** at `c224825`, where rows 1 and 3 closed their full acceptance sets and row 2's headless half passed, and **9** at `647d4df`, where T-FAME-01..09 closed row 4 — so the first three links of the critical path are evidence rather than schedule. **42 IDs remain unclosed**: T-DATA-05, which leaves row 2 unflipped, plus the 41 in rows 5–10, which hold no code
```
**NEW**
```
**Specification outruns the build** — **69** written acceptance IDs at this revision (§4.7–§4.11) against **8** verified ledger rows (§3). **Reduced and re-scoped at 2026-08-02, not retired:** no new ID has been written since `c224825`, and **36** of the 69 are green — **18** at `c224825`, where rows 1 and 3 closed their full acceptance sets and row 2's headless half passed, **9** at `647d4df`, where T-FAME-01..09 closed row 4, and **9** at `ad77b13`, where T-TURN-01..09 closed row 5 — so the first four links of the critical path are evidence rather than schedule. **33 IDs remain unclosed**: T-DATA-05, which leaves row 2 unflipped, plus the 32 in rows 6–10, which hold no code
```

## Pair 9 — §4.5, the mitigation's slip clause

**OLD**
```
so a slip in rows 5–8 moves everything downstream
```
**NEW**
```
so a slip in rows 6–8 moves everything downstream
```

## Pair 10 — §4.11 preamble, which rows have flipped

Rewrapped across three lines to hold the section's ~75-column wrapping. The
§4.7-heading sentence that follows is untouched.

**OLD**
```
Rows 1–8 are the §4.7 stubs — the eight ledger rows that read `*pending*` when
this table was written, of which **rows 1, 3 and 4 have since flipped** (§3).
```
**NEW**
```
Rows 1–8 are the §4.7 stubs — the eight ledger rows that read `*pending*`
when this table was written, of which **rows 1, 3, 4 and 5 have since
flipped** (§3).
```

## Pair 11 — §4.11 preamble, what depends on landed code

**OLD**
```
**Rows 1 and 3 are green at `c224825`, and row 4 at `647d4df`**, so rows 5–8
depend on landed code rather than on scheduled code, and **row 5 is the critical
path's next link**, both of its dependencies having landed — row 4 at `647d4df`
and Combat/Repair at `5ffa8d6`.
```
**NEW**
```
**Rows 1 and 3 are green at `c224825`, row 4 at `647d4df` and row 5 at
`ad77b13`**, so rows 6–8 depend on landed code rather than on scheduled code,
and **row 6 is the critical path's next link**, its dependency cell in the
table below reading `5`, which has landed.
```

---

## Placement

| Pair | Section | Exact site |
|---|---|---|
| 1 | §3 | *Status: live tracker* line, the head-commit sentence |
| 2 | §3 | Same line, the "What week 1 did **not** close" sentence |
| 3 | §3 | Same line, its end — after the row-4 record, to the italic close |
| 4 | §3 | The ledger table, the Turn loop row |
| 5 | §3 | Populated-rows paragraph, its opening sentence |
| 6 | §3 | Same paragraph, from the `crew/tasks.py` extent sentence through the Data-tables ordinal |
| 7 | §3 | Same paragraph, the lineage parenthetical |
| 8 | §4.5 | *Specification outruns the build*, the risk cell |
| 9 | §4.5 | The same row, the mitigation cell |
| 10 | §4.11 | Preamble, sentence 1 |
| 11 | §4.11 | Preamble, the green-rows sentence |

Pairs 1–3 are disjoint spans of one source line and apply in any order; so do
5–7 and 8–9. No pair touches §1, §2, §4.4, §4.7, §4.8, §4.9, §4.10, §4.11's
table body, or the Q register.

## Grounding

Every **OLD** block was grepped against `source/gdd.md` (md5
`10b9a7ab4c5fbb4a7464faea37821122`) and returns **exactly one** match. Facts A
and P back pairs 1 and 7 — `ad77b13` on `main`, parent `caa8267`, with
`5ffa8d6`, `c224825`, `9f87ecd`, `647d4df` and `caa8267` all ancestors. Fact B
backs pair 4's evidence cell, the gate and buggy-run clauses in pairs 3 and 6,
and the Q29 consequence in both; Fact P carries the same gate result to
`ad77b13`, where `cpp_reference/Turn.good.cpp` and `cpp_reference/test_turn.cpp`
are byte-identical to `caa8267`. Facts C and P back pair 3's five-source
citation set, at the extent they establish: path existence at the commit named.
Fact D backs pair 3's week-3 clause; §4.4 is not edited. Fact E backs pair 3's
ownership, `BoardSnapshot`, T-TURN-04..07, Q7 and T-TURN-08 clauses. Facts F and
O back the two documented readings in pair 3, written as choices rather than
rules; Fact O supplies the two sites reading 1 is read off — §4.7 Stub 8's
`match` snapshot, the document's only occurrence of `sideToMove`, and §4.10's
canonical state hash field order. Fact G backs pair 3's driver clauses, the
`flag` designation, the refusal of `turn <n>` during a match, and
GATE-DRV-01..09. Fact H backs every figure in pair 8 and pair 3's 69, 27 → 36
and 8-verified-rows clauses, and pair 2's rows 6–8. Facts I and P back the
nine-`main()` count in pair 3, at the extent of tracked `.cpp` files at that
commit. Fact J backs the harness clauses in pairs 3 and 6, and the
`crew/tasks.py` check is written at its own extent. Fact L backs pair 3's
closing sentence, bound to `ad77b13`. Row 6's status as the next link (pairs 2
and 11) is read from §4.11's own row-6 dependency cell, which names row 5.
**Fact Q** is why every pair names `ad77b13` and no pair names a second commit
for row 5: the pass-2 gate, the pass-1 block, the driver suite and the week-1
record were all re-run at `ad77b13` with an empty `git status --porcelain`, and
rows 6–8 hold no code there.

**Merge precondition (Facts K, N and P).** Apply this addendum only after
`ad77b13` is pushed: pairs 3, 4 and 6 add links to it, pair 1 links it and its
parent `caa8267`, and pair 7 keeps the document's existing claim that every
commit link above resolves. At authoring, `ad77b13` is committed and not pushed;
the Director authorises the crew push and the GDD merge together, as they did
for rows 1–4.

No pair contains the ruling text on "Playable via debug commands" in an OLD
block, and no pair states or implies a ruling on it.

## Open questions for the Director

None.

## Change requests

None.

## Handoffs

None owed. No pair states or restates a rule, a map fact, or a screen layout;
pair 3's Q7 clause reports that an already-ruled question is executed in code.
