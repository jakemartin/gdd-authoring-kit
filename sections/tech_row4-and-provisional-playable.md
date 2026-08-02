# Technical design — row 4 built, and the week-1 goal made provisional (tech-director)

> ✅ **APPLIED ADDENDUM — DO NOT RE-APPLY.**
> All fifteen replacement pairs were applied verbatim to the master GDD and merged
> on 2026-08-02. Re-applying them would fail — the OLD anchors no longer match.
> All fifteen are straight replacements; none is an insertion, so no anchor is
> retained by design. Gate record: run `row4-playable-3`, PASS, zero violations,
> after `-1` (1 `stat-drift`) and `-2` (3 `contradiction`, all in this file's own
> front matter, none in merged text). Master GDD md5
> `6a446c9408cbaf838a57f3326617e4d3` → `10b9a7ab4c5fbb4a7464faea37821122`.
> Later changes to these sections need a NEW addendum file.

Fifteen replacement pairs. Seven are in **§3**'s italic *Status: live tracker*
line, one is the ledger table's row 4, three are in the populated-rows paragraph
beneath it, two are in **§4.5**'s *Specification outruns the build* row, and two
are in **§4.11**'s preamble. Each **OLD** block was grepped against
`source/gdd.md` (md5 `6a446c9408cbaf838a57f3326617e4d3`) and returns **exactly
one** match. No NEW block contains a fenced block, so every pair uses three
backticks. §3's status paragraph, its populated-rows paragraph and §4.5's risk
row are each **one long source line**, so every NEW block for pairs 1–13 is a
single line; §4.11 is hard-wrapped and pairs 14–15 reproduce its wrapping.

**The amendment is the point of this file.** The Director's ruling of
2026-08-02 — that §4.4's week-1 goal "Playable via debug commands" is met at
`9f87ecd`, in its current state — **stands, and no pair here deletes, edits or
weakens it**. It is not inside any OLD block: pair 7 anchors on the eight words
after it. What pair 7 adds is the Director's qualification of the same day — the
state is acceptable *at this current time*, is *not a final call*, and the goal
should eventually include all game features as they come online. Recorded, the
goal is **provisionally met** and **re-opens as each system lands**, so the bare
word *met* cannot be read as permanent closure once rows 5–8 exist.

**Row 4 is early, not late.** §4.4 puts rows 4–5 in **week 3** (Fact D), so this
row is ahead of the milestone table. This document has been careful to
distinguish a row delivered early from a row delivered late, and pair 7 says
which this is. **§4.4 stays a plan** (ruled): no pair touches it.

**The harness is on the record.** Fact I supplies what an earlier draft of this
file could not state: a **Claude Code session** authored row 4 from
`spec/economy_spec.md`, not a live CrewAI run. Pair 10 attaches it to §3's
**existing** week-1 harness sentence rather than opening a third one — the
paragraph carries two authoring sentences and should keep carrying two.

**Live markers — the `stat-drift` finding, run `row4-playable-1`.** Moving a
paragraph's standing commit falsifies an unbound *now*. The gate found one such
sentence; pair 3 binds it. The table records the markers this addendum examined
in the four paragraphs it moves, and what it did with each.

| Site | Marker | Disposition |
|---|---|---|
| §3 status | "its first two links are **now** evidence" | Pair 2 drops it — the clause is rewritten to three links, unmarked |
| §3 status | "**Seven** tracked sources **now** define `main()`" | **The finding.** Pair 3 binds it to `9f87ecd`; pair 7 states eight at `647d4df` |
| §3 status | "A human can **now** drive units" | Pair 5 rebinds to "from that commit on" — true then and since, and no longer live |
| §3 status | "that row **now** states the arithmetic" | Kept. A cross-reference to §4.5, which still states arithmetic after pair 12; not a repo-state claim, so no commit binds it |
| §3 status | "the row 2 module, whose ledger row is **still** unflipped" | Kept. True of row 2 at `647d4df` — T-DATA-05 has not run, and pair 8 flips row 4, not row 2 |
| §3 populated | "Six rows **now** carry a ✓" | Pair 9 rewrites to "in the table above" — the count is a property of the table two lines up, not of a commit |
| §3 populated | "which the cells **now** name in full" | Kept. Document-state, bound to the adjacent table; unaffected by any commit move |
| §3 populated | "`crew/tasks.py` is **still** written against the Combat spec alone" | Kept. A present-tense fact about a file byte-unchanged from `5ffa8d6` to `647d4df` (Fact I), so moving the standing commit cannot falsify it; pair 10 states the same fact beside it |
| §4.5 | "**at this revision**"; "Row 2 is **now** that clause's worked example" | Both kept and both still true at `647d4df` — 69 is unmoved (Fact G) and row 2 is still unflipped |
| §4.11 preamble | "rows 1 and 3 have **since** flipped" | Carried forward, not removed: pair 14 rewrites it to "rows 1, 3 and 4 have since flipped". *Since* is bound by the clause before it — "when this table was written" — so it is anchored to the table rather than to a commit |

**Not in scope.** The Q register is unedited: Q4, Q5, Q6 and Q8 already read
RULED and pair 7 adds that four invariants execute them. §4.7's Stub 4 is
unedited, matching Stubs 1 and 3, which carry no built-annotation. §4.7's
**heading** is likewise unedited — it is dated "at 2026-08-01", so it records a
state rather than asserting a live count, and pair 14 says so **in the document**
at §4.11's undated twin, which is where a later reader would otherwise notice the
asymmetry and correct the wrong side of it. §4.8's bare `Combat.h` at line 2440
is the one pre-existing citation defect and no pair touches it.

---

## Pair 1 — §3 status paragraph, the head commit

**OLD**
```
This draft stands at 2026-08-02, at commit [`9f87ecd`](https://github.com/jakemartin/stratocracy-crew/commit/9f87ecd) — the head of `main` in the crew repo, whose parent is [`c224825`](https://github.com/jakemartin/stratocracy-crew/commit/c224825).
```
**NEW**
```
This draft stands at 2026-08-02, at commit [`647d4df`](https://github.com/jakemartin/stratocracy-crew/commit/647d4df) — the head of `main` in the crew repo, whose parent is [`9f87ecd`](https://github.com/jakemartin/stratocracy-crew/commit/9f87ecd).
```

## Pair 2 — §3 status paragraph, what week 1 did not close

The week-1 tense is preserved; the present-tense half moves and is bound to the
paragraph's new standing commit rather than to a bare *now*.

**OLD**
```
rows 4–8 hold no code, and since §4.11's critical path runs 1 → 3 → 4 → 5 → 6/8, its first two links are now evidence rather than schedule and **row 4 (Capture & Fame) is blocked on nothing but itself**.
```
**NEW**
```
rows 4–8 held no code then, and **row 4 has since landed** — recorded at the end of this paragraph — so at `647d4df` only rows 5–8 hold none; since §4.11's critical path runs 1 → 3 → 4 → 5 → 6/8, its first three links are evidence rather than schedule and **row 5 (Turn loop & win/tiebreak) is blocked on nothing but itself**.
```

## Pair 3 — §3 status paragraph, the entry-point count

**The gate's finding.** The sentence carried a live *now* with no commit
attached, in the same paragraph where pair 7 cites
`cpp_reference/test_economy.cpp` as tracked at `647d4df` — a sixth harness, so
seven was false the moment pair 1 moved the standing commit. It is bound to
`9f87ecd`, where seven was true and where the sentences around it now sit (pairs
4, 5, 6), and the current count is stated at the paragraph's standing commit, in
pair 7.

**OLD**
```
**Seven** tracked sources now define `main()` — `cpp_reference/test_combat.cpp`, `cpp_reference/test_hex.cpp`, `cpp_reference/test_data.cpp`, `cpp_reference/test_move.cpp`, `cpp_reference/test_driver.cpp`, `cpp_reference/selfplay.cpp`, `cpp_reference/driver_main.cpp` — five test harnesses, one combat duel simulator, and the REPL.
```
**NEW**
```
**Seven** tracked sources defined `main()` at that commit — `cpp_reference/test_combat.cpp`, `cpp_reference/test_hex.cpp`, `cpp_reference/test_data.cpp`, `cpp_reference/test_move.cpp`, `cpp_reference/test_driver.cpp`, `cpp_reference/selfplay.cpp`, `cpp_reference/driver_main.cpp` — five test harnesses, one combat duel simulator, and the REPL; **row 4 has since added an eighth**, counted at the end of this paragraph.
```

## Pair 4 — §3 status paragraph, what the driver refused

Four sentences about the driver were true at `9f87ecd` and are not true of the
head (Fact F). Pairs 3, 4, 5 and 6 bind each to the commit it describes rather
than restate it, so no claim is deleted and none is left standing false; what
the driver can no longer be said to refuse is stated once, in pair 7.

**OLD**
```
the driver **refuses the command rather than deciding it**, so the build wrote no rule this document has not.
```
**NEW**
```
the driver at that commit **refused the command rather than deciding it**, so the build wrote no rule this document has not.
```

## Pair 5 — §3 status paragraph, the no-flip clause and the driving human

Two adjacent sentences in one span. The first is true of the driver's own gate
and now sits in a paragraph where a row does flip; the second carried a bare
*now*. Neither claim is withdrawn — both are bound.

**OLD**
```
so §4.5's 69-ID count does not move and **no ledger row flips**. A human can now drive units:
```
**NEW**
```
so §4.5's 69-ID count does not move and **no ledger row flips on the driver's account**. A human can drive units from that commit on:
```

## Pair 6 — §3 status paragraph, the limits at `9f87ecd`

Re-tensed, not thinned: every item in the list is reproduced.

**OLD**
```
What there is no way to do is play a match: **no turn structure, no capture, no Fame, no production, no AI and no scenario file**, and the driver exposes none of it.
```
**NEW**
```
What there was no way to do at that commit is play a match: **no turn structure, no capture, no Fame, no production, no AI and no scenario file**, and the driver exposed none of it.
```

## Pair 7 — §3 status paragraph, the amendment and row 4

The OLD block is the last eight words of the ruling sentence plus the italic
close. The ruling itself is untouched and unquoted; the amendment attaches
directly to it, and row 4's record follows the amendment so that the re-opening
clause is read before the system that re-opened it. This block is the
paragraph's standing-commit block, so it is where the current entry-point count
belongs — **eight** at `647d4df`, at the extent the check establishes: entry
points in the tracked tree at that commit.

**OLD**
```
the artifact exists and the match does not.*
```
**NEW**
```
the artifact exists and the match does not. **The Director amended that ruling the same day, qualifying it rather than retracting it:** the current state is acceptable **at this current time** and is **not a final call**, because "Playable via debug commands" should eventually include **all game features as they come online**. The goal is therefore **provisionally met** — met against the feature set that existed at the commit it was ruled on, and **re-opened by each system that lands after it**, rows 5–8 included. The bare word *met* is a current-state acceptance and not a permanent closure. **Row 4 then landed**, at [`647d4df`](https://github.com/jakemartin/stratocracy-crew/commit/647d4df): **Capture & Fame economy**, gated **T-FAME-01..09, 9/9 under clang++ and MSVC both**, cited by five tracked sources each probed present at that commit — `spec/economy_spec.md`, `cpp_reference/Economy.h`, `cpp_reference/Economy.good.cpp`, `cpp_reference/Economy.buggy.cpp`, `cpp_reference/test_economy.cpp`. The last of those is a sixth harness, so **eight** tracked sources define `main()` at `647d4df` — the seven listed above plus `cpp_reference/test_economy.cpp` — six test harnesses, one combat duel simulator, and one debug REPL. **No ID is left uncovered:** unlike row 2 there is no in-editor half, so the full acceptance set closes at one commit, Q29 is satisfied, and the row flips in the table below. **No new acceptance ID was written**, so §4.5's 69 stands and its green count moves 18 → 27. §4.4 schedules rows 4–5 for **week 3**, so this row is **ahead of the milestone table, not behind it** — the opposite of the debt recorded above, and the two are different facts. Row 4 owns the economy and not the turn: it never advances a turn and never decides whose turn it is, taking the turn number as an argument, which is why it could land before row 5. **Four of its nine invariants execute a ruled question** rather than a stated reading — Q8 (no accrual on turn 1; Fame committed at queue time), Q4 (capture progress is tile-held, resets, and never transfers), Q5 (the flag award replaces rather than stacks, so 500 and not 650) and Q6 (no undamaged-strike bonus, asserted by absence) — so those four rulings are executed rather than only written. The driver reaches it: `objectives`, `fame`, `turn <n>`, `income <side>`, `build <side> <Type> <col> <row>` and `capture <side>` are new commands, plus a kill award paid through `attack`, and each is a call into `cpp_reference/Economy.h`, so the driver still holds no rules of its own; `turn <n>` is a **debug setter, not a turn structure**, and `GATE-DRV-01..07` is still 7/7 and still not `T-*`. What there is no way to do at `647d4df` is still play a match: there is **no turn structure, no AI and no scenario file**, and a setter for the turn number is not the first of those.*
```

## Pair 8 — §3 ledger table, row 4

Formatted on rows 1 and 3, which cite the good implementation and its test at
one commit. `cpp_reference/Economy.buggy.cpp` is a gate fixture and is cited in
the status paragraph, not here.

**OLD**
```
| Capture & Fame economy | *pending* | — | *pending build* |
```
**NEW**
```
| **Capture & Fame economy** | agent | ✓ | `cpp_reference/Economy.good.cpp` + `cpp_reference/test_economy.cpp` @ [`647d4df`](https://github.com/jakemartin/stratocracy-crew/commit/647d4df) · T-FAME-01..09 (9/9) |
```

## Pair 9 — §3 populated-rows paragraph, the count

Data tables is unchanged in kind — it still carries evidence without a ✓ — and
moves from seventh to eighth only because a row flipped above it. The count is a
property of the table two lines up, not of a commit, so the bare *now* is
replaced by the binding that is actually true rather than by a commit hash.

**OLD**
```
**Six rows now carry a ✓, and a seventh carries evidence without one.**
```
**NEW**
```
**Seven rows carry a ✓ in the table above, and an eighth carries evidence without one.**
```

## Pair 10 — §3 populated-rows paragraph, row 4's evidence, its harness, and the ordinal

The OLD span opens on the sentence that already states the harness rule — *the
two sentences differ because the harness differed* — so row 4's harness clause
lands **against that sentence** and the paragraph still carries two authoring
sentences rather than three. Row 4's evidence precedes its attribution, so the
row is introduced before it is attributed. The `crew/tasks.py` check is written
at its own extent: it establishes that the file has not moved between those two
commits, and nothing about what any run did. The Data-tables ordinal moves in
the same span.

**OLD**
```
The author is an agent either way; the two sentences differ because the harness differed, and reporting a harness that did not run is the exact failure this ledger exists to prevent. Two IDs are recorded as **uncovered** rather than omitted: **T-DATA-05**, the in-editor Unreal Automation half, and **T-MOVE-07**, reserved and unwritten on Q2. The first is why **Data tables** is the seventh row and does *not* flip
```
**NEW**
```
The author is an agent either way; the two sentences differ because the harness differed, and reporting a harness that did not run is the exact failure this ledger exists to prevent. **Capture & Fame economy** joined at [`647d4df`](https://github.com/jakemartin/stratocracy-crew/commit/647d4df) — T-FAME-01..09, **9/9 under clang++ and MSVC both** — and unlike rows 2 and 3 it leaves **no ID uncovered**: it has no in-editor half and no reserved ID, so its full acceptance set closes at one commit and Q29 is satisfied rather than blocking. **It belongs to the second of those two sentences and does not start a third:** a **Claude Code session** authored it from the Director-written stub `spec/economy_spec.md`, again **not a live CrewAI run** — `crew/tasks.py` is **byte-unchanged from `5ffa8d6` to `647d4df`**, so the file the live crew runs from still describes the Combat spec alone. That check establishes that the file has not moved across those commits; it is not evidence about what any run did, and the harness is reported here because it is known and not because a diff proved it. Two IDs are still recorded as **uncovered** rather than omitted: **T-DATA-05**, the in-editor Unreal Automation half, and **T-MOVE-07**, reserved and unwritten on Q2. The first is why **Data tables** is the eighth row and does *not* flip
```

## Pair 11 — §3 populated-rows paragraph, the lineage parenthetical

The same head-of-`main` fact stated a second time; both sites must move.

**OLD**
```
*(Commit `9f87ecd` is the head of `main`; its parent is [`c224825`](https://github.com/jakemartin/stratocracy-crew/commit/c224825), so `5ffa8d6` and `c224825` both remain ancestors and every commit link above resolves.
```
**NEW**
```
*(Commit `647d4df` is the head of `main`; its parent is [`9f87ecd`](https://github.com/jakemartin/stratocracy-crew/commit/9f87ecd), so `5ffa8d6`, `c224825` and `9f87ecd` all remain ancestors and every commit link above resolves.
```

## Pair 12 — §4.5, the risk row's arithmetic

69 is unchanged because no ID was written. Green is 18 + 9 = **27** across two
commits, and the row says which at which rather than attributing all 27 to one.
Unclosed is 69 − 27 = **42**: T-DATA-05 plus the 41 in rows 5–10 (50 − 9). "This
week" becomes a commit range for the same reason pair 3 exists.

**OLD**
```
**Specification outruns the build** — **69** written acceptance IDs at this revision (§4.7–§4.11) against **6** verified ledger rows (§3). **Reduced and re-scoped at 2026-08-02, not retired:** no new ID was written this week, and **18** of the 69 are green at `c224825` — rows 1 and 3 closed their full acceptance sets and row 2's headless half passed — so the first two links of the critical path are evidence rather than schedule. **51 IDs remain unclosed**: T-DATA-05, which leaves row 2 unflipped, plus the 50 in rows 4–10, which hold no code
```
**NEW**
```
**Specification outruns the build** — **69** written acceptance IDs at this revision (§4.7–§4.11) against **7** verified ledger rows (§3). **Reduced and re-scoped at 2026-08-02, not retired:** no new ID has been written since `c224825`, and **27** of the 69 are green — **18** at `c224825`, where rows 1 and 3 closed their full acceptance sets and row 2's headless half passed, and **9** at `647d4df`, where T-FAME-01..09 closed row 4 — so the first three links of the critical path are evidence rather than schedule. **42 IDs remain unclosed**: T-DATA-05, which leaves row 2 unflipped, plus the 41 in rows 5–10, which hold no code
```

## Pair 13 — §4.5, the mitigation's slip clause

**OLD**
```
so a slip in rows 4–8 moves everything downstream
```
**NEW**
```
so a slip in rows 5–8 moves everything downstream
```

## Pair 14 — §4.11 preamble, which rows have flipped, and why §4.7's heading does not move

The second sentence is the one-line note that stops a later reader from
"correcting" §4.7's heading to match this one. It sits here, beside the undated
twin, because that is where the asymmetry is visible. The OLD block's trailing
lowercase `rows` becomes a capitalised `Rows`, so the following source line —
`9–10 are the §4.9 and §4.10 systems.` — opens a sentence rather than continuing
one.

**OLD**
```
Rows 1–8 are the §4.7 stubs — the eight ledger rows that read `*pending*` when
this table was written, of which **rows 1 and 3 have since flipped** (§3); rows
```
**NEW**
```
Rows 1–8 are the §4.7 stubs — the eight ledger rows that read `*pending*` when
this table was written, of which **rows 1, 3 and 4 have since flipped** (§3).
§4.7's heading names the same eight **as at 2026-08-01** and is dated for that
reason: it records a state and is not a live count, so it does not move when a
row flips and is not out of step with this sentence. Rows
```

## Pair 15 — §4.11 preamble, what depends on landed code

Both of row 5's dependencies are named with the commit each landed at, so the
sentence carries no unbound marker of its own.

**OLD**
```
**Rows 1 and 3 are green at `c224825`**, so rows 4–8 depend on landed code
rather than on scheduled code.
```
**NEW**
```
**Rows 1 and 3 are green at `c224825`, and row 4 at `647d4df`**, so rows 5–8
depend on landed code rather than on scheduled code, and **row 5 is the critical
path's next link**, both of its dependencies having landed — row 4 at `647d4df`
and Combat/Repair at `5ffa8d6`.
```

---

## Placement

| Pair | Section | Exact site |
|---|---|---|
| 1 | §3 | *Status: live tracker* line, the head-commit sentence |
| 2 | §3 | Same line, the "What week 1 did **not** close" sentence |
| 3 | §3 | Same line, the `main()` entry-point sentence |
| 4 | §3 | Same line, the driver's refusal sentence |
| 5 | §3 | Same line, the GATE-DRV clause and the sentence after it |
| 6 | §3 | Same line, the sentence of limits |
| 7 | §3 | Same line, its end — the amendment, then row 4 |
| 8 | §3 | The ledger table, row 4 |
| 9 | §3 | Populated-rows paragraph, its opening sentence |
| 10 | §3 | Same paragraph, from the harness sentence through the Data-tables ordinal |
| 11 | §3 | Same paragraph, the lineage parenthetical |
| 12 | §4.5 | *Specification outruns the build*, the risk cell |
| 13 | §4.5 | The same row, the mitigation cell |
| 14 | §4.11 | Preamble, sentence 1 |
| 15 | §4.11 | Preamble, the green-rows sentence |

Pairs 1–7 are disjoint spans of one source line and apply in any order; so do
9–11 and 12–13. Pair 3's site sits between pairs 2 and 4, and pair 5's span ends
where pair 6's begins, with no overlap. No pair touches §1, §2, §4.4, §4.7,
§4.8, §4.9, §4.10, §4.11's table body, or the Q register.

## Grounding

Fact A backs pairs 1 and 11 — `647d4df` on `main`, parent `9f87ecd`, with
`5ffa8d6`, `c224825` and `9f87ecd` all ancestors. Fact B backs pair 8's evidence
cell and the gate line in pairs 7 and 10, including the no-uncovered-ID claim
and the Q29 consequence. Fact C backs pair 7's five-source citation set, each
probed `EXISTS` at that commit; `build/` is untracked, which the paragraph pair
11 edits already records, so nothing new is claimed about it. Fact D backs pair
7's week-3 sentence — the row is early against §4.4, and §4.4 itself is not
edited. Fact E backs pair 7's "owns the economy and not the turn" clause and its
four ruled-question invariants; the Q4/Q5/Q6/Q8 readings quoted there are the
ones already written in the Q register, not new ones. Fact F backs pairs 4, 5
and 6's binding and pair 7's command list, the debug-setter caveat, and the
unchanged `GATE-DRV-01..07`. Fact G backs every figure in pair 12 and the
18 → 27 clause in pair 7, and is why "no new ID" can be stated across the whole
`c224825` → `647d4df` range. Fact H backs pairs 2 and 15 — rows 5–8 hold no code
and row 5 is the next link; row 5's second dependency, Combat/Repair at
`5ffa8d6`, is read from §4.11's own row-5 cell. Fact I backs pair 10's harness
clause: the Claude Code session and the Director-written stub are the Director's
own statement, and the `crew/tasks.py` diff is written as corroboration at its
own extent — the file is byte-unchanged between those two commits, which is a
fact about the file and not about any run. `crew/tasks.py` occurs once in the
document, inside the sentence pair 10 extends, so the harness claim has one site
and pair 10 is at it.

**The entry-point counts.** Seven at `9f87ecd` is the document's own existing
figure, kept and bound rather than recomputed (pair 3). Eight at `647d4df` is
the count supplied with the gate finding — `git ls-tree -r` plus a `main(` grep
over tracked `.cpp` — and pair 7 states it at that extent: entry points in the
tracked tree at that commit, six test harnesses, one duel simulator, one debug
REPL. The eighth is `cpp_reference/test_economy.cpp`, which Fact C independently
probes `EXISTS` at the same commit, so the increment and the citation agree.

The amendment in pair 7 is a **Director ruling of 2026-08-02**, not a check
result, and is written as one — dated, attributed, and attached to the ruling it
qualifies. No probe or gate run establishes it, which is why it is recorded
rather than derived. The ruling it amends is byte-unchanged and appears in no
OLD block.

## Open questions for the Director

**None.** The one question this draft carried — which harness authored row 4 at
`647d4df` — was answered by the Director (Fact I) and is written into pair 10.
The register is empty.

## Change requests

None.

## Handoffs

None owed. No pair states, restates or implies a rule, a map fact, or a screen
layout: pair 7's Q4/Q5/Q6/Q8 clause reports that four already-ruled questions
are executed in code and quotes their existing register text, and the Fame
numbers it names (500 not 650) are §3's, unchanged.
