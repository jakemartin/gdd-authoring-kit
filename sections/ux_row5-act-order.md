> ## ✅ APPLIED ADDENDUM — DO NOT RE-APPLY
>
> All eleven pairs of this stage were merged into the master GDD on 2026-08-03,
> **together with** the other two files of round `row5-flags`:
> `sections/rules_row5-act-order.md` (2 pairs), `sections/tech_row5-act-order.md`
> (1 pair) and `sections/ux_row5-act-order.md` (8 pairs), applied in that order.
> Master md5 `7dc635b4f06589f89b46e2fa1b7ad86b` → `9742f695f71d625763d9a3eeef21e70b`.
>
> Gate: run `row5-flags-3`, **PASS**, 0 violations, after `row5-flags-1`
> (BLOCK, 4 — two on `rules`, one on `tech`, one on `ux`) and `row5-flags-2`
> (BLOCK, 1 — `ux` alone; `rules` and `tech` both PASS at 0 there and were not
> touched again).
>
> **This file applied third. Pairs 3 and 8 are insertions — their OLD anchors are
> retained deliberately.** Post-check on the merged master: every NEW present exactly
> once; pairs 3 and 8's OLDs present **once** each, the other six **zero** times.
> This file is **not safe to apply twice**.
>
> Pair 8 suppresses **both** routes into beat 1a's soft-lock for the marked Infantry
> — the SELECTED → attack transition and **Space** — a constraint the ruling created
> and which nothing in the round's brief pointed at.

# UX, UI & onboarding — row-5 act-order addendum (ux-onboarding-designer)

## Placement

An OLD/NEW addendum against `source/gdd.md` @ md5 `7dc635b4f06589f89b46e2fa1b7ad86b`.
Eight pairs, in file order: **§2.11.1**'s selection-state-machine lead-in (1),
its four-state block (1), its state-machine footnote (1), its input table's
hover-unit row (1); **§2.11.2**'s earn-your-pixels audit row for the unacted pip
(1) and its hovered-unit info-panel line (1); **§2.11.3**'s
forecast-availability sentence (1); **§2.11.6-B**'s beat-1a constraint cell (1).

Four Director rulings drive this file. The DONE bit is confirmed as read
(ruling 1), so pairs 5 and 6 and the DONE half of pair 3 are unchanged from the
first draft. The machine gains a direct **SELECTED → attack** transition
(ruling 2), which is pairs 2, 4, 7 and 8 and the rewritten first half of pair 3.
The flags clearing at the start of the owner's turn (ruling 3) falsifies nothing
here; pair 3 states DONE's own per-turn lifetime so the UI bit and the flags are
not left with unstated, differing lifetimes. §2.1's core-loop line is ruled into
this round (ruling 4), which is pair 1.

**Pair 1 removes a reproduction rather than correcting one.** §2.11.1's lead-in
reprised §2.1's written sequence inline. `rules-designer` is rewriting that line
in `sections/rules_row5-act-order.md` in this same sitting, so a corrected
reprise would be a fresh assertion in the same place, needing a fresh pair every
time §2.1 moves. Pair 1 therefore cites §2.1 and stops. Nothing in this file
reproduces, quotes or predicts that agent's new text.

**Pairs 2 and 8 close both doors into beat 1a's dead end.** Exactly two routes
run from SELECTED to DONE **without passing through MOVED** — the attack ruling 2
added, and Wait, which the input table has always granted from SELECTED and which
the fenced block did not list. Those are the two that can strand beat 1a, because
every other route to DONE runs through MOVED and therefore spends the move the
beat is waiting for. Pair 8 closes both for the marked Infantry while beat 1a is
outstanding; pair 2 adds the missing Wait transition to the block, because a
suppression of a transition the machine does not list cannot be read.

No pair states a rule. Pair 3 points at `T-TURN-01` (§4.7 Spec Stub 5) as the
invariant that owns the per-unit flags and the orderings they permit, and does
not reproduce or paraphrase that invariant's text either — `tech-director` is
rewriting it in the same sitting. `T-MOVE-03` is cited only for the fact
ruling 2 explicitly preserved: standing still is not a move, and the unit's own
hex does not join the lit reachable set.

---

## Pair 1 — §2.11.1, the selection-state-machine lead-in (replacement)

**OLD**

```
**Selection state machine.** The core loop (§2.1: select → move → act → done, any unit order) maps to four UI states:
```

**NEW**

```
**Selection state machine.** The core loop (§2.1) maps to four UI states. The loop's own sequence, and its list of what counts as an act, are §2.1's to state; this machine is the input surface for them and deliberately does not reprise them:
```

The parenthetical was a verbatim copy of §2.1's sequence living two sections
away from the line it copied. The citation is kept and the copy is dropped, so
this sentence cannot go stale again when §2.1 is edited. The trailing clause is
there so a later editor reads the absence as deliberate rather than as a missing
summary and restores the arrows.

## Pair 2 — §2.11.1, the four-state block (replacement)

**OLD**

```
IDLE ──LMB on own unacted unit──▶ SELECTED (reachable hexes lit, §2.5)
IDLE ──LMB on own factory──────▶ PRODUCTION MENU (§2.11.5)
SELECTED ──LMB on lit hex──────▶ MOVED (attack targets lit; Wait available)
SELECTED ──RMB / Esc───────────▶ IDLE (nothing committed)
```

**NEW**

```
IDLE ──LMB on own unacted unit──▶ SELECTED (reachable hexes lit, §2.5; attack targets lit)
IDLE ──LMB on own factory──────▶ PRODUCTION MENU (§2.11.5)
SELECTED ──LMB on lit hex──────▶ MOVED (targets relit from the new hex; Wait available)
SELECTED ──hover enemy target──▶ forecast card shown (§2.11.3)
SELECTED ──LMB on lit target───▶ attack resolves as forecast → unit DONE (move unspent)
SELECTED ──Space (Wait)────────▶ unit DONE without moving or acting
SELECTED ──RMB / Esc───────────▶ IDLE (nothing committed)
```

Two additions and two edits. The attack pair is ruling 2. The **Space** line is
not new behaviour — the input table's `Wait — mark the selected/moved unit done
without acting` has always granted it — but the block never listed it, and pair 8
now suppresses it for one unit, which is unreadable against a transition the
machine does not show. With it listed, the two routes from SELECTED to DONE that
skip the move are both on the diagram and both visibly enumerable.

The four MOVED lines below the anchor are untouched and stay byte-identical, so
the MOVED path — including the starred RMB/Esc line the move-undo footnote hangs
off — is unaffected. The state count is unchanged: this adds transitions, not a
fifth state, so pair 1's `maps to four UI states` still reads true.

## Pair 3 — §2.11.1, after the Q11 move-undo footnote (insertion)

**OLD**

```
The two behaviors share a UI; only the rules module differs.
```

**NEW**

```
The two behaviors share a UI; only the rules module differs.

**The machine is narrower than the rule, and that is deliberate.** `T-TURN-01` (§4.7 Spec Stub 5) owns the per-unit move and act flags and the orderings they permit; read them there, not off this diagram. The machine above reaches an attack two ways — after a move, or straight from SELECTED with the move unspent — and it retires the unit at the act either way, whatever that unit has left. What it does not offer is the reverse, a unit returning to the board after acting: an ordering the invariant permits is not on screen. This is a UI restriction and nothing more: no line here asks the rules module to refuse a command it would otherwise accept, and AI turns, headless runs and replays are untouched. It is also not provisional the way the move-undo note above it is — that note waits on an unruled question, this one scopes a ruled rule down to what one screen teaches. The cost is paid to keep the per-unit vocabulary at exactly two verbs (*attack* or *wait*, below) and the board at one per-unit state: the SELECTED attack is precisely the case that retires a unit with a flag to spare, and a unit that could come back for it needs a third pip state, a rule for what **Tab** does with it, and an explanation — in a first session already spending its attention on hexes, capture and the forecast (§2.11.6). Nothing announces the restriction to the player, by §2.11.6's first principle: the option is never offered, so there is nothing to un-learn.

**Standing still is never a move.** The unit's own hex does not join the lit reachable set (`T-MOVE-03`: a move never ends on an occupied hex), so SELECTED's two lit sets — reachable hexes and attack targets — are disjoint, and **LMB** on a lit hex is never ambiguous between moving and attacking. A unit that attacks from SELECTED has not moved; it has spent its act and been retired by this machine, not by the rules module.

**What DONE means, and what binds to it.** DONE is this machine's own per-unit bit — *this unit takes no further command this turn* — and it is not the act flag. It is per-turn: it clears when the owner's next turn begins. **Space** (Wait) and RMB/Esc in MOVED both reach DONE without acting, so the two bits come apart in ordinary play. Every surface in §2.11 that says a unit *has not acted* binds to the machine's bit: the `unacted unit` entry into SELECTED, the **Tab** cycle, the **Enter** confirm's count and its `3 units have not acted. End turn?` string, the idle count and the unacted pip (§2.11.2), and the spawned unit's pip in §2.11.6-D. Bound that way each of those stays literally true, because the machine retires a unit the instant it acts — so every unit still carrying a pip has in fact not acted. Bound to the act flag instead, a waited unit would keep its pip, answer **Tab**, and be counted in the End Turn confirm the player had just dismissed it from: a surprise the player caused and the UI then denied, which is the one thing §2.11 does not ship.
```

## Pair 4 — §2.11.1, input table, the hover-unit row (replacement)

**OLD**

```
| **Hover** unit | Unit stats in the info panel; if own MOVED unit has it in reach, the **forecast card** (§2.11.3) |
```

**NEW**

```
| **Hover** unit | Unit stats in the info panel; if an own SELECTED or MOVED unit has it in reach, the **forecast card** (§2.11.3) |
```

The row named MOVED as the only state a forecast can be read from. With the
attack reachable from SELECTED, that row would have hidden the card from exactly
the player who needs it most — the one deciding whether to move at all.

## Pair 5 — §2.11.2, earn-your-pixels audit, the unacted-pip row (replacement)

**OLD**

```
| Unacted pip on own units | Which units still have a move | §2.1 |
```

**NEW**

```
| Unacted pip on own units | Which units I can still give an order to | §2.1 per-unit loop, via the DONE bit of §2.11.1's machine |
```

The pip is one bit and ruling 1 makes *has a move left* and *has an act left*
two different facts, so the old decision text now names a fact the pip does not
carry — most sharply for the unit that attacked from SELECTED, which is retired
with its move flag untouched. What the pip has always supported is the decision
it is read for at End Turn: who is still mine to command. The Rule-surfaced
column keeps its bare `§2.1` citation and gains no reprise of that section's
text, for pair 1's reason.

## Pair 6 — §2.11.2, info panel, hovered unit (replacement)

**OLD**

```
- Hovered unit: name, HP as `12/20`, Atk/Def/Move/Range, `has acted` flag.
```

**NEW**

```
- Hovered unit: name, HP as `12/20`, Atk/Def/Move/Range, and `ready` or `done` — the machine's DONE bit (§2.11.1), not a raw flag name: a waited unit reads `done` while its act flag is unspent.
```

The panel is the durable home of a per-unit fact (§2.11's principle 3), so it is
the one surface where displaying the wrong bit is directly readable: under
ruling 1 a waited unit is retired with `has acted` false, and the old line would
have shown a greyed, pip-less unit alongside the word `no`.

## Pair 7 — §2.11.3, when the forecast card appears (replacement)

**OLD**

```
It appears on **hover** over any lit target from the MOVED state; **LMB commits**, RMB/Esc cancels.
```

**NEW**

```
It appears on **hover** over any lit target from either the SELECTED or the MOVED state (§2.11.1); **LMB commits**, RMB/Esc cancels. A commit from SELECTED spends the act with the move unspent and retires the unit all the same.
```

§2.11.3 is the section that calls the forecast the teaching instrument; gating it
on MOVED would have made the game teach *move before you look*, which is the one
lesson ruling 2 removes. This is also the sentence that makes §2.11.3's next
paragraph — `Selecting Artillery renders its attack ring as range 2–3` — read
literally rather than loosely: the ring is now lit in the state that sentence
names.

## Pair 8 — §2.11.6-B, beat 1a's constraint cell (insertion)

**OLD**

```
End Turn is inert until that Infantry has moved (hover: `Move the marked Infantry first.`)
```

**NEW**

```
End Turn is inert until that Infantry has moved (hover: `Move the marked Infantry first.`), and while 1a is outstanding that Infantry cannot retire itself without moving: its attack targets are not lit, so the SELECTED → attack transition (§2.11.1) is closed to it, and **Space** is inert for it on the same footing as End Turn and for the same reason. Those are the machine's only two routes from SELECTED to DONE that do not pass through MOVED, so both are closed for that one unit and nothing the player can do leaves End Turn inert with no move left to satisfy it
```

Beat 1a is the only guided-opening constraint that gates a player **input**, and
it gates it on the move flag. Every route by which the marked Infantry could
reach DONE without moving is a dead end: End Turn inert, 1a's retire condition
(`Move completes`) unreachable, and no other unit selectable. Ruling 2 opened one
such route; **Space** was the other, and had been open all along. Both are closed
here. The machine's remaining routes to DONE all run through MOVED, so each
spends the move that retires the beat and none of them can strand it. The fix is
a constraint, not a message, which is 1a's existing character — it already dims
every other unit — it adds no player-facing string, since Space goes inert on the
End-Turn hover already in this cell, and it leaves Q27's adopted gate and 1a's
retire condition exactly as ruled.

---

## Survey, anchor and overlap checks

Re-run over the current bytes of this file.

**Anchors.** Each OLD above was grepped against `source/gdd.md` and matched
**exactly once**.

**Classification by substring test.** Pair 3's NEW and pair 8's NEW each contain
their OLD verbatim as a prefix → **insertions**. Pairs 1, 2, 4, 5, 6 and 7 each
drop bytes their OLD carries — `: select → move → act → done, any unit order`;
the block's `SELECTED (reachable hexes lit, §2.5)` line and `MOVED (attack
targets lit; Wait available)` line; `if own MOVED unit`; `Which units still have
a move`; `` `has acted` flag. ``; `from the MOVED state` — so no NEW contains its
OLD → **replacements**. **6 replacements, 2 insertions.**

**Overlap.** The eight OLDs sit in eight paragraphs across four subsections and
share no bytes. Within §2.11.1, pair 1's anchor is the lead-in sentence above the
fence, pair 2's is the first four transition lines inside it, pair 3's is the
last sentence of the footnote below it, and pair 4's is a table row below that —
four disjoint regions in that order. Pairs are in ascending file order
throughout.

**Survey A — every §2.11 site that reproduces or depends on §2.1's written
sequence or its act list.** Grepped for the sequence, for the act list, and for
every `§2.1` citation in the section:

| Site | Verdict |
|---|---|
| §2.11.1, the selection-state-machine lead-in | **Paired** (pair 1). The only verbatim reproduction of §2.1's sequence anywhere in §2.11 — the other two matches in the document are §2.1 itself and `T-TURN-01` in §4.7, neither of them mine. |
| §2.11.1, `**Capture and build need no extra verbs.** Capture is by presence (§2.7 …). Building is the factory's own interaction, not a unit's.` | **Left.** It does not reproduce §2.1's act list, it cites §2.7 rather than §2.1 for capture, and it makes no claim about which commands set a flag. Nothing in it depends on how §2.1 words that list. |
| §2.11.1, `This keeps the per-unit action vocabulary to exactly two: *attack* or *wait*.` | **Left.** It states this machine's verb count, not §2.1's act list. |
| §2.11.2, `\| End Turn + idle count \| Is my turn genuinely spent \| §2.1 per-unit loop \|` | **Left.** A bare citation with no reprise; it survives any rewording of §2.1. |
| §2.11.2, the unacted-pip audit row's `§2.1` | **Paired for its decision column** (pair 5); its Rule-surfaced column stays a bare citation and gains no reprise. |
| §2.11.2, `A brief \`YOUR TURN\` / \`ENEMY TURN\` banner marks the IGOUGO handoff (§2.1).` | **Left.** IGOUGO alternation is §2.1's own separate sentence and no part of the per-unit sequence; a bare citation either way. |
| §2.11.6-B, beat 1b's `IGOUGO (§2.1)` | **Left**, same reason. |
| §2.11.6-D, the Capture row's disabled `Capture — Infantry only.` label | **Left.** A disabled explanatory label on a non-Infantry, not a verb in the machine; it asserts nothing about §2.1's sequence or about act flags. |
| §2.11.3, §2.11.4, §2.11.5, §2.11.7, §2.11.8 | **No match.** None cites §2.1, reproduces its sequence, or names its act list. |

**Survey B — every §2.11 site that states or implies an ordering between a
unit's move and its act, or that states when a unit stops being available for
further commands.** Re-run after ruling 2:

| Site | Verdict |
|---|---|
| §2.11.1, the four-state block | **Paired** (pair 2). Surveyed as *left* in the first draft on the ground that changing it would be rules-facing; ruling 2 made that change, so it is now mine. |
| §2.11.1, the machine's **Space**-from-SELECTED gap | **Paired** (pair 2), reversing the first draft's *left, and pre-existing*. It is pre-existing, but pair 8 now suppresses that transition for one unit, so the block has to list it; a reader cannot check a suppression against a diagram that omits what is suppressed. Scope is what my own edits make load-bearing, not what the round is nominally about. |
| §2.11.1, `MOVED ──Space (Wait)───────────▶ unit DONE without acting` | **Left — ruling 1 makes it more exact, not less.** With two flags, *DONE without acting* is a precise statement, and pair 3 names it as a case where DONE and the act flag come apart. It is also one of the three routes to DONE that run through MOVED, which is why pair 8's enumeration is qualified to the routes that skip the move rather than stated over all routes. |
| §2.11.1, `MOVED ──RMB / Esc──────────────▶ unit DONE where it stands (move already spent)*` | **Left**, same reason; *move already spent* names one flag correctly, and the move-undo footnote it carries is untouched. |
| §2.11.1 input table, **Hover** unit | **Paired** (pair 4) — it named MOVED as the only forecast state. |
| §2.11.1 input table, **LMB** (`Select own unit / commit previewed move / commit forecast attack / …`) | **Left.** It lists the LMB verbs without binding them to a state, so both attack entries are already covered. |
| §2.11.1 input table, **Tab** (`Cycle to the next unit that has not acted`) | **Left, binding fixed by pair 3.** True once it binds to DONE; false only under the act-flag binding, which pair 3 forbids. |
| §2.11.1 input table, **Space** (`Wait — mark the selected/moved unit done without acting`) | **Left, and it is the authority pair 2's new line is written from.** The row already grants Wait from SELECTED; pair 2 brings the block into line with it rather than the other way round, so the row itself needs no edit. |
| §2.11.1 input table, **Enter** (`3 units have not acted. End turn?`) | **Left, binding fixed by pair 3.** The count is of units the machine has not retired, and every such unit has genuinely not acted — including one that attacked from SELECTED, which is retired and not counted. |
| §2.11.1 input table, remaining rows — hover hex, RMB/Esc, MMB-drag/WASD, mouse wheel, `F`, `B`, `Z`, enemy-turn skip | **Not falsified.** None states or implies an order between move and act, and none states when a unit stops taking commands. |
| §2.11.2, `unacted-unit pips` in the persistent layer | **Left, binding fixed by pair 3.** |
| §2.11.2, contextual layer (`reachable-hex highlight, path preview, attack-target highlight …`) | **Left.** Already scoped as *selection-driven* rather than MOVED-driven, which ruling 2 makes literal. |
| §2.11.2, `\| Attack-target highlight (incl. Artillery's dark range-1 hole) \| Who is actually hittable from here` | **Left.** *From here* is the unit's current hex in either state. |
| §2.11.2, unacted-pip audit row / info-panel hovered-unit line | **Paired** (pairs 5, 6). |
| §2.11.3, `It appears on **hover** over any lit target from the MOVED state` | **Paired** (pair 7). Flagged in the first draft as the site that made the open question reachable; ruling 2 made it false. |
| §2.11.3, `Selecting Artillery renders its attack ring as range 2–3` | **Left — the ruling repairs it.** It said *selecting* while the ring was reachable only from MOVED; pair 7 makes the two agree. |
| §2.11.3, the card's own rules (terrain line, counter line, HP before→after, kill Fame, flag band, the determinism one-shot) | **Not falsified.** None depends on which state the card was opened from. |
| §2.11.4, §2.11.5, §2.11.7, §2.11.8 | **Not falsified.** No move/act ordering and no unit-availability claim in any of them; §2.11.5's `the factory has not built this turn` is a per-factory record, not a unit flag, and §2.11.8's build ranking already lists the machine and input table as one must-have item. |
| §2.11.6-B, beat 1a's constraint cell | **Paired** (pair 8) — the only site in §2.11.6 that gates on the move flag, and the only one that can be stranded by a route to DONE that skips the move. |
| §2.11.6-B, beat 1a's directive and retire condition (`Click one to move.` / `Move completes`) | **Left.** Pair 8 closes both routes from SELECTED to DONE that skip the move — the attack and Wait — and every remaining route runs through MOVED, so the directive stays satisfiable and `Move completes` stays reachable, and neither needs to change. |
| §2.11.6-B, `this is what makes 1a retire inside turn 1 in every branch` | **Left, and pair 8 is what keeps it true.** Either skip-the-move route left open would have made *every branch* false; the sentence sits in the same cell, immediately after pair 8's insertion point, and is carried through unedited. |
| §2.11.6-B, beats 1b, 2, 3 and the schedule table | **Not falsified.** They retire on an enemy turn ending, a capture pip and a spawn; none reads a unit's move or act flag. |
| §2.11.6-C, the first-attack and edge-matchup one-shots | **Not falsified.** They fire on a forecast hover or a resolution, both of which pair 7 widens rather than moves. |
| §2.11.6-D, `carrying its unacted pip` | **Left, binding fixed by pair 3**, which names this row explicitly so the receipt is not read against the act flag. |
| §2.11.6-D, the Hexes & movement and Forecast/determinism rows | **Not falsified.** Their teach moments and confirmations survive pairs 7 and 8 unchanged. |

**Outside §2.11:** nothing found and left. The one site the first draft filed —
§2.1's core-loop line — is ruled into this round and belongs to
`rules-designer`; no pair here touches it.

## Change requests

Change request 1 of the first draft — §2.1's core-loop line — was **accepted and
ruled into this round**, carrying both its edits at once, and `rules-designer` is
writing it in `sections/rules_row5-act-order.md`. It is therefore no longer a
request. Its consequence inside my own file is **pair 1**, which deletes
§2.11.1's copy of that line rather than correcting it, so the two files agree by
one of them no longer making the claim.

One request stands, unchanged from the first draft and not pulled forward:

| Existing § | Current text | Proposed change | Why |
|---|---|---|---|
| §4.7 Spec Stub 8, snapshot per-unit field list | `per-unit  {id, side, unitId, hex, hp, hpMax, isFlag, hasActed, captureProgress}` | Name where the DONE bit lives — a snapshot field, or explicitly widget-local and not persisted | Pair 3 binds §2.11's availability surfaces to a per-unit bit that is **neither** rules flag: Wait and cancel-in-MOVED set no rules flag at all, and ruling 1 confirms the rules module gains no wait or pass command, so DONE cannot be derived from any field the snapshot carries. This is distinct from the second-flag request `tech-director` filed against the same list — a second rules flag still would not produce this bit. Row 8's text and row 8's call. Until it is answered, a mid-turn save/load can return a retired unit to the player with its pip back. |

## Open questions for the Director

None. The one question this file carried — whether a unit may attack without
moving, and what that costs it — is ruling 2, and its answer is written into
pairs 2, 3, 4, 7 and 8: the transition exists, it spends the act, it leaves the
move flag unspent, it retires the unit on the DONE bit, and standing still never
becomes a move.

## Handoffs

- **`rules-designer` (§2.1).** Pair 1 removes §2.11.1's reproduction of your
  line. After it merges, §2.11 cites §2.1 in several places and reprises it in
  none, so your rewrite cannot be contradicted by anything in my section, and
  this handoff does not recur the next time §2.1 moves. I have not read, quoted
  or predicted your new wording.
- **`tech-director` (§4.7 Spec Stub 8, §4.10).** The change request above. The bit
  §2.11's pip, idle count, Tab cycle and End-Turn confirm bind to after this
  merge is a UI bit with no rules flag behind it. Where it lives and whether it
  survives a save is yours; that it exists is pair 3. Ruling 3 gives DONE and the
  flags the same clearing moment, which is what pair 3's `it clears when the
  owner's next turn begins` records on the UI side.
- **`tech-director` (`T-TURN-01`).** Pair 3 cites `T-TURN-01` as the owner of the
  per-unit flags and their orderings and quotes none of its text, so your rewrite
  and this pair cannot contradict each other on wording. The one thing pair 3
  relies on is that the ID stays `T-TURN-01` in Stub 5.
- **`tech-director` (Stub 3, `T-MOVE-03`).** Pair 3 cites `T-MOVE-03` for one
  consequence only — the unit's own hex is not a legal move destination, so it is
  not lit and the two SELECTED highlight sets are disjoint. Ruling 2 states
  `T-MOVE-03` is untouched; if its wording nevertheless moves, that citation
  moves with it.
- **`tech-director` (`T-UI-02`, `T-UI-03`, Stub 8's UI queries).** Pair 2 lights
  attack targets in SELECTED as well as MOVED. The set is the same range/forecast
  query already in the stub, asked one state earlier, so no new query is
  requested — but `T-UI-02`'s reachable-set assertion and whatever asserts the
  attack-target highlight now have a second state to cover.
- **`scenario-designer` (§2.13.1, guided opening).** Pair 8 closes the marked
  Infantry's two routes from SELECTED to DONE that skip the move, while beat 1a is
  outstanding. It asks nothing of the scenario file — `guidedOpening.infantry`
  already names the unit — but if any scenario ever deploys that Infantry within
  range of an enemy on turn 1, pair 8 is the reason the first session still
  teaches movement rather than combat.

## Grounding

- **Why pair 1 deletes rather than corrects** — a corrected reprise is a fresh
  assertion in the same place, and it would need a fresh pair every time §2.1 is
  edited. A bare citation cannot go stale. This is the same discipline pair 3
  applies to `T-TURN-01`, applied to a second section being written in the same
  sitting, and it is why nothing in this file needs to know what
  `rules-designer` wrote.
- **Why pair 1 says the omission is deliberate** — without that clause the next
  editor reads a missing summary and helpfully restores the arrows, which is how
  the copy got there in the first place.
- **Why the block was paired this round and not last** — ruling 2 changed the
  machine. The first draft surveyed it as *left* because widening it was a
  rules-facing change I could not make; the Director made it, so pair 2 writes it.
- **Why pair 8 constrains rather than retracts** — the alternative was to drop the
  claim that beat 1a's retire condition stays reachable, which would have left a
  documented dead end in the shipped first session and falsified §2.11.6-B's own
  `this is what makes 1a retire inside turn 1 in every branch` in the same cell.
  Constraining costs one suppressed hotkey for one unit for one beat; retracting
  costs the guarantee that beat 1a always retires. Teach-by-constraint is also
  1a's existing character, so the remedy is in the register the cell already uses.
- **Why the closure is exhaustive, stated over the right set** — the claim is
  about routes to DONE that **skip the move**, not about routes to DONE. From
  SELECTED there are exactly two that skip it, the attack and Wait, and both are
  closed; RMB/Esc from SELECTED returns to IDLE with nothing committed, and a unit
  in IDLE has not been retired. The machine's three further routes — LMB on a lit
  target, Space, and RMB/Esc, all from MOVED — reach DONE only after the move has
  been spent, which is precisely the condition beat 1a is waiting on, so none can
  strand it. Pair 2's block is what makes that enumeration checkable against the
  diagram.
- **Why a footnote and not a redesign** — the ruling says the remaining
  narrowness is deliberate and is not itself a rule. A narrowing that is correct
  needs a reader-visible reason, not new states.
- **Why the footnote sits where it sits** — §2.11.1 already carries a starred
  note under the same fenced block doing the same job: naming a rule-level fact
  the diagram does not express and stating what ships. The **placement and
  register fit exactly**; the **rationale shape does not**, because that note is
  provisional (`Until that rule is adjudicated`) and this one is not. Pair 3
  adopts the position and the voice and separates itself from the provisionality
  in the sentence beginning `It is also not provisional`. It uses bold lead-ins
  rather than a second footnote marker, which is §2.11.1's own convention for an
  editorial note (`**Capture and build need no extra verbs.**` two paragraphs
  down) and avoids editing bytes inside the fence.
- **Why the cost argument survives ruling 2** — it never rested on there being
  one way to attack. It rests on the unit being retired at the act, and ruling 2
  makes that argument stronger: the SELECTED attack is the case that retires a
  unit with a flag visibly to spare, so it is the case a third pip state would
  have to explain. Pair 3 says so rather than leaving the reader to notice.
- **Why DONE needed a definition at all** — ruling 1 splits one bit into two, and
  §2.11's availability surfaces were written when there was one. The definition
  is what makes those sentences bind to something that still exists, which is why
  most of them need no pair; survey B states, per site, which are covered by the
  binding and which are paired.
- **Pair 5's decision column** — §2.11.2's audit asks what decision an element
  supports. *Which units still have a move* is a fact the pip cannot carry once
  moving and acting are separate, and ruling 2 produces the unit that proves it.
- **Pair 7 against §2.11.3's own thesis** — that section calls the forecast the
  teaching instrument and says the player should be shown the exact outcome
  before committing. A card that only opens after a move shows it after half the
  commitment is already made.
- **Pair 6's `ready` / `done`** — neutral system voice per `kb/setting.md`, which
  reserves faction voice for the result screen. No new one-shot or banner string
  is added anywhere in this file, so that file's ≤ 30-word ceiling is not
  engaged; pairs 1 and 8 add no player-facing string at all — pair 8's suppressed
  **Space** goes inert behind the End-Turn hover already written in that cell.
- **Nothing was invented** — no number appears in any pair. The only identifiers
  cited, `T-TURN-01` and `T-MOVE-03`, are in `source/gdd.md` today.
- **Substring classification, as a falsifiable claim about the bytes above:**
  pair 3's NEW and pair 8's NEW each **contain** their OLD verbatim as a prefix
  (insertions); pairs 1, 2, 4, 5, 6 and 7 each have a NEW that does **not**
  contain its OLD, because each drops bytes the OLD carries — respectively
  `: select → move → act → done, any unit order`, the block's two edited
  transition lines, `if own MOVED unit`, `Which units still have a move`,
  `` `has acted` flag. ``, and `from the MOVED state`. **6 replacements, 2
  insertions.**
- **Nothing in this file describes row 5's shipped code.** The pairs describe a
  UI machine and the bit the HUD binds to; they make no claim about what
  `ad77b13` implements, and `T-TURN-10` is not cited anywhere in them.
