# Gate report — run `rulings-f-i-3`

Master GDD md5 `f327f0cf6a92e53fe59fab8550558e2e` (`source/MANIFEST.txt` present,
three entries; `kb_rules.md` @ `024523449be1873c9d545dbea6d3bc9d`,
`kb_setting.md` @ `b3e9e89daaef1cdeb333e3fb4368d1c0`). Sections read:
`sections/tech_rulings-f-i.md`, `sections/ux_rulings-f-g.md`. Both re-checked in
full against `source/` and this round's shared fact block, Ruling J included. The
`rulings-f-i-2` PASS was treated as no waiver: every pair was re-verified verbatim
against the master, and the amended sites were checked as new text.

**Top-level verdict: PASS. Violations: 0.**

---

## `sections/tech_rulings-f-i.md` — PASS (0 violations)

No violations filed. What was verified:

- **All eight OLD blocks match the master verbatim and uniquely** — Pair 1 at
  Stub 7's `guidedOpening` note ("…other source for the pair. The guidance layer
  reads this field from the loaded scenario directly — marked/locked is
  presentation state, not rules state, so it stays out of the Stub-8 snapshot.");
  Pairs 2–5 in Stub 8's scope paragraph, per-unit group, per-side group and
  presentation block; Pair 6 at §4.9's T-INT-05; Pair 7 in Q27's Blocks cell;
  Pair 8 in §4.4's week-3 cell ("Only T-SAVE-07 still waits — for wk 4's
  self-play logs. AI second pass").
- **No copy language survives anywhere in the file for `isGuidedMarked`.** The
  only remaining occurrences of "mirror" are Pair 4's `fameTotal` / `fameCombat`
  sentence, which the master already carries verbatim and which this round
  deliberately leaves alone. Pair 1 now reads "DECLARED DERIVED at that stub on
  this field"; Pair 3 marks and derives it; Pairs 5, 6 and 7 name it as a
  snapshot field without asserting a kind. Nothing calls it a copy, a mirror, an
  equal of a module-side value, or a value read across from the scenario file.
- **DECLARED DERIVED is consistent with T-UI-05 (b) and (c).** Clause (c) admits
  exactly "an unmarked mirror of a named module-side value" or "a marked field
  with a stated derivation"; Pair 3 supplies the second, in `spawnBlocked`'s form
  ("computed by the module and never widget-side"). Clause (b) requires the
  derivation to be recomputed inside the check from the sources T-UI-05 names —
  `strat::GameState`, the §4.8 tables, and the Stub-7 scenario file. Two ways
  this could have failed were checked and did not:
  - *Recomputation after the marked unit moves.* Pair 3 makes the field a
    property of the placement, not of the current hex, so the check must map the
    live unit back to `guidedOpening.infantry`'s placement. Stub 7 supplies the
    hex→placement half ("A hex identifies the placement uniquely because T-SCN-02
    already forbids two placements sharing one"), and the placement→unit half is
    module-side identity in `GameState`, which clause (b) names as a permitted
    source. Recomputable.
  - *§4.10's omission rule.* "What the hash omits is anything recomputable from
    the fields it already carries." The canonical state hash carries per-unit
    `{id, …}`, and the save file carries `scenarioId`/`scenarioHash` with a save
    being `loadScenario` + the command log, so the placement→`id` binding is
    reproducible from what they already carry. The field is omitted on exactly
    the footing §4.10 already states for `spawnBlocked`; no §4.10 pair is owed,
    and the draft's "checked, no pair needed" entry for it stands.
- **Ruling F's blast radius is fully covered.** Every master sentence that calls
  DONE the block's sole member or quantifies over the block's membership is
  paired: Stub 8's scope paragraph ("the per-unit state §2.11.1's SELECTION
  MACHINE owns"), the block header ("its membership is that machine's per-unit
  state and nothing else"), the DONE note ("and so the block's sole member"), and
  §2.11.1's "as that block's sole member", which is UX Pair 1's. A document-wide
  sweep for *guidance layer*, *marked/locked*, *presentation block*, *sole
  member* and *isGuidedMarked* returns no unpaired site.
- **Quoted §2.8 text is verbatim.** Criterion 2 — "the factories and captured
  towns a side owns at the cap, as *X of N*. Ownership only: a capture in
  progress (§2.7) counts for nobody until the objective flips." Criterion 3 —
  "total remaining HP of a side's units." N over the scenario's factories and
  capturable towns is what §2.11.4 already supplies (N = 8 on *Ferrum
  Crossing*). No rule is minted, as Ruling H requires.
- **Ruling G's turn-1 reading is grounded.** Q8(a): income accrues "at the start
  of the owner's turn" and "there is no accrual on turn 1", so the standing rate
  is what pays at the start of turn 2, which is what Pair 4 states.
- **Ruling I's schedule is grounded in §4.4's own text.** "each piece lands in
  the week the thing that consumes it runs" is verbatim in §4.4's note under the
  milestone table, and `Build` arriving with rows 4–5 in week 3 is week 2's cell.
- **No count moves and none is claimed.** No arithmetic section, no acceptance
  ID, no commit and no test-ID claim for T-UI-05 or for anything Rulings F–J add;
  the draft grounds the unimplemented state in Stub 8's acceptance line, §4.5's
  risk row and §3's UI evidence cell.

## `sections/ux_rulings-f-g.md` — PASS (0 violations)

No violations filed. What was verified:

- **All three OLD blocks match the master verbatim and uniquely** — §2.11.1's "It
  lives in the **view-model** … as that block's sole member."; §2.11.6-B turn
  1a's "Only one marked Infantry selectable; others dimmed (hover: `Locked this
  turn.`)."; §2.11.2's `+X/turn` audit-row clause. Each splices mechanically at
  one site.
- **The amendment leaves no copy language.** Pair 2 now reads "*Marked* — whether
  this unit is the scenario's `guidedOpening.infantry` — is the snapshot field
  `isGuidedMarked`, which the turn-1a unit marker reads out of the snapshot",
  which states the field and the read surface and asserts no field kind; the
  parenthetical gloss is Ruling F's own wording from the fact block and is
  therefore grounded, not invented. The grounding bullet no longer classifies the
  field. A full-file sweep for *mirror*, *copy*, *equals*, *reflect* and
  *scenario file* returns nothing.
- **Pair 1 does not re-quantify.** It states DONE's membership and names
  `lockedThisTurn`'s owner without fixing a count, so a later addition to the
  block does not falsify it. It does not conflict with tech Pair 5's and Pair 6's
  "two members": both are true of the block as this round leaves it.
- **The check table holds.** Each swept site was re-read on the master; none of
  the twelve asserts anything about the block's membership, about the marked
  field's kind, or about turn-1 income that Rulings F, G or J falsify. §2.11.6
  beat 3's "there is none (Q8, §4.7)" and Pair 3's "rather than the 0 that pays
  on turn 1" agree.
- **Lanes are clean.** UX touches §2.11.1, §2.11.2 and §2.11.6-B only; tech
  touches §4.4, §4.7, §4.9 and Q27 and explicitly disclaims §2.11. No two
  placements target one site, and no placement is vague.

---

## Verdict

**PASS**, both sections, zero violations, at `gdd.md` md5
`f327f0cf6a92e53fe59fab8550558e2e`. Nothing must happen before merge beyond the
Director's ordinary checklist: apply the eight tech pairs and the three UX pairs
at the placements they name, rebuild the derived files, and re-sync
`kb/rules.md`, since UX Pairs 1–3 move §2.11 text that the rules parse reads. The
item escalated at `rulings-f-i-2` — the definitional strain in calling
`isGuidedMarked` a mirror — is answered by Ruling J and is closed; the two places
the reclassification could have left a stale consequence, T-UI-05 clause (b)'s
recomputation after the marked unit moves and §4.10's omission rule, were each
carried back to the binding text and neither yields a finding, so there is
nothing further to escalate on this run. §4.5 does not move: 71 written / 52
green / 19 unclosed, 17 IDs in rows 8–10, 9 verified ledger rows, §3's uncovered
count 9, row 8 `*pending*`.
