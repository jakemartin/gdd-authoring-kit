# Technical design — row8-ui-binding addendum (tech-director)

> ## ✅ APPLIED ADDENDUM — DO NOT RE-APPLY
>
> The one pair was merged into the master GDD on 2026-08-04.
> Master md5 `f5284420e237b1cbedbf3fd7d46f0988` →
> `83899833551abbe9d4518e21fd771520`.
>
> Gate: run `row8-2`, **PASS**, 0 violations, after `row8-1` (BLOCK, 2). Both
> violations were in the material around the pair; the Draft passed at
> `row8-1` and was not edited. (1) `contradiction` — the §4.10 change request
> told the Director no scenario or save file exists, while §3 records
> `data/ferrum_crossing.json` probed present at `9086d6a` and §4.10's own file
> layout names its `scenarioHash`; the conclusion survived but the reason a
> Director rules on was false. Fixed by deleting the existence claim and
> stating the two reasons separately. (2) `dead-reference` — Open question 1
> cited "the second CR above" for a T-INT-05 problem the fourth change request
> states, while Open question 3 used the same ordinal correctly, sending the
> Director to one row for two incompatible purposes. Fixed by naming the change
> request instead of numbering it.
>
> **The pair is a replacement, not an insertion**, so no OLD anchor survives on
> the merged master — verified after the apply: `isFlag, hasActed,` occurs 0
> times, `hasMoved` 2 and `hasActed` 2. The OLD was verified against the
> **master** before anything was written, matching exactly once.
>
> **What this round did:** wrote the GDD half of §4.11 row 8 — the drift §4.7
> Spec Stub 8 had carried since row 5's rebuild. Its snapshot named `hasActed`
> as one per-unit field while `T-TURN-01` asserts two independent flags, so the
> contract could not express a unit that had spent exactly one. `hasMoved` is
> the only identifier minted; it is a snapshot field name, not an acceptance
> ID, so §4.5 stands at 70 written / 20 unclosed / 16 in rows 8–10.
>
> **Row 8 still holds no code and nothing flips in §3** — its ledger row reads
> *pending*. §2 was byte-identical across the merge (103,435 chars, compared as
> strings), so `kb/rules.md` was untouched.
>
> **Four change requests and four open questions below are unwritten and owed a
> Director ruling** — the load-bearing ones being where per-unit presentation
> state lives (§2.11.1's DONE bit is neither flag) and whether a
> snapshot-fidelity check is owed and mints `T-UI-05` (§4.5 would become 71 /
> 21 / 17).

## Placement

An addendum against the merged master. One OLD/NEW pair, in **§4.7 Spec Stub 8
— UI binding contract**, on the snapshot's per-unit field list. No other
section is edited; the grep record behind that decision is in **Grounding**.

Row 8 holds no code. This draft adds none and flips nothing in §3.

## Draft

### Pair 1 — §4.7, SPEC STUB 8, snapshot per-unit fields

**OLD** (verbatim, §4.7 Spec Stub 8, the `per-unit` line and its continuation):

```
         per-unit  {id, side, unitId, hex, hp, hpMax, isFlag, hasActed,
                    captureProgress}
```

**NEW:**

```
         per-unit  {id, side, unitId, hex, hp, hpMax, isFlag, hasMoved,
                    hasActed, captureProgress}
                    `hasMoved` and `hasActed` are the TWO INDEPENDENT flags
                    T-TURN-01 asserts, carried into the snapshot as two
                    fields: one field cannot express a unit that has spent
                    exactly one of them. Neither is §2.11.1's DONE bit, and
                    no §2.11 surface reading "has not acted" binds to
                    either — §2.11.1 states where those bind.
```

`hasMoved` is the one identifier this addendum mints. It is a snapshot field
name, not a rule, a number or an acceptance ID: §4.5's written-ID count of 70
does not move, the 16 IDs in rows 8–10 stay 16, and the 20 unclosed stay 20.

## Build order

| # | System (ledger row) | Depends on | Headless? | Acceptance test IDs |
|---|---|---|---|---|
| 8 | UI binding (Stub 8) | 5, 7 (snapshot needs full state) | Contract + queries yes; widgets in-editor | T-UI-01..04 (**T-UI-03, 04 †**) + GATE-CAP-PARTIAL |

Unchanged from §4.11's row 8. This addendum moves no dependency, no † mark and
no acceptance ID.

## Change requests

| Existing § | Current text | Proposed change | Why |
|---|---|---|---|
| §4.7 Stub 8, snapshot per-hex fields | `per-hex   {terrainId, owner}` | Add a per-factory record of whether that factory has taken its build this turn — Stub 5's Inputs already name "the per-factory record of builds taken this turn (T-TURN-10)" as module state. Proposed NEW: `per-hex   {terrainId, owner}` plus a second field on capturable hexes carrying that record. | §2.11.5: "When any unit is affordable **and the factory has not built this turn**, the factory tile shows a small `BUILD` pulse." The snapshot as written carries no field that condition can read, so a widget §2.11 specifies cannot be fed. I did not write it: it mints a second identifier and the Director owns the schema. |
| §4.7 Stub 8, Acceptance | `Acceptance: T-UI-01..02 headless (the queries are headless functions); T-UI-03..04 in-editor Automation; GATE-CAP-PARTIAL headless, on the snapshot…` | Add one check asserting the snapshot's per-unit fields equal the rules module's own — i.e. that `hasMoved`/`hasActed` in the snapshot are the T-TURN-01 flags and not a widget-side copy that drifts. | No written invariant asserts the snapshot mirrors `GameState` at all; T-UI-01..04 each assert a binding downstream of it. Unnumbered on the `GATE-AI-SMOKE` / `GATE-CAP-PARTIAL` precedent, §4.5's count stays 70. Numbered as `T-UI-05` it becomes 71 written, 17 in rows 8–10, 21 unclosed. Which of the two — or neither — is a Director ruling. |
| §4.10, Canonical state hash | per-unit `{id, side, hex, hp, isFlag, captureProgress, pendingBuilds}` | Append the two per-unit turn flags, and the per-factory build record if the CR above is accepted. | The hash omits every per-unit turn flag, so two states differing only in which units have spent which flag hash equal. T-INT-02 and T-SAVE-06 compare hashes and nothing else, so a divergence in flag handling between the headless and in-engine builds is invisible to them. No save file carries a stale `stateHash`. `scenarioHash` is taken over scenario file content, which the §4.10 per-unit list never enters. Not written: §4.10's field order is a contract and row 10 is not mine to open this round. |
| §4.9, T-INT-05 | "rebuilding all widgets/actors from the current view-model snapshot alone reproduces the same displayed values (nothing lives only in a widget)" | Either name where §2.11.1's DONE bit lives in the view model, or scope T-INT-05 to values the Stub-8 snapshot carries. | §2.11.2's info panel displays `ready` or `done` from the DONE bit; §2.11.1 states that bit is the selection machine's own and is not the act flag, and Stub 8's snapshot is "produced by the rules module". A rebuild from that snapshot alone reproduces no DONE bit, so T-INT-05 as written is unsatisfiable for that one displayed value. This predates the flag split. |

## Open questions for the Director

1. **Where does per-unit presentation state live?** §2.11.1's DONE bit is
   per-unit, per-turn, and is neither `hasMoved` nor `hasActed`. Stub 7 has a
   precedent for keeping presentation state out of the Stub-8 snapshot
   (`guidedOpening`'s marked/locked). If DONE follows that precedent, T-INT-05
   needs the §4.9 T-INT-05 change request above; if DONE joins the snapshot,
   the snapshot stops being "produced by the rules module" alone. No gate is
   written either way.
2. **Is the per-factory build record a snapshot field or a query?** Stub 8
   already carries two queries (`reachable`, `forecast`) beside its fields.
   §2.11.5's pulse needs one or the other; the document states neither.
3. **Is a snapshot-fidelity check owed, and does it mint an ID?** Stated with
   its §4.5 arithmetic in the second change request above.
4. **The Fame widget's income rate has no snapshot field.** §2.11.2 shows
   `+175/turn` as a persistent element. It is computable from per-hex
   `{terrainId, owner}` and §2.7's +100 / +25, but that computation would sit
   widget-side. T-UI-03 forbids widget-side arithmetic for the scoreboard rows
   only, so this is unruled rather than violated.

## Handoffs

- **ux-onboarding-designer** — question 1 above touches §2.11.1's DONE
  paragraph and §2.11.2's `ready`/`done` info-panel line, and the first change
  request touches §2.11.5's BUILD pulse. I specify how a widget is fed, not
  what it shows; the wording of those three sites is that lane's.
- **rules-designer** — nothing. T-TURN-01's text is unchanged by this
  addendum; only its mirror in the snapshot moves.
- **scenario-designer** — nothing.

## Grounding

- Two independent per-unit flags, and T-TURN-01 asserting them: §4.7 Spec Stub
  5, Inputs line and T-TURN-01 (a)–(e); §2.1's core-loop block. Row 5's
  acceptance set closes at `6ccd40b` per §3's ledger row and §4.5.
- Row 8 holds no code, and both its dependencies have landed: §4.11's opening
  paragraph and row-8 cell; §3's UI row reads *pending*.
- DONE is not the act flag, and every §2.11 "has not acted" surface binds to
  DONE: §2.11.1, "What DONE means, and what binds to it"; §2.11.2's
  earn-your-pixels row for the unacted pip and its info-panel line.
- The BUILD pulse's condition: §2.11.5, third bullet. The per-factory record
  as module state: §4.7 Stub 5, Inputs.
- §4.5's counts — 70 written, 16 in rows 8–10, 20 unclosed — read off §4.5's
  risk row; they hold because this addendum mints no acceptance ID.
- Sites grepped document-wide and found unaffected, each checked in the text
  that would falsify it, not by the identifier alone:
  - `hasActed` occurs once in the document, at the pair above.
  - `captureProgress` per-unit against Q4's tile-held ruling (T-FAME-05):
    progress is non-zero only while the capturing Infantry stands on the tile
    and never transfers, so a per-unit field expresses the tile's state
    without loss. Unchanged.
  - `match {turn, turnCap, sideToMove, resultTier or null}` is quoted verbatim
    inside §3's ledger paragraph. The pair does not touch that line.
  - GATE-CAP-PARTIAL's "adding no field and no numbered ID" describes
    GATE-CAP-PARTIAL, not the snapshot, and survives the pair.
  - §2.10's "row 8 (UI binding) depends on row 7 because the snapshot needs
    full state", and §4.11's row-8 dependency cell `5, 7`: unchanged.
  - §2.11.1's selection machine reaches SELECTED only from a unit the DONE bit
    leaves live, and relights attack targets rather than reachable hexes in
    MOVED, so T-UI-02's highlight is never raised for a unit whose move flag
    is spent. No edit needed.
  - §4.10's per-unit hash list is a different list from the snapshot's and
    claims no equality with it; it is filed as a change request above rather
    than edited.
