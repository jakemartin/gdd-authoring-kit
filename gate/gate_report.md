# Continuity gate — run `row5-2`

`source/MANIFEST.txt` present (no `sync-missing`). `gdd.md` md5
`10b9a7ab4c5fbb4a7464faea37821122`, unchanged from `row5-1`. One file gated:
`sections/tech_row5-turn-loop.md` (eleven OLD/NEW replacement pairs) — and no
other.

**Top-level verdict: PASS. Total violations: 0.**

Every pair was judged as **merging text**; the pair headings, placement table,
grounding note, merge precondition and the "None" answers under Open questions /
Change requests / Handoffs were judged as **non-merging apparatus**. Neither
category yields a violation. Where a risk is named below, it is labelled with the
category it lands in.

---

## `sections/tech_row5-turn-loop.md` — **PASS** (0 violations)

### The four `row5-1` findings

| `row5-1` finding | State at `row5-2` |
|---|---|
| 1 · `placement-collision` (doubled `**` at pair 3's join) | **Withdrawn — and the withdrawal is correct.** Re-derived below. |
| 2 · `dead-reference` (§4.10 save header cited for `sideToMove`) | **Fixed.** |
| 3 · `dead-reference` (bare `` `Combat.h` ``) | **Fixed.** |
| 4 · `dead-reference` (bare `` `Economy.h::killAward` ``) | **Fixed.** |

**Finding 2.** Pair 3 now reads: *"read off two sites that keep the turn number
and the side to move as separate fields — §4.7 Stub 8's UI snapshot `match
{turn, turnCap, sideToMove, resultTier or null}`, and §4.10's canonical state
hash, which serializes `GameState` in a fixed field order beginning turn
counter, side to move"*. Both sites verified against `source/gdd.md`:
`sideToMove` occurs **exactly once** in the document, in §4.7 SPEC STUB 8's
snapshot field list; §4.10's canonical-state-hash paragraph reads *"serialize
the `GameState` in a fixed field order — turn counter, side to move, per-side
`fameTotal`/`fameCombat`, …"*. §4.10's file-layout table is no longer cited for a
`match` group it does not carry.

**Findings 3 and 4.** Pair 3's NEW block now carries `cpp_reference/Combat.h`
and `cpp_reference/Economy.h::killAward`. A search of the whole addendum returns
no surviving bare `Combat.h` or `Economy.h` in any form.

### Re-derivation of the withdrawn finding — the `row5-1` gate was wrong

I reach the **opposite** conclusion to `row5-1` and agree with the
orchestrator's byte-level check. Evidence, taken with a byte/line-oriented tool
(anchored ripgrep), not a Markdown-aware one:

- Addendum line 40 against `not the first of those\.\*$` — the `$` anchor matches
  immediately after the asterisk, so the OLD block's final two bytes are `.` `*`
  and no byte follows on that line:

      40:and a setter for the turn number is not the first of those.*

- `source/gdd.md` against `not the first of those\.\* Legend:` — **1
  occurrence**. The asterisk-inclusive OLD block is unique and is followed by
  ` Legend:`.
- Pair 3's NEW block against `no file format is defined or read\.\*$` — **1
  occurrence**; the NEW block terminates in exactly one `*`.

Applied, §3's status line closes `…no file format is defined or read.* Legend:`
— one italic open at `*Status:`, one italic close. Correct. The `row5-1`
report's own quotation of the OLD block, which dropped its final byte, was the
defect, not the addendum.

Same class, checked while I was there: pair 3's NEW introduces a nested italic
run, `*both players draw income from turn 2*`, inside the outer italic status
line. That is already the line's own convention — the unedited text carries
`§2.6's *the forecast the player sees is exactly what resolves*` in the same run
— and the delimiter runs pair to each other, not to the outer run. No finding.

### What was checked and cleared

**Uniqueness and disjointness.** Pairs 1–3 are disjoint spans of GDD line 1466;
pairs 5–7 of line 1483; pairs 8–9 of line 1537; pairs 10 and 11 of §4.11's
preamble (lines 2639–2640 and 2646–2649). No OLD block is a substring of
another, and no two pairs target the same span. Only one file is in this stage,
so no cross-section collision is possible. The placement table's claim that
pairs 1–3, 5–7 and 8–9 are order-independent disjoint spans is accurate.

**Commit substitution — complete and consistent.** Every row-5 binding names
`ad77b13` and nothing else: pair 2 (`at ad77b13 only rows 6–8 hold none`), pair 3
(the record, the `main()` count, the closing state), pair 4 (ledger evidence
cell), pair 6 (populated-rows record and the `crew/tasks.py` extent), pair 8
(§4.5's green split), pair 11 (§4.11's green-rows sentence). The three `caa8267`
survivals are each a parent/ancestor reference and each correct against Fact P —
pair 1's parent link, pair 7's parent link plus the widened ancestor list
`5ffa8d6, c224825, 9f87ecd, 647d4df, caa8267`, and the grounding note's
byte-identity clause (apparatus). The `647d4df` survivals in merging text are
each bound to row 4 or to the driver sandbox and stay true there: pair 3's *"the
same free sandbox it was at `647d4df`"*, pair 8's *"**9** at `647d4df`, where
T-FAME-01..09 closed row 4"*, pair 11's *"row 4 at `647d4df`"*.

**Arithmetic, re-derived from §4.11 rather than accepted.** Written IDs by row:
7 + 6 + 6 + 9 + 9 + (6 + 10 + 4 + 5 + 7) = **69**, and no new ID is written.
Green: 18 + 9 + 9 = **36**. Unclosed: T-DATA-05 + **32** in rows 6–10 = **33**;
36 + 33 = 69. Rows 6–10's 32 = T-AI 6 + T-SCN 10 + T-UI 4 + T-INT 5 + T-SAVE 7,
which also confirms the OLD text's 41 for rows 5–10. Verified ledger rows 7 →
**8**; evidence-carrying rows 8 → **9**, so Data tables becomes the *ninth* row
in pairs 5 and 6 on the same "row carrying evidence" ordinal §3 already uses.
`main()`-defining tracked sources 8 → **nine** = seven harnesses + one duel
simulator + one REPL, and *"the eight named above"* resolves: seven are listed
by name in the driver sentence and the eighth,
`cpp_reference/test_economy.cpp`, in the row-4 sentence.

**Tense bindings.** Every claim bound to `647d4df` stays bound there; every claim
bound to `ad77b13` is true there per Facts P and Q. Pair 3 correctly does *not*
repeat the row-4 tail's *"no way to … play a match"* — a turn structure now
exists — and states only what `ad77b13` does not have.

**Fact M compliance.** No OLD block contains the "Playable via debug commands"
ruling or its amendment; no NEW block states, implies or pre-empts a re-ruling,
and none restates that the ruling has re-opened.

**Cross-checks against unedited source.** §2.8's *"one guard, one three-key
comparison, and one grade"*; Stub 5's T-TURN-04..07 content; T-TURN-08's *"this
gate asserts the turn loop calls it at the right moment with the right board
facts, nothing more"*; Q7 ruled as per-scenario data; Q10 open, naming
`isFlag`/Stub 7; Q29's conservative reading; T-FAME-07's flat 500 flag award;
§2.7's *"both players draw income from **turn 2**"*; §4.4's week-3 row for §4.11
rows 4–5; §4.11 row 6's dependency cell reading `5`; the Repair row's
T-REPAIR-01..07 @ `5ffa8d6`. All agree with the addendum as written.

**Lane and knowledge base.** All eleven pairs land in §3, §4.5 and §4.11 —
`tech-director`'s lane, no scope breach. Nothing touches §2, so `kb_rules.md` is
unaffected; its turn-cap and cap-resolution blocks stay correct as parsed. No
`kb-desync`.

**Register.** Declarative and present-tense, matching §3's existing evidence
prose sentence for sentence. No UI strings are written, so no faction-voice or
system-voice surface is touched.

---

## The addendum's own highest-risk new phrases

Named as requested. **None is filed as a violation** — each is grounded and each
is true as written. Ranked by how likely it is to be the one that is wrong.

1. **"the module refuses a cap below 1 rather than substituting a default"**
   (pair 3, *merging*). The addendum's only new *behavioural* claim. Nothing in
   §2.8, §2.11.4, Q7 or Stub 7's `turnCap` row states a lower bound or a
   refusal, so once merged this sentence is the document's first and only
   statement of one, resting on Fact E alone. If §3 prose is ever read as
   normative, this is the line that becomes a rule nobody ruled.
2. **"`g++` is not installed on this machine"** (pair 3, *merging*). Deictic:
   the GDD has no antecedent for "this machine", and §3 records a few hundred
   words earlier that Combat was certified at `5ffa8d6` *"on a live
   `g++`/`clang++` compile+run"*. Both are true — different harness, different
   time — but the sentence invites the reading that they are not.
3. **"the §2.8 facts arrive as a caller-supplied `BoardSnapshot`"** (pair 3,
   *merging*). `BoardSnapshot` occurs nowhere in `source/`; it is a source-code
   identifier entering the GDD on Fact E's word, and it is the load-bearing half
   of the "it owns **no board**" claim.
4. **"§2.11.4 displays the counter as `N / turnCap`"** (pair 3, *merging*).
   §2.11.4 literally renders `TURN 12 / 20`; `N / turnCap` is the addendum's
   abstraction of it. Defensible — §2.11.4's bullet says the widget *"reads
   `turnCap` from the scenario rather than hardcoding a number"* — but it is a
   paraphrase presented as a citation, and stated reading 2 rests entirely on it.
5. **"an AI or a scenario file (rows 6–8)"** (pair 3's closing sentence,
   *merging*). Two systems, three row numbers; row 8 is UI binding. Fact L
   phrases it this way and pair 2 has already said correctly that rows 6–8 are
   the rows holding no code, so it reads through — but the parenthetical does
   not enumerate what it appears to enumerate.
6. **"the first four links of the critical path are evidence rather than
   schedule"** and **"row 6 (Opponent AI) is blocked on nothing but itself"**
   (pairs 2, 8, 11, *merging*). The only claims here that depend on §4.11's
   *table body*, which this addendum deliberately does not edit. True today;
   they are the phrases that will need re-cutting first when row 6 lands.
7. **"no file format is defined or read"** (pair 3, *merging*). True of the
   build at `ad77b13`, in a document whose §4.10 and Stub 7 both define file
   formats on paper. Context carries it; nothing else does.
8. **The grounding note's "Fact H backs every figure in pair 8 and pair 3's 69,
   27 → 36 and 8-verified-rows clauses"** (*apparatus*). Pair 3 has no
   8-verified-rows clause; pair 8 carries the "**8** verified ledger rows"
   figure and pair 5 carries the ✓-count. Fact H backs both and "every figure in
   pair 8" already covers the figure, so the attribution is loose rather than
   wrong. Same paragraph: pairs **5, 9 and 10** are never named in the grounding
   note. Each is an arithmetic or consequential edit checkable against the
   merged document itself, which is why none is filed — but a grounding note
   that skips three of eleven pairs is one edit away from the exact defect
   `row5-1` filed.

## The three items held back from this file

A view was asked for; none is a finding against this addendum.

- **§4.11's row-9 dependency cell** — *"re-open when rows 4–5 add
  `Capture`/`Build`/`EndTurn`"*. Correctly held back: it sits in the table body
  this addendum does not touch, row 9 holds no code, and a gate that has never
  run cannot re-open. Note for the Director that after this merge it is the
  document's only remaining future-tense clause whose antecedent is fully
  satisfied, and it belongs to whoever files rows 9–10.
- **§4.8's bare `Combat.h`** — correctly held back. §3's lineage parenthetical
  scopes its "every path this table cites was probed" claim to the ledger table,
  so §4.8 lies outside it and this addendum does not widen the claim.
- **The T-CAP / T-TURN two-family seam** — correctly held back from a
  subject-scoped file, and it should reach the Director **at this merge** rather
  than the next. Row 5 flipping is what makes it bite: §2.8 phrases its own
  invariants as T-CAP-01..08, no T-CAP ID appears in any acceptance set, and
  this addendum's own *"T-TURN-04, 05, 06 and 07 encode §2.8's procedure
  exactly"* is precisely the bridge between the two families — asserted in §3
  prose, gated nowhere.

---

## Verdict

`sections/tech_row5-turn-loop.md` passes with zero violations, so run `row5-2`
is **PASS** and the addendum is clear to merge. All three accepted `row5-1`
findings are fixed in place: both citations now carry their `cpp_reference/`
paths, and stated reading 1 is re-sourced to §4.7 Spec Stub 8's `match` snapshot
and §4.10's canonical state hash — the document's only two sites that hold the
turn number and the side to move as separate fields. The withdrawn
`placement-collision` is confirmed withdrawn on my own byte-exact re-derivation:
pair 3's OLD block does include the closing `*`, that asterisk-inclusive string
occurs once in `source/gdd.md`, and the merge yields exactly one italic close,
so the `row5-1` gate — not the addendum — was wrong. The commit substitution to
`ad77b13` is complete and consistent across §3, §4.5 and §4.11, the three
`caa8267` survivals are each a correct parent or ancestor reference, and the
69 / 36 / 33 / 8 / 9 arithmetic re-derives unaided from §4.11's acceptance sets.
Before merge, one thing must still happen, and it is the addendum's own stated
precondition rather than a waiver of mine: **`ad77b13` must be pushed before
this addendum is applied**, because pairs 1, 3, 4, 6 and 7 add commit links to
it and pair 7 keeps the document's standing claim that every commit link
resolves; the Director should take the T-CAP / T-TURN seam as a noted item at
the same time.
