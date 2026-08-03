> ## ✅ APPLIED ADDENDUM — DO NOT RE-APPLY
>
> All eleven pairs were merged into the master GDD on 2026-08-02.
> Master md5 `cc07e1f0db78b4955059933520194360` → `324dfa07c91fc4ddec4c5315ba1c397b`.
>
> Gate: run `row6-3`, **PASS**, 0 violations, after `row6-1` (BLOCK, 2 — both in
> pair 3, both a check cited as evidence for a claim wider than the check could
> see) and `row6-2` (BLOCK, 1 — a false document-wide negative in the third
> change request, which was new text a fix had just written). All three fixes
> were deletions.
>
> All eleven pairs are **replacements**, none an insertion. Post-check on the
> merged master: every NEW present exactly once, every OLD present zero times.
> Pair 3's italic boundary closes correctly — the master now reads
> `definitions above.* Legend:`, exactly one asterisk.
>
> Merge precondition met: crew `d8284f1` was pushed to `main` first, and all
> eight commits the pairs link were confirmed present on the remote.
>
> `kb/rules.md` was **not** re-synced. §2 is byte-identical across this merge
> (98,194 chars both sides, compared as strings), since no pair touches §2.

# Technical design — row 6 built (tech-director)

Eleven replacement pairs. Seven are in **§3** — three in the italic *Status: live
tracker* line, one in the ledger table, three in the populated-rows paragraph —
two are in **§4.5**'s *Specification outruns the build* row, and two are in
**§4.11**'s preamble.

---

## Pair 1 — §3 status line, the head commit

**OLD**
```
This draft stands at 2026-08-02, at commit [`ad77b13`](https://github.com/jakemartin/stratocracy-crew/commit/ad77b13) — the head of `main` in the crew repo, whose parent is [`caa8267`](https://github.com/jakemartin/stratocracy-crew/commit/caa8267).
```
**NEW**
```
This draft stands at 2026-08-02, at commit [`d8284f1`](https://github.com/jakemartin/stratocracy-crew/commit/d8284f1) — the head of `main` in the crew repo, whose parent is [`2381ca0`](https://github.com/jakemartin/stratocracy-crew/commit/2381ca0).
```

## Pair 2 — §3 status line, what week 1 did not close

**OLD**
```
rows 4–8 held no code then, and **rows 4 and 5 have since landed** — both recorded at the end of this paragraph — so at `ad77b13` only rows 6–8 hold none; since §4.11's critical path runs 1 → 3 → 4 → 5 → 6/8, its first four links are evidence rather than schedule and **row 6 (Opponent AI) is blocked on nothing but itself**.
```
**NEW**
```
rows 4–8 held no code then, and **rows 4, 5 and 6 have since landed** — all three recorded at the end of this paragraph — so at `d8284f1` only rows 7–8 hold none; since §4.11's critical path runs 1 → 3 → 4 → 5 → 6/8, everything on that path but **row 8** is now evidence rather than schedule, and row 8's other dependency is **row 7**, which holds no code.
```

## Pair 3 — §3 status line, its tail: row 6's record

The row-5 sentence that ends the paragraph today is bound to `ad77b13` and stays
true there, so it is kept and row 6's record is added after it, bound to
`d8284f1`. The closing italic `*` is carried in both blocks so the replacement
leaves exactly one.

**OLD**
```
and no file format is defined or read.*
```
**NEW**
```
and no file format is defined or read. **Row 6 then landed**, at [`d8284f1`](https://github.com/jakemartin/stratocracy-crew/commit/d8284f1): **Opponent AI**, gated **T-AI-01..06 plus GATE-AI-SMOKE, 7/7 under clang++ and MSVC both** — `g++` is not installed on this machine — while its pass-1 implementation `cpp_reference/Ai.buggy.cpp` is blocked at 5/7, on T-AI-05 and T-AI-06, under both compilers. Five tracked sources are cited, each probed present at that commit: `spec/ai_spec.md`, `cpp_reference/Ai.h`, `cpp_reference/Ai.good.cpp`, `cpp_reference/Ai.buggy.cpp`, `cpp_reference/test_ai.cpp`. The last of those is an eighth harness, so **ten** tracked sources define `main()` at `d8284f1` — the nine named above plus `cpp_reference/test_ai.cpp` — eight test harnesses, one combat duel simulator, and one debug REPL. **No ID is left uncovered:** row 6 has no in-editor half and no reserved-unwritten ID, so its full acceptance set closes at one commit, Q29 is satisfied, and the row flips in the table below. **GATE-AI-SMOKE mints no acceptance ID.** The self-play smoke run is acceptance and §4.11 row 6 names it, but it carries no numbered ID in this document and `spec/ai_spec.md` declines to mint one, since a `T-AI-07` would move §4.5's count. The gate is therefore 7/7 while **six** IDs close: §4.5's 69 stands and its green count moves 36 → 42. §4.4 schedules row 6 for **week 3**, so this row too is **ahead of the milestone table, not behind it**. This is **the shipping opponent** (§2.9) and not a stand-in: difficulty is a starting-Fame handicap and never a smarter routine, and nothing in the module reads a difficulty tier at all. **It decides and applies nothing** — it emits one ordinary command at a time and the caller applies it, in the gate through the debug driver's own `execute`, the same door a typed command uses, which is what makes T-AI-01's *validated like any player command* structural rather than asserted; T-AI-01's counter printed `129 AI commands issued across 6 games`. It holds no rules — routes to `cpp_reference/Move.h`, damage and counters to `cpp_reference/Combat.h`, stats to `cpp_reference/Data.h`, affordability and kill value to `cpp_reference/Economy.h`, act flags and alternation to `cpp_reference/Turn.h` — and it owns **no board**, reading a caller-composed `AiState` on which `spec/ai_spec.md` records **no field a player could not read off the screen**, which is where §4.7 Stub 6's *the AI cheats at nothing* is carried. **Q9 is executed rather than only written, and the gate caught pass 1 breaking it:** T-AI-06 fixes position and target ties to canonical hex order — for a target, the hex it occupies — and build ties to Infantry > Recon > Artillery > Tank, ascending §2.4 cost and **not** the order §2.4's table prints, which is the order pass 1 used. **T-AI-05 is a sweep rather than a fixture:** of **348** exchanges in the shipped stat table where the counter kills the attacker, the good build skips **338** and permits **10**, each permitted one checked not to trade down, while the pass-1 build permits **0** — its guard had collapsed to *do not attack if the counter kills you*, dropping §2.9's *and trades down* half, which is the failure the sweep exists to catch. Five readings are recorded in `spec/ai_spec.md` as **documented choices, not rules**: the buildlist is caller-supplied data, since §2.9 names a composition and no ratio; *undefended* (T-AI-03) excludes an enemy adjacent to the objective as well as one standing on it, since `cpp_reference/Move.h` already refuses an occupied hex; *near* (T-AI-03) is reachable this turn and cheapest to reach among those, ties by canonical hex order; *trades down* (T-AI-05) prices value dealt as the victim's kill award prorated by the damage share of its max HP and value lost as the attacker's own kill award unprorated, both read through `cpp_reference/Economy.h::killAward`; and with no flag designated the advance goal is the canonically first enemy unit, `isFlag` being Stub 7's placement field with row 7 unbuilt and Q10 open. The driver reaches the module: `ai` plays the active side's turn and `ai buildlist` sets §2.9's list, and the start of a turn now runs repair, income and capture tick in that order. `GATE-DRV-01..07` are unchanged and still pass; the driver suite is now **GATE-DRV-01..10, 10/10 under clang++ and MSVC both**, `GATE-DRV-10` being new at this commit — it replays the AI's printed command lines by hand and asserts an identical state hash — and those IDs are still **not** `T-*`: the driver is not a §4.7 stub, has no row in the ledger below, and flips nothing. A **Claude Code session** authored row 6 from the Director-written stub `spec/ai_spec.md`, **not a live CrewAI run**. No scenario harness and no UI harness is among the ten `main()` definitions above.*
```

## Pair 4 — §3 ledger table, row 6

Formatted on the **Turn loop & win / tiebreak** row above it: the good
implementation and its test at one commit. `cpp_reference/Ai.buggy.cpp` is a
gate fixture and is cited in the status paragraph, not here. GATE-AI-SMOKE is
named without a `T-` ID because it mints none.

**OLD**
```
| Opponent AI | *pending* | — | *pending build* |
```
**NEW**
```
| **Opponent AI** | agent | ✓ | `cpp_reference/Ai.good.cpp` + `cpp_reference/test_ai.cpp` @ [`d8284f1`](https://github.com/jakemartin/stratocracy-crew/commit/d8284f1) · T-AI-01..06 (6/6) + GATE-AI-SMOKE |
```

## Pair 5 — §3 populated-rows paragraph, the count

**OLD**
```
**Eight rows carry a ✓ in the table above, and a ninth carries evidence without one.**
```
**NEW**
```
**Nine rows carry a ✓ in the table above, and a tenth carries evidence without one.**
```

## Pair 6 — §3 populated-rows paragraph, row 6's evidence, its harness, and the ordinal

Row 6 lands against the paragraph's existing second authoring sentence, the one
rows 4 and 5 joined, so the paragraph still carries two authoring sentences.

**OLD**
```
and that check likewise establishes only that the file has not moved across those commits. Two IDs are still recorded as **uncovered** rather than omitted: **T-DATA-05**, the in-editor Unreal Automation half, and **T-MOVE-07**, reserved and unwritten on Q2. The first is why **Data tables** is the ninth row and does *not* flip
```
**NEW**
```
and that check likewise establishes only that the file has not moved across those commits. **Opponent AI** joined at [`d8284f1`](https://github.com/jakemartin/stratocracy-crew/commit/d8284f1) — T-AI-01..06 plus GATE-AI-SMOKE, **7/7 under clang++ and MSVC both** — and it leaves **no ID uncovered** either: no in-editor half and no reserved ID, so its full acceptance set closes at one commit and Q29 is satisfied rather than blocking. Six of those seven checks are numbered IDs; GATE-AI-SMOKE mints none, for the reason the paragraph above gives. **It belongs to that same second sentence and does not start a third:** a **Claude Code session** authored it from the Director-written stub `spec/ai_spec.md`, again **not a live CrewAI run** — `crew/tasks.py` is **byte-unchanged from `5ffa8d6` to `d8284f1`**, so the file the live crew runs from still describes the Combat spec alone, and that check carries the same extent as the two before it: the file has not moved. Two IDs are still recorded as **uncovered** rather than omitted: **T-DATA-05**, the in-editor Unreal Automation half, and **T-MOVE-07**, reserved and unwritten on Q2. The first is why **Data tables** is the tenth row and does *not* flip
```

## Pair 7 — §3 populated-rows paragraph, the lineage parenthetical

**OLD**
```
*(Commit `ad77b13` is the head of `main`; its parent is [`caa8267`](https://github.com/jakemartin/stratocracy-crew/commit/caa8267), so `5ffa8d6`, `c224825`, `9f87ecd`, `647d4df` and `caa8267` all remain ancestors and every commit link above resolves.
```
**NEW**
```
*(Commit `d8284f1` is the head of `main`; its parent is [`2381ca0`](https://github.com/jakemartin/stratocracy-crew/commit/2381ca0), so `5ffa8d6`, `c224825`, `9f87ecd`, `647d4df`, `caa8267`, `ad77b13` and `2381ca0` all remain ancestors and every commit link above resolves.
```

## Pair 8 — §4.5, the risk row's arithmetic

**OLD**
```
**Specification outruns the build** — **69** written acceptance IDs at this revision (§4.7–§4.11) against **8** verified ledger rows (§3). **Reduced and re-scoped at 2026-08-02, not retired:** no new ID has been written since `c224825`, and **36** of the 69 are green — **18** at `c224825`, where rows 1 and 3 closed their full acceptance sets and row 2's headless half passed, **9** at `647d4df`, where T-FAME-01..09 closed row 4, and **9** at `ad77b13`, where T-TURN-01..09 closed row 5 — so the first four links of the critical path are evidence rather than schedule. **33 IDs remain unclosed**: T-DATA-05, which leaves row 2 unflipped, plus the 32 in rows 6–10, which hold no code
```
**NEW**
```
**Specification outruns the build** — **69** written acceptance IDs at this revision (§4.7–§4.11) against **9** verified ledger rows (§3). **Reduced and re-scoped at 2026-08-02, not retired:** no new ID has been written since `c224825` — row 6's GATE-AI-SMOKE is acceptance that deliberately mints none, so it closes a check without moving this count — and **42** of the 69 are green: **18** at `c224825`, where rows 1 and 3 closed their full acceptance sets and row 2's headless half passed, **9** at `647d4df`, where T-FAME-01..09 closed row 4, **9** at `ad77b13`, where T-TURN-01..09 closed row 5, and **6** at `d8284f1`, where T-AI-01..06 closed row 6 — so everything on the critical path but row 8 is evidence rather than schedule. **27 IDs remain unclosed**: T-DATA-05, which leaves row 2 unflipped, plus the 26 in rows 7–10, which hold no code
```

## Pair 9 — §4.5, the mitigation's slip clause

**OLD**
```
so a slip in rows 6–8 moves everything downstream
```
**NEW**
```
so a slip in rows 7–8 moves everything downstream
```

## Pair 10 — §4.11 preamble, which rows have flipped

Rewrapped to hold the section's ~75-column wrapping. The §4.7-heading sentence
that follows is untouched.

**OLD**
```
Rows 1–8 are the §4.7 stubs — the eight ledger rows that read `*pending*`
when this table was written, of which **rows 1, 3, 4 and 5 have since
flipped** (§3).
```
**NEW**
```
Rows 1–8 are the §4.7 stubs — the eight ledger rows that read `*pending*`
when this table was written, of which **rows 1, 3, 4, 5 and 6 have since
flipped** (§3).
```

## Pair 11 — §4.11 preamble, what depends on landed code

**OLD**
```
**Rows 1 and 3 are green at `c224825`, row 4 at `647d4df` and row 5 at
`ad77b13`**, so rows 6–8 depend on landed code rather than on scheduled code,
and **row 6 is the critical path's next link**, its dependency cell in the
table below reading `5`, which has landed.
```
**NEW**
```
**Rows 1 and 3 are green at `c224825`, row 4 at `647d4df`, row 5 at
`ad77b13` and row 6 at `d8284f1`**, so rows 7–8 depend on landed code rather
than on scheduled code, and **row 8 is the critical path's remaining link**,
its dependency cell in the table below reading `5, 7` — row 5 has landed and
row 7 has not.
```

---

## Placement

| Pair | Section | Exact site |
|---|---|---|
| 1 | §3 | *Status: live tracker* line, the head-commit sentence |
| 2 | §3 | Same line, the "What week 1 did **not** close" sentence |
| 3 | §3 | Same line, its end — after the row-5 record, to the italic close |
| 4 | §3 | The ledger table, the Opponent AI row |
| 5 | §3 | Populated-rows paragraph, its opening sentence |
| 6 | §3 | Same paragraph, from the row-5 extent sentence through the Data-tables ordinal |
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
`cc07e1f0db78b4955059933520194360`) and returns **exactly one** match. Fact A'
backs pairs 1 and 7 — `d8284f1` on `main`, parent `2381ca0`, with `5ffa8d6`,
`c224825`, `9f87ecd`, `647d4df`, `caa8267`, `ad77b13` and `2381ca0` all
ancestors. **Fact P** is why every pair names `d8284f1` and no pair names a
second commit for row 6's evidence: the full gate was re-run there from a clean
tree — row 6 7/7, pass 1 blocked at 5/7 on T-AI-05 and T-AI-06, driver 10/10 —
and **Fact O** carries the row-6 sources to that commit byte-identical. Fact B
backs the gate and pass-1 figures; Fact C backs pair 3's five-source citation
set at the extent it establishes, path existence at the commit named. Fact D
backs the ten-`main()` count in pair 3 and the closing sentence about that
census, at the extent of tracked `.cpp` files at that commit; both were
re-checked at `d8284f1` and are unchanged. Fact G backs the driver-suite clause;
Facts H and I back the T-AI-05 sweep figures and T-AI-01's printed counter.
Fact L backs the authoring sentences in pairs 3 and 6; Facts E and O together
back pair 6's `crew/tasks.py` check, written at its own extent — the file is
byte-unchanged `5ffa8d6` → `2381ca0` → `d8284f1`. Everything pair 3 says about
row 6's design — the decide/apply split, the module boundaries, the five stated
readings, Q9's tie-breaks and the driver commands — is from `spec/ai_spec.md`
and the build's commit message. §4.4's week-3 cell, §2.9 and §4.7 Stub 6 back
the schedule, shipping-opponent and cheats-at-nothing clauses.

**Derived figures.** §4.5's green count 36 → **42** and unclosed 33 → **27**:
row 6 closes six numbered IDs (T-AI-01..06) and GATE-AI-SMOKE mints none
(Fact N), so the written total 69 is unchanged and 18 + 9 + 9 + 6 = 42, leaving
69 − 42 = 27 — T-DATA-05 plus **26** across rows 7–10, which is the previous 32
less row 6's 6. Verified ledger rows 8 → **9** and the ✓ count in pair 5 follow
from the one row that flips. Row 8's remaining dependency in pairs 2 and 11 is
read off §4.11's own row-8 dependency cell, which names rows 5 and 7.

**Merge precondition (Fact M).** Apply this addendum only after `d8284f1` is
pushed: pairs 3, 4, 6, 8 and 11 add links to or cite it, pair 1 links it and its
parent `2381ca0`, and pair 7 keeps the document's existing claim that every
commit link above resolves. At authoring, `d8284f1` is committed and not pushed;
the Director authorises the crew push and the GDD merge together, as they did
for rows 1–5.

No pair contains the ruling text on "Playable via debug commands" in an OLD
block, and no pair states or implies a ruling on it.

## Open questions for the Director

1. §4.11 row 6's acceptance cell reads `T-AI-01..06 + self-play smoke`. The
   smoke run now exists under the name `GATE-AI-SMOKE` and mints no `T-` ID.
   Whether that cell should name the gate is a Director call; no pair here
   touches the table body.

## Change requests

All three are **unruled**, and no pair in this file states a ruling on any of
them. The first two are filed by `spec/ai_spec.md`; row 6 is the first caller to
exercise either, and both are consequences of rows landing in order rather than
defects row 6 introduced. The third is filed by the driver's start-of-turn
sequence, which pair 3 records as a fact about `d8284f1`.

| Existing § | Current text | Proposed change | Why |
|---|---|---|---|
| §2.7 | "one build per factory per turn" | Decide where the per-turn half is enforced — row 5, row 4, or a stated caller obligation | It is enforced only as one *pending* build per factory, which was the whole of it before row 5 owned the turn; once a build spawns the slot frees within the same turn. Row 6 takes `builtThisTurn` as a caller-supplied board fact and the driver maintains it, but a player's `build` command is not gated by it |
| §2.1 / §4.9 | The loop is *select → move → act*, and §4.9's snapshot carries one per-unit `hasActed` | Decide whether row 5 gains a second flag, or `hasActed` is defined to mean the act step only with movement tracked separately | Row 5 models one flag and the driver marks it on both `move` and `attack`, so a unit does one or the other; the AI therefore cannot close and strike in the same turn, which weakens §2.9's "if an enemy is within reach **after moving**, attack" |
| §2.7 | "A captured objective flips its Fame income to the new owner." | Rule the order of the three start-of-turn calls — repair, income and capture tick — and in particular whether the tick runs before or after income accrual | §2.7 states the outcome and not the timing. The debug driver's `openActiveTurn` runs start-of-turn repair, then income, then the capture tick, so an objective whose capture completes at the start of turn T pays its new owner from turn T+1. `spec/turn_spec.md` states neither the capture tick nor an order among the three calls. The phrase "flips income the following turn" admits two readings — the turn following the hold, or the turn following the flip |

## Handoffs

None owed. No pair states or restates a rule, a map fact, or a screen layout;
pair 3's Q9 clause reports that an already-ruled question is executed in code.
The three change requests above are rules questions and go to the Director, not
to `rules-designer`: the first two concern which built module owns an existing
§2 rule, and the third concerns a timing §2.7 does not state.
