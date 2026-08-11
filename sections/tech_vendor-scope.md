> # ✅ APPLIED ADDENDUM — DO NOT RE-APPLY
>
> All 3 replacement pairs in this file **have been applied to the master GDD**.
> Verified 2026-08-10 against `source/gdd.md` md5 `1f27e981b623c7af2f6402d9a5b6a62b` (3365 lines): every OLD
> block is absent from the master, matched newline-insensitively. Re-applying is a
> no-op at best.
>
> Its quoted "current" text, register extents and open items are a **snapshot of
> the moment it was written**, not the state of the document.
>
> **The master GDD is the source of truth** — read `source/gdd.md`. Further changes
> to a merged section go in a *new* addendum file.

# Technical design — `vendor-scope` draft (tech-director)

## Placement

Three old→new pairs, all inside §4: two in **§4.8 Data contract — DataTable
schemas**, one in **§4.9 Headless-module → Unreal integration path** part 1.
No §3 pair — see the disposition table for why.

## Draft

### Pair 1 — §4.8: give "the vendored bytes" its extent, before the ruling that quantifies over it

OLD

```
`GATE-DATA-VENDOR` asserts that the vendored bytes are the recorded ones, so the
two readers are reading one authored file rather than two that resemble each
other; it **mints no acceptance ID**, on the `GATE-AI-SMOKE` and
```

NEW

```
**On the data path the vendored bytes are five files in three kinds**, and the
extent matters because the ruling below quantifies over them: the three tables
this section schematises — `units.csv`, `terrain.csv`, `effectiveness.csv` — the
shipped scenario file `ferrum_crossing.json` (§4.7 Stub 7), and the committed
parity fixture `parity_fixture.save` (§4.10). `Data/StratData.manifest.json` at
`4ceaf93` records a sha256 for each of those five names and no others. **Only
the three tables are §4.8 tables.** The other two travel this path because both
sides must read the same bytes: §4.9 part 2's bridge loads the shipped scenario
through `strat::loadScenario`, and `T-INT-02` requires the headless and
in-engine replays to seed `GameState` from those bytes rather than from two
copies; the fixture the editor pass replays would compare the engine against
itself if it were re-emitted engine-side. Neither is imported into any
`UDataTable`, and `T-DATA-05` asserts over the tables alone — being carried
makes neither a table. Both joined on 2026-08-07, the fixture at
[`5c47cc1`](https://github.com/jakemartin/stratocracy-crew/commit/5c47cc1) (§3).
What is stated here is the extent of the data-side payload and not the meaning
of *vendored*, which §4.9 states once for both mechanisms.
`GATE-DATA-VENDOR` asserts that the vendored bytes are the recorded ones — all
five files, all three kinds — so the
two readers are reading one authored file rather than two that resemble each
other; the manifest itself is not one of those five, and it is verified by
recomputation rather than by hash-match for a stated reason: it records
`dataCommit`, so it cannot be stored at that commit — the same discipline
`StratRules.manifest.json` is under (§4.9). `GATE-DATA-VENDOR` **mints no acceptance ID**, on the `GATE-AI-SMOKE` and
```

### Pair 2 — §4.8: make the illustration read as the rule working

OLD

```
`4ceaf93`, which re-vendored the widened parity fixture; the three CSVs are
byte-identical across those two vendorings.
```

NEW

```
`4ceaf93`, which re-vendored the widened parity fixture; the three CSVs are
byte-identical across those two vendorings, and that is the rule working rather
than an exception to it. Exactly one data-touching crew commit falls between
those two vendorings — `c2f5860` — and it changed exactly one file,
`data/parity_fixture.save`. A vendored file changed, so `dataCommit` advanced;
had none changed, it would have stayed where it was. Read against the three
tables alone the same advance would be a counterexample, which is why the extent
is stated above rather than left to the reader.
```

### Pair 3 — §4.9: widen the narrowed payload, leaving the mechanism distinction and the 2026-08-06 ruling untouched

OLD

```
under which gate — the crew's C++ sources into `Source/StratRules/` by
`sync_stratrules.py` under `T-INT-01`, and the §4.8 CSVs into the UE project's
data directory by `sync_stratdata.py` under `GATE-DATA-VENDOR`. The sentence
above is about the first, and its quantifier is scoped by its own stated reason:
a UBT module cannot hold a second `main()`, which is a constraint on C++ sources,
so the CSVs sit outside it by construction rather than by exception.
```

NEW

```
under which gate — the crew's C++ sources into `Source/StratRules/` by
`sync_stratrules.py` under `T-INT-01`, and the data payload whose extent §4.8
states — five files in three kinds: the three §4.8 CSVs, the shipped scenario
file and the committed parity fixture — into the UE project's
data directory by `sync_stratdata.py` under `GATE-DATA-VENDOR`. The sentence
above is about the first, and its quantifier is scoped by its own stated reason:
a UBT module cannot hold a second `main()`, which is a constraint on C++ sources,
so all three data kinds sit outside it by construction rather than by exception.
```

## Disposition of every candidate

Cut from this draft: the sweep narrative — search terms, extraction method, the
"sites I would not have predicted" list, and the locator-convention note. The
table below is the record.

| Candidate (quoted from `source/gdd.md`) | Disposition |
|---|---|
| "`GATE-DATA-VENDOR` asserts that the vendored bytes are the recorded ones" | **Pair 1.** This is the sentence the missing extent was hanging off. |
| "`4ceaf93`, which re-vendored the widened parity fixture; the three CSVs are byte-identical across those two vendorings." | **Pair 2.** The illustration that read as a counterexample. |
| "the §4.8 CSVs into the UE project's data directory by `sync_stratdata.py` under `GATE-DATA-VENDOR`" | **Pair 3.** The narrowing the ruling names. |
| "**The manifest's `dataCommit` names the commit the vendored bytes came from, and it advances when and only when those bytes change (ruled 2026-08-06).**" | **Left alone.** The rule is true; only its quantifier's extent was missing, and Pair 1 supplies that three lines above it. Editing a ruling's text would re-date what rests on it for no gain. |
| "*Vendored* means the same thing in each: bytes copied out of a named commit's object store into the UE project, and gated for identity." | **Left alone.** Untouched by this round. Pair 3 changes only which bytes, in the clause that already exists to say which bytes. |
| "**The word is not split, and the reason is that the artifact does not split it:**" | **Left alone.** Still true and still the reason. |
| "*vendored* covers both, and the two mechanisms are distinguished once at §4.9." (§4.8) | **Left alone.** Pair 1 adds a pointer of the same shape rather than a second statement of the ruling. |
| "**The §4.8 CSVs are vendored, and their bytes are asserted rather than assumed:**" (§3) | **Left alone**, deliberately. It is a landing record pinned at `fed8ae9`, it says the CSVs are vendored and not that only they are, and I have no measurement of that manifest's `files` map at that commit. Widening it would be an unpinned claim about a past tree. |
| "over [`b1ea992`] … which vendors the §4.8 CSVs into the UE project — with the Stratocracy UE project repo at `fed8ae9`" (§3) | **Left alone**, same reason and same pin. `5c47cc1`, which put the fixture on this path, is not shown to precede that landing. |
| "an unrecorded file in the data directory (vendor only)" (§3) | **Left alone.** Already directory-scoped; the widened extent corroborates it. |
| "`sync_stratdata.py` carries the parity fixture from [`5c47cc1`]" (§3) | **Left alone.** Pair 1 cites it rather than restating it. |
| "The committed fixture carries the complete §4.9 command set at [`c2f5860`] and is vendored at that commit into the UE project at `4ceaf93`" (§3) | **Left alone.** The §3 twin of the §4.9 part 3 sentence below: it already speaks of the fixture as vendored, so the stated extent makes it consistent rather than disturbing it. No clause of it moves. |
| "The parity fixture's `stateHash` altered with the manifest untouched: `T-INT-02` FAIL and `GATE-DATA-VENDOR` FAIL" (§3) | **Left alone.** A known-bad-input record in which `GATE-DATA-VENDOR` already FAILs on a forged fixture — a non-table on this path — so it corroborates the stated extent rather than moving under it. It records what a past run did, and the stated extent changes nothing in it. |
| "the committed parity fixture carries the complete §4.9 command set at `c2f5860`, vendored into the UE project at `4ceaf93`" (§4.9 part 3) | **Left alone.** Consistent under the stated extent; no clause of it moves. |
| "the committed fixture carries the complete §4.9 command set at `c2f5860`" (§4.11) | **Left alone**, and not a candidate: this variant has no vendoring clause at all, so no extent for "the vendored bytes" changes its truth value. Recorded here only because an earlier draft of this table misaddressed the §4.9 sentence above to §4.11. |
| "`GATE-DATA-VENDOR` establishes that both halves ran against the same data bytes" (§3 and Q34) | **Left alone.** Q34 turns on row 2's acceptance set — `T-DATA-01..04, 06` headless plus `T-DATA-05` in the editor pass — and none of those five IDs' subjects changes. A gate that covers more bytes cannot weaken a claim that both halves read the same ones. |
| "T-DATA-05 (the editor pass) every imported DataTable row equals the CSV field-for-field" and the §4.8 `Acceptance:` line | **Left alone.** `T-DATA-05`'s subject is the imported tables. Pair 1 says so in terms rather than moving the invariant. No acceptance ID is minted, widened or re-dated by this round. |
| Q33 (`T-INT-01` text-vs-check) | **Out of scope, checked.** Its subject is `Source/StratRules/`; nothing on the data path bears on it. |
| §4.10 save & replay format | **Out of scope, checked.** It defines the fixture's format; it says nothing about vendoring. |

## Change requests

None.

## Open questions for the Director

None new on the round's rule content. The one rule gap this round existed to
close — the extent of the data-side vendored payload — is closed by Pairs 1 and
3 from measurements the fact block supplies. **Rule-gap count: 0.**

Standing and still unruled, filed by the previous round's author: **should
addendum apparatus be held document-wide to quoted master text plus a section
number, and no finer?**

One measurement I did not have and would need for a fourth pair: whether
`Data/StratData.manifest.json` at `fed8ae9` listed the two non-tables. Without
it the two `fed8ae9`-pinned §3 sentences stay as the disposition table records
them, which is the correct outcome either way — they are pinned and
non-exclusive.

## Handoffs

None. No rule, map, or screen changes.

## Grounding

- Five files, three kinds, and the manifest's `files` map at `4ceaf93` —
  `source/FACTS_vendor-scope.md` §2.1, §2.2.
- Why each non-table is carried, and that neither is imported into a
  `UDataTable` nor asserted by `T-DATA-05` — §2.3.
- The gate covering all five regardless of kind, and the manifest's exemption
  with its stated reason — §2.4.
- The 2026-08-07 join and crew `5c47cc1` — §2.5; the master already states the
  fixture half of it in §3.
- One data-touching commit between the two vendorings, `c2f5860`, changing
  `data/parity_fixture.save` alone — §3.1, §3.2.
- The two pinned vendorings, `dataCommit` `862a225` at `0897cb5` and `c2f5860`
  at `4ceaf93` — `source/gdd.md` §4.8, unedited by Pair 2's OLD boundary.
- `strat::loadScenario` on the shipped scenario asset — `source/gdd.md` §4.9
  part 2, **Load** bullet; read this round.
- Row 2's acceptance set and the Q34 repo-pair reading — `source/gdd.md` §3
  ledger row 2 and the Q34 row of §4.7.
- The two §3 sentences added to the disposition table this run — quoted from
  `source/gdd.md` §3's status line.
- That *"the committed fixture carries the complete §4.9 command set at
  `c2f5860`"* is what §4.11's build-order variant reads, without a vendoring
  clause — read this round on `source/gdd.md` §4.11.
