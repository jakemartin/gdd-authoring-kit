> # ✅ APPLIED ADDENDUM — DO NOT RE-APPLY
>
> Every replacement pair in this file **has been applied to the master GDD**, and
> the master has moved on since. Its Old blocks no longer match, so re-applying is
> a no-op at best; its quoted "current" text, register extents, and any hash it
> names are a **snapshot of the moment it was written**, not the current state.
>
> **The master GDD is the source of truth** — read `source/gdd.md`. Further changes
> to a merged section go in a *new* addendum file.

# Technical design — post-merge-5 draft (tech-director)

## Placement

Five exact edits, all inside **§4.6 Token budget** (`source/gdd.md` L1303,
L1306, L1307, L1315–1317, L1329). No other section, stub, test ID, or open
question is touched. Q26 and Stub 7 are unchanged, as instructed.

## Draft

### The diagnosis, stated plainly

The printed **$267** was never derived from the per-task lines. It is
**1.5 × $178** — the rounded dev-time subtotal scaled by the overrun factor —
presented in a sentence that claims to derive it from `315 × $0.69 + 47 × $delta`.
That derivation cannot reach $267 for any delta the table supports:

| Delta used | `315 × $0.69 + 47 × delta` | Result |
|---|---|---|
| $1.03 (as printed on the ceiling line) | $217.35 + $48.41 | **$265.76** |
| $1.04 (as the table above it computes: $1.73 − $0.69) | $217.35 + $48.88 | **$266.23** |
| $1.035 (the exact, unrounded delta) | $217.35 + $48.645 | **$265.995** |

So the gate is right on both counts: the two deltas disagree, *and* the printed
total came from a third route (scaling a rounded subtotal) that appears nowhere
on the line. The $1.24 gap it measured is $267 − $265.76.

**The actual error is the rounded delta, not the rate, the task count, or the
escalation fraction.** Opus per task is exactly **$1.725** ($0.50 + $0.10 +
$1.125); the table displays $1.73 and $1.13, and the escalation line then
subtracts *displayed* figures instead of exact ones. Rounding before
subtracting is what let two deltas exist. The fix is to compute the delta once,
unrounded — **$1.035/task** — and use it everywhere, including in the base-case
escalation line, which currently uses $1.04 implicitly.

No API rate changes. The 210-task count, the 15% escalation fraction, and the
1.5× overrun factor are all unchanged — none of them was the error.

---

**Edit 1 of 5 — L1303.** State the Opus per-task cost unrounded, so the delta
below has an exact figure to subtract from. `$1.125` is the exact product of
45k × $25/M; `$1.13` was its two-decimal display.

**OLD**
```
| Cost per task — Opus 4.8 | 100k × $5/M + 200k × $0.50/M + 45k × $25/M = $0.50 + $0.10 + $1.13 = **$1.73** |
```
**NEW**
```
| Cost per task — Opus 4.8 | 100k × $5/M + 200k × $0.50/M + 45k × $25/M = $0.50 + $0.10 + $1.125 = **$1.725** (quoted to the cent as $1.73; **$1.725 is the exact figure**, and every escalation delta in this section is computed from it, not from the rounded display) |
```

---

**Edit 2 of 5 — L1306.** One delta, stated to the precision actually used, with
the task rounding shown. 15% of 210 = 31.5, which is where the ≈ 32 comes from.

**OLD**
```
| **Opus escalation — a line, not a multiplier** | ~15% of tasks (≈ 32) run on Opus *instead of* Sonnet, same tokens at a higher rate: 32 × ($1.73 − $0.69) ≈ **+$33** |
```
**NEW**
```
| **Opus escalation — a line, not a multiplier** | ~15% of tasks — 15% of 210 = 31.5, i.e. **32** to the nearest whole task — run on Opus *instead of* Sonnet, same tokens at a higher rate. The delta is taken **unrounded**: $1.725 − $0.690 = **$1.035/task**. So 32 × $1.035 = $33.12 ≈ **+$33**. $1.035 is the only escalation delta used anywhere in §4.6 |
```

---

**Edit 3 of 5 — L1307.** The subtotal is the sum of the *unrounded* lines, not
of the two rounded ones. It matters because the old ceiling scaled the rounded
$178 and called the result a derivation.

**OLD**
```
| **Dev-time subtotal** | **≈ 72M tokens · ≈ $178** ($145 + $33) |
```
**NEW**
```
| **Dev-time subtotal** | **≈ 72M tokens · ≈ $178** — unrounded, $144.90 + $33.12 = **$178.02**; rounding first ($145 + $33) reaches the same $178, so the printed figure is stable either way. Downstream lines scale the **unrounded** per-task costs, never this rounded total |
```

---

**Edit 4 of 5 — L1315–1317.** The "runs in addition" variant multiplies by the
same unrounded figure, and shows its subtotal arithmetic. `32 × $1.725 = $55.20`;
`$144.90 + $55.20 = $200.10`. Both previously-printed roundings ($55, $200)
survive unchanged — only the derivation is made exact.

**OLD**
```
assumes Opus **substitutes** for Sonnet on those tasks; if it instead runs *in
addition* (a re-run rather than a substitution) the line is 32 × $1.73 ≈ +$55
and the subtotal ≈ $200.
```
**NEW**
```
assumes Opus **substitutes** for Sonnet on those tasks; if it instead runs *in
addition* (a re-run rather than a substitution) the line is 32 × $1.725 =
$55.20 ≈ **+$55** and the subtotal $144.90 + $55.20 = $200.10 ≈ **$200**.
```

---

**Edit 5 of 5 — L1329, the ceiling.** The whole sentence is replaced so the
printed figure is what its own inputs produce. The overrun scales *agent task
volume*; it does not scale the 200-match playtest plan, so part B is carried
across unchanged — that assumption is now stated rather than assumed, and is
flagged below for the Director. The all-in is a two-ended band because part B
already is one ($19 Haiku / $37 Sonnet); "near $290" was a midpoint of a band
that was never printed. Both ends reproduce from figures printed in the tables:
$266 + $19 = $285, $266 + $37 = $303.

**OLD**
```
Cost scales linearly with task volume, and the overrun case is stated rather than buried in a wide band: at **1.5× task volume** (315 rather than 210 tasks) the dev-time line is 315 × $0.69 + 47 × $1.03 ≈ **$267**, putting the all-in near **$290**. That is the ceiling, and it is a derivation rather than a round number — as is every figure in the two tables above.
```
**NEW**
```
Cost scales linearly with task volume, and the overrun case is stated rather than buried in a wide band. At **1.5× task volume** — 315 tasks rather than 210, of which 15% escalate to Opus (47.25, i.e. **47** to the nearest whole task) — the dev-time line is 315 × $0.69 + 47 × $1.035 = $217.35 + $48.645 = **$265.995**, i.e. **≈ $266**. The overrun is in *agent task volume*; it does not scale the 200-match playtest plan, so part B carries across unchanged and the all-in overrun is **$266 + $19 ≈ $285** with the Haiku 4.5 commander and **$266 + $37 ≈ $303** with Sonnet 5. **$303 is the ceiling.** Each of those is a derivation rather than a round number — as is every figure in the two tables above. (An earlier draft printed **$267** here. That was 1.5 × the *rounded* $178 subtotal, not a re-derivation from the per-task lines, and it sat $1.24 above what its own stated inputs produced — the second arithmetic fault this table has surfaced by being fully re-derivable, and the reason the escalation delta is now quoted unrounded at $1.035 throughout.)
```

---

### Every §4.6 figure that depends on the delta, re-derived

Checked against the post-edit text, each from its own printed inputs:

| Figure | Derivation from stated inputs | Prints as |
|---|---|---|
| Sonnet per task | $0.20 + $0.04 + $0.45 | **$0.69** (exact) |
| Opus per task | $0.50 + $0.10 + $1.125 | **$1.725** (exact) |
| Escalation delta | $1.725 − $0.690 | **$1.035** (exact, one figure only) |
| Sonnet-only base | 210 × $0.69 = $144.90 | ≈ **$145** |
| Escalation line | 32 × $1.035 = $33.12 | ≈ **+$33** |
| Dev-time subtotal | $144.90 + $33.12 = $178.02 | ≈ **$178** |
| "In addition" variant | 32 × $1.725 = $55.20; $144.90 + $55.20 = $200.10 | ≈ **+$55**, ≈ **$200** |
| Dev-time tokens | 210 × 345k = 72.45M | ≈ **72M** |
| All-in band, low | $178 + $19 = $197 (unrounded $178.02 + $18.60 = $196.62) | **$197** |
| All-in band, high | $178 + $37 = $215 (unrounded $178.02 + $37.20 = $215.22) | **$215** |
| Total tokens | 72.45M + 17.6M = 90.05M | ≈ **90M** |
| Overrun dev-time | $217.35 + $48.645 = $265.995 | ≈ **$266** |
| Overrun all-in, Haiku | $266 + $19 | ≈ **$285** |
| Overrun all-in, Sonnet | $266 + $37 | ≈ **$303** (ceiling) |

Part B was re-checked as well and needs no edit: $0.0025 + $0.00015 + $0.002 =
$0.00465 ≈ $0.0047/turn; ×20 = $0.093 ≈ $0.09/match; ×200 = $18.60 ≈ $19;
Sonnet introductory $0.005 + $0.0003 + $0.004 = $0.0093/turn → $37.20 ≈ $37;
standard rate $0.0075 + $0.00045 + $0.006 = $0.01395/turn → $55.80 ≈ $56.
20 × 4.4k = 88k/match; ×200 = 17.6M. All reproduce.

## Build order

No change this pass. This draft alters no system, stub, schema, dependency, or
acceptance test ID. T-SCN-05 and T-SCN-06..10 are untouched, per instruction;
nothing is renumbered.

## Change requests

| Existing § | Current text | Proposed change | Why |
|---|---|---|---|
| — | — | None outside §4.6 | All five edits are inside my own section and are given above as exact old→new pairs. |

## Open questions for the Director

No new rule gap, and no new register ID — the register stays **Q1–Q26**.

One **stated assumption** in Edit 5 needs a nod rather than a ruling: the 1.5×
overrun scales agent task volume only, leaving the 200-match playtest plan (and
therefore the whole of part B) unchanged. That is now written into the text
instead of being silently assumed, so a reader can disagree with it visibly. If
you would rather the overrun scale both surfaces, the ceiling becomes
$266 + $28 ≈ $294 (Haiku, 300 matches) or $266 + $56 ≈ $322 (Sonnet), and I
will file it as the next free register ID rather than claim one now — claiming
one unprompted is exactly what produced the Q24/Q26 double-filing you just had
to resolve.

## Handoffs

- **Director:** apply the five pairs; §4.6 is the only file region affected.
  Nothing in `../stratocracy-content/kb/rules.md` parses §4, so the KB re-sync
  step of the merge checklist is not triggered by this change.
- **rules-designer / scenario-designer / ux-onboarding-designer:** nothing.
  No rule, map, or screen figure moves.
- **continuity-gate:** re-check `invented-fact` §4.6 against Edit 5; the
  ceiling now reproduces as $217.35 + $48.645 = $265.995.

## Grounding

| Claim | Source |
|---|---|
| Rate lines ($2/$10, $0.20/M cache; $5/$25, $0.50/M; $1/$5, $0.10/M) — all unchanged by this draft | `source/gdd.md` §4.6 L1295, L1297 (md5 `d5fc06396a738ecb842b3263cf36c1ca`) |
| Sonnet per task $0.69; Opus per task $1.725 displayed as $1.73 | L1302–1303 |
| 210 tasks; 15% escalation; $145 / +$33 / $178 subtotal | L1304–1307 |
| "Escalation is priced once", the dead $225 figure, the +$55/$200 variant | L1309–1317 |
| Part B per-turn, per-match, 200-match and Sonnet-rate figures | L1323–1327 |
| The faulty ceiling line: `315 × $0.69 + 47 × $1.03 ≈ $267 … near $290` | L1329 |
| $267 = 1.5 × $178 (the rounded subtotal), the route that appears nowhere on the line | Arithmetic on L1307 and L1329 |
| Q26 owns the horizontal-mirror question in full; Stub 7 citation unchanged | Orchestrator ruling, this task prompt; §4.7 Stub 7 / §2.13.1 not edited here |
| Combat's 17/17 invariants @ `5ffa8d6` remain the only gate-verified system | §3 provenance ledger; §4.7 preamble L1331–1339 — unchanged by this draft |
