# Gate report — run `row5-rulings-3`

- `source/MANIFEST.txt`: **present**, resolved against the kit root
  `E:\MultiAgent\gdd-authoring-kit`. No `sync-missing`.
- `gdd.md` md5 at this run: `ca397f4f2eca447b451fca2ca2393092` — matches the
  MANIFEST line and the md5 both drafts declare in their Placement headers.
- Files gated: `sections/rules_row5-rulings-and-t-cap-05.md` (6 pairs),
  `sections/tech_row5-rulings-t-turn-10.md` (13 pairs).

## Top-level verdict: **PASS**

| File | Verdict | Violations |
|---|---|---|
| `sections/rules_row5-rulings-and-t-cap-05.md` | **PASS** | 0 |
| `sections/tech_row5-rulings-t-turn-10.md` | **PASS** | 0 |

Both round-3 fixes are confirmed on the bytes, and both were made by deletion or
restoration rather than substitution, as the standing rule requires.

---

## What was re-derived independently, not accepted

Nothing below rests on the orchestrator's report or on an earlier run of mine.
Every figure was re-run against `source/gdd.md` at the md5 above.

### 1. TECH pair 7 — the insertion risk, checked first and hardest

Pair 7 had text restored into it, so it was the pair most likely to have flipped
from replacement to insertion. Re-derived:

- `**20 IDs remain unclosed**` occurs **once** in the master, at line 1558 — the
  pair's own anchor. `**21` occurs at line 1571 only, in §4.6's token table, and
  nowhere in §4.5.
- Pair 7's OLD carries `**20 IDs remain unclosed**`; its NEW carries
  `**21 IDs remain unclosed**` and carries the string `20 IDs` nowhere.
- Therefore the NEW does **not** contain the OLD. **Pair 7 is a replacement.**

The restored clause is byte-identical on both sides: `— so everything on the
critical path but row 8 is evidence rather than schedule.` appears in pair 7's
OLD and in pair 7's NEW, and the identical phrase `evidence rather than
schedule` occurs at exactly two master sites — line 1487 (§3) and line 1558
(§4.5). Restoring it is what keeps those two sections stating one fact in one
voice, which is what K2 blocked on. Confirmed.

### 2. Pair census

Re-derived by substring test on the current bytes of both drafts:

| File | Pairs | Replacements | Insertions |
|---|---|---|---|
| rules | 6 | 5 | 1 (pair 6, §2.13.3 — NEW contains OLD as a prefix) |
| tech | 13 | 12 | 1 (pair 11, Stub 5 — NEW contains OLD as a prefix) |
| **total** | **19** | **17** | **2** |

This agrees with the orchestrator's independent count. All 19 OLD anchors were
located in the master and each matches exactly once. No NEW text is already
present in the master — in particular `T-TURN-10` occurs **zero** times in
`source/gdd.md` today, and `21 IDs` occurs zero times.

**Cross-file overlaps: zero.** RULES occupies lines 235–238, 353–356, 375, 383,
388–391, 1160–1161. TECH occupies line 1487 (×5), 1558 (×2), 1727–1731,
1753–1754, 1758–1759, 1778–1779, 1781, 2705. Disjoint, and disjoint within each
shared line as well.

### 3. The five §3 sentences after harmonisation

The class was re-derived by property, not by phrase — the failure recorded at
J2/K5. `§4.5's 69` occurs 4× and `§4.5's 69-ID` 1×, all on line 1487; a bare
`\b69\b` sweep returns those five plus two inside pair 6's own OLD at 1558 and
three unrelated dollar figures in §4.6 (`$0.69` at 1569, 1572, 1596). **The
class is exactly five and all five are paired.**

Anchor uniqueness after harmonisation, checked as instructed:

- No OLD is a substring of any other. Pairs 2, 3 and 5 are separated by their
  green-count deltas (`18 → 27`, `27 → 36`, `42 → 49`); pair 4 by its
  `IDs close: ` prefix *and* its delta `36 → 42`; pair 1 shares no text with the
  other four beyond `§4.5's 69`, and is distinguished by `-ID count does not
  move`.
- Byte order along line 1487 confirmed: the driver clause (pair 1) precedes all
  four row clauses, which then run 18 → 27, 27 → 36, 36 → 42, 42 → 49. Pair
  numbering matches.
- The harmonised name `written-ID count` is vocabulary the master already
  carries — line 2444, Q32: *"A ruling that mints an ID for one of the checks
  would move §4.5's written-ID count"*. K6's rationale checks out.

### 4. `T-TURN-10`'s three states, and §4.5's green count

Fact E requires WRITTEN, UNBLOCKED, ASSERTING, NOT GREEN. Every sentence in both
files that touches the ID was checked against that:

- tech pair 6 NEW: *"it is **written, unblocked and asserting, and not green**,
  because the code that satisfies it does not exist yet"* — correct, all four.
- tech pair 7 NEW: *"`T-TURN-10`, written this revision, unblocked and asserting
  — the code it gates does not exist yet, so it has not run and is not green"* —
  correct.
- tech Placement head: *"`T-TURN-10` is **written, unblocked and asserting, and
  not green**"* — correct.
- rules pair 5 NEW, on the parallel `GATE-CAP-PARTIAL` case: *"**It has not run,
  so T-CAP-05 is asserting and not green.**"* — correct, and it matches the
  master's own register text at line 2398: *"row 8 holds no code, so that gate
  has not run — it asserts, and it is not green."*

No passage calls `T-TURN-10` unwritten, blocked, or pending a ruling.

**The green count does not move.** Pair 6's NEW reads *"**49** of the 70 are
green"* against the OLD's *"**49** of the 69 are green"* — 49 unchanged. `49`
occurs at exactly two master sites (1487 and 1558) and both are inside pairs
whose NEW preserves it. Arithmetic closes: 1 + 3 + 1 + 16 = 21, and 49 + 21 = 70.

### 5. Locators that were checked rather than trusted

Given three locator errors this session, every citable locator in either
Grounding was run:

- rules Grounding cites `Driver.good.cpp` lines 552–554, 557, 569 and
  `Economy.good.cpp` lines 157, 169. **All five verified in the binding unit.**
  The driver comment at 552–554 reads *"the tick runs AFTER income, so an
  objective whose capture completes at the start of turn T pays its new owner
  from T+1"*; `accrueIncome` is called at 557 and `captureTick` at 569;
  `fresh.turnsHeld = 1` is at 157 and `if (prog->turnsHeld >= s.captureTurns)`
  at 169. The flip-counted reading in pair 6 is correct.
- rules' §2.1 claim — *"A grep for `at most once|acts once|acted this turn|once
  per own turn|move or act` across the whole document returns a single hit"* —
  **verified: one hit, line 1758, §4.7's `T-TURN-01` line.** Writing no pair for
  §2.1 is right; §2.1's pseudocode at lines 126–127 already states C2.
- rules' §2.8 range claim — *"Within §2 the only site carrying a `T-TURN-` range
  is this one"* — **verified**: `T-TURN-\d+\.\.\d+` returns 354 (§2.8), 1487,
  1496, 1504, 1558, 1781, 2705. Line 354 is the only one inside §2.
- I8's cross-file assumption re-run from scratch: pair 11's anchor
  `T-TURN-09  determinism` is at line 1778, and the enclosing fence opens at
  line 1752 with `SPEC STUB 5: Turn loop & win / tiebreak`. **`T-TURN-10` lands
  in Stub 5**, so rules pair 2's `..10` range change is correct.
- tech Grounding's quotes from Q8(b) and Q8(c) verified verbatim at line 2420;
  §2.7's *"**One build per factory per turn**, for the player and the AI alike
  (§2.9)"* verified at line 233; §3's row-4 clause *"never advances a turn and
  never decides whose turn it is, taking the turn number as an argument, which
  is why it could land before row 5"* verified on line 1487; §4.7's register
  quote verified at 2398–2399.
- tech's claim that §4.5's *"**9** at `ad77b13`, where T-TURN-01..09 closed row
  5"* sits between pairs 6 and 7 — **verified**, it is inside the per-commit
  green list that separates the two OLDs, and no pair reaches it.

### 6. Cross-file semantic consistency

The two files describe the same three rulings from different sections. Checked
pair against pair:

- **Per-turn limit.** rules pair 1 (*"the per-turn limit binds for the rest of
  that turn either way"*) and tech pair 11 (*"BOTH dispositions of the first
  build count against the allowance"*) state the same rule. tech pair 8 removes
  the clause from `T-FAME-04` and says where it went; rules leaves §2.7's own
  line 233 rule sentence untouched, which is correct — the rule stays, only the
  ID's coverage moves.
- **Suite range.** rules pair 2 (`gates within T-TURN-01..10`) and tech pairs 12
  and 13 (`T-TURN-01..10`) agree. tech's handoff quotes §2.8's OLD without
  dictating a NEW, so `gates as` → `gates within` is rules' call and does not
  cross a lane.
- **Alias map.** tech's handoff states *"The alias map's eight rows need no new
  row"*; rules changes an existing row and adds none. Agreed.
- **`T-CAP-05`.** rules pairs 4 and 5 agree with the master's own three
  statements of the same fact — lines 2333, 2396–2398, 2426 — and keep *"No
  `T-TURN-` ID asserts it"*, which is what those sites say.
- **Lanes.** No pair in either file lands in the other's sections. §3 pairs are
  scoped to the five sentences I5 widened scope to; no ledger table row is
  touched, and no pair flips, unflips, or re-opens row 5 (C7 satisfied).

### 7. `kb_rules.md`

rules discloses the drift: *"§2.7, §2.8 and §2.13.3 change here, so the parse of
§2 drifts on merge (F)."* Confirmed live — `kb_rules.md` line 66 carries *"hex;
if the factory is boxed in, the build waits. **One build per factory per*",
which is the §2.7 bullet rules pair 1 edits. No `kb-desync`.

tech needs no such note: `kb_rules.md` contains no `T-TURN-`, `T-CAP-`,
`T-FAME-`, no acceptance range and no ID count, so nothing tech writes reaches
it. Verified by grep, not assumed.

### 8. Items correctly left open — not filed

I6, I7, J7 and K3 were checked and none is a gap. Specifically: tech's four
Director questions, the Stub 8 second-flag change request, the `per-unit act
flags` §3 phrase, the `T-FAME-04` handoff, rules' two §2.13.3 tuning change
requests, and rules' Open Question 1 on the alias caption's singular. K3's
row-level vs ID-level filing is correct and is not counted against the file.

---

## Highest-risk remaining phrases across both files

Zero violations does not mean zero exposure. Ranked, most likely to become a
filed violation first.

**R1 — TECH / §3 line 1504. The K3 residual has a third site that neither file
names.** K3 pairs §4.5 with §3's `evidence rather than schedule` sentence, and
tech Open Question 4 names §4.11's preamble and §4.5. Neither names §3's *other*
row-5 sentence on line 1504:

> **Turn loop & win / tiebreak** joined at `ad77b13` — T-TURN-01..09, **9/9
> under clang++ and MSVC both** — and it leaves **no ID uncovered** either: no
> in-editor half and no reserved ID, so its full acceptance set closes at one
> commit and Q29 is satisfied rather than blocking.

and the tally two sentences later in the same paragraph:

> Six IDs are still recorded as **uncovered** rather than omitted, in **two
> states that are not the same state**. … Four are **written and not green**:
> **T-DATA-05** … and **T-SCN-08**, **T-SCN-09** and **T-SCN-11**.

After pair 13 makes row 5's acceptance set `T-TURN-01..10` and pair 7 lists
`T-TURN-10` among the unclosed, `T-TURN-10` is a candidate seventh uncovered ID
and a fifth written-and-not-green ID, and row 5 no longer plainly "leaves no ID
uncovered". This is not filed — F puts §3 out of scope and C7 reserves row 5's
status for the rebuild addendum — but it is a bare count, and a bare count goes
stale silently. **The rebuild addendum's site list must carry line 1504's
sentence and its `Six` / `Four` tally, not only §4.5 and §4.11's preamble.**

**R2 — TECH / the deictic in `at this landing`, ×5 on line 1487.** Each of the
five sentences means *its own* commit — 9f87ecd, 647d4df, ad77b13, d8284f1,
9086d6a — and each sits beside that commit's hash, so context carries it today.
Read instead as "at this revision" the sentence is false, because the written-ID
count **does** move at this revision, 69 → 70. The harmonisation is right and
the phrase is defensible; the risk is that it is now five identical deictics
whose referent lives outside the clause. Related: after merge `written-ID count`
occurs six times (five new plus Q32 at line 2444), so the next author grepping
that phrase gets a class that mixes two meanings. **Anchor on the green-count
delta, never on the phrase.**

**R3 — TECH / the pair-7 classification note quotes a token that does not
exist.** The note reads *"its NEW carries `**21 IDs remain unclosed**` where its
OLD carries `**20**`"*. The OLD carries `**20 IDs remain unclosed**`; the bare
string `**20**` appears nowhere in that OLD, and it **does** appear elsewhere in
the master — line 2419, Q7: *"*Ferrum Crossing* ships **20** turns"*. The
conclusion is correct and I re-derived it independently, but the token named is
not the token that carries the test, and it collides with an unrelated site.
This is exactly the K5 shape — a locator written as a detail rather than as a
claim. **Quote `**20 IDs remain unclosed**` in full.**

**R4 — RULES / `one row names a gate outside the `T-TURN-` numbering`** (pairs 2
and 3). True of the *Aliases to* column, which is the scope the caption itself
sets — *"The map below names, for each invariant, the ID or IDs that gate it"*.
But the `T-CAP-03` row's Why cell names **T-FAME-01** as what gates one half of
that invariant, so a reader counting rows that mention a non-`T-TURN-` gate
reaches two, not one. The OLD (*"one row names none"*) did not expose this,
because an empty cell is unmistakably a cell-level claim while "names a gate" is
not. Open Question 1 flags the singular's fragility against a *future* second
`GATE-` row; it does not flag `T-CAP-03`.

**R5 — RULES / a gate written into a column headed `Aliases to`.** Pair 4 puts
`**GATE-CAP-PARTIAL**` in that column while §4.7's Q6 cell, line 2418, reads:
*"T-CAP-05 aliases onto no `T-TURN-` ID (§2.8), so it has a gate of its own
**rather than an alias**."* The cell's own text (*"not a `T-TURN-` ID; see
below"*) and the rewritten caption stop the draft short of asserting an alias,
and D3 explicitly hands the column question to the Director as a §2.8 formatting
call — so this is within the grant. It is named because the **header word** is
the one thing in that table no pair touches, and it is the word Q6 uses to say
the opposite.

**R6 — RULES / two live senses of "turn" inside one disambiguating sentence.**
Pair 6's exclusion clause reads *"and not the next turn in the I-GO-U-GO
alternation (§2.1), which is the opponent's."* That is true under §2.1, which
the clause cites and whose pseudocode labels `Player turn:` and `Opponent turn:`
as separate turns. But §3 line 1487 records the documented choice that *"a turn
is one full I-GO-U-GO round shared by both sides"*, under which turn T+1 belongs
to both sides and is not "the opponent's". The main clause is safe because it
says *"the capturing side's own turns"*; the exclusion clause carries no such
qualifier. A sentence whose whole job is to remove an off-by-one should not lean
on the document's most overloaded noun unqualified.

**R7 — the one seam stated in two vocabularies.** tech pair 11's *"The allowance
renews at the start of the owner's turn"* and rules pair 1's *"the per-turn
limit binds for the rest of that turn"* are the same rule in different words,
and they diverge only when a factory changes hands mid-round — tech Open
Question 2, ruled correctly open at J7. Named only because neither file's merged
text signals that the other exists, so a reader of §2.7 alone and a reader of
Stub 5 alone will not know they are reading one rule.

---

## Verdict

**PASS**, both files, zero violations. Every OLD anchor resolves to exactly one
site in `source/gdd.md` at md5 `ca397f4f2eca447b451fca2ca2393092`; the 19 pairs
are 17 replacements and 2 insertions; there are no cross-file overlaps and no
placement collision; the two files agree with each other on all three rulings
and with the master on every figure they carry. The two round-3 fixes hold:
TECH pair 7's restored conclusion clause is byte-identical on both sides and the
pair remains a replacement, re-derived here on the current bytes rather than
taken from the author's or the orchestrator's report; RULES' false enumeration
is gone by deletion with no replacement locator, and the deletion's extension to
the sibling enumeration and the Handoffs count leaves nothing behind that
asserts a line number. **Nothing must happen before merge.** Two things must
happen at merge and just after it: re-sync `kb/rules.md`, since §2.7, §2.8 and
§2.13.3 all move and §2 has been byte-identical across every merge since row 5;
and carry R1 — §3 line 1504's *"leaves no ID uncovered"* sentence and its
`Six` / `Four` tally — into the rebuild addendum's site list alongside §4.5 and
§4.11's preamble, because those counts are the only row-5 statements in the
document that no open question currently names.
