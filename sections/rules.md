# Rules — stage-2 draft (rules-designer)

## Placement

Replaces **§2.1–§2.10 and §2.12 in full**, and inserts a new **§2.0
Player-experience goals** immediately before §2.1. Every existing §2.x number
is preserved, so cross-references from §1, §1.5, §3, and §4 stay valid without
edits.

**§2.11 (UI/UX & art) is deliberately absent from this draft** — the
ux-onboarding-designer's stage-2 draft expands it; merge theirs in its place.

**This draft supersedes the stage-1 rules draft.** The stage-1 §2.8 tiebreak
rework (verdict: defended, with two trims) is folded verbatim-in-substance
into §2.8 below, and its still-unmerged change requests are re-filed in the
table here so they are not lost to the file overwrite.

## Draft

### 2.0 Player-experience goals

The pillars (§1) state what the design values; these goals state what the
player should experience, phrased so each is observable in the test suite or
the balance harness (§4.1). A goal that cannot be checked is a preference, not
a goal — so each row carries its check. Self-play reports and playtest notes
cite goals by ID.

| ID | The player experiences | Rule source | Observable check |
|---|---|---|---|
| PX-1 | Matches feel short and decisive: ~10–15 minutes typical, ~20 worst-case at the cap. A match never becomes the hour-long slog the lineage was criticized for. | §1, §2.8 | Self-play turn-length distribution: the median match ends before the turn cap; cap-tiebreak matches are a minority of results. |
| PX-2 | The rules can be trusted completely. The forecast shown before committing an attack is exactly what resolves — a whole turn can be planned in advance. | §2.6 | Every attack's forecast equals its resolution; identical inputs give identical results (determinism invariants, T-COMBAT suite). |
| PX-3 | Depth comes from where units stand, not from a memorized counter chart. The triangle is read off movement and range on the board. | §2.4 | The type-effectiveness table ships all-1.0; no counter-multiplier is load-bearing at ship. |
| PX-4 | Fighting is always better than hiding. There is no line of play where sealing a corner and running the clock wins. | §2.7, §2.8 | A side with zero combat Fame never wins a capped match (T-CAP-02, T-CAP-03). |
| PX-5 | The player always knows who is currently winning and how close the cap is. The tiebreak is never a hidden win condition. | §2.8, §2.11 | The standings scoreboard displays every tiebreak input (combat Fame, objectives held *X/N*, surviving HP) plus the turn counter against the cap. |
| PX-6 | The economy is one thought: earn Fame, spend Fame. The player never converts between currencies or tracks parallel pools. | §2.7 | Every income, build cost, and combat reward mutates a single per-side Fame pool; no second resource exists in the data schema. |

### 2.1 Core loop
```
Player turn:
  for each of your units (any order):
     select → move (within range, terrain-costed) → act (attack / capture / build) → done
  end turn
Opponent turn: same, driven by AI
repeat until a flag unit dies, an objective is met, or the turn cap triggers a tiebreak
```
I-GO-U-GO alternation. No simultaneous resolution.

### 2.2 Hex grid
The battlefield is a field of pointy-top hexagons. The player reads adjacency
and distance at a glance — every hex has six equal neighbours, so no direction
is unfairly cheap the way diagonals are on a square grid — and each unit
occupies exactly one hex. Line-of-sight blocking (a unit can't see or fire
through a ridge) is a stretch goal.

### 2.3 Terrain (prototype set: 6 movement terrains + the capturable Factory tile)
Terrain is the first thing the player weighs before moving: some hexes cost
more of a unit's movement allowance to enter, some make a unit standing on
them harder to kill, and some are closed to certain movement classes entirely
— the player is always trading speed against cover and reach. Move cost is per
movement class. All values are starter/tuning targets.

| Terrain | Move cost | Defense | Passable |
|---|---|---|---|
| Plains | 1 | 0% | land, air |
| Woods | 2 | +20% | land, air |
| Mountains | 3 | +40% | land (slow), air |
| Water | — | 0% | sea, air |
| Town | 1 | +10% | land, air; capturable |
| Bridge | 1 | −10% | land, air; **the only hex a land unit crosses Water** |
| Factory | 1 | +15% | land, air; capturable; build/spawn + repair point |

**Bridge** turns Water from dead space into a chokepoint system: land routes
must funnel across bridges, and the negative defense makes a unit caught
mid-crossing an exposed target — a contested kill-zone, not a safe shortcut.
*(Tuning fallback: −10% → 0% if too punishing.)* **Factory** is the economy's
anchor (§2.7): occupiable by either side, capturable by Infantry, a defensive
anchor, and the build/spawn + repair point.

### 2.4 Units (prototype set: 4)
Rock-paper-scissors, not a roster. Starter stats.

| Unit | HP | Move | Atk | Def | Range | Cost (Fame) | Notes |
|---|---|---|---|---|---|---|---|
| Infantry | 10 | 3 | 4 | 2 | 1 | 100 | Cheap; the only unit that captures towns/factories |
| Tank | 20 | 5 | 8 | 5 | 1 | 300 | Line breaker; **Flag Unit** is a Tank variant (not producible) |
| Artillery | 8 | 3 | 10 | 1 | 2–3 | 200 | Strong ranged, fragile, no melee counter |
| Recon/Air | 12 | 7 | 5 | 3 | 1 | 150 | High move; ignores some terrain cost |

**Cost is in Fame**, the single currency (§2.7). All values are tuning
targets, scaled down from *Conflict*'s cost ladder for four units and
~20-turn matches (§2.12).

**Flag Unit:** a designated Tank. Its death = loss. Not producible.

**The triangle is positional, not a counter chart.** Stratocracy's
rock-paper-scissors lives in movement and range, an invariant worth naming:
**Artillery beats Tank** (fires from range 2–3, takes no melee counter),
**Recon beats Artillery** (move 7 runs it down into a fragile melee), **Tank
beats Recon** (higher atk/def wins the range-1 fight). Infantry sits outside
the triangle as the capture/objective unit. A type-effectiveness multiplier
exists in the combat formula (§3) but ships **defaulted to 1.0 everywhere** —
populated only if self-play shows the positional triangle too weak, so depth
stays in positioning rather than in a lookup table (Pillar 3; PX-3).

### 2.5 Movement & pathfinding
The player selects a unit and every hex it can truly reach this turn lights
up, terrain costs already accounted for — the highlight is the real move set,
not an estimate. Clicking a lit hex sends the unit by the cheapest route. Only
one unit fits in a hex, so lanes, chokepoints, and blocking are part of the
plan. Zones of control — enemy units freezing anything that moves next to them
— are cut from the prototype; they return only if matches feel too fluid.

### 2.6 Combat resolution
Before an attack is committed, the game shows the outcome up front: the
predicted damage dealt, and the counterattack the defender strikes back with
if it survives and the attacker is within its reach (attack forecast, §2.11).
Combat is a pure function of attacker, defender, the defender's terrain, and
the attacker's remaining health — the same matchup always resolves the same
way, so a player can plan a whole turn and trust it plays out as shown (PX-2).
Any randomness added later is **seeded**, so a given fight stays reproducible:
the forecast the player sees is exactly what resolves, with no hidden roll.

### 2.7 Economy & capture — the Fame currency
Stratocracy runs on a **single currency, Fame** (inherited from *Conflict*,
§2.12): earned from held objectives and combat, spent to build, tallied to
decide a capped match. Production points, combat rewards, and the win-score
are **one pool, not three** (PX-6). *All numbers are starter/tuning targets,
scaled down from Conflict's for four units and ~20-turn matches.*

- **Factories & starting layout:** the map ships with **multiple factories** —
  a **home factory per side** (owned at start, so both players have income
  from turn 1) plus **two or more neutral factories** in contested ground; a
  typical small skirmish map has **~4 factories total**. The spread is what
  makes expansion worth fighting for and "objectives held" (§2.8) a real 0–N
  measure instead of a 1–0 coin-flip.
- **Income:** each **factory** held pays **+100 Fame/turn**; each captured
  **town** pays **+25/turn**. More objectives held = a faster army, so the
  neutral factories are the mid-game prize.
- **Build & spawn:** spend Fame at a factory to produce a unit from the
  buildlist (§2.4 costs: Infantry 100, Recon 150, Artillery 200, Tank 300).
  The unit **spawns on the factory hex if it's free, otherwise an adjacent
  free hex; if the factory is boxed in, the build waits.** Fame has no hard
  cap — deployment is throttled by board space, not a point ceiling.
- **Combat Fame:** destroying an enemy unit pays **~half its Fame cost**
  (e.g. a Tank kill = +150 — see change request to make this exact); an
  **undamaged strike** (attacker takes no counter) pays a small bonus (see
  open question 1); destroying the enemy **flag pays +500 and ends the
  match**. These feed the same Fame pool and the cap tiebreak (§2.8).
- **Capture:** move an Infantry (the only capturer) onto a town/factory and
  hold to capture over N turns (start N=1–2); a captured objective flips its
  Fame income to the new owner.
- **Starting Fame:** each side opens with **200 Fame** (enough for two
  Infantry or one Artillery on turn 1) plus home-factory income from turn 1.
  Single-player difficulty is a starting-Fame handicap — see §2.9.
- **Repair:** a unit that ends its turn on an **owned Town or Factory and is
  not adjacent to any enemy** heals **+25% of max HP** (rounded down, min 1,
  capped at max) at the start of its next turn — free for the prototype. This
  is the game's only HP-recovery path; without it every unit is a one-way
  asset. The **not-adjacent clause is the anti-fortress lock**: a unit must
  break contact to repair, so a factory next to the front never becomes
  unkillable — and because repairing earns zero combat Fame, a repair-turtle
  still loses the cap tiebreak (§2.8). *(Heal %, and a possible small Fame
  cost, are tuning levers.)*

### 2.8 Turn structure & victory
- **Primary win — decisive victory:** destroy the enemy flag unit. Ends the
  match immediately.
- **Secondary win — territorial domination:** control **every factory on the
  map** at the start of your turn. Ends the match immediately and is ranked a
  **Decisive win**, equal to a flag kill. Because taking the last factory
  means capturing the enemy home factory deep in their territory, a flag kill
  is usually already available by then — this is an **active backstop that
  closes out a flag-turtle stalemate before the cap**, not a common win.
  Factories only (towns excluded), so it stays hard-won.
- **Loss:** your own flag unit is destroyed, or the enemy dominates all
  factories.

**Turn cap → attrition tiebreak.** If neither flag has fallen by the turn cap
(20 turns — see change request pinning the value), the match resolves as a
battle of attrition. The full procedure is one guard, one three-key
comparison, and one grade. Every input is a value the game already tracks for
the economy (§2.7) and already shows on the standings scoreboard (§2.11): the
tiebreak adds no new state, only an ordering over existing state.

*Tally definition.* A side's **combat Fame** is the Fame it earned from unit
kills and undamaged-strike bonuses (§2.7). It **excludes** passive factory and
town income — counting income would let a staller re-earn the turtle exploit
(§1.5 #1) by sitting on objectives. The flag bonus (+500) can never appear in
a capped tally: destroying the flag ends the match immediately, so no match
that reaches the cap contains one.

*Resolution procedure, in order:*

1. **Mutual-passivity guard.** If *both* sides' combat Fame is zero — nobody
   engaged — the match is an immediate **draw**. It does not fall through to
   the keys below, because "objectives held" would otherwise re-crown a turtle
   who simply sat on more factories.
2. **Lexicographic comparison** — higher wins at the first key that differs:
   1. **Combat Fame earned.** The anti-turtle lever (PX-4): a player who
      sealed a corner and refused to fight scores zero here and loses the cap
      to anyone who dealt damage. (The guard already covers the both-zero
      case, so no separate "both sides fought" precondition is needed on the
      later keys — if this key ties at a nonzero value, both sides fought by
      construction.)
   2. **Objectives held** — the factories and captured towns a side owns at
      the cap, as *X of N*. Ownership only: a capture in progress (§2.7)
      counts for nobody until the objective flips. Towns count here even
      though the domination win is factories-only — domination must stay
      hard-won; this key merely breaks an exact Fame tie. With ~4 factories
      plus towns on the map (§2.3, §2.7) this is a genuine spread.
   3. **Surviving strength** — total remaining HP of a side's units.
      Deliberately last: alone it would re-reward turtling, but by the time it
      applies both sides have earned identical nonzero combat Fame, so an HP
      edge measures trading efficiency between two sides that both fought.
      It is free to compute (the scoreboard already sums it) and decides
      matches that would otherwise be draws.
3. All three keys equal → **draw**. Acceptable for the prototype; a
   competitive build would add a sudden-death overtime.

**Victory quality.** A result is graded as a **tier**, not a number:

| Tier | Trigger |
|---|---|
| **Decisive win** | Enemy flag destroyed, or territorial domination |
| **Marginal win** | Led the attrition comparison at the cap |
| **Draw** | The passivity guard fired, or all three keys tied |

Tiers rank categorically: a **decisive win always outranks a marginal win**,
regardless of how much Fame either side piled up. Combat Fame is only the sort
key *inside* the tiebreak, never the grade — keeping the two separate prevents
a long capped match's accumulated kill-Fame from "outscoring" an actual flag
kill (§1.5 #5). For self-play tuning, log the tier plus the Fame breakdown per
match. The result: a flag kill is always the best outcome, so Pillar 2 ("short
and decisive") is enforced by the grading itself, not just by the turn cap.

*Invariants (each phrases directly as a `T-CAP-` test):*

1. **T-CAP-01** — Flag destruction on any turn at or before the cap yields a
   Decisive result; the tiebreak procedure is never evaluated.
2. **T-CAP-02** — Both sides at zero combat Fame at the cap → Draw, regardless
   of objectives held or surviving HP.
3. **T-CAP-03** — Passive income never decides the cap: a side holding 4
   factories with zero kills loses the cap to a side holding 1 factory with
   one Infantry kill.
4. **T-CAP-04** — No capped tally contains the +500 flag bonus.
5. **T-CAP-05** — A capture in progress at the cap contributes zero to
   "objectives held" for either side.
6. **T-CAP-06** — Tier order is Decisive > Marginal > Draw for *any* pair of
   Fame totals.
7. **T-CAP-07** — Determinism: identical end state at the cap → identical
   result and tier.
8. **T-CAP-08** — Controlling every factory at the start of your turn ends the
   match immediately as a Decisive win; towns do not count toward domination.

> **Why this shape (the delete-test).** Every piece of the apparatus was
> tested by deletion. Delete key 1 → the documented turtle exploit (§1.5 #1)
> returns whole. Delete the guard → a four-factory turtle beats a one-factory
> turtle without a shot fired. Delete key 2 → contesting the neutral factories
> (§2.7's mid-game prize) stops mattering at the cap. Delete key 3 → more
> draws for zero savings, since the HP sum already exists for the scoreboard.
> Delete the tiers → a capped grind's tally can read as "beating" a flag kill
> in tuning logs — the inversion §1.5 #5 closed. Delete the domination
> backstop → a walled-in flag forces every such match to run the full cap for
> a Marginal result instead of ending early and Decisively (Pillar 2). The one
> piece that failed the test — the floated per-turn Fame decay — is cut (see
> change request). What remains is a guard, a sort, and an enum, all over
> state the game tracks anyway.

**On the turn cap vs. real time.** The cap bounds *turns*, which guarantees
the match terminates; it does not bound wall-clock minutes. Against the
shipping single-player AI (which moves instantly) that is a non-issue, so
"~20 minutes" (§1) is an expected duration at a normal move pace, not a hard
real-time ceiling. The only mode that would need a per-turn timer is **PvP
hotseat**, a stretch feature (§2.10) — if it ships, add a move clock there.

### 2.9 Opponent AI (runtime gameplay system)
- **Baseline (ships): simple objective-seeker.** Two phases each turn, so the
  AI actually *uses* the economy (§2.7), not just the map:
  - **Economy phase.** At each factory it holds: if it can afford a unit,
    build one from a default buildlist (mostly Infantry, an occasional Tank),
    spawning per §2.7. It spends Fame and replaces losses instead of hoarding.
  - **Unit phase, per unit:** (1) an idle **Infantry** adjacent to or near an
    uncaptured, **undefended** factory/town moves onto it to capture — the AI
    contests objectives, keeping capture, production, and the "objectives
    held" tiebreak live on *both* sides; (2) if an enemy is within reach after
    moving, attack — prefer the enemy flag, else the best expected-damage
    target; (3) ranged units (Artillery) fire from maximum standoff so they
    don't eat a counter; (4) otherwise advance along the cheapest path toward
    the enemy flag.
  - One cheap guard keeps it from looking broken: **skip a strictly-losing
    attack** (the unit would die and trade down).

  Deliberately un-clever — decisive, readable, and fully testable. This is the
  shipping opponent.
- **Difficulty = a starting-Fame handicap, not a smarter AI** (mirrors
  *Conflict*). The baseline routine is identical at every tier; only the
  economy shifts: **Easy** = player +150 opening Fame; **Normal** = even
  (200/200, §2.7); **Hard** = player −100. Deterministic and trivially
  tunable, with no AI-quality risk. *(Stretch dial, documented only: also
  scale AI income ±25%/tier.)*
- **Stretch: AI second pass (utility + threat map).** Upgrade the baseline to
  score candidate actions on attack value (expected damage vs. counter),
  objective proximity, and safety (a threat map of enemy reach). Week-3 work,
  only if the baseline proves too exploitable in self-play.
- **Stretch: LLM commander.** Serialize the board to text, enumerate legal
  moves, ask the model to rank one, then **validate and apply** (never trust
  an unchecked move). Behind a toggle, heuristic as fallback. This is the one
  place an AI *agent* appears in the shipped product — see §3.

### 2.10 Scope table

| | Contents |
|---|---|
| **IN** (core; phased wk 1–3 per §4.4) | Grid; 4 units; **6 terrains + the Factory tile**; move + attack; **multiple factories** (home-per-side + contested neutrals, ~4) + capture + Fame production *(these land wk 3, not wk 1–2)*; heuristic AI; **one hand-built scenario**; win-by-flag; functional UI |
| **STRETCH** (if ahead) | 2nd–3rd scenario; LLM commander; fog/recon; sea/air units; map-gen MCP toolset; 2-player hotseat |
| **CUT** | All 16 original scenarios; campaign/meta; zones of control; elaborate art; anything real-time |

### 2.12 Lineage extraction — what we kept, diverged, and cut from *Conflict*

The prototype was digested against the original *Conflict* (Vic Tokai, NES,
1989) manual so the lineage is a deliberate set of decisions, not an accident.
**Kept and mapped:** hex board, terrain move/defense, capturable
towns/factories, factory production, a single Fame currency, held-objective
income, and destroy-the-commander victory. **Extracted as new pillar-fitting
features:** the *Bridge* terrain (§2.3), *Repair* at owned objectives (§2.7)
— the one survivable slice of *Conflict*'s logistics — *starting Fame +
difficulty-as-Fame-handicap* (§2.7, §2.9), the *territorial-domination*
secondary win (§2.8), and an all-1.0 *type-effectiveness* lever (§3 spec).
**Deliberately diverged/cut** (recorded so the choice is on the record, not
implemented): the real-time **battle mini-game** (NORMAL/AUTO + weapon/
maneuver menus + evasion %) → replaced by the deterministic forecast
(Pillar 1); **fuel/ammo logistics** and their supply units → cut for pacing;
the **16-map password campaign** → one polished scenario; and *Conflict*'s
**combat Fame penalties** (retreat/base/flag) → omitted so a flag kill can
never be out-piled by attrition (Pillar 2, §1.5 #5). **Declined levers:** the
per-turn **activation cap** (3-Units mode) and **one-type-per-turn**
production — both lean against Pillar 2 or duplicate the existing board-space
throttle.

## Change requests

| Existing § | Current text | Proposed change | Why |
|---|---|---|---|
| §2.8 | "the turn cap (e.g. 20 turns)" | Pin the cap: "the turn cap (20 turns)" | *Re-filed from stage 1 (unmerged).* The `T-CAP-` suite needs a constant; §1, §2.4, and §2.7 already scale every economy number to "~20-turn matches". An "e.g." cap is not machine-checkable. |
| §2.8 | "an optional per-turn decay past an expected turn count can further nudge toward closing matches out" | Strike the sentence (the consolidated draft omits it). | *Re-filed from stage 1.* Unpriced, unowned, and redundant — the combat-Fame key already makes stalling a losing line. It failed the delete-test, and a floated-but-undefined lever is exactly what the kb parser will trip on. |
| §2.7 | "destroying an enemy unit pays **~half its Fame cost** (e.g. a Tank kill = +150)" | "destroying an enemy unit pays **exactly half its Fame cost** (Infantry 50 / Recon 75 / Artillery 100 / Tank 150)" | *Re-filed from stage 1.* Kill Fame is the tiebreak's primary key; a "~" value is not a pure function of inputs (Pillar 1). All four costs are even, so half is exact — the derived values invent nothing, and the Tank example already confirms 150. |
| §2.10 | "5 terrains" (IN row) | "6 terrains + the Factory tile" (the draft already carries this) | Reconciles the scope table to §2.3, which has shipped 6 movement terrains + Factory since the Bridge/Factory fold. The stale count is drift inside the GDD itself. |
| §1 (Scope at a glance) | "four units, five terrains" | "four units, six terrains plus the capturable Factory tile" | Same reconciliation as above. §1 is outside my file — Director edit at merge time. |
| §2.4 | "…rather than in a lookup table (Pillar 4)" | "(Pillar 3)" (the draft already carries this) | Miscitation: Pillar 4 is "minimal art, maximal system"; depth-from-data-not-feature-count is Pillar 3. |

## Open questions for the Director

1. **The undamaged-strike bonus is still unpriced** *(re-filed from stage 1)*.
   §2.7 says "a small bonus" with no number, yet it feeds the tiebreak's
   primary key, so criterion 1 cannot be fully specified, tested (T-CAP-03
   tallies), or synced to the kb until it is resolved. Options: (a) price it;
   (b) keep it in the Fame pool but exclude it from the cap tally until
   priced; (c) cut it — kills already pay half-cost, and the positional RPS
   already rewards a clean standoff strike with tempo. I recommend (c), with
   (b) as the fallback; either unblocks the `T-CAP-` suite immediately.
2. **Confirm the capture-in-progress ruling** *(re-filed from stage 1)*. The
   draft resolves an ambiguity conservatively: at the cap, an objective counts
   only for its current owner; mid-capture counts for nobody (grounded in
   §2.7's flip-on-capture wording, which grants nothing before the flip). If
   the Director wants partial credit instead, key 2 needs a fractional-count
   rule and T-CAP-05 inverts. Blocks T-CAP-05 and the kb victory table.
3. **Recon's "ignores some terrain cost" is unquantified.** §2.3 states move
   cost is per movement class, but Recon's class has no per-terrain cost row —
   "some" is not a rule. This blocks the Movement & pathfinding ledger row
   (§3), the reachable-hex highlight's correctness tests, and the terrain
   DataTable schema (tech-director's lane). Needs a per-terrain move-cost
   column for Recon's movement class; I do not propose values, since none
   exist in the document.
4. **Capture duration "start N=1–2" is a range, not a value.** A deterministic
   capture test and the AI's capture step (§2.9) both need one N. Blocks the
   capture-system spec stub. Director picks; either value in the stated range
   is consistent with the rest of the document.

## Handoffs

- **ux-onboarding-designer:** §2.11 is left entirely to their stage-2 draft —
  this consolidation cites it (§2.6 forecast, §2.8 scoreboard, PX-5) but does
  not touch it. Two dependencies from the rules side: (a) the scoreboard's
  "enemy-strength-destroyed" figure must be labeled as *combat Fame — excludes
  factory income*, or players will read their income-swollen pool as their cap
  standing; (b) PX-1–PX-6 are written to double as onboarding beats (each goal
  is a thing the tutorial can demonstrate) if they want them.
- **scenario-designer:** the §2.7 layout promise — home factory per side plus
  2+ contested neutrals, ~4 total — is load-bearing for PX-1, PX-4, and
  tiebreak key 2. Their stage-2 map spec should assert it as a validation
  rule, not repeat it as prose.
- **tech-director:** the `T-CAP-01..08` block seeds the "Turn loop & win /
  tiebreak" spec stub (§3 ledger, *pending*); PX-1's check belongs in the
  balance-harness report format and PX-2's in the combat test gate; open
  question 3 (Recon movement class) directly shapes the terrain DataTable
  schema.
- **Director (merge checklist) — kb drift, GDD wins in all cases** *(re-flagged
  from stage 1, still present)*: `kb_rules.md` (a) terrain table is missing
  the **Bridge** and **Factory** rows and states "only Town is capturable,"
  contradicting §2.3; (b) victory table omits §2.8's territorial domination
  as a Decisive trigger; (c) the gate-verified **Repair** rule (§2.7, §3
  ledger 2026-07-29) is absent from the economy section; (d) kb says "Move
  cost is per land unit" where the GDD says per movement class.

## Grounding

- **PX-1**: match length 10–15 min typical / ~20 worst-case — §1 Concept;
  turn-length distributions as a harness output — §4.1; pacing as the
  lineage's named flaw — §1 Lineage, §4.5.
- **PX-2**: forecast-equals-resolution, no hidden rolls, seeded RNG — §2.6;
  determinism invariant style — §3 Combat spec.
- **PX-3**: positional triangle, eff ships all-1.0 — §2.4; §3 TypeEff line.
- **PX-4**: combat-Fame-first tiebreak, income excluded, passivity guard —
  §2.8; turtle-exploit history — §1.5 #1.
- **PX-5**: live standings scoreboard with tiebreak inputs and turn counter —
  §2.11; "never a hidden win condition" — §2.11.
- **PX-6**: one pool, not three — §2.7; §1 decision 2.
- §2.1–§2.6 draft text: consolidated from the same-numbered GDD sections; all
  tables (terrain, units) copied value-for-value from §2.3 and §2.4.
- §2.7 draft: all numbers (100/25 income, build costs, ~half-cost kills, +500
  flag, N=1–2 capture, 200 starting Fame, +25% repair with min 1) — GDD §2.7
  verbatim.
- §2.8 draft: win/loss conditions, domination-as-Decisive at start of turn,
  towns excluded — §2.8; tiebreak order, guard, tiers, draw — §2.8 criteria
  1–4 and Victory quality; folded stage-1 rework (this file's prior
  revision), whose every claim was grounded to §2.8/§2.7/§1.5 in its own
  Grounding section; kb_rules.md "Victory & outcomes" agrees on the order.
- "20 turns" as the cap value: §2.8 "(e.g. 20 turns)" plus the "~20-turn
  matches" scaling basis in §2.4/§2.7 — pinning it is a change request, not
  asserted as settled.
- §2.9 draft: two-phase AI, buildlist, capture step, standoff fire,
  strictly-losing-attack guard, difficulty Fame handicaps (+150/even/−100,
  ±25% stretch) — GDD §2.9 verbatim.
- §2.10 draft: IN/STRETCH/CUT rows — GDD §2.10; the terrain-count correction
  is grounded in §2.3's table and filed as a change request.
- §2.12 draft: kept/extracted/diverged/declined lists — GDD §2.12 verbatim in
  substance.
- Pillar 3 vs Pillar 4 citation fix: §1 Design pillars list.
- kb drift items: kb_rules.md terrain/victory/economy sections vs GDD §2.3,
  §2.8, §2.7, §3 ledger.
