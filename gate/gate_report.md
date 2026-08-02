# Gate report — run `compiler-gap-2` (re-gate of `compiler-gap-1`)

**Source of truth:** `source/gdd.md`, md5 `97ccf0e9cc8c3f72adfaca10bd42d862`,
per `source/MANIFEST.txt` (present; no `sync-missing`). The md5 the draft states
in its own header matches it byte for byte.

**Sections gated this stage:** one — `sections/tech_compiler-and-playable-gap.md`.
Every other file in `sections/` carries an `✅ APPLIED ADDENDUM — DO NOT
RE-APPLY` banner (spot-verified on the most recent, `sections/tech_week1-build.md`,
line 3) and is history, not this stage's output. None was gated.

**Top-level verdict: PASS.** Zero violations.

---

## `sections/tech_compiler-and-playable-gap.md` — PASS, 0 violations

### The clause that blocked `compiler-gap-1` — cleared

The prior run filed one `unverified-claim` against Pair 1's commentary for
claiming the gate *"has **always** detected one compiler"*, a history no cited
check reaches. The clause now reads, at lines 23–25:

> Documentation-only: the gate detected one compiler at both commits Fact A
> checks, `5ffa8d6` and `c224825`, so the old text understated it rather than
> describing a tooling change.

Fact A's bound:

> Verified byte-identical at `5ffa8d6` and `c224825` via
> `git show <commit>:crew/tools.py`. **Extent: two commits, not the whole
> history.**

The clause now names exactly the two commits the check covers, in the past
tense, and reaches no further. It also no longer contradicts the file's own
Grounding note (lines 114–116), which states the same bound. The standing
**Extent** ruling is satisfied.

### Independent re-sweep for absolutes of the same shape

Not taken on the author's report. Grepped the draft case-insensitively for
`always|never|whole history|since week|all four|every`:

- `always`, `never`, `whole history`, `since week` — **zero occurrences.**
- `every pair below uses three backticks` (line 7) — a claim about this file,
  true on inspection: all four pairs use three-backtick delimiters.
- `not under all four` (line 37), `would read as requiring all four` (line 62),
  `it does not require all four` (line 77) — all three are the *negative* of the
  overreach, which is the ruling, not a claim beyond it.
- `everything after it` (lines 89, 93) — this is the GDD's own wording inside
  the Pair 4 anchor and its NEW continuation, not a new claim.

No absolute in the file now exceeds a cited check.

### What the edit could have disturbed — re-verified

| Check | Result |
|---|---|
| `source/MANIFEST.txt` present | Yes; md5 in draft header matches |
| OLD anchors byte-exact | 4 / 4, unchanged |
| OLD anchors unique | 4 / 4, one match each |
| Curly quotes / smart punctuation | None |
| Placement collision | None |
| kb-desync | None |
| Fence rule | Satisfied |
| Path form | Satisfied |

**Anchors re-read at their lines in `source/gdd.md`, not taken from the prior
report:**

- **Pair 1** → lines 1582–1583, §4.7 head. Byte-exact. `engine dependencies,
  compiled by the same` returns **1** match document-wide.
- **Pair 2** → lines 2490–2492, §4.9 item 1. Byte-exact, including the short
  line 2491 (`lands — where the ``g++``/``clang++`` + ``python run.py`` gate`).
  `sources live canonically in the crew repo` returns **1** match.
- **Pair 3** → lines 2541–2542, T-INT-04 inside the §4.9 spec stub.
  Byte-exact. `T-INT-04  no engine deps` returns **1** match. The fence at
  lines 2527/2549 contains no backticks anywhere between them, so Pair 3's
  backtick-free NEW text is correct; its 12-space continuation indent matches
  T-INT-02's at lines 2536–2538, so it merges without reflowing the stub.
- **Pair 4** → line 1466, §3's italic *Status: live tracker* line. The fragment
  `What week 1 did **not** close is everything after it: rows 4–8 hold no code,`
  is byte-exact and returns **1** match. The NEW text rejoins the source line at
  `and since §4.11's critical path runs 1 → 3 → 4 → 5 → 6/8` without a seam.

**No NEW block, OLD anchor or placement row moved.** Confirmed rather than
assumed: all four OLD blocks still match `source/gdd.md` at the same four line
ranges the prior run recorded (1582–1583, 2490–2492, 2541–2542, 1466); all four
NEW blocks are unchanged in substance and still carry the three-backtick
delimiters the header claims; the four-row Placement table (lines 100–105) still
names §4.7, §4.9 item 1, §4.9 T-INT-04 and §3. The single edit is confined to
prose that does not merge.

**Curly quotes.** Grepped the draft for `[“”‘’—–]`. Every hit is an em dash or
an en dash (`4–8`, `1–3`), both of which match the GDD's own register; zero
smart quotes and zero smart apostrophes — `§4.4's` on line 93 uses a straight
apostrophe.

**Placement collision.** Pairs 2 and 3 are both in §4.9 and do not overlap:
line 2491 is prose above the spec stub, line 2542 is inside the fence that opens
at line 2527. No other stage produced a section, so no cross-file collision is
possible.

**kb-desync.** All four pairs land in §3, §4.7 and §4.9. `source/kb_rules.md` is
a parse of §2; grepped for `clang|g++|compiler|debug command|T-INT|run.py|main()|Playable`
— **zero occurrences**. `source/kb_setting.md` likewise zero. Nothing in the
knowledge base goes stale.

### The three Director rulings — still satisfied after the edit

**Ruling 1 (any ONE detected compiler).** `clang` occurs at exactly four lines
in `source/gdd.md`: 1483, 1582, 2491, 2542. Pairs 1–3 take the last three, which
are the three named sites. Line 1483 is §3's populated-rows paragraph, which
Fact B protects — the draft leaves it untouched and quotes it accurately
(*"on a live `g++`/`clang++` compile+run"*, *"under clang++ and MSVC both"*).
Pair 3's NEW states the semantics outright, as an acceptance ID must:
*"Any one of them compiling clean satisfies this invariant; it does not require
all four."*

**Ruling 2 (§4.4 stays a plan).** Confirmed by anchor line numbers, not by the
Placement prose: §4.4 spans lines 1513–1526 and no anchor falls inside it. §4.4's
week-1 cell (line 1517) is *quoted* by Pair 4 and not edited.

**Ruling 3 (the unmet goal, stated negatively).** Pair 4's NEW records the
negative and carries its extent on its face — *"at `c224825` five tracked
sources define `main()`"* — matching Fact C's stated extent. All five paths are
written in full per the path-form ruling. No compensating positive is
volunteered.

### Grounding claims re-checked against `source/gdd.md`

- `Playable via debug commands` — **1** occurrence, line 1517, inside §4.4's
  week-1 cell, exactly as the draft says.
- `selfplay`, `duel simulator`, `entry point` — **0** occurrences each
  (`self-play` with a hyphen occurs widely, but that is the balance-sim concept,
  not the file). So no other site in the document restates what Pair 4 corrects.
- `No pair touches §1, §2, §4.4, §4.5, §4.8, §4.11 or the Q register` — true by
  the anchor line numbers above.

---

## Verdict

**PASS.** The one violation `compiler-gap-1` filed is fixed and fixed in the
right place: Pair 1's commentary now bounds the gate's behaviour to `5ffa8d6`
and `c224825`, the two commits Fact A checks, and an independent sweep for
absolutes of the same shape — `always`, `never`, `whole history`, `since week` —
returns nothing anywhere in the file. The author's claim that no NEW block, OLD
anchor or placement row was touched is confirmed rather than accepted: all four
OLD anchors were re-read at lines 1582–1583, 2490–2492, 2541–2542 and 1466 and
are still byte-exact and still unique document-wide, the NEW blocks still carry
three-backtick delimiters over backtick-free content, the Placement table still
names four sites in three sections, and the file remains free of smart
punctuation, placement collisions and kb-desync. Nothing further is owed before
merge: the Director may apply all four pairs at the placements stated, then
rebuild `.pdf`/`.txt`, re-sync `../stratocracy-content/kb/rules.md`, and re-run
`python sync.py`.
