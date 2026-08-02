# Technical design — the debug driver landed (tech-director)

> ✅ **APPLIED ADDENDUM — DO NOT RE-APPLY.**
> All four replacement pairs were applied verbatim to the master GDD and merged
> on 2026-08-02. Re-applying them would fail — the OLD anchors no longer match.
> All four are straight replacements; none is an insertion, so no anchor is
> retained by design in this file. Gate record: run `driver-built-5`, PASS, zero
> violations, after runs `-1` (3), `-2` (2), `-3` PASS, and `-4` (1) — `-4` was
> a re-gate of an already-passing draft, required because the Director's ruling
> changed pair 3 after `-3` passed. Master GDD md5
> `83fb9acbc19b8c6cb7adb037ea50d150` → `6a446c9408cbaf838a57f3326617e4d3`.
> Later changes to these sections need a NEW addendum file.

Four replacement pairs, all in **§3**. Three edit the italic *Status: live
tracker* paragraph, one edits the populated-rows paragraph beneath the ledger
table. Each **OLD** block was grepped against `source/gdd.md` (md5
`83fb9acbc19b8c6cb7adb037ea50d150`) and returns **exactly one** match. No NEW
block contains a fenced block, so every pair below uses three backticks. Every
NEW block is a **single line**: §3's status paragraph and its populated-rows
paragraph are each one long source line, and a splice that introduces a newline
breaks the paragraph.

`selfplay`, `driver_main`, `Driver.h` and `stratocracy_debug` together occur
**once** in the document — inside pair 2's OLD text — so the stale claim has one
site and pairs 2 and 3 close it. `2fcbf32` occurs twice, in pairs 1 and 4, and
leaves the document with them; the ancestry it was there to establish is carried
by the new chain (Fact A).

**Ruling, 2026-08-02, recorded so it is not re-opened.** This draft registered
one open question — whether §4.4's week-1 goal "Playable via debug commands" is
met at `9f87ecd`. The **Director ruled it met, in its current state**, on
2026-08-02. It is applied as the one-clause edit the question specified, at the
end of pair 3, and it is written **as a ruling on a judgement rather than as a
result a check produced** — no check establishes it, which is why it was
registered instead of decided. The limits that sentence sits beside are
unchanged: no turn structure, no capture, no Fame, no production, no AI, no
scenario file, and rows 4–8 hold no code. The ruling is recorded next to them,
not in place of them.

**Not in scope, per Fact E:** §4.5's *Specification outruns the build* row
counts **69** written acceptance IDs against **18** green at `c224825`.
`GATE-DRV-01..07` are not GDD acceptance IDs, the driver has no ledger row, and
no row flips — so that row is true as written and is not edited. **§4.4 stays a
plan** (ruled last stage); the ruling above changes what §3 records about the
week-1 goal, not §4.4's own cell, and no pair touches §4.4.

**Also not in scope:** the document contains exactly one bare backticked header
citation — §4.8's `Combat.h`, at `source/gdd.md` line 2440, the only match for a
backticked `*.h` anywhere in the file. It is a pre-existing instance of the
citation defect and no pair here touches it. Pair 3 writes
`cpp_reference/Combat.h` in full because that is the path pair 3 is itself
citing; it does not repair, and must not be read as repairing, line 2440.

---

## Pair 1 — §3 status paragraph, the commit this draft stands at

`main` has moved. Rows 1–3 keep citing `c224825` and stay correct, because it is
now the parent rather than the head.

**OLD**
```
This draft stands at 2026-08-02, at commit [`c224825`](https://github.com/jakemartin/stratocracy-crew/commit/c224825) — the head of `main` in the crew repo, whose parent is `2fcbf32`.
```
**NEW**
```
This draft stands at 2026-08-02, at commit [`9f87ecd`](https://github.com/jakemartin/stratocracy-crew/commit/9f87ecd) — the head of `main` in the crew repo, whose parent is [`c224825`](https://github.com/jakemartin/stratocracy-crew/commit/c224825).
```

## Pair 2 — §3 status paragraph, retiring the stale clause

The clause was true at `c224825` and is false at `9f87ecd`. It is removed here
rather than patched in place, because what replaces it is longer than the
sentence it sat inside; pair 3 states it. The surrounding sentence survives
intact — "rows 4–8 hold no code" is still true (Fact F).

**OLD**
```
rows 4–8 hold no code, and §4.4's week-1 goal "Playable via debug commands" is **unmet** — at `c224825` five tracked sources define `main()` (`cpp_reference/test_combat.cpp`, `cpp_reference/test_hex.cpp`, `cpp_reference/test_data.cpp`, `cpp_reference/test_move.cpp`, `cpp_reference/selfplay.cpp`), which are four test harnesses and a combat duel simulator, and none of them drives a unit around a board, and since §4.11's
```
**NEW**
```
rows 4–8 hold no code, and since §4.11's
```

## Pair 3 — §3 status paragraph, what landed after week 1

Appended at the end of the paragraph, after §4.5's sentence, so the "therefore"
in that sentence keeps the clause it refers to. The trailing `*` closes the
paragraph's italics and is reproduced. The driver runs on **built** modules, not
on three certified ones: row 2 does not flip in this same paragraph and §4.11
says "Row 2 is not green", and `cpp_reference/Data.h` is the module the driver
leans on hardest, so the clause names that rather than papering over it.

The **final sentence now carries the Director's ruling**, dated and attributed.
It is placed last, immediately after the sentence listing what the driver cannot
do, so the two are read together: the sentence of limits is unchanged and the
ruling does not thin it.

**OLD**
```
§4.5's *Specification outruns the build* risk is therefore reduced and re-scoped rather than retired, and that row now states the arithmetic.*
```
**NEW**
```
§4.5's *Specification outruns the build* risk is therefore reduced and re-scoped rather than retired, and that row now states the arithmetic. **What landed after week 1 is a debug driver**, at [`9f87ecd`](https://github.com/jakemartin/stratocracy-crew/commit/9f87ecd): `cpp_reference/driver_main.cpp` builds a command REPL, `build/stratocracy_debug`, over the built modules. The binary is **not citable** — `build/` is untracked, as the paragraph below the table already records — so what is cited is its five tracked sources, each probed present at that commit: `spec/driver_spec.md`, `cpp_reference/Driver.h`, `cpp_reference/Driver.good.cpp`, `cpp_reference/driver_main.cpp`, `cpp_reference/test_driver.cpp`. **Seven** tracked sources now define `main()` — `cpp_reference/test_combat.cpp`, `cpp_reference/test_hex.cpp`, `cpp_reference/test_data.cpp`, `cpp_reference/test_move.cpp`, `cpp_reference/test_driver.cpp`, `cpp_reference/selfplay.cpp`, `cpp_reference/driver_main.cpp` — five test harnesses, one combat duel simulator, and the REPL. **The driver holds no rules of its own.** Reach, path and move delegate to `cpp_reference/Move.h`, damage and counter eligibility to `cpp_reference/Combat.h`, distance and adjacency to `cpp_reference/Hex.h`, and every stat to `cpp_reference/Data.h` over `data/units.csv`, `data/terrain.csv` and `data/effectiveness.csv` — the row 2 module, whose ledger row is still unflipped; `forecast` and `attack` call one computation, so §2.6's *the forecast the player sees is exactly what resolves* holds structurally at this surface. Where an answer would need §4.11 rows 4–8 — who owns a unit, whose turn it is, what a scenario file looks like — the driver **refuses the command rather than deciding it**, so the build wrote no rule this document has not. Its gate is **GATE-DRV-01..07, 7/7 under clang++ and MSVC both**, and the checks that compare a value compute their expectation by calling the module directly rather than hardcoding it; those IDs are deliberately **not** `T-*`, because the driver is not a §4.7 stub and has no row in the ledger below, so §4.5's 69-ID count does not move and **no ledger row flips**. A human can now drive units: `move`, `attack`, `forecast` and `repair` are four of the sixteen commands `cpp_reference/Driver.good.cpp` dispatches at that commit. What there is no way to do is play a match: **no turn structure, no capture, no Fame, no production, no AI and no scenario file**, and the driver exposes none of it. On that record the Director **ruled, 2026-08-02, that §4.4's week-1 goal "Playable via debug commands" is met at `9f87ecd`, in its current state** — a ruling on a judgement rather than a result any check produced: the artifact exists and the match does not.*
```

## Pair 4 — §3 populated-rows paragraph, the lineage parenthetical

The same head-of-`main` fact, stated a second time under the table. Both must
move or the document contradicts itself.

**OLD**
```
*(Commit `c224825` is the head of `main`; its parent is [`2fcbf32`](https://github.com/jakemartin/stratocracy-crew/commit/2fcbf32), so `5ffa8d6` remains an ancestor and every commit link above resolves.
```
**NEW**
```
*(Commit `9f87ecd` is the head of `main`; its parent is [`c224825`](https://github.com/jakemartin/stratocracy-crew/commit/c224825), so `5ffa8d6` and `c224825` both remain ancestors and every commit link above resolves.
```

---

## Placement

| Pair | Section | Exact site |
|---|---|---|
| 1 | §3 | The italic *Status: live tracker* line, the sentence naming the head commit |
| 2 | §3 | The same line, the "What week 1 did **not** close" sentence |
| 3 | §3 | The same line, at its end, after §4.5's sentence — the ruling is its last sentence |
| 4 | §3 | The populated-rows paragraph below the ledger table, its lineage parenthetical |

Pairs 1–3 are disjoint spans of one source line and can be applied in any order.
No pair touches §1, §2, the ledger table itself, §4.4, §4.5, §4.7, §4.8, §4.9,
§4.11 or the Q register.

## Grounding

Fact A backs pairs 1 and 4 — `9f87ecd` on `main`, parent `c224825`, with
`5ffa8d6` and `c224825` both ancestors. Fact B backs pair 3's five-source
citation set and the reason `build/stratocracy_debug` is named but not cited;
the untracked status of `build/` is already stated in the paragraph pair 4
edits. Facts C, E and F back the `main()` count of seven, the gate line, and the
list of what does not exist.

Four of pair 3's claims rest on checks run against `9f87ecd` rather than on a
summary.

- **The delegation targets.** `git cat-file -e` reports **EXISTS** for
  `cpp_reference/Hex.h`, `cpp_reference/Move.h`, `cpp_reference/Data.h` and
  `cpp_reference/Combat.h`, so all four are cited at paths that resolve.
- **The command set.** `git show 9f87ecd:cpp_reference/Driver.good.cpp`
  dispatches sixteen commands — `attack`, `dist`, `exit`, `fixture`, `forecast`,
  `help`, `hp`, `map`, `move`, `path`, `place`, `quit`, `reach`, `remove`,
  `repair`, `units`. That is the extent pair 3 claims: commands the driver
  dispatches at that commit, not events a running game emits. §4.9's `Repaired`
  is an emitted event and a different thing; pair 3 does not mention it.
- **How the checks are built.** `git show 9f87ecd:cpp_reference/test_driver.cpp`
  computes its expectations by calling the modules — `reachable(...)` at line
  93, `findPath(...)` at line 126, `hexDistance(...)` at lines 152 and 232, and
  `resolveDamage(...)` at line 168. Pair 3 therefore says **the checks that
  compare a value** compute their expectation that way, which is what those five
  lines establish; it does not claim every check in the file does so.
- **What the clause does not certify.** "The built modules" is deliberately not
  "rows 1–3 certified": the same paragraph says **Row 2 does not flip** and
  §4.11 says **Row 2 is not green**, and the driver reads every stat through
  that module.

**Pair 3's last sentence is grounded differently from the rest, and says so.**
The week-1 verdict is a **Director ruling of 2026-08-02**, not a check result:
no probe, read or gate run establishes it, and the sentence attributes it and
dates it for that reason. The ruling carries **one** qualifier — *in its current
state* — and that qualifier is part of the ruling as given rather than a
softener added here. The sentence of limits that precedes it is byte-unchanged
from the draft that passed run `driver-built-3`.

Pair 2 removes a claim Facts A and C falsify; its OLD text remains a true
statement about `c224825`, which is why it is retired rather than corrected.
§2.6's forecast sentence is quoted from `source/gdd.md`.

## Open questions for the Director

**None.** The one question this draft registered — whether §4.4's week-1 goal
"Playable via debug commands" is met at `9f87ecd` — was ruled met, in its
current state, on 2026-08-02, and is applied at the end of pair 3.

## Change requests

None.

## Handoffs

None owed. Fact D is the reason: the driver decides nothing, so no pair here
states, restates or implies a rule, a map fact, or a screen layout. The week-1
goal being ruled met adds nothing for `ux-onboarding-designer` either — the REPL
is a developer surface with no §2.11 presence, and the ruling is recorded in §3
rather than creating any player-facing surface.
