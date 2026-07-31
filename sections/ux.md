# UX, UI & onboarding — stage-2 draft (ux-onboarding-designer)

## Placement

**Replaces §2.11 wholesale.** The current §2.11 is a two-bullet stub ("UI (the real time cost)" + "Art (minimal)"); this draft expands it into a full UX section, §2.11.1–§2.11.8. Every element named in the current stub (pan/zoom, selection, reachable-hex highlight, attack-target highlight, attack forecast, info panel, turn banner, end-turn, production menu, flag marker, live standings scoreboard) is retained and specified; the art bullet survives unchanged as §2.11.7.

This draft **supersedes and integrates the stage-1 onboarding draft**: the guided opening, one-shot lesson table, and concept ledger are carried forward (as §2.11.6), while the forecast-card and scoreboard specs that stage-1 sketched inside the onboarding plan now live in their proper homes (§2.11.3, §2.11.4) and the onboarding text references them instead of duplicating them. The stage-1 change requests are still unresolved in `source/gdd.md` and are re-filed below.

## Draft

### 2.11 UI/UX

Stratocracy's interface has one job: make a deterministic game *look* deterministic. Every rule in §2 is knowable before the player commits, so the UI's standard is not "pretty" but **no surprises** — if the player is ever surprised by an outcome, the UI failed, not the player. Three principles govern everything below:

1. **Hover is information, click is commitment.** Hovering never changes game state; it only reveals (terrain lines, path previews, the forecast). A single left-click commits. Cancel is always right-click or Esc.
2. **Every element earns its pixels.** Each HUD element is audited against the decision it supports (§2.11.2); anything supporting no decision is cut. Two deliberate cuts up front: **no minimap** (the one shipped scenario is a small skirmish map, §2.7 — it fits on screen at default zoom; pan/zoom covers the rest) and **no combat log** (determinism plus the forecast make a history redundant for the prototype; a log rides the replay format if that ships, see Handoffs).
3. **Rules-critical information is never transient-only.** Toasts and banners are receipts; the durable version of every fact lives on a persistent or hover-recallable surface.

UI is budgeted as core work from week 2 (§4.4, §4.5 — "UI underestimated" is a named risk) and everything below is scoped to what one person can build in UMG on top of agent-scaffolded widget skeletons (§3, UI Scaffolder role).

---

#### 2.11.1 Control scheme

**Selection state machine.** The core loop (§2.1: select → move → act → done, any unit order) maps to four UI states:

```
IDLE ──LMB on own unacted unit──▶ SELECTED (reachable hexes lit, §2.5)
IDLE ──LMB on own factory──────▶ PRODUCTION MENU (§2.11.5)
SELECTED ──LMB on lit hex──────▶ MOVED (attack targets lit; Wait available)
SELECTED ──RMB / Esc───────────▶ IDLE (nothing committed)
MOVED ──hover enemy target─────▶ forecast card shown (§2.11.3)
MOVED ──LMB on lit target──────▶ attack resolves exactly as forecast → unit DONE
MOVED ──Space (Wait)───────────▶ unit DONE without acting
MOVED ──RMB / Esc──────────────▶ unit DONE where it stands (move already spent)*
```

\* Under the pending **move-undo change request** (re-filed below), RMB/Esc in MOVED instead reverts the unit to its pre-move hex and returns to IDLE. Until that rule is adjudicated, the shipping semantics are the conservative ones shown: a completed move stands. The two behaviors share a UI; only the rules module differs.

**Capture and build need no extra verbs.** Capture is by presence (§2.7: an Infantry that ends its move on a capturable tile begins capturing — a progress pip appears, no button). Building is the factory's own interaction, not a unit's. This keeps the per-unit action vocabulary to exactly two: *attack* or *wait*.

**Input reference.**

| Input | Effect |
|---|---|
| **Hover** hex | Terrain line in the info panel (§2.11.2); if a unit is SELECTED, dotted **path preview** along the cheapest route (§2.5) with the terrain-cost tick per hex |
| **Hover** unit | Unit stats in the info panel; if own MOVED unit has it in reach, the **forecast card** (§2.11.3) |
| **LMB** | Select own unit / commit previewed move / commit forecast attack / open production menu on own factory / activate buttons |
| **RMB / Esc** | Cancel: close menu or forecast, deselect, back out one state (see machine above) |
| **MMB drag** or **WASD / arrows** | Pan camera |
| **Mouse wheel** | Zoom (two or three fixed steps, not continuous — readability over cinematography) |
| **Tab** | Cycle to the next unit that has not acted |
| **Space** | Wait — mark the selected/moved unit done without acting |
| **F** | Snap camera to your flag unit |
| **B** | Open the production menu at the selected owned factory (or your home factory if none selected) |
| **Enter** | End turn — with a confirm dialog if any unit has not acted: `3 units have not acted. End turn?` |
| **Z** | Undo move *(only if the §2.5 change request is accepted; otherwise unbound)* |
| **Any click / Esc during enemy turn** | Skip AI playback to its end state (§2.11.2, turn banner) |

No hidden double-functions, no drag-to-move, no context menus. A first-session player can complete a match knowing only: hover, LMB, RMB, Enter.

---

#### 2.11.2 HUD layout & information architecture

**Screen layout.**

```
+--------------------------------------------------------------------------+
| +-------------------+   [ DIRECTIVE STRIP / TURN BANNER ]   +----------+ |
| | TURN 12 / 20      |        (top center, transient)        | FAME 350 | |
| |-------------------|                                       | +125/turn| |
| |        YOU  ENEMY |                                       +----------+ |
| | Destr. 450   600◀ |                                                    |
| | Obj.   3/6   2/6  |                                                    |
| | HP     47    55   |          ( hex battlefield )                       |
| +-------------------+                                                    |
|   (live scoreboard,               [H] flag markers on-map                |
|    §2.11.4)                       [forecast card floats near target]     |
|                                                                          |
| +-------------------+                              +-------------------+ |
| | INFO PANEL        |      [ toast queue,          | 3 units idle      | |
| | Woods             |        bottom center ]       | [ END TURN  ⏎ ]   | |
| | move 2 · def +20% |                              +-------------------+ |
| +-------------------+                                                    |
+--------------------------------------------------------------------------+
```

**Three information layers**, strictly tiered:

1. **Persistent** (always on screen): scoreboard + turn counter, Fame pool + income rate, End Turn + idle-unit count, on-map flag `H` markers and unacted-unit pips. These are the four standing decisions of every turn — *am I winning the cap, can I afford to build, is my turn actually finished, what must I protect.*
2. **Contextual** (selection-driven): reachable-hex highlight, path preview, attack-target highlight, info panel content, forecast card, production menu, capture pips. Appears with a selection or hover, gone when it ends.
3. **Transient** (event receipts): toasts (`+100 Fame — Factory`, `+[N] HP — repaired`, `+150 Fame` on a kill), turn banner, one-shot onboarding lines (§2.11.6), cap-approach banners (§2.11.4). Each transient fact has a durable home: income toasts restate what the Fame widget's `+X/turn` already shows; kill toasts restate the scoreboard's Destroyed row.

**Earn-your-pixels audit** — every persistent/contextual element, the decision it supports, and the rule it surfaces:

| Element | Decision it supports | Rule surfaced |
|---|---|---|
| Scoreboard (turn + 3 rows) | Force combat or hold; how close is the cap | §2.8 tiebreak order, turn cap |
| Fame pool + `+X/turn` | Build now vs. save; which neutral factory is worth a fight | §2.7 income (+100 factory / +25 town), costs |
| End Turn + idle count | Is my turn genuinely spent | §2.1 per-unit loop |
| Flag `H` marker (both sides, always visible) | What to protect, what to hunt | §2.4 flag death ends the match; *Conflict*'s `H` convention |
| Unacted pip on own units | Which units still have a move | §2.1 |
| Reachable-hex highlight | Where can this unit truly go | §2.5 — "the real move set, not an estimate" |
| Path preview with cost ticks | Which route; exposure en route (e.g. a turn spent on the Bridge at −10%) | §2.3, §2.5 cheapest-route |
| Attack-target highlight (incl. Artillery's dark range-1 hole) | Who is actually hittable from here | §2.4 ranges; the Artillery dead zone |
| Forecast card | Commit this attack or not | §2.6 — the whole section (§2.11.3) |
| Info panel | Speed-vs-cover terrain trade; matchup reading | §2.3 table, §2.4 stats |
| Production menu | What to buy, where it will spawn | §2.7 build & spawn rules (§2.11.5) |
| Capture progress pip | Hold or abandon the capture | §2.7 capture over N turns |
| Repair eligibility pip (owned tile, damaged unit selected, no adjacent enemy) | Retreat to heal or keep fighting | §2.7 repair + anti-fortress clause |

**Info panel** (bottom-left, hover-driven, ~3 lines, never modal):
- Hovered hex: terrain name, move cost, defense bonus, and status if capturable — `Factory · move 1 · def +15% · yours (+100/turn)` or `· neutral` or `· enemy`.
- Hovered unit: name, HP as `12/20`, Atk/Def/Move/Range, `has acted` flag. The flag unit's panel is red-edged and appends `FLAG — its loss ends the match.`
- Empty when nothing is hovered. It never covers the board's lower-center where fighting happens.

**Turn banner & AI playback.** A brief `YOUR TURN` / `ENEMY TURN` banner marks the IGOUGO handoff (§2.1). The headless AI resolves instantly (§2.8); the presentation layer **replays its action list at a watchable fixed pace** (~0.5 s per action, camera stepping to each) so the player can read what the AI built, captured, and attacked — this is presentation pacing only, no rules change. Any click or Esc skips to the end state. First-session value: watching the AI's economy phase is how the player learns the enemy shares the same Fame economy (§2.9).

---

#### 2.11.3 The attack forecast — the game's centerpiece display

Combat is a pure function (§2.6, §3 spec), so the forecast is not an estimate — it is the resolution, shown early. It appears on **hover** over any lit target from the MOVED state; **LMB commits**, RMB/Esc cancels. The card:

```
+------------------------------------------+
| ATTACK FORECAST                          |
| Artillery  →  Tank      (Woods +20%)     |
|                                          |
|  You deal    3 dmg      Tank 20 → 17     |
|  Counter     0          out of range     |
|                                          |
|  [LMB] Commit        [RMB / Esc] Cancel  |
+------------------------------------------+
```

*(Values follow the §3 formula: Artillery atk 10 at full HP vs Tank def 5 in Woods → round(10 × 1.0 × 0.8) − 5 = 3; counter 0 because the attacker sits outside the Tank's range 1.)*

Hard rules for the card:

- **The defender's terrain bonus is named inline** (`Woods +20%`), every time — terrain defense must never read as hidden dice. (Per the §3 invariant, it is always the *defender's* hex; the card's placement of the modifier next to the defender teaches that for free.)
- **The counter line is never omitted, and always states its reason**: a number, `out of range`, or `defender destroyed`. This line is where the positional RPS triangle (§2.4) becomes visible — there is no type chart to consult, deliberately, so `Counter 0 — out of range` *is* the Artillery-beats-Tank lesson and `Counter 5` on an adjacent brawl *is* the Tank-beats-Recon lesson.
- **HP is shown before → after** for the defender (and for the attacker whenever the counter is nonzero), so the HP-scaling term of the formula (§2.6 — a damaged attacker hits softer) is observable across fights rather than asserted.
- **Lethal forecasts state their reward**: if the defender dies, the card appends `Destroys Tank · +150 Fame` (kill ≈ half cost, §2.7) — the tiebreak's combat-Fame criterion (§2.8) is priced on the commit card, not discovered at the cap.
- **Flag warning band**: if the forecast is lethal to *either* flag, the card gains a band — `FLAG AT RISK — this attack ends the match` (own flag: red; enemy flag: gold, with `+500 · Decisive victory`). No player can end a match, theirs or the enemy's, without having been told on the card they clicked.
- **Determinism is restated once**, via the first-attack one-shot (§2.11.6): `Check the forecast. It is exact — what you see is what resolves.` After that the card carries no reassurance text; the outcomes matching the card, every time, are the proof.

Selecting Artillery renders its attack ring as range 2–3 **with the range-1 hole drawn visibly dark** — the dead zone on the map is the "Recon runs it down" lesson in pixels, using the attack-target highlight already budgeted.

---

#### 2.11.4 The live Fame scoreboard

The scoreboard exists because of revision §1.5-#1: the tiebreak must never be a hidden win condition. It is persistent (top-left), compact, and its **rows are ordered top-to-bottom in exact tiebreak order (§2.8)** — the layout *is* the rule, read passively all match:

```
+---------------------------+
| TURN 12 / 20              |
|---------------------------|
|            YOU      ENEMY |
| Destroyed  450      600 ◀ |
| Objectives 3/6      2/6   |
| Unit HP    47       55    |
+---------------------------+
```

- **Turn counter** against the cap, always. (`/ 20` uses the §2.8 example value; the cap must be fixed before this ships — change request below.)
- **Destroyed** = combat Fame earned (kills + undamaged-strike and flag bonuses, §2.7) — **passive income is excluded**, exactly as the tiebreak excludes it. Hover tooltip: `Fame from kills and strike bonuses. Factory income does not count at the cap.` This row deliberately does *not* equal the spendable Fame pool (top-right widget), and the tooltip on each names the difference — the one place the single-currency design (§2.7) needs a disambiguating sentence.
- **Objectives** as *X of N* over all factories + capturable towns (§2.8 criterion 2), N supplied by the scenario (Handoffs).
- **Unit HP** = surviving strength (criterion 3), listed last because it *is* last.
- A **chevron (◀)** marks the current attrition-tiebreak leader, evaluated in criteria order, and flips visibly when the lead changes. It is drawn beside the leading side's value — in the mock above the enemy leads at criterion 1, 600 combat Fame to 450 (§2.8: higher wins), so the chevron sits on the enemy column. If both Destroyed values are zero, the chevron is replaced by `— no engagements —` spanning the row: the mutual-passivity draw (§2.8) made visible before it bites.
- **Cap-approach banners** (transient, once each): at cap−5, `5 turns to the cap. The scoreboard decides a capped match.`; additionally, if both sides are still at zero combat Fame, `No engagements. A capped match with no combat is a draw.`

**End-of-match screen.** The result is the tier first (§2.8 — Decisive / Marginal / Draw), then the same three rows in the same order, so the verdict is always a restatement of what was on screen all match. Beneath the tier, one **faction-voiced result line** (per the setting guide: faction voice appears only on result screens; ≤ 30 words; field-manual register). Samples, one per case, generated content to follow these:

- Directorate, decisive: `Command directive fulfilled. The enemy flag is struck from the record. Order is restored.`
- Directorate, marginal: `The cap is reached. The ledger favors the Directorate. The record stands.`
- Vanguard, decisive: `Their flag is down. We hold the ground. That's the whole report.`
- Vanguard, marginal: `Cap hit. We did the damage; they held the rear. The ground says we win.`
- Draw, neutral system voice: `Turn cap reached. Attrition equal. Recorded as a draw.` / mutual passivity: `Turn cap reached. Neither side engaged. Recorded as a draw.`

---

#### 2.11.5 Production menu & match-flow surfaces

**Production menu** — opens on LMB on an own factory (or `B`), anchored beside it:

```
+--------------------------------------+
| FACTORY — BUILD          Fame: 250   |
|--------------------------------------|
|  Infantry   100   [Build]            |
|  Recon      150   [Build]            |
|  Artillery  200   [Build]            |
|  Tank       300    ----   (need 50)  |
|--------------------------------------|
|  Spawns here, or adjacent if         |
|  occupied.                           |
+--------------------------------------+
```

- Unaffordable rows are greyed with the shortfall named (`need 50` at the mocked 250-Fame pool against the Tank's 300 cost, §2.4), never hidden — the price list is also the strategy lesson (§2.4 costs).
- The spawn rule (§2.7: factory hex if free, else an adjacent free hex) is one static line in the footer. If the factory is fully boxed in, the footer swaps to `Boxed in — build waits for a free hex.` and Build buttons disable: the space-throttle (§2.7) explains itself at the moment it applies.
- When any unit is affordable and the factory has not built this turn, the factory tile shows a small `BUILD` pulse — the nudge that connects hoarded Fame to an army (a first-session failure mode, §2.11.6 ledger).
- The row hover shows the unit's stat line in the info panel, so buying is done with the §2.4 table in view.

**Pre-match**: the static briefing overlay (three callouts: flag, Bridge, factories — §2.11.6-A). **Post-match**: the end screen above. That is the complete screen list for the prototype: title/menu, briefing, match, result. No settings screen beyond volume + resolution is budgeted (Enhanced Input remap is a polish item).

---

#### 2.11.6 Onboarding — the first session

*(Carried forward from the stage-1 accepted draft, with the forecast-card and scoreboard material now living in §2.11.3–§2.11.4; the plan is unchanged in substance.)*

**Philosophy.** No manual, no tutorial mode, no modal text walls. Three teachers:

1. **Constraint** — the first turn removes every option except the one being taught.
2. **The forecast** (§2.11.3) — deterministic combat means every attack is a free, truthful lesson in terrain defense, range, and HP scaling. The plan makes the player *read* the forecast once, early; after that the game teaches itself.
3. **One-shot event tips** — a single system-voice line (≤ 30 words, tone bible), fired the first time a concept becomes relevant, never repeated (boolean flags in the save slot, §4.1).

The first match runs on the one shipped scenario at **Easy** by default (player +150 opening Fame, §2.9) with a **guided opening**: scripted directives across turns 1–3, then hands-off. Any completed match on the save skips all guidance automatically; a `Skip guidance` control kills it instantly for anyone.

**A. Pre-match briefing** — a dimmed board, three anchored callouts, click-through (~5 s): **your flag** (`If it falls, you lose. It cannot be rebuilt.`), **the Bridge** (`The only land crossing.`), **factories** (`Hold them for Fame. Fame builds units.`). Why only three: the flag is the win condition, factories are the economy, and the Bridge is the map-reading trap — a player who misses the single Water crossing misplans the whole match.

**B. Guided opening (turns 1–3), via a one-line directive strip** at top center, one instruction at a time, each retiring on completion:

| Turn | Constraint | Directive | Teaches | Retires when |
|---|---|---|---|---|
| 1a | Only one marked Infantry selectable; others dimmed (hover: `Locked this turn.`) | `Select the marked Infantry. Lit hexes are its true reach. Click one to move.` | Selection; the highlight is the real move set (§2.5) | Move completes |
| 1b | End Turn pulses | `End turn. The enemy moves; then you.` | IGOUGO (§2.1) — the player watches a full AI turn | Enemy turn ends |
| 2 | None. Targets the nearest neutral factory (scenario guarantee — Handoffs) | `Move Infantry onto the Factory. Only Infantry captures.` | Capture; the Infantry-only rule (§2.7) | Capture pip appears |
| 3 | None. Fame ≥ 100 guaranteed by 200 start + home income (§2.7) | `Spend Fame at your Factory. Infantry costs 100.` | Fame → factory → unit | A unit spawns |

After turn 3 the strip disappears for good.

**C. Event-driven one-shots** (once each, at first relevance): first attack hover → `Check the forecast. It is exact — what you see is what resolves.`; first Artillery strike at range 2–3 → `No counter at this range. Artillery strikes beyond reply.`; first Recon-vs-Artillery forecast → `Recon closes fast. Artillery cannot answer at range 1.`; first Tank-vs-Recon forecast at range 1 → `Armor wins the adjacent fight.`; first Water hover with a unit selected → `Impassable to land. Cross at the Bridge.`; first Bridge hover → `The only crossing. −10% defense — do not stall on it.`; first combat Fame → `+150 Fame. Kills count at the cap. Income does not.` *(amount = actual award)*; first undamaged strike → `+[N] Fame — undamaged strike.`; first repair blocked by adjacency → `No repair — enemy adjacent. Break contact to repair.`; first repair tick → `+[N] HP — repaired at Factory.`; plus the two cap-approach banners (§2.11.4).

**D. Concept ledger** — every concept, its failure point, its teach moment, its confirmation:

| Concept | Where a first-timer gets lost | Taught at | Confirmed landed when |
|---|---|---|---|
| Hexes & movement | Clicks the map with nothing selected | Turn 1a: single selectable unit + reach highlight | Move completes; directive retires |
| IGOUGO turns | Expects simultaneous movement | Turn 1b: pulsing End Turn, then watching the AI's turn | Player ends turn 2 unprompted |
| Terrain move cost | Lopsided highlight (shallow into Woods/Mountains) reads as a bug | The asymmetric highlight + info-panel hover line | Player routes around a Mountain, or hovers 2+ terrains in one selection |
| Terrain defense | Same attack, different damage → suspects hidden dice | Forecast names the defender's bonus inline, every time (§2.11.3) | Resolution matches forecast, every time |
| **The Bridge** | Reads Water as decoration; "half the map is unreachable" | Briefing callout + Water never lights in any reach set + hover one-shots | First previewed or executed path crosses the Bridge |
| Forecast / determinism | Veterans hedge for RNG; novices fear committing | First-attack one-shot: `It is exact.` | Player commits; outcome equals card; usage becomes habitual |
| **Positional RPS triangle** | No counter chart exists — the triangle is emergent from range and move, invisible until experienced | The counter-reason line (§2.11.3), the three edge one-shots, the Artillery dead-zone ring | One uncountered Artillery strike lands — the undamaged-strike toast is the receipt |
| Capture | Parks a Tank on the factory and waits | Turn 2 directive; non-Infantry on a capturable tile shows disabled `Capture — Infantry only.` | Pip → tile recolors → next turn's `+100 Fame — Factory` toast |
| Fame income & build | Fame is abstract; player hoards, never connects factories → army | Income toasts; `BUILD` pulse when affordable; greyed rows with shortfall (§2.11.5) | Turn 3 directive completes: a bought unit stands on the board |
| Flag = the game | Loses one specific Tank in a "fair trade"; match ends out of nowhere | Briefing callout; persistent `H`; red-edged info panel; flag warning band (§2.11.3) | Any lethal-to-flag forecast has been shown before any match can end |
| Turn cap & tiebreak | Assumes "most stuff wins"; income exclusion and passivity-draw are the least guessable rules | Scoreboard rows in tiebreak order (§2.11.4); first-combat-Fame one-shot; cap−5 banners | Chevron flips noticed in play; end screen matches the board watched all match |
| Repair | Heal silently fails next to an enemy; reads as a bug | Eligibility pip; the `enemy adjacent` one-shot fires at the *blocked* case first if it occurs | `+[N] HP — repaired` toast at turn start |

---

#### 2.11.7 Art (unchanged)

Flat/low-poly color-coded hexes, simple unit meshes or billboarded icons, generative/agent-assisted. Feel comes from subtle tweens and clear feedback, not VFX. One readability addition, cheap and worth naming: ownership is **double-coded** (faction color *and* a shape/border difference), so faction reading never depends on hue alone.

#### 2.11.8 Build ranking (solo dev, UMG)

**Must-have for a playable first session:** selection state machine + input table (§2.11.1); reachable highlight and path preview (the path is already computed by §2.5 pathfinding — rendering it is cheap); forecast card with terrain-inline, counter-reason, HP before→after, kill-Fame line, and flag band; scoreboard in tiebreak order with turn counter and chevron; Fame pool + income widget; production menu with grey/shortfall/boxed states; info panel; End Turn + idle confirm; turn banner + paced AI playback with click-to-skip; toast queue; flag `H` markers and unacted pips; directive strip with the four beats; the one-shot system (string table + boolean flags); pre-match briefing overlay; end-of-match screen with tier + rows + one faction line.

**Polish:** chevron flip animation; Artillery dead-zone shading (plain target highlight conveys most of it); cap banners' timing tuning; camera smoothing and zoom-to-action; hotkey remap via Enhanced Input; colorblind palette variants beyond the default double-coding; hover-delay tuning; a dedicated micro-tutorial map (explicitly stretch — it would occupy a stretch scenario slot, §2.10).

## Change requests

| Existing § | Current text | Proposed change | Why |
|---|---|---|---|
| §2.5 Movement & pathfinding *(re-filed from stage-1, unresolved)* | No mention of undoing a move | Add: "A move may be undone at no cost until the unit acts (attack / capture / build). With fog cut (§2.10), undo reveals no hidden information." | Safe experimentation is the cheapest teacher; a mis-clicked 7-move Recon teaches fear of clicking. §2.11.1 specifies both semantics so the UI ships either way — but the rule needs adjudication. |
| §2.7 Capture *(re-filed)* | "hold to capture over N turns (start N=1–2)" | Fix N | N=1 is "captured on arrival"; N=2 needs the progress pip and a "hold" verb. The pip design covers both, but directive and tip strings can't lock until N does. |
| §2.8 Turn cap *(re-filed)* | "the turn cap (e.g. 20 turns)" | Fix the cap value | The scoreboard renders `TURN X / cap` permanently and the cap−5 banners need a number. "e.g." can't ship on a HUD. |

## Open questions for the Director

1. **Enemy spendable-Fame visibility.** The scoreboard shows enemy combat Fame (Destroyed row), but should the enemy's *spendable* pool be visible too? Recommendation: **yes, show it** (small line under the enemy column) — the prototype has no fog (§2.10), the game is full-information by pillar 1, and "can they afford a Tank next turn?" is a real decision. But the GDD doesn't currently say either way, so this is yours to call, not mine to invent.
2. **AI playback pace.** ~0.5 s per action with click-to-skip is proposed (§2.11.2). Any preference for a settings-exposed speed, or is skip-only enough for the prototype? (Recommendation: skip-only; a slider is polish.)
3. **First-match default difficulty** *(carried from stage-1)*: default a fresh save to Easy with the guided opening, no difficulty menu before match one? (Recommendation stands: yes — one fewer decision before the player has context.)
4. **Directive during the AI economy phase** *(carried)*: fire a one-time `Enemy builds at Factory` callout during the first watched AI turn? Cheap, teaches the shared economy, but adds one interrupt.

## Handoffs

- **tech-director:** the widget inventory in §2.11.8 is the UMG scaffolding list; data bindings needed from the headless module: combat **forecast/preview function** (pure query, same formula as resolution — the card must call the real function, never a UI-side copy); path preview polyline for a candidate destination; per-side combat-Fame and objectives-X/N and total-HP for the scoreboard; unacted-unit query; production affordability + spawn-hex/boxed-in query; repair-eligibility query; AI turn **action list** for paced playback; first-time boolean flags in the save slot; event hooks (first-attack-available, first-combat-Fame, repair-blocked, cap−5). A combat log, if ever, rides the replay format — tech's call, not a UI ask.
- **scenario-designer:** the guided opening keeps its three map guarantees — (1) a neutral factory reachable by a starting player Infantry by end of turn 2; (2) the Bridge on or beside the natural advance path; (3) enemy Artillery, Recon, and Tank all present early enough that the three triangle one-shots can fire in match one. Also needed: the scenario's objective count N for the scoreboard's X/N.
- **rules-designer:** adjudicate the three re-filed change requests (move-undo, capture N, cap value); confirm that "capture by presence, no button" is the intended §2.7 reading.
- **Director:** open questions 1–4; and the stage-1 note stands that the cap value feeds both the scoreboard and the onboarding banners.

## Grounding

| UX decision | Mechanic it serves |
|---|---|
| Hover=info / click=commit; RMB/Esc cancel everywhere | §2.1 select→move→act loop; pillar 1 legibility |
| Selection state machine with only attack/wait as unit verbs | §2.1; §2.7 capture-by-presence and factory-owned build keep the verb set minimal |
| Path preview with per-hex cost ticks | §2.5 cheapest-route over §2.3 variable terrain cost |
| Forecast card: inline terrain bonus, counter-reason line, HP before→after | §2.6 determinism; §3 invariants (defender-hex terrain only; counter only if survivor in range; HP-ratio scaling) |
| Kill-Fame line and +500 flag band on lethal forecasts | §2.7 kill ≈ half cost, flag +500; §2.8 combat-Fame tiebreak priced at the moment of commitment |
| Artillery ring with dark range-1 hole | §2.4 positional RPS — the dead zone *is* Recon-beats-Artillery |
| Scoreboard rows in tiebreak order; Destroyed excludes income; passivity indicator | §2.8 criteria order; income exclusion and mutual-passivity guard (revision §1.5-#1, #5) |
| Chevron on the leading side's value, criteria order ("higher wins") | §2.8 criterion 1 — the mocks show the enemy leading at 600 vs 450, so the glyph sits on the enemy column |
| Destroyed row ≠ Fame pool, disambiguated by tooltips | §2.7 single currency vs. §2.8 combat-Fame-only tiebreak — the one place they diverge on screen |
| Production menu grey/shortfall/boxed states | §2.7 costs, spawn rule, space-throttle — the mock's 250-Fame pool legally greys only the 300-cost Tank (`need 50`) |
| Paced AI playback with skip | §2.9 two-phase AI (economy visible in play); §2.8 "AI moves instantly" untouched — presentation only |
| End screen = tier + same rows + faction line | §2.8 categorical tiers; setting guide (faction voice only on result screens, ≤30 words, no banned register) |
| No minimap, no combat log | Pillar 4 / earn-your-pixels: small single-screen map (§2.7 skirmish scale); determinism + forecast make history redundant |
| Onboarding by constraint + one-shots + concept ledger | §2.1–§2.8 across the ledger; §4.4 wk-5 onboarding milestone; §2.9 Easy = +150 Fame, identical AI |
| Everything is UMG widgets, toasts, string tables, boolean flags | §4.4 solo-dev budget; §4.5 "UI underestimated" risk; §3 UI-Scaffolder skeletons |
