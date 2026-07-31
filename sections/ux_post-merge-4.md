> # ✅ APPLIED ADDENDUM — DO NOT RE-APPLY
>
> Every replacement pair in this file **has been applied to the master GDD**, and
> the master has moved on since. Its Old blocks no longer match, so re-applying is
> a no-op at best; its quoted "current" text, register extents, and any hash it
> names are a **snapshot of the moment it was written**, not the current state.
>
> **The master GDD is the source of truth** — read `source/gdd.md`. Further changes
> to a merged section go in a *new* addendum file.

# UX, UI & onboarding — post-merge-4 fix draft (ux-onboarding-designer)

## Placement

All edits sit inside **§2.11.6 Onboarding — the first session** of the merged
master (`source/gdd.md`, md5 `d5fc06396a738ecb842b3263cf36c1ca`). Four of the
five pairs are in **§2.11.6-B**; the fifth is the one cell of the **§2.11.6-D**
concept ledger that paraphrases a §2.11.6-B claim I am correcting, and would
otherwise be left restating the corrected sentence in its old, false form.

Nothing outside §2.11.6 is touched. **No rule, cost, or stat changes.**
Infantry Move 3 (§2.4), the 6 MP opening-capture budget and *Ferrum Crossing*'s
5 MP / 5 MP with 1 MP of slack (§2.13.1), the stretch maps' 2 and 3 MP of slack,
and capture N = 1 as an assumption in force under Q4 (§2.7) all stand as
written and are cited, not restated differently. **The schedule table is not
edited** — the gate re-traced all twelve cells and the strip-gone condition and
they are correct. Everything below makes prose agree with that table.

## Draft

Five exact old→new pairs. Apply in file order.

---

### V1 — beat 2's row: "at most one turn" is false in the wandered branch

This is the reported violation. The retire cell still describes beat 2 as
holding the line for **at most one turn**. The schedule table's wandered column
returns beat 2 to the line on **turn 4** as a rule-2 last call, so in that
branch it holds the line on turn 2 *and* again on turn 4 — twice.

This is the residue of the original "occupies the line for turn 2 only." I
corrected that phrasing once in the fast-lane direction (beat 2 never holds the
line at all when the pip lands on turn 1) and left the ceiling untouched. The
ceiling is the other end of the same sentence and is wrong by one.

The underlying mechanism is unchanged and correct — a beat gives up the line at
the end of the turn it first appeared, and rule 2 can return it later — so the
row below states **outcomes per branch** and does not restate the yield rule,
which lives two paragraphs down and stays as it is.

**OLD**

```
| 2 *(standing)* | None on selection. The scenario's designated neutral factory (`guidedOpening.objective`, §2.13.1) is ringed from turn 1; its info-panel line appends `Only Infantry captures.` | `Move the Infantry onto the ringed Factory. Only Infantry captures.` | Capture; the Infantry-only rule (§2.7) | A capture pip appears — on whatever turn that happens. *Standing* means it stays **outstanding**, not that it holds the strip: it occupies the line for **at most one turn** — turn 2 in the common case, and not at all if the pip has already landed (fast lane) — then yields and runs on the ring and the unit marker. Hard-expires at end of turn 4 |
```

**NEW**

```
| 2 *(standing)* | None on selection. The scenario's designated neutral factory (`guidedOpening.objective`, §2.13.1) is ringed from turn 1; its info-panel line appends `Only Infantry captures.` | `Move the Infantry onto the ringed Factory. Only Infantry captures.` | Capture; the Infantry-only rule (§2.7) | A capture pip appears — on whatever turn that happens. *Standing* means it stays **outstanding**, not that it holds the strip. How many turns it actually holds the line is decided by rules 1–2 and by when the pip lands, and the schedule table's three branches are exhaustive: **twice** — turn 2, then a turn-4 rule-2 last call, if the pip has still not landed (wandered); **once** — turn 2 only, retiring on a turn-2 or turn-3 pip; or **never** — the pip lands on turn 1 and beat 2 retires before rule 1 can select it (fast lane). On every turn it does not hold the line it runs on the ring and the unit marker. Hard-expires at end of turn 4 |
```

---

### V1-b — the guarantee sentence claims a turn on the strip for *every* beat

Same defect, one paragraph later, and it is what made the ceiling look safe.
"Every beat is guaranteed its own turn on the strip" is contradicted by the
schedule table's fast-lane turn-1 cell, which says in as many words that beat 2
retires **without ever holding the line**. The guarantee that is actually true —
and the one the strip is built to deliver — is that no beat *expires* unheard: a
beat either retires on its own event, meaning the lesson landed in play, or rule
2 puts it on the line before the window closes. Restated to say that, the
sentence's job in the paragraph (a hanging beat 2 cannot starve beat 3) is
unchanged.

**OLD**

```
The consequence that matters: **every beat is guaranteed its own turn on the strip.**
```

**NEW**

```
The consequence that matters: **no beat expires unheard.** Each beat either retires on its own event — its lesson landed in play, which is exactly what beat 2 does on turn 1 in the fast-lane branch, before it has ever held the line — or it holds the line at least once before the window closes, which is what rule 2 exists to force.
```

---

### V1-c — the "why beat 2 is standing" paragraph states turn 2 and turn 3 unconditionally

The two sentences below describe beat 2's line time as fixed: it *appears on
turn 2*, holds turn 2, yields turn 3, returns for a turn-4 last call. That is
the shipped map's story and it is true there — on *Ferrum Crossing* both lanes
cost 5 MP against Infantry Move 3 (§2.13.1, §2.4), so the pip cannot land on
turn 1 and beat 2 must take the line on turn 2. Stated without that scope, it
contradicts the fast-lane column, where beat 2 never takes the line. Scoping
the claim to the map the paragraph is about costs nothing and makes the
ceiling — two turns — explicit in the one place a reader goes looking for it.
No number in the paragraph moves: 5 MP, 5 MP, 1 MP of slack, 6 MP budget,
end of turn 4.

**OLD**

```
The standing directive absorbs precisely that: it appears on turn 2, stays outstanding until the pip appears, and hard-expires at the end of turn 4 — the last turn of the guided window, not one turn past it. It persists as an *objective*, not as a line of text: it holds the strip for turn 2, yields the line to beat 3 for turn 3, and returns for a turn-4 last call only if the pip still has not landed.
```

**NEW**

```
The standing directive absorbs precisely that: on *Ferrum Crossing*, where a turn-1 pip is impossible at 5 MP per lane against Move 3, it takes the line on turn 2, stays outstanding until the pip appears, and hard-expires at the end of turn 4 — the last turn of the guided window, not one turn past it. It persists as an *objective*, not as a line of text: it holds the strip for turn 2, yields the line to beat 3 for turn 3, and returns for a turn-4 last call only if the pip still has not landed. That is **two turns on the line at the outside** — one in the common case, where the turn-2 pip retires it, and none at all on a map whose lanes let the pip land on turn 1 (the fast-lane column).
```

---

### V1-d — the End Turn gate becomes Q27 in the text, not a footnote in my draft

Raised twice, unruled twice, and load-bearing: the gate's own verification of
the schedule table's turn-1 row depends on 1a being unable to outlive turn 1,
which depends on End Turn being inert until the marked Infantry has moved. A
constraint that a gate leans on should carry a number in the text rather than
live in an author's open-questions list, so it is cited here in the house style
§2.13.1 already uses for Q24 and Q26. The constraint itself is unchanged — same
scope (beat 1a of a first match), same hover string, same death on
`Skip guidance`. Only the citation is added. **The Q27 entry text is in Open
questions below and must land in §4.7's register at merge.**

**OLD**

```
| 1a | Only one marked Infantry selectable; others dimmed (hover: `Locked this turn.`). End Turn is inert until that Infantry has moved (hover: `Move the marked Infantry first.`) — this is what makes 1a retire inside turn 1 in every branch | `Select the marked Infantry. Lit hexes are its true reach. Click one to move.` | Selection; the highlight is the real move set (§2.5) | Move completes |
```

**NEW**

```
| 1a | Only one marked Infantry selectable; others dimmed (hover: `Locked this turn.`). End Turn is inert until that Infantry has moved (hover: `Move the marked Infantry first.`) — this is what makes 1a retire inside turn 1 in every branch, and it is the only guided-opening constraint that gates a player *input* rather than a selection, so it is carried as **pending Q27** (§4.7) rather than adopted silently | `Select the marked Infantry. Lit hexes are its true reach. Click one to move.` | Selection; the highlight is the real move set (§2.5) | Move completes |
```

---

### V2 — the §2.11.6-D ledger cell that paraphrases the corrected guarantee

Outside -B, but it is a direct cross-reference to the sentence V1-b rewrites —
"guaranteed its own turn on the strip **(B)**" — and it is false in the same
corner plus one more: a player who builds on turn 1, or on turn 2 in the common
case, retires beat 3 before rule 1 ever selects it. Leaving a paraphrase of a
corrected claim standing next to the corrected claim is the exact drift that
produced this violation. The cell's own point is untouched: the row confirms on
the **spawn event**, not on the directive.

**OLD**

```
| Fame income & build | Fame is abstract; player hoards, never connects factories → army | Beat 3, which is guaranteed its own turn on the strip (B); income toasts; `BUILD` pulse when affordable; greyed rows with shortfall (§2.11.5) | A bought unit spawns and stands on the board carrying its unacted pip — the **event**, not the directive, so the row also confirms for a player who skipped guidance |
```

**NEW**

```
| Fame income & build | Fame is abstract; player hoards, never connects factories → army | Beat 3, which holds the strip on turn 2 or turn 3 in every branch where the player has not already built — and where they have, the lesson landed without it (B); income toasts; `BUILD` pulse when affordable; greyed rows with shortfall (§2.11.5) | A bought unit spawns and stands on the board carrying its unacted pip — the **event**, not the directive, so the row also confirms for a player who skipped guidance |
```

---

### Sweep result — every other frequency claim in §2.11.6-B, re-traced

Checked against the schedule table, cell by cell. These are correct as written
and are **not** edited:

| Sentence | Claim | Verdict |
|---|---|---|
| "The Turn column is the beat's **order index** … not a floor … beat 3 takes turn 2 in the fast-lane branch" | Beat 3 can appear before its index | Matches the table's fast-lane turn-2 cell |
| "A beat gives up the line either the instant it retires … or at the end of the turn it first appeared, whichever comes first" | Yield rule | Names the *first* yield; rule 2's later return is a fresh selection, not an exception. Gate-verified, untouched |
| "Rule 2 then makes turn 4 a last call for whatever is still outstanding" | Turn-4 behaviour | Matches all three turn-4 cells |
| "How to read a cell" note — "*this beat — or, if it has already retired, the next beat rules 1–2 select — or nothing*" | Cell semantics | Gate-verified; it is what makes the twice/once/never split above legible |
| "The earliest that can occur is the end of turn 1, and only in the fast-lane branch with a turn-1 build" | Strip-gone earliest | Gate-verified. 1a on the move, 1b on the turn boundary, beat 2 on a turn-1 pip, beat 3 on a turn-1 build — four retires inside turn 1 |
| "A **turn-4** last-call line … renders on turn 4 only" | Tag frequency | Matches the table's `untagged` fast-lane turn-3 cell and the three tagged turn-4 cells |
| "The strip disappears for good once all four beats have retired, and unconditionally at the end of turn 4" | Disappearance | Gate-verified |

The only frequency claims that were wrong were the three above, and all three
were the same claim written three times: that a beat's time on the line is
fixed at one turn.

## Change requests

None. Every fix is a description correcting itself against rules and numbers
that already exist — this section's own rules 1–2 and schedule table, §2.4's
Move 3, §2.13.1's lane table. No rule, cost, stat, or map value moves, and
nothing in another author's lane is touched.

## Open questions for the Director

1. **Q27 — Is gating End Turn during beat 1a presentation or rule?** *(new; the
   register runs Q1–Q26, so this is the next free ID. Entry text for §4.7
   below.)*

   > **Q27.** During beat 1a of a guided opening only, End Turn is inert until
   > the marked Infantry (`guidedOpening.infantry`) has moved; hover reads
   > `Move the marked Infantry first.` It is scoped to the first match, dies
   > with `Skip guidance`, and never applies outside the guided window.
   > **Reading in force (conservative):** it ships as specified, because the
   > §2.11.6-B schedule table's turn-1 row is unconditional in all three
   > branches only if 1a cannot outlive turn 1. **Blocks:** nothing today —
   > the directive-strip stub asserts the turn-1 row, so a ruling of "no input
   > gating" would require that assertion to be re-derived. **If ruled the
   > other way:** a player who ends turn 1 without moving leaves 1a
   > outstanding, and rule 1 hands the strip to 1b (`End turn.`) — an
   > instruction they have just followed — so the fallback is to let 1a expire
   > silently at the turn boundary like 1b, and the turn-1 row gains a
   > footnote.

   I am filing it rather than dropping it because a gate now leans on it. If
   you read UI input gating inside an onboarding window as squarely
   presentation, rule it so and Q27 closes the same day it opens.

2. **Should the guided opening be shipped-map-only?** Raised last round,
   unruled, still not blocking — recorded here so it is not lost, not to press
   it. *The Causeway* is match 9–10 (§2.13.4), by which point any completed
   match on the save has switched guidance off, so the fast-lane branch is
   reachable only for a player who starts there directly or clears the save.
   Keeping it specified is what let this violation be found at all — the branch
   is where beat 2's "never" case lives. If you would rather declare the guided
   opening shipped-map-only, the fast-lane column collapses to a footnote and
   the twice/once/never split in V1 collapses to twice/once. I recommend
   keeping it.

## Handoffs

- **`tech-director`** — two items. (1) §4.7's register is yours: **Q27** needs
  the entry quoted above, or a note that the Director ruled it presentation and
  it never opens. (2) The directive strip's assertion set is now stated in
  outcome form and is directly testable: for each of the three branches, beat 2
  holds the line **twice / once / never**, and the invariant across all
  branches is *no beat reaches the end of turn 4 outstanding without having
  held the line at least once*. That last line is the one worth pinning, and it
  is the one V1-b restates in the doc.
- **`scenario-designer`** — no action. Nothing here re-measures a lane. V1-c
  now cites *Ferrum Crossing*'s 5 MP / 5 MP by name as the reason a turn-1 pip
  is impossible there, so if a future redraw drops either shipped lane to 3 MP
  the shipped map moves into the fast-lane branch and V1-c's scope sentence
  must be struck. Flagging the dependency, not requesting a change.
- **`rules-designer`** — no request. Capture N = 1 remains an assumption in
  force under Q4; beat 2 retires on the pip either way, so an N = 2 ruling
  changes none of the three branch counts.

## Grounding

| Decision | Mechanic it serves |
|---|---|
| Beat 2's row states twice / once / never instead of a ceiling | Rules 1–2 (§2.11.6-B): rule 1 gives beat 2 turn 2, rule 2 can return it on turn 4. The row now enumerates the outcomes the schedule table generates instead of asserting a bound the table breaks. |
| The row states outcomes and not the yield mechanism | The yield rule ("at the end of the turn it first appeared") is gate-verified and unchanged; a second statement of it in a table cell is what drifted last time. |
| "No beat expires unheard" replaces "every beat gets its own turn" | The strip's actual purpose: a beat that retires on its event has already taught its concept (§2.11.6-D confirms on events, not directives). Only an *outstanding* beat needs the line, and rule 2 guarantees it one. |
| V1-c scoped to *Ferrum Crossing* | §2.13.1's lane table: 5 MP West, 5 MP East, against Infantry Move 3 (§2.4) — two turns minimum, so no turn-1 pip, so beat 2 must take turn 2 on the shipped map and only there. |
| "Two turns on the line at the outside" said in the standing-directive paragraph | That paragraph is where a reader goes to ask "how much strip time does a slow walk cost beat 3?" The answer is the ceiling, so the ceiling belongs there. |
| End Turn gate cited as pending Q27 | Teach-by-constraint (§2.11.6 philosophy) plus the turn-1 row's unconditionality. It gates an input, so it is registered rather than assumed. |
| §2.11.6-D's beat 3 cell reworded | Beat 3 retires on a spawn **event** and Fame ≥ 100 from turn 1 (§2.7, 200 start), so an early build retires it before it holds the line. The ledger row confirms on the spawn either way. |
| Schedule table untouched | Gate re-traced all twelve cells and the strip-gone condition. The table is the authority these sentences are being corrected against. |
