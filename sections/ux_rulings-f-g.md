# UX, UI & onboarding — rulings-f-g draft (ux-onboarding-designer)

> ## ✅ APPLIED ADDENDUM — DO NOT RE-APPLY
>
> All three pairs were merged into the master GDD on 2026-08-04, together with
> `tech_rulings-f-i.md` (8 pairs) in one 11-pair application. Master md5
> `f327f0cf6a92e53fe59fab8550558e2e` → `5075d853166d99858fd3a5a4b7dfc27c`.
>
> **Pair 1 is a replacement. Pairs 2 and 3 are INSERTIONS** — each NEW opens with
> its OLD verbatim and appends — so **those two anchors survive on the merged
> master by design** and this file is not safe to apply twice. Classified by
> substring test over the final bytes, not by eye. Every OLD was verified against
> the **master** before anything was written, each matching exactly once.
>
> Gate: run `rulings-f-i-3`, **PASS**, 0 violations. This file passed at every
> run — `rulings-f-i-1` (0), `-2` (0), `-3` (0); the round's one violation was in
> the tech draft. It was nonetheless amended twice between runs, both times for
> facts that did not exist when it was written: the identifiers `isGuidedMarked`
> and `lockedThisTurn`, minted by `tech-director` after both briefs went out, and
> then **Ruling J**, which reclassified the first field and made the word
> *mirroring* inaccurate. **A file that passes can still be wrong about a fact
> that changed after it was drafted.**
>
> **`kb/rules.md` was NOT re-synced, against the gate's own merge note**, which
> said a re-sync was needed because these pairs move §2.11 text. That is the "§2
> changed" heuristic, not the test. The test is whether the change reaches what
> the KB *mirrors*: it mirrors §2.3, §2.4, §2.7 and §2.8 only, this round changed
> §2.11.1, §2.11.2 and §2.11.6, and all four mirrored subsections are
> **byte-identical** across the merge — enumerated by comparing every §2 heading
> block, heading to next heading of any level. KB md5 unchanged at
> `024523449be1873c9d545dbea6d3bc9d`.
>
> Over-90-char non-table lines: **126 before, 126 after**.

## Pairs

### Pair 1 — §2.11.1, "What DONE means, and what binds to it": the presentation block's membership

**OLD**

```
It lives in the **view-model** — the rules-produced snapshot plus a declared **presentation block** — as that block's sole member.
```

**NEW:**

```
It lives in the **view-model** — the rules-produced snapshot plus a declared **presentation block** — as a member of that block, alongside the guided opening's `lockedThisTurn` (§2.11.6-B, turn 1a), which is per-unit and per-turn and which the guidance layer owns rather than the selection machine.
```

Ruling F puts *locked this turn* in the presentation block under a second owner, so the sentence naming DONE the sole member no longer holds. The replacement states DONE's membership and its neighbour's owner without fixing a membership count, so a later addition to the block does not falsify it again.

### Pair 2 — §2.11.6-B, beat 1a: where each of the two surfaces reads from

**OLD**

```
Only one marked Infantry selectable; others dimmed (hover: `Locked this turn.`).
```

**NEW:**

```
Only one marked Infantry selectable; others dimmed (hover: `Locked this turn.`). The two states behind that surface read from two places. *Marked* — whether this unit is the scenario's `guidedOpening.infantry` — is the snapshot field `isGuidedMarked`, which the turn-1a unit marker reads out of the snapshot. `lockedThisTurn` is per-unit and per-turn, owned by the guidance layer, so the dimming and its hover string read it out of the view-model's presentation block.
```

Ruling F splits the state these two surfaces display, and the read source of each is what §2.11 owes: the marker binds to a snapshot field, the dimming and its hover string bind to the presentation block.

### Pair 3 — §2.11.2, earn-your-pixels audit, `Fame pool + +X/turn` row: the turn-1 reading

**OLD**

```
the `+X/turn` figure is the snapshot's per-side `incomePerTurn`, not a figure derived from the scoreboard's *X of N*, which does not separate factories from towns
```

**NEW:**

```
the `+X/turn` figure is the snapshot's per-side `incomePerTurn`, not a figure derived from the scoreboard's *X of N*, which does not separate factories from towns; and `incomePerTurn` is the standing rate, so on turn 1 the widget shows the rate that will pay at the start of turn 2 (Q8, §4.7) rather than the 0 that pays on turn 1
```

Ruling G decides the turn-1 reading of `incomePerTurn`, and this row is where §2.11 states what the player sees in that widget. The decision it supports — build now versus save — is answered by the rate that will pay, so the displayed figure and the decision named in the same row agree on turn 1.

## Check results — sites swept, no pair needed

Swept across §2.11.1–§2.11.8 for every spelling of the terms these two rulings introduce, split or widen: *presentation block* / PRESENTATION BLOCK, *view-model*, *sole member* / member / membership, *snapshot* / snapshot field, *marked* / marker / mark, *locked* / `Locked this turn.`, *guidance layer*, `guidedOpening.infantry`, `guidedOpening.objective`, *income* / `incomePerTurn` / `+X/turn` / per-turn, T-INT-05, T-UI-05.

| Site | Text swept | Finding |
|---|---|---|
| §2.11.2 audit, `Unacted pip` row | "carried in the view-model's presentation block" | States where the DONE bit is carried; asserts nothing about what else the block carries |
| §2.11.2 info panel, hovered unit | "read from the view-model's presentation block and not from a snapshot flag" | Binds the `ready`/`done` string to the DONE bit; asserts nothing about what else the block carries |
| §2.11.2 layer 3 (transient) | "income toasts restate what the Fame widget's `+X/turn` already shows" | Pairs a toast with the widget; the first income toast fires at the start of turn 2 (§2.7, Q8) |
| §2.11.2 screen mock | `FAME 350` / `+175/turn` at `TURN 12 / 20` | Mocked at turn 12 |
| §2.11.4 Destroyed row | "**passive income is excluded**" and its tooltip | About the tiebreak criterion, not about the income widget's figure |
| §2.11.5 production menu | `Fame: 250` header, `need 50` shortfall | Reads `fameTotal`, not the rate |
| §2.11.6 opening paragraph | "kills the guided opening's board state with it — the objective ring and the turn-1a unit marker clear in the same frame as the strip" | Names what the surfaces do on skip |
| §2.11.6, beat 3 | "Turn-1 income is not assumed anywhere in this beat: there is none (Q8, §4.7)" | States what is paid on turn 1 |
| §2.11.6, "Giving up the line is not retiring" | "the ringed objective and the marked Infantry" | Names the surfaces that keep running |
| §2.11.6, "Why beat 2 is a standing directive" | "The directive strip reads exactly those two fields: `guidedOpening.infantry` is the Infantry marked in beat 1a, `guidedOpening.objective` is the factory ringed from turn 1" | Names which authored fields the guided opening's content comes from, against a runtime heuristic; Pair 2 states the read source |
| §2.11.6, disappearance rule | "every beat, the objective ring, and the turn-1a marker expire with it" | Names what the surfaces do at end of turn 4 |
| §2.11.6-D ledger, Fame income & build row | "A bought unit spawns and stands on the board carrying its unacted pip" | Binds to the DONE bit via §2.11.1 |
| §2.11.8 build ranking | "directive strip with the four beats", "Fame pool + income widget" | Names deliverables |

## Change requests

None filed.

## Grounding

- Pair 1 — Ruling F (*locked this turn* joins the presentation block under a second owner); §2.11.1's DONE paragraph as the sentence that quantified over the block's membership; §4.7 Stub 8's presentation-block declaration and its `lockedThisTurn` member.
- Pair 2 — Ruling F (*marked* is a snapshot field; *locked this turn* is per-unit, per-turn, owned by the guidance layer); §2.11.6-B turn-1a row as the beat whose surfaces display both; §4.7 Stub 8's `isGuidedMarked` and `lockedThisTurn`; §4.7 Stub 7 `guidedOpening` for the scenario field name.
- Pair 3 — Ruling G (`incomePerTurn` reads the standing rate on turn 1); §2.7 income rates and first income landing on turn 2 (Q8, §4.7); §4.7 Stub 8's per-side group, where `incomePerTurn` sits.
