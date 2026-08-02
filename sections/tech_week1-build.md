# Technical design — week-1 build addendum (tech-director)

> ✅ **APPLIED ADDENDUM — DO NOT RE-APPLY.**
> All thirteen replacement pairs in this file were applied verbatim to the master
> GDD and merged on 2026-08-02. Re-applying them would fail (the OLD anchors no
> longer match) or, worse, **double-apply pair 13**, which is an insertion whose
> NEW text deliberately ends with the anchor it replaces — that anchor survives
> by design, so a naive re-run would insert the block a second time. Gate record:
> run `week1-build-9`, PASS, zero violations, after eight blocking runs. Master
> GDD md5 `d3f6913b1ecf228c19811328db33b27d` → `97ccf0e9cc8c3f72adfaca10bd42d862`.
> Later changes to these sections need a NEW addendum file.
>
> Thirteen replacement pairs, all in §3, §4.5, §4.7, §4.8, §4.9 and §4.11.
> Nothing here redrafts a section. Every **OLD** block below was searched against
> `source/gdd.md` and returned **exactly one** match; the apostrophes and double
> quotes in the source are straight ASCII, which I confirmed before writing the
> anchors. At merge time each anchor was re-verified against the master GDD
> itself — all thirteen matched exactly once — and the pairs were extracted
> programmatically from this file rather than retyped.
>
> **Fence convention.** OLD and NEW blocks are delimited by three backticks,
> except **pair 13**, whose NEW text itself contains a fenced block — that one
> pair is delimited by **four** backticks, so each block still has exactly one
> unambiguous boundary and a naive extraction cannot truncate it early.
>
> **Path convention (Director ruling).** In anything that merges, **every path
> is written in full, with no construction that requires the reader to
> distribute a prefix** — not a shared directory stated once for a list, not a
> governing scope introducing one, not a group label standing in for a family of
> files, and not a bare directory that a later "there" or "them" points back at.
> The test is a grader clicking, not parsing. **OLD anchors are exempt**, because
> they must stay byte-identical to the source; text quoting an OLD anchor in
> order to correct it is exempt with it. Nothing else is. Two constructions in
> this file rely on that exemption: pair 9's OLD anchor, and the Target 4
> sentence that quotes it.

## The ✓ is contingent — read this before applying pairs 1 and 2

> **RULED 2026-08-02: the Director signed off.** Bar (b) was put to the Director
> explicitly at merge time, with both branches drafted. Pairs 1 and 2 were
> applied as drafted — `✓`, System cells bolded. The `—` fallback below was not
> taken and is retained as the record of what the alternative would have been.

§3 defines **Agent-verified** as **both** bars: (a) agent-authored automated
tests that pass in the headless suite, **and** (b) sign-off at the human review
gate. Bar (a) is closed for §4.11 rows 1 and 3 at `c224825`. **Bar (b) is
yours.** Pairs 1 and 2 propose `✓`; if you decline the sign-off they still
apply, but with **two** changes each, because §3's ledger encodes verification
twice per row: the Agent-verified cell reads **`—`**, *and* the System cell is
**unbolded** — every `✓` row in that table is bolded and every `—` row is not,
which is the same signal pair 3 uses to keep row 2 visibly unflipped. The
Evidence cell stands exactly as drafted either way; it is bar (a). Pair 3 (Data
tables) proposes `—` under both readings and needs no such decision.

**Declining moves five sites, and they move together.** A `—` in the table
beside a bolded row name, or beside a "flipped" in the prose, is precisely the
two-bar rule's own failure case — so each fallback is written out rather than
left to the merge:

| Pair | As drafted | If bar (b) is declined |
|---|---|---|
| 1 and 2 | `\| **Hex grid & math** \| agent \| ✓ \|` and `\| **Movement & pathfinding** \| agent \| ✓ \|` | System cell unbolded and the mark dropped: `\| Hex grid & math \| agent \| — \|`, `\| Movement & pathfinding \| agent \| — \|`. Evidence cells unchanged |
| 8 | rows 1 and 3 "**flip in the table below**" | rows 1 and 3 "**close bar (a) in the table below**" |
| 9 | "**Six rows now carry a ✓, and a seventh carries evidence without one**", and the two week-1 rows "**joined them**" | both clauses move together: **four** rows carry a ✓, two more have **closed bar (a)** and await sign-off, and the seventh still carries a partial pass |
| 10 | "against **6** verified ledger rows (§3)" | "against **4** verified ledger rows (§3)" |
| 12 | "of which **rows 1 and 3 have since flipped** (§3)" | "of which **rows 1 and 3 have since closed bar (a)** (§3)" |

---

## TARGET 1 — the three week-1 ledger rows

Rows 1 and 3 flip on their **full** acceptance sets. Row 2 does not, and is
drafted so that a reader sees the non-flip rather than infers it.

**Why row 2 stays unflipped, and how.** §4.11's own † bullet prices T-DATA-05 as
"row 2's ledger flip, since Q29 requires the full acceptance set at one commit."
Its headless half going green does not touch that reading: Q29's conservative
rule is *full set at one commit*, and T-DATA-05 is in the set. So the row keeps
the unbolded system name every unflipped row in the table has, keeps `—` in
Agent-verified, and its Evidence cell opens with **"Partial pass — not a flip"**
before it cites anything. Three signals, none of which depends on the reader
knowing Q29. What the cell adds is the record itself — the headless five are
green at a named commit, and discarding that would report *less* than is true,
which is the opposite failure from claiming more.

One distinction the cell states because the † legend would otherwise be
misread: row 2 is unflipped **because the editor pass is not due yet**, not
because the cut line fired. T-DATA-05 stands down only if the calendar takes it;
it has not yet had a calendar slot.

**Author column.** Rows 1–3 all move from `*pending*` to `agent`. Author and
Agent-verified are separate axes in §3's legend, and `*pending*` was never a
legal Author value — it was a placeholder for *no work exists*. Work exists for
all three. For row 2 the code is agent-authored and the **data values** are
§2.3's and §2.4's own, which is not an authorship claim I am making but a fact
T-DATA-01 and T-DATA-02 assert and that passed.

### Pair 1 — §3 ledger, Hex grid & math

**OLD**
```
| Hex grid & math | *pending* | — | *pending build* |
```
**NEW**
```
| **Hex grid & math** | agent | ✓ | `cpp_reference/Hex.good.cpp` + `cpp_reference/test_hex.cpp` @ [`c224825`](https://github.com/jakemartin/stratocracy-crew/commit/c224825) · T-HEX-01..07 (7/7) |
```

### Pair 2 — §3 ledger, Movement & pathfinding

**OLD**
```
| Movement & pathfinding | *pending* | — | *pending build* |
```
**NEW**
```
| **Movement & pathfinding** | agent | ✓ | `cpp_reference/Move.good.cpp` + `cpp_reference/test_move.cpp` @ [`c224825`](https://github.com/jakemartin/stratocracy-crew/commit/c224825) · T-MOVE-01..06 (6/6); T-MOVE-07 reserved-unwritten on Q2 |
```

### Pair 3 — §3 ledger, Data tables (units/terrain) — recorded, not flipped

**OLD**
```
| Data tables (units/terrain) | *pending* | — | *pending build* |
```
**NEW**
```
| Data tables (units/terrain) | agent | — | **Partial pass — not a flip.** `cpp_reference/Data.good.cpp` + `cpp_reference/test_data.cpp` over `data/units.csv`, `data/terrain.csv`, `data/effectiveness.csv` @ [`c224825`](https://github.com/jakemartin/stratocracy-crew/commit/c224825) · T-DATA-01..04, 06 (5/5) headless. **T-DATA-05 (in-editor) has not run**, so the acceptance set is incomplete at this commit and Q29 keeps the row unverified |
```

---

## TARGET 2 — the citation defect the ledger's own honesty rule requires fixing

**In scope, and not filed as a change request.** §3 says each Verified row cites
"the commit and passing test IDs that back it **so the claim is auditable rather
than asserted**", and the paragraph below the table says "every link above
resolves and the ledger's 'independently checkable' claim is testable by
clicking it."

**The tally, in the two units it needs.** Cells and citations are different
things, and conflating them produced three wrong counts in a row. Counted from
`source/gdd.md`: **five bare citations across four cells** — `Combat.cpp` three
times (bare in the Combat resolution cell, `::repairAmount` in the Repair cell,
`::effectiveness` in the Type-effectiveness cell) and `test_combat.cpp` twice
(in the Combat resolution cell and in the Test suite cell). The Combat
resolution cell carries two of the five on its own, which is what every earlier
count missed. **Those five resolve to two files** —
`cpp_reference/Combat.good.cpp` and `cpp_reference/test_combat.cpp` — a third
unit that has to be kept separate from the other two, since neither corrected
path is its bare name with a directory bolted on. Nothing under `build/` is
tracked.

An addendum that flips two rows on the strength of that claim while leaving the
claim false in all four cells is the half-applied edit this document keeps
catching. The claim sentence is not weakened; the citations are corrected to
paths that resolve.

**What the corrected citations rest on — probes and history, not a listing.** A
working tree plus a `.gitignore` read establishes the state at one commit, which
is less than the claim needs, and a filtered listing shows what a query returned
rather than what a specific path does. Both were replaced with checks that carry
the extent the claim states, run in `stratocracy-crew` and supplied to me.

*Extent 1 — the whole history.* `git log --all --diff-filter=A --name-only`
(every path ever added on any ref) and `git rev-list --all --objects` (every
object in every reachable commit). The complete set of Combat-matching paths the
repository has ever held is `cpp_reference/Combat.buggy.cpp`,
`cpp_reference/Combat.good.cpp`, `cpp_reference/Combat.h`,
`cpp_reference/test_combat.cpp`, `spec/combat_spec.md` and
`spec/combat_spec_addendum.md` — **no `Combat.cpp`, no `build/Combat.cpp` and no
root-level `test_combat.cpp` in any commit**. The same enumeration gives the
`build/` count: **0 entries ever added**, on any ref.

*Extent 2 — `5ffa8d6`, the commit pairs 4–6 cite.* `git cat-file -e
5ffa8d6:<path>`, one existence probe per path, which is what establishes that a
**specific citation** resolves rather than that a query matched something:

```
EXISTS   cpp_reference/Combat.good.cpp     EXISTS   spec/combat_spec.md
EXISTS   cpp_reference/test_combat.cpp     EXISTS   spec/combat_spec_addendum.md
EXISTS   cpp_reference/Combat.h            EXISTS   crew/tasks.py
EXISTS   cpp_reference/Combat.buggy.cpp
ABSENT   Combat.cpp                        0 tracked entries under build/
ABSENT   build/Combat.cpp
```

So pairs 4, 5 and 6 cite paths that resolve at the commit each row names, not
merely at HEAD, and `Combat.cpp`'s absence is established **at that same commit**
as well as across the history.

*Extent 3 — `c224825`, the commit pairs 1–3 cite.* The previous revision of this
file recorded these paths as the one citation class **not** held to the probe
standard: they were established in the working tree only. They are held to it
now, by the same per-path form:

```
EXISTS   cpp_reference/Hex.good.cpp       EXISTS   data/units.csv
EXISTS   cpp_reference/Data.good.cpp      EXISTS   data/terrain.csv
EXISTS   cpp_reference/Move.good.cpp      EXISTS   data/effectiveness.csv
EXISTS   cpp_reference/test_hex.cpp       EXISTS   cpp_reference/Hex.h
EXISTS   cpp_reference/test_data.cpp      EXISTS   cpp_reference/Data.h
EXISTS   cpp_reference/test_move.cpp      EXISTS   cpp_reference/Move.h
EXISTS   crew/tasks.py                    EXISTS   spec/hex_spec.md
EXISTS   spec/combat_spec.md              EXISTS   spec/data_spec.md
EXISTS   spec/combat_spec_addendum.md     EXISTS   spec/move_spec.md
ABSENT   build/acceptance_week1.json      ABSENT   build/Hex.cpp
0 tracked entries under build/
```

**Every path pairs 1–3 cite resolves at the commit those rows name. No citation
in this addendum fails a probe at the commit its own row cites** — which is the
standard, and is why the Combat paths are probed at `5ffa8d6` above rather than
folded into this block. The two absences are the same defect class the pairs
above repair, arriving one commit later and doing no damage: the week-1 rows
cite `cpp_reference/`, never `build/`, so `build/Hex.cpp`'s absence costs
nothing — and `build/acceptance_week1.json`, the Test Engineer's release record,
is untracked exactly as `build/Combat.cpp` is, which is why no evidence cell
cites it.

**The extent, stated once so it is not stretched.** Each probe set fixes the
state of named paths at **one** commit and says nothing about any other; extent
1 is what carries the "never at any commit" claim, and nothing here establishes
the *content* of any file, only that the path resolves.

### Pair 4 — §3 ledger, the Combat resolution and Test suite rows

Between them these two cells carry three of the five bare citations, and this
pair replaces all three. The Test suite cell then names five paths across two
commits, every one written out in full: an earlier revision wrote the three
week-1 harnesses with the `cpp_reference/` prefix on the first item only, which
is the same shape as the bare citations this pair exists to repair, inside the
repair itself.

**OLD**
```
| **Combat resolution** | agent | ✓ | `Combat.cpp` + `test_combat.cpp` @ [`5ffa8d6`](https://github.com/jakemartin/stratocracy-crew/commit/5ffa8d6) · T-COMBAT-01..10 (10/10) |
| **Test suite** | agent | ✓ | `test_combat.cpp` @ [`5ffa8d6`](https://github.com/jakemartin/stratocracy-crew/commit/5ffa8d6) · 17/17 invariants, re-runnable via `python run.py` |
```
**NEW**
```
| **Combat resolution** | agent | ✓ | `cpp_reference/Combat.good.cpp` + `cpp_reference/test_combat.cpp` @ [`5ffa8d6`](https://github.com/jakemartin/stratocracy-crew/commit/5ffa8d6) · T-COMBAT-01..10 (10/10) |
| **Test suite** | agent | ✓ | `cpp_reference/test_combat.cpp` @ [`5ffa8d6`](https://github.com/jakemartin/stratocracy-crew/commit/5ffa8d6) · 17/17 invariants; `cpp_reference/test_hex.cpp`, `cpp_reference/test_data.cpp`, `cpp_reference/test_move.cpp` @ [`c224825`](https://github.com/jakemartin/stratocracy-crew/commit/c224825) · 18/18 of the IDs that ran. All re-runnable via `python run.py` |
```

### Pair 5 — §3 ledger, the Repair and Type-effectiveness rows

The remaining two of the five bare citations, one per cell.

**OLD**
```
| **Repair (owned-tile heal, §2.7)** | agent | ✓ | `Combat.cpp::repairAmount` @ [`5ffa8d6`](https://github.com/jakemartin/stratocracy-crew/commit/5ffa8d6) · T-REPAIR-01..07 (7/7) |
| **Type-effectiveness (§3 spec)** | agent | ✓ | `Combat.cpp::effectiveness` @ [`5ffa8d6`](https://github.com/jakemartin/stratocracy-crew/commit/5ffa8d6) · T-COMBAT-09..10 (neutral, 2/2) |
```
**NEW**
```
| **Repair (owned-tile heal, §2.7)** | agent | ✓ | `cpp_reference/Combat.good.cpp::repairAmount` @ [`5ffa8d6`](https://github.com/jakemartin/stratocracy-crew/commit/5ffa8d6) · T-REPAIR-01..07 (7/7) |
| **Type-effectiveness (§3 spec)** | agent | ✓ | `cpp_reference/Combat.good.cpp::effectiveness` @ [`5ffa8d6`](https://github.com/jakemartin/stratocracy-crew/commit/5ffa8d6) · T-COMBAT-09..10 (neutral, 2/2) |
```

### Pair 6 — §4.8, the same path cited with the same commit

Outside the ledger table, and outside the five: §4.8 repeats the
`Combat.cpp::effectiveness` citation with the same commit.

**OLD**
```
(`Combat.cpp::effectiveness` @ `5ffa8d6`) hardcodes the neutral stub; this
```
**NEW**
```
(`cpp_reference/Combat.good.cpp::effectiveness` @ `5ffa8d6`) hardcodes the
neutral stub; this
```

### Pair 7 — §4.9, where the certified sources live

The old text names `Combat.cpp` as a canonical crew-repo path, which is the same
defect one section over, and its "each §4.7 stub as it lands" is now
three-quarters landed. **The NEW text cites no path.** §4.9 §1 is a layout
statement, not an inventory: what it needs to say is that the canonical home of
the certified sources is the crew repo rather than the UE project, and the §3
ledger is what cites the files. A sentence that cites no path cannot cite one
wrongly.

Three revisions of this pair each kept one path-shaped element and each drew a
finding: a commit binding, then a group label, then a directory governing a
"there". The element is gone rather than narrowed. The alternative permitted
route — enumerating every week-1 path in full inside this sentence — was
available and is recorded here as the fallback if the Director wants §4.9 to
carry an inventory after all; it would be verbose and correct, where the drafted
text is short and cites no path.

**OLD**
```
sources (`Combat.h`/`Combat.cpp` today; each §4.7 stub as it lands) live
canonically in the crew repo, where the `g++`/`clang++` + `python run.py` gate
```
**NEW**
```
sources live canonically in the crew repo, and each §4.7 stub joins them as it
lands — where the `g++`/`clang++` + `python run.py` gate
```

---

## TARGET 3 — §3's status paragraph, whose second half is now false

The replaced text is the closing two sentences of the italic status line. What
it asserted — three rows `*pending*`, no hex-grid, movement or DataTable source
in the repo, the repo holding the Combat module alone — is false at 2026-08-02
in every clause. The date is stated as a date, not as a distance from the last
commit: I was given `c224825`'s position in the history but not its authoring
date, so "N days past the last commit" is a figure I do not have.

### Pair 8 — §3, the ledger status line

**OLD**
```
This draft stands at 2026-08-01, three days past the last code commit: §4.4's week-1 deliverable is §4.11 rows 1–3 — grid and hex math, the §4.8 tables, movement and pathfinding — and all three still read `*pending*` in the table below, with no hex-grid, movement or DataTable source in the crew repo, which holds the Combat module alone. Because §4.11's critical path runs 1 → 3 → 4 → 5 → 6/8, nothing §4.4 schedules for weeks 2–3 clears without those three rows — only row 2 itself, row 10(a)'s format spec, T-INT-01/04 and the parallel UMG skeletons proceed meanwhile — so weeks 2–3 move with week 1 one for one rather than absorbing it, which is why §4.5 now carries that as a named risk with a cut line attached rather than as a discovery.
```
**NEW**
```
This draft stands at 2026-08-02, at commit [`c224825`](https://github.com/jakemartin/stratocracy-crew/commit/c224825) — the head of `main` in the crew repo, whose parent is `2fcbf32`. §4.4's week-1 deliverable is §4.11 rows 1–3 — grid and hex math, the §4.8 tables, movement and pathfinding — and **week 1 closed two of the three**: rows 1 and 3 passed their full acceptance sets at that commit (T-HEX-01..07, 7/7; T-MOVE-01..06, 6/6) and flip in the table below. **Row 2 does not flip.** Its headless half is green — T-DATA-01..04 and 06, 5/5 — but T-DATA-05, the in-editor Unreal Automation parity pass, has not run, and Q29 requires the full acceptance set at one commit, so the row records a partial pass and stays unverified; the editor pass is not yet due, so that is the ordinary schedule and not §4.7's cut line firing. What week 1 did **not** close is everything after it: rows 4–8 hold no code, and since §4.11's critical path runs 1 → 3 → 4 → 5 → 6/8, its first two links are now evidence rather than schedule and **row 4 (Capture & Fame) is blocked on nothing but itself**. §4.5's *Specification outruns the build* risk is therefore reduced and re-scoped rather than retired, and that row now states the arithmetic.
```

---

## TARGET 4 — the populated-rows paragraph, and the evidence sentence the new rows need

**Why the new rows get their own sentence.** The existing sentence says "a live
CrewAI run authored the module." That is true of the Combat rows and **not** of
the week-1 rows: a Claude Code session authored all three week-1 modules from
Director-written spec stubs, and `crew/tasks.py` is still written against the
Combat spec alone. Author is *agent* under §3's legend either way — that column
does not distinguish harnesses — but the prose does, and a ledger whose whole
purpose is not over-claiming cannot describe a crew run that did not happen. So
the paragraph now carries two evidence sentences and says why there are two.

The head count also changes twice over: six rows carry a ✓ and a seventh carries
evidence without one, which is a distinction the old "*Four rows are now
populated*" opening had no room for. And `main`'s head has moved off `2fcbf32`,
so the ancestry parenthetical is restated from the new head. One inherited
shorthand is corrected while this paragraph is open: the source text writes
"`spec/combat_spec.md` (+ `combat_spec_addendum.md`)", the prefix on the first
item only, and the path convention above does not permit it.

**Read as a whole against the path convention**, since this is the longest block
that merges. Every path it names is written in full —
`spec/combat_spec.md`, `spec/combat_spec_addendum.md`, `spec/hex_spec.md`,
`spec/data_spec.md`, `spec/move_spec.md`, `crew/tasks.py`,
`cpp_reference/Combat.good.cpp` and `cpp_reference/test_combat.cpp`. Three
tokens are deliberately not citations and are not written as paths: `python
run.py`, a command inherited from §3's own Test suite row; `build/`, named as
the subject of a claim about tracking rather than as a source; and the two bare
names `Combat.cpp` and `test_combat.cpp`, quoted as the defect the sentence
exists to record, in the same clause that says neither has ever existed.

### Pair 9 — §3, the paragraph under the ledger table

**OLD**
```
Four rows are now populated — the headless Combat module built for the Assignment-3 agent crew ([github.com/jakemartin/stratocracy-crew](https://github.com/jakemartin/stratocracy-crew), commit [`5ffa8d6`](https://github.com/jakemartin/stratocracy-crew/commit/5ffa8d6)): **Combat resolution** and its **Test suite**, plus **Repair** and **Type-effectiveness**, all agent-authored from `spec/combat_spec.md` (+ `combat_spec_addendum.md`) and verified by the real compile+test gate — a live CrewAI run authored the module and the Test Engineer certified **17/17** on a live `g++`/`clang++` compile+run. *(Commit `5ffa8d6` is published: it is an ancestor of `main` at [`2fcbf32`](https://github.com/jakemartin/stratocracy-crew/commit/2fcbf32) on the public remote, so every link above resolves and the ledger's "independently checkable" claim is testable by clicking it.)* The remaining rows fill in the same format — commit + passing test IDs — as each system clears the gate.
```
**NEW**
```
**Six rows now carry a ✓, and a seventh carries evidence without one.** Four came from the headless Combat module built for the Assignment-3 agent crew ([github.com/jakemartin/stratocracy-crew](https://github.com/jakemartin/stratocracy-crew), commit [`5ffa8d6`](https://github.com/jakemartin/stratocracy-crew/commit/5ffa8d6)): **Combat resolution** and its **Test suite**, plus **Repair** and **Type-effectiveness**, all agent-authored from `spec/combat_spec.md` (+ `spec/combat_spec_addendum.md`) and verified by the real compile+test gate — a live CrewAI run authored the module and the Test Engineer certified **17/17** on a live `g++`/`clang++` compile+run. **Hex grid & math** and **Movement & pathfinding** joined them at [`c224825`](https://github.com/jakemartin/stratocracy-crew/commit/c224825), and their evidence sentence is deliberately not the one above: a **Claude Code session** authored the three week-1 modules against the Director-written stubs `spec/hex_spec.md`, `spec/data_spec.md` and `spec/move_spec.md` — **not a live CrewAI run**, since `crew/tasks.py` is still written against the Combat spec alone — and the Test Engineer certified them through the same `python run.py` compile+run pipeline, **18/18 on the IDs that ran, under clang++ and MSVC both**. The author is an agent either way; the two sentences differ because the harness differed, and reporting a harness that did not run is the exact failure this ledger exists to prevent. Two IDs are recorded as **uncovered** rather than omitted: **T-DATA-05**, the in-editor Unreal Automation half, and **T-MOVE-07**, reserved and unwritten on Q2. The first is why **Data tables** is the seventh row and does *not* flip — T-DATA-01..04 and 06 are green at the same commit, but Q29 requires the full acceptance set at one commit, so that row records a partial pass and stays unverified. *(Commit `c224825` is the head of `main`; its parent is [`2fcbf32`](https://github.com/jakemartin/stratocracy-crew/commit/2fcbf32), so `5ffa8d6` remains an ancestor and every commit link above resolves. The **file** paths resolve too, which they previously did not: four evidence cells carried **five** bare citations between them — `Combat.cpp` three times and `test_combat.cpp` twice — and neither bare name has ever existed in this repository at any commit. Those five citations resolve to two tracked files, `cpp_reference/Combat.good.cpp` and `cpp_reference/test_combat.cpp`, which the cells now name in full; every path this table cites was probed at the commit its own row names. The `build/` directory is not tracked at all. That correction is what the "independently checkable" claim required, not a cosmetic one.)* The remaining rows fill in the same format — commit + passing test IDs — as each system clears the gate.
```

---

## TARGET 5 — §4.5's risk row: reduced and re-scoped, not retired

**69 is unchanged** — no acceptance ID was written this week, so the numerator
of the ratio does not move. Everything after it does. The arithmetic, from
figures already in §4.11's acceptance cells: T-HEX 7 + T-DATA 6 + T-MOVE 6 = 19
IDs across rows 1–3, of which **18 are green** at `c224825` (T-DATA-05 is the
one that did not run), leaving **69 − 18 = 51 unclosed** — T-DATA-05 plus the 50
in rows 4–10 (T-FAME 9, T-TURN 9, T-AI 6, T-SCN 10, T-UI 4, T-INT 5, T-SAVE 7).

The mitigation text is kept verbatim except its final clause, which named rows
1–3 as the slip surface. Those rows have landed; the slip surface is now rows
4–8, and row 2 has become the worked example of the clause about subset passes
rather than a hypothetical.

### Pair 10 — §4.5, the *Specification outruns the build* row

**OLD**
```
| **Specification outruns the build** — **69** written acceptance IDs at this revision (§4.7–§4.11) against **4** verified ledger rows (§3), all four inside Combat; §4.4 week 1 is due §4.11 rows 1–3 and all three read `*pending*` at 2026-08-01 | The **† cut line** (§4.7 head; members marked in §4.11's build-order table, which is authoritative for which side an ID is on) separates the IDs the MVP line above needs from the correctness infrastructure that stands down if the calendar takes it — so a slip drops named suites rather than silently thinning every suite. And the discipline Q20 and Q23 already applied holds for the rest of the table — *each piece lands in the week the thing that consumes it runs* (§4.4), and a gate that runs green over a subset does not flip its ledger row (Q29) — so a slip in rows 1–3 moves everything downstream of them rather than being absorbed by calling a row done on a partial pass |
```
**NEW**
```
| **Specification outruns the build** — **69** written acceptance IDs at this revision (§4.7–§4.11) against **6** verified ledger rows (§3). **Reduced and re-scoped at 2026-08-02, not retired:** no new ID was written this week, and **18** of the 69 are green at `c224825` — rows 1 and 3 closed their full acceptance sets and row 2's headless half passed — so the first two links of the critical path are evidence rather than schedule. **51 IDs remain unclosed**: T-DATA-05, which leaves row 2 unflipped, plus the 50 in rows 4–10, which hold no code | The **† cut line** (§4.7 head; members marked in §4.11's build-order table, which is authoritative for which side an ID is on) separates the IDs the MVP line above needs from the correctness infrastructure that stands down if the calendar takes it — so a slip drops named suites rather than silently thinning every suite. And the discipline Q20 and Q23 already applied holds for the rest of the table — *each piece lands in the week the thing that consumes it runs* (§4.4), and a gate that runs green over a subset does not flip its ledger row (Q29) — so a slip in rows 4–8 moves everything downstream of them rather than being absorbed by calling a row done on a partial pass. Row 2 is now that clause's worked example rather than its hypothetical: its headless suite is green and its ledger row is not |
```

---

## TARGET 6 — two stale "eight `*pending*`" counts this prompt did not name

**Five** ledger rows read `*pending*` after pairs 1–3 apply, not eight — Capture
& Fame, Turn loop, Opponent AI, Content/scenario and UI. Pairs 1–3 take Hex grid
& math, Movement & pathfinding and Data tables off that marker, the last of the
three without flipping it. Two sites state the old count of eight as a
present-tense fact. Both are edited here rather than filed, because a set
identity that no longer holds is exactly the drift the gate catches, and leaving
one of the two would be a half-applied edit.

The §4.7 heading keeps its stem — `4.7 Pending-system gate plan` — so every
cross-reference to §4.7 by number or by name still lands. The document contains
**no** internal `](#…)` anchors, so no link target moves.

### Pair 11 — §4.7, the section heading

**OLD**
```
### 4.7 Pending-system gate plan — the eight `*pending*` ledger rows
```
**NEW**
```
### 4.7 Pending-system gate plan — the eight ledger rows that read `*pending*` at 2026-08-01
```

### Pair 12 — §4.11, the build-order preamble

**OLD**
```
Rows 1–8 are the §4.7 stubs (the eight `*pending*` ledger rows); rows 9–10 are
the §4.9 and §4.10 systems. Combat, its test suite, Repair, and Type-effectiveness are
green at `5ffa8d6` and are prerequisites, not work items.
```
**NEW**
```
Rows 1–8 are the §4.7 stubs — the eight ledger rows that read `*pending*` when
this table was written, of which **rows 1 and 3 have since flipped** (§3); rows
9–10 are the §4.9 and §4.10 systems. Combat, its test suite, Repair, and
Type-effectiveness are green at `5ffa8d6` and are prerequisites, not work items.
**Rows 1 and 3 are green at `c224825`**, so rows 4–8 depend on landed code
rather than on scheduled code. **Row 2 is not green:** T-DATA-01..04 and 06 pass
at that commit and T-DATA-05 has not run, which is exactly the flip cost its †
bullet below already priced — reached by the ordinary schedule, since the editor
pass is not yet due, and not by the cut line firing.
```

---

## TARGET 7 — the gate's second recorded catch

§3 rests its whole argument on one worked example, T-COMBAT-07, and says of it
that the gate catches rules the agent hallucinates. Week 1 produced a second
case that is stronger on two counts — it blocked three invariants rather than
one, and the invariant that caught it compares against an oracle the module
cannot influence. That is a fact about the method §3 is documenting, so it
belongs in §3 and nowhere else. It is inserted immediately before "**This crew
is the buildable deliverable.**", which puts it beside the T-COMBAT-07 block it
generalises. Pair 13 cites no path.

**This pair's fences.** Its NEW text contains a fenced block of its own, so the
OLD and NEW delimiters below are **four** backticks. Copy everything between the
four-backtick lines, inner three-backtick block included; the inner fence is
part of the replacement text and terminates nothing.

### Pair 13 — §3, a second worked example

**OLD**
````
**This crew is the buildable deliverable.**
````
**NEW**
````
**A second recorded case, at `c224825`.** Movement did the same thing, and the block was wider:

```
T-MOVE-01/02/03: reachable-set exactness
  Pass 1  reachable set computed as hexDistance <= move — terrain never
          consulted. A plausible reading of "reachable"; not the §2.3 rule.
          Merge blocked on T-MOVE-01, T-MOVE-02 and T-MOVE-03 at once.
  Pass 2  Dijkstra over terrain cost, ties broken by canonical hex order →
          T-MOVE-01..06 green (6/6) → merged.
```

The load-bearing detail is what T-MOVE-01 compares against: an **independent** shortest-path pass written inside the test, not the module's own search. An invariant that re-runs the implementation agrees with it by construction and asserts nothing; this one could not, which is why a pass that was wrong *consistently* still failed it. Same shape as T-COMBAT-07, one layer deeper — there the spec's invariant caught a generalisation, here the test's own oracle caught a simplification.

**This crew is the buildable deliverable.**
````

---

## Build-order status at `c224825` — informational, not a replacement pair

Nothing below merges. It is the dependency read behind pairs 8, 10 and 12.

| # | System (ledger row) | Acceptance set | State at `c224825` | Unblocks |
|---|---|---|---|---|
| 1 | Hex grid & math | T-HEX-01..07 | **Closed, 7/7** | 3, and row 7's structural half |
| 2 | Data tables | T-DATA-01..04, 06 headless + 05 in-editor | **Headless 5/5; 05 not run — unflipped** | 3 and row 7's structural half, both already consuming it; the flip is a reporting debt, not a build block |
| 3 | Movement & pathfinding | T-MOVE-01..06 (07 reserved, Q2) | **Closed, 6/6** | **4**, row 7's priced half, row 9's T-INT-02/03/05 run scope, row 10(b) |
| 4 | Capture & Fame economy | T-FAME-01..09 | No code | 5 |
| 5 | Turn loop & win/tiebreak | T-TURN-01..09 | No code | 6, 8 |
| 6 | Opponent AI | T-AI-01..06 + smoke | No code | T-SAVE-02, T-SAVE-07 |
| 7 | Scenario file & validator | T-SCN-01..09, 11 | No code | 8, 10(b) |
| 8 | UI binding | T-UI-01..04 | No code | — |
| 9 | Integration parity | T-INT-01..05 | No code | — |
| 10 | Save & replay | T-SAVE-01..07 | No code | 9's T-INT-02 |

**The dependency most likely to blow up the schedule is row 4.** It is the sole
successor of row 3 and **the only unblocked row on the critical path**, and it
carries nine invariants against a §2.7 economy that took **four ruled questions**
(Q4, Q5, Q6, Q8) to become assertable. Rows 5, 6 and 8 all queue behind it. Two
other rows are unblocked but off the chain: **row 10(a)**, the format spec, which
§4.11 states has "no deps at all; write it first", and **row 7**, whose stated
dependencies — rows 1, 2 and 3 — all hold code at `c224825`. Row 2's unflipped
state is a reporting debt and blocks no build.

---

## Change requests

| Existing § | Current text | Proposed change | Why |
|---|---|---|---|
| §4.7 head note; §4.9 §1; §4.9 T-INT-04 | "compiled by the same `g++`/`clang++` + `python run.py` gate"; "where the `g++`/`clang++` + `python run.py` gate runs"; "StratRules compiles standalone under the existing g++/clang++ gate" | Name the gate's compiler set once, in whatever wording you prefer, and let the other two sites point at it | The week-1 run was certified under **clang++ and MSVC**, and pair 9 states that. These three sites name the set as `g++`/`clang++`, which does not include MSVC. I was not told whether MSVC is now a standing member of the gate, whether it ran only for the cross-compiler determinism T-HEX-07 asserts, or whether `g++` still runs — so I cannot edit them without inventing a tooling fact. Left unedited and filed. Note that T-INT-04's assertion text is one of the three, so this is gate wording, not only prose |
| §4.4, week-1 row | "1 \| Headless C++ core — §4.11 **rows 1–3** … **+ test suite.** Playable via debug commands." | Either leave it as the plan of record, or append the outcome — rows 1 and 3 closed, row 2 headless-only | §4.4 is a schedule; §3 is a status tracker. I did not touch §4.4, because those two sections disagreeing about status is the failure mode Q20 and Q23 both repaired, and duplicating an outcome into a plan table re-creates it. But a reader who opens §4.4 first sees week 1 in the future tense. Whichever you choose, it should be stated once — a document-policy call, not a technical one |

---

## Open questions for the Director

Four, none given a Q ID: the register is headed "Open questions (Director
rulings owed)" and numbering a row is a Director act. **Three are policy calls;
one is a fact I was not given.** Each names the gate or the edit its answer
produces. Questions carried in earlier revisions of this file are now answered
by the probes recorded in Target 2 and are not repeated here.

1. **Bar (b) — do rows 1 and 3 have your sign-off?** §3 requires both bars and
   bar (b) is the human review gate. Pairs 1 and 2 propose `✓` and cannot
   self-authorise it. **Effect of the ruling:** `✓` as drafted, or `—` **with
   the System cell unbolded** and the Evidence cell unchanged, plus the rest of
   the five coupled sites in the fallback table at the head of this file.
2. **Is MSVC a standing member of the compile gate, and does `g++` still run?**
   The first change request above cannot be written without this, and it is the
   one outstanding *fact* in this list. **Effect:** the three `g++`/`clang++`
   sites either gain MSVC or stay as drafted, and T-INT-04's assertion text
   follows whichever way it goes.
3. **Should the release record be tracked?** `build/acceptance_week1.json` is
   **ABSENT at `c224825`**, so it is not citable and no evidence cell cites it.
   **Effect:** tracking the record — by whatever means you prefer — would let a
   future ledger row cite the certification itself rather than only the sources
   plus a re-run instruction. Left as drafted until you rule, since changing a
   repo's ignore rules is not mine to do.
4. **Does §4.4 record outcomes, or does §3 own status alone?** See the second
   change request. **Effect:** one sentence in §4.4's week-1 cell, or a stated
   rule that the milestone table is the plan and never the status.

---

## Handoffs

- **rules-designer** — nothing owed. No pair here states, restates or implies a
  rule. Row 4 (Capture & Fame) is the next system to build and its nine
  invariants rest on the Q4/Q5/Q6/Q8 rulings; if any of those is to move, it
  should move before the module is authored rather than after.
- **scenario-designer** — **row 3 has landed**, which clears the movement
  precondition §4.11 named for row 7: "the scenario row flips after movement,
  not before." T-SCN-04, 06, 08 and 11 can now be priced against a real
  Dijkstra, and row 7's other two dependencies (rows 1 and 2) hold code as well,
  so row 7 is buildable now. The second gating condition I filed against that
  sentence in the rubric-round-2 addendum — the stretch-map-resident fixtures —
  is untouched by this week and still stands.
- **ux-onboarding-designer** — §2.11.6's guided opening is gated by T-SCN-06,
  which prices a Stub-3 path; that path now exists, so the opening's lane
  measurement is buildable rather than blocked. No layout or copy claim is made
  here.
- **Director** — the ✓s are contingent on your sign-off, and declining moves
  five sites including the System-cell bolding in pairs 1 and 2 (fallback table,
  top of file). The bare citations in §3's ledger are corrected by pairs 4 and
  5, and §4.8's copy of one of them by pair 6; **pair 7 cites no path**, since
  §4.9 §1 only needs to say that the canonical home of the certified sources is
  the crew repo, and the ledger is what cites files. **Every path this addendum
  cites is probed at the commit its row names** — `5ffa8d6` for the Combat
  family, `c224825` for the week-1 family — and no citation fails. Two "eight
  `*pending*`" counts go stale the moment pairs 1–3 apply and are handled in
  pairs 11–12; the compiler-set discrepancy is a change request rather than an
  edit because I was not given the fact it needs.

---

## Grounding

| Claim | Backed by |
|---|---|
| Commit `c224825` on `main`, parent `2fcbf32`, `5ffa8d6` an ancestor | Director-supplied, verified |
| Row 1: T-HEX-01..07, 7/7 · Row 2: T-DATA-01..04, 06, 5/5, T-DATA-05 did not run · Row 3: T-MOVE-01..06, 6/6, T-MOVE-07 reserved | Director-supplied, verified |
| 18 invariants, clang++ and MSVC both, via the `python run.py` pipeline that certified Combat | Director-supplied, verified |
| 7 + 5 + 6 = 18 green; 7 + 6 + 6 = 19 written across rows 1–3; 69 − 18 = 51 unclosed; rows 4–10 hold 50 (9 + 9 + 6 + 10 + 4 + 5 + 7) | Arithmetic on §4.11's acceptance cells and the 69 the rubric-round-2 recount established |
| **Five bare citations across four cells, resolving to two files** — `Combat.cpp` ×3 (bare in the Combat resolution cell, `::repairAmount` in Repair, `::effectiveness` in Type-effectiveness) and `test_combat.cpp` ×2 (Combat resolution, Test suite), which correct to `cpp_reference/Combat.good.cpp` and `cpp_reference/test_combat.cpp` | Counted from `source/gdd.md`'s ledger table, per citation rather than per cell, and matched against the probe sets below for the file count. The Combat resolution cell carries two citations, which is what the earlier counts of "three cells", "four cells" and "three and one" each missed; and neither corrected path is its bare name with a directory prefixed, which is what a shared-prefix phrasing implied |
| Row 2 does not flip on a headless-only pass | §4.11's T-DATA-05 † bullet, verbatim: "Cost: row 2's ledger flip, since Q29 requires the full acceptance set at one commit"; Q29's conservative reading in force |
| T-DATA-05 is the in-editor Unreal Automation half | §4.8's principle paragraph and the T-DATA invariant block; §4.11 row 2's Headless cell |
| **The two authoring passes:** movement pass 1 was `hexDistance <= move` and was blocked on T-MOVE-01/02/03; pass 2 was Dijkstra with canonical-order tie-breaks and passed 6/6 | Director-supplied, verified. Not established by the file evidence in the row below, and kept separate from it |
| **The oracle:** T-MOVE-01's expectation is computed by an independent pass inside the harness, not by the module's own search | `git show c224825:cpp_reference/test_move.cpp` — the tracked harness at the commit pair 13 concerns. Line 10: the comparison is "never against the module's own Dijkstra"; line 86: `// --- the independent oracle ---`; lines 87 and 90: repeated relaxation over every hex until nothing changes, `static std::vector<int> oracleCosts(const Board& board, ...)`, deliberately a different algorithm; lines 125 and 341: the two call sites where the expectation is built from `oracleCosts(...)`. **Extent:** this shows the harness at that commit contains an independently-computed expectation. It does not establish the two authoring passes above, and it is not a claim about what the suite proves at runtime |
| Author = agent, harness ≠ CrewAI: a Claude Code session, Director-written stubs, `crew/tasks.py` still Combat-only | Director-supplied, verified. Corroborated at the repository level: `git diff 5ffa8d6 c224825 -- crew/tasks.py` is empty, so the file is byte-unchanged across week 1 |
| **No `Combat.cpp`, no `build/Combat.cpp` and no root-level `test_combat.cpp` in any commit** — the whole-history extent, which neither a working-tree listing nor a single-commit check can establish | Director-supplied, verified: `git log --all --diff-filter=A --name-only` and `git rev-list --all --objects` in `stratocracy-crew`. Every Combat-matching path the repository has ever held is `cpp_reference/{Combat.buggy.cpp, Combat.good.cpp, Combat.h, test_combat.cpp}` and `spec/{combat_spec.md, combat_spec_addendum.md}` |
| Each path pairs 4–6 cite exists at `5ffa8d6`, and `Combat.cpp` does not exist there either | Director-supplied, verified by **per-path existence probe** — `git cat-file -e 5ffa8d6:<path>`: EXISTS for `cpp_reference/Combat.good.cpp`, `cpp_reference/test_combat.cpp`, `cpp_reference/Combat.h`, `cpp_reference/Combat.buggy.cpp`, `spec/combat_spec.md`, `spec/combat_spec_addendum.md`, `crew/tasks.py`; ABSENT for `Combat.cpp` and `build/Combat.cpp`. A probe is what establishes that a **specific citation** resolves, where a filtered listing only shows what a query returned |
| Each path pairs 1–3 cite exists at `c224825` — the three `.good.cpp` modules, their three harnesses, the three `data/` CSVs, the three `cpp_reference/*.h` headers, the five `spec/` files and `crew/tasks.py`; `build/acceptance_week1.json` and `build/Hex.cpp` are ABSENT | Director-supplied, verified by the same per-path form — `git cat-file -e c224825:<path>`. This replaces the working-tree listing an earlier revision rested on |
| Every citation is probed at the commit its own row cites — pairs 1–3 at `c224825`, pairs 4–6 at `5ffa8d6`. **Pair 7 cites no path**, so it needs no probe | The two probe sets above, read against the commit each pair's rows name. No probe at one commit is used to support a citation at the other |
| Extent of every probe set: named paths at **one** commit, path existence only — never file content, never another commit | Stated in Target 2. The "never at any commit" claim rests on the two whole-history checks, not on any probe |
| Nothing under `build/` is tracked | Director-supplied, verified, counted three ways: **0** tracked entries under `build/` at `c224825`, **0** at `5ffa8d6`, and **0** ever added across all refs |
| Critical path 1 → 3 → 4 → 5 → 6/8; row 4 the sole successor of row 3 on that chain | §4.11's critical-path paragraph and the Depends-on column |
| Row 10(a) has no dependencies; row 7 depends on rows 1, 2, 3 — so neither is blocked, and row 4's "only unblocked" claim is scoped to the critical path | §4.11 row 10's cell, verbatim: "no deps at all; write it first"; §4.11 row 7's Depends-on cell |
| Row 4's rules took four ruled questions | Q4, Q5, Q6 and Q8 in §4.7's register, each marked RULED and each naming a T-FAME ID. **Q14 is not ruled** — it sits inside the open Q10–Q19 range §4.7's register summary states |
| Both bars required for `✓`; bar (b) is the human review gate | §3, "Agent-verified = both bars" |
| A `✓` row is bolded and a `—` row is not, so a declined sign-off unbolds the System cell as well as clearing the mark | §3's ledger table as synced: the four `✓` rows (Combat resolution, Test suite, Repair, Type-effectiveness) are bolded; all eight `—` rows are not |
| Exactly eight rows read `*pending*` at 2026-08-01; five after pairs 1–3 apply | Count of the ledger table as synced — Hex, Movement, Capture & Fame, Turn loop, Opponent AI, Data tables, Content/scenario, UI — less the three rows pairs 1–3 rewrite, leaving Capture & Fame, Turn loop, Opponent AI, Content/scenario, UI |
| No internal anchors, so pair 11 breaks no link | `](#` returns zero matches document-wide |
| Straight ASCII apostrophes and quotes at every anchor | `§4.4's` returns 4 matches, `§4.4’s` returns 0 |
| No new acceptance ID written, so 69 holds | Director-supplied; no pair here adds a `T-` ID |
| No Q registered | Deliberate. Numbering a register row is a Director act; the four questions above are unnumbered, and neither extent-bearing site of the register is touched |

---

## PLACEMENT

| Pair | Section | Exact site |
|---|---|---|
| 1 | §3 | Ledger table, the *Hex grid & math* row |
| 2 | §3 | Ledger table, the *Movement & pathfinding* row |
| 3 | §3 | Ledger table, the *Data tables (units/terrain)* row |
| 4 | §3 | Ledger table, the *Combat resolution* and *Test suite* rows (two adjacent lines, one block) |
| 5 | §3 | Ledger table, the *Repair* and *Type-effectiveness* rows (two adjacent lines, one block) |
| 6 | §4.8 | Type-effectiveness schema paragraph, the parenthetical citation |
| 7 | §4.9 | Item 1, *Module layout — one source, two compilers* |
| 8 | §3 | The italic *Status: live tracker* line, its second half, inside the closing italic marker |
| 9 | §3 | The paragraph immediately below the ledger table |
| 10 | §4.5 | Risks table, the *Specification outruns the build* row |
| 11 | §4.7 | The section heading |
| 12 | §4.11 | The build-order preamble, first three lines |
| 13 | §3 | Inserted immediately above "**This crew is the buildable deliverable.**" — **four-backtick fences** |

No pair touches §1, §2, the Q register, §4.4, or §4.11's build-order table rows
and † legend. Pairs 1–5 edit five separate lines of one table and do not
overlap: the ledger's row order is Combat, Test suite, Hex, Movement, Capture,
Turn loop, AI, Data tables, Repair, Type-effectiveness, Content, UI — so pair 4
sits above pairs 1–2, pair 3 sits above pair 5, and no OLD block spans another
pair's anchor.

---

## SUMMARY FOR THE DIRECTOR

Thirteen replacement pairs across §3, §4.5, §4.7, §4.8, §4.9 and §4.11, each OLD
block confirmed to occur exactly once in the synced source. §4.11 rows 1 and 3
flip to agent / ✓ / `c224825` on their full acceptance sets — T-HEX-01..07 (7/7)
and T-MOVE-01..06 (6/6) — and both ✓s are contingent on your bar-(b) sign-off,
with the fallback tabulated at the top of the file across **five** coupled
sites, the first of them being the System-cell bolding inside pairs 1 and 2
themselves. **Row 2 stays visibly unflipped**: unbolded name, `—` in
Agent-verified, and an Evidence cell that opens "Partial pass — not a flip"
before recording T-DATA-01..04 and 06 green at the same commit, because §4.11's
own † bullet prices T-DATA-05 as row 2's flip cost under Q29 and a green
headless half does not change that reading — with the added note that the row is
unflipped by the ordinary schedule, not by the cut line firing. §3's status
paragraph and its populated-rows paragraph are rewritten to 2026-08-02, the
latter carrying a second evidence sentence stating that a Claude Code session
authored the week-1 modules from Director-written stubs and **not** a live
CrewAI run, since `crew/tasks.py` is still Combat-only; §4.5's risk row keeps
69, moves to six verified rows, and states that 18 IDs are green and **51 remain
unclosed**, so the risk reads as reduced and re-scoped rather than retired. I
judged the citation defect in scope rather than a change request — the ledger's
"independently checkable" claim is the thing pairs 1–2 lean on — and it counts
in three units that must not be conflated: **five bare citations, across four
cells, resolving to two files**, `cpp_reference/Combat.good.cpp` and
`cpp_reference/test_combat.cpp`, both named in full wherever the correction is
described. Pairs 4 and 5 carry it in the ledger and pair 6 fixes §4.8's separate
copy. **Under your path ruling, every path in anything that merges is written in
full, with no construction requiring the reader to distribute a prefix**, and
pair 7 takes the other permitted route — **its NEW text cites no path**, because
§4.9 §1 only needs to say that the canonical home of the certified sources is
the crew repo, and the ledger is what cites files. The only two constructions
left under the exemption are pair 9's OLD anchor and the Target 4 sentence
quoting it. **Every citation is probed at the commit its own row cites** — `git
cat-file -e` per path, pairs 1–3 at `c224825` and pairs 4–6 at `5ffa8d6`; the
"never at any commit" extent rests on two whole-history checks. Two sites this
prompt did not name state "the eight `*pending*` ledger rows" as present tense
and go stale the moment pairs 1–3 land: §4.7's heading and §4.11's build-order
preamble, both edited; five rows still read `*pending*` afterwards. Four
questions are filed — three policy calls and one outstanding fact, whether MSVC
is a standing member of a gate three sites still describe as `g++`/`clang++`,
which is why that discrepancy is a change request rather than an edit.
