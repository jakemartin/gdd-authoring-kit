# Addendum — round `ue-harness` (tech-director)

> **SEALED — MERGED 2026-08-05.** Applied to
> `../stratocracy-content/Stratocracy_Prototype_GDD.md`; master md5
> `7f161314` → **`e1d36927`** (the LF/index convention). Do not re-apply and do
> not edit: the master is now the record.
>
> **Gate history:** `ue-harness-1` BLOCK 5 → `-2` BLOCK 2 → `-3` BLOCK 1 →
> `-4` BLOCK 1 → `-5` BLOCK 5 → `-6` BLOCK 3 → `-7` BLOCK 2 → `-8` BLOCK 1 →
> **`ue-harness-9` PASS 0**. Accept record: `gate/accept.json`.
>
> **25 pairs. Pairs 12 and 14 are INSERTIONS** — classified by substring test on
> the bytes, never by the prose, and their OLD anchors **survive in the master by
> design**. The other 23 are replacements. A post-check expecting zero surviving
> anchors would misread those two, and a second application would duplicate them.
>
> **A NEW block ends at its `*Note.*` line**, or at the `---` for the two pairs
> that carry no note. The notes are apparatus and were **not** merged.
>
> **Measurements at merge:** over-90-char non-table lines **125 → 129 → 125**,
> restored by a reflow of four lines proved whitespace-only by comparing a
> whitespace-collapsed view of the whole document. §3's two ledger paragraphs are
> deliberately single lines of 79,989 and 8,446 characters and were **not**
> reflowed. §2 byte-identical at 105,465 characters, all 29 heading blocks
> unchanged and all four `kb/rules.md`-mirrored subsections identical, so the
> **KB was untouched** — decided positively, and confirmed by its md5. Derived
> files rebuilt after both recipes were control-tested against the previous
> commit: `.txt` reproduced it byte-exactly, the PDF's extraction identically.
> PDF **96 → 99 pages**.

OLD/NEW pairs applied to
`../stratocracy-content/Stratocracy_Prototype_GDD.md`. Every OLD block was
searched against `source/gdd.md` — and again against the master itself at merge
time — and appeared in each exactly once.

---

### Pair 1 — §3 status line: the round's commits and their ancestry

**OLD**

This draft stands at 2026-08-05, at commit [`1ee890e`](https://github.com/jakemartin/stratocracy-crew/commit/1ee890e) in the crew repo and at `9dec48c` in the Stratocracy UE project repo. In the crew repo, [`ec15be6`](https://github.com/jakemartin/stratocracy-crew/commit/ec15be6), [`737f666`](https://github.com/jakemartin/stratocracy-crew/commit/737f666) and [`d837fc8`](https://github.com/jakemartin/stratocracy-crew/commit/d837fc8) are each an ancestor of `1ee890e`, measured with `git merge-base --is-ancestor` per sha rather than read off a branch. `1ee890e` is cited as a commit, and this line makes no claim about how it stands to any branch.

**NEW:**

This draft stands at 2026-08-05, at commit [`031ee20`](https://github.com/jakemartin/stratocracy-crew/commit/031ee20) in the crew repo and at `a13626f` in the Stratocracy UE project repo. In the crew repo, [`ec15be6`](https://github.com/jakemartin/stratocracy-crew/commit/ec15be6), [`737f666`](https://github.com/jakemartin/stratocracy-crew/commit/737f666), [`d837fc8`](https://github.com/jakemartin/stratocracy-crew/commit/d837fc8), [`30a73f0`](https://github.com/jakemartin/stratocracy-crew/commit/30a73f0), [`188f966`](https://github.com/jakemartin/stratocracy-crew/commit/188f966), [`e19605e`](https://github.com/jakemartin/stratocracy-crew/commit/e19605e) and `1ee890e` are each an ancestor of `031ee20`, measured with `git merge-base --is-ancestor` per sha rather than read off a branch. In the UE project repo, `9dec48c` is an ancestor of `a13626f`, measured the same way. `031ee20` and `a13626f` are cited as commits, and this line makes no claim about how either stands to any branch.

*Note.* The ancestry is now stated once, against `031ee20`, where the draft
stands. **Deletion tripwire:** the clause measuring `ec15be6`, `737f666` and
`d837fc8` against `1ee890e` is dropped rather than kept beside the new one —
each of those shas was measured against `031ee20` this round, and `1ee890e` is
named in the same enumeration, so no measured claim is lost. Nothing else in
the line changes.

---

### Pair 2 — §3, the `b23823f` landing: unpin the present tense that a build has now falsified

**OLD**

**What this landing did not build is stated so it is not inferred.** The module is **defined** by `StratRules.Build.cs` and is **not wired into any build target** — `Stratocracy.uproject` does not list it, nothing depends on it, and **no UBT build was run** — the Director's decision this session, on the ground that registering it would claim an in-engine build this round cannot verify.

**NEW:**

**What this landing did not build is stated so it is not inferred.** The module was **defined** by `StratRules.Build.cs` and was **not wired into any build target** — `Stratocracy.uproject` did not list it, nothing depended on it, and **no UBT build was run** — the Director's decision that session, on the ground that registering it would have claimed an in-engine build that round could not verify. Registration and the first UBT build are recorded below, at their own commits.

*Note.* The three present-tense clauses asserted something about the reader's
now, not about `b23823f`; the registration at `a13626f` falsifies them. Tense
is the whole change — the landing record is otherwise untouched.

---

### Pair 3 — §3, the `d837fc8` landing: its two closure sentences were written in the present

**OLD**

**`T-INT-01`'s green re-dates to this commit**, over the vendored tree at `9dec48c`, and is recorded here rather than left at `b23823f`: `ue_module/manifest_fields.json` did not exist at `b23823f`, so the amended text cannot have been satisfied there, and the closure convention §4.5 states governs where the green lands. **`T-INT-04` is unaffected** — its text did not change, it is green at `b23823f` and green again here.

**NEW:**

**`T-INT-01`'s green re-dated to this commit**, over the vendored tree at `9dec48c`, and was recorded here rather than left at `b23823f`: `ue_module/manifest_fields.json` did not exist at `b23823f`, so the amended text cannot have been satisfied there, and the closure convention §4.5 states governs where the green lands. **`T-INT-04` was unaffected at this landing** — its text did not change, and it passed at `b23823f` and again here. Both greens moved on at `e19605e`, each for its own reason, recorded below.

*Note.* Same defect as Pair 2 in the other direction: a green stated in the
present outlives the landing it belongs to. The re-dating itself is Pair 5's
subject; this pair only stops the older record from contradicting it.

---

### Pair 4 — §3, the `d837fc8` landing: registration and build status pinned to that commit

**OLD**

the vendored module is **still not registered** in `Stratocracy.uproject`, and **no UBT build has been run**.

**NEW:**

the vendored module was **still not registered** in `Stratocracy.uproject` at that commit, and **no UBT build had been run** by it.

*Note.* "Has been run" is a claim about today, and today it is false. The
neighbouring clause in the same sentence — `T-INT-02`, `T-INT-03` and
`T-INT-05` still did not run, no in-editor Automation harness existing — is
left as written: the harness still does not exist.

---

### Pair 5 — §3, new landing record: the UBT build, the check defect and its repair, and the re-dating

**OLD**

**How `1ee890e` was authored is deliberately not stated:** no harness claim is made for it, because none was established.* Legend:

**NEW:**

**How `1ee890e` was authored is deliberately not stated:** no harness claim is made for it, because none was established. **The UBT landing then followed**, at [`031ee20`](https://github.com/jakemartin/stratocracy-crew/commit/031ee20) in the crew repo — over [`30a73f0`](https://github.com/jakemartin/stratocracy-crew/commit/30a73f0), which added the `Build.cs` line and a spec repair, [`188f966`](https://github.com/jakemartin/stratocracy-crew/commit/188f966), which corrects a sentence `30a73f0` had written ahead of a landing that did not then happen, and [`e19605e`](https://github.com/jakemartin/stratocracy-crew/commit/e19605e) — with the UE project repo at `a13626f`, where `Stratocracy.uproject`, `Source/StratRules/StratRules.Build.cs`, `Source/StratRules/StratRules.manifest.json` and `Source/StratRules/Turn.h` changed. `Stratocracy.uproject` now lists `StratRules`, and building the `StratocracyEditor` target compiles the vendored crew modules and links `UnrealEditor-StratRules.dll`. **These sources had never been compiled by UBT before.** The first attempt **failed**, on one diagnostic — *Driver.good.cpp(657,24): error C4456: declaration of 'r' hides previous local declaration* — because both targets set `DefaultBuildSettings = BuildSettingsVersion.V7`, and `BuildSettingsVersion.V2` onward raises `ShadowVariableWarningLevel` to `Error`, read from the engine's own `TargetRules.cs`; every other vendored crew module compiled clean. With `CppCompileWarningSettings.ShadowVariableWarningLevel = WarningLevel.Warning` in `StratRules.Build.cs`, scoped to that UBT module, the build succeeds, and C4456 and a C4457 that was never an error still print. **What this landing does not establish is stated so it is not inferred:** it compiled and it linked. **No editor was launched, nothing was executed, no runtime behaviour was observed, and the build mints no acceptance ID and closes none.** A green UBT build is not evidence for any acceptance ID — `T-INT-04` asserts the **standalone** compile, outside UBT, while in-engine compilation is what the editor pass gates, and that pass does not exist. What the build does add is an MSVC compile **through UBT, under the engine's own flags** — a toolchain configuration these sources had not been built under, and not a compiler they had not seen, the standalone gate having compiled them under clang++ and MSVC both throughout. **`T-INT-01`'s running check was then found defective, and repaired at `e19605e`.** The check derived its expected file set with `git ls-tree --name-only <rulesCommit>:cpp_reference` filtered to `*.h` and `*.good.cpp` — that is, every crew module — while the vendored set is the ten crew modules §4.9 enumerates, `Save`, `Replay` and `Balance` being ruled out of vendoring. Those two sets coincided only until `Save` landed at [`737f666`](https://github.com/jakemartin/stratocracy-crew/commit/737f666). Measured: re-vendoring at `30a73f0` produced *FAIL T-INT-01 ... missing 6: Balance.good.cpp, Balance.h, Replay.good.cpp, Replay.h, Save.good.cpp, Save.h*. **The consequence is what makes it worth a ledger entry: `rulesCommit` could not be advanced to any commit at or after `737f666`, for any reason.** The vendored manifest recorded `d837fc8` throughout, and `d837fc8` is an ancestor of `737f666`, so the collision had no occasion to show itself while three landings went by. `T-INT-01`'s written text quantifies over *every file in `Source/StratRules/`* — the vendored tree — and not over every crew source, so **the check asserted more than the text did**, which is the mirror image of Q33 and is ruled the mirror way: **the vendored set is declared, not inferred, and `T-INT-01`'s invariant text is unchanged**, the repaired check asserting what the text always said, so this is the check catching up rather than a widening. `ue_module/vendored_set.json` declares the set; both `sync_stratrules.py` and the check read it from the git object store at the commit in question, so neither imports the other's constants, and the declaration **must partition** the crew's modules — every crew module appears in exactly one of `vendored` and `excluded`. **`rulesCommit` moves `d837fc8` → `e19605e`**, where `T-INT-01` and `T-INT-04` pass **2/2**. The `T-INT-01` PASS line reads, verbatim: *T-INT-01 source identity: all 22 files in Source/StratRules/ are accounted for at e19605e — 20 sources and StratRules.Build.cs hash-match tracked blobs, StratRules.manifest.json recomputes byte-for-byte, and the declared vendored set partitions the 13 crew modules (10 vendored, 3 ruled out)*. The full `python run.py --week1` record is accepted, with every row's tally unchanged from the pre-change baseline taken before anything was edited — row 1 7/7, row 2 6/6, row 3 6/6, row 4 9/9, row 5 11/11, row 6 7/7, row 7 12/12, row 8 34/34, row 10 parts (a) 25/25, (b) 29/29 and (c) 12/12, and the debug driver 12/12. **The gate was shown to fail before it was trusted**, on known-bad inputs each restored afterwards: a comment appended to a vendored source FAILs `T-INT-01` on a hash mismatch; a deleted vendored header FAILs `T-INT-01` missing and FAILs `T-INT-04`; an extra `Sneaky.good.cpp` FAILs `T-INT-01` unexpected; a comment appended to the vendored `StratRules.Build.cs` FAILs `T-INT-01` on a hash mismatch; a crew module in neither declared list FAILs `T-INT-01` unaccounted; a module in both declared lists FAILs `T-INT-01` declared-both; and a declared module with no `cpp_reference` source FAILs `T-INT-01` no-source. One input is a **design control rather than a defect**: the declaration edited in the **working tree only** PASSes, the verdict unmoved, because the check reads the object store. The first attempt at the no-source control was **invalid** — `sync` aborts when a declared module has no source, so the manifest was never rewritten and the gate re-read the previous control's commit; it was redone against a distinct commit. Those are the inputs that were run and the verdicts they produced, and no claim of coverage beyond them is made here. **Both `T-INT` closures re-date to `e19605e`, for different reasons, and each is stated separately.** `T-INT-01` re-dates because it asserts identity **at `rulesCommit`**, and `rulesCommit` moved. `T-INT-04` re-dates because it compiles the **vendored copy**, and one vendored source's bytes changed: `Turn.h`, which changed at [`ec15be6`](https://github.com/jakemartin/stratocracy-crew/commit/ec15be6) with row 10's part (b) and is, measured file by file, the only vendored source whose bytes differ between `d837fc8` and `e19605e`. Neither ID's **text** changed, so this is a closure movement and not a widening. **No acceptance ID is minted and none closes**, so §4.5's written, green and unclosed figures do not move; what moves is the by-commit attribution of two already-green IDs. **No ledger row is created, flipped or removed by this landing**, and the register of open questions gains no row and loses none. `T-SAVE-06` remains the only † of row 10's seven, and among what it waits on are the in-editor Automation harness and a vendored replayer: it is asserted jointly with `T-INT-02`, whose replay runs **in-engine** and so needs the replayer compiled into the engine, and `Replay` is ruled out of vendoring until a bridge consumer exists. Whether *the editor pass* is meant to carry those subjects is **not ruled here**. `cpp_reference/selfplay.cpp` is untouched. `Save`, `Replay` and `Balance` remain unvendored, and the ruling that keeps them out is now **stated in the declaration** rather than implied by a glob. **Two further rulings are recorded here.** The win-rate / turn-length **distribution reporter** is scheduled in the week that already owes the sims and the tuning themselves, and it gains **no build-order row and no acceptance ID**: it aggregates logs, defines no format and owns no rule, §4.10 already enumerates the Balance Analyst self-play log among the format's consumers, and the producer of that log has landed. The driver's `openActiveTurn` retirement condition stays **filed and deliberately unasserted**: the driver owns no rule, so a second implementation of a ruled *order* is duplication rather than unsoundness, and nothing green depends on it. **Two forms were considered and declined, with the reason recorded so neither is re-filed:** a document-wide reachability form that survives a landing, and a rule that a "has since" sentence must carry a commit pin. Both are ways of phrasing claims, and a closed list of legal phrasings has been adopted and withdrawn here before. **How `031ee20` was authored is deliberately not stated:** no harness claim is made for it, because none was established.* Legend:

*Note.* An insertion. OLD is the anchor sentence that ends the ledger
narrative, reproduced verbatim at the head of NEW; everything after it is new,
and the closing `*` and ` Legend:` are carried through unchanged so the
italic run and the legend that follows it are not disturbed. **The sentence
recording `T-SAVE-06`'s status has been amended at successive gate runs, and
nothing else in this NEW block has moved at any of them.** After gate run
`ue-harness-4` it said the ID waits on the in-editor Automation harness
*alone*, which this pair's own neighbour — Pair 15's decomposition —
falsifies. After gate run `ue-harness-5` the replacement was read as **a
narrower universal in the same family**: *what it waits on is the harness and a
vendored replayer* is still an exhaustiveness claim, so the form became
**non-exhaustive** (*among what it waits on are …*). At this pass the §4.8
tables imported in-editor are **removed** from the list. That phrase comes from
§4.9's parity stub `Inputs` line, which is stub-level, and this draft records
`T-INT-01` and `T-INT-04` green at `e19605e` over the very tree in which Pair
15 measures those tables absent — so naming them as a subject of this ID
attributes a stub-level line to a particular assertion, which the round did not
establish. Nothing replaces them: *among* does not promise the list is
complete, which is what makes the removal safe. The sentence leaves the reading
of *the editor pass* to the Director, change request 3 below carries that
judgement, and change request 4 carries the per-ID question about the tables.

---

### Pair 6 — §3, the parenthetical enumerating which cited commits are not objects in the crew repo

**OLD**

**Not every cited commit is an object in the crew repo**: `99fcb84` and `9dec48c` are not objects in it at all: each is a commit in the **Stratocracy** UE project repo, whose tree it pins, and this parenthetical makes no claim about how either stands to any branch there (ruled 2026-08-05).

**NEW:**

**Not every cited commit is an object in the crew repo**: `99fcb84`, `9dec48c` and `a13626f` are not objects in it at all, measured with `git cat-file -e` per sha and controlled against `e19605e`, which does resolve there: each is a commit in the **Stratocracy** UE project repo, whose tree it pins, and this parenthetical makes no claim about how any of them stands to any branch there (ruled 2026-08-05).

*Note.* This sentence is an enumeration, so citing `a13626f` in the status line
and in the landing record above without naming it here would leave the
enumeration false. The control is stated because a probe that silently returns
nothing looks exactly like a probe that finds nothing: `e19605e` resolves in
the crew repo under the same command. The rest of the passage is left as
written and still holds with the further sha named — the ruling this
parenthetical records and its confinement to this parenthetical, the replaced
`master`-reachability form, the reason the split across repos is structural,
and the observation that `99fcb84` was the first citation this ledger made
outside the crew repo.

---

### Pair 7 — §4.4, the week-2 gate cell: where the two `T-INT` greens now stand

**OLD**

**T-INT-04 is green at `b23823f`** and **T-INT-01 at [`d837fc8`](https://github.com/jakemartin/stratocracy-crew/commit/d837fc8)**, over the vendored tree at `9dec48c`

**NEW:**

**T-INT-04 and T-INT-01 are green at [`e19605e`](https://github.com/jakemartin/stratocracy-crew/commit/e19605e)**, over the vendored tree at `a13626f`

*Note.* The cell's own argument — all three IDs ahead of this cell rather than
behind it, since none runs on a command log or needs a rules row — is
untouched and still holds.

---

### Pair 8 — §4.5, green distribution: the two entries the re-dating vacates

**OLD**

and **1** at [`b23823f`](https://github.com/jakemartin/stratocracy-crew/commit/b23823f), where T-INT-04 closed over the vendored tree at `99fcb84` without closing row 9's acceptance set, and **1** at [`d837fc8`](https://github.com/jakemartin/stratocracy-crew/commit/d837fc8), where the widened T-INT-01 closed over the vendored tree at `9dec48c` without closing it either — under **the closure convention this document states once, here: an ID whose written text widens closes at the commit at which the widened text is met**, `T-INT-04`'s text not having changed (§3) — and **1** at [`737f666`](https://github.com/jakemartin/stratocracy-crew/commit/737f666)

**NEW:**

and, under **the closure convention this document states once, here: an ID whose written text widens closes at the commit at which the widened text is met**, the widened T-INT-01 first closed at [`d837fc8`](https://github.com/jakemartin/stratocracy-crew/commit/d837fc8) over the vendored tree at `9dec48c` rather than at [`b23823f`](https://github.com/jakemartin/stratocracy-crew/commit/b23823f), where T-INT-04, whose text did not change, first passed over the vendored tree at `99fcb84`; both greens now stand at `e19605e` and are counted there below (§3) — and **1** at [`737f666`](https://github.com/jakemartin/stratocracy-crew/commit/737f666)

*Note.* **Deletion tripwire.** The two per-commit tallies are dropped from this
position and the entry that replaces them is Pair 9, at the end of the list
where the commit belongs chronologically. Nothing else is lost: the closure
convention — stated once in the whole document, here — and both first-pass
commits are kept in the NEW block. The addends are reconciled under
*Arithmetic* below.

---

### Pair 9 — §4.5, green distribution: the entry the re-dating creates

**OLD**

and **1** at [`1ee890e`](https://github.com/jakemartin/stratocracy-crew/commit/1ee890e), where `T-SAVE-07` closed on row 10's part (c) over a self-play log written in this format, without closing that row's acceptance set either — so every row on the critical path has now landed

**NEW:**

and **1** at [`1ee890e`](https://github.com/jakemartin/stratocracy-crew/commit/1ee890e), where `T-SAVE-07` closed on row 10's part (c) over a self-play log written in this format, without closing that row's acceptance set either, and **2** at [`e19605e`](https://github.com/jakemartin/stratocracy-crew/commit/e19605e), where `T-INT-01` and `T-INT-04` re-date over the vendored tree at `a13626f` without closing row 9's acceptance set either — `T-INT-01` because it asserts identity at `rulesCommit`, which moved there, and `T-INT-04` because it compiles the vendored copy, whose `Turn.h` bytes changed — neither on a text change, so both are closure movements rather than widenings (§3) — so every row on the critical path has now landed

*Note.* An anchored append: the `1ee890e` entry is reproduced verbatim and the
new entry is added after it, before the clause that closes the sentence. The
two reasons are stated separately because they are different reasons.

---

### Pair 10 — §4.5, row 9's unclosed IDs: the two that have closed

**OLD**

its other two having closed — T-INT-04 at `b23823f`, and T-INT-01 at `d837fc8` on the widening of its own text (§3);

**NEW:**

its other two having closed and both now credited at `e19605e` — T-INT-01 because it asserts identity at `rulesCommit`, which moved there, and T-INT-04 because it compiles the vendored copy, whose `Turn.h` bytes changed; T-INT-04 first passed at `b23823f`, and T-INT-01 first closed at `d837fc8` on the widening of its own text (§3);

*Note.* Same movement as Pairs 8 and 9, at the second site in §4.5 that names
these commits. The unclosed set itself does not change.

---

### Pair 11 — §4.9, module layout: the vendored tree and the commit it records

**OLD**

as `rulesCommit` in `StratRules.manifest.json`. **That module now exists**, at
`9dec48c` in the UE project repo against `rulesCommit`
[`d837fc8`](https://github.com/jakemartin/stratocracy-crew/commit/d837fc8)
(§3): the ten modules Combat, Hex, Data, Move, Economy, Turn, Ai, Scenario, Ui

**NEW:**

as `rulesCommit` in `StratRules.manifest.json`. **That module now exists**, at
`a13626f` in the UE project repo against `rulesCommit`
[`e19605e`](https://github.com/jakemartin/stratocracy-crew/commit/e19605e)
(§3): the ten modules Combat, Hex, Data, Move, Economy, Turn, Ai, Scenario, Ui

---

### Pair 12 — §4.9, module layout: the vendored set is declared

**OLD**

optional: `Ai.good.cpp` links against it. Nothing else is vendored — a UBT
module cannot hold a second `main()`, which excludes every `test_*.cpp`,
`driver_main.cpp` and `selfplay.cpp`, and the `*.buggy.cpp` files are pass-1
fixtures, not shippable code.

**NEW:**

optional: `Ai.good.cpp` links against it. Nothing else is vendored — a UBT
module cannot hold a second `main()`, which excludes every `test_*.cpp`,
`driver_main.cpp` and `selfplay.cpp`, and the `*.buggy.cpp` files are pass-1
fixtures, not shippable code. **The set is declared, not inferred (ruled
2026-08-05).** `ue_module/vendored_set.json` in the crew repo names it, and
both `sync_stratrules.py` and `T-INT-01`'s check read that declaration from the
git object store at the commit in question, so neither takes its expectation
from the other. The declaration **must partition** the crew's modules: every
crew module appears in exactly one of `vendored` and `excluded`, so a module
can be neither swept in by a glob nor left out in silence, and the check FAILs
a module that appears in neither list and one that appears in both (§3).

*Note.* An anchored append; the OLD paragraph opening is reproduced verbatim.
This is the rule that replaces the `*.h` + `*.good.cpp` glob the repaired
check dropped.

---

### Pair 13 — §4.9, the three unvendored modules: their closure claim was written in the present

**OLD**

re-date `T-INT-01`'s and `T-INT-04`'s closures. That is a decision rather than
an omission, and **nothing re-dates on their account**: `T-INT-01` stays green
at `d837fc8` and `T-INT-04` at `b23823f`, both still passing 2/2 at
`rulesCommit` `d837fc8` after the third module landed, and no UE project commit
was made at any of the three landings.

**NEW:**

re-date `T-INT-01`'s and `T-INT-04`'s closures. That is a decision rather than
an omission, and **nothing re-dated on their account**: after the third module
landed `T-INT-01` was green at `d837fc8` and `T-INT-04` at `b23823f`, both
still passing 2/2 at `rulesCommit` `d837fc8`, and no UE project commit was made
at any of the three landings. Both closures now stand at `e19605e` (§3) —
`T-INT-01` because `rulesCommit` moved and `T-INT-04` because `Turn.h`'s
vendored bytes changed — and neither moved on these three modules' account,
which leaves the decision recorded here as it was made.

*Note.* The claim the paragraph needs is that these three modules cost no
re-dating, and that claim survives; what did not survive is the present-tense
evidence offered for it.

---

### Pair 14 — §4.9, new paragraph: the UBT build, and what a green build is not

**OLD**

`namespace strat`, exactly the base-spec constraint. The standalone gate keeps
compiling the identical files, so "the engine build works" never substitutes
for "the gate passed."

**NEW:**

`namespace strat`, exactly the base-spec constraint. The standalone gate keeps
compiling the identical files, so "the engine build works" never substitutes
for "the gate passed."

**The UBT module is registered, and it builds.** `Stratocracy.uproject` lists
`StratRules` at `a13626f`, and building the `StratocracyEditor` target compiles
the vendored crew modules and links `UnrealEditor-StratRules.dll` — sources UBT
had never compiled before (§3). The setting that governs shadowing under UBT is
recorded here with the diagnostic that stopped the first attempt: both targets
set `DefaultBuildSettings = BuildSettingsVersion.V7`, and
`BuildSettingsVersion.V2` onward raises `ShadowVariableWarningLevel` to
`Error`, read from the engine's own `TargetRules.cs`. Under that setting C4456
— `Driver.good.cpp` shadowing a local — stopped the first attempt. The build
sets `CppCompileWarningSettings.ShadowVariableWarningLevel =
WarningLevel.Warning` in `StratRules.Build.cs`, **scoped to this UBT module**
and to nothing else, and C4456 still prints, as a warning. **A green UBT build
closes nothing.** It
compiled and it linked; no editor was launched, nothing was executed, and the
build mints no acceptance ID and closes none. `T-INT-04` asserts the
**standalone** compile, outside UBT; in-engine compilation is what the editor
pass gates, and that pass does not exist. What the build does add is an MSVC
compile **through UBT, under the engine's own flags** — a toolchain
configuration these sources had not been built under, and not a compiler they
had not seen, the standalone gate having compiled them under clang++ and MSVC
both throughout. **A UBT rejection cannot be fixed in place.** The vendored
sources are hash-matched against the crew repo by `T-INT-01`, so an edit in
`Source/StratRules/` FAILs the gate rather than fixing the build: the fix goes
into the crew repo and the tree is re-vendored. This round is the worked
example, and it is not free — both `T-INT` closures re-dated as a result (§3).

*Note.* An insertion; OLD is the closing sentence of §4.9 part 1, reproduced
verbatim at the head of NEW. Nothing in the anchor changes. The paragraph
states the mechanism and the diagnostic that was observed under it, and
generalises from neither: C4456 is the diagnostic that stopped the build, and
the C4457 the same builds printed was a warning throughout.

---

### Pair 15 — §4.9 part 2: the harness is recorded as a blocker, and it is not sufficient

**OLD**

The harness is recorded here as the remaining blocker and is not scheduled here.

**NEW:**

The harness is recorded here among what part 2 is blocked on, and is not
scheduled here. **It is also not sufficient**, and among what the remaining
editor-pass IDs need besides it are the subjects named here rather than left to
be discovered at the pass: `T-INT-02` needs a **vendored replayer**, and
`Replay` is ruled out of vendoring until a bridge consumer exists; `T-INT-03`
needs the **command surface**, which is part of the unbuilt bridge; `T-INT-05`,
`T-UI-03` and `T-UI-04` need **real Stratocracy widgets**; `T-DATA-05` needs
**imported DataTables and a `UENUM` mirror of the unit type**; and `T-SAVE-06`
is asserted jointly with `T-INT-02`. None of those subjects exists at
`a13626f`, measured in the UE project repo
there: the identifier `EUnitType` occurs zero times case-sensitively in the
tracked tree; `UENUM` occurs zero times anywhere under `Source/`, a zero
controlled against `UCLASS`, which does occur there; and every tracked
DataTable and widget asset belongs to the `AdvancedTurnBasedTileToolkit`
marketplace content or to the UE template. The stub below carries its own
`Inputs` line — a §4.10 replay file and the §4.8 tables imported in-editor —
which lists what that stub draws on; the imported tables are not among the
DataTable assets measured above. **Registering the UBT module closes
no acceptance ID, and neither does the harness by itself.** One constraint the
harness inherits: `T-INT-01` asserts that no file in `Source/StratRules/` is
unaccounted for, so **the harness may not live in that directory** — a test
file there fails a green ID, confirmed against the running check, where an
extra `Sneaky.good.cpp` in that directory FAILs (§3).

*Note.* An anchored **replacement**, not an append: the anchor sentence is
repaired rather than reproduced. **Amended after gate run `ue-harness-6`**,
which found *the remaining blocker* — the OLD sentence, carried verbatim into
this pair's own NEW block through five runs — to be a further member of the
family Pairs 19–25 repair. It is a definite article doing sufficiency work,
spelled without a single token any earlier sweep probed, and it says of the
harness exactly what those pairs stop the document saying elsewhere. The
sentence now records the harness **among** what part 2 is blocked on. The same
run found the umbrella one clause later — *what each remaining editor-pass ID
needs besides it is stated* — to be the same defect at the level of the list,
so the umbrella is now **non-exhaustive**, and the stub's `Inputs` line stands
as its own sentence rather than inside the `T-SAVE-06` clause where the
`ue-harness-5` amendment had put it. **Amended again after gate run
`ue-harness-7`**, which read that sentence's second half — *that line binds the
invariants the stub governs, `T-INT-03` and `T-INT-05` among them* — as a
contradiction introduced by the previous amendment: the stub governs `T-INT-01`
through `T-INT-05`, and `T-INT-01` and `T-INT-04` are recorded green at
`e19605e` over the very tree in which this block measures those tables absent.
The half is **deleted rather than narrowed**, because a shorter list of bound
IDs is the same defect one level down. The line is now named as what the stub
draws on, and this pair attaches it to no invariant. **This block did not move
at this pass**, which extends that same treatment to Pairs 5, 19, 20 and 21.

---

### Pair 16 — §4.11, the row-9 paragraph: where row 9's two green IDs are credited

**OLD**

**Row 9's headless half has since landed**, at `b23823f`
in the crew repo with the vendored tree at `99fcb84` in the UE project
repo: `T-INT-04` is green there, under clang++, which is
what this row's cell means by closing as soon as vendoring lands.
**`T-INT-01` is green at `d837fc8`**, over the vendored tree at `9dec48c`,
and not at the earlier landing: its written text was widened there, over an
input that did not exist before it, so it closes there under the closure
convention §4.5 states (§3). The landing stands as the landing it was; what moves is where
the widened ID closes — the treatment row 5 already has, whose
`T-TURN-01..10` closes at its rebuild while `T-TURN-01..09` first closed at
`ad77b13`.

**NEW:**

**Row 9's headless half has since landed**, at `b23823f`
in the crew repo with the vendored tree at `99fcb84` in the UE project
repo, which is what this row's cell means by closing as soon as vendoring
lands. **`T-INT-01` and `T-INT-04` are green at `e19605e`**, over the vendored
tree at `a13626f`, the standalone gate that asserts `T-INT-04` running under
clang++, and not at the landings that first passed them: `T-INT-01` asserts
identity at `rulesCommit`, and `rulesCommit` moved there, while `T-INT-04`
compiles the vendored copy, whose `Turn.h` bytes changed. Neither ID's text
changed there, so both are closure movements rather than widenings; earlier,
`T-INT-01`'s written text was widened at `d837fc8`, over an input that did not
exist before it, so it closed there under the closure convention §4.5 states
(§3). Each landing stands as the landing it was; what moves is where an ID's
green is credited — the treatment row 5 already has, whose
`T-TURN-01..10` closes at its rebuild while `T-TURN-01..09` first closed at
`ad77b13`.

*Note.* "Under clang++" is kept, attached to the gate that asserts `T-INT-04`.
The row's own argument — that vendoring alone closes these two and that the
acceptance set still does not close — is unchanged, and the sentences after
this passage that say `T-INT-02`, `T-INT-03` and `T-INT-05` did not run remain
true.

---

### Pair 17 — §4.11, the row-9 dependency cell

**OLD**

and close as soon as vendoring lands, which `T-INT-04` did at `b23823f` over the vendored tree at `99fcb84`, and `T-INT-01` at `d837fc8` over the vendored tree at `9dec48c` (§3).

**NEW:**

and close as soon as vendoring lands, which `T-INT-04` first did at `b23823f` over the vendored tree at `99fcb84`, and `T-INT-01` at `d837fc8` over the vendored tree at `9dec48c`; **both greens now stand at `e19605e`**, over the vendored tree at `a13626f`, re-dated there for their own separate reasons (§3).

---

### Pair 18 — §4.9, module layout: the sentence that says what the paragraph gains

**OLD**

The enumeration above is correct as it
stands and gains only the statement that three modules were left out on
purpose.

**NEW:**

The enumeration above is correct as it
stands, and three modules were left out on purpose.

*Note.* Pair 12 appends a second ruling to this same paragraph — the set is
declared, not inferred, and the declaration must partition the crew's
modules — so *gains only the statement that* is false as soon as this round's
pairs are applied. The exhaustive quantifier is **deleted rather than
corrected**: a replacement that counted what the paragraph now gains would put
a cardinal where an enumeration belongs, and the paragraph's own sentences
already say what it contains. Both surviving claims are checked and hold: the
ten-module enumeration is unchanged by anything this round, `vendored_set.json`
declaring exactly those ten as `vendored`, and the deliberate exclusion of
`Save`, `Replay` and `Balance` is the sentence's own subject and is restated in
Pair 12's declaration. Nothing else is made false by this edit; the sentence
that follows it — `cpp_reference/selfplay.cpp` is not one of the three, is
excluded because a UBT module cannot hold a second `main()`, and stays in that
exclusion list unchanged — is untouched and still true, `selfplay.cpp` being a
source file rather than a crew module and so not a member of either declared
list.

---

### Pair 19 — §3, the `T-SAVE-06` landing record: what it waits on, decomposed

**OLD**

its other blocker — §4.10's canonical state hash having no implementation — is removed here, so the in-editor Automation harness is now the whole of what it waits on.

**NEW:**

its other blocker — §4.10's canonical state hash having no implementation — is removed here, and among what it still waits on are the in-editor Automation harness and a vendored replayer: it is asserted jointly with `T-INT-02`, whose replay runs **in-engine** and so needs the replayer compiled into the engine and therefore vendored, and `Replay` is ruled out of vendoring until a bridge consumer exists. Whether *the editor pass* is meant to carry those subjects is **not ruled here**.

*Note.* **This defect predates this round; nothing that landed caused it.** It
is in scope because Pair 15 is the first text in the document to state the
decomposition that falsifies it, so applying these pairs without this one would
put the decomposition and its contradiction in the same document. **Rewritten
after gate run `ue-harness-5`:** the first repair replaced *the whole of what it
waits on* with *what remains is the harness and a vendored replayer*, which is
a narrower universal of the same family, so the form became **non-exhaustive** —
it names subjects without claiming to have named them all. **Rewritten again at
this pass:** the §4.8 tables imported in-editor are **removed** from the list,
and nothing replaces them. What the round established per-ID comes from
`T-INT-02`'s own invariant text — an in-engine replay needs the replayer
compiled into the engine, and so vendored — while the imported tables are named
by §4.9's parity stub `Inputs` line, which is stub-level: the stub governs
`T-INT-01` through `T-INT-05`, and this draft records `T-INT-01` and `T-INT-04`
green at `e19605e` over a tree in which Pair 15 measures those tables absent.
Attaching that line to this assertion is therefore an inference, and change
request 4 carries the question instead. The removal costs nothing, because the
list never claimed to be complete. The sentence's own opening clause is
reproduced verbatim, and the clauses ahead of it in the same sentence — that
`T-SAVE-06` is the only † of row 10's seven, that it is asserted jointly with
`T-INT-02`, and that no in-editor Automation harness exists — are untouched and
still true; the second of them is the premise this repair reasons from. The
`T-SAVE-07` sentence that follows is untouched.

---

### Pair 20 — §4.11, row 10's cell: the same universal, at the build-order site

**OLD**

**`T-SAVE-06` is now the only ID this row lacks**, so its set closes on the editor pass alone (§3).

**NEW:**

**`T-SAVE-06` is now the only ID this row lacks**, and among what that ID waits on are the in-editor Automation harness and a vendored replayer: `T-SAVE-06` is asserted jointly with `T-INT-02`, whose replay runs **in-engine**, so the replayer has to be compiled into the engine and therefore vendored, and `Replay` is ruled out of vendoring until a bridge consumer exists. Whether *the editor pass* is meant to carry those subjects is not ruled here (§3).

*Note.* Same defect as Pair 19 at the build-order site, and the same repair.
**Rewritten after gate run `ue-harness-5`:** *its set closes on the editor pass
alone* was first replaced by *its set closes on the harness together with a
vendored replayer*, which is a sufficiency claim, so the form became
non-exhaustive. **Rewritten again at this pass**, for the reason Pair 19's note
now gives: the §4.8 tables imported in-editor are removed from the list, and
nothing replaces them. The clause ahead of it — `T-SAVE-06` being the only ID the
row lacks — is unchanged and unaffected: this pair changes what that ID waits
on, and not which IDs the row still lacks. The cell's `†` marking, its `Yes, all
but slot I/O` headless column and its `T-SAVE-01..07` acceptance list are
untouched, and the sentence that follows — slot I/O being week 5 with no
headless gate waiting on it — is untouched and still true.

---

### Pair 21 — §4.5, the risk row: the third site carrying the same universal

**OLD**

leaving `T-SAVE-06` on the in-editor Automation harness, which is now the whole of what row 10 lacks (§3)

**NEW:**

leaving `T-SAVE-06`, among what it waits on being the in-editor Automation harness and a vendored replayer — it is asserted jointly with `T-INT-02`, whose replay runs **in-engine**, and `Replay` is ruled out of vendoring until a bridge consumer exists (§3)

*Note.* **Filed as a sibling, not as one of the two sites gate run
`ue-harness-4` named.** The sweep for this defect was run over the claim rather
than over the two quoted strings, and this §4.5 risk-row cell carries the same
universal in a third form — *the whole of what row 10 lacks* — so repairing only
the two named sites would have left the document asserting the falsified claim
once more. **Amended after gate run `ue-harness-5`**, and **again at this
pass**, each time to the exact wording its siblings carry, so that these
sentences do not differ from each other in what they appear to quantify over:
first the non-exhaustive *among what it waits on* form, and now the removal of
the §4.8 tables imported in-editor, for the reason Pair 19's note gives. What
the cell says before this clause is untouched and unaffected: row 10's other
`T-SAVE` IDs, the commits they closed at, and the observation that part (b) ran
over the command set part (c) requires, are all outside this block and none of
them turns on what `T-SAVE-06` waits on. The `†` cut-line text that begins the
next cell is outside this block too.

---

### Pair 22 — §4.5, the risk row: the same universal, for row 8

**OLD**

they are now the whole of what row 8 lacks, so its flip waits on the editor pass alone;

**NEW:**

they are the IDs row 8 still lacks, and among what its flip waits on are an in-editor Automation pass and the real Stratocracy widgets `T-UI-03` and `T-UI-04` assert against, which are measured absent at `a13626f` (§4.9);

*Note.* **Filed by gate run `ue-harness-5` as a sixth site of this family, one
clause earlier in the very cell Pair 21 edits.** The claim is the same shape as
Pairs 19–21's and false the same way: §4.9 part 2's decomposition (Pair 15)
records that `T-UI-03` and `T-UI-04` need real Stratocracy widgets, and measures
every tracked widget asset at `a13626f` as belonging to the
`AdvancedTurnBasedTileToolkit` marketplace content or to the UE template. Two
claims are separated here rather than merged, because only one of them was
false: **which IDs row 8 lacks** is `T-UI-03` and `T-UI-04`, which is unchanged
and unaffected by anything this round, and **what row 8's flip waits on** is
what the universal got wrong. The clauses ahead of this one in the same
sentence — that both IDs are written, unblocked and asserting, and that no
in-editor pass exists at either of row 8's two commits — are untouched and
still true, and the row-9 clause that follows the semicolon is outside this
block. This pair moves no count: row 8's unclosed set is the same after it as
before. **Amended after gate run `ue-harness-7`:** the section pointer read
`(§3)`, and the `a13626f` widget measurement it points at is carried by Pair
15, whose target is §4.9 part 2. §3's own row-8 sentence — Pair 23's NEW —
names the widgets but not the measurement, so it does not discharge the
pointer either. The pointer now reads `(§4.9)`, where the measurement lands;
the clause is otherwise unchanged, and it did not move at this pass.

---

### Pair 23 — §3, the ledger's unclosed-ID list: row 8's universal at its second site

**OLD**

those two wait on a harness, and they are now the whole of what row 8 lacks.

**NEW:**

among what those two wait on are a harness and real Stratocracy widgets, and they are the IDs row 8 still lacks.

*Note.* A sibling of Pair 22 found by this round's claim-shape sweep rather
than by searching for an identifier: it is the same universal about row 8, in
§3's unclosed-ID list rather than in §4.5's risk row, and the two sites use
different wording for it. It is not enclosed by a commit-pinned landing record —
the list it sits in is written about the document's present — so it does not
survive on the pin the §3 landing records rely on. Repaired to the same
non-exhaustive form, with the ID-set claim kept because it is true. The
`T-DATA-05` sentence that follows is untouched. This block names the widgets
and states no measurement of them, which is what Pair 22's pointer repair
turns on.

---

### Pair 24 — §4.11, the row-8 paragraph: row 8's universal at its third site

**OLD**

so the in-editor
pass is now the whole of what this row still lacks and the row stays
unflipped on it.

**NEW:**

so the IDs this
row still lacks are `T-UI-03` and `T-UI-04`, and among what the row's flip
waits on are an in-editor Automation pass and the real Stratocracy widgets
those IDs assert against (§3), the row staying unflipped on them.

*Note.* The third site of the row-8 universal, in §4.11's row-8 paragraph,
found by the same claim-shape sweep. The sentence ahead of it — `T-UI-05` being
green at `41a1452`, the rebuild at which the snapshot additions ruled beside it
were built — is reproduced up to its comma and is unchanged, and the **Row 9's
headless half has since landed** sentence that follows is outside this block
and is Pair 16's subject. This pair moves no count. Its `(§3)` pointer is for
the widgets the IDs assert against, which Pair 23's NEW puts in §3's
unclosed-ID list; it claims no measurement there, and it did not move at gate
run `ue-harness-7` or at this pass.

---

### Pair 25 — §3, the `41a1452` landing record: the row-8 universal inside a landing record

**OLD**

before this commit the editor pass was not the whole of what the row lacked, because `T-UI-05` was headless and unimplemented, and now it is

**NEW:**

before this commit the IDs the row lacked included `T-UI-05`, which was headless and unimplemented, and after it the IDs it lacks are the in-editor `T-UI-03` and `T-UI-04`

*Note.* The fourth site of the row-8 universal. It is enclosed by a
commit-pinned landing record, so its *now* reads as *at this commit* rather
than as the reader's present — but the universal it asserts is the same one
Pairs 22–24 repair, and leaving it would put the claim and its repairs in the
same document. What the landing record actually established is kept: at
`41a1452` the snapshot additions and `T-UI-05` were built, so the IDs row 8
lacks after it are the two in-editor ones. The clause is rewritten to state
**which IDs** the row lacks — a claim that is true, that no pair in this file
changes, and that quantifies over IDs rather than over blockers. The sentence
after the em dash, on the row keeping its partial pass, is outside this block
and is untouched, as is the earlier sentence in the same record saying that
what row 8 lacked after `7c36303` was no longer the in-editor pass alone: that
is a **negation** of the universal at an earlier commit, and it stays true.

---

## Arithmetic

One count moves: §4.5's distribution of green IDs by commit. The total does
not.

| Commit | Before | After |
|---|---|---|
| `b23823f` | 1 (`T-INT-04`) | — |
| `d837fc8` | 1 (`T-INT-01`) | — |
| `e19605e` | — | 2 (`T-INT-01`, `T-INT-04`) |

Every other addend in that enumeration is untouched: `c224825` 18, `647d4df`
9, `ad77b13` 9, `d8284f1` 6, `9086d6a` 7, `6ccd40b` 1, `7c36303` 2, `41a1452`
1, `737f666` 1, `ec15be6` 4, `1ee890e` 1. Before: 18 + 9 + 9 + 6 + 7 + 1 + 2 +
1 + 1 + 1 + 1 + 4 + 1 = 61. After: 18 + 9 + 9 + 6 + 7 + 1 + 2 + 1 + 1 + 4 + 1
+ 2 = 61. The stated totals — written 71, green 61, unclosed 10 — do not move,
and §4.5's per-row unclosed figures do not move: row 9's unclosed set is still
`T-INT-02`, `T-INT-03`, `T-INT-05`, and row 10's is still `T-SAVE-06`.

Pair 6 moves no count. It names a further sha in an enumeration that carries
no tally, and Pair 1 adds no addend to anything: both are commit citations.
Pair 18 moves no count either: it deletes a quantifier and states no figure.
Pairs 19, 20 and 21 move no count: each changes what one unclosed ID waits on,
and none changes which IDs are unclosed, so row 10's unclosed set is still
`T-SAVE-06` and every figure above is the same after them as before. Pairs 22,
23, 24 and 25 move no count for the same reason on the other row: each changes
what row 8's flip waits on, none changes which IDs row 8 lacks, and row 8's
unclosed set is still `T-UI-03` and `T-UI-04` — the figure §4.5 states for it
is unchanged, and no green, written or unclosed total is touched. Pair 15's
amendments move no count either: they repair its anchor sentence, widen an
umbrella over a list of subjects, and delete a clause about what an `Inputs`
line binds, and none of that states a figure or changes a row's ID set. Pair
22's `ue-harness-7` amendment moves no count: it changes a section pointer. The
change made at this pass moves no count either: it removes a named subject from
a list of what an unclosed ID waits on, states no figure, and leaves every ID
set above as it was.

## Check results

- Each OLD block was searched against `source/gdd.md` and matched exactly one
  site. Three candidate anchors were widened after failing that test: `` `1ee890e`
  is cited as a commit, and this line makes no claim `` matched twice, so Pair
  1's OLD was widened to begin at *This draft stands at 2026-08-05*;
  *close as soon as vendoring lands* was checked against the near-identical
  *closing as soon as vendoring lands* in the row-9 paragraph before Pair 17
  was anchored on it; and *they are now the whole of what row 8 lacks* matched
  **twice** — §3's unclosed-ID list and §4.5's risk row carry it verbatim — so
  Pair 22's OLD carries its trailing *so its flip waits on the editor pass
  alone;* and Pair 23's carries its leading *those two wait on a harness, and*,
  each of which then matched one site.
- No OLD block moved at gate run `ue-harness-7`, and none moved at this pass
  either. The repairs at both passes are inside NEW blocks — Pair 15's and Pair
  22's then, Pairs 5, 19, 20 and 21's now — so every anchor above stands as it
  was probed.
- Pair 15's OLD is unchanged by this pass and was re-probed: it stands at line
  2820 of `source/gdd.md` and matches one site. What changed is its NEW block,
  which no longer reproduces it.
- Pair 6's OLD was probed as a whole sentence, from its bold opening through
  *(ruled 2026-08-05).*, and matched exactly one site. The passage it sits in
  was read whole, sentence by sentence, before the pair was written: the
  sentence before it confines its own 2026-08-05 ruling to itself and points at
  the §3 status line, and the sentences after it replace the
  `master`-reachability form, confine this parenthetical's ruling the same way,
  explain why the split across repos is structural, and then turn to the
  separate matter of bare file citations that did not resolve. None of those
  changes with the further sha named, and none carries a tally.
- Prose probes were run against a whitespace-collapsed view, because the
  §4.9 and §4.11 passages are hard-wrapped and the §3 and §4.5 passages are
  not; the §4.9 anchor for Pair 14 returns nothing on a single-line probe and
  had to be matched across the wrap, and Pair 24's anchor in §4.11 spans three
  wrapped lines and is reproduced with that wrap.
- **Every section pointer in this file was grepped against `source/gdd.md`
  before it was left standing**, each against the heading it names and the
  content it claims is there: §3's ledger narrative, its unclosed-ID list and
  its outside-the-crew-repo parenthetical, which carry the anchors Pairs 1–6,
  19, 23 and 25 use; §4.4's milestone table, which carries Pair 7's week-2 cell;
  §4.5's risk row, which carries the green distribution, the closure convention
  stated once there, row 9's second naming of its closed IDs, and Pairs 21 and
  22's clauses; §4.7's preamble, which carries the gate-plan stubs and a *pure
  C++17* site; §4.8's schema section, whose tables the parity stub requires
  imported in-editor; §4.9's parts 1 and 2, which carry the module layout, the
  ten-module enumeration, the three unvendored modules, the other *pure C++17*
  site, the integration parity stub and the harness paragraph; §4.10's format
  section, which enumerates the Balance Analyst self-play log among the format's
  consumers and carries `T-SAVE-06`'s invariant text; and §4.11's row-8 and
  row-9 paragraphs, its row-9 dependency cell and its row-10 cell. Two pointers
  failed that check and were corrected: the language-standard change request had
  named §4.1, which names no language standard, and an earlier revision of this
  bullet placed `T-SAVE-06`'s invariant text in §4.7, where **no `T-SAVE-06`
  occurs at all** — it stands at line 2972, inside §4.10.
- **A third pointer failed at gate run `ue-harness-7`, and the whole set was
  re-grepped after it was fixed.** Pair 22's clause cited `(§3)` for the
  `a13626f` widget measurement; the block that carries that measurement is Pair
  15's, whose target is §4.9 part 2, and §3's row-8 sentence — Pair 23's NEW —
  names the widgets without measuring them, so it does not discharge the
  pointer. Pair 22 now cites §4.9. The pointers this file's NEW blocks carry
  after that change are **§3, §4.5, §4.8, §4.9 and §4.10**, and each was
  re-checked against what the citing clause claims stands there: §3 for the
  landing narrative Pairs 8–14, 17 and 20–21 cite and for the widgets Pair 24
  cites, which Pair 23's NEW puts in §3's unclosed-ID list; §4.5 for the
  closure convention Pairs 3 and 16 cite and for the green figures Pair 5
  cites; §4.8 for the schema tables Pair 15 names in the stub's `Inputs` line;
  §4.9 for the ten-module enumeration and the parity stub Pair 5 cites, and for
  the `a13626f` measurement Pair 22 now cites; and §4.10 for the canonical state
  hash Pair 19 cites, the replay file Pair 15 names, and the Balance Analyst
  log Pair 5 cites among the format's consumers. **This pass drops a §4.8
  pointer from Pairs 5, 19, 20 and 21 and adds none**, the imported tables
  having been removed from those blocks; §4.8 is still carried, by Pair 15's
  `Inputs` sentence, so the pointer set above is unchanged.
- **The sweep, run this pass over the claim's MEANING rather than over its
  vocabulary.** Every earlier pass probed a token set — *alone*, *the whole of
  what*, *waits on*, *closes on*, *all that remains*, *what remains is* — and
  each of those passes found a site spelled without the tokens it had probed,
  so the probe itself is what kept failing. The tell used this pass is **a
  definite article or a superlative doing sufficiency work**, and the question
  put to every candidate sentence is whether it says the editor pass, or the
  harness, is the last thing needed. Read that way, the family this round
  repairs — a sentence saying what an unclosed ID or an unflipped row is waiting
  for — takes in §3's unclosed-ID list (Pair 23), §4.11's row-8 paragraph (Pair
  24), §3's `41a1452` landing record (Pair 25), the row-8 site gate run
  `ue-harness-5` filed (Pair 22), the three repaired before it (Pairs 19, 20,
  21), and **§4.9 part 2's own *the remaining blocker* at line 2820** — Pair
  15's anchor, which every token probe had passed over and which gate run
  `ue-harness-6` filed. The meaning tell was then re-run over the whole
  document and surfaced no further member, which is why each site is repaired
  where it stands rather than replaced by a single statement the others cite:
  the citing structure is the right answer to a family that keeps growing, and
  this sweep is the first that did not grow it. Gate run `ue-harness-7`
  enumerated the family's sites independently and found each of them repaired
  by a pair here.
  Every other hit was judged and left as written: the `Acceptance:` lines of the
  §4.9 and §4.10 stubs, where
  *in the editor pass* is a schedule bucket and not a blocker set; the `†`
  cut-line note's *an editor pass cut to its marked IDs alone would still owe
  T-INT-03*, which asserts the opposite of a sufficiency claim; the `†` cut
  line's *its only unique coverage is an in-editor Automation pass*, which
  quantifies over an ID's coverage and not over a row's blockers; row 10's
  *T-SAVE-04 ... closes on it alone*, whose subject is part (a)'s format spec
  and which names no editor-pass subject; row 10's *`T-SAVE-06` waits on the
  in-editor Automation harness and `T-SAVE-07` on a self-play log written in
  this format*, which names a blocker without quantifying over the set and is
  pinned to part (b) by the *has since landed* sentence after it; §4.4's *One
  still waits: `T-SAVE-06`, on the in-editor Automation harness it is asserted
  jointly with `T-INT-02` on*, the same; §4.11's `†` list, *T-INT-02, 05 and
  T-SAVE-06 — the in-editor half of the parity pair*, whose parenthetical
  already records the joint assertion; the Balance-module record's *the
  in-editor Automation harness `T-SAVE-06` waits on is untouched by it*, a
  relative clause whose subject is that landing; row 10's *what it waits on is
  `T-SAVE-06` alone*, whose subject is the row and whose claim is over IDs;
  §4.11's *T-UI-05 is the sole assertion that the snapshot tells the truth*,
  which says what one ID covers and not what any row waits on; §3's *Row 8 was
  the last unbuilt link on §4.11's critical path*, a superlative over build-order
  rows that is pinned to its landing and true there; and §3's *what row 8 lacked
  after this commit was no longer the in-editor pass alone*, which is a negation
  of the universal and stays true. Every remaining *alone* in the document was
  read and belongs to §2's rules prose or to a fixture description, quantifying
  over nothing in this family.
- **The two sentences immediately ahead of Pair 15's anchor were judged under
  the same tell and left as written**, and the judgement is recorded because
  they sit inside the passage this pair repairs. *It waits on **an in-editor
  Automation harness*** names a blocker under an indefinite article and
  quantifies over nothing, and *The other blocker recorded here was §4.10's
  canonical state hash* is scoped by *recorded here* to what the document had
  recorded at that point, which is what it says and is true. With the anchor
  repaired, neither sentence any longer stands beside a claim that the harness
  is the last thing needed, and Pair 15's own NEW text is what follows them.
- The sweep was generated sentence-first over five subjects — registration and
  build status, the two `T-INT` closures, the vendored set's definition, what
  the editor pass waits on, and what row 8's flip waits on — and every sentence
  found was read whole.
  It surfaced one site nobody had filed on an earlier pass: §4.5's second naming
  of row 9's closed IDs, *its other two having closed — T-INT-04 at `b23823f`,
  and T-INT-01 at `d837fc8`*, which is Pair 10.
- **The §4.9 module-layout paragraph was then re-read end to end, sentence by
  sentence, rather than by term**, which is how Pair 18's sentence was found:
  it is a sibling of Pair 12's edit, not part of it, and no term-level probe
  for a commit, an ID or a module name reaches it. Every other sentence in that
  paragraph was judged individually and left as written — the canonical sources
  and the gate's compiler detection; the vendoring mechanism and `rulesCommit`;
  the ten-module enumeration with `StratRules.Build.cs` and the manifest that
  has no counterpart; *`T-INT-01` states what each of those two states
  requires*, whose text did not change this round; the unchanged vendored names
  and the absent rename map; `Driver` being non-optional because `Ai.good.cpp`
  links against it, which the C4456 in `Driver.good.cpp` does not disturb;
  *Nothing else is vendored* and its `main()` reasoning, which Pair 12 appends
  to rather than contradicts; the eleventh, twelfth and thirteenth-module
  clause, which agrees with the declaration's partition; the absent bridge and
  the unbuilt §4.9 part 2, which Pair 15 measures again at `a13626f`; *vendoring
  now would re-date `T-INT-01`'s and `T-INT-04`'s closures*, which remains true
  of a future vendoring; the `selfplay.cpp` exclusion; the *pure C++17*
  sentence, which is filed as a change request below and deliberately not
  edited; and the closing standalone-gate sentence, which Pair 14 reproduces
  verbatim as its anchor.
- **§4.9's integration parity stub was read as a stub, `Inputs` line first.**
  It requires *vendored StratRules sources + recorded source commit; a §4.10
  replay file; the §4.8 tables imported in-editor*. The stub governs `T-INT-01`
  through `T-INT-05`, and its own `Acceptance` line splits them between the
  gate run and the editor pass. **Amended after gate run `ue-harness-7`:** Pair
  15 had said that line binds the invariants the stub governs, `T-INT-03` and
  `T-INT-05` among them — which this draft's own record refutes, `T-INT-01` and
  `T-INT-04` being recorded green at `e19605e` over the tree in which Pair 15
  measures those tables absent. A shorter list of bound IDs would assert a
  binding this round did not establish, so none is written: Pair 15 now names
  the line as what the stub draws on and attaches it to no invariant.
  **Extended at this pass to the same attribution one level down.** Pairs 5,
  19, 20 and 21 each named the imported tables among the inputs of the joint
  `T-SAVE-06`/`T-INT-02` assertion, which attaches the stub-level line to a
  particular assertion — the same inference the `ue-harness-7` repair declined,
  and one the round did not establish. The phrase is **removed** from those four
  blocks and nothing is put in its place: their lists are non-exhaustive, so
  dropping a subject asserts nothing about what remains. What stays in them is
  what `T-INT-02`'s own invariant text establishes — an in-engine replay needs
  the replayer compiled into the engine, and so vendored — together with the
  harness. Change request 4 carries the per-ID question. The stub's
  `Determinism` and `Acceptance` lines are untouched by every pair here.
- Three present-tense passages were judged individually against the pin test
  and left as written, because a commit-pinned landing record encloses each:
  *`T-INT-01` and `T-INT-04` still pass 2/2 at `rulesCommit` `d837fc8` after
  this module landed* (the `ec15be6` record); *still 2/2 at `rulesCommit`
  `d837fc8`, run this session after the change* (the `1ee890e` record); and
  *Nothing was compiled by UBT at this landing, no editor was launched, and no
  UE project file was touched* (the `1ee890e` record, whose scope is that
  landing and which the `a13626f` build does not reach). Pair 25's clause is
  enclosed by a pin in the same way and is **not** left as written: the pin
  governs when a claim is true, and this one is of the shape that is false at
  its own commit too.
- Q33's register row was read whole and left unedited: it records a ruling
  made at `d837fc8` about a check that asserted **less** than its text, and
  this round's defect is the opposite direction. The open-question register
  gains no row and loses none, and the judgement Pairs 15 and 19–25 leave
  unruled is filed as a change request below rather than written into the
  register.
- Both passages naming what the UBT build does not establish — Pair 5's in §3
  and Pair 14's in §4.9 — were re-read whole after the wording of either
  changed, because each pair's own sentences are the nearest siblings of the
  other's. Each states the `BuildSettingsVersion` mechanism and the C4456 that
  stopped the first attempt, and each is confined to those: the C4457 both
  builds printed was a warning throughout, so the round's own logs are what
  rule out any claim about shadowed diagnostics as a class.
- **Pair 5's NEW block was re-read end to end after each amendment, this pass's
  included**, and the sentence recording `T-SAVE-06`'s status is the only one in
  it that has moved at any of them. The sentences either side of it — the
  register of open questions gaining no row and losing none, and
  `cpp_reference/selfplay.cpp` being untouched — are unchanged and unaffected,
  and the amendment states no figure, so the *Arithmetic* reconciliation above
  is unaffected by it.
- **Pair 15's NEW block was re-read end to end after the last pass's amendment,
  and again at this one, at which it did not move.** The per-ID list is
  unchanged in what it names, the `a13626f` measurements are unchanged and still
  attach to the subjects that list names, the closes-no-acceptance-ID sentence
  and the `Source/StratRules/` location constraint are unchanged, and the
  parity-stub `Inputs` line — a sentence of its own — ends at what the stub
  draws on and at the tables' absence from the assets measured in the sentence
  before it. Pairs 5, 19, 20 and 21 cited that line and no longer do: the
  imported tables are removed from each of them at this pass, so Pair 15 is
  where this file names the line, as what the stub draws on.
- **Pairs 5, 19, 20 and 21 were re-read end to end after this pass's removal.**
  In each, the subject list now names the in-editor Automation harness and a
  vendored replayer, the reason clause that follows names the joint assertion
  with `T-INT-02`, the in-engine replay and `Replay`'s deferred vendoring, and
  the parity-stub clause is **deleted rather than reworded**. The *among what it
  waits on are* form is unchanged, no cardinal is stated for any of those lists,
  and the text on either side of each edited sentence is unchanged: Pair 5's
  neighbours in the ledger narrative, Pair 19's reproduced opening clause and
  its `T-SAVE-07` successor, Pair 20's *only ID this row lacks* clause and the
  slot-I/O sentence after it, and Pair 21's other row-10 `T-SAVE` clauses and
  the `†` cut line beyond the cell. Each pair's `(§3)` or *not ruled here*
  ending is unchanged.
- **Pair 22's NEW block was re-read end to end after the last pass's
  amendment.** The two claims it separates are unchanged — which IDs row 8
  lacks, and what its flip waits on — the non-exhaustive *among what … waits on
  are* form is unchanged, the `a13626f` measurement clause is unchanged in what
  it asserts, and the section pointer is the only text that moved. It did not
  move at this pass.
- **No sentence written or amended this pass says that the editor pass, or the
  harness, is the last thing needed.** The test applied is the meaning tell
  above rather than a token list, because a token list is exactly what let *the
  remaining blocker* stand inside this file's own NEW block through five gate
  runs. Each repaired site names subjects under *among what … waits on are …*,
  claims no completeness for the list, and states no cardinal for a blocker set;
  and the umbrella sentence over each such list was read the same way, which is
  how Pair 15's was found. Removing a subject from such a list leaves the form
  as it was: *among* was never a promise that the list was complete.
- **And no sentence in this file attributes the parity stub's `Inputs` line to
  an invariant, at any width.** The `ue-harness-7` repair deleted that claim
  from Pair 15 rather than narrowing it, on the ground the gate gave —
  narrowing the list of bound IDs is the same defect one level down — and this
  pass extends the same treatment to Pairs 5, 19, 20 and 21, which had attached
  the imported tables to the joint `T-SAVE-06`/`T-INT-02` assertion. In each the
  phrase is removed rather than replaced. What Pair 15 states is what the line
  lists and where the tables stand at `a13626f`, and change request 4 carries
  the per-ID question.

## Filed change requests

1. **Language standard.** UBT compiles these sources as C++20 with MSVC strict
   conformance (`BuildSettingsVersion.V4` onward), while the standalone gate
   compiles them as C++17 — the same bytes under two language standards.
   Located by grep rather than by memory, the phrase *pure C++17* occurs in
   **§4.7**'s preamble, where all rules code is described as headless —
   `namespace strat`, pure C++17, zero engine dependencies — and in **§4.9**
   part 1, where `StratRules` is described as carrying no engine headers, no
   UObject and no third-party includes, *pure C++17 in `namespace strat`*, and
   nowhere else; §4.1 names no language standard at all, so there is nothing
   to reword there. Both compile clean, so this is a wording question and
   **not** a finding about the sources. No pair above changes either sentence
   — Pair 14's anchor reproduces the tail of the §4.9 one verbatim and leaves
   it as written — and the Director owns the wording.
2. **The in-editor Automation harness has no calendar owner.** Giving it one
   was considered this round and **declined**, on the ground that its own
   dependencies are unscheduled and a milestone scheduled ahead of its
   dependencies is the seam this document has already repaired more than once.
   Filed so the absence is a decision on the record rather than an oversight.
3. **What does *the editor pass* denote — the harness, or the harness plus
   whatever subjects its IDs need?** The document uses the phrase both ways, and
   that is the judgement to make; the vendoring deferral is one consequence of
   it rather than the whole question.

   **The permissive reading is in force for row 8.** §3's unclosed-ID list,
   §4.5's risk row and §4.11's row-8 paragraph all said row 8's flip waits on
   *the editor pass*, while §4.9 part 2's decomposition records that `T-UI-03`
   and `T-UI-04` need real Stratocracy widgets and measures every tracked widget
   asset at `a13626f` as marketplace or template content. Read permissively
   those sentences were true, because *the editor pass* silently included
   building the widgets.

   **The strict reading is in force for row 10.** `T-SAVE-06` is asserted
   jointly with `T-INT-02`, `T-INT-02` replays a log in-engine, an in-engine
   replay needs `Replay` vendored, and `Replay` is ruled out of vendoring until
   a bridge consumer exists. Read strictly, *the editor pass* is the harness and
   those subjects are separate work.

   **Taking one reading on one row and the other reading on the other row is
   the defect**, and it must be resolved **once, either way**. Under the
   permissive reading, *the editor pass* is defined in the document as a
   milestone that carries every subject its IDs need — vendoring `Replay`,
   importing the DataTables `T-DATA-05` needs, and building the widgets — and
   change request 2's missing calendar owner has to cover all of that. Under the
   strict reading, the harness and each subject are separate gates that have to
   be scheduled separately, and every row's cell has to say which it waits on.

   Pairs 15 and 19–25 state the decomposition **non-exhaustively** and settle
   nothing beyond it, on both rows, so that the document says the same thing
   about row 8 and row 10 while the question is open. **Nothing in this file
   phrases the question away**, which is the failure mode a draft has here: an
   author who picks either reading in prose has made the ruling rather than
   filed it, and an author who replaces one exhaustive list with a shorter one
   has made a claim the round did not establish.
4. **Which of the parity stub's invariants require the §4.8 tables imported
   in-editor?** The stub's `Inputs` line names them; the stub governs
   `T-INT-01` through `T-INT-05`; and `T-INT-01` and `T-INT-04` are green at
   `e19605e` over a tree in which those tables are measured absent, so the line
   is not a requirement of each of them. Nothing in this file answers the
   question either way: Pair 15 names the line as what the stub draws on, and
   the pairs that had attached the tables to the joint `T-SAVE-06`/`T-INT-02`
   assertion no longer name them, so the per-ID reading is left to the Director
   rather than written into §4.9 or §3. This is adjacent to change request 3:
   under the permissive reading of *the editor pass* the question may not need a
   separate answer, and under the strict reading each in-editor ID has to say
   whether the imported tables are among its own subjects.

## Grounding

- Commits, ancestry and the four changed UE project files: facts §1.
- The ancestry Pair 1 now states against `031ee20`: facts §9a.
- Pair 6's measurement: `git cat-file -e` was run in the crew repo per sha on
  `99fcb84`, `9dec48c` and `a13626f`, each of which fails to resolve there,
  with `e19605e` resolving under the same command as the control: facts §9a,
  which records the probe for all three shas.
- Registration, the `StratocracyEditor` build, the C4456 diagnostic, the
  `BuildSettingsVersion` reading, the scoped warning setting, the C4457 that
  printed as a warning in both builds, the explicit list of what the build does
  **not** establish, and the framing of the MSVC compile through UBT as a
  toolchain configuration rather than a second compiler — the standalone gate
  already compiling these sources under clang++ and MSVC both: facts §2.
- The `T-INT-01` check defect, the `git ls-tree` derivation, the `30a73f0`
  measurement, the `rulesCommit` consequence, and the `vendored_set.json`
  repair with its partition requirement: facts §3.
- The 2/2 result, the verbatim PASS line, the accepted `--week1` record and its
  per-row tallies, the known-bad inputs and their verdicts, the working-tree
  design control, and the invalid-then-redone no-source control: facts §4.
- The two closure movements, each with its own reason, and the statement that
  no ID is minted and none closes: facts §5.
- Ruling X (declared, not inferred; text unchanged), Ruling Y (distribution
  reporter), Ruling Z (`openActiveTurn`), and the two declined phrasing rules:
  facts §6.
- Change requests 1 and 2, and the located sites of the phrase *pure C++17*:
  facts §7, confirmed by grep against `source/gdd.md` for the section each
  site falls in.
- The editor-pass decomposition per ID, the widgets `T-UI-03` and `T-UI-04`
  need, the DataTables `T-DATA-05` needs, and the `a13626f` measurements of
  `EUnitType`, `UENUM` and the tracked assets: facts §8.
- **Pairs 19, 20, 21, 22, 23, 24 and 25, Pair 5's amended sentence, and Pair
  15's amended umbrella and repaired anchor, and change request 3: facts §8a**,
  which records that `T-SAVE-06`
  is asserted jointly with `T-INT-02` in six places in the master, that
  `T-INT-02` replays a log in-engine and so needs the replayer vendored, that
  `Replay` is deliberately unvendored on a ruling, that the decomposition
  **must be stated non-exhaustively** rather than as a narrower universal, that
  this family **must be swept by meaning rather than by vocabulary**, the tell
  being a definite article or a superlative doing sufficiency work, that the
  document takes the permissive reading of *the editor pass* for row 8 while
  taking the strict reading for the vendoring, that the defect predates this
  round, and that the judgement belongs to the Director and must be filed
  rather than made. The seven OLD blocks those pairs replace are quoted from
  `source/gdd.md`, each matched there exactly once, as is Pair 15's, at line
  2820.
- **Pair 15's `ue-harness-7` deletion, this pass's removal of the imported
  tables from Pairs 5, 19, 20 and 21, and change request 4: facts §8a's closing
  paragraphs**, which supersede anything earlier in that file attributing the
  imported tables to `T-INT-02`. They record that the harness and a vendored
  replayer are established per-ID from `T-INT-02`'s own invariant text, which is
  why those two stay in each list; that the §4.8 tables imported in-editor are
  **not** established as a requirement of `T-INT-02` or of any other single
  invariant, the phrase coming from the stub-level `Inputs` line; that the stub
  governs `T-INT-01` through `T-INT-05` and that `T-INT-01` and `T-INT-04` are
  green at `e19605e` over a tree in which those tables are measured absent; and
  that the line is therefore to be named as what the stub draws on rather than
  attributed to any invariant, at any width, the per-ID question belonging in a
  change request.
- The parity stub's `Inputs` line as quoted in Pair 15: `source/gdd.md` §4.9's
  integration parity stub, read at the stub itself; that the stub governs
  `T-INT-01` through `T-INT-05` and that its `Acceptance` line splits them is
  read from the same stub and from the §4.9 sentence immediately above it, and
  no pair here draws a binding from either.
- **Pair 22's section pointer**: the `a13626f` widget measurement it cites is
  the sentence in Pair 15's NEW block that measures every tracked DataTable and
  widget asset as marketplace or template content, and Pair 15's target is
  §4.9 part 2 — read in this file, pair by pair, after gate run `ue-harness-7`
  reported the `(§3)` pointer dead.
- `T-SAVE-06`'s invariant text and the section it stands in: `source/gdd.md`
  §4.10's save-and-replay format section, located by grep; §4.7 carries no
  `T-SAVE-06`.
- The `Source/StratRules/` harness-location constraint and the
  cannot-fix-in-place constraint: facts §9.
- No ledger row moves, no register row moves, `selfplay.cpp` untouched, and the
  three modules staying unvendored: facts §10.
- Pair 18's subject: the sentence stands in `source/gdd.md` §4.9 part 1,
  immediately after the passage Pair 13 replaces and in the same paragraph as
  Pair 12's; that Pair 12 adds a further ruling to that paragraph is the
  content of Pair 12's own NEW block, and the ten modules the enumeration names
  are the `vendored` list of `ue_module/vendored_set.json`, facts §3.
- The two sentences ahead of Pair 15's anchor that were judged and left — *It
  waits on an in-editor Automation harness* and *The other blocker recorded
  here was §4.10's canonical state hash* — stand at `source/gdd.md` lines
  2815–2816, read in place.
- Master text quoted in every OLD block: `source/gdd.md` §3's ledger narrative,
  its unclosed-ID list and its outside-the-crew-repo parenthetical, §4.4's
  week-2 cell, §4.5's green enumeration and risk row, §4.9 parts 1–2, and
  §4.11's row-8 paragraph, row-9 paragraph, row-9 dependency cell and row-10
  cell.
