# Scenario & map design — stage-2 draft (scenario-designer)

## Placement

New section **§2.13 Scenario & map design**, inserted after §2.12 (Lineage
extraction) and before §3. The GDD currently has no spatial specification at
all — "one hand-built scenario" (§2.10) and the §2.7 starting-layout bullet
("home factory per side + two or more neutral, ~4 total") are the only
anchors. This section becomes the concrete referent for both, and for the
§4.4 wk-2 milestone ("the one scenario"). It supersedes and absorbs my
stage-1 draft (the replay-cliff plan), which becomes subsection §2.13.4 here;
map names, the asymmetric-shipping-map decision, and the stage-1 open rulings
are carried forward unchanged for continuity.

## Draft

> *All layout values are starter/tuning targets, per the GDD's standing
> convention (§2.3, §2.7). Nothing here adds a unit, terrain, or rule: the
> palette is the six movement terrains + the capturable Factory tile (§2.3)
> and the four-unit roster (§2.4), exactly.*

### §2.13 Scenario & map design

#### 2.13.1 Layout conventions (shared by every map)

- **Coordinates:** `(col, row)`, col 0 = west, row 0 = north; pointy-top
  hexes (§2.2), odd rows offset +½ hex east (odd-r). ASCII glyphs: `p`
  Plains · `w` Woods · `m` Mountains · `~` Water · `B` Bridge · `T` Town ·
  `F` Factory.
- **Factories:** each side owns exactly one **home factory** at start;
  all others are **neutral** (no income until captured, §2.7). The factory
  set is also the §2.8 territorial-domination win set, so factory count and
  placement is the primary match-length dial (see 2.13.5).
- **Starting force (standard):** **5 units per side — 1 Flag Tank (§2.4,
  not producible), 2 Infantry, 1 Artillery, 1 Recon** — plus 200 starting
  Fame (§2.7) ± the §2.9 difficulty handicap. Rationale: one of each
  producible system is live from turn 1, so the positional RPS triangle and
  capture are in play before the first build; two Infantry means the
  standard opening (one to a town, one to a neutral factory) doesn't consume
  the only capturer; the producible force is worth 550 Fame — about two
  turns of mid-game income — so losing the opening force is recoverable, not
  match-ending. *The GDD never sizes the starting force; this number is
  filed as a Change request, not silently adopted.*
- **Home factory hex starts empty** in every deployment, so the turn-1
  build spawns on the factory itself (§2.7 spawn rule) instead of scattering.
- **Validation invariants** (for the §4.2 `validate_scenario` tool — schema
  handoff to tech-director): every land-passable hex reaches every factory
  (Bridges are the only Water crossings, §2.3, and there is no sea unit —
  connectivity is a build-time check, not a hope); all deployment hexes are
  free and land-passable; factory count in the map file equals the count the
  domination check uses; declared symmetry (mirror/rotation/none) is
  machine-verified.

#### 2.13.2 The shipped scenario — *Ferrum Crossing* (§2.10 IN)

| Spec | Value |
|---|---|
| Dimensions | **11 × 9 = 99 hexes** |
| Starting units per side | **5** (standard force, 2.13.1) |
| Factories | **4** — one home per side + 2 neutral (verbatim the §2.7 "~4 total" layout) |
| Towns | **4** |
| Turn cap | **20 turns** (fixes §2.8's "e.g. 20" for this scenario) |
| Symmetry | **Asymmetric** — handicap story below |
| Estimated match length | **12–16 turns** (reasoning below) |

**Layout.**

```
r0:  p  p  p  p  p  ~  p  p  p  p  p
r1:   p  p  p  T  p  B  w  p  T  p  p
r2:  p  p  w  p  p  ~  F  w  p  p  p
r3:   p  p  p  w  p  ~  w  p  p  p  p
r4:  p  F  p  p  p  B  w  w  p  F  p
r5:   p  p  w  p  p  ~  p  p  p  p  p
r6:  p  p  p  p  m  p  m  T  p  p  p
r7:   p  p  T  p  p  F  p  p  p  p  p
r8:  p  p  p  p  p  p  p  p  p  p  p
```

**Key coordinates.** Water (5,0)(5,2)(5,3)(5,5) · Bridges **(5,1)** north,
**(5,4)** center · Home factories: West **(1,4)**, East **(9,4)** · Neutral
factories: **North (6,2)** on East's bank, **South (5,7)** in the mountain
pass · Towns (3,1)(8,1)(2,7)(7,6) · Pass mountains (4,6)(6,6) · Woods bands:
East bank (6,1)(7,2)(6,3)(6,4)(7,4), West approaches (2,2)(3,3)(2,5).

**Terrain distribution (99 hexes):** Plains 75 · Woods 8 · Mountains 2 ·
Water 4 · Bridge 2 · Town 4 · Factory 4. Three-quarters open ground is
deliberate: movement stays fast (§2.3 cost 1), contact comes early, and the
match fits Pillar 2's 10–15-minute envelope — cover is a *purchase*, not the
default.

**Starting positions** (all on Plains; home factory hex left free):

| Unit | West | East |
|---|---|---|
| Flag Tank | (0,4) | (10,4) |
| Infantry ×2 | (1,3), (1,5) | (9,3), (9,5) |
| Artillery | (0,3) | (10,5) |
| Recon | (0,5) | (10,3) |

**Terrain as economics, hex by hex.** The river spans rows 0–5 only, crossed
at two Bridges (−10% defense, §2.3): a unit forcing a crossing under
Artillery (range 2–3, no counter, §2.4) buys ground with HP — the intended
price. The river deliberately does **not** bisect the map: the southern pass
(row 6) is a bridge-free route priced by two Mountains (cost 3, +40%), so it
is the *slow* flank, never a free one. The one-hex river also means opposite
banks are distance 2 — inside Artillery range, and the prototype ships
without line-of-sight blocking (§2.2) — so bank control is contested by fire
even before anyone crosses. East's bank carries the Woods band (+20%):
cover in exchange for the longer road south. West gets open Plains: speed
in exchange for fighting uncovered. The South neutral factory sits between
the pass Mountains — +15% defense and a spawn point anchoring the southern
flank; the North neutral sits on East's bank, so West must win a bridge to
contest it. Rear towns (3,1)/(2,7) west and (8,1)/(7,6) east are the repair
points (§2.7): the anti-fortress clause (no repair adjacent to an enemy)
keeps the forward ones from healing a frontline garrison.

**The tactical question this map asks:** *which neutral factory do you race,
and which bridge do you contest — knowing the two answers pull a 5-unit army
in opposite directions?* West's fast prize is South (open Plains approach);
East's is North (no crossing needed). Committing to both splits the army
into halves that lose either fight.

**Asymmetry and its handicap story.** Starting Fame and forces are
identical; the asymmetry is purely spatial and intended to be
self-balancing — each seat is closer to a different neutral factory, and
each seat's advantage (West: tempo and open approaches; East: cover and a
crossing-free path to its prize) is the other's problem. If §4.1 self-play
shows either seat above ~55% win rate, the corrective is the existing §2.9
dial — a per-seat starting-Fame offset — never a terrain rework. This is
also the replay lever: the two seats are two different deterministic
puzzles (see 2.13.4).

**If one side holds both bridges:** the other side is not locked out — the
southern pass exists precisely so bridge control here is *tempo*, not a
topological wall. A double-bridge holder who then sits earns zero combat
Fame and loses the §2.8 cap tiebreak (or draws under the mutual-passivity
guard); meanwhile the cross-river Artillery duel and the open southern pass
keep combat Fame available to both sides. Full lockout as a map premise is
reserved for *The Causeway* (2.13.6), where the tiebreak rules carry the
whole anti-turtle load by design.

#### 2.13.3 Match-length reasoning — and the dial it exposes

**Estimate: 12–16 turns; cap at 20.** Not just the number:

- **Contact turn 3–4.** Homes are 8 columns apart over mostly cost-1
  Plains; Tank (move 5) reaches a bridge or the pass mouth in 2–3 turns,
  Infantry (move 3) in 3–4.
- **Economy online turn 3–4.** Each side's near Infantry reaches its
  closest neutral factory in ~2 turns; capture at N=1 (fixed from §2.7's
  "start N=1–2" range — Open question 2) flips income the following turn.
  Income ramps 100 → ~225–250 Fame/turn: a reinforcing unit every 1–2
  turns, continuously feeding the fight without flooding it (board space is
  the throttle, §2.7).
- **Kill speed.** Damage is punchy against 8–20 HP pools (§2.4): units die
  in 2–3 hits, so bridge and pass fights *resolve* rather than accumulate.
  Mid-game runs turns 5–12; the flag hunt closes 12–16.
- At ~45 s/player-turn that is ~10–13 minutes — inside §1's "10–15 typical,
  ~20 at the cap".

**The match-length dial is factory count × home separation.** More neutral
factories → steeper income ramp → bloodier, faster mid-game and a wider
"objectives held" spread at the cap; fewer → slower armies and more stall
risk. Each column of home separation moves the contact turn back roughly
one-for-Tank-move. Scenarios tune these two numbers first; unit and terrain
stats are never per-map (those belong to rules and balance, §3).

#### 2.13.4 Replayability — configurations, not mechanics

Carried from the stage-1 draft, condensed. Stratocracy is deterministic
end-to-end (Pillar 1, §2.6, §2.9's tier-invariant AI), so any line that
beats the AI once beats it forever; by match ~4 a single mirrored map is a
solved puzzle. The replay unit is therefore a **configuration = map × seat ×
difficulty handicap**, each a distinct deterministic puzzle:

| Matches | Configuration | Ships in |
|---|---|---|
| 1–3 | *Ferrum Crossing*, West seat, Easy → Normal → Hard (§2.9 Fame ladder) | Core |
| 4–6 | *Ferrum Crossing*, **East seat**, same ladder | Core (seat-select = scenario data + one menu affordance) |
| 7–8 | *Longwater March*, Normal → Hard | Stretch P1 (§4.4 wk 4) |
| 9–10 | *The Causeway*, Normal → Hard | Stretch P2 (wk 4, only after P1) |

If no stretch lands, the shipped scope alone moves the cliff from match ~3
to match ~6 — that is what the asymmetric map buys, and why *Ferrum
Crossing* is not mirrored. Honest ceiling: determinism means every
configuration is eventually solved; this multiplies puzzles, it does not
make them unsolvable. The long-term fixes (AI second pass, map-gen MCP
toolset) already sit in the GDD's stretch column and are not re-proposed.

#### 2.13.5 Stretch scenario — *Longwater March* (P1, §4.4 wk 4)

| Spec | Value |
|---|---|
| Dimensions | 13 × 9 = 117 hexes |
| Starting units per side | 5 (standard force — one variable at a time; this map's variable is factory count) |
| Factories | **6** — one home per side + 4 neutral *(above §2.7's "typical ~4", inside its "two or more neutral"; licensed via Change request)* |
| Towns | 4 |
| Symmetry | **Mirrored** — fair and admittedly dull; chosen so the factory-count dial is the only variable under test |
| Estimated match length | **16–20 turns, frequently reaching the cap** |

```
r0:  m  p  p  p  p  p  T  p  p  p  p  p  m
r1:   p  p  p  p  p  p  p  p  p  p  p  p  p
r2:  p  p  p  p  F  p  p  p  F  p  p  p  p
r3:   p  p  p  p  p  p  w  p  p  p  p  p  p
r4:  p  F  p  T  p  w  p  w  p  T  p  F  p
r5:   p  p  p  p  p  p  w  p  p  p  p  p  p
r6:  p  p  p  p  F  p  p  p  F  p  p  p  p
r7:   p  p  p  p  p  p  p  p  p  p  p  p  p
r8:  m  p  p  p  p  p  T  p  p  p  p  p  m
```

Homes (1,4)/(11,4); neutrals (4,2)(8,2)(4,6)(8,6); towns
(6,0)(3,4)(9,4)(6,8); central Woods knot (6,3)(5,4)(7,4)(6,5); corner
Mountains. Deployment mirrors Ferrum Crossing's pattern around each home
(flag on the outside edge, factory hex free). **No Water at all** — the map
that teaches what the chokepoint map can't: open-field maneuver, Recon (move
7) flanking wide, and expansion tempo deciding who holds 4-of-6 at the cap,
so "objectives held" (§2.8 criterion 2) is a genuine 0–6 spread.

**Match-length reasoning:** 4 neutral factories scale income toward 600+
Fame/turn (§2.7) — losses are replaced almost as fast as they land (a Tank
kill pays +150 while the victim's economy rebuilds the Tank in under a turn
at full income). Attrition drags, the flag hides behind rebuilt lines, and
the match leans on the §2.8 tiebreak. That is the point: this is the
scenario that *exercises* the combat-Fame tiebreak and the §2.11 scoreboard,
which on the shipped map rarely fire.

**Tactical question:** *how many factories can you hold with the army those
factories pay for?* Over-expansion strands Infantry on capture duty while
the center Woods fight is lost; under-expansion loses the income race and,
at the cap, the objectives-held sort.

#### 2.13.6 Stretch scenario — *The Causeway* (P2, wk 4, only after P1)

| Spec | Value |
|---|---|
| Dimensions | 9 × 9 = 81 hexes |
| Starting units per side | 5 (standard force) |
| Factories | 4 — one home per side + 2 neutral (conforms to §2.7 ~4) |
| Towns | 2 |
| Symmetry | **180° rotational** — fair, and rotation (unlike mirroring) puts each seat's near bridge on the opposite flank, so seat-swap stays non-cosmetic even on a symmetric map |
| Estimated match length | **8–12 turns** |

```
r0:  p  p  p  p  ~  p  p  p  p
r1:   p  T  p  w  ~  p  p  p  p
r2:  p  p  m  F  B  p  p  p  p
r3:   p  p  p  w  ~  p  p  p  p
r4:  p  F  p  p  ~  p  p  F  p
r5:   p  p  p  p  ~  w  p  p  p
r6:  p  p  p  p  B  F  m  p  p
r7:   p  p  p  p  ~  w  p  T  p
r8:  p  p  p  p  ~  p  p  p  p
```

Water fills column 4 end to end except Bridges (4,2) and (4,6) — **a full
bisection, the deliberate opposite of Ferrum Crossing.** Homes (1,4)/(7,4);
neutral factories (3,2) and (5,6) each guard the approach to their adjacent
bridge: +15% defense *and* a spawn point at the chokepoint (§2.7
build-and-spawn makes a held bridge-factory a reinforcement faucet exactly
where reinforcements matter). Woods overlook each bridge for defenders;
single Mountains (2,2)/(6,6) are Artillery perches — range 2–3 covers the
bridge hex from +40% cover with no counter (§2.3, §2.4).

**Both bridges held — stated in full, because on this map it is the whole
design.** No naval unit, no other crossing: double-bridge control is a true
lockout — the locked-out side cannot reach the enemy flag *or* home factory,
so both the flag kill and territorial domination are out of its reach. The
rules already make this a trap, and the map exists to prove it: the holder
must still *cross* to win decisively; if it sits, it earns zero combat Fame
and **loses the cap tiebreak to any opponent who dealt any damage at all**
(§2.8 criterion 1); if both sides sit, the mutual-passivity guard calls a
draw. Lockout on The Causeway is a tempo platform for a prepared crossing,
never a victory condition — the map that demonstrates §1.5 finding #1 (the
turtle exploit) is dead.

**Match-length reasoning:** homes only 6 columns apart, but every route
crosses a Bridge; the map forces commitment, and the first successful
bridgehead (turn 3–5) usually cascades into the flag kill within 4–6 turns
because the defender's Fame went into defending crossings, not expanding.

**Tactical question:** *how do you buy a bridgehead when the crossing hex
fights at −10% and the far bank fights at +20?* The §2.6 forecast makes the
price exact before you pay it — the scenario where the forecast display
earns its keep.

#### 2.13.7 Scenario-set summary

| Map | Status | Hexes | Units/side | Factories | Towns | Symmetry | Dial it turns | Est. turns |
|---|---|---|---|---|---|---|---|---|
| *Ferrum Crossing* | **Ships** (§2.10 IN) | 11×9 | 5 | 4 | 4 | Asymmetric (Fame-correctable) | baseline / seat asymmetry | 12–16 |
| *Longwater March* | Stretch P1 (wk 4) | 13×9 | 5 | 6 | 4 | Mirrored | factory count → cap pressure | 16–20 |
| *The Causeway* | Stretch P2 (wk 4) | 9×9 | 5 | 4 | 2 | Rotational | bridge lockout → decisiveness | 8–12 |

Neither stretch map may pull work forward of week 4 or block core; if week 4
is consumed by balance (its primary §4.4 purpose), the set stays on paper.

## Change requests

| Existing § | Current text | Proposed change | Why |
|---|---|---|---|
| §2.7 (starting-layout bullet) | Defines starting Fame (200) but never sizes the starting *force* | Add: "Each side also opens with a fixed starting force defined per scenario (§2.13); the shipped scenario fields 5 units per side (Flag Tank, 2 Infantry, Artillery, Recon)." | §2.9 and §1.5-#4 assume a starting force exists; no source number sizes it. The 5-unit count is this draft's proposal and needs Director approval, not silent adoption. |
| §2.8 (turn cap) | "the turn cap (e.g. 20 turns)" | "the turn cap (a per-scenario value; 20 turns on the shipped scenario, §2.13)" | The cap drives every match-length estimate; "e.g." leaves the shipped value formally undefined. Per-scenario, because *The Causeway* (8–12 expected) reads better at ~15 while *Longwater March* wants the full 20. |
| §2.7 (factories bullet) | "A typical small skirmish map has **~4 factories total**." | Append: "(scenarios may vary this — factory count is the match-length dial, §2.13)" | *Longwater March* uses 6: inside "two or more neutral", above "typical ~4"; one clause makes the variation licensed instead of drift. |
| §2.10 (IN and STRETCH rows) | "**one hand-built scenario**" / "2nd–3rd scenario" | "one hand-built scenario (§2.13 *Ferrum Crossing*)" / "2nd–3rd scenario (priority order in §2.13: *Longwater March*, then *The Causeway*)" | Cross-references; makes the wk-4 stretch decision pre-made at zero scope cost. |
| §2.9 (difficulty bullet) | "**Easy** = player +150 … **Hard** = player −100." | Append: "The same dial doubles as the per-seat balance corrective for the asymmetric shipped map (§2.13): if self-play shows a seat >~55%, offset that seat's starting Fame rather than reworking terrain." | The asymmetric map's handicap mechanism, using an existing dial — no new rule. §2.9 is rules-designer's lane; needs their sign-off. |
| §2.4 (Recon row) | "ignores some terrain cost" | Specify exactly which terrains and at what cost (rules-designer's lane) | Un-validatable as written — whether Mountains gate Recon changes the flanking geometry of every map above. |

## Open questions for the Director

1. **Approve the 5-unit standard starting force** (2.13.1) — the one number
   family in this draft with no source antecedent, alongside map dimensions
   and town counts (all flagged above).
2. **Capture N fixed at 1** for the shipped scenario (within §2.7's "start
   N=1–2")? N=2 delays the income ramp a turn and adds ~1–2 turns to the
   estimate; N=1 better serves Pillar 2 at this map size.
3. **Recon/Air vs. Water — carried from stage 1, still the sharpest open
   ruling.** §2.3 marks Water passable by "sea, air"; §2.4's "Recon/Air"
   never says whether it *is* air. If Recon crosses Water freely, the
   Causeway lockout and every bridge chokepoint leak. All three maps assume
   the conservative reading: **Recon is a land unit with terrain-cost
   discounts**, and bridges bind it. Needs a ruling (routed to
   rules-designer).
4. **Cross-Water Artillery fire at distance 2 is load-bearing.** With LOS
   blocking a stretch goal (§2.2), bank-to-bank fire across a one-hex river
   is legal at ship, and both river maps use it (it is part of what prices a
   bridge lock on *Ferrum Crossing*). If LOS blocking ever ships, Water must
   not block, or those maps need a redesign pass. Confirm.
5. **Seat-select scope:** confirm that choosing your seat on the shipped map
   is in scope as "scenario data + one menu affordance" (my read: yes — the
   cheapest replay lever in this document), or the East seat moves to
   stretch and the shipped replay ceiling drops from 6 configurations to 3.

## Handoffs

- **rules-designer:** (a) the Recon/Water ruling (Open question 3); (b) the
  ranged-fire-over-Water confirmation (Open question 4); (c) sign-off on the
  §2.9 per-seat Fame corrective and the §2.7 starting-force sentence; (d)
  the §2.4 Recon terrain-cost specification (Change request).
- **tech-director:** the scenario schema this section implies — map
  dimensions, terrain grid (glyph codes above), initial ownership
  (home vs. neutral per objective), per-seat deployment lists with a flag
  designation, seat-selection flag, per-scenario turn cap and capture-N —
  plus the `validate_scenario` invariants listed in 2.13.1 (connectivity via
  bridges, free spawn hexes, factory-count agreement with the domination
  check, declared-symmetry verification).
- **ux-onboarding-designer:** (a) seat-select + difficulty-select on match
  start (the delivery mechanism for matches 4–6); (b) on the shipped map the
  §2.8/§2.11 "objectives held X/N" scoreboard has **N = 8** (4 factories +
  4 towns); (c) the attack forecast is the natural teacher of Bridge −10% —
  the first forced crossing shows the penalty before commit; (d) *Longwater
  March*, if it ships, is the scenario where the live scoreboard carries the
  match — worth HUD emphasis.
- **Director (merge checklist step 3):** `kb_rules.md` is stale against GDD
  §2.3/§2.8 — its terrain table is missing the **Bridge** and **Factory**
  rows and its outcomes table is missing **territorial domination**. The GDD
  wins; the KB needs its §2 re-parse at merge or the A#4 critic validates
  content against dead rules. Title/lineage framing remains unowned (no
  narrative-designer in this kit) — not touched here.

## Grounding

- **99-hex shipped map, 75% Plains, contact turn 3–4** ← §1 "small
  skirmish-sized hex map", Pillar 2, the §1 10–15-minute envelope; contact
  math from §2.4 Move values (Tank 5, Infantry 3, Recon 7) over §2.3 costs.
- **4 factories = home per side + 2 neutral** ← §2.7 starting-layout bullet,
  quoted numbers.
- **Bridges as the sharpest chokepoint / no bypass by sea** ← §2.3 (Bridge
  is "the only hex a land unit crosses Water", −10% defense) + §2.4 roster
  (no sea unit) + §2.10 (sea/air units STRETCH).
- **Non-bisecting river on the shipped map vs. full bisection on The
  Causeway** ← §2.8's anti-turtle stack (combat-Fame-first tiebreak,
  mutual-passivity draw, domination backstop) makes full lockout safe to
  ship as a *stretch* premise; the shipping scenario avoids leaning on
  edge-case rules — §1.5 finding #1 is the cautionary record.
- **Cross-river Artillery duel at distance 2** ← §2.4 Artillery range 2–3 +
  §2.2 (LOS blocking is stretch, i.e. absent at ship).
- **Bridgehead factories as reinforcement faucets** ← §2.7 build-and-spawn
  ("spawns on the factory hex if free, else adjacent").
- **Repair placement (rear towns heal, forward ones don't)** ← §2.7 repair
  rule + its "not adjacent to any enemy" anti-fortress clause — checked so
  no map creates an unkillable chokepoint garrison.
- **Income-ramp and reinforcement arithmetic** ← §2.7 (+100/factory,
  +25/town, unit costs 100–300, starting Fame 200, kill ≈ ½ cost).
- **Capture timing in every estimate** ← §2.7 (Infantry-only capture,
  N=1–2) + §2.4 movement + §2.3 costs.
- **Turn cap 20 and tiebreak order** ← §2.8 ("e.g. 20 turns"; combat Fame →
  objectives held → surviving HP → draw; mutual-passivity guard).
- **Factory count as the match-length dial** ← §2.7 (income slope) + §2.8
  (domination is defined over the factory set): count sets both the economy
  and the size of the win set — hence *Longwater March*'s 6-factory
  cap-pressure design and its 0–6 objectives spread.
- **Asymmetry corrective via starting Fame** ← §2.9 already uses Fame
  offsets as the difficulty mechanism (Easy +150 / Hard −100); per-seat use
  is a new application of an existing dial, filed as a Change request.
- **Replay = configurations** ← Pillar 1 + §2.6 determinism + §2.9
  (tier-invariant AI) + §2.10 (closed roster/terrain): with variance and new
  mechanics both off the table, layout × seat × handicap is the only replay
  surface — the stage-1 finding, carried forward.
- **One scenario ships; stretch at wk 4+, priority-ordered** ← §1 resolved
  decision 1, §2.10 scope table, §4.4 wk 4 ("additional scenarios only as
  stretch").
- **Numbers with no source antecedent** — starting-force size, map
  dimensions, town counts, *Longwater March*'s 6th factory, the fixed cap
  values — are all flagged in Change requests / Open questions, per the
  no-invention rule.
