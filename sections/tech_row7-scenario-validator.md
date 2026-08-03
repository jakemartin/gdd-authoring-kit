> ## ✅ APPLIED ADDENDUM — DO NOT RE-APPLY
>
> All thirteen pairs were merged into the master GDD on 2026-08-03.
> Master md5 `f456445d516e75e5e31a5b749157bfd2` →
> `ca397f4f2eca447b451fca2ca2393092`.
>
> Gate: run `row7-3`, **PASS**, 0 violations, after `row7-1` (BLOCK, 2 — a
> stale §4.11 preamble clause still reading "row 7 has not" landed, and three
> missing file sections, the latter caused by the orchestrator's kickoff brief)
> and `row7-2` (BLOCK, 5 — all five in text the previous round had written: a
> §2.13.7 condition restated in §3, a "shipped map supplies" gloss false of
> T-SCN-08's synthetic fixture (c), and two overreaching claims in the new Q32
> cell). All five were fixed by **deletion**, none by substitution.
>
> **Pairs 3 and 10 are insertions — their OLD anchors are retained
> deliberately.** Each NEW block opens with its OLD anchor verbatim and appends
> after it. Post-check on the merged master: every NEW present exactly once;
> pairs 3 and 10's OLDs present **once** each, the other eleven **zero** times.
> This file is **not safe to apply twice**.
>
> Pairs 7 and 13 land in the same §4.5 cell. Their anchors were located in the
> master and their spans compared programmatically: **disjoint**, ~160
> characters apart.
>
> `kb/rules.md` was **not** re-synced. §2 is byte-identical across this merge
> (98,195 chars both sides, compared as strings); no pair touches §2.
>
> Row 7's ledger row **does not flip** — it records a partial pass, the posture
> row 2 holds on T-DATA-05.

# Technical design — row 7 built, partial pass (tech-director)

## Placement

Thirteen pairs — **eleven replacements, two insertions**, classified by
substring test over the blocks as they now stand: an insertion's NEW block
contains its OLD anchor verbatim and contiguously, so the anchor survives the
merge by design. The two insertions are **Pair 3** and **Pair 10**; the other
eleven are replacements, and their OLD text should be absent from the master
afterwards.

Seven pairs are in **§3**: three in the italic *Status: live tracker* line, one
in the ledger table, three in the populated-rows paragraph. Two are in
**§4.5**'s *Specification outruns the build* row — Pair 13 on its date stamp and
Pair 7 on its arithmetic, whose anchors are disjoint spans of that one cell with
untouched text between them. Three are in **§4.7**'s register: the provenance
chain, the preamble count, and the new `Q32` row. One is in **§4.11**'s
preamble.

Pair 3's closing italic `*` is deliberately **outside** both blocks, so the
italic boundary of the tracker line is untouched.

---

## Pair 1 — §3 status line, the head commit (replacement)

**OLD**
```
This draft stands at 2026-08-02, at commit [`d8284f1`](https://github.com/jakemartin/stratocracy-crew/commit/d8284f1) — the head of `main` in the crew repo, whose parent is [`2381ca0`](https://github.com/jakemartin/stratocracy-crew/commit/2381ca0).
```
**NEW**
```
This draft stands at 2026-08-03, at commit [`9086d6a`](https://github.com/jakemartin/stratocracy-crew/commit/9086d6a) in the crew repo, whose parent is [`d8284f1`](https://github.com/jakemartin/stratocracy-crew/commit/d8284f1).
```

## Pair 2 — §3 status line, row 8's other dependency (replacement)

**OLD**
```
and row 8's other dependency is **row 7**, which holds no code.
```
**NEW**
```
and row 8's other dependency is **row 7**, which has since landed at [`9086d6a`](https://github.com/jakemartin/stratocracy-crew/commit/9086d6a) on a partial pass, recorded at the end of this paragraph.
```

## Pair 3 — §3 status line, its tail: row 7's record (insertion)

The row-6 sentence that ends the paragraph today is bound to `d8284f1`'s census
of ten and stays true there, so it is kept and row 7's record is added after it.

**OLD**
```
No scenario harness and no UI harness is among the ten `main()` definitions above.
```
**NEW**
```
No scenario harness and no UI harness is among the ten `main()` definitions above. **Row 7 then landed**, at [`9086d6a`](https://github.com/jakemartin/stratocracy-crew/commit/9086d6a): **Scenario file & validator**, gated **12/12 under clang++ and MSVC both** — `g++` is not installed on this machine — while its pass-1 implementation `cpp_reference/Scenario.buggy.cpp` is blocked at 11/12, on T-SCN-11 alone, under both compilers: it minimised the opposing route over the opposing seat's `guidedOpening.infantry` alone rather than over every CanCapture-row unit that seat deploys, which is reading (b) at Q28 and the one that ruling refused. Six tracked sources are cited, each probed present at that commit: `spec/scenario_spec.md`, `cpp_reference/Scenario.h`, `cpp_reference/Scenario.good.cpp`, `cpp_reference/Scenario.buggy.cpp`, `cpp_reference/test_scenario.cpp`, `data/ferrum_crossing.json`. The fifth of those is a ninth harness, so **eleven** tracked sources define `main()` at [`9086d6a`](https://github.com/jakemartin/stratocracy-crew/commit/9086d6a) — the ten named above plus `cpp_reference/test_scenario.cpp` — nine test harnesses, one combat duel simulator, and one debug REPL. **This row does not flip.** Q29 requires the full acceptance set at one commit, and it is applied **per acceptance ID as well as per row** — an ID closes only when its whole written fixture set has run. Of the twelve checks that passed, **T-SCN-01..07 ran in full and close**; `GATE-SCN-PARSE` and `GATE-SCN-HASH` gate a file format rather than a §4.7 stub and mint no numbered acceptance ID, on the `GATE-AI-SMOKE` precedent; and **T-SCN-08, T-SCN-09 and T-SCN-11 ran a part of their fixture sets and do not close** — T-SCN-08 on fixture (c) plus its measure-and-report behaviour on the shipped map, T-SCN-09 on its refusal branch, T-SCN-11 on fixtures (a) and (b), (b) being a required failure. So the row records a partial pass and stays unverified, which is the posture row 2 holds on T-DATA-05. **No new acceptance ID was written**, so §4.5's 69 stands and its green count moves 42 → 49. **Four fixtures did not run, and each is named rather than absorbed** — each printed by name with its reason before the tally and recorded in the acceptance record: T-SCN-08 (a) *The Causeway* and (b) *Longwater March*; T-SCN-09's asserting branch; T-SCN-11 (c) *The Causeway*. Each needs a stretch map authored as a scenario file, and **none was replaced by a synthetic map**. Those three IDs are **written, unblocked and asserting**; what they lack is a map to run against, not a rule. **T-SCN-10 is a different state and is not one of them:** it is reserved and **unwritten** on Q26, so no invariant text exists for it, nothing asserts and nothing waits. **The shipped scenario file is a transcription, not an authoring**: all 99 terrain hexes of `data/ferrum_crossing.json` were diffed against §2.13.2's grid, zero mismatches, and the distribution is the one §2.13.2 states. **A change request out of the build is registered rather than acted on**: §2.13.1's validation-invariants bullet names three checks no `T-SCN-` ID asserts as written, and the build implemented T-SCN-02 and T-SCN-04 to their exact written text rather than widening them — registered as **Q32**, with no invariant text changed and no acceptance ID minted. The debug driver's suite is now **GATE-DRV-01..11, 11/11 under clang++ and MSVC both**, `GATE-DRV-11` being new at this commit, and those IDs are still **not** `T-*`: the driver is not a §4.7 stub, has no row in the ledger below, and flips nothing. A **Claude Code session** authored row 7 from the Director-written stub `spec/scenario_spec.md`, **not a live CrewAI run**. **Row 7 is not on §4.11's critical path**: it was built because row 8 queues behind it and its own dependencies had landed. No UI harness is among the eleven `main()` definitions above.
```

## Pair 4 — §3 ledger table, the scenario row (replacement)

Formatted on the **Data tables** row, the table's other partial pass, and not on
a flipped row.

**OLD**
```
| Content / scenario | *pending* | — | *pending build* |
```
**NEW**
```
| Content / scenario | agent | — | **Partial pass — not a flip.** `cpp_reference/Scenario.good.cpp` + `cpp_reference/test_scenario.cpp` over `data/ferrum_crossing.json` @ [`9086d6a`](https://github.com/jakemartin/stratocracy-crew/commit/9086d6a) · T-SCN-01..07 (7/7) headless, plus `GATE-SCN-PARSE` and `GATE-SCN-HASH`, which mint no acceptance ID. **T-SCN-08, T-SCN-09 and T-SCN-11 ran only part of their fixture sets** — the four fixtures that did not run each need a stretch map authored as a scenario file — so the acceptance set is incomplete at this commit and Q29, read per ID, keeps the row unverified |
```

## Pair 5 — §3 populated-rows paragraph, the count (replacement)

**OLD**
```
**Nine rows carry a ✓ in the table above, and a tenth carries evidence without one.**
```
**NEW**
```
**Nine rows carry a ✓ in the table above, and two more carry evidence without one.**
```

## Pair 6 — §3 populated-rows paragraph, the uncovered IDs (replacement)

**OLD**
```
Two IDs are still recorded as **uncovered** rather than omitted: **T-DATA-05**, the in-editor Unreal Automation half, and **T-MOVE-07**, reserved and unwritten on Q2. The first is why **Data tables** is the tenth row and does *not* flip — T-DATA-01..04 and 06 are green at the same commit, but Q29 requires the full acceptance set at one commit, so that row records a partial pass and stays unverified.
```
**NEW**
```
Six IDs are still recorded as **uncovered** rather than omitted, in **two states that are not the same state**. Two are **unwritten**: **T-MOVE-07**, reserved on Q2, and **T-SCN-10**, reserved on Q26 — no invariant text exists for either, so neither asserts and neither is waiting on a run. Four are **written and not green**: **T-DATA-05**, the in-editor Unreal Automation half, which has not run; and **T-SCN-08**, **T-SCN-09** and **T-SCN-11**, each written, unblocked and asserting, each having run only part of its fixture set. T-DATA-05 is why **Data tables** carries evidence without a ✓ — T-DATA-01..04 and 06 are green at the same commit, but Q29 requires the full acceptance set at one commit, so that row records a partial pass and stays unverified — and the three `T-SCN-` IDs are why **Content / scenario** does the same at [`9086d6a`](https://github.com/jakemartin/stratocracy-crew/commit/9086d6a), Q29 there being read per ID.
```

## Pair 7 — §4.5, the risk row's arithmetic (replacement)

**OLD**
```
and **42** of the 69 are green: **18** at `c224825`, where rows 1 and 3 closed their full acceptance sets and row 2's headless half passed, **9** at `647d4df`, where T-FAME-01..09 closed row 4, **9** at `ad77b13`, where T-TURN-01..09 closed row 5, and **6** at `d8284f1`, where T-AI-01..06 closed row 6 — so everything on the critical path but row 8 is evidence rather than schedule. **27 IDs remain unclosed**: T-DATA-05, which leaves row 2 unflipped, plus the 26 in rows 7–10, which hold no code
```
**NEW**
```
and **49** of the 69 are green: **18** at `c224825`, where rows 1 and 3 closed their full acceptance sets and row 2's headless half passed, **9** at `647d4df`, where T-FAME-01..09 closed row 4, **9** at `ad77b13`, where T-TURN-01..09 closed row 5, **6** at `d8284f1`, where T-AI-01..06 closed row 6, and **7** at [`9086d6a`](https://github.com/jakemartin/stratocracy-crew/commit/9086d6a), where T-SCN-01..07 closed without closing row 7 — so everything on the critical path but row 8 is evidence rather than schedule. **20 IDs remain unclosed**: T-DATA-05, which leaves row 2 unflipped; T-SCN-08, T-SCN-09 and T-SCN-11, which are written, unblocked and asserting, but ran only part of their fixture sets, and which leave row 7 unflipped; and the **16** in rows 8–10, which hold no code
```

## Pair 8 — §4.7 register, the provenance chain (replacement)

**OLD**
```
commitment ruling exposed against §2.11.5's Build-button rule (Q31)
— so that each question
```
**NEW**
```
commitment ruling exposed against §2.11.5's Build-button rule (Q31), and the
three §2.13.1 validation checks row 7 found gated under no `T-SCN-` ID (Q32)
— so that each question
```

## Pair 9 — §4.7 register, the preamble count (replacement)

**OLD**
```
**Fifteen of the thirty-one rows are ruled; the other
sixteen remain open but *readable*** — Q1, Q2, Q3, Q10–Q19, Q29, Q30 and the
newly registered Q31 — each
```
**NEW**
```
**Fifteen of the thirty-two rows are ruled; the other
seventeen remain open but *readable*** — Q1, Q2, Q3, Q10–Q19, Q29, Q30, Q31
and the newly registered Q32 — each
```

## Pair 10 — §4.7 register table, the Q32 row (insertion)

Anchored on the tail of the Q31 row, which is the table's last row; the new row
follows it.

**OLD**
```
Registered rather than assumed because Q8(c) ruled on a state the UI makes unreachable — the ruling stands, its player-facing half is simply not exercised yet. |
```
**NEW**
```
Registered rather than assumed because Q8(c) ruled on a state the UI makes unreachable — the ruling stands, its player-facing half is simply not exercised yet. |
| **Q32** | Three §2.13.1 validation checks that no `T-SCN-` ID asserts. §2.13.1's validation-invariants bullet names *every land-passable hex reaches every factory*, *all deployment hexes are free and land-passable*, and *factory count in the map file equals the count the domination check uses*, for the §4.2 `validate_scenario` tool whose schema is Stub 7's. Building row 7 against that stub found no `T-SCN-` ID that gates any of the three as written. Widen an existing invariant, mint IDs for the three checks, or accept that the tool description is wider than the gated suite? | Nothing today: no `T-SCN-` ID gates the three, so no gate waits on the ruling. A ruling that mints an ID for one of the checks would move §4.5's written-ID count | **The invariants ship as written.** Row 7 implemented T-SCN-02 and T-SCN-04 to their exact written text at [`9086d6a`](https://github.com/jakemartin/stratocracy-crew/commit/9086d6a) rather than widening them, and minted no ID for the three checks, so the bullet describes more than the suite gates. |
```

## Pair 11 — §3 populated-rows paragraph, the lineage parenthetical (replacement)

The head-of-`main` claim here is Pair 1's twin and goes false on the same merge.
Quantified rather than enumerated, so a landing row extends nothing. The
sentences after it, about file paths and bare citations, are outside both
blocks.

**OLD**
```
*(Commit `d8284f1` is the head of `main`; its parent is [`2381ca0`](https://github.com/jakemartin/stratocracy-crew/commit/2381ca0), so `5ffa8d6`, `c224825`, `9f87ecd`, `647d4df`, `caa8267`, `ad77b13` and `2381ca0` all remain ancestors and every commit link above resolves.
```
**NEW**
```
*(Every commit this section cites — `d8284f1`, row 6's, included — is reachable from the head of `main` in the crew repo, so every commit link above resolves.
```

## Pair 12 — §4.11 preamble, the clause that says row 7 has not landed (replacement)

Anchored on the trailing clause alone. The bolded green list two lines above it
is **outside both blocks and unchanged**: row 7 landed and is not green, so
adding it to a list of green rows would merge the two states this addendum
exists to keep apart. Wrapped to the section's ~75 columns.

**OLD**
```
its dependency cell in the table below reading `5, 7` — row 5 has landed and
row 7 has not.
```
**NEW**
```
its dependency cell in the table below reading `5, 7` — both have landed,
row 7 on a partial pass that leaves its ledger row unflipped (§3).
```

## Pair 13 — §4.5, the risk row's date stamp (replacement)

The stamp sits before Pair 7's anchor in the same cell, separated by the
`c224825` / GATE-AI-SMOKE clause that neither pair touches. Only the date moves;
*Reduced and re-scoped* and *not retired* are true of this landing as they were
of the last.

**OLD**
```
**Reduced and re-scoped at 2026-08-02, not retired:**
```
**NEW**
```
**Reduced and re-scoped at 2026-08-03, not retired:**
```

---

## Grounding

Every OLD block was grepped against `source/gdd.md` (md5
`f456445d516e75e5e31a5b749157bfd2`) as an exact string, including its line
breaks where it spans lines: **each matched exactly once**. Pair 13's was
grepped when it was written; no other OLD block's bytes changed in this round.
Pair 13's anchor ends at `not retired:**` and Pair 7's begins at `and **42** of
the 69 are green`, so the two spans in that cell are disjoint.

Eight `9086d6a` citations are linked — Pairs 1, 2, 4, 6, 7 and 10 once each and
Pair 3 twice — and the link shape is copied from the `d8284f1` and `ad77b13`
links already in §3 rather than composed. Pairs 12 and 13 cite no commit,
matching the style around them.

Pair 11 rests on ancestry verified by command at `9086d6a` as it stands on the
remote: `9086d6a^` is `d8284f1`, and `5ffa8d6`, `c224825`, `9f87ecd`, `647d4df`,
`caa8267`, `ad77b13`, `2381ca0` and `d8284f1` are each an ancestor of `9086d6a`.
That is ancestry only, and no claim about any file's content at any commit.

Commit, source, `main()`-census, ID-count and gate facts — `9086d6a` and its
parent, the six tracked sources, the eleven `main()` definitions, 12/12 and the
11/12 pass-1 block on T-SCN-11, the twelve checks and the four fixtures that did
not run, the 99-hex transcription diff, `GATE-DRV-01..11`, and the 26 written
IDs behind rows 7–10 — are the standing fact block for this round (A1–A7,
B1–B9). The rulings the pairs execute are C1 (stretch maps unauthored), C2 (no
flip), C3 (per-ID counting), C4 (nothing written) and C5 (`Q32`, nothing else
moves).

The arithmetic in Pair 7 is re-derived rather than copied: 18 + 9 + 9 + 6 + 7 =
**49**; unclosed = T-DATA-05 (1) + T-SCN-08/09/11 (3) + rows 8–10 (**16**, being
T-UI-01..04, T-INT-01..05 and T-SAVE-01..07) = **20**; and 69 − 49 = 20.
Pair 9's counts are re-derived from the register table itself: 15 rows marked
RULED, and Q1, Q2, Q3, Q10–Q19, Q29, Q30, Q31 plus the new Q32 = **17** open,
totalling **32**.

`source/gdd.md` supplies the rest: the two extent-bearing sites the register
names for itself; Q26 for T-SCN-10's unwritten state; Q28 for the reading pass 1
took; Q29 for the flip criterion Pair 3 applies per ID; §2.13.1's
validation-invariants bullet for Q32's three quoted checks; and the **Data
tables** row for the partial-pass shape Pairs 4 and 6 follow.

## Open questions for the Director

- **The ledger row's label.** Pair 4 leaves the row named `Content / scenario`
  rather than renaming it to §4.11's *Scenario file & validator*. Renaming a
  ledger row changes an identifier other sites may lean on, so it is left to a
  ruling rather than taken.
- **How far the per-ID reading of Q29 reaches.** Pair 3 states it inside row 7's
  record, where the facts for it are in hand. It has **not** been audited
  against the IDs behind rows 1–6, and no pair claims it holds there. Whether it
  should be written into Q29's own register row as a general rule is a Director
  edit, not an author's.
- **Two shas leave the document — decisions taken, not questions.** Pair 1
  removes the last occurrence of `2381ca0` and Pair 11 the last occurrence of
  `caa8267`, each verified by grep against `source/gdd.md` before and after.
  Neither was cited as evidence: `2381ca0` appeared as row 6's parent and
  `caa8267` only inside the enumerated ancestor list, and row 5's cited commit
  is `ad77b13`. That list has gone stale on every landing, so Pair 11's
  quantifier replaces it.
- **The §4.5 date stamp will stale again.** Pair 13 moves it to 2026-08-03. A
  formulation that never stales was considered and not taken: the stamp's other
  words are load-bearing and a one-token edit is the smaller assertion.
- **Two present-tense sites this addendum does not touch, reported rather than
  folded in.** §3's tracker line carries `row 7 is unbuilt` inside row 5's
  record and `row 7 unbuilt` inside row 6's, each explaining a spec choice made
  at `ad77b13` and `d8284f1` respectively. They are commit-bound in the same way
  as the row-5 sentence Pair 3 deliberately keeps, and they precede row 7's own
  record in the paragraph. If they should be tensed instead, that is a
  fourteenth pair and I have not written it.

## Change requests

None. CR-1 is ruled and lands as the `Q32` register row in Pair 10, not as a
change request; no pair in this file proposes a change to a section outside
§3, §4.5, §4.7 and §4.11's preamble.
