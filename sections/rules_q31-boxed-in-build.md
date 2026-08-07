# Rules — Q31 ruling: player may queue at a boxed-in factory (rules-designer)

## Placement
Amends §2.7 (build-and-spawn bullet) and §4.7 (the Q&A register: Q31's row,
Q8's row, and the register's own open/ruled count paragraph). No new section;
this is a ruling addendum, applied as exact OLD → NEW pairs against
`source/gdd.md` / the master GDD.

## Draft

Director's ruling on Q31: **enable it.** The player may queue a build at a
boxed-in factory. The Fame commitment this prices (Q8(c): committed at queue
time, non-refundable) is shown before the click, same as any other build.
This closes no gate and mints no acceptance ID — no gate today asserts a
player-queued waiting build, and none is written this round. This is a
GDD-text-only ruling; §2.11.5's button-enable mechanics are the
`ux-onboarding-designer`'s text this same round and are cited here as ruled,
not restated.

Four sites in gdd.md stated the pre-ruling fact as present tense and are
corrected below: the §2.7 build-and-spawn bullet, the Q31 register row, one
stale sentence in the Q8 register row, and the register's own ruled/open
count paragraph (one of the document's two stated "extent-bearing sites",
§4.7 preamble commentary) — grepped document-wide for `Q31`, `boxed-in`,
`boxed in`, and `AI-only`; no other site in §2 or §4.7 makes the claim.

Two sites were found and deliberately **not** touched, per this round's
scope: §2.11.5's own widget/UI text (line ~704 of the master, "Build buttons
disable") and §4.7 Stub 8's snapshot spec prose (the `buildWaiting` /
`spawnBlocked` passage, which itself says "Q31 asks whether a player may
queue... nothing here rules it") — both belong to other authors this round
and are left for them to amend against this same ruling.

### P1 — §2.7 build-and-spawn bullet
TARGET: gdd

**OLD**
```text
  build for the turn. The **player cannot currently reach the waiting
  case**: §2.11.5 disables the Build buttons while a factory is boxed in, so
  for the player queue time and spawn time are the same instant, and the
  waiting build is an **AI-only path** today (§2.9 builds without the UI).
  Whether the player should be able to queue into a boxed-in factory is **Q31**
  (§4.7).
```

**NEW**
```text
  build for the turn. The player **can** reach the waiting case: §2.11.5's
  Build buttons stay enabled while a factory is boxed in (ruled this
  revision — Q31, §4.7), so a player may queue a build at a boxed-in
  factory exactly as at any other factory, with the Fame commitment this
  clause prices — **committed at queue time, not refundable** (Q8(c), §4.7)
  — shown before the click. The waiting build is no longer an AI-only path:
  player and AI alike can reach it, though no gate today asserts a
  player-queued one (Q31, §4.7).
```

---

### P2 — §4.7 Q31 register row
TARGET: gdd

**OLD**
```text
| **Q31** | Queuing a build at a boxed-in factory. §2.7 says a build that cannot spawn **waits**, and Q8(c) prices that wait as a non-refundable commitment — but §2.11.5 disables the Build buttons while a factory is boxed in, so the player can never create the state the clause prices. Should the buttons be enabled, with the commitment shown before the click, or is the waiting build correctly an AI-only path? | §2.11.5's Build-button rule; §2.7's waiting-build clause; Q8(c)'s commitment, which today binds only on ordinary player builds | §2.11.5 ships as written: Build is disabled while boxed in, so the waiting build is an **AI-only path** (§2.9 builds without the UI) and for the player queue time and spawn time are the same instant. No gate asserts a player-queued waiting build. Registered rather than assumed because Q8(c) ruled on a state the UI makes unreachable — the ruling stands, its player-facing half is simply not exercised yet. |
```

**NEW**
```text
| **Q31** | ~~Queuing a build at a boxed-in factory.~~ **RULED (this revision).** §2.7 says a build that cannot spawn **waits**, and Q8(c) prices that wait as a non-refundable commitment; §2.11.5 disabled the Build buttons while boxed in, so the player could not create the state the clause prices. Should the buttons be enabled, with the commitment shown before the click, or is the waiting build correctly an AI-only path? | §2.11.5's Build-button rule (amended this revision by the UX author to stay enabled while boxed in — cited here as ruled, its widget text not restated); §2.7's waiting-build clause; Q8(c)'s commitment, which now binds on a player-queued build the same as any other | **Ruled: enabled.** The player may queue a build at a boxed-in factory, with the Fame commitment this clause prices — committed at queue time, not refundable (Q8(c), §4.7) — shown before the click, same as any other build. §2.7's build-and-spawn bullet is corrected to match: the player-cannot-reach clause is retracted, and the waiting build is no longer stated as an AI-only path. **This ruling changes what the GDD claims about the Build button, not the test suite:** no gate today asserts or exercises a player-queued waiting build, and none is written this revision — the ruling mints no acceptance ID and moves no §4.5 count. |
```

---

### P3 — §4.7 Q8 register row, stale Q31-status sentence
TARGET: gdd

**OLD**
```text
Whether the Build buttons should be enabled while boxed in — and the commitment shown before the click — is registered as **Q31**, not assumed.
```

**NEW**
```text
Whether the Build buttons should be enabled while boxed in — and the commitment shown before the click — was registered as **Q31**, now **RULED: enabled**, with the commitment shown before the click (§4.7).
```

---

### P4 — §4.7 preamble, ruled/open count and list (an extent-bearing site the register's own text names)
TARGET: gdd

**OLD**
```text
moves on its account, and **T-CAP-05 closes there**, ruled
2026-08-04 (Q14). **Seventeen of the thirty-four rows are ruled; the other
seventeen remain open but *readable*** — Q1, Q2, Q3, Q10–Q19, Q29, Q30, Q31
and Q32 — each
```

**NEW**
```text
moves on its account, and **T-CAP-05 closes there**, ruled
2026-08-04 (Q14). **Eighteen of the thirty-four rows are ruled; the other
sixteen remain open but *readable*** — Q1, Q2, Q3, Q10–Q19, Q29, Q30 and
Q32 — each
```

---

## Change requests
| Existing § | Current text | Proposed change | Why |
|---|---|---|---|
| — | — | — | None. This is a Director ruling on an already-filed question; nothing here is a new proposal for the Director. |

## Open questions for the Director
None. Q31 is ruled; this addendum only carries the ruling's text consequences into the document.

## Handoffs
- **§2.11.5 widget/UI text** (the Build-button enable/disable behavior and its
  footer/tooltip copy) is `ux-onboarding-designer`'s to amend this round —
  found at the same "Boxed in — build waits for a free hex" passage this
  ruling makes stale, but its exact wording is UI prose, not rules prose, and
  I have not touched it.
- **§4.7 Stub 8's snapshot spec** (the `buildWaiting` / `spawnBlocked`
  passage that reads "Q31 asks whether a player may queue... nothing here
  rules it — today the waiting build is an AI-only path (Q31)") is
  `tech-director`'s schema prose. It states the same now-stale fact and
  needs the equivalent fix (drop "nothing here rules it" / "AI-only path",
  note Q31 ruled) but I have not touched it — it is explicitly out of scope
  for this round per instruction, and it is not §2 or the register table.

## Grounding
- Q8(c): Fame committed at queue time, non-refundable — §4.7 Q8 row (ruled),
  restated in §2.7's build-and-spawn bullet.
- §2.7's build-and-spawn bullet's existing text on spawn rules, the per-turn
  build limit, and the waiting-build slot — unchanged by this addendum,
  quoted only as anchor context in the OLD/NEW pairs.
- Q31's original question text and "Blocks" column contents — §4.7 Q31 row,
  reproduced in P2's OLD block.
- The "no gate asserts a player-queued waiting build" fact and "mints no
  acceptance ID" convention — matches this register's own stated convention
  for a ruling that changes GDD text without moving a §4.5 count (see Q29,
  Q33, Q34 rows, none of which mint an ID for a text-only ruling).
- The ruled/open row count (17/17 before, 18/16 after) and the open-row list
  — §4.7 preamble paragraph, arithmetic check: the prior list held 17 items
  (Q1, Q2, Q3; Q10–Q19 = 10; Q29, Q30, Q31, Q32 = 4; 3+10+4 = 17), and removing
  Q31 leaves 16 (3+10+3 = 16), with the ruled side moving 17 → 18.
- Task-provided facts taken as given, not re-verified by me: `Economy.h::queueBuild`
  has no occupancy check (stated as independently verified in the task); this
  ruling is GDD-text-only with no code change in scope.
