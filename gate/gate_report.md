# Gate report — run `row5-flags-3`

- `source/MANIFEST.txt`: **present**, three lines, resolved against the kit root
  `E:\MultiAgent\gdd-authoring-kit`. No `sync-missing`.
- `gdd.md` md5 at this run: `7dc635b4f06589f89b46e2fa1b7ad86b` — matches the
  MANIFEST line and the md5 all three drafts declare in their Placement headers.
  Unchanged from `row5-flags-1` and `row5-flags-2`.
- Files gated: `sections/rules_row5-act-order.md` (**2** pairs),
  `sections/tech_row5-act-order.md` (**1** pair),
  `sections/ux_row5-act-order.md` (**8** pairs). **Eleven** pairs total.

## Top-level verdict: **PASS**

| Section | Verdict | Violations |
|---|---|---|
| `sections/rules_row5-act-order.md` | **PASS** | 0 |
| `sections/tech_row5-act-order.md` | **PASS** | 0 |
| `sections/ux_row5-act-order.md` | **PASS** | 0 |

Total: **0 violations**. Four at `row5-flags-1`, one at `row5-flags-2`, none
here.

---

## Re-derived, not accepted

**Anchors — eleven of eleven, each unique.** Every OLD was matched as a literal
against the current bytes of `source/gdd.md`, independently of the claim that
the OLDs are byte-identical to the last run:

- `rules` pair 2 — `  for each of your units (any order):`, two leading spaces,
  L126. `rules` pair 1 — `     select → move (within range, terrain-costed) →
  act (attack / capture / build) → done`, five leading spaces, L127. The fence
  runs L124–L131: **six body lines, eight including both delimiters**, and pair
  1 is the **third** body line, pair 2 the **second** — which is what Placement
  says.
- `tech` pair 1 — the seven-line `T-TURN-01` block, L1773–1779, matched once as
  a multiline literal.
- `ux` pairs 1–8 — L509, L512–515, L522, L531, L587, L599, L608, L712. Each
  counted **1**. Pair 8's anchor deserved the second look it got: `Move the
  marked Infantry first.` occurs twice in the document (L712 and Q27's entry at
  L2471), but the full OLD — `End Turn is inert until that Infantry has moved
  (hover: …)` — occurs only at L712; Q27 words it `End Turn is inert during beat
  1a until the marked Infantry has moved`, so there is no near-miss. **No
  problem anchor.** This confirms the byte-identical claim rather than relying
  on it.

**Classifications — confirmed by substring test on the bytes, not on the
authors' words.** `rules`: 2 replacements. `tech`: 1 replacement (`at most once,
per` occurs zero times in the NEW). `ux`: pair 3's NEW and pair 8's NEW each
contain their OLD verbatim as a prefix → **insertions**; pairs 1, 2, 4, 5, 6, 7
each drop OLD bytes the NEW does not carry → **replacements**. Pair 7 is the one
worth stating: the OLD's `from the MOVED state` does not survive into the NEW's
`from either the SELECTED or the MOVED state`, so the NEW does not contain its
OLD. **Stage total: 11 pairs, 9 replacements, 2 insertions**, and `ux`'s own
count of 8 pairs / 6 replacements / 2 insertions holds.

**Placements — no collision.** Three files, three disjoint regions: §2.1
(`rules`), §4.7 Stub 5 (`tech`), §2.11 (`ux`). Inside §2.1 the two anchors are
adjacent but disjoint body lines, order-independent. Inside §2.11 the four
§2.11.1 anchors are four disjoint regions in file order — lead-in above the
fence, the fence's first four transition lines, the last sentence of the
footnote below it, a table row below that. The two change requests that both
target §4.7 Stub 8's `hasActed` field are **requests, not pairs**, and each
names the other, so there is nothing to file.

**`kb_rules.md` — no `kb-desync`, and none was owed.** `kb_rules.md` declares
itself a parse of §2.3, §2.4, §2.7 and §2.8. Grepped for `act flag`, `core
loop`, `select →`, `move at most once`, `has acted` and `per turn`: **zero
matches**. No pair in this stage touches §2.3, §2.4, §2.7 or §2.8's bytes.
Nothing in this stage makes that file wrong.

---

## `sections/rules_row5-act-order.md` — PASS

Untouched since `row5-flags-2` and re-derived, not carried. Both anchors are
unique and correctly located in the fence; the Placement line-count facts
(`six body lines`, `eight including both ``` delimiters`, `third body line`,
`second body line`) match L124–131 exactly. Both pairs are replacements. The
change-request table is correctly empty — neither pair states or moves a number.
Both open questions stay withdrawn against the rulings that answer them. §2.9's
routine, §3's `per-unit act flags`, §4.7 Stub 5's `may move at most once AND act
at most once` and §4.7's `T-MOVE-03` are cited and none is restated or altered.

## `sections/tech_row5-act-order.md` — PASS

Untouched since `row5-flags-2` and re-derived. Pair 1's OLD is verbatim
L1773–1779. The five lettered checks stand against the document: (d)'s §4.9
citation is verbatim; (e)'s `the same moment T-TURN-10's per-factory build
allowance renews` matches `T-TURN-10`'s already-merged `The allowance renews at
the start of the owner's turn` at L1806–1807 and adds no second proposition; the
Inputs and Transition lines are quoted as they stand at L1766–1771; §2.8's
alias-map preamble does read `T-TURN-01..10`, so the handoff that says the
suite's extent is unaffected is correct. No ID minted, none retired, no §4.5
count paired, and the file disclaims any statement about `ad77b13`.

## `sections/ux_row5-act-order.md` — PASS

**The one filed violation is discharged, at its own site and in the right
scope.** Pair 8's NEW now reads `Those are the machine's only two routes from
SELECTED to DONE that do not pass through MOVED`. Checked against the merged
machine rather than against the author's summary: after pair 2, SELECTED has
five exits — `LMB on lit hex → MOVED`, `hover enemy target → forecast card`,
`LMB on lit target → DONE`, `Space → DONE`, `RMB / Esc → IDLE`. Exactly two
reach DONE without entering MOVED, and both are the ones pair 8 closes. The
Grounding bullet, retitled *Why the closure is exhaustive, stated over the right
set*, now states the claim over routes that skip the move, names the two from
SELECTED, disposes of `RMB/Esc → IDLE` as committing nothing, and enumerates the
three from MOVED — `LMB on a lit target`, `Space`, `RMB/Esc` — which is exactly
MOVED's three DONE exits at L517–519. The false proposition is gone and the true
conclusion is unchanged.

**The three unfiled, self-initiated corrections — audited hardest, and all three
land clean.** No violation constrained their wording, so each was checked as a
fresh assertion:

1. **Placement** — *"Exactly two routes run from SELECTED to DONE **without
   passing through MOVED** … Those are the two that can strand beat 1a, because
   every other route to DONE runs through MOVED and therefore spends the move
   the beat is waiting for."* True on both halves. DONE has no other producer in
   the machine — PRODUCTION MENU has no DONE exit, IDLE reaches DONE only via
   SELECTED — so *every other route* is the three MOVED exits, and entry to
   MOVED is `LMB on lit hex`, which is the move beat 1a waits on. The
   subordinate claim that Wait *"the input table has always granted from
   SELECTED"* is verbatim true at L537: `Wait — mark the **selected**/moved unit
   done without acting`.
2. **Pair 2's rationale** — *"With it listed, the two routes from SELECTED to
   DONE that skip the move are both on the diagram and both visibly
   enumerable."* Correct, and correctly scoped to the diagram it is arguing
   about. The paragraph's `Two additions and two edits` is not a miscount: the
   two additions are the attack pair (two lines, one behaviour, named in the next
   sentence) and the Space line, against two edited lines.
3. **The two survey-B rows** — the `MOVED ──Space (Wait)` row now says the
   transition *"is one of the three routes to DONE that run through MOVED, which
   is why pair 8's enumeration is qualified to the routes that skip the move
   rather than stated over all routes"*, and beat 1a's directive row says
   *"every remaining route runs through MOVED, so the directive stays satisfiable
   and `Move completes` stays reachable"*. Both are true against L516–519, and
   the second is the row that would have carried the overstatement forward into
   the survey if it had been left. The adjacent row on `this is what makes 1a
   retire inside turn 1 in every branch` is also correct on its placement claim:
   pair 8's insertion point at L712 is immediately before that clause, in the
   same cell, and the clause is carried through unedited.

**Nothing else in the file still carries the old enumeration.** Every remaining
statement about routes to DONE — Placement, pair 8's NEW, pair 8's rationale
(*"Every route by which the marked Infantry could reach DONE without moving is a
dead end"*, *"The machine's remaining routes to DONE all run through MOVED"*),
the `scenario-designer` handoff, and the Grounding bullet — is scoped to the
skip-the-move set or to the through-MOVED set, and each is true against the
merged block. The author's judgment that an uncorrected duplicate would resurface
was right, and no correction overreached its site: no anchor moved, no
classification moved, no pair was added or dropped, and the eight OLDs are the
ones already verified.

Everything else in the file re-checks: `T-TURN-01` is in §4.7 Stub 5,
`T-MOVE-03` reads `a move never ends on an occupied hex` at L1702, `T-UI-02` and
`T-UI-03` exist, `carrying its unacted pip` occurs once, `guidedOpening.infantry`
is named in the scenario sections, and `kb_setting.md` does carry the ≤ 30-word
result-line ceiling the Grounding bullet invokes. No pair states a number that is
not carried verbatim out of its own OLD.

---

## Deferrals and non-blocking observations — nothing is filed

**§2.7's build-limit boundary sentence** — still non-blocking, on the ground
ruled twice: check (e) cites `T-TURN-10`'s already-merged renewal sentence rather
than adding a proposition. Unchanged this round.

**§2.9** — still no pair owed; its routine never passes through §2.11.1's
machine.

**§4.11's preamble and §3's seven/five tally** — still the rebuild round's by
Director placement ruling. No pair in this stage mints or retires an acceptance
ID, all three files disclaim any statement about `ad77b13`, and merging these
eleven pairs neither worsens nor repairs that tally. Not a condition of this
merge.

**§4.7 Stub 8's `hasActed` field** — two distinct requests, both still open, each
naming the other. `tech` asks for a second **rules** flag; `ux` asks where the
**DONE** bit lives, which no rules flag yields. Neither states the field in its
prose, so neither is `invented-fact` or `stat-drift`. They must be resolved in
one edit or the field is edited twice.

**The second UI/rules divergence** — `rules` pair 2 writes into §2.1 that a unit
may be given its remaining command with other units' commands in between, and
§2.11.1's machine still does not offer that. Not filed, for the reason given at
`row5-flags-2`: `ux` pair 3's heading and its *"This is a UI restriction and
nothing more"* generalise over the class, so no merged sentence is false. It is a
word to the Director, not a condition of merge.

**`ux`'s Placement claim `No pair states a rule`** — waived at `row5-flags-1` on
bytes that have not changed since. I do not re-file what I have waived on
unchanged bytes.

---

## Verdict

**PASS.** All three files clear at zero: `sections/rules_row5-act-order.md` and
`sections/tech_row5-act-order.md` are unchanged and were re-derived rather than
carried — anchors, line counts, classifications and every citation re-checked
against the current bytes — and `sections/ux_row5-act-order.md` discharges its
single blocker exactly, by qualifying the enumeration to the routes that skip the
move in pair 8's NEW and in the matching Grounding bullet, without moving an
anchor, a classification or a pair count. The three unfiled corrections the
author made on its own initiative — Placement, pair 2's rationale, and two
survey-B rows — were audited as fresh assertions and are each true against
§2.11.1's merged block; taken together they remove the last four sites where the
overstatement could have resurfaced, which is the right call and the right scope.
Eleven anchors are unique, nine replacements and two insertions are correctly
classified, the three placements are disjoint, no number is invented, no
acceptance ID moves, and no draft owed a `kb_rules.md` note. The Director may
merge all eleven pairs at the placements each draft specifies; the merge
checklist's remaining obligations for this stage are the two open `hasActed`
requests, which must be answered in a single edit to Stub 8, and the rebuild
round, which still owns §3's tally and §4.11's preamble.
