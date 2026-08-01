# ✅ APPLIED ADDENDUM — DO NOT RE-APPLY

All 33 pairs below were applied, each having matched exactly once. Re-applying
would fail on every `OLD` and, if forced, would double-write the rulings.

**Four claims in the NEW text were wrong and were corrected in the master after
application.** They are recorded here rather than edited into the pairs above,
so the pairs still say what was actually applied:

1. **Q9 verdict and T-AI-06** asserted that `Infantry > Recon > Artillery >
   Tank` "is §2.4's own listing order". It is not — §2.4's table prints
   **Infantry, Tank, Artillery, Recon**. The order is ascending **cost**
   (100 / 150 / 200 / 300). Corrected in both sites to name the cost column and
   to say explicitly that it is *not* the table's row order.
2. **Q9 verdict** claimed the order "agrees with §2.9's stated buildlist bias".
   It agrees on the first term (Infantry) and contradicts the second — §2.9
   favours an occasional Tank, this priority ranks Tank last. Corrected to name
   both, and to state why they do not conflict: the bias governs free choice,
   the priority governs only already-equal scores.
3. **Q6 verdict** said the cut "reaches five sites that never cite Q6" and then
   listed §2.7's bullet among them — but that bullet *did* cite Q6. Corrected
   to six sites that never cited it (four in the GDD, two in `kb/rules.md`),
   stated separately from §2.7's own bullet.
4. **Q8 verdict** called the two §2.7 sentences "the whole textual cost of the
   ruling". It is not — §2.9's economy phase, T-FAME-02/04 and two `kb/rules.md`
   lines also changed. Corrected to scope the claim to §2.7.

Every one of the four was a factual claim *about* the rule being stated, in
text the fix had just written, and none was in the text being replaced.

---

# Director rulings — Q4, Q5, Q6, Q8, Q9

Ruling cycle of 2026-07-31. These five were the only register rows that stated
**no reading** and therefore blocked their gates outright. All five are ruled
below. Q2, Q11 and Q30 remain unruled and are **not** touched here — each
carries a stated reading, and Q30 is deliberately left open.

**Rulings as given by the Director:**

| Row | Ruling |
|---|---|
| **Q4** | Capture progress is tile-held and **resets to zero when the capturing Infantry leaves the hex or dies**. Never transfers. |
| **Q5** | Kill awards are **exactly half** the §2.4 cost — 50 / 75 / 100 / 150. The flag's **+500 does not stack**: it replaces the ordinary award, so a flag Tank pays 500, not 650. |
| **Q6** | The undamaged-strike bonus is **cut**, not priced (author's option (c)). |
| **Q8a** | Income accrues **at the start of your turn, spendable that same turn** — with **no accrual on turn 1**. |
| **Q8b** | **One build per factory per turn**, both sides; a **waiting build holds that factory's slot** until it spawns. |
| **Q8c** | Fame is **committed at queue time, not refundable**. |
| **Q9** | Target ties break by **canonical hex order**; build ties by the fixed priority **Infantry > Recon > Artillery > Tank**. |

Applied by parsing the pairs below and asserting each `OLD` matches exactly
once. Never retyped by hand.

---

### P1 — §2.7 factories bullet (Q8a: no turn-1 income)
TARGET: gdd

**OLD**
```text
  a **home factory per side** (owned at start, so both players have income
  from turn 1) plus **two or more neutral factories** in contested ground; a
  typical small skirmish map has **~4 factories total**.
```

**NEW**
```text
  a **home factory per side** (owned at start, so both players draw income
  from **turn 2**, the first accrual — Q8, §4.7) plus **two or more neutral
  factories** in contested ground; a typical small skirmish map has **~4
  factories total**.
```

---

### P2 — §2.7 income bullet (Q8a: accrual timing)
TARGET: gdd

**OLD**
```text
- **Income:** each **factory** held pays **+100 Fame/turn**; each captured
  **town** pays **+25/turn**. More objectives held = a faster army, so the
  neutral factories are the mid-game prize.
```

**NEW**
```text
- **Income:** each **factory** held pays **+100 Fame/turn**; each captured
  **town** pays **+25/turn**. Income accrues **at the start of your turn and is
  spendable in that same turn's economy phase** (§2.9) — with **no accrual on
  turn 1**, so turn-1 buying power is the 200 starting Fame alone and the first
  income lands on turn 2 (Q8, §4.7). More objectives held = a faster army, so
  the neutral factories are the mid-game prize.
```

---

### P3 — §2.7 build & spawn bullet (Q8b, Q8c)
TARGET: gdd

**OLD**
```text
  The unit **spawns on the factory hex if it's free, otherwise an adjacent
  free hex; if the factory is boxed in, the build waits.** Fame has no hard
  cap — deployment is throttled by board space, not a point ceiling.
```

**NEW**
```text
  **One build per factory per turn**, for the player and the AI alike (§2.9).
  The unit **spawns on the factory hex if it's free, otherwise an adjacent
  free hex; if the factory is boxed in, the build waits.** A waiting build
  **holds that factory's slot until it spawns**, and its Fame is **committed
  when the build is queued, not when the unit appears, and is not
  refundable** — a boxed-in factory is a commitment to read before spending
  (Q8, §4.7). Fame has no hard cap — deployment is throttled by board space,
  not a point ceiling.
```

---

### P4 — §2.7 Combat Fame bullet (Q5 values + no stacking, Q6 cut)
TARGET: gdd

**OLD**
```text
- **Combat Fame:** destroying an enemy unit pays **~half its Fame cost**
  (e.g. a Tank kill = +150 — see Q5, §4.7, to make this exact); an
  **undamaged strike** (attacker takes no counter) pays a small bonus (see
  Q6, §4.7); destroying the enemy **flag pays +500 and ends the
  match**. These feed the same Fame pool and the cap tiebreak (§2.8).
```

**NEW**
```text
- **Combat Fame:** destroying an enemy unit pays **exactly half its §2.4
  cost — Infantry +50, Recon +75, Artillery +100, Tank +150** (Q5, §4.7;
  every value an integer). Destroying the enemy **flag pays a flat +500 and
  ends the match** — the flag award **replaces** the victim's ordinary kill
  award rather than stacking with it, so a flag Tank pays 500, not 650 (Q5).
  There is **no undamaged-strike bonus**: it was cut rather than priced,
  because kills already pay half-cost and the positional triangle already
  rewards a clean standoff strike with tempo (Q6, §4.7). These feed the same
  Fame pool and the cap tiebreak (§2.8).
```

---

### P5 — §2.7 capture bullet (Q4 interruption)
TARGET: gdd

**OLD**
```text
- **Capture:** move an Infantry (the only capturer) onto a town/factory and
  hold to capture over N turns (start N=1–2); a captured objective flips its
  Fame income to the new owner.
```

**NEW**
```text
- **Capture:** move an Infantry (the only capturer) onto a town/factory and
  hold to capture over N turns (**N = 1** on the shipped scenario; N is
  per-scenario data). Capture progress is **held by the tile and resets to
  zero the moment the capturing Infantry leaves the hex or dies** — it never
  transfers to another unit and never survives an interruption (Q4, §4.7). A
  captured objective flips its Fame income to the new owner.
```

---

### P6 — §2.7 starting Fame bullet (Q8a)
TARGET: gdd

**OLD**
```text
- **Starting Fame:** each side opens with **200 Fame** (enough for two
  Infantry or one Artillery on turn 1) plus home-factory income from turn 1.
```

**NEW**
```text
- **Starting Fame:** each side opens with **200 Fame** — enough for two
  Infantry or one Artillery on turn 1, and the whole of turn-1 buying power,
  since income first accrues on turn 2 (Q8, §4.7). Home-factory income adds
  +100/turn from turn 2 onward.
```

---

### P7 — §2.8 tally definition (Q6 cut)
TARGET: gdd

**OLD**
```text
*Tally definition.* A side's **combat Fame** is the Fame it earned from unit
kills and undamaged-strike bonuses (§2.7). It **excludes** passive factory and
```

**NEW**
```text
*Tally definition.* A side's **combat Fame** is the Fame it earned from unit
kills (§2.7) — the undamaged-strike bonus this key once also counted was cut
unpriced (Q6, §4.7), so kills are its only source. It **excludes** passive
factory and
```

---

### P8 — §2.11 standings "Destroyed" row (Q6 cut)
TARGET: gdd

**OLD**
```text
- **Destroyed** = combat Fame earned (kills + undamaged-strike and flag bonuses, §2.7) — **passive income is excluded**, exactly as the tiebreak excludes it. Hover tooltip: `Fame from kills and strike bonuses. Factory income does not count at the cap.`
```

**NEW**
```text
- **Destroyed** = combat Fame earned (kills and the flag bonus, §2.7; there is no undamaged-strike bonus — Q6, §4.7) — **passive income is excluded**, exactly as the tiebreak excludes it. Hover tooltip: `Fame from kills. Factory income does not count at the cap.`
```

---

### P9 — §2.11.6 event one-shot removed (Q6 cut)
TARGET: gdd

**OLD**
```text
; first undamaged strike → `+[N] Fame — undamaged strike.`; first repair blocked by adjacency →
```

**NEW**
```text
; first repair blocked by adjacency →
```

---

### P10 — §2.11.6 concept ledger, RPS receipt (Q6 cut removes the old receipt)
TARGET: gdd

**OLD**
```text
| One uncountered Artillery strike lands — the undamaged-strike toast is the receipt |
```

**NEW**
```text
| One uncountered Artillery strike lands — the range-2–3 one-shot (`No counter at this range.`) is the receipt, the undamaged-strike toast having been cut with the bonus (Q6, §4.7) |
```

---

### P11 — §2.9 economy phase (Q8a, Q8b, Q9 build ties)
TARGET: gdd

**OLD**
```text
  - **Economy phase.** At each factory it holds: if it can afford a unit,
    build one from a default buildlist (mostly Infantry, an occasional Tank),
    spawning per §2.7. It spends Fame and replaces losses instead of hoarding.
```

**NEW**
```text
  - **Economy phase.** Runs first, on the income that has just accrued for
    this turn (§2.7 — none on turn 1). At each factory it holds: if it can
    afford a unit, build one — the single build that factory gets this turn
    (§2.7) — from a default buildlist (mostly Infantry, an occasional Tank),
    spawning per §2.7. Ties between affordable units break by the fixed
    priority **Infantry > Recon > Artillery > Tank** (Q9, §4.7). It spends
    Fame and replaces losses instead of hoarding.
```

---

### P12 — §2.9 unit phase, target ties (Q9)
TARGET: gdd

**OLD**
```text
    moving, attack — prefer the enemy flag, else the best expected-damage
    target; (3) ranged units (Artillery) fire from maximum standoff so they
```

**NEW**
```text
    moving, attack — prefer the enemy flag, else the best expected-damage
    target, ties broken by the target's canonical hex order (Q9, §4.7); (3)
    ranged units (Artillery) fire from maximum standoff so they
```

---

### P13 — T-FAME-02 (Q8a)
TARGET: gdd

**OLD**
```text
  T-FAME-02  income: each held factory pays +100/turn, each held town +25/turn
             (§2.7); accrual timing per the Q8 ruling
```

**NEW**
```text
  T-FAME-02  income: each held factory pays +100/turn, each held town +25/turn
             (§2.7); accrues at the START of the owner's turn and is spendable
             in that same turn's economy phase, with NO accrual on turn 1 —
             turn-1 buying power is the 200 starting Fame alone (Q8, ruled)
```

---

### P14 — T-FAME-04 (Q8b, Q8c)
TARGET: gdd

**OLD**
```text
  T-FAME-04  spawn: on the factory hex if free, else an adjacent free hex, else
             the build waits (§2.7); waiting-build semantics per Q8
```

**NEW**
```text
  T-FAME-04  spawn: on the factory hex if free, else an adjacent free hex, else
             the build waits (§2.7). One build per factory per turn; a waiting
             build HOLDS that factory's slot until it spawns; Fame is committed
             at queue time, never at spawn time, and is not refundable (Q8,
             ruled)
```

---

### P15 — T-FAME-05 (Q4)
TARGET: gdd

**OLD**
```text
  T-FAME-05  capture: Infantry only (§2.7, §2.4); completes after N turns of
             holding (N per Q4); interruption/reset semantics per Q4
```

**NEW**
```text
  T-FAME-05  capture: Infantry only (§2.7, §2.4); completes after N turns of
             holding (N = 1 on the shipped scenario, per-scenario data);
             progress is tile-held and RESETS TO ZERO when the capturing
             Infantry leaves the hex or dies, and never transfers to another
             unit (Q4, ruled)
```

---

### P16 — T-FAME-07 (Q5, Q6)
TARGET: gdd

**OLD**
```text
  T-FAME-07  kill awards: ~half the victim's Fame cost, small undamaged-strike
             bonus, flag kill +500 and the match ends (§2.7) — exact values per
             Q5/Q6; the gate pins whatever the Director rules
```

**NEW**
```text
  T-FAME-07  kill awards: exactly half the victim's §2.4 cost — Infantry 50,
             Recon 75, Artillery 100, Tank 150 (Q5, ruled). A flag kill pays a
             flat 500 and ends the match; the flag award REPLACES the ordinary
             kill award rather than stacking, so a flag Tank pays 500, not 650
             (Q5). No undamaged-strike bonus exists — cut, not priced (Q6,
             ruled) — so the gate asserts its ABSENCE from every award
```

---

### P17 — T-AI-06 (Q9)
TARGET: gdd

**OLD**
```text
  T-AI-06  determinism: same state → same move; every scoring tie is broken by a
           stated deterministic rule (canonical hex order for position ties;
           remaining tie dimensions per the Q9 ruling)
```

**NEW**
```text
  T-AI-06  determinism: same state → same move; every scoring tie is broken by a
           stated deterministic rule (Q9, ruled): position AND target ties break
           by canonical hex order — for a target, the hex it occupies — and
           build ties break by the fixed type priority Infantry > Recon >
           Artillery > Tank, which is §2.4's own listing order
```

---

### P18 — §4.7 register preamble
TARGET: gdd

**OLD**
```text
**Rows marked *unruled* state no reading and block their gate outright** (Q4's
interruption semantics, Q5's stacking, Q6, Q8, and Q9's target- and
build-choice ties); those gates and milestones cannot be settled until the
Director answers.
```

**NEW**
```text
**No row now states *no reading*.** The five that did — Q4's interruption
semantics, Q5's stacking, Q6, Q8's three sub-questions, and Q9's target- and
build-choice ties — were all ruled this revision, and the gates they blocked
outright (T-FAME-02, T-FAME-04, T-FAME-05, T-FAME-07, T-AI-06 and the T-CAP-
tally suite) now assert. Three rows remain open but **readable** — Q2, Q11 and
Q30 — each carrying a stated reading rather than a blank: Q2 leaves T-MOVE-07
reserved-but-unwritten, Q11's reading is "no undo", and Q30's is partial and
deliberately not hardened. The convention is unchanged: **where a row states no
reading, its gate stays blocked until the Director answers.**
```

---

### P19 — Q4 register row title
TARGET: gdd

**OLD**
```text
| **Q4** | Capture N and interruption. Pin N
```

**NEW**
```text
| **Q4** | ~~Capture N and interruption.~~ **RULED (this revision).** Pin N
```

---

### P20 — Q4 register row verdict
TARGET: gdd

**OLD**
```text
N = 1 on the shipped scenario (§2.13.3's recommendation, inside §2.7's stated range). Interruption semantics are **unruled**, so T-FAME-05 stays blocked. |
```

**NEW**
```text
Ruled. N = 1 on the shipped scenario (§2.13.3's recommendation, inside §2.7's stated range), and N is per-scenario data. **Interruption: capture progress is held by the tile and resets to zero the moment the capturing Infantry leaves the hex or dies** — it never transfers to another unit. This is the conservative reading, and it is what keeps the window between arrival and flip a real risk: at N = 1 the Infantry stands on the tile at the end of one turn and the tile flips at the start of the next, so the opponent gets exactly one turn to answer, and killing or displacing the capturer now costs the attacker the whole count rather than a fraction of it. T-FAME-05 unblocked and asserting. |
```

---

### P21 — Q5 register row title
TARGET: gdd

**OLD**
```text
| **Q5** | Kill-award exact values.
```

**NEW**
```text
| **Q5** | ~~Kill-award exact values.~~ **RULED (this revision).**
```

---

### P22 — Q5 register row verdict
TARGET: gdd

**OLD**
```text
The §2.7 change request proposes exactly half of each §2.4 cost — 50 / 75 / 100 / 150, all integers. Stacking is **unruled**. |
```

**NEW**
```text
Ruled, and the change request is accepted as proposed: exactly half of each §2.4 cost — **Infantry 50, Recon 75, Artillery 100, Tank 150**, all integers, so no rounding rule is needed anywhere. **The flag's +500 does not stack**: it replaces the victim's ordinary kill award rather than adding to it, so a flag Tank pays **500, not 650**. The choice is nearly free at the cap — §2.8 already states the flag bonus can never appear in a capped tally, since a flag kill ends the match immediately — so it binds the live scoreboard (§2.11) and the balance logs rather than any victory condition. T-FAME-07 unblocked. |
```

---

### P23 — Q6 register row title
TARGET: gdd

**OLD**
```text
| **Q6** | Undamaged-strike bonus.
```

**NEW**
```text
| **Q6** | ~~Undamaged-strike bonus.~~ **RULED (this revision) — cut.**
```

---

### P24 — Q6 register row verdict
TARGET: gdd

**OLD**
```text
**Unruled** — unpriced, so no gate asserts it. The rules author recommends (c), with (b) as the fallback; either unblocks the T-CAP- suite immediately. |
```

**NEW**
```text
Ruled **(c) — cut**, as the rules author recommended. Kills already pay half-cost and the positional triangle already rewards a clean standoff strike with tempo, so the bonus was paying twice for one thing; cutting it removes an unpriced term from the §2.8 tiebreak's **primary** sort key rather than leaving a number nobody had chosen inside it. Cheaper than (b), which would have required the document to carry two different Fame totals — one for the pool, one for the cap tally — in both the kb economy block and the T-CAP- suite. The cut reaches five sites that never cite Q6: §2.7's bullet, §2.8's tally definition, §2.11's standings row and tooltip, the §2.11.6 one-shot toast, and the concept ledger's RPS row, whose *receipt* was that toast and is now the range-2–3 one-shot instead. T-FAME-07 and the T-CAP- tally suite unblocked. |
```

---

### P25 — Q8 register row title
TARGET: gdd

**OLD**
```text
| **Q8** | Income timing and build limits.
```

**NEW**
```text
| **Q8** | ~~Income timing and build limits.~~ **RULED (this revision) — all three.**
```

---

### P26 — Q8 register row verdict
TARGET: gdd

**OLD**
```text
**Unruled** — all three sub-questions. T-FAME-02 and T-FAME-04 stay blocked until ruled, and they gate Stub 4, which §4.11 builds *before* the turn loop. |
```

**NEW**
```text
Ruled, all three. **(a) Timing:** income accrues at the **start** of the owner's turn and is spendable in that same turn's economy phase — the phase §2.9 already runs first — but there is **no accrual on turn 1**, so turn-1 buying power is the 200 starting Fame alone. That reading was chosen because it is the one §2.13.2 was already priced on: it prices East's turn-1 Infantry as "100 of the 200 starting Fame", not of 300, so no map number moves. It does correct two sentences that said the opposite — §2.7's "both players have income from turn 1" and its "plus home-factory income from turn 1" — which is the whole textual cost of the ruling. **(b) Limit:** one build per factory per turn, player and AI alike, matching what §2.9 already describes for the AI; a waiting build **holds that factory's slot** until it spawns. **(c) Commitment:** Fame is committed at **queue** time and is **not refundable**, so fameTotal moves once and never reverses, no cancel affordance is owed by §2.11, and a boxed-in factory becomes a commitment the player must read before spending. T-FAME-02 and T-FAME-04 unblocked; Stub 4 is no longer gated on an unruled row. |
```

---

### P27 — Q9 register row title
TARGET: gdd

**OLD**
```text
| **Q9** | AI tie-breaks.
```

**NEW**
```text
| **Q9** | ~~AI tie-breaks.~~ **RULED (this revision).**
```

---

### P28 — Q9 register row verdict
TARGET: gdd

**OLD**
```text
Position ties break by canonical hex order (as gated). Target-choice and build-choice tie order are **unruled** and need naming so determinism is a rule, not an accident. |
```

**NEW**
```text
Ruled, and split by axis rather than forced onto one rule. **Position and target ties break by canonical hex order** — for a target, the hex it occupies — so the convention already gated for positions extends to targets with no new state and nothing new to remember. **Build ties break by the fixed type priority Infantry > Recon > Artillery > Tank**, which is §2.4's own listing order, because a production choice has no board position to sort on and geometry would have been an arbitrary key there. The build order also agrees with §2.9's stated buildlist bias toward Infantry, so the tiebreak reinforces the behaviour that section already describes instead of cutting across it. Determinism is now a stated rule on every axis rather than an implementation accident. T-AI-06 unblocked. |
```

---

### P29 — kb/rules.md starting Fame (Q8a)
TARGET: kb

**OLD**
```text
- **Starting Fame: 200** per side, plus home-factory income from turn 1.
```

**NEW**
```text
- **Starting Fame: 200** per side. Income accrues at the start of your turn and
  is spendable that same turn, but **not on turn 1** — home-factory income adds
  +100/turn from turn 2 onward, so turn-1 buying power is the 200 alone.
```

---

### P30 — kb/rules.md build limit (Q8b, Q8c)
TARGET: kb

**OLD**
```text
  hex; if the factory is boxed in, the build waits.
```

**NEW**
```text
  hex; if the factory is boxed in, the build waits. **One build per factory per
  turn.** A waiting build holds that factory's slot until it spawns, and its
  Fame is committed when the build is queued, not when the unit appears, and is
  not refundable.
```

---

### P31 — kb/rules.md combat award (Q5, Q6)
TARGET: kb

**OLD**
```text
- Destroying an enemy unit pays **~half its cost** (a Tank kill = +150) **[unpinned:
  exact per-unit award]**; an **undamaged strike** (attacker takes no counter) pays a
  small bonus **[unpinned]**; destroying the enemy **flag pays +500 and ends the match**.
```

**NEW**
```text
- Destroying an enemy unit pays **exactly half its cost — Infantry 50 / Recon 75 /
  Artillery 100 / Tank 150**; there is **no undamaged-strike bonus** (cut, not priced);
  destroying the enemy **flag pays a flat +500 and ends the match** — the flag award
  replaces the ordinary kill award rather than stacking, so a flag Tank pays 500, not 650.
```

---

### P32 — kb/rules.md capture N and interruption (Q4)
TARGET: kb

**OLD**
```text
- **Capture:** move an Infantry onto a town/factory and hold to capture over **N turns
  (start N=1-2)**; a captured objective flips its income. **[unpinned: exact N — the
  shipped scenario assumes N=1, but this is an assumption in force, not a rule; also
  unpinned is what happens to progress if the Infantry leaves or dies mid-capture]**
```

**NEW**
```text
- **Capture:** move an Infantry onto a town/factory and hold to capture over **N turns
  (N = 1 on the shipped scenario; N is per-scenario data)**; a captured objective flips
  its income. Capture progress is held by the tile and **resets to zero when the
  capturing Infantry leaves the hex or dies**; it never transfers to another unit.
```

---

### P33 — kb/rules.md combat Fame definition (Q6)
TARGET: kb

**OLD**
```text
**Combat Fame** counts only kills and undamaged-strike bonuses. It **excludes passive
```

**NEW**
```text
**Combat Fame** counts only kills — the undamaged-strike bonus was cut unpriced
(Q6). It **excludes passive
```
