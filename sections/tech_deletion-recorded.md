> # ✅ APPLIED ADDENDUM — DO NOT RE-APPLY
>
> All 2 replacement pairs in this file **have been applied to the master GDD**.
> Verified 2026-08-10 against `source/gdd.md` md5 `1f27e981b623c7af2f6402d9a5b6a62b` (3365 lines): every OLD
> block is absent from the master, matched newline-insensitively. Re-applying is a
> no-op at best.
>
> Its quoted "current" text, register extents and open items are a **snapshot of
> the moment it was written**, not the state of the document.
>
> **The master GDD is the source of truth** — read `source/gdd.md`. Further changes
> to a merged section go in a *new* addendum file.

# Technical design — `deletion-recorded` addendum (tech-director)

## Placement

§3, the provenance-ledger evidence prose that precedes the ledger table (the
long paragraph ending `Legend: **Author** ∈ {agent, agent+human, human}; …`).
Two pairs, both inside the block that records crew `9289c1d`. No section is
redrafted. No ledger row, count, acceptance ID or open-question row moves.

---

## The sweep

**What I swept for.** Not "sentences about `9289c1d`" — sentences whose truth
value moves when the fourteen closure clauses stop existing in the crew tree.
Newline-insensitive, sentence-granular (`[^.\n]{0,170}(…)[^.\n]{0,170}\.` with
`multiline`), because `source/gdd.md` is hard-wrapped and §3's evidence prose is
one ~44 000-character line, so a line-oriented sweep returns "omitted long
matching line" and silently under-counts.

Predicates swept, each on the whole file:

| Predicate | Why it could move |
|---|---|
| `fourteen`, `closure claus`, `b5f524d`, `9289c1d` | the round's own subject |
| `clause`, `true negative`, `closure` | a sentence about what sits beside a clause |
| `runner module`, `spec documents`, `README`, `ten files`, `harness sources` | the master's description of the ten files |
| `crew repo`, `crew tip`, `crew tree` | present-tense claims about tree contents |
| `false`, `falsif`, `stale claim`, `assert that`, `asserted that`, `states that` | the falsity half, and its neighbours |
| `deleted`, `removed`, `corrected`, `retract` | an existing record of a removal that my pairs could collide with |
| `\b71\b`, `62 green`, `unclosed` | the counts the fact block says do not move |

**What moved.** Exactly two sentences, both in §3, both adjacent. Everything
else that mentions `9289c1d`, `T-SAVE-06`, `T-INT-02` or `0897cb5` is about a
*run* or a *green attribution*, and a deletion of prose does not touch either.

**Two sites I would not have predicted, and their disposition.**

1. §3 already carries `This commit **modifies only** — `git show --summary`
   prints no create, delete or rename line, **14 files changed**: `README.md`,
   `crew/tools.py`, …` — a *different* commit, whose subject is T-TURN-01's
   move/act split, T-TURN-10 and T-FAME-04. Its 14 is a **file count**; this
   round's 14 is a **clause count**, over 10 files. The collision is live in one
   paragraph. My NEW never writes "14 files" — it writes `10-file, +26 / −31` —
   so the two numbers cannot be read into each other. Not edited; flagged.
2. §3's `Sentences of the form *"they do not run **here**"* are true of every
   headless suite in that repo and were kept.` sits three sentences upstream of
   the pair and is present-tense about the crew tree. Its truth does **not**
   move: `b5f524d` deleted closure clauses, and `spec/replay_spec.md`'s
   *"`T-SAVE-06` does not close here … so no headless build closes it"* is a
   member of exactly this family and was kept. Not edited — but it is the same
   unpinned species as the sentence this round is repairing, so it is filed
   below rather than left silently.

---

## Draft — exact old → new pairs against `source/gdd.md`

Both OLD strings are copied byte-for-byte from `source/gdd.md`
(md5 `8c738e860a403d254af0317533b23c75`), and each is unique in the file.

### Pair 1 — the existence claim

**OLD**

```
**That same commit introduced false claims of its own:** fourteen clauses across **ten** files — two runner modules, three test and harness sources, the README and four spec documents — assert that `T-SAVE-06` and `T-INT-02` **closed** in the editor pass at `0897cb5`.
```

**NEW**

```
**That same commit introduced false claims of its own:** fourteen clauses across **ten** files — two runner modules, three test and harness sources, the README and four spec documents — asserted that `T-SAVE-06` and `T-INT-02` **closed** in the editor pass at `0897cb5`.
```

One word. `assert` → `asserted`. The file description is left exactly as
written because it is accurate against `b5f524d`'s file list: `crew/tools.py`
and `crew/offline.py` are the two runner modules; `test_replay.cpp`,
`test_save.cpp`, `test_balance.cpp` the three test and harness sources; plus
`README.md` and the four specs.

### Pair 2 — the neighbouring clause, and the deletion record

**OLD**

```
In almost every case such a clause sits beside a true negative — that no headless build can close `T-SAVE-06`, that it is marked † and asserted jointly with `T-INT-02` — and the true negative stands.
```

**NEW**

```
In almost every case such a clause sat beside a true negative — that no headless build can close `T-SAVE-06`, that it is marked † and asserted jointly with `T-INT-02`. **All fourteen were deleted at [`b5f524d`](https://github.com/jakemartin/stratocracy-crew/commit/b5f524d)**, across those same ten files — three in `crew/tools.py`, two each in `cpp_reference/test_replay.cpp` and `spec/integration_spec.md`, one in each of the remaining seven — in a 10-file, +26 / −31 diff that removed clause text and no file, and every adjacent true negative was kept as written there. Deleting a sentence does not make what it said true: `T-SAVE-06` and `T-INT-02` still ran and did not close at `0897cb5`, so all fourteen remain false, and what ended at `b5f524d` is their presence in the crew repo and nothing else. Three sites had also asserted that the two IDs were **not open** — false because `T-SAVE-06` and `T-INT-02` ran and passed at `0897cb5` without closing, so both remain open — and those assertions were deleted with the closure clause: `cpp_reference/test_balance.cpp`, `cpp_reference/test_replay.cpp` in `main()`, and `cpp_reference/test_save.cpp`. Two sites carried a true description of what the bridge does with `data/parity_fixture.save`, and that description was **kept and re-pinned to the bridge landing at UE `0897cb5`** rather than to a closure — `cpp_reference/test_replay.cpp`'s `main()` and `crew/tools.py`'s `certify_week1_fn`. §4.5's written, green and unclosed figures do not move at `b5f524d` — **71**, **62** and **9**, row 9's unclosed count staying **3** and row 10's **1** — because none of the ten files it touched is a vendored module source and none is in the Stratocracy UE project repo at all, so no acceptance ID's subject changed. `b5f524d` records a deletion and not a gate run, and no gate figure is cited for it.
```

**What gate run 1 changed in this NEW, and nothing else changed.** Three
referents were spelled; no disposition was cut and no claim weakened.

| Was | Now | Why |
|---|---|---|
| `which the same ruling falsifies` | `false because \`T-SAVE-06\` and \`T-INT-02\` ran and passed at \`0897cb5\` without closing, so both remain open` | No ruling is named anywhere in the NEW or upstream in the paragraph, and `CR-1` is a session label with 0 occurrences in `source/gdd.md`. The substance is stated instead, in the master's own §3 words — *"`T-INT-02`, `T-INT-03` and `T-SAVE-06` ran and passed, and none of them closes."* |
| `kept and re-pinned to **the landing**` | `kept and re-pinned to **the bridge landing at UE \`0897cb5\`**` | `parity_fixture` occurs 0 times in `source/gdd.md`, so no landing for it is identifiable there, and §3's definite-article convention resolves a bare "the landing" to the enclosing block's own commit — `b5f524d`, the deletion, which is not where the description was re-pinned. Commit supplied by fact-block appendix §A, measured from `b5f524d`'s own replacement text. |
| `their presence in **the tree**` | `their presence in **the crew repo**` | Not filed by the gate; found on the whole-NEW re-read. In §3 "the tree" overwhelmingly means the *vendored* tree (`over the vendored tree at \`0897cb5\``), and the clauses were never in it. `the crew repo` is the master's own phrase for the repository they were in. |

**Sentence between the two pairs — deliberately untouched.**

```
They ran and passed and did not close, so all fourteen are false.
```

This is the falsity half. The fact block's error species 3 forbids weakening it
into a past tense, and the safest way to not weaken a sentence is to not edit
it. It sits between Pair 1's OLD and Pair 2's OLD and is unchanged by both.

---

## Disposition of every candidate considered

A candidate is carried as **quoted master text plus its section number**, and
nothing finer. Quoted text checks itself against `source/gdd.md`; a description
of where inside a section a candidate lives is a separate assertion that has to
be verified separately, and at gate run 2 one such description was false while
the disposition it decorated was sound. Row 10 below is that row, now carrying
the sentence itself.

| # | Candidate sentence (§) | Disposition | Why |
|---|---|---|---|
| 1 | §3 `… fourteen clauses across **ten** files … **assert** that …` | **Edited (Pair 1)** | Present tense, no pin. The clauses no longer assert anything; `asserted` is true and stays true. |
| 2 | §3 `They ran and passed and did not close, so all fourteen are false.` | **Left, verbatim** | Falsity is a property of the propositions, not of their presence. `b5f524d` does not touch it. Editing it is the failure mode this round is guarding against. |
| 3 | §3 `In almost every case such a clause **sits** beside a true negative … and the true negative **stands**.` | **Edited (Pair 2)** | Both halves are unpinned present tense about tree contents. `sits` → `sat`; `stands` → `was kept as written there`, pinned inside the `b5f524d` clause. |
| 4 | §3 `Sentences of the form *"they do not run **here**"* are true of every headless suite in that repo and were kept.` | **Left, filed** | Truth does not move — `b5f524d` deleted closure clauses, and the surviving `spec/replay_spec.md` negative is a member of this family. Same unpinned species; see Open questions. |
| 5 | §3 `**Stale claims in the crew repo were repaired at [`9289c1d`]…:** eleven sites said …` | **Left** | The eleven repaired stale claims are a different set, in different files. `b5f524d` does not disturb the repair or its record. |
| 6 | §3 `**Two commit messages carry claims measurement contradicts, and neither can be amended.**` and the two sentences it governs | **Left** | A message cannot be amended by a later commit. `b5f524d` is a later commit; the point stands unchanged. |
| 7 | §3 `The tree was corrected at the crew tip; the message cannot be.` | **Left, filed** | About the `Selfplay` naming, corrected at crew `5072d10`. Same moving-referent species, but none of my pairs makes it false, so it is out of scope by the scope rule. Filed knowingly. |
| 8 | §3 `**Where a commit message and this ledger disagree, this ledger is the record.**` | **Left** | Unaffected; if anything, this round is that rule being applied. |
| 9 | §3 `This commit **modifies only** … 14 files changed: `README.md`, `crew/tools.py`, …` | **Left** | Different commit, different 14 (files, not clauses). Pair 2 writes `10-file` and never `14 files`, so no collision is created. |
| 10 | §3 `Both are green at [`9289c1d`] over the vendored tree at `0897cb5`` | **Left** | A green attribution is about runs. No vendored byte moved at `b5f524d`. |
| 11 | §4.5 `… among what its closure waits on is a further editor pass replaying the widened fixture in-engine, none having run since `0897cb5` (§3)` | **Left** | A claim about runs, not about clause text. Still true. |
| 12 | §4.5 `Row 2 was that clause's worked example while its editor half was outstanding, and it has since flipped (§3).` | **Left** | "that clause" is the † cut line, not one of the fourteen. |
| 13 | §4.9 `**`T-INT-02`, `T-INT-03` and `T-SAVE-06` ran and passed in the editor pass … without closing**` | **Left** | The no-closure finding, which is what makes the fourteen false. Unchanged. |
| 14 | §4.11 `Among what its closure waits on is a further editor pass replaying the widened fixture in-engine, none having run since `0897cb5`.` | **Left** | Same as #11. |
| 15 | §1.7, all of it | **Left** | Swept; the fourteen clauses, `9289c1d` and `b5f524d` appear nowhere in §1.7. |
| 16 | §3 `§4.5's written, green and unclosed figures do not move at this landing — **71**, **62** and **9** — row 9's unclosed count stays **3** and row 10's stays **1**.` | **Left; restated for `b5f524d` inside Pair 2** | The existing sentence is pinned to its own landing and stays true. Pair 2 states the same figures for `b5f524d` with its own reason, following the paragraph's established convention. |

**Verification of the arithmetic Pair 2 asserts.** Clauses: 3 (`crew/tools.py`)
+ 2 (`cpp_reference/test_replay.cpp`) + 2 (`spec/integration_spec.md`) + 7 × 1
= **14**. Files: 1 + 1 + 1 + 7 = **10**. The remaining seven are `README.md`,
`crew/offline.py`, `cpp_reference/test_save.cpp`,
`cpp_reference/test_balance.cpp`, `spec/replay_spec.md`, `spec/save_spec.md`,
`spec/balance_spec.md`.

---

## Re-read of each NEW against fact-block §4

| Species | Check against Pair 1 | Check against Pair 2 |
|---|---|---|
| 1 — no unpinned finite present-tense claim about the crew tree | NEW is past tense (`asserted`); no tree claim. | Every tree claim is inside a clause naming `b5f524d`: `were deleted at b5f524d`, `kept as written there`, `deleted with the closure clause`, `kept and re-pinned`, `none of the ten files **it touched**`. The only present-tense verbs left are `remain false` and `remain open` (properties of propositions and of acceptance IDs, not of tree contents), `can close` / `is marked †` (pre-existing), and `records a deletion` (a property of the commit). |
| 2 — "has since" is not a pin | n/a | The phrase does not appear; the deletion sentence names `b5f524d` and links it. |
| 3 — do not weaken falsity into past tense | Only the *asserting* verb moved. | `all fourteen remain false` — present, and `what ended … is their presence in the crew repo and nothing else` says explicitly which half ended. The untouched sentence `so all fourteen are false` is between the two pairs and unedited. |
| 4 — do not narrow the quantifier | `fourteen … across **ten** files` retained verbatim. | `**All fourteen were deleted**`, `across those same ten files`, and a per-file distribution summing to 14/10. No "most", no "the closure clauses". |
| 5 — state dispositions, not a count | n/a | Three named, all retained through the gate-run-1 repair: the closure clause deleted at all fourteen sites; three sites' "NOT open" assertions deleted with it, named; two sites' true fixture description kept and re-pinned to UE `0897cb5`, named; every adjacent true negative kept as written. |
| §2.6 — do not restate `b5f524d`'s unverified gate figures | n/a | No week-1 PASS, no 2/2, no compile-failure count. Pair 2 ends by saying so. |
| §1 — "the crew tip" is a moving referent | n/a | Pair 2 introduces no sentence depending on the tip. It does not say `b5f524d` is an ancestor of `c2f5860`, does not say how many clauses survive at the tip, and does not count what pairs those IDs with a closure word at the tip. |
| appendix §B — no NEW may cite `CR-1` or lean on an unnamed ruling | n/a | `CR-1` does not appear in either NEW; the no-closure finding is stated in substance. |

**Referents in Pair 2's NEW a master-only reader must resolve, after the
repair.** `such a clause` and `those same ten files` → Pair 1's sentence, two
sentences upstream in the same paragraph. `there` → `b5f524d`, the nearest and
only pin in its clause. `the bridge` → resolved forward in its own clause to the
bridge landing at UE `0897cb5`, which §3 already names (*"part 2's bridge
landed, at `0897cb5`"*). `row 9` / `row 10` → §4.5, the paragraph's standing
convention. `the remaining seven` → the ten of Pair 1 minus the three named
files; a cardinality, which is all the arithmetic needs, and the seven filenames
are deliberately not spelled to keep the sentence from becoming a file list.

---

## Build order

Unchanged by this round. No ledger row is created, flipped or removed; §4.11's
dependency table and §4.4's week numbers are untouched. Recorded here so the
absence is deliberate rather than an omission.

| # | System (ledger row) | Depends on | Headless? | Acceptance test IDs |
|---|---|---|---|---|
| — | *no row moves at `b5f524d`* | — | — | 71 written / 62 green / 9 unclosed, unchanged |

---

## Change requests

| Existing § | Current text | Proposed change | Why |
|---|---|---|---|
| §3 | `**That same commit introduced false claims of its own:** … **assert** that `T-SAVE-06` and `T-INT-02` **closed** in the editor pass at `0897cb5`.` | Pair 1 above | The clauses were deleted at `b5f524d`; a present-tense `assert` has gone false at the crew tip. |
| §3 | `In almost every case such a clause **sits** beside a true negative … and the true negative **stands**.` | Pair 2 above | Same species, plus the deletion record itself, its three dispositions, and the no-count-moves line. |

---

## Open questions for the Director

1. **`The tree was corrected at the crew tip; the message cannot be.` (§3).**
   Pre-existing, about the `Selfplay` naming corrected at crew `5072d10`, and
   none of my pairs falsifies it — so I left it. But "the crew tip" is a moving
   referent and this is precisely the species this round is repairing. Ruling
   wanted: pin it to `5072d10` in a later round, or accept "the crew tip" as an
   idiom for "some commit after the message" and say so once.
2. **`Sentences of the form "they do not run here" are true of every headless
   suite in that repo and were kept.` (§3).** Present tense, unpinned, about
   crew-tree contents. True today and unmoved by `b5f524d`, so out of this
   round's scope; same question as #1 — pin it or exempt it.
3. **Whether the ledger should ever record an ancestry fact.** The fact block
   measured that `b5f524d` is an ancestor of the crew tip `c2f5860`. I did not
   write it, because a sentence "X is an ancestor of the crew tip" expires the
   moment the tip moves in a way that a sha-to-sha statement would not. If the
   Director wants ancestry recorded, the durable form is `b5f524d` is an
   ancestor of `c2f5860`, both spelled — that is a Director ruling, not mine.
4. **Whether a post-deletion gate run should be commissioned.** `b5f524d`'s own
   message reports a week-1 PASS, integration 2/2 and zero compile failures.
   None was re-run for this round and none is restated. If the ledger wants a
   green at `b5f524d`, that is a run, and a different round.
5. **New, from the gate-run-1 repair: the no-closure finding has no name in the
   master.** It is the load-bearing premise of four separate §3 sentences and
   is restated in full every time, because `CR-1` is a session label with 0
   occurrences in `source/gdd.md`. Pair 2 restates it too. Either the Director
   mints a document-visible label for it once and later prose cites the label,
   or the restatement is accepted as the convention — but "the same ruling" and
   "that ruling" must not be used in either case, which is what blocked this
   file at gate run 1.
6. **Should "the tree", bare, be reserved for the vendored tree in §3?** It is
   used that way at nearly every occurrence, which is why Pair 2 now writes
   `the crew repo`. A one-line convention would make the next round's sweep
   mechanical instead of judgemental.
7. **New, from the gate-run-2 repair: apparatus locators are claims, and this
   file's last three findings were all in apparatus.** The disposition table now
   carries quoted master text and a section number only. If the Director wants
   finer locators in future addenda — a table name, a row number, a line range
   — they need the same verification a pair's OLD gets, and I would rather the
   convention say so once than have each author decide.

---

## Handoffs

None. No rule, map, scenario, screen or control surface is touched by either
pair. `rules-designer`, `scenario-designer` and `ux-onboarding-designer` have
nothing to action from this round.

---

## Grounding

| Claim in this file | Backed by |
|---|---|
| The two OLD strings, byte-for-byte | `source/gdd.md`, md5 `8c738e860a403d254af0317533b23c75`, the §3 evidence paragraph (single hard-wrapped line 1516) |
| The clauses were deleted at crew `b5f524d`; 10 files, +26 / −31 | `FACTS_deletion-recorded.md` §2.1 |
| Per-file clause distribution summing to 14 across 10 | `FACTS_deletion-recorded.md` §2.2, re-added here |
| The master's "two runner modules, three test and harness sources, the README and four spec documents" is accurate and needs no amendment | `FACTS_deletion-recorded.md` §2.3 |
| The three dispositions — "NOT open" assertions deleted at three named sites; the `data/parity_fixture.save` description kept and re-pinned at two named sites; every adjacent true negative kept as written | `FACTS_deletion-recorded.md` §2.4 |
| The fixture description was re-pinned to UE `0897cb5`, the bridge landing | `FACTS_deletion-recorded.md` appendix §A, measured from `b5f524d`'s own replacement text at both sites; §2.4's "the landing" is superseded there |
| No acceptance ID moves; 71 / 62 / 9, row 9 unclosed 3, row 10 unclosed 1 | `FACTS_deletion-recorded.md` §2.5 (inferred, with its reason restated in the NEW so a reader can check it), and the same figures already stated in §3's most recent landing sentence |
| The fourteen are false because `T-INT-02`, `T-INT-03` and `T-SAVE-06` ran and passed at UE `0897cb5` and did not close | The master's own §3 sentence *"**`T-INT-02`, `T-INT-03` and `T-SAVE-06` ran and passed, and none of them closes.**"*, restated in §4.9 and §4.11; `FACTS_deletion-recorded.md` §3 |
| `CR-1` is unusable inside a NEW, and no ruling is nameable there | `FACTS_deletion-recorded.md` appendix §B; `CR-1` occurs 0 times in `source/gdd.md`, which I re-measured |
| "the landing", bare, would resolve to `b5f524d` in the master | `FACTS_deletion-recorded.md` appendix §A; `parity_fixture` occurs 0 times in `source/gdd.md`, which I re-measured |
| "the tree", bare, reads as the vendored tree in §3 | `source/gdd.md` §3, where the phrase recurs as `over the vendored tree at \`0897cb5\`` and `the vendored tree at \`99fcb84\`` |
| No gate figure is cited for `b5f524d` | `FACTS_deletion-recorded.md` §2.6 — the figures were not re-run |
| `The tree was corrected at the crew tip` is pre-existing and unfalsified by these pairs | `FACTS_deletion-recorded.md` §5, and my own sweep, which found no pair-induced dependency on it |
| The unrelated "14 files changed" sentence belongs to a different commit | `source/gdd.md` §3, the landing whose subject is T-TURN-01's move/act split, T-TURN-10 and T-FAME-04 |
| Row 10's candidate text `Both are green at [\`9289c1d\`] over the vendored tree at \`0897cb5\`` | `source/gdd.md`, 1 occurrence, on line 1516 — the §3 evidence prose, which I re-measured newline-insensitively |
