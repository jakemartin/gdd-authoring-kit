# Addendum — build-order row 10 part (c), and Rulings U, V, W (tech-director)

Exact OLD → NEW pairs against `source/gdd.md`. Every OLD was checked to be a
unique substring of that file before it was written here.

---

### Pair 1 — §3's status line: this round's commit and its ancestry

Re-points the line to this round's crew commit, states the ancestry that was
measured, and gives the new sha the same no-branch-claim clause the line
already gives `9dec48c`. The retained final clause is pinned to the commit it
was measured against rather than carried forward.

**OLD**

```
This draft stands at 2026-08-05, at commit [`ec15be6`](https://github.com/jakemartin/stratocracy-crew/commit/ec15be6) in the crew repo and at `9dec48c` in the Stratocracy UE project repo. In the crew repo, [`737f666`](https://github.com/jakemartin/stratocracy-crew/commit/737f666), [`41a1452`](https://github.com/jakemartin/stratocracy-crew/commit/41a1452) and [`d837fc8`](https://github.com/jakemartin/stratocracy-crew/commit/d837fc8) are each an ancestor of `ec15be6`, measured with `git merge-base --is-ancestor` per sha rather than read off a branch, and every crew-repo commit this GDD cites is an ancestor of `ec15be6`, measured the same way per sha.
```

**NEW:**

```
This draft stands at 2026-08-05, at commit [`1ee890e`](https://github.com/jakemartin/stratocracy-crew/commit/1ee890e) in the crew repo and at `9dec48c` in the Stratocracy UE project repo. In the crew repo, [`ec15be6`](https://github.com/jakemartin/stratocracy-crew/commit/ec15be6), [`737f666`](https://github.com/jakemartin/stratocracy-crew/commit/737f666) and [`d837fc8`](https://github.com/jakemartin/stratocracy-crew/commit/d837fc8) are each an ancestor of `1ee890e`, measured with `git merge-base --is-ancestor` per sha rather than read off a branch. `1ee890e` is cited as a commit, and this line makes no claim about how it stands to any branch. Measured at `ec15be6`, every crew-repo commit this GDD cited then is an ancestor of `ec15be6`, measured the same way per sha.
```

---

### Pair 2 — Ruling U, the reachability parenthetical's UE-project half

**Deletion tripwire — fired.** This pair *deletes* a claim rather than updating
it: the parenthetical currently asserts that `99fcb84` and `9dec48c` are *"each
reachable from the head of `master`"* in the UE project repo. It goes rather
than changes because the form itself is the defect — a head expires and a sha
does not, and the §3 status line above already records one such expiry. What
replaces it is the weaker claim that is durable: each is cited as a commit, and
the sentence makes no branch claim. Ruling S made exactly this move for the
crew half earlier in this same parenthetical, so the parenthetical now speaks
one way about both repos. Pair 15 repairs the crew half's own instance of that
sentence, which is the sentence this pair's passage opens with.

**OLD**

```
`99fcb84` and `9dec48c` are not objects in it at all, and each is reachable from the head of `master` in the **Stratocracy** UE project repo, whose tree it pins.
```

**NEW:**

```
`99fcb84` and `9dec48c` are not objects in it at all: each is a commit in the **Stratocracy** UE project repo, whose tree it pins, and this parenthetical makes no claim about how either stands to any branch there (ruled 2026-08-05). The claim this replaces was that each is reachable from the head of `master`; a head expires and a sha does not, which is the defect the §3 status line above records, so the form goes rather than being re-measured. That is Ruling S's move applied to the other half, and the ruling is confined to this parenthetical for the same reason Ruling S was: restating every reachability claim in this document against a named commit was considered when Ruling S was made and declined, and that declining stands.
```

---

### Pair 3 — Ruling V, the start-of-turn order gains a named owner

The two implementations were recorded side by side with neither named as the
owner. This names one, records the other as a second implementation with a
stated retirement condition, and keeps the convergence filed rather than
calling it done.

**OLD**

```
and `cpp_reference/Driver.good.cpp`'s `openActiveTurn` performs that same sequence over the driver's `Session`. That is a duplication of a ruled **order** and not of a rule a module owns, and it is filed as a change request in `spec/replay_spec.md`.
```

**NEW:**

```
and `cpp_reference/Driver.good.cpp`'s `openActiveTurn` performs that same sequence over the driver's `Session`. **`Replay.h::openTurn` owns that sequence over `strat::GameState` (ruled 2026-08-05)**, and `openActiveTurn` is recorded as a **second implementation over the driver's own `Session`**, retained until the driver reads from `GameState`. That is a duplication of a ruled **order** and not of a rule a module owns, and the convergence stays **filed rather than done**: the change request in `spec/replay_spec.md` is not withdrawn, it gains an owner.
```

---

### Pair 4 — the record of part (c)

Goes at the end of §3's status paragraph, immediately before its closing italic
marker, following the posture the part (a) and part (b) records before it hold.
The OLD carries that closing marker so the anchor does not stop one character
short of it.

**OLD**

```
**How `ec15be6` was authored is deliberately not stated:** no harness claim is made for it, because none was established.*
```

**NEW:**

```
**How `ec15be6` was authored is deliberately not stated:** no harness claim is made for it, because none was established. **Build-order row 10's part (c) then landed**, at [`1ee890e`](https://github.com/jakemartin/stratocracy-crew/commit/1ee890e), with the UE project repo unmoved at `9dec48c`. New in the crew repo: `spec/balance_spec.md`, `cpp_reference/Balance.h`, `cpp_reference/Balance.good.cpp`, `cpp_reference/Balance.buggy.cpp` and `cpp_reference/test_balance.cpp`; modified: `crew/tools.py` and `crew/offline.py`. **What landed is a producer of §4.10 command logs**, and the in-editor Automation harness `T-SAVE-06` waits on is untouched by it. The new module is registered as registry row `balance` in `crew/tools.py`, so it runs under the `python run.py` gate rather than by an ad-hoc compile, and it is row 10's **third** registry row beside `save` and `replay`: its link set encodes part (c)'s own dependency claim — rows 4, 5 and 6, the command set, the match that runs to a result, and the AI that plays it — while folding it into the `replay` row would have put row 6 inside part (b)'s stated claim. `cpp_reference/test_balance.cpp` is a thirteenth harness, so **fifteen** tracked sources define `main()` at [`1ee890e`](https://github.com/jakemartin/stratocracy-crew/commit/1ee890e) — thirteen test harnesses, one combat duel simulator, and one debug REPL — a figure taken by enumerating them at that commit with `git grep -l` and diffing that list against the fourteen at [`ec15be6`](https://github.com/jakemartin/stratocracy-crew/commit/ec15be6) rather than by adding one to a count above: the difference is exactly `cpp_reference/test_balance.cpp`, and nothing was removed. The gate is **`T-SAVE-07` plus `GATE-BALANCE-*`, 12/12 under clang++ and MSVC both**. Pass-1 `cpp_reference/Balance.buggy.cpp` is blocked at **6/12** under both compilers — **six FAIL lines, identical under each, and predicted in full at clause level before the run**: `GATE-BALANCE-TRANSLATE-ATTACK-IS-TARGET-HEX`, `GATE-BALANCE-TRANSLATE-BUILD-NAMES-THE-UNIT-BUILT`, `GATE-BALANCE-RUN-ENDS-WITH-A-TIER`, `GATE-BALANCE-COMMAND-SET-IS-THE-AIS-FOUR`, `GATE-BALANCE-LOG-HOLDS-ONLY-ACCEPTED-COMMANDS`, and `T-SAVE-07` clause (b). **What the defective module did not disturb is recorded rather than smoothed over: `T-SAVE-07` clauses (a) and (c) PASSED against it.** The §4.10 format is agnostic to whether the rules accepted a command, so a log of refused entries still validates and still round-trips byte-identically; only clause (b), which replays the log, can see the difference, which is why this ID's discriminating power sits in one clause of three. The gate's own run emitted a **35-command log over a 6-turn cap**, printed by the runner. **`GATE-BALANCE-*` mint no acceptance ID**, on the `GATE-SAVE-PARSE` and `GATE-REPLAY-*` precedent. **No acceptance ID was written**, so §4.5's written-ID count does not move at this landing, its green count moves **60 → 61** and its unclosed count moves **11 → 10**. **The module owns the translation** between row 6's command vocabulary and §4.9's, and the discipline that only an **accepted** command enters the log; it chooses no move — `nextCommand` does — and applies no rule — `applyCommand` does. **A self-play log carries four command kinds, not five, and that is a property of the AI rather than of the format.** `cpp_reference/Ai.h` states that capture is deliberately outside the AI's vocabulary — a turn-boundary event the caller runs beside income, the AI's part of it being the move onto the objective (`T-AI-03`) — so `AiCommandKind` has four members where §4.9 has five, and a self-play match emits `Move`, `Attack`, `Build` and `EndTurn` and never `Capture`. The complete §4.9 command set was exercised by part (b)'s hand-authored log at [`ec15be6`](https://github.com/jakemartin/stratocracy-crew/commit/ec15be6). `T-SAVE-07` asserts **format compatibility, not command coverage**, so those four are its whole written fixture set, Q29 is satisfied over that set, and the gate asserts the four are present and the fifth absent rather than leaving the absence to be read as a shortfall. Part (c) drives its match through `applyCommand`, so the ruled start-of-turn order runs via `Replay.h::openTurn` here and not via the driver's `openActiveTurn`. **The module could not be named `Selfplay`, and the reason is a fact about the repo rather than a preference:** `cpp_reference/selfplay.cpp` is tracked and `crew/tools.py::ensure_workspace` copies it into `build/` on every gate call, the build filesystem is case-insensitive, so a `Selfplay.cpp` authored beside it is the same file — the duel harness's `main()` replaced the module, which surfaced as a linker error naming a duplicate `main` rather than as an overwrite — and §4.9 names `selfplay.cpp` in its enumeration of what is excluded from vendoring, so renaming that file would falsify a merged sentence. `Balance` is also the name this document already uses for the role that owns the artifact. **`cpp_reference/selfplay.cpp` is unchanged by this landing**: it is still tracked, still a combat-only 1v1 duel harness over `cpp_reference/Combat.h` that prints a table of duel outcomes and opens no file, still one of the files §4.9 excludes from vendoring because a UBT module cannot hold a second `main()`, and still not a producer of a §4.10 log. It did not become the new module and was not replaced by it. **`Balance` is deliberately not vendored** on the same ruling the other two unvendored modules stand on (§4.9), and `T-INT-01` and `T-INT-04` are unaffected — still 2/2 at `rulesCommit` `d837fc8`, run this session after the change. **Nothing was compiled by UBT at this landing, no editor was launched, and no UE project file was touched.** **`T-SAVE-07` closes here.** **`T-SAVE-06` did not close**: it is the only † of row 10's seven, it is asserted jointly with `T-INT-02`, and no in-editor Automation harness exists. **Row 10's acceptance set therefore does not close**, on the Q29 reading applied per acceptance ID as well as per row, and its unclosed count moves **2 → 1**, `T-SAVE-06` alone. **No ledger row is created, flipped or removed by this landing**: §4.11 calls row 10 a *proposed* ledger row, which is row 9's posture and deliberately not the partial-pass posture of rows 2, 7 and 8, and the row the Director named without creating it is created as one row when its full acceptance set closes. **How `1ee890e` was authored is deliberately not stated:** no harness claim is made for it, because none was established.*
```

---

### Pair 5 — §4.5's green total

**OLD**

```
**60** of the 71 are green
```

**NEW:**

```
**61** of the 71 are green
```

---

### Pair 6 — §4.5's green-by-commit decomposition

Adds this landing's term.

**OLD**

```
run over the command set part (c) requires, without closing that row's acceptance set either — so every row on the critical path has now landed
```

**NEW:**

```
run over the command set part (c) requires, without closing that row's acceptance set either, and **1** at [`1ee890e`](https://github.com/jakemartin/stratocracy-crew/commit/1ee890e), where `T-SAVE-07` closed on row 10's part (c) over a self-play log written in this format, without closing that row's acceptance set either — so every row on the critical path has now landed
```

---

### Pair 7 — §4.5's unclosed total

**OLD**

```
**11 IDs remain unclosed**
```

**NEW:**

```
**10 IDs remain unclosed**
```

---

### Pair 8 — §4.5's row-10 term

The tail of the unclosed enumeration: the term itself, and what the ID behind
it waits on.

**OLD**

```
and the **2** left in row 10, whose parts (a) and (b) have since landed — `T-SAVE-04` closed at [`737f666`](https://github.com/jakemartin/stratocracy-crew/commit/737f666) and `T-SAVE-01`, `T-SAVE-02`, `T-SAVE-03` and `T-SAVE-05` at [`ec15be6`](https://github.com/jakemartin/stratocracy-crew/commit/ec15be6), part (b) having run over the command set part (c) requires — leaving `T-SAVE-06` on the in-editor Automation harness and `T-SAVE-07` on a self-play log written in the §4.10 format (§3)
```

**NEW:**

```
and the **1** left in row 10, whose parts (a), (b) and (c) have all since landed — `T-SAVE-04` closed at [`737f666`](https://github.com/jakemartin/stratocracy-crew/commit/737f666), `T-SAVE-01`, `T-SAVE-02`, `T-SAVE-03` and `T-SAVE-05` at [`ec15be6`](https://github.com/jakemartin/stratocracy-crew/commit/ec15be6), part (b) having run over the command set part (c) requires, and `T-SAVE-07` at [`1ee890e`](https://github.com/jakemartin/stratocracy-crew/commit/1ee890e) over a self-play log written in the §4.10 format — leaving `T-SAVE-06` on the in-editor Automation harness, which is now the whole of what row 10 lacks (§3)
```

---

### Pair 9 — §4.4's week-3 cell

The cell named two IDs as still waiting; one of them closed.

**OLD**

```
**Two still wait**: `T-SAVE-06` on the in-editor Automation harness it is asserted jointly with `T-INT-02` on, and `T-SAVE-07` on a self-play log written in the §4.10 format, which wk 4's self-play is scheduled to produce.
```

**NEW:**

```
**`T-SAVE-07` is green at [`1ee890e`](https://github.com/jakemartin/stratocracy-crew/commit/1ee890e)** (§3), on row 10's part (c), which emitted a self-play match in the §4.10 format — ahead of the wk-4 cell that scheduled it rather than behind it. **One still waits**: `T-SAVE-06`, on the in-editor Automation harness it is asserted jointly with `T-INT-02` on.
```

---

### Pair 10 — §4.4's week-4 cell

The cell closes `T-SAVE-07` on this week's own output; it closed earlier. The
point the cell makes about dialect drift is retained, because it is what the ID
asserts and is unaffected by when it ran.

**OLD**

```
**T-SAVE-07 (harness compatibility) closes here**, not in wk 5: one format, no dialect drift between a save and a balance log
```

**NEW:**

```
**T-SAVE-07 (harness compatibility) closed ahead of this cell**, at [`1ee890e`](https://github.com/jakemartin/stratocracy-crew/commit/1ee890e) on row 10's part (c) (§3), rather than here and certainly not in wk 5 — the reason it was placed here holds either way: one format, no dialect drift between a save and a balance log. What this week still owes is the sims and the tuning themselves
```

---

### Pair 11 — §4.9's unvendored modules, and the disposition of each

Ruling R's statement covered two modules; a third landed under the same
standing reason. The three do not share one fate in this document's other
claims, so each is named rather than counted into a cardinal alone.

**OLD**

```
**Two crew modules exist and are deliberately
not vendored (ruled 2026-08-05).** `Save` landed at
[`737f666`](https://github.com/jakemartin/stratocracy-crew/commit/737f666) and
`Replay` at
[`ec15be6`](https://github.com/jakemartin/stratocracy-crew/commit/ec15be6)
(§3), and both stay out of `Source/StratRules/`, where they would be an
eleventh and a twelfth module beside the ten enumerated above. §3 records that
no bridge exists — no load mapping, no command surface, no event list, no
actor and no widget — so §4.9 part 2 is unbuilt and the bridge consumer that
would read them is still hypothetical, while vendoring now would re-date
`T-INT-01`'s and `T-INT-04`'s closures. That is a decision rather than an
omission, and **nothing re-dates on their account**: `T-INT-01` stays green at
`d837fc8` and `T-INT-04` at `b23823f`, and no UE project commit was made at
either landing. The enumeration above is correct as it stands and gains only
the statement that two modules were left out on purpose.
```

**NEW:**

```
**Three crew modules exist and are deliberately
not vendored (ruled 2026-08-05).** `Save` landed at
[`737f666`](https://github.com/jakemartin/stratocracy-crew/commit/737f666),
`Replay` at
[`ec15be6`](https://github.com/jakemartin/stratocracy-crew/commit/ec15be6) and
`Balance` at
[`1ee890e`](https://github.com/jakemartin/stratocracy-crew/commit/1ee890e)
(§3), and all three stay out of `Source/StratRules/`, where they would be an
eleventh, a twelfth and a thirteenth module beside the ten enumerated above.
§3 records that no bridge exists — no load mapping, no command surface, no
event list, no actor and no widget — so §4.9 part 2 is unbuilt and the bridge
consumer that would read them is still hypothetical, while vendoring now would
re-date `T-INT-01`'s and `T-INT-04`'s closures. That is a decision rather than
an omission, and **nothing re-dates on their account**: `T-INT-01` stays green
at `d837fc8` and `T-INT-04` at `b23823f`, both still passing 2/2 at
`rulesCommit` `d837fc8` after the third module landed, and no UE project commit
was made at any of the three landings. The enumeration above is correct as it
stands and gains only the statement that three modules were left out on
purpose. `cpp_reference/selfplay.cpp` is **not** one of the three and is
excluded for the different reason stated above — a UBT module cannot hold a
second `main()` — and it stays in that exclusion list unchanged.
```

---

### Pair 12 — §4.11 row 10's cell records part (c)

**OLD**

```
`T-SAVE-06` waits on the in-editor Automation harness and `T-SAVE-07` on a self-play log written in this format, so this row holds code without closing its set (§3).
```

**NEW:**

```
`T-SAVE-06` waits on the in-editor Automation harness and `T-SAVE-07` on a self-play log written in this format, so this row holds code without closing its set (§3). **Part (c) has since landed**, at [`1ee890e`](https://github.com/jakemartin/stratocracy-crew/commit/1ee890e), on a third registry row whose link set encodes exactly the dependency this cell states — rows 4, 5 and 6: `T-SAVE-07` is green there under clang++ and MSVC both, beside `GATE-BALANCE-*`, which mint no acceptance ID. That log carries the four command kinds row 6's AI emits and not the fifth, `Capture` being outside the AI's vocabulary by design (`T-AI-03`), and `T-SAVE-07` asserts format compatibility rather than command coverage, so its whole written fixture set ran. **`T-SAVE-06` is now the only ID this row lacks**, so its set closes on the editor pass alone (§3).
```

---

### Pair 13 — Ruling W, §4.11 row 10's acceptance column

Rows 6 and 8 carry their gate names in this column; row 10 carried only its
numbered IDs. None of the three gate families mints an acceptance ID, so this
moves no §4.5 figure. The two wildcard families are written in backticks, the
way this document writes them everywhere else, because two bare `*` on one
table row would render the text between them as emphasis.

**OLD**

```
T-SAVE-01..07 (**T-SAVE-06 †**)
```

**NEW:**

```
T-SAVE-01..07 (**T-SAVE-06 †**) + `GATE-SAVE-PARSE`, `GATE-REPLAY-*`, `GATE-BALANCE-*`
```

---

### Pair 14 — §4.11's cut-line bullet for `T-SAVE-07`

The bullet defends leaving the ID unmarked on a calendar argument about week
4's output. The ID is green, so the calendar the argument weighed can no longer
reach it; the argument itself is retained as the reason the mark was declined.

**OLD**

```
It is headless and §4.4 closes it on week 4's own self-play
  output; under §2.13.7's slip condition self-play still runs and only the
  stretch maps stand down, so cutting it would buy no calendar.
```

**NEW:**

```
It is headless, and it is **green at
  [`1ee890e`](https://github.com/jakemartin/stratocracy-crew/commit/1ee890e)**
  (§3) on row 10's part (c) — ahead of the week-4 output §4.4 scheduled it on,
  so no slip in that week can reach it now. The reason the mark was declined
  stands as written: under §2.13.7's slip condition self-play still runs and
  only the stretch maps stand down, so cutting it would have bought no calendar.
```

---

### Pair 15 — the reachability parenthetical's crew half, re-pinned

The opening sentence of the parenthetical Pair 2 edits claims that every
crew-repo commit §3 cites is an ancestor of `ec15be6`. Pairs 1, 4, 6 and 8 make
§3 cite `1ee890e`, of which `ec15be6` is an ancestor, so that sentence goes
false at merge. This pins it to the commit and the citation set it was measured
over — the move Pair 1 makes for the status line's own instance of the same
claim — and points forward to where the later pinning lives rather than
asserting an ancestry nobody measured in that direction.

**Scoping, not deletion:** *"so every commit link above resolves"* is retained
and narrowed to the citation set the measurement covered. It is not dropped.

**OLD**

```
*(Every **crew-repo** commit this section **cites** — `d8284f1`, row 6's, included — is an ancestor of [`ec15be6`](https://github.com/jakemartin/stratocracy-crew/commit/ec15be6), measured with `git merge-base --is-ancestor` per sha, so every commit link above resolves.
```

**NEW:**

```
*(Every **crew-repo** commit this section **cited at** [`ec15be6`](https://github.com/jakemartin/stratocracy-crew/commit/ec15be6) — `d8284f1`, row 6's, included — is an ancestor of `ec15be6`, measured with `git merge-base --is-ancestor` per sha, so every commit link this section carried then resolves; each commit cited since is pinned at the landing that cites it, and the §3 status line above carries that pinning.
```

---

### Pair 16 — Ruling T's naming sentence: what row 10's eventual ledger row waits on

The clause states row 10's waiting set in the present tense, and it hangs off
*"The Director **has since** named that row"* rather than off the `ec15be6`
landing record, so it is not pinned to a commit and cannot survive on the
"true at that commit" reading. `T-SAVE-07` closing makes it false, and Pair 12
asserts the opposite in as many words. The surrounding argument is untouched:
the one-row-not-several point and the Q29 condition are unaffected by this
round and stay exactly as written.

**OLD**

```
so parts (a), (b) and (c) resolve to one ledger row rather than to several, and what it waits on is `T-SAVE-06` and `T-SAVE-07`.
```

**NEW:**

```
so parts (a), (b) and (c) resolve to one ledger row rather than to several, and what it waits on is `T-SAVE-06` alone, `T-SAVE-07` having since closed at [`1ee890e`](https://github.com/jakemartin/stratocracy-crew/commit/1ee890e) on part (c).
```

---

### Pair 17 — the part-(a) record's `T-SAVE-07` clause, pinned to its commit

Found by reading §3's part-(a) landing record whole rather than at the terms
this round swept for. The clause is a present-tense statement of what the ID
lacked, sitting inside a record of a past commit — the same shape the previous
round pinned two of its siblings for. `T-SAVE-07` needs nothing now, so the
predicate goes into the tense of the record it sits in.

**OLD**

```
`T-SAVE-07` needs row 6's self-play, which part (c) reaches.
```

**NEW:**

```
`T-SAVE-07` needed row 6's self-play, which part (c) reached.
```

---

## Arithmetic

This is the one section that reconciles a movement. Where a pair states a
movement in §3's own words, that is the landing-record series §3 has kept at
every commit; the figure is reconciled here and appears in no third place.

- **§4.5 moves 71 / 60 / 11 → 71 / 61 / 10.** No acceptance ID is minted;
  `T-SAVE-07` closes at `1ee890e`. Pairs 5, 7 and 8 carry the three figures,
  and Pair 4 states the two movements in §3.
- **The green-by-commit decomposition gains a term of 1 at `1ee890e`** (Pair 6).
  It re-credits no existing term, no invariant's text having been amended this
  round, so no closure re-dates and the terms then sum to the total Pair 5
  states.
- **§4.5's unclosed enumeration keeps its other terms** — 1 for T-DATA-05, 3 for
  the `T-SCN-` IDs, 2 for T-UI-03/04, 3 for row 9 — and its row-10 term moves
  2 → 1 (Pair 8). Those terms sum to the total Pair 7 states, and the ten they
  sum to are `T-DATA-05`; `T-SCN-08`, `T-SCN-09`, `T-SCN-11`; `T-UI-03`,
  `T-UI-04`; `T-INT-02`, `T-INT-03`, `T-INT-05`; and `T-SAVE-06`.
- **Row 10's own unclosed count moves 2 → 1** (Pair 4, Pair 8, Pair 12), the
  survivor being `T-SAVE-06`. **Pair 16 states that same survivor as the
  waiting set of the ledger row row 10 will eventually become**, which is the
  same disposition read off the row rather than off the count.
- **§3's `main()` census moves 14 → 15** at `1ee890e` (Pair 4). Enumerated at
  that commit with `git grep -l` and diffed against the list at `ec15be6`: that
  one addition, `cpp_reference/test_balance.cpp`, no removal. Its §3
  decomposition at this commit is thirteen test harnesses, one combat duel
  simulator, one debug REPL.
- **§4.9's unvendored enumeration moves 2 → 3** (Pair 11), and the three
  members' dispositions are stated in words rather than left to the cardinal:
  `Save` unchanged and still not vendored, `Replay` unchanged and still not
  vendored, `Balance` new and not vendored on the same ruling.
  `cpp_reference/selfplay.cpp` is excluded from vendoring for a different
  reason and is not in that enumeration at all.
- **Pair 13 moves no §4.5 figure.** `GATE-SAVE-PARSE`, `GATE-REPLAY-*` and
  `GATE-BALANCE-*` each mint no acceptance ID, so naming them in the acceptance
  column adds no written ID.
- **Pair 15 moves no figure.** It pins one sentence's citation set to the commit
  that set was measured at, and states no quantity.
- **Pair 17 moves no figure.** It changes the tense of one predicate. The *six
  of row 10's seven IDs* the sentence it sits in opens with is a record of that
  run and stays as written.
- **9 verified ledger rows — unchanged.** §3's table gains, loses and flips no
  row: §4.11 calls row 10 a *proposed* ledger row, and the row named without
  being created is created when its full acceptance set closes.
- **§3's "Nine rows carry a ✓ in the table above, and three more carry evidence
  without one" does not move**, for the same reason. **Pairs 2 and 15 edit two
  other sentences of the paragraph that figure opens**, and neither touches the
  figure itself.
- **§3's "eight IDs still recorded as uncovered" does not move.** That
  enumeration lists only IDs belonging to §3 ledger rows, and row 10 has no
  ledger row, so no `T-SAVE-` ID was ever among the eight. It sits in the same
  paragraph as the two sentences Pairs 2 and 15 edit; **no pair moves this
  figure.**
- **The §4.7 register stands at 33 rows, 16 ruled and 17 open** — measured by
  testing each `| **Qnn**` row for its `RULED` marker. This round mints no `Q`
  row; U, V and W are Director rulings and not register rows, and the letter Q
  is skipped in the ruling series so a ruling letter cannot be read as a
  register row. **No pair touches the register's two extent-bearing sites.**

## Check results

- Every OLD was grepped against `source/gdd.md` and returned exactly one
  occurrence, matches counted with `-o` so that anchors sitting inside a single
  very long line are counted as occurrences and not as lines. Two of §3's lines
  are of that kind and both carry anchors — the status line, and the
  ledger-summary line that closes with the reachability parenthetical. Two
  anchors span a hard line wrap, Pairs 11 and 14, and each was verified on the
  distinguishing fragment that sits whole on one line, then read in place across
  the wrap; every other anchor sits inside one line of the master.
- **Insertion versus replacement was decided by substring test against the
  master rather than by how a pair reads.** Pair 12's and Pair 13's OLD are
  each a prefix of their NEW, so those two are insertions. Every other pair
  rewrites text inside its span — Pair 4 included: its OLD ends at the closing
  italic marker, which the NEW moves to the end of the appended record, so the
  OLD is not contiguous inside the NEW. Pairs 15, 16 and 17 are replacements,
  each re-inflecting words its OLD carries.
- **§3's status line was read record by record, not at this round's search
  terms**, after two blocking findings that were both sibling sentences inside a
  passage a pair had already opened. Its records and their dispositions:
  - the header and ancestry record — **Pair 1**;
  - the head-expiry defect record — **survives**, and Pair 2 now cites it as the
    site of that record;
  - the week-1, debug-driver, row-4, row-5, row-6, row-7, row-5-rebuild, row-8,
    row-8-rebuild and runner-repair records — **each survives**: each states its
    own commit's tallies and its own `main()` census, none of which this round
    moves, and the census series is extended by Pair 4 rather than revised;
  - the row-9 records at `b23823f` and `d837fc8` — **survive**: their
    `T-INT-02`, `T-INT-03` and `T-INT-05` clauses turn on the in-editor
    Automation harness, which this round does not touch;
  - the part-(a) record — one present-tense clause survived last round's pinning
    of its siblings and is **Pair 17**; its other predicates are already pinned
    to that commit or unaffected;
  - the part-(b) record — **Pair 3** takes its `openTurn`/`openActiveTurn`
    sentence pair, **Pair 16** takes the waiting-set clause of the Ruling T
    sentence that closes it, and **Pair 4** appends after its final sentence.
    Its *`T-SAVE-07` did not close* sentence **survives**: what it asserts about
    `cpp_reference/selfplay.cpp` — a combat-only duel harness that writes no
    §4.10 command log — is still true of that file, and Pair 4 says so in the
    same words.
- **Overlap was checked within each shared line.** In §3's status line the
  anchors run Pair 1, Pair 17, Pair 3, Pair 16, Pair 4, in that order and
  disjoint: Pair 1 ends at *the same way per sha.*, Pair 17 sits in the
  part-(a) record's enumeration of IDs that did not run, Pair 3 sits mid
  part-(b) record, Pair 16 sits in the Ruling T sentence after it, and Pair 4
  begins at the *How `ec15be6` was authored* sentence that closes that record.
  Pairs 15 and 2 both fall in the ledger-summary line, in that order and
  disjoint. Pairs 5, 6, 7 and 8 all fall in §4.5's risk cell, in that order and
  disjoint. Pairs 9 and 10 are in different §4.4 rows, and Pairs 12, 13 and 14
  are in §4.11 — 12 and 13 in different cells of row 10's line, 14 in the
  cut-line list below the table.
- **The reachability parenthetical was read whole, sentence by sentence**, once
  Pair 2 was found to have opened it. Its dispositions, in order, with no count
  standing in for them:
  - the ancestry sentence — **Pair 15**;
  - *That form was ruled on 2026-08-05, and the ruling is confined to this
    sentence …* — **survives**: it is about the form Pair 15 keeps, and the
    declining it records is what Pair 2 leans on;
  - the sentence headed **Not every cited commit is an object in the crew
    repo** — **Pair 2** edits its tail; the bolded text is that sentence's head
    and not a sentence of its own, and Pair 2's anchor begins after it;
  - *`99fcb84` was the first citation this ledger made outside the crew repo …
    each commit is cited against the repo it is in* — **survives**: where the
    `T-INT-01` check lives and where the tree it asserts over lives are both
    unchanged this round;
  - *The **file** paths resolve too, which they previously did not …* —
    **survives**: it is about bare `Combat.cpp` and `test_combat.cpp` citations;
  - *Those five citations resolve to two tracked files … every path this table
    cites was probed at the commit its own row names* — **survives**: this round
    adds no path to any evidence cell, no ledger row being created, flipped or
    removed;
  - *The `build/` directory is not tracked at all* — **survives**, and no pair
    here cites anything in `build/` as evidence;
  - *That correction is what the "independently checkable" claim required, not a
    cosmetic one.)* — **survives**, unaffected.
- **Pair 2's citation of the head-expiry record was checked against where that
  record sits.** It is in §3's status line, not in the paragraph the
  parenthetical closes, so the pair names the §3 status line — the form the
  parenthetical's own ruling sentence already uses.
- **The distinct senses of "harness" were separated before drafting, and each
  pair was re-read against them.** No pair says a harness now exists. Pair 4
  says what exists is a producer of §4.10 command logs and says in the same
  breath that the in-editor Automation harness is untouched; Pairs 9, 14 and 16
  name `T-SAVE-06`'s blocker as the in-editor Automation harness and nothing
  else; the `main()` census in Pair 4 uses *test harness* in §3's own census
  sense; and `T-SAVE-07`'s own name, *harness compatibility*, is quoted only
  where §4.4 already carries it (Pair 10). Pairs 15 and 17 say nothing about any
  of them.
- **No pair conflates `cpp_reference/selfplay.cpp` with the `Balance` module.**
  Both are named in Pair 4 with their separate dispositions, and Pair 11 states
  that the duel harness is not one of the three unvendored modules and is
  excluded on the second-`main()` rule instead. The sweep confirmed §4.9's
  exclusion sentence naming `selfplay.cpp` is unaffected, and no pair edits it.
- **No pair states or implies a UE build.** This file was swept
  whitespace-collapsed and case-insensitive for *UBT*, *editor*, *build target*,
  *uproject*, *in-engine* and *compile* beside any claim of effect: every site
  states either that nothing was compiled by UBT and no editor was launched, or
  that a headless gate ran under clang++ and MSVC. Nothing is written about what
  a UE build does, would do, or now permits.
- **Closure is claimed for `T-SAVE-07` and refused for row 10.** Pairs 4, 8, 12
  and 16 each state `T-SAVE-06` as the survivor by name, and this file was swept
  for *closes*, *closed*, *complete* and *done* beside *row 10* and beside *part
  (c)*: every site says the ID closed and the row's set did not.
- **Pass-1 dispositions were stated per clause rather than as a tally alone.**
  `T-SAVE-07` clauses (a) and (c) passing against the defective module is
  recorded in Pair 4 with the reason — the format is agnostic to acceptance —
  because a tally cannot say which clause carries the discriminating power, and
  a check that cannot fail on its own subject is the defect the previous round
  found in its own instruments.
- **This file's own prose was re-read for a cardinal standing in for an
  enumeration**, that being the shape of one blocking finding. Where a figure
  remains, the members it counts are enumerated beside it or it sits in the
  Arithmetic section as a movement; where they were not, the figure is gone and
  the members are named — the parenthetical's sentences and the senses of
  *harness* above, and the fact block's disambiguation in Grounding below.
- **The blast-radius sweep ran whitespace-collapsed and case-insensitive** over
  `T-SAVE-07`, `T-SAVE-06`, `selfplay.cpp`, *self-play*, *not vendored*,
  *eleventh*, *twelfth*, *thirteenth*, *uncovered*, `main()`, *duel simulator*,
  *unclosed*, *green*, the green-count decomposition, `openTurn`,
  `openActiveTurn`, *reachable from the head*, *is an ancestor of*, *waits on*,
  *needs*, `1ee890e`, `ec15be6`, `d837fc8`, `9dec48c`, `99fcb84`, *Balance
  Analyst*, *balance lock*, *balance sims*, *harness*, and row 10's acceptance
  column. **Each hit's whole paragraph was read** rather than the matched line
  alone. Sites found and deliberately left unedited, with the reason each
  survives:
  - §4.1's *Balance sim harness — headless AI-vs-AI self-play, N games →
    win-rate and turn-length distributions → tuning input* — an architecture
    statement about a reporter of distributions, which is a different artifact
    from a producer of command logs; filed below rather than edited.
  - §3's Balance Analyst role row, whose output column reads *Balance logs +
    tuning diffs* — a role contract, unchanged.
  - §4.10's consumer 3, *Balance Analyst self-play logs (§4.1 harness) — each
    self-play match is emitted as this same format* — a design statement this
    landing satisfies rather than falsifies.
  - §4.10's Spec Stub text for `T-SAVE-07`, *a Balance Analyst self-play log
    validates and replays as a save file* — the invariant's own text, unamended
    this round, which is why nothing re-dates.
  - §2.10's *the week-4 self-play logs T-SAVE-07 validates are the same format*
    and Q20's identical clause — scope and schedule statements a landing
    satisfies.
  - §4.4's week-2 cell, *neither can the week-4 self-play logs (T-SAVE-07)* — a
    statement of why the format ships in week 2, which a log written in that
    format satisfies.
  - §4.11's closing paragraph, carrying the same clause — same, and it
    deliberately restates no week number.
  - §4.9's *a UBT module cannot hold a second `main()`, which excludes every
    `test_*.cpp`, `driver_main.cpp` and `selfplay.cpp`* — still true of all
    three, and load-bearing for why the new module could not take that name.
  - §4.9 part 2's blocker sentence, *It waits on an in-editor Automation
    harness* — untouched by this round.
  - §3's `main()` sentences at every earlier landing — each scoped to its own
    commit, so Pair 4 extends the series.
  - §3's part-(b) record's *`T-SAVE-07` did not close* sentence — a record of
    what ran at that commit, whose stated reason is still true of
    `cpp_reference/selfplay.cpp`.
  - §4.11's *T-SAVE-01..05 stay unmarked on cost* bullet — a statement about the
    editor pass, which no ID in it needs.
  - §3's *eight IDs still recorded as uncovered* enumeration — no `T-SAVE-` ID
    is among them.

## Change requests

**Dispositions of the five filed at the previous round, stated so none is left
hanging:**

1. *The §3 parenthetical's UE-project half* — **ruled**, as Ruling U (Pair 2).
2. *The ruled start-of-turn order has two implementations* — **ruled**, as
   Ruling V (Pair 3): it gains an owner and stays filed rather than done.
3. *`T-SAVE-07`'s producer does not exist in the §4.10 format* — **answered by
   this landing** (Pair 4).
4. *§4.11's acceptance column for row 10 lists no gate name* — **ruled**, as
   Ruling W (Pair 13).
5. *Should §3 state a landing's outstanding IDs in the past tense as a
   convention* — **declined, and the declining is the ruling.** A closed list of
   legal phrasings has previously produced more violations than it prevented,
   and the precedent is the one Ruling U is scoped by. Individual sentences
   about `T-SAVE-07` change this round because the fact changed, not because a
   convention was adopted — Pairs 16 and 17 are two such sentences, each fixed
   on its own facts. No pair here adopts a convention.

**Filed this round:**

1. **The `openActiveTurn` retirement condition is named by no build-order row.**
   Ruling V retains the driver's second implementation *until the driver reads
   from `strat::GameState`*. That migration is work §4.11 does not schedule and
   no acceptance ID asserts, so the condition can be met only by a change nobody
   has costed. Whether it becomes a row, a clause of an existing row, or stays
   an open duplication is a §4.11 decision.
2. **§4.1's balance-sim harness and §4.10's consumer 3 describe two different
   artifacts, and only one of them now has a producer.** §4.1 promises *N games
   → win-rate and turn-length distributions → tuning input*; what landed emits
   §4.10 command logs from a driven match. §4.4's week 4 schedules the sims and
   week 6 the balance lock, and §2.0's PX-1 row states its observable check as a
   self-play turn-length distribution — so a reporter of those distributions is
   load-bearing for a stated player-experience goal and is named by no
   build-order row and no acceptance ID. Whether §4.11 gains a row for it is a
   Director decision; I have written no schema or field list for it here.
3. **A repo-level naming constraint is unrecorded in §4.9.** The build workspace
   is case-insensitive and every gate call copies the excluded `test_*.cpp`,
   `driver_main.cpp` and `selfplay.cpp` into it, so a module whose name collides
   case-insensitively with any excluded file is unavailable — it surfaces as a
   duplicate-`main` link error rather than as a name clash. §4.9 states the
   exclusion rule but not this consequence of it. Whether §4.9's vendoring
   paragraph should carry it is a §4.9 text decision; no pair here adds it.
4. **The same reachability claim has now been pinned in two places for the same
   cause.** Pair 1 pins the §3 status line's instance and Pair 15 the
   parenthetical's, each because a later commit made an earlier ancestry claim
   false. Ruling S and Ruling U both decline a document-wide convention and are
   each confined to one sentence, so the next landing meets these same two
   sentences again. Whether §3 should carry that claim in a form that survives a
   landing — and what that form is — is a Director decision this round did not
   take, and no pair here proposes one.
5. **A *has since* sentence in §3 is not pinned by the record enclosing it, and
   that is where this round's outstanding-ID claim went stale.** Pair 16's
   clause reads as current state because its sentence reports a ruling made
   after the commit whose record encloses it, so the "true at that commit"
   reading that protects the surrounding prose does not reach it. Whether §3's
   *has since* sentences should carry their own date or commit, so a later
   landing can pin them the way it pins a landing record, is a §3 structure
   decision; no pair here proposes one, and Pair 16 fixes only the clause that
   went false.

## Grounding

- The commit, its three measured ancestries, and that it is cited as a commit
  with no branch claim: fact block §1.
- The new and modified tracked files, the registry row `balance`, its being
  row 10's third registry row, and the dependency claim its link set encodes:
  fact block §1 and §4.
- The 12/12 result under both compilers, the 6/12 pass-1 block, the six named
  FAIL lines identical under both compilers and predicted at clause level, the
  35-command log over a 6-turn cap, and `GATE-BALANCE-*` minting no acceptance
  ID: fact block §2.
- `T-SAVE-07` clauses (a) and (c) passing against the buggy module, and the
  reason only clause (b) can see the defect: fact block §2.
- That nothing was compiled by UBT, no editor was launched, no UE project file
  was touched, and the UE project repo is untouched at `9dec48c`: fact block §2.
- The written / green / unclosed movements, row 10's own unclosed movement, the
  ten that remain unclosed by name, and the verified-ledger-row count: fact
  block §3.
- The `main()` census of fifteen, its measurement with `git grep -l`, and its
  §3 decomposition at this commit: fact block §3.
- The module owning the translation and the accepted-only-into-the-log
  discipline, `nextCommand` and `applyCommand` owning what it does not, the four
  command kinds against §4.9's five, `Ai.h`'s stated reason and `T-AI-03`, part
  (b)'s hand-authored log having exercised the complete set at `ec15be6`,
  `T-SAVE-07` asserting format compatibility rather than command coverage, Q29
  over that fixture set, and the gate asserting the fifth absent: fact block §4.
- The start-of-turn order running via `Replay.h::openTurn` because part (c)
  drives through `applyCommand`: fact block §4 and §8, Ruling V.
- The dispositions of `Save`, `Replay` and `Balance` on vendoring, the
  enumeration going two → three, and `T-INT-01`/`T-INT-04` still 2/2 at
  `rulesCommit` `d837fc8`: fact block §5.
- `cpp_reference/selfplay.cpp` being unchanged — tracked, a combat-only 1v1 duel
  harness over `Combat.h` that prints a table and opens no file, still named by
  §4.9's exclusion, still not a producer of a §4.10 log — and that it neither
  became nor was replaced by the new module: fact block §5.
- The disambiguation of *harness*, *self-play*, *log* and *Balance*, and the
  test that `T-SAVE-07` closing does not close row 10's set: fact block §6.
- The case-insensitive build filesystem, `ensure_workspace` copying
  `selfplay.cpp` on every gate call, the duplicate-`main` link error, §4.9
  naming `selfplay.cpp` in its exclusion, and `Balance` being the document's own
  role name: fact block §7.
- Rulings U, V and W in full, their scope limits, the skipped letter, and the
  declined convention: fact block §8.
- The register's extent and that no `Q` row is minted: fact block §9.
- Row 10's three parts and their dependency sets, `T-SAVE-06`'s † mark and its
  joint assertion with `T-INT-02`, Q29's per-acceptance-ID reading, the
  *proposed* ledger row posture, and rows 6 and 8 carrying gate names in the
  acceptance column: `source/gdd.md` §4.11 rows 6, 8 and 10 and its cut-line
  list, and §4.7 register Q29.
- **Pair 15's retained measurement** — that every crew-repo commit §3 cited at
  `ec15be6` is an ancestor of `ec15be6` — is the master's own sentence at that
  revision, kept and scoped rather than re-measured this round; the later
  pinning it points to is Pair 1, from fact block §1.
- **Pair 16's and Pair 17's subjects** — Ruling T's naming of row 10's eventual
  ledger row and its waiting set, and the part-(a) record's enumeration of the
  IDs that did not run at `737f666`: `source/gdd.md` §3, against `T-SAVE-07`'s
  closure in fact block §3.
- §2.0's PX-1 row and its observable check, and §4.4's week-4 and week-6 cells:
  `source/gdd.md`, read this round.
- The reachability parenthetical's sentences, the site of the head-expiry record
  in §3's status line, and this document's own record of a head expiring within
  the hour: `source/gdd.md` §3.
