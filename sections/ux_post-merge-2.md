> # ✅ APPLIED ADDENDUM — DO NOT RE-APPLY
>
> Every replacement pair in this file **has been applied to the master GDD**, and
> the master has moved on since. Its Old blocks no longer match, so re-applying is
> a no-op at best; its quoted "current" text, register extents, and open items are
> a **snapshot of the moment it was written**, not the state of the document.
>
> Specifically: its CR-1 was routed and applied by the Director, so the Open-questions item asking how to route it is closed — and CR-1's own OLD text would now *revert* §2.13.1's turns-1–4 window if re-applied.
>
> **The master GDD is the source of truth** — read `source/gdd.md`. Further changes
> to a merged section go in a *new* addendum file.

# UX, UI & onboarding — post-merge-2 draft (ux-onboarding-designer)

> **Form: addendum of replacement passages.** This file is *not* a section
> draft and does not restate §2.11. It contains exact **old → new** passage
> pairs against `source/gdd.md` (md5 `0eedea2dfd7b17a508e162427682ce64`),
> each keyed to the line it replaces in the merged master. Apply the pairs;
> nothing else in §2.11 or §2.13 changes.
>
> **`sections/ux.md` is superseded and must not be re-merged.** Everything
> below supersedes it where they overlap.
>
> **No rule or number changes.** Infantry Move 3 (§2.4), the 6 MP lane budget
> and §2.13.1's measured 5/5 MP on *Ferrum Crossing*, and capture N = 1 as an
> assumption in force under Q4 are all untouched. The open-question register
> stays at **Q1–Q23**; this fix needs no new Q.

## Placement

Six replacement passages, all inside already-merged text:

| # | Target | Address in `source/gdd.md` | Violation it closes |
|---|---|---|---|
| R1 | §2.11.6 intro | line 586 | 1 (window) |
| R2 | §2.11.6-B heading | line 590 | 1 (window) |
| R3 | §2.11.6-B table, beat 2 row | line 596 | 2 (starvation) |
| R4 | §2.11.6-B, the strip-ordering paragraph | line 599 | 2 (starvation) |
| R5 | §2.11.6-B, "Why beat 2 is a standing directive" — closing sentences | line 603 | 1 + 2 |
| R6 | §2.11.6-D, "Fame income & build" row | line 621 | 2 (reachable confirmation) |

Plus **CR-1** below: §2.13.1 bullet "Opening-capture reachability", point 2
(line 722) — inside the scenario-designer's section, filed as a change
request rather than applied.

**The window I settled on: the guided opening runs turns 1–4.** §1.6 row 2's
"a scripted turn-1–3 guided opening" should read "a scripted four-turn guided
opening (turns 1–4)". Per instruction I have written no replacement for §1.6.

## Draft

### The decision behind both fixes, in one paragraph

The window is **turns 1–4**, not 1–3, because turn 4 is already the real edge
of guidance in the merged text: beat 2 hard-expires there and the strip
disappears there unconditionally. Naming the window 1–3 while the surface
lives to turn 4 was the contradiction; extending the name is the cheaper
reconciliation than pulling the expiry back to turn 3, which would reopen the
*Ferrum Crossing* 1-MP-slack problem the standing directive exists to absorb.

The starvation is real and I am not rewording it. **Beat 2 stops competing for
the strip after one turn.** A beat *holding the line* and a beat *being
outstanding* are separated: beat 2 holds the line for turn 2, then yields it
whether or not the pip has landed, and continues to run as **board state** —
the ringed objective and the marked Infantry, both already on screen since
turn 1 and both already specified. Beat 3 therefore always gets turn 3. The
instruction is not lost when the line is yielded, because for beat 2 the
instruction was always spatial: a ring around one hex and a marker on one
unit. The text line was the introduction, not the reminder.

Belt-and-braces, R6 also re-anchors §2.11.6-D's "Fame income & build"
confirmation on the **spawn event** rather than on "the turn 3 directive
completes", so that row is reachable even for a player who skipped guidance
entirely. Both halves of the Director's option list, because the scheduling
fix makes the lesson reachable and the re-anchor makes the *ledger* independent
of scheduling.

---

### R1 — §2.11.6 intro (line 586)

**OLD**

> The first match runs on the one shipped scenario at **Easy** by default (player +150 opening Fame, §2.9) with a **guided opening**: scripted directives across turns 1–3, then hands-off. Any completed match on the save skips all guidance automatically; a `Skip guidance` control kills it instantly for anyone.

**NEW**

> The first match runs on the one shipped scenario at **Easy** by default (player +150 opening Fame, §2.9) with a **guided opening**: four scripted directives inside a fixed four-turn window — the first appears on turn 1, the strip and every beat behind it are gone for good at the end of turn 4, then hands-off. Any completed match on the save skips all guidance automatically; a `Skip guidance` control kills it instantly for anyone, and kills the guided opening's board state with it — the objective ring and the turn-1a unit marker clear in the same frame as the strip.

---

### R2 — §2.11.6-B heading (line 590)

**OLD**

> **B. Guided opening (turns 1–3), via a one-line directive strip** at top center, one instruction at a time, each retiring on completion:

**NEW**

> **B. Guided opening (turns 1–4), via a one-line directive strip** at top center, one instruction at a time, each retiring on completion:

---

### R3 — §2.11.6-B table, beat 2 row (line 596)

**OLD**

> | 2 *(standing)* | None on selection. The scenario's designated neutral factory (`guidedOpening.objective`, §2.13.1) is ringed from turn 1; its info-panel line appends `Only Infantry captures.` | `Move the Infantry onto the ringed Factory. Only Infantry captures.` | Capture; the Infantry-only rule (§2.7) | A capture pip appears — on whatever turn that happens; hard-expires at end of turn 4 |

**NEW**

> | 2 *(standing)* | None on selection. The scenario's designated neutral factory (`guidedOpening.objective`, §2.13.1) is ringed from turn 1; its info-panel line appends `Only Infantry captures.` | `Move the Infantry onto the ringed Factory. Only Infantry captures.` | Capture; the Infantry-only rule (§2.7) | A capture pip appears — on whatever turn that happens. *Standing* means it stays **outstanding**, not that it holds the strip: it occupies the line for turn 2 only, then yields and runs on the ring and the unit marker. Hard-expires at end of turn 4 |

---

### R4 — §2.11.6-B, the strip-ordering paragraph (line 599)

**OLD**

> The Turn column is the *earliest* turn a beat can appear; the strip shows one directive at a time, oldest outstanding first, so a beat that retires early simply advances the next one. The strip disappears for good once all four beats have retired, and unconditionally at the end of turn 4.

**NEW**

> The Turn column is the *earliest* turn a beat can appear. The strip shows **one directive at a time**, and the line is assigned at the start of each turn by two rules in order:
>
> 1. the lowest-numbered **outstanding** beat that has **not yet held the line on an earlier turn**;
> 2. if every outstanding beat has already had its turn on the line, the lowest-numbered outstanding beat — a **last call**.
>
> A beat gives up the line either the instant it retires (which is how 1a hands off to 1b inside turn 1) or at the end of the turn it first appeared, whichever comes first. **Giving up the line is not retiring.** An outstanding beat that has yielded keeps running on its board state: for beat 2 that is the ringed objective and the marked Infantry, which are the same instruction in spatial form and have been on screen since turn 1. The text line introduces the objective; the ring is what reminds.
>
> The consequence that matters: **every beat is guaranteed its own turn on the strip.** A beat 2 that hangs — the *Ferrum Crossing* 1-MP-slack case below — cannot starve beat 3, whose Fame → factory → unit lesson is the one the §2.11.6-D ledger confirms with a bought unit on the board. Rule 2 then makes turn 4 a last call for whatever is still outstanding, so the strip's final turn is spent on the player's actual gap rather than on order-of-arrival:
>
> | Turn | Common case — pip lands turn 2 | Wandered case — pip lands turn 3 or 4 | Fast lane — pip lands turn 1 (stretch maps) |
> |---|---|---|---|
> | 1 | 1a, then 1b when 1a retires | 1a, then 1b | 1a, then 1b; beat 2 may retire here |
> | 2 | beat 2 — retires on the pip | beat 2 — holds, then yields | beat 3 (rule 1) |
> | 3 | beat 3 | beat 3 | beat 3 last call, or strip quiet |
> | 4 | beat 3 last call, or strip quiet | beat 2 last call | strip quiet |
> | end of 4 | strip gone; all beats expire | strip gone; all beats expire | strip gone; all beats expire |
>
> A last-call line is the beat's own text with a dim right-hand tag, so the player is never dropped mid-instruction without warning:
>
> ```
> +--------------------------------------------------------------------------+
> |  Move the Infantry onto the ringed Factory. Only Infantry captures.      |
> |                                                    guidance ends this turn|
> +--------------------------------------------------------------------------+
> ```
>
> The strip disappears for good once all four beats have retired, and unconditionally at the end of turn 4; every beat, the objective ring, and the turn-1a marker expire with it.

---

### R5 — §2.11.6-B, closing sentences of "Why beat 2 is a standing directive" (line 603)

Replace only the final two sentences of that paragraph. Everything before
"The standing directive absorbs precisely that" is unchanged.

**OLD**

> The standing directive absorbs precisely that: it appears on turn 2, persists until the pip appears, and hard-expires at end of turn 4, one turn past the guided window. Ringing the objective from turn 1 biases beat 1a's free move onto the lane without constraining it, so in the common case the slack is never spent and the pip lands on turn 2 as designed.

**NEW**

> The standing directive absorbs precisely that: it appears on turn 2, stays outstanding until the pip appears, and hard-expires at the end of turn 4 — the last turn of the guided window, not one turn past it. It persists as an *objective*, not as a line of text: it holds the strip for turn 2, yields the line to beat 3 for turn 3, and returns for a turn-4 last call only if the pip still has not landed. That is the whole price of "standing", and it is paid in ring and marker rather than in strip time, so the Fame → factory → unit lesson is never the thing that gets crowded out by a slow walk. Ringing the objective from turn 1 biases beat 1a's free move onto the lane without constraining it, so in the common case the slack is never spent and the pip lands on turn 2 as designed.

---

### R6 — §2.11.6-D, "Fame income & build" row (line 621)

**OLD**

> | Fame income & build | Fame is abstract; player hoards, never connects factories → army | Income toasts; `BUILD` pulse when affordable; greyed rows with shortfall (§2.11.5) | Turn 3 directive completes: a bought unit stands on the board |

**NEW**

> | Fame income & build | Fame is abstract; player hoards, never connects factories → army | Beat 3, which is guaranteed its own turn on the strip (B); income toasts; `BUILD` pulse when affordable; greyed rows with shortfall (§2.11.5) | A bought unit spawns and stands on the board carrying its unacted pip — the **event**, not the directive, so the row also confirms for a player who skipped guidance |

**Reachability check on the two rows the gate named.** *Capture* row (line 620)
is unchanged and needs no change: its confirmation is `Pip → tile recolors →
next turn's +100 Fame — Factory toast`, a board-and-toast chain that never
referenced the strip. Under Q4's N = 1 assumption in force the pip lands at
end of turn 2 and the toast on turn 3; if the pip slips to turn 4 the toast
falls outside the guided window, which is correct — the toast is a permanent
game surface, not onboarding, and it fires whenever the flip happens.
*Fame income & build* row is now confirmed by the spawn event under R6 and is
additionally reachable through beat 3's guaranteed turn 3 under R4. Both rows
are reachable in every branch of the schedule table.

---

### Build note (unchanged cut line)

R4 is not new scaffolding. The strip already tracks four beats; this adds one
boolean per beat — `hasHeldLine` alongside the existing `retired` — and turns
directive selection into a min over ≤ 4 entries evaluated once at turn start.
The last-call tag is one more `TextBlock` in the existing strip widget.
§2.11.8's must-have list ("directive strip with the four beats") already covers
it and needs no edit.

## Change requests

| Existing § | Current text | Proposed change | Why |
|---|---|---|---|
| §2.13.1, "Opening-capture reachability", point 2 (line 722) | "2. **Slack is not uniform.** *Ferrum Crossing* carries only 1 MP of slack against the 6, so a turn-1 move spent walking away from the lane pushes the pip to turn 3 — still inside the guided window (turns 1–3). The stretch maps carry 2–4 MP of slack." | "2. **Slack is not uniform.** *Ferrum Crossing* carries only 1 MP of slack against the 6, so a turn-1 move spent walking away from the lane pushes the pip to turn 3 — still inside the guided window, which runs **turns 1–4** (§2.11.6-B). The stretch maps carry 2–4 MP of slack." | Third of the three statements the gate cited. The passage sits in the scenario-designer's §2.13, so it is filed rather than applied — no measured MP value, lane, or map fact changes; only the parenthetical window name. |
| §1.6, row 2 (line 69) | "a scripted turn-1–3 guided opening" | Director-owned. The window is **turns 1–4**; no replacement drafted, per instruction. | Same reconciliation, Director's prose. |

## Open questions for the Director

1. **Confirm the window as turns 1–4**, then align §1.6 row 2 and apply CR-1.
   The alternative — pulling the strip's expiry back to end of turn 3 to
   preserve the 1–3 name — is available but costs the *Ferrum Crossing*
   wandered-player case the design already paid for; I recommend against it.
2. **The turn-4 last call**: I kept it and defused the "dropped mid-instruction"
   objection with the `guidance ends this turn` tag rather than by going quiet.
   If you would rather the strip simply fall silent on turn 4 whenever every
   outstanding beat has already had its turn, delete rule 2 in R4 and the
   wireframe with it; nothing else in the fix depends on it, and beat 3's
   guaranteed turn 3 survives either way.
3. **Routing of CR-1** — apply it yourself at merge, or send it through
   `scenario-designer` so §2.13 stays single-authored.
4. **No new Q number filed.** Nothing here needs a ruling: the fix changes
   only which turn a line of text occupies. If you disagree and want the
   yield behaviour recorded as a pending decision rather than a specification,
   it becomes **Q24** and the register moves to Q1–Q24.

## Handoffs

- **`tech-director`** — the directive strip's state is now, per beat:
  `retired: bool`, `hasHeldLine: bool`, plus the existing retire predicate.
  Selection is evaluated once at turn start (rule 1, then rule 2) and once
  more immediately on any retire, so 1a → 1b still hands off inside turn 1.
  Worth a line in the §4.7 stub that owns onboarding flags, and one
  acceptance case: *beat 2 outstanding at start of turn 3 ⇒ beat 3 holds the
  line on turn 3.* That case is the regression guard for this violation.
- **`scenario-designer`** — CR-1 only. No lane, MP value, or
  `guidedOpening.*` field changes; `guidedOpening.objective`'s ring now also
  carries beat 2's reminder after turn 2, which is a use of existing map data,
  not a new field.
- **`rules-designer`** — nothing. No rule, cost, or capture-timing claim is
  touched; Q4's N = 1 stays an assumption in force and R3's wording is still
  correct if it is ever ruled N = 2 (the pip is the arrival event either way).

## Grounding

| Decision | Mechanic it serves |
|---|---|
| Window named **turns 1–4** | Beat 2's hard expiry and the strip's unconditional expiry both already sit at end of turn 4 (§2.11.6-B); the name now matches the surface. |
| Beat 2 yields the line after one turn | §2.13.1's opening-capture invariant guarantees the lane at ≤ 6 MP but *Ferrum Crossing* leaves 1 MP of slack, so the pip can legitimately slip. Guidance absorbs the slip; it must not spend the whole window on it. |
| The ring and marker carry beat 2 after it yields | Both are specified from turn 1 and read from `guidedOpening.objective` / `guidedOpening.infantry` (§2.13.1). The reminder costs no new surface. |
| Beat 3 guaranteed turn 3 | §2.7 Fame income and the 200 opening Fame make Infantry (100) affordable by turn 3; §2.11.5's `BUILD` pulse and shortfall rows only teach if the player is pointed at the factory once. |
| Confirmation re-anchored on the spawn event | §2.7's spawn rule fires a visible, unmissable board event; anchoring the ledger there makes the row hold for skipped guidance too. |
| `guidance ends this turn` tag | The strip's disappearance is unconditional (§2.11.6-B); an unannounced disappearance mid-instruction would read as a bug, the same failure mode §2.11.6-D flags for silently blocked repair. |
