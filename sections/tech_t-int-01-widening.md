# T-INT-01 widening: GDD addendum (tech-director)

Exact OLD/NEW pairs against `source/gdd.md` (MANIFEST md5 `0121ee5b`). Every OLD
was searched in the master before the pair was written.

---

### Pair 1 — §3 ledger status line: where the draft stands

**OLD**

```
This draft stands at 2026-08-04, at commit [`b23823f`](https://github.com/jakemartin/stratocracy-crew/commit/b23823f) in the crew repo, whose parent is [`e06c44b`](https://github.com/jakemartin/stratocracy-crew/commit/e06c44b) and whose grandparent is [`41a1452`](https://github.com/jakemartin/stratocracy-crew/commit/41a1452), and at `99fcb84` in the Stratocracy UE project repo, the first commit in that repo since its Git LFS migration.
```

**NEW:**

```
This draft stands at 2026-08-04, at commit [`d837fc8`](https://github.com/jakemartin/stratocracy-crew/commit/d837fc8) in the crew repo and at `9dec48c` in the Stratocracy UE project repo, each verified with `git ls-remote` to be the head of its own repo's default branch — `main` in the crew repo, `master` in the UE project — with both working trees clean. The landing this ledger records before them is [`b23823f`](https://github.com/jakemartin/stratocracy-crew/commit/b23823f) in the crew repo, whose parent is [`e06c44b`](https://github.com/jakemartin/stratocracy-crew/commit/e06c44b) and whose grandparent is [`41a1452`](https://github.com/jakemartin/stratocracy-crew/commit/41a1452), with the UE project's half at `99fcb84`, the first commit in that repo since its Git LFS migration.
```

Moves the anchor to the two heads measured this session, and keeps the prior
landing's chain rather than asserting an ancestry no command established.

---

### Pair 2 — §3 ledger paragraph: the filed question is now ruled

**OLD**

```
Whether the ledger should gain the row is filed for the Director.
```

**NEW:**

```
Whether the ledger should gain the row was filed for the Director and has since been ruled, at the end of this paragraph.
```

Stops the paragraph carrying an open filing that the same paragraph now answers.

---

### Pair 3 — §3 reachability parenthetical: a second UE-project citation

**OLD**

```
**One cited commit is in a different repository**: `99fcb84` is not an object in the crew repo at all, and is reachable from the head of `master` in the **Stratocracy** UE project repo, whose tree it pins. That is the first citation this ledger makes outside the crew repo, and
```

**NEW:**

```
**Not every cited commit is an object in the crew repo**: `99fcb84` and `9dec48c` are not objects in it at all, and each is reachable from the head of `master` in the **Stratocracy** UE project repo, whose tree it pins. `99fcb84` was the first citation this ledger made outside the crew repo, and
```

The singular was true only while one UE-project commit was cited. Rewritten so a
further citation into that repo does not stale it again.

---

### Pair 4 — §3 ledger paragraph: the record of the widening (Rulings 1, 2 and 3)

**OLD**

```
**How `e06c44b` and `b23823f` were authored is deliberately not stated:** no harness claim is made for either, because none was established.*
```

**NEW:**

```
**How `e06c44b` and `b23823f` were authored is deliberately not stated:** no harness claim is made for either, because none was established. **`T-INT-01`'s running check was then widened**, at [`d837fc8`](https://github.com/jakemartin/stratocracy-crew/commit/d837fc8) in the crew repo with the UE project repo at `9dec48c`. Its PASS line reads, verbatim: *T-INT-01 source identity: all 22 files in Source/StratRules/ are accounted for at d837fc8 — 20 sources and StratRules.Build.cs hash-match tracked blobs, and StratRules.manifest.json recomputes byte-for-byte*. **Nothing in that directory is exempt from it**, and what it must satisfy is stated in §4.9's invariant text, amended with it. **Two files became tracked in the crew repo to make that possible** — `ue_module/StratRules.Build.cs` and `ue_module/manifest_fields.json`. `StratRules.Build.cs` was previously a string literal inside `sync_stratrules.py` and is now vendored from the git object store exactly as the sources are, so it has a counterpart to be matched against where it had none. **The check reads both of those from the git object store and imports nothing from the vendor script**, because a check that called the generator's own constant would assert nothing about the generator. **The widening was shown to be a widening rather than asserted as one:** the **pre-change** check was run against each new known-bad input first, and each passed it **undetected** — a comment appended to `StratRules.Build.cs`, the manifest's `note` altered, and the manifest's `generator` altered — while the post-change check FAILs all three. An extra `Sneaky.good.cpp` was run beside them as a **control** and FAILs both before and after, which is what makes those three results a widening rather than a changed disposition. **Two further controls behaved as designed:** editing `ue_module/StratRules.Build.cs` in the **working tree** moves no verdict, because the check reads the blob at the recorded commit; and tampering a vendored source *together with* its recorded hash in the manifest still FAILs. **`T-INT-01`'s green re-dates to this commit**, over the vendored tree at `9dec48c`, and is recorded here rather than left at `b23823f`: `ue_module/manifest_fields.json` did not exist at `b23823f`, so the amended text cannot have been satisfied there, and an ID whose written text widens closes at the commit at which the widened text is met. **`T-INT-04` is unaffected** — its text did not change, it is green at `b23823f` and green again here. **No acceptance ID was minted here** — the amendment widened an ID that already existed — so §4.5's written-ID count does not move at this landing, its green count moves **54 → 55** and its unclosed count moves **17 → 16**, which is the second half of the movement whose first half the `b23823f` landing above records. **The whole crew gate is green at `d837fc8` under clang++** — row 1 7/7, row 2 6/6, row 3 6/6, row 4 9/9, row 5 11/11, row 6 7/7, row 7 12/12, row 8 34/34, the debug driver 12/12 and the integration gate 2/2 — the same figures already recorded above, and **no rules code changed**: `cpp_reference/` is byte-identical between `b23823f` and `d837fc8`, `git diff --stat` over that path printing nothing. `spec/integration_spec.md` was updated at `d837fc8` to describe the widened check, having described the old one. `T-INT-02`, `T-INT-03` and `T-INT-05` **still did not run** — no in-editor Automation harness exists — so **build-order row 9's acceptance set still does not close**, on the Q29 reading applied per acceptance ID as well as per row; the vendored module is **still not registered** in `Stratocracy.uproject`, and **no UBT build has been run**. **The ledger table below deliberately gains no row for build-order row 9, and no row is added, removed or flipped by this landing.** That is the ruling on the question filed above, and it turns on what a row would claim: what has landed is the vendoring step and its identity check, while the bridge §4.9 part 2 describes is unbuilt, so a row written now would either name a system that half-exists or start a practice of one row per half. The row is deferred until the bridge is built, so the ledger later gains a row describing a whole system. **The text-versus-check question this landing settled is registered as Q33** (§4.7), written already marked RULED. **How `d837fc8` was authored is deliberately not stated:** no harness claim is made for it, because none was established.*
```

The record of the widening, in the shape rows 4–9 use, and the single home for
Ruling 2's deferral. It states the run, the controls and the re-dating; §4.9
owns what the vendored set is and what the invariant requires. Its per-landing
figures are the second half of the movement Pair 17 splits.

---

### Pair 5 — §4.9 part 1: which commits the existing module is pinned to

**OLD**

```
**That module now exists**, at
`99fcb84` in the UE project repo against `rulesCommit`
[`b23823f`](https://github.com/jakemartin/stratocracy-crew/commit/b23823f)
(§3):
```

**NEW:**

```
**That module now exists**, at
`9dec48c` in the UE project repo against `rulesCommit`
[`d837fc8`](https://github.com/jakemartin/stratocracy-crew/commit/d837fc8)
(§3):
```

A present-tense claim about which tree exists and which commit it answers to.
The tree moved when the module was re-vendored, so both commits move with it;
§3 keeps the earlier pair as the landing it was.

---

### Pair 6 — §4.9 part 1: which vendored file has a counterpart and which cannot

**OLD**

```
beside two UE-owned files that have
no counterpart in the crew repo — `StratRules.Build.cs` and the manifest.
```

**NEW:**

```
beside `StratRules.Build.cs`, which is
vendored from `ue_module/StratRules.Build.cs` in the crew repo on the same
terms as the sources, and `StratRules.manifest.json`, which the sync script
generates and which has **no counterpart to be vendored from**: it records
`rulesCommit`, and a file's bytes cannot contain the identity of the tree that
holds them. `T-INT-01` states what each of those two states requires.
```

`StratRules.Build.cs` now has a counterpart, so the sentence's shared predicate
is false of it. Splits the two files by the property that decides which
mechanism reaches them, and leaves the requirement itself to the invariant.

---

### Pair 7 — §4.9 spec stub: T-INT-01's invariant text (Ruling 1)

**OLD**

```
  T-INT-01  source identity: every file in Source/StratRules/ hash-matches the
            recorded crew commit — the ledger's evidence chain survives vendoring
```

**NEW:**

```
  T-INT-01  source identity: every file in Source/StratRules/ is accounted for
            against the recorded crew commit, and none is unaccounted for. A
            file that has a tracked counterpart at that commit must hash-match
            it. A file for which no such counterpart can exist must instead be
            recomputed from tracked inputs at that commit and equal the
            vendored bytes exactly. Recomputation is not the weaker of the two:
            it is the strongest check available on a file whose bytes no stored
            blob can predict. Neither mechanism may take its expectation from
            the vendored tree or from the vendoring script — the ledger's
            evidence chain survives vendoring
```

The old text stated a requirement no file set could satisfy and no check ever
ran. The new text states what must hold: total coverage, two mechanisms
partitioned by a property rather than by a list of named files, and an
independent expectation for both. A file changing category — as
`StratRules.Build.cs` did this round — moves no word of it.

---

### Pair 8 — §4.7 register provenance chain: Q33's origin

**OLD**

```
three §2.13.1 validation checks row 7 found gated under no `T-SCN-` ID (Q32)
— so that each question
```

**NEW:**

```
three §2.13.1 validation checks row 7 found gated under no `T-SCN-` ID (Q32),
and the disagreement between an invariant's written text and the check that
runs it, found while widening build-order row 9's integration check (Q33)
— so that each question
```

The chain is the register's provenance record and names every row's origin.

---

### Pair 9 — §4.7 register: the ruled/open figures

**OLD**

```
**Fifteen of the thirty-two rows are ruled; the other
seventeen remain open but *readable*** — Q1, Q2, Q3, Q10–Q19, Q29, Q30, Q31
and the newly registered Q32 — each
```

**NEW:**

```
**Sixteen of the thirty-three rows are ruled; the other
seventeen remain open but *readable*** — Q1, Q2, Q3, Q10–Q19, Q29, Q30, Q31
and Q32 — each
```

Derivation in the arithmetic section. Q32 is no longer the newly registered row,
so the epithet moves off it rather than to Q33, which is ruled.

---

### Pair 10 — §4.7 register: Q33, registered already ruled (Ruling 3)

**OLD**

```
so the bullet describes more than the suite gates. |
```

**NEW:**

```
so the bullet describes more than the suite gates. |
| **Q33** | ~~An invariant whose written text and running check disagree.~~ **RULED (this revision), and registered already ruled.** `T-INT-01` required every file in `Source/StratRules/` to hash-match the recorded crew commit. Two vendored files had no counterpart at that commit to match, so the text was unsatisfiable as written, and the check shipped at [`b23823f`](https://github.com/jakemartin/stratocracy-crew/commit/b23823f) did not reach them — measured rather than assumed: a comment appended to `StratRules.Build.cs`, the manifest's `note` altered and its `generator` altered each passed that check undetected (§3). Narrow the text to describe the check that runs, or widen the check until the text is satisfiable and then amend the text to what was actually met? | `T-INT-01`'s invariant text (§4.9), and the commit its green is credited to. No gate waits on the ruling: `T-INT-01` runs on every gate run under either answer, and neither answer mints an acceptance ID. | **Ruled: widen the check, and never narrow the text.** The widened check accounts for every file in that directory and exempts none; it landed at [`d837fc8`](https://github.com/jakemartin/stratocracy-crew/commit/d837fc8) with the UE project repo at `9dec48c` (§3), and §4.9's invariant text is amended to state what must hold rather than to describe an implementation. **It mints no acceptance ID:** the amendment widens the coverage of an ID that already exists rather than adding an assertion the suite did not carry, so no §4.5 total moves on its account — what moves is the commit `T-INT-01`'s green is credited to, since an ID whose text widens closes where the widened text is met (§4.5, §4.11). The general rule the row settles: **where an invariant's text and its running check disagree, the check moves first and the text is then amended to the requirement that was actually met** — a text edited down to what the code happens to do asserts nothing the code could fail, which is the failure this ledger exists to prevent. It is registered already marked RULED because the Director ruled it in the session that found it; the register carries it so the amendment above has a stated cause rather than an unexplained rewrite. |
```

The register row for Ruling 1's question, appended after Q32. Its OLD is the
final cell of the Q32 row.

---

### Pair 11 — §4.7 register: Q33 enters ruled, not open

**OLD**

```
The convention is unchanged: **where a row states no
reading, its gate stays blocked until the Director answers.**
```

**NEW:**

```
**Q33 is registered already marked RULED**, so it enters the ruled side and
the open list above is unchanged. The convention is unchanged: **where a row
states no reading, its gate stays blocked until the Director answers.**
```

States the disposition that makes Pair 9's arithmetic legible without repeating
a figure.

---

### Pair 12 — §4.4 week-2 cell: which commit each of the two IDs is green at

**OLD**

```
**T-INT-01/04 are green at `b23823f`** (§3), ahead of this cell rather than behind it, since neither runs on a command log or needs a rules row, and the vendoring they assert over has landed.
```

**NEW:**

```
**T-INT-04 is green at `b23823f`** and **T-INT-01 at [`d837fc8`](https://github.com/jakemartin/stratocracy-crew/commit/d837fc8)**, over the vendored tree at `9dec48c` (§3), both ahead of this cell rather than behind it, since neither runs on a command log or needs a rules row, and the vendoring they assert over has landed.
```

Present tense, so the joint credit to `b23823f` is false on merge. The two IDs
part company here and are named separately from this point on.

---

### Pair 13 — §4.5 risk cell: the green-by-commit breakdown

**OLD**

```
and **2** at [`b23823f`](https://github.com/jakemartin/stratocracy-crew/commit/b23823f), where T-INT-01 and T-INT-04 closed over the vendored tree at `99fcb84` without closing row 9's acceptance set
```

**NEW:**

```
and **1** at [`b23823f`](https://github.com/jakemartin/stratocracy-crew/commit/b23823f), where T-INT-04 closed over the vendored tree at `99fcb84` without closing row 9's acceptance set, and **1** at [`d837fc8`](https://github.com/jakemartin/stratocracy-crew/commit/d837fc8), where the widened T-INT-01 closed over the vendored tree at `9dec48c` without closing it either — an ID whose written text widens closes at the commit at which the widened text is met, and T-INT-04's text did not change (§3)
```

Re-attribution, not a movement: the entry splits, the breakdown still sums to
the same green total, and the arithmetic section carries the sum.

---

### Pair 14 — §4.5 risk cell: the unclosed enumeration's row-9 clause

**OLD**

```
its other two having closed at `b23823f` (§3);
```

**NEW:**

```
its other two having closed — T-INT-04 at `b23823f`, and T-INT-01 at `d837fc8` on the widening of its own text (§3);
```

The same cell's second credit to `b23823f`, which would otherwise disagree with
the breakdown three sentences above it.

---

### Pair 15 — §4.11 lead prose: row 9's headless half

**OLD**

```
**Row 9's headless half has since landed**, at `b23823f`
in the crew repo with the vendored tree at `99fcb84` in the UE project
repo: `T-INT-01` and `T-INT-04` are green there, under clang++, which is
what this row's cell means by closing as soon as vendoring lands.
```

**NEW:**

```
**Row 9's headless half has since landed**, at `b23823f`
in the crew repo with the vendored tree at `99fcb84` in the UE project
repo: `T-INT-04` is green there, under clang++, which is
what this row's cell means by closing as soon as vendoring lands.
**`T-INT-01` is green at `d837fc8`**, over the vendored tree at `9dec48c`,
and not at the earlier landing: its written text was widened there, over an
input that did not exist before it, so the widened text is first met at that
commit (§3). The landing stands as the landing it was; what moves is where
the widened ID closes — the treatment row 5 already has, whose
`T-TURN-01..10` closes at its rebuild while `T-TURN-01..09` first closed at
`ad77b13`.
```

The one place the re-dating rule is stated in full, beside the precedent §4.11
already carries two sentences away.

---

### Pair 16 — §4.11 row-9 cell: what closed as soon as vendoring landed

**OLD**

```
and close as soon as vendoring lands, which they did at `b23823f` over the vendored tree at `99fcb84` (§3).
```

**NEW:**

```
and close as soon as vendoring lands, which `T-INT-04` did at `b23823f` over the vendored tree at `99fcb84`, and `T-INT-01` at `d837fc8` over the vendored tree at `9dec48c` (§3).
```

Two things went false in one clause: the joint closure, and `99fcb84` as the
vendored tree the cell's own condition is satisfied over.

---

### Pair 17 — §3 `b23823f` landing record: its per-landing figures

**OLD**

```
its green count moves 53 → 55 and its unclosed count moves 18 → 16
```

**NEW:**

```
its green count moves 53 → 54 and its unclosed count moves 18 → 17
```

One closure is credited at this landing, so its per-landing figures move by one.
The other half is carried by the `d837fc8` record in Pair 4, on the per-landing
convention every other landing sentence in §3 follows.

---

## Arithmetic

The register gains one numbered row, ruled at registration. Nothing else moves:
no acceptance ID is minted, none closes for the first time, and no ledger row is
added, removed or flipped.

| Quantity | Site | Before | Movement | After |
|---|---|---|---|---|
| Numbered register rows | §4.7 register table | 32 | + Q33 | 33 |
| Ruled rows | §4.7 (Pair 9) | 15 | + Q33 | 16 |
| Open rows | §4.7 (Pair 9) | 17 | none | 17 |
| Written acceptance IDs | §4.5 risk cell | 71 | none minted | 71 |
| Green | §4.5 risk cell | 55 | none closed, one re-credited | 55 |
| Unclosed | §4.5 risk cell | 16 | none | 16 |
| Verified ledger rows | §3 table | 9 | no row added, no flip | 9 |

Existing register rows are Q1..Q32 contiguous, so the new row is Q33.
Ruled + open = 16 + 17 = 33. Complement check on §4.5: 71 − 55 = 16, unmoved,
so no §4.5 total is owed a pair.

**Re-credit, not a movement.** `T-INT-01`'s green moves from `b23823f` to
`d837fc8` because its written text widened there; `T-INT-04`'s text did not
change and its green stays at `b23823f`. Pair 13 therefore splits the entry
**2** at `b23823f` into **1** at `b23823f` and **1** at `d837fc8`, and the
breakdown still sums to the green total above:
18 + 9 + 9 + 6 + 7 + 1 + 2 + 1 + 1 + 1 = 55. The §3 per-landing figures split
with it — green 53 → 54 and unclosed 18 → 17 at `b23823f` (Pair 17), green
54 → 55 and unclosed 17 → 16 at `d837fc8` (Pair 4) — reaching the same totals
by the same two steps.

---

## Check results

- Every OLD returns exactly one occurrence in `source/gdd.md`. Pairs 5, 6, 7, 8,
  9, 11 and 15 were matched across their line breaks; Pair 6's OLD begins
  mid-line.
- Both insertions were checked against the text abutting the seam on each side.
  Pair 4 inserts before the ledger paragraph's closing `*` and the `Legend:`
  sentence that follows it, neither of which carries a demonstrative, and its
  own first sentence names `d837fc8` outright. Pair 10 inserts a whole table row
  between the Q32 row and the blank line that ends the register table.
- Pairs 5 and 6 edit two clauses of one sentence and were checked as one edit:
  read together, the sentence names the tree that exists, the commit it answers
  to, and what each of its files is matched against. Pairs 13 and 14 edit two
  clauses of one §4.5 cell, and Pairs 4 and 17 the two halves of one movement
  inside one §3 paragraph; both were checked the same way.
- Pair 7 preserves the stub block's two-space ID indent and twelve-space
  continuation indent.
- The sweep was run mechanically over `99fcb84`, `9dec48c`, `b23823f`,
  `d837fc8`, `T-INT-01`, `T-INT-04`, `StratRules.Build.cs`, `manifest`,
  `rulesCommit` and the register's two extent-bearing sites. It put in scope
  every present-tense claim about the vendored tree, its commits or its file
  set, every sentence crediting `T-INT-01`'s green to a commit or counting a
  closure at one, every sentence quantifying over UE-project citations or over
  register rows, and the invariant text itself; each of those is a pair above,
  and what it left out states what a past landing did rather than what is now
  true.

---

## Change requests

| Existing § | Current text | Proposed change | Why |
|---|---|---|---|
| §4.9 part 1 | `via `sync_stratrules.py`, which reads each source from the git object store rather than the working tree — so identity is true by construction at the moment the script finishes` | Director to decide whether the by-construction clause should be scoped to the files the script copies, or dropped | `StratRules.manifest.json` is generated rather than copied, so identity of the vendored tree is no longer true by construction for every file in it; the manifest's correctness is established by the check's recomputation instead. Pair 6 states which file is generated and asserts nothing about the clause |
| §4.11 row 9 cell; §3 ledger table | `Presentation bridge & integration — §4.9 (proposed ledger row)` | Director to decide what the deferred row is called and what its acceptance set is when the bridge lands | Ruling 2 defers the row rather than declining it, so the deferral has a stated end condition and no name. Naming it now would be inventing the row this round declined to add |
| §4.9 part 2 | The bridge — load mapping, command surface, event list, actor and widget — is described and unbuilt | Director to decide whether the bridge is specified enough to be gated, or needs a stub pass first | `T-INT-02`, `T-INT-03` and `T-INT-05` cannot run until an in-editor Automation harness exists, and no build-order row owns creating one. That harness is currently the only route by which row 9's acceptance set can close |
| §4.7 head; §3 ledger | The document states no rule for what happens to a green ID when its invariant text widens | Director to decide whether Q33's re-dating consequence should be written as a general convention, or left as the sites this addendum re-credits | Q33 rules the text-versus-check question, and this addendum applies the re-dating to `T-INT-01` alone. Whether the next widened ID re-dates by rule or by another round of pairs is a convention decision rather than a technical one |

---

## Grounding

- Heads `d837fc8` (crew `main`) and `9dec48c` (UE project `master`), each
  verified with `git ls-remote` against its own repo, both trees clean.
- `99fcb84`'s reachability from that head, which Pair 3 asserts:
  `git merge-base --is-ancestor 99fcb84 HEAD` returns true in the UE project
  repo, and `git log --oneline` gives the chain `99fcb84` → `6f6dd58` →
  `9dec48c`, `9dec48c` being the head.
- The PASS line quoted in Pair 4, the two mechanisms, and the totality of the
  coverage: the `--integration` gate run at `d837fc8`.
- The three known-bad inputs, their pre-change results, their post-change
  results, the `Sneaky.good.cpp` control and the two further controls: the
  pre-change and post-change check runs over each input this session.
- New tracked files `ue_module/StratRules.Build.cs` and
  `ue_module/manifest_fields.json`, the prior string literal in
  `sync_stratrules.py`, the object-store read and the absence of any import from
  the vendor script: `d837fc8`.
- `T-INT-01`'s re-dated green: `ue_module/manifest_fields.json` is tracked at
  `d837fc8` and did not exist at `b23823f`, and the widened check was run green
  at `d837fc8` over the vendored tree at `9dec48c`. `T-INT-04`'s text is
  unchanged and it is green at both commits.
- The precedent Pair 15 names — a widened acceptance set closing at the commit
  that meets it while the earlier closure stays recorded as what it was:
  §4.11's own sentence on row 5's `T-TURN-01..10` against `T-TURN-01..09` at
  `ad77b13`.
- The per-landing convention Pairs 4 and 17 follow: §3's own landing sentences
  for rows 4–9, each of which moves the §4.5 figures by what closed at that
  commit.
- Whole-suite tallies at `d837fc8` under clang++, and `cpp_reference/`
  byte-identical between `b23823f` and `d837fc8` (`git diff --stat` prints
  nothing over that path): the crew gate run at `d837fc8`.
- `spec/integration_spec.md` updated at `d837fc8` to describe the widened check.
- `T-INT-02`, `T-INT-03`, `T-INT-05` not run, no in-editor Automation harness,
  module not registered in `Stratocracy.uproject`, no UBT build run: the same
  gate run, and the state of the UE project repo at `9dec48c`.
- The manifest's unmatchability: it records `rulesCommit`, which §4.10's file
  layout defines as the crew commit of the rules module that wrote the file.
- Rulings 1, 2 and 3 — widen the check rather than narrow the text; defer the
  ledger row until the bridge is built; register the question already ruled:
  Director rulings this session.
- Q29's per-acceptance-ID reading, which keeps row 9's set unclosed: §4.7's Q29
  row and §3's ledger paragraph.
- The register's two extent-bearing sites and the failure mode of pinned ranges:
  §4.7's register preamble, in its own words.
- Prior-round figures 71 / 55 / 16 and nine verified ledger rows: §4.5's risk
  cell and §3's table as they stand in `source/gdd.md`.
