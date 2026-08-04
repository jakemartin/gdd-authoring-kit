# Technical design — `row5-rebuild` addendum (tech-director)

> ## ✅ APPLIED ADDENDUM — DO NOT RE-APPLY
>
> All fifteen pairs were merged into the master GDD on 2026-08-03.
> Master md5 `9742f695f71d625763d9a3eeef21e70b` →
> `5bad314bcb34e52a88bff92727f5fcc5`.
>
> Gate: run `row5-rebuild-2`, **PASS**, 0 violations, after `row5-rebuild-1`
> (BLOCK, 1 — a `format-breach`: the change requests and open questions were
> filed under non-standard heading names). Fixed by renaming two headings with
> no content change, and no `OLD`/`NEW` block moved between the two runs.
>
> **Pair 8 is an insertion — its OLD anchor is retained deliberately.** Its NEW
> block opens with its OLD anchor verbatim and appends after it. Post-check on
> the merged master: every NEW present exactly once; pair 8's OLD present
> **once**, the other fourteen **zero** times. This file is **not safe to apply
> twice**.
>
> Pair 7 reads as an insertion in intent — it appends a landing record to the
> end of the §3 status paragraph — but it is a **replacement** by the byte test,
> because its OLD ends `above.*` and that closing `*` migrates to the end of the
> appended record. The distinction is recorded because a post-check that
> classified it by eye would look for the wrong anchor count.
>
> Pairs 12, 13 and 14 land in the same §4.5 cell. All fifteen anchors were
> verified against the **master** before anything was written — each matching
> exactly once — and the apply refused to write unless every one did.
>
> §2 was **byte-identical across this merge** (103,435 chars, compared as
> strings), and so was each of the four subsections `kb/rules.md` mirrors —
> 2.3, 2.4, 2.7 and 2.8 — so the knowledge base needed no re-sync.

## Placement

Addendum against `source/gdd.md`, md5 **`9742f695f71d625763d9a3eeef21e70b`**.
Exact `OLD` → `NEW` pairs only; no section is redrafted.

**15 pairs — 14 replacements, 1 insertion.** The insertion is **Pair 8**, the
only pair whose `NEW` contains its `OLD` verbatim as a prefix. Pair 7 reads as
an insertion in intent — it appends a landing record to the end of the §3 status
paragraph — but it is a **replacement** by the byte test, because its `OLD` ends
`above.*` and that closing `*` moves to the end of the appended record.

| Pair | Placement | Kind |
|---|---|---|
| 1 | §3, provenance-ledger status paragraph — the "This draft stands at" lead-in | replacement |
| 2 | §3, status paragraph — row 5's landing record at `ad77b13`, gate tally | replacement |
| 3 | §3, status paragraph — row 5's "No ID is left uncovered" claim | replacement |
| 4 | §3, status paragraph — row 5's `flag` debug-designation sentence | replacement |
| 5 | §3, status paragraph — row 6's `isFlag` documented-choice clause | replacement |
| 6 | §3, status paragraph — row 6's T-AI-01 printed counter | replacement |
| 7 | §3, status paragraph — the rebuild record, appended at the end of the paragraph | replacement |
| 8 | §3, status paragraph — the critical-path "evidence rather than schedule" sentence | **insertion** |
| 9 | §3, ledger table — the **Turn loop & win / tiebreak** evidence cell | replacement |
| 10 | §3, the paragraph below the table — row 5's "joined at" sentence | replacement |
| 11 | §3, the paragraph below the table — the parenthetical "every commit link above resolves" | replacement |
| 12 | §4.5, *Specification outruns the build* — the "Reduced and re-scoped" clause | replacement |
| 13 | §4.5, same cell — the green-ID listing sentence | replacement |
| 14 | §4.5, same cell — the unclosed-ID listing | replacement |
| 15 | §4.11, prose above the build-order table — which rows are green at which commit | replacement |

Every `OLD` below was counted document-wide and matches **exactly once**.

---

## Pair 1 — §3 status lead-in: the commit this draft stands at, and its parent

**OLD**

```
This draft stands at 2026-08-03, at commit [`9086d6a`](https://github.com/jakemartin/stratocracy-crew/commit/9086d6a) in the crew repo, whose parent is [`d8284f1`](https://github.com/jakemartin/stratocracy-crew/commit/d8284f1).
```

**NEW**

```
This draft stands at 2026-08-03, at commit `6ccd40b` in the crew repo, whose parent is [`9086d6a`](https://github.com/jakemartin/stratocracy-crew/commit/9086d6a); `6ccd40b` is cited without a link, for the reason the paragraph below the table gives.
```

---

## Pair 2 — §3: row 5's landing record at `ad77b13` is a record of that commit, not of row 5's current gated set

**OLD**

```
gated **T-TURN-01..09, 9/9 under clang++ and MSVC both** — `g++` is not installed on this machine — while its pass-1 implementation `cpp_reference/Turn.buggy.cpp` is blocked at 6/9, on T-TURN-05, T-TURN-06 and T-TURN-07, under both compilers.
```

**NEW**

```
gated, **as the acceptance set then read**, **T-TURN-01..09, 9/9 under clang++ and MSVC both** — `g++` is not installed on this machine — while its pass-1 implementation `cpp_reference/Turn.buggy.cpp` is blocked at 6/9, on T-TURN-05, T-TURN-06 and T-TURN-07, under both compilers. That set has since widened to `T-TURN-01..10` and row 5 was rebuilt against it; **this sentence records what ran at `ad77b13` and is not row 5's current evidence**, which is recorded at the end of this paragraph.
```

---

## Pair 3 — §3: where row 5's full acceptance set closes

**OLD**

```
**No ID is left uncovered:** row 5 has no in-editor half and no reserved-unwritten ID, so its full acceptance set closes at one commit, Q29 is satisfied, and the row flips in the table below.
```

**NEW**

```
**No ID is left uncovered:** row 5 has no in-editor half and no reserved-unwritten ID, so its full acceptance set closes at one commit — but that commit is no longer this one. The set was widened to `T-TURN-01..10` this revision, and it closes at the `6ccd40b` rebuild recorded at the end of this paragraph; Q29, read per acceptance ID, is satisfied there, and the row flips in the table below on that commit rather than on this one.
```

---

## Pair 4 — §3: row 5's `flag` designation states in the present tense that row 7 is unbuilt

**OLD**

```
`flag` is a **debug designation** standing in for Stub 7's `isFlag` — row 7 is unbuilt and Q10 is open on exactness —
```

**NEW**

```
`flag` is a **debug designation** standing in for Stub 7's `isFlag` — at that commit row 7 held no code, and Q10 is open on exactness —
```

---

## Pair 5 — §3: row 6's record carries the same present-tense statement

**OLD**

```
`isFlag` being Stub 7's placement field with row 7 unbuilt and Q10 open.
```

**NEW**

```
`isFlag` being Stub 7's placement field, which held no code at that commit, and Q10 being open on exactness.
```

---

## Pair 6 — §3: T-AI-01's printed counter is commit-scoped

**OLD**

```
T-AI-01's counter printed `129 AI commands issued across 6 games`.
```

**NEW**

```
T-AI-01's counter printed `129 AI commands issued across 6 games` **at that commit**. That figure is **commit-scoped and is not an invariant** — it counts what the routine emitted against the rules as they then stood, so an upstream rule change moves it without moving anything else in this row: re-run at `6ccd40b`, after row 5's rebuild, the same counter prints `120 AI commands issued across 6 games`, while row 6's commit, its 7/7 tally and its ledger row are unchanged.
```

---

## Pair 7 — §3: the rebuild record, appended at the end of the status paragraph

**OLD**

```
No UI harness is among the eleven `main()` definitions above.*
```

**NEW**

```
No UI harness is among the eleven `main()` definitions above. **Row 5 was then rebuilt**, at `6ccd40b`, whose parent is [`9086d6a`](https://github.com/jakemartin/stratocracy-crew/commit/9086d6a), against three rulings whose **GDD half had already merged before any code satisfied them**: T-TURN-01's move/act split into two independent per-unit flags, the new `T-TURN-10` build allowance, and T-FAME-04's dropped per-turn clause. This commit **modifies only** — `git show --summary` prints no create, delete or rename line, 14 files changed: `README.md`, `crew/tools.py`, `spec/ai_spec.md`, `spec/driver_spec.md`, `spec/turn_spec.md`, and in `cpp_reference/`, `Ai.buggy.cpp`, `Ai.good.cpp`, `Driver.good.cpp`, `Driver.h`, `Turn.buggy.cpp`, `Turn.good.cpp`, `Turn.h`, `test_driver.cpp` and `test_turn.cpp`. **No harness was added:** the same **eleven** tracked sources define `main()` as at `9086d6a`. The gate is **T-TURN-01..10, 11/11 under clang++ and MSVC both** — `g++` is still not installed on this machine — and **the 11 counts printed checks, not IDs**: ten IDs close, and `T-TURN-01` prints two of the eleven lines, `alternation-and-once-per-own-turn` and `two-independent-flags-in-either-order`. Pass-1 `cpp_reference/Turn.buggy.cpp` is blocked at **5/11** — six FAIL lines over **five** distinct IDs: `T-TURN-01` (both of its lines), `T-TURN-05`, `T-TURN-06`, `T-TURN-07` and `T-TURN-10` — under both compilers. **This is the commit at which row 5's acceptance set closes.** Because the set was widened to `T-TURN-01..10` in the GDD half, row 5's ✓ rested on nine of its ten written IDs between that merge and this commit; Q29, read per acceptance ID, is satisfied at `6ccd40b` and at no earlier commit, and the evidence cell below names it. **No new acceptance ID was written here** — `T-TURN-10` was minted in the GDD half — so §4.5's written-ID count does not move at this landing, its green count moves 49 → 50, and its unclosed count moves 21 → 20. **Q8(b) is now executed rather than only written:** a Build naming a factory that has already taken its build this turn is refused, fameTotal is unchanged by the refusal, and both dispositions of the first build — one that spawned and one that waits holding the slot (T-FAME-04) — count against the allowance. Two rulings carried in with the code are recorded here because neither is derivable from the invariant text alone: the allowance's **renewal boundary is per side-turn, not per round** — `beginTurn` clears both act flags and the allowance together, so a factory captured at the start of a side's half arrives with a clear record, and T-TURN-10 asserts that case inside one round number — and **command ordering is unconstrained**, move-then-attack and attack-then-move both completing and spending the same two flags, which is what T-TURN-01's second printed check asserts. The debug driver's suite is **GATE-DRV-01..11, 11/11 under clang++ and MSVC both**, the same ID range as at `9086d6a`, and those IDs are still **not** `T-*`, so nothing flips on the driver's account here either. **Row 6 was re-run and is not re-recorded:** its commit, its `T-AI-01..06` plus `GATE-AI-SMOKE` 7/7 and its ledger row are unmoved, and only T-AI-01's printed command counter moves, as recorded above. **How `6ccd40b` was authored is deliberately not stated:** no harness claim is made for it, because none was established, and reporting a harness that did not run is the exact failure this ledger exists to prevent.*
```

---

## Pair 8 — §3: the critical-path sentence, now true per acceptance ID as well as per row

**OLD**

```
since §4.11's critical path runs 1 → 3 → 4 → 5 → 6/8, everything on that path but **row 8** is now evidence rather than schedule
```

**NEW**

```
since §4.11's critical path runs 1 → 3 → 4 → 5 → 6/8, everything on that path but **row 8** is now evidence rather than schedule — **per acceptance ID as well as per row**, since `T-TURN-10`, the one path ID that was written and asserting without being green, closed at `6ccd40b`
```

---

## Pair 9 — §3 ledger table: row 5's evidence cell

**OLD**

```
| **Turn loop & win / tiebreak** | agent | ✓ | `cpp_reference/Turn.good.cpp` + `cpp_reference/test_turn.cpp` @ [`ad77b13`](https://github.com/jakemartin/stratocracy-crew/commit/ad77b13) · T-TURN-01..09 (9/9) |
```

**NEW**

```
| **Turn loop & win / tiebreak** | agent | ✓ | `cpp_reference/Turn.good.cpp` + `cpp_reference/test_turn.cpp` @ `6ccd40b` · T-TURN-01..10, all ten closing — the runner prints **11** PASS lines over those ten IDs, T-TURN-01 printing two of them, so the 11 counts checks and not IDs. T-TURN-01..09 first closed at [`ad77b13`](https://github.com/jakemartin/stratocracy-crew/commit/ad77b13); `6ccd40b` is the rebuild at which the **full** set closes at one commit, which is what Q29 requires |
```

---

## Pair 10 — §3, below the table: row 5's summary sentence

**OLD**

```
**Turn loop & win / tiebreak** joined at [`ad77b13`](https://github.com/jakemartin/stratocracy-crew/commit/ad77b13) — T-TURN-01..09, **9/9 under clang++ and MSVC both** — and it leaves **no ID uncovered** either: no in-editor half and no reserved ID, so its full acceptance set closes at one commit and Q29 is satisfied rather than blocking.
```

**NEW**

```
**Turn loop & win / tiebreak** joined at [`ad77b13`](https://github.com/jakemartin/stratocracy-crew/commit/ad77b13) — T-TURN-01..09, **9/9 under clang++ and MSVC both** — and its acceptance set has since widened to **T-TURN-01..10**, green at the `6ccd40b` rebuild under clang++ and MSVC both, on **11 printed checks over those ten IDs**. It leaves **no ID uncovered**: no in-editor half and no reserved ID, so its full acceptance set closes at one commit — `6ccd40b`, not `ad77b13` — and Q29, read per acceptance ID, is satisfied rather than blocking.
```

---

## Pair 11 — §3, below the table: the link-resolution parenthetical, the one site that carries the unlinked-citation convention

**OLD**

```
*(Every commit this section cites — `d8284f1`, row 6's, included — is reachable from the head of `main` in the crew repo, so every commit link above resolves.
```

**NEW**

```
*(Every commit this section **links** — `d8284f1`, row 6's, included — is reachable from the head of `main` in the crew repo, so every commit link above resolves. **`6ccd40b`, row 5's rebuild, carries no link anywhere in this section**: it is committed on `main` and not yet pushed, so it is reachable in the working repository and not on GitHub, and the section states the commit rather than a link that would fail. Pushing it is what makes the link form available, and this sentence is the only one that has to move when it does.
```

---

## Pair 12 — §4.5: `T-TURN-10`'s status

**OLD**

```
**Reduced and re-scoped at 2026-08-03, not retired:** one new ID has been written since `c224825` — `T-TURN-10`, minted this revision into Spec Stub 5 for the per-turn build limit Q8(b) ruled — and it is **written, unblocked and asserting, and not green**, because the code that satisfies it does not exist yet;
```

**NEW**

```
**Reduced and re-scoped at 2026-08-03, not retired:** one new ID has been written since `c224825` — `T-TURN-10`, minted this revision into Spec Stub 5 for the per-turn build limit Q8(b) ruled — and it is **green at `6ccd40b`**, the rebuild at which row 5's widened acceptance set closes in full (§3);
```

---

## Pair 13 — §4.5: the green-ID listing

**OLD**

```
**49** of the 70 are green: **18** at `c224825`, where rows 1 and 3 closed their full acceptance sets and row 2's headless half passed, **9** at `647d4df`, where T-FAME-01..09 closed row 4, **9** at `ad77b13`, where T-TURN-01..09 closed row 5, **6** at `d8284f1`, where T-AI-01..06 closed row 6, and **7** at [`9086d6a`](https://github.com/jakemartin/stratocracy-crew/commit/9086d6a), where T-SCN-01..07 closed without closing row 7 — so everything on the critical path but row 8 is evidence rather than schedule.
```

**NEW**

```
**50** of the 70 are green: **18** at `c224825`, where rows 1 and 3 closed their full acceptance sets and row 2's headless half passed, **9** at `647d4df`, where T-FAME-01..09 closed row 4, **9** at `ad77b13`, where T-TURN-01..09 closed, **6** at `d8284f1`, where T-AI-01..06 closed row 6, **7** at [`9086d6a`](https://github.com/jakemartin/stratocracy-crew/commit/9086d6a), where T-SCN-01..07 closed without closing row 7, and **1** at `6ccd40b`, where T-TURN-10 closed and completed row 5's acceptance set — so everything on the critical path but row 8 is evidence rather than schedule, **per acceptance ID as well as per row** now that T-TURN-10 has closed.
```

---

## Pair 14 — §4.5: the unclosed-ID listing

**OLD**

```
**21 IDs remain unclosed**: T-DATA-05, which leaves row 2 unflipped; T-SCN-08, T-SCN-09 and T-SCN-11, which are written, unblocked and asserting, but ran only part of their fixture sets, and which leave row 7 unflipped; `T-TURN-10`, written this revision, unblocked and asserting — the code it gates does not exist yet, so it has not run and is not green; and the **16** in rows 8–10, which hold no code
```

**NEW**

```
**20 IDs remain unclosed**: T-DATA-05, which leaves row 2 unflipped; T-SCN-08, T-SCN-09 and T-SCN-11, which are written, unblocked and asserting, but ran only part of their fixture sets, and which leave row 7 unflipped; and the **16** in rows 8–10, which hold no code
```

---

## Pair 15 — §4.11: which commit row 5 is green at

**OLD**

```
**Rows 1 and 3 are green at `c224825`, row 4 at `647d4df`, row 5 at
`ad77b13` and row 6 at `d8284f1`**
```

**NEW**

```
**Rows 1 and 3 are green at `c224825`, row 4 at `647d4df`, row 5 at
`6ccd40b` — its rebuild, where the widened `T-TURN-01..10` closes; `T-TURN-01..09`
first closed at `ad77b13` — and row 6 at `d8284f1`**
```

---

## Judgement calls made, not filed

**Row 5's (and row 6's) present-tense "row 7 is unbuilt".** Decided, and
changed — Pairs 4 and 5. Reasoning, stated so the Director can overrule it:
the statement was stale rather than wrong when row 7 landed, and the gate
declined to file it three times on that reading. What is new is that
`6ccd40b` — the commit this round's evidence rests on — **itself corrected the
equivalent statements in `spec/ai_spec.md` and `spec/turn_spec.md`**, as the
crew `README.md` did when row 7 landed. The code half has now moved where the
document has not, and a present-tense falsehood sitting inside the very record
whose evidence is that commit is not defensible. Both sites are repaired by
**pinning the claim to the commit it was true at** ("held no code at that
commit") rather than by deleting it, so the historical record survives and
nothing is asserted about today. Row 6's site is changed for the same reason
and on the same commit's authority; that change touches **no** part of row 6's
provenance — not its commit, not its 7/7, not its ledger row.

**Where the unlinked-citation convention lives — one site, not two.** Decided:
**Pair 11 alone carries it.** The first cut of Pair 1 asserted it a second time
in the §3 lead-in, quantified over every citation of `6ccd40b` in the section.
That is the same exposure this round exists to repair — a claim stated in two
places, one of which will be edited without the other — and both copies go
stale the moment the commit is pushed and one citation is relinked. The
convention belongs in the sentence whose truth depends on it: the parenthetical
is the site that claims every commit link resolves, so it is the site that must
state the exception, and Pair 11 now says outright that it is the only sentence
that has to move on a push. Pair 1 keeps a **pointer** rather than a
restatement — "cited without a link, for the reason the paragraph below the
table gives." A pointer asserts nothing about push state, so it cannot fall out
of agreement with Pair 11; what it buys is that an unlinked `6ccd40b` beside a
linked `9086d6a` in the same sentence reads as a decision rather than as a
dropped link.

**T-AI-01's counter, and row 6's other figures.** Pair 6 pins `129` to
`d8284f1` and records `120` at `6ccd40b` as a re-run, with an explicit
statement that the figure is commit-scoped. Row 6's sweep figures were checked
against the artifact and are **not** falsified by this rebuild; no pair touches
them and no sentence is added beside them.

**Row 5's historical landing record.** Pairs 2 and 3 qualify it rather than
restate it: the tally at `ad77b13` was true of `ad77b13` and stays, with a
pointer forward, so the sentence does not re-stale the next time row 5's set
moves.

---

## Open questions for the Director

1. **Does a rebuild of an already-landed row re-open "Playable via debug
   commands"?** §4.4's week-1 goal was ruled provisionally met at `9f87ecd`
   and explicitly re-opened by *each system that lands after it*, rows 5–8
   included — a ruling applied three times, always to a system landing for the
   first time. `6ccd40b` lands no new system; it changes the rule a landed one
   enforces, and it changes what the driver accepts. Whether that is a
   "system landing after it" is a ruling, not a derivation. **No closure is
   written either way in this addendum**, and no pair touches the §4.4 week-1
   cell or the provisional-met passage.
2. **What authored `6ccd40b`?** Every prior row record names its harness — a
   Claude Code session against a Director-written stub, explicitly *not* a live
   CrewAI run. Nothing establishes the harness for this commit, so Pair 7
   states that it is not stated. If the Director knows it, one sentence closes
   this.
3. **Push state.** `6ccd40b` is unpushed, so it is cited unlinked at every site
   this addendum touches, and **Pair 11 is the single sentence that states why**.
   If the Director prefers the linked form, push first: the citations may then
   be relinked and Pair 11's exception sentence retired, and those two edits
   must land together or §3 asserts a link that 404s.

---

## Change requests

Four rule gaps, found while writing the gates. Each is a rule the Director
writes and I gate; no invariant text is edited by this addendum.

- **Q8(b)'s renewal boundary is nowhere in the document.** T-TURN-10's written
  text says only "the allowance renews at the start of the owner's turn." The
  shipped code renews it **per side-turn**, together with both act flags, and
  the distinction is load-bearing for a factory captured mid-round. It reached
  the document only as a Director ruling carried in with the code; Pair 7
  records it as a ruling rather than deriving it from the invariant. **If the
  Director wants it gate-visible it belongs in Stub 5's T-TURN-10 text**, which
  this addendum does not edit.
- **Command ordering.** T-TURN-01 asserts flags, not order, and says so; that
  ordering is *unconstrained* is a ruling, recorded in Pair 7, not something
  the invariant states. Same disposition: a Stub 5 text change is the Director's
  to make.
- **Nothing states what a rebuild does to a flipped ledger row.** Q29 governs
  partial passes and per-ID closure; no row governs a row that was ✓ on a set
  that later widened. Row 5 spent this revision in exactly that state — ✓ on
  nine of ten written IDs. Pair 3 and Pair 7 repair the instance; the general
  rule is unwritten.
- **The harness question above is also a gap in the ledger's own contract**:
  §3 requires the harness be reported, and offers no disposition for "not
  established".

---

## Findings my scoping brief did not name

- **§3's "Six IDs are still recorded as uncovered" sentence is repaired by this
  round without an edit.** It enumerates two unwritten (T-MOVE-07, T-SCN-10)
  and four written-and-not-green (T-DATA-05, T-SCN-08/09/11) — and omits
  `T-TURN-10`, which was written and not green from the GDD-half merge until
  `6ccd40b`. The sentence was short by one for that window; with T-TURN-10 green
  it is correct as written, and **no pair touches it**. Flagged so the Director
  knows the arithmetic was checked and why nothing moved.
- **§3's link-resolution parenthetical would have been falsified by citing an
  unpushed commit** — the reason Pair 11 exists. It is not in the six scoped
  items.

---

## Handoffs

None outbound. No pair touches §2 rules text, §2.13 map data, or §2.11 screen
material; the move/act split and T-FAME-04's dropped clause were merged in the
GDD half and are not re-opened here.

---

## Grounding

| Claim | Backed by |
|---|---|
| `6ccd40b` on `main`, parent `9086d6a`, subject, unpushed | round fact block §A |
| 14 files modified, no create/delete/rename, path list | `git show --summary 6ccd40b` (fact block §A) |
| Eleven `main()` definitions unchanged | `git grep -l "int main(" 6ccd40b -- cpp_reference` = 11 (fact block §A) |
| T-TURN-01..10, 11/11; 11 counts checks not IDs; the two T-TURN-01 check names | fact block §B, five runs under clang++ and MSVC, working tree clean at `6ccd40b` |
| Pass-1 5/11, six FAILs over five IDs | fact block §B |
| T-AI-01 prints `120 … across 6 games`; row 6 still 7/7 | fact block §B |
| `GATE-DRV-01..11`, 11/11, same range as `9086d6a` | fact block §B |
| Renewal per side-turn; ordering unconstrained; T-FAME-04's dropped clause | Director rulings, fact block §C |
| GDD half merged first (content `ff6b78b`, kit `18fae0a`) | fact block §C |
| Row 5's written set is `T-TURN-01..10` | `source/gdd.md` §4.7 Stub 5 (`Acceptance: T-TURN-01..10`); §4.11 row 5; §2.8's `T-CAP-` alias note |
| Q29 read per acceptance ID | `source/gdd.md` §4.7 register, Q29; its per-ID application in row 7's record |
| 70 written / 49 green / 21 unclosed before this round | `source/gdd.md` §4.5, *Specification outruns the build* |
| Row 5 previously cited at `ad77b13` in four places | `source/gdd.md` §3 status paragraph, §3 ledger cell, §3 summary paragraph, §4.11 prose |
| "Playable via debug commands" provisionally met and re-opened by later systems | `source/gdd.md` §3 status paragraph (Director ruling 2026-08-02, amended same day) |
