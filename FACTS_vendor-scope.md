# Fact block — round `vendor-scope`

One file. The author and the gate are both given this path and nothing else as
supplied fact. It is appended to, never trimmed.

**If a fact in this block looks wrong, say so instead of writing around it.**
Last round one of the two blocking findings came from a defective phrasing in
this block that the author lifted in good faith; a gate handed a false fact
cannot catch it, so the author is the only adversary this block has. Ask of every
claim here: *true of what, exactly, and at which commit?*

---

## 0. What the round is

The Director has ruled: **state the five-file, three-kind scope of the vendored
data in §4.8, and reconcile §4.9's narrowing with §3.**

§4.8 rules that `dataCommit` *"advances when and only when those bytes change"*
and then illustrates it with a pair of vendorings across which **the three CSVs
are byte-identical**. §4.9 describes what `sync_stratdata.py` vendors as **"the
§4.8 CSVs"**. Read together, the illustration falsifies the rule: the bytes did
not change, and `dataCommit` advanced anyway.

The rule is in fact true. What is missing is the extent of *"the vendored
bytes"*, which the master never states. The round states it.

It closes nothing, mints no acceptance ID, and moves no count.

`source/gdd.md` md5 `8c738e860a403d254af0317533b23c75`, the master as merged at
content `769d887`.

## 1. Disambiguation — the round's own subject nouns

Not standing vocabulary. These are the words this round turns on.

- **"the vendored bytes"** is the phrase §4.8's ruling quantifies over, and it
  has no stated extent anywhere in the master. This round gives it one. It must
  not be read as covering the **rules** vendoring — `sync_stratrules.py` into
  `Source/StratRules/` under `T-INT-01` — which is a different mechanism over
  different bytes under a different check.
- **"vendored"** — the master already rules (2026-08-06) that the word means one
  thing on both paths: bytes copied out of a named commit's object store into the
  UE project, gated for identity. **That ruling stands and this round does not
  touch it.** What is being stated is the *extent of one payload*, not the
  meaning of the word. Do not write anything that reads as splitting the word.
- **"the §4.8 tables"** are the three CSVs, and only those. The scenario file and
  the parity fixture travel the same path and **are not §4.8 tables**. Being
  carried makes none of them another. `T-DATA-05` asserts over the tables alone.
- **"kinds" and "files" are different counts.** Three kinds; five files. A
  sentence giving one without the other hides the distinction the round exists to
  make.

## 2. What travels the data path, measured

**2.1 From the script itself.** `sync_stratdata.py`, at the crew repo root,
declares three lists and vendors their concatenation:

| list | contents |
|---|---|
| `TABLES` | `units.csv`, `terrain.csv`, `effectiveness.csv` |
| `SCENARIOS` | `ferrum_crossing.json` |
| `FIXTURES` | `parity_fixture.save` |

It iterates `TABLES + SCENARIOS + FIXTURES` — **five files, three kinds**. The
"three kinds" framing is the script's own and is dated 2026-08-07 in its header.

**2.2 From the manifest it generates.** `Data/StratData.manifest.json` in the
Stratocracy UE project repo at `4ceaf93` records `sourcePrefix` `data/`,
`generator` `sync_stratdata.py`, `dataCommit`
`c2f58608c77c60c44e6c0fc87988bd3b372beaf5`, and a `files` map with a sha256 for
each of those five names and no others.

**2.3 What each non-table is for, and why it is not a table.** Both are imported
into **no** `UDataTable`, and `T-DATA-05` asserts nothing about either.

- `ferrum_crossing.json` is Stub 7's scenario file. It is carried because §4.9
  part 2's bridge loads the shipped scenario through `strat::loadScenario`, and
  `T-INT-02` requires the headless and in-engine replays to seed `GameState`
  from the same bytes.
- `parity_fixture.save` is the committed §4.10 save the editor pass replays — the
  subject of `T-INT-02` and of `T-SAVE-06`'s in-engine half. It is carried for
  the same reason: a fixture re-emitted on the engine side would compare the
  engine against itself. `GATE-REPLAY-FIXTURE` keeps it fresh at the source;
  `GATE-DATA-VENDOR` keeps this copy equal to that source.

**2.4 The vendor gate's extent.** Every file in the manifest's `files` map is
hash-checked by `GATE-DATA-VENDOR` **regardless of which kind it is**. The
manifest itself is the exception, and for a stated reason: it records
`dataCommit`, so it cannot be stored at that commit, and it is verified by
recomputation rather than by hash-match — the same discipline
`StratRules.manifest.json` is under.

**2.5 When the two non-tables joined.** Both on 2026-08-07. The fixture's script
change is crew `5c47cc1`, whose own subject reads *"Vendor the parity fixture: a
third kind on the data path"*; it changed `sync_stratdata.py` alone and touched
no file under `data/`, which is why it is not among the commits in §2.6.

## 3. The rule, and why it is true

**3.1 Every data-touching crew commit in the whole history to `c2f5860`:**
`c224825`, `9086d6a`, `862a225`, `c2f5860`. Measured with `git log -- data/`.

**3.2 Between the two vendorings the master pins, exactly one:** `c2f5860`,
changing exactly one file — `data/parity_fixture.save`, +153 / −48. The other
four files, the three CSVs among them, are byte-identical across `862a225` and
`c2f5860`.

**3.3 So the ruling holds under the five-file scope and fails under a
three-CSV one.** *This is the round's finding, and it is an inference from the
document's own wording rather than a measurement — here is the reasoning so it
can be checked:* `dataCommit` advanced because a vendored file changed; that file
is the fixture; the fixture is vendored; so "those bytes" must span it. Under a
reading where "those bytes" means the tables, the same advance is a
counterexample to "when and only when".

## 4. What the master says now

**4.1 The absences.** Measured newline-insensitively on `source/gdd.md`:
`three kinds` **0**, `five files` **0**, `sourcePrefix` **0**.
`StratData.manifest.json` occurs **once**, in §3, only to say where `dataCommit`
is recorded.

**4.2 The narrowing.** §4.9 describes the data side's payload as *"the §4.8 CSVs
into the UE project's data directory by `sync_stratdata.py` under
`GATE-DATA-VENDOR`"*. That sentence's own job is to distinguish the two vendoring
*mechanisms*, and it is right about that; what it gets wrong is the payload.

**4.3 The master already half-knows.** Two places corroborate the wider scope and
are useful ground rather than contradictions to repair:

- §3 states that `sync_stratdata.py` **carries the parity fixture** from
  `5c47cc1`.
- §3's list of known-bad inputs the suite was proven able to FAIL on includes
  *"an unrecorded file in the data directory (vendor only)"* — a
  **directory-scoped** check, not a table-scoped one.

## 5. Error species this round must not commit

1. **Do not restate the 2026-08-06 *vendored-means-one-thing* ruling as
   changed.** It is untouched. Only the extent of the data-side payload is being
   stated.
2. **Do not turn the scenario or the fixture into a §4.8 table.** Any sentence
   implying `T-DATA-05` covers either is false, and so is any sentence implying
   either is imported into a `UDataTable`.
3. **Do not narrow the gate.** `GATE-DATA-VENDOR` hash-checks all five
   regardless of kind; the manifest's own exemption has a stated reason and is
   not a gap.
4. **No finite present-tense claim about either repo's tree contents without a
   commit pin enclosing it.** Standing rule, carried from the last round.
5. **Never a count without its kinds.** "Five files" alone hides the distinction;
   "three kinds" alone hides the extent.

## 6. Scope

The candidate set is larger than the last round's. A mechanical sweep of
`source/gdd.md` for the round's subject returns **32 sentences**, of which **21**
state or depend on a scope for what is vendored or checked. **That is a candidate
set and not the scope** — it matches vocabulary, and the scope is the set of
sentences whose truth moves. Sweep independently; the master is **hard-wrapped**,
so a line-oriented sweep under-counts silently.

§3, §4.8 and §4.9 are all in the blast radius by the Director's ruling. Whether
anything else is, is for the author's sweep to establish rather than for this
block to assert.

## 7. What the author produces

An addendum at `sections/tech_vendor-scope.md`: exact **old → new** pairs against
the merged master, no section redrafted, each OLD copied byte-for-byte from
`source/gdd.md` and unique in it. The gate run id is `vendor-scope`.
