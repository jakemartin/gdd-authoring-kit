# Continuity gate — run `row6-3`

`source/MANIFEST.txt` present (no `sync-missing`). `gdd.md` md5
`cc07e1f0db78b4955059933520194360`, unchanged from `row6-1` and `row6-2`. One
file gated: `sections/tech_row6-opponent-ai.md` (eleven OLD/NEW replacement
pairs) — and no other. `sections/rules_t-cap-alias.md` is sealed into that
snapshot and was not gated.

| File | Verdict | Violations |
|---|---|---|
| `sections/tech_row6-opponent-ai.md` | **PASS** | 0 |

**Top-level verdict: PASS.**

---

## `sections/tech_row6-opponent-ai.md`

**No violations.** The file is clean. What follows is the record of what was
checked, not a hedge against the verdict.

### The `row6-2` violation is closed

The false clause is gone. `driver's choice` and `so the sequence` both return
**zero** hits in the file, and nothing was substituted in that position — the
sentence now ends at the true narrow claim it was appended to:

> `spec/turn_spec.md` states neither the capture tick nor an order among the
> three calls.

That claim was ruled true in its own scope at `row6-2` and is unchanged.

### The one new assertion, weighed on its own

**Draft** (Change requests, third row, Why cell, final clause):

> The phrase "flips income the following turn" admits two readings — the turn
> following the hold, or the turn following the flip

**Source** — `source/gdd.md` §2.13.3, *Match-length reasoning* (line 1161):

> capture at N=1 (fixed from §2.7's "start N=1–2" range — Q4, §4.7) **flips
> income the following turn.**

Four things were checked and each holds.

1. **The locator resolves.** `flips income the following turn` occurs **exactly
   once** in `source/gdd.md`, at line 1161, and exactly once in the draft. A
   bare quoted phrase that matches uniquely is a locator, not a
   `dead-reference`; the author is not obliged to use the section number I
   named in the `row6-2` fix so long as the cell stops asserting the document
   is silent. It does stop.

2. **The two readings are fairly stated.** They are the same pair this gate
   itself set out at `row6-2` — "following the hold turn (turn 3 …) or …
   following the flip turn (turn 4 …)". Both are available from the sentence:
   its subject is "capture at N=1", and the ambiguity is whether *capture*
   denotes the hold or its completion. §2.13.7's worked case keeps both alive
   rather than closing either — "the Infantry stands on the factory at the end
   of turn 2 and the tile **flips on turn 3**" fixes the *tile* flip on turn 3
   and says nothing about whether the *income* flip is simultaneous with it or
   one turn behind it. Neither §2.7's capture bullet ("A captured objective
   flips its Fame income to the new owner.") nor §2.7's accrual bullet
   ("Income accrues **at the start of your turn and is spendable in that same
   turn's economy phase**") nor Stub 5's "start-of-turn repair application
   (§2.7)" orders the capture tick against income accrual. The claim of
   ambiguity is therefore true, and it is not an `invented-fact`: it asserts
   nothing about the game, only about a quoted phrase that is reproduced
   verbatim beside it.

3. **Stating it without resolving it is correct here, not incomplete.** A
   change request's job is to put the open question in front of the Director;
   picking a reading in the Why cell would be the author ruling a live
   question, which is the shape that blocked at `row6-1` and `row6-2`. The cell
   still states the driver's behaviour precisely — "an objective whose capture
   completes at the start of turn T pays its new owner from turn T+1" — so the
   Director has the build's answer, the document's phrase, and both readings of
   it, in one cell.

4. **The request is not asking for something already ruled.** "Rule the order
   of the three start-of-turn calls … and in particular whether the tick runs
   before or after income accrual" survives §2.13.3 under either reading:
   §2.13.3 constrains at most which turn income moves, never repair's position,
   and under one of its two readings does not constrain the tick at all.

### Everything else re-checked this run

- **Anchors.** All eleven OLD blocks were re-grepped against `source/gdd.md` at
  this md5 and each returns **exactly one** match — pairs 1, 2, 3, 4, 5, 6, 7,
  8, 9, 10 and 11 individually, not as a group. Pairs 1–3, 5–7 and 8–9 are
  disjoint spans of one source line each and apply in any order.
- **No `placement-collision`.** One file, eleven pairs, no overlapping target
  spans; the Placement table names an exact site for each.
- **Arithmetic unchanged and still correct.** §4.5: 18 + 9 + 9 + 6 = 42 green
  against a written total of 69, leaving 27 unclosed — T-DATA-05 plus 32 − 6 =
  26 across rows 7–10; verified ledger rows 8 → 9; nine ✓ rows and a tenth
  carrying evidence. §4.11 row 8's dependency cell reads `5, 7`, so pairs 2 and
  11 read it correctly.
- **No `kb-desync`.** No pair touches §2. `source/kb_rules.md` states the
  capture flip with no timing either ("a captured objective flips its income"),
  so the addendum makes nothing there wrong, and the change requests are
  proposals rather than changes.
- **No `stat-drift`.** Every number moved in prose is either derived from a
  flipping row (green count, unclosed count, ✓ count, ledger rows) or filed
  against a stated fact; no §2 value is retuned anywhere in the file.
- **No `unverified-claim`.** Row 6's claims are bound to `d8284f1` with named
  IDs (T-AI-01..06 plus GATE-AI-SMOKE, 7/7), and the pass-1 block is stated
  with its failing IDs.

### Standing rulings, untouched and not re-opened

`GATE-DRV-01..07` as written; the unruled voice of all three change-request
rows; the Grounding section not covering the change-request table (the preamble
carries the attribution); pair 3's surviving clause "the start of a turn now
runs repair, income and capture tick in that order"; and the absent `## Draft`
heading, the eleven pair blocks being the draft in the sealed-addendum shape.

---

## Verdict

**PASS.** The one violation filed at `row6-2` is closed by deletion with nothing
substituted, and the single new assertion added on top of that fix — that
"flips income the following turn" admits the turn following the hold or the turn
following the flip — is a true statement about a phrase that occurs exactly once
in `source/gdd.md`, stated without picking a reading, which is the correct form
for a question that is the Director's to settle. Nothing else in the file moved,
and the eleven anchors, the arithmetic and the placement table were re-verified
independently at this md5 rather than taken on report. Before merge, one
precondition still stands and it is not a gate finding: Fact M — `d8284f1` is
committed and **not pushed**, and pairs 1, 3, 4, 6, 8 and 11 either link it or
cite it while pair 7 keeps the document's existing claim that every commit link
above resolves, so the crew push must precede or accompany the merge. The
Director should also note the file's own open question — whether §4.11 row 6's
acceptance cell should name `GATE-AI-SMOKE` — which no pair touches.
