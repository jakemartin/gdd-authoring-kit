# Gate report — run `vendor-scope-4`

`source/MANIFEST.txt` present; `gdd.md` md5 `8c738e860a403d254af0317533b23c75`,
matching the md5 `source/FACTS_vendor-scope.md` §0 states. Sections read: one —
`sections/tech_vendor-scope.md`. Fact set read: `source/FACTS_vendor-scope.md`.

**Top-level verdict: PASS. 0 violations.**

**Where I measured.** `source/gdd.md` was searched newline-insensitively with
multiline patterns throughout; every quote in this report was extracted with a
bounded-window `-o` match rather than by line, because §3's status line —
**line 1516** — is a single ~30,000-character source line that no line-oriented
read returns. Section extents re-measured this run from the heading index:
§3 begins **1425**, §4.4 **1563**, §4.7 **1629**, §4.8 **2669**, §4.9 **2774**
(part 1 opens at **2779**), §4.10 **3066**, §4.11 **3183**. Every locator below
is a claim and each was measured in this run, not carried from run 3.

One correction to my own method, recorded because it nearly produced a false
finding: a first pass for `committed parity fixture carries` returned **zero**
hits and would have made the §4.9 part 3 disposition row look like a fabricated
quote. The master hard-wraps between `fixture` and `carries` (2970/2971), so the
literal-space pattern could not match. The newline-insensitive re-run found it
exactly once at **2970-2972**. No finding rests on a single-spelling sweep.

---

## `sections/tech_vendor-scope.md` — PASS (0)

No violations. What follows is the record of what was checked, since a PASS on a
draft that *deleted* a section has to show the deletion left nothing behind.

### Item 1 — the two run-3 universals are gone by deletion, and neither was inherited

Case-insensitive sweep of the draft for `only place`, `all found`, `sites I
would not`, `search term`, `windowed`, `locator convention`: the **only** hits
are draft lines 100-101, which are the cut record itself —

> Cut from this draft: the sweep narrative — search terms, extraction method, the
> "sites I would not have predicted" list, and the locator-convention note. The
> table below is the record.

Both falsified constructions — *"the only place the master already names a
non-table on this path"* and the *"all found in that §3 line"* heading — are
absent as text and, more importantly, absent as meaning. I read every
quantified sentence that survives and none carries either scope claim:

- The `sync_stratdata.py`-carries-the-fixture row (draft line 116) now reads
  only **"Pair 1 cites it rather than restating it."** — no exclusivity clause.
- The §4.9 part 3 row (line 119) makes no claim about *where in the document*
  the sentence sits beyond `(§4.9 part 3)`, which resolves to 2970-2972 inside
  §4.9 (2774-3066). Nothing quantifies over a set of sites.

Nothing was narrowed into a smaller-but-still-false universal, which was the
failure shape the instruction named.

### Item 2 — the two added §3 dispositions: quotes byte-exact, dispositions correct

**Row A**, draft line 117, quoted as *"The committed fixture carries the
complete §4.9 command set at [`c2f5860`] and is vendored at that commit into the
UE project at `4ceaf93`"*. Master, §3 status line **1516**:

> The committed fixture carries the complete §4.9 command set at
> [`c2f5860`](https://github.com/jakemartin/stratocracy-crew/commit/c2f5860) and
> is vendored at that commit into the UE project at `4ceaf93`;

Byte-exact apart from the elided link target inside the `[...]`, which is the
table's pre-existing convention on `[`b1ea992`]` and `[`5c47cc1`]` and was
cleared at run 3. The disposition — **Left alone**, "it already speaks of the
fixture as vendored, so the stated extent makes it consistent rather than
disturbing it" — is right: the sentence asserts the fixture *is vendored into
the UE project at `4ceaf93`*, which is the same vendoring §4.8 (2687-2690)
describes as having "re-vendored the widened parity fixture". A five-file extent
makes it true; a three-CSV extent is what would leave it stranded. No clause of
it moves.

**Row B**, draft line 118, quoted as *"The parity fixture's `stateHash` altered
with the manifest untouched: `T-INT-02` FAIL and `GATE-DATA-VENDOR` FAIL"*.
Master, same line **1516**:

> **…on three known-bad inputs, each restored afterwards.** The parity fixture's
> `stateHash` altered with the manifest untouched: `T-INT-02` FAIL and
> `GATE-DATA-VENDOR` FAIL.

Byte-exact. The disposition — **Left alone**, a known-bad-input record in which
`GATE-DATA-VENDOR` already FAILs on a forged fixture — is right on both halves:
it is inside §3's three-known-bad-inputs list, and the gate FAILing on a forged
*non-table* is corroboration of the wider extent, not a sentence that moves
under it. It is a past-run record; the stated extent changes nothing in it.

### Item 3 — the disposition table is complete on its own terms

This is the check the cut made necessary, so it was done by sweeping the master
rather than by reading the table.

Every occurrence of the round's key phrase **`vendored bytes`** in the master —
**2679** (Pair 1's OLD), **2683** (the 2026-08-06 ruling, dispositioned *Left
alone*) and **3034** — is accounted for. 3034 is `T-INT-01`'s invariant text
inside a §4.9 spec stub, whose subject is `Source/StratRules/`; fact-block §1
holds the rules path out of this round, so it is not a data-path candidate.

Every occurrence of **`sync_stratdata.py`** — **1516** (§3, dispositioned),
**2676** (§4.8 "*vendored* covers both", dispositioned), **2809** (Pair 3's OLD)
and **2814** (§4.9 "the word is not split", dispositioned) — is accounted for.

Every occurrence of **`dataCommit`** — **1516**, **2682-2683**, **2685**,
**2692** — was read. 2682-2683 is dispositioned. The other three are unaffected:
1516 records `dataCommit` `862a225` at a pin; 2685 ("a crew commit that does not
touch the data directory leaves it where it is") is directory-scoped and
corroborating; 2692 ("what it asserts is the file hashes") is unqualified as to
kind and stays true under five files.

I looked specifically for a sentence whose **truth value moves** under the
stated extent and is missing from the table, and found none. Two things that are
*not* violations, recorded so the Director can see they were weighed:

- §3's sibling known-bad input, *"The same forgery with the manifest **updated to
  match**: `GATE-DATA-VENDOR` passes and **`T-INT-02` FAILS alone**"* (line
  1516), is not in the table. Its truth does not move — like Row B it already
  treats the fixture as gate-covered — so under the criterion that admits
  everything else in the table, it is not a candidate. Filing it would be an
  apparatus finding against a sentence nothing in this round touches.
- The string the §4.11 row quotes occurs **twice**, at **1569** (§4.4's week-3
  milestone cell) and **3252** (§4.11). Both carry **no vendoring clause**, so
  neither is a candidate and the §4.4 twin's absence is correct. Same disposition
  as run 3, re-measured rather than carried.

### Item 4 — re-checked from scratch, not assumed to have survived

**The three OLDs.** Each multiline pattern returned exactly **one** hit:
**2679-2681** (§4.8), **2690-2691** (§4.8), **2807-2812** (§4.9). Byte-exact,
unique, non-overlapping, and all inside §4 — so Placement's "two in §4.8, one in
§4.9 part 1" is accurate: §4.9's numbered part 1 opens at 2779 and 2807 sits
inside it. One section this run, so no `placement-collision`.

**Fact-block §5, against all three NEWs.**

- §5.1 — *vendored* does not read as split. The 2026-08-06 ruling at 2803-2805
  and "**The word is not split**" at 2812-2813 lie outside every OLD boundary,
  and Pair 1 says in terms that it states "the extent of the data-side payload
  and not the meaning of *vendored*, which §4.9 states once for both
  mechanisms" — which matches the master's own "this is the single statement of
  both" at 2803-2804. Pair 3's "all three data kinds sit outside it" replaces
  "the CSVs sit outside it" without touching the mechanism distinction or the
  `main()` reason.
- §5.2 — neither non-table becomes a §4.8 table: "**Only the three tables are
  §4.8 tables.**", "Neither is imported into any `UDataTable`, and `T-DATA-05`
  asserts over the tables alone — being carried makes neither a table." Pair 3
  calls them payload throughout.
- §5.3 — the gate is not narrowed: "all five files, all three kinds", with the
  manifest's exemption kept and given its stated reason, whose §4.9 locator
  resolves (`StratRules.manifest.json` "has **no counterpart to be vendored
  from**", 2794-2797).
- §5.4 — every finite claim is pinned: the `files` map at `4ceaf93`, the
  interval bounded by `862a225` and `c2f5860`, the join dated 2026-08-07 and
  pinned at `5c47cc1`.
- §5.5 — no count without its kinds; both counts share a sentence in Pair 1 and
  a clause in Pair 3.

**Fact-block §3.3 is not promoted from inference to measurement.** Pair 2 states
the measurements as measurements ("Exactly one data-touching crew commit falls
between those two vendorings — `c2f5860` — and it changed exactly one file",
fact §3.1-§3.2) and the inference as inference ("A vendored file changed, so
`dataCommit` advanced; had none changed, it would have stayed where it was …
would be a counterexample"). Nothing reads as measured that was reasoned.

**Nothing moves for `T-DATA-05`, row 2's acceptance set, or Q34.** `T-DATA-05`'s
subject (§4.8 parity-gate sentence, 2695-2696), row 2's acceptance set and Q34's
ruling (2667, §4.7) all lie outside the three OLD spans. Pair 1 restates
`T-DATA-05`'s subject in terms without moving the invariant. No acceptance ID is
minted, widened or re-dated — `GATE-DATA-VENDOR` mints none (2681), and Pair 1
preserves that clause verbatim.

**Two locator claims in the table, verified rather than accepted.**
`strat::loadScenario` on the shipped scenario asset sits in §4.9 part 2's
**Load** bullet, lines **2914-2916**. §4.10 (3066-3182) contains **zero**
occurrences of `vendor` in any case, so "it says nothing about vendoring" holds.

**Format and kb.** All five required headings present: Placement (l.3), Draft
(l.9), Change requests (l.126, "None."), Open questions for the Director
(l.130), Grounding (l.150). Open questions still files the standing convention
question and adds no new rule gap. `source/kb_rules.md` returns **0** matches
for `vendor`, `dataCommit`, `StratData`, `parity` and `manifest`
case-insensitively, so no `kb-desync` arises. Grounding was checked bullet by
bullet against the draft; every substantive number, date, commit and mechanism
traces to `source/FACTS_vendor-scope.md` §2.1-§2.5 or §3.1-§3.2, or to a
`source/gdd.md` location measured above, including the new bullet for the two §3
sentences.

---

## Verdict

**PASS.** The cut did what a narrowing could not: both falsified universals are
gone as text and as meaning, no surviving sentence inherited either quantifier,
and the apparatus that remains is a disposition table plus a one-line record of
what was removed. The two dispositions the last run required were added with
quotes that are byte-exact against §3's status line at 1516, and both are
correctly ruled **Left alone** as corroborating rather than moving — the
fixture's vendoring at `4ceaf93` and `GATE-DATA-VENDOR` FAILing on a forged
fixture are exactly the sentences a five-file extent makes coherent. I swept the
master independently for every site of `vendored bytes`, `sync_stratdata.py` and
`dataCommit` and found no sentence whose truth moves that the table omits, so
the completeness claim the table's heading makes now holds. The three pairs are
byte-exact, unique, non-overlapping and unchanged; no acceptance ID, no
disposition verdict and no pinned record moves. Nothing must happen before
merge: the Director may merge `sections/tech_vendor-scope.md` at the three
placements it specifies, and should on merge re-sync `kb/rules.md` as a matter
of course even though this round's content is absent from it.
