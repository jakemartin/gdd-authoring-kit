> # ✅ APPLIED ADDENDUM — DO NOT RE-APPLY
>
> Every replacement pair in this file **has been applied to the master GDD**.
> Verified 2026-08-10 against `source/gdd.md` md5 `1f27e981b623c7af2f6402d9a5b6a62b`
> (3365 lines), matched newline-insensitively: each pair's old text is either
> absent from the master, or present only inside the new text that replaced it —
> the pairs that extend a sentence rather than swap it. No pair is outstanding.
>
> No pair count is stated here deliberately: this file's line-initial markers do
> not reconcile with its own pair headings, because narrative prose that begins a
> line with the word *old* parses as a marker. The verified claim is the one
> above, which is per-pair and needs no total.
>
> Its quoted "current" text, register extents and open items are a **snapshot of
> the moment it was written**, not the state of the document.
>
> **The master GDD is the source of truth** — read `source/gdd.md`. Further changes
> to a merged section go in a *new* addendum file.

# Technical design — rulings AO and AP (tech-director)

## Placement

Addendum of exact OLD → NEW pairs against `source/gdd.md` at md5
`18555ea139cc70d8026957c4b3b5ef14`. Sites are in §4.7's register (Q34) and
§4.9 part 1, with one pointer in §4.8. No section is redrafted, and the
merged `t-data-05-harness` addendum is not touched.

---

## Pairs

### §4.7 — Q34's register row

**Pair 1**

OLD

```
**That rules which IDs re-open and nothing about what this ledger shows in the interval** between the edit and the re-run; the pinned record is untouched either way, since *green at `b1ea992` over the UE tree at `fed8ae9`* stays true of those commits, which is what pinning is for.
```

NEW

```
**What this ledger shows between a §4.8 CSV edit and the re-run that closes the new pair is ruled with it (2026-08-06): across that interval row 2 keeps its live ✓.** §3 makes a row verified when it cites the commit and passing test IDs that back it; row 2's cell cites [`b1ea992`](https://github.com/jakemartin/stratocracy-crew/commit/b1ea992) and `fed8ae9`, and a CSV edit falsifies neither citation, so the ✓ is a claim about named evidence and not about the current working tree — the pinned record is untouched either way, since *green at `b1ea992` over the UE tree at `fed8ae9`* stays true of those commits, which is what pinning is for. **The display cannot mislead in silence**, because the gates refuse loudly for as long as that interval lasts: an edited CSV FAILs `GATE-DATA-VENDOR` on a hash mismatch and the parity check on a value, both measured (§3).
```

*Note.* Ruling AO. The OLD carries the document's only occurrence of *interval*
and the only phrase that defines it, so the NEW names the span in full at first
use — between a §4.8 CSV edit and the re-run that closes the new pair — and
refers back to it twice after that. The disclaimer is replaced rather than
qualified, because it is the sentence the ruling exists to falsify; the half of
it that survives the ruling, the pinned record standing either way, is kept
verbatim, because it is what the ruling rests on. The ✓ is grounded on §3's own
verification rule rather than on a new one, so no rule is minted here.

### §4.9 — part 1, module layout

**Pair 2**

OLD

```
fixtures, not shippable code.
```

NEW

```
fixtures, not shippable code. **One word, two mechanisms, and this is the single
statement of both (ruled 2026-08-06).** *Vendored* means the same thing in each:
bytes copied out of a named commit's object store into the UE project, and gated
for identity. What differs is which bytes, by which script,
under which gate — the crew's C++ sources into `Source/StratRules/` by
`sync_stratrules.py` under `T-INT-01`, and the §4.8 CSVs into the UE project's
data directory by `sync_stratdata.py` under `GATE-DATA-VENDOR`. The sentence
above is about the first, and its quantifier is scoped by its own stated reason:
a UBT module cannot hold a second `main()`, which is a constraint on C++ sources,
so the CSVs sit outside it by construction rather than by exception. **The word
is not split, and the reason is that the artifact does not split it:**
`sync_stratdata.py`, its manifest note and its crew commit message all say
*vendor*, so a rename confined to this document would diverge the document from
the thing it describes.
```

*Note.* Ruling AP, stated once and placed at the sentence most open to being
read as covering both mechanisms. "Nothing else is vendored" is reproduced
untouched and takes no repair — it is true as written, and this passage says why
rather than narrowing it.

### §4.8 — data contract

**Pair 3**

OLD

```
and the editor imports the
vendored copy into a `UDataTable` whose row struct derives `FTableRowBase`.
```

NEW

```
and the editor imports the
vendored copy into a `UDataTable` whose row struct derives `FTableRowBase`. That
copy is made by `sync_stratdata.py`, the CSV counterpart of the script that
vendors the C++ sources; *vendored* covers both, and the two mechanisms are
distinguished once at §4.9.
```

*Note.* The citation half of Ruling AP: the other place the word appears for
these bytes gets a pointer and not a second copy of the distinction. It also
names the script, which this section did not.

---

## Check results

- **No count moves, so this addendum carries no arithmetic.** Neither ruling
  mints an acceptance ID, and neither adds a register row: AO completes the
  ruling already filed inside Q34's row, and AP is prose in §4.9. §4.7's
  register stands at 34 rows, 17 ruled and 17 open; §4.5 stands at 71 written,
  62 green and 9 unclosed; §3 stands at ten ✓ rows, two rows carrying evidence
  without one, and seven uncovered IDs. AO keeps row 2's ✓, so it moves none of
  those figures either.
- **OLD strings:** each OLD above was matched against `source/gdd.md` at
  `18555ea1` and returned exactly one match.
- **Pair inventory:** **3** pairs, numbered 1–3, no gap and no duplicate. **2**
  are insertions whose OLD survives verbatim inside their NEW — pairs 2 and 3.
  Pair 1 replaces its OLD and is not one.
- **Dependant-sentence sweep, at the widened reach**, run per pair and including
  enumerations keyed on set membership at any distance.
  - *AO.* The only site in the master that treats the interval as unsettled is
    the clause pair 1 replaces; the other occurrences of *re-open* — §4.4's wk-2
    cell and §4.11 row 9's cell, both about a gate re-opening when a command set
    widens, and §3's *re-opened by each system that lands after it* about the
    week-1 debug-command goal — are a different event and are untouched.
    Membership: AO keeps row 2 in the ✓ set, so §3's *Ten rows carry a ✓*, §3's
    *two more carry evidence without one*, §4.5's *10 verified ledger rows* and
    §4.11's flipped-row list all stand unmoved, which is the outcome that needed
    no edit rather than one I made. No Q row exists for the interval question —
    it was carried in the addendum's own Open questions, not registered — so the
    register's extent sentences and its 34 / 17 / 17 counts are untouched.
  - *AP.* Sites where *vendored* or *unvendored* appears and the quantifier could
    be read across both mechanisms: §4.9's enumeration of what
    `Source/StratRules/` holds, which lists ten crew modules plus
    `StratRules.Build.cs` and `StratRules.manifest.json`; §4.9's *the set is
    declared, not inferred* and its partition requirement over crew modules;
    §4.9's and §3's *`Save`, `Replay` and `Balance` remain unvendored* and
    *ruled out of vendoring until a bridge consumer exists*; §4.4's and §4.11's
    *vendored replayer*; and `T-INT-01`'s *every file in `Source/StratRules/`*.
    Every one of them is about crew C++ modules or that directory, which is the
    first mechanism, and pair 2 states that scope explicitly, so each holds as
    written and none takes a pair.
  - *Over the open question.* It binds no pair and moves no count, so nothing in
    the master depends on it.
  - *Found and filed:* nothing beyond the three pairs.

---

## Change requests

None. The two the merged addendum filed are answered and closed: §4.9's
*Nothing else is vendored* holds as written, its quantifier being scoped by its
own stated reason (pair 2 records that scope where the ambiguity was, and
repairs nothing); and §4.9's stub `Inputs` line holds as written, because the
tables are imported in-editor and that is what the line names, while where the
bytes travelled is the vendoring mechanism's business and is gated separately.
Neither gets a pair.

---

## Open questions for the Director

1. **Should the CSV mechanism carry a source-identity invariant of its own?**
   `T-INT-01`'s text ends: *"Recomputation is not the weaker of the two: it is
   the strongest check available on a file whose bytes no stored blob can
   predict. Neither mechanism may take its expectation from the vendored tree or
   from the vendoring script — the ledger's evidence chain survives vendoring"*.
   **"Mechanism" there is fixed by "the two" in the sentence before it**: the two
   identity mechanisms that invariant has just named — hash-match against a
   tracked counterpart, and recomputation from tracked inputs — both of which sit
   inside the check. So the invariant binds no script. The check-versus-script
   independence is a separate and weaker §4.9 prose sentence, and it is about the
   declared set rather than about the bytes: *"both `sync_stratrules.py` and
   `T-INT-01`'s check read that declaration from the git object store at the
   commit in question, so neither takes its expectation from the other."*

   For the CSVs, §4.8 states that *"`GATE-DATA-VENDOR` asserts that the vendored
   bytes are the recorded ones"* and that *"the UE project cannot see the crew
   repo at test time"*. `GATE-DATA-VENDOR` carries no invariant text in this
   document, and the six invariants of the `T-DATA` set are about loaded values,
   row counts, sanity, the editor parity pass and the effectiveness table, so no
   counterpart to either sentence above is stated for that mechanism. What
   follows is a difference in **where the identity check runs** — crew-side
   against the git object store for the sources, in-editor against a record for
   the CSVs — which Ruling AP's one word neither creates nor removes, and which
   is the thing a reader may now assume away.

   Three answers, derived from that: **(i)** leave it — the recorded hashes plus
   the loud failure Ruling AO relies on are what the CSV mechanism offers, and
   these are data rather than the shipped rules module; **(ii)** mint a crew-side
   CSV identity check, the analogue of `T-INT-01`, asserting the vendored bytes
   against `dataCommit`'s blobs where the crew repo *is* visible — which mints an
   acceptance ID and moves §4.5's written count, and is the only one of the three
   that does; **(iii)** extend the §4.9 prose discipline to the CSV manifest
   without minting an ID, so that the record and whatever writes it are not the
   same authority. I have no measurement of how `GATE-DATA-VENDOR` derives its
   expectation, so I state none — the question is what this document should
   require, not what the gate currently does.

---

## Grounding

- §3's verification rule that Ruling AO rests on — the ledger's *each Verified
  row citing the commit and passing test IDs that back it*, and row 2's evidence
  cell, which names `b1ea992` and `fed8ae9`.
- The measured behaviour in the interval — §3's landing record of the six
  known-bad inputs, whose first is the perturbed CSV value that failed the
  parity check on value and `GATE-DATA-VENDOR` on hash.
- Q34's row, which already carries the repo-pair rule and the
  which-IDs-re-open half beside it — §4.7's register.
- The first vendoring mechanism, its script, its manifest field and its gate —
  §4.9 part 1, including *Nothing else is vendored* with its own stated reason,
  the declared-not-inferred ruling of 2026-08-05 and its prose sentence about
  the declaration, and `T-INT-01`'s invariant text, whose *Neither mechanism*
  clause binds the two identity mechanisms the same invariant has just named.
- The second mechanism, its manifest, its `dataCommit` field and its gate —
  §4.8's principle paragraph as merged, and the `T-DATA` invariant block.
- **Ruling AP's stated reason, which merges inside pair 2, is measured outside
  this document:** that `sync_stratdata.py`, its manifest note and its crew
  commit message all say *vendor* is measured in the **crew repo at
  [`c2edae0`](https://github.com/jakemartin/stratocracy-crew/commit/c2edae0)**
  and is supplied as measured in this round's fact block; `sync_stratdata.py` is
  introduced to this document by pair 3.
- The precedent for stating a thing once and citing it from the sites that would
  otherwise restate it — §4.9's own *stated once here and cited elsewhere*,
  which is what that section does for what the editor pass denotes, and which is
  the practice pairs 2 and 3 follow.
- The precedent against a document-only rename — §4.9's record that a name
  change would have to reconcile with commit-pinned §3 records, which is why
  that rename is deferred to its own round.
- Snapshot: `source/MANIFEST.txt`, `gdd.md` md5
  `18555ea139cc70d8026957c4b3b5ef14`.
