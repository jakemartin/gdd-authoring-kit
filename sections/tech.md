# Technical design — stage-2 draft (tech-director)

## Placement

Expands **§4 Technical Strategy** with four new subsections and small amendments
to existing §4 text (see Change requests):

- **§4.7 Pending-system gate plan** — the eight `*pending*` §3 ledger rows, each
  with a gateable spec stub (the stage-1 target). **Filed here in full:** no
  stage-1 draft of this file exists as a repo artifact, so rather than cite one,
  this draft carries every load-bearing definition — stubs, gate IDs, the
  canonical hex order, the scenario-file fields, the UI binding contract, and
  the Q1–Q10 rule-gap register — inside itself. The merged §4 is self-contained;
  every ID that §4.8–§4.10 cite resolves within this draft.
- **§4.8 Data contract — DataTable schemas** (canonical CSVs, both-side structs,
  parity gate)
- **§4.9 Headless-module → Unreal integration path** (module layout, bridge,
  command/event boundary, parity gates)
- **§4.10 Save & replay format** (one format serving save/load, the integration
  parity gate, and the Balance Analyst's self-play logs)

Test-ID prefixes reserved by this draft: **T-HEX, T-DATA, T-MOVE, T-FAME,
T-TURN, T-AI, T-SCN, T-UI** (§4.7) and **T-INT** (integration parity),
**T-SAVE** (save/replay) (§4.9–§4.10).

**Project state, stated plainly:** four ledger rows are built and gate-verified —
Combat resolution, its test suite, Repair, and Type-effectiveness, all at commit
`5ffa8d6`, 17/17 invariants on a live `g++`/`clang++` compile. **Nothing else in
this draft exists as code.** `Source/` is still the stock Unreal template; every
stub, schema, module, and format below is a specification with gates attached,
written so its ledger row can flip the same way Combat's did.

## Draft

### §4.7 Pending-system gate plan — the eight `*pending*` ledger rows

Each stub below follows the proven Combat-spec shape (§3): Inputs, Formula or
state transition, Invariants (one per assertable rule), Determinism, Acceptance
test IDs. All rules code is **headless** — `namespace strat`, pure C++17, zero
engine dependencies, compiled by the same `g++`/`clang++` + `python run.py` gate
that certified Combat (§3 ledger). Where a stub needs a rule the GDD does not
state, the gate is parameterized on a numbered open question (Q1–Q10, Open
questions below) — the Director rules, the gate then pins the ruling.

**Shared conventions (Director-owned contract):**

- **Coordinates:** axial `(q, r)`, pointy-top hexes (§2.2). Distance is the
  standard axial hex metric `(|dq| + |dr| + |dq + dr|) / 2` — pure integer math.
- **Canonical hex order** (the subject of T-HEX-07): a total order over hexes —
  **ascending `r`, then ascending `q`**. Used everywhere enumeration order could
  leak into behavior or bytes: reachable-set enumeration, movement/AI tie-breaks
  (T-MOVE-04, T-AI-06), scenario serialization and hashing (Stub 7), and the
  §4.10 canonical state hash.
- **Numbering:** stubs 1–8 below are also the build-order row numbers (Build
  order table).

---

```
SPEC STUB 1: Hex grid & math               (Director → Systems Engineer)
Inputs:  map dimensions (Q1); axial coords (q, r).
Functions: neighbors(hex) — the six adjacent hexes in a fixed, documented
         enumeration order, out-of-bounds candidates filtered; distance(a, b);
         inBounds(hex).
Invariants:
  T-HEX-01  every in-bounds hex has exactly six neighbor candidates in the fixed
            order; filtering removes only out-of-bounds hexes (§2.2 "six equal
            neighbours")
  T-HEX-02  distance is a metric: d(a,a)=0; d(a,b)=d(b,a); triangle inequality
  T-HEX-03  d(a,b)=1  ⟺  b ∈ neighbors(a)
  T-HEX-04  direction fairness: each of the six unit steps has distance exactly
            1 — no direction is cheap the way diagonals are on squares (§2.2)
  T-HEX-05  inBounds agrees with the Q1 dimensions; every hex reference the
            engine or a scenario hands the module is bounds-checked, never trusted
  T-HEX-06  single distance definition: combat's range checks (T-COMBAT-06..08 @
            5ffa8d6) consume THIS distance function — Artillery at distance 1
            cannot counter, per the verified module, with no second metric to drift
  T-HEX-07  canonical order + determinism: sorting any hex set by (r asc, q asc)
            is total, stable, and platform-independent; neighbors() enumeration
            order is fixed across runs and compilers
Determinism: pure integer functions; no state.
Acceptance: T-HEX-01..07.
```

```
SPEC STUB 2: Data tables (units/terrain)   (Director → Systems Engineer)
Defined in full in §4.8 (schemas, both-side structs, parity gate). Invariants
T-DATA-01..06 are specified there once — this stub defers to §4.8 rather than
duplicate a contract that must never fork.
```

```
SPEC STUB 3: Movement & pathfinding        (Director → Systems Engineer)
Inputs:  unit {move, moveClass}; terrain move costs (§2.3 via Stub 2); current
         occupancy; start hex.
Transition: reachable set + cheapest paths via Dijkstra over terrain cost (§4.1);
         executing a move relocates the unit along the chosen path (§2.5).
Invariants:
  T-MOVE-01  reachable set is exact: a hex is in the set ⟺ its cheapest path
             cost ≤ Move — "the real move set, not an estimate" (§2.5)
  T-MOVE-02  costs per §2.3: Plains 1, Woods 2, Mountains 3, Town/Bridge/Factory
             1; Water impassable to land — a land path across a Water span
             exists ⟺ it crosses on Bridge hexes (§2.3, "the only hex a land
             unit crosses Water")
  T-MOVE-03  occupancy: a move never ends on an occupied hex (§2.5, one unit per
             hex). Pass-through of friendly-occupied hexes: parameterized on the
             Q3 ruling; until ruled, the gate asserts the conservative reading
             (occupied hexes block pathing entirely)
  T-MOVE-04  the executed path is minimal-cost; ties between equal-cost paths are
             broken by canonical hex order, so the route is reproducible
  T-MOVE-05  no zones of control: moving adjacent to an enemy costs nothing
             extra and freezes nothing (§2.5 — ZOC is cut)
  T-MOVE-06  determinism: same state → identical reachable set and identical path
  (T-MOVE-07 reserved: Recon's "ignores some terrain cost" (§2.4) — blocked on
   the Q2 movement-class ruling; no gate is written until the rule exists.)
Determinism: pure; all tie-breaks canonical.
Acceptance: T-MOVE-01..06 (07 reserved on Q2).
```

```
SPEC STUB 4: Capture & Fame economy        (Director → Systems Engineer)
Inputs:  game state; commands Build{factoryHex, unitId}, Capture{unit}; the §2.7
         income/award values; §2.4 costs via Stub 2.
Transition: income accrual; build-and-spawn; capture progress; kill awards.
Invariants:
  T-FAME-01  single pool (§2.7): income, kill awards, and spending all mutate one
             per-side fameTotal; combat awards ALSO accrue a separate fameCombat
             counter (the §2.8 tiebreak criterion-1 sort key); passive income
             never touches fameCombat
  T-FAME-02  income: each held factory pays +100/turn, each held town +25/turn
             (§2.7); accrual timing per the Q8 ruling
  T-FAME-03  build: deducts the exact §2.4 cost (Infantry 100, Recon 150,
             Artillery 200, Tank 300); refused if unaffordable; fameTotal is
             never negative
  T-FAME-04  spawn: on the factory hex if free, else an adjacent free hex, else
             the build waits (§2.7); waiting-build semantics per Q8
  T-FAME-05  capture: Infantry only (§2.7, §2.4); completes after N turns of
             holding (N per Q4); interruption/reset semantics per Q4
  T-FAME-06  a captured objective's income flips to the new owner (§2.7)
  T-FAME-07  kill awards: ~half the victim's Fame cost, small undamaged-strike
             bonus, flag kill +500 and the match ends (§2.7) — exact values per
             Q5/Q6; the gate pins whatever the Director rules
  T-FAME-08  no Fame cap: fameTotal is unbounded; deployment is throttled by
             board space only (§2.7)
  T-FAME-09  determinism: same state + command → identical Fame deltas and state
Determinism: pure state transitions; no RNG anywhere in the economy.
Acceptance: T-FAME-01..09.
```

```
SPEC STUB 5: Turn loop & win / tiebreak    (Director → Systems Engineer)
Inputs:  game state; per-unit act flags; the turn counter and cap (Q7, stored in
         the scenario file, Stub 7); commands incl. EndTurn{}.
Transition: I-GO-U-GO alternation (§2.1); win/loss/draw evaluation (§2.8);
         start-of-turn repair application (§2.7).
Invariants:
  T-TURN-01  strict alternation; each unit acts at most once per own turn, in
             any order the owner chooses (§2.1)
  T-TURN-02  flag death ends the match immediately — Decisive win for the killer,
             loss for the owner (§2.8)
  T-TURN-03  territorial domination: controlling every factory on the map at the
             start of your turn ends the match immediately, ranked Decisive
             (§2.8; factories only, towns excluded)
  T-TURN-04  at the turn cap, the attrition tiebreak resolves in the exact §2.8
             order: combat Fame → objectives held → surviving HP → draw
  T-TURN-05  mutual-passivity guard: both sides' fameCombat == 0 at the cap →
             immediate draw, with NO fall-through to objectives held (§2.8)
  T-TURN-06  criterion 2 (objectives held, X of N) is evaluated only when both
             sides fought and their fameCombat is equal (§2.8)
  T-TURN-07  result tiers are categorical: Decisive > Marginal > Draw, regardless
             of Fame totals — Fame is only the sort key inside criterion 1 (§2.8)
  T-TURN-08  repair fires at the start of the unit's turn exactly when the
             verified repairAmount says so (owned Town/Factory, no adjacent
             enemy, +25% max HP floored, min 1, capped — T-REPAIR-01..07 @
             5ffa8d6); this gate asserts the turn loop calls it at the right
             moment with the right board facts, nothing more
  T-TURN-09  determinism: the same command sequence from the same scenario →
             identical result tier and identical state at every step
Determinism: pure state machine; the §4.10 hash is taken from this state.
Acceptance: T-TURN-01..09.
```

```
SPEC STUB 6: Opponent AI (baseline)        (Director → Systems Engineer)
Inputs:  full game state (the AI cheats at nothing and sees only real state);
         the §2.9 baseline routine; default buildlist (§2.9).
Transition: economy phase then unit phase, emitting ordinary commands that the
         rules module validates like any player's (§2.9).
Invariants:
  T-AI-01  legality: every AI command passes the same validation as a player
           command; zero rejected commands across N self-play games
  T-AI-02  economy phase: at each held factory, if a buildlist unit is
           affordable, one is built — the AI spends and replaces losses rather
           than hoarding (§2.9)
  T-AI-03  capture behavior: an idle Infantry near an uncaptured, undefended
           factory/town moves onto it to capture (§2.9) — objectives stay live
           on both sides
  T-AI-04  attack preference: the enemy flag if in reach, else the best
           expected-damage target; Artillery fires from maximum standoff (§2.9)
  T-AI-05  strictly-losing-attack guard: the AI never makes an attack in which
           its unit dies and trades down (§2.9)
  T-AI-06  determinism: same state → same move; every scoring tie is broken by a
           stated deterministic rule (canonical hex order for position ties;
           remaining tie dimensions per the Q9 ruling)
Determinism: pure function of state; difficulty changes only starting Fame
         (§2.9), never the routine.
Acceptance: T-AI-01..06, plus a self-play smoke run: N headless AI-vs-AI games
         all terminate at or before the cap with a valid result tier.
```

```
SPEC STUB 7: Scenario file & validator     (Director → Content/Scenario Designer,
                                            Systems Engineer for the loader)
Format:  one versioned JSON file per scenario; strat::loadScenario parses and
         validates it headless. Fields:
           formatVersion   int     unknown → refuse load
           scenarioId      string  stable identifier
           scenarioHash    string  hash of the canonical serialization (fields
                                   in this order, hexes in canonical hex order)
           map             object  width/height (Q1) + per-hex terrain Id
                                   (row-major in canonical hex order; Ids are
                                   §2.3 / Stub 2 row names)
           ownership       array   initial owner of each capturable hex — a home
                                   factory per side, neutral factories/towns
                                   unowned (§2.7)
           placements      array   {side, unitId, hex, isFlag} — starting units;
                                   isFlag is valid only on a Tank (§2.4: the
                                   flag is "a designated Tank")
           startingFame    object  per side; 200/200 baseline (§2.7). The
                                   difficulty handicap (§2.9) is a match-setup
                                   parameter applied on top, not a scenario field
           turnCap         int     the §2.8 cap (value per Q7)
Invariants:
  T-SCN-01  exactly one isFlag placement per side, and it is a Tank; the flag
            appears in no buildlist anywhere — "not producible" (§2.4) is a
            scenario/production fact, not a fifth unit row
  T-SCN-02  structural validity: every hex reference is in bounds (T-HEX-05);
            every terrain and unit Id resolves to a Stub-2 row; no two
            placements share a hex (§2.5)
  T-SCN-03  economy validity: each side owns exactly one home factory at start,
            and at least two neutral factories exist in contested ground (§2.7,
            "~4 factories total")
  T-SCN-04  playability: the two flags are mutually reachable by land movement
            (Stub 3 pathing, Bridge rules respected) — a scenario cannot be born
            stalemated
Determinism: pure parse + validation; any failure refuses the whole file with a
         reason. scenarioHash is platform-stable by canonical ordering.
Acceptance: T-SCN-01..04 headless. The §4.2 validate_scenario MCP tool wraps the
         same checks in-editor for the Content agent; its manual fallback is
         running the headless validator on the exported file (MCP stays off the
         critical path, §3 guardrails).
```

```
SPEC STUB 8: UI binding contract           (Director → UI Scaffolder)
Scope:   NOT layout or visual design (ux-onboarding-designer's lane) — this is
         the contract for how every widget is fed. Widgets bind to a view-model
         snapshot plus the §4.9 event list, and hold no rules state (§4.1).
Snapshot fields (read-only, produced by the rules module):
         per-hex   {terrainId, owner}
         per-unit  {id, side, unitId, hex, hp, hpMax, isFlag, hasActed,
                    captureProgress}
         per-side  {fameTotal, fameCombat, objectivesHeld X of N, survivingHP}
         match     {turn, turnCap, sideToMove, resultTier or null}
Queries: reachable(unit) → the T-MOVE-01 set; forecast(attacker, defenderHex) →
         {damage, counterDamage} computed by the verified resolveDamage /
         defenderCanCounter (5ffa8d6).
Invariants:
  T-UI-01  forecast = resolution: the forecast shown before commit is produced
           by the same strat call that resolves the attack — identical numbers,
           mechanically (§2.6, §2.11)
  T-UI-02  the reachable-hex highlight displays exactly the T-MOVE-01 set — the
           UI queries the module and never recomputes movement (§2.5)
  T-UI-03  the live standings scoreboard (§2.11, §2.8) binds 1:1 to snapshot
           fields — enemy strength destroyed, objectives held X/N, surviving
           units/HP, turn vs cap — with no widget-side arithmetic
  T-UI-04  the production menu binds to the buildlist derived from the four
           Stub-2 unit rows plus current fameTotal; the flag never appears
           (T-SCN-01's non-producible clause, enforced at the UI layer too)
Determinism: widgets are pure functions of snapshot + events; asserted
         end-to-end by T-INT-05 (§4.9).
Acceptance: T-UI-01..02 headless (the queries are headless functions);
         T-UI-03..04 in-editor Automation.
```

### §4.8 Data contract — DataTable schemas

**Principle: authored once, read twice, proven equal.** Each table is one
canonical CSV in the repo (`data/`). The headless loader parses it directly; the
Unreal editor imports the same file into a `UDataTable` whose row struct derives
`FTableRowBase`. A parity gate (T-DATA-05, Unreal Automation) iterates every
imported row and asserts it equals the CSV field-for-field. Nothing is authored
twice, so the headless sim and the engine can never disagree about a stat.
Missing column or unparseable value = hard load failure, never a silent default.

**Unit schema** — `data/units.csv` → headless `strat::UnitDef` → UStruct `FUnitRow`.
Exactly four rows (Infantry, Tank, Artillery, Recon; §2.4). The **flag unit is
not a row**: §2.4 defines it as "a designated Tank," so flag status is a
placement-level field in the scenario file (`isFlag`, §4.7 Stub 7), gated by
T-SCN-01 — not a fifth unit type. One representation, one gate.

| Column | CSV type | Headless field (`strat::UnitDef`) | UStruct field (`FUnitRow`) | Source |
|---|---|---|---|---|
| `Id` (row name) | string | `id` | RowName (`FName`) | §2.4 |
| `HP` | int | `hpMax` | `int32 HP` | §2.4 (10/20/8/12) |
| `Move` | int | `move` | `int32 Move` | §2.4 (3/5/3/7) |
| `Atk` | int | `atk` | `int32 Atk` | §2.4 (4/8/10/5) |
| `Def` | int | `def` | `int32 Def` | §2.4 (2/5/1/3) |
| `RangeMin` | int | `rangeMin` | `int32 RangeMin` | §2.4 (Artillery 2, others 1) |
| `RangeMax` | int | `rangeMax` | `int32 RangeMax` | §2.4 (Artillery 3, others 1) |
| `CostFame` | int | `costFame` | `int32 CostFame` | §2.4 (100/300/200/150) |
| `Type` | enum string | `strat::UnitType type` | `EUnitType Type` | addendum Part A — order fixed: Infantry, Tank, Artillery, Recon |
| `CanCapture` | bool | `canCapture` | `bool bCanCapture` | §2.7 (Infantry only) |
| `MoveClass` | enum string | *reserved* | *reserved* | **blocked on Q2** |

`EUnitType` is a `UENUM` mirroring `strat::UnitType` (`Combat.h`, addendum Part
A) with the enumerator order pinned; T-DATA-05 asserts the mirror is exact so an
editor-side reorder can never silently reindex the effectiveness table below.

**Terrain schema** — `data/terrain.csv` → headless `strat::TerrainDef` → UStruct `FTerrainRow`.
Exactly seven rows (§2.3).

| Column | CSV type | Headless field | UStruct field | Source |
|---|---|---|---|---|
| `Id` (row name) | string | `id` | RowName | §2.3 |
| `MoveCost` | int (0 = impassable) | `moveCost` | `int32 MoveCost` | §2.3 (Plains 1, Woods 2, Mountains 3, Water —, Town 1, Bridge 1, Factory 1) |
| `DefensePct` | int, signed | `defensePct` | `int32 DefensePct` | §2.3 (0, 20, 40, 0, 10, **−10**, 15) |
| `PassLand`/`PassAir`/`PassSea` | bool ×3 | `passLand/Air/Sea` | `bool bPassLand/Air/Sea` | §2.3 Passable column |
| `Capturable` | bool | `capturable` | `bool bCapturable` | §2.3 (Town, Factory) |
| `IncomeFame` | int | `incomeFame` | `int32 IncomeFame` | §2.7 (Factory 100, Town 25, else 0) |
| `IsSpawnPoint` | bool | `isSpawnPoint` | `bool bIsSpawnPoint` | §2.7 (Factory) |
| `IsRepairPoint` | bool | `isRepairPoint` | `bool bIsRepairPoint` | §2.7 Repair (Town + Factory) |

**Type-effectiveness schema** — `data/effectiveness.csv` → `strat::effectiveness`
→ UStruct `FEffectivenessRow`. A 4×4 matrix, row = attacker type, columns =
defender types, values ∈ {0.5, 1.0, 1.5} (§3 spec), **shipping all-1.0**
(§2.4 — the triangle stays positional). The verified implementation
(`Combat.cpp::effectiveness` @ `5ffa8d6`) hardcodes the neutral stub; this
schema is the lever's *data* form, so that if self-play ever asks for a non-1.0
cell, populating it is a CSV edit gated by the existing directional-gate plan
(addendum Part A), not a code change. T-COMBAT-09 (neutral stub, 16/16 pairs)
continues to pin the shipped state; a non-neutral CSV with T-COMBAT-09 still in
the suite is a deliberate, visible gate change the Director must approve — the
"do not invent balance values" rule enforced by the pipeline itself.

```
Invariants (the T-DATA set — Stub 2, §4.7):
  T-DATA-01  loaded unit values equal the §2.4 table exactly (4 rows, all columns)
  T-DATA-02  loaded terrain values equal the §2.3 table exactly (7 rows),
             including Bridge's NEGATIVE defense and Water impassable-to-land
  T-DATA-03  exactly one unit row has CanCapture == true (Infantry, §2.7)
  T-DATA-04  sanity: all costs > 0; RangeMin <= RangeMax; HP > 0
  T-DATA-05  (editor, Unreal Automation) every imported DataTable row equals the
             CSV field-for-field, and EUnitType mirrors strat::UnitType exactly
  T-DATA-06  effectiveness.csv is 4×4, indexed in the pinned type order, every
             cell ∈ {0.5, 1.0, 1.5}; the SHIPPED file is all-1.0 (re-asserting
             T-COMBAT-09 at the data layer)
Determinism: pure parse; missing/malformed field = hard fail, no defaults.
Acceptance: T-DATA-01..04, 06 headless; T-DATA-05 in the editor pass.
```

### §4.9 Headless-module → Unreal integration path

The rules module's value is that it has **zero engine dependencies** (§3, §4.1);
integration must add Unreal *around* it without ever adding Unreal *to* it.

**1. Module layout — one source, two compilers.** The certified headless
sources (`Combat.h`/`Combat.cpp` today; each §4.7 stub as it lands) live
canonically in the crew repo, where the `g++`/`clang++` + `python run.py` gate
runs (§3 ledger). The UE project vendors them verbatim into a UBT runtime
module, `Source/StratRules/`, via a sync script that records the source commit
hash. `StratRules` contains **no engine headers, no UObject, no third-party
includes** — pure C++17 in `namespace strat`, exactly the base-spec constraint.
The standalone gate keeps compiling the identical files, so "the engine build
works" never substitutes for "the gate passed."

**2. Bridge — the only code that knows both worlds.** The game module
(`Stratocracy`) owns:
- **Load:** `FUnitRow`/`FTerrainRow`/`FEffectivenessRow` → `strat::UnitDef` /
  `strat::TerrainDef` / effectiveness table (a mechanical §4.8 mapping), plus
  `strat::loadScenario` on the shipped scenario asset (§4.7 Stub 7).
- **The authoritative `strat::GameState`.** Actors and UMG hold no rules state
  (§4.1 "never own rules" — here made structural, not aspirational).
- **Command in / events out.** Presentation submits commands —
  `Move{unit, destHex}`, `Attack{unit, targetHex}`, `Build{factoryHex, unitId}`,
  `Capture{unit}`, `EndTurn{}` — the rules module validates then applies each,
  and emits an **ordered, deterministic event list**: `Moved(path)`, `Damaged`,
  `Destroyed`, `Captured`, `Spawned`, `BuildWaiting`, `Repaired`, `IncomePaid`,
  `MatchEnded(tier)`. Actors and widgets animate and rebind **from events and
  the view-model snapshot only** (§4.7 Stub 8). An invalid command returns a
  rejection reason and changes nothing.
- **Threading:** synchronous on the game thread. A full turn resolution is
  microseconds of integer math; the shipping AI "moves instantly" (§2.8). No
  async, and no MCP involvement anywhere in the runtime path — the MCP plugin
  remains editor-only tooling, experimental, off the critical path (§3
  guardrails, §4.2, §4.5).

**3. Parity gates.** The command log format of §4.10 is the instrument: the
same recorded match is replayed by the headless harness and by an in-editor
Automation test through the UBT-compiled module, and both must land on the same
canonical state hash. This is what catches the one genuinely engine-shaped
risk — a compiler/CRT divergence in the damage formula's `round` — mechanically
instead of by playtest anecdote.

```
SPEC STUB: Integration parity              (Director → Systems Engineer / UI Scaffolder)
Inputs:  vendored StratRules sources + recorded source commit; a §4.10 replay
         file; the §4.8 tables imported in-editor.
Invariants:
  T-INT-01  source identity: every file in Source/StratRules/ hash-matches the
            recorded crew commit — the ledger's evidence chain survives vendoring
  T-INT-02  replay parity: the same command log replayed headless and in-engine
            (Automation test) produces the same final canonical state hash.
            (The tripwire of this stub: an agent that "ports" rather than vendors
            the module — or a compiler that rounds differently — passes every
            behavior test in one world and silently diverges in the other.)
  T-INT-03  rejection safety: an illegal command leaves the state hash unchanged
            and returns a reason; no partial application
  T-INT-04  no engine deps: StratRules compiles standalone under the existing
            g++/clang++ gate — the gate run itself is the assert
  T-INT-05  (editor, Automation) presentation statelessness: after any event
            sequence, rebuilding all widgets/actors from the current view-model
            snapshot alone reproduces the same displayed values (nothing lives
            only in a widget)
Determinism: the bridge never reorders, drops, or synthesizes events.
Acceptance: T-INT-01, 04 on every gate run; T-INT-02, 03, 05 in the editor pass.
```

### §4.10 Save & replay format

**Design choice: a save *is* a replay.** Because every system is a deterministic
pure function or state machine (§2.6, §4.1, and every §4.7 determinism gate),
the cheapest correct save is not a state snapshot but **the scenario reference
plus the ordered command log**. Loading = `loadScenario` + re-apply the log —
headless-speed, sub-second. One format, four consumers:

1. **Single-slot save/load** (§4.1's "minimal single-slot," now specified).
2. **The T-INT-02 parity gate** — its input file is a save file.
3. **Balance Analyst self-play logs** (§4.1 harness) — each self-play match is
   emitted as this same format, so every balance claim in the ledger's evidence
   chain is a *replayable* artifact, not a summary statistic.
4. **Bug reproduction** — a playtest failure attaches its save; any agent can
   replay it headless.

**File layout** — versioned JSON, one file:

| Field | Type | Meaning |
|---|---|---|
| `formatVersion` | int | This layout's version; unknown = refuse load |
| `rulesCommit` | string | Crew commit of the rules module that wrote the file (T-INT-01's hash) |
| `dataHash` | string | Hash of the §4.8 CSV set in effect |
| `scenarioId` / `scenarioHash` | string | The §4.7 Stub-7 scenario file and its hash |
| `seed` | int | Reserved; **written as 0** — no RNG ships (§2.6, pending Q12) |
| `commandLog` | array | The ordered commands of §4.9, exactly as the bridge consumed them, tagged `{turn, side}` |
| `stateHash` | string | Canonical hash of the resulting state (integrity check) |
| `result` | string/null | Result tier (§2.8) if the match ended, else null |

**Canonical state hash.** Defined once, in the headless module: serialize the
`GameState` in a fixed field order — turn counter, side to move, per-side
`fameTotal`/`fameCombat`, objective ownership, per-unit `{id, side, hex, hp,
isFlag, captureProgress, pendingBuilds}` sorted by the canonical hex order
(§4.7 conventions, T-HEX-07) — then hash the bytes. Every field is an
**integer** (`eff` and the HP ratio exist only transiently inside
`resolveDamage`), so the hash is platform-stable by construction; T-INT-02
proves it across compilers.

**Policies (prototype):**
- **Single slot** — one file (`slot0`), stored via a thin `USaveGame` wrapper
  holding the JSON so platform save paths are respected. Overwrite-confirm UX
  belongs to the ux-onboarding designer (Handoffs).
- **Save points** — a save is accepted between atomic commands during the
  player's turn. The AI turn resolves synchronously in one call (§4.9), so
  "mid-AI-turn" is not a reachable save state by construction.
- **Mid-match saves** — the log up to the last completed command *is* the save.
  Derived pending state (a waiting build, capture-in-progress) replays
  correctly because it is a function of the log.
- **Version policy** — mismatched `formatVersion`, `rulesCommit`, `dataHash`,
  or `scenarioHash` → **refuse load with a reason**. No migration in the
  prototype; a save is only valid against the exact rules and data that wrote it.

```
SPEC STUB: Save & replay                   (Director → Systems Engineer)
Inputs:  scenario file (Stub 7), command log, §4.8 data set, module commit.
Invariants:
  T-SAVE-01  round-trip: play N commands → save → load → identical stateHash
  T-SAVE-02  replay determinism: the same file loaded twice → identical hashes
             (leans on every §4.7 determinism gate — T-HEX-07, T-MOVE-06,
             T-FAME-09, T-TURN-09, T-AI-06; this is their end-to-end composition)
  T-SAVE-03  prefix validity: every prefix of a valid log is itself a valid,
             loadable save (mid-match save falls out of this)
  T-SAVE-04  refusal: any header mismatch (version/rules/data/scenario hash) →
             load refused with a reason; state untouched
  T-SAVE-05  no partial load: a log with an illegal command at index k is
             refused whole; the pre-load state survives. (The tripwire: an agent
             that applies-then-validates leaves a corrupted half-loaded state
             that passes every happy-path test.)
  T-SAVE-06  stateHash stability: hash of a given state is identical across the
             headless and in-engine builds (asserted jointly with T-INT-02)
  T-SAVE-07  harness compatibility: a Balance Analyst self-play log validates
             and replays as a save file — one format, no dialect drift
Determinism: pure; the file contains everything needed to reproduce the state.
Acceptance: T-SAVE-01..07 headless (05 also exercised in-editor via the load UI
            path); slot I/O smoke test in the editor pass.
```

## Build order

Rows 1–8 are the §4.7 stubs (the eight `*pending*` ledger rows); rows 9–10 are
the stage-2 systems. Combat, its test suite, Repair, and Type-effectiveness are
green at `5ffa8d6` and are prerequisites, not work items. Note **row 10's
format spec must exist by the row-9 integration pass**, because T-INT-02's
input file is a §4.10 save.

| # | System (ledger row) | Depends on | Headless? | Acceptance test IDs |
|---|---|---|---|---|
| 1 | Hex grid & math (§4.7 Stub 1) | — (Q1 pins bounds) | Yes | T-HEX-01..07 |
| 2 | Data tables (§4.8, incl. effectiveness CSV) | — (MoveClass column blocked on Q2) | Loader + T-DATA-06 yes; import parity in-editor | T-DATA-01..06 |
| 3 | Movement & pathfinding (Stub 3) | 1, 2 | Yes | T-MOVE-01..06 |
| 4 | Capture & Fame economy (Stub 4) | 3 | Yes | T-FAME-01..09 |
| 5 | Turn loop & win/tiebreak (Stub 5) | 4 + verified Combat/Repair @ 5ffa8d6 | Yes | T-TURN-01..09 |
| 6 | Opponent AI (Stub 6) | 5 | Yes | T-AI-01..06 + self-play smoke |
| 7 | Scenario file & validator (Stub 7) | 1, 2 (3 for T-SCN-04) | Yes; MCP tool wraps it in-editor, manual fallback stands | T-SCN-01..04 |
| 8 | UI binding (Stub 8) | 5, 7 (snapshot needs full state) | Contract + queries yes; widgets in-editor | T-UI-01..04 |
| 9 | Presentation bridge & integration — §4.9 (proposed ledger row) | Rows 1–5 built; vendoring + T-INT-01/04 can start with any subset | Source/compile gates yes; replay parity + statelessness in-editor | T-INT-01..05 |
| 10 | Save & replay — §4.10 (proposed ledger row) | 4, 5 (command set + turn loop); 7 (scenario format); **format spec itself has no deps — write it first** | Yes, all but slot I/O | T-SAVE-01..07 |

**Critical path: 1 → 3 → 4 → 5 → 6/8.** Rows 2 and 7 run in parallel with the
chain (2 immediately; 7 once 1–2 land); 6 and 8 fork after 5. §4.4's milestone
table currently parks save/load in week 5, and this draft shows that is one
week too late in one respect: the *format and headless replayer* are the
instrument for the week-2 vertical-slice integration gate (T-INT-02) and the
week-4 self-play logs (T-SAVE-07). The change request below splits the row —
format + replayer early, save-slot UI stays week 5.

## Change requests

| Existing § | Current text | Proposed change | Why |
|---|---|---|---|
| §2.7 Combat Fame | "destroying an enemy unit pays **~half its Fame cost** … an **undamaged strike** … pays a small bonus" | Pin the kill awards to exactly half of each §2.4 cost — Infantry 50, Recon 75, Artillery 100, Tank 150 (all integers; no rounding rule needed) — pin the undamaged-strike bonus to a number, and state whether the flag's +500 stacks with the Tank kill award | T-FAME-07 cannot assert "~" or "small"; see Q5/Q6 |
| §2.7 Capture | "capture over **N turns (start N=1–2)**" | Pin N to one value | T-FAME-05 needs a number; see Q4 |
| §2.8 Turn cap | "the turn cap (**e.g. 20 turns**)" | Pin the cap (the GDD's own exemplar 20, unless the Director rules otherwise) and store it per-scenario as `turnCap` (§4.7 Stub 7) | T-TURN-04 and the scenario schema need a value, not an example; see Q7 |
| §2.3 caption | "(move cost is **per movement class**)" | Either add the movement-class table (classes × per-terrain costs, including Recon's "ignores some terrain cost", §2.4) or drop the caption | The §2.3 table has a single cost column; the §4.8 `MoveClass` column and T-MOVE-07 are blocked; see Q2 |
| §3 ledger | Eight `*pending*` rows with empty Evidence cells | Annotate each pending row with its reserved test-ID prefix (T-HEX, T-DATA, T-MOVE, T-FAME, T-TURN, T-AI, T-SCN, T-UI per §4.7) | The evidence format is pre-agreed before the build, so each row flips exactly the way Combat's did — commit + named passing IDs |
| §3 ledger | No rows for integration or save/replay | Add two `*pending*` rows: "Presentation bridge & integration (T-INT)" and "Save/replay (T-SAVE)" | Otherwise this work lands unledgered as invisible glue; the ledger's honesty rule (§3) wants it tracked, with pre-agreed evidence prefixes like the CR above gives the other eight |
| §4.1 | "**Save/load:** minimal single-slot for the prototype." | "…minimal single-slot; format and gates per §4.10 (a save is a replay — the same file drives the integration parity gate and the self-play logs)." | The bullet now has a specified, gateable backing |
| §4.1 | "Balance sim harness — headless AI-vs-AI self-play, N games → win-rate and turn-length distributions" | Append: "each self-play match is emitted as a §4.10 replay file (T-SAVE-07), so balance findings are replayable evidence" | Ties the ledger's "checkable" claim (§3) to balance data, not just tests |
| §4.4, wk 5 | "UI polish, feedback/juice, save/load, onboarding." | Move the **save format + headless replayer** to wk 2–3 (integration parity instrument); only the save-slot UI remains wk 5 | T-INT-02 (wk-2 vertical slice) consumes the format; wk-5 discovery of a format problem would invalidate prior parity runs |

## Open questions for the Director

Every gap found while writing the §4.7 gates (Q1–Q10) and this stage's additions
(Q11–Q13). Each blocks the gate named beside it; the Director writes the rule,
the gate then pins it.

1. **Map dimensions (Q1).** §2.2 and §2.10 never state the prototype map's
   size or shape. Blocks T-HEX-05 bounds and the Stub-7 `map` field. (The
   scenario-designer's layout work needs the same ruling — Handoffs.)
2. **Movement classes (Q2).** §2.3's caption says "move cost is per movement
   class" and §2.4 gives Recon "ignores some terrain cost," but no class set or
   per-class cost table exists. Blocks the §4.8 `MoveClass` column and the
   reserved T-MOVE-07.
3. **Pass-through (Q3).** §2.5 pins one-unit-per-hex for *ending* a move; it is
   silent on pathing *through* a friendly-occupied hex. T-MOVE-03 asserts the
   conservative reading (blocked) until ruled.
4. **Capture N and interruption (Q4).** Pin N (§2.7 says "start N=1–2"), and
   rule the edge cases: does progress reset if the Infantry leaves or dies
   mid-capture? Blocks T-FAME-05's exactness.
5. **Kill-award exact values (Q5).** "~half its Fame cost" → the CR above
   proposes exactly-half (50/75/100/150). Also: does the flag kill's +500 stack
   with the Tank's ordinary kill award? Blocks T-FAME-07.
6. **Undamaged-strike bonus (Q6).** "a small bonus" (§2.7) has no number.
   Blocks T-FAME-07.
7. **Turn cap value (Q7).** "e.g. 20 turns" (§2.8) is an example, not a rule.
   Blocks T-TURN-04 and Stub 7's `turnCap`.
8. **Income timing and build limits (Q8).** When within the turn does
   factory/town income pay, and can it fund a build the same turn? Is there a
   builds-per-factory-per-turn limit (§2.9's AI implies one; the player's rule
   is unstated)? For a waiting build (§2.7 "the build waits"): is Fame committed
   at queue time or spawn time, and can it be canceled? Blocks T-FAME-02/04.
9. **AI tie-breaks (Q9).** §2.9's "best expected-damage target" and pathing
   choices can tie. T-AI-06 breaks position ties by canonical hex order; the
   Director should confirm that rule and name the tie order for any remaining
   dimensions (target choice, build choice) so AI determinism is a rule, not an
   implementation accident.
10. **Flag designation (Q10).** Confirm: exactly one flag per side, designated
    by the scenario (`isFlag` placement, Stub 7), with otherwise-standard Tank
    stats — §2.4's "Tank variant" read as *not producible and nothing else*.
    Blocks T-SCN-01's exactness and the flag's data representation (§4.8).
11. **Undo (§2.5–§2.6 are silent).** The command log makes single-step undo of
    an uncommitted move nearly free, but the GDD never grants it, and the §2.6
    forecast-then-commit flow arguably *forbids* it. Rule needed before any
    T-SAVE/T-UI gate can reference undo — currently no gate assumes it exists.
12. **Zero-RNG confirmation.** §2.6/§4.1 say any RNG "is seeded"; nothing in §2
    actually uses RNG. Confirm the prototype ships with **none**, so §4.10's
    `seed` field is pinned to a written-as-0 reserved field (as drafted). If any
    seeded RNG is ever added, the seed becomes load-bearing and T-SAVE-01/02
    extend to it.
13. **Player-facing replay: in scope or not?** §4.10's format makes a "watch
    replay" feature cheap, but the §2.10 scope table doesn't list one and I have
    not added it. Confirm the format stays internal (saves, gates, balance
    logs) for the prototype — or explicitly scope the feature, which would then
    be a UX handoff, not a rules change.

## Handoffs

- **ux-onboarding-designer** — owns the save/load surface: slot UI,
  overwrite-confirm, where "Save" lives, and any player-visible load-refusal
  message (T-SAVE-04 supplies the reason string; they decide how it reads).
  The §4.9 event list and the §4.7 Stub-8 view-model snapshot are the complete
  feed for their §2.11 expansion — their HUD spec should name which event or
  snapshot field drives each element, keeping the T-UI binding gates 1:1.
- **scenario-designer** — §4.10's header stores their scenario's `scenarioId` +
  `scenarioHash`; their new layout section should treat every layout number as
  a Stub-7 scenario-file value (validated by T-SCN-02..04), never a constant in
  the rules module — that is what keeps a second scenario a data drop. The Q1
  map-dimensions ruling lands in their layout spec and in Stub 7's `map` field
  simultaneously.
- **rules-designer** — if their §2 consolidation changes the command set (e.g.
  capture mechanics per Q4), the §4.9 command list and §4.10 log entries change
  with it; flag any §2 verb added or cut so the formats track. Q4–Q8 rulings
  land in their consolidated §2 text and in the T-FAME/T-TURN gates together.
- **Director** — Q1–Q13 above and the nine change requests.

## Grounding

- Project state (4 verified rows at `5ffa8d6`, 17/17 invariants; 8 rows
  pending; `Source/` = stock template): `source/gdd.md` §3 ledger + its status
  and certification paragraphs.
- Spec-stub shape and constraints (namespace `strat`, pure C++17, no engine
  deps, test-first, "do not invent balance values"):
  `../stratocracy-crew/spec/combat_spec.md` (Required functions, Determinism,
  invariants 1–8); `combat_spec_addendum.md` (Parts A/B, T-COMBAT-09..10,
  T-REPAIR-01..07).
- §4.7 stub content, per stub: Stub 1 — §2.2 (pointy-top, six equal
  neighbours, no cheap direction). Stub 3 — §2.5 (exact reachable set, one
  unit per hex, ZOC cut), §2.3 (costs, Bridge/Water rule), §4.1 (Dijkstra over
  terrain cost). Stub 4 — §2.7 (single pool, income values, build/spawn/wait,
  kill awards, capture-by-Infantry, no Fame cap, starting Fame 200). Stub 5 —
  §2.1 (I-GO-U-GO), §2.8 (win/loss, tiebreak order, mutual-passivity guard,
  categorical tiers), §2.7 + addendum Part B (repair rule, verified @
  `5ffa8d6`). Stub 6 — §2.9 (two-phase baseline, capture behavior, standoff,
  strictly-losing-attack guard, difficulty = Fame handicap). Stub 7 — §2.4
  (flag = designated Tank, not producible), §2.7 (home factory per side, two+
  neutrals, ~4 total, starting Fame), §4.2 (`validate_scenario` MCP tool), §3
  guardrails (MCP off critical path, manual fallback). Stub 8 — §2.11 (forecast,
  reachable highlight, scoreboard fields, production menu), §2.6 (forecast =
  resolution), §4.1 (presentation never owns rules).
- Canonical hex order and the axial distance formula: technical conventions
  defined by this draft (§4.7 conventions block), not game rules — flagged
  as Director-owned contract, consumed by T-HEX-07, T-MOVE-04, T-AI-06, Stub 7
  hashing, and the §4.10 state hash.
- Unit/terrain constants in the §4.8 schemas: GDD §2.3, §2.4 tables. Income,
  capture-by-Infantry, spawn/repair points, starting Fame: §2.7. Flag as "a
  designated Tank… Not producible": §2.4.
- `UnitType` order and the appended-last `type` field: addendum Part A header
  contract. Effectiveness value set {0.5, 1.0, 1.5} and ships-all-1.0: GDD §3
  spec block + §2.4; verified neutral stub: ledger row @ `5ffa8d6`,
  T-COMBAT-09..10.
- Headless-first architecture, presentation-never-owns-rules, Enhanced Input,
  single-slot save, balance harness: GDD §4.1.
- AI "moves instantly" (grounds synchronous bridge + no mid-AI-turn save): GDD
  §2.8 "On the turn cap vs. real time."
- MCP experimental / serial / off critical path / manual fallback: GDD §3
  guardrails, §4.2, §4.5.
- Determinism promises composed by T-SAVE-02: GDD §2.6 (forecast = resolution,
  seeded-if-any RNG), §4.1, and the §4.7 determinism gates T-HEX-07, T-MOVE-06,
  T-FAME-09, T-TURN-09, T-AI-06 — all defined in this draft.
- Milestone table and the wk-2 vertical slice / wk-5 save-load placement the
  change request amends: GDD §4.4.
- Result tiers stored in the save trailer: GDD §2.8 victory-quality tiers.
- **No stage-1 artifact is cited anywhere in this draft.** Every gate ID, stub
  field, and question number referenced by §4.8–§4.10 is defined in §4.7 or
  Open questions of this file, in `source/gdd.md`, or in the two crew spec
  files above.
