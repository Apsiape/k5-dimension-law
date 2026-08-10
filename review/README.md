# Review record — how this paper was refereed

**Redaction note, 2026-08-10.** The three review documents in this directory
were produced inside a private working repository. Filesystem paths,
repository-internal directory names, workspace locations and internal
organisational labels have been replaced
with bracketed placeholders such as `[private-workspace]` and
`[unrelated-work]`. Four substitutions were needed in total — one in
`REPAIR-LOG-R1.md` and three in `VERDICT-PAPER-BLIND-R2.md`;
`VERDICT-PAPER-BLIND-R1.md` required none. No word of any review's substance —
no finding, quotation, number, ruling or adjudication — was altered, added or
removed. Each file carries its own note in its header recording which case it
is.

---

## What is here

| file | what it is |
|---|---|
| `VERDICT-PAPER-BLIND-R1.md` | Blind round 1. Refutation-first referee report on the paper and its three engines. 26 findings (F1–F26): six blocking, eight should-fix, twelve hygiene. **Ruling: CONDITIONAL ON REPAIRS.** |
| `REPAIR-LOG-R1.md` | The repair round answering R1. Every finding answered in place, with three deviations from the referee's drafted repairs flagged `[DEVIATION]` and argued. **26 of 26 repaired, 0 dissents.** |
| `VERDICT-PAPER-BLIND-R2.md` | Blind round 2, the confirm round: an adversarial audit of the *repairs* rather than of the paper. Per-finding faithfulness table, adjudication of the three deviations, four new conditions (N-1…N-4), then an appended residual-confirmation section R2b. **Final ruling: PROMOTE.** |

Read them in that order. Together they are the complete refereeing history of
this result; nothing was withheld and no round was discarded.

## The protocol

The paper was refereed by rounds with three distinct jobs, held apart on
purpose.

**1. Blind, refutation-first rounds.** A referee receives the paper and the
engines as a self-contained package and is instructed to *break* the result,
not to assess whether it is publishable. The referee runs the engines, re-derives
the load-bearing numbers with an instrument of their own, reads the primary
sources against the paper's citations, and sweeps for prior art. Findings are
graded blocking / should-fix / hygiene and are written so that each one names
the exact quoted text it kills. A blocking finding is one a hostile reader could
quote verbatim against the paper.

The referee is required to supply, wherever possible, a **drop-in repair** — the
sentence or the code that would fix the finding. This is deliberate: it converts
"I don't believe this" into a testable claim about what the corrected paper
should say, and it lets the next round check whether the repair was executed
faithfully or quietly softened.

**2. Repair rounds.** Every finding is answered in writing, in one place, with
the outcome recorded as REPAIRED, DEVIATION or DISSENT. A **deviation** is a
repair implemented differently from the referee's draft; each is flagged, given
its reason, and must be argued to be *stronger or more accurate*, never weaker.
A **dissent** is a refusal to repair, and must be argued. Deviations and
dissents are not merged silently — they are handed to the next round to
adjudicate. In R1 there were three deviations and zero dissents; all three were
subsequently adjudicated SOUND, and on one of them (the relative deviations at
$N = 305$ and $N = 1292$) the repair round was right and the R1 referee was
wrong by a factor of 14. That is recorded here rather than smoothed away.

**3. Confirm rounds.** A second blind referee audits the *repairs*, not the
original paper. The question is not "is the paper good" but, finding by finding:
did the repair land, was it faithful, was it an overcorrection, did it introduce
new decay, and was any deviation from the drafted repair legitimate. The confirm
round independently re-runs the engines, re-derives the numbers with a **third**
method sharing nothing with either engine — in R2, $\sqrt5$ as a two-sided
rational bound from `math.isqrt`, fourth roots by bisection on `Fraction`s to 80
digits, no `Decimal`, no floating point in any load-bearing step, and the §4.3
transport reduction re-implemented from the paper's prose rather than from the
paper's engine — and re-audits every downstream site touched by a repair.

**Mutation testing.** A confirm round does not accept "the check passes" as
evidence that the check *tests* anything. Where a check is claimed to certify a
constant or a tolerance, the referee mutates the input to the value that ought
to fail and confirms the check actually fails on it. In R2 this is what caught
condition N-1: a printed constant wrong in its fifth significant figure
(`4.1226` for `4.1227`) that the existing check's tolerance was too loose to
see. The discharge of N-1 is recorded together with the mutation that
demonstrates the tightened check now fails on the old value.

**Freeze checks.** Each blind round opens by recording that the reviewed
directory is at a named, clean state, so that the object reviewed is
unambiguous and the review cannot be invalidated by concurrent edits. The
confirm round repeats the check after the repairs and reports exactly which
files moved.

## What the record shows

- 26 findings raised, 26 repaired, 0 dissents.
- 24 of 26 confirmed faithful on audit; one honest substitution (F26, an
  unreproducible citing-set sweep downgraded to disclosed supporting evidence
  rather than invented into a reproducible one); one softening reopened and
  closed.
- Zero missing, zero overcorrected.
- Four residual conditions raised in the confirm round, all four discharged,
  each verified — including by mutation where the condition was about a check's
  sensitivity.
- No arithmetic in the paper was found to be wrong in any round. What the rounds
  killed was the paper *misdescribing its own arithmetic and its own engines* —
  a false flatness claim, a cross-convention constant comparison, a check whose
  label promised more than it asserted, an engine test that did not test what
  the lemma claimed, and a stale comment shipped in an appendix.

The corrections that mattered are in the paper's final text, not hidden behind
it. The record of how they were found is this directory.
