# Technical design — Q31 ruling, Stub 8 snapshot spec addendum (tech-director)

## Placement

Addendum against the merged master. Exact OLD/NEW pair only, scoped to §4.7
Spec Stub 8's per-factory field description — the one site inside that fenced
block where `Q31` and `AI-only path` occur. No other file, table row, or
section is touched.

---

## Draft

### Pair 1 — §4.7 Spec Stub 8, the `spawnBlocked`/`buildWaiting` field description

Replacement inside the fenced stub. The passage stated the waiting build as
an open question and an AI-only path; the Director's ruling on Q31 settles
both. `buildWaiting` and `spawnBlocked` already carry the distinction the
ruling needs — they were built distinct under **T-UI-05** for exactly this
case — so the amendment records the ruling as fact and states plainly that no
gate asserts a player-queued waiting build today, rather than reopening the
question.

**OLD**

```
Q31 asks whether a player may queue into a
                    boxed-in factory; `buildWaiting` is the field such a
                    ruling would bind to, and nothing here rules it — today
                    the waiting build is an AI-only path (Q31) and no gate
                    asserts a player-queued one.
```

**NEW:**

```
Q31 is RULED: the player may queue into a
                    boxed-in factory, reaching the same waiting-build state
                    the AI already reaches. `buildWaiting` is the field the
                    ruling binds to, and `spawnBlocked`/`buildWaiting` were
                    already built DISTINCT for exactly this case, under
                    T-UI-05 — no rebuild is needed for the ruling to hold.
                    The ruling changes what the GDD claims is reachable, not
                    the test suite: no gate asserts a player-queued waiting
                    build today, and none is written this round either.
```

---

## Checks

- The fenced Stub 8 block runs from the line opening `SPEC STUB 8: UI binding
  contract` to its closing fence. Within it, `Q31` occurs exactly TWICE —
  once in "Q31 asks whether a player may queue into a boxed-in factory..."
  and once in "...the waiting build is an AI-only path (Q31)" — and both
  occurrences sit inside the same `per-factory` field description edited
  above. `AI-only path` occurs exactly once, in that same passage — confirmed
  by a targeted grep bounded to that fence's line range (lines 2379–2547).
- Every other `Q31` occurrence in the master sits outside Stub 8: one in
  §2.7's Fame/build rules prose (*"Whether the player should be able to queue
  into a boxed-in factory is Q31"*), one in the §4.7 register's provenance
  chain (naming when Q31 was raised), one in the register's open/ruled tally
  paragraph (*"Q1, Q2, Q3, Q10–Q19, Q29, Q30, Q31 and Q32"*), and the Q31 row
  of the register table itself — four sites, none edited: the first is §2.7
  rules prose, the second and third are register apparatus, and the fourth is
  the table row — all explicitly out of scope this round.
- Document-wide, `Q31` therefore occurs six times total: two inside the Stub
  8 fence (both replaced by this pair's NEW text, which itself states the
  ruling once as `Q31 is RULED`) and four outside it (all left untouched).
- No code change is implied or requested. `Economy.h::queueBuild` already has
  no occupancy check; that is stated as an already-verified fact, not
  re-verified here.
- No new acceptance ID is minted and no existing one is touched. This pair
  does not move any §3 or §4.5 tally.

## Change requests

None. This round is a text-only ruling application inside material this
agent owns; no gap requires the Director's separate action beyond the Q31
ruling already given.

## Open questions for the Director

None raised by this pair. The ruling as given is sufficient to amend the
Stub 8 passage without inventing a new rule; whether a future round should
also add a headless acceptance ID for a player-queued waiting build (there is
none today) is a scheduling question, not a rule gap, and is left to the
build-order table rather than raised here.

## Handoffs

- §2.7's own Q31 sentence (*"Whether the player should be able to queue into
  a boxed-in factory is Q31"*) is rules-designer's prose and is not touched
  by this addendum; it will need its own amendment to state the ruling as
  settled, but that edit belongs to the section's owner.
- The §4.7 Q&A register's Q31 table row, its provenance-chain mention, and
  its open/ruled tally paragraph are register apparatus owned by other
  authors this round and are likewise left untouched here.

## Grounding

- The Director's ruling on Q31 (enable player queuing at a boxed-in factory;
  GDD-text-only, no code changes in scope; `Economy.h::queueBuild` already
  has no occupancy check) — Director's task message, this session.
- `buildWaiting` and `spawnBlocked` built DISTINCT for exactly this
  reachability case, under **T-UI-05** — `sections/tech_t-ui-05-built.md`,
  Pair 5 and Pair 15 (`spawnBlocked` is DECLARED DERIVED, occupancy alone;
  the two fields are distinct in the snapshot contract T-UI-05 gates).
- The exact OLD text, its location inside the Stub 8 fence
  (lines 2379–2547 of `source/gdd.md`), and its two `Q31` occurrences within
  that fence — `source/gdd.md` §4.7 Spec Stub 8, verified by grep bounded to
  the fence's line range.
- The four other `Q31` sites in the master and their ownership (§2.7 rules
  prose; the register's provenance chain; the register's open/ruled tally
  paragraph; the register table's Q31 row) — `source/gdd.md` §2.7 and §4.7,
  read and left unedited per this round's scope instruction.
- Master identity: `source/MANIFEST.txt`.
