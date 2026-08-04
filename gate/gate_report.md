# Gate report — run `row8-2`

- **Master**: `source/gdd.md`, md5 `f5284420e237b1cbedbf3fd7d46f0988` (from
  `source/MANIFEST.txt`) — the same master `row8-1` gated. No re-sync intervened.
- **Sync**: `source/MANIFEST.txt` present. Three entries — `gdd.md`,
  `kb_rules.md`, `kb_setting.md`.
- **Top-level verdict**: **PASS**
- **Total violations**: **0**

---

## `sections/tech_row8-ui-binding.md` — **PASS**, 0 violations

### The two `row8-1` violations are discharged

**1. `contradiction` — the false existence claim is gone.**

The blocked sentence was:

> No scenario or save file's hash is affected while none exists.

It no longer appears anywhere in the file. The §4.10 change request's *Why*
column now reads:

> No save file carries a stale `stateHash`. `scenarioHash` is taken over
> scenario file content, which the §4.10 per-unit list never enters.

Both replacement claims were checked in the text that would falsify them, not
by assertion:

- *No save file carries a stale `stateHash`.* §4.10 is row 10, and §4.5's
  *Specification outruns the build* row states "the **16** in rows 8–10, which
  hold no code". §3's ledger carries no save/replay row at all — §4.11 calls
  row 10 a "*proposed* ledger row". No save artifact exists, so none carries a
  stale hash. True, and it no longer smuggles a claim about the scenario file.
- *`scenarioHash` is taken over scenario file content.* §4.7 Stub 7:
  "`scenarioHash    string  hash of the canonical serialization (fields in this
  order, hexes in canonical hex order)`", and, on `guidedOpening`, "Entries
  serialize in the module's side enumeration order, not authoring order, so the
  hash is content-only." That serialization is the **scenario file's** field
  list; §4.10's per-unit list `{id, side, hex, hp, isFlag, captureProgress,
  pendingBuilds}` is the `GameState` list and does not enter it. Appending the
  two turn flags to §4.10's state hash therefore cannot move
  `data/ferrum_crossing.json`'s hash. True.

The two reasons are now stated separately, which is what the ruling required:
the Director is told nothing exists **on one side** and the other side is
unaffected **for a different reason**. No new claim was introduced in making
the repair.

**2. `dead-reference` — Open question 1 now names its change request.**

Open question 1 now reads:

> If DONE follows that precedent, T-INT-05 needs the §4.9 T-INT-05 change
> request above; if DONE joins the snapshot, the snapshot stops being "produced
> by the rules module" alone.

"§4.9 T-INT-05" matches the fourth change-request row's *Existing §* cell,
`§4.9, T-INT-05`, and matches no other row — no CR row else names §4.9 or
T-INT-05. Open question 3's ordinal, "the second change request above", is
unchanged and still denotes the §4.7 Stub 8 Acceptance row correctly, with its
71 / 17 / 21 arithmetic. The two references can no longer collide.

### Verification of the "byte-identical" claim

There is no retained copy of the `row8-1` draft on disk and no shell available
to this gate, so a literal byte comparison was not possible and is not claimed.
The unchanged material was verified the stronger way instead — re-checked
against `source/gdd.md` in full, so that a silent change would have had to be
independently correct to survive:

- **Every passage the `row8-1` report quoted verbatim still matches the draft
  character for character** — the Acceptance-row *Current text* cell, the §4.9
  T-INT-05 *Current text* and *Proposed change* cells, and the unaltered second
  half of Open question 1.
- **The OLD block is still verbatim and still unique.** §4.7 Stub 8 lines
  2370–2371 read `per-unit  {id, side, unitId, hex, hp, hpMax, isFlag, hasActed,` /
  `           captureProgress}` — matching the draft's OLD including the nine-
  and twenty-space indents. `hasActed` occurs **once** in `source/`, at that
  site; `hasMoved` occurs **zero** times. The pair merges mechanically.
- **The build-order row is verbatim against §4.11 row 8** — `| 8 | UI binding
  (Stub 8) | 5, 7 (snapshot needs full state) | Contract + queries yes; widgets
  in-editor | T-UI-01..04 (**T-UI-03, 04 †**) + GATE-CAP-PARTIAL |`. No
  dependency, no † mark, no acceptance ID moves.
- **§4.5's counts are unmoved and the alternative arithmetic is right.** §4.5
  reads "**70** written acceptance IDs at this revision", "**20 IDs remain
  unclosed**", "the **16** in rows 8–10, which hold no code". A snapshot field
  name is not an acceptance ID, so 70 / 20 / 16 hold, and 71 / 17 / 21 is the
  correct alternative if the Director mints `T-UI-05`.
- **Change request 1's quotations hold.** §2.11.5: "When any unit is affordable
  and the factory has not built this turn, the factory tile shows a small
  `BUILD` pulse." §4.7 Stub 5 Inputs: "the per-factory record of builds taken
  this turn (T-TURN-10)". The snapshot's `per-hex {terrainId, owner}` carries no
  field that condition can read. Filed, not written — correct disposition.
- **Change request 3's remaining claims hold.** §4.10's per-unit hash list is
  quoted exactly; T-SAVE-06 is "stateHash stability … (asserted jointly with
  T-INT-02)"; §4.10 serializes "in a fixed field order".
- **Change request 4's claims hold.** §2.11.2's info panel shows "`ready` or
  `done` — the machine's DONE bit (§2.11.1)"; §2.11.1 states "DONE is this
  machine's own per-unit bit … and it is not the act flag"; Stub 8's fields are
  "read-only, produced by the rules module". T-INT-05 as written is indeed
  unsatisfiable for that one displayed value.
- **The NEW text's claims are grounded.** §2.1's core loop gives "two
  independent flags: at most one move and at most one act per unit"; Stub 5's
  Inputs give "TWO flags per unit, not one (T-TURN-01)"; §2.11.1 gives "Every
  surface in §2.11 that says a unit *has not acted* binds to the machine's bit".
- **The grounding list's cleared sites still hold, each re-checked in the
  binding text.** `captureProgress` against T-FAME-05 ("progress is tile-held and
  RESETS TO ZERO when the capturing Infantry leaves the hex or dies, and never
  transfers"); §3's quotation of the `match` line, not the `per-unit` line;
  GATE-CAP-PARTIAL's "adding no field and no numbered ID", whose subject is the
  gate; §2.10's row-8/row-7 dependency sentence and §4.11's `5, 7` cell;
  §2.11.1's machine entering SELECTED only "on own unacted unit" and relighting
  targets rather than reachable hexes in MOVED, so T-UI-02 is never raised for a
  spent move flag.
- **Open question 1's `guidedOpening` precedent is real.** §4.7 Stub 7:
  "marked/locked is presentation state, not rules state, so it stays out of the
  Stub-8 snapshot."
- **Open question 4's arithmetic is grounded.** §2.11.2 shows `+175/turn`; §2.7
  gives "+100 Fame/turn" per factory and "+25/turn" per town; T-UI-03 forbids
  widget-side arithmetic for "the live standings scoreboard" rows only, so the
  Fame rate is unruled rather than violated.
- **No `kb-desync`.** `source/kb_rules.md` and `source/kb_setting.md` contain no
  occurrence of `hasActed`, `hasMoved` or any snapshot text; the pair edits §4.7
  only, and §4.7 is not parsed into either file.
- **No `scope-breach`.** The handoffs name the three §2.11 sites and write none
  of them; the addendum flips nothing in §3, mints no acceptance ID, and leaves
  §3's UI row at `*pending*`.
- **The out-of-scope items remain correctly absent.** T-TURN-10's per-side-turn
  renewal boundary and the unconstrained command ordering are carried in §3 as
  rulings that arrived with the code; their absence here is not filed.
- **All five required headings are present** — Placement, Draft, Change
  requests, Open questions, Grounding. No `format-breach`.
- **No `placement-collision`.** One section this run, one pair, one site, and
  that site is not targeted by any other draft in `sections/`.

---

## Verdict

**PASS.** The two filed violations are discharged exactly, and the repair
introduced nothing. The §4.10 change request no longer tells the Director that
no scenario file exists — it now states the two independent reasons the append
is free, and both were verified in the text that would falsify them: §4.5 and
§4.11 put row 10 among the rows that hold no code, so no save file carries a
stale `stateHash`, and §4.7 Stub 7 makes `scenarioHash` a content-only hash of
the scenario file's own canonical serialization, which the §4.10 per-unit list
does not enter. Open question 1 now names the §4.9 T-INT-05 change request, a
label unique in the table, so it can no longer collide with Open question 3's
correct ordinal use. The byte-identity of the rest was not asserted on the
author's word: no prior copy exists to diff, so the whole draft was re-verified
against `source/gdd.md` claim by claim, and the OLD block, the build-order row,
the other three change requests, the four open questions, the handoffs and every
cleared grounding site all still hold against the same master md5. Nothing
blocks merge; the addendum's single pair may be applied at §4.7 Spec Stub 8's
`per-unit` line, and the four change requests and four open questions go to the
Director as filed.
