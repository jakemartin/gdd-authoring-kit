# Gate report — run `row8-rulings-7`

Master: `source/gdd.md` @ md5 `a5c266b921ea3ea7a3ce79c89137cc66`
(`source/MANIFEST.txt` present; `kb_rules.md` @ `024523449be1873c9d545dbea6d3bc9d`,
`kb_setting.md` @ `b3e9e89daaef1cdeb333e3fb4368d1c0`.)

**Top-level verdict: PASS.** Both sections pass; zero violations.

| Section | Verdict | Violations |
|---|---|---|
| `sections/ux_row8-rulings-view-model.md` | **PASS** | 0 |
| `sections/tech_row8-rulings-snapshot-hash.md` | **PASS** | 0 |

---

## `sections/ux_row8-rulings-view-model.md` — PASS

No violations. Re-checked whole, not exempted for having passed in runs 5 and 6.

All five pairs are §2.11-internal (Pairs 1 and 5 on §2.11.1 and §2.11.5, Pairs
2–4 on §2.11.2), each OLD present once in the master and each NEW consistent
with the rest of §2.11 and with §4.7 Stub 8 as the tech addendum rewrites it.
The two files agree on vocabulary (**view-model**, **presentation block**,
**declared derived**) and on the per-factory block's membership
`{hex, owner, hasBuiltThisTurn, buildWaiting, spawnBlocked}`, stated identically
in UX Pair 5 and tech Pair 9. Pair 4's `incomePerTurn` and Pair 5's
`hasBuiltThisTurn` / `spawnBlocked` are fields tech Pair 9 adds in the same
stage, and the draft files their absence at `7c36303` under "Filed for the
Director" (three fields, matching what Pairs 4 and 5 name) rather than claiming
any of them implemented. §2.11.4's Objectives row, §2.11.2's three-layer list
and §2.11.6-D are correctly left unpaired: none is falsified by Rulings A, C
or E.

## `sections/tech_row8-rulings-snapshot-hash.md` — PASS

No violations. All 22 pairs, the §4.5 arithmetic, the deletions and the
re-anchored Grounding were checked.

**The two run-6 defects are gone and no substitute was introduced.** Pair 6a's
NEW now reads "the presentation block and the snapshot fields ruled beside
T-UI-05 on the same day, which mint no ID at all" — no count, and the phrase
covers all four fields Rulings C and E add, `spawnBlocked` included, without
excluding any. The `hpMax` inference and the §4.10 per-unit-record bullet it
hung on are gone from Grounding; `hpMax` and `unitId` are now grounded on
§4.8's unit schema, which carries them (`HP` → `strat::UnitDef::hpMax`, `Id`
as the row key), and no surviving Grounding bullet claims more than its
citation carries.

**The deletions cut nothing load-bearing.** Every one of the 22 pairs still
carries prose saying what it does and why, sufficient for a Director to rule
on it: the insertion/replacement kind is named where it matters (Pairs 2, 8,
8b, 9, 10, 11), the single-line constraint is stated where a table cell or an
unwrapped paragraph requires it (Pairs 1, 2b, 3, 6a, 6b, 18), and each pair
names the ruling it executes. The two items called load-bearing survive: Pair
8b's grouped field enumeration is intact and complete — 17 `GameState` mirrors,
2 §4.8-table mirrors, 3 scenario-file mirrors, 4 declared derived, which is
exactly the 26 fields Stub 8 lists once Pairs 9 and 8b land — and §4.5's
itemisation is intact. Surviving prose was checked for truth, including the
sites the deletions left adjacent: "Checked, and needing no pair" now carries
the both-spellings grep result, and that result is correct — `view model` /
`view-model` occurs at exactly four sites in the master (§3's driver sentence,
Stub 8's Scope, §4.9's rebind bullet, T-INT-05), and all four are paired
(2b, 7, 14, 15).

**Arithmetic and counts.** 70 → **71** written, **52** green, 18 → **19**
unclosed, 16 → **17** in rows 8–10 (row 8 `T-UI-01..05` = 5, row 9
`T-INT-01..05` = 5, row 10 `T-SAVE-01..07` = 7), **9** verified ledger rows —
all consistent with §4.5's risk row, §4.11's rows 8–10 and §3 as they stand.
The unclosed itemisation sums (1 + 3 + 2 + 1 + 12 = 19), §3's uncovered count
moves 8 → 9 as 2 unwritten + 7 written-and-not-green, and Pair 4's NEW
enumerates exactly those seven. `T-UI-05` is the only ID minted; the
presentation block, the per-factory block, `incomePerTurn` and `spawnBlocked`
mint none, and no pair says otherwise. §3's commit-scoped records — "its
unclosed count moves 20 → 18" at `7c36303`, "21 → 20" at `6ccd40b` — are
records of movement at a landing and stay true unpaired.

**Ruling D's hash.** Pair 16's added fields are integers written 0 or 1, the
per-factory collection is in the same canonical hex order the per-unit list
uses, and `spawnBlocked`'s exclusion is written as recomputability from hashed
fields — which holds: unit positions are hashed and terrain is fixed by the
scenario file whose `scenarioHash` is a header field in §4.10's own table. The
narrower test is required, and the draft says so: §4.10's *Mid-match saves*
bullet calls a waiting build and capture-in-progress derived pending state and
both are hashed, so a rule phrased as "derived" would have contradicted the
Policies list. §4.4's week-2 cell survives on the same reading, and its
`{Move, Attack}` scope reaches both added per-unit flags.

**Nothing is claimed built.** Pairs 2, 3, 4, 5, 6a, 6b, 13 and 17 each state
that no code implements `T-UI-05`, the per-factory block, `incomePerTurn`,
`spawnBlocked` or the widened hash; row 8's ledger row stays `*pending*` and
no §3 count of verified rows moves. Every commit named is `7c36303`,
`6ccd40b`, `9086d6a`, `c224825` or `d8284f1`, each already in §3.

**Placement and lanes.** The UX addendum touches §2.11 only, the tech addendum
§3 and §4 only; the two file their cross-lane observations rather than pairing
them, and no OLD anchor is shared between the files. Every placement is an
exact OLD/NEW pair and merges mechanically. `kb_rules.md` is a parse of §2's
rules and carries no §2.11 binding text and no acceptance-ID count; neither
addendum changes a §2 rule, so nothing here staleness-breaks it and no
kb-desync declaration was owed.

**The one open tension is filed, not created.** §4.7 Stub 7's `guidedOpening`
note keeps the marked/locked state out of Stub 8, while Pair 15 widens
T-INT-05's subject to the whole view-model. Pair 15's OLD already carried the
same gap ("from the current view-model snapshot alone"), the note is left
unedited and unpaired, and the addendum files the disposition as a change
request naming three options and taking none. That is the correct handling.

---

## Verdict

**PASS.** This run is clean: both files carry zero violations, and the two
defects run 6 filed — Pair 6a's stale count and the `hpMax` inference — are
repaired without regression anywhere else in either file. The structural
deletion pass removed prose without removing explanation: every pair remains
rulable on its own framing, both passages the author flagged as load-bearing
survive intact, and the surviving non-pair prose is true against the master.
Nothing further must happen before merge: the Director may merge both drafts
at the placements their OLD/NEW pairs specify, then rebuild the derived files,
re-sync `kb/rules.md`, update the §3 provenance ledger's row-8 evidence cell
per Pair 3 — row 8 stays `*pending*` — and re-run `python sync.py`.
