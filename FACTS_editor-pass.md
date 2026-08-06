# Round `editor-pass` — fact block

Everything below was verified this session against the merged master, the four
repos, or a measurement named with its instrument. Nothing here is inherited
from a briefing unchecked.

---

## 1. Repo state — commits and ancestry, never heads

Verified per repo with `git ls-remote`, and each working tree confirmed clean
and byte-equal to its own remote:

- `stratocracy-content` `main` — `1a41d26`
- `gdd-authoring-kit` `master` — `c7b87e6`
- `stratocracy-crew` `main` — `031ee20`
- `Stratocracy` `master` — `a13626f`

The master GDD's md5 is `e1d36927`, the LF/index one, reproduced with
`git show HEAD:<file>`. `source/gdd.md` is byte-equal to it, so what you read
is what is merged.

`rulesCommit` is **`e19605e`**. It is an **ancestor** of crew `031ee20`,
verified with `git merge-base --is-ancestor`; it is not that repo's head.

`gate/accept.json` records run `ue-harness-9`, PASS. Nothing is unmerged.

## 2. Measurements taken this session, each with its unit and instrument

**The engine build's language standard.** The UBT build that produced
`UnrealEditor-StratRules.dll` left one compiler response file per vendored
`.good.cpp` in the UE project's `Intermediate/Build` tree. All **ten** carry
`/std:c++20`. The complete set of non-path flags in those files is:

    /GR-  /TP  /experimental:log  /nologo  /sourceDependencies  /std:c++20  /wd5054

That enumeration is complete, so what it does not contain is settled by reading
it. No claim about conformance mode is available from it, and none may be
written.

**The standalone gate's language standard.** The crew repo's gate runner at
`031ee20` compiles with `-std=c++17` for GCC/Clang and `/std:c++17` for MSVC.

**Build settings.** Both target rules files in the UE project set
`DefaultBuildSettings = BuildSettingsVersion.V7`. That is the whole of what was
measured about build settings; the GDD already records V7 and the
shadow-variable consequence, and this round adds nothing to that record.

**`main()` census.** **15** tracked sources define `main()` in the crew repo at
`031ee20`, enumerated with `git grep -l` at that commit rather than by adding to
a remembered count. This round adds no harness and the figure does not move.

## 3. The three rulings

### Ruling AA — what "the editor pass" denotes

**"The editor pass" denotes the in-editor Unreal Automation harness. It is a
runner and nothing more.**

The subjects the IDs scheduled into it assert against — real Stratocracy
widgets, DataTables imported in-editor together with a `UENUM` mirror of the
unit type, a vendored replayer, the bridge's command surface — are **separate
requirements**, not contents of the pass. Running the pass supplies none of
them.

This is the reading the document already operates on: §4.9 states that the
harness is also not sufficient, and names each affected ID's own subject
individually. What the ruling changes is that the denotation is **stated once**
and the sites that currently reserve the question **cite that statement instead
of restating it** — the shape Ruling M used for the re-dating rule.

Which IDs run in the pass does not change. No ID's status moves.

### Ruling AB — a scheduled ID gets a stated disposition

**Every acceptance ID a §4.4 milestone cell schedules to close in a week gets a
stated disposition in that cell.**

A cell that schedules a set and then reports the outcome for part of it leaves
the rest claimed and unresolved. **A tally of how many remain is not a
disposition** and does not satisfy this ruling — a count cannot say which ID is
in which state, and it goes false the moment one of them moves.

### Ruling AC — the two "pure C++17" sites

**Both sites state the source constraint and both compile configurations.**

"Pure C++17" is a true claim about the sources as a base-spec constraint and it
stays. What is added is that the same certified bytes are compiled under two
different standard settings — the standalone gate's and the engine build's, the
measured values being in §2 above. This is the divergence surface §4.9 exists to
track, so it belongs where the constraint is stated rather than only in a
landing record.

No conformance-mode claim.

## 4. Register and arithmetic

**No register row is minted by this round.** Rulings K through Z minted none;
Q32 and Q33 registered text-versus-check gaps, and these three rulings are
document-truth repairs rather than gaps between a text and a running check.

**§4.5's 71 written / 61 green / 10 unclosed, and the 9 verified ledger rows,
are unmoved by all three rulings.** No acceptance ID is minted, closed or
re-opened. No ledger row is created, flipped or removed. If a pair you write
would move any of those figures, **stop and say so** rather than adjusting a
count to match.

## 5. Hard constraints

- **No repo but this one is edited.** The crew repo and the UE project repo are
  untouched this round. `ue_module/StratRules.Build.cs` in the crew repo
  contains the phrase "pure C++17" in a comment and is hash-matched by
  `T-INT-01`; editing it would re-date that ID's closure, and `T-INT-04`'s if a
  vendored source's bytes moved with it. Write no pair against any file outside
  the master GDD.
- **You do not edit the master GDD.** You write OLD/NEW pairs into your own file
  under `sections/`. The Director merges.
- **Nothing is invented.** Any number you state must already exist in
  `source/gdd.md` or be one of the measurements in §2. Anything else is a change
  request for the Director.
