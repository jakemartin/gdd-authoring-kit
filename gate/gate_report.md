# Gate report — run `driver-built-5`

`source/MANIFEST.txt` present. `gdd.md` md5 `83fb9acbc19b8c6cb7adb037ea50d150`,
matching the md5 the draft names in its own preamble.
One section produced this stage: `sections/tech_driver-built.md`. Every other
file in `sections/` carries the applied-addendum banner and was not re-gated.

**Top-level verdict: PASS.** Zero violations.

---

## `sections/tech_driver-built.md` — PASS (0 violations)

### The `-4` violation — closed, and closed the way it was scoped

`driver-built-4` filed one `invented-fact`: the ruling picked up a second
qualifier, and the Grounding attributed both to the Director. The author took
the first of the two offered fixes — deletion rather than re-attribution.

**Pair 3's NEW block, the ruling as it now reads:**

> On that record the Director **ruled, 2026-08-02, that §4.4's week-1 goal
> "Playable via debug commands" is met at `9f87ecd`, in its current state** — a
> ruling on a judgement rather than a result any check produced: the artifact
> exists and the match does not.*

The `-4` clause "and a ruling on the artifact as it stands rather than on any
fuller sense of playability a turn loop would later satisfy" is gone, together
with the comma that joined it. What remains is the `-4` text minus that clause;
the sentence is still one clause about the ruling's kind, and the block is still
a single source line ending in the italic-closing `*`.

**Grounding, the replaced sentence:**

> The ruling carries **one** qualifier — *in its current state* — and that
> qualifier is part of the ruling as given rather than a softener added here.

That is a one-qualifier statement, and it names the qualifier the Director's
ruling actually carries. `fuller sense`, `two qualifiers` and `not any fuller
sense of playability` return **zero** matches anywhere in the file. The four
places the ruling is mentioned — preamble (line 20), pair 3's NEW block (line
95), Grounding (line 162), Open questions (line 175) — each state exactly one
qualifier and each attribute the ruling to the Director on 2026-08-02.

### Nothing else moved

The author reports touching two places. Checked against the `-4` report's
verbatim quotes and against `source/gdd.md` from scratch, not inherited:

- **The limits sentence is byte-identical to the text `-4` quoted.** It reads:
  "What there is no way to do is play a match: **no turn structure, no capture,
  no Fame, no production, no AI and no scenario file**, and the driver exposes
  none of it." All six of Fact F's items are present, in one bolded run, still
  immediately before the ruling. Nothing was thinned to buy the verdict.
- **The ruling still reads as a dated Director ruling**, not as a property of the
  artifact: "the Director **ruled, 2026-08-02, that …**", plus the explicit "a
  ruling on a judgement rather than a result any check produced". The deletion
  removed a gloss, not the attribution or the date.
- **Placement row 3 is unchanged** — "at its end, after §4.5's sentence — the
  ruling is its last sentence" — and is still mechanically sufficient to merge.
- **All four OLD anchors are unedited**, re-grepped as full escaped literals at
  this md5, not as prefixes.

### Mechanical half — re-verified, not inherited

| Pair | Anchor site | Matches |
|---|---|---|
| 1 | line 1466, `This draft stands at 2026-08-02 … whose parent is \`2fcbf32\`.` | exactly 1 |
| 2 | line 1466, `rows 4–8 hold no code … and since §4.11's` | exactly 1 |
| 3 | line 1466, `§4.5's *Specification outruns the build* … the arithmetic.*` | exactly 1 |
| 4 | line 1483, `*(Commit \`c224825\` is the head of \`main\`; …` | exactly 1 |

- **No placement collision.** Pairs 1, 2 and 3 occupy disjoint, strictly ordered,
  non-overlapping spans of source line 1466 — head, middle, tail — and pair 4 is
  on line 1483. Applicable in any order, as the Placement table claims.
- **No curly quotes or apostrophes.** `[""'']` returns zero matches in the draft.
- **No dead references.** `Row 2 is not green` resolves (line 2644); §4.5's
  *Specification outruns the build* row resolves (line 1537) and states **69**
  written IDs, **18** green at `c224825`, **51** unclosed; §2.6 is at line 199 and
  *the forecast the player sees is exactly what resolves* at line 207, quoted
  verbatim; §4.4's week-1 cell is line 1517 and is untouched; the paragraph pair
  4 edits already records "The `build/` directory is not tracked at all".
- **Sweep claims verified.** `selfplay|driver_main|Driver.h|Driver.good|stratocracy_debug`
  returns **1** matching line document-wide — line 1466, inside pair 2's OLD.
  `2fcbf32` matches two lines, 1466 and 1483, both wholly inside pairs 1 and 4's
  OLD text, so it leaves the document with them. `9f87ecd` is not yet in the GDD,
  as expected for a draft that introduces it.
- **Fences.** No NEW block contains a fenced block; three backticks is correct
  under Director ruling 3.
- **Path form.** Every path in every NEW block is written in full —
  `spec/driver_spec.md`, `cpp_reference/Driver.h`, `cpp_reference/Driver.good.cpp`,
  `cpp_reference/driver_main.cpp`, `cpp_reference/test_driver.cpp`, the seven
  `main()` sources, `cpp_reference/Move.h`, `cpp_reference/Combat.h`,
  `cpp_reference/Hex.h`, `cpp_reference/Data.h`, `data/units.csv`,
  `data/terrain.csv`, `data/effectiveness.csv`, `build/stratocracy_debug`. No
  prefix is left for the reader to distribute, and no `*.csv` glob merges.
- **Ruling 5 respected.** A backticked bare `*.h` matches exactly once in the
  whole document — §4.8's `Combat.h` at line 2440 — and no pair touches it. Pair
  3's `cpp_reference/Combat.h` is its own citation, not a repair of that line.
- **No stat-drift.** Seven `main()` definitions and their seven paths (Fact C);
  sixteen dispatched commands, enumerated and counted (Fact D2); `GATE-DRV-01..07`,
  7/7 under clang++ and MSVC (Fact E); 69 / 18 / 51 restated exactly as §4.5 has
  them and explicitly not moved; rows 4–8 hold no code and row 2 stays unflipped
  (Fact G, GDD lines 1477 and 2644). No number in the draft's prose differs from
  the GDD's, and no ledger row flips.
- **Extent, per ruling 4.** "the checks that compare a value compute their
  expectation by calling the module directly" is exactly Fact H's extent, and the
  Grounding names the five lines (93, 126, 152, 232, 168) that establish it. The
  command claim is scoped to "commands `cpp_reference/Driver.good.cpp` dispatches
  at that commit", and the Grounding separates it from §4.9's emitted `Repaired`,
  which pair 3 does not mention. §2.6's forecast line is claimed to hold
  "structurally at this surface", not generally.
- **No unverified-claim.** Every "landed" claim carries `9f87ecd` plus either a
  probed path (Fact B/B2) or the `GATE-DRV-01..07` result (Fact E).
- **No scope-breach.** All four pairs land in §3, the tech-director's lane, and
  §4.4 keeps its cell per ruling 1. No new work is proposed; Change requests and
  Handoffs are both correctly "None".
- **No kb-desync.** `kb_rules.md` is a parse of §2; `driver`, `forecast`,
  `c224825`, `9f87ecd` and `main()` all return zero hits there, and pair 3 quotes
  §2.6 without altering it.
- **No contradiction.** Pair 2 retires the "**unmet**" clause in the same
  paragraph in which pair 3 records the ruling, so the merged document never
  holds both; §4.4's cell states the goal and does not adjudicate it.
- **No voice-drift.** The NEW prose is declarative and present-tense, and the
  past tense on "ruled, 2026-08-02" matches the paragraph's other dated events
  ("added and gate-verified 2026-07-29", "week 1 closed two of the three").
- **No format-breach.** Placement, Grounding, Open questions, Change requests and
  Handoffs are all present; the numbered OLD/NEW pairs are the draft body, which
  is this kit's established addendum form.

---

## Verdict

**PASS.** The one violation from `driver-built-4` is closed by deletion, which is
the cleaner of the two fixes offered: the Director's ruling now appears with the
single qualifier it was given — *in its current state* — in all four places the
draft mentions it, and no authored gloss is filed on the Director's side of the
Grounding line. The two edits the author reports are the only two I can find: the
limits sentence is byte-identical to the text `-4` quoted, still carries all six
of Fact F's items, and still sits immediately before the verdict, and the ruling
still reads as a dated, attributed judgement rather than as a self-evident
property of the artifact. The mechanical half was re-run from scratch rather than
inherited — four OLD anchors matching exactly once each as full literals, no
curly characters, no dead references, no collision among the three pairs sharing
line 1466, no path abbreviated, no number moved, no ledger row flipped, no
kb-desync. Nothing is owed before merge: apply the four pairs at the placements
given, then update `../stratocracy-content/kb/rules.md` only if §2 moves for some
other reason — this draft does not move it.
