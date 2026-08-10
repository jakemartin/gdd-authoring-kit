# Fact block — round `deletion-recorded`

One file. The author and the gate are both given this path and nothing else as
supplied fact. It is appended to, never trimmed.

**If a fact in this block looks wrong, say so instead of writing around it.**
In an earlier round three blocking findings were facts of mine that the gate,
holding the same block, was structurally unable to challenge; in the last round
the author overruled one of my claims and was right. Only the author can be this
block's adversary. Ask of every claim here: *true of what, exactly, and at which
commit?*

---

## 0. What the round is

The Director has ruled: **record the deletion at crew `b5f524d`.**

§3 records that the fourteen false closure clauses `9289c1d` introduced exist and
are false. It does not record that they have since been deleted. The record is
written in the present tense with no pin to a tree state, so the part of it that
asserts those clauses *exist* has gone false at the crew tip. The round amends
that record. It closes nothing and moves no count.

`source/gdd.md` md5 `8c738e860a403d254af0317533b23c75`, which is the master as
merged at content `769d887`.

## 1. Disambiguation — the round's own subject nouns

Not standing vocabulary. These are the words this round turns on, and the first
two name different things in different sentences of the master.

- **"the fourteen clauses"** always means the clauses `9289c1d` *introduced*,
  each asserting that `T-SAVE-06` and `T-INT-02` **closed** in the editor pass at
  UE `0897cb5`. It never means the **eleven stale claims `9289c1d` repaired**,
  which are a different set, in different files, and whose repair stands
  untouched by this round. The master describes both sets in adjacent sentences.
- **"deleted"** means the clause text was removed from the ten files. It does not
  mean a file was removed, and it does not mean the true negative beside a clause
  was removed. See §2.4.
- **"false"** — *this is the distinction the round turns on.* The fourteen were
  false when written and remain false **as propositions**: `T-SAVE-06` and
  `T-INT-02` did not close, and deleting a sentence does not make what it said
  true. What ended is their **presence in the tree**. So a claim of the form
  *"all fourteen are false"* survives, and a claim of the form *"fourteen clauses
  … assert"* does not. Amending the second must not weaken the first.
- **"the crew tip"** is `c2f5860`, not `b5f524d`. It is a moving referent and
  this round should not introduce a new sentence that depends on it.

## 2. Crew `b5f524d`, measured

Measured by reading the commit and its diff hunk by hunk, not by taking the
figures in its own message.

**2.1 The commit.** Author Jake Martin, 2026-08-08 23:19:20 -0400, subject
*"Delete the closure clauses 9289c1d asserted, under the Director's ruling"*.
It is an **ancestor of the crew tip `c2f5860`**, measured with
`git merge-base --is-ancestor`. Diffstat: **10 files, +26 / −31**.

**2.2 Fourteen clauses across ten files.** Counted per site from the diff, and
the total is the sum of these rather than a number carried in from anywhere:

| file | clauses deleted |
|---|---|
| `README.md` | 1 |
| `crew/tools.py` | 3 |
| `crew/offline.py` | 1 |
| `cpp_reference/test_replay.cpp` | 2 |
| `cpp_reference/test_save.cpp` | 1 |
| `cpp_reference/test_balance.cpp` | 1 |
| `spec/integration_spec.md` | 2 |
| `spec/replay_spec.md` | 1 |
| `spec/save_spec.md` | 1 |
| `spec/balance_spec.md` | 1 |
| **total** | **14** |

**2.3 The master's existing description of the ten files is accurate and does not
need amending on this point.** It reads *"two runner modules, three test and
harness sources, the README and four spec documents"*: `crew/tools.py` and
`crew/offline.py` are the two runner modules; `test_replay.cpp`, `test_save.cpp`
and `test_balance.cpp` the three test and harness sources; `README.md`; and
`integration_spec.md`, `replay_spec.md`, `save_spec.md`, `balance_spec.md` the
four specs. Measured against the diff's file list.

**2.4 Three dispositions, not one.** A count of fourteen does not say what
happened at each site, and three different things did:

- **Three sites also asserted "NOT open"**, which the same ruling falsifies, and
  those assertions were deleted with the closure clause:
  `cpp_reference/test_balance.cpp`, `cpp_reference/test_replay.cpp` (in `main()`)
  and `cpp_reference/test_save.cpp`.
- **Two sites carried a true description of what the bridge does with
  `data/parity_fixture.save`.** That description was **kept and re-pinned to the
  landing** rather than to a closure: `cpp_reference/test_replay.cpp` (`main()`)
  and `crew/tools.py` (`certify_week1_fn`).
- **Every adjacent true negative was kept as written.** Two survive at the tip
  and are the only sentences there pairing `T-SAVE-06`/`T-INT-02` with a closure
  word, both true: `crew/offline.py` — *"asserted jointly with T-INT-02, so it
  closes in the editor pass and nowhere headless"*; `spec/replay_spec.md` —
  *"`T-SAVE-06` does not close here … so no headless build closes it"*.

**2.5 No acceptance ID moves at `b5f524d`.** *Inferred, and here is the reason so
it can be checked rather than taken:* the vendored set is declared in
`ue_module/vendored_set.json` as twelve modules with `Balance` excluded, and a
module is a `cpp_reference/X.h` + `X.good.cpp` pair. **None of the ten files
`b5f524d` touched is a module source, and none is in the UE project repo at
all** — they are the README, two crew runner modules, three test harnesses and
four specs. So nothing `T-INT-01` accounts for, nothing `T-INT-04` compiles, and
no vendored byte changed. Under **CR-1** the counts stay **71 / 62 / 9**, row 9's
unclosed at **3** and row 10's at **1**.

**2.6 What I did not measure.** `b5f524d`'s message reports gate figures after
the deletions — a week-1 PASS, the integration gate 2/2, zero compile failures.
**I did not re-run them, and this round should not restate them.** The round
records a deletion, not a gate run. If a figure of that kind is wanted in the
master it needs a run, and that is a different round.

## 3. What stands and is not re-opened

- **CR-1 — NO CLOSURE.** `T-INT-02`, `T-INT-03` and `T-SAVE-06` ran and passed at
  UE `0897cb5` and did not close. This is what makes all fourteen clauses false,
  and `b5f524d` does not disturb it.
- `9289c1d`'s **repair of the eleven stale claims** stands, as does the master's
  record of it.
- The **two unamendable commit messages** §3 records — UE `0897cb5`'s body and
  crew `9289c1d`'s `Selfplay` naming — are unaffected. A message cannot be
  amended by a later commit, which is the point that record makes.

## 4. Error species this round must not commit

The round exists because a present-tense claim outlived its subject. Do not
repeat the shape while repairing it.

1. **No new finite present-tense claim about the crew tree's contents unless a
   commit pin encloses it.** "the tree now contains", "no file states", "the crew
   tip has" — each needs the commit it is true at, inside the clause.
2. **"has since" is not a pin.** A sentence saying the clauses "have since been
   deleted" must name `b5f524d`.
3. **Do not weaken the falsity claim into a past tense.** The fourteen *are*
   false; only their presence ended. Amending existence must leave falsity
   standing. (§1, third bullet.)
4. **Do not narrow the quantifier.** It was all fourteen, at all ten files — not
   "most", not "the closure clauses".
5. **State dispositions, not a count.** §2.4 has three outcomes; a sentence
   saying only "fourteen were deleted" hides two of them.

## 5. Adjacent, known, and not filed

§3 carries the sentence *"The tree was corrected at the crew tip; the message
cannot be."* — about the `Selfplay` naming, corrected at crew `5072d10`. "the
crew tip" is a moving referent, so the sentence is of the same species this round
is about. **It is pre-existing and none of this round's edits makes it false.**
The author may file it or leave it; if it is left, it is left knowingly, and both
agents are looking at the same fact in saying so.

## 6. What the author produces

An addendum at `sections/tech_deletion-recorded.md`, in the established form:
exact **old → new** pairs against the merged master, no section redrafted, each
pair's OLD copied byte-for-byte from `source/gdd.md`. The master is
**hard-wrapped** — any line-oriented sweep under-counts silently, so sweep
newline-insensitively and at sentence granularity.

The gate run id is `deletion-recorded`.

---

# APPENDED 2026-08-09 — corrections after gate run `deletion-recorded` (BLOCK, 2 violations)

Nothing above is edited or removed. These are corrections **in place**: where a
claim below contradicts one above, the one below governs, and the one above stays
visible so the error is legible.

## A. Correction to §2.4 — "re-pinned to the landing" has no antecedent in the master

**§2.4 above says the fixture description was "kept and re-pinned to the landing".
That phrasing is mine and it is defective for use in the master.** In this block
"the landing" was readable from context. In the master it is not: the gate
measured `parity_fixture` at **0** occurrences in `source/gdd.md`, so no landing
for that fixture is identifiable there, and §3's own convention — "do not move at
this landing", "removed by this landing", 33 occurrences of *this landing* —
resolves a bare definite article to the enclosing block's own commit, which after
merge is `b5f524d`. I verified both counts. The sentence would therefore assert
the description was re-pinned to the deletion commit, which §2.4 contradicts.

**The commit is UE `0897cb5`, the bridge landing.** Measured from `b5f524d`'s own
replacement text at both sites, which reads *"The bridge that landed at UE
`0897cb5` replays `data/parity_fixture.save` …"* — in
`cpp_reference/test_replay.cpp`'s `main()` and in `crew/tools.py`'s
`certify_week1_fn`. Any sentence entering the master must spell it.

## B. `CR-1` is a session label and is not document vocabulary

The gate measured `CR-1` at **0** occurrences in `source/gdd.md`; I confirmed it.
So a NEW cannot lean on "the same ruling" and cannot cite `CR-1` either. What the
master carries is the substance, stated in its own words at §3 — that
`T-INT-02`, `T-INT-03` and `T-SAVE-06` ran and passed and none of them closes.
How to refer to that inside the paragraph is the author's call; the constraint is
only that the referent be recoverable by a reader of the master alone.

## C. What this says about the round

Both violations are dangling antecedents in prose lifted from this block, and
neither touches what the round is for. The gate found no error species from §4,
confirmed both OLDs byte-exact and unique, and confirmed that leaving *"They ran
and passed and did not close, so all fourteen are false."* untouched is correct.

**Do not weaken a true claim to satisfy either finding.** Both sentences state
something true; each needs its referent spelled, not removed. Cutting the
`data/parity_fixture.save` disposition would drop one of the three dispositions
§4 species 5 requires, and cutting the "NOT open" disposition would drop another.
