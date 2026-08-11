# FACTS — round `stamp-scope`

**Subject.** §3's provenance-ledger status block opens with a stamp that reads as
though it fixes a reading point for the block. The block outruns it, in both
repos.

> **Corrected 2026-08-10, gate run `stamp-scope` violation 3, marked beside the
> claim rather than over it: the block does not open with the stamp.** The block
> opens with the dated *Status: live tracker* preamble; the stamp sits inside it,
> beginning at character offset 218. Read this Subject line as *"§3's
> provenance-ledger status block carries a stamp"*. The rest of the sentence —
> that it reads as a reading point, and that the block outruns it — is unaffected,
> and F1's locator was correct.

## Pre-send pass — declared

Every fact below was re-measured in the unit the author will use it in. No fact is
written "at `<sha>`" bare. Material facts are separated from my justification.
Each quotation was checked for both of its claims — that the string exists, and
that it exists in the section attributed. Each fact is labelled MEASURED or
INFERRED, and **an INFERRED fact may not be promoted to a bare assertion.**

> **Corrected 2026-08-10, after gate run `stamp-scope`: this declaration was
> false when written.** The pass was declared complete without being run on F2,
> and the gate filed both of F2's defects — a quotation whose count belonged to a
> different string, and a claim about where the stamp sits. **A quotation carries
> a third claim this pass did not name: that any number attached to it is a count
> of the string as quoted.** Both defects are corrected in place below. The
> declaration is left standing so that what it certified, and did not, stays
> visible.

All measurements are against `source/gdd.md` md5
`1f27e981b623c7af2f6402d9a5b6a62b`, 3365 lines, byte-identical to the master at
sync time. String work is on a whitespace-collapsed copy, so a sentence that
wraps a line is still visible. The matcher was control-tested against a mutated
copy of the quotation (0 hits) before each count.

## F1 — the stamp. MEASURED

Exact text, occurring **once** document-wide:

> This draft stands at 2026-08-06, at commit [`c2edae0`](https://github.com/jakemartin/stratocracy-crew/commit/c2edae0) in the crew repo and at `fed8ae9` in the Stratocracy UE project repo.

It sits in **§3** by nearest preceding `## ` heading (`## 3. AI Architecture — how
AI agents are used (roles)`, line 1425).

## F2 — the unit it opens. MEASURED

The stamp opens a single physical line of **101,086 characters**, blank-line
delimited on both sides, containing no table pipe, no heading and no fence — the
italic *Status: live tracker* block immediately above §3's provenance-ledger
table.

> **Corrected 2026-08-10, gate run `stamp-scope` violation 3: the stamp does not
> open that line.** The line opens with the *Status: live tracker* preamble ending
> "(wk 1–3, §4.4)."; the stamp begins at character offset **218**. Every other
> measurement in this paragraph — the 101,086 characters, the blank-line
> delimiting, the absence of pipe, heading and fence — was re-measured and holds.

**`paragraph` is ambiguous in this round and must be disambiguated wherever it is
used.** The block's prose says *"recorded at the end of this paragraph"* **8**
times, and no blank line separates any of them from the block's end, so on the
physical reading all 8 resolve to the same point. Use *block* for the physical
line; where the prose sense is meant, say which paragraph.

> **Corrected 2026-08-10, gate run `stamp-scope` violation 4: the quotation and
> the count are of two different strings.** Measured document-wide at this md5:
> `recorded at the end of this paragraph` occurs **6** times, and
> `end of this paragraph` occurs **8**. The other two of the eight read
> *"counted at the end of this paragraph"* and *"has since been ruled, at the end
> of this paragraph"*. **The count of 8 belongs to `end of this paragraph`, and
> that is the string the disambiguation rests on.** The conclusion — that all
> sites resolve to one point on the physical reading — survives; the quotation as
> written did not.

## F3 — the block outruns both halves of the stamp. MEASURED

Every distinct 7-hex token in the block was enumerated: **37**. Each resolves in
exactly one of the two repos — none in both, none in neither. Each of the 11
below was checked to be cited as a commit at its first occurrence.

**11 of the 37 are not ancestors of the stamp half for their own repo, and each
was committed after it.** Measured per sha with `git merge-base --is-ancestor`.

Crew half — `c2edae0`, committed at 2026-08-06T20:02:59-04:00:

| sha | committed | occurrences in the block |
|---|---|---|
| `f5fdb69` | 2026-08-07T13:27:59-04:00 | 4 |
| `cb8e12b` | 2026-08-07T13:48:25-04:00 | 8 |
| `862a225` | 2026-08-07T14:26:36-04:00 | 2 |
| `5c47cc1` | 2026-08-07T15:33:05-04:00 | 2 |
| `9289c1d` | 2026-08-07T16:31:44-04:00 | 10 |
| `5072d10` | 2026-08-07T18:13:43-04:00 | 2 |
| `b5f524d` | 2026-08-08T23:19:20-04:00 | 5 |
| `c2f5860` | 2026-08-08T23:35:37-04:00 | 6 |
| `11ef8ce` | 2026-08-10T12:09:05-04:00 | 2 |

UE half — `fed8ae9`, committed at 2026-08-06T18:58:48-04:00:

| sha | committed | occurrences in the block |
|---|---|---|
| `0897cb5` | 2026-08-07T15:34:02-04:00 | 16 |
| `4ceaf93` | 2026-08-08T23:36:31-04:00 | 1 |

The most recent, `11ef8ce`, was committed four days after the stamp's date and on
the day these measurements were taken.

**Sufficiency.** The enumeration sees `\b[0-9a-f]{7}\b` tokens. A commit written
at another abbreviation length, or referred to without a sha, is outside what this
probe can see. **11 is a floor, not a ceiling**, and the same caveat applies to
F4.

## F4 — the complement. MEASURED

The other **26** tokens are ancestors of their own repo's stamp half. This is the
complement of F3 over the same probe and carries F3's floor/ceiling caveat.

## F5 — what this round does not reach. MEASURED under round `pinned-vs-since`, Q1

The stamp is **not** the enclosure for the §3 clause filed as exposed in
`OPEN_pinned-vs-since.md` — the clause whose verb is `are` and whose subject is
two `T-UI-` acceptance IDs. Repairing the stamp does not pin that clause. **That
clause is outside this round; do not edit it here.**

## F6 — not material. My justification, and not for the master

This round exists because Q1 measured that no commit-pinned record encloses that
clause, and identified the stamp as the only candidate encloser it could find.
**That reasoning is why the round is happening. It is not a fact about the game or
the build, and it must not be written into the GDD.**

## Forbidden species this round

The round's own subject names the first of these. Check your own draft against
them before you return it.

1. **A scope claim that reads wider than what was measured** — a sentence that
   appears to fix a reading point for text it does not cover. This is the defect
   being repaired; the repair is the first place to look for it.
2. **A claim whose truth depends on a landing, not enclosed by a commit-pinned
   record.** The standing subject of `OPEN_pinned-vs-since.md`.
3. **A closed list offered as sufficient** where only necessity was established.
   If your list is of necessary conditions, say so.
4. **"at `<sha>`" written bare.** Write *committed at* or *as read at* — the two
   say different things and the difference has already produced a wrong pair.
5. **A volunteered positive beside a true negative finding.** State the negative
   negatively and stop.

**This is not a list of approved phrasings and must not become one.** It bans
species; it supplies no vocabulary.

## What is not specified here

**The form of the repair is the author's to determine and the Director's to
rule.** This block names the defect and measures it. It does not say whether the
stamp should be re-pinned, re-scoped, split, or replaced, and it offers no
replacement sentence — the author measures the site and I am working from a
brief.
