# Round `editor-pass` — OLD/NEW pairs (tech-director)

Rulings AA, AB and AC. Nine pairs. Anchors are byte-exact against
`source/gdd.md` at md5 `e1d36927` (`source/MANIFEST.txt`), each verified unique
by a literal regex probe over the file — see **Checks**.

---

### Pair 1 — AA: the denotation, stated once, in §4.9

**OLD**

scheduled here. **It is also not sufficient**, and among what the remaining

**NEW:**

scheduled here. **What "the editor pass" denotes, stated once here and cited
elsewhere (ruled 2026-08-05): the in-editor Automation harness this paragraph
names. It is a runner and nothing more, and running it supplies none of the
subjects the IDs scheduled into it assert against — those are separate
requirements.** The harness is **also not sufficient**, and among what the
remaining

*Note.* This is where the denotation is stated; Pairs 2–4 cite it rather than
repeating it. The OLD is the whole of source line 2859; the NEW ends with
"remaining" so it rejoins the following line, which begins "editor-pass IDs
need besides it …". "It is also not sufficient" becomes "The harness is also
not sufficient" because the inserted sentences move the antecedent of "It";
"besides it" on the next line still resolves to the harness. No new name for
the runner is introduced — the NEW points at the name the paragraph already
uses.

---

### Pair 2 — AA: §3, row 10 part (b) landing record — cite, do not reserve

**OLD**

Whether *the editor pass* is meant to carry those subjects is **not ruled here**. **`T-SAVE-07` did not close:**

**NEW:**

Both what *the editor pass* denotes and what running it does not supply are stated at §4.9. **`T-SAVE-07` did not close:**

*Note.* A reserving clause replaced by a citation, per AA. Nothing measured in
this record changes: no commit, no acceptance ID and no ledger row is touched,
so the record's pin is undisturbed. The replacement asserts no definition of
its own — it names where the definition is.

---

### Pair 3 — AA: §3, row 10 part (c) landing record — cite, do not reserve

**OLD**

Whether *the editor pass* is meant to carry those subjects is **not ruled here**. `cpp_reference/selfplay.cpp` is untouched.

**NEW:**

Both what *the editor pass* denotes and what running it does not supply are stated at §4.9. `cpp_reference/selfplay.cpp` is untouched.

*Note.* Same shape as Pair 2, in the other §3 record that reserves the
question. Same wording deliberately, so this record and Pair 2's cite
identically.

---

### Pair 4 — AA: §4.11 row 10 cell — cite, do not reserve

**OLD**

Whether *the editor pass* is meant to carry those subjects is not ruled here (§3).

**NEW:**

Both what *the editor pass* denotes and what running it does not supply are stated at §4.9.

*Note.* The remaining site that reserves the question, per the AA sweep
recorded in **Checks**. Its old pointer was to §3, which reserved it too; the
pointer now goes to the statement.

---

### Pair 5 — AA: §4.5 equates acceptance IDs with "the editor pass"

**OLD**

T-INT-02, T-INT-03 and T-INT-05, the editor pass, for which no in-editor Automation harness exists

**NEW:**

T-INT-02, T-INT-03 and T-INT-05, which are scheduled into the editor pass (§4.9), and no in-editor Automation harness exists

*Note.* Filed beyond what AA, AB and AC name, because Pair 1 makes it false: an
appositive that equates acceptance IDs with the runner cannot stand once the
runner's denotation is fixed. The figure this clause sits inside is untouched,
and the clause's other content — that no in-editor Automation harness exists —
is preserved verbatim in meaning.

---

### Pair 6 — AB: §4.4 week 3 — a disposition per scheduled ID

**OLD**

**One still waits**: `T-SAVE-06`, on the in-editor Automation harness it is asserted jointly with `T-INT-02` on.

**NEW:**

`T-SAVE-06` did not close here: among what it waits on are the in-editor Automation harness and a vendored replayer, it being asserted jointly with `T-INT-02` (§4.9). `T-INT-02` did not close here either: among what it waits on are that harness and that replayer, `Replay` being ruled out of vendoring until a bridge consumer exists (§4.9). Nor did `T-INT-03`: among what it waits on is the bridge's command surface, which is unbuilt (§4.9). Nor did `T-INT-05`: among what it waits on are the real Stratocracy widgets it asserts against, measured absent at `a13626f` (§4.9).

*Note.* The week-3 cell schedules T-INT-02/03/05 and T-SAVE-01/03/05/06 on rows
4–5 and T-SAVE-02 on row 6, and separately schedules T-UI-05. It then reports
green for T-SAVE-01/02/03/05 and for T-UI-05, and reported what was left as a
tally. The tally is replaced by a disposition per ID: `T-SAVE-06`'s
tally-shaped outcome becomes a stated one, and `T-INT-02`, `T-INT-03` and
`T-INT-05`, which the cell scheduled without giving any outcome of their own,
now have one. Each disposition uses "among what it waits on", so none of them
goes false when a further blocker is found, and no cardinal replaces the one
removed. **Pair 9 is required with this pair**: the clause this cell opens with
asserts closure, in the indicative, of IDs this pair states did not close, and
the two cannot both stand.

---

### Pair 7 — AC: §4.7 head, the source constraint and the compile configurations

**OLD**

whichever one it found, not under all four. Where a stub needs a rule the GDD

**NEW:**

whichever one it found, not under all four. **"Pure C++17" constrains the
sources; it does not name a setting they are compiled under.** That standalone
gate at `031ee20` compiles at `-std=c++17` for GCC/Clang and `/std:c++17` for
MSVC, while the UBT build that produced `UnrealEditor-StratRules.dll` compiled
the same certified bytes at `/std:c++20` — the value carried by every compiler
response file that build left beside a vendored `.good.cpp`. That divergence is
what §4.9 exists to track. Where a stub needs a rule the GDD

*Note.* The OLD is the whole of source line 1633; the NEW ends with the same
words so it rejoins the following line, which begins "does not". The
"pure C++17" claim itself is unchanged and stays. Nothing is said about
conformance mode, and nothing is said about which configurations are the only
ones: the gate's settings and the engine build's are named, not enumerated as
a complete set.

---

### Pair 8 — AC: §4.9, the second "pure C++17" site

**OLD**

**no engine headers, no UObject, no third-party includes** — pure C++17 in
`namespace strat`, exactly the base-spec constraint. The standalone gate keeps
compiling the identical files, so "the engine build works" never substitutes
for "the gate passed."

**NEW:**

**no engine headers, no UObject, no third-party includes** — pure C++17 in
`namespace strat`, exactly the base-spec constraint. That constrains the
sources and not the setting they are built under: the standalone gate at
`031ee20` compiles at `-std=c++17` for GCC/Clang and `/std:c++17` for MSVC,
while the UBT build that produced `UnrealEditor-StratRules.dll` compiled the
same certified bytes at `/std:c++20` — the value carried by every compiler
response file that build left beside a vendored `.good.cpp`. That is the
divergence surface this section exists to track. The standalone gate keeps
compiling the identical files, so "the engine build works" never substitutes
for "the gate passed."

*Note.* The OLD spans source lines 2790–2793 including its line breaks and its
closing period inside the quotation marks. The section already records the UBT
build as adding "an MSVC compile through UBT, under the engine's own flags";
this adds the standard setting that build used, which that sentence does not
carry. AC asks both sites to state the constraint and the configurations, so
the repetition between Pairs 7 and 8 is the ruling rather than a drift risk.

---

### Pair 9 — AB: §4.4 week 3, the clause that asserts the closure Pair 6 denies

**OLD**

Rows 4–5 add precisely the three commands week 2 lacked, so the wk-2 gates re-run over the complete set and **close here**: T-INT-02/03/05 and T-SAVE-01/03/05/06 on rows 4–5, and T-SAVE-02 on row 6, whose determinism gate (T-AI-06) it composes.

**NEW:**

Rows 4–5 add precisely the three commands week 2 lacked, so the wk-2 gates re-run over the complete set, and **this week is where the schedule places their closure**: T-INT-02/03/05 and T-SAVE-01/03/05/06 on rows 4–5, and T-SAVE-02 on row 6, whose determinism gate (T-AI-06) it composes.

*Note.* Filed on the gate's finding. The clause carried no scheduling word, so
it asserted closure in the indicative for T-INT-02/03/05 and T-SAVE-06, in the
same cell in which Pair 6 states that each of them did not close. Recast, the
cell schedules and then reports, which is the shape the rest of the cell
already has. Only the verb moves; the ID list, the row attributions and the
T-AI-06 composition are byte-identical. The re-read this required is in
**Checks**.

---

## Checks

- Every OLD above was probed as a literal regex against `source/gdd.md`. Each
  returned exactly one occurrence, Pair 9's included. Pair 8's probe ran in
  multiline mode with its two internal line breaks written explicitly, since
  the anchor wraps.
- Pairs 1 and 7 anchor whole source lines (2859 and 1633 respectively), probed
  with `^…$`, so their boundary characters are settled by the line boundary
  rather than by a reader's rendering.
- **Week-3 cell re-read, whole, after drafting Pair 9.** The sentences that
  lean on the framing are the ones that report an ID as landing *before* its
  scheduled week — T-SAVE-07 "ahead of the wk-4 cell that scheduled it rather
  than behind it", and T-UI-05 "ahead of this cell rather than behind it".
  Both describe a cell that schedules, so recasting the opening clause into a
  scheduling claim leaves them true and removes the tension they previously
  sat in. The wk-2 cell's own "T-INT-01/04 and T-SAVE-04 close here, the rest
  do not" is a different cell about different IDs and is untouched. Nothing
  else in the week-3 cell turned up needing repair.
- Sweep for AA was run over the collapsed form, case-insensitively, with the
  pattern `editor[\s-]+pass` in multiline mode so a wrap between the two words
  could not hide a site. The census it returned was read hit by hit, and the
  paragraph around each was read through. Sites that schedule an ID into the
  pass (§4.8's and §4.9's and §4.10's Acceptance lines, §4.11's † bullets) and
  sites that say no pass exists at a commit are consistent with the denotation
  and are untouched. Three sites reserve the question and are Pairs 2–4; one
  site equates IDs with the runner and is Pair 5.
- Sweep for AB read all seven §4.4 milestone cells through. Week 2 names the
  IDs that close there and states that the others do not; weeks 4 and 5 state
  the disposition of what they name; weeks 1, 6 and 7 schedule no acceptance
  ID. Week 3 is the only cell that schedules IDs to close and leaves some
  without a disposition, and it is Pairs 6 and 9.
- Sweep for AC used `pure\s+C\+\+1?7|C\+\+\s*17|C\+\+\s*20|std:c\+\+|std=c\+\+`
  in multiline mode over the whole document. The phrase occurs at the two sites
  AC names and the document states no other language-standard value; those two
  are Pairs 7 and 8.
- A separate sweep for sufficiency phrasing (`still waits`, `only ID`,
  `remaining blocker`, `the only thing`, `is now the only`, `last thing`,
  `sole remaining`, `only remaining`) returned four hits. Two are outside these
  rulings and true as written (§2.13.1's measurement clause; §4.11 row 10's
  claim over that row's own closed ID set). One is §3's row-10 record, which
  already says "among what it still waits on are …" and needs nothing. The
  fourth is Pair 6.
- **Note sweep.** Every `*Note.*` block was read for cardinals, ordinals and
  "both", and each occurrence decided explicitly against one test: is the note
  asserting something about `source/gdd.md` that it has not measured? Those
  that were have been deleted; those kept are recorded in the report for this
  round with their grounding. The counts in this Checks section are check
  results and are unchanged.
- **Naming census — a string count and a reading, kept apart.** The table
  below answers only *how often a string occurs*. Surface: `source/gdd.md` as
  stored, at md5 `e1d36927`. Instrument: ripgrep in multiline mode,
  case-insensitive, counting **occurrences and not lines**; every inter-word
  space written `\s+` and the hyphen in `in-editor` written `-\s*`, so a line
  wrap at any interior word boundary still matches. All figures were measured
  under that one method, in one pass.

  | String | Pattern | Occurrences |
  |---|---|---|
  | `editor pass`, all forms, `in-editor` included | `editor\s+pass` | 25 |
  | `in-editor pass` | `in-\s*editor\s+pass` | 8 |
  | bare `editor pass` | the two rows above, 25 − 8 | 17 |
  | attributive `editor-pass` | `editor-\s*pass` | 1 |
  | `in-editor Automation harness` | `in-\s*editor\s+Automation\s+harness` | 14 |
  | `in-editor Automation pass` | `in-\s*editor\s+Automation\s+pass` | 3 |
  | `in-editor Unreal Automation parity pass` | `in-\s*editor\s+Unreal\s+Automation\s+parity\s+pass` | 1 |

  Under the same method `in-\s*editor\s+Unreal\s+Automation\s+pass` returns
  zero.

  **What a string count cannot answer.** A string can occur without naming the
  runner, so the second question — *does this occurrence name the runner?* —
  was answered by reading each occurrence in its own sentence, on the same
  surface, read rather than matched. **Among** what that reading found are
  occurrences naming the runner under `editor pass`, `in-editor pass`, the
  attributive `editor-pass`, `in-editor Automation harness` and `in-editor
  Automation pass`, which is what supports treating each of those as a name
  the document uses for it. That is not a claim about every occurrence of
  those strings, and one of them is a pair site: line 1585's `T-INT-02,
  T-INT-03 and T-INT-05, the editor pass` is counted under the first string in
  the table and is Pair 5's OLD anchor, the appositive Pair 5 exists to
  repair. The reading **excludes** `in-editor Unreal Automation parity pass`:
  its single occurrence is an appositive on an acceptance ID — "T-DATA-05, the
  in-editor Unreal Automation parity pass, has not run" — and §3 carries the
  parallel construction with a different noun, "T-DATA-05, the in-editor
  Unreal Automation half, which has not run", where the noun describes the ID
  rather than the runner. §4.8's Acceptance line schedules T-DATA-05 *in* the
  editor pass, and §4.11's cut-line bullet calls it "row 2's only in-editor
  half", both of which distinguish the ID from the pass. Read that way the
  occurrence is not a Pair 5 site, and no pair is filed for it.

  **Corrections recorded, all in this census.** An earlier version reported
  `in-editor Automation harness` as 4; that came from a literal-space,
  case-sensitive probe — a different instrument from the one used for the
  other figures — which missed occurrences broken by a line wrap and collapsed
  line 1514's several into one. The figure is 14. An earlier version also
  listed `in-editor Unreal Automation parity pass` as a spelling of the
  runner; that was a string match reported as a name, which the count could
  not establish either way, and the reading above is what settles it. An
  earlier version then said the retained spellings named the runner at *every*
  occurrence counted — a universal falsified by the file's own Pair 5 anchor,
  now replaced by the non-exhaustive statement above rather than by a narrower
  universal. No pair depends on any of the three.
- No figure the fact block pins as unmoved is touched by any pair: no
  acceptance ID is minted, closed or re-opened, no ledger row is created,
  flipped or removed, and no register row is minted.
- Each pair's whole enclosing passage was re-read after drafting. Pair 5 is
  what the first such re-read produced; Pair 9 is what the gate's finding and
  the second re-read produced.

## Change requests for the Director

1. **The runner is called several different things, and standardising wants
   its own round.** Ruling AA fixes what "the editor pass" denotes; it does
   not fix what the runner is called, and the document calls it by more than
   one name. Which spellings those are, on what surface, and by what reading
   each was established, are in **Checks** rather than restated here. I have
   introduced no new spelling and have not standardised the existing ones,
   because choosing among them is a Director call and because several of the
   sites sit inside pinned §3 records. A standardising round should handle
   those records deliberately.
2. **Pairs 2 and 3 edit §3 landing records.** They replace a reserving clause
   with a citation and change nothing that those records measure. Flagging it
   so the edit to a sealed record is a decision you make rather than one that
   arrives inside a batch.

## Grounding

- Ruling AA, AB, AC as stated — `FACTS_editor-pass.md` §3.
- The standalone gate's `-std=c++17` / `/std:c++17` at crew `031ee20`, the UBT
  build's `/std:c++20` in every response file left beside a vendored
  `.good.cpp`, and the completeness of that flag enumeration —
  `FACTS_editor-pass.md` §2.
- `source/gdd.md` md5 `e1d36927`, byte-equal to the merged master —
  `FACTS_editor-pass.md` §1 and `source/MANIFEST.txt`.
- Pair 1's site, and the fact that §4.9 already names each affected ID's own
  subject and states the harness is not sufficient — `source/gdd.md` §4.9,
  the "No further spec-stub pass is owed for part 2" paragraph.
- Pair 5's site — `source/gdd.md` §4.5, the "Specification outruns the build"
  risk cell.
- Pairs 6 and 9's site — `source/gdd.md` §4.4, the week-3 milestone cell, read
  in its pre-edit state for the dispositions Pair 6 supplies.
- Pair 6's dispositions: T-SAVE-06 jointly asserted with T-INT-02 and waiting
  on the harness and a vendored replayer, `Replay` out of vendoring until a
  bridge consumer exists; T-INT-03 waiting on the bridge's command surface;
  T-INT-05 waiting on real Stratocracy widgets, measured absent at `a13626f` —
  `source/gdd.md` §4.9. That T-INT-02/03/05 did not run for want of an
  in-editor Automation harness — `source/gdd.md` §4.11, row 9's paragraph.
- Pairs 7 and 8's untouched claims — the gate detecting one compiler per run
  (`source/gdd.md` §4.7 head, and T-INT-04 in §4.9's stub) and the UBT build
  adding an MSVC compile under the engine's own flags (`source/gdd.md` §4.9).
- The T-DATA-05 appositives that exclude `in-editor Unreal Automation parity
  pass` from the runner's names — `source/gdd.md` §3 (both constructions),
  §4.8's T-DATA set Acceptance line, and §4.11's cut-line bullet for
  T-DATA-05.
- The naming census — measured and then read this round against
  `source/gdd.md`; method, patterns, figures and the reading are in **Checks**.
