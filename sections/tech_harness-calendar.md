# Technical design — harness-calendar addendum (tech-director)

Exact OLD→NEW replacement pairs against `source/gdd.md`
(md5 `8491e0133cfa04207b909d29785397e0`). No section is redrafted.
This round moves no count, so there is no arithmetic section.

---

### Pair 1 — AD: the harness's calendar ownership (§4.4)

**OLD**
And because a gate that runs green over a subset is not a verified system, **no §3 ledger row flips on a partial pass** (Q29).

**NEW:**
And because a gate that runs green over a subset is not a verified system, **no §3 ledger row flips on a partial pass** (Q29).

**The in-editor Automation harness is deliberately not on this calendar (ruled 2026-08-06).** No cell above gives it a week — wk 3 names it among what `T-SAVE-06` and `T-INT-02` wait on, which is a blocker record rather than a goal cell — and §4.9 records it among what part 2 is blocked on and states that it is not scheduled there either. Both sections now decline it in the open, so the absence reads as a decision and not as an oversight. Among what stands between it and a cell: the harness by itself closes no acceptance ID (§4.9), so a week that added the runner and nothing else would close none, and the subjects the editor-pass IDs assert against besides it sit differently against this table. The widget work is scheduled here — wk 1's UMG widget skeletons, wk 2's select/move/attack wiring onto them. The wiring that submits commands is scheduled here too, in wk 2's `{Move, Attack}` and in the `Capture`, `Build` and `EndTurn` the wk-2 cell places in wk 3. An in-editor import step for the §4.8 tables has no cell; wk 1 names those tables inside the headless core. A `UENUM` mirror of the unit type is named in no cell. And a **vendored** replayer is held out rather than merely uncelled: §4.9 rules `Replay` out of vendoring until a bridge consumer exists, a condition no cell here dates — the *headless* replayer wk 2 schedules is a different artifact. None of those subjects exists at `a13626f` (§4.9), which is a claim about what is built and not about where this table puts it. When the harness does take a cell it takes it on the principle stated above: the week the thing that consumes it runs.

*Note.* Records in §4.4 that the harness is unscheduled by decision, and gives a per-subject disposition, non-exhaustively, of what stands between it and a cell.

---

### Pair 2 — AE: which parity-stub invariants need the §4.8 tables (§4.9 stub)

**OLD**
```
Inputs:  vendored StratRules sources + recorded source commit; a §4.10 replay
         file; the §4.8 tables imported in-editor.
```

**NEW:**
```
Inputs:  vendored StratRules sources + recorded source commit; a §4.10 replay
         file; the §4.8 tables imported in-editor — among this stub's
         invariants, T-INT-02 requires them (ruled 2026-08-06): it replays a
         command log in-engine to a canonical state hash, and the commands it
         applies resolve against the unit definitions the bridge maps from
         FUnitRow (part 2 above), the same stats the compiler-rounding
         tripwire in this invariant's own text runs through. T-INT-01 and
         T-INT-04 do not require them: a source-identity check, by whichever
         mechanism T-INT-01 puts on a given file, and a standalone compile
         load no unit definition. What T-INT-03 and T-INT-05 still need is
         assigned per ID above, and those are different subjects.
```

*Note.* Assigns the imported tables to `T-INT-02` on that invariant's own written text, non-exhaustively, and states which invariants do not need them.

---

### Pair 3 — AF: the runner's names (§4.9)

**OLD**
file there fails a green ID, confirmed against the running check, where an
extra `Sneaky.good.cpp` in that directory FAILs (§3).

**NEW:**
file there fails a green ID, confirmed against the running check, where an
extra `Sneaky.good.cpp` in that directory FAILs (§3). **Its names vary
across this document, and that variance is tracked here rather than being
drift (ruled 2026-08-06).** Among the forms this document uses for it are
*the editor pass*, *an in-editor Automation pass* and *an in-editor pass*,
and §3 records forms from the gate runner's printed output at named
commits — at `b23823f`, where the runner prints by name that no in-editor
Automation harness exists, and at `41a1452`, where the lines for the IDs
that did not run state that no in-editor pass exists at that commit. The
denotation is settled by the ruling above and does not turn on which form
a section reaches for. A rename would have to reconcile with those
commit-pinned §3 records and is deferred to its own round. **No name is
changed in this revision.**

*Note.* Records the naming variance as tracked and defers a rename, citing the denotation ruling already stated in this section.

---

## Check results

**Anchor uniqueness.** Each OLD anchor is unique in the file, probed full-file:
Pair 1 on "And because a gate that runs green over a subset is not a verified
system"; Pair 2 on "vendored StratRules sources + recorded source commit";
Pair 3 on "extra Sneaky.good.cpp in that directory FAILs". The phrase "the §4.8
tables imported in-editor" is not unique in the file, which is why the Pair 2
anchor carries the `Inputs:` prefix.

**Ruling AD — the §4.4 cells I read, subject by subject.** I read the wk-1
through wk-7 cells and the Q23/Q20 paragraph below the table.

- *Real Stratocracy widgets* — scheduled. Wk 1: "**UI-scaffolder agent starts
  UMG widget skeletons in parallel**". Wk 2: "Engine presentation + UI wiring
  (select/move/attack) onto the wk-1 skeletons". Pair 1 says the widget work is
  scheduled, which is what these cells say; it does not identify the skeletons
  with the assets §4.9 measured absent at `a13626f`.
- *The bridge's command surface* — scheduled. Wk 2: "**Week 2's command set is
  exactly `{Move, Attack}`**", with "`Capture`, `Build` and `EndTurn` … with
  §4.11 rows 4–5 in wk 3". Wk 3 also carries the phrase "command surface"
  itself, in the blocker note "Nor did `T-INT-03`: among what it waits on is
  the bridge's command surface, which is unbuilt (§4.9)" — a note about the
  unbuilt bridge rather than a name for the scheduled wiring.
- *DataTables imported in-editor* — wk 1 names "the §4.8 tables" inside
  "Headless C++ core — §4.11 **rows 1–3**", and wk 2 names "the one scenario
  loading, validating and rendering". Reading the cells, I found no in-editor
  import step among them.
- *A `UENUM` mirror of the unit type* — reading the cells, I found it named in
  none of them.
- *A vendored replayer* — held out by ruling with a stated condition, §4.9
  "`Replay` is ruled out of vendoring until a bridge consumer exists", rather
  than merely uncelled. Wk 2 schedules the *headless* replayer — "**and the
  §4.10 save/replay format + headless replayer** (Q20, ruled)" — which is a
  different artifact, and Pair 1 keeps the two apart by name.
- *Built state, separately from calendar state* — §4.9 reads "None of those
  subjects exists at `a13626f`, measured in the UE project repo there", over
  the same subjects. Pair 1 cites that for the built-state claim and states the
  calendar claim on its own.

Wk 3 names the harness in `T-SAVE-06`'s and `T-INT-02`'s blocker notes — "among
what it waits on are the in-editor Automation harness and a vendored replayer"
— so Pair 1 says no cell gives it a *week*, not that §4.4 fails to mention it.
Wk 4's "T-SAVE-07 (harness compatibility)" names the Balance self-play harness,
a different subject, and no pair touches it.

**Ruling AE — the invariant texts behind the requirement.**

- `T-INT-02` — "replay parity: the same command log replayed headless and
  in-engine (Automation test) produces the same final canonical state hash",
  with its tripwire naming "a compiler that rounds differently". Applying a
  logged command in-engine reaches the unit definitions §4.9 part 2 maps from
  `FUnitRow` to `strat::UnitDef`, and §4.1 states damage is a function of
  attacker/defender stats — the stats those definitions carry (§4.8 `Atk`,
  `Def`).
- `T-INT-01` — "source identity … A file that has a tracked counterpart at that
  commit must hash-match it. A file for which no such counterpart can exist
  must instead be recomputed from tracked inputs at that commit and equal the
  vendored bytes exactly", binding both mechanisms with "Neither mechanism may
  take its expectation from the vendored tree or from the vendoring script".
  Pair 2's gloss names the check by what it establishes, so it holds under
  either mechanism.
- `T-INT-04` — "no engine deps: StratRules compiles standalone under the
  existing python run.py gate … The gate run itself is the assert".
- `T-INT-03` and `T-INT-05` — Pair 2 makes no claim about whether they need the
  tables. §4.9 assigns `T-INT-03` "the **command surface**, which is part of
  the unbuilt bridge" and `T-INT-05` "**real Stratocracy widgets**", and
  assigns "**imported DataTables and a `UENUM` mirror of the unit type**" to
  `T-DATA-05`, an ID this stub does not carry. That list is introduced by
  "among what the remaining editor-pass IDs need besides it are", so Pair 2's
  requirement is additive to it.

## Change requests

| Existing § | Current text | Proposed change | Why |
|---|---|---|---|
| §4.11, row-2 note | "reached by the ordinary schedule, since the editor pass is not yet due, and not by the cut line firing" | Replace "since the editor pass is not yet due" with "since the editor pass has no week on §4.4's calendar by decision (§4.4), so nothing about T-DATA-05 is late" | Pair 1 does not change this sentence's truth value — §4.4 gave the pass no cell before this round either. But "not yet due" implies a due date on a calendar that §4.4 now says, in the open, it does not set. Flagging rather than editing, because the fix is a schedule claim outside this round's rulings and is the Director's to word. |

## Grounding

- Pair 1 anchor — §4.4, the Q23/Q20 paragraph at 1573. Its dispositions —
  §4.4's table, 1565–1568.
- "the harness by itself closes no acceptance ID" — §4.9, 2892–2893.
- "`Replay` is ruled out of vendoring until a bridge consumer exists" — §4.9,
  2878–2879; the same ruling at 2771–2783 and in §3.
- "None of those subjects exists at `a13626f`, measured in the UE project repo
  there" — §4.9, 2883–2889.
- Pair 2 anchor — §4.9's fenced stub, 2901–2902. Its requirement — `T-INT-02`,
  2914–2918. The mapping it reaches — §4.9 part 2 **Load**, 2835–2837. The
  stats that mapping carries — §4.8's unit schema, 2674–2686 (`Atk` 2679, `Def`
  2680), with §4.1's damage sentence at 1545. Its negative — `T-INT-01`,
  2904–2913, and `T-INT-04`, 2921–2925. The per-ID subjects it defers to —
  §4.9, 2877–2883.
- Pair 3 anchor — §4.9, 2896–2897. The denotation it cites — §4.9, 2871–2875.
  The printed-output records — §3, at `b23823f` and at `41a1452`.
- `UENUM` mirror of the unit type — §4.8, 2688; §4.9, 2882 and 2886.
- CR-1 — §4.11, 3101–3102.
