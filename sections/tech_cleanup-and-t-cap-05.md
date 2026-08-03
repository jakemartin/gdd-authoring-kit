> ## ✅ APPLIED ADDENDUM — DO NOT RE-APPLY
>
> All six pairs were merged into the master GDD on 2026-08-03.
> Master md5 `324dfa07c91fc4ddec4c5315ba1c397b` → `f456445d516e75e5e31a5b749157bfd2`.
>
> Gate: run `cleanup-3`, **PASS**, 0 violations, after `cleanup-1` (BLOCK, 4 —
> one repeated fault: treating "row 8 holds no code" as making the gate
> unwritten, non-asserting and still blocked, where this document separates
> *written* / *unblocked-and-asserting* / *green*) and `cleanup-2` (BLOCK, 1 —
> a Grounding sentence left claiming all six pairs were replacements after the
> previous fix had turned one into an insertion).
>
> **Pair 3 is an insertion — its OLD anchor is retained deliberately.** Its NEW
> block opens with its OLD sentence and appends after it. Post-check on the
> merged master: every NEW present exactly once; pair 3's OLD present **once**,
> the other five OLDs **zero** times. This file is **not safe to apply twice**.
>
> `kb/rules.md` was **not** re-synced. §2 is byte-identical across this merge
> (98,194 chars both sides, compared as strings); no pair touches §2.

# Technical design — cleanup and T-CAP-05's gate home (tech-director)

## Pair 1 — §4.11 row 9, the dependency cell's tense

**OLD**
```
and they re-open when rows 4–5 add `Capture`/`Build`/`EndTurn`
```
**NEW**
```
and they re-open on the `Capture`/`Build`/`EndTurn` that rows 4–5 have since added
```

## Pair 2 — §4.7 register head, the suite that "now asserts"

**OLD**
```
and the gates they blocked
outright (T-FAME-02, T-FAME-04, T-FAME-05, T-FAME-07, T-AI-06 and the T-CAP-
tally suite) now assert.
```
**NEW**
```
and the gates they blocked
outright (T-FAME-02, T-FAME-04, T-FAME-05, T-FAME-07, T-AI-06 and the T-CAP-
tally suite less T-CAP-05) now assert. **T-CAP-05 is excepted:** it aliases
onto no `T-TURN-` ID (§2.8), and its gate home was ruled on 2026-08-02 to be
Stub 8's snapshot, where it is `GATE-CAP-PARTIAL`; row 8 holds no code, so that
gate has not run — it asserts, and it is not green.
```

## Pair 3 — §4.7 Q6, the tail of the ruled cell

**OLD**
```
T-FAME-07 and the T-CAP- tally suite unblocked.
```
**NEW**
```
T-FAME-07 and the T-CAP- tally suite unblocked. T-CAP-05 aliases onto no `T-TURN-` ID (§2.8), so it has a gate of its own rather than an alias: `GATE-CAP-PARTIAL`, ruled separately on 2026-08-02 into Stub 8's snapshot.
```

## Pair 4 — §4.7 Q14, the Blocks cell

**OLD**
```
T-CAP-05 — the one `T-CAP-` ID with no `T-TURN-` counterpart and no gate of its own (§2.8's alias map); the kb victory table
```
**NEW**
```
T-CAP-05 — the one `T-CAP-` ID with no `T-TURN-` counterpart (§2.8's alias map); its gate home was ruled on 2026-08-02 to be Stub 8's snapshot, where it is `GATE-CAP-PARTIAL`, and row 8 holds no code, so that gate has not run and T-CAP-05 is not green; the kb victory table
```

## Pair 5 — §4.7 Spec Stub 8, the check and its acceptance

The span is contiguous, so the Determinism block sits inside it; it is carried
byte-identical in both.

**OLD**
```
           (T-SCN-01's non-producible clause, enforced at the UI layer too)
Determinism: widgets are pure functions of snapshot + events; asserted
         end-to-end by T-INT-05 (§4.9).
Acceptance: T-UI-01..02 headless (the queries are headless functions);
         T-UI-03..04 in-editor Automation.
```
**NEW**
```
           (T-SCN-01's non-producible clause, enforced at the UI layer too)
  GATE-CAP-PARTIAL
           a capture in progress contributes zero to "objectives held" for
           either side: raising a unit's captureProgress short of completion
           leaves both sides' objectivesHeld unchanged. This is §2.8's
           T-CAP-05, which aliases onto no T-TURN- ID; it is a differential
           read of two fields this snapshot already carries, adding no field
           and no numbered ID (the GATE-AI-SMOKE precedent, row 6)
Determinism: widgets are pure functions of snapshot + events; asserted
         end-to-end by T-INT-05 (§4.9).
Acceptance: T-UI-01..02 headless (the queries are headless functions);
         T-UI-03..04 in-editor Automation; GATE-CAP-PARTIAL headless, on the
         snapshot rather than on a widget — which is why it carries no † and
         does not stand down if the editor pass does. A marked ID may not
         guard a rules invariant (§4.11's † note), and T-CAP-05 is one.
```

## Pair 6 — §4.11 row 8, the acceptance cell

**OLD**
```
| 8 | UI binding (Stub 8) | 5, 7 (snapshot needs full state) | Contract + queries yes; widgets in-editor | T-UI-01..04 (**T-UI-03, 04 †**) |
```
**NEW**
```
| 8 | UI binding (Stub 8) | 5, 7 (snapshot needs full state) | Contract + queries yes; widgets in-editor | T-UI-01..04 (**T-UI-03, 04 †**) + GATE-CAP-PARTIAL |
```

---

## Placement

| Pair | Section | Exact site |
|---|---|---|
| 1 | §4.11 | Table body, row 9's *Depends on* cell |
| 2 | §4.7 | Register preamble, the "No row now states *no reading*" sentence |
| 3 | §4.7 | Register table, Q6's *Assumption in force until ruled* cell, its last sentence |
| 4 | §4.7 | Register table, Q14's *Blocks* cell |
| 5 | §4.7 | Spec Stub 8's fenced block, from T-UI-04's last line to the end of Acceptance |
| 6 | §4.11 | Table body, row 8's *Acceptance test IDs* cell |

No pair touches §1, §2, §3, §4.4, §4.5, §4.8, §4.9, §4.10, §4.11's preamble or
its † bullets, or Spec Stubs 1–7. Pairs 2, 3, 4 and 5 are disjoint spans of §4.7
and apply in any order; so do 1 and 6.

## Grounding

Every **OLD** block was grepped against `source/gdd.md` (md5
`324dfa07c91fc4ddec4c5315ba1c397b`) and returns **exactly one** match; pairs 2
and 5 were grepped multiline, with their internal line breaks as written. Five
of the six pairs are replacements; **pair 3 is an insertion** — its NEW block
opens with its OLD anchor verbatim and appends one sentence after it, so that
anchor is retained deliberately and survives the merge. The insertion-aware
post-check should therefore expect pair 3's OLD to return **one** match after
application, and the other five to return **none**. Because that anchor
survives by design, **this file is not safe to apply twice**: a second
application would append pair 3's sentence a second time.

The ruling of 2026-08-02 names row 8's Stub 8 snapshot as T-CAP-05's gate home.
Both fields `GATE-CAP-PARTIAL` reads are already in that snapshot's field list —
`captureProgress` in the per-unit record and `objectivesHeld X of N` in the
per-side record — so the check adds no field. T-CAP-05's own wording
("contributes zero to 'objectives held' for either side") is §2.8's, quoted
rather than restated. That T-CAP-05 aliases onto no `T-TURN-` ID is the §2.8
alias map's own row for it. That row 8 holds no code is §3's ledger row for UI,
which reads `*pending*`.

`GATE-AI-SMOKE` is the precedent for acceptance that mints no numbered ID:
`spec/ai_spec.md` in the crew repo states the reason as "minting a `T-` ID here
would move §4.5's count", and §4.11 row 6's acceptance cell carries the check
without a `T-` ID. That is one precedent, from one row.

The rule pair 5 cites — that a marked ID may not guard a rules invariant — is
stated in §4.11's † paragraph and again in its T-INT-03 bullet. §4.7's cut-line
paragraph states a narrower version, scoped to the critical path.

**Arithmetic — no §4.5 figure moves.** §4.5 states **69** written acceptance IDs,
**42** green and **27** unclosed. `GATE-CAP-PARTIAL` mints no numbered ID, so the
written total stays 69; row 8 holds no code, so nothing closes and green stays
42; 69 − 42 = 27 unclosed stands. The `T-CAP-` IDs are not in that total in
either direction — they are §2.8's own numbering, aliases onto `T-TURN-` IDs.
No pair in this file touches §4.5.

## Open questions for the Director

1. **The alternative form for T-CAP-05, filed rather than written.** The ruling
   named the home and not the form. I chose an unnumbered gate check. The
   alternative is a numbered `T-UI-05`, which would put T-CAP-05 in an
   acceptance set under a `T-` ID and make it countable, at this cost: §4.5's
   written total goes 69 → 70 and its unclosed count 27 → 28, and §4.5's
   sentence "no new ID has been written since `c224825`" becomes false and has
   to be rewritten rather than qualified. Folding the assertion into T-UI-03 was
   the third option and I judged it excluded by the document rather than by
   preference: T-UI-03 is †, and a marked ID may not guard a rules invariant.
   If you prefer `T-UI-05`, pairs 5 and 6 are the ones to redraft and a §4.5
   pair becomes owed.
2. **Q14 is left open on purpose.** The ruling gave T-CAP-05 a gate home; it did
   not answer Q14's question, which is whether a partial capture counts toward
   "objectives held". Q14's stated reading is that it counts for nobody, and
   `GATE-CAP-PARTIAL` asserts exactly that reading, per the register's
   convention that a stated reading is what the gates assert. So the row is
   narrowed, not closed — a later ruling that granted partial credit would
   invert the gate. Closing Q14 is yours to call.
3. **§4.5's exemplar clause now under-reports.** It reads "row 6's
   GATE-AI-SMOKE is acceptance that deliberately mints none". That sentence
   stays true after these pairs, and no figure beside it moves, so I wrote no
   pair against it. Whether it should name both unnumbered checks — and whether
   the `GATE-` prefix is now a stated convention rather than one row's habit —
   is a Director call. Related: §4.11 row 6's acceptance cell names the smoke
   run descriptively ("self-play smoke") while pair 6 names row 8's check by its
   `GATE-` name, so the two cells use different conventions.
4. **Where capture progress lives.** Stub 8's snapshot exposes `captureProgress`
   on the unit; Q4's interruption ruling makes the tile its owner.
   `GATE-CAP-PARTIAL` reads the field wherever the snapshot puts it, so the
   check does not depend on the answer.
5. **§4.11 row 9's "re-open" presupposes a close that row 9 never had.** Pair 1
   fixes only the tense of the rows-4–5 clause, as scoped. T-INT-02/03/05 have
   never run, so they cannot re-open; rows 4–5 landed before row 9 was reached,
   and those gates will meet the widened command set on their first run. Whether
   the cell should say that instead is a rewrite, not a tense fix, so I did not
   make it.

## Change requests

None. No pair in this file states or restates a rule, and none proposes a change
to a section outside §4.7 and §4.11.

## Handoffs

**To `rules-designer` — §2.8, after these pairs land.** Two sites go stale, both
about **T-CAP-05**, and neither is touched here because §2.8's alias-map text is
that lane.

- The sentence to grep is **"no gate asserts it end to end, and it appears in no
  acceptance set."** Once pair 5 and pair 6 land, **both halves are false**:
  `GATE-CAP-PARTIAL` asserts the whole property end to end and nothing blocks
  it, and T-CAP-05 appears in Spec Stub 8's Acceptance line and in §4.11 row 8's
  acceptance cell. The residual true fact, if the rewritten sentence wants one,
  is that the gate has not run and T-CAP-05 is not green.
- The alias-map row that reads **`| T-CAP-05 | **nothing** | see below |`** no
  longer has "nothing" to name. Its gate is `GATE-CAP-PARTIAL`, which is not a
  `T-TURN-` ID, so whether that column can hold a non-`T-TURN-` name — or
  whether the row keeps pointing below to a rewritten paragraph — is a §2.8
  formatting call, not mine.

Both are cited by ID: **T-CAP-05** and **GATE-CAP-PARTIAL** are greppable, and
`GATE-CAP-PARTIAL` returns no match against `source/gdd.md` at this md5.

No handoff is owed to `scenario-designer` or `ux-onboarding-designer`: pair 5
specifies how a snapshot field is checked and states no screen layout.
