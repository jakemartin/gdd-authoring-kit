# Row 9 — integration, headless half: GDD addendum (tech-director)

Exact OLD/NEW pairs against `source/gdd.md` (md5 `8db63b1a`). Every OLD was
searched in the master before the pair was written.

---

### Pair 1 — §3 ledger status line: where the draft stands

**OLD**

```
This draft stands at 2026-08-04, at commit [`41a1452`](https://github.com/jakemartin/stratocracy-crew/commit/41a1452) in the crew repo, whose parent is [`7c36303`](https://github.com/jakemartin/stratocracy-crew/commit/7c36303).
```

**NEW:**

```
This draft stands at 2026-08-04, at commit [`b23823f`](https://github.com/jakemartin/stratocracy-crew/commit/b23823f) in the crew repo, whose parent is [`e06c44b`](https://github.com/jakemartin/stratocracy-crew/commit/e06c44b) and whose grandparent is [`41a1452`](https://github.com/jakemartin/stratocracy-crew/commit/41a1452), and at `99fcb84` in the Stratocracy UE project repo, the first commit in that repo since its Git LFS migration.
```

Moves the anchor commit, and names the second repo the evidence chain spans.

---

### Pair 2 — §3 ledger paragraph: the record of the runner repair and row 9's headless half

**OLD**

```
rather than preserved in place from `7c36303`.*
```

**NEW:**

```
rather than preserved in place from `7c36303`. **The gate runner was then repaired**, at [`e06c44b`](https://github.com/jakemartin/stratocracy-crew/commit/e06c44b), whose parent is [`41a1452`](https://github.com/jakemartin/stratocracy-crew/commit/41a1452). Before it, `python run.py --week1` did not compile past §4.11 row 5: row 6 failed with `.\Driver.h:18:10: fatal error: 'Ui.h' file not found`, and rows 6, 7, 8 and the debug driver never ran. **The cause was in the runner and in no module:** [`7c36303`](https://github.com/jakemartin/stratocracy-crew/commit/7c36303) added `#include "Ui.h"` to `cpp_reference/Driver.h`, and the string `Ui` occurred **zero** times in `crew/tools.py`, so the runner's registry never gained `Ui.h`, `Ui.cpp` or `test_ui.cpp`; row 8's and `T-UI-05`'s gates had been run by ad-hoc compiles, so nothing exercised the runner after that commit. **The breakage was found by running the runner at `41a1452`** — it was not reported by anyone and was visible in no record, and it is recorded here rather than repaired quietly. **No module source, header, harness or invariant was touched by the repair**; it is registry and record text only. After it, from a clean tree under clang++, the whole suite ran — row 1 7/7, row 2 6/6, row 3 6/6, row 4 9/9, row 5 11/11, row 6 7/7, row 7 12/12, row 8 34/34, and the debug driver 12/12, with row 8's pass-1 fixture blocked at 21/34 on 13 FAIL lines over three distinct IDs — the same figures already recorded above, now produced by the runner rather than by hand. The three link lines the repair changed were also built and run under MSVC: row 8 34/34, row 6 7/7, and the driver 12/12. **No ledger row moves on a repair to the runner** and no acceptance ID closed here. **Build-order row 9's headless half then landed**, at [`b23823f`](https://github.com/jakemartin/stratocracy-crew/commit/b23823f), with the UE project's half at `99fcb84`. New in the crew repo: `sync_stratrules.py`, `spec/integration_spec.md`, `run_integration_gate_fn` in `crew/tools.py`, and `python run.py --integration`, which `--week1` now also runs at its end; the vendored module itself is described in §4.9. The gate is **`T-INT-01` and `T-INT-04`, 2/2 under clang++**, at `rulesCommit` `b23823f` over the vendored tree at `99fcb84`. `T-INT-02`, `T-INT-03` and `T-INT-05` **did not run** — no in-editor Automation harness exists, and the runner prints that sentence by name before its tally. **Row 9's acceptance set therefore does not close**, on the Q29 reading applied per acceptance ID as well as per row. It has no row in the table below to leave unflipped: §4.11 calls it a *proposed* ledger row, and this landing creates none, since what landed is the vendoring step and not the bridge §4.9 part 2 describes. Whether the ledger should gain the row is filed for the Director. **No acceptance ID was minted** — this row wrote no invariant text — so §4.5's written-ID count does not move at this landing, its green count moves 53 → 55 and its unclosed count moves 18 → 16. **Compiler detection was measured rather than assumed:** `g++` is not installed on this machine, `clang++` is found first, and `cl` is present but never reached. §4.9's `T-INT-04` states that any one of the four compiling clean satisfies it and that it does not require all four, so a single-compiler run is the invariant's own terms and not a shortfall against them. **The check was shown to fail before it was believed** — known-bad inputs, each restored afterwards: a comment appended to a vendored source (`T-INT-01` FAIL, `T-INT-04` PASS); the same edit **plus the manifest's own recorded hash updated to match it** (`T-INT-01` still FAIL); a vendored header deleted (`T-INT-01` FAIL and `T-INT-04` FAIL, because `Ai.good.cpp` genuinely stops compiling); an extra `Sneaky.good.cpp` added (`T-INT-01` FAIL, and `T-INT-04` compiled eleven files rather than ten); and `#include "CoreMinimal.h"` injected (`T-INT-04` FAIL and `T-INT-01` FAIL). **Two of those results exceeded the prediction made before running them** — the deleted header also broke `T-INT-04`, and the added file moved `T-INT-04`'s compile count — and both are the checks being right rather than the deliberate breaks being wrong. **The manifest-hash control is the one that matters:** the check does **not** trust the manifest's own hashes and does **not** import the vendor script's file list, taking only `rulesCommit` and re-deriving both the expected file set and every expected hash from the crew repo at that commit, so a manifest-versus-disk comparison would have passed that edit and this one does not. **When the UE project is absent the gate SKIPS with its reason stated and asserts nothing**; it does not pass, because a vacuous green `T-INT-01` beside a vendoring that never happened is the failure this ledger exists to prevent. The module was first vendored at `e06c44b` and re-vendored at `b23823f`; `cpp_reference/` is byte-identical between those two commits — `git diff --stat` over that path prints nothing — so only the manifest's `rulesCommit` line changed. **The `.gitattributes` rule is load-bearing rather than housekeeping:** the UE repo runs with `core.autocrlf=true` and that path carried no `text` attribute, so a fresh clone would have rewritten the vendored files to CRLF while the crew blob stayed LF, failing a byte-for-byte check on another machine; working-tree bytes, staged index blob and crew blob were verified to hash identically for every vendored file. **What this landing did not build is stated so it is not inferred.** The module is **defined** by `StratRules.Build.cs` and is **not wired into any build target** — `Stratocracy.uproject` does not list it, nothing depends on it, and **no UBT build was run** — the Director's decision this session, on the ground that registering it would claim an in-engine build this round cannot verify. **No bridge exists:** no load mapping, no command surface, no event list, no actor and no widget, so §4.9 part 2 is unbuilt. `T-INT-03`'s subject is §4.10's canonical state hash, which build-order row 10 has not built; the `stateHash` in `cpp_reference/Driver.h` remains the driver's own debug digest under `GATE-DRV-06` and is a different thing, as recorded above. **How `e06c44b` and `b23823f` were authored is deliberately not stated:** no harness claim is made for either, because none was established.*
```

The record of both commits, in the shape rows 4–8 use. It is the single home
for what was not built; §4.9 owns the vendoring step and §4.11 the build order.

---

### Pair 3 — §3 reachability parenthetical: the evidence chain now spans two repositories

**OLD**

```
Every commit this section **cites** — `d8284f1`, row 6's, included — is reachable from the head of `main` in the crew repo, so every commit link above resolves.
```

**NEW:**

```
Every **crew-repo** commit this section **cites** — `d8284f1`, row 6's, included — is reachable from the head of `main` there, so every commit link above resolves. **One cited commit is in a different repository**: `99fcb84` is not an object in the crew repo at all, and is reachable from the head of `master` in the **Stratocracy** UE project repo, whose tree it pins. That is the first citation this ledger makes outside the crew repo, and the split is structural rather than incidental — the `T-INT-01` gate check lives in the crew repo while the vendored tree it asserts over lives in the UE project, so the evidence chain spans both and each commit is cited against the repo it is in.
```

The universal was true until this landing and is now false as written: the
citation of `99fcb84` is not a crew-repo object. The sentence's purpose is that
every citation resolves, so it is widened to name the second source rather than
narrowed by dropping the commit that pins the vendored tree.

---

### Pair 4 — §4.5 risk cell: green total

**OLD**

```
**53** of the 71 are green
```

**NEW:**

```
**55** of the 71 are green
```

Derivation in the arithmetic section.

---

### Pair 5 — §4.5 risk cell: the per-commit green breakdown

**OLD**

```
and **1** at [`41a1452`](https://github.com/jakemartin/stratocracy-crew/commit/41a1452), where T-UI-05 closed without closing it either — so every row on the critical path has now landed, row 8 last and on a partial pass, **per acceptance ID as well as per row**.
```

**NEW:**

```
and **1** at [`41a1452`](https://github.com/jakemartin/stratocracy-crew/commit/41a1452), where T-UI-05 closed without closing it either, and **2** at [`b23823f`](https://github.com/jakemartin/stratocracy-crew/commit/b23823f), where T-INT-01 and T-INT-04 closed over the vendored tree at `99fcb84` without closing row 9's acceptance set — so every row on the critical path has now landed, row 8 last and on a partial pass, **per acceptance ID as well as per row**.
```

Adds the commit, so the breakdown still sums to Pair 4's total. It names the
acceptance set rather than a ledger row, because row 9 has none.

---

### Pair 6 — §4.5 risk cell: unclosed total

**OLD**

```
**18 IDs remain unclosed**
```

**NEW:**

```
**16 IDs remain unclosed**
```

The complement of Pair 4 against an unmoved written-ID total.

---

### Pair 7 — §4.5 risk cell: the unclosed enumeration for rows 9–10

**OLD**

```
alone; and the **12** in rows 9–10, which hold no code |
```

**NEW:**

```
alone; the **3** left in row 9 — T-INT-02, T-INT-03 and T-INT-05, the editor pass, for which no in-editor Automation harness exists — its other two having closed at `b23823f` (§3); and the **7** in row 10, which holds no code |
```

Row 9 now holds code, so the "hold no code" clause can no longer quantify over
both rows.

---

### Pair 8 — §4.4 week 2: T-INT-01/04 closed ahead of the cell

**OLD**

```
T-INT-01/04 and T-SAVE-04 close here, the rest do not (§4.11 rows 9–10).
```

**NEW:**

```
T-INT-01/04 and T-SAVE-04 close here, the rest do not (§4.11 rows 9–10) — and **T-INT-01/04 are green at `b23823f`** (§3), ahead of this cell rather than behind it, since neither runs on a command log or needs a rules row, and the vendoring they assert over has landed.
```

Same treatment §4.4's week-3 cell already gives `T-UI-05`. Its second clause is
also the one place this addendum states that the two IDs run on no log — see
the sweep note under check results.

---

### Pair 9 — §4.9 part 1: the vendoring step, now built

**OLD**

```
The UE project vendors them verbatim into a UBT runtime
module, `Source/StratRules/`, via a sync script that records the source commit
hash.
```

**NEW:**

```
The UE project vendors them verbatim into a UBT runtime
module, `Source/StratRules/`, via `sync_stratrules.py`, which reads each source
from the git object store rather than the working tree — so identity is true by
construction at the moment the script finishes — and records the source commit
as `rulesCommit` in `StratRules.manifest.json`. **That module now exists**, at
`99fcb84` in the UE project repo against `rulesCommit`
[`b23823f`](https://github.com/jakemartin/stratocracy-crew/commit/b23823f)
(§3): the ten modules Combat, Hex, Data, Move, Economy, Turn, Ai, Scenario, Ui
and Driver, each as `X.h` and `X.good.cpp`, beside two UE-owned files that have
no counterpart in the crew repo — `StratRules.Build.cs` and the manifest.
Vendored names are unchanged from the crew repo, so the comparison is
path-for-path with no rename map. `Driver` is in the set and is not optional:
`Ai.good.cpp` links against it. Nothing else is vendored — a UBT module cannot
hold a second `main()`, which excludes every `test_*.cpp`, `driver_main.cpp`
and `selfplay.cpp`, and the `*.buggy.cpp` files are pass-1 fixtures, not
shippable code.
```

The single home for the vendoring step, the vendored set and its derivation. It
states what the step produced and asserts nothing about what `T-INT-01`
compares.

---

### Pair 10 — §4.11 build-order table, row 9 cell

**OLD**

```
**Run vs close.** Vendoring and **T-INT-01/04** depend on no rules row at all — the sync script and the standalone gate run *are* the assert — and close as soon as vendoring lands.
```

**NEW:**

```
**Run vs close.** Vendoring and **T-INT-01/04** depend on no rules row at all — the sync script and the standalone gate run *are* the assert — and close as soon as vendoring lands, which they did at `b23823f` over the vendored tree at `99fcb84` (§3).
```

Pins the cell's own condition to the commit that satisfied it.

---

### Pair 11 — §4.11 lead prose: row 9's headless half

**OLD**

```
pass is now the whole of what this row still lacks and the row stays
unflipped on it. **Row 2 is not green:** T-DATA-01..04 and 06 pass
at that commit and T-DATA-05 has not run,
```

**NEW:**

```
pass is now the whole of what this row still lacks and the row stays
unflipped on it. **Row 9's headless half has since landed**, at `b23823f`
in the crew repo with the vendored tree at `99fcb84` in the UE project
repo: `T-INT-01` and `T-INT-04` are green there, under clang++, which is
what this row's cell means by closing as soon as vendoring lands.
**Row 9's acceptance set does not close**, on the Q29 reading rows 2, 7 and
8 stand on: `T-INT-02`, `T-INT-03` and `T-INT-05` did not run, no in-editor
Automation harness existing. **Row 2 is not green:** T-DATA-01..04 and 06
pass at `c224825` and T-DATA-05 has not run,
```

Puts row 9's partial landing in the build-order narrative beside rows 2, 7
and 8. The OLD runs one clause past the insertion point because *"at that
commit"* abuts it: the insertion moves that demonstrative's nearest antecedent
from `41a1452` to `99fcb84`, so the commit is named outright instead.

---

## Arithmetic

Derived from the closing fact that `T-INT-01` and `T-INT-04` closed at
`b23823f`, and that no acceptance ID was minted because no invariant text was
written this round.

| Quantity (§4.5 risk cell) | Before | Movement | After |
|---|---|---|---|
| Written acceptance IDs | 71 | none minted | 71 |
| Green | 53 | + T-INT-01, T-INT-04 | 55 |
| Unclosed | 18 | − T-INT-01, T-INT-04 | 16 |
| Verified ledger rows | 9 | no flip | 9 |

Green breakdown after Pair 5, summed: 18 + 9 + 9 + 6 + 7 + 1 + 2 + 1 + 2 = 55.

Unclosed enumeration after Pairs 6 and 7, summed: T-DATA-05 (1) + T-SCN-08, 09,
11 (3) + T-UI-03, 04 (2) + T-INT-02, 03, 05 (3) + T-SAVE-01..07 (7) = 16.

Complement: 71 − 55 = 16.

Row-9 written IDs: T-INT-01..05 = 5, of which 2 closed and 3 did not. Row-10
written IDs: T-SAVE-01..07 = 7, none closed. The prior combined figure 12 =
5 + 7; the figure that survives Pair 7 is row 10's 7 alone.

---

## Check results

- Every OLD returns exactly one occurrence in `source/gdd.md`. Pairs 2, 9 and
  11 were matched across their line breaks.
- **Both insertions were checked against the text abutting the seam on each
  side.** Pair 11 needed a second edit: the sentence after the seam reads
  *"T-DATA-01..04 and 06 pass at that commit"*, whose nearest antecedent the
  insertion moves from `41a1452` to `99fcb84`, so the OLD and NEW extend
  through that clause and name `c224825`, which is where §3's Data-tables
  evidence cell and §4.5's own breakdown put those five IDs. Pair 2 needed
  none: the sentence before the seam ends at *"preserved in place from
  `7c36303`"* and carries no forward reference, the inserted text opens by
  naming `e06c44b` outright, and the text after the seam is the Legend
  sentence, which contains no demonstrative.
- Pair 5's NEW opens with the same `and` the OLD opens with.
- Pair 7's OLD ends at the table-cell delimiter ` |`.
- The runner's pre-repair reach is stated as rows 6, 7, 8 and the driver, which
  is what did not run; rows 1–5 compiled and passed.
- No pair says row 9 flips, fails to flip, or records a partial pass as a
  ledger row: §4.11 calls it a *proposed* ledger row and none exists, so every
  pair speaks of its **acceptance set**.
- **Swept: `an integration or replay gate is scoped to the command set of the
  log it runs on` occurs twice** — in §4.4's note beneath the milestone table
  and in the Q20 register row — and **neither takes a pair.** The universal's
  own subject is the log a gate runs on, and each site immediately scopes
  itself to a gate that has one: §4.4's continues *"It runs as soon as that log
  can be produced and it closes only when the log carries every §4.9 command"*,
  and Q20's continues *"so T-INT-02 runs in week 2 over `{Move, Attack}`"*.
  `T-INT-01` and `T-INT-04` replay no log, so they were never inside the scope
  and no carve-out is owed at either site. That reading is stated once, in Pair
  8, where §4.4 says what those two do need.
- §4.11's † bullet reconciles §4.9's Acceptance line with the row-9 cell's
  marks — *"**T-INT-03 stays unmarked on the rule, not on cost:** §4.9 does
  place it in the editor pass, but what it asserts … is the bridge behaviour
  §4.9 contracts …, and a marked ID may not guard a rules invariant"* — so the
  † marks track cut-line membership and not headless-versus-editor, and the two
  passages never disagreed. No pair asserts which side `T-INT-03` is on.
- §3's *"Nine rows carry a ✓ … and three more carry evidence without one"* and
  *"Eight IDs are still recorded as **uncovered**"* are unchanged and not made
  false: no pair adds or removes a §3 table row, and that enumeration names
  T-MOVE-07, T-SCN-10, T-DATA-05, T-SCN-08, T-SCN-09, T-SCN-11, T-UI-03 and
  T-UI-04, none of which this round touches. §4.5 counts the `T-INT-` IDs
  separately — *"and the **12** in rows 9–10"* — so the two were already
  disjoint over them.
- §4.5's *"**71** written acceptance IDs … against **9** verified ledger rows"*
  and *"two new IDs have been written since `c224825`"* are unchanged.
- §4.11's † bullet *"T-INT-01/04 and T-SAVE-01..05 stay unmarked on **cost** —
  §4.9 runs T-INT-01/04 on every gate run"* is unchanged and now exercised.
- No pair edits invariant text, and no pair mints, renames or renumbers an
  acceptance ID or an open-question row.

---

## Change requests

| Existing § | Current text | Proposed change | Why |
|---|---|---|---|
| §4.9 spec stub, `T-INT-01` | `T-INT-01  source identity: every file in Source/StratRules/ hash-matches the recorded crew commit` | Director to decide whether the invariant text should name a UE-owned exemption, and whether that widening mints an ID | `StratRules.Build.cs` and `StratRules.manifest.json` have no counterpart in the crew repo to match, so the invariant as written cannot be satisfied by construction. The shipped check exempts exactly those and asserts presence, expectedness and identity of every other file. Invariant text is the Director's; the build changed none and no pair here writes the exemption into §4.9 |
| §3 ledger table; §4.11 rows 9–10 `(proposed ledger row)` | The §3 table has no row for §4.9 or §4.10 | Director to decide whether §3 gains a row for build-order row 9 now, and what it is called | Row 9's headless half landed with a citable commit and passing IDs, but §4.9 part 2 — the bridge — is unbuilt, so a row named for the bridge would claim a system that does not exist. This addendum records the landing in §3 prose and creates no row |
| §3 open-question register | — | Director to decide whether the `T-INT-01` question above becomes a numbered register row | Row 7's precedent registered its change request as `Q32`. A new register row moves that register's own ruled/open figures and the §4.7 sentence pinning their extent, so it is not done unasked |

---

## Grounding

- Runner breakage, cause, repair scope, post-repair tallies and MSVC re-runs:
  commit `e06c44b`, and the runner output of that run; the failing include
  originates at `7c36303`.
- Row 9's headless half, its new files and entry points: commit `b23823f`.
  Vendored tree, UE-owned files, `.gitattributes`: commit `99fcb84`, in the UE
  project repo and not resolvable in the crew repo, which is what Pair 3
  records.
- `T-INT-01` and `T-INT-04` 2/2; `T-INT-02`, `T-INT-03`, `T-INT-05` printed by
  name as not run; the control results; the skip-when-absent behaviour; the
  eleven-file and object-store observations: the `--integration` gate run at
  `rulesCommit` `b23823f`, and the five control runs beside it.
- The vendored set: forced by §4.9's *"no engine headers, no UObject, no
  third-party includes — pure C++17 in `namespace strat`"* together with a UBT
  module's inability to hold a second `main()`, which between them exclude
  every `test_*.cpp`, `driver_main.cpp` and `selfplay.cpp` and leave the ten
  modules' headers and good implementations.
- Name preservation, the object-store read, and the decision not to register
  the module in `Stratocracy.uproject`: Director rulings this session.
- `T-INT-04`'s any-one-compiler clause and the vendoring sentence Pair 9
  replaces: §4.9 as it stands in `source/gdd.md`.
- The run-versus-close split and the † bullet reconciling `T-INT-03`: §4.11's
  row-9 cell and its cut-line bullets.
- The log-scoping universal at both of its sites: §4.4's note beneath the
  milestone table, and the Q20 register row.
- `T-DATA-01..04, 06` green at `c224825`, which Pair 11 names: §3's Data-tables
  evidence cell and §4.5's per-commit breakdown.
- Q29's per-ID reading and the partial-pass posture of rows 2, 7 and 8: §3's
  ledger paragraph and evidence cells, and §4.5's unclosed enumeration.
- Post-repair per-row tallies match the figures §3 already records for rows 1–8
  at their own commits, which is how the runner's output was checked rather
  than taken.
