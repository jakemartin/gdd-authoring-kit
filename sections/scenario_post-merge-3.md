> # ✅ APPLIED ADDENDUM — DO NOT RE-APPLY
>
> Every replacement pair in this file **has been applied to the master GDD**, and
> the master has moved on since. Its Old blocks no longer match, so re-applying is
> a no-op at best; its quoted "current" text, register extents, and any hash it
> names are a **snapshot of the moment it was written**, not the current state.
>
> **The master GDD is the source of truth** — read `source/gdd.md`. Further changes
> to a merged section go in a *new* addendum file.

# Scenario & map design — post-merge-3 correction addendum (scenario-designer)

## Placement

Not a new section. **Six exact replacements inside already-merged text**, at
§2.13.1 (two prose sites), §2.13.5 (one table cell), §2.13.6 (one table cell),
and §4.7's Q24 row (two substrings). Every replacement is a correction to a
claim *about* the geometry. **No lane number, map layout, terrain count,
dimension, hex, factory/town count, match-length estimate or ρ moves.**

### Which of the four flagged sites I am replacing — read this before applying

The Director named four sites for Violation 1. I am replacing **three** of them
and **not** the fourth:

| Flagged site | Mine? | This addendum |
|---|---|---|
| §2.13.1 fact 1 | yes | **R1** |
| §2.13.5 Symmetry row | yes | **R4** |
| §4.7 Stub 7 `symmetry` field description | **no — `tech-director`** | **not replaced here.** Wording it needs is in **Handoffs**. |
| Q24 question text | yes (I filed it) | **R6a**, plus **R6b** on the same row's assumption column |

**Two further sites carry the same unqualified claim and were not flagged.**
Both are mine, both are in §2.13, and leaving either would re-open the same
`invented-fact` next run:

| Unflagged site | This addendum |
|---|---|
| §2.13.1's **Validation invariants** bullet — "because an odd-r rectangle has no mirror axis at any dimension" | **R3** |
| §2.13.6's Symmetry row — "the only symmetry an odd-r rectangle has" | **R5** |

Violation 2 is **R2** (§2.13.1 fact 2).

Total: **six replacements, R1–R6b.** Nothing outside them.

---

## Draft

### R1 — §2.13.1, fact 1 (Violation 1, primary site)

The derivation in the merged text is a *vertical*-axis argument and is correct
for the vertical axis. The headline generalised it to "any mirror axis," which
11 × 9 *Ferrum Crossing* — in this same document — refutes. Restoring the
qualifier, and stating the horizontal case rather than leaving it implied.

**OLD**

```
  1. **No odd-r rectangle has a mirror axis, at any dimension.** Even rows
     occupy columns 0…W−1 and are centred on (W−1)/2; odd rows sit ½ hex east
     and are centred on W/2. The centres differ by ½ hex for every W, so a
     single vertical axis cannot serve both parities. `mirror` is therefore
     not a declarable value (Q24, §4.7).
```

**NEW**

```
  1. **No odd-r rectangle has a *vertical* mirror axis, at any dimension —
     but one with an odd row count has a horizontal one.** Even rows occupy
     columns 0…W−1 and are centred on (W−1)/2; odd rows sit ½ hex east and
     are centred on W/2. The centres differ by ½ hex for every W, so a single
     **vertical** axis cannot serve both parities, at any dimension. The
     horizontal axis is a different question with a different answer:
     c ↔ c, r ↔ H−1−r is exact whenever H−1 is even — i.e. whenever **H is
     odd** — because r and H−1−r then share a parity, so every row keeps its
     ½-hex offset and no column moves at all. In axial it is one parity-free
     affine map, **μ(q, r) = (q + r − (H−1)/2, H−1−r)**, integer-valued
     exactly when H is odd. That is the precise complement of fact 2's
     even-row-count precondition, so an odd-r rectangle admits *at most one*
     of the two symmetries and its row parity chooses which: even H → 180°
     rotation, odd H → horizontal mirror, never both, never a vertical
     mirror. 11 × 9 *Ferrum Crossing* (§2.13.2) sits on a geometry that has
     such an axis and is deliberately not drawn to it (§2.13.4) — an
     asymmetry that is a design choice, not a geometric accident. Whether a
     horizontal `mirror` therefore becomes a declarable value alongside
     `rot180`, with an odd-row-count precondition, is open; no map in the set
     declares one today (Q24, §4.7).
```

### R2 — §2.13.1, fact 2 (Violation 2)

The conclusion (rotation valid iff H even) is verified and unchanged; only the
middle clause is rebuilt. The merged sentence paired the reflection `c ↔ W−c`
with the stranded column W−1. Those belong to different axis placements:
`c ↔ W−c` strands column 0, and the map that strands W−1 is `c ↔ W−2−c`. Both
now appear with their own stranded column, and the argument is stated as what
it actually is — one rigid motion forced to choose between two centres ½ hex
apart, breaking whichever parity it does not sit on.

**OLD**

```
  2. **An odd-r rectangle admits a 180° rotation only when the row count is
     even.** The rotation pairs row r with row H−1−r. With H odd those rows
     share a parity, and the even-row reflection (c ↔ W−1−c) and the odd-row
     reflection (c ↔ W−c) then demand two different centres — column W−1 of
     every odd row is left without an image. With H even the parities
     alternate and the board closes exactly under
     **ρ(c, r) = (W−1−c, H−1−r)**. This is why *Longwater March* is 13 × **8**
     and *The Causeway* is 9 × **8** rather than nine rows each.
```

**NEW**

```
  2. **An odd-r rectangle admits a 180° rotation only when the row count is
     even.** The rotation pairs row r with row H−1−r. With H odd those two
     rows share a parity, so each must land on a row carrying the same ½-hex
     offset — and a rotation is one rigid motion with one centre, while fact
     1 has just shown the two parities' centres differ by ½ hex. Put that
     centre on the even rows, at (W−1)/2, and every odd row reflects as
     c ↔ W−2−c, which sends column W−1 to column −1. Put it on the odd rows,
     at W/2, and every even row reflects as c ↔ W−c, which sends column 0 to
     column W. Either placement throws one column of every second row off the
     board. In axial the same fact is pure arithmetic: the rotation constant
     W − H/2 is a half-integer on odd H, so *no* hex has a hex image — on
     9 × 9 the constant is 4.5 and (1,1) rotates to column 6.5, which is why
     §4.7's T-SCN-09 refuses the file with a reason instead of reporting
     failed comparisons. With H even the parities
     alternate and the board closes exactly under
     **ρ(c, r) = (W−1−c, H−1−r)**. This is why *Longwater March* is 13 × **8**
     and *The Causeway* is 9 × **8** rather than nine rows each.
```

### R3 — §2.13.1, Validation invariants bullet (unflagged echo, mine)

**OLD**

```
  the check has no other place to run). The declarable values are
  **`rot180` or `none`** — `mirror` is not one of them, because an odd-r
  rectangle has no mirror axis at any dimension, and `rot180` is well-formed
  only on an **even row count** (see the symmetry note at the end of this
  section). Both constraints are pending Q24, §4.7.
```

**NEW**

```
  the check has no other place to run). The declarable values are
  **`rot180` or `none`** — `mirror` is not one of them, because no odd-r
  rectangle has a *vertical* mirror axis at any dimension and no map in the
  set is drawn to the *horizontal* one, which exists only on an odd row
  count (see the symmetry note at the end of this section); and `rot180` is
  well-formed only on an **even row count**. Both constraints are pending
  Q24, §4.7 — which now also asks whether the horizontal mirror is worth a
  third enum value, since it is available and merely unused rather than
  impossible.
```

### R4 — §2.13.5, *Longwater March* Symmetry row (flagged site 2)

Substring replacement inside the existing table cell; the rest of the row —
ρ(c, r) = (12−c, 7−r), the 4 MP lanes, the dial-under-test sentence — is
untouched. The withdrawal of *Mirrored* still stands, and now stands for the
reason that is actually true at 13 × 8: the vertical axis never exists, and
the horizontal one needs an odd row count, which this map does not have.

**OLD**

```
*Mirrored* was the earlier declaration and is withdrawn: no odd-r rectangle has a mirror axis (§2.13.1).
```

**NEW**

```
*Mirrored* was the earlier declaration and is withdrawn: no odd-r rectangle has a vertical mirror axis at any dimension, and the horizontal one exists only on an odd row count — this map is 8 rows (§2.13.1).
```

### R5 — §2.13.6, *The Causeway* Symmetry row (unflagged echo, mine)

Substring replacement inside the existing table cell; ρ(c, r) = (8−c, 7−r) and
the near-bridge/seat-swap argument are untouched.

**OLD**

```
Rotation is not a preference here but the only symmetry an odd-r rectangle has (§2.13.1); the row count is even so that it actually closes.
```

**NEW**

```
Rotation is not a preference here but the only symmetry available to an odd-r rectangle with an even row count — the vertical mirror exists at no dimension, the horizontal one only on odd H (§2.13.1); the row count is even so that the rotation actually closes.
```

### R6a — §4.7, Q24 row, question column (flagged site 4)

Substring replacement inside the Q24 cell. Escaped pipes preserved verbatim.
**This states the consequence and does not rule it** — the two options are
posed, neither is adopted, and the assumption column (R6b) records what stays
in force meanwhile.

**OLD**

```
but an odd-r offset rectangle has **no** mirror axis at any dimension, and admits a 180° rotation only when the row count is even. So `mirror` is a value the validator could never legally accept, and `rot180` is only well-formed against an even-H map. Narrow the field to `rot180 \| none` with an even-row-count precondition, and make `rot180` on an odd row count a hard refusal rather than a failed hex comparison?
```

**NEW**

```
but an odd-r offset rectangle has **no vertical** mirror axis at any dimension, and admits a 180° rotation only when the row count is even. So a vertical `mirror` is a value the validator could never legally accept, and `rot180` is only well-formed against an even-H map. It does, however, have a **horizontal** mirror axis (c ↔ c, r ↔ H−1−r) exactly when the row count is **odd** — the geometry the shipped 11 × 9 map sits on (§2.13.1 fact 1, §2.13.2) — so the field is a choice, not a forced hand. Two parts to one ruling. (a) Narrow the field to `rot180 \| none` with an even-row-count precondition, and make `rot180` on an odd row count a hard refusal rather than a failed hex comparison? (b) Or admit a **third** value for the horizontal mirror, with an odd-row-count precondition that refuses on even H exactly as `rot180` refuses on odd — and if so, is it spelled `mirror` or `mirrorH`, given that the bare word reads as the vertical axis, which is the one that is impossible here?
```

### R6b — §4.7, Q24 row, assumption column

**OLD**

```
If the Director rules otherwise, the only consequence is that a bad declaration surfaces as N failed hex comparisons instead of one refusal — no layout moves.
```

**NEW**

```
If the Director rules otherwise on (a), the only consequence is that a bad declaration surfaces as N failed hex comparisons instead of one refusal — no layout moves. `rot180 \| none` also holds against (b), but now on scope rather than on impossibility: no map in the set is drawn to a horizontal axis, so a third value would today be a slot nothing fills. Adding it later is purely additive — one enum value, one precondition, one further T-SCN-09 clause — and moves no layout either way.
```

---

## Change requests

| Existing § | Current text | Proposed change | Why |
|---|---|---|---|
| §2.13.1 fact 1 | "No odd-r rectangle has a mirror axis, at any dimension." | **R1** — restore the *vertical* qualifier; state the horizontal axis, its odd-H precondition, its axial form μ, and that the two symmetries are mutually exclusive by row parity. | The unqualified claim is false and 11 × 9 *Ferrum Crossing* is a counterexample in the same document. The derivation under it was always a vertical-axis argument. |
| §2.13.1 fact 2 | "…the odd-row reflection (c ↔ W−c) then demand two different centres — column W−1 of every odd row is left without an image." | **R2** — `c ↔ W−c` strands **column 0**; the map stranding W−1 is `c ↔ W−2−c`. Both now appear with the axis placement that produces them. | Self-contradictory as written. Conclusion (rotation iff H even) unchanged and independently re-verified. |
| §2.13.1 Validation invariants | "because an odd-r rectangle has no mirror axis at any dimension" | **R3** — same qualifier; reason for excluding `mirror` becomes "unused in this set," not "impossible." | Not flagged by the gate, same false claim, same lane. |
| §2.13.5 Symmetry row | "no odd-r rectangle has a mirror axis (§2.13.1)" | **R4** — qualifier plus the even-row-count reason that actually applies at 13 × 8. | The withdrawal of *Mirrored* is correct; its stated reason was not. |
| §2.13.6 Symmetry row | "the only symmetry an odd-r rectangle has" | **R5** — "…an odd-r rectangle **with an even row count** has." | Not flagged, same false claim, same lane. |
| §4.7 Q24 | "has **no** mirror axis at any dimension… Narrow the field to `rot180 \| none`…" | **R6a/R6b** — corrected premise; the third-option sub-question added; `rot180 \| none` stays in force on scope grounds, unruled. | The question was filed on a false premise, so it under-asks. Consequence stated, not ruled, per instruction. |

---

## Open questions for the Director

**No new Q number is filed, and Q1–Q25 is unchanged.** The correction does not
create a decision; it widens one that already exists. Q24 is exactly "what may
a scenario declare, and under what precondition" — the horizontal mirror is a
third candidate answer to that same question, so it belongs inside Q24 (R6a)
rather than as a Q26 that would have to be ruled in the same breath. If the
Director would rather have it as a separate row, **Q26** is the next free
number and R6a's clause (b) lifts out cleanly into it.

**The consequence, stated and not ruled.** `mirror` is no longer an
*undeclarable* value — it is an *unused* one. On odd-H maps the horizontal
mirror is a genuine isometry with an integer axial form, machine-verifiable by
exactly the T-SCN-09 machinery already specified for `rot180`, with the
precondition inverted (refuse on **even** H). So Q24's proposed `rot180 | none`
does not *need* a third option, but it can no longer be defended as the only
well-formed field. What holds it at two values today is scope: the shipped map
declares `none` and both stretch maps are 8-row and declare `rot180`. Cost of
adding the third value later is one enum value, one precondition and one
T-SCN-09 clause — no layout, no lane, no dimension moves under either ruling.

**One design consequence worth the Director's eye, no edit requested.**
§2.13.4's "that is what the asymmetric map buys, and why *Ferrum Crossing* is
not mirrored" is *strengthened*, not contradicted: at 11 × 9 (odd H) a
horizontal mirror was geometrically on the table and was not taken. Under the
old false fact that sentence was trivially true of any odd-r map; under the
corrected fact it records a real choice. I recommend leaving the line exactly
as merged — flagging it only so it is not mistaken for a seventh site.

---

## Handoffs

- **`tech-director` (§4.7 Stub 7, `symmetry` field).** Not mine to replace;
  being fixed in parallel. So the two do not diverge, the claim that needs the
  qualifier is: "*`mirror` is not a value, because no odd-r rectangle has a
  mirror axis at any dimension.*" The vertical qualifier is the fix, and the
  reason for the exclusion changes from **impossible** to **unused in this
  scenario set** — a horizontal mirror on odd H is well-formed and verifiable
  and would need its own precondition (refuse on even H) if ever admitted. My
  §2.13.1 (R1/R3) and Q24 (R6a/R6b) now read that way; Stub 7 is the only site
  left that will not.
- **`tech-director` (T-SCN-09), informational only.** No change requested this
  run. If Q24 later admits the horizontal mirror, the clause is the dual of the
  existing one: μ(q, r) = (q + r − (H−1)/2, H−1−r), integer-valued iff H is
  odd, verified over the same terrain + ownership + placement sets Q25 governs.
  I am not asking for it now — no map declares it.
- **`rules-designer`:** nothing. No rule, cost, Fame value or victory condition
  is touched.
- **`ux-onboarding-designer`:** nothing. §2.11.6-B's lane counts are unaffected
  — R1–R6b change no lane, no MP, no slack figure. §2.11.6-B's "stretch maps
  carry 2–4" is not mine and is untouched here.

---

## Grounding

- **The vertical impossibility (unchanged, R1 keeps it).** Even rows span
  x ∈ [0, W−1], centre (W−1)/2. Odd rows sit ½ east, span [½, W−½], centre
  W/2. Centres differ by ½ for every W. One vertical axis, two centres — no
  W makes them agree. This is the merged derivation, and it was always about
  the vertical axis only.
- **The horizontal availability (new in R1, and the counterexample the gate
  caught).** c ↔ c, r ↔ H−1−r preserves the ½-hex offset iff r and H−1−r
  share a parity, iff H−1 is even, iff **H is odd**. Axially, with
  q = c − ⌊r/2⌋: q′ = c − ⌊(H−1−r)/2⌋ = q + ⌊r/2⌋ + ⌈r/2⌉ − (H−1)/2 =
  q + r − (H−1)/2, integer iff H odd. Checked on the merged 11 × 9: (H−1)/2 =
  4, so (0,0) ↔ (0,8), (0,1) ↔ (0,7), and row 4 is fixed pointwise.
- **Mutual exclusion (new in R1).** Rotation needs H even (fact 2); horizontal
  mirror needs H odd (fact 1). No odd-r rectangle has both, and none has a
  vertical mirror. Row parity is therefore the symmetry dial: choosing 8 rows
  for *Longwater March* and *The Causeway* chose rotation, and choosing 9 for
  *Ferrum Crossing* left the mirror available and unused.
- **The stranded columns (R2).** Even-row axis at x = (W−1)/2 applied to an
  odd row: x′ = (W−1) − (c+½) = (W−2−c) + ½ → c′ = W−2−c, so column W−1 maps
  to −1. Odd-row axis at x = W/2 applied to an even row: x′ = W − c → c′ =
  W−c, so column 0 maps to W. Each axis breaks the parity it does not sit on.
  This matches the gate's finding exactly and keeps both cited maps.
- **The conclusion R2 preserves.** Rotation is valid iff H is even; ρ(q, r) =
  (W − H/2 − q, H−1−r); on odd H the constant W − H/2 is a half-integer, on
  9 × 9 it is 4.5 and (1,1) → column 6.5. Independently re-verified by the
  Director and by T-SCN-09's fixture text at §4.7 — unchanged here.
- **Nothing spatial moved.** *Ferrum Crossing* 11 × 9, 4 factories, 4 towns,
  5 units/side, 12–16 turns. *Longwater March* 13 × 8, 6 factories, 4 towns,
  16–20 turns, lanes 4/4. *The Causeway* 9 × 8, 4 factories, 2 towns, 8–12
  turns, lanes 3/3. Terrain counts, ρ pairings, bridge positions and the
  §2.13.7 summary table are all as gated — this addendum edits six claims
  about that geometry and none of the geometry.
