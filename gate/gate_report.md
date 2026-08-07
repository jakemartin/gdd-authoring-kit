# Gate report — run `t-data-05-harness-6`

Master: `source/gdd.md`, md5 `46d05e398f5df9d6aefae5eab017a51e` (per `source/MANIFEST.txt`).
Snapshot present; the run reads current material.

**Top-level verdict: PASS.**

## sections/tech_t-data-05-harness.md — PASS (0 violations)

Nothing is filed. What was checked, and why each check clears.

### 1. Pair 24's amended NEW against its unchanged OLD

OLD is the tail of the Q33 register row, which occurs once in `source/gdd.md` at
§4.7 (line 2658):

> `the register carries it so the amendment above has a stated cause rather than an unexplained rewrite. |`

NEW reproduces that string verbatim and appends one new table row beginning
`| **Q34** |`, so the edit is an insertion immediately after Q33 and inside the
§4.7 register table, which is where a new register row belongs. The row carries
the four columns the table uses (question, dependencies, ruling) in the same
order as Q33 and Q29, and it is marked `**RULED (this revision), and registered
already ruled.**` on Q33's stated precedent — Q33's own row ends "It is
registered already marked RULED because the Director ruled it in the session
that found it", and Q34 closes with the same clause.

Q34's premise checks against Q29 as written (§4.7, line 2654): Q29 requires "a
row flips only when its **full** acceptance set passes over the **complete**
§4.9 command set at one commit", so Q34's "no single commit in either repo can
carry both halves and Q29's condition is unsatisfiable read literally" states
Q29's condition rather than restating it loosely.

### 2. Ruling AN and Open question 1 — the run-5 contradiction is discharged

Run 5's violation was that AN said row 2's flip re-pins to the new pair "rather
than surviving on the old one" while Open question 1 presented the surviving
reading as live. Both sides now read:

AN, pair 24 NEW:

> **That rules which IDs re-open and nothing about what this ledger shows in the interval** between the edit and the re-run; the pinned record is untouched either way, since *green at `b1ea992` over the UE tree at `fed8ae9`* stays true of those commits, which is what pinning is for.

Open question 1:

> It settles nothing about the interval, and the two are separate claims: the pinned record *green at `b1ea992` over the UE tree at `fed8ae9`* stays true of those commits throughout, so what is in question is the **live mark** and not the evidence behind it.

The two now name the same two objects — the pinned evidence citation and the
live ✓ — and assign the same one to each side of the split. AN's surviving
temporal clause, "the flip re-pins to a new pair **when the re-run completes**",
speaks to when the evidence pin moves; it is satisfiable under either answer to
Open question 1 (a ✓ withdrawn in the interval still re-pins at completion; a ✓
left standing still re-pins at completion). Neither decides the other's case.

The pinning premise is grounded: §3's parenthetical beneath the ledger records
that "a head expires and a sha does not", which is what makes a commit-pinned
record survive a later change.

### 3. The narrowing did not over-shoot

AN still rules what the Director ruled:

> **Which IDs a §4.8 CSV edit re-opens is ruled with it:** such an edit re-opens the **whole** pair — `T-DATA-05` and the headless `T-DATA` IDs together — and the flip re-pins to a new pair when the re-run completes.

with the reason kept ("the bytes both halves read are one file, so a change to
them is a change to both halves' subject") and the refused alternative kept
("re-opening the headless half alone was the alternative, and it is refused for
that reason"). The scope limit is worded as a conjunction — "That rules which
IDs re-open **and nothing about** what this ledger shows in the interval" — so it
affirms the re-opening in the same sentence that disclaims the interval; it does
not disclaim the ruling itself.

### 4. No third site takes a position on the interval

Every occurrence of *re-open* in the draft was read: pair 24's ruling, pair 24's
note ("AN is scoped to which IDs re-open; the interim display is not ruled and is
registered below"), the Check-results sweep sentence distinguishing AN's event
from the §4.4 wk-2 / Q20 "re-open when it widens", Open question 1, and the
Open-questions closing pointer. None of the other four states what §3 displays
in the interval. Pair 25 (AM, `dataCommit`) governs a manifest field's advance
condition and says nothing about the ✓; pairs 4, 9 and 38 state row 2's present
state, not its state after a future edit. The two GDD-side *re-open* sites
(§3's provisionally-met natural-language-commands goal at line 1514, and the
§4.4 wk-2 command-set note at line 1566) are about different objects and are
untouched.

### 5. Apparatus

- **Arithmetic.** Each row of the table matches the pair it cites: §3 9→10 ✓
  rows and 3→2 evidence-without-✓ (pairs 5, 9), 8→7 uncovered (pair 6), 6→5
  written-and-not-green (pair 7); §4.5 9→10 verified rows (pair 14), 61→62 green
  (pair 15) with 62 + 9 = 71 against 10→9 unclosed (pair 17); §4.7 33→34 rows,
  16→17 ruled, 17 open, and 17 + 17 = 34 matches pair 22's NEW; §4.11 5→6 flipped
  rows (pair 37). The note "AN is filed inside the existing Q34 row, so no
  register row is added" is true of pair 24 as written — the pair inserts exactly
  one row, already counted by pair 22.
- **Check results.** Every assertion is carried by the fact block: 5/5 in-editor
  at `fed8ae9`; 6/6 headless at `c2edae0` with WEEK-1 GATE PASS and INTEGRATION
  GATE PASS 2/2 under MSVC; `T-INT-01`/`T-INT-04` green at `e19605e` with 22
  files accounted for; the six known-bad controls with their catching checks; the
  `dataCommit` lag at `b1ea992` with the three CSVs byte-identical to `c2edae0`;
  the 44-pair inventory with insertions 24, 26 and 36 and the disjoint §4.9 sites
  2877–2885 and 2893–2894. Nothing in the bullet list has gone stale under this
  edit: the fail-proving bullet's "the control Ruling AN rests on" still names a
  control AN's amended text still cites, and the dependant-sentence sweep's new
  paragraph enumerates the sites that refer to AN's scope — pair 24's note, the
  Arithmetic note, the Open-questions pointer, §3's row-2 evidence cell and
  §4.5's green count — each of which reads as the sweep describes. The
  `Infantry.HP` figures are reported as a perturbed control's failure message,
  not as a unit stat, so §2's Infantry HP of 10 (line 174) is not contradicted.
- **Change requests.** Both are confirm-requests filed against existing text
  (§4.9's stub `Inputs` line and §4.9 part 1's *Nothing else is vendored*), with
  no pair filed and no prose change smuggled in; neither moves a number.
- **Open questions.** One question, on a §3 presentation matter no gate decides,
  plus the record of the three questions ruled this round (AL, AM, AN) pointing
  at the pairs that carry them.
- **Grounding.** Each bullet resolves to a live site in `source/gdd.md`: §3's
  ledger table and the paragraph beneath it (line 1531), Q29 and Q33 (lines 2654,
  2658), §3's per-sha pinning parenthetical, §4.9's module-registration
  paragraph, §4.11's † bullets and prose, §4.4's harness note. The commits and
  the `md5` line match `source/MANIFEST.txt`.
- **kb-desync.** No pair touches §2; `kb_rules.md` carries none of the ledger
  counts, the §4.8 UStruct field names or `dataCommit`, so nothing this addendum
  merges would make it wrong.

## Verdict

`sections/tech_t-data-05-harness.md` passes with zero violations, and the run
verdict is PASS. Run 5's contradiction was repaired at its cause rather than
papered over: Ruling AN now rules only which acceptance IDs a §4.8 CSV edit
re-opens and states its own scope limit, while what §3 displays between the edit
and the re-run is carried as Open question 1 for the Director; the two claims no
longer overlap, and no other site in the file takes a position on the interval.
Nothing must happen before merge beyond the ordinary merge discipline — apply
the 44 pairs at their stated sites, and put Open question 1 and the two
confirm-requests in front of the Director, since the §3 interim-display question
and the two senses of *vendored* are decisions this addendum deliberately does
not make.
