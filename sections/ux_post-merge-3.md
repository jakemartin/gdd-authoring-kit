> # ✅ APPLIED ADDENDUM — DO NOT RE-APPLY
>
> Every replacement pair in this file **has been applied to the master GDD**, and
> the master has moved on since. Its Old blocks no longer match, so re-applying is
> a no-op at best; its quoted "current" text, register extents, and any hash it
> names are a **snapshot of the moment it was written**, not the current state.
>
> **The master GDD is the source of truth** — read `source/gdd.md`. Further changes
> to a merged section go in a *new* addendum file.

# UX, UI & onboarding — post-merge-3 fix draft (ux-onboarding-designer)

## Placement

Both violations sit inside **§2.11.6-B (Guided opening, turns 1–4)** of the
merged master. Four of the five edits below are the fix for Violation 1
(schedule table vs. selection rules); the fifth is the fix for Violation 2
(stretch-map slack figure). No text outside §2.11.6-B is touched. No rule,
cost, or stat is changed: Infantry Move 3 (§2.4), the 6 MP reachability budget
and *Ferrum Crossing*'s 5/5 (§2.13.1), and capture N = 1 under Q4 all stand as
written and are cited, not restated differently.

## Draft

Five exact old→new pairs. Apply in file order.

---

### V1-a — the "earliest turn" claim (§2.11.6-B, sentence introducing rules 1–2)

The existing sentence says the Turn column is the *earliest* turn a beat can
appear. Rule 1 already breaks that: in the fast-lane branch beat 3 takes the
line on turn 2, one turn before its listed number. The column is an order
index, not a floor.

**OLD**

```
The Turn column is the *earliest* turn a beat can appear.
```

**NEW**

```
The Turn column is the beat's **order index** — the turn it takes the line in the common case — not a floor. Rules 1–2 below assign the line, so a beat moves up whenever a lower-numbered beat has already retired: beat 3 takes turn 2 in the fast-lane branch of the schedule table.
```

---

### V1-b — beat table, rows 1a and 2

Two cells to fix. **Row 1a:** the schedule table's turn-1 row is identical in
all three branches, and that is only true if 1a and 1b cannot outlive turn 1.
1b's retire condition is the turn boundary itself, so it cannot; 1a can, if the
player ends the turn without moving — which would strand rule 1 on beat 1b
(`End turn`) for a player who has not yet moved. The guided opening closes that
by constraint, which is how the rest of this section teaches: End Turn is inert
until the marked Infantry has moved. **Row 2:** its retire cell claims beat 2
"occupies the line for turn 2 only." In the fast lane the pip lands on turn 1
and beat 2 never holds the line at all.

**OLD**

```
| 1a | Only one marked Infantry selectable; others dimmed (hover: `Locked this turn.`) | `Select the marked Infantry. Lit hexes are its true reach. Click one to move.` | Selection; the highlight is the real move set (§2.5) | Move completes |
| 1b | End Turn pulses | `End turn. The enemy moves; then you.` | IGOUGO (§2.1) — the player watches a full AI turn | Enemy turn ends |
| 2 *(standing)* | None on selection. The scenario's designated neutral factory (`guidedOpening.objective`, §2.13.1) is ringed from turn 1; its info-panel line appends `Only Infantry captures.` | `Move the Infantry onto the ringed Factory. Only Infantry captures.` | Capture; the Infantry-only rule (§2.7) | A capture pip appears — on whatever turn that happens. *Standing* means it stays **outstanding**, not that it holds the strip: it occupies the line for turn 2 only, then yields and runs on the ring and the unit marker. Hard-expires at end of turn 4 |
| 3 | None. Fame ≥ 100 guaranteed by 200 start + home income (§2.7) | `Spend Fame at your Factory. Infantry costs 100.` | Fame → factory → unit | A unit spawns |
```

**NEW**

```
| 1a | Only one marked Infantry selectable; others dimmed (hover: `Locked this turn.`). End Turn is inert until that Infantry has moved (hover: `Move the marked Infantry first.`) — this is what makes 1a retire inside turn 1 in every branch | `Select the marked Infantry. Lit hexes are its true reach. Click one to move.` | Selection; the highlight is the real move set (§2.5) | Move completes |
| 1b | End Turn pulses | `End turn. The enemy moves; then you.` | IGOUGO (§2.1) — the player watches a full AI turn | Enemy turn ends |
| 2 *(standing)* | None on selection. The scenario's designated neutral factory (`guidedOpening.objective`, §2.13.1) is ringed from turn 1; its info-panel line appends `Only Infantry captures.` | `Move the Infantry onto the ringed Factory. Only Infantry captures.` | Capture; the Infantry-only rule (§2.7) | A capture pip appears — on whatever turn that happens. *Standing* means it stays **outstanding**, not that it holds the strip: it occupies the line for **at most one turn** — turn 2 in the common case, and not at all if the pip has already landed (fast lane) — then yields and runs on the ring and the unit marker. Hard-expires at end of turn 4 |
| 3 | None. Fame ≥ 100 guaranteed by 200 start + home income (§2.7) | `Spend Fame at your Factory. Infantry costs 100.` | Fame → factory → unit | A unit spawns — on whatever turn that happens, including turn 1 |
```

---

### V1-c — the schedule table itself, plus a reading note

The reported hole: the fast-lane turn-4 cell reads `strip quiet`
unconditionally. Traced against the rules — pip on turn 1 retires beat 2; beat
3 takes the line on turn 2 under rule 1; turn 3 is a rule-2 last call; if the
player still has not bought a unit, beat 3 is *still outstanding* on turn 4 and
rule 2 puts it back on the line, exactly as the common-case column shows for
its own turn 4. The cell is replaced. Every other cell was re-traced the same
way; the second correction that fell out is that **"strip quiet" is not a state
this system has at all** — rule 2 has no exit while any beat is outstanding, so
the only empty strip is a *gone* strip, and that requires all four beats
retired. Both instances of the phrase are therefore removed, and the column
header is corrected per V1-d/V2 (only *The Causeway*'s 3 MP lanes let an
Infantry at Move 3 reach the objective in one turn; *Longwater March*'s 4 MP
lanes cannot).

**OLD**

```
| Turn | Common case — pip lands turn 2 | Wandered case — pip lands turn 3 or 4 | Fast lane — pip lands turn 1 (stretch maps) |
|---|---|---|---|
| 1 | 1a, then 1b when 1a retires | 1a, then 1b | 1a, then 1b; beat 2 may retire here |
| 2 | beat 2 — retires on the pip | beat 2 — holds, then yields | beat 3 (rule 1) |
| 3 | beat 3 | beat 3 | beat 3 last call, or strip quiet |
| 4 | beat 3 last call, or strip quiet | beat 2 last call | strip quiet |
| end of 4 | strip gone; all beats expire | strip gone; all beats expire | strip gone; all beats expire |
```

**NEW**

```
| Turn | Common case — pip lands turn 2 | Wandered case — pip lands turn 3 or 4 | Fast lane — pip lands turn 1 (*The Causeway*, 3 MP lanes) |
|---|---|---|---|
| 1 | 1a, then 1b when 1a retires | 1a, then 1b | 1a, then 1b; the pip lands inside this turn, so beat 2 retires **without ever holding the line** |
| 2 | beat 2 (rule 1) — retires on the pip | beat 2 (rule 1) — holds, then yields | beat 3 (rule 1) |
| 3 | beat 3 (rule 1) | beat 3 (rule 1) | beat 3 — rule 2 last call, **untagged** |
| 4 | beat 3 — rule 2 last call, tagged | beat 2 — rule 2 last call, tagged | beat 3 — rule 2 last call **again**, tagged |
| end of 4 | strip gone; anything still outstanding expires | strip gone; anything still outstanding expires | strip gone; anything still outstanding expires |

**How to read a cell.** Each cell names the beat that rules 1–2 select for that turn, given the column's pip timing *and* beat 3 still outstanding when its cell is reached. Beat 3 retires on a spawn **event**, not on turn 3, and Fame ≥ 100 from turn 1, so a player who builds early retires it early. Every cell is therefore read as: *this beat — or, if it has already retired, the next beat rules 1–2 select — or nothing, if none is outstanding.* Turn 1 is identical in all three columns because 1a and 1b cannot outlive it: End Turn stays inert until the marked Infantry moves (beat table, row 1a), and 1b's retire condition **is** the turn boundary.

**Is the strip ever quiet before the end of turn 4?** No — there is no live-but-blank strip in this system. Rule 2 has no exit: while any beat is outstanding, some beat holds the line. The only empty state reachable before end of turn 4 is the strip being **gone**, and its condition is exact — *all four beats retired*: 1a and 1b inside turn 1, beat 2 on its pip, beat 3 on a spawn. The earliest that can occur is the end of turn 1, and only in the fast-lane branch with a turn-1 build; it is permanent, per the disappearance rule below, not a pause. In particular, fast-lane turn 4 is **not** unconditionally quiet: a player who has not bought a unit still has beat 3 outstanding, and rule 2 returns it to the line, exactly as the common-case column does at its own turn 4. That is the guarantee working, not an exception to it.
```

---

### V1-d — the last-call tag is a fact about the window, not about rule 2

The corrected table fires a rule-2 last call on turn 3 in the fast lane. The
tag reads `guidance ends this turn`, which is false on turn 3 — and a warning
that mis-states when it will be honoured is worse than no warning. Bind the tag
to the turn number.

**OLD**

```
A last-call line is the beat's own text with a dim right-hand tag, so the player is never dropped mid-instruction without warning:
```

**NEW**

```
A **turn-4** last-call line is the beat's own text with a dim right-hand tag, so the player is never dropped mid-instruction without warning. The tag states a fact about the *window*, not about rule 2, so it renders on turn 4 only: an earlier rule-2 last call (fast lane, turn 3) shows the same line untagged, because guidance does not end that turn and the strip must not say it does:
```

---

### V2 — stretch-map slack figure (§2.11.6-B against §2.13.1)

"2–4" is a pre-redraw figure. Both stretch maps were redrawn on even row
counts — *Longwater March* 13 × 8 and *The Causeway* 9 × 8, both `rot180` — and
their lanes now price at 4 MP / 4 MP and 3 MP / 3 MP against the 6 MP budget
(§2.13.1's table). Slack is 2 and 3; no lane on either 8-row map produces 4.
*Ferrum Crossing*'s 1 MP remains the tightest, so the surrounding sentence's
claim and the whole "walking off the lane pushes the pip to turn 3" argument
that follows it are unaffected.

**OLD**

```
Against the 6 MP budget that is **1 MP of slack**, the tightest of the three maps (§2.13.1's table; the stretch maps carry 2–4).
```

**NEW**

```
Against the 6 MP budget that is **1 MP of slack**, the tightest of the three maps and the only one that is tight at all: both stretch maps were redrawn on even row counts (*Longwater March* 13 × 8, *The Causeway* 9 × 8, both `rot180`), and their lanes price at **4 MP / 4 MP** and **3 MP / 3 MP**, so they carry **2** and **3** MP of slack respectively (§2.13.1's table). No lane on either 8-row map carries 4.
```

---

### Consequence worth naming (no edit required)

The corrected slack figures are also what fix the fast-lane column header.
A turn-1 pip needs a lane costing ≤ Infantry Move 3 (§2.4) and *The Causeway*
is the only map whose lanes are 3 MP; *Longwater March* at 4 MP needs two turns
of movement like the shipped map, and therefore runs the **common case**, not
the fast lane. The two violations were one drift with two faces: the stale
"2–4" is what let the header say "stretch maps" plural, and the plural is what
made the fast-lane branch look like an odd corner rather than a branch worth
tracing to turn 4.

## Change requests

None. Both fixes are internal to §2.11.6-B, and both were resolved by making my
own text agree with rules and numbers that already exist — §2.13.1's lane table,
§2.4's Move 3, and this section's own selection rules 1–2. Nothing outside my
lane moves.

## Open questions for the Director

1. **Is gating End Turn during beat 1a presentation or rule?** V1-b adds one
   guided-opening constraint: End Turn is inert until the marked Infantry has
   moved. It is scoped to beat 1a of the first match, dies with
   `Skip guidance`, and it is the condition that makes the schedule table's
   turn-1 row unconditional in all three branches — without it, a player who
   ends turn 1 without moving leaves 1a outstanding and rule 1 hands the strip
   to 1b (`End turn`), an instruction they have just followed. I read this as
   UI gating inside a section I own, so I have not filed it as a Q. If you read
   input gating as a rule, the next free number is **Q26** and I will restate
   it there rather than in §2.11.6-B.
2. **Does the fast-lane branch survive scenario order?** *The Causeway* is
   match 9–10 (§2.13.4), by which point any completed match on the save has
   already switched guidance off. The branch is therefore reachable in practice
   only for a player who starts on *The Causeway* directly, or clears the save.
   Keeping it specified costs nothing and makes the table auditable, but if you
   would rather the guided opening be declared shipped-map-only, say so and the
   column collapses to a footnote.

## Handoffs

- **`scenario-designer`** — no action. This draft consumes your redraw
  (13 × 8 / 9 × 8, 4/4 and 3/3 MP) as the authority and cites §2.13.1 rather
  than restating it. One thing to be aware of: *The Causeway*'s 3 MP lanes make
  its guided opening a **one-turn** capture, which is the only place the
  onboarding branches on map geometry. If a future redraw moves either
  Causeway lane to 4 MP, the fast-lane column stops being reachable and the
  header in V1-c should be struck.
- **`tech-director`** — the directive strip's line assignment is now fully
  specified as a per-turn selection over an outstanding set: rules 1–2, four
  beats, event-based retire conditions, tag rendered on turn 4 only, widget
  destroyed when the outstanding set empties or the turn-4 boundary passes.
  That is a small enough state machine to be a gateable stub if you want one;
  the assertion worth testing is the guarantee itself — *no beat reaches end of
  turn 4 outstanding without having held the line at least once*.
- **`rules-designer`** — no request. Capture N = 1 stays an assumption in force
  under Q4 and the directive still retires on the pip, so a ruling of N = 2
  changes nothing here.

## Grounding

| Decision | Mechanic it serves |
|---|---|
| Fast-lane turn 4 = beat 3 last call, not quiet | Rule 2 (§2.11.6-B): while a beat is outstanding, it takes the line. The turn-4 cell now matches the rule that generates it. |
| "Strip gone", never "strip quiet" | The disappearance rule already in §2.11.6-B — the strip dies when all four beats retire, or at end of turn 4. A blank live strip was never a defined state. |
| Every cell read as "this beat, or the next rules 1–2 select, or nothing" | Beat 2 and beat 3 retire on **events** (pip, spawn), not turn numbers, and 200 starting Fame (§2.7) makes a turn-1 build legal. |
| End Turn inert during beat 1a | Teach-by-constraint (§2.11.6 philosophy) and the turn-1 row's unconditionality. 1b's directive must never be shown to a player who has not yet moved. |
| Last-call tag on turn 4 only | The tag's own text, `guidance ends this turn`, is a claim about the four-turn window (§2.11.6-B, §2.13.1). |
| Stretch slack = 2 and 3, not 2–4 | §2.13.1's lane table post-redraw: *Longwater March* 4/4 MP, *The Causeway* 3/3 MP, against the 6 MP budget from 2 × Infantry Move 3 (§2.4). |
| Fast lane = *The Causeway* only | A turn-1 pip requires a lane ≤ 3 MP (§2.4 Move 3); only *The Causeway*'s 3 MP lanes qualify. |
| *Ferrum Crossing* stays the tightest at 1 MP | §2.13.1's 5 MP West and 5 MP East, gate-reconfirmed; the beat-2 standing-directive argument depends on it and is unchanged. |
