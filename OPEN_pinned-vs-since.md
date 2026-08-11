# Open candidate — claims that depend on a landing, and the "since" family

**Filed 2026-08-10, not scoped, not a round.** Noticed while sweeping addendum
seals; recorded so it is not re-discovered. Nothing here has been dispositioned.

Measured against `source/gdd.md` md5 `1f27e981b623c7af2f6402d9a5b6a62b` (3365 lines),
on a whitespace-collapsed copy so a sentence that wraps a line is still visible.
The matcher was control-tested against a known-absent string. **31** raw
occurrences of `has|have|having|had since` fall in **27** sentences —
two different units, and neither is the scope.

---

## The site that prompted this, and a correction to how I first reported it

I told the Director the master reads *"`T-UI-05` having since closed at
`41a1452`"* and flagged it as the unpinned `has since` shape. **That
characterisation was wrong, and the clause is not the problem.** It carries a
past participle of its own *and* names its own commit inline, plus points to a
fuller record at the end of its paragraph. On the enclosure test it passes.

What is exposed is the clause it sits inside, which occurs exactly once and sits
in **§3** by nearest preceding heading, both measured this round:

> `T-TURN-10` closed at `6ccd40b`, and the path IDs still written and asserting
> without being green **are** **T-UI-03** and **T-UI-04**

That `are` is present tense, carries no commit of its own, and is a claim about
the current state of two acceptance IDs. It goes false the moment `T-UI-03` or
`T-UI-04` closes. Whether a commit-pinned record encloses it has **not** been
measured — that is the first question a round here must answer, and it is a
question about the enclosing paragraph, not about the `since` wording.

## Two traps for whoever scopes this

**Proximity is not enclosure.** The `sha-near` flag below asks only whether a
seven-character sha appears within 160 characters after the match. That is a
cheap proxy and it is *not* the enclosure test, which asks whether a
commit-pinned record encloses the clause and whether the clause has a past-tense
verb of its own. **14** of 27 sentences carry a sha nearby and
13 do not; do not read either number as a verdict.

**Vocabulary is not the species.** This list matched four spellings of one idiom.
The species is *a claim whose truth depends on a landing, not enclosed by a
commit-pinned record* — and that can be written with no `since` in it at all
(`is currently`, `remains`, `still`, `as things stand`, a bare present-tense
`are`). The site above was found by reading, not by this probe. Sweep by meaning
and add what this missed; say plainly if it missed nothing.

**A count is not a disposition.** Give each item one of `pinned, so unmoved`,
`enclosed by a commit-pinned record`, `exposed — needs a pin`, `outside this
round`.

---

# Q1 answered — measured 2026-08-10

The question left open above: whether a commit-pinned record encloses the `are`
clause. **It does not.** Disposition of that clause: **`exposed — needs a pin`**.
It remains the only item here with a disposition; the 27 below have none.

Measured against `source/gdd.md` md5 `1f27e981b623c7af2f6402d9a5b6a62b`, the same
text this file was written against, on a whitespace-collapsed copy. The matcher
was control-tested against a known-absent string (0 hits) before each count.

**1 — The enclosing unit, MEASURED.** The clause occurs once, at line 1516,
character offset 3306. Line 1516 is the italic *Status: live tracker* block that
sits between §3's provenance-ledger lead-in and the ledger table, and it is
**101,086 characters on one physical line** — lines 1515 and 1517 are blank, so
that whole block is the only blank-line unit the clause sits in. It contains no
table pipe, no heading and no fence.

**2 — The candidate encloser, and why it fails, MEASURED.** The block opens
(offset ~230) with *"This draft stands at 2026-08-06, at commit `c2edae0` in the
crew repo and at `fed8ae9` in the Stratocracy UE project repo."* That stamp does
not enclose the clause, on a count that needs no reading of intent: **the block
cites four crew commits that postdate it.** In `../stratocracy-crew`, measured
per sha with `git merge-base --is-ancestor`, `cb8e12b`, `9289c1d`, `5072d10` and
`b5f524d` are each **not** an ancestor of `c2edae0`, and each was committed after
it — `c2edae0` committed at 2026-08-06T20:02:59-04:00, the four at
2026-08-07T13:48:25, 2026-08-07T16:31:44, 2026-08-07T18:13:43 and
2026-08-08T23:19:20-04:00. The eight other shas checked (`d8284f1`, `6ccd40b`,
`9086d6a`, `7c36303`, `41a1452`, `ec15be6`, `1ee890e`, `031ee20`) are ancestors.
A stamp its own block's later content outruns cannot fix that block's present
tense.

One other candidate was considered and rejected on subject: *"Measured at
`ec15be6`, every crew-repo commit this GDD cited then is an ancestor of
`ec15be6`"*, at offset 1212. Its subject is the ancestry of cited commits, not
the state of any acceptance ID. **These two were found by reading the block head
and by a scan over the terms `as read at` / `committed at` / `Measured at` /
`as at`. A pin can be written in none of those words — the stamp in the paragraph
above is itself an instance — so the scan does not establish that no third
candidate exists.**

**3 — The clause has no past-tense verb of its own, MEASURED by reading.** `closed
at 6ccd40b` is the verb of the coordinate clause before it. The exposed clause's
own verb is `are`, and it carries no commit.

**4 — The same fact is stated in enclosed form 30,348 characters later, MEASURED.**
Inside the `41a1452` landing record the block writes *"**T-UI-03 and T-UI-04 did
not run**, being editor-pass Automation marked † in §4.11, and **no editor pass
exists at this commit**"* (offset 33654) and *"after it the IDs it lacks are the
editor-pass `T-UI-03` and `T-UI-04`"* (offset 34621). Both sit inside a
commit-pinned landing record and are scoped to it. **That those two are enclosed
and tense-scoped is measured; whether what they say is true was not tested here.**
Being a separate record 30k characters later, neither reaches the clause at 3306.

**5 — Instrument finding for whoever scopes the round.** If "enclosed by a
commit-pinned record" is read as *anywhere in the same paragraph*, then every item
in this block is enclosed by that stale stamp and the test returns a pass for all
of them. **8 of the 27 items below sit inside line 1516** — items 2, 3, 4, 5, 6,
7, 8 and 9 — measured by locating each item's first 120 characters in the
collapsed block; the other 19 each match exactly once elsewhere in the document.
The test needs a stated reach before it is run on the rest. Fixing the stamp is a
separate question and is not dispositioned here.

---

# Q1(b) — what the landing that closes these two IDs makes false

Asked by the Director: the clause Q1 exposed is closed by an editor session, so
what happens after that commit. Measured against the same text and md5, on a
whitespace-collapsed copy, sentence-first; the matcher was control-tested against
a known-absent ID spelling (0 hits) before each count.

**The condition comes first: an editor session alone closes neither ID.** The
master states this itself — the harness *"is a runner and nothing more, and
running it supplies none of the subjects the IDs scheduled into it assert
against"*, and *"the harness is **also not sufficient**"*. Both IDs additionally
need real Stratocracy widgets, which the master records as **measured absent at
`a13626f`**. **That absence is the master's claim and was not re-measured here.**
It is the load-bearing condition for everything below: at a commit where the
widgets are still absent, no site in the table moves.

**MEASURED: 20 sentences in the master name `T-UI-03` or `T-UI-04`.** If the
widgets exist and both IDs go green, **nine sites go false or move**, of which
Q1's clause is one:

**Corrected 2026-08-10, beside the claim rather than over it: ten, not nine.** The
sentence splitter did not break at the `### 4.5` heading, so §4.9's *"What is
still uncelled is the real Stratocracy widgets `T-INT-05`, `T-UI-03` and
`T-UI-04` assert against"* was folded into the §4.5 risk-row entry instead of
being counted as a site of its own. It is the last row of the table. The nine is
left standing so the undercount stays visible, and the cause was the instrument,
not the reading.

| Site | As written | After the landing |
|---|---|---|
| §3, the Q1 clause | `are` **T-UI-03** and **T-UI-04** | false |
| §4.7 | "Five are **written and not green**" | three |
| §4.7 | "they are the IDs row 8 still lacks" | false |
| §4.11 | "**9 IDs remain unclosed**" | 7 |
| §3 | "**Two rows still carry evidence without a ✓**" | one |
| §3 | "**Ten rows carry a ✓** … two more carry evidence without one" | eleven, one |
| §4.5 risk row | "**71** written … against **10** verified ledger rows" | 71 unmoved, 11 |
| §4.5 running figures | 62 green, 9 unclosed | 64, 7 |
| §3 ledger table, UI row | "**Partial pass — not a flip.**" | flips to ✓ |
| §4.9 | "What is still **uncelled** is the real Stratocracy widgets …" | false |

**The two figure rows are arithmetic on the master's own recorded figures, not
read off a run:** §3 records the live figures as 71 written, 62 green and 9
unclosed, and the master's own convention through the block is that closing an ID
moves green up and unclosed down by the same step while the written count stays
put where no ID is minted. The ledger-row flip is conditional on Q29's per-row
reading and on these two being the only IDs row 8 lacks, which §4.11 states.

**Corrected 2026-08-10, beside the table rather than in it: the figure rows count
`T-UI-03` and `T-UI-04` in isolation, and the widget landing does not close only
those two.** It also closes `T-INT-05` (row 9, folded in below). A widget landing
that comes *before* the further editor pass therefore moves the figures 62 → 65
green and 9 → 6 unclosed, and the "**9 IDs remain unclosed**" row above reads 6
rather than 7 in that order. **These figures depend on which landing lands first,
and the table as first written assumed row 8 in isolation.**

**The remaining eleven sentences survive the landing** — they are pinned (`at this
commit`, `at either commit`, `at 41a1452`), or they are the §4.9 invariant text,
which specifies what the IDs assert and is not a claim about their state. **That
split is a reading of the twenty and is not measured.**

## Two things this changes for whoever scopes the round

**Pinning Q1's clause alone does not survive the landing.** It is one of seven
live prose sites that expire together, plus two figure sites. A repair that
reaches only the clause Q1 named leaves six sites saying the same expired thing —
the failure shape recorded in the `don't-narrow-a-universal` round, where every
repair that narrowed the quantifier made a new false claim.

**The widget landing is wider than these two IDs.** `T-INT-05` carries the same
widget dependency at three of the twenty sentences, and row 9's unclosed count of
**3** includes it. The commit that supplies widgets therefore reaches row 9 as
well as row 8, and this table does not cover row 9's sites. — **Corrected
2026-08-10: row 9 is measured and folded in below.** The sentence stood when
written.

## Row 9, on the same method — folded in 2026-08-10

**MEASURED: 63 sentences name `T-INT-02`, `T-INT-03` or `T-INT-05`.** Row 9's
three unclosed IDs **do not share a blocker**, and that changes the answer this
write-up gives above for row 8.

- `T-INT-02` and `T-INT-03` **already ran and passed** in the editor pass at
  `0897cb5`, and did not close because the fixture there carried `Move`, `Attack`
  and `EndTurn` and no `Capture` and no `Build` — a run and not a closure under
  Q29. What they wait on is a further editor pass, none having run since.
  **The complete-command-set fixture is already committed at `c2f5860` and
  vendored into the UE project at `4ceaf93`**, so their subject is in the tree.
- `T-INT-05` waits on the real Stratocracy widgets — the same dependency as
  `T-UI-03` and `T-UI-04`, and the reason it is not closed by an editor pass.
- `T-SAVE-06` belongs to row 10 rather than row 9, is asserted jointly with
  `T-INT-02`, and did not close at `0897cb5` for that same fixture reason.

**So for row 9, unlike row 8, an editor session alone does close something.** The
two landings are separate triggers with separate consequences:

| Trigger | Closes | Unclosed | Green |
|---|---|---|---|
| A further editor pass over the complete fixture | `T-INT-02`, `T-INT-03`, `T-SAVE-06` | 9 → 6 | 62 → 65 |
| The widget landing | `T-INT-05`, `T-UI-03`, `T-UI-04` | 6 → 3 | 65 → 68 |

The residue of **3** is row 7's `T-SCN-08`, `T-SCN-09` and `T-SCN-11`. The nine
decomposes exactly — 3 + 2 + 3 + 1 — measured from §4.11's own enumeration, which
is why the two triggers account for all of it and no ID is left unassigned.

**A condition that blocks both ledger creations, and is not measured here.** Rows
9 and 10 are **named but uncreated**: neither is in §3's ledger table, which holds
twelve rows, and each is created as one row when its full set closes. Q29 requires
the full set green **at one commit**. `T-INT-02`/`T-INT-03` closing at one pass and
`T-INT-05` at another does not satisfy that unless the later pass re-runs all five,
and the same holds for row 10 over `T-SAVE-01..07`. **Whether either pass carries
its whole set was not measured, so neither row's creation is asserted here** — the
green and unclosed figures above do not depend on it.

---

## 1  [NO-SHA-NEAR]

> **It has since run, and §3 records the run:** it passed on a fixture configured with `captureTurns = 2`, a state *Ferrum Crossing* cannot reach at N = 1 (Q4).

## 2  [sha-near]

> What week 1 did **not** close is everything after it: rows 4–8 held no code then, and **rows 4, 5 and 6 have since landed** — all three recorded at the end of this paragraph — so at `d8284f1` only rows 7–8 hold none; since §4.11's critical path runs 1 → 3 → 4 → 5 → 6/8, every row on that path has since landed, **row 8** last and on a partial pass that leaves its ledger row unflipped — **per acceptance ID as well as per row**: `T-TURN-10` closed at `6ccd40b`, and the path IDs still written and asserting without being green are **T-UI-03** and **T-UI-04**, `T-UI-05` having since closed at `41a1452` as recorded at the end of this paragraph, and row 8's other dependency is **row 7**, which has since landed at [`9086d6a`](https://github.com/jakemartin/stratocracy-crew/commit/9086d6a) on a partial pass, recorded at the end of this paragraph. §4.5's *Specification outruns the build* risk is therefore reduced and re-scoped rather than retired, and that row now states the arithmetic.

## 3  [NO-SHA-NEAR]

> **Seven** tracked sources defined `main()` at that commit — `cpp_reference/test_combat.cpp`, `cpp_reference/test_hex.cpp`, `cpp_reference/test_data.cpp`, `cpp_reference/test_move.cpp`, `cpp_reference/test_driver.cpp`, `cpp_reference/selfplay.cpp`, `cpp_reference/driver_main.cpp` — five test harnesses, one combat duel simulator, and the REPL; **row 4 has since added an eighth**, counted at the end of this paragraph.

## 4  [sha-near]

> That set has since widened to `T-TURN-01..10` and row 5 was rebuilt against it; **this sentence records what ran at `ad77b13` and is not row 5's current evidence**, which is recorded at the end of this paragraph.

## 5  [NO-SHA-NEAR]

> **All three have since been ruled into §4.7 Stub 8**, on 2026-08-04: the first two as snapshot fields — the per-factory block `{hex, owner, hasBuiltThisTurn, buildWaiting, spawnBlocked}` and the per-side `incomePerTurn` — and the DONE bit into the stub's **presentation block**, which the rules module does not produce and which is the second half of the view-model beside the snapshot.

## 6  [NO-SHA-NEAR]

> Whether the ledger should gain the row was filed for the Director and has since been ruled, at the end of this paragraph.

## 7  [NO-SHA-NEAR]

> **The Director has since named that row without creating it (ruled 2026-08-05):** it is **Headless → Unreal integration**, its acceptance set is `T-INT-01..05`, and it is created as **one** row when §4.9 part 2 lands whole — which is this deferral's own reason stated forward rather than a second decision.

## 8  [NO-SHA-NEAR]

> **The Director has since named that row without creating it (ruled 2026-08-05), on Ruling K's precedent for row 9:** it is **Save & replay**, its acceptance set is `T-SAVE-01..07`, and it is created as **one** row when that full set closes — which under Q29 is the same condition as its flipping — so parts (a), (b) and (c) resolve to one ledger row rather than to several, and what it waits on is `T-SAVE-06` alone, `T-SAVE-07` having since closed at [`1ee890e`](https://github.com/jakemartin/stratocracy-crew/commit/1ee890e) on part (c).

## 9  [NO-SHA-NEAR]

> **Two forms were considered and declined, with the reason recorded so neither is re-filed:** a document-wide reachability form that survives a landing, and a rule that a "has since" sentence must carry a commit pin.

## 10  [sha-near]

> **Turn loop & win / tiebreak** joined at [`ad77b13`](https://github.com/jakemartin/stratocracy-crew/commit/ad77b13) — T-TURN-01..09, **9/9 under clang++ and MSVC both** — and its acceptance set has since widened to **T-TURN-01..10**, green at the [`6ccd40b`](https://github.com/jakemartin/stratocracy-crew/commit/6ccd40b) rebuild under clang++ and MSVC both, on **11 printed checks over those ten IDs**.

## 11  [sha-near]

> T-DATA-05 was why **Data tables** carried evidence without a ✓; it has since run, 4/4 in the editor pass at `fed8ae9`, completing that row's acceptance set across the repo pair Q34 rules on, and that row now carries one.

## 12  [sha-near]

> `T-SAVE-06`, `T-INT-02` and `T-INT-03` did not close here, and have since run and passed without closing, in the editor pass at `0897cb5` in the Stratocracy UE project repo against the crew half `cb8e12b` (§3), in no week this table names: `Replay` was vendored into `Source/StratRules/` at that UE commit and the bridge's command surface landed there, and the editor pass all three also lacked had landed at `fed8ae9` in the same repo (§3).

## 13  [sha-near]

> The principle stated above — the week the thing that consumes it runs — governed the two that have since landed off this calendar: the vendored replayer and the bridge's command surface, both at `0897cb5` in the Stratocracy UE project repo against the crew half `cb8e12b`, where `T-INT-02`, `T-INT-03` and `T-SAVE-06` ran and passed in the editor pass without closing (§3).

## 14  [NO-SHA-NEAR]

> Row 2 was that clause's worked example while its editor half was outstanding, and it has since flipped (§3).

## 15  [sha-near]

> **T-CAP-05 is excepted:** it aliases onto no `T-TURN-` ID (§2.8), and its gate home was ruled on 2026-08-02 to be Stub 8's snapshot, where it is `GATE-CAP-PARTIAL`; row 8 has since landed at [`7c36303`](https://github.com/jakemartin/stratocracy-crew/commit/7c36303), where that gate ran and passed under clang++ and MSVC both — on a fixture configured with `captureTurns = 2`, a state the shipped scenario cannot reach at N = 1 (Q4).

## 16  [sha-near]

> Does a partially captured objective count toward "objectives held" (§2.8 criterion 2)? | T-CAP-05 — the one `T-CAP-` ID with no `T-TURN-` counterpart (§2.8's alias map); its gate home was ruled on 2026-08-02 to be Stub 8's snapshot, where it is `GATE-CAP-PARTIAL`, and row 8 has since landed at [`7c36303`](https://github.com/jakemartin/stratocracy-crew/commit/7c36303), where that gate ran and passed under clang++ and MSVC both, on a fixture configured with `captureTurns = 2` — a state *Ferrum Crossing* cannot reach, since it ships N = 1 on Q4's ruling.

## 17  [NO-SHA-NEAR]

> **Scope, re-checked after the Q28 deployment move rather than assumed.** This row's scope was stated as a property of the drawn deployment, and a deployment has since moved — East's second Infantry (9,5) → (9,1), §2.13.2 — so it was re-measured.

## 18  [NO-SHA-NEAR]

> Part 2 has since supplied it — the bridge's load mapping and command surface are built, and it has no event list, no actor and no widget — and the crew declared `Save` and `Replay` vendored at [`f5fdb69`](https://github.com/jakemartin/stratocracy-crew/commit/f5fdb69), the UE project vendoring them into `Source/StratRules/` at `0897cb5`, which makes the vendored set twelve: the ten enumerated above plus those two.

## 19  [sha-near]

> **`T-DATA-05`'s two subjects have since been built** (§3): at `fed8ae9` the `UENUM` mirror `EUnitType` and the imported `DT_Units`, `DT_Terrain` and `DT_Effectiveness` exist, alongside `FUnitRow`, `FTerrainRow` and `FEffectivenessRow` — all of them in the `Stratocracy` module and none in `Source/StratRules/`, which is the constraint stated below.

## 20  [NO-SHA-NEAR]

> It is not the live statement about the vendored replayer or the command surface: both have since landed, as recorded above.

## 21  [NO-SHA-NEAR]

> ``` ### 4.11 Build order Rows 1–8 are the §4.7 stubs — the eight ledger rows that read `*pending*` when this table was written, of which **rows 1, 2, 3, 4, 5 and 6 have since flipped** (§3), row 2 last and across a repo pair (Q34). §4.7's heading names the same eight **as at 2026-08-01** and is dated for that reason: it records a state and is not a live count, so it does not move when a row flips and is not out of step with this sentence.

## 22  [sha-near]

> **Row 8 has since landed too**, at `7c36303`, on a partial pass that leaves its ledger row unflipped, as row 7's does (§3): T-UI-03 and T-UI-04 are the editor-pass half and no editor pass exists at that commit, and **T-UI-05 was then headless and unimplemented** — minted 2026-08-04, after that commit.

## 23  [sha-near]

> **Row 9's headless half has since landed**, at `b23823f` in the crew repo with the vendored tree at `99fcb84` in the UE project repo, which is what this row's cell means by closing as soon as vendoring lands.

## 24  [NO-SHA-NEAR]

> **T-INT-02/03/05** need only the rows behind the log they replay: rows 1–3 for week 2's `{Move, Attack}` log, and they re-open on the `Capture`/`Build`/`EndTurn` that rows 4–5 have since added.

## 25  [sha-near]

> **Part (a) has since landed**, at [`737f666`](https://github.com/jakemartin/stratocracy-crew/commit/737f666): `T-SAVE-04` is green there under clang++ and MSVC both, beside `GATE-SAVE-PARSE`, which mints no acceptance ID, so this row holds code without closing its set (§3). (b) *Headless replayer* — rows 1–3, plus row 7's **structural** half for the `scenarioId`/`scenarioHash` it loads; it runs T-SAVE-01/02/03/05/06 over week 2's `{Move, Attack}` log. (c) *Closure* — rows **4, 5** complete the command set (T-SAVE-01/03/05/06), row **6** completes T-SAVE-02's determinism composition, and T-SAVE-07 needs row 6's self-play besides.

## 26  [sha-near]

> **Part (b) has since landed**, at [`ec15be6`](https://github.com/jakemartin/stratocracy-crew/commit/ec15be6), and was run against these closure conditions rather than after them (ruled 2026-08-05, rows 4, 5 and 6 all being green): `T-SAVE-01`, `T-SAVE-02`, `T-SAVE-03` and `T-SAVE-05` are green there under clang++ and MSVC both, beside `GATE-REPLAY-*`, which mint no acceptance ID.

## 27  [sha-near]

> **Part (c) has since landed**, at [`1ee890e`](https://github.com/jakemartin/stratocracy-crew/commit/1ee890e), on a third registry row whose link set encodes exactly the dependency this cell states — rows 4, 5 and 6: `T-SAVE-07` is green there under clang++ and MSVC both, beside `GATE-BALANCE-*`, which mint no acceptance ID.
