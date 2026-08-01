# UX, UI & onboarding — rubric-round-2 addendum (ux-onboarding-designer)

**This is an addendum, not a draft.** §2.11 is merged and carries Director
rulings that `sections/ux.md` never saw. Nothing here redrafts a section.
Apply the pairs below and nothing else; `sections/ux.md` stays superseded.

Each **OLD** block below was verified to occur **exactly once** in
`source/gdd.md` before being written here (search terms used, and their hit
counts, are recorded under *Uniqueness checks*).

---

## Pair 1 — §2.11.6-B, beat 3 constraint cell (Q8 residue)

Line 632 of `source/gdd.md`, the guided-opening beat table.

**OLD**
```
| 3 | None. Fame ≥ 100 guaranteed by 200 start + home income (§2.7) |
```
**NEW**
```
| 3 | None. Fame ≥ 100 whenever this beat is outstanding, and not because of income: builds are Fame's only sink (§2.7), and the beat retires on the first spawn — so an outstanding beat 3 means nothing has been spent and the player still holds **at least their opening Fame**, which is 350 at §2.11.6's default Easy tier and never below Infantry's 100 at any tier the player can pick (Normal 200, Hard 100 — §2.7, §2.9). Turn-1 income is not assumed anywhere in this beat: there is none (Q8, §4.7) |
```

**Why the old text was wrong twice and the guarantee still holds.**

- *"+ home income"* cites an accrual that does not exist when the beat can
  first run. §2.7: income accrues at the start of your turn **with no accrual
  on turn 1**, first income on turn 2 (Q8, §4.7). Beat 3 can take the line on
  turn 1 in the fast lane (§2.11.6-B schedule table, fast-lane column), and
  §2.11.6-B's read-a-cell paragraph already says beat 3 can retire on a turn-1
  build. So the old constraint justified a turn-1 fact with turn-2 money.
- *"200 start"* is a Normal-tier baseline, not a constant. §2.7's Starting
  Fame bullet says so in as many words — *"the 200 is a baseline, not a
  constant, for the player"* — and §2.9's handicap moves the player's side
  only: Easy 350, Normal 200, Hard 100. §2.11.6-B runs the first match at
  **Easy**, so the number the old cell cited is not even the number in play at
  the beat it constrains.

**The guarantee survives at every tier, and here is the check.** Fame is
spent only on builds (§2.7 build & spawn; repair is free for the prototype,
§2.7 repair bullet — no other sink exists in §2). Beat 3 retires the instant
a unit spawns. Therefore, for as long as beat 3 is outstanding, the player's
pool is monotonically non-decreasing from its opening value:

| Tier | Player opening Fame (§2.7, §2.9) | Beat-3 requirement | Clears? | Margin |
|---|---|---|---|---|
| Easy (§2.11.6 default) | 350 | 100 (Infantry, §2.4) | Yes | +250 |
| Normal | 200 | 100 | Yes | +100 |
| Hard | 100 | 100 | Yes | 0 — exact |

Hard is the binding case and it clears **exactly**: the directive
`Spend Fame at your Factory. Infantry costs 100.` is satisfiable on turn 1
with zero margin, and one Infantry is the whole of that turn's buying power.
No change request is filed, because nothing breaks — but the zero-margin
tier is named in the Open questions below, since it is the one tier where a
future cost change to Infantry would silently falsify this cell.

No number in the NEW text is new: 350 / 200 / 100 openings are §2.7's Starting
Fame bullet and §2.9's difficulty bullet; 100 for Infantry is §2.4 via §2.7's
build bullet; "no accrual on turn 1" is §2.7's Income bullet under Q8.

---

## Pair 2 — §2.11.4, the uncited setting guide

Line 576 of `source/gdd.md`, the End-of-match screen paragraph.

**OLD**
```
Beneath the tier, one **faction-voiced result line** (per the setting guide: faction voice appears only on result screens; ≤ 30 words; field-manual register). Samples, one per case, generated content to follow these:
```
**NEW**
```
Beneath the tier, one **faction-voiced result line**, written to the setting and voice guide (`kb/setting.md`), which supplies all three constraints on it: faction voice appears only in result-screen text, a result line is **≤ 30 words**, and the register is field-manual plain — terse tactical briefing, substance over drama, no melodrama or fantasy filler. The same file's two faction blocks supply the voices the samples below are written in — the **Directorate** cold, doctrinal, bureaucratic-military, framing every outcome as a matter of record; the **Vanguard** terse, pragmatic, defiant, measuring everything by ground held — and its pipeline note retrieves a faction block *only* for this screen, which is why faction voice appears nowhere else in the UI. Samples, one per case, generated content to follow these:
```

**The citation genuinely carries the claim** — checked line by line against
`source/kb_setting.md` before pointing at it:

| Clause in §2.11.4 | Backed by `kb/setting.md` |
|---|---|
| "faction voice appears only in result-screen text" | Tone bible, closing line: *"Faction voice appears only in result-screen text."* Also the header note: the pipeline *"retrieves a faction block only for faction-flavored content (result-screen text)"* |
| "≤ 30 words" | Tone bible, Length: *"A result line is <= 30 words."* |
| "field-manual plain" register | Tone bible, Register: *"terse tactical briefing. Field-manual plain, not marketing copy."* |
| "generated content to follow these" | Header: *"The pipeline retrieves the tone bible for every generation"* |
| Directorate voice of the two Directorate samples | Faction A: *"cold, doctrinal, bureaucratic-military. Speaks in directives and ledgers… frames every outcome as a matter of record."* Sample cadences *"Command directive:"* and *"Order is restored."* are both literally in the shipped decisive line; *"The ledger favors the Directorate. The record stands."* is the ledger/record register verbatim |
| Vanguard voice of the two Vanguard samples | Faction B: *"terse, pragmatic, defiant… measures everything by ground held."* Sample cadence *"We hold the ridge."* → shipped *"We hold the ground."*; *"The ground says we win."* is the ground-held measure |
| The two draw lines, "neutral system voice" | Not a contradiction: the guide reserves faction voice *for* result screens; it does not require every result line to be factional, and it names a *"neutral field-manual voice"* for non-faction content |

Also checked and clean: none of the four faction samples uses a word from the
guide's banned register (*destiny, glory, honor, legend, forever, epic,
heroic, sacred, doom*), and all six sample lines are under 30 words. The
citation is sound; nothing in §2.11.4 asserts setting content the guide does
not carry. No new faction fiction is written here — the NEW text paraphrases
the guide's own descriptors and nothing more.

Path style follows the GDD's existing convention for repo-relative files
(`data/units.csv`, `data/terrain.csv` in §4).

---

## Pair 3 — §2.11.6, the other uncited "tone bible" *(Director's discretion)*

Line 619, teacher 3 of the onboarding philosophy list. **Same defect as Pair
2, one subsection away**, and it is the only other uncited reference to that
file in §2.11 (search: `tone bible` — 1 hit outside Pair 2's paragraph). Drop
this pair without consequence if the round is being held to two targets.

**OLD**
```
(≤ 30 words, tone bible)
```
**NEW**
```
(neutral system voice per the tone bible in `kb/setting.md`; ≤ 30 words, borrowing that file's result-line ceiling — one-shot tips are not a length category it names)
```

The honesty clause is deliberate. `kb/setting.md` gives two length ceilings —
codex blurb ≤ 40 words, result line ≤ 30 — and a one-shot event tip is
neither. The 30 is a house cap the UX section chose; the *register* is the
part the guide actually supplies (*"Unit and terrain codex entries use this
neutral field-manual voice (no faction)"*, and faction voice is reserved to
result screens, which is why one-shots are system-voiced). Pointing an
uncaveated citation at a number the file does not state for this category
would be the same rubric defect in a new place.

---

## The turn-1 income sweep — what it found and what it cleared

Q8 rewrote §2.7's Income and Starting Fame bullets, §2.9's economy phase, and
two gates. I searched §2.11 (lines 412–702, read in full, plus targeted
searches) for any UI string, constraint, or mock that still assumes turn-1
accrual or treats 200 as a constant. **One genuine hit — Pair 1.** The rest,
recorded so a later reader does not re-run the search:

| Site | Text | Verdict |
|---|---|---|
| §2.11.6-B preamble | *"at **Easy** by default (player +150 opening Fame, §2.9)"* | **Correct and post-Q8.** Cites the handicap as a delta on the player's side, exactly as §2.9 states it |
| §2.11.6-B, "How to read a cell" | *"Fame ≥ 100 from turn 1"* | **True at every tier and cites no income** — Hard's 100 opening meets it exactly. Left alone; Pair 1 is now the sentence that justifies it |
| §2.11.2 HUD mock | `FAME 350` / `+175/turn` | Not a turn-1 claim — a turn-12 mock. The 350 is coincidental, not the Easy opening |
| §2.11.2 layer 3, §2.11.2 audit row | income toasts, `+X/turn` widget | **Rate statements, not accrual-timing claims.** On turn 1 the widget reads a rate that first pays at the start of turn 2; the player ends turn 1 and sees the pool rise. No contradiction, no edit |
| §2.11.2 info panel | `Factory · move 1 · def +15% · yours (+100/turn)` | Same — a per-turn rate from §2.7's Income bullet |
| §2.11.2 turn banner | *"watching the AI's economy phase is how the player learns the enemy shares the same Fame economy"* | **Still true post-Q8.** §2.9's economy phase explicitly runs on *"none on turn 1"*; the AI's 200 opening funds a visible turn-1 build regardless |
| §2.11.5 production mock | `Fame: 250`, `need 50` vs Tank 300 | Illustrative pool, no tier or turn claim |
| §2.11.4 Destroyed row + tooltip | *"Factory income does not count at the cap."* | Cap-exclusion rule (§2.8), untouched by Q8's accrual timing |
| §2.11.6-C one-shots | *"+150 Fame. Kills count at the cap. Income does not."* | Same — exclusion, not timing |

The only occurrence of the string `200 start` in the whole document was
Pair 1's cell. §2.11 contains no other bare `200` outside unit costs
(Artillery 200, §2.4).

---

## Change requests

**None.** The Pair 1 guarantee was tested at all three tiers and holds at all
three, so it is restated on a true basis rather than escalated. Pairs 2 and 3
add a citation and invent nothing.

---

## Open questions for the Director

1. **Hard tier clears beat 3 with exactly zero margin** (opening 100 vs
   Infantry 100). That is fine today and needs no rule change. But it means
   the beat-3 guarantee is now load-bearing on *two* numbers at once —
   §2.9's Hard handicap of −100 and §2.4's Infantry cost of 100. If either
   moves, this cell falsifies silently. Worth a line in the §4.7 register, or
   a note on the Hard row of §2.9, so the coupling is visible from both ends.
   I have not written either — both are outside §2.11.
2. **Pair 3 is optional.** It fixes the same uncited-file defect as Pair 2 but
   was not in this round's brief. Take it or leave it; the two are independent.

---

## Handoffs

- **rules-designer** — Open question 1 is a rules-side coupling
  (§2.9 Hard handicap × §2.4 Infantry cost). §2.11 only consumes it.
- **tech-director** — nothing new. The one-shot string table (§4.1 boolean
  flags) and the result-line strings now both cite `kb/setting.md` as their
  source-of-voice file; if a string table is authored as data, that file is
  its review reference. No schema change requested.
- **scenario-designer** — untouched. The fast-lane branch and the 1-MP-slack
  case in §2.11.6-B are cited above only as evidence that beat 3 can run on
  turn 1; no scenario claim is altered.

---

## Grounding

| Change | Mechanic it serves |
|---|---|
| Pair 1 rebasing the guarantee on *opening Fame + no sink but builds* | §2.7 Income (no accrual on turn 1, Q8), §2.7 Starting Fame (200 is a baseline, not a constant), §2.9 handicap (Easy +150 / Hard −100), §2.7 build & repair (builds are Fame's only sink), §2.4 Infantry 100 |
| Pair 1 naming the tier explicitly rather than a bare number | §2.11.6-B already runs the first match at Easy; a constraint that cites a Normal number cannot be checked against the match it governs |
| Pair 2 naming `kb/setting.md` | §2.11.4's end screen is the only faction-voiced surface in the game; the rule that makes it the only one lives in that file, so the rule and the citation must point at the same place |
| Pair 3's caveat on the 30-word cap | §2.11.6's one-shot tips are system voice, which the guide supplies; the length ceiling it does not, and a UX doc should not launder a house choice as a cited constraint |

---

## PLACEMENT

Three surgical replacements, all inside §2.11. No section is rewritten, no
heading moves, no table gains or loses a row or column.

| Pair | Target | Location in `source/gdd.md` |
|---|---|---|
| 1 | **§2.11.6-B**, guided-opening beat table, **row "3", Constraint column** | line 632 — replace the cell text between the `| 3 |` marker and the closing pipe before the backticked directive. The Directive, Teaches and "Retires when" columns of that row are **unchanged** |
| 2 | **§2.11.4**, "End-of-match screen" paragraph, first two sentences after *"…on screen all match."* | line 576 — replace from *"Beneath the tier,"* through *"generated content to follow these:"*. The five bulleted sample lines that follow are **unchanged** |
| 3 *(optional)* | **§2.11.6**, Philosophy list, item 3 | line 619 — replace the parenthetical `(≤ 30 words, tone bible)` only; the rest of the bullet, including the `(boolean flags in the save slot, §4.1)` citation, is **unchanged** |

### Uniqueness checks run before writing

| OLD block | Search term | Hits in `source/gdd.md` |
|---|---|---|
| Pair 1 | `200 start` | 1 (line 632) |
| Pair 2 | `per the setting guide` | 1 (line 576) |
| Pair 3 | `tone bible` | 1 (line 619) |

---

## Summary for the Director (relay verbatim)

Two rubric targets in §2.11, plus one optional adjacent fix, delivered as
three exact OLD/NEW replacement pairs — no redraft, so the rulings merged into
§2.11 since `sections/ux.md` are untouched. **Pair 1** rewrites §2.11.6-B beat
3's constraint, which justified "Fame ≥ 100" with "200 start + home income":
both halves are dead after Q8 (there is no turn-1 accrual) and §2.9 (200 is a
Normal baseline, and this beat runs at Easy). The guarantee itself survives
and is now stated on a basis that is actually true at the beat — builds are
Fame's only sink and beat 3 retires on the first spawn, so an outstanding beat
3 means the player still holds at least their opening Fame: 350 at Easy, 200 at
Normal, 100 at Hard, versus Infantry's 100. It clears at all three tiers, so
**no change request is filed**; Hard clears exactly, with zero margin, and that
coupling between §2.9's −100 handicap and §2.4's Infantry cost is raised as an
open question rather than fixed in someone else's section. A full sweep of
§2.11 for other turn-1-income or 200-as-a-constant residue found **one** hit —
that same cell — and the nine near-misses are listed with verdicts so the
search need not be repeated. **Pair 2** replaces §2.11.4's unnamed "per the
setting guide" with a named citation to `kb/setting.md`, after checking clause
by clause that the file genuinely carries all three constraints (result-screen-
only faction voice, ≤ 30 words, field-manual register) and both faction voices
the four shipped result strings are written in; it does, and no banned-register
word or over-length line appears in them. **Pair 3**, optional and droppable,
fixes the identical uncited-file defect at §2.11.6's "tone bible" reference and
flags honestly that the 30-word cap on one-shot tips is a house choice borrowed
from that file's result-line limit, not a number the file states for tips.
