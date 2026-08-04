# Gate report — run `t-cap-05-rebuild-2`

Master: `source/gdd.md` @ md5 `d2cfe86d6decad525a9a002d3f2c17b8`
(`source/MANIFEST.txt` present; `kb_rules.md` @ `024523449be1873c9d545dbea6d3bc9d`,
`kb_setting.md` @ `b3e9e89daaef1cdeb333e3fb4368d1c0`.)

**Top-level verdict: PASS.** One section, one PASS, **0 violations.**

---

## sections/tech_t-cap-05-and-rebuild.md — PASS (0)

No violations filed. Four pairs, all replacements, all four OLD anchors unique.

### The two `t-cap-05-rebuild-1` findings — both cleared

**1. `contradiction` (T-SCN-08 (c) "accepted as closing") — cleared, and the
replacement is verified rather than accepted.**

The string "accepted as closing" occurs nowhere in
`sections/tech_t-cap-05-and-rebuild.md` and nowhere in `source/gdd.md`. The
rewritten precedent reads:

> a synthetic fixture is legitimate exactly where the stub calls for one and
> counts when it runs — the precedent is **T-SCN-08 (c)**, whose stub asks for a
> scenario whose lanes both cost 7 and names no map, and which ran and was
> counted at `9086d6a`. T-SCN-08 itself does not close, on fixtures (a) and (b),
> which need a stretch map nobody has authored

Each limb checks out against the master:

- *"a scenario whose lanes both cost 7"* and *"names no map"* — §4.7 Stub 7,
  T-SCN-08's fixture list: "(c) A scenario whose lanes both cost 7 FAILS the
  T-SCN-06 ceiling", against (a) *The Causeway* and (b) *Longwater March*, which
  are named maps. Fixture (c) is the only unnamed one.
- *"ran and was counted at `9086d6a`"* — §3, row-7 paragraph: "**T-SCN-08,
  T-SCN-09 and T-SCN-11 ran a part of their fixture sets and do not close** —
  T-SCN-08 on fixture (c) plus its measure-and-report behaviour on the shipped
  map", inside a gate recorded "**12/12 under clang++ and MSVC both**" whose
  twelve decompose as T-SCN-01..07 + two `GATE-SCN-` checks + those three
  partial IDs. So (c) both ran and was counted.
- *"does not close, on fixtures (a) and (b)"* — §3: "**Four fixtures did not
  run** … T-SCN-08 (a) *The Causeway* and (b) *Longwater March* … Each needs a
  stretch map authored as a scenario file, and **none was replaced by a
  synthetic map**." Consistent too with §4.11's † note, which says a stood-down
  T-SCN-08 keeps "only the synthetic ceiling refusal (c)".

The contrast the ruling now rests on is likewise carried by the master. The cell
claims `GATE-CAP-PARTIAL` "has **one** written fixture and it ran, under clang++
and MSVC both, so no part of its set is outstanding". §4.7 Stub 8's
`GATE-CAP-PARTIAL` block enumerates no fixture list and states one differential
assertion; §3's row-8 paragraph records the run on "**a fixture configured with
`captureTurns = 2`**" (singular), and its pass-1 tally is decisive on the count —
"**four FAIL lines over two distinct IDs**, `T-UI-02` on all three of its checks
and `GATE-CAP-PARTIAL` on its differential" — three plus one, so the gate is a
single check. Nothing in §3's enumeration of what did not run at `7c36303`
(T-UI-03 and T-UI-04, both whole IDs) leaves any part of that gate outstanding.
The per-ID reading of Q29 the cell applies is the master's own: §3 applies Q29
"**per acceptance ID as well as per row**", and applies it to T-SCN-08 the other
way — "Q29, read per ID, keeps the row unverified" (§3's Content / scenario
evidence cell). The asymmetry the cell asserts is therefore the document's.

**2. `dead-reference` ("the row above it") — cleared.** The referent is now
named and internal:

> **This rules the closure only, and not Q14's own rules question** — whether a
> partially captured objective counts toward "objectives held" — which keeps the
> stated reading in the next column and stays open

That matches Q14's own Question column ("Does a partially captured objective
count toward \"objectives held\" (§2.8 criterion 2)?") and points at the
Assumption column, which is in fact the next column after Blocks and reads "It
counts for nobody until the objective flips". No pointer escapes the row.

### The Grounding bullet that carried the same false fact

The bullet now reads:

> T-SCN-08 (c) as the synthetic-fixture precedent — §4.7's T-SCN-08 fixture
> list. §3's row-7 paragraph records that (c) ran at `9086d6a` while (a) and (b)
> did not, each needing a stretch map authored as a scenario file, and that
> T-SCN-08 therefore **does not close**; §4.5 counts it among the 18 unclosed.

It agrees with the §4.5 arithmetic bullet beneath it, which lists "Unclosed 18 =
T-DATA-05 + T-SCN-08 + T-SCN-09 + T-SCN-11 + T-UI-03 + T-UI-04 + 12 in rows
9–10", and with §4.5 itself. The remaining Grounding bullets are unchanged in
substance and each still resolves: §2.7's "N is per-scenario data" is verbatim at
§2.7's Capture bullet; Stub 8's "raising a unit's captureProgress short of
completion" is verbatim; §3's row-8 paragraph carries the `7c36303` clang++/MSVC
pass and the pass-1 partial-credit refusal. No ungrounded substantive claim
remains in the section.

### Re-confirmed after the revision

- **No new contradiction about T-SCN-08's status.** Every T-SCN-08 site in the
  master — §3's row-7 paragraph, §3's Content / scenario evidence cell, §3's
  eight-uncovered-IDs passage, §4.5's unclosed list, §4.11's † note — records the
  ID as written, asserting and **not closed**, which is exactly what the
  rewritten cell now says.
- **No new contradiction about T-CAP-05's status.** Its status is asserted at
  three sites only — §2.8's exception paragraph (Pair 1), §4.7's register
  preamble (Pair 2) and Q14's Blocks cell (Pair 3) — and all three move together.
  The other T-CAP-05 mentions (§2.8 criterion 5 and the alias table, Stub 8's
  block, §4.7's "excepted" sentence, Q6's cell) state alias, gate home or rule
  text and no closure state, so none is falsified.
- **Anchors.** All four OLD strings occur exactly once in `source/gdd.md` and
  none is empty: §2.8 line 404, §4.7 preamble lines 2471–2472, Q14's Blocks cell
  line 2499, §3's status paragraph inside line 1513 ("provisionally met" — 1
  occurrence file-wide). All four are replacements; no insertions. Pair 3's OLD
  still ends at "the kb victory table" and the NEW still ends there, so the
  cell's column structure is unchanged.
- **Format.** Placement, Draft, Change requests, Open questions, Grounding all
  present.
- **Dates and voice.** All four pairs rule 2026-08-04, which is today; the new
  prose is declarative and present-tense and matches the register's register.

Not re-litigated, per the run brief and unchanged since `t-cap-05-rebuild-1`: the
§4.5 decomposition (70 = 52 + 18, T-CAP-05 in neither), both rulings' blast
radius, §4.11's Build-order row 8 reproduction, and the absence of `kb-desync`.

---

## Verdict

**PASS.** Both `t-cap-05-rebuild-1` violations are fixed at their source rather
than papered over: the T-SCN-08 precedent is restated as what the master actually
records — a synthetic fixture that ran and was counted while the ID it belongs to
stays open — and the closure/rules-question distinction now points at Q14's own
question and its Assumption column instead of at the row above. The correction of
the duplicated false fact in Grounding is within the filed finding and leaves that
list consistent with the §4.5 line below it. Nothing else in the section moved,
all four anchors still resolve uniquely, and no §4.5 count, register count or
ledger row changes. The section is clear to merge as four exact replacements; the
Director's remaining decisions are the two Open Questions the author filed, which
are choices rather than defects.
